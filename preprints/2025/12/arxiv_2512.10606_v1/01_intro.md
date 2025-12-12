---
authors:
- Paolo Bartesaghi
- Rosanna Grassi
- Pierpaolo Uberti
doc_id: arxiv:2512.10606v1
family_id: arxiv:2512.10606
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Local and Global Balance in Financial Correlation Networks: an Application
  to Investment Decisions'
url_abs: http://arxiv.org/abs/2512.10606v1
url_html: https://arxiv.org/html/2512.10606v1
venue: arXiv q-fin
version: 1
year: 2025
---


Paolo Bartesaghi

Rosanna Grassi

Pierpaolo Uberti
University of Milano, Via Conservatorio 7, 20122 Milano, Italy
University of Milano - Bicocca, Via Bicocca degli Arcimboldi 8, 20126 Milano, Italy

###### Abstract

The global balance is a well-known indicator of the behavior of a signed network. Recent literature has introduced the concept of local balance as a measure of the contribution of a single node to the overall balance of the network. In the present research, we investigate the potential of using deviations of local balance from global balance as a criterion for selecting outperforming assets. The underlying idea is that, during financial crises, most assets in the investment universe behave similarly: losses are severe and widespread, and the global balance of the correlation-based signed network reaches its maximum value. Under such circumstances, standard diversification (mainly related to portfolio size) is unable to reduce risk or limit losses. Therefore, it may be useful to concentrate portfolio exposures on the few assets—if such assets exist—that behave differently from the rest of the market. We argue that these assets are those for which the local balance strongly departs from the global balance of the underlying signed network. The paper supports this hypothesis through an application using real financial data. The results, in both descriptive and predictive contexts, confirm the proposed intuition.

###### keywords:

Signed networks, Local balance, Structural Stability, Systemic risk measures, Stock Picking
JEL Codes: C02, G11, C80

## 1 Introduction

Global balance of a signed network was introduced in [Harary1953, Cartwright1956] to assess weather a network is structurally balanced. More recently, the concept of local balance has been proposed to measure the contribution of a single node to the overall balance of the network (for further details, see [diazdiaz2024]).

A recent contribution proposes the global balance as a valuable measure of systemic risk in financial correlation networks [bartesaghi2025a].
In general, network theory is one possible approach to addressing systemic risk. The failure of one node can propagate and trigger defaults or distress across many others, depending on the network topology. The study by [AllenGale2000] is a prominent contribution to the field. Since then, the literature on this topic has grown, exploiting different network tools. For example, various structural network indicators have been used as measures to assess risk contagion in the interbank system [Battiston2012, Tabak2014, Bardoscia2017, Bongini2018]. Multi-layer financial networks have been proposed to model contagion propagation in bank-firm connections [poledna2021, wang2025]. Dynamic network indicators are useful for tracing the dynamics of contagion across countries and sectors of the financial system [FRANCH2024].
In financial applications of signed networks, [adhikari2025] proposes a discrete optimization model that reduces the asset selection problem to the desired size. Signed graphs have also been used to analyze correlated and anticorrelated asset returns in portfolio risk management and the structural balance of stock markets in [Harary2002, ferreira2021]. The related literature is wide, and we refer the reader to [pacelli2025] for a detailed treatment.

During financial crises, it is well known that correlations among assets increase, causing severe and widespread losses across the market. This phenomenon significantly limits investors’ ability to reduce risk by diversifying portfolio exposures across different assets. In such circumstances, since standard diversification may become ineffective, it may be useful to concentrate investments in a few assets—if such assets exist—that deviate from the behavior of the market.
Transposing this idea in terms of local and global balance, we observe that during financial crises, the level of global balance in financial correlation networks increases, approaching its theoretical maximum (see [bartesaghi2025a]).
In this paper, we test the following intuitive hypothesis: significant deviations of a node’s local balance from the network’s global balance can help identify nodes (assets) that potentially hedge against losses during financial crises and outperform the reference market.

