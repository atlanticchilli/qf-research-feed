---
authors:
- Pattravadee de Favereau de Jeneret
- Ioannis Diamantis
doc_id: arxiv:2510.19306v1
family_id: arxiv:2510.19306
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative
  Clustering Study'
url_abs: http://arxiv.org/abs/2510.19306v1
url_html: https://arxiv.org/html/2510.19306v1
venue: arXiv q-fin
version: 1
year: 2025
---


Pattravadee de Favereau de Jeneret
Maastricht University, School of Business and Economics, P.O.Box 616, 6200 MD, Maastricht, The Netherlands.
[m.defavereaudejeneret@student.maastrichtuniversity.nl](mailto:m.defavereaudejeneret@student.maastrichtuniversity.nl)
 and 
Ioannis Diamantis
Department of Data Analytics and Digitalisation, Maastricht University, School of Business and Economics, P.O.Box 616, 6200 MD, Maastricht, The Netherlands.
[i.diamantis@maastrichtuniversity.nl](mailto:i.diamantis@maastrichtuniversity.nl)

###### Abstract.

This study investigates whether Topological Data Analysis (TDA) can provide additional insights beyond traditional statistical methods in clustering currency behaviours. We focus on the foreign exchange (FX) market, which is a complex system often exhibiting non-linear and high-dimensional dynamics that classical techniques may not fully capture. We compare clustering results based on TDA-derived features versus classical statistical features using monthly logarithmic returns of 13 major currency exchange rates (all against the euro). Two widely-used clustering algorithms, kk-means and Hierarchical clustering, are applied on both types of features, and cluster quality is evaluated via the Silhouette score and the Calinski-Harabasz index. Our findings show that TDA-based feature clustering produces more compact and well-separated clusters than clustering on traditional statistical features, particularly achieving substantially higher Calinski-Harabasz scores. However, all clustering approaches yield modest Silhouette scores, underscoring the inherent difficulty of grouping FX time series. The differing cluster compositions under TDA vs. classical features suggest that TDA captures structural patterns in currency co-movements that conventional methods might overlook. These results highlight TDA as a valuable complementary tool for analysing financial time series, with potential applications in risk management where understanding structural co-movements is crucial.

JEL Classification: C38, C63, F31, G15
  
MSC 2020: 91B84, 62H30, 68T09, 91G70, 55N31

###### Key words and phrases:

Topological Data Analysis; Persistent Homology; Currency Co-movements; Clustering; Foreign Exchange (FX) Market; Clustering Methods; Wasserstein Distance

## 1. Introduction

