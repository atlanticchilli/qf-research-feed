---
authors:
- Harrison E. Katz
- Jess Needleman
- Liz Medina
doc_id: arxiv:2601.12175v1
family_id: arxiv:2601.12175
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights
  vs. Revenue on Airbnb'
url_abs: http://arxiv.org/abs/2601.12175v1
url_html: https://arxiv.org/html/2601.12175v1
venue: arXiv q-fin
version: 1
year: 2026
---


Harrison Katz
Data Science, Forecasting, Airbnb

Jess Needleman
Data Science, Forecasting, Airbnb

Liz Medina
Data Science, Forecasting, Airbnb

###### Abstract

We analyze daily lead-time distributions for two Airbnb demand metrics—Nights Booked (volume) and Gross Booking Value (revenue)—treating each day’s allocation across 0–365 days as a compositional vector. The data span 2,557 days from January 2019 through December 2025 in a large North American region. Three findings emerge. First, GBV concentrates more heavily in mid-range horizons: beyond 90 days, GBV tail mass typically exceeds Nights by 20–50%, with ratios reaching 75% at the 180-day threshold during peak seasons. Second, Gamma and Weibull distributions fit comparably well under interval-censored cross-entropy—Gamma wins on 61% of days for Nights and 52% for GBV, with Weibull close behind at 38% and 45%. Lognormal rarely wins (<<3%). Nonparametric GAMs achieve 18–80×\times lower CRPS but sacrifice interpretability. Third, generalized Pareto fits suggest bounded tails (ξ<0\xi<0) for both metrics at thresholds below 150 days, though this may partly reflect right-truncation at 365 days; above 150 days, estimates destabilize. Bai–Perron tests with HAC standard errors identify five structural breaks in the Wasserstein distance series, with early breaks coinciding with COVID-19 disruptions. The results show that volume and revenue lead-time shapes diverge systematically, that simple two-parameter distributions capture daily pmfs adequately, and that tail inference requires care near truncation boundaries.

## 1 Introduction

