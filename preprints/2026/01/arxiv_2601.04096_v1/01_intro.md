---
authors:
- Riley James Bendel
doc_id: arxiv:2601.04096v1
family_id: arxiv:2601.04096
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Sharp Transitions and Systemic Risk in Sparse Financial Networks
url_abs: http://arxiv.org/abs/2601.04096v1
url_html: https://arxiv.org/html/2601.04096v1
venue: arXiv q-fin
version: 1
year: 2026
---


Riley James Bendel
  
Independent Researcher
  
rileyjbendel@protonmail.com

(2026)

###### Abstract

We study contagion and systemic risk in sparse financial networks with balance-sheet interactions on a directed random graph. Each institution has homogeneous liabilities and equity, and exposures along outgoing edges are split equally across counterparties. A linear fraction of institutions have zero out-degree in sparse digraphs; we adopt an external-liability convention that makes the exposure mapping well-defined without altering propagation. We isolate a single-hit transmission mechanism and encode it by a sender-truncated subgraph Gs​hG\_{sh}. We define adversarial and random systemic events with shock size kn=⌈c​log⁡n⌉k\_{n}=\lceil c\log n\rceil and systemic fraction ε​n\varepsilon n. In the subcritical regime ρo​u​t<1\rho\_{out}<1, we prove that maximal forward reachability in Gs​hG\_{sh} is O​(log⁡n)O(\log n) whp, yielding O​((log⁡n)2)O((\log n)^{2}) cascades from shocks of size knk\_{n}. For random shocks, we give an explicit fan-in (multi-hit) accumulation bound, showing that multi-hit defaults are negligible whp when the explored default set is polylogarithmic. In the supercritical regime, we give an exact distributional representation of Gs​hG\_{sh} as an i.i.d.-outdegree random digraph with uniform destinations, placing it directly within the scope of the strong-giant/bow-tie theorem of Penrose (2014). We derive the resulting implication for random-shock systemic events. Finally, we explain why sharp-threshold machinery does not directly apply: systemic-event properties need not be monotone in the edge set because adding outgoing edges reduces per-edge exposure.

#### Proof roadmap.

The paper proceeds in four steps. First, the balance-sheet model and cascade dynamics are fixed, including a convention that makes exposures well-defined for zero out-degree institutions without affecting propagation. Second, a single-hit transmission mechanism is isolated and encoded by the sender-truncated graph Gs​hG\_{sh}, allowing contagion to be studied via forward reachability. Third, in the subcritical regime ρo​u​t<1\rho\_{out}<1, forward exploration in Gs​hG\_{sh} is controlled by a subcritical branching process, and a deferred-decisions argument shows that multi-hit accumulation is negligible when the explored set is polylogarithmic. Finally, in the supercritical regime ρo​u​t>1\rho\_{out}>1, the distribution of Gs​hG\_{sh} is identified with an i.i.d.-outdegree random digraph, placing it within the scope of existing strong-giant results and yielding the random-shock systemic threshold.

## 1 Model and Definitions

### 1.1 Network

Let [n]:={1,…,n}[n]:=\{1,\dots,n\}. Let G∼G​(n,λ/n)G\sim G(n,\lambda/n) be a directed Erdős–Rényi graph: for each ordered pair (u,v)(u,v) with u≠vu\neq v, (u→v)(u\to v) is present independently with probability λ/n\lambda/n.

### 1.2 Balance-sheet primitives

#### Liabilities.

Each institution has total nominal liabilities L>0L>0.

#### Leverage and equity.

Fix C>1C>1 and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | E:=LC−1.E:=\frac{L}{C-1}. |  | (1) |

#### Recovery.

We assume zero recovery.

### 1.3 Degree-zero closure

###### Assumption 1 (External liabilities for do​u​t=0d^{out}=0).

If dGo​u​t​(u)=0d^{out}\_{G}(u)=0, then uu has no interbank out-exposures; its liabilities are owed to an external sector.

###### Lemma 1 (Prevalence of do​u​t=0d^{out}=0).

For each fixed uu, dGo​u​t​(u)⇒Pois​(λ)d^{out}\_{G}(u)\Rightarrow\mathrm{Pois}(\lambda) and

