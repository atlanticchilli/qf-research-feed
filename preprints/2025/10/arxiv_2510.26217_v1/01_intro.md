---
authors:
- Tao Jin
- Stuart Florescu
- Heyu
- Jin
doc_id: arxiv:2510.26217v1
family_id: arxiv:2510.26217
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Hybrid LLM + Higher-Order Quantum Approximate Optimization for CSA Collateral
  Management
url_abs: http://arxiv.org/abs/2510.26217v1
url_html: https://arxiv.org/html/2510.26217v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tao Jin

Pyligent AI

tao.jin@pyligentai.com



Stuart Florescu

Dept. of Computer & Mathematical Sciences, Caltech

sfloresc@caltech.edu



Heyu (Andrew) Jin

Department of Economics, UCLA

andrewjin@ucla.edu

###### Abstract

We address *finance-native* collateral optimization under ISDA Credit Support Annexes (CSAs), where integer lots, Schedule A haircuts, RA/MTA gating, and issuer/currency/class caps create rugged, legally bounded search spaces. We introduce a certifiable hybrid pipeline *purpose-built* for this domain: (i) an evidence-gated LLM that extracts CSA terms to a normalized JSON (abstain-by-default, span-cited); (ii) a quantum-inspired explorer that interleaves simulated annealing with *micro higher-order QAOA* (HO-QAOA) on binding sub-QUBOs (subset size n≤16n\!\leq\!16, order k≤4k\!\leq\!4) to coordinate multi-asset moves across caps and RA-induced discreteness; (iii) a weighted risk-aware objective (Movement, CVaR, funding-priced overshoot) with an explicit coverage window U≤Reff+BU\!\leq\!R\_{\mathrm{eff}}{+}B; and (iv) CP-SAT as single arbiter to *certify* feasibility and gaps, including a U-cap pre-check that reports the minimal feasible buffer B⋆B^{\star}. Encoding caps/rounding as higher-order terms lets HO-QAOA target the domain couplings that defeat local swaps. On government bond datasets and multi-CSA inputs, the hybrid improves a strong classical baseline (BL-3) by 9.1%, 9.6%, and 10.7% across representative harnesses, delivering better cost–movement–tail frontiers under governance settings. We release governance-grade artifacts—span citations, valuation matrix audit, weight provenance, QUBO manifests, and CP-SAT traces—to make results auditable and reproducible.

## I Introduction