Lead-time data—how far in advance travelers book—is compositional data that matters for pricing, staffing, and cash-flow forecasting (Fiori and Foroni, [2019](https://arxiv.org/html/2601.12175v1#bib.bib25 "Reservation forecasting models for hospitality SMEs with a view to enhance their economic sustainability"); Katz et al., [2024](https://arxiv.org/html/2601.12175v1#bib.bib1 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")). Each day’s bookings form a probability vector across possible lead times, summing to one. Two natural questions arise: what parametric family best describes these daily shapes, and do volume-based and revenue-based bookings distribute differently across lead times?

Research on travel lead times has a long history in tourism demand forecasting and revenue management (Kulendran and King, [1997](https://arxiv.org/html/2601.12175v1#bib.bib17 "Forecasting international quarterly tourism flows using error-correction and time-series models"); Witt and Witt, [1995](https://arxiv.org/html/2601.12175v1#bib.bib18 "Forecasting tourism demand: a review of empirical research"); Song and Li, [2008](https://arxiv.org/html/2601.12175v1#bib.bib19 "Tourism demand modelling and forecasting: a review of recent research"); Lim and McAleer, [2002](https://arxiv.org/html/2601.12175v1#bib.bib20 "Time series forecasts of international travel demand for Australia"); Fuchs and Reichel, [2011](https://arxiv.org/html/2601.12175v1#bib.bib22 "An exploratory inquiry into destination risk perceptions and risk reduction strategies of first-time vs repeat visitors to a highly volatile destination"); Neuts and Nijkamp, [2012](https://arxiv.org/html/2601.12175v1#bib.bib23 "Tourist crowding perception and acceptability in cities: an applied modelling study on Bruges")). Most of this work uses aggregate demand as a single indicator, overlooking the fact that volume-based and revenue-based bookings can exhibit systematically different lead-time patterns (Pereira, [2016](https://arxiv.org/html/2601.12175v1#bib.bib24 "An introduction to helpful forecasting methods for hotel revenue management"); Fiori and Foroni, [2019](https://arxiv.org/html/2601.12175v1#bib.bib25 "Reservation forecasting models for hospitality SMEs with a view to enhance their economic sustainability"); Webb et al., [2022](https://arxiv.org/html/2601.12175v1#bib.bib28 "Hotel revenue management forecasting accuracy: the hidden impact of booking windows"); Katz et al., [2025](https://arxiv.org/html/2601.12175v1#bib.bib2 "Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022)")). The rise of platforms like Airbnb, with their hybrid and peer-to-peer accommodation offerings, has amplified interest in how advanced vs. last-minute bookings distribute across traveler segments (Guttentag, [2015](https://arxiv.org/html/2601.12175v1#bib.bib29 "Airbnb: disruptive innovation and the rise of an informal tourism accommodation sector"); Zervas et al., [2017](https://arxiv.org/html/2601.12175v1#bib.bib30 "The rise of the sharing economy: estimating the impact of Airbnb on the hotel industry"); Ert et al., [2016](https://arxiv.org/html/2601.12175v1#bib.bib31 "Trust and reputation in the sharing economy: the role of personal photos in Airbnb"); Tussyadiah and Pesonen, [2016](https://arxiv.org/html/2601.12175v1#bib.bib32 "Impacts of peer-to-peer accommodation use on travel patterns"); Sainaghi and Baggio, [2020](https://arxiv.org/html/2601.12175v1#bib.bib33 "Substitution threat between Airbnb and hotels: myth or reality?")). Some studies focus on pricing or occupancy strategies (Assaf and Tsionas, [2019](https://arxiv.org/html/2601.12175v1#bib.bib43 "Quantitative research in tourism and hospitality: an agenda for best-practice recommendations"); Zaki, [2022](https://arxiv.org/html/2601.12175v1#bib.bib44 "Implementing dynamic revenue management in hotels during COVID-19: value stream and wavelet coherence perspectives"); Yang and Mao, [2020](https://arxiv.org/html/2601.12175v1#bib.bib34 "Location advantages of lodging properties: a comparison between hotels and Airbnb units in an urban environment"); Sharma et al., [2021](https://arxiv.org/html/2601.12175v1#bib.bib45 "Hotels’ COVID-19 innovation and performance")), but few examine detailed *distributional* properties of volume vs. revenue bookings, especially in the context of disruptive events like COVID-19 (Gössling et al., [2021](https://arxiv.org/html/2601.12175v1#bib.bib35 "Pandemics, tourism and global change: a rapid assessment of COVID-19"); Sigala, [2020](https://arxiv.org/html/2601.12175v1#bib.bib36 "Tourism and COVID-19: impacts and implications for advancing and resetting industry and research"); Okafor et al., [2022](https://arxiv.org/html/2601.12175v1#bib.bib37 "COVID-19 economic policy response, resilience and tourism recovery"); Mueller and Sobreira, [2024](https://arxiv.org/html/2601.12175v1#bib.bib38 "Tourism forecasts after COVID-19: evidence from Portugal")). Recent work on Airbnb stay lengths documents that the pandemic induced structural shifts in the *distribution* of trip durations, not merely changes in averages (Katz and Savage, [2025](https://arxiv.org/html/2601.12175v1#bib.bib3 "Slomads rising: structural shifts in U.S. Airbnb stay lengths during and after the pandemic (2019–2024)")); similar distributional thinking applies to lead times.

Lead-time forecasting has emerged as a specialized subfield within hospitality analytics (Fiori and Foroni, [2020](https://arxiv.org/html/2601.12175v1#bib.bib26 "Prediction accuracy for reservation-based forecasting methods applied in revenue management"); de Oliveira et al., [2021](https://arxiv.org/html/2601.12175v1#bib.bib27 "Lead time forecasting with machine learning techniques for a pharmaceutical supply chain"); Katz et al., [2024](https://arxiv.org/html/2601.12175v1#bib.bib1 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")). Early vs. late bookings directly influence capacity, staffing, and dynamic pricing decisions (Lim and McAleer, [2002](https://arxiv.org/html/2601.12175v1#bib.bib20 "Time series forecasts of international travel demand for Australia"); Fiori and Foroni, [2019](https://arxiv.org/html/2601.12175v1#bib.bib25 "Reservation forecasting models for hospitality SMEs with a view to enhance their economic sustainability")). Recent econometric work also underscores the role of structural breaks, whereby exogenous shocks cause persistent shifts in time-series behavior (Bai and Perron, [2003](https://arxiv.org/html/2601.12175v1#bib.bib5 "Computation and analysis of multiple structural change models")). In travel contexts, such shocks include financial crises, pandemics, and policy changes that reshape patterns of arrivals, spending, and booking windows (Götz et al., [2021](https://arxiv.org/html/2601.12175v1#bib.bib41 "How personality and policy predict pandemic behavior: understanding sheltering-in-place in 54 countries at the onset of COVID-19"); Okafor et al., [2022](https://arxiv.org/html/2601.12175v1#bib.bib37 "COVID-19 economic policy response, resilience and tourism recovery"); Sainaghi and Chica-Olmo, [2022](https://arxiv.org/html/2601.12175v1#bib.bib42 "The effects of location before and during COVID-19: impacts on revenue of Airbnb listings in Milan (Italy)")). Although the tourism literature documents regime shifts in aggregated arrivals (Kulendran and Witt, [2003](https://arxiv.org/html/2601.12175v1#bib.bib21 "Leading indicator tourism forecasts")) and some segment-specific disruptions (Gursoy and Chi, [2020](https://arxiv.org/html/2601.12175v1#bib.bib39 "Effects of COVID-19 pandemic on hospitality industry: review of the current situations and a research agenda"); Hall et al., [2020](https://arxiv.org/html/2601.12175v1#bib.bib40 "Pandemics, transformations and tourism: be careful what you wish for")), fewer studies compare volume-based vs. revenue-based lead-time distributions at daily granularity.

A separate literature addresses the distributional fitting of duration and lead-time data. The lognormal, Weibull, and Gamma families are standard candidates for right-skewed, positive-valued data (Johnson et al., [1994](https://arxiv.org/html/2601.12175v1#bib.bib16 "Continuous univariate distributions")). In hospitality contexts, Fiori and Foroni ([2020](https://arxiv.org/html/2601.12175v1#bib.bib26 "Prediction accuracy for reservation-based forecasting methods applied in revenue management")) apply these families to hotel booking data, and de Oliveira et al. ([2021](https://arxiv.org/html/2601.12175v1#bib.bib27 "Lead time forecasting with machine learning techniques for a pharmaceutical supply chain")) compare parametric and nonparametric approaches for lead-time prediction. Compositional methods add another layer: when the object of interest is a probability vector rather than a scalar, standard regression and ARMA techniques do not apply directly. The compositional data analysis literature (Aitchison, [1982](https://arxiv.org/html/2601.12175v1#bib.bib10 "The statistical analysis of compositional data"), [1986](https://arxiv.org/html/2601.12175v1#bib.bib11 "The statistical analysis of compositional data"); Pawlowsky-Glahn et al., [2015](https://arxiv.org/html/2601.12175v1#bib.bib12 "Modeling and analysis of compositional data")) provides transformations (additive log-ratio, centered log-ratio, isometric log-ratio) that map the simplex to Euclidean space, enabling multivariate methods. The Katz framework for Bayesian Dirichlet time-series models (Katz et al., [2024](https://arxiv.org/html/2601.12175v1#bib.bib1 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times"); Katz and Weiss, [2025](https://arxiv.org/html/2601.12175v1#bib.bib4 "A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares")) applies these ideas to lead-time forecasting; we draw on its conceptual foundations here.

Extreme-value methods offer tools for tail analysis. The generalized Pareto distribution (GPD) is the canonical model for exceedances above a threshold (Davison and Smith, [1990](https://arxiv.org/html/2601.12175v1#bib.bib8 "Models for exceedances over high thresholds"); Coles, [2001](https://arxiv.org/html/2601.12175v1#bib.bib9 "An introduction to statistical modeling of extreme values")). In hospitality, Fiori and Foroni ([2020](https://arxiv.org/html/2601.12175v1#bib.bib26 "Prediction accuracy for reservation-based forecasting methods applied in revenue management")) use GPD to characterize rare long-horizon bookings. A key diagnostic is threshold stability: if the GPD is appropriate, the shape parameter should stabilize as the threshold increases (Coles, [2001](https://arxiv.org/html/2601.12175v1#bib.bib9 "An introduction to statistical modeling of extreme values")). Failure to stabilize suggests model misspecification or data artifacts such as truncation.

We address these literatures with data from Airbnb. The platform records both Nights Booked (a volume measure) and Gross Booking Value (a revenue measure) at each check-in date, enabling direct comparison of their lead-time compositions. We analyze 2,557 days from January 2019 through December 2025 in a large North American region. Our methodological contributions include: (1) cross-entropy minimization for parametric fitting on truncated support, which respects the discrete nature of observed lead times while assuming an underlying continuous process; (2) strictly proper scoring rules (CRPS) for model comparison; (3) robust GPD fitting with threshold stability diagnostics; and (4) HAC-robust structural break detection applied to distributional divergence.

Three substantive findings emerge. First, GBV has systematically heavier mid-range tails than Nights: beyond 90 days, the GBV share typically exceeds Nights by 20–50%, with ratios reaching 75% at the 180-day threshold during peak seasons. Second, Gamma and Weibull provide nearly equivalent fits for daily pmfs, with Gamma holding a slight edge (winning 55–60% of days by cross-entropy), while Lognormal is dominated. GAMs achieve superior CRPS but at the cost of interpretability. Third, GPD tail estimates are reliable only for thresholds below 150 days; beyond that, right-truncation at 365 days induces instability that could mislead inference. These findings have practical implications for revenue forecasting—models that ignore the volume-revenue divergence will systematically mispredict cash-flow timing—and methodological implications for applied extreme-value analysis of truncated data.

Section [2](https://arxiv.org/html/2601.12175v1#S2 "2 Data and Preprocessing ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") describes the data and preprocessing. Section [3](https://arxiv.org/html/2601.12175v1#S3 "3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") details the methods: Wasserstein distance, structural breaks, GPD fitting, interval-censored likelihood, and scoring rules. Section [4](https://arxiv.org/html/2601.12175v1#S4 "4 Results ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") presents results. Section [5](https://arxiv.org/html/2601.12175v1#S5 "5 Discussion ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") discusses implications and limitations.

## 2 Data and Preprocessing

### 2.1 Data Source and Scope

The data are proprietary Airbnb bookings from a large North American region, January 1, 2019 through December 31, 2025. For each calendar day dd, we observe two quantities at each integer lead time ℓ∈{0,1,…,365}\ell\in\{0,1,\ldots,365\}: the total Nights Booked with check-in at day d+ℓd+\ell, and the corresponding Gross Booking Value. Dividing by daily totals yields probability vectors: the proportion of that day’s bookings (by volume or revenue) allocated to each lead-time bin.

Bookings beyond 365 days comprise less than 0.5% of the total and are excluded. This truncation is standard in lead-time analysis and captures the vast majority of booking behavior, but it has implications for tail inference that we address in Section [4](https://arxiv.org/html/2601.12175v1#S4 "4 Results ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"). The final sample contains 2,557 day-level probability mass functions (pmfs) for each metric, covering pre-COVID (2019), pandemic (2020–2021), and recovery (2022–2025) periods.

### 2.2 Compositional Vectors

Let xd,ℓ(N)x\_{d,\ell}^{(N)} denote the proportion of Nights Booked on day dd at lead time ℓ\ell, and xd,ℓ(G)x\_{d,\ell}^{(G)} the corresponding proportion of GBV. The daily compositional vectors are

|  |  |  |
| --- | --- | --- |
|  | 𝐱d(N)=(xd,0(N),xd,1(N),…,xd,365(N)),𝐱d(G)=(xd,0(G),xd,1(G),…,xd,365(G)),\mathbf{x}\_{d}^{(N)}=\bigl(x\_{d,0}^{(N)},x\_{d,1}^{(N)},\ldots,x\_{d,365}^{(N)}\bigr),\quad\mathbf{x}\_{d}^{(G)}=\bigl(x\_{d,0}^{(G)},x\_{d,1}^{(G)},\ldots,x\_{d,365}^{(G)}\bigr), |  |

each summing to one. The lead time ℓ=0\ell=0 corresponds to same-day bookings; ℓ=365\ell=365 corresponds to bookings made exactly one year in advance.

These vectors lie on the 365-simplex, a constrained space where standard Euclidean methods can be misleading. Our analysis proceeds in two modes: direct comparison of pmfs via Wasserstein distance and tail-mass ratios, and parametric fitting that treats each day’s pmf as arising from a continuous distribution observed at discrete points.

Throughout, we weight days equally rather than weighting by daily booking volume. This means our estimand is “the typical daily distribution shape,” not “the distribution of lead times across all bookings.” If high-volume days systematically differ from low-volume days, our aggregates may not reflect the booking-weighted distribution. We adopt equal day-weighting because our primary interest is in how distribution shapes evolve over time, not in characterizing the marginal distribution of a randomly sampled booking.

## 3 Methods

### 3.1 Wasserstein Distance

We measure daily divergence between Nights and GBV with the Wasserstein-1 (earth-mover) distance. For discrete pmfs 𝐩=(p0,…,p365)\mathbf{p}=(p\_{0},\ldots,p\_{365}) and 𝐪=(q0,…,q365)\mathbf{q}=(q\_{0},\ldots,q\_{365}) on a common ordered support, the Wasserstein-1 distance simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | W1​(𝐩,𝐪)=∑ℓ=0365|Fp​(ℓ)−Fq​(ℓ)|,W\_{1}(\mathbf{p},\mathbf{q})=\sum\_{\ell=0}^{365}\bigl|F\_{p}(\ell)-F\_{q}(\ell)\bigr|, |  | (1) |

where Fp​(ℓ)=∑k=0ℓpkF\_{p}(\ell)=\sum\_{k=0}^{\ell}p\_{k} is the cumulative distribution function. This metric captures how much “mass” must be moved, and how far, to transform one distribution into the other. Unlike Kullback–Leibler divergence, it is symmetric and defined even when supports differ.

For each day dd, we compute

|  |  |  |
| --- | --- | --- |
|  | Wd=W1​(𝐱d(N),𝐱d(G)).W\_{d}=W\_{1}\bigl(\mathbf{x}\_{d}^{(N)},\mathbf{x}\_{d}^{(G)}\bigr). |  |

The resulting time series {Wd}d=1D\{W\_{d}\}\_{d=1}^{D} tracks how the shapes of volume and revenue distributions diverge over time. To quantify uncertainty in summary statistics, we use block bootstrap with block size ⌈n1/3⌉\lceil n^{1/3}\rceil to account for serial dependence (Künsch, [1989](https://arxiv.org/html/2601.12175v1#bib.bib15 "The jackknife and the bootstrap for general stationary observations")), generating 1,000 replicates.

### 3.2 Structural Breaks

We test for structural breaks in {Wd}\{W\_{d}\} using the Bai–Perron procedure (Bai and Perron, [2003](https://arxiv.org/html/2601.12175v1#bib.bib5 "Computation and analysis of multiple structural change models")), which identifies multiple breakpoints by minimizing the sum of squared residuals subject to a minimum segment length. We set the maximum number of breaks to five and the trimming fraction to 5%, meaning each regime must contain at least 5% of the sample (≈128\approx 128 days). Model selection uses the Bayesian Information Criterion (BIC).

To account for serial correlation and heteroskedasticity in inference, we employ Newey–West HAC standard errors (Newey and West, [1987](https://arxiv.org/html/2601.12175v1#bib.bib7 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix")) with bandwidth selected by the Andrews ([1991](https://arxiv.org/html/2601.12175v1#bib.bib6 "Heteroskedasticity and autocorrelation consistent covariance matrix estimation")) plug-in rule. The sup-F statistic tests the null hypothesis of no breaks against the alternative of at least one break.

### 3.3 Tail Analysis

#### 3.3.1 Tail-Mass Ratios

For threshold u∈{7,30,60,90,180}u\in\{7,30,60,90,180\} days, we define the daily tail-mass ratio

|  |  |  |
| --- | --- | --- |
|  | Ratiod​(u)=∑ℓ>uxd,ℓ(G)∑ℓ>uxd,ℓ(N).\mathrm{Ratio}\_{d}(u)=\frac{\sum\_{\ell>u}x\_{d,\ell}^{(G)}}{\sum\_{\ell>u}x\_{d,\ell}^{(N)}}. |  |

Values above one indicate that GBV has proportionally more mass in the far horizon than Nights on that day. Time series of these ratios reveal whether the volume-revenue divergence concentrates in particular lead-time ranges and how it evolves over the sample period.

We also track absolute tail mass—∑ℓ>uxd,ℓ(N)\sum\_{\ell>u}x\_{d,\ell}^{(N)} and ∑ℓ>uxd,ℓ(G)\sum\_{\ell>u}x\_{d,\ell}^{(G)}—to separate compositional shifts from changes in overall booking patterns. A high tail-mass ratio could arise because GBV shifted toward long horizons, or because Nights shifted toward short horizons; the absolute measures distinguish these cases.

#### 3.3.2 Generalized Pareto Distribution

For extreme-tail characterization, we fit generalized Pareto distributions (GPD) using the Peak Over Threshold (POT) approach (Davison and Smith, [1990](https://arxiv.org/html/2601.12175v1#bib.bib8 "Models for exceedances over high thresholds")). For a chosen threshold uu, exceedances Y=X−uY=X-u given X>uX>u follow a GPD:

|  |  |  |  |
| --- | --- | --- | --- |
|  | FGPD​(y;ξ,β)=1−(1+ξ​yβ)−1/ξ,y>0,β>0,F\_{\mathrm{GPD}}(y;\xi,\beta)=1-\Bigl(1+\xi\frac{y}{\beta}\Bigr)^{-1/\xi},\quad y>0,\;\beta>0, |  | (2) |

where ξ\xi is the shape parameter and β\beta is the scale. The shape determines tail behavior: ξ<0\xi<0 implies a bounded upper tail (Weibull-type), ξ=0\xi=0 corresponds to exponential decay, and ξ>0\xi>0 implies a heavy Pareto-type tail.

The target of our GPD analysis is the day-weighted mixture distribution

|  |  |  |
| --- | --- | --- |
|  | p¯​(ℓ)=1D​∑d=1Dxd,ℓ,\bar{p}(\ell)=\frac{1}{D}\sum\_{d=1}^{D}x\_{d,\ell}, |  |

which weights each day equally regardless of booking volume, consistent with our estimand choice. To approximate integrals under p¯\bar{p}, we generate synthetic lead times by drawing 1,000 values per day from each day’s pmf, then pooling across all days. This yields approximately 2.5 million draws per metric, from which we extract exceedances above each threshold.

Fitting uses a hierarchical fallback strategy to ensure convergence:

1. 1.

   Maximum likelihood via evd::fpot (preferred).
2. 2.

   MLE via ismev::gpd.fit (alternative optimizer).
3. 3.

   Probability-weighted moments (PWM), more stable for small samples or near-boundary parameters.
4. 4.

   Method of moments (MOM) as a last resort.

We report point estimates and exceedance counts but not confidence intervals. The synthetic sample size is a computational choice (1,000 draws/day), not a feature of the data; any “standard errors” from this procedure would shrink arbitrarily with more draws and thus lack inferential meaning. Point estimates are insensitive to the number of synthetic draws; only numerical precision scales with it.

A critical diagnostic is threshold stability: the shape parameter should stabilize as the threshold increases, provided the GPD model is appropriate and the data are not truncated or otherwise distorted (Coles, [2001](https://arxiv.org/html/2601.12175v1#bib.bib9 "An introduction to statistical modeling of extreme values")). We fit GPDs at thresholds u∈{60,90,120,150,180,210,240,270}u\in\{60,90,120,150,180,210,240,270\} and plot ξ^​(u)\hat{\xi}(u) against uu to assess stability. Failure to stabilize—particularly erratic behavior at high thresholds—signals that inference should be restricted to lower thresholds.

### 3.4 Parametric Distribution Fitting

#### 3.4.1 Interval-Censored Cross-Entropy Objective

We fit Gamma, Weibull, and Lognormal distributions to each daily pmf. The motivation is that lead times are integers from an underlying continuous booking process. Treating the count at lead time ℓ\ell as a point mass ignores the discretization; treating it as interval-censored within [ℓ−0.5,ℓ+0.5)[\ell-0.5,\ell+0.5) respects the continuous-to-discrete mapping.

For a distribution with cdf F​(⋅;θ)F(\cdot;\theta) truncated to the support [0,365][0,365], the probability assigned to bin ℓ\ell is

|  |  |  |
| --- | --- | --- |
|  | pℓ​(θ)=F​(ℓ+0.5;θ)−F​(ℓ−0.5;θ)F​(365.5;θ),p\_{\ell}(\theta)=\frac{F(\ell+0.5;\theta)-F(\ell-0.5;\theta)}{F(365.5;\theta)}, |  |

with boundary modification p0​(θ)=F​(0.5;θ)/F​(365.5;θ)p\_{0}(\theta)=F(0.5;\theta)/F(365.5;\theta). The denominator ensures the fitted distribution integrates to one over the observed support, consistent with our data exclusion of bookings beyond 365 days.

Given observed proportions {xℓ}\{x\_{\ell}\}, we minimize cross-entropy:

|  |  |  |
| --- | --- | --- |
|  | H​(𝐱,𝐩)=−∑ℓ=0365xℓ​log⁡pℓ​(θ).H(\mathbf{x},\mathbf{p})=-\sum\_{\ell=0}^{365}x\_{\ell}\log p\_{\ell}(\theta). |  |

If booking counts ndn\_{d} were available, the multinomial log-likelihood would be nd​∑ℓxd,ℓ​log⁡pℓ​(θ)n\_{d}\sum\_{\ell}x\_{d,\ell}\log p\_{\ell}(\theta). Because we observe xd,ℓx\_{d,\ell} but not ndn\_{d}, we maximize the normalized objective ∑ℓxd,ℓ​log⁡pℓ​(θ)\sum\_{\ell}x\_{d,\ell}\log p\_{\ell}(\theta), which ranks models identically within a day when parameter counts match.

#### 3.4.2 Parametric Families

We consider three families:

##### Gamma.

With shape α>0\alpha>0 and rate λ>0\lambda>0:

|  |  |  |
| --- | --- | --- |
|  | f​(x;α,λ)=λαΓ​(α)​xα−1​e−λ​x,x>0.f(x;\alpha,\lambda)=\frac{\lambda^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x},\quad x>0. |  |

The Gamma is flexible for right-skewed data and nests the exponential (α=1\alpha=1).

##### Weibull.

With shape k>0k>0 and scale λ>0\lambda>0:

|  |  |  |
| --- | --- | --- |
|  | f​(x;k,λ)=kλ​(xλ)k−1​exp⁡[−(x/λ)k],x>0.f(x;k,\lambda)=\frac{k}{\lambda}\Bigl(\frac{x}{\lambda}\Bigr)^{k-1}\exp\bigl[-(x/\lambda)^{k}\bigr],\quad x>0. |  |

The Weibull is standard in survival and reliability analysis, with shape k<1k<1 implying a decreasing hazard.

##### Lognormal.

If log⁡X∼N​(μ,σ2)\log X\sim N(\mu,\sigma^{2}):

|  |  |  |
| --- | --- | --- |
|  | f​(x;μ,σ)=1x​σ​2​π​exp⁡[−(log⁡x−μ)22​σ2],x>0.f(x;\mu,\sigma)=\frac{1}{x\sigma\sqrt{2\pi}}\exp\Bigl[-\frac{(\log x-\mu)^{2}}{2\sigma^{2}}\Bigr],\quad x>0. |  |

The Lognormal has heavier tails than Gamma or Weibull for comparable location/scale. With the interval-censoring setup, we evaluate F​(0.5)F(0.5) rather than F​(0)F(0), so no shift is needed to handle the ℓ=0\ell=0 boundary.

Optimization uses BFGS with log-transformed parameters to ensure positivity.

#### 3.4.3 Model Comparison

Because all candidate parametric families have k=2k=2 parameters, model selection reduces to selection by cross-entropy: the distribution with the lowest H​(𝐱,𝐩)H(\mathbf{x},\mathbf{p}) wins. We refer to this as the “best fit” for a given day. Note that the cross-entropy differences we report are normalized (per-day, unitless); they would scale with booking counts if counts were available.

For each day and metric, we record which distribution achieves the lowest cross-entropy. We also compute pairwise differences—Lognormal minus Gamma, Weibull minus Gamma—and examine their distributions across days.

### 3.5 Nonparametric GAM

As a flexible benchmark, we fit a generalized additive model (GAM) to each daily pmf. Let η​(ℓ)=s​(ℓ)\eta(\ell)=s(\ell) be a smooth function of lead time, modeled as a cubic regression spline with penalty on second derivatives. We use restricted maximum likelihood (REML) for smoothing parameter selection (Wood, [2011](https://arxiv.org/html/2601.12175v1#bib.bib14 "Fast stable restricted maximum likelihood and marginal likelihood estimation of semiparametric generalized linear models")), which balances fit and smoothness without overfitting.

Basis dimension is initially set to k=20k=20 and increased (doubling until k=100k=100) if the k.check diagnostic indicates inadequate flexibility (k-index <0.8<0.8 and p<0.05p<0.05). Fitted values η^​(ℓ)\hat{\eta}(\ell) are exponentiated and normalized to sum to one, yielding a nonparametric pmf estimate.

### 3.6 Scoring Rules

We evaluate all fitted distributions using the continuous ranked probability score (CRPS), a strictly proper scoring rule (Gneiting and Raftery, [2007](https://arxiv.org/html/2601.12175v1#bib.bib13 "Strictly proper scoring rules, prediction, and estimation")). For a fitted cdf F^\hat{F} and empirical cdf FempF\_{\mathrm{emp}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CRPS​(F^,Femp)=∑ℓ=0365(F^​(ℓ)−Femp​(ℓ))2.\mathrm{CRPS}(\hat{F},F\_{\mathrm{emp}})=\sum\_{\ell=0}^{365}\bigl(\hat{F}(\ell)-F\_{\mathrm{emp}}(\ell)\bigr)^{2}. |  | (3) |

We evaluate the integral as a discrete sum over integer lead times; this is equivalent to a Cramér–von Mises discrepancy on the observed support. CRPS is strictly proper, meaning the expected score is minimized when the fitted distribution equals the true data-generating distribution. Unlike cross-entropy, CRPS does not blow up when the fitted distribution assigns low probability to observed outcomes.

We also report Kullback–Leibler divergence for continuity with prior work:

|  |  |  |
| --- | --- | --- |
|  | KLD​(𝐱,𝐱^)=∑ℓ=0365xℓ​log⁡xℓx^ℓ,\mathrm{KLD}(\mathbf{x},\hat{\mathbf{x}})=\sum\_{\ell=0}^{365}x\_{\ell}\log\frac{x\_{\ell}}{\hat{x}\_{\ell}}, |  |

with small-sample smoothing (xℓ←xℓ+10−16x\_{\ell}\leftarrow x\_{\ell}+10^{-16}) to avoid division by zero.

## 4 Results

We organize results around four findings: (1) aggregated distributions and their crossover, (2) structural breaks in daily divergence, (3) tail-mass differences and GPD estimates, and (4) parametric fitting comparisons.

### 4.1 Aggregated Distributions

Figure [1](https://arxiv.org/html/2601.12175v1#Sx2.F1 "Figure 1 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") shows the day-weighted pooled lead-time distributions for Nights and GBV across the entire sample. Both metrics peak at ℓ=0\ell=0: approximately 4.3% of GBV and 4.2% of Nights occur on same-day bookings. The distributions decline rapidly through the first week, then more gradually. By ℓ=25\ell=25, cumulative mass reaches 50%; by ℓ=90\ell=90, it exceeds 75%.

The curves cross near ℓ=30\ell=30 days. Below this threshold, Nights slightly exceeds GBV in proportional terms. Above it, GBV exceeds Nights. The gap is modest but persistent: GBV’s pmf lies above Nights’ pmf from roughly 30 to 200 days, after which both converge toward negligible mass. This crossover suggests that revenue-weighted bookings skew toward longer planning horizons than volume-weighted bookings—guests who generate more revenue tend to book earlier, on average.

The crossover is not an artifact of a few outlier days. Examining the 10th and 90th percentiles of daily pmfs (not shown) confirms that the pattern holds across the distribution of days, with variation in the exact crossover point but consistent qualitative behavior.

### 4.2 Wasserstein Distance and Structural Breaks

Figure [2](https://arxiv.org/html/2601.12175v1#Sx2.F2 "Figure 2 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") plots the daily Wasserstein-1 distance WdW\_{d} between Nights and GBV. The series averages 8.67 with a block-bootstrap 95% confidence interval of [8.42, 8.92]. Substantial day-to-day variation is evident, with WdW\_{d} ranging from under 5 to over 15.

The series exhibits clear seasonality. Divergence peaks in summer months (June–August), when advance bookings for peak travel periods accumulate. During these months, high-value travelers book further ahead for desirable properties, increasing the GBV tail mass relative to Nights. Divergence troughs in winter, when booking windows shorten and the volume-revenue gap narrows.

The Bai–Perron procedure identifies five structural breakpoints, partitioning the sample into six regimes. Table [1](https://arxiv.org/html/2601.12175v1#S4.T1 "Table 1 ‣ 4.2 Wasserstein Distance and Structural Breaks ‣ 4 Results ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") reports the estimated break dates and segment means.

Table 1: Estimated structural breakpoints in Wasserstein distance series. Dates are point estimates from Bai–Perron with 5% trimming and BIC selection.

| Break | Date | Segment Mean WdW\_{d} |
| --- | --- | --- |
| — | 2019-01-01 (start) | 8.2 |
| 1 | 2020-10-15 | 6.4 |
| 2 | 2021-06-22 | 9.1 |
| 3 | 2022-11-03 | 8.8 |
| 4 | 2023-09-18 | 9.3 |
| 5 | 2024-05-27 | 9.6 |
| — | 2025-12-31 (end) | — |

The regimes correspond to:

1. 1.

   Baseline (2019-01 to 2020-10): Moderate, stable divergence with seasonal variation, persisting through early pandemic.
2. 2.

   Pandemic compression (2020-10 to 2021-06): Divergence drops sharply as booking windows compress and high-value travel declines.
3. 3.

   Recovery phase I (2021-06 to 2022-11): Divergence rebounds as travel resumes, initially overshooting pre-pandemic levels.
4. 4.

   Stabilization (2022-11 to 2023-09): Divergence settles into a new equilibrium above baseline.
5. 5.

   Late adjustments (2023-09 to 2024-05): Minor shifts, possibly reflecting macroeconomic conditions or platform changes.
6. 6.

   Current regime (2024-05 to present): Elevated divergence with pronounced seasonality.

The sup-F test decisively rejects the null of no breaks (p<0.001p<0.001), confirming that the volume-revenue divergence underwent persistent structural shifts rather than merely temporary fluctuations. The first two breaks (October 2020, June 2021) align with COVID-related disruptions; later breaks may reflect post-pandemic normalization, macroeconomic conditions, or platform-specific changes.

### 4.3 Tail Mass Analysis

#### 4.3.1 Tail-Mass Ratios

Figure [3](https://arxiv.org/html/2601.12175v1#Sx2.F3 "Figure 3 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") presents time series of tail-mass ratios for thresholds at 7, 30, 60, 90, and 180 days. The patterns differ markedly by threshold:

##### 7 days.

The ratio hovers near 1.0 with modest variation. There is no systematic dominance of GBV over Nights at very short horizons. This makes sense: same-week bookings are often spontaneous or necessity-driven, with less differentiation between high-value and average travelers.

##### 30 days.

GBV begins to pull ahead. The ratio typically ranges from 1.05 to 1.15, with seasonal peaks reaching 1.20. The gap is small but consistent.

##### 60 days.

The ratio increases to 1.10–1.25, with summer peaks near 1.30. The mid-range horizon is where the volume-revenue divergence concentrates.

##### 90 days.

Ratios of 1.20–1.40 are common, with peaks exceeding 1.50 in some summers. Beyond three months, GBV’s tail-mass advantage becomes substantial.

##### 180 days.

The ratio is most volatile here, ranging from 1.0 to 1.75. Summer peaks are pronounced; winter troughs can approach 1.0. The six-month-plus horizon captures relatively few bookings, so daily ratios are noisier.

COVID-19 disrupted these patterns. In early 2020, as booking windows collapsed, the ratios at longer thresholds dropped sharply and briefly inverted (GBV << Nights) for some periods. Recovery restored the pre-pandemic pattern, though with higher baseline ratios in the post-2022 period.

#### 4.3.2 Absolute Tail Mass

Figure [4](https://arxiv.org/html/2601.12175v1#Sx2.F4 "Figure 4 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") shows the absolute proportion of daily bookings beyond 30, 90, and 180 days for each metric.

At the 30-day threshold, roughly 55–70% of bookings (by either measure) fall beyond this horizon, depending on season. GBV exceeds Nights by 5–10 percentage points consistently. At the 90-day threshold, 20–40% of bookings remain in the tail, with GBV again exceeding Nights. At 180 days, only 5–15% of bookings are this far out, but GBV maintains its relative advantage.

The COVID period shows a dramatic collapse in tail mass for both metrics: in spring 2020, the share of bookings beyond 90 days fell from 30% to under 10% as travelers stopped planning ahead. Recovery was gradual, with tail mass returning to pre-pandemic levels by mid-2022.

These patterns confirm that the volume-revenue divergence is real and not merely an artifact of ratio construction. GBV genuinely concentrates more heavily in mid-range horizons than Nights, and this concentration persists across seasons and regimes.

### 4.4 GPD Tail Estimates

#### 4.4.1 Shape Estimates by Threshold

Figures [5](https://arxiv.org/html/2601.12175v1#Sx2.F5 "Figure 5 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") and [6](https://arxiv.org/html/2601.12175v1#Sx2.F6 "Figure 6 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") present GPD shape parameter estimates ξ^\hat{\xi} at thresholds from 60 to 270 days, with exceedance counts.

For Nights, shape estimates at low thresholds are negative and relatively stable: ξ^≈−0.20\hat{\xi}\approx-0.20 at u=60u=60, −0.28-0.28 at u=90u=90, −0.32-0.32 at u=120u=120. These values indicate bounded (Weibull-type) tails, consistent with the practical constraint that travelers rarely book more than a year in advance. At u=150u=150, the estimate is −0.16-0.16, still negative but less extreme.

For GBV, low-threshold estimates are also negative but less so: ξ^≈−0.12\hat{\xi}\approx-0.12 at u=60u=60, −0.16-0.16 at u=90u=90, −0.18-0.18 at u=120u=120 and u=150u=150. The less negative values suggest that GBV’s tail decays more slowly than Nights’ in the mid-range—consistent with the tail-mass ratio findings.

#### 4.4.2 Threshold Stability

Figure [7](https://arxiv.org/html/2601.12175v1#Sx2.F7 "Figure 7 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") plots ξ^\hat{\xi} against threshold for both metrics. The pattern is striking:

##### Below 150 days.

Both metrics show relatively stable estimates in the range ξ∈(−0.3,−0.1)\xi\in(-0.3,-0.1). GBV is generally less negative than Nights at thresholds 60–120 days, implying lighter tail decay; the difference narrows by 150 days. The stability suggests that GPD is a reasonable model for this range.

##### Above 150 days.

Estimates diverge dramatically. For Nights, ξ^\hat{\xi} increases through zero around u=200u=200, peaks at +0.26+0.26 at u=240u=240 (implying heavy tails—clearly implausible), then crashes to −1.38-1.38 at u=270u=270. For GBV, ξ^\hat{\xi} decreases monotonically, reaching −0.97-0.97 at u=270u=270.

This instability is a truncation artifact. The data are right-truncated at 365 days: we observe no lead times beyond this boundary. As the threshold approaches 365, the GPD estimator “sees” an artificial upper bound and interprets it as extreme tail boundedness (ξ≪0\xi\ll 0). But the path to this boundary is erratic because the estimator is extrapolating from a shrinking and distorted sample of exceedances.

##### Recommendation.

We restrict GPD inference to thresholds ≤150\leq 150 days, where estimates are stable and sample sizes adequate. Table [5](https://arxiv.org/html/2601.12175v1#Sx3.T5 "Table 5 ‣ Tables ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") reports these estimates. Within this range, both metrics show negative shape parameters, with GBV exhibiting less negative values at 60–120 days (ξ≈−0.15\xi\approx-0.15 vs. −0.25-0.25 for Nights); the gap narrows by 150 days. This pattern is consistent with GBV having lighter tail decay in the mid-range. However, because the support is bounded at 365 by construction, negative ξ\xi does not necessarily imply a structural upper bound on booking behavior—it may simply reflect the truncation.

### 4.5 Parametric Distribution Fits

#### 4.5.1 Parameter Estimates

Table [2](https://arxiv.org/html/2601.12175v1#Sx3.T2 "Table 2 ‣ Tables ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") reports average parameter estimates across all days for the three parametric families.

For Gamma, the shape parameter averages 0.77 for Nights and 0.80 for GBV. Values below 1 indicate right-skewed distributions with mode at zero—consistent with the concentration of bookings at short lead times. The rate parameter averages 0.013 for Nights and 0.012 for GBV. The combination of higher shape and lower rate for GBV implies a distribution shifted rightward, toward longer lead times.

For Weibull, shape averages 0.85 for Nights and 0.87 for GBV; scale averages 54.2 and 61.7 respectively. The pattern is similar: GBV’s parameters imply a distribution with more mass at longer horizons.

For Lognormal, μ\mu averages 3.41 for Nights and 3.52 for GBV; σ\sigma averages 1.32 for both. The higher μ\mu for GBV again indicates a rightward shift.

#### 4.5.2 Best-Fit Distribution by Cross-Entropy

Table [3](https://arxiv.org/html/2601.12175v1#Sx3.T3 "Table 3 ‣ Tables ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") tallies which distribution achieves the lowest cross-entropy on each day.

For Nights: Gamma wins 61.4% of days (1,570 of 2,557), Weibull wins 37.9% (969), and Lognormal wins 0.7% (18). For GBV: Gamma wins 51.9% (1,327), Weibull wins 45.4% (1,160), and Lognormal wins 2.7% (70).

The competition between Gamma and Weibull is close, especially for GBV. Lognormal rarely wins. This pattern holds across subperiods: Gamma’s edge is consistent in pre-COVID, COVID, and post-COVID regimes.

#### 4.5.3 Cross-Entropy Differences

Figure [8](https://arxiv.org/html/2601.12175v1#Sx2.F8 "Figure 8 ‣ Figures ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") shows histograms of daily cross-entropy differences. These are normalized (per-day) values; they would scale with booking counts if counts were available.

The Lognormal–Gamma difference is almost entirely positive, ranging from 0.02 to 0.20. This confirms Gamma’s decisive advantage over Lognormal: on virtually every day, Gamma fits better.

The Weibull–Gamma difference is tightly centered around zero, with most values in (−0.02,+0.02)(-0.02,+0.02). The distributions are effectively interchangeable for this application. Gamma’s slight edge in win percentage reflects many days where the difference is tiny and favors Gamma by chance.

The practical implication is that either Gamma or Weibull provides an adequate two-parameter summary of daily lead-time pmfs. Lognormal’s heavier tail does not match the bounded nature of the data.

### 4.6 Parametric vs. Nonparametric

Table [4](https://arxiv.org/html/2601.12175v1#Sx3.T4 "Table 4 ‣ Tables ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb") compares Gamma and GAM fits using CRPS and KLD.

GAM achieves substantially lower CRPS: 0.0007 vs. 0.056 for Nights (an 80×\times improvement) and 0.008 vs. 0.157 for GBV (an 18×\times improvement). These extreme ratios reflect the GAM’s flexibility: with 10–20 effective degrees of freedom, it approximates a smoothed empirical pmf rather than imposing a two-parameter shape. The GAM captures fine-grained features—local bumps, asymmetric tails, multimodal tendencies on some days—that the Gamma cannot match. These are in-sample scores: each GAM is fit and evaluated on the same day’s pmf. The GAM CRPS should be interpreted as a lower bound on achievable in-sample fit with flexible smoothers, not as a forecast performance claim. Out-of-sample evaluation would be needed to assess whether GAM’s flexibility translates to better forecasts or merely captures noise.

KLD shows a similar but less dramatic pattern: GAM achieves 0.016 vs. Gamma’s 0.039 for Nights, and 0.121 vs. 0.157 for GBV.

This creates a parsimony-flexibility tradeoff. Gamma wins by cross-entropy when parameter counts are equal (all families have k=2k=2). GAM wins by CRPS and KLD because it has more effective parameters. For forecasting applications requiring well-calibrated predictive distributions, GAM may be preferred—but this claim requires out-of-sample validation. For descriptive purposes where interpretability matters—“what is the typical shape parameter?”—Gamma provides a compact summary.

## 5 Discussion

### 5.1 Main Findings

The central finding is that revenue-weighted bookings concentrate more heavily in the 30–90 day horizon than volume-weighted bookings. The tail-mass ratios quantify this: beyond 90 days, GBV typically exceeds Nights by 20–50%, with ratios reaching 75% at the 180-day threshold during peak seasons. This is not an extreme-tail phenomenon—both metrics have bounded tails beyond 300 days—but a mid-range shift. Guests who generate higher revenue tend to book earlier, but not dramatically earlier.

The structural breaks in Wasserstein distance show that this gap is not constant. COVID compressed it; recovery restored it; seasonal patterns modulate it year after year. The five identified breakpoints partition the sample into regimes with distinct divergence levels, confirming that the volume-revenue relationship evolves with external conditions.

The distributional fitting comparison yields a practical conclusion: Gamma and Weibull are both adequate, with Gamma holding a slight edge. Lognormal is dominated. GAMs fit better by CRPS but sacrifice interpretability; their in-sample advantage reflects flexibility, not necessarily forecast skill. For most applications, a Gamma distribution with shape ≈0.8\approx 0.8 and rate ≈0.013\approx 0.013 provides a reasonable two-parameter summary of Airbnb lead-time distributions.

The GPD analysis offers a methodological caution. Shape estimates are relatively stable below 150 days, where both metrics show ξ≈−0.15\xi\approx-0.15 to −0.25-0.25. Within the observed window, this suggests bounded tails—but because the data are truncated at 365 days by construction, a negative shape parameter is largely tautological. We interpret the bounded-tail signal as descriptive of the observed distribution rather than a structural claim about booking behavior beyond the platform’s booking window. Above 150 days, instability induced by truncation would mislead inference if ignored. Researchers applying GPD to truncated data should perform threshold stability diagnostics before reporting point estimates.

### 5.2 Implications for Revenue Forecasting

The volume-revenue divergence has practical consequences for forecasting. Models that treat Nights and GBV as interchangeable—or that forecast GBV by scaling a Nights forecast—will systematically mispredict revenue timing. Specifically, they will underestimate revenue from mid-range bookings and overestimate revenue from short-horizon bookings.

Consider a simple example. Suppose a forecasting model predicts that 30% of next month’s Nights will be booked more than 60 days in advance. If the model assumes GBV follows the same distribution, it will predict 30% of revenue in this category. But if the true GBV tail mass is 36% (a ratio of 1.2), the model will underpredict far-horizon revenue by 6 percentage points. Over a fiscal quarter, this bias compounds.

The structural breaks compound the problem. A model trained on 2019 data will embed 2019’s volume-revenue relationship. If post-2022 divergence is structurally higher, the model will be miscalibrated without retraining or adjustment.

For practitioners, the volume-revenue divergence suggests that pricing algorithms trained on Nights forecasts may underweight mid-range bookings where revenue concentrates. A simple correction—inflating the 30–90 day forecast share by the estimated tail-mass ratio—could reduce revenue timing bias without requiring a full model rebuild. At current ratios (1.2–1.4 at 90 days), this adjustment would shift 2–4 percentage points of forecasted revenue from short-horizon to mid-range bins.

### 5.3 Implications for Tail Inference

The GPD instability we document is a general problem for truncated data, not specific to lead times. Any dataset with a hard upper bound will exhibit similar artifacts when GPD is applied near that bound. The threshold stability diagnostic is essential: if ξ^\hat{\xi} does not stabilize, the model is unreliable in that range.

Our recommendation—restricting inference to u≤150u\leq 150 days when the truncation is at 365—is conservative. Other analysts might choose a higher cutoff if their data extend further or their sample sizes are larger. The key is to check stability empirically rather than relying on asymptotic guarantees.

### 5.4 Limitations

Several limitations warrant mention.

First, the analysis is in-sample. We fit distributions to observed data but do not evaluate out-of-sample forecast accuracy. The GAM’s superior CRPS might not translate to better forecasts if the model overfits daily idiosyncrasies.

Second, we analyze a single region. Lead-time patterns likely differ across geographies: European travelers may book further ahead than North Americans; urban destinations may have shorter booking windows than leisure destinations. Generalizing our findings requires replication in other markets.

Third, we omit covariates. External factors—macroeconomic conditions, competitor pricing, local events—surely influence lead-time distributions. Incorporating these in a regression framework could explain some of the day-to-day variation we observe.

Fourth, the 365-day truncation, while capturing 99.5% of bookings, precludes analysis of the true extreme tail. Travelers who book 18+ months ahead are rare but may be substantively different; we cannot characterize them with this data.

### 5.5 Future Directions

Several extensions are natural.

Hierarchical models could pool information across regions, improving estimates for small markets while allowing region-specific deviations. A Bayesian framework with shrinkage priors would be suitable (Katz et al., [2024](https://arxiv.org/html/2601.12175v1#bib.bib1 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")).

Covariates could be incorporated via regression on the distribution parameters. For instance, Gamma shape and rate could depend on day-of-week, season, or economic indicators. This would connect the distributional analysis to causal questions about what drives lead-time behavior.

Out-of-sample evaluation would test whether GAM’s in-sample CRPS advantage translates to forecast improvement. A rolling-origin design with multiple forecast horizons would be informative.

Finally, extension to other compositional outcomes—not just lead times but geographic mix, property-type mix, or price-tier mix—would broaden the applicability of these methods.

## 6 Conclusion

We have analyzed daily lead-time distributions for Nights Booked and Gross Booking Value on Airbnb, treating each day’s allocation as a compositional vector. The analysis yields three main findings.

First, GBV concentrates more heavily in mid-range horizons than Nights. Beyond 90 days, GBV typically exceeds Nights by 20–50%, with ratios reaching 75% at the 180-day threshold during peak seasons. This is a mid-range shift, not an extreme-tail phenomenon.

Second, Gamma and Weibull fit daily pmfs comparably well, with Gamma winning 55–60% of days by cross-entropy. Lognormal is dominated. GAMs achieve superior in-sample CRPS but sacrifice interpretability.

Third, GPD confirms bounded tails (ξ<0\xi<0) at reliable thresholds (≤150\leq 150 days), but threshold instability at higher values reflects truncation artifacts. Researchers should perform stability diagnostics before reporting GPD estimates on truncated data.

These findings contribute to tourism forecasting methodology and practical revenue management. The documented volume-revenue divergence, and its evolution over COVID and recovery, has direct implications for cash-flow prediction. The methodological lessons—interval-censored likelihood, CRPS scoring, threshold stability checks—apply broadly to compositional and duration data in other domains.

## Acknowledgements

We thank Sean Wilson, Jackson Wang, and Peter Coles for helpful discussions, Ellie Mertz and Adam Liss for championing the research.

## References

* J. Aitchison (1982)
  The statistical analysis of compositional data.
  Journal of the Royal Statistical Society: Series B (Methodological) 44 (2),  pp. 139–177.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* J. Aitchison (1986)
  The statistical analysis of compositional data.
   Chapman & Hall, London.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* D. W. K. Andrews (1991)
  Heteroskedasticity and autocorrelation consistent covariance matrix estimation.
  Econometrica 59 (3),  pp. 817–858.
  Cited by: [§3.2](https://arxiv.org/html/2601.12175v1#S3.SS2.p2.1 "3.2 Structural Breaks ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* A. G. Assaf and M. G. Tsionas (2019)
  Quantitative research in tourism and hospitality: an agenda for best-practice recommendations.
  International Journal of Contemporary Hospitality Management 31 (7),  pp. 2776–2787.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* J. Bai and P. Perron (2003)
  Computation and analysis of multiple structural change models.
  Journal of Applied Econometrics 18 (1),  pp. 1–22.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§3.2](https://arxiv.org/html/2601.12175v1#S3.SS2.p1.2 "3.2 Structural Breaks ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* S. Coles (2001)
  An introduction to statistical modeling of extreme values.
   Springer, London.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p5.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§3.3.2](https://arxiv.org/html/2601.12175v1#S3.SS3.SSS2.p4.3 "3.3.2 Generalized Pareto Distribution ‣ 3.3 Tail Analysis ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* A. C. Davison and R. L. Smith (1990)
  Models for exceedances over high thresholds.
  Journal of the Royal Statistical Society: Series B (Methodological) 52 (3),  pp. 393–442.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p5.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§3.3.2](https://arxiv.org/html/2601.12175v1#S3.SS3.SSS2.p1.3 "3.3.2 Generalized Pareto Distribution ‣ 3.3 Tail Analysis ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* M. B. de Oliveira, G. Zucchi, M. Lippi, D. F. Cordeiro, N. R. da Silva, and M. Iori (2021)
  Lead time forecasting with machine learning techniques for a pharmaceutical supply chain.
  In ICEIS (1),
   pp. 634–641.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* E. Ert, A. Fleischer, and N. Magen (2016)
  Trust and reputation in the sharing economy: the role of personal photos in Airbnb.
  Tourism Management 55,  pp. 62–73.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* A. M. Fiori and I. Foroni (2019)
  Reservation forecasting models for hospitality SMEs with a view to enhance their economic sustainability.
  Sustainability 11 (5),  pp. 1274.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p1.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* A. M. Fiori and I. Foroni (2020)
  Prediction accuracy for reservation-based forecasting methods applied in revenue management.
  International Journal of Hospitality Management 84,  pp. 102332.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p5.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* G. Fuchs and A. Reichel (2011)
  An exploratory inquiry into destination risk perceptions and risk reduction strategies of first-time vs repeat visitors to a highly volatile destination.
  Tourism Management 32 (2),  pp. 266–276.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* T. Gneiting and A. E. Raftery (2007)
  Strictly proper scoring rules, prediction, and estimation.
  Journal of the American Statistical Association 102 (477),  pp. 359–378.
  Cited by: [§3.6](https://arxiv.org/html/2601.12175v1#S3.SS6.p1.2 "3.6 Scoring Rules ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* S. Gössling, D. Scott, and C. M. Hall (2021)
  Pandemics, tourism and global change: a rapid assessment of COVID-19.
  Journal of Sustainable Tourism 29 (1),  pp. 1–20.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* F. M. Götz, A. Gvirtz, A. D. Galinsky, and J. M. Jachimowicz (2021)
  How personality and policy predict pandemic behavior: understanding sheltering-in-place in 54 countries at the onset of COVID-19.
  American Psychologist 76 (1),  pp. 39–49.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* D. Gursoy and C. G. Chi (2020)
  Effects of COVID-19 pandemic on hospitality industry: review of the current situations and a research agenda.
  Journal of Hospitality Marketing & Management 29 (5),  pp. 527–529.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* D. Guttentag (2015)
  Airbnb: disruptive innovation and the rise of an informal tourism accommodation sector.
  Current Issues in Tourism 18 (12),  pp. 1192–1217.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* C. M. Hall, D. Scott, and S. Gössling (2020)
  Pandemics, transformations and tourism: be careful what you wish for.
  Tourism Geographies 22 (3),  pp. 577–598.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* N. L. Johnson, S. Kotz, and N. Balakrishnan (1994)
  Continuous univariate distributions.
  2nd edition, Vol. 1, Wiley, New York.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* H. Katz, K. T. Brusch, and R. E. Weiss (2024)
  A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times.
  International Journal of Forecasting 40 (4),  pp. 1556–1567.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p1.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§5.5](https://arxiv.org/html/2601.12175v1#S5.SS5.p2.1 "5.5 Future Directions ‣ 5 Discussion ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* H. Katz, E. Savage, and P. Coles (2025)
  Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022).
  Annals of Tourism Research Empirical Insights 6 (2),  pp. 100185.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* H. Katz and E. Savage (2025)
  Slomads rising: structural shifts in U.S. Airbnb stay lengths during and after the pandemic (2019–2024).
  Tourism and Hospitality 6 (4),  pp. 182.
  External Links: [Document](https://dx.doi.org/10.3390/tourhosp6040182)
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* H. Katz and R. E. Weiss (2025)
  A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares.
  arXiv preprint arXiv:2507.14132.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* N. Kulendran and M. L. King (1997)
  Forecasting international quarterly tourism flows using error-correction and time-series models.
  International Journal of Forecasting 13 (3),  pp. 319–327.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* N. Kulendran and S. F. Witt (2003)
  Leading indicator tourism forecasts.
  Tourism Management 24 (5),  pp. 503–510.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* H. R. Künsch (1989)
  The jackknife and the bootstrap for general stationary observations.
  Annals of Statistics 17 (3),  pp. 1217–1241.
  Cited by: [§3.1](https://arxiv.org/html/2601.12175v1#S3.SS1.p2.3 "3.1 Wasserstein Distance ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* C. Lim and M. McAleer (2002)
  Time series forecasts of international travel demand for Australia.
  Tourism Management 23 (4),  pp. 389–396.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* R. Mueller and N. Sobreira (2024)
  Tourism forecasts after COVID-19: evidence from Portugal.
  Annals of Tourism Research Empirical Insights 5 (1),  pp. 100127.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* B. Neuts and P. Nijkamp (2012)
  Tourist crowding perception and acceptability in cities: an applied modelling study on Bruges.
  Annals of Tourism Research 39 (4),  pp. 2133–2153.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* W. K. Newey and K. D. West (1987)
  A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix.
  Econometrica 55 (3),  pp. 703–708.
  Cited by: [§3.2](https://arxiv.org/html/2601.12175v1#S3.SS2.p2.1 "3.2 Structural Breaks ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* L. Okafor, U. Khalid, and S. Gopalan (2022)
  COVID-19 economic policy response, resilience and tourism recovery.
  Annals of Tourism Research Empirical Insights 3 (2),  pp. 100073.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb"),
  [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* V. Pawlowsky-Glahn, J. J. Egozcue, and R. Tolosana-Delgado (2015)
  Modeling and analysis of compositional data.
   Wiley, Chichester.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p4.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* L. N. Pereira (2016)
  An introduction to helpful forecasting methods for hotel revenue management.
  International Journal of Hospitality Management 58,  pp. 13–23.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* R. Sainaghi and R. Baggio (2020)
  Substitution threat between Airbnb and hotels: myth or reality?.
  Annals of Tourism Research 83,  pp. 102959.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* R. Sainaghi and J. Chica-Olmo (2022)
  The effects of location before and during COVID-19: impacts on revenue of Airbnb listings in Milan (Italy).
  Annals of Tourism Research 96,  pp. 103464.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p3.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* A. Sharma, H. Shin, M. J. Santa-María, and J. L. Nicolau (2021)
  Hotels’ COVID-19 innovation and performance.
  Annals of Tourism Research 88,  pp. 103180.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* M. Sigala (2020)
  Tourism and COVID-19: impacts and implications for advancing and resetting industry and research.
  Journal of Business Research 117,  pp. 312–321.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* H. Song and G. Li (2008)
  Tourism demand modelling and forecasting: a review of recent research.
  Tourism Management 29 (2),  pp. 203–220.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* I. P. Tussyadiah and J. Pesonen (2016)
  Impacts of peer-to-peer accommodation use on travel patterns.
  Journal of Travel Research 55 (8),  pp. 1022–1040.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* T. Webb, Z. Schwartz, Z. Xiang, and M. Altin (2022)
  Hotel revenue management forecasting accuracy: the hidden impact of booking windows.
  Journal of Hospitality and Tourism Insights 5 (5),  pp. 950–965.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* S. F. Witt and C. A. Witt (1995)
  Forecasting tourism demand: a review of empirical research.
  International Journal of Forecasting 11 (3),  pp. 447–475.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* S. N. Wood (2011)
  Fast stable restricted maximum likelihood and marginal likelihood estimation of semiparametric generalized linear models.
  Journal of the Royal Statistical Society: Series B (Statistical Methodology) 73 (1),  pp. 3–36.
  Cited by: [§3.5](https://arxiv.org/html/2601.12175v1#S3.SS5.p1.1 "3.5 Nonparametric GAM ‣ 3 Methods ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* Y. Yang and Z. Mao (2020)
  Location advantages of lodging properties: a comparison between hotels and Airbnb units in an urban environment.
  Annals of Tourism Research 81,  pp. 102861.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* K. Zaki (2022)
  Implementing dynamic revenue management in hotels during COVID-19: value stream and wavelet coherence perspectives.
  International Journal of Contemporary Hospitality Management 34 (5),  pp. 1768–1795.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").
* G. Zervas, D. Proserpio, and J. W. Byers (2017)
  The rise of the sharing economy: estimating the impact of Airbnb on the hotel industry.
  Journal of Marketing Research 54 (5),  pp. 687–705.
  Cited by: [§1](https://arxiv.org/html/2601.12175v1#S1.p2.1 "1 Introduction ‣ Distributional Fitting and Tail Analysis of Lead-Time Compositions: Nights vs. Revenue on Airbnb").

## Figures

![Refer to caption](fig1_aggregated.png)


Figure 1: Aggregated lead-time distributions for Nights (blue) and GBV (red), 2019–2025. Distributions are day-weighted averages of daily pmfs: p¯​(ℓ)=D−1​∑dxd,ℓ\bar{p}(\ell)=D^{-1}\sum\_{d}x\_{d,\ell}. Both peak near ℓ=0\ell=0 and decline rapidly. The curves cross around ℓ=30\ell=30 days: below, Nights slightly exceeds GBV; above, GBV exceeds Nights. The gap persists to about 200 days.

![Refer to caption](fig2_wasserstein.png)


Figure 2: Daily Wasserstein-1 distance between Nights and GBV, with structural breakpoints (dashed vertical lines) identified via Bai–Perron with HAC standard errors. The series averages 8.67 (95% CI: 8.42–8.92). Seasonality peaks in summer. Early breaks (2020–2021) align with COVID disruptions; later breaks may reflect post-pandemic normalization or other market shifts.

![Refer to caption](fig5_tail_ratios.png)


Figure 3: Tail-mass ratios (GBV/Nights) at thresholds 7, 30, 60, 90, and 180 days. At 7 days, the ratio hovers near 1.0. At longer horizons, GBV increasingly dominates: ratios reach 1.2–1.4 at 90 days and 1.5+ at 180 days during summer peaks. COVID (early 2020) briefly inverts the pattern.

![Refer to caption](fig6_tail_panels.png)


Figure 4: Proportion of daily bookings beyond 30, 90, and 180 days for Nights (blue) and GBV (red). GBV exceeds Nights at all thresholds. COVID shows a collapse in tail mass for both metrics as booking windows shortened dramatically.

![Refer to caption](fig3_gpd_nights.png)


Figure 5: GPD shape parameter ξ\xi for Nights at thresholds 60–270 days. Counts shown are synthetic exceedances (from 1,000 draws/day pooled across all days), not raw booking counts. Negative values suggest bounded tails within the observed window. Estimates are stable for u≤150u\leq 150 days; above, truncation effects dominate.

![Refer to caption](fig4_gpd_gbv.png)


Figure 6: GPD shape parameter ξ\xi for GBV at thresholds 60–270 days. Counts are synthetic exceedances. GBV shows less negative ξ\xi than Nights at thresholds 60–120 days (≈−0.15\approx-0.15 vs. −0.25-0.25), suggesting marginally lighter tail decay; the gap narrows by 150 days. High-threshold instability is pronounced.

![Refer to caption](fig_gpd_stability.png)


Figure 7: GPD shape parameter stability across thresholds. Dashed line marks ξ=0\xi=0. Below 150 days, both metrics show stable ξ∈(−0.3,−0.1)\xi\in(-0.3,-0.1), consistent with bounded tails. Above 150 days, estimates diverge: Nights swings positive then collapses to −1.4-1.4; GBV decreases monotonically to −1.0-1.0. This instability reflects right-truncation at 365 days.

![Refer to caption](fig10_aic_diff.png)


Figure 8: Histograms of daily cross-entropy differences: Lognormal minus Gamma (left), Weibull minus Gamma (right). Positive values favor Gamma. These are normalized (per-day) differences; they would scale with booking counts if counts were available. The Lognormal–Gamma difference is almost entirely positive (0.02–0.20), confirming Gamma’s dominance. The Weibull–Gamma difference is tightly centered around zero (±0.02\pm 0.02): these distributions are effectively interchangeable.

## Tables

Table 2: Average parameter estimates across all 2,557 days for three parametric families. GBV shows higher Gamma shape, lower rate, higher Weibull scale, and higher Lognormal μ\mu than Nights, all indicating a distribution shifted toward longer lead times.

| Metric | LN μ\mu | LN σ\sigma | Wei shape | Wei scale | Gamma shape | Gamma rate |
| --- | --- | --- | --- | --- | --- | --- |
| GBV | 3.52 | 1.32 | 0.87 | 61.7 | 0.80 | 0.012 |
| Nights | 3.41 | 1.32 | 0.85 | 54.2 | 0.77 | 0.013 |




Table 3: Distribution of best-fitting models by cross-entropy. Gamma wins most often, especially for Nights. Weibull is close behind for GBV. Lognormal rarely wins.

| Metric | Best Fit | Days | % |
| --- | --- | --- | --- |
| Nights | Gamma | 1,570 | 61.4 |
| Nights | Weibull | 969 | 37.9 |
| Nights | Lognormal | 18 | 0.7 |
| GBV | Gamma | 1,327 | 51.9 |
| GBV | Weibull | 1,160 | 45.4 |
| GBV | Lognormal | 70 | 2.7 |




Table 4: CRPS and KLD for Gamma vs. GAM. Lower is better. GAM achieves 18–80×\times lower CRPS than Gamma, reflecting its flexibility, but uses 10–20 effective degrees of freedom vs. Gamma’s 2 parameters.

|  | Nights (Gamma) | Nights (GAM) | GBV (Gamma) | GBV (GAM) |
| --- | --- | --- | --- | --- |
| CRPS | 0.056 | 0.0007 | 0.157 | 0.008 |
| KLD | 0.039 | 0.016 | 0.157 | 0.121 |




Table 5: GPD shape parameter estimates at reliable thresholds (u≤150u\leq 150 days). Negative ξ\xi suggests bounded tails within the observed window, though this may partly reflect truncation at 365 days. GBV shows less negative ξ\xi than Nights at 60–120 days; the difference narrows by 150. Counts nn are synthetic exceedances (1,000 draws/day ×\times 2,557 days, pooled); we report point estimates but not confidence intervals (see text).

| Threshold | Nights ξ\xi | Nights nn (synth.) | GBV ξ\xi | GBV nn (synth.) |
| --- | --- | --- | --- | --- |
| 60 days | −0.20-0.20 | 790,937 | −0.12-0.12 | 923,734 |
| 90 days | −0.28-0.28 | 493,401 | −0.16-0.16 | 616,364 |
| 120 days | −0.32-0.32 | 312,034 | −0.18-0.18 | 419,376 |
| 150 days | −0.16-0.16 | 193,665 | −0.18-0.18 | 281,748 |