|  |  |  |
| --- | --- | --- |
|  | ℙ​(dGo​u​t​(u)=0)→e−λ.\mathbb{P}(d^{out}\_{G}(u)=0)\to e^{-\lambda}. |  |

### 1.4 Interbank exposures

If dGo​u​t​(u)≥1d^{out}\_{G}(u)\geq 1, each outgoing edge carries exposure

|  |  |  |  |
| --- | --- | --- | --- |
|  | wu→v:=LdGo​u​t​(u).w\_{u\to v}:=\frac{L}{d^{out}\_{G}(u)}. |  | (2) |

### 1.5 Cascade dynamics

Given S0⊂[n]S\_{0}\subset[n], define D0:=S0D\_{0}:=S\_{0} and iterate

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt+1:=Dt∪{v∉Dt:∑u∈Dt:(u→v)∈E​(G)wu→v≥E}.D\_{t+1}:=D\_{t}\cup\left\{v\notin D\_{t}:\ \sum\_{u\in D\_{t}:(u\to v)\in E(G)}w\_{u\to v}\geq E\right\}. |  | (3) |

###### Definition 1 (Terminal default set).

D∞​(S0):=⋃t≥0DtD\_{\infty}(S\_{0}):=\bigcup\_{t\geq 0}D\_{t}.

## 2 Single-Hit Mechanism and Gs​hG\_{sh}

###### Definition 2 (Single-hit cutoff).

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | d⋆​(C):=max⁡{d∈ℕ:d≥1,Ld≥E}=⌊LE⌋.d^{\star}(C):=\max\left\{d\in\mathbb{N}:\ d\geq 1,\ \frac{L}{d}\geq E\right\}=\left\lfloor\frac{L}{E}\right\rfloor. |  | (4) |

A node is *active* if dGo​u​t​(u)≤d⋆​(C)d^{out}\_{G}(u)\leq d^{\star}(C).

###### Definition 3 (Single-hit graph).

(u→v)∈E​(Gs​h)(u\to v)\in E(G\_{sh}) iff (u→v)∈E​(G)(u\to v)\in E(G) and uu is active.

#### Intuition (single-hit reduction).

The sender-truncated graph Gs​hG\_{sh} isolates defaults that can be caused by a single counterparty failure. When a sender has sufficiently many outgoing obligations, each individual exposure is too small to trigger default on its own, and such edges cannot participate in single-hit contagion. Retaining only edges from active senders therefore captures exactly the part of the network along which one-step propagation is possible, without altering the underlying balance-sheet dynamics.

## 3 Branching Parameters

Let D∼Pois​(λ)D\sim\mathrm{Pois}(\lambda) and define

|  |  |  |
| --- | --- | --- |
|  | X:=D​ 1​{D≤d⋆​(C)}.X:=D\,\mathbf{1}\{D\leq d^{\star}(C)\}. |  |

###### Definition 4 (Branching mean).

|  |  |  |
| --- | --- | --- |
|  | ρo​u​t:=𝔼​[X]=λ​ℙ​(D≤d⋆​(C)−1).\rho\_{out}:=\mathbb{E}[X]=\lambda\,\mathbb{P}(D\leq d^{\star}(C)-1). |  |

## 4 Systemic Events

Fix ε∈(0,1)\varepsilon\in(0,1) and kn=⌈c​log⁡n⌉k\_{n}=\lceil c\log n\rceil.

###### Definition 5 (Random-shock systemic event).

Let S0S\_{0} be uniform among subsets of [n][n] of size knk\_{n}, independent of GG. Define

|  |  |  |
| --- | --- | --- |
|  | ℱnr​a​n​d:={|D∞​(S0)|≥ε​n}.\mathcal{F}\_{n}^{rand}:=\{|D\_{\infty}(S\_{0})|\geq\varepsilon n\}. |  |

## 5 Subcritical Regime

###### Lemma 2 (Subcritical forward reachability is polylogarithmic).

