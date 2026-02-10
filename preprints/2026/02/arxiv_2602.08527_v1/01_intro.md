---
authors:
- Mario Ayala
- Benjamin Vallejo Jiménez
doc_id: arxiv:2602.08527v1
family_id: arxiv:2602.08527
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Consumption–Investment with anticipative noise
url_abs: http://arxiv.org/abs/2602.08527v1
url_html: https://arxiv.org/html/2602.08527v1
venue: arXiv q-fin
version: 1
year: 2026
---


Mario Ayala
  
School of Computation, Information and Technology,
  
Chair for Analysis and Modelling, Technische Universität München,
  
Boltzmannstraße 3, 85748 Garching, Germany
  
Benjamin Vallejo Jiménez
  
Facultad de Economía, Universidad de Colima
  
Josefa Ortiz de Domínguez #64, Col. La Haciendita,
  
C.P. 28970, Villa de Álvarez, Colima, México

(August 2025)

###### Abstract

We revisit the classical Merton consumption–investment problem when risky asset
returns are modeled by stochastic differential equations interpreted through a
general α\alpha–integral, interpolating between Itô, Stratonovich, and related
conventions. Holding preferences and the investment opportunity set fixed,
changing the noise interpretation modifies the effective drift of asset returns
in a systematic way.

For logarithmic utility and constant volatilities, we derive closed–form optimal
policies in a market with nn risky assets: optimal consumption remains a fixed
fraction of wealth, while optimal portfolio weights are shifted according to

|  |  |  |
| --- | --- | --- |
|  | θα∗=V−1​(μ−r​𝟏)+α​V−1​diag⁡(V)​ 1,\theta\_{\alpha}^{\*}=V^{-1}(\mu-r\mathbf{1})+\alpha\,V^{-1}\operatorname{diag}(V)\,\mathbf{1}, |  |

where VV is the return covariance matrix. In the single–asset case this reduces
to θα∗=(μ−r)/σ2+α\theta\_{\alpha}^{\*}=(\mu-r)/\sigma^{2}+\alpha.

We then show that genuinely state–dependent effects arise when asset volatility
is driven by a stochastic factor correlated with returns. In this setting, the
α\alpha–interpretation generates an additional drift correction proportional to
the instantaneous covariation between factor and return noise. As a canonical
example, we analyze a Heston stochastic volatility model, where the resulting
optimal risky exposure depends inversely on the current variance level.

## 1 Introduction