Although the present approach is implemented using return correlations, it overcomes some well-known limitations of standard correlation. For example, comparing a global indicator computed on the entire network with a local
indicator associated with a single node allows us to move beyond the pairwise structure of standard correlation. Moreover, the present approach not only identifies the assets in which allocations should be concentrated but also the periods during which such concentration may be beneficial. To support this intuition, we present an empirical application using different datasets of real financial data, in both descriptive and predictive contexts. We also conduct a sensitivity analysis to determine when a deviation of local balance from global balance can be considered significant.

## 2 Data, notation and preliminaries

Given NN risky assets, the correlation matrix of their returns, 𝐂\bf{C}, and the signed network GG derived from 𝐂\bf{C}, the local and global balance indices are defined as follows:

|  |  |  |
| --- | --- | --- |
|  | κ​(G)=∑i=1N[e𝐂]i​i∑i=1N[e|𝐂|]i​i=∑i=1Neλi∑i=1Neλ¯i,κi​(G):=[e𝐂]i​i[e|𝐂|]i​i\kappa(G)=\frac{\sum\_{i=1}^{N}[e^{\bf C}]\_{ii}}{\sum\_{i=1}^{N}[e^{|{\bf C}|}]\_{ii}}=\frac{\sum\_{i=1}^{N}e^{\lambda\_{i}}}{\sum\_{i=1}^{N}e^{\overline{\lambda}\_{i}}},\quad\quad\kappa\_{i}(G):=\frac{[e^{\bf C}]\_{ii}}{[e^{|{\bf C}|}]\_{ii}} |  |

where λi\lambda\_{i} and λ¯i\overline{\lambda}\_{i} are, respectively, the eigenvalues of 𝐂\bf{C} and |𝐂||\bf{C}|, with i=1,…,Ni=1,\ldots,N, and e𝐂e^{\bf C} represents the matrix exponential.

The application is conducted on four datasets, each identified by the name of the corresponding financial index. The datasets contain daily log returns from 05/01/2005 to 17/09/2020. The indices considered are DAX (N=18N=18), ESX (N=42N=42), FTSE (N=80N=80), and NIKKEI (N=199N=199). The number NN of stocks in each dataset is smaller than the nominal number of index constituents, as the analysis is restricted to stocks that remained in the index throughout the reference period. The experiments are performed using a standard rolling-window setting, where the window length Δ​T\Delta T satisfies the condition Δ​T≥N\Delta T\geq N. This assumption ensures that 𝐂\bf{C} is a full-rank matrix. In the applications, the rolling window is shifted by a step of Δ​t=10\Delta t=10 days.

