---
authors:
- Sam Babichenko
doc_id: arxiv:2603.12140v1
family_id: arxiv:2603.12140
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Forecasting and Manipulating the Forecasts of Others
url_abs: http://arxiv.org/abs/2603.12140v1
url_html: https://arxiv.org/html/2603.12140v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sam Babichenko
Department of Statistics and Applied Probability, South Hall,
University of California, Santa Barbara, CA 93106, USA.
E-mail: sam@sbabichenko.com.
I am grateful to my advisor Tomoyuki Ichiba for guidance and
support throughout this project. I thank Javier Birchenall for
valuable discussions on the economic applications. Thiha Aung, Olivier Mulkin, Yan Lashchev, and Daniel Naylor provided encouragement and companionship
throughout my doctoral studies.
Replication code is available at
<https://github.com/sbabichenko/Noise-State-Games>.

###### Abstract

In strategic environments with private information, evaluating a change in policy requires predicting how the equilibrium responds—but when actions reshape opponents’ signals, each agent’s optimal response depends on an infinite hierarchy of beliefs about beliefs [[28](#bib.bib28)] that has resisted exact analysis for four decades. We provide the first exact equilibrium characterization of finite-player continuous-time LQG games with endogenous signals. Conditioning on primitive Brownian shocks rather than the physical state—a dynamic analogue of Harsanyi’s common-prior construction—collapses the belief hierarchy onto deterministic two-time kernels, reducing Nash equilibrium to a deterministic fixed point with no truncation and no large-population limit. The characterization yields an explicit information wedge 𝒱ti\mathcal{V}^{i}\_{t}—a deterministic Volterra process—that prices the marginal value of shifting opponents’ posteriors. The wedge vanishes precisely when signals are exogenous to controls, formally delineating the boundary where strategic belief manipulation matters, and provides a closed-form mapping from information primitives to equilibrium outcomes.

## 1 Introduction

In strategic environments with private information, evaluating a change in policy—a disclosure mandate, a shift in the precision of public communication, a redesign of market transparency—requires understanding how the equilibrium responds, not merely how agents behave under existing rules. When a regulator alters the information structure, each agent’s optimal action depends on their beliefs about the state and on their beliefs about how others are filtering, and both change with the policy. The filtering environment and the strategic equilibrium are jointly determined.

This joint determination is the central obstacle. Consider a central bank shifting from quarterly to real-time disclosure of its output gap estimates. Each firm’s pricing decision depends on its belief about the gap and on its belief about how other firms filter the bank’s announcements. Under the new policy, signal precision changes, which changes how firms filter, which changes how each firm forecasts the pricing decisions of others, which changes equilibrium inflation dynamics. Existing tools cannot trace this chain because the Townsend hierarchy makes the mapping from signal precision to equilibrium outcomes intractable. The characterization in this paper makes it explicit.

The same obstruction arises across a wide range of fields: in market microstructure, where prices aggregate dispersed information and trading itself is informative; in dynamic information design, where the mapping from signal structures to equilibrium outcomes is intractable when filtering and equilibrium interact; in contract theory, where multiple agents exert unobservable effort on a shared outcome and draw inferences from it; and in decentralized control—autonomous vehicle fleets, multi-robot systems with misaligned operators—wherever agents observe a shared state through private channels and actions reshape what others sense. Existing approaches to the decentralized control problem typically assume cooperative teams or a common information base; the framework here requires neither.

Townsend [[28](#bib.bib28)] crystallized the difficulty: in a game with private signals, each agent must forecast others’ forecasts of the state, generating an infinite hierarchy of conditional expectations. Sargent [[26](#bib.bib26)] showed that even in linear–Gaussian environments the hierarchy prevents finite-dimensional recursive analysis, because each agent’s action enters the state dynamics, entangling every agent’s past actions, beliefs, and signals in a way the Kalman filter cannot close.

The conceptual move parallels Harsanyi’s [[10](#bib.bib10)] resolution of the belief hierarchy in incomplete-information games. Harsanyi replaced an infinite regress of beliefs about beliefs with a common prior over a type space from which all higher-order beliefs follow by conditioning. We replace the Townsend regress with the common probability space of primitive shocks W=(W0,…,Wn)W=(W^{0},\ldots,W^{n}), from which all higher-order conditional expectations follow by orthogonal projection onto deterministic two-time kernels with no truncation. The analogy is imperfect in a revealing way: Harsanyi’s types are drawn once and the information partition is fixed, whereas here noise unfolds continuously and actions reshape signals, so the closure requires not just a common prior but a fixed point—the deterministic kernels governing how projections evolve must be consistent with the strategy profile they induce (Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Forecasting and Manipulating the Forecasts of Others")).

In the single-agent problem the conditional mean of the state is a sufficient statistic, but the state estimate is a linear functional of the noise estimate, not the reverse. In the multi-agent setting the state estimate fails to close the equilibrium because it entangles exogenous shocks with endogenous responses—precisely the Townsend hierarchy. Estimating the noise path avoids this entanglement. We call the path W^ti​(⋅):=𝔼​[W⋅∣ℱti]\widehat{W}\_{t}^{i}(\cdot):=\mathbb{E}[W\_{\cdot}\mid\mathcal{F}\_{t}^{i}] the player’s *noise-state*; optimal controls are affine functionals of it, just as single-agent controls are affine in the state estimate.

The main results establish that the best response to any profile of deterministic-kernel strategies is itself deterministic-kernel (closure over the full admissible L2L^{2} class), so Nash equilibrium reduces to a deterministic fixed point in two-time kernels. The equilibrium characterization produces an explicit information wedge 𝒱ti\mathcal{V}^{i}\_{t}: a Volterra process with deterministic mean 𝒱¯i​(t)\bar{\mathcal{V}}^{i}(t) and deterministic kernel 𝒱i​(t,r)\mathcal{V}^{i}(t,r), which prices the marginal value to player ii of shifting opponents’ posteriors. The mean wedge distorts equilibrium mean actions; the kernel wedge distorts equilibrium impulse responses. Both vanish identically when signals are exogenous to controls, formally delineating the boundary where strategic belief manipulation matters. The propagation Δ​Pi→Δ​X~i→Δ​𝒱ti→Δ​Di\Delta P^{i}\to\Delta\widetilde{X}^{i}\to\Delta\mathcal{V}^{i}\_{t}\to\Delta D^{i} provides an explicit mapping from information primitives to equilibrium outcomes that a model with fixed filtering cannot deliver: because information enters through precision paths {Pi​(⋅)}\{P^{i}(\cdot)\} and affects the equilibrium only through deterministic filtering sensitivities, a principal can trace how disclosure precision propagates into equilibrium payoffs without simulating higher-order beliefs.

(i) Candidate
Opponents use
Volterra controls

(ii) Closure
State & filters
have det. kernels

(iii) Deviations
Fixed maps ⇒\Rightarrow
det. propagation

(iv) Best response
FOC ⇒\Rightarrow control
linear in W^i\widehat{W}^{\,i}

(v) Fixed point
BR map closes
⟺\Longleftrightarrow Nash eq.


Figure 1: The Volterra fixed-point loop.
(i) Assume opponents use Volterra controls with deterministic kernels.
(ii) The state and filtering equations close on deterministic two-time kernels.
(iii) Under fixed strategy maps, unobserved deviations propagate deterministically.
(iv) The maximum principle produces a best response that is itself Volterra, closing the loop.
(v) A fixed point of this best-response map is a Nash equilibrium.

### 1.1 Related Literature

The joint determination of filtering and equilibrium has been approached from
several directions, each achieving tractability by restricting or removing the
informational externality that makes the problem hard.

##### Higher-order expectations and the social value of information.

The infinite regress of “forecasting the forecasts of others” was identified by
Townsend [[28](#bib.bib28)] and shown by Sargent [[26](#bib.bib26)] to resist
finite-dimensional recursive analysis even in linear–Gaussian environments.
Morris and Shin [[20](#bib.bib20)] demonstrated that the social value of
public information can be negative when agents overweight common signals—a
static manifestation of the belief-manipulation channel that arises dynamically
through the information wedge 𝒱ti\mathcal{V}^{i}\_{t}.
Our Proposition [3.6](#S3.Thmthm6 "Proposition 3.6 (Information cost). ‣ Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") provides a dynamic counterpart:
Section [4](#S4 "4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others") shows that nearly all welfare
gains from pooling come from eliminating the strategic channel rather than
improving state estimation, consistent with the Morris–Shin intuition that the
coordination externality, not statistical efficiency, drives welfare losses.

##### Frequency-domain methods and exogenous-signal models.

A substantial literature solves dispersed-information models in the frequency
domain [[9](#bib.bib9), [14](#bib.bib14), [24](#bib.bib24)], culminating in Huo
and Takayama [[12](#bib.bib12)], who obtain finite-state representations
for equilibrium aggregates under exogenous ARMA signals.
These methods succeed because the filtering environment is invariant to changes
in control laws—the spectral factorization can be solved independently of
the policy.
When controls enter the state dynamics the transfer function depends on the
policy, breaking this separation; the present paper addresses this
complementary case.

##### Common-information approaches.

A powerful technique in decentralized control conditions on a common information
base shared by all agents to obtain a recursive reduction
[[21](#bib.bib21)].
The approach handles asymmetric information but resolves it through a coordinator’s beliefs; the channel by which player ii’s action shifts player kk’s posterior, which
shifts kk’s action, which shifts ii’s signal, is not captured.

##### Team theory.

The decentralized decision problem with shared objectives originates with
Marschak and Radner [[19](#bib.bib19)]; Radner [[23](#bib.bib23)]
established certainty equivalence and linear optimal policies for LQG teams.
Team-theoretic solutions bypass the belief hierarchy because aligned objectives
eliminate the incentive to manipulate others’ forecasts.
The information wedge 𝒱ti\mathcal{V}^{i}\_{t} is precisely the object that vanishes
under team objectives and survives under misaligned payoffs.

##### Mean-field LQG games.

Mean-field games take large-population limits in which no single agent’s action
measurably affects any other agent’s signal
[[6](#bib.bib6), [11](#bib.bib11)].
Carmona and Delarue [[7](#bib.bib7)] provide a comprehensive
two-volume treatment including LQG specifications with common noise.
The bilateral informational externality is absent by construction in the
mean-field limit; 𝒱ti\mathcal{V}^{i}\_{t} is a finite-nn object that vanishes in any
limit where individual actions become negligible.

##### Truncation of the belief hierarchy.

Nimark [[22](#bib.bib22)] approximates the higher-order belief hierarchy by
truncation at finite order—the closest existing method in spirit to the
present paper.
The deterministic kernel system derived here provides an exact benchmark
against which truncation error can be assessed.

##### Applied continuous-time filtering games.

Kyle [[15](#bib.bib15)], Back [[2](#bib.bib2)], and Foster and
Viswanathan [[8](#bib.bib8)] solve strategic trading problems with
private information, each exploiting special structure—a single informed
trader, correlated-signal symmetry—to close the belief hierarchy through
model-specific conjectures.
Sannikov [[25](#bib.bib25)] solves a continuous-time principal–agent problem
by showing that the agent’s continuation value serves as a sufficient statistic
for the principal’s problem, yielding a recursive characterization despite the
agent’s private action.
The technique relies on the bilateral structure: the principal’s belief about
a single agent’s hidden action can be summarized by a one-dimensional state
variable, and the agent has no beliefs about other agents to forecast.
With multiple agents exerting unobservable effort on a shared outcome—the
moral-hazard analogue of our setting—each agent draws inferences from the
shared output about others’ effort, generating the same belief hierarchy that
arises here.
The noise-state framework extends naturally to this setting: each agent’s
hidden effort enters the output dynamics exactly as controls enter the state
in ([2.1](#S2.E1 "In State dynamics. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")), and the information wedge prices the value of
shifting the principal’s and co-agents’ posteriors about one’s effort.
The present paper provides a general framework that nests these as special
cases: in the Kyle–Back embedding (Section [5](#S5 "5 Market microstructure as a special case ‣ Forecasting and Manipulating the Forecasts of Others")), the
information wedge corresponds to the strategic component of price impact, and
the characterization extends to multi-trader settings where guess-and-verify
breaks down.

##### Information design.

Kamenica and Gentzkow [[13](#bib.bib13)] established Bayesian persuasion;
Bergemann and Morris [[3](#bib.bib3), [4](#bib.bib4)]
introduced Bayes correlated equilibrium and survey the field, identifying
dynamic decentralized settings as a central open problem.
Bergemann, Heumann, and Morris [[5](#bib.bib5)] provide
precision comparative statics in static coordination games analogous to the
propagation Δ​Pi→Δ​𝒱ti→Δ​Ji\Delta P^{i}\to\Delta\mathcal{V}^{i}\_{t}\to\Delta J^{i} derived here.
The difficulty in extending these results dynamically is that filtering and
equilibrium interact; our characterization provides the equilibrium mapping
that dynamic information design requires as an input.

##### Rational inattention.

Sims [[27](#bib.bib27)] introduced rational inattention;
Maćkowiak and Wiederholt [[17](#bib.bib17)] showed that firms
optimally attend to idiosyncratic over aggregate conditions, generating sluggish
price adjustment (see Maćkowiak, Mat́ejka, and
Wiederholt [[18](#bib.bib18)] for a survey).
These models take the strategic environment as given when solving the attention
problem; Corollary [3.7](#S3.Thmthm7 "Corollary 3.7 (Endogenous precision closure). ‣ Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") and the FOC ([C.9](#A3.E9 "In Endogenous precision. ‣ C.3 The Hamilton–Jacobi–Bellman equation ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"))
extend the framework to settings where the marginal value of precision depends
on the equilibrium through the information wedge.

## 2 The Decentralized LQG Game

##### Informal description of the game.

The class of games we study has three features:
(i) multiple agents share a common evolving state but observe it through private noisy channels;
(ii) each agent’s action feeds back into the state dynamics and thereby into every other agent’s signal process; and
(iii) agents minimize individual quadratic objectives over a finite horizon.
Because actions enter the state, they simultaneously serve the physical objective and reshape what opponents observe, making each agent’s problem jointly strategic and informational.
Features (i)–(ii) generate the infinite belief hierarchy identified by Townsend; feature (iii) provides the linear–Gaussian structure that makes it tractable.

### 2.1 Primitives

Consider nn players interacting over a finite time horizon [0,T][0,T] on a
filtered probability space (Ω,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}).

##### State dynamics.

The state Xt∈ℝdX\_{t}\in\mathbb{R}^{d} evolves as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(A​(t)​Xt+∑i=1nDti)​d​t+Σ​(t)​d​Wt0,X0=x0,dX\_{t}=\bigl(A(t)X\_{t}+\sum\_{i=1}^{n}D\_{t}^{i}\bigr)dt+\Sigma(t)\,dW\_{t}^{0},\qquad X\_{0}=x\_{0}, |  | (2.1) |

where A​(t)∈ℝd×dA(t)\in\mathbb{R}^{d\times d} is deterministic and bounded,
W0W^{0} is a dd-dimensional Brownian motion,
Σ​(t)∈ℝd×d\Sigma(t)\in\mathbb{R}^{d\times d} is deterministic and bounded,
and Dti∈ℝdD\_{t}^{i}\in\mathbb{R}^{d} is player ii’s control.

###### Remark 2.1 (Control matrices and dimensions).

All results extend to Dti=Bi​(t)​UtiD\_{t}^{i}=B\_{i}(t)U\_{t}^{i} with control UtiU^{i}\_{t} by appropriately modifying the cost function and first order conditions.

##### Observations.

Player ii does not observe XtX\_{t} directly. Instead, they observe a
noisy measurement process Yti∈ℝdY^{i}\_{t}\in\mathbb{R}^{d} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yti=Pi​(t)​Xt​d​t+d​Wti,Y0i=0,dY^{i}\_{t}=\sqrt{P^{i}(t)}X\_{t}\,dt+dW^{i}\_{t},\quad Y^{i}\_{0}=0, |  | (2.2) |

where:111The square-root parameterization is convenient for interpreting
Pi​(t)P^{i}(t) as a precision matrix, but all results extend to observation
channels of the form d​Yti=Hi​(t)​Xt​d​t+Ei​(t)​d​WtdY^{i}\_{t}=H^{i}(t)X\_{t}\,dt+E^{i}(t)\,dW\_{t} with
arbitrary deterministic Hi​(t)∈ℝdi×dH^{i}(t)\in\mathbb{R}^{d\_{i}\times d} and
Ei​(t)​Ei​(t)⊤=IE^{i}(t)E^{i}(t)^{\top}=I, including correlated observation noises across
players and signals that weight different state coordinates
asymmetrically.
All kernel formulas remain verbatim under this generalization.

* •

  Wti∈ℝdW^{i}\_{t}\in\mathbb{R}^{d} is a standard Brownian motion
  (player ii’s observation noise),
* •

  Pi​(t)∈ℝd×dP^{i}(t)\in\mathbb{R}^{d\times d} is symmetric positive semidefinite, and
  Pi​(t)\sqrt{P^{i}(t)} denotes its unique symmetric positive
  semidefinite square root.
* •

  All Brownian motions {W0,W1,…,Wn}\{W^{0},W^{1},\ldots,W^{n}\} are mutually
  independent.

##### Stacked noise and block selectors.

We collect all primitive noises into a single vector
Wt:=(Wt0,…,Wtn)⊤∈ℝ(n+1)​dW\_{t}:=(W^{0}\_{t},\dots,W^{n}\_{t})^{\top}\in\mathbb{R}^{(n+1)d}.
For each j∈{0,…,n}j\in\{0,\dots,n\}, the block selector Ej∈ℝd×(n+1)​dE^{j}\in\mathbb{R}^{d\times(n+1)d}
extracts the jj-th channel: Ej​Wt=WtjE^{j}W\_{t}=W^{j}\_{t}.
The block projector Πi:=Ei,⊤​Ei\Pi^{i}:=E^{i,\top}E^{i} is the identity on the ii-th block
and zero elsewhere: Πi​v=(0,…,0,vi,0,…,0)\Pi^{i}v=(0,\dots,0,v^{i},0,\dots,0).
Player ii directly observes Πi​W\Pi^{i}W and must infer (I−Πi)​W(I-\Pi^{i})W from drift-based learning.

Player ii’s information at time tt is their observation history,
ℱti:=σ(Ysi:s≤t)\mathcal{F}^{i}\_{t}:=\sigma(Y^{i}\_{s}:s\leq t).
An admissible control is ℱti\mathcal{F}^{i}\_{t}-adapted with
𝔼​[∫0T‖Dti‖2​𝑑t]<∞\mathbb{E}[\int\_{0}^{T}\|D^{i}\_{t}\|^{2}\,dt]<\infty,
where ∥⋅∥\|\cdot\| denotes the Euclidean norm on ℝd\mathbb{R}^{d}.

##### Unresolved state kernel.

For each player ii, define

|  |  |  |
| --- | --- | --- |
|  | X~i​(t,u):=X​(t,u)−X^i​(t,u),\widetilde{X}^{i}(t,u):=X(t,u)-\widehat{X}^{\,i}(t,u), |  |

the component of the state’s impulse response to the uu-th shock that player ii
has not yet resolved at time tt—large when the shock is recent or the
observation channel weak, and shrinking as observations accumulate.
Formally, X~i​(t,u)=Cov⁡(Xt,d​Wu∣ℱti)/d​u\widetilde{X}^{i}(t,u)=\operatorname{Cov}(X\_{t},\,dW\_{u}\mid\mathcal{F}\_{t}^{i})/du;
it serves as the filtering gain in the noise-state update
(Theorem [3.1](#S3.Thmthm1 "Theorem 3.1 (Volterra Filtering Closure). ‣ Filtering closure. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")), with its algebraic
representation in terms of FiF^{i} given in ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).

##### Objectives.

Each player ii incurs the random cost

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞i​(Di;D−i):=∫0T(Xt⊤​GX​Xi​(t)​Xt+2​(GXi​(t))⊤​Xt+Gi​(t)+(Dti)⊤​GD​Di​(t)​Dti)​𝑑t+XT⊤​GX​Xi​(T)​XT+2​GXi​(T)​XT,\begin{split}\mathcal{C}^{i}(D^{i};D^{-i}):=&\int\_{0}^{T}\left(X\_{t}^{\top}G^{i}\_{XX}(t)X\_{t}+2(G^{i}\_{X}(t))^{\top}X\_{t}+G^{i}(t)+(D^{i}\_{t})^{\top}G^{i}\_{DD}(t)D^{i}\_{t}\right)dt\\ &+X\_{T}^{\top}G^{i}\_{XX}(T)X\_{T}+2G^{i}\_{X}(T)X\_{T},\end{split} |  | (2.3) |

where GX​Xi​(t)G^{i}\_{XX}(t) and GD​Di​(t)G^{i}\_{DD}(t) are symmetric positive
semidefinite matrices (with GD​Di​(t)G^{i}\_{DD}(t) positive definite), and D−i:=(Dj)j≠iD^{-i}:=(D^{j})\_{j\neq i} denotes
opponents’ controls.
Each player ii seeks to minimize

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ji​(Di;D−i):=𝔼​[𝒞i​(Di;D−i)].J^{i}(D^{i};D^{-i}):=\mathbb{E}\bigl[\mathcal{C}^{i}(D^{i};D^{-i})\bigr]. |  | (2.4) |

Opponents’ controls enter player ii’s cost only through XtX\_{t}, which they move
via ([2.1](#S2.E1 "In State dynamics. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")) and which player ii observes through ([2.2](#S2.E2 "In Observations. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")).

### 2.2 Nash Equilibrium

Because each player’s drift depends on opponents’ estimates X^tk:=𝔼​[Xt∣ℱtk]\widehat{X}\_{t}^{k}:=\mathbb{E}[X\_{t}\mid\mathcal{F}\_{t}^{k}],
optimal actions generate an infinite hierarchy of conditional expectations. The following equilibrium concept fixes opponents’ strategy maps rather than their
realized actions, which is essential for the closure results in Section [3](#S3 "3 Main results ‣ Forecasting and Manipulating the Forecasts of Others").

###### Definition 2.1 (Nash equilibrium in private-signal strategies).

Throughout, a player’s choice is a strategy map:
for each t∈[0,T]t\in[0,T], the action DtiD\_{t}^{i} is a (progressively measurable) functional of the
private observation history Y⋅∧tiY^{i}\_{\cdot\wedge t}.
We write Dti=Dti​[Yi]D\_{t}^{i}=D\_{t}^{i}[Y^{i}], where the bracket notation Dti​[⋅]D\_{t}^{i}[\cdot] denotes the map
from the observation path (Ysi)s≤t(Y^{i}\_{s})\_{s\leq t} to the action at time tt.
We identify a strategy with its induced adapted control
process, assuming 𝔼​∫0T‖Dti‖2​𝑑t<∞\mathbb{E}\int\_{0}^{T}\|D\_{t}^{i}\|^{2}\,dt<\infty.

A profile D∗=(D∗,1,…,D∗,n)D^{\*}=(D^{\*,1},\ldots,D^{\*,n}) is a Nash equilibrium if for every player ii and every
admissible alternative strategy map D~i​[⋅]\widetilde{D}^{i}[\cdot],

|  |  |  |
| --- | --- | --- |
|  | Ji​(D∗,i;D∗,−i)≤Ji​(D~i;D∗,−i),J^{i}(D^{\*,i};D^{\*,-i})\leq J^{i}(\widetilde{D}^{i};D^{\*,-i}), |  |

where the inequality compares the costs induced by the corresponding strategy profiles.
Equivalently: in a unilateral deviation by ii, opponents’ maps are held fixed and are
applied to the deviated signal paths.

In a unilateral deviation by ii, opponents’ strategy maps
Y⋅∧tk↦Dtk​[Yk]Y^{k}\_{\cdot\wedge t}\mapsto D\_{t}^{k}[Y^{k}] are held fixed and applied to the
perturbed observation histories; in the Volterra class these maps are
parameterized by deterministic kernels that remain unchanged off equilibrium.

The requirement that opponents’ strategy maps be held fixed under deviations—rather than their realized actions or their realized beliefs—is the formal expression of the Lucas critique in this environment: if player ii changes their control law, the state dynamics change, which changes every opponent’s signal process, filtering problem, and actions, which feeds back into the state.

This paper aims to establish that the Volterra class is closed under best responses and to derive a deterministic kernel system whose fixed points correspond to Nash equilibria in that class.

##### Noise-state.

For each player ii and each t∈[0,T]t\in[0,T], define the *noise-state* as the conditional mean path of the aggregated primitive noise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W^ti​(u):=𝔼​[Wu∣ℱti],0≤u≤t.\widehat{W}\_{t}^{i}(u):=\mathbb{E}[W\_{u}\mid\mathcal{F}\_{t}^{i}],\qquad 0\leq u\leq t. |  | (2.5) |

In linear–Gaussian settings, the conditional law of primitive shocks is Gaussian with
deterministic conditional covariance, so W^ti​(⋅)\widehat{W}\_{t}^{i}(\cdot) is a complete (path-valued)
summary of player ii’s private information.

###### Definition 2.2 (Primitive-noise Volterra process).

An L2L^{2} stochastic process L=(Lt)t∈[0,T]L=(L\_{t})\_{t\in[0,T]} is a (primitive-noise) Volterra process if there exist deterministic functions

|  |  |  |
| --- | --- | --- |
|  | L¯:[0,T]→ℝm,L:[0,T]2→ℝm×(n+1)​d,\bar{L}:[0,T]\to\mathbb{R}^{m},\qquad L:[0,T]^{2}\to\mathbb{R}^{m\times(n+1)d}, |  |

such that, for every t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | Lt=L¯​(t)+∫0tL​(t,s)​𝑑Ws,∫0t‖L​(t,s)‖2​𝑑s<∞.L\_{t}\;=\;\bar{L}(t)+\int\_{0}^{t}L(t,s)\,dW\_{s},\qquad\int\_{0}^{t}\|L(t,s)\|^{2}\,ds<\infty. |  |

When convenient, we extend L​(t,s)L(t,s) by 0 for s>ts>t.

###### Remark 2.2 (Properties of primitive-noise Volterra processes).

By construction, primitive-noise Volterra processes are 𝔽\mathbb{F}-adapted Gaussian processes.
Moreover, by Itô isometry the square-integrability condition above is equivalent to Lt∈L2L\_{t}\in L^{2}
for each tt. Finally, the martingale representation theorem implies that any L2L^{2}
ℱt\mathcal{F}\_{t}-measurable random variable admits a representation of the form
∫0tZs​𝑑Ws\int\_{0}^{t}Z\_{s}\,dW\_{s} with a stochastic integrand ZZ; the defining restriction of the
Volterra class is that the representation kernel L​(t,⋅)L(t,\cdot) is deterministic (for each fixed tt).

###### Definition 2.3 (Noise-state Volterra control / strategy).

Fix a player ii and recall their noise-state path W^ti​(⋅)\widehat{W}\_{t}^{i}(\cdot)
(Section [3](#S3 "3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")). An admissible control
Di=(Dti)t∈[0,T]D^{i}=(D\_{t}^{i})\_{t\in[0,T]} is a noise-state Volterra control if there exist deterministic functions

|  |  |  |
| --- | --- | --- |
|  | D¯i:[0,T]→ℝd,Di:[0,T]2→ℝd×(n+1)​d,\bar{D}^{i}:[0,T]\to\mathbb{R}^{d},\qquad D^{i}:[0,T]^{2}\to\mathbb{R}^{d\times(n+1)d}, |  |

such that, for every t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | Dti=D¯i​(t)+∫0tDi​(t,u)​du​W^ti​(u),∫0t‖Di​(t,u)‖2​𝑑u<∞,D\_{t}^{i}=\bar{D}^{i}(t)+\int\_{0}^{t}D^{i}(t,u)\,d\_{u}\widehat{W}\_{t}^{i}(u),\qquad\int\_{0}^{t}\|D^{i}(t,u)\|^{2}\,du<\infty, |  |

and we extend Di​(t,u)D^{i}(t,u) by 0 for u>tu>t.
Equivalently, writing W^i​[Yi]\widehat{W}^{\,i}[Y^{i}] to emphasize dependence on the observation path,
this defines the strategy map

|  |  |  |
| --- | --- | --- |
|  | Y⋅∧ti⟼Dti[Yi]:=D¯i(t)+∫0tDi(t,u)duW^ti[Yi](u).Y^{i}\_{\cdot\wedge t}\longmapsto D\_{t}^{i}[Y^{i}]:=\bar{D}^{i}(t)+\int\_{0}^{t}D^{i}(t,u)\,d\_{u}\widehat{W}\_{t}^{\,i}[Y^{i}](u). |  |

## 3 Main results

We work in the linear–Gaussian model of Section [2](#S2 "2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")
and establish two closure results—filtering and best response—that
reduce Nash equilibrium to a deterministic fixed point in two-time kernels.
The filtering closure (Theorem [3.1](#S3.Thmthm1 "Theorem 3.1 (Volterra Filtering Closure). ‣ Filtering closure. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")) shows that
noise-state dynamics have deterministic kernels;
the best-response closure (Theorem [3.2](#S3.Thmthm2 "Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")) derives the
adjoint system and the information wedge;
Proposition [3.6](#S3.Thmthm6 "Proposition 3.6 (Information cost). ‣ Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") then decomposes equilibrium cost into a
certainty-equivalent term and an information cost linked to
endogenous precision.

##### Filtering closure.

Recall the noise-state W^ti​(⋅)\widehat{W}\_{t}^{i}(\cdot) ([2.5](#S2.E5 "In Noise-state. ‣ 2.2 Nash Equilibrium ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")).
We record the deterministic-kernel representation of the estimated-noise increment
and its innovations gain in noise-state coordinates.
Two-time kernels throughout live on the causal triangle
ΔT:={(t,s)∈[0,T]2:0≤s≤t≤T}\Delta\_{T}:=\{(t,s)\in[0,T]^{2}:0\leq s\leq t\leq T\}, extended by 0 off ΔT\Delta\_{T}.
We write dud\_{u} for increments in the path index uu at fixed estimation time tt,
and dtd\_{t} for updates in tt at fixed uu.
The state is assumed to admit the Volterra form
Xt=X¯​(t)+∫0tX​(t,s)​𝑑WsX\_{t}=\bar{X}(t)+\int\_{0}^{t}X(t,s)\,dW\_{s}, where X​(t,s)∈ℝd×(n+1)​dX(t,s)\in\mathbb{R}^{d\times(n+1)d} is a
deterministic impulse-response kernel mapping primitive shocks into the physical state.

###### Theorem 3.1 (Volterra Filtering Closure).

Fix a player ii.
Assume the state admits the primitive-noise Volterra form

|  |  |  |
| --- | --- | --- |
|  | Xt=X¯​(t)+∫0tX​(t,s)​𝑑Ws,X\_{t}=\bar{X}(t)+\int\_{0}^{t}X(t,s)\,dW\_{s}, |  |

and player ii observes

|  |  |  |
| --- | --- | --- |
|  | d​Yti=Pi​(t)​Xt​d​t+Ei​d​Wt,dY\_{t}^{i}=\sqrt{P^{i}(t)}\,X\_{t}\,dt+E^{i}\,dW\_{t}, |  |

with deterministic Pi​(t)⪰0P^{i}(t)\succeq 0 and block selector EiE^{i}.

Let Πi:=Ei,⊤​Ei\Pi^{i}:=E^{i,\top}E^{i} and X^ti:=𝔼​[Xt∣ℱti]\widehat{X}\_{t}^{i}:=\mathbb{E}[X\_{t}\mid\mathcal{F}\_{t}^{i}], and define the innovation
d​Iti:=d​Yti−Pi​(t)​X^ti​d​tdI\_{t}^{i}:=dY\_{t}^{i}-\sqrt{P^{i}(t)}\,\widehat{X}\_{t}^{i}\,dt.

(i) The estimated-noise path increments admit the decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | du​W^ti​(u)=Πi​d​Wu+(∫0tFti​(u,s)​𝑑Ws)​d​u,u<t,d\_{u}\widehat{W}\_{t}^{i}(u)=\Pi^{i}\,dW\_{u}+\Big(\int\_{0}^{t}F\_{t}^{i}(u,s)\,dW\_{s}\Big)\,du,\qquad u<t, |  | (3.1) |

where the deterministic kernel FiF^{i} is given explicitly by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fti​(u,s)=X~i​(s,u)⊤​Pi​(s)​Ei+Ei,⊤​Pi​(u)​X~i​(u,s)+∫max⁡(u,s)tX~i​(r,u)⊤​Pi​(r)​X~i​(r,s)​𝑑r.F\_{t}^{i}(u,s)=\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,E^{i}\;+\;E^{i,\top}\sqrt{P^{i}(u)}\,\widetilde{X}^{i}(u,s)\;+\;\int\_{\max(u,s)}^{t}\widetilde{X}^{i}(r,u)^{\top}P^{i}(r)\,\widetilde{X}^{i}(r,s)\,dr. |  | (3.2) |

(ii) The mixed (t,u)(t,u)-update satisfies

|  |  |  |
| --- | --- | --- |
|  | dt​(du​W^ti​(u))=X~i​(t,u)⊤​Pi​(t)​d​Iti​d​u.d\_{t}\bigl(d\_{u}\widehat{W}\_{t}^{i}(u)\bigr)=\widetilde{X}^{i}(t,u)^{\top}\sqrt{P^{i}(t)}\,dI\_{t}^{i}\,du. |  |

The unresolved kernel X~i\widetilde{X}^{i} is determined algebraically
from FiF^{i} by ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")); the filtering kernel FiF^{i}
is the unique solution of the forward evolution
system ([A.14](#A1.E14 "In Definition A.1 (Filtering kernel system). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))–([A.15](#A1.E15 "In Definition A.1 (Filtering kernel system). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))
(Definition [A.1](#A1.Thmdefn1 "Definition A.1 (Filtering kernel system). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).

###### Remark 3.1 (Regression interpretation and scale separation).

Discretizing time, each observation increment is affine in the noise
increments Δ​W1:k\Delta W\_{1:k}, so by joint Gaussianity the conditional mean
𝔼​[Δ​W1:k∣Δ​Y1:ki]\mathbb{E}[\Delta W\_{1:k}\mid\Delta Y^{i}\_{1:k}] is a deterministic linear
projection; each layer of “beliefs about beliefs” is a further
deterministic composition of projections, which is why the regress closes.
The decomposition in part (i) reflects a scale separation: the direct
component Πi​d​Wu\Pi^{i}\,dW\_{u} is O​(1)O(1) (player ii observes their own noise
contemporaneously), while the indirect component—absolutely continuous
in uu with density driven by FiF^{i}—captures drift-based inference
about unobserved noise coordinates at scale O​(d​t)O(dt).

##### Best-response closure and information wedges.

When opponents use noise-state Volterra strategies, a player’s best response over the
full admissible L2L^{2} class remains noise-state Volterra; the maximum principle yields
a closed backward system of deterministic adjoint kernels including the information
wedge 𝒱i​(t)\mathcal{V}^{i}(t) that prices bilateral belief manipulation.

###### Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges).

Fix a player ii and suppose each opponent k≠ik\neq i uses a noise-state Volterra strategy with deterministic kernels, which pins down a deterministic forward kernel environment
(state impulse response X​(⋅,⋅)X(\cdot,\cdot), filtering objects (Pk,X~k,Fk)(P^{k},\widetilde{X}^{k},F^{k}), and policy kernels DkD^{k}).

Structure.
Because the equilibrium control is a Volterra process Dti=D¯i​(t)+∫0tDi​(t,u)​𝑑WuD\_{t}^{i}=\bar{D}^{i}(t)+\int\_{0}^{t}D^{i}(t,u)\,dW\_{u} with deterministic mean and kernel, the backward system splits into two structurally identical subsystems—one for the mean coefficients (H¯Xi,H¯k,i)(\bar{H}\_{X}^{i},\bar{H}^{k,i}), one for the kernel coefficients (HXi,Hk,i)(H\_{X}^{i},H^{k,i})—that should be read in parallel.

In each subsystem, the single-agent costate acquires an additional coupling term: player ii’s action shifts the state, which shifts opponent kk’s signal, posterior, and action, feeding back into the state.
This channel introduces *belief-adjoint* variables (H¯k,i,Hk,i)(\bar{H}^{k,i},H^{k,i}) that track the shadow value of perturbing opponent kk’s noise-state estimate, coupled into the physical costate through the opponents’ filtering gains.

Mean backward system.
The mean physical costate H¯Xi​(t)\bar{H}\_{X}^{i}(t) and mean belief-adjoints H¯k,i​(t,u)\bar{H}^{k,i}(t,u) satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​H¯Xi​(t)\displaystyle\frac{d}{dt}\bar{H}\_{X}^{i}(t) | =−(GX​Xi​(t)​X¯​(t)+GX​(t))−A​(t)⊤​H¯Xi​(t)−∑k≠i∫0tPk​(t)​X~k​(t,z)​H¯k,i​(t,z)​𝑑z⏟=⁣:𝒱¯i​(t),mean information wedge,\displaystyle=-\big(G^{i}\_{XX}(t)\bar{X}(t)+G\_{X}(t)\big)-A(t)^{\top}\bar{H}\_{X}^{i}(t)-\underbrace{\sum\_{k\neq i}\int\_{0}^{t}P^{k}(t)\widetilde{X}^{k}(t,z)\,\bar{H}^{k,i}(t,z)\,dz}\_{=:\;\bar{\mathcal{V}}^{i}(t),\;\text{mean information wedge}}, |  | (3.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​H¯k,i​(t,u)\displaystyle\frac{d}{dt}\bar{H}^{k,i}(t,u) | =−(Dk​(t,u))⊤​H¯Xi​(t)+∫0tX​(t,u)⊤​Pk​(t)​X~k​(t,z)​H¯k,i​(t,z)​𝑑z,k≠i,\displaystyle=-\big(D^{k}(t,u)\big)^{\top}\bar{H}\_{X}^{i}(t)+\int\_{0}^{t}X(t,u)^{\top}P^{k}(t)\widetilde{X}^{k}(t,z)\,\bar{H}^{k,i}(t,z)\,dz,\qquad k\neq i, |  | (3.4) |

with terminal conditions
H¯Xi​(T)=GX​Xi​(T)​X¯​(T)+GXi​(T)\bar{H}\_{X}^{i}(T)=G^{i}\_{XX}(T)\bar{X}(T)+G^{i}\_{X}(T) and H¯k,i​(T,⋅)=0\bar{H}^{k,i}(T,\cdot)=0.

The first two terms in ([3.3](#S3.E3 "In Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")) are the standard single-agent costate equation; the third term 𝒱¯i​(t)\bar{\mathcal{V}}^{i}(t) is the mean information wedge, absent in the single-agent problem.
In the belief-adjoint equation ([3.4](#S3.E4 "In Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")), the forcing −Dk​(t,u)⊤​H¯Xi​(t)-D^{k}(t,u)^{\top}\bar{H}\_{X}^{i}(t) transmits the physical costate into the belief channel through opponent kk’s policy kernel: the larger Dk​(t,u)D^{k}(t,u), the more opponent kk’s action at time tt responds to the uu-th shock, and the more valuable it is for player ii to have shifted kk’s estimate of that shock.
The integral term is a self-coupling through which belief perturbations propagate forward via the filtering gain X~k\widetilde{X}^{k}.

Kernel backward system.
The kernel physical costate HXi​(t,r)H\_{X}^{i}(t,r) and kernel belief-adjoints Hk,i​(t,u,r)H^{k,i}(t,u,r) satisfy the structurally identical system with X¯​(t)→X​(t,r)\bar{X}(t)\to X(t,r), GX​(t)→0G\_{X}(t)\to 0, and H¯k,i​(t,u)→Hk,i​(t,u,r)\bar{H}^{k,i}(t,u)\to H^{k,i}(t,u,r):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​HXi​(t,r)\displaystyle\frac{d}{dt}H\_{X}^{i}(t,r) | =−GX​Xi​(t)​X​(t,r)−A​(t)⊤​HXi​(t,r)−∑k≠i∫0tPk​(t)​X~k​(t,z)​Hk,i​(t,z,r)​𝑑z⏟=⁣:𝒱i​(t,r),kernel information wedge,\displaystyle=-\,G^{i}\_{XX}(t)X(t,r)-A(t)^{\top}H\_{X}^{i}(t,r)-\underbrace{\sum\_{k\neq i}\int\_{0}^{t}P^{k}(t)\widetilde{X}^{k}(t,z)\,H^{k,i}(t,z,r)\,dz}\_{=:\;\mathcal{V}^{i}(t,r),\;\text{kernel information wedge}}, |  | (3.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​Hk,i​(t,u,r)\displaystyle\frac{d}{dt}H^{k,i}(t,u,r) | =−(Dk​(t,u))⊤​HXi​(t,r)+∫0tX​(t,u)⊤​Pk​(t)​X~k​(t,z)​Hk,i​(t,z,r)​𝑑z,k≠i,\displaystyle=-\big(D^{k}(t,u)\big)^{\top}H\_{X}^{i}(t,r)+\int\_{0}^{t}X(t,u)^{\top}P^{k}(t)\widetilde{X}^{k}(t,z)\,H^{k,i}(t,z,r)\,dz,\qquad k\neq i, |  | (3.6) |

with terminal conditions
HXi​(T,r)=GX​Xi​(T)​X​(T,r)H\_{X}^{i}(T,r)=G^{i}\_{XX}(T)X(T,r) and Hk,i​(T,⋅,r)=0H^{k,i}(T,\cdot,r)=0.

The two subsystems are identical in structure because they are the Volterra mean and kernel of a single stochastic costate.
We define the (full) information wedge as the Volterra process

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱ti:=𝒱¯i​(t)+∫0t𝒱i​(t,r)​𝑑Wr,\mathcal{V}^{i}\_{t}:=\bar{\mathcal{V}}^{i}(t)+\int\_{0}^{t}\mathcal{V}^{i}(t,r)\,dW\_{r}, |  | (3.7) |

which is the total distortion of the physical costate relative to the single-agent benchmark.
The mean wedge 𝒱¯i​(t)\bar{\mathcal{V}}^{i}(t) captures how belief manipulation distorts the equilibrium level (mean actions); the kernel wedge 𝒱i​(t,r)\mathcal{V}^{i}(t,r) captures how it distorts the equilibrium *response to shocks*.
Both components—and hence 𝒱ti\mathcal{V}^{i}\_{t} itself—vanish when signals are exogenous.

##### Policy interpretation of the wedge.

The information wedge 𝒱ti\mathcal{V}^{i}\_{t} vanishes identically when signals are exogenous to controls, recovering the standard LQG costate equation. When controls enter the state dynamics, a change in signal precision Pk​(t)P^{k}(t) also operates through the belief-manipulation channel: it alters how sharply opponents’ posteriors respond to drift perturbations (through X~k\widetilde{X}^{k}), which alters the shadow value of shifting those posteriors (through H¯k,i\bar{H}^{k,i}), which feeds back into the equilibrium control through ([3.3](#S3.E3 "In Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")). A model that omits this channel predicts the single-agent response where the true equilibrium response includes a strategic distortion whose mean is given by 𝒱¯i​(t)\bar{\mathcal{V}}^{i}(t) and whose shock-by-shock profile is given by 𝒱i​(t,r)\mathcal{V}^{i}(t,r). The mean wedge 𝒱¯i​(t)\bar{\mathcal{V}}^{i}(t) governs the distortion in equilibrium mean actions (Section [4.3](#S4.SS3 "4.3 Mean actions, separation failure, and bilateral belief manipulation ‣ 4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others")); the kernel wedge 𝒱i​(t,r)\mathcal{V}^{i}(t,r) governs the distortion in equilibrium impulse responses. Section [4](#S4 "4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others") quantifies both channels numerically.

###### Corollary 3.3 (Exogenous-signal reduction).

If controls do not enter the state dynamics, then 𝒱ti≡0\mathcal{V}^{i}\_{t}\equiv 0 for all ii and tt, the belief-adjoint equations ([3.4](#S3.E4 "In Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others"))–([3.6](#S3.E6 "In Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")) decouple, and the equilibrium reduces to nn independent single-agent LQG problems against a common exogenous state.

###### Lemma 3.4 (Why the maximum-principle stationarity condition is global here).

Fix opponents’ strategy maps D−iD^{-i} in the deterministic-kernel class (hence fixed linear operators
from signal histories to actions). Then player ii’s induced objective
Di↦Ji​(Di;D−i)D^{i}\mapsto J^{i}(D^{i};D^{-i}) is a strictly convex functional on the admissible L2L^{2} control space.
Consequently, the spike-variation stationarity condition
([B.8](#A2.E8 "In Stationarity condition (globally necessary and sufficient). ‣ B.4 First variation of costs and the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) is not only necessary but sufficient: any admissible control satisfying it
is the unique global best response.

###### Proof sketch.

With opponents’ maps fixed and linear, the closed-loop drift of XX is affine in DiD^{i},
so (X,D−i)(X,D^{-i}) depend affinely on DiD^{i}. The cost ([2.4](#S2.E4 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")) is quadratic with
GD​Di​(t)≻0G^{i}\_{DD}(t)\succ 0, hence strictly convex in DiD^{i}.
∎

###### Corollary 3.5 (Noise-state Volterra best response (global closure)).

Under the conditions of Theorem [3.2](#S3.Thmthm2 "Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others"), fix an opponents’ profile D−iD^{-i} of
noise-state Volterra strategies with deterministic kernels (Definition [2.3](#S2.Thmdefn3 "Definition 2.3 (Noise-state Volterra control / strategy). ‣ Noise-state. ‣ 2.2 Nash Equilibrium ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")).
If DiD^{i} is a best response to D−iD^{-i} over the full admissible L2L^{2} control class, then for a.e. t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | GD​Di​(t)​Dti+H¯Xi​(t)+∫0tHXi​(t,u)​𝑑W^ti​(u)=0,G^{i}\_{DD}(t)D\_{t}^{i}+\bar{H}\_{X}^{i}(t)+\int\_{0}^{t}H\_{X}^{i}(t,u)\,d\widehat{W}\_{t}^{i}(u)=0, |  |

and hence

|  |  |  |
| --- | --- | --- |
|  | Dti=−(GD​Di​(t))−1​H¯Xi​(t)−(GD​Di​(t))−1​∫0tHXi​(t,u)​𝑑W^ti​(u).D\_{t}^{i}=-(G^{i}\_{DD}(t))^{-1}\bar{H}\_{X}^{i}(t)-(G^{i}\_{DD}(t))^{-1}\int\_{0}^{t}H\_{X}^{i}(t,u)\,d\widehat{W}\_{t}^{i}(u). |  |

In particular, every best response over the full admissible class is itself a noise-state Volterra control
with deterministic coefficients.

###### Proof.

With opponents’ maps fixed and linear, the innovation
d​Iti:=d​Yti−Pi​(t)​X^ti​d​tdI\_{t}^{i}:=dY\_{t}^{i}-\sqrt{P^{i}(t)}\,\widehat{X}\_{t}^{i}\,dt
is a standard (ℱi,ℙ)(\mathcal{F}^{i},\mathbb{P})-Brownian motion whose law does not depend on DiD^{i}
(Liptser–Shiryaev [[16](#bib.bib16)], Theorem 7.12).
Since W^ti​(⋅)\widehat{W}\_{t}^{i}(\cdot) is a deterministic linear functional of I[0,t]iI^{i}\_{[0,t]}
(Theorem [3.1](#S3.Thmthm1 "Theorem 3.1 (Volterra Filtering Closure). ‣ Filtering closure. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") in innovations coordinates),
player ii’s control is a deterministic affine functional of the exogenous process IiI^{i}.
The induced objective is strictly convex (Lemma [3.4](#S3.Thmthm4 "Lemma 3.4 (Why the maximum-principle stationarity condition is global here). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")),
so the stationarity condition ([B.8](#A2.E8 "In Stationarity condition (globally necessary and sufficient). ‣ B.4 First variation of costs and the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) is necessary and sufficient,
yielding the stated formula.
Note that the exogeneity of IiI^{i} is a property of the best-response problem:
the deterministic kernels mediating between IiI^{i} and the noise-state depend on the
full strategy profile through the forward closure, so the equilibrium remains a
genuine fixed point (Theorem [C.5](#A3.Thmthm5 "Theorem C.5 (Short-horizon equilibrium). ‣ C.5 Well-posedness ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")).
∎

###### Remark 3.2.

Since every best response over the full admissible L2L^{2} class is noise-state Volterra
(Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")), any Nash equilibrium of the restricted game in which
players are confined to noise-state Volterra controls is automatically a Nash equilibrium
of the unrestricted game.
The open question is whether equilibria outside the deterministic-kernel class exist; Section [6](#S6 "6 Conclusion ‣ Forecasting and Manipulating the Forecasts of Others") discusses a program for ruling them out.

###### Remark 3.3 (Single-player benchmark).

When n=1n=1, 𝒱ti≡0\mathcal{V}^{i}\_{t}\equiv 0 and the ansatz
HXi​(t,r)=S​(t)​X​(t,r)H\_{X}^{i}(t,r)=S(t)X(t,r) reduces the backward system to the
standard matrix Riccati equation for SS, recovering classical
separated LQG control.

##### Risk-sensitive extension.

Replace ([2.4](#S2.E4 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")) with the entropic risk measure
Jθii:=θi−1​log⁡𝔼​[eθi​𝒞i]J^{i}\_{\theta\_{i}}:=\theta\_{i}^{-1}\log\mathbb{E}[e^{\,\theta\_{i}\mathcal{C}^{i}}],
which penalizes cost variance in addition to cost mean
(θi>0\theta\_{i}>0 governs risk aversion; θi→0\theta\_{i}\to 0 recovers ([2.4](#S2.E4 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others"))).
The entire Volterra framework carries over: the best-response FOC is identical to
Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") with the noise-state W^ti\widehat{W}\_{t}^{i} replaced by a
risk-adjusted noise-state W^ti,θ\widehat{W}^{\,i,\theta}\_{t} that tilts the conditional
mean of WW toward directions that reduce expected cost and rescales conditional
precision along directions where cost variance is large.
The filtering closure is unchanged; separation fails because the quadratic structure
of the cost reshapes the posterior without altering the observation channel.
The full statement and derivation are in Appendix [B.6](#A2.SS6 "B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")
(Theorem [B.1](#A2.Thmthm1 "Theorem B.1 (Risk-sensitive extension). ‣ B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")).

##### Information cost and endogenous precision.

At the equilibrium profile, the control gap between full and partial
information is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dti−Dti,full=(GD​Di​(t))−1​∫0tHXi​(t,u)​dW~ti​(u),D^{i}\_{t}-D^{i,\mathrm{full}}\_{t}=(G^{i}\_{DD}(t))^{-1}\int\_{0}^{t}H^{i}\_{X}(t,u)\,\mathrm{d}\widetilde{W}^{i}\_{t}(u), |  | (3.8) |

where Dti,full:=−(GD​Di​(t))−1​MtiD^{i,\mathrm{full}}\_{t}:=-(G^{i}\_{DD}(t))^{-1}M^{i}\_{t} is the
best response under full observation of WW,
Mti:=H¯Xi​(t)+∫0tHXi​(t,u)​dWuM^{i}\_{t}:=\bar{H}^{i}\_{X}(t)+\int\_{0}^{t}H^{i}\_{X}(t,u)\,\mathrm{d}W\_{u}
is the stochastic costate, and
W~ti​(u):=Wu−W^ti​(u)\widetilde{W}^{i}\_{t}(u):=W\_{u}-\widehat{W}^{i}\_{t}(u) is the noise-state
estimation error.

###### Proposition 3.6 (Information cost).

At the equilibrium profile,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ji:=Ji​(Di;D∗,−i)−Ji​(Di,full;D∗,−i)=∫0Ttr​[GD​Di​(t)−1​ΣtM,i]​dt,\Delta J^{i}:=J^{i}(D^{i};D^{\*,-i})-J^{i}(D^{i,\mathrm{full}};D^{\*,-i})=\int\_{0}^{T}\mathrm{tr}\!\left[G^{i}\_{DD}(t)^{-1}\,\Sigma^{M,i}\_{t}\right]\mathrm{d}t, |  | (3.9) |

where ΣtM,i:=Cov⁡(Mti∣ℱti)\Sigma^{M,i}\_{t}:=\operatorname{Cov}(M^{i}\_{t}\mid\mathcal{F}^{i}\_{t}) is the
costate estimation error covariance (deterministic by Gaussianity).
Moreover, Δ​Ji\Delta J^{i} depends on PiP^{i} only through the
filtering kernels (X~i,Fi)(\widetilde{X}^{i},F^{i}) and is independent
of player ii’s control DiD^{i}.

The total cost decomposes as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ji​(Di;D∗,−i)=Ji​(Di,full;D∗,−i)⏟certainty-equivalent cost+Δ​Ji​(Pi)⏟information cost,J^{i}(D^{i};D^{\*,-i})=\underbrace{J^{i}(D^{i,\mathrm{full}};D^{\*,-i})}\_{\text{certainty-equivalent cost}}+\;\underbrace{\Delta J^{i}(P^{i})}\_{\text{information cost}}, |  | (3.10) |

This decomposition underlies the welfare comparisons in
Section [4](#S4 "4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others"): the information wedge
enters through HXiH^{i}\_{X} inside ΣtM,i\Sigma^{M,i}\_{t}.
The joint optimization over (Di,Pi)(D^{i},P^{i}) separates: DiD^{i} is
determined by Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") for any given PiP^{i},
and PiP^{i} solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | minPi​(⋅)⪰0Δ​Ji​(Pi)+∫0Tci​(t,Pi​(t))​dt,\min\_{P^{i}(\cdot)\succeq 0}\quad\Delta J^{i}(P^{i})+\int\_{0}^{T}c^{i}(t,P^{i}(t))\,\mathrm{d}t, |  | (3.11) |

where cic^{i} is a convex attention cost.

###### Corollary 3.7 (Endogenous precision closure).

If each opponent k≠ik\neq i uses a deterministic precision path
Pk​(⋅)P^{k}(\cdot), then Δ​Ji\Delta J^{i} is a deterministic functional of
Pi​(⋅)P^{i}(\cdot), and the best-response precision is deterministic.

###### Proof.

Immediate from Proposition [3.6](#S3.Thmthm6 "Proposition 3.6 (Information cost). ‣ Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others"): the forward
environment and backward adjoint are deterministic, so
([3.11](#S3.E11 "In Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")) is a deterministic variational problem.
∎

###### Remark 3.4 (Connection to rational inattention).

When n=1n=1 the FOC for ([3.11](#S3.E11 "In Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")) reduces to the
continuous-time analogue of Sims [[27](#bib.bib27)]; with n>1n>1
the information wedge enters through HXiH^{i}\_{X}, so the marginal
value of precision depends on the strategic environment—a more
responsive opponent raises the return to filtering because
better inference enables more effective belief manipulation.

###### Remark 3.5 (Infinite horizon and the frequency domain).

Under time-homogeneous primitives, Volterra kernels reduce to
convolution kernels K​(t,u)=k​(t−u)K(t,u)=k(t-u) and the fixed point becomes
one in transfer functions, extending
[[12](#bib.bib12), [14](#bib.bib14), [24](#bib.bib24)] to
endogenous signals.
Rational transfer functions correspond to finite-dimensional
Markov sufficient statistics, so the pole structure of
equilibrium kernels diagnoses whether an exact state-space
reduction exists.

##### Reference: kernel objects.

For convenience, we collect the kernel objects introduced above.

|  |  |  |  |
| --- | --- | --- | --- |
| W=(W0,…,Wn)W=(W^{0},\dots,W^{n}) | primitive noise | Ei,Πi:=Ei,⊤​EiE^{i},\;\Pi^{i}:=E^{i,\top}E^{i} | selector / projector |
| W^ti​(u)\widehat{W}\_{t}^{i}(u) | noise-state | X​(t,s)X(t,s) | state impulse response |
| Fti​(u,s)F\_{t}^{i}(u,s) | filtering kernel | X~i​(t,u)\widetilde{X}^{i}(t,u) | unresolved state kernel |
| Di​(t,u)D^{i}(t,u) | policy kernel | 𝒟i​(t,s)\mathcal{D}^{i}(t,s) | primitive-noise control |
| (H¯Xi,HXi)(\bar{H}\_{X}^{i},H\_{X}^{i}) | physical adjoints | (H¯k,i,Hk,i)(\bar{H}^{k,i},H^{k,i}) | belief adjoints |
| 𝒱ti=𝒱¯i​(t)+∫0t𝒱i​(t,r)​𝑑Wr\mathcal{V}^{i}\_{t}=\bar{\mathcal{V}}^{i}(t)+\int\_{0}^{t}\mathcal{V}^{i}(t,r)\,dW\_{r} | information wedge |  |  |

## 4 Bilateral belief manipulation in a two-player game

To make the general theory concrete, we specialize to the simplest game that exhibits bilateral belief manipulation: two symmetric players with scalar state, opposing targets, and equal signal precision. This strips away all structure except the core strategic friction. Neither player observes the state directly; each receives a private diffusion signal of precision p>0p>0. Because each player’s control enters the state dynamics, it reshapes the opponent’s signal and thereby the opponent’s posterior. The information wedge 𝒱ti\mathcal{V}^{i}\_{t} of Theorem [3.2](#S3.Thmthm2 "Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") prices this externality exactly; the mean wedge 𝒱¯i​(t)\bar{\mathcal{V}}^{i}(t) is the component we visualize below.

### 4.1 Primitives, objectives, and symmetry

Fix a horizon [0,T][0,T]. The state Xt∈ℝX\_{t}\in\mathbb{R} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(Dt1+Dt2)​d​t+d​Wt0,X0=x0,dX\_{t}=\big(D\_{t}^{1}+D\_{t}^{2}\big)\,dt+dW\_{t}^{0},\qquad X\_{0}=x\_{0}, |  | (4.1) |

where W0W^{0} is a standard Brownian motion. Player i∈{1,2}i\in\{1,2\} does not observe XX
directly; instead they observe the diffusion channel

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt1=p​Xt​d​t+d​Wt1,d​Yt2=p​Xt​d​t+d​Wt2,dY\_{t}^{1}=\sqrt{p}X\_{t}\,dt+dW\_{t}^{1},\qquad dY\_{t}^{2}=\sqrt{p}X\_{t}\,dt+dW\_{t}^{2}, |  | (4.2) |

with (W0,W1,W2)(W^{0},W^{1},W^{2}) mutually independent and p>0p>0 representing root precision. Player ii chooses DiD^{i} adapted to
ℱti=σ(Ysi:s≤t)\mathcal{F}\_{t}^{i}=\sigma(Y\_{s}^{i}:s\leq t).

Running costs are symmetric tracking losses with quadratic effort penalty r>0r>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J1​(D1;D2)=𝔼​∫0T((Xt−1)2+r​(Dt1)2)​𝑑t,J2​(D2;D1)=𝔼​∫0T((Xt+1)2+r​(Dt2)2)​𝑑t.J^{1}(D^{1};D^{2})=\mathbb{E}\!\int\_{0}^{T}\Big((X\_{t}-1)^{2}+r\,(D\_{t}^{1})^{2}\Big)\,dt,\quad J^{2}(D^{2};D^{1})=\mathbb{E}\!\int\_{0}^{T}\Big((X\_{t}+1)^{2}+r\,(D\_{t}^{2})^{2}\Big)\,dt. |  | (4.3) |

There is no terminal cost in this worked example.

The model is invariant under the sign/label symmetry

|  |  |  |
| --- | --- | --- |
|  | (X,Y1,Y2,D1,D2)⟼(−X,Y2,Y1,−D2,−D1).(X,\;Y^{1},\;Y^{2},\;D^{1},\;D^{2})\ \longmapsto\ (-X,\;Y^{2},\;Y^{1},\;-D^{2},\;-D^{1}). |  |

Primitive shocksW0W^{0} (fundamental), W1,W2W^{1},W^{2} (signal noise)Private signal Yt1Y\_{t}^{1}(precision pp)State / fundamentalXtX\_{t}Private signal Yt2Y\_{t}^{2}(precision pp)Filter / beliefW^t1​(⋅)\widehat{W}\_{t}^{1}(\cdot)ActionsDti=D¯i​(t)+∫0tDi​(t,u)​du​W^ti​(u)D\_{t}^{i}=\bar{D}^{i}(t)+\int\_{0}^{t}D^{i}(t,u)\,d\_{u}\widehat{W}\_{t}^{i}(u)Filter / beliefW^t2​(⋅)\widehat{W}\_{t}^{2}(\cdot)


Figure 2: Information-to-action feedback in the worked example. Actions move XtX\_{t} and shift opponents’ beliefs, so equilibrium mean actions depend on precision pp.

### 4.2 Numerical equilibrium and kernel visualization

We now present the numerical equilibrium obtained from the Picard iteration described above.
All figures below are generated from the converged kernel profile
D1D^{1}, its primitive-noise representation 𝒟1\mathcal{D}^{1},
the state kernel XX, and the filtering kernel F1F^{1}.

##### Computation.

Equilibrium is obtained by relaxed Picard iteration on the deterministic
kernel system, discretized on a uniform grid of N=40N=40 points; no Monte
Carlo is used.
At each iterate the forward environment (X,X~i,Fi)(X,\widetilde{X}^{i},F^{i}) is
recomputed from the closure equations, the backward adjoint HXiH\_{X}^{i} is
solved by explicit backward Euler, and the updated policy is blended into
the current profile.
Parameters: T=1T=1, x0=0x\_{0}=0, r=0.1r=0.1, GX​Xi​(T)=0G^{i}\_{XX}(T)=0.
The outer residual reaches 10−510^{-5} in 1919 iterations(≈ 10{\approx}\,10 ms in C++).
At longer horizons the binding constraint is representational
(the filtering kernel becomes more singular) rather
than economic.

##### Convergence of the fixed point.

The outer Picard residual decays geometrically, confirming convergence of the
fixed-point scheme in this symmetric benchmark; we use the iteration as a
constructive computation rather than an existence proof.

##### Impulse-response viewpoint.

The key distinction is between D1​(t,s)D^{1}(t,s) (response to a shock as inferred
through the filter).

![Refer to caption](2603.12140v1/x1.png)


(a) Primitive-noise state kernel X​(t,s)X(t,s).

![Refer to caption](2603.12140v1/x2.png)


(b) Equilibrium noise-state feedback kernel D1​(t,s)D^{1}(t,s).

Figure 3: Equilibrium kernel time-slices, shown channel-by-channel for
(W0,W1,W2)(W^{0},W^{1},W^{2}) with curves colored by evaluation time tt.
(a) Both players jointly stabilize older fundamental shocks
(decay in the W0W^{0} panel); observation-noise channels show
smaller, opposed effects mediated by the belief loop.
(b) The system-noise channel dominates; observation-noise
channels exhibit curvature reflecting drift-based inference.

### 4.3 Mean actions, separation failure, and bilateral belief manipulation

Since the stochastic integral in
Dti=D¯i​(t)+∫0tDi​(t,u)​du​W^ti​(u)D\_{t}^{i}=\bar{D}^{i}(t)+\int\_{0}^{t}D^{i}(t,u)\,d\_{u}\widehat{W}\_{t}^{i}(u)
has zero unconditional mean,
𝔼​[Dti]=D¯i​(t)\mathbb{E}[D\_{t}^{i}]=\bar{D}^{i}(t) isolates the deterministic tug-of-war
over the target ±1\pm 1, while the kernel term captures
impulse responses to posterior shocks.
Under perfect information, the mean policy does not depend on
signal precision—a separation property.
Decentralized information breaks this: changing precision changes
how fast opponents’ posteriors react to drift, so players choose
actions partly to shift opponents’ beliefs, not only to move the
physical state.

![Refer to caption](2603.12140v1/x3.png)


Figure 4: Equilibrium mean control D¯1​(t)\bar{D}^{1}(t) as a function of signal
precision pp, with the perfect-information benchmark (dashed). Low
precision makes opponents’ posteriors sluggish, amplifying the incentive
to manipulate beliefs; as p→∞p\to\infty the mean policy converges to the
perfect-information limit.

##### Deadweight loss.

The kernel figures in Section [4](#S4 "4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others") describe the variance channel (through Var​(Xt)\mathrm{Var}(X\_{t})) while Figure [4](#S4.F4 "Figure 4 ‣ 4.3 Mean actions, separation failure, and bilateral belief manipulation ‣ 4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others") isolates the mean channel.
In this symmetric game the mean channel captures a purely strategic
inefficiency: effort spent shifting the opponent’s posterior raises both
tracking loss and effort cost relative to the perfect-information benchmark.

##### The information wedge as a dynamic rent density.

In the general theory (Theorem [3.2](#S3.Thmthm2 "Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")), the backward
equation for H¯X\bar{H}^{X} contains opponent-filter coupling terms that
vanish under perfect information or in the single-player case.
Here these terms aggregate into

|  |  |  |
| --- | --- | --- |
|  | 𝒱¯1​(t)=P2​(t)​∫0tX~2​(t,z)⋅H¯2​(t,z)​𝑑z,\bar{\mathcal{V}}^{1}(t)=P^{2}(t)\int\_{0}^{t}\widetilde{X}^{2}(t,z)\cdot\bar{H}^{2}(t,z)\,dz, |  |

which enters the mean adjoint equation as
dd​t​H¯X​(t)=−(X¯​(t)−1)−𝒱¯1​(t)\tfrac{d}{dt}\bar{H}^{X}(t)=-(\bar{X}(t)-1)-\bar{\mathcal{V}}^{1}(t).
The unresolved kernel X~2​(t,z)\widetilde{X}^{2}(t,z) measures how much of the zz-th
shock remains unresolved by player 2 at time tt; the belief-adjoint
H¯2​(t,z)\bar{H}^{2}(t,z) measures the shadow value to player 1 of that shift.
Their inner product 𝒱¯1​(t)\bar{\mathcal{V}}^{1}(t) prices the mean channel of bilateral belief manipulation
at time tt; Figures [5](#S4.F5 "Figure 5 ‣ The information wedge as a dynamic rent density. ‣ 4.3 Mean actions, separation failure, and bilateral belief manipulation ‣ 4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others")–[6](#S4.F6 "Figure 6 ‣ The information wedge as a dynamic rent density. ‣ 4.3 Mean actions, separation failure, and bilateral belief manipulation ‣ 4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others")
visualize this object across precision asymmetries.

![Refer to caption](2603.12140v1/x4.png)


Figure 5: Asymmetric equilibrium with p1=3p\_{1}=3 fixed and p2p\_{2} varying.
Left: mean controls D¯1​(t)\bar{D}^{1}(t) (solid) and D¯2​(t)\bar{D}^{2}(t) (dashed)
diverge as the precision gap widens.
Center: the mean state path X¯​(t)\bar{X}(t) tilts toward the
better-informed player’s target.
Right: aggregate mean effort |D¯1|+|D¯2||\bar{D}^{1}|+|\bar{D}^{2}| exceeds the
perfect-information benchmark (gray dashed), with the excess growing
in the precision asymmetry.

![Refer to caption](2603.12140v1/x5.png)


Figure 6: Mean information wedges 𝒱¯1​(t)\bar{\mathcal{V}}^{1}(t) and 𝒱¯2​(t)\bar{\mathcal{V}}^{2}(t)
as p2p\_{2} varies (p1=3p\_{1}=3 fixed).
Both wedges are hump-shaped in tt, confirming that belief manipulation
is most valuable at intermediate dates.
Increasing the opponent’s precision amplifies the wedge: a
better-informed opponent reacts more sharply to drift, raising the
marginal value of manipulating their posterior.
The wedges vanish at the terminal date, consistent with the zero
terminal condition on the belief adjoint.

![Refer to caption](2603.12140v1/x6.png)


Figure 7: Equilibrium costs under private signals (dashed) and pooled
signals (solid) with p1=3p\_{1}=3 fixed and p2p\_{2} varying.
Left: competitive targets (θ1=1\theta\_{1}=1, θ2=−1\theta\_{2}=-1).
Right: cooperative targets (θ1=θ2=0\theta\_{1}=\theta\_{2}=0).
Pooling is Pareto-improving in both cases, but the gain is an order
of magnitude larger under competition, where it eliminates the
bilateral belief-manipulation externality priced by 𝒱i​(t)\mathcal{V}^{i}(t).
Blue: player 1; red: player 2.

##### Information pooling as a Pigouvian intervention.

Figure [7](#S4.F7 "Figure 7 ‣ The information wedge as a dynamic rent density. ‣ 4.3 Mean actions, separation failure, and bilateral belief manipulation ‣ 4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others") compares equilibrium costs under
private signals with those under a pooled signal of precision P1+P2P^{1}+P^{2},
for both competitive (θ1=1\theta\_{1}=1, θ2=−1\theta\_{2}=-1) and cooperative
(θ1=θ2=0\theta\_{1}=\theta\_{2}=0) targets.
Pooling is Pareto-improving in both cases, but the gains differ by an
order of magnitude: roughly 0.020.02–0.050.05 under cooperation versus
0.30.3–0.50.5 under competition.
Since the estimation benefit of pooling enters identically regardless of
the target structure, the difference isolates the strategic externality
channel priced by 𝒱ti\mathcal{V}^{i}\_{t}: nearly all of the welfare gain from
mandatory disclosure comes from eliminating bilateral belief manipulation,
not from improving state estimation.

## 5 Market microstructure as a special case

The two-player example operates within the quadratic-cost framework of Section [2](#S2 "2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others").
We now show that the noise-state technique embeds the Kyle–Back model with no additional machinery, despite traders maximizing expected profits against the market maker’s price rather than minimizing a quadratic objective.
The embedding works because λ​(t)>0\lambda(t)>0 provides the strict convexity needed for the best-response closure, the filtering closure applies verbatim to the stacked observation channel, and the backward system of Appendix [D](#A4 "Appendix D Kyle–Back derivations ‣ Forecasting and Manipulating the Forecasts of Others") yields the optimality condition.
We derive the equilibrium characterization for a single informed trader and identify the two channels through which belief manipulation operates; the extension to multiple asymmetrically informed traders follows the same backward system and is a natural application of the general theory.

### 5.1 Model and embedding

Adjoin a fundamental-value Brownian motion WVW^{V} independent of
(W0,…,Wn)(W^{0},\dots,W^{n}), with selector EVE^{V} and projector ΠV\Pi^{V}.
The fundamental is Vt:=σV​WtVV\_{t}:=\sigma\_{V}W\_{t}^{V}.
All players observe aggregate order flow
d​Zt=∑jDtj​d​t+σ0​d​Wt0dZ\_{t}=\sum\_{j}D\_{t}^{j}\,dt+\sigma\_{0}\,dW\_{t}^{0};
trader ii additionally observes a private signal
d​Sti=pi​Vt​d​t+d​WtidS\_{t}^{i}=\sqrt{p\_{i}}\,V\_{t}\,dt+dW\_{t}^{i}.
The market maker observes only ZZ and posts the competitive
price Pt:=𝔼​[VT∣ℱt0]=σV​∫0tEV​du​W^t0​(u)P\_{t}:=\mathbb{E}[V\_{T}\mid\mathcal{F}\_{t}^{0}]=\sigma\_{V}\int\_{0}^{t}E^{V}d\_{u}\widehat{W}\_{t}^{0}(u).
Trader ii maximizes
πi:=𝔼​[∫0TDti​(VT−Pt)​𝑑t]\pi^{i}:=\mathbb{E}[\int\_{0}^{T}D\_{t}^{i}(V\_{T}-P\_{t})\,dt].
By symmetry W↦−WW\mapsto-W, all mean terms vanish.

##### Embedding.

Rescaling the order-flow channel to unit noise, trader ii’s
stacked observation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(Zt/σ0Sti)=(σ0−1pi)⏟Pi​(demand driftσV​EV​Wt)​d​t+(E0Ei)⏟ℰi​d​Wt,d\!\begin{pmatrix}Z\_{t}/\sigma\_{0}\\ S\_{t}^{i}\end{pmatrix}=\underbrace{\begin{pmatrix}\sigma\_{0}^{-1}\\[2.0pt] \sqrt{p\_{i}}\end{pmatrix}}\_{\sqrt{P^{i}}}\!\!\begin{pmatrix}\text{demand drift}\\ \sigma\_{V}E^{V}W\_{t}\end{pmatrix}\!dt\;+\;\underbrace{\begin{pmatrix}E^{0}\\ E^{i}\end{pmatrix}}\_{\mathcal{E}^{i}}\!dW\_{t}, |  | (5.1) |

which is the observation equation of Section [2](#S2 "2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")
with Pi=(σ0−1,pi)⊤\sqrt{P^{i}}=(\sigma\_{0}^{-1},\sqrt{p\_{i}})^{\top} and
Ei→ℰiE^{i}\to\mathcal{E}^{i}; the market maker has
P0=σ0−1\sqrt{P^{0}}=\sigma\_{0}^{-1}, ℰ0=E0\mathcal{E}^{0}=E^{0}.

##### Kyle’s lambda.

Define the aggregate primitive-noise demand kernel
𝒟Σ​(t,s):=∑j𝒟j​(t,s)\mathcal{D}\_{\Sigma}(t,s):=\sum\_{j}\mathcal{D}^{j}(t,s).
Since EV​E0,⊤=0E^{V}E^{0,\top}=0, all price information comes through
drift-based inference:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Pt=λ​(t)​d​It0,λ​(t):=σV​∫0tEV​C~0​(t,u)⊤​𝑑u,dP\_{t}=\lambda(t)\,dI\_{t}^{0},\qquad\lambda(t):=\sigma\_{V}\!\int\_{0}^{t}E^{V}\widetilde{C}^{0}(t,u)^{\top}du, |  | (5.2) |

where C~0\widetilde{C}^{0} is the market maker’s unresolved drift
kernel under the projection
decomposition ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).
The execution cost 𝔼​[∫Dti​Pt​𝑑t]\mathbb{E}[\int D\_{t}^{i}P\_{t}\,dt] is quadratic in
DtiD\_{t}^{i} with coefficient λ​(t)\lambda(t)—the endogenous GD​DiG^{i}\_{DD}.

### 5.2 Equilibrium characterization

The optimality condition from a unit demand impulse at tt equates the
conditional mispricing to the integrated impact cost
(Appendix [D](#A4 "Appendix D Kyle–Back derivations ‣ Forecasting and Manipulating the Forecasts of Others")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | σV​EV​∂u(W^ti−W^t0)​(u)⏟Hi,val​(t,u):information rent density=∫tTδ​Pτ​Di​(τ,u)​𝑑τ⏟Hi,imp​(t,u):impact cost density,\underbrace{\sigma\_{V}E^{V}\,\partial\_{u}\bigl(\widehat{W}\_{t}^{i}-\widehat{W}\_{t}^{0}\bigr)(u)}\_{H^{i,\mathrm{val}}(t,u):\;\text{information rent density}}\;=\;\underbrace{\int\_{t}^{T}\delta P\_{\tau}\,D^{i}(\tau,u)\,d\tau}\_{H^{i,\mathrm{imp}}(t,u):\;\text{impact cost density}}, |  | (5.3) |

where δ​Pτ\delta P\_{\tau} is the price perturbation for an impulse at tt.
Differentiating both sides in tt and solving for Di​(t,u)D^{i}(t,u) yields
a closed backward ODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(t)​Di​(t,u)=−dd​t​Hi,val​(t,u)+∫tT∂tδ​Pτ​Di​(τ,u)​d​τ,\lambda(t)\,D^{i}(t,u)=-\frac{d}{dt}H^{i,\mathrm{val}}(t,u)+\int\_{t}^{T}\partial\_{t}\delta P\_{\tau}\,D^{i}(\tau,u)\,d\tau, |  | (5.4) |

with terminal condition
Di​(T,u)=λ​(T)−1​Hi,val​(T,u)D^{i}(T,u)=\lambda(T)^{-1}H^{i,\mathrm{val}}(T,u).

###### Assumption 5.1 (Persistent price informativeness).

λ​(t)>0\lambda(t)>0 for all t∈[0,T]t\in[0,T].

This requires that aggregate order flow remains informative about the fundamental at every date, the economically relevant case since temporary uninformativeness would present an arbitrage opportunity.
The condition is self-reinforcing: positive λ\lambda induces finite trading rates, which maintain the drift informativeness that sustains λ>0\lambda>0.
It plays the role of GD​Di≻0G^{i}\_{DD}\succ 0 (Lemma [3.4](#S3.Thmthm4 "Lemma 3.4 (Why the maximum-principle stationarity condition is global here). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")), ensuring strict convexity of the best-response problem on the domain of the fixed-point operator.

The derivative dd​t​Hi,val\frac{d}{dt}H^{i,\mathrm{val}} and the deviation
system determining δ​Pτ\delta P\_{\tau} are given in
Appendix [D](#A4 "Appendix D Kyle–Back derivations ‣ Forecasting and Manipulating the Forecasts of Others").

### 5.3 Two channels of belief manipulation

Decompose δ​Pτ\delta P\_{\tau} into δ​Pτdir\delta P\_{\tau}^{\mathrm{dir}}
(computed with Dk≡0D^{k}\equiv 0, i.e. the market maker’s response alone)
and δ​Pτind:=δ​Pτ−δ​Pτdir\delta P\_{\tau}^{\mathrm{ind}}:=\delta P\_{\tau}-\delta P\_{\tau}^{\mathrm{dir}}
(opponent-mediated).
Since δ​Pτdir=λ​(t)\delta P\_{\tau}^{\mathrm{dir}}=\lambda(t) for all τ≥t\tau\geq t,
the impact adjoint splits into:

1. (i)

   𝒱i,price​(t,u)=λ​(t)​∫tTDi​(τ,u)​𝑑τ\mathcal{V}^{i,\mathrm{price}}(t,u)=\lambda(t)\int\_{t}^{T}D^{i}(\tau,u)\,d\tau:
   instantaneous impact times the integrated future policy kernel.
   This is the standard Kyle channel—the trader internalizes how
   each demand impulse moves the price.
2. (ii)

   𝒱i,opp​(t,u)=∫tTδ​Pτind​Di​(τ,u)​𝑑τ\mathcal{V}^{i,\mathrm{opp}}(t,u)=\int\_{t}^{T}\delta P\_{\tau}^{\mathrm{ind}}\,D^{i}(\tau,u)\,d\tau:
   opponent-mediated impact, arising because opponents also observe
   order flow and adjust their trading, which feeds back into prices.

##### Back’s model.

When n=1n=1 and p1=0p\_{1}=0 (Back’s model), the opponent channel vanishes
(δ​Pτind≡0\delta P\_{\tau}^{\mathrm{ind}}\equiv 0) and ([5.3](#S5.E3 "In 5.2 Equilibrium characterization ‣ 5 Market microstructure as a special case ‣ Forecasting and Manipulating the Forecasts of Others")) reduces to
Back’s integral equation for the optimal trading rate.
With n≥2n\geq 2 and pi>0p\_{i}>0 both channels are active: each trader tempers
demand not only to limit direct price impact but to prevent opponents
from inferring and front-running through shared order flow.
Guess-and-verify cannot close this system; the noise-state technique
handles it with no additional machinery.

## 6 Conclusion

A single coordinate change—conditioning on primitive Brownian shocks—reduces Nash equilibrium in
continuous-time LQG games with endogenous signals to a deterministic
fixed point in two-time kernels, with no truncation and no
large-population limit.
The information wedge 𝒱ti\mathcal{V}^{i}\_{t}—with mean component 𝒱¯i​(t)\bar{\mathcal{V}}^{i}(t) and kernel component 𝒱i​(t,r)\mathcal{V}^{i}(t,r)—prices bilateral belief
manipulation and vanishes when signals are exogenous.
The two-player example shows that nearly all welfare gains from
mandatory disclosure come from eliminating this channel;
the Kyle–Back embedding shows the noise-state technique extends
beyond quadratic costs and identifies a second channel—opponent
inference through shared order flow—that applies immediately to
asymmetric precisions and continuous private learning.

##### Further directions.

The main open question is whether the deterministic-kernel class
is without loss of generality.
A natural program proceeds in three steps:
(i) a Blackwell reduction showing that under quadratic costs the
best response depends on the posterior
πti:=ℒ​(W[0,t]∣ℱti)\pi\_{t}^{i}:=\mathcal{L}(W\_{[0,t]}\mid\mathcal{F}\_{t}^{i}) only through its
mean and covariance;
(ii) a belief-of-belief collapse in which player ii’s estimate of
πtk\pi\_{t}^{k} factors through a deterministic operator—the posterior
analogue of the kernel maps (Fi,X~i)(F^{i},\widetilde{X}^{i});
(iii) a contraction argument on the variance functional
V​(𝐃):=∑i𝔼​∫∫‖Di​(t,s,πti)−𝔼​[Di​(t,s,πti)]‖2​𝑑s​𝑑tV(\mathbf{D}):=\sum\_{i}\mathbb{E}\int\!\!\int\|D^{i}(t,s,\pi\_{t}^{i})-\mathbb{E}[D^{i}(t,s,\pi\_{t}^{i})]\|^{2}\,ds\,dt,
which vanishes exactly in the deterministic-kernel class and which
iterated best responses are expected to contract.
Beyond this, stochastic coefficients
(Remark [C.2](#A3.Thmrem2 "Remark C.2 (Stochastic coefficients). ‣ C.5 Well-posedness ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")), graph-structured
interactions, and global uniqueness via the dissipative structure
of FiF^{i} are natural extensions.

## Appendix A Filtering

##### Roadmap.

Throughout, formal calculations identify the kernel equations for FiF^{i};
we then define FiF^{i} as the unique solution of those equations,
with uniqueness following from uniqueness of L2L^{2}-projection.
The pipeline proceeds in three steps.
[A.1](#A1.SS1 "A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others") derives the dynamics of
t↦W^ti​(u)t\mapsto\widehat{W}\_{t}^{i}(u) from a characterizing identity for
conditional expectations, using an ansatz with undetermined coefficients
matched against exponential test martingales.
[A.2](#A1.SS2 "A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others") specializes the abstract dynamics to the
physical observation model, identifying X~i​(t,u)\widetilde{X}^{i}(t,u) as the
filtering gain via Itô isometry, establishing the algebraic identity
X~i=X​(I−Πi)−X∗Fi\widetilde{X}^{i}=X(I-\Pi^{i})-X\*F^{i}, and recording the contraction
identity ∫0tX​(t,s)​X~i​(t,s)⊤​𝑑s=ΣX​Xi​(t)\int\_{0}^{t}X(t,s)\,\widetilde{X}^{i}(t,s)^{\top}\,ds=\Sigma\_{XX}^{i}(t).
[A.3](#A1.SS3 "A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others") defines FiF^{i} as the primitive filtering object
through its forward evolution equation, derives the explicit three-term
formula, and verifies uniqueness.

### A.1 Dynamics of the noise-state

Fix a player ii. Recall the noise-state
W^ti​(u):=𝔼​[Wu∣ℱti]\widehat{W}\_{t}^{i}(u):=\mathbb{E}[W\_{u}\mid\mathcal{F}\_{t}^{i}], 0≤u≤t0\leq u\leq t,
and the observation channel

|  |  |  |
| --- | --- | --- |
|  | d​Yti=(C¯​(t)+∫0tC​(t,s)​𝑑Ws)​d​t+Ei​d​Wt,Y0i=0,dY\_{t}^{i}=\Big(\bar{C}(t)+\int\_{0}^{t}C(t,s)\,dW\_{s}\Big)\,dt+E^{i}\,dW\_{t},\qquad Y\_{0}^{i}=0, |  |

where C​(t,s)C(t,s) is deterministic.
Since C¯\bar{C} is deterministic, we may assume without loss that C¯≡0\bar{C}\equiv 0
by replacing YtiY\_{t}^{i} with Yti−∫0tC¯​(r)​𝑑rY\_{t}^{i}-\int\_{0}^{t}\bar{C}(r)\,dr.

###### Proposition A.1 (Volterra closure for W^\widehat{W}).

The map u↦W^ti​(u)u\mapsto\widehat{W}\_{t}^{i}(u) is a Volterra process:
there exists a deterministic kernel Fti​(⋅,⋅)F\_{t}^{i}(\cdot,\cdot) such that

|  |  |  |
| --- | --- | --- |
|  | W^ti​(u)=Πi​Wu+∫0t∫0uFti​(z,s)​𝑑z​𝑑Ws,0≤u≤t.\widehat{W}\_{t}^{i}(u)=\Pi^{i}W\_{u}+\int\_{0}^{t}\!\int\_{0}^{u}F\_{t}^{i}(z,s)\,dz\,dW\_{s},\qquad 0\leq u\leq t. |  |

###### Proposition A.2 (Dynamics of W^ti​(u)\widehat{W}\_{t}^{i}(u)).

There exist deterministic matrix-valued functions BY​(u,t)B^{Y}(u,t) and B​(u;t,s)B(u;t,s)
such that, for each fixed uu,

|  |  |  |  |
| --- | --- | --- | --- |
|  | W^ti​(u)−W^t0i​(u)=∫t0t∫0rB​(u;r,s)​𝑑W^ri​(s)​𝑑r+∫t0tBY​(u,r)​𝑑Yri,t≥t0≥u,\widehat{W}\_{t}^{i}(u)-\widehat{W}\_{t\_{0}}^{i}(u)=\int\_{t\_{0}}^{t}\!\!\int\_{0}^{r}B(u;r,s)\,d\widehat{W}\_{r}^{i}(s)\,dr\;+\;\int\_{t\_{0}}^{t}B^{Y}(u,r)\,dY\_{r}^{i},\qquad t\geq t\_{0}\geq u, |  | (A.1) |

or equivalently in differential form,

|  |  |  |  |
| --- | --- | --- | --- |
|  | dt​W^ti​(u)=(∫0tB​(u;t,s)​𝑑W^ti​(s))​d​t+BY​(u,t)​d​Yti,d\_{t}\widehat{W}\_{t}^{i}(u)=\Big(\int\_{0}^{t}B(u;t,s)\,d\widehat{W}\_{t}^{i}(s)\Big)\,dt+B^{Y}(u,t)\,dY\_{t}^{i}, |  | (A.2) |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | BY​(u,t)\displaystyle B^{Y}(u,t) | =∫0t∂s𝖢ti​(u,s)​C​(t,s)⊤​d​s+Ei,⊤​𝟏{u≥t},\displaystyle=\int\_{0}^{t}\partial\_{s}\mathsf{C}\_{t}^{i}(u,s)\,C(t,s)^{\top}\,ds\;+\;E^{i,\top}\mathbf{1}\_{\{u\geq t\}}, |  | (A.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | B​(u;t,s)\displaystyle B(u;t,s) | =−BY​(u,t)​C​(t,s),\displaystyle=-B^{Y}(u,t)\,C(t,s), |  | (A.4) |

where 𝖢ti​(u,s):=Cov⁡(Wu,Ws∣ℱti)\mathsf{C}\_{t}^{i}(u,s):=\operatorname{Cov}(W\_{u},W\_{s}\mid\mathcal{F}\_{t}^{i}) is the deterministic
conditional error covariance kernel.

###### Proof.

We use the characterizing identity for conditional expectations via
exponential test martingales.
Fix a deterministic vector function r→​(⋅)\vec{r}(\cdot) and define
φtr\varphi\_{t}^{r} by φ0r=1\varphi\_{0}^{r}=1 and
d​φtr=i​φtr​(d​Yti)⊤​r→​(t)d\varphi\_{t}^{r}=i\,\varphi\_{t}^{r}\,(dY\_{t}^{i})^{\top}\vec{r}(t).
A necessary and sufficient condition characterizing W^ti​(u)\widehat{W}\_{t}^{i}(u) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[W^ti​(u)​φtr]=𝔼​[Wu​φtr]for all ​r→​(⋅).\mathbb{E}\!\big[\widehat{W}\_{t}^{i}(u)\,\varphi\_{t}^{r}\big]=\mathbb{E}\!\big[W\_{u}\,\varphi\_{t}^{r}\big]\qquad\text{for all }\vec{r}(\cdot). |  | (A.5) |

We compute the time derivative of each side independently, then match.

Left-hand side.
Apply Itô’s product rule to W^ti​(u)​φtr\widehat{W}\_{t}^{i}(u)\,\varphi\_{t}^{r}, using the
ansatz ([A.2](#A1.E2 "In Proposition A.2 (Dynamics of 𝑊̂_𝑡^𝑖⁢(𝑢)). ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) and
d​φtr=i​φtr​(d​Yti)⊤​r→​(t)d\varphi\_{t}^{r}=i\,\varphi\_{t}^{r}(dY\_{t}^{i})^{\top}\vec{r}(t):

|  |  |  |
| --- | --- | --- |
|  | d​(W^ti​(u)​φtr)=i​W^ti​(u)​φtr​(d​Yti)⊤​r→​(t)+φtr​dt​W^ti​(u)+d​⟨W^i​(u),φr⟩t.d\big(\widehat{W}\_{t}^{i}(u)\,\varphi\_{t}^{r}\big)=i\,\widehat{W}\_{t}^{i}(u)\,\varphi\_{t}^{r}\,(dY\_{t}^{i})^{\top}\vec{r}(t)+\varphi\_{t}^{r}\,d\_{t}\widehat{W}\_{t}^{i}(u)+d\langle\widehat{W}^{i}(u),\varphi^{r}\rangle\_{t}. |  |

The quadratic covariation contributes
d​⟨W^i​(u),φr⟩t=i​φtr​BY​(u,t)​r→​(t)​d​td\langle\widehat{W}^{i}(u),\varphi^{r}\rangle\_{t}=i\,\varphi\_{t}^{r}\,B^{Y}(u,t)\,\vec{r}(t)\,dt.
Taking expectations and collecting the d​tdt terms gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​𝔼​[W^ti​(u)​φtr]\displaystyle\frac{d}{dt}\mathbb{E}\!\big[\widehat{W}\_{t}^{i}(u)\,\varphi\_{t}^{r}\big] | =i​𝔼​[φtr​(W^ti​(u)​∫0tC​(t,s)​𝑑W^ti​(s)⊤+BY​(u,t))]​r→​(t)\displaystyle=i\,\mathbb{E}\!\bigg[\varphi\_{t}^{r}\Big(\widehat{W}\_{t}^{i}(u)\!\int\_{0}^{t}C(t,s)\,d\widehat{W}\_{t}^{i}(s)^{\top}+B^{Y}(u,t)\Big)\bigg]\vec{r}(t) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼​[φtr​∫0t(B​(u;t,s)+BY​(u,t)​C​(t,s))​𝑑W^ti​(s)].\displaystyle\quad+\mathbb{E}\!\bigg[\varphi\_{t}^{r}\int\_{0}^{t}\!\big(B(u;t,s)+B^{Y}(u,t)\,C(t,s)\big)\,d\widehat{W}\_{t}^{i}(s)\bigg]. |  | (A.6) |

Right-hand side.
Expand 𝔼​[Wu​φtr]\mathbb{E}[W\_{u}\,\varphi\_{t}^{r}] using the SDE for φr\varphi^{r} and apply the
tower property in the form
𝔼​[φsr​L]=𝔼​[φsr​𝔼​[L∣ℱsi]]\mathbb{E}[\varphi\_{s}^{r}\,L]=\mathbb{E}[\varphi\_{s}^{r}\,\mathbb{E}[L\mid\mathcal{F}\_{s}^{i}]].
Define the conditional second-moment kernel

|  |  |  |
| --- | --- | --- |
|  | ℳsi​(u,z):=𝔼​[Wu​Wz⊤∣ℱsi]=𝖢si​(u,z)+W^si​(u)​W^si​(z)⊤.\mathcal{M}\_{s}^{i}(u,z):=\mathbb{E}[W\_{u}W\_{z}^{\top}\mid\mathcal{F}\_{s}^{i}]=\mathsf{C}\_{s}^{i}(u,z)+\widehat{W}\_{s}^{i}(u)\,\widehat{W}\_{s}^{i}(z)^{\top}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Wu​∫0sC​(s,z)​𝑑Wz⊤|ℱsi]=∫0s∂zℳsi​(u,z)​C​(s,z)⊤​d​z.\mathbb{E}\!\Big[W\_{u}\!\int\_{0}^{s}C(s,z)\,dW\_{z}^{\top}\;\Big|\;\mathcal{F}\_{s}^{i}\Big]=\int\_{0}^{s}\partial\_{z}\mathcal{M}\_{s}^{i}(u,z)\,C(s,z)^{\top}\,dz. |  |

Splitting ℳsi=𝖢si+W^si​W^si,⊤\mathcal{M}\_{s}^{i}=\mathsf{C}\_{s}^{i}+\widehat{W}\_{s}^{i}\,\widehat{W}\_{s}^{i,\top} separates
this into a covariance piece and a product-of-means piece:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0s∂zℳsi​(u,z)​C​(s,z)⊤​d​z=∫0s∂z𝖢si​(u,z)​C​(s,z)⊤​d​z+W^si​(u)​∫0sC​(s,z)​𝑑W^si​(z)⊤.\int\_{0}^{s}\partial\_{z}\mathcal{M}\_{s}^{i}(u,z)\,C(s,z)^{\top}\,dz=\int\_{0}^{s}\partial\_{z}\mathsf{C}\_{s}^{i}(u,z)\,C(s,z)^{\top}\,dz\;+\;\widehat{W}\_{s}^{i}(u)\!\int\_{0}^{s}C(s,z)\,d\widehat{W}\_{s}^{i}(z)^{\top}. |  | (A.7) |

Differentiating 𝔼​[Wu​φtr]\mathbb{E}[W\_{u}\,\varphi\_{t}^{r}] and collecting d​tdt terms then gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​𝔼​[Wu​φtr]\displaystyle\frac{d}{dt}\mathbb{E}\!\big[W\_{u}\,\varphi\_{t}^{r}\big] | =i​𝔼​[φtr​(∫0t∂s𝖢ti​(u,s)​C​(t,s)⊤​d​s+W^ti​(u)​∫0tC​(t,s)​𝑑W^ti​(s)⊤+Ei,⊤​𝟏{u≥t})]​r→​(t).\displaystyle=i\,\mathbb{E}\!\bigg[\varphi\_{t}^{r}\Big(\int\_{0}^{t}\partial\_{s}\mathsf{C}\_{t}^{i}(u,s)\,C(t,s)^{\top}\,ds\;+\;\widehat{W}\_{t}^{i}(u)\!\int\_{0}^{t}C(t,s)\,d\widehat{W}\_{t}^{i}(s)^{\top}\;+\;E^{i,\top}\mathbf{1}\_{\{u\geq t\}}\Big)\bigg]\vec{r}(t). |  | (A.8) |

Coefficient matching.
Equating ([A.6](#A1.E6 "In Proof. ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) and ([A.8](#A1.E8 "In Proof. ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) for all
r→​(⋅)\vec{r}(\cdot) and all tt yields two conditions.
Matching the terms multiplying r→​(t)\vec{r}(t) (after canceling the common
W^ti​(u)​∫C​𝑑W^i,⊤\widehat{W}\_{t}^{i}(u)\int C\,d\widehat{W}^{i,\top} terms that appear on both
sides via ([A.7](#A1.E7 "In Proof. ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))) gives ([A.3](#A1.E3 "In Proposition A.2 (Dynamics of 𝑊̂_𝑡^𝑖⁢(𝑢)). ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).
Requiring the residual drift in ([A.6](#A1.E6 "In Proof. ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) to vanish gives

|  |  |  |
| --- | --- | --- |
|  | ∫0t(B​(u;t,s)+BY​(u,t)​C​(t,s))​𝑑W^ti​(s)=0,\int\_{0}^{t}\big(B(u;t,s)+B^{Y}(u,t)\,C(t,s)\big)\,d\widehat{W}\_{t}^{i}(s)=0, |  |

hence B​(u;t,s)=−BY​(u,t)​C​(t,s)B(u;t,s)=-B^{Y}(u,t)\,C(t,s), which is ([A.4](#A1.E4 "In Proposition A.2 (Dynamics of 𝑊̂_𝑡^𝑖⁢(𝑢)). ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).
∎

### A.2 Specialization to the physical observation model

We now specialize to the observation equation of Section [2](#S2 "2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others"),

|  |  |  |
| --- | --- | --- |
|  | d​Yti=Pi​(t)​Xt​d​t+Ei​d​Wt,dY\_{t}^{i}=\sqrt{P^{i}(t)}\,X\_{t}\,dt+E^{i}\,dW\_{t}, |  |

which corresponds to setting C​(t,s)=Pi​(t)​X​(t,s)C(t,s)=\sqrt{P^{i}(t)}\,X(t,s) in the
general framework of Proposition [A.2](#A1.Thmthm2 "Proposition A.2 (Dynamics of 𝑊̂_𝑡^𝑖⁢(𝑢)). ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others").

##### Innovation process.

Define the innovation

|  |  |  |
| --- | --- | --- |
|  | d​Iti:=d​Yti−Pi​(t)​X^ti​d​t,dI\_{t}^{i}:=dY\_{t}^{i}-\sqrt{P^{i}(t)}\,\widehat{X}\_{t}^{i}\,dt, |  |

where X^ti:=𝔼​[Xt∣ℱti]\widehat{X}\_{t}^{i}:=\mathbb{E}[X\_{t}\mid\mathcal{F}\_{t}^{i}].
By the innovations theorem for Gaussian linear filtering
(Liptser–Shiryaev [[16](#bib.bib16)], Theorem 7.12),
IiI^{i} is a standard (ℱi,ℙ)(\mathcal{F}^{i},\mathbb{P})-Brownian motion.

##### Innovation form of the dynamics.

Substituting C​(t,s)=Pi​(t)​X​(t,s)C(t,s)=\sqrt{P^{i}(t)}\,X(t,s) into
Proposition [A.2](#A1.Thmthm2 "Proposition A.2 (Dynamics of 𝑊̂_𝑡^𝑖⁢(𝑢)). ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others") and using
d​Iti=d​Yti−Pi​(t)​X^ti​d​tdI\_{t}^{i}=dY\_{t}^{i}-\sqrt{P^{i}(t)}\,\widehat{X}\_{t}^{i}\,dt,
the dynamics ([A.2](#A1.E2 "In Proposition A.2 (Dynamics of 𝑊̂_𝑡^𝑖⁢(𝑢)). ‣ A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) become

|  |  |  |  |
| --- | --- | --- | --- |
|  | dt​W^ti​(u)=(∫0t∂s𝖢ti​(u,s)​X​(t,s)⊤​d​s)​Pi​(t)​d​Iti+Ei,⊤​𝟏{u≥t}​d​Iti.d\_{t}\widehat{W}\_{t}^{i}(u)=\Big(\int\_{0}^{t}\partial\_{s}\mathsf{C}\_{t}^{i}(u,s)\,X(t,s)^{\top}\,ds\Big)\sqrt{P^{i}(t)}\,dI\_{t}^{i}\,+\;E^{i,\top}\mathbf{1}\_{\{u\geq t\}}\,dI\_{t}^{i}. |  | (A.9) |

##### Identifying X~i\widetilde{X}^{i} as the filtering gain.

For u<tu<t, the indicator term in ([A.9](#A1.E9 "In Innovation form of the dynamics. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) is locally
constant in uu, so the mixed (t,u)(t,u)-update takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | dt​(du​W^ti​(u))=X~i​(t,u)⊤​Pi​(t)​d​Iti​d​u,0≤u<t≤T.d\_{t}\!\bigl(d\_{u}\widehat{W}\_{t}^{i}(u)\bigr)=\widetilde{X}^{i}(t,u)^{\top}\sqrt{P^{i}(t)}\,dI\_{t}^{i}\,du,\qquad 0\leq u<t\leq T. |  | (A.10) |

To verify the gain coefficient, recall that
Xt−X^ti=∫0tX~i​(t,s)​𝑑WsX\_{t}-\widehat{X}\_{t}^{i}=\int\_{0}^{t}\widetilde{X}^{i}(t,s)\,dW\_{s}
and that the innovation ([A.17](#A1.E17 "In Expanding the innovation. ‣ A.3.1 Derivation ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) has martingale component
Ei​d​WtE^{i}\,dW\_{t} and absolutely continuous component
Pi​(t)​∫0tX~i​(t,s)​𝑑Ws​𝑑t\sqrt{P^{i}(t)}\int\_{0}^{t}\widetilde{X}^{i}(t,s)\,dW\_{s}\,dt.
The gain in ([A.10](#A1.E10 "In Identifying 𝑋̃^𝑖 as the filtering gain. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) equals the conditional
cross-covariance density Cov⁡(d​Wu,Pi​(t)​(Xt−X^ti)​d​t∣ℱti)/d​t\operatorname{Cov}(dW\_{u},\,\sqrt{P^{i}(t)}(X\_{t}{-}\widehat{X}\_{t}^{i})\,dt\mid\mathcal{F}\_{t}^{i})/dt;
by Itô isometry applied to ∫0tX~i​(t,s)​𝑑Ws\int\_{0}^{t}\widetilde{X}^{i}(t,s)\,dW\_{s}, this picks
out X~i​(t,u)\widetilde{X}^{i}(t,u).
Thus X~i​(t,u)⊤​Pi​(t)\widetilde{X}^{i}(t,u)^{\top}\sqrt{P^{i}(t)} is the Kalman gain for updating the
uu-th noise increment: it maps observation innovations at time tt into
revisions of the noise estimate at the earlier time uu.

###### Remark A.1 (Conditional cross-covariance interpretation).

The identification above can be restated as

|  |  |  |
| --- | --- | --- |
|  | X~i​(t,u)=Cov⁡(Xt,d​Wu∣ℱti)d​u.\widetilde{X}^{i}(t,u)\;=\;\frac{\operatorname{Cov}\!\big(X\_{t},\,dW\_{u}\mid\mathcal{F}\_{t}^{i}\big)}{du}. |  |

Integrating in uu recovers the full conditional cross-covariance

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov⁡(Xt,Wu∣ℱti)=∫0uX~i​(t,s)​𝑑s=∫0tX​(t,s)​∂s𝖢ti​(s,u)​d​s,\operatorname{Cov}\!\big(X\_{t},\,W\_{u}\mid\mathcal{F}\_{t}^{i}\big)\;=\;\int\_{0}^{u}\widetilde{X}^{i}(t,s)\,ds\;=\;\int\_{0}^{t}X(t,s)\,\partial\_{s}\mathsf{C}\_{t}^{i}(s,u)\,ds, |  | (A.11) |

where the second equality follows from
Xt−X^ti=∫0tX​(t,s)​𝑑W~ti​(s)X\_{t}-\widehat{X}\_{t}^{i}=\int\_{0}^{t}X(t,s)\,d\widetilde{W}\_{t}^{i}(s)
and Itô isometry against W~ti​(u)\widetilde{W}\_{t}^{i}(u).

##### Algebraic identity for X~i\widetilde{X}^{i} in terms of FiF^{i}.

Recall the induced estimated-state kernel
X^i​(t,s):=X​(t,s)​Πi+∫0tX​(t,z)​Fti​(z,s)​𝑑z\widehat{X}^{\,i}(t,s):=X(t,s)\Pi^{i}+\int\_{0}^{t}X(t,z)\,F\_{t}^{i}(z,s)\,dz.
Since X~i​(t,u):=X​(t,u)−X^i​(t,u)\widetilde{X}^{i}(t,u):=X(t,u)-\widehat{X}^{\,i}(t,u),

|  |  |  |  |
| --- | --- | --- | --- |
|  | X~i​(t,u)=X​(t,u)​(I−Πi)−∫0tX​(t,z)​Fti​(z,u)​𝑑z.\widetilde{X}^{i}(t,u)=X(t,u)(I-\Pi^{i})-\int\_{0}^{t}X(t,z)\,F\_{t}^{i}(z,u)\,dz. |  | (A.12) |

This identity is algebraic: once FiF^{i} is determined
(Section [A.3](#A1.SS3 "A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")), X~i\widetilde{X}^{i} follows with
no further fixed-point step.

###### Remark A.2 (State uncertainty as a contraction).

The conditional state covariance satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣX​Xi​(t)=∫0tX​(t,s)​X~i​(t,s)⊤​𝑑s,\Sigma\_{XX}^{i}(t)=\int\_{0}^{t}X(t,s)\,\widetilde{X}^{i}(t,s)^{\top}\,ds, |  | (A.13) |

which follows from Itô isometry applied to
Xt−X^ti=∫0tX~i​(t,s)​𝑑WsX\_{t}-\widehat{X}\_{t}^{i}=\int\_{0}^{t}\widetilde{X}^{i}(t,s)\,dW\_{s}.

###### Remark A.3 (Kalman-filter interpretation).

Identity ([A.13](#A1.E13 "In Remark A.2 (State uncertainty as a contraction). ‣ Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) says that the
d×dd\times d state uncertainty ΣX​Xi​(t)\Sigma\_{XX}^{i}(t) is obtained by
“projecting” the unresolved kernel X~i​(t,s)\widetilde{X}^{i}(t,s) back through the
state impulse response X​(t,s)X(t,s).
In the single-player case with no endogenous drift, this reduces to
the classical relation between the Kalman gain and the error covariance.
In the multi-player setting the identity persists because the forward
kernel environment is deterministic.

### A.3 The filtering kernel FiF^{i}

We define FiF^{i} as the primitive filtering object through its
evolution equation. The unresolved kernel X~i\widetilde{X}^{i} is then
a derived quantity via the algebraic
identity ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).

###### Definition A.1 (Filtering kernel system).

Fix player ii. A deterministic causal kernel FiF^{i} on ΔT\Delta\_{T}
solves the *filtering kernel system* if, with X~i\widetilde{X}^{i}
defined by ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")), it satisfies F0i=0F\_{0}^{i}=0 and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tFti​(u,s)\displaystyle\partial\_{t}F\_{t}^{i}(u,s) | =X~i​(t,u)⊤​Pi​(t)​X~i​(t,s),u,s<t,\displaystyle=\widetilde{X}^{i}(t,u)^{\top}P^{i}(t)\,\widetilde{X}^{i}(t,s),\qquad u,s<t, |  | (A.14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Fti​(u,t)\displaystyle F\_{t}^{i}(u,t) | =X~i​(t,u)⊤​Pi​(t)​Ei,Fti​(t,u)=Ei,⊤​Pi​(t)​X~i​(t,u).\displaystyle=\widetilde{X}^{i}(t,u)^{\top}\sqrt{P^{i}(t)}\,E^{i},\qquad F\_{t}^{i}(t,u)=E^{i,\top}\sqrt{P^{i}(t)}\,\widetilde{X}^{i}(t,u). |  | (A.15) |

Since ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) expresses X~i\widetilde{X}^{i} as a
deterministic linear functional of FiF^{i},
the system ([A.14](#A1.E14 "In Definition A.1 (Filtering kernel system). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))–([A.15](#A1.E15 "In Definition A.1 (Filtering kernel system). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) is a
closed forward ODE for FiF^{i} (quadratic through the substitution).

###### Proposition A.3 (Explicit formula).

Integrating ([A.14](#A1.E14 "In Definition A.1 (Filtering kernel system). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) from max⁡(u,s)\max(u,s) to tt and
adding the boundary contributions gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fti​(u,s)=X~i​(s,u)⊤​Pi​(s)​Ei+Ei,⊤​Pi​(u)​X~i​(u,s)+∫max⁡(u,s)tX~i​(r,u)⊤​Pi​(r)​X~i​(r,s)​𝑑r.F\_{t}^{i}(u,s)=\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,E^{i}\;+\;E^{i,\top}\sqrt{P^{i}(u)}\,\widetilde{X}^{i}(u,s)\;+\;\int\_{\max(u,s)}^{t}\widetilde{X}^{i}(r,u)^{\top}P^{i}(r)\,\widetilde{X}^{i}(r,s)\,dr. |  | (A.16) |

The three terms are: (i) the unresolved response at observation
time ss, projected through the observation channel;
(ii) the drift component of the innovation at time uu, revealing
information about earlier increments at s≤us\leq u;
(iii) accumulated indirect inference from observations at times
r∈[max⁡(u,s),t]r\in[\max(u,s),\,t].

###### Remark A.4 (Self-adjointness).

Under (u,s)↦(s,u)(u,s)\mapsto(s,u) with transpose, the first two terms
in ([A.16](#A1.E16 "In Proposition A.3 (Explicit formula). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) exchange and the integral is
invariant (since Pi​(r)P^{i}(r) is symmetric).
Hence Fti​(u,s)=Fti​(s,u)⊤F\_{t}^{i}(u,s)=F\_{t}^{i}(s,u)^{\top}, confirming that the
induced map is an orthogonal projection.

###### Remark A.5 (Uniqueness).

If FiF^{i} and F~i\tilde{F}^{i} both yield the density representation
of Theorem [3.1](#S3.Thmthm1 "Theorem 3.1 (Volterra Filtering Closure). ‣ Filtering closure. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")(i),
Itô isometry gives Fti​(u,s)=F~ti​(u,s)F\_{t}^{i}(u,s)=\tilde{F}\_{t}^{i}(u,s) a.e.

###### Remark A.6 (Computation).

In the numerical scheme of
Section [4](#S4 "4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others"),
X~i\widetilde{X}^{i} is computed from FiF^{i}
via ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) at each time step, and the
integral in ([A.16](#A1.E16 "In Proposition A.3 (Explicit formula). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) is accumulated forward
alongside the FiF^{i} update.

We now convert the innovations-based characterization of
Subsections [A.1](#A1.SS1 "A.1 Dynamics of the noise-state ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")–[A.2](#A1.SS2 "A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")
into primitive-noise coordinates.
The goal is to construct the deterministic kernel FiF^{i} such that
for every t∈[0,T]t\in[0,T] and u<tu<t,

|  |  |  |
| --- | --- | --- |
|  | du​W^ti​(u)=Πi​d​Wu+(∫0tFti​(u,s)​𝑑Ws)​d​u.d\_{u}\widehat{W}\_{t}^{i}(u)=\Pi^{i}\,dW\_{u}+\Bigg(\int\_{0}^{t}F\_{t}^{i}(u,s)\,dW\_{s}\Bigg)\,du. |  |

#### A.3.1 Derivation

Recall the innovation form of the estimated-noise dynamics
(equation ([A.9](#A1.E9 "In Innovation form of the dynamics. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))):
for u≤tu\leq t,

|  |  |  |
| --- | --- | --- |
|  | du​W^ti​(u)=Ei,⊤​d​Iui+(∫utX~i​(s,u)⊤​Pi​(s)​𝑑Isi)​d​u,d\_{u}\widehat{W}\_{t}^{i}(u)=E^{i,\top}\,dI\_{u}^{i}+\Bigg(\int\_{u}^{t}\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,dI\_{s}^{i}\Bigg)\,du, |  |

where the first term is the direct observation at time uu and the
second is the accumulated drift-based revision over (u,t](u,t].
To pass from innovations to primitive noise, we expand each d​IsidI\_{s}^{i}
in terms of d​WdW.

##### Expanding the innovation.

The physical-measure decomposition of the innovation is

|  |  |  |
| --- | --- | --- |
|  | d​Iti=Ei​d​Wt+Pi​(t)​(Xt−X^ti)​d​t.dI\_{t}^{i}=E^{i}\,dW\_{t}\;+\;\sqrt{P^{i}(t)}\,(X\_{t}-\widehat{X}\_{t}^{i})\,dt. |  |

The first piece is the martingale component;
the second is absolutely continuous.
Substituting the Volterra forms and using
X~i​(t,r):=X​(t,r)−X^i​(t,r)\widetilde{X}^{i}(t,r):=X(t,r)-\widehat{X}^{\,i}(t,r)
(the definition of X~i\widetilde{X}^{i}
and ([A.13](#A1.E13 "In Remark A.2 (State uncertainty as a contraction). ‣ Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Iti=Ei​d​Wt+Pi​(t)​∫0tX~i​(t,r)​𝑑Wr​𝑑t.dI\_{t}^{i}=E^{i}\,dW\_{t}+\sqrt{P^{i}(t)}\int\_{0}^{t}\widetilde{X}^{i}(t,r)\,dW\_{r}\,dt. |  | (A.17) |

##### Expanding the direct term.

Substituting ([A.17](#A1.E17 "In Expanding the innovation. ‣ A.3.1 Derivation ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) at t=ut=u into
Ei,⊤​d​IuiE^{i,\top}\,dI\_{u}^{i}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ei,⊤​d​Iui\displaystyle E^{i,\top}\,dI\_{u}^{i} | =Ei,⊤​Ei​d​Wu⏟=Πi​d​Wu+Ei,⊤​Pi​(u)​∫0uX~i​(u,r)​𝑑Wr​𝑑u.\displaystyle=\underbrace{E^{i,\top}E^{i}\,dW\_{u}}\_{=\;\Pi^{i}\,dW\_{u}}\;+\;E^{i,\top}\sqrt{P^{i}(u)}\int\_{0}^{u}\widetilde{X}^{i}(u,r)\,dW\_{r}\,du. |  | (A.18) |

The first piece contributes the Πi​d​Wu\Pi^{i}\,dW\_{u} in the density
representation.
The second is absolutely continuous in uu with primitive-noise density
Ei,⊤​Pi​(u)​X~i​(u,s)E^{i,\top}\sqrt{P^{i}(u)}\,\widetilde{X}^{i}(u,s) at source-noise index s≤us\leq u.

##### Expanding the integral term.

Substituting ([A.17](#A1.E17 "In Expanding the innovation. ‣ A.3.1 Derivation ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) into
∫utX~i​(s,u)⊤​Pi​(s)​𝑑Isi\int\_{u}^{t}\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,dI\_{s}^{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫utX~i​(s,u)⊤​Pi​(s)​𝑑Isi\displaystyle\int\_{u}^{t}\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,dI\_{s}^{i} | =∫utX~i​(s,u)⊤​Pi​(s)​Ei​𝑑Ws⏟(a) martingale\displaystyle=\underbrace{\int\_{u}^{t}\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,E^{i}\,dW\_{s}}\_{\text{(a) martingale}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫utX~i​(s,u)⊤​Pi​(s)​∫0sX~i​(s,r)​𝑑Wr​𝑑s⏟(b) abs. continuous.\displaystyle\quad+\;\underbrace{\int\_{u}^{t}\widetilde{X}^{i}(s,u)^{\top}P^{i}(s)\int\_{0}^{s}\widetilde{X}^{i}(s,r)\,dW\_{r}\,ds}\_{\text{(b) abs.\ continuous}}. |  |

Term (a) contributes X~i​(s,u)⊤​Pi​(s)​Ei\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,E^{i} at
source-noise index s∈(u,t]s\in(u,t].
Applying stochastic Fubini to term (b) and reading off the
coefficient of d​WrdW\_{r}:

|  |  |  |
| --- | --- | --- |
|  | (b)=∫0t(∫max⁡(u,r)tX~i​(s,u)⊤​Pi​(s)​X~i​(s,r)​𝑑s)​𝑑Wr.\text{(b)}=\int\_{0}^{t}\Bigg(\int\_{\max(u,r)}^{t}\widetilde{X}^{i}(s,u)^{\top}P^{i}(s)\,\widetilde{X}^{i}(s,r)\,ds\Bigg)\,dW\_{r}. |  |

##### Assembling the density.

Collecting the coefficient of d​Ws​d​udW\_{s}\,du from all three
contributions and noting that causality (X~i​(s,u)=0\widetilde{X}^{i}(s,u)=0 for u>su>s)
automatically zeroes the irrelevant indicators:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fti​(u,s)=X~i​(s,u)⊤​Pi​(s)​Ei+Ei,⊤​Pi​(u)​X~i​(u,s)+∫max⁡(u,s)tX~i​(r,u)⊤​Pi​(r)​X~i​(r,s)​𝑑r.F\_{t}^{i}(u,s)=\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,E^{i}\;+\;E^{i,\top}\sqrt{P^{i}(u)}\,\widetilde{X}^{i}(u,s)\;+\;\int\_{\max(u,s)}^{t}\widetilde{X}^{i}(r,u)^{\top}P^{i}(r)\,\widetilde{X}^{i}(r,s)\,dr. |  | (A.19) |

The three terms admit a direct interpretation:

* •

  X~i​(s,u)⊤​Pi​(s)​Ei\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,E^{i}:
  the unresolved response at observation time ss, projected through the
  observation channel.
  Nonzero only when u≤su\leq s (causal in the observation direction).
* •

  Ei,⊤​Pi​(u)​X~i​(u,s)E^{i,\top}\sqrt{P^{i}(u)}\,\widetilde{X}^{i}(u,s):
  the drift component of the innovation at time uu, which
  reveals information about earlier noise increments at index s≤us\leq u.
  Nonzero only when s≤us\leq u (causal in the noise direction).
* •

  ∫max⁡(u,s)tX~i​(r,u)⊤​Pi​(r)​X~i​(r,s)​𝑑r\int\_{\max(u,s)}^{t}\widetilde{X}^{i}(r,u)^{\top}P^{i}(r)\,\widetilde{X}^{i}(r,s)\,dr:
  accumulated indirect inference—the joint information about
  the uu-th and ss-th increments extracted from observations
  at times r∈[max⁡(u,s),t]r\in[\max(u,s),\,t].

###### Remark A.7 (Self-adjointness and uniqueness).

Under (u,s)↦(s,u)(u,s)\mapsto(s,u) with transpose, the first two terms
exchange and the integral is invariant (since Pi​(r)P^{i}(r) is symmetric).
Hence Fti​(u,s)=Fti​(s,u)⊤F\_{t}^{i}(u,s)=F\_{t}^{i}(s,u)^{\top}, confirming that the
induced map
(𝒫ti​f)​(s):=Πi​f​(s)+∫0tFti​(r,s)⊤​f​(r)​𝑑r(\mathcal{P}\_{t}^{i}f)(s):=\Pi^{i}f(s)+\int\_{0}^{t}F\_{t}^{i}(r,s)^{\top}f(r)\,dr
is self-adjoint, as required by its interpretation as an orthogonal
projection.
Uniqueness follows from Itô isometry: if F~\tilde{F} also
satisfies the density representation, then
∫0t‖Fti​(u,s)−F~ti​(u,s)‖2​𝑑s=0\int\_{0}^{t}\|F\_{t}^{i}(u,s)-\tilde{F}\_{t}^{i}(u,s)\|^{2}\,ds=0 a.e.

###### Remark A.8 (Boundary condition and evolution).

Evaluating ([A.19](#A1.E19 "In Assembling the density. ‣ A.3.1 Derivation ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) at s=ts=t (using X~i​(u,t)=0\widetilde{X}^{i}(u,t)=0 for u<tu<t):

|  |  |  |
| --- | --- | --- |
|  | Fti​(u,t)=X~i​(t,u)⊤​Pi​(t)​Ei,Fti​(t,u)=Ei,⊤​Pi​(t)​X~i​(t,u),F\_{t}^{i}(u,t)=\widetilde{X}^{i}(t,u)^{\top}\sqrt{P^{i}(t)}\,E^{i},\qquad F\_{t}^{i}(t,u)=E^{i,\top}\sqrt{P^{i}(t)}\,\widetilde{X}^{i}(t,u), |  |

which are each other’s transposes.
Differentiating ([A.19](#A1.E19 "In Assembling the density. ‣ A.3.1 Derivation ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) in tt at fixed u,s<tu,s<t
gives the evolution

|  |  |  |
| --- | --- | --- |
|  | ∂tFti​(u,s)=X~i​(t,u)⊤​Pi​(t)​X~i​(t,s),\partial\_{t}F\_{t}^{i}(u,s)=\widetilde{X}^{i}(t,u)^{\top}P^{i}(t)\,\widetilde{X}^{i}(t,s), |  |

which is manifestly self-adjoint under (u,s)↦(s,u)⊤(u,s)\mapsto(s,u)^{\top}.

###### Remark A.9 (Computational simplification).

The formula ([A.19](#A1.E19 "In Assembling the density. ‣ A.3.1 Derivation ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")) is explicit in the gain
kernel X~i\widetilde{X}^{i}: once X~i\widetilde{X}^{i} is computed from ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")), the filtering kernel FiF^{i} requires
no further fixed-point iteration.
In the numerical scheme of
Section [4](#S4 "4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others"), the integral
∫max⁡(u,s)tX~i​(r,u)⊤​Pi​(r)​X~i​(r,s)​𝑑r\int\_{\max(u,s)}^{t}\widetilde{X}^{i}(r,u)^{\top}P^{i}(r)\,\widetilde{X}^{i}(r,s)\,dr
is accumulated forward alongside the X~i\widetilde{X}^{i}-computation, and the
two boundary terms are set at each new observation time.

#### A.3.2 Formal characterization

###### Definition A.2 (Filtering kernel system (definition of FiF^{i})).

Fix player ii. The inputs are the state kernel X​(⋅,⋅)X(\cdot,\cdot) and
the unresolved kernel X~i\widetilde{X}^{i} from Subsection [A.2](#A1.SS2 "A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others").
The output is the primitive-noise density kernel FiF^{i} of
Theorem [3.1](#S3.Thmthm1 "Theorem 3.1 (Volterra Filtering Closure). ‣ Filtering closure. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")(i).

A deterministic kernel FiF^{i} is said to be admissible if it is causal
(Fti​(u,s)=0F\_{t}^{i}(u,s)=0 when max⁡{u,s}>t\max\{u,s\}>t) and, together with the induced
kernel

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fti​(u,s)=X~i​(s,u)⊤​Pi​(s)​Ei+Ei,⊤​Pi​(u)​X~i​(u,s)+∫max⁡(u,s)tX~i​(r,u)⊤​Pi​(r)​X~i​(r,s)​𝑑r,u,s≤t.\begin{split}F\_{t}^{i}(u,s)&=\widetilde{X}^{i}(s,u)^{\top}\sqrt{P^{i}(s)}\,E^{i}\;+\;E^{i,\top}\sqrt{P^{i}(u)}\,\widetilde{X}^{i}(u,s)\\ &\quad+\;\int\_{\max(u,s)}^{t}\widetilde{X}^{i}(r,u)^{\top}P^{i}(r)\,\widetilde{X}^{i}(r,s)\,dr,\qquad u,s\leq t.\end{split} |  | (A.20) |

We define FiF^{i} to be the unique causal solution of
([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))–([A.20](#A1.E20 "In Definition A.2 (Filtering kernel system (definition of 𝐹^𝑖)). ‣ A.3.2 Formal characterization ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).

###### Proposition A.4 (Verification: primitive-noise density of the noise-state).

Let FiF^{i} be the kernel defined by
Definition [A.1](#A1.Thmdefn1 "Definition A.1 (Filtering kernel system). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others").
Then for every t∈[0,T]t\in[0,T] and u<tu<t,

|  |  |  |
| --- | --- | --- |
|  | du​W^ti​(u)=Πi​d​Wu+(∫0tFti​(u,s)​𝑑Ws)​d​u.d\_{u}\widehat{W}\_{t}^{i}(u)=\Pi^{i}\,dW\_{u}+\Bigg(\int\_{0}^{t}F\_{t}^{i}(u,s)\,dW\_{s}\Bigg)\,du. |  |

Moreover, FiF^{i} is unique among deterministic causal kernels with this
property.

###### Proof of uniqueness.

If FiF^{i} and F~i\tilde{F}^{i} both satisfy the density representation, then
∫0t(Fti​(u,s)−F~ti​(u,s))​𝑑Ws=0\int\_{0}^{t}(F\_{t}^{i}(u,s)-\tilde{F}\_{t}^{i}(u,s))\,dW\_{s}=0 a.s. for each (t,u)(t,u).
By Itô isometry, ∫0t‖Fti​(u,s)−F~ti​(u,s)‖2​𝑑s=0\int\_{0}^{t}\|F\_{t}^{i}(u,s)-\tilde{F}\_{t}^{i}(u,s)\|^{2}\,ds=0,
hence Fti​(u,s)=F~ti​(u,s)F\_{t}^{i}(u,s)=\tilde{F}\_{t}^{i}(u,s) a.e.
∎

## Appendix B Control First Order Conditions

This appendix derives the stationarity condition
([B.8](#A2.E8 "In Stationarity condition (globally necessary and sufficient). ‣ B.4 First variation of costs and the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) and the closed backward system for the
adjoint kernels (H¯X,HX,{H¯k,Hk}k≠i)(\bar{H}^{X},H^{X},\{\bar{H}^{k},H^{k}\}\_{k\neq i}).
By the innovations exogeneity established in Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others"), the best-response problem for player ii (opponents’ maps fixed) is an optimization over deterministic kernels weighting the exogenous innovation IiI^{i}.222To avoid circularity: opponents’ deterministic kernels make IiI^{i} a standard Brownian motion independent of DiD^{i} [[16](#bib.bib16), Theorem 7.12]; Lemma [3.4](#S3.Thmthm4 "Lemma 3.4 (Why the maximum-principle stationarity condition is global here). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") then gives strict convexity over the full L2L^{2} class; the FOC derived here is therefore necessary and sufficient, yielding the deterministic-kernel best response of Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others").

### B.1 The best-response problem in innovations coordinates

Fix a baseline deterministic-kernel Volterra profile and a deviating
player ii.
By the innovations exogeneity established in Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others"), W^ti​(⋅)\widehat{W}\_{t}^{i}(\cdot) is a deterministic linear functional of I[0,t]iI^{i}\_{[0,t]}, and IiI^{i} is a standard (ℱi,ℙ)(\mathcal{F}^{i},\mathbb{P})-Brownian motion invariant to DiD^{i}.
Player ii’s control

|  |  |  |
| --- | --- | --- |
|  | Dti=D¯i​(t)+∫0tDi​(t,u)​du​W^ti​(u)D\_{t}^{i}=\bar{D}^{i}(t)+\int\_{0}^{t}D^{i}(t,u)\,d\_{u}\widehat{W}\_{t}^{i}(u) |  |

is a deterministic affine functional of IiI^{i}, and the
optimization is over (D¯i,Di)(\bar{D}^{i},D^{i}) with no self-referential
signal dependence.
Since the state dynamics are linear in DiD^{i} and the cost is quadratic
with GD​Di​(t)≻0G^{i}\_{DD}(t)\succ 0, the induced objective is strictly convex:
the stationarity condition derived below is the unique global optimum.

### B.2 Spike variation and the first-variation system

We use spike variations to expose the adjoint structure.
Fix t∈[0,T)t\in[0,T) and v∈L2​(Ω,ℱti;ℝd)v\in L^{2}(\Omega,\mathcal{F}\_{t}^{i};\mathbb{R}^{d}).
The spike perturbation
Dsi,ρ,ε:=Dsi+ρ​v​ 1[t,t+ε]​(s)D\_{s}^{i,\rho,\varepsilon}:=D\_{s}^{i}+\rho\,v\,\mathbf{1}\_{[t,t+\varepsilon]}(s)
induces the normalized first variation
δ​Xs:=limε↓01ε​∂∂ρ​Xsρ,ε|ρ=0\delta X\_{s}:=\lim\_{\varepsilon\downarrow 0}\frac{1}{\varepsilon}\frac{\partial}{\partial\rho}X\_{s}^{\rho,\varepsilon}\big|\_{\rho=0}
with δ​Xt=v\delta X\_{t}=v.

Because opponents apply fixed linear maps with deterministic kernels,
the map v↦(δ​Xs,{δ​wsk​(⋅)}k≠i)v\mapsto(\delta X\_{s},\{\delta w\_{s}^{k}(\cdot)\}\_{k\neq i})
is *exactly* linear in vv with deterministic coefficients—not
a linearization but the full response.
The deviator’s own innovation is unaffected (δ​Isi=0\delta I\_{s}^{i}=0),
since δ​Xs∈ℱti\delta X\_{s}\in\mathcal{F}\_{t}^{i} implies
δ​X^si=δ​Xs\delta\widehat{X}\_{s}^{i}=\delta X\_{s}.

##### Opponents’ filter response.

For each k≠ik\neq i,
δ​(du​W^sk​(u))=δ​wsk​(u)​d​u\delta(d\_{u}\widehat{W}\_{s}^{k}(u))=\delta w\_{s}^{k}(u)\,du
with δ​wtk​(⋅)≡0\delta w\_{t}^{k}(\cdot)\equiv 0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂sδ​wsk​(u)=X~k​(s,u)⊤​Pk​(s)​(δ​Xs−∫0sX​(s,r)​δ​wsk​(r)​𝑑r),0≤u≤s.\partial\_{s}\delta w\_{s}^{k}(u)=\widetilde{X}^{k}(s,u)^{\top}P^{k}(s)\Bigl(\delta X\_{s}-\int\_{0}^{s}X(s,r)\,\delta w\_{s}^{k}(r)\,dr\Bigr),\qquad 0\leq u\leq s. |  | (B.1) |

The opponent control variation is
δ​Dsk=∫0sDk​(s,u)​δ​wsk​(u)​𝑑u\delta D\_{s}^{k}=\int\_{0}^{s}D^{k}(s,u)\,\delta w\_{s}^{k}(u)\,du,
giving the coupled state system

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​s​δ​Xs=A​(s)​δ​Xs+∑k≠i∫0sDk​(s,u)​δ​wsk​(u)​𝑑u,δ​Xt=v.\frac{d}{ds}\delta X\_{s}=A(s)\,\delta X\_{s}+\sum\_{k\neq i}\int\_{0}^{s}D^{k}(s,u)\,\delta w\_{s}^{k}(u)\,du,\qquad\delta X\_{t}=v. |  | (B.2) |

### B.3 Transition kernels

The coupled system
([B.1](#A2.E1 "In Opponents’ filter response. ‣ B.2 Spike variation and the first-variation system ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others"))–([B.2](#A2.E2 "In Opponents’ filter response. ‣ B.2 Spike variation and the first-variation system ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others"))
has bounded deterministic coefficients and admits a unique
deterministic two-parameter evolution family.

###### Definition B.1 (Block transition kernels).

For s≥ts\geq t, define ΦX​X​(s,t)∈ℝd×d\Phi^{XX}(s,t)\in\mathbb{R}^{d\times d} and
ΦX​k​(s,t,u)\Phi^{Xk}(s,t,u) (k≠ik\neq i, u∈[0,t]u\in[0,t]) by

|  |  |  |
| --- | --- | --- |
|  | δ​Xs=ΦX​X​(s,t)​v+∑k≠i∫0tΦX​k​(s,t,u)​ηk​(u)​𝑑u,\delta X\_{s}=\Phi^{XX}(s,t)\,v+\sum\_{k\neq i}\int\_{0}^{t}\Phi^{Xk}(s,t,u)\,\eta^{k}(u)\,du, |  |

for initial data δ​Xt=v\delta X\_{t}=v, δ​wtk​(⋅)=ηk​(⋅)\delta w\_{t}^{k}(\cdot)=\eta^{k}(\cdot).
In the spike deviation ηk≡0\eta^{k}\equiv 0, so
δ​Xs=ΦX​X​(s,t)​v\delta X\_{s}=\Phi^{XX}(s,t)\,v.

These blocks satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂∂t​ΦX​X​(s,t)\displaystyle\frac{\partial}{\partial t}\Phi^{XX}(s,t) | =−ΦX​X​(s,t)​A​(t)−∑k≠i∫0tΦX​k​(s,t,z)​X~k​(t,z)⊤​Pk​(t)​𝑑z,\displaystyle=-\Phi^{XX}(s,t)A(t)-\sum\_{k\neq i}\int\_{0}^{t}\Phi^{Xk}(s,t,z)\,\widetilde{X}^{k}(t,z)^{\top}P^{k}(t)\,dz, |  | (B.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂∂t​ΦX​k​(s,t,u)\displaystyle\frac{\partial}{\partial t}\Phi^{Xk}(s,t,u) | =−ΦX​X​(s,t)​Dk​(t,u)+∫0tΦX​k​(s,t,z)​X~k​(t,z)⊤​Pk​(t)​X​(t,u)​𝑑z,\displaystyle=-\Phi^{XX}(s,t)D^{k}(t,u)+\int\_{0}^{t}\Phi^{Xk}(s,t,z)\,\widetilde{X}^{k}(t,z)^{\top}P^{k}(t)\,X(t,u)\,dz, |  | (B.4) |

with ΦX​X​(t,t)=I\Phi^{XX}(t,t)=I and ΦX​k​(t,t,u)=0\Phi^{Xk}(t,t,u)=0.

### B.4 First variation of costs and the adjoint kernels

Fix player ii and suppress player superscripts on weight matrices.
Using δ​Xs=ΦX​X​(s,t)​v\delta X\_{s}=\Phi^{XX}(s,t)v and the Volterra form of XsX\_{s},
the normalized cost variation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​Jti​(v)=2​𝔼​[v⊤​(GD​Di​(t)​Dti+H¯X​(t)+∫0THX​(t,u)​𝑑W^ti​(u))|ℱti],\delta J\_{t}^{i}(v)=2\,\mathbb{E}\!\left[\left.v^{\top}\Bigl(G\_{DD}^{i}(t)D\_{t}^{i}+\bar{H}^{X}(t)+\int\_{0}^{T}H^{X}(t,u)\,d\widehat{W}\_{t}^{i}(u)\Bigr)\ \right|\mathcal{F}\_{t}^{i}\right], |  | (B.5) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H¯X​(t)\displaystyle\bar{H}^{X}(t) | :=∫tTΦX​X​(s,t)⊤​[GX​X​(s)​X¯​(s)+GX​(s)]​𝑑s+ΦX​X​(T,t)⊤​[GX​Xi​(T)​X¯​(T)+GXi​(T)],\displaystyle:=\int\_{t}^{T}\Phi^{XX}(s,t)^{\top}\bigl[G\_{XX}(s)\bar{X}(s)+G\_{X}(s)\bigr]\,ds+\Phi^{XX}(T,t)^{\top}\bigl[G^{i}\_{XX}(T)\bar{X}(T)+G^{i}\_{X}(T)\bigr], |  | (B.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | HX​(t,u)\displaystyle H^{X}(t,u) | :=∫tTΦX​X​(s,t)⊤​GX​X​(s)​X​(s,u)​𝑑s+ΦX​X​(T,t)⊤​GX​Xi​(T)​X​(T,u).\displaystyle:=\int\_{t}^{T}\Phi^{XX}(s,t)^{\top}G\_{XX}(s)\,X(s,u)\,ds+\Phi^{XX}(T,t)^{\top}G^{i}\_{XX}(T)\,X(T,u). |  | (B.7) |

##### Stationarity condition (globally necessary and sufficient).

Setting δ​Jti​(v)=0\delta J\_{t}^{i}(v)=0 for all ℱti\mathcal{F}\_{t}^{i}-measurable vv gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | GD​Di​(t)​Dti+H¯X​(t)+∫0THX​(t,u)​𝑑W^ti​(u)=0a.s.,G\_{DD}^{i}(t)D\_{t}^{i}+\bar{H}^{X}(t)+\int\_{0}^{T}H^{X}(t,u)\,d\widehat{W}\_{t}^{i}(u)=0\qquad\text{a.s.,} |  | (B.8) |

with equilibrium coefficients
D¯i​(t)=−GD​Di​(t)−1​H¯X​(t)\bar{D}^{i}(t)=-G\_{DD}^{i}(t)^{-1}\bar{H}^{X}(t) and
Di​(t,u)=−GD​Di​(t)−1​HX​(t,u)D^{i}(t,u)=-G\_{DD}^{i}(t)^{-1}H^{X}(t,u).

Equivalently, Dti=−(GD​Di​(t))−1​𝔼​[H¯X​(t)+∫0THX​(t,u)​𝑑Wu∣ℱti]D\_{t}^{i}=-(G^{i}\_{DD}(t))^{-1}\mathbb{E}[\bar{H}^{X}(t)+\int\_{0}^{T}H^{X}(t,u)\,dW\_{u}\mid\mathcal{F}\_{t}^{i}]:
the control is the conditional expectation of the full-information action
(a separation property).

### B.5 Closed backward system for the adjoint kernels

Define the belief-adjoint objects

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H¯k​(t,u)\displaystyle\bar{H}^{k}(t,u) | :=∫tTΦX​k​(s,t,u)⊤​[GX​X​(s)​X¯​(s)+GX​(s)]​𝑑s+ΦX​k​(T,t,u)⊤​[GX​Xi​(T)​X¯​(T)+GXi​(T)],\displaystyle:=\int\_{t}^{T}\Phi^{Xk}(s,t,u)^{\top}\bigl[G\_{XX}(s)\bar{X}(s)+G\_{X}(s)\bigr]\,ds+\Phi^{Xk}(T,t,u)^{\top}\bigl[G^{i}\_{XX}(T)\bar{X}(T)+G^{i}\_{X}(T)\bigr], |  | (B.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hk​(t,u,r)\displaystyle H^{k}(t,u,r) | :=∫tTΦX​k​(s,t,u)⊤​GX​X​(s)​X​(s,r)​𝑑s+ΦX​k​(T,t,u)⊤​GX​Xi​(T)​X​(T,r).\displaystyle:=\int\_{t}^{T}\Phi^{Xk}(s,t,u)^{\top}G\_{XX}(s)\,X(s,r)\,ds+\Phi^{Xk}(T,t,u)^{\top}G^{i}\_{XX}(T)\,X(T,r). |  | (B.10) |

Then (H¯X,{H¯k},HX,{Hk})(\bar{H}^{X},\{\bar{H}^{k}\},H^{X},\{H^{k}\}) satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​H¯X​(t)\displaystyle\frac{d}{dt}\bar{H}^{X}(t) | =−[GX​Xi​(t)​X¯​(t)+GXi​(t)]−A​(t)⊤​H¯X​(t)−∑k≠i∫0tPk​(t)​X~k​(t,z)​H¯k​(t,z)​𝑑z,\displaystyle=-\bigl[G^{i}\_{XX}(t)\bar{X}(t)+G^{i}\_{X}(t)\bigr]-A(t)^{\top}\bar{H}^{X}(t)-\sum\_{k\neq i}\int\_{0}^{t}P^{k}(t)\,\widetilde{X}^{k}(t,z)\,\bar{H}^{k}(t,z)\,dz, |  | (B.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​H¯k​(t,u)\displaystyle\frac{d}{dt}\bar{H}^{k}(t,u) | =−Dk​(t,u)⊤​H¯X​(t)+∫0tX​(t,u)⊤​Pk​(t)​X~k​(t,z)​H¯k​(t,z)​𝑑z,\displaystyle=-D^{k}(t,u)^{\top}\bar{H}^{X}(t)+\int\_{0}^{t}X(t,u)^{\top}P^{k}(t)\,\widetilde{X}^{k}(t,z)\,\bar{H}^{k}(t,z)\,dz, |  | (B.12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​HX​(t,r)\displaystyle\frac{d}{dt}H^{X}(t,r) | =−GX​Xi​(t)​X​(t,r)−A​(t)⊤​HX​(t,r)−∑k≠i∫0tPk​(t)​X~k​(t,z)​Hk​(t,z,r)​𝑑z,\displaystyle=-G^{i}\_{XX}(t)X(t,r)-A(t)^{\top}H^{X}(t,r)-\sum\_{k\neq i}\int\_{0}^{t}P^{k}(t)\,\widetilde{X}^{k}(t,z)\,H^{k}(t,z,r)\,dz, |  | (B.13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​t​Hk​(t,u,r)\displaystyle\frac{d}{dt}H^{k}(t,u,r) | =−Dk​(t,u)⊤​HX​(t,r)+∫0tX​(t,u)⊤​Pk​(t)​X~k​(t,z)​Hk​(t,z,r)​𝑑z,\displaystyle=-D^{k}(t,u)^{\top}H^{X}(t,r)+\int\_{0}^{t}X(t,u)^{\top}P^{k}(t)\,\widetilde{X}^{k}(t,z)\,H^{k}(t,z,r)\,dz, |  | (B.14) |

with terminal conditions
H¯X​(T)=GX​Xi​(T)​X¯​(T)+GXi​(T)\bar{H}^{X}(T)=G^{i}\_{XX}(T)\bar{X}(T)+G^{i}\_{X}(T), 
H¯k​(T,⋅)=0\bar{H}^{k}(T,\cdot)=0, 
HX​(T,r)=GX​Xi​(T)​X​(T,r)H^{X}(T,r)=G^{i}\_{XX}(T)X(T,r), 
Hk​(T,⋅,r)=0H^{k}(T,\cdot,r)=0.

### B.6 Risk-sensitive extension: exponential utility FOC

###### Theorem B.1 (Risk-sensitive extension).

Replace ([2.4](#S2.E4 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")) with the entropic risk measure

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jθii:=θi−1​log⁡𝔼​[eθi​𝒞i],θi>0,J^{i}\_{\theta\_{i}}:=\theta\_{i}^{-1}\log\mathbb{E}\!\left[e^{\,\theta\_{i}\mathcal{C}^{i}}\right],\qquad\theta\_{i}>0, |  | (B.15) |

where 𝒞i\mathcal{C}^{i} is the random cost ([2.3](#S2.E3 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")).
A Taylor expansion gives
Jθii=𝔼​[𝒞i]+θi2​Var⁡(𝒞i)+O​(θi2)J^{i}\_{\theta\_{i}}=\mathbb{E}[\mathcal{C}^{i}]+\tfrac{\theta\_{i}}{2}\operatorname{Var}(\mathcal{C}^{i})+O(\theta\_{i}^{2}),
so θi\theta\_{i} governs the degree of risk aversion
(the risk-neutral case θi→0\theta\_{i}\to 0 recovers ([2.4](#S2.E4 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others"))).

Under a deterministic-kernel Volterra profile, the best-response FOC is
identical to Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") with W^ti\widehat{W}\_{t}^{i}
replaced by the risk-adjusted noise-state

|  |  |  |
| --- | --- | --- |
|  | W^ti,θ:=(I−θi​Ct​Kt)−1​(W^ti+θi​Ct​kt),\widehat{W}^{\,i,\theta}\_{t}:=\bigl(I-\theta\_{i}C\_{t}K\_{t}\bigr)^{-1}\!\left(\widehat{W}\_{t}^{i}+\theta\_{i}C\_{t}k\_{t}\right), |  |

where Ct:=𝖢ti​(u,s)=Cov⁡(Wu,Ws∣ℱti)C\_{t}:=\mathsf{C}\_{t}^{i}(u,s)=\operatorname{Cov}(W\_{u},W\_{s}\mid\mathcal{F}\_{t}^{i}) is the
deterministic conditional covariance kernel
of WW given ℱti\mathcal{F}\_{t}^{i} (deterministic by Gaussianity of the
conditional law under the Volterra profile),
KtK\_{t} is the symmetric quadratic kernel of 𝒞i\mathcal{C}^{i} in the
Wiener-chaos representation ([B.17](#A2.E17 "In Quadratic structure of the cost. ‣ B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")), and ktk\_{t} is the
corresponding linear kernel ([B.16](#A2.E16 "In Quadratic structure of the cost. ‣ B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")).
The formula is valid when
I−θi​Ct1/2​Kt​Ct1/2≻0I-\theta\_{i}C\_{t}^{1/2}K\_{t}C\_{t}^{1/2}\succ 0,
which holds for θi\theta\_{i} sufficiently small or TT sufficiently short.
The filtering structure is unchanged; separation fails because the
quadratic cost kernel rescales conditional precision via
(I−θi​Ct​Kt)−1(I-\theta\_{i}C\_{t}K\_{t})^{-1} while ktk\_{t} shifts the conditional mean.

We now derive this result.
Replace ([2.4](#S2.E4 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")) with
Jθii:=θi−1​log⁡𝔼​[eθi​𝒞i]J^{i}\_{\theta\_{i}}:=\theta\_{i}^{-1}\log\mathbb{E}[e^{\,\theta\_{i}\mathcal{C}^{i}}],
where 𝒞i\mathcal{C}^{i} is the random cost ([2.3](#S2.E3 "In Objectives. ‣ 2.1 Primitives ‣ 2 The Decentralized LQG Game ‣ Forecasting and Manipulating the Forecasts of Others")).
The spike variation of Section [B.2](#A2.SS2 "B.2 Spike variation and the first-variation system ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others") carries over;
differentiating JθiiJ^{i}\_{\theta\_{i}} in the spike amplitude gives

|  |  |  |
| --- | --- | --- |
|  | δ​Jθi,ti​(v)=𝔼​[Zi​δ​𝒞ti​(v)],Zi:=eθi​𝒞i𝔼​[eθi​𝒞i],\delta J^{i}\_{\theta\_{i},t}(v)=\mathbb{E}\!\left[Z^{i}\,\delta\mathcal{C}^{i}\_{t}(v)\right],\qquad Z^{i}:=\frac{e^{\,\theta\_{i}\mathcal{C}^{i}}}{\mathbb{E}[e^{\,\theta\_{i}\mathcal{C}^{i}}]}, |  |

with δ​𝒞ti​(v)\delta\mathcal{C}^{i}\_{t}(v) identical to ([B.5](#A2.E5 "In B.4 First variation of costs and the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")).

##### Quadratic structure of the cost.

Expanding 𝒞i\mathcal{C}^{i} via the Volterra forms
Xs=X¯​(s)+∫0sX​(s,u)​𝑑WuX\_{s}=\bar{X}(s)+\int\_{0}^{s}X(s,u)\,dW\_{u} and
Dsi=D¯i​(s)+∫0s𝒟i​(s,u)​𝑑WuD^{i}\_{s}=\bar{D}^{i}(s)+\int\_{0}^{s}\mathcal{D}^{i}(s,u)\,dW\_{u}
and applying stochastic Fubini yields the Wiener-chaos representation

|  |  |  |
| --- | --- | --- |
|  | 𝒞i=c0+∫0Tℓ​(r)⊤​𝑑Wr+12​∫0T∫0T𝑑Wr⊤​K​(r,s)​𝑑Ws,\mathcal{C}^{i}=c\_{0}+\int\_{0}^{T}\ell(r)^{\top}dW\_{r}+\tfrac{1}{2}\int\_{0}^{T}\!\!\int\_{0}^{T}dW\_{r}^{\top}K(r,s)\,dW\_{s}, |  |

where c0c\_{0} absorbs deterministic and trace terms, and the linear and symmetric quadratic kernels are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(r)\displaystyle\ell(r) | :=∫rT[X​(t,r)⊤​(GX​Xi​(t)​X¯​(t)+GXi​(t))+𝒟i​(t,r)⊤​GD​Di​(t)​D¯i​(t)]​𝑑t\displaystyle:=\int\_{r}^{T}\!\Big[X(t,r)^{\top}\bigl(G^{i}\_{XX}(t)\bar{X}(t)+G^{i}\_{X}(t)\bigr)+\mathcal{D}^{i}(t,r)^{\top}G^{i}\_{DD}(t)\,\bar{D}^{i}(t)\Big]\,dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +X​(T,r)⊤​(GX​Xi​(T)​X¯​(T)+GXi​(T)),\displaystyle\qquad+\;X(T,r)^{\top}\bigl(G^{i}\_{XX}(T)\bar{X}(T)+G^{i}\_{X}(T)\bigr), |  | (B.16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K​(r,s)\displaystyle K(r,s) | :=∫max⁡(r,s)T[X​(t,r)⊤​GX​Xi​(t)​X​(t,s)+𝒟i​(t,r)⊤​GD​Di​(t)​𝒟i​(t,s)]​𝑑t+X​(T,r)⊤​GX​Xi​(T)​X​(T,s).\displaystyle:=\int\_{\max(r,s)}^{T}\!\Big[X(t,r)^{\top}G^{i}\_{XX}(t)\,X(t,s)+\mathcal{D}^{i}(t,r)^{\top}G^{i}\_{DD}(t)\,\mathcal{D}^{i}(t,s)\Big]\,dt+X(T,r)^{\top}G^{i}\_{XX}(T)\,X(T,s). |  | (B.17) |

##### Tilted conditional FOC.

Since 𝒞i\mathcal{C}^{i} is quadratic in WW, the weight ZiZ^{i} tilts a Gaussian measure
by a quadratic form, preserving Gaussianity.
Setting δ​Jθi,ti​(v)=0\delta J^{i}\_{\theta\_{i},t}(v)=0 for all ℱti\mathcal{F}\_{t}^{i}-measurable vv and
applying the tower property gives

|  |  |  |
| --- | --- | --- |
|  | GD​Di(t)Dti+𝔼Qi[ℳti|ℱti]=0,𝔼Qi[⋅∣ℱti]:=𝔼​[Zi​(⋅)∣ℱti]𝔼​[Zi∣ℱti],G^{i}\_{DD}(t)D^{i}\_{t}+\mathbb{E}^{Q^{i}}\!\left[\mathcal{M}^{i}\_{t}\,\Big|\,\mathcal{F}\_{t}^{i}\right]=0,\qquad\mathbb{E}^{Q^{i}}[\,\cdot\mid\mathcal{F}\_{t}^{i}]:=\frac{\mathbb{E}[Z^{i}(\cdot)\mid\mathcal{F}\_{t}^{i}]}{\mathbb{E}[Z^{i}\mid\mathcal{F}\_{t}^{i}]}, |  |

which has the structure of ([B.8](#A2.E8 "In Stationarity condition (globally necessary and sufficient). ‣ B.4 First variation of costs and the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) under the tilted measure.

##### Risk-adjusted noise-state.

Since ℳti\mathcal{M}^{i}\_{t} is linear in WW with deterministic kernels,
the FOC reduces to computing the tilted conditional mean
W^ti,θ:=𝔼Qi​[Wr∣ℱti]\widehat{W}^{\,i,\theta}\_{t}:=\mathbb{E}^{Q^{i}}[W\_{r}\mid\mathcal{F}\_{t}^{i}].
Under the deterministic-kernel profile,
ℒ​(W∣ℱti)\mathcal{L}(W\mid\mathcal{F}\_{t}^{i}) is Gaussian with mean mt:=W^tim\_{t}:=\widehat{W}\_{t}^{i}
and deterministic covariance Ct:=𝖢tiC\_{t}:=\mathsf{C}\_{t}^{i}.
The quadratic tilt shifts this to

|  |  |  |
| --- | --- | --- |
|  | Ct,θ−1=Ct−1−θi​Kt,mt,θ=Ct,θ​(Ct−1​mt+θi​kt),C\_{t,\theta}^{-1}=C\_{t}^{-1}-\theta\_{i}K\_{t},\qquad m\_{t,\theta}=C\_{t,\theta}(C\_{t}^{-1}m\_{t}+\theta\_{i}k\_{t}), |  |

provided I−θi​Ct1/2​Kt​Ct1/2≻0I-\theta\_{i}C\_{t}^{1/2}K\_{t}C\_{t}^{1/2}\succ 0
(satisfied for |θi||\theta\_{i}| small or TT short).
Rearranging gives

|  |  |  |
| --- | --- | --- |
|  | W^ti,θ=(I−θi​Ct​Kt)−1​(W^ti+θi​Ct​kt),\widehat{W}^{\,i,\theta}\_{t}=(I-\theta\_{i}C\_{t}K\_{t})^{-1}(\widehat{W}\_{t}^{i}+\theta\_{i}C\_{t}k\_{t}), |  |

and substituting into the tilted FOC yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | GD​Di(t)Dti+H¯X(t)+∫0THX(t,r)drW^ti,θ(r)= 0,\boxed{G^{i}\_{DD}(t)D^{i}\_{t}\;+\;\bar{H}^{X}(t)\;+\;\int\_{0}^{T}H^{X}(t,r)\,d\_{r}\,\widehat{W}^{\,i,\theta}\_{t}(r)\;=\;0,} |  | (B.18) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | W^ti,θ​(r):=[(I−θi​Ct​Kt)−1​(W^ti+θi​Ct​kt)]​(r).\widehat{W}^{\,i,\theta}\_{t}(r):=\bigl[(I-\theta\_{i}C\_{t}K\_{t})^{-1}\bigl(\widehat{W}\_{t}^{i}+\theta\_{i}\,C\_{t}k\_{t}\bigr)\bigr](r). |  | (B.19) |

The risk-adjusted noise-state W^ti,θ\widehat{W}^{\,i,\theta}\_{t}
differs from the risk-neutral noise-state W^ti\widehat{W}\_{t}^{i} in two ways:
the linear kernel ktk\_{t} ([B.16](#A2.E16 "In Quadratic structure of the cost. ‣ B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) shifts the conditional mean of WW
in the direction that reduces expected cost, while the quadratic
kernel KtK\_{t} ([B.17](#A2.E17 "In Quadratic structure of the cost. ‣ B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) rescales conditional precision through
(I−θi​Ct​Kt)−1(I-\theta\_{i}C\_{t}K\_{t})^{-1}, amplifying the weight on directions
of WW-space along which cost variance is large.
As θi→0\theta\_{i}\to 0, W^ti,θ→W^ti\widehat{W}^{\,i,\theta}\_{t}\to\widehat{W}\_{t}^{i}
and ([B.18](#A2.E18 "In Risk-adjusted noise-state. ‣ B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) recovers ([B.8](#A2.E8 "In Stationarity condition (globally necessary and sufficient). ‣ B.4 First variation of costs and the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")).

The first variation δ​Jθi,ti​(v)\delta J^{i}\_{\theta\_{i},t}(v) is computed
by differentiating JθiiJ^{i}\_{\theta\_{i}} in the spike amplitude
(Section [B.2](#A2.SS2 "B.2 Spike variation and the first-variation system ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")), which introduces the
exponential tilt
Zi:=eθi​𝒞i/𝔼​[eθi​𝒞i]Z^{i}:=e^{\theta\_{i}\mathcal{C}^{i}}/\mathbb{E}[e^{\theta\_{i}\mathcal{C}^{i}}].
Setting δ​Jθi,ti​(v)=0\delta J^{i}\_{\theta\_{i},t}(v)=0 for all
ℱti\mathcal{F}\_{t}^{i}-measurable vv gives the tilted stationarity condition
GD​Di​(t)​Dti+𝔼Qi​[Mti∣ℱti]=0G^{i}\_{DD}(t)D^{i}\_{t}+\mathbb{E}^{Q^{i}}[M^{i}\_{t}\mid\mathcal{F}\_{t}^{i}]=0,
where 𝔼Qi[⋅∣ℱti]:=𝔼[Zi(⋅)∣ℱti]/𝔼[Zi∣ℱti]\mathbb{E}^{Q^{i}}[\cdot\mid\mathcal{F}\_{t}^{i}]:=\mathbb{E}[Z^{i}(\cdot)\mid\mathcal{F}\_{t}^{i}]/\mathbb{E}[Z^{i}\mid\mathcal{F}\_{t}^{i}]
is the conditional expectation under the cost-tilted measure.
Since 𝒞i\mathcal{C}^{i} is quadratic in WW under the Volterra profile,
QiQ^{i} is a Gaussian measure, and computing the tilted conditional
mean of the stochastic costate MtiM^{i}\_{t} yields ([B.18](#A2.E18 "In Risk-adjusted noise-state. ‣ B.6 Risk-sensitive extension: exponential utility FOC ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")).

### B.7 Information cost: proof of Proposition [3.6](#S3.Thmthm6 "Proposition 3.6 (Information cost). ‣ Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")

##### Full- and partial-information controls.

At the equilibrium profile D∗D^{\*}, the stochastic costate is

|  |  |  |
| --- | --- | --- |
|  | Mti:=H¯Xi​(t)+∫0tHXi​(t,u)​dWu,M^{i}\_{t}:=\bar{H}^{i}\_{X}(t)+\int\_{0}^{t}H^{i}\_{X}(t,u)\,\mathrm{d}W\_{u}, |  |

where (H¯Xi,HXi)(\bar{H}^{i}\_{X},H^{i}\_{X}) solve the backward system
([B.11](#A2.E11 "In B.5 Closed backward system for the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others"))–([B.14](#A2.E14 "In B.5 Closed backward system for the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) evaluated at D∗D^{\*}.
The full-information and equilibrium controls are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Dti,full\displaystyle D^{i,\mathrm{full}}\_{t} | =−(GD​Di​(t))−1​Mti,\displaystyle=-(G^{i}\_{DD}(t))^{-1}M^{i}\_{t}, |  | (B.20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Dti\displaystyle D^{i}\_{t} | =−(GD​Di​(t))−1​𝔼​[Mti∣ℱti].\displaystyle=-(G^{i}\_{DD}(t))^{-1}\mathbb{E}[M^{i}\_{t}\mid\mathcal{F}^{i}\_{t}]. |  | (B.21) |

Both are evaluated at the same adjoint kernels: opponents’ maps are
fixed and linear with deterministic kernels, so the backward system is
identical regardless of player ii’s information. The control gap is

|  |  |  |
| --- | --- | --- |
|  | δ​Dti:=Dti−Dti,full=(GD​Di​(t))−1​∫0tHXi​(t,u)​dW~ti​(u),\delta D^{i}\_{t}:=D^{i}\_{t}-D^{i,\mathrm{full}}\_{t}=(G^{i}\_{DD}(t))^{-1}\int\_{0}^{t}H^{i}\_{X}(t,u)\,\mathrm{d}\widetilde{W}^{i}\_{t}(u), |  |

where W~ti​(u):=Wu−W^ti​(u)\widetilde{W}^{i}\_{t}(u):=W\_{u}-\widehat{W}^{i}\_{t}(u).

##### Completion of the square.

Since Di,fullD^{i,\mathrm{full}} minimizes the strictly convex quadratic
Di↦Ji​(Di;D∗,−i)D^{i}\mapsto J^{i}(D^{i};D^{\*,-i}) over L2​(ℱ)L^{2}(\mathcal{F})
(Lemma [3.4](#S3.Thmthm4 "Lemma 3.4 (Why the maximum-principle stationarity condition is global here). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")), and δ​Di∈L2​(ℱ)\delta D^{i}\in L^{2}(\mathcal{F}), the first
variation vanishes and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ji=𝔼​[∫0T(δ​Dti)⊤​GD​Di​(t)​δ​Dti​dt].\Delta J^{i}=\mathbb{E}\!\left[\int\_{0}^{T}(\delta D^{i}\_{t})^{\top}G^{i}\_{DD}(t)\,\delta D^{i}\_{t}\,\mathrm{d}t\right]. |  | (B.22) |

To verify that only GD​DiG^{i}\_{DD} appears: since δ​X\delta X is affine in
δ​Di\delta D^{i} (the dynamics are linear), the full cost perturbation
contains terms of order zero, one, and two in δ​Di\delta D^{i}. The
zero-order term vanishes by definition. All first-order
terms—including those from δ​X⊤​GX​Xi​Xfull\delta X^{\top}G^{i}\_{XX}X^{\mathrm{full}}
and (GXi)⊤​δ​X(G^{i}\_{X})^{\top}\delta X—vanish by the stationarity condition at
Di,fullD^{i,\mathrm{full}}. The second-order terms comprise the direct
control cost (δ​Di)⊤​GD​Di​δ​Di(\delta D^{i})^{\top}G^{i}\_{DD}\,\delta D^{i} and the state
cost δ​X⊤​GX​Xi​δ​X\delta X^{\top}G^{i}\_{XX}\,\delta X (plus terminal). The standard
LQG completion-of-the-square identifies these: using
GD​Di​(t)​Dti,full+Mti=0G^{i}\_{DD}(t)\,D^{i,\mathrm{full}}\_{t}+M^{i}\_{t}=0 and the definition
of MtiM^{i}\_{t} through the transition kernel ΦX​X\Phi\_{XX} (which
incorporates opponents’ linear feedback), the state-cost second-order
terms cancel against cross-terms from the adjoint, leaving
([B.22](#A2.E22 "In Completion of the square. ‣ B.7 Information cost: proof of Proposition 3.6 ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")).

##### Kernel formula for ΣtM,i\Sigma^{M,i}\_{t}.

Substituting the control gap into ([B.22](#A2.E22 "In Completion of the square. ‣ B.7 Information cost: proof of Proposition 3.6 ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ji=𝔼​[∫0T(∫0tHXi​(t,u)​dW~ti​(u))⊤​(GD​Di​(t))−1​(∫0tHXi​(t,v)​dW~ti​(v))​dt].\Delta J^{i}=\mathbb{E}\!\left[\int\_{0}^{T}\left(\int\_{0}^{t}H^{i}\_{X}(t,u)\,\mathrm{d}\widetilde{W}^{i}\_{t}(u)\right)^{\top}(G^{i}\_{DD}(t))^{-1}\left(\int\_{0}^{t}H^{i}\_{X}(t,v)\,\mathrm{d}\widetilde{W}^{i}\_{t}(v)\right)\mathrm{d}t\right]. |  | (B.23) |

Since W~ti\widetilde{W}^{i}\_{t} is Gaussian with deterministic covariance
Cti​(u,v)C^{i}\_{t}(u,v), the expectation evaluates to
tr​[(GD​Di​(t))−1​ΣtM,i]\mathrm{tr}[(G^{i}\_{DD}(t))^{-1}\,\Sigma^{M,i}\_{t}] at each tt,
giving ([3.9](#S3.E9 "In Proposition 3.6 (Information cost). ‣ Information cost and endogenous precision. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")). It remains to verify the kernel
representation of ΣtM,i\Sigma^{M,i}\_{t}.

The conditional mean of MtiM^{i}\_{t} given ℱti\mathcal{F}^{i}\_{t} is

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Mti∣ℱti]=H¯Xi​(t)+∫0tℋi​(t,s)​dWs,\mathbb{E}[M^{i}\_{t}\mid\mathcal{F}^{i}\_{t}]=\bar{H}^{i}\_{X}(t)+\int\_{0}^{t}\mathcal{H}^{i}(t,s)\,\mathrm{d}W\_{s}, |  |

where the filtered adjoint kernel is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋi​(t,s):=HXi​(t,s)​Πi+∫stHXi​(t,u)​Fti​(u,s)​du.\mathcal{H}^{i}(t,s):=H^{i}\_{X}(t,s)\,\Pi^{i}+\int\_{s}^{t}H^{i}\_{X}(t,u)\,F^{i}\_{t}(u,s)\,\mathrm{d}u. |  | (B.24) |

This is obtained by substituting the noise-state decomposition
du​W^ti​(u)=Πi​d​Wu+(∫0tFti​(u,s)​dWs)​d​u\mathrm{d}\_{u}\widehat{W}^{i}\_{t}(u)=\Pi^{i}\,\mathrm{d}W\_{u}+(\int\_{0}^{t}F^{i}\_{t}(u,s)\,\mathrm{d}W\_{s})\,\mathrm{d}u (Theorem [3.1](#S3.Thmthm1 "Theorem 3.1 (Volterra Filtering Closure). ‣ Filtering closure. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")(i))
into ∫0tHXi​(t,u)​dW^ti​(u)\int\_{0}^{t}H^{i}\_{X}(t,u)\,\mathrm{d}\widehat{W}^{i}\_{t}(u) and
applying stochastic Fubini. Then

|  |  |  |
| --- | --- | --- |
|  | Mti−𝔼​[Mti∣ℱti]=∫0t(HXi​(t,s)−ℋi​(t,s))​dWs=∫0t𝒰i​(t,s)​dWs,M^{i}\_{t}-\mathbb{E}[M^{i}\_{t}\mid\mathcal{F}^{i}\_{t}]=\int\_{0}^{t}\bigl(H^{i}\_{X}(t,s)-\mathcal{H}^{i}(t,s)\bigr)\,\mathrm{d}W\_{s}=\int\_{0}^{t}\mathcal{U}^{i}(t,s)\,\mathrm{d}W\_{s}, |  |

where
𝒰i​(t,s):=HXi​(t,s)​(I−Πi)−∫stHXi​(t,u)​Fti​(u,s)​du\mathcal{U}^{i}(t,s):=H^{i}\_{X}(t,s)(I-\Pi^{i})-\int\_{s}^{t}H^{i}\_{X}(t,u)\,F^{i}\_{t}(u,s)\,\mathrm{d}u. By Itô isometry,

|  |  |  |
| --- | --- | --- |
|  | ΣtM,i=𝔼​[(∫0t𝒰i​(t,s)​dWs)​(∫0t𝒰i​(t,s)​dWs)⊤]=∫0t𝒰i​(t,s)​𝒰i​(t,s)⊤​ds.\Sigma^{M,i}\_{t}=\mathbb{E}\!\left[\left(\int\_{0}^{t}\mathcal{U}^{i}(t,s)\,\mathrm{d}W\_{s}\right)\left(\int\_{0}^{t}\mathcal{U}^{i}(t,s)\,\mathrm{d}W\_{s}\right)^{\top}\right]=\int\_{0}^{t}\mathcal{U}^{i}(t,s)\,\mathcal{U}^{i}(t,s)^{\top}\,\mathrm{d}s. |  |

##### Separation from control.

The covariance Cti​(u,v)C^{i}\_{t}(u,v) of W~ti\widetilde{W}^{i}\_{t} is deterministic
(Gaussianity of the conditional law) and depends on the signal
structure (Pi,X)(P^{i},X) but not on the realized signal path or on DiD^{i}.
The adjoint HXiH^{i}\_{X} depends on the equilibrium profile D∗,−iD^{\*,-i}
through the forward environment, not on DiD^{i} itself. Both
𝒰i\mathcal{U}^{i} and ΣtM,i\Sigma^{M,i}\_{t} are therefore deterministic
functionals of (Pi,D∗,−i)(P^{i},D^{\*,-i}), completing the proof.
∎

## Appendix C Well-posedness of the deterministic kernel fixed point

This appendix formulates the equilibrium as a dynamic programming
problem on the kernel state space, records the a priori bounds that
follow from the projection structure of the filtering kernel, and
establishes well-posedness: contraction for short horizons,
existence for arbitrary horizons.

##### Notation.

CC denotes a generic constant depending on (n,d,L,λ)(n,d,L,\lambda);
C​(M)C(M) when it also depends on a policy-norm bound MM.

### C.1 Standing assumptions

###### Assumption C.1.

There exist L>0L>0 and λ>0\lambda>0 such that, for all t∈[0,T]t\in[0,T]
and all ii,
‖A​(t)‖+‖Σ​(t)‖+‖Pi​(t)‖+‖GX​Xi​(t)‖+‖GXi​(t)‖+‖GX​Xi​(T)‖+‖GXi​(T)‖≤L\|A(t)\|+\|\Sigma(t)\|+\|P^{i}(t)\|+\|G^{i}\_{XX}(t)\|+\|G^{i}\_{X}(t)\|+\|G^{i}\_{XX}(T)\|+\|G^{i}\_{X}(T)\|\leq L
and GD​Di​(t)⪰λ​IdG^{i}\_{DD}(t)\succeq\lambda\,I\_{d}.

### C.2 The kernel state space and its dynamics

At time tt the kernel state is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒵t:=(X¯​(t),X​(t,⋅),{Ftj}j=1n)∈ℝd×L2​([0,t];ℝd×(n+1)​d)×∏j=1nLsym2​([0,t]2;ℝ(n+1)​d×(n+1)​d).\mathcal{Z}\_{t}:=\bigl(\bar{X}(t),\;X(t,\cdot),\;\{F\_{t}^{j}\}\_{j=1}^{n}\bigr)\;\in\;\mathbb{R}^{d}\times L^{2}([0,t];\mathbb{R}^{d\times(n+1)d})\times\prod\_{j=1}^{n}L^{2}\_{\mathrm{sym}}([0,t]^{2};\mathbb{R}^{(n+1)d\times(n+1)d}). |  | (C.1) |

The unresolved kernel X~j\widetilde{X}^{j} is not a state variable; it is
determined algebraically from (𝒵t)(\mathcal{Z}\_{t}) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | X~j​(t,u)=X​(t,u)​(I−Πj)−∫0tX​(t,z)​Ftj​(z,u)​𝑑z.\widetilde{X}^{j}(t,u)=X(t,u)(I-\Pi^{j})-\int\_{0}^{t}X(t,z)\,F\_{t}^{j}(z,u)\,dz. |  | (C.2) |

Under a noise-state Volterra profile
𝐃={(D¯j,Dj)}j=1n\mathbf{D}=\{(\bar{D}^{j},D^{j})\}\_{j=1}^{n}, the kernel state evolves by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X¯˙​(t)\displaystyle\dot{\bar{X}}(t) | =A​(t)​X¯​(t)+∑kD¯k​(t),\displaystyle=A(t)\bar{X}(t)+\textstyle\sum\_{k}\bar{D}^{k}(t), |  | (C.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X˙​(t,s)\displaystyle\dot{X}(t,s) | =A​(t)​X​(t,s)+∑k𝒟k​(t,s),X​(s,s)=Σ​(s),\displaystyle=A(t)X(t,s)+\textstyle\sum\_{k}\mathcal{D}^{k}(t,s),\qquad X(s,s)=\Sigma(s), |  | (C.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tFtj​(u,s)\displaystyle\partial\_{t}F\_{t}^{j}(u,s) | =X~j​(t,u)⊤​Pj​(t)​X~j​(t,s),F0j=0,\displaystyle=\widetilde{X}^{j}(t,u)^{\top}P^{j}(t)\,\widetilde{X}^{j}(t,s),\qquad F\_{0}^{j}=0, |  | (C.5) |

with boundary Ftj​(u,t)=X~j​(t,u)⊤​Pj​(t)​EjF\_{t}^{j}(u,t)=\widetilde{X}^{j}(t,u)^{\top}\sqrt{P^{j}(t)}\,E^{j},
and primitive-noise control
𝒟k​(t,s):=Dk​(t,s)​Πk+∫0tDk​(t,u)​Ftk​(u,s)​𝑑u\mathcal{D}^{k}(t,s):=D^{k}(t,s)\Pi^{k}+\int\_{0}^{t}D^{k}(t,u)\,F\_{t}^{k}(u,s)\,du.

The policy 𝐃\mathbf{D} enters
([C.3](#A3.E3 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"))–([C.4](#A3.E4 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")) but does *not* enter
([C.5](#A3.E5 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")) directly: FjF^{j} depends on 𝐃\mathbf{D} only through
XX via ([C.2](#A3.E2 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")).

### C.3 The Hamilton–Jacobi–Bellman equation

Let Vi​(t,𝒵)V^{i}(t,\mathcal{Z}) denote the equilibrium continuation cost
for player ii from kernel state 𝒵\mathcal{Z} at time tt.
Since the kernel-state dynamics are deterministic, the HJB is a
first-order terminal-value problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tVi+DX¯​Vi⋅X¯˙+⟨DX​Vi,X˙⟩+∑j=1n⟨DFj​Vi,F˙j⟩+ℓi​(t,𝒵,𝐃)=0,Vi​(T,⋅)=gi​(⋅),\partial\_{t}V^{i}+D\_{\bar{X}}V^{i}\cdot\dot{\bar{X}}+\langle D\_{X}V^{i},\,\dot{X}\rangle+\sum\_{j=1}^{n}\langle D\_{F^{j}}V^{i},\,\dot{F}^{j}\rangle+\ell^{i}(t,\mathcal{Z},\mathbf{D})=0,\qquad V^{i}(T,\cdot)=g^{i}(\cdot), |  | (C.6) |

where ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle denotes the L2L^{2} pairing,
ℓi\ell^{i} is the running cost, and
gig^{i} is the terminal cost, both evaluated at the kernel state.

Player ii’s control (D¯i​(t),Di​(t,⋅))(\bar{D}^{i}(t),D^{i}(t,\cdot)) enters
X¯˙\dot{\bar{X}} and X˙\dot{X} linearly but does *not* enter
F˙j\dot{F}^{j}; the Hamiltonian minimization over DiD^{i} therefore
involves only DX¯​ViD\_{\bar{X}}V^{i}, DX​ViD\_{X}V^{i}, and the quadratic effort
cost, giving the first-order condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | D¯i​(t)=−(GD​Di​(t))−1​DX¯​Vi,Di​(t,u)=−(GD​Di​(t))−1​DX​Vi​(u).\bar{D}^{i}(t)=-(G^{i}\_{DD}(t))^{-1}D\_{\bar{X}}V^{i},\qquad D^{i}(t,u)=-(G^{i}\_{DD}(t))^{-1}D\_{X}V^{i}(u). |  | (C.7) |

Along the equilibrium path, DX¯​Vi=H¯Xi​(t)D\_{\bar{X}}V^{i}=\bar{H}\_{X}^{i}(t) and
DX​Vi​(⋅)=HXi​(t,⋅)D\_{X}V^{i}(\cdot)=H\_{X}^{i}(t,\cdot), recovering
Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others").

##### The information wedge as a shadow price.

The ∑j⟨DFj​Vi,F˙j⟩\sum\_{j}\langle D\_{F^{j}}V^{i},\dot{F}^{j}\rangle term
in ([C.6](#A3.E6 "In C.3 The Hamilton–Jacobi–Bellman equation ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")) captures the indirect effect of the kernel state’s
evolution on player ii’s continuation cost through opponents’ filters.
Along the equilibrium path, differentiating through the chain
Di→X→X~k→FkD^{i}\to X\to\widetilde{X}^{k}\to F^{k} identifies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱¯i​(t)=∑k≠i∫0tPk​(t)​X~k​(t,z)​H¯k,i​(t,z)​𝑑z=∑k≠i⟨DFk​Vi,∂XF˙k⟩,\bar{\mathcal{V}}^{i}(t)=\sum\_{k\neq i}\int\_{0}^{t}P^{k}(t)\,\widetilde{X}^{k}(t,z)\,\bar{H}^{k,i}(t,z)\,dz=\sum\_{k\neq i}\langle D\_{F^{k}}V^{i},\,\partial\_{X}\dot{F}^{k}\rangle, |  | (C.8) |

i.e. the mean information wedge of Theorem [3.2](#S3.Thmthm2 "Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")
is the shadow price of the opponent’s filter evolution, contracted
against the sensitivity of that evolution to the state kernel.
The kernel wedge 𝒱i​(t,r)\mathcal{V}^{i}(t,r) admits the same interpretation with H¯k,i\bar{H}^{k,i} replaced by Hk,i​(⋅,⋅,r)H^{k,i}(\cdot,\cdot,r).

##### Endogenous precision.

If Pi​(⋅)P^{i}(\cdot) is player ii’s control subject to attention cost
∫0Tci​(t,Pi​(t))​𝑑t\int\_{0}^{T}c^{i}(t,P^{i}(t))\,dt, then PiP^{i} enters ([C.6](#A3.E6 "In C.3 The Hamilton–Jacobi–Bellman equation ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"))
only through F˙i\dot{F}^{i} via ([C.5](#A3.E5 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")), and the FOC

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨DFi​Vi,X~i​(t,⋅)⊤​(⋅)​X~i​(t,⋅)⟩=∂ci∂Pi​(t,Pi​(t))\bigl\langle D\_{F^{i}}V^{i},\;\widetilde{X}^{i}(t,\cdot)^{\top}(\cdot)\,\widetilde{X}^{i}(t,\cdot)\bigr\rangle=\frac{\partial c^{i}}{\partial P^{i}}(t,P^{i}(t)) |  | (C.9) |

decouples from the FOC for DiD^{i}: the left side is the marginal
value of accelerating the filter, which vanishes as
𝒫ti→I\mathcal{P}\_{t}^{i}\to I
(Lemma [C.3](#A3.Thmthm3 "Lemma C.3 (Dissipation). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")), guaranteeing an
interior solution when ∂ci/∂Pi>0\partial c^{i}/\partial P^{i}>0.

### C.4 A priori bounds from projection structure

The filtering kernel FtjF\_{t}^{j} parametrizes a portion of the
conditional projection
(𝒫tj​f)​(u):=Πj​f​(u)+∫0tFtj​(u,s)​f​(s)​𝑑s(\mathcal{P}\_{t}^{j}f)(u):=\Pi^{j}f(u)+\int\_{0}^{t}F\_{t}^{j}(u,s)\,f(s)\,ds,
an orthogonal projection on L2​([0,t];ℝ(n+1)​d)L^{2}([0,t];\mathbb{R}^{(n+1)d})
(Remark [A.4](#A1.Thmrem4 "Remark A.4 (Self-adjointness). ‣ A.3 The filtering kernel 𝐹^𝑖 ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others")).

###### Lemma C.2 (Projection bounds).

For each jj and t≥0t\geq 0:
(i) ‖𝒫tj‖op=1\|\mathcal{P}\_{t}^{j}\|\_{\mathrm{op}}=1;
(ii) both 𝒫tj\mathcal{P}\_{t}^{j} and I−𝒫tjI-\mathcal{P}\_{t}^{j} are L2L^{2}-contractions;
(iii) ‖ℱtj‖op≤2\|\mathcal{F}\_{t}^{j}\|\_{\mathrm{op}}\leq 2
where ℱtj:=𝒫tj−Πj\mathcal{F}\_{t}^{j}:=\mathcal{P}\_{t}^{j}-\Pi^{j}.

###### Proof.

Standard properties of orthogonal projections; (iii) is the triangle
inequality.
∎

###### Lemma C.3 (Dissipation).

{𝒫tj}t≥0\{\mathcal{P}\_{t}^{j}\}\_{t\geq 0} is non-decreasing in the positive
semidefinite order, and
‖X~j​(t,⋅)‖L2​([0,t])≤‖X​(t,⋅)‖L2​([0,t])\|\widetilde{X}^{j}(t,\cdot)\|\_{L^{2}([0,t])}\leq\|X(t,\cdot)\|\_{L^{2}([0,t])}
for all tt.

###### Proof.

Equation ([C.5](#A3.E5 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")) adds a positive semidefinite increment
to FtjF\_{t}^{j}, so 𝒫tj\mathcal{P}\_{t}^{j} is non-decreasing.
Since X~j​(t,⋅)=(I−𝒫tj)​X​(t,⋅)\widetilde{X}^{j}(t,\cdot)=(I-\mathcal{P}\_{t}^{j})X(t,\cdot)
by ([C.2](#A3.E2 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")),
Lemma [C.2](#A3.Thmthm2 "Lemma C.2 (Projection bounds). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")(ii) gives the bound.
∎

These bounds hold uniformly in the precision paths, the policy
profile, and the horizon TT.
The quadratic right-hand side of ([C.5](#A3.E5 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")) is self-limiting:
as 𝒫tj\mathcal{P}\_{t}^{j} grows toward II, the complementary projection
contracts, driving X~j→0\widetilde{X}^{j}\to 0 and decelerating FjF^{j}.
This prevents finite-time blowup despite the quadratic nonlinearity
and is the Volterra-coordinate manifestation of Kalman variance collapse.

### C.5 Well-posedness

###### Definition C.1.

𝔹TM:={𝐃={(D¯i,Di)}i=1n:D¯i∈C​([0,T];ℝd),Di∈L∞​(ΔT),‖𝐃‖≤M}\mathbb{B}\_{T}^{M}:=\bigl\{\mathbf{D}=\{(\bar{D}^{i},D^{i})\}\_{i=1}^{n}:\;\bar{D}^{i}\in C([0,T];\mathbb{R}^{d}),\;D^{i}\in L^{\infty}(\Delta\_{T}),\;\|\mathbf{D}\|\leq M\bigr\},
where
‖𝐃‖:=maxi⁡(‖D¯i‖C+‖Di‖L∞)\|\mathbf{D}\|:=\max\_{i}(\|\bar{D}^{i}\|\_{C}+\|D^{i}\|\_{L^{\infty}}).

###### Definition C.2 (Best-response operator).

𝒯​(𝐃):={(−(GD​Di)−1​H¯Xi,𝐃,−(GD​Di)−1​HXi,𝐃)}i=1n\mathcal{T}(\mathbf{D}):=\bigl\{(-(G^{i}\_{DD})^{-1}\bar{H}\_{X}^{i,\mathbf{D}},\;-(G^{i}\_{DD})^{-1}H\_{X}^{i,\mathbf{D}})\bigr\}\_{i=1}^{n},
where the adjoints solve the backward system of
Theorem [3.2](#S3.Thmthm2 "Theorem 3.2 (Multiplayer belief-adjoint kernels and information wedges). ‣ Best-response closure and information wedges. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") at the forward environment
induced by 𝐃\mathbf{D}.
Fixed points are Nash equilibria
(Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others"),
Remark [3.2](#S3.Thmrem2 "Remark 3.2. ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")).

The following estimates are proved by Grönwall arguments on the
forward system ([C.3](#A3.E3 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"))–([C.5](#A3.E5 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"))
(using the a priori bounds of
Lemmas [C.2](#A3.Thmthm2 "Lemma C.2 (Projection bounds). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")–[C.3](#A3.Thmthm3 "Lemma C.3 (Dissipation). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others") to
control the quadratic nonlinearity in ([C.5](#A3.E5 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"))) and by
backward Grönwall on the linear adjoint system
([B.11](#A2.E11 "In B.5 Closed backward system for the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others"))–([B.14](#A2.E14 "In B.5 Closed backward system for the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others"))
(using Cauchy–Schwarz on the belief-adjoint coupling integrals
∫0tPk​X~k​H¯k,i​𝑑z\int\_{0}^{t}P^{k}\widetilde{X}^{k}\,\bar{H}^{k,i}\,dz).

###### Proposition C.4 (Bounds and Lipschitz continuity).

Under Assumption [C.1](#A3.Thmthm1 "Assumption C.1. ‣ C.1 Standing assumptions ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"), for 𝐃∈𝔹TM\mathbf{D}\in\mathbb{B}\_{T}^{M}:

(i) The forward system has a unique global solution with
‖X¯‖C+‖X‖L∞≤Kfwd\|\bar{X}\|\_{C}+\|X\|\_{L^{\infty}}\leq K\_{\mathrm{fwd}},
‖X~j​(t,⋅)‖L2≤Kfwd​T\|\widetilde{X}^{j}(t,\cdot)\|\_{L^{2}}\leq K\_{\mathrm{fwd}}\sqrt{T},
‖𝒫tj‖op=1\|\mathcal{P}\_{t}^{j}\|\_{\mathrm{op}}=1.

(ii) The backward system has a unique solution with
‖H¯Xi‖C+‖HXi‖L∞≤Kbwd\|\bar{H}\_{X}^{i}\|\_{C}+\|H\_{X}^{i}\|\_{L^{\infty}}\leq K\_{\mathrm{bwd}},
and time derivatives bounded by C​(M)​KbwdC(M)K\_{\mathrm{bwd}}.

(iii) Both maps
𝐃↦(X¯,X,X~j)\mathbf{D}\mapsto(\bar{X},X,\widetilde{X}^{j}) and
𝐃↦(H¯Xi,HXi)\mathbf{D}\mapsto(\bar{H}\_{X}^{i},H\_{X}^{i}) are Lipschitz with constants
Cfwd​(T,M)C\_{\mathrm{fwd}}(T,M) and Cbwd​(T,M)C\_{\mathrm{bwd}}(T,M)
respectively, both bounded by C​(M)​T​eC​(M)​TC(M)\,T\,e^{C(M)T}.

Here Kfwd,Kbwd≤C​(M)​eC​(M)​TK\_{\mathrm{fwd}},K\_{\mathrm{bwd}}\leq C(M)e^{C(M)T}.

###### Proof sketch.

For the forward system:
(X¯,X)(\bar{X},X) solve linear Volterra equations with bounded
coefficients once 𝒟k\mathcal{D}^{k} is controlled.
Since 𝒟k\mathcal{D}^{k} involves FkF^{k} through a Volterra integral,
and ‖ℱtk‖op≤2\|\mathcal{F}\_{t}^{k}\|\_{\mathrm{op}}\leq 2
(Lemma [C.2](#A3.Thmthm2 "Lemma C.2 (Projection bounds). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")), the coupled system for
ϕ​(t):=‖X‖L∞​(Δt)\phi(t):=\|X\|\_{L^{\infty}(\Delta\_{t})} closes as
ϕ​(t)≤C​(M)+C​(M)​∫0tϕ​(r)​𝑑r\phi(t)\leq C(M)+C(M)\int\_{0}^{t}\phi(r)\,dr.

For the Lipschitz bound: the variation δ​𝒟k\delta\mathcal{D}^{k}
decomposes into a direct term bounded by
C​(M)​‖δ​𝐃‖C(M)\|\delta\mathbf{D}\| and an indirect term through
δ​Fk\delta F^{k}, which couples to δ​X~k\delta\widetilde{X}^{k} and back to
δ​X\delta X via ([C.2](#A3.E2 "In C.2 The kernel state space and its dynamics ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")).
A Grönwall argument on the aggregate
Ψ​(t):=‖δ​X‖L∞​(Δt)+maxj​supr≤t‖δ​X~j​(r,⋅)‖L2\Psi(t):=\|\delta X\|\_{L^{\infty}(\Delta\_{t})}+\max\_{j}\sup\_{r\leq t}\|\delta\widetilde{X}^{j}(r,\cdot)\|\_{L^{2}}
gives
Ψ​(T)≤C​(M)​T​eC​(M)​T​‖δ​𝐃‖\Psi(T)\leq C(M)Te^{C(M)T}\|\delta\mathbf{D}\|;
the factor of TT arises because the policy enters through
integrals of length ≤T\leq T.

The backward estimates follow from linearity of the adjoint
system, Cauchy–Schwarz on coupling terms, and backward Grönwall.
∎

###### Theorem C.5 (Short-horizon equilibrium).

Under Assumption [C.1](#A3.Thmthm1 "Assumption C.1. ‣ C.1 Standing assumptions ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"), there exists T∗>0T^{\*}>0 depending only on
(n,d,L,λ)(n,d,L,\lambda) such that for T∈(0,T∗]T\in(0,T^{\*}], 𝒯\mathcal{T} is a
contraction on 𝔹TM0\mathbb{B}\_{T}^{M\_{0}} for a suitable M0M\_{0}.
In particular, there exists a unique Nash equilibrium in noise-state
Volterra strategies with bounded kernels, Picard iterates converge
geometrically, and the equilibrium is Nash over the full admissible
L2L^{2} class.

###### Proof.

By Proposition [C.4](#A3.Thmthm4 "Proposition C.4 (Bounds and Lipschitz continuity). ‣ C.5 Well-posedness ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")(iii),
Lip​(𝒯)≤λ−1​C​(M0)​T​eC​(M0)​T\mathrm{Lip}(\mathcal{T})\leq\lambda^{-1}C(M\_{0})Te^{C(M\_{0})T}.
Self-mapping (𝒯:𝔹TM0→𝔹TM0\mathcal{T}:\mathbb{B}\_{T}^{M\_{0}}\to\mathbb{B}\_{T}^{M\_{0}})
holds because at M=0M=0 the belief-adjoint decouples
(Dk≡0D^{k}\equiv 0 kills the forcing
in ([B.12](#A2.E12 "In B.5 Closed backward system for the adjoint kernels ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others"))), giving finite
Kbwd​(0,T)K\_{\mathrm{bwd}}(0,T); the intermediate value theorem yields M0M\_{0}.
Since M0M\_{0} is bounded as T→0T\to 0, choosing T∗T^{\*} small enough
makes Lip​(𝒯)≤12\mathrm{Lip}(\mathcal{T})\leq\tfrac{1}{2}.
Banach’s theorem gives existence, uniqueness, and geometric
convergence.
Corollary [3.5](#S3.Thmthm5 "Corollary 3.5 (Noise-state Volterra best response (global closure)). ‣ Policy interpretation of the wedge. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others") extends to the full L2L^{2} class.
∎

###### Theorem C.6 (Global existence).

Under Assumption [C.1](#A3.Thmthm1 "Assumption C.1. ‣ C.1 Standing assumptions ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others"), for every T>0T>0 there exists a Nash
equilibrium over the full admissible L2L^{2} class.

###### Proof sketch.

Apply the Schauder fixed-point theorem to 𝒯\mathcal{T} on
𝔹TM0\mathbb{B}\_{T}^{M\_{0}}, working in the topology
τ:=(C​([0,T])×L2​(ΔT))n\tau:=(C([0,T])\times L^{2}(\Delta\_{T}))^{n}.
Self-mapping holds by the same argument as above.
τ\tau-closedness of 𝔹TM0\mathbb{B}\_{T}^{M\_{0}}: weak-∗\* lower
semicontinuity of the L∞L^{\infty} norm preserves the bound under
L2L^{2} limits.
τ\tau-continuity of 𝒯\mathcal{T}: on the bounded set
𝔹TM0\mathbb{B}\_{T}^{M\_{0}}, L2L^{2}-convergence of policy kernels propagates
through the forward Volterra equations (via Cauchy–Schwarz) and the
linear backward system.
τ\tau-precompactness of the image: the uniform time-derivative
bound on H¯Xi\bar{H}\_{X}^{i} (Proposition [C.4](#A3.Thmthm4 "Proposition C.4 (Bounds and Lipschitz continuity). ‣ C.5 Well-posedness ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")(ii)) gives
equicontinuity of D¯i,new\bar{D}^{i,\mathrm{new}} in C​([0,T])C([0,T]);
the same bound gives pointwise-in-uu equicontinuity of
Di,new​(t,u)D^{i,\mathrm{new}}(t,u) in tt, which with the uniform L∞L^{\infty}
bound yields L2L^{2}-equicontinuity of
t↦Di,new​(t,⋅)t\mapsto D^{i,\mathrm{new}}(t,\cdot) and hence sequential
compactness in L2​(ΔT)L^{2}(\Delta\_{T})
by the vector-valued Arzelà–Ascoli theorem
([[1](#bib.bib1), Theorem 1.3.2]).
∎

###### Remark C.1 (Uniqueness beyond the contraction regime).

Theorem [C.6](#A3.Thmthm6 "Theorem C.6 (Global existence). ‣ C.5 Well-posedness ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others") gives existence but not uniqueness
for T>T∗T>T^{\*}.
The dissipation of Lemma [C.3](#A3.Thmthm3 "Lemma C.3 (Dissipation). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others") suggests
enough structure to preclude multiplicity, but a proof requires
monotonicity estimates beyond the Grönwall bounds used here.
In Section [4](#S4 "4 Bilateral belief manipulation in a two-player game ‣ Forecasting and Manipulating the Forecasts of Others"), Picard iteration
converges to the same limit from multiple initial conditions for all
parameter values tested.

###### Remark C.2 (Stochastic coefficients).

If A​(t,ω)A(t,\omega), Pi​(t,ω)P^{i}(t,\omega), or the cost matrices depend on a
public factor process ξt\xi\_{t} (e.g. a finite-state Markov chain
representing regime switches or stochastic automation events), the kernel state augments to
(𝒵t,ξt)(\mathcal{Z}\_{t},\xi\_{t}).
The projection bounds of
Lemmas [C.2](#A3.Thmthm2 "Lemma C.2 (Projection bounds). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others")–[C.3](#A3.Thmthm3 "Lemma C.3 (Dissipation). ‣ C.4 A priori bounds from projection structure ‣ Appendix C Well-posedness of the deterministic kernel fixed point ‣ Forecasting and Manipulating the Forecasts of Others") are algebraic
properties of orthogonal projections and hold pathwise, so the
forward well-posedness extends to each sample path between jumps
of ξ\xi.
Each jump triggers a regime transition in which filtering gains,
strategies, and the information wedge shift discontinuously, while
𝒵\mathcal{Z} is continuous across jumps.
The backward ODE is replaced by a backward stochastic differential
equation in the adjoint kernels, driven by jumps of ξ\xi; the
deterministic Grönwall arguments extend to pathwise bounds
conditional on the regime path.

## Appendix D Kyle–Back derivations

This appendix derives the deviation propagation system, the
first-order condition ([5.3](#S5.E3 "In 5.2 Equilibrium characterization ‣ 5 Market microstructure as a special case ‣ Forecasting and Manipulating the Forecasts of Others")), and the closed backward
ODE ([5.4](#S5.E4 "In 5.2 Equilibrium characterization ‣ 5 Market microstructure as a special case ‣ Forecasting and Manipulating the Forecasts of Others")) stated in Section [5](#S5 "5 Market microstructure as a special case ‣ Forecasting and Manipulating the Forecasts of Others").

### D.1 Drift kernels

The market maker’s drift kernel is
C0​(t,s):=σ0−1​𝒟Σ​(t,s)C^{0}(t,s):=\sigma\_{0}^{-1}\mathcal{D}\_{\Sigma}(t,s);
for trader kk:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ck​(t,s):=(σ0−1​𝒟Σ​(t,s)pk​σV​EV),Πℰk:=Π0+Πk.C^{k}(t,s):=\begin{pmatrix}\sigma\_{0}^{-1}\mathcal{D}\_{\Sigma}(t,s)\\[2.0pt] \sqrt{p\_{k}}\,\sigma\_{V}\,E^{V}\end{pmatrix}\!,\qquad\Pi\_{\mathcal{E}}^{k}:=\Pi^{0}+\Pi^{k}. |  | (D.1) |

The unresolved kernels C~0\widetilde{C}^{0} and C~k\widetilde{C}^{k} are
defined by the projection decomposition ([A.12](#A1.E12 "In Algebraic identity for 𝑋̃^𝑖 in terms of 𝐹^𝑖. ‣ A.2 Specialization to the physical observation model ‣ Appendix A Filtering ‣ Forecasting and Manipulating the Forecasts of Others"))
with CjC^{j} replacing Pj​X\sqrt{P^{j}}X and Πℰj\Pi\_{\mathcal{E}}^{j}
replacing Πj\Pi^{j}.

### D.2 Deviation propagation

A spike perturbation of trader ii’s demand at time tt enters
aggregate order flow, triggering a coupled forward response.
For s>ts>t, let δ​DΣ,s\delta D\_{\Sigma,s} be the aggregate demand
perturbation and δ​wsj​(u)\delta w\_{s}^{j}(u) the noise-state density perturbation
for observer jj.
The deviation system (cf. Section [B.2](#A2.SS2 "B.2 Spike variation and the first-variation system ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others")) is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ​DΣ,s\displaystyle\delta D\_{\Sigma,s} | =∑k≠i∫0sDk​(s,u)​δ​wsk​(u)​𝑑u,\displaystyle=\sum\_{k\neq i}\int\_{0}^{s}D^{k}(s,u)\,\delta w\_{s}^{k}(u)\,du, |  | (D.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂sδ​ws0​(u)\displaystyle\partial\_{s}\delta w\_{s}^{0}(u) | =C~0​(s,u)⊤​(σ0−1​δ​DΣ,s−∫0sC0​(s,r)​δ​ws0​(r)​𝑑r),\displaystyle=\widetilde{C}^{0}(s,u)^{\top}\biggl(\sigma\_{0}^{-1}\delta D\_{\Sigma,s}-\int\_{0}^{s}C^{0}(s,r)\,\delta w\_{s}^{0}(r)\,dr\biggr), |  | (D.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂sδ​wsk​(u)\displaystyle\partial\_{s}\delta w\_{s}^{k}(u) | =C~k​(s,u)⊤​((σ0−1​δ​DΣ,s0)−∫0sCk​(s,r)​δ​wsk​(r)​𝑑r),k≠i,\displaystyle=\widetilde{C}^{k}(s,u)^{\top}\biggl(\begin{pmatrix}\sigma\_{0}^{-1}\delta D\_{\Sigma,s}\\ 0\end{pmatrix}-\int\_{0}^{s}C^{k}(s,r)\,\delta w\_{s}^{k}(r)\,dr\biggr),\quad k\neq i, |  | (D.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ​Ps\displaystyle\delta P\_{s} | =σV​∫0sEV​δ​ws0​(u)​𝑑u,\displaystyle=\sigma\_{V}\int\_{0}^{s}E^{V}\delta w\_{s}^{0}(u)\,du, |  | (D.5) |

with δ​wtj≡0\delta w\_{t}^{j}\equiv 0, δ​DΣ,t=1\delta D\_{\Sigma,t}=1, δ​Isi=0\delta I\_{s}^{i}=0.
The demand perturbation enters each observer’s stacked
observation through the order-flow row only.
Equation ([D.2](#A4.E2 "In D.2 Deviation propagation ‣ Appendix D Kyle–Back derivations ‣ Forecasting and Manipulating the Forecasts of Others")) closes the loop: opponents’
noise-state shifts feed through their policy kernels back
into aggregate demand.
Since EV​E0,⊤=0E^{V}E^{0,\top}=0, δ​Pt=λ​(t)\delta P\_{t}=\lambda(t);
when n=1n=1, δ​DΣ,s=0\delta D\_{\Sigma,s}=0 for s>ts>t and
δ​Ps=λ​(t)\delta P\_{s}=\lambda(t) for all s≥ts\geq t.

### D.3 First-order condition

The optimality condition from a unit demand impulse at tt is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[VT−Pt−∫tTDτi​δ​Pτ​𝑑τ|ℱti]=0.\mathbb{E}\!\left[V\_{T}-P\_{t}-\int\_{t}^{T}D\_{\tau}^{i}\,\delta P\_{\tau}\,d\tau\;\Big|\;\mathcal{F}\_{t}^{i}\right]=0. |  | (D.6) |

The mispricing is
𝔼​[VT−Pt∣ℱti]=σV​∫0tEV​du​(W^ti−W^t0)​(u)\mathbb{E}[V\_{T}-P\_{t}\mid\mathcal{F}\_{t}^{i}]=\sigma\_{V}\int\_{0}^{t}E^{V}\,d\_{u}(\widehat{W}\_{t}^{i}-\widehat{W}\_{t}^{0})(u)
(since ℱt0⊂ℱti\mathcal{F}\_{t}^{0}\subset\mathcal{F}\_{t}^{i}).
The conditional future demand in Volterra form is
𝔼​[Dτi∣ℱti]=∫0tDi​(τ,u)​du​W^ti​(u)\mathbb{E}[D\_{\tau}^{i}\mid\mathcal{F}\_{t}^{i}]=\int\_{0}^{t}D^{i}(\tau,u)\,d\_{u}\widehat{W}\_{t}^{i}(u)
for τ>t\tau>t (the noise-state is a martingale, so only
u≤tu\leq t contributes).
Both terms are linear in W^ti\widehat{W}\_{t}^{i}, so matching
noise-state densities gives ([5.3](#S5.E3 "In 5.2 Equilibrium characterization ‣ 5 Market microstructure as a special case ‣ Forecasting and Manipulating the Forecasts of Others")).
Di​(t,u)D^{i}(t,u) does not appear directly: the integral over
[t,T][t,T] does not isolate τ=t\tau=t.
To pin down Di​(t,u)D^{i}(t,u), we differentiate both sides in tt.

### D.4 Leibniz differentiation and backward ODE

##### Impact adjoint.

Leibniz on Hi,impH^{i,\mathrm{imp}} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​Hi,imp​(t,u)=−λ​(t)​Di​(t,u)+∫tT∂tδ​Pτ​Di​(τ,u)​d​τ,\frac{d}{dt}H^{i,\mathrm{imp}}(t,u)=-\lambda(t)\,D^{i}(t,u)+\int\_{t}^{T}\partial\_{t}\delta P\_{\tau}\,D^{i}(\tau,u)\,d\tau, |  | (D.7) |

where the boundary term −δ​Pt⋅Di​(t,u)=−λ​(t)​Di​(t,u)-\delta P\_{t}\cdot D^{i}(t,u)=-\lambda(t)D^{i}(t,u)
is instantaneous self-impact—this is where λ​(t)\lambda(t) enters as
the endogenous GD​DiG^{i}\_{DD} and where Di​(t,u)D^{i}(t,u) first appears
explicitly.

##### Value adjoint.

In primitive-noise coordinates (Theorem [3.1](#S3.Thmthm1 "Theorem 3.1 (Volterra Filtering Closure). ‣ Filtering closure. ‣ 3 Main results ‣ Forecasting and Manipulating the Forecasts of Others")(i)),
Hi,val​(t,u)H^{i,\mathrm{val}}(t,u) has a tt-independent term
(the direct observation gap Πℰi−Π0\Pi\_{\mathcal{E}}^{i}-\Pi^{0}) and
an integral ∫0t(Fti−Ft0)​(v,u)​𝑑v\int\_{0}^{t}(F\_{t}^{i}-F\_{t}^{0})(v,u)\,dv.
Differentiating by Leibniz and the kernel evolution
∂tFtj​(v,u)=C~j​(t,v)⊤​C~j​(t,u)\partial\_{t}F\_{t}^{j}(v,u)=\widetilde{C}^{j}(t,v)^{\top}\widetilde{C}^{j}(t,u):

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​Hi,val​(t,u)=σV​EV​[(Fti−Ft0)​(t,u)+∫0t(C~i​(t,v)⊤​C~i​(t,u)−C~0​(t,v)⊤​C~0​(t,u))​𝑑v].\frac{d}{dt}H^{i,\mathrm{val}}(t,u)=\sigma\_{V}E^{V}\biggl[\bigl(F\_{t}^{i}-F\_{t}^{0}\bigr)(t,u)+\int\_{0}^{t}\bigl(\widetilde{C}^{i}(t,v)^{\top}\widetilde{C}^{i}(t,u)-\widetilde{C}^{0}(t,v)^{\top}\widetilde{C}^{0}(t,u)\bigr)\,dv\biggr]. |  | (D.8) |

##### Closed backward ODE.

Equating dd​t​Hi,val=dd​t​Hi,imp\frac{d}{dt}H^{i,\mathrm{val}}=\frac{d}{dt}H^{i,\mathrm{imp}} and solving for Di​(t,u)D^{i}(t,u)
yields ([5.4](#S5.E4 "In 5.2 Equilibrium characterization ‣ 5 Market microstructure as a special case ‣ Forecasting and Manipulating the Forecasts of Others")).
The derivative ∂tδ​Pτ\partial\_{t}\delta P\_{\tau} is obtained by
differentiating ([D.2](#A4.E2 "In D.2 Deviation propagation ‣ Appendix D Kyle–Back derivations ‣ Forecasting and Manipulating the Forecasts of Others"))–([D.5](#A4.E5 "In D.2 Deviation propagation ‣ Appendix D Kyle–Back derivations ‣ Forecasting and Manipulating the Forecasts of Others")) in
the impulse time, following the same logic as
Section [B.2](#A2.SS2 "B.2 Spike variation and the first-variation system ‣ Appendix B Control First Order Conditions ‣ Forecasting and Manipulating the Forecasts of Others") with
Pk​X→Ck\sqrt{P^{k}}X\to C^{k}, X~k→C~k\widetilde{X}^{k}\to\widetilde{C}^{k}.
Convexity (from λ​(t)>0\lambda(t)>0) ensures sufficiency.

## References

* Arendt et al. [2011]

  Wolfgang Arendt, Charles J. K. Batty, Matthias Hieber, and Frank Neubrander.
  *Vector-Valued Laplace Transforms and Cauchy Problems*,
  volume 96 of *Monographs in Mathematics*.
  Birkhäuser, 2nd edition, 2011.
  doi: 10.1007/978-3-0348-0087-7.
* Back [1992]

  Kerry Back.
  Insider trading in continuous time.
  *The Review of Financial Studies*, 5(3):387–409, 1992.
  doi: 10.1093/rfs/5.3.387.
* Bergemann and Morris [2016]

  Dirk Bergemann and Stephen Morris.
  Bayes correlated equilibrium and the comparison of information
  structures in games.
  *Theoretical Economics*, 11(2):487–522,
  2016.
  doi: 10.3982/TE1808.
* Bergemann and Morris [2019]

  Dirk Bergemann and Stephen Morris.
  Information design: A unified perspective.
  *Journal of Economic Literature*, 57(1):44–95, 2019.
  doi: 10.1257/jel.20181489.
* Bergemann et al. [2015]

  Dirk Bergemann, Tibor Heumann, and Stephen Morris.
  Information and volatility.
  *Journal of Economic Theory*, 158:427–465, 2015.
  doi: 10.1016/j.jet.2014.12.002.
* Cardaliaguet et al. [2019]

  Pierre Cardaliaguet, François Delarue, Jean-Michel Lasry, and
  Pierre-Louis Lions.
  *The Master Equation and the Convergence Problem in Mean Field
  Games*, volume 201 of *Annals of Mathematics Studies*.
  Princeton University Press, Princeton, 2019.
* Carmona and Delarue [2018]

  René Carmona and François Delarue.
  *Probabilistic Theory of Mean Field Games with Applications*,
  volume I–II of *Probability Theory and Stochastic Modelling*.
  Springer, 2018.
  doi: 10.1007/978-3-319-56436-4.
* Foster and Viswanathan [1996]

  F. Douglas Foster and S. Viswanathan.
  Strategic trading when agents forecast the forecasts of others.
  *The Journal of Finance*, 51(4):1437–1478,
  1996.
  doi: 10.1111/j.1540-6261.1996.tb04075.x.
* Hansen and Sargent [1981]

  Lars Peter Hansen and Thomas J. Sargent.
  Linear rational expectations models for dynamically interrelated
  variables.
  In Robert E. Lucas, Jr. and Thomas J. Sargent, editors,
  *Rational Expectations and Econometric Practice*, volume 1, pages
  127–156. University of Minnesota Press, Minneapolis, 1981.
* Harsanyi [1967]

  John C. Harsanyi.
  Games with incomplete information played by “Bayesian” players,
  I–III. Part I. the basic model.
  *Management Science*, 14(3):159–182, 1967.
  doi: 10.1287/mnsc.14.3.159.
* Huang et al. [2006]

  Minyi Huang, Roland P. Malhamé, and Peter E. Caines.
  Large population stochastic dynamic games: Closed-loop
  McKean–Vlasov systems and the Nash certainty equivalence principle.
  *Communications in Information and Systems*, 6(3):221–252, 2006.
* Huo and Takayama [2023]

  Zhen Huo and Naoki Takayama.
  Rational expectations models with higher-order beliefs.
  Working paper, 2023.
* Kamenica and Gentzkow [2011]

  Emir Kamenica and Matthew Gentzkow.
  Bayesian persuasion.
  *American Economic Review*, 101(6):2590–2615, 2011.
  doi: 10.1257/aer.101.6.2590.
* Kasa [2000]

  Kenneth Kasa.
  Forecasting the forecasts of others in the frequency domain.
  *Journal of Economic Dynamics and Control*, 24(5–7):875–902, 2000.
  doi: 10.1016/S0165-1889(99)00085-6.
* Kyle [1985]

  Albert S. Kyle.
  Continuous auctions and insider trading.
  *Econometrica*, 53(6):1315–1335, 1985.
  doi: 10.2307/1913210.
* Liptser and Shiryaev [2001]

  Robert S. Liptser and Albert N. Shiryaev.
  *Statistics of Random Processes*, volume I–II.
  Springer, 2nd edition, 2001.
* Maćkowiak and Wiederholt [2009]

  Bartosz Maćkowiak and Mirko Wiederholt.
  Optimal sticky prices under rational inattention.
  *American Economic Review*, 99(3):769–803,
  2009.
  doi: 10.1257/aer.99.3.769.
* Maćkowiak et al. [2023]

  Bartosz Maćkowiak, Filip Matějka, and Mirko Wiederholt.
  Rational inattention: A review.
  *Journal of Economic Literature*, 61(1):226–273, 2023.
  doi: 10.1257/jel.20211524.
* Marschak and Radner [1972]

  Jacob Marschak and Roy Radner.
  *Economic Theory of Teams*.
  Yale University Press, New Haven, 1972.
* Morris and Shin [2002]

  Stephen Morris and Hyun Song Shin.
  Social value of public information.
  *American Economic Review*, 92(5):1521–1534, 2002.
  doi: 10.1257/000282802762024610.
* Nayyar et al. [2013]

  Ashutosh Nayyar, Aditya Mahajan, and Demosthenis Teneketzis.
  Decentralized stochastic control with partial history sharing: A
  common information approach.
  *IEEE Transactions on Automatic Control*, 58(7):1644–1658, 2013.
* Nimark [2017]

  Kristoffer P. Nimark.
  Dynamic higher order expectations.
  Working paper, Cornell University, 2017.
* Radner [1962]

  Roy Radner.
  Team decision problems.
  *The Annals of Mathematical Statistics*, 33(3):857–881, 1962.
  doi: 10.1214/aoms/1177704455.
* Rondina and Walker [2021]

  Giacomo Rondina and Todd B. Walker.
  Confounding dynamics.
  *Journal of Economic Theory*, 196:105293, 2021.
  doi: 10.1016/j.jet.2021.105293.
* Sannikov [2008]

  Yuliy Sannikov.
  A continuous-time version of the principal-agent problem.
  *The Review of Economic Studies*, 75(3):957–984, 2008.
  doi: 10.1111/j.1467-937X.2008.00486.x.
* Sargent [1991]

  Thomas J. Sargent.
  Equilibrium with signal extraction from endogenous variables.
  *Journal of Economic Dynamics and Control*, 15(2):245–273, 1991.
  doi: 10.1016/0165-1889(91)90012-P.
* Sims [2003]

  Christopher A. Sims.
  Implications of rational inattention.
  *Journal of Monetary Economics*, 50(3):665–690, 2003.
  doi: 10.1016/S0304-3932(03)00029-1.
* Townsend [1983]

  Robert M. Townsend.
  Forecasting the forecasts of others.
  *Journal of Political Economy*, 91(4):546–588, 1983.
  doi: 10.1086/261166.

BETA