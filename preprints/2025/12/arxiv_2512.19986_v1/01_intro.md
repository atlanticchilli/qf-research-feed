---
authors:
- Nikolaos Iliopoulos
doc_id: arxiv:2512.19986v1
family_id: arxiv:2512.19986
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization
url_abs: http://arxiv.org/abs/2512.19986v1
url_html: https://arxiv.org/html/2512.19986v1
venue: arXiv q-fin
version: 1
year: 2025
---


Nikolaos Iliopoulos
  
Rakuten Institute of Technology
  
nick.iliopoulos@rakuten.com

###### Abstract

Metaheuristic algorithms for cardinality-constrained portfolio optimization require repair operators to map infeasible candidates onto the feasible region. Standard Euclidean projection treats assets as independent and can ignore the covariance structure that governs portfolio risk, potentially producing less diversified portfolios. This paper introduces Covariance-Aware Simplex Projection (CASP), a two-stage repair operator that (i) selects a target number of assets using volatility-normalized scores and (ii) projects the candidate weights using a covariance-aware geometry aligned with tracking-error risk. This provides a portfolio-theoretic foundation for using a covariance-induced distance in repair operators. On S&P 500 data (2020–2024), CASP-Basic delivers materially lower portfolio variance than standard Euclidean repair without relying on return estimates, with improvements that are robust across assets and statistically significant. Ablation results indicate that volatility-normalized selection drives most of the variance reduction, while the covariance-aware projection provides an additional, consistent improvement. We further show that optional return-aware extensions can improve Sharpe ratios, and out-of-sample tests confirm that gains transfer to realized performance. CASP integrates as a drop-in replacement for Euclidean projection in metaheuristic portfolio optimizers.

Keywords: Cardinality-constrained portfolio optimization; Repair operators; Covariance-aware simplex projection; Tracking error; Metaheuristics; ESG integration

## 1  Introduction

