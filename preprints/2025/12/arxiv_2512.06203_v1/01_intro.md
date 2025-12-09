---
authors:
- Julius Tranquilli
- Naman Gupta
doc_id: arxiv:2512.06203v1
family_id: arxiv:2512.06203
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced
  Timed Automata, Finite-State Transducers, and Provable Rounding Bounds'
url_abs: http://arxiv.org/abs/2512.06203v1
url_html: https://arxiv.org/html/2512.06203v1
venue: arXiv q-fin
version: 1
year: 2025
---


Julius Tranquilli2 and Dr. Naman Gupta2

###### Abstract

Concentrated-liquidity automated market makers (CLAMMs), as exemplified by Uniswap v3, are now a common primitive in decentralized finance frameworks. Their design combines continuous trading on constant-function curves with discrete tick boundaries at which liquidity positions change and rounding effects accumulate. While there is a body of economic and game-theoretic analysis of CLAMMs, there is negligible work that treats Uniswap v3 at the level of formal *state machines* amenable to model checking or theorem proving.

In this paper we propose a formal modeling approach for Uniswap v3-style CLAMMs using (i) networks of priced timed automata (PTA), and (ii) finite-state transducers (FST) over discrete ticks. Positions are treated as stateful objects that transition only when the pool price crosses the ticks that bound their active range. We show how to encode the piecewise constant-product invariant, fee-growth variables, and tick-crossing rules in a PTA suitable for tools such as UPPAAL, and how to derive a tick-level FST abstraction for specification in TLA+.

We define an explicit tick-wise invariant for a discretized, single-tick CLAMM model and prove that it is preserved up to a tight additive rounding bound under fee-free swaps. This provides a formal justification for the “ϵ\epsilon-slack” used in invariance properties and shows how rounding enters as a controlled perturbation. We then instantiate these models in TLA+ and use TLC to exhaustively check the resulting invariants on structurally faithful instances, including a three-tick concentrated-liquidity configuration and a bounded no-rounding-only-arbitrage property in a bidirectional single-tick model. We discuss how these constructions lift to the tick-wise structure of Uniswap v3 via virtual reserves, and how the resulting properties can be phrased as PTA/TLA+ invariants about cross-tick behaviour and rounding safety.

## I Introduction