We start by examining the relationship between the average market return and the Sharpe ratio within a given time window, on the one hand, and the global balance calculated over the same period, on the other. As shown in Table [2.1](https://arxiv.org/html/2512.10606v1#S2.T1 "Table 2.1 ‣ 2 Data, notation and preliminaries ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") for all four datasets, this relationship is negative. This indicates that the values of κ​(G)\kappa(G) increase when average returns and Sharpe ratios decrease. This is a sign that the global balance of a financial correlation network can be interpreted as a measure of systemic risk, accordingly to the hypothesis presented in [bartesaghi2025a].

|  | Global balance - AMR | Global balance - SR |
| --- | --- | --- |
| DAX | −0.262-0.262 (−0.317-0.317) | −0.313-0.313 (−0.350-0.350) |
| ESX | −0.177-0.177 (−0.274-0.274) | −0.227-0.227 (−0.316-0.316) |
| FTSE | −0.215-0.215 (−0.324-0.324) | −0.199-0.199 (−0.325-0.325) |
| NIKKEI | −0.236-0.236 (−0.236-0.236) | −0.250-0.250 (−0.233-0.233) |

Table 2.1: Pearson correlations (Spearman correlations within brackets) between global balance and average market return (AMR) and between global balance and Sharpe ratio (SR) for the four datasets.

This initial evidence is fundamental for the implementation of the investment strategy. In general, a deviation of a node’s local balance from the global balance of the underlying network only indicates that the node behaves differently from the others, without providing information on the direction of this divergence. In contrast, when the global balance of a financial correlation signed network is high, all nodes (assets) tend to report losses. Therefore, assets with a local balance that deviates from the global one are those that outperform the rest of the market.

## 3 Numerical analysis

The idea of concentrating the portfolio in a few assets that locally deviate from the systemic behavior of the market, in time windows characterized by high global balance, is implemented in the following experiment.
We select two thresholds, τG\tau\_{G} and τL\tau\_{L}, to simultaneously identify when the global balance is high and the local balance deviates significantly from it.
Specifically, the set of selected assets is SA={i=1,…​N:κ​(G)≥τG,κG​(t)−κi​(t)≥τL}S\_{A}=\{i=1,\ldots N:\kappa(G)\geq\tau\_{G},\kappa\_{G}(t)-\kappa\_{i}(t)\geq\tau\_{L}\}, whose cardinality |SA||S\_{A}| gives the number of selected assets.

Since the specific allocation rule is not the focus of the present work, we invest in an equally weighted portfolio of the selected assets when the conditions are met, and in an equally weighted portfolio (1/N1/N) otherwise.
Finally, the performance of the 1/N1/N portfolio over the entire period, measured in terms of return and Sharpe ratio, is compared with that of the proposed strategy.

### 3.1 In sample results

We begin by analyzing the in-sample performance, based on the average returns of the last five days of each examined window. Figure [3.1](https://arxiv.org/html/2512.10606v1#S3.F1 "Figure 3.1 ‣ 3.1 In sample results ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") presents the value – in terms of price – of the proposed portfolio strategy (red line) compared with that of the 1/N1/N portfolio (blue line), for all datasets, with different values of the thresholds τL\tau\_{L} and τG\tau\_{G}. What clearly emerges is that the proposed portfolio outperforms the 1/N1/N portfolio across all datasets. Moreover, the higher final value does not imply higher volatility for the improved strategy.

![Refer to caption](Prices_DAX_19_10_0.75_0.35_-5.jpeg)


(a)

![Refer to caption](Prices_ESX_43_10_0.75_0.25_-5.jpeg)


(b)

![Refer to caption](Prices_FTSE_81_10_0.9_0.4_-5.jpeg)


(c)

![Refer to caption](Prices_NIKKEI_200_10_0.9_0.45_-5.jpeg)


(d)

Figure 3.1: Prices of the standard portfolio (blue line) and the improved portfolio (red line): (a) DAX, τG=0.75\tau\_{G}=0.75 and τL=0.35\tau\_{L}=0.35; (b) ESX, τG=0.75\tau\_{G}=0.75 and τL=0.25\tau\_{L}=0.25; (c) FTSE, τG=0.90\tau\_{G}=0.90 and τL=0.40\tau\_{L}=0.40; (d) NIKKEI, τG=0.90\tau\_{G}=0.90 and τL=0.45\tau\_{L}=0.45;

The chosen thresholds are different for each examined dataset. An
appropriate calibration of these values is required for the improved portfolio to outperform the baseline portfolio. The robustness of these results with respect to the chosen parameters is discussed in Section [3.2](https://arxiv.org/html/2512.10606v1#S3.SS2 "3.2 Sensitivity analysis with respect to the choice of the thresholds ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions"), where we present a dedicated sensitivity analysis.

To further support the results, we analyze the probability distributions of returns and corresponding Sharpe ratios of the selected stocks within each time window and compare them with those of the remaining stocks. To ensure consistent comparisons between distributions and to avoid biases related to the smaller number of selected assets relative to the remaining ones, we proceed as follows.
We randomly sample from the remaining stocks a number of securities equal to |SA||S\_{A}|.
This random selection is repeated 10,000 times, and the results are averaged to obtain statistics that enable a robust comparison.

In Figure [3.2](https://arxiv.org/html/2512.10606v1#S3.F2 "Figure 3.2 ‣ 3.1 In sample results ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions"), we present the density functions and box plots for the NIKKEI dataset. As in Figure [3.1](https://arxiv.org/html/2512.10606v1#S3.F1 "Figure 3.1 ‣ 3.1 In sample results ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions"), the red line represents the selected stocks, while the blue line represents the others. Both the distributions and the box plots show that the distribution of the selected stocks is characterized by a higher mean, comparable variance, a thinner left tail, a fatter right tail, and greater skewness. All these findings are visually supported by Figure [3.2](https://arxiv.org/html/2512.10606v1#S3.F2 "Figure 3.2 ‣ 3.1 In sample results ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") and confirmed by the values of the distribution moments, reported in the Table [3.1](https://arxiv.org/html/2512.10606v1#S3.T1 "Table 3.1 ‣ 3.1 In sample results ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") together with the threshold values.

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.9_0.46_-5.jpeg)


(a)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.9_0.46_-5.jpeg)


(b)

Figure 3.2: In sample densities, panel (a) and box plot, panel (b), for the Sharpe ratios of the selected stocks (in red) and the remainder of the dataset (in blue) for the NIKKEI index.




Table 3.1: In-sample distribution moments for Sharpe ratios of selected stocks and remaining dataset for NIKKEI index.

| Group | 𝝉𝑮\tau\_{G} | 𝝉𝑳\tau\_{L} | Mean | Variance | Skewness | Kurtosis |
| --- | --- | --- | --- | --- | --- | --- |
| Selected stocks | 0.90 | 0.46 | 0.1697782 | 0.2853324 | 0.06643058 | 0.6962828 |
| Remaining stocks | 0.90 | 0.46 | -0.01147054 | 0.2928941 | -0.09771086 | 1.240045 |

### 3.2 Sensitivity analysis with respect to the choice of the thresholds

The robustness of the in-sample results is tested on the NIKKEI dataset, which has the largest number of assets (N=199N=199). Specifically, we conduct a sensitivity analysis on the two parameters, τG\tau\_{G} and τL\tau\_{L}. Figure [3.3](https://arxiv.org/html/2512.10606v1#S3.F3 "Figure 3.3 ‣ 3.2 Sensitivity analysis with respect to the choice of the thresholds ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") shows how the distributions of the Sharpe ratio evolve as τG\tau\_{G} increases from 0.750.75 (panel (a)) to 0.900.90 (panel (d)), in increments of 0.050.05, while τL\tau\_{L} remains constant at τL=0.45\tau\_{L}=0.45.
It is evident how the distribution of the selected securities consistently outperforms that of randomly selected securities within the global portfolio. These results confirm that the findings are independent of the specific value of τG\tau\_{G}, which can therefore be used to calibrate the desired overall risk level and determine the number of time windows in which the improved portfolio should replace the baseline one. In general, when both the global and local balance thresholds are reduced, the two distributions converge, as gradually all the securities in the dataset are selected. Table [3.2](https://arxiv.org/html/2512.10606v1#S3.T2 "Table 3.2 ‣ 3.2 Sensitivity analysis with respect to the choice of the thresholds ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") shows the values of the moments of the two distributions for the four values of τG\tau\_{G}.

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.75_0.45_-5.jpeg)


(a)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.8_0.45_-5.jpeg)


(b)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.85_0.45_-5.jpeg)


(c)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.9_0.45_-5.jpeg)


