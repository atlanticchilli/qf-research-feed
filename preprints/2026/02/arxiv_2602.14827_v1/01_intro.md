---
authors:
- Javier Mancilla
- Theodoros D. Bouloumis
- Frederic Goguikian
doc_id: arxiv:2602.14827v1
family_id: arxiv:2602.14827
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm
  (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct
  Indexing'
url_abs: http://arxiv.org/abs/2602.14827v1
url_html: https://arxiv.org/html/2602.14827v1
venue: arXiv q-fin
version: 1
year: 2026
---


Javier Mancilla1∗, Theodoros D. Bouloumis2, Frederic Goguikian1
1. SquareOne Capital, 1221 Brickell Ave. Suite 900, Miami Fl 33131., Miami, US
2. School of Physics, Faculty of Sciences, Aristotle University of Thessaloniki, GR-54124 Thessaloniki, Greece
Email Address: javier.m@squareonecap.com, tmpoulou@physics.auth.gr, fredi.g@squareonecap.com

###### Abstract

Portfolio optimization under strict cardinality constraints is a combinatorial challenge that defies classical convex optimization techniques, particularly in the context of “Direct Indexing” and ESG-constrained mandates. In the Noisy Intermediate-Scale Quantum (NISQ) era, the Quantum Approximate Optimization Algorithm (QAOA) offers a promising hybrid approach. However, standard QAOA implementations utilizing transverse field mixers often fail to strictly enforce hard constraints, necessitating soft penalties that distort the energy landscape. This paper presents a comprehensive analysis of a constraint-preserving QAOA formulation against Simulated Annealing (SA) and Hierarchical Risk Parity (HRP). We implement a specific QAOA ansatz utilizing a Dicke state initialization |DNK⟩|D\_{N}^{K}\rangle and an XY-mixer Hamiltonian that strictly preserves the Hamming weight of the solution, ensuring only valid portfolios of size KK are explored. Furthermore, we introduce a Trotterized parameter initialization schedule inspired by adiabatic quantum computing to mitigate the “Barren Plateau” problem. Backtesting on a basket of 10 US equities over 2025 reveals that our QAOA approach achieves a Sharpe Ratio of 1.81, significantly outperforming Simulated Annealing (1.31) and HRP (0.98). We further analyze the operational implications of the algorithm’s high turnover (76.8%), discussing the trade-offs between theoretical optimality and implementation costs in institutional settings.

## I Introduction

The modern asset management industry is increasingly moving toward “Direct Indexing”—strategies where investors own the underlying components of an index rather than an ETF. This allows for granular customization, such as tax-loss harvesting or ESG (Environmental, Social, and Governance) screening. However, Direct Indexing introduces a computationally intractable problem: Cardinality Constrained Portfolio Optimization.

The classical framework, introduced by Markowitz in 1952 as Mean-Variance Optimization (MVO), models risk as the variance of portfolio returns and seeks allocations that minimize risk for a given expected return [[12](https://arxiv.org/html/2602.14827v1#bib.bib1 "Portfolio selection")]. While MVO provides closed-form solutions for unconstrained portfolios, the requirement to select exactly KK assets out of NN (to minimize transaction costs or tracking error) transforms the convex optimization problem into a non-convex, NP-hard combinatorial problem [[4](https://arxiv.org/html/2602.14827v1#bib.bib2 "Computational study of a family of mixed-integer quadratic programming problems")]. As NN grows, the search space (NK)\binom{N}{K} expands factorially, rendering exhaustive search impossible. In addition, MVO is highly sensitive to estimation errors in expected returns and covariances, and its reliance on matrix inversion poses computational challenges for large asset universes [[13](https://arxiv.org/html/2602.14827v1#bib.bib3 "Efficient asset management: a practical guide to stock portfolio optimization and asset allocation"), [2](https://arxiv.org/html/2602.14827v1#bib.bib4 "The sharpe ratio efficient frontier"), [7](https://arxiv.org/html/2602.14827v1#bib.bib24 "Risk-based and factor investing")]

Alternative approaches have also emerged. Hierarchical Risk Parity (HRP), for example, uses hierarchical clustering to allocate capital without requiring covariance matrix inversion, improving robustness under noisy conditions [[11](https://arxiv.org/html/2602.14827v1#bib.bib7 "Building diversified portfolios that outperform out of sample")]. However, HRP and other classical methods still rely on deterministic optimization techniques that may struggle with combinatorial constraints, such as selecting a fixed number of assets (a cardinality constraint).

Classical heuristics like Simulated Annealing (SA) [[8](https://arxiv.org/html/2602.14827v1#bib.bib10 "Optimization by simulated annealing")] and Genetic Algorithms [[1](https://arxiv.org/html/2602.14827v1#bib.bib12 "A genetic algorithm approach for portfolio optimization")] are the current industry standard but often get trapped in local minima. The Quantum Approximate Optimization Algorithm (QAOA) [[5](https://arxiv.org/html/2602.14827v1#bib.bib17 "A quantum approximate optimization algorithm")] proposes a quantum-classical hybrid approach to finding better approximations by leveraging variational quantum circuits. Yet, standard QAOA implementations struggle with hard constraints, often relaxing them into penalty terms that complicate convergence. Nevertheless, these techniques are particularly relevant for portfolio selection, which can be formulated as a Quadratic Unconstrained Binary Optimization (QUBO) problem, where each decision (include or exclude an asset) is represented as a binary variable [[6](https://arxiv.org/html/2602.14827v1#bib.bib18 "A tutorial on formulating and using QUBO models")].

This paper bridges the gap between quantum theory and financial practice. We propose a Hard-Constraint QAOA using XY-mixers and Dicke states, specifically designed for the KK-of-NN selection problem. Our contributions are threefold: (1) a constraint‑preserving QAOA formulation for cardinality‑constrained portfolio selection that uses Dicke‑state initialization and a complete‑graph XY mixer to keep evolution within the exact‑KK subspace, plus a trotterized (γ,β\gamma,\beta) initialization to improve optimization stability; (2) an end‑to‑end evaluation pipeline that benchmarks QAOA‑XY against SA and HRP, then performs Sharpe‑max weight allocation with 5–50% bounds and applies transaction costs (5 bps ×\times turnover) to report net performance; and (3) a 2025 monthly walk‑forward on 10 U.S. equities with a 180‑day lookback, accompanied by optimization‑landscape, convergence, and circuit depth‑scaling (up to p=6p=6) diagnostics for interpretability and reproducibility. The remainder of the paper is organized as follows: Section II reviews related work; Section III details the problem mapping, QAOA ansatz, and baselines; Section IV describes data and experimental setup; Section V presents results and diagnostics; and Section VI discusses limitations and implementation considerations before concluding.

## II Literature Review - Business Application & Context

### II-A Classical Portfolio Optimization

Portfolio optimization has been a central theme in finance since Harry Markowitz introduced Mean-Variance Optimization (MVO) in 1952, laying the foundation for modern portfolio theory [[12](https://arxiv.org/html/2602.14827v1#bib.bib1 "Portfolio selection")]. MVO seeks to minimize portfolio variance (a measure of risk) for a given level of expected return, using the covariance matrix of asset returns to capture how assets move together [[13](https://arxiv.org/html/2602.14827v1#bib.bib3 "Efficient asset management: a practical guide to stock portfolio optimization and asset allocation")]. However, MVO suffers from estimation risk: small errors in expected returns or covariance estimates can lead to unstable allocations [[2](https://arxiv.org/html/2602.14827v1#bib.bib4 "The sharpe ratio efficient frontier")]. This sensitivity is particularly problematic in real-world settings where data is noisy and markets are dynamic [[7](https://arxiv.org/html/2602.14827v1#bib.bib24 "Risk-based and factor investing")].

To mitigate these issues, researchers have proposed techniques such as shrinkage estimators, which adjust covariance estimates to improve robustness [[10](https://arxiv.org/html/2602.14827v1#bib.bib5 "Honey, i shrunk the sample covariance matrix")]. Another significant advancement is Hierarchical Risk Parity (HRP), introduced by Lopez de Prado in 2016 [[11](https://arxiv.org/html/2602.14827v1#bib.bib7 "Building diversified portfolios that outperform out of sample")]. HRP uses hierarchical clustering to group assets based on correlation structure and allocates capital according to a tree-based hierarchy. By avoiding matrix inversion entirely, HRP improves stability and scalability, making it suitable for high-dimensional portfolios.

### II-B The “Combinatorial Cliff” in Asset Management

For a typical S&P 500 replication strategy (N=500N=500), selecting a sub-portfolio of K=50K=50 stocks involves exploring approximately 106910^{69} combinations. Institutional managers often face a “Combinatorial Cliff” where classical solvers (like Mixed-Integer Quadratic Programming) timeout or fail to converge within trading windows [[3](https://arxiv.org/html/2602.14827v1#bib.bib23 "Portfolio construction through mixed-integer programming at Grantham, Mayo, Van Otterloo and Company")]. This is particularly acute in high-frequency rebalancing scenarios where solutions must be found in seconds.

### II-C Direct Indexing and Custom SMAs

In Separately Managed Accounts (SMAs), wealth managers must create personalized portfolios for thousands of clients. If a client requests “S&P 500 excluding Fossil Fuels, limited to 30 stocks,” the optimization must run rapidly and reliably. A quantum solver that consistently finds lower-energy states (higher Sharpe Ratios) translates directly to Capital Efficiency—achieving the same target return with less risk exposure.

### II-D Quantum Computing in Finance

Quantum computing introduces a fundamentally different approach to computation, leveraging principles of quantum mechanics such as superposition and entanglement. These properties allow quantum systems to explore large solution spaces more efficiently than classical computers for certain problem classes [[14](https://arxiv.org/html/2602.14827v1#bib.bib19 "Quantum computing for finance: overview and prospects")].

In the context of finance, portfolio selection can be formulated as a combinatorial optimization problem, which is computationally challenging for large asset universes. Algorithms such as the Quantum Approximate Optimization Algorithm (QAOA) address these challenges by using variational quantum circuits to approximate solutions to NP-hard problems—a class of problems that are extremely difficult to solve optimally on classical hardware. QAOA alternates between applying a cost Hamiltonian (encoding the objective function) and a mixer Hamiltonian (exploring feasible solutions), optimizing circuit parameters to minimize expected cost [[5](https://arxiv.org/html/2602.14827v1#bib.bib17 "A quantum approximate optimization algorithm")].

Other quantum (or hybrid quantum-classical) algorithms, such as the Variational Quantum Eigensolver (VQE), have also been explored for optimization tasks [[15](https://arxiv.org/html/2602.14827v1#bib.bib22 "The variational quantum eigensolver: a review of methods and best practices")]. Additionally, quantum annealing, implemented on specialized hardware like D-Wave systems, solves optimization problems by evolving a quantum system toward its lowest-energy state [[9](https://arxiv.org/html/2602.14827v1#bib.bib11 "Quantum annealing for combinatorial optimization: a comparative study")]. While true quantum annealing requires quantum hardware, classical analogs such as simulated annealing mimic this process heuristically.

### II-E Turnover vs. Optimality

A key operational metric is turnover. High turnover implies high transaction costs (slippage, commissions). While our QAOA approach finds superior theoretical portfolios (higher Sharpe), it exhibits higher turnover. For high-frequency trading firms or liquid markets (S&P 500 large caps), this is acceptable. For illiquid markets, the cost of execution may outweigh the alpha generation, necessitating multi-objective cost functions in future iterations of the algorithm.

## III Methodology

This section details the theoretical formulation and the end‑to‑end pipeline we implement for cardinality‑constrained portfolio selection with constraint‑preserving QAOA‑XY and Simulated Annealing (SA), followed by Sharpe‑max weight allocation and a 2025 monthly walk‑forward backtest with explicit transaction costs.

### III-A Problem Formulation: Ising Hamiltonian

We treat construction as a two‑stage process: (i) selection of exactly KK assets out of NN (discrete), and (ii) allocation of continuous weights within the selected subset. Let xi∈{0,1}x\_{i}\in\{0,1\} indicate exclusion or inclusion of asset ii. The selection objective is the standard risk–return trade‑off as represented by the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | m​i​n⏟x∈{0,1}N​q​x⊤​Σ​x⏟risk−(1−q)​μ⊤​x⏟returns.t.∑i=1Nxi=K,\underbrace{min}\_{x\in\{0,1\}^{N}}\underbrace{q\,x^{\top}\Sigma x}\_{\text{risk}}-\underbrace{(1-q)\,\mu^{\top}x}\_{\text{return}}\quad\text{s.t.}\quad\sum\_{i=1}^{N}x\_{i}=K, |  | (1) |

where μ\mu and Σ\Sigma are estimated on a rolling 180‑trading‑day lookback and annualized (covariance via Ledoit–Wolf shrinkage). We set K=5K=5 and q=0.3q=0.3 in all experiments. The choice of the risk aversion parameter, qq, depends on the strategy one wants to follow, as explained in the next section.

For QAOA, we map Eq. [1](https://arxiv.org/html/2602.14827v1#S3.E1 "In III-A Problem Formulation: Ising Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") to an Ising form using xi=1−Zi2x\_{i}=\tfrac{1-Z\_{i}}{2}. In practice, our implementation constructs a cost Hamiltonian with linear ZiZ\_{i} terms from expected returns and pairwise Zi​ZjZ\_{i}Z\_{j} terms from covariance off‑diagonals; diagonal risk contributions are treated within constants/linear terms and are not required explicitly for the selection dynamics used here. The sign conventions match the code, where −(1−q)​μi-(1-q)\mu\_{i} multiplies ZiZ\_{i} and 2​q​Σi​j2q\Sigma\_{ij} multiplies Zi​ZjZ\_{i}Z\_{j}.

To discourage unnecessary turnover between months, we incorporate a continuity bonus that slightly lowers the linear cost of assets held in the previous period; this warm‑start bias is applied consistently in both SA and QAOA constructions.

### III-B The Constraint‑Preserving Ansatz

Standard QAOA uses a transverse field mixer HX=∑XiH\_{X}=\sum X\_{i} which flips single spins, violating the constraint ∑X​i=K\sum Xi=K. We replace this with a subspace-preserving approach.

#### III-B1 Dicke State Initialization

We initialize the system in the Dicke state |DNK⟩|D\_{N}^{K}\rangle, an equal superposition of all computational basis states with Hamming weight KK:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ψ0⟩=|DNK⟩=(NK)−1/2​∑|x|=K|x⟩|\psi\_{0}\rangle=|D\_{N}^{K}\rangle=\binom{N}{K}^{-1/2}\sum\_{|x|=K}|x\rangle |  | (2) |

This ensures the optimization begins strictly inside the feasible subspace.

#### III-B2 XY-Mixer Hamiltonian

We utilize the XY-mixer, de-
fined on a ring or complete graph:

|  |  |  |  |
| --- | --- | --- | --- |
|  | HXY=∑(i,j)∈E(Xi​Xj+Yi​Yj).H\_{\mathrm{XY}}=\sum\_{(i,j)\in E}\bigl(X\_{i}X\_{j}+Y\_{i}Y\_{j}\bigr). |  | (3) |

Noting that Xi​Xj+Yi​Yj=|01⟩​⟨10|i​j+|10⟩​⟨01|i​jX\_{i}X\_{j}+Y\_{i}Y\_{j}=|01\rangle\langle 10|\_{ij}+|10\rangle\langle 01|\_{ij}, this operator performs a partial SWAP, exchanging excitation between qubits ii and jj. Crucially, it commutes with the total number operator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [HX​Y,∑iZi]=0[H\_{XY},\sum\_{i}Z\_{i}]=0 |  | (4) |

This commutation ensures that the unitary evolution U​(β)=e−i​β​HX​YU(\beta)=e^{-i\beta H\_{XY}} never leaves the subspace of KK selected assets, eliminating the need for penalty terms and reducing the effective Hilbert space dimension.

### III-C The Cost Hamiltonian

The cost Hamiltonian is

|  |  |  |  |
| --- | --- | --- | --- |
|  | HC=∑iαi​Zi+∑i<jβi​j​Zi​Zj,H\_{C}\;=\;\sum\_{i}\alpha\_{i}Z\_{i}\;+\;\sum\_{i<j}\beta\_{ij}\,Z\_{i}Z\_{j}, |  | (5) |

|  |  |  |
| --- | --- | --- |
|  | with​αi=−(1−q)​μi(ann),βi​j=2​q​Σi​j(ann).\mbox{with}\;\;\alpha\_{i}=-(1-q)\mu\_{i}^{(\text{ann})},\quad\beta\_{ij}=2q\,\Sigma\_{ij}^{(\text{ann})}. |  |

If asset ii was held last month, we apply a continuity discount to αi\alpha\_{i} to reduce churn.

### III-D Trotterized Parameter Initialization

A major hurdle in training Parametrized Quantum Circuits (PQC) is the “Barren Plateau” phenomenon, where gradients vanish exponentially. To mitigate this, we employ a Trotterized Initialization strategy.

We interpret QAOA as a discretized version of Adiabatic Quantum Computation (AQC). In AQC, the system evolves slowly under H​(t)=(1−s)​Hm​i​x+s​Hc​o​s​tH(t)=(1-s)H\_{mix}+sH\_{cost}. By mapping the adiabatic schedule to QAOA parameters, we initialize the variational parameters (γ,β)(\gamma,\beta) for depth pp as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γl=lp​Δ​t,βl=(1−lp)​Δ​t\gamma\_{l}=\frac{l}{p}\Delta t,\quad\beta\_{l}=\left(1-\frac{l}{p}\right)\Delta t |  | (6) |

This linear ramp provides a high-quality “warm start” for the classical optimizer (Adam), ensuring the optimization trajectory begins in a convex basin rather than a flat plateau.

### III-E Measurement & Candidate Selection

After training a given depth, we evaluate the full probability vector and retain only strings with Hamming weight KK and probability ≥1%\geq 1\%; among these we compute the classical cost in Eq. [1](https://arxiv.org/html/2602.14827v1#S3.E1 "In III-A Problem Formulation: Ising Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") and keep the minimum‑cost string as the selection for that depth. The final selection for the period is the best across tested depths (up to p=6p=6).

### III-F Simulated Annealing (Selection via QUBO)

We encode Eq. [1](https://arxiv.org/html/2602.14827v1#S3.E1 "In III-A Problem Formulation: Ising Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") as a QUBO by adding a budget penalty P​(∑ixi−K)2P(\sum\_{i}x\_{i}-K)^{2}. Expanding the square yields:

|  |  |  |
| --- | --- | --- |
|  | Qi​i=q​Σi​i(ann)−(1−q)​μi(ann)+P​(1−2​K),Q\_{ii}=q\,\Sigma\_{ii}^{(\text{ann})}-(1-q)\,\mu\_{i}^{(\text{ann})}+P\,(1-2K), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qi​j=2​q​Σi​j(ann)+2​P(i<j).Q\_{ij}=2q\,\Sigma\_{ij}^{(\text{ann})}+2P\ \ (i<j). |  | (7) |

We scale PP relative to the largest objective term to enforce feasibility. As in QAOA, a continuity bonus lowers the diagonal term Qi​iQ\_{ii} for previously held names. We then call neal.SimulatedAnnealingSampler with n​u​m​\_​r​e​a​d​s=5000num\\_reads=5000 and n​u​m​\_​s​w​e​e​p​s=1000num\\_sweeps=1000, and retain the best feasible sample with ∑ixi=K\sum\_{i}x\_{i}=K.

### III-G Weight Allocation and Trading Frictions

Given the selected subset S={i:xi=1}S=\{i:x\_{i}=1\}, we solve a continuous Sharpe‑max problem (equivalently, minimize negative Sharpe) using SLSQP, subject to ∑i∈Swi=1\sum\_{i\in S}w\_{i}=1 and per‑name bounds 0.05≤wi≤0.500.05\leq w\_{i}\leq 0.50. If the selector fails, we fall back to HRP weights computed via PyPortfolioOpt; HRP also serves as a continuous‑weight baseline for comparison.

We define turnover as ∑i|wi,t−wi,t−1|\sum\_{i}|w\_{i,t}-w\_{i,t-1}| and apply transaction costs of 5 bps ×\times turnover each rebalance to obtain net returns. Portfolio value starts at $1,000,000 and compounds monthly.

### III-H Walk‑Forward Protocol and Data

Universe & horizon. Ten U.S. large‑cap equities (AAPL, MSFT, GOOGL, AMZN, JPM, V, TSLA, UNH, LLY, XOM) are included. Rebalancing is monthly across calendar year 2025. At each rebalance, we compute μ,Σ\mu,\Sigma from the preceding 180 trading days and annualize.

Data source & preprocessing. We use Yahoo Finance auto‑adjusted Close prices via yfinance. Missing values are forward‑filled, and non‑trading rows dropped. Covariance is estimated with Ledoit–Wolf shrinkage.

Continuity. Prior‑period selections are provided to the next period’s optimization via a continuity bonus.

### III-I Complete Algorithm

Algorithm [1](https://arxiv.org/html/2602.14827v1#alg1 "Algorithm 1 ‣ III-I Complete Algorithm ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") summarizes the end‑to‑end pipeline executed at each monthly rebalance date.

Algorithm 1  QAOA-XY / SA Hybrid Portfolio Construction (Monthly, 2025)

0: Price data PP (auto-adjusted), universe UU (|U|=N|U|=N), cardinality K=5K=5, risk-aversion q=0.3q=0.3, lookback L=180L=180 trading days, transaction cost τ=5​bps\tau=5~\mbox{bps}, continuity bonus κ≥0\kappa\geq 0

0: Weights wtw\_{t} for each month tt in 2025; value path VtV\_{t} (net of costs)

1: for each rebalance month tt do

2:  Extract window [t−L,t)[t-L,t) from PP; compute daily returns; drop NA

3:  Estimate μ\mu (mean) and Σ\Sigma (Ledoit–Wolf); annualize both

4:  Set continuity indicators sprevs\_{\text{prev}} from prior selection (if any)

5:  Selection via SA (QUBO):

6:  Form QQ with diag/off-diag per Eq. ([7](https://arxiv.org/html/2602.14827v1#S3.E7 "In III-F Simulated Annealing (Selection via QUBO) ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")); apply continuity bonus κ\kappa on diagonal terms

7:  Sample with neal: num\_reads=5000, num\_sweeps=1000; keep best feasible (∑ixi=K\sum\_{i}x\_{i}=K)

8:  Selection via QAOA-XY (constraint-preserving):

9:  Build HCH\_{C} as in Eq. ([5](https://arxiv.org/html/2602.14827v1#S3.E5 "In III-C The Cost Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")); build HX​YH\_{XY} as in Eq. ([3](https://arxiv.org/html/2602.14827v1#S3.E3 "In III-B2 XY-Mixer Hamiltonian ‣ III-B The Constraint‑Preserving Ansatz ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")); prepare |DNK⟩\lvert D\_{N}^{K}\rangle

10:  for p=1p=1 to 66 do

11:   Initialize (γ,β)(\gamma,\beta) with linear (trotter-inspired) ramp; Adam(stepsize 0.020.02, ϵ=10−10\epsilon=10^{-10})

12:   Optimize with early stopping; compute probabilities; filter weight-KK, prob ≥1%\geq 1\%

13:   Score candidates by classical cost Eq. ([1](https://arxiv.org/html/2602.14827v1#S3.E1 "In III-A Problem Formulation: Ising Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")); keep best

14:  end for

15:  Choose final QAOA selection as best across p=1,…,6p=1,\dots,6

16:  Allocation (common):

17:  for each selector S∈{SA,QAOA-XY}S\in\{\text{SA},\text{QAOA-XY}\} do

18:   Solve Sharpe-max (SLSQP) on SS with bounds 0.05≤wi≤0.500.05\leq w\_{i}\leq 0.50 and ∑iwi=1\sum\_{i}w\_{i}=1

19:  end for

20:  Compute HRP baseline weights (PyPortfolioOpt)

21:  Returns and transaction costs:

22:  Compute gross monthly returns for each strategy; turnover =∑i|wi,t−wi,t−1|=\sum\_{i}\lvert w\_{i,t}-w\_{i,t-1}\rvert

23:  Net return =gross−τ×turnover=\text{gross}-\tau\times\text{turnover};  Vt←Vt−1​(1+net return)V\_{t}\leftarrow V\_{t-1}\,(1+\text{net return})

24: end for

25: return {wt,Vt}\{w\_{t},V\_{t}\} and diagnostics

## IV Experimental Setup

### IV-A Data and Asset Universe

We evaluate the approach on a 10‑stock U.S. large‑cap universe, as shown below. Price data are auto‑adjusted Close series retrieved via Yahoo Finance (through yfinance) and forward‑filled where necessary; non‑trading rows are dropped. The out‑of‑sample period is calendar year 2025 with monthly rebalancing. For each rebalance date tt, statistics are computed from the preceding 180 trading days and then annualized; pre‑2025 data are used only for lookback estimation and never for trading. In Fig. [1](https://arxiv.org/html/2602.14827v1#S4.F1 "Figure 1 ‣ IV-A Data and Asset Universe ‣ IV Experimental Setup ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"), we present a schematic of our end-to-end experimental pipeline.

![Refer to caption](images/Workflow.png)


Figure 1: End-to-end experimental pipeline. Stage 1 estimates μ\mu and Σ\Sigma on a rolling L=180L=180 day window (Ledoit–Wolf covariance) and sets the cardinality constraint K=5K=5. Stage 2 performs constraint-preserving QAOA-XY selection using Dicke-state initialization and an XY mixer, with a trotterized parameter warm-start and classical optimization. Candidate portfolios are obtained by measurement, filtered to |x|=K|x|=K and P​(x)≥1%P(x)\geq 1\%, and rescored classically using Eq. [1](https://arxiv.org/html/2602.14827v1#S3.E1 "In III-A Problem Formulation: Ising Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"). Stage 3 allocates continuous weights via SLSQP (Sharpe-max) under box constraints and evaluates performance net of turnover-based transaction costs.

In the table below we summarize the most important parameters of the experiments, and further analyze them below.

TABLE I: Experimental Configuration

| Parameter | Value |
| --- | --- |
| Universe | |  | | --- | | 10 Liquid US Equities (AAPL, MSFT, | | GOOGL, AMZN, JPM, V, TSLA, | | UNH, LLY, XOM) | |
| Cardinality Constraint (KK) | 5 |
| Initial Capital | $1,000,000 |
| Risk Aversion (qq) | 0.3 |
| Period | 2025-01-01 to 2025-12-31, Monthly rebalance |
| Lookback Window | 180 days |
| Transaction Cost | 5 bps |
| Allocation bounds | 0.05≤wi≤0.500.05\leq w\_{i}\leq 0.50, ∑wi=1\sum w\_{i}=1 |
| Continuity Bonus | 0.1 |
| QAOA-XY Parameters | |
| Circuit Depth | 1,…,6 |
| Epsilon | 1e-10 |
| Stepsize | 0.02 |
| Max. Iterations | 100 |
| Initialization | Trotter ramp γ:0.1→0.5,β:0.5→0.1\gamma:0.1\rightarrow 0.5,\beta:0.5\rightarrow 0.1 |
| Readout filter | Hamming weight KK, probability ≥1%\geq 1\% |
| Simulated Annealing Parameters | |
| Number of Reads | 5,000 |
| Number of Sweeps | 1,000 |

### IV-B Walk‑Forward Protocol and Estimation Window

We use a monthly walk‑forward protocol. At each rebalance date tt in 2025, model inputs (μt,Σt\mu\_{t},\Sigma\_{t}) are estimated from the previous L=180L=180 trading days of returns, i.e., a rolling window [t−L,t)[t-L,t). Portfolios are then held from tt to the next rebalance date t+t^{+}.

Annualization. Expected returns are annualized by multiplying the daily mean by 252, and covariance is annualized by multiplying the Ledoit–Wolf covariance estimate by 252.

### IV-C Objective, Constraint, and Common Portfolio Construction Steps

#### IV-C1 Discrete selection objective (K‑of‑N)

All selection methods target the same cardinality‑constrained risk–return objective used throughout the manuscript as indicated in Eq. ([1](https://arxiv.org/html/2602.14827v1#S3.E1 "In III-A Problem Formulation: Ising Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")), with risk aversion q=0.3q=0.3 and cardinality K=5K=5.

#### IV-C2 Continuous allocation

Given a selected subset S={i:xi=1}S=\{i:x\_{i}=1\}, we compute portfolio weights by maximizing Sharpe Ratio (equivalently minimizing negative Sharpe) via SLSQP, subject to:

* •

  Full investment: ∑i∈Swi=1\sum\_{i\in S}w\_{i}=1
* •

  Box constraints: 0.05≤wi≤0.500.05\leq w\_{i}\leq 0.50 for all i∈Si\in S

If the optimizer fails or selection is invalid, we fall back to HRP weights.

### IV-D Hyperparameters and Compared Methods

It is important to discuss certain hyperparameters used in the models and justify their values set.

Risk Aversion qq: For a module oriented towards generating high alpha, return ought to be the parameter with the highest relative weight to variance, but not to the extreme of almost ignoring it. Without somehow penalizing return, the module may tend to produce excessively concentrated, correlated portfolios with extreme drawdowns that can destroy the generated alpha and generate idiosyncratic risks. Therefore, we set the risk aversion to q=0.3q=0.3 to continue prioritizing return with some variance control.

Lookback Window: In the case of seeking alpha opportunities, part of a manager’s role is to react quickly to news and sharp market movements to exploit inefficiencies. Therefore, a 6-month window would work better than an annual. The annual window is more stable, but it resembles a more passive approach that does not seek to capture these risk-return optimizations and tends to lag when volatility or correlations change suddenly. Ultimately, the choice of the lookback window should also align with the type of alpha generation sought. A more fundamental manager, with long investment horizons and lower portfolio turnover, could justify a 1-year lookback, prioritizing stability and avoiding overreacting to short-term noise. Conversely, if the style is more active, with higher turnover and greater sensitivity to tactical market changes, a 3–6 month window would fit the process better.

Rebalance Frequency: It also depends on the approach. If the approach is similar to a high-frequency quantitative hedge fund, even a weekly rebalance would be insufficient. At the same time, for a more fundamental manager, doing it every week would be too aggressive. In our case, and given the computational cost significantly increasing with circuit depth we chose a monthly rebalance which seems more suitable to manage transaction costs, and thus protect net return.

Nevertheless, further experimentation with the above hyperparameters is an interesting topic for future study, in order to understand how such parameters affect the final asset selection, and adjust accordingly based on the desired portfolio selection strategy.

We benchmark the constraint‑preserving QAOA‑XY approach against Simulated Annealing (SA), and Hierarchical Risk Parity (HRP).

#### IV-D1 Simulated Annealing (SA) baseline

The SA solver uses a QUBO with a quadratic penalty enforcing cardinality, sampled with neal.SimulatedAnnealingSampler. The penalty scale is set adaptively as:

|  |  |  |
| --- | --- | --- |
|  | P=2.5×m​a​xc​o​e​f​f×N,P=2.5\times max\_{coeff}\times N, |  |

where m​a​xc​o​e​f​fmax\_{coeff} is the maximum magnitude among the return and covariance contributions used in the QUBO construction.

Sampling parameters.

* •

  Number of reads: 5,000
* •

  Number of sweeps: 1,000
* •

  Feasibility: keep best sample satisfying ∑ixi=K\sum\_{i}x\_{i}=K

If an asset was selected in the previous month, its QUBO diagonal term is reduced (a small “bonus”) to discourage unnecessary churn.

#### IV-D2 Constraint‑preserving QAOA‑XY

All QAOA experiments are performed using PennyLane’s statevector simulator default.qubit. Each QAOA circuit begins in a Dicke state, the uniform superposition over all bitstrings of Hamming weight KK. This guarantees feasibility at initialization. In addition, as described in the previous section, we use a complete‑graph XY mixer (Eq. ([3](https://arxiv.org/html/2602.14827v1#S3.E3 "In III-B2 XY-Mixer Hamiltonian ‣ III-B The Constraint‑Preserving Ansatz ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")), which preserves Hamming weight and therefore maintains feasibility throughout the QAOA evolution. Next, we construct a diagonal cost Hamiltonian as per the Eq. ([5](https://arxiv.org/html/2602.14827v1#S3.E5 "In III-C The Cost Hamiltonian ‣ III Methodology ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")) and perform the optimization using the Adam (qml.AdamOptimizer) optimizer, and with parameters:

* •

  Stepsize: 0.02
* •

  Epsilon: 1e-10
* •

  Iterations: Up to 100 with early stopping if improvement stalls

Next, we perform the Trotterized parameter initialization with a linear ramp where γ\gamma linearly increases from 0.1 to 0.5 and β\beta linearly decreases from 0.5 to 0.1. Note that for each rebalance month we test circuit depths p=1,…,6p=1,\dots,6, and for each depth the parameters are re-initialized.

After optimization at a given depth, we compute the full probability vector and:

1. 1.

   keep only bitstrings with Hamming weight KK, and
2. 2.

   keep only candidates with probability ≥1%\geq 1\%, then
3. 3.

   rescore with the classical objective and keep the best candidate.

#### IV-D3 Hierarchical Risk Parity (HRP) baseline

HRP weights are computed directly from the lookback returns using PyPortfolioOpt.HRPOpt().optimize(). HRP serves both as a continuous‑allocation baseline and as a fallback weighting scheme if selection/allocation fails.

### IV-E Performance Metrics

To evaluate the effectiveness of each strategy, we use standard portfolio performance indicators. Below, we provide definitions and their practical interpretation:

* •

  Total Return: Rt​o​t=(Vf​i​n​a​l/Vi​n​i​t​i​a​l)−1R\_{tot}=(V\_{final}/V\_{initial})-1.
    
  Measures the overall portfolio value percentage gain or loss of the over the backtesting period. A higher total return indicates better absolute performance, but it does not account for risk.
* •

  Annualized Volatility: σa​n​n=σ×periods per year\sigma\_{ann}=\sigma\times\sqrt{\mbox{periods per year}}.
    
  Represents the standard deviation of returns scaled to an annual basis. It is a proxy for risk—higher volatility implies greater uncertainty in returns.
* •

  Sharpe Ratio: S​R=mean return×periodsσa​n​nSR=\frac{\mbox{mean return}\times\mbox{periods}}{\sigma\_{ann}},
    
  a risk-adjusted performance measure. It indicates how much excess return is earned per unit of risk. Higher values suggest more efficient portfolios.
* •

  Maximum Drawdown: MDD=mint⁡(Vtmaxs≤t⁡Vs−1)\mbox{MDD}=\min\_{t}\left(\frac{V\_{t}}{\max\_{s\leq t}V\_{s}}-1\right).
    
  Captures the largest peak-to-trough decline during the period. It reflects the worst-case loss an investor could have experienced.
* •

  Monthly Turnover: ∑i=1n|wi,t−wi,t−1|\sum\_{i=1}^{n}\left|w\_{i,t}-w\_{i,t-1}\right|.
    
  Measures how much the portfolio composition of nn number of assets changes from one period to the next one (monthly). High turnover implies higher transaction costs and operational complexity. From the monthly turnover, we calculate the net monthly return as

  |  |  |  |
  | --- | --- | --- |
  |  | rtn​e​t=rtg​r​o​s​s−τ×Turnover,r^{net}\_{t}=r^{gross}\_{t}-\tau\times\mbox{Turnover}, |  |

  where τ\tau is the transaction cost set to τ=5​bps\tau=5~\mbox{bps} (0.0005) in our experiments, and therefore, the portfolio value evolves as

  |  |  |  |
  | --- | --- | --- |
  |  | Vt=Vt−1​(1+rtn​e​t).V\_{t}=V\_{t-1}(1+r^{net}\_{t}). |  |

## V Results and Discussion

### V-A Depth Scaling: Validating the Ansatz

At first, we investigated how the QAOA‑XY performance varies with circuit depth and whether the optimization remains trainable as depth increases. The findings are presented in the Table [II](https://arxiv.org/html/2602.14827v1#S5.T2 "TABLE II ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") and the accompanying diagnostic plot (Fig. [2](https://arxiv.org/html/2602.14827v1#S5.F2 "Figure 2 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(a)). According to those, the increasing circuit depth yields progressively lower final cost values: the optimized cost decreases from −0.1488​(p=1)-0.1488~(p=1) to −0.5355​(p=6)-0.5355~(p=6). This pattern supports the core expressibility claim that deeper alternating applications of the cost and XY‑mixer unitaries produce a more expressive variational family, enabling lower-energy (better) configurations to be reached.

TABLE II: QAOA Depth Scaling Analysis (Validation of Trotterization)

| Depth (pp) | Final Cost | Iter. to Conv. | Gradient Norm |
| --- | --- | --- | --- |
| 1 | -0.1488 | 100 | 5.33×10−35.33\times 10^{-3} |
| 2 | -0.2979 | 72 | 1.21×10−21.21\times 10^{-2} |
| 3 | -0.3869 | 66 | 1.86×10−21.86\times 10^{-2} |
| 4 | -0.3319 | 81 | 1.11×10−21.11\times 10^{-2} |
| 5 | -0.3568 | 90 | 1.97×10−21.97\times 10^{-2} |
| 6 | -0.5355 | 100 | 5.47×10−25.47\times 10^{-2} |



![Refer to caption](images/cost_circuit.png)


(a)

![Refer to caption](images/barren.png)


(b)

![Refer to caption](images/time_depth.png)


(c)

Figure 2: (a) Cost minimization, (b) gradient magnitudes, and (c) computational cost, as a function of QAOA’s circuit depth.

A practical nuance appears in Fig. [2](https://arxiv.org/html/2602.14827v1#S5.F2 "Figure 2 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(a) where improvement is not strictly monotonic across all intermediate depths; a mild regression around p=4p=4 and p=5p=5 is observed. This is not uncommon in variational training: as parameter dimension increases, the optimizer can temporarily converge to poorer basins or require more iterations/tuning to consistently realize the theoretical expressibility gains. In our pipeline, this is mitigated by selecting the best portfolio across tested depths each month, rather than committing to a single depth globally.

A practical challenge in training parametrized quantum circuits is the potential emergence of flat optimization landscapes known as “barren plateaus”, which would manifest as gradient norms collapsing toward zero at larger circuit depths. However, as shown in Table [II](https://arxiv.org/html/2602.14827v1#S5.T2 "TABLE II ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"), increasing pp from 1 to 6 improved the ground state energy by >250%>250\%. Crucially, the Gradient Norm did not vanish at p=6p=6, but instead it increased from 5.33×10−35.33\times 10^{-3} (p=1p=1) to 5.47×10−25.47\times 10^{-2}) (p=6p=6).

This finding is depicted more clearly in Fig. [2](https://arxiv.org/html/2602.14827v1#S5.F2 "Figure 2 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(b), where gradient magnitudes remain far above a “vanishing gradient” threshold band. The most direct implication is that the training procedure remains numerically learnable at least up to depth 6 in this problem size (N=10), providing strong evidence that our Trotterized initialization successfully avoids Barren Plateaus and supporting its practical utility.

Figure [2](https://arxiv.org/html/2602.14827v1#S5.F2 "Figure 2 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(c) shows the computational cost per iteration to be increasing linearly with the circuit depth which is expected, since circuit evaluation cost grows with the number of layers. This observation along with the finding in Fig. [2](https://arxiv.org/html/2602.14827v1#S5.F2 "Figure 2 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(a) that for p=4p=4 and p=5p=5 the final optimized cost is actually worse than for p=3p=3 suggests that incremental benefit per added layer is uneven, motivating two practical operating points:

* •

  p=3p=3 as a good tradeoff between quality and runtime, and
* •

  p=6p=6 when the objective is maximum quality and compute budget allows.

This “two-mode” interpretation fits the real deployment view: if the strategy must rebalance under tight time budgets, p=3p=3 is reasonable; if running offline or with higher compute allowances, p=6p=6 is preferable.

![Refer to caption](images/portfolio_value_2025.png)


(a)

![Refer to caption](images/drawdown_2025.png)


(b)

Figure 3: (a) Portfolio value evolution and (b) Drawdown analysis per month of 2025 for each model.

### V-B 2025 Out-of-Sample Performance

Herein, we report the out‑of‑sample results from the 2025 monthly walk‑forward backtest under a consistent transaction cost model. Headline performance metrics are summarized in Table [III](https://arxiv.org/html/2602.14827v1#S5.T3 "TABLE III ‣ V-B 2025 Out-of-Sample Performance ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"), and the pathwise behavior is illustrated by the respective figures.

TABLE III: 2025 Financial Performance Metrics

| Metric | QAOA (XY) | Sim. Annealing | HRP |
| --- | --- | --- | --- |
| Total Return | 30.09% | 24.17% | 10.88% |
| Sharpe Ratio | 1.81 | 1.31 | 0.98 |
| Volatility | 18.55% | 19.53% | 10.65% |
| Max Drawdown | -8.27% | -9.26% | -8.40% |
| Turnover (Monthly) | 76.8% | 21.0% | 21.6% |

#### V-B1 Performance Metrics

As shown in Table [III](https://arxiv.org/html/2602.14827v1#S5.T3 "TABLE III ‣ V-B 2025 Out-of-Sample Performance ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") and Fig. [3](https://arxiv.org/html/2602.14827v1#S5.F3 "Figure 3 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(a), the QAOA-XY model demonstrated consistent outperformance in the 2025 backtest exhibiting the highest total return of 30.09%30.09\%, while SA and HRP resulted in 24.17%24.17\% and 10.88%10.88\% return, respectively. This shows that QAOA creates a portfolio with almost 25%25\% higher value compared to the portfolio created by the SA, within 2025. The portfolio value trajectories (Fig. [3](https://arxiv.org/html/2602.14827v1#S5.F3 "Figure 3 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(a)) show QAOA leading SA and HRP over most of the year, with the performance gap widening toward late 2025.

In addition, the maximum drawdown values are of similar magnitude across methods, with QAOA‑XY at −8.27%-8.27\%, SA at −9.26%-9.26\%, and HRP at −8.40%-8.40\%. The drawdown series shown in Fig. [3](https://arxiv.org/html/2602.14827v1#S5.F3 "Figure 3 ‣ V-A Depth Scaling: Validating the Ansatz ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing")(b) indicate that the strategies experience broadly similar drawdown episodes, although QAOA seems to improve its drawdown trend much earlier than SA and HRP already at the third month of testing (2025-05). Therefore, it is important to highlight that QAOA‑XY improves return relative to SA without incurring a materially larger drawdown, indicating a more favorable realized risk–return trade‑off.

More importantly, with a Sharpe Ratio of 1.81, QAOA outperformed SA (1.31) by 38%. This indicates that the quantum algorithm found portfolio combinations that SA missed — suggesting “narrow” global minima in the energy landscape that stochastic thermal hopping overshot. This is also summarized in Fig. [4](https://arxiv.org/html/2602.14827v1#S5.F4 "Figure 4 ‣ V-B1 Performance Metrics ‣ V-B 2025 Out-of-Sample Performance ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") where the risk-return profile is plotted, showing the QAOA to achieve both higher return and lower volatility compared with the SA, hence the higher Sharpe Ratio. As expected, the HRP achieves the lowest volatility but with significantly lower total return, therefore scoring a Sharpe Ratio of 0.98.

![Refer to caption](images/risk_return_2025.png)


Figure 4: The risk-return profile for 2025, for the three models. QAOA exhibits the highest total return from the three models, and for lower volatility than SA. As expected, the HRP results in the lowest volatility but with significantly lower return, as well.

#### V-B2 The Turnover Trade-off

A striking feature in our findings is QAOA’s high average monthly turnover being 76.8%76.8\% vs 21.0%21.0\% for SA and 21.6%21.6\% for HRP, as shown in Table [III](https://arxiv.org/html/2602.14827v1#S5.T3 "TABLE III ‣ V-B 2025 Out-of-Sample Performance ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"). Figure [5](https://arxiv.org/html/2602.14827v1#S5.F5 "Figure 5 ‣ V-B2 The Turnover Trade-off ‣ V-B 2025 Out-of-Sample Performance ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") confirms this in both the average turnover bar chart and the time-series panel, where QAOA‑XY exhibits repeated spikes above typical “high turnover” thresholds. QAOA‑XY (with constraint-preserving evolution) more aggressively re-optimizes within the feasible KK-subspace each month, which can produce large changes in selected subsets and/or weight re-allocations. While SA tends to stick to a local minimum across rebalancing periods due to its “warm start” nature, QAOA, initialized via Trotterization, effectively resolves the selection problem more aggressively each rebalance, resulting in lower-cost solutions under the tested objective.

* •

  Pros: Captures short-term alpha and momentum shifts instantly.
* •

  Cons: Incurs higher transaction costs.

This suggests QAOA is best suited for liquid, low-fee environments (e.g., U.S. Large Cap) rather than illiquid credit or emerging markets. For settings where market impact and slippage dominate, the next methodological step would be to incorporate turnover explicitly into the selection objective (multi-period coupling / temporal regularization), rather than relying only on a small continuity bonus.

![Refer to caption](images/turnover_analysis_2025.png)


(a)

![Refer to caption](images/turnover_time.png)


(b)

Figure 5: (a) Average monthly turnover by strategy, (b) Turnover over time for 2025 per strategy.

### V-C Portfolio Composition and Allocation Dynamics

In Fig. [6](https://arxiv.org/html/2602.14827v1#S5.F6 "Figure 6 ‣ V-C Portfolio Composition and Allocation Dynamics ‣ V Results and Discussion ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing") we plot the monthly weight allocation for each method. As expected, HRP produces relatively smooth allocations across time reflecting its diversification-first construction and continuous nature. On the contrary, QAOA‑XY shows pronounced reallocations in which certain assets become dominant (high weights) in some months and de-emphasized later. This qualitative picture aligns with the occurring high turnover costs discussed earlier for the QAOA approach.

The heatmap provides an interesting interpretability angle: QAOA‑XY behaves like a high-conviction strategy that rapidly reconfigures/adapts the portfolio to the most attractive discrete subset under the current window estimates. That is beneficial for responsiveness when market structure shifts and fast adaptation is desired, but costly in environments where turnover is penalized. HRP is stable and diversified, but in this sample it sacrifices return. Lastly, Simulated Annealing sits between these extremes of QAOA and HRP, showing periods of concentration and periods of reallocation, but typically less extreme month-to-month reshuffling than QAOA‑XY, and consistently for the same assets.

Because QAOA‑XY evolves strictly within the KK-hot feasible manifold (via Dicke initialization and XY mixing) and then applies a feasibility filter at readout, observed portfolio selections are always valid by construction. This makes the allocation heatmap and selection changes easier to interpret operationally: changes reflect genuine shifts in the objective landscape rather than penalty “leakage” into invalid portfolios.

![Refer to caption](images/weight_allocation_2025.png)


Figure 6: Asset weight allocation over time in 2025.

## VI Conclusion & Future Outlook

This paper studied cardinality-constrained portfolio selection in the context of Direct Indexing and proposed a constraint-preserving QAOA formulation that operates strictly within the feasible KK-of-NN subspace. QAOA is not merely a theoretical curiosity but a viable candidate for the next generation of Fintech solvers. By utilizing Dicke States and XY-Mixers, the quantum evolution explores only valid portfolios of size KK, eliminating the penalty-tuning problem that plagues classical solvers.

Empirically, the depth-scaling diagnostics support both expressibility and trainability in the tested regime (N=10N=10, K=5K=5, p≤6p\leq 6). Increasing circuit depth generally improved the achieved cost values, and the reported gradient norms remained well above vanishing levels through p=6p=6, indicating that the optimization procedure remains numerically learnable under the trotterized initialization used here. In addition, our Trotterized Initialization strategy proved robust against Barren Plateaus up to depth p=6p=6, showcasing that such parameter ramps can provide stable warmtstarts for training QAOA circuits at moderate depths in practical instances of constrained portfolio selection.

In the 2025 monthly walk-forward backtest, QAOA-XY achieved the strongest overall performance among the compared methods, reporting 30.09%30.09\% total return and a 1.811.81 Sharpe Ratio versus 24.17%24.17\% and 1.311.31 for Simulated Annealing, and 10.88%10.88\% return with 0.980.98 SR for HRP, respectively. Importantly, this outperformance did not coincide with materially worse drawdowns in the tested year, indicating that the improvement is not solely explained by higher realized downside risk. For business application, the superior Sharpe Ratio resulted by the QAOA approach justifies the integration of quantum-inspired solvers into Direct Indexing platforms, provided transaction costs are managed.

The primary practical limitation observed is turnover: QAOA-XY exhibited substantially higher average monthly turnover (76.8%76.8\%) than the classical baselines (≈21%\approx 21\%). While performance remains favorable under the cost model applied in this study, turnover at this level can become prohibitive when incorporating realistic slippage and market impact, especially outside highly liquid large-cap universes. This highlights a core implementation trade-off: improved discrete selection quality may come at the cost of more frequent reallocation, and real-world deployment should treat turnover as a first-class objective rather than a secondary diagnostic.

Future Work: Future research directions naturally follow from these findings.

1. 1.

   Turnover can be addressed by incorporating explicit trading frictions/costs or temporal regularization directly into the selection objective, e.g., via multi-period coupling terms that penalize changes in holdings across rebalances. Another approach to try taming the turnover could possibly be to increase continuity bonus or add explicit turnover penalty to QAOA cost.
2. 2.

   Scaling beyond N=10N=10 requires additional investigation: while the constraint-preserving approach reduces the effective search space to the Hamming-weight-KK subspace, circuit depth, optimizer stability, and sampling/readout policies will likely require adjustment as NN grows.
3. 3.

   Broader robustness evaluation—across longer horizons, different market regimes, and alternative asset universes—would help characterize when constraint-preserving QAOA offers the largest advantage relative to classical heuristics.
4. 4.

   Implementing and testing the circuit on noisy hardware, or under realistic noise models, would clarify the sensitivity of the observed benefits to NISQ limitations and guide hardware-aware ansatz design.

Overall, the results support the conclusion that constraint-preserving QAOA is a viable and interpretable approach for hard-constrained portfolio selection, with a clear pathway toward institutional relevance provided that turnover-aware objectives and scaling/robustness questions are addressed in future work.

## References

* [1]
  I. Anadani, A. Sharma, D. Dave, and A. Sharma (2024)
  A genetic algorithm approach for portfolio optimization.
  In Data Science and Applications, S. J. Nanda, R. P. Yadav, A. H. Gandomi, and M. Saraswat (Eds.),
  Singapore,  pp. 113–124.
  External Links: ISBN 978-981-99-7862-5
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p4.1 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [2]
  D. H. Bailey and M. López de Prado (2012)
  The sharpe ratio efficient frontier.
  Journal of Risk 15 (2),  pp. 3–44.
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p2.4 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"),
  [§II-A](https://arxiv.org/html/2602.14827v1#S2.SS1.p1.1 "II-A Classical Portfolio Optimization ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [3]
  D. Bertsimas, C. Darnell, and R. Soucy (1999)
  Portfolio construction through mixed-integer programming at Grantham, Mayo, Van Otterloo and Company.
  Interfaces 29 (1),  pp. 49–66.
  Cited by: [§II-B](https://arxiv.org/html/2602.14827v1#S2.SS2.p1.3 "II-B The “Combinatorial Cliff” in Asset Management ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [4]
  D. Bienstock (1996)
  Computational study of a family of mixed-integer quadratic programming problems.
  Mathematical Programming 74 (2),  pp. 121–140.
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p2.4 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [5]
  E. Farhi, J. Goldstone, and S. Gutmann (2014)
  A quantum approximate optimization algorithm.
  arXiv preprint arXiv:1411.4028.
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p4.1 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"),
  [§II-D](https://arxiv.org/html/2602.14827v1#S2.SS4.p2.1 "II-D Quantum Computing in Finance ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [6]
  F. Glover, G. Kochenberger, and Y. Du (2019)
  A tutorial on formulating and using QUBO models.
  arXiv preprint arXiv:1811.11538.
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p4.1 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [7]
  E. Jurczenko (2016)
  Risk-based and factor investing.
   ISTE Press - Elsevier.
  External Links: ISBN 978-1-78548-008-9
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p2.4 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"),
  [§II-A](https://arxiv.org/html/2602.14827v1#S2.SS1.p1.1 "II-A Classical Portfolio Optimization ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [8]
  S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi (1983)
  Optimization by simulated annealing.
  Science 220 (4598),  pp. 671–680.
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p4.1 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [9]
  H. Lang et al. (2022)
  Quantum annealing for combinatorial optimization: a comparative study.
  IEEE Transactions on Quantum Engineering 3,  pp. 1–15.
  Cited by: [§II-D](https://arxiv.org/html/2602.14827v1#S2.SS4.p3.1 "II-D Quantum Computing in Finance ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [10]
  O. Ledoit and M. Wolf (2004)
  Honey, i shrunk the sample covariance matrix.
  The Journal of Portfolio Management 30 (4),  pp. 110–119.
  Cited by: [§II-A](https://arxiv.org/html/2602.14827v1#S2.SS1.p2.1 "II-A Classical Portfolio Optimization ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [11]
  M. López de Prado (2016)
  Building diversified portfolios that outperform out of sample.
  The Journal of Financial Data Science 1 (1),  pp. 9–18.
  Note: (Hierarchical Risk Parity)
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p3.1 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"),
  [§II-A](https://arxiv.org/html/2602.14827v1#S2.SS1.p2.1 "II-A Classical Portfolio Optimization ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [12]
  H. Markowitz (1952)
  Portfolio selection.
  The Journal of Finance 7 (1),  pp. 77–91.
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p2.4 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"),
  [§II-A](https://arxiv.org/html/2602.14827v1#S2.SS1.p1.1 "II-A Classical Portfolio Optimization ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [13]
  R. O. Michaud and R. O. Michaud (2008)
  Efficient asset management: a practical guide to stock portfolio optimization and asset allocation.
  2nd edition, Oxford University Press.
  Cited by: [§I](https://arxiv.org/html/2602.14827v1#S1.p2.4 "I Introduction ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing"),
  [§II-A](https://arxiv.org/html/2602.14827v1#S2.SS1.p1.1 "II-A Classical Portfolio Optimization ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [14]
  R. Orús, S. Mugel, and E. Lizaso (2019)
  Quantum computing for finance: overview and prospects.
  Reviews in Physics 4,  pp. 100028.
  Cited by: [§II-D](https://arxiv.org/html/2602.14827v1#S2.SS4.p1.1 "II-D Quantum Computing in Finance ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").
* [15]
  J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L. Wossnig, I. Rungger, G. H. Booth, and J. Tennyson (2022)
  The variational quantum eigensolver: a review of methods and best practices.
  Quantum Physics [quant-ph] (arXiv:2111.05176v3).
  Cited by: [§II-D](https://arxiv.org/html/2602.14827v1#S2.SS4.p3.1 "II-D Quantum Computing in Finance ‣ II Literature Review - Business Application & Context ‣ Constrained Portfolio Optimization via Quantum Approximate Optimization Algorithm (QAOA) with XY-Mixers and Trotterized Initialization: A Hybrid Approach for Direct Indexing").