Automated market makers (AMMs) are a core building block of decentralized finance, enabling on-chain swaps via constant-function pricing rather than order books. Uniswap v3 introduced *concentrated liquidity*, allowing liquidity providers (LPs) to allocate capital to bounded price intervals rather than over the full price range [[1](https://arxiv.org/html/2512.06203v1#bib.bib1)]. This design increases capital efficiency but complicates both economic analysis and security reasoning: liquidity is now piecewise, tick-driven, and stateful.

Existing work on Uniswap v3 has focused primarily on economic aspects: strategic liquidity provision [[2](https://arxiv.org/html/2512.06203v1#bib.bib2)], expected fees and impermanent loss [[3](https://arxiv.org/html/2512.06203v1#bib.bib3)], or the exact liquidity mathematics of ticks [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. Simultaneously, there is increasing interest in mechanized reasoning about AMMs, for example the Lean 4 formalization of constant-product AMMs by Pusceddu and Bartoletti [[5](https://arxiv.org/html/2512.06203v1#bib.bib5)]. However, there is no work that captures Uniswap v3 as an explicit *transition system* suitable for off-the-shelf model checkers such as UPPAAL or TLA+ model checking.

This paper argues that Uniswap v3 and related CLAMMs are viewed as:

* •

  a network of *priced timed automata* (PTA) [[6](https://arxiv.org/html/2512.06203v1#bib.bib6)] capturing both discrete tick-crossing events and temporal aspects (e.g. gas cost budgets, time-weighted liquidity measures), and
* •

  a *finite-state transducer* (FST) on discrete ticks and bounded balances, expressing swap and liquidity actions as input symbols and pool/LP outputs as output symbols.

Within this framework we sketch a verification agenda that includes:

1. 1.

   Invariance: a pool-specific constant-function quantity remains invariant under swaps and tick-crossings, modulo bounded rounding error.
2. 2.

   Reachability: checking whether certain adverse price states (e.g. extreme ticks) are reachable under specified adversary and LP strategies.
3. 3.

   Rounding safety: establishing the absence of round-trip trading cycles that extract positive value purely from rounding behaviour, in the spirit of economic no-arbitrage conditions.

We construct a core object: a tick-wise invariant KiK\_{i} and its behaviour under discrete swaps. We define and analyze a simplified, single-tick CLAMM model that captures the arithmetic structure (constant product plus flooring) without the complication of multiple ticks. For this model we prove an explicit bound on the deviation of X​YXY (the usual constant-product invariant) due to rounding, for arbitrary fee-free swaps within the tick.

#### Contributions.

The contributions of this paper are:

* •

  A self-contained state-machine model of a Uniswap v3 pool and its positions in terms of PTA and FSTs, parameterized by ticks and bounded balances.
* •

  A concrete definition of a tick-wise invariant KiK\_{i} consistent with Uniswap-style constant-product math, together with a *proved* bound on its change under discretized swaps in a single-tick model. Mathematically this bound is elementary; the contribution lies in turning it into an explicit, parameterised *rounding core* (Definition [4](https://arxiv.org/html/2512.06203v1#Thmdefinition4 "Definition 4 (Discretized Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"), Theorem [1](https://arxiv.org/html/2512.06203v1#Thmtheorem1 "Theorem 1 (Epsilon-Slack Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds")) that can be instantiated in mechanised models.
* •

  Formal definitions of invariance and safety properties relevant to CLAMM correctness, including a “kk-invariance across ticks” property and a notion of rounding-arbitrage-freeness, together with fully explored TLA+ instances that check these properties under explicit bounds.
* •

  A mapping of this model into UPPAAL (for PTA-based model checking) and into TLA+ (for discrete state exploration), with example queries and invariants, showing how the rounding core and its bound thread through the specifications and support exhaustive exploration for bounded parameter regimes.
* •

  A discussion of how this approach relates to and complements existing theorem-proving work on AMMs in Lean and general surveys of timed automata in security [[8](https://arxiv.org/html/2512.06203v1#bib.bib8)], and how the same templates apply to constant-product AMMs beyond Uniswap v3.

## II Background

### II-A Uniswap v3 Concentrated Liquidity

At a high level, a Uniswap v3 pool manages reserves (x,y)(x,y) of two ERC-20 tokens (A,B)(A,B) and supports swaps subject to a constant-function pricing rule, but with liquidity *concentrated* in one or more price intervals [[1](https://arxiv.org/html/2512.06203v1#bib.bib1), [4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. Price is represented via a discrete *tick* index i∈ℤi\in\mathbb{Z} and a geometric tick-to-price mapping

|  |  |  |
| --- | --- | --- |
|  | Pi=λi,λ>1,P\_{i}=\lambda^{i},\quad\lambda>1, |  |

with λ≈1.0001\lambda\approx 1.0001 in the deployed protocol.

Each LP position is specified by a lower tick iℓi\_{\ell}, an upper tick iui\_{u}, and a liquidity amount L>0L>0. The position’s liquidity contributes to the pool’s *active liquidity* only when the current tick ici\_{c} lies within the half-open interval [iℓ,iu)[i\_{\ell},i\_{u}).

Inside a single tick interval [Pi,Pi+1)[P\_{i},P\_{i+1}) with active liquidity LL, the pool behaves like a standard constant-product AMM in terms of the relationship between price and reserves, but expressed in terms of P\sqrt{P} and LL rather than explicit reserves [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. When swaps drive the price to the boundary Pi+1P\_{i+1}, a *tick crossing* occurs, adjusting active liquidity by the net liquidity of all positions whose lower or upper bounds equal i+1i+1.

Economically-focused work has analyzed fees, impermanent loss, and optimal LP strategies under this design [[2](https://arxiv.org/html/2512.06203v1#bib.bib2), [3](https://arxiv.org/html/2512.06203v1#bib.bib3)].

### II-B Timed and Priced Timed Automata

Timed automata, introduced by Alur and Dill [[7](https://arxiv.org/html/2512.06203v1#bib.bib7)] and later surveyed by Bengtsson and Yi [[6](https://arxiv.org/html/2512.06203v1#bib.bib6)], extend finite-state automata with real-valued clocks that evolve continuously with time. Guards involving clock inequalities control when transitions may fire; invariants on locations bound dwelling time.

Priced timed automata (PTA) further attach costs (or prices) to locations and transitions, enabling model checking of temporal properties that involve accumulated resource usage, such as “minimal expected cost” or “maximal reward” [[9](https://arxiv.org/html/2512.06203v1#bib.bib9)]. Tools such as UPPAAL and its SMC extension support networks of PTA and queries in a fragment of timed computation tree logic (TCTL) [[10](https://arxiv.org/html/2512.06203v1#bib.bib10)].

Recent surveys show that timed automata are a natural fit for security protocols and resource-sensitive systems, capturing both functional and temporal/quantitative properties [[8](https://arxiv.org/html/2512.06203v1#bib.bib8)]. CLAMMs are similarly resource-sensitive: tokens and fees are conserved (up to rounding), while gas consumption and time in-range are important quantities.

### II-C TLA+ and Model Checking of Blockchain Protocols

TLA+ is a state-based formal specification language based on actions and temporal logic [[11](https://arxiv.org/html/2512.06203v1#bib.bib11)]. It has been used to model and verify blockchain protocols such as cross-chain swaps and consensus algorithms [[12](https://arxiv.org/html/2512.06203v1#bib.bib12), [13](https://arxiv.org/html/2512.06203v1#bib.bib13)]. In TLA+, systems are described via a state space of variable valuations and a *next-state relation* 𝖭𝖾𝗑𝗍\mathsf{Next}, together with invariants and liveness properties.

A CLAMM like Uniswap v3 fits this style of modeling: pool reserves, active liquidity, fee-growth variables, and positions all contribute to a finite (or finitely bounded) state vector. Swaps, mint-burn operations, and tick crossings are actions.

## III Uniswap v3 as a State Machine

We now define a simplified operational model of a Uniswap v3-style CLAMM, separating out the discrete tick dimension and the continuous-time dimension.

### III-A Discrete Pool State

We fix:

* •

  a finite tick range 𝖳𝗂𝖼𝗄={imin,…,imax}⊂ℤ\mathsf{Tick}=\{i\_{\min},\dots,i\_{\max}\}\subset\mathbb{Z},
* •

  a tick-to-price mapping P:𝖳𝗂𝖼𝗄→ℝ>0P:\mathsf{Tick}\to\mathbb{R}\_{>0}, Pi=λiP\_{i}=\lambda^{i},
* •

  a finite index set of positions ℐ={1,…,N}\mathcal{I}=\{1,\dots,N\}.

###### Definition 1 (Pool Configuration).

A *pool configuration* is a tuple

|  |  |  |
| --- | --- | --- |
|  | 𝖼𝖿𝗀=(ic,X,Y,Lact,ℒ,Fx,Fy)\mathsf{cfg}=(i\_{c},X,Y,L\_{\mathrm{act}},\mathcal{L},F\_{x},F\_{y}) |  |

where

* •

  ic∈𝖳𝗂𝖼𝗄i\_{c}\in\mathsf{Tick} is the current tick index,
* •

  X,Y∈ℕX,Y\in\mathbb{N} are token reserves of AA and BB in minimal units,
* •

  Lact∈ℕL\_{\mathrm{act}}\in\mathbb{N} is the active liquidity at tick ici\_{c},
* •

  ℒ:ℐ→ℕ×𝖳𝗂𝖼𝗄×𝖳𝗂𝖼𝗄\mathcal{L}:\mathcal{I}\to\mathbb{N}\times\mathsf{Tick}\times\mathsf{Tick} maps a position index kk to (Lk,iℓk,iuk)(L\_{k},i\_{\ell}^{k},i\_{u}^{k}) such that iℓk<iuki\_{\ell}^{k}<i\_{u}^{k} and Lk≥0L\_{k}\geq 0,
* •

  Fx,Fy∈ℕF\_{x},F\_{y}\in\mathbb{N} are fee-growth variables tracking cumulative fees in token units, as in the Uniswap v3 whitepaper [[1](https://arxiv.org/html/2512.06203v1#bib.bib1)].

The active liquidity LactL\_{\mathrm{act}} is derived from positions:

|  |  |  |
| --- | --- | --- |
|  | Lact=∑k∈ℐ:iℓk≤ic<iukLk.L\_{\mathrm{act}}=\sum\_{k\in\mathcal{I}:i\_{\ell}^{k}\leq i\_{c}<i\_{u}^{k}}L\_{k}. |  |

In the actual protocol, reserves and prices are represented in fixed-point formats with specific Q64.96 encodings [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)]; we abstract this as integer amounts with a fixed scale factor and a rounding operator ⌊⋅⌉\lfloor\cdot\rceil capturing rounding to the nearest representable value.

### III-B Swap and Tick-Crossing Transitions

We distinguish three classes of atomic pool transitions:

1. 1.

   Swap(δ)(\delta): swap an input amount δ>0\delta>0 of one token for the other, modifying (X,Y)(X,Y) and potentially changing ici\_{c}.
2. 2.

   Mint(k,…)(k,\dots) / Burn(k)(k): add or remove a position kk with certain (Lk,iℓk,iuk)(L\_{k},i\_{\ell}^{k},i\_{u}^{k}).
3. 3.

   Cross(±)(\pm): pure tick-crossing events where the price moves from PiP\_{i} to Pi±1P\_{i\pm 1} and LactL\_{\mathrm{act}} is updated.

We assume swaps are decomposed into infinitesimal steps that move the price along the curve up to a tick boundary; at the boundary a Cross transition updates LactL\_{\mathrm{act}} and the swap continues in the next tick interval if needed [[1](https://arxiv.org/html/2512.06203v1#bib.bib1), [4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. For the purposes of model checking, we discretize swaps into *single-tick* swaps that never cross more than one tick, and represent multi-tick swaps as finite sequences of these.

Let 𝖲𝗍𝖺𝗍𝖾\mathsf{State} denote the set of all pool configurations. Then the transition relation 𝖭𝖾𝗑𝗍⊆𝖲𝗍𝖺𝗍𝖾×𝖲𝗍𝖺𝗍𝖾\mathsf{Next}\subseteq\mathsf{State}\times\mathsf{State} is the smallest relation satisfying:

(Swap within tick) Given 𝖼𝖿𝗀\mathsf{cfg} with tick ici\_{c} and active liquidity Lact>0L\_{\mathrm{act}}>0, an input δx>0\delta\_{x}>0 of token AA yields a new configuration 𝖼𝖿𝗀′\mathsf{cfg}^{\prime} with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X′\displaystyle X^{\prime} | =X+δx,\displaystyle=X+\delta\_{x}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Y′\displaystyle Y^{\prime} | =Y−⌊ϕ(δx,Lact,ic)⌉,\displaystyle=Y-\lfloor\phi(\delta\_{x},L\_{\mathrm{act}},i\_{c})\rceil, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ic′\displaystyle i\_{c}^{\prime} | =ic,Lact′=Lact,\displaystyle=i\_{c},\quad L\_{\mathrm{act}}^{\prime}=L\_{\mathrm{act}}, |  |

where ϕ\phi encodes the constant-product pricing function on the interval [Pic,Pic+1)[P\_{i\_{c}},P\_{i\_{c}+1}) as in [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)], and the rounding operator captures Uniswap v3’s fixed-point arithmetic. We require Y′≥0Y^{\prime}\geq 0.

A symmetrical rule applies for token BB inputs.

(Tick crossing) If a swap drives the price exactly to Pic+1P\_{i\_{c}+1} (or Pic−1P\_{i\_{c}-1}), a Cross transition updates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ic′\displaystyle i\_{c}^{\prime} | =ic+1,\displaystyle=i\_{c}+1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Lact′\displaystyle L\_{\mathrm{act}}^{\prime} | =Lact+Δ​Lic+1,\displaystyle=L\_{\mathrm{act}}+\Delta L\_{i\_{c}+1}, |  |

where Δ​Lj\Delta L\_{j} is the net liquidity added or removed at tick boundary jj by positions whose range starts or ends at jj [[1](https://arxiv.org/html/2512.06203v1#bib.bib1)]. Reserves (X,Y)(X,Y) and fee-growth variables (Fx,Fy)(F\_{x},F\_{y}) are unchanged by pure crossings. Analogous rules apply for downward crossings.

(Mint/Burn) Minting and burning adjust ℒ\mathcal{L} and implicitly LactL\_{\mathrm{act}} when ici\_{c} falls inside or outside the new range.

### III-C Piecewise Constant-Function Invariant

A core correctness property of constant-product AMMs is that, in absence of fees, swaps preserve the product k=X​Yk=XY (after discrete rounding). In Uniswap v3, the invariant is defined in terms of virtual reserves computed from LactL\_{\mathrm{act}} and price; see [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. For our purposes, we separate two levels:
(i) a concrete constant-product invariant on per-tick *virtual reserves*, and
(ii) a derived tick-wise invariant KiK\_{i} on the actual pool state.

###### Definition 2 (Tick-wise Invariant).

For a tick ii and active liquidity L>0L>0, define

|  |  |  |
| --- | --- | --- |
|  | Ki​(X,Y,L):=X⋅Y,K\_{i}(X,Y,L):=X\cdot Y, |  |

the product of (virtual) reserves in the tick. In a faithful Uniswap v3 model, XX and YY can be instantiated as the virtual reserves induced by LL and the current price in [Pi,Pi+1)[P\_{i},P\_{i+1}) [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. In the simplified models below, we identify X,YX,Y with the actual reserves.

Within a single tick where no mint-burn or tick-crossing occurs, idealized fee-free swaps preserve KiK\_{i} exactly at the real-valued level; discretization introduces bounded slack. Section [IV](https://arxiv.org/html/2512.06203v1#S4 "IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") proves an explicit bound for a single-tick model. The cross-tick behaviour can then be expressed as a global invariant:

###### Definition 3 (Cross-Tick kk-Invariance).

A CLAMM satisfies *cross-tick kk-invariance* if for any sequence of swaps and tick crossings that does not mint or burn liquidity, there exists a constant k¯\overline{k} and a bound ϵ≥0\epsilon\geq 0 such that

|  |  |  |
| --- | --- | --- |
|  | |Kic​(X,Y,Lact)−k¯|≤ϵ|K\_{i\_{c}}(X,Y,L\_{\mathrm{act}})-\overline{k}|\leq\epsilon |  |

for all reachable configurations.

The explicit bound in the single-tick model will motivate concrete candidates for ϵ\epsilon.

## IV A Toy Single-Tick Model and a kk-Invariance Theorem

To ground the abstract invariant in a concrete calculation, we now analyze a simplified, single-tick CLAMM model. The goal is to exhibit a proved lemma about discretized swaps and rounding. This lemma can be understood as a local approximation of Uniswap v3 behaviour within a single tick, and provides a formally justified choice of the ϵ\epsilon bound in invariance properties.

### IV-A Toy Model

Fix a single tick (so price is constant within this model) and consider a fee-free constant-product AMM with integer reserves (X,Y)∈ℕ2(X,Y)\in\mathbb{N}^{2}, where XX and YY count minimal token units. Let

|  |  |  |
| --- | --- | --- |
|  | K:=X⋅YK:=X\cdot Y |  |

be the usual constant-product invariant.

We define a discretized swap rule for a token-AA input δ∈ℕ\delta\in\mathbb{N}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X′\displaystyle X^{\prime} | =X+δ,\displaystyle=X+\delta, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Y′\displaystyle Y^{\prime} | =⌊KX′⌋.\displaystyle=\left\lfloor\frac{K}{X^{\prime}}\right\rfloor. |  |

That is, we first compute the ideal continuous new reserve Y∗:=K/X′Y^{\ast}:=K/X^{\prime}, then round down to the nearest integer to obtain Y′Y^{\prime}. (We ignore underflow cases where Y′Y^{\prime} would be negative; these are excluded by guards in the transition system.)

This is the continuous constant-product update with a fixed rounding direction on the output leg; it is the structure underlying Uniswap v2 and, via virtual reserves, the per-tick behaviour of Uniswap v3.

### IV-B A Concrete Invariance Bound

We now prove the following statement: under the discretized swap rule above, the new product K′:=X′​Y′K^{\prime}:=X^{\prime}Y^{\prime} is bounded between K−X′K-X^{\prime} and KK.

###### Lemma 1 (Single-Swap Constant-Product Bound).

Let (X,Y)∈ℕ2(X,Y)\in\mathbb{N}^{2} with K=X​YK=XY and let δ∈ℕ\delta\in\mathbb{N}. Suppose we perform a fee-free token-AA swap according to

|  |  |  |
| --- | --- | --- |
|  | X′=X+δ,Y′=⌊KX′⌋.X^{\prime}=X+\delta,\qquad Y^{\prime}=\left\lfloor\frac{K}{X^{\prime}}\right\rfloor. |  |

Then the new product K′:=X′​Y′K^{\prime}:=X^{\prime}Y^{\prime} satisfies

|  |  |  |
| --- | --- | --- |
|  | K−X′≤K′≤K.K-X^{\prime}\;\leq\;K^{\prime}\;\leq\;K. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | |K′−K|≤X+δ.|K^{\prime}-K|\leq X+\delta. |  |

###### Proof.

Let X′=X+δX^{\prime}=X+\delta and Y∗:=K/X′Y^{\ast}:=K/X^{\prime}. By definition of floor,

|  |  |  |
| --- | --- | --- |
|  | Y∗−1<Y′≤Y∗.Y^{\ast}-1<Y^{\prime}\leq Y^{\ast}. |  |

Multiply by X′X^{\prime}:

|  |  |  |
| --- | --- | --- |
|  | X′​(Y∗−1)<X′​Y′≤X′​Y∗.X^{\prime}(Y^{\ast}-1)<X^{\prime}Y^{\prime}\leq X^{\prime}Y^{\ast}. |  |

But X′​Y∗=X′⋅(K/X′)=KX^{\prime}Y^{\ast}=X^{\prime}\cdot(K/X^{\prime})=K, so the upper bound gives

|  |  |  |
| --- | --- | --- |
|  | K′=X′​Y′≤K.K^{\prime}=X^{\prime}Y^{\prime}\leq K. |  |

For the lower bound,

|  |  |  |
| --- | --- | --- |
|  | X′​(Y∗−1)=X′​(KX′−1)=K−X′.X^{\prime}(Y^{\ast}-1)=X^{\prime}\left(\frac{K}{X^{\prime}}-1\right)=K-X^{\prime}. |  |

Since X′​(Y∗−1)<X′​Y′X^{\prime}(Y^{\ast}-1)<X^{\prime}Y^{\prime}, we have K−X′<K′K-X^{\prime}<K^{\prime}, and because K′K^{\prime} is integer this implies

|  |  |  |
| --- | --- | --- |
|  | K−X′≤K′.K-X^{\prime}\leq K^{\prime}. |  |

Finally, X′=X+δX^{\prime}=X+\delta, so

|  |  |  |
| --- | --- | --- |
|  | |K′−K|=K−K′≤X′=X+δ.|K^{\prime}-K|=K-K^{\prime}\leq X^{\prime}=X+\delta. |  |

∎

This lemma isolates the effect of the floor operation on the constant-product invariant. The upper bound K′≤KK^{\prime}\leq K is expected: rounding down can only reduce the product. The error is bounded *linearly* in X′X^{\prime}.

###### Remark 1 (Multiple Swaps).

For a sequence of swaps with inputs δ1,…,δn\delta\_{1},\dots,\delta\_{n} and corresponding intermediate reserves XjX\_{j}, repeated application of Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") yields

|  |  |  |
| --- | --- | --- |
|  | Kn≥K0−∑j=1nXj,K\_{n}\geq K\_{0}-\sum\_{j=1}^{n}X\_{j}, |  |

where Kj=Xj​YjK\_{j}=X\_{j}Y\_{j}. In particular, if Xj≤BX\_{j}\leq B for all jj, then

|  |  |  |
| --- | --- | --- |
|  | |Kn−K0|≤n​B.|K\_{n}-K\_{0}|\leq nB. |  |

For bounded reserves and bounded swap length nn, the deviation from the initial KK is therefore uniformly bounded, justifying an ϵ\epsilon in the invariance property that depends only on these bounds.

###### Definition 4 (Discretized Constant-Product Core).

A *discretized constant-product core* consists of integer reserves (X,Y)∈ℕ2(X,Y)\in\mathbb{N}^{2}, a product K=X​YK=XY, and a family of swap steps of the form

|  |  |  |
| --- | --- | --- |
|  | X′=X+δ,Y′=⌊KX′⌋,X^{\prime}=X+\delta,\qquad Y^{\prime}=\left\lfloor\frac{K}{X^{\prime}}\right\rfloor, |  |

with inputs δ∈ℕ\delta\in\mathbb{N} chosen from some bounded range, together with a bound BB such that X≤BX\leq B holds in all reachable states.

###### Theorem 1 (Epsilon-Slack Constant-Product Core).

Consider a discretized constant-product core as in Definition [4](https://arxiv.org/html/2512.06203v1#Thmdefinition4 "Definition 4 (Discretized Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"). For any finite sequence of fee-free swaps of length at most nn starting from (X0,Y0)(X\_{0},Y\_{0}) with product K0=X0​Y0K\_{0}=X\_{0}Y\_{0} and satisfying Xj≤BX\_{j}\leq B at each intermediate state, the products Kj=Xj​YjK\_{j}=X\_{j}Y\_{j} obey

|  |  |  |
| --- | --- | --- |
|  | |Kj−K0|≤n​Bfor all ​j≤n.|K\_{j}-K\_{0}|\leq nB\quad\text{for all }j\leq n. |  |

Equivalently, the core preserves the constant-product invariant up to an additive slack ϵ=n​B\epsilon=nB determined entirely by the reserve bound BB and the maximal path length nn.

The single-swap Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") and the multi-swap Remark [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") together provide the proof: each step perturbs KK by at most its current Xj≤BX\_{j}\leq B, and so a path of length nn accumulates at most n​BnB deviation in the downward direction. This abstract rounding core underlies all of the subsequent PTA, FST, and TLA+ models; Uniswap v3-style virtual reserves simply instantiate (X,Y)(X,Y) and (K,B,n)(K,B,n) with protocol-specific parameters.

jjKjK\_{j}K0K\_{0}K0−ϵK\_{0}-\epsilon0112233nn


Figure 1: Schematic illustration of the discretized constant-product core. Each swap step moves from KjK\_{j} to Kj+1K\_{j+1}, remaining within an ϵ\epsilon-band [K0−ϵ,K0][K\_{0}-\epsilon,K\_{0}] with ϵ=n​B\epsilon=nB as in Theorem [1](https://arxiv.org/html/2512.06203v1#Thmtheorem1 "Theorem 1 (Epsilon-Slack Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds").

### IV-C Rounding-Core Template for AMMs

Definition [4](https://arxiv.org/html/2512.06203v1#Thmdefinition4 "Definition 4 (Discretized Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") and Theorem [1](https://arxiv.org/html/2512.06203v1#Thmtheorem1 "Theorem 1 (Epsilon-Slack Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") capture the reusable “rounding core” that underlies a wide class of constant-product AMMs: a piece of math that can be dropped into many different models to obtain an explicit ϵ\epsilon-slack bound. Informally, any protocol that:

* •

  maintains integer (or fixed-point) reserves (X,Y)(X,Y) for a trading pair,
* •

  updates (X,Y)(X,Y) by first setting X′=X+δX^{\prime}=X+\delta or Y′=Y+δY^{\prime}=Y+\delta for an input δ\delta drawn from a bounded range,
* •

  computes the counter-reserve by dividing the product K=X​YK=XY and applying a fixed rounding direction (e.g. floor),
* •

  and enforces a uniform upper bound BB on one side of the reserves along any admissible execution,

inherits an ϵ\epsilon-slack invariant of the form |Kj−K0|≤n​B|K\_{j}-K\_{0}|\leq nB for paths of length at most nn.

In practice, applying the rounding core to a specific AMM or DEX proceeds in four steps:

1. 1.

   Identify reserves and product. Choose a pair of integer (or scaled fixed-point) reserves (X,Y)(X,Y) and a product K=X​YK=XY that captures the invariant quantity of interest (e.g. a virtual-reserve product in a Uniswap v3 tick, or the literal reserve product in a Uniswap v2 pool).
2. 2.

   Characterize swap updates. Write the swap rule in the form X′=X+δX^{\prime}=X+\delta together with Y′=⌊K/X′⌋Y^{\prime}=\lfloor K/X^{\prime}\rfloor (or symmetrically for YY input), matching the division-and-floor pattern of Definition [4](https://arxiv.org/html/2512.06203v1#Thmdefinition4 "Definition 4 (Discretized Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds").
3. 3.

   Fix bounds BB and nn. Establish a bound BB on the relevant reserve (e.g. via protocol limits, liquidity caps, or a modeling assumption) and a maximal path length nn for the executions of interest (e.g. a bound on the number of swaps in a scenario or arbitrage search).
4. 4.

   Instantiate ϵ\epsilon. Set ϵ:=n​B\epsilon:=nB and assert an ϵ\epsilon-slack invariant |Kj−K0|≤ϵ|K\_{j}-K\_{0}|\leq\epsilon along all such paths, either analytically or via a model-checking proof in a concrete bounded instance.

The TLA+ modules in Section [VII](https://arxiv.org/html/2512.06203v1#S7 "VII TLA+ Specification Sketch ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") illustrate this template: ToyCLAMM, ToyCLAMM2Dir, ToyCLAMM2DirArb, and ToyCLAMM3Tick differ only in their choice of bounds, swap directions, and inclusion of traders or ticks, but all instantiate the same discretized constant-product core.

### IV-D Connecting Back to KiK\_{i}

In a faithful Uniswap v3 tick, one does not store explicit per-tick reserves (X,Y)(X,Y) but liquidity LL and square-root price P\sqrt{P}; actual amounts of each token are derived from (L,P,Pℓ,Pu)(L,\sqrt{P},\sqrt{P\_{\ell}},\sqrt{P\_{u}}) via the formulas in [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. However, for any fixed tick interval [Pi,Pi+1)[P\_{i},P\_{i+1}) and price PP within that interval, one can define *virtual reserves* (Xvirt,Yvirt)(X^{\mathrm{virt}},Y^{\mathrm{virt}}) whose continuous evolution under swaps matches the Uniswap v3 formulas.

If we then discretize the virtual reserves via flooring to minimal token units, the swap update for (Xvirt,Yvirt)(X^{\mathrm{virt}},Y^{\mathrm{virt}}) takes the form of the single-tick model above, and Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") applies with

|  |  |  |
| --- | --- | --- |
|  | Ki​(X,Y,Lact):=Xvirt⋅Yvirt.K\_{i}(X,Y,L\_{\mathrm{act}}):=X^{\mathrm{virt}}\cdot Y^{\mathrm{virt}}. |  |

This provides an explicit and proved bound on intra-tick deviations of KiK\_{i} under discretized swaps, which can then be used as the per-tick ϵ\epsilon when stating cross-tick invariants.

### IV-E A Concrete Virtual-Reserve and Fixed-Point Instantiation

To make the link to Uniswap v3’s liquidity math more explicit, we sketch a concrete virtual-reserve construction on a single tick together with a fixed-point rounding scheme. Inside a tick interval [Pi,Pi+1)[P\_{i},P\_{i+1}) with mid-price PP and active liquidity LactL\_{\mathrm{act}}, we define continuous virtual reserves

|  |  |  |
| --- | --- | --- |
|  | X∗​(P,Lact):=LactP,Y∗​(P,Lact):=Lact​P,X^{\ast}(P,L\_{\mathrm{act}}):=\frac{L\_{\mathrm{act}}}{\sqrt{P}},\qquad Y^{\ast}(P,L\_{\mathrm{act}}):=L\_{\mathrm{act}}\sqrt{P}, |  |

so that X∗​Y∗=Lact2X^{\ast}Y^{\ast}=L\_{\mathrm{act}}^{2} is constant along the idealized price curve. This is a simplified instance of the virtual-reserve constructions in [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)], focusing on a single active price interval and omitting explicit lower/upper bounds Pℓ,PuP\_{\ell},P\_{u}.

Uniswap v3 represents prices in a Q64.96 fixed-point encoding and performs arithmetic in scaled integers [[4](https://arxiv.org/html/2512.06203v1#bib.bib4)]. To reflect this, we fix a scaling factor S∈ℕS\in\mathbb{N} (with S=296S=2^{96} corresponding to the deployed format) and define discrete virtual reserves by

|  |  |  |
| --- | --- | --- |
|  | Xvirt:=⌊S⋅X∗​(P,Lact)⌋,Yvirt:=⌊S⋅Y∗​(P,Lact)⌋.X^{\mathrm{virt}}:=\left\lfloor S\cdot X^{\ast}(P,L\_{\mathrm{act}})\right\rfloor,\qquad Y^{\mathrm{virt}}:=\left\lfloor S\cdot Y^{\ast}(P,L\_{\mathrm{act}})\right\rfloor. |  |

Swaps are then executed on (Xvirt,Yvirt)(X^{\mathrm{virt}},Y^{\mathrm{virt}}) using the discrete update rule of Section [IV](https://arxiv.org/html/2512.06203v1#S4 "IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"), and actual token transfers are recovered by rescaling back by SS. For any finite choice of SS and bounds on LactL\_{\mathrm{act}} and PP, there exist corresponding bounds Bx,ByB\_{x},B\_{y} such that Xvirt≤BxX^{\mathrm{virt}}\leq B\_{x} and Yvirt≤ByY^{\mathrm{virt}}\leq B\_{y} for all reachable states. In this regime, Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") applies verbatim to (Xvirt,Yvirt)(X^{\mathrm{virt}},Y^{\mathrm{virt}}) with Ki:=Xvirt​YvirtK\_{i}:=X^{\mathrm{virt}}Y^{\mathrm{virt}}, and the ϵ\epsilon in cross-tick invariants can be instantiated in terms of SS, LactL\_{\mathrm{act}}, and the maximal number of intra-tick swaps. This construction therefore realizes, in fixed-point arithmetic, the abstract “rounding core” used throughout the PTA, FST, and TLA+ models.

###### Remark 2 (Why a Simplified Single-Tick Model, and How It Ports to Uniswap v3).

The single-tick, fee-free reference model abstracts away several features of the deployed Uniswap v3 protocol (a large tick range, Q64.96 fixed-point arithmetic, fees, and many overlapping positions). Including all of these at once would lead to a large bounded state space for model checking and obscure the specific contribution of the rounding analysis. By isolating the floor operation on a constant-product update, Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") and its instantiated TLA+ specification capture the part of the behaviour that depends only on the division-and-floor pattern, not on the exact price parametrization. The parameters BB (or B​x,B​yBx,By) and n​M​a​xnMax in these models and ToyCLAMM are free bounds that can be calibrated to realistic reserve sizes and swap lengths, and the same reasoning applies when X,YX,Y are interpreted as Uniswap v3 virtual reserves computed from Q64.96 price and liquidity. This makes the construction a portable “rounding core” that can be embedded into more faithful, but still finitely bounded, Uniswap v3 specifications in PTA or TLA+.

## V Modeling as Priced Timed Automata

We now return to the PTA model, this time threading through the concrete invariant and bound established above.

### V-A PTA Syntax

A (priced) timed automaton [[6](https://arxiv.org/html/2512.06203v1#bib.bib6), [9](https://arxiv.org/html/2512.06203v1#bib.bib9)] is a tuple

|  |  |  |
| --- | --- | --- |
|  | 𝒜=(L,ℓ0,Xc,E,Inv,C),\mathcal{A}=(L,\ell\_{0},X\_{c},E,\mathrm{Inv},C), |  |

where:

* •

  LL is a finite set of locations; ℓ0∈L\ell\_{0}\in L is the initial location.
* •

  XcX\_{c} is a finite set of real-valued clocks.
* •

  E⊆L×𝒢​(Xc)×Act×2Xc×LE\subseteq L\times\mathcal{G}(X\_{c})\times\mathrm{Act}\times 2^{X\_{c}}\times L is a set of edges, each with a guard, action label, clock reset set, and target location.
* •

  Inv:L→𝒢​(Xc)\mathrm{Inv}:L\to\mathcal{G}(X\_{c}) assigns an invariant to each location.
* •

  CC assigns cost rates to locations and cost weights to edges.

A network of PTA is a parallel composition of such automata sharing clocks and synchronizing on action labels.

### V-B Pool Automaton

We represent the pool as an automaton 𝒜𝖯𝗈𝗈𝗅\mathcal{A}\_{\mathsf{Pool}} with:

* •

  Locations L={ℓi∣i∈𝖳𝗂𝖼𝗄}L=\{\ell\_{i}\mid i\in\mathsf{Tick}\}, one location per tick.
* •

  A clock tt measuring time since the last state update, and possibly additional clocks for LP-specific timers.
* •

  Integer-valued global variables encoding (X,Y,Lact,Fx,Fy)(X,Y,L\_{\mathrm{act}},F\_{x},F\_{y}) and the per-position data ℒ\mathcal{L}.

Intuitively, the automaton resides in location ℓic\ell\_{i\_{c}} when the current pool tick is ici\_{c}. Swap requests arrive from a separate *trader* automaton via synchronizing channels (e.g. swap0?, swap1? in UPPAAL syntax), and tick crossings correspond to edges between adjacent locations.

#### Locations and Invariants.

For each tick ii, location ℓi\ell\_{i} has an invariant:

|  |  |  |
| --- | --- | --- |
|  | Inv​(ℓi):t≤Tmax,\mathrm{Inv}(\ell\_{i}):t\leq T\_{\max}, |  |

bounding the time the system can remain without processing a swap or maintenance action. The cost rate C​(ℓi)C(\ell\_{i}) can encode, for example, the cost of capital (impermanent loss, opportunity cost) per unit time associated with the current liquidity configuration.

#### Swap Edges.

From location ℓi\ell\_{i}, a token-AA swap edge has the form:

|  |  |  |
| --- | --- | --- |
|  | (ℓi,giswap,swap0?,{t},ℓi)(\ell\_{i},\;g\_{i}^{\mathrm{swap}},\;\texttt{swap0?},\;\{t\},\;\ell\_{i}) |  |

with guard giswapg\_{i}^{\mathrm{swap}} expressing:

* •

  the requested input δx\delta\_{x} is non-zero and within a configured bound,
* •

  the resulting reserves remain non-negative,
* •

  the post-swap price remains in [Pi,Pi+1)[P\_{i},P\_{i+1}) (i.e. no tick crossing).

The action updates the global variables (X,Y,Fx,Fy)(X,Y,F\_{x},F\_{y}) and resets clock tt using the discretized update rule. On the level of the invariant, this update satisfies the per-tick bound from Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"); in particular, if we define a derived variable

|  |  |  |
| --- | --- | --- |
|  | K:=X⋅Y,K:=X\cdot Y, |  |

then each such edge satisfies

|  |  |  |
| --- | --- | --- |
|  | K−X′≤K′≤K,K-X^{\prime}\leq K^{\prime}\leq K, |  |

where primes denote post-state variables.

If the swap would reach the boundary Pi+1P\_{i+1} exactly, the edge instead targets ℓi+1\ell\_{i+1} and updates LactL\_{\mathrm{act}} by Δ​Li+1\Delta L\_{i+1} (the tick-cross rule). If the swap would overshoot the tick, we split it into a crossing part and a residual part, encoded as two edges; we approximate this with a single “crossing” edge that leaves a bounded rounding slack.

#### Mint/Burn Edges

Mint and burn operations are modeled as edges labeled mint! and burn! between locations ℓic\ell\_{i\_{c}} and itself, updating ℒ\mathcal{L} and, if needed, LactL\_{\mathrm{act}}.

### V-C Trader and Environment Automata

The pool automaton composes with trader, LP, and oracle automata as described previously. The main point is that the concrete invariant KK and its bound are now part of the model: they are expressed as integer-valued state variables and constraints on edges, rather than left abstract.

Pool(PTA)Trader(PTA)LPs(PTA)Oracle(PTA)Tick-wise FST /TLA+ rounding coreswapsliquiditypricestick abstraction+ rounding core


Figure 2: High-level architecture: the Uniswap v3 pool is modeled as a priced timed automaton composed with trader, LP, and oracle automata. A tick-wise finite-state transducer / TLA+ specification abstracts the discrete dynamics and instantiates the discretized constant-product core of Definition [4](https://arxiv.org/html/2512.06203v1#Thmdefinition4 "Definition 4 (Discretized Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds").

### V-D Properties in TCTL

With this PTA model, we can formulate verification goals as TCTL queries, as supported by UPPAAL and UPPAAL SMC [[10](https://arxiv.org/html/2512.06203v1#bib.bib10)].

#### (1) Invariant with Concrete ϵ\epsilon.

Introduce an integer-valued variable KK and a ghost variable K0K\_{0} storing its value in the initial configuration. For per-tick bounds X′≤BXX^{\prime}\leq B\_{X} and swap length at most nn, Remark 1 yields

|  |  |  |
| --- | --- | --- |
|  | |K−K0|≤n​BX.|K-K\_{0}|\leq nB\_{X}. |  |

In UPPAAL we can express a safety property:

|  |  |  |
| --- | --- | --- |
|  | A​[]​|K−K0|≤n​BX,\mathrm{A}[]\ |K-K\_{0}|\leq nB\_{X}, |  |

which is a direct translation of the analytic bound into the model checker.

#### (2) Price Reachability.

As before, we can ask whether certain “bad” ticks are reachable and whether this remains true under bounded rounding effects.

#### (3) Rounding-Arbitrage-Freeness (Local).

One can formulate a local no-arbitrage property stating that any cycle of swaps that starts and ends at the same reserves (X,Y)(X,Y) cannot increase the trader’s mark-to-market value, up to the known KK-slack. For short cycles within a single tick and bounded XX, Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") implies that the pool’s effective depth always weakens, which can be used as a potential function argument against profitable pure-rounding cycles of fixed length in the PTA model.

## VI Finite-State Transducer Abstraction

Timed automata are suited to capturing temporal and cost aspects, but many correctness questions about CLAMMs concern the *purely discrete* tick-wise dynamics and arithmetic. For these, a finite-state transducer (FST) abstraction is appropriate.

### VI-A Definition

Fix finite bounds on:

* •

  tick range 𝖳𝗂𝖼𝗄\mathsf{Tick},
* •

  reserves X,Y≤BX,Y\leq B,
* •

  number and size of positions (via bounds on LkL\_{k}).

###### Definition 5 (CLAMM Transducer).

A CLAMM FST is a tuple

|  |  |  |
| --- | --- | --- |
|  | 𝒯=(Q,Σ,Γ,q0,δ,λ),\mathcal{T}=(Q,\Sigma,\Gamma,q\_{0},\delta,\lambda), |  |

where:

* •

  QQ is a finite set of states, each encoding a bounded pool configuration 𝖼𝖿𝗀\mathsf{cfg},
* •

  Σ\Sigma is an input alphabet of actions: swap requests, mint-burn operations, administrative updates,
* •

  Γ\Gamma is an output alphabet of observed effects: actual trade amounts, fee updates, tick-crossing indicators,
* •

  q0∈Qq\_{0}\in Q is an initial state,
* •

  δ:Q×Σ→Q\delta:Q\times\Sigma\to Q is a (possibly partial) transition function,
* •

  λ:Q×Σ→Γ\lambda:Q\times\Sigma\to\Gamma is an output function.

As before,

|  |  |  |
| --- | --- | --- |
|  | Σ={Swap0​(δx),Swap1​(δy),Mint​(k,…),Burn​(k)},\Sigma=\{\texttt{Swap0}(\delta\_{x}),\ \texttt{Swap1}(\delta\_{y}),\ \texttt{Mint}(k,\dots),\ \texttt{Burn}(k)\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Γ={Traded​(dx,dy),Fees​(fx,fy),Crossed​(i→j)}.\Gamma=\{\texttt{Traded}(d\_{x},d\_{y}),\ \texttt{Fees}(f\_{x},f\_{y}),\ \texttt{Crossed}(i\to j)\}. |  |

The discretized update of (X,Y)(X,Y) inside a tick is the single-tick model from Section [IV](https://arxiv.org/html/2512.06203v1#S4 "IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"). Thus each intra-tick transition in 𝒯\mathcal{T} satisfies the product bound of Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"). This lifts the analytic lemma into an automata-theoretic invariant: for any path of length nn consisting solely of intra-tick swaps and with X≤BX\leq B, we have

|  |  |  |
| --- | --- | --- |
|  | |K​(qn)−K​(q0)|≤n​B,|K(q\_{n})-K(q\_{0})|\leq nB, |  |

where K​(q)K(q) is the value of X​YXY encoded in state qq. This can be expressed as a CTL or LTL property over 𝒯\mathcal{T}.

## VII TLA+ Specification Sketch

We briefly sketch a TLA+ specification style for the CLAMM FST that incorporates the invariant and its bound. The concrete modules introduced below—ToyCLAMM, ToyCLAMM2Dir, ToyCLAMM2DirArb, and ToyCLAMM3Tick—are instances of the discretized constant-product core from Definition [4](https://arxiv.org/html/2512.06203v1#Thmdefinition4 "Definition 4 (Discretized Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"), and can be viewed as reusable templates for constant-product+rounding systems beyond Uniswap v3 itself.

### VII-A State Variables

We introduce the following TLA+ variables:

* •

  t​i​c​k∈𝖳𝗂𝖼𝗄tick\in\mathsf{Tick},
* •

  X,Y∈0​…​BX,Y\in 0\dots B,
* •

  L​A​c​t∈0​…​Lm​a​xLAct\in 0\dots L\_{max},
* •

  Positions∈[1…N→[L:0…Lm​a​x,Low:𝖳𝗂𝖼𝗄,High:𝖳𝗂𝖼𝗄]]Positions\in[1\dots N\to[L:0\dots L\_{max},Low:\mathsf{Tick},High:\mathsf{Tick}]],
* •

  F​x,F​y∈0​…​Fm​a​xFx,Fy\in 0\dots F\_{max},
* •

  optional: T​r​a​d​e​r​B​a​l,T​r​a​d​e​r​V​a​lTraderBal,TraderVal,
* •

  a ghost variable K​0K0 storing the initial product X⋅YX\cdot Y.

We define

|  |  |  |
| --- | --- | --- |
|  | K≜X∗YK\triangleq X\*Y |  |

as a derived expression in TLA+.

### VII-B Next-State Relation

We define actions 𝖲𝗐𝖺𝗉𝟢​(δx)\mathsf{Swap0}(\delta\_{x}), 𝖲𝗐𝖺𝗉𝟣​(δy)\mathsf{Swap1}(\delta\_{y}), 𝖢𝗋𝗈𝗌𝗌𝖴𝗉\mathsf{CrossUp}, 𝖢𝗋𝗈𝗌𝗌𝖣𝗈𝗐𝗇\mathsf{CrossDown}, 𝖬𝗂𝗇𝗍​(k,…)\mathsf{Mint}(k,\dots), 𝖡𝗎𝗋𝗇​(k)\mathsf{Burn}(k) analogously to the operational model, using an explicit Floor operator for the discretized update. For intra-tick swaps, the TLA+ rule for (X′,Y′)(X^{\prime},Y^{\prime}) is the one used in Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds").

### VII-C Invariants

The concrete bound from Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") suggests the following invariants:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖨𝗇𝗏NonNeg\displaystyle\mathsf{Inv}\_{\mathrm{NonNeg}} | ≜X≥0∧Y≥0∧L​A​c​t≥0,\displaystyle\triangleq X\geq 0\land Y\geq 0\land LAct\geq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖨𝗇𝗏k,ϵ\displaystyle\mathsf{Inv}\_{k,\epsilon} | ≜|K−K​0|≤n​M​a​x∗B,\displaystyle\triangleq\bigl|K-K0\bigr|\leq nMax\*B, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖨𝗇𝗏Bounds\displaystyle\mathsf{Inv}\_{\mathrm{Bounds}} | ≜X≤B∧Y≤B∧…\displaystyle\triangleq X\leq B\land Y\leq B\land\dots |  |

where n​M​a​xnMax and BB are configuration parameters representing an upper bound on the length of intra-tick swap sequences and the maximal XX reserve respectively.

A specification

|  |  |  |
| --- | --- | --- |
|  | 𝖲𝗉𝖾𝖼≜𝖨𝗇𝗂𝗍∧□​[𝖭𝖾𝗑𝗍]⟨X,Y,L​A​c​t,P​o​s​i​t​i​o​n​s,…⟩\mathsf{Spec}\triangleq\mathsf{Init}\land\Box[\mathsf{Next}]\_{\langle X,Y,LAct,Positions,\dots\rangle} |  |

then admits the theorem

|  |  |  |
| --- | --- | --- |
|  | 𝖳𝖧𝖤𝖮𝖱𝖤𝖬𝖲𝗉𝖾𝖼⇒□​(𝖨𝗇𝗏NonNeg∧𝖨𝗇𝗏k,ϵ∧𝖨𝗇𝗏Bounds),\mathsf{THEOREM}\ \ \mathsf{Spec}\Rightarrow\Box(\mathsf{Inv}\_{\mathrm{NonNeg}}\land\mathsf{Inv}\_{k,\epsilon}\land\mathsf{Inv}\_{\mathrm{Bounds}}), |  |

which directly corresponds to the analytic reasoning. For finite bounds 𝖳𝗂𝖼𝗄,B,n​M​a​x\mathsf{Tick},B,nMax, this is amenable to model checking via TLC.

### VII-D Instantiated TLA+ Modules and TLC Checks

To instantiate the preceding sketch, we implement TLA+ modules that encode bounded instances of the single-tick model and mechanically check the invariants.

#### Single-direction ToyCLAMM.

The first module ToyCLAMM encodes the single-tick, fee-free reference model with bounded integer reserves:

* •

  Constants B​x,B​yBx,By bound the reserves X,YX,Y; L​M​a​xLMax bounds the active liquidity L​A​c​tLAct; N​M​a​xNMax bounds the number of intra-tick swaps.
* •

  Variables X,Y,L​A​c​t,𝑠𝑡𝑒𝑝,K​0X,Y,LAct,\mathit{step},K0 follow the structure above, with K≜X∗YK\triangleq X\*Y as a derived expression.
* •

  The Swap0 action implements

  |  |  |  |
  | --- | --- | --- |
  |  | X′=X+δx,Y′=⌊KX′⌋,X^{\prime}=X+\delta\_{x},\qquad Y^{\prime}=\left\lfloor\frac{K}{X^{\prime}}\right\rfloor, |  |

  for a nondeterministically chosen δx\delta\_{x} in a bounded range, and increments 𝑠𝑡𝑒𝑝\mathit{step} up to N​M​a​xNMax.

For a concrete instantiation we take

|  |  |  |
| --- | --- | --- |
|  | B​x=B​y=10,L​M​a​x=0,N​M​a​x=3,Bx=By=10,\quad LMax=0,\quad NMax=3, |  |

which bounds the state space and fixes an explicit ϵ\epsilon for the product invariant. In this setting we define the combined invariant

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖨𝗇𝗏All≜\displaystyle\mathsf{Inv}\_{\mathrm{All}}\triangleq{} | (X≥0∧Y≥0∧L​A​c​t≥0)\displaystyle(X\geq 0\land Y\geq 0\land LAct\geq 0) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∧\displaystyle{}\land{} | (X≤B​x∧Y≤B​y∧L​A​c​t≤L​M​a​x)\displaystyle(X\leq Bx\land Y\leq By\land LAct\leq LMax) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∧\displaystyle{}\land{} | (K​0−N​M​a​x∗B​x≤K≤K​0),\displaystyle(K0-NMax\*Bx\leq K\leq K0), |  |

which is a direct instantiation of 𝖨𝗇𝗏NonNeg\mathsf{Inv}\_{\mathrm{NonNeg}}, 𝖨𝗇𝗏Bounds\mathsf{Inv}\_{\mathrm{Bounds}}, and 𝖨𝗇𝗏k,ϵ\mathsf{Inv}\_{k,\epsilon} with ϵ=N​M​a​x⋅B​x=30\epsilon=NMax\cdot Bx=30. The corresponding TLA+ specification

|  |  |  |
| --- | --- | --- |
|  | 𝖲𝗉𝖾𝖼Toy≜𝖨𝗇𝗂𝗍∧□​[𝖭𝖾𝗑𝗍]⟨X,Y,L​A​c​t,𝑠𝑡𝑒𝑝,K​0⟩\mathsf{Spec}\_{\mathrm{Toy}}\triangleq\mathsf{Init}\land\Box[\mathsf{Next}]\_{\langle X,Y,LAct,\mathit{step},K0\rangle} |  |

is accompanied, in TLA+ syntax, by the theorem

|  |  |  |
| --- | --- | --- |
|  | 𝖳𝖧𝖤𝖮𝖱𝖤𝖬𝖲𝗉𝖾𝖼Toy⇒□​(𝖨𝗇𝗏All),\mathsf{THEOREM}\ \ \mathsf{Spec}\_{\mathrm{Toy}}\Rightarrow\Box(\mathsf{Inv}\_{\mathrm{All}}), |  |

which we have model checked with TLC using a standard configuration file and the constants above. In this instance, TLC explores 855 distinct reachable states (2818 generated in total) with search depth 44 and reports no counterexample to 𝖨𝗇𝗏All\mathsf{Inv}\_{\mathrm{All}}. This leads to the following named result.

###### Proposition 1 (Instantiated Single-Tick Invariant).

For B​x=B​y=10Bx=By=10, L​M​a​x=0LMax=0, and N​M​a​x=3NMax=3, every behaviour of 𝖲𝗉𝖾𝖼Toy\mathsf{Spec}\_{\mathrm{Toy}} satisfies □​(𝖨𝗇𝗏All)\Box(\mathsf{Inv}\_{\mathrm{All}}), i.e. the non-negativity, boundedness, and ϵ\epsilon-bounded product constraints with ϵ=30\epsilon=30 hold in all reachable states.

#### Bidirectional ToyCLAMM2Dir.

To move slightly closer to an actual AMM while keeping the model finite and analyzable, we introduce a second module ToyCLAMM2Dir that allows swaps in both token directions. It reuses the same constants and variables (B​x,B​y,L​M​a​x,N​M​a​x,X,Y,L​A​c​t,𝑠𝑡𝑒𝑝,K​0)(Bx,By,LMax,NMax,X,Y,LAct,\mathit{step},K0) and invariant 𝖨𝗇𝗏All\mathsf{Inv}\_{\mathrm{All}}, but extends the next-state relation with a symmetric token-BB swap:

* •

  Swap0 is as above.
* •

  Swap1 nondeterministically chooses an input δy\delta\_{y}, updates Y′=Y+δyY^{\prime}=Y+\delta\_{y} (bounded by B​yBy), and sets X′=⌊K/Y′⌋X^{\prime}=\left\lfloor K/Y^{\prime}\right\rfloor, incrementing 𝑠𝑡𝑒𝑝\mathit{step} up to N​M​a​xNMax.

The Stop action again stutters once the swap budget is exhausted. For the same concrete bounds B​x=B​y=10Bx=By=10, L​M​a​x=0LMax=0, N​M​a​x=3NMax=3, TLC explores 2542 distinct states (16950 generated in total) with search depth 44 and reports no counterexample to 𝖨𝗇𝗏All\mathsf{Inv}\_{\mathrm{All}}.

###### Proposition 2 (Bidirectional Single-Tick Invariant).

For B​x=B​y=10Bx=By=10, L​M​a​x=0LMax=0, and N​M​a​x=3NMax=3, every behaviour of the bidirectional specification based on ToyCLAMM2Dir satisfies □​(𝖨𝗇𝗏All)\Box(\mathsf{Inv}\_{\mathrm{All}}), so the same ϵ\epsilon-bounded product invariant remains stable under both token-AA and token-BB discretized swaps.

This shows that the invariant structure persists under *bidirectional* discretized constant-product swaps, which is closer to the behaviour of a real AMM pool while still fitting into a fully explored state space.

#### Rounding-Only Arbitrage Search in ToyCLAMM2DirArb.

To probe an economically meaningful property, we further extend the bidirectional single-tick model with explicit trader balances in tokens XX and YY. The module ToyCLAMM2DirArb introduces variables T​r​a​d​e​r​X,T​r​a​d​e​r​YTraderX,TraderY and a derived mark-to-market value V​a​l:=T​r​a​d​e​r​X+T​r​a​d​e​r​YVal:=TraderX+TraderY under a fixed external price normalization, together with ghost variables X0,Y0,V​a​l0X\_{0},Y\_{0},Val\_{0} storing the initial pool state and trader value. Swap actions now transfer tokens between the trader and the pool while still using the discretized constant-product update on (X,Y)(X,Y). A *rounding-only arbitrage* state is defined by

|  |  |  |
| --- | --- | --- |
|  | B​a​d​A​r​b≜(X=X0)∧(Y=Y0)∧(V​a​l>V​a​l0),BadArb\triangleq(X=X\_{0})\land(Y=Y\_{0})\land(Val>Val\_{0}), |  |

meaning that the pool has returned exactly to its initial reserves while the trader has strictly increased her value, without any change in external prices. For concrete bounds we take B​x=B​y=10Bx=By=10, L​M​a​x=0LMax=0, N​M​a​x=4NMax=4, T​0​x=10T0x=10, and T​0​y=0T0y=0.
TLC explores 10,849 distinct states (73,826 generated in total) with search depth 77 and reports no reachable state satisfying B​a​d​A​r​bBadArb.

###### Proposition 3 (No Short Rounding-Only Arbitrage).

For B​x=B​y=10Bx=By=10, L​M​a​x=0LMax=0, N​M​a​x=6NMax=6, T​0​x=10T0x=10, and T​0​y=0T0y=0, there is no behaviour of the ToyCLAMM2DirArb specification that both returns the pool from (X0,Y0)(X\_{0},Y\_{0}) to (X0,Y0)(X\_{0},Y\_{0}) and strictly increases the trader’s value V​a​lVal. Equivalently, there is no rounding-only arbitrage cycle of length at most six under these bounds.

In other words, within this bounded model there is no short *rounding-only* arbitrage cycle: no sequence of at most four bidirectional swaps returns the pool to its initial configuration while strictly increasing the trader’s mark-to-market value.

#### Three-tick ToyCLAMM3Tick.

As a minimal structural approximation of concentrated liquidity, we further define a three-tick module ToyCLAMM3Tick with ticks {T​i​c​k​M​i​n,T​i​c​k​M​i​d,T​i​c​k​M​a​x}\{TickMin,TickMid,TickMax\} representing a bounded tick range. The state now includes a tick index and an active-liquidity variable L​A​c​tLAct, while (X,Y)(X,Y) continue to represent integer “virtual” reserves updated by the same discretized constant-product swaps as above. In addition to Swap0 and Swap1, we add tick-crossing actions CrossUp and CrossDown that move the tick between neighbouring values and adjust L​A​c​tLAct within a fixed bound, leaving (X,Y)(X,Y) unchanged. For concrete bounds we take B​x=B​y=10Bx=By=10, L​M​a​x=5LMax=5, N​M​a​x=4NMax=4, and (T​i​c​k​M​i​n,T​i​c​k​M​i​d,T​i​c​k​M​a​x)=(0,1,2)(TickMin,TickMid,TickMax)=(0,1,2). We equip the model with an invariant 𝖨𝗇𝗏All3\mathsf{Inv}\_{\mathrm{All3}} that combines non-negativity, bounded tick range, bounded reserves/liquidity, and the same product bound K​0−N​M​a​x⋅B​x≤K≤K​0K0-NMax\cdot Bx\leq K\leq K0. TLC then explores 54,756 distinct states (674,604 generated in total) with search depth 55 and reports no counterexample to 𝖨𝗇𝗏All3\mathsf{Inv}\_{\mathrm{All3}}.

###### Proposition 4 (Three-Tick Cross-Tick Invariant).

For B​x=B​y=10Bx=By=10, L​M​a​x=5LMax=5, N​M​a​x=4NMax=4, and (T​i​c​k​M​i​n,T​i​c​k​M​i​d,T​i​c​k​M​a​x)=(0,1,2)(TickMin,TickMid,TickMax)=(0,1,2), every behaviour of the ToyCLAMM3Tick specification satisfies □​(𝖨𝗇𝗏All3)\Box(\mathsf{Inv}\_{\mathrm{All3}}), so the ϵ\epsilon-bounded product invariant is preserved across both intra-tick swaps and bounded sequences of tick-crossing steps.

This provides a fully explored three-tick model in which the ϵ\epsilon-bounded product invariant remains stable not only under intra-tick swaps but also under bounded sequences of tick crossings, mirroring the cross-tick kk-invariance property discussed at the semantic level. For example, if we interpret a unit of XX as a single minimal token unit and bound B=106B=10^{6} and n=100n=100 in Theorem [1](https://arxiv.org/html/2512.06203v1#Thmtheorem1 "Theorem 1 (Epsilon-Slack Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"), then the cumulative slack ϵ=n​B\epsilon=nB corresponds to at most 10810^{8} token units of deviation in KK, which in a pool with KK on the order of 101810^{18} translates to a deviation on the order of 10−1010^{-10} in relative terms (i.e. at most a few nano-basis-points of invariant drift). Although our instantiated TLA+ models use smaller bounds to keep the state space finite, the parameterised theorem explicitly shows how to scale ϵ\epsilon with realistic reserve and path-length choices.

### VII-E A Non-Uniswap Constant-Product Example

To emphasize that the discretized constant-product core is not specific to Uniswap v3, consider a standard Uniswap v2-style pool for tokens (A,B)(A,B) with integer reserves (X,Y)∈ℕ2(X,Y)\in\mathbb{N}^{2} and the usual constant-product invariant K=X​YK=XY. Fees aside, the idealized continuous swap rule for an input δ\delta of token AA sets X′=X+δX^{\prime}=X+\delta and Y′=K/X′Y^{\prime}=K/X^{\prime}, with the trader receiving Y−Y′Y-Y^{\prime}. In an on-chain implementation based on fixed-point integers, this update is realized as

|  |  |  |
| --- | --- | --- |
|  | X′=X+δ,Y′=⌊KX′⌋,X^{\prime}=X+\delta,\qquad Y^{\prime}=\left\lfloor\frac{K}{X^{\prime}}\right\rfloor, |  |

matching the division-and-floor pattern in Definition [4](https://arxiv.org/html/2512.06203v1#Thmdefinition4 "Definition 4 (Discretized Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"). If we assume that X≤BX\leq B holds along all executions of interest (e.g. by restricting attention to a range of pool sizes or by instrumenting the TLA+ model with an explicit bound), then Theorem [1](https://arxiv.org/html/2512.06203v1#Thmtheorem1 "Theorem 1 (Epsilon-Slack Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") applies directly: any sequence of at most nn fee-free swaps in such a Uniswap v2-style pool satisfies |Kj−K0|≤n​B|K\_{j}-K\_{0}|\leq nB. Thus the ϵ\epsilon-slack constant-product invariant and its TLA+ instantiations can be reused for constant-product AMMs more broadly, with Uniswap v3’s tick structure providing one particular way of organizing the state space.

### VII-F Summary of TLA+ Model Parameters

Table [I](https://arxiv.org/html/2512.06203v1#S7.T1 "TABLE I ‣ VII-F Summary of TLA+ Model Parameters ‣ VII TLA+ Specification Sketch ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") summarizes the main TLA+ instances used in this paper, including their bounds, the corresponding ϵ\epsilon from Theorem [1](https://arxiv.org/html/2512.06203v1#Thmtheorem1 "Theorem 1 (Epsilon-Slack Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds"), and the size of the state space explored by TLC.

TABLE I: Parameters and TLC statistics for TLA+ models

| Model | (B​x,L​M​a​x,N​M​a​x)(Bx,LMax,NMax) | ϵ=N​M​a​x⋅B​x\epsilon=NMax\cdot Bx | Distinct states | Depth |
| --- | --- | --- | --- | --- |
| ToyCLAMM | (10,0,3)(10,0,3) | 3030 | 855855 | 44 |
| ToyCLAMM2Dir | (10,0,3)(10,0,3) | 3030 | 25422542 | 44 |
| ToyCLAMM2DirArb | (10,0,6)(10,0,6) | 6060 | 10,84910{,}849 | 77 |
| ToyCLAMM3Tick | (10,5,4)(10,5,4) | 4040 | 54,75654{,}756 | 55 |

### VII-G A Calibrated Rounding-Only Profit Bound

To give the rounding core an explicit economic reading, consider a single tick of a Uniswap-style ETH/USDC pool whose virtual reserves on each side lie between 10610^{6} and 10710^{7} minimal units, so that K0=X0​Y0K\_{0}=X\_{0}Y\_{0} is on the order of 101210^{12} to 101410^{14}. If we conservatively bound the relevant reserve by B=106B=10^{6} units and restrict attention to cycles of at most n=6n=6 swaps (a handful of swaps in a typical MEV bundle), Theorem [1](https://arxiv.org/html/2512.06203v1#Thmtheorem1 "Theorem 1 (Epsilon-Slack Constant-Product Core). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") yields

|  |  |  |
| --- | --- | --- |
|  | |Kj−K0|≤ϵ=n​B=6⋅106|K\_{j}-K\_{0}|\leq\epsilon=nB=6\cdot 10^{6} |  |

for all j≤6j\leq 6. In relative terms this gives

|  |  |  |
| --- | --- | --- |
|  | ϵK0≤6⋅1061012=6⋅10−6,\frac{\epsilon}{K\_{0}}\leq\frac{6\cdot 10^{6}}{10^{12}}=6\cdot 10^{-6}, |  |

that is, at most 0.0006%0.0006\% or 0.060.06 basis points of invariant drift for six-step paths in such a tick.

Since a change Δ​K\Delta K in the product translates into a change of order Δ​K/X\Delta K/X or Δ​K/Y\Delta K/Y in one of the reserves, the corresponding upper bound on a trader’s mark-to-market gain from a rounding-only six-swap cycle is on the order of a few minimal token units, i.e. well below a basis point of the pool’s notional value in this regime. Our TLC search in ToyCLAMM2DirArb with B​x=B​y=10Bx=By=10 and N​M​a​x=6NMax=6 should be read as a scaled instance of this argument: each integer reserve unit can be interpreted as a fixed block of physical token units, and the absence of rounding-only arbitrage cycles of length at most six in the finite model is consistent with the analytic bound that any such cycle would be economically negligible under these parameters.

## VIII Relation to Existing Formal Work

Our automata-based approach is complementary to theorem-proving work in Lean [[5](https://arxiv.org/html/2512.06203v1#bib.bib5)] and economic analyses of CLAMMs [[3](https://arxiv.org/html/2512.06203v1#bib.bib3), [2](https://arxiv.org/html/2512.06203v1#bib.bib2)].

Pusceddu and Bartoletti mechanize the correctness of constant-product AMMs in Lean [[5](https://arxiv.org/html/2512.06203v1#bib.bib5)], proving properties such as arbitrage behaviour and optimal swaps in a general mathematical framework. Their model focuses on the v2-style, full-range constant-product construction. Our model, by contrast, aims at the piecewise-constant, tick-driven structure of v3, with explicit state-machine semantics suitable for model checking. Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") is a self-contained result in the same spirit as Lean-level reasoning but tailored to the discretized invariant we feed into automata-based tools.

Timed automata have already been used extensively for verifying security and resource properties in other domains [[8](https://arxiv.org/html/2512.06203v1#bib.bib8), [10](https://arxiv.org/html/2512.06203v1#bib.bib10)]. Our use of PTA to reason about CLAMM fees, gas, and liquidity costs fits neatly into this tradition. Similarly, TLA+ has been applied to blockchain protocols such as cross-chain swaps [[12](https://arxiv.org/html/2512.06203v1#bib.bib12)] and CBC Casper consensus [[13](https://arxiv.org/html/2512.06203v1#bib.bib13)]; a CLAMM TLA+ specification can reuse many of the same modeling patterns (e.g. action decomposition, fairness constraints, ghost variables for invariants), but now grounded in an explicit, proved arithmetic bound on the core invariant.

## IX Limitations and Future Work

The models described in this paper remain simplified:

* •

  We bound ticks, reserves, and position counts to achieve finiteness, whereas real deployments are unbounded (within gas limits).
* •

  We abstract away EVM-level implementation details, event ordering, and reentrancy, focusing on the idealized CLAMM logic.
* •

  Our invariant analysis is currently local to a single tick and fee-free swaps; extending Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") to include fees and multi-tick paths via virtual reserves is a natural next step.
* •

  We do not yet instantiate a full Q64.96 fixed-point semantics; doing so would sharpen the rounding bounds but also enlarge the state space.

Several directions for future work are immediate:

* •

  Instantiate the PTA model in UPPAAL for bounded parameters and check the kk-invariance property with a concrete ϵ\epsilon, using Lemma [1](https://arxiv.org/html/2512.06203v1#Thmlemma1 "Lemma 1 (Single-Swap Constant-Product Bound). ‣ IV-B A Concrete Invariance Bound ‣ IV A Toy Single-Tick Model and a 𝑘-Invariance Theorem ‣ Formal State-Machine Models for Uniswap v3 Concentrated-Liquidity AMMs: Priced Timed Automata, Finite-State Transducers, and Provable Rounding Bounds") as a sanity check on reported counterexamples.
* •

  Develop a library of TLA+ modules for CLAMMs, including parameterized Uniswap v2/v3 specifications, and mechanically check 𝖨𝗇𝗏NonNeg\mathsf{Inv}\_{\mathrm{NonNeg}} and 𝖨𝗇𝗏k,ϵ\mathsf{Inv}\_{k,\epsilon} for finite instances.
* •

  Integrate the CLAMM model with cross-chain bridges or L2 sequencers modeled in TLA+, to study end-to-end correctness of rollups or bridges that rely on CLAMM-based price oracles.
* •

  Refine the single-tick model to capture known classes of rounding exploits (e.g. multi-hop paths that amplify rounding) and prove, under explicit parameter bounds, that no such exploit exists up to a given path length.

## X Conclusion

We have argued that Uniswap v3-style concentrated-liquidity AMMs can be effectively modeled as networks of priced timed automata and finite-state transducers, with positions as stateful objects whose behaviour is driven by tick crossings. Within this view, important correctness questions such as cross-tick invariance, price-state reachability, and rounding-arbitrage absence, become standard safety and liveness properties for which mature model-checking tools exist.

To ensure that this perspective is not purely aspirational, we isolated and proved a concrete lemma about the behaviour of the constant-product invariant under discretized swaps in a single-tick model. This lemma provides a mathematically justified ϵ\epsilon-slack for invariance properties and demonstrates how the rounding behaviour can be reasoned about explicitly. Lifting such local results to full CLAMM specifications in PTA and TLA+ remains a substantial but, we believe, tractable research program.

## References

* [1]

  H. Adams, N. Zinsmeister, M. Salem, R. Keefer, and D. Robinson.
  Uniswap v3 Core.
  Technical report, Uniswap Labs, 2021.
  <https://uniswap.org/whitepaper-v3.pdf>.
* [2]

  Z. Fan, F. Marmolejo-Cossío, D. J. Moroz, M. Neuder, R. Rao, and D. C.
  Parkes.
  Strategic Liquidity Provision in Uniswap v3.
  In *5th Conference on Advances in Financial Technologies
  (AFT 2023)*, volume 282 of *LIPIcs*, pages 25:1–25:22. Schloss Dagstuhl,
  2023.
* [3]

  S. Hashemseresht and M. Pourpouneh.
  Concentrated Liquidity Analysis in Uniswap V3.
  In *Proceedings of the 2022 ACM CCS Workshop on Decentralized
  Finance and Security (DeFi’22)*, pages 63–70. ACM, 2022.
* [4]

  A. Elsts.
  Liquidity Math in Uniswap v3.
  Technical report, 2021.
  <https://atiselsts.github.io/pdfs/uniswap-v3-liquidity-math.pdf>.
* [5]

  D. Pusceddu and M. Bartoletti.
  Formalizing Automated Market Makers in the Lean 4 Theorem Prover.
  In *5th International Workshop on Formal Methods for Blockchains
  (FMBC 2024)*, volume 118 of *OASIcs*, pages 5:1–5:13. Schloss Dagstuhl,
  2024.
* [6]

  J. Bengtsson and W. Yi.
  Timed Automata: Semantics, Algorithms and Tools.
  In J. Desel, W. Reisig, and G. Rozenberg, editors, *Lectures on
  Concurrency and Petri Nets*, volume 3098 of *LNCS*, pages 87–124.
  Springer, 2004.
* [7]

  R. Alur and D. L. Dill.
  A Theory of Timed Automata.
  *Theoretical Computer Science*, 126(2):183–235, 1994.
* [8]

  J. Arcile and É. André.
  Timed Automata as a Formalism for Expressing Security: A Survey on
  Theory and Practice.
  *ACM Computing Surveys*, 55(6):1–37, 2022.
* [9]

  A. David, P. G. Jensen, K. G. Larsen, A. Legay, D. Lime, M. G. Sørensen,
  and J. H. Taankvist.
  On Time with Minimal Expected Cost!
  In F. Cassez and J.-F. Raskin, editors, *Automated Technology
  for Verification and Analysis (ATVA)*, volume 8837 of *LNCS*, pages
  129–145. Springer, 2014.
* [10]

  A. David, K. G. Larsen, A. Legay, M. Mikučionis, and D. B. Poulsen.
  Uppaal SMC Tutorial.
  *International Journal on Software Tools for Technology
  Transfer*, 17(4):397–415, 2015.
* [11]

  L. Lamport.
  *Specifying Systems: The TLA+ Language and Tools for Hardware
  and Software Engineers*.
  Addison-Wesley, 2002.
* [12]

  Z. Nehaï, F. Bobot, S. Tucci-Piergiovanni, C. Delporte-Gallet, and
  H. Fauconnier.
  A TLA+ Formal Proof of a Cross-Chain Swap.
  In *23rd International Conference on Distributed Computing and
  Networking (ICDCN 2022)*, pages 148–159. ACM, 2022.
* [13]

  A. Ouyang.
  Formal Analysis of the CBC Casper Consensus Algorithm with TLA+.
  Trail of Bits Blog, 2019.
  <https://blog.trailofbits.com/2019/10/25/formal-analysis-of-the-cbc-casper-consensus-algorithm-with-tla/>.