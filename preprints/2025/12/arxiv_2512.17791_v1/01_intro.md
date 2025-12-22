---
authors:
- José E. Figueroa-López
- Ruoting Gong
doc_id: arxiv:2512.17791v1
family_id: arxiv:2512.17791
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Near-Maturity Asymptotics of Critical Prices of American Put Options under
  Exponential Lévy Models
url_abs: http://arxiv.org/abs/2512.17791v1
url_html: https://arxiv.org/html/2512.17791v1
venue: arXiv q-fin
version: 1
year: 2025
---


José E. Figueroa-López
Department of Statistics and Data Science, Washington University in St. Louis, St. Louis, MO, 63130, USA
[figueroa-lopez@wustl.edu](mailto:)
 and 
Ruoting Gong
Mathematical Reviews, American Mathematical Society, Ann Arbor, MI, 48103, USA
[rxg@ams.org](mailto:)

(Date: December 19, 2025)

###### Abstract.

In the present paper, we study the near-maturity (t→T−t\rightarrow T^{-}) convergence rate of the optimal early-exercise price b​(t)b(t) of an American put under an exponential Lévy model with a nonzero Brownian component. Two important settings, not previous covered in the literature, are considered. In the case that the optimal exercise price converges to the strike price (b​(T−)=Kb(T^{-})=K), we contemplate models with negative jumps of unbounded variation (i.e., processes that exhibit high activity of negative jumps or sudden falls in asset prices). In the second case, when the optimal exercise price tend to a value lower than KK, we consider infinite activity jumps (though still of bounded variations), extending existing results for models with finite jump activity (finitely many jumps in any finite interval). In both cases, we show that b​(T−)−b​(t)b(T^{-})-b(t) is of order T−t\sqrt{T-t} with explicit constants proportionality. Furthermore, we also derive the second-order near-maturity expansion of the American put price around the critical price along a certain parabolic branch.

KEYWORDS: American options, convergence rate, critical price, exponential Lévy models, near-maturity asymptotics

Mathematics Subject Classification (2010): 60F99 60G40 60G51 91G20

JEL Classification: C6

## 1. Introduction

