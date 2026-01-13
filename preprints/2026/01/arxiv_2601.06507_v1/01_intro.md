---
authors:
- Khizar Qureshi
- H. Oliver Gao
doc_id: arxiv:2601.06507v1
family_id: arxiv:2601.06507
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Emissions-Robust Portfolios
url_abs: http://arxiv.org/abs/2601.06507v1
url_html: https://arxiv.org/html/2601.06507v1
venue: arXiv q-fin
version: 1
year: 2026
---


Khizar Qureshi
  
Department of Mathematics
  
Massachusetts Institute of Technology
  
Cambridge, MA 02139
  
kqureshi@mit.edu
  
&H. Oliver Gao
  
School of Civil and Environmental Engineering
  
Cornell University
  
Ithaca, NY 14850
  
hg55@cornell.edu

###### Abstract

We study portfolio choice when firm-level emissions intensities are measured with error. We introduce a scope-specific penalty operator that rescales asset payoffs as a smooth function of revenue-normalized emissions intensity. Under payoff homogeneity, unit-scale invariance, mixture linearity, and a curvature semigroup axiom, the operator is unique and has the closed form Pj(m)​(r,λ)=(1−λ/λmax,j)m​rP^{(m)}\_{j}(r,\lambda)=\bigl(1-\lambda/\lambda\_{\max,j}\bigr)^{m}r. Combining this operator with norm- and moment-constrained ambiguity sets yields robust mean–variance and CVaR programs with exact linear and second-order cone reformulations and economically interpretable dual variables. In a U.S. large-cap equity universe with monthly rebalancing and uniform transaction costs, the resulting strategy reduces average Scope 1 emissions intensity by roughly 92% relative to equal weight while exhibiting no statistically detectable reduction in the Sharpe ratio under block-bootstrap inference and no statistically detectable change in average returns under HAC inference. We report the return–emissions Pareto frontier, sensitivity to robustness and turnover constraints, and uncertainty propagation from multiple imputation of emissions disclosures.

*Keywords* robust optimization, portfolio selection, sustainable finance, carbon emissions, conic optimization

## 1 Introduction