(d)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.75_0.45_-5.jpeg)


(e)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.8_0.45_-5.jpeg)


(f)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.85_0.45_-5.jpeg)


(g)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.9_0.45_-5.jpeg)


(h)

Figure 3.3: Densities for the Sharpe ratios of two groups of selected stocks (in red) and the remainder of the dataset (in blue) for NIKKEI index; τL=0.45\tau\_{L}=0.45 for all plots.




Table 3.2: Summary statistics for Sharpe ratios of selected stocks and global dataset across different threshold configurations for NIKKEI index.

| Panels | 𝝉𝑮\tau\_{G} | Group | Mean | Variance | Skewness | Kurtosis |
| --- | --- | --- | --- | --- | --- | --- |
| (a), (e) | 0.75 | Selected | 0.1507192 | 0.2576365 | 0.008535879 | 1.064017 |
|  |  | Global | 0.007813921 | 0.1589361 | -0.4683775 | 0.4643931 |
| (b), (f) | 0.80 | Selected | 0.1507192 | 0.2576365 | 0.008535879 | 0.6962828 |
|  |  | Global | 0.02143808 | 0.2239296 | 0.3006724 | 1.408511 |
| (c), (g) | 0.85 | Selected | 0.1507192 | 0.2576365 | 0.008535879 | 1.064017 |
|  |  | Global | -0.02057534 | 0.2327003 | -1.020191 | 3.301265 |
| (d), (h) | 0.90 | Selected | 0.1507192 | 0.2576365 | 0.008535879 | 1.064017 |
|  |  | Global | 0.002948375 | 0.2498295 | 0.2155788 | 2.109817 |

