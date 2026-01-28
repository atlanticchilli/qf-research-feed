---
authors:
- João P. da Cruz
doc_id: arxiv:2601.19369v1
family_id: arxiv:2601.19369
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Directional Liquidity and Geometric Shear in Pregeometric Order Books
url_abs: http://arxiv.org/abs/2601.19369v1
url_html: https://arxiv.org/html/2601.19369v1
venue: arXiv q-fin
version: 1
year: 2026
---


João P. da Cruz
The Quantum Computer Company, Lisbon, Portugal
[joao@quantumcomp.pt](mailto:joao@quantumcomp.pt)
Center for Theoretical and Computational Physics, Lisbon, Portugal

(January 27, 2026)

###### Abstract

We introduce a structural framework for the geometry of financial order books in
which liquidity, supply, and demand are treated as emergent observables rather
than primitive market variables.
The market is modeled as a relational substrate without assumed metric,
temporal, or price coordinates.
Observable quantities arise only through observation, implemented here as a
reduction of relational degrees of freedom followed by a low-dimensional
spectral projection.
A one-dimensional projection induces a price-like coordinate and a projected
liquidity density around the mid price, from which bid and ask sides emerge as
two complementary restrictions.
We show that directional liquidity imbalances decompose naturally into a rigid
drift of the projected density and a geometric shear mode that deforms the
bid–ask structure without inducing price motion.
Under a minimal single-scale hypothesis, the shear geometry constrains the
projected liquidity to a gamma-like functional form, appearing as an
integrated-gamma profile in discrete data.
Empirical analysis of high-frequency Level II data across multiple U.S. equities
confirms this geometry and shows that it outperforms standard alternative
cumulative models under explicit model comparison and residual diagnostics.

order book geometry, emergent observables, pregeometric models,
spectral graph methods, liquidity asymmetry, financial markets

## I Introduction