It is generally recognized that the standard Black-Scholes option pricing model is inconsistent with options data, while remaining a widely used model in practice because of its simplicity. Exponential Lévy models provides a tractable extension of the classical Black-Scholes setup by allowing jumps in stock prices and heavy-tailed return distributions, while preserving the independence and stationarity of returns. We refer the readers to the monograph [[3](https://arxiv.org/html/2512.17791v1#bib.bib3)] for further motivations and literature on the use of jump processes in financial modeling. A large number of publications have been devoted to the pricing of European options under various Lévy-based models. In this paper, we revisit the problem of American put option pricing with finite maturity under general exponential Lévy models and, especially, on the study of the near-maturity asymptotics of the critical price (the exercise boundary) in this setting. No closed-form solution are known for American options and, as a result, numerical and approximation methods are employed in practice.

The near-maturity behavior of the critical price of the American put is well understood in the Black-Scholes model. In the pioneer work of Moerbeke [[9](https://arxiv.org/html/2512.17791v1#bib.bib9)], the near-maturity limit of the critical price for American call options is investigated, which can be easily transferred to American puts. Moreover, the conclusion in [[9](https://arxiv.org/html/2512.17791v1#bib.bib9)] suggests a parabolic behavior for the convergence rate without any restrictions on the model parameters. However, Barles et. al. [[1](https://arxiv.org/html/2512.17791v1#bib.bib1)] show that a parabolic behavior cannot occur in some situations. Indeed, they show that, in the absence of dividends,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→T−K−bBS​(t)σ​K​−(T−t)​ln⁡(T−t)=1,\displaystyle\lim\_{t\rightarrow T^{-}}\frac{K-b^{\text{BS}}(t)}{\sigma K\sqrt{-(T-t)\ln(T-t)}}=1, |  | (1.1) |

where TT is the maturity, KK is the strike price, σ\sigma is the volatility, and bBS​(t)b^{\text{BS}}(t) is the critical price at time tt. This asymptotic behavior remains valid when 0≤δ<r0\leq\delta<r, where δ\delta and rr denote the respective constant dividend and interest rates, and can be proved by the method of [[1](https://arxiv.org/html/2512.17791v1#bib.bib1)]. Lamberton and Villeneuve [[8](https://arxiv.org/html/2512.17791v1#bib.bib8)] provide the near-maturity behavior of the critical price for the cases r<δr<\delta and r=δr=\delta. More precisely, they show that the parabolic behavior stated by Moerbeke [[9](https://arxiv.org/html/2512.17791v1#bib.bib9)] holds in the case r<δr<\delta. They also prove that, when r=δr=\delta, the critical price satisfies the following estimate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→T−K−bBS​(t)σ​K​−(T−t)​ln⁡(T−t)=2.\displaystyle\lim\_{t\rightarrow T^{-}}\frac{K-b^{\text{BS}}(t)}{\sigma K\sqrt{-(T-t)\ln(T-t)}}=\sqrt{2}. |  | (1.2) |

The above results have been generalized to exponential Lévy models under various conditions. Let ν\nu be the Lévy measure of the underlying Lévy process XX, and let

|  |  |  |  |
| --- | --- | --- | --- |
|  | d:=r−δ−∫0+∞(ez−1)​ν​(d​z).\displaystyle d:=r-\delta-\int\_{0+}^{\infty}\big(e^{z}-1\big)\nu(dz). |  | (1.3) |

Note that in the Black-Scholes model, the quantity dd reduces to d=r−δd=r-\delta. Lamberton and Mikou [[5](https://arxiv.org/html/2512.17791v1#bib.bib5)] provide the near-maturity limits of the critical price of the American put for both the cases d≥0d\geq 0 and d<0d<0 (see Theorem [2.5](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") below). When XX has finite jump activity (i.e., ν​(ℝ\{0})<∞\nu(\mathbb{R}\backslash\{0\})<\infty or, equivalently, the process exhibits finitely many jumps on each finite time interval), and a nonzero Brownian component, the convergence rates of the critical price for all three cases d>0d>0, d=0d=0, and d<0d<0 have been fully studied by Bouselmi and Lamberton [[2](https://arxiv.org/html/2512.17791v1#bib.bib2)] (see also [[11](https://arxiv.org/html/2512.17791v1#bib.bib11)]). In the former two cases, they recover the same convergence rates as in ([1.1](https://arxiv.org/html/2512.17791v1#S1.E1 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([1.2](https://arxiv.org/html/2512.17791v1#S1.E2 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), respectively, while in the last case, they show that the critical price exhibits an analogous parabolic behavior to the Black-Scholes framework (see Theorem [3.1](https://arxiv.org/html/2512.17791v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1. Finite Jump Activity Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") below). When XX has infinite jump activity, Lamberton and Mikou [[7](https://arxiv.org/html/2512.17791v1#bib.bib7)] obtain the convergence rates of the critical price in the following scenarios with d>0d>0 (see Theorem [3.5](https://arxiv.org/html/2512.17791v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3. Infinite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") below):

* •

  XX is a pure-jump Lévy process with a jump component of finite variation;
* •

  XX has a nonzero Brownian component and a jump component of finite variation;
* •

  XX is a pure-jump Lévy process with tempered stable negative small jumps of infinite variation.

In particular, they recover the convergence rate ([1.1](https://arxiv.org/html/2512.17791v1#S1.E1 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) in the second case above.

In the present paper, we study the near-maturity convergence rate of the critical price of the American put under an exponential Lévy model with a nonzero Brownian component, which is arguably more relevant for financial modelling. Firstly, we consider the scenario of d>0d>0 without imposing any restriction on the jump activity of XX111Even though, by definition, d>0d>0 implies that the positive jump component of the process is of bounded variation., for which we recover the convergence rate ([1.1](https://arxiv.org/html/2512.17791v1#S1.E1 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), thus extending the corresponding results in [[1](https://arxiv.org/html/2512.17791v1#bib.bib1), [2](https://arxiv.org/html/2512.17791v1#bib.bib2), [7](https://arxiv.org/html/2512.17791v1#bib.bib7)] to exponential Lévy models with a possibly negative jumps of infinite variation. Our analysis combines a careful decomposition of the jump component of XX with a comparison argument between the European and American critical prices analogous to [[7](https://arxiv.org/html/2512.17791v1#bib.bib7)]. Secondly, we consider the case of d<0d<0 and assume that the jump component of XX is of finite variation, for which we obtain a parabolic behavior similar to those derived in [[2](https://arxiv.org/html/2512.17791v1#bib.bib2), [8](https://arxiv.org/html/2512.17791v1#bib.bib8)]. As a byproduct, we also derive the second-order near-maturity expansion of the American put price around the critical price along a certain parabolic branch.

The rest of the article is organized as follows. Section [2](https://arxiv.org/html/2512.17791v1#S2 "2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") provides preliminary definitions and properties of the American put option price and the corresponding critical price under an exponential Lévy model. Section [3](https://arxiv.org/html/2512.17791v1#S3 "3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") reviews some existing results on near-maturity asymptotics of the critical price which are related to our study. Sections [4](https://arxiv.org/html/2512.17791v1#S4 "4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") establishes the convergence rate of the critical price under an exponential Lévy model with a nonzero Brownian component and d>0d>0. Section [5](https://arxiv.org/html/2512.17791v1#S5 "5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") provides the convergence rate of the critical price under a similar model but with d<0d<0 and a jump component of finite variations. Some technical proofs are deferred to the appendices.

## 2. Setup and Preliminary Results

Throughout this paper, we consider a risky asset with price process S:=(St)t∈ℝ+S:=(S\_{t})\_{t\in\mathbb{R}\_{+}}, where ℝ+:=[0,∞)\mathbb{R}\_{+}:=[0,\infty), defined on a complete filtered probability space (Ω,ℱ,𝔽,ℙ)(\Omega,\mathscr{F},\mathbb{F},\mathbb{P}), where 𝔽:=(ℱt)t∈ℝ+\mathbb{F}:=(\mathscr{F}\_{t})\_{t\in\mathbb{R}\_{+}} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​e(r−δ)​t+Xt,t∈ℝ+.\displaystyle S\_{t}=S\_{0}\,e^{(r-\delta)t+X\_{t}},\quad t\in\mathbb{R}\_{+}. |  | (2.1) |

Above, r∈ℝ+r\in\mathbb{R}\_{+} is the interest rate, δ∈ℝ+\delta\in\mathbb{R}\_{+} is the dividend yield, and X:=(Xt)t∈ℝ+X:=(X\_{t})\_{t\in\mathbb{R}\_{+}} is a Lévy process with Lévy triplet (b,σ2,ν)(b,\sigma^{2},\nu).

###### Assumption 2.1.

Throughout we will always assume that XX satisfies at least one of the conditions in each of the following two categories:

* (i)

  σ≠0\sigma\neq 0, ν​((−∞,0))>0\nu((-\infty,0))>0, or ∫(0,1]z​ν​(d​z)=∞\displaystyle{\int\_{(0,1]}z\,\nu(dz)=\infty};
* (ii)

  σ≠0\sigma\neq 0, ν​((0,∞))>0\nu((0,\infty))>0, or ∫[−1,0)z​ν​(d​z)=∞\displaystyle{\int\_{[-1,0)}z\,\nu(dz)=\infty}.

###### Remark 2.2.

By [[14](https://arxiv.org/html/2512.17791v1#bib.bib14), Theorem 21.5], Assumption [2.1](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") implies that the trajectories of XX are neither almost surely increasing nor almost surely decreasing. This, together with [[3](https://arxiv.org/html/2512.17791v1#bib.bib3), Proposition 9.9], ensures that the exponential Lévy model ([2.1](https://arxiv.org/html/2512.17791v1#S2.E1 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) is arbitrage-free (or equivalently, the existence of martingale measures).

###### Assumption 2.3.

To guarantee that ℙ\mathbb{P} is a martingale measure for the discounted price process (e−(r−δ)​t​St)t∈ℝ+(e^{-(r-\delta)t}S\_{t})\_{t\in\mathbb{R}\_{+}} (or equivalently, (eXt)t∈ℝ+(e^{X\_{t}})\_{t\in\mathbb{R}\_{+}}), we impose the following two assumptions on XX:

|  |  |  |
| --- | --- | --- |
|  | (i)​∫1∞ez​ν​(d​z)<∞;(ii)​b=−σ22−∫ℝ0(ez−1−z​𝟏{|z|≤1})​ν​(d​z),\displaystyle\text{(i)}\,\,\,\int\_{1}^{\infty}e^{z}\,\nu(dz)<\infty;\qquad\text{(ii)}\,\,\,\,b=-\frac{\sigma^{2}}{2}-\int\_{\mathbb{R}\_{0}}\big(e^{z}-1-z{\bf 1}\_{\{|z|\leq 1\}}\big)\nu(dz), |  |

where ℝ0:=ℝ∖{0}\mathbb{R}\_{0}:=\mathbb{R}\setminus\{0\}.

In view of Assumption [2.3](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem3 "Assumption 2.3. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), we have the Lévy-Itô decomposition of XX as

|  |  |  |
| --- | --- | --- |
|  | Xt=σ​Wt+Lt:=σ​Wt−σ2​t2−t​∫ℝ0(ez−1−z)​ν​(d​z)+∫0t∫ℝ0z​N~​(d​s,d​z),t∈ℝ+,\displaystyle X\_{t}=\sigma W\_{t}+L\_{t}:=\sigma W\_{t}-\frac{\sigma^{2}t}{2}-t\int\_{\mathbb{R}\_{0}}\big(e^{z}-1-z\big)\nu(dz)+\int\_{0}^{t}\int\_{\mathbb{R}\_{0}}z\,\widetilde{N}(ds,dz),\quad t\in\mathbb{R}\_{+}, |  |

where W:=(Wt)t∈ℝ+W:=(W\_{t})\_{t\in\mathbb{R}\_{+}} is a standard Brownian motion, N​(d​s,d​z)N(ds,dz) is a Poisson random measure on ℝ+×ℝ0\mathbb{R}\_{+}\times\mathbb{R}\_{0} with intensity measure d​s​ν​(d​z)ds\nu(dz), independent of WW, and N~​(d​s,d​z):=N​(d​s,d​z)−d​s​ν​(d​z)\widetilde{N}(ds,dz):=N(ds,dz)-ds\nu(dz) is the compensated measure of NN.

Let Pe​(t,s)P\_{e}(t,s) and P​(t,s)P(t,s) be the respective time-tt risk-neutral prices of the European and American put options on SS, with strike K∈(0,∞)K\in(0,\infty) and maturity T∈(0,∞)T\in(0,\infty), namely,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Pe​(t,s)\displaystyle P\_{e}(t,s) | :=𝔼​(e−r​(T−t)​(K−s​e(r−δ)​(T−t)+XT−t)+),(t,s)∈[0,T]×ℝ+,\displaystyle:=\mathbb{E}\Big(e^{-r(T-t)}\big(K-s\,e^{(r-\delta)(T-t)+X\_{T-t}}\big)^{+}\Big),\quad(t,s)\in[0,T]\times\mathbb{R}\_{+}, |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(t,s)\displaystyle P(t,s) | :=supτ∈𝒯0,T−t𝔼​(e−r​τ​(K−s​e(r−δ)​τ+Xτ)+),(t,s)∈[0,T]×ℝ+,\displaystyle:=\sup\_{\tau\in\mathscr{T}\_{0,T-t}}\mathbb{E}\Big(e^{-r\tau}\big(K-s\,e^{(r-\delta)\tau+X\_{\tau}}\big)^{+}\Big),\quad(t,s)\in[0,T]\times\mathbb{R}\_{+}, |  | (2.3) |

where 𝒯u,v\mathscr{T}\_{u,v} denotes the collection of 𝔽\mathbb{F}-stopping times taking values in [u,v][u,v], for any 0≤u≤v0\leq u\leq v. Assumption [2.1](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") ensures that P​(t,s)≥Pe​(t,s)>0P(t,s)\geq P\_{e}(t,s)>0 for all (t,s)∈[0,T]×ℝ+(t,s)\in[0,T]\times\mathbb{R}\_{+}. Moreover, we define the European and American critical prices, respectively, as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | be​(t)\displaystyle b\_{e}(t) | :=inf{s∈ℝ+:Pe​(t,s)>(K−s)+},t∈[0,T],\displaystyle=\inf\big\{s\in\mathbb{R}\_{+}\!:\,P\_{e}(t,s)>(K-s)^{+}\big\},\quad t\in[0,T], |  | (2.4) |
|  | b​(t)\displaystyle b(t) | :=inf{s∈ℝ+:P​(t,s)>(K−s)+},t∈[0,T].\displaystyle=\inf\big\{s\in\mathbb{R}\_{+}\!:\,P(t,s)>(K-s)^{+}\big\},\quad t\in[0,T]. |  |

Clearly, b​(T)=be​(T)=Kb(T)=b\_{e}(T)=K. The following proposition summaries some regularity properties of PP (cf. [[3](https://arxiv.org/html/2512.17791v1#bib.bib3), Section 12.1.3], [[5](https://arxiv.org/html/2512.17791v1#bib.bib5), Proposition 3.2], [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Proposition 2.2], and [[11](https://arxiv.org/html/2512.17791v1#bib.bib11), Proposition 2.1]).

###### Proposition 2.4.

* (a)

  For each t∈[0,T]t\in[0,T], P​(t,⋅)P(t,\cdot) is nonincreasing and convex on ℝ+\mathbb{R}\_{+}, and satisfies

  |  |  |  |
  | --- | --- | --- |
  |  | |P​(t,s1)−P​(t,s2)|≤|s1−s2|,s1,s2∈ℝ+.\displaystyle\big|P(t,s\_{1})-P(t,s\_{2})\big|\leq|s\_{1}-s\_{2}|,\quad s\_{1},s\_{2}\in\mathbb{R}\_{+}. |  |
* (b)

  For each s∈ℝ+s\in\mathbb{R}\_{+}, P​(⋅,s)P(\cdot,s) is continuous and nonincreasing on [0,T][0,T].

It follows that (cf. [[5](https://arxiv.org/html/2512.17791v1#bib.bib5), Proposition 4.1] and [[11](https://arxiv.org/html/2512.17791v1#bib.bib11), Proposition 2.2]) the American critical price bb is nondecreasing on [0,T][0,T] and that

|  |  |  |
| --- | --- | --- |
|  | b​(t)∈(0,K),P​(t,b​(t))=K−b​(t),for any ​t∈[0,T).\displaystyle b(t)\in(0,K),\quad P\big(t,b(t)\big)=K-b(t),\quad\text{for any }\,t\in[0,T). |  |

Similar results holds for be​(t)b\_{e}(t) and Pe​(t,s)P\_{e}(t,s), namely, beb\_{e} is nondecreasing on [0,T][0,T] and

|  |  |  |  |
| --- | --- | --- | --- |
|  | be​(t)∈(0,K),Pe​(t,be​(t))=K−be​(t),for any ​t∈[0,T).\displaystyle b\_{e}(t)\in(0,K),\quad P\_{e}\big(t,b\_{e}(t)\big)=K-b\_{e}(t),\quad\text{for any }\,t\in[0,T). |  | (2.5) |

Moreover, since P​(t,s)≥Pe​(t,s)P(t,s)\geq P\_{e}(t,s) for all (t,s)∈[0,T]×ℝ+(t,s)\in[0,T]\times\mathbb{R}\_{+}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<b​(t)≤be​(t)<K,for all ​t∈[0,T).\displaystyle 0<b(t)\leq b\_{e}(t)<K,\quad\text{for all }\,t\in[0,T). |  | (2.6) |

We are interested in the near-maturity asymptotic behavior of b​(t)b(t) and P​(t,s)P(t,s), i.e., when t→T−t\rightarrow T^{-}. The following result provides the limit of the critical price near maturity (cf. [[5](https://arxiv.org/html/2512.17791v1#bib.bib5), Theorem 4.4]).

###### Theorem 2.5.

Let dd be defined as in ([1.3](https://arxiv.org/html/2512.17791v1#S1.E3 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). Then, the following assertions hold:

* (a)

  If d≥0d\geq 0, then we have

  |  |  |  |
  | --- | --- | --- |
  |  | b​(T):=limt→T−b​(t)=K.\displaystyle b(T):=\lim\_{t\rightarrow T^{-}}b(t)=K. |  |
* (b)

  If d<0d<0, then we have

  |  |  |  |
  | --- | --- | --- |
  |  | b​(T):=limt→T−b​(t)=ξ,\displaystyle b(T):=\lim\_{t\rightarrow T^{-}}b(t)=\xi, |  |

  where ξ\xi is the unique solution in (0,K)(0,K) to the following equation:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | r​K−δ​ξ−∫ℝ0(ξ​ez−K)+​ν​(d​z)=0.\displaystyle rK-\delta\xi-\int\_{\mathbb{R}\_{0}}\big(\xi e^{z}-K\big)^{+}\nu(dz)=0. |  | (2.7) |

###### Remark 2.6.

When d≥0d\geq 0, it is intrinsically assumed that

|  |  |  |
| --- | --- | --- |
|  | ∫0+∞(ez−1)​ν​(d​z)<∞,\displaystyle\int\_{0+}^{\infty}\big(e^{z}-1\big)\nu(dz)<\infty{\color[rgb]{1,0,0},} |  |

and, thus, this case intrinsically entails that the positive jump part of XX has finite variation.

## 3. The Known Cases of the Convergence Rate of the Critical Price

In this section, we review some known results on the asymptotic behavior of the critical exercise price bb as defined in ([2.4](https://arxiv.org/html/2512.17791v1#S2.E4 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) near maturity.

### 3.1. Finite Jump Activity Case

The following result is a combination of [[11](https://arxiv.org/html/2512.17791v1#bib.bib11), Theorem 4.2] and [[2](https://arxiv.org/html/2512.17791v1#bib.bib2), Theorems 3.2 & 4.1].

###### Theorem 3.1.

Assume that σ>0\sigma>0 and ν​(ℝ0)<∞\nu(\mathbb{R}\_{0})<\infty.

* (a)

  When d>0d>0, we have

  |  |  |  |
  | --- | --- | --- |
  |  | K−b​(t)∼σ​K​(T−t)​|ln⁡(T−t)|,t→T−.\displaystyle K-b(t)\sim\sigma K\sqrt{(T-t)\big|\ln(T-t)\big|},\quad t\rightarrow T^{-}. |  |
* (b)

  When d=0d=0, we have

  |  |  |  |
  | --- | --- | --- |
  |  | K−b​(t)∼2​σ​K​(T−t)​|ln⁡(T−t)|,t→T−.\displaystyle K-b(t)\sim\sqrt{2}\,\sigma K\sqrt{(T-t)\big|\ln(T-t)\big|},\quad t\rightarrow T^{-}. |  |
* (c)

  Suppose that d<0d<0. Let ξ\xi be given as in Theorem [2.5](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")-(b), and denote the local time of WW at x∈ℝx\in\mathbb{R} by LW​(x)L^{W}(x). For any λ,β∈ℝ+\lambda,\beta\in\mathbb{R}\_{+} and y∈ℝy\in\mathbb{R}, we define

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | vλ,β​(y):=supτ∈𝒯0,1W,N¯𝔼​(e−λ​τ​𝟏{N¯τ=0}​∫0τfλ​β​(y+Ws)​𝑑s+β​eλ​τ2​𝟏{N¯τ=1}​(LτW​(−y)−LT¯1W​(−y))),\displaystyle v\_{\lambda,\beta}(y)\!:=\!\!\sup\_{\tau\in\mathscr{T}\_{0,1}^{W,\overline{N}}}\!\mathbb{E}\bigg(e^{-\lambda\tau}{\bf 1}\_{\{\overline{N}\_{\tau}=0\}}\!\int\_{0}^{\tau}\!f\_{\lambda\beta}(y\!+\!W\_{s})\,ds+\frac{\beta e^{\lambda\tau}}{2}{\bf 1}\_{\{\overline{N}\_{\tau}=1\}}\!\Big(L\_{\tau}^{W}(-y)\!-\!L\_{\overline{T}\_{1}}^{W}(-y)\Big)\!\bigg),\,\, |  | (3.1) |

  where N¯:=(N¯t)t∈ℝ+\overline{N}:=(\overline{N}\_{t})\_{t\in\mathbb{R}\_{+}} is a Poisson process with intensity λ\lambda which is independent of WW, T¯1\overline{T}\_{1} is the first jump time of N¯\overline{N}, 𝒯0,1W,N¯\mathscr{T}\_{0,1}^{W,\overline{N}} is the collection of 𝔽W,N¯\mathbb{F}^{W,\overline{N}}-stopping times taking values in [0,1][0,1], and fa​(x):=x+a​x+f\_{a}(x):=x+ax^{+}. Let yλ,β:=−inf{x∈ℝ:vλ,β​(x)>0}y\_{\lambda,\beta}:=-\inf\{x\in\mathbb{R}:\,v\_{\lambda,\beta}(x)>0\}.

  + (c.1)

    If ν​({ln⁡(K/ξ)})=0\nu(\{\ln(K/\xi)\})=0, then we have

    |  |  |  |
    | --- | --- | --- |
    |  | ξ−b​(t)∼y0,0​σ​ξ​T−t,t→T−.\displaystyle\xi-b(t)\sim y\_{0,0}\sigma\xi\sqrt{T-t},\quad t\rightarrow T^{-}. |  |
  + (c.2)

    If ν​({ln⁡(K/ξ)})>0\nu(\{\ln(K/\xi)\})>0, then we have

    |  |  |  |
    | --- | --- | --- |
    |  | ξ−b​(t)∼yλ,β​σ​ξ​T−t,t→T−,\displaystyle\xi-b(t)\sim y\_{\lambda,\beta}\sigma\xi\sqrt{T-t},\quad t\rightarrow T^{-}, |  |

    with λ:=ν​({ln⁡(K/ξ)})\lambda:=\nu(\{\ln(K/\xi)\}) and β:=K/ξ​(δ+∫(ln⁡(K/ξ),∞)ez​ν​(d​z))\beta:=K/\xi(\delta+\int\_{(\ln(K/\xi),\infty)}e^{z}\nu(dz)).

### 3.2. Finite Variation Case

In this section, we consider in ([2.1](https://arxiv.org/html/2512.17791v1#S2.E1 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) a Lévy process XX with a finite variation jump component, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(−1,1)∖{0}|z|​ν​(d​z)<∞.\displaystyle\int\_{(-1,1)\setminus\{0\}}|z|\,\nu(dz)<\infty. |  | (3.2) |

In this case, the convergence rate of the American critical price is only known when d>0d>0.

For a pure-jump (σ=0\sigma=0) Lévy process XX, the following result is due to [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Theorems 5.1 & 5.2].

###### Theorem 3.2.

Assume σ=0\sigma=0 and that ([3.2](https://arxiv.org/html/2512.17791v1#S3.E2 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) holds true. Then, we have

|  |  |  |
| --- | --- | --- |
|  | limt→T−1T−t​(Kbe​(t)−1)=∫ℝ0(ex−1)−​ν​(d​x)andlimt→T−be​(t)−b​(t)T−t=0.\displaystyle\lim\_{t\rightarrow T^{-}}\frac{1}{T-t}\bigg(\frac{K}{b\_{e}(t)}-1\bigg)=\int\_{\mathbb{R}\_{0}}\big(e^{x}-1\big)^{-}\nu(dx)\quad\text{and}\quad\lim\_{t\rightarrow T^{-}}\frac{b\_{e}(t)-b(t)}{T-t}=0. |  |

Consequently, we have

|  |  |  |
| --- | --- | --- |
|  | limt→T−1T−t​(Kb​(t)−1)=∫ℝ0(ex−1)−​ν​(d​x).\displaystyle\lim\_{t\rightarrow T^{-}}\frac{1}{T-t}\bigg(\frac{K}{b(t)}-1\bigg)=\int\_{\mathbb{R}\_{0}}\big(e^{x}-1\big)^{-}\nu(dx). |  |

Next, we consider the case when XX has a non-zero Brownian component (i.e., σ>0\sigma>0). Let bBSb^{\text{BS}} be the American critical price under the Black-Scholes model. It was shown in [[1](https://arxiv.org/html/2512.17791v1#bib.bib1)] that, when d>0d>0 (which simply reduces to r>δr>\delta in the Black-Scholes model),

|  |  |  |  |
| --- | --- | --- | --- |
|  | K−bBS​(t)∼σ​K​−(T−t)​ln⁡(T−t),t→T−.\displaystyle K-b^{\text{BS}}(t)\sim\sigma K\sqrt{-(T-t)\ln(T-t)},\quad t\rightarrow T^{-}. |  | (3.3) |

The following result follows from [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Theorem 4.1 & Corollary 4.1].

###### Theorem 3.3.

Assume σ>0\sigma>0, d>0d>0, and that ([3.2](https://arxiv.org/html/2512.17791v1#S3.E2 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) holds true. Then, there exists C∈(0,∞)C\in(0,\infty) such that

|  |  |  |
| --- | --- | --- |
|  | 0≤b*BS*​(t)−b​(t)≤C​T−t,t→T−.\displaystyle 0\leq b^{\emph{BS}}(t)-b(t)\leq C\sqrt{T-t},\quad t\rightarrow T^{-}. |  |

Together with ([3.3](https://arxiv.org/html/2512.17791v1#S3.E3 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |
| --- | --- | --- |
|  | K−b​(t)∼σ​K​−(T−t)​ln⁡(T−t),t→T−.\displaystyle K-b(t)\sim\sigma K\sqrt{-(T-t)\ln(T-t)},\quad t\rightarrow T^{-}. |  |

### 3.3. Infinite Variation Case

In this section, we consider in ([2.1](https://arxiv.org/html/2512.17791v1#S2.E1 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) a Lévy process XX with an infinite variation jump part, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(−1,1)∖{0}|z|​ν​(d​z)=∞.\displaystyle\int\_{(-1,1)\setminus\{0\}}|z|\,\nu(dz)=\infty. |  | (3.4) |

In this case, the convergence rate of the American critical price is only known when d>0d>0 with some additional assumption on the negative jumps of XX. Note that when d>0d>0, in view of Remark [2.6](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), only the negative jump component of XX has infinite variation.

###### Remark 3.4.

When d≥0d\geq 0, it was shown in [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Theorem 6.1] that the convergence rate of b​(t)b(t) to KK cannot be linear for an infinite variation Lévy process XX (i.e., either σ>0\sigma>0 or ([3.4](https://arxiv.org/html/2512.17791v1#S3.E4 "In 3.3. Infinite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) holds). Indeed, in this case we have

|  |  |  |
| --- | --- | --- |
|  | limt→T−1T−t​(Kb​(t)−1)=∞.\displaystyle\lim\_{t\rightarrow T^{-}}\frac{1}{T-t}\bigg(\frac{K}{b(t)}-1\bigg)=\infty. |  |

The following result, due to [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Theorem 7.1], provides the convergence rate of bb when d>0d>0 and XX is a pure-jump Lévy process with infinite variation tempered stable negative small jumps.

###### Theorem 3.5.

Assume that σ=0\sigma=0, d>0d>0, and that there exist z0∈(−∞,0)z\_{0}\in(-\infty,0), a positive bounded Borel measurable function η\eta on [z0,0)[z\_{0},0) satisfying limz→0η​(z)=η0>0\lim\_{z\rightarrow 0}\eta(z)=\eta\_{0}>0, and α∈(1,2)\alpha\in(1,2), such that

|  |  |  |
| --- | --- | --- |
|  | 𝟏(z0,0)​(z)​ν​(d​z)=η​(z)|z|1+α​𝟏(z0,0)​(z)​d​z.\displaystyle{\bf 1}\_{(z\_{0},0)}(z)\,\nu(dz)=\frac{\eta(z)}{|z|^{1+\alpha}}{\bf 1}\_{(z\_{0},0)}(z)\,dz. |  |

Then we have

|  |  |  |
| --- | --- | --- |
|  | limt→T−K−b​(t)(T−t)1/α​|ln⁡(T−t)|1−1/α=K​(η0​Γ​(2−α)α−1)1/α.\displaystyle\lim\_{t\rightarrow T^{-}}\frac{K-b(t)}{(T-t)^{1/\alpha}\big|\ln(T-t)\big|^{1-1/\alpha}}=K\bigg(\frac{\eta\_{0}\,\Gamma(2-\alpha)}{\alpha-1}\bigg)^{1/\alpha}. |  |

## 4. New Results on the Convergence Rate of the Critical Price when d>0d>0

In this section, we consider the rate of convergence of bb near maturity when σ>0\sigma>0 and d>0d>0.

###### Theorem 4.1.

Assume that σ>0\sigma>0 and d>0d>0. Then we have

|  |  |  |
| --- | --- | --- |
|  | K−b​(t)=σ​K​−(T−t)​ln⁡(T−t)+O​(T−t),t→T−.\displaystyle K-b(t)=\sigma K\sqrt{-(T-t)\ln(T-t)}+O\big(\sqrt{T-t}\big),\quad t\rightarrow T^{-}. |  |

The proof of Theorem [4.1](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") follows a similar plan as in [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Sections 5 & 7]. Namely, we first characterize the rate of convergence of the European critical price (Proposition [4.4](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") below), and then, we proceed to estimate the difference between the European and the American critical prices (Proposition [4.9](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem9 "Proposition 4.9. ‣ 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") below).

To begin with, recalling that XX has a finite variation positive jump component when d>0d>0 (Remark [2.6](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we introduce the following decomposition of XX:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=XtW−t​∫ℝ0(ez−1)+​ν​(d​z)+Jt++Jt−,t∈ℝ+,\displaystyle X\_{t}=X\_{t}^{W}-t\int\_{\mathbb{R}\_{0}}\big(e^{z}-1\big)^{+}\nu(dz)+J\_{t}^{+}+J\_{t}^{-},\quad t\in\mathbb{R}\_{+}, |  | (4.1) |

where

|  |  |  |
| --- | --- | --- |
|  | XtW:=σ​Wt−σ2​t2,Jt+:=∫0t∫(0,∞)z​N​(d​s,d​z),Jt−:=∫0t∫(−∞,0)z​N~​(d​s,d​z)−t​∫−∞0(ez−1−z)​ν​(d​z).\displaystyle X\_{t}^{W}\!:=\sigma W\_{t}\!-\!\frac{\sigma^{2}t}{2},\,\,\,\,J\_{t}^{+}\!:=\!\!\int\_{0}^{t}\!\!\int\_{(0,\infty)}\!\!zN(ds,dz),\,\,\,\,J\_{t}^{-}\!:=\!\!\int\_{0}^{t}\!\!\int\_{(-\infty,0)}\!\!z\widetilde{N}(ds,dz)-t\!\int\_{-\infty}^{0}\!\!\big(e^{z}\!-\!1\!-\!z\big)\nu(dz). |  |

Clearly, XW:=(XtW)t∈ℝ+X^{W}:=(X\_{t}^{W})\_{t\in\mathbb{R}\_{+}}, J+:=(Jt+)t∈ℝ+J^{+}:=(J^{+}\_{t})\_{t\in\mathbb{R}\_{+}}, and J−:=(Jt−)t∈ℝ+J^{-}:=(J^{-}\_{t})\_{t\in\mathbb{R}\_{+}} are independent of each other. Note that for any p∈ℝ+p\in\mathbb{R}\_{+} (cf. [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Lemma 7.3]),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(ep​Jt−)=exp⁡(t​∫(−∞,0)(ep​z−1−p​(ez−1))​ν​(d​z)),t∈ℝ+.\displaystyle\mathbb{E}\big(e^{pJ\_{t}^{-}}\big)=\exp\bigg(t\int\_{(-\infty,0)}\big(e^{pz}-1-p(e^{z}-1)\big)\nu(dz)\bigg),\quad t\in\mathbb{R}\_{+}. |  | (4.2) |

The following lemma characterizes the small-time behavior for a Lévy process with σ>0\sigma>0 and a finite variation positive jump component,
the proof of which is deferred to Appendix [A](https://arxiv.org/html/2512.17791v1#A1 "Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models").

###### Lemma 4.2.

Assume that σ>0\sigma>0 and d>0d>0, then Xt/t⟶𝔇σ​W1X\_{t}/\sqrt{t}\;{\stackrel{{\scriptstyle\mathfrak{D}}}{{\longrightarrow}}}\;\sigma W\_{1}, as t→0+t\rightarrow 0^{+}.

###### Remark 4.3.

Lemma [4.2](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") is valid regardless of the value of dd. Indeed, in the proof of Theorem 8.1-(ii) in Sato [[14](https://arxiv.org/html/2512.17791v1#bib.bib14)], it is shown that for any infinitely divisible distribution μ\mu with Gaussian component σ2∈[0,∞)\sigma^{2}\in[0,\infty), it holds that (see p. 40 in [[14](https://arxiv.org/html/2512.17791v1#bib.bib14)])

|  |  |  |
| --- | --- | --- |
|  | lims→∞s−2​ln⁡μ^​(s​z)=−12​σ2​z2,z∈ℝ,\displaystyle\lim\_{s\rightarrow\infty}s^{-2}\ln\widehat{\mu}(sz)=-\frac{1}{2}\sigma^{2}z^{2},\quad z\in\mathbb{R}, |  |

where μ^\widehat{\mu} denotes the characteristic function of μ\mu. Taking t=1/s2t=1/s^{2}, it follows that

|  |  |  |
| --- | --- | --- |
|  | limt→0+t​ln⁡μ^​(z/t)=−12​σ2​z2,z∈ℝ.\displaystyle\lim\_{t\rightarrow 0^{+}}t\ln\widehat{\mu}(z/\sqrt{t})=-\frac{1}{2}\sigma^{2}z^{2},\quad z\in\mathbb{R}. |  |

Now, let μ\mu be the distribution of X1X\_{1}, then the distribution of XtX\_{t} is μt\mu^{t} due to the infinite divisibility, meaning that its characteristic function is given by μ^t\widehat{\mu}^{\,t}. Hence, we obtain that

|  |  |  |
| --- | --- | --- |
|  | limt→0+𝔼​(ei​z​Xt/t)=limt→0+(μ^​(z/t))t=e−σ2​z2/2,z∈ℝ,\displaystyle\lim\_{t\rightarrow 0^{+}}\mathbb{E}\big(e^{izX\_{t}/\sqrt{t}}\big)=\lim\_{t\rightarrow 0^{+}}\big(\widehat{\mu}(z/\sqrt{t})\big)^{t}=e^{-\sigma^{2}z^{2}/2},\quad z\in\mathbb{R}, |  |

and, thus, the result of Lemma [4.2](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models").

We are now ready to prove Theorem [4.1](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"). The proof is divided into two steps which are presented in the following two subsections, respectively.

### 4.1. Step 1: The rate of convergence of be​(t)b\_{e}(t)

Using ([2.1](https://arxiv.org/html/2512.17791v1#S2.E1 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([2.2](https://arxiv.org/html/2512.17791v1#S2.E2 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([2.5](https://arxiv.org/html/2512.17791v1#S2.E5 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) as well as the martingale property of (eXt)t∈ℝ+(e^{X\_{t}})\_{t\in\mathbb{R}\_{+}}, we first have

|  |  |  |  |
| --- | --- | --- | --- |
|  | K−be​(t)\displaystyle K-b\_{e}(t) | =Pe​(t,be​(t))=e−r​τ​𝔼​((K−be​(t)​e(r−δ)​τ+Xτ)+)\displaystyle=P\_{e}\big(t,b\_{e}(t)\big)=e^{-r\tau}\mathbb{E}\Big(\big(K-b\_{e}(t)e^{(r-\delta)\tau+X\_{\tau}}\big)^{+}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K​e−r​τ−be​(t)​e−δ​τ+e−r​τ​𝔼​((be​(t)​e(r−δ)​τ+Xτ−K)+),\displaystyle=Ke^{-r\tau}-b\_{e}(t)e^{-\delta\tau}+e^{-r\tau}\mathbb{E}\Big(\big(b\_{e}(t)e^{(r-\delta)\tau+X\_{\tau}}-K\big)^{+}\Big), |  |

where τ=T−t\tau=T-t, and so

|  |  |  |
| --- | --- | --- |
|  | Kbe​(t)​(1−e−r​τ)−(1−e−δ​τ)=e−r​τ​𝔼​((e(r−δ)​τ+Xτ−Kbe​(t))+).\displaystyle\frac{K}{b\_{e}(t)}\big(1-e^{-r\tau}\big)-\big(1-e^{-\delta\tau}\big)=e^{-r\tau}\mathbb{E}\left(\bigg(e^{(r-\delta)\tau+X\_{\tau}}-\frac{K}{b\_{e}(t)}\bigg)^{+}\right). |  |

Denote by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ​(τ):=Kbe​(T−τ)−1.\displaystyle\zeta(\tau):=\frac{K}{b\_{e}(T-\tau)}-1. |  | (4.3) |

By Theorem [2.5](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")-(a), we deduce that, as τ→0+\tau\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (r−δ)​τ=e−r​τ​𝔼​((e(r−δ)​τ+Xτ−1−ζ​(τ))+)+o​(τ)=𝔼​((e(r−δ)​τ+Xτ−1−ζ​(τ))+)+o​(τ),\displaystyle(r-\delta)\tau=e^{-r\tau}\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}}-1-\zeta(\tau)\big)^{+}\Big)+o(\tau)=\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}}-1-\zeta(\tau)\big)^{+}\Big)+o(\tau),\quad\,\,\, |  | (4.4) |

where the second equality above follows from the fact that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limτ→0+𝔼​((e(r−δ)​τ+Xτ−1−ζ​(τ))+)=0.\displaystyle\lim\_{\tau\rightarrow 0^{+}}\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}}-1-\zeta(\tau)\big)^{+}\Big)=0. |  | (4.5) |

The following proposition shows the rate of convergence of be​(t)b\_{e}(t) to KK, as t→T−t\rightarrow T^{-}, by characterizing the rate of convergence of ζ​(τ)\zeta(\tau) to 0 as τ→0+\tau\rightarrow 0^{+}.

###### Proposition 4.4.

Assume that σ>0\sigma>0 and d>0d>0. Then we have

|  |  |  |
| --- | --- | --- |
|  | limτ→0+ζ​(τ)−τ​ln⁡τ=σ.\displaystyle\lim\_{\tau\rightarrow 0^{+}}\frac{\zeta(\tau)}{\sqrt{-\tau\ln\tau}}=\sigma. |  |

The first step of the proof of Proposition [4.4](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") is the following lemma, the proof of which is deferred to Appendix [A](https://arxiv.org/html/2512.17791v1#A1 "Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models").

###### Lemma 4.5.

Assume that σ>0\sigma>0 and d>0d>0. Then we have

|  |  |  |
| --- | --- | --- |
|  | limτ→0+ζ​(τ)τ=∞.\displaystyle\lim\_{\tau\rightarrow 0^{+}}\frac{\zeta(\tau)}{\sqrt{\tau}}=\infty. |  |

The next two lemmas are seeking for a small-time large deviations result for (XτW+Jτ−)/τ(X\_{\tau}^{W}+J\_{\tau}^{-})/\sqrt{\tau}, the proof of which are again deferred to Appendix [A](https://arxiv.org/html/2512.17791v1#A1 "Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models").

###### Lemma 4.6.

Assume that σ>0\sigma>0 and d>0d>0. For any ε∈(0,1)\varepsilon\in(0,1) and r∈(0,∞)r\in(0,\infty), let

|  |  |  |  |
| --- | --- | --- | --- |
|  | L=L​(ε;σ):=σ2+2​∫[−ε,0)z2​ν​(d​z),τ0=τ0​(r,σ,ε):=r2(ν​((−∞,−ε))−σ2/2)2.\displaystyle L=L(\varepsilon;\sigma):=\sigma^{2}+2\int\_{[-\varepsilon,0)}z^{2}\nu(dz),\quad\tau\_{0}=\tau\_{0}(r,\sigma,\varepsilon):=\frac{r^{2}}{\big(\nu((-\infty,-\varepsilon))-\sigma^{2}/2\big)^{2}}. |  | (4.6) |

Then, for any τ∈(0,τ0]\tau\in(0,\tau\_{0}], we have

|  |  |  |
| --- | --- | --- |
|  | ℙ​(XτW+Jτ−≥r​τ)≤e−L​p2/2,\displaystyle\mathbb{P}\Big(X\_{\tau}^{W}+J\_{\tau}^{-}\geq r\sqrt{\tau}\Big)\leq e^{-Lp^{2}/2}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | p=p​(τ;r,σ,ε)=1L​[r−τ​(ν​((−∞,−ε))−σ22)]∈ℝ+.\displaystyle p=p(\tau;r,\sigma,\varepsilon)=\frac{1}{L}\bigg[r-\sqrt{\tau}\bigg(\nu((-\infty,-\varepsilon))-\frac{\sigma^{2}}{2}\bigg)\bigg]\in\mathbb{R}\_{+}. |  | (4.7) |

###### Lemma 4.7.

Assume that σ>0\sigma>0 and d>0d>0. Then for any f:ℝ+→ℝ+f:\mathbb{R}\_{+}\rightarrow\mathbb{R}\_{+} with limτ→0+f​(τ)=∞\lim\_{\tau\rightarrow 0^{+}}f(\tau)=\infty,

|  |  |  |
| --- | --- | --- |
|  | limτ→0+1f2​(τ)​ln⁡ℙ​(XτW+Jτ−≥τ​f​(τ))=−12​σ2.\displaystyle\lim\_{\tau\rightarrow 0^{+}}\frac{1}{f^{2}(\tau)}\ln\mathbb{P}\Big(X\_{\tau}^{W}+J\_{\tau}^{-}\geq\sqrt{\tau}f(\tau)\Big)=-\frac{1}{2\sigma^{2}}. |  |

Proof of Proposition [4.4](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"). In view of ([4.1](https://arxiv.org/html/2512.17791v1#S4.E1 "In 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and the independence among XWX^{W}, J+J^{+}, and J−J^{-}, for any τ∈ℝ+\tau\in\mathbb{R}\_{+}, by conditioning on XτW+Jτ−X^{W}\_{\tau}+J^{-}\_{\tau} and noting that,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(eJτ+)=exp⁡(τ​∫(0,∞)(ez−1)​ν​(d​z)),\displaystyle\mathbb{E}\big(e^{J\_{\tau}^{+}}\big)=\exp\bigg(\tau\int\_{(0,\infty)}\big(e^{z}-1\big)\,\nu(dz)\bigg), |  |

we first have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​((e(r−δ)​τ+Xτ−1−ζ​(τ))+)\displaystyle\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}}\!-\!1\!-\!\zeta(\tau)\big)^{+}\Big) | ≥𝔼​((e(r−δ)​τ+XτW+Jτ−​exp⁡(−τ​∫ℝ0(ez−1)+​ν​(d​z))​𝔼​(eJτ+)−1−ζ​(τ))+)\displaystyle\geq\mathbb{E}\!\left(\!\left(e^{(r-\delta)\tau+X\_{\tau}^{W}+J\_{\tau}^{-}}\!\exp\!\bigg(\!\!-\!\tau\!\!\int\_{\mathbb{R}\_{0}}\!\!\big(e^{z}\!-\!1\big)^{+}\nu(dz)\!\bigg)\mathbb{E}\big(e^{J\_{\tau}^{+}}\big)\!-\!1\!-\!\zeta(\tau)\!\right)^{+}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​((e(r−δ)​τ+XτW+Jτ−−1−ζ​(τ))+)≥𝔼​((XτW+Jτ−−ζ​(τ))+),\displaystyle=\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}^{W}+J\_{\tau}^{-}}-1-\zeta(\tau)\big)^{+}\Big)\geq\mathbb{E}\Big(\big(X\_{\tau}^{W}+J\_{\tau}^{-}-\zeta(\tau)\big)^{+}\Big), |  |

where we have used Jensen’s inequality in the first inequality and ez≥1+ze^{z}\geq 1+z in the last inequality. Together with ([4.4](https://arxiv.org/html/2512.17791v1#S4.E4 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |
| --- | --- | --- |
|  | ln⁡𝔼​((XτW+Jτ−τ−ζ​(τ)τ)+)≤12​ln⁡τ+ln⁡(r−δ)+o​(1),τ→0+,\displaystyle\ln\mathbb{E}\left(\bigg(\frac{X\_{\tau}^{W}+J\_{\tau}^{-}}{\sqrt{\tau}}-\frac{\zeta(\tau)}{\sqrt{\tau}}\bigg)^{+}\right)\leq\frac{1}{2}\ln\tau+\ln(r-\delta)+o(1),\quad\tau\rightarrow 0^{+}, |  |

which, together with Lemma [4.5](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infτ→0+τζ2​(τ)​ln⁡𝔼​((XτW+Jτ−τ−ζ​(τ)τ)+)≤lim infτ→0+τ​ln⁡τ2​ζ2​(τ).\displaystyle\liminf\_{\tau\rightarrow 0^{+}}\frac{\tau}{\zeta^{2}(\tau)}\ln\mathbb{E}\left(\bigg(\frac{X\_{\tau}^{W}+J\_{\tau}^{-}}{\sqrt{\tau}}-\frac{\zeta(\tau)}{\sqrt{\tau}}\bigg)^{+}\right)\leq\liminf\_{\tau\rightarrow 0^{+}}\frac{\tau\ln\tau}{2\zeta^{2}(\tau)}. |  | (4.8) |

Moreover, by Markov’s inequality, for any β∈(1,∞)\beta\in(1,\infty) and τ∈ℝ+\tau\in\mathbb{R}\_{+} we have

|  |  |  |
| --- | --- | --- |
|  | ℙ​(XτW+Jτ−≥β​ζ​(τ))≤τ(β−1)​ζ​(τ)​𝔼​((XτW+Jτ−τ−ζ​(τ)τ)+).\displaystyle\mathbb{P}\Big(X\_{\tau}^{W}+J\_{\tau}^{-}\geq\beta\zeta(\tau)\Big)\leq\frac{\sqrt{\tau}}{(\beta-1)\zeta(\tau)}\mathbb{E}\left(\bigg(\frac{X\_{\tau}^{W}+J\_{\tau}^{-}}{\sqrt{\tau}}-\frac{\zeta(\tau)}{\sqrt{\tau}}\bigg)^{+}\right). |  |

This, together with Lemma [4.7](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") (with f​(τ)=β​ζ​(τ)/τf(\tau)=\beta\zeta(\tau)/\sqrt{\tau}) and ([4.8](https://arxiv.org/html/2512.17791v1#S4.E8 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), implies that

|  |  |  |
| --- | --- | --- |
|  | lim infτ→0+τ​ln⁡τ2​ζ2​(τ)≥limτ→0+τζ2​(τ)​ln⁡ℙ​(XτW+Jτ−≥β​ζ​(τ))+limτ→0+ln⁡((β−1)​ζ​(τ)/τ)ζ2​(τ)/τ=−β22​σ2,\displaystyle\liminf\_{\tau\rightarrow 0^{+}}\frac{\tau\ln\tau}{2\zeta^{2}(\tau)}\geq\lim\_{\tau\rightarrow 0^{+}}\frac{\tau}{\zeta^{2}(\tau)}\ln\mathbb{P}\Big(X\_{\tau}^{W}+J\_{\tau}^{-}\geq\beta\zeta(\tau)\Big)+\lim\_{\tau\rightarrow 0^{+}}\frac{\ln\big((\beta-1)\zeta(\tau)/\sqrt{\tau}\big)}{\zeta^{2}(\tau)/\tau}=-\frac{\beta^{2}}{2\sigma^{2}}, |  |

or equivalently,

|  |  |  |
| --- | --- | --- |
|  | lim infτ→0+ζ​(τ)−τ​ln⁡τ≥σβ.\displaystyle\liminf\_{\tau\rightarrow 0^{+}}\frac{\zeta(\tau)}{\sqrt{-\tau\ln\tau}}\geq\frac{\sigma}{\beta}. |  |

Since β∈(1,∞)\beta\in(1,\infty) is arbitrary, by taking β→1+\beta\rightarrow 1^{+} above we obtain that

|  |  |  |
| --- | --- | --- |
|  | lim infτ→0+ζ​(τ)−τ​ln⁡τ≥σ.\displaystyle\liminf\_{\tau\rightarrow 0^{+}}\frac{\zeta(\tau)}{\sqrt{-\tau\ln\tau}}\geq\sigma. |  |

In order to derive an upper bound for lim supτ→0+ζ​(τ)/−τ​ln⁡τ\limsup\_{\tau\rightarrow 0^{+}}\zeta(\tau)/\sqrt{-\tau\ln\tau}, we first deduce from ([4.4](https://arxiv.org/html/2512.17791v1#S4.E4 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) a lower bound for 𝔼​((eXτW+Jτ−−1−ζ​(τ))+)\mathbb{E}((e^{X\_{\tau}^{W}+J\_{\tau}^{-}}-1-\zeta(\tau))^{+}) as τ→0+\tau\rightarrow 0^{+}. Indeed, for any τ∈ℝ+\tau\in\mathbb{R}\_{+}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​((e(r−δ)​τ+Xτ−1−ζ​(τ))+)\displaystyle\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}}-1-\zeta(\tau)\big)^{+}\Big) | =𝔼​(e(r−δ)​τ+Xτ​𝟏{Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ})\displaystyle=\mathbb{E}\Big(e^{(r-\delta)\tau+X\_{\tau}}{\bf 1}\_{\{X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\}}\Big) |  | (4.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(1+ζ​(τ))​ℙ​(Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ).\displaystyle\quad-\big(1+\zeta(\tau)\big)\mathbb{P}\big(X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\big). |  | (4.10) |

Note that Lemmas [4.2](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") and [4.5](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") imply that

|  |  |  |
| --- | --- | --- |
|  | limτ→0+ℙ​(Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ)=limτ→0+ℙ​(Xττ≥ln⁡(1+ζ​(τ))τ+(r−δ)​τ)=0.\displaystyle\lim\_{\tau\rightarrow 0^{+}}\mathbb{P}\big(X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\big)=\lim\_{\tau\rightarrow 0^{+}}\mathbb{P}\bigg(\frac{X\_{\tau}}{\sqrt{\tau}}\geq\frac{\ln(1+\zeta(\tau))}{\sqrt{\tau}}+(r-\delta)\sqrt{\tau}\bigg)=0. |  |

Hence, we obtain from ([4.5](https://arxiv.org/html/2512.17791v1#S4.E5 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([4.10](https://arxiv.org/html/2512.17791v1#S4.E10 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) that

|  |  |  |
| --- | --- | --- |
|  | limτ→0+𝔼​(eXτ​𝟏{Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ})=limτ→0+𝔼​(e(r−δ)​τ+Xτ​𝟏{Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ})=0,\displaystyle\lim\_{\tau\rightarrow 0^{+}}\mathbb{E}\Big(e^{X\_{\tau}}{\bf 1}\_{\{X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\}}\Big)=\lim\_{\tau\rightarrow 0^{+}}\mathbb{E}\Big(e^{(r-\delta)\tau+X\_{\tau}}{\bf 1}\_{\{X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\}}\Big)=0, |  |

and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​((e(r−δ)​τ+Xτ−1−ζ​(τ))+)\displaystyle\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}}-1-\zeta(\tau)\big)^{+}\Big) | =𝔼​(eXτ​𝟏{Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ})\displaystyle=\mathbb{E}\Big(e^{X\_{\tau}}{\bf 1}\_{\{X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1+ζ​(τ))​ℙ​(Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ)+o​(τ),τ→0+.\displaystyle\quad-\big(1+\zeta(\tau)\big)\mathbb{P}\big(X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\big)+o(\tau),\quad\tau\rightarrow 0^{+}. |  |

This, together with ([4.4](https://arxiv.org/html/2512.17791v1#S4.E4 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), implies that, as τ→0+\tau\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (r−δ)​τ=𝔼​((eXτ−1−ζ​(τ))​𝟏{Xτ≥ln⁡(1+ζ​(τ))+(r−δ)​τ})+o​(τ)≤𝔼​((eXτ−1−ζ​(τ))+)+o​(τ).\displaystyle(r-\delta)\tau=\mathbb{E}\Big(\big(e^{X\_{\tau}}\!-\!1\!-\!\zeta(\tau)\big){\bf 1}\_{\{X\_{\tau}\geq\ln(1+\zeta(\tau))+(r-\delta)\tau\}}\Big)+o(\tau)\leq\mathbb{E}\Big(\big(e^{X\_{\tau}}\!-\!1\!-\!\zeta(\tau)\big)^{+}\Big)+o(\tau).\qquad |  | (4.11) |

Using ([4.1](https://arxiv.org/html/2512.17791v1#S4.E1 "In 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([4.2](https://arxiv.org/html/2512.17791v1#S4.E2 "In 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) as well as the independence among XWX^{W}, J+J^{+}, and J−J^{-}, the expectation on the right-hand side of ([4.11](https://arxiv.org/html/2512.17791v1#S4.E11 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) can be bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​((eXτ−1−ζ​(τ))+)\displaystyle\mathbb{E}\Big(\!\big(e^{X\_{\tau}}\!\!-\!1\!-\!\zeta(\tau)\big)^{+}\!\Big)\! | ≤𝔼​((eXτW+Jτ++Jτ−−1−ζ​(τ))+)≤𝔼​((eJτ+−1)​eXτW+Jτ−)+𝔼​((eXτW+Jτ−−1−ζ​(τ))+)\displaystyle\leq\mathbb{E}\Big(\!\big(e^{X\_{\tau}^{W}\!+J\_{\tau}^{+}\!+J\_{\tau}^{-}}\!\!-\!1\!-\!\zeta(\tau)\big)^{+}\!\Big)\!\!\leq\!\mathbb{E}\Big(\!\big(e^{J\_{\tau}^{+}}\!\!-\!1\big)e^{X\_{\tau}^{W}\!+J\_{\tau}^{-}}\Big)\!\!+\!\mathbb{E}\Big(\!\big(e^{X\_{\tau}^{W}\!+J\_{\tau}^{-}}\!\!-\!1\!-\!\zeta(\tau)\big)^{+}\!\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(eJτ+−1)​𝔼​(eXτW)​𝔼​(eJτ−)+𝔼​((eXτW+Jτ−−1−ζ​(τ))+)\displaystyle=\mathbb{E}\big(e^{J\_{\tau}^{+}}-1\big)\mathbb{E}\big(e^{X\_{\tau}^{W}}\big)\mathbb{E}\big(e^{J\_{\tau}^{-}}\big)+\mathbb{E}\Big(\big(e^{X\_{\tau}^{W}+J\_{\tau}^{-}}-1-\zeta(\tau)\big)^{+}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(τ​∫(0,∞)(ez−1)​ν​(d​z))−1+𝔼​((eXτW+Jτ−−1−ζ​(τ))+)\displaystyle=\exp\bigg(\tau\int\_{(0,\infty)}\big(e^{z}-1\big)\nu(dz)\bigg)-1+\mathbb{E}\Big(\big(e^{X\_{\tau}^{W}+J\_{\tau}^{-}}-1-\zeta(\tau)\big)^{+}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =τ​∫(0,∞)(ez−1)​ν​(d​z)+𝔼​((eXτW+Jτ−−1−ζ​(τ))+)+o​(τ),τ→0+.\displaystyle=\tau\int\_{(0,\infty)}\big(e^{z}-1\big)\nu(dz)+\mathbb{E}\Big(\big(e^{X\_{\tau}^{W}+J\_{\tau}^{-}}-1-\zeta(\tau)\big)^{+}\Big)+o(\tau),\quad\tau\rightarrow 0^{+}. |  |

Together with ([1.3](https://arxiv.org/html/2512.17791v1#S1.E3 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([4.11](https://arxiv.org/html/2512.17791v1#S4.E11 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​τ≤𝔼​((eXτW+Jτ−−1−ζ​(τ))+)+o​(τ),τ→0+.\displaystyle d\tau\leq\mathbb{E}\Big(\big(e^{X\_{\tau}^{W}+J\_{\tau}^{-}}-1-\zeta(\tau)\big)^{+}\Big)+o(\tau),\quad\tau\rightarrow 0^{+}. |  | (4.12) |

Next, we will derive an upper bound for 𝔼​((eXτW+Jτ−−1−ζ​(τ))+)\mathbb{E}((e^{X\_{\tau}^{W}+J\_{\tau}^{-}}-1-\zeta(\tau))^{+}) as τ→0+\tau\rightarrow 0^{+}. For any ε∈(0,1)\varepsilon\in(0,1), in view of Lemma [4.5](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), we take τ∈ℝ+\tau\in\mathbb{R}\_{+} small enough so that τ≤ln2⁡(1+ζ​(τ))/[τ​(ν​((−∞,−ε))−σ2/2)2]\tau\leq\ln^{2}(1+\zeta(\tau))/[\tau(\nu((-\infty,-\varepsilon))-\sigma^{2}/2)^{2}]. By Lemma [4.6](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​((eXτW+Jτ−−1−ζ​(τ))+)\displaystyle\mathbb{E}\Big(\!\big(e^{X\_{\tau}^{W}\!+J\_{\tau}^{-}}\!\!-\!1\!-\!\zeta(\tau)\big)^{+}\!\Big)\! | =∫ln⁡(1+ζ​(τ))∞ey​ℙ​(XτW+Jτ−≥y)​𝑑y=τ​∫ln⁡(1+ζ​(τ))/τ∞eτ​z​ℙ​(XτW+Jτ−≥τ​z)​𝑑z\displaystyle=\!\!\int\_{\ln(1+\zeta(\tau))}^{\infty}\!\!e^{y}\mathbb{P}\big(X\_{\tau}^{W}\!\!+\!J\_{\tau}^{-}\!\!\geq\!y\big)dy\!=\!\sqrt{\tau}\!\!\int\_{\ln(1+\zeta(\tau))/\sqrt{\tau}}^{\infty}\!\!e^{\sqrt{\tau}z}\mathbb{P}\big(X\_{\tau}^{W}\!\!+\!J\_{\tau}^{-}\!\!\geq\!\!\sqrt{\tau}z\big)dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤τ​∫ln⁡(1+ζ​(τ))/τ∞eτ​z​exp⁡(−12​L​[z−τ​(ν​((−∞,−ε))−σ22)]2)​𝑑z\displaystyle\leq\sqrt{\tau}\int\_{\ln(1+\zeta(\tau))/\sqrt{\tau}}^{\infty}e^{\sqrt{\tau}z}\exp\bigg(\!\!-\!\frac{1}{2L}\bigg[z-\sqrt{\tau}\bigg(\nu((-\infty,-\varepsilon))-\frac{\sigma^{2}}{2}\bigg)\bigg]^{2}\bigg)dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L​τ​(1+O​(τ))​∫[ln⁡(1+ζ​(τ))−τ​(L+ν​((−∞,−ε))−σ2/2)]/L​τ∞e−x2/2​𝑑x,\displaystyle\leq\sqrt{L\tau}\big(1+O(\sqrt{\tau})\big)\int\_{[\ln(1+\zeta(\tau))-\tau(L+\nu((-\infty,-\varepsilon))-\sigma^{2}/2)]/\sqrt{L\tau}}^{\infty}e^{-x^{2}/2}\,dx, |  |

where we used change of variable x=L​ω+τ​(L+ν​((−∞,−ε))−σ2/2){x}=\sqrt{L}\omega+\sqrt{\tau}(L+\nu((-\infty,-\varepsilon))-\sigma^{2}/2) in the last inequality, and L=L​(ε;σ)L=L(\varepsilon;\sigma) is given as in ([4.7](https://arxiv.org/html/2512.17791v1#S4.E7 "In Lemma 4.6. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). In view of Lemma [4.5](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), the lower limit of the last integral above explodes as τ→0+\tau\rightarrow 0^{+}. Hence, by ([A.2](https://arxiv.org/html/2512.17791v1#A1.E2 "In Proof of Lemma 4.7 ‣ Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) we obtain that, as τ→0+\tau\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​((eXτW+Jτ−−1−ζ​(τ))+)≤2​π​L​τ​(1+O​(τ))​ϕ​(ln⁡(1+ζ​(τ))−τ​(L+ν​((−∞,−ε))−σ2/2)L​τ).\displaystyle\mathbb{E}\Big(\!\big(e^{X\_{\tau}^{W}\!+J\_{\tau}^{-}}\!\!-\!1\!-\!\zeta(\tau)\big)^{+}\!\Big)\!\leq\!\sqrt{2\pi L\tau}\big(1\!+\!O(\sqrt{\tau})\big)\phi\bigg(\frac{\ln\!\big(1\!+\!\zeta(\tau)\big)\!-\!\tau\big(L\!+\!\nu((-\infty,-\varepsilon))\!-\!\sigma^{2}\!/2\big)}{\sqrt{L\tau}}\!\bigg).\qquad |  | (4.13) |

Combining ([4.12](https://arxiv.org/html/2512.17791v1#S4.E12 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([4.13](https://arxiv.org/html/2512.17791v1#S4.E13 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |
| --- | --- | --- |
|  | d​τ+o​(τ)≤2​π​L​(1+O​(τ))​ϕ​(ln⁡(1+ζ​(τ))−τ​(L+ν​((−∞,−ε))−σ2/2)L​τ),τ→0+,\displaystyle d\sqrt{\tau}+o\big(\sqrt{\tau}\big)\leq\sqrt{2\pi L}\big(1+O(\sqrt{\tau})\big)\phi\bigg(\frac{\ln\big(1+\zeta(\tau)\big)-\tau\big(L+\nu((-\infty,-\varepsilon))-\sigma^{2}/2\big)}{\sqrt{L\tau}}\bigg),\quad\tau\rightarrow 0^{+}, |  |

and so

|  |  |  |
| --- | --- | --- |
|  | lim supτ→0+ln⁡τ2​ζ2​(τ)/τ≤−limτ→0+[ln⁡(1+ζ​(τ))−τ​(L+ν​((−∞,−ε))−σ2/2)]22​L​ζ2​(τ)=−12​L,\displaystyle\limsup\_{\tau\rightarrow 0^{+}}\frac{\ln\tau}{2\zeta^{2}(\tau)/\tau}\leq-\lim\_{\tau\rightarrow 0^{+}}\frac{\big[\ln\big(1+\zeta(\tau)\big)-\tau\big(L+\nu((-\infty,-\varepsilon))-\sigma^{2}/2\big)\big]^{2}}{2L\zeta^{2}(\tau)}=-\frac{1}{2L}, |  |

or equivalently,

|  |  |  |
| --- | --- | --- |
|  | lim supτ→0+ζ​(τ)−τ​ln⁡τ≤L.\displaystyle\limsup\_{\tau\rightarrow 0^{+}}\frac{\zeta(\tau)}{\sqrt{-\tau\ln\tau}}\leq\sqrt{L}. |  |

Finally, by taking ε→0+\varepsilon\rightarrow 0^{+} above and noting from ([4.6](https://arxiv.org/html/2512.17791v1#S4.E6 "In Lemma 4.6. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) that L=L​(ε;σ)→σ2L=L(\varepsilon;\sigma)\rightarrow\sigma^{2}, we obtain that

|  |  |  |
| --- | --- | --- |
|  | lim supτ→0+ζ​(τ)−τ​ln⁡τ≤σ,\displaystyle\limsup\_{\tau\rightarrow 0^{+}}\frac{\zeta(\tau)}{\sqrt{-\tau\ln\tau}}\leq\sigma, |  |

which completes the proof of the proposition. □\Box

### 4.2. Step 2: The difference between European and American critical prices

To study the asymptotic behavior of the difference between the European and American critical prices, we first recall some regularity results on the American put price PP defined as in ([2.3](https://arxiv.org/html/2512.17791v1#S2.E3 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). It is more convenient to state those results after a logarithmic change of variable. Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | P~​(t,x):=P​(t,ex),(t,x)∈[0,T]×ℝ,\displaystyle\widetilde{P}(t,x):=P\big(t,e^{x}\big),\quad(t,x)\in[0,T]\times\mathbb{R}, |  | (4.14) |

Since x↦exx\mapsto e^{x} is increasing and convex on ℝ\mathbb{R}, it follows from the analogous properties of P​(t,⋅)P(t,\cdot) that P~​(t,⋅)\widetilde{P}(t,\cdot) is non-increasing and convex on ℝ\mathbb{R}, for any t∈[0,T]t\in[0,T]. Let 𝒜~\widetilde{\mathscr{A}} be the infinitesimal generator of X~:=(X~t)t∈ℝ+\widetilde{X}:=(\widetilde{X}\_{t})\_{t\in\mathbb{R}\_{+}}, where X~t:=(r−δ)​t+Xt\widetilde{X}\_{t}:=(r-\delta)t+X\_{t}, namely,

|  |  |  |
| --- | --- | --- |
|  | 𝒜~​f​(x):=(r−δ−σ22)​f′​(x)+σ22​f′′​(x)+∫ℝ0(f​(x+z)−f​(x)−f′​(x)​(ez−1))​ν​(d​z).\displaystyle\widetilde{\mathscr{A}}f(x):=\bigg(r-\delta-\frac{\sigma^{2}}{2}\bigg)f^{\prime}(x)+\frac{\sigma^{2}}{2}f^{\prime\prime}(x)+\int\_{\mathbb{R}\_{0}}\big(f(x+z)-f(x)-f^{\prime}(x)\big(e^{z}-1\big)\big)\nu(dz). |  |

The following result (cf. [[5](https://arxiv.org/html/2512.17791v1#bib.bib5), Theorem 3.3]) shows that the American put price satisfies a variational inequality in the sense of distributions.

###### Theorem 4.8.

The distribution (∂/∂t+𝒜~−r)​P~(\partial/\partial t+\widetilde{\mathscr{A}}-r)\widetilde{P} is a nonpositive measure on (0,T)×ℝ(0,T)\times\mathbb{R}. Moreover, (∂/∂t+𝒜~−r)​P~=0(\partial/\partial t+\widetilde{\mathscr{A}}-r)\widetilde{P}=0 on the continuation region 𝒞~:={(t,x)∈(0,T)×ℝ:P~​(t,x)>(K−ex)+}\widetilde{\mathcal{C}}:=\{(t,x)\in(0,T)\times\mathbb{R}:\widetilde{P}(t,x)>(K-e^{x})^{+}\}.

The following result provides the estimation of the difference be​(t)−b​(t)b\_{e}(t)-b(t) near maturity.

###### Proposition 4.9.

Assume σ>0\sigma>0 and d>0d>0. Then we have

|  |  |  |
| --- | --- | --- |
|  | lim supt→T−be​(t)−b​(t)T−t<∞.\displaystyle\limsup\_{t\rightarrow T^{-}}\frac{b\_{e}(t)-b(t)}{\sqrt{T-t}}<\infty. |  |

Proof. Since P~​(⋅,x)\widetilde{P}(\cdot,x) is non-increasing on [0,T][0,T], for each x∈ℝx\in\mathbb{R}, it follows from Theorem [4.8](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜~​P~=r​P~−∂P~∂t≥r​P~≥0​ on ​𝒞~,\displaystyle\widetilde{\mathscr{A}}\,\widetilde{P}=r\widetilde{P}-\frac{\partial\widetilde{P}}{\partial t}\geq r\widetilde{P}\geq 0\,\,\,\text{ on }\,\widetilde{\mathcal{C}}, |  | (4.15) |

in the sense of distribution, or, equivalently,

|  |  |  |
| --- | --- | --- |
|  | (r−δ−σ22)∂P~∂x+σ22∂2P~∂x2+∫ℝ0(P~(⋅,⋅+z)−P~(⋅,⋅)−∂P~∂x(⋅,⋅)(ez−1))ν(dz)≥0 on 𝒞~.\displaystyle\bigg(r-\delta-\frac{\sigma^{2}}{2}\bigg)\frac{\partial\widetilde{P}}{\partial x}+\frac{\sigma^{2}}{2}\frac{\partial^{2}\widetilde{P}}{\partial x^{2}}+\int\_{\mathbb{R}\_{0}}\bigg(\widetilde{P}(\cdot\,,\cdot+z)-\widetilde{P}(\cdot\,,\cdot)-\frac{\partial\widetilde{P}}{\partial x}(\cdot\,,\cdot)\big(e^{z}-1\big)\bigg)\nu(dz)\geq 0\,\,\,\text{ on }\,\widetilde{\mathcal{C}}. |  |

Since P~​(t,⋅)\widetilde{P}(t,\cdot) is convex on ℝ\mathbb{R} for any t∈[0,T]t\in[0,T], the right partial derivative of P~​(t,⋅)\widetilde{P}(t,\cdot),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂+P~​(t,x)∂x:=limh→0+P~​(t,x+h)−P~​(t,x)h,\displaystyle\frac{\partial\_{+}\widetilde{P}(t,x)}{\partial x}:=\lim\_{h\rightarrow 0^{+}}\frac{\widetilde{P}(t,x+h)-\widetilde{P}(t,x)}{h}, |  | (4.16) |

is a well-defined function on [0,T]×ℝ[0,T]\times\mathbb{R}, and we also have ∂P~/∂x=∂+P~/∂x\partial\widetilde{P}/\partial x=\partial\_{+}\widetilde{P}/\partial x on [0,T]×ℝ[0,T]\times\mathbb{R} in the sense of distribution. With the notion of dd defined as in ([1.3](https://arxiv.org/html/2512.17791v1#S1.E3 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ22​(∂2P~∂x2−∂P~∂x)+ℐ≥−d​∂+P~∂x−∫(0,∞)supy∈(ln⁡b​(t),ln⁡K)|P~​(⋅,y+z)−P~​(⋅,y)|​ν​(d​z)​ on ​𝒞~,\displaystyle\frac{\sigma^{2}}{2}\bigg(\frac{\partial^{2}\widetilde{P}}{\partial x^{2}}-\frac{\partial\widetilde{P}}{\partial x}\bigg)+\mathcal{I}\geq-d\frac{\partial\_{+}\widetilde{P}}{\partial x}-\int\_{(0,\infty)}\sup\_{y\in(\ln b(t),\ln K)}\big|\widetilde{P}(\cdot\,,y+z)-\widetilde{P}(\cdot\,,y)\big|\,\nu(dz)\,\,\,\text{ on }\,\widetilde{\mathcal{C}},\qquad |  | (4.17) |

in the sense of distribution, where

|  |  |  |
| --- | --- | --- |
|  | ℐ​(t,x):=∫(−∞,0)(P~​(t,x+z)−P~​(t,x)−∂+P~∂x​(t,x)​(ez−1))​ν​(d​z),(t,x)∈𝒞~.\displaystyle\mathcal{I}(t,x):=\int\_{(-\infty,0)}\bigg(\widetilde{P}(t,x+z)-\widetilde{P}(t,x)-\frac{\partial\_{+}\widetilde{P}}{\partial x}(t,x)\big(e^{z}-1\big)\bigg)\nu(dz),\quad(t,x)\in\widetilde{\mathcal{C}}. |  |

Recall that for each t∈(0,T)t\in(0,T), P​(t,⋅)P(t,\cdot) is non-increasing and Lipschitz on ℝ+\mathbb{R}\_{+} (see Proposition [2.4](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and thus, for any y∈(ln⁡b​(t),ln⁡K)y\in(\ln b(t),\ln K) and z∈(0,∞)z\in(0,\infty),

|  |  |  |
| --- | --- | --- |
|  | 0≤P~​(t,y)−P~​(t,y+z)=P​(t,ey)−P​(t,ey+z)≤ey​(ez−1)≤K​(ez−1),\displaystyle 0\leq\widetilde{P}(t,y)-\widetilde{P}(t,y+z)=P\big(t,e^{y}\big)-P\big(t,e^{y+z}\big)\leq e^{y}\big(e^{z}-1\big)\leq K\big(e^{z}-1\big), |  |

and

|  |  |  |
| --- | --- | --- |
|  | 0≤P~​(t,y)−P~​(t,y+z)=P​(t,ey)−P​(t,ey+z)≤P​(t,b​(t))=(K−b​(t))→0,as ​t→T−.\displaystyle 0\leq\widetilde{P}(t,y)-\widetilde{P}(t,y+z)=P\big(t,e^{y}\big)-P\big(t,e^{y+z}\big)\leq P\big(t,b(t)\big)=\big(K-b(t)\big)\rightarrow 0,\quad\text{as }\,t\rightarrow T^{-}. |  |

Hence, the dominated convergence theorem ensures that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→T−∫(0,∞)supy∈(ln⁡b​(t),ln⁡K)|P~​(t,y+z)−P~​(t,y)|​ν​(d​z)=0.\displaystyle\lim\_{t\rightarrow T^{-}}\int\_{(0,\infty)}\sup\_{y\in(\ln b(t),\ln K)}\big|\widetilde{P}(t,y+z)-\widetilde{P}(t,y)\big|\,\nu(dz)=0. |  | (4.18) |

Now for any t∈(0,T)t\in(0,T) and x∈(ln⁡b​(t),ln⁡be​(t))x\in(\ln b(t),\ln b\_{e}(t)), using ([4.14](https://arxiv.org/html/2512.17791v1#S4.E14 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), the convexity of P​(t,⋅)P(t,\cdot), and the fact that (P−Pe)​(t,⋅)(P-P\_{e})(t,\cdot) is non-increasing on ℝ+\mathbb{R}\_{+} (cf. [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Corollary 3.1]), we have (with τ=T−t\tau=T-t)

|  |  |  |
| --- | --- | --- |
|  | e−x​∂+P~∂x​(t,x)=∂+P∂s​(t,ex)≤∂−P∂s​(t,be​(t))≤∂−Pe∂s​(t,be​(t))=−𝔼​(e−δ​τ+Xτ​𝟏{be​(t)​e(r−δ)​τ+Xτ≤K}),\displaystyle e^{-x}\frac{\partial\_{+}\widetilde{P}}{\partial x}(t,x)=\frac{\partial\_{+}P}{\partial s}(t,e^{x})\leq\frac{\partial\_{-}P}{\partial s}\big(t,b\_{e}(t)\big)\leq\frac{\partial\_{-}P\_{e}}{\partial s}\big(t,b\_{e}(t)\big)=-\mathbb{E}\bigg(e^{-\delta\tau+X\_{\tau}}{\bf 1}\_{\{b\_{e}(t)e^{(r-\delta)\tau+X\_{\tau}}\leq K\}}\!\bigg), |  |

where the left-derivatives ∂−P/∂x\partial\_{-}{P}/\partial x and ∂−Pe/∂x\partial\_{-}{P}\_{e}/\partial x are defined analogously to ([4.16](https://arxiv.org/html/2512.17791v1#S4.E16 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), but taking h→0−h\rightarrow 0^{-}. Using ([4.3](https://arxiv.org/html/2512.17791v1#S4.E3 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), Lemmas [4.2](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") and [4.5](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), and the martingale property of (eXt)t∈ℝ+(e^{X\_{t}})\_{t\in\mathbb{R}\_{+}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −limt→T−∂+P∂s​(t,ex)\displaystyle-\!\!\lim\_{t\rightarrow T^{-}}\!\!\frac{\partial\_{+}P}{\partial s}(t,e^{x}) | ≥limτ→0+𝔼​(e−δ​τ+Xτ​𝟏{be​(t)​e(r−δ)​τ+Xτ≤K})=limτ→0+𝔼​(e−δ​τ+Xτ​𝟏{(r−δ)​τ+Xτ≤ln⁡(1+ζ​(τ))})\displaystyle\geq\!\lim\_{\tau\rightarrow 0^{+}}\!\!\mathbb{E}\bigg(e^{-\delta\tau+X\_{\tau}}{\bf 1}\_{\{b\_{e}(t)e^{(r-\delta)\tau+X\_{\tau}}\leq K\}}\!\bigg)=\!\lim\_{\tau\rightarrow 0^{+}}\!\!\mathbb{E}\bigg(e^{-\delta\tau+X\_{\tau}}{\bf 1}\_{\{(r-\delta)\tau+X\_{\tau}\leq\ln(1+\zeta(\tau))\}}\!\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =limτ→0+𝔼​(e−δ​τ+Xτ​𝟏{((r−δ)​τ+Xτ)/τ≤ln⁡(1+ζ​(τ))/τ})=limτ→0+𝔼​(eXτ)=1.\displaystyle=\lim\_{\tau\rightarrow 0^{+}}\mathbb{E}\bigg(e^{-\delta\tau+X\_{\tau}}{\bf 1}\_{\{((r-\delta)\tau+X\_{\tau})/\sqrt{\tau}\leq\ln(1+\zeta(\tau))/\sqrt{\tau}\}}\bigg)=\lim\_{\tau\rightarrow 0^{+}}\mathbb{E}\big(e^{X\_{\tau}}\big)=1. |  | (4.19) |

By combining ([4.18](https://arxiv.org/html/2512.17791v1#S4.E18 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([4.19](https://arxiv.org/html/2512.17791v1#S4.E19 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we have

|  |  |  |
| --- | --- | --- |
|  | lim inft→T−infx∈(ln⁡b​(t),ln⁡be​(t))(−d​∂+P~∂x​(t,x)−∫(0,∞)supy∈(ln⁡b​(t),ln⁡K)|P~​(t,y+z)−P~​(t,y)|​ν​(d​z))\displaystyle\liminf\_{t\rightarrow T^{-}}\inf\_{x\in(\ln b(t),\ln b\_{e}(t))}\bigg(\!-d\,\frac{\partial\_{+}\widetilde{P}}{\partial x}(t,x)-\int\_{(0,\infty)}\sup\_{y\in(\ln b(t),\ln K)}\big|\widetilde{P}(t,y+z)-\widetilde{P}(t,y)\big|\,\nu(dz)\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | =lim inft→T−infs∈(b​(t),be​(t))(−d​s​∂+P∂s​(t,s)−∫(0,∞)supu∈(b​(t),K)|P​(t,u​ez)−P​(t,u)|​ν​(d​z))≥d​K.\displaystyle\quad=\liminf\_{t\rightarrow T^{-}}\inf\_{s\in(b(t),b\_{e}(t))}\bigg(-ds\frac{\partial\_{+}P}{\partial s}(t,s)-\int\_{(0,\infty)}\sup\_{u\in(b(t),K)}\big|P(t,ue^{z})-P(t,u)\big|\,\nu(dz)\bigg)\geq dK. |  |

Hence, we can choose ρ∈(0,∞)\rho\in(0,\infty) such that for all t∈(T−ρ,T)t\in(T-\rho,T) and x∈(ln⁡b​(t),ln⁡be​(t))x\in(\ln b(t),\ln b\_{e}(t)),

|  |  |  |
| --- | --- | --- |
|  | −d​∂+P~∂x​(t,x)−∫(0,∞)supy∈(ln⁡b​(t),ln⁡K)|P~​(t,y+z)−P~​(t,y)|​ν​(d​z)≥d​K2.\displaystyle-d\,\frac{\partial\_{+}\widetilde{P}}{\partial x}(t,x)-\int\_{(0,\infty)}\sup\_{y\in(\ln b(t),\ln K)}\big|\widetilde{P}(t,y+z)-\widetilde{P}(t,y)\big|\,\nu(dz)\geq\frac{dK}{2}. |  |

Together with ([4.17](https://arxiv.org/html/2512.17791v1#S4.E17 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that, in the sense of distribution,

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ22​(∂2P~∂x2−∂P~∂x)+ℐ≥d​K2​ on ​𝒞~ρ,\displaystyle\frac{\sigma^{2}}{2}\bigg(\frac{\partial^{2}\widetilde{P}}{\partial x^{2}}-\frac{\partial\widetilde{P}}{\partial x}\bigg)+\mathcal{I}\geq\frac{dK}{2}\,\,\,\text{ on }\,\widetilde{\mathcal{C}}\_{\rho}, |  | (4.20) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝒞~ρ:={(t,x)∈ℝ+×ℝ:t∈(T−ρ,T),x∈(ln⁡b​(t),ln⁡be​(t))}.\displaystyle\widetilde{\mathcal{C}}\_{\rho}:=\big\{(t,x)\in\mathbb{R}\_{+}\times\mathbb{R}:t\in(T-\rho,T),x\in(\ln b(t),\ln b\_{e}(t))\big\}. |  |

Next we will derive an upper bound for ℐ​(t,x)\mathcal{I}(t,x) on 𝒞~\widetilde{\mathcal{C}}. To begin with, by ([4.14](https://arxiv.org/html/2512.17791v1#S4.E14 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) we first have

|  |  |  |
| --- | --- | --- |
|  | ℐ​(t,x)=(∫(−∞,ln⁡b​(t)−x]+∫(ln⁡b​(t)−x,0))​(P​(t,ex+z)−P​(t,ex)−ex​∂+P∂s​(t,ex)​(ez−1))​ν​(d​z),\displaystyle\mathcal{I}(t,x)=\left(\int\_{(-\infty,\ln b(t)-x]}+\int\_{(\ln b(t)-x,0)}\right)\bigg(P(t,e^{x+z})-P(t,e^{x})-e^{x}\frac{\partial\_{+}P}{\partial s}(t,e^{x})\big(e^{z}-1\big)\bigg)\nu(dz), |  |

for any (t,x)∈𝒞~(t,x)\in\widetilde{\mathcal{C}}. Note that, for any z∈(−∞,ln⁡b​(t)−x]z\in(-\infty,\ln b(t)-x], we have

|  |  |  |
| --- | --- | --- |
|  | P​(t,ex+z)−P​(t,ex)−ex​∂+P∂s​(t,ex)​(ez−1)=(K−ex+z)−P​(t,ex)−ex​∂+P∂s​(t,ex)​(ez−1)\displaystyle P(t,e^{x+z})-P(t,e^{x})-e^{x}\frac{\partial\_{+}P}{\partial s}(t,e^{x})\big(e^{z}-1\big)=\big(K-e^{x+z}\big)-P(t,e^{x})-e^{x}\frac{\partial\_{+}P}{\partial s}(t,e^{x})\big(e^{z}-1\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(K−ex+z)−(K−ex)−ex​∂+P∂s​(t,ex)​(ez−1)=ex​(∂+P∂s​(t,ex)+1)​(1−ez),\displaystyle\quad\leq\big(K-e^{x+z}\big)-\big(K-e^{x}\big)-e^{x}\frac{\partial\_{+}P}{\partial s}(t,e^{x})\big(e^{z}-1\big)=e^{x}\bigg(\frac{\partial\_{+}P}{\partial s}(t,e^{x})+1\bigg)\big(1-e^{z}\big), |  |

while for any z∈(ln⁡b​(t)−x,0)z\in(\ln b(t)-x,0), we have from the convexity of P​(t,⋅)P(t,\cdot) that

|  |  |  |
| --- | --- | --- |
|  | P​(t,ex+z)−P​(t,ex)−ex​∂+P∂s​(t,ex)​(ez−1)≤ex​(ez−1)​(∂+P∂s​(t,ex+z)−∂+P∂s​(t,ex)).\displaystyle P(t,e^{x+z})-P(t,e^{x})-e^{x}\frac{\partial\_{+}P}{\partial s}(t,e^{x})\big(e^{z}-1\big)\leq e^{x}\big(e^{z}-1\big)\bigg(\frac{\partial\_{+}P}{\partial s}\big(t,e^{x+z}\big)-\frac{\partial\_{+}P}{\partial s}(t,e^{x})\bigg). |  |

Hence, we deduce that, for any t∈(0,T)t\in(0,T) and x∈(ln⁡b​(t),ln⁡be​(t))x\in(\ln b(t),\ln b\_{e}(t)),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℐ​(t,x)\displaystyle\mathcal{I}(t,x) | ≤ex​(∂+P∂s​(t,ex)+1)​∫(−∞,ln⁡b​(t)−x](1−ez)​ν​(d​z)\displaystyle\leq e^{x}\bigg(\frac{\partial\_{+}P}{\partial s}(t,e^{x})+1\bigg)\int\_{(-\infty,\ln b(t)-x]}\big(1-e^{z}\big)\,\nu(dz) |  | (4.21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ex​∫(ln⁡b​(t)−x,0)(ez−1)​(∂+P∂s​(t,ex+z)−∂+P∂s​(t,ex))​ν​(d​z).\displaystyle\quad+e^{x}\int\_{(\ln b(t)-x,0)}\big(e^{z}-1\big)\bigg(\frac{\partial\_{+}P}{\partial s}\big(t,e^{x+z}\big)-\frac{\partial\_{+}P}{\partial s}(t,e^{x})\bigg)\nu(dz). |  | (4.22) |

For any t∈(0,T)t\in(0,T) and ξ∈(0,ln⁡(be​(t)/b​(t)))\xi\in(0,\ln(b\_{e}(t)/b(t))), we set gt​(ξ):=P​(t,b​(t)​eξ)g\_{t}(\xi):=P(t,b(t)e^{\xi}) and its right-derivative is

|  |  |  |  |
| --- | --- | --- | --- |
|  | gt+′​(ξ):=d+​gt​(ξ)d​ξ=b​(t)​eξ​∂+P∂s​(t,b​(t)​eξ),\displaystyle g\_{t+}^{\prime}(\xi):=\frac{d\_{+}g\_{t}(\xi)}{d\xi}=b(t)e^{\xi}\,\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{\xi}\big), |  | (4.23) |

Due to the smooth-pasting property when σ>0\sigma>0 (cf. [[6](https://arxiv.org/html/2512.17791v1#bib.bib6), Proposition 4.1 & Theorem 4.1]), gt′​(0)g\_{t}^{\prime}(0) exists and gt′​(0)=gt+′​(0)=−b​(t)g\_{t}^{\prime}(0)=g\_{t+}^{\prime}(0)=-b(t). By the non-increasing property and the convexity of P​(t,⋅)P(t,\cdot) on ℝ+\mathbb{R}\_{+} as well as the smooth-pasting property, we also have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |gt+′​(ξ)|≤be​(t)​(−∂+P∂s​(t,b​(t)​eξ))≤be​(t)​(−∂+P∂s​(t,b​(t)))≤be​(t)≤K.\displaystyle\big|g\_{t+}^{\prime}(\xi)\big|\leq b\_{e}(t)\bigg(\!-\!\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{\xi}\big)\bigg)\leq b\_{e}(t)\bigg(\!-\!\frac{\partial\_{+}P}{\partial s}\big(t,b(t)\big)\bigg)\leq b\_{e}(t)\leq K. |  | (4.24) |

Using these notations and with x=ln⁡b​(t)+ξx=\ln b(t)+\xi, we can rewrite ([4.22](https://arxiv.org/html/2512.17791v1#S4.E22 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(t,x)\displaystyle\mathcal{I}\big(t,x\big) | ≤(gt+′​(ξ)−gt′​(0)​eξ)​∫(−∞,−ξ](1−ez)​ν​(d​z)+∫(−ξ,0)(gt+′​(ξ)−gt+′​(ξ+z)​e−z)​(1−ez)​ν​(d​z).\displaystyle\leq\big(g\_{t+}^{\prime}(\xi)-g\_{t}^{\prime}(0)e^{\xi}\big)\!\int\_{(-\infty,-\xi]}\!\big(1-e^{z}\big)\,\nu(dz)+\!\int\_{(-\xi,0)}\!\big(g\_{t+}^{\prime}(\xi)-g\_{t+}^{\prime}(\xi+z)e^{-z}\big)\big(1-e^{z}\big)\,\nu(dz). |  |

Note that for any ε∈(0,∞)\varepsilon\in(0,\infty), since ξ∈(0,ln⁡(be​(t)/b​(t)))\xi\in(0,\ln(b\_{e}(t)/b(t))),

|  |  |  |  |
| --- | --- | --- | --- |
|  | (eξ−1)​∫(−∞,−ξ](1−ez)​ν​(d​z)\displaystyle\big(e^{\xi}-1\big)\int\_{(-\infty,-\xi]}\!\big(1-e^{z}\big)\,\nu(dz) | ≤(eξ−1)​ν​((−∞,−ε])+∫(−ε,0)(e−z−1)​(1−ez)​ν​(d​z)\displaystyle\leq\big(e^{\xi}-1\big)\nu((-\infty,-\varepsilon])+\int\_{(-\varepsilon,0)}\big(e^{-z}-1\big)\big(1-e^{z}\big)\,\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(be​(t)b​(t)−1)​ν​((−∞,−ε])+∫(−ε,0)(e−z−1)​(1−ez)​ν​(d​z),\displaystyle\leq\bigg(\frac{b\_{e}(t)}{b(t)}-1\bigg)\nu((-\infty,-\varepsilon])+\int\_{(-\varepsilon,0)}\big(e^{-z}-1\big)\big(1-e^{z}\big)\,\nu(dz), |  |

and so, by ([2.6](https://arxiv.org/html/2512.17791v1#S2.E6 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and Theorem [2.5](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")-(a), we have

|  |  |  |
| --- | --- | --- |
|  | limt→T−supξ∈(0,ln⁡(be​(t)/b​(t)))(eξ−1)​∫(−∞,−ξ](1−ez)​ν​(d​z)=0.\displaystyle\lim\_{t\rightarrow T^{-}}\sup\_{\xi\in(0,\ln(b\_{e}(t)/b(t)))}\big(e^{\xi}-1\big)\int\_{(-\infty,-\xi]}\!\big(1-e^{z}\big)\,\nu(dz)=0. |  |

Therefore, we obtain that, for any x∈(ln⁡b​(t),ln⁡be​(t))x\in(\ln b(t),\ln b\_{e}(t)),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(t,x)≤𝒥1​(t,x)+𝒥2​(t,x)+o​(1),t→T−,\displaystyle\mathcal{I}\big(t,x\big)\leq\mathcal{J}\_{1}(t,x)+\mathcal{J}\_{2}(t,x)+o(1),\quad t\rightarrow T^{-}, |  | (4.25) |

where, for any ξ∈(0,ln⁡(be​(t)/b​(t)))\xi\in(0,\ln(b\_{e}(t)/b(t))),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥1​(t,x)\displaystyle\mathcal{J}\_{1}(t,x) | :=𝒥~1​(t,x−ln⁡b​(t)),𝒥~1​(t,ξ):=(gt+′​(ξ)−gt′​(0))​∫(−∞,−ξ](1−ez)​ν​(d​z),\displaystyle:=\widetilde{\mathcal{J}}\_{1}(t,x-\ln b(t)),\quad{\widetilde{\mathcal{J}}\_{1}(t,\xi)}:=\big(g\_{t+}^{\prime}(\xi)-g\_{t}^{\prime}(0)\big)\int\_{(-\infty,-\xi]}\big(1-e^{z}\big)\,\nu(dz), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥2​(t,x)\displaystyle\mathcal{J}\_{2}(t,x) | :=𝒥~2​(t,x−ln⁡b​(t)),𝒥~2​(t,ξ):=∫(−ξ,0)(gt+′​(ξ)−gt+′​(ξ+z)​e−z)​(1−ez)​ν​(d​z).\displaystyle:=\widetilde{\mathcal{J}}\_{2}(t,x-\ln b(t)),\quad{\widetilde{\mathcal{J}}\_{2}(t,\xi)}:=\int\_{(-\xi,0)}\big(g\_{t+}^{\prime}(\xi)-g\_{t+}^{\prime}(\xi+z)e^{-z}\big)\big(1-e^{z}\big)\,\nu(dz).\quad |  |

By combining ([4.20](https://arxiv.org/html/2512.17791v1#S4.E20 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([4.25](https://arxiv.org/html/2512.17791v1#S4.E25 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), there exists ρ∈(0,T)\rho\in(0,T) such that, in the sense of distribution,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​K4≤𝒥1+𝒥2+σ22​(∂2P~∂x2−∂P~∂x)​ on ​𝒞~ρ.\displaystyle\frac{dK}{4}\leq\mathcal{J}\_{1}+\mathcal{J}\_{2}+\frac{\sigma^{2}}{2}\bigg(\frac{\partial^{2}\widetilde{P}}{\partial x^{2}}-\frac{\partial\widetilde{P}}{\partial x}\bigg)\,\,\,\text{ on }\,\widetilde{\mathcal{C}}\_{\rho}. |  | (4.26) |

Using the continuity of P:[0,T]×ℝ+→ℝP:[0,T]\times\mathbb{R}\_{+}\rightarrow\mathbb{R}, and the convexity of P​(t,⋅)P(t,\cdot), we can prove that (see Appendix [A](https://arxiv.org/html/2512.17791v1#A1 "Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), for any t∈(T−ρ,T)t\in(T-\rho,T) and a∈(0,ln⁡(be​(t)/b​(t)))a\in(0,\ln(b\_{e}(t)/b(t))),

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​K​a4\displaystyle\frac{dKa}{4} | ≤∫ln⁡b​(t)a+ln⁡b​(t)𝒥1​(t,x)​𝑑x+∫ln⁡b​(t)a+ln⁡b​(t)𝒥2​(t,x)​𝑑x+σ2​b​(t)​ea2​(∂+P​(t,b​(t)​ea)∂s+1)\displaystyle\leq\int\_{\ln b(t)}^{a+\ln b(t)}\mathcal{J}\_{1}(t,x)\,dx+\int\_{\ln b(t)}^{a+\ln b(t)}\mathcal{J}\_{2}(t,x)\,dx+\frac{\sigma^{2}b(t)e^{a}}{2}\bigg(\frac{\partial\_{+}P(t,b(t)e^{a})}{\partial s}+1\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0a𝒥~1​(t,ξ)​𝑑ξ+∫0a𝒥~2​(t,ξ)​𝑑ξ+σ2​b​(t)​ea2​(∂+P​(t,b​(t)​ea)∂s+1).\displaystyle=\int\_{0}^{a}\widetilde{\mathcal{J}}\_{1}(t,\xi)\,d\xi+\int\_{0}^{a}\widetilde{\mathcal{J}}\_{2}(t,\xi)\,d\xi+\frac{\sigma^{2}b(t)e^{a}}{2}\bigg(\frac{\partial\_{+}P(t,b(t)e^{a})}{\partial s}+1\bigg). |  | (4.27) |

We now estimate the first two integrals on the right-hand side of ([4.27](https://arxiv.org/html/2512.17791v1#S4.E27 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). To begin with, in order to estimate the integral of 𝒥~1\widetilde{\mathcal{J}}\_{1}, we first have, for any ξ∈(0,a)\xi\in(0,a),

|  |  |  |
| --- | --- | --- |
|  | gt+′​(ξ)=b​(t)​eξ​∂+P∂s​(t,b​(t)​eξ)≤b​(t)​eξ​∂+P∂s​(t,b​(t)​ea)=eξ−a​gt+′​(a)≤e−a​gt+′​(a),\displaystyle g\_{t+}^{\prime}(\xi)=b(t)e^{\xi}\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{\xi}\big)\leq b(t)e^{\xi}\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{a}\big)=e^{\xi-a}g\_{t+}^{\prime}(a)\leq e^{-a}g\_{t+}^{\prime}(a), |  |

where the first inequality follows from the convexity of P​(t,⋅)P(t,\cdot) and the last inequality follows from the fact that gt+′​(a)≤0g\_{t+}^{\prime}(a)\leq 0 (since ∂+P/∂s≤0\partial\_{+}P/\partial s\leq 0). In addition, with the help of the convexity of P​(t,⋅)P(t,\cdot) and the smooth-pasting property, we also have, for any a>0a>0,

|  |  |  |
| --- | --- | --- |
|  | e−a​gt+′​(a)−gt+′​(0)=b​(t)​(1+∂+P∂s​(t,b​(t)​ea))≥b​(t)​(1+∂+P∂s​(t,b​(t)))=0,\displaystyle e^{-a}g\_{t+}^{\prime}(a)-g\_{t+}^{\prime}(0)=b(t)\bigg(1+\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{a}\big)\bigg)\geq b(t)\bigg(1+\frac{\partial\_{+}P}{\partial s}\big(t,b(t)\big)\bigg)=0, |  |

Hence, we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0a𝒥~1​(t,ξ)​𝑑ξ\displaystyle\int\_{0}^{a}\widetilde{\mathcal{J}}\_{1}(t,\xi)\,d\xi | ≤(e−a​gt+′​(a)−gt′​(0))​∫0a(∫(−∞,−ξ](1−ez)​ν​(d​z))​𝑑ξ\displaystyle\leq\big(e^{-a}g\_{t+}^{\prime}(a)-g\_{t}^{\prime}(0)\big)\int\_{0}^{a}\bigg(\int\_{(-\infty,-\xi]}\big(1-e^{z}\big)\,\nu(dz)\bigg)d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(e−a​gt+′​(a)−gt′​(0))​(a​∫(−∞,−a)(1−ez)​ν​(d​z)+∫[−a,0)z​(ez−1)​ν​(d​z))\displaystyle=\big(e^{-a}g\_{t+}^{\prime}(a)-g\_{t}^{\prime}(0)\big)\bigg(a\int\_{(-\infty,-a)}\big(1-e^{z}\big)\,\nu(dz)+\int\_{[-a,0)}z\big(e^{z}-1\big)\,\nu(dz)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(e−a​gt+′​(a)−gt′​(0))​(−a​∫(−∞,−a)z​ν​(d​z)+∫[−a,0)z2​ν​(d​z)).\displaystyle\leq\big(e^{-a}g\_{t+}^{\prime}(a)-g\_{t}^{\prime}(0)\big)\bigg(\!-\!a\int\_{(-\infty,-a)}z\,\nu(dz)+\int\_{[-a,0)}z^{2}\,\nu(dz)\bigg). |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤lim supa→0+∫(−∞,−a)(−a​z)​ν​(d​z)\displaystyle 0\leq\limsup\_{a\rightarrow 0^{+}}\int\_{(-\infty,-a)}(-az)\,\nu(dz) | =limε→0+lim supa→0+(∫(−∞,−ε)+∫[−ε,−a))​(−a​z)​ν​(d​z)\displaystyle=\lim\_{\varepsilon\rightarrow 0^{+}}\limsup\_{a\rightarrow 0^{+}}\bigg(\int\_{(-\infty,-\varepsilon)}+\int\_{[-\varepsilon,-a)}\bigg)(-az)\,\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤limε→0+lim supa→0+(∫(−∞,−ε)(−a​z)​ν​(d​z)+∫[−ε,0)z2​ν​(d​z))=0,\displaystyle\leq\lim\_{\varepsilon\rightarrow 0^{+}}\limsup\_{a\rightarrow 0^{+}}\bigg(\int\_{(-\infty,-\varepsilon)}(-az)\,\nu(dz)+\int\_{[-\varepsilon,0)}z^{2}\,\nu(dz)\bigg)=0, |  |

we obtain that, as a→0+a\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0a𝒥~1​(t,ξ)​𝑑ξ≤(e−a​gt+′​(a)−gt′​(0))​o​(1)≤gt+′​(a)−gt′​(0)+o​(a).\displaystyle\int\_{0}^{a}\widetilde{\mathcal{J}}\_{1}(t,\xi)\,d\xi\leq\big(e^{-a}g\_{t+}^{\prime}(a)-g\_{t}^{\prime}(0)\big)o(1)\leq g\_{t+}^{\prime}(a)-g\_{t}^{\prime}(0)+o(a). |  | (4.28) |

As for the integral of 𝒥~2\widetilde{\mathcal{J}}\_{2} in ([4.27](https://arxiv.org/html/2512.17791v1#S4.E27 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we first have

|  |  |  |
| --- | --- | --- |
|  | ∫0a𝒥~2​(t,ξ)​𝑑ξ≤∫0a(∫(−ξ,0)(gt+′​(ξ)−gt+′​(ξ+z)​e−z)​(−z)​ν​(d​z))​𝑑ξ\displaystyle\int\_{0}^{a}\widetilde{\mathcal{J}}\_{2}(t,\xi)\,d\xi\leq\int\_{0}^{a}\bigg(\int\_{(-\xi,0)}\big(g\_{t+}^{\prime}(\xi)-g\_{t+}^{\prime}(\xi+z)e^{-z}\big)(-z)\,\nu(dz)\bigg)d\xi |  |
|  |  |  |
| --- | --- | --- |
|  | =∫(−a,0)(−z)​(∫−za(gt+′​(ξ)−gt+′​(ξ+z)​e−z)​𝑑ξ)​ν​(d​z)\displaystyle\quad=\int\_{(-a,0)}(-z)\bigg(\int\_{-z}^{a}\big(g\_{t+}^{\prime}(\xi)-g\_{t+}^{\prime}(\xi+z)e^{-z}\big)\,d\xi\bigg)\nu(dz) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫(−a,0)(−z)​(gt​(a)−gt​(a+z)​e−z−gt​(−z)+gt​(0)​e−z)​ν​(d​z)\displaystyle\quad=\int\_{(-a,0)}(-z)\big(g\_{t}(a)-g\_{t}(a+z)e^{-z}-g\_{t}(-z)+g\_{t}(0)e^{-z}\big)\,\nu(dz) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫(−a,0)(−z)​(gt​(a)−gt​(a+z)−gt​(−z)+gt​(0))​ν​(d​z)+∫(−a,0)(−z)​(gt​(0)−gt​(a+z))​(e−z−1)​ν​(d​z).\displaystyle\quad=\int\_{(-a,0)}\!\!(-z)\big(g\_{t}(a)\!-\!g\_{t}(a\!+\!z)\!-\!g\_{t}(-z)\!+\!g\_{t}(0)\big)\nu(dz)+\!\int\_{(-a,0)}\!\!(-z)\big(g\_{t}(0)\!-\!g\_{t}(a\!+\!z)\big)\big(e^{-z}\!-\!1\big)\nu(dz). |  |

By ([4.23](https://arxiv.org/html/2512.17791v1#S4.E23 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and the nonincreasing property and the convexity of P​(t,⋅)P(t,\cdot), we have, for any z∈(−a,0)z\in(-a,0),

|  |  |  |  |
| --- | --- | --- | --- |
|  | gt​(a)−gt​(a+z)\displaystyle g\_{t}(a)-g\_{t}(a+z) | =∫z0gt+′​(a+y)​𝑑y=∫z0b​(t)​ea+y​∂+P∂s​(t,b​(t)​ea+y)​𝑑y\displaystyle=\int\_{z}^{0}g\_{t+}^{\prime}(a+y)\,dy=\int\_{z}^{0}b(t)e^{a+y}\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{a+y}\big)\,dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤b​(t)​∂+P∂s​(t,b​(t)​ea)​∫z0ea+y​𝑑y≤b​(t)​∂+P∂s​(t,b​(t)​ea)​(−z)=gt+′​(a)​e−a​(−z),\displaystyle\leq b(t)\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{a}\big)\int\_{z}^{0}e^{a+y}\,dy\leq b(t)\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{a}\big)(-z)=g\_{t+}^{\prime}(a)e^{-a}(-z), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | gt​(−z)−gt​(0)\displaystyle g\_{t}(-z)-g\_{t}(0) | =∫0−zgt+′​(y)​𝑑y=∫0−zb​(t)​ey​∂+P∂s​(t,b​(t)​ey)​𝑑y\displaystyle=\int\_{0}^{-z}g\_{t+}^{\prime}(y)\,dy=\int\_{0}^{-z}b(t)e^{y}\frac{\partial\_{+}P}{\partial s}\big(t,b(t)e^{y}\big)\,dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥b​(t)​∂+P∂s​(t,b​(t))​∫0−zey​𝑑y≥b​(t)​∂+P∂s​(t,b​(t))​(−z)​e−z=gt′​(0)​(−z)​e−z.\displaystyle\geq b(t)\frac{\partial\_{+}P}{\partial s}\big(t,b(t)\big)\int\_{0}^{-z}e^{y}\,dy\geq b(t)\frac{\partial\_{+}P}{\partial s}\big(t,b(t)\big)(-z)e^{-z}=g\_{t}^{\prime}(0)(-z)e^{-z}. |  |

Together with ([4.24](https://arxiv.org/html/2512.17791v1#S4.E24 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that, as a→0+a\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫0a𝒥~2​(t,ξ)​𝑑ξ≤∫(−a,0)z2​(gt+′​(a)​e−a−gt′​(0)​e−z)​ν​(d​z)+supz∈(0,a)|gt+′​(z)|​∫(−a,0)(−z)​(a+z)​(e−z−1)​ν​(d​z)\displaystyle\int\_{0}^{a}\widetilde{\mathcal{J}}\_{2}(t,\xi)\,d\xi\!\leq\!\!\int\_{(-a,0)}\!\!z^{2}\big(g\_{t+}^{\prime}(a)e^{-a}\!-\!g\_{t}^{\prime}(0)e^{-z}\big)\nu(dz)\!+\!\!\sup\_{z\in(0,a)}\!\big|g\_{t+}^{\prime}(z)\big|\!\int\_{(-a,0)}\!\!(-z)(a\!+\!z)\big(e^{-z}\!-\!1\big)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(e−a​gt+′​(a)−gt′​(0))​∫(−a,0)z2​ν​(d​z)−gt′​(0)​∫(−a,0)z2​(e−z−1)​ν​(d​z)−K​a​∫(−a,0)z​(e−z−1)​ν​(d​z)\displaystyle\quad\leq\big(e^{-a}g\_{t+}^{\prime}(a)\!-\!g\_{t}^{\prime}(0)\big)\!\int\_{(-a,0)}\!z^{2}\nu(dz)-g\_{t}^{\prime}(0)\!\int\_{(-a,0)}\!z^{2}\big(e^{-z}\!-\!1\big)\nu(dz)-Ka\!\int\_{(-a,0)}\!z\big(e^{-z}\!-\!1\big)\nu(dz) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(e−a​gt+′​(a)−gt′​(0))​o​(1)+o​(a)≤gt+′​(a)−gt′​(0)+o​(a).\displaystyle\quad=\big(e^{-a}g\_{t+}^{\prime}(a)-g\_{t}^{\prime}(0)\big)o(1)+o(a)\leq g\_{t+}^{\prime}(a)-g\_{t}^{\prime}(0)+o(a). |  | (4.29) |

By combining ([4.27](https://arxiv.org/html/2512.17791v1#S4.E27 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([4.28](https://arxiv.org/html/2512.17791v1#S4.E28 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([4.29](https://arxiv.org/html/2512.17791v1#S4.E29 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that there exists ρ∈(0,∞)\rho\in(0,\infty) such that, when t∈(T−ρ,T)t\in(T-\rho,T), for any x∈(ln⁡b​(t),ln⁡be​(t))x\in(\ln b(t),\ln b\_{e}(t)),

|  |  |  |
| --- | --- | --- |
|  | d​(x−ln⁡b​(t))6≤gt+′​(x−ln⁡b​(t))−gt′​(0)+σ2​ex4​(∂+P​(t,ex)∂s+1).\displaystyle\frac{d\big(x-\ln b(t)\big)}{6}\leq g\_{t+}^{\prime}\big(x-\ln b(t)\big)-g\_{t}^{\prime}(0)+\frac{\sigma^{2}e^{x}}{4}\bigg(\frac{\partial\_{+}P(t,e^{x})}{\partial s}+1\bigg). |  |

thus, setting at:=ln⁡(be​(t)/b​(t))a\_{t}:=\ln(b\_{e}(t)/b(t)),

|  |  |  |
| --- | --- | --- |
|  | d​(ln⁡be​(t)−ln⁡b​(t))212≤∫ln⁡b​(t)ln⁡be​(t)(gt+′​(x−ln⁡b​(t))−gt′​(0))​𝑑x+σ24​∫ln⁡b​(t)ln⁡be​(t)ex​(∂+P​(t,ex)∂s+1)​𝑑x\displaystyle\frac{d\big(\ln b\_{e}(t)-\ln b(t)\big)^{2}}{12}\leq\int\_{\ln b(t)}^{\ln b\_{e}(t)}\Big(g\_{t+}^{\prime}\big(x-\ln b(t)\big)-g\_{t}^{\prime}(0)\Big)dx+\frac{\sigma^{2}}{4}\int\_{\ln b(t)}^{\ln b\_{e}(t)}e^{x}\bigg(\frac{\partial\_{+}P(t,e^{x})}{\partial s}+1\bigg)dx |  |
|  |  |  |
| --- | --- | --- |
|  | =gt​(at)−gt​(0)−gt′​(0)​at+σ24​(P​(t,be​(t))−P​(t,b​(t))+be​(t)−b​(t))\displaystyle\quad=g\_{t}(a\_{t})-g\_{t}(0)-g\_{t}^{\prime}(0)a\_{t}+\frac{\sigma^{2}}{4}\big(P(t,b\_{e}(t))-P(t,b(t))+b\_{e}(t)-b(t)\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =P​(t,be​(t))−P​(t,b​(t))+b​(t)​ln⁡(be​(t)b​(t))+σ24​(P​(t,be​(t))−P​(t,b​(t))+be​(t)−b​(t))\displaystyle\quad=P\big(t,b\_{e}(t)\big)-P\big(t,b(t)\big)+b(t)\ln\bigg(\frac{b\_{e}(t)}{b(t)}\bigg)+\frac{\sigma^{2}}{4}\big(P(t,b\_{e}(t))-P(t,b(t))+b\_{e}(t)-b(t)\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(1+σ24)​(P​(t,be​(t))−(K−b​(t))+be​(t)−b​(t))=(1+σ24)​(P​(t,be​(t))−Pe​(t,be​(t))),\displaystyle\quad\leq\bigg(1+\frac{\sigma^{2}}{4}\bigg)\Big(P\big(t,b\_{e}(t)\big)-\big(K-b(t)\big)+b\_{e}(t)-b(t)\Big)=\bigg(1+\frac{\sigma^{2}}{4}\bigg)\Big(P\big(t,b\_{e}(t)\big)-P\_{e}\big(t,b\_{e}(t)\big)\Big), |  |

where we used ln⁡(1+x)≤x\ln(1+x)\leq x for x>0x>0 in the second inequality. Therefore, by the early exercise premium formula (cf. [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Theorem 3.1 & Remark 3.1]), we obtain that, for any t∈(T−ρ,T)t\in(T-\rho,T),

|  |  |  |
| --- | --- | --- |
|  | d​(ln⁡be​(t)−b​(t))212≤r​K​(T−t)​(1+σ24),\displaystyle\frac{d\big(\ln b\_{e}(t)-b(t)\big)^{2}}{12}\leq rK(T-t)\bigg(1+\frac{\sigma^{2}}{4}\bigg), |  |

and thus

|  |  |  |
| --- | --- | --- |
|  | lim supt→T−be​(t)−b​(t)T−t=lim supt→T−ln⁡(be​(t)/b​(t))T−t<∞,\displaystyle\limsup\_{t\rightarrow T^{-}}\frac{b\_{e}(t)-b(t)}{\sqrt{T-t}}=\limsup\_{t\rightarrow T^{-}}\frac{\ln(b\_{e}(t)/b(t))}{\sqrt{T-t}}<\infty, |  |

which completes the proof of the proposition. □\Box

Proof of Theorem 4.1. In view of Proposition [4.9](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem9 "Proposition 4.9. ‣ 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), clearly we have

|  |  |  |
| --- | --- | --- |
|  | K−b​(t)=K−be​(t)+be​(t)−b​(t)=K−be​(t)+O​(T−t),t→T−.\displaystyle K-b(t)=K-b\_{e}(t)+b\_{e}(t)-b(t)=K-b\_{e}(t)+O\big(\sqrt{T-t}\big),\quad t\rightarrow T^{-}. |  |

Moreover, by ([4.3](https://arxiv.org/html/2512.17791v1#S4.E3 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and Proposition [4.4](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") and noting that limt→T−be​(t)=K\lim\_{t\rightarrow T^{-}}b\_{e}(t)=K, we have

|  |  |  |
| --- | --- | --- |
|  | limt→T−K−be​(t)K​−(T−t)​ln⁡(T−t)=limt→T−K−be​(t)be​(t)​−(T−t)​ln⁡(T−t)=limτ→0+ζ​(τ)−τ​ln⁡τ=σ,\displaystyle\lim\_{t\rightarrow T^{-}}\frac{K-b\_{e}(t)}{K\sqrt{-(T-t)\ln(T-t)}}=\lim\_{t\rightarrow T^{-}}\frac{K-b\_{e}(t)}{b\_{e}(t)\sqrt{-(T-t)\ln(T-t)}}=\lim\_{\tau\rightarrow 0^{+}}\frac{\zeta(\tau)}{\sqrt{-\tau\ln\tau}}=\sigma, |  |

which completes the proof of the theorem. □\Box

## 5. New Results on the Rate of Convergence of the Critical Price when d<0d<0

In this section, we consider the rate of convergence of critical boundary bb near maturity when σ>0\sigma>0 and d<0d<0. We first assume that XX has a jump component of finite variation, i.e., ([3.2](https://arxiv.org/html/2512.17791v1#S3.E2 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) holds true. In this case, the model ([2.1](https://arxiv.org/html/2512.17791v1#S2.E1 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​e(r−δ)​t+Xt=S0​eX~t,X~t:=(r−δ)​t+Xt=(γ0−σ22)​t+σ​Wt+Zt,t∈ℝ+,\displaystyle S\_{t}=S\_{0}\,e^{(r-\delta)t+X\_{t}}=S\_{0}\,e^{\widetilde{X}\_{t}},\quad\widetilde{X}\_{t}:=(r-\delta)t+X\_{t}=\bigg(\gamma\_{0}-\frac{\sigma^{2}}{2}\bigg)t+\sigma W\_{t}+Z\_{t},\quad t\in\mathbb{R}\_{+}, |  | (5.1) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ0:=r−δ−∫ℝ0(ex−1)​ν​(d​x),Zt=∫0t∫ℝ0z​N​(d​s,d​z).\displaystyle\gamma\_{0}:=r-\delta-\int\_{\mathbb{R}\_{0}}\big(e^{x}-1\big)\nu(dx),\quad Z\_{t}=\int\_{0}^{t}\int\_{\mathbb{R}\_{0}}z\,N(ds,dz). |  | (5.2) |

###### Assumption 5.1.

Throughout this section, we make the following standard assumption:

|  |  |  |
| --- | --- | --- |
|  | ν​(d​z)=s​(z)​d​z, for some ​s∈C​(ℝ0).\displaystyle\nu(dz)=s(z)\,dz,\quad\text{ for some }\,s\in C(\mathbb{R}\_{0}). |  |

We begin with the following lemma which provides an estimation of the expectation of LtKL\_{t}^{K}, the local time of the process SS at KK until time tt, for small t>0t>0. The proof is deferred to Appendix [B](https://arxiv.org/html/2512.17791v1#A2 "Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models").

###### Lemma 5.2.

Let S0=b​(T)​ea​θS\_{0}=b(T)e^{a\sqrt{\theta}} with a∈(−∞,0)a\in(-\infty,0). If b​(T)<Kb(T)<K, then we have, for any 𝔽\mathbb{F}-stopping time τ\tau taking values in [0,θ][0,\theta],

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(LτK)=2​K​𝔼​(((−a​θ−σ​Wτ)+−(−a​θ−σ​WT^1)+)​𝟏{T^1<τ})+o​(θ3/2)≤ω0​θ3/2,\displaystyle\mathbb{E}\big(L\_{\tau}^{K}\big)=2K\,\mathbb{E}\Big(\Big(\big(\!-\!a\sqrt{\theta}-\sigma W\_{\tau}\big)^{+}-\big(\!-\!a\sqrt{\theta}-\sigma W\_{\widehat{T}\_{1}}\big)^{+}\Big){\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\Big)+o\big(\theta^{3/2}\big)\leq\omega\_{0}\,\theta^{3/2}, |  | (5.3) |

as θ→0+\theta\rightarrow 0^{+}, where T^1:=inf{s∈ℝ+:Δ​Ls=ln⁡(K/b​(T))}\widehat{T}\_{1}:=\inf\{s\in\mathbb{R}\_{+}:\Delta L\_{s}=\ln(K/b(T))\} and ω0∈(0,∞)\omega\_{0}\in(0,\infty) is independent of aa.

The following theorem provides a second-order near-maturity expansion for the American put price PP around b​(T)b(T) along a certain parabolic branch, which serves as a key step to derive the convergence rate of the critical price. This is similar to Theorem 3.1 in [[2](https://arxiv.org/html/2512.17791v1#bib.bib2)], where only jumps of finite-activity were considered.

###### Theorem 5.3.

Let d<0d<0. For any a∈(−∞,0)a\in(-\infty,0), we have

|  |  |  |
| --- | --- | --- |
|  | P​(T−θ,b​(T)​ea​θ)=(K−b​(T)​ea​θ)++σ​b​(T)​δ¯​eλ​vλ,β​(a/σ)​θ3/2+o​(θ3/2),\displaystyle P\big(T-\theta,b(T)e^{a\sqrt{\theta}}\big)=\big(K-b(T)e^{a\sqrt{\theta}}\big)^{+}+\sigma b(T)\bar{\delta}e^{\lambda}v\_{\lambda,\beta}(a/\sigma)\theta^{3/2}+o\big(\theta^{3/2}\big), |  |

as θ→0+\theta\rightarrow 0^{+}, where λ=ν​({ln⁡(K/b​(T))})\lambda=\nu(\{\ln(K/b(T))\}), δ¯=δ+∫(ln⁡(K/b​(T)),∞)ez​ν​(d​z)\bar{\delta}=\delta+\int\_{(\ln(K/b(T)),\infty)}e^{z}\nu(dz), and vλ,βv\_{\lambda,\beta} is defined as in ([3.1](https://arxiv.org/html/2512.17791v1#S3.E1 "In item (c) ‣ Theorem 3.1. ‣ 3.1. Finite Jump Activity Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) with β=K/(b​(T)​δ¯)\beta=K/(b(T)\bar{\delta}).

Proof. By Itô-Meyer’s formula (see, e,g,, Theorem 70 in [[13](https://arxiv.org/html/2512.17791v1#bib.bib13), Chapter IV]) and the product formula for semimartingales, for any 𝔽\mathbb{F}-stopping time τ∈𝒯0,θ\tau\in\mathscr{T}\_{0,\theta} and with S0=b​(T)​ea​θS\_{0}=b(T)e^{a\sqrt{\theta}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(e−r​τ​(K−Sτ)+)−(K−b​(T)​ea​θ)+=ℐa​(τ)+𝒥a​(τ),\displaystyle\mathbb{E}\big(e^{-r\tau}(K-S\_{\tau})^{+}\big)-\big(K-b(T)e^{a\sqrt{\theta}}\big)^{+}=\mathcal{I}^{a}(\tau)+\mathcal{J}^{a}(\tau), |  | (5.4) |

where (recalling Φ​(y,z):=(K−y​ez)+−(K−y)+\Phi(y,z):=(K-ye^{z})^{+}-(K-y)^{+})

|  |  |  |
| --- | --- | --- |
|  | ℐa​(τ):=𝔼​(∫0τe−r​t​(𝟏{St≤K}​(r​(St−K)−γ0​St)+∫ℝ0Φ​(St,z)​ν​(d​z))​𝑑t),𝒥a​(τ):=12​𝔼​(∫0τe−r​s​𝑑LsK).\displaystyle\mathcal{I}^{a}(\tau)\!:=\!\mathbb{E}\!\left(\int\_{0}^{\tau}\!e^{-rt}\!\bigg(\!{\bf 1}\_{\{S\_{t}\leq K\}}\!\big(r(S\_{t}\!-\!K)\!-\!\gamma\_{0}S\_{t}\big)\!+\!\!\int\_{\mathbb{R}\_{0}}\!\!\Phi(S\_{t},z)\nu(dz)\!\bigg)dt\!\right)\!,\,\,\,\mathcal{J}^{a}(\tau)\!:=\!\frac{1}{2}\mathbb{E}\bigg(\!\int\_{0}^{\tau}\!e^{-rs}dL\_{s}^{K}\!\bigg). |  |

By Lemma [5.2](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem2 "Lemma 5.2. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") we deduce that222Note that the second term in ([5.5](https://arxiv.org/html/2512.17791v1#S5.E5 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) is o​(θ3/2)o(\theta^{3/2}). Indeed, since s→LsKs\to L\_{s}^{K} is nondecreasing, 0≤1−e−r​s≤r​s0\leq 1-e^{-rs}\leq rs, and τ≤θ\tau\leq\theta, by Lemma [5.2](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem2 "Lemma 5.2. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") we have 𝔼​(∫0τ(1−e−r​s)​𝑑LsK)≤r​θ​𝔼​(LτK)=O​(θ5/2)\mathbb{E}\big(\int\_{0}^{\tau}\big(1-e^{-rs}\big)dL\_{s}^{K}\big)\leq r\theta\,\mathbb{E}\big(L\_{\tau}^{K}\big)=O(\theta^{5/2}).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒥a​(τ)\displaystyle\mathcal{J}^{a}(\tau) | =12​𝔼​(LτK)−12​𝔼​(∫0τ(1−e−r​s)​𝑑LsK)\displaystyle=\frac{1}{2}\,\mathbb{E}\big(L\_{\tau}^{K}\big)-\frac{1}{2}\,\mathbb{E}\bigg(\int\_{0}^{\tau}\big(1-e^{-rs}\big)dL\_{s}^{K}\bigg) |  | (5.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =K​𝔼​(𝟏{T^1<τ}​((−a​θ−σ​Wτ)+−(−a​θ−σ​WT^1)+))+o​(θ3/2),θ→0+,\displaystyle=K\,\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\Big(\big(\!-a\sqrt{\theta}-\sigma W\_{\tau}\big)^{+}-\big(\!-a\sqrt{\theta}-\sigma W\_{\widehat{T}\_{1}}\big)^{+}\Big)\Big)+o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+},\quad |  | (5.6) |

where we recall T^1=inf{t∈ℝ+:Δ​Lt=ln⁡(K/b​(T))}\widehat{T}\_{1}=\inf\{t\in\mathbb{R}\_{+}:\Delta L\_{t}=\ln(K/b(T))\}.

Next, we analyze ℐa​(τ)\mathcal{I}^{a}(\tau). To begin with, for any ε∈(0,∞)\varepsilon\in(0,\infty) and recalling T1ε=inf{t∈ℝ+:|Δ​Xt|>ε}T\_{1}^{\varepsilon}=\inf\{t\in\mathbb{R}\_{+}:|\Delta X\_{t}|>\varepsilon\}, we first have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(∫0τe−r​t​𝟏{St>K}​∫ℝ0Φ​(St,z)​ν​(d​z)​𝑑t)=𝔼​(∫0τe−r​t​𝟏{St>K}​∫ℝ0(K−St​ez)+​ν​(d​z)​𝑑t)\displaystyle\mathbb{E}\bigg(\int\_{0}^{\tau}e^{-rt}{\bf 1}\_{\{S\_{t}>K\}}\int\_{\mathbb{R}\_{0}}\Phi(S\_{t},z)\,\nu(dz)\,dt\bigg)=\mathbb{E}\bigg(\int\_{0}^{\tau}e^{-rt}{\bf 1}\_{\{S\_{t}>K\}}\int\_{\mathbb{R}\_{0}}\big(K-S\_{t}e^{z}\big)^{+}\nu(dz)dt\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​∫ℝ0|1−ez|​ν​(d​z)​∫0θℙ​(St>K)​𝑑t≤K​∫ℝ0|1−ez|​ν​(d​z)​∫0θ(ℙ​(St>K,T1ε>θ)+ℙ​(T1ε≤θ))​𝑑t\displaystyle\leq K\int\_{\mathbb{R}\_{0}}\!\big|1\!-\!e^{z}\big|\nu(dz)\int\_{0}^{\theta}\!\mathbb{P}\big(S\_{t}\!>\!K\big)dt\leq K\int\_{\mathbb{R}\_{0}}\!\big|1\!-\!e^{z}\big|\nu(dz)\int\_{0}^{\theta}\!\Big(\mathbb{P}\big(S\_{t}\!>\!K,T\_{1}^{\varepsilon}\!>\!\theta\big)+\mathbb{P}\big(T\_{1}^{\varepsilon}\!\leq\!\theta\big)\Big)dt |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​θ​∫ℝ0|1−ez|​ν​(d​z)​(ℙ​(supt∈[0,θ]Stε>K)+ℙ​(T1ε≤θ))\displaystyle\leq K\theta\int\_{\mathbb{R}\_{0}}\big|1-e^{z}\big|\nu(dz)\bigg(\mathbb{P}\Big(\sup\_{t\in[0,\theta]}S\_{t}^{\varepsilon}>K\Big)+\mathbb{P}\big(T\_{1}^{\varepsilon}\leq\theta\big)\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | =K​θ​∫ℝ0|1−ez|​ν​(d​z)​(ℙ​(τKε≤θ)+1−e−θ​ν​([−ε,ε]c))=O​(θ2),θ→0+,\displaystyle=K\theta\int\_{\mathbb{R}\_{0}}\big|1-e^{z}\big|\nu(dz)\Big(\mathbb{P}\big(\tau\_{K}^{\varepsilon}\leq\theta\big)+1-e^{-\theta\nu([-\varepsilon,\varepsilon]^{c})}\Big)=O(\theta^{2}),\quad\theta\rightarrow 0^{+}, |  |

where the last equality follows from ([B.7](https://arxiv.org/html/2512.17791v1#A2.E7 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). Together with ([5.2](https://arxiv.org/html/2512.17791v1#S5.E2 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐa​(τ)\displaystyle\mathcal{I}^{a}(\tau) | =𝔼​(∫0τe−r​t​𝟏{St≤K}​((r​(St−K)−γ0​St)+∫ℝ0Φ​(St,z)​ν​(d​z))​𝑑t)+o​(θ3/2)\displaystyle=\mathbb{E}\left(\int\_{0}^{\tau}e^{-rt}{\bf 1}\_{\{S\_{t}\leq K\}}\bigg(\big(r(S\_{t}-K)-\gamma\_{0}S\_{t}\big)+\int\_{\mathbb{R}\_{0}}\Phi(S\_{t},z)\,\nu(dz)\bigg)dt\right)+o\big(\theta^{3/2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(∫0τe−r​t​𝟏{St≤K}​(−r​K+δ​St+∫ℝ0(St​ez−K)+​ν​(d​z))​𝑑t)+o​(θ3/2)\displaystyle=\mathbb{E}\left(\int\_{0}^{\tau}e^{-rt}{\bf 1}\_{\{S\_{t}\leq K\}}\bigg(\!-rK+\delta S\_{t}+\int\_{\mathbb{R}\_{0}}\big(S\_{t}e^{z}-K\big)^{+}\nu(dz)\bigg)dt\right)+o\big(\theta^{3/2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(∫0τ(e−r​t−1)​𝟏{St≤K}​(−r​K+δ​St+∫ℝ0(St​ez−K)+​ν​(d​z))​𝑑t)\displaystyle=\mathbb{E}\left(\int\_{0}^{\tau}\big(e^{-rt}-1\big){\bf 1}\_{\{S\_{t}\leq K\}}\bigg(\!-rK+\delta S\_{t}+\int\_{\mathbb{R}\_{0}}\big(S\_{t}e^{z}-K\big)^{+}\nu(dz)\bigg)dt\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​(∫0τ𝟏{St≤K}​(−r​K+δ​St+∫ℝ0(St​ez−K)+​ν​(d​z))​𝑑t)+o​(θ3/2)\displaystyle\quad+\mathbb{E}\left(\int\_{0}^{\tau}{\bf 1}\_{\{S\_{t}\leq K\}}\bigg(\!-rK+\delta S\_{t}+\int\_{\mathbb{R}\_{0}}\big(S\_{t}e^{z}-K\big)^{+}\nu(dz)\bigg)dt\right)+o\big(\theta^{3/2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(∫0τ𝟏{St≤K}​(−r​K+δ​St+∫ℝ0(St​ez−K)+​ν​(d​z))​𝑑t)+o​(θ3/2),θ→0+,\displaystyle=\mathbb{E}\left(\int\_{0}^{\tau}{\bf 1}\_{\{S\_{t}\leq K\}}\bigg(\!-rK+\delta S\_{t}+\int\_{\mathbb{R}\_{0}}\big(S\_{t}e^{z}-K\big)^{+}\nu(dz)\bigg)dt\right)+o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}, |  |

where we note that

|  |  |  |
| --- | --- | --- |
|  | |𝔼​(∫0τ(e−r​t−1)​𝟏{St≤K}​(−r​K+δ​St+∫ℝ0(St​ez−K)+​ν​(d​z))​𝑑t)|\displaystyle\left|\mathbb{E}\left(\int\_{0}^{\tau}\big(e^{-rt}-1\big){\bf 1}\_{\{S\_{t}\leq K\}}\bigg(\!-rK+\delta S\_{t}+\int\_{\mathbb{R}\_{0}}\big(S\_{t}e^{z}-K\big)^{+}\nu(dz)\bigg)dt\right)\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤((r+δ)​K+K​∫ℝ0|ez−1|​ν​(d​z))​∫0θ(1−e−r​t)​𝑑t=O​(θ2).\displaystyle\quad\leq\bigg((r+\delta)K+K\int\_{\mathbb{R}\_{0}}\big|e^{z}-1\big|\nu(dz)\bigg)\int\_{0}^{\theta}\big(1-e^{-rt}\big)dt=O(\theta^{2}). |  |

Denoting by

|  |  |  |
| --- | --- | --- |
|  | h​(x):=𝟏{x≤ln⁡K}​(−r​K+δ​ex+∫ℝ0(ex+z−K)+​ν​(d​z)),\displaystyle h(x):={\bf 1}\_{\{x\leq\ln K\}}\bigg(\!-rK+\delta e^{x}+\int\_{\mathbb{R}\_{0}}\big(e^{x+z}-K\big)^{+}\nu(dz)\bigg), |  |

and recalling ([5.1](https://arxiv.org/html/2512.17791v1#S5.E1 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) as well as S0=b​(T)​ea​θS\_{0}=b(T)e^{a\sqrt{\theta}}, we thus have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐa​(τ)=𝔼​(∫0τh​(ln⁡b​(T)+a​θ+X~t)​𝑑t)+o​(θ3/2),θ→0+.\displaystyle\mathcal{I}^{a}(\tau)=\mathbb{E}\left(\int\_{0}^{\tau}h\big(\ln b(T)+a\sqrt{\theta}+\widetilde{X}\_{t}\big)\,dt\right)+o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}. |  | (5.7) |

Now we will try to express the expectation in ([5.7](https://arxiv.org/html/2512.17791v1#S5.E7 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) in a more appropriate form. Notice that, for any (fixed) ε∈(0,ln⁡(K/b​(T)))\varepsilon\in(0,\ln(K/b(T))), we have

|  |  |  |
| --- | --- | --- |
|  | |h​(x)−h​(y)|≤|h​(x)−h​(y)|​𝟏{x∨y≤ln⁡K}+|h​(x)|​𝟏{x≤ln⁡K<y}+|h​(y)|​𝟏{y≤ln⁡K<x}\displaystyle\big|h(x)-h(y)\big|\leq\big|h(x)-h(y)\big|{\bf 1}\_{\{x\vee y\leq\ln K\}}+\big|h(x)\big|{\bf 1}\_{\{x\leq\ln K<y\}}+\big|h(y)\big|{\bf 1}\_{\{y\leq\ln K<x\}} |  |
|  |  |  |
| --- | --- | --- |
|  | =|h​(x)−h​(y)|​(𝟏{x∨y≤ln⁡K−ε}+𝟏{x≤ln⁡K−ε<y≤ln⁡K}+𝟏{y≤ln⁡K−ε<x≤ln⁡K}+𝟏{ln⁡K−ε<x,y≤ln⁡K})\displaystyle\quad=\big|h(x)-h(y)\big|\big({\bf 1}\_{\{x\vee y\leq\ln K-\varepsilon\}}+{\bf 1}\_{\{x\leq\ln K-\varepsilon<y\leq\ln K\}}+{\bf 1}\_{\{y\leq\ln K-\varepsilon<x\leq\ln K\}}+{\bf 1}\_{\{\ln K-\varepsilon<x,y\leq\ln K\}}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | +|h​(x)|​𝟏{x≤ln⁡K<y}+|h​(y)|​𝟏{y≤ln⁡K<x}\displaystyle\qquad+\big|h(x)\big|{\bf 1}\_{\{x\leq\ln K<y\}}+\big|h(y)\big|{\bf 1}\_{\{y\leq\ln K<x\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤A0ε​|ex−ey|​𝟏{x∨y≤ln⁡K−ε}+(A0ε​|ex−ey|+A1ε)​(𝟏{x≤ln⁡K−ε<y≤ln⁡K}+𝟏{y≤ln⁡K−ε<x≤ln⁡K})\displaystyle\quad\leq A\_{0}^{\varepsilon}\,\big|e^{x}-e^{y}\big|{\bf 1}\_{\{x\vee y\leq\ln K-\varepsilon\}}+\Big(A\_{0}^{\varepsilon}\,\big|e^{x}-e^{y}\big|+A\_{1}^{\varepsilon}\Big)\big({\bf 1}\_{\{x\leq\ln K-\varepsilon<y\leq\ln K\}}+{\bf 1}\_{\{y\leq\ln K-\varepsilon<x\leq\ln K\}}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | +(A0ε​|ex−ey|+2​A1ε)​𝟏{ln⁡K−ε<x,y≤ln⁡K}+K​(r∨|d|)​(𝟏{x≤ln⁡K<y}+𝟏{y≤ln⁡K<x})\displaystyle\qquad+\Big(A\_{0}^{\varepsilon}\,\big|e^{x}-e^{y}\big|+2A\_{1}^{\varepsilon}\Big){\bf 1}\_{\{\ln K-\varepsilon<x,y\leq\ln K\}}+K(r\vee|d|)\big({\bf 1}\_{\{x\leq\ln K<y\}}+{\bf 1}\_{\{y\leq\ln K<x\}}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤A0ε​|ex−ey|+2​A1ε​𝟏{ln⁡K−ε<x∧y}+K​(r∨|d|)​(𝟏{ln⁡K<y}+𝟏{ln⁡K<x}),\displaystyle\quad\leq A\_{0}^{\varepsilon}\big|e^{x}-e^{y}\big|+2A\_{1}^{\varepsilon}{\bf 1}\_{\{\ln K-\varepsilon<x\wedge y\}}+K(r\vee|d|)\big({\bf 1}\_{\{\ln K<y\}}+{\bf 1}\_{\{\ln K<x\}}\big), |  |

where

|  |  |  |
| --- | --- | --- |
|  | A0ε:=δ+∫(ε,∞)ez​ν​(d​z),A1ε:=K​∫(0,ε)(ez−1)​ν​(d​z).\displaystyle A\_{0}^{\varepsilon}:=\delta+\int\_{(\varepsilon,\infty)}e^{z}\nu(dz),\quad A\_{1}^{\varepsilon}:=K\int\_{(0,\varepsilon)}\big(e^{z}-1\big)\nu(dz). |  |

Hence, we deduce that, for any t∈[0,θ]t\in[0,\theta],

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​(|h​(ln⁡b​(T)+a​θ+X~t)−h​(ln⁡b​(T)+a​θ+σ​Wt)|)\displaystyle\mathbb{E}\Big(\Big|h\big(\ln b(T)+a\sqrt{\theta}+\widetilde{X}\_{t}\big)-h\big(\ln b(T)+a\sqrt{\theta}+\sigma W\_{t}\big)\Big|\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤A0ε​b​(T)​ea​θ​𝔼​(|eX~t−eσ​Wt|)+2​A1ε​ℙ​(X~t∧(σ​Wt)>ln⁡K−ln⁡b​(T)−ε−a​θ)\displaystyle\quad\leq A\_{0}^{\varepsilon}\,b(T)e^{a\sqrt{\theta}}\mathbb{E}\Big(\big|e^{\widetilde{X}\_{t}}-e^{\sigma W\_{t}}\big|\Big)+2A\_{1}^{\varepsilon}\mathbb{P}\big(\widetilde{X}\_{t}\wedge(\sigma W\_{t})>\ln K-\ln b(T)-\varepsilon-a\sqrt{\theta}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +K​(r∨|d|)​(ℙ​(X~t>ln⁡K−ln⁡b​(T)−a​θ)+ℙ​(σ​Wt>ln⁡K−ln⁡b​(T)−a​θ))\displaystyle\qquad+K(r\vee|d|)\Big(\mathbb{P}\big(\widetilde{X}\_{t}>\ln K-\ln b(T)-a\sqrt{\theta}\big)+\mathbb{P}\big(\sigma W\_{t}>\ln K-\ln b(T)-a\sqrt{\theta}\big)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤A0ε​b​(T)​𝔼​(eσ​Wt)​𝔼​(|e(γ0−σ2/2)​t+Zt−1|)+(2​A1ε+K​(r∨|d|))​ℙ​(Wt>ln⁡K−ln⁡b​(T)−εσ)\displaystyle\quad\leq A\_{0}^{\varepsilon}\,b(T)\mathbb{E}\big(e^{\sigma W\_{t}}\big)\mathbb{E}\Big(\big|e^{(\gamma\_{0}-\sigma^{2}/2)t+Z\_{t}}-1\big|\Big)+\big(2A\_{1}^{\varepsilon}+K(r\vee|d|)\big)\mathbb{P}\bigg(W\_{t}>\frac{\ln K-\ln b(T)-\varepsilon}{\sigma}\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +K​(r∨|d|)​ℙ​(X~t>ln⁡K−ln⁡b​(T)).\displaystyle\qquad+K(r\vee|d|)\mathbb{P}\big(\widetilde{X}\_{t}>\ln K-\ln b(T)\big). |  | (5.8) |

As θ→0+\theta\rightarrow 0^{+}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​(eσ​Wt)​𝔼​(|e(γ0−σ2/2)​t+Zt−1|)≤eσ2​t/2​|e(γ0−σ2/2)​t−1|​𝔼​(eZt)+eσ2​t/2​𝔼​(|eZt−1|)=O​(θ),\displaystyle\mathbb{E}\big(e^{\sigma W\_{t}}\big)\mathbb{E}\Big(\big|e^{(\gamma\_{0}-\sigma^{2}/2)t+Z\_{t}}\!-\!1\big|\Big)\leq e^{\sigma^{2}t/2}\big|e^{(\gamma\_{0}-\sigma^{2}/2)t}\!-\!1\big|\mathbb{E}\big(e^{Z\_{t}}\big)+e^{\sigma^{2}t/2}\mathbb{E}\Big(\big|e^{Z\_{t}}\!-\!1\big|\Big)=O(\theta),\qquad |  | (5.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℙ​(supt∈[0,θ]Wt>ln⁡K−ln⁡b​(T)−εσ)≤e−(ln⁡K−ln⁡b​(T)−ε)2/(2​σ2​θ)=o​(θn),for any ​n∈ℕ,\displaystyle\mathbb{P}\bigg(\sup\_{t\in[0,\theta]}W\_{t}>\frac{\ln K-\ln b(T)-\varepsilon}{\sigma}\bigg)\leq e^{-(\ln K-\ln b(T)-\varepsilon)^{2}/(2\sigma^{2}\theta)}=o(\theta^{n}),\quad\text{for any }n\in\mathbb{N}, |  | (5.10) |

where we used Doob’s martingale inequality in the last inequality, and by ([5.1](https://arxiv.org/html/2512.17791v1#S5.E1 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.2](https://arxiv.org/html/2512.17791v1#A2.E2 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.3](https://arxiv.org/html/2512.17791v1#A2.E3 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(supt∈[0,θ]X~t>ln⁡(Kb​(T)))\displaystyle\mathbb{P}\bigg(\sup\_{t\in[0,\theta]}\!\widetilde{X}\_{t}\!>\!\ln\!\bigg(\frac{K}{b(T)}\bigg)\!\bigg) | ≤ℙ​(supt∈[0,θ]Wtε>A2​(θ)3​σ)+ℙ​(supt∈[0,θ]Ztε>A2​(θ)3)+ℙ​(supt∈[0,θ]Z¯tε>A2​(θ)3)\displaystyle\leq\mathbb{P}\bigg(\sup\_{t\in[0,\theta]}\!W\_{t}^{\varepsilon}\!>\!\frac{A\_{2}(\theta)}{3\sigma}\bigg)+\mathbb{P}\bigg(\sup\_{t\in[0,\theta]}\!Z\_{t}^{\varepsilon}\!>\!\frac{A\_{2}(\theta)}{3}\bigg)+\mathbb{P}\bigg(\sup\_{t\in[0,\theta]}\!\overline{Z}\_{t}^{\varepsilon}\!>\!\frac{A\_{2}(\theta)}{3}\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤e−A22​(θ)/(2​σ2​θ)+o​(θn)+ℙ​(T1ε≤θ)=O​(θ),\displaystyle\leq e^{-A\_{2}^{2}(\theta)/(2\sigma^{2}\theta)}+o(\theta^{n})+\mathbb{P}\big(T\_{1}^{\varepsilon}\leq\theta\big)=O(\theta), |  | (5.11) |

where we again used Doob’s martingale inequality as well as [[4](https://arxiv.org/html/2512.17791v1#bib.bib4), Remark 3.1] in the second inequality, and denoted by A2​(θ):=ln⁡K−ln⁡b​(T)−|γ0−σ2/2|​θA\_{2}(\theta):=\ln K-\ln b(T)-|\gamma\_{0}-\sigma^{2}/2|\theta. By combining ([5.7](https://arxiv.org/html/2512.17791v1#S5.E7 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([5.8](https://arxiv.org/html/2512.17791v1#S5.E8 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([5.9](https://arxiv.org/html/2512.17791v1#S5.E9 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([5.10](https://arxiv.org/html/2512.17791v1#S5.E10 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([5.11](https://arxiv.org/html/2512.17791v1#S5.E11 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐa​(τ)=𝔼​(∫0τh​(ln⁡b​(T)+a​θ+σ​Wt)​𝑑t)+o​(θ3/2),θ→0+.\displaystyle\mathcal{I}^{a}(\tau)=\mathbb{E}\left(\int\_{0}^{\tau}h\big(\ln b(T)+a\sqrt{\theta}+\sigma W\_{t}\big)\,dt\right)+o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}. |  | (5.12) |

Note that the function hh is convex on (−∞,ln⁡K)(-\infty,\ln K), and thus it is right- and left-differentiable. In particular, for x∈(−∞,ln⁡K)x\in(-\infty,\ln K), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | h+′​(x)=ex​(δ+∫[ln⁡K−x,∞)ez​ν​(d​z)),h−′​(x)=ex​(δ+∫(ln⁡K−x,∞)ez​ν​(d​z)).\displaystyle h^{\prime}\_{+}(x)=e^{x}\bigg(\delta+\int\_{[\ln K-x,\infty)}e^{z}\nu(dz)\bigg),\quad h^{\prime}\_{-}(x)=e^{x}\bigg(\delta+\int\_{(\ln K-x,\infty)}e^{z}\nu(dz)\bigg). |  | (5.13) |

Hence, with x0:=ln⁡b​(T)x\_{0}:=\ln b(T), we can write

|  |  |  |
| --- | --- | --- |
|  | h+′​(x0)​(x−x0)+−h−′​(x0)​(x−x0)−≤h​(x)−h​(x0)≤h−′​(x)​(x−x0)+−h+′​(x)​(x−x0)−,\displaystyle h^{\prime}\_{+}(x\_{0})(x-x\_{0})^{+}-h^{\prime}\_{-}(x\_{0})(x-x\_{0})^{-}\leq h(x)-h(x\_{0})\leq h^{\prime}\_{-}(x)(x-x\_{0})^{+}-h^{\prime}\_{+}(x)(x-x\_{0})^{-}, |  |

and thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≤h​(x)−h​(x0)−h+′​(x0)​(x−x0)++h−′​(x0)​(x−x0)−\displaystyle\leq h(x)-h(x\_{0})-h^{\prime}\_{+}(x\_{0})(x-x\_{0})^{+}+h^{\prime}\_{-}(x\_{0})(x-x\_{0})^{-} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(h−′​(x)−h+′​(x0))​(x−x0)++(h−′​(x0)−h+′​(x))​(x−x0)−=(h−′​(x∨x0)−h+′​(x∧x0))​|x−x0|.\displaystyle\leq\big(h^{\prime}\_{-}(x)\!-\!h^{\prime}\_{+}(x\_{0})\big)(x-x\_{0})^{+}+\big(h^{\prime}\_{-}(x\_{0})\!-\!h^{\prime}\_{+}(x)\big)(x-x\_{0})^{-}=\big(h^{\prime}\_{-}(x\vee x\_{0})\!-\!h^{\prime}\_{+}(x\wedge x\_{0})\big)|x-x\_{0}|. |  |

Noting that h​(x0)=h​(ln⁡b​(T))=0h(x\_{0})=h(\ln b(T))=0 in light of ([2.7](https://arxiv.org/html/2512.17791v1#S2.E7 "In item (b) ‣ Theorem 2.5. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x+x0)=h−′​(x0)​x+(h+′​(x0)−h−′​(x0))​x++|x|​R~​(x),x∈(−∞,ln⁡K−x0),\displaystyle h(x+x\_{0})=h^{\prime}\_{-}(x\_{0})x+\big(h^{\prime}\_{+}(x\_{0})-h^{\prime}\_{-}(x\_{0})\big)x^{+}+|x|\widetilde{R}(x),\quad x\in(-\infty,\ln K-x\_{0}), |  | (5.14) |

where R~​(x)≥0\widetilde{R}(x)\geq 0 and R~​(x)→0\widetilde{R}(x)\rightarrow 0 as x→0x\rightarrow 0. For x∈(−∞,0]x\in(-\infty,0], clearly

|  |  |  |  |
| --- | --- | --- | --- |
|  | R~(x)≤h−′(x0)−h+′(x+x0)≤h−′(x0)=:C−.\displaystyle\widetilde{R}(x)\leq h^{\prime}\_{-}(x\_{0})-h^{\prime}\_{+}(x+x\_{0})\leq h^{\prime}\_{-}(x\_{0})=:C\_{-}. |  | (5.15) |

For x∈(0,ln⁡K−x0)x\in(0,\ln K-x\_{0}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R~​(x)\displaystyle\widetilde{R}(x) | =1x​h​(x+x0)−h+′​(x0)=1x​(h​(x+x0)−h​(x0))−h+′​(x0)\displaystyle=\frac{1}{x}h(x+x\_{0})-h^{\prime}\_{+}(x\_{0})=\frac{1}{x}\big(h(x+x\_{0})-h(x\_{0})\big)-h^{\prime}\_{+}(x\_{0}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =δx​ex0​(ex−1)+1x​∫ℝ0((ex+x0+z−K)+−(ex0+z−K)+)​ν​(d​z)−h+′​(x0)\displaystyle=\frac{\delta}{x}e^{x\_{0}}\big(e^{x}-1\big)+\frac{1}{x}\int\_{\mathbb{R}\_{0}}\Big(\big(e^{x+x\_{0}+z}-K\big)^{+}-\big(e^{x\_{0}+z}-K\big)^{+}\Big)\nu(dz)-h^{\prime}\_{+}(x\_{0}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤δ​ex0+x+1x​((ex+x0−ex0)​∫(ln⁡K−x0,∞)ez​ν​(d​z)+∫(ln⁡K−x0−x,ln⁡K−x0)(ex0+x+z−K)​ν​(d​z))\displaystyle\leq\delta e^{x\_{0}+x}+\frac{1}{x}\bigg(\big(e^{x+x\_{0}}-e^{x\_{0}}\big)\int\_{(\ln K-x\_{0},\infty)}e^{z}\,\nu(dz)+\int\_{(\ln K-x\_{0}-x,\ln K-x\_{0})}\big(e^{x\_{0}+x+z}-K\big)\nu(dz)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤δ​ex0+x+ex0+x​∫(ln⁡K−x0,∞)ez​ν​(d​z)+Kx​∫(ln⁡K−x0−x,ln⁡K−x0)(ez−1)​ν​(d​z)\displaystyle\leq\delta e^{x\_{0}+x}+e^{x\_{0}+x}\int\_{(\ln K-x\_{0},\infty)}e^{z}\,\nu(dz)+\frac{K}{x}\int\_{(\ln K-x\_{0}-x,\ln K-x\_{0})}\big(e^{z}-1\big)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​δ+K​∫(ln⁡K−x0,∞)ez​ν​(d​z)+Kx​∫(ln⁡K−x0−x,ln⁡K−x0)(ez−1)​ν​(d​z).\displaystyle\leq K\delta+K\int\_{(\ln K-x\_{0},\infty)}e^{z}\,\nu(dz)+\frac{K}{x}\int\_{(\ln K-x\_{0}-x,\ln K-x\_{0})}\big(e^{z}-1\big)\nu(dz). |  |

By Assumption [5.1](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") and the Fundamental theorem of calculus,

|  |  |  |
| --- | --- | --- |
|  | limx→0+1x​∫(ln⁡K−x0−x,ln⁡K−x0)(ez−1)​s​(z)​𝑑z=(Kb​(T)−1)​s​(ln⁡K−x0).\displaystyle\lim\_{x\rightarrow 0+}\frac{1}{x}\int\_{(\ln K-x\_{0}-x,\ln K-x\_{0})}\big(e^{z}-1\big)s(z)\,dz=\bigg(\frac{K}{b(T)}-1\bigg)s\big(\ln K-x\_{0}\big). |  |

Hence, there exists η0∈(0,ln⁡K−x0)\eta\_{0}\in(0,\ln K-x\_{0}), such that for any x∈(0,η0)x\in(0,\eta\_{0}),

|  |  |  |
| --- | --- | --- |
|  | 1x​∫(ln⁡K−x0−x,ln⁡K−x0)(ez−1)​s​(z)​𝑑z≤2​(Kb​(T)−1)​s​(ln⁡K−x0).\displaystyle\frac{1}{x}\int\_{(\ln K-x\_{0}-x,\ln K-x\_{0})}\big(e^{z}-1\big)s(z)\,dz\leq 2\bigg(\frac{K}{b(T)}-1\bigg)s\big(\ln K-x\_{0}\big). |  |

Consequently, for any x∈(0,ln⁡K−x0)x\in(0,\ln K-x\_{0}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R~(x)≤K(δ+∫ln⁡K−x0∞ezs(z)dz+1η0∫0ln⁡K−x0(ez−1)s(z)dz)+2(Kb​(T)−1)s(lnK−x0)=:C+.\displaystyle\widetilde{R}(x)\!\leq\!K\bigg(\!\delta\!+\!\!\int\_{\ln K-x\_{0}}^{\infty}\!\!e^{z}s(z)\,dz\!+\!\frac{1}{\eta\_{0}}\!\int\_{0}^{\ln K-x\_{0}}\!\!\big(e^{z}\!-\!1\big)s(z)\,dz\!\bigg)\!+\!2\bigg(\!\frac{K}{b(T)}\!-\!1\!\bigg)s(\ln K\!-\!x\_{0})\!=:\!C\_{+}.\qquad |  | (5.16) |

By combining ([5.15](https://arxiv.org/html/2512.17791v1#S5.E15 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([5.16](https://arxiv.org/html/2512.17791v1#S5.E16 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | R~​(x)≤C−+C+<∞,for all ​x∈(−∞,ln⁡K−x0).\displaystyle\widetilde{R}(x)\leq C\_{-}+C\_{+}<\infty,\quad\text{for all }\,x\in(-\infty,\ln K-x\_{0}). |  | (5.17) |

Coming back to the estimation of Ia​(τ)I^{a}(\tau), we deduce from ([5.14](https://arxiv.org/html/2512.17791v1#S5.E14 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​(∫0τh​(x0+a​θ+σ​Wt)​𝑑t)=𝔼​(∫0τh​(x0+a​θ+σ​Wt)​𝟏{x0+a​θ+σ​Wt<ln⁡K}​𝑑t)\displaystyle\mathbb{E}\bigg(\int\_{0}^{\tau}h\big(x\_{0}+a\sqrt{\theta}+\sigma W\_{t}\big)\,dt\bigg)=\mathbb{E}\bigg(\int\_{0}^{\tau}h\big(x\_{0}+a\sqrt{\theta}+\sigma W\_{t}\big){\bf 1}\_{\{x\_{0}+a\sqrt{\theta}+\sigma W\_{t}<\ln K\}}\,dt\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(∫0τ(h−′​(x0)​(a​θ+σ​Wt)+(h+′​(x0)−h−′​(x0))​(a​θ+σ​Wt)+)​𝟏{x0+a​θ+σ​Wt<ln⁡K}​𝑑t)\displaystyle\quad=\mathbb{E}\bigg(\int\_{0}^{\tau}\Big(h^{\prime}\_{-}(x\_{0})\big(a\sqrt{\theta}+\sigma W\_{t}\big)+\big(h^{\prime}\_{+}(x\_{0})-h^{\prime}\_{-}(x\_{0})\big)\big(a\sqrt{\theta}+\sigma W\_{t}\big)^{+}\Big){\bf 1}\_{\{x\_{0}+a\sqrt{\theta}+\sigma W\_{t}<\ln K\}}\,dt\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼​(∫0τ|a​θ+σ​Wt|​R~​(a​θ+σ​Wt)​𝟏{x0+a​θ+σ​Wt<ln⁡K}​𝑑t),\displaystyle\qquad+\mathbb{E}\bigg(\int\_{0}^{\tau}\big|a\sqrt{\theta}+\sigma W\_{t}\big|\widetilde{R}\big(a\sqrt{\theta}+\sigma W\_{t}\big){\bf 1}\_{\{x\_{0}+a\sqrt{\theta}+\sigma W\_{t}<\ln K\}}\,dt\bigg), |  | (5.18) |

where the first equality follows from the fact that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≤𝔼​(∫0τh​(x0+a​θ+σ​Wt)​𝟏{x0+a​θ+σ​Wt=ln⁡K}​𝑑t)\displaystyle\leq\mathbb{E}\bigg(\int\_{0}^{\tau}h\big(x\_{0}+a\sqrt{\theta}+\sigma W\_{t}\big){\bf 1}\_{\{x\_{0}+a\sqrt{\theta}+\sigma W\_{t}=\ln K\}}dt\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−d​K​ℙ​(Leb​{t∈[0,θ]:σ​Wt=ln⁡K−x0−a​θ})=0,\displaystyle\leq-dK\,\mathbb{P}\big(\,\text{Leb}\big\{t\in[0,\theta]:\,\sigma W\_{t}=\ln K-x\_{0}-a\sqrt{\theta}\big\}\big)=0, |  |

since h​(ln⁡K)=−d​K≥0h(\ln K)=-dK\geq 0 in light of ([1.3](https://arxiv.org/html/2512.17791v1#S1.E3 "In 1. Introduction ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). For the first term in ([5.18](https://arxiv.org/html/2512.17791v1#S5.E18 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |𝔼​(∫0τ((h+′​(x0)−h−′​(x0))​(a​θ+σ​Wt)++h−′​(x0)​(a​θ+σ​Wt))​𝟏{x0+a​θ+σ​Wt≥ln⁡K}​𝑑t)|\displaystyle\left|\mathbb{E}\bigg(\int\_{0}^{\tau}\Big(\big(h^{\prime}\_{+}(x\_{0})-h^{\prime}\_{-}(x\_{0})\big)\big(a\sqrt{\theta}+\sigma W\_{t}\big)^{+}+h^{\prime}\_{-}(x\_{0})\big(a\sqrt{\theta}+\sigma W\_{t}\big)\Big){\bf 1}\_{\{x\_{0}+a\sqrt{\theta}+\sigma W\_{t}\geq\ln K\}}\,dt\bigg)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h+′​(x0)​θ​𝔼​(∫0θ(|a|+tθ​|σ​W1|)​𝟏{|σ​W1|≥−a+(ln⁡K−x0)/θ}​𝑑t)\displaystyle\quad\leq h^{\prime}\_{+}(x\_{0})\sqrt{\theta}\,\mathbb{E}\left(\int\_{0}^{\theta}\bigg(|a|+\sqrt{\frac{t}{\theta}}\big|\sigma W\_{1}\big|\bigg){\bf 1}\_{\{|\sigma W\_{1}|\geq-a+(\ln K-x\_{0})/\sqrt{\theta}\}}\,dt\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤h+′​(x0)​θ3/2​𝔼​((|a|+|W1|)2)​ℙ​(σ​|W1|≥ln⁡K−x0θ)=o​(θn),θ→0+,\displaystyle\quad\leq h^{\prime}\_{+}(x\_{0})\,\theta^{3/2}\sqrt{\mathbb{E}\Big(\big(|a|+|W\_{1}|\big)^{2}\Big)}\sqrt{\mathbb{P}\bigg(\sigma|W\_{1}|\geq\frac{\ln K-x\_{0}}{\sqrt{\theta}}\bigg)}=o(\theta^{n}),\quad\theta\rightarrow 0^{+}, |  | (5.19) |

for any n∈ℕn\in\mathbb{N}. As for the second term in ([5.18](https://arxiv.org/html/2512.17791v1#S5.E18 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), by ([5.17](https://arxiv.org/html/2512.17791v1#S5.E17 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and bounded convergence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​(∫0τ|a​θ+σ​Wt|​R~​(a​θ+σ​Wt)​𝟏{x0+a​θ+σ​Wt<ln⁡K}​𝑑t)\displaystyle\mathbb{E}\bigg(\int\_{0}^{\tau}\big|a\sqrt{\theta}+\sigma W\_{t}\big|\widetilde{R}\big(a\sqrt{\theta}+\sigma W\_{t}\big){\bf 1}\_{\{x\_{0}+a\sqrt{\theta}+\sigma W\_{t}<\ln K\}}\,dt\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤θ3/2​𝔼​(∫01|a+σ​Ws|​R~​(θ​(a+σ​Ws))​𝟏{x0+θ​(a+σ​Ws)<ln⁡K}​𝑑s)=o​(θ3/2),θ→0+.\displaystyle\leq\theta^{3/2}\,\mathbb{E}\bigg(\int\_{0}^{1}\big|a+\sigma W\_{s}\big|\widetilde{R}\big(\sqrt{\theta}(a+\sigma W\_{s})\big){\bf 1}\_{\{x\_{0}+\sqrt{\theta}(a+\sigma W\_{s})<\ln K\}}\,ds\bigg)=o(\theta^{3/2}),\quad\theta\rightarrow 0^{+}.\qquad |  | (5.20) |

By combining ([5.12](https://arxiv.org/html/2512.17791v1#S5.E12 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([5.13](https://arxiv.org/html/2512.17791v1#S5.E13 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([5.18](https://arxiv.org/html/2512.17791v1#S5.E18 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([5.19](https://arxiv.org/html/2512.17791v1#S5.E19 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([5.20](https://arxiv.org/html/2512.17791v1#S5.E20 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐa​(τ)\displaystyle\mathcal{I}^{{\color[rgb]{1,0,0}a}}(\tau) | =𝔼​(∫0τ(h−′​(x0)​(a​θ+σ​Wt)+(h+′​(x0)−h−′​(x0))​(a​θ+σ​Wt)+)​𝑑t)+o​(θ3/2)\displaystyle=\mathbb{E}\bigg(\int\_{0}^{\tau}\Big(h^{\prime}\_{-}(x\_{0})\big(a\sqrt{\theta}+\sigma W\_{t}\big)+\big(h^{\prime}\_{+}(x\_{0})-h^{\prime}\_{-}(x\_{0})\big)\big(a\sqrt{\theta}+\sigma W\_{t}\big)^{+}\Big)\,dt\bigg)+o(\theta^{3/2}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =b​(T)​δ¯​𝔼​(∫0τ((a​θ+σ​Wt)+λ​β​(a​θ+σ​Wt)+)​𝑑t)+o​(θ3/2),θ→0+,\displaystyle=b(T)\overline{\delta}\,\mathbb{E}\bigg(\int\_{0}^{\tau}\Big(\big(a\sqrt{\theta}+\sigma W\_{t}\big)+\lambda\beta\big(a\sqrt{\theta}+\sigma W\_{t}\big)^{+}\Big)dt\bigg)+o(\theta^{3/2}),\quad\theta\rightarrow 0^{+}, |  | (5.21) |

where δ¯=δ+∫(ln⁡(K/b​(T)),∞)ez​ν​(d​z)\bar{\delta}=\delta+\int\_{(\ln(K/b(T)),\infty)}e^{z}\nu(dz), λ=ν​({ln⁡(K/b​(T))})\lambda=\nu(\{\ln(K/b(T))\}), and β=K/(b​(T)​δ¯)\beta=K/(b(T)\overline{\delta}).

Coming back to ([5.4](https://arxiv.org/html/2512.17791v1#S5.E4 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and using ([5.6](https://arxiv.org/html/2512.17791v1#S5.E6 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([5.21](https://arxiv.org/html/2512.17791v1#S5.E21 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(e−r​τ​(K−Sτ)+)\displaystyle\mathbb{E}\big(e^{-r\tau}(K\!-\!S\_{\tau})^{+}\big) | =(K−b​(T)​ea​θ)++b​(T)​δ¯​𝔼​(∫0τ((a​θ+σ​Wt)+λ​β​(a​θ+σ​Wt)+)​𝑑t)\displaystyle=\big(K-b(T)e^{a\sqrt{\theta}}\big)^{+}+b(T)\overline{\delta}\,\mathbb{E}\bigg(\int\_{0}^{\tau}\Big(\big(a\sqrt{\theta}+\sigma W\_{t}\big)+\lambda\beta\big(a\sqrt{\theta}+\sigma W\_{t}\big)^{+}\Big)dt\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +K​𝔼​(𝟏{T^1<τ}​((−a​θ−σ​Wτ)+−(−a​θ−σ​WT^1)+))+o​(θ3/2)\displaystyle\quad+K\,\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\Big(\big(\!-\!a\sqrt{\theta}\!-\!\sigma W\_{\tau}\big)^{+}-\big(\!-\!a\sqrt{\theta}\!-\!\sigma W\_{\widehat{T}\_{1}}\big)^{+}\Big)\Big)+o\big(\theta^{3/2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(K−b​(T)​ea​θ)++b​(T)​δ¯​𝔼​(∫0τ((a​θ+σ​Wt)+λ​β​(a​θ+σ​Wt)+)​𝑑t)\displaystyle=\big(K-b(T)e^{a\sqrt{\theta}}\big)^{+}+b(T)\overline{\delta}\,\mathbb{E}\bigg(\int\_{0}^{\tau}\Big(\big(a\sqrt{\theta}+\sigma W\_{t}\big)+\lambda\beta\big(a\sqrt{\theta}+\sigma W\_{t}\big)^{+}\Big)dt\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +K​𝔼​(𝟏{T^1<τ}​((a​θ+σ​Wτ)+−(a​θ+σ​WT^1)+))+o​(θ3/2),θ→0+,\displaystyle\quad+K\,\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\Big(\big(a\sqrt{\theta}+\sigma W\_{\tau}\big)^{+}-\big(a\sqrt{\theta}+\sigma W\_{\widehat{T}\_{1}}\big)^{+}\Big)\Big)+o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}, |  |

with the o​(θ3/2)o(\theta^{3/2}) term independent of τ\tau, where the last equality follows from the Tanaka’s formula. Therefore, we obtain that

|  |  |  |
| --- | --- | --- |
|  | P​(T−θ,b​(T)​ea​θ)=(K−b​(T)​ea​θ)++σ​b​(T)​δ¯​v¯λ,β,θ​(a/σ)+o​(θ3/2),θ→0+,\displaystyle P\big(T-\theta,b(T)e^{a\sqrt{\theta}}\big)=\big(K-b(T)e^{a\sqrt{\theta}}\big)^{+}+\sigma b(T)\overline{\delta}\,\bar{v}\_{\lambda,\beta,\theta}(a/\sigma)+o(\theta^{3/2}),\quad\theta\rightarrow 0^{+}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | v¯λ,β,θ​(y):=supτ∈𝒯0,θ𝔼​(∫0τfλ​β​(y​θ+Wt)​𝑑t+β​ 1{T^1<τ}​((y​θ+Wτ)+−(y​θ+WT^1)+)),\displaystyle\bar{v}\_{\lambda,\beta,\theta}(y):=\sup\_{\tau\in\mathscr{T}\_{0,\theta}}\mathbb{E}\bigg(\int\_{0}^{\tau}f\_{\lambda\beta}\big(y\sqrt{\theta}+W\_{t}\big)\,dt+\beta\,{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\Big(\big(y\sqrt{\theta}+W\_{\tau}\big)^{+}-\big(y\sqrt{\theta}+W\_{\widehat{T}\_{1}}\big)^{+}\Big)\bigg), |  |

with fc​(x)=x+c​x+f\_{c}(x)=x+cx^{+}, because v¯λ,β,θ​(y)=v¯λ,β​(y)​θ3/2+o​(θ3/2)\bar{v}\_{\lambda,\beta,\theta}(y)=\bar{v}\_{\lambda,\beta}(y)\theta^{3/2}+o(\theta^{3/2}) as shown at the end of the proof of Theorem 3.1 in [[2](https://arxiv.org/html/2512.17791v1#bib.bib2)]. □\Box

Thanks to Theorem [5.3](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem3 "Theorem 5.3. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), we are now ready to present our main result in this section. The proof is similar to that of [[2](https://arxiv.org/html/2512.17791v1#bib.bib2), Theorem 3.2], and is presented below for completeness.

###### Theorem 5.4.

Suppose that ([3.2](https://arxiv.org/html/2512.17791v1#S3.E2 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and Assumption [5.1](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") hold. Assume that σ>0\sigma>0 and d<0d<0, and let yλ,βy\_{\lambda,\beta}, λ,β∈ℝ+\lambda,\beta\in\mathbb{R}\_{+}, be given as in Theorem [3.1](https://arxiv.org/html/2512.17791v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1. Finite Jump Activity Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")-(c).

* (a)

  If ν​({ln⁡(K/b​(T))})=0\nu(\{\ln(K/b(T))\})=0, then we have

  |  |  |  |
  | --- | --- | --- |
  |  | limt→T−b​(T)−b​(t)σ​b​(T)​T−t=y0,0.\displaystyle\lim\_{t\rightarrow T^{-}}\frac{b(T)-b(t)}{\sigma b(T)\sqrt{T-t}}=y\_{0,0}. |  |
* (b)

  If ν​({ln⁡(K/b​(T))})>0\nu(\{\ln(K/b(T))\})>0, then we have

  |  |  |  |
  | --- | --- | --- |
  |  | limt→T−b​(T)−b​(t)σ​b​(T)​T−t=yλ,β,\displaystyle\lim\_{t\rightarrow T^{-}}\frac{b(T)-b(t)}{\sigma b(T)\sqrt{T-t}}=y\_{\lambda,\beta}, |  |

  where λ=ν​({ln⁡(K/b​(T))})\lambda=\nu(\{\ln(K/b(T))\}), β=K/(b​(T)​δ¯)\beta=K/(b(T)\bar{\delta}), and δ¯=δ+∫(ln⁡(K/b​(T)),∞)ez​ν​(d​z)\bar{\delta}=\delta+\int\_{(\ln(K/b(T)),\infty)}e^{z}\nu(dz).

The proof of Theorem [5.4](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem4 "Theorem 5.4. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") requires the following technical lemma, the proof of which is deferred to Appendix [B](https://arxiv.org/html/2512.17791v1#A2 "Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"). Note that this lemma was proved in [[2](https://arxiv.org/html/2512.17791v1#bib.bib2)] (see Lemmas 2.2 therein) when ν​(ℝ0)<∞\nu(\mathbb{R}\_{0})<\infty. Here we extend it to the case when the jump component of XX is of finite variation (i.e., ([3.2](https://arxiv.org/html/2512.17791v1#S3.E2 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) holds).

###### Lemma 5.5.

Under the model assumptions, for any s∈(b​(t),b​(T))s\in(b(t),b(T)), we have

|  |  |  |
| --- | --- | --- |
|  | ∫b​(t)s(u−b​(t))​∂2P∂s2​(t,d​u)≥h​(s,T−t)σ2​b2​(T)​(s−b​(t))2,t→T−,\displaystyle\int\_{b(t)}^{s}(u-b(t))\frac{\partial^{2}P}{\partial s^{2}}(t,du)\geq\frac{h(s,T-t)}{\sigma^{2}b^{2}(T)}(s-b(t))^{2},\quad t\rightarrow T^{-}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | h​(s,θ):=(δ¯−ε​(θ))​(b​(T)−s)−b​(T)​δ¯​λ​β​𝔼​((σ​Wθ−ln⁡(b​(T)/s))+)+o​(θ),θ→0+,\displaystyle h(s,\theta):=\big(\bar{\delta}-\varepsilon(\theta)\big)(b(T)-s)-b(T)\bar{\delta}\lambda\beta\,\mathbb{E}\Big(\big(\sigma W\_{\theta}-\ln(b(T)/s)\big)^{+}\Big)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}, |  |

with limθ→0+ε​(θ)=0\lim\_{\theta\rightarrow 0^{+}}\varepsilon(\theta)=0, and λ\lambda, β\beta, and δ¯\bar{\delta} are given as in Theorem [5.4](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem4 "Theorem 5.4. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")-(b).

Proof of Theorem [5.4](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem4 "Theorem 5.4. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"). We first note that by ([3.1](https://arxiv.org/html/2512.17791v1#S3.E1 "In item (c) ‣ Theorem 3.1. ‣ 3.1. Finite Jump Activity Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), when λ=ν​({ln⁡(K/b​(T))})=0\lambda=\nu(\{\ln(K/b(T))\})=0, the function v0,βv\_{0,\beta} is independent of the value of β∈ℝ+\beta\in\mathbb{R}\_{+}, i.e., v0,0=v0,βv\_{0,0}=v\_{0,\beta} for any β∈ℝ+\beta\in\mathbb{R}\_{+}. Therefore, we can proceed the proof for parts (a) and (b) together by considering any λ,β∈ℝ+\lambda,\beta\in\mathbb{R}\_{+}.

By [[2](https://arxiv.org/html/2512.17791v1#bib.bib2), Lemma 3.1], we have yλ,β>0y\_{\lambda,\beta}>0. Also, from the definition of vλ,βv\_{\lambda,\beta}, we have vλ,β​(a/σ)>0v\_{\lambda,\beta}(a/\sigma)>0 for all a>−σ​yλ,βa>-\sigma y\_{\lambda,\beta}. Hence, by Theorem [5.3](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem3 "Theorem 5.3. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") we have that, for any a∈(−σ​yλ,β,0)a\in(-\sigma y\_{\lambda,\beta},0),

|  |  |  |
| --- | --- | --- |
|  | P​(T−θ,b​(T)​ea​θ)>(K−b​(T)​ea​θ)+,for ​θ>0​small enough.\displaystyle P\big(T-\theta,b(T)e^{a\sqrt{\theta}}\big)>\big(K-b(T)e^{a\sqrt{\theta}}\big)^{+},\quad\text{for }\,\theta>0\,\,\,\text{small enough}. |  |

Taking t=T−θt=T-\theta, it follow from the definition of the critical price that

|  |  |  |
| --- | --- | --- |
|  | ln⁡b​(T)+a​T−t>ln⁡b​(t).\displaystyle\ln b(T)+a\sqrt{T-t}>\ln b(t). |  |

Using the nondecreasing property of bb on [0,T][0,T] and the inequality ln⁡(1+z)≤z\ln(1+z)\leq z, z>−1z>-1, we have

|  |  |  |
| --- | --- | --- |
|  | b​(T)−b​(t)b​(t)​T−t≥1σ​(ln⁡b​(T)−ln⁡b​(t))T−t>−a.\displaystyle\frac{b(T)-b(t)}{b(t)\sqrt{T-t}}\geq\frac{1}{\sigma}\frac{\big(\ln b(T)-\ln b(t)\big)}{\sqrt{T-t}}>-a. |  |

By taking first t→T−t\rightarrow T^{-} and then a→(−σ​yλ,β)+a\rightarrow(-\sigma y\_{\lambda,\beta})^{+}, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim inft→T−b​(T)−b​(t)b​(T)​T−t≥σ​yλ,β.\displaystyle\liminf\_{t\rightarrow T^{-}}\frac{b(T)-b(t)}{b(T)\sqrt{T-t}}\geq\sigma y\_{\lambda,\beta}. |  | (5.22) |

On the other hand, for any a≤−σ​yλ,β<0a\leq-\sigma y\_{\lambda,\beta}<0, vλ,β​(a/σ)=0v\_{\lambda,\beta}(a/\sigma)=0 and consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(θ):=P​(T−θ,b​(T)​ea​θ)−(K−b​(T)​ea​θ)+=o​(θ3/2),θ→0+.\displaystyle g(\theta):=P\big(T-\theta,b(T)e^{a\sqrt{\theta}}\big)-\big(K-b(T)e^{a\sqrt{\theta}}\big)^{+}=o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}. |  | (5.23) |

In addition, for any t∈[0,T)t\in[0,T) and s∈(b​(t),b​(T))s\in(b(t),b(T)), we have

|  |  |  |
| --- | --- | --- |
|  | P​(t,s)−P​(t,b​(t))−(s−b​(t))​∂P∂s​(t,b​(t))=∫b​(t)s(u−b​(t))​∂2P∂s2​(t,d​u),\displaystyle P(t,s)-P(t,b(t))-(s-b(t))\frac{\partial P}{\partial s}(t,b(t))=\int\_{b(t)}^{s}(u-b(t))\frac{\partial^{2}P}{\partial s^{2}}(t,du), |  |

in the distributional sense (note that (∂2P/∂s2)​(t,d​u)(\partial^{2}P/\partial s^{2})(t,du) is a positive measure on (0,∞)(0,\infty)). Due to the smooth-fit property (cf. [[6](https://arxiv.org/html/2512.17791v1#bib.bib6), Proposition 4.1 & Theorem 4.1]) and Lemma [5.5](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem5 "Lemma 5.5. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), we deduce that

|  |  |  |
| --- | --- | --- |
|  | P​(t,s)−(K−s)=∫b​(t)s(u−b​(t))​∂2P∂s2​(t,d​u)≥h​(s,T−t)σ2​b2​(T)​(s−b​(t))2,for small ​θ=T−t>0.\displaystyle P(t,s)-(K-s)=\int\_{b(t)}^{s}(u-b(t))\frac{\partial^{2}P}{\partial s^{2}}(t,du)\geq\frac{h(s,T-t)}{\sigma^{2}b^{2}(T)}(s-b(t))^{2},\quad\text{for small }\,\theta=T-t>0. |  |

For any t∈[0,T]t\in[0,T] with θ=T−t\theta=T-t small enough, by ([5.22](https://arxiv.org/html/2512.17791v1#S5.E22 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) we can pick a=a​(t)<−σ​yλ,βa=a(t)<-\sigma y\_{\lambda,\beta} big enough so that s=s​(t):=b​(T)​ea​θ∈(b​(t),b​(T))s=s(t):=b(T)e^{a\sqrt{\theta}}\in(b(t),b(T)) and that a​(t)↑−σ​yλ,βa(t)\uparrow-\sigma y\_{\lambda,\beta} as θ→0+\theta\rightarrow 0^{+}. It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(s,θ)\displaystyle h(s,\theta) | =b​(T)​(δ¯−ε​(θ))​(1−ea​θ)−b​(T)​δ¯​λ​β​𝔼​((σ​Wθ+a​θ)+)+o​(θ)\displaystyle=b(T)\big(\bar{\delta}-\varepsilon(\theta)\big)\big(1-e^{a\sqrt{\theta}}\big)-b(T)\bar{\delta}\lambda\beta\,\mathbb{E}\Big(\big(\sigma W\_{\theta}+a\sqrt{\theta}\big)^{+}\Big)+o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥b​(T)​(δ¯−ε​(θ))​(−a​θ−a2​θ2)−b​(T)​δ¯​λ​β​σ​θ​𝔼​((W1+a​σ−1)+)+o​(θ)\displaystyle\geq b(T)\big(\bar{\delta}-\varepsilon(\theta)\big)\bigg(-a\sqrt{\theta}-\frac{a^{2}\theta}{2}\bigg)-b(T)\bar{\delta}\lambda\beta\sigma\sqrt{\theta}\,\mathbb{E}\big((W\_{1}+a\sigma^{-1})^{+}\big)+o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =b​(T)​δ¯​σ​θ​(−aσ−λ​β​𝔼​((W1+a​σ−1)+))+o​(θ),θ→0+.\displaystyle=b(T)\bar{\delta}\sigma\sqrt{\theta}\bigg(-\frac{a}{\sigma}-\lambda\beta\,\mathbb{E}\big((W\_{1}+a\sigma^{-1})^{+}\big)\bigg)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}. |  |

Letting C​(z):=z−λ​β​𝔼​[(W1−z)+]C(z):=z-\lambda\beta\,\mathbb{E}[(W\_{1}-z)^{+}], z∈ℝz\in\mathbb{R}, we have

|  |  |  |
| --- | --- | --- |
|  | P​(t,b​(T)​ea​θ)−(K−b​(T)​ea​θ)≥(b​(T)​ea​θ−b​(t))2​(δ¯​θ​C​(−a​σ−1)σ​b​(T)+o​(θ)),θ→0+.\displaystyle P\big(t,b(T)e^{a\sqrt{\theta}}\big)-\big(K-b(T)e^{a\sqrt{\theta}}\big)\geq\big(b(T)e^{a\sqrt{\theta}}-b(t)\big)^{2}\left(\frac{\bar{\delta}\sqrt{\theta}\,C(-a\sigma^{-1})}{\sigma b(T)}+o(\sqrt{\theta})\right),\quad\theta\rightarrow 0^{+}. |  |

By [[2](https://arxiv.org/html/2512.17791v1#bib.bib2), Lemma 3.2], C​(z)>0C(z)>0 for all z>yλ,βz>y\_{\lambda,\beta}. Together with ([5.23](https://arxiv.org/html/2512.17791v1#S5.E23 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that,

|  |  |  |
| --- | --- | --- |
|  | (b​(T)​ea​θ−b​(t))2≤2​b​(T)​σ​g​(θ)δ¯​θ​C​(−a​σ−1)=o​(θ),\displaystyle\big(b(T)e^{a\sqrt{\theta}}-b(t)\big)^{2}\leq\frac{2b(T)\sigma g(\theta)}{\bar{\delta}\sqrt{\theta}C(-a\sigma^{-1})}=o(\theta), |  |

for θ>0\theta>0 small enough, which implies that

|  |  |  |
| --- | --- | --- |
|  | b​(T)−b​(t)b​(T)​θ≤−a+o​(1).\displaystyle\frac{b(T)-b(t)}{b(T)\sqrt{\theta}}\leq-a+o(1). |  |

Finally, by taking t→T−t\rightarrow T^{-}, we obtain that

|  |  |  |
| --- | --- | --- |
|  | lim supt→T−b​(T)−b​(t)b​(T)​T−t≤σ​yλ,β,\displaystyle\limsup\_{t\rightarrow T^{-}}\frac{b(T)-b(t)}{b(T)\sqrt{T-t}}\leq\sigma y\_{\lambda,\beta}, |  |

which completes the proof of the theorem. □\Box

## 6. Conclusions

The present work study the convergence rate of the critical price of an American put option near-maturity under an exponential Lévy model with a nonzero Brownian component. We focus on two important scenarios which were not investigated in the literature. Namely, we consider the models with negative jumps of infinite variation when the critical price converges to the strike price and the models with infinite activity jumps when the critical price tends to a value strictly lower than the strike price. In both scenarios, the convergence rate is shown to be of order O​(T−t)O(\sqrt{T-t}) with explicit constants proportionality. As a by product, we obtain a second-order near-maturity expansion of the American put price around the critical price.

## Appendix A Proofs of Lemmas in Section [4](https://arxiv.org/html/2512.17791v1#S4 "4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

### Proof of Lemma [4.2](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

Clearly, we have

|  |  |  |
| --- | --- | --- |
|  | 1t​(XtW−t​∫ℝ0(ez−1)+​ν​(d​z)−t​∫−∞0−(ez−1−z)​ν​(d​z))⟶𝔇σ​W1,as ​t→0+.\displaystyle\frac{1}{\sqrt{t}}\bigg(X\_{t}^{W}-t\int\_{\mathbb{R}\_{0}}\big(e^{z}-1\big)^{+}\nu(dz)-t\int\_{-\infty}^{0-}\big(e^{z}-1-z\big)\,\nu(dz)\bigg)\;{\stackrel{{\scriptstyle\mathfrak{D}}}{{\longrightarrow}}}\;\sigma W\_{1},\quad\text{as }\,t\rightarrow 0^{+}. |  |

Since J+J^{+} is a Lévy process of type B (cf. [[14](https://arxiv.org/html/2512.17791v1#bib.bib14), Definition 11.9]), by [[14](https://arxiv.org/html/2512.17791v1#bib.bib14), Theorem 43.20] we also have

|  |  |  |
| --- | --- | --- |
|  | limt→0+Jt+t→0ℙ−a.​s.\displaystyle\lim\_{t\rightarrow 0^{+}}\frac{J\_{t}^{+}}{\sqrt{t}}\rightarrow 0\quad\mathbb{P}-\text{a.}\,\text{s.} |  |

In view of ([4.1](https://arxiv.org/html/2512.17791v1#S4.E1 "In 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), it remains to analyze the behavior of the stochastic integral in J−J^{-}. For any η∈(0,∞)\eta\in(0,\infty), we define

|  |  |  |
| --- | --- | --- |
|  | Jt−η:=∫0t∫[−η,0)z​N~​(d​s,d​z),J¯t−η:=∫0t∫(−∞,−η)z​N​(d​s,d​z),t∈ℝ+,\displaystyle J\_{t}^{-\eta}:=\int\_{0}^{t}\int\_{[-\eta,0)}z\,\widetilde{N}(ds,dz),\quad\overline{J}\_{t}^{-\eta}:=\int\_{0}^{t}\int\_{(-\infty,-\eta)}z\,N(ds,dz),\quad t\in\mathbb{R}\_{+}, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | Jt−=Jt−η+J¯t−η−t​∫−∞0(ez−1−z​𝟏[−η,0)​(z))​ν​(d​z).\displaystyle J\_{t}^{-}=J\_{t}^{-\eta}+\overline{J}\_{t}^{-\eta}-t\int\_{-\infty}^{0}\big(e^{z}-1-z{\bf 1}\_{[-\eta,0)}(z)\big)\,\nu(dz). |  |

Clearly the last integral above is of order o​(t)o(\sqrt{t}) as t→0+t\rightarrow 0^{+}. We now show that

|  |  |  |
| --- | --- | --- |
|  | Jt−η+J¯t−η=oℙ​(t),as ​t→0+.\displaystyle J\_{t}^{-\eta}+\overline{J}\_{t}^{-\eta}=o\_{\mathbb{P}}(\sqrt{t}),\quad\text{as }\,t\rightarrow 0^{+}. |  |

For any ε,κ∈(0,∞)\varepsilon,\kappa\in(0,\infty), choose η∈(0,∞)\eta\in(0,\infty) small enough so that ∫[−η,0)z2​ν​(d​z)≤ε2​κ2\int\_{[-\eta,0)}z^{2}\nu(dz)\leq\varepsilon^{2}\kappa^{2}. For any t∈(0,ε2​κ2)t\in(0,\varepsilon^{2}\kappa^{2}), by Markov inequality and Cauchy-Schwarz inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Jt−η+J¯t−η>κ​t)\displaystyle\mathbb{P}\big(J\_{t}^{-\eta}+\overline{J}\_{t}^{-\eta}>\kappa\sqrt{t}\big) | ≤1κ​t​(𝔼​(|Jt−η|)+𝔼​(|J¯t−η|))≤𝔼​(|Jt−η|2)κ​t+tκ​∫(−∞,−η)|z|​ν​(d​z)\displaystyle\leq\frac{1}{\kappa\sqrt{t}}\Big(\mathbb{E}\big(|J\_{t}^{-\eta}|\big)+\mathbb{E}\big(|\overline{J}\_{t}^{-\eta}|\big)\Big)\leq\frac{\sqrt{\mathbb{E}\big(|J\_{t}^{-\eta}|^{2}\big)}}{\kappa\sqrt{t}}+\frac{\sqrt{t}}{\kappa}\int\_{(-\infty,-\eta)}|z|\,\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1κ​(∫[−η,0)z2​ν​(d​z))1/2+tκ​∫(−∞,−η)|z|​ν​(d​z)≤ε​(1+∫(−∞,−η)|z|​ν​(d​z)).\displaystyle=\frac{1}{\kappa}\bigg(\int\_{[-\eta,0)}\!z^{2}\nu(dz)\bigg)^{1/2}\!\!+\frac{\sqrt{t}}{\kappa}\!\int\_{(-\infty,-\eta)}\!|z|\,\nu(dz)\leq\varepsilon\bigg(1+\!\int\_{(-\infty,-\eta)}\!|z|\,\nu(dz)\bigg). |  |

Hence, we conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt−t⟶ℙ 0,t→0+.\displaystyle\frac{J\_{t}^{-}}{\sqrt{t}}\;{\stackrel{{\scriptstyle\mathbb{P}}}{{\longrightarrow}}}\;0,\quad t\rightarrow 0^{+}. |  | (A.1) |

The result of the lemma follows from ([4.1](https://arxiv.org/html/2512.17791v1#S4.E1 "In 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and Slutsky’s theorem. □\Box

### Proof of Lemma [4.5](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

Note that

|  |  |  |
| --- | --- | --- |
|  | |𝔼​((e(r−δ)​τ+Xτ−1−ζ​(τ))+)−𝔼​((eXτ−1−ζ​(τ))+)|≤(e(r−δ)​τ−1)​𝔼​(eXτ)=O​(τ),τ→0+.\displaystyle\bigg|\mathbb{E}\Big(\big(e^{(r-\delta)\tau+X\_{\tau}}\!-1-\zeta(\tau)\big)^{+}\Big)-\mathbb{E}\Big(\big(e^{X\_{\tau}}\!-1-\zeta(\tau)\big)^{+}\Big)\bigg|\leq\big(e^{(r-\delta)\tau}\!-1\big)\mathbb{E}\big(e^{X\_{\tau}}\big)=O(\tau),\quad\tau\rightarrow 0^{+}. |  |

In view of ([4.4](https://arxiv.org/html/2512.17791v1#S4.E4 "In 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and since ez≥1+ze^{z}\geq 1+z, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​((Xτ−ζ​(τ))+)≤𝔼​((eXτ−1−ζ​(τ))+)=O​(τ),τ→0+.\displaystyle\mathbb{E}\big((X\_{\tau}-\zeta(\tau))^{+}\big)\leq\mathbb{E}\Big(\big(e^{X\_{\tau}}-1-\zeta(\tau)\big)^{+}\Big)=O(\tau),\quad\tau\rightarrow 0^{+}. |  |

Hence, we deduce that

|  |  |  |
| --- | --- | --- |
|  | limτ→0+𝔼​((Xττ−ζ​(τ)τ)+)=0.\displaystyle\lim\_{\tau\rightarrow 0^{+}}\mathbb{E}\bigg(\bigg(\frac{X\_{\tau}}{\sqrt{\tau}}-\frac{\zeta(\tau)}{\sqrt{\tau}}\bigg)^{+}\bigg)=0. |  |

Now if we had λ:=lim infτ→0+ζ​(τ)/τ<∞\lambda:=\liminf\_{\tau\rightarrow 0^{+}}\zeta(\tau)/\sqrt{\tau}<\infty, then by Lemma [4.2](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models") and Fatou’s lemma
we would have 𝔼​((σ​W1−λ)+)=0\mathbb{E}((\sigma W\_{1}-\lambda)^{+})=0, and so ℙ​(σ​W1≤λ)=1\mathbb{P}(\sigma W\_{1}\leq\lambda)=1. However, the support of W1W\_{1} is the whole real line. The lemma is proved by contradiction. □\Box

### Proof of Lemma [4.6](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

For any ε∈(0,1)\varepsilon\in(0,1), r∈(0,∞)r\in(0,\infty), and t∈(0,t0]t\in(0,t\_{0}], by Markov inequality, the independence between XWX^{W} and J−J^{-}, and ([4.2](https://arxiv.org/html/2512.17791v1#S4.E2 "In 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(XτW+Jτ−≥r​τ)\displaystyle\mathbb{P}\Big(X\_{\tau}^{W}+J\_{\tau}^{-}\geq r\sqrt{\tau}\Big) | ≤e−p​r​𝔼​(ep​XτW/τ)​𝔼​(ep​Jτ−/τ)\displaystyle\leq e^{-pr}\,\mathbb{E}\Big(e^{pX\_{\tau}^{W}\!/\sqrt{\tau}}\Big)\mathbb{E}\Big(e^{pJ\_{\tau}^{-}\!/\sqrt{\tau}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(−p​r+12​(σ2​p2−p​σ2​τ)+τ​∫(−∞,0)(ep​z/τ−1−pτ​(ez−1))​ν​(d​z))\displaystyle=\exp\!\left(-pr+\frac{1}{2}\big(\sigma^{2}p^{2}\!-\!p\sigma^{2}\!\sqrt{\tau}\big)+\tau\!\int\_{(-\infty,0)}\!\!\bigg(e^{pz/\sqrt{\tau}}\!-\!1\!-\!\frac{p}{\sqrt{\tau}}\big(e^{z}-1\big)\bigg)\nu(dz)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤exp⁡(−p​r+12​(σ2​p2−p​σ2​τ)+p​τ​ν​((−∞,−ε))+p2​∫[−ε,0)z2​ν​(d​z))\displaystyle\leq\exp\bigg(\!\!-\!pr+\frac{1}{2}\big(\sigma^{2}p^{2}-p\sigma^{2}\!\sqrt{\tau}\big)+p\sqrt{\tau}\,\nu((-\infty,-\varepsilon))+p^{2}\int\_{[-\varepsilon,0)}z^{2}\,\nu(dz)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(−p​r+L​p22+p​τ​(ν​((−∞,−ε))−σ22))=e−L​p2/2,\displaystyle=\exp\bigg(\!\!-\!pr+\frac{Lp^{2}}{2}+p\sqrt{\tau}\bigg(\nu((-\infty,-\varepsilon))-\frac{\sigma^{2}}{2}\bigg)\bigg)=e^{-Lp^{2}/2}, |  |

which completes the proof of the lemma. □\Box

### Proof of Lemma [4.7](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

For any ε∈(0,1)\varepsilon\in(0,1), note that τ≤f2​(τ)/(ν​((−∞,−ε))−σ2/2)2\tau\leq f^{2}(\tau)/(\nu((-\infty,-\varepsilon))-\sigma^{2}/2)^{2} for τ>0\tau>0 small enough. Taking r=f​(τ)r=f(\tau) in Lemma [4.6](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), and noting from ([4.6](https://arxiv.org/html/2512.17791v1#S4.E6 "In Lemma 4.6. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([4.7](https://arxiv.org/html/2512.17791v1#S4.E7 "In Lemma 4.6. ‣ 4.1. Step 1: The rate of convergence of 𝑏_𝑒⁢(𝑡) ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) that

|  |  |  |
| --- | --- | --- |
|  | p=p​(τ;f​(τ),σ,ε)∼f​(τ)L,τ→0+,andL=L​(ε;σ)→σ2,ε→0+,\displaystyle p=p(\tau;f(\tau),\sigma,\varepsilon)\sim\frac{f(\tau)}{L},\quad\tau\rightarrow 0^{+},\quad\text{and}\quad L=L(\varepsilon;\sigma)\rightarrow\sigma^{2},\quad\varepsilon\rightarrow 0^{+}, |  |

we deduce that

|  |  |  |
| --- | --- | --- |
|  | lim supτ→0+1f2​(τ)​ln⁡ℙ​(XτW+Jτ−≥τ​f​(τ))≤limε→0+limτ→0+−L​(ε;σ)​p2​(τ;f​(τ),σ,ε)2​f2​(τ)=−12​σ2.\displaystyle\limsup\_{\tau\rightarrow 0^{+}}\frac{1}{f^{2}(\tau)}\ln\mathbb{P}\Big(X\_{\tau}^{W}+J\_{\tau}^{-}\geq\sqrt{\tau}f(\tau)\Big)\leq\lim\_{\varepsilon\rightarrow 0^{+}}\lim\_{\tau\rightarrow 0^{+}}-\frac{L(\varepsilon;\sigma)p^{2}(\tau;f(\tau),\sigma,\varepsilon)}{2f^{2}(\tau)}=-\frac{1}{2\sigma^{2}}. |  |

On the other hand, using the independence between XWX^{W} and J−J^{-}, for any τ∈(0,∞)\tau\in(0,\infty) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(XτW+Jτ−≥τ​f​(τ))\displaystyle\mathbb{P}\Big(X\_{\tau}^{W}+J\_{\tau}^{-}\geq\sqrt{\tau}f(\tau)\Big) | ≥ℙ​(σ​W1+Jτ−τ−σ2​τ2≥f​(τ),|Jτ−τ−σ2​τ2|≤ε)\displaystyle\geq\mathbb{P}\bigg(\sigma W\_{1}+\frac{J\_{\tau}^{-}}{\sqrt{\tau}}-\frac{\sigma^{2}\sqrt{\tau}}{2}\geq f(\tau),\,\bigg|\frac{J\_{\tau}^{-}}{\sqrt{\tau}}-\frac{\sigma^{2}\sqrt{\tau}}{2}\bigg|\leq\varepsilon\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥ℙ​(σ​W1≥f​(τ)+ε)​ℙ​(|Jτ−τ−σ2​τ2|≤ε)\displaystyle\geq\mathbb{P}\big(\sigma W\_{1}\geq f(\tau)+\varepsilon\big)\mathbb{P}\bigg(\bigg|\frac{J\_{\tau}^{-}}{\sqrt{\tau}}-\frac{\sigma^{2}\sqrt{\tau}}{2}\bigg|\leq\varepsilon\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥σ​(f​(τ)+ε)​ϕ​((f​(τ)+ε)/σ)σ2+(f​(τ)+ε)2​ℙ​(|Jτ−τ−σ2​τ2|≤ε),\displaystyle\geq\frac{\sigma\big(f(\tau)+\varepsilon\big)\phi\big((f(\tau)+\varepsilon)/\sigma\big)}{\sigma^{2}+\big(f(\tau)+\varepsilon\big)^{2}}\mathbb{P}\bigg(\bigg|\frac{J\_{\tau}^{-}}{\sqrt{\tau}}-\frac{\sigma^{2}\sqrt{\tau}}{2}\bigg|\leq\varepsilon\bigg), |  |

where ϕ\phi denotes the standard normal density, and we used the following bounds on the tail probability of standard normal distribution in the last inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | z​ϕ​(z)1+z2≤∫z∞ϕ​(z)​𝑑z≤ϕ​(z)z,z∈(0,∞).\displaystyle\frac{z\phi(z)}{1+z^{2}}\leq\int\_{z}^{\infty}\phi(z)\,dz\leq\frac{\phi(z)}{z},\quad z\in(0,\infty). |  | (A.2) |

In view of ([A.1](https://arxiv.org/html/2512.17791v1#A1.E1 "In Proof of Lemma 4.2 ‣ Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |
| --- | --- | --- |
|  | lim infτ→0+ln⁡ℙ​(XτW+Jτ−≥τ​f​(τ))f2​(τ)≥−limτ→0+((f​(τ)+ε)22​σ2​f2​(τ)+ln⁡2​πf2​(τ)−1f2​(τ)​ln⁡(σ​(f​(τ)+ε)σ2+(f​(τ)+ε)2))=−12​σ2,\displaystyle\liminf\_{\tau\rightarrow 0^{+}}\frac{\ln\!\mathbb{P}\Big(\!X\_{\tau}^{W}\!\!+\!J\_{\tau}^{-}\!\geq\!\!\sqrt{\tau}f(\tau)\!\Big)}{f^{2}(\tau)}\!\geq\!-\!\!\lim\_{\tau\rightarrow 0^{+}}\!\!\left(\!\frac{(f(\tau)\!+\!\varepsilon)^{2}}{2\sigma^{2}f^{2}(\tau)}\!+\!\frac{\ln\!\sqrt{2\pi}}{f^{2}(\tau)}\!-\!\frac{1}{f^{2}(\tau)}\!\ln\!\bigg(\frac{\sigma\big(f(\tau)+\varepsilon\big)}{\sigma^{2}\!+\!\big(f(\tau)\!+\!\varepsilon\big)^{2}}\!\bigg)\!\!\right)\!\!=\!-\frac{1}{2\sigma^{2}}, |  |

which completes the proof of the lemma. □\Box

### Proof of ([4.27](https://arxiv.org/html/2512.17791v1#S4.E27 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"))

In view of ([4.26](https://arxiv.org/html/2512.17791v1#S4.E26 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), for any test function ϕ~∈Cc∞​(𝒞~ρ)\widetilde{\phi}\in C\_{c}^{\infty}(\widetilde{\mathcal{C}}\_{\rho}), we have

|  |  |  |
| --- | --- | --- |
|  | ∬C~ρ(d​K4−𝒥1​(t,x)−𝒥2​(t,x))​ϕ~​(t,x)​𝑑x​𝑑t≤σ22​∬C~ρP~​(t,x)​(∂2ϕ~∂x2​(t,x)+∂ϕ~∂x​(t,x))​𝑑x​𝑑t.\displaystyle\iint\_{\widetilde{C}\_{\rho}}\bigg(\frac{dK}{4}-\mathcal{J}\_{1}(t,x)-\mathcal{J}\_{2}(t,x)\bigg)\widetilde{\phi}(t,x)\,dx\,dt\leq\frac{\sigma^{2}}{2}\iint\_{\widetilde{C}\_{\rho}}\widetilde{P}(t,x)\bigg(\frac{\partial^{2}\widetilde{\phi}}{\partial x^{2}}(t,x)+\frac{\partial\widetilde{\phi}}{\partial x}(t,x)\bigg)dx\,dt. |  |

In view of Proposition [2.4](https://arxiv.org/html/2512.17791v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), PP is jointly continuous on [0,T]×ℝ+[0,T]\times\mathbb{R}\_{+}, and so is P~\widetilde{P} on [0,T]×ℝ[0,T]\times\mathbb{R}. Together with the fact that ϕ~∈Cc∞​(𝒞~ρ)\widetilde{\phi}\in C\_{c}^{\infty}(\widetilde{\mathcal{C}}\_{\rho}), we deduce that, for any t∈(T−ρ,T)t\in(T-\rho,T),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ln⁡b​(t)ln⁡be​(t)(d​K4−𝒥1​(t,x)−𝒥2​(t,x))​ϕ~​(t,x)​𝑑x≤σ22​∫ln⁡b​(t)ln⁡be​(t)P~​(t,x)​(∂2ϕ~∂x2​(t,x)+∂ϕ~∂x​(t,x))​𝑑x.\displaystyle\int\_{\ln b(t)}^{\ln b\_{e}(t)}\!\!\bigg(\frac{dK}{4}\!-\!\mathcal{J}\_{1}(t,x)\!-\!\mathcal{J}\_{2}(t,x)\!\bigg)\widetilde{\phi}(t,x)\,dx\leq\frac{\sigma^{2}}{2}\!\int\_{\ln b(t)}^{\ln b\_{e}(t)}\!\widetilde{P}(t,x)\bigg(\frac{\partial^{2}\widetilde{\phi}}{\partial x^{2}}(t,x)\!+\!\frac{\partial\widetilde{\phi}}{\partial x}(t,x)\!\bigg)dx.\quad |  | (A.3) |

For any fixed (t0,x0)∈𝒞~ρ(t\_{0},x\_{0})\in\widetilde{\mathcal{C}}\_{\rho}, we choose (ψn)n∈ℕ⊂Cc∞​(ln⁡b​(t0),ln⁡be​(t0))(\psi\_{n})\_{n\in\mathbb{N}}\subset C\_{c}^{\infty}(\ln b(t\_{0}),\ln b\_{e}(t\_{0})) such that ψn≥0\psi\_{n}\geq 0 and ψn→𝟏(ln⁡b​(t0),x0]\psi\_{n}\rightarrow{\bf 1}\_{(\ln b(t\_{0}),x\_{0}]} pointwisely on (ln⁡b​(t0),ln⁡be​(t0))(\ln b(t\_{0}),\ln b\_{e}(t\_{0})), as n→∞n\rightarrow\infty. Then we extend each ψn\psi\_{n} to ϕ~n∈Cc∞​(𝒞~ρ)\widetilde{\phi}\_{n}\in C\_{c}^{\infty}(\widetilde{\mathcal{C}}\_{\rho}) such that ϕ~n​(t0,⋅)=ψn​(⋅)\widetilde{\phi}\_{n}(t\_{0},\cdot)=\psi\_{n}(\cdot), and clearly ϕ~n\widetilde{\phi}\_{n} satisfies ([A.3](https://arxiv.org/html/2512.17791v1#A1.E3 "In Proof of (4.27) ‣ Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). Denote Ft0​(s):=∂+P​(t0,s)/∂sF\_{t\_{0}}(s):=\partial\_{+}P(t\_{0},s)/\partial s and ϕn​(t,s):=ϕ~n​(t,ln⁡s)\phi\_{n}(t,s):=\widetilde{\phi}\_{n}(t,\ln s), s∈(b​(t0),be​(t0))s\in(b(t\_{0}),b\_{e}(t\_{0})). Due to the convexity of P​(t0,⋅)P(t\_{0},\cdot), Ft0F\_{t\_{0}} is monotone nondecreasing on (b​(t0),be​(t0))(b(t\_{0}),b\_{e}(t\_{0})). Hence, we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫ln⁡b​(t0)ln⁡be​(t0)P~​(t0,x)​(∂2ϕ~n∂x2​(t0,x)+∂ϕ~n∂x​(t0,x))​𝑑x\displaystyle\int\_{\ln b(t\_{0})}^{\ln b\_{e}(t\_{0})}\!\widetilde{P}(t\_{0},x)\bigg(\frac{\partial^{2}\widetilde{\phi}\_{n}}{\partial x^{2}}(t\_{0},x)+\frac{\partial\widetilde{\phi}\_{n}}{\partial x}(t\_{0},x)\bigg)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ln⁡b​(t0)ln⁡be​(t0)P​(t0,ex)​(e2​x​∂2ϕn∂s2​(t0,ex)+2​ex​∂ϕn∂s​(t0,ex))​𝑑x\displaystyle\quad=\int\_{\ln b(t\_{0})}^{\ln b\_{e}(t\_{0})}P(t\_{0},e^{x})\bigg(e^{2x}\frac{\partial^{2}\phi\_{n}}{\partial s^{2}}(t\_{0},e^{x})+2e^{x}\frac{\partial\phi\_{n}}{\partial s}(t\_{0},e^{x})\bigg)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫b​(t0)be​(t0)P​(t0,s)​(s​∂2ϕn∂s2​(t0,s)+2​∂ϕn∂s​(t0,s))​𝑑s=∫b​(t0)be​(t0)P​(t0,s)​∂2(s​ϕn)∂s2​(t0,s)​𝑑s\displaystyle\quad=\int\_{b(t\_{0})}^{b\_{e}(t\_{0})}P(t\_{0},s)\bigg(s\frac{\partial^{2}\phi\_{n}}{\partial s^{2}}(t\_{0},s)+2\frac{\partial\phi\_{n}}{\partial s}(t\_{0},s)\!\bigg)ds=\int\_{b(t\_{0})}^{b\_{e}(t\_{0})}P(t\_{0},s)\frac{\partial^{2}(s\phi\_{n})}{\partial s^{2}}(t\_{0},s)\,ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∫b​(t0)be​(t0)Ft0​(s)​∂(s​ϕn)∂s​(t0,s)​𝑑s=∫b​(t0)be​(t0)s​ϕn​(t0,s)​𝑑Ft0​(s).\displaystyle\quad=-\int\_{b(t\_{0})}^{b\_{e}(t\_{0})}F\_{t\_{0}}(s)\frac{\partial(s\phi\_{n})}{\partial s}(t\_{0},s)\,ds=\int\_{b(t\_{0})}^{b\_{e}(t\_{0})}s\,\phi\_{n}(t\_{0},s)\,dF\_{t\_{0}}(s). |  | (A.4) |

Combining ([A.3](https://arxiv.org/html/2512.17791v1#A1.E3 "In Proof of (4.27) ‣ Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) (for ϕ~n\widetilde{\phi}\_{n} with t=t0t=t\_{0}) and ([A.4](https://arxiv.org/html/2512.17791v1#A1.E4 "In Proof of (4.27) ‣ Appendix A Proofs of Lemmas in Section 4 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain from the dominated convergence that

|  |  |  |
| --- | --- | --- |
|  | ∫ln⁡b​(t0)x0(d​K4−𝒥1​(t0,x)−𝒥2​(t0,x))​𝑑x=limn→∞∫ln⁡b​(t0)ln⁡be​(t0)(d​K4−𝒥1​(t0,x)−𝒥2​(t0,x))​ϕ~n​(t,x)​𝑑x\displaystyle\int\_{\ln b(t\_{0})}^{x\_{0}}\!\bigg(\frac{dK}{4}\!-\!\mathcal{J}\_{1}(t\_{0},x)\!-\!\mathcal{J}\_{2}(t\_{0},x)\bigg)dx=\lim\_{n\rightarrow\infty}\int\_{\ln b(t\_{0})}^{\ln b\_{e}(t\_{0})}\!\bigg(\frac{dK}{4}\!-\!\mathcal{J}\_{1}(t\_{0},x)\!-\!\mathcal{J}\_{2}(t\_{0},x)\bigg)\widetilde{\phi}\_{n}(t,x)dx |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ22​limn→∞∫b​(t0)be​(t0)s​ϕn​(t0,s)​𝑑Ft0​(s)=σ22​∫b​(t0)ex0s​𝑑Ft0​(s)\displaystyle\quad\leq\frac{\sigma^{2}}{2}\lim\_{n\rightarrow\infty}\int\_{b(t\_{0})}^{b\_{e}(t\_{0})}s\,\phi\_{n}(t\_{0},s)\,dF\_{t\_{0}}(s)=\frac{\sigma^{2}}{2}\int\_{b(t\_{0})}^{e^{x\_{0}}}s\,dF\_{t\_{0}}(s) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤σ2​ex02​(Ft0​(ex0)−Ft0​(b​(t0)))=σ2​ex02​(∂+P​(t,ex0)∂s+1).\displaystyle\quad\leq\frac{\sigma^{2}e^{x\_{0}}}{2}\big(F\_{t\_{0}}(e^{x\_{0}})\!-\!F\_{t\_{0}}(b(t\_{0}))\big)=\frac{\sigma^{2}e^{x\_{0}}}{2}\bigg(\frac{\partial\_{+}P(t,e^{x\_{0}})}{\partial s}\!+\!1\!\bigg). |  |

Finally, by taking t0=tt\_{0}=t and x0=a+ln⁡b​(t)x\_{0}=a+\ln b(t), we conclude ([4.27](https://arxiv.org/html/2512.17791v1#S4.E27 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), for any t∈(T−ρ,T)t\in(T-\rho,T) and a∈(0,ln⁡(be​(t)/b​(t)))a\in(0,\ln(b\_{e}(t)/b(t))). □\Box

## Appendix B Proofs of Lemmas in Section [5](https://arxiv.org/html/2512.17791v1#S5 "5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

### Proof of Lemma [5.2](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem2 "Lemma 5.2. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

For any ε∈(0,ln⁡(K/b​(T)))\varepsilon\in(0,\ln(K/b(T))), let T1ε:=inf{t∈ℝ+:|Δ​Xt|>ε}T\_{1}^{\varepsilon}:=\inf\{t\in\mathbb{R}\_{+}:|\Delta X\_{t}|>\varepsilon\}. Clearly

|  |  |  |  |
| --- | --- | --- | --- |
|  | LτK=Lτ∧T1εK+(LτK−Lτ∧T1εK).\displaystyle L\_{\tau}^{K}=L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}+\big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big). |  | (B.1) |

For any t∈ℝ+t\in\mathbb{R}\_{+}, set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ztε:=∫0t∫[−ε,ε]∖{0}z​N​(d​s,d​z),Ztε,+:=∫0t∫(0,ε]z​N​(d​s,d​z),Ztε,−:=∫0t∫[−ε,0)z​N​(d​s,d​z),\displaystyle Z\_{t}^{\varepsilon}:=\!\int\_{0}^{t}\!\int\_{[-\varepsilon,\varepsilon]\setminus\{0\}}\!z\,N(ds,dz),\,\,\,\,Z\_{t}^{\varepsilon,+}:=\!\int\_{0}^{t}\!\int\_{(0,\varepsilon]}\!z\,N(ds,dz),\,\,\,\,Z\_{t}^{\varepsilon,-}:=\!\int\_{0}^{t}\!\int\_{[-\varepsilon,0)}\!z\,N(ds,dz),\quad |  | (B.2) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z¯tε:=Zt−Ztε,Stε:=S0​exp⁡((γ0−σ22)​t+σ​Wt+Ztε),N¯tε:=N​([0,t]×[−ε,ε]c).\displaystyle\overline{Z}\_{t}^{\varepsilon}:=Z\_{t}-Z\_{t}^{\varepsilon},\quad S\_{t}^{\varepsilon}:=S\_{0}\exp\bigg(\bigg(\gamma\_{0}-\frac{\sigma^{2}}{2}\bigg)t+\sigma W\_{t}+Z\_{t}^{\varepsilon}\bigg),\quad\overline{N}\_{t}^{\varepsilon}:=N([0,t]\times[-\varepsilon,\varepsilon]^{c}). |  | (B.3) |

The local time of the process Sε:=(Stε)t∈ℝ+S^{\varepsilon}:=(S\_{t}^{\varepsilon})\_{t\in\mathbb{R}\_{+}} at KK until time tt will be denoted by LtK,εL\_{t}^{K,\varepsilon}.

Step 1. Estimating 𝔼​(Lτ∧T1εK)\mathbb{E}(L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}).

Note that the two processes SS and SεS^{\varepsilon} coincide up to T1εT\_{1}^{\varepsilon}, and so

|  |  |  |
| --- | --- | --- |
|  | Lτ∧T1εK≤Lθ∧T1εK=Lθ∧T1εK,ε≤LθK,ε=LθK,ε​𝟏{τKε<θ}ℙ−a.​s.,\displaystyle L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\leq L\_{\theta\wedge T\_{1}^{\varepsilon}}^{K}=L\_{\theta\wedge T\_{1}^{\varepsilon}}^{K,\varepsilon}\leq L\_{\theta}^{K,\varepsilon}=L\_{\theta}^{K,\varepsilon}{\bf 1}\_{\{\tau\_{K}^{\varepsilon}<\theta\}}\quad\mathbb{P}-\text{a.}\,\text{s.}, |  |

where the last equality is due to the fact that the sample paths of LK,ε:=(LtK,ε)t∈ℝ+L^{K,\varepsilon}:=(L\_{t}^{K,\varepsilon})\_{t\in\mathbb{R}\_{+}} are strictly increasing only on {t∈ℝ+:Stε=K}\{t\in\mathbb{R}\_{+}:S\_{t}^{\varepsilon}=K\} and τKε:=inf{t∈ℝ+:Stε≥K}\tau\_{K}^{\varepsilon}:=\inf\{t\in\mathbb{R}\_{+}:S\_{t}^{\varepsilon}\geq K\}. Hence, by Hölder’s inequality we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(Lτ∧T1εK)≤𝔼​(LθK,ε​𝟏{τKε<θ})≤𝔼​((LθK,ε)2)​ℙ​(τKε<θ)\displaystyle\mathbb{E}\Big(L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big)\leq\mathbb{E}\Big(L\_{\theta}^{K,\varepsilon}{\bf 1}\_{\{\tau\_{K}^{\varepsilon}<\theta\}}\Big)\leq\sqrt{\mathbb{E}\Big(\big(L\_{\theta}^{K,\varepsilon}\big)^{2}\Big)\,\mathbb{P}\big(\tau\_{K}^{\varepsilon}<\theta\big)} |  | (B.4) |

The first expectation on the right-hand side of ([B.4](https://arxiv.org/html/2512.17791v1#A2.E4 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) can be estimated using the Meyer-Itô formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​((LθK,ε)2)=4​𝔼​(((K−Sθε)+−(K−S0)++∫0θ𝟏{St−ε≤K}​St−ε​(γ0​d​t+σ​d​Wt)−∑t∈[0,θ]Δ​(K−Stε)+)2)\displaystyle\mathbb{E}\Big(\big(L\_{\theta}^{K,\varepsilon}\big)^{2}\Big)=4\mathbb{E}\!\left(\!\bigg(\!\big(K\!-\!S\_{\theta}^{\varepsilon}\big)^{+}\!-(K\!-\!S\_{0})^{+}\!+\!\int\_{0}^{\theta}\!{\bf 1}\_{\{S\_{t-}^{\varepsilon}\leq K\}}S\_{t-}^{\varepsilon}\big(\gamma\_{0}dt\!+\!\sigma dW\_{t}\big)-\!\!\sum\_{t\in[0,\theta]}\!\!\Delta\big(K\!-\!S\_{t}^{\varepsilon}\big)^{+}\bigg)^{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤20​𝔼​(2​K2+(∫0θγ0​𝟏{Stε≤K}​Stε​𝑑t)2+(∫0θσ​𝟏{Stε≤K}​Stε​𝑑Wt)2+(∑t∈[0,θ]Δ​(K−Stε)+)2)\displaystyle\quad\leq 20\,\mathbb{E}\left(2K^{2}+\bigg(\int\_{0}^{\theta}\gamma\_{0}{\bf 1}\_{\{S\_{t}^{\varepsilon}\leq K\}}S\_{t}^{\varepsilon}\,dt\bigg)^{2}+\bigg(\int\_{0}^{\theta}\sigma{\bf 1}\_{\{S\_{t}^{\varepsilon}\leq K\}}S\_{t}^{\varepsilon}\,dW\_{t}\bigg)^{2}+\bigg(\sum\_{t\in[0,\theta]}\Delta\big(K-S\_{t}^{\varepsilon}\big)^{+}\bigg)^{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤20​𝔼​(2​K2+∫0θγ02​ 1{Stε≤K}​(Stε)2​𝑑t+∫0θσ2​ 1{Stε≤K}​(Stε)2​𝑑t+(∑t∈[0,θ]St−ε​|eΔ​Ztε−1|)2)\displaystyle\quad\leq 20\,\mathbb{E}\left(2K^{2}+\int\_{0}^{\theta}\gamma\_{0}^{2}\,{\bf 1}\_{\{S\_{t}^{\varepsilon}\leq K\}}\big(S\_{t}^{\varepsilon}\big)^{2}dt+\int\_{0}^{\theta}\sigma^{2}\,{\bf 1}\_{\{S\_{t}^{\varepsilon}\leq K\}}\big(S\_{t}^{\varepsilon}\big)^{2}dt+\bigg(\sum\_{t\in[0,\theta]}S\_{t-}^{\varepsilon}\Big|e^{\Delta Z\_{t}^{\varepsilon}}-1\Big|\bigg)^{2}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤40​K2+20​K2​(γ02+σ2)​θ+4​𝔼​((∑t∈[0,θ]St−ε​|eΔ​Ztε−1|)2)=O​(1),θ→0+,\displaystyle\quad\leq 40K^{2}+20K^{2}\big(\gamma\_{0}^{2}+\sigma^{2}\big)\theta+4\mathbb{E}\left(\bigg(\sum\_{t\in[0,\theta]}S\_{t-}^{\varepsilon}\Big|e^{\Delta Z\_{t}^{\varepsilon}}-1\Big|\bigg)^{2}\right)=O(1),\quad\theta\rightarrow 0^{+}, |  | (B.5) |

where the bound is independent of aa, since the last expectation above can be bounded by (recalling the definition of the process SεS^{\varepsilon} in ([B.3](https://arxiv.org/html/2512.17791v1#A2.E3 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and that S0=b​(T)​ea​θ≤b​(T)S\_{0}=b(T)e^{a\sqrt{\theta}}\leq b(T))

|  |  |  |
| --- | --- | --- |
|  | 𝔼​((∑t∈[0,θ]St−ε​|eΔ​Ztε−1|)2)=𝔼​((∫0θ∫(−ε,ε)∖{0}St−ε​|ez−1|​N​(d​t,d​z))2)\displaystyle\mathbb{E}\left(\bigg(\sum\_{t\in[0,\theta]}S\_{t-}^{\varepsilon}\Big|e^{\Delta Z\_{t}^{\varepsilon}}-1\Big|\bigg)^{2}\right)=\mathbb{E}\left(\bigg(\int\_{0}^{\theta}\int\_{(-\varepsilon,\varepsilon)\setminus\{0\}}S\_{t-}^{\varepsilon}\big|e^{z}-1\big|\,N(dt,dz)\bigg)^{2}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0θ𝔼​((St−ε)2)​𝑑t​∫(−ε,ε)∖{0}(ez−1)2​ν​(d​z)+(∫0θ𝔼​(St−ε)​𝑑t​∫(−ε,ε)∖{0}|ez−1|​ν​(d​z))2\displaystyle\quad=\int\_{0}^{\theta}\mathbb{E}\Big(\big(S\_{t-}^{\varepsilon}\big)^{2}\Big)\,dt\int\_{(-\varepsilon,\varepsilon)\setminus\{0\}}\big(e^{z}-1\big)^{2}\nu(dz)+\bigg(\int\_{0}^{\theta}\mathbb{E}\big(S\_{t-}^{\varepsilon}\big)\,dt\int\_{(-\varepsilon,\varepsilon)\setminus\{0\}}\big|e^{z}-1\big|\,\nu(dz)\bigg)^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫0θ𝔼​(b2​(T)​e(2​γ0−σ2)​t+2​σ​Wt+2​Zt−ε)​𝑑t​∫(−ε,ε)∖{0}(ez−1)2​ν​(d​z)\displaystyle\quad\leq\int\_{0}^{\theta}\mathbb{E}\Big(b^{2}(T)e^{(2\gamma\_{0}-\sigma^{2})t+2\sigma W\_{t}+2Z\_{t-}^{\varepsilon}}\Big)\,dt\int\_{(-\varepsilon,\varepsilon)\setminus\{0\}}\big(e^{z}-1\big)^{2}\nu(dz) |  |
|  |  |  |
| --- | --- | --- |
|  | +(∫0θ𝔼​(b​(T)​e(γ0−σ2/2)​t+σ​Wt+Zt−ε)​𝑑t​∫(−ε,ε)∖{0}|ez−1|​ν​(d​z))2=O​(θ),θ→0+,\displaystyle\qquad+\bigg(\int\_{0}^{\theta}\mathbb{E}\Big(b(T)e^{(\gamma\_{0}-\sigma^{2}/2)t+\sigma W\_{t}+Z\_{t-}^{\varepsilon}}\Big)\,dt\int\_{(-\varepsilon,\varepsilon)\setminus\{0\}}\!\!\big|e^{z}-1\big|\,\nu(dz)\bigg)^{2}=O(\theta),\quad\theta\rightarrow 0^{+}, |  |

where the O​(θ)O(\theta) term is independent of aa. For the last probability on the right-hand side of ([B.4](https://arxiv.org/html/2512.17791v1#A2.E4 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), with cθ:=ln⁡(K/S0)−|γ0−σ2/2|​θc\_{\theta}:=\ln(K/S\_{0})-|\gamma\_{0}-\sigma^{2}/2|\theta and z∈(0,ln⁡(K/b​(T)))z\in(0,\ln(K/b(T))), by ([B.2](https://arxiv.org/html/2512.17791v1#A2.E2 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([B.3](https://arxiv.org/html/2512.17791v1#A2.E3 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) we have,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℙ​(τKε<θ)=ℙ​(supt∈[0,θ]Stε≥K)≤ℙ​(supt∈[0,θ]σ​Wt+Zθε,+≥cθ)\displaystyle\mathbb{P}\big(\tau\_{K}^{\varepsilon}<\theta\big)=\mathbb{P}\Big(\sup\_{t\in[0,\theta]}S\_{t}^{\varepsilon}\geq K\Big)\leq\mathbb{P}\Big(\sup\_{t\in[0,\theta]}\sigma W\_{t}+Z\_{\theta}^{\varepsilon,+}\geq c\_{\theta}\Big) |  | (B.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤ℙ​(supt∈[0,θ]Wt≥cθ−zσ)+ℙ​(Zθε,+≥z)≤e−(cθ−z)2/(2​σ2​θ)+ℙ​(Zθε,+≥z)=o​(θn),θ→0+,\displaystyle\!\!\!\!\!\leq\mathbb{P}\bigg(\sup\_{t\in[0,\theta]}\!W\_{t}\geq\frac{c\_{\theta}\!-\!z}{\sigma}\bigg)+\mathbb{P}\big(Z\_{\theta}^{\varepsilon,+}\!\geq z\big)\leq e^{-(c\_{\theta}-z)^{2}/(2\sigma^{2}\theta)}+\mathbb{P}\big(Z\_{\theta}^{\varepsilon,+}\!\geq z\big)=o\big(\theta^{n}\big),\quad\theta\rightarrow 0^{+},\qquad |  | (B.7) |

for any n∈ℕn\in\mathbb{N}, where the last inequality follows from the Doob’s martingale inequality, and the last equality is due to [[4](https://arxiv.org/html/2512.17791v1#bib.bib4), Remark 3.1]. By combining ([B.4](https://arxiv.org/html/2512.17791v1#A2.E4 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.5](https://arxiv.org/html/2512.17791v1#A2.E5 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.7](https://arxiv.org/html/2512.17791v1#A2.E7 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(Lτ∧T1εK)=o​(θn),θ→0+,\displaystyle\mathbb{E}\big(L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)=o\big(\theta^{n}\big),\quad\theta\rightarrow 0^{+}, |  | (B.8) |

for any n∈ℕn\in\mathbb{N}, where the o​(θn)o(\theta^{n}) term is independent of aa.

Step 2. Estimating 𝔼​(LτK−Lτ∧T1εK)\mathbb{E}(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}).

Denoting by 𝔼x(⋅):=𝔼(⋅|S0=x)\mathbb{E}\_{x}(\cdot):=\mathbb{E}(\cdot\,|\,S\_{0}=x). The strong Markov property and time-homogeneity of SS imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(LτK−Lτ∧T1εK)\displaystyle\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big) | =𝔼​(𝟏{T1ε<τ}​(LτK−Lτ∧T1εK))=𝔼​(𝟏{T1ε<τ}​𝔼​((LτK−Lτ∧T1εK)|ℱτ∧T1ε))\displaystyle=\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\tau\}}\big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)\Big)=\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\tau\}}\,\mathbb{E}\Big(\big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)\,\big|\,\mathscr{F}\_{\tau\wedge T\_{1}^{\varepsilon}}\Big)\Big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​(𝟏{T1ε<τ}​𝔼ST1ε​(Lτ−τ∧T1εK))≤𝔼​(𝟏{T1ε<θ}​𝔼ST1ε​(LθK)).\displaystyle=\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\tau\}}\,\mathbb{E}\_{S\_{T\_{1}^{\varepsilon}}}\big(L\_{\tau-\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)\Big)\leq\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\theta\}}\,\mathbb{E}\_{S\_{T\_{1}^{\varepsilon}}}\big(L\_{\theta}^{K}\big)\Big). |  | (B.9) |

2.1. Estimating 𝔼x​(LθK)\mathbb{E}\_{x}(L^{K}\_{\theta}).

By the Meyer-Itô formula, we have

|  |  |  |
| --- | --- | --- |
|  | 12​𝔼x​(LθK)=𝔼x​((K−Sθ)+)−(K−x)++𝔼​(∫0θγ0​𝟏{St−≤K}​St−​𝑑t+∫0θ∫ℝ0Φ​(St−,z)​ν​(d​z)​𝑑t),\displaystyle\frac{1}{2}\mathbb{E}\_{x}\big(L\_{\theta}^{K}\big)=\mathbb{E}\_{x}\big((K-S\_{\theta})^{+}\big)-(K-x)^{+}+\mathbb{E}\bigg(\int\_{0}^{\theta}\gamma\_{0}{\bf 1}\_{\{S\_{t-}\leq K\}}S\_{t-}\,dt+\int\_{0}^{\theta}\int\_{\mathbb{R}\_{0}}\Phi(S\_{t-},z)\,\nu(dz)\,dt\bigg), |  |

where Φ​(y,z):=(K−y​ez)+−(K−y)+\Phi(y,z):=(K-ye^{z})^{+}-(K-y)^{+} satisfies |Φ​(y,z)|≤|y​(ez−1)||\Phi(y,z)|\leq|y(e^{z}-1)|, and so by ([5.1](https://arxiv.org/html/2512.17791v1#S5.E1 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 12​𝔼x​(LθK)\displaystyle\frac{1}{2}\mathbb{E}\_{x}\big(L\_{\theta}^{K}\big) | =𝔼x​((K−Sθ)+)−(K−x)++x​O​(θ)\displaystyle=\mathbb{E}\_{x}\big((K-S\_{\theta})^{+}\big)-(K-x)^{+}+xO(\theta) |  | (B.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼x​((K−x​e(γ0−σ2/2)​θ+σ​Wθ+Zθ)+)−(K−x)++x​O​(θ),θ→0+,\displaystyle=\mathbb{E}\_{x}\bigg(\Big(K-x\,e^{(\gamma\_{0}-\sigma^{2}/2)\theta+\sigma W\_{\theta}+Z\_{\theta}}\Big)^{+}\bigg)-(K-x)^{+}+xO(\theta),\quad\theta\rightarrow 0^{+}, |  | (B.11) |

where the O​(θ)O(\theta) term is independent of xx. By the independence of WW and Z:=(Zt)t∈ℝ+Z:=(Z\_{t})\_{t\in\mathbb{R}\_{+}}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼x​(|e(γ0−σ2/2)​θ+σ​Wθ+Zθ−eσ​Wθ|)=eσ2​θ/2​𝔼x​(|e(γ0−σ2/2)​θ+Zθ−1|)=O​(θ),θ→0+.\displaystyle\mathbb{E}\_{x}\Big(\Big|e^{(\gamma\_{0}-\sigma^{2}/2)\theta+\sigma W\_{\theta}+Z\_{\theta}}-e^{\sigma W\_{\theta}}\Big|\Big)=e^{\sigma^{2}\theta/2}\,\mathbb{E}\_{x}\Big(\Big|e^{(\gamma\_{0}-\sigma^{2}/2)\theta+Z\_{\theta}}-1\Big|\Big)=O(\theta),\quad\theta\rightarrow 0^{+}. |  |

Hence, using [[2](https://arxiv.org/html/2512.17791v1#bib.bib2), Lemma 3.3], we deduce that, as θ→0+\theta\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​𝔼x​(LθK)\displaystyle\frac{1}{2}\mathbb{E}\_{x}\big(L\_{\theta}^{K}\big) | =𝔼x​((K−x​eσ​Wθ)+)−(K−x)++x​O​(θ)=𝔼x​((K−x​(1+σ​Wθ))+)−(K−x)++x​O​(θ)\displaystyle=\mathbb{E}\_{x}\big(\big(K\!-\!x\,e^{\sigma W\_{\theta}}\big)^{+}\big)-(K\!-\!x)^{+}\!+xO(\theta)=\mathbb{E}\_{x}\big((K\!-\!x(1\!+\!\sigma W\_{\theta}))^{+}\big)-(K\!-\!x)^{+}\!+xO(\theta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x​σ​(𝔼x​((K−xx​σ−Wθ)+)−(K−xx​σ)+)+x​O​(θ)≤x​σ​θ2​π​exp⁡(−(K−x)22​x2​σ2​θ)+x​O​(θ),\displaystyle=x\sigma\!\left(\mathbb{E}\_{x}\!\left(\!\bigg(\frac{K\!-\!x}{x\sigma}\!-\!W\_{\theta}\bigg)^{+}\!\right)\!-\!\bigg(\frac{K\!-\!x}{x\sigma}\bigg)^{+}\right)\!+xO(\theta)\leq\frac{x\sigma\sqrt{\theta}}{\sqrt{2\pi}}\exp\bigg(\!\!-\!\frac{(K\!-\!x)^{2}}{2x^{2}\sigma^{2}\theta}\bigg)\!+\!xO(\theta), |  |

where the O​(θ)O(\theta) term is independent of xx.

Next, plugging back intp ([B.9](https://arxiv.org/html/2512.17791v1#A2.E9 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​𝔼​(LτK−Lτ∧T1εK)\displaystyle\frac{1}{2}\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big) | ≤σ​θ2​π​𝔼​(𝟏{T1ε<θ}​ST1ε​exp⁡(−(K−ST1ε)22​σ2​θ​ST1ε))+𝔼​(𝟏{T1ε<θ}​ST1ε)​O​(θ),\displaystyle\leq\frac{\sigma\sqrt{\theta}}{\sqrt{2\pi}}\mathbb{E}\left({\bf 1}\_{\{T\_{1}^{\varepsilon}<\theta\}}S\_{T\_{1}^{\varepsilon}}\exp\bigg(\!-\frac{\big(K-S\_{T\_{1}^{\varepsilon}}\big)^{2}}{2\sigma^{2}\theta S\_{T\_{1}^{\varepsilon}}}\bigg)\right)+\mathbb{E}\big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\theta\}}S\_{T\_{1}^{\varepsilon}}\big)O(\theta), |  |

as θ→0+\theta\rightarrow 0^{+}, where the O​(θ)O(\theta) term is independent of aa. Note that, conditionally on {T1ε<θ}\{T\_{1}^{\varepsilon}<\theta\}, T1εT\_{1}^{\varepsilon} is uniformly distributed on [0,θ][0,\theta]. Since T1εT\_{1}^{\varepsilon}, WW, Zε:=(Ztε)t∈ℝ+Z^{\varepsilon}:=(Z\_{t}^{\varepsilon})\_{t\in\mathbb{R}\_{+}}, and Z¯ε:=(Z¯tε)t∈ℝ+\overline{Z}^{\varepsilon}:=(\overline{Z}\_{t}^{\varepsilon})\_{t\in\mathbb{R}\_{+}} are independent,

|  |  |  |
| --- | --- | --- |
|  | ST1ε|{T1ε<θ}=𝔇b(T)ea​θ+(γ0−σ2/2)​θ​U+Wθ​U+Zθ​Uε+Vε=:Γθ,\displaystyle S\_{T\_{1}^{\varepsilon}}\big|\,\{T\_{1}^{\varepsilon}<\theta\}\,{\,\stackrel{{\scriptstyle\mathfrak{D}}}{{=}}\,}\,b(T)\,e^{a\sqrt{\theta}+(\gamma\_{0}-\sigma^{2}/2)\theta U+W\_{\theta U}+Z\_{\theta U}^{\varepsilon}+V\_{\varepsilon}}=:\Gamma\_{\theta}, |  |

where U∼𝒰​[0,1]U\sim\mathcal{U}[0,1], Vε=𝔇Z¯T1εεV\_{\varepsilon}{\,\stackrel{{\scriptstyle\mathfrak{D}}}{{=}}\,}\overline{Z}\_{T\_{1}^{\varepsilon}}^{\varepsilon}, and UU, VεV\_{\varepsilon}, WW, and ZεZ^{\varepsilon} are independent. Therefore, we conclude that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​(LτK−Lτ∧T1εK)≤(σ​2​θπ​𝔼​(Γθ​exp⁡(−(K−Γθ)22​σ2​θ​Γθ))+𝔼​(Γθ)​O​(θ))​ℙ​(T1ε<θ)\displaystyle\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big)\leq\left(\frac{\sigma\sqrt{2\theta}}{\sqrt{\pi}}\mathbb{E}\left(\Gamma\_{\theta}\exp\bigg(\!-\frac{\big(K-\Gamma\_{\theta}\big)^{2}}{2\sigma^{2}\theta\Gamma\_{\theta}}\bigg)\right)+\mathbb{E}\big(\Gamma\_{\theta}\big)O(\theta)\right)\mathbb{P}\big(T\_{1}^{\varepsilon}<\theta\big) |  | (B.12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤(2​σπ+O​(θ))​𝔼​(b​(T)​e(γ0−σ2/2)​θ​U+Wθ​U+Zθ​Uε+Vε)​ν​([−ε,ε]c)​θ3/2,θ→0+,\displaystyle\quad\leq\bigg(\frac{\sqrt{2}\sigma}{\sqrt{\pi}}+O(\sqrt{\theta})\bigg)\mathbb{E}\Big(b(T)\,e^{(\gamma\_{0}-\sigma^{2}/2)\theta U+W\_{\theta U}+Z\_{\theta U}^{\varepsilon}+V\_{\varepsilon}}\Big)\nu\big([-\varepsilon,\varepsilon]^{c}\big)\theta^{3/2},\quad\theta\rightarrow 0^{+}, |  | (B.13) |

where the O​(θ)O(\sqrt{\theta}) term is independent of aa. Combining ([B.1](https://arxiv.org/html/2512.17791v1#A2.E1 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.8](https://arxiv.org/html/2512.17791v1#A2.E8 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.13](https://arxiv.org/html/2512.17791v1#A2.E13 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) leads to the inequality in ([5.3](https://arxiv.org/html/2512.17791v1#S5.E3 "In Lemma 5.2. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")).

2.2. Estimating 𝔼​(LτK−Lτ∧T1εK)\mathbb{E}(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}) and proving the equality in ([5.3](https://arxiv.org/html/2512.17791v1#S5.E3 "In Lemma 5.2. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) when ν​({ln⁡(K/b​(T))})=0\nu(\{\ln(K/b(T))\})=0.

As θ→0+\theta\rightarrow 0^{+}, we have Γθ→b​(T)​eVε\Gamma\_{\theta}\rightarrow b(T)e^{V\_{\varepsilon}}. When ν​({ln⁡(K/b​(T))})=0\nu(\{\ln(K/b(T))\})=0, b​(T)​eVε≠Kb(T)e^{V\_{\varepsilon}}\neq K ℙ\mathbb{P}-a. s. Therefore, we deduce from the dominated convergence that

|  |  |  |
| --- | --- | --- |
|  | limθ→0+𝔼​(Γθ​exp⁡(−(K−Γθ)22​σ2​θ​Γθ))=0,\displaystyle\lim\_{\theta\rightarrow 0^{+}}\mathbb{E}\left(\Gamma\_{\theta}\exp\bigg(\!-\frac{\big(K-\Gamma\_{\theta}\big)^{2}}{2\sigma^{2}\theta\Gamma\_{\theta}}\bigg)\right)=0, |  |

By ([B.12](https://arxiv.org/html/2512.17791v1#A2.E12 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), this implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(LτK−Lτ∧T1εK)=o​(θ3/2),θ→0+.\displaystyle\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big)=o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}. |  | (B.14) |

Together with ([B.1](https://arxiv.org/html/2512.17791v1#A2.E1 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([B.8](https://arxiv.org/html/2512.17791v1#A2.E8 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(LτK)=o​(θ3/2),θ→0+.\displaystyle\mathbb{E}\big(L\_{\tau}^{K}\big)=o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}. |  |

2.3. Estimating 𝔼​(LτK−Lτ∧T1εK)\mathbb{E}(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}) and proving the equality in ([5.3](https://arxiv.org/html/2512.17791v1#S5.E3 "In Lemma 5.2. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) when ν​({ln⁡(K/b​(T))})≠0\nu(\{\ln(K/b(T))\})\neq 0.

Now assume ν​({ln⁡(K/b​(T))})≠0\nu(\{\ln(K/b(T))\})\neq 0. Introduce the processes X^:=(X^t)t∈ℝ+\widehat{X}:=(\widehat{X}\_{t})\_{t\in\mathbb{R}\_{+}} and Z^:=(Z^t)t∈ℝ+\widehat{Z}:=(\widehat{Z}\_{t})\_{t\in\mathbb{R}\_{+}} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z^t:=∫0t∫{ln⁡(K/b​(T))}z​N​(d​s,d​z),X^t:=X~t−Z^t,t∈ℝ+,\displaystyle\widehat{Z}\_{t}:=\int\_{0}^{t}\int\_{\{\ln(K/b(T))\}}z\,N(ds,dz),\quad\widehat{X}\_{t}:=\widetilde{X}\_{t}-\widehat{Z}\_{t},\quad t\in\mathbb{R}\_{+}, |  | (B.15) |

and let T^1:=inf{t∈ℝ+:Δ​Z^t≠0}\widehat{T}\_{1}:=\inf\{t\in\mathbb{R}\_{+}:\Delta\widehat{Z}\_{t}\neq 0\}. Since T1ε≤T^1T\_{1}^{\varepsilon}\leq\widehat{T}\_{1} (recalling ε<ln⁡(K/b​(T))\varepsilon<\ln(K/b(T))), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​(LτK−Lτ∧T1εK)=𝔼​(LτK−Lτ∧T^1K)+𝔼​(Lτ∧T^1K−Lτ∧T1εK)\displaystyle\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big)=\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge\widehat{T}\_{1}}^{K}\Big)+\mathbb{E}\Big(L\_{\tau\wedge\widehat{T}\_{1}}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big) |  | (B.16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​(LτK−Lτ∧T^1K)+𝔼​(𝟏{T1ε<τ<T^1}​(LτK−Lτ∧T1εK))+𝔼​(𝟏{T1ε<T^1≤τ}​(Lτ∧T^1K−Lτ∧T1εK)).\displaystyle\quad=\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge\widehat{T}\_{1}}^{K}\Big)+\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\tau<\widehat{T}\_{1}\}}\big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)\Big)+\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\widehat{T}\_{1}\leq\tau\}}\big(L\_{\tau\wedge\widehat{T}\_{1}}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)\Big).\qquad |  | (B.17) |

Note that prior to T^1\widehat{T}\_{1}, the process X~\widetilde{X} matches with the process X^\widehat{X} whose Lévy measure does not charge the point ln⁡(K/b​(T))\ln(K/b(T)). It follows from ([B.14](https://arxiv.org/html/2512.17791v1#A2.E14 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(𝟏{T1ε<τ<T^1}​(LτK−Lτ∧T1εK))=o​(θ3/2),θ→0+.\displaystyle\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\tau<\widehat{T}\_{1}\}}\big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)\Big)=o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}. |  | (B.18) |

Also, on the event {T1ε<T^1≤τ}⊂{T1ε<T^1≤θ}\{T\_{1}^{\varepsilon}<\widehat{T}\_{1}\leq\tau\}\subset\{T\_{1}^{\varepsilon}<\widehat{T}\_{1}\leq\theta\} (since τ≤θ\tau\leq\theta), the process Z¯ε\overline{Z}^{\varepsilon} jumps at least two times before θ\theta, and so

|  |  |  |
| --- | --- | --- |
|  | ℙ​(T1ε<T^1≤θ)≤ℙ​(∑t∈[0,θ]𝟏{Δ​Z¯tε≠0}≥2)=O​(θ2),θ→0+.\displaystyle\mathbb{P}\big(T\_{1}^{\varepsilon}<\widehat{T}\_{1}\leq\theta\big)\leq\mathbb{P}\bigg(\sum\_{t\in[0,\theta]}{\bf 1}\_{\{\Delta\overline{Z}^{\varepsilon}\_{t}\neq 0\}}\geq 2\bigg)=O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+}. |  |

Hence, by the strong Markov property and time-homogeneity of SS, we deduce that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​(𝟏{T1ε<T^1≤τ}​(Lτ∧T^1K−Lτ∧T1εK))\displaystyle\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\widehat{T}\_{1}\leq\tau\}}\big(L\_{\tau\wedge\widehat{T}\_{1}}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\big)\Big) | ≤𝔼​(𝟏{T1ε<T^1≤θ}​𝔼ST^1​(LθK))\displaystyle\leq\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\widehat{T}\_{1}\leq\theta\}}\mathbb{E}\_{S\_{\widehat{T}\_{1}}}\!\big(L\_{\theta}^{K}\big)\Big) |  | (B.19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤𝔼​(𝟏{T1ε<T^1≤θ}​(2​K+ST^1​O​(θ)))=O​(θ2),θ→0+,\displaystyle\leq\mathbb{E}\Big({\bf 1}\_{\{T\_{1}^{\varepsilon}<\widehat{T}\_{1}\leq\theta\}}\big(2K+S\_{\widehat{T}\_{1}}O(\theta)\big)\Big)=O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+},\quad |  | (B.20) |

where we used ([B.10](https://arxiv.org/html/2512.17791v1#A2.E10 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) in the second inequality. Combining ([B.17](https://arxiv.org/html/2512.17791v1#A2.E17 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.18](https://arxiv.org/html/2512.17791v1#A2.E18 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.20](https://arxiv.org/html/2512.17791v1#A2.E20 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) leads to

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(LτK−Lτ∧T1εK)=𝔼​(LτK−Lτ∧T^1K)+o​(θ3/2),θ→0+.\displaystyle\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge T\_{1}^{\varepsilon}}^{K}\Big)=\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge\widehat{T}\_{1}}^{K}\Big)+o\big(\theta^{3/2}\big),\quad\theta\rightarrow 0^{+}. |  |

Next, by the strong Markov property and the time-homogeneity of SS as well as ([B.10](https://arxiv.org/html/2512.17791v1#A2.E10 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we have

|  |  |  |
| --- | --- | --- |
|  | 12​𝔼​(LτK−Lτ∧T^1K)=12​𝔼​(𝟏{T^1<τ}​𝔼ST^1​(Lτ−τ∧T^1K))\displaystyle\frac{1}{2}\,\mathbb{E}\Big(L\_{\tau}^{K}-L\_{\tau\wedge\widehat{T}\_{1}}^{K}\Big)=\frac{1}{2}\,\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\mathbb{E}\_{S\_{\widehat{T}\_{1}}}\!\big(L\_{\tau-\tau\wedge\widehat{T}\_{1}}^{K}\big)\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​(𝟏{T^1<τ}​(𝔼ST^1​((K−Sτ−τ∧T^1)+)−(K−ST^1)++O​(θ2)))\displaystyle\quad=\mathbb{E}\bigg({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\Big(\mathbb{E}\_{S\_{\widehat{T}\_{1}}}\!\Big(\big(K-S\_{\tau-\tau\wedge\widehat{T}\_{1}}\big)^{+}\Big)-\big(K-S\_{\widehat{T}\_{1}}\big)^{+}+O\big(\theta^{2}\big)\Big)\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​(𝟏{T^1<τ}​((K−Sτ)+−(K−ST^1)+))+O​(θ2)\displaystyle\quad=\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\Big(\big(K-S\_{\tau}\big)^{+}-\big(K-S\_{\widehat{T}\_{1}}\big)^{+}\Big)\Big)+O\big(\theta^{2}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​(𝟏{T^1<τ}​((K−K​S0b​(T)​eX~τ+X^T^1−X~T^1)+−(K−K​S0​eX^T^1b​(T))+))+O​(θ2),θ→0+,\displaystyle\quad=\mathbb{E}\left({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\left(\bigg(K-\frac{KS\_{0}}{b(T)}e^{\widetilde{X}\_{\tau}+\widehat{X}\_{\widehat{T}\_{1}}-\widetilde{X}\_{\widehat{T}\_{1}}}\bigg)^{+}-\bigg(K-\frac{KS\_{0}\,e^{\widehat{X}\_{\widehat{T}\_{1}}}}{b(T)}\bigg)^{+}\right)\right)+O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+}, |  |

where the last equality follows from the fact that X~T^1−X^T^1=ln⁡(K/b​(T))\widetilde{X}\_{\widehat{T}\_{1}}-\widehat{X}\_{\widehat{T}\_{1}}=\ln(K/b(T)). Since ℙ​(N¯θε≥2)=O​(θ2)\mathbb{P}(\overline{N}\_{\theta}^{\varepsilon}\geq 2)=O(\theta^{2}), we deduce that, as θ→0+\theta\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(LτK−Lτ∧T^1K)\displaystyle\mathbb{E}\Big(L\_{\tau}^{K}\!-\!L\_{\tau\wedge\widehat{T}\_{1}}^{K}\Big) | =2​K​𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​((1−S0​eX~τ+X^T^1−X~T^1b​(T))+−(1−S0​eX^T^1b​(T))+))+O​(θ2)\displaystyle=2K\,\mathbb{E}\!\left(\!{\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\!\left(\!\bigg(1-\frac{S\_{0}\,e^{\widetilde{X}\_{\tau}+\widehat{X}\_{\widehat{T}\_{1}}-\widetilde{X}\_{\widehat{T}\_{1}}}}{b(T)}\bigg)^{+}\!\!-\bigg(1-\frac{S\_{0}\,e^{\widehat{X}\_{\widehat{T}\_{1}}}}{b(T)}\bigg)^{+}\right)\!\right)\!+O\big(\theta^{2}\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​K​𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​((1−S0​eX^τb​(T))+−(1−S0​eX^T^1b​(T))+))+O​(θ2).\displaystyle=2K\,\mathbb{E}\left({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\left(\bigg(1-\frac{S\_{0}\,e^{\widehat{X}\_{\tau}}}{b(T)}\bigg)^{+}\!-\bigg(1-\frac{S\_{0}\,e^{\widehat{X}\_{\widehat{T}\_{1}}}}{b(T)}\bigg)^{+}\right)\right)+O\big(\theta^{2}\big). |  | (B.21) |

To further estimate the first expectation in ([B.21](https://arxiv.org/html/2512.17791v1#A2.E21 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we first have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(1−S0​eX^τb​(T))+)=𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​𝟏{a​θ+X^τ≤0}​(1−ea​θ+X^τ))\displaystyle\mathbb{E}\left({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\bigg(1-\frac{S\_{0}\,e^{\widehat{X}\_{\tau}}}{b(T)}\bigg)^{+}\right)=\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}{\bf 1}\_{\{a\sqrt{\theta}+\widehat{X}\_{\tau}\leq 0\}}\big(1-e^{a\sqrt{\theta}+\widehat{X}\_{\tau}}\big)\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​𝟏{a​θ+X^τ≤0}​(1−ea​θ+X^τ+a​θ+X^τ))+𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(−a​θ−X^τ)+).\displaystyle=\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}{\bf 1}\_{\{a\sqrt{\theta}+\widehat{X}\_{\tau}\leq 0\}}\big(1\!-\!e^{a\sqrt{\theta}+\widehat{X}\_{\tau}}\!+\!a\sqrt{\theta}\!+\!\widehat{X}\_{\tau}\big)\Big)+\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\big(\!-\!a\sqrt{\theta}\!-\!\widehat{X}\_{\tau}\big)^{+}\Big). |  |

Recalling that τ\tau takes values in [0,θ][0,\theta] and ε∈(0,ln⁡(K/b​(T)))\varepsilon\in(0,\ln(K/b(T))), we see that Z¯τε=Z^τ=ln⁡(K/b​(T))\overline{Z}\_{\tau}^{\varepsilon}=\widehat{Z}\_{\tau}=\ln(K/b(T)) and on the event {N¯θε=1,T^1<τ}\{\overline{N}\_{\theta}^{\varepsilon}=1,\widehat{T}\_{1}<\tau\}. Using the independence between N¯ε:=(N¯tε)t∈ℝ+\overline{N}^{\varepsilon}:=(\overline{N}^{\varepsilon}\_{t})\_{t\in\mathbb{R}\_{+}}, WW, and ZεZ^{\varepsilon} together with ([5.1](https://arxiv.org/html/2512.17791v1#S5.E1 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.3](https://arxiv.org/html/2512.17791v1#A2.E3 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.15](https://arxiv.org/html/2512.17791v1#A2.E15 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​𝟏{a​θ+X^τ≤0}​|1−ea​θ+X^τ+a​θ+X^τ|)≤𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(a​θ+X^τ)2)\displaystyle\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}{\bf 1}\_{\{a\sqrt{\theta}+\widehat{X}\_{\tau}\leq 0\}}\big|1-e^{a\sqrt{\theta}+\widehat{X}\_{\tau}}+a\sqrt{\theta}+\widehat{X}\_{\tau}\big|\Big)\leq\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\big(a\sqrt{\theta}+\widehat{X}\_{\tau}\big)^{2}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(a​θ+X~τ−ln⁡(K/b​(T)))2)=𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(a​θ+(r−δ)​τ+σ​Wτ+Zτε)2)\displaystyle=\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\!\big(a\sqrt{\theta}+\!\widetilde{X}\_{\tau}\!-\!\ln(K/b(T))\big)^{2}\Big)\!=\!\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\!\big(a\sqrt{\theta}\!+\!(r\!-\!\delta)\tau\!+\!\sigma W\_{\tau}\!+\!Z\_{\tau}^{\varepsilon}\big)^{2}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤4​(r−δ)​θ2+4​ℙ​(N¯θε=1)​(a2​θ+𝔼​(supt∈[0,θ]σ2​Wt2+(Zτε)2))=O​(θ2),θ→0+,\displaystyle\leq 4(r-\delta)\theta^{2}+4\,\mathbb{P}\big(\overline{N}\_{\theta}^{\varepsilon}=1\big)\bigg(a^{2}\theta+\mathbb{E}\Big(\sup\_{t\in[0,\theta]}\sigma^{2}W\_{t}^{2}+(Z\_{\tau}^{\varepsilon})^{2}\Big)\bigg)=O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+}, |  |

and that

|  |  |  |
| --- | --- | --- |
|  | |𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(−a​θ−X^τ)+)−𝔼​(𝟏{T^1<τ}​(−a​θ−σ​Wτ)+)|\displaystyle\bigg|\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\big(\!-a\sqrt{\theta}-\widehat{X}\_{\tau}\big)^{+}\Big)-\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\big(\!-a\sqrt{\theta}-\sigma W\_{\tau}\big)^{+}\Big)\bigg| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​|(−a​θ−X^τ)+−(−a​θ−σ​Wτ)+|)+𝔼​(𝟏{N¯θε≥2}​(−a​θ−σ​Wτ)+)\displaystyle\quad\leq\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\big|\big(\!-a\sqrt{\theta}-\widehat{X}\_{\tau}\big)^{+}-\big(\!-a\sqrt{\theta}-\sigma W\_{\tau}\big)^{+}\big|\Big)+\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}\geq 2\}}\big(\!-a\sqrt{\theta}-\sigma W\_{\tau}\big)^{+}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼​(𝟏{N¯θε=1}​|Zτε+(γ0−σ22)​τ|)+𝔼​(𝟏{N¯θε≥2}​(−a​θ−σ​Wτ)+)\displaystyle\quad\leq\mathbb{E}\left({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}\bigg|Z\_{\tau}^{\varepsilon}+\bigg(\gamma\_{0}-\frac{\sigma^{2}}{2}\bigg)\tau\bigg|\right)+\mathbb{E}\Big({\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}\geq 2\}}\big(\!-a\sqrt{\theta}-\sigma W\_{\tau}\big)^{+}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤ℙ​(N¯θε=1)​(𝔼​(Zτε)+|γ0−σ22|​θ)+ℙ​(N¯θε≥2)​𝔼​(|a​θ+σ​Wτ|)=O​(θ2),θ→0+.\displaystyle\quad\leq\mathbb{P}\big(\overline{N}\_{\theta}^{\varepsilon}=1\big)\left(\mathbb{E}\big(Z\_{\tau}^{\varepsilon}\big)+\bigg|\gamma\_{0}-\frac{\sigma^{2}}{2}\bigg|\theta\right)+\mathbb{P}\big(\overline{N}\_{\theta}^{\varepsilon}\geq 2\big)\mathbb{E}\big(|a\sqrt{\theta}+\sigma W\_{\tau}|\big)=O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+}. |  |

Hence, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(1−S0​eX^τb​(T))+)=𝔼​(𝟏{T^1<τ}​(−a​θ−σ​Wτ)+)+O​(θ2),θ→0+.\displaystyle\mathbb{E}\left(\!{\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\bigg(1\!-\!\frac{S\_{0}\,e^{\widehat{X}\_{\tau}}}{b(T)}\bigg)^{+}\right)=\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\!\big(\!-\!a\sqrt{\theta}\!-\!\sigma W\_{\tau}\big)^{+}\Big)+O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+}.\quad |  | (B.22) |

Similar arguments lead to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(𝟏{N¯θε=1}​𝟏{T^1<τ}​(1−S0​eX^T^1b​(T))+)=𝔼​(𝟏{T^1<τ}​(−a​θ−σ​WT^1)+)+O​(θ2),θ→0+.\displaystyle\mathbb{E}\left(\!{\bf 1}\_{\{\overline{N}\_{\theta}^{\varepsilon}=1\}}{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\bigg(1\!-\!\frac{S\_{0}\,e^{\widehat{X}\_{\widehat{T}\_{1}}}}{b(T)}\bigg)^{+}\right)=\mathbb{E}\Big({\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\!\big(\!-\!a\sqrt{\theta}\!-\!\sigma W\_{\widehat{T}\_{1}}\big)^{+}\Big)+O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+}.\qquad |  | (B.23) |

By Combining ([B.21](https://arxiv.org/html/2512.17791v1#A2.E21 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.22](https://arxiv.org/html/2512.17791v1#A2.E22 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.23](https://arxiv.org/html/2512.17791v1#A2.E23 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(LτK−Lτ∧T^1K)=2​K​𝔼​(𝟏{T^1<τ}​((−a​θ−σ​Wτ)+−(−a​θ−σ​WT^1)+))+O​(θ2),θ→0+.\displaystyle\!\!\!\!\mathbb{E}\Big(\!L\_{\tau}^{K}\!-\!L\_{\tau\wedge\widehat{T}\_{1}}^{K}\!\Big)\!=\!2K\mathbb{E}\Big(\!{\bf 1}\_{\{\widehat{T}\_{1}<\tau\}}\!\Big(\big(\!-\!a\sqrt{\theta}\!-\!\sigma W\_{\tau}\big)^{+}\!\!-\!\big(\!-\!a\sqrt{\theta}\!-\!\sigma W\_{\widehat{T}\_{1}}\big)^{+}\Big)\!\Big)\!+\!O\big(\theta^{2}\big),\quad\theta\rightarrow 0^{+}.\quad |  | (B.24) |

Finally, by combining ([B.1](https://arxiv.org/html/2512.17791v1#A2.E1 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.8](https://arxiv.org/html/2512.17791v1#A2.E8 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.24](https://arxiv.org/html/2512.17791v1#A2.E24 "In Proof of Lemma 5.2 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we deduce the inequality in ([5.3](https://arxiv.org/html/2512.17791v1#S5.E3 "In Lemma 5.2. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). □\Box

### Proof of Lemma [5.5](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem5 "Lemma 5.5. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")

The variational inequality ([4.15](https://arxiv.org/html/2512.17791v1#S4.E15 "In 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ22​(∂2P~∂x2−∂P~∂x)\displaystyle\frac{\sigma^{2}}{2}\bigg(\frac{\partial^{2}\widetilde{P}}{\partial x^{2}}-\frac{\partial\widetilde{P}}{\partial x}\bigg) | ≥rP~−(r−δ)∂P~∂x−∫ℝ0(P~(⋅,⋅+z)−P~(⋅,⋅)−∂P~∂x(⋅,⋅)(ez−1))ν(dz)\displaystyle\geq r\widetilde{P}-(r-\delta)\frac{\partial\widetilde{P}}{\partial x}-\int\_{\mathbb{R}\_{0}}\!\bigg(\widetilde{P}(\cdot\,,\cdot+z)-\widetilde{P}(\cdot\,,\cdot)-\frac{\partial\widetilde{P}}{\partial x}(\cdot\,,\cdot)\big(e^{z}-1\big)\bigg)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =rP~−(r−δ)∂+P~∂x−∫ℝ0(P~(⋅,⋅+z)−P~(⋅,⋅)−∂+P~∂x(⋅,⋅)(ez−1))ν(dz)=:g~\displaystyle=r\widetilde{P}-(r-\delta)\frac{\partial\_{+}\widetilde{P}}{\partial x}-\int\_{\mathbb{R}\_{0}}\!\bigg(\widetilde{P}(\cdot\,,\cdot+z)-\widetilde{P}(\cdot\,,\cdot)-\frac{\partial\_{+}\widetilde{P}}{\partial x}(\cdot\,,\cdot)\big(e^{z}-1\big)\bigg)\nu(dz)=:\tilde{g} |  |

on 𝒞~={(t,x)∈(0,T)×ℝ:P~​(t,x)>(K−ex)+}={(t,x)∈(0,T)×ℝ:b​(t)<ex}\widetilde{\mathcal{C}}=\{(t,x)\in(0,T)\times\mathbb{R}:\widetilde{P}(t,x)>(K-e^{x})^{+}\}=\{(t,x)\in(0,T)\times\mathbb{R}:b(t)<e^{x}\} in the sense of distribution. Taking any φ~∈Cc∞​(𝒞~)\widetilde{\varphi}\in C\_{c}^{\infty}(\widetilde{\mathcal{C}}) and ψ∈Cc∞​((0,T))\psi\in C\_{c}^{\infty}((0,T)) and since φ~​ψ∈Cc∞​(𝒞~)\widetilde{\varphi}\psi\in C\_{c}^{\infty}(\widetilde{\mathcal{C}}), we have

|  |  |  |
| --- | --- | --- |
|  | σ22​∫𝒞~P~​(t,x)​(∂2∂x2+∂∂x)​φ~​(t,x)​ψ​(t)​𝑑x​𝑑t≥∫𝒞~g~​(t,x)​φ~​(t,x)​ψ​(t)​𝑑x​𝑑t.\displaystyle\frac{\sigma^{2}}{2}\int\_{\widetilde{\mathcal{C}}}\widetilde{P}(t,x)\bigg(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial}{\partial x}\bigg)\widetilde{\varphi}(t,x)\psi(t)\,dx\,dt\geq\int\_{\widetilde{\mathcal{C}}}\tilde{g}(t,x)\widetilde{\varphi}(t,x)\psi(t)\,dx\,dt. |  |

Since ψ\psi is arbitrary, for any t∈(0,T)t\in(0,T) with 𝒞~t:={x∈ℝ:(t,x)∈C~}\widetilde{\mathcal{C}}\_{t}:=\{x\in\mathbb{R}:(t,x)\in\widetilde{C}\}, we have

|  |  |  |
| --- | --- | --- |
|  | σ22​∫𝒞~tP~​(t,x)​(∂2∂x2+∂∂x)​φ~​(t,x)​𝑑x≥∫𝒞~tg~​(t,x)​φ~​(t,x)​𝑑x.\displaystyle\frac{\sigma^{2}}{2}\int\_{\widetilde{\mathcal{C}}\_{t}}\widetilde{P}(t,x)\bigg(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial}{\partial x}\bigg)\widetilde{\varphi}(t,x)\,dx\geq\int\_{\widetilde{\mathcal{C}}\_{t}}\tilde{g}(t,x)\widetilde{\varphi}(t,x)\,dx. |  |

Define gg and φ\varphi on 𝒞={(t,s)∈(0,T)×ℝ+:b​(t)<s}\mathcal{C}=\{(t,s)\in(0,T)\times\mathbb{R}\_{+}:b(t)<s\} respectively via g​(t,s)=g~​(t,ln⁡s)g(t,s)=\tilde{g}(t,\ln s) and φ​(t,s)=φ~​(t,ln⁡s)\varphi(t,s)=\widetilde{\varphi}(t,\ln s). Then by using change of variable s=exs=e^{x}, we deduce that

|  |  |  |
| --- | --- | --- |
|  | σ22​∫𝒞~tP~​(t,x)​(∂2∂x2+∂∂x)​φ~​(t,x)​𝑑x=σ22​∫𝒞~tP​(t,ex)​(∂2∂x2+∂∂x)​φ​(t,ex)​𝑑x\displaystyle\frac{\sigma^{2}}{2}\int\_{\widetilde{\mathcal{C}}\_{t}}\widetilde{P}(t,x)\bigg(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial}{\partial x}\bigg)\widetilde{\varphi}(t,x)\,dx=\frac{\sigma^{2}}{2}\int\_{\widetilde{\mathcal{C}}\_{t}}P(t,e^{x})\bigg(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial}{\partial x}\bigg)\varphi(t,e^{x})\,dx |  |
|  |  |  |
| --- | --- | --- |
|  | =σ22​∫𝒞~tP​(t,ex)​(e2​x​∂2φ∂s2​(t,ex)+2​ex​∂φ∂s​(t,ex))​𝑑x=σ22​∫𝒞tP​(t,s)​(s​∂2φ∂s2​(t,s)+2​∂φ∂s​(t,s))​𝑑s\displaystyle\quad=\frac{\sigma^{2}}{2}\!\int\_{\widetilde{\mathcal{C}}\_{t}}P(t,e^{x})\bigg(e^{2x}\frac{\partial^{2}\varphi}{\partial s^{2}}(t,e^{x})+2e^{x}\frac{\partial\varphi}{\partial s}(t,e^{x})\bigg)\,dx=\frac{\sigma^{2}}{2}\!\int\_{\mathcal{C}\_{t}}P(t,s)\bigg(s\frac{\partial^{2}\varphi}{\partial s^{2}}(t,s)+2\frac{\partial\varphi}{\partial s}(t,s)\bigg)\,ds |  |
|  |  |  |
| --- | --- | --- |
|  | =σ22​∫𝒞tP​(t,s)​∂2∂s2​(s​φ​(t,s))​𝑑s=σ22​∫𝒞ts​φ​(t,s)​∂2P∂s2​(t,d​s),\displaystyle\quad=\frac{\sigma^{2}}{2}\int\_{\mathcal{C}\_{t}}P(t,s)\frac{\partial^{2}}{\partial s^{2}}\big(s\varphi(t,s)\big)\,ds=\frac{\sigma^{2}}{2}\int\_{\mathcal{C}\_{t}}s\varphi(t,s)\frac{\partial^{2}P}{\partial s^{2}}(t,ds), |  |

where 𝒞t:={s∈ℝ+:(t,s)∈𝒞}\mathcal{C}\_{t}:=\{s\in\mathbb{R}\_{+}:(t,s)\in\mathcal{C}\}, and thus

|  |  |  |
| --- | --- | --- |
|  | σ22​∫𝒞ts​φ​(t,s)​∂2P∂s2​(t,d​s)≥∫𝒞t1s​g​(t,s)​φ​(t,s)​𝑑s.\displaystyle\frac{\sigma^{2}}{2}\int\_{\mathcal{C}\_{t}}s\varphi(t,s)\frac{\partial^{2}P}{\partial s^{2}}(t,ds)\geq\int\_{\mathcal{C}\_{t}}\frac{1}{s}g(t,s)\varphi(t,s)\,ds. |  |

Now for any fixed t∈(0,T)t\in(0,T) and s∈(b​(t),b​(T))s\in(b(t),b(T)), we can choose a nonnegative sequence (φn)n≥1⊂Cc∞​(𝒞)(\varphi\_{n})\_{n\geq 1}\subset C\_{c}^{\infty}(\mathcal{C}) such that φn​(t,u)↑𝟏[b​(t),s]​(u)​(u−b​(t))\varphi\_{n}(t,u)\uparrow{\bf 1}\_{[b(t),s]}(u)(u-b(t)) for all u∈𝒞tu\in\mathcal{C}\_{t}. It follows that

|  |  |  |
| --- | --- | --- |
|  | σ22​∫b​(t)su​(u−b​(t))​∂2P∂s2​(t,d​u)≥∫b​(t)su−b​(t)u​g​(t,u)​𝑑u,\displaystyle\frac{\sigma^{2}}{2}\int\_{b(t)}^{s}u(u-b(t))\frac{\partial^{2}P}{\partial s^{2}}(t,du)\geq\int\_{b(t)}^{s}\frac{u-b(t)}{u}g(t,u)\,du, |  |

which implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫b​(t)s(u−b​(t))​∂2P∂s2​(t,d​u)≥2σ2​b2​(T)​∫b​(t)s(u−b​(t))​g​(t,u)​𝑑u.\displaystyle\int\_{b(t)}^{s}(u-b(t))\frac{\partial^{2}P}{\partial s^{2}}(t,du)\geq\frac{2}{\sigma^{2}b^{2}(T)}\int\_{b(t)}^{s}(u-b(t))g(t,u)\,du. |  | (B.25) |

To estimate the function gg from below, we need to establish the following technical lemma. Denote the early exercise premium by e​(T−t,s):=P​(t,s)−Pe​(t,s)e(T-t,s):=P(t,s)-P\_{e}(t,s), and set θ=T−t\theta=T-t as usual.

###### Lemma B.1.

Under the model assumptions, for any s∈(0,b​(T))s\in(0,b(T)), we have

|  |  |  |
| --- | --- | --- |
|  | (a)​|∂+e∂s​(θ,s)|=o​(θ),(b)​∂+P∂s​(t,s)+1=o​(θ),\displaystyle\text{(a)}\,\,\,\left|\frac{\partial\_{+}e}{\partial s}(\theta,s)\right|=o(\sqrt{\theta}),\qquad\text{(b)}\,\,\,\frac{\partial\_{+}P}{\partial s}(t,s)+1=o(\sqrt{\theta}), |  |

as θ=T−t→0+\theta=T-t\rightarrow 0^{+}, with o​(θ)o(\sqrt{\theta}) uniform with respect to ss.

Proof. Clearly, for any s∈(0,b​(t))s\in(0,b(t)) we have (∂+P/∂s)​(t,s)+1=0(\partial\_{+}P/\partial s)(t,s)+1=0, so it suffices to consider s∈(b​(t),b​(T))s\in(b(t),b(T)). In view of [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Corollary 3.1], the function s↦P​(t,s)−Pe​(t,s)s\mapsto P(t,s)-P\_{e}(t,s) is nonincreasing on ℝ+\mathbb{R}\_{+}. Moreover, the convexity of P​(t,⋅)P(t,\cdot) ensures that the function s↦P​(t,s)−(K−s)s\mapsto P(t,s)-(K-s) is nondecreasing. It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤∂+P∂s​(t,s)+1≤∂+Pe∂s​(t,s)+1.\displaystyle 0\leq\frac{\partial\_{+}P}{\partial s}(t,s)+1\leq\frac{\partial\_{+}P\_{e}}{\partial s}(t,s)+1. |  | (B.26) |

Let Z~t:=X~t−σ​Wt\widetilde{Z}\_{t}:=\widetilde{X}\_{t}-\sigma W\_{t}, t∈ℝ+t\in\mathbb{R}\_{+}. For any s∈(b​(t),b​(T))s\in(b(t),b(T)), noting that b​(T)<Kb(T)<K when d<0d<0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1+∂+Pe∂s​(t,s)\displaystyle 1+\frac{\partial\_{+}P\_{e}}{\partial s}(t,s) | =1−e−r​θ​𝔼​(eX~θ​𝟏{X~θ<ln⁡(K/s)})=1−𝔼​(eσ​Wθ​𝟏{X~θ<ln⁡(K/s)})+o​(θ)\displaystyle=1-e^{-r\theta}\,\mathbb{E}\Big(e^{\widetilde{X}\_{\theta}}{\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/s)\}}\Big)=1-\mathbb{E}\Big(e^{\sigma W\_{\theta}}{\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/s)\}}\Big)+o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​((1−eσ​Wθ)​𝟏{X~θ<ln⁡(K/s)})+ℙ​(X~θ≥ln⁡(K/b​(T)))+o​(θ)\displaystyle\leq\mathbb{E}\Big(\big(1-e^{\sigma W\_{\theta}}\big){\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/s)\}}\Big)+\mathbb{P}\big(\widetilde{X}\_{\theta}\geq\ln(K/b(T))\big)+o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(1−eσ​Wθ)−𝔼​((1−eσ​Wθ)​𝟏{X~θ≥ln⁡(K/s)})+o​(θ)\displaystyle=\mathbb{E}\big(1-e^{\sigma W\_{\theta}}\big)-\mathbb{E}\Big(\big(1-e^{\sigma W\_{\theta}}\big){\bf 1}\_{\{\widetilde{X}\_{\theta}\geq\ln(K/s)\}}\Big)+o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​(|1−eσ​Wθ|​𝟏{σ​Wθ≥ln⁡(K/b​(T))/2}​𝟏{Z~θ≥ln⁡(K/b​(T))/2})+o​(θ),θ→0+.\displaystyle\leq\mathbb{E}\Big(\big|1-e^{\sigma W\_{\theta}}\big|{\bf 1}\_{\{\sigma W\_{\theta}\geq\ln(K/b(T))/2\}}{\bf 1}\_{\{\widetilde{Z}\_{\theta}\geq\ln(K/b(T))/2\}}\Big)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}. |  |

Using arguments similar to those leading to ([5.11](https://arxiv.org/html/2512.17791v1#S5.E11 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) together with the independence between (Wt)t∈ℝ+(W\_{t})\_{t\in\mathbb{R}\_{+}} and (Z~t)t∈ℝ+(\widetilde{Z}\_{t})\_{t\in\mathbb{R}\_{+}}, we deduce that, as θ→0+\theta\rightarrow 0^{+},

|  |  |  |
| --- | --- | --- |
|  | 1+∂+Pe∂s​(t,s)≤𝔼​(|1−eσ​Wθ|​𝟏{σ​Wθ≥ln⁡(K/b​(T))/2})​ℙ​(Z~θ≥ln⁡(K/b​(T))2)+o​(θ)=o​(θ),\displaystyle 1+\frac{\partial\_{+}P\_{e}}{\partial s}(t,s)\leq\mathbb{E}\Big(\big|1-e^{\sigma W\_{\theta}}\big|{\bf 1}\_{\{\sigma W\_{\theta}\geq\ln(K/b(T))/2\}}\Big)\mathbb{P}\bigg(\widetilde{Z}\_{\theta}\geq\frac{\ln(K/b(T))}{2}\bigg)+o(\sqrt{\theta})=o(\sqrt{\theta}), |  |

which, together with ([B.26](https://arxiv.org/html/2512.17791v1#A2.E26 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and the definition of early exercise premium, completes the proof. □\Box

Coming back to the proof of Lemma [5.5](https://arxiv.org/html/2512.17791v1#S5.Thmtheorem5 "Lemma 5.5. ‣ 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), for any fixed t∈(0,T)t\in(0,T) and s∈(b​(t),be​(t)∧b​(T))s\in(b(t),b\_{e}(t)\wedge b(T)), we will estimate g​(t,u)g(t,u) from below for u∈[b​(t),s]u\in[b(t),s]. To begin with, we first have

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,u)\displaystyle g(t,u) | =r​P​(t,u)−(r−δ)​u​∂+P∂s​(t,u)−∫ℝ0(P​(t,u​ez)−P​(t,u)−u​(ez−1)​∂+P∂s​(t,u))​ν​(d​z)\displaystyle=rP(t,u)-(r-\delta)u\frac{\partial\_{+}P}{\partial s}(t,u)-\int\_{\mathbb{R}\_{0}}\bigg(P(t,ue^{z})-P(t,u)-u\big(e^{z}-1\big)\frac{\partial\_{+}P}{\partial s}(t,u)\bigg)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥r​(K−u)+(r−δ)​u−∫ℝ0(P​(t,u​ez)−P​(t,u)+u​(ez−1))​ν​(d​z)\displaystyle\geq r(K-u)+(r-\delta)u-\int\_{\mathbb{R}\_{0}}\left(P(t,ue^{z})-P(t,u)+u\big(e^{z}-1\big)\right)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −u​(∂+P∂s​(t,u)+1)​((r−δ)−∫ℝ0(ez−1)​ν​(d​z)),\displaystyle\quad-u\bigg(\frac{\partial\_{+}P}{\partial s}(t,u)+1\bigg)\bigg((r-\delta)-\int\_{\mathbb{R}\_{0}}\big(e^{z}-1\big)\nu(dz)\bigg), |  |

where both integrals on the right-hand side of the second inequality are finite due to ([3.2](https://arxiv.org/html/2512.17791v1#S3.E2 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")). Thanks to ([3.2](https://arxiv.org/html/2512.17791v1#S3.E2 "In 3.2. Finite Variation Case ‣ 3. The Known Cases of the Convergence Rate of the Critical Price ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and Lemma [B.1](https://arxiv.org/html/2512.17791v1#A2.Thmtheorem1 "Lemma B.1. ‣ Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")-(a), we see that, as θ=T−t→0+\theta=T-t\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝ0(P​(t,u​ez)−P​(t,u)−Pe​(t,u​ez)+P​(t,u))​ν​(d​z)=∫ℝ0(e​(θ,u​ez)−e​(θ,u))​ν​(d​z)=o​(θ).\displaystyle\int\_{\mathbb{R}\_{0}}\!\big(P(t,ue^{z})\!-\!P(t,u)\!-\!P\_{e}(t,ue^{z})\!+\!P(t,u)\big)\nu(dz)=\!\int\_{\mathbb{R}\_{0}}\!\big(e(\theta,ue^{z})\!-\!e(\theta,u)\big)\nu(dz)=o(\sqrt{\theta}).\qquad |  | (B.27) |

Together with Lemma [B.1](https://arxiv.org/html/2512.17791v1#A2.Thmtheorem1 "Lemma B.1. ‣ Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")-(b), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,u)≥r​K−δ​s−∫ℝ0(Pe​(t,u​ez)−Pe​(t,u)+u​(ez−1))​ν​(d​z)+o​(θ),θ→0+.\displaystyle g(t,u)\geq rK-\delta s-\int\_{\mathbb{R}\_{0}}\left(P\_{e}(t,ue^{z})-P\_{e}(t,u)+u\big(e^{z}-1\big)\right)\nu(dz)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}. |  | (B.28) |

In view of ([2.2](https://arxiv.org/html/2512.17791v1#S2.E2 "In 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and the martingale property of (eXt)t∈ℝ+=(e−(r−δ)​t+X~t)t∈ℝ+(e^{X\_{t}})\_{t\in\mathbb{R}\_{+}}=(e^{-(r-\delta)t+\widetilde{X}\_{t}})\_{t\in\mathbb{R}\_{+}},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫ℝ0(Pe​(t,u​ez)−Pe​(t,u)+u​(ez−1))​ν​(d​z)\displaystyle\int\_{\mathbb{R}\_{0}}\left(P\_{e}(t,ue^{z})-P\_{e}(t,u)+u\big(e^{z}-1\big)\right)\nu(dz) |  | (B.29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−r​θ​∫ℝ0𝔼​((K−u​ez​eX~θ)+−(K−u​eX~θ)++u​eδ​θ​(ez−1)​eX~θ)​ν​(d​z)\displaystyle\quad=e^{-r\theta}\int\_{\mathbb{R}\_{0}}\mathbb{E}\Big(\big(K-ue^{z}e^{\widetilde{X}\_{\theta}}\big)^{+}-\big(K-ue^{\widetilde{X}\_{\theta}}\big)^{+}+ue^{\delta\theta}\big(e^{z}-1\big)e^{\widetilde{X}\_{\theta}}\Big)\nu(dz) |  | (B.30) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫ℝ0𝔼​((K−u​ez​eX~θ)+−(K−u​eX~θ)++u​(ez−1)​eX~θ)​ν​(d​z)+O​(θ),θ→0+,\displaystyle\quad=\int\_{\mathbb{R}\_{0}}\mathbb{E}\Big(\big(K-ue^{z}e^{\widetilde{X}\_{\theta}}\big)^{+}-\big(K-ue^{\widetilde{X}\_{\theta}}\big)^{+}+u\big(e^{z}-1\big)e^{\widetilde{X}\_{\theta}}\Big)\nu(dz)+O(\theta),\quad\theta\rightarrow 0^{+}, |  | (B.31) |

we thus deduce that, for u∈[b​(t),s]u\in[b(t),s] where s∈(b​(t),be​(t)∧b​(T))s\in(b(t),b\_{e}(t)\wedge b(T)) and t∈(0,T)t\in(0,T),

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,u)≥r​K−δ​s−∫ℝ0𝔼​((K−u​ez​eX~θ)+−(K−u​eX~θ)++u​(ez−1)​eX~θ)​ν​(d​z)+o​(θ),θ→0+.\displaystyle g(t,u)\!\geq\!rK\!-\!\delta s\!-\!\!\int\_{\mathbb{R}\_{0}}\!\!\mathbb{E}\Big(\!\big(K\!-\!ue^{z}e^{\widetilde{X}\_{\theta}}\big)^{+}\!\!\!-\!\big(K\!-\!ue^{\widetilde{X}\_{\theta}}\big)^{+}\!\!\!+\!u\big(e^{z}\!-\!1\big)e^{\widetilde{X}\_{\theta}}\Big)\nu(dz)\!+\!o(\sqrt{\theta}),\,\,\,\,\theta\rightarrow 0^{+}.\qquad |  | (B.32) |

We will estimate the integral term above over various subsets of ℝ0\mathbb{R}\_{0}. For this purpose, we set

|  |  |  |
| --- | --- | --- |
|  | I​(A):=∫A𝔼​((K−u​ez​eX~θ)+−(K−u​eX~θ)++u​(ez−1)​eX~θ)​ν​(d​z),A∈ℬ​(ℝ0).\displaystyle I(A):=\int\_{A}\mathbb{E}\Big(\big(K-ue^{z}e^{\widetilde{X}\_{\theta}}\big)^{+}-\big(K-ue^{\widetilde{X}\_{\theta}}\big)^{+}+u\big(e^{z}-1\big)e^{\widetilde{X}\_{\theta}}\Big)\nu(dz),\quad A\in\mathcal{B}(\mathbb{R}\_{0}). |  |

First, for A1=(−∞,0)A\_{1}=(-\infty,0), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(A1)=∫A1𝔼​((K−u​eX~θ)​𝟏{z+X~θ<ln⁡(K/u)≤X~θ}+u​(ez−1)​eX~θ​𝟏{X~θ≥ln⁡(K/u)−z})​ν​(d​z)≤0.\displaystyle I(A\_{1})=\int\_{A\_{1}}\mathbb{E}\Big(\big(K-ue^{\widetilde{X}\_{\theta}}\big){\bf 1}\_{\{z+\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}\}}+u\big(e^{z}-1\big)e^{\widetilde{X}\_{\theta}}{\bf 1}\_{\{\widetilde{X}\_{\theta}\geq\ln(K/u)-z\}}\Big)\nu(dz)\leq 0.\qquad |  | (B.33) |

Next, for A2=(0,ln⁡(K/b​(T))/2)A\_{2}=(0,\ln(K/b(T))/2), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(A2)\displaystyle I(A\_{2}) | =∫A2𝔼​((u​ez​eX~θ−K)​𝟏{X~θ<ln⁡(K/u)≤X~θ+z}+u​(ez−1)​eX~θ​𝟏{X~θ≥ln⁡(K/u)})​ν​(d​z)\displaystyle=\int\_{A\_{2}}\mathbb{E}\Big(\big(ue^{z}e^{\widetilde{X}\_{\theta}}-K\big){\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}+z\}}+u\big(e^{z}-1\big)e^{\widetilde{X}\_{\theta}}{\bf 1}\_{\{\widetilde{X}\_{\theta}\geq\ln(K/u)\}}\Big)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫A2𝔼​((u​ez​eX~θ−u​eX~θ)​𝟏{X~θ<ln⁡(K/u)≤X~θ+z}+u​(ez−1)​eX~θ​𝟏{X~θ≥ln⁡(K/u)})​ν​(d​z)\displaystyle\leq\int\_{A\_{2}}\mathbb{E}\Big(\big(ue^{z}e^{\widetilde{X}\_{\theta}}-ue^{\widetilde{X}\_{\theta}}\big){\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}+z\}}+u\big(e^{z}-1\big)e^{\widetilde{X}\_{\theta}}{\bf 1}\_{\{\widetilde{X}\_{\theta}\geq\ln(K/u)\}}\Big)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​∫A2(ez−1)​ν​(d​z)⋅2​𝔼​(eX~θ​𝟏{X~θ≥ln⁡(K/b​(T))/2}).\displaystyle\leq K\int\_{A\_{2}}(e^{z}-1)\nu(dz)\cdot 2\mathbb{E}\Big(e^{\widetilde{X}\_{\theta}}{\bf 1}\_{\{\widetilde{X}\_{\theta}\geq\ln(K/b(T))/2\}}\Big). |  |

Using an argument similar to those leading to ([5.11](https://arxiv.org/html/2512.17791v1#S5.E11 "In 5. New Results on the Rate of Convergence of the Critical Price when 𝑑<0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) together with Hölder’s inequality, we deduce that, for some p∈(1,2)p\in(1,2) and q>2q>2 with p−1+q−1=1p^{-1}+q^{-1}=1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(A2)≤2​K​∫A2(ez−1)​ν​(d​z)⋅(𝔼​(eq​X~θ))1/q​(ℙ​(X~θ≥ln⁡(K/b​(T))/2))1/p=o​(θ),θ→0+.\displaystyle I(A\_{2})\leq 2K\!\int\_{A\_{2}}\!(e^{z}-1)\nu(dz)\!\cdot\!\left(\mathbb{E}\big(e^{q\widetilde{X}\_{\theta}}\big)\right)^{1/q}\!\left(\mathbb{P}\big(\widetilde{X}\_{\theta}\geq\ln(K/b(T))/2\big)\right)^{1/p}\!\!=o(\sqrt{\theta}),\,\,\,\,\theta\rightarrow 0^{+}.\qquad\, |  | (B.34) |

Finally, for A3=[ln⁡(K/b​(T))/2,ln⁡(K/b​(T)))A\_{3}=[\ln(K/b(T))/2,\ln(K/b(T))), by a similar argument leading to ([B.34](https://arxiv.org/html/2512.17791v1#A2.E34 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) we first have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(A3)\displaystyle I(A\_{3}) | =∫A3𝔼​((u​ez​eX~θ−K)​𝟏{X~θ<ln⁡(K/u)≤X~θ+z}+u​(ez−1)​eX~θ​𝟏{X~θ≥ln⁡(K/u)})​ν​(d​z)\displaystyle=\int\_{A\_{3}}\mathbb{E}\Big(\big(ue^{z}e^{\widetilde{X}\_{\theta}}-K\big){\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}+z\}}+u\big(e^{z}-1\big)e^{\widetilde{X}\_{\theta}}{\bf 1}\_{\{\widetilde{X}\_{\theta}\geq\ln(K/u)\}}\Big)\nu(dz) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫A3𝔼​((u​ez​eX~θ−u​ez)​𝟏{X~θ<ln⁡(K/u)≤X~θ+z})​ν​(d​z)+o​(θ)\displaystyle\leq\int\_{A\_{3}}\mathbb{E}\Big(\big(ue^{z}e^{\widetilde{X}\_{\theta}}-ue^{z}\big){\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}+z\}}\Big)\,\nu(dz)+o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​∫A3ez​𝔼​((eX~θ−1)​𝟏{X~θ<ln⁡(K/u)≤X~θ+z})​ν​(d​z)+o​(θ),θ→0+.\displaystyle\leq K\int\_{A\_{3}}e^{z}\,\mathbb{E}\Big(\big(e^{\widetilde{X}\_{\theta}}-1\big){\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}+z\}}\Big)\,\nu(dz)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}. |  |

Using the independence between (Wt)t∈ℝ+(W\_{t})\_{t\in\mathbb{R}\_{+}} and (Z~t)t∈ℝ+(\widetilde{Z}\_{t})\_{t\in\mathbb{R}\_{+}}, we see that

|  |  |  |
| --- | --- | --- |
|  | |𝔼​((eX~θ−eσ​Wθ)​𝟏{X~θ<ln⁡(K/u)≤X~θ+z})|≤𝔼​(eσ​Wθ)​𝔼​(|eZ~θ−1|)=O​(θ),θ→0+.\displaystyle\left|\mathbb{E}\Big(\big(e^{\widetilde{X}\_{\theta}}-e^{\sigma W\_{\theta}}\big){\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}+z\}}\Big)\right|\leq\mathbb{E}\big(e^{\sigma W\_{\theta}}\big)\mathbb{E}\left(\big|e^{\widetilde{Z}\_{\theta}}-1\big|\right)=O(\theta),\quad\theta\rightarrow 0^{+}. |  |

Hence, we deduce that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(A3)\displaystyle I(A\_{3}) | ≤K​∫A3ez​𝔼​(|eσ​Wθ−1|​𝟏{X~θ<ln⁡(K/u)≤X~θ+z})​ν​(d​z)+o​(θ)\displaystyle\leq K\int\_{A\_{3}}e^{z}\,\mathbb{E}\Big(\big|e^{\sigma W\_{\theta}}-1\big|{\bf 1}\_{\{\widetilde{X}\_{\theta}<\ln(K/u)\leq\widetilde{X}\_{\theta}+z\}}\Big)\,\nu(dz)+o(\sqrt{\theta}) |  | (B.35) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤σ​K​θ​∫A3ez​𝔼​(|W1|​𝟏{W1≥(ln⁡(K/b​(T))−z−Z~θ)/θ})​ν​(d​z)+o​(θ)\displaystyle\leq\sigma K\sqrt{\theta}\int\_{A\_{3}}e^{z}\,\mathbb{E}\Big(|W\_{1}|{\bf 1}\_{\{W\_{1}\geq(\ln(K/b(T))-z-\widetilde{Z}\_{\theta})/\sqrt{\theta}\}}\Big)\,\nu(dz)+o(\sqrt{\theta}) |  | (B.36) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤σ​K​θ​∫A3ez​(ℙ​(W1≥(ln⁡(K/b​(T))−z−Z~θ)/θ))1/2​ν​(d​z)+o​(θ)=o​(θ),θ→0+.\displaystyle\leq\sigma K\sqrt{\theta}\!\int\_{A\_{3}}\!\!e^{z}\!\Big(\mathbb{P}\big(W\_{1}\!\geq\!(\ln(K/b(T))\!-\!z\!-\!\widetilde{Z}\_{\theta})/\sqrt{\theta}\big)\Big)^{1/2}\!\!\nu(dz)\!+\!o(\sqrt{\theta})\!=\!o(\sqrt{\theta}),\,\,\,\theta\rightarrow 0^{+}.\qquad\, |  | (B.37) |

Combining ([B.32](https://arxiv.org/html/2512.17791v1#A2.E32 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.33](https://arxiv.org/html/2512.17791v1#A2.E33 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.34](https://arxiv.org/html/2512.17791v1#A2.E34 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.37](https://arxiv.org/html/2512.17791v1#A2.E37 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that, as θ→0+\theta\rightarrow 0^{+},

|  |  |  |
| --- | --- | --- |
|  | g​(t,u)≥r​K−δ​s−∫[ln⁡(K/b​(T)),∞)𝔼​((K−u​ez​eX~θ)+−(K−u​eX~θ)++u​(ez−1)​eX~θ)​ν​(d​z)+o​(θ).\displaystyle g(t,u)\geq rK-\delta s-\int\_{[\ln(K/b(T)),\infty)}\mathbb{E}\Big(\!\big(K\!-\!ue^{z}e^{\widetilde{X}\_{\theta}}\big)^{+}\!\!\!-\!\big(K\!-\!ue^{\widetilde{X}\_{\theta}}\big)^{+}\!\!\!+\!u\big(e^{z}\!-\!1\big)e^{\widetilde{X}\_{\theta}}\Big)\nu(dz)+o(\sqrt{\theta}). |  |

Moreover, by ([B.27](https://arxiv.org/html/2512.17791v1#A2.E27 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.28](https://arxiv.org/html/2512.17791v1#A2.E28 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.31](https://arxiv.org/html/2512.17791v1#A2.E31 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) (with ℝ0\mathbb{R}\_{0} replaced by [ln⁡(K/b​(T)),∞)[\ln(K/b(T)),\infty)), and noting that P​(t,u)>(K−u)P(t,u)>(K-u) for u>b​(t)u>b(t), we have, for any u∈[b​(t),s]u\in[b(t),s], s∈(b​(t),be​(t)∧b​(T))s\in(b(t),b\_{e}(t)\wedge b(T)), and t∈(0,T)t\in(0,T),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(t,u)\displaystyle g(t,u) | ≥r​K−δ​s−∫[ln⁡(K/b​(T)),∞)(P​(t,u​ez)−P​(t,u)+u​(ez−1))​ν​(d​z)+o​(θ)\displaystyle\geq rK-\delta s-\int\_{[\ln(K/b(T)),\infty)}\left(P(t,ue^{z})-P(t,u)+u\big(e^{z}-1\big)\right)\nu(dz)+o(\sqrt{\theta}) |  | (B.38) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥r​K−δ​s−∫[ln⁡(K/b​(T)),∞)(P​(t,u​ez)−(K−u​ez))​ν​(d​z)+o​(θ),θ→0+.\displaystyle\geq rK-\delta s-\int\_{[\ln(K/b(T)),\infty)}\left(P(t,ue^{z})-\big(K-ue^{z}\big)\right)\nu(dz)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}. |  | (B.39) |

We are left to estimate the integral term above.

In view of the early exercise premium formula (cf. [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Theorem 3.2]), we have that

|  |  |  |
| --- | --- | --- |
|  | e​(θ,s)=𝔼​(∫0θe−r​u​Ψ​(t+u,s​eX~u)​𝑑u),\displaystyle e(\theta,s)=\mathbb{E}\bigg(\int\_{0}^{\theta}e^{-ru}\,\Psi\big(t+u,se^{\widetilde{X}\_{u}}\big)du\bigg), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Ψ​(t,s)=(r​K−δ​s−∫(0,∞)(P​(t,s​ez)−(K−s​ez))​ν​(d​z))​𝟏{s<b​(t)},(t,s)∈[0,T)×ℝ+.\displaystyle\Psi(t,s)=\bigg(rK-\delta s-\int\_{(0,\infty)}\big(P(t,se^{z})-(K-se^{z})\big)\nu(dz)\bigg){\bf 1}\_{\{s<b(t)\}},\quad(t,s)\in[0,T)\times\mathbb{R}\_{+}. |  |

By Theorem [4.8](https://arxiv.org/html/2512.17791v1#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.2. Step 2: The difference between European and American critical prices ‣ 4. New Results on the Convergence Rate of the Critical Price when 𝑑>0 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models"), the distribution (∂/∂t+𝒜~−r)​P~(\partial/\partial t+\widetilde{\mathscr{A}}-r)\widetilde{P} is a nonpositive measure on (0,T)×ℝ(0,T)\times\mathbb{R}. On the other hand, by [[7](https://arxiv.org/html/2512.17791v1#bib.bib7), Proposition 3.1],

|  |  |  |
| --- | --- | --- |
|  | (∂∂t+𝒜~−r)​P~​(t,x)=−Ψ​(t,ex)d​t​d​x​-a.e.​on ​(0,T)×ℝ.\displaystyle\bigg(\frac{\partial}{\partial t}+\widetilde{\mathscr{A}}-r\bigg)\widetilde{P}(t,x)=-\Psi(t,e^{x})\quad dt\,dx\text{-a.e.}\,\,\text{on }(0,T)\times\mathbb{R}. |  |

Since Ψ\Psi is continuous on [0,T)×ℝ+[0,T)\times\mathbb{R}\_{+}, we deduce that Ψ\Psi is nonnegative on [0,T)×ℝ+[0,T)\times\mathbb{R}\_{+}. Noting that the integral term in Ψ\Psi is nonnegative, we obtain that 0≤Ψ​(t,s)≤r​K0\leq\Psi(t,s)\leq rK for any (t,s)∈[0,T)×ℝ+(t,s)\in[0,T)\times\mathbb{R}\_{+}. It follows that e​(θ,s)=O​(θ)e(\theta,s)=O(\theta) as θ→0+\theta\rightarrow 0^{+}, and hence we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫[ln⁡(K/b​(T)),∞)P​(t,u​ez)​ν​(d​z)=∫[ln⁡(K/b​(T)),∞)Pe​(t,u​ez)​ν​(d​z)+o​(θ)\displaystyle\int\_{[\ln(K/b(T)),\infty)}P(t,ue^{z})\,\nu(dz)=\int\_{[\ln(K/b(T)),\infty)}P\_{e}(t,ue^{z})\,\nu(dz)+o(\sqrt{\theta}) |  | (B.40) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫[ln⁡(K/b​(T)),∞)𝔼​((K−s​ez+X~θ)+)​ν​(d​z)+o​(θ)\displaystyle\quad=\int\_{[\ln(K/b(T)),\infty)}\mathbb{E}\left(\big(K-s\,e^{z+\widetilde{X}\_{\theta}}\big)^{+}\right)\nu(dz)+o(\sqrt{\theta}) |  | (B.41) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫[ln⁡(K/b​(T)),∞)𝔼​((K−s​ez+σ​Wθ)+)​ν​(d​z)+o​(θ)\displaystyle\quad=\int\_{[\ln(K/b(T)),\infty)}\mathbb{E}\left(\big(K-s\,e^{z+\sigma W\_{\theta}}\big)^{+}\right)\nu(dz)+o(\sqrt{\theta}) |  | (B.42) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫[ln⁡(K/b​(T)),∞)𝔼​((K−s​ez​(1+σ​Wθ))+)​ν​(d​z)+o​(θ),θ→0+.\displaystyle\quad=\int\_{[\ln(K/b(T)),\infty)}\mathbb{E}\left(\big(K-se^{z}(1+\sigma W\_{\theta})\big)^{+}\right)\nu(dz)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}. |  | (B.43) |

On the set (ln⁡(K/b​(T)),∞)(\ln(K/b(T)),\infty), we have b​(T)​ez>Kb(T)e^{z}>K, and so

|  |  |  |
| --- | --- | --- |
|  | ∫(ln⁡(K/b​(T)),∞)𝔼​((K−s​ez​(1+σ​Wθ))+)​ν​(d​z)\displaystyle\int\_{(\ln(K/b(T)),\infty)}\mathbb{E}\left(\big(K-se^{z}(1+\sigma W\_{\theta})\big)^{+}\right)\nu(dz) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫(ln⁡(K/b​(T)),∞)𝔼((b(T)ez−sez−sezσθW1)𝟏{s​ez​σ​θ​W1<(K−s​ez)}))ν(dz)\displaystyle\quad\leq\int\_{(\ln(K/b(T)),\infty)}\mathbb{E}\left(\big(b(T)e^{z}-se^{z}-se^{z}\sigma\sqrt{\theta}W\_{1}\big){\bf 1}\_{\{se^{z}\sigma\sqrt{\theta}W\_{1}<(K-se^{z})\}}\big)\right)\nu(dz) |  |
|  |  |  |
| --- | --- | --- |
|  | =(b​(T)−s)​∫(ln⁡(K/b​(T)),∞)ez​ℙ​(W1<K​e−z​s−1−1σ​θ)​ν​(d​z)\displaystyle\quad=(b(T)-s)\int\_{(\ln(K/b(T)),\infty)}e^{z}\,\mathbb{P}\bigg(W\_{1}<\frac{Ke^{-z}s^{-1}-1}{\sigma\sqrt{\theta}}\bigg)\nu(dz) |  |
|  |  |  |
| --- | --- | --- |
|  | −θ​σ​s​∫(ln⁡(K/b​(T)),∞)ez​𝔼​(W1​𝟏{W1<(K​e−z​s−1−1)/(σ​θ)})​ν​(d​z).\displaystyle\qquad-\sqrt{\theta}\sigma s\int\_{(\ln(K/b(T)),\infty)}e^{z}\,\mathbb{E}\Big(W\_{1}{\bf 1}\_{\{W\_{1}<(Ke^{-z}s^{-1}-1)/(\sigma\sqrt{\theta})\}}\Big)\nu(dz). |  |

Since s>b​(t)s>b(t), for all z>ln⁡(K/b​(T))z>\ln(K/b(T)) we have K​e−z/s−1<K​e−z/b​(t)−1≤0Ke^{-z}/s-1<Ke^{-z}/b(t)-1\leq 0, which implies that

|  |  |  |
| --- | --- | --- |
|  | limθ→0+ℙ​(W1<K​e−z​s−1−1σ​θ)=0,limθ→0+𝔼​(|W1|​𝟏{W1<(K​e−z​s−1−1)/(σ​θ)})=0.\displaystyle\lim\_{\theta\rightarrow 0^{+}}\mathbb{P}\bigg(W\_{1}<\frac{Ke^{-z}s^{-1}-1}{\sigma\sqrt{\theta}}\bigg)=0,\quad\lim\_{\theta\rightarrow 0^{+}}\mathbb{E}\Big(|W\_{1}|{\bf 1}\_{\{W\_{1}<(Ke^{-z}s^{-1}-1)/(\sigma\sqrt{\theta})\}}\Big)=0. |  |

Therefore, by dominated convergence we obtain that, as θ→0+\theta\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε​(θ):=∫(ln⁡(K/b​(T)),∞)ez​ℙ​(W1<K​e−z​s−1−1σ​θ)​ν​(d​z)\displaystyle\varepsilon(\theta):=\int\_{(\ln(K/b(T)),\infty)}e^{z}\,\mathbb{P}\bigg(W\_{1}<\frac{Ke^{-z}s^{-1}-1}{\sigma\sqrt{\theta}}\bigg)\nu(dz) | →0,\displaystyle\rightarrow 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​σ​s​∫(ln⁡(K/b​(T)),∞)ez​𝔼​(W1​𝟏{W1<(K​e−z​s−1−1)/(σ​θ)})​ν​(d​z)\displaystyle\sqrt{\theta}\sigma s\int\_{(\ln(K/b(T)),\infty)}e^{z}\,\mathbb{E}\Big(W\_{1}{\bf 1}\_{\{W\_{1}<(Ke^{-z}s^{-1}-1)/(\sigma\sqrt{\theta})\}}\Big)\nu(dz) | =o​(θ).\displaystyle=o(\sqrt{\theta}). |  |

Consequently, we deduce that, with ε​(θ)→0\varepsilon(\theta)\rightarrow 0 as θ→0+\theta\rightarrow 0^{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(ln⁡(K/b​(T)),∞)𝔼​((K−s​ez​(1+σ​Wθ))+)​ν​(d​z)≤(b​(T)−s)​ε​(θ)+o​(θ),θ→0+.\displaystyle\int\_{(\ln(K/b(T)),\infty)}\mathbb{E}\left(\big(K-se^{z}(1+\sigma W\_{\theta})\big)^{+}\right)\nu(dz)\leq(b(T)-s)\varepsilon(\theta)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}. |  | (B.44) |

Moreover, on the singleton {ln⁡(K/b​(T))}\{\ln(K/b(T))\}, since s<b​(T)s<b(T), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫{ln⁡(K/b​(T))}𝔼​((K−s​ez​(1+σ​Wθ))+)​ν​(d​z)\displaystyle\int\_{\{\ln(K/b(T))\}}\mathbb{E}\left(\big(K-se^{z}(1+\sigma W\_{\theta})\big)^{+}\right)\nu(dz) |  | (B.45) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫{ln⁡(K/b​(T))}(K−s​ez)​ν​(d​z)+∫{ln⁡(K/b​(T))}𝔼​((s​ez​σ​Wθ−(K−s​ez))+)​ν​(d​z)\displaystyle\quad=\int\_{\{\ln(K/b(T))\}}\big(K-se^{z}\big)\nu(dz)+\int\_{\{\ln(K/b(T))\}}\mathbb{E}\left(\big(se^{z}\sigma W\_{\theta}-(K-se^{z})\big)^{+}\right)\nu(dz) |  | (B.46) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫{ln⁡(K/b​(T))}(K−s​ez)​ν​(d​z)+s​Kb​(T)​ν​({ln⁡(K/b​(T))})​𝔼​((σ​Wθ−(s−1​b​(T)−1))+)\displaystyle\quad=\int\_{\{\ln(K/b(T))\}}\big(K-se^{z}\big)\nu(dz)+\frac{sK}{b(T)}\nu(\{\ln(K/b(T))\})\,\mathbb{E}\Big(\big(\sigma W\_{\theta}-(s^{-1}b(T)-1)\big)^{+}\Big) |  | (B.47) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤∫{ln⁡(K/b​(T))}(K−s​ez)​ν​(d​z)+K​ν​({ln⁡(K/b​(T))})​𝔼​((σ​Wθ−ln⁡(b​(T)/s))+).\displaystyle\quad\leq\int\_{\{\ln(K/b(T))\}}\big(K-se^{z}\big)\nu(dz)+K\nu(\{\ln(K/b(T))\})\,\mathbb{E}\Big(\big(\sigma W\_{\theta}-\ln(b(T)/s)\big)^{+}\Big). |  | (B.48) |

Combining ([B.43](https://arxiv.org/html/2512.17791v1#A2.E43 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), ([B.44](https://arxiv.org/html/2512.17791v1#A2.E44 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and ([B.48](https://arxiv.org/html/2512.17791v1#A2.E48 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that, as θ→0+\theta\rightarrow 0^{+},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∫[ln⁡(K/b​(T)),∞)P​(t,u​ez)​ν​(d​z)\displaystyle\int\_{[\ln(K/b(T)),\infty)}P(t,ue^{z})\,\nu(dz) | ≤(b​(T)−s)​ε​(θ)+∫{ln⁡(K/b​(T))}(K−s​ez)​ν​(d​z)\displaystyle\leq(b(T)-s)\varepsilon(\theta)+\int\_{\{\ln(K/b(T))\}}\big(K-se^{z}\big)\nu(dz) |  | (B.49) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +K​ν​({ln⁡(K/b​(T))})​𝔼​((σ​Wθ−ln⁡(b​(T)/s))+)+o​(θ).\displaystyle\quad+K\nu(\{\ln(K/b(T))\})\mathbb{E}\Big(\big(\sigma W\_{\theta}-\ln(b(T)/s)\big)^{+}\Big)+o(\sqrt{\theta}).\quad |  | (B.50) |

Finally, combining ([B.39](https://arxiv.org/html/2512.17791v1#A2.E39 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")) and ([B.50](https://arxiv.org/html/2512.17791v1#A2.E50 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), and noting that b​(T)b(T) satisfies ([2.7](https://arxiv.org/html/2512.17791v1#S2.E7 "In item (b) ‣ Theorem 2.5. ‣ 2. Setup and Preliminary Results ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,u)\displaystyle g(t,u) | ≥r​K−δ​s+∫(ln⁡(K/b​(T)),∞)(K−s​ez)​ν​(d​z)−(b​(T)−s)​ε​(θ)−K​λ​𝔼​((σ​Wθ−ln⁡(b​(T)/s))+)+o​(θ)\displaystyle\geq rK\!-\!\delta s\!+\!\!\int\_{(\ln(K/b(T)),\infty)}\!\!\!\!\big(K\!-\!se^{z}\big)\nu(dz)\!-\!(b(T)\!-\!s)\varepsilon(\theta)\!-\!K\lambda\mathbb{E}\Big(\!\big(\sigma W\_{\theta}\!-\!\ln(b(T)/s)\big)^{+}\!\Big)\!+\!o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(b​(T)−s)​(δ+∫(ln⁡(K/b​(T)),∞)ez​ν​(d​z)−ε​(θ))−K​λ​𝔼​((σ​Wθ−ln⁡(b​(T)/s))+)+o​(θ)\displaystyle=(b(T)-s)\bigg(\delta+\int\_{(\ln(K/b(T)),\infty)}e^{z}\nu(dz)-\varepsilon(\theta)\bigg)-K\lambda\mathbb{E}\Big(\big(\sigma W\_{\theta}-\ln(b(T)/s)\big)^{+}\Big)+o(\sqrt{\theta}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(δ¯−ε​(θ))​(b​(T)−s)−b​(T)​δ¯​λ​β​𝔼​((σ​Wθ−ln⁡(b​(T)/s))+)+o​(θ),θ→0+,\displaystyle=\big(\bar{\delta}-\varepsilon(\theta)\big)(b(T)-s)-b(T)\bar{\delta}\lambda\beta\,\mathbb{E}\Big(\big(\sigma W\_{\theta}-\ln(b(T)/s)\big)^{+}\Big)+o(\sqrt{\theta}),\quad\theta\rightarrow 0^{+}, |  |

which, together with ([B.25](https://arxiv.org/html/2512.17791v1#A2.E25 "In Proof of Lemma 5.5 ‣ Appendix B Proofs of Lemmas in Section 5 ‣ Near-Maturity Asymptotics of Critical Prices of American Put Options under Exponential Lévy Models")), completes the proof of the lemma. □\Box

## References

* [1]

  G. Barles, J. Burdeau, M. Romano, and N. Samsoen.
  Critical Stock Price near Expiration.
  Math. Financ., 5(2), 77−-95, 1995.
* [2]

  A. Bouselmi and D. Lamberton.
  The Critical Price of the American Put Near Maturity in the Jump Diffusion Model.
  SIAM J. Financ. Math., 7(1), 236−-272, 2016.
* [3]

  R. Cont and P. Tankov.
  Financial Modelling with Jump Processes.
  Chapman & Hall/CRC Financ. Math. Ser., Chapman & Hall/CRC, Boca Raton, FL, U.S.A., 2004.
* [4]

  J. E. Figueroa-López and C. Houdré.
  Small-Time Expansions for the Transition Distributions of Lévy Processes.
  Stoch. Proc. Appl., 119(11), 3862−-3889, 2009.
* [5]

  D. Lamberton and M. Mikou.
  The Critical Price for the American Put in an Exponential Lévy Model.
  Financ. Stoch., 12(4), 561−-581, 2008.
* [6]

  D. Lamberton and M. Mikou.
  The Smooth-Fit Property in an Exponential Lévy Model.
  J. Appl. Prob., 49(1), 137−-149, 2012.
* [7]

  D. Lamberton and M. Mikou.
  Exercise Boundary of the American Put near Maturity in an Exponential Lévy Model.
  Financ. Stoch., 17(2), 355−-394, 2013.
* [8]

  D. Lamberton and S. Villeneuve.
  Critical Price near Maturity for an American Option on a Dividend-Paying Stock.
  Ann. Appl. Probab., 13(2), 800−-815, 2003.
* [9]

  P. V. Moerbeke.
  On Optimal Stopping and Free Boundary Problems.
  Arch. Ration. Mech. Anal., 60(2), 101−-148, 1976.
* [10]

  C. Mou and Y. P. Zhang.
  Regularity Theory for Second Order Integro-PDEs.
  Potential Anal., 54(2), 387−-407, 2021.
* [11]

  H. Pham.
  Optimal Stopping, Free Boundary, and American Option in a Jump-Diffusion Model.
  Appl. Math. Optim., 35(2), 145−-164, 1997.
* [12]

  H. Pham.
  Optimal Stopping of Controlled Jump Diffusion Processes: A Viscosity Solution Approach.
  J. Math. Systems Estim. Control, 8(1), 1−-27, 1998.
* [13]

  P. E. Protter.
  Stochastic Integration and Differential Equations, 2nd Ed.
  Stoch. Model. Appl. Probab., 21, Springer-Verlag Berlin Heidelberg, 2005.
* [14]

  K. Sato.
  Lévy Processes and Infinitely Divisible Distributions.
  Cambridge Stud. Adv. Math., 68, Cambridge University Press, Cambridge, U.K., 1999.