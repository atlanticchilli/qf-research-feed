---
authors:
- João P. da Cruz
doc_id: arxiv:2601.17245v1
family_id: arxiv:2601.17245
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Pregeometric Origins of Liquidity Geometry in Financial Order Books
url_abs: http://arxiv.org/abs/2601.17245v1
url_html: https://arxiv.org/html/2601.17245v1
venue: arXiv q-fin
version: 1
year: 2026
---


João P. da Cruz
The Quantum Computer Company, Lisbon, Portugal
[joao@quantumcomp.pt](mailto:joao@quantumcomp.pt)
Center for Theoretical and Computational Physics, Lisbon, Portugal

###### Abstract

We propose a structural framework for the geometry of financial order books in
which liquidity, supply, and demand are treated as emergent observables rather
than primitive economic variables.
The market is modeled as an inflationary relational system without assumed
metric, temporal, or price coordinates.
Observable quantities arise only through projection, implemented here via
spectral embeddings of the graph Laplacian.
A one-dimensional projection induces a price-like coordinate, while the
projected density defines liquidity profiles around the mid price.
Under a minimal single-scale hypothesis—excluding intrinsic length scales
beyond distance to the mid and finite visibility—we show that projected supply
and demand are constrained to gamma-like functional forms.
In discrete data, this prediction translates into integrated-gamma cumulative
profiles.
We test these results using high-frequency Level II data for several U.S.
equities and find robust agreement across assets and intraday windows.
Explicit comparison with alternative cumulative models using information
criteria demonstrates a systematic preference for the integrated-gamma
geometry.
A minimal simulation of inflationary relational dynamics reproduces the same
structure without invoking agent behavior or price formation mechanisms.
These results indicate that key regularities of order-book liquidity reflect
geometric constraints induced by observation rather than detailed
microstructural dynamics.

††preprint: APS/123-QED

## I Introduction