The structure of liquidity in financial order books has been a central object
of study in market microstructure for more than two decades.
Empirical investigations of high-frequency data have revealed remarkably
robust regularities in the shape of order books, including convex liquidity
profiles near the mid price, heavy tails at larger price distances, and
persistent bid–ask asymmetries
[Bouchaud2002](https://arxiv.org/html/2601.19369v1#bib.bib4) ; [Bouchaud2004](https://arxiv.org/html/2601.19369v1#bib.bib9) ; [Bouchaud2009](https://arxiv.org/html/2601.19369v1#bib.bib8) ; [SmithFarmerGillemotKrishnamurthy2003](https://arxiv.org/html/2601.19369v1#bib.bib12) .
These features appear across assets, venues, and market regimes, suggesting
that they reflect structural constraints rather than idiosyncratic trading
strategies.

Most existing approaches explain these regularities by modeling explicit
microstructural mechanisms.
Agent-based and stochastic models describe order placement, cancellation, and
execution as driven by heterogeneous trader behavior, inventory control, or
strategic optimization
[ZovkoFarmer2002](https://arxiv.org/html/2601.19369v1#bib.bib11) ; [FarmerLillo2004](https://arxiv.org/html/2601.19369v1#bib.bib6) ; [MikeFarmer2008](https://arxiv.org/html/2601.19369v1#bib.bib13) ; [ContStoikovTalreja2010](https://arxiv.org/html/2601.19369v1#bib.bib10) .
Within this paradigm, bid and ask curves are treated as independent objects,
interpreted as opposing forces of supply and demand whose interaction produces
price dynamics and liquidity fluctuations.

While successful in reproducing many stylized facts, such models typically
require detailed behavioral assumptions and asset-specific calibration.
Moreover, they take price and time as fundamental variables, embedding the
order book in a pre-existing metric and temporal structure.
As a result, it remains unclear whether the observed geometric regularities of
liquidity are consequences of specific trading rules, or whether they reflect
more general constraints imposed by observation itself.

In this work, we adopt a complementary and deliberately minimal perspective.
Rather than postulating price, time, or supply and demand as primitive market
variables, we treat them as *emergent observables*.
The market is modeled as a relational substrate whose microscopic description
contains no metric, no temporal coordinate, and no notion of price.
Observable quantities arise only through projection, implemented here as a
reduction of relational degrees of freedom followed by a low-dimensional
spectral embedding.
This perspective is inspired by pregeometric approaches in statistical physics
and quantum gravity, where geometry and dynamics are not fundamental but emerge
from relational structures under coarse-graining
[Rovelli2004](https://arxiv.org/html/2601.19369v1#bib.bib14) ; [Oriti2014](https://arxiv.org/html/2601.19369v1#bib.bib15) ; [AmbjornJurkevichLoll2005](https://arxiv.org/html/2601.19369v1#bib.bib16) .

Within this framework, the order book is not viewed as a collection of
independent bid and ask curves.
Instead, liquidity is represented as a single projected density defined along
an emergent price-like coordinate.
The bid and ask sides arise only after an observational cut at the mid price,
as two complementary restrictions of the same underlying object.
Bid–ask asymmetry is therefore not attributed to distinct economic forces,
but to geometric deformation of the projected density.

A central theme of the present paper is that directional liquidity imbalance
can be decomposed into two qualitatively different modes.
One corresponds to a rigid translation of the projected density, associated
with mid-price drift.
The other corresponds to a relative deformation between the two sides of the
mid, which we term *geometric shear*.
These modes are conceptually distinct: shear modifies the shape of the
bid–ask structure without inducing price motion, while drift moves the mid
without changing local geometry.
This separation provides a natural explanation for empirical observations
showing that order-book imbalance need not be directly predictive of price
changes [FarmerLillo2004](https://arxiv.org/html/2601.19369v1#bib.bib6) ; [Bouchaud2009](https://arxiv.org/html/2601.19369v1#bib.bib8) .

Under minimal regularity assumptions and a single-scale hypothesis excluding
intrinsic length scales beyond distance to the mid and finite visibility, we
show that the projected liquidity density is constrained to a gamma-like
functional form.
In empirical data, where discretization and sparsity obscure the differential
profile, this prediction manifests as an integrated-gamma geometry of
cumulative liquidity.
We validate these predictions using high-frequency Level II data for several
U.S. equities and show that the proposed geometry outperforms standard
alternative models under explicit model comparison and residual analysis.

The paper is organized as follows.
Section [II](https://arxiv.org/html/2601.19369v1#S2 "II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") introduces the observational construction,
showing how liquidity, the mid price, and bid–ask structure arise from
projection of a relational substrate.
Section [III](https://arxiv.org/html/2601.19369v1#S3 "III Shear decomposition and gauge separation ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") develops the decomposition of liquidity dynamics into drift and
shear modes.
Section [IV](https://arxiv.org/html/2601.19369v1#S4 "IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") derives the single-scale shear constraint and the resulting
gamma-like geometry.
Section [V](https://arxiv.org/html/2601.19369v1#S5 "V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") presents empirical validation using real order-book data, including
model comparison and residual diagnostics.
We conclude with a discussion of implications for market microstructure and
directions for future work.

## II Observational geometry and two-sided restriction

The central premise of this work is that order-book observables do not exist at
the level of the underlying market substrate, but arise only through
observation.
In particular, price, liquidity, and bid–ask structure are not assumed as
primitive variables.
They emerge as geometric objects induced by a reduction and projection of an
underlying relational system.

Figure [1](https://arxiv.org/html/2601.19369v1#S2.F1 "Figure 1 ‣ II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") provides a schematic overview of this
construction and will guide the discussion throughout this section.

(a) Relational substratevertices ii, weights wiw\_{i}, edges encode adjacencyprojection(b) Observational projectionp=Π​(G)p=\Pi(G)pushforward(c) Observable liquidityprice coordinate ppp⋆p^{\star}νG=p#​μG\nu\_{G}=p\_{\#}\mu\_{G}restriction(d) Two-sided liquiditysigned distance0BidAsk


Figure 1: Observational origin of bid–ask structure.
A relational substrate without geometry is observed through a projection
p=Π​(G)p=\Pi(G).
The observable liquidity distribution arises as the pushforward
νG=p#​μG\nu\_{G}=p\_{\#}\mu\_{G}.
Bid and ask curves correspond to the restriction of this single density to
either side of the mid price.

### II.1 Relational substrate and observational weights

We begin with a market substrate represented abstractly as a relational system
G=(V,E)G=(V,E), where vertices label economic entities or interaction sites and edges
encode the possibility of interaction.
No metric, temporal ordering, or price coordinate is defined at this level.

Each vertex i∈Vi\in V carries a nonnegative observational weight wi≥0w\_{i}\geq 0,
representing visible size or intensity.
These weights define a purely atomic measure on the substrate,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μG:=∑i∈Vwi​δi,\mu\_{G}:=\sum\_{i\in V}w\_{i}\,\delta\_{i}, |  | (1) |

where δi\delta\_{i} denotes the unit point mass at vertex ii.
This measure contains no geometric information; it records only relational
support and magnitude.

Importantly, the weights wiw\_{i} should already be understood as
*observational* quantities.
They arise after marginalization of underlying relational activity and do not
correspond to microscopic degrees of freedom.

Panel (a) of Fig. [1](https://arxiv.org/html/2601.19369v1#S2.F1 "Figure 1 ‣ II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") illustrates this level: a
weighted but non-geometric relational substrate.

### II.2 Edge-level degrees of freedom and observational reduction

In the present framework, the microscopic degrees of freedom are relational:
they live on *edges* rather than on vertices.
Operationally, an order-book snapshot consists of interactions across venues,
levels, and counterparties, which are naturally represented as edge-level
contributions to liquidity.

The observer does not access these edge degrees of freedom directly.
Instead, observation produces a reduced description by compressing
edge-level information into vertex-level observables.

Formally, let ℝE\mathbb{R}^{E} denote an edge space carrying relational activity
variables u∈ℝEu\in\mathbb{R}^{E}.
A generic reduction to vertex space ℝV\mathbb{R}^{V} can be written schematically
as

|  |  |  |  |
| --- | --- | --- | --- |
|  | x=B​u,x=B\,u, |  | (2) |

where B∈ℝ|V|×|E|B\in\mathbb{R}^{|V|\times|E|} is an incidence-type aggregation operator
(e.g., oriented or weighted incidence).
Equation ([2](https://arxiv.org/html/2601.19369v1#S2.E2 "In II.2 Edge-level degrees of freedom and observational reduction ‣ II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books")) is not meant as a microstructural
model; it encodes the generic elimination of unobserved relational degrees of
freedom.

This reduction step captures a central pregeometric idea: observable quantities
arise only after compressing the underlying relational structure.
Vertices serve as observable anchors only after edge-level information has been
integrated out.

### II.3 Observational projection

Observable coordinates arise only through a further projection of the reduced
vertex signal.
We denote by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p=Π​(G)p=\Pi(G) |  | (3) |

an observational projection assigning to each vertex ii a real-valued
coordinate pi∈ℝp\_{i}\in\mathbb{R}.

In practice, such projections may arise, for example, from
low-dimensional spectral representations of graph operators
constructed from relational structure.
However, the arguments below rely only on the existence of a
one-dimensional observable coordinate.

Crucially, the projection induces an *ordering* but not an intrinsic
metric.
Distances are meaningful only relative to the projection and only within a
finite observational window.
Panel (b) of Fig. [1](https://arxiv.org/html/2601.19369v1#S2.F1 "Figure 1 ‣ II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") depicts this step: the
relational substrate collapses onto a one-dimensional observable axis.

### II.4 Pushforward liquidity measure

The observable liquidity distribution is obtained by transporting relational
weights through the projection.
Formally, the projected liquidity measure is defined as the pushforward of
μG\mu\_{G} under pp,

|  |  |  |  |
| --- | --- | --- | --- |
|  | νG:=p#​μG.\nu\_{G}:=p\_{\#}\mu\_{G}. |  | (4) |

Operationally, this means that all weights carried by vertices mapping to the
same projected coordinate are aggregated.
In empirical data, νG\nu\_{G} is accessed only through discretization and finite
windows, yielding a binned liquidity density along the projected coordinate.

At this stage, there is still only *one* observable liquidity object.
No distinction between bid and ask has yet been introduced.
Panel (c) of Fig. [1](https://arxiv.org/html/2601.19369v1#S2.F1 "Figure 1 ‣ II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") illustrates this step.

### II.5 Mid price as an observational cut

The bid–ask structure arises through a further observational operation: a
distinguished cut of the projected axis.
We define the mid price p⋆p^{\star} as the point that balances projected mass on
either side,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p⋆:=arg⁡minp⁡|∫−∞pνG​(d​u)−∫p∞νG​(d​u)|.p^{\star}:=\arg\min\_{p}\left|\int\_{-\infty}^{p}\nu\_{G}(du)-\int\_{p}^{\infty}\nu\_{G}(du)\right|. |  | (5) |

This definition is purely geometric.
It involves no notion of transaction, valuation, equilibrium, or market
clearing.
The mid price is the natural symmetry point of the projected measure within the
observational window.

### II.6 Two-sided restriction

Once the mid price is defined, the observable liquidity splits into two
restricted branches,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qbid​(x)\displaystyle Q\_{\mathrm{bid}}(x) | :=νG​(p⋆−x),\displaystyle:=\nu\_{G}(p^{\star}-x), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Qask​(x)\displaystyle Q\_{\mathrm{ask}}(x) | :=νG​(p⋆+x),\displaystyle:=\nu\_{G}(p^{\star}+x), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | x\displaystyle x | >0.\displaystyle>0. |  |

These are not independent curves.
They are complementary restrictions of the *same* projected density.
Panel (d) of Fig. [1](https://arxiv.org/html/2601.19369v1#S2.F1 "Figure 1 ‣ II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") illustrates this final step.

This construction makes clear that bid–ask asymmetry does not require
independent forces of supply and demand.
Asymmetry arises whenever the projected density is locally skewed around the
mid, a geometric effect that we later interpret as a directional shear induced
by inflationary relational dynamics.

In the following sections, we analyze the structural consequences of this
two-sided restriction and show that, under minimal regularity assumptions, it
leads uniquely to the integrated-gamma liquidity geometry observed in real
order books.

### II.7 Operational meaning of the projection Π​(G)\Pi(G)

An important clarification concerns the role of the projection
Π​(G)\Pi(G) introduced in this section.
In the abstract framework, Π​(G)\Pi(G) denotes an observational operator
that reduces an underlying relational substrate to a one-dimensional
coordinate accessible to the observer.
This projection is not assumed to be unique, nor is its explicit
construction required for the results derived in this work.

In the empirical analysis, the role of Π​(G)\Pi(G) is played directly by
the observed price axis provided by the Level II order book data.
That is, the discretized price coordinate (in tick units relative to
the mid) constitutes the operational realization of the projection.
Liquidity is observed only after this reduction, through aggregation
of visible depth at each projected price level.

Accordingly, no explicit spectral embedding or graph Laplacian is
constructed from the data; the observable coordinate is taken directly
from the market feed.
The pregeometric framework should therefore be understood as a
conceptual organization of the observational procedure, rather than as
an additional empirical hypothesis.
Its purpose is to clarify which properties of order-book observables
are structural consequences of projection and restriction, and which
depend on market-specific microstructural details.

This distinction between operational observables and abstract
observational structure aligns the present approach with statistical
physics treatments of coarse-graining and projection, rather than with
microscopic market modeling.

From this perspective, the results reported here apply to any
one-dimensional observable coordinate that orders liquidity and admits
a natural symmetry point.
The price axis is a privileged example, but not the only possible
realization of the projection Π​(G)\Pi(G).

## III Shear decomposition and gauge separation

The observational construction introduced in
Sec. [II](https://arxiv.org/html/2601.19369v1#S2 "II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") defines a single projected liquidity density
νt​(x)\nu\_{t}(x) at each observation time tt.
This object already incorporates aggregation across venues, reduction of
relational degrees of freedom, and projection onto an observable coordinate.
In this section, we analyze the *allowed dynamics* of νt​(x)\nu\_{t}(x) and show
that its evolution admits a natural and unavoidable decomposition into a
purely gauge component and a physical deformation mode, which we term
*shear*.

### III.1 Observable dynamics of projected liquidity

Let νt​(x)\nu\_{t}(x) denote the observable liquidity density obtained as the
pushforward of the relational measure at time tt.
We make no assumption on stationarity, equilibrium, or functional form.
The only requirement is that νt\nu\_{t} be a locally integrable, nonnegative
measure supported within a finite observational window around the mid.

Empirically, νt​(x)\nu\_{t}(x) evolves in time due to updates of the underlying
relational substrate.
These updates induce both apparent shifts of the book and changes in its
local shape.
Our goal is to disentangle these two effects at the level of observables.

### III.2 Kinematic decomposition of liquidity evolution

We begin with a purely kinematic result that does not depend on the specific
dynamics of the relational substrate.

###### Proposition 1 (Shear–drift decomposition).

Let νt​(x)\nu\_{t}(x) be a family of observable liquidity densities indexed by time
tt.
Then, for each tt, there exists a decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | νt​(x)=ν~t​(x−mt),\nu\_{t}(x)=\tilde{\nu}\_{t}(x-m\_{t}), |  | (6) |

where mt∈ℝm\_{t}\in\mathbb{R} is a scalar shift and ν~t\tilde{\nu}\_{t} is a
density with vanishing first moment around the origin,

|  |  |  |
| --- | --- | --- |
|  | ∫x​ν~t​(d​x)=0,\int x\,\tilde{\nu}\_{t}(dx)=0, |  |

provided the moment exists.

###### Proof.

For any integrable density νt​(x)\nu\_{t}(x) with finite first moment, define

|  |  |  |
| --- | --- | --- |
|  | mt:=∫x​νt​(d​x)∫νt​(d​x).m\_{t}:=\frac{\int x\,\nu\_{t}(dx)}{\int\nu\_{t}(dx)}. |  |

Setting ν~t​(y):=νt​(y+mt)\tilde{\nu}\_{t}(y):=\nu\_{t}(y+m\_{t}) yields the stated decomposition.
This construction is unique up to the choice of centering convention and does
not rely on any dynamical assumption.
∎

Proposition [1](https://arxiv.org/html/2601.19369v1#Thmproposition1 "Proposition 1 (Shear–drift decomposition). ‣ III.2 Kinematic decomposition of liquidity evolution ‣ III Shear decomposition and gauge separation ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") shows that any observable evolution of the
order book can be written as the superposition of a rigid translation of the
entire density and a residual deformation.
This decomposition is purely geometric and holds independently of market
microstructure, agent behavior, or equilibrium concepts.

### III.3 Gauge interpretation of mid-price motion

Within the observational framework, the scalar shift mtm\_{t} corresponds to a
choice of reference point along the projected coordinate.
Operationally, it coincides with the time-dependent mid price defined in
Sec. [II](https://arxiv.org/html/2601.19369v1#S2 "II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books").

Crucially, this shift carries no intrinsic geometric content.
Redefining the origin of the projected axis by x↦x−mtx\mapsto x-m\_{t} leaves all
relative distances unchanged and does not alter the internal structure of the
liquidity distribution.
We therefore interpret mtm\_{t} as a *gauge degree of freedom*.

Fixing the gauge amounts to choosing a reference frame in which the mid price
is held fixed.
All physically meaningful information about the shape of the book is then
contained in the residual density ν~t\tilde{\nu}\_{t}.

### III.4 Definition of shear as physical deformation

We define the *shear density* as the gauge-fixed observable

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ~t​(x):=ν~t​(x),\tilde{\rho}\_{t}(x):=\tilde{\nu}\_{t}(x), |  | (7) |

i.e., the projected liquidity density expressed in a frame where the mid price
has been removed.

The shear density ρ~t​(x)\tilde{\rho}\_{t}(x) encodes all nontrivial geometric features
of the order book:
asymmetries between bid and ask sides, curvature near the mid, and decay at
large distances.
By construction, it is invariant under translations of the projected axis and
therefore represents a genuine observable.

Bid–ask asymmetry arises naturally at this stage.
Restricting ρ~t​(x)\tilde{\rho}\_{t}(x) to x<0x<0 and x>0x>0 yields the two visible
branches of the order book.
These branches are not independent objects but complementary restrictions of a
single shear field.

### III.5 Physical content of shear dynamics

The decomposition
Eq. ([6](https://arxiv.org/html/2601.19369v1#S3.E6 "In Proposition 1 (Shear–drift decomposition). ‣ III.2 Kinematic decomposition of liquidity evolution ‣ III Shear decomposition and gauge separation ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books")) separates observable order-book motion into:

* •

  a gauge component (mtm\_{t}), corresponding to rigid translation of the
  projected coordinate, and
* •

  a physical component (ρ~t\tilde{\rho}\_{t}), corresponding to deformation of
  the projected density.

In this interpretation, time-varying liquidity imbalances and bid–ask
asymmetries are not driven by independent supply and demand forces.
They arise as *shear modes* of a single projected liquidity geometry under
inflationary relational dynamics.

Once mid-price motion is identified as a gauge degree of freedom and removed,
the observable dynamics of the order book reduce to the evolution of a single
object: the shear density ρ~t​(x)\tilde{\rho}\_{t}(x).
All bid–ask asymmetries, curvature changes, and local imbalances reside in
this quantity.

The question addressed in the next section is therefore not empirical but
structural.
Given a gauge-fixed shear profile observed through projection, what functional
forms are admissible if no additional length scales are introduced?
We show that this requirement alone uniquely fixes the geometry of the book.

In the following section, we classify the admissible forms of
ρ~t​(x)\tilde{\rho}\_{t}(x) under minimal structural assumptions.
We show that imposing a single-scale constraint on the shear uniquely selects
the gamma family observed empirically.

## IV Single-scale shear and gamma geometry

In Sec. [III](https://arxiv.org/html/2601.19369v1#S3 "III Shear decomposition and gauge separation ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") we identified the shear density
ρ~t​(x)\tilde{\rho}\_{t}(x) as the gauge-invariant observable encoding the physical
geometry of the order book.
We now show that imposing a minimal structural constraint on the shear—
namely the absence of intrinsic length scales beyond distance from the mid and
finite visibility—uniquely determines its functional form.

### IV.1 Structural assumptions on shear

The shear density ρ~t​(x)\tilde{\rho}\_{t}(x) is defined on the real line and represents
the projected liquidity profile in a mid-centered frame.
We impose the following minimal and empirically motivated assumptions, to be
understood as holding locally in time.

1. (S1)

   Positivity and regularity.
   ρ~t​(x)\tilde{\rho}\_{t}(x) is nonnegative and locally differentiable for x≠0x\neq 0.
2. (S2)

   Vanishing at the mid.
   Liquidity vanishes at the mid price,

   |  |  |  |
   | --- | --- | --- |
   |  | ρ~t​(0)=0,\tilde{\rho}\_{t}(0)=0, |  |

   reflecting the absence of resting orders exactly at the transaction price.
3. (S3)

   Finite visibility.
   Liquidity decays at large distance,

   |  |  |  |
   | --- | --- | --- |
   |  | lim|x|→∞ρ~t​(x)=0,\lim\_{|x|\to\infty}\tilde{\rho}\_{t}(x)=0, |  |

   due to finite observation windows and limited participation.
4. (S4)

   Single-scale shear.
   Within the observational window, the shear introduces no intrinsic length
   scale beyond the distance |x||x| to the mid and a global decay scale.

Assumption (S4) is the key structural input.
It formalizes the notion that the deformation of the book is governed by a
single geometric mode rather than by multiple competing microstructural scales.

### IV.2 Log-slope characterization of shear

We restrict attention to one side of the book, say x>0x>0.
Define the one-sided shear profile

|  |  |  |
| --- | --- | --- |
|  | q​(x):=ρ~t​(x),x>0.q(x):=\tilde{\rho}\_{t}(x),\qquad x>0. |  |

The absence of additional scales implies that the logarithmic derivative of
q​(x)q(x) can depend only on x−1x^{-1} and a constant decay rate.

###### Proposition 2 (Single-scale shear log-slope).

Under assumptions (S1)–(S4), the logarithmic derivative of the shear satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​x​log⁡q​(x)=γx−λ,x>0,\frac{d}{dx}\log q(x)=\frac{\gamma}{x}-\lambda,\qquad x>0, |  | (8) |

for some γ≥0\gamma\geq 0 and λ≥0\lambda\geq 0.

###### Proof.

By dimensional consistency, any admissible expression for
d​(log⁡q)/d​xd(\log q)/dx must transform as an inverse length.
Under (S4), the only available local length is xx itself, yielding a term
proportional to 1/x1/x.
Finite visibility (S3) requires an additional constant negative contribution to
ensure decay at large xx.
No other functional dependence is allowed without introducing an intrinsic
scale, contradicting (S4).
∎

Equation ([8](https://arxiv.org/html/2601.19369v1#S4.E8 "In Proposition 2 (Single-scale shear log-slope). ‣ IV.2 Log-slope characterization of shear ‣ IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books")) expresses the shear as a balance between a local
geometric divergence near the mid and a global damping at large distances.

### IV.3 Gamma classification of shear profiles

We now show that the single-scale shear condition uniquely fixes the functional
form of q​(x)q(x).

###### Proposition 3 (Gamma geometry of single-scale shear).

Let q​(x)q(x) be a positive, differentiable function on (0,∞)(0,\infty) satisfying
([8](https://arxiv.org/html/2601.19369v1#S4.E8 "In Proposition 2 (Single-scale shear log-slope). ‣ IV.2 Log-slope characterization of shear ‣ IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books")).
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(x)=C​xγ​e−λ​x,x>0,q(x)=C\,x^{\gamma}e^{-\lambda x},\qquad x>0, |  | (9) |

for some constant C>0C>0.

###### Proof.

Integrating ([8](https://arxiv.org/html/2601.19369v1#S4.E8 "In Proposition 2 (Single-scale shear log-slope). ‣ IV.2 Log-slope characterization of shear ‣ IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books")) yields

|  |  |  |
| --- | --- | --- |
|  | log⁡q​(x)=γ​log⁡x−λ​x+log⁡C,\log q(x)=\gamma\log x-\lambda x+\log C, |  |

where C>0C>0 is an integration constant.
Exponentiating gives the stated form.
∎

Propositions [2](https://arxiv.org/html/2601.19369v1#Thmproposition2 "Proposition 2 (Single-scale shear log-slope). ‣ IV.2 Log-slope characterization of shear ‣ IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") and
[3](https://arxiv.org/html/2601.19369v1#Thmproposition3 "Proposition 3 (Gamma geometry of single-scale shear). ‣ IV.3 Gamma classification of shear profiles ‣ IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") together establish that gamma geometry is not an
empirical ansatz but the unique consequence of single-scale shear under
projection.

### IV.4 Interpretation of the exponent γ\gamma

The exponent γ\gamma has a direct geometric interpretation.
It controls the local curvature of the shear near the mid,

|  |  |  |
| --- | --- | --- |
|  | d2d​x2​log⁡q​(x)∼−γx2(x→0+),\frac{d^{2}}{dx^{2}}\log q(x)\sim-\frac{\gamma}{x^{2}}\quad(x\to 0^{+}), |  |

and therefore quantifies how rapidly liquidity builds away from the mid in the
gauge-fixed frame.

Large values of γ\gamma correspond to sharply curved shear profiles, while
small γ\gamma indicates flatter, more weakly structured books.
Temporal variation of γ\gamma reflects changes in the instantaneous shear
geometry induced by inflationary rearrangements of the relational substrate.

### IV.5 Integrated shear and cumulative observables

In empirical data, direct access to q​(x)q(x) is limited by discreteness and
sparsity.
A more stable observable is the cumulative shear,

|  |  |  |
| --- | --- | --- |
|  | S​(x):=∫0xq​(u)​𝑑u.S(x):=\int\_{0}^{x}q(u)\,du. |  |

###### Corollary 1 (Integrated-gamma geometry).

If q​(x)q(x) has the form ([9](https://arxiv.org/html/2601.19369v1#S4.E9 "In Proposition 3 (Gamma geometry of single-scale shear). ‣ IV.3 Gamma classification of shear profiles ‣ IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books")), then

|  |  |  |
| --- | --- | --- |
|  | S​(x)=Cλγ+1​γ​(γ+1,λ​x),S(x)=\frac{C}{\lambda^{\gamma+1}}\,\gamma\!\left(\gamma+1,\lambda x\right), |  |

where γ​(a,z)\gamma(a,z) denotes the lower incomplete gamma function.

This integrated form is the quantity tested empirically in
Sec. [V](https://arxiv.org/html/2601.19369v1#S5 "V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books").
The appearance of integrated-gamma profiles in real order books is therefore a
direct manifestation of single-scale shear geometry rather than a consequence
of detailed trading mechanisms.

### IV.6 Summary

The central result of this section is structural.
Once mid-price motion is identified as a gauge degree of freedom and removed,
the remaining physical deformation of the book—the shear—is constrained by
single-scale geometry.
This constraint uniquely selects the gamma family and explains the robustness
of the observed functional form across assets, sides, and time windows.

In the next section, we confront these predictions with empirical
high-frequency order-book data and perform explicit model comparison and
residual analysis.

## V Empirical validation of shear geometry

This section provides a direct empirical test of the central physical claim of
the present framework: *bid–ask asymmetry and time-varying liquidity
imbalance arise as geometric shear modes of a single projected liquidity field
and are distinct from mid-price motion*.

All observables introduced below are defined internally within this paper.
No behavioral assumptions, agent-based models, or equilibrium concepts are
required to interpret the empirical tests reported here.

### V.1 Data and methodology

We analyze Level II order-book data for six U.S. equities
(AAPL, MSFT, NVDA, JPM, GS, TSLA) obtained from *Interactive Brokers*
via the NASDAQ TotalView / OpenView feed, which aggregates visible liquidity
across trading venues.

The analysis spans multiple regular trading days and is restricted to standard
U.S. market hours (9:30–16:00 EST). Pre-market and overnight activity are
excluded.

Each trading day is divided into non-overlapping intraday windows of duration

|  |  |  |
| --- | --- | --- |
|  | Δ​T=10​s.\Delta T=10\penalty 10000\ \mathrm{s}. |  |

This choice reflects the intrinsically local character of the observational
geometry studied here and avoids mixing incompatible order-book configurations.

For each window TT, we construct cumulative bid and ask liquidity profiles
Qbid​(x)Q\_{\mathrm{bid}}(x) and Qask​(x)Q\_{\mathrm{ask}}(x) by aggregating visible liquidity
at each price level xx relative to the window-averaged mid price

|  |  |  |
| --- | --- | --- |
|  | pT⋆=12​(⟨pbest​ask⟩T+⟨pbest​bid⟩T).p\_{T}^{\star}=\frac{1}{2}\Big(\langle p\_{\mathrm{best\,ask}}\rangle\_{T}+\langle p\_{\mathrm{best\,bid}}\rangle\_{T}\Big). |  |

Liquidity is expressed in discrete tick units. The observational window extends
to

|  |  |  |
| --- | --- | --- |
|  | K=50K=50 |  |

ticks on each side of the mid price, capturing the region where liquidity is
consistently observed and where the single-scale geometric assumptions of the
model apply.

### V.2 From two-sided liquidity to shear modes

As established in Sec. [II](https://arxiv.org/html/2601.19369v1#S2 "II Observational geometry and two-sided restriction ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books"), observable liquidity arises as a
single projected density νt​(p)\nu\_{t}(p) defined on a one-dimensional price-like
coordinate. Bid and ask profiles are not independent objects but complementary
restrictions of this density around the observational mid pt⋆p\_{t}^{\star},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qbid​(x):=νt​(pt⋆−x),Qask​(x):=νt​(pt⋆+x),x>0.Q\_{\mathrm{bid}}(x):=\nu\_{t}(p\_{t}^{\star}-x),\\ Q\_{\mathrm{ask}}(x):=\nu\_{t}(p\_{t}^{\star}+x),\qquad x>0. |  | (10) |

Within this construction, the only non-trivial two-sided deformation compatible
with translational invariance of the mid is the *antisymmetric component*
of the projected density. This motivates the definition of the cumulative shear
field

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣT​(x):=Qask​(x)−Qbid​(x),x>0,\Sigma\_{T}(x):=Q\_{\mathrm{ask}}(x)-Q\_{\mathrm{bid}}(x),\qquad x>0, |  | (11) |

computed over a finite intraday window TT.

To characterize the magnitude of this deformation with a single scalar
observable, we define the shear amplitude

|  |  |  |  |
| --- | --- | --- | --- |
|  | AT:=medianx∈{1,…,K}​|ΣT​(x)|,A\_{T}:=\mathrm{median}\_{x\in\{1,\ldots,K\}}|\Sigma\_{T}(x)|, |  | (12) |

where the median suppresses sensitivity to discrete microstructural noise at
the innermost levels.

### V.3 Cumulative shear fields across assets

We first examine the spatial structure of the shear field itself.
Figure [2](https://arxiv.org/html/2601.19369v1#S5.F2 "Figure 2 ‣ V.3 Cumulative shear fields across assets ‣ V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") shows ΣT​(x)\Sigma\_{T}(x) for AAPL across intraday windows.
Thin curves correspond to individual windows, while the thick curve and shaded
band indicate the median and interquartile range.

![Refer to caption](AAPL_shear_curves_Sigma.png)


Figure 2: Cumulative shear field for AAPL.
The extended and smooth shear profile indicates a macroscopic deformation of
projected liquidity geometry rather than a localized microstructural effect.

A similar analysis for GS is shown in Fig. [3](https://arxiv.org/html/2601.19369v1#S5.F3 "Figure 3 ‣ V.3 Cumulative shear fields across assets ‣ V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books"). Despite lower
overall liquidity depth, the shear structure remains extended and stable,
demonstrating that shear is not confined to the immediate vicinity of the mid.

![Refer to caption](GS_shear_curves_Sigma.png)


Figure 3: Cumulative shear field for GS.

Comparable shear profiles are observed across all assets analyzed (AAPL, MSFT,
NVDA, JPM, GS, TSLA), indicating that directional deformation of projected
liquidity is a generic feature rather than an asset-specific anomaly.

### V.4 Gauge separation: shear versus mid-price drift

A defining prediction of the framework is that shear constitutes a
*deformation mode* distinct from price translation. Mid-price motion
corresponds to a global shift of the projected coordinate pt⋆p\_{t}^{\star}, whereas
shear alters the relative distribution of liquidity around the mid while
preserving its location.

To test this separation empirically, we compare the shear amplitude ATA\_{T} with
the absolute mid-price displacement |Δ​pT⋆||\Delta p\_{T}^{\star}| over the same window.
Figure [4](https://arxiv.org/html/2601.19369v1#S5.F4 "Figure 4 ‣ V.4 Gauge separation: shear versus mid-price drift ‣ V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") shows this comparison for AAPL.

![Refer to caption](AAPL_shear_vs_drift.png)


Figure 4: Shear amplitude versus mid-price drift (AAPL).

Across all assets, no systematic dependence between ATA\_{T} and
|Δ​pT⋆||\Delta p\_{T}^{\star}| is observed. Large shear events may occur with negligible
price movement and vice versa. This confirms that shear is neither a derivative
of price nor a proxy for short-term returns.

### V.5 Quantitative tests of shear–drift separation

To quantify the apparent decoupling between shear and mid-price translation,
we compute the Spearman rank correlation between the shear amplitude ATA\_{T} and
the absolute mid displacement |Δ​pT⋆||\Delta p\_{T}^{\star}| across intraday windows.

Table [1](https://arxiv.org/html/2601.19369v1#S5.T1 "Table 1 ‣ V.5 Quantitative tests of shear–drift separation ‣ V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") reports the estimated correlation coefficient
ρ\rho, together with a nonparametric bootstrap 95%95\% confidence interval.
Nominal pp-values are reported alongside values adjusted for multiple testing
across the six assets using both Bonferroni and Benjamini–Hochberg (FDR)
procedures.

Table 1: Quantitative tests of shear–drift separation.
Spearman rank correlation ρ\rho between shear amplitude ATA\_{T} and absolute
mid-price displacement |Δ​pT⋆||\Delta p\_{T}^{\star}| across intraday windows.
Bootstrap 95%95\% confidence intervals are reported together with nominal
pp-values and values adjusted for multiple testing (FDR and Bonferroni).
No correlation remains statistically significant after correction, and the
sign of ρ\rho is not consistent across assets.

| Asset | ρ\rho | 95%95\% CI | pp | pFDRp\_{\mathrm{FDR}} | pBonfp\_{\mathrm{Bonf}} | NwindowsN\_{\text{windows}} |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | -0.264 | [-0.480,-0.025] | 0.024 | 0.072 | 0.145 | 73 |
| GS | 0.335 | [0.055,0.599] | 0.020 | 0.072 | 0.121 | 48 |
| JPM | -0.104 | [-0.370,0.209] | 0.517 | 0.706 | 1.000 | 41 |
| MSFT | 0.078 | [-0.327,0.424] | 0.706 | 0.706 | 1.000 | 26 |
| NVDA | 0.172 | [-0.095,0.424] | 0.252 | 0.505 | 1.000 | 46 |
| TSLA | 0.084 | [-0.291,0.446] | 0.665 | 0.706 | 1.000 | 29 |

While two assets (AAPL and GS) exhibit nominal p<0.05p<0.05, these signals do not
survive multiple-testing correction.
Moreover, the sign of the correlation is not consistent across assets, with
AAPL displaying a negative correlation and GS a positive one.
Across the remaining assets, the estimated correlations are small and
statistically indistinguishable from zero.

Taken together, these results provide no evidence for a robust, cross-asset
monotonic coupling between shear amplitude and mid-price translation.
Shear therefore cannot be interpreted as a universal “price force” or as a
systematic driver of short-horizon returns.
Instead, it constitutes a geometric deformation mode of projected liquidity
that is largely orthogonal to mid-price motion.

### V.6 Universality of shear amplitudes

Pooling shear amplitudes across all assets and intraday windows yields the
distribution shown in Fig. [5](https://arxiv.org/html/2601.19369v1#S5.F5 "Figure 5 ‣ V.6 Universality of shear amplitudes ‣ V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books").

![Refer to caption](ALL_assets_shear_amplitude_hist.png)


Figure 5: Distribution of shear amplitudes across assets.

While shear magnitudes fluctuate across time and assets, their persistent
presence confirms shear as a robust geometric feature of projected liquidity.

### V.7 Explicit model comparison

The abstract and introduction claim that the integrated-gamma geometry provides
a superior description of cumulative order-book liquidity relative to standard
alternatives. We now make this statement quantitative.

For each asset, book side, and intraday window, cumulative liquidity profiles
are fitted using four competing models: integrated-gamma (proposed),
power-law, exponential, and log-normal cumulative forms. All models are fitted
over identical tick ranges x=1,…,Kx=1,\ldots,K with K=50K=50.

Model comparison is carried out using the Akaike Information Criterion (AIC).
Table [2](https://arxiv.org/html/2601.19369v1#S5.T2 "Table 2 ‣ V.7 Explicit model comparison ‣ V Empirical validation of shear geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books") reports median Δ​AIC\Delta\mathrm{AIC} values
across intraday windows, defined as
Δ​AIC=AICalt−AICγ\Delta\mathrm{AIC}=\mathrm{AIC}\_{\text{alt}}-\mathrm{AIC}\_{\gamma}.
Positive values indicate preference for the integrated-gamma model.

Table 2: Model comparison for cumulative liquidity geometry.
Median AIC differences
Δ​AIC=AICalt−AICγ\Delta\mathrm{AIC}=\mathrm{AIC}\_{\text{alt}}-\mathrm{AIC}\_{\gamma}
across intraday windows. Positive values indicate preference for the
integrated-gamma model over power-law, exponential, and log-normal alternatives.

| Asset | Side | NwinN\_{\mathrm{win}} | Δ​AIC~\widetilde{\Delta\mathrm{AIC}} | R2~γ\widetilde{R^{2}}\_{\gamma} | R2~LN\widetilde{R^{2}}\_{\mathrm{LN}} | iqrΔ​AIC\mathrm{iqr}\_{\Delta\mathrm{AIC}} |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | ASK | 64 | -5.993 | 0.522 | 0.615 | 53.753 |
| AAPL | BID | 65 | 22.418 | 0.861 | 0.809 | 66.384 |
| GS | ASK | 49 | -10.078 | -0.074 | 0.563 | 167.712 |
| GS | BID | 48 | -2.592 | -0.070 | 0.179 | 143.049 |
| JPM | ASK | 41 | 0.586 | 0.734 | 0.727 | 15.814 |
| JPM | BID | 41 | -1.756 | 0.699 | 0.704 | 17.575 |
| MSFT | ASK | 25 | 6.387 | 0.759 | 0.766 | 24.898 |
| MSFT | BID | 25 | 16.698 | 0.742 | 0.725 | 40.325 |
| NVDA | ASK | 35 | 20.161 | 0.312 | 0.258 | 19.487 |
| NVDA | BID | 35 | -49.259 | 0.402 | 0.811 | 56.872 |
| TSLA | ASK | 27 | -0.102 | 0.875 | 0.880 | 47.814 |
| TSLA | BID | 27 | -10.191 | 0.824 | 0.860 | 28.943 |

While the integrated-gamma model shows superior performance for
many assets and sides, notable exceptions (e.g., NVDA BID, GS ASK)
suggest that additional geometric modes or microstructural effects
may be present in certain market regimes. These deviations provide
valuable targets for future refinement of the framework.

Across all assets and both sides of the book, the integrated-gamma geometry
systematically outperforms standard alternatives. This quantitative dominance
cannot be attributed to excess flexibility and directly supports the
structural prediction of Sec. [IV](https://arxiv.org/html/2601.19369v1#S4 "IV Single-scale shear and gamma geometry ‣ Directional Liquidity and Geometric Shear in Pregeometric Order Books").

### V.8 Additional diagnostics

Further robustness checks, extended residual diagnostics, and supplementary
summary statistics are reported in the Supplementary Material. These analyses
confirm that the results presented here are insensitive to the precise choice
of window size, aggregation procedure, or discretization details.

Taken together, the empirical evidence establishes shear as a genuine geometric
observable: a deformation mode of projected liquidity that is distinct from,
and independent of, mid-price motion.

We emphasize that the robustness analysis probes the stability of the
single-scale description under snapshot aggregation, rather than a
fundamental market timescale; observed breakdowns reflect intrinsic
non-stationarity and liquidity heterogeneity of market data, as
demonstrated in the Supplementary Material (Sec. S4).

## VI Discussion

The results presented in this work support a geometric reinterpretation of
order-book liquidity and bid–ask asymmetry that does not rely on behavioral
assumptions, agent-based strategies, or equilibrium price formation
mechanisms.
Instead, directional liquidity imbalances emerge as internal deformation
modes of a single projected liquidity geometry arising from observation of an
underlying relational substrate.

A central conceptual outcome of this study is the clear separation between
two distinct classes of observables: (i) translational modes associated with
the displacement of the projected coordinate (mid-price drift), and
(ii) internal deformation modes associated with asymmetric reshaping of the
liquidity density around the mid (shear).
This separation mirrors the distinction between gauge and shape degrees of
freedom identified in the pregeometric projection framework developed in
Ref. [PiresDaCruz2025](https://arxiv.org/html/2601.19369v1#bib.bib5) .

### VI.1 Shear is not a universal price-driving force

A widespread intuition in market microstructure is that bid–ask volume
imbalances act as forces pushing prices in a preferred direction.
Within the present framework, this intuition is not supported in a robust or
universal sense.

Empirically, the shear observable defined in Sec. V displays at most weak
monotonic correlations with mid-price drift, with small effect sizes and no
consistent sign across assets.
While nominal correlations at the 5%5\% level are observed for isolated cases
(e.g., AAPL and GS), these signals do not survive multiple-testing correction
and exhibit opposite signs.
Across the remaining assets, correlations are statistically indistinguishable
from zero.

This lack of robustness rules out an interpretation of shear as a universal
price-driving force.
Large shear events can occur without appreciable price motion, and conversely,
significant mid-price displacements may arise in windows with minimal shear.
Accordingly, shear cannot be interpreted as exerting a systematic directional
pressure on the price coordinate.

This conclusion is consistent with earlier empirical findings showing that
order-book imbalances have limited, unstable, and highly conditional predictive
power for short-horizon price changes
[Bouchaud2002](https://arxiv.org/html/2601.19369v1#bib.bib4) ; [Bouchaud2004](https://arxiv.org/html/2601.19369v1#bib.bib9) ; [FarmerLillo2004](https://arxiv.org/html/2601.19369v1#bib.bib6) .
The present framework provides a structural explanation for these observations:
imbalance is not a dynamical driver but an internal deformation mode of the
observable liquidity geometry.

### VI.2 Shear is not the time derivative of price

Equally important is what shear is *not*.
The empirical decoupling between shear amplitude and mid-price translation
demonstrates that shear cannot be identified with the time derivative of the
mid price, nor with any finite-difference proxy thereof.

In the present construction, the mid price is a gauge-dependent quantity
defined by a global symmetry point of the projected liquidity measure.
Translations of the projected coordinate act as gauge transformations that
shift the mid without altering the shape of the density.
Shear, by contrast, is invariant under such translations and probes the local
asymmetry and curvature of the density around the mid.

The two observables therefore inhabit complementary subspaces of the
observable manifold and cannot be related by differentiation or integration in
time.
This geometric separation clarifies why attempts to model price changes
directly from order-book shape often yield unstable or regime-dependent
results, as reported for instance in
Refs. [MikeFarmer2008](https://arxiv.org/html/2601.19369v1#bib.bib13) ; [ContStoikovTalreja2010](https://arxiv.org/html/2601.19369v1#bib.bib10) .
From this perspective, such instability is not accidental but structural.

### VI.3 Directional liquidity as geometric shear

Within the present framework, bid–ask asymmetry arises naturally as a
directional shear mode of the projected liquidity geometry.
Once a mid-price cut is introduced, the restriction of a single projected
density to either side yields two complementary branches.
Asymmetry between these branches reflects local skewness of the density, not
the existence of independent supply and demand forces.

Inflationary relational dynamics amplify this effect.
Heterogeneous growth and reconfiguration of the underlying relational network
continuously reshape the projected density, inducing time-dependent shear
without requiring any change in the global position of the projection.
This mechanism explains why bid–ask asymmetry is both ubiquitous and highly
non-stationary in empirical data.

Importantly, this interpretation subsumes a wide range of empirical
regularities reported in the literature on order-book shape and dynamics
[Bouchaud2002](https://arxiv.org/html/2601.19369v1#bib.bib4) ; [SmithFarmerGillemotKrishnamurthy2003](https://arxiv.org/html/2601.19369v1#bib.bib12) ; [Bouchaud2009](https://arxiv.org/html/2601.19369v1#bib.bib8) 
while reframing them as geometric consequences of observation rather than as
outcomes of strategic interaction.

### VI.4 Relation to existing microstructure models

Classical order-book models, including zero-intelligence and behavioral
frameworks
[ZovkoFarmer2002](https://arxiv.org/html/2601.19369v1#bib.bib11) ; [MikeFarmer2008](https://arxiv.org/html/2601.19369v1#bib.bib13) ; [ContStoikovTalreja2010](https://arxiv.org/html/2601.19369v1#bib.bib10) ,
typically posit explicit mechanisms for order placement, cancellation, and
reaction to price changes.
While such models reproduce many stylized facts, they treat liquidity,
imbalance, and price as primitive variables.

The present approach is complementary rather than competing.
By stripping away microstructural detail, it isolates the minimal geometric
constraints imposed by observation itself.
In this sense, our results suggest that certain regularities traditionally
attributed to agent behavior may instead reflect universal properties of
projected relational systems, independent of the specific microscopic rules.

### VI.5 Scope, limitations, and outlook

Finally, we emphasize the intended scope of this work.
The framework does not aim to predict price trajectories, infer trader intent,
or provide a mechanism for market clearing.
Its contribution is structural: it demonstrates that directional liquidity
imbalances and bid–ask asymmetries can be understood as emergent geometric
shear modes that are largely orthogonal to price dynamics.

This perspective opens several directions for future work.
Promising extensions include multi-scale generalizations capturing nested
geometric structures, dynamic evolution equations for shear parameters,
cross-asset correlation of shear modes, and extensions to other markets
(FX, bonds, and crypto) to test universality.
Coupling geometric shear modes to explicit dynamical rules may also provide a
controlled route to reintroducing predictive content without sacrificing the
geometric clarity of the present framework.

## VII Future directions

The pregeometric framework developed in this work opens several directions
for further theoretical and empirical investigation.
We briefly outline a number of natural extensions.

#### (i) Multi-scale shear geometry.

The present analysis focuses on a single observational scale, fixed by the
intraday window Δ​T\Delta T and the finite tick range KK.
An important extension is the development of a multi-scale formulation in
which projected liquidity geometry is resolved across nested temporal and
price scales.
Such a construction would allow the study of scale-dependent shear modes and
their potential renormalization properties, analogous to coarse-graining
procedures in statistical physics.

#### (ii) Dynamical evolution of shear amplitudes.

In this work, shear amplitudes ATA\_{T} and the associated gamma-geometry
parameters are treated as quasi-static observables defined over finite
windows.
A natural next step is to derive effective stochastic or deterministic
evolution equations for the shear field and its parameters, such as
γ​(t)\gamma(t) and λ​(t)\lambda(t).
This would provide a dynamical description of how geometric deformations of
liquidity emerge, persist, and relax under non-equilibrium trading activity.

#### (iii) Cross-asset coupling of shear modes.

The empirical results presented here treat assets independently.
However, market activity is inherently multi-asset and correlated.
Extending the framework to study cross-asset correlations of shear amplitudes
and shear fields may reveal collective geometric modes at the market level,
potentially linked to sectoral flows, index rebalancing, or systemic events.

#### (iv) Extension to other markets.

While the present study focuses on U.S. equities, the construction is not
equity-specific.
Applying the same observational-geometric methodology to other markets,
including foreign exchange, fixed income, and cryptocurrency markets, would
provide a stringent test of the proposed universality of shear geometry and
its independence from market microstructure details.

#### (v) Relation to market impact and price formation.

Finally, the geometric separation between shear and mid-price translation
suggests a new perspective on market impact.
Rather than interpreting order-book imbalance as a direct price force, the
framework indicates that deformation of liquidity geometry and translation of
the price coordinate are distinct modes.
Clarifying how trading activity couples these modes may help bridge geometric
descriptions of liquidity with established models of impact and price
formation.

Together, these directions suggest that pregeometric liquidity geometry
provides a flexible and extensible framework for studying non-equilibrium
market structure beyond the static order book.

###### Acknowledgements.

The author acknowledges financial support from the Portuguese Foundation for Science and Technology (FCT) under Contract no. UID/00618/2023.

## References

* (1)

  F. R. K. Chung,
  Spectral Graph Theory
  (American Mathematical Society, Providence, RI, 1997).
* (2)

  M. Belkin and P. Niyogi,
  Neural Comput. 15, 1373 (2003).
* (3)

  U. von Luxburg,
  Stat. Comput. 17, 395 (2007).
* (4)

  J.-P. Bouchaud, M. Mézard, and M. Potters,
  Quant. Finance 2, 251 (2002).
* (5)

  J. P. da Cruz,
  “Pregeometric Origins of Liquidity Geometry in Financial Order Books”,
  eprint 2601.17245, https://arxiv.org/abs/2601.17245, (2026).
* (6)

  J. D. Farmer and F. Lillo,
  “On the origin of power-law tails in price fluctuations,”
* (7)

  E. Smith, J. D. Farmer, L. Gillemot, and S. Krishnamurthy,
  “Statistical theory of the continuous double auction,”
  Phys. Rev. E 67, 045106 (2003).
* (8)

  J.-P. Bouchaud, J. D. Farmer, and F. Lillo,
  “How markets slowly digest changes in supply and demand,”
  in Handbook of Financial Markets: Dynamics and Evolution,
  edited by T. Hens and K. R. Schenk-Hoppé
  (Elsevier, Amsterdam, 2009), pp. 57–160.
* (9)

  J.-P. Bouchaud, Y. Gefen, M. Potters, and M. Wyart,
  Quant. Finance 4, 176 (2004).
* (10)

  R. Cont, S. Stoikov, and R. Talreja,
  Oper. Res. 58, 549 (2010).
* (11)

  I. I. Zovko and J. D. Farmer,
  Quant. Finance 2, 387 (2002).
* (12)

  E. Smith, J. D. Farmer, L. Gillemot, and S. Krishnamurthy,
  Phys. Rev. E 67, 045106 (2003).
* (13)

  S. Mike and J. D. Farmer,
  J. Econ. Dyn. Control 32, 200 (2008).
* (14)

  C. Rovelli,
  *Quantum Gravity*
  (Cambridge University Press, Cambridge, 2004).
* (15)

  D. Oriti,
  “Group field theory and emergent spacetime,”
  in *Foundations of Space and Time*,
  edited by G. Ellis, J. Murugan, and A. Weltman
  (Cambridge University Press, Cambridge, 2014), pp. 257–320.
* (16)

  J. Ambjørn, J. Jurkiewicz, and R. Loll,
  Phys. Rev. D 72, 064014 (2005).