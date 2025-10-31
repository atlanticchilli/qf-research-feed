---
authors:
- Jorge A. Arroyo
doc_id: arxiv:2510.25782v1
family_id: arxiv:2510.25782
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan
url_abs: http://arxiv.org/abs/2510.25782v1
url_html: https://arxiv.org/html/2510.25782v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jorge A. Arroyo
  
Independent Researcher
  
[arroyo.jorgeantonio@gmail.com](mailto:arroyo.jorgeantonio@gmail.com)

(October 2025)

###### Abstract

I evaluate San Juan, Puerto Rico’s late-night alcohol sales ordinance using a multi-outcome synthetic control that pools economic and public-safety series. I show that a common-weight estimator clarifies mechanisms under low-rank outcome structure. I find economically meaningful reallocations in targeted sectors—restaurants and bars, gasoline and convenience, and hospitality employment—while late-night public disorder arrests and violent crime show no clear departures from pre-policy trends. The short post-policy window and small donor pool limit statistical power; joint conformal and permutation tests do not reject the null at conventional thresholds. I therefore emphasize effect magnitudes, temporal persistence, and pre-trend fit over formal significance. Code and diagnostics are available for replication.

## 1 Introduction

Policies that touch nightlife, public safety, and local commerce often operate through several channels at once. When outcomes span domains, applying synthetic control separately to each series can overfit idiosyncratic noise and yield counterfactuals that tell inconsistent stories (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). I implement and evaluate the multi-outcome synthetic control (MOSC) framework of Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34))—a common-weights approach that estimates a single donor-weight vector across outcomes via concatenated or average objectives—showing that common weights improve interpretability and, when outcomes share an underlying factor structure, deliver more reliable counterfactuals than outcome-specific fits. Using both theory and an empirical application to a municipal nightlife regulation, I demonstrate that common weights reveal cross-domain patterns that outcome-specific fits may obscure.