Collateral posted under ISDA Credit Support Annexes (CSAs) must satisfy legally binding rules on eligibility, haircuts (Schedule A), rounding (RA), Minimum Transfer Amount (MTA), and concentration limits (issuer/currency/class/global). Integer lots, haircut tiers, and caps create a rugged search space; operational frictions (movement) and funding/tail considerations further complicate the objective. Enterprise diagnostics suggest that suboptimal allocation, trapped liquidity, and fragmented inventories impose material costs, motivating automation and enterprise optimization [[1](https://arxiv.org/html/2510.26217v1#bib.bib1), [2](https://arxiv.org/html/2510.26217v1#bib.bib2), [3](https://arxiv.org/html/2510.26217v1#bib.bib3)].

We present a *domain-specific, certifiable* hybrid pipeline for CSA-governed collateral allocation that integrates document understanding, higher-order discrete optimization, and formal certification:

1. 1.

   *Evidence-gated CSA extraction.* An abstain-by-default LLM converts CSAs and related legal/financial documents into a normalized, CSA-aware JSON with span citations (thresholds, IA/IM, MTA, RA, eligibility and haircut matrices, regime selectors, caps, inventory metadata, scenarios).
2. 2.

   *Hybrid explorer with micro higher-order QAOA (HO-QAOA).* We interleave quantum-inspired simulated annealing with *micro-HO-QAOA* on binding sub-QUBOs (subset size n≤16n\!\leq\!16, interaction order k≤4k\!\leq\!4), explicitly encoding rounding/caps as higher-order terms to coordinate multi-asset moves that defeat local swaps. This aligns with recent evidence that higher-order QAOA outperforms quadratic QAOA on rugged finance landscapes [[10](https://arxiv.org/html/2510.26217v1#bib.bib10), [11](https://arxiv.org/html/2510.26217v1#bib.bib11)]. We cap k≤4k\!\leq\!4 to limit ancilla overhead and compilation depth.
3. 3.

   *Weighted, risk-aware objective with funding-priced overshoot.* We scalarize operational and risk trade-offs as

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | J=\displaystyle J\;= | BaseCost​\_​abs+λ​Movement\displaystyle\mathrm{BaseCost\\_abs}+\lambda\,\mathrm{Movement} |  | (1) |
   |  |  | +μ​CVaR+γ​(U−Reff)+.\displaystyle{}+\mu\,\mathrm{CVaR}+\gamma\,\bigl(U-R\_{\mathrm{eff}}\bigr)\_{+}. |  |

   Here λ\lambda prices execution/ops churn, μ\mu prices tail risk via CVaR, and γ\gamma prices funding on over-posted collateral (“overshoot”) consistent with LVA/FVA [[12](https://arxiv.org/html/2510.26217v1#bib.bib12), [13](https://arxiv.org/html/2510.26217v1#bib.bib13), [14](https://arxiv.org/html/2510.26217v1#bib.bib14), [15](https://arxiv.org/html/2510.26217v1#bib.bib15), [16](https://arxiv.org/html/2510.26217v1#bib.bib16), [17](https://arxiv.org/html/2510.26217v1#bib.bib17), [18](https://arxiv.org/html/2510.26217v1#bib.bib18)]. We also enforce an explicit coverage window U≤Reff+BU\!\leq\!R\_{\mathrm{eff}}{+}B to govern buffers.
4. 4.

   *CP-SAT certification with feasibility diagnostics.* The incumbent is *certified* (status, bounds, gap) under identical constraints, and a U-cap pre-check reports the minimal feasible buffer B⋆B^{\star} when windows are too tight.
5. 5.

   *Governance-grade artifacts.* We emit span citations, a valuation matrix audit, weight-provenance JSON, QUBO manifests (subset nn, order kk, depth pp), and CP-SAT traces (status, bounds, slacks) for auditability and reproducibility.

Upstream CSA-domain LLM.
As an upstream stage, we train a CSA-domain LLM to extract key terms from CSAs and related documents (Schedules, Credit Support Deeds, eligibility matrices). The model is evidence-gated (abstain-by-default with span citations) and emits the CSA-aware data model that directly feeds the optimizer (see *CSA-Aware Data Model*). Full training data, model architecture, and benchmarks are covered in a separate paper.

Weighted scalarization and provenance.
Our weighted formulation traces Pareto-efficient trade-offs [[12](https://arxiv.org/html/2510.26217v1#bib.bib12), [13](https://arxiv.org/html/2510.26217v1#bib.bib13)], with CVaR capturing tail exposure [[14](https://arxiv.org/html/2510.26217v1#bib.bib14)], movement reflecting execution frictions [[15](https://arxiv.org/html/2510.26217v1#bib.bib15)], and γ\gamma dailyizing funding spreads per LVA/FVA principles [[16](https://arxiv.org/html/2510.26217v1#bib.bib16), [17](https://arxiv.org/html/2510.26217v1#bib.bib17), [18](https://arxiv.org/html/2510.26217v1#bib.bib18)]. We calibrate (λ,μ,γ)(\lambda,\mu,\gamma) from observed ops costs, tail pricing, and funding bps, and record inputs/units in a weights-provenance artifact for governance.

Positioning and comparisons.
By targeting higher-order domain couplings (RA/MTA interactions and concentration caps) with micro-HO-QAOA, and certifying outcomes with CP-SAT, our pipeline improves cost–movement–tail frontiers on realistic government bond datasets and multi-CSA inputs.

## II Background and Related Work

### II-A Collateral Optimization

Classical formulations encode haircut schedules, eligibility, and concentration limits, with rounding to RA and MTA gating. Pricing practice introduces liquidity/funding adjustments: the Liquidity Valuation Adjustment (LVA) discounts cash collateral at rate rcr\_{c} vs. risk-free rr; FVA reflects funding costs on uncollateralized parts [[1](https://arxiv.org/html/2510.26217v1#bib.bib1)]. Operating models emphasize enterprise views and the six levers—Documentation, Automation, Transformation, Optimization, Mobilization, Segregation—[[3](https://arxiv.org/html/2510.26217v1#bib.bib3)]. We retain MILP/CP-SAT certification and augment exploration with quantum-inspired sampling and micro-HO-QAOA near binding corners, shaping the objective with movement penalties and Weighted-CVaR.

### II-B Related Work

LLMs for CSA extraction. Evidence-gated LLMs achieve 90%+90\%+ clause-level accuracy for thresholds, MTA, eligibility, and haircut schedules mapped to CDM-like schemas [[4](https://arxiv.org/html/2510.26217v1#bib.bib4)].
  
Collateral & liquidity efficiency. Guidance urges minimizing trapped liquidity, balancing movement, and reserving buffers [[5](https://arxiv.org/html/2510.26217v1#bib.bib5)].
  
Quantum(-inspired) optimization. QUBO mappings and NISQ-era methods motivate micro-QUBOs near binding constraints [[6](https://arxiv.org/html/2510.26217v1#bib.bib6), [7](https://arxiv.org/html/2510.26217v1#bib.bib7)].
  
Hybrid solvers. QAOA/VQE sampling paired with classical local search improves quality under resource limits [[8](https://arxiv.org/html/2510.26217v1#bib.bib8)]. Hardware performance milestones suggest headroom for small structured QAOA in workflows [[9](https://arxiv.org/html/2510.26217v1#bib.bib9)].
  
Higher-order QAOA for finance. Closest to our setting, Uotila, Ripatti, and Zhao extend QAOA to *higher-order* (HUBO) portfolio optimization and report 15–25% gains over vanilla (quadratic) QAOA on rugged financial landscapes for n=8n{=}8–2424 variables on NISQ simulators [[10](https://arxiv.org/html/2510.26217v1#bib.bib10), [11](https://arxiv.org/html/2510.26217v1#bib.bib11)]. Their formulation explicitly models multi-asset interactions (e.g., covariance/risk and cardinality) as k>2k{>}2 terms and uses *order-aware partitioning* and spectral grouping to set subset sizes nn (base n=8n{=}8–1212 for k=2k{=}2, add 44–88 for constraints). We borrow three elements: (i) treating CSA caps/eligibility and MTA/rounding couplings as higher-order penalties in micro-HO-QAOA (e.g., using k=3k{=}3 terms to model window/MTA interactions and multi-cap couplings); (ii) selecting n≈8n\!\approx\!8–1616 via spectral clustering of highly coupled lots, which aligns with their nn recommendations and our ancilla budget; and (iii) warm-starting quantum jumps from a classical incumbent (our CP-SAT/SA incumbent), which their results show mitigates barren plateaus. Conceptually, their “integer shares” mirror our discrete lots xix\_{i}, and their eligibility screens map to our CSA-based haircut/eligibility flags, making their method particularly applicable to ISDA-CSA collateral allocation.
  
Benchmarking and noisy regimes.
Recent studies benchmark QAOA/HO-QAOA and related hybrids for finance portfolios in noisy settings, including VQE-style variants and noise-aware compilations (add exact citations). We position our *micro*-HO-QAOA as a targeted jump operator embedded in a certified pipeline rather than a stand-alone solver, and we cap k≤4k\!\leq\!4 to control ancilla overhead.

## III Problem Formulation

We pick integer lots xi∈ℤ≥0x\_{i}\!\in\!\mathbb{Z}\_{\geq 0} for eligible assets ii with after-haircut value viv\_{i} and daily carry cost cic\_{i}. Coverage U=∑ivi​xiU=\sum\_{i}v\_{i}x\_{i}. The effective requirement uses RA rounding:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Reff=⌈max⁡(E−T−IA−IM, 0)RA⌉​RA.R\_{\mathrm{eff}}=\Big\lceil\tfrac{\max(E-T-\mathrm{IA}-\mathrm{IM},\,0)}{\mathrm{RA}}\Big\rceil\mathrm{RA}. |  | (2) |

We enforce U≥ReffU\!\geq\!R\_{\mathrm{eff}}, an optional cap U≤Reff+BU\!\leq\!R\_{\mathrm{eff}}{+}B, and cash/issuer/class/currency/global caps.

#### Objective.

|  |  |  |  |
| --- | --- | --- | --- |
|  | min⁡J=\displaystyle\min\;J\;=\; | ∑ici​xi+λ​‖x−h‖1\displaystyle\sum\_{i}c\_{i}x\_{i}\;+\;\lambda\,\|x-h\|\_{1} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +μCVaR(Lx)+γ(U−Reff)+.\displaystyle+\;\mu\,\mathrm{CVaR}\_{(}Lx)\;+\;\gamma\,(U-R\_{\mathrm{eff}})\_{+}. |  | (3) |

CVaR uses a linearization (τ,zs)(\tau,z\_{s}) with scenario weights ∑sws=1\sum\_{s}w\_{s}\!=\!1.

#### Binary/QUBO view.

Integer lots are encoded via bounded binaries yi​ℓ∈{0,1}y\_{i\ell}\!\in\!\{0,1\} s.t. xi=∑ℓ=1miyi​ℓx\_{i}=\sum\_{\ell=1}^{m\_{i}}y\_{i\ell} with per-lot valuation vi​ℓ=viv\_{i\ell}\!=\!v\_{i} and costs ci​ℓ=cic\_{i\ell}\!=\!c\_{i}.

#### HO-QAOA definition and (n,k)(n,k) roles.

We construct a higher-order Ising Hamiltonian

|  |  |  |
| --- | --- | --- |
|  | HP=∑jaj​Zj+∑j<kbj​k​Zj​Zk+∑j<k<ℓcj​k​ℓ​Zj​Zk​Zℓ+⋯H\_{P}\;=\;\sum\_{j}a\_{j}Z\_{j}\;+\;\sum\_{j<k}b\_{jk}Z\_{j}Z\_{k}\;+\;\sum\_{j<k<\ell}c\_{jk\ell}Z\_{j}Z\_{k}Z\_{\ell}\;+\;\cdots |  |

where higher-order (k≥3k\!\geq\!3) terms encode multi-asset interactions from caps (issuer/class/currency/global), window coupling (UU near ReffR\_{\mathrm{eff}}), and lot granularity. The *order* kk denotes the maximum Pauli-ZZ tensor product degree needed to represent constraints/objective couplings in the subproblem. We use a *micro-HO-QAOA* on *subsets* of variables of size nn (typically 8−168\!-\!16) selected near binding corners. The HO-QAOA state of depth pp is

|  |  |  |
| --- | --- | --- |
|  | |γ,β⟩=∏ℓ=1p(e−i​βℓ​∑jXj​e−i​γℓ​HP)​|+⟩⊗n,|\gamma,\beta\rangle\;=\;\prod\_{\ell=1}^{p}\Big(e^{-i\beta\_{\ell}\sum\_{j}X\_{j}}\;e^{-i\gamma\_{\ell}H\_{P}}\Big)\,|+\rangle^{\otimes n}, |  |

with standard XX-mixer; higher-order phase operators e−i​γℓ​Zj1​⋯​Zjke^{-i\gamma\_{\ell}Z\_{j\_{1}}\cdots Z\_{j\_{k}}} are compiled either directly or via ancillas. For k>2k>2, ancilla qubits linearize/multiply higher moments; if ancillas inflate the subset above nmaxn\_{\max}, we skip the quantum jump for that iteration and log the reason.

Impact of nn. Larger nn captures more coupled moves across caps/rounding but increases circuit width and optimizer complexity; empirically, n∈[8,16]n\in[8,16] balances expressivity and run time, reliably crossing rugged neighborhoods that defeat local swaps.
Order/size crosswalk. Our practical caps (k≤4k\!\leq\!4) and subset limits (n≤16n\!\leq\!16) follow the order-aware guidance observed in higher-order finance QAOA benchmarks, which report best empirical trade-offs around n≈12n\!\approx\!12–1818 for k>2k{>}2 on rugged landscapes with warm starts [[10](https://arxiv.org/html/2510.26217v1#bib.bib10), [11](https://arxiv.org/html/2510.26217v1#bib.bib11)].

Impact of kk. Higher kk allows direct encoding of multi-way caps and overshoot couplings; however, gate compilation depth and noise rise with kk. We cap at k≤4k\!\leq\!4 in practice; above this, we fall back to classical exploration.

## IV CSA-Aware Data Model

As an upstream stage, we train a CSA-domain LLM to extract key terms from CSAs and related financial/legal documents (e.g., Schedules, Credit Support Deeds, annexed eligibility matrices). The model is evidence-gated (abstain-by-default with span citations) and emits a normalized, CSA-aware data model that includes terms (Threshold, IA/IM, MTA, RA), eligibility and haircut matrices, regime selectors, concentration caps, inventory metadata, and scenario inputs.We standardize those extraction parameters as inputs/outputs in a governance-ready JSON schema. Key fields:

### IV-A Counterparty & Legal

* •

  csa.meta: governing law (NY/English), bilateral/one-way.
* •

  csa.terms: Threshold TT, Independent Amount IA\mathrm{IA}, Initial Margin IM\mathrm{IM}, Minimum Transfer Amount (MTA), Rounding Amount (RA), Base Currency, FX conventions.
* •

  csa.regime: valuation regime selector in Schedule A; the default may be overridden per asset bucket.

  + –

    sp: S&P column (sp\_pct)
  + –

    m1: Moody’s First (m1\_pct)
  + –

    m2: Moody’s Second (m2\_pct)

### IV-B Valuation Haircuts and Eligibility

* •

  haircuts.matrix: haircut percentage indexed by (ICAD,bucket,regime)(\mathrm{ICAD},\ \mathrm{bucket},\ \mathrm{regime}).
* •

  eligibility.scheduleA: eligible asset classes and buckets (Govt, Agency, Corp, MBS, TIPS, Cash), issuer ratings/tenor constraints.

### IV-C Caps and Windows

* •

  caps: cash\_cap (e.g., 20%20\% of UU), issuer\_cap, class\_cap, currency\_cap, global\_cap.
* •

  window: policy buffer BB (bps or $), optional hard coverage cap U≤Reff+BU\leq R\_{\mathrm{eff}}+B.

### IV-D Exposure and Scenarios

* •

  exposure: EE (base currency) and timestamp; optional path of EtE\_{t} for rolling re-optimization.
* •

  scenarios: matrix LL (per-asset loss/PNL across scenarios) with weights wsw\_{s} (normalized for CVaR).

### IV-E Inventory and Costs

* •

  inventory: items with id, class, issuer, bucket, currency, price, unit, current lots hih\_{i}, and per-lot valuation viv\_{i} after haircut.
* •

  costs: daily carry cic\_{i} ($/lot/day), operational move cost unit for movement.

### IV-F Weights and Provenance

* •

  weights: (λ,μ,γ)(\lambda,\mu,\gamma) with calibration inputs and units: λ\lambda (ops amortization per lot over horizon), μ\mu (price per $MM CVaR per day), γ\gamma (funding bps →\to daily carry).
* •

  weights\_provenance: calibration inputs (ops move cost, horizon days, CVaR price, funding bps), hash, and timestamp.

### IV-G Governance/Audit Toggles

* •

  audit.flags: enable span citations, valuation audit, QUBO manifests, CP-SAT traces.
* •

  solver.limits: SA iterations, HO-QAOA nmaxn\_{\max}, kmaxk\_{\max}, depth pp, and wall constraints.

## V Hybrid Pipeline (Explore →\rightarrow Prove →\rightarrow Explain/Audit)

We create the full workflow with four phases:

### V-A Phase 1: Explore (Search)

1. 1.

   Initialization: Compute ReffR\_{\mathrm{eff}} via ([2](https://arxiv.org/html/2510.26217v1#S3.E2 "In III Problem Formulation ‣ Hybrid LLM + Higher-Order Quantum Approximate Optimization for CSA Collateral Management")); derive per-lot viv\_{i} from haircuts; seed with BL-1 (density greedy).
2. 2.

   Local search: Simulated annealing (integer neighborhoods; add/swap/remove) with feasibility repair (caps, RA, MTA, window).
3. 3.

   Spectral subset selection: Build a unitless interaction graph (dual/gradient proxies, feasibility slacks) and pick top-KK nodes by |dual||\mathrm{dual}|; prune edges by ε\varepsilon to stabilize.
4. 4.

   Micro-HO-QAOA jump: If improvement <0.3%<\!0.3\% over SS SA steps, form a sub-QUBO on n≤16n\!\leq\!16 variables (with ancillas if k>2k\!>\!2) and perform one HO-QAOA jump (depth pp); accept if JJ decreases and feasibility holds; otherwise revert.Please see the Algorith 1: Micro-HO-QAOA Jump (Explore).

### V-B Phase 2: Prove (Certification)

We pass the incumbent to CP-SAT with the same constraints and objective components (linearized CVaR and overshoot). We report: status (OPTIMAL/FEASIBLE/INFEASIBLE), incumbent/best bound, MIP gap, and per-constraint slacks.

Algorithm 1  Micro-HO-QAOA Jump (Explore)

1incumbent xx, objective JJ, graph GG, limits (nmax,kmax,p)(n\_{\max},k\_{\max},p), plateau (S,ϵ)(S,\epsilon), optional angles (γ1:p(0),β1:p(0))(\gamma^{(0)}\_{1:p},\beta^{(0)}\_{1:p})

2if Plateau(x,S,ϵ)=false(x,S,\epsilon)=\textsc{false} then

3  return xx

4S←SpectralSelect​(G,nmax)S\leftarrow\textsc{SpectralSelect}(G,n\_{\max}) ⊳\triangleright |S|≤nmax|S|\!\leq\!n\_{\max} (typ. 8–16)

5HP←BuildHubo​(S,kmax)H\_{P}\leftarrow\textsc{BuildHubo}(S,k\_{\max}) ⊳\triangleright RA/MTA, window, caps; ancillas for k>2k{>}2

6w←AncillaWidth​(HP)w\leftarrow\textsc{AncillaWidth}(H\_{P})

7if w>nmaxw>n\_{\max} then

8  return xx ⊳\triangleright skip jump; continue SA + repair

9|ψ|←PREP​(w)|\psi|\leftarrow\textsc{PREP}(w); optionally (γℓ,βℓ)←(γℓ(0),βℓ(0))(\gamma\_{\ell},\beta\_{\ell})\leftarrow(\gamma^{(0)}\_{\ell},\beta^{(0)}\_{\ell})

10for ℓ=1\ell=1 to pp do ⊳\triangleright mixer ramp allowed

11  |ψ|←MIX​(βℓ)​(PHASE​(γℓ,HP)​(|ψ|))|\psi|\leftarrow\textsc{MIX}(\beta\_{\ell})\big(\textsc{PHASE}(\gamma\_{\ell},H\_{P})(|\psi|)\big)

12z∼|ψ|z\sim|\psi|; y←MapLots​(z)y\leftarrow\textsc{MapLots}(z) ⊳\triangleright ancillas→\tovars

13y←Repair​(y)y\leftarrow\textsc{Repair}(y) ⊳\triangleright caps/RA/MTA/window

14x~←x\tilde{x}\leftarrow x; x~S←yS\tilde{x}\_{S}\leftarrow y\_{S}

15if Feasible(x~)(\tilde{x}) and J​(x~)<J​(x)J(\tilde{x})<J(x) then

16  return x~\tilde{x} ⊳\triangleright accept

17else

18  return xx ⊳\triangleright reject

### V-C Phase 3/4: Explain & Audit (Governance)

We emit governance HTML with: objective breakdown; valuation matrix audit; weight provenance; spectral/QUBO manifests (subsets, n,k,pn,k,p); and CP-SAT traces (status, bounds, slacks). Reproducibility hashes and seeds are included.

### V-D Baselines and Feasibility (Overshoot & B⋆B^{\star})

#### Baselines.

We benchmark three progressively stronger heuristics:

* •

  BL-1 (density greedy, cap-safe): ranks assets by cost-to-valuation density and fills to the window under caps; fast, but can stall near binding corners.
* •

  BL-2 (bucket-first greedy + repair): prioritizes bucket/cap compliance during greedy fill, then repairs to align with the window; tighter coverage, typically higher movement.
* •

  BL-3 (BL-1 seed + 2-opt swaps): starts from BL-1 and applies local pairwise swaps to reduce cost while respecting feasibility; strong local polish, but prone to plateaus.

Hybrid. Uses BL-3 as a seed, then interleaves simulated annealing with a spectral micro-HO-QAOA jump to cross binding constraints and escape BL-3 plateaus, followed by local repair for feasibility.

#### Overshoot and Feasibility

Because lots are discrete, U=ReffU{=}R\_{\mathrm{eff}} is rare. We compute a minimal feasible buffer B⋆B^{\star} by (i) building any feasible cover without the UU-cap, then (ii) greedily reducing UU while preserving caps/RA. If the user-specified buffer B<B⋆B\!<\!B^{\star}, we flag infeasible\_u\_cap and report B⋆B^{\star} (USD and bps). The objective’s overshoot penalty γ​(U−Reff)+\gamma\,\bigl(U-R\_{\mathrm{eff}}\bigr)\_{+} trades off carry versus buffer.

## VI Case Study

### VI-A CSA Summary

Governing law. 2009 New York–law CSA, bilateral.
  
Base currency & eligibility. USD base; USD/EUR cash and securities per Schedule A (government, agencies, corporates, TIPS, MBS), valuation by rating/tenor.
  
Threshold/MTA/Rounding. T=0T\!=\!0, IA=0\mathrm{IA}\!=\!0, IM=0\mathrm{IM}\!=\!0; MTA =$​100,000=\mathdollar 100{,}000; RA =$​10,000=\mathdollar 10{,}000.
  
Valuation regime. Moody’s First (m1) default; S&P (sp) and Moody’s Second (m2) available.
  
Operational caps. Buffer B=B{=}25 bps of ReffR\_{\mathrm{eff}}; cash cap =20%=20\% of UU.
  
Exposure. E=$​130,340,000E=\mathdollar 130{,}340{,}000; ReffR\_{\mathrm{eff}} computed via ([2](https://arxiv.org/html/2510.26217v1#S3.E2 "In III Problem Formulation ‣ Hybrid LLM + Higher-Order Quantum Approximate Optimization for CSA Collateral Management")).
  
Inventory proxy. USD cash and UST ladder (6M–20Y), TIPS, Agency, AAA MBS, IG Corps; per-lot viv\_{i} after haircuts; lots aligned to RA (cash) and $1MM coupons (bonds).

### VI-B Valuation Regimes

We consider sp, m1 (default), and m2, using the Schedule A matrix for haircuts.

### VI-C Objective and Constraints (shared)

Minimize J=BaseCost​\_​abs+λ​Movement+μ​CVaR+γ​OvershootJ=\mathrm{BaseCost\\_abs}+\lambda\,\mathrm{Movement}+\mu\,\mathrm{CVaR}+\gamma\,\mathrm{Overshoot}, subject to Reff≤U≤Reff+BR\_{\mathrm{eff}}\leq U\leq R\_{\mathrm{eff}}{+}B, cash cap, and integer-lot availability. Units: BaseCost\_abs [$/day], Movement [lots], CVaR and Overshoot [$].

### VI-D How to Choose Weights (practical guidance)

We calibrate (λ,μ,γ)(\lambda,\mu,\gamma) from operational inputs: (i) per-lot Ops move cost and amortization horizon ⇒λ\Rightarrow\lambda, (ii) daily price for 1$MM CVaR ⇒μ\Rightarrow\mu, (iii) annual funding bps ⇒γ\Rightarrow\gamma via day-count. Each run logs a weights\_provenance.json (inputs, units, calibrated triplet, hash).

### VI-E CP-SAT Results and Meaning

CP-SAT returns OPTIMAL when the incumbent attains the global minimum and the MIP gap is zero; FEASIBLE when a feasible incumbent exists with a nonzero bound-gap; INFEASIBLE when no solution satisfies caps/window/RA. For each case we report per-constraint slacks (cash/issuer/class/currency/global), confirming which limits bind.

### VI-F Harness Setups and Results

We analyze three scenarios. Across harnesses A/B/C, the Hybrid improves the BL-3 objective by 9.1%, 9.6%, and 10.7%, respectively (see tables below).

* •

  Units: BaseCost\_abs [$/day], Movement [lots], CVaR0.90/Overshoot/UsedValue [$]; all rounded to 2 dp.
* •

  CVaR weights normalized (∑w=1.0\sum w=1.0); governance HTML warns if renormalization occurred.
* •

  Weight provenance (.json) and valuation audit are linked in each governance HTML.

#### Harness A: m1, buffer 25 bps, cash cap 20%, practical weights.

| Model | BaseCost | Movement | CVaR | Overshoot | JJ |
| --- | --- | --- | --- | --- | --- |
| BL-1 | 100.0 | 28 | 540,000 | 210,000 | 1,12x |
| BL-2 | 99.1 | 35 | 528,000 | 195,000 | 1,10x |
| BL-3 | 98.7 | 24 | 520,000 | 182,000 | 1,00x |
| Hybrid | 98.4 | 22 | 515,000 | 155,000 | 0.91x |

* •

  Configuration: m1 regime; buffer B=0.25%B=0.25\% of ReffR\_{\mathrm{eff}}; cash cap =20%=20\% of UcapU\_{\mathrm{cap}}; weights ≈(λ,μ,γ)=(30.0, 0.001, 1.39×10−5​day−1)\approx(\lambda,\mu,\gamma)=(30.0,\;0.001,\;1.39\times 10^{-5}\ \text{day}^{-1}).
* •

  Intent: “Everyday” governance settings with moderate funding and moderate tail price; tests balanced trade-offs.
* •

  Effect:

  + –

    γ\gamma penalizes overshoot enough to cut excess usage without exploding Movement.
  + –

    μ\mu applies light tail pressure; λ\lambda moderates lot churn.
  + –

    Subset size nn stays ≈8\approx 8–1616; must-jump triggers rarely.
* •

  Result (vs BL-3): Hybrid improves Objective by ≈9.1%\approx 9.1\% with lower *Movement* and *Overshoot*; breakdown shows most gains from γ⋅Overshoot\gamma\!\cdot\!\text{Overshoot}, with some from μ⋅CVaR\mu\!\cdot\!\mathrm{CVaR}.

*Conclusion:* Hybrid reduces JJ by ≈9.1%\approx 9.1\% vs BL-3, primarily by trimming Overshoot at similar BaseCost and slightly lower Movement.

#### Harness B: m1, buffer 10 bps, cash cap 15%, tight-liquidity weights (higher γ\gamma).

| Model | BaseCost | Movement | CVaR | Overshoot | JJ |
| --- | --- | --- | --- | --- | --- |
| BL-1 | 101.3 | 31 | 556,000 | 132,000 | 1,14x |
| BL-2 | 100.6 | 37 | 544,000 | 121,000 | 1,11x |
| BL-3 | 100.2 | 25 | 536,000 | 113,000 | 1,00x |
| Hybrid | 100.0 | 24 | 533,000 | 91,000 | 0.904x |

* •

  Configuration: m1; buffer B=0.10%B=0.10\%; cash cap =15%=15\%; weights ≈(λ,μ,γ)=(28.57, 0.0025, 2.22×10−5​day−1)\approx(\lambda,\mu,\gamma)=(28.57,\;0.0025,\;2.22\times 10^{-5}\ \text{day}^{-1}).
* •

  Intent: Tighter liquidity and higher funding pressure; tests robustness when overshoot is expensive and buffer small.
* •

  Effect:

  + –

    Larger γ\gamma materially suppresses overshoot, trading some BaseCost/Movement.
  + –

    Higher μ\mu drives tail reduction; λ\lambda still curbs churn.
  + –

    n≈8n\approx 8–1616; must-jump fires more often to escape SA plateaus.
* •

  Result (vs BL-3): Hybrid improves Objective by ≈9.6%\approx 9.6\%; gains mainly from γ⋅Overshoot\gamma\!\cdot\!\text{Overshoot} and μ⋅CVaR\mu\!\cdot\!\mathrm{CVaR}, with Movement contained by λ\lambda.

*Conclusion:* With tighter buffer and cash cap, overshoot control dominates. The must-jump rule breaks SA plateaus; JJ improves ≈9.6%\approx 9.6\% vs BL-3.

#### Harness C: m2, buffer 25 bps, cash cap 20%, practical weights.

| Model | BaseCost | Movement | CVaR | Overshoot | JJ |
| --- | --- | --- | --- | --- | --- |
| BL-1 | 99.5 | 27 | 501,000 | 204,000 | 1,13x |
| BL-2 | 99.0 | 33 | 492,000 | 193,000 | 1,08x |
| BL-3 | 98.6 | 23 | 485,000 | 178,000 | 1,00x |
| Hybrid | 98.3 | 22 | 480,000 | 149,000 | 0.893x |

* •

  Configuration: m2; buffer B=0.25%B=0.25\%; cash cap =20%=20\%; weights ≈(λ,μ,γ)=(30.0, 0.001, 1.39×10−5​day−1)\approx(\lambda,\mu,\gamma)=(30.0,\;0.001,\;1.39\times 10^{-5}\ \text{day}^{-1}).
* •

  Intent: Regime sensitivity with tighter haircuts; tests ability to coordinate under higher required usage/tail.
* •

  Effect:

  + –

    Tighter valuations raise UsedValue and CVaR; Hybrid’s spectral n≈8n\approx 8–1616 helps cross binding corners (window/caps/lot granularity).
  + –

    Must-jump occasionally assists when caps bind.
* •

  Result (vs BL-3): Hybrid improves Objective by ≈10.7%\approx 10.7\%; breakdown shows meaningful γ⋅Overshoot\gamma\!\cdot\!\text{Overshoot} and μ⋅CVaR\mu\!\cdot\!\mathrm{CVaR} reductions while keeping Movement controlled.

*Conclusion:* Under tighter m2 haircuts, Hybrid improves JJ by ≈10.7%\approx 10.7\% vs BL-3, keeping nn within 8–16 via spectral capping.

### VI-G Weight Selection: Why These Numbers

We target business trade-offs: (i) if Ops capacity is constrained, increase λ\lambda to suppress Movement; (ii) if funding costs dominate, raise γ\gamma to push U↓U\downarrow (less overshoot); (iii) if tail discipline is paramount, raise μ\mu (CVaR), accept modest BaseCost/Motion increases. Calibration is documented in the weight provenance blob and mirrored in governance HTML.

## VII Governance

We produce:

* •

  Span citations (LLM extraction): prompt hash and source spans for each clause (Threshold, MTA, RA, eligibility, haircuts).
* •

  Valuation matrix audit: table mapping *instrument* →\rightarrow *ICAD/bucket/regime* →\rightarrow *haircut%* →\rightarrow viv\_{i} for full reproducibility.
* •

  Weight provenance: calibration inputs/units and (λ,μ,γ)(\lambda,\mu,\gamma), with hashes/timestamps.
* •

  QUBO manifests: for each jump: subset IDs, n,k,pn,k,p, compiled terms, and acceptance decision.
* •

  CP-SAT traces: status (OPTIMAL/FEASIBLE/INFEASIBLE), incumbent, best bound, gap, and per-constraint slacks (cash/issuer/class/currency/global); infeasible windows include B⋆B^{\star}.

## VIII Ablations

Spectral stability. Bounding edge weights to [0,1][0,1] and ε\varepsilon-pruning yield stable cluster selection; without pruning, acceptance variance rises.
  
Subset size nn and cap. Performance saturates around n≈12n\!\approx\!12; n<8n{<}8 underfits multi-way caps; n>16n{>}16 adds overhead and ancilla pressure with diminishing returns. We hard-cap n≤16n\!\leq\!16.
  
Order kk and ancillas. Enabling k=3k\!=\!3 captures issuer/class/currency triples and RA/MTA window couplings; k=4k{=}4 further improves near tight windows at higher compilation cost. We cap k≤4k\!\leq\!4 to contain ancilla-expanded width.
  
γ/μ\gamma/\mu sweeps. Increasing γ\gamma drives overshoot ↓\downarrow and BaseCost ↑\uparrow monotonically; increasing μ\mu reduces tail exposure with modest Movement increase. Hybrid dominates BL-3 along both trade-off frontiers.
  
Must-jump rule. Enforcing at least one HO-QAOA jump after SS low-improvement SA steps avoids long plateaus and drives consistent Overshoot reductions.

Weighted-CVaR. Pricing tails (μ>0\mu>0) smooths the BaseCost–Overshoot frontier and reduces solution churn across scenario sets; renormalization warnings are emitted if ∑sws≠1\sum\_{s}w\_{s}\neq 1 and auto-fixed.
  
Overshoot penalty γ\gamma. Sweeps show monotone Overshoot↓\downarrow and BaseCost↑\uparrow; Hybrid dominates BL-3 along this frontier, indicating effective cross-cap coordination.
  
Fallback behavior. If ancillas inflate nn past nmaxn\_{\max} or compilation fails, the iteration logs a skip and reverts to SA/BL-3 neighborhoods; solution quality degrades gracefully.

## IX Conclusion

We presented a domain-specific, certifiable hybrid optimizer for CSA-governed collateral that unifies evidence-gated CSA extraction, quantum-inspired search, and higher-order QAOA micro-jumps with CP-SAT certification. By encoding RA/MTA interactions and concentration limits as higher-order couplings, our method coordinates discrete lot moves that defeat purely local heuristics, while a weighted objective (movement, CVaR, funding-priced overshoot) captures the operational and risk economics of posting. Across realistic government bond datasets and multi-CSA inputs, the pipeline—*extract, explore, certify, audit*—consistently improves cost–movement–tail frontiers over strong classical baselines and yields governance-grade artifacts suitable for operational sign-off.

## References

* [1]

  B. Genest, D. Rego, and H. Freon, “Collateral Optimization: Liquidity & Funding Value Adjustments, Best Practices,” *MPRA Paper No. 62908*, 2013. [Online]. Available: <https://mpra.ub.uni-muenchen.de/62908/>
* [2]

  EY, “Collateral optimization: Capabilities that drive financial resource efficiency,” Ernst & Young LLP, 2020. [Online]. Available: <https://assets.ey.com/content/dam/ey-sites/ey-com/en_us/topics/banking-and-capital-markets/ey-collateral-optimization.pdf>
* [3]

  PwC, “Collateral Management Transformation: Dynamic changes in the collateral ecosystem,” PricewaterhouseCoopers Co., Ltd., 2015. [Online]. Available: <https://www.pwc.com/jp/en/industries/financial-services/assets/collateral-management-transformation.pdf>
* [4]

  International Swaps and Derivatives Association (ISDA),
  “Benchmarking Generative AI for CSA Clause Extraction and CDM Representation,” May 2025. [Online]. Available: <https://www.isda.org/2025/05/15/benchmarking-generative-ai-for-csa-clause-extraction-and-cdm-representation/>
* [5]

  ISDA Future Leaders in Derivatives,
  “Collateral and Liquidity Efficiency in the Derivatives Market,” May 2025. [Online]. Available: <https://www.isda.org/2025/05/15/isda-future-leaders-in-derivatives-publishes-whitepaper-on-collateral-and-liquidity-efficiency/>
* [6]

  Various Authors, “Collateral Portfolio Optimization in Crypto-Backed Stablecoins,” arXiv:2405.08305, 2024. [Online]. Available: <https://arxiv.org/abs/2405.08305>
* [7]

  Various Authors, “Approaching Collateral Optimization for NISQ and Quantum-Inspired Computing,” arXiv:2305.16395, 2023. [Online]. Available: <https://arxiv.org/abs/2305.16395>
* [8]

  Various Authors, “Solving Combinatorial Optimization and ML Problems Using Hybrid Quantum–Classical Systems,” *Future Generation Computer Systems*, 2025 (early access). [Online]. Available: <https://www.sciencedirect.com/science/article/pii/S0167739X25002298>
* [9]

  IonQ Inc., “IonQ Achieves Record Breaking Quantum Performance Milestone of #AQ 64,” Press release, Sept. 2025. [Online]. Available: <https://investors.ionq.com/news/news-details/2025/IonQ-Achieves-Record-Breaking-Quantum-Performance-Milestone-of-AQ-64/default.aspx>
* [10]

  V. Uotila, J. Ripatti, and B. Zhao, “Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm,” in *Proc. IEEE Quantum Week (QCE)*, 2025. [Online]. Available: <https://qce.quantum.ieee.org/2025/program/paper-schedule/>
* [11]

  V. Uotila, J. Ripatti, and B. Zhao, “Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm,” *arXiv:2509.01496*, Sept. 2025. [Online]. Available: <https://arxiv.org/abs/2509.01496>
* [12]

  K. Miettinen, *Nonlinear Multiobjective Optimization*. Kluwer, 1999.
* [13]

  S. Boyd and L. Vandenberghe, *Convex Optimization*. Cambridge University Press, 2004.
* [14]

  R. T. Rockafellar and S. Uryasev, “Optimization of Conditional Value-at-Risk,” *Journal of Risk*, vol. 2, no. 3, pp. 21–41, 2000.
* [15]

  R. Almgren and N. Chriss, “Optimal Execution of Portfolio Transactions,” *Journal of Risk*, vol. 3, no. 2, pp. 5–39, 2000.
* [16]

  V. Piterbarg, “Funding beyond discounting: Collateral agreements and derivatives pricing,” *Risk Magazine*, vol. 23, no. 2, pp. 97–102, 2010.
* [17]

  B. Genest, D. Rego, and H. Freon, “Collateral Optimization: Liquidity & Funding Value Adjustments, Best Practices,” *MPRA Paper No. 62908*, 2013. Available: <https://mpra.ub.uni-muenchen.de/62908/>
* [18]

  L. Andersen and D. Duffie, “Funding Value Adjustments,” *NBER Working Paper No. 23680*, 2017. Available: <https://www.nber.org/papers/w23680>