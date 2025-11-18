---
authors:
- Harrison Katz
doc_id: arxiv:2511.12763v1
family_id: arxiv:2511.12763
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Impact by design: translating Lead times in flux into an R handbook with code'
url_abs: http://arxiv.org/abs/2511.12763v1
url_html: https://arxiv.org/html/2511.12763v1
venue: arXiv q-fin
version: 1
year: 2025
---


pid <- dplyr::first(Lk\_pickup$property\_id)

latest <- max(Lk\_pickup$month)

cohort <- subset(Lk\_pickup, property\_id == pid & month == latest)

Chist\_14 <- cohort$Chist[cohort$k == 14][1]

bound <- relative\_error\_bound(D = D\_est, delta = 14, delta\_max = 60, Chist\_delta = Chist\_14)

actions <- recommend\_actions(bound)

print(list(latest\_month = latest, D\_est = round(D\_est, 3),

Chist\_14 = round(Chist\_14, 3), bound = round(bound, 3), actions = actions))

## 5 Results on synthetic data

All artifacts are produced by the script scripts/make\_paper\_artifacts.R and saved under paper\_artifacts/.

### 5.1 Adjacent month divergence

Figure [1](https://arxiv.org/html/2511.12763v1#S5.F1 "Figure 1 ‣ 5.1 Adjacent month divergence ‣ 5 Results on synthetic data ‣ Impact by design: translating Lead times in flux into an R handbook with code") shows the adjacent month normalized L1 divergence D​(Lt,Lt−1)D(L\_{t},L\_{t-1}) by property over 2021 to 2022 with quarterly x axis ticks for readability.

![Refer to caption](fig1_divergence_adjacent.png)


Figure 1: Adjacent month divergence D​(Lt,Lt−1)D(L\_{t},L\_{t-1}) by property. A value of 0.20 indicates that 20% of the mass in the lead time distribution moved relative to the prior month. Properties differ in both amplitude and pattern, which is expected under heterogeneous demand and policy environments.

The series stay in a narrow band between roughly 0.12 and 0.20. Property P001 exhibits a late year rise, property P002 shows a dip followed by recovery, and property P003 trends downward into late 2022. These patterns are the distributional changes that a mean or a single percentile can fail to register. The 90th percentile and related summary statistics are reported in Table [1](https://arxiv.org/html/2511.12763v1#S5.T1 "Table 1 ‣ 5.1 Adjacent month divergence ‣ 5 Results on synthetic data ‣ Impact by design: translating Lead times in flux into an R handbook with code"), pulled directly from the generated CSV.

Table 1: Divergence summary by property (adjacent month). Values read from paper\_artifacts/tables/tbl3\_divergence\_summary.csv.

| Property | Months | Mean D | Median D | P90 D |
| --- | --- | --- | --- | --- |
| P001 | 23 | 0.157 | 0.155 | 0.179 |
| P002 | 23 | 0.162 | 0.160 | 0.185 |
| P003 | 23 | 0.161 | 0.161 | 0.175 |

### 5.2 Pickup and the risk bound

Figure [2](https://arxiv.org/html/2511.12763v1#S5.F2 "Figure 2 ‣ 5.2 Pickup and the risk bound ‣ 5 Results on synthetic data ‣ Impact by design: translating Lead times in flux into an R handbook with code") shows Chist​(Δ)C\_{\text{hist}}(\Delta) for the latest cohort of property P001. About half of total pickup occurs by two weeks before arrival, which is consistent with the heavy short horizon mass in the corresponding histogram in Figure [3](https://arxiv.org/html/2511.12763v1#S5.F3 "Figure 3 ‣ 5.2 Pickup and the risk bound ‣ 5 Results on synthetic data ‣ Impact by design: translating Lead times in flux into an R handbook with code"). Combining a typical divergence in the upper teens with a 14 day horizon and Chist​(14)C\_{\text{hist}}(14) near one half yields a risk bound near one half by Equation ([2](https://arxiv.org/html/2511.12763v1#S1.E2 "In 1 What the original article established ‣ Impact by design: translating Lead times in flux into an R handbook with code")). The exact values used in the manuscript are read from the CSV in Table [2](https://arxiv.org/html/2511.12763v1#S5.T2 "Table 2 ‣ 5.2 Pickup and the risk bound ‣ 5 Results on synthetic data ‣ Impact by design: translating Lead times in flux into an R handbook with code").

![Refer to caption](fig2_pickup_curves_latest.png)


Figure 2: Cumulative pickup Chist​(Δ)C\_{\text{hist}}(\Delta) for property P001, latest month.

![Refer to caption](fig3_leadtime_histograms_latest.png)


Figure 3: Lead time histogram Lt​(k)L\_{t}(k) for property P001, latest month. The tall bar at k=60k=60 is a truncation artifact from capping Δmax\Delta\_{\max} at 60 in the simulation. In practice either increase Δmax\Delta\_{\max} or treat a right censored bin 60+60+ separately.




Table 2: Risk index and mapped actions at standard horizons for the latest month of each property. Values read from paper\_artifacts/tables/tbl2\_risk\_latest\_month.csv.

| Property | Month | Delta (days) | C\_hist | Bound | Price cadence | AP buffer (days) | Staffing buffer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P001 | 2022-12 | 7 | 0.289 | 1.086 | intraday | 0 | 15% |
| P001 | 2022-12 | 14 | 0.478 | 0.570 | intraday | 0 | 15% |
| P001 | 2022-12 | 21 | 0.625 | 0.369 | intraday | 0 | 15% |
| P002 | 2022-12 | 7 | 0.276 | 1.138 | intraday | 0 | 15% |
| P002 | 2022-12 | 14 | 0.521 | 0.522 | intraday | 0 | 15% |
| P002 | 2022-12 | 21 | 0.634 | 0.364 | intraday | 0 | 15% |
| P003 | 2022-12 | 7 | 0.260 | 1.208 | intraday | 0 | 15% |
| P003 | 2022-12 | 14 | 0.479 | 0.568 | intraday | 0 | 15% |
| P003 | 2022-12 | 21 | 0.611 | 0.377 | intraday | 0 | 15% |

The table reports the bound at 7, 14, and 21 days together with a simple, auditable mapping to operations. Months and properties with larger divergence and smaller Chist​(Δ)C\_{\text{hist}}(\Delta) at the chosen horizon produce higher risk values and stricter actions. As the service date approaches the (1−Δ/Δmax)(1-\Delta/\Delta\_{\max}) term contracts the bound monotonically.

## 6 Synthetic case studies

To keep everything reproducible, we include calibrated simulations that mimic the empirical patterns reported in the article. A compression parameter c∈[0,1]c\in[0,1] moves probability mass toward short horizons, which raises the divergence series and the pickup risk index in predictable ways. The R scripts generate arrivals across multiple properties and segments, compute DtD\_{t} and Chist​(Δ)C\_{\text{hist}}(\Delta), and apply the decision templates.

### 6.1 Data generating process

Lead times are drawn from a two component lognormal mixture. The compression parameter cc shifts weight toward the short horizon component and therefore increases mass inside the last two weeks. Seasonality and event weeks can be introduced as multiplicative factors so that the divergence series reflects both steady changes and occasional spikes. Segment heterogeneity is introduced as random effects. All generators accept seeds so that figures are exactly reproducible.

### 6.2 Illustrative results

As compression rises, the divergence series increases and change points appear earlier in the period. The pickup risk index is largest when divergence is high and the historical pickup fraction is low at the chosen horizon. The templates therefore suggest a higher pricing cadence and looser advance purchase buffers in those months. As the service date approaches the bound contracts by construction and the recommended actions revert to a less intensive cadence.

## 7 Evaluation plan for operational settings

Effects can be estimated with standard designs that are robust to nonstationarity.

* •

  Difference in differences. Compare units that adopt the monitoring and decision templates against matched units on a rolling basis, using horizon specific forecast metrics as outcomes (Callaway and Sant’Anna, [2021](https://arxiv.org/html/2511.12763v1#bib.bib8)).
* •

  Interrupted time series with synthetic control. When the number of units is small, construct a counterfactual series for a treated unit and evaluate level and variance changes after the intervention (Abadie et al., [2010](https://arxiv.org/html/2511.12763v1#bib.bib9)).
* •

  Experimentation when feasible. For pricing cadence or advance purchase rules, randomize policies at the unit level and analyze horizon specific metrics.

Primary forecast outcomes are MASE and sMAPE at 0 to 7, 8 to 14, and 15 to 21 days. Operational outcomes include spoilage, denied service, and the variance of ADR or RevPAR.

## 8 Governance and reproducibility

All analysis runs locally on booking event data. No external connections are required. The package ships with a synthetic dataset and scripts that regenerate all figures. A brief executive summary reports the divergence series, the pickup risk index at standard horizons, and any actions taken. Versioned code and seeds allow third parties to reproduce results and extend simulations.

## 9 Limits

The divergence metric captures global shifts in the distribution shape. It does not attribute causes and it does not replace demand models. The pickup bound is conservative, especially when divergence is large and historical pickup is small at the chosen horizon. Users who require parametric forecasts of the full lead time vector can adopt B–DARMA or related compositional time series models while still benefiting from divergence monitoring and the risk index (Katz et al., [2024](https://arxiv.org/html/2511.12763v1#bib.bib2)). The decision templates are intentionally simple and are intended as safe defaults that can be tuned over time.

## 10 Conclusion

By turning two ideas from the article into a minimal R artifact that analysts can run on their own files, it becomes easier to detect distributional change, to translate that change into a clear risk index, and to connect the index to concrete actions. The same artifact defines how to measure effects in operational settings. This closes the loop between research and decision and sets the stage for comparative evaluation across markets and segments.

## Declarations

Funding None declared.

Competing interests The authors declare no conflicts of interest and that all work and opinions are their own and that the work is not sponsored or endorsed by Airbnb.

Data availability All results are generated from simulations. A synthetic dataset and an R package archive are provided as supplementary material.

Code availability The R package leadtimefluxR and example scripts are provided as supplementary files and are available at <https://github.com/harrisonekatz/leadtimefluxR>.

Ethics approval, consent, and permissions Not applicable.

## References

* Katz et al. (2025)

  Katz, H., Savage, E., Coles, P. (2025).
  Lead times in flux: Analyzing Airbnb booking dynamics during global upheavals (2018–2022).
  Annals of Tourism Research Empirical Insights, 6(2), 100185.
* Katz et al. (2024)

  Katz, H., Brusch, K. T., Weiss, R. E. (2024).
  A Bayesian Dirichlet auto regressive moving average model for forecasting lead times.
  International Journal of Forecasting, 40(4), 1556–1567.
  <https://doi.org/10.1016/j.ijforecast.2024.01.004>
* Cleveland et al. (1990)

  Cleveland, R. B., Cleveland, W. S., McRae, J. E., Terpenning, I. (1990).
  STL: A seasonal trend decomposition procedure based on loess.
  Journal of Official Statistics, 6(1), 3–73.
* Hyndman and Koehler (2006)

  Hyndman, R. J., Koehler, A. B. (2006).
  Another look at measures of forecast accuracy.
  International Journal of Forecasting, 22(4), 679–688.
* Gibbs and Su (2002)

  Gibbs, A. L., Su, F. E. (2002).
  On choosing and bounding probability metrics.
  International Statistical Review, 70(3), 419–435.
* Weatherford and Kimes (2003)

  Weatherford, L. R., Kimes, S. E. (2003).
  A comparison of forecasting methods for hotel revenue management.
  International Journal of Forecasting, 19(3), 401–415.
* Talluri and van Ryzin (2004)

  Talluri, K. T., van Ryzin, G. J. (2004).
  The Theory and Practice of Revenue Management.
  Springer.
* Callaway and Sant’Anna (2021)

  Callaway, B., Sant’Anna, P. H. C. (2021).
  Difference in differences with multiple time periods.
  Journal of Econometrics, 225(2), 200–230.
* Abadie et al. (2010)

  Abadie, A., Diamond, A., Hainmueller, J. (2010).
  Synthetic control methods for comparative case studies.
  Journal of the American Statistical Association, 105(490), 493–505.