Models of intertemporal choice under uncertainty often rely on continuous–time
representations of portfolio dynamics. Since the seminal contributions of
Merton [[15](https://arxiv.org/html/2602.08527v1#bib.bib41 "Lifetime portfolio selection under uncertainty: the continuous‐time case"), [16](https://arxiv.org/html/2602.08527v1#bib.bib42 "Optimum consumption and portfolio rules in a continuous‐time model")], the standard approach assumes that asset
returns follow Brownian diffusions and that investors choose consumption and
portfolio shares to maximize expected discounted utility. Under these premises,
the resulting optimal policies have shaped much of modern asset pricing,
household finance, and dynamic decision theory.

Beyond the classical formulation, numerous extensions of the Merton problem have
been proposed, including models with Markov–modulated drifts and volatilities
that capture regime–switching behavior in financial markets
[[19](https://arxiv.org/html/2602.08527v1#bib.bib56 "Optimal consumption and portfolio decisions when the risky asset is driven by a time-inhomogeneous markov modulated diffusion process"), [21](https://arxiv.org/html/2602.08527v1#bib.bib57 "Consumption and portfolio rules with stochastic dynamics driven by markov switching processes"), [20](https://arxiv.org/html/2602.08527v1#bib.bib58 "Closed-form consumption–investment rules under markov-modulated preferences")]. Further
developments allow for richer asset price dynamics, such as stochastic volatility
and jump–diffusion specifications, or more general time–varying investment
opportunities [[14](https://arxiv.org/html/2602.08527v1#bib.bib59 "Optimal consumption and insurance: a continuous-time markov chain approach"), [4](https://arxiv.org/html/2602.08527v1#bib.bib63 "Option theory with stochastic volatility and jumps")]. Other strands of the literature
introduce non–standard preferences and additional life–cycle features,
including habit formation, mortality, and insurance decisions
[[16](https://arxiv.org/html/2602.08527v1#bib.bib42 "Optimum consumption and portfolio rules in a continuous‐time model"), [5](https://arxiv.org/html/2602.08527v1#bib.bib60 "On the relation between continuous and discrete-time portfolio problems")], or incorporate portfolio constraints
and transaction costs to better reflect institutional and regulatory frictions
[[9](https://arxiv.org/html/2602.08527v1#bib.bib61 "Portfolio selection with transaction costs"), [18](https://arxiv.org/html/2602.08527v1#bib.bib62 "Dynamic stochastic portfolio optimization with transaction costs and constraints")].

A key modelling convention shared by most of this literature is the use of the
Itô integral to describe how information enters asset prices. Economically, the
Itô interpretation embodies strict non–anticipation: trading strategies are
based on current information and discounted prices form semimartingales under the
usual modeling assumptions. This guarantees compatibility with the absence of
arbitrage and supports the normative interpretation of optimal portfolio
decisions.

However, empirical research shows that high–frequency returns are affected by
microstructure frictions such as discreteness, bid–ask bounce, order–flow
imbalances, and latency
[[12](https://arxiv.org/html/2602.08527v1#bib.bib43 "Realized variance and market microstructure noise"), [1](https://arxiv.org/html/2602.08527v1#bib.bib44 "High frequency market microstructure noise estimates and liquidity measures"), [6](https://arxiv.org/html/2602.08527v1#bib.bib47 "Algorithmic and high-frequency trading"), [11](https://arxiv.org/html/2602.08527v1#bib.bib48 "High-frequency trading: methodologies and market impact")].
In such environments, observed returns reflect information aggregated over short
intervals, and the stylized Itô convention may not accurately represent how
agents process shocks in real time. This has motivated interest in alternative
stochastic interpretations, most notably the Stratonovich integral and the more
general α\alpha–interpretation, which evaluate increments at different points
within each time interval. Although these interpretations differ only by a
modelling convention about temporal averaging, they induce systematic and
interpretable changes in effective drift terms
[[10](https://arxiv.org/html/2602.08527v1#bib.bib50 "On the relation between stratonovich and itô integrals with functional integrands"), [22](https://arxiv.org/html/2602.08527v1#bib.bib51 "Beyond itô versus stratonovich")].

Changing the interpretation of stochastic noise can also affect fundamental
structural properties of continuous–time models, such as time reversibility,
long–run invariant measures, and behavior under temporal aggregation
[[2](https://arxiv.org/html/2602.08527v1#bib.bib55 "Reversibility, covariance and coarse-graining for langevin dynamics: on the choice of multiplicative noise")]. These features play an important role in how
stochastic dynamics are estimated, coarse–grained, or calibrated from
high–frequency data, and are therefore directly relevant for economic decision
problems built on estimated dynamics. At the same time, when asset prices are
driven by noises that are not semimartingales, classical self–financing
conditions may permit arbitrage. Fractional Brownian motion provides a prominent
example: [[7](https://arxiv.org/html/2602.08527v1#bib.bib53 "Arbitrage in fractional brownian motion models")] shows that fractional Bachelier and
Samuelson models admit arbitrage unless admissible strategies are severely
restricted, while [[3](https://arxiv.org/html/2602.08527v1#bib.bib52 "An itô formula for a fractional stratonovich type integral with arbitrary hurst parameter and stratonovich self-financing arbitrage")] constructs a Stratonovich–type integral for
fractional Brownian motion and demonstrates arbitrage in fractional
Black–Scholes markets. Taken together, these results illustrate that seemingly
innocuous modelling conventions governing how randomness is interpreted can have
economically significant implications.

### Contribution

This paper revisits the Merton consumption–investment problem when noisy asset
returns are interpreted using a general α\alpha–integral, interpolating between
Itô, Stratonovich, and related conventions. We deliberately hold preferences,
technology, and the self–financing constraint fixed, and isolate the effect of
the noise interpretation on optimal behavior.

We first analyze markets with constant volatilities and show that, in this
setting, the α\alpha–interpretation induces a transparent deterministic shift
in expected returns proportional to instantaneous variances. For logarithmic
utility, this yields closed–form optimal policies in a market with nn risky
assets. Optimal consumption remains a fixed proportion of wealth, while optimal
portfolio weights satisfy

|  |  |  |
| --- | --- | --- |
|  | θα∗=V−1​(μ−r​𝟏)+α​V−1​diag⁡(V)​ 1,\theta\_{\alpha}^{\*}=V^{-1}(\mu-r\mathbf{1})+\alpha\,V^{-1}\operatorname{diag}(V)\,\mathbf{1}, |  |

where V=Σ​Σ⊤V=\Sigma\Sigma^{\top} is the return covariance matrix. In the single–asset
case this reduces to

|  |  |  |
| --- | --- | --- |
|  | θα∗=μ−rσ2+α,\theta\_{\alpha}^{\*}=\frac{\mu-r}{\sigma^{2}}+\alpha, |  |

implying that interpretations closer to the anticipative end of the
α\alpha–scale prescribe higher optimal risky exposure than the Itô benchmark.

We then show that genuinely state–dependent effects arise once asset volatility
is driven by a stochastic factor that is correlated with returns. In this
factor–driven setting, the α\alpha–interpretation generates an additional
drift correction proportional to the instantaneous covariation between the
factor and the return noise. For logarithmic utility, optimal consumption remains
myopic, while the optimal risky fraction acquires a factor–dependent
α\alpha–correction.

As a canonical illustration, we analyze a Heston stochastic volatility model, introduced in [[13](https://arxiv.org/html/2602.08527v1#bib.bib64 "A closed-form solution for options with stochastic volatility with applications to bond and currency options")] ,in
which the instantaneous variance follows a square–root diffusion and return
and volatility shocks are correlated. In this setting, the
α\alpha–interpretation induces a constant shift in the effective expected
return and modifies the long–run mean of the variance process, while preserving
its CIR structure. For logarithmic utility, optimal consumption remains
proportional to wealth, while the optimal risky fraction takes the explicit form

|  |  |  |
| --- | --- | --- |
|  | ct∗=ρ​At,πt∗=μeff−rVt=μ−rVt+α​ϱ​ξ2​1Vt.c\_{t}^{\ast}=\rho A\_{t},\qquad\pi\_{t}^{\ast}=\frac{\mu\_{\mathrm{eff}}-r}{V\_{t}}=\frac{\mu-r}{V\_{t}}+\alpha\,\varrho\,\frac{\xi}{2}\,\frac{1}{V\_{t}}. |  |

The impact of the noise interpretation therefore scales inversely with the
current variance level, amplifying its economic relevance in low–volatility
regimes.

Overall, our results show that modelling conventions governing the
interpretation of stochastic noise, often treated as innocuous, can have
economically meaningful and state–dependent consequences for optimal
intertemporal decisions, particularly in environments with stochastic volatility
and correlated sources of uncertainty.

### Structure of the paper

Section [2.1](https://arxiv.org/html/2602.08527v1#S2.SS1 "2.1 Filtered probability space and Brownian motion ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise") introduces the probabilistic framework and the
stochastic–calculus conventions used throughout.
Section [2.2](https://arxiv.org/html/2602.08527v1#S2.SS2 "2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise") revisits the classical one–asset Merton
consumption–investment problem under the Itô interpretation, while
Section [3](https://arxiv.org/html/2602.08527v1#S3 "3 Stratonovich interpretation and its impact on optimal investment ‣ Consumption–Investment with anticipative noise") analyzes the same problem under the
Stratonovich convention and identifies the induced drift correction and its
impact on optimal portfolio choice.
Section [4](https://arxiv.org/html/2602.08527v1#S4 "4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise") extends the analysis to a market with nn risky
assets under a general α\alpha–interpretation and derives closed–form optimal
consumption and portfolio rules together with their comparative statics in
α\alpha.
Section [5](https://arxiv.org/html/2602.08527v1#S5 "5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise") introduces factor–driven volatility
with correlated return and factor shocks, showing how the α\alpha–interpretation
leads to genuinely state–dependent effects; the Heston stochastic volatility
model is treated as a canonical illustration.
Appendix [A](https://arxiv.org/html/2602.08527v1#A1 "Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise") collects conversion formulas between Itô,
Stratonovich, Klimontovich, and intermediate α\alpha–conventions, including the
correlated–noise reduction used in the factor–driven setting.

## 2 Preliminaries

### 2.1 Filtered probability space and Brownian motion

We work on a complete probability space

|  |  |  |
| --- | --- | --- |
|  | (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) |  |

supporting an nn-dimensional standard Brownian motion

|  |  |  |
| --- | --- | --- |
|  | B=(Bt)t≥0=(Bt1,…,Btn)⊤.B=(B\_{t})\_{t\geq 0}=(B\_{t}^{1},\dots,B\_{t}^{n})^{\top}. |  |

Thus B0=0B\_{0}=0 almost surely, BB has continuous paths, and its increments are independent, stationary, and Gaussian with

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Bt]=0,Cov​(Bt)=t​In,t≥0,\mathbb{E}[B\_{t}]=0,\qquad\mathrm{Cov}(B\_{t})=t\,I\_{n},\qquad t\geq 0, |  |

where InI\_{n} is the n×nn\times n identity matrix.

Let {ℱtB}t≥0\{\mathcal{F}\_{t}^{B}\}\_{t\geq 0} be the natural filtration generated by BB,

|  |  |  |
| --- | --- | --- |
|  | ℱtB:=σ(Bs: 0≤s≤t),\mathcal{F}\_{t}^{B}:=\sigma(B\_{s}:\,0\leq s\leq t), |  |

and let {𝔽t}t≥0\{\mathbb{F}\_{t}\}\_{t\geq 0} denote its usual augmentation:

|  |  |  |
| --- | --- | --- |
|  | 𝔽t:=⋂u>t(ℱuB∨𝒩),\mathbb{F}\_{t}:=\bigcap\_{u>t}(\mathcal{F}\_{u}^{B}\vee\mathcal{N}), |  |

where 𝒩\mathcal{N} is the collection of ℙ\mathbb{P}-null sets contained in ℱ\mathcal{F}.
Throughout, {𝔽t}\{\mathbb{F}\_{t}\} is assumed to be complete and right-continuous.
All stochastic processes are 𝔽\mathbb{F}-adapted unless explicitly stated otherwise.

###### Definition 2.1 (Progressive measurability and the Itô integral).

Let 𝒫\mathscr{P} be the progressive σ\sigma-algebra on Ω×[0,∞)\Omega\times[0,\infty) associated with the filtration {𝔽t}\{\mathbb{F}\_{t}\}.

A process H=(Ht)t≥0H=(H\_{t})\_{t\geq 0} taking values in ℝd×n\mathbb{R}^{d\times n} is called progressively measurable if it is measurable with respect to 𝒫\mathscr{P}.

We say that HH belongs to ℋloc2​(B)\mathcal{H}^{2}\_{\mathrm{loc}}(B) if

|  |  |  |
| --- | --- | --- |
|  | ∫0T‖Ht‖F2​𝑑t<∞almost surely for all ​T>0,\int\_{0}^{T}\|H\_{t}\|\_{F}^{2}\,dt<\infty\quad\text{almost surely for all }T>0, |  |

where ‖A‖F:=(tr​(A⊤​A))1/2\|A\|\_{F}:=(\mathrm{tr}(A^{\top}A))^{1/2} is the Frobenius norm.

For any H∈ℋloc2​(B)H\in\mathcal{H}^{2}\_{\mathrm{loc}}(B), the Itô integral

|  |  |  |
| --- | --- | --- |
|  | ∫0tHs​𝑑Bs\int\_{0}^{t}H\_{s}\,dB\_{s} |  |

is an ℝd\mathbb{R}^{d}-valued continuous local martingale satisfying

|  |  |  |
| --- | --- | --- |
|  | [∫0⋅Hs​𝑑Bs]t=∫0tHs​Hs⊤​𝑑s,\left[\int\_{0}^{\cdot}H\_{s}\,dB\_{s}\right]\_{t}=\int\_{0}^{t}H\_{s}H\_{s}^{\top}\,ds, |  |

and the Itô isometry

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖∫0tHs​𝑑Bs‖2=𝔼​∫0ttr​(Hs​Hs⊤)​𝑑s.\mathbb{E}\left\|\int\_{0}^{t}H\_{s}\,dB\_{s}\right\|^{2}=\mathbb{E}\int\_{0}^{t}\mathrm{tr}(H\_{s}H\_{s}^{\top})\,ds. |  |

###### Remark 2.1.

Let RR be a symmetric positive definite n×nn\times n matrix.
Choose any deterministic matrix CC satisfying C​C⊤=RCC^{\top}=R (for instance, a Cholesky factor).
Define

|  |  |  |
| --- | --- | --- |
|  | Wt:=C​Bt,t≥0.W\_{t}:=CB\_{t},\qquad t\geq 0. |  |

Then WW is an nn–dimensional Brownian motion with covariance matrix RR,
in the sense that

|  |  |  |
| --- | --- | --- |
|  | [W]t=R​t.[W]\_{t}=R\,t. |  |

If GG is a progressively measurable ℝd×n\mathbb{R}^{d\times n}-valued process with
∫0T‖Gt‖F2​𝑑t<∞\int\_{0}^{T}\|G\_{t}\|\_{F}^{2}\,dt<\infty almost surely, then

|  |  |  |
| --- | --- | --- |
|  | ∫0tGs​𝑑Ws=∫0t(Gs​C)​𝑑Bs,\int\_{0}^{t}G\_{s}\,dW\_{s}=\int\_{0}^{t}(G\_{s}C)\,dB\_{s}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | [∫0⋅Gs​𝑑Ws]t=∫0tGs​R​Gs⊤​𝑑s,\left[\int\_{0}^{\cdot}G\_{s}\,dW\_{s}\right]\_{t}=\int\_{0}^{t}G\_{s}RG\_{s}^{\top}\,ds, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖∫0tGs​𝑑Ws‖2=𝔼​∫0ttr​(Gs​R​Gs⊤)​𝑑s.\mathbb{E}\left\|\int\_{0}^{t}G\_{s}\,dW\_{s}\right\|^{2}=\mathbb{E}\int\_{0}^{t}\mathrm{tr}(G\_{s}RG\_{s}^{\top})\,ds. |  |

Setting R=InR=I\_{n} yields the standard Brownian case W=BW=B.

###### Remark 2.2.

For a matrix MM, tr​(M)\mathrm{tr}(M) denotes its trace and diag​(M)\mathrm{diag}(M) the vector of its diagonal entries.
For vectors x,y∈ℝmx,y\in\mathbb{R}^{m}, the Euclidean inner product is x⊤​yx^{\top}y.
For matrices A,BA,B of the same size, the Frobenius inner product is

|  |  |  |
| --- | --- | --- |
|  | ⟨A,B⟩F:=tr​(A⊤​B).\langle A,B\rangle\_{F}:=\mathrm{tr}(A^{\top}B). |  |

###### Assumption 2.1 (Standing assumptions).

Throughout the paper we impose the following conditions.

1. (i)

   Stochastic basis.
   All processes are defined on a filtered probability space

   |  |  |  |
   | --- | --- | --- |
   |  | (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) |  |

   satisfying the usual conditions, and all stochastic integrals are taken with respect to
   (ℱt)(\mathcal{F}\_{t})–Brownian motions.
2. (ii)

   Regularity of coefficients.
   All drift and diffusion coefficients appearing in the asset, factor, and
   wealth dynamics are deterministic functions.
   More precisely, whenever a state process Y={Yt}t≥0Y=\{Y\_{t}\}\_{t\geq 0} is defined as a
   solution to an SDE of the form

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | d​Yt=μ​(Yt)​d​t+σ​(Yt)∘αd​Wt,\mathrm{d}Y\_{t}=\mu(Y\_{t})\,\mathrm{d}t+\sigma(Y\_{t})\,\circ\_{\alpha}\mathrm{d}W\_{t}, |  | (2.1) |

   the functions μ,σ:ℝ→ℝ\mu,\sigma:\mathbb{R}\to\mathbb{R} satisfy the following
   conditions:

   1. (a)

      Local Lipschitz continuity:
      For every R>0R>0 there exists a constant LR>0L\_{R}>0 such that

      |  |  |  |
      | --- | --- | --- |
      |  | |μ​(x)−μ​(y)|+|σ​(x)−σ​(y)|≤LR​|x−y|,∀x,y∈[−R,R].|\mu(x)-\mu(y)|+|\sigma(x)-\sigma(y)|\leq L\_{R}|x-y|,\qquad\forall\,x,y\in[-R,R]. |  |
   2. (b)

      Linear growth:
      There exists a constant C>0C>0 such that

      |  |  |  |
      | --- | --- | --- |
      |  | |μ​(x)|+|σ​(x)|≤C​(1+|x|),∀x∈ℝ.|\mu(x)|+|\sigma(x)|\leq C\,(1+|x|),\qquad\forall\,x\in\mathbb{R}. |  |
   3. (c)

      Differentiability of diffusion coefficients:
      Whenever an α\alpha–to–Itô conversion is performed, the diffusion
      coefficient σ\sigma is assumed to be continuously differentiable, with
      derivative σ′\sigma^{\prime} satisfying a linear growth bound

      |  |  |  |
      | --- | --- | --- |
      |  | |σ′​(x)|≤C​(1+|x|),∀x∈ℝ.|\sigma^{\prime}(x)|\leq C\,(1+|x|),\qquad\forall\,x\in\mathbb{R}. |  |

### 2.2 Classical one–asset consumption–investment problem

In this subsection we recall the classical continuous–time consumption–investment
problem with logarithmic utility introduced by Merton [[17](https://arxiv.org/html/2602.08527v1#bib.bib1 "Optimum consumption and portfolio rules in a continuous-time model")].
We work with n=1n=1 and on the filtered probability space
(Ω,ℱ,{𝔽t}t≥0,ℙ)(\Omega,\mathcal{F},\{\mathbb{F}\_{t}\}\_{t\geq 0},\mathbb{P})
specified in Section [2.1](https://arxiv.org/html/2602.08527v1#S2.SS1 "2.1 Filtered probability space and Brownian motion ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise").

In the classical formulation, an infinitely–lived agent observes the evolution of a
financial market in continuous time and must choose, at each moment, (i) how much
wealth to consume and (ii) how to split remaining wealth between a risk–free asset and
a risky asset. The objective is to maximize discounted expected utility of consumption
over the infinite horizon. A central modelling assumption is that decisions cannot
anticipate future randomness: controls must be adapted to the market filtration.
We also impose the usual self–financing constraint, so changes in wealth arise solely
from investment gains and consumption. Under these assumptions, Merton’s framework
reduces the economic problem to a stochastic control problem driven by Brownian noise.

#### 2.2.1 Assets and source of randomness

On the filtered probability space
(Ω,ℱ,{𝔽t}t≥0,ℙ)(\Omega,\mathcal{F},\{\mathbb{F}\_{t}\}\_{t\geq 0},\mathbb{P})
we consider a risk–free money–market account b=(bt)t≥0b=(b\_{t})\_{t\geq 0} and a risky
asset S=(St)t≥0S=(S\_{t})\_{t\geq 0}.
The money–market account evolves deterministically as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​bt=r​bt​d​t,r>0,\mathrm{d}b\_{t}=r\,b\_{t}\,\mathrm{d}t,\qquad r>0, |  | (2.2) |

while the risky asset follows a geometric Brownian motion,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=μ​St​d​t+σ​St​d​Wt,μ∈ℝ,σ>0,\mathrm{d}S\_{t}=\mu\,S\_{t}\,\mathrm{d}t+\sigma\,S\_{t}\,\mathrm{d}W\_{t},\qquad\mu\in\mathbb{R},\ \sigma>0, |  | (2.3) |

where W=(Wt)t≥0W=(W\_{t})\_{t\geq 0} is a one–dimensional standard Brownian motion
adapted to {𝔽t}\{\mathbb{F}\_{t}\}.

#### 2.2.2 Controls and wealth dynamics

We denote by ata\_{t} the total wealth of the investor at time tt.
A *control* is a progressively measurable pair (ct,θt)(c\_{t},\theta\_{t}), where

* •

  ct≥0c\_{t}\geq 0 is the consumption rate; the cumulative consumption process
  is Ct=∫0tcs​dsC\_{t}=\int\_{0}^{t}c\_{s}\,\mathrm{d}s,
* •

  θt∈ℝ\theta\_{t}\in\mathbb{R} is the fraction of current wealth invested in
  the risky asset (so 1−θt1-\theta\_{t} is invested in the money–market account).

The *self–financing* condition stipulates that changes in wealth, whose value at time t≥0t\geq 0 we denote by ata\_{t},
are due only to trading gains/losses and consumption. In differential form,
this reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​at=at​(1−θt)​d​btbt+at​θt​d​StSt−ct​d​t.\mathrm{d}a\_{t}=a\_{t}(1-\theta\_{t})\,\frac{\mathrm{d}b\_{t}}{b\_{t}}+a\_{t}\theta\_{t}\,\frac{\mathrm{d}S\_{t}}{S\_{t}}-c\_{t}\,\mathrm{d}t. |  | (2.4) |

Substituting ([2.2](https://arxiv.org/html/2602.08527v1#S2.E2 "In 2.2.1 Assets and source of randomness ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) and ([2.3](https://arxiv.org/html/2602.08527v1#S2.E3 "In 2.2.1 Assets and source of randomness ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) into
([2.4](https://arxiv.org/html/2602.08527v1#S2.E4 "In 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) yields the Itô SDE for wealth,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​at=at​(r+θt​(μ−r)−ctat)​d​t+at​θt​σ​d​Wt.\mathrm{d}a\_{t}=a\_{t}\Big(r+\theta\_{t}(\mu-r)-\frac{c\_{t}}{a\_{t}}\Big)\mathrm{d}t+a\_{t}\,\theta\_{t}\,\sigma\,\mathrm{d}W\_{t}. |  | (2.5) |

###### Definition 2.2 (Admissible controls).

A progressively measurable pair (ct,θt)(c\_{t},\theta\_{t}) is *admissible* if:

1. 1.

   ct≥0c\_{t}\geq 0 and θt∈ℝ\theta\_{t}\in\mathbb{R} for all t≥0t\geq 0, and
   Ct=∫0tcs​dsC\_{t}=\int\_{0}^{t}c\_{s}\,\mathrm{d}s has almost surely finite variation;
2. 2.

   the wealth process ata\_{t} is strictly positive and satisfies the SDE
   ([2.5](https://arxiv.org/html/2602.08527v1#S2.E5 "In 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise"));
3. 3.

   for every T>0T>0,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼​∫0T(ct+θt2​σ2​at2)​dt<∞.\mathbb{E}\!\int\_{0}^{T}\bigl(c\_{t}+\theta\_{t}^{2}\sigma^{2}a\_{t}^{2}\bigr)\,\mathrm{d}t<\infty. |  | (2.6) |

###### Remark 2.3.

The requirements in the definition of admissible controls ensure both economic
coherence and mathematical well–posedness. Their roles can be summarized as follows:

* •

  Regularity of consumption.
  The conditions ct≥0c\_{t}\geq 0 and the finite variation of
  Ct=∫0tcs​dsC\_{t}=\int\_{0}^{t}c\_{s}\,\mathrm{d}s rule out irregular or distributional
  consumption paths.
  This ensures that consumption enters the budget identity in a meaningful
  and economically interpretable way.
* •

  Positivity and well–defined wealth dynamics.
  Imposing at>0a\_{t}>0 and requiring that ata\_{t} satisfies ([2.5](https://arxiv.org/html/2602.08527v1#S2.E5 "In 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise"))
  ensures existence, uniqueness, and nonexplosion of the wealth process.
  Economically, it prevents bankruptcy in finite time and excludes
  unbounded negative wealth positions that would make the optimization
  problem degenerate.
* •

  Square–integrability of controls.
  The integrability condition ([2.6](https://arxiv.org/html/2602.08527v1#S2.E6 "In item 3 ‣ Definition 2.2 (Admissible controls). ‣ 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise"))
  excludes trading strategies that generate infinite instantaneous variation
  or rely on unbounded leverage.
  Analytically, it guarantees that the stochastic integral in the wealth
  equation is well-defined and that the HJB verification argument applies.

Taken together, these conditions eliminate pathological strategies and ensure
that the consumption–investment problem is mathematically well posed.

#### 2.2.3 Utility maximization problem

Given a subjective discount rate ρ>0\rho>0, the investor selects an admissible
control (ct,θt)(c\_{t},\theta\_{t}) to maximize the expected discounted utility of
consumption. The associated *value function* is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(a,t):=sup(c,θ)​adm.𝔼​[∫t∞e−ρ​(s−t)​u​(cs)​ds|at=a],J(a,t):=\sup\_{(c,\theta)\ \text{adm.}}\mathbb{E}\!\left[\int\_{t}^{\infty}e^{-\rho(s-t)}\,u(c\_{s})\,\mathrm{d}s\,\Big|\,a\_{t}=a\right], |  | (2.7) |

where a>0a>0 denotes current wealth at time tt, and where throughout this
subsection we take u​(x)=ln⁡xu(x)=\ln x.
Under logarithmic utility the investor exhibits constant relative risk aversion,
and the optimal portfolio rule depends only on the instantaneous investment
opportunities (the so-called *myopic* property).

To characterize the function JJ, we assume that the dynamic programming
principle holds and that JJ is sufficiently smooth: specifically,
J∈C2,1​((0,∞)×[0,∞))J\in C^{2,1}((0,\infty)\times[0,\infty)), with

|  |  |  |
| --- | --- | --- |
|  | Ja​(a,t)=∂J∂a​(a,t),Ja​a​(a,t)=∂2J∂a2​(a,t),Jt​(a,t)=∂J∂t​(a,t).J\_{a}(a,t)=\frac{\partial J}{\partial a}(a,t),\qquad J\_{aa}(a,t)=\frac{\partial^{2}J}{\partial a^{2}}(a,t),\qquad J\_{t}(a,t)=\frac{\partial J}{\partial t}(a,t). |  |

Applying Itô’s formula to J​(at,t)J(a\_{t},t) along the wealth dynamics
([2.5](https://arxiv.org/html/2602.08527v1#S2.E5 "In 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) yields that JJ must satisfy the Hamilton–Jacobi–Bellman
equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=supc≥0,θ∈ℝ{ln⁡c−ρ​J​(a,t)+Jt​(a,t)+Ja​(a,t)​a​(r+θ​(μ−r)−ca)+12​Ja​a​(a,t)​a2​θ2​σ2}.0=\sup\_{c\geq 0,\ \theta\in\mathbb{R}}\left\{\ln c-\rho J(a,t)+J\_{t}(a,t)+J\_{a}(a,t)\,a\!\left(r+\theta(\mu-r)-\frac{c}{a}\right)+\tfrac{1}{2}\,J\_{aa}(a,t)\,a^{2}\theta^{2}\sigma^{2}\right\}. |  | (2.8) |

Because ln\ln is strictly concave in cc and Ja​a​(a,t)≤0J\_{aa}(a,t)\leq 0 at an interior
optimum (the value function is concave in wealth), the maximizers of
([2.8](https://arxiv.org/html/2602.08527v1#S2.E8 "In 2.2.3 Utility maximization problem ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) are characterized by the corresponding first–order conditions.

###### Theorem 2.1 (Merton solution for one risky asset).

Consider the wealth dynamics ([2.5](https://arxiv.org/html/2602.08527v1#S2.E5 "In 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) under admissible controls
(ct,θt)(c\_{t},\theta\_{t}), and let the utility function be u​(x)=ln⁡xu(x)=\ln x.
Assume that the value function JJ solves the HJB equation
([2.8](https://arxiv.org/html/2602.08527v1#S2.E8 "In 2.2.3 Utility maximization problem ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) and is sufficiently smooth to justify the first–order
conditions. Then the unique optimal controls are

|  |  |  |
| --- | --- | --- |
|  | ct∗=ρ​at,θt∗=μ−rσ2,c\_{t}^{\*}=\rho\,a\_{t},\qquad\theta\_{t}^{\*}=\frac{\mu-r}{\sigma^{2}}, |  |

and the corresponding value function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(a,t)=(β0+1ρ​ln⁡a)​e−ρ​t,J(a,t)=\left(\beta\_{0}+\frac{1}{\rho}\ln a\right)e^{-\rho t}, |  | (2.9) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | β0=1ρ​(rρ+ln⁡ρ−1)+12​ρ2​(μ−r)2σ2.\beta\_{0}=\frac{1}{\rho}\Bigl(\frac{r}{\rho}+\ln\rho-1\Bigr)+\frac{1}{2\rho^{2}}\,\frac{(\mu-r)^{2}}{\sigma^{2}}. |  | (2.10) |

###### Remark 2.4.

In Merton’s original formulation [[17](https://arxiv.org/html/2602.08527v1#bib.bib1 "Optimum consumption and portfolio rules in a continuous-time model")], the logarithmic case
appears as a special instance of the general HARA (hyperbolic absolute risk
aversion) utility class.
For this specific utility, the HJB equation ([2.8](https://arxiv.org/html/2602.08527v1#S2.E8 "In 2.2.3 Utility maximization problem ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) admits a closed-form
solution, and the first–order conditions lead directly to the explicit controls
and value function stated in Theorem [2.1](https://arxiv.org/html/2602.08527v1#S2.Thmtheorem1 "Theorem 2.1 (Merton solution for one risky asset). ‣ 2.2.3 Utility maximization problem ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise").
Several modern expositions provide streamlined derivations of these formulas.

###### Remark 2.5 (Wealth dynamics under the optimal policy).

Substituting ct∗=ρ​atc\_{t}^{\*}=\rho\,a\_{t} and θt∗=(μ−r)/σ2\theta\_{t}^{\*}=(\mu-r)/\sigma^{2} into the wealth
equation ([2.5](https://arxiv.org/html/2602.08527v1#S2.E5 "In 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) yields the geometric SDE

|  |  |  |
| --- | --- | --- |
|  | d​atat=(r+(μ−r)2σ2−ρ)​d​t+μ−rσ​d​Wt.\frac{\mathrm{d}a\_{t}}{a\_{t}}=\left(r+\frac{(\mu-r)^{2}}{\sigma^{2}}-\rho\right)\mathrm{d}t+\frac{\mu-r}{\sigma}\,\mathrm{d}W\_{t}. |  |

Applying Itô’s formula to ln⁡at\ln a\_{t} gives

|  |  |  |
| --- | --- | --- |
|  | d​(ln⁡at)=(r−ρ+12​(μ−r)2σ2)​d​t+μ−rσ​d​Wt,\mathrm{d}(\ln a\_{t})=\left(r-\rho+\frac{1}{2}\,\frac{(\mu-r)^{2}}{\sigma^{2}}\right)\mathrm{d}t+\frac{\mu-r}{\sigma}\,\mathrm{d}W\_{t}, |  |

which is consistent with the value function ([2.9](https://arxiv.org/html/2602.08527v1#S2.E9 "In Theorem 2.1 (Merton solution for one risky asset). ‣ 2.2.3 Utility maximization problem ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")).
Moreover, under the optimal policy the transversality condition

|  |  |  |
| --- | --- | --- |
|  | limT→∞𝔼​[e−ρ​T​J​(aT,T)]=0\lim\_{T\to\infty}\mathbb{E}\!\left[e^{-\rho T}\,J(a\_{T},T)\right]=0 |  |

holds, ensuring that the infinite-horizon optimization problem is well posed.

###### Remark 2.6.

In the classical formulation above, the economic environment is fully characterised
by three modelling choices: the self–financing wealth equation, the restriction to
non–anticipative (i.e., 𝔽t\mathbb{F}\_{t}–adapted) controls, and the adoption of the
Itô interpretation for the stochastic integral. These assumptions jointly determine
the wealth dynamics and, through the associated HJB equation, the resulting optimal
consumption and portfolio policies. In particular, the familiar Merton portfolio
share arises precisely from this combination of conventions.

In the remainder of the paper we illustrate that, once the interpretation of the noise
is allowed to vary , moving from Itô to Stratonovich, Klimontovich, or the general
α\alpha–scheme, the optimal investment rule changes in a systematic and
quantifiable manner. The reason is that different stochastic interpretations induce
different effective drift terms in the wealth dynamics; from an economic perspective,
this corresponds to altering the informational structure under which the agent
operates. For α>0\alpha>0, the induced drift correction increases the effective
return of the risky asset and leads, under logarithmic utility, to a larger
optimal portfolio share.

## 3 Stratonovich interpretation and its impact on optimal investment

We now reconsider the one–asset consumption–investment problem when the risky
asset is modelled with the Stratonovich interpretation of noise, corresponding
to α=12\alpha=\tfrac{1}{2} in the general α\alpha–scheme.

### 3.1 Stratonovich GBM and effective drift

Let the risky asset S=(St)t≥0S=(S\_{t})\_{t\geq 0} satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=μ​d​t+σ∘1/2d​Wt,μ∈ℝ,σ>0,\frac{\mathrm{d}S\_{t}}{S\_{t}}=\mu\,\mathrm{d}t+\sigma\,\circ\_{1/2}\mathrm{d}W\_{t},\qquad\mu\in\mathbb{R},\ \sigma>0, |  | (3.1) |

while the money–market account evolves as in ([2.2](https://arxiv.org/html/2602.08527v1#S2.E2 "In 2.2.1 Assets and source of randomness ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")).
A Stratonovich SDE of the form

|  |  |  |
| --- | --- | --- |
|  | d​Xt=b​(Xt)​d​t+σ​(Xt)∘1/2d​Wt\mathrm{d}X\_{t}=b(X\_{t})\,\mathrm{d}t+\sigma(X\_{t})\,\circ\_{1/2}\mathrm{d}W\_{t} |  |

is equivalent, using Proposition [A.1](https://arxiv.org/html/2602.08527v1#A1.Thmproposition1 "Proposition A.1 (Conversion between 𝛼– and 𝛾–interpretations). ‣ A.1 General 𝛼→𝛾 conversion ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise"), to the Itô SDE

|  |  |  |
| --- | --- | --- |
|  | d​Xt=(b​(Xt)+12​σ​(Xt)​σ′​(Xt))​d​t+σ​(Xt)​d​Wt.\mathrm{d}X\_{t}=\bigl(b(X\_{t})+\tfrac{1}{2}\sigma(X\_{t})\sigma^{\prime}(X\_{t})\bigr)\mathrm{d}t+\sigma(X\_{t})\,\mathrm{d}W\_{t}. |  |

Since σ​(x)=σ​x\sigma(x)=\sigma x in ([3.1](https://arxiv.org/html/2602.08527v1#S3.E1 "In 3.1 Stratonovich GBM and effective drift ‣ 3 Stratonovich interpretation and its impact on optimal investment ‣ Consumption–Investment with anticipative noise")), we obtain the equivalent Itô form

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=(μ+12​σ2)​d​t+σ​d​Wt.\frac{\mathrm{d}S\_{t}}{S\_{t}}=\bigl(\mu+\tfrac{1}{2}\sigma^{2}\bigr)\mathrm{d}t+\sigma\,\mathrm{d}W\_{t}. |  | (3.2) |

Thus the Stratonovich interpretation does not merely change the calculus rules:
for the same parameters (μ,σ)(\mu,\sigma) it produces a higher *effective drift*

|  |  |  |
| --- | --- | --- |
|  | μeff(1/2)=μ+12​σ2.\mu\_{\mathrm{eff}}^{(1/2)}=\mu+\tfrac{1}{2}\sigma^{2}. |  |

### 3.2 Wealth dynamics and the origin of the modified Merton rule

With at>0a\_{t}>0 denoting wealth, ct≥0c\_{t}\geq 0 consumption, and θt∈ℝ\theta\_{t}\in\mathbb{R} the
risky fraction, the self–financing identity ([2.4](https://arxiv.org/html/2602.08527v1#S2.E4 "In 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")) gives the
wealth SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​at=at​(r+θt​(μ+12​σ2−r)−ctat)​d​t+at​θt​σ​d​Wt,\mathrm{d}a\_{t}=a\_{t}\Bigl(r+\theta\_{t}\bigl(\mu+\tfrac{1}{2}\sigma^{2}-r\bigr)-\frac{c\_{t}}{a\_{t}}\Bigr)\mathrm{d}t+a\_{t}\theta\_{t}\sigma\,\mathrm{d}W\_{t}, |  | (3.3) |

which differs from the classical Itô formulation only through the drift adjustment
μ−r↦μ+12​σ2−r\mu-r\mapsto\mu+\tfrac{1}{2}\sigma^{2}-r.

Crucially, *all steps of the dynamic programming argument remain unchanged*.
The Hamilton–Jacobi–Bellman equation is the same as in
([2.8](https://arxiv.org/html/2602.08527v1#S2.E8 "In 2.2.3 Utility maximization problem ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")), except that the drift of the risky asset entering the
Hamiltonian is now the effective drift ([3.2](https://arxiv.org/html/2602.08527v1#S3.E2 "In 3.1 Stratonovich GBM and effective drift ‣ 3 Stratonovich interpretation and its impact on optimal investment ‣ Consumption–Investment with anticipative noise")).

For logarithmic utility this immediately yields

|  |  |  |
| --- | --- | --- |
|  | θt∗,Strat=μ+12​σ2−rσ2=μ−rσ2+12=θt∗,I​t​o+12,\theta\_{t}^{\*,\,\mathrm{Strat}}=\frac{\mu+\tfrac{1}{2}\sigma^{2}-r}{\sigma^{2}}=\frac{\mu-r}{\sigma^{2}}+\frac{1}{2}=\theta\_{t}^{\*,\,Ito}+\frac{1}{2}, |  |

i.e. Stratonovich noise leads the log–utility investor to allocate an
additional fraction 1/21/2 of wealth into the risky asset.

### 3.3 The chain rule viewpoint

Although the optimal control problem itself is unaffected, the Stratonovich
interpretation has a convenient analytic feature: ordinary calculus applies to
variable transformations.
For example, for xt:=ln⁡atx\_{t}:=\ln a\_{t} the Stratonovich chain rule gives

|  |  |  |
| --- | --- | --- |
|  | d​xt=1at∘1/2d​at=(r+θt​(μ−r)−ct​e−xt)​d​t+θt​σ∘1/2d​Wt.\mathrm{d}x\_{t}=\frac{1}{a\_{t}}\,\circ\_{1/2}\mathrm{d}a\_{t}=\Bigl(r+\theta\_{t}(\mu-r)-c\_{t}e^{-x\_{t}}\Bigr)\mathrm{d}t+\theta\_{t}\sigma\,\circ\_{1/2}\mathrm{d}W\_{t}. |  |

This classical differential form allows one to derive the HJB by a Taylor
expansion and the short-time variance
Var⁡(xt+h−xt)=θt2​σ2​h+o​(h)\operatorname{Var}(x\_{t+h}-x\_{t})=\theta\_{t}^{2}\sigma^{2}h+o(h), rather than invoking Itô’s
lemma explicitly.

However, it is important to emphasize that *the change in the optimal
portfolio rule is not caused by the chain rule*.
The economic effect arises exclusively from the drift correction
μ↦μ+12​σ2\mu\mapsto\mu+\tfrac{1}{2}\sigma^{2} intrinsic to the Stratonovich
(α=12\alpha=\tfrac{1}{2}) interpretation of noise.

###### Remark 3.1 (Summary).

Under the Stratonovich interpretation:

* •

  the effective drift of the risky asset increases by 12​σ2\tfrac{1}{2}\sigma^{2};
* •

  all structural features of the Merton problem remain intact;
* •

  the optimal risky allocation increases by exactly 12\tfrac{1}{2};
* •

  the chain rule becomes classical, which can simplify transformations
  but does not modify the economics of the control problem.

This viewpoint will generalize directly to arbitrary α∈[0,1]\alpha\in[0,1], where the
optimal risky fraction increases by exactly α\alpha.

## 4 nn risky assets under the α\alpha–interpretation

We now extend the log–utility consumption–investment problem to a market with
nn risky assets.
Throughout this section ∘α\circ\_{\alpha} denotes the stochastic integral in the
α\alpha–interpretation, and the nn–dimensional Brownian motion is the one
specified in Section [2.1](https://arxiv.org/html/2602.08527v1#S2.SS1 "2.1 Filtered probability space and Brownian motion ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise").
We write 𝟏∈ℝn\mathbf{1}\in\mathbb{R}^{n} for the vector of ones.

### 4.1 Risky-asset dynamics and the α\alpha–dependent drift shift

Let St=(St1,…,Stn)⊤∈(0,∞)nS\_{t}=(S\_{t}^{1},\dots,S\_{t}^{n})^{\top}\in(0,\infty)^{n} denote the vector of risky
asset prices.
Fix a constant drift μ∈ℝn\mu\in\mathbb{R}^{n} and a constant volatility loading
Σ∈ℝn×n\Sigma\in\mathbb{R}^{n\times n}, and set

|  |  |  |
| --- | --- | --- |
|  | V:=Σ​Σ⊤.V\;:=\;\Sigma\Sigma^{\top}. |  |

For notational convenience let D​(S):=diag​(S1,…,Sn)\mathrm{D}(S):=\mathrm{diag}(S^{1},\dots,S^{n}).
We model prices in the α\alpha–interpretation by the vector SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=D​(St)​(μ​d​t+Σ∘αd​Wt).\mathrm{d}S\_{t}=\mathrm{D}(S\_{t})\Big(\mu\,\mathrm{d}t+\Sigma\,\circ\_{\alpha}\mathrm{d}W\_{t}\Big). |  | (4.1) |

Componentwise,

|  |  |  |
| --- | --- | --- |
|  | d​Sti=Sti​(μi​d​t+∑k=1nΣi​k∘αd​Wtk).\mathrm{d}S\_{t}^{i}=S\_{t}^{i}\Bigl(\mu\_{i}\,\mathrm{d}t+\sum\_{k=1}^{n}\Sigma\_{ik}\circ\_{\alpha}\mathrm{d}W\_{t}^{k}\Bigr). |  |

###### Proposition 4.1 (Itô form of the α\alpha–interpreted SDE).

The α\alpha–SDE ([4.1](https://arxiv.org/html/2602.08527v1#S4.E1 "In 4.1 Risky-asset dynamics and the 𝛼–dependent drift shift ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) is equivalent to the Itô SDE

|  |  |  |
| --- | --- | --- |
|  | d​St=D​(St)​(μIto​d​t+Σ​d​Wt),μIto:=μ+α​diag⁡(V),\mathrm{d}S\_{t}=\mathrm{D}(S\_{t})\Big(\mu^{\mathrm{Ito}}\,\mathrm{d}t+\Sigma\,\mathrm{d}W\_{t}\Big),\qquad\mu^{\mathrm{Ito}}:=\mu+\alpha\,\operatorname{diag}(V), |  |

i.e. only the drift changes, while the diffusion remains Σ​d​Wt\Sigma\,\mathrm{d}W\_{t}.
Equivalently, for each i=1,…,ni=1,\dots,n,

|  |  |  |
| --- | --- | --- |
|  | d​Sti=Sti​(μi+α​Vi​i)​d​t+Sti​∑k=1nΣi​k​d​Wtk.\mathrm{d}S\_{t}^{i}=S\_{t}^{i}\Bigl(\mu\_{i}+\alpha V\_{ii}\Bigr)\mathrm{d}t+S\_{t}^{i}\sum\_{k=1}^{n}\Sigma\_{ik}\mathrm{d}W\_{t}^{k}. |  |

###### Proof.

Write ([4.1](https://arxiv.org/html/2602.08527v1#S4.E1 "In 4.1 Risky-asset dynamics and the 𝛼–dependent drift shift ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) as d​Xt=a​(Xt)​d​t+B​(Xt)∘αd​Wt\mathrm{d}X\_{t}=a(X\_{t})\mathrm{d}t+B(X\_{t})\circ\_{\alpha}\mathrm{d}W\_{t}
with X=SX=S, a​(S)=D​(S)​μa(S)=\mathrm{D}(S)\mu, B​(S)=D​(S)​ΣB(S)=\mathrm{D}(S)\Sigma.
The standard α\alpha–to–Itô conversion formula gives

|  |  |  |
| --- | --- | --- |
|  | aiIto​(x)=ai​(x)+α​∑k=1n∑j=1nBj​k​(x)​∂xjBi​k​(x).a\_{i}^{\mathrm{Ito}}(x)=a\_{i}(x)+\alpha\sum\_{k=1}^{n}\sum\_{j=1}^{n}B\_{jk}(x)\,\partial\_{x\_{j}}B\_{ik}(x). |  |

Since Bi​k​(S)=Σi​k​SiB\_{ik}(S)=\Sigma\_{ik}S^{i} depends only on SiS^{i},
∂xjBi​k​(S)=Σi​k​δi​j\partial\_{x\_{j}}B\_{ik}(S)=\Sigma\_{ik}\delta\_{ij} and hence

|  |  |  |
| --- | --- | --- |
|  | ∑k,jBj​k​(S)​∂xjBi​k​(S)=∑kBi​k​(S)​Σi​k=Si​∑kΣi​k2=Si​Vi​i.\sum\_{k,j}B\_{jk}(S)\,\partial\_{x\_{j}}B\_{ik}(S)=\sum\_{k}B\_{ik}(S)\Sigma\_{ik}=S^{i}\sum\_{k}\Sigma\_{ik}^{2}=S^{i}V\_{ii}. |  |

Thus aiIto​(S)=Si​(μi+α​Vi​i)a\_{i}^{\mathrm{Ito}}(S)=S^{i}(\mu\_{i}+\alpha V\_{ii}) and diffusion remains
B​(S)=D​(S)​ΣB(S)=\mathrm{D}(S)\Sigma, yielding the claim.
∎

###### Remark 4.1 (Economic interpretation).

Under the α\alpha–interpretation, all parameters (μ,Σ)(\mu,\Sigma) are kept fixed,
but the effective expected returns become

|  |  |  |
| --- | --- | --- |
|  | μIto=μ+α​diag⁡(V).\mu^{\mathrm{Ito}}=\mu+\alpha\,\operatorname{diag}(V). |  |

In dimension one this gives μIto=μ+α​σ2\mu^{\mathrm{Ito}}=\mu+\alpha\sigma^{2}, increasing
expected returns by α​σ2\alpha\sigma^{2}.
Thus, interpreting noise closer to the anticipative end of the scale
(α>0\alpha>0) increases the risk premium and consequently leads to larger optimal
positions in risky assets.

### 4.2 Wealth dynamics under the α\alpha–interpretation

Let θt∈ℝn\theta\_{t}\in\mathbb{R}^{n} denote the vector of portfolio weights invested in risky
assets, and ct≥0c\_{t}\geq 0 denote consumption.
As in the one-dimensional case, the self–financing identity gives the Itô wealth
dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​at=at​(r+θt⊤​(μIto−r​𝟏)−ctat)​d​t+at​θt⊤​Σ​d​Wt,\mathrm{d}a\_{t}=a\_{t}\Bigl(r+\theta\_{t}^{\top}(\mu^{\mathrm{Ito}}-r\mathbf{1})-\tfrac{c\_{t}}{a\_{t}}\Bigr)\mathrm{d}t+a\_{t}\,\theta\_{t}^{\top}\Sigma\,\mathrm{d}W\_{t}, |  | (4.2) |

where μIto\mu^{\mathrm{Ito}} is given in Proposition [4.1](https://arxiv.org/html/2602.08527v1#S4.Thmproposition1 "Proposition 4.1 (Itô form of the 𝛼–interpreted SDE). ‣ 4.1 Risky-asset dynamics and the 𝛼–dependent drift shift ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise").
The only difference from the standard Merton model is the drift adjustment
μ−r​𝟏↦μIto−r​𝟏.\mu-r\mathbf{1}\mapsto\mu^{\mathrm{Ito}}-r\mathbf{1}.

### 4.3 Optimization problem

As in the one–asset case, admissible controls (ct,θt)(c\_{t},\theta\_{t}) are required to
be progressively measurable, to satisfy ct≥0c\_{t}\geq 0 and at>0a\_{t}>0, and to fulfill
the integrability conditions ([2.6](https://arxiv.org/html/2602.08527v1#S2.E6 "In item 3 ‣ Definition 2.2 (Admissible controls). ‣ 2.2.2 Controls and wealth dynamics ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")), which ensure that the wealth
process is well defined and that the objective functional is finite.

For logarithmic utility, the optimization problem remains time–homogeneous and
Markovian in the wealth variable. We therefore introduce the value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(a,t):=sup(c,θ)𝔼​[∫t∞e−ρ​(s−t)​ln⁡cs​d​s|at=a].J(a,t):=\sup\_{(c,\theta)}\mathbb{E}\!\left[\int\_{t}^{\infty}e^{-\rho(s-t)}\ln c\_{s}\,\mathrm{d}s\;\Big|\;a\_{t}=a\right]. |  | (4.3) |

Standard dynamic programming arguments then yield the Hamilton–Jacobi–Bellman
equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=supc≥0,θ∈ℝn{ln⁡c−ρ​J+Jt+Ja​(a​(r+θ⊤​(μIto−r​𝟏))−c)+12​Ja​a​a2​θ⊤​V​θ}.0=\sup\_{c\geq 0,\ \theta\in\mathbb{R}^{n}}\Big\{\ln c-\rho J+J\_{t}+J\_{a}\bigl(a(r+\theta^{\top}(\mu^{\mathrm{Ito}}-r\mathbf{1}))-c\bigr)+\tfrac{1}{2}J\_{aa}\,a^{2}\,\theta^{\top}V\theta\Big\}. |  | (4.4) |

Compared to the classical Merton HJB, the only modification is the replacement
of the excess–return vector μ−r​𝟏\mu-r\mathbf{1} by its α\alpha–adjusted version
μIto−r​𝟏\mu^{\mathrm{Ito}}-r\mathbf{1}, as identified in
Proposition [4.1](https://arxiv.org/html/2602.08527v1#S4.Thmproposition1 "Proposition 4.1 (Itô form of the 𝛼–interpreted SDE). ‣ 4.1 Risky-asset dynamics and the 𝛼–dependent drift shift ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise").

### 4.4 Optimal policies and value function

The logarithmic utility function preserves the homothetic structure of the
problem even in the presence of multiple risky assets. As a consequence, the
HJB equation admits an explicit solution, and optimal policies can be obtained
in closed form.

###### Theorem 4.1 (Log utility with nn risky assets under α\alpha).

Assume that the covariance matrix V=Σ​Σ⊤V=\Sigma\Sigma^{\top} is positive definite.
Then the optimal consumption rate and portfolio weights are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct∗=ρ​at,θα∗=V−1​(μIto−r​𝟏)=V−1​(μ−r​𝟏)+α​V−1​diag⁡(V)​ 1.c\_{t}^{\*}=\rho\,a\_{t},\qquad\theta\_{\alpha}^{\*}=V^{-1}(\mu^{\mathrm{Ito}}-r\mathbf{1})=V^{-1}(\mu-r\mathbf{1})+\alpha\,V^{-1}\operatorname{diag}(V)\,\mathbf{1}. |  | (4.5) |

The corresponding value function is

|  |  |  |
| --- | --- | --- |
|  | J​(a,t)=(β0+ρ−1​ln⁡a)​e−ρ​t,β0=1ρ​(rρ+ln⁡ρ−1)+12​ρ2​(μIto−r​𝟏)⊤​V−1​(μIto−r​𝟏).J(a,t)=\Bigl(\beta\_{0}+\rho^{-1}\ln a\Bigr)e^{-\rho t},\qquad\beta\_{0}=\frac{1}{\rho}\Bigl(\tfrac{r}{\rho}+\ln\rho-1\Bigr)+\frac{1}{2\rho^{2}}(\mu^{\mathrm{Ito}}-r\mathbf{1})^{\top}V^{-1}(\mu^{\mathrm{Ito}}-r\mathbf{1}). |  |

###### Remark 4.2.

The α\alpha–interpretation modifies optimal portfolio choice exclusively
through an additive shift in the vector of excess returns. In particular, the
correction term

|  |  |  |
| --- | --- | --- |
|  | α​V−1​diag⁡(V)​ 1\alpha\,V^{-1}\operatorname{diag}(V)\,\mathbf{1} |  |

increases risky exposure in each asset in proportion to its marginal variance.
When n=1n=1 and V=σ2V=\sigma^{2}, this reduces to the transparent formula

|  |  |  |
| --- | --- | --- |
|  | θα∗=μ−rσ2+α,\theta^{\*}\_{\alpha}=\frac{\mu-r}{\sigma^{2}}+\alpha, |  |

showing that each unit increase in α\alpha raises the optimal risky position by
one unit.

###### Proof of Theorem [4.1](https://arxiv.org/html/2602.08527v1#S4.Thmtheorem1 "Theorem 4.1 (Log utility with 𝑛 risky assets under 𝛼). ‣ 4.4 Optimal policies and value function ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise").

Let λ:=μIto−r​𝟏\lambda:=\mu^{\mathrm{Ito}}-r\mathbf{1}. Motivated by the homotheticity of
logarithmic utility, we insert the ansatz
J​(a,t)=(β0+β1​ln⁡a)​e−ρ​tJ(a,t)=\bigl(\beta\_{0}+\beta\_{1}\ln a\bigr)e^{-\rho t}
into the HJB equation ([4.4](https://arxiv.org/html/2602.08527v1#S4.E4 "In 4.3 Optimization problem ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")). Dividing out the common factor
e−ρ​te^{-\rho t} yields the reduced Hamiltonian

|  |  |  |
| --- | --- | --- |
|  | ℋ​(c,θ;a)=ln⁡c−β1a​c+β1​r+β1​θ⊤​λ−12​β1​θ⊤​V​θ.\mathcal{H}(c,\theta;a)=\ln c-\tfrac{\beta\_{1}}{a}c+\beta\_{1}r+\beta\_{1}\theta^{\top}\lambda-\tfrac{1}{2}\beta\_{1}\theta^{\top}V\theta. |  |

This expression is strictly concave in (c,θ)(c,\theta), and the first–order
conditions therefore identify the unique maximizers

|  |  |  |
| --- | --- | --- |
|  | c∗​(a)=aβ1,θ∗=V−1​λ.c^{\*}(a)=\frac{a}{\beta\_{1}},\qquad\theta^{\*}=V^{-1}\lambda. |  |

Substituting these expressions back into the HJB equation forces the coefficient
of ln⁡a\ln a to vanish, which yields β1=1/ρ\beta\_{1}=1/\rho, and determines β0\beta\_{0}
uniquely as stated. Positivity of c∗c^{\*} follows from β1>0\beta\_{1}>0, and uniqueness
from strict concavity.
∎

## 5 Factor–driven risky asset with correlated noise under the α\alpha–interpretation

The analysis of Sections [4](https://arxiv.org/html/2602.08527v1#S4 "4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise") shows that, in markets with
constant volatilities, the α\alpha–interpretation can be absorbed into a
deterministic modification of expected returns. From a structural viewpoint,
this raises a natural question: under which modeling assumptions does the
interpretation of stochastic integration have genuinely state–dependent
consequences?

In this section we address this question by introducing a factor–driven
volatility, coupled to the risky return through correlated Brownian noise. This
setting encompasses classical stochastic volatility models and isolates the
precise channel through which the α\alpha–interpretation affects the dynamics:
the instantaneous covariation between the factor and the return. The resulting
corrections to optimal portfolio choice are no longer static, but depend on the
current state of the factor.

### 5.1 Financial market

We now specify the financial market underlying the factor–driven model. The distinguishing
feature of this setting is the presence of an auxiliary factor process whose
fluctuations affect the volatility of the risky asset and are correlated with
the return noise.

We work on a filtered probability space
(Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) supporting a
two–dimensional Brownian motion

|  |  |  |
| --- | --- | --- |
|  | Wt:=(WtS,WtX)⊤,t≥0,W\_{t}:=(W\_{t}^{S},W\_{t}^{X})^{\top},\qquad t\geq 0, |  |

whose components drive, respectively, the risky return and the factor dynamics.
The instantaneous covariance structure is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | [W]t=R​t,R:=(1ϱϱ1),ϱ∈[−1,1].[W]\_{t}=R\,t,\qquad R:=\begin{pmatrix}1&\varrho\\ \varrho&1\end{pmatrix},\qquad\varrho\in[-1,1]. |  | (5.1) |

Equivalently,

|  |  |  |
| --- | --- | --- |
|  | d​⟨WS,WX⟩t=ϱ​d​t,d​⟨WS⟩t=d​⟨WX⟩t=d​t.\mathrm{d}\langle W^{S},W^{X}\rangle\_{t}=\varrho\,\mathrm{d}t,\qquad\mathrm{d}\langle W^{S}\rangle\_{t}=\mathrm{d}\langle W^{X}\rangle\_{t}=\mathrm{d}t. |  |

The correlation parameter ϱ\varrho quantifies the instantaneous coupling
between factor fluctuations and asset returns and will play a central role in
the α\alpha–dependent corrections derived below.

As before, the money–market account b=(bt)t≥0b=(b\_{t})\_{t\geq 0} evolves according to
([2.2](https://arxiv.org/html/2602.08527v1#S2.E2 "In 2.2.1 Assets and source of randomness ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise")). The risky asset S=(St)t≥0S=(S\_{t})\_{t\geq 0} is modeled in the
α\alpha–interpretation by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=μ​(Xt)​d​t+σ​(Xt)∘αd​WtS,\frac{\mathrm{d}S\_{t}}{S\_{t}}=\mu(X\_{t})\,\mathrm{d}t+\sigma(X\_{t})\,\circ\_{\alpha}\mathrm{d}W\_{t}^{S}, |  | (5.2) |

where the drift and volatility depend on the current state of the factor.
Throughout we assume μ,σ∈C1​(ℝ)\mu,\sigma\in C^{1}(\mathbb{R}) and σ​(x)≠0\sigma(x)\neq 0 for all
xx.

The factor process X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} evolves autonomously according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b​(Xt)​d​t+ν​(Xt)∘αd​WtX,\mathrm{d}X\_{t}=b(X\_{t})\,\mathrm{d}t+\nu(X\_{t})\,\circ\_{\alpha}\mathrm{d}W\_{t}^{X}, |  | (5.3) |

with b,ν∈C1​(ℝ)b,\nu\in C^{1}(\mathbb{R}). While XX does not depend on SS directly, the
shared noise structure encoded in ([5.1](https://arxiv.org/html/2602.08527v1#S5.E1 "In 5.1 Financial market ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) induces an indirect
coupling that will become apparent after conversion to Itô form.

Unless stated otherwise, coefficients are chosen so that
([5.2](https://arxiv.org/html/2602.08527v1#S5.E2 "In 5.1 Financial market ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise"))–([5.3](https://arxiv.org/html/2602.08527v1#S5.E3 "In 5.1 Financial market ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) admit unique strong
solutions and all controls are admissible in the sense of
Assumption [2.1](https://arxiv.org/html/2602.08527v1#S2.Thmassumption1 "Assumption 2.1 (Standing assumptions). ‣ 2.1 Filtered probability space and Brownian motion ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise"). In addition, the present section allows for
state dynamics that fall outside the globally Lipschitz framework adopted
earlier, as formalized below.

###### Assumption 5.1.

In Section [5](https://arxiv.org/html/2602.08527v1#S5 "5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise") we allow state dynamics with
coefficients that are not globally Lipschitz (e.g. square–root diffusions),
as is standard in stochastic volatility models.

1. (i)

   Local well–posedness.
   The factor/asset system (in Itô form) admits a unique strong solution up to
   its maximal lifetime τ∈(0,∞]\tau\in(0,\infty].
2. (ii)

   Nonattainment of boundaries / positivity (when relevant).
   In models with a boundary (e.g. Vt≥0V\_{t}\geq 0), parameters are chosen so that the
   boundary is not attained, hence τ=∞\tau=\infty and the state remains in its
   natural domain almost surely.
3. (iii)

   Admissibility of feedback controls.
   The candidate optimal feedback controls derived in this section are admissible,
   i.e. the corresponding wealth process remains strictly positive and satisfies,
   for all T>0T>0,

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[∫0Tπt2​σ​(Xt)2​dt]<∞,𝔼​[∫0Tct​dt]<∞.\mathbb{E}\!\left[\int\_{0}^{T}\pi\_{t}^{2}\sigma(X\_{t})^{2}\,\mathrm{d}t\right]<\infty,\qquad\mathbb{E}\!\left[\int\_{0}^{T}c\_{t}\,\mathrm{d}t\right]<\infty. |  |

### 5.2 Conversion to Itô form

Equation ([5.3](https://arxiv.org/html/2602.08527v1#S5.E3 "In 5.1 Financial market ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) is equivalent to the Itô SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(b​(Xt)+α​ν​(Xt)​ν′​(Xt))​d​t+ν​(Xt)​d​WtX.\mathrm{d}X\_{t}=\Big(b(X\_{t})+\alpha\,\nu(X\_{t})\nu^{\prime}(X\_{t})\Big)\mathrm{d}t+\nu(X\_{t})\,\mathrm{d}W\_{t}^{X}. |  | (5.4) |

For the risky asset, note that the diffusion coefficient is St​σ​(Xt)S\_{t}\sigma(X\_{t})
driven by WSW^{S}. Since XX and WSW^{S} have nonzero quadratic covariation whenever
ϱ≠0\varrho\neq 0, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨σ​(X),WS⟩t=σ′​(Xt)​d​⟨X,WS⟩t.\mathrm{d}\langle\sigma(X),W^{S}\rangle\_{t}=\sigma^{\prime}(X\_{t})\,\mathrm{d}\langle X,W^{S}\rangle\_{t}. |  | (5.5) |

From ([5.4](https://arxiv.org/html/2602.08527v1#S5.E4 "In 5.2 Conversion to Itô form ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) and ([5.1](https://arxiv.org/html/2602.08527v1#S5.E1 "In 5.1 Financial market ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")), the martingale part of XX
is ∫0tν​(Xs)​dWsX\int\_{0}^{t}\nu(X\_{s})\mathrm{d}W\_{s}^{X}, hence

|  |  |  |
| --- | --- | --- |
|  | d​⟨X,WS⟩t=d​⟨∫0⋅ν​(Xs)​dWsX,WS⟩t=ν​(Xt)​d​⟨WX,WS⟩t=ϱ​ν​(Xt)​d​t.\mathrm{d}\langle X,W^{S}\rangle\_{t}=\mathrm{d}\Big\langle\int\_{0}^{\cdot}\nu(X\_{s})\mathrm{d}W\_{s}^{X},\,W^{S}\Big\rangle\_{t}=\nu(X\_{t})\,\mathrm{d}\langle W^{X},W^{S}\rangle\_{t}=\varrho\,\nu(X\_{t})\,\mathrm{d}t. |  |

Substituting into ([5.5](https://arxiv.org/html/2602.08527v1#S5.E5 "In 5.2 Conversion to Itô form ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) yields

|  |  |  |
| --- | --- | --- |
|  | d​⟨σ​(X),WS⟩t=ϱ​σ′​(Xt)​ν​(Xt)​d​t.\mathrm{d}\langle\sigma(X),W^{S}\rangle\_{t}=\varrho\,\sigma^{\prime}(X\_{t})\nu(X\_{t})\,\mathrm{d}t. |  |

Therefore ([5.2](https://arxiv.org/html/2602.08527v1#S5.E2 "In 5.1 Financial market ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) is equivalent to the Itô SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=(μ​(Xt)+α​ϱ​σ′​(Xt)​ν​(Xt))​d​t+σ​(Xt)​d​WtS.\frac{\mathrm{d}S\_{t}}{S\_{t}}=\Big(\mu(X\_{t})+\alpha\,\varrho\,\sigma^{\prime}(X\_{t})\nu(X\_{t})\Big)\mathrm{d}t+\sigma(X\_{t})\,\mathrm{d}W\_{t}^{S}. |  | (5.6) |

###### Remark 5.1 (When does α\alpha matter?).

If ϱ=0\varrho=0 (independent factor and return shocks), then the α\alpha–dependent
drift correction in ([5.6](https://arxiv.org/html/2602.08527v1#S5.E6 "In 5.2 Conversion to Itô form ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) vanishes. Thus, in the present class of
factor models, the α\alpha–interpretation affects optimal portfolio choice only through
the *noise correlation* between the factor and the risky return.

### 5.3 Wealth dynamics

We next derive the wealth dynamics induced by the factor–dependent asset
returns. Let AtA\_{t} denote the investor’s wealth at time tt, and let πt\pi\_{t}
denote the fraction of wealth invested in the risky asset, with the remainder
invested in the money–market account. As before, ctc\_{t} denotes the consumption
rate.

Under the self–financing constraint, and using the Itô form of the asset
dynamics derived above, the wealth process satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​AtAt=(r+πt​(μeff​(Xt)−r)−ctAt)​d​t+πt​σ​(Xt)​d​WtS,\frac{\mathrm{d}A\_{t}}{A\_{t}}=\Big(r+\pi\_{t}\big(\mu\_{\mathrm{eff}}(X\_{t})-r\big)-\frac{c\_{t}}{A\_{t}}\Big)\mathrm{d}t+\pi\_{t}\sigma(X\_{t})\,\mathrm{d}W\_{t}^{S}, |  | (5.7) |

where the *effective return drift* is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μeff​(x):=μ​(x)+α​ϱ​σ′​(x)​ν​(x).\mu\_{\mathrm{eff}}(x):=\mu(x)+\alpha\,\varrho\,\sigma^{\prime}(x)\nu(x). |  | (5.8) |

Relative to the constant–volatility case, the structure of the wealth equation
is unchanged. All effects of the α\alpha–interpretation are captured by the
state–dependent drift correction μeff​(Xt)−μ​(Xt)\mu\_{\mathrm{eff}}(X\_{t})-\mu(X\_{t}), which
originates from the interaction between the factor dynamics and the correlated
return noise. In particular, when ϱ=0\varrho=0 the effective drift coincides with
the original drift, and the α\alpha–interpretation has no impact on the wealth
dynamics.

### 5.4 Logarithmic utility maximization

We now consider the investor’s optimal consumption–investment problem in the
factor–driven market. The objective is to maximize discounted expected utility
of consumption,

|  |  |  |
| --- | --- | --- |
|  | sup(π,c)𝔼​[∫0∞e−ρ​t​log⁡(ct)​dt],ρ>0,\sup\_{(\pi,c)}\mathbb{E}\Bigg[\int\_{0}^{\infty}e^{-\rho t}\log(c\_{t})\,\mathrm{d}t\Bigg],\qquad\rho>0, |  |

over admissible controls (πt,ct)(\pi\_{t},c\_{t}).

Despite the presence of a stochastic factor, the problem retains a simple
structure under logarithmic utility. In particular, log utility eliminates
intertemporal hedging motives and preserves homotheticity in wealth. Motivated
by this observation, we seek a value function of the separable form

|  |  |  |
| --- | --- | --- |
|  | V​(a,x)=log⁡a+v​(x),V(a,x)=\log a+v(x), |  |

where vv accounts for the contribution of the factor process.

Substituting this ansatz into the associated Hamilton–Jacobi–Bellman equation
and optimizing pointwise with respect to cc and π\pi yields the first–order
conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct∗=ρ​At,πt∗=μeff​(Xt)−rσ​(Xt)2.c\_{t}^{\ast}=\rho A\_{t},\qquad\pi\_{t}^{\ast}=\frac{\mu\_{\mathrm{eff}}(X\_{t})-r}{\sigma(X\_{t})^{2}}. |  | (5.9) |

Using the explicit form of the effective drift ([5.8](https://arxiv.org/html/2602.08527v1#S5.E8 "In 5.3 Wealth dynamics ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")), the
optimal risky fraction can be decomposed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt∗=μ​(Xt)−rσ​(Xt)2+α​ϱ​σ′​(Xt)​ν​(Xt)σ​(Xt)2.\pi\_{t}^{\ast}=\frac{\mu(X\_{t})-r}{\sigma(X\_{t})^{2}}+\alpha\,\varrho\,\frac{\sigma^{\prime}(X\_{t})\nu(X\_{t})}{\sigma(X\_{t})^{2}}. |  | (5.10) |

The first term coincides with the classical myopic demand evaluated at the
current factor level. The second term is the genuine α\alpha–correction,
originating from the interaction between the factor dynamics and the correlated
return noise.

This correction vanishes in each of the following cases: (i) the volatility
coefficient σ\sigma is constant, so that factor fluctuations do not affect the
return variance; (ii) the factor has no diffusive component (ν≡0\nu\equiv 0); or
(iii) the factor and return noises are uncorrelated (ϱ=0\varrho=0). In all three
situations, the α\alpha–interpretation has no effect on optimal portfolio
choice, and the problem reduces to the classical Merton setting.

### 5.5 Example: Heston stochastic volatility

We illustrate the mechanism identified above by specializing to the Heston
stochastic volatility model, which provides a canonical example of a
factor–driven risky asset with correlated noise. In this setting, the factor
process represents the instantaneous variance of returns, and correlation
between return and variance shocks is an empirically well–established feature
of financial markets.

We take the factor to be the variance process VtV\_{t} and set Xt=VtX\_{t}=V\_{t}, with
coefficients

|  |  |  |
| --- | --- | --- |
|  | σ​(v)=v,b​(v)=κ​(θ−v),ν​(v)=ξ​v,\sigma(v)=\sqrt{v},\qquad b(v)=\kappa(\theta-v),\qquad\nu(v)=\xi\sqrt{v}, |  |

where κ,θ,ξ>0\kappa,\theta,\xi>0 and V0>0V\_{0}>0. The resulting α\alpha–interpreted
dynamics are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​StSt\displaystyle\frac{\mathrm{d}S\_{t}}{S\_{t}} | =μ​d​t+Vt∘αd​WtS,\displaystyle=\mu\,\mathrm{d}t+\sqrt{V\_{t}}\,\circ\_{\alpha}\mathrm{d}W\_{t}^{S}, |  | (5.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Vt\displaystyle\mathrm{d}V\_{t} | =κ​(θ−Vt)​d​t+ξ​Vt∘αd​WtX,\displaystyle=\kappa(\theta-V\_{t})\,\mathrm{d}t+\xi\sqrt{V\_{t}}\,\circ\_{\alpha}\mathrm{d}W\_{t}^{X}, |  | (5.12) |

with d​⟨WS,WX⟩t=ϱ​d​t\mathrm{d}\langle W^{S},W^{X}\rangle\_{t}=\varrho\,\mathrm{d}t.

In the Heston case the α\alpha–dependent corrections can be computed explicitly.
Since σ′​(v)=12​v\sigma^{\prime}(v)=\frac{1}{2\sqrt{v}} and ν​(v)=ξ​v\nu(v)=\xi\sqrt{v}, we have
σ′​(v)​ν​(v)=ξ/2\sigma^{\prime}(v)\nu(v)=\xi/2, which is constant. As a consequence, the Itô form of
([5.11](https://arxiv.org/html/2602.08527v1#S5.E11 "In 5.5 Example: Heston stochastic volatility ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=(μ+α​ϱ​ξ2)​d​t+Vt​d​WtS.\frac{\mathrm{d}S\_{t}}{S\_{t}}=\Big(\mu+\alpha\,\varrho\,\frac{\xi}{2}\Big)\mathrm{d}t+\sqrt{V\_{t}}\,\mathrm{d}W\_{t}^{S}. |  | (5.13) |

Thus, in contrast to the general factor model, the α\alpha–interpretation
induces a constant shift in the effective expected return.

For the variance process, the identity
ν​(v)​ν′​(v)=ξ2/2\nu(v)\nu^{\prime}(v)=\xi^{2}/2 shows that ([5.12](https://arxiv.org/html/2602.08527v1#S5.E12 "In 5.5 Example: Heston stochastic volatility ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt=(κ​(θ−Vt)+α​ξ22)​d​t+ξ​Vt​d​WtX.\mathrm{d}V\_{t}=\Big(\kappa(\theta-V\_{t})+\alpha\,\frac{\xi^{2}}{2}\Big)\mathrm{d}t+\xi\sqrt{V\_{t}}\,\mathrm{d}W\_{t}^{X}. |  | (5.14) |

Equivalently, the drift can be rewritten as κ​(θα−Vt)\kappa(\theta\_{\alpha}-V\_{t}) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | θα:=θ+α​ξ22​κ.\theta\_{\alpha}:=\theta+\alpha\,\frac{\xi^{2}}{2\kappa}. |  | (5.15) |

The α\alpha–interpretation therefore shifts the long–run mean of the variance
process while preserving its CIR structure.

In this model the effective return drift ([5.8](https://arxiv.org/html/2602.08527v1#S5.E8 "In 5.3 Wealth dynamics ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")) reduces to
the constant

|  |  |  |
| --- | --- | --- |
|  | μeff=μ+α​ϱ​ξ2.\mu\_{\mathrm{eff}}=\mu+\alpha\,\varrho\,\frac{\xi}{2}. |  |

Consequently, optimal consumption remains proportional to wealth, while the
optimal risky fraction takes the explicit form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct∗=ρ​At,πt∗=μeff−rVt=μ−rVt+α​ϱ​ξ2​1Vt.c\_{t}^{\ast}=\rho A\_{t},\qquad\pi\_{t}^{\ast}=\frac{\mu\_{\mathrm{eff}}-r}{V\_{t}}=\frac{\mu-r}{V\_{t}}+\alpha\,\varrho\,\frac{\xi}{2}\,\frac{1}{V\_{t}}. |  | (5.16) |

The α\alpha–correction thus scales inversely with the current variance level:
it is amplified during low–volatility periods and becomes negligible when
volatility is high.

Since πt∗\pi\_{t}^{\ast} grows like 1/Vt1/V\_{t}, admissibility requires strict positivity
of the variance process and sufficient integrability of 1/Vt1/V\_{t}. A classical
sufficient condition ensuring that the boundary V=0V=0 is not attained is the Feller (see [[8](https://arxiv.org/html/2602.08527v1#bib.bib65 "A theory of the term structure of interest rates")]) for the CIR process ([5.14](https://arxiv.org/html/2602.08527v1#S5.E14 "In 5.5 Example: Heston stochastic volatility ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")),

|  |  |  |
| --- | --- | --- |
|  | 2​κ​θα≥ξ2,2\kappa\theta\_{\alpha}\geq\xi^{2}, |  |

with θα\theta\_{\alpha} given by ([5.15](https://arxiv.org/html/2602.08527v1#S5.E15 "In 5.5 Example: Heston stochastic volatility ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise")).

## Appendix A A dictionary between noise interpretations

In the main text we formulate asset–price dynamics using stochastic differential
equations written in the α\alpha–interpretation, where the stochastic integral
∘α\circ\_{\alpha} interpolates between Itô (α=0\alpha=0), Stratonovich
(α=12\alpha=\tfrac{1}{2}), and Klimontovich (α=1\alpha=1) conventions. For the
consumption–investment problem studied in this paper, we focus on geometric
Brownian motion, which corresponds to the simplest instance of multiplicative
noise and allows for closed–form solutions.

The purpose of this appendix is to place this choice within a broader modelling
framework. We collect general conversion formulas that allow one to translate
an SDE written under a given interpretation into an equivalent SDE under another
interpretation, for diffusion coefficients beyond the geometric Brownian case.
These dictionaries enable the reader to understand how changes in noise
interpretation modify effective drift terms for more general stock price
dynamics, and thus how the analysis of the main text can be extended to
alternative multiplicative or state–dependent volatility structures. The drift
corrections derived here underlie, as a special case, the shifts used in
Sections [2.2](https://arxiv.org/html/2602.08527v1#S2.SS2 "2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise") and [4](https://arxiv.org/html/2602.08527v1#S4 "4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise").

### A.1 General α→γ\alpha\to\gamma conversion

Let W=(Wt)t≥0W=(W\_{t})\_{t\geq 0} be an mm–dimensional Brownian motion on the filtered
probability space specified in Section [2.1](https://arxiv.org/html/2602.08527v1#S2.SS1 "2.1 Filtered probability space and Brownian motion ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise"), and consider the
dd–dimensional SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b​(Xt)​d​t+Σ​(Xt)∘αd​Wt,\mathrm{d}X\_{t}=b(X\_{t})\,\mathrm{d}t+\Sigma(X\_{t})\,\circ\_{\alpha}\mathrm{d}W\_{t}, |  | (A.1) |

where b:ℝd→ℝdb:\mathbb{R}^{d}\to\mathbb{R}^{d} and Σ:ℝd→ℝd×m\Sigma:\mathbb{R}^{d}\to\mathbb{R}^{d\times m} are sufficiently smooth
(e.g. C2C^{2} with bounded derivatives), and ∘α\circ\_{\alpha} denotes integration in
the α\alpha–interpretation.

Writing ([A.1](https://arxiv.org/html/2602.08527v1#A1.E1 "In A.1 General 𝛼→𝛾 conversion ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")) in Itô form corresponds to the special
case γ=0\gamma=0 in the following general dictionary.

###### Proposition A.1 (Conversion between α\alpha– and γ\gamma–interpretations).

Fix α,γ∈[0,1]\alpha,\gamma\in[0,1] and let XX solve ([A.1](https://arxiv.org/html/2602.08527v1#A1.E1 "In A.1 General 𝛼→𝛾 conversion ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")).
Then XX also solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b~​(Xt)​d​t+Σ​(Xt)∘γd​Wt,\mathrm{d}X\_{t}=\widetilde{b}(X\_{t})\,\mathrm{d}t+\Sigma(X\_{t})\,\circ\_{\gamma}\mathrm{d}W\_{t}, |  | (A.2) |

where the drift b~\widetilde{b} is given componentwise by

|  |  |  |  |
| --- | --- | --- | --- |
|  | b~i​(x)=bi​(x)+(α−γ)​∑k=1m∑j=1dΣj​k​(x)​∂xjΣi​k​(x),i=1,…,d.\widetilde{b}\_{i}(x)=b\_{i}(x)+(\alpha-\gamma)\sum\_{k=1}^{m}\sum\_{j=1}^{d}\Sigma\_{jk}(x)\,\partial\_{x\_{j}}\Sigma\_{ik}(x),\qquad i=1,\dots,d. |  | (A.3) |

Equivalently, the diffusion coefficient Σ​(x)\Sigma(x) is unchanged, while the
drift is shifted by

|  |  |  |
| --- | --- | --- |
|  | b~​(x)=b​(x)+(α−γ)​c​(x),ci​(x):=∑k,jΣj​k​(x)​∂xjΣi​k​(x).\widetilde{b}(x)=b(x)+(\alpha-\gamma)\,c(x),\qquad c\_{i}(x):=\sum\_{k,j}\Sigma\_{jk}(x)\,\partial\_{x\_{j}}\Sigma\_{ik}(x). |  |

###### Proof sketch.

The proof is standard and relies on writing both α\alpha– and γ\gamma–integrals
as limits of Riemann sums with evaluation at intermediate points of each time
interval. For smooth Σ\Sigma, the difference between the two evaluations can be
expanded to first order and expressed in terms of the quadratic covariation of
XX and WW. This yields the correction term proportional to
(α−γ)​∑j,kΣj​k​∂xjΣi​k(\alpha-\gamma)\sum\_{j,k}\Sigma\_{jk}\partial\_{x\_{j}}\Sigma\_{ik}.
Rigorous derivations can be found, for example, in classical references on
generalised stochastic integrals.
∎

The Itô form of ([A.1](https://arxiv.org/html/2602.08527v1#A1.E1 "In A.1 General 𝛼→𝛾 conversion ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")) corresponds to γ=0\gamma=0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(b​(Xt)+α​c​(Xt))​d​t+Σ​(Xt)​d​Wt,ci​(x)=∑k,jΣj​k​(x)​∂xjΣi​k​(x).\mathrm{d}X\_{t}=\Bigl(b(X\_{t})+\alpha\,c(X\_{t})\Bigr)\mathrm{d}t+\Sigma(X\_{t})\,\mathrm{d}W\_{t},\qquad c\_{i}(x)=\sum\_{k,j}\Sigma\_{jk}(x)\,\partial\_{x\_{j}}\Sigma\_{ik}(x). |  | (A.4) |

Similarly, the Stratonovich form is obtained by taking γ=12\gamma=\tfrac{1}{2}, and
the Klimontovich form by taking γ=1\gamma=1.

###### Remark A.1 (Correlated Brownian motions).

The conversion formulas above are stated for an mm–dimensional Brownian motion
WW with identity covariance, i.e. [W]t=Im​t[W]\_{t}=I\_{m}\,t. This entails no loss of
generality.

Indeed, if W~\widetilde{W} is an mm–dimensional Brownian motion with constant
covariance matrix RR, one may write W~=C​W\widetilde{W}=CW for some deterministic
matrix CC satisfying C​C⊤=RCC^{\top}=R. Rewriting
([A.1](https://arxiv.org/html/2602.08527v1#A1.E1 "In A.1 General 𝛼→𝛾 conversion ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")) in terms of WW replaces the diffusion coefficient
Σ​(x)\Sigma(x) by Σ​(x)​C\Sigma(x)C, and the conversion formula
([A.3](https://arxiv.org/html/2602.08527v1#A1.E3 "In Proposition A.1 (Conversion between 𝛼– and 𝛾–interpretations). ‣ A.1 General 𝛼→𝛾 conversion ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")) applies verbatim.

In particular, in the factor–driven model of
Section [5](https://arxiv.org/html/2602.08527v1#S5 "5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise"), the additional drift term
α​ϱ​σ′​(x)​ν​(x)\alpha\,\varrho\,\sigma^{\prime}(x)\nu(x) arises precisely from this covariance
structure.

### A.2 Diagonal–multiplicative noise

In the main body of the paper we work with a class of multiplicative diffusion
models in which each risky asset is affected by a common vector of Brownian
shocks, but with volatility proportional to its own price level.
Let St=(St1,…,Stn)∈(0,∞)nS\_{t}=(S\_{t}^{1},\dots,S\_{t}^{n})\in(0,\infty)^{n} denote the vector of risky asset
prices, let μ∈ℝn\mu\in\mathbb{R}^{n} be a constant drift vector, and let
Γ∈ℝn×n\Gamma\in\mathbb{R}^{n\times n} be a constant volatility loading matrix.
We consider the α\alpha–interpreted SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=D​(St)​(μ​d​t+Γ∘αd​Wt),\mathrm{d}S\_{t}=\mathrm{D}(S\_{t})\Bigl(\mu\,\mathrm{d}t+\Gamma\,\circ\_{\alpha}\mathrm{d}W\_{t}\Bigr), |  | (A.5) |

where D​(S)=diag⁡(S1,…,Sn)\mathrm{D}(S)=\operatorname{diag}(S^{1},\dots,S^{n}) and WtW\_{t} is an nn–dimensional
Brownian motion.

Equivalently, in components,

|  |  |  |
| --- | --- | --- |
|  | d​Sti=Sti​(μi​d​t+∑k=1nΓi​k∘αd​Wtk),i=1,…,n.\mathrm{d}S\_{t}^{i}=S\_{t}^{i}\left(\mu\_{i}\,\mathrm{d}t+\sum\_{k=1}^{n}\Gamma\_{ik}\,\circ\_{\alpha}\mathrm{d}W\_{t}^{k}\right),\qquad i=1,\dots,n. |  |

The diffusion coefficient in ([A.5](https://arxiv.org/html/2602.08527v1#A1.E5 "In A.2 Diagonal–multiplicative noise ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")) is the matrix–valued
function

|  |  |  |
| --- | --- | --- |
|  | B​(S):=D​(S)​Γ∈ℝn×n,B(S):=\mathrm{D}(S)\Gamma\in\mathbb{R}^{n\times n}, |  |

with components

|  |  |  |
| --- | --- | --- |
|  | Bi​k​(S)=Si​Γi​k.B\_{ik}(S)=S^{i}\,\Gamma\_{ik}. |  |

In particular, the ii–th *row* of B​(S)B(S) depends only on the component
SiS^{i}, a structural property that will be crucial in the computation of the
α\alpha–to–Itô drift correction.

Define the constant covariance matrix

|  |  |  |
| --- | --- | --- |
|  | V:=Γ​Γ⊤∈ℝn×n,Vi​j=∑k=1nΓi​k​Γj​k.V:=\Gamma\Gamma^{\top}\in\mathbb{R}^{n\times n},\qquad V\_{ij}=\sum\_{k=1}^{n}\Gamma\_{ik}\Gamma\_{jk}. |  |

Applying the general conversion formula
([A.4](https://arxiv.org/html/2602.08527v1#A1.E4 "In A.1 General 𝛼→𝛾 conversion ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")) to ([A.5](https://arxiv.org/html/2602.08527v1#A1.E5 "In A.2 Diagonal–multiplicative noise ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")), we obtain that
the Itô drift correction has components

|  |  |  |
| --- | --- | --- |
|  | ci​(S):=∑j=1n∑k=1nBj​k​(S)​∂SjBi​k​(S).c\_{i}(S):=\sum\_{j=1}^{n}\sum\_{k=1}^{n}B\_{jk}(S)\,\partial\_{S^{j}}B\_{ik}(S). |  |

Since Bi​k​(S)=Si​Γi​kB\_{ik}(S)=S^{i}\Gamma\_{ik}, we have

|  |  |  |
| --- | --- | --- |
|  | ∂SjBi​k​(S)=Γi​k​δi​j,\partial\_{S^{j}}B\_{ik}(S)=\Gamma\_{ik}\,\delta\_{ij}, |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | ci​(S)=∑k=1nBi​k​(S)​Γi​k=Si​∑k=1nΓi​k2=Si​Vi​i,i=1,…,n.c\_{i}(S)=\sum\_{k=1}^{n}B\_{ik}(S)\Gamma\_{ik}=S^{i}\sum\_{k=1}^{n}\Gamma\_{ik}^{2}=S^{i}\,V\_{ii},\qquad i=1,\dots,n. |  |

The α\alpha–interpreted SDE ([A.5](https://arxiv.org/html/2602.08527v1#A1.E5 "In A.2 Diagonal–multiplicative noise ‣ Appendix A A dictionary between noise interpretations ‣ Consumption–Investment with anticipative noise")) is thus equivalent to
the Itô SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=D​(St)​(μIto​d​t+Γ​d​Wt),μIto:=μ+α​diag⁡(V).\mathrm{d}S\_{t}=\mathrm{D}(S\_{t})\Bigl(\mu^{\mathrm{Ito}}\,\mathrm{d}t+\Gamma\,\mathrm{d}W\_{t}\Bigr),\qquad\mu^{\mathrm{Ito}}:=\mu+\alpha\,\operatorname{diag}(V). |  | (A.6) |

This coincides exactly with Proposition [4.1](https://arxiv.org/html/2602.08527v1#S4.Thmproposition1 "Proposition 4.1 (Itô form of the 𝛼–interpreted SDE). ‣ 4.1 Risky-asset dynamics and the 𝛼–dependent drift shift ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise") in
Section [4](https://arxiv.org/html/2602.08527v1#S4 "4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise").

More generally, changing the interpretation parameter from α\alpha to
γ\gamma leaves the diffusion term unchanged and shifts the drift according to

|  |  |  |
| --- | --- | --- |
|  | μIto⟼μIto+(α−γ)​diag⁡(V).\mu^{\mathrm{Ito}}\;\longmapsto\;\mu^{\mathrm{Ito}}+(\alpha-\gamma)\,\operatorname{diag}(V). |  |

In particular, moving from Itô to Stratonovich adds
12​diag⁡(V)\tfrac{1}{2}\operatorname{diag}(V) to the drift, while moving from Itô to Klimontovich adds
diag⁡(V)\operatorname{diag}(V).

###### Remark A.2.

From the perspective of the consumption–investment problem, this dictionary
justifies treating different noise interpretations as changes in effective
expected returns, while keeping both the volatility structure and the
self–financing constraint unchanged. This mechanism is responsible for the
shift

|  |  |  |
| --- | --- | --- |
|  | θα∗=V−1​(μ−r​𝟏)+α​V−1​diag⁡(V)​𝟏\theta^{\*}\_{\alpha}=V^{-1}(\mu-r\mathbf{1})+\alpha V^{-1}\operatorname{diag}(V)\mathbf{1} |  |

in the optimal risky portfolio derived in
Theorem [4.1](https://arxiv.org/html/2602.08527v1#S4.Thmtheorem1 "Theorem 4.1 (Log utility with 𝑛 risky assets under 𝛼). ‣ 4.4 Optimal policies and value function ‣ 4 𝑛 risky assets under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise").

## References

* [1]
  Y. Aït-Sahalia and D. Yu (2009)
  High frequency market microstructure noise estimates and liquidity measures.
  The Annals of Applied Statistics 3 (1),  pp. 422–457.
  External Links: [Document](https://dx.doi.org/10.1214/08-AOAS203)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p4.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [2]
  M. Ayala, N. Dirr, G. A. Pavliotis, and J. Zimmer (2025)
  Reversibility, covariance and coarse-graining for langevin dynamics: on the choice of multiplicative noise.
  arXiv preprint arXiv:2511.03347.
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p5.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [3]
  C. Bender (2003)
  An itô formula for a fractional stratonovich type integral with arbitrary hurst parameter and stratonovich self-financing arbitrage.
  Preprint, Department of Mathematics, University of Konstanz.
  Note: Available at [https://www.math.uni-konstanz.de/˜kohlmann/ftp/dp02\_07.pdf](https://www.math.uni-konstanz.de/~kohlmann/ftp/dp02_07.pdf)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p5.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [4]
  F. E. Benth (2001)
  Option theory with stochastic volatility and jumps.
  (Journal details to be completed).
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [5]
  P. Boyle, R. C. Merton, and W. Samuelson (1992)
  On the relation between continuous and discrete-time portfolio problems.
  (Journal details to be completed).
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [6]
  A. Cartea, S. Jaimungal, and J. Penalva (2015)
  Algorithmic and high-frequency trading.
   Cambridge University Press.
  External Links: [Document](https://dx.doi.org/10.1017/CBO9781139137046)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p4.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [7]
  P. Cheridito (2003)
  Arbitrage in fractional brownian motion models.
  Finance and stochastics 7 (4),  pp. 533–553.
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p5.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [8]
  J. C. Cox, J. E. Ingersoll, S. A. Ross, et al. (1985)
  A theory of the term structure of interest rates.
  Econometrica 53 (2),  pp. 385–407.
  Cited by: [§5.5](https://arxiv.org/html/2602.08527v1#S5.SS5.p6.4 "5.5 Example: Heston stochastic volatility ‣ 5 Factor–driven risky asset with correlated noise under the 𝛼–interpretation ‣ Consumption–Investment with anticipative noise").
* [9]
  M. H. A. Davis and A. R. Norman (1990)
  Portfolio selection with transaction costs.
  Mathematics of Operations Research 15 (4),  pp. 676–713.
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [10]
  G. dos Reis and A. Platonov (2021)
  On the relation between stratonovich and itô integrals with functional integrands.
  Journal of Stochastic Analysis.
  Note: Available at <https://arxiv.org/abs/2105.14793>
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p4.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [11]
  F. J. Fabozzi, S. M. Focardi, and C. Jonas (2011)
  High-frequency trading: methodologies and market impact.
  The Journal of Portfolio Management 37 (2),  pp. 33–44.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2011.37.2.033)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p4.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [12]
  P. R. Hansen and A. Lunde (2006)
  Realized variance and market microstructure noise.
  Journal of Business Economic Statistics 24 (2),  pp. 127–161.
  External Links: [Document](https://dx.doi.org/10.1198/073500106000000024)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p4.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [13]
  S. L. Heston (1993)
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  The review of financial studies 6 (2),  pp. 327–343.
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.SSx1.p4.1 "Contribution ‣ 1 Introduction ‣ Consumption–Investment with anticipative noise").
* [14]
  H. Kraft and M. Steffensen (2008)
  Optimal consumption and insurance: a continuous-time markov chain approach.
  ASTIN Bulletin: The Journal of the IAA 38 (1),  pp. 231–257.
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [15]
  R. C. Merton (1969)
  Lifetime portfolio selection under uncertainty: the continuous‐time case.
  The Review of Economics and Statistics 51 (3),  pp. 247–257.
  External Links: [Document](https://dx.doi.org/10.2307/1926560)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p1.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [16]
  R. C. Merton (1971)
  Optimum consumption and portfolio rules in a continuous‐time model.
  Journal of Economic Theory 3 (4),  pp. 373–413.
  External Links: [Document](https://dx.doi.org/10.1016/0022-0531%2871%2990038-X)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p1.1 "1 Introduction ‣ Consumption–Investment with anticipative noise"),
  [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [17]
  R. C. Merton (1975)
  Optimum consumption and portfolio rules in a continuous-time model.
  In Stochastic optimization models in finance,
   pp. 621–661.
  Cited by: [§2.2](https://arxiv.org/html/2602.08527v1#S2.SS2.p1.2 "2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise"),
  [Remark 2.4](https://arxiv.org/html/2602.08527v1#S2.Thmremark4.p1.1 "Remark 2.4. ‣ 2.2.3 Utility maximization problem ‣ 2.2 Classical one–asset consumption–investment problem ‣ 2 Preliminaries ‣ Consumption–Investment with anticipative noise").
* [18]
  N. Moehle and S. Boyd (2021)
  Dynamic stochastic portfolio optimization with transaction costs and constraints.
  (Journal details to be completed).
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [19]
  B. Vallejo-Jiménez, F. Venegas-Martínez, and Y. V. Soriano-Morales (2015)
  Optimal consumption and portfolio decisions when the risky asset is driven by a time-inhomogeneous markov modulated diffusion process.
  International Journal of Pure and Applied Mathematics 104 (3),  pp. 353–362.
  External Links: [Link](https://www.researchgate.net/publication/284887406_Optimal_consumption_and_portfolio_decisions_when_the_risky_asset_is_driven_by_a_time-inhomogeneous_Markov_modulated_diffusion_process)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [20]
  B. Vallejo-Jiménez and F. Venegas-Martínez (2017)
  Closed-form consumption–investment rules under markov-modulated preferences.
  Economics Bulletin 37 (1),  pp. 230–239.
  External Links: [Link](http://www.accessecon.com/Pubs/EB/2017/Volume37/EB-17-V37-I1-P28.pdf)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [21]
  F. Venegas-Martínez and coauthors (2022)
  Consumption and portfolio rules with stochastic dynamics driven by markov switching processes.
  Mathematics 10 (16),  pp. 2926.
  External Links: [Document](https://dx.doi.org/10.3390/math10162926),
  [Link](https://www.mdpi.com/2227-7390/10/16/2926)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p2.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").
* [22]
  R. Yuan and P. Ao (2012)
  Beyond itô versus stratonovich.
  Journal of Statistical Mechanics: Theory and Experiment,  pp. P07010.
  External Links: [Document](https://dx.doi.org/10.1088/1742-5468/2012/07/P07010)
  Cited by: [§1](https://arxiv.org/html/2602.08527v1#S1.p4.1 "1 Introduction ‣ Consumption–Investment with anticipative noise").