Portfolio optimization represents one of the most important problems in quantitative finance, with roots extending back to Markowitz’s seminal mean-variance framework [[1](https://arxiv.org/html/2512.19986v1#bib.bib1)]. The central insight, that rational investors should consider both expected returns and the covariance structure of assets, has profoundly influenced both academic research and practical portfolio construction [[2](https://arxiv.org/html/2512.19986v1#bib.bib2), [3](https://arxiv.org/html/2512.19986v1#bib.bib3)].

In practice, portfolio managers face constraints beyond the simple budget requirement that weights sum to one. Cardinality constraints limiting portfolios to KK assets from a universe of NN reflect essential practical considerations: transaction costs scale with the number of positions, monitoring complexity increases with portfolio breadth, and regulatory requirements often mandate concentration limits [[4](https://arxiv.org/html/2512.19986v1#bib.bib4), [5](https://arxiv.org/html/2512.19986v1#bib.bib5)]. When K≪NK\ll N, the feasible region fragments into (NK)\binom{N}{K} disjoint simplices, transforming the optimization problem from convex to combinatorial and rendering it NP-hard [[4](https://arxiv.org/html/2512.19986v1#bib.bib4)].

This computational complexity has motivated extensive research on metaheuristic approaches, including genetic algorithms [[4](https://arxiv.org/html/2512.19986v1#bib.bib4)], particle swarm optimization [[6](https://arxiv.org/html/2512.19986v1#bib.bib6)], differential evolution [[3](https://arxiv.org/html/2512.19986v1#bib.bib3)], and grey wolf optimizers [[7](https://arxiv.org/html/2512.19986v1#bib.bib7), [8](https://arxiv.org/html/2512.19986v1#bib.bib8)]. A fundamental requirement of all such methods is a repair operator that maps infeasible candidate solutions onto the feasible region, ensuring that the evolutionary search operates within the constraint set [[9](https://arxiv.org/html/2512.19986v1#bib.bib9)].

Alongside risk and return, Environmental, Social, and Governance (ESG) criteria have become a mainstream consideration in portfolio construction, with global ESG-mandated assets exceeding $16.7 trillion [[10](https://arxiv.org/html/2512.19986v1#bib.bib10)]. We therefore adopt a tri-objective formulation that optimizes variance, expected return, and portfolio-level ESG quality simultaneously, providing a realistic testbed for evaluating repair operators in modern investment contexts.

The standard approach projects infeasible candidates using Euclidean distance, solving:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wEuc∗=arg⁡minw∈𝒲⁡‖w−z‖22w^{\*}\_{\text{Euc}}=\arg\min\_{w\in\mathcal{W}}\|w-z\|\_{2}^{2} |  | (1) |

where zz is the infeasible candidate and 𝒲\mathcal{W} is the feasible region. This formulation treats assets as independent and ignores their correlation structure, a fundamental mismatch with portfolio theory, which emphasizes that asset interactions determine portfolio risk [[11](https://arxiv.org/html/2512.19986v1#bib.bib11)].

We propose Covariance-Aware Simplex Projection (CASP), which replaces Euclidean distance with a covariance-induced (tracking-error) metric:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wCASP∗=argminw∈𝒲(w−z)⊤Ω(w−z)w^{\*}\_{\text{CASP}}=\arg\min\_{w\in\mathcal{W}}(w-z)^{\top}\Omega(w-z) |  | (2) |

where Ω\Omega is the asset covariance matrix. We establish that this formulation minimizes tracking error variance relative to the infeasible candidate, providing a portfolio-theoretic interpretation that connects the projection geometry to financial risk measurement.

## 2  Contributions

This paper makes the following contributions to the literature on portfolio optimization and constraint handling:

1. 1.

   Risk-based repair operator with a portfolio-theoretic interpretation. We replace Euclidean projection with a covariance-induced objective, (w−z)⊤​Ω​(w−z)(w-z)^{\top}\Omega(w-z), and show that it is exactly the tracking error variance between the repaired portfolio ww and the candidate zz. This yields a principled repair step that preserves proximity in risk space, consistent with modern portfolio theory.
2. 2.

   Benchmarking design and attribution of performance drivers. We decompose CASP into (a) volatility-normalized asset selection and (b) covariance-aware (Ω\Omega-metric) projection, with optional return-aware extensions. To isolate the effect of projection geometry from selection, we introduce a selection-matched baseline (VolNorm+Euc) that uses the same selection rule as CASP but applies standard Euclidean projection. This experimental design enables a clean attribution of improvements to selection versus projection geometry.

## 3  Related Work

### 3.1  Portfolio Optimization Theory

Modern portfolio theory originated with Markowitz’s mean-variance framework [[1](https://arxiv.org/html/2512.19986v1#bib.bib1)], which formalized the trade-off between expected return and risk as measured by portfolio variance. The Capital Asset Pricing Model [[12](https://arxiv.org/html/2512.19986v1#bib.bib12)] extended this framework to asset pricing, while subsequent work developed robust estimation techniques for covariance matrices [[13](https://arxiv.org/html/2512.19986v1#bib.bib13), [14](https://arxiv.org/html/2512.19986v1#bib.bib14)]. Recent research by Taljaard and Maré [[15](https://arxiv.org/html/2512.19986v1#bib.bib15)] demonstrated that estimation error can cause sophisticated optimization approaches to underperform naive diversification strategies, highlighting the importance of regularization and out-of-sample validation.

The addition of cardinality constraints was first studied by Chang et al. [[4](https://arxiv.org/html/2512.19986v1#bib.bib4)], who proved NP-hardness and proposed genetic algorithms. Recent advances include Kobayashi et al. [[16](https://arxiv.org/html/2512.19986v1#bib.bib16)], who proposed cutting-plane approaches for cardinality-constrained mean-CVaR optimization, and Cesarone et al. [[5](https://arxiv.org/html/2512.19986v1#bib.bib5)], who demonstrated that optimally chosen small portfolios can outperform large ones. Kalayci et al. [[3](https://arxiv.org/html/2512.19986v1#bib.bib3)] provide a comprehensive survey of metaheuristic approaches to cardinality-constrained portfolio optimization.

### 3.2  ESG Integration in Portfolio Management

ESG investing has evolved from a niche concern to a mainstream investment approach. Pedersen et al. [[17](https://arxiv.org/html/2512.19986v1#bib.bib17)] developed the theoretical framework for ESG-efficient frontiers, demonstrating conditions under which ESG integration can improve risk-adjusted returns through better information incorporation. Avramov et al. [[18](https://arxiv.org/html/2512.19986v1#bib.bib18)] extended this framework to account for ESG rating uncertainty, while Escobar-Saldívar et al. [[19](https://arxiv.org/html/2512.19986v1#bib.bib19)] use two decades of U.S. stock panel data to show that high ESG levels are associated with lower returns and higher volatility, whereas improvements in ESG scores predict higher short-term returns and lower risk. However, significant disagreement across ESG rating providers persists due to methodological differences, complicating their consistent application in practice [[20](https://arxiv.org/html/2512.19986v1#bib.bib20)].

### 3.3  Metaheuristics for Multi-Objective Optimization

Multi-objective evolutionary algorithms have become the dominant paradigm for approximating Pareto fronts in complex optimization problems. NSGA-II [[21](https://arxiv.org/html/2512.19986v1#bib.bib21)] introduced fast non-dominated sorting with crowding distance for diversity preservation. The Grey Wolf Optimizer [[7](https://arxiv.org/html/2512.19986v1#bib.bib7)] simulates the social hierarchy and collaborative hunting behavior of grey wolf packs. Multi-objective extensions [[8](https://arxiv.org/html/2512.19986v1#bib.bib8)] have been successfully applied to portfolio problems [[2](https://arxiv.org/html/2512.19986v1#bib.bib2), [6](https://arxiv.org/html/2512.19986v1#bib.bib6)]. Recent advances include surrogate-assisted deep reinforcement learning for expensive multi-objective problems [[22](https://arxiv.org/html/2512.19986v1#bib.bib22)], hybrid deep learning evolutionary portfolio optimizers [[23](https://arxiv.org/html/2512.19986v1#bib.bib23)], and metaheuristics tailored for rich portfolio settings [[24](https://arxiv.org/html/2512.19986v1#bib.bib24)].

### 3.4  Constraint Handling in Evolutionary Algorithms

Constraint-handling techniques for portfolio optimization include penalty functions, repair operators, and decoder-based approaches [[3](https://arxiv.org/html/2512.19986v1#bib.bib3)]. For cardinality-constrained problems, repair operators have proven particularly effective [[6](https://arxiv.org/html/2512.19986v1#bib.bib6)]. Liagkouras and Metaxiotis [[9](https://arxiv.org/html/2512.19986v1#bib.bib9)] proposed two-phase repair combining asset selection with rebalancing. Gambeta and Kwon [[25](https://arxiv.org/html/2512.19986v1#bib.bib25)] developed relaxed constraint handling for risk parity portfolios.

Projection onto the probability simplex is a fundamental optimization primitive. Condat [[26](https://arxiv.org/html/2512.19986v1#bib.bib26)] achieved O​(N)O(N) complexity using pivoting for Euclidean projection. However, Euclidean projection treats assets as independent and can be suboptimal when the true objective is risk-based: Bongiorno and Challet [[27](https://arxiv.org/html/2512.19986v1#bib.bib27)] showed that covariance estimators optimized under Euclidean (Frobenius) distance are misaligned with the covariance-weighted risk objective of portfolio optimization. This motivates exploring covariance-metric (Ω\Omega-metric) projection, which aligns the repair geometry with tracking error variance.

### 3.5  Mahalanobis-type and Covariance-Aware Distances

The Mahalanobis distance [[28](https://arxiv.org/html/2512.19986v1#bib.bib28)] accounts for variable correlations and scales. In portfolio contexts, Ledoit and Wolf [[13](https://arxiv.org/html/2512.19986v1#bib.bib13), [14](https://arxiv.org/html/2512.19986v1#bib.bib14)] used covariance-aware metrics for shrinkage estimation, while Bodnar et al. [[29](https://arxiv.org/html/2512.19986v1#bib.bib29)] analyzed mean-variance efficiency under covariance uncertainty. Butin [[30](https://arxiv.org/html/2512.19986v1#bib.bib30)] studied distances to simplices under standard norm-based metrics, but did not consider projections under covariance-weighted quadratic forms. The application of covariance-aware projection to portfolio repair operators remains understudied.

## 4  Problem Formulation

Consider an investment universe of NN assets with expected return vector μ∈ℝN\mu\in\mathbb{R}^{N}, positive definite covariance matrix Ω∈ℝN×N\Omega\in\mathbb{R}^{N\times N}, and ESG quality scores e∈ℝNe\in\mathbb{R}^{N}. A portfolio is represented by weight vector w∈ℝNw\in\mathbb{R}^{N} where component wiw\_{i} denotes the fraction of capital allocated to asset ii. We formulate a tri-objective optimization problem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minw\displaystyle\min\_{w}\; | f1​(w)=w⊤​Ω​w(variance)\displaystyle f\_{1}(w)=w^{\top}\Omega w\quad\text{(variance)} |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxw\displaystyle\max\_{w}\; | f2​(w)=μ⊤​w(return)\displaystyle f\_{2}(w)=\mu^{\top}w\quad\text{(return)} |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxw\displaystyle\max\_{w}\; | f3​(w)=e⊤​w(ESG)\displaystyle f\_{3}(w)=e^{\top}w\quad\text{(ESG)} |  | (5) |

subject to constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏⊤​w=1,wi≥0∀i(budget)\displaystyle\mathbf{1}^{\top}w=1,\quad w\_{i}\geq 0\quad\forall i\quad\text{(budget)} |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖w‖0≤K(cardinality)\displaystyle\|w\|\_{0}\leq K\quad\text{(cardinality)} |  | (7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | wi=0​ or ​wi∈[ℓ,u]∀i(box)\displaystyle w\_{i}=0\text{ or }w\_{i}\in[\ell,u]\quad\forall i\quad\text{(box)} |  | (8) |

The cardinality constraint combined with the simplex constraint creates a feasible region 𝒲\mathcal{W} comprising (NK)\binom{N}{K} disjoint simplices, each corresponding to a specific subset of KK active assets. Given an infeasible candidate z∈ℝNz\in\mathbb{R}^{N} from a metaheuristic search, the repair operator must project zz onto 𝒲\mathcal{W}.

## 5  Methodology

### 5.1  Theoretical Foundation

###### Definition 1 (Tracking-error metric (covariance-induced distance)).

We define the Ω\Omega-induced distance between a,b∈ℝNa,b\in\mathbb{R}^{N} as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dΩ​(a,b)=(a−b)⊤​Ω​(a−b)d\_{\Omega}(a,b)=\sqrt{(a-b)^{\top}\Omega(a-b)} |  | (9) |

###### Remark 1 (Terminology).

The classical statistical Mahalanobis distance is typically defined using Ω−1\Omega^{-1}. We use Ω\Omega so that dΩ2d\_{\Omega}^{2} equals tracking error variance (Proposition [1](https://arxiv.org/html/2512.19986v1#Thmproposition1 "Proposition 1 (Tracking Error Interpretation). ‣ 5.1 Theoretical Foundation ‣ 5 Methodology ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization")), which is the portfolio-relevant notion of proximity.

###### Proposition 1 (Tracking Error Interpretation).

For portfolios w1,w2w\_{1},w\_{2} invested in assets with covariance matrix Ω\Omega, the squared Ω\Omega-induced distance equals tracking error variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dΩ​(w1,w2)2=Var​[Rw1−Rw2]d\_{\Omega}(w\_{1},w\_{2})^{2}=\text{Var}[R\_{w\_{1}}-R\_{w\_{2}}] |  | (10) |

where Rw=w⊤​rR\_{w}=w^{\top}r denotes portfolio return.

Proof.
Let rr denote the random vector of asset returns with covariance matrix Ω\Omega. The tracking error (return difference) is Rw1−Rw2=(w1−w2)⊤​rR\_{w\_{1}}-R\_{w\_{2}}=(w\_{1}-w\_{2})^{\top}r. Its variance is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​[(w1−w2)⊤​r]\displaystyle\text{Var}[(w\_{1}-w\_{2})^{\top}r] | =(w1−w2)⊤​Ω​(w1−w2)\displaystyle=(w\_{1}-w\_{2})^{\top}\Omega(w\_{1}-w\_{2}) |  | (11) |
|  |  | =dΩ​(w1,w2)2\displaystyle=d\_{\Omega}(w\_{1},w\_{2})^{2} |  |

This proposition provides the financial justification for CASP: by minimizing the Ω\Omega-induced distance, we find the feasible portfolio with minimum tracking error variance relative to the infeasible candidate. This is a natural metric for portfolio proximity because it accounts for how assets move together. Figure [1](https://arxiv.org/html/2512.19986v1#S5.F1 "Figure 1 ‣ 5.1 Theoretical Foundation ‣ 5 Methodology ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") illustrates the geometric difference: Euclidean projection uses circular contours that ignore correlations, while Ω\Omega-metric projection uses elliptical contours aligned with the covariance structure.

###### Corollary 1 (Diversification Benefit).

Ω\Omega-metric projection penalizes concentration in correlated assets more heavily than Euclidean projection, naturally encouraging diversification.

![Refer to caption](x1.png)


Figure 1: Geometric intuition for covariance-aware projection. The gray triangle represents the feasible region (simplex) where portfolio weights are non-negative and sum to one. Given an infeasible candidate zz, (a) Euclidean projection finds the nearest feasible point using circular iso-distance contours, treating assets as independent. (b) Ω\Omega-metric projection (CASP) uses elliptical contours aligned with the covariance structure, finding the feasible point with minimum tracking error variance.

### 5.2  Two-Stage Algorithm

The CASP algorithm operates in two stages: asset selection followed by constrained projection. The complete procedure is summarized in Algorithm [1](https://arxiv.org/html/2512.19986v1#alg1 "Algorithm 1 ‣ 5.2 Two-Stage Algorithm ‣ 5 Methodology ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization").

Stage 1: Volatility-normalized asset selection.
We select KK assets using scores that normalize by individual volatility:

|  |  |  |  |
| --- | --- | --- | --- |
|  | si=|zi|Ωi​is\_{i}=\frac{|z\_{i}|}{\sqrt{\Omega\_{ii}}} |  | (12) |

This ensures that high-volatility assets are not selected merely due to larger absolute signal values. The KK assets with highest scores form the active set SS.

Stage 2: Ω\Omega-metric (tracking-error) projection.
For the selected asset set SS with |S|=K|S|=K, we solve:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minwS\displaystyle\min\_{w\_{S}}\; | 12​(wS−zS)⊤​ΩS​(wS−zS)\displaystyle\tfrac{1}{2}(w\_{S}-z\_{S})^{\top}\Omega\_{S}(w\_{S}-z\_{S}) |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | s.t. | 𝟏⊤​wS=1,ℓ≤wS,i≤u∀i∈S\displaystyle\mathbf{1}^{\top}w\_{S}=1,\quad\ell\leq w\_{S,i}\leq u\quad\forall i\in S |  | (14) |

where ΩS\Omega\_{S} is the submatrix of Ω\Omega corresponding to selected assets. This is a convex quadratic program with linear constraints, solvable efficiently via SLSQP or active-set methods.

###### Remark 2 (Two-stage heuristic vs global projection).

Because the feasible set is a union of simplices over all (NK)\binom{N}{K} active sets, the global Ω\Omega-metric projection onto 𝒲\mathcal{W} would require a combinatorial search over subsets. CASP is therefore a two-stage heuristic: it selects SS first, then computes the exact constrained Ω\Omega-metric projection on that simplex.

Algorithm 1  CASP: Covariance-Aware Simplex Projection

0: Candidate z∈ℝNz\in\mathbb{R}^{N}, covariance Ω\Omega, cardinality KK, bounds [ℓ,u][\ell,u]

0: Feasible portfolio w∗∈𝒲w^{\*}\in\mathcal{W}

1: Compute volatilities σi=Ωi​i\sigma\_{i}=\sqrt{\Omega\_{ii}}

2: Compute selection scores si=|zi|/σis\_{i}=|z\_{i}|/\sigma\_{i} for all ii

3: S←S\leftarrow indices of top KK scores

4: Extract zSz\_{S}, ΩS\Omega\_{S} for selected assets

5: Solve QP ([13](https://arxiv.org/html/2512.19986v1#S5.E13 "In 5.2 Two-Stage Algorithm ‣ 5 Methodology ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization")) to obtain wS∗w\_{S}^{\*}

6: w∗←𝟎Nw^{\*}\leftarrow\mathbf{0}\_{N}; set wS∗←wS∗w^{\*}\_{S}\leftarrow w\_{S}^{\*}

7: return w∗w^{\*}

Complexity Analysis. Stage 1 requires O​(N)O(N) for partial sorting via argpartition. Stage 2 solves a KK-dimensional QP, requiring O​(K3)O(K^{3}) in the worst case but typically much faster with warm starts. Total complexity is O​(N+K3)O(N+K^{3}), dominated by the O​(N2)O(N^{2}) covariance matrix operations in fitness evaluation.

### 5.3  Extension: Return-Aware Variant (RA-CASP)

For applications where return incorporation is desired, we extend CASP with return-aware modifications:

Return-Boosted Selection:

|  |  |  |  |
| --- | --- | --- | --- |
|  | si=|zi|⋅(1+λ​μ~i)Ωi​is\_{i}=\frac{|z\_{i}|\cdot(1+\lambda\tilde{\mu}\_{i})}{\sqrt{\Omega\_{ii}}} |  | (15) |

where μ~i=(μi−μmin)/(μmax−μmin)∈[0,1]\tilde{\mu}\_{i}=(\mu\_{i}-\mu\_{\min})/(\mu\_{\max}-\mu\_{\min})\in[0,1] is normalized expected return and λ≥0\lambda\geq 0 controls return-awareness.

Return-Regularized Projection:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minwS⁡12​(wS−zS)⊤​ΩS​(wS−zS)−γ​μ~S⊤​wS\min\_{w\_{S}}\tfrac{1}{2}(w\_{S}-z\_{S})^{\top}\Omega\_{S}(w\_{S}-z\_{S})-\gamma\tilde{\mu}\_{S}^{\top}w\_{S} |  | (16) |

where γ≥0\gamma\geq 0 biases the projection toward higher-return portfolios.

Remark on Evaluation. When using return-aware variants, care must be taken in performance evaluation to avoid circularity. We address this through: (a) ablation studies that isolate contributions, and (b) out-of-sample validation where return estimates are formed on training data only.

## 6  Experimental Setup

### 6.1  Data Sources

We construct our experimental dataset from real financial market data. Daily adjusted closing prices for 100 S&P 500 constituents are obtained via Yahoo Finance from January 2, 2020 to November 29, 2024 (1,237 trading days). The universe includes major constituents across all sectors: technology (AAPL, MSFT, NVDA, GOOGL, META), healthcare (JNJ, UNH, LLY, PFE), financials (JPM, BAC, GS), energy (XOM, CVX), and others. Expected returns are computed as annualized mean log returns. The covariance matrix is estimated from daily returns and stabilized via a 10% shrinkage toward the identity matrix (in the spirit of Ledoit–Wolf [[13](https://arxiv.org/html/2512.19986v1#bib.bib13)]) to ensure numerical robustness.

Dataset Statistics. Annualized return range: [−12.3%,54.1%][-12.3\%,54.1\%]. Annualized volatility range: [22.4%,65.5%][22.4\%,65.5\%]. Covariance condition number: 285.0.

ESG Scores. We construct ESG quality scores using (i) real governance risk signals from Yahoo Finance (auditRisk, boardRisk, compensationRisk, shareHolderRightsRisk, overallRisk) and (ii) sector-level environmental/social proxies reflecting typical sector ESG profiles. The composite is ESG=0.4×G+0.6×E​S\text{ESG}=0.4\times G+0.6\times ES, where G=(10−overallRisk)×10G=(10-\text{overallRisk})\times 10 and E​SES is the sector proxy. Scores range from 36.0 to 81.0 in our sample. Because firm-level E and S scores typically require licensed datasets, we treat the ESG objective as an illustrative third objective and focus our main claims on the covariance-aware repair mechanism.

### 6.2  Temporal Data Split

For out-of-sample validation, we partition data temporally:

* •

  Training Period: January 2020 – December 2023 (1,006 trading days)
* •

  Test Period: January 2024 – November 2024 (231 trading days)

All parameter estimation (expected returns, covariance matrix) uses training data only. Test period data is held out for realized performance evaluation.

### 6.3  Experimental Configurations

Portfolio Constraints. Cardinality K=15K=15, weight bounds [ℓ,u]=[2%,15%][\ell,u]=[2\%,15\%], risk-free rate rf=4.5%r\_{f}=4.5\%.

CASP Parameters. CASP-Basic is parameter-free, using only the covariance matrix. The return-aware extension (RA-CASP) introduces two hyperparameters: λ\lambda controls selection bias toward high-return assets, and γ\gamma controls projection bias toward high-return weights. We perform grid search over λ∈{0.4,0.6,0.8,1.0,1.2}\lambda\in\{0.4,0.6,0.8,1.0,1.2\} and γ∈{0.15,0.20,0.25,0.30,0.35}\gamma\in\{0.15,0.20,0.25,0.30,0.35\} using the training period, selecting λ=1.2\lambda=1.2 and γ=0.35\gamma=0.35.

Optimizer. Multi-Objective Grey Wolf Optimizer (MOGWO)  [[8](https://arxiv.org/html/2512.19986v1#bib.bib8)] with population size 50, maximum iterations 100, and archive size 30.

Transaction Costs. We assume 10 basis points per unit of turnover, consistent with institutional trading costs for liquid large-cap equities.

### 6.4  Comparison Methods

We compare seven projection methods to enable comprehensive ablation:

1. 1.

   Euclidean: Standard projection selecting by |zi||z\_{i}| (baseline)
2. 2.

   VolNorm+Euc: Selection by |zi|/Ωi​i|z\_{i}|/\sqrt{\Omega\_{ii}}, Euclidean projection (selection-only baseline)
3. 3.

   MinVar+Euc: Selection by |zi|/Ωi​i|z\_{i}|/\Omega\_{ii}, Euclidean projection
4. 4.

   Sharpe+Euc: Selection by individual Sharpe ratios, Euclidean projection
5. 5.

   CASP-Basic: Volatility-normalized selection, Ω\Omega-metric projection
6. 6.

   CASP-RetSel: Return-aware selection, Ω\Omega-metric projection (no return term)
7. 7.

   RA-CASP: Return-aware selection, return-regularized Ω\Omega-metric projection

### 6.5  Statistical Analysis

We employ the Wilcoxon signed-rank test at significance level α=0.05\alpha=0.05 for pairwise comparisons. Effect sizes are reported using relative improvement percentages. For out-of-sample validation, we report Spearman rank correlation between in-sample and out-of-sample performance to assess prediction quality.

## 7  Results

### 7.1  Ablation Study: Isolating Contributions

Table [1](https://arxiv.org/html/2512.19986v1#S7.T1 "Table 1 ‣ 7.1 Ablation Study: Isolating Contributions ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") and Figure [2](https://arxiv.org/html/2512.19986v1#S7.F2 "Figure 2 ‣ 7.1 Ablation Study: Isolating Contributions ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") present results from 500 random projections, systematically decomposing the contributions of each algorithmic component.

Table 1: Ablation Study: Mean Performance Across 500 Projections (S&P 500 Data)

|  |  |  |  |
| --- | --- | --- | --- |
| Method | Variance | Sharpe | Var Red |
| Euclidean | 0.0524 | 0.276 | — |
| VolNorm+Euc | 0.0449 | 0.241 | 14.3% |
| MinVar+Euc | 0.0399 | 0.232 | 23.9% |
| Sharpe+Euc | 0.0603 | 0.687 | −-15.1% |
| CASP-Basic | 0.0442 | 0.229 | 15.7% |
| CASP-RetSel | 0.0459 | 0.358 | 12.5% |
| RA-CASP | 0.0485 | 0.573 | 7.4% |

![Refer to caption](x2.png)


Figure 2: Ablation study results across 500 random projections. (a) Portfolio variance: VolNorm+Euc shows that volatility-normalized selection explains most of the variance reduction, while CASP-Basic adds an incremental gain via Ω\Omega-metric projection (15.7% total reduction vs Euclidean). (b) Sharpe ratio: return-aware methods achieve higher values but with reduced variance benefits. Dashed line indicates Euclidean baseline.

Key findings:

* •

  VolNorm+Euc achieves 14.3% variance reduction, showing that volatility-normalized selection alone is a strong baseline even with Euclidean projection.
* •

  CASP-Basic achieves 15.7% variance reduction without return information. Relative to VolNorm+Euc, the Ω\Omega-metric projection geometry contributes an additional 1.4% incremental variance reduction (p=8.6×10−5p=8.6\times 10^{-5}), isolating the benefit of using the full covariance structure beyond diagonal scaling.
* •

  MinVar+Euc achieves the largest variance reduction (23.9%) by favoring low-volatility assets, but at the cost of lower mean Sharpe ratios, reflecting a classic risk–return trade-off.
* •

  Return-aware methods (Sharpe+Euc, RA-CASP) achieve higher Sharpe ratios but with smaller or negative variance reductions. The relevant question is whether these improvements persist out-of-sample.

CASP-Basic improves variance against Euclidean with strong significance (p<10−54p<10^{-54}, Wilcoxon signed-rank test).

### 7.2  Out-of-Sample Validation

Table [2](https://arxiv.org/html/2512.19986v1#S7.T2 "Table 2 ‣ 7.2 Out-of-Sample Validation ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") and Figure [3](https://arxiv.org/html/2512.19986v1#S7.F3 "Figure 3 ‣ 7.2 Out-of-Sample Validation ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") present out-of-sample results using parameters estimated on 2020–2023 data and tested on 2024.

Table 2: Out-of-Sample Validation: Walk-Forward Testing (Train: 2020–2023, Test: 2024)

| Method | In-Sample | Out-of-Sample | Corr |
| --- | --- | --- | --- |
|  | Sharpe | Sharpe |  |
| Euclidean | 0.289 | 1.306 | 0.29 |
| VolNorm+Euc | 0.255 | 1.338 | 0.24 |
| CASP-Basic | 0.241 | 1.347 | 0.07 |
| RA-CASP | 0.568 | 1.650 | 0.25 |
| Sharpe+Euc | 0.677 | 1.533 | 0.09 |

![Refer to caption](x3.png)


Figure 3: Out-of-sample validation: in-sample vs. realized Sharpe ratios for 200 portfolio instances (train: 2020–2023, test: 2024). (a) Euclidean shows moderate correlation (ρ≈0.29\rho\approx 0.29). (b) CASP-Basic shows lower rank correlation (ρ≈0.07\rho\approx 0.07), consistent with its return-agnostic design. (c) RA-CASP achieves higher absolute performance with moderate correlation (ρ≈0.25\rho\approx 0.25).

Key findings:

* •

  RA-CASP achieves 26.3% higher out-of-sample Sharpe ratio than Euclidean (1.650 vs 1.306, p<0.0001p<0.0001), suggesting that return-aware improvements partially transfer to realized performance.
* •

  VolNorm+Euc achieves a modest out-of-sample improvement (+2.5%, not significant), indicating that volatility-normalized selection alone can slightly improve realized performance. CASP-Basic improves further (+3.1%, not significant), consistent with a small incremental benefit from covariance-aware projection beyond selection.
* •

  In-sample to out-of-sample rank correlations are positive but method-dependent. Euclidean shows the highest correlation (0.29), while CASP-Basic is lower (0.07); because CASP-Basic is return-agnostic, in-sample Sharpe rankings are not a primary target, so we emphasize mean realized performance rather than rank predictiveness.
* •

  The 2024 test period was favorable for return-aware methods, as the bull market rewarded portfolios tilted toward high-return assets.

### 7.3  Walk-forward Validation Across Market Regimes

To reduce dependence on a single test year, we repeat the out-of-sample evaluation over three expanding-window splits: train 2020–2021 / test 2022, train 2020–2022 / test 2023, and train 2020–2023 / test 2024. Table [3](https://arxiv.org/html/2512.19986v1#S7.T3 "Table 3 ‣ 7.3 Walk-forward Validation Across Market Regimes ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") reports mean realized Sharpe ratios (200 random candidates per split). Results highlight a regime sensitivity: return-aware methods excel in the bull-like 2024 period, but underperform in the 2022 drawdown regime; CASP-Basic is comparatively more stable in 2022 due to its return-agnostic design.

Table 3: Walk-forward out-of-sample Sharpe ratios across test years (expanding window; 200 random candidates per split).

| Method | Test 2022 | Test 2023 | Test 2024 |
| --- | --- | --- | --- |
| Euclidean | −-0.638 | 0.879 | 1.306 |
| VolNorm+Euc | −-0.579 | 0.547 | 1.338 |
| CASP-Basic | −-0.559 | 0.474 | 1.347 |
| RA-CASP | −-0.918 | 0.593 | 1.650 |
| Sharpe+Euc | −-1.090 | 0.846 | 1.533 |

### 7.4  Transaction Cost Analysis

Table [4](https://arxiv.org/html/2512.19986v1#S7.T4 "Table 4 ‣ 7.4 Transaction Cost Analysis ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") reports turnover and an illustrative transaction-cost adjustment across 50 simulated rebalancing events. We report average one-way turnover and implied costs (10 bps per unit turnover). “Net Sharpe” is a simple proxy obtained by subtracting an annualized cost approximation from the gross Sharpe estimate.

Table 4: Turnover and transaction cost proxy (10 bps per unit turnover)

| Method | Avg Turnover | Avg Cost | Net Sharpe |
| --- | --- | --- | --- |
|  |  | (bps) |  |
| Euclidean | 0.565 | 5.65 | 0.261 |
| CASP-Basic | 0.571 | 5.70 | 0.210 |
| RA-CASP | 0.548 | 5.48 | 0.552 |

Key findings:

* •

  RA-CASP achieves slightly lower turnover (0.548 vs 0.565) and, due to higher gross Sharpe, remains favorable under the cost proxy (0.552 vs 0.261).
* •

  Transaction costs are modest (5.5–5.7 bps per rebalance), indicating that the turnover differences across methods are small in absolute terms.

### 7.5  Optimization Results

Table [5](https://arxiv.org/html/2512.19986v1#S7.T5 "Table 5 ‣ 7.5 Optimization Results ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization") presents results from 15 independent MOGWO runs with different projection operators.

Table 5: Optimization Results: 15 Independent MOGWO Runs

| Method | Best Sharpe | Best Return | Hypervolume |
| --- | --- | --- | --- |
| Euclidean | 0.861 | 0.229 | 0.0040 |
| CASP-Basic | 0.703 | 0.186 | 0.0027 |
| RA-CASP | 1.137 | 0.337 | 0.0142 |
| Sharpe+Euc | 1.145 | 0.325 | 0.0093 |

Key findings:

* •

  RA-CASP achieves 32.0% higher best Sharpe ratio than Euclidean (1.137 vs 0.861, p=0.0001p=0.0001, Wilcoxon), demonstrating substantial improvement in optimization outcomes.
* •

  Hypervolume improvement (0.0142 vs 0.0040) indicates broader Pareto front coverage, though this metric is sensitive to the return-aware asset selection which biases toward high-return regions.
* •

  CASP-Basic underperforms Euclidean in optimization (Sharpe 0.703 vs 0.861), suggesting that pure variance minimization without return guidance may over-emphasize defensive assets in this period. The lesson: for optimization, return-awareness is essential.
* •

  Sharpe+Euc achieves similar best Sharpe to RA-CASP (1.145 vs 1.137), but RA-CASP achieves 53% higher hypervolume, indicating better diversity across the Pareto front.

## 8  Discussion

### 8.1  Attribution of Performance Improvements

The improvements from CASP stem from two related mechanisms that can be separated empirically. First, volatility-normalized selection avoids favoring high-volatility assets purely because they produce larger raw signals. By selecting assets according to |zi|/Ωi​i|z\_{i}|/\sqrt{\Omega\_{ii}}, the method normalizes for individual asset risk. The VolNorm+Euc baseline shows that this selection step alone delivers 14.3% variance reduction versus the Euclidean baseline.

Second, covariance-aware projection geometry provides an incremental benefit beyond selection. Holding selection fixed, replacing Euclidean projection with the Ω\Omega-metric projection further penalizes shifts that increase tracking-error variance against correlated assets. Compared to VolNorm+Euc, CASP-Basic achieves an additional 1.4% incremental variance reduction (p=8.6×10−5p=8.6\times 10^{-5}), isolating the benefit of using the full covariance structure beyond diagonal scaling.

The return-aware extension (RA-CASP) introduces return terms in both selection and projection, trading some variance reduction for higher expected (and in our 2024 split, realized) Sharpe ratios.

The ablation study reveals an important insight: variance reduction and Sharpe improvement require different emphases. CASP-Basic achieves robust variance reduction (15.7%) using only covariance information, with no reliance on return estimates. This makes it suitable for settings where return forecasts are unreliable. RA-CASP incorporates return information and achieves higher Sharpe ratios, but this improvement is partially expected given the method design. Practitioners should choose CASP-Basic for risk-focused mandates where return estimates are uncertain, and RA-CASP when high-confidence return forecasts are available.

### 8.2  Out-of-Sample Robustness

The walk-forward evaluation (Table [3](https://arxiv.org/html/2512.19986v1#S7.T3 "Table 3 ‣ 7.3 Walk-forward Validation Across Market Regimes ‣ 7 Results ‣ Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization")) underscores the role of regime: return-aware methods excel in 2024 but underperform in the 2022 drawdown regime. CASP-Basic, being return-agnostic, exhibits more stable behavior in 2022. More broadly, covariance matrices tend to be estimated more reliably than expected returns [[15](https://arxiv.org/html/2512.19986v1#bib.bib15), [13](https://arxiv.org/html/2512.19986v1#bib.bib13)], so covariance-focused repair operators can be attractive when return estimates are noisy.

### 8.3  Practical implications

For risk-averse investors (or settings where return forecasts are unreliable), CASP-Basic provides a return-agnostic repair operator that reduces variance versus standard Euclidean repair, with a statistically significant incremental benefit from covariance-aware projection beyond volatility-normalized selection. For high-frequency rebalancers, CASP’s lower turnover translates directly to reduced transaction costs, improving net performance. For multi-objective optimization, CASP enables discovery of Pareto-optimal portfolios in regions inaccessible to Euclidean projection, expanding the range of available risk-return-ESG trade-offs.

### 8.4  Limitations and Future Work

Several limitations warrant consideration. Our ESG scores incorporate real governance metrics, but the environmental and social components are sector-estimated. Full validation with comprehensive ESG data from multiple providers (MSCI, Sustainalytics, Refinitiv) would strengthen the tri-objective analysis.

Performance also depends on covariance matrix quality. Integration with robust estimation methods [[14](https://arxiv.org/html/2512.19986v1#bib.bib14)] or regime-switching models is a natural extension.

The current framework is single-period; extension to multi-period optimization with transaction costs embedded in the objective is important for practical implementation. Finally, CASP adds O​(K3)O(K^{3}) overhead; therefore, extremely large cardinality constraints may benefit from approximate projection methods.

## 9  Conclusion

We introduced Covariance-Aware Simplex Projection (CASP), a repair operator for cardinality-constrained portfolio optimization that replaces Euclidean distance with a covariance-induced (tracking-error) metric. By establishing the connection between Ω\Omega-metric projection and tracking error variance minimization, we provide a portfolio-theoretic foundation for the projection geometry.

Through comprehensive ablation analysis on S&P 500 data (2020–2024), we demonstrated that:

* •

  CASP-Basic achieves 15.7% variance reduction (p<10−54p<10^{-54}) using only covariance information, with no reliance on return estimates. With the added VolNorm+Euc baseline, we find that 14.3% is explained by volatility-normalized selection and 1.4% is an incremental contribution from the Ω\Omega-metric projection geometry.
* •

  Optional return-aware extensions (RA-CASP) can further improve Sharpe ratios when reliable return forecasts are available, with out-of-sample validation confirming improvements transfer to realized performance.
* •

  The method integrates as a drop-in replacement for Euclidean projection in any metaheuristic framework.

The ablation study reveals that variance reduction and Sharpe improvement require different emphases, suggesting practitioners choose between CASP-Basic (for risk-focused mandates) and RA-CASP (for return-focused mandates). Both variants provide principled repair operators grounded in portfolio theory, immediately applicable to any metaheuristic framework for cardinality-constrained portfolio optimization.

## References

* Markowitz [1952]

  Markowitz, H. (1952).
  Portfolio selection.
  *The Journal of Finance*, 7(1):77–91.
* Zhang et al. [2018]

  Zhang, Y., Li, X., and Guo, S. (2018).
  Portfolio selection problems with Markowitz’s mean-variance framework: A review of literature.
  *Fuzzy Optimization and Decision Making*, 17(2):125–158.
* Kalayci et al. [2019]

  Kalayci, C.B., Ertenlice, O., and Akbay, M.A. (2019).
  A comprehensive review of deterministic models and applications for mean-variance portfolio optimization.
  *Expert Systems with Applications*, 125:345–368.
* Chang et al. [2000]

  Chang, T.-J., Meade, N., Beasley, J.E., and Sharaiha, Y.M. (2000).
  Heuristics for cardinality constrained portfolio optimisation.
  *Computers & Operations Research*, 27(13):1271–1302.
* Cesarone et al. [2016]

  Cesarone, F., Moretti, J., and Tardella, F. (2016).
  Optimally chosen small portfolios are better than large ones.
  *Economics Bulletin*, 36(4):1876–1891.
* Liagkouras and Metaxiotis [2018]

  Liagkouras, K. and Metaxiotis, K. (2018).
  A new efficiently encoded multiobjective algorithm for the solution of the cardinality constrained portfolio optimization problem.
  *Annals of Operations Research*, 267(1):281–319.
* Mirjalili et al. [2014]

  Mirjalili, S., Mirjalili, S.M., and Lewis, A. (2014).
  Grey Wolf Optimizer.
  *Advances in Engineering Software*, 69:46–61.
* Mirjalili et al. [2016]

  Mirjalili, S., Saremi, S., Mirjalili, S.M., and Coelho, L. (2016).
  Multi-objective grey wolf optimizer: A novel algorithm for multi-criterion optimization.
  *Expert Systems with Applications*, 47:106–119.
* Liagkouras and Metaxiotis [2018]

  Liagkouras, K. and Metaxiotis, K. (2018).
  Multi-period mean-variance fuzzy portfolio optimization model with transaction costs.
  *Engineering Applications of Artificial Intelligence*, 67:260–269.
* GSIA [2024]

  Global Sustainable Investment Alliance (2024).
  Global Sustainable Investment Review 2024.
  *GSIA Report*.
* Rutkowska-Ziarko [2013]

  Rutkowska-Ziarko, A. (2013).
  Fundamental portfolio construction based on Mahalanobis distance.
  In B. Lausen, D. Van den Poel, and A. Ultsch (eds.), *Algorithms from and for Nature and Life*. Springer, p. 11.
* Sharpe [1964]

  Sharpe, W.F. (1964).
  Capital asset prices: A theory of market equilibrium under conditions of risk.
  *The Journal of Finance*, 19(3):425–442.
* Ledoit and Wolf [2004]

  Ledoit, O. and Wolf, M. (2004).
  Honey, I shrunk the sample covariance matrix.
  *Journal of Portfolio Management*, 30(4), 110–119.
* Ledoit and Wolf [2020]

  Ledoit, O. and Wolf, M. (2020).
  Analytical nonlinear shrinkage of large-dimensional covariance matrices.
  *The Annals of Statistics*, 48(5):3043–3065.
* Taljaard and Maré [2021]

  Taljaard, B.H. and Maré, E. (2021).
  Why has the equal weight portfolio underperformed and what can we do about it?
  *Quantitative Finance*, 21(11):1855–1868.
* Kobayashi et al. [2020]

  Kobayashi, K., Takano, Y., and Nakata, K. (2020).
  Bilevel cutting-plane algorithm for solving cardinality-constrained mean-CVaR portfolio optimization problems.
  *arXiv preprint arXiv:2005.12797*.
* Pedersen et al. [2021]

  Pedersen, L.H., Fitzgibbons, S., and Pomorski, L. (2021).
  Responsible investing: The ESG-efficient frontier.
  *Journal of Financial Economics*, 142(2):572–597.
* Avramov et al. [2022]

  Avramov, D., Cheng, S., Lioui, A., and Tarelli, A. (2022).
  Sustainable investing with ESG rating uncertainty.
  *Journal of Financial Economics*, 145(2, Part B):642–664.
* Escobar-Saldívar et al. [2025]

  Escobar-Saldívar, L.J., Villarreal-Samaniego, D., and Santillán-Salgado, R.J. (2025).
  The effects of ESG scores and ESG momentum on stock returns and volatility: Evidence from U.S. markets.
  *Journal of Risk and Financial Management*, 18:367.
* Berg et al. [2022]

  Berg, F., Kölbel, J.F., and Rigobon, R. (2022).
  Aggregate confusion: The divergence of ESG ratings.
  *Review of Finance*, 26(6):1315–1344.
* Deb et al. [2002]

  Deb, K., Pratap, A., Agarwal, S., and Meyarivan, T. (2002).
  A fast and elitist multiobjective genetic algorithm: NSGA-II.
  *IEEE Transactions on Evolutionary Computation*, 6(2):182–197.
* Shao et al. [2025]

  Shao, S., Tian, Y., and Zhang, Y. (2025).
  Deep reinforcement learning assisted surrogate model management for expensive constrained multi-objective optimization.
  *Swarm and Evolutionary Computation*, 92:101817.
* Joshi and Dhodiya [2023]

  Joshi, N.K. and Dhodiya, J.M. (2023).
  Intelligent multi-objective portfolio optimization using hybrid deep learning and evolutionary algorithm approach for advanced decision-making.
  *SSRN Working Paper*.
* Doering et al. [2019]

  Doering, J., Kizys, R., Juan, A.A., Fitó, À., and Polat, O. (2019).
  Metaheuristics for rich portfolio optimisation and risk management: Current state and future trends.
  *Operations Research Perspectives*, 6:100121.
* Gambeta and Kwon [2020]

  Gambeta, V. and Kwon, R. (2020).
  Risk–return trade-off in relaxed risk parity portfolio optimization.
  *Journal of Risk and Financial Management*, 13:237.
* Condat [2016]

  Condat, L. (2016).
  Fast projection onto the simplex and the ℓ1\ell\_{1} ball.
  *Mathematical Programming*, 158(1):575–585.
* Bongiorno and Challet [2022]

  Bongiorno, C. and Challet, D. (2022).
  Non-linear shrinkage of the price return covariance matrix is far from optimal for portfolio optimisation.
  *arXiv preprint arXiv:2112.07521*.
* Mahalanobis [1936]

  Mahalanobis, P.C. (1936).
  On the generalised distance in statistics.
  *Proceedings of the National Institute of Sciences of India*, 2(1):49–55.
* Bodnar et al. [2020]

  Bodnar, T., Ivasiuk, D., Parolya, N., and Schmid, W. (2020).
  Mean–variance efficiency of optimal power and logarithmic utility portfolios.
  *Mathematics and Financial Economics*, 14(4):675–698.
* Butin [2020]

  Butin, F. (2020).
  Generalized distance to a simplex and a new geometrical method for portfolio optimization.
  *arXiv preprint arXiv:2009.08826*.

## Appendix A Implementation Details

### A.1 Simplex Projection with Box Constraints

The projection onto the constrained simplex {w:∑iwi=1,ℓ≤wi≤u}\{w:\sum\_{i}w\_{i}=1,\ell\leq w\_{i}\leq u\} is computed via bisection search for the optimal threshold τ∗\tau^{\*} such that ∑iclip​(zi−τ∗,ℓ,u)=1\sum\_{i}\text{clip}(z\_{i}-\tau^{\*},\ell,u)=1. Convergence is guaranteed within O​(log⁡(1/ϵ))O(\log(1/\epsilon)) iterations for tolerance ϵ\epsilon.

### A.2 Ω\Omega-metric Projection Implementation

For the Ω\Omega-metric projection, we solve the KK-dimensional QP using Sequential Least Squares Programming (SLSQP). To ensure numerical stability, we add a small regularization term ϵ​I\epsilon I to ΩS\Omega\_{S} if the minimum eigenvalue falls below 10−810^{-8}.