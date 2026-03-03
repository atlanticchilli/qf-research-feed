---
authors:
- Bernhard K Meister
doc_id: arxiv:2603.00361v1
family_id: arxiv:2603.00361
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Market Dynamics of Information Avalanches
url_abs: http://arxiv.org/abs/2603.00361v1
url_html: https://arxiv.org/html/2603.00361v1
venue: arXiv q-fin
version: 1
year: 2026
---


B. K. Meister
[bernhard.k.meister@gmail.com](2603.00361v1/mailto:bernhard.k.meister@gmail.com)

###### Abstract

Financial markets convert the incremental arrival of information into asset price changes.
In a sandpile model grains of sand represent bits of data, and the size of an avalanche, governed by a scaling law, is linked to price volatility.
While this model of self-organized criticality reproduces stylized facts, it also identifies a structural tension between the non-arbitrage condition and price adjustments consistent with a constant Sharpe ratio.

## I Introduction

> He had bought a large map representing the sea,
>   
>  Without the least vestige of land:
>   
>  And the crew were much pleased when they found it to be
>   
>  A map they could all understand

A sandpile model[bak](#bib.bib2)  simulates the arrival and processing of information. Bits of data replace grains of sand; otherwise the Bak-Tang-Wiesenfeld mechanism111The Kuramoto model of synchronization offers an alternative to the Bak-Tang-Wiesenfeld sandpile.
An early description of synchronization dynamics was given by Christiaan Huygens, who observed in 1665 that two pendulum clocks suspended from a wooden beam would soon move in ‘sympathy’. To test the coupling, he introduced obstructions and separated them to desynchronize, only to find that, when brought back to the common support, the cadence re-established within half an hour. stays unchanged. Through a steady inflow the sandpile is driven towards self-organised criticality (SOC). It leads to avalanches that follow a scaling law. The step from informational propensities, to use a term coined by Popper, to market influence itself is achieved via avalanches, and temporarily bumps up price volatility. Therefore, a financial market can be viewed as physical system that processes granular information.

The paper builds on the geometric foundations established in the companion paper[meister2026b](#bib.bib5) , which showed that finite-resource observability forces markets into the exponential family. In the current paper, we look at Gaussians described in the one dimensional asset case by drift and volatility - a two dimensional manifold.
Here we ask: what are the dynamics on the manifold?

Desynchronization occurs, when market’s rapid geodesic flow - propelled by information avalanches in a state of SOC - meets the lagging response of (central) bankers.
Markets can be viewed as multi-layered:

Layer 1: The Static View.
:   Static equilibrium – a fixed point in the exponential family.

Layer 2: The Sandpile Flow.
:   Motion on the equilibrium manifold. The system moves along paths on the upper half-plane, with coordinates (μ,σ)(\mu,\sigma). Rapid traversals of these geodesics in the non-arbitrage case are responses to avalanches. The Bankers lag behind, when volatility leaps.

Layer 3: The Non-Equilibrium Extension.
:   Limited Onsager excursions slightly off the manifold, governed by detailed balance, which return via linear response.

Bankers’ lag belongs to Layer 2. The market does not have to break down for conventional methods to fail.

To simplify, we introduce a slowly varying Sharpe ratio that ties excess return to volatility. A doubling of volatility doubles the excess return, which – assuming a slowly adjusting long-run target price – implies a sudden price drop when volatility spikes. Time scales matter: avalanches happen suddenly; the Sharpe ratio and long-run target price adjust relatively slowly. This provides a rationale why downward corrections are often sudden.

The mapping of avalanche size to the volatility σ\sigma through averaging, sliding windows or weight functions provides many choices, and in particular influences option valuations. We forego analysing derivatives and instead look at ‘arbitrage’. This arises from the different path the drift and volatility can take on the manifold between relatively stable configurations.
The point on the manifold normally creeps along, but is occasionally jolted by a burst of incoming information leading to a leap in volatility. How does the market state move from the initial point in σ\sigma and μ\mu space to this new point? It can follow a geodesic path, which is selected out, because it has an extremal property, or deviate from it.
It will be shown that deviations from the geodesic, e.g. by following a Sharpe ratio constant path, provide profit opportunities.

Each section is introduced by a stanza from Lewis Carroll’s *The Hunting of the Snark*.

The paper is organized as follows. Section II develops the sandpile model. Section III introduces the geometry of the upper half-plane and the geodesic equations. Section IV states the geodesic no-arbitrage relation. Section V quantifies the arbitrage potential between geodesic and Euclidean paths and derives the optimal dynamic trading strategy. Section VI distinguishes geodesic flow from Onsager excursions. Section VII concludes.

## II Sandpile Model

> They sought it with thimbles, they sought it with care;
>   
> They pursued it with forks and hope;
>   
> They threatened its life with a railway-share;
>   
> They charmed it with smiles and soap.

Information is modeled as a sandpile in a state of self-organized criticality.
Each discrete event – a trade, a news announcement, a data release – adds a grain to an accumulating pile. The pile’s slope measures unrevealed information, waiting to be integrated in the price. When the slope reaches a critical threshold, the chance of an additional grain to trigger an avalanche is high. Information floods the market.

Two features of importance:
Information loading happens slowly and deterministically; i.e. grain by grain.
Avalanches happen suddenly and reset the information gradient.

Incremental data events accumulate to form an information gradient, the system’s height of unprocessed information, and corresponds to the pile’s angle θ​(t)\theta(t).
Between avalanches, the information gradient builds at rate vv:

|  |  |  |
| --- | --- | --- |
|  | d​θ=v​d​td\theta=vdt |  |

As the critical threshold θc\theta\_{c} is approached, the probability for an avalanche of size ss to occur, resetting θ\theta to a lower value, increases. The probability for avalanche size ss is proportional to the overshoot:

|  |  |  |
| --- | --- | --- |
|  | s∝α​(θ−θc).s\propto\alpha(\theta-\theta\_{c}). |  |

After the avalanche, the cycle repeats. This is a mean-reverting process with jumps222The relationship between avalanche size ss and volatility is captured by the slope dynamics: d​θt=v​d​t−s​(θt)​d​N​(θt)d\theta\_{t}=vdt-s(\theta\_{t})dN(\theta\_{t}), where vv is the steady information inflow. As θt→θc\theta\_{t}\to\theta\_{c}, the state-dependent coupling of the jump probability d​N​(θt)dN(\theta\_{t}) and the magnitude s​(θt)s(\theta\_{t}) ensures the system exhibits the characteristic scaling laws of SOC, pinning the dynamics to the critical threshold.
.

In the financial context, the avalanche size ss drives volatility. When an avalanche occurs, volatility jumps; between avalanches, it mean-reverts. This asymmetry–volatility jumps up instantaneously and decays slowly–is the signature of information avalanches. It distinguishes the model from symmetric jump processes. The exact mapping of avalanche size ss to the volatility σ\sigma through averaging, sliding windows or a weight function we forego, since any ‘reasonable’ mapping333By reasonable’ we mean any mapping that is monotonic in ss, does not use future information, and allows avalanches to bump volatility discontinuously, but
the exact functional form does not affect the existence of the geodesic vs. Euclidean path difference, which is the focus of this paper. The discontinuity is essential, because it forces the interpolation between two distinct states.
will lead to the same result.
What matters is the qualitative picture: stress builds, stress releases, and releases are fast.

## III The Geometry of the Upper Half-Plane

> The Butcher rendered ideas of his own,
>   
> With a somewhat peculiar grace:
>   
> And instructed the Snark on the path it should take,
>   
> By the light of the sun and the face.

The statistical manifold for a normal distribution is the upper half-plane with coordinates.

|  |  |  |
| --- | --- | --- |
|  | x1=μ(drift),x2=σ(volatility).x^{1}=\mu\quad(\text{drift}),\qquad x^{2}=\sigma\quad(\text{volatility}). |  |

The Fisher information metric (up to a global scaling factor444Note, the parameters (μ,σ)(\mu,\sigma), where drift μ\mu normally scales as T−1T^{-1} and volatility σ\sigma as T−1/2T^{-1/2}, are de-dimensionalized by the characteristic information-arrival window to resolve any temporal scaling discrepancies.) is

|  |  |  |
| --- | --- | --- |
|  | d​s2=d​μ2+2​d​σ2σ2.ds^{2}=\frac{d\mu^{2}+2d\sigma^{2}}{\sigma^{2}}. |  |

The metric is non-flat, possessing a constant negative curvature; this renders Euclidean straight-line paths non-geodesic, a fact of importance in subsequent sections.
The Christoffel symbols are

|  |  |  |
| --- | --- | --- |
|  | Γμ​σμ=−1σ,Γμ​μσ=12​σ,Γσ​σσ=−1σ.\Gamma^{\mu}\_{\mu\sigma}=-\frac{1}{\sigma},\quad\Gamma^{\sigma}\_{\mu\mu}=\frac{1}{2\sigma},\quad\Gamma^{\sigma}\_{\sigma\sigma}=-\frac{1}{\sigma}. |  |

For Gaussians, the Fisher information metric, the Christoffel symbols, and the resulting semicircular geodesic equations, confirming its structure as the hyperbolic Poincare upper half-plane, as well as the path length of importance in the next two sections can all be found in Amari’s book[amari2016](#bib.bib1) .

Imagine an avalanche occurs. This leads not to a departure from the equilibrium manifold, but it is an extremely rapid traversal of a particular path. The system moves from (μ1,σ1)(\mu\_{1},\sigma\_{1}) to (μ2,σ2)(\mu\_{2},\sigma\_{2}) along a geodesic, i.e. a minimal length path.
The geodesic connecting two points is given by the semicircle

|  |  |  |  |
| --- | --- | --- | --- |
|  | (μ−μc)2+2​σ2=R2,(\mu-\mu\_{c})^{2}+2\sigma^{2}=R^{2}, |  | (1) |

where the center μc\mu\_{c} and radius RR are determined by the endpoints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μc\displaystyle\mu\_{c} | =μ1+μ22+σ12−σ22μ1−μ2,\displaystyle=\frac{\mu\_{1}+\mu\_{2}}{2}+\frac{\sigma\_{1}^{2}-\sigma\_{2}^{2}}{\mu\_{1}-\mu\_{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | R\displaystyle R | =(μ1−μc)2+2​σ12.\displaystyle=\sqrt{(\mu\_{1}-\mu\_{c})^{2}+2\sigma\_{1}^{2}}. |  |

The resulting path is the information-geometric analogue of a brachistochrone555Just as Bernoulli derived the global Brachistochrone by integrating the local refraction (Snell’s law) into Fermat’s Principle of Least Time, the Fisher-Rao geodesic integrates the infinitesimal Kullback-Leibler divergence (the Fisher information metric) into a global minimal distance..

The Banker’s lag occurs in Layer 2, because the market moves rapidly within the equilibrium manifold. The geometry still holds; the coordinates still transform via geodesics; the exponential family still describes the state, but a central banker’s responses normally would lag. Crashes are therefore not necessarily breakdowns of equilibrium. Instead, they can be due to rapid traversals of the equilibrium manifold666The implied volatility smile emerges as a projection of the geodesic onto option strike space. This connects to the maximum entropy option pricing of [Brody](#bib.bib3) ..

## IV No-Arbitrage Geodesics

> And the Banker, inspired with a courage so new –
>   
> It was matter for general remark,
>   
> Rushed madly ahead and was lost to their view
>   
> In his zeal to discover the Snark

The market evolves from an initial to a final market state as a response to an avalanche. This update must satisfy the principle of Minimum Information Action777The principle of ‘Minimum Information Action’ is the information-theoretic equivalent of the principle of least action in classical mechanics.
It dictates that the system moves between equilibria (μ1,σ1)(\mu\_{1},\sigma\_{1}) and (μ2,σ2)(\mu\_{2},\sigma\_{2}) along the geodesic – the unique path of zero dissipation (d​Q=0dQ=0). Suboptimal path-selection generates ‘information heat’, and any deviation from geodesic implies that the market is ‘performing’ unnecessary informational work and results in potentially harvestable arbitrage – see [meister2026b](#bib.bib5) 
 and selects out a geodesic, which represents a reversible, zero-dissipation evolution. Any other path generates ‘information heat’ (d​Q>0dQ>0) and an arbitrage potential.

The no-arbitrage condition forces the response to the avalanche to follow the unique geodesic – the path of zero dissipation. The geodesic length is the hyperbolic distance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lgeo=arcosh⁡(1+(μ2−μ1)2+2​(σ2−σ1)24​σ1​σ2).L\_{\text{geo}}=\operatorname{arcosh}\left(1+\frac{(\mu\_{2}-\mu\_{1})^{2}+2(\sigma\_{2}-\sigma\_{1})^{2}}{4\sigma\_{1}\sigma\_{2}}\right). |  | (2) |

The existence of avalanches also reprices options. In the presence of Self-Organized Criticality (SOC), avalanche size ss scales as s−τs^{-\tau} and creates heavy-tailed option pricing888Option valuation is given by ∫σ22​Γ​𝑑t\int\frac{\sigma^{2}}{2}\Gamma\,dt. In the extreme case of roughly τ<2\tau<2 and a ‘reasonable’ mapping into σ\sigma the s−τs^{-\tau} scaling of the SOC avalanche size leads to an unlimited volatility-driven gamma rent, transforming ‘informational heat’ into a wealth divergence. The paper forgoes a comparison of SOC option pricing with rough volatility, wandering gaussians or other models to avoid having to justify how to map avalanche size to σ\sigma.
  
One must distinguish between two types of ‘information heat’, i.e. ‘arbitrage heat’ and ‘geometric heat’. Arbitrage heat is dynamic and path-dependent; it is the ‘wealth leak’ from choosing a linear ray instead of a geodesic. Geometric heat is the inescapable cost of the information flow itself, and determines option values. Restoring correct time dependence clarifies sensitivity to time. Arbitrage Heat scales linearly, while the Geometric Heat scales as the square root of time..

The Sharpe ratio999Only one asset is directly considered, but this asset is assumed to be part of a wider market. For simplicity the risk-free rate is set to zero, r=0r=0.

|  |  |  |
| --- | --- | --- |
|  | S=μ1σ1,S=\frac{\mu\_{1}}{\sigma\_{1}}, |  |

is a natural market invariant that allows assets and portfolios to be compared. For a transition between states sharing the same Sharpe ratio, SS defines both the coordinate ray from the origin and the slope of the linear chord between them.
However, the Sharpe ratio conserving dynamics do not coincide with the geodesic.
As an example, consider the ‘linear’ path with constant Sharpe ratios that switches from (μ1,σ1)(\mu\_{1},\sigma\_{1}) to (μ2,σ2)(\mu\_{2},\sigma\_{2}), and the trajectory is

|  |  |  |
| --- | --- | --- |
|  | σ​(f)=σ1+f​(σ2−σ1),μ​(f)=σ​(f)​S+r,f∈[0,1].\sigma(f)=\sigma\_{1}+f(\sigma\_{2}-\sigma\_{1}),\quad\mu(f)=\sigma(f)S+r,\quad f\in[0,1]. |  |

Its length in the Fisher metric is

|  |  |  |
| --- | --- | --- |
|  | Llin=∫01(d​μd​f)2+2​(d​σd​f)2σ​(f)​𝑑f=S2+2​ln⁡σ2σ1.L\_{\text{lin}}=\int\_{0}^{1}\frac{\sqrt{(\frac{d\mu}{df})^{2}+2(\frac{d\sigma}{df})^{2}}}{\sigma(f)}df=\sqrt{S^{2}+2}\ln\frac{\sigma\_{2}}{\sigma\_{1}}. |  |

The discrepancy Δ​Lt=Llin−Lgeo\Delta L\_{t}=L\_{\text{lin}}-L\_{\text{geo}} is the source of the dynamic arbitrage strategy, ∫Wt​Δ​Lt​𝑑t\int W\_{t}\,\Delta L\_{t}\,dt, where WtW\_{t} is the capital employed, and evaluated in a discrete approximation in the beginning of the following section.

While the existence of Δ​L>0\Delta L>0 identifies and quantifies an opportunity, is it is not a sufficient condition for risk-less profit.
In real markets, frictions and constraints may prevent exploitation. Nevertheless, the geodesic is the unique path consistent ‘non-arbitrage’.
The actual exploitation also depends on the arbitrageurs ability to navigate the manifold faster than the dissipation of the information signal. Otherwise, the heat might simply dissipate as noise.

## V The Dynamic Arbitrage Strategy

> The Bellman looked frightened, and turned very pale,
>   
> And let the bell drop from his hand:
>   
> And his voice trembled so, that he could hardly say
>   
> The first thing he’d planned to say.

The geodesic no-arbitrage relation establishes that any transition between equilibrium states must follow the Fisher-Rao geodesic to avoid ‘information heat’. But this heat is not merely a theoretical abstraction—it represents a profit opportunity. We now quantify the excess action of the Euclidean (constant Sharpe) path and derive the optimal dynamic strategy to capture it.

Consider an infinitesimal step from (μ,σ)(\mu,\sigma) to (μ+d​μ,σ+d​σ)(\mu+d\mu,\sigma+d\sigma) with d​σ=εd\sigma=\varepsilon small and d​μ=S​εd\mu=S\varepsilon following the constant Sharpe constraint. The linear path length in the Fisher metric is

|  |  |  |
| --- | --- | --- |
|  | Llin=S2+2​ϵσ+𝒪​(ε2).L\_{\text{lin}}=\sqrt{S^{2}+2}\,\frac{\epsilon}{\sigma}+\mathcal{O}(\varepsilon^{2}). |  |

The geodesic connecting these nearby points is given by the hyperbolic distance.
The expansion of the ‘arcosh’ function,

|  |  |  |
| --- | --- | --- |
|  | arcosh⁡(1+x)=2​x+𝒪​(x3/2),\operatorname{arcosh}(1+x)=\sqrt{2x}+\mathcal{O}(x^{3/2}), |  |

with

|  |  |  |
| --- | --- | --- |
|  | x=(S2+2)​ε24​σ​(σ+ε)=(S2+2)​ε24​σ2+𝒪​(ϵ3),x=\frac{(S^{2}+2)\varepsilon^{2}}{4\sigma(\sigma+\varepsilon)}=\frac{(S^{2}+2)\varepsilon^{2}}{4\sigma^{2}}+\mathcal{O}(\epsilon^{3}), |  |

gives

|  |  |  |
| --- | --- | --- |
|  | Lgeo=S2+22​εσ+𝒪​(ε2).L\_{\text{geo}}=\sqrt{\frac{S^{2}+2}{2}}\,\frac{\varepsilon}{\sigma}+\mathcal{O}(\varepsilon^{2}). |  |

The excess action for this infinitesimal step is therefore

|  |  |  |
| --- | --- | --- |
|  | Δ​L=Llin−Lgeo=S2+2​(1−12)​εσ+𝒪​(ε2),\Delta L=L\_{\text{lin}}-L\_{\text{geo}}=\sqrt{S^{2}+2}\left(1-\frac{1}{\sqrt{2}}\right)\frac{\varepsilon}{\sigma}+\mathcal{O}(\varepsilon^{2}), |  |

and represents the arbitrage potential. In an ideal market it would be eliminated by forcing the geodesic. But if the market temporarily follows the Euclidean path, Δ​L\Delta L becomes a potentially harvestable profit.
Even if the arbitrageur does not know the endpoint (μ2,σ2)(\mu\_{2},\sigma\_{2}), the opportunity is exploitable, since the strategy is local and dynamic.

At any instant, the current market state (μ,σ)(\mu,\sigma) defines a local geodesic direction via the geodesic equation:

|  |  |  |
| --- | --- | --- |
|  | d​μd​σ=−2​σμ−μc,\frac{d\mu}{d\sigma}=-\frac{2\sigma}{\mu-\mu\_{c}}, |  |

where μc\mu\_{c} is the (unknown) center of the full geodesic. The local slope can be inferred from the current curvature of the manifold.

The mispricing between the Euclidean expectation (constant Sharpe) and the geodesic creates instantaneous hedge ratios. For any derivative V​(μ,σ,t)V(\mu,\sigma,t), the difference in its predicted change along the two paths is

|  |  |  |
| --- | --- | --- |
|  | δ​V=∂V∂μ​(μgeo−μlin)+∂V∂σ​(σgeo−σlin).\delta V=\frac{\partial V}{\partial\mu}(\mu\_{\text{geo}}-\mu\_{\text{lin}})+\frac{\partial V}{\partial\sigma}(\sigma\_{\text{geo}}-\sigma\_{\text{lin}}). |  |

To be neutral to the geodesic, i.e. to have zero exposure if the market follows the geodesic, while being exposed to the Euclidean path, the arbitrageur holds:

* •

  Long the underlying in proportion to ∂V/∂μ\partial V/\partial\mu,
* •

  Short volatility (Vega) in proportion to ∂V/∂σ\partial V/\partial\sigma.

The ratio of Vega short to stock long at any instant is

|  |  |  |
| --- | --- | --- |
|  | Vega positionStock position=∂V/∂σ∂V/∂μ=νΔ,\frac{\text{Vega position}}{\text{Stock position}}=\frac{\partial V/\partial\sigma}{\partial V/\partial\mu}=\frac{\nu}{\Delta}, |  |

where ν\nu is Vega and Δ\Delta is delta. This ratio evolves along the path according to the geodesic curvature.
Re-balancing continuously as the market updates its state, the arbitrageur harvests Δ​L\Delta L increment by increment, and is analogous to running a Carnot engine (for an application of Carnot cycles to finance see [Meister2026a](#bib.bib4) ) between the initial and final states. The geodesic is the reversible, zero-entropy path. The Euclidean path corresponds to an irreversible, heat-generating process. The arbitrageur’s aim is to extract as much as possible of the excess heat.
Heat is not a modeling artifact; it is the fundamental cost of moving through information space in a suboptimal way.

## VI Geodesic Flow and Onsager Excursions

> Other maps are such shapes, with their islands and capes!
>   
>  But we’ve got our brave Captain to thank
>   
>  (So the crew would protest) ‘that he’s bought us the best-
>   
>  A perfect and absolute blank!’

The companion paper established that finite-resource markets are described by a minimal exponential family – an equilibrium geometry. This section outlines two different ways of market movement.

Layer 2: Geodesic Flow on the Equilibrium Manifold

The upper half-plane with coordinates (μ,σ)(\mu,\sigma) carries the Fisher metric. The avalanche is an extremely rapid traversal of a geodesic segment. The system never leaves the equilibrium manifold.

Layer 3: Onsager Excursions (Limited Departures)

When the system is pushed slightly off the equilibrium manifold – by a perturbation that violates the geodesic flow – it enters the linear response regime governed by Onsager reciprocity (see [meister2026b](#bib.bib5)  for an application to finance):

|  |  |  |
| --- | --- | --- |
|  | η˙i=∑jLi​j​Xj,\dot{\eta}\_{i}=\sum\_{j}L\_{ij}X^{j}, |  |

where XjX^{j} are thermodynamic forces and Li​jL\_{ij} is the transport matrix. This is a limited, controlled departure from equilibrium – a transient perturbation.

## VII Conclusion: Banker’s Fate

> He offered large discount – he offered a cheque
>   
> (Drawn to bearer’) for seven-pounds-ten:
>   
> But the Bandersnatch merely extended its neck
>   
> And grabbed at the Banker again.

Banker’s lag is the consequence of minimizing the time spent violating the Sharpe-constancy macro-constraint. By hurtling along the zero-dissipation geodesic to eliminate micro-arbitrage during an informational avalanche, the market outruns the Banker’s capacity to respond and results in a state of market desynchronization.
This is not a failure of the
equilibrium. The minimal exponential families are rich enough to host both static equilibrium and market corrections, proving there is no necessity to invoke non-exponential families to study extreme market events.

The dynamic arbitrage strategy derived from this geometry provides a possible way to harvest the excess when markets deviate from the geodesic, and the three-layer framework unifies the static equilibrium of the companion paper[meister2026b](#bib.bib5)  with the dynamics of stress accumulation and release.

Many questions remain: empirical calibration of the stress gap, the functional form of the loading rate vv and the jump process, and more generally the thermodynamic signature of the information avalanches.

The Bandersnatch is already contained in the minimal map of exponential families navigated by the banker. There is no requirement to extend the map to understand the territory. The elusive Snark of the equilibrium can already force the Banker’s Lag.

## References

* (1)
   Amari, S. (2016). Information Geometry and Its Applications. Springer Press.
* (2)

  Bak, P., Tang, C., & Wiesenfeld, K. (1988). Self-organized criticality. Physical review A, 38(1), 364.
* (3)
   Brody, D. C., Buckley, I. R. C., & Meister, B. K. (2004). Information flow and the speed of the market. *Proceedings of the Royal Society of London A*, 460, 1-18.
* (4)
   Meister, B. K. (2026). Automated Liquidity: Market Impact, Cycles, and De-pegging Risk. arXiv:2601.11375.
* (5)
   Meister, B. K. (2026). Caratheodory, Finite Resources and the Geometry of Arbitrage arXiv:2602.16539.

BETA