Assume ρo​u​t<1\rho\_{out}<1. Fix c>0c>0 and let S0S\_{0} be uniform among subsets of [n][n] of size kn=⌈c​log⁡n⌉k\_{n}=\lceil c\log n\rceil, independent of GG. Then for every fixed M>0M>0, with s:=M​(log⁡n)2s:=M(\log n)^{2},

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|Reach+​(S0;Gs​h)|>s)→0.\mathbb{P}\Big(|\mathrm{Reach}^{+}(S\_{0};G\_{sh})|>s\Big)\to 0. |  |

###### Proof.

Fix M>0M>0 and set s:=M​(log⁡n)2s:=M(\log n)^{2}. Explore Reach+​(S0;Gs​h)\mathrm{Reach}^{+}(S\_{0};G\_{sh}) by breadth-first search (BFS) in Gs​hG\_{sh}, revealing out-edges of newly discovered vertices as they are explored, and stopping the exploration if the discovered set size reaches ss. For each tail uu, the out-edge indicators {𝟏​{(u→v)∈E​(G)}:v≠u}\{\mathbf{1}\{(u\to v)\in E(G)\}:v\neq u\} are independent Bernoulli(λ/n)(\lambda/n), independent across distinct tails. Moreover, in Gs​hG\_{sh} all out-edges from uu are retained iff dGo​u​t​(u)≤d⋆​(C)d^{out}\_{G}(u)\leq d^{\star}(C) and otherwise none are retained. Hence, the number of out-edges revealed from a newly explored vertex in Gs​hG\_{sh} has distribution KK with

|  |  |  |
| --- | --- | --- |
|  | K=dBin​(n−1,λ/n)​𝟏​{Bin​(n−1,λ/n)≤d⋆​(C)},K\stackrel{{\scriptstyle d}}{{=}}\mathrm{Bin}(n-1,\lambda/n)\mathbf{1}\{\mathrm{Bin}(n-1,\lambda/n)\leq d^{\star}(C)\}, |  |

and these KK’s are independent across explored tails. While the discovered set has size at most ss, each revealed out-edge chooses a destination uniformly from [n]∖{u}[n]\setminus\{u\}; the number of *new* vertices found is at most the number of revealed out-edges. Consequently, the BFS discovered-set size is stochastically dominated by the total population size of a Galton–Watson process with offspring distribution KK. Since d⋆​(C)d^{\star}(C) is fixed once CC is fixed, KK is uniformly bounded by d⋆​(C)d^{\star}(C), and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[K]→𝔼​[X]=ρo​u​t<1.\mathbb{E}[K]\to\mathbb{E}[X]=\rho\_{out}<1. |  |

Therefore the associated Galton–Watson total progeny has an exponential tail: there exists a>0a>0 and n0n\_{0} such that for all n≥n0n\geq n\_{0} and all m≥1m\geq 1,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(GW total progeny started from one particle≥m)≤e−a​m.\mathbb{P}(\text{GW total progeny started from one particle}\geq m)\leq e^{-am}. |  |

Starting from |S0|=kn=⌈c​log⁡n⌉|S\_{0}|=k\_{n}=\lceil c\log n\rceil initial particles and using a union bound over the knk\_{n} independent GW trees gives

|  |  |  |
| --- | --- | --- |
|  | ℙ​(GW total progeny started from kn particles≥s)≤kn​e−a​s.\mathbb{P}(\text{GW total progeny started from $k\_{n}$ particles}\geq s)\leq k\_{n}\,e^{-as}. |  |

With s=M​(log⁡n)2s=M(\log n)^{2}, the right-hand side tends to 0. Since the BFS discovered set is dominated by this GW total progeny, the same bound holds for |Reach+​(S0;Gs​h)||\mathrm{Reach}^{+}(S\_{0};G\_{sh})|, proving the claim.
∎

###### Theorem 1 (Random-shock subcriticality).

Assume ρo​u​t<1\rho\_{out}<1. Then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℱnr​a​n​d)→0.\mathbb{P}(\mathcal{F}\_{n}^{rand})\to 0. |  |

Moreover, with probability 1−o​(1)1-o(1), the cascade contains no multi-hit defaults and

|  |  |  |
| --- | --- | --- |
|  | D∞​(S0)=Reach+​(S0;Gs​h).D\_{\infty}(S\_{0})=\mathrm{Reach}^{+}(S\_{0};G\_{sh}). |  |