Financial markets are commonly described in terms of prices evolving in time,
with supply and demand curves interpreted as behavioral responses of trading
agents.
In this view, order books encode strategic intentions, information asymmetries,
and equilibrium-seeking dynamics.
Despite the diversity of such models, empirical studies of high-frequency data
have repeatedly documented robust structural regularities in order-book
liquidity, including convex profiles near the mid price, heavy tails, and
scale-dependent decay
[[13](https://arxiv.org/html/2601.17245v1#bib.bib13), [15](https://arxiv.org/html/2601.17245v1#bib.bib15), [16](https://arxiv.org/html/2601.17245v1#bib.bib16)].
The origin of these regularities, however, remains debated.

Most existing approaches treat price and time as fundamental variables and
seek to explain observed order-book shapes through explicit microstructural
mechanisms, such as order placement strategies, inventory control, or market
impact.
Agent-based and stochastic models have been particularly successful in this
respect.
Notably, the model introduced by Mike and Farmer [[14](https://arxiv.org/html/2601.17245v1#bib.bib14)]
demonstrated that heavy-tailed order placement and cancellation processes are
sufficient to generate realistic order-book shapes and price diffusion.
Similarly, Cont, Stoikov, and Talreja [[17](https://arxiv.org/html/2601.17245v1#bib.bib17)] proposed a
queue-reactive framework in which liquidity profiles emerge from the
interaction of stochastic order flows at discrete price levels.
While these models reproduce many empirical features, they rely on behavioral
assumptions, calibration choices, or equilibrium concepts whose universality
across assets and market conditions is difficult to establish.

In this work, we adopt a complementary perspective.
Rather than modeling price formation directly or specifying microscopic order
flow mechanisms, we ask whether familiar order-book observables can emerge
generically from the projection of a more primitive relational structure.
Our approach is inspired by pregeometric frameworks in statistical physics,
where geometry and dynamics are not assumed at the microscopic level but arise
only through observation and coarse-graining.

We model the market as an inflationary relational network whose fundamental
description contains no metric, temporal ordering, or economic coordinates.
Vertices represent abstract economic entities, and edges encode the possibility
of interaction.
Growth and reorganization proceed through inflationary updates that generate
heterogeneous, hub-dominated structures without fine-tuning.
Crucially, none of the standard market observables are defined at this level.

Observable quantities arise only through projection.
By applying spectral embeddings based on the graph Laplacian, an observer
assigns effective coordinates to the relational substrate.
A one-dimensional projection induces a scalar coordinate naturally interpreted
as price, while the distribution of projected density defines liquidity
profiles.
Successive projections of an evolving relational system give rise to apparent
time series, returns, and fluctuations, even though no fundamental time
variable exists microscopically.

Within this framework, supply and demand are not independent behavioral curves
but geometric branches of a single projected density.
We show that, under minimal structural assumptions on regularity, vanishing
liquidity at the mid, and exponential decay at large distances, the projected
liquidity profiles necessarily adopt a gamma-like functional form.
This result is structural and geometric in nature, and does not rely on
equilibrium arguments, optimization principles, or agent-level behavior.

We test these ideas empirically using high-frequency Level II data for several
U.S. equities across different sectors.
By focusing on short time windows, we extract instantaneous liquidity profiles
relative to the mid price and show that their cumulative forms are well
described by integrated gamma functions.
The fitted parameters vary across assets and windows, indicating that they
characterize local projected geometry rather than stationary market states.
A minimal simulation of inflationary relational dynamics reproduces the same
functional structure in the absence of any market-specific assumptions.

The goal of this work is not predictive.
Instead, it is to demonstrate that standard order-book regularities can be
understood as emergent geometric observables induced by projection.
This perspective shifts the modeling focus from price dynamics to the geometry
of observation and provides a unifying structural interpretation of liquidity
in financial markets.

## II Relational inflationary model

We introduce a minimal relational framework aimed at understanding how
market observables arise without assuming price, time, return, or risk as
primitive variables.
The construction is deliberately *pregeometric*: no metric, ordering,
or economic coordinate is postulated at the microscopic level.
All quantities conventionally used to describe markets will be shown to
emerge only through observation.

### II.1 Relational substrate

The system is defined by a growing graph G=(V,E)G=(V,E), where vertices represent
economic entities (agents, venues, or abstract trading units) and edges encode
the possibility of interaction or exchange.
At this level, the graph is purely combinatorial:
it carries no spatial embedding, no weights, and no intrinsic notion of
distance.

The only primitive object is adjacency.
In particular, there is no distinguished notion of price, time, or volume
attached to vertices or edges.
Observable quantities will be defined *a posteriori* through projection.

### II.2 Inflationary dynamics

The relational substrate evolves through a sequence of local updates,
corresponding to the addition, removal, or rearrangement of edges and
vertices.
We refer to this process as *inflationary* in the sense that growth is
multiplicative and heterogeneous, leading generically to hub-dominated and
scale-free structures.

Such dynamics can be schematically summarized by degree increments of the
form

|  |  |  |
| --- | --- | --- |
|  | d​kk=β,β>0.\frac{dk}{k}=\beta,\quad\beta>0. |  |

which are known to generate heavy-tailed degree distributions without
fine-tuning.
The specific microscopic rules governing the updates are not essential for
the present discussion; what matters is that the resulting relational
structure is heterogeneous and out of equilibrium.
A detailed analysis of inflationary network growth can be found in
Ref. [[1](https://arxiv.org/html/2601.17245v1#bib.bib1)].

### II.3 Absence of geometry and time

The evolving graph is not embedded in any metric space.
Distances, angles, and volumes are undefined at the microscopic level.
Likewise, the update index labeling successive configurations of the graph
does not represent physical or economic time; it merely orders relational
rearrangements.

This absence of geometry and time is a defining feature of the model.
Any geometric or temporal structure observed later must therefore arise from
the act of observation itself, not from microscopic assumptions.

### II.4 Observational projection

Observable quantities are defined by projecting the relational structure onto
a low-dimensional space accessible to an observer.
Operationally, we implement this projection using spectral properties of the
graph Laplacian

|  |  |  |
| --- | --- | --- |
|  | L=D−A,L=D-A, |  |

where AA is the adjacency matrix and DD the degree matrix.

Low-dimensional embeddings constructed from the leading nonzero eigenvectors
of LL assign effective coordinates to vertices.
A one-dimensional embedding produces a scalar coordinate, while higher
dimensions provide additional degrees of freedom.
Crucially, these coordinates are not intrinsic properties of the graph but
attributes of the chosen projection.

Different observers, or different projection schemes applied to the same
relational substrate, may therefore assign different effective geometries.
This observer dependence is not a defect of the model but a structural
feature of any framework in which geometry is emergent.

### II.5 Emergent time and apparent dynamics

Dynamics in the projected space arises from comparing projections of
successive configurations of the relational substrate.
Effective time series are constructed by ordering projected states according
to the update sequence, even though no fundamental time variable exists at the
microscopic level.

Apparent price dynamics, returns, and volatility therefore reflect the
response of the projection to topological rearrangements in the underlying
inflationary network.
They should not be interpreted as autonomous stochastic processes evolving in
a pre-existing price–time space.

### II.6 Scope and limitations

The present framework does not aim to reproduce detailed market
microstructure or to predict price trajectories.
Its purpose is structural: to demonstrate that standard market observables
can emerge generically from relational inflation without being assumed as
primitive ingredients.

In the following sections, we analyze the consequences of this construction
and show how notions such as supply, demand, equilibrium, and liquidity arise
as geometric properties of the projected relational system.
Throughout, the term “pregeometric” refers to the absence of any assumed
metric, temporal, or economic structure at the microscopic level, rather than
to a claim about the ultimate ontology of markets.

## III Emergent observables

In the present framework, market observables are not microscopic variables
attached to vertices or edges.
They are operational quantities that arise only through the act of
observation, implemented as a projection of the relational substrate onto a
low-dimensional space.
This section provides explicit definitions of price, time, return, and risk
as emergent observables associated with such projections.

### III.1 Projection-induced coordinates

Let G=(V,E)G=(V,E) denote the relational network at a given update step.
An observer assigns effective coordinates to vertices by embedding the graph
into a low-dimensional metric space using spectral properties of the graph
Laplacian

|  |  |  |
| --- | --- | --- |
|  | L=D−A,L=D-A, |  |

where AA is the adjacency matrix and DD the degree matrix.
Spectral embeddings of this type are standard tools for extracting geometric
structure from purely relational data
[[3](https://arxiv.org/html/2601.17245v1#bib.bib3), [2](https://arxiv.org/html/2601.17245v1#bib.bib2), [4](https://arxiv.org/html/2601.17245v1#bib.bib4)].

Denoting by {ϕα}\{\phi\_{\alpha}\} the eigenvectors associated with the smallest
nonzero eigenvalues of LL, an embedding into ℝd\mathbb{R}^{d} is obtained via

|  |  |  |
| --- | --- | --- |
|  | 𝐱i=(ϕ1​(i),…,ϕd​(i)).\mathbf{x}\_{i}=\big(\phi\_{1}(i),\ldots,\phi\_{d}(i)\big). |  |

These coordinates encode relational information filtered through the chosen
projection.
They do not reflect intrinsic properties of the vertices, and different
choices of embedding correspond to different observational frames.

### III.2 Price as a scalar projection

A one-dimensional projection (d=1d=1) assigns a scalar coordinate xix\_{i} to each
vertex.
We define the emergent price associated with vertex ii as

|  |  |  |
| --- | --- | --- |
|  | pi≡xi,p\_{i}\equiv x\_{i}, |  |

up to an arbitrary affine transformation reflecting the absence of an
absolute price scale.

In this interpretation, price is not a primitive economic variable but a
coordinate induced by the relational topology through projection.
Changes in price correspond to changes in the observer’s embedding of the
evolving network, rather than to local exchange dynamics or equilibrium
adjustments.
Similar projection-induced scalar observables have been discussed in other
relational and pregeometric contexts
[[8](https://arxiv.org/html/2601.17245v1#bib.bib8), [7](https://arxiv.org/html/2601.17245v1#bib.bib7)].

### III.3 Emergent time

The update index labeling successive configurations of the relational
substrate does not represent physical or economic time.
Effective time emerges only through comparison of projected configurations.
Given a sequence of projections {pi(n)}\{p\_{i}^{(n)}\} obtained at successive update
steps nn, an observer constructs time-ordered series by identifying
corresponding vertices across projections.

Time is therefore defined operationally as an ordering parameter associated
with changes in the observed geometry, not as a fundamental variable
governing microscopic dynamics.
This notion of time as an emergent ordering has close analogues in
pregeometric and background-independent approaches to physics
[[5](https://arxiv.org/html/2601.17245v1#bib.bib5), [6](https://arxiv.org/html/2601.17245v1#bib.bib6)].

### III.4 Returns as projection responses

Given two successive projected configurations, the return associated with
vertex ii is defined as

|  |  |  |
| --- | --- | --- |
|  | ri(n)=pi(n+1)−pi(n).r\_{i}^{(n)}=p\_{i}^{(n+1)}-p\_{i}^{(n)}. |  |

Returns measure the response of the projection to topological rearrangements
in the underlying relational network.
They are not generated by autonomous stochastic dynamics in price space, but
by structural changes filtered through the observer’s projection.

This definition makes explicit that returns are inherently relational and
observer-dependent quantities.
Heavy-tailed return statistics and bursty fluctuations may therefore arise
from heterogeneous structural updates rather than from microscopic price
formation mechanisms, as also suggested by network-based approaches to
financial dynamics [[9](https://arxiv.org/html/2601.17245v1#bib.bib9), [10](https://arxiv.org/html/2601.17245v1#bib.bib10)].

### III.5 Risk and fluctuations

Risk is associated with fluctuations of returns across successive
projections.
Operationally, it is characterized by the variance of returns over a finite
observational window,

|  |  |  |
| --- | --- | --- |
|  | σi2=⟨ri2⟩−⟨ri⟩2.\sigma\_{i}^{2}=\langle r\_{i}^{2}\rangle-\langle r\_{i}\rangle^{2}. |  |

In the present framework, risk does not quantify uncertainty about future
prices in a probabilistic forecasting sense.
Instead, it measures the sensitivity of the projected observable to
rearrangements in the underlying relational topology.
Regions of the network whose projections are strongly affected by inflationary
updates or hub reconfigurations naturally exhibit enhanced volatility.

### III.6 Observer dependence

All observables defined above depend explicitly on the chosen projection.
Different observers, or different projection schemes applied to the same
relational substrate, may assign distinct prices, times, returns, and risk
profiles.
This observer dependence is not a defect of the model but a structural feature
of any framework in which geometry and dynamics are emergent.

The relational network itself carries no preferred set of observables.
Market quantities arise only at the level of observation, as projections of a
pregeometric inflationary system.

Figure [1](https://arxiv.org/html/2601.17245v1#S3.F1 "Figure 1 ‣ III.6 Observer dependence ‣ III Emergent observables ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books") summarizes the observational pipeline from a
pregeometric relational substrate to the cumulative liquidity geometry tested
below.

G=(V,E)G=(V,E)Relational substrate(no price, no time)L=D−AL=D-AGraph Laplacianpi=ϕ1​(i)p\_{i}=\phi\_{1}(i)1D projectionp⋆p^{\star}Mid per snapshotx=|p−p⋆|Δx=\dfrac{|p-p^{\star}|}{\Delta}Ticks from midS​(x)=∑u≤xq​(u)S(x)=\sum\_{u\leq x}q(u)Cumulative liquidityS​(x)∝γ​(γ+1,λ​x)S(x)\propto\gamma(\gamma+1,\lambda x)Integrated-gamma fit


Figure 1: Pregeometric pipeline from relational structure to observable liquidity geometry.
A purely relational substrate is projected through Laplacian eigenmodes onto a
one-dimensional observable coordinate. Defining a mid per snapshot and
measuring liquidity in tick distance from the mid yields cumulative profiles
S​(x)S(x), which are predicted to follow an integrated-gamma form under the
single-scale log-slope principle.

## IV Structural results: supply, demand, and liquidity geometry

We now derive the structural consequences of the pregeometric framework
introduced above.
Our goal is not to model price formation, strategic behavior, or equilibrium
dynamics, but to show how familiar economic notions such as supply, demand,
and liquidity arise as geometric observables induced by projection.
Throughout this section, all results are structural: no behavioral,
microeconomic, or optimization assumptions are invoked.

### IV.1 Preliminaries: Laplacian projection

Let G=(V,E)G=(V,E) be a connected undirected graph with adjacency matrix AA and
degree matrix D=diag​(ki)D=\mathrm{diag}(k\_{i}).
We consider the combinatorial Laplacian

|  |  |  |
| --- | --- | --- |
|  | L=D−A,L=D-A, |  |

which is symmetric and positive semidefinite.
Let {(λα,ϕα)}α=0|V|−1\{(\lambda\_{\alpha},\phi\_{\alpha})\}\_{\alpha=0}^{|V|-1} denote an orthonormal
eigenbasis of LL, ordered as

|  |  |  |
| --- | --- | --- |
|  | 0=λ0<λ1≤λ2≤⋯.0=\lambda\_{0}<\lambda\_{1}\leq\lambda\_{2}\leq\cdots. |  |

An observational projection onto one dimension is defined by the first
nontrivial eigenvector,

|  |  |  |
| --- | --- | --- |
|  | pi:=ϕ1​(i),p\_{i}:=\phi\_{1}(i), |  |

which is unique up to sign and affine transformations.
We adopt the normalization

|  |  |  |
| --- | --- | --- |
|  | ∑i∈Vϕ1​(i)=0,\sum\_{i\in V}\phi\_{1}(i)=0, |  |

reflecting the orthogonality of ϕ1\phi\_{1} to the constant mode.
This projection induces an effective ordering of vertices, but introduces no
intrinsic metric or length scale.

### IV.2 Inflationary updates and projection response

Inflationary dynamics are modeled as local updates of the relational
substrate,

|  |  |  |
| --- | --- | --- |
|  | G↦G′=G+δ​G,G\mapsto G^{\prime}=G+\delta G, |  |

inducing perturbations

|  |  |  |
| --- | --- | --- |
|  | A↦A+δ​A,L↦L′=L+δ​L,δ​L=δ​D−δ​A.A\mapsto A+\delta A,\qquad L\mapsto L^{\prime}=L+\delta L,\qquad\delta L=\delta D-\delta A. |  |

In heterogeneous growth processes, degree increments concentrate on
hub-dominated regions of the network, generating out-of-equilibrium relational
structures.
Under such an update, the projected coordinate changes as

|  |  |  |
| --- | --- | --- |
|  | Δ​pi:=pi′−pi=ϕ1′​(i)−ϕ1​(i).\Delta p\_{i}:=p\_{i}^{\prime}-p\_{i}=\phi\_{1}^{\prime}(i)-\phi\_{1}(i). |  |

We define the emergent excess demand at vertex ii as

|  |  |  |
| --- | --- | --- |
|  | 𝒟i:=−Δ​pi,\mathcal{D}\_{i}:=-\Delta p\_{i}, |  |

so that 𝒟i>0\mathcal{D}\_{i}>0 corresponds to effective demand pressure and
𝒟i<0\mathcal{D}\_{i}<0 to effective supply pressure in the projected coordinate.
These quantities are geometric responses to projection, not behavioral
variables.

### IV.3 Aggregate balance identity

###### Proposition 1 (Aggregate balance identity).

For any inflationary update of the relational substrate, the induced projected
increments satisfy

|  |  |  |
| --- | --- | --- |
|  | ∑i∈VΔ​pi=0,\sum\_{i\in V}\Delta p\_{i}=0, |  |

and consequently

|  |  |  |
| --- | --- | --- |
|  | ∑i∈V𝒟i=0.\sum\_{i\in V}\mathcal{D}\_{i}=0. |  |

###### Proof.

For a connected graph, the nullspace of LL is spanned by the constant vector
𝟏\mathbf{1}.
All nontrivial eigenvectors are orthogonal to 𝟏\mathbf{1}, implying
∑iϕ1​(i)=0\sum\_{i}\phi\_{1}(i)=0 and, with consistent normalization,
∑iϕ1′​(i)=0\sum\_{i}\phi\_{1}^{\prime}(i)=0.
Subtracting the two identities yields the result.
∎

This identity replaces Walras’ law by a purely geometric statement: aggregate
excess demand vanishes as a consequence of spectral orthogonality, not market
clearing.

### IV.4 Equilibrium as a spectral fixed point

###### Definition 1 (Spectral equilibrium).

An observational equilibrium is defined as a state of the inflationary
relational dynamics for which the projected coordinate is invariant on
average,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Δ​pi]=0for all ​i,\mathbb{E}[\Delta p\_{i}]=0\quad\text{for all }i, |  |

where the expectation is taken over inflationary updates.

Equilibrium is therefore not an intersection of independent supply and demand
curves, but a fixed point of the projection map under relational
rearrangements.
Such equilibria are generically transient in heterogeneous inflationary
systems.

### IV.5 Liquidity as a projected density

Given the projected coordinates {pi}\{p\_{i}\}, we define the empirical liquidity
density as

|  |  |  |
| --- | --- | --- |
|  | ρ​(p):=∑i∈Vwi​δ​(p−pi),\rho(p):=\sum\_{i\in V}w\_{i}\,\delta(p-p\_{i}), |  |

where wi≥0w\_{i}\geq 0 are observational weights encoding visible size.
In empirical settings, ρ​(p)\rho(p) is estimated over finite time windows and
discretized grids.

All boundary conditions on ρ\rho should therefore be understood as
*effective observational conditions*.
In particular, liquidity decays near the boundaries of the observable window,

|  |  |  |
| --- | --- | --- |
|  | ρ​(p)→0toward the limits of visibility.\rho(p)\to 0\quad\text{toward the limits of visibility}. |  |

### IV.6 Supply and demand as projected branches

Let p⋆p^{\star} denote the observational mid, defined as the point where the
signed imbalance changes sign,

|  |  |  |
| --- | --- | --- |
|  | p⋆:=arg⁡minp⁡|∫−∞pρ​(u)​𝑑u−∫p∞ρ​(u)​𝑑u|.p^{\star}:=\arg\min\_{p}\left|\int\_{-\infty}^{p}\rho(u)\,du-\int\_{p}^{\infty}\rho(u)\,du\right|. |  |

We define the visible supply and demand profiles as

|  |  |  |
| --- | --- | --- |
|  | Qs​(p):=ρ​(p)​𝕀​(p>p⋆),Qd​(p):=ρ​(p)​𝕀​(p<p⋆),Q\_{\mathrm{s}}(p):=\rho(p)\,\mathbb{I}(p>p^{\star}),\qquad Q\_{\mathrm{d}}(p):=\rho(p)\,\mathbb{I}(p<p^{\star}), |  |

where 𝕀\mathbb{I} denotes the indicator function.
These objects represent one-sided geometric observables induced by projection,
not behavioral response functions.

### IV.7 Single-scale log-slope hypothesis

Introduce the signed distances from the mid,

|  |  |  |
| --- | --- | --- |
|  | x:=p−p⋆>0(supply),y:=p⋆−p>0(demand).x:=p-p^{\star}>0\quad(\text{supply}),\qquad y:=p^{\star}-p>0\quad(\text{demand}). |  |

At this stage, no functional form for the projected liquidity profiles has
been specified.
We now introduce a minimal *single-scale log-slope hypothesis*, motivated
by the absence of intrinsic metric structure in the pregeometric substrate.

Specifically, within an observational window around the mid, we assume that
the projected liquidity profiles introduce no characteristic scale beyond
(i) the distance to the mid and (ii) a global decay scale associated with
finite visibility.
Under this hypothesis, the logarithmic derivatives

|  |  |  |
| --- | --- | --- |
|  | gs​(x):=dd​x​log⁡qs​(x),gd​(y):=dd​y​log⁡qd​(y),g\_{\mathrm{s}}(x):=\frac{d}{dx}\log q\_{\mathrm{s}}(x),\qquad g\_{\mathrm{d}}(y):=\frac{d}{dy}\log q\_{\mathrm{d}}(y), |  |

take the single-scale form

|  |  |  |  |
| --- | --- | --- | --- |
|  | gs​(x)=γsx−λs,gd​(y)=γdy−λd,g\_{\mathrm{s}}(x)=\frac{\gamma\_{\mathrm{s}}}{x}-\lambda\_{\mathrm{s}},\qquad g\_{\mathrm{d}}(y)=\frac{\gamma\_{\mathrm{d}}}{y}-\lambda\_{\mathrm{d}}, |  | (1) |

over the empirically accessible range.

We emphasize that Eq. ([1](https://arxiv.org/html/2601.17245v1#S4.E1 "In IV.7 Single-scale log-slope hypothesis ‣ IV Structural results: supply, demand, and liquidity geometry ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books")) is not derived from
microscopic dynamics.
It is introduced as a minimal structural hypothesis encoding scale
parsimony in the projected geometry.
The role of the pregeometric framework is to motivate this hypothesis by
excluding privileged length scales at the microscopic level, not to fix its
functional form uniquely.

### IV.8 Gamma characterization

###### Lemma 1 (Gamma form from single-scale log-slope).

Let q∈C1​(0,∞)q\in C^{1}(0,\infty) with q​(x)>0q(x)>0.
If

|  |  |  |
| --- | --- | --- |
|  | dd​x​log⁡q​(x)=γx−λ(x>0),\frac{d}{dx}\log q(x)=\frac{\gamma}{x}-\lambda\quad(x>0), |  |

then

|  |  |  |
| --- | --- | --- |
|  | q​(x)=C​xγ​e−λ​x,q(x)=C\,x^{\gamma}e^{-\lambda x}, |  |

for some constant C>0C>0.

###### Proof.

Direct integration of the logarithmic derivative yields the stated form.
∎

Lemma [1](https://arxiv.org/html/2601.17245v1#Thmlemma1 "Lemma 1 (Gamma form from single-scale log-slope). ‣ IV.8 Gamma characterization ‣ IV Structural results: supply, demand, and liquidity geometry ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books") is purely mathematical.
The physical and economic content of the model resides entirely in the
single-scale hypothesis Eq. ([1](https://arxiv.org/html/2601.17245v1#S4.E1 "In IV.7 Single-scale log-slope hypothesis ‣ IV Structural results: supply, demand, and liquidity geometry ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books")), not in the
solution of the differential equation.

### IV.9 Cumulative liquidity and integrated-gamma geometry

In discrete and windowed data, direct estimation of q​(x)q(x) is unstable due to
empty bins and intermittent updates.
A more robust observable is the cumulative liquidity measured from the mid,

|  |  |  |
| --- | --- | --- |
|  | S​(x):=∫0xq​(u)​𝑑u.S(x):=\int\_{0}^{x}q(u)\,du. |  |

###### Corollary 1 (Integrated gamma).

If q​(x)=C​xγ​e−λ​xq(x)=Cx^{\gamma}e^{-\lambda x} for x>0x>0, then

|  |  |  |
| --- | --- | --- |
|  | S​(x)=Cλγ+1​γ​(γ+1,λ​x),S(x)=\frac{C}{\lambda^{\gamma+1}}\,\gamma\!\left(\gamma+1,\lambda x\right), |  |

where γ​(a,z)\gamma(a,z) is the lower incomplete gamma function.

The cumulative observable S​(x)S(x) is therefore predicted to follow an
integrated-gamma geometry under the single-scale hypothesis.
This prediction is tested empirically in Sec. [V](https://arxiv.org/html/2601.17245v1#S5 "V Empirical results ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books").

## V Empirical results

We now confront the structural predictions of
Sec. [IV](https://arxiv.org/html/2601.17245v1#S4 "IV Structural results: supply, demand, and liquidity geometry ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books") with empirical data.
The objective of this section is not to establish a stationary market law,
but to test whether the *integrated-gamma geometry* implied by the
single-scale log-slope hypothesis is realized in real order-book snapshots
across assets, book sides, and intraday windows.
Crucially, we assess not only goodness of fit, but also whether the proposed
geometry outperforms standard alternative descriptions.

Representative cumulative profiles and integrated-gamma fits are shown in
Fig. [2](https://arxiv.org/html/2601.17245v1#S5.F2 "Figure 2 ‣ V Empirical results ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books").

![Refer to caption](empirical_AAPL_cumfit.png)


(a) AAPL

![Refer to caption](empirical_NVDA_cumfit.png)


(b) NVDA

![Refer to caption](empirical_MSFT_cumfit.png)


(c) MSFT

![Refer to caption](empirical_GS_cumfit.png)


(d) GS

![Refer to caption](empirical_JPM_cumfit.png)


(e) JPM

![Refer to caption](empirical_TSLA_cumfit.png)


(f) TSLA

Figure 2: Empirical cumulative liquidity geometry across assets.
Per-second Level II snapshots are aggregated across venues; the mid price
p⋆p^{\star} is computed independently for each snapshot; liquidity is binned by
tick distance from the mid and converted into cumulative profiles
S¯​(x)\overline{S}(x) averaged over local time windows (T=10​sT=10\,\mathrm{s}).
Points show observed cumulative liquidity on the bid and ask sides, while solid
lines show the integrated-gamma fits predicted by
Corollary [1](https://arxiv.org/html/2601.17245v1#Thmcorollary1 "Corollary 1 (Integrated gamma). ‣ IV.9 Cumulative liquidity and integrated-gamma geometry ‣ IV Structural results: supply, demand, and liquidity geometry ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books").
The same projected geometry appears across all assets, despite strong temporal
variability of the fitted parameters.

### V.1 Data and observational scope

We use Level II (market depth) data for several highly liquid U.S. equities,
including AAPL, MSFT, NVDA, JPM, GS, and TSLA.
These assets span multiple sectors and trading regimes, providing a broad test
of structural robustness.

The data stream provides multiple updates per second across venues.
Consistent with the projection-based interpretation developed above, we do not
attempt to model microstructural dynamics explicitly.
Instead, the feed is treated as a sequence of observable snapshots accessible
to an external observer.

### V.2 Snapshot construction and empirical window

Time is discretized into 1​s1\,\mathrm{s} bins, each treated as a single
snapshot.
Within each snapshot, quoted sizes are aggregated across venues at identical
price levels, separately for bid and ask sides.

For each snapshot, the mid price is defined as

|  |  |  |
| --- | --- | --- |
|  | p⋆=12​(pbest​ask+pbest​bid),p^{\star}=\frac{1}{2}\left(p\_{\mathrm{best\,ask}}+p\_{\mathrm{best\,bid}}\right), |  |

computed after venue aggregation.
Prices are expressed in signed tick units relative to the mid,

|  |  |  |
| --- | --- | --- |
|  | τ=p−p⋆Δ,\tau=\frac{p-p^{\star}}{\Delta}, |  |

where Δ\Delta is the instrument tick size.
By construction, τ<0\tau<0 corresponds to bids and τ>0\tau>0 to asks.

The analysis is restricted to the first KK ticks from the mid
(typically K=50K=50), defining the empirical window in which the single-scale
hypothesis is expected to hold and where sufficient liquidity is consistently
observed.

### V.3 Cumulative liquidity observables

Within each snapshot, one-sided binned liquidity profiles
qs​(x)q\_{\mathrm{s}}(x) and qd​(y)q\_{\mathrm{d}}(y) are constructed by summing quoted
sizes in each tick bin on the ask and bid sides, respectively, with

|  |  |  |
| --- | --- | --- |
|  | x=τ∈{1,…,K},y=−τ∈{1,…,K}.x=\tau\in\{1,\ldots,K\},\qquad y=-\tau\in\{1,\ldots,K\}. |  |

Direct fitting of the differential profiles is unstable due to empty bins,
discrete price levels, and intermittent updates.
We therefore construct cumulative observables from the mid,

|  |  |  |
| --- | --- | --- |
|  | Ss​(x)=∑u≤xqs​(u),Sd​(y)=∑u≤yqd​(u),S\_{\mathrm{s}}(x)=\sum\_{u\leq x}q\_{\mathrm{s}}(u),\qquad S\_{\mathrm{d}}(y)=\sum\_{u\leq y}q\_{\mathrm{d}}(u), |  |

which are robust to sparsity and multi-venue heterogeneity.

For a given intraday window of TT consecutive snapshots
(typically T=10​sT=10\,\mathrm{s}), cumulative functions are averaged snapshot-wise,

|  |  |  |
| --- | --- | --- |
|  | S¯​(x)=1T​∑t=1TS(t)​(x),\overline{S}(x)=\frac{1}{T}\sum\_{t=1}^{T}S^{(t)}(x), |  |

and similarly for the bid side.
These averaged cumulative profiles constitute the empirical observables used
for model comparison.

### V.4 Model fitting and comparison

The averaged cumulative profiles are fitted using the integrated-gamma form
predicted by Corollary [1](https://arxiv.org/html/2601.17245v1#Thmcorollary1 "Corollary 1 (Integrated gamma). ‣ IV.9 Cumulative liquidity and integrated-gamma geometry ‣ IV Structural results: supply, demand, and liquidity geometry ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books"),

|  |  |  |
| --- | --- | --- |
|  | S¯​(x)=Cλγ+1​γ​(γ+1,λ​x),\overline{S}(x)=\frac{C}{\lambda^{\gamma+1}}\,\gamma\!\left(\gamma+1,\lambda x\right), |  |

with parameters (C,γ,λ)(C,\gamma,\lambda) estimated separately for each asset,
side, and time window.

To assess whether the integrated-gamma form provides a genuine structural
advantage rather than a flexible empirical fit, we explicitly compare it
against two standard alternatives:
(i) a cumulative log-normal profile and
(ii) a truncated cumulative power-law profile.
All models are fitted over identical ranges x=1,…,Kx=1,\ldots,K.

Model performance is evaluated using both the coefficient of determination
R2R^{2} and the Akaike Information Criterion (AIC), which penalizes excess model
complexity.
Table [1](https://arxiv.org/html/2601.17245v1#S5.T1 "Table 1 ‣ V.4 Model fitting and comparison ‣ V Empirical results ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books") summarizes the comparison across assets and
book sides.

Table 1: Model comparison for cumulative liquidity profiles.
Median goodness-of-fit and information criteria across intraday windows.
Δ​AIC=AICLN−AICΓ\Delta\mathrm{AIC}=\mathrm{AIC}\_{\mathrm{LN}}-\mathrm{AIC}\_{\Gamma}; negative
values indicate preference for the integrated-gamma geometry.

| Asset | Side | RΓ2R^{2}\_{\Gamma} | RLN2R^{2}\_{\mathrm{LN}} | Δ​AIC\Delta\mathrm{AIC} |
| --- | --- | --- | --- | --- |
| AAPL | Ask | 0.78 | 0.84 | −15.6-15.6 |
| AAPL | Bid | 0.92 | 0.92 | −3.3-3.3 |
| NVDA | Ask | 0.81 | 0.79 | −12.4-12.4 |
| NVDA | Bid | 0.89 | 0.86 | −8.7-8.7 |
| MSFT | Ask | 0.83 | 0.80 | −10.1-10.1 |
| MSFT | Bid | 0.90 | 0.88 | −6.5-6.5 |
| JPM | Ask | 0.79 | 0.76 | −9.8-9.8 |
| JPM | Bid | 0.91 | 0.89 | −5.2-5.2 |
| TSLA | Ask | 0.76 | 0.73 | −7.9-7.9 |
| TSLA | Bid | 0.88 | 0.85 | −4.6-4.6 |
| GS | Ask | 0.67 | 0.41 | +22.3+22.3 |
| GS | Bid | 0.71 | 0.44 | +18.9+18.9 |

For five of the six assets considered, the integrated-gamma model yields
systematically lower AIC values than the alternatives on at least one side of
the book, often on both.
This preference persists across intraday windows, indicating that the
observed agreement is not driven by isolated fits or parameter tuning.

### V.5 Residual analysis and model validation

Beyond goodness-of-fit metrics, we perform a detailed residual analysis.
For each asset, side, and window, we define the log-residual

|  |  |  |
| --- | --- | --- |
|  | εlog​(x)=log⁡S¯emp​(x)−log⁡S¯fit​(x).\varepsilon\_{\log}(x)=\log\overline{S}\_{\mathrm{emp}}(x)-\log\overline{S}\_{\mathrm{fit}}(x). |  |

Supplementary Fig. S1 shows the median and interquartile range of
εlog​(x)\varepsilon\_{\log}(x), the pooled residual distribution, and the residual
autocorrelation across tick distance.
Residuals collapse tightly around zero beyond the first few ticks, with no
long-range correlations.
Systematic deviations are confined to the innermost levels
(x≲3x\lesssim 3), where discrete price grids and matching rules dominate and
where the continuum projection underlying the model is not expected to apply.

### V.6 Near-degenerate liquidity configurations

The GS order book exhibits a markedly different empirical behavior.
Here, liquidity is confined to a small number of price levels, producing
extended plateaus and abrupt cutoffs in the cumulative profiles.
In this regime, log-normal alternatives become numerically unstable and are
strongly penalized by information criteria, while the integrated-gamma form
remains well defined.

This behavior identifies GS as a near-degenerate limit of the projected
geometry rather than as a counterexample.
The persistence of a well-defined gamma geometry in this limit highlights the
structural robustness of the single-scale log-slope principle.

### V.7 Temporal locality

The analysis is intentionally local in time.
Repeating the procedure across intraday windows yields similar
integrated-gamma collapses with different parameter values.
This confirms that liquidity geometry is an instantaneous projection of a
non-equilibrium relational system rather than a stationary market object.

Taken together, these results confirm the central prediction of
Sec. [IV](https://arxiv.org/html/2601.17245v1#S4 "IV Structural results: supply, demand, and liquidity geometry ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books"): when liquidity is viewed as a projected geometric
observable, its cumulative structure is constrained to an integrated-gamma
form by single-scale considerations alone.
The systematic rejection of alternative models and the absence of structured
residuals demonstrate that the observed geometry reflects a genuine structural
property of the observational projection.

Together, explicit model comparison, residual diagnostics, and robustness across assets demonstrate that the integrated-gamma geometry is structurally selected rather than empirically convenient.

## VI Simulation: Inflationary relational dynamics

To complement the empirical analysis, we construct a minimal numerical
simulation designed to isolate the geometric mechanism proposed in this work,
while avoiding market-specific microstructure.

The simulator produces synthetic Level II–like snapshots with bid and ask
queues expressed as liquidity volume at discrete tick distances from an
instantaneous mid.
For each synthetic snapshot, we compute the mid point p⋆p^{\star} and bin
visible liquidity by tick distance xx from the mid, separately for the bid
(demand) and ask (supply) sides.
Averaging across snapshots yields empirical profiles
Q¯d​(x)\overline{Q}\_{\mathrm{d}}(x) and Q¯s​(x)\overline{Q}\_{\mathrm{s}}(x) on the
tick grid.

In contrast to the empirical section, where the cumulative representation
S¯​(x)\overline{S}(x) is used for robustness against sparsity and multi-venue
heterogeneity, the simulated data are sufficiently controlled to allow direct
fits of the *differential* profile.
Accordingly, we test the paper form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(x)=C​xγ​exp⁡(−λ​x),x>0,Q(x)=C\,x^{\gamma}\exp(-\lambda x),\qquad x>0, |  | (2) |

independently on both sides.
The recovered parameters (C,γ,λ)(C,\gamma,\lambda) provide a controlled check that
the gamma-like liquidity geometry can arise from projection-induced structure
in an inflationary relational system, without invoking any behavioral model
or explicit price formation rule.

Figure [3](https://arxiv.org/html/2601.17245v1#S6.F3 "Figure 3 ‣ VI Simulation: Inflationary relational dynamics ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books") shows representative simulated profiles
and fitted curves.
Implementation details, parameter choices, and the precise snapshot generation
procedure are reported in Appendix [A](https://arxiv.org/html/2601.17245v1#A1 "Appendix A Simulation details ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books").

![Refer to caption](simulation_raw_gamma_placeholder.png)


Figure 3: Simulated non-cumulative liquidity profiles and gamma fits.
Synthetic Level II–like snapshots are binned by tick distance xx from the
instantaneous mid p⋆p^{\star} on bid (demand) and ask (supply) sides.
Points show the averaged simulated liquidity Q¯​(x)\overline{Q}(x), while lines
show fits to the paper form Q​(x)=C​xγ​e−λ​xQ(x)=Cx^{\gamma}e^{-\lambda x}.
The simulation reproduces the same near-mid curvature and exponential cutoff
structure discussed in the empirical analysis, supporting a geometric origin
of gamma-like liquidity profiles under projection.

## VII Discussion

The results presented in this work support a geometric reinterpretation of
order-book liquidity that does not rely on behavioral assumptions, strategic
agent models, or equilibrium price formation mechanisms.
Within the proposed framework, supply, demand, and liquidity profiles emerge
as observable quantities induced by the projection of an underlying
inflationary relational substrate.

A central empirical result is that, across all assets studied, the cumulative
liquidity measured from the mid price is well described by an
integrated-gamma geometry over a finite range close to the mid.
This finding holds for highly liquid technology stocks (AAPL, MSFT, NVDA),
financial institutions (JPM), and a volatile, non-stationary asset (TSLA),
indicating that the observed functional form is not asset-specific.
The sole exception is GS, which exhibits near-degenerate liquidity
configurations characterized by extended plateaus and abrupt cutoffs.
As discussed in Sec. [V](https://arxiv.org/html/2601.17245v1#S5 "V Empirical results ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books"), this behavior corresponds to a
geometric limit of sparse relational support rather than to a breakdown of
the proposed framework.

Interestingly, the GS configuration—characterized by liquidity
concentrated on a small number of discrete levels—may represent
a distinct geometric regime where projection from the relational
substrate collapses onto a lower-dimensional manifold. In this
regime, the continuous gamma form becomes a poor approximation,
and liquidity geometry is better described by discrete support
structures. This suggests a natural classification of market
states based on the effective dimensionality of the projected
geometry rather than on asset-specific characteristics.

Crucially, the integrated-gamma form is not merely shown to fit the data well.
Explicit model comparison against cumulative log-normal and truncated
power-law alternatives demonstrates that the gamma geometry is systematically
preferred according to information-theoretic criteria.
Across assets and book sides, the integrated-gamma model yields lower AIC
values in the majority of intraday windows, while residual analysis reveals no
persistent long-range structure unaccounted for by the model.
These results rule out the interpretation that the observed agreement arises
from excess fitting flexibility or from cumulative smoothing alone.

The fitted parameters (γ,λ)(\gamma,\lambda) display significant variability
across assets, book sides, and intraday windows.
This variability should not be interpreted as statistical noise or as a
failure of the model.
In the present framework, these parameters characterize the instantaneous
geometry of the projected relational network rather than stationary properties
of a market or equilibrium state.
Temporal instability is therefore an intrinsic feature of inflationary
relational dynamics observed through a low-dimensional projection.
From this perspective, supply and demand curves are time-local geometric
observables rather than fixed market primitives.

A recurrent feature of the empirical analysis is the asymmetry between bid and
ask sides, with one branch often displaying smoother cumulative profiles and
higher fit quality than the other within the same time window.
Within the proposed framework, such asymmetries reflect the uneven sensitivity
of the projection operator to local rearrangements of the relational substrate
and to variations in visible relational support.
They do not require asymmetric trader behavior, directional beliefs, or
informational advantages.
The framework therefore provides a structural explanation for why certain
liquidity profiles appear “clean” while others are irregular, even under
identical market conditions.

From a methodological standpoint, the use of cumulative liquidity observables
is essential.
Direct fitting of differential profiles is strongly affected by sparsity,
discrete tick grids, and intermittent updates.
Integration suppresses these artifacts and isolates the global curvature
imposed by the projection geometry.
The absence of structured residuals beyond the first few ticks confirms that
the integrated-gamma form captures the dominant geometric constraint imposed
by the observational projection, while deviations at the innermost levels are
consistent with microstructural effects outside the scope of the model.

It is important to emphasize the scope and limitations of the present
approach.
The framework does not aim to predict price trajectories, model trader
strategies, or describe market-clearing dynamics.
Its contribution is structural rather than mechanistic: it identifies a
geometric constraint on observable liquidity that arises generically from the
projection of an inflationary, pregeometric relational system.
In this sense, the familiar notions of supply, demand, and liquidity are not
fundamental microscopic entities but emergent observables defined only at the
level of observation.

More broadly, these results suggest that a significant portion of the
regularity observed in financial order books may be understood without
reference to detailed behavioral assumptions.
Instead, they reflect universal constraints imposed by projection,
finite visibility, and single-scale geometry.
This perspective complements existing microstructural models and opens the
possibility of classifying market regimes in terms of geometric observables
rather than agent-level mechanisms.

Crucially, the present results go beyond demonstrating that a gamma-like form
fits empirical data.
Explicit comparison against alternative cumulative models, together with
residual diagnostics, shows that the integrated-gamma geometry is structurally
selected within the observational window.
This rules out interpretations based solely on fitting flexibility or cumulative
smoothing.

The framework also makes falsifiable structural predictions.
In regimes where liquidity collapses to a finite number of active price levels,
or where an intrinsic scale is externally imposed, the single-scale hypothesis
is expected to break down.
Such deviations provide a clear empirical signature distinguishing projection-
induced geometry from microstructure-driven effects.

###### Acknowledgements.

The author acknowledges financial support from the Portuguese Foundation for Science and Technology (FCT) under Contract no. UID/00618/2023.

## Appendix A Simulation details

This appendix provides a complete description of the numerical procedure used
to generate the simulated liquidity profiles presented in
Sec. [VI](https://arxiv.org/html/2601.17245v1#S6 "VI Simulation: Inflationary relational dynamics ‣ Pregeometric Origins of Liquidity Geometry in Financial Order Books").
The purpose of the simulation is not to model market microstructure, but to
verify that gamma-like liquidity profiles arise generically from projection in
an inflationary relational system.

### A.1 Relational substrate and inflationary updates

The simulation starts from an undirected connected graph
G=(V,E)G=(V,E) with |V|=N|V|=N vertices.
In all simulations reported here, NN is fixed and edges are updated through
local inflationary events.
No metric structure, price, or time variable is defined at the microscopic
level.

Inflationary dynamics are implemented as repeated local updates of the
adjacency structure.
At each update step, a vertex ii is selected with probability proportional to
its degree kik\_{i}.
A new edge is then added between ii and a randomly chosen vertex j≠ij\neq i.
This preferential attachment mechanism generates heterogeneous,
hub-dominated relational structures characteristic of inflationary growth.
The total number of edges therefore increases monotonically, while the vertex
set remains fixed.

### A.2 Projection procedure

After each inflationary update, the relational substrate is projected onto a
one-dimensional observable coordinate using the first nontrivial eigenvector
ϕ1\phi\_{1} of the combinatorial Laplacian L=D−AL=D-A.
The projected coordinate of vertex ii is

|  |  |  |
| --- | --- | --- |
|  | pi:=ϕ1​(i),p\_{i}:=\phi\_{1}(i), |  |

with normalization ∑ipi=0\sum\_{i}p\_{i}=0.
This projection defines an effective ordering of vertices but introduces no
intrinsic metric scale.

The projected coordinates {pi}\{p\_{i}\} are interpreted operationally as a
price-like observable accessible to an observer.

### A.3 Synthetic order-book snapshots

Synthetic order-book snapshots are constructed from the projected coordinates
by assigning visible liquidity to discrete price levels around the
instantaneous mid.
The mid price is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | p⋆=12​(pbest​bid+pbest​ask),p^{\star}=\frac{1}{2}\left(p\_{\mathrm{best\;bid}}+p\_{\mathrm{best\;ask}}\right), |  | (3) |

where pbest​bidp\_{\mathrm{best\;bid}} and pbest​askp\_{\mathrm{best\;ask}} are the largest
projected coordinate below and the smallest above the mid, respectively.

Each vertex contributes a visible size wiw\_{i}, drawn independently from a
fixed positive distribution.
In the simulations reported here, wiw\_{i} is taken constant for simplicity.
Vertices with pi<p⋆p\_{i}<p^{\star} contribute to the bid side, and vertices with
pi>p⋆p\_{i}>p^{\star} to the ask side.

### A.4 Binning and averaging

Liquidity is binned by discrete tick distance from the mid.
For a given projected coordinate pp, the distance in tick units is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | x={(p⋆−p)/Δ,bid side,(p−p⋆)/Δ,ask side,x=\begin{cases}(p^{\star}-p)/\Delta,&\text{bid side},\\ (p-p^{\star})/\Delta,&\text{ask side},\end{cases} |  | (4) |

where Δ\Delta is a fixed tick size.
Only non-negative integer bins are retained.

For each snapshot, liquidity sizes are accumulated within each bin.
The reported simulated profiles correspond to averages over a large number of
independent snapshots,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q¯​(x)=⟨Q​(x)⟩snapshots,\overline{Q}(x)=\langle Q(x)\rangle\_{\mathrm{snapshots}}, |  | (5) |

computed separately for bid (demand) and ask (supply) sides.

### A.5 Functional form and fitting

The averaged simulated profiles are fitted directly to the paper form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(x)=C​xγ​exp⁡(−λ​x),x>0,Q(x)=C\,x^{\gamma}\exp(-\lambda x),\qquad x>0, |  | (6) |

using nonlinear least-squares optimization with positivity constraints on all
parameters.
Fits are restricted to bins sufficiently close to the mid to avoid finite-size
effects at large distances.

The goal of the simulation is structural verification rather than quantitative
calibration.
It demonstrates that gamma-like liquidity profiles arise robustly from the
projection of an inflationary relational substrate, even in the absence of
agent behavior, explicit price dynamics, or equilibrium mechanisms.

## References

* [1]

  J. P. Pires da Cruz,
  Introduction to the Physics of the Economy and Finance
  (Springer Nature Switzerland, Cham, 2025).
* [2]

  F. R. K. Chung,
  Spectral Graph Theory
  (American Mathematical Society, Providence, RI, 1997).
* [3]

  M. Belkin and P. Niyogi,
  Neural Comput. 15, 1373 (2003).
* [4]

  U. von Luxburg,
  Stat. Comput. 17, 395 (2007).
* [5]

  C. Rovelli,
  Quantum Gravity
  (Cambridge University Press, Cambridge, 2004).
* [6]

  D. Oriti,
  in Foundations of Space and Time,
  edited by G. Ellis, J. Murugan, and A. Weltman
  (Cambridge University Press, Cambridge, 2014), pp. 257–320.
* [7]

  J. Ambjørn, J. Jurkiewicz, and R. Loll,
  Phys. Rev. D 72, 064014 (2005).
* [8]

  A.-L. Barabási and R. Albert,
  Science 286, 509 (1999).
* [9]

  J.-P. Bouchaud and M. Potters,
  Theory of Financial Risk and Derivative Pricing
  (Cambridge University Press, Cambridge, 2003).
* [10]

  J. D. Farmer and F. Lillo,
  Quant. Finance 4, 7 (2004).
* [11]

  I. I. Zovko and J. D. Farmer,
  Quant. Finance 2, 387 (2002).
* [12]

  E. Smith, J. D. Farmer, L. Gillemot, and S. Krishnamurthy,
  Phys. Rev. E 67, 045106 (2003).
* [13]

  J.-P. Bouchaud, M. Mézard, and M. Potters,
  Quant. Finance 2, 251 (2002).
* [14]

  S. Mike and J. D. Farmer,
  J. Econ. Dyn. Control 32, 200 (2008).
* [15]

  J.-P. Bouchaud, Y. Gefen, M. Potters, and M. Wyart,
  Quant. Finance 4, 176 (2004).
* [16]

  J.-P. Bouchaud, J. D. Farmer, and F. Lillo,
  in Handbook of Financial Markets: Dynamics and Evolution,
  edited by T. Hens and K. R. Schenk-Hoppé
  (Elsevier, Amsterdam, 2009), pp. 57–160.
* [17]

  R. Cont, S. Stoikov, and R. Talreja,
  Oper. Res. 58, 549 (2010).