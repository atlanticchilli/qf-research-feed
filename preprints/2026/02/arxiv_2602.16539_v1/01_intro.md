---
authors:
- B. K. Meister
doc_id: arxiv:2602.16539v1
family_id: arxiv:2602.16539
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Carathéodory, Finite Resources and the Geometry of Arbitrage
url_abs: http://arxiv.org/abs/2602.16539v1
url_html: https://arxiv.org/html/2602.16539v1
venue: arXiv q-fin
version: 1
year: 2026
---


B. K. Meister
[bernhard.k.meister@gmail.com](mailto:bernhard.k.meister@gmail.com)

###### Abstract

Carathéodory’s axiom of adiabatic inaccessibility states that, in any neighborhood of a thermodynamic state, certain states remain unreachable via adiabatic processes. Non-arbitrage mirrors this topological restriction in finance.
Preserving this constraint in resource-limited systems identifies the exponential family not as a modeling convenience but as the requisite geometric structure unifying both domains.

## I Introduction

Carathéodory’s second law begins with a seemingly local statement – in any neighborhood of an equilibrium state, there exist states that are adiabatically inaccessible111A more precise formulation of Axiom II: ‘In jeder beliebigen Umgebung eines willkürlich vorgeschriebenen Anfangszustandes gibt es Zustände, die durch adiabatische Zuständsänderungen nicht beliebig approximiert werden können’. – yet it is in effect a global constraint.
Carathéodory[caratheodory1909](https://arxiv.org/html/2602.16539v1#bib.bib5)  showed that, for the ‘simple systems’ he considered, local integrability follows, and from this, a global foliation into entropy surfaces222Buchdahl [buchdahl1966](https://arxiv.org/html/2602.16539v1#bib.bib3) ; [buchdahl1975](https://arxiv.org/html/2602.16539v1#bib.bib4)  offers a minimalist restatement of classical thermodynamics from conceptual foundations.. But a global extension from local integrability for arbitrary systems is not automatic, as Boyling’s counterexample[boyling1968](https://arxiv.org/html/2602.16539v1#bib.bib1)  demonstrates333Buchdahl & Greve[buchdahl](https://arxiv.org/html/2602.16539v1#bib.bib2)  and others had earlier noted this limitation..

This gap is not a thermodynamic curiosity. No-arbitrage in finance presents a direct analogue. Within any small neighborhood of a portfolio state, local non-arbitrage ensures the existence of a local pricing function. This local consistency does not guarantee global market stability. A trader might execute locally fair trades along a closed loop for net gain. Without additional structure, the local foliation that guarantees path-independence in the small fails to extend globally.

To close this gap, an operational constraint444This aligns with the “ultra-finitism” of A. S. Esenin-Volpin[esenin1970](https://arxiv.org/html/2602.16539v1#bib.bib6) , who rejected the infinite-precision continuum as a mathematical fiction, arguing that physical reality is bounded by the feasibility of step-wise construction. If a value cannot be constructed in a finite number of observable steps, it does not exist.
Esenin-Volpin went further, questioning the existence of even very large finite numbers. is imposed: the market’s probabilistic state must remain describable with finite resources regardless of scale – ergo, information about the market state must be compressible into a fixed set of summary statistics whose number does not grow with the size of the system.

The Pitman-Koopman-Darmois theorem (PKD) characterizes the unique consequence of this condition for independent and identically distributed observations: if a family of distributions admits a sufficient statistic whose dimension does not grow with sample size, then it must be an exponential family555In the Information Geometry of Amari, an ’exponential family’ is intrinsically defined by a finite set of sufficient statistics (making ’finite-rank’ technically redundant)..
Finite-resource description thus mandates the exponential family for market observables.

This result depends crucially on the IID assumption666The IID assumption is the simplest setting in which the thermodynamic limit is well-defined and the PKD theorem applies. While real markets may exhibit dependencies and non-stationarities, this idealized regime defines the baseline where our sufficient condition holds; violations signal a possible departure from the simple equilibrium described by our framework, though more general equilibrium concepts (such as those of Lieb-Yngvason) may still apply.. Consequently, our framework excludes regimes where this assumption fails. In thermodynamics, this would be small systems where fluctuations dominate (the ‘Resolution Gap’) and critical points where correlation lengths diverge (the ‘Correlation Boojum’). In finance this includes for example periods of market instability, liquidity crises, and structural breaks where ‘market temperature’ becomes ill-defined due to non-stationarity.

Under the operational constraint imposed, the exponential family is thus not a modeling convenience but the necessary geometric structure that preserves coherence of local no-arbitrage conditions across scales.

Our choice forgoes the axiomatic generality of approaches like Lieb & Yngvason [LY](https://arxiv.org/html/2602.16539v1#bib.bib8)  in favor of a more constrained and operational structure. While their formulation establishes entropy under general conditions, it places no bound on descriptive complexity. Our operational approach aligns with viewing thermodynamic and financial problems through the lens of information. For systems where finite-resource describability holds – a class that includes many thermodynamic settings and equilibrium states of observable markets – the distribution belongs to the exponential family, yielding a globally convex potential with a well-behaved Fisher metric. This provides a sufficient condition for thermodynamic-like behavior in finance777Buchdahl in his publications on thermodynamics lets “physical intuition take precedence over mathematical subtleties”. We share his stance, even if it chafes against the realities of finance and statistics..

Two characters from Lewis Carroll frame the challenge. The Snark represents the elusive goal of a globally integrable market model. The Boojum is where this structure ‘softly and suddenly vanishes away’: in the ‘resolution gap’ of small systems, the diverging correlations at critical points, and during the ‘regime shifts’ of non-stationary markets – where the foliation tears, description length becomes infinite, or ’market temperature’ loses meaning.

Section II reviews the thermodynamic laws and their financial analogues. Section III presents Boyling’s counterexample in detail. Section IV introduces the PKD theorem and shows how finite-resource describability leads to the exponential family. Section V extends the geometry to dynamics via Onsager reciprocity. Section VI concludes.

## II Thermodynamic Laws: Prerequisites and Constraint

Market structure, by thermodynamic analogy, comprises three layers.
The first two are prerequisites that make the third meaningful; only the third imposes the geometric constraint.

### II.1 Zeroth Law: State Space Exists

The Zeroth Law establishes that thermal equilibrium is transitive: if system AA equilibrates with BB and BB with CC, then AA equilibrates with CC.
This partitions state space into equivalence classes – surfaces of constant temperature – yielding a foliated manifold for thermodynamics.
In finance, the Law of One Price plays the analogous role.

### II.2 First Law: Path-Independence

The First Law asserts path-independence of work in insulated systems: δ​Wad=−d​U\delta W\_{\text{ad}}=-dU establishes internal energy UU as a state function. This defines what counts as an ‘adiabatic process’ (one with δ​Q=0\delta Q=0) and foliates state space into isoenergetic surfaces.
In finance, this corresponds to the self-financing condition. Namely, changes in portfolio value are given solely by price changes of the constituent assets, with no external inflows or outflows – the analogue of an adiabatic process.

### II.3 Second Law: Geometric Constraint

Carathéodory’s axiom states that in any neighborhood of an equilibrium state, there exist states inaccessible via adiabatic processes. In finance, the non-arbitrage axiom states that in any neighborhood of an allowed market state, some markets states are inaccessible via non-arbitrage processes.

## III The Boyling Counterexample: A Toy Model of Market Incoherence

Building on the Zeroth and First Law analogues from Section II – the Law of One Price and the self-financing condition – the wealth change from a trading strategy is represented by a 1-form ψ\psi
on the state space. To understand why local integrability does not guarantee global stability, consider a ‘toy market’ defined on a two-dimensional plane ℝ2\mathbb{R}^{2}. In this model (directly taken from Boyling [boyling1968](https://arxiv.org/html/2602.16539v1#bib.bib1) ), the infinitesimal flux of wealth is described by the 1-form:

|  |  |  |
| --- | --- | --- |
|  | ψ=y3​(1−y)2​d​x+[y3−2​(1−y)2]​d​y.\psi=y^{3}(1-y)^{2}dx+[y^{3}-2(1-y)^{2}]dy. |  |

This expression satisfies the condition for local consistency.
In this context, local consistency is synonymous with local non-arbitrage: it means that within any sufficiently small neighborhood, the market is integrable. In such a neighborhood, there exists a relationship ψ=f​d​g\psi=fdg, where gg is a local potential and ff is a local integrating factor (the inverse ”market temperature”).

Under a microscope, this relationship ensures the state space appears ‘layered’, preventing any infinitesimal closed-loop trading strategy from extracting risk-free gain. Because the local flux is tied to a local potential, any round-trip trade within a small patch must return to its starting value.

This local non-arbitrage does not generalize to the system as a whole. While the manifold is smooth and simply connected, the field ψ\psi is fundamentally twisted, as
the local relationship ψ=f​d​G\psi=fdG fails to cohere into a single, global potential. On the strip x∈Rx\in R and 0<y<10<y<1, G​(x,y)\,\,\,G(x,y) has the form

|  |  |  |
| --- | --- | --- |
|  | h​(x+1y2+11−y).h\left(x+\frac{1}{y^{2}}+\frac{1}{1-y}\right). |  |

The integrating factor ff must satisfy on the strip

|  |  |  |
| --- | --- | --- |
|  | f​(x,y)​h′​(x+1y2+11−y)=y3​(1−y)2.f(x,y)h^{\prime}\left(x+\frac{1}{y^{2}}+\frac{1}{1-y}\right)=y^{3}(1-y)^{2}. |  |

The contradiction is then found in the asymptotic requirements of h′​(t)h^{\prime}(t). For the market to remain globally consistent, ff must be continuous and non-zero across the entire domain, requiring it to tend toward finite, non-zero limits as y→0y\to 0 and y→1y\to 1. As a consequence, h′​(t)h^{\prime}(t) is forced to satisfy two mutually exclusive decay rates for t→+∞t\to+\infty: it must scale as t−3/2t^{-3/2} to satisfy the y→0y\to 0 boundary and as t−2t^{-2} for the y→1y\to 1 boundary,
leading to a contradiction.

The geometry is thus inherently twisted, representing a geometric manifestation of an infinite-rank system. This occurs because the local integrating factor (temperature) cannot be scaled across the manifold without the description length of the market state exploding.

The missing link is this: unbounded decay rates prevent the local potentials from cohering into a single global function. As is shown in the next section, imposing finite-resource describability eliminates this obstruction.

Lack of a single global function enables general arbitrage over long cycles; a trader can execute a series of locally ‘fair’ trades and return to the starting point with a net gain. Without the exponential family identified by the PKD theorem or something analogous, local consistency cannot prevent a ’perpetual motion machine’ as market complexity scales. The gap can be closed by moving beyond the local topology to the information-theoretic requirement of a fixed-dimension sufficient statistic.

The Boyling counterexample thus reveals a hierarchy888Instantaneous Non-Arbitrage (Short-Path Consistency): Corresponds to local integrability (ψ∧d​ψ=0\psi\wedge d\psi=0). This ensures that for any immediate portfolio adjustment, a local ”up” and ”down” direction exists. It forbids ”short-path” wealth extraction but remains blind to global topology.
  
General Arbitrage (Round-Trip Incoherence): A global condition requiring path-independence. In a system lacking global integrability, a trader can execute a ”long-path” cycle—a series of trades that return to the same state-space coordinates but result in a net gain in wealth.: a market can satisfy instantaneous non-arbitrage (local integrability) while permitting general arbitrage (global incoherence). Closing this gap requires additional structure.

## IV The PKD Theorem as the Geometric Stabilizer

The Boyling counterexample established that a market can be locally integrable everywhere yet globally twisted, permitting closed-loop arbitrage. The question is what additional structure can prevent this. The PKD theorem999The theorem’s regularity conditions (smoothness) and the requirement of constant support are assumed to be satisfied for the families of distributions considered here. shows that, under an operational constraint on describability, the distribution must be exponential family.

A conditional distribution belongs to the exponential family if it can be written in the form:

|  |  |  |
| --- | --- | --- |
|  | p​(X|θ)=exp⁡(⟨θ,T​(X)⟩−ψ​(θ)),p(X|\theta)=\exp\left(\langle\theta,T(X)\rangle-\psi(\theta)\right), |  |

where XX represents the observable variables (prices, returns, volumes), θ∈ℝd\theta\in\mathbb{R}^{d} is the latent market state (e.g., risk factor exposures), T​(X)T(X) is a vector of sufficient statistics that capture all information in XX relevant to θ\theta, and ψ​(θ)\psi(\theta) is the log-partition function that ensures normalization. The sufficient statistics T​(X)T(X) serve as the macroscopic observables – the quantities that summarize the market’s microscopic activity.

The exponential family is not an arbitrary choice: its log-partition function ψ​(θ)\psi(\theta) is globally convex. Its Hessian, the Fisher information metric gi​j=∂i∂jψg\_{ij}=\partial\_{i}\partial\_{j}\psi, is therefore positive-definite everywhere.

The Boyling construction reveals incompatible scaling requirements for the integrating factor as one moves across the manifold. In statistical terms, this incompatibility means that describing the market state in different regions would require different sufficient statistics – or a sufficient statistic of growing dimension – to capture the local structure. The description length, therefore, cannot remain fixed.

To see why this forces an infinite-dimensional sufficient statistic, suppose contrarywise that a fixed-dimensional statistic T​(X)∈ℝdT(X)\in\mathbb{R}^{d} sufficed for all regions. Then the conditional distributions p​(X∣θ)p(X\mid\theta) would belong to a dd-dimensional exponential family, with potential ψ​(θ)\psi(\theta) globally convex. The Fisher metric gi​j=∂i∂jψg\_{ij}=\partial\_{i}\partial\_{j}\psi would then be positive-definite everywhere. But Boyling’s construction shows that any such global metric would have to satisfy two incompatible scaling regimes at the boundaries – a contradiction. Hence, no fixed-dimensional sufficient statistic can exist within the IID regime that defines the scope of our analysis101010One might ask: could a fixed-dimensional statistic exist without the family being exponential? The PKD theorem proves this is impossible under IID. Hence the chain – fixed-dimensional statistic ⇒\Rightarrow exponential family ⇒\Rightarrow convex ψ\psi ⇒\Rightarrow positive-definite metric – is necessary.. The Boyling twist therefore precludes any finite-dimensional sufficient statistic.

The functional contradiction in Boyling’s decay rates (t−3/2t^{-3/2}  vs.  t−2t^{-2}) is not merely a topological curiosity; it is the geometric manifestation of statistical non-sufficiency. In information-geometric terms, the inability to find a single, globally valid integrating factor implies that the system possesses infinite rank.

Applying this to the Boyling setting, the contradictory asymptotic regimes correspond precisely to a violation of the fixed-dimension condition. The manifold contains regions that, if they were to support a probabilistic interpretation, would require different sufficient statistics – or a sufficient statistic of growing dimension – to capture their structure. The Boyling twist is thus a geometric signature of a system that fails the finite-resource describability constraint.

For an exponential family, the potential ψ​(θ)\psi(\theta) is globally convex, ensuring the Fisher metric remains invertible across the entire manifold. This is precisely what Boyling’s construction lacks, and it is exactly what finite-resource describability, via PKD, guarantees: a fixed-dimensional sufficient statistic requires the exponential family111111While infinite-rank integrable forms may exist as mathematical possibilities, they fail the resource-constraint of a stable, macroscopic ”temperature” by requiring an unbounded description length.. This positive-definiteness forbids global arbitrage121212This establishes global coherence for the statistical manifold and for the wealth potential defined by the self-financing condition. Other financial quantities, if they are smooth functions of the state, retain this property. However, it is possible that for example securities with non-smooth payoffs may require additional analysis. This is left as an open question..

### IV.1 Thermometer Failure

The previous argument shows that finite-resource describability forces the market into the exponential family. This is equilibrium geometry. A ‘thermometer test’ can now be formulated. When does this geometry not describe observable markets?
In at least three regimes: for small
NN where fluctuations dominate (Resolution Gap); at critical points where correlations diverge (Correlation Boojum); and for non-stationary markets where the IID precondition fails (Regime Shifts).

In a discrete setting – viewing the market as a Directed Acyclic Graph of transactions – establishing equilibrium conditions is simpler: local exchange rates around any elementary loop (e.g., triangular arbitrage) must sum to zero in log-space131313Because exchange rates are multiplicative, no-arbitrage across a cycle requires the product of rates to equal unity (R12⋅R23⋅R31=1R\_{12}\cdot R\_{23}\cdot R\_{31}=1). In log-space, this product becomes a linear summation (∑log⁡Ri​j=0\sum\log R\_{ij}=0). .As before, local consistency on the graph does not guarantee a global potential if the network topology allows large-scale cycles141414Transitory ‘cyclic arbitrage’ observed in liquid markets is thus interpreted not as a topological Snark, but as an extrinsic information flux (noise plus signal) that momentarily pushes the market off the rigid, dually flat manifold considered in equilibrium finance. Such fluctuations are not internal to the state manifold’s geometry but represent a departure from the equilibrium description..

## V Onsager Reciprocal Relations and Market Dynamics

The preceding sections established the equilibrium geometry. This section connects this geometry to market dynamics, showing how symmetry of the transport matrix – first studied by Onsager[onsager1931a](https://arxiv.org/html/2602.16539v1#bib.bib11) ; [onsager1931b](https://arxiv.org/html/2602.16539v1#bib.bib12)  – emerges from micro-structural scaling or a gradient-flow hypothesis.

### V.1 Deriving Detailed Balance from Microstructural Scaling

In the standard continuous-time limit of market dynamics – common to diffusion models – price fluctuations are dominated by volatility rather than drift over short horizons. Specifically, fluctuations scale as 𝒪​(Δ​t)\mathcal{O}(\sqrt{\Delta t}) while directional drift scales as 𝒪​(Δ​t)\mathcal{O}(\Delta t)151515This separation of scales assumes continuous price paths. Jumps, when present, introduce an additional component: jump events occur with probability 𝒪​(Δ​t)\mathcal{O}(\Delta t) and their sizes scale independently of Δ​t\Delta t. At leading order as Δ​t→0\Delta t\to 0, the continuous component still dominates local dynamics, but jumps can in principle break detailed balance. For markets where jump risk is not hedgeable, the detailed balance condition should be understood as applying to the continuous part of the evolution. We leave the pure-jump case for future work.. This separation justifies detailed balance in the local frame, since within each isentropic leaf, forward and reverse transitions become statistically indistinguishable at leading order Δ​t→0\Delta t\to 0.

In the linear response regime, fluxes respond to thermodynamic forces via a transport matrix Li​jL\_{ij}:

|  |  |  |
| --- | --- | --- |
|  | η˙i=∑jLi​j​Xj\dot{\eta}\_{i}=\sum\_{j}L\_{ij}X^{j} |  |

The thermodynamic variables are

* •

  Forces (XjX^{j}): These are the gradients of the potential ∂jψ\partial\_{j}\psi. They represent the ‘informational pressure’ or ‘stress’ pushing the system away from its current equilibrium θ\theta.
* •

  Fluxes (η˙i\dot{\eta}\_{i}): These are the expectation flows, representing the rate of change in market volume or holdings (ηi\eta\_{i}) as the system moves to resolve those pressures.
* •

  Transport Matrix (Li​jL\_{ij}): This serves as the kinetic linkage (conductance) that determines the magnitude of flow for a given force.161616By inversion, one can define the Price Impact Matrix M=L−1M=L^{-1}, where Xi=∑jMi​j​η˙jX^{i}=\sum\_{j}M\_{ij}\dot{\eta}\_{j}. In this dual view, the symmetry Mi​j=Mj​iM\_{ij}=M\_{ji} ensures that volume shocks (‘fluxes’) push prices (‘forces’).

Detailed balance implies Li​j=Lj​iL\_{ij}=L\_{ji}. Asymmetry would permit net circulation around closed loops in state space – the dynamical analogue of the Boyling twist – enabling cyclic wealth extraction. Symmetry thus emerges as a necessary condition for the absence of dynamical arbitrage.

### V.2 Gradient Flow as a Sufficient Condition

A complementary connection arises if it is assumed that market dynamics follow a gradient flow on the statistical manifold. If the system relaxes according to the natural geometry of the space:

|  |  |  |
| --- | --- | --- |
|  | η˙i=∑jgi​j​Xj\dot{\eta}\_{i}=\sum\_{j}g\_{ij}X^{j} |  |

where gi​jg\_{ij} is the Fisher information metric. In this case, the transport matrix Li​jL\_{ij} is identical to the metric gi​jg\_{ij}. Because the Fisher metric is a Hessian (gi​j=∂i∂jψg\_{ij}=\partial\_{i}\partial\_{j}\psi), it is inherently symmetric. Consequently, Li​j=Lj​iL\_{ij}=L\_{ji} is satisfied automatically.

Under this hypothesis, the dynamics inherit the full geometric structure, and the path to equilibrium is determined by the curvature of the manifold171717When the transport matrix is symmetric, the informational cost of moving between equilibrium states is path-independent and quantified by the Bregman divergence D​(η∥η′)=ψ​(θ)+ϕ​(η′)−∑iθi​ηi′D(\eta\|\eta^{\prime})=\psi(\theta)+\phi(\eta^{\prime})-\sum\_{i}\theta\_{i}\eta\_{i}^{\prime}, where ϕ\phi is the dual potential related to ψ\psi by Legendre transform. This divergence is generally asymmetric; and if the transport matrix were asymmetric, the work done in a round-trip strategy would not sum to zero, allowing for arbitrage..

## VI Conclusion: Holding the Boojum at Bay

Carathéodory’s theorem – that adiabatic inaccessibility yields a global entropy –holds only for ‘simple systems’. As Boyling’s counterexample shows, this does not extend to complex systems.

This vulnerability is resolved by requiring the market’s state to be observable via finite resources. This operational choice, via the PKD theorem, forces the exponential family – whose globally convex potential ψ​(θ)\psi(\theta) ensures that local no-arbitrage coheres into a global potential.

Only limits on resources can reasonably ensure that the market’s foliation does not ‘softly and suddenly vanish away – for the Snark was a Boojum’, and global loops do not extract wealth despite local fairness.
The absence of ‘unlimited money pumps’[meister2022](https://arxiv.org/html/2602.16539v1#bib.bib9) ; [meister2023](https://arxiv.org/html/2602.16539v1#bib.bib10)  accords with finite-resource constraints, and the exponential family provides the sufficient geometry to hold the Boojum at bay.

Open questions include: (1) Can the finite resource condition be formulated beyond the PKD theorem?
(2) Can the gradient-flow hypothesis in Section V be derived more simply?

## References

* (1)

  Boyling, J. B. (1968). “Carathéodory’s principle and the existence of global thermal variables.” Communications in Mathematical Physics, 10(1), 52-68.
* (2)
  Buchdahl, H. A., & W. Greve. (1962). “Entropy concept and ordering of states. II.” Zeitschrift für Physik 168.4: 386-391
* (3)
  Buchdahl, H. A. (1966). “The Concepts of Classical Thermodynamics”. Cambridge University Press.
* (4)
  Buchdahl, H. A. (1975). “Twenty Lectures on Thermodynamics”. Pergamon Press.
* (5)

  Carathéodory, C. (1909). “Untersuchungen über die Grundlagen der Thermodynamik”. Mathematische Annalen, 67(3), 355-386.
* (6)

  Yessenin-Volpin, A. S., (1970). “The ultra-intuitionistic criticism and the antitraditional program for foundations of mathematics”, in Intuitionism and Proof Theory (Proc. Conf. Buffalo, N.Y., 1968), North-Holland, Amsterdam, pp. 3–45.
* (7)

  Koopman, B. O. (1936). “On distributions admitting a sufficient statistic”. Transactions of the American Mathematical Society, 39(3), 399-409.
* (8)
  Lieb, E. H., & Yngvason, J. (1999). “The physics and mathematics of the second law of thermodynamics”. Physics Reports, 310(1), 1-96.
* (9)

  Meister, B. K. (2022).
  ”Meta-CTA Trading Strategies and Rational Market Failures”, arXiv:2209.05360.
* (10)

  Meister, B. K. (2023).
  “Gambling the World Away: Myopic Investors”, arXiv:2302.13994.
* (11)
   Onsager, L. (1931). “Reciprocal Relations in Irreversible Processes. I”. Physical Review, 37(4), 405.
* (12)
   Onsager, L. (1931). “Reciprocal Relations in Irreversible Processes. II”. Physical Review, 38(12), 2265.
* (13)

  Pitman, E. J. G. (1936). “Sufficient statistics and intrinsic accuracy”. Proceedings of the Cambridge Philosophical Society, 32, 567-579.