###### Proof (deferred-decisions filtration).

Fix M>0M>0 and set s:=M​(log⁡n)2s:=M(\log n)^{2}. By Lemma [2](https://arxiv.org/html/2601.04096v1#Thmlemma2 "Lemma 2 (Subcritical forward reachability is polylogarithmic). ‣ 5 Subcritical Regime ‣ Sharp Transitions and Systemic Risk in Sparse Financial Networks"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|Reach+​(S0;Gs​h)|≤s)→1.\mathbb{P}\Big(|\mathrm{Reach}^{+}(S\_{0};G\_{sh})|\leq s\Big)\to 1. |  | (5) |

Let (Dt)t≥0(D\_{t})\_{t\geq 0} be the cascade and Δt:=Dt∖Dt−1\Delta\_{t}:=D\_{t}\setminus D\_{t-1}. Define ℱt\mathcal{F}\_{t} as the sigma-field generated by (D0,…,Dt)(D\_{0},\dots,D\_{t}) and all edge indicators with tails in Dt−1D\_{t-1}. In particular, prior to time tt no edge indicators with tails in Δt\Delta\_{t} have been revealed. Conditional on ℱt\mathcal{F}\_{t}, the indicators

|  |  |  |
| --- | --- | --- |
|  | {𝟏​{(u→v)∈E​(G)}:u∈Δt,v∉Dt}\{\mathbf{1}\{(u\to v)\in E(G)\}:u\in\Delta\_{t},\ v\notin D\_{t}\} |  |

are independent Bernoulli(λ/n)(\lambda/n). For v∉Dtv\notin D\_{t}, let

|  |  |  |
| --- | --- | --- |
|  | Yt,v:=#​{u∈Δt:(u→v)∈E​(G)}.Y\_{t,v}:=\#\{u\in\Delta\_{t}:(u\to v)\in E(G)\}. |  |

Then Yt,v∼Bin​(|Δt|,λ/n)Y\_{t,v}\sim\mathrm{Bin}(|\Delta\_{t}|,\lambda/n) conditionally, and

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Yt,v≥2∣ℱt)≤(|Δt|2)​(λ/n)2.\mathbb{P}(Y\_{t,v}\geq 2\mid\mathcal{F}\_{t})\leq\binom{|\Delta\_{t}|}{2}(\lambda/n)^{2}. |  |

Summing over v∉Dtv\notin D\_{t} yields

|  |  |  |
| --- | --- | --- |
|  | ℙ(∃v∉Dt:Yt,v≥2∣ℱt)≤λ2​|Δt|2n.\mathbb{P}(\exists v\notin D\_{t}:\ Y\_{t,v}\geq 2\mid\mathcal{F}\_{t})\leq\frac{\lambda^{2}|\Delta\_{t}|^{2}}{n}. |  |