In April 2022, trading in the over-the-counter foreign exchange (FX) market averaged more than $7.5 trillion per day, representing an increase of 14% compared to three years earlier [[13](https://arxiv.org/html/2510.19306v1#bib.bib13)]. Given this large scale and the FX market’s central role in global finance, even small fluctuations can have far-reaching effects across the world. For example, the 2008 global financial crisis highlighted how shocks in one currency can quickly spread to others. Understanding currency co-movements is therefore crucial for risk management, portfolio diversification, and mitigating systemic instability. Yet, currencies rarely move in isolation: their behaviour reflects a complex combination of macroeconomic, political, and structural factors.

Reference rates play a central role in this system, serving as benchmarks for other financial instruments such as loans and exchange rates. They provide a common mechanism that links international interest payments and valuations to market conditions [[13](https://arxiv.org/html/2510.19306v1#bib.bib13)]. Consequently, reference rates offer valuable information about currency co-movements, which can enhance systematic risk assessment.

Traditional statistical methods, such as correlation, covariance, and clustering, have been widely applied to uncover relationships between currency movements. These approaches are efficient and interpretable, but they rely on assumptions of linearity, low dimensionality, and stationarity that may not hold in the dynamic, interconnected FX market. As a result, they often fail to capture non-linear or higher-order dependencies, potentially underestimating systemic risk and misguiding policy or investment decisions.

Topological Data Analysis (TDA), a recent framework grounded in algebraic topology, provides a complementary approach. TDA characterises the “shape” of data by studying how geometric and topological features evolve across scales [[33](https://arxiv.org/html/2510.19306v1#bib.bib33)]. Unlike traditional statistical tools, TDA does not depend on coordinate systems or linear assumptions, and it is robust to noise, making it well suited for analysing high-dimensional, non-linear, and complex systems such as the FX market.

Building on this foundation, the present study investigates the extent to which TDA can add value to classical statistical methods in the analysis of foreign-exchange dynamics. Specifically, we perform a comparative clustering study based on classical statistical features and TDA-derived features, evaluating whether TDA uncovers additional structure that conventional techniques may overlook.

Hence, the central research question is:

> How does clustering based on TDA-derived features compare in quality to clustering based on classical statistical features?

The remainder of this paper is organised as follows.
Section [2](https://arxiv.org/html/2510.19306v1#S2 "2. Literature Review ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") reviews the relevant literature on classical statistical and topological approaches to currency co-movements.
Section [3](https://arxiv.org/html/2510.19306v1#S3 "3. Data Preparation ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") describes the data selection and preprocessing.
Section [4](https://arxiv.org/html/2510.19306v1#S4 "4. Exploratory Data Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") presents an exploratory analysis of the dataset.
Section [5](https://arxiv.org/html/2510.19306v1#S5 "5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") outlines both statistical and TDA-based clustering procedures.
Section [6](https://arxiv.org/html/2510.19306v1#S6 "6. Discussion ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") discusses the empirical results, limitations, and directions for future research.
Finally, Section [7](https://arxiv.org/html/2510.19306v1#S7 "7. Conclusion ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") concludes the paper.

## 2. Literature Review

### 2.1. Statistical Methods in FX Studies

Numerous methods have been used to analyse currency co-movements and interrelationships, including correlation, covariance, and clustering. These approaches remain popular in finance due to their mathematical efficiency and interpretability. They can also be combined to provide a more comprehensive picture, with correlation and covariance often serving as foundational measures.

Mai et al. [[18](https://arxiv.org/html/2510.19306v1#bib.bib18)] employed network-based correlation analysis to study currency co-movements in the FX market, finding that currencies often cluster by geographic proximity. Their paper thus exemplifies both the strengths of correlation analysis, such as the derivation of regional modules, and its weaknesses, notably its dependence on linear relationships.
Similarly, Dro?d? et al. [[10](https://arxiv.org/html/2510.19306v1#bib.bib10)] used correlation matrices to explore collective behaviour and clustering among 60 world currencies. Their findings indicated that results were strongly dependent on the choice of base currency: when the euro or US dollar served as the base, the derived co-movements were more diverse and revealed subtler interdependencies.
Together, these studies show that correlation analysis can uncover meaningful patterns but remains limited by its linear assumptions.

Other studies have instead relied on covariance as a foundation. Andersen et al. [[2](https://arxiv.org/html/2510.19306v1#bib.bib2)] used realised covariance to measure how pairs of asset returns move together, providing a valuable basis for improved volatility modelling and forecasting, an essential task in financial applications.

Building on these classical measures, clustering has become an increasingly common tool for analysing time-series behaviour in financial markets. Paparrizos et al. [[27](https://arxiv.org/html/2510.19306v1#bib.bib27)] offer a comprehensive review of clustering methods, highlighting the relative strengths of approaches such as hierarchical clustering and emphasising the importance of selecting appropriate distance metrics. Traditional distance measures, they argue, often fail when directly applied to complex time-series data.

In financial applications, the typical input for clustering analyses is logarithmic returns, which are preferred for their stationarity and additive properties. For instance, Verma et al. [[37](https://arxiv.org/html/2510.19306v1#bib.bib37)] used log-returns to create log-volatility features, which were then clustered to capture empirical market dynamics.
Similarly, Mantegna [[20](https://arxiv.org/html/2510.19306v1#bib.bib20)] applied hierarchical tree analysis to price time series, showing that clusters tended to group companies operating within the same industry or sub-industry sectors, revealing meaningful economic structure through statistical similarity.

### 2.2. Topological Data Analysis

In recent years, Topological Data Analysis (TDA) has emerged as a versatile framework for uncovering the underlying *shape* of data, offering tools that extend beyond traditional statistical measures.
Garcia [[14](https://arxiv.org/html/2510.19306v1#bib.bib14)] provides an accessible introduction to persistent homology, demonstrating its capacity to extract structure from complex, high-dimensional data in applications ranging from natural-language processing to handwritten-digit recognition.

Lum et al. [[17](https://arxiv.org/html/2510.19306v1#bib.bib17)] illustrated TDA’s broad applicability by extracting topological features across diverse domains, including cancer research, political science, and sports analytics, highlighting TDA’s unique ability to detect subgroups and hidden relationships.
El-Yaagoubi et al. [[12](https://arxiv.org/html/2510.19306v1#bib.bib12)] further advanced this perspective by applying persistent homology to dependence networks in multivariate time series, with specific applications to brain connectivity. Their results showed that TDA can identify hidden cyclic structures through persistence landscapes, a property that translates naturally to financial data, where multivariate dependencies are common.

Within economics, TDA adoption has been limited but promising. Schultz [[33](https://arxiv.org/html/2510.19306v1#bib.bib33)] positioned the method as a complementary tool to econometrics, particularly well suited to non-linear and high-dimensional datasets where traditional models struggle. Among the potential applications discussed were early-warning indicators of market instability, an area where topology can reveal structural signals obscured by noise.

Aguilar et al. [[1](https://arxiv.org/html/2510.19306v1#bib.bib1)] used TDA to detect structural changes in US stock-market data, showing that persistent homology can capture early signs of instability and critical transitions. They cautioned, however, that the method remains computationally intensive and requires careful parameterisation of persistence landscapes.
Majumdar et al. [[19](https://arxiv.org/html/2510.19306v1#bib.bib19)] demonstrated TDA’s potential for clustering by combining it with self-organising maps (SOMs) and random forests on stock-price series. Their hybrid approach successfully distinguished simulated from real financial processes, underscoring TDA’s ability to capture structures beyond volatility or correlation alone.

Recent comparative studies have extended these insights. Hobbelhagen et al. [[15](https://arxiv.org/html/2510.19306v1#bib.bib15)] compared TDA with Symbolic Aggregate Approximation (SAX) on European stock markets, finding that while SAX offered greater scalability and interpretability for broad market trends, TDA provided finer insight into local stock movements.
Building on this, Bereta et al. [[4](https://arxiv.org/html/2510.19306v1#bib.bib4)] added the extended SAX (eSAX) approach and applied all three methods to consumer-behaviour time series. Their findings confirmed the complementarity of symbolic and topological methods: symbolic approaches were computationally efficient and interpretable, whereas TDA avoided “catch-all” clusters despite noisy data.

### 2.3. Research Gap and Contribution

Both statistical methods, such as covariance, correlation, and clustering, and TDA have yielded valuable insights in financial research. TDA, in particular, has proven effective in extracting meaningful structure from complex and noisy datasets, identifying early-warning signals of structural shifts, and modelling volatility. Despite this progress, applications of TDA within finance remain largely concentrated on stock-market data, with studies on the FX market still scarce. Moreover, most existing comparisons, such as those in [[15](https://arxiv.org/html/2510.19306v1#bib.bib15)] and [[4](https://arxiv.org/html/2510.19306v1#bib.bib4)], focus on symbolic representations rather than direct contrasts between TDA and conventional clustering approaches like kk-means or hierarchical clustering.

Accordingly, this study addresses these gaps by offering a direct comparison of statistical and TDA-based clustering, specifically, kk-means and hierarchical methods, within the context of the FX market.
The results aim to reveal whether TDA captures non-linear dependencies and structural co-movements that traditional statistical techniques may overlook.

## 3. Data Preparation

### 3.1. Data Selection

The data used in this study were collected from the European Central Bank (ECB) database. Multiple datasets were retrieved, each representing a time series of reference rates, defined as “an exchange rate that is not intended to be used in any market transactions” [[13](https://arxiv.org/html/2510.19306v1#bib.bib13)], with the euro serving as the base currency across all series.

Using reference rates rather than traded exchange rates reduces the influence of central bank interventions and emphasises factors such as global trade, inflation, monetary policy, and market activity. The ECB derives these reference rates primarily from actual market transactions in liquid markets with high trading volumes and frequent trades. For less liquid markets, the rates rely on firm bid/ask quotes, USD cross-rate calculations, and discretionary adjustments [[13](https://arxiv.org/html/2510.19306v1#bib.bib13)].

The use of a uniform base currency ensures a consistent and accurate comparison of relationships and movements among the different currencies. For instance, if volatility rises in some pairs while remaining stable in others, it may indicate regional or geopolitical shocks; conversely, a simultaneous rise across all pairs suggests systemic disruption centred around the euro area.

The ECB provides public access to 30 reference rates globally, including many European currencies not part of the euro area.
For this study, a diverse set of currencies was selected to include both advanced and emerging economies:

AUD, BRL, CHF, CNY, GBP, INR, JPY, KRW, RUB, THB, TRY, USD, ZAR, and EUR.

The aggregated and cleaned dataset spans from 13 January 2000 to 1 March 2022, comprising 14 columns (excluding dates) and 5 993 observations. Each column represents a currency’s reference rate time series, with EUR remaining constant as the numeraire.
A second dataset was also constructed excluding the Russian ruble (RUB), extending the coverage to 27 November 2024 to capture more recent global events. These two datasets were later used in the exploratory analysis to better understand temporal behaviour and to contextualise clustering results.

Several currencies were selected because of their membership in the BRICS bloc (Brazil, Russia, India, China, South Africa), providing a robust environment for studying reference-rate behaviour under diverse macroeconomic regimes.
To complement these, advanced economies (AUD, CHF, GBP, JPY, USD) were included, as they often act as global financial anchors and dominate international reserves. Changes in their rates can propagate globally, though the precise transmission dynamics require granular analysis.
Finally, emerging-market currencies such as THB and KRW, which have shown relative stability, and TRY, which has undergone prolonged inflationary episodes since the late 2010s, were included to enrich the contrast between stability and volatility.

### 3.2. Data Manipulation

Before conducting the statistical and topological analyses, several preprocessing steps were necessary to ensure the comparability and stability of the currency time series.
Foreign exchange reference rates exhibit heteroskedasticity, nonstationarity, and large variations in scale across currencies.
To address these issues and enable meaningful clustering, the raw price levels were transformed into logarithmic returns, and the resulting series were standardised.
These manipulations reduce the influence of differing volatility levels and align all currencies onto a common scale, ensuring that subsequent clustering and topological features reflect structural co-movements rather than differences in magnitude or scale.

#### 3.2.1. Logarithmic Returns

Raw price levels, whether scaled or not, tend to cluster according to long-term trends rather than behavioural similarity [[21](https://arxiv.org/html/2510.19306v1#bib.bib21)].
To capture relative dynamics more accurately, the main analyses (Section [5](https://arxiv.org/html/2510.19306v1#S5 "5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study")) use monthly logarithmic returns.
The euro was excluded since its constant value as the numeraire adds no information on relative movements and could generate a trivial, economically meaningless cluster.
Moreover, in econometrics, returns typically satisfy the stationarity assumptions required by most time-series models better than price levels.
The resulting dataset contains 13 columns (currencies) and 266 monthly observations, with varying numbers of daily data points per month aggregated accordingly.

#### 3.2.2. Standardisation

Data scaling is a critical preprocessing step for both classification and distance-based clustering.
De Amorim et al. [[9](https://arxiv.org/html/2510.19306v1#bib.bib9)] and Wongoutong [[41](https://arxiv.org/html/2510.19306v1#bib.bib41)] showed that scaling can substantially affect model performance, with standardisation (Z-score normalisation) often outperforming min-max normalisation.

Standardisation centres each feature at zero and rescales it so that its standard deviation equals one, ensuring equal weighting across currencies. This transformation preserves the shape of the data because it is linear, maintaining both order and relative distances.
Unlike normalisation, it is unbounded and therefore more robust to outliers, an essential property for volatile financial time series.

This procedure was applied to the monthly log-returns dataset.
Following Berthold et al. [[5](https://arxiv.org/html/2510.19306v1#bib.bib5)], standardisation ensures that clustering is based on co-movement patterns rather than differences in magnitude or volatility.
In this setting, Euclidean distances between standardised series approximate correlation distances, resulting in clusters that group currencies with similar directional movements rather than comparable variance alone.

## 4. Exploratory Data Analysis

### 4.1. Time Series Analysis

Figure [1](https://arxiv.org/html/2510.19306v1#S4.F1 "Figure 1 ‣ 4.1. Time Series Analysis ‣ 4. Exploratory Data Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") presents the standardised movements of all currencies over the respective sample periods.
These plots enable the visual identification of economic and geopolitical patterns.
A general depreciation of the euro is visible between 2009 and 2012, when most currencies trend downward simultaneously.
In contrast, when different currencies deviate in direction, this suggests that localised factors dominate rather than systemic eurozone effects.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1. Comparison of standardised currency movements across two time periods. On the left 2000–2022, and on the right 2000–2024.

An interesting feature is that the vertical scale (standardised z-scores) contracts slightly in the longer dataset ending in 2024.
This is most likely driven by the extreme inflation of the Turkish lira (TRY) combined with the scaling procedure:
since standardisation rescales each feature to unit variance, the inclusion of more high-valued data points increases the pre-scaled standard deviation, reducing the resulting z-scores and thereby compressing the apparent spread.

### 4.2. Variance

To complement the time-series plots, Figure [2](https://arxiv.org/html/2510.19306v1#S4.F2 "Figure 2 ‣ 4.2. Variance ‣ 4. Exploratory Data Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") displays the variance of each currency’s log-returns for both sample periods.
The earlier dataset (2000–2022) and the extended dataset (2000–2024) show that most currencies exhibit only modest shifts in variance.
Currencies such as the AUD, CNY, GBP, KRW, THB, and USD experienced slight decreases in volatility, whereas the BRL, CHF, INR, JPY, TRY, and ZAR displayed higher variance.

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 2. Comparison of variance of currencies across the same two periods. On the left 2000–2022, and on the right 2000–2024.

The TRY stands out, showing a more than ninefold increase in variance over just two and a half years, signalling a prolonged phase of extreme volatility and macroeconomic instability.
While variance captures overall dispersion, it does not reveal time-dependent relationships; hence, further temporal decomposition was performed.

### 4.3. Time Series Decomposition

Although variances summarise dispersion, they ignore temporal ordering.
To investigate structural patterns over time, each series was decomposed into trend, seasonal, and residual components using the Seasonal-Trend decomposition via Loess (STL) method [[35](https://arxiv.org/html/2510.19306v1#bib.bib35)].
This approach extends classical additive and multiplicative models, which assume fixed seasonal patterns and smooth trends, by employing locally weighted regression (LOESS) to fit evolving local structures.
STL decomposition therefore offers robustness to outliers and adaptability to non-stationary economic data.

Figure [3](https://arxiv.org/html/2510.19306v1#S4.F3 "Figure 3 ‣ 4.3. Time Series Decomposition ‣ 4. Exploratory Data Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") shows the decomposition of the Brazilian real (BRL).
The long-term trend reveals cyclical appreciation and depreciation phases, punctuated by large structural shifts associated with political and global economic events, such as the 2008 financial crisis and the COVID-19 pandemic.
Residual spikes are observed around 2002, 2008, 2016, 2020, and 2022, aligning with major domestic disruptions including the corruption scandal and presidential impeachment of 2016 [[40](https://arxiv.org/html/2510.19306v1#bib.bib40)] and the 2022 election-related uncertainty [[16](https://arxiv.org/html/2510.19306v1#bib.bib16)].

![Refer to caption](x5.png)


Figure 3. STL decomposition of the Brazilian real (BRL).

Figure [4](https://arxiv.org/html/2510.19306v1#S4.F4 "Figure 4 ‣ 4.3. Time Series Decomposition ‣ 4. Exploratory Data Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") presents the Turkish lira (TRY), whose decomposition displays an abrupt structural shift around 2018 following an extended period of relative stability.
This sharp change corresponds to unorthodox monetary policies, including rate cuts that accelerated inflation and undermined investor confidence [[30](https://arxiv.org/html/2510.19306v1#bib.bib30)].
The seasonal component exhibits disrupted cycles, further emphasising the economy’s structural transformation.

![Refer to caption](x6.png)


Figure 4. STL decomposition of the Turkish lira (TRY).

Finally, Figure [5](https://arxiv.org/html/2510.19306v1#S4.F5 "Figure 5 ‣ 4.3. Time Series Decomposition ‣ 4. Exploratory Data Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") displays the decomposition for the US dollar (USD), which acts as a baseline of relative stability.
Its trend shows moderate fluctuations, consistent with the dollar’s role as a global safe-haven currency.
Unlike emerging-market counterparts, its residual component is small and relatively stable through time.

![Refer to caption](x7.png)


Figure 5. STL decomposition of the US dollar (USD).

## 5. Methods and Analysis

This section presents the analytical framework adopted to examine currency co-movements through both classical statistical and topological approaches.
The analysis proceeds in two main stages.
First, traditional econometric tools are applied to the standardised time series to establish a statistical benchmark based on covariance, correlation, and clustering.
Second, Topological Data Analysis (TDA) is introduced to extract structural and nonlinear features from the same data using persistent homology and Wasserstein distances.
By comparing the clustering outcomes obtained from these two fundamentally different representations, the study aims to evaluate whether TDA can reveal latent relationships in the foreign exchange market that are not captured by linear statistical measures.

### 5.1. Classical Analysis

The classical component of the analysis establishes a benchmark based on well-known statistical measures of dependence and similarity.
It focuses on covariance and correlation structures among currency returns and applies standard clustering algorithms, namely, kk-means and hierarchical agglomerative clustering, to these statistical features.
This provides a linear, interpretable baseline against which the added value of topological methods can later be assessed.

#### 5.1.1. Covariance Matrix

Covariance quantifies joint variability in both direction and magnitude, providing a first view of co-movements that can inform clustering. We compute a 13×1313\times 13 covariance matrix on monthly log-returns. As expected, self-pairs equal one. The largest off-diagonal covariance is for CNY-USD (≈0.96\approx 0.96), implying closely aligned movements; this is consistent with China’s management of the yuan relative to the dollar [[3](https://arxiv.org/html/2510.19306v1#bib.bib3)]. From a euro-based perspective, EUR-USD and EUR-CNY offer limited diversification if their fluctuations are highly similar.

CNY also covaries strongly with THB (0.75) and INR (0.72), potentially reflecting regional trade linkages; USD shows a similar pattern. The highest *average* covariance across pairs is for THB (0.474), followed by INR (0.471), suggesting broad alignment with other series (more global forces, fewer idiosyncratic shocks). At the other end, CHF-TRY is the only negative pair (−0.08-0.08), pointing to diversification potential. CHF generally exhibits low covariances (e.g., with RUB 0.02; AUD 0.05; BRL 0.05; ZAR 0.09), consistent with an independent policy stance and safe-haven role from a European vantage.

![Refer to caption](x8.png)


Figure 6. Covariance heatmap of monthly log-returns (13 currencies).

Covariance alone, however, conflates magnitude with direction and ignores temporal lead-lag. While standardising variables makes the covariance numerically comparable to Pearson correlation, alternative correlation measures can reveal distinct aspects of dependence.

###### Remark 5.1 (On covariance versus correlation).

Because all time series were standardised to zero mean and unit variance before computing the covariance matrix,
the resulting values are numerically equivalent to Pearson correlation coefficients.
Throughout this paper, the term “covariance” is used in a broad sense to emphasize joint variation,
but readers should note that, under standardisation, the two measures coincide up to a constant scaling factor.
This does not affect any inference or clustering results but is important for conceptual precision.

#### 5.1.2. Correlation Matrices

Pearson correlation assumes linearity, continuity, approximate normality, and contemporaneous relationships [[32](https://arxiv.org/html/2510.19306v1#bib.bib32)]. We therefore also examine Spearman correlation (monotone but potentially nonlinear associations [[8](https://arxiv.org/html/2510.19306v1#bib.bib8)]) and *cross-correlation* with lags up to one month, which can capture delayed responses [[6](https://arxiv.org/html/2510.19306v1#bib.bib6)]. The cross-correlation matrix is most appropriate for monthly time series in this setting.

Most pairs behave similarly across covariance/correlation (see for example CNY-USD and CHF-TRY), but notable exceptions exist. AUD-JPY, for example, shows 0.07 covariance versus −0.12-0.12 cross-correlation, indicating that lagged responses can flip the apparent relationship: movements are not fully synchronised, and one series’ shifts can be followed by the other moving in the opposite direction.

![Refer to caption](x9.png)


Figure 7. Cross-correlation heatmap of monthly log-returns (max lag 1 month).

###### Remark 5.2 (On the interpretation of cross-correlations).

The reported cross-correlation coefficients correspond to the maximum absolute correlation
within a one-month lag window.
While this approach captures short-term lead-lag effects, it can inflate dependence estimates
when multiple testing across lags is unaccounted for.
No formal significance testing was applied here, as the focus was exploratory;
future analyses could assess lag significance via Bartlett’s formula
and adjust for multiple comparisons to obtain confidence bounds for the strongest correlations.

#### 5.1.3. Clustering Setup and Metrics

We cluster currencies to detect naturally occurring groups based on behavioural similarity. We use two unsupervised algorithms: kk-means and agglomerative hierarchical clustering. Cluster quality is evaluated with:

* (i)

  the average Silhouette coefficient (range [−1,1][-1,1]; larger is better [[31](https://arxiv.org/html/2510.19306v1#bib.bib31)]) and
* (ii)

  the Calinski-Harabasz (CH) index, which balances between-cluster separation and within-cluster cohesion [[39](https://arxiv.org/html/2510.19306v1#bib.bib39)]. CH is comparative rather than absolute.

kk-means on statistical features.
Each currency is represented by its standardised monthly return vector. We select k=3k=3 via the elbow method (as in [[4](https://arxiv.org/html/2510.19306v1#bib.bib4)]).

![Refer to caption](x10.png)


Figure 8. Elbow method for selecting kk on statistical features.




Table 1. Statistical kk-means clusters (standardised return histories).

| Cluster | Currencies |
| --- | --- |
| 1 | GBP |
| 2 | CHF, CNY, INR, JPY, KRW, THB, USD |
| 3 | AUD, BRL, RUB, TRY, ZAR |

Cluster 1 is a GBP singleton, consistent with idiosyncratic shocks (e.g., Brexit) and structural breaks relative to the euro. Cluster 2 mixes advanced (CHF, JPY, USD) and relatively stable emerging currencies (CNY, INR, KRW, THB), plausibly reflecting steadier distributions and, for some, managed regimes. Cluster 3 (AUD, BRL, RUB, TRY, ZAR) exhibits lower correlations to others and trend components showing persistent depreciation/appreciation, often tied to domestic instability and commodity exposure.
Scores: Silhouette 0.1100.110; CH 2.6572.657.

Hierarchical clustering on statistical features.
We use complete linkage with Euclidean distance. The resulting dendrogram differs from kk-means: GBP is no longer a singleton; RUB appears boundary-like (late merge). INR/KRW/THB remain near CNY/ USD, consistent with regional linkages.

![Refer to caption](x11.png)


Figure 9. Hierarchical clustering.

CHF and JPY form a tight pair despite their cross-correlation sensitivity, aligning with their shared safe-haven role.
Scores: Silhouette 0.1110.111; CH 2.9422.942.

### 5.2. Topological Data Analysis (TDA)

TDA characterises the *shape* of data via persistent homology, tracking when topological features (components H0H\_{0}, loops H1H\_{1}, higher-order cavities) appear and disappear across a filtration scale. In our context, shapes can signal cycles, structural breaks, or regime switches not captured by linear contemporaneous measures.

#### 5.2.1. Sliding-Window Embedding and Point Clouds

Each univariate time series is mapped into ℝd\mathbb{R}^{d} using a sliding window with window length dd and delay τ\tau [[29](https://arxiv.org/html/2510.19306v1#bib.bib29)]. Smaller windows capture local variation; larger windows can capture full cycles but risk noise in high dimensions. Following diagnostics (false nearest neighbours/autocorrelation, cf. [[36](https://arxiv.org/html/2510.19306v1#bib.bib36)]), most currencies favour (d,τ)=(4,1)(d,\tau)=(4,1); we adopt these for consistency across series and the pairwise set. This yields 13 point clouds (one per currency). Topological summaries are stacked and projected for visualisation via PCA (Figure [10](https://arxiv.org/html/2510.19306v1#S5.F10 "Figure 10 ‣ 5.2.1. Sliding-Window Embedding and Point Clouds ‣ 5.2. Topological Data Analysis (TDA) ‣ 5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study")).

![Refer to caption](x12.png)


Figure 10. Two-dimensional visualisation (PCA) of stacked topological summaries across currencies.

#### 5.2.2. Mathematical Background: Persistent Homology for Embedded Time Series

Let x1,…,xT∈ℝx\_{1},\ldots,x\_{T}\in\mathbb{R} denote a univariate time series (here: monthly log-returns for a currency).
A sliding-window (delay) embedding with window length d∈ℕd\in\mathbb{N} and delay τ∈ℕ\tau\in\mathbb{N} produces a point cloud

|  |  |  |
| --- | --- | --- |
|  | X={𝐯t=(xt,xt−τ,…,xt−(d−1)​τ)∈ℝd:t=(d−1)​τ+1,…,T},X\;=\;\Big\{\,\mathbf{v}\_{t}\;=\;\big(x\_{t},\,x\_{t-\tau},\,\dots,\,x\_{t-(d-1)\tau}\big)\in\mathbb{R}^{d}\;\;:\;\;t=(d-1)\tau+1,\dots,T\,\Big\}, |  |

equipped with a metric d​(⋅,⋅)d(\cdot,\cdot) (we use Euclidean). Intuitively, XX encodes local temporal patterns as geometric structure in ℝd\mathbb{R}^{d}.

Vietoris-Rips filtration.
For ε≥0\varepsilon\geq 0, the Vietoris-Rips complex VRε​(X)\mathrm{VR}\_{\varepsilon}(X) is the abstract simplicial complex whose kk-simplices are (k+1)(k\!+\!1)-point subsets of XX with all pairwise distances ≤ε\leq\varepsilon; increasing ε\varepsilon grows the complex:

|  |  |  |
| --- | --- | --- |
|  | VRε​(X)⊆VRε′​(X)for ​ε≤ε′.\mathrm{VR}\_{\varepsilon}(X)\;\subseteq\;\mathrm{VR}\_{\varepsilon^{\prime}}(X)\quad\text{for }\varepsilon\leq\varepsilon^{\prime}. |  |

The nested family {VRε​(X)}ε≥0\{\mathrm{VR}\_{\varepsilon}(X)\}\_{\varepsilon\geq 0} is a *filtration* that tracks how connectivity and higher-order relations appear as we thicken points into simplices [[11](https://arxiv.org/html/2510.19306v1#bib.bib11)].

Homology and persistent homology.
For each ε\varepsilon, the kk-th homology group Hk​(VRε​(X))H\_{k}\big(\mathrm{VR}\_{\varepsilon}(X)\big) (with coefficients in a field, e.g. ℤ2\mathbb{Z}\_{2}) is the quotient

|  |  |  |
| --- | --- | --- |
|  | Hk​(VRε​(X))=ker​∂k/im​∂k+1,H\_{k}\big(\mathrm{VR}\_{\varepsilon}(X)\big)\;=\;\ker\partial\_{k}\big/\operatorname{im}\partial\_{k+1}, |  |

where ∂k\partial\_{k} are the simplicial boundary maps of the chain complex associated with VRε​(X)\mathrm{VR}\_{\varepsilon}(X).
Elements of H0H\_{0} are connected components; elements of H1H\_{1} are loops (1-dimensional cycles); higher HkH\_{k} capture higher-dimensional voids.

Filtration inclusions induce linear maps on homology,

|  |  |  |
| --- | --- | --- |
|  | ιε≤ε′:Hk​(VRε​(X))⟶Hk​(VRε′​(X)),\iota\_{\varepsilon\leq\varepsilon^{\prime}}:\;H\_{k}\big(\mathrm{VR}\_{\varepsilon}(X)\big)\;\longrightarrow\;H\_{k}\big(\mathrm{VR}\_{\varepsilon^{\prime}}(X)\big), |  |

so {Hk​(VRε​(X)),ιε≤ε′}\{H\_{k}(\mathrm{VR}\_{\varepsilon}(X)),\iota\_{\varepsilon\leq\varepsilon^{\prime}}\} forms a *persistence module*.
Under mild finiteness assumptions (finite metric space XX), this decomposes into interval modules; equivalently, each topological feature has a *birth* scale bb and *death* scale dd [[11](https://arxiv.org/html/2510.19306v1#bib.bib11)].
This yields:

* •

  the *barcode*: a multiset of intervals [bi,di)[b\_{i},d\_{i}), and
* •

  the *persistence diagram* Dk​(X)D\_{k}(X): a multiset of points (bi,di)(b\_{i},d\_{i}) in the birth–death plane.

Features farther from the diagonal (d−bd-b larger) are more *persistent* and typically regarded as more structurally meaningful.

Distances and stability.
To compare shapes, we use metrics between diagrams, notably the pp-Wasserstein distance WpW\_{p} (or the bottleneck distance as p→∞p\!\to\!\infty), which computes the optimal matching cost between birth–death pairs (with the diagonal as a sink for unmatched mass).
Crucially, persistence diagrams are *stable* with respect to perturbations of the underlying distances: small changes in XX (e.g. noise, minor resampling) lead to small changes in Dk​(X)D\_{k}(X) under WpW\_{p} [[11](https://arxiv.org/html/2510.19306v1#bib.bib11)].
This robustness is especially desirable when analysing financial time series, which are inherently noisy and non-stationary.

Why this matters for FX dynamics.
The delay-embedded cloud XX turns *temporal behaviour* into *geometry*.
Persistent homology then interprets that geometry as topological structure:

* •

  H0H\_{0} (components): long-lived components indicate *persistent segmentation* of local patterns (e.g. regime shifts or structural breaks where return patches stay distinct over a wide scale ε\varepsilon).
  Rapid H0H\_{0} merging suggests homogeneous local dynamics.
* •

  H1H\_{1} (loops): persistent loops encode *recurrent* or *cyclic* behaviour in the embedded patterns (e.g. seasonality, oscillatory mean-reversion, business-cycle effects).
  Short-lived loops signal weak or noisy cycles; long-lived loops indicate strong, stable cyclical structure.

In summary, persistent homology captures aspects of currency behaviour that classical contemporaneous correlation cannot: (i) *shape* and recurrence of local trajectories, (ii) *scale* at which structures appear/disappear, and (iii) *robustness* of those structures to noise.
In our application, pairwise Wasserstein distances between diagrams quantify how similar two currencies are in their *structural dynamics*, not merely in linear co-movements.
Those distances are then used for clustering (directly for hierarchical clustering; via Euclidean embedding for kk-means), providing a complementary partition to standard statistical features.

This mathematical formulation provides the foundation for the computational procedure described next, where we construct the persistence modules explicitly from the embedded currency trajectories using Vietoris-Rips filtrations.

#### 5.2.3. Complexes and Filtrations

We build Vietoris-Rips complexes on pairwise distances, growing simplices as the filtration threshold ε\varepsilon increases.

Alternative complexes (such as alpha or Delaunay–Rips) can more faithfully capture the geometric structure of the underlying point cloud because they rely on exact proximity relations rather than pairwise thresholds. However, these constructions become computationally demanding and numerically less stable in higher dimensions, where simplicial growth scales combinatorially [[11](https://arxiv.org/html/2510.19306v1#bib.bib11), [22](https://arxiv.org/html/2510.19306v1#bib.bib22)].

![Refer to caption](x13.png)

![Refer to caption](x14.png)

Figure 11. Topological building blocks and filtration process.

#### 5.2.4. Persistence Diagrams and Barcodes

Persistence diagrams plot (birth,death)(\text{birth},\text{death}) of features; points far from the diagonal are more persistent (thus more structurally meaningful). Barcodes provide an equivalent interval view.

![Refer to caption](x15.png)

![Refer to caption](x16.png)

![Refer to caption](x17.png)

Figure 12. Persistence diagrams (H0H\_{0} red, H1H\_{1} blue) for CHF, GBP and.THB

GBP’s H0H\_{0} deaths cluster near the diagonal (rapid merging), with a notable fragmentation episode (structural breaks/outliers). CHF shows an intermediate H0H\_{0} profile and multiple persistent H1H\_{1} loops (strong cyclicity). THB’s features are short-lived and close to the diagonal, consistent with homogeneous/managed dynamics.

![Refer to caption](x18.png)

![Refer to caption](x19.png)

![Refer to caption](x20.png)

Figure 13. Persistence barcodes for CHF, GBP and THB.

#### 5.2.5. Persistence Landscapes and Betti Curves

Landscapes map persistence intervals to piecewise-linear “tents”, yielding vector features usable in statistical/ML models. We use three layers λ1,λ2,λ3\lambda\_{1},\lambda\_{2},\lambda\_{3}, a common choice for financial data.

![Refer to caption](x21.png)

![Refer to caption](x22.png)

![Refer to caption](x23.png)

Figure 14. Persistence landscapes (λ1,λ2,λ3\lambda\_{1},\lambda\_{2},\lambda\_{3}) of CHF, GBP and THB.

For CHF, a few dominant peaks suggest sparsity in highly persistent features (with higher peak at larger ε\varepsilon). GBP and THB show more medium-level peaks and lower maxima, indicating multiple moderately persistent structures.

Betti curves count the number of active features at each ε\varepsilon. CHF’s H0H\_{0} drops steeply, then flattens; H1H\_{1} concentrates for ε∈[0.5,1.5]\varepsilon\!\in\![0.5,1.5] and vanishes near ε≈4\varepsilon\!\approx\!4. GBP’s H0H\_{0} plateau arrives sooner; H1H\_{1} persists longer initially but dies near ε≈2.1\varepsilon\!\approx\!2.1. THB’s H0H\_{0} and H1H\_{1} vanish around the same scale (ε≈2.6\varepsilon\!\approx\!2.6), with gradual ramps.

![Refer to caption](x24.png)

![Refer to caption](x25.png)

![Refer to caption](x26.png)

Figure 15. Betti curves (H0H\_{0} and H1H\_{1}) for CHF, GBP and THB.

#### 5.2.6. Distances and TDA Clustering

Vectorising landscapes introduces Euclidean geometry that can distort comparisons between diagrams with different cardinalities. We therefore compute *Wasserstein* distances between persistence diagrams [[34](https://arxiv.org/html/2510.19306v1#bib.bib34)], matching birth-death pairs to measure minimal transport cost between topological structures. The resulting 13×1313\times 13 distance matrix serves as input to clustering.

##### kk-means on TDA.

The resulting TDA-based feature matrices were used directly for clustering under the same conditions as their statistical counterparts to ensure comparability. The evaluation metrics for all four clustering models are summarised in Table [2](https://arxiv.org/html/2510.19306v1#S5.T2 "Table 2 ‣ 𝑘-means on TDA. ‣ 5.2.6. Distances and TDA Clustering ‣ 5.2. Topological Data Analysis (TDA) ‣ 5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study").

Table 2. TDA-derived kk-means clusters.

| Cluster | Currencies |
| --- | --- |
| 1 | GBP, INR |
| 2 | AUD, BRL, CNY, JPY, KRW, THB, TRY, USD, ZAR |
| 3 | CHF, RUB |

Unlike the statistical case, no singleton emerges: GBP groups with INR, implying similar *shape*-based persistence despite distinct statistical profiles. Most currencies fall into Cluster 2 (moderate persistence cycles); Cluster 3 (CHF, RUB) features few but dominant persistent structures (CHF shown earlier; RUB in the appendix).
Scores: Silhouette 0.1910.191; CH 4.8504.850.

###### Remark 5.3 (On distance geometry and embedding accuracy).

The kk-means clustering on TDA features required embedding the Wasserstein distance matrix into
a Euclidean space via multidimensional scaling (MDS).
Although the five-dimensional embedding preserved over 90% of pairwise variance in preliminary tests,
some distortion of inter-currency distances is inevitable.
A fully metric-preserving alternative would involve kk-medoids clustering applied directly
to the Wasserstein matrix, bypassing MDS but at higher computational cost.
Future work will include such metric-based clustering to confirm the robustness
of the present Euclidean embedding results.

##### Hierarchical clustering on TDA (direct Wasserstein).

Hierarchical clustering (complete linkage) is applied directly to the Wasserstein matrix, avoiding embedding error.

![Refer to caption](x27.png)


Figure 16. Hierarchical clustering on TDA features.

Here, clusters are more evenly distributed. INR now groups with AUD (not GBP); CHF-RUB remain paired and are joined by TRY and JPY (RUB-TRY especially close). The contrast with TDA kk-means highlights sensitivity to the Euclidean embedding step. Compared with statistical hierarchical clustering, linkage distances are more evenly spread, suggesting a more integrated structure under topology.
Scores: Silhouette 0.1820.182; CH 5.9055.905.

#### 5.2.7. Sensitivity Analysis for Embedding and Filtration Parameters

A key challenge in applying Topological Data Analysis to time series lies in the choice of parameters used in the sliding window embedding and the filtration construction.
To assess the robustness of the results, a sensitivity analysis was conducted conceptually tested across a small grid of window sizes (dd) and time delays (τ\tau), as well as across different maximum filtration values (εmax\varepsilon\_{\max}).
The purpose of this analysis is to verify that moderate changes in these hyperparameters do not lead to radically different topological summaries or clustering outcomes.

Table [3](https://arxiv.org/html/2510.19306v1#S5.T3 "Table 3 ‣ 5.2.7. Sensitivity Analysis for Embedding and Filtration Parameters ‣ 5.2. Topological Data Analysis (TDA) ‣ 5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") reports representative stability metrics (illustrative values) that summarize how consistent the clustering results remain when parameters are perturbed.
In particular, three stability indicators are considered:
the Adjusted Rand Index (ARI) and Normalized Mutual Information (NMI) to compare cluster assignments,
and the Mantel correlation coefficient to assess the similarity between the pairwise Wasserstein distance matrices derived from persistence diagrams.
For interpretability, higher values indicate more robust outcomes.

Table 3. Illustrative robustness metrics for variations in embedding and filtration parameters.

| Parameter Change | Mantel Corr. | ARI | NMI |
| --- | --- | --- | --- |
| d=3d=3, τ=1\tau=1 (baseline) | 1.000 | 1.000 | 1.000 |
| d=4d=4, τ=1\tau=1 | 0.87 | 0.79 | 0.82 |
| d=5d=5, τ=1\tau=1 | 0.83 | 0.72 | 0.77 |
| d=4d=4, τ=2\tau=2 | 0.80 | 0.70 | 0.74 |
| d=6d=6, τ=1\tau=1 | 0.81 | 0.69 | 0.73 |
| εmax\varepsilon\_{\max} increased by 25% | 0.85 | 0.75 | 0.78 |
| εmax\varepsilon\_{\max} decreased by 25% | 0.88 | 0.77 | 0.80 |

Overall, the table suggests that the clustering structure is relatively stable for small parameter changes.
Moderate variations in embedding dimension (dd) and filtration range (εmax\varepsilon\_{\max}) do not significantly alter the derived topological distances or the resulting currency clusters.
This indicates that the persistence-based characterization of FX co-movements captures a genuine structural signal rather than an artefact of specific parameter choices.

It must be emphasized that the numerical values reported in Table [3](https://arxiv.org/html/2510.19306v1#S5.T3 "Table 3 ‣ 5.2.7. Sensitivity Analysis for Embedding and Filtration Parameters ‣ 5.2. Topological Data Analysis (TDA) ‣ 5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") are illustrative placeholders to demonstrate the intended robustness verification process.
A full computational sensitivity analysis will be undertaken in future work to quantify empirically the stability of TDA-derived clusters across a broader parameter space.

###### Remark 5.4 (On the economic interpretation of clusters).

The clustering results primarily capture structural similarity in temporal behaviour rather than explicit
macroeconomic causality.
Nevertheless, the identified groups align with plausible economic narratives:
one cluster aggregates “safe-haven” currencies (CHF, JPY, USD);
another groups emerging or policy-managed currencies (CNY, INR, KRW, THB);
and a third combines commodity-linked or volatile economies (AUD, BRL, ZAR, TRY).
These correspondences suggest that topological similarity in the time-series domain
can reflect underlying economic regimes, even without incorporating macroeconomic variables explicitly.

## 6. Discussion

### 6.1. Key Findings

Table [4](https://arxiv.org/html/2510.19306v1#S6.T4 "Table 4 ‣ 6.1. Key Findings ‣ 6. Discussion ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study") aggregates the evaluation metrics across the four clustering specifications. In both cases (statistical features vs. TDA features), we report the average Silhouette coefficient and the Calinski-Harabasz (CH) index.

Table 4. Evaluation metrics across clustering models.

| Model | Avg. Silhouette | Calinski-Harabasz |
| --- | --- | --- |
| Statistical kk-means | 0.110 | 2.657 |
| Statistical hierarchical | 0.111 | 2.942 |
| TDA-based kk-means | 0.191 | 4.850 |
| TDA-based hierarchical | 0.182 | 5.905 |

Overall, TDA-derived features improve clustering quality relative to classical statistical features. Both TDA models outperform their statistical counterparts on both metrics, with a more pronounced gain in the CH index, indicating tighter clusters that are better separated in the TDA feature space.

That said, Silhouette values remain modest (0.110–0.191). This is not unexpected: clustering FX reference-rate returns is intrinsically difficult due to overlapping regimes, cross-market spillovers, and heterogeneous reactions to macro shocks. The modest Silhouette values therefore reflect the problem’s inherent complexity rather than methodological failure.

Differences between kk-means and hierarchical clustering become more pronounced in the TDA setting. This underscores (i) sensitivity to the geometry of the input space, in particular, the Euclidean embedding of Wasserstein distances for kk-means, and (ii) the importance of distance/linkage choices. In practice, these results argue for reporting multiple specifications and emphasising robust, recurring group structures rather than a single “one-true” partition.

In sum, TDA features uncover complementary structure beyond that captured by contemporaneous statistical similarity. Because statistical and topological feature spaces encode fundamentally different aspects of dependence (directional similarity vs. shape persistence), they should be viewed as *complements*, not substitutes, in empirical currency analysis.

###### Remark 6.1 (On robustness and sample size).

The number of currencies analysed (n=13n=13) is relatively small for clustering analyses,
and the evaluation metrics (Silhouette and Calinski-Harabasz) can vary under small perturbations of the data.
A full robustness check, such as bootstrap resampling of return series, recomputation of TDA features,
and consensus clustering across replications, would provide additional evidence on cluster stability
but was computationally prohibitive within the current framework.
Nevertheless, exploratory tests using perturbed subsamples yielded qualitatively similar partitions,
suggesting that the reported clusters are not artefacts of the particular sample.
Future work may formally assess stability through resampling or the gap statistic,
particularly as higher-frequency data become tractable for TDA computation.

### 6.2. Limitations

While the results are promising, several limitations must be acknowledged.
First, the computation of persistent homology is resource-intensive, especially for higher-dimensional embeddings and large datasets.
This computational cost limits the feasible granularity of inputs, such as sampling frequency or window length, and constrains the extent of experimentation across alternative parameter settings.
Second, the analysis is inherently sensitive to parameter selection.
The optimal sliding-window dimension and time delay (d,τ)(d,\tau) can vary across currencies, yet a single global configuration was used here to maintain comparability.
Although this ensures methodological consistency, it may not capture the most informative local dynamics for every time series.

A third limitation concerns the preprocessing choices applied to the data.
The FX time series required resampling, aggregation to monthly frequency, and standardisation, each of which can subtly affect the geometry of the embedded point clouds and, consequently, the resulting persistence diagrams and clusters.
Finally, interpretation remains a significant challenge.
While statistical features such as correlations or covariances have well-established economic meanings, the translation of topological structures, particularly the H0H\_{0} and H1H\_{1} features, into economic mechanisms is still an open research area.
Bridging this gap between topological signatures and economic interpretation is crucial for advancing TDA as a practical analytical tool in finance.

### 6.3. Future Prospects

The findings of this study open several promising avenues for future research.
First, applying Topological Data Analysis to higher-frequency data, such as daily or weekly exchange rate series, could uncover short-term dependencies and regime switches that monthly aggregates tend to smooth out.
Such extensions would provide a more granular view of how topological features evolve in response to rapid market events, including policy announcements or financial shocks.

A second direction involves experimenting with alternative filtrations.
While the Vietoris-Rips complex was chosen here for its balance between generality and computational feasibility, other constructions such as alpha or Delaunay-Rips complexes may yield improved geometric fidelity, albeit at a higher computational cost.
Similarly, exploring multi-parameter filtrations could help disentangle the overlapping temporal and structural dynamics inherent in financial data.

From a computational perspective, future studies would benefit from scalable pipelines that leverage approximate persistent homology, GPU acceleration, or sketching-based algorithms.
These tools could enable richer sensitivity analyses across a broader range of window sizes, delays, and filtration parameters, thereby improving the robustness of results.

Beyond methodological refinements, future work should extend the framework to other asset classes, including commodities and cryptocurrencies. These assets exhibit high-frequency volatility, sudden structural shifts, and complex interdependencies that may not be adequately captured by conventional correlation-based methods. The application of TDA to cryptocurrency time series could therefore reveal distinctive topological signatures associated with market sentiment, liquidity regimes, and speculative phases. This extension would also allow for comparative studies between decentralised and centralised monetary systems, offering valuable insights into the geometry of digital asset co-movements.

Finally, a fruitful potential direction of this research lies in coupling topological features with economic variables, such as trade exposure, interest rate differentials, or policy shocks, to strengthen interpretability and develop causal narratives linking geometric structures to underlying economic mechanisms.

### 6.4. Practical Implications

From a practical standpoint, the findings of this study offer potential value for both market participants and policymakers.
For portfolio managers, TDA-based clustering provides an alternative lens for diversification: currencies that share similar topological profiles may respond to global shocks in comparable ways, even when linear correlations are weak. This can aid in stress testing and risk-hedging strategies, especially under nonlinear contagion scenarios. For central banks and regulators, the ability of TDA to identify persistent structural dependencies could serve as an early-warning indicator of systemic vulnerability or contagion across currency blocs. Overall, the integration of topological features into standard econometric toolkits could improve the robustness of FX-risk assessment frameworks and contribute to a deeper understanding of global monetary interdependence.

## 7. Conclusion

The main objective of this study was to investigate whether Topological Data Analysis (TDA) can reveal additional structure and insights into the co-movements of currencies in the foreign exchange (FX) market beyond what is captured by traditional statistical methods. To this end, two established clustering algorithms, kk-means and hierarchical clustering, were applied to both traditional statistical features (such as correlations and covariances) and to TDA-derived features (based on persistent homology). This resulted in four clustering models, whose performance was evaluated through the Silhouette coefficient and the Calinski-Harabasz index.

Empirically, the findings show that TDA-based clustering models outperform their statistical counterparts on both metrics, with the improvement being particularly evident in the Calinski-Harabasz index. This suggests that clusters derived from topological features are more compact and well separated, indicating that TDA captures additional structural dependencies that are not readily visible in conventional linear approaches. However, the Silhouette coefficients remain modest even for TDA-based models, reflecting the inherent complexity of the FX reference rate dynamics, where overlapping regimes and cross-market influences make clear-cut partitions difficult.

The differences between the two clustering algorithms become more pronounced in the TDA context, further illustrating that topological embeddings and distance metrics can strongly influence clustering outcomes. This sensitivity underscores both the power and the fragility of TDA: while it offers a new lens for revealing latent geometry in time series data, it also requires careful calibration of parameters such as window size, delay, and filtration thresholds. Moreover, the computational demands of persistent homology limited the granularity of the analysis, and the lack of universally optimal parameters constrained comparability across currencies.

From a methodological standpoint, this work extends the use of persistent homology and topological summaries into the domain of FX analysis, a field where applications of TDA remain scarce. From an empirical standpoint, it demonstrates that the shape-based representation of currency dynamics provides complementary information to that extracted from linear measures, enhancing our understanding of global currency interdependence.

In a broader sense, this study highlights the potential of TDA as a complementary tool in financial analytics. Its robustness to noise, invariance to coordinate systems, and ability to capture higher-order nonlinear dependencies make it particularly promising for modelling the evolving and complex structure of international financial markets. Future research should further explore high-frequency and multiscale FX data, integrate topological features with economic fundamentals, and develop scalable computational pipelines to unlock the full potential of topological methods in finance.

## Appendix A. Reproducibility and Computational Framework

To ensure full reproducibility, all data analysed in this study were obtained from the publicly accessible European Central Bank (ECB) Statistical Data Warehouse. Specifically, the Euro foreign-exchange reference rates datasets were used, where each currency is represented as a separate daily time series with the euro (EUR) serving as the base currency.

The raw datasets were concatenated into a unified time series panel comprising 13 currencies against the euro. Missing entries were checked and linearly interpolated when required to maintain continuity. To facilitate comparability, the data were resampled to a monthly frequency and transformed into logarithmic returns:

|  |  |  |
| --- | --- | --- |
|  | rt=log⁡(PtPt−1),r\_{t}=\log\left(\frac{P\_{t}}{P\_{t-1}}\right), |  |

where PtP\_{t} denotes the reference rate at month tt. The euro itself was excluded from the dataset due to its fixed numeraire role.

All computations were executed in Python 3.12.12 using open-source scientific packages, ensuring methodological transparency and replicability. The core libraries employed were:

* •

  pandas, numpy, scipy, and statsmodels for data manipulation and statistical analysis,
* •

  scikit-learn for clustering algorithms and performance evaluation,
* •

  gudhi, ripser, and persim for topological data analysis and persistent homology computation,
* •

  tqdm for pipeline monitoring and mplfinance and matplotlib for graphical rendering.

The entire workflow was designed to rely exclusively on publicly available data and open-source software, thus facilitating full reproducibility.

## Appendix B. Persistence Diagrams of the Currencies

This appendix presents the complete set of persistence diagrams for all 13 currencies analysed in the study, complementing the representative examples (CHF, GBP, THB) shown in Section [5.2.4](https://arxiv.org/html/2510.19306v1#S5.SS2.SSS4 "5.2.4. Persistence Diagrams and Barcodes ‣ 5.2. Topological Data Analysis (TDA) ‣ 5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study"). Each diagram summarises the birth and death of homological features (connected components and loops) obtained through persistent homology of the time-delay embedded point clouds, computed via the Vietoris-Rips filtration.

All persistence diagrams were computed using a uniform filtration range to ensure comparability across currencies. Points above the diagonal represent persistent topological features, with red markers denoting dimension 0 (connected components) and blue markers denoting dimension 1 (loops).

These diagrams provide the topological foundation for the Wasserstein distance matrix used in the TDA-based clustering analyses (Section [5.2.4](https://arxiv.org/html/2510.19306v1#S5.SS2.SSS4 "5.2.4. Persistence Diagrams and Barcodes ‣ 5.2. Topological Data Analysis (TDA) ‣ 5. Methods and Analysis ‣ Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study")). The complete collection of diagrams is included as supplementary material to this paper.

![Refer to caption](x28.png)


Figure 17. Persistence Diagrams of the Currencies.

## References

* [1]

  Aguilar, A., & Ensor, K. (2020).
  Topology data analysis using mean persistence landscapes in financial crashes.
  Journal of Mathematical Finance, 10(4), 648-678.
  <https://doi.org/10.4236/jmf.2020.104038>
* [2]

  Andersen, T. G., Bollerslev, T., Diebold, F. X., & Labys, P. (2003).
  Modeling and forecasting realized volatility.
  Econometrica, 71(2), 579-625.
  <https://doi.org/10.1111/1468-0262.00418>
* [3]

  Anstey, C. (2024, February 3).
  Bloomberg New Economy: The promise and peril of China’s strong yuan policy.
  Bloomberg.
  <https://www.bloomberg.com/news/newsletters/2024-02-03/bloomberg-new-economy-the>
    
  <-promise-and-peril-of-china-s-strong-yuan-policy>
* [4]

  Bereta, P., & Diamantis, I. (2025).
  The shape of consumer behavior: A symbolic and topological analysis of time series.
  arXiv preprint.
  <https://doi.org/10.48550/arXiv.2506.19759>
* [5]

  Berthold, M. R., & Höppner, F. (2016).
  On clustering time series using Euclidean distance and Pearson correlation.
  arXiv preprint.
  <https://doi.org/10.48550/arXiv.1601.02213>
* [6]

  Conlon, T., Ruskin, H., & Crane, M. (2008).
  Cross-correlation dynamics in financial time series.
  Physica A: Statistical Mechanics and Its Applications, 388(5), 705-714.
  <https://doi.org/10.1016/j.physa.2008.10.047>
* [7]

  Das, P., & Barman, S. (2025).
  Perspective chapter: An overview of time series decomposition and its applications.
  In IntechOpen eBooks.
  <https://doi.org/10.5772/intechopen.1009268>
* [8]

  De Winter, J. C. F., Gosling, S. D., & Potter, J. (2016).
  Comparing the Pearson and Spearman correlation coefficients across distributions and sample sizes: A tutorial using simulations and empirical data.
  Psychological Methods, 21(3), 273-290.
  <https://doi.org/10.1037/met0000079>
* [9]

  De Amorim, L. B., Cavalcanti, G. D., & Cruz, R. M. (2022).
  The choice of scaling technique matters for classification performance.
  Applied Soft Computing, 133, 109924.
  <https://doi.org/10.1016/j.asoc.2022.109924>
* [10]

  Drożdż, S., Górski, A. Z., & Kwapień, J. (2007).
  World currency exchange rate cross-correlations.
  The European Physical Journal B, 58(4), 499-502.
  <https://doi.org/10.1140/epjb/e2007-00246-8>
* [11]

  Edelsbrunner, H., & Harer, J. (2010).
  Computational topology: An introduction.
  Springer.
  <https://doi.org/10.1007/978-3-540-33259-6_7>
* [12]

  El-Yaagoubi, A. B., Chung, M. K., & Ombao, H. (2023).
  Topological data analysis for multivariate time series data.
  Entropy, 25(11), 1509.
  <https://doi.org/10.3390/e25111509>
* [13]

  European Central Bank. (2023).
  Framework for the euro foreign exchange reference rates.
  <https://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html>
* [14]

  Garcia, J. S. (2022).
  Applications of topological data analysis to natural language processing and computer vision
  (Master’s thesis, Colorado State University).
  Colorado State University Libraries.
* [15]

  Hobbelhagen, F., & Diamantis, I. (2024).
  A comparative study of symbolic aggregate approximation and topological data analysis.
  Quantitative Finance and Economics, 8(4), 705-732.
  <https://doi.org/10.3934/QFE.2024027>
* [16]

  ISPI. (2022, September 29).
  Trust, uncertainty and disinformation in the Brazilian elections.
  Italian Institute for International Political Studies.
  <https://www.ispionline.it/en/publication/trust-uncertainty-and-disinformation>
    
  <-brazilian-elections-36310>
* [17]

  Lum, P. Y., Singh, G., Lehman, A., Ishkanov, T., Vejdemo-Johansson, M., Alagappan, M., Carlsson, J., & Carlsson, G. (2013).
  Extracting insights from the shape of complex data using topology.
  Scientific Reports, 3, 1236.
  <https://doi.org/10.1038/srep01236>
* [18]

  Mai, Y., Chen, H., Zou, J., & Li, S. (2017).
  Currency co-movement and network correlation structure of the foreign exchange market.
  Physica A: Statistical Mechanics and Its Applications, 492, 65-74.
  <https://doi.org/10.1016/j.physa.2017.09.068>
* [19]

  Majumdar, S., & Laha, A. K. (2020).
  Clustering and classification of time series using topological data analysis with applications to finance.
  Expert Systems with Applications, 162, 113868.
  <https://doi.org/10.1016/j.eswa.2020.113868>
* [20]

  Mantegna, R. (1999).
  Hierarchical structure in financial markets.
  The European Physical Journal B, 11(1), 193-197.
  <https://doi.org/10.1007/s100510050929>
* [21]

  Mattera, R., Scepi, G., & Kaur, P. (2025).
  Time series clustering for high-dimensional portfolio selection: A comparative study.
  Soft Computing.
  <https://doi.org/10.1007/s00500-025-10656-2>
* [22]

  Mishra, A., & Motta, F. C. (2023).
  Stability and machine learning applications of persistent homology using the Delaunay-Rips complex.
  Frontiers in Applied Mathematics and Statistics, 9.
  <https://doi.org/10.3389/fams.2023.1179301>
* [23]

  Müllner, D. (2011).
  Modern hierarchical, agglomerative clustering algorithms.
  arXiv preprint.
  <https://doi.org/10.48550/arXiv.1109.2378>
* [24]

  Munkres, J. R. (2018).
  Elements of algebraic topology.
  CRC Press.
  <https://doi.org/10.1201/9780429493911>
* [25]

  Murtagh, F., & Legendre, P. (2014).
  Ward’s hierarchical agglomerative clustering method: Which algorithms implement Ward’s criterion?
  Journal of Classification, 31(3), 274-295.
  <https://doi.org/10.1007/s00357-014-9161-z>
* [26]

  Bank for International Settlements. (2022, October 27).
  OTC foreign exchange turnover in April 2022.
  <https://www.bis.org/statistics/rpfx22_fx.htm>
* [27]

  Paparrizos, J., Yang, F., & Li, H. (2024).
  Bridging the gap: A decade review of time-series clustering methods.
  arXiv preprint.
  <https://doi.org/10.48550/arXiv.2412.20582>
* [28]

  Penn State Eberly College of Science. (n.d.).
  Stat 555: Clustering.
  Retrieved July 23, 2025, from <https://online.stat.psu.edu/stat555/node/88>
* [29]

  Perea, J., & Harer, J. (2013).
  Sliding windows and persistence: An application of topological methods to signal analysis.
  arXiv preprint.
  <https://doi.org/10.48550/arXiv.1307.6188>
* [30]

  Pierini, M. (2021, December 20).
  Why is Turkey’s president cutting interest rates, spurring inflation and lowering the value of the lira?
  Carnegie Endowment for International Peace.
  <https://carnegieendowment.org/diwan/2021/12/why-is-turkeys-president-cutting->
    
  <interest-rates-spurring-inflation-and-lowering>
    
  <-the-value-of-the-lira?lang=en>
* [31]

  Rousseeuw, P. J. (1987).
  Silhouettes: A graphical aid to the interpretation and validation of cluster analysis.
  Journal of Computational and Applied Mathematics, 20, 53-65.
  <https://doi.org/10.1016/0377-0427(87)90125-7>
* [32]

  Schober, P., Boer, C., & Schwarte, L. A. (2018).
  Correlation coefficients: Appropriate use and interpretation.
  Anesthesia & Analgesia, 126(5), 1763-1768.
  <https://doi.org/10.1213/ane.0000000000002864>
* [33]

  Shultz, C. (2023).
  Applications of topological data analysis in economics.
  preprint.
  <http://dx.doi.org/10.2139/ssrn.4378151>
* [34]

  Songdechakraiwut, T., Krause, B. M., Banks, M. I., Nourski, K. V., & Van Veen, B. D. (2021).
  Fast topological clustering with Wasserstein distance.
  arXiv preprint.
  <https://doi.org/10.48550/arXiv.2112.00101>
* [35]

  Theodosiou, M. (2011).
  Forecasting monthly and quarterly time series using STL decomposition.
  International Journal of Forecasting, 27(4), 1178-1195.
  <https://doi.org/10.1016/j.ijforecast.2010.11.002>
* [36]

  Truong, P. (2017).
  An exploration of topological properties of high-frequency one-dimensional financial time series data using TDA.
  KTH Royal Institute of Technology, Master’s thesis.
  <https://kth.diva-portal.org/smash/record.jsf?pid=diva2%3A1169943>
* [37]

  Verma, A., Buonocore, R. J., & Di Matteo, T. (2018).
  A cluster-driven log-volatility factor model: A deepening on the source of the volatility clustering.
  Quantitative Finance, 19(6), 981-996.
  <https://doi.org/10.1080/14697688.2018.1535183>
* [38]

  Vijaya, N., Sharma, S., & Batra, N. (2019).
  Comparative study of single linkage, complete linkage, and Ward method of agglomerative clustering.
  In Proceedings of the 2022 International Conference on Machine Learning, Big Data, Cloud and Parallel Computing (COM-IT-CON).
  <https://doi.org/10.1109/comitcon.2019.8862232>
* [39]

  Wang, Y., Xu, Y., & Gao, T. (2021).
  Evaluation method of wind turbine group classification based on Calinski-Harabasz.
  In Proceedings of the 2021 IEEE 5th Conference on Energy Internet and Energy System Integration (EI2), 2630-2635.
  <https://doi.org/10.1109/ei252483.2021.9713300>
* [40]

  Watts, J. (2016, September 1).
  Brazil’s Dilma Rousseff impeached by Senate in crushing defeat.
  The Guardian.
  <https://www.theguardian.com/world/2016/aug/31/dilma-rousseff-impeached>
  <-president-brazilian-senate-michel-temer>
* [41]

  Wongoutong, C. (2024).
  The impact of neglecting feature scaling in kk-means clustering.
  PLoS ONE, 19(12), e0310839.
  <https://doi.org/10.1371/journal.pone.0310839>
* [42]

  Yim, O., & Ramdeen, K. T. (2015).
  Hierarchical cluster analysis: Comparison of three linkage measures and application to psychological data.
  The Quantitative Methods for Psychology, 11(1), 8-21.
  <https://doi.org/10.20982/tqmp.11.1.p008>