I study San Juan, Puerto Rico’s Public Order Code enacted on November 9, 2023, which restricts late-night alcohol sales with limited exemptions (Section [5.1.1](https://arxiv.org/html/2510.25782v1#S5.SS1.SSS1 "5.1.1 Policy Context ‣ 5.1 Background and Context ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).111Ordinance No. 3 (Series 2023–2024) was approved on August 4, 2023; per §13 (with the publication requirement in §12), the operational provisions—including Article 2.101—became effective 90 days after publication (Municipio Autónomo de San Juan, Legislatura
Municipal, [2023](https://arxiv.org/html/2510.25782v1#bib.bib29)). I therefore treat 2023Q4 as the first (partially exposed) post period, and I use a quarter-end cutoff solely for aggregation. The Code was defended as balancing nightlife with safety and tranquility and later withstood a federal challenge under rational-basis review, where the court noted that “a legislative choice … may be based on rational speculation unsupported by evidence or empirical data” (Asociación de Empresarios Calle Loíza,
Inc., et al. v. Municipality of San
Juan, [2024](https://arxiv.org/html/2510.25782v1#bib.bib9)). Its implementation followed a May 6, 2023 incident in which two tourists were fatally shot on Loíza Street, prompting what critics described as a business-restriction response rather than direct law-enforcement measures (Asociación de Empresarios Calle Loíza,
Inc., et al. v. Municipality of San Juan, [2023](https://arxiv.org/html/2510.25782v1#bib.bib8)). My study provides the systematic evidence that judicial review does not require, while acknowledging short-run data and small-NN limitations that preclude definitive causal claims.

### Contributions

I contribute to policy evaluation methodology and practice in four ways:

* •

  Method to practice. I bring common-weight MOSC into a realistic policy setting and show that, when outcomes share low-rank structure, common weights improve interpretability and reduce bias relative to separate fits; I also use diagnostics to assess the shared-factor assumption (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).
* •

  Diagnostics. I operationalize scree-based rank checks (Figure [1](https://arxiv.org/html/2510.25782v1#S5.F1 "Figure 1 ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), leave-one-outcome-out validation (Appendix Table [A6](https://arxiv.org/html/2510.25782v1#A3.T6 "Table A6 ‣ C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), and pre-treatment fit comparisons (Figure [2](https://arxiv.org/html/2510.25782v1#S5.F2 "Figure 2 ‣ Pre-treatment fit concern: Sector 18 revenue. ‣ 5.3.1 Pre-Treatment Fit Validation ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) to assess the plausibility of shared factors.
* •

  Empirical pattern. I document economically meaningful short-run changes in targeted sectors alongside near-zero effects on crime outcomes—a divergence only visible in a multi-outcome design (Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).
* •

  Applied implementation. Following MOSC (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)), I package a common-weight implementation for a real policy setting with end-to-end code, diagnostics, and a data guide to enable replication and reuse.

I emphasize uncertainty. With six donors, unit-placebo inference alone yields a minimum attainable pp-value of 1/(6+1)≈0.1431/(6{+}1)\approx 0.143. I augment with seven in-time placebos (treating pre-treatment periods as hypothetical intervention dates), yielding 14 total observations for the randomization distribution: 13 placebos (6 donor-unit placebos + 7 in-time placebos) plus the treated unit. This configuration yields a minimum attainable permutation pp-value of 1/14≈0.0711/14\approx 0.071, and I complement permutation tests with joint conformal procedures. Substantive conclusions are therefore suggestive and contingent on the short post-period (six quarters) and small donor pool.

Evaluating this ordinance illustrates the challenges that motivate MOSC. The policy may affect multiple interconnected domains—sectoral revenues, employment, and late-night public disorder—requiring joint analysis. San Juan’s role as the island’s capital and economic hub also complicates parallel-trends assumptions across multiple outcomes (O’Neill et al., [2020](https://arxiv.org/html/2510.25782v1#bib.bib30)). The methodological task is to construct a coherent counterfactual that leverages information across outcomes while remaining interpretable for policy guidance.

### Methodological Framework

The MOSC “average estimator” minimizes pre-treatment imbalance in the average of de-meaned outcomes—producing one set of donor weights shared across outcomes (and, in practice, outcomes can be standardized by their pre-treatment SD before averaging) (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). Under regularity conditions—mean-zero sub-Gaussian errors and adequate signal-to-noise with a shared factor structure—common-weights approaches reduce bias from overfitting relative to separate fits as the product T0​KT\_{0}K grows; for the average objective specifically, the noise in the objective has a standard deviation smaller by roughly 1/K1/\sqrt{K}, further attenuating idiosyncratic variability (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). This is well suited to urban policy evaluation, where interventions operate through multiple channels and coherent cross-outcome interpretation is essential.

My empirical implementation shows these gains in practice. When outcomes exhibit shared factor structure—assessed with pre-treatment diagnostics including scree plots—common-weight estimation yields comprehensive detection across domains that separate approaches may not synthesize. In my application, the average estimator highlights measurable economic responses in targeted sectors while effects on public safety remain near zero, a distinction that would be harder to see with fragmented, outcome-specific counterfactuals.

##### Effect size reporting convention

Throughout, I report treatment effects in two complementary forms. For substantive interpretation, tables present effects after conversion to economically meaningful units: revenue effects as millions of dollars per quarter (computed by scaling estimated share changes by post-period island-wide sectoral totals); employment and crime as per-capita rates (per 1,000 residents). For cross-outcome comparison, the text emphasizes standardized effects in units of the treated municipality’s pre-treatment standard deviation (σ)(\sigma). This dual reporting facilitates both economic interpretation and methodological assessment of relative magnitudes across disparate outcome scales.

### Empirical Design

My empirical design implements a multi-stage screening protocol that reduces the initial pool of 77 municipalities to 6 final donors (Aguadilla, Arecibo, Bayamón, Cayey, Hatillo, Humacao) based on demographic comparability, economic structure matching, data completeness, policy-timing contamination screens, and pre-period predictability assessment using Granger causality diagnostics. To address scale heterogeneity between San Juan and smaller municipalities, I construct revenue outcomes as island-wide shares—capturing each municipality’s position in the island’s sectoral economy while avoiding inappropriate population denominators given San Juan’s role as a regional hub with visitor inflows and commuting patterns (details in Appendix [A.2](https://arxiv.org/html/2510.25782v1#A1.SS2 "A.2 Outcome Variable Construction ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). With the donor pool established, I assess whether the assumption of shared factor structure holds across my seven outcome variables—a crucial requirement for common-weight estimators (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

Rank diagnostics support low-rank structure: the first four components explain 94.4% of systematic variation with a clear elbow (leading singular values 11.73, 7.80, 6.24, 4.85; Figure [1](https://arxiv.org/html/2510.25782v1#S5.F1 "Figure 1 ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Leave-one-outcome-out checks and pre-treatment RMSPE comparisons appear in Appendix Table [A6](https://arxiv.org/html/2510.25782v1#A3.T6 "Table A6 ‣ C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") and Figure [2](https://arxiv.org/html/2510.25782v1#S5.F2 "Figure 2 ‣ Pre-treatment fit concern: Sector 18 revenue. ‣ 5.3.1 Pre-Treatment Fit Validation ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"). While broader applications are needed for external validation, this pattern suggests that economic, employment, and social outcomes in municipal settings share common drivers that common-weight methods can exploit.

My analysis proceeds in three steps: (i) pre-treatment diagnostics for shared structure, (ii) comparison of separate versus averaged synthetic controls, and (iii) statistical inference using joint conformal procedures and permutation-based placebos. The separate estimator attains better pre-treatment fit (mean RMSPE 0.7520.752 vs. 0.8780.878 for average), but the average estimator yields coherent donor selection—trading ≈17%\approx 17\% worse in-sample fit for greater stability and interpretability.

### Empirical Findings

I construct a balanced quarterly panel integrating three data sources spanning 2019 Q1 through 2025 Q1 (19 pre-treatment quarters, 6 post-treatment quarters): Puerto Rico’s Department of Economic Development and Commerce retail revenue data, Department of Labor and Human Resources employment statistics, and Police Bureau NIBRS crime incident reports. Across the first six post-treatment quarters, point estimates show economically meaningful employment responses—accommodation/food services employment +7.59​σ+7.59\sigma (+67.8+67.8 per 1,000), arts/entertainment employment +0.32​σ+0.32\sigma (+0.23+0.23 per 1,000)—alongside small revenue effects: restaurants/bars +0.01​σ+0.01\sigma (++$0.18M per quarter), supermarkets/liquor +0.00​σ+0.00\sigma (++$0.00M per quarter), gasoline/convenience stores +0.02​σ+0.02\sigma (++$0.07M per quarter). Crime effects remain near zero: late-night public disorder +0.01​σ+0.01\sigma (+0.00088+0.00088 per 1,000) and violent crime −0.26​σ-0.26\sigma (−0.08-0.08 per 1,000) (Figure [5](https://arxiv.org/html/2510.25782v1#S5.F5 "Figure 5 ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Joint conformal tests (p=0.600p{=}0.600, rank 12/2012/20, mid-p=0.575p{=}0.575) and permutation placebos (pp-value of 1/14≈0.0711/14\approx 0.071; 13 placebos plus the treated unit) do not reject the null, underscoring power-magnitude tradeoffs typical in small-NN designs.

The salient pattern is a divergence: economically meaningful employment responses without corresponding reductions in public disorder or violent crime. Both estimators indicate positive effects in targeted economic outcomes, while crime outcomes remain near zero. This distinction is policy-relevant: hour-based restrictions may shift economic behavior without delivering the intended public safety gains.

While longer-run dynamics await additional data releases, the framework and short-run evidence provide timely input where nightlife regulation, safety, and local development intersect. More broadly, my implementation shows that MOSC can enhance practice by enabling comprehensive cross-domain assessment—provided researchers diagnose low-rank structure and acknowledge limited power in small-sample settings.

Scope and robustness. I follow the multi–outcome synthetic control (MOSC) framework and confine robustness to *within–framework diagnostics*—pre-treatment standardization and sign alignment; averaged/concatenated/combined objectives with a ν\nu-grid; donor screening with weight-concentration metrics; and placebo and conformal inference with pre-period low-rank checks (scree, hold-one-outcome-out). Proposals to *swap estimators*, expand into mechanism modeling, re-time treatment beyond simple sensitivities, or alter the screened donor pool lie outside my identification strategy and are not required for validity (see Sections [3](https://arxiv.org/html/2510.25782v1#S3 "3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")–[4](https://arxiv.org/html/2510.25782v1#S4 "4 Multi-Outcome Synthetic Control: Inference ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

### Organization

Section [2.1](https://arxiv.org/html/2510.25782v1#S2.SS1 "2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") outlines MOSC theory; Section [3](https://arxiv.org/html/2510.25782v1#S3 "3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") details implementation; Section [4](https://arxiv.org/html/2510.25782v1#S4 "4 Multi-Outcome Synthetic Control: Inference ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents inference procedures; Section [5.1.1](https://arxiv.org/html/2510.25782v1#S5.SS1.SSS1 "5.1.1 Policy Context ‣ 5.1 Background and Context ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") describes the Code and institutional context; Section [5.2](https://arxiv.org/html/2510.25782v1#S5.SS2 "5.2 Data, Variables, and Sample Construction ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") covers data and donor screening; Section [5.3](https://arxiv.org/html/2510.25782v1#S5.SS3 "5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") assesses shared structure; Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") compares estimators; Section [5.5](https://arxiv.org/html/2510.25782v1#S5.SS5 "5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reports inference results; Section [6](https://arxiv.org/html/2510.25782v1#S6 "6 Discussion and Conclusion ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") concludes. Appendices document donor selection, outcome construction, robustness analyses, and additional cross-estimator comparisons.

## 2 Multi-Outcome Synthetic Control: Theory

### 2.1 Common Weights & Shared Structure

The baseline approach applies synthetic control independently to each outcome kk, estimating outcome-specific weights γk\gamma\_{k} that minimize pre-treatment RMSPE. While this achieves superior pre-treatment fit, it can overfit idiosyncratic noise and produces fragmented donor selection that complicates cross-outcome interpretation (full baseline details in Appendix [B.1](https://arxiv.org/html/2510.25782v1#A2.SS1 "B.1 Baseline Separate SCM Framework ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Under shared low-rank structure, common-weight estimators address these limitations: one set of donor weights can balance all outcomes while preserving interpretability.222Common weights leverage cross-outcome correlations to improve donor selection, but noise in any single outcome can propagate through joint optimization and degrade all predictions. This raises both R0R\_{0} (imperfect pre-fit) and R1R\_{1} (overfitting) in the bias decomposition; the 1/K1/\sqrt{K} gain assumes independent errors across outcomes. See Appendix [B.3](https://arxiv.org/html/2510.25782v1#A2.SS3 "B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") for the formal decomposition. Leave-one-outcome-out diagnostics can validate this consideration empirically.

#### 2.1.1 Factor Model and Low-Rank Assumption

Following Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)), I model potential outcomes under control with a linear factor structure. For unit ii at time tt and outcome kk,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi​t​k​(0)=αi​k+Li​t​k+εi​t​k,Y\_{itk}(0)\;=\;\alpha\_{ik}\;+\;L\_{itk}\;+\;\varepsilon\_{itk}, |  | (1) |

where αi​k\alpha\_{ik} are unit–outcome fixed effects (absorbed by de-meaning pre-treatment), Li​t​k=ϕi⊤​μt​kL\_{itk}=\phi\_{i}^{\top}\mu\_{tk} captures the systematic component driven by latent factors, and εi​t​k\varepsilon\_{itk} is idiosyncratic noise with 𝔼​[εi​t​k]=0\mathbb{E}[\varepsilon\_{itk}]=0 (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). Unit-specific loadings ϕi∈ℝr\phi\_{i}\in\mathbb{R}^{r} and time–outcome factors μt​k∈ℝr\mu\_{tk}\in\mathbb{R}^{r} allow both factors common across outcomes and outcome-specific factors, enabling dimension reduction while retaining flexibility (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

###### Assumption 1 (Low-Rank Structure).

Let L∈ℝN×(T​K)L\in\mathbb{R}^{N\times(TK)} stack {Li​t​k}\{L\_{itk}\} over all times and outcomes, and let L−1L\_{-1} exclude the treated unit. Then rank​(L−1)=rank​(L)<N−1\mathrm{rank}(L\_{-1})=\mathrm{rank}(L)<N-1.

This implies the treated unit’s latent trajectory lies in the donors’ row space (adds no new directions), so a nontrivial linear representation using donors exists; hence oracle weights can simultaneously balance the treated unit’s latent component across all pre-treatment times and outcomes (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

#### 2.1.2 Why Low-Rank Enables Common Weights

Under Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), there exist oracle weights γ⋆\gamma^{\star} such that L1​t​k=∑i=2Nγi⋆​Li​t​kL\_{1tk}=\sum\_{i=2}^{N}\gamma^{\star}\_{i}\,L\_{itk} for all times tt and outcomes kk, with 𝟏⊤​γ⋆=1\mathbf{1}^{\top}\gamma^{\star}=1. These oracle weights remove bias from the unobserved latent component simultaneously across all outcome-time pairs. When the treated unit’s factor loading additionally lies in the convex hull of donor loadings, simplex-constrained oracle weights exist. Feasible common-weight estimators target this goal by aggregating pre-treatment information across outcomes. Under regularity conditions (sub-Gaussian errors, adequate signal-to-noise, and shared factor structure), the bias component from overfitting to noise is tighter for common-weight estimators—scaling like O​((T0​K)−1/2)O((T\_{0}K)^{-1/2}) rather than O​(T0−1/2)O(T\_{0}^{-1/2})—by exploiting the KK-fold increase in pre-treatment observations (see Appendix [B](https://arxiv.org/html/2510.25782v1#A2 "Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") for formal statements and proofs from Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

#### 2.1.3 When Is Low-Rank Structure Plausible?

The shared-factor structure underlying Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") is compelling in many policy settings (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). Economic policy interventions affecting units with similar economic structure (labor markets, consumer demand, investment) induce co-movement across outcomes through shared channels. Institutional similarities from common legal or regulatory frameworks create correlated responses under interventions. Demographic and geographic factors such as spatial proximity and similar population characteristics generate shared exposure to shocks. Multiple measurements of related constructs—such as different test scores or crime categories indexing the same broad phenomenon—typically load on a small number of common factors (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). The low-rank premise is ultimately empirical and should be validated through practical diagnostics (see Section [5.3](https://arxiv.org/html/2510.25782v1#S5.SS3 "5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"); cf. Sec. 4.5 in Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

##### Forward reference.

The theoretical framework above motivates common-weight estimation but leaves implementation choices underspecified. Section [3.3](https://arxiv.org/html/2510.25782v1#S3.SS3 "3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") details the specific parameter choices, optimization procedures, standardization conventions, and temporal window specifications used throughout my analysis, with justification for each design decision. Readers primarily interested in implementation details may proceed directly to Section [3.3](https://arxiv.org/html/2510.25782v1#S3.SS3 "3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") after reviewing the empirical setting in Sections [5.1.1](https://arxiv.org/html/2510.25782v1#S5.SS1.SSS1 "5.1.1 Policy Context ‣ 5.1 Background and Context ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")–[5.2](https://arxiv.org/html/2510.25782v1#S5.SS2 "5.2 Data, Variables, and Sample Construction ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

## 3 Multi-Outcome Synthetic Control: Implementation

I implement the Multi-Outcome Synthetic Control (MOSC) “average estimator” of Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34))—which minimizes pre-treatment imbalance in the average of the outcome series—using simplex weights and intercept-shifted (de-meaned) prediction (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). My only departures from their framework are the treated-unit scaling and optional sign-alignment conventions described below, which facilitate interpretation and placebo testing in my application.

##### Scope of implementation.

The analysis is pre-specified within MOSC. Robustness is limited to *MOSC-internal* diagnostics: (i) scaling and sign alignment across outcomes; (ii) sensitivity across averaged, concatenated, and combined objectives via a ν\nu-grid; and (iii) donor screening with Stage-6 weight-concentration metrics. I deliberately do not engage in estimator horse-races or redesign the screened donor set, as such changes are orthogonal to the identification delivered by common donor weights across outcomes.

### 3.1 Average Estimator: Objective Function

For the pre-treatment mean Y¯i​kpre=1T0​∑t≤T0Yi​t​k\overline{Y}\_{ik}^{\text{pre}}=\tfrac{1}{T\_{0}}\sum\_{t\leq T\_{0}}Y\_{itk}, I define the demeaned series

|  |  |  |
| --- | --- | --- |
|  | Y˙i​t​k=Yi​t​k−Y¯i​kpre.\dot{Y}\_{itk}\;=\;Y\_{itk}-\overline{Y}\_{ik}^{\text{pre}}. |  |

For any γ∈𝒞\gamma\in\mathcal{C}, the per-outcome pre-treatment residual is

|  |  |  |
| --- | --- | --- |
|  | rt,k​(γ)=Y˙1​t​k−∑j∈𝒟γj​Y˙j​t​k(t≤T0),r\_{t,k}(\gamma)\;=\;\dot{Y}\_{1tk}-\sum\_{j\in\mathcal{D}}\gamma\_{j}\,\dot{Y}\_{jtk}\qquad(t\leq T\_{0}), |  |

and its cross-outcome average at time tt is

|  |  |  |
| --- | --- | --- |
|  | r¯t​(γ)=1K​∑k=1Krt,k​(γ)=Y˙¯1​t−∑j∈𝒟γj​Y˙¯j​t,\bar{r}\_{t}(\gamma)\;=\;\frac{1}{K}\sum\_{k=1}^{K}r\_{t,k}(\gamma)\;=\;\overline{\dot{Y}}\_{1t}-\sum\_{j\in\mathcal{D}}\gamma\_{j}\,\overline{\dot{Y}}\_{jt}, |  |

where Y˙¯i​t=1K​∑k=1KY˙i​t​k\overline{\dot{Y}}\_{it}=\tfrac{1}{K}\sum\_{k=1}^{K}\dot{Y}\_{itk} is the cross-outcome average (within time tt) of demeaned outcomes.

The average estimator chooses a *single* set of donor weights by minimizing pre-treatment imbalance in the timewise averaged residuals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ^avg∈arg⁡minγ∈𝒞⁡qavg​(γ),\hat{\gamma}^{\text{avg}}\in\arg\min\_{\gamma\in\mathcal{C}}\;q\_{\text{avg}}(\gamma), |  | (2) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | qavg​(γ)={1T0​∑t≤T0r¯t​(γ)2}1/2,q\_{\text{avg}}(\gamma)=\left\{\frac{1}{T\_{0}}\sum\_{t\leq T\_{0}}\bar{r}\_{t}(\gamma)^{2}\right\}^{1/2}, |  | (3) |

and 𝒞\mathcal{C} is a convex feasibility set for weights. In my baseline specification,

|  |  |  |
| --- | --- | --- |
|  | 𝒞=ΔN0={γ∈ℝN0:γj≥0, 1N0⊤​γ=1}.\mathcal{C}=\Delta\_{N\_{0}}=\Big\{\gamma\in\mathbb{R}^{N\_{0}}:\ \gamma\_{j}\geq 0,\ \mathbf{1}\_{N\_{0}}^{\top}\gamma=1\Big\}. |  |

For reference, the *concatenated* common-weights objective stacks all outcomes before averaging: qcat​(γ)={1T0​K​∑k=1K∑t≤T0rt,k​(γ)2}1/2q\_{\text{cat}}(\gamma)=\{\frac{1}{T\_{0}K}\sum\_{k=1}^{K}\sum\_{t\leq T\_{0}}r\_{t,k}(\gamma)^{2}\}^{1/2}. By Jensen’s inequality applied within each tt, for any fixed γ\gamma: qavg​(γ)≤qcat​(γ)q\_{\text{avg}}(\gamma)\leq q\_{\text{cat}}(\gamma). This inequality holds pointwise for any weight vector γ\gamma and implies that qavg​(γ^avg)≤qcat​(γ^avg)q\_{\text{avg}}(\hat{\gamma}^{\text{avg}})\leq q\_{\text{cat}}(\hat{\gamma}^{\text{avg}}) when both objectives are evaluated at the average estimator’s solution.

##### Reporting conventions.

Throughout Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") I report a mean per-outcome RMSPE: 1K​∑k=1K{1T0​∑t≤T0rt,k​(γ)2}1/2\frac{1}{K}\sum\_{k=1}^{K}\left\{\frac{1}{T\_{0}}\sum\_{t\leq T\_{0}}r\_{t,k}(\gamma)^{2}\right\}^{1/2}, where T0T\_{0} is the pre-period length. This reporting metric differs from the optimization objectives because ⋅\sqrt{\cdot} is concave (Jensen’s inequality): for the concatenated estimator, qcat​(γ^cat)q\_{\text{cat}}(\hat{\gamma}^{\text{cat}}) will generally differ from the mean per-outcome RMSPE. The objective reflects what the estimator minimizes; the RMSPE provides a standardized cross-estimator comparison that weights outcomes symmetrically.

For the averaged objective, two values of qavg​(⋅)q\_{\text{avg}}(\cdot) may be reported: qavg​(γ^avg)q\_{\text{avg}}(\hat{\gamma}^{\text{avg}}) (the objective evaluated at the averaged estimator) and qavg​(γ^cat)q\_{\text{avg}}(\hat{\gamma}^{\text{cat}}) (the same objective evaluated at the concatenated weights, used for scale-matching in Section [3.3.4](https://arxiv.org/html/2510.25782v1#S3.SS3.SSS4 "3.3.4 Combined Estimator and Parameter Selection ‣ 3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). The argument notation clarifies which estimator’s weights are being evaluated.

### 3.2 Post-Treatment Prediction: Intercept-Shift Reconstruction

Having obtained γ^avg\hat{\gamma}^{\text{avg}} from pre-treatment data, I construct post-treatment counterfactuals using intercept-shifted prediction. For each outcome kk and post-treatment period t>T0t>T\_{0}, the counterfactual is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y^1​t​kavg​(0)=Y¯1​kpre+(Yt​ksyn,avg−Y¯ksyn,avg,pre),\hat{Y}\_{1tk}^{\text{avg}}(0)\;=\;\overline{Y}\_{1k}^{\text{pre}}+\left(Y\_{tk}^{\text{syn,avg}}-\overline{Y}\_{k}^{\text{syn,avg,pre}}\right), |  | (4) |

where Yt​ksyn,avg=∑j∈𝒟γ^javg​Yj​t​kY\_{tk}^{\text{syn,avg}}=\sum\_{j\in\mathcal{D}}\hat{\gamma}\_{j}^{\text{avg}}Y\_{jtk} is the synthetic control outcome at time tt for outcome kk, and Y¯ksyn,avg,pre=1T0​∑t≤T0Yt​ksyn,avg\overline{Y}\_{k}^{\text{syn,avg,pre}}=\tfrac{1}{T\_{0}}\sum\_{t\leq T\_{0}}Y\_{tk}^{\text{syn,avg}} is its pre-treatment mean. The estimated treatment effect is then τ^t​kavg=Y1​t​k−Y^1​t​kavg​(0)\hat{\tau}\_{tk}^{\text{avg}}=Y\_{1tk}-\hat{Y}\_{1tk}^{\text{avg}}(0).

### 3.3 Implementation Conventions and Design Choices

My implementation follows Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) with specific choices tailored to my empirical setting. This section details the key design decisions that affect estimation, provides justification for each choice, and explains how these conventions facilitate interpretation and inference in my application.

#### 3.3.1 Optimization and Constraint Specification

I solve the convex quadratic program in Equation ([2](https://arxiv.org/html/2510.25782v1#S3.E2 "Equation 2 ‣ 3.1 Average Estimator: Objective Function ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) over the unit simplex 𝒞=ΔN0\mathcal{C}=\Delta\_{N\_{0}} using only pre-treatment observations (t≤T0t\leq T\_{0}). This specification imposes three key constraints:

##### Simplex constraint.

I require γj≥0\gamma\_{j}\geq 0 for all jj and 𝟏N0⊤​γ=1\mathbf{1}\_{N\_{0}}^{\top}\gamma=1. Non-negativity ensures the synthetic control interpolates rather than extrapolates, reducing sensitivity to model misspecification (Abadie et al., [2010](https://arxiv.org/html/2510.25782v1#bib.bib4)). The sum-to-one constraint enables intercept-shift reconstruction (Equation [4](https://arxiv.org/html/2510.25782v1#S3.E4 "Equation 4 ‣ 3.2 Post-Treatment Prediction: Intercept-Shift Reconstruction ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) by preserving level differences between treated and synthetic units in the post-period (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). While Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) allow a general constraint set for weights—often the simplex in practice—and also consider a combined objective that mixes the averaged and concatenated imbalance via a tuning parameter ν\nu, I use the simplex-only specification (i.e., C=ΔC=\Delta, no additional penalties) to maintain consistency with the canonical synthetic control framework and to avoid introducing extra tuning that would complicate replication.

##### Convex optimization.

I estimate γ^\hat{\gamma} by minimizing the squared averaged pre-treatment fit, qavg​(γ)2q\_{\mathrm{avg}}(\gamma)^{2}, over the simplex 𝒞={γ≥0, 1⊤​γ=1}\mathcal{C}=\{\gamma\geq 0,\ \mathbf{1}^{\top}\gamma=1\}. This is a smooth convex quadratic program. I solve it with projected gradient descent using a constant step η=1/L\eta=1/L, where L=‖X‖22+αL=\|X\|\_{2}^{2}+\alpha is the Lipschitz constant of the gradient computed from the spectral norm of the design matrix (with a power-iteration fallback). After each step I project onto the simplex using the efficient sort–threshold method of Duchi et al. ([2008](https://arxiv.org/html/2510.25782v1#bib.bib17)). For convex LL-smooth objectives over a convex set, projected gradient descent converges to a global minimizer; in practice I terminate when the relative iterate change falls below a fixed tolerance, ensuring reproducibility.

For the concatenated objective I solve the analogous least-squares program via the same PGD + projection routine. For the ν\nu-combined objective (a linear combination of RMSEs), I follow the paper’s formulation and solve the resulting SOCP in cvxpy (SCS/ECOS), then re-project onto the simplex.

##### Pre-treatment-only fitting.

I estimate weights using observations from t=1,…,T0t=1,\ldots,T\_{0} only, excluding all post-treatment data from the optimization. This ensures that weight selection cannot be influenced by post-treatment outcomes, preserving the integrity of the counterfactual construction and avoiding look-ahead bias that would invalidate causal inference (Abadie, [2021](https://arxiv.org/html/2510.25782v1#bib.bib3)).

#### 3.3.2 Standardization and Scaling Choices

I standardize each outcome kk by the treated unit’s pre-treatment standard deviation s1​kpres\_{1k}^{\text{pre}} before weight estimation, applying this same scale factor to all units (treated and donors) for outcome kk. This choice addresses three distinct challenges in multi-outcome synthetic control:

##### Cross-outcome comparability.

Without standardization, outcomes measured on different scales (e.g., employment in thousands versus raw revenue levels) would receive vastly different implicit weights in the averaged objective qavg​(γ)q\_{\text{avg}}(\gamma) (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). Standardization ensures that each outcome contributes approximately equally to the optimization, preventing outcomes with larger scales from dominating the weight selection; in practice, Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) recommend standardizing each series by its pre-treatment standard deviation (and optionally aligning signs for interpretability). This is particularly important in my application, where sectoral revenues (scale varies by municipality and sector) must be balanced against per-capita employment (scale ∼0.001\sim 0.001) and crime rates (scale ∼0.0001\sim 0.0001).

##### Treated-unit reference scale.

I use s1​kpres\_{1k}^{\text{pre}} rather than donor-specific standard deviations sj​kpres\_{jk}^{\text{pre}} for three reasons. First, this ensures consistent scaling across all placebo experiments during permutation inference: when any donor becomes the pseudo-treated unit, I can apply the same standardization protocol by using that unit’s pre-treatment SD as the reference. Second, it facilitates interpretation of treatment effects in units of the treated municipality’s pre-treatment variability, providing a natural benchmark for effect magnitude assessment. Third, it avoids the complication of choosing an aggregation rule when donor SDs differ substantially across units. The theoretical results in Section [2.1](https://arxiv.org/html/2510.25782v1#S2.SS1 "2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") hold under any consistent standardization scheme; my choice simply operationalizes this flexibility in a way that supports inference and interpretation.

##### Standardization timing and reversal.

Standardization occurs after demeaning but before weight optimization. I apply the transformation Y~i​t​k=Y˙i​t​k/s1​kpre\tilde{Y}\_{itk}=\dot{Y}\_{itk}/s\_{1k}^{\text{pre}} to construct the design matrices, estimate γ^avg\hat{\gamma}^{\text{avg}} on these standardized series, then reverse the standardization when reporting treatment effects. This ensures that final results appear on the original outcome scales (raw revenue levels, per-capita employment and crime rates), making coefficients directly interpretable for policy analysis. All treatment effect estimates reported in Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reflect this de-standardization, with standardized effects (σ\sigma units) used only for cross-outcome comparisons in the text discussion.

#### 3.3.3 Sign Alignment Convention

For outcomes where increases represent adverse policy effects (late-night public disorder, violent crime), I multiply the standardized series by −1-1 before computing the averaged objective. This sign alignment convention serves two purposes. First, it ensures that “positive” uniformly means “desirable” when averaging across outcomes, making the averaged residual r¯t​(γ)\bar{r}\_{t}(\gamma) interpretable as a scalar measure of overall imbalance in the direction of policy goals. Second, it facilitates joint hypothesis testing by aligning all outcomes so that positive treatment effects indicate success along each dimension.

I apply this convention only when computing cross-outcome summaries (e.g., the joint conformal test statistic in Section [4](https://arxiv.org/html/2510.25782v1#S4 "4 Multi-Outcome Synthetic Control: Inference ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) and when averaging standardized effects for narrative interpretation. Outcome-specific trajectories, tables, and figures always report effects on the original signed scale to preserve transparency about the direction of estimated impacts. The sign alignment mapping for each outcome appears in the replication code’s module, making this convention explicit and reproducible.

#### 3.3.4 Combined Estimator and Parameter Selection

The combined estimator of Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) interpolates between averaged and concatenated objectives via a convex combination with mixing parameter ν∈[0,1]\nu\in[0,1]:

|  |  |  |
| --- | --- | --- |
|  | qcomb​(γ;ν)=ν​qavg​(γ)+(1−ν)​qcat​(γ).q\_{\text{comb}}(\gamma;\nu)=\nu\,q\_{\text{avg}}(\gamma)+(1-\nu)\,q\_{\text{cat}}(\gamma). |  |

At ν=0\nu=0 this is the pure concatenated objective, and at ν=1\nu=1 the pure averaged objective, enabling a systematic sensitivity check to the aggregation method.

##### Implementation convention and selection.

For clarity relative to my main estimator, I adopt a relabeling of Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)): define ν:=1−νSBF\nu:=1-\nu\_{\text{SBF}}, so that larger ν\nu places more weight on cross-outcome averaging.333Mapping for readers comparing to Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)): νSBF=1−ν\nu\_{\text{SBF}}=1-\nu. The optimization problems are identical under this change of variables.
I select ν\nu using a simple scale-matching heuristic to avoid one objective dominating numerically in the convex combination: evaluate both objectives at the concatenated solution γ^cat\hat{\gamma}^{\text{cat}} and set

|  |  |  |
| --- | --- | --- |
|  | ν^=min⁡{1,qcat​(γ^cat)/qavg​(γ^cat)}.\hat{\nu}=\min\bigl\{1,\;q\_{\text{cat}}(\hat{\gamma}^{\text{cat}})/q\_{\text{avg}}(\hat{\gamma}^{\text{cat}})\bigr\}. |  |

This choice aligns the scales of the two objectives in the convex combination. When ν^=1\hat{\nu}=1, this coincides with the pure averaged estimator.

##### Sensitivity analysis.

Sensitivity to ν\nu can be assessed by evaluating the estimator across a grid of values (e.g., {0,0.25,0.5,0.75,1}\{0,0.25,0.5,0.75,1\}) and examining how fit metrics, donor allocations, and treatment effect estimates vary. Results for my application appear in Appendix [C.4](https://arxiv.org/html/2510.25782v1#A3.SS4 "C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

#### 3.3.5 Temporal Windows and Robustness Considerations

My primary specification uses 19 pre-treatment quarters (2019 Q1–2023 Q3) and six post-treatment quarters (2023 Q4–2025 Q1), with 2023 Q4 representing partial exposure following the November 9, 2023 implementation date. This configuration balances three considerations: capturing sufficient pre-treatment variation to estimate stable weights, respecting the binding data availability constraint from Department of Economic Development and Commerce retail statistics, and maintaining a focused analysis window that emphasizes immediate policy responses.

##### Pre-treatment window specification.

The 19-quarter pre-period provides adequate degrees of freedom for weight estimation (T0​K=19×7=133T\_{0}K=19\times 7=133 observations for 6 donor weights) while remaining short enough to make the parallel trends assumption plausible. The sample begins in 2019 Q1 to provide a consistent baseline across NIBRS crime data and Department of Labor and Human Resources employment statistics. I conduct robustness checks using alternative pre-treatment window endpoints, excluding the earliest quarters (2019 Q1–Q2) to assess sensitivity to potential startup effects. These checks, reported in Appendix [C](https://arxiv.org/html/2510.25782v1#A3 "Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), yield no material changes to weight allocation or treatment effect estimates, confirming that results are not driven by the specific choice of sample start date.

##### Post-treatment horizon.

The six-quarter post-period (2023 Q4–2025 Q1) captures both immediate adjustments and medium-term adaptation patterns while acknowledging that longer-run equilibrium effects may continue to evolve as businesses and consumers adapt more fully to the restrictions. This temporal window maintains a consistent post-period across all outcomes (retail revenue, employment, and crime data) to ensure that estimated effects reflect synchronized responses rather than differential observation windows.

##### Partial exposure treatment.

I include 2023 Q4 in the post-period despite containing only seven weeks of exposure (November 9–December 31, 2023, out of 13 calendar weeks). I use the first calendar quarter containing the treatment date as the initial post-period. This convention treats any quarter containing the treatment date as post-treatment, consistent with standard quarterly panel analysis where treatment timing within quarters cannot be precisely identified. The implications of partial exposure can be assessed through robustness checks using alternative test statistics and examining temporal patterns in estimated effects (see Appendix [C](https://arxiv.org/html/2510.25782v1#A3 "Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

#### 3.3.6 Summary of Implementation Conventions

Table [1](https://arxiv.org/html/2510.25782v1#S3.T1 "Table 1 ‣ 3.3.6 Summary of Implementation Conventions ‣ 3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") summarizes the key implementation choices and their primary justifications. These conventions apply consistently throughout the analysis, including the baseline estimation (Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), robustness checks (Appendix [C](https://arxiv.org/html/2510.25782v1#A3 "Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), and inference procedures (Section [4](https://arxiv.org/html/2510.25782v1#S4 "4 Multi-Outcome Synthetic Control: Inference ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

Table 1: Summary of implementation conventions

|  |  |
| --- | --- |
| Convention | Specification and Justification |
| Weight constraints | Simplex only (γj≥0\gamma\_{j}\geq 0, ∑jγj=1\sum\_{j}\gamma\_{j}=1); no ridge penalty (α=0\alpha=0). Ensures interpolation, preserves intercept-shift, maintains canonical SCM framework. |
| Optimization | Pre-treatment data only (t≤T0t\leq T\_{0}); projected gradient descent. Avoids look-ahead bias, guarantees global optimum. |
| Standardization | Treated unit’s pre-treatment SD (s1​kpres\_{1k}^{\text{pre}}) applied to all units for each outcome. Ensures cross-outcome comparability, facilitates permutation inference, supports effect interpretation. |
| Sign alignment | Crime outcomes (late-night public disorder, violent crime) multiplied by −1-1; all other outcomes by +1+1. Mapping: Sector 14 revenue (+1)(+1), Sector 16 revenue (+1)(+1), Sector 18 revenue (+1)(+1), Accommodation/Food Emp. (+1)(+1), Arts/Entertainment Emp. (+1)(+1), Late Public Disorder (−1)(-1), Violent Crime (−1)(-1). Aligns “positive” with “desirable” for joint tests; outcome-specific results always reported on original signed scales. |
| Intercept-shift | Pre-treatment means removed before optimization, restored in reconstruction (Eq. [4](https://arxiv.org/html/2510.25782v1#S3.E4 "Equation 4 ‣ 3.2 Post-Treatment Prediction: Intercept-Shift Reconstruction ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Focuses fit on trends rather than levels. |
| Temporal windows | PRE: 2019 Q1–2023 Q3 (19 quarters); POST: 2023 Q4–2025 Q1 (6 quarters). Balances stability, data availability, and immediate response focus. |
| Combined estimator | Mixing parameter ν=1.0\nu=1.0 from scale matching (pure averaged estimator); sensitivity across ν∈[0,1]\nu\in[0,1] in Appendix [C.4](https://arxiv.org/html/2510.25782v1#A3.SS4 "C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"). Validates robustness to aggregation method. |
| Effects reporting | Original scales (raw revenue levels, per-capita rates) in tables/figures; standardized effects (σ\sigma units) for cross-outcome text comparisons. Maintains interpretability. |

Results using these implementation conventions are presented in Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") and Appendix [C.4](https://arxiv.org/html/2510.25782v1#A3.SS4 "C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

### 3.4 Bias Properties and Theoretical Motivation

When outcomes share a common low-rank factor structure (Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), the average estimator offers several advantages over separate estimation. First, *noise attenuation*: averaging across KK outcomes reduces objective variability by roughly 1/K1/\sqrt{K} when outcomes share common factors, suppressing outcome-specific noise and curbing overfitting. Second, *fit dominance*: because qavgq\_{\text{avg}} averages within-tt before squaring, for any fixed weights qavg​(γ)≤qcat​(γ)q\_{\text{avg}}(\gamma)\leq q\_{\text{cat}}(\gamma) by Jensen’s inequality. My empirical RMSPE comparisons use a common reporting metric and therefore can rank estimators differently, but this mathematical relationship yields tighter R0R\_{0} bounds in finite samples. Third, *information pooling*: by consolidating information across outcomes into a single balancing problem, the average estimator reduces the overfitting risk that arises when fitting KK separate weight vectors, particularly when T0T\_{0} is limited.

Formally, estimation error decomposes into bias and noise components. The bias term can be further expressed as imperfect pre-treatment fit (R0R\_{0}) minus overfitting to noise (R1R\_{1}). Under the shared factor structure, R0R\_{0} attenuates at rate O​(1/K)O(1/\sqrt{K}) for the average estimator (versus O​(1)O(1) for separate estimation), while R1R\_{1} scales like O​(1/T0​K)O(1/\sqrt{T\_{0}K}) (versus O​(1/T0)O(1/\sqrt{T\_{0}}) for separate estimation). These high-probability bounds hold under sub-Gaussian errors and sufficient temporal signal assumptions. With strong cross-outcome error correlation, additional conditions are needed; in the extreme case of perfectly correlated errors, the benefit from additional outcomes disappears. A single synthetic control also aids interpretation by providing a unified donor composition for all outcomes, enabling coherent cross-outcome narratives and parsimonious reporting.

*Full formal treatment—including formal assumptions (Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), oracle weights (Proposition [1](https://arxiv.org/html/2510.25782v1#Thmproposition1 "Proposition 1 (Oracle Weights). ‣ B.2.2 Formal Assumptions and Oracle Weights ‣ B.2 Multi-Outcome Common-Weight Framework ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), R0/R1R\_{0}/R\_{1} bias decomposition (Equations [27](https://arxiv.org/html/2510.25782v1#A2.E27 "Equation 27 ‣ 1st item ‣ B.3.3 Scaling Rates for Common-Weight Estimators ‣ B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")–[28](https://arxiv.org/html/2510.25782v1#A2.E28 "Equation 28 ‣ 2nd item ‣ B.3.3 Scaling Rates for Common-Weight Estimators ‣ B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), finite-sample fit dominance, and proofs—appears in Appendix [B](https://arxiv.org/html/2510.25782v1#A2 "Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").*

## 4 Multi-Outcome Synthetic Control: Inference

Statistical inference for multi-outcome synthetic control presents unique challenges. I leverage the joint structure across outcomes to test comprehensive hypotheses about policy effects using two complementary approaches: joint conformal inference and permutation placebos.

##### Inference scope.

Consistent with MOSC best practice, I use permutation placebos and joint conformal inference adapted to multiple outcomes. With a small donor pool and short post–period, coarse permutation pp–values are expected; conformal procedures address this explicitly under stated assumptions. I do not introduce auxiliary inference frameworks or additional estimators, as they do not strengthen identification within the MOSC design. *Implementation conventions are identical across both methods: pre-period intercept shift (demeaning within unit–outcome), outcome-wise scaling by the treated unit’s pre-period standard deviation, and sign alignment applied after scaling; the two methods differ only in their test statistic and time aggregation.*

### 4.1 Joint Conformal Inference

Following Chernozhukov et al. ([2021](https://arxiv.org/html/2510.25782v1#bib.bib13)) as adapted by Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)), I test the joint sharp null H0:τ=𝟎KH\_{0}:\tau=\mathbf{0}\_{K} using a first-post conformal procedure. Under H0H\_{0}, I null-adjust the treated unit’s *first* post-treatment observation, augment the pre-treatment sample with this null-adjusted period, and *re-estimate weights using the same objective as in estimation (hard-coded: averaged)* on the augmented sample. Preprocessing matches estimation exactly: intercept-shift within (unit, outcome) over the pre-period, standardization by the treated unit’s pre SD for each outcome, and sign alignment applied after scaling. I then compute a joint-KK residual score at t=T0+1t=T\_{0}+1 using the L1/KL\_{1}/\sqrt{K} norm; the pp-value compares this post-period score to the empirical distribution of the same score over the T0T\_{0} pre-periods (with the standard +1+1 correction). Asymptotic validity holds—i.e., the test attains approximately correct size—as T0T\_{0} (and the donor pool size NN, insofar as it delivers consistent counterfactual estimation) grow, provided the counterfactual estimator is consistent when re-estimated on the augmented sample that includes the post period. Full procedures are in Appendix [C.2](https://arxiv.org/html/2510.25782v1#A3.SS2 "C.2 Inference Procedures: Joint Conformal and Permutation Tests ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

### 4.2 Permutation-Based Placebo Tests

Permutation inference treats donors as placebo-treated units under the null that, *conditional on the pre-specified screening rules and pre-treatment data*, the treated unit could have been any element of the screened donor set (i.e., labels are exchangeable). For each donor, I remove it from the pool, re-estimate as if treated, compute its first post-treatment effect vector, and construct a scalar test statistic. The placebo pool 𝒫\mathcal{P} combines in-space placebos (donor units) and, when the pool is small, in-time placebos (pre-treatment periods treated as hypothetical intervention dates). The total placebo pool size determines the discrete pp-value grid: with NplaceboN\_{\text{placebo}} total placebos, the minimum achievable pp-value is 1/(Nplacebo+1)1/(N\_{\text{placebo}}+1). This discreteness is inherent to small-sample permutation inference (details in Appendix [C.2](https://arxiv.org/html/2510.25782v1#A3.SS2 "C.2 Inference Procedures: Joint Conformal and Permutation Tests ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). *In implementation, I use the averaged objective with the same preprocessing as above and take as the primary scalar statistic the post/pre RMSPE ratio computed from gaps scaled by the treated unit’s pre SDs, aggregating the first HH post periods (here H=5H=5); I also report a sensitivity statistic equal to the first-post median absolute gap across outcomes.*

### 4.3 Advantages of Joint Testing

Joint testing across outcomes offers several advantages: it avoids multiple-testing corrections by using a single test for the global null; it provides policy-relevant power by detecting effects across interconnected outcomes; it delivers coherent interpretation through one p-value; and it exploits the shared factor structure motivating MOSC. *(In this implementation, conformal uses a first-post L1L\_{1} joint score, whereas permutation uses a multi-post RMSPE-ratio score.)* Conformal inference emphasizes finite-sample validity in the time dimension, while permutation tests emphasize randomization validity in the cross-sectional dimension. Agreement across both methods strengthens credibility. Following Abadie ([2020](https://arxiv.org/html/2510.25782v1#bib.bib2)), who cautions against relying on statistical significance alone and recommends weighing estimate magnitude/precision, plausibility, and design quality, I complement formal tests with effect trajectories, placebo distributions, and diagnostic plots. Implementation conventions (standardization, sign alignment, weight constraints) are detailed in Appendix [C.2](https://arxiv.org/html/2510.25782v1#A3.SS2 "C.2 Inference Procedures: Joint Conformal and Permutation Tests ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") and applied consistently across all procedures.

## 5 Empirical Application: Effect of San Juan’s Public Order Code

### 5.1 Background and Context

San Juan’s Public Order Code restricts late-night alcohol sales across multiple commercial sectors, creating a natural experiment for evaluating how temporal regulations affect economic activity and public safety outcomes.

#### 5.1.1 Policy Context

Effective November 9, 2023, San Juan’s Public Order Code establishes temporal restrictions on alcohol sales during 1–6 AM on weekdays and 2–6 AM on weekends, with Mondays that are legal holidays following the weekend schedule (Municipio Autónomo de San Juan, Legislatura
Municipal, [2023](https://arxiv.org/html/2510.25782v1#bib.bib29)). The policy applies uniformly to establishments selling or serving alcoholic beverages—including restaurants, bars, nightlife venues, convenience stores, gas stations, supermarkets, and liquor stores—with limited exemptions for registered hotel guests and private non-commercial events. Violations carry escalating penalties including administrative fines and potential permit cancellation for repeat offenders.

Municipal authorities framed the ordinance as balancing vibrant nightlife with public safety and residential tranquility, while business associations contested its economic impacts and safety benefits (Asociación de Empresarios Calle Loíza,
Inc., et al. v. Municipality of San Juan, [2023](https://arxiv.org/html/2510.25782v1#bib.bib8)). The ordinance later withstood federal court challenge under rational-basis review, where the court noted that “a legislative choice … may be based on rational speculation unsupported by evidence or empirical data” (Asociación de Empresarios Calle Loíza,
Inc., et al. v. Municipality of San
Juan, [2024](https://arxiv.org/html/2510.25782v1#bib.bib9)). Extended institutional context, enforcement details, stakeholder perspectives, and theoretical mechanisms appear in Appendix [D](https://arxiv.org/html/2510.25782v1#A4 "Appendix D Context & Mechanisms ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

#### 5.1.2 Multi-Outcome Framework and Analytical Strategy

The ordinance may affect multiple interconnected domains through different mechanisms: sectoral revenue shifts reflect temporal and venue substitution as consumers adjust purchasing patterns; employment effects capture business operational responses to reduced hours; and crime outcomes test whether alcohol access restrictions achieve public safety objectives. A joint analytical framework is essential for coherent policy evaluation when effects manifest across outcome domains (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

I examine seven outcomes across three domains: *island-wide revenue shares* for restaurants/bars (Sector 18), gas stations/convenience stores (Sector 16), and supermarkets/liquor stores (Sector 14); per-capita employment in accommodation/food services (NAICS 72) and arts/entertainment/recreation (NAICS 71); and per-capita crime rates for late-night public disorder (during restricted hours) and all-hours violent crime. The employment outcome (NAICS 72) includes both hotels and standalone food establishments, while the revenue outcome (Sector 18) likely captures primarily standalone restaurants and bars due to differential measurement coverage across data sources, enabling examination of how the policy’s hotel exemption reallocates activity between establishment types with differential regulatory treatment and measurement. Because all alcohol sales face identical time restrictions except for this hotel exemption, differential sectoral effects reflect operational adaptation and the regulatory advantage granted to hotel-affiliated venues. The temporal crime distinction tests whether impacts concentrate in policy-relevant hours. Data sources, outcome construction, and donor pool screening appear in Appendix [A](https://arxiv.org/html/2510.25782v1#A1 "Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

The multi-outcome synthetic control framework constructs coherent counterfactuals that leverage information across outcomes while maintaining transparency and interpretability (Abadie et al., [2015](https://arxiv.org/html/2510.25782v1#bib.bib5)). Given the policy’s recent implementation and data availability constraints, the analysis covers six post-treatment quarters (2023 Q4 through 2025 Q1), with 2023 Q4 featuring partial exposure by construction, capturing immediate adjustments while recognizing that longer-run equilibrium effects may differ as businesses and consumers fully adapt.

### 5.2 Data, Variables, and Sample Construction

I construct a balanced quarterly panel (2019 Q1–2025 Q1: 19 pre-treatment, 6 post-treatment quarters) integrating retail revenue, employment, and crime data from three primary sources: Puerto Rico’s Department of Economic Development and Commerce (monthly retail sales tax records), Department of Labor and Human Resources (quarterly employment statistics), and Police Bureau (NIBRS incident reports). The treatment date is November 9, 2023, placing 2023 Q4 as the first post-treatment quarter with partial exposure. Data sources, temporal harmonization procedures, outcome construction, and donor pool screening methodology appear in Appendix [A](https://arxiv.org/html/2510.25782v1#A1 "Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

##### Crime variable definitions.

I measure “public disorder” using NIBRS Group B arrest codes for Disorderly Conduct (90C), Driving Under the Influence (90D), and Liquor Law Violations (90G), excluding Trespass (90J), Drug violations (35A, 35B), Vandalism (290), and “All Other Offenses” (90Z) to avoid the 2021 NIBRS revision structural break. “Violent crime” aggregates Part I serious offenses: Murder/Non-negligent Manslaughter (09A), Negligent Manslaughter (09B), Kidnapping/Abduction (100), Rape (11A), Sodomy (11B), Sexual Assault with an Object (11C), Fondling (11D), Aggravated Assault (13A), and Robbery (120), excluding Justifiable Homicide (09C), Simple Assault (13B), and Intimidation (13C).

Critical measurement distinction: NIBRS reporting requirements create an important interpretive difference between these crime measures. Group A offenses (violent crime) are reported for all incidents regardless of arrest, providing a comprehensive measure of violent incidents. In contrast, Group B offenses (public disorder) are recorded only upon arrest or citation (Federal Bureau of Investigation, [2025](https://arxiv.org/html/2510.25782v1#bib.bib19)). This means the public disorder outcome measures *arrests for disorder* rather than *incidents of disorder*. Consequently, the observed null effect for late-night public disorder could reflect either (a) no change in underlying disorder incidents, or (b) unchanged disorder levels accompanied by reduced police enforcement (e.g., officers reallocated away from nightlife districts, changed arrest priorities, or reduced late-night patrols). This limitation does not affect the violent crime measure, which captures all incidents regardless of police response.

##### Outcome framework.

I examine seven outcomes across three domains: *island-wide revenue shares* for restaurants/bars (Sector 18: NAICS 722), gas stations/convenience stores (Sector 16: NAICS 447, 4471), and supermarkets/liquor stores (Sector 14: NAICS 4451, 4453); per-capita employment in accommodation/food services (NAICS 72) and arts/entertainment/recreation (NAICS 71); and per-capita crime rates for late-night public disorder (during restricted hours 1–6 AM on weekdays and 2–6 AM on weekends) and all-hours violent crime.

Measurement structure and interpretation. The employment and revenue outcomes capture different establishment types by design. The accommodation/food employment outcome (NAICS 72) includes both hotels (NAICS 721) and standalone food service establishments (NAICS 722), while the Sector 18 revenue measure is defined by DDEC as "Restaurants & Drinking Places" (NAICS 722). I cannot verify from publicly available DDEC documentation whether hotels—as accommodation establishments rather than retail establishments—report food and beverage revenue within the retail sales tax system at all. The DDEC data covers approximately 45,000 "establecimientos comerciales" (commercial establishments) classified into 18 retail sectors, with no accommodation sector among them.

The observed pattern—substantial employment increases (+7.59σ\sigma) alongside minimal Sector 18 revenue effects (+0.01σ\sigma)—admits two interpretations. If hotels report F&B revenue under Sector 18, hotels anticipated increased demand from the exemption but this demand did not fully materialize. If hotels do not report F&B revenue under Sector 18 (the most plausible interpretation given the retail sales terminology and sector classification), hotels both anticipated and experienced increased demand, but I observe only the employment effect because hotel revenue operates outside this measurement system. I interpret the employment-revenue divergence under the second scenario: the measurement asymmetry between data sources—employment captures both hotels and standalone establishments (NAICS 72) while revenue captures primarily standalone establishments (Sector 18)—combined with the hotel exemption creates precisely the observed pattern. This interpretation is supported by three empirical patterns: the large divergence magnitude, the break in pre-treatment correlation (0.93), and the temporal persistence across all post-treatment quarters rather than subsequent adjustment. Because all alcohol sales face identical time restrictions except for the hotel exemption, differential effects between these measures reflect the policy’s heterogeneous impact across establishment types with differing regulatory treatment.

Outcome construction details, including the rationale for using shares for revenue and per-capita scaling for crime/employment, appear in Appendix [A.2](https://arxiv.org/html/2510.25782v1#A1.SS2 "A.2 Outcome Variable Construction ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

##### Analytical strategy.

The multi-outcome synthetic control framework constructs coherent counterfactuals that leverage information across outcomes while maintaining transparency and interpretability (Abadie et al., [2015](https://arxiv.org/html/2510.25782v1#bib.bib5)). My six-stage donor pool screening protocol—filtering for demographic similarity, economic structure alignment, data quality, pre-treatment contamination, and *design* validation of parallel trends and proximity (70/7)—yields a six-municipality design pool: Aguadilla, Arecibo, Bayamón, Cayey, Hatillo, Humacao (methodology in Appendix [A.3](https://arxiv.org/html/2510.25782v1#A1.SS3 "A.3 Six-Stage Donor Pool Screening ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"); final pool summary in Appendix [A.4](https://arxiv.org/html/2510.25782v1#A1.SS4 "A.4 Final Donor Pool ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Stage 6 provides *non-binding* diagnostics on this design pool and does not alter selection.

### 5.3 Diagnostics: Assessing Shared Structure

The validity of common-weight MOSC estimators hinges on the low-rank assumption (Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") from Section [2.1](https://arxiv.org/html/2510.25782v1#S2.SS1 "2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), which requires that the treated unit’s latent trajectory lies within the span of the donor units’ factor space. When this condition holds, oracle weights exist that can simultaneously balance all outcomes, enabling the theoretical advantages outlined in Section [2.1](https://arxiv.org/html/2510.25782v1#S2.SS1 "2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"). I empirically assess whether my pre-treatment data exhibit the requisite shared structure through singular value decomposition (SVD) of the stacked outcome matrix.

Following my replication code, I apply MOSC pre-treatment transformations, column-center the donor matrix, and compute its SVD. I define effective rank as singular values exceeding numerical tolerance and report cumulative explained variance.

Figure [1](https://arxiv.org/html/2510.25782v1#S5.F1 "Figure 1 ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") shows a scree plot with a pronounced elbow: singular values drop rapidly from σ1≈11.73\sigma\_{1}\approx 11.73 to 7.807.80, 6.246.24, and 4.854.85. This pattern is consistent with a low-dimensional factor structure in the donors’ pre-treatment stack. The rank diagnostics confirm this visual evidence quantitatively. The effective rank equals 66, indicating six components contain meaningful signal above numerical tolerance thresholds. Variance explained: 49.8%49.8\% (r=1r=1), 71.8%71.8\% (r=2r=2), 85.8%85.8\% (r=3r=3), 94.4%94.4\% (r=4r=4), 97.7%97.7\% (r=5r=5). Five components (r95=5r\_{95}=5) capture essentially all systematic variation in the pre-treatment data, with all six components accounting for 100%100\% within numerical precision. This empirical validation directly supports Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") from Section [2.1](https://arxiv.org/html/2510.25782v1#S2.SS1 "2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"): the treated unit’s latent trajectory lies within the donors’ factor space, justifying common-weight constraints that balance all outcomes simultaneously.

![Refer to caption](figures/compare/pre_block_rank.png)


Figure 1: Scree plot showing rapid decay in singular values. Five components explain 97.7% of variance, supporting low-rank structure assumption (Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

##### Condition number diagnostic.

Following MOSC’s Online Appendix, I compare the condition number of the averaged pre-treatment design with those from outcome-specific designs. MOSC suggest that, when a strong common factor is present, averaging increases the condition number relative to separate SCM; with largely idiosyncratic variation, the increase is modest. In my data, κ​(X¯pre)=7.46\kappa(\bar{X}\_{\text{pre}})=7.46 and the median separate κ=19.57\kappa=19.57, yielding a ratio of 0.38(<1)0.38\,(<1). This pattern does not match the strong-common-factor signal described by MOSC. However, MOSC recommends the Average objective as default when outcomes exhibit shared factor structure (confirmed by our scree plot), noting that the condition number diagnostic and RMSPE reporting can favor Concatenated due to Jensen’s inequality even when averaging is theoretically appropriate. To assess whether this diagnostic indicates a substantive methodological concern, I implement both Average and Concatenated estimators and compare their inference properties in Section [5.5](https://arxiv.org/html/2510.25782v1#S5.SS5 "5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

##### Pre-treatment imbalance metrics.

The averaged estimator achieves qavg=0.240q\_{\text{avg}}=0.240 (definitions in Section [3.1](https://arxiv.org/html/2510.25782v1#S3.SS1 "3.1 Average Estimator: Objective Function ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"); numerical values for all estimators in Appendix [C.4](https://arxiv.org/html/2510.25782v1#A3.SS4 "C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), Table [A9](https://arxiv.org/html/2510.25782v1#A3.T9 "Table A9 ‣ Pre-treatment imbalance at selected 𝜈 values. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Outcomes are standardized by treated-unit pre-treatment SD and signs aligned so positive effects indicate desirable outcomes (Section [3.3.3](https://arxiv.org/html/2510.25782v1#S3.SS3.SSS3 "3.3.3 Sign Alignment Convention ‣ 3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Donor leave-one-out sensitivity analysis confirms acceptable robustness (maximum degradation 5.3%; see Appendix [C.3](https://arxiv.org/html/2510.25782v1#A3.SS3 "C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), Figure [A1](https://arxiv.org/html/2510.25782v1#A3.F1 "Figure A1 ‣ C.3.1 Leave-One-Donor-Out (LODO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

##### Cross-outcome error correlation.

The 1/K1/\sqrt{K} variance reduction relies on limited cross-outcome error correlation.

Table 2: Cross-outcome correlation matrix of pre-treatment residuals (Average estimator)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Acc/Food | Violent | Arts/Ent | Late Dis. | Sector 14 | Sector 16 | Sector 18 |
| Acc/Food Emp | 1.00 |  |  |  |  |  |  |
| Violent Crime | 0.67 | 1.00 |  |  |  |  |  |
| Arts/Ent Emp | 0.34 | -0.05 | 1.00 |  |  |  |  |
| Late Public Disorder | 0.33 | 0.11 | 0.33 | 1.00 |  |  |  |
| Sector 14 share | 0.02 | 0.33 | -0.55 | 0.20 | 1.00 |  |  |
| Sector 16 share | 0.08 | 0.33 | -0.43 | 0.25 | 0.64 | 1.00 |  |
| Sector 18 share | 0.93 | 0.65 | 0.25 | 0.31 | 0.18 | 0.24 | 1.00 |
| Summary: Mean |ρ||\rho| = 0.34; Median |ρ||\rho| = 0.33; Range = [−0.55-0.55, 0.93]; Max = 0.93 | | | | | | | |

Notes: Correlations computed from pre-treatment residuals (2019Q1–2023Q3, T0=19T\_{0}=19 quarters) under the average estimator. Residuals are gaps between treated outcomes and synthetic control predictions. The strongest correlations (0.93) occur between Sector 18 and accommodation/food employment, reflecting their direct linkages. All correlations |ρ|<0.95|\rho|<0.95 support the assumption of limited error dependence required for 1/K1/\sqrt{K} efficiency gains.

##### Connection to LOOO robustness.

The “drop-the-noisiest” check is a special case of the leave-one-out-outcome (LOOO) analysis already reported in Appendix [C.3.2](https://arxiv.org/html/2510.25782v1#A3.SS3.SSS2 "C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"). Let o⋆=arg⁡maxo⁡RMSPEoo^{\star}=\arg\max\_{o}\text{RMSPE}\_{o} denote the outcome with the largest pre-treatment RMSPE; the LOOO specification that excludes o⋆o^{\star} *is* the requested check. As shown in Appendix [C.3.2](https://arxiv.org/html/2510.25782v1#A3.SS3.SSS2 "C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), excluding each outcome in turn—which includes the o⋆o^{\star} case—leaves aggregated economic and crime effects qualitatively unchanged, preserves signs, and yields similar donor allocations. For clarity, Appendix Table [A6](https://arxiv.org/html/2510.25782v1#A3.T6 "Table A6 ‣ C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") highlights the o⋆o^{\star} column; readers can verify that the K−1K{-}1 estimates align with the full-KK results, confirming that the 1/K1/\sqrt{K} gains are not driven by a single noisy series.

#### 5.3.1 Pre-Treatment Fit Validation

Table [3](https://arxiv.org/html/2510.25782v1#S5.T3 "Table 3 ‣ 5.3.1 Pre-Treatment Fit Validation ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents pre-treatment RMSPE statistics across estimators.

Table 3: Pre-treatment fit summary: RMSPE by estimator. Average’s 17% fit disadvantage reflects information pooling constraints that reduce overfitting in treatment effect estimation.

|  |  |  |
| --- | --- | --- |
| Estimator | Mean RMSPE | Std. Error |
| Separate | 0.752 | (0.063) |
| Average | 0.878 | (0.046) |

Notes: RMSPE computed on series standardized by the treated unit’s pre-treatment standard deviation. Lower values indicate better fit. Reported standard errors are across outcomes.

The empirical results confirm theoretical predictions: separate estimation achieves 17% better pre-treatment fit (mean RMSPE 0.752 vs. 0.878) through outcome-specific optimization. However, as I demonstrate in Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), this fit advantage produces highly volatile treatment effects that undermine policy inference. The per-outcome breakdown shows separate’s strongest advantages in arts/entertainment employment and late-night public disorder, while the average estimator maintains more uniform fit quality across outcomes—reflecting its information pooling design.

Figure [2](https://arxiv.org/html/2510.25782v1#S5.F2 "Figure 2 ‣ Pre-treatment fit concern: Sector 18 revenue. ‣ 5.3.1 Pre-Treatment Fit Validation ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") demonstrates that the average estimator achieves strong pre-treatment balance across all outcomes, with both low RMSPE and high correlation between treated and synthetic trajectories. Figure [3](https://arxiv.org/html/2510.25782v1#S5.F3 "Figure 3 ‣ Pre-treatment fit concern: Sector 18 revenue. ‣ 5.3.1 Pre-Treatment Fit Validation ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") illustrates the temporal fit quality, showing narrow confidence bands and near-zero mean gaps during the pre-treatment period.

##### Outcome-specific fit quality and trend alignment.

Figure [2](https://arxiv.org/html/2510.25782v1#S5.F2 "Figure 2 ‣ Pre-treatment fit concern: Sector 18 revenue. ‣ 5.3.1 Pre-Treatment Fit Validation ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reveals an important diagnostic pattern for accommodation/food employment: while this outcome exhibits the poorest absolute fit among all seven outcomes (RMSE = 6.140, compared to the next-worst of 0.531 for arts/entertainment employment), it simultaneously shows the *strongest* trend correlation (0.928). This combination—poor level fit but excellent directional tracking—provides critical information about the nature of the fitting challenge and supports interpreting post-treatment divergences as genuine policy responses rather than artifacts of poor pre-treatment matching.

The high correlation (0.928) indicates that the synthetic control successfully captures the temporal dynamics of San Juan’s accommodation/food employment series, correctly tracking the ups and downs during the pre-treatment period even though the absolute levels differ. This pattern is consistent with a *systematic level offset*—San Juan’s employment baseline differs from what the donor pool can reproduce, likely reflecting its unique position as Puerto Rico’s economic hub—rather than random fitting failure or structural mismatch. If the poor fit were due to noise or fundamental incompatibility between San Juan and the donors, we would expect both poor RMSE and poor correlation. Instead, the donors appear to capture the relevant factor structure for this outcome, just with a persistent level shift.

This interpretation is strengthened by comparison to other outcomes with different RMSE-correlation patterns, particularly Sector 18 revenue, which exhibits the opposite pattern: low RMSE but negative correlation (discussed below).

##### Pre-treatment fit concern: Sector 18 revenue.

A significant pre-treatment fit limitation warrants explicit discussion. Revenue Sector 18 (restaurants and drinking places) exhibits RMSE = 0.021—seemingly excellent absolute fit—but correlation = −0.40-0.40 with San Juan’s pre-treatment trajectory. This negative correlation means the synthetic control moves in the *opposite direction* from the treated unit during the pre-treatment period, suggesting the low RMSE is achieved by coincidence rather than by capturing the underlying dynamics. This is a more serious fit failure than accommodation/food employment’s high-RMSE-but-high-correlation pattern, as it indicates the donor pool cannot replicate Sector 18’s temporal evolution.

This poor pre-treatment match weakens the credibility of the estimated null effect for Sector 18 revenue (+$0.18M, +0.01σ\sigma). The synthetic control’s failure to track pre-treatment trends means post-treatment comparisons are less reliable for this outcome. However, several factors suggest the null finding is not solely an artifact of poor fit. First, the standardized effect magnitude is very small (+0.01σ\sigma), meaning even if the true effect were somewhat larger, it would remain economically negligible relative to the employment response (+7.59σ\sigma). Second, the separate estimator—which optimizes weights specifically for Sector 18 and is not constrained by common-weight pooling—yields a nearly identical small effect (+$0.21M, Table [6](https://arxiv.org/html/2510.25782v1#S5.T6 "Table 6 ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), suggesting the null finding is robust across estimation approaches. Third, the proposed hotel exemption mechanism predicts minimal Sector 18 effects under the most plausible measurement scenario: if hotels do not report F&B revenue within the retail sales system captured by Sector 18, demand shifts toward hotel venues would increase employment (observable in NAICS 72) without affecting standalone restaurant revenue (Sector 18), producing precisely the observed divergence.

Despite these mitigating factors, I acknowledge the Sector 18 inference is less credible than for other outcomes due to poor pre-treatment fit. Future research with establishment-level data distinguishing hotel-affiliated from standalone food service revenue would provide more reliable measurement of within-sector reallocation and stronger identification of the proposed mechanism.

The accommodation/food employment pattern thus raises a methodological question: should a poor absolute fit (high RMSE) invalidate post-treatment inferences when the synthetic control demonstrably tracks the correct temporal patterns (high correlation)? Two lines of evidence suggest the answer is no in this case. First, the separate estimator—which optimizes weights specifically for this outcome and achieves better overall mean fit (0.752 vs. 0.878)—yields a nearly identical post-treatment effect (+62.34 vs. +67.80 per 1,000; Table [6](https://arxiv.org/html/2510.25782v1#S5.T6 "Table 6 ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). If the average estimator’s large employment effect were an artifact of its poor fit, the separate estimator should produce a radically different estimate. The convergence across independent approaches suggests the employment response is genuine. Second, the effect persists across all six post-treatment quarters (+67.72 to +68.21 per 1,000; Table [7](https://arxiv.org/html/2510.25782v1#S5.T7 "Table 7 ‣ Partial-exposure robustness. ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) rather than exhibiting the volatility expected from random noise.

I interpret the accommodation/food employment finding as reflecting a genuine policy response, with the high RMSE signaling measurement challenges (San Juan’s structural differences) rather than invalidating the counterfactual. The systematic level offset is consistent with the hotel exemption mechanism discussed in Appendix [D.2](https://arxiv.org/html/2510.25782v1#A4.SS2 "D.2 Theoretical Mechanisms ‣ Appendix D Context & Mechanisms ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"): hotels (part of NAICS 72) expanded employment to service exempt demand during restricted hours, creating an employment increase that likely does not appear in standalone restaurant revenue (Sector 18) due to differential measurement coverage across data sources. This within-sector reallocation combined with measurement asymmetry produces exactly the observed pattern: high correlation (both hotels and restaurants respond to common demand shocks) but persistent level differences (hotels gain employment share under the new regulatory environment, but their revenue operates outside the Sector 18 measurement system).

![Refer to caption](figures/compare/pre_treatment_balance.png)


Figure 2: Pre-treatment RMSPE and correlation by outcome for the average estimator. Accommodation/food employment (far right in left panel) exhibits the highest RMSE (6.140) but also the highest correlation (0.928, right panel), indicating systematic level offset rather than random fitting failure.

![Refer to caption](figures/average/gap_preband_late_public_disorder.png)


Figure 3: Pre-treatment gap with ±2​σ\pm 2\sigma band for late-night public disorder.

The concentrated variance structure supports common-weight estimation: with 97.7% of variation captured by five components, the average estimator can exploit shared information while avoiding the overfitting that plagues outcome-specific approaches. I proceed to compare separate versus average estimators in Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

### 5.4 Results: Separate vs Common-Weights (Average) Estimator

Section [5.3](https://arxiv.org/html/2510.25782v1#S5.SS3 "5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") documented strong shared structure across outcomes (94.4% of pre-period variance in four components) and the expected bias–variance tradeoff: the Separate approach achieves 17% better pre-treatment fit (mean RMSPE 0.752 vs. 0.878) than common-weights. Here I assess whether that fit advantage translates into superior treatment-effect estimation and cross-outcome coherence. I take the Average (common-weights) estimator as the primary specification, consistent with MOSC’s recommendation for shared-factor settings and empirically validated through objective-matched inference comparisons (Section [5.5](https://arxiv.org/html/2510.25782v1#S5.SS5 "5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Concatenated and Combined estimators are reported as robustness/sensitivity checks.

#### 5.4.1 Donor Weight Patterns

Common-weights solutions yield transparent, stable synthetic control composition across outcomes, while Separate exhibits outcome-by-outcome fragmentation.

Table 4: Donor weight allocation by estimator

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Donor | Average | Concatenated | Combined | Separate Range |
| Aguadilla | 41.9% | 37.4% | 39.5% | 0.0–100.0 |
| Arecibo | 0.0% | 0.0% | 0.0% | 0.0–85.7 |
| Bayamón | 45.3% | 24.1% | 29.3% | 0.0–98.2 |
| Cayey | 7.8% | 0.0% | 0.0% | 0.0–16.4 |
| Hatillo | 0.0% | 9.0% | 5.1% | 0.0–20.5 |
| Humacao | 5.0% | 29.4% | 26.2% | 0.0–63.0 |

Notes: Weights sum to 1 within each estimator column. The *Separate Range* column shows the minimum and maximum weights each donor receives across the seven outcomes when estimated separately. Common-weight estimators distribute weights across multiple donors (average Neff≈3.1N\_{\text{eff}}\approx 3.1), with Bayamón and Aguadilla receiving primary weights. Donors receiving zero weight in some common-weight estimators are retained to avoid ex-post donor selection.

The common-weight estimators (Average, Concatenated, Combined) are qualitatively similar, primarily combining Aguadilla, Bayamón, and Humacao. By contrast, the *Separate* estimator varies sharply by outcome: different donors dominate different outcomes, undermining cross-outcome interpretation for related sectors.

Table 5: Donor weight comparison across estimators

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Donor | Separate Estimator | | Average Estimator | |
|  | Range | Appears in | Weight | Applies to |
| Aguadilla | 0.0–100.0% | 4/7 outcomes | 41.9% | All outcomes |
| Arecibo | 0.0–85.7% | 1/7 outcomes | 0.0% | All outcomes |
| Bayamón | 0.0–98.2% | 5/7 outcomes | 45.3% | All outcomes |
| Cayey | 0.0–16.4% | 1/7 outcomes | 7.8% | All outcomes |
| Hatillo | 0.0–20.5% | 3/7 outcomes | 0.0% | All outcomes |
| Humacao | 0.0–63.0% | 1/7 outcomes | 5.0% | All outcomes |

Notes: Separate estimator ranges show minimum and maximum weights across seven outcomes. Average estimator applies identical weights to all outcomes. The Separate estimator assigns 100% to Aguadilla for 1 outcome (Sector 18), 85.7% to Arecibo for Sector 14, 98.2% to Bayamón for violent crime, and 63.0% to Humacao for late-night public disorder; remaining outcomes distribute across multiple donors.

This fragmentation hinders cross-outcome comparisons: related outcomes like Sectors 18 and 14 use different synthetic controls, obscuring substitution patterns. The Average estimator’s shared donor allocation leverages the documented low-rank structure to deliver a coherent cross-outcome narrative.

##### Imbalance frontier.

To summarize the trade-off between balancing the concatenated outcomes and the averaged target, I trace the
*imbalance frontier* generated by the combined estimator
Jν​(γ)=ν​qavg​(γ)+(1−ν)​qcat​(γ)J\_{\nu}(\gamma)=\nu\,q\_{\text{avg}}(\gamma)+(1-\nu)\,q\_{\text{cat}}(\gamma).

![Refer to caption](figures/compare/nu_frontier_scatter.png)


Figure 4: Imbalance frontier: qavgq\_{\text{avg}} vs. qcatq\_{\text{cat}} trade-off. Each point shows (qcat​(γ^ν),qavg​(γ^ν))(q\_{\text{cat}}(\hat{\gamma}\_{\nu}),\,q\_{\text{avg}}(\hat{\gamma}\_{\nu})) for ν∈{0,0.25,0.5,0.75,1}\nu\in\{0,0.25,0.5,0.75,1\}, tracing the Pareto frontier of achievable imbalance combinations. The concatenated estimator (ν=0\nu{=}0, red square) minimizes qcatq\_{\text{cat}} at the expense of larger qavgq\_{\text{avg}}; the averaged estimator (ν=1\nu{=}1, green triangle) minimizes qavgq\_{\text{avg}} with moderately higher qcatq\_{\text{cat}}. Intermediate values interpolate smoothly between these extremes. This 2D representation mirrors MOSC’s frontier figure and complements the 1D combined-objective plot reported in Appendix [C.4](https://arxiv.org/html/2510.25782v1#A3.SS4 "C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), (Fig. [A5](https://arxiv.org/html/2510.25782v1#A3.F5 "Figure A5 ‣ Donor weight allocations across 𝜈. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

##### Robustness to donor composition.

Leave-one-donor-out checks (Appendix [C.3](https://arxiv.org/html/2510.25782v1#A3.SS3 "C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), Figure [A1](https://arxiv.org/html/2510.25782v1#A3.F1 "Figure A1 ‣ C.3.1 Leave-One-Donor-Out (LODO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) indicate acceptable stability, with maximum degradation in mean pre-treatment RMSPE of 5.2% when excluding Aguadilla. As a further check, alternative donor pools drawn from the initial similarity screens yield similar allocations. The six-donor pool provides sufficient support without critical dependence on any single municipality.

#### 5.4.2 Treatment Effects and Stability

Table [6](https://arxiv.org/html/2510.25782v1#S5.T6 "Table 6 ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reports post-intervention effects on original outcome scales. Average is the primary specification; Separate is shown for comparison. Effects are reported as post-period means and their across-quarter standard deviations over 2023Q4–2025Q1.

Table 6: Treatment effects by estimator (original scales, post-period 2023Q4–2025Q1)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Separate | | Average | |
| Outcome | Mean Effect | Effect Std | Mean Effect | Effect Std |
| Economic Outcomes ($M per quarter) | | | | |
| Sector 18 (Restaurants/Bars) | 0.17 | 0.06 | 0.18 | 0.07 |
| Sector 14 (Supermarkets/Liquor) | 0.01 | 0.01 | 0.00 | 0.01 |
| Sector 16 (Gas/Convenience) | 0.07 | 0.21 | 0.07 | 0.21 |
| Employment Outcomes (Per 1,000 residents) | | | | |
| Accommodation/Food Employment | 62.34 | 5.18 | 67.80 | 9.30 |
| Arts/Entertainment Employment | −0.08-0.08 | 0.35 | 0.23 | 0.30 |
| Crime Outcomes (Per 1,000 residents) | | | | |
| Late-Night Public Disorder | 0.00 | 0.00 | 0.00 | 0.00 |
| Violent Crime | −0.08-0.08 | 0.09 | −0.08-0.08 | 0.09 |

Notes: Economic outcomes are quarterly revenue in millions of dollars; employment and crime are per 1,000 residents. “Effect Std” is the across-quarter standard deviation during 2023Q4–2025Q1. Values are de-standardized to original units.

Figure [5](https://arxiv.org/html/2510.25782v1#S5.F5 "Figure 5 ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") visualizes Average-estimator treatment effects for key outcomes. Sector 18 (restaurants/bars) shows sustained positive deviations throughout the post-period, mirrored by accommodation/food employment.

![Refer to caption](figures/average/path_plot_revenue_sector18.png)

![Refer to caption](figures/average/path_plot_acc_food_services_avg_emp.png)

Figure 5: Treatment effect trajectories for selected outcomes (Average estimator). Left: Sector 18 revenue (original units). Right: accommodation/food employment (per 1,000). Vertical line marks the intervention (November 9, 2023). Treated values exceed synthetic predictions persistently in the post-period.

##### Interpreting the employment increase.

The large positive employment effect (+67.80 per 1,000, +7.59σ\sigma) may initially appear counterintuitive: why would restricting business hours increase aggregate employment? The ordinance’s institutional details suggest a mechanism, though key measurement assumptions cannot be definitively verified. Article 2.101 explicitly exempts registered hotel guests from late-night alcohol restrictions, creating a regulatory advantage for hotel-affiliated food and beverage operations over standalone bars and restaurants.

The observed employment-revenue divergence—substantial employment increases alongside minimal Sector 18 revenue effects (+0.01σ\sigma)—is consistent with a measurement asymmetry between data sources. The employment outcome (NAICS 72: Accommodation and Food Services) includes both hotels and standalone food establishments, while the revenue outcome (Sector 18: Restaurants & Drinking Places) is based on DDEC retail sales tax reports. I cannot verify from publicly available DDEC documentation whether hotels report food and beverage revenue within this retail sales system. If hotels do not report under Sector 18 (the most plausible interpretation given the retail sales terminology), demand shifts toward exempt hotel venues would increase NAICS 72 employment without appearing in Sector 18 revenue—precisely the observed pattern. If hotels do report under Sector 18, the minimal revenue effect suggests anticipated demand from the exemption did not fully materialize despite the employment expansion. I interpret the divergence under the first scenario: hotels expanded late-night staffing to capture demand displaced from restricted standalone venues, producing an employment increase observable in NAICS 72 but revenue effects unobservable in Sector 18 due to differential measurement coverage. This proposed mechanism, including its data limitations, is detailed in Appendix [D.2.3](https://arxiv.org/html/2510.25782v1#A4.SS2.SSS3 "D.2.3 The Hotel Exemption and Within-Sector Employment Reallocation ‣ D.2 Theoretical Mechanisms ‣ Appendix D Context & Mechanisms ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

##### Post-period uncertainty (all outcomes).

To summarize uncertainty around the Average-estimator treatment paths, Figure [6](https://arxiv.org/html/2510.25782v1#S5.F6 "Figure 6 ‣ Post-period uncertainty (all outcomes). ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") shows the treated–synthetic gap for each outcome with a donor-placebo band shaded *only over the post period* (5–95% range); the vertical line marks the end of the pre period.

![Refer to caption](figures/compare/post_path_uncertainty_revenue_sector18.png)

![Refer to caption](figures/compare/post_path_uncertainty_revenue_sector14.png)

![Refer to caption](figures/compare/post_path_uncertainty_revenue_sector16.png)

![Refer to caption](figures/compare/post_path_uncertainty_acc_food_services_avg_emp.png)

![Refer to caption](figures/compare/post_path_uncertainty_arts_ent_avg_emp.png)

![Refer to caption](figures/compare/post_path_uncertainty_late_public_disorder.png)

![Refer to caption](figures/compare/post_path_uncertainty_all_violent_crime.png)

Figure 6: Post-treatment gap trajectories (Average estimator; all seven outcomes). Each panel plots the treated–synthetic gap across the full time series. The vertical dotted line marks the pre–post cutoff (November 9, 2023). Post-treatment patterns show: persistent positive employment effects (accommodation/food services), near-zero revenue effects across all sectors, minimal crime effects (both violent crime and late-night public disorder), and volatile arts/entertainment employment.

##### Crime outcomes.

Both estimators deliver near-zero average effects for crime. Under Average, late-night public disorder is 0.000820.00082 per 1,000 and violent crime is −0.081-0.081 per 1,000 on average. The convergence across estimators suggests the ordinance’s economic impacts were not accompanied by material changes in reported crime. However, interpretation of the public disorder null requires caution: because Group B offenses are recorded only upon arrest (Section [5.2](https://arxiv.org/html/2510.25782v1#S5.SS2 "5.2 Data, Variables, and Sample Construction ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), this outcome measures enforcement activity rather than total incidents. The null effect could reflect either genuinely unchanged disorder levels or unchanged disorder accompanied by altered police enforcement patterns. The violent crime measure does not face this limitation, as Group A offenses are reported for all incidents regardless of arrest.

##### Partial-exposure robustness.

To guard against partial exposure in 2023Q4, I re-compute post-treatment means excluding that quarter. Table [7](https://arxiv.org/html/2510.25782v1#S5.T7 "Table 7 ‣ Partial-exposure robustness. ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") shows (i) the baseline mean across all six post quarters (2023Q4–2025Q1), (ii) the mean for fully exposed quarters only (Q1 2024–Q1 2025), and (iii) a first-post vs later-post split. Conclusions are unchanged: sectoral gains persist when focusing on fully exposed quarters; crime remains near zero on average.

Table 7: Post-period timing robustness: excluding the partial-exposure quarter (2023Q4), Average estimator

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Outcome | Mean  (All 6Q) | Mean  (Q1’24–Q1’25) | First-post  (Q4’23) | Later-post  Mean |
| Revenues ($M per quarter) and per-capita outcomes (per 1,000) | | | | |
| Sector 18 (Restaurants/Bars) | 0.180.18 | 0.180.18 | 0.180.18 | 0.180.18 |
| Sector 14 (Supermarkets/Liquor) | 0.000.00 | 0.000.00 | 0.010.01 | 0.000.00 |
| Sector 16 (Gas/Convenience) | 0.070.07 | 0.090.09 | −0.03-0.03 | 0.090.09 |
| Accommodation/Food Employment | 67.8067.80 | 67.7267.72 | 68.2168.21 | 67.7267.72 |
| Arts/Entertainment Employment | 0.230.23 | 0.190.19 | 0.440.44 | 0.190.19 |
| Late-Night Public Disorder | 0.000.00 | 0.000.00 | 0.010.01 | 0.000.00 |
| Violent Crime | −0.08-0.08 | −0.10-0.10 | −0.01-0.01 | −0.10-0.10 |

Notes: Means are computed on original scales. “All 6Q” averages over 2023Q4–2025Q1; “Q1’24–Q1’25” excludes 2023Q4; “First-post” is 2023Q4; “Later-post” averages 2024Q1–2025Q1.

#### 5.4.3 Cross-Outcome Coherence

The Average estimator identifies a consistent cross-outcome pattern: Sector 18 (restaurants/bars) and Sector 16 (gas/convenience) show positive mean increases, while Sector 14 (supermarkets/liquor) shows small positive effects. Employment rises in accommodation/food services (67.8 per 1,000 on average) and modestly in arts/entertainment (0.23 per 1,000). Crime effects remain near zero: late-night public disorder averages 0.000820.00082 per 1,000 and violent crime averages −0.081-0.081 per 1,000. Figure [7](https://arxiv.org/html/2510.25782v1#S5.F7 "Figure 7 ‣ 5.4.3 Cross-Outcome Coherence ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") summarizes the temporal profile across all outcomes.

![Refer to caption](figures/average/gap_heatmap.png)


Figure 7: Treatment effects heatmap (Average estimator) on original scales, 2023Q4–2025Q1. Positive effects concentrate in targeted economic sectors with persistent employment gains; crime remains near zero throughout.

#### 5.4.4 Methodological Implications

The comparative analysis highlights the bias–variance tradeoff. While Separate attains slightly better pre-treatment fit, the Average estimator—leveraging shared low-rank structure (94.4% of variance in four components)—delivers (i) coherent donor selection, (ii) stable, interpretable cross-outcome mechanisms (e.g., venue substitution across alcohol-related sectors), and (iii) small-crime-effect conclusions that are consistent across aggregation choices. In this setting, the modest fit sacrifice relative to Separate is compensated by gains in interpretability and stability that matter for multi-outcome policy evaluation.

#### 5.4.5 Estimator Comparison: Gap Trajectories

Figure [8](https://arxiv.org/html/2510.25782v1#S5.F8 "Figure 8 ‣ 5.4.5 Estimator Comparison: Gap Trajectories ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents treatment effect trajectories (gaps between treated and synthetic outcomes) across all four estimators for all seven outcomes. The common-weight estimators (Average, Concatenated, Combined) track together closely in both pre- and post-treatment periods, while the Separate estimator shows outcome-specific divergence. This visual comparison validates the theoretical prediction: common weights leverage shared structure to deliver stable, coherent estimates, whereas outcome-specific optimization introduces estimator-dependent variation that complicates cross-outcome interpretation.

![Refer to caption](figures/compare/compare_gaps_revenue_sector18.png)

![Refer to caption](figures/compare/compare_gaps_revenue_sector14.png)

![Refer to caption](figures/compare/compare_gaps_revenue_sector16.png)

![Refer to caption](figures/compare/compare_gaps_acc_food_services_avg_emp.png)

![Refer to caption](figures/compare/compare_gaps_arts_ent_avg_emp.png)

![Refer to caption](figures/compare/compare_gaps_late_public_disorder.png)

![Refer to caption](figures/compare/compare_gaps_all_violent_crime.png)

Figure 8: Gap trajectories across estimators (all seven outcomes). Each panel compares Separate, Average, Concatenated, and Combined estimators plus a uniform-weights baseline. Gaps are “Observed −- Synthetic”; the vertical dotted line marks the treatment (November 9, 2023). Common-weight estimators converge in post-treatment trajectories, while Separate shows outcome-specific variation. Pre-treatment gaps near zero for all estimators confirm adequate fit quality.

### 5.5 Inference and Sensitivity

Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") documented economically meaningful effects across outcome domains. I now assess statistical significance using joint conformal inference and permutation-based placebo tests.

Implementation detail. Following MOSC, for each candidate null I enforce the null on the treated unit, augment the sample to include the post period under that null, and *re-estimate donor weights using the same objective as in estimation*. In the implementation used for the main results, this objective is *averaged* (hard-coded), with identical preprocessing across procedures: pre-period intercept shift (demeaning within unit–outcome), outcome-wise scaling by the treated unit’s pre-period standard deviation, and sign alignment applied after scaling.

##### Maintained assumptions for inference validity.

Both inference procedures require specific conditions on the data-generating process and estimator properties:

1. A1.

   Permutation test validity (Abadie, [2021](https://arxiv.org/html/2510.25782v1#bib.bib3)): The treated unit and donor pool are exchangeable under the null hypothesis of no treatment effect. This requires that (i) assignment is as-if random conditional on pre-treatment covariates, and (ii) no donor is systematically selected on anticipated treatment effects. I approximate exchangeability through the donor screening protocol (Appendix [A](https://arxiv.org/html/2510.25782v1#A1 "Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), which selects municipalities with similar economic structure, population size, and pre-treatment outcome trajectories.
2. A2.

   Conformal inference validity (Chernozhukov et al., [2021](https://arxiv.org/html/2510.25782v1#bib.bib13); Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)): Asymptotic validity requires (i) the synthetic control estimator is consistent for the counterfactual when re-estimated on the augmented sample including the post-treatment period under the null, and (ii) sufficient pre-treatment periods relative to the donor pool size (T0=19T\_{0}=19 quarters; N0=6N\_{0}=6 donors). Finite-sample coverage relies on exchangeability of residuals under the fitted model.
3. A3.

   Error structure: Outcome residuals (gaps between treated and synthetic predictions) satisfy (i) limited cross-outcome correlation—validated in Table [2](https://arxiv.org/html/2510.25782v1#S5.T2 "Table 2 ‣ Cross-outcome error correlation. ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), which shows mean absolute correlation |ρ|=0.34|\rho|=0.34 with no pair exceeding 0.93—supporting the 1/K1/\sqrt{K} efficiency gains from averaging (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)), and (ii) sub-Gaussian tails or bounded moments for concentration inequalities.
4. A4.

   Low-rank structure: The treated unit’s latent trajectory lies within the span of the donor pool’s factor space (Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Section [5.3](https://arxiv.org/html/2510.25782v1#S5.SS3 "5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") validates this empirically: five singular components capture 97.7% of pre-treatment variance, supporting common-weight constraints that balance all outcomes simultaneously.

Under these conditions, the permutation test provides valid finite-sample inference when assignment is randomized (or as-if random), while conformal inference offers asymptotic guarantees even without randomization, at the cost of stronger consistency requirements. I report results from both procedures to provide complementary evidence.

#### 5.5.1 Inference Results: Effect Sizes and Statistical Significance

Statistical inference for multi-outcome synthetic control faces inherent power limitations in small-sample settings. With six donors, the minimum attainable permutation pp-value is 1/14≈0.0711/14\approx 0.071, yielding a coarse discrete grid where conventional thresholds (α=0.05\alpha=0.05) are unattainable. By contrast, the joint-KK conformal test with T0=19T\_{0}=19 pre-periods has a minimum p=1/(T0+1)=1/20=0.05p=1/(T\_{0}{+}1)=1/20=0.05. In light of these constraints, I emphasize effect sizes alongside pp-values, following Abadie ([2020](https://arxiv.org/html/2510.25782v1#bib.bib2)) that substantive magnitudes can be informative even absent statistical rejection.

##### Effect size context.

Table [8](https://arxiv.org/html/2510.25782v1#S5.T8 "Table 8 ‣ Effect size context. ‣ 5.5.1 Inference Results: Effect Sizes and Statistical Significance ‣ 5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reports treatment effects in original and standardized units, providing the magnitude context needed to interpret statistical tests (Average/common-weights estimator).

Table 8: Treatment effect magnitudes and standardized units (Average estimator)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Outcome | Mean Effect | Std. Effect | Pre-Treatment SD | Domain |
| Sector 18 (Restaurants/Bars) | +$0.179M | +0.01​σ+0.01\sigma | $0.02M | Economic |
| Sector 14 (Supermarkets/Liquor) | +$0.003M | +0.00​σ+0.00\sigma | $0.01M | Economic |
| Sector 16 (Gas/Convenience) | +$0.067M | +0.02​σ+0.02\sigma | $0.01M | Economic |
| Accommodation/Food Emp. | +67.80 | +7.59​σ+7.59\sigma | 8.93 | Economic |
| Arts/Entertainment Emp. | +0.23 | +0.32​σ+0.32\sigma | 0.71 | Economic |
| Late Public Disorder | +0.00+0.00 | +0.01​σ+0.01\sigma | 0.07 | Crime |
| Violent Crime | −0.08-0.08 | −0.26​σ-0.26\sigma | 0.31 | Crime |

Notes: Mean Effect averages across six post-treatment quarters (2023Q4–2025Q1). Std. Effect expresses magnitude relative to San Juan’s pre-treatment SD (σ\sigma). Revenue outcomes (Sectors 14, 16, 18) are quarterly revenue in millions of dollars; employment and crime are per 1,000 residents. Employment shows the largest standardized responses; revenue and crime effects remain near zero in standardized terms.

33footnotetext: Value rounds to $0.00000M; exact implied mean ≈\approx $0.0000025M ($2.50).

Employment outcomes exhibit the largest standardized effects: accommodation/food employment shows +7.59​σ+7.59\sigma and arts/entertainment employment shows +0.32​σ+0.32\sigma. Revenue outcomes are small in standardized terms: Sector 18 at +0.01​σ+0.01\sigma, Sector 16 at +0.02​σ+0.02\sigma, and Sector 14 near zero at +0.00​σ+0.00\sigma. Crime outcomes show minimal effects: late-night public disorder at +0.01​σ+0.01\sigma and violent crime at −0.26​σ-0.26\sigma. The employment responses are substantively meaningful, indicating measurable labor-market adjustments to the ordinance, while revenue and crime effects remain near zero in standardized terms.

##### Formal statistical tests.

I construct 13 placebos total for permutation inference: 6 donor-unit placebos plus 7 in-time placebos (treating pre-treatment periods as pseudo-intervention dates), yielding minimum attainable two-sided pp-value of 1/14≈0.0711/14\approx 0.071 (construction details in Appendix [C.5](https://arxiv.org/html/2510.25782v1#A3.SS5 "C.5 Placebo Distribution Details ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Table [9](https://arxiv.org/html/2510.25782v1#S5.T9 "Table 9 ‣ Formal statistical tests. ‣ 5.5.1 Inference Results: Effect Sizes and Statistical Significance ‣ 5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reports pp-values from the joint conformal and permutation procedures, together with their discrete grid structures.

The joint conformal test yields p=0.600p=0.600, failing to reject the null at conventional levels. *The conformal rank is 1212 out of 2020 (exact p=0.600p=0.600, mid-p=0.575p=0.575).* The permutation RMSPE test yields p=0.071p=0.071, approaching but not surpassing the minimum achievable pp-value of 1/141/14. San Juan’s RMSPE ratio of 3.983.98 ranks first among the 14 units (6 donors + 7 in-time placebos + treated unit), but the discrete grid structure limits formal significance. An alternate median-based statistic focusing on the first post period yields p=0.286p=0.286, well above conventional significance thresholds. These results suggest effects are present—particularly in employment outcomes—but the small donor pool constrains statistical power.

Table 9: Statistical test results and discrete pp-value grid

|  |  |  |  |
| --- | --- | --- | --- |
| Test Method | pp-value | Null Hypothesis | Grid Structure |
| Joint-KK Conformal | 0.600 | Sharp null: zero effects on all outcomes | 1/20,2/20,…1/20,2/20,\ldots |
| Permutation (RMSPE) | 0.071 | Placebo exchangeability | 1/14,2/14,…1/14,2/14,\ldots |
| Permutation (Median) | 0.286 | Placebo exchangeability | 1/14,2/14,…1/14,2/14,\ldots |

Notes: Conformal test uses the first post period and the L1/KL\_{1}/\sqrt{K} joint score with T0=19T\_{0}=19 pre-periods (minimum p=1/(T0+1)=0.05p=1/(T\_{0}{+}1)=0.05). Permutation tests use 6 donor placebos + 7 in-time placebos + 1 treated unit =14=14 total (minimum p=1/14≈0.071p=1/14\approx 0.071). The RMSPE statistic aggregates gaps across outcomes over the first HH post periods (here H=5H=5); the *Median* statistic uses the median across outcomes in the first post period (2023Q4). For the conformal test, the rank is 1212 of 2020 (mid-p=0.575p=0.575).

The joint conformal test yields p=0.600p=0.600, failing to reject the null at conventional levels. The permutation RMSPE test yields p=0.071p=0.071, approaching but not surpassing the minimum achievable pp-value of 1/141/14. San Juan’s RMSPE ratio of 3.983.98 ranks first among the 14 units (6 donors + 7 in-time placebos + treated unit), but the discrete grid structure limits formal significance. An alternate median-based statistic focusing on the first post period yields p=0.286p=0.286, well above conventional significance thresholds. These results suggest effects are present—particularly in employment outcomes—but the small donor pool constrains statistical power.

##### Objective diagnostics (Average vs. Concatenated).

The pre-treatment diagnostics indicate strong shared factor structure, for which MOSC recommends the *Average* objective as the default. Condition-number and RMSPE summaries can nonetheless favor *Concatenated* due to Jensen’s inequality even when averaging is theoretically appropriate. To probe whether this is a substantive concern, I compute first-post joint-KK conformal tests under both objectives. Results are similar and non-rejecting: the *Average* objective yields rank 12/2012/20 (exact p=0.600p=0.600, mid-p=0.575p=0.575), while the *Concatenated* objective yields rank 13/2013/20 (exact p=0.650p=0.650, mid-p=0.625p=0.625). These concordant outcomes support using *Average* as the primary specification, consistent with the low-rank diagnostics.

Table 10: Joint-KK conformal results by objective (first post period)

|  |  |  |  |
| --- | --- | --- | --- |
| Objective | Rank (/20/20) | pexactp\_{\text{exact}} | pmidp\_{\text{mid}} |
| Average | 1212 | 0.6000.600 | 0.5750.575 |
| Concatenated | 1313 | 0.6500.650 | 0.6250.625 |

Notes: Concatenated-objective outputs from the conformal routine: rank 13/2013/20, pexact=0.650p\_{\text{exact}}=0.650, pmid=0.625p\_{\text{mid}}=0.625, first-post date 2023Q4.

##### Robustness to objective weighting (ν\nu).

The combined estimator nests concatenated (ν=0\nu=0) and averaged (ν=1\nu=1) objectives as special cases. I evaluate sensitivity by estimating across a grid ν∈{0,0.25,0.5,0.75,1.0}\nu\in\{0,0.25,0.5,0.75,1.0\} and assessing stability of treatment effects and placebo rankings. *Inference is computed with the averaged objective for conformal and for permutation re-fits, so reported pp-values are invariant to ν\nu by construction; the ν\nu-grid is used for effect-size robustness.* Treatment magnitudes are qualitatively stable: accommodation/food employment ranges from +6.45​σ+6.45\sigma (ν=0\nu=0) to +7.59​σ+7.59\sigma (ν=1.0\nu=1.0), while crime outcomes remain near zero across all specifications. The employment–revenue divergence pattern persists for all ν\nu.

For transparency, I report the averaged objective as the *baseline specification* to align estimation and inference. Figure [A4](https://arxiv.org/html/2510.25782v1#A3.F4 "Figure A4 ‣ Treatment effect stability across 𝜈. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") plots treatment effects across ν\nu with placebo bands, demonstrating stability.

##### Power and interpretation.

Failure to reject does *not* imply a zero effect. With only six donors, the discrete permutation grid and small N0N\_{0} limit power even for moderate effects. The observed employment effects (+7.59​σ+7.59\sigma for accommodation/food; +0.32​σ+0.32\sigma for arts/entertainment) are substantively meaningful even without conventional statistical significance, indicating measurable labor-market responses to the ordinance. Revenue and crime effects remain near zero in both absolute and standardized terms.

![Refer to caption](figures/compare/permutation_plot.png)


Figure 9: Permutation placebo distribution. San Juan’s RMSPE ratio (3.98) ranks first among 14 units (6 donors + 7 in-time placebos + treated), providing descriptive evidence of a notable effect. The permutation test yields p=0.071p=0.071, the minimum achievable value on the 1/141/14 grid.

##### Bottom line.

Statistical tests do not reject the null, reflecting the fundamental power limitations imposed by a small donor pool (coarse permutation grid 1/141/14; conformal p=0.600p=0.600; permutation RMSPE p=0.071p=0.071). While failure to reject does not imply absence of effects, the statistical evidence alone cannot support strong causal claims. Descriptively, employment shows large standardized effects (accommodation/food +7.59​σ+7.59\sigma; arts/entertainment +0.32​σ+0.32\sigma), while revenue effects are near zero in standardized terms (≈0.00​σ\approx 0.00\sigma to 0.02​σ0.02\sigma). Crime remains minimal (violent −0.26​σ-0.26\sigma, late-night disorder +0.01​σ+0.01\sigma). These patterns are consistent with the proposed hotel exemption mechanism, but definitive causal identification would require a larger donor pool or longer post-treatment period.

## 6 Discussion and Conclusion

I implement and assess the multi-outcome synthetic control (MOSC) framework of Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)), addressing interpretability and statistical challenges when interventions affect multiple related outcomes. Through an empirical application to San Juan, Puerto Rico’s 2023 Public Order Code, I show how common-weight approaches can deliver methodological advantages over outcome-specific estimation when the data exhibit the necessary shared structure.

### 6.1 Summary of Key Findings

The rank diagnostics (Section [5.3](https://arxiv.org/html/2510.25782v1#S5.SS3 "5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) support low-rank structure: four components explain 94.4% of systematic variation with a clear elbow in the scree plot. My analysis yields economically meaningful effects in targeted sectors—accommodation/food services employment +7.59σ\sigma—alongside small revenue effects: restaurants/bars +0.01σ\sigma, gasoline/convenience stores +0.02σ\sigma. Crime effects remain near zero: late-night public disorder (+0.01σ\sigma) and violent crime (−0.26​σ-0.26\sigma). The public disorder measure reflects arrests rather than total incidents, limiting causal interpretation of this null finding. The divergence between economic response and public safety outcomes illustrates the value of multi-outcome evaluation: hour-based restrictions generated measurable sectoral adjustments, with crime patterns showing more variability than originally anticipated as a policy objective.

### 6.2 Methodological Contributions

My findings demonstrate that common-weight estimation can improve policy evaluation when outcomes share underlying structure. As shown in Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), the Average estimator provides coherent cross-outcome interpretation and unified donor selection at an ≈\approx17% pre-treatment fit cost—a worthwhile tradeoff when low-rank structure is present (94.4% variance in four components), reflecting the bias-variance considerations formalized in Appendix [B.3](https://arxiv.org/html/2510.25782v1#A2.SS3 "B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

##### Understanding the tradeoff.

This tradeoff illustrates the core tension: exploiting shared structure pools information but exposes the estimator to error propagation from noisy outcomes (see Appendix [B.3](https://arxiv.org/html/2510.25782v1#A2.SS3 "B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

#### 6.2.1 When to Apply Common-Weight Methods

I recommend that researchers routinely examine scree plots and cumulative variance profiles before choosing between separate and common-weight estimation strategies. Applications where the first three to four components explain over 90% of systematic variation represent strong candidates for common-weight approaches. However, researchers should avoid common weights when outcomes exhibit heterogeneous data quality, when shared factor structure is sharply violated (flat scree plots), or when policy theory suggests genuinely independent causal mechanisms operating on different outcomes.

### 6.3 Policy Implications

The contrast between economic responses and public safety outcomes illustrates why interpretability matters for evidence-based policymaking. Traditional outcome-specific evaluation might conclude either that the policy had no effects (missing economic adjustments) or that economic changes indicated success (missing the absent crime reduction). The Average estimator’s comprehensive detection enables a more nuanced interpretation: the observed patterns suggest economic adjustments in targeted sectors without corresponding changes in public safety outcomes. While causal inference is limited by statistical power, these patterns are consistent with the hypothesis that hour-based restrictions may be insufficient for addressing underlying determinants of public disorder in this context, and point toward complementary strategies that target behavior directly or address underlying risk factors.

The inference results (Section [5.5](https://arxiv.org/html/2510.25782v1#S5.SS5 "5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) illustrate the complex relationship between statistical evidence and policy decision-making. Following Abadie ([2020](https://arxiv.org/html/2510.25782v1#bib.bib2)), who cautions against relying on statistical significance alone and recommends assessing magnitude/precision, plausibility, and design quality, I also examine temporal patterns and cross-outcome consistency alongside formal tests. The observed permutation pp-value of 0.071 (the minimum achievable with 13 placebos; see Section [4](https://arxiv.org/html/2510.25782v1#S4 "4 Multi-Outcome Synthetic Control: Inference ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) reflects the fundamental tradeoff between donor pool size and donor quality inherent to synthetic control applications in small jurisdictions. An alternate median-based statistic focusing on the first post-period yields p=0.286p=0.286, providing more conservative evidence.

### 6.4 Limitations

Despite these contributions, my analysis faces several important limitations. The most significant concern is statistical power: the small donor pool constrains formal tests (minimum permutation pp-value of 1/14≈0.0711/14\approx 0.071; see Section [4](https://arxiv.org/html/2510.25782v1#S4 "4 Multi-Outcome Synthetic Control: Inference ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). While statistical tests do not reject the null at conventional levels, several lines of evidence are consistent with economically meaningful effects: the permutation test achieves its minimum attainable pp-value (p=0.071p=0.071), the employment effect is large in magnitude (+7.59​σ7.59\sigma), and the proposed mechanism (the hotel exemption combined with differential measurement coverage) provides a plausible institutional explanation for the employment-revenue divergence. However, the limited donor pool prevents definitive causal claims, and I interpret the findings as providing suggestive evidence that (a) demonstrates the multi-outcome synthetic control methodology in a realistic policy setting, (b) identifies an institutional mechanism worthy of further investigation with richer data, and (c) documents economically meaningful short-run patterns whose causal interpretation awaits replication with larger samples or longer time series. The six-quarter post-treatment window may miss longer-run adjustments, and the Puerto Rico municipal context may limit external validity. In light of concerns that researcher degrees of freedom can inflate false positives, I restrict flexibility and use common procedures across outcomes to discipline specification search (Brodeur et al., [2020](https://arxiv.org/html/2510.25782v1#bib.bib11)). Recognizing evidence of a “null result penalty,” I report and archive all estimates and robustness checks to enhance transparency (Abadie, [2020](https://arxiv.org/html/2510.25782v1#bib.bib2); Chopra et al., [2022](https://arxiv.org/html/2510.25782v1#bib.bib14)). Finally, while limited power reduces precision, transparently reporting (as-precise-as-feasible) nulls remains policy-relevant in dynamic environments where future signals are noisy (Abadie, [2020](https://arxiv.org/html/2510.25782v1#bib.bib2); Frankel and Kasy, [2022](https://arxiv.org/html/2510.25782v1#bib.bib20)).

The robustness analyses (Section [5.5](https://arxiv.org/html/2510.25782v1#S5.SS5 "5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") and Appendix [C](https://arxiv.org/html/2510.25782v1#A3 "Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) demonstrate that my central narrative—activation of economic mechanisms without commensurate crime reductions—remains stable across alternative pre-treatment windows, estimator choices, and leave-one-out specifications. An important caveat concerns the Sector 18 (restaurants/bars) revenue outcome: the pre-treatment correlation between San Juan and its synthetic control is negative (ρ=−0.40\rho=-0.40), indicating poor trend alignment (Section [5.3](https://arxiv.org/html/2510.25782v1#S5.SS3 "5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). While this limits confidence in the counterfactual for this specific outcome, the null revenue effect is consistent with the proposed hotel exemption mechanism (Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), and the separate-SCM estimator independently yields a null effect for this sector, providing corroborating evidence. However, my design cannot isolate individual-level behavioral mechanisms with available data, and the focus on San Juan restricts generalizability. Future work using longer panels, expanded geographic coverage, and micro-level data would strengthen these conclusions.

### 6.5 Conclusion

This paper demonstrates that multi-outcome synthetic control methods can address important interpretability challenges in policy evaluation when appropriate structural conditions are satisfied. Through diagnostic assessment of low-rank structure, researchers can identify settings where common-weight approaches enable comprehensive evaluation capturing both mechanism implementation and goal achievement. The distinction between intermediate mechanism detection and ultimate outcome assessment suggests that evaluation frameworks should systematically examine both dimensions.

The success of common-weight estimation in my municipal policy application suggests broader potential across diverse evaluation contexts, including education interventions affecting multiple outcomes, health policies with multiple clinical endpoints, and labor market interventions affecting employment and wages across sectors. Looking forward, integrating multi-outcome methods with recent synthetic control innovations—including machine learning approaches and robust inference procedures—offers promising avenues for enhancing policy evaluation practice. By prioritizing interpretability alongside statistical rigor, multi-outcome synthetic control methods can enhance the practical utility of causal inference for evidence-based policy while maintaining methodological standards necessary for credible evaluation research.

Replication materials, including complete code and data construction protocols, are available from the author upon request and will be posted to a public repository upon publication.

##### AI Disclosure.

During the preparation of this work the author used Claude (Anthropic) in order to generate Python code for all data processing, statistical analysis, and visualization presented in this paper. After using this tool, the author reviewed and edited the code as needed and takes full responsibility for the content of the publication.

## Online Appendix

## Appendix A Data Construction & Donor Pool Screening

This appendix details the data sources, outcome construction, and donor pool screening methodology underlying my multi-outcome synthetic control analysis. I implement a rigorous six-stage screening protocol to construct a donor pool that is demographically comparable, economically similar, free from pre-treatment contamination, and exhibits parallel trends with San Juan across multiple outcome domains. This ex ante design-stage screening ensures that synthetic control weights are estimated on a theoretically valid and structurally comparable set of municipalities.

### A.1 Data Sources & Temporal Coverage

My analysis integrates three primary data sources spanning 2019 Q1 through 2025 Q1 (25 quarters: 19 pre-treatment, 6 post-treatment). The treatment date is November 9, 2023, placing 2023 Q4 as the first post-treatment quarter with partial exposure (seven weeks of the thirteen-week quarter).

##### Monthly retail revenue data.

The Puerto Rico Department of Economic Development and Commerce (DDEC) compiles monthly retail sales data by municipality and sector from Sales and Use Tax (IVU) records (Gobierno de Puerto Rico, Departamento de Desarrollo Económico y
Comercio, Secretaría Auxiliar de Sectores Estratégicos, Oficina de
Estrategia e Inteligencia de Negocios, [2025](https://arxiv.org/html/2510.25782v1#bib.bib21)). The dataset covers approximately 45,000 retail businesses across 18 NAICS-based sectors from January 2019 through March 2025. I extract raw revenue levels for three policy-relevant sectors: Sector 14 (supermarkets and liquor stores: NAICS 4451, 4453), Sector 16 (gasoline stations and convenience stores: NAICS 447, 4471), and Sector 18 (restaurants and drinking places: NAICS 722). Monthly revenues are summed within calendar quarters to create quarterly series. For analysis, I convert these raw revenues to island-wide shares (see Section [A.2.1](https://arxiv.org/html/2510.25782v1#A1.SS2.SSS1 "A.2.1 Revenue Outcomes: Island-Wide Shares (Option A) ‣ A.2 Outcome Variable Construction ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") below).

##### Quarterly employment data.

The Puerto Rico Department of Labor and Human Resources (DTRH) publishes quarterly establishment-level employment and salary data derived from employer reports under the Employment Security Law (Gobierno de Puerto Rico, Departamento del Trabajo y Recursos
Humanos, [2023](https://arxiv.org/html/2510.25782v1#bib.bib24)). I use average quarterly employment for two sectors: NAICS 72 (Accommodation and Food Services) and NAICS 71 (Arts, Entertainment, and Recreation). Employment figures reflect workers at establishments located within each municipality, regardless of workers’ residence. I convert raw employment counts to per-capita rates (per 1,000 residents) for comparability across municipalities.

##### NIBRS crime data.

The Puerto Rico Police Department reports crime incidents through the National Incident-Based Reporting System (NIBRS), with incident-level data including offense type, date, time, and location. I construct two crime measures: late-night public disorder arrests (occurring during restricted hours) and all-hours violent crime. Incidents are classified by time window at the incident level before quarterly aggregation. NIBRS reporting requirements specify that incidents are recorded by the jurisdiction where they occur (Gobierno de Puerto Rico, Departamento de Seguridad Pública,
Negociado de la Policía de Puerto Rico, [2020](https://arxiv.org/html/2510.25782v1#bib.bib22)). I convert raw incident counts to per-capita rates (per 1,000 residents) for cross-municipality comparability.

##### Temporal harmonization.

All data sources are aggregated or aligned to calendar quarters using quarter-end dates (March 31, June 30, September 30, December 31). This quarterly frequency balances temporal resolution with data quality, minimizing missing observations while preserving sufficient time-series variation for synthetic control estimation.

### A.2 Outcome Variable Construction

My analysis employs seven outcome variables spanning three policy-relevant domains: economic activity (revenue), crime, and employment. The choice of normalization differs by outcome domain to address distinct measurement and interpretation concerns.

#### A.2.1 Revenue Outcomes: Island-Wide Shares (Option A)

Revenue outcomes use island-wide share metrics rather than raw levels or per-capita rates. For each municipality ii, sector s∈{14,16,18}s\in\{14,16,18\}, and quarter tt, I construct:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sharei​s​t=Revenuei​s​t∑j∈PRRevenuej​s​t,\text{Share}\_{ist}\;=\;\frac{\text{Revenue}\_{ist}}{\sum\_{j\in\text{PR}}\text{Revenue}\_{jst}}, |  | (5) |

where the denominator sums over all Puerto Rican municipalities. This share metric captures each municipality’s position in the island’s sectoral economy.

##### Rationale for island-wide shares.

The island-wide share specification offers several advantages over alternative normalizations for revenue outcomes:

Theoretical advantages:

* •

  Common denominator: The island-wide total provides a natural scale-free metric that controls for aggregate economic fluctuations, inflation, and seasonal patterns affecting all municipalities
* •

  Zero-sum dynamics: Changes in one municipality’s share directly reflect relative gains or losses against the rest of Puerto Rico, making the counterfactual interpretation natural
* •

  Policy interpretation: The treatment effect on share captures San Juan’s changing competitive position in the island’s nightlife economy, which is the policy-relevant object
* •

  Regional hub spillovers: Unlike per-capita rates, shares avoid confounding treatment effects with cross-border consumption by non-residents, which is particularly relevant for San Juan as a regional entertainment destination

Practical advantages:

* •

  Stability: Island-wide denominators are less susceptible to local measurement error than municipal-level population denominators
* •

  Comparability: Shares naturally account for municipality size without requiring additional per-capita adjustments
* •

  Bounded support: Share values lie in [0,1][0,1], providing well-behaved numerical properties for optimization

The intercept-shifted estimation approach (see Section [3.3](https://arxiv.org/html/2510.25782v1#S3.SS3 "3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") in main text) removes municipality-specific level differences by demeaning each series by its pre-treatment mean before optimization. Subsequent standardization by the treated unit’s pre-treatment standard deviation ensures comparability across outcomes for common-weight estimation. This transformation sequence—shares →\to demean →\to standardize—preserves temporal dynamics while handling scale appropriately for the shared factor framework.

#### A.2.2 Employment & Crime: Per-Capita Rates

Employment and crime outcomes use conventional per-capita standardization where population denominators are policy-relevant and less susceptible to regional-hub spillover concerns that affect revenue measures.

For employment, I construct

|  |  |  |  |
| --- | --- | --- | --- |
|  | Employmenti​t​kpc=Average Employmenti​t​kPopulationi/1000for ​k∈{NAICS 71, NAICS 72}.\text{Employment}\_{itk}^{\text{pc}}\;=\;\frac{\text{Average Employment}\_{itk}}{\text{Population}\_{i}/1000}\quad\text{for }k\in\{\text{NAICS 71, NAICS 72}\}. |  | (6) |

For crime, I construct

|  |  |  |  |
| --- | --- | --- | --- |
|  | Crimei​t​kpc=Incident Counti​t​kPopulationi/1000for ​k∈{Late Disorder, Violent}.\text{Crime}\_{itk}^{\text{pc}}\;=\;\frac{\text{Incident Count}\_{itk}}{\text{Population}\_{i}/1000}\quad\text{for }k\in\{\text{Late Disorder, Violent}\}. |  | (7) |

Population denominators use 2023 Census American Community Survey 5-year estimates for all municipalities, treating population as fixed over the study window to avoid confounding treatment effects with measurement changes in the denominator. The per-1,000-residents scaling facilitates interpretation and aligns with policy evaluation conventions in crime and employment domains.

#### A.2.3 Late-Night Time Window Definition

The Public Order Code restricts on-premise alcohol sales during specific late-night hours: 1:00–6:00 AM on weekdays and 2:00–6:00 AM on weekends. For crime incident classification, I define late-night public disorder as arrests occurring within these restricted windows. The ordinance specifies that Monday legal holidays follow the weekend schedule (2:00–6:00 AM). Twelve Monday holidays occur during the post-treatment period (2023: December 25; 2024: January 1, January 15, February 19, May 27, September 2, October 14, November 11; 2025: January 6, January 20, February 17, March 3), representing a one-hour classification difference affecting 12/548 days ≈\approx 2.2% of post-period observations. I implement this distinction in the time-window logic, applying 2:00–6:00 AM restrictions to post-intervention holiday Mondays and 1:00–6:00 AM restrictions to all other weekdays.

### A.3 Six-Stage Donor Pool Screening

I implement a comprehensive six-stage screening protocol to construct a donor pool that satisfies the theoretical requirements for valid synthetic control estimation while maintaining adequate pool size for inference. The screening proceeds sequentially, with each stage filtering municipalities based on progressively more stringent criteria related to comparability, data quality, and structural stability.

#### A.3.1 Stage 1: Demographic & Socioeconomic Similarity

The initial stage filters all 77 Puerto Rican municipalities (excluding San Juan) to retain those demographically and socioeconomically similar to the treated unit. Following guidance to select comparable, uncontaminated donors (Abadie, [2021](https://arxiv.org/html/2510.25782v1#bib.bib3)), I implement tolerance bounds based on the cross-sectional distribution of municipal characteristics.

##### Data and features.

I use U.S. Census Bureau American Community Survey 5-year estimates (2019–2023) (U.S. Census Bureau, [2023](https://arxiv.org/html/2510.25782v1#bib.bib36)) for five demographic and socioeconomic indicators: median age, share of population aged 18–34, poverty rate, median household income, and share of housing units that are renter-occupied multi-family dwellings. Let X=[xi​j]∈ℝn×pX=[x\_{ij}]\in\mathbb{R}^{n\times p} denote the feature matrix, where n=78n=78 municipalities and p=5p=5 features, with xbx\_{b} denoting San Juan’s feature vector.

##### Statistical bounds.

For each feature jj, I compute the standard deviation across all municipalities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σj=1n−1​∑i=1n(xi​j−x¯j)2.\sigma\_{j}\;=\;\sqrt{\frac{1}{n-1}\sum\_{i=1}^{n}(x\_{ij}-\bar{x}\_{j})^{2}}. |  | (8) |

Tolerance bounds are established at ±1\pm 1 standard deviation around San Juan’s value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [Lowerj,Upperj]=[xb,j−σj,xb,j+σj].[\text{Lower}\_{j},\text{Upper}\_{j}]\;=\;[x\_{b,j}-\sigma\_{j},\,x\_{b,j}+\sigma\_{j}]. |  | (9) |

##### Similarity screening.

A municipality passes feature jj if xi​j∈[Lowerj,Upperj]x\_{ij}\in[\text{Lower}\_{j},\text{Upper}\_{j}]. The total number of passing features for municipality ii is Si=∑j=1p𝟙​{xi​j∈[Lowerj,Upperj]}S\_{i}=\sum\_{j=1}^{p}\mathbb{1}\{x\_{ij}\in[\text{Lower}\_{j},\text{Upper}\_{j}]\}. I retain municipalities with Si≥4S\_{i}\geq 4 (passing at least four of five criteria).

Table [A1](https://arxiv.org/html/2510.25782v1#A1.T1 "Table A1 ‣ Similarity screening. ‣ A.3.1 Stage 1: Demographic & Socioeconomic Similarity ‣ A.3 Six-Stage Donor Pool Screening ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents the filtering criteria and San Juan baseline values.

Table A1: Stage 1 demographic filtering criteria (ACS 2019–2023)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Variable | San Juan | Filter Range | Passing | Source |
| Median Age | 45.4 years | 44.2–46.6 | 22 | DP05 |
| Share Ages 15–34 | 25.5% | 24.5–26.5% | 22 | DP05 |
| Poverty Rate | 36.1% | 30.3–41.9% | 22 | S1701 |
| Median HH Income | $26,981 | $23,197–$30,765 | 22 | S1901 |
| Renter Multifamily | 66.0% | 57.8–74.2% | 22 | S2503 |

Notes: Filter ranges represent San Juan value ±\pm 1 SD across all 78 municipalities. Municipalities pass if Si≥4S\_{i}\geq 4. All monetary values in 2023 inflation-adjusted dollars.

##### Stage 1 result.

Twenty-three municipalities pass Stage 1 by satisfying at least four of five demographic criteria: Aguadilla, Aguas Buenas, Aibonito, Añasco, Arecibo, Bayamón, Cabo Rojo, Caguas, Camuy, Cataño, Cayey, Ceiba, Cidra, Fajardo, Hatillo, Humacao, Luquillo, Quebradillas, Río Grande, Salinas, Vega Baja, Vega Alta, Villalba.

#### A.3.2 Stage 2: Economic Structure Screening

This stage assesses the structural and dynamic similarity of Stage 1 candidates’ local economies to San Juan, focusing on sectors directly affected by the ordinance. I evaluate both level similarity (average sectoral composition) and dynamic similarity (co-movement in quarterly changes).

##### Data and preprocessing.

Using quarterly municipal revenue data for Sectors 14, 16, and 18, I restrict analysis to the pre-treatment window (2019 Q1–2023 Q3). For each municipality ii, sector ss, and quarter tt, I compute island-wide revenue shares:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sharei​s​t=Revenuei​s​t∑j∈PRRevenuej​s​tfor ​s∈{14,16,18},\text{Share}\_{ist}\;=\;\frac{\text{Revenue}\_{ist}}{\sum\_{j\in\text{PR}}\text{Revenue}\_{jst}}\quad\text{for }s\in\{14,16,18\}, |  | (10) |

where the denominator sums over all Puerto Rican municipalities in that sector-quarter. This share-based screening metric identifies municipalities with similar sectoral economic positioning in the island economy.

##### Similarity metrics.

For each Stage 1 donor ii and sector ss, I compute two metrics relative to San Juan (bb) over the T0T\_{0} pre-treatment quarters:

Average absolute gap (level similarity):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gapi​s=1T0​∑t=1T0|Sharei​s​t−Shareb​s​t|.\text{Gap}\_{is}\;=\;\frac{1}{T\_{0}}\sum\_{t=1}^{T\_{0}}|\text{Share}\_{ist}-\text{Share}\_{bst}|. |  | (11) |

Movement match (dynamic similarity):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Movei​s=1T0−1​∑t=2T0𝟙​{sgn​(Δ​Sharei​s​t)=sgn​(Δ​Shareb​s​t)},\text{Move}\_{is}\;=\;\frac{1}{T\_{0}-1}\sum\_{t=2}^{T\_{0}}\mathbb{1}\{\text{sgn}(\Delta\text{Share}\_{ist})=\text{sgn}(\Delta\text{Share}\_{bst})\}, |  | (12) |

where Δ​Sharei​s​t=Sharei​s​t−Sharei​s,t−1\Delta\text{Share}\_{ist}=\text{Share}\_{ist}-\text{Share}\_{is,t-1}.

##### Selection rule with auto-relaxation.

A donor passes if, for all three sectors, it satisfies Gapi​s≤γ0\text{Gap}\_{is}\leq\gamma\_{0} and Movei​s≥μ0\text{Move}\_{is}\geq\mu\_{0}, with initial thresholds γ0=0.10\gamma\_{0}=0.10 (10 percentage points) and μ0=0.80\mu\_{0}=0.80 (80% directional match). If fewer than 15 donors pass, I implement automatic threshold relaxation: decreasing μ\mu incrementally to 0.70, then supplementing with the next-best-ranked donors based on a composite score averaging Gap and Movement metrics.

##### Stage 2 result.

The filtering yields a pool of 16 municipalities with comparable economic exposure to the targeted sectors and similar quarterly dynamics: Aguadilla, Aguas Buenas, Añasco, Arecibo, Bayamón, Cabo Rojo, Caguas, Cataño, Cayey, Ceiba, Cidra, Fajardo, Hatillo, Humacao, Luquillo, and Quebradillas. Four municipalities (Bayamón, Caguas, Cayey, Arecibo) pass the initial thresholds; the remaining twelve are selected via fallback ranking after threshold relaxation to γ=0.10\gamma=0.10 and μ=0.70\mu=0.70.

#### A.3.3 Stage 3: Panel Construction & Normalization

Stage 3 integrates all data sources into a unified panel and applies data quality screens to ensure complete, balanced coverage across outcomes.

##### Stage 3A: Multi-domain data integration.

I merge crime data, employment data (NAICS 71, 72), and island-wide revenue shares (Sectors 14, 16, 18) for San Juan and all Stage 2 donors. Municipality names and quarter-end dates are standardized across datasets to ensure accurate merging on the key (municipality, quarter\_date). The merged dataset contains all variables in wide format, with revenue outcomes already expressed as island-wide shares from Stage 2, and crime/employment outcomes in raw counts awaiting per-capita conversion.

##### Data quality screen.

I apply a strict missingness rule: any municipality with more than 2 missing observations in any single outcome variable is dropped from the pool. This threshold ensures high-quality longitudinal coverage while allowing minimal interpolation for sporadic data gaps. The screen primarily binds on Arts/Entertainment employment (NAICS 71), which exhibits sporadic reporting in smaller municipalities.

##### Stage 3A result.

Eight municipalities pass the missingness screen: Aguadilla, Arecibo, Bayamón, Caguas, Cayey, Fajardo, Hatillo, and Humacao. Eight municipalities are dropped due to excessive missing data: Aguas Buenas, Añasco, Cabo Rojo, Cataño (extensive missing NAICS 71 data), Ceiba (missing NAICS 72 data), Cidra, Luquillo, and Quebradillas (extensive missing NAICS 71 data), and Río Grande (missing data in both employment sectors). The merged wide-format panel with eight donors proceeds to Stage 3B for long-format transformation and per-capita conversion.

##### Stage 3B: Long-format panel with balanced support.

Using the eight donors from Stage 3A, I construct the outcome set with island-wide revenue shares and per-capita crime/employment rates. Per-capita rates are computed by dividing raw counts by population (in thousands) using 2023 ACS 5-year estimates. Observations are restricted through 2025-03-31 (2025 Q1), yielding 25 quarters from 2019 Q1 through 2025 Q1.

The data integration process identifies one missing observation: Arts/Entertainment employment for Arecibo in 2023 Q4. Before applying balanced support constraints, I fill this gap using time-based linear interpolation applied separately within the pre-treatment period (interpolation respects the treatment boundary to avoid contamination). The interpolated panel is then reshaped to long format with columns (unit, time, outcome, value).

Balanced support enforcement ensures each municipality contributes only time periods where all seven outcomes are jointly observed. Since interpolation has already filled the single missing cell, this constraint is automatically satisfied without dropping any observations. The final panel achieves complete coverage: 1,575 observations (9 units ×\times 25 quarters ×\times 7 outcomes).

##### Stage 3B result.

The complete Stage 3 process yields a balanced long-format quarterly panel (2019 Q1–2025 Q1; 25 quarters) with seven outcomes for San Juan and eight donors: Aguadilla, Arecibo, Bayamón, Caguas, Cayey, Fajardo, Hatillo, and Humacao. Revenue outcomes are expressed as island-wide shares; crime and employment outcomes are per-capita rates (per 1,000 residents). After time-based interpolation fills the single missing value, the panel contains 1,575 observations with complete coverage. The panel is ready for contamination screening.

#### A.3.4 Stage 4: Pre-Treatment Contamination Scan

Small donor pools magnify the influence of any contaminated unit. Stage 4 identifies and excludes donors exhibiting pre-treatment structural breaks or instability that could confound the synthetic control comparison.

##### Placebo-break methodology.

I implement a data-driven contamination scan entirely within the pre-treatment window. For each donor, I test a grid of placebo intervention dates spanning 2021 Q1 through 2023 Q1, constructing synthetic controls for each placebo date and evaluating outcome gaps and root mean squared prediction error (RMSPE) around each placebo break. Known island-wide shock windows (e.g., the acute pandemic period in 2020) are excluded from the break grid to avoid spurious flags.

##### Flagging criteria.

A donor is flagged if it exhibits persistently elevated RMSPE ratios (post-placebo RMSPE / pre-placebo RMSPE) or large median absolute post-break gaps (measured in pre-break standard deviations) across multiple consecutive placebo dates. I require at least 4 consecutive quarters of instability to flag a municipality, reducing false positives from isolated noise.

##### Stage 4 result.

Six municipalities pass the contamination screen: Aguadilla, Arecibo, Bayamón, Cayey, Hatillo, and Humacao. Two municipalities are flagged and excluded: Caguas (flagged at 4 consecutive quarters: 2021 Q3–2022 Q2 with median RMSPE ratio 1.72) and Fajardo (flagged at 4 consecutive quarters: 2021 Q4–2022 Q3 with median RMSPE ratio 1.65). The six passing donors exhibit stable factor structure throughout the pre-treatment window, free from idiosyncratic pre-treatment structural breaks that could contaminate synthetic control weights.

#### A.3.5 Stage 5: Parallel Trends & Proximity Validation (Design Selection: 70/7)

Stage 5 applies *pre-specified design* criteria to the Stage 4 survivors. The goal is to finalize a donor set that is dynamically comparable to San Juan while preserving adequate pool size for estimation and inference.

##### Parallel trends screening (design threshold).

For each (donor, outcome) pair, I run a bivariate Granger non-causality test on pre-treatment quarters only, testing whether the donor predicts San Juan conditional on San Juan’s lags. Let H0H\_{0} denote “donor does not Granger-cause San Juan.” A donor’s pass rate is the fraction of the seven outcomes for which H0H\_{0} is not rejected. The design threshold is 70% of outcomes (“70/7”), i.e., pass rate ≥0.70\geq 0.70.

##### Donor proximity (levels & trends).

I compute standardized Euclidean distances on (i) pre-treatment outcome means and (ii) linear pre-treatment trends across the seven outcomes. The combined distance is

|  |  |  |
| --- | --- | --- |
|  | Ddcombined= 0.6⋅Ddmean+ 0.4⋅Ddslope,D\_{d}^{\text{combined}}\;=\;0.6\cdot D\_{d}^{\text{mean}}\;+\;0.4\cdot D\_{d}^{\text{slope}}, |  |

and donors are ranked in ascending order of DdcombinedD\_{d}^{\text{combined}}. The design rule requires rank ≤7\leq 7.

##### Selection rule (design) and sensitivity variant.

A donor is retained if it satisfies both 70/7 parallel-trends and rank ≤7\leq 7. To assess robustness to stricter dynamic similarity, I also evaluate a 75/7 variant as a *sensitivity check only*; it does not govern selection.

##### Stage 5 (design 70/7) result.

Applying the design thresholds to the Stage 4 survivors yields a six-municipality donor pool:

|  |  |  |
| --- | --- | --- |
|  | Aguadilla, Arecibo, Bayamón, Cayey, Hatillo, Humacao.\textbf{Aguadilla, Arecibo, Bayamón, Cayey, Hatillo, Humacao}. |  |

Under the stricter sensitivity threshold (75/7), two donors (Cayey, Humacao) would be excluded; this sensitivity is reported for transparency and does not affect the design pool.

#### A.3.6 Stage 6: Weight Concentration Diagnostics (Non-binding)

Stage 6 reports *non-binding* diagnostics on the six-donor design pool from Stage 5 (70/7). These statistics characterize geometry and concentration; they do not add or remove donors and do not alter estimation.

##### Pre-treatment design matrix.

For each outcome kk, I demean by pre-treatment means, standardize by the treated unit’s pre-treatment standard deviation, and apply sign alignment where appropriate (crime ×(−1)\times(-1)). Stacking the pre-period blocks yields (X,y)(X,y), identical to the preprocessing used in estimation.

##### Diagnostic metrics.

I report: (i) effective rank of XX; (ii) donor leverage via right singular vectors; (iii) nearest-neighbor cosine similarity between San Juan and each donor in standardized outcome space; and (iv) weight concentration via the effective number of donors Neff=1/∑iwi2N\_{\text{eff}}=1/\sum\_{i}w\_{i}^{2}.

##### Regularization sensitivity grid.

For Λ={0,10−4,10−3,10−2,10−1,1}\Lambda=\{0,10^{-4},10^{-3},10^{-2},10^{-1},1\}, I solve

|  |  |  |
| --- | --- | --- |
|  | minw∈Δ⁡‖y−X​w‖22+λ​‖w‖22s.t.w≥0, 1⊤​w=1,\min\_{w\in\Delta}\;\|y-Xw\|\_{2}^{2}\;+\;\lambda\|w\|\_{2}^{2}\quad\text{s.t.}\quad w\geq 0,\ \mathbf{1}^{\top}w=1, |  |

recording pre-treatment RMSPE, NeffN\_{\text{eff}}, and maxi⁡wi\max\_{i}w\_{i}.

##### Baseline diagnostic results (six-donor design pool).

With λ=0\lambda=0 (simplex only), pre-treatment RMSPE is ≈0.859\approx 0.859 and Neff≈3.41N\_{\text{eff}}\approx 3.41 (where Neff=1/∑iwi2N\_{\text{eff}}=1/\sum\_{i}w\_{i}^{2}). Leverage is uniform across donors (no single municipality dominates the covariance of XX). The baseline weights and nearest-neighbor cosine similarities for the six-donor pool are:

|  |  |  |
| --- | --- | --- |
| Donor | Weight | Cosine Similarity |
| Aguadilla | 37.4% | 0.365 |
| Humacao | 29.4% | 0.297 |
| Bayamón | 24.1% | 0.203 |
| Hatillo | 9.0% | 0.180 |
| Arecibo | 0.0% | 0.010 |
| Cayey | 0.0% | 0.103 |

The low maxima indicate San Juan lies in a region requiring interpolation across multiple donors rather than a near-exact single match.

##### Regularization sensitivity.

Increasing λ\lambda from 0 to 11 alters fit and concentration negligibly: relative RMSPE rises by ∼0.00024%\sim 0.00024\% (<0.001%<0.001\%), NeffN\_{\text{eff}} nudges from ≈3.41\approx 3.41 to ≈3.42\approx 3.42, and maxi⁡wi\max\_{i}w\_{i} declines slightly (from 37.4%37.4\% to 37.3%37.3\%). This suggests the observed concentration reflects donor-geometry rather than numerical instability.

##### Stage 6 conclusion (non-binding).

Diagnostics show *moderate* concentration (Neff≈3.41N\_{\text{eff}}\approx 3.41) with no pathological dominance. These findings support proceeding with the six-donor design pool selected in Stage 5 (70/7). The stricter 75/7 variant remains a *robustness* check and does not change the design-based donor set.

### A.4 Final Donor Pool

The six-stage screening protocol (with Stage 5 *design* threshold 70/7) yields a final donor pool of six municipalities:

Aguadilla, Arecibo, Bayamón, Cayey, Hatillo, Humacao

Table [A2](https://arxiv.org/html/2510.25782v1#A1.T2 "Table A2 ‣ A.4 Final Donor Pool ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") summarizes key validation and diagnostic metrics for the design pool. The stricter 75/7 variant is reported as a sensitivity check only and does not govern selection.

Table A2: Final donor pool (design 70/7) validation and diagnostics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Municipality | Granger Pass Rate | Stage 4 Flags | Stage 6 Weight | Stage 6 Cosine |
| Aguadilla | 85.7% | 0 | 37.4% | 0.365 |
| Arecibo | 100.0% | 0 | 0.0% | 0.010 |
| Bayamón | 100.0% | 0 | 24.1% | 0.203 |
| Cayey | 71.4% | 0 | 0.0% | 0.103 |
| Hatillo | 85.7% | 0 | 9.0% | 0.180 |
| Humacao | 71.4% | 0 | 29.4% | 0.297 |
| San Juan | — | — | — | — |

Notes:
Granger pass rate is the fraction of 7 outcomes for which the donor does not Granger-cause San Juan at p>0.05p>0.05.
Stage 4 flags count consecutive placebo-break quarters flagged for structural instability (exclusion threshold: ≥4\geq 4).
Stage 6 weight and cosine are *diagnostic* quantities computed on the six-donor *design* pool; Stage 6 is non-binding and does not alter the pool.
The 75/7 variant is a *sensitivity-only* screen; under 75/7, Cayey and Humacao would be excluded, but the design pool remains the six municipalities listed above.

This design pool balances comparability requirements with adequate size for inference. All six donors pass the contamination screen (zero flags) and meet the *design* parallel-trends threshold (70/7). The 75/7 sensitivity confirms robustness to stricter dynamic similarity without changing the design-based donor set.

### A.5 Methodological Compatibility with MOSC

My donor pool screening is fully compatible with the MOSC estimation framework for three reasons:

##### Ex ante design-stage screening.

All screening decisions use only information available before weight estimation for the main analysis. The six stages rely exclusively on pre-treatment data (with respect to San Juan’s treatment date) and do not condition on post-treatment outcomes or estimated treatment effects. This separates the design stage (donor selection) from the estimation stage (weight computation), preserving the experimental-design logic of synthetic control methods (Abadie and Zhao, [2025](https://arxiv.org/html/2510.25782v1#bib.bib6)).

##### No outcome-specific donor swapping.

Unlike outcome-by-outcome SCM that might select different donors for different outcomes, I fix a single donor pool before estimating common weights. This ensures that the same set of comparison municipalities contributes to all outcomes, facilitating coherent interpretation of the multi-outcome estimator and avoiding data-driven selection that could invalidate inference.

##### Orthogonal to MOSC estimation.

The screening protocol neither anticipates nor constrains the MOSC weight estimation procedure. Stage 6 diagnostics assess concentration patterns but do not alter the estimator specification. Final MOSC estimation applies the standard simplex-constrained common-weight framework to the Stage 5 donor pool, with weights chosen to minimize pre-treatment aggregate fit across all seven outcomes simultaneously.

Table [A3](https://arxiv.org/html/2510.25782v1#A1.T3 "Table A3 ‣ Orthogonal to MOSC estimation. ‣ A.5 Methodological Compatibility with MOSC ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") summarizes the key data harmonization conventions used throughout the analysis.

Table A3: Data harmonization and estimation conventions

|  |  |
| --- | --- |
| Convention | Specification |
| Temporal frequency | Quarterly (2019 Q1–2025 Q1; 25 quarters total) |
| Treatment date | November 9, 2023 (2023 Q4) |
| Pre-treatment window | 2019 Q1–2023 Q3 (19 quarters) |
| Post-treatment window | 2023 Q4–2025 Q1 (6 quarters; Q4 has partial exposure) |
| Revenue outcomes | Island-wide shares (Sectors 14, 16, 18) |
| Employment outcomes | Per 1,000 residents (NAICS 71, 72) |
| Crime outcomes | Per 1,000 residents (late-night disorder, violent crime) |
| Revenue denominator | Island-wide sector total (all PR municipalities) |
| Population denominator | 2023 ACS 5-year estimates (fixed throughout study window) |
| Intercept-shift | Pre-treatment means removed before optimization |
| Standardization | Treated unit’s pre-treatment SD (applied to all units) |
| Sign alignment | Crime outcomes ×(−1)\times(-1); others ×(+1)\times(+1) |
| Weight constraints | Simplex (w≥0w\geq 0, 𝟏⊤​w=1\mathbf{1}^{\top}w=1); no ridge penalty |

Notes: These conventions apply uniformly across baseline estimation (Section [5.4](https://arxiv.org/html/2510.25782v1#S5.SS4 "5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), robustness checks (Appendix [C](https://arxiv.org/html/2510.25782v1#A3 "Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), and inference procedures (Section [4](https://arxiv.org/html/2510.25782v1#S4 "4 Multi-Outcome Synthetic Control: Inference ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

This comprehensive six-stage screening protocol ensures that the final donor pool satisfies both the theoretical requirements for valid synthetic control estimation (comparability, stability, parallel trends) and the practical requirements for credible inference (adequate pool size, data quality, freedom from contamination). The resulting six-municipality pool provides the foundation for all multi-outcome synthetic control analyses reported in the main text and subsequent appendices.

## Appendix B Formal Theory

This appendix presents the formal theoretical framework for multi-outcome synthetic control estimation under shared factor structure. I begin by establishing the baseline separate SCM framework and documenting its limitations (Section [B.1](https://arxiv.org/html/2510.25782v1#A2.SS1 "B.1 Baseline Separate SCM Framework ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), then present the common-weight alternative and oracle results (Section [B.2](https://arxiv.org/html/2510.25782v1#A2.SS2 "B.2 Multi-Outcome Common-Weight Framework ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), and finally provide the bias decomposition that formalizes the efficiency gains of common-weight approaches (Section [B.3](https://arxiv.org/html/2510.25782v1#A2.SS3 "B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). I adapt the framework of Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) to an intercept-shifted implementation with treated-unit standardization. Complete proofs, additional regularity conditions, and detailed bias decompositions appear in Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) (Sections 3–4 and Online Appendix A–B).

### B.1 Baseline Separate SCM Framework

The traditional synthetic control method estimates counterfactual outcomes by constructing a weighted average of donor units, with weights chosen to minimize pre-treatment imbalance (Abadie et al., [2010](https://arxiv.org/html/2510.25782v1#bib.bib4)). In applications with multiple outcomes, the standard approach applies SCM separately to each outcome series, producing outcome-specific donor weights. This section formalizes the separate estimation framework and documents its limitations, motivating the common-weight alternatives developed in subsequent sections.

#### B.1.1 Mathematical Framework

Consider a panel with NN units and TT time periods, where unit i=1i=1 is treated and units i∈𝒟={2,3,…,N}i\in\mathcal{D}=\{2,3,\ldots,N\} are potential donors. Let N0=N−1N\_{0}=N-1 denote the number of donor units. For KK outcomes indexed by k=1,…,Kk=1,\ldots,K, let Yi​t​kY\_{itk} denote the observed value for unit ii at time tt on outcome kk. Treatment occurs after period T0T\_{0}, so periods t=1,…,T0t=1,\ldots,T\_{0} constitute the pre-treatment window.

Following Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)), I implement intercept-shifted estimators that focus on trend dynamics rather than level differences. For each unit–outcome pair (i,k)(i,k), define the pre-treatment mean

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y¯i​kpre=1T0​∑t=1T0Yi​t​k\overline{Y}\_{ik}^{\text{pre}}\;=\;\frac{1}{T\_{0}}\sum\_{t=1}^{T\_{0}}Y\_{itk} |  | (13) |

and the demeaned series

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y˙i​t​k=Yi​t​k−Y¯i​kpre.\dot{Y}\_{itk}\;=\;Y\_{itk}-\overline{Y}\_{ik}^{\text{pre}}. |  | (14) |

Let 𝒞⊂ℝN0\mathcal{C}\subset\mathbb{R}^{N\_{0}} be a convex constraint set for weights. I focus on the unit simplex

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔN0={γ∈ℝN0:γj≥0​ for all ​j, 1N0⊤​γ=1}.\Delta\_{N\_{0}}\;=\;\Big\{\gamma\in\mathbb{R}^{N\_{0}}:\gamma\_{j}\geq 0\text{ for all }j,\;\mathbf{1}\_{N\_{0}}^{\top}\gamma=1\Big\}. |  | (15) |

For any γ∈𝒞\gamma\in\mathcal{C}, define the pre-treatment residual for outcome kk using the demeaned outcomes as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt,k​(γ)=Y˙1​t​k−∑j∈𝒟γj​Y˙j​t​kfor ​t≤T0.r\_{t,k}(\gamma)\;=\;\dot{Y}\_{1tk}\;-\;\sum\_{j\in\mathcal{D}}\gamma\_{j}\dot{Y}\_{jtk}\quad\text{for }t\leq T\_{0}. |  | (16) |

The separate SCM approach estimates outcome-specific weights by solving independent optimization problems for each outcome:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ^ksep∈arg⁡minγ∈𝒞⁡qksep​(γ),qksep​(γ)={1T0​∑t=1T0rt,k​(γ)2}1/2,\hat{\gamma}^{\text{sep}}\_{k}\;\in\;\arg\min\_{\gamma\in\mathcal{C}}\;q\_{k}^{\text{sep}}(\gamma),\qquad q\_{k}^{\text{sep}}(\gamma)\;=\;\left\{\frac{1}{T\_{0}}\sum\_{t=1}^{T\_{0}}r\_{t,k}(\gamma)^{2}\right\}^{1/2}, |  | (17) |

which produces KK distinct weight vectors {γ^1sep,…,γ^Ksep}\{\hat{\gamma}^{\text{sep}}\_{1},\ldots,\hat{\gamma}^{\text{sep}}\_{K}\}. The synthetic control for the treated unit’s counterfactual outcome kk in any post-treatment period is then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y^1​t​k​(0)=Y¯1​kpre+∑j∈𝒟γ^jsep​Y˙j​t​kkfor ​t>T0.\hat{Y}\_{1tk}(0)\;=\;\overline{Y}\_{1k}^{\text{pre}}\;+\;\sum\_{j\in\mathcal{D}}\hat{\gamma}\_{j}^{\text{sep}}{}\_{k}\,\dot{Y}\_{jtk}\quad\text{for }t>T\_{0}. |  | (18) |

The treatment effect estimate for outcome kk at time tt is

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ^t​k=Y1​t​k−Y^1​t​k​(0).\hat{\tau}\_{tk}\;=\;Y\_{1tk}-\hat{Y}\_{1tk}(0). |  | (19) |

#### B.1.2 Limitations of Separate Estimation

While conceptually straightforward and often achieving superior pre-treatment fit, the separate approach faces several fundamental challenges that motivate multi-outcome alternatives.

##### Overfitting risk in short panels.

In shorter panels, separate estimation can achieve near-perfect pre-treatment fit by overfitting to idiosyncratic noise rather than identifying weights that balance fundamental drivers (Abadie et al., [2010](https://arxiv.org/html/2510.25782v1#bib.bib4); Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). From a factor-model perspective (formalized in Section [B.2](https://arxiv.org/html/2510.25782v1#A2.SS2 "B.2 Multi-Outcome Common-Weight Framework ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), imperfect-fit bias remains O​(1)O(1) and overfitting bias decays at O​(1/T0)O(1/\sqrt{T\_{0}}). Critically, increasing the number of outcomes KK does not improve these orders under separate estimation—each outcome is fit independently, so additional outcomes provide no statistical efficiency gains. This contrasts with common-weight approaches, where the overfitting component scales as O​(1/T0​K)O(1/\sqrt{T\_{0}K}), exploiting information pooling across outcomes (see Section [B.3](https://arxiv.org/html/2510.25782v1#A2.SS3 "B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

##### Fragmented interpretation and donor selection.

Separate estimation typically produces different donor compositions across outcomes, making it difficult to construct a coherent narrative about which comparison units best represent the treated unit’s counterfactual (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). This fragmentation is not merely a presentational inconvenience—it undermines the interpretability central to synthetic control for policy evaluation. When related outcomes rely on disjoint donor sets, cross-outcome comparisons and mechanism interpretation become opaque.

##### Inefficient information use under shared structure.

When outcomes share common underlying factors—as is typical when interventions operate through multiple interconnected mechanisms—separate estimation fails to leverage this shared structure. Each outcome-specific optimization discards information contained in the other K−1K-1 outcomes about which donors provide the best structural match to the treated unit. This manifests as *noise amplification* (idiosyncratic shocks drive outcome-specific weights) and *missed factor identification* (separate fits cannot exploit the (T0×K)(T\_{0}\times K) matrix structure that common weights utilize).

##### Effective degrees of freedom and specification search.

By estimating KK separate weight vectors, separate SCM increases effective degrees of freedom in the sense formalized by Pouliot and Xie ([2022](https://arxiv.org/html/2510.25782v1#bib.bib31)), raising concerns about specification search and multiple testing. While outcome-by-outcome inference can be adjusted for multiplicity, a fragmented weight structure still permits implicit discretion in emphasizing outcomes with favorable donor matches. Common-weight constraints impose a unified donor composition across outcomes, disciplining this form of specification search.

### B.2 Multi-Outcome Common-Weight Framework

Building on the limitations above, I now formalize the common-weight alternative under shared factor structure. The key insight is that when outcomes exhibit low-rank structure—driven by a small number of common latent factors—there exist weights that can simultaneously balance all outcomes, enabling both efficiency gains and interpretability advantages.

#### B.2.1 Notation and Setup

I work with a panel of NN units over TT time periods. Unit i=1i=1 is treated; units i∈𝒟={2,…,N}i\in\mathcal{D}=\{2,\ldots,N\} are potential donors, with N0=N−1N\_{0}=N-1 donors total. I observe KK outcomes Yi​t​kY\_{itk} (k=1,…,Kk=1,\ldots,K) for each unit-time pair. Treatment occurs after period T0T\_{0}.

Potential outcomes under control follow a linear factor structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi​t​k​(0)=αi​k+Li​t​k+εi​t​k,Y\_{itk}(0)\;=\;\alpha\_{ik}\;+\;L\_{itk}\;+\;\varepsilon\_{itk}, |  | (20) |

where αi​k\alpha\_{ik} are unit–outcome fixed effects, Li​t​k=ϕi⊤​μt​kL\_{itk}=\phi\_{i}^{\top}\mu\_{tk} captures systematic variation via latent factors (ϕi∈ℝr\phi\_{i}\in\mathbb{R}^{r} unit-specific, μt​k∈ℝr\mu\_{tk}\in\mathbb{R}^{r} time–outcome factors), and εi​t​k\varepsilon\_{itk} is mean-zero idiosyncratic noise. Let L∈ℝN×(T​K)L\in\mathbb{R}^{N\times(TK)} stack {Li​t​k}\{L\_{itk}\} across all times and outcomes, with L−1L\_{-1} excluding the treated unit.

For estimation, I use demeaned series Y˙i​t​k=Yi​t​k−Y¯i​kpre\dot{Y}\_{itk}=Y\_{itk}-\overline{Y}\_{ik}^{\text{pre}} where Y¯i​kpre=1T0​∑t=1T0Yi​t​k\overline{Y}\_{ik}^{\text{pre}}=\frac{1}{T\_{0}}\sum\_{t=1}^{T\_{0}}Y\_{itk}. This intercept-shift removes the unit–outcome fixed effects αi​k\alpha\_{ik}, focusing estimation on the latent factor component Li​t​kL\_{itk} and idiosyncratic variation εi​t​k\varepsilon\_{itk}. Pre-treatment residuals are

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt,k​(γ)=Y˙1​t​k−∑j∈𝒟γj​Y˙j​t​k(t≤T0).r\_{t,k}(\gamma)\;=\;\dot{Y}\_{1tk}\;-\;\sum\_{j\in\mathcal{D}}\gamma\_{j}\dot{Y}\_{jtk}\qquad(t\leq T\_{0}). |  | (21) |

(Intercept-shifted / de-meaned multi-outcome SCM follows Sun et al. [2025](https://arxiv.org/html/2510.25782v1#bib.bib34).)

#### B.2.2 Formal Assumptions and Oracle Weights

The central assumption enabling common-weight estimation is that the treated unit’s latent trajectory lies within the span of the donor units’ factor space.

###### Assumption 2 (Low-Rank Structure).

The latent factor matrix LL satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | rank​(L−1)=rank​(L)<N−1.\mathrm{rank}(L\_{-1})\;=\;\mathrm{rank}(L)\;<\;N-1. |  | (22) |

This condition ensures the treated unit’s latent trajectory lies in the donors’ row space, enabling perfect reconstruction via linear combinations. The rank equality means the treated unit adds no new direction to the factor space—intuitively, the treated unit’s systematic variation can be expressed as a combination of the systematic patterns present in the donor pool (cf. Assumption 2a in Sun et al. [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

###### Proposition 1 (Oracle Weights).

Under Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), there exist oracle weights γ⋆∈ℝN0\gamma^{\star}\in\mathbb{R}^{N\_{0}} with 𝟏N0⊤​γ⋆=1\mathbf{1}\_{N\_{0}}^{\top}\gamma^{\star}=1 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L1​t​k=∑i=2Nγi⋆​Li​t​kfor all ​t,k.L\_{1tk}\;=\;\sum\_{i=2}^{N}\gamma^{\star}\_{i}L\_{itk}\qquad\text{for all }t,k. |  | (23) |

###### Proof.

The rank condition in Assumption [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") implies existence of such weights by the fundamental theorem of linear algebra: if the treated unit’s row in LL lies in the row space of L−1L\_{-1}, then it can be expressed as a linear combination of donor rows. See Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)), Definition 1, Proposition 1, and Online Appendix B.1 for the complete formal proof. ∎∎

These oracle weights remove bias from the unobserved latent component simultaneously across all outcome-time pairs. The key advantage over separate estimation is that the *same* weights balance *all* outcomes, exploiting the shared factor structure.

For empirical implementation, I require that oracle weights satisfy my constraint set:

###### Assumption 3 (Bounded-Norm Oracle).

There exists a convex constraint set 𝒞⊆ℝN0\mathcal{C}\subseteq\mathbb{R}^{N\_{0}} and constant C>0C>0 such that ‖γ‖1≤C\|\gamma\|\_{1}\leq C for all γ∈𝒞\gamma\in\mathcal{C}, and oracle weights γ⋆∈𝒞\gamma^{\star}\in\mathcal{C} exist.

In what follows, I focus on the unit simplex 𝒞=ΔN0={γ∈ℝN0:γ≥0,𝟏N0⊤​γ=1}\mathcal{C}=\Delta\_{N\_{0}}=\{\gamma\in\mathbb{R}^{N\_{0}}:\gamma\geq 0,\mathbf{1}\_{N\_{0}}^{\top}\gamma=1\} for interpretability (convex-hull interpolation), though analogous rates apply to other convex ℓ1\ell\_{1}-bounded sets.

##### Feasible common-weight estimators.

While oracle weights γ⋆\gamma^{\star} are infeasible (they depend on unobserved Li​t​kL\_{itk}), feasible estimators approximate them by aggregating pre-treatment information across outcomes. I implement the *average estimator*, which minimizes the average of outcome-specific pre-treatment RMSPEs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ^avg∈arg⁡minγ∈𝒞⁡1K​∑k=1Kqksep​(γ),\hat{\gamma}^{\text{avg}}\;\in\;\arg\min\_{\gamma\in\mathcal{C}}\;\frac{1}{K}\sum\_{k=1}^{K}q\_{k}^{\text{sep}}(\gamma), |  | (24) |

where qksep​(γ)q\_{k}^{\text{sep}}(\gamma) is defined as in Equation ([17](https://arxiv.org/html/2510.25782v1#A2.E17 "Equation 17 ‣ B.1.1 Mathematical Framework ‣ B.1 Baseline Separate SCM Framework ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). This estimator pools information across outcomes, producing a single weight vector γ^avg\hat{\gamma}^{\text{avg}} applied to all outcomes. Under regularity conditions detailed in Section [B.3](https://arxiv.org/html/2510.25782v1#A2.SS3 "B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), this pooling yields efficiency gains that scale with KK.

### B.3 Bias Decomposition and Scaling Results

I now formalize the efficiency advantages of common-weight estimation relative to the separate baseline. The key results show that exploiting shared structure through common weights improves the scaling rates of both imperfect-fit and overfitting bias components.

#### B.3.1 Error Decomposition

For any estimator γ^\hat{\gamma}, the treatment effect estimation error for outcome kk at the first post-treatment period t=T0+1t=T\_{0}+1 decomposes as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τk−τ^k​(γ^)=L1,T0+1,k−∑i∈𝒟γ^i​Li,T0+1,k⏟Bias​(γ^)+ε˙1,T0+1,k−∑i∈𝒟γ^i​ε˙i,T0+1,k⏟Noise,\tau\_{k}-\hat{\tau}\_{k}(\hat{\gamma})\;=\;\underbrace{L\_{1,T\_{0}+1,k}-\sum\_{i\in\mathcal{D}}\hat{\gamma}\_{i}L\_{i,T\_{0}+1,k}}\_{\text{Bias}(\hat{\gamma})}\;+\;\underbrace{\dot{\varepsilon}\_{1,T\_{0}+1,k}-\sum\_{i\in\mathcal{D}}\hat{\gamma}\_{i}\dot{\varepsilon}\_{i,T\_{0}+1,k}}\_{\text{Noise}}, |  | (25) |

where τk=Y1,T0+1,k​(1)−Y1,T0+1,k​(0)\tau\_{k}=Y\_{1,T\_{0}+1,k}(1)-Y\_{1,T\_{0}+1,k}(0) is the true treatment effect. The noise term has mean zero and is not affected by weight choice (given the constraint set), so the estimation challenge centers on minimizing bias.

The bias further decomposes into two components:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bias​(γ^)=R0​(γ^)−R1​(γ^),\text{Bias}(\hat{\gamma})\;=\;R\_{0}(\hat{\gamma})\;-\;R\_{1}(\hat{\gamma}), |  | (26) |

where:

* •

  R0​(γ^)R\_{0}(\hat{\gamma}) represents imperfect pre-treatment fit—the residual imbalance in latent factors when using feasible weights γ^\hat{\gamma} rather than oracle weights γ⋆\gamma^{\star}
* •

  R1​(γ^)R\_{1}(\hat{\gamma}) captures overfitting—the spurious fit to pre-treatment idiosyncratic noise εi​t​k\varepsilon\_{itk} that does not generalize post-treatment

Both terms depend on estimator-specific weights over pre-treatment observations. Intuitively, R0R\_{0} decreases as I achieve better pre-treatment fit, while R1R\_{1} increases as I overfit to noise. The optimal estimator balances these competing forces (cf. Eqs. (6)–(7) in Sun et al. [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

#### B.3.2 Holistic Information Tradeoff (Remark)

Pooling across outcomes both helps and can potentially hurt. When outcome k′k^{\prime} is revised to better measure a construct, the optimization updates to balance the improved measurement alongside other outcomes—this propagation keeps predictions mutually consistent under the best available donor composition. However, if outcome k′k^{\prime} contains substantial measurement error or data quality issues, that noise can propagate through the joint optimization and degrade predictions for all outcomes—an issue absent under separate estimation, where each outcome is insulated from errors in others.

In the terms of Equation ([26](https://arxiv.org/html/2510.25782v1#A2.E26 "Equation 26 ‣ B.3.1 Error Decomposition ‣ B.3 Bias Decomposition and Scaling Results ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), noisy outcomes raise both imperfect pre-fit (R0R\_{0}, by making true balance harder) and overfitting (R1R\_{1}, by providing more noise to fit). Moreover, the 1/K1/\sqrt{K} variance reduction in the scaling rates (below) relies on limited error dependence across outcomes; strong cross-outcome error correlation attenuates this benefit. This motivates leave-one-outcome-out diagnostics (see, e.g., Section [C.3.2](https://arxiv.org/html/2510.25782v1#A3.SS3.SSS2 "C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) to assess robustness to individual outcome quality.

#### B.3.3 Scaling Rates for Common-Weight Estimators

Under Assumptions [1](https://arxiv.org/html/2510.25782v1#Thmassumption1 "Assumption 1 (Low-Rank Structure). ‣ 2.1.1 Factor Model and Low-Rank Assumption ‣ 2.1 Common Weights & Shared Structure ‣ 2 Multi-Outcome Synthetic Control: Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")–[3](https://arxiv.org/html/2510.25782v1#Thmassumption3 "Assumption 3 (Bounded-Norm Oracle). ‣ B.2.2 Formal Assumptions and Oracle Weights ‣ B.2 Multi-Outcome Common-Weight Framework ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") and regularity conditions (sub-Gaussian errors, adequate signal-to-noise ratio, moderate cross-outcome correlation), Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) show that common-weight estimators achieve:

* •

  Imperfect pre-fit: For the average estimator,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | R0=Op​(1K),R\_{0}\;=\;O\_{p}\left(\frac{1}{\sqrt{K}}\right), |  | (27) |

  compared to Op​(1)O\_{p}(1) for separate estimation, due to information pooling across outcomes (Theorem 1 and Table 1 of Sun et al. [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).
* •

  Overfitting: Common weights exploit both time and outcome dimensions:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | R1=Op​(1T0​K),R\_{1}\;=\;O\_{p}\left(\frac{1}{\sqrt{T\_{0}K}}\right), |  | (28) |

  compared to Op​(1/T0)O\_{p}(1/\sqrt{T\_{0}}) for separate estimation (Theorem 1 and Table 1 of Sun et al. [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)).

##### Interpretation.

The Op​(1/K)O\_{p}(1/\sqrt{K}) scaling for R0R\_{0} reflects noise averaging: by balancing multiple outcomes simultaneously, the average estimator’s objective contains more information about the true donor composition, reducing the impact of outcome-specific idiosyncratic variation. The Op​(1/T0​K)O\_{p}(1/\sqrt{T\_{0}K}) scaling for R1R\_{1} captures the effective sample size for identifying weights—common-weight estimation uses T0×KT\_{0}\times K pre-treatment observations rather than T0T\_{0} observations per outcome, dramatically reducing overfitting when KK is moderately large and outcomes share structure. For moderate KK and T0T\_{0}, these rates imply sizable reductions in both components relative to separate estimation.

### B.4 Finite-Sample Fit Dominance

Beyond asymptotic scaling rates, the average estimator enjoys a finite-sample property: for any fixed weights γ\gamma, the average objective satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | qavg​(γ)≤qcat​(γ)q\_{\text{avg}}(\gamma)\;\leq\;q\_{\text{cat}}(\gamma) |  | (29) |

by Jensen’s inequality, where qcatq\_{\text{cat}} is the concatenated objective that stacks all outcomes (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). This relationship concerns the optimization objectives rather than the common RMSPE reporting metric (which can rank estimators differently) and provides theoretical justification for robustness properties of the average estimator.

### B.5 When Common Weights May Fail

Despite the theoretical advantages documented above, common-weight estimation is not universally appropriate. Four conditions where separate estimation may be preferable:

##### Heterogeneous data quality or measurement protocols.

When outcomes are measured with vastly different precision or reliability, forcing common weights can propagate measurement error from low-quality outcomes to high-quality ones. Leave-one-outcome-out diagnostics (e.g., Section [C.3.2](https://arxiv.org/html/2510.25782v1#A3.SS3.SSS2 "C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) help detect such contamination.

##### Violated low-rank structure.

When scree plots show no clear elbow and cumulative variance increases nearly linearly (flat scree), the low-rank assumption is dubious. This indicates outcomes are driven by largely independent factors rather than shared structure, weakening the theoretical basis for common weights. See Section [5.3](https://arxiv.org/html/2510.25782v1#S5.SS3 "5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") for general diagnostic guidance.

##### Independent causal mechanisms.

Policy theory may posit that treatment operates through genuinely separate channels for different outcomes, with no shared transmission mechanism. In such settings, separate controls can be justified even if some outcomes are correlated empirically.

##### Unstable weight allocations.

Leave-one-outcome-out diagnostics may reveal instability when excluding individual outcomes dramatically changes donor composition. Large shifts suggest the common-weight solution is precariously balanced, with different outcomes pulling toward incompatible donor mixes (e.g., the treated unit lies near the boundary of the donor convex hull).

The diagnostics in Sections [C.3](https://arxiv.org/html/2510.25782v1#A3.SS3 "C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")–[C.5](https://arxiv.org/html/2510.25782v1#A3.SS5 "C.5 Placebo Distribution Details ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") provide tools to assess these conditions empirically before relying on common-weight efficiency gains.

### B.6 Summary: When to Use Common Weights

I recommend common-weight MOSC estimation when:

1. 1.

   Scree plots show clear low-rank structure (elbow with r≪Kr\ll K components explaining a large share of variance)
2. 2.

   Outcomes share theoretical linkages through common policy channels
3. 3.

   Leave-one-outcome-out diagnostics show stable weight allocations
4. 4.

   Cross-outcome error correlations are moderate (not near-perfect)
5. 5.

   Interpretability benefits of unified donor composition are valued

Conversely, separate estimation remains appropriate when:

1. 1.

   Outcomes have heterogeneous data quality requiring isolation
2. 2.

   Scree plots indicate no shared structure (flat profile)
3. 3.

   Policy mechanisms are theoretically independent
4. 4.

   Diagnostics reveal unstable common weights
5. 5.

   Only individual outcome-specific effects matter for the research question

The choice between separate and common-weight estimation is ultimately an empirical question requiring careful diagnostic assessment. The theoretical results above delineate conditions for efficiency gains and clarify the tradeoffs inherent in pooling across outcomes.

## Appendix C Implementation, Inference Procedures and Robustness

This appendix provides detailed inference procedures and robustness diagnostics for the multi-outcome synthetic control analysis. Section [C.1](https://arxiv.org/html/2510.25782v1#A3.SS1 "C.1 Implementation Overview ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") provides a brief overview of implementation conventions with cross-references to the main text. Section [C.2](https://arxiv.org/html/2510.25782v1#A3.SS2 "C.2 Inference Procedures: Joint Conformal and Permutation Tests ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") details conformal and permutation inference algorithms. Sections [C.3](https://arxiv.org/html/2510.25782v1#A3.SS3 "C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")–[C.5](https://arxiv.org/html/2510.25782v1#A3.SS5 "C.5 Placebo Distribution Details ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") present validation diagnostics and sensitivity analyses.

### C.1 Implementation Overview

Core implementation conventions appear in Section [3.3](https://arxiv.org/html/2510.25782v1#S3.SS3 "3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") of the main text, with summary table (Table [1](https://arxiv.org/html/2510.25782v1#S3.T1 "Table 1 ‣ 3.3.6 Summary of Implementation Conventions ‣ 3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) and detailed justification for each design choice. All estimators use intercept-shifted prediction (Equation [4](https://arxiv.org/html/2510.25782v1#S3.E4 "Equation 4 ‣ 3.2 Post-Treatment Prediction: Intercept-Shift Reconstruction ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) and pre-treatment-only weight fitting. Results are reported on original outcome scales throughout.

##### When common weights may be inappropriate.

As discussed in Section [B.5](https://arxiv.org/html/2510.25782v1#A2.SS5 "B.5 When Common Weights May Fail ‣ Appendix B Formal Theory ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"), common-weight estimation may be inappropriate when outcomes exhibit heterogeneous data quality or measurement protocols, scree plots show no clear low-rank structure, policy theory suggests independent causal mechanisms, or leave-one-outcome-out diagnostics reveal unstable weight allocations. See that section for detailed conditions under which the low-rank assumption may fail. The diagnostics in Sections [C.3](https://arxiv.org/html/2510.25782v1#A3.SS3 "C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")–[C.5](https://arxiv.org/html/2510.25782v1#A3.SS5 "C.5 Placebo Distribution Details ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") help assess these conditions empirically.

#### C.1.1 Baseline Donor Weights (Pointer)

For the baseline donor allocations (Average, Concatenated, Combined, and Separate ranges),
see Table [4](https://arxiv.org/html/2510.25782v1#S5.T4 "Table 4 ‣ 5.4.1 Donor Weight Patterns ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") in the main text. All robustness analyses in this appendix
use the same donor pool and preprocessing as in the baseline specification.

Table A4: Baseline donor weights (reference to main text)

|  |  |
| --- | --- |
| Reference | Location |
| Full table | Table [4](https://arxiv.org/html/2510.25782v1#S5.T4 "Table 4 ‣ 5.4.1 Donor Weight Patterns ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") (Results) |
| Notes | Common-weight estimators share the same donor pool and preprocessing |

### C.2 Inference Procedures: Joint Conformal and Permutation Tests

#### C.2.1 Joint Conformal Inference

I adapt the conformal inference approach of Chernozhukov et al. ([2021](https://arxiv.org/html/2510.25782v1#bib.bib13)) to the multi-outcome setting following Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)). The framework tests sharp nulls about simultaneous effects across all KK outcomes:

|  |  |  |
| --- | --- | --- |
|  | H0:τ=τ0,τ∈ℝK,H\_{0}:\ \tau=\tau\_{0},\qquad\tau\in\mathbb{R}^{K}, |  |

with τ0=𝟎K\tau\_{0}=\mathbf{0}\_{K} corresponding to no effects. I implement a first-post conformal test using only the first post-treatment period t=T0+1t=T\_{0}+1.

Algorithm: Joint Conformal Inference (multi-outcome)

1.

Null enforcement. For a candidate τ0∈ℝK\tau\_{0}\in\mathbb{R}^{K}, set Y~1​t​k=Y1​t​k−τ0​k\tilde{Y}\_{1tk}=Y\_{1tk}-\tau\_{0k} for the first post period t=T0+1t=T\_{0}+1 (respecting the same sign/scale conventions as in estimation).
2.

Augment & re-estimate. Augment the sample to include this (null-adjusted) post period and *re-estimate donor weights* using the same objective, preprocessing (demeaning/standardization), and constraints as in estimation.
3.

Test statistic. Compute the post-treatment gap vector and evaluate the qq-norm statistic Sq​(τ0)S\_{q}(\tau\_{0}) (I use q=1q=1 by default).
4.

Reference & pp-value. Form the conformity/reference distribution by re-using the T0T\_{0} pre-periods (or unit placebos) under the same re-estimated weights, and compute the conformal pp-value for τ0\tau\_{0}.

Notes: The conformal test uses the same objective (Average or Concatenated) as the primary estimation to ensure objective-matched inference (see Section [5.5](https://arxiv.org/html/2510.25782v1#S5.SS5 "5.5 Inference and Sensitivity ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") for a comparison of results under both objectives). Asymptotic validity (approximately correct size) holds as T0T\_{0} (and, insofar as it delivers consistent counterfactual estimation, the donor pool size NN) grows, provided the counterfactual is consistently estimated when re-estimated on the augmented sample including the post period (Sun et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib34), §4.4 and Online Appendix A).

The joint-KK conformal test aggregates information across all seven outcomes into a single statistic, avoiding separate outcome-specific tests (and thus additional multiplicity adjustments) while providing a coherent joint assessment of whether any outcome was affected.

#### C.2.2 Permutation-Based Placebo Tests

Permutation inference treats donors as placebo-treated units, requiring an exchangeable donor pool with the treated unit under the null. My donor screening (Appendix [A](https://arxiv.org/html/2510.25782v1#A1 "Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) approximates this exchangeability by selecting municipalities with similar economic structure and pre-treatment trajectories (Abadie et al., [2010](https://arxiv.org/html/2510.25782v1#bib.bib4); Abadie, [2021](https://arxiv.org/html/2510.25782v1#bib.bib3)).

##### Procedure summary.

##### Exact resampling protocol.

Permutation/placebo inference exhaustively evaluates donor relabelings (plus any pre-specified in-time placebos); *weights are re-fit each draw*. Two-sided pp-values are computed from the upper-tail rank with the +1 correction,

|  |  |  |
| --- | --- | --- |
|  | p=#​{T^(b)≥T^obs}+1B+1,ptwo-sided=min⁡(1, 2​min⁡(p,1−p)),p=\frac{\#\{\hat{T}^{(b)}\geq\hat{T}^{\text{obs}}\}+1}{B+1},\qquad p\_{\text{two-sided}}=\min\!\bigl(1,\,2\min(p,1-p)\bigr), |  |

and confidence sets are obtained by inversion of the joint-null test. No random seed is used (no stochastic sampling); B=Ndonors+Nin-time placebosB=N\_{\text{donors}}+N\_{\text{in-time placebos}}.

For each donor u∈𝒟u\in\mathcal{D}, I remove uu from the pool, fit the model as if uu were treated, re-estimate SCM with the same specification, compute the first-post placebo effect vector scaled by that placebo unit’s own pre-treatment SD, and construct the statistic

|  |  |  |
| --- | --- | --- |
|  | stat​(u)=‖Yu,T0+1,⋅−Y^u,T0+1,⋅​(0)su⁣⋅pre‖q,\text{stat}(u)=\left\lVert\frac{Y\_{u,\,T\_{0}+1,\,\cdot}-\hat{Y}\_{u,\,T\_{0}+1,\,\cdot}(0)}{s^{\text{pre}}\_{u\,\cdot}}\right\rVert\_{q}, |  |

noting that SCM permutation tests allow flexible choices of test statistics (Abadie, [2021](https://arxiv.org/html/2510.25782v1#bib.bib3), §3.5).

##### Test statistic choice.

I use the RMSPE ratio statistic, which aggregates standardized gaps across all seven outcomes and five post-treatment quarters:

|  |  |  |
| --- | --- | --- |
|  | RMSPE ratio​(u):=RMSPEpost​(u)RMSPEpre​(u),\text{RMSPE ratio}(u)\;:=\;\frac{\text{RMSPE}\_{\text{post}}(u)}{\text{RMSPE}\_{\text{pre}}(u)}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | RMSPEpost​(u)=1K​Tpost​∑k=1K∑t>T0(Yu​t​k−Y^u​t​k​(0)su​kpre)2,\text{RMSPE}\_{\text{post}}(u)=\sqrt{\frac{1}{K\,T\_{\text{post}}}\sum\_{k=1}^{K}\sum\_{t>T\_{0}}\left(\frac{Y\_{utk}-\hat{Y}\_{utk}(0)}{s^{\text{pre}}\_{uk}}\right)^{2}}, |  |

and RMSPEpre​(u)\text{RMSPE}\_{\text{pre}}(u) is defined analogously over the pre-period. Each placebo unit uu is standardized by its own pre-treatment SD su​kpres^{\text{pre}}\_{uk}, making the RMSPE ratio interpretable as that unit’s fit degradation relative to its own baseline variability. This statistic aggregates information across all post-treatment periods and outcomes, rewarding sustained effects over transient noise. The RMSPE statistic uses the first five fully-exposed post-treatment quarters (2024Q1–2025Q1), excluding 2023Q4 due to partial exposure, to ensure the test statistic reflects periods with complete treatment implementation. As a sensitivity check, I also compute a median-based statistic using only the first post-period:

|  |  |  |
| --- | --- | --- |
|  | mediank⁡|Yu,T0+1,k−Y^u,T0+1,k​(0)su​kpre|,\operatorname{median}\_{k}\!\left|\frac{Y\_{u,\,T\_{0}+1,\,k}-\hat{Y}\_{u,\,T\_{0}+1,\,k}(0)}{s^{\text{pre}}\_{uk}}\right|, |  |

which emphasizes immediate impacts.

##### Validity assumptions.

Conformal inference requires a sufficiently long pre-period and stable estimation applied identically in pre and post; validity follows from exchangeability under H0H\_{0} (finite-sample) or consistency as T0→∞T\_{0}\to\infty (asymptotic). Permutation tests require treated and donor units to be exchangeable under the null, with no systematic selection on latent shocks. Both approaches use identical transformations and first-post focus for comparability. See Sun et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib34)) §4.4 and Online Appendix A for complete technical conditions.

#### C.2.3 Implementation Conventions for Inference

Table [A5](https://arxiv.org/html/2510.25782v1#A3.T5 "Table A5 ‣ C.2.3 Implementation Conventions for Inference ‣ C.2 Inference Procedures: Joint Conformal and Permutation Tests ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") summarizes the specific choices for conformal and permutation inference procedures.

|  |  |
| --- | --- |
| Convention | Specification |
| Treatment period | Post periods include treatment date; partial exposure labeled. |
| Intercept shift | Pre-treatment means removed before weight estimation; restored in reconstruction. |
| Standardization (weight fitting) | Treated unit’s pre-treatment s1​kpres\_{1k}^{\text{pre}} for each kk (applied uniformly during weight estimation). |
| Standardization (test statistic) | Unit-specific pre-treatment su​kpres\_{uk}^{\text{pre}} for each placebo unit uu and outcome kk. |
| Sign alignment | Outcome-specific ak∈{+1,−1}a\_{k}\in\{+1,-1\} applied post-standardization, pre-optimization. |
| Weight constraints | Simplex weights (γj≥0\gamma\_{j}\geq 0, ∑jγj=1\sum\_{j}\gamma\_{j}=1), no ridge penalty. |
| Conformal config | First post-treatment period; L1L\_{1} score on transformed residuals. |
| Permutation config | Same transformations/scaling across placebo units; pooled 𝒫\mathcal{P} with in-time placebos. |
| Primary statistic | RMSPE ratio across all post periods and outcomes. |
| Alternate statistic | Median absolute first-post gap (sensitivity check). |
| Results reporting | All effects on original scales via exact intercept-shift back-transformation. |

Table A5: Inference implementation conventions.

### C.3 Additional Diagnostics

#### C.3.1 Leave-One-Donor-Out (LODO)

LODO diagnostics assess sensitivity to individual donor exclusion by sequentially removing each donor, re-estimating weights using identical specifications, and measuring impact on pre-treatment fit quality. Figure [A1](https://arxiv.org/html/2510.25782v1#A3.F1 "Figure A1 ‣ C.3.1 Leave-One-Donor-Out (LODO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents results for the average estimator.

The separate estimator exhibits highest sensitivity: excluding Aguadilla increases mean pre-period RMSPE from 0.752 to 0.802 (+6.70%). The concatenated and average estimators have baselines of 0.843 and 0.878; excluding Aguadilla raises them to 0.883 (+4.80%) and 0.924 (+5.26%), respectively. For Average, Arecibo and Hatillo exclusions change RMSPE by ∼\sim0.000% (negligible); Bayamón and Humacao produce small increases (+0.16% and +0.77%), while Cayey slightly improves fit (−0.30%-0.30\%). This robustness advantage stems from information pooling: the average estimator distributes influence across the donor pool rather than relying heavily on any single municipality.

![Refer to caption](figures/average/leave_one_donor_out.png)


Figure A1: Leave-one-donor-out sensitivity (average estimator). Bars show absolute change in mean pre-treatment RMSPE when each donor is excluded and weights re-estimated. Maximum degradation is 5.2% (Aguadilla), confirming acceptable stability. The minimal impact from excluding Arecibo and Hatillo reflects their near-zero weights in the full-sample solution. The relatively uniform distribution validates that the six-donor pool provides sufficient support without critical dependence on any individual municipality.

#### C.3.2 Leave-One-Outcome-Out (LOOO)

When outcomes share common factor structure, a single set of weights estimated on all outcomes should maintain reasonable fit quality even when individual outcomes are excluded. Table [A6](https://arxiv.org/html/2510.25782v1#A3.T6 "Table A6 ‣ C.3.2 Leave-One-Outcome-Out (LOOO) ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents LOOO fit quality for concatenated and average estimators.

Both estimators achieve mean LOOO RMSPE close to full-sample baselines. The average estimator shows mean LOOO RMSPE of 0.893 (baseline 0.878); concatenated shows similar performance (mean 0.928 vs. baseline 0.843). Excluding sector 18 revenue produces highest LOOO RMSPE for both estimators (1.006 average, 1.051 concatenated), while excluding arts/entertainment employment yields lowest (0.675 average, 0.837 concatenated). The relatively uniform LOOO distribution confirms robust shared structure with no single outcome driving the common-weight solution.

Table A6: Leave-one-outcome-out fit quality (pre-treatment RMSPE). Each row shows mean standardized RMSPE across all seven outcomes when the corresponding outcome is excluded from weight optimization. Lower values indicate better out-of-sample fit. *Note*: Baseline values (0.843 concat, 0.878 average, 0.752 separate) report mean per-outcome RMSPE for cross-estimator comparison, distinct from the optimization objectives that appear in sensitivity analyses.

|  |  |  |
| --- | --- | --- |
| Excluded Outcome | Concat RMSPE | Average RMSPE |
| Sector 18 revenue | 0.989 | 1.006 |
| Sector 14 revenue | 1.027 | 0.989 |
| Sector 16 revenue | 0.951 | 0.928 |
| Accommodation/Food Emp. | 0.673 | 0.728 |
| Arts/Entertainment Emp. | 0.837 | 0.675 |
| Late Public Disorder | 1.051 | 1.022 |
| Violent Crime | 0.969 | 0.904 |
| Mean across exclusions | 0.928 | 0.893 |
| Baseline (all outcomes) | 0.843 | 0.878 |

#### C.3.3 Magnitude Verification: Accommodation/Food Services Employment

The large employment effect (+67.80 per 1,000, +7.59σ\sigma) warrants explicit verification that standardized and original-scale magnitudes are internally consistent and not artifacts of measurement error or data processing issues. Table [A7](https://arxiv.org/html/2510.25782v1#A3.T7 "Table A7 ‣ C.3.3 Magnitude Verification: Accommodation/Food Services Employment ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents a comprehensive reconciliation of effect magnitudes across units and confirms data quality.

Table A7: Employment outcome magnitude verification (Accommodation/Food Services, NAICS 72)

|  |  |  |
| --- | --- | --- |
| Statistic | Value | Units |
| Treatment Effect (2023Q4–2025Q1, N=6 quarters) | | |
| Standardized | 7.59 | σ\sigma |
| Original scale | 67.80 | per 1,000 residents |
| Across-quarter std. dev. | 9.30 | per 1,000 residents |
| Pre-treatment baseline (2019Q1–2023Q3, N=19 quarters) | | |
| Mean (San Juan) | 57.60 | per 1,000 residents |
| Standard deviation | 8.93 | per 1,000 residents |
| Mean (Synthetic) | 57.60 | per 1,000 residents |
| Mean gap (pre-fit) | 0.00 | per 1,000 residents |
| Post-treatment levels (2023Q4–2025Q1) | | |
| Mean (San Juan) | 125.40 | per 1,000 residents |
| Mean (Synthetic) | 57.60 | per 1,000 residents |
| Difference | 67.80 | per 1,000 residents |
| Verification | | |
| De-standardization check | 7.59×8.93=67.777.59\times 8.93=67.77 | ≈67.80\approx 67.80 ✓ |
| Effect as % of pre-mean | 117.7% | (67.80/57.60) |
| Effect in pre-SD units | 7.59σ\sigma | (67.80/8.93) |
| Data quality confirmations | | |
| Population denominator | ACS 2023 5-year | Fixed throughout |
| Employment source | PR Dept. of Labor | Quarterly |
| Interpolation applied | None | — |
| Calculation | (avg\_emp / pop) ×\times 1000 | Standard |

Notes: Treatment effect is the average gap between actual and synthetic control across six post-treatment quarters. The standardized effect (σ\sigma units) converts to original scale by multiplying by the pre-treatment standard deviation (8.93 per 1,000). Pre-treatment means are computed from standardized values in merged\_average.csv (which are in σ\sigma units) rather than raw panel data. Post-treatment levels are inferred as pre-mean plus treatment effect. The calculation confirms internal consistency of reported magnitudes: no denominator changes, measurement artifacts, or interpolation issues affect the large observed employment response.

The verification confirms four critical points:

##### Internal consistency.

The standardized effect correctly de-scales to original units via the pre-treatment standard deviation: 7.59​σ×8.93=67.77≈67.807.59\sigma\times 8.93=67.77\approx 67.80 per 1,000 residents. The minor rounding difference (0.03 per 1,000) is negligible and reflects floating-point precision in the JSON serialization chain.

##### Magnitude interpretation.

The effect represents a 117.7% increase relative to San Juan’s pre-treatment mean employment level (57.60 per 1,000). In absolute terms, this corresponds to moving from approximately 19,700 workers (pre-treatment) to 42,900 workers (post-treatment) given San Juan’s population of 342,259 residents (ACS 2023). This large shift is consistent with the hotel exemption mechanism discussed in Appendix [D.2.3](https://arxiv.org/html/2510.25782v1#A4.SS2.SSS3 "D.2.3 The Hotel Exemption and Within-Sector Employment Reallocation ‣ D.2 Theoretical Mechanisms ‣ Appendix D Context & Mechanisms ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"): hotels expanded employment to capture demand displaced from restricted standalone venues.

##### Denominator stability.

The population denominator uses fixed ACS 2023 5-year estimates (342,259 residents for San Juan) throughout the entire study window (2019Q1–2025Q1), avoiding confounding from population changes or demographic shifts. Per-capita rates are computed consistently as (average employment / population) ×\times 1,000 for all municipalities and time periods.

##### Measurement quality.

Employment data are quarterly administrative records from the Puerto Rico Department of Labor and Human Resources with no interpolation applied to the accommodation/food services series. The single interpolated observation in the entire panel affects a different outcome (arts/entertainment employment for Arecibo in 2023Q4, as documented in Appendix [A.3.3](https://arxiv.org/html/2510.25782v1#A1.SS3.SSS3 "A.3.3 Stage 3: Panel Construction & Normalization ‣ A.3 Six-Stage Donor Pool Screening ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) and does not impact the treated unit’s employment measurement. Raw employment counts are directly converted to per-capita rates without intermediate transformations that could introduce artifacts.

These verification steps confirm that the large employment effect reflects a genuine shift in San Juan’s labor market rather than measurement error, scaling artifacts, or data processing issues. The effect magnitude—though striking—is plausible given the policy’s differential treatment of hotel versus standalone establishments and is robust across estimators (Separate: +62.34 per 1,000; Average: +67.80 per 1,000; Table [6](https://arxiv.org/html/2510.25782v1#S5.T6 "Table 6 ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")).

#### C.3.4 Cross-Validation

Held-out temporal fit provides an additional diagnostic for estimator performance. I implement blocked 5-fold cross-validation on the 19 pre-treatment quarters, partitioning into five contiguous blocks and sequentially holding out each block while estimating weights on the remaining four.

Figure [A2](https://arxiv.org/html/2510.25782v1#A3.F2 "Figure A2 ‣ C.3.4 Cross-Validation ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents mean held-out RMSPE across folds. The separate estimator achieves the best CV RMSPE (0.912), followed by average (0.925) and concatenated (0.925). The separate estimator wins for 4 of 7 outcomes. However, superior CV performance tests prediction accuracy, not post-treatment bias. The separate estimator’s flexibility achieves better in-sample fit but facilitates overfitting to transient noise. The CV penalty for the average estimator represents the cost of constraining weights to balance multiple outcomes—a sacrifice that purchases bias reduction through information pooling. In policy evaluation contexts where outcomes share theoretical linkages through common mechanisms (here, alcohol availability restrictions affecting multiple retail sectors and public safety), coherent cross-outcome interpretation and structural bias reduction often outweigh pure predictive accuracy as evaluation criteria.

![Refer to caption](figures/compare/cv_holdout_fit.png)


Figure A2: Cross-validation: Held-out pre-treatment fit. Bars show mean RMSPE from 5-fold blocked CV on the pre-treatment period. Separate achieves best out-of-sample prediction (mean 0.912), followed by Average (0.925) and Concatenated (0.925). The separate estimator’s superior CV performance reflects outcome-specific optimization flexibility, while the average estimator’s penalty represents the bias–variance tradeoff: sacrificing pre-period prediction accuracy for reduced post-treatment overfitting bias through information pooling.

##### Uniform weights baseline.

Table [A8](https://arxiv.org/html/2510.25782v1#A3.T8 "Table A8 ‣ Uniform weights baseline. ‣ C.3.4 Cross-Validation ‣ C.3 Additional Diagnostics ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") compares optimized estimators against a naïve uniform-weights baseline (γj=1/N0\gamma\_{j}=1/N\_{0} for all donors). The separate estimator achieves the largest improvement (15.1%) through outcome-specific flexibility, while common-weight estimators show modest gains (0.8–4.7%) relative to equal weighting. The small gap between optimized average (0.878) and uniform (0.885) reflects the high quality of the donor pool: municipalities were pre-screened for economic similarity (Appendix [A](https://arxiv.org/html/2510.25782v1#A1 "Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")), making simple averaging nearly as effective as constrained optimization. This validates the donor selection protocol while demonstrating that optimization still delivers measurable—if modest—gains over naïve approaches.

Table A8: Pre-treatment fit comparison: Optimized vs. Uniform weights

|  |  |  |
| --- | --- | --- |
| Estimator | Mean Pre-RMSPE | Improvement vs. Uniform |
| Uniform (baseline) | 0.885 | — |
| Separate | 0.752 | −15.1%-15.1\% |
| Concatenated | 0.843 | −4.7%-4.7\% |
| Combined | 0.846 | −4.4%-4.4\% |
| Average | 0.878 | −0.8%-0.8\% |

Notes: RMSPE computed on standardized outcomes (pre-treatment period 2019Q1–2023Q3, T0=19T\_{0}=19 quarters). Uniform baseline assigns equal weight (1/N0=1/61/N\_{0}=1/6) to each donor. “Improvement” shows the percentage reduction in RMSPE achieved by optimization. The modest gap between Average (0.878) and Uniform (0.885) reflects careful donor selection: municipalities were pre-screened for economic structure similarity, making simple averaging competitive with optimization. The Separate estimator’s larger advantage (15.1%) comes from outcome-specific flexibility, which also increases overfitting risk in post-treatment estimation.

### C.4 Combined Estimator ν\nu-Sensitivity

The combined estimator interpolates between concatenated (ν=0\nu=0) and averaged (ν=1\nu=1) objectives. I conduct sensitivity analysis by sweeping ν∈[0,1]\nu\in[0,1] in increments of 0.25, re-estimating weights at each value to assess robustness of (i) pre-treatment fit quality, (ii) treatment effect estimates, and (iii) permutation inference.

The scale-matching heuristic (derived in [3.3.4](https://arxiv.org/html/2510.25782v1#S3.SS3.SSS4 "3.3.4 Combined Estimator and Parameter Selection ‣ 3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) yields ν=1.0\nu=1.0, selecting the pure averaged estimator for the main results. Across the grid, donor weights transition smoothly: Aguadilla increases (0.374 →\to 0.419), Bayamón increases (0.241 →\to 0.453), Hatillo declines (0.090 →\to 0.000), Humacao declines (0.294 →\to 0.050), and Cayey rises from near zero to 0.078; Arecibo remains near zero. The treated standardized effects at ν=1.0\nu=1.0 match the main text (Sector 18 +0.012​σ+0.012\sigma, Sector 16 +0.018​σ+0.018\sigma, Accommodation/Food +7.59​σ+7.59\sigma, Arts/Entertainment +0.32​σ+0.32\sigma, Late Disorder +0.01​σ+0.01\sigma, Violent Crime −0.26​σ-0.26\sigma). Figure [A5](https://arxiv.org/html/2510.25782v1#A3.F5 "Figure A5 ‣ Donor weight allocations across 𝜈. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") shows the weight allocations remain stable across the ν\nu grid, with donor contributions varying smoothly as the estimator transitions from concatenated to averaged objectives. The smooth trajectory confirms robustness: any ν∈[0.3,0.7]\nu\in[0.3,0.7] would yield qualitatively similar results.

##### Inference robustness across ν\nu.

Figure [A3](https://arxiv.org/html/2510.25782v1#A3.F3 "Figure A3 ‣ Inference robustness across 𝜈. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") shows permutation p-values across the ν\nu grid. The flat profile at p=0.071p=0.071 (the minimum achievable value on the discrete 1/141/14 grid) demonstrates that treatment effect detection is robust to aggregation method choice. Whether weights prioritize concatenated (ν=0\nu=0) or averaged (ν=1\nu=1) objectives, the permutation test yields identical inference: San Juan ranks first among 14 placebos (6 donor + 7 in-time + treated) for all specifications, with RMSPE ratios ranging narrowly from 3.67 to 3.74. This invariance demonstrates that the inference conclusions are not artifacts of estimator choice.

![Refer to caption](figures/compare/nu_pvalue_robustness.png)


Figure A3: Inference robustness across ν\nu. Permutation p-values (joint null test, RMSPE ratio statistic) remain constant at the minimum achievable value (p=0.071p=0.071) across all ν∈[0,1]\nu\in[0,1]. Mid-p values (accounting for ties) similarly show no variation. This stability demonstrates that treatment effect detection is insensitive to the choice between concatenated and averaged aggregation methods. The red dotted line marks the conventional significance threshold (α=0.05\alpha=0.05), which is unattainable on the discrete 1/141/14 permutation grid.

##### Treatment effect stability across ν\nu.

Figure [A4](https://arxiv.org/html/2510.25782v1#A3.F4 "Figure A4 ‣ Treatment effect stability across 𝜈. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") displays post-treatment effects (standardized units) for all seven outcomes across the ν\nu grid, with 90% placebo bands. Employment outcomes show moderate sensitivity to ν\nu: accommodation/food employment ranges from +6.45​σ+6.45\sigma (ν=0\nu=0) to +7.59​σ+7.59\sigma (ν=1\nu=1), while arts/entertainment employment ranges from +0.23​σ+0.23\sigma to +0.32​σ+0.32\sigma. Revenue and crime outcomes remain stable and near zero across all specifications, with treated trajectories consistently within or near placebo bands. The qualitative pattern—economically meaningful employment reallocations without commensurate crime reductions—persists across the entire ν\nu grid, demonstrating that the central narrative is not driven by the choice of objective weighting.

![Refer to caption](figures/compare/nu_barcode.png)


Figure A4: Treatment effect sensitivity to ν\nu. Each panel shows the mean post-treatment effect (2023Q4–2025Q1) in standardized units as ν\nu varies from 0 (concatenated) to 1 (averaged). Gray bands indicate 5th–95th percentile of the placebo distribution (6 donor + 7 in-time placebos). Accommodation/food employment exhibits moderate sensitivity to ν\nu (+6.45σ\sigma at ν=0\nu=0 to +7.59σ\sigma at ν=1\nu=1), reflecting the variation in optimal donor weights across specifications. Revenue outcomes (Sectors 14, 16, 18) and crime outcomes (late-night public disorder, violent crime) remain stable and near zero. The central empirical pattern—activation of economic mechanisms without corresponding crime reductions—holds across all specifications.

##### Pre-treatment imbalance at selected ν\nu values.

Table [A9](https://arxiv.org/html/2510.25782v1#A3.T9 "Table A9 ‣ Pre-treatment imbalance at selected 𝜈 values. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reports the two objective components (qavg,qcat)(q\_{\text{avg}},q\_{\text{cat}}) and their weighted combination for the grid of ν\nu values. At ν=0\nu=0 (pure concatenated), qcatq\_{\text{cat}} is minimized; at ν=1\nu=1 (pure averaged), qavgq\_{\text{avg}} is minimized. Intermediate values trace the Pareto frontier shown in Figure [4](https://arxiv.org/html/2510.25782v1#S5.F4 "Figure 4 ‣ Imbalance frontier. ‣ 5.4.1 Donor Weight Patterns ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan"). The combined objective decreases monotonically as ν\nu increases from 0 to 1, supporting the scale-matching heuristic’s selection of ν=1.0\nu=1.0.

Table A9: Pre-treatment imbalance across ν\nu values (combined estimator)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ν\nu | qavgq\_{\text{avg}} | qcatq\_{\text{cat}} | Combined: ν​qavg+(1−ν)​qcat\nu q\_{\text{avg}}+(1-\nu)q\_{\text{cat}} | Estimator |
| 0.00 | 0.260 | 0.859 | 0.859 | Concatenated |
| 0.25 | 0.253 | 0.860 | 0.708 |  |
| 0.50 | 0.247 | 0.864 | 0.555 |  |
| 0.75 | 0.242 | 0.871 | 0.399 |  |
| 1.00 | 0.240 | 0.885 | 0.240 | Averaged |

Notes: Imbalance metrics computed on standardized pre-treatment outcomes (2019Q1–2023Q3, T0=19T\_{0}=19 quarters). qavgq\_{\text{avg}} measures RMSE on the averaged outcome (mean across K=7K=7 outcomes at each time period); qcatq\_{\text{cat}} measures RMSE on the concatenated (T0×K)(T\_{0}\times K) stack. The combined objective is minimized at ν=1.0\nu=1.0 (pure averaged estimator), which is selected via the scale-matching heuristic (main text Section [3.3.4](https://arxiv.org/html/2510.25782v1#S3.SS3.SSS4 "3.3.4 Combined Estimator and Parameter Selection ‣ 3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). As ν\nu increases from 0 to 1, the estimator transitions from minimizing concatenated imbalance to minimizing averaged imbalance; the combined objective decreases monotonically, supporting the averaged estimator’s selection. See Figures [4](https://arxiv.org/html/2510.25782v1#S5.F4 "Figure 4 ‣ Imbalance frontier. ‣ 5.4.1 Donor Weight Patterns ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") and [A5](https://arxiv.org/html/2510.25782v1#A3.F5 "Figure A5 ‣ Donor weight allocations across 𝜈. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") for visual representations of this Pareto frontier.

##### Donor weight allocations across ν\nu.

Table [A10](https://arxiv.org/html/2510.25782v1#A3.T10 "Table A10 ‣ Donor weight allocations across 𝜈. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") reports donor weight allocations for each ν\nu value, demonstrating smooth transitions without extreme concentration. As ν\nu increases from 0 to 1, Aguadilla’s weight increases moderately (0.374 →\to 0.419, +12%), Bayamón increases more substantially (0.241 →\to 0.453, +88%), while Humacao declines sharply (0.294 →\to 0.050, −83%-83\%) and Hatillo declines to zero (0.090 →\to 0.000). Cayey enters with modest weight at higher ν\nu values (0.078 at ν=1.0\nu=1.0), while Arecibo remains excluded across all specifications. Effective sample sizes range from Neff=2.8N\_{\text{eff}}=2.8 (ν=0.75\nu=0.75) to Neff=3.4N\_{\text{eff}}=3.4 (ν=0.0\nu=0.0), indicating balanced donor representation without critical dependence on any single municipality. The smooth weight trajectories validate robustness of donor pool composition across objective specifications.

Table A10: Donor weight allocations across ν\nu

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ν\nu | Aguadilla | Arecibo | Bayamón | Cayey | Hatillo | Humacao |
| 0.00 | 0.374 | 0.000 | 0.241 | 0.000 | 0.090 | 0.294 |
| 0.25 | 0.391 | 0.000 | 0.283 | 0.000 | 0.058 | 0.268 |
| 0.50 | 0.408 | 0.000 | 0.339 | 0.000 | 0.018 | 0.235 |
| 0.75 | 0.424 | 0.000 | 0.396 | 0.012 | 0.000 | 0.168 |
| 1.00 | 0.419 | 0.000 | 0.453 | 0.078 | 0.000 | 0.050 |

Notes: Each row sums to 1.0 by simplex constraints. Weights are estimated by minimizing the combined objective Jν​(γ)=ν​qavg​(γ)+(1−ν)​qcat​(γ)J\_{\nu}(\gamma)=\nu q\_{\text{avg}}(\gamma)+(1-\nu)q\_{\text{cat}}(\gamma) subject to γj≥0\gamma\_{j}\geq 0 and ∑jγj=1\sum\_{j}\gamma\_{j}=1. As ν\nu increases from 0 (concatenated) to 1 (averaged), Aguadilla and Bayamón increase their weight shares while Humacao and Hatillo decline. Arecibo receives near-zero weight across all specifications, consistent with its lower similarity scores in the demographic screening stage (Appendix [A](https://arxiv.org/html/2510.25782v1#A1 "Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Effective N ranges from 2.8 to 3.4, indicating balanced donor representation without extreme concentration.

![Refer to caption](figures/compare/nu_sweep.png)


Figure A5: Imbalance frontier (1D view).
The combined objective Jν​(γ^)=ν​qavg​(γ^)+(1−ν)​qcat​(γ^)J\_{\nu}(\hat{\gamma})=\nu\,q\_{\mathrm{avg}}(\hat{\gamma})+(1-\nu)\,q\_{\mathrm{cat}}(\hat{\gamma}) is traced over ν∈{0,0.25,0.5,0.75,1}\nu\in\{0,0.25,0.5,0.75,1\}, interpolating between the concatenated (ν=0\nu{=}0) and averaged (ν=1\nu{=}1) objectives. This 1D view complements the 2D frontier in Fig. [4](https://arxiv.org/html/2510.25782v1#S5.F4 "Figure 4 ‣ Imbalance frontier. ‣ 5.4.1 Donor Weight Patterns ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

##### Consolidated estimator comparison.

Table [A11](https://arxiv.org/html/2510.25782v1#A3.T11 "Table A11 ‣ Consolidated estimator comparison. ‣ C.4 Combined Estimator 𝜈-Sensitivity ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") consolidates pre-treatment fit, imbalance metrics, and inference results across all four estimators. The Separate estimator achieves best pre-treatment fit (RMSPE 0.752) but sacrifices cross-outcome coherence. Common-weight estimators trade modest fit quality for interpretable donor allocation and consistent treatment effect inference.

Table A11: Estimator comparison summary

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Estimator | Pre-RMSPE | qavgq\_{\text{avg}} | qcatq\_{\text{cat}} | pp-value |
| Separate | 0.752 | — | — | — |
| Average | 0.878 | 0.240 | 0.885 | 0.071 |
| Concat | 0.843 | 0.260 | 0.859 | 0.071 |
| Combined | 0.846 | 0.247 | 0.864 | 0.071 |

### C.5 Placebo Distribution Details

#### C.5.1 Augmented Placebo Pool Construction

With six donors, unit-placebo inference alone yields a minimum attainable pp-value of 1/7≈0.1431/7\approx 0.143. I augment with seven in-time placebos (treating pre-treatment periods as hypothetical intervention dates), yielding 14 total observations: 13 placebos (6 donor-unit + 7 in-time) plus the treated unit. This configuration yields a minimum attainable permutation pp-value of 1/14≈0.0711/14\approx 0.071.

In-time placebos use pre-treatment periods as hypothetical treatment dates, splitting the available pre-period into pseudo-PRE and pseudo-POST windows. For example, treating 2021 Q2 as a hypothetical intervention date uses 2019 Q1–2021 Q1 as pseudo-PRE (9 quarters) and 2021 Q2–2023 Q3 as pseudo-POST (10 quarters). I select seven consecutive quarterly pseudo-intervention dates from 2020 Q4 (2020-12-31) through 2022 Q2 (2022-06-30)—2020 Q4, 2021 Q1, 2021 Q2, 2021 Q3, 2021 Q4, 2022 Q1, 2022 Q2—each separated by one quarter and requiring at least two years (≥8\geq 8 quarters) of pre-treatment data for every placebo. These in-time placebos test whether the observed post-treatment effect magnitude is unusual relative to spurious fluctuations during the pre-treatment period, complementing the cross-sectional comparison provided by donor-unit placebos.

#### C.5.2 Discrete p-Value Grid and Permutation Quantiles

The discrete nature of permutation inference in small samples creates a stepped p-value grid. Table [A12](https://arxiv.org/html/2510.25782v1#A3.T12 "Table A12 ‣ C.5.2 Discrete p-Value Grid and Permutation Quantiles ‣ C.5 Placebo Distribution Details ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") presents both the achievable p-value grid and the empirical placebo distribution quantiles.

Table A12: Permutation inference: p-value grid and placebo distribution. Left panel shows the discrete p-value grid; right panel shows placebo distribution quantiles. San Juan ranks 1st of 14 (RMSPE ratio 3.984), yielding p=1/14=0.071p=1/14=0.071.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| p-Value Grid | | Placebo Distribution | | |
| San Juan Rank | p-value | Statistic | RMSPE ratio | Unit/Period |
| 1st of 14 | 0.071 | Maximum | 3.984 | San Juan (treated) |
| 2nd of 14 | 0.143 | 95th pct | 2.551 | Aguadilla (donor) |
| 3rd of 14 | 0.214 | 90th pct | 1.509 | Arecibo (donor) |
| 8th of 14 | 0.571 | Median | 1.290 | Cayey (donor) |
| 14th of 14 | 1.000 | Minimum | 0.915 | Humacao (donor) |
| San Juan (observed) | | Treated | 3.984 | Actual intervention |
| Percentile rank | | 100th | Exceeds all 13 placebos | |

Notes: Placebo pool comprises 6 donor municipalities (Aguadilla, Arecibo, Bayamón, Cayey, Hatillo, Humacao) and 7 consecutive quarterly in-time placebos for San Juan (2020-12-31, 2021-03-31, 2021-06-30, 2021-09-30, 2021-12-31, 2022-03-31, 2022-06-30). The permutation test yields p=0.071p=0.071, the minimum attainable with 13 placebos. San Juan’s RMSPE ratio substantially exceeds both donor-unit and in-time placebo distributions, providing stronger evidence than the donor-only comparison (p=1/7=0.143p=1/7=0.143).

#### C.5.3 Outcome-Specific Contributions to Permutation Ranking

Table [A13](https://arxiv.org/html/2510.25782v1#A3.T13 "Table A13 ‣ C.5.3 Outcome-Specific Contributions to Permutation Ranking ‣ C.5 Placebo Distribution Details ‣ Appendix C Implementation, Inference Procedures and Robustness ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") decomposes San Juan’s RMSPE ratio by outcome, showing which domains drive the permutation ranking.

Table A13: Outcome-specific contributions to permutation ranking. Mean effects average across six post-treatment quarters (2023Q4–2025Q1). Standardized effects express magnitudes relative to San Juan’s pre-treatment SD.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Outcome | Mean Effect | Std. Effect | Pre-Treatment SD | Contribution |
| Sector 18 (Restaurants/Bars) | +0.179+0.179 | +0.012​σ+0.012\sigma | 0.0210.021 | Low |
| Sector 14 (Supermarkets/Liquor) | +0.003+0.003 | +0.00044​σ+0.00044\sigma | 0.00570.0057 | Low |
| Sector 16 (Gas/Convenience) | +0.067+0.067 | +0.018​σ+0.018\sigma | 0.00700.0070 | Low |
| Accommodation/Food Emp. | +67.80+67.80 | +7.59​σ+7.59\sigma | 8.938.93 | High |
| Arts/Entertainment Emp. | +0.23+0.23 | +0.32​σ+0.32\sigma | 0.710.71 | Low |
| Late Night Public Disorder | +0.00082+0.00082 | +0.01​σ+0.01\sigma | 0.0660.066 | Low |
| Violent Crime | −0.081-0.081 | −0.26​σ-0.26\sigma | 0.3110.311 | Low |
| RMSPE ratio (aggregate): 3.984 | | | | |

Notes: Revenue effects measured in millions of US dollars per quarter. Employment and crime effects measured as changes per 1,000 residents. Standardized effects are mean effects divided by San Juan’s pre-treatment SD. Contribution categories:

* High: |std. effect|>1.0\lvert\text{std. effect}\rvert>1.0
* Moderate: 0.5<|std. effect|≤1.00.5<\lvert\text{std. effect}\rvert\leq 1.0
* Low: |std. effect|≤0.5\lvert\text{std. effect}\rvert\leq 0.5

#### C.5.4 Alternate Statistic: First-Post Median Gap

As a sensitivity check, I compute an alternate test statistic using only the first post-treatment period (2023 Q4):

|  |  |  |
| --- | --- | --- |
|  | Median​(u):=mediank=1,…,K⁡|Yu,T0+1,k−Y^u,T0+1,k​(0)s1​kpre|.\mathrm{Median}(u)\;:=\;\operatorname{median}\_{k=1,\ldots,K}\left|\frac{Y\_{u,\,T\_{0}+1,\,k}-\hat{Y}\_{u,\,T\_{0}+1,\,k}(0)}{s^{\text{pre}}\_{1k}}\right|. |  |

This statistic emphasizes immediate impacts and is less sensitive to sustained trends across multiple quarters. San Juan’s median gap yields p=0.286p=0.286 (4th of 14), providing more conservative evidence than the RMSPE ratio. This contrast suggests that San Juan’s effects, while substantial in aggregate, show more heterogeneity in the first post-treatment period across outcomes. The RMSPE ratio (p=0.071p=0.071) provides stronger evidence by integrating information across the five fully-exposed post-treatment quarters and accounting for temporal persistence.

## Appendix D Context & Mechanisms

This appendix provides extended institutional and theoretical context for San Juan’s Public Order Code evaluation. Section [D.1](https://arxiv.org/html/2510.25782v1#A4.SS1 "D.1 Institutional Background ‣ Appendix D Context & Mechanisms ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") elaborates on the ordinance’s enforcement, stakeholder perspectives, and legal challenges. Section [D.2](https://arxiv.org/html/2510.25782v1#A4.SS2 "D.2 Theoretical Mechanisms ‣ Appendix D Context & Mechanisms ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") discusses theoretical mechanisms linking alcohol restrictions to economic activity, crime reduction, and tourism impacts. Data sources, outcome construction, and donor pool screening methodology appear in Appendix [A](https://arxiv.org/html/2510.25782v1#A1 "Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan").

### D.1 Institutional Background

#### D.1.1 Population Characteristics and Policy Context

Puerto Rico has been characterized as a “wet” environment with relatively high drinking levels (Caetano et al., [2016](https://arxiv.org/html/2510.25782v1#bib.bib12)), though a 2001 survey revealed that 93% to 95% of Puerto Ricans favor restrictions on alcohol consumption in public places (Harwood et al., [2004](https://arxiv.org/html/2510.25782v1#bib.bib26)). This widespread support suggests the municipal ordinance aligned with prevailing public sentiment, though the specific form and stringency of restrictions remained contested among business stakeholders and residents.

#### D.1.2 Ordinance Scope and Enforcement

The ordinance restricts on-premise alcohol sales during 1–6 AM on weekdays and 2–6 AM on weekends across restaurants/bars (Sector 18), gas stations/convenience stores (Sector 16), supermarkets/liquor stores (Sector 14), and hospitality venues (Municipio Autónomo de San Juan, Legislatura
Municipal, [2023](https://arxiv.org/html/2510.25782v1#bib.bib29)). Mondays that are legal holidays follow the weekend schedule (2:00–6:00 AM restricted hours). Hotels regulated by the Puerto Rico Tourism Company retain limited rights to serve registered guests for on-premises consumption during restricted hours, creating within-sector heterogeneity that may affect employment measures (Municipio Autónomo de San Juan, Legislatura
Municipal, [2023](https://arxiv.org/html/2510.25782v1#bib.bib29), Art. 2.101). Private events by non-profit civic, educational, or professional organizations lacking commercial purpose are exempt from restrictions.

Violations carry an administrative fine of $5,000, with establishments incurring three infractions within one year facing permit cancellation and a one-year prohibition on new permit applications (Municipio Autónomo de San Juan, Legislatura
Municipal, [2023](https://arxiv.org/html/2510.25782v1#bib.bib29), Art. 2.101). This escalating enforcement structure creates financial incentives for compliance beyond the initial monetary penalty. I do not observe enforcement data directly and cannot assess implementation fidelity or compliance rates empirically. The analysis assumes uniform enforcement across establishments, though actual compliance may vary by venue type, neighborhood, or ownership structure.

#### D.1.3 Stakeholder Perspectives and Legal Challenge

Municipal authorities argued that restricting late-night alcohol sales was necessary to balance a vibrant nightlife economy with public safety and residential tranquility (Municipio Autónomo de San Juan, Legislatura
Municipal, [2023](https://arxiv.org/html/2510.25782v1#bib.bib29)), emphasizing harm reduction objectives and quality-of-life concerns for residents living near commercial entertainment districts. The ordinance’s stated objectives included reducing public disorder incidents, alcohol-related violence, and noise disturbances during late-night hours.

Business associations countered that the policy would cause significant economic harm without meaningfully improving public safety, potentially leading to business closures and job losses while merely displacing rather than eliminating social problems to unrestricted hours or neighboring municipalities (Asociación de Empresarios Calle Loíza,
Inc., et al. v. Municipality of San Juan, [2023](https://arxiv.org/html/2510.25782v1#bib.bib8)). These competing claims—harm reduction versus economic displacement—motivated my joint examination of economic and public safety outcomes to assess whether the ordinance achieved its stated objectives and whether economic costs accompanied any safety benefits.

The ordinance later withstood federal court challenge under rational-basis review, where the court noted that “a legislative choice … may be based on rational speculation unsupported by evidence or empirical data” (Asociación de Empresarios Calle Loíza,
Inc., et al. v. Municipality of San
Juan, [2024](https://arxiv.org/html/2510.25782v1#bib.bib9)), confirming that judicial scrutiny does not require systematic empirical validation of policy premises. This legal standard highlights the value of empirical policy evaluation independent of judicial review—courts apply deferential standards to legislative judgments, but evidence-based policymaking benefits from rigorous causal analysis of actual policy effects.

### D.2 Theoretical Mechanisms

#### D.2.1 Economic Rationale and External Costs

Alcohol generates significant “external costs”—harms borne by people other than the drinker, such as victims of alcohol-related violence, traffic accidents, and public disorder—which are not reflected in market prices, providing economic rationale for government intervention (Cook and Moore, [2002](https://arxiv.org/html/2510.25782v1#bib.bib15)). When individual consumption decisions impose costs on third parties, market equilibrium typically results in overconsumption relative to the social optimum. Private benefits to drinkers exceed social benefits when external costs are unpriced, leading to market failure.

Temporal restrictions represent availability reduction operating through time rather than price or quantity channels. By prohibiting sales during specific hours, the ordinance increases transaction costs during restricted periods without affecting daytime availability or altering prices for legal purchases. Effectiveness depends on whether late-night consumption reflects distinct demand patterns (consumers who drink specifically during late hours) versus temporal substitution elasticity (consumers shifting consumption to earlier hours when late-night purchases become unavailable). If late-night demand is price-inelastic but time-elastic, restrictions may generate substantial substitution to pre-restriction hours with minimal reduction in total consumption.

#### D.2.2 Operational Adaptation Mechanisms

Because the ordinance restricts *when* alcohol can be sold with uniform application across affected establishment types, venues face several adaptation strategies that may generate observable effects in revenue and employment data.

##### Non-alcoholic product substitution.

Establishments can remain open during restricted hours selling non-alcoholic products, potentially increasing sales of food, coffee, energy drinks, and snacks to late-night patrons. This non-alcoholic complementarity could affect revenue patterns even if alcohol sales decline, representing operational adaptation within existing venue types. Restaurants and bars may shift emphasis toward food service during restricted hours, while convenience stores may experience increased demand for non-alcoholic beverages and packaged foods from customers who previously combined alcohol purchases with other shopping.

##### Temporal concentration of activity.

Venues may adjust operating hours, either closing during restricted periods to reduce labor costs or shifting peak service hours earlier to capture demand before restrictions take effect. This temporal adaptation could concentrate economic activity into pre-restriction hours, affecting sectoral employment and revenue without necessarily reducing total alcohol consumption if consumers shift drinking to earlier times. Employment effects may manifest through reduced night-shift staffing or altered scheduling patterns rather than aggregate job losses, though such within-establishment adjustments are not directly observable in my aggregate quarterly employment measures.

##### Venue substitution patterns.

The uniform hour restriction across on-premise venues (Sector 18) and off-premise retail (Sectors 14, 16) may generate substitution between venue types. Consumers unable to purchase alcohol at restaurants/bars during late hours may shift to pre-purchasing from supermarkets or convenience stores for home consumption. This substitution would manifest as relative revenue gains in off-premise sectors (14, 16) compared to on-premise venues (18), measurable through the revenue level outcomes in my analysis. However, if total alcohol consumption remains constant through temporal substitution to earlier hours, all alcohol-selling sectors could experience proportional changes in temporal sales patterns without clear cross-sector reallocation.

My analytical framework using *island-wide revenue shares* (Appendix [A.2](https://arxiv.org/html/2510.25782v1#A1.SS2 "A.2 Outcome Variable Construction ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) captures these compositional shifts, isolating venue substitution and sectoral reallocation effects from aggregate island-wide shocks; subsequent intercept-shift and standardization focus identification on dynamics rather than level differences.

#### D.2.3 The Hotel Exemption and Within-Sector Employment Reallocation

The observed pattern—a large employment increase (+67.80 per 1,000, +7.59σ\sigma) alongside negligible revenue effects in Sector 18 (+$0.18M, +0.01σ\sigma)—requires explanation. A key institutional feature of the ordinance provides the mechanism: the hotel guest exemption combined with differential outcome measurement across establishment types.

##### Regulatory heterogeneity and measurement asymmetry.

Article 2.101 of the Public Order Code states: “Hotels regulated by the Puerto Rico Tourism Company retain limited rights to serve registered guests for on-premises consumption during restricted hours” (Municipio Autónomo de San Juan, Legislatura
Municipal, [2023](https://arxiv.org/html/2510.25782v1#bib.bib29)). This exemption creates regulatory heterogeneity within the accommodation and food services sector. Hotel-affiliated bars and restaurants can legally serve alcohol to guests during the restricted hours (1-6 AM weekdays, 2-6 AM weekends), while standalone establishments face a complete prohibition during these windows.

Our outcome definitions capture this regulatory split asymmetrically due to data source characteristics. The *employment* outcome uses NAICS 72 (Accommodation and Food Services), which includes both hotels (NAICS 721: Accommodation) and standalone food establishments (NAICS 722: Food Services and Drinking Places). The *revenue* outcome uses Sector 18 from DDEC retail sales reports, defined as “Restaurants & Drinking Places.” These reports compile sales tax (IVU) data from approximately 45,000 retail establishments across Puerto Rico, classified into 18 retail sectors following NAICS conventions.

Critical measurement assumption: The DDEC retail sales dataset classifies approximately 45,000 businesses into 18 retail sectors, with no accommodation sector among them. I cannot verify from publicly available DDEC documentation whether hotels—as accommodation establishments rather than retail establishments—report food and beverage revenue within this retail sales tax system at all. The DDEC describes the dataset as covering "establecimientos comerciales" (commercial establishments) in "ventas al detal" (retail sales), terminology that suggests hotels may fall outside this classification framework.

##### What we observe and two interpretations.

Hotels increased employment substantially while Sector 18 revenue remained essentially flat. This divergence admits two interpretations depending on the unverifiable measurement structure:

Scenario A: Hotels report F&B revenue under Sector 18. Hotels anticipated increased demand from the exemption and hired additional staff accordingly. The minimal revenue effect (+0.01σ\sigma) suggests the anticipated demand shift did not fully materialize. Possible explanations include standalone venues retaining customers through temporal substitution (shifting service to earlier hours) or the exemption’s practical scope being more limited than anticipated (e.g., few locals purchasing hotel rooms for late-night access, limited tourist demand during restricted hours).

Scenario B: Hotels do not report F&B revenue under Sector 18. Hotels both anticipated and experienced increased demand from the exemption, hiring additional staff and generating additional F&B revenue. I observe the employment effect in NAICS 72 but cannot observe the corresponding revenue effect because hotels report outside the retail sales measurement system captured by Sector 18. This scenario would produce precisely the observed pattern: demand shifts from standalone establishments (captured in both employment and revenue measures) to hotel establishments (captured in employment via NAICS 72 but excluded from Sector 18 revenue).

##### My interpretation: Measurement divergence (Scenario B).

I interpret the employment-revenue divergence under Scenario B for three empirical reasons:

1. 1.

   Magnitude and persistence: The employment effect appears immediately in 2023 Q4 (+68.21 per 1,000) and remains stable through 2025 Q1 (+67.72 per 1,000 average for fully exposed quarters; Table [7](https://arxiv.org/html/2510.25782v1#S5.T7 "Table 7 ‣ Partial-exposure robustness. ‣ 5.4.2 Treatment Effects and Stability ‣ 5.4 Results: Separate vs Common-Weights (Average) Estimator ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). Under Scenario A (demand failed to materialize), I would expect either employment adjustment downward in later quarters as hotels correct their hiring decisions, or compensating revenue declines in standalone venues if demand did shift but hotels report within Sector 18. Neither pattern appears in the data. The stability suggests a structural shift in sectoral composition rather than a transient misalignment between expectations and outcomes.
2. 2.

   Pre-treatment correlation break: Table [2](https://arxiv.org/html/2510.25782v1#S5.T2 "Table 2 ‣ Cross-outcome error correlation. ‣ 5.3 Diagnostics: Assessing Shared Structure ‣ 5 Empirical Application: Effect of San Juan’s Public Order Code ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") shows that Sector 18 revenue and accommodation/food employment exhibited the strongest correlation (0.93) among all outcome pairs during the pre-treatment period. Both measures respond to common demand shocks (tourism flows, events, aggregate spending) when all establishments operate under identical regulations. The post-treatment divergence represents a policy-induced break in this previously strong relationship. Under Scenario B, the exemption creates differential regulatory treatment that separates hotel and standalone establishment trajectories while measurement conventions prevent observing hotel F&B revenue shifts directly, producing exactly this correlation break. Under Scenario A, the strong pre-treatment correlation should persist if both hotel and standalone revenue remain captured in Sector 18, yet we observe divergence.
3. 3.

   Parsimonious institutional alignment: The hotel exemption creates a clear regulatory advantage that should generate precisely the observed measurement divergence under Scenario B. Consumers seeking late-night alcohol service shift from standalone bars (now prohibited) to hotel-affiliated establishments (exempt for registered guests). This could include both tourists already staying in hotels and local residents who obtain rooms specifically to access late-night service. Hotels increase staffing for late-night food and beverage operations to capture this shifted demand. From an aggregate employment perspective using Department of Labor data (which classifies establishments by their primary NAICS code), this registers as an increase in NAICS 72 employment. Meanwhile, hotel F&B revenue does not appear in Sector 18 because hotels report sales tax revenue under their primary establishment classification (accommodation) rather than as restaurant revenue, consistent with the absence of an accommodation sector in the DDEC retail sales reporting system.

This interpretation—the hotel exemption mechanism combined with recognition of measurement asymmetries inherent in using different data sources for employment (Department of Labor, NAICS-based) and revenue (DDEC retail sales, establishment-type-based)—provides the most complete explanation for the full pattern of results: large employment increases, minimal standalone restaurant revenue effects, strong pre-treatment correlation that breaks post-treatment, and temporal persistence across all post-treatment quarters.

##### Alternative mechanisms and limitations.

Two alternative mechanisms could contribute under either scenario:

Formalization of employment: The ordinance’s enforcement provisions ($5,000 fine, escalating penalties for repeat violations) may have incentivized businesses to formalize previously informal employment relationships, increasing measured employment without corresponding revenue changes. However, this mechanism would not explain why the employment increase concentrates in NAICS 72 or why the effect magnitude is so large relative to other outcomes.

Temporal concentration with service quality maintenance: Establishments may hire additional staff to serve compressed demand in fewer hours. However, this mechanism predicts employment increases accompanied by higher revenue per hour (demand concentration), not the near-zero revenue effects observed (+0.01σ\sigma).

##### Data constraints and interpretation.

I acknowledge a fundamental limitation that affects interpretation of the central finding: I cannot definitively verify how hotels report disaggregated food and beverage revenue within the IVU sales tax system. As of the date of this study, no publicly available DDEC source specifies establishment-level attribution rules when businesses operate multiple revenue streams under a single tax identifier. The 18-sector classification framework published by DDEC focuses on retail establishments, and hotels’ primary classification as accommodation providers (NAICS 721) suggests their F&B operations may not appear in Sector 18 (Restaurants & Drinking Places, NAICS 722), but this remains an assumption based on standard NAICS conventions and the terminology used in DDEC documentation rather than confirmed DDEC practice.

Despite this limitation, the hotel exemption mechanism under Scenario B (measurement divergence) provides the most parsimonious explanation for the observed pattern. The exemption creates a regulatory advantage that should produce exactly this divergence; the strong pre-treatment correlation (0.93) breaks post-treatment precisely when the differential treatment begins; and the effect persists across all post-treatment quarters rather than showing the volatility or correction expected under alternative interpretations. The measurement gap—observable employment changes (NAICS 72) without corresponding observable revenue changes (Sector 18)—is itself evidence consistent with the hotel exemption mechanism operating through differential measurement coverage.

#### D.2.4 Crime Prevention: Theoretical Foundations and Evidence

Theoretical foundations for reducing crime through environmental controls on alcohol availability are well-established. The premise is that alcohol consumption increases probability of violent behavior, public disorder, and risky decision-making through both pharmacological effects (impaired judgment, increased aggression) and situational factors (late-night crowding, reduced guardianship), such that reducing late-night availability should decrease incidents during restricted hours (Cook and Moore, [2002](https://arxiv.org/html/2510.25782v1#bib.bib15)).

Systematic reviews provide mixed evidence on the effectiveness of trading-hour restrictions. Research finds that extending late-night trading hours increases alcohol-related harms (Hahn et al., [2010](https://arxiv.org/html/2510.25782v1#bib.bib25)), providing indirect support for the hypothesis that restricting hours should reduce harm through the reverse mechanism. However, evidence specifically for trading-hour restrictions shows good support for harm reduction though with mixed effects across settings and implementation contexts (Eassey et al., [2024](https://arxiv.org/html/2510.25782v1#bib.bib18)). Multicomponent interventions combining hour restrictions with other measures (enhanced enforcement, responsible beverage service training, environmental design changes) show the strongest and most consistent results for reducing assaults (Eassey et al., [2024](https://arxiv.org/html/2510.25782v1#bib.bib18)), suggesting that hour restrictions alone may be insufficient without complementary interventions.

The link between availability restrictions and harm is not deterministic and may be attenuated by several factors. A Swedish study of extended off-premise retail hours found that while alcohol sales increased significantly following liberalization, there was no corresponding increase in adverse health or crime outcomes (Avdic and von Hinke, [2021](https://arxiv.org/html/2510.25782v1#bib.bib10)), illustrating that availability changes may be offset by behavioral adaptation (consumers adjusting drinking location or timing), enforcement practices (police reallocation or changed arrest policies), or contextual factors (alternative availability through informal channels). These mixed findings underscore that availability restrictions operate through multiple channels and that effectiveness depends critically on local context, enforcement capacity, and the broader regulatory environment.

The San Juan ordinance represents a specific configuration—late-night hours only, broad coverage across both on- and off-premise venues, limited exemptions for hotels—whose effects may differ from other contexts studied in the international literature. My empirical strategy examines both late-night public disorder (incidents occurring during restricted hours) and all-hours violent crime to distinguish between temporal displacement effects and genuine harm reduction.

#### D.2.5 Tourism and Regional Economic Structure

Concerns about economic harm from alcohol restrictions frequently emphasize potential tourism impacts, particularly relevant given San Juan’s role as Puerto Rico’s primary tourist destination and economic hub. However, evidence challenges claims that availability restrictions necessarily harm tourism demand or hospitality sector performance.

A time-series analysis in Western Australia found no evidence that area-wide alcohol restrictions negatively affected tourism, with restricted regions experiencing growth patterns significantly correlated with unrestricted control regions (Symons et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib35)). This suggests that concerns about tourism harm may be overstated, particularly when restrictions apply uniformly within a destination (avoiding competitive disadvantage) and target late-night hours that may not constitute primary draw for most tourist segments. Visitors seeking cultural attractions, beaches, dining, and daytime activities may be minimally affected by late-night alcohol restrictions, while the late-night party segment represents a smaller share of total tourism demand.

San Juan’s role as Puerto Rico’s tourism gateway creates systematic differences from potential control municipalities that complicate causal inference. The city functions as the island’s economic and administrative capital, attracting substantial out-of-municipality demand through both tourism and commuting. On the visitor side, recent tourism market updates document demand concentrated in and around the Metro (San Juan) area, with outsized lodging activity and event-driven surges (Discover Puerto Rico, [2025](https://arxiv.org/html/2510.25782v1#bib.bib16)). On the commuter side, transportation planning documents describe the San Juan region as the island’s major commuter hub and primary employment center, concentrating a large share of population and jobs and generating substantial inter-municipal inflows (Gobierno de Puerto Rico, Departamento de Transportación y Obras
Públicas, [2023](https://arxiv.org/html/2510.25782v1#bib.bib23)).

This regional hub status exacerbates what Lee et al. ([2025](https://arxiv.org/html/2510.25782v1#bib.bib28)) term the “scale sub-problem” of the Modifiable Areal Unit Problem (MAUP): many urban indicators scale nonlinearly with population, so resident population may not accurately proxy market size, and simple per-capita normalization can mislead when comparing jurisdictions with different catchment areas. Consistent with the urban scaling literature, multiple economic indicators exhibit systematic sub- or super-linear scaling with population, undermining the linearity implicit in per-capita normalization (Ribeiro and Netto, [2024](https://arxiv.org/html/2510.25782v1#bib.bib32); Shuai et al., [2024](https://arxiv.org/html/2510.25782v1#bib.bib33); Xu et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib37)). In a regional hub like San Juan, per-capita revenue measures embed catchment effects (tourism inflows, commuter spending) absent in smaller municipalities, inflating levels and potentially distorting trends relative to demographically similar but non-hub comparators.

My multi-stage donor screening (Appendix [A.3](https://arxiv.org/html/2510.25782v1#A1.SS3 "A.3 Six-Stage Donor Pool Screening ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) addresses MAUP concerns by selecting municipalities with similar demographic and economic structure, while my outcome measurement strategy (Appendix [A.2](https://arxiv.org/html/2510.25782v1#A1.SS2 "A.2 Outcome Variable Construction ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")) uses *island-wide revenue shares (Option A)* for economic outcomes. Shares normalize by the island total within each sector-quarter, mitigating catchment-size inflation in hubs like San Juan and reducing spurious cross-sectional scale effects. The intercept-shifted estimation approach (see Section [3.3](https://arxiv.org/html/2510.25782v1#S3.SS3 "3.3 Implementation Conventions and Design Choices ‣ 3 Multi-Outcome Synthetic Control: Implementation ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan") in the main text) demeans each series by its pre-treatment mean and then standardizes by the treated unit’s pre-treatment standard deviation, preserving temporal dynamics while providing a common scale for multi-outcome weighting.

#### D.2.6 Measurement Strategy and Scale Considerations

Urban scaling research documents that many economic indicators covary nonlinearly with population size—often super-linearly due to agglomeration and network effects—so per-capita indicators, which implicitly assume linear scaling, can bias comparisons across municipalities with heterogeneous catchment areas (Ribeiro and Netto, [2024](https://arxiv.org/html/2510.25782v1#bib.bib32); Shuai et al., [2024](https://arxiv.org/html/2510.25782v1#bib.bib33); Xu et al., [2025](https://arxiv.org/html/2510.25782v1#bib.bib37); Alves et al., [2015](https://arxiv.org/html/2510.25782v1#bib.bib7)).

For revenue, I use *island-wide shares* rather than raw levels or per-capita rates. Shares provide a scale-free, common-denominator metric that (i) normalizes by the sector’s island-wide total each quarter, dampening hub-driven catchment effects; (ii) places municipalities on a bounded [0,1][0,1] support that is numerically well-behaved; and (iii) directly measures changes in a municipality’s competitive position within Puerto Rico’s sectoral economy. Because shares can still co-move with island-wide shocks, I subsequently apply an intercept shift (demeaning by pre-treatment means) and standardize by San Juan’s pre-treatment standard deviation before estimation, which focuses identification on pre-/post-dynamics rather than cross-sectional levels.

For crime and employment, I use conventional per-capita rates (per 1,000 residents) with a fixed 2023 ACS baseline population (Appendix [A.2.2](https://arxiv.org/html/2510.25782v1#A1.SS2.SSS2 "A.2.2 Employment & Crime: Per-Capita Rates ‣ A.2 Outcome Variable Construction ‣ Appendix A Data Construction & Donor Pool Screening ‣ Short-Run Multi-Outcome Effects of Nightlife Regulation in San Juan")). These outcomes are jurisdiction-based (incidents occur where they are recorded; establishments are located where employment is reported) and are standardly interpreted on a per-resident basis. Fixing denominators avoids endogenous population changes during the study window and maintains comparability across municipalities and over time.

This mixed framework—*shares for revenue* and *per-capita for crime/employment*—balances theoretical scale considerations with outcome-specific policy relevance and supports coherent, common-weight MOSC estimation after intercept-shift and standardization.

### D.3 Scope and Limitations

The analysis focuses on short-run effects through 2025 Q1, capturing immediate operational adjustments and behavioral responses during the first six post-treatment quarters. Longer-run equilibrium effects may differ as businesses and consumers fully adapt to the new regulatory environment, establishments adjust their business models, and market structure potentially changes through entry or exit. The employment dimension emphasizes aggregate per-capita employment for assessing short-run structural effects, though longer-term assessment would benefit from more granular occupational and wage analysis to examine job quality and distributional dynamics (Kronenberg and Fuchs, [2022](https://arxiv.org/html/2510.25782v1#bib.bib27)).

Data limitations constrain my ability to observe within-establishment adjustments (shift scheduling, product mix changes, hour adjustments), enforcement patterns (inspection frequency, fine collection, permit revocations), or compliance heterogeneity across establishment types and neighborhoods. The analysis assumes uniform compliance and enforcement, though actual implementation may vary. These micro-level mechanisms remain important directions for future research as administrative enforcement data become available and longer time series permit analysis of dynamic adjustment and potential equilibrium effects.

## References

* (1)
* Abadie (2020)

  Abadie, Alberto, “Statistical Nonsignificance in Empirical Economics,”
  American Economic Review: Insights, June 2020, 2 (2), 193–208.
* Abadie (2021)

    , “Using Synthetic Controls: Feasibility, Data Requirements,
  and Methodological Aspects,” Journal of Economic Literature, June
  2021, 59 (2), 391–425.
* Abadie et al. (2010)

    , Alexis Diamond, and Jens Hainmueller, “Synthetic Control
  Methods for Comparative Case Studies: Estimating the Effect of California’s
  Tobacco Control Program,” Journal of the American Statistical
  Association, June 2010, 105 (490), 493–505.
* Abadie et al. (2015)

    ,   , and   , “Comparative Politics and the
  Synthetic Control Method,” American Journal of Political Science,
  April 2015, 59 (2), 495–510.
* Abadie and Zhao (2025)

     and Jinglong Zhao, “Synthetic Controls for Experimental
  Design,” arXiv, April 2025.
* Alves et al. (2015)

  Alves, Luiz G. A., Renio S. Mendes, Ervin K. Lenzi, and Haroldo V.
  Ribeiro, “Scale-Adjusted Metrics for Predicting the Evolution of Urban
  Indicators and Quantifying the Performance of Cities,” PLOS ONE,
  September 2015, 10 (9), 1–27.
  Asociación de Empresarios Calle Loíza, Inc., et al. v.
  Municipality of San Juan
* Asociación de Empresarios Calle Loíza,
  Inc., et al. v. Municipality of San Juan (2023)

  Asociación de Empresarios Calle Loíza, Inc., et al. v.
  Municipality of San Juan, Complaint, Civ. No. 23-1541 (D.P.R. October 27,
  2023) October 2023.
  Asociación de Empresarios Calle Loíza, Inc., et al. v.
  Municipality of San Juan
* Asociación de Empresarios Calle Loíza,
  Inc., et al. v. Municipality of San
  Juan (2024)

  Asociación de Empresarios Calle Loíza, Inc., et al. v.
  Municipality of San Juan, Opinion and Order, Civ. No. 23-1541 (D.P.R. July
  30, 2024) July 2024.
  Judge Silvia L. Carreño-Coll (SCC).
* Avdic and von Hinke (2021)

  Avdic, Daniel and Stephanie von Hinke, “Extending Alcohol Retailers’
  Opening Hours: Evidence from Sweden,” Discussion Paper 2021-03, Monash
  University, Centre for Health Economics, Clayton, Victoria June 2021.
* Brodeur et al. (2020)

  Brodeur, Abel, Nikolai Cook, and Anthony Heyes, “Methods Matter:
  p-Hacking and Publication Bias in Causal Analysis in Economics,” American Economic Review, November 2020, 110 (11), 3634–3660.
* Caetano et al. (2016)

  Caetano, Raul, Patrice A. C. Vaeth, Britain Mills, and Glorisa Canino,
  “Employment Status, Depression, Drinking, and Alcohol Use Disorder in Puerto
  Rico,” Alcoholism: Clinical and Experimental Research, April 2016,
  40 (4), 806–815.
* Chernozhukov et al. (2021)

  Chernozhukov, Victor, Kaspar Wüthrich, and Yinchu Zhu, “An Exact and
  Robust Conformal Inference Method for Counterfactual and Synthetic
  Controls,” Journal of the American Statistical Association, October
  2021, 116 (536), 1849–1864.
* Chopra et al. (2022)

  Chopra, Felix, Ingar Haaland, Christopher Roth, and Andreas Stegmann,
  “The Null Result Penalty,” ECONtribute Discussion Paper 169, University of
  Bonn and University of Cologne, Reinhard Selten Institute (RSI), Bonn and
  Cologne, Germany May 2022.
  May 27, 2022.
* Cook and Moore (2002)

  Cook, Philip J. and Michael J. Moore, “The Economics of Alcohol Abuse
  and Alcohol-Control Policies,” Health Affairs, March–April 2002, 21 (2), 120–133.
* Discover Puerto Rico (2025)

  Discover Puerto Rico, “Research Update: Tourism Revenue on the Rise:
  Lodging Industry Sees Strong Growth,” Discover Puerto Rico Industry Research
  June 2025.
  Estimates of room tax collections, hotel vs. rental contributions,
  and lodging trends in Puerto Rico.
* Duchi et al. (2008)

  Duchi, John, Shai Shalev-Shwartz, Yoram Singer, and Tushar Chandra,
  “Efficient Projections onto the ℓ1\ell\_{1}-Ball for Learning in High
  Dimensions,” in “Proceedings of the 25th International Conference on
  Machine Learning” ICML ’08 Association for Computing Machinery Helsinki,
  Finland 2008, pp. 272–279.
* Eassey et al. (2024)

  Eassey, Christopher, Caitlin E. Hughes, Phillip Wadds, Dominique de
  Andrade, and Monica J. Barratt, “A Systematic Review of Interventions that
  Impact Alcohol and Other Drug-Related Harms in Licensed Entertainment
  Settings and Outdoor Music Festivals,” Harm Reduction Journal,
  February 2024, 21, 47.
* Federal Bureau of Investigation (2025)

  Federal Bureau of Investigation, “National Incident-Based Reporting
  System (NIBRS) User Manual,” Technical and Reporting Guidance 2025.
  Version 2025.0, June 26, 2025.
* Frankel and Kasy (2022)

  Frankel, Alexander and Maximilian Kasy, “Which Findings Should Be
  Published?,” American Economic Journal: Microeconomics, February 2022,
  14 (1), 1–38.
* Gobierno de Puerto Rico, Departamento de Desarrollo Económico y
  Comercio, Secretaría Auxiliar de Sectores Estratégicos, Oficina de
  Estrategia e Inteligencia de Negocios (2025)

  Gobierno de Puerto Rico, Departamento de Desarrollo Económico y
  Comercio, Secretaría Auxiliar de Sectores Estratégicos, Oficina de
  Estrategia e Inteligencia de Negocios, “Informes Municipales de Ventas al
  Detal,” Portal de publicaciones: Informes e Indicadores 2025.
  Serie mensual con ventas por municipio y 18 sectores NAICS; fuente:
  IVU (Depto. de Hacienda) con ~45,000 negocios. Sección:
  “Informes Municipales de Ventas al Detal”.
* Gobierno de Puerto Rico, Departamento de Seguridad Pública,
  Negociado de la Policía de Puerto Rico (2020)

  Gobierno de Puerto Rico, Departamento de Seguridad Pública, Negociado
  de la Policía de Puerto Rico, “600–621: Manejo de los Informes de
  Incidentes o Servicios Policiacos,” Procedimiento Administrativo Interno
  2020.
  Versión oficial revisada del manual de procedimientos para la
  recopilación de datos NIBRS y UCR.
* Gobierno de Puerto Rico, Departamento de Transportación y Obras
  Públicas (2023)

  Gobierno de Puerto Rico, Departamento de Transportación y Obras
  Públicas, “Appendix: Chapter 6 - Transportation Demand Management,”
  Technical Report, Departamento de Transportación y Obras Públicas, Puerto
  Rico 2023.
  Estrategias, objetivos y medidas de manejo de demanda de transporte
  (TDM) para Puerto Rico; parte del plan de largo plazo.
* Gobierno de Puerto Rico, Departamento del Trabajo y Recursos
  Humanos (2023)

  Gobierno de Puerto Rico, Departamento del Trabajo y Recursos Humanos,
  “Composición Industrial por Municipio – 3er Trimestre 2023,” Informe
  estadístico 2023.
  Publicación trimestral de empleo y número de establecimientos por
  municipio y sector industrial (NAICS).
* Hahn et al. (2010)

  Hahn, Robert A., Jennifer L. Kuzara, Randy Elder, Robert Brewer, Sajal
  Chattopadhyay, Jonathan Fielding, Timothy S. Naimi, Traci Toomey,
  Jennifer Cook Middleton, and Briana Lawrence, “Effectiveness of Policies
  Restricting Hours of Alcohol Sales in Preventing Excessive Alcohol
  Consumption and Related Harms,” American Journal of Preventive
  Medicine, December 2010, 39 (6), 590–604.
* Harwood et al. (2004)

  Harwood, Eileen M., Debra H. Bernat, Kathleen M. Lenk, Mary Jo Vázquez,
  and Alexander C. Wagenaar, “Public Opinion in Puerto Rico on Alcohol
  Control Policies,” Hispanic Journal of Behavioral Sciences, November
  2004, 26 (4), 426–445.
* Kronenberg and Fuchs (2022)

  Kronenberg, Kai and Matthias Fuchs, “The Socio-Economic Impact of
  Regional Tourism: An Occupation-Based Modelling Perspective from Sweden,”
  Journal of Sustainable Tourism, December 2022, 30 (12),
  2785–2805.
* Lee et al. (2025)

  Lee, Dong Wook, Melissa Rogers, and Hillel David Soifer, “The Modifiable
  Areal Unit Problem in Political Science,” Political Analysis, October
  2025, 33 (4), 412–424.
* Municipio Autónomo de San Juan, Legislatura
  Municipal (2023)

  Municipio Autónomo de San Juan, Legislatura Municipal, “Ordenanza
  Núm. 3, Serie 2023–2024: Código de Orden Público del Municipio de San
  Juan (sustituyendo al P. de O. Núm. 53, Serie 2022–2023),” Ordenanza
  municipal August 2023.
  Aprobada el 8 de agosto de 2023.
* O’Neill et al. (2020)

  O’Neill, Stephen, Noemi Kreif, Matt Sutton, and Richard Grieve, “A
  Comparison of Methods for Health Policy Evaluation with Controlled Pre-Post
  Designs,” Health Services Research, April 2020, 55 (2),
  328–338.
* Pouliot and Xie (2022)

  Pouliot, Guillaume Allaire and Zhen Xie, “Degrees of Freedom and
  Information Criteria for the Synthetic Control Method,” arXiv
  e-prints, July 2022.
* Ribeiro and Netto (2024)

  Ribeiro, Fabiano L. and Vinicius M. Netto, “Urban Scaling Laws,” arXiv, April 2024.
  Compendium of Urban Complexity chapter.
* Shuai et al. (2024)

  Shuai, Chenyang, Chuan Liao, Shen Qu, Xi Chen, Bu Zhao, Jian-Ping Zou, and
  Ming Xu, “Scaling of Development Indicators in Countries and Its Origin,”
  iScience, August 2024, 27 (8), 110497.
* Sun et al. (2025)

  Sun, Liyang, Eli Ben-Michael, and Avi Feller, “Using Multiple Outcomes
  to Improve the Synthetic Control Method,” Review of Economics and
  Statistics, 2025.
  Advance online publication.
* Symons et al. (2025)

  Symons, Martyn, William Gilmore, Naomi Henrickson, and Tanya Chikritzhs,
  “Are Alcohol Restrictions Bad for Tourism? An Exploratory Study of Tourism
  Trends in Western Australia,” Australian and New Zealand Journal of
  Public Health, August 2025, p. 100256.
  Early online.
* U.S. Census Bureau (2023)

  U.S. Census Bureau, “American Community Survey 5-Year Estimates,
  2019–2023,” Data Tables 2023.
  Table DP05 (Demographic and Housing Estimates), S1701 (Poverty
  Status), S2503 (Financial Characteristics), for Puerto Rico municipalities.
* Xu et al. (2025)

  Xu, Zhibang, Gang Xu, Ting Lan, Xi Li, Zuoqi Chen, Hao Cui, Zhengzi Zhou,
  Haowei Wang, Limin Jiao, and Christopher Small, “Global Consistency of
  Urban Scaling Evidenced by Remote Sensing,” PNAS Nexus, February 2025,
  4 (2), pgaf037.