On {|D∞​(S0)|≤s}\{|D\_{\infty}(S\_{0})|\leq s\}, ∑t|Δt|2≤s2\sum\_{t}|\Delta\_{t}|^{2}\leq s^{2}, hence a union bound gives probability O​(s2/n)=o​(1)O(s^{2}/n)=o(1) of any multi-hit default. On the intersection of the event in ([5](https://arxiv.org/html/2601.04096v1#S5.E5 "In Proof (deferred-decisions filtration). ‣ 5 Subcritical Regime ‣ Sharp Transitions and Systemic Risk in Sparse Financial Networks")) and the no-multi-hit event, contagion proceeds only by single-hit transmissions along edges from active senders, so the cascade coincides with single-hit propagation:

|  |  |  |
| --- | --- | --- |
|  | D∞​(S0)=Reach+​(S0;Gs​h).D\_{\infty}(S\_{0})=\mathrm{Reach}^{+}(S\_{0};G\_{sh}). |  |

In particular, |D∞​(S0)|≤s=o​(n)|D\_{\infty}(S\_{0})|\leq s=o(n) whp, and therefore

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℱnr​a​n​d)→0.\mathbb{P}(\mathcal{F}\_{n}^{rand})\to 0. |  |

∎

## 6 Supercritical Regime

###### Lemma 3 (Distributional identification of Gs​hG\_{sh}).

Gs​hG\_{sh} has the same law as an i.i.d.-outdegree digraph with

|  |  |  |
| --- | --- | --- |
|  | K=dBin​(n−1,λ/n)​𝟏​{Bin​(n−1,λ/n)≤d⋆​(C)}.K\stackrel{{\scriptstyle d}}{{=}}\mathrm{Bin}(n-1,\lambda/n)\mathbf{1}\{\mathrm{Bin}(n-1,\lambda/n)\leq d^{\star}(C)\}. |  |

###### Proof.

Outgoing edge families in G​(n,λ/n)G(n,\lambda/n) are independent across tails. Conditional on dGo​u​t​(u)=kd^{out}\_{G}(u)=k, the out-neighbors of uu are uniform. Sender-truncation retains all kk edges if k≤d⋆​(C)k\leq d^{\star}(C) and none otherwise, independently across uu.
∎

###### Theorem 2 (Bow-tie / strong-giant structure for Gs​hG\_{sh}).

Assume ρo​u​t>1\rho\_{out}>1. Then there exist constants

|  |  |  |
| --- | --- | --- |
|  | αi​n,αo​u​t,αs​c​c∈(0,1)\alpha\_{in},\alpha\_{out},\alpha\_{scc}\in(0,1) |  |

and random vertex sets

|  |  |  |
| --- | --- | --- |
|  | ℐn,𝒪n,𝒞n⊂[n]\mathcal{I}\_{n},\ \mathcal{O}\_{n},\ \mathcal{C}\_{n}\subset[n] |  |

such that with probability 1−o​(1)1-o(1):

1. (i)

   |ℐn|≥αi​n​n|\mathcal{I}\_{n}|\geq\alpha\_{in}n, |𝒪n|≥αo​u​t​n|\mathcal{O}\_{n}|\geq\alpha\_{out}n, and |𝒞n|≥αs​c​c​n|\mathcal{C}\_{n}|\geq\alpha\_{scc}n;
2. (ii)

   𝒞n\mathcal{C}\_{n} is strongly connected in Gs​hG\_{sh};
3. (iii)

   every v∈ℐnv\in\mathcal{I}\_{n} has a directed path to 𝒞n\mathcal{C}\_{n} in Gs​hG\_{sh};
4. (iv)

   every u∈𝒞nu\in\mathcal{C}\_{n} has directed paths to all vertices in 𝒪n\mathcal{O}\_{n}.

In particular, for every v∈ℐnv\in\mathcal{I}\_{n},

|  |  |  |
| --- | --- | --- |
|  | Reach+​(v;Gs​h)⊇𝒪n.\mathrm{Reach}^{+}(v;G\_{sh})\supseteq\mathcal{O}\_{n}. |  |

###### Corollary 1 (Random shocks trigger systemic events).

Assume ρo​u​t>1\rho\_{out}>1. Fix ε∈(0,αo​u​t)\varepsilon\in(0,\alpha\_{out}) and any c>0c>0. Then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℱnr​a​n​d)→1.\mathbb{P}(\mathcal{F}\_{n}^{rand})\to 1. |  |

#### Remark on non-monotonicity.

Although the results exhibit sharp transitions, standard monotone sharp-threshold machinery does not directly apply. Adding outgoing edges to a node increases diversification but simultaneously reduces per-edge exposure, so the occurrence of systemic events is not monotone in the edge set. The analysis therefore proceeds by isolating a monotone substructure (Gs​hG\_{sh}) rather than appealing to global monotonicity.

## Scope and Limitations

The results are derived for a sparse directed Erdős–Rényi network with homogeneous liabilities, equity, and zero recovery, under the specific exposure-splitting rule defined in Section 2. The analysis isolates single-hit contagion and characterizes systemic events arising from shocks of logarithmic size. The paper does not address heterogeneous balance sheets, alternative recovery rules, correlated exposures, time-varying networks, or cascade mechanisms requiring coordinated multi-hit accumulation at macroscopic scales. Conclusions should therefore be interpreted strictly within the stated model and assumptions.

## References

* [1]

  M. D. Penrose.
  The strong giant in a random digraph.
  Random Structures & Algorithms, 45(1):1–31, 2014.