A higher sensitivity is observed for τL\tau\_{L}, which affects the number of selected securities. As the gap κG​(t)−κi​(t)\kappa\_{G}(t)-\kappa\_{i}(t) increases, the cardinality |SA||S\_{A}| decreases accordingly, and the resulting distribution becomes less meaningful. Therefore, an optimal threshold value for the gap exists and could be found by maximizing the difference in Sharpe ratios, possibly without excessively reducing the portfolio size. Figure [3.4](https://arxiv.org/html/2512.10606v1#S3.F4 "Figure 3.4 ‣ 3.2 Sensitivity analysis with respect to the choice of the thresholds ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions"), where τG=0.90\tau\_{G}=0.90 and τL\tau\_{L} varies from 0.440.44 to 0.500.50, shows that maintaining τL\tau\_{L} within a relatively narrow range yields robust results, confirming the existence of a profitable region for applying the strategy. Table [3.3](https://arxiv.org/html/2512.10606v1#S3.T3 "Table 3.3 ‣ 3.2 Sensitivity analysis with respect to the choice of the thresholds ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") collects the values of the moments of the two distributions for the four values of τL\tau\_{L}.

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.9_0.44_-5.jpeg)


(a)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.9_0.46_-5.jpeg)


(b)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.9_0.48_-5.jpeg)


(c)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.9_0.5_-5.jpeg)


(d)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.9_0.44_-5.jpeg)


(e)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.9_0.46_-5.jpeg)


(f)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.9_0.48_-5.jpeg)


(g)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.9_0.5_-5.jpeg)


(h)

Figure 3.4: Densities for the Sharpe ratios of the selected stocks (in red) and the remainder of the dataset (in blue) for NIKKEI index; τG=0.90\tau\_{G}=0.90 for all plots.




Table 3.3: Summary statistics for Sharpe ratios of selected stocks and global dataset across different threshold configurations for NIKKEI index.

| Panels | 𝝉𝑳\tau\_{L} | Group | Mean | Variance | Skewness | Kurtosis |
| --- | --- | --- | --- | --- | --- | --- |
| (a), (e) | 0.44 | Selected | 0.1476046 | 0.2567015 | 0.02498729 | 1.093287 |
|  |  | Global | 0.03372156 | 0.2652361 | 0.7340246 | 1.92165 |
| (b), (f) | 0.46 | Selected | 0.1697782 | 0.2853324 | 0.06643058 | 0.6962828 |
|  |  | Global | -0.01147054 | 0.2928941 | -0.09771086 | 1.240045 |
| (c), (g) | 0.48 | Selected | 0.1607774 | 0.2839912 | 0.03776458 | 5.63365 |
|  |  | Global | 0.11454 | 0.7331053 | 4.157748 | 22.83232 |
| (d), (h) | 0.50 | Selected | 0.1657216 | 0.2885198 | 0.01298107 | 0.291521 |
|  |  | Global | 0.01242995 | 0.1607477 | 0.2007902 | 1.410646 |

### 3.3 Out-of-sample analysis

We extend the analysis to the out-of-sample context to evaluate whether the proposed strategy outperforms the benchmark 1/N1/N in practice. Specifically, returns are averaged over the five days following the assessment window. Accordingly, we concentrate the portfolio in a few stocks based on a large balance gap (local versus global) and compare the out-of-sample Sharpe ratios of the selected stocks with those of the remaining ones. The strategy of randomly selecting from the remaining stocks a number equal to that of the selected ones is again employed to compare the corresponding distributions.

We report results only for the NIKKEI index. Since the highest sensitivity is observed for the τL\tau\_{L} values, we present graphs for a fixed τG\tau\_{G} and four different levels of τL\tau\_{L}. Figure [3.5](https://arxiv.org/html/2512.10606v1#S3.F5 "Figure 3.5 ‣ 3.3 Out-of-sample analysis ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") shows the distributions and box plots of the two groups of stocks, and Table [3.4](https://arxiv.org/html/2512.10606v1#S3.T4 "Table 3.4 ‣ 3.3 Out-of-sample analysis ‣ 3 Numerical analysis ‣ Local and Global Balance in Financial Correlation Networks: an Application to Investment Decisions") collects the values for τL\tau\_{L} and the corresponding moments.

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.95_0.45_5.jpeg)