Climate change is a canonical global stock externality: the damage-relevant state variable is the atmospheric concentration of greenhouse gases, not the contemporaneous flow of emissions. Anthropogenic CO2 concentrations exceeded 420 ppm in 2023, relative to a pre-industrial baseline of roughly 280 ppm (IPCC, [2023](https://arxiv.org/html/2601.06507v1#bib.bib73 "Climate change 2023: synthesis report")). A back-of-the-envelope calculation links temperature targets to the residual global carbon budget. Let BmaxB\_{\max} denote the cumulative CO2 emissions compatible with a maximum admissible warming Δ​Tmax\Delta T\_{\max}, and let κ\kappa be the temperature response per gigaton of CO2. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bmax\displaystyle B\_{\max} | =Δ​Tmaxκ\displaystyle=\frac{\Delta T\_{\max}}{\kappa} |  | (1) |
|  |  | ≈1.5∘​C4.8×10−4​C∘/GtCO2\displaystyle\approx\frac{1.5^{\circ}\mathrm{C}}{4.8\times 10^{-4}\,{}^{\circ}\mathrm{C}/\mathrm{GtCO}\_{2}} |  |
|  |  | ≈310​GtCO2.\displaystyle\approx 10~\mathrm{GtCO}\_{2}. |  |

At current emissions rates of roughly 40​GtCO2/year40\,\mathrm{GtCO}\_{2}/\text{year}, this residual budget would be exhausted within a decade.

![Refer to caption](figures/atm_growth_with_ci_1959_2024.png)


(a) Net atmospheric addition of CO2 (GtCO2/yr), 1959–2024, with a 95% confidence band. The band propagates NOAA Mauna Loa growth-rate uncertainty (±1.96×0.11\pm 1.96\times 0.11 ppm) into mass units (1 ppm ≈\approx 7.77 GtCO2).

![Refer to caption](figures/budget_scenarios_curvature_2024_2038.png)


(b) Stylized 1.5∘C remaining budget, B0=310B\_{0}=310 GtCO2, under alternative usage paths: constant 40 GtCO2/yr, linear decline to net-zero by 2032, exponential 5%/yr reduction. And late action (flat to 2028 then 15%/yr decline). Exhaustion years are annotated where applicable.

Figure 1: From atmospheric accumulation to policy-relevant budgets.
Panel (a) translates ppm growth into GtCO2/yr and shows measurement uncertainty, panel (b) illustrates how non-linear emissions pathways induce different curvature in the remaining-budget trajectory. Values are illustrative and sensitive to methodological choices (e.g., non-CO2 forcers and probability thresholds).

These numbers underscore a simple point: anthropogenic warming is driven by the cumulative stock of CO2. The IPCC Sixth Assessment Report (AR6) formalizes the remaining carbon quotas consistent with 1.5∘​C1.5^{\circ}\mathrm{C} and 2∘​C2^{\circ}\mathrm{C} pathways and emphasizes the need for deep, near-term mitigation IPCC ([2023](https://arxiv.org/html/2601.06507v1#bib.bib73 "Climate change 2023: synthesis report")). Flow estimates from the Global Carbon Budget (Friedlingstein and others, [2025](https://arxiv.org/html/2601.06507v1#bib.bib74 "Global carbon budget 2024")) document record or near-record fossil emissions, highlighting the gap between physical constraints and realized trajectories. The Paris Agreement’s Article 2.1(c) explicitly commits signatories to “making finance flows consistent with a pathway towards low greenhouse gas emissions and climate-resilient development” (UNFCCC, [2015](https://arxiv.org/html/2601.06507v1#bib.bib76 "The paris agreement")). Complementary analyses by the UNEP Emissions Gap Report (United Nations Environment Programme, [2023](https://arxiv.org/html/2601.06507v1#bib.bib75 "Emissions gap report 2023: broken record—temperatures hit new highs, yet world fails to cut emissions (again)")) quantify the shortfall between pledged policies and emissions pathways compatible with 1.5∘​C1.5^{\circ}\mathrm{C}. Together, these developments motivate a quantitative finance response: design portfolio frameworks that deliver verifiable emissions reductions without sacrificing financial performance or risk discipline.

Institutional investors sit at the transmission channel between these climate constraints and the real economy. Global capital markets intermediate on the order of $400 trillion in financial assets (Bolton et al., [2020](https://arxiv.org/html/2601.06507v1#bib.bib45 "The green swan: central banking and financial stability in the age of climate change")). Redirecting even a modest fraction of this capital toward climate-compatible firms could generate first-order mitigation effects. Two frictions, however, impede such realignment. First, corporate greenhouse gas (GHG) disclosures are incomplete, noisy, and subject to strategic reporting and methodological disagreement across data vendors (Berg et al., [2022](https://arxiv.org/html/2601.06507v1#bib.bib70 "Aggregate confusion: the divergence of esg ratings")). Second, asset managers are still evaluated through classical lenses—risk-adjusted return, drawdown control, and turnover. Credible portfolio design must therefore integrate two classes of uncertainty on equal footing: (i) estimation risk in corporate GHG disclosures and (ii) the familiar mean–variance trade-off governing financial optimization (Markowitz, [1952](https://arxiv.org/html/2601.06507v1#bib.bib52 "Portfolio selection")).
In §[4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios") we make this comparison concrete by benchmarking EAPO against deterministic inverse-intensity tilts that treat estimated intensities as known.

![Refer to caption](figures/global_co2_by_source.png)


(a) Global fossil and land-use CO2 emissions by source, 1960–2023.

![Refer to caption](figures/co2_by_source_top_emitters_2023.png)


(b) Decomposition of 2023 CO2 emissions by source for major emitters.

Figure 2: Global and 2023 CO2 emissions by source. Source: Our World in Data, “CO2 and Greenhouse Gas Emissions” dataset.

##### Literature and conceptual foundations.

Debate on the financial performance of ESG-tilted portfolios dates back to early comparisons of socially responsible and conventional mutual funds (Renneboog et al., [2008](https://arxiv.org/html/2601.06507v1#bib.bib46 "The price of ethics and stakeholder governance: the performance of socially responsible mutual funds"); Fabozzi et al., [2008](https://arxiv.org/html/2601.06507v1#bib.bib35 "Sin stock returns")). Meta-analyses such as Friede et al. ([2015](https://arxiv.org/html/2601.06507v1#bib.bib36 "ESG and financial performance: aggregated evidence from more than 2000 empirical studies")) find on average a weakly positive relation between ESG characteristics and financial performance. Production-based asset pricing models attribute ESG premia to profitability and investment channels (Balvers, [2017](https://arxiv.org/html/2601.06507v1#bib.bib31 "Profitability, value, and stock returns in production-based asset pricing without frictions")). Building on these findings, a growing literature studies the optimal construction of ESG-integrated and low-carbon portfolios.

On the portfolio-design side, early low-carbon strategies imposed exogenous carbon-budget constraints on Markowitz frontiers or introduced decarbonization factors in index construction (Andersson et al., [2016](https://arxiv.org/html/2601.06507v1#bib.bib59 "Hedging climate risk"); Guenedal and Roncalli, [2021](https://arxiv.org/html/2601.06507v1#bib.bib47 "The market measure of carbon risk and its impact on the minimum variance portfolio")). Subsequent work incorporated climate Value-at-Risk measures (Weisang and Roncalli, [2022](https://arxiv.org/html/2601.06507v1#bib.bib48 "Portfolio construction with climate risk measures")) and climate-hedging overlays for liquid instruments (Engle et al., [2020](https://arxiv.org/html/2601.06507v1#bib.bib83 "Hedging climate change news")). Robust optimization provides the natural mathematical foundation for such extensions. Originating with the ellipsoidal uncertainty sets of Ben-Tal and Nemirovski ([2001](https://arxiv.org/html/2601.06507v1#bib.bib53 "Lectures on modern convex optimization: analysis, algorithms, and engineering applications")) and the budget-of-uncertainty model of Bertsimas and Sim ([2004](https://arxiv.org/html/2601.06507v1#bib.bib54 "The price of robustness")), robust methods have been adapted for climate stress testing and transition risk analysis (Bolton et al., [2020](https://arxiv.org/html/2601.06507v1#bib.bib45 "The green swan: central banking and financial stability in the age of climate change")). Yet, most existing approaches treat emissions exposures as known constants and either enforce hard constraints or apply ad hoc tilts, rather than modeling emissions as a noisy state variable and incorporating disclosure uncertainty within the optimization problem itself.

Parallel work in macroeconomics and asset pricing documents that climate risk is economically material. Global output follows a nonlinear, concave temperature–productivity relation with large welfare losses at high temperatures (Burke et al., [2015](https://arxiv.org/html/2601.06507v1#bib.bib77 "Global non-linear effect of temperature on economic production"); Hsiang et al., [2017](https://arxiv.org/html/2601.06507v1#bib.bib78 "Estimating economic damage from climate change in the united states")). In asset markets, long-run temperature risk carries priced premia (Bansal et al., [2016](https://arxiv.org/html/2601.06507v1#bib.bib80 "Price of long-run temperature shifts in capital markets")), and damages are heterogeneous across sectors and geographies (Carleton and Hsiang, [2016](https://arxiv.org/html/2601.06507v1#bib.bib79 "Social and economic impacts of climate")). Transition risk now appears as a priced cross-sectional factor: carbon-intensive issuers exhibit higher realized returns consistent with exposure to a transition premium (Bolton and Kacperczyk, [2021](https://arxiv.org/html/2601.06507v1#bib.bib81 "Do investors care about carbon risk?")), while option-implied volatilities reveal elevated compensation for downside climate risk (Ilhan et al., [2021](https://arxiv.org/html/2601.06507v1#bib.bib82 "Carbon tail risk")). Dynamic climate-hedging strategies reduce exposure to climate news using liquid equity instruments (Engle et al., [2020](https://arxiv.org/html/2601.06507v1#bib.bib83 "Hedging climate change news")). The ESG-efficient frontier formalizes the trade-off between risk-adjusted return and sustainability exposure (Pedersen et al., [2021](https://arxiv.org/html/2601.06507v1#bib.bib60 "Responsible investing: the esg-efficient frontier")), and equilibrium analyses show that heterogeneous investor preferences can generate structural return differentials between “green” and “brown” assets (Pastor et al., [2021](https://arxiv.org/html/2601.06507v1#bib.bib61 "Sustainable investing in equilibrium")). Finally, Giglio et al. ([2021](https://arxiv.org/html/2601.06507v1#bib.bib87 "Climate finance")) provide a comprehensive review and emphasize that climate-related risks are economically material while identification and measurement remain central challenges for empirical asset pricing.

Regulatory and disclosure frameworks have begun to codify these practices. The EU’s Paris-Aligned Benchmark (PAB) and Climate Transition Benchmark (CTB) frameworks impose minimum decarbonization rates and transparency requirements (EU Technical Expert Group on Sustainable Finance, [2019](https://arxiv.org/html/2601.06507v1#bib.bib88 "Final report on climate benchmarks and benchmarks’ esg disclosures")). Disclosure has shifted from largely voluntary to increasingly mandatory, anchored by the TCFD (Task Force on Climate-related Financial Disclosures, [2017](https://arxiv.org/html/2601.06507v1#bib.bib89 "Recommendations of the tcfd")) and the IFRS S2 climate reporting standard (International Sustainability Standards Board, [2023](https://arxiv.org/html/2601.06507v1#bib.bib90 "IFRS s2: climate-related disclosures")). The PCAF methodology provides standardized attribution rules for financed emissions (Partnership for Carbon Accounting Financials, [2020](https://arxiv.org/html/2601.06507v1#bib.bib91 "Global ghg accounting and reporting standard for the financial industry")), while the Network for Greening the Financial System (NGFS) scenarios underpin climate stress testing by supervisors (Network for Greening the Financial System (NGFS), [2025](https://arxiv.org/html/2601.06507v1#bib.bib95 "NGFS climate scenarios: technical documentation (phase iv)")). At the measurement level, the GHG Protocol defines Scope 1–3 boundaries and revenue-normalization conventions (WRI and WBCSD, [2004](https://arxiv.org/html/2601.06507v1#bib.bib92 "The greenhouse gas protocol: a corporate accounting and reporting standard (revised edition)")). Despite this progress, substantial rating divergence and measurement error persist (Berg et al., [2022](https://arxiv.org/html/2601.06507v1#bib.bib70 "Aggregate confusion: the divergence of esg ratings")), reflecting genuine differences in coverage and methodology rather than minor weighting choices. These observations motivate a formal treatment of emissions uncertainty via multiple imputation and distributionally robust modeling, replacing brittle point estimates with statistically grounded ambiguity sets.

This paper contributes to the intersection of robust optimization and sustainable investing by taking emissions uncertainty seriously. Rather than superimposing hard carbon budgets on point estimates of corporate emissions, we introduce an emissions-penalty operator that acts directly on expected returns and is robustified over scope-specific ambiguity sets. The operator admits an exact linear or second-order cone representation and yields an economically interpretable dual: Lagrange multipliers on the ambiguity sets can be read as “shadow carbon prices” that mediate the trade-off between return and robustness. The central empirical question we study is whether such an emissions-aware robust formulation can deliver material reductions in financed emissions—at institutional scale and under realistic transaction costs—without deteriorating classical risk-adjusted performance.

### 1.1 Positioning and Contributions

Let Zj​(Γ)Z\_{j}(\Gamma) denote an ambiguity set for firm-level scope-jj emissions intensities, indexed by a robustness budget Γ≥0\Gamma\geq 0. Section [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") shows that our basic emissions-aware robust portfolio optimization (EAPO) problem can be written in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈Δn⁡minzj∈Zj​(Γ)⁡x⊤​(R−α​zj),\max\_{x\in\Delta\_{n}}\,\min\_{z\_{j}\in Z\_{j}(\Gamma)}x^{\top}\bigl(R-\alpha z\_{j}\bigr), |  | (2) |

where R∈ℝnR\in\mathbb{R}^{n} collects nominal expected returns, zj∈ℝ+nz\_{j}\in\mathbb{R}^{n}\_{+} is the vector of scope-jj emissions intensities, α≥0\alpha\geq 0 is a policy penalty parameter, and Δn:={x∈ℝ≥0n:𝟏⊤​x=1}\Delta\_{n}:=\{x\in\mathbb{R}^{n}\_{\geq 0}:\mathbf{1}^{\top}x=1\} is the simplex of long-only portfolio weights. We show that, for a broad class of ambiguity sets motivated by disclosure uncertainty, problem ([2](https://arxiv.org/html/2601.06507v1#S1.E2 "In 1.1 Positioning and Contributions ‣ 1 Introduction ‣ Emissions-Robust Portfolios")) admits an exact linear or second-order cone representation with O​(n)O(n) conic constraints, ensuring polynomial-time solvability for institutional-scale universes with thousands of securities. Our contributions are both methodological and empirical:

1. C1.

   Axiomatic modeling of emissions penalties. We introduce a scope-specific emissions-penalty operator Pj(m)P^{(m)}\_{j} that maps raw returns into emissions-adjusted payoffs by scaling each asset’s return according to its revenue-normalized emissions intensity. The operator is characterized by natural axioms—payoff homogeneity, normalization at zero and maximum intensity, monotonicity in emissions, unit-scale invariance, mixture linearity, and a curvature semigroup property. We prove an axiomatic uniqueness result: within this class, the only admissible family is Pj(m)​(r,λ)=(1−λ/λmax,j)m​rP^{(m)}\_{j}(r,\lambda)=(1-\lambda/\lambda\_{\max,j})^{m}r. The curvature parameter m∈ℕ+m\in\mathbb{N}\_{+} controls the strength of penalization and yields a Schur-convex dependence on intensities, so reallocating weight from high- to low-intensity firms weakly increases every component of the emissions-adjusted return vector.
2. C2.

   Robust optimization under disclosure uncertainty. We model emissions disclosure risk through scope-specific ambiguity sets that combine moment constraints and ℓp\ell\_{p}-norm bounds on intensities. Using a Lipschitz envelope for the penalty operator, we show that robust mean–variance and tail-risk (CVaR) formulations reduce to convex programs of the form

   |  |  |  |
   | --- | --- | --- |
   |  | maxx∈Δn⁡x⊤​μje−Γ​‖diag​(L)​x‖p⋆−θ​x⊤​Σ​x,\max\_{x\in\Delta\_{n}}x^{\top}\mu^{e}\_{j}-\Gamma\|\mathrm{diag}(L)\,x\|\_{p^{\star}}-\theta x^{\top}\Sigma x, |  |

   where μje\mu^{e}\_{j} are emissions-adjusted expected returns, Σ\Sigma is the covariance matrix, LL collects asset-wise Lipschitz constants, and p⋆p^{\star} is the dual norm. For p∈{1,∞}p\in\{1,\infty\} the resulting program is a linear program (LP). For p=2p=2 it is a second-order cone program (SOCP) with O​(n)O(n) cones. We further extend the framework to dynamic and distributionally robust settings via φ\varphi-divergence balls. In all cases, Lagrange multipliers on the ambiguity constraints admit a natural economic interpretation as shadow carbon prices: the marginal Sharpe loss an investor is willing to accept per unit of additional robustness.
3. C3.

   Large-scale empirical evaluation. We implement EAPO on a U.S. large-cap equity universe using daily returns, annual scope-specific emissions from CDP, and quarterly revenues combined into revenue-normalized intensities. The empirical pipeline—detailed in Section [3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios")—uses sector-aware hierarchical Bayesian imputation for missing emissions, multiple imputation to propagate disclosure uncertainty, and Ledoit–Wolf shrinkage for covariance estimation. Under monthly rebalancing and uniform transaction costs, EAPO delivers order-of-magnitude reductions in portfolio Scope-1 emissions intensity—up to roughly 8080–90%90\% relative to equal-weight, global minimum-variance, and naive emissions-weighted benchmarks—without statistically significant deterioration in Sharpe ratio, volatility, drawdowns, or turnover. We quantify uncertainty via HAC-robust (Newey–West) inference and show that these performance comparisons are statistically stable across regimes.
4. C4.

   Managerial interpretation and policy relevance. By embedding emissions penalties directly in the return kernel rather than as external hard constraints, EAPO integrates cleanly with existing mean–variance and risk-budgeting infrastructures used by asset managers. The return–emissions Pareto frontier generated by our framework provides an explicit menu of decarbonization targets and associated performance impacts, which can be used to negotiate mandates and monitor compliance. The shadow carbon prices arising from the dual variables supply an internal carbon valuation consistent with regulatory frameworks such as PAB/CTB, TCFD, IFRS S2, and PCAF, and offer a transparent metric for calibrating robustness budgets Γ\Gamma to investor-specific climate preferences.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") formalizes the stochastic environment, introduces the emissions-penalty operator, and develops robust mean–variance, CVaR, dynamic, and distributionally robust formulations together with their conic reformulations. Section [3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios") describes the data architecture, statistical pre-processing (including multiple imputation and covariance shrinkage), benchmark portfolio constructions, and the optimization workflow. Section [4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios") presents empirical results on financial performance, emissions intensity, and sensitivity analysis, including HAC-robust inference and the estimated return–emissions Pareto frontier. Section [4.4](https://arxiv.org/html/2601.06507v1#S4.SS4 "4.4 Discussion ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") discusses strategic implications and policy relevance, and Section [5](https://arxiv.org/html/2601.06507v1#S5 "5 Conclusion and Future Research ‣ Emissions-Robust Portfolios") concludes.

## 2 Mathematical Model and Data

This section presents the emissions-aware portfolio optimization (EAPO) framework that underlies the empirical analysis. The model incorporates climate considerations directly into expected returns through a scope-specific emissions penalty and then accounts for disclosure uncertainty using norm-based ambiguity sets. Embedding these components within standard mean–risk objectives yields optimization problems that admit exact linear programming (LP) or second-order cone programming (SOCP) reformulations, ensuring tractability for large institutional universes with n>103n>10^{3}. Throughout the section, attention is restricted to a fixed emissions scope j∈{1,2,3}j\in\{1,2,3\}. The empirical analysis later focuses on direct Scope 1 emissions, and extending the formulation to multiple scopes is notational rather than conceptual.

### 2.1 Stochastic Environment and Financial Primitives

All random variables are defined on a complete probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). Let n∈ℕn\in\mathbb{N} denote the number of tradable assets, and define the one-period gross return vector

|  |  |  |
| --- | --- | --- |
|  | R:=(R1,…,Rn)⊤:Ω→ℝn.R:=(R\_{1},\dots,R\_{n})^{\top}:\Omega\to\mathbb{R}^{n}. |  |

###### Assumption 2.1 (Finite second moment).

The return vector satisfies 𝔼​[‖R‖22]<∞\mathbb{E}[\|R\|\_{2}^{2}]<\infty.

Assumption [2.1](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem1 "Assumption 2.1 (Finite second moment). ‣ 2.1 Stochastic Environment and Financial Primitives ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") ensures feasibility of the mean–variance and CVaR formulations introduced below. Define the expected return vector and covariance matrix as

|  |  |  |
| --- | --- | --- |
|  | μ:=𝔼​[R]∈ℝn,Σ:=Cov​(R)∈ℝn×n.\mu:=\mathbb{E}[R]\in\mathbb{R}^{n},\qquad\Sigma:=\mathrm{Cov}(R)\in\mathbb{R}^{n\times n}. |  |

Returns are expressed in excess of the funding rate, so the risk-free asset can be omitted without loss of generality.

A portfolio is represented by a weight vector x∈Δnx\in\Delta\_{n}, where

|  |  |  |
| --- | --- | --- |
|  | Δn:={x∈ℝ≥0n:𝟏⊤​x=1}\Delta\_{n}:=\{x\in\mathbb{R}^{n}\_{\geq 0}:\mathbf{1}^{\top}x=1\} |  |

is the unit simplex. The one-period portfolio gross return is Rp:=x⊤​RR^{p}:=x^{\top}R. The analysis focuses on long-only portfolios, leverage or short positions can be incorporated by replacing the simplex with an appropriate convex polytope.

### 2.2 Emissions Accounting and Intensities

For each firm i∈{1,…,n}i\in\{1,\dots,n\} and scope j∈{1,2,3}j\in\{1,2,3\}, let

* •

  Ci,j>0C\_{i,j}>0 denote annual greenhouse gas emissions of scope jj, measured in tCO2e,
* •

  Si>0S\_{i}>0 denote trailing-twelve-month revenue (USD).

Following standard GHG Protocol and CDP conventions, emissions are expressed using revenue-normalized intensities,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λi,j\displaystyle\lambda\_{i,j} | =Ci,jSi,i=1,…,n,\displaystyle=\frac{C\_{i,j}}{S\_{i}},\qquad i=1,\ldots,n, |  | (3) |
|  | λj\displaystyle\lambda\_{j} | =(λ1,j,…,λn,j)⊤∈ℝ≥0n.\displaystyle=(\lambda\_{1,j},\ldots,\lambda\_{n,j})^{\top}\in\mathbb{R}^{n}\_{\geq 0}. |  |

Normalization removes scale-driven differences attributable solely to firm size and aligns the portfolio measure with scope-consistent financed-emissions metrics.

In empirical implementation (§[3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios")), the components Ci,jC\_{i,j} and SiS\_{i} are updated at lower frequency (annual and quarterly, respectively) than financial returns. Accordingly, the intensities λi,j\lambda\_{i,j} are treated as slowly evolving state variables: they are updated when new disclosures become available and held fixed between disclosure dates. Section [3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios") documents the associated timing conventions and the multiple-imputation procedure used to address missing or noisy emissions data.

### 2.3 Emissions–Penalty Operator

We now formalize the mechanism that maps firm-level emissions intensities into return adjustments.
The construction is guided by four principles:
(i) linearity in payoffs to preserve convexity and enable conic reformulations,
(ii) monotonicity with respect to emissions intensity,
(iii) invariance to unit scaling, and
(iv) a one-parameter curvature family that controls the strength of penalization.
Appendix [6.1](https://arxiv.org/html/2601.06507v1#S6.SS1 "6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios") states these axioms formally and shows that they identify the operator uniquely.

Fix scope jj and define the cross-sectional maximum intensity

|  |  |  |
| --- | --- | --- |
|  | λmax,j:=maxi≤n⁡λi,j∈(0,∞).\lambda\_{\max,j}:=\max\_{i\leq n}\lambda\_{i,j}\in(0,\infty). |  |

Let λ~i,j:=λi,j/λmax,j∈[0,1]\tilde{\lambda}\_{i,j}:=\lambda\_{i,j}/\lambda\_{\max,j}\in[0,1] denote the normalized intensity.

###### Definition 2.2 (Emissions–penalty operator).

For scope jj and curvature parameter m∈ℕ+m\in\mathbb{N}\_{+}, the emissions–penalty operator
Pj(m):ℝ×[0,λmax,j]→ℝP^{(m)}\_{j}:\mathbb{R}\times[0,\lambda\_{\max,j}]\to\mathbb{R} for some return rr is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj(m)​(r,λ):=(1−λλmax,j)m​r.P^{(m)}\_{j}(r,\lambda):=\Big(1-\frac{\lambda}{\lambda\_{\max,j}}\Big)^{m}r. |  | (4) |

For firm ii, the emissions-adjusted gross return is

|  |  |  |
| --- | --- | --- |
|  | Ri,je:=Pj(m)​(Ri,λi,j),Rje:=(R1,je,…,Rn,je)⊤.R^{e}\_{i,j}:=P^{(m)}\_{j}(R\_{i},\lambda\_{i,j}),\qquad R^{e}\_{j}:=(R^{e}\_{1,j},\dots,R^{e}\_{n,j})^{\top}. |  |

The factor (1−λ/λmax,j)m∈[0,1](1-\lambda/\lambda\_{\max,j})^{m}\in[0,1] applies a smooth return haircut that increases with emissions intensity.
The curvature parameter mm governs the steepness of this penalty:
m=1m=1 yields a linear schedule, while larger mm place disproportionately greater weight on high-intensity firms—approximating hard exclusions in the upper tail of the intensity distribution.

Definition [2.2](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem2 "Definition 2.2 (Emissions–penalty operator). ‣ 2.3 Emissions–Penalty Operator ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") arises directly from the axioms in Appendix [6.1](https://arxiv.org/html/2601.06507v1#S6.SS1 "6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios").
Under payoff homogeneity, normalization at λ=0\lambda=0 and λ=λmax,j\lambda=\lambda\_{\max,j}, monotonicity in λ\lambda, unit-scale invariance, mixture linearity, and the curvature semigroup condition Pj(m1+m2)=Pj(m1)∘Pj(m2)P^{(m\_{1}+m\_{2})}\_{j}=P^{(m\_{1})}\_{j}\circ P^{(m\_{2})}\_{j} for all m1,m2∈ℕ+m\_{1},m\_{2}\in\mathbb{N}\_{+}, the form in ([4](https://arxiv.org/html/2601.06507v1#S2.E4 "In Definition 2.2 (Emissions–penalty operator). ‣ 2.3 Emissions–Penalty Operator ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) is the unique admissible family.

The operator maintains desirable analytical structure:

###### Lemma 2.3 (Analytic properties).

For fixed scope jj and m∈ℕ+m\in\mathbb{N}\_{+}:

1. 1.

   For fixed λ\lambda, the map r↦Pj(m)​(r,λ)r\mapsto P^{(m)}\_{j}(r,\lambda) is linear with Lipschitz constant
   |1−λ/λmax,j|m≤1|1-\lambda/\lambda\_{\max,j}|^{m}\leq 1.
2. 2.

   For fixed rr, the map λ↦Pj(m)​(r,λ)\lambda\mapsto P^{(m)}\_{j}(r,\lambda) is strictly decreasing, C∞C^{\infty} on (0,λmax,j)(0,\lambda\_{\max,j}), and convex on [0,λmax,j][0,\lambda\_{\max,j}].
3. 3.

   Let Rje=(Pj(m)​(Ri,λi,j))i≤nR^{e}\_{j}=(P^{(m)}\_{j}(R\_{i},\lambda\_{i,j}))\_{i\leq n}.
   For any portfolio x∈Δnx\in\Delta\_{n} with xi≥0x\_{i}\geq 0, the mapping λj↦x⊤​𝔼​[Rje]\lambda\_{j}\mapsto x^{\top}\mathbb{E}[R^{e}\_{j}] is Schur–convex in λj\lambda\_{j}.

###### Proof.

(i) follows directly from ([4](https://arxiv.org/html/2601.06507v1#S2.E4 "In Definition 2.2 (Emissions–penalty operator). ‣ 2.3 Emissions–Penalty Operator ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")).
(ii) follows from

|  |  |  |
| --- | --- | --- |
|  | ∂∂λ​Pj(m)​(r,λ)=−mλmax,j​(1−λλmax,j)m−1​r\frac{\partial}{\partial\lambda}P^{(m)}\_{j}(r,\lambda)=-\frac{m}{\lambda\_{\max,j}}\Big(1-\frac{\lambda}{\lambda\_{\max,j}}\Big)^{m-1}r |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∂2∂λ2​Pj(m)​(r,λ)=m​(m−1)λmax,j2​(1−λλmax,j)m−2​r.\frac{\partial^{2}}{\partial\lambda^{2}}P^{(m)}\_{j}(r,\lambda)=\frac{m(m-1)}{\lambda\_{\max,j}^{2}}\Big(1-\frac{\lambda}{\lambda\_{\max,j}}\Big)^{m-2}r. |  |

(iii) uses symmetry and convexity of
λ↦(1−λ/λmax,j)m\lambda\mapsto(1-\lambda/\lambda\_{\max,j})^{m}
together with the standard characterization of Schur–convex functions.
∎

These properties ensure that inserting the operator into classical mean–risk objectives preserves convexity.
In particular, Schur–convexity captures the intuitive idea that reallocating weight from high- to low-intensity firms weakly increases emissions-adjusted expected returns.

Define the scope-jj emissions-adjusted mean vector:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μje\displaystyle\mu^{e}\_{j} | :=𝔼​[Rje]\displaystyle=\mathbb{E}[R^{e}\_{j}] |  | (5) |
|  |  | =𝔼​[diag​((1−λ1,jλmax,j)m,…,(1−λn,jλmax,j)m)​R].\displaystyle=\mathbb{E}\!\Big[\mathrm{diag}\big((1-\tfrac{\lambda\_{1,j}}{\lambda\_{\max,j}})^{m},\ldots,(1-\tfrac{\lambda\_{n,j}}{\lambda\_{\max,j}})^{m}\big)R\Big]. |  |

Empirically, μje\mu^{e}\_{j} is estimated using rolling windows. See §[3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios").

### 2.4 Ambiguity Sets for Emissions Uncertainty

Corporate emissions disclosures are noisy, incomplete, and in part judgmental.
Rather than treat λj\lambda\_{j} as known, we allow it to vary within a statistically
motivated uncertainty set. Let λ^j\widehat{\lambda}\_{j} be the point estimate
constructed from CDP and financial-statement data, and let Σλ,j\Sigma\_{\lambda,j}
be a positive semidefinite dispersion proxy obtained from multiple imputation
(see Section [3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios")).

We model deviations through εj:=λj−λ^j\varepsilon\_{j}:=\lambda\_{j}-\widehat{\lambda}\_{j},
restricted to the norm ball

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒰j​(Γ):=\displaystyle\mathcal{U}\_{j}(\Gamma)= | {ε∈ℝn:‖Σλ,j−1/2​ε‖p≤Γ},\displaystyle\ \Bigl\{\varepsilon\in\mathbb{R}^{n}:\bigl\|\Sigma\_{\lambda,j}^{-1/2}\varepsilon\bigr\|\_{p}\leq\Gamma\Bigr\}, |  | (6) |
|  |  | p∈{1,2,∞},Γ>0.\displaystyle p\in\{1,2,\infty\},\qquad\Gamma>0. |  |

The scalar Γ\Gamma is the robustness budget: larger values admit more
severe misspecification in firm-level intensities.
The choices p=1p=1 and p=∞p=\infty yield polyhedral (Bertsimas–Sim–type)
uncertainty sets, whereas p=2p=2 yields an ellipsoid. In all cases,
([26](https://arxiv.org/html/2601.06507v1#S6.E26 "In Proposition 6.1 (Uniqueness and closed form). ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios")) admits an exact LP/SOCP representation.

Because RjeR^{e}\_{j} depends on λj\lambda\_{j} only through the scalar weights
(1−λi,j/λmax,j)m\bigl(1-\lambda\_{i,j}/\lambda\_{\max,j}\bigr)^{m}, Lemma [2.3](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem3 "Lemma 2.3 (Analytic properties). ‣ 2.3 Emissions–Penalty Operator ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")
implies that each component of μje​(λj)\mu^{e}\_{j}(\lambda\_{j}) is Lipschitz in λj\lambda\_{j}.
Writing

|  |  |  |
| --- | --- | --- |
|  | μje​(λj)=μje​(λ^j)+δj​(εj),εj∈𝒰j​(Γ),\mu^{e}\_{j}(\lambda\_{j})=\mu^{e}\_{j}(\widehat{\lambda}\_{j})+\delta\_{j}(\varepsilon\_{j}),\qquad\varepsilon\_{j}\in\mathcal{U}\_{j}(\Gamma), |  |

the perturbation δj​(εj)\delta\_{j}(\varepsilon\_{j}) can be norm-bounded.
A compact envelope inequality (proved in Appendix [6.6](https://arxiv.org/html/2601.06507v1#S6.SS6 "6.6 Lipschitz sensitivity in the robustness budget (Theorem 2.3) ‣ 6 Appendix ‣ Emissions-Robust Portfolios")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | supεj∈𝒰j​(Γ)x⊤​(μje​(λ^j)−μje​(λ^j+εj))\displaystyle\sup\_{\varepsilon\_{j}\in\mathcal{U}\_{j}(\Gamma)}x^{\top}\!\big(\mu\_{j}^{e}(\widehat{\lambda}\_{j})-\mu\_{j}^{e}(\widehat{\lambda}\_{j}+\varepsilon\_{j})\big) |  | (7) |
|  |  | ≤Γ​‖diag​(L)​x‖p⋆.\displaystyle\qquad\leq\,\Gamma\,\|\mathrm{diag}(L)\,x\|\_{p^{\star}}. |  |

where L=(L1,…,Ln)⊤L=(L\_{1},\dots,L\_{n})^{\top} is a vector of asset-wise Lipschitz constants
and p⋆p^{\star} is the dual exponent (1/p+1/p⋆=11/p+1/p^{\star}=1).
Expression ([7](https://arxiv.org/html/2601.06507v1#S2.E7 "In 2.4 Ambiguity Sets for Emissions Uncertainty ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) is the key ingredient enabling the tractable
robust counterparts in subsequent sections.

### 2.5 Robust Mean–Variance with Emissions Penalties

We embed the emissions–penalty operator and ambiguity set into a mean–variance program.
For parameters θ>0\theta>0 (risk aversion) and Γ>0\Gamma>0 (robustness budget), consider the
robust mean–variance problem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxx∈Δn{\displaystyle\max\_{x\in\Delta\_{n}}\ \Bigl\{ | x⊤​μje​(λ^j)\displaystyle x^{\top}\mu^{e}\_{j}(\widehat{\lambda}\_{j}) |  | (8) |
|  |  | −supεj∈𝒰j​(Γ)x⊤​(μje​(λ^j)−μje​(λ^j+εj))\displaystyle{}-\sup\_{\varepsilon\_{j}\in\mathcal{U}\_{j}(\Gamma)}x^{\top}\Bigl(\mu^{e}\_{j}(\widehat{\lambda}\_{j})-\mu^{e}\_{j}(\widehat{\lambda}\_{j}+\varepsilon\_{j})\Bigr) |  |
|  |  | −θx⊤Σx}.\displaystyle{}-\theta\,x^{\top}\Sigma x\Bigr\}. |  |

Because only the drift is uncertain, the covariance matrix Σ\Sigma is unaffected.
By Lemma [2.3](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem3 "Lemma 2.3 (Analytic properties). ‣ 2.3 Emissions–Penalty Operator ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios"), each component of μje​(λj)\mu^{e}\_{j}(\lambda\_{j}) is Lipschitz in
λj\lambda\_{j}. Let LiL\_{i} denote the Lipschitz constant of asset ii, and define
L=(L1,…,Ln)⊤L=(L\_{1},\dots,L\_{n})^{\top}. A standard envelope bound
(Appendix [6.6](https://arxiv.org/html/2601.06507v1#S6.SS6 "6.6 Lipschitz sensitivity in the robustness budget (Theorem 2.3) ‣ 6 Appendix ‣ Emissions-Robust Portfolios")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | supεj∈𝒰j​(Γ)x⊤​(μje​(λ^j)−μje​(λ^j+εj))≤Γ​‖diag​(L)​x‖q,\displaystyle\sup\_{\varepsilon\_{j}\in\mathcal{U}\_{j}(\Gamma)}x^{\top}\Bigl(\mu^{e}\_{j}(\widehat{\lambda}\_{j})-\mu^{e}\_{j}(\widehat{\lambda}\_{j}+\varepsilon\_{j})\Bigr)\;\leq\;\Gamma\,\|\mathrm{diag}(L)\,x\|\_{q}, |  | (9) |

where qq is the Hölder–conjugate exponent of pp, satisfying 1/p+1/q=11/p+1/q=1
(with the conventions p=1⇒q=∞p=1\Rightarrow q=\infty and p=∞⇒q=1p=\infty\Rightarrow q=1).
Equivalently, ∥⋅∥q\|\cdot\|\_{q} is the dual norm of ∥⋅∥p\|\cdot\|\_{p}.

Substituting this bound into ([8](https://arxiv.org/html/2601.06507v1#S2.E8 "In 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) yields the reduced robust mean–variance problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈Δn⁡{x⊤​μje​(λ^j)−Γ​‖diag​(L)​x‖q−θ​x⊤​Σ​x}.\displaystyle\max\_{x\in\Delta\_{n}}\Bigl\{x^{\top}\mu^{e}\_{j}(\widehat{\lambda}\_{j})-\Gamma\,\|\mathrm{diag}(L)\,x\|\_{q}-\theta\,x^{\top}\Sigma x\Bigr\}. |  | (10) |

###### Theorem 2.4 (Exact conic reformulation).

For p∈{1,2,∞}p\in\{1,2,\infty\}, problem ([10](https://arxiv.org/html/2601.06507v1#S2.E10 "In 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) admits an exact conic formulation:

* •

  if p∈{1,∞}p\in\{1,\infty\} (equivalently q∈{∞,1}q\in\{\infty,1\}), it is equivalent to a linear
  program of size O​(n)O(n);
* •

  if p=2p=2 (so q=2q=2), it is equivalent to a second–order cone program with O​(n)O(n) cones,
  solvable in O​(n3.5​log⁡(1/ϵ))O(n^{3.5}\log(1/\epsilon)) time via standard interior–point methods.

###### Proof.

Introduce an epigraph variable uu and rewrite ([10](https://arxiv.org/html/2601.06507v1#S2.E10 "In 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) as

|  |  |  |
| --- | --- | --- |
|  | maxx∈Δn,u⁡{x⊤​μje​(λ^j)−Γ​u−θ​x⊤​Σ​x}s.t.u≥‖diag​(L)​x‖q.\max\_{x\in\Delta\_{n},\,u}\ \Bigl\{x^{\top}\mu^{e}\_{j}(\widehat{\lambda}\_{j})-\Gamma u-\theta\,x^{\top}\Sigma x\Bigr\}\quad\text{s.t.}\quad u\geq\|\mathrm{diag}(L)\,x\|\_{q}. |  |

If q∈{1,∞}q\in\{1,\infty\}, the epigraph constraint is polyhedral and admits an LP representation
of size O​(n)O(n). If q=2q=2, it is a second–order cone constraint. The remaining objective terms
are linear or convex quadratic in xx, with Σ⪰0\Sigma\succeq 0, yielding the stated LP/SOCP
reformulations.
∎

The multiplier associated with the epigraph constraint
u≥‖diag​(L)​x‖qu\geq\|\mathrm{diag}(L)\,x\|\_{q} admits an economic interpretation.
Denote this dual variable by π⋆\pi^{\star}. It represents a shadow carbon price, interpreted as
the marginal reduction in risk–adjusted performance the investor is willing to accept per
unit increase in the emissions ambiguity budget Γ\Gamma.

### 2.6 Tail–Risk Extension (CVaR)

Variance is symmetric by construction and does not distinguish between upside and downside moves. To
capture asymmetric transition or litigation risk, we replace the variance penalty in ([10](https://arxiv.org/html/2601.06507v1#S2.E10 "In 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios"))
by a CVaR term. For a fixed portfolio xx and scope jj, define the loss
L:=−x⊤​RjeL:=-x^{\top}R^{e}\_{j}. For confidence level α∈(0,1)\alpha\in(0,1) the CVaR of LL is

|  |  |  |
| --- | --- | --- |
|  | CVaRα​(L)=minν∈ℝ⁡{ν+11−α​𝔼​[(L−ν)+]},\mathrm{CVaR}\_{\alpha}(L)=\min\_{\nu\in\mathbb{R}}\left\{\nu+\frac{1}{1-\alpha}\,\mathbb{E}\bigl[(L-\nu)\_{+}\bigr]\right\}, |  |

following Rockafellar and Uryasev ([2000](https://arxiv.org/html/2601.06507v1#bib.bib55 "Optimization of conditional value-at-risk")). Discretizing ℙ\mathbb{P} into MM scenarios
{R(s)}s=1M\{R^{(s)}\}\_{s=1}^{M} with equal mass yields the convex surrogate

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CVaRα​(L)\displaystyle\mathrm{CVaR}\_{\alpha}(L) | =minν∈ℝ,ξ∈ℝ≥0M{ν+1(1−α)​M∑s=1Mξs\displaystyle=\min\_{\nu\in\mathbb{R},\,\xi\in\mathbb{R}^{M}\_{\geq 0}}\Biggl\{\nu+\frac{1}{(1-\alpha)M}\sum\_{s=1}^{M}\xi\_{s} |  | (11) |
|  |  | :ξs≥−x⊤Rje,(s)−ν,s≤M}.\displaystyle\qquad:\,\xi\_{s}\geq-x^{\top}R^{e,(s)}\_{j}-\nu,\quad s\leq M\Biggr\}. |  |

This formulation is linear in (x,ν,ξ)(x,\nu,\xi) conditional on the scenario returns Rje,(s)R^{e,(s)}\_{j}. The robust CVaR program becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈Δn⁡minεj∈𝒰j​(Γ)⁡{x⊤​μje​(λ^j+εj)−β​CVaRα​(L)},\max\_{x\in\Delta\_{n}}\min\_{\varepsilon\_{j}\in\mathcal{U}\_{j}(\Gamma)}\left\{x^{\top}\mu^{e}\_{j}(\widehat{\lambda}\_{j}+\varepsilon\_{j})-\beta\,\mathrm{CVaR}\_{\alpha}(L)\right\}, |  | (12) |

with tail–risk aversion β>0\beta>0. Exactly the same Lipschitz argument as in
§[2.5](https://arxiv.org/html/2601.06507v1#S2.SS5 "2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") implies that the inner minimum over εj\varepsilon\_{j} again collapses to a norm
penalty of the form Γ​‖diag​(L)​x‖p⋆\Gamma\|\mathrm{diag}(L)\,x\|\_{p^{\star}}. After scenario discretization,
([12](https://arxiv.org/html/2601.06507v1#S2.E12 "In 2.6 Tail–Risk Extension (CVaR) ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) is therefore an LP (for p∈{1,∞}p\in\{1,\infty\}) or an SOCP (for p=2p=2), albeit in a
higher–dimensional space of size O​(M​n)O(Mn).

### 2.7 Comparative Statics in Curvature, Robustness, and Risk Aversion

Let V⋆​(m,Γ,θ)V^{\star}(m,\Gamma,\theta) denote the optimal value of the reduced robust
mean–variance program ([10](https://arxiv.org/html/2601.06507v1#S2.E10 "In 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) with curvature parameter mm,
robustness budget Γ\Gamma, and risk aversion θ\theta. Let (x⋆,π⋆)(x^{\star},\pi^{\star})
denote a primal–dual optimal pair, where π⋆\pi^{\star} is the Lagrange multiplier
associated with the epigraph constraint
u≥‖diag​(L)​x‖qu\geq\|\mathrm{diag}(L)x\|\_{q} in the conic reformulation of
Section [2.5](https://arxiv.org/html/2601.06507v1#S2.SS5 "2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios").

###### Proposition 2.5 (Sensitivity).

Under mild regularity conditions (e.g., uniqueness of the optimal solution),
the following comparative statics hold:

|  |  |  |
| --- | --- | --- |
|  | ∂V⋆∂Γ=−π⋆≤ 0,∂V⋆∂m=(x⋆)⊤​∂μje∂m≤ 0.\frac{\partial V^{\star}}{\partial\Gamma}=-\,\pi^{\star}\,\leq\,0,\qquad\frac{\partial V^{\star}}{\partial m}=(x^{\star})^{\top}\frac{\partial\mu^{e}\_{j}}{\partial m}\,\leq\,0. |  |

Moreover, the mapping θ↦V⋆​(m,Γ,θ)\theta\mapsto V^{\star}(m,\Gamma,\theta) is concave and
1/λmax,j1/\lambda\_{\max,j}–Lipschitz.

###### Proof.

Apply the envelope theorem to the Lagrangian associated with the epigraph
formulation of ([10](https://arxiv.org/html/2601.06507v1#S2.E10 "In 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")). Differentiation with respect to the
robustness budget Γ\Gamma yields
∂ΓV⋆=−π⋆\partial\_{\Gamma}V^{\star}=-\pi^{\star}, where π⋆≥0\pi^{\star}\geq 0 by dual feasibility,
implying monotonicity in Γ\Gamma.

Monotonicity in the curvature parameter mm follows from the fact that
∂mμje≤0\partial\_{m}\mu^{e}\_{j}\leq 0 componentwise by
Lemma [2.3](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem3 "Lemma 2.3 (Analytic properties). ‣ 2.3 Emissions–Penalty Operator ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")(ii), together with optimality of x⋆x^{\star}.
Finally, concavity in θ\theta is standard in mean–variance problems with
quadratic risk penalties, and the Lipschitz bound follows from the spectral
bound on Σ\Sigma.
∎

Proposition [2.5](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem5 "Proposition 2.5 (Sensitivity). ‣ 2.7 Comparative Statics in Curvature, Robustness, and Risk Aversion ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") formalizes a simple but important message for
mandate design. Greater ambiguity aversion, as encoded by a larger robustness
budget Γ\Gamma, and sharper curvature (m↑)(m\uparrow) both reduce
emissions–adjusted expected returns, but do so in a controlled and quantifiable
manner. The dual variable π⋆\pi^{\star} admits a natural economic interpretation as
a *shadow carbon price*: it measures the marginal reduction in
risk–adjusted performance (e.g., Sharpe ratio) the investor is willing to accept
per unit tightening of the emissions ambiguity budget Γ\Gamma.

### 2.8 Distributionally Robust Extension

The ambiguity sets in §[2.4](https://arxiv.org/html/2601.06507v1#S2.SS4 "2.4 Ambiguity Sets for Emissions Uncertainty ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") control pointwise deviations of emissions intensities.
They do not, however, address the possibility that the entire joint distribution of intensity revisions shifts.
To guard against this, we embed the model in a simple divergence–based distributionally robust framework.

Let ℙ^\widehat{\mathbb{P}} be the empirical law of an underlying disturbance zz (e.g., a vector of emissions
forecast errors), and let ϕ\phi be a convex divergence generator. Define the ϕ\phi–divergence ball

|  |  |  |
| --- | --- | --- |
|  | 𝒫ρ:={ℚ≪ℙ^:Dϕ​(ℚ∥ℙ^)≤ρ},\mathcal{P}\_{\rho}:=\left\{\mathbb{Q}\ll\widehat{\mathbb{P}}:D\_{\phi}(\mathbb{Q}\,\|\,\widehat{\mathbb{P}})\leq\rho\right\}, |  |

where DϕD\_{\phi} is the usual ϕ\phi–divergence and ρ>0\rho>0 is a robustness radius. Consider a
linear loss

|  |  |  |
| --- | --- | --- |
|  | ℓx​(z):=∑i=1nxi​(γi+δi​z),\ell\_{x}(z):=\sum\_{i=1}^{n}x\_{i}(\gamma\_{i}+\delta\_{i}z), |  |

representing an emissions–adjusted drift under disturbance zz.
Here γi\gamma\_{i} is the nominal component and δi\delta\_{i} is the sensitivity of asset ii’s drift to the
disturbance, which can be interpreted as a linearization of how emissions measurement shocks propagate into
effective expected returns.

###### Theorem 2.6 (ϕ\phi–divergence DRO reformulation).

For any fixed x∈Δnx\in\Delta\_{n},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | infℚ∈𝒫ρ𝔼ℚ​[ℓx​(z)]\displaystyle\inf\_{\mathbb{Q}\in\mathcal{P}\_{\rho}}\mathbb{E}\_{\mathbb{Q}}[\ell\_{x}(z)] | =maxη≥0,ν∈ℝ{ν−ρη\displaystyle=\max\_{\eta\geq 0,\,\nu\in\mathbb{R}}\Biggl\{\nu-\rho\eta |  | (13) |
|  |  | −η𝔼ℙ^[ϕ⋆(ℓx​(z)−νη)]}.\displaystyle\qquad-\eta\,\mathbb{E}\_{\widehat{\mathbb{P}}}\Bigl[\phi^{\star}\Bigl(\frac{\ell\_{x}(z)-\nu}{\eta}\Bigr)\Bigr]\Biggr\}. |  |

where ϕ⋆\phi^{\star} denotes the convex conjugate of ϕ\phi. When ℙ^\widehat{\mathbb{P}} is discrete with
M>0M>0 support points and equal mass, the right–hand side reduces to a finite–dimensional conic program
with only two additional scalar decision variables (η,ν)(\eta,\nu).

###### Proof.

The result follows from standard Fenchel duality applied to the inner infimum over ℚ\mathbb{Q},
together with Slater’s condition for ϕ\phi–divergence balls (Boyd and Vandenberghe, [2004](https://arxiv.org/html/2601.06507v1#bib.bib62 "Convex optimization")).
The scalar variables (η,ν)(\eta,\nu) arise as dual variables associated with the divergence constraint and the
mass constraint, respectively.
∎

Theorem [2.6](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem6 "Theorem 2.6 (ϕ–divergence DRO reformulation). ‣ 2.8 Distributionally Robust Extension ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") shows that distributional robustness over a fairly rich family of models can
be implemented at minimal computational cost: we pay at most two extra scalar variables and one
expectation of ϕ⋆\phi^{\star}, which collapses to a sum in the empirical case.

### 2.9 Return–Emissions Pareto Frontier and Lipschitz Bounds

Portfolio committees typically reason in terms of trade–offs: “How much expected return must we give up
to achieve a given reduction in financed emissions?" Our framework allows us to compute this Pareto
frontier explicitly.

Consider the scalarized static “return minus carbon” problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈Δn⁡{x⊤​r−μ​x⊤​λj},μ≥0,\max\_{x\in\Delta\_{n}}\left\{x^{\top}r-\mu\,x^{\top}\lambda\_{j}\right\},\qquad\mu\geq 0, |  | (14) |

for some fixed expected return vector rr and intensity vector λj\lambda\_{j}. Let x⋆​(μ)x^{\star}(\mu) denote an
optimizer. Define

|  |  |  |
| --- | --- | --- |
|  | r¯​(μ):=x⋆​(μ)⊤​r,λ¯​(μ):=x⋆​(μ)⊤​λj,\bar{r}(\mu):=x^{\star}(\mu)^{\top}r,\qquad\bar{\lambda}(\mu):=x^{\star}(\mu)^{\top}\lambda\_{j}, |  |

where λ¯​(μ)\bar{\lambda}(\mu) is the portfolio-weighted average emissions intensity. The scalar μ\mu plays the
role of an internal carbon price in units of expected return per unit intensity. When intensities are
reported in tCO2e/$ of revenue, μ\mu can be translated to $/tCO2e by scaling expected returns into
currency units at the investor’s horizon.

###### Proposition 2.7 (Convex Pareto frontier).

As μ\mu varies in [0,∞)[0,\infty), the set
{(r¯​(μ),λ¯​(μ)):μ≥0}\{(\bar{r}(\mu),\bar{\lambda}(\mu)):\mu\geq 0\} traces the upper convex Pareto frontier of feasible
pairs (x⊤​r,x⊤​λj)(x^{\top}r,x^{\top}\lambda\_{j}) with x∈Δnx\in\Delta\_{n}. Moreover,

|  |  |  |
| --- | --- | --- |
|  | d​F⋆d​μ​(μ)=−λ¯​(μ),\frac{dF^{\star}}{d\mu}(\mu)=-\,\bar{\lambda}(\mu), |  |

whenever the derivative exists.

###### Proof.

The feasible set {(x⊤​r,x⊤​λj):x∈Δn}\{(x^{\top}r,x^{\top}\lambda\_{j}):x\in\Delta\_{n}\} is a convex polytope. For fixed xx,
the objective x⊤​r−μ​x⊤​λjx^{\top}r-\mu x^{\top}\lambda\_{j} is affine in μ\mu, so F⋆​(μ)F^{\star}(\mu) is the upper envelope
of linear functions and hence convex. Standard scalarization arguments imply that every efficient point
on the frontier is attained for some μ\mu. Differentiability and the expression for d​F⋆/d​μdF^{\star}/d\mu follow
from the envelope theorem.
∎

Proposition [2.7](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem7 "Proposition 2.7 (Convex Pareto frontier). ‣ 2.9 Return–Emissions Pareto Frontier and Lipschitz Bounds ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") underlies the empirical Pareto curves reported in §[4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios").
The scalarization parameter μ\mu is the marginal rate at which the optimizer trades expected return for
emissions intensity at the optimum. The envelope relation d​F⋆/d​μ=−λ¯​(μ)dF^{\star}/d\mu=-\bar{\lambda}(\mu) provides a
direct way to read the implied intensity from scalarized runs. Conversely, μ\mu itself can be read as
the marginal expected return the investor is willing to forego per unit reduction in portfolio intensity
(tCO2e/$ of revenue).

Finally, we quantify how sensitive the robust optimal value is to changes in the robustness budget.

###### Theorem 2.8 (Lipschitz performance bound).

Suppose the emissions–adjusted return of each asset is LL–Lipschitz in the underlying disturbance
zz in the norm induced by 𝒰j​(Γ)\mathcal{U}\_{j}(\Gamma).
Let R⋆​(Γ)R^{\star}(\Gamma) denote the optimal robust expected return of ([10](https://arxiv.org/html/2601.06507v1#S2.E10 "In 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")) (or its CVaR
analogue) under robustness budget Γ\Gamma. Then, for any Γ1,Γ2>0\Gamma\_{1},\Gamma\_{2}>0,

|  |  |  |
| --- | --- | --- |
|  | |R⋆​(Γ1)−R⋆​(Γ2)|≤L​|Γ1−Γ2|.\big|R^{\star}(\Gamma\_{1})-R^{\star}(\Gamma\_{2})\big|\leq L\,|\Gamma\_{1}-\Gamma\_{2}|. |  |

###### Proof.

Let Γ1<Γ2\Gamma\_{1}<\Gamma\_{2} and fix an optimal solution at Γ2\Gamma\_{2} with worst–case disturbance
z⋆​(Γ2)z^{\star}(\Gamma\_{2}). Radially project z⋆​(Γ2)z^{\star}(\Gamma\_{2}) onto the smaller uncertainty set associated
with Γ1\Gamma\_{1}. Lipschitz continuity of the payoff in zz bounds the change in objective value by
L​|Γ1−Γ2|L|\Gamma\_{1}-\Gamma\_{2}|. Reversing the roles of Γ1\Gamma\_{1} and Γ2\Gamma\_{2} yields the symmetric
bound.
∎

Theorem [2.8](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem8 "Theorem 2.8 (Lipschitz performance bound). ‣ 2.9 Return–Emissions Pareto Frontier and Lipschitz Bounds ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") gives an easily communicable guarantee: increasing the robustness
budget from Γ1\Gamma\_{1} to Γ2\Gamma\_{2} cannot reduce the optimal robust expected return by more than
L​|Γ2−Γ1|L|\Gamma\_{2}-\Gamma\_{1}|, all else equal. In particular, doubling Γ\Gamma does not double the
performance cost unless the Lipschitz constant is itself very large.

### 2.10 Dynamic Robust Formulation

Portfolio rebalancing interacts with evolving disclosures, transaction costs, and drift in return and
intensity processes. To make this explicit, we consider a finite–horizon dynamic model with periods
t=0,…,Tt=0,\dots,T. Let xt∈Δnx\_{t}\in\Delta\_{n} denote the portfolio at time tt, and write

|  |  |  |
| --- | --- | --- |
|  | Rt=γt+Δt​zt,R\_{t}=\gamma\_{t}+\Delta\_{t}z\_{t}, |  |

where γt\gamma\_{t} is a predictable component, Δt\Delta\_{t} is a matrix of factor loadings, and ztz\_{t} lies in an
uncertainty set ZtZ\_{t} capturing return shocks. The emissions–adjusted one–period payoff is
xt⊤​Rj,tex\_{t}^{\top}R^{e}\_{j,t}, defined via the period–tt intensities λj,t\lambda\_{j,t}.

Let β∈(0,1]\beta\in(0,1] denote a discount factor. Define the value function

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt​(xt)\displaystyle V\_{t}(x\_{t}) | :=maxxt,…,xT∈Δn⁡minzs∈Zs,s≥t\displaystyle=\max\_{x\_{t},\dots,x\_{T}\in\Delta\_{n}}\min\_{z\_{s}\in Z\_{s},\,s\geq t} |  | (15) |
|  |  | ∑s=tTβs−t​xs⊤​Rj,se,\displaystyle\qquad\sum\_{s=t}^{T}\beta^{s-t}\,x\_{s}^{\top}R^{e}\_{j,s}, |  |
|  | VT+1\displaystyle V\_{T+1} | ≡0.\displaystyle\equiv 0. |  |

###### Proposition 2.9 (Dynamic robust Bellman recursion).

The value functions {Vt}\{V\_{t}\} satisfy the recursion

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt​(xt)\displaystyle V\_{t}(x\_{t}) | =maxxt∈Δn⁡minzt∈Zt\displaystyle=\max\_{x\_{t}\in\Delta\_{n}}\min\_{z\_{t}\in Z\_{t}} |  | (16) |
|  |  | {xt⊤​Rj,te+β​Vt+1​(xt+1)}\displaystyle\qquad\Bigl\{x\_{t}^{\top}R^{e}\_{j,t}+\beta\,V\_{t+1}(x\_{t+1})\Bigr\} |  |
|  |  | t=0,…,T.\displaystyle\qquad t=0,\dots,T. |  |

with terminal condition VT+1≡0V\_{T+1}\equiv 0. If each ZtZ\_{t} is convex and compact and the one–period
problem is feasible, then VtV\_{t} is concave and the Bellman recursion preserves LP/SOCP structure when
ZtZ\_{t} is polyhedral or ellipsoidal.

###### Proof.

The result is a standard application of dynamic programming with max–min structure. Convexity and
compactness of ZtZ\_{t} ensure existence of minimizers and preservation of concavity. For polyhedral or
ellipsoidal ZtZ\_{t}, dualization of the inner minimization produces linear or SOC constraints, exactly as in
Theorem [2.4](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem4 "Theorem 2.4 (Exact conic reformulation). ‣ 2.5 Robust Mean–Variance with Emissions Penalties ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios").
∎

Proposition [2.9](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem9 "Proposition 2.9 (Dynamic robust Bellman recursion). ‣ 2.10 Dynamic Robust Formulation ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") justifies our use of rolling one–period robust problems in the empirical
section: under mild conditions, the dynamic program decomposes into a sequence of tractable conic
subproblems with turnover and other trading frictions handled via additional convex constraints.

Taken together, the results in this section show that emissions–aware robust portfolio optimization can
be formulated as a family of LP/SOCP problems with interpretable dual variables and well–behaved
comparative statics. The next section turns to the empirical ingredients—data architecture, statistical
pre–processing, and benchmark construction—required to implement these models in a realistic
large–cap equity universe.

## 3 Empirical Framework

Implementing the emissions-aware robust portfolio optimization (EAPO) model from Section [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") requires an empirical design that respects the different clocks on which financial and climate data arrive. Corporate greenhouse-gas (GHG) inventories are reported annually, financial statements are quarterly, and asset returns are observed daily. Our objective is to translate the theoretical framework into a transparent, auditable pipeline that could realistically be deployed by a large asset manager.

Figure [3](https://arxiv.org/html/2601.06507v1#S3.F3 "Figure 3 ‣ 3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") summarizes this pipeline: raw market and emissions data are ingested, pre-processed to handle missing values and estimation error, fed through the EAPO optimizer, and evaluated against financial and sustainability metrics in an out-of-sample back-test.

Throughout Section [3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios"), firms are indexed by i∈I:={1,…,n}i\in I:=\{1,\dots,n\} and rebalancing dates by t∈𝒯:={1,…,T}t\in\mathcal{T}:=\{1,\dots,T\}. We work with a U.S. large-cap equity universe and rebalance monthly on an equally spaced grid of trading dates. Boldface capitals denote random vectors and boldface lower-case letters their realizations. The full implementation and scripts are available in an online repository.111<https://github.com/stone-technologies/ERP/tree/main>

### 3.1 Data Architecture

Scope-consistent portfolio intensities require revenue-normalized emissions and a disciplined policy for handling the reporting lag in corporate carbon disclosures. The data architecture is therefore built around three principles: (i) scope-specific, revenue-normalized intensities for each firm, (ii) a forward-carry rule that mimics the information available to an investor in real time. And (iii) a joint panel structure that keeps returns, balance-sheet variables, and emissions aligned at each decision date.

##### Emissions and revenues.

For each firm ii, we obtain annual scope-specific emissions

|  |  |  |
| --- | --- | --- |
|  | (Ci,1,Ci,2,Ci,3)(tCO2e)(C\_{i,1},C\_{i,2},C\_{i,3})\quad\text{(tCO${}\_{2}$e)} |  |

from the Carbon Disclosure Project (CDP), together with the associated disclosure confidence grades. Missing emissions entries are treated as missing-not-at-random (MNAR) and handled by a hierarchical imputation procedure described in Section [3.2](https://arxiv.org/html/2601.06507v1#S3.SS2 "3.2 Statistical Pre-processing ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios"). Firm revenues Si,tS\_{i,t} are obtained from quarterly income statements and aggregated to a trailing-twelve-month measure at each rebalancing date.

##### Prices and returns.

Daily adjusted close prices {Pi,t}\{P\_{i,t}\} come from a consolidated market data provider (e.g., AlphaVantage). Gross returns are

|  |  |  |
| --- | --- | --- |
|  | Ri,t:=Pi,tPi,t−1,Rt:=(R1,t,…,Rn,t)⊤.R\_{i,t}:=\frac{P\_{i,t}}{P\_{i,t-1}},\qquad R\_{t}:=(R\_{1,t},\dots,R\_{n,t})^{\top}. |  |

We denote the unconditional mean and covariance of daily returns by

|  |  |  |
| --- | --- | --- |
|  | μ:=𝔼​[Rt],Σ:=Cov​(Rt).\mu:=\mathbb{E}[R\_{t}],\qquad\Sigma:=\mathrm{Cov}(R\_{t}). |  |

##### Emissions intensities and timing.

At each rebalancing date tt, we form scope-jj revenue-normalized emissions intensities

|  |  |  |
| --- | --- | --- |
|  | λi,j,t:=Ci,j,τ​(i,t)Si,τ​(i,t)(tCO2e/$)\lambda\_{i,j,t}:=\frac{C\_{i,j,\tau(i,t)}}{S\_{i,\tau(i,t)}}\quad\text{(tCO${}\_{2}$e/\textdollar)} |  |

|  |  |  |
| --- | --- | --- |
|  | λj,t:=(λ1,j,t,…,λn,j,t)⊤,\lambda\_{j,t}:=(\lambda\_{1,j,t},\dots,\lambda\_{n,j,t})^{\top}, |  |

where τ​(i,t)\tau(i,t) is the most recent fiscal year for which firm ii has disclosed emissions prior to date tt. Intensities are therefore forward-carried between disclosure dates, avoiding look-ahead bias and reflecting the information set available to an actual portfolio manager.

Emissions-adjusted returns R~j,t\widetilde{R}\_{j,t} are constructed by applying the emissions-penalty operator from Definition 2.1 in Section [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") to each asset, using the contemporaneous intensities λj,t\lambda\_{j,t}.

###### Assumption 3.1 (Stationary, mixing returns).

The daily return process {Rt}t≥1\{R\_{t}\}\_{t\geq 1} is strictly stationary and β\beta-mixing with a summable mixing rate. In particular, the sample mean and covariance satisfy a functional central limit theorem.

Assumption [3.1](https://arxiv.org/html/2601.06507v1#S3.Thmtheorem1 "Assumption 3.1 (Stationary, mixing returns). ‣ Emissions intensities and timing. ‣ 3.1 Data Architecture ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") is standard in empirical asset pricing and suffices for the consistency and asymptotic normality of the estimators used below. It underpins both the covariance shrinkage in Section [3.2](https://arxiv.org/html/2601.06507v1#S3.SS2 "3.2 Statistical Pre-processing ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") and the regret bounds in Section [3.4](https://arxiv.org/html/2601.06507v1#S3.SS4 "3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios").

### 3.2 Statistical Pre-processing

Two statistical pre-processing steps are essential for a stable implementation: (i) multiple imputation of missing emissions and revenues, and (ii) shrinkage of the return covariance matrix. The first addresses systematic gaps in the GHG data. The second controls estimation noise in high-dimensional covariance matrices.

##### Hierarchical multiple imputation.

Missing pairs (Ci,j,Si)(C\_{i,j},S\_{i}) are imputed using a sector-aware hierarchical model. Let sector​(i)\text{sector}(i) denote firm ii’s sector (e.g., GICS level). On the log scale we posit

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Ci,j∣sector​(i)\displaystyle\log C\_{i,j}\mid\text{sector}(i) | ∼𝒩​(ηj,sector​(i),τj2),\displaystyle\sim\mathcal{N}\!\big(\eta\_{j,\text{sector}(i)},\tau\_{j}^{2}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Si∣sector​(i)\displaystyle\log S\_{i}\mid\text{sector}(i) | ∼𝒩​(ζsector​(i),υ2),\displaystyle\sim\mathcal{N}\!\big(\zeta\_{\text{sector}(i)},\upsilon^{2}\big), |  |

with conjugate Gaussian priors on the sector-level parameters (ηj,⋅,ζ⋅)(\eta\_{j,\cdot},\zeta\_{\cdot}). Hyperparameters are estimated via empirical Bayes. Posterior modes provide point estimates, and multiple imputation is obtained by drawing KK samples from the posterior of (Ci,j,Si)(C\_{i,j},S\_{i}) and propagating them into intensities

|  |  |  |
| --- | --- | --- |
|  | λi,j,t(k):=Ci,j,τ​(i,t)(k)Si,τ​(i,t)(k),k=1,…,K,\lambda^{(k)}\_{i,j,t}:=\frac{C^{(k)}\_{i,j,\tau(i,t)}}{S^{(k)}\_{i,\tau(i,t)}},\qquad k=1,\dots,K, |  |

|  |  |  |
| --- | --- | --- |
|  | λj,t(k):=(λ1,j,t(k),…,λn,j,t(k))⊤,k=1,…,K.\lambda^{(k)}\_{j,t}:=\bigl(\lambda^{(k)}\_{1,j,t},\dots,\lambda^{(k)}\_{n,j,t}\bigr)^{\top},\qquad k=1,\dots,K. |  |

All subsequent portfolio quantities that depend on intensities—for example the emissions-adjusted mean return—are averaged over these KK draws.

###### Lemma 3.2 (Consistency of multiple imputation).

Suppose Assumption [3.1](https://arxiv.org/html/2601.06507v1#S3.Thmtheorem1 "Assumption 3.1 (Stationary, mixing returns). ‣ Emissions intensities and timing. ‣ 3.1 Data Architecture ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") holds and the hierarchical log-normal model above is correctly specified with a regular prior. Then, as the time span and number of imputations grow,

|  |  |  |
| --- | --- | --- |
|  | 1K​∑k=1Kλj,t(k)→T→∞,K→∞ℙ𝔼​[λj,t∣ℱt],\frac{1}{K}\sum\_{k=1}^{K}\lambda^{(k)}\_{j,t}\,\xrightarrow[T\to\infty,\,K\to\infty]{\mathbb{P}}\,\mathbb{E}[\lambda\_{j,t}\mid\mathcal{F}\_{t}], |  |

where ℱt\mathcal{F}\_{t} is the sigma-field generated by the observed data up to time tt.

The proof follows from a Bernstein–von Mises theorem for the hierarchical log-normal model combined with the mixing central limit theorem implied by Assumption [3.1](https://arxiv.org/html/2601.06507v1#S3.Thmtheorem1 "Assumption 3.1 (Stationary, mixing returns). ‣ Emissions intensities and timing. ‣ 3.1 Data Architecture ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios"). In practice we fix a moderate KK (e.g., 5–10), which empirically suffices to stabilize portfolio intensities.

##### Covariance shrinkage.

Sample covariance matrices of daily returns are noisy, especially when the cross-section is large relative to the time-series window. In this regime, the sample eigenvalues are severely biased, which in turn produces unstable Markowitz weights and unnecessary turnover. We use Ledoit–Wolf linear shrinkage to trade a small, controlled bias for a large reduction in estimation variance and to obtain a well-conditioned covariance estimator at each rebalancing date tt:

|  |  |  |
| --- | --- | --- |
|  | Σ^t:=δt​Ft+(1−δt)​St,\widehat{\Sigma}\_{t}:=\delta\_{t}F\_{t}+(1-\delta\_{t})S\_{t}, |  |

where StS\_{t} is the sample covariance of {Rs}s≤t−1\{R\_{s}\}\_{s\leq t-1} over a rolling window of fixed length, FtF\_{t} is a parsimonious factor-model target (e.g., constant-correlation or multi-factor), and δt∈[0,1]\delta\_{t}\in[0,1] is chosen optimally in closed form. The estimator Σ^t\widehat{\Sigma}\_{t} is positive definite by construction and rotation-equivariant, and it substantially reduces out-of-sample variance of portfolio returns relative to the raw sample covariance.

Combining multiple imputation for (C,S)(C,S) with covariance shrinkage for RR yields a set of cleaned inputs: emissions-adjusted means μ^j,t\widehat{\mu}\_{j,t}, shrinkage covariances Σ^t\widehat{\Sigma}\_{t}, and ambiguity sets calibrated from historical forecast errors. These objects drive both the benchmarks and the EAPO strategy.

### 3.3 Benchmark Portfolio Constructions

To isolate the incremental value of EAPO, we compare it with three transparent benchmarks that span common practice in institutional portfolio construction. All benchmarks respect the long-only simplex

|  |  |  |
| --- | --- | --- |
|  | Δn:={x∈ℝ≥0n:𝟏⊤​x=1}\Delta\_{n}:=\{x\in\mathbb{R}^{n}\_{\geq 0}:\mathbf{1}^{\top}x=1\} |  |

and are recomputed at each monthly rebalancing date using only information available at that time.

###### Definition 3.3 (Equal-weight portfolio (EW)).

The equal-weight portfolio holds each asset with the same weight,

|  |  |  |
| --- | --- | --- |
|  | xtEW:=1n​𝟏.x^{\mathrm{EW}}\_{t}:=\frac{1}{n}\mathbf{1}. |  |

###### Definition 3.4 (Global minimum-variance portfolio (GMV)).

Given the shrinkage covariance Σ^t\widehat{\Sigma}\_{t} at date tt, the global minimum-variance (GMV) portfolio is

|  |  |  |
| --- | --- | --- |
|  | xtGMV:=Σ^t−1​𝟏𝟏⊤​Σ^t−1​𝟏.x^{\mathrm{GMV}}\_{t}:=\frac{\widehat{\Sigma}\_{t}^{-1}\mathbf{1}}{\mathbf{1}^{\top}\widehat{\Sigma}\_{t}^{-1}\mathbf{1}}. |  |

###### Definition 3.5 (Emissions-weighted portfolio (EMW)).

Let gi,t:=Ci,1,τ​(i,t)g\_{i,t}:=C\_{i,1,\tau(i,t)} denote firm ii’s latest available scope-1 emissions at date tt. The emissions-weighted portfolio (EMW) tilts toward low emitters:

|  |  |  |
| --- | --- | --- |
|  | xi,tEMW:={gi,t−1∑k=1ngk,t−1,if ​gi,t>0,0,otherwise.x^{\mathrm{EMW}}\_{i,t}:=\begin{cases}\dfrac{g\_{i,t}^{-1}}{\sum\_{k=1}^{n}g\_{k,t}^{-1}},&\text{if }g\_{i,t}>0,\\ 0,&\text{otherwise.}\end{cases} |  |

In implementation we exclude firms with nonpositive or missing gi,tg\_{i,t} and renormalize weights over the remaining universe, so the “otherwise” branch simply encodes this exclusion.

EW serves as a simple baseline. GMV isolates the effect of risk-only optimization. EMW is a mechanically decarbonized benchmark that tilts toward low emitters without conditioning on expected returns or risk. In particular, EMW treats the estimated intensities gi,tg\_{i,t} as fixed inputs and therefore corresponds to a plug-in approach that ignores disclosure uncertainty. EAPO must improve upon these comparators in both risk-adjusted performance and emissions intensity to be economically relevant.

### 3.4 Robust Optimization Workflow

The EAPO weights xt⋆x^{\star}\_{t} at each rebalancing date are obtained by solving a robust mean–variance problem in which ambiguity arises from uncertainty in emissions-adjusted expected returns. Let μ^j,t\widehat{\mu}\_{j,t} denote the KK-draw average of emissions-adjusted mean returns at date tt (using the imputed intensities), and let Uj,t​(Γ)U\_{j,t}(\Gamma) be an ambiguity set for the misspecification εj,t\varepsilon\_{j,t} in scope-jj intensities, calibrated from past forecast errors and governed by a robustness budget Γ>0\Gamma>0.

The period-tt robust EAPO problem is

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈Δn⁡minε∈Uj,t​(Γ)⁡{x⊤​(μ^j,t−ε)−θ​x⊤​Σ^t​x},\max\_{x\in\Delta\_{n}}\,\min\_{\varepsilon\in U\_{j,t}(\Gamma)}\left\{x^{\top}\big(\widehat{\mu}\_{j,t}-\varepsilon\big)-\theta\,x^{\top}\widehat{\Sigma}\_{t}x\right\}, |  | (17) |

where θ>0\theta>0 is the investor’s risk-aversion parameter. The inner minimization attenuates expected returns in proportion to emissions uncertainty, while the outer maximization chooses portfolio weights that trade off robust expected return and variance.

###### Proposition 3.6 (Out-of-sample regret bound).

Let xt⋆x\_{t}^{\star} be an optimizer of ([17](https://arxiv.org/html/2601.06507v1#S3.E17 "In 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")) with a box-type ambiguity set and robustness budget Γ\Gamma fixed ex ante. Under Assumption [3.1](https://arxiv.org/html/2601.06507v1#S3.Thmtheorem1 "Assumption 3.1 (Stationary, mixing returns). ‣ Emissions intensities and timing. ‣ 3.1 Data Architecture ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios"),

|  |  |  |
| --- | --- | --- |
|  | supt≤T|𝔼​[xt⋆⊤​R~j,t+1]−xt⋆⊤​μ^j,t|=𝒪ℙ​(log⁡nT).\sup\_{t\leq T}\left|\mathbb{E}\big[x\_{t}^{\star\top}\widetilde{R}\_{j,t+1}\big]-x\_{t}^{\star\top}\widehat{\mu}\_{j,t}\right|=\mathcal{O}\_{\mathbb{P}}\!\left(\sqrt{\frac{\log n}{T}}\right). |  |

Proposition [3.6](https://arxiv.org/html/2601.06507v1#S3.Thmtheorem6 "Proposition 3.6 (Out-of-sample regret bound). ‣ 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") formalizes the sense in which the robust objective in ([17](https://arxiv.org/html/2601.06507v1#S3.E17 "In 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")) is a stable proxy for out-of-sample emissions-adjusted performance as the gap between what the optimizer sees at time tt and what is realized at t+1t+1 shrinks at a parametric rate, up to a mild log⁡n\sqrt{\log n} factor. The shrinkage arises from two reinforcing mechanisms. First, the box-type
ambiguity set regularizes the portfolio by uniformly bounding sensitivity to
estimation error in each asset’s emissions-adjusted drift, preventing extreme
exposures that would otherwise amplify out-of-sample noise. Second, under the
mixing assumption, estimation errors in μ^j,t\widehat{\mu}\_{j,t} concentrate at
rate T−1/2T^{-1/2}, while the supremum over nn assets introduces only a logarithmic
penalty through standard maximal inequalities. As a result, robustness trades a
small amount of in-sample optimality for stability, ensuring that the optimizer’s
perceived performance converges rapidly to realized performance even in
moderately high dimensions.

##### Projected-gradient implementation.

Solving ([17](https://arxiv.org/html/2601.06507v1#S3.E17 "In 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")) to full interior-point accuracy at every month is unnecessary and computationally heavy. Instead, we use a first-order projected-gradient method on the simplex, initialized at the previous month’s solution. The algorithm operates on the equivalent concave objective derived in Section [3.7](https://arxiv.org/html/2601.06507v1#S3.SS7 "3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") (equation ([20](https://arxiv.org/html/2601.06507v1#S3.E20 "In 3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios"))), and enforces an explicit turnover cap.

Algorithm 1  Robust emissions-aware projected gradient update

Inputs: shrinkage covariance Σ^t\widehat{\Sigma}\_{t}, emissions-adjusted mean μ^j,t\widehat{\mu}\_{j,t}, robustness budget Γ\Gamma, risk aversion θ\theta, turnover cap τ\tau, step size η\eta, previous weights xt−1x\_{t-1}.

1. 1.

   Initialize x←xt−1x\leftarrow x\_{t-1}.
2. 2.

   For k=1,…,Kiterk=1,\dots,K\_{\mathrm{iter}}:

   1. (a)

      Compute g←μ^j,t−Γ​x/∥x∥2−2​θ​Σ^t​xg\leftarrow\widehat{\mu}\_{j,t}-\Gamma\,x/\lVert x\rVert\_{2}-2\theta\,\widehat{\Sigma}\_{t}x.
   2. (b)

      Update x←ΠΔn​(x+η​g)x\leftarrow\Pi\_{\Delta\_{n}}\bigl(x+\eta g\bigr), where
      ΠΔn\Pi\_{\Delta\_{n}} is the standard O​(n​log⁡n)O(n\log n) Euclidean projection onto Δn\Delta\_{n}.
3. 3.

   If ∥x−xt−1∥1>τ\lVert x-x\_{t-1}\rVert\_{1}>\tau, set

   |  |  |  |
   | --- | --- | --- |
   |  | x←arg⁡miny∈Δn⁡{∥y−x∥2:∥y−xt−1∥1≤τ}.x\leftarrow\arg\min\_{y\in\Delta\_{n}}\bigl\{\lVert y-x\rVert\_{2}:\lVert y-x\_{t-1}\rVert\_{1}\leq\tau\bigr\}. |  |
4. 4.

   Set xt←xx\_{t}\leftarrow x.

Warm-starting from xt−1x\_{t-1} and using a modest number of iterations KiterK\_{\mathrm{iter}} yields near–KKT solutions with negligible wall-clock time, even for nn in the thousands. The explicit ℓ1\ell\_{1}-turnover cap keeps trading costs and operational complexity under control.

### 3.5 Performance and Sustainability Metrics

We evaluate each strategy on both standard risk-adjusted performance metrics and emissions-based footprint measures. Let {RtS}\{R^{S}\_{t}\} be the gross returns of strategy SS (after transaction costs), and let rtS:=RtS−1r^{S}\_{t}:=R^{S}\_{t}-1 denote net returns.

###### Definition 3.7 (Risk-adjusted performance).

Let r¯S\bar{r}^{S} be the sample mean of {rtS}\{r^{S}\_{t}\}, σ^r\hat{\sigma}\_{r} its sample standard deviation, and σ^r−\hat{\sigma}\_{r^{-}} the sample standard deviation of negative returns. Then

|  |  |  |
| --- | --- | --- |
|  | Sharpe​(S):=r¯Sσ^r,Sortino​(S):=r¯Sσ^r−.\text{Sharpe}(S):=\frac{\bar{r}^{S}}{\hat{\sigma}\_{r}},\qquad\text{Sortino}(S):=\frac{\bar{r}^{S}}{\hat{\sigma}\_{r^{-}}}. |  |

Maximum drawdown (MDD) over the sample is

|  |  |  |
| --- | --- | --- |
|  | MDD​(S):=minu≤v⁡{∏t=uvRtS−1}.\text{MDD}(S):=\min\_{u\leq v}\left\{\prod\_{t=u}^{v}R^{S}\_{t}-1\right\}. |  |

###### Definition 3.8 (Portfolio emissions intensity and yield).

For scope jj at date tt, the emissions intensity of strategy SS is the portfolio-weighted average of firm intensities,

|  |  |  |
| --- | --- | --- |
|  | Λj,tS:=xt−1S⊤​λj,t(tCO2e/$ of revenue),\Lambda^{S}\_{j,t}:=x\_{t-1}^{S\top}\lambda\_{j,t}\quad\text{(tCO${}\_{2}$e/\textdollar of revenue)}, |  |

and the corresponding emissions yield normalizes by realized net return,

|  |  |  |
| --- | --- | --- |
|  | Yj,tS:=Λj,tSrtS.Y^{S}\_{j,t}:=\frac{\Lambda^{S}\_{j,t}}{r^{S}\_{t}}. |  |

The path {Λj,tS}\{\Lambda^{S}\_{j,t}\} tracks the financed-emissions intensity of the portfolio over time, while {Yj,tS}\{Y^{S}\_{j,t}\} measures “emissions per unit of return,” a useful summary statistic when comparing strategies with different expected-return profiles. In Section [4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios") we complement these point estimates with Newey–West heteroskedasticity- and autocorrelation-robust confidence intervals for mean return differences and with block-bootstrap confidence intervals for Sharpe differences.

### 3.6 Hyper-parameter Selection

Hyper-parameters should have an economic interpretation and be calibrated by transparent procedures rather than hand-tuning. Two parameters are central for EAPO: the curvature mm of the emissions-penalty operator and the robustness budget Γ\Gamma governing the size of the ambiguity set.

##### Penalty curvature mm.

The curvature parameter m∈ℕ+m\in\mathbb{N}\_{+} controls how aggressively the emissions-penalty operator from Definition 2.1 attenuates the returns of high-intensity firms. A larger mm steepens the penalty as λi,j,t\lambda\_{i,j,t} approaches the cross-sectional maximum, pushing more weight into the lowest-intensity names.

We select mm via nested rolling cross-validation. An inner loop, operating on a training window, computes the empirical return–emissions Pareto frontier for a grid m∈{1,10,100,1000}m\in\{1,10,100,1000\} and identifies the smallest mm such that the Sharpe ratio on the efficient frontier does not deteriorate by more than 5% relative to m=1m=1. An outer loop evaluates the resulting m⋆m^{\star} out of sample. This procedure yields a penalty that is “as curved as necessary but no more,” in the sense of preserving most of the classical mean–variance frontier while delivering substantial emissions reductions.

##### Robustness budget Γ\Gamma.

The robustness budget Γ>0\Gamma>0 determines the radius of the ambiguity set around estimated intensities. In the conic reformulation discussed in Section [3.7](https://arxiv.org/html/2601.06507v1#S3.SS7 "3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios"), the dual multiplier on the ambiguity constraint has a natural interpretation as a shadow carbon price: it is the marginal rate at which the investor is willing to sacrifice expected return (in basis points) to buy protection against misspecified emissions.

We therefore calibrate Γ\Gamma by a profile-likelihood–style condition: we choose Γ⋆\Gamma^{\star} such that the estimated dual shadow price π⋆​(Γ)\pi^{\star}(\Gamma) lies below a pre-specified monetary threshold determined by the investor (e.g., “we are willing to pay up to 10 basis points of expected return per 10% reduction in worst-case intensity”). This makes Γ\Gamma an economically interpretable policy lever rather than a free statistical knob.

With (m⋆,Γ⋆)(m^{\star},\Gamma^{\star}) fixed ex ante, all reported results in Section [4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios") are genuine out-of-sample tests of the EAPO strategy.

### 3.7 EAPO: From Theory to Implementable Program

This subsection collects the optimization primitives into the single static problem that Algorithm [1](https://arxiv.org/html/2601.06507v1#alg1 "Algorithm 1 ‣ Projected-gradient implementation. ‣ 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") approximately solves each month. Fix a scope jj (we use j=1j=1 in the main experiments) and consider a one-period setting with gross returns R=(R1,…,Rn)⊤R=(R\_{1},\dots,R\_{n})^{\top} and weights x∈Δnx\in\Delta\_{n}. At date tt, the scope-jj intensities are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λi,j,t\displaystyle\lambda\_{i,j,t} | :=Ci,j,τ​(i,t)Si,τ​(i,t)(tCO2e/$),\displaystyle=\frac{C\_{i,j,\tau(i,t)}}{S\_{i,\tau(i,t)}}\quad\text{(tCO${}\_{2}$e/\textdollar)}, |  | (18) |
|  | λj,t\displaystyle\lambda\_{j,t} | :=(λ1,j,t,…,λn,j,t)⊤.\displaystyle=(\lambda\_{1,j,t},\dots,\lambda\_{n,j,t})^{\top}. |  |

Let λmax,j,t:=maxk⁡λk,j,t\lambda\_{\max,j,t}:=\max\_{k}\lambda\_{k,j,t} be the cross-sectional maximum intensity at tt. For curvature m∈ℕ+m\in\mathbb{N}\_{+}, the emissions-penalty operator from Definition 2.1 specializes to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Pj(m)​(r,λ)\displaystyle P^{(m)}\_{j}(r,\lambda) | :=(1−λλmax,j,t)m​r,\displaystyle=\Bigl(1-\frac{\lambda}{\lambda\_{\max,j,t}}\Bigr)^{m}r, |  | (19) |
|  | R~i,te\displaystyle\widetilde{R}\_{i,t}^{e} | :=Pj(m)​(Ri,t,λi,j,t).\displaystyle=P^{(m)}\_{j}(R\_{i,t},\lambda\_{i,j,t}). |  |

The map is linear in rr and decreasing, smooth, and Schur-convex in λ\lambda, higher-intensity firms suffer a larger proportional reduction in their effective returns.

Define the emissions-adjusted expected return for asset ii at time tt as

|  |  |  |
| --- | --- | --- |
|  | μi,j,te:=𝔼​[R~i,te],\mu\_{i,j,t}^{e}:=\mathbb{E}\big[\widetilde{R}\_{i,t}^{e}\big], |  |

and let μj,te\mu\_{j,t}^{e} be the vector collecting these means. Using the Lipschitz properties of Pj(m)P^{(m)}\_{j} with respect to λ\lambda one can construct a simple bound on how much misspecification in intensities can distort the portfolio’s mean.

###### Lemma 3.9 (Lipschitz envelope).

For each asset ii there exists a constant

|  |  |  |
| --- | --- | --- |
|  | Li:=mλmax,j​𝔼​[|Ri|]L\_{i}:=\frac{m}{\lambda\_{\max,j}}\,\mathbb{E}[|R\_{i}|] |  |

such that

|  |  |  |
| --- | --- | --- |
|  | |∂∂λ​𝔼​[Pj(m)​(Ri,λ)]|≤Li.\left|\frac{\partial}{\partial\lambda}\mathbb{E}\big[P^{(m)}\_{j}(R\_{i},\lambda)\big]\right|\leq L\_{i}. |  |

Consequently, for any ℓp\ell\_{p} ambiguity ball

|  |  |  |
| --- | --- | --- |
|  | {ε∈ℝn:‖ε‖p≤Γ}\{\varepsilon\in\mathbb{R}^{n}:\|\varepsilon\|\_{p}\leq\Gamma\} |  |

on intensities, the worst-case deterioration in emissions-adjusted expected return is bounded by

|  |  |  |
| --- | --- | --- |
|  | sup‖ε‖p≤Γx⊤​(μje​(λ)−μje​(λ+ε))≤Γ​‖diag​(L)​x‖p⋆,\sup\_{\|\varepsilon\|\_{p}\leq\Gamma}x^{\top}\big(\mu\_{j}^{e}(\lambda)-\mu\_{j}^{e}(\lambda+\varepsilon)\big)\leq\Gamma\,\|\mathrm{diag}(L)\,x\|\_{p^{\star}}, |  |

where p⋆p^{\star} is the dual norm and diag​(L)\mathrm{diag}(L) is the diagonal matrix with entries LiL\_{i}.

Lemma [3.9](https://arxiv.org/html/2601.06507v1#S3.Thmtheorem9 "Lemma 3.9 (Lipschitz envelope). ‣ 3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") motivates the static robust mean–variance objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈Δn⁡{x⊤​μje−Γ​‖diag​(L)​x‖p⋆−θ​x⊤​Σ​x},\max\_{x\in\Delta\_{n}}\Big\{x^{\top}\mu\_{j}^{e}-\Gamma\|\mathrm{diag}(L)\,x\|\_{p^{\star}}-\theta\,x^{\top}\Sigma x\Big\}, |  | (20) |

where Γ\Gamma plays the role of the robustness budget and p∈{1,2,∞}p\in\{1,2,\infty\} determines the shape of the ambiguity set.

###### Proposition 3.10 (Robust mean–variance as LP/SOCP).

For p∈{1,∞}p\in\{1,\infty\}, problem ([20](https://arxiv.org/html/2601.06507v1#S3.E20 "In 3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")) can be written as a linear program (LP) with O​(n)O(n) additional variables and constraints. For p=2p=2, it admits a second-order cone program (SOCP) representation with O​(n)O(n) second-order cones. In all cases the problem is solvable in polynomial time.

In the empirical implementation we specialize to the ℓ2\ell\_{2} case with diag​(L)\mathrm{diag}(L) absorbed into the scaling of Γ\Gamma, so that the ambiguity penalty reduces to Γ​‖x‖2\Gamma\|x\|\_{2}. The gradient of ([20](https://arxiv.org/html/2601.06507v1#S3.E20 "In 3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")) in this specialization is exactly the expression used in Algorithm [1](https://arxiv.org/html/2601.06507v1#alg1 "Algorithm 1 ‣ Projected-gradient implementation. ‣ 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") and equation ([22](https://arxiv.org/html/2601.06507v1#S4.E22 "In 4.1 Projected-gradient solver ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios")) in Section [4.1](https://arxiv.org/html/2601.06507v1#S4.SS1 "4.1 Projected-gradient solver ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios").

###### Remark 3.11 (Shadow carbon price).

In the conic reformulation of ([20](https://arxiv.org/html/2601.06507v1#S3.E20 "In 3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")), the dual multiplier on the ambiguity constraint is equal to −∂V⋆/∂Γ-\partial V^{\star}/\partial\Gamma, where V⋆​(Γ)V^{\star}(\Gamma) is the optimal value. This multiplier is naturally interpreted as an investor-specific shadow carbon price: it is the marginal reduction in expected Sharpe per marginal tightening of the robustness budget.

Finally, to map out the efficient trade-off between expected return and portfolio emissions intensity, we consider the scalarized problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈Δn⁡{x⊤​r−μ​x⊤​λj},μ≥0,\max\_{x\in\Delta\_{n}}\Big\{x^{\top}r-\mu\,x^{\top}\lambda\_{j}\Big\},\qquad\mu\geq 0, |  | (21) |

where rr is a vector of expected returns and μ\mu is a Lagrange multiplier on scope-jj intensity.

Proposition [2.7](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem7 "Proposition 2.7 (Convex Pareto frontier). ‣ 2.9 Return–Emissions Pareto Frontier and Lipschitz Bounds ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") makes explicit the cost, in expected return units, of tightening the portfolio’s emissions constraint. Empirically, the frontier in Figure [7](https://arxiv.org/html/2601.06507v1#S4.F7 "Figure 7 ‣ 4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") shows that large reductions in average scope-1 intensity are attainable at modest return cost over a wide range of μ\mu, a point we return to in Section [4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios").

Taken together, Sections [3.2](https://arxiv.org/html/2601.06507v1#S3.SS2 "3.2 Statistical Pre-processing ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")–[3.7](https://arxiv.org/html/2601.06507v1#S3.SS7 "3.7 EAPO: From Theory to Implementable Program ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios") specify a complete, implementable EAPO system: data are cleaned and aligned, benchmark and robust portfolios are constructed on an equal footing, and hyper-parameters are chosen by economically interpretable rules. The next section evaluates how this system performs out of sample relative to the benchmarks, both financially and in terms of financed emissions.

|  |
| --- |
| Data sources (prices, emissions, revenues) |
| ↓\downarrow |
| Pre-processing (imputation, mapping, shrinkage) |
| ↓\downarrow |
| EAPO model (P(m)P^{(m)}, ambiguity, SOCP and LP) |
| ↓\downarrow |
| Projected gradient with turnover projection |
| ↓\downarrow |
| Evaluation (wealth, Sharpe, drawdown, intensity) |

Figure 3: Workflow from data ingestion to optimization and evaluation.



![Refer to caption](figures/CDF_TOP_EMISSIONS.jpg)


(a) Cumulative distribution of reported emissions across firms.

![Refer to caption](figures/TOP_REVENUE.jpg)


(b) Firms with the highest reported revenue over the sample period.

Figure 4: Distribution of reported emissions and concentration of revenue among the largest firms. Panels show (a) the cumulative distribution of reported emissions across firms and (b) the set of firms with the highest reported revenue over the sample period.



![Refer to caption](figures/uncertainty_area_ts.png)


(a) Evolution of uncertainty set area over time.

![Refer to caption](figures/uncertainty_ellipses.png)


(b) Annual uncertainty sets visualized as ellipses.

Figure 5: Temporal dynamics and cross-sectional geometry of uncertainty sets. Panels show (a) the evolution of the uncertainty set area over time and (b) annual uncertainty sets represented as ellipses in the state space.

## 4 Empirical Results

We evaluate the empirical performance of the emissions-aware robust optimization framework. In particular, we evaluate whether EAPO can deliver order-of-magnitude reductions in financed emissions while preserving risk-adjusted performance once we charge realistic transaction costs.

Our empirical design follows the data architecture in Section [3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios"). Annual Scope-1 intensities are computed as
λi,1,t=Ci,1,t/Si,t\lambda\_{i,1,t}=C\_{i,1,t}/S\_{i,t}
mapped to the monthly rebalancing grid using a forward-carry convention that
reflects the reporting lags in corporate carbon disclosures. Portfolios are
rebalanced on the last trading day of each month using a
252-trading-day lookback window for both mean and covariance estimates.
We impose uniform transaction costs of 2​bps2\,\text{bps} per dollar traded,
measured in ℓ1\ell\_{1} turnover. All strategies respect the long-only budget
constraint xt∈ΔS:={x∈ℝ≥0n:𝟏⊤​x=1}x\_{t}\in\Delta^{S}:=\{x\in\mathbb{R}^{n}\_{\geq 0}:\mathbf{1}^{\top}x=1\}.

EAPO is evaluated against three standard benchmarks constructed from the same universe and data: (i) equal weight (EW), (ii) a global minimum-variance proxy based on inverse variance (GMV), and (iii) an emissions-weighted portfolio (EMW) with xi∝1/Ci,1,tx\_{i}\propto 1/C\_{i,1,t} conditional on positive Scope-1 emissions. This configuration isolates the incremental effect of robustness relative to a mechanically decarbonized tilt (EMW), a risk-only optimizer (GMV), and an equal-weight baseline (EW).

The remainder of this section is organized as follows. Section [4.1](https://arxiv.org/html/2601.06507v1#S4.SS1 "4.1 Projected-gradient solver ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") briefly describes the projected-gradient implementation used to solve the EAPO problem at scale. Section [4.2](https://arxiv.org/html/2601.06507v1#S4.SS2 "4.2 HAC inference ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") outlines the HAC inference used to compare strategies with serially correlated daily returns. Section [4.3](https://arxiv.org/html/2601.06507v1#S4.SS3 "4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") presents the main performance and footprint results, together with sensitivity to model parameters and turnover constraints. Section [4.4](https://arxiv.org/html/2601.06507v1#S4.SS4 "4.4 Discussion ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") interprets these findings through the lens of mandates, regulation, and disclosure practice.

### 4.1 Projected-gradient solver

Interior-point methods are numerically robust but heavier than necessary for end-of-day rebalancing on large universes. Given the smooth, strictly concave objective in our robust mean–variance specification, a first-order method with simplex projection is sufficient and far more scalable.

For each rebalancing date tt, let μ^te\hat{\mu}^{e}\_{t} denote the vector of emissions-adjusted expected returns and Σt\Sigma\_{t} the Ledoit–Wolf shrinkage covariance built from the 252-day rolling window. The robust mean–variance objective in ([17](https://arxiv.org/html/2601.06507v1#S3.E17 "In 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios")) yields the gradient

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇ft​(x)=μ^te−Γ​x‖x‖2− 2​θ​Σt​x,\nabla f\_{t}(x)\,=\,\hat{\mu}^{e}\_{t}\,-\,\Gamma\,\frac{x}{\|x\|\_{2}}\,-\,2\theta\,\Sigma\_{t}x, |  | (22) |

where Γ>0\Gamma>0 is the robustness budget on intensity ambiguity and θ>0\theta>0 is the risk-aversion parameter.

We maximize ftf\_{t} over the simplex ΔS\Delta\_{S} by projected gradient:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x(k+1)=ΠΔS​(x(k)+η​∇ft​(x(k))),x^{(k+1)}\,=\,\Pi\_{\Delta\_{S}}\!\bigl(x^{(k)}+\eta\,\nabla f\_{t}(x^{(k)})\bigr), |  | (23) |

where η>0\eta>0 is the stepsize and ΠΔS\Pi\_{\Delta\_{S}} is the simplex projection, implemented in O​(n​log⁡n)O(n\log n) time using the standard sorting-based algorithm. Warm-starting at x(0)=xt−1x^{(0)}=x\_{t-1} exploits temporal smoothness in the optimal solution and collapses wall-clock time. In practice, a modest and fixed number of iterations suffices for convergence to first-order optimality.

Turnover is controlled explicitly rather than via ad hoc penalties. After the projected step, we enforce an ℓ1\ell\_{1} turnover cap τ\tau by projecting onto the intersection

|  |  |  |
| --- | --- | --- |
|  | {y∈ΔS:‖y−xt−1‖1≤τ},\bigl\{y\in\Delta\_{S}:\|y-x\_{t-1}\|\_{1}\leq\tau\bigr\}, |  |

again using a closed-form ℓ1\ell\_{1} ball projection. The resulting algorithm is summarized in Algorithm [1](https://arxiv.org/html/2601.06507v1#alg1 "Algorithm 1 ‣ Projected-gradient implementation. ‣ 3.4 Robust Optimization Workflow ‣ 3 Empirical Framework ‣ Emissions-Robust Portfolios"). The O​(n​log⁡n)O(n\log n) projection keeps per-iteration cost low, warm starts across months keep the number of iterations small. The method preserves feasibility at all times and admits a simple stopping rule based on the projected gradient norm. In what follows, the optimization error is negligible relative to estimation noise in μ^te\hat{\mu}^{e}\_{t} and Σt\Sigma\_{t}.

### 4.2 HAC inference

Daily P&L differences between strategies are serially correlated and heteroskedastic. Standard errors that assume independence would overstate significance. We therefore rely on standard Newey–West heteroskedasticity- and autocorrelation-consistent (HAC) standard errors to conduct pairwise tests of average daily returns.

For any two strategies AA and BB, let RtAR^{A}\_{t} and RtBR^{B}\_{t} denote gross daily returns and define the return differential

|  |  |  |
| --- | --- | --- |
|  | Δt=(RtA−1)−(RtB−1).\Delta\_{t}=(R^{A}\_{t}-1)-(R^{B}\_{t}-1). |  |

Let Δ¯\bar{\Delta} be the sample mean of {Δt}t=1T\{\Delta\_{t}\}\_{t=1}^{T}, and define the sample autocovariances

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ^ℓ\displaystyle\hat{\gamma}\_{\ell} | =1T​∑t>ℓ(Δt−Δ¯)​(Δt−ℓ−Δ¯)\displaystyle=\frac{1}{T}\sum\_{\,t>\ell}(\Delta\_{t}-\bar{\Delta})\,(\Delta\_{t-\ell}-\bar{\Delta}) |  | (24) |
|  |  | ℓ=0,1,…,L.\displaystyle\qquad\ell=0,1,\dots,L. |  |

The Newey–West variance estimator with bandwidth LL is

|  |  |  |  |
| --- | --- | --- | --- |
|  | se^2=γ^0+ 2​∑ℓ=1L(1−ℓL+1)​γ^ℓ,\widehat{\mathrm{se}}^{2}\,=\,\hat{\gamma}\_{0}\,+\,2\sum\_{\ell=1}^{L}\Bigl(1-\frac{\ell}{L+1}\Bigr)\hat{\gamma}\_{\ell}, |  | (25) |

and the associated tt-statistic is t=Δ¯/se^t=\bar{\Delta}/\widehat{\mathrm{se}}. We set L=20L=20, corresponding to roughly one trading month of serial dependence, which yields conservative confidence intervals for our horizon and sampling frequency. All statements below about differences in average returns are supported by these HAC standard errors.

### 4.3 Baseline comparison and robustness

Table [1](https://arxiv.org/html/2601.06507v1#S4.T1 "Table 1 ‣ 4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") reports annualized performance and average Scope-1 intensity for the three benchmarks and the EAPO strategy under our baseline configuration: monthly rebalancing, a 252-day lookback, and 2 bps transaction costs per dollar traded.

Table 1: Monthly rebalancing, 252-day window, 2 bps transaction costs.

| Strategy | Ann. Ret (%) | Ann. Vol (%) | Sharpe | MaxDD (%) | Avg Scope-1 Intensity |
| --- | --- | --- | --- | --- | --- |
| Equal Weight | 13.397 | 18.726 | 0.766 | -39.375 | 246.066 |
| GMV (inv-var) | 9.470 | 16.585 | 0.629 | -37.386 | 347.016 |
| EMW (1/Scope-1) | 14.501 | 21.389 | 0.740 | -39.285 | 100.129 |
| EAPO (Γ=3.5,m=10,θ=0.5\Gamma{=}3.5,\,m{=}10,\,\theta{=}0.5) | 12.698 | 17.767 | 0.762 | -37.412 | 18.297 |

Carbon footprint.
EAPO’s average Scope-1 intensity is 18.30 tCO2e per $mm of revenue, compared with 246.07 for EW, 347.02 for GMV, and 100.13 for the naive EMW tilt. This corresponds to a reduction of approximately 92.6% relative to EW, 94.7% relative to GMV, and 81.7% relative to EMW. Equivalently, relative to conventional large-cap benchmarks, the EAPO strategy finances roughly one-tenth as much Scope-1 carbon per unit of revenue. Cross-sectional distributions of portfolio-weighted intensities confirm that this reduction is broad-based: the entire distribution shifts left rather than being driven by a handful of ultra-low-emissions names.

Risk and return.
Despite this dramatic footprint reduction, EAPO exhibits benchmark-level risk-adjusted performance. Its annualized Sharpe ratio is 0.762, which is close to equal weight (0.766) and comparable to the emissions-minimizing benchmark (0.740), while exceeding GMV (0.629). Volatility is 17.8% annualized, below EW (18.7%) and well below EMW (21.4%). Maximum drawdown is slightly smaller than EW and EMW (about −37.4%-37.4\% versus −39.3%-39.3\%), and close to GMV.

Average annual returns are naturally somewhat lower than for the more aggressive EW and EMW portfolios (12.7% versus 13.4% and 14.5%), but the difference is modest in economic terms. HAC/Newey–West tests on daily return differences (EAPO minus EW/GMV/EMW, with L=20L{=}20) yield tt-statistics of approximately −0.52-0.52, 1.091.09, and −0.64-0.64, respectively—well below conventional significance thresholds. Any differences in Sharpe are primarily attributable to volatility, not to a statistically detectable change in average returns.

The distribution of daily excess returns (EAPO minus EW) is tightly concentrated around zero with slightly heavier shoulders than a Gaussian benchmark, consistent with a strategy that rebalances risk but does not systematically time the market. Cumulative wealth and drawdown paths show EAPO tracking EW closely, with marginally shallower troughs during stress periods, including the COVID-19 drawdown.

Sector exposure and attribution.
A common concern is that large emissions reductions may simply proxy for extreme sector rotation. To diagnose this channel, Table [2](https://arxiv.org/html/2601.06507v1#S4.T2 "Table 2 ‣ 4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") decomposes the reduction in average intensity into a sector allocation component and a within-sector selection component, in the spirit of Brinson-style attribution. In our baseline, roughly three quarters of the intensity reduction relative to EW comes from underweighting high-intensity sectors, with the remainder coming from within-sector reweighting toward lower-intensity firms. Figure [6](https://arxiv.org/html/2601.06507v1#S4.F6 "Figure 6 ‣ 4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") visualizes the largest average sector weight differences between EAPO and EW.

Table 2: Emissions attribution of EAPO versus the equal-weight benchmark. The decomposition writes the difference in average portfolio intensity as the sum of a sector allocation term and a within-sector selection term.

| Component | Value |
| --- | --- |
| Average Scope-1 intensity, Equal Weight | 246.066 |
| Average Scope-1 intensity, EAPO | 18.297 |
| Total reduction (EW minus EAPO) | 227.769 |
| Sector allocation component | 174.112 ( 76.4% ) |
| Within-sector selection component | 53.860 ( 23.6% ) |

![Refer to caption](figures/R2_sector_tilts_eapo_minus_ew.png)


Figure 6: Average sector weight differences between EAPO and the equal-weight benchmark. The plot reports the top sectors by absolute weight difference, with the remainder aggregated into an “Other sectors” category.

Benchmark tracking.
Table [3](https://arxiv.org/html/2601.06507v1#S4.T3 "Table 3 ‣ 4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") reports beta, correlation, and tracking error relative to the equal-weight benchmark. EAPO maintains a high correlation with EW and a modest tracking error, consistent with a decarbonization overlay rather than a wholesale reallocation of aggregate market risk.

Table 3: Benchmark-tracking diagnostics relative to the equal-weight portfolio. Tracking error is the annualized standard deviation of daily active returns. The information ratio is the annualized mean active return divided by tracking error.

| Strategy | Beta | Correlation | Tracking error (%) | Information ratio |
| --- | --- | --- | --- | --- |
| GMV (inv-var) | 0.864 | 0.975 | 4.464 | -0.874 |
| EMW (1/Scope-1) | 1.008 | 0.883 | 10.047 | 0.150 |
| EAPO | 0.925 | 0.975 | 4.202 | -0.189 |

Subperiod stability and inference on Sharpe differences.
Appendix Table [4](https://arxiv.org/html/2601.06507v1#S6.T4 "Table 4 ‣ 6.7 Supplementary tables and figures ‣ 6 Appendix ‣ Emissions-Robust Portfolios") provides block-bootstrap confidence intervals for the Sharpe difference between EAPO and EW, which are wide enough to encompass economically small positive and negative values. Appendix Table [5](https://arxiv.org/html/2601.06507v1#S6.T5 "Table 5 ‣ 6.7 Supplementary tables and figures ‣ 6 Appendix ‣ Emissions-Robust Portfolios") reports simple price-based style diagnostics computed at rebalance dates.

Turnover, frictions, and parameter sweeps.
A natural concern is that robust decarbonization might require frequent trading and therefore high implicit and explicit costs. In our baseline configuration, average monthly ℓ1\ell\_{1} turnover for EAPO is in the low single digits as a percentage of portfolio weight, so at 2 bps per dollar traded the drag from transaction costs is well below 1 bp per rebalance and economically negligible at a monthly horizon.

We also explore sensitivity to the risk-aversion parameter θ\theta and to turnover caps τ\tau. Without a turnover cap, wealth trajectories for different values of θ\theta are tightly bunched, and average Scope-1 intensities are nearly unchanged. This is economically intuitive: the ℓ2\ell\_{2}-based robustness term already discourages excessive concentration, so moderate changes in θ\theta mainly smooth the weights without materially altering the emissions profile.

Imposing a turnover cap of τ=0.2\tau=0.2 (20% of notional per month) reduces turnover further, with little visible impact on cumulative wealth or average intensity. Pareto plots of expected return versus average Scope-1 intensity exhibit the convex, monotone trade-off predicted by Proposition [2.7](https://arxiv.org/html/2601.06507v1#S2.Thmtheorem7 "Proposition 2.7 (Convex Pareto frontier). ‣ 2.9 Return–Emissions Pareto Frontier and Lipschitz Bounds ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios"): large reductions in intensity are attainable with modest movements along the expected-return axis, and the volatility “bubble sizes” remain comparable across the frontier rather than exploding in the low-emissions region.

Holdings transparency.
To make the emissions reductions interpretable at the security level, Appendix Table [7](https://arxiv.org/html/2601.06507v1#S6.T7 "Table 7 ‣ 6.7 Supplementary tables and figures ‣ 6 Appendix ‣ Emissions-Robust Portfolios") reports the top holdings by average weight in the baseline EAPO portfolio together with their average Scope-1 intensities. Appendix Figure [9](https://arxiv.org/html/2601.06507v1#S6.F9 "Figure 9 ‣ 6.7 Supplementary tables and figures ‣ 6 Appendix ‣ Emissions-Robust Portfolios") visualizes the corresponding monthly weight paths. For replication and integration into reporting pipelines, we also provide a full monthly weight panel for EW, GMV, EMW, and EAPO as CSV exports in the supplementary files.

![Refer to caption](figures/R2_pareto_frontier.png)


(a) Pareto frontier: annualized return versus average Scope-1 intensity under a μ\mu-sweep.

![Refer to caption](figures/R2_turnover_series.png)


(b) Monthly ℓ1\ell\_{1} turnover per rebalance for EAPO (θ=0.5\theta=0.5) under a turnover cap τ=0.20\tau=0.20.

Figure 7: Return–emissions trade-off and implementability. The left panel traces the empirical return–Scope-1-intensity frontier as the scalarization weight μ\mu varies. The right panel reports realized turnover across rebalances under a representative turnover cap.



![Refer to caption](figures/R2_cum_wealth.png)


(a) Cumulative wealth of EAPO, and benchmarks equal weight, global minimum variance (EWM), and inverse scope (EMW)

![Refer to caption](figures/R2_drawdowns.png)


(b) Max drawdown comparison between EAPO and EW

![Refer to caption](figures/R2_hist_eapo_minus_ew.png)


(c) Distribution of daily excess return between EAPO and EW

Figure 8: (i)–(iii) summary of portfolio performance.

Taken together, these results support the claim that emissions-aware robustness can achieve order-of-magnitude reductions in financed Scope-1 intensity while delivering benchmark-level Sharpe ratios.

### 4.4 Discussion

Performance statistics alone do not justify deployment in an institutional setting. The strategy must also align with regulatory developments and internal governance. The empirical results above show that EAPO satisfies three requirements that matter for asset owners and regulators alike.

First, material decarbonization: the reductions in portfolio-level Scope-1 intensity—on the order of 80–95% relative to standard benchmarks in our sample—are large enough to matter for financed-emissions reporting under PCAF and related frameworks. The fact that the reduction is broad-based across the book, rather than concentrated in a small sleeve, makes it easier to communicate the effect to clients and oversight committees.

Second, financial integrity: we do not observe statistically significant changes in average daily returns relative to EW, GMV, or EMW once serial correlation is accounted for with HAC inference. Sharpe ratios remain close to benchmark values, and any differences are largely attributable to modest changes in volatility and drawdowns rather than to pursuing climate-themed risk premia. This property is important for mandate governance: a risk committee can adopt EAPO as a sustainability overlay without implicitly accepting a fundamentally different return-generation process.

Third, operational tractability: the projected-gradient implementation with explicit turnover control, combined with the LP/SOCP structure of the underlying robust problem, scales comfortably to institutional universes. The algorithm respects existing long-only, fully-invested constraints, and the dual variables admit a clear interpretation as shadow carbon prices, which can be reported alongside traditional risk budgets.

#### 4.4.1 Why deep decarbonization can be performance neutral

The absence of a Sharpe penalty is consistent with several mechanisms. First, emissions intensity is correlated with sector membership and with standard equity characteristics, so decarbonization can be achieved through a combination of sector allocation and within-sector selection. Table [2](https://arxiv.org/html/2601.06507v1#S4.T2 "Table 2 ‣ 4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") shows that, in our baseline, most of the reduction in average intensity relative to EW comes from underweighting high-intensity sectors, with a material remainder coming from reweighting toward lower-intensity firms within sectors. Figure [6](https://arxiv.org/html/2601.06507v1#S4.F6 "Figure 6 ‣ 4.3 Baseline comparison and robustness ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios") makes the associated sector tilts explicit. When sector tilts and within-sector dispersion both contribute, the opportunity cost of decarbonization depends on cross-sector risk premia and on competitive dispersion rather than on an arbitrary loss of diversification.

Second, carbon exposure can behave like a priced factor, but the associated compensation is time-varying and can be partially subsumed by other state variables. Carbon-intensive firms have earned higher average returns in some samples, consistent with a transition-risk premium (Bolton and Kacperczyk, [2021](https://arxiv.org/html/2601.06507v1#bib.bib81 "Do investors care about carbon risk?")). A penalty on emissions therefore reduces expected return when the carbon premium is positive. In finite samples, realized carbon premia can be weak and can co-move with standard factor returns. One plausible channel for performance neutrality is therefore a combination of moderate shadow carbon prices and correlated factor realizations over the back-test window.

Third, transition risk is asymmetric. Option-implied evidence indicates that high-emissions firms embed downside climate risk that is not well summarized by variance (Ilhan et al., [2021](https://arxiv.org/html/2601.06507v1#bib.bib82 "Carbon tail risk")). By reallocating away from high-intensity firms, an emissions-aware strategy can reduce exposure to tail risk that is imperfectly priced or poorly proxied by quadratic risk. This channel can raise realized Sharpe ratios even when average returns are unchanged.

Finally, robustness changes the optimization problem in a way that can improve out-of-sample performance. The ambiguity penalty shrinks the solution away from concentrated positions that are sensitive to noisy estimates of both expected returns and emissions intensities. This regularization can lower realized volatility and turnover. It also stabilizes the emissions footprint when disclosures are revised, which reduces implementation risk for mandate reporting. In the model, the dual multiplier on the ambiguity radius provides a disciplined summary of this trade-off in return units.

In summary, the empirical evidence is consistent with the message of Sections [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios")–[3](https://arxiv.org/html/2601.06507v1#S3 "3 Empirical Framework ‣ Emissions-Robust Portfolios"): an axiomatized emissions-penalty operator, embedded in a robust mean–risk program with explicit implementability controls, can move a large long-only equity portfolio substantially down the emissions ladder while leaving conventional performance statistics essentially unchanged. This makes EAPO a credible choice for mandates in which financed emissions are a primary objective rather than a secondary disclosure metric.

## 5 Conclusion and Future Research

This paper develops and empirically validates an emissions-aware portfolio optimization (EAPO) framework that remains tractable at institutional scale while being explicitly robust to uncertainty in corporate greenhouse gas (GHG) reporting. By embedding a scope-specific, axiomatized emissions-penalty operator into convex robust programs with exact LP/SOCP representations, we show that climate objectives can be placed on the same footing as classical mean–variance and CVaR criteria. The framework preserves the familiar geometry of portfolio choice while internalizing financed emissions through a disciplined treatment of measurement error.

Our analysis delivers three main messages.
First, on the modeling side, we characterize a unique family of curvature-controlled emissions-penalty operators that are compatible with homogeneity, scale invariance, mixture linearity, and a semigroup property. This operator nests smoothly into both moment- and distributionally-robust formulations, admits linear or second-order cone reformulations, and yields dual variables that are naturally interpretable as shadow carbon prices. These duals quantify, in return units, the marginal cost of additional robustness against misreported emissions, providing a direct bridge between optimization primitives and climate-policy narratives.

Second, on the algorithmic side, we show that emissions-aware robustness does not require sacrificing scalability. The EAPO problems we study reduce to sparse LP/SOCP instances with complexity linear in the number of assets and cones, and can be solved reliably via projected-gradient schemes on the simplex with turnover projections. This architecture is compatible with daily or monthly rebalancing, standard covariance shrinkage, and realistic transaction-cost schedules, making it implementable within existing buy-side risk and execution stacks.

Third, on the empirical side, we document that robust decarbonization is attainable at negligible performance cost in a large-cap U.S. equity universe. In our baseline S&P 500 experiment with monthly rebalancing, EAPO reduces average Scope 1 portfolio emissions intensity by roughly an order of magnitude relative to the equal-weight benchmark, and by more than 80% relative to a simple emissions-weighted portfolio, while delivering Sharpe ratios that are statistically indistinguishable from those benchmarks under block-bootstrap inference. Drawdowns remain comparable or slightly attenuated, transaction-cost drag is modest under realistic turnover caps, and the return–emissions Pareto frontier exhibits the predicted convex shape: large reductions in financed emissions are available at small marginal costs in risk-adjusted performance. Taken together, these results suggest that properly designed robust optimization can reconcile sustainability constraints with traditional portfolio objectives in a way that is both economically meaningful and operationally realistic.

### 5.1 Managerial and Policy Implications

For practitioners, the EAPO framework is best viewed as an overlay technology rather than a wholesale replacement for existing investment processes. Because the emissions operator acts directly on the return kernel, it can be composed with standard constraints (e.g., sector, factor, liquidity) and integrated into existing mean–variance, risk-parity, or factor-model architectures with minimal re-engineering.

From an asset-management perspective, three implications are immediate.
(i) Implementability at scale. The conic reformulations and first-order algorithms in Sections [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") and [4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios") imply that emissions-robust overlays can be deployed on institutional universes (hundreds to thousands of names) under standard end-of-day time budgets. This makes EAPO compatible with large index-plus and enhanced passive mandates, where operational frictions are often the binding constraint.
(ii) Governance via shadow prices. The dual variables associated with the ambiguity sets deliver an internal “shadow carbon tax” that measures the marginal Sharpe reduction per unit tightening of the robustness budget Γ\Gamma. This provides investment committees and risk officers with a quantitative, dollar-denominated knob for calibrating how aggressively to trade off expected return against protection from emissions misreporting, and for documenting those trade-offs to clients and boards.
(iii) Robust reporting of financed emissions. Because the framework explicitly models estimation error in λ\lambda and propagates it into portfolio-level exposures, it yields intensity and “emissions yield” metrics (emissions per unit of excess return) that can be reported alongside traditional performance statistics. This is directly aligned with emerging disclosure regimes under IFRS S2, PCAF, and related climate-reporting standards, and can reduce the probability that portfolios appear green in-sample but fail to decarbonize once misreporting is corrected.

For regulators and benchmark providers, the main implication is methodological: EAPO-type constructions demonstrate that Paris-aligned and climate-transition benchmarks need not rely solely on hard exclusions or ad hoc tilts. Instead, robust, optimization-based designs can internalize both transition pathways and disclosure noise, producing indices and supervisory stress tests that are transparent, reproducible, and less sensitive to idiosyncrasies in vendor data. Finally, for corporate issuers, the framework highlights a concrete channel through which higher-quality emissions disclosure can relax investors’ robustness penalties, lowering perceived risk premia and potentially improving access to capital.

### 5.2 Open Problems and Future Research

Several limitations of the present analysis point to a research agenda at the intersection of finance, optimization, and climate science.

First, our empirical work focuses on Scope 1 emissions in a single large-cap U.S. equity universe. Extending the framework to multi-scope, multi-region settings—including Scope 2 and material Scope 3 categories, as well as financed-emissions metrics for credit and private assets—would allow a more complete mapping between portfolio construction and real-economy decarbonization. Doing so will require both richer data and new modeling for the dependence structure between scopes and across corporate value chains.

Second, the dynamic analysis in Section [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") treats the investor as small relative to the market and abstracts from general-equilibrium feedbacks. As robust, emissions-aware strategies scale, they will affect prices, cost of capital, and firms’ incentives to disclose and abate. Embedding EAPO-style preferences into equilibrium asset-pricing models, and quantifying the induced changes in emissions trajectories, remains a central open problem with direct relevance for sustainable-finance regulation.

Third, while we incorporate transition and disclosure risk through robust drift and intensity terms, we work with relatively standard return-generating processes and linear penalties. A natural extension is to couple EAPO with heavy-tailed or jump processes that better capture physical and transition tail events, as well as with forward-looking scenario sets such as NGFS pathways. This would allow a unified treatment of chronic and acute climate risk within the same robust optimization backbone.

Fourth, our empirical implementation uses a single class of ambiguity sets and a particular choice of curvature parameter mm. Although the sensitivity and Lipschitz results in Sections [2](https://arxiv.org/html/2601.06507v1#S2 "2 Mathematical Model and Data ‣ Emissions-Robust Portfolios") and [4](https://arxiv.org/html/2601.06507v1#S4 "4 Empirical Results ‣ Emissions-Robust Portfolios") show that performance deteriorates sub-linearly as robustness is tightened, a more systematic comparison of alternative divergence measures, ambiguity geometries, and learning rules for Γ\Gamma is warranted. In particular, data-driven updating of robustness budgets—for example, as disclosure quality or verification coverage improves—could make the framework adaptive over the life of a mandate.

Finally, there is an open methodological opportunity on the interface with corporate and operational decision-making. On the real-economy side, firm-level abatement projects, capital-budgeting decisions, and supply-chain redesigns are increasingly evaluated under internal carbon prices and scenario analysis. On the financial side, investors are beginning to use shadow carbon prices and emissions-adjusted discount rates. Developing joint models that couple EAPO-type portfolio optimization with firm-level real-options or capacity-planning problems would move the literature closer to a fully integrated view of climate risk, capital allocation, and operations.

In summary, our results indicate that robust optimization provides a viable and implementable pathway for reconciling the dual imperatives of portfolio performance and climate responsibility. The combination of axiomatic modeling, tractable convex reformulations, and statistically disciplined empirical evidence suggests that emissions-robust portfolio design can be a core tool—rather than an add-on—in the next generation of sustainable investment mandates.

## References

* M. Andersson, P. Bolton, and F. Samama (2016)
  Hedging climate risk.
  Financial Analysts Journal 72 (3),  pp. 13–32.
  External Links: [Document](https://dx.doi.org/10.2469/faj.v72.n3.4)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p2.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* R. J. Balvers (2017)
  Profitability, value, and stock returns in production-based asset pricing without frictions.
  Journal of Money, Credit and Banking 49 (2-3),  pp. 367–398.
  External Links: [Document](https://dx.doi.org/10.1111/jmcb.12354)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p1.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* R. Bansal, D. Kiku, and M. Ochoa (2016)
  Price of long-run temperature shifts in capital markets.
  NBER Working Paper (22529).
  External Links: [Document](https://dx.doi.org/10.3386/w22529),
  [Link](https://www.nber.org/papers/w22529)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* A. Ben-Tal and A. Nemirovski (2001)
  Lectures on modern convex optimization: analysis, algorithms, and engineering applications.
  SIAM.
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p2.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* F. Berg, J. F. Kölbel, and R. Rigobon (2022)
  Aggregate confusion: the divergence of esg ratings.
  Review of Finance 26 (6),  pp. 1315–1344.
  External Links: [Document](https://dx.doi.org/10.1093/rof/rfac033)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p4.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios"),
  [§1](https://arxiv.org/html/2601.06507v1#S1.p3.1 "1 Introduction ‣ Emissions-Robust Portfolios").
* D. Bertsimas and M. Sim (2004)
  The price of robustness.
  Operations Research 52 (1),  pp. 35–53.
  External Links: [Document](https://dx.doi.org/10.1287/opre.1030.0065)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p2.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* P. Bolton, M. Després, L. A. P. da Silva, F. Samama, and R. Svartzman (2020)
  The green swan: central banking and financial stability in the age of climate change.
   Bank for International Settlements, Basel.
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p2.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios"),
  [§1](https://arxiv.org/html/2601.06507v1#S1.p3.1 "1 Introduction ‣ Emissions-Robust Portfolios").
* P. Bolton and M. Kacperczyk (2021)
  Do investors care about carbon risk?.
  Journal of Financial Economics 142 (2),  pp. 517–549.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2021.05.008)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios"),
  [§4.4.1](https://arxiv.org/html/2601.06507v1#S4.SS4.SSS1.p2.1 "4.4.1 Why deep decarbonization can be performance neutral ‣ 4.4 Discussion ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios").
* S. Boyd and L. Vandenberghe (2004)
  Convex optimization.
   Cambridge University Press, Cambridge.
  Cited by: [§2.8](https://arxiv.org/html/2601.06507v1#S2.SS8.1.p1.3 "Proof. ‣ 2.8 Distributionally Robust Extension ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios").
* M. Burke, S. M. Hsiang, and E. Miguel (2015)
  Global non-linear effect of temperature on economic production.
  Nature 527 (7577),  pp. 235–239.
  External Links: [Document](https://dx.doi.org/10.1038/nature15725)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* T. A. Carleton and S. M. Hsiang (2016)
  Social and economic impacts of climate.
  Science 353 (6304),  pp. aad9837.
  External Links: [Document](https://dx.doi.org/10.1126/science.aad9837)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* R. F. Engle, S. Giglio, B. Kelly, H. Lee, and J. Stroebel (2020)
  Hedging climate change news.
  The Review of Financial Studies 33 (3),  pp. 1184–1216.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhz072)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p2.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios"),
  [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* EU Technical Expert Group on Sustainable Finance (2019)
  Final report on climate benchmarks and benchmarks’ esg disclosures.
  Technical report
   European Commission.
  External Links: [Link](https://finance.ec.europa.eu/system/files/2019-09/190930-sustainable-finance-teg-final-report-climate-benchmarks-and-disclosures_en.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p4.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* F. J. Fabozzi, K. C. J. Ma, and B. Oliphant (2008)
  Sin stock returns.
  Journal of Portfolio Management 35 (1),  pp. 82–94.
  External Links: [Document](https://dx.doi.org/10.3905/JPM.2008.35.1.82)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p1.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* G. Friede, T. Busch, and A. Bassen (2015)
  ESG and financial performance: aggregated evidence from more than 2000 empirical studies.
  Journal of Sustainable Finance & Investment 5 (4),  pp. 210–233.
  External Links: [Document](https://dx.doi.org/10.1080/20430795.2015.1118917)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p1.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* P. Friedlingstein et al. (2025)
  Global carbon budget 2024.
  Earth System Science Data 17,  pp. 965–.
  External Links: [Document](https://dx.doi.org/10.5194/essd-17-965-2025),
  [Link](https://essd.copernicus.org/articles/17/965/2025/essd-17-965-2025.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.p2.4 "1 Introduction ‣ Emissions-Robust Portfolios").
* S. Giglio, B. Kelly, and J. Stroebel (2021)
  Climate finance.
  Annual Review of Financial Economics 13,  pp. 15–36.
  External Links: [Document](https://dx.doi.org/10.1146/annurev-financial-102620-103311)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* T. L. Guenedal and T. Roncalli (2021)
  The market measure of carbon risk and its impact on the minimum variance portfolio.
  Journal of Portfolio Management 47 (8),  pp. 102–118.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2021.1.272)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p2.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* S. Hsiang, R. Kopp, A. Jina, et al. (2017)
  Estimating economic damage from climate change in the united states.
  Science 356 (6345),  pp. 1362–1369.
  External Links: [Document](https://dx.doi.org/10.1126/science.aal4369)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* E. Ilhan, Z. Sautner, and G. Vilkov (2021)
  Carbon tail risk.
  The Review of Financial Studies 34 (3),  pp. 1540–1571.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhaa071)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios"),
  [§4.4.1](https://arxiv.org/html/2601.06507v1#S4.SS4.SSS1.p3.1 "4.4.1 Why deep decarbonization can be performance neutral ‣ 4.4 Discussion ‣ 4 Empirical Results ‣ Emissions-Robust Portfolios").
* International Sustainability Standards Board (2023)
  IFRS s2: climate-related disclosures.
  External Links: [Link](https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ifrs-s2-climate-related-disclosures/)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p4.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* IPCC (2023)
  Climate change 2023: synthesis report.
  Technical report
   Intergovernmental Panel on Climate Change.
  Note: Summary for Policymakers and Longer Report
  External Links: [Link](https://www.ipcc.ch/report/ar6/syr/),
  [Document](https://dx.doi.org/10.59327/IPCC/AR6-9789291691647.001)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.p1.6 "1 Introduction ‣ Emissions-Robust Portfolios"),
  [§1](https://arxiv.org/html/2601.06507v1#S1.p2.4 "1 Introduction ‣ Emissions-Robust Portfolios").
* H. Markowitz (1952)
  Portfolio selection.
  Journal of Finance 7 (1),  pp. 77–91.
  External Links: [Document](https://dx.doi.org/10.2307/2975974)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.p3.1 "1 Introduction ‣ Emissions-Robust Portfolios").
* Network for Greening the Financial System (NGFS) (2025)
  NGFS climate scenarios: technical documentation (phase iv).
  Technical report
   Network for Greening the Financial System.
  External Links: [Link](https://www.ngfs.net/system/files/2025-01/NGFS%20Climate%20Scenarios%20Technical%20Documentation.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p4.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* Partnership for Carbon Accounting Financials (2020)
  Global ghg accounting and reporting standard for the financial industry.
  External Links: [Link](https://carbonaccountingfinancials.com/files/downloads/PCAF-Global-GHG-Standard-2020.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p4.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* L. Pastor, R. F. Stambaugh, and L. A. Taylor (2021)
  Sustainable investing in equilibrium.
  Journal of Financial Economics 142 (2),  pp. 550–571.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2021.05.011)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* L. H. Pedersen, S. Fitzgibbons, and L. Pomorski (2021)
  Responsible investing: the esg-efficient frontier.
  Journal of Financial Economics 142 (2),  pp. 572–597.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2021.05.014)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p3.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* L. Renneboog, J. T. Horst, and C. Zhang (2008)
  The price of ethics and stakeholder governance: the performance of socially responsible mutual funds.
  Journal of Corporate Finance 14 (3),  pp. 302–322.
  External Links: [Document](https://dx.doi.org/10.1016/j.jcorpfin.2008.03.009)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p1.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* R. T. Rockafellar and S. Uryasev (2000)
  Optimization of conditional value-at-risk.
  Journal of Risk 2 (3),  pp. 21–41.
  Cited by: [§2.6](https://arxiv.org/html/2601.06507v1#S2.SS6.p1.8 "2.6 Tail–Risk Extension (CVaR) ‣ 2 Mathematical Model and Data ‣ Emissions-Robust Portfolios").
* Task Force on Climate-related Financial Disclosures (2017)
  Recommendations of the tcfd.
  Technical report
   Task Force on Climate-related Financial Disclosures.
  External Links: [Link](https://assets.bbhub.io/company/sites/60/2021/10/FINAL-2017-TCFD-Report.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p4.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* UNFCCC (2015)
  The paris agreement.
  Note: Adopted at COP21, Paris
  External Links: [Link](https://unfccc.int/sites/default/files/english_paris_agreement.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.p2.4 "1 Introduction ‣ Emissions-Robust Portfolios").
* United Nations Environment Programme (2023)
  Emissions gap report 2023: broken record—temperatures hit new highs, yet world fails to cut emissions (again).
  Technical report
   United Nations Environment Programme.
  External Links: [Document](https://dx.doi.org/10.59117/20.500.11822/43922),
  [Link](https://www.unep.org/resources/emissions-gap-report-2023)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.p2.4 "1 Introduction ‣ Emissions-Robust Portfolios").
* G. Weisang and T. Roncalli (2022)
  Portfolio construction with climate risk measures.
  Technical report
  Technical Report 90, Amundi Research Center.
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p2.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").
* WRI and WBCSD (2004)
  The greenhouse gas protocol: a corporate accounting and reporting standard (revised edition).
  External Links: [Link](https://ghgprotocol.org/sites/default/files/standards/ghg-protocol-revised.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.06507v1#S1.SS0.SSS0.Px1.p4.1 "Literature and conceptual foundations. ‣ 1 Introduction ‣ Emissions-Robust Portfolios").

## 6 Appendix

### 6.1 Axioms and uniqueness of the emissions–penalty operator

Fix a scope jj and let λi,j≥0\lambda\_{i,j}\geq 0 denote the emissions intensity of asset ii at the decision date,
with

|  |  |  |
| --- | --- | --- |
|  | λmax,j≡maxi⁡λi,j∈(0,∞).\lambda\_{\max,j}\equiv\max\_{i}\lambda\_{i,j}\in(0,\infty). |  |

For a curvature parameter m∈ℕ+m\in\mathbb{N}\_{+}, an emissions–penalty operator is a mapping

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj(m)\displaystyle P^{(m)}\_{j} | :ℝ×[0,λmax,j]→ℝ,\displaystyle:\,\mathbb{R}\times[0,\lambda\_{\max,j}]\,\to\,\mathbb{R}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (r,λ)\displaystyle(r,\lambda) | ↦“emissions-adjusted” payoff.\displaystyle\mapsto\text{``emissions-adjusted'' payoff}. |  |

The following hold for generator Pj(1)P^{(1)}\_{j}.

##### Axiom (H) — payoff homogeneity.

For all α≥0\alpha\geq 0 and r∈ℝr\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | Pj(1)​(α​r,λ)=α​Pj(1)​(r,λ).P^{(1)}\_{j}(\alpha r,\lambda)=\alpha\,P^{(1)}\_{j}(r,\lambda). |  |

##### Axiom (N) — normalization.

For all r∈ℝr\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | Pj(1)​(r,0)=r,Pj(1)​(r,λmax,j)=0.P^{(1)}\_{j}(r,0)=r,\qquad P^{(1)}\_{j}(r,\lambda\_{\max,j})=0. |  |

##### Axiom (M) — monotonicity in intensity.

If 0≤λ1≤λ2≤λmax,j0\leq\lambda\_{1}\leq\lambda\_{2}\leq\lambda\_{\max,j} and r≥0r\geq 0, then

|  |  |  |
| --- | --- | --- |
|  | Pj(1)​(r,λ1)≥Pj(1)​(r,λ2).P^{(1)}\_{j}(r,\lambda\_{1})\geq P^{(1)}\_{j}(r,\lambda\_{2}). |  |

##### Axiom (SI) — scale invariance of units.

For any β>0\beta>0,

|  |  |  |
| --- | --- | --- |
|  | Pj(1)​(r,λ,λmax,j)=Pj(1)​(r,β​λ,β​λmax,j),P^{(1)}\_{j}(r,\lambda,\lambda\_{\max,j})=P^{(1)}\_{j}(r,\beta\lambda,\beta\lambda\_{\max,j}), |  |

that is, rescaling the emissions unit leaves the transformed payoff unchanged.

##### Axiom (L) — mixture linearity in intensity.

For all θ∈[0,1]\theta\in[0,1] and λ1,λ2∈[0,λmax,j]\lambda\_{1},\lambda\_{2}\in[0,\lambda\_{\max,j}],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj(1)​(r,θ​λ1+(1−θ)​λ2)\displaystyle P^{(1)}\_{j}\!\bigl(r,\theta\lambda\_{1}+(1-\theta)\lambda\_{2}\bigr) | =θ​Pj(1)​(r,λ1)\displaystyle=\theta\,P^{(1)}\_{j}(r,\lambda\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−θ)​Pj(1)​(r,λ2).\displaystyle\quad+(1-\theta)\,P^{(1)}\_{j}(r,\lambda\_{2}). |  |

##### Axiom (C) — curvature semigroup.

There exists a family {Pj(m)}m∈ℕ+\{P^{(m)}\_{j}\}\_{m\in\mathbb{N}\_{+}} with generator Pj(1)P^{(1)}\_{j} such that

|  |  |  |
| --- | --- | --- |
|  | Pj(m1+m2)=Pj(m1)∘Pj(m2),∀m1,m2∈ℕ+.P^{(m\_{1}+m\_{2})}\_{j}=P^{(m\_{1})}\_{j}\circ P^{(m\_{2})}\_{j},\qquad\forall\,m\_{1},m\_{2}\in\mathbb{N}\_{+}. |  |

We additionally assume that Pj(1)P^{(1)}\_{j} is continuous in λ\lambda.

###### Proposition 6.1 (Uniqueness and closed form).

Under axioms (H)–(N)–(M)–(SI)–(L)–(C) and continuity in λ\lambda, the only admissible family
{Pj(m)}m∈ℕ+\{P^{(m)}\_{j}\}\_{m\in\mathbb{N}\_{+}} is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Pj(m)​(r,λ)\displaystyle P^{(m)}\_{j}(r,\lambda) | =(1−λλmax,j)m​r,\displaystyle=\Bigl(1-\frac{\lambda}{\lambda\_{\max,j}}\Bigr)^{m}r, |  | (26) |
|  | (r,λ)\displaystyle(r,\lambda) | ∈ℝ×[0,λmax,j].\displaystyle\in\mathbb{R}\times[0,\lambda\_{\max,j}]. |  |

###### Proof.

We give a fully explicit argument that isolates where each axiom enters.
As a compact summary, payoff homogeneity (H) and unit-scale invariance (SI) imply the existence of a
scalar function φj(1):[0,1]→[0,1]\varphi^{(1)}\_{j}:[0,1]\to[0,1] such that
Pj(1)​(r,λ)=φj(1)​(λ/λmax,j)​rP^{(1)}\_{j}(r,\lambda)=\varphi^{(1)}\_{j}(\lambda/\lambda\_{\max,j})\,r.
The steps below justify this representation and pin down φj(1)\varphi^{(1)}\_{j} uniquely.

Fix r∈ℝr\in\mathbb{R} and define the one-dimensional section

|  |  |  |
| --- | --- | --- |
|  | fr​(x):=Pj(1)​(r,x​λmax,j),x∈[0,1].f\_{r}(x):=P^{(1)}\_{j}\bigl(r,x\,\lambda\_{\max,j}\bigr),\qquad x\in[0,1]. |  |

Unit-scale invariance (SI) implies that the dependence on (λ,λmax,j)(\lambda,\lambda\_{\max,j}) is only through
the ratio x=λ/λmax,jx=\lambda/\lambda\_{\max,j}, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj(1)​(r,λ)=fr​(λλmax,j).P^{(1)}\_{j}(r,\lambda)=f\_{r}\!\Bigl(\frac{\lambda}{\lambda\_{\max,j}}\Bigr). |  | (27) |

By mixture linearity (L), for any x1,x2∈[0,1]x\_{1},x\_{2}\in[0,1] and θ∈[0,1]\theta\in[0,1],

|  |  |  |  |
| --- | --- | --- | --- |
|  | fr​(θ​x1+(1−θ)​x2)\displaystyle f\_{r}\bigl(\theta x\_{1}+(1-\theta)x\_{2}\bigr) | =Pj(1)​(r,(θ​x1+(1−θ)​x2)​λmax,j)\displaystyle=P^{(1)}\_{j}\bigl(r,(\theta x\_{1}+(1-\theta)x\_{2})\lambda\_{\max,j}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =θ​Pj(1)​(r,x1​λmax,j)+(1−θ)​Pj(1)​(r,x2​λmax,j)\displaystyle=\theta\,P^{(1)}\_{j}\bigl(r,x\_{1}\lambda\_{\max,j}\bigr)+(1-\theta)\,P^{(1)}\_{j}\bigl(r,x\_{2}\lambda\_{\max,j}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =θ​fr​(x1)+(1−θ)​fr​(x2).\displaystyle=\theta f\_{r}(x\_{1})+(1-\theta)f\_{r}(x\_{2}). |  |

Thus frf\_{r} satisfies Jensen’s functional equation on the interval [0,1][0,1].
Since Pj(1)P^{(1)}\_{j} is continuous in λ\lambda by assumption, frf\_{r} is continuous in xx.
The standard regularity result for Jensen’s equation on an interval then yields that frf\_{r} is affine.
Concretely, there exist constants a​(r),b​(r)∈ℝa(r),b(r)\in\mathbb{R} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | fr​(x)=a​(r)​x+b​(r),x∈[0,1].f\_{r}(x)=a(r)\,x+b(r),\qquad x\in[0,1]. |  | (28) |

Normalization (N) implies

|  |  |  |
| --- | --- | --- |
|  | fr​(0)=Pj(1)​(r,0)=r,fr​(1)=Pj(1)​(r,λmax,j)=0.f\_{r}(0)=P^{(1)}\_{j}(r,0)=r,\qquad f\_{r}(1)=P^{(1)}\_{j}(r,\lambda\_{\max,j})=0. |  |

Substituting into ([28](https://arxiv.org/html/2601.06507v1#S6.E28 "In Proof. ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios")) gives b​(r)=rb(r)=r and a​(r)=−ra(r)=-r. Therefore

|  |  |  |
| --- | --- | --- |
|  | fr​(x)=r​(1−x),x∈[0,1].f\_{r}(x)=r(1-x),\qquad x\in[0,1]. |  |

Combining with ([27](https://arxiv.org/html/2601.06507v1#S6.E27 "In Proof. ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios")) yields the closed form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj(1)​(r,λ)=(1−λλmax,j)​r,(r,λ)∈ℝ×[0,λmax,j].P^{(1)}\_{j}(r,\lambda)=\Bigl(1-\frac{\lambda}{\lambda\_{\max,j}}\Bigr)\,r,\qquad(r,\lambda)\in\mathbb{R}\times[0,\lambda\_{\max,j}]. |  | (29) |

Define φj(1):[0,1]→[0,1]\varphi^{(1)}\_{j}:[0,1]\to[0,1] by φj(1)​(x):=1−x\varphi^{(1)}\_{j}(x):=1-x. Then ([29](https://arxiv.org/html/2601.06507v1#S6.E29 "In Proof. ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios"))
is equivalently

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj(1)​(r,λ)=φj(1)​(λλmax,j)​r.P^{(1)}\_{j}(r,\lambda)=\varphi^{(1)}\_{j}\!\Big(\frac{\lambda}{\lambda\_{\max,j}}\Big)\,r. |  | (30) |

Payoff homogeneity (H) is consistent with this representation and will be inherited by the full curvature
family.
Normalization (N) implies

|  |  |  |
| --- | --- | --- |
|  | φj(1)​(0)=1,φj(1)​(1)=0,\varphi^{(1)}\_{j}(0)=1,\qquad\varphi^{(1)}\_{j}(1)=0, |  |

and monotonicity (M) guarantees that φj(1)\varphi^{(1)}\_{j} is nonincreasing.

Mixture linearity (L), combined with ([30](https://arxiv.org/html/2601.06507v1#S6.E30 "In Proof. ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios")), gives for all
x1,x2∈[0,1]x\_{1},x\_{2}\in[0,1] and θ∈[0,1]\theta\in[0,1],

|  |  |  |  |
| --- | --- | --- | --- |
|  | φj(1)​(θ​x1+(1−θ)​x2)\displaystyle\varphi^{(1)}\_{j}\!\bigl(\theta x\_{1}+(1-\theta)x\_{2}\bigr) | =θ​φj(1)​(x1)\displaystyle=\theta\,\varphi^{(1)}\_{j}(x\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−θ)​φj(1)​(x2).\displaystyle\quad+(1-\theta)\,\varphi^{(1)}\_{j}(x\_{2}). |  |

This is Jensen’s functional equation on [0,1][0,1]. Under continuity, the only solutions are affine functions.
One way to see this is to first use the midpoint identity
φj(1)​(x+y2)=φj(1)​(x)+φj(1)​(y)2\varphi^{(1)}\_{j}\bigl(\tfrac{x+y}{2}\bigr)=\tfrac{\varphi^{(1)}\_{j}(x)+\varphi^{(1)}\_{j}(y)}{2},
iterate to obtain the identity for all dyadic rationals, extend to all rationals by induction on denominators,
and then use continuity to extend to all real x∈[0,1]x\in[0,1]. Thus there exist aj,bj∈ℝa\_{j},b\_{j}\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | φj(1)​(x)=aj​x+bj,x∈[0,1].\varphi^{(1)}\_{j}(x)=a\_{j}x+b\_{j},\qquad x\in[0,1]. |  |

Using φj(1)​(0)=1\varphi^{(1)}\_{j}(0)=1 and φj(1)​(1)=0\varphi^{(1)}\_{j}(1)=0 gives bj=1b\_{j}=1 and aj=−1a\_{j}=-1, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | φj(1)​(x)\displaystyle\varphi^{(1)}\_{j}(x) | =1−x\displaystyle=1-x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟹Pj(1)​(r,λ)=(1−λλmax,j)​r.\displaystyle\Longrightarrow\quad P^{(1)}\_{j}(r,\lambda)=\Bigl(1-\frac{\lambda}{\lambda\_{\max,j}}\Bigr)r. |  |

Axiom (C) now determines all higher curvatures. For any m∈ℕ+m\in\mathbb{N}\_{+}, the semigroup identity implies

|  |  |  |
| --- | --- | --- |
|  | Pj(m)=Pj(1)∘Pj(1)∘⋯∘Pj(1)⏟m​ compositions,P^{(m)}\_{j}=\underbrace{P^{(1)}\_{j}\circ P^{(1)}\_{j}\circ\cdots\circ P^{(1)}\_{j}}\_{m\text{ compositions}}, |  |

which is proved by a short induction on mm using
Pj(m+1)=Pj(m)∘Pj(1)P^{(m+1)}\_{j}=P^{(m)}\_{j}\circ P^{(1)}\_{j}.
Substituting ([29](https://arxiv.org/html/2601.06507v1#S6.E29 "In Proof. ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios")) into this composition gives

|  |  |  |
| --- | --- | --- |
|  | Pj(m)​(r,λ)=(1−λλmax,j)m​r.P^{(m)}\_{j}(r,\lambda)=\Big(1-\frac{\lambda}{\lambda\_{\max,j}}\Big)^{m}r. |  |

This family clearly satisfies the semigroup relation and inherits the remaining axioms by construction.
Conversely, if another family satisfies (C) with the same generator Pj(1)P^{(1)}\_{j}, the same induction shows
it must coincide with the mm-fold composition above, hence the representation ([26](https://arxiv.org/html/2601.06507v1#S6.E26 "In Proposition 6.1 (Uniqueness and closed form). ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios"))
is unique.
∎

Proposition [6.1](https://arxiv.org/html/2601.06507v1#S6.Thmtheorem1 "Proposition 6.1 (Uniqueness and closed form). ‣ Axiom (C) — curvature semigroup. ‣ 6.1 Axioms and uniqueness of the emissions–penalty operator ‣ 6 Appendix ‣ Emissions-Robust Portfolios") shows that the curvature family used is not an
ad hoc choice: it is the unique continuous, scale-invariant, and mixture-linear way to modulate payoffs by
relative emissions intensity while preserving a semigroup structure over mm.

### 6.2 Dynamic robust Bellman recursion (Proposition 2.2)

For completeness we reproduce the dynamic value function. Let t=0,…,Tt=0,\dots,T index decision dates, and let
β∈(0,1]\beta\in(0,1] denote the discount factor. Given an initial portfolio xt∈Δn−1x\_{t}\in\Delta^{n-1}, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(xt)\displaystyle V\_{t}(x\_{t}) | :=maxxt,…,xT∈Δn−1\displaystyle=\max\_{x\_{t},\dots,x\_{T}\in\Delta^{\,n-1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | minzs∈Zs,s=t,…,T\displaystyle\qquad\min\_{z\_{s}\in Z\_{s},\,s=t,\dots,T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑s=tTβs−t​xs⊤​(γs+Δs​zs).\displaystyle\qquad\sum\_{s=t}^{T}\beta^{\,s-t}\,x\_{s}^{\top}\bigl(\gamma\_{s}+\Delta\_{s}z\_{s}\bigr). |  |

with VT+1​(⋅)≡0V\_{T+1}(\cdot)\equiv 0.

##### Remark (well-posedness and time consistency).

The display above follows the notation in the main text and writes Vt​(xt)V\_{t}(x\_{t}) while also maximizing
over xtx\_{t}. One may interpret VtV\_{t} as the pre-decision value at time tt, in which case the argument
xtx\_{t} is only a mnemonic for the time-tt control. Alternatively, one can define a post-decision value
V~t​(x¯t)\widetilde{V}\_{t}(\bar{x}\_{t}) that conditions on a pre-existing holding x¯t\bar{x}\_{t} and includes transaction
costs or turnover constraints in the transition. In either convention, the Bellman recursion below is
valid under the standard rectangularity condition that the uncertainty set factorizes as a Cartesian
product Zt×Zt+1×⋯×ZTZ\_{t}\times Z\_{t+1}\times\cdots\times Z\_{T}, as written in the inner minimization.

###### Proof.

We proceed by backward induction on tt.

##### Base case t=Tt=T.

At the terminal date t=Tt=T we have

|  |  |  |
| --- | --- | --- |
|  | VT​(xT)=maxxT∈Δn−1⁡minzT∈ZT⁡xT⊤​(γT+ΔT​zT),V\_{T}(x\_{T})=\max\_{x\_{T}\in\Delta^{n-1}}\min\_{z\_{T}\in Z\_{T}}x\_{T}^{\top}(\gamma\_{T}+\Delta\_{T}z\_{T}), |  |

which matches the Bellman form with VT+1≡0V\_{T+1}\equiv 0.

##### Induction step.

Assume now that the recursion holds at t+1t+1. Starting from date tt, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt+1​(xt+1)\displaystyle V\_{t+1}(x\_{t+1}) | =maxxt+1,…,xT∈Δn−1⁡minzt+1:T∈Zt+1:T\displaystyle=\max\_{x\_{t+1},\dots,x\_{T}\in\Delta^{\,n-1}}\min\_{z\_{t+1:T}\in Z\_{t+1:T}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑s=t+1Tβs−(t+1)​xs⊤​(γs+Δs​zs).\displaystyle\qquad\sum\_{s=t+1}^{T}\beta^{\,s-(t+1)}\,x\_{s}^{\top}(\gamma\_{s}+\Delta\_{s}z\_{s}). |  |

Because the uncertainty is rectangular, the inner minimization over zt,…,zTz\_{t},\dots,z\_{T} can be written as
an iterated minimization. For any fixed control sequence {xs}s=tT\{x\_{s}\}\_{s=t}^{T}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | minzs∈Zs,s=t,…,T​∑s=tTβs−t​xs⊤​(γs+Δs​zs)\displaystyle\min\_{z\_{s}\in Z\_{s},\,s=t,\dots,T}\sum\_{s=t}^{T}\beta^{s-t}x\_{s}^{\top}(\gamma\_{s}+\Delta\_{s}z\_{s}) | =minzt∈Zt{xt⊤(γt+Δtzt)\displaystyle=\min\_{z\_{t}\in Z\_{t}}\Bigl\{x\_{t}^{\top}(\gamma\_{t}+\Delta\_{t}z\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +βminzt+1:T∈Zt+1:T∑s=t+1Tβs−(t+1)xs⊤(γs+Δszs)}.\displaystyle\qquad+\beta\,\min\_{z\_{t+1:T}\in Z\_{t+1:T}}\sum\_{s=t+1}^{T}\beta^{s-(t+1)}x\_{s}^{\top}(\gamma\_{s}+\Delta\_{s}z\_{s})\Bigr\}. |  |

This step is purely algebraic and uses that ztz\_{t} appears only in the period-tt term.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt​(xt)\displaystyle V\_{t}(x\_{t}) | =maxxt∈Δn−1minzt∈Zt{xt⊤(γt+Δtzt)\displaystyle=\max\_{x\_{t}\in\Delta^{\,n-1}}\min\_{z\_{t}\in Z\_{t}}\Bigl\{x\_{t}^{\top}(\gamma\_{t}+\Delta\_{t}z\_{t}) |  | (31) |
|  |  | +β​maxxt+1,…,xT∈Δn−1⁡minzt+1:T∈Zt+1:T\displaystyle\qquad+\beta\max\_{x\_{t+1},\dots,x\_{T}\in\Delta^{\,n-1}}\min\_{z\_{t+1:T}\in Z\_{t+1:T}} |  |
|  |  | ∑s=t+1Tβs−(t+1)xs⊤(γs+Δszs)}.\displaystyle\qquad\sum\_{s=t+1}^{T}\beta^{\,s-(t+1)}x\_{s}^{\top}(\gamma\_{s}+\Delta\_{s}z\_{s})\Bigr\}. |  |

The term in braces depends on the future controls only through xt+1x\_{t+1}, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(xt)\displaystyle V\_{t}(x\_{t}) | =maxxt∈Δn−1minzt∈Zt{xt⊤(γt+Δtzt)\displaystyle=\max\_{x\_{t}\in\Delta^{\,n-1}}\min\_{z\_{t}\in Z\_{t}}\Bigl\{x\_{t}^{\top}(\gamma\_{t}+\Delta\_{t}z\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +βVt+1(xt+1)}.\displaystyle\qquad+\beta\,V\_{t+1}(x\_{t+1})\Bigr\}. |  |

Compactness of ZtZ\_{t} and continuity of z↦xt⊤​(γt+Δt​z)z\mapsto x\_{t}^{\top}(\gamma\_{t}+\Delta\_{t}z) ensure existence of a
minimizer zt⋆​(xt)z\_{t}^{\star}(x\_{t}) for each feasible xtx\_{t}. Concavity of the outer maximization over the simplex
follows from linearity of the stage payoff in xtx\_{t}. This completes the backward recursion.
∎

### 6.3 φ\varphi–divergence dual reformulation (Theorem 2.2)

Consider the distributionally robust problem

|  |  |  |
| --- | --- | --- |
|  | maxx∈Δn−1​infP∈𝒫𝔼z∼P​[ℓx​(z)],\displaystyle\max\_{x\in\Delta^{\,n-1}}\,\inf\_{P\in\mathcal{P}}\,\mathbb{E}\_{z\sim P}\bigl[\ell\_{x}(z)\bigr], |  |
|  |  |  |
| --- | --- | --- |
|  | ℓx​(z):=∑i=1nxi​(γi+δi​z).\displaystyle\ell\_{x}(z)=\sum\_{i=1}^{n}x\_{i}\bigl(\gamma\_{i}+\delta\_{i}z\bigr). |  |

with ambiguity set

|  |  |  |
| --- | --- | --- |
|  | 𝒫:={P:Dφ​(P∥P^)≤θ},\mathcal{P}:=\big\{P:D\_{\varphi}(P\,\|\,\widehat{P})\leq\theta\big\}, |  |

where DφD\_{\varphi} is a φ\varphi–divergence centered at the empirical law P^\widehat{P}. For clarity, suppose P^\widehat{P} is discrete with support {z(m)}m=1M\{z^{(m)}\}\_{m=1}^{M} and probabilities p^m>0\hat{p}\_{m}>0. Any P≪P^P\ll\widehat{P} admits a Radon–Nikodym density w=d​Pd​P^w=\frac{dP}{d\widehat{P}}
satisfying w​(z(m))≥0w(z^{(m)})\geq 0 and ∑mw​(z(m))​p^m=1\sum\_{m}w(z^{(m)})\hat{p}\_{m}=1. The robust inner problem can then be
written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | infw\displaystyle\inf\_{w} | ∑m=1Mℓx​(z(m))​wm​p^m\displaystyle\sum\_{m=1}^{M}\ell\_{x}\bigl(z^{(m)}\bigr)\,w\_{m}\hat{p}\_{m} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | ∑m=1Mφ​(wm)​p^m≤θ,\displaystyle\sum\_{m=1}^{M}\varphi(w\_{m})\,\hat{p}\_{m}\,\leq\,\theta, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑m=1Mwm​p^m= 1,\displaystyle\sum\_{m=1}^{M}w\_{m}\hat{p}\_{m}\,=1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | wm≥0,m=1,…,M.\displaystyle w\_{m}\geq 0,\quad m=1,\dots,M. |  |

###### Proof.

The feasible set is nonempty since wm≡1w\_{m}\equiv 1 satisfies ∑mwm​p^m=1\sum\_{m}w\_{m}\hat{p}\_{m}=1 and
∑mφ​(1)​p^m=φ​(1)\sum\_{m}\varphi(1)\hat{p}\_{m}=\varphi(1). For standard φ\varphi–divergences one has φ​(1)=0\varphi(1)=0, hence
for any θ>0\theta>0 this choice is strictly feasible for the divergence inequality. This Slater point
ensures strong duality for the convex program in ww.

Introduce Lagrange multipliers λ≥0\lambda\geq 0 for the divergence constraint and ν∈ℝ\nu\in\mathbb{R} for the
normalization constraint. The Lagrangian of the inner problem is

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(w,λ,ν)\displaystyle L(w,\lambda,\nu) | =∑m=1Mℓx​(z(m))​wm​p^m\displaystyle=\sum\_{m=1}^{M}\ell\_{x}\bigl(z^{(m)}\bigr)\,w\_{m}\hat{p}\_{m} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​(∑m=1Mφ​(wm)​p^m−θ)\displaystyle\quad+\,\lambda\Bigl(\sum\_{m=1}^{M}\varphi(w\_{m})\,\hat{p}\_{m}-\theta\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ν​(∑m=1Mwm​p^m−1).\displaystyle\quad+\,\nu\Bigl(\sum\_{m=1}^{M}w\_{m}\hat{p}\_{m}-1\Bigr). |  |

Rearranging terms yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(w,λ,ν)\displaystyle L(w,\lambda,\nu) | =−θ​λ−ν\displaystyle=-\theta\,\lambda-\nu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑m=1Mp^m[ℓx(z(m))wm\displaystyle\qquad+\sum\_{m=1}^{M}\hat{p}\_{m}\Bigl[\ell\_{x}\bigl(z^{(m)}\bigr)\,w\_{m} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​φ​(wm)\displaystyle\qquad\qquad\qquad+\lambda\,\varphi(w\_{m}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +νwm].\displaystyle\qquad\qquad\qquad+\nu\,w\_{m}\Bigr]. |  |

Because the constraints are separable across mm, the Lagrangian decouples across the coordinates
wmw\_{m}. Write the coefficient on wmw\_{m} as cm:=ℓx​(z(m))+νc\_{m}:=\ell\_{x}\bigl(z^{(m)}\bigr)+\nu. For fixed (λ,ν)(\lambda,\nu)
we therefore need the scalar infimum

|  |  |  |
| --- | --- | --- |
|  | infu≥0{cm​u+λ​φ​(u)}.\inf\_{u\geq 0}\{c\_{m}u+\lambda\varphi(u)\}. |  |

Recall the convex conjugate φ⋆​(y):=supu≥0{u​y−φ​(u)}\varphi^{\star}(y):=\sup\_{u\geq 0}\{uy-\varphi(u)\}. A standard identity
then gives

|  |  |  |
| --- | --- | --- |
|  | infu≥0{φ​(u)+y​u}=−φ⋆​(−y).\inf\_{u\geq 0}\{\varphi(u)+yu\}=-\varphi^{\star}(-y). |  |

Applying this with y=cm/λy=c\_{m}/\lambda when λ>0\lambda>0 yields the claimed expression. To match the more
common DRO parametrization in which the shift variable appears with the sign (ℓ−ν)/λ(\ell-\nu)/\lambda,
one may equivalently substitute ν←−ν\nu\leftarrow-\nu at the end of the derivation.

For fixed (λ,ν)(\lambda,\nu), the pointwise infimum over wm≥0w\_{m}\geq 0 is governed by the convex conjugate
φ⋆\varphi^{\star}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | infwm≥0\displaystyle\inf\_{w\_{m}\geq 0} | {ℓx​(z(m))​wm+λ​φ​(wm)+ν​wm}\displaystyle\bigl\{\ell\_{x}\bigl(z^{(m)}\bigr)\,w\_{m}+\lambda\varphi(w\_{m})+\nu w\_{m}\bigr\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−λ​φ⋆​(ℓx​(z(m))−νλ).\displaystyle=-\lambda\,\varphi^{\star}\!\Bigl(\frac{\ell\_{x}\bigl(z^{(m)}\bigr)-\nu}{\lambda}\Bigr). |  |

with the convention that λ​φ⋆​(⋅)\lambda\varphi^{\star}(\cdot) is +∞+\infty when λ=0\lambda=0 and the argument lies
outside the effective domain. Substituting back,

|  |  |  |  |
| --- | --- | --- | --- |
|  | infwL​(w,λ,ν)\displaystyle\inf\_{w}L(w,\lambda,\nu) | =ν−θ​λ\displaystyle=\nu-\theta\,\lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −λ​∑m=1Mp^m​φ⋆​(ℓx​(z(m))−νλ).\displaystyle\qquad-\lambda\sum\_{m=1}^{M}\hat{p}\_{m}\,\varphi^{\star}\!\Bigl(\frac{\ell\_{x}(z^{(m)})-\nu}{\lambda}\Bigr). |  |

Taking the supremum over (λ,ν)(\lambda,\nu) produces the dual representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | infP∈𝒫𝔼P​[ℓx​(z)]\displaystyle\inf\_{P\in\mathcal{P}}\mathbb{E}\_{P}[\ell\_{x}(z)] | =supλ≥0,ν∈ℝ{ν\displaystyle=\sup\_{\lambda\geq 0,\,\nu\in\mathbb{R}}\Biggl\{\nu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​λ\displaystyle\qquad-\theta\,\lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −λ∑m=1Mp^mφ⋆(ℓx​(z(m))−νλ)}.\displaystyle\qquad-\lambda\sum\_{m=1}^{M}\hat{p}\_{m}\,\varphi^{\star}\!\Bigl(\frac{\ell\_{x}(z^{(m)})-\nu}{\lambda}\Bigr)\Biggr\}. |  |

Strong duality holds under standard regularity conditions (e.g., Slater’s condition for the primal), so the
robust problem is equivalent to maximizing this dual objective over x∈Δn−1x\in\Delta^{n-1}. This is precisely
the scalar dual formulation stated.
∎

### 6.4 Continuous φ\varphi–DRO reformulation

The preceding argument extends verbatim beyond a discrete empirical support. For a general ambiguity set

|  |  |  |
| --- | --- | --- |
|  | 𝒫={P:Dφ​(P∥P^)≤θ}\mathcal{P}=\big\{P:D\_{\varphi}(P\,\|\,\widehat{P})\leq\theta\big\} |  |

and linear loss ℓx\ell\_{x}, Fenchel duality yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supx∈Δn−1infP∈𝒫𝔼P​[ℓx​(z)]\displaystyle\sup\_{x\in\Delta^{\,n-1}}\inf\_{P\in\mathcal{P}}\mathbb{E}\_{P}[\ell\_{x}(z)] | =supx∈Δn−1supλ≥0,ν∈ℝ{ν\displaystyle=\sup\_{x\in\Delta^{\,n-1}}\sup\_{\lambda\geq 0,\,\nu\in\mathbb{R}}\Biggl\{\nu |  | (32) |
|  |  | −θ​λ\displaystyle\qquad-\theta\,\lambda |  |
|  |  | −λ𝔼P^[φ⋆(ℓx​(z)−νλ)]}.\displaystyle\qquad-\lambda\,\mathbb{E}\_{\widehat{P}}\Bigl[\varphi^{\star}\!\Bigl(\tfrac{\ell\_{x}(z)-\nu}{\lambda}\Bigr)\Bigr]\Biggr\}. |  |

The distributional uncertainty enters only through the scalar pair (λ,ν)(\lambda,\nu) and the expectation of
φ⋆\varphi^{\star}, so the robustification adds two decision variables and a one-dimensional nonlinearity
independently of the dimension of zz.

### 6.5 Convexity of the return–emissions Pareto frontier (Proposition 2.3)

Consider the scalarized problem

|  |  |  |
| --- | --- | --- |
|  | maxx∈Δn−1⁡Fμ​(x):=x⊤​r−μ​x⊤​λ,μ≥0,\max\_{x\in\Delta^{n-1}}F\_{\mu}(x):=x^{\top}r-\mu\,x^{\top}\lambda,\qquad\mu\geq 0, |  |

and denote the optimal value by

|  |  |  |
| --- | --- | --- |
|  | g​(μ):=maxx∈Δn−1⁡Fμ​(x).g(\mu):=\max\_{x\in\Delta^{n-1}}F\_{\mu}(x). |  |

The attainable set of pairs (x⊤​r,x⊤​λ)(x^{\top}r,x^{\top}\lambda) over x∈Δn−1x\in\Delta^{n-1} forms a compact convex
polytope.

###### Proof.

For each fixed xx, Fμ​(x)F\_{\mu}(x) is affine in μ\mu, hence g​(μ)g(\mu) is a pointwise supremum of affine
functions and therefore convex and continuous on [0,∞)[0,\infty). The attainable set
S:={(x⊤​r,x⊤​λ):x∈Δn−1}S:=\{(x^{\top}r,x^{\top}\lambda):x\in\Delta^{n-1}\} is the image of a simplex under an affine map, so it is
compact and convex.

Each μ≥0\mu\geq 0 defines a supporting hyperplane with normal vector (1,μ)(1,\mu), and g​(μ)g(\mu) is the associated
support function evaluated at that normal direction. Therefore any optimizer x⋆​(μ)x^{\star}(\mu) attains a
supported efficient point on the boundary of SS. Since SS is a polytope in finite dimension, every
efficient extreme point is supported, hence varying μ\mu recovers the full efficient frontier up to
degeneracies that correspond to boundary segments.

When the maximizer x⋆​(μ)x^{\star}(\mu) is unique for a given μ\mu, Danskin’s theorem yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​μ​g​(μ)\displaystyle\frac{d}{d\mu}g(\mu) | =∂∂μ​(x⋆​(μ)⊤​r−μ​x⋆​(μ)⊤​λ)\displaystyle=\frac{\partial}{\partial\mu}\Bigl(x^{\star}(\mu)^{\!\top}r-\mu\,x^{\star}(\mu)^{\!\top}\lambda\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−x⋆​(μ)⊤​λ.\displaystyle=-\,x^{\star}(\mu)^{\!\top}\lambda. |  |

Thus the marginal slope of the efficient frontier with respect to the scalarization weight μ\mu is

|  |  |  |
| --- | --- | --- |
|  | dd​μ​𝔼​[x⋆​(μ)⊤​r]=−𝔼​[x⋆​(μ)⊤​λ],\frac{d}{d\mu}\,\mathbb{E}[x^{\star}(\mu)^{\top}r]=-\,\mathbb{E}[x^{\star}(\mu)^{\top}\lambda], |  |

The rate at which expected return declines when the investor
tightens the penalty on emissions equals minus the current portfolio intensity. If the maximizer is not
unique, any x⋆​(μ)x^{\star}(\mu) in the argmax set gives a valid subgradient, and the same interpretation applies
at the level of subdifferentials.
∎

### 6.6 Lipschitz sensitivity in the robustness budget (Theorem 2.3)

Recall the robust value function

|  |  |  |
| --- | --- | --- |
|  | R⋆​(Γ):=maxx∈Δn−1⁡min∥z∥≤Γ⁡x⊤​(γ+Δ​z),R^{\star}(\Gamma):=\max\_{x\in\Delta^{n-1}}\,\min\_{\lVert z\rVert\leq\Gamma}x^{\top}\big(\gamma+\Delta z\big), |  |

where ∥⋅∥\lVert\cdot\rVert is a norm on the disturbance space and Γ>0\Gamma>0 is the robustness radius. Let
∥⋅∥∗\lVert\cdot\rVert\_{\ast} denote the associated dual norm. Assume that each component return
ri​(z):=γi+δi​zr\_{i}(z):=\gamma\_{i}+\delta\_{i}z is LL–Lipschitz in zz with respect to ∥⋅∥\lVert\cdot\rVert, so that

|  |  |  |
| --- | --- | --- |
|  | |ri​(z1)−ri​(z2)|≤L​∥z1−z2∥,∀z1,z2.\big|r\_{i}(z\_{1})-r\_{i}(z\_{2})\big|\leq L\,\lVert z\_{1}-z\_{2}\rVert,\qquad\forall\,z\_{1},z\_{2}. |  |

###### Proof.

Fix 0<Γ1<Γ20<\Gamma\_{1}<\Gamma\_{2} and let x2⋆x\_{2}^{\star} and z2⋆z\_{2}^{\star} be primal and worst-case disturbance
solutions at robustness Γ2\Gamma\_{2}:

|  |  |  |
| --- | --- | --- |
|  | R⋆​(Γ2)=x2⋆⊤​(γ+Δ​z2⋆),∥z2⋆∥≤Γ2.R^{\star}(\Gamma\_{2})=x\_{2}^{\star\top}\big(\gamma+\Delta z\_{2}^{\star}\big),\qquad\lVert z\_{2}^{\star}\rVert\leq\Gamma\_{2}. |  |

Define the radial projection of z2⋆z\_{2}^{\star} onto the smaller ball of radius Γ1\Gamma\_{1}:

|  |  |  |
| --- | --- | --- |
|  | zπ:={Γ1Γ2​z2⋆,z2⋆≠0,0,z2⋆=0.z\_{\pi}:=\begin{cases}\dfrac{\Gamma\_{1}}{\Gamma\_{2}}z\_{2}^{\star},&z\_{2}^{\star}\neq 0,\\[3.22916pt] 0,&z\_{2}^{\star}=0.\end{cases} |  |

Then ∥zπ∥≤Γ1\lVert z\_{\pi}\rVert\leq\Gamma\_{1} and

|  |  |  |
| --- | --- | --- |
|  | ∥z2⋆−zπ∥≤Γ2−Γ1.\lVert z\_{2}^{\star}-z\_{\pi}\rVert\leq\Gamma\_{2}-\Gamma\_{1}. |  |

##### Justification of the radius bound.

The inequality follows from positive homogeneity of norms. When z2⋆≠0z\_{2}^{\star}\neq 0,

|  |  |  |
| --- | --- | --- |
|  | ∥z2⋆−zπ∥=‖(1−Γ1Γ2)​z2⋆‖=(1−Γ1Γ2)​∥z2⋆∥≤(1−Γ1Γ2)​Γ2=Γ2−Γ1.\lVert z\_{2}^{\star}-z\_{\pi}\rVert=\Bigl\lVert\Bigl(1-\frac{\Gamma\_{1}}{\Gamma\_{2}}\Bigr)z\_{2}^{\star}\Bigr\rVert=\Bigl(1-\frac{\Gamma\_{1}}{\Gamma\_{2}}\Bigr)\lVert z\_{2}^{\star}\rVert\leq\Bigl(1-\frac{\Gamma\_{1}}{\Gamma\_{2}}\Bigr)\Gamma\_{2}=\Gamma\_{2}-\Gamma\_{1}. |  |

The case z2⋆=0z\_{2}^{\star}=0 is immediate.

By feasibility,

|  |  |  |
| --- | --- | --- |
|  | R⋆​(Γ1)≥x2⋆⊤​(γ+Δ​zπ).R^{\star}(\Gamma\_{1})\,\geq\,x\_{2}^{\star\top}\big(\gamma+\Delta z\_{\pi}\big). |  |

Using the Lipschitz property of each rir\_{i} and the fact that x2⋆∈Δn−1x\_{2}^{\star}\in\Delta^{n-1},

|  |  |  |  |
| --- | --- | --- | --- |
|  | x2⋆⊤​(γ+Δ​zπ)\displaystyle x\_{2}^{\star\top}\big(\gamma+\Delta z\_{\pi}\big) | ≥x2⋆⊤​(γ+Δ​z2⋆)−L​∥z2⋆−zπ∥\displaystyle\geq x\_{2}^{\star\top}\big(\gamma+\Delta z\_{2}^{\star}\big)-L\,\lVert z\_{2}^{\star}-z\_{\pi}\rVert |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥R⋆​(Γ2)−L​(Γ2−Γ1).\displaystyle\geq R^{\star}(\Gamma\_{2})-L(\Gamma\_{2}-\Gamma\_{1}). |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | R⋆​(Γ1)−R⋆​(Γ2)≥−L​(Γ2−Γ1).R^{\star}(\Gamma\_{1})-R^{\star}(\Gamma\_{2})\geq-L(\Gamma\_{2}-\Gamma\_{1}). |  |

Interchanging the roles of Γ1\Gamma\_{1} and Γ2\Gamma\_{2} yields the reverse inequality, so we obtain the
two-sided bound

|  |  |  |
| --- | --- | --- |
|  | |R⋆​(Γ1)−R⋆​(Γ2)|≤L​|Γ2−Γ1|.\big|R^{\star}(\Gamma\_{1})-R^{\star}(\Gamma\_{2})\big|\leq L\,|\Gamma\_{2}-\Gamma\_{1}|. |  |

This is the Lipschitz continuity claim in the robustness budget.
∎

### 6.7 Supplementary tables and figures

This subsection collects numerical summaries and graphics referenced in the empirical section.

Table 4: Block bootstrap inference for the Sharpe ratio difference between EAPO and the equal-weight benchmark. The bootstrap resamples paired daily returns in blocks of length 20 trading days to preserve short-range dependence.

|  |  |
| --- | --- |
| Statistic | Value |
| Sharpe(EAPO) | 0.762 |
| Sharpe(EW) | 0.766 |
| Difference (EAPO minus EW) | -0.003 |
| 95% CI (2.5th, 97.5th) | [ -0.163, 0.148 ] |
| Bootstrap replications | 2000 |
| Block length (trading days) | 20 |




Table 5: Average portfolio exposures to simple price-based characteristics, computed at monthly rebalance dates. Volatility is the weighted-average stock-level daily volatility over the trailing 252 trading days. Momentum is the weighted-average 12–1 momentum, measured as the cumulative return from t−252t-252 to t−21t-21 trading days.

| Strategy | Avg. stock vol. (% per day) | Avg. 12–1 momentum (%) |
| --- | --- | --- |
| EW | 1.996 | 15.407 |
| GMV | 1.600 | 13.946 |
| EMW | 2.059 | 17.193 |
| EAPO | 1.844 | 10.730 |




Table 6: Average 95% ellipsoidal uncertainty set statistics by calendar year. “Axis 1” and
“Axis 2” report the semi-axis lengths of the average covariance ellipse for firm-level emissions
intensities, “Area” is the corresponding ellipse area. Larger areas indicate more dispersion in
estimated intensities, and hence greater disclosure uncertainty in that year.

| Year | Axis 1 | Axis 2 | Area |
| --- | --- | --- | --- |
| 2010 | 0.268 | 0.072 | 0.061 |
| 2011 | 0.281 | 0.082 | 0.074 |
| 2012 | 0.301 | 0.085 | 0.082 |
| 2013 | 0.184 | 0.070 | 0.041 |
| 2014 | 0.167 | 0.058 | 0.031 |
| 2015 | 0.207 | 0.063 | 0.042 |
| 2016 | 0.219 | 0.081 | 0.055 |
| 2017 | 0.136 | 0.083 | 0.035 |
| 2018 | 0.212 | 0.084 | 0.056 |
| 2019 | 0.275 | 0.085 | 0.077 |
| 2020 | 0.475 | 0.158 | 0.236 |
| 2021 | 0.214 | 0.135 | 0.091 |
| 2022 | 0.310 | 0.116 | 0.113 |
| 2023 | 0.197 | 0.110 | 0.068 |
| 2024 | 0.164 | 0.107 | 0.055 |




Table 7: Top holdings in the baseline EAPO portfolio. “Avg weight” reports the mean portfolio
weight at monthly rebalancing dates over the sample. “Avg Scope-1 intensity” reports the
corresponding time-average of firm-level Scope-1 emissions intensity measured in tCO2e per
$mm of revenue. The full monthly weight panels for all strategies are provided as CSV exports in
the supplementary replication files.

| Ticker | Avg weight (%) | Avg Scope-1 intensity |
| --- | --- | --- |
| FLS | 1.73 | 5.22 |
| PCAR | 1.73 | 5.52 |
| BIIB | 1.73 | 5.55 |
| MCD | 1.72 | 6.40 |
| HBAN | 1.71 | 5.02 |
| HAS | 1.71 | 6.25 |
| ED | 1.70 | 11.82 |
| EXPD | 1.70 | 5.16 |
| CAH | 1.68 | 5.17 |
| TROW | 1.67 | 4.94 |
| BMY | 1.67 | 6.17 |
| CINF | 1.67 | 6.10 |
| UPS | 1.66 | 9.45 |
| DOV | 1.65 | 10.83 |
| JNJ | 1.65 | 5.50 |

![Refer to caption](figures/R2_eapo_top_holdings_heatmap.png)


Figure 9: Heatmap of monthly portfolio weights for the top holdings in the baseline EAPO portfolio.
Each row corresponds to a ticker and each column to a monthly rebalance date. The plot highlights
that the emissions reductions are achieved through a diversified set of persistent positions rather
than through episodic concentration in a small set of names.