---
authors:
- Keywan Christian Rasekhschaffe
doc_id: arxiv:2602.00196v1
family_id: arxiv:2602.00196
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Generative AI for Stock Selection
url_abs: http://arxiv.org/abs/2602.00196v1
url_html: https://arxiv.org/html/2602.00196v1
venue: arXiv q-fin
version: 1
year: 2026
---


result = data.groupby('date')['analyst\_sal\_interaction\_rolling'].rank(pct=True)

return result

The highest IC (0.0089) of all showcased features. When many analysts
follow a stock showing strong sales, that information spreads
efficiently and gets priced. The 30-day smoothing prevents single-day
spikes from dominating.

### Statistical Summary of 225 Top Features

Sample Coverage: - 225 features analyzed (top 75 per dataset by
absolute IC) - Three datasets: Price Universe (2015-2024), TrueBeats
(2015-2023), SpiderRock (2019-2024) - Mean |IC| =
0.00343 (median: 0.00295) - Mean |Sharpe| = 0.559
(median: 0.492)

Pattern Prevalence: - 100% Cross-sectional ranking (universal)
- 93% Regime-aware normalization - 80% Variable interactions - 67%
Momentum with adjustments - 45% Statistical outlier detection - 27%
Multi-timeframe patterns

Complexity Metrics: - Mean operations: 14.2 (median: 13) -
Range: 8-22 operations per feature - Comparison: 2-4 operations typical
in academic factors

Window Convergence: - 5 days: 32% of all window specifications
- 10 days: 18% of all window specifications - 20-21 days: 38% of all
window specifications - 60 days: 12% of all window specifications -
Search space available: 1-252 days

Performance Distribution: - 78% achieve |IC|
> 0.002 (meaningful predictive power) - 80% achieve
|Sharpe| > 0.2 (acceptable risk-adjusted
returns) - 46% achieve |IC| > 0.003
(strong signals) - 44% achieve |Sharpe| >
0.5 (strong risk-adjusted performance)