(a)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.95_0.5_5.jpeg)


(b)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.95_0.55_5.jpeg)


(c)

![Refer to caption](Final_Density_sharpe_ratio_equal_length_NIKKEI_200_10_0.95_0.6_5.jpeg)


(d)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.95_0.45_5.jpeg)


(e)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.95_0.5_5.jpeg)


(f)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.95_0.55_5.jpeg)


(g)

![Refer to caption](Final_Boxplot_sharpes_ratio_equal_length_NIKKEI_200_10_0.95_0.6_5.jpeg)


(h)

Figure 3.5: Out-of-sample densities and box plots for the Sharpe ratios of two groups of selected stocks (in red) and the remainder of the dataset (in blue) for the NIKKEI index; τG=0.95\tau\_{G}=0.95 for all plots.




Table 3.4: Out-of-sample summary statistics for Sharpe ratios of selected stocks and global dataset across different threshold configurations for NIKKEI index.

| Panels | 𝝉𝑳\tau\_{L} | Group | Mean | Variance | Skewness | Kurtosis |
| --- | --- | --- | --- | --- | --- | --- |
| (a), (e) | 0.45 | Selected | 0.2603452 | 0.5146761 | 1.716332 | 3.608807 |
|  |  | Global | 0.04530861 | 0.2191899 | 0.5939232 | 0.6505542 |
| (b), (f) | 0.50 | Selected | 0.258769 | 0.5325863 | 1.751952 | 3.694765 |
|  |  | Global | 0.05657042 | 0.2661601 | 0.1199921 | 1.890272 |
| (c), (g) | 0.55 | Selected | 0.187869 | 0.3785311 | 1.784601 | 5.63365 |
|  |  | Global | 0.05414324 | 0.2583662 | 2.644774 | 9.726742 |
| (d), (h) | 0.60 | Selected | 0.1932738 | 0.3740916 | 1.802024 | 5.765645 |
|  |  | Global | 0.04606595 | 0.1607477 | -0.08739961 | 0.07603652 |

Consider, as an example, the periods and stocks extracted from the NIKKEI index by the proposed out-of-sample approach with τG=0.95\tau\_{G}=0.95 and τL=0.50\tau\_{L}=0.50. In this case, the selected stocks exhibit a Sharpe ratio of 0.2587690.258769, while the remaining stocks show a Sharpe ratio of 0.056570420.05657042, indicating a positive gap in favor of the selected portfolio. We also observe that the skewness of the first distribution is higher than that of the second: 1.7519521.751952 for the selected portfolio compared with 0.11999210.1199921 for the remaining stocks. Even in the out-of-sample context, local balance proves to be an effective criterion for selecting securities with higher Sharpe ratios. This therefore empirically confirms the validity of the proposed methodology.

## 4 Conclusions

The main idea proposed in this paper is to study deviations of local balance from global balance in a signed network to identify distinctive behaviors of specific nodes. This intuition is applied in a financial context by proposing an investment strategy that concentrates allocations in a few assets when two conditions are met: (i) a high level of global balance, indicating a financial crisis, and (ii) some nodes characterized by low levels of local balance. The rationale is that during periods of financial turbulence, standard diversification does not effectively reduce risk, and investors may instead consider concentrating their portfolios in a small number of assets that potentially outperform the market. During such crises, the risk associated with holding a concentrated portfolio is limited, as diversification opportunities reduce. The proposed criterion for selecting outperforming assets is based on the divergence between the global balance of the underlying signed network and the local balance of individual nodes. Experiments conducted on four datasets of real financial data confirm both the intuition and the effectiveness of the proposed investment strategy in outperforming the benchmark equally weighted portfolio, which approximates the market. The application demonstrates that meaningful results are obtained not only in a descriptive context but also in a predictive framework. Future research will focus on a more systematic investigation of these findings and on extending the proposed selection criterion to signed networks constructed from inputs other than the correlation matrix of returns.