---
authors:
- Jing Liu
- Maria Grith
- Xiaowen Dong
- Mihai Cucuringu
doc_id: arxiv:2603.10559v1
family_id: arxiv:2603.10559
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting
url_abs: http://arxiv.org/abs/2603.10559v1
url_html: https://arxiv.org/html/2603.10559v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jing Liu
Corresponding author; Email: jing.liu@exeter.ox.ac.uk
Department of Statistics, University of Oxford, UK

Maria Grith
Finance Department, Neoma Business School, France

Xiaowen Dong
Department of Engineering Science, University of Oxford, UK

Mihai Cucuringu
Department of Mathematics, University of California Los Angeles, US
Department of Statistics, University of Oxford, UK
Oxford-Man Institute of Quantitative Finance, University of Oxford, UK

###### Abstract

This paper studies cross-market return predictability through a machine learning framework that preserves economic structure. Exploiting the non-overlapping trading hours of the U.S. and Chinese equity markets, we construct a directed bipartite graph that captures time-ordered predictive linkages between stocks across markets. Edges are selected via rolling-window hypothesis testing, and the resulting graph serves as a sparse, economically interpretable feature-selection layer for downstream machine learning models. We apply a range of regularized and ensemble methods to forecast open-to-close returns using lagged foreign-market information. Our results reveal a pronounced directional asymmetry: U.S. previous-close-to-close returns contain substantial predictive information for Chinese intraday returns, whereas the reverse effect is limited. This informational asymmetry translates into economically meaningful performance differences and highlights how structured machine learning frameworks can uncover cross-market dependencies while maintaining interpretability.

Keywords: Return prediction, cross-market analysis, machine learning, bipartite graphs

JEL Classification: G17, G15, C58

## 1 Introduction

Return prediction remains a central problem in empirical asset pricing and portfolio management, yet its statistical difficulty is amplified by noise, non-stationarity, and nonlinear dependence structures in financial markets. While machine learning methods have become increasingly prevalent in single-market forecasting applications (chen2015lstm; wang2024stock; yang2026enhancing), comparatively little attention has been paid to stock-level cross-market return prediction under realistic trading-session timing constraints.

Most existing studies on return forecasting focus on predicting within a single market. For example, chen2015lstm apply a Long Short-Term Memory (LSTM) model to predict stock returns in the Chinese market, while wang2024stock studies U.S. stock return prediction using neural network models. Similarly, yang2026enhancing propose an intraday volume-based uncertainty proxy to predict return direction in the Chinese market. These studies demonstrate the growing use of machine learning methods in single-market settings.
By contrast, research on cross-market interactions has largely emphasized contemporaneous co-movement, spillovers, or causal transmission rather than explicit stock-level return prediction.
For instance, eun1989international analyze the international transmission of stock market movements using vector autoregression, baur2006return evaluate contemporaneous return correlations using GARCH models, and rapach2013international document the leading role of the U.S. market through causality tests. sarwar2014us examine the relationship between U.S. market uncertainty and European equity returns during crisis periods, while jung2024threshold study interdependency patterns between the U.S. and Chinese markets using threshold overnight co-movement processes.

Only a limited number of studies have attempted explicit cross-market predictive analysis using machine learning models. For example, lee2020multimodal apply a deep neural network to fuse information from the U.S. and South Korean markets for index-level return prediction, and kumar2024dynamic propose a graph neural network to model volatility spillovers across markets. However, most existing work operates at the index level, and to our knowledge no prior study has examined stock-level cross-market return prediction between the U.S. and Chinese markets under realistic trading-session timing.

Our study fills this gap by developing a directed bipartite graph framework for stock-level cross-market return forecasting between the U.S. and Chinese equity markets. We construct a time-ordered bipartite graph that selects cross-market predictors based on rolling-window screening, thereby capturing directed predictive links across non-overlapping trading sessions. The selected predictors are then embedded into a suite of ten machine learning models to forecast next-session open-to-close (OPCL) returns in each market.

Empirically, we demonstrate a pronounced directional asymmetry: U.S. market information is substantially more informative for predicting Chinese stock returns than vice versa. Sharpe Ratios (SRs) obtained when forecasting Chinese stocks using U.S. predictors consistently exceed those in the reverse direction. We further show that both the graph-based selection mechanism and cross-market information contribute materially to predictive performance.

Sector-level patterns in the estimated graph reveal economically interpretable transmission channels across markets. For instance, sector-level aggregation of the bipartite graph reveals meaningful cross-sector transmission patterns rather than a block-diagonal structure. Our focus is on documenting directional cross-market predictability and the structure of the associated dependency graph rather than designing a fully implementable trading strategy. Accordingly, performance metrics are reported pre-transaction-cost and without liquidity-optimized weighting, and should be interpreted as evidence of predictive asymmetry rather than deployable alpha.

Our setting is economically and statistically distinctive because the U.S. and Chinese equity sessions do not overlap. This implies that U.S. previous-close-to-close (pvCLCL) information is fully observed before the subsequent Chinese OPCL window begins, yielding a clean timing structure for cross-market prediction. The directed bipartite graph can therefore be interpreted as a time-ordered map of potential information transmission channels across markets, rather than a contemporaneous correlation network.

The structure of the paper is arranged as follows. Section [2](#S2 "2 Related Literature ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") provides a detailed review of related work. Section [3](#S3 "3 Data ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") describes the data we use and the definitions of financial terms involved. Section [4](#S4 "4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") introduces the graph-based methodology for feature selection and prediction. Section [5](#S5 "5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") presents the evaluation metrics and experimental results. Finally, Section [6](#S6 "6 Conclusion and Future Research ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") summarizes the study and discusses future research directions.

## 2 Related Literature

### 2.1 Cross-Market Analysis and Prediction

Global financial markets have become increasingly interconnected with the intensification of international economic and financial integration. As a result, shocks, volatility, and information can propagate rapidly across countries through multiple transmission channels. A substantial body of research therefore examines cross-market linkages, including price discovery, return co-movement, volatility spillovers, and broader measures of financial interconnectedness, typically within econometric frameworks.
Such interconnectedness has motivated studies of directional information flow and market leadership across countries.
For example, liu2011information examine information transmission and price discovery between the U.S. and Chinese markets. asgharian2013spatial study how economic and geographical relationships across countries affect stock market returns. mohammadi2015return analyze daily returns and volatility dynamics in the U.S. and Chinese markets. clements2015volatility investigate global transmission of news and volatility across financial markets, while ahmad2018financial explore market interconnectedness through return and volatility spillovers. huang2023cross construct a financial network to characterize cross-market risk spillovers and interaction topology. These studies primarily emphasize contemporaneous relationships and transmission mechanisms rather than explicit stock-level return prediction.

Beyond studying cross-market information propagation, a growing strand of research incorporates signals from multiple markets into forecasting models to improve predictive performance. Such integration typically relies on feature engineering that embeds external market indicators, deep learning architectures that fuse multi-market inputs, or graph-based models designed to capture inter-market dependencies. For example, thenmozhi2016forecasting use foreign index information to enhance index prediction, lee2020multimodal develop multimodal deep learning models for cross-market index forecasting, and lin2025cspo leverage external futures market data to predict movements of the China Securities Index. gong2025cross propose a cross-market volatility forecasting framework exploiting risk transmission across markets.

However, much of this literature focuses on aggregate indices or volatility measures rather than stock-level return prediction. Moreover, network structures are often employed to characterize spillovers and interconnectedness rather than as predictive screening devices for individual stocks. Explicit stock-level cross-market return forecasting under time-ordered, non-overlapping trading sessions remains largely unexplored.
Applying our methodology in this setting is therefore novel. Empirically, the directed bipartite structure reveals pronounced asymmetry in cross-market predictability, with U.S. stocks exerting substantially stronger predictive influence on Chinese stocks than vice versa.
These findings align with the literature documenting asymmetric cross-market return predictability with a leading role for the U.S.. rapach2013international show that lagged U.S. market returns possess substantial predictive power for foreign equity markets, while the reverse predictability is considerably weaker, highlighting the central role of the U.S. in global price discovery. Similarly, siliverstovs2017international finds that the predictive influence of the U.S. is particularly pronounced during market downturns, reinforcing the view that U.S. information dominates international return dynamics. Focusing specifically on China-related markets, mohammadi2015return document significant return and volatility spillovers from the U.S. to China mainland and Hong Kong, with weaker effects in the opposite direction.

### 2.2 Graph Methods in Finance

Graph methods provide a way to represent relationships among financial entities, rather than treating each entity in isolation. The use of graphs aligns with the view that financial systems are interconnected (bardoscia2021physics), and that modeling these interconnections can improve forecasting and risk‐management (chen2025financial). Many financial phenomena, such as asset co-movements, spillovers and supply-chain linkages, are naturally represented as graphs.

Bipartite graphs, which originate in graph theory and network science as representations of relationships between two distinct sets of nodes (guillaume2006bipartite; newman2018networks), provide a natural framework for modeling interactions across disjoint groups. In economics and finance, bipartite structures arise in contexts such as credit networks, production networks, and supply-chain relationships, where connections form between two heterogeneous sets of entities rather than within a single homogeneous market. For instance, kley2020modelling study extremal dependence for operational risk by a bipartite graph. wang2020bipartite design a bipartite-graph-based recommender for crowdfunding with sparse data. In econometrics, wu2024bipartite propose a quasi-maximum likelihood approach to estimate a bipartite network influence model.

A growing literature applies graph neural networks (GNNs) and related architectures to financial forecasting tasks.
wang2021review provide a survey of GNN methods in financial applications, including stock movement prediction, loan default risk assessment, recommender systems, fraud detection, and other financial events. chen2018incorporating apply a Graph Convolutional Network (GCN) to integrate information from related companies and improve stock price prediction. li2021modeling propose an LSTM-relational GCN that captures inter-stock relationships through correlation matrices to predict overnight movements. capponi2024graph develop a GNN framework for asset pricing using supply-chain data. zhang2025forecasting incorporate cross-stock spillover effects to forecast multivariate realized volatilities, and luo2025spatial construct a semantic company relationship graph to enhance stock price forecasting.

Some recent empirical work extends graph-based forecasting to richer and more dynamic architectures. For example, cheng2021modeling employ a Graph Attention Network (GAT) to model momentum spillovers in stock returns, while kumar2024dynamic introduce a temporal GAT that combines graph convolution and attention mechanisms to capture structural and temporal dependencies across global market indices. lee2025symmetry show that GCN- and GAT-based models can outperform conventional machine learning baselines by exploiting symmetric interdependencies among financial indices. Related research also incorporates multimodal information into graph construction. cheng2022financial integrate financial events and news into a multimodal GNN framework for price prediction, and liu2024multimodal develop a multiscale dynamic GCN that combines textual and numerical inputs to forecast stock movements.

Despite these advances, most graph-based forecasting models construct within-market networks, where edges are defined through contemporaneous similarity, correlation, or learned attention mechanisms. Such graphs typically capture symmetric interdependencies among assets within a single market and are primarily used to enhance predictive performance through richer representation learning. In contrast, our framework constructs a directed bipartite graph across two distinct markets, where edges are formed through time-ordered predictive screening rather than contemporaneous association. The resulting graph serves as a feature-selection mechanism for stock-level cross-market return prediction, explicitly exploiting the non-overlapping trading sessions between the U.S. and Chinese markets.

### 2.3 Machine Learning in Finance

Driven by increasing data availability and computational power, the application of machine learning in finance has expanded substantially in recent years. Compared to classical time-series and econometric models, such as ARIMA and GARCH, machine learning approaches are often considered better suited to high-dimensional and nonlinear settings. A survey by rundo2019machine documents that machine-learning-based systems demonstrate superior overall performance compared to traditional approaches. Another survey by kelly2023financial highlights how machine learning methods have become established in empirical financial research. Key applications include forecasting asset returns, volatility estimation, fraud detection, and algorithmic trading. Forecasting asset returns remains inherently difficult due to low signal-to-noise ratios, structural instability, and nonlinear dependence patterns. Moreover, evidence of predictive gains is often sensitive to model specification and feature construction. These challenges partly motivate the adoption of flexible machine learning methods and the incorporation of richer information sets. Given recent developments in machine learning, its applications in finance can be grouped into several major categories: traditional machine learning methods, deep learning methods, and large-language-model-based methods.

For traditional machine learning methods, huang2005forecasting employ support vector machines (SVM) to predict the direction of weekly price movements. kumar2006forecasting investigate the application of SVM and Random Forests (RF) in predicting the direction of a market index. cakra2015stock incorporate sentiment information and use a basic linear regression model for stock price prediction. thenmozhi2016forecasting predict stock prices of several major indices using support vector regression. yang2026enhancing propose a novel proxy and apply Extreme Gradient Boosting (XGBoost) to predict return directions in the Chinese market.

For deep learning methods, chen2015lstm use an LSTM model for sequence learning and Chinese stock return forecasting. wang2024stock investigates the performance of neural network models in predicting stock returns. A survey by gao2024machine highlights the expanding use of deep neural networks, convolutional neural networks, recurrent neural networks, and other advanced architectures in financial contexts.

For large-language-model-based methods, nie2024survey review how Large Language Models (LLMs) are applied in finance. ding2023integrating demonstrate the effectiveness of LLMs in forecasting stock returns. chen2023chatgpt propose a framework that integrates ChatGPT and GNN to forecast stock movements. chen2024does investigate the ability of ChatGPT for stock return forecasting.

Despite these advances, most existing studies focus on single-market return prediction and rely primarily on information drawn from within the same market. Additional information is often shown to improve predictive performance, yet it is typically incorporated in contemporaneous or symmetric settings. Very few studies employ machine learning methods in stock-level cross-market forecasting environments characterized by asynchronous trading sessions and explicitly time-ordered information flows. Differing from existing studies, our framework combines directed bipartite screening with a second-stage machine learning prediction step, enabling systematic exploitation of cross-market dependencies, temporal ordering, and asymmetric predictive structure.

## 3 Data

The stock data used in this study cover several of the world’s largest markets by market capitalization, including the New York Stock Exchange (NYSE), Nasdaq, the Shanghai Stock Exchange (SSE), and the Shenzhen Stock Exchange (SZSE). Daily U.S. stock data are sourced from the Center for Research in Security Prices111https://www.crsp.org/ (CRSP), while daily Chinese stock data are sourced from the Wind Database222https://www.wind.com.cn/. The data span the period from 2014 through 2021. This selection of data enables us to investigate the transferability of signals across the world’s largest and most liquid equity markets operating under non-overlapping trading sessions.

In this paper, we rely on the market excess return of a stock, defined as the difference between the raw return of its price and the return of an exchange-traded fund (ETF) representing overall stock market performance. We use both pvCLCL returns and OPCL returns in one market to forecast OPCL returns in the other market (see Section [4.2](#S4.SS2 "4.2 Predictive Analysis with Machine Learning ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") for a more detailed justification of this setting). The pvCLCL logarithmic raw return for stock i\displaystyle i on day t\displaystyle t can be calculated by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri,pvCLCL(t)=log⁡pi,cl(t)pi,cl(t−1),R\_{i,\text{pvCLCL}}^{(t)}=\log\frac{p\_{i,\text{cl}}^{(t)}}{p\_{i,\text{cl}}^{(t-1)}}, |  | (1) |

while the OPCL logarithmic raw return for stock i\displaystyle i on day t\displaystyle t can be calculated by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri,OPCL(t)=log⁡pi,cl(t)pi,op(t).R\_{i,\text{OPCL}}^{(t)}=\log\frac{p\_{i,\text{cl}}^{(t)}}{p\_{i,\text{op}}^{(t)}}. |  | (2) |

Here pi,cl(t)\displaystyle p\_{i,\text{cl}}^{(t)} and pi,op(t)\displaystyle p\_{i,\text{op}}^{(t)} denote the closing and opening price of stock i\displaystyle i on day t\displaystyle t respectively. Then the market excess return of stock i\displaystyle i on day t\displaystyle t can be defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri(t)=Ri,pvCLCL(t)−RETF,pvCLCL(t)r\_{i}^{(t)}=R\_{i,\text{pvCLCL}}^{(t)}-R\_{\text{ETF},\text{pvCLCL}}^{(t)} |  | (3) |

for pvCLCL returns, or

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri(t)=Ri,OPCL(t)−RETF,OPCL(t)r\_{i}^{(t)}=R\_{i,\text{OPCL}}^{(t)}-R\_{\text{ETF},\text{OPCL}}^{(t)} |  | (4) |

for OPCL returns.
We use SPY as the market ETF in the U.S. and 513500.SH in China.

We select 500 stocks with the highest average market capitalizations over the years covered in the dataset from each country.333This universe selection relies on full-sample information (average market capitalization over 2014–2021) and therefore introduces a mechanical look-ahead component. We adopt it as a pragmatic way to focus on continuously traded, highly liquid stocks and reduce missing observations. However, we caution that a fully investable design would require time-t\displaystyle t reconstitution based solely on lagged market capitalization information. Importantly, our main qualitative finding is directional asymmetry (the influence of the U.S. market on the Chinese market being stronger than the reverse effect), which is unlikely to be driven solely by this selection procedure. Nonetheless, we consider time-local universe formation as a valuable extension.
Unless otherwise specified, all returns mentioned in the following contents refer to market excess returns.

To mitigate the influence of extreme values and potential outliers, we apply winsorization to the training-sample returns of each stock, replacing observations below the 0.5th percentile with the 0.5th percentile value and those above the 99.5th percentile with the 99.5th percentile value.

## 4 Methodology

This study aims to predict individual stock returns using a cross-market directed bipartite graph. The prediction framework consists of two main stages. First, we build a directed bipartite graph using return data from two markets within a look-back training window. This graph identifies cross-market predictive links: if a directed edge connects two stocks, the stock at the source of the edge is treated as a predictor for forecasting the returns of the stock at the destination. In the second stage, we apply various machine learning methods to forecast returns based on the identified relationships.

### 4.1 Directed Bipartite Graph

A graph can be defined as 𝒢=(𝒱,ℰ)\displaystyle\mathcal{G}=(\mathcal{V},\mathcal{E}), where 𝒱\displaystyle\mathcal{V} represents the vertex set and ℰ\displaystyle\mathcal{E} represents the edge set. 𝒢\displaystyle\mathcal{G} is called bipartite if 𝒱\displaystyle\mathcal{V} can be divided into two disjoint sets 𝒳\displaystyle\mathcal{X} and 𝒴\displaystyle\mathcal{Y} such that all edges have one endpoint in 𝒳\displaystyle\mathcal{X} and another in 𝒴\displaystyle\mathcal{Y}. We denote a directed edge from vi\displaystyle v\_{i} to vj\displaystyle v\_{j} as ei​j\displaystyle e\_{ij} with associated weight wi​j\displaystyle w\_{ij}.
For a bipartite graph 𝒢\displaystyle\mathcal{G}, the biadjacency matrix 𝐁\displaystyle\mathbf{B} is defined where rows correspond to nodes in 𝒳\displaystyle\mathcal{X}, columns correspond to nodes in 𝒴\displaystyle\mathcal{Y}, and each entry bi​j\displaystyle b\_{ij} contains the weight wi​j\displaystyle w\_{ij} of edge ei​j\displaystyle e\_{ij}.

We represent two different markets, the source market 𝒳\displaystyle\mathcal{X} and target market 𝒴\displaystyle\mathcal{Y}, as two vertex sets, where stocks in each market are interpreted as nodes. Edges originate from nodes in 𝒳\displaystyle\mathcal{X} and point to nodes in 𝒴\displaystyle\mathcal{Y}.
For a specific period of time w\displaystyle w, which is the look-back training window in the experiment, the daily return vector of the j​th\displaystyle j\text{th} stock in market 𝒳\displaystyle\mathcal{X} is

|  |  |  |
| --- | --- | --- |
|  | 𝒙=[rXj(t−l−w),rXj(t−l−w+1),…,rXj(t−l−1)]⊺,\bm{x}=[r\_{X\_{j}}^{(t-l-w)},r\_{X\_{j}}^{(t-l-w+1)},...,r\_{X\_{j}}^{(t-l-1)}]^{\intercal}, |  |

where rXj(t)\displaystyle r\_{X\_{j}}^{(t)} is the return of the j​th\displaystyle j\text{th} stock on day t\displaystyle t. The daily return vector of the i​th\displaystyle i\text{th} stock in market 𝒴\displaystyle\mathcal{Y} is

|  |  |  |
| --- | --- | --- |
|  | 𝒚=[rYi(t−w),rYi(t−w+1),…,rYi(t−1)]⊺.\bm{y}=[r\_{Y\_{i}}^{(t-w)},r\_{Y\_{i}}^{(t-w+1)},...,r\_{Y\_{i}}^{(t-1)}]^{\intercal}. |  |

The lag parameter l\displaystyle l captures the temporal ordering induced by non-overlapping trading sessions, ensuring that returns in the source market precede those in the target market.
Note that in our study the calculation with t\displaystyle t uses the trading calendar rather than the natural calendar.

This time-ordered screening procedure induces a directed bipartite graph, where nodes in the source market 𝒳\displaystyle\mathcal{X} are connected to nodes in the target market 𝒴\displaystyle\mathcal{Y} whenever statistically significant predictive links are detected within the rolling training window. Figure [1](#S4.F1 "Figure 1 ‣ 4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") provides a schematic illustration of this bipartite structure.

![Refer to caption](2603.10559v1/my_plots/graph_structure_2.png)


Figure 1: Schematic illustration of the directed bipartite graph linking source-market stocks to target-market stocks based on significant predictive relationships.

For each ordered pair (Xj,Yi)\displaystyle(X\_{j},Y\_{i}), we estimate a univariate linear regression of 𝒚\displaystyle\bm{y} on 𝒙\displaystyle\bm{x} within the look-back window.
We quantify such relationship using the t-statistic from regression, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | tβ=βse/∑i=1w(xi−x¯)2.t\_{\beta}=\frac{\beta}{s\_{e}/\sqrt{\sum\_{i=1}^{w}{(x\_{i}-\bar{x})^{2}}}}. |  | (5) |

Here, β\displaystyle\beta is the slope coefficient of the simple linear regression, given by
β=cov⁡(𝒙,𝒚)var⁡(𝒙)\displaystyle\beta=\frac{\operatorname{cov}(\bm{x},\bm{y})}{\operatorname{var}(\bm{x})}
and se\displaystyle s\_{e} denotes the standard error of the regression
se=SSEw−2\displaystyle s\_{e}=\sqrt{\frac{\text{SSE}}{w-2}}.
SSE denotes the sum of squared residuals,
SSE=∑i=1w(yi−yi^)2\displaystyle\text{SSE}=\sum\_{i=1}^{w}{(y\_{i}-\hat{y\_{i}})^{2}},
where
𝒚^=β​𝒙+𝜶\displaystyle\hat{\bm{y}}=\beta\bm{x}+\bm{\alpha}, and
𝜶=𝒚¯−β​𝒙¯\displaystyle\bm{\alpha}=\bar{\bm{y}}-\beta\bar{\bm{x}}.
Here, yi^\displaystyle\hat{y\_{i}} is the fitted value of yi\displaystyle y\_{i}, and α\displaystyle\alpha is the intercept of the regression line.

The use of pairwise univariate screening serves primarily as a computationally tractable sparsification device rather than as a formal structural inference procedure. Similar marginal screening approaches are common in high-dimensional predictive settings where the objective is feature selection rather than causal identification (see, e.g., fan2008\_sure\_screening; hastie2009elements). We recognize that testing across a large number of stock pairs raises multiple-testing considerations and may introduce spurious edges in finite samples (cf. Harvey2015\_multiple\_testing). In principle, false discovery rate or multiple-comparison corrections could be applied. However, our primary goal is to construct a predictive graph that enhances out-of-sample forecasting performance rather than to perform statistical inference on individual edges. We therefore treat the screening step as a model-selection heuristic and assess its validity through out-of-sample forecasting performance and robustness analyses.

Figure [2](#S4.F2 "Figure 2 ‣ 4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") shows the return time series for an example pair of U.S. and Chinese technology stocks, CDNS (pvCLCL returns) and 002410.XSHE (OPCL returns), smoothed with a three-day moving average for visualization purposes. Here l=1\displaystyle l=1 and w=250\displaystyle w=250. The t-statistic from the regression of 002410.XSHE on CDNS is high during the period shown, illustrating a statistically significant cross-market predictive relation within the training window under the linear screening specification.

![Refer to caption](2603.10559v1/my_plots/pair4_250_data.jpg)


Figure 2: Example time series of U.S. pvCLCL returns for CDNS and Chinese OPCL returns for 002410.XSHE over the rolling training window. The series are shown for illustrative purposes to highlight cross-market co-movement underlying the detected predictive link.

In our setting, either the U.S. or the Chinese market can be treated as the source market 𝒳\displaystyle\mathcal{X}, with the target market of prediction serving as market 𝒴\displaystyle\mathcal{Y}. After performing the regression t-test above for all ordered stock pairs in market 𝒳\displaystyle\mathcal{X} and 𝒴\displaystyle\mathcal{Y}, we set a threshold to filter the resulting t-statistics by magnitude.
We introduce an explicit threshold parameter, denoted by τ\displaystyle\tau, to facilitate later reference. In our experiments, we set τ=2\displaystyle\tau=2, and select edges whenever |tβ|>τ\displaystyle|t\_{\beta}|>\tau, corresponding approximately to conventional significance levels under standard asymptotic approximations.
If the magnitude of the t-statistics for 𝒙\displaystyle\bm{x} and 𝒚\displaystyle\bm{y} is larger than τ\displaystyle\tau, we select the return of Xj\displaystyle X\_{j} on day t−l\displaystyle t-l to predict the return of Yi\displaystyle Y\_{i} on day t\displaystyle t. This selection forms a directed edge in the graph pointing from Xj\displaystyle X\_{j} to Yi\displaystyle Y\_{i}.
Note that the thresholding step is used purely as a sparsification mechanism, aimed at denoising the signal and improving computational tractability rather than constituting a formal multiple-testing correction.
A sample directed bipartite graph is shown in Figure [1](#S4.F1 "Figure 1 ‣ 4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), where Xj\displaystyle X\_{j} and Xk\displaystyle X\_{k} on day t−l\displaystyle t-l are selected to predict Yi\displaystyle Y\_{i} on day t\displaystyle t.
This construction yields a time-lagged cross-market predictive network that can be naturally interpreted as a directed bipartite graph.

Figure [3](#S4.F3 "Figure 3 ‣ 4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") presents a section of the heatmap corresponding to the biadjacency matrix of the U.S.–Chinese stock network on 21 October 2021. To illustrate the structure more clearly, we select 25 representative stocks from each sector. For sectors containing fewer than 25 stocks in the original dataset, all available stocks are included, resulting in 254 U.S. stocks and 235 Chinese stocks in this visualization. Each row corresponds to a Chinese stock, while each column represents a U.S. stock. The colour intensity represents the value of the t-statistic, and black grid lines delineate sectoral boundaries.
This visualization shows that cross-market predictive connectivity is not restricted to within-sector interactions (which would lead to a block-diagonal structure), thereby motivating a flexible cross-market predictive framework.

![Refer to caption](2603.10559v1/my_plots/2020-10-21_heatmap_filtered_sorted_adj.png)


Figure 3: Heatmap of the directed biadjacency matrix for a representative trading day. Rows correspond to Chinese stocks and columns to U.S. stocks, grouped by sector. Each entry represents the t-statistic from the rolling-window regression of Chinese returns on lagged U.S. returns. Colour intensity reflects the magnitude and sign of the predictive relationship.

To summarize cross-market structure over time, we average the daily biadjacency matrices across the full sample period, obtaining an aggregate representation of predictive linkages.
We then compute, for this time-averaged matrix, the median of absolute t-statistics within each sector-by-sector block of the corresponding heatmap (Figure [4](#S4.F4 "Figure 4 ‣ 4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting")).
This aggregation highlights systematic sectoral dependencies rather than stock-specific effects. For example, the financial services sector in the Chinese market exhibits strong predictive links with the utilities sector in the U.S. market.

![Refer to caption](2603.10559v1/my_plots/all_date_sector_heatmap_median_abs.png)


Figure 4: Sector-level heatmap of the absolute median t-statistic in the time-averaged biadjacency matrix of the directed cross-market graph. Rows correspond to Chinese sectors and columns to U.S. sectors. Each entry reports the median absolute predictive strength across all stock pairs within the corresponding sector-by-sector block.

We also examine the cross-market relations over time.
Figure [5](#S4.F5 "Figure 5 ‣ 4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") shows how the in-degree of all nodes in set 𝒴\displaystyle\mathcal{Y} evolves over time. For each day, the 25th, 50th, and 75th percentiles of the in-degree distribution are computed across all target nodes. The blue curves represent the number of U.S. pvCLCL nodes selected to predict Chinese OPCL returns, while the red curves correspond to the number of Chinese pvCLCL nodes selected to predict U.S. OPCL returns. As time progresses, the in-degree in both directions increases, suggesting strengthening cross-market predictive connectivity over the sample period.

![Refer to caption](2603.10559v1/my_plots/comparison_bydecile_neighbours_by_date.jpg)


Figure 5: The figure shows the 25th, 50th, and 75th percentiles of the in-degree distribution of target nodes by day. US-CN represents the number of U.S. pvCLCL nodes selected to predict Chinese OPCL returns, while CN-US represents the number of Chinese pvCLCL nodes selected to predict U.S. OPCL returns.

### 4.2 Predictive Analysis with Machine Learning

In order to predict the return of stock Yi\displaystyle Y\_{i} on day t\displaystyle t, we use training data from day t−w\displaystyle t-w to day t−1\displaystyle t-1 for market 𝒴\displaystyle\mathcal{Y} and from day t−l−w\displaystyle t-l-w to day t−l−1\displaystyle t-l-1 for market 𝒳\displaystyle\mathcal{X}.
Since we wish to predict rYi(t)\displaystyle r\_{Y\_{i}}^{(t)} by using information from market 𝒳\displaystyle\mathcal{X}, we select n\displaystyle n stocks, i.e., X1,X2,…,Xn\displaystyle X\_{1},X\_{2},...,X\_{n} from market 𝒳\displaystyle\mathcal{X},
corresponding to those stocks that exhibit the strongest cross-market predictive associations with Yi\displaystyle Y\_{i} according to the t-statistic defined above.
Their daily returns on day t−l\displaystyle t-l are rX1(t−l),rX2(t−l),…,rXn(t−l)\displaystyle r\_{X\_{1}}^{(t-l)},r\_{X\_{2}}^{(t-l)},...,r\_{X\_{n}}^{(t-l)}. The data used for training and prediction are illustrated in Figure [6](#S4.F6 "Figure 6 ‣ 4.2 Predictive Analysis with Machine Learning ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting").
All predictor selection is performed within the rolling training window to avoid look-ahead bias.

![Refer to caption](2603.10559v1/my_plots/regression_data_4.png)


Figure 6: Schematic illustration of the rolling training and prediction framework. For each target stock Yi\displaystyle Y\_{i}, returns over the look-back window [t−w,t−1]\displaystyle[t-w,t-1] are regressed on lagged source-market returns over [t−l−w,t−l−1]\displaystyle[t-l-w,t-l-1]. The bottom row represents the out-of-sample prediction of rYi(t)\displaystyle r\_{Y\_{i}}^{(t)} using source returns observed at t−l\displaystyle t-l, thereby preserving temporal ordering and eliminating look-ahead bias.

The U.S. market is open from 9:30am to 4:00pm U.S. Eastern Time (ET), while the Chinese market is open from 9:30am to 11:30am, and 1:00pm to 3:00pm China Standard Time (UTC+8). There is no overlap between the two trading periods, as shown in the time zone diagram in Figure [7](#S4.F7 "Figure 7 ‣ 4.2 Predictive Analysis with Machine Learning ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), under the standard time difference. Note that adjusting for daylight saving time does not result in any overlap between the trading sessions. We predict OPCL returns for both countries. We set l=1\displaystyle l=1 when predicting Chinese stocks using the latest information from the U.S. market, and l=0\displaystyle l=0 in the reverse direction.
This timing structure ensures that predictor information from the source market is fully observable prior to the opening of the target market.

![Refer to caption](2603.10559v1/my_plots/timeline.png)


Figure 7: Timeline of opening and closing times for the U.S. and Chinese stock markets. The non-overlapping trading sessions induce a natural temporal ordering of information, with U.S. day t−1\displaystyle t-1 close preceding Chinese day t\displaystyle t trading, and Chinese day t\displaystyle t close preceding U.S. day t\displaystyle t trading.

We build the forecasting model as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rYi(t)=Fi​(rX1(t−l),rX2(t−l),…,rXn(t−l);θ)+ϵi(t).r\_{Y\_{i}}^{(t)}=F\_{i}(r\_{X\_{1}}^{(t-l)},r\_{X\_{2}}^{(t-l)},...,r\_{X\_{n}}^{(t-l)};\theta)+\epsilon\_{i}^{(t)}. |  | (6) |

Here, the function Fi\displaystyle F\_{i} represents the different machine learning methods we use, and θ\displaystyle\theta refers to the parameters that are estimated for each machine learning model. The aim is to identify a model that can generate accurate out-of-sample predictions of rYi(t)\displaystyle r\_{Y\_{i}}^{(t)} so that a high SR can be achieved.

We applied a total of ten machine learning models to forecast returns. They include: Ordinary Least Squares (OLS), Least Absolute Shrinkage and Selection Operator (LASSO), Ridge Regression (RIDGE), Support Vector Machine (SVM), Extreme Gradient Boosting (XGBoost), Light Gradient Boosting Machine (LGBM), Random Forests (RF), Adaptive Boosting (AdaBoost), ensemble by results average (ensemble-avg) and ensemble by results median (ensemble-med). This range of models spans linear, regularized, kernel-based, tree-based, and ensemble approaches, allowing us to assess whether cross-market predictive gains depend on model class or are robust across specifications. We describe each model in detail below. All models are estimated within each rolling training window and evaluated out-of-sample to ensure temporal validity.

* •

  Ordinary Least Squares (OLS):
  The main idea of OLS is to estimate regression coefficients by choosing parameter values that minimize the sum of squared residuals between observed and predicted values. Specifically, the model is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | rYi(t)=αi+∑j=1nβi​j​rXj(t−l)+ϵi(t).r\_{Y\_{i}}^{(t)}=\alpha\_{i}+\sum\_{j=1}^{n}\beta\_{ij}r\_{X\_{j}}^{(t-l)}+\epsilon\_{i}^{(t)}. |  | (7) |

  The linear model is fit with an objective of minimizing the residual sum of squares (RSS):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | minαi,𝒘⁡‖𝒚−αi​𝟏−𝐗​𝒘‖22.\min\_{\alpha\_{i},\bm{w}}\left\|\bm{y}-\alpha\_{i}\bm{1}-\mathbf{X}\bm{w}\right\|\_{2}^{2}. |  | (8) |

  𝒚∈ℝd\displaystyle\bm{y}\in\mathbb{R}^{d} is the vector of returns corresponding to rYi(t)\displaystyle r\_{Y\_{i}}^{(t)}, 𝐗∈ℝd×n\displaystyle\mathbf{X}\in\mathbb{R}^{d\times n} is the matrix of predictors where each row is [rX1(t−l),…,rXn(t−l)]\displaystyle[r\_{X\_{1}}^{(t-l)},\dots,r\_{X\_{n}}^{(t-l)}], and 𝒘=[βi​1,…,βi​n]⊤\displaystyle\bm{w}=[\beta\_{i1},\dots,\beta\_{in}]^{\top} is the associated coefficient vector. Here d=w\displaystyle d=w, which is the length of training window, i.e., the number of time points.
* •

  Least Absolute Shrinkage and Selection Operator (LASSO):
  The OLS method often leads to low bias but high variance (hastie2009elements). Shrinkage methods are introduced to mitigate this problem, and LASSO is one of them. It uses ℓ1\displaystyle\ell\_{1}-norm regularization to impose a penalty on the size of regression coefficients (hastie2009elements). The objective function is given by:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | minαi,𝒘⁡(12​d​‖𝒚−αi​𝟏−𝐗​𝒘‖22+λ​‖𝒘‖1).\min\_{\alpha\_{i},\bm{w}}\left(\frac{1}{2d}\left\|\bm{y}-\alpha\_{i}\bm{1}-\mathbf{X}\bm{w}\right\|\_{2}^{2}+\lambda\|\bm{w}\|\_{1}\right). |  | (9) |

  Here λ\displaystyle\lambda is the regularization parameter.
* •

  Ridge Regression (RIDGE):
  RIDGE is another type of shrinkage method. It adds ℓ2\displaystyle\ell\_{2}-norm regularization to the linear least squares loss function. The objective function is given by:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | minαi,𝒘⁡(‖𝒚−αi​𝟏−𝐗​𝒘‖22+λ​‖𝒘‖22).\min\_{\alpha\_{i},\bm{w}}\left(\left\|\bm{y}-\alpha\_{i}\bm{1}-\mathbf{X}\bm{w}\right\|\_{2}^{2}+\lambda\|\bm{w}\|\_{2}^{2}\right). |  | (10) |
* •

  Support Vector Machine (SVM):
  SVMs can tackle complex learning problems while retaining the analytical simplicity of linear models. With kernel functions, this method avoids direct computation in high-dimensional spaces, enabling nonlinear learning using a linear algorithm in the feature space (hearst1998support). We use the radial basis function kernel throughout our experiment. The goal is to minimize the following dual optimization problem with respect to the Lagrange multipliers:

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | min𝜶\displaystyle\min\_{\bm{\alpha}} | 12​∑j=1n∑k=1nαj​αk​yj​yk​K​(𝒙j,𝒙k)−∑j=1nαj\displaystyle\frac{1}{2}\sum\_{j=1}^{n}\sum\_{k=1}^{n}\alpha\_{j}\alpha\_{k}y\_{j}y\_{k}{K(\bm{x}\_{j},\bm{x}\_{k})}-\sum\_{j=1}^{n}\alpha\_{j} |  | (11) |
  |  | s.t. | ∑j=1nαj​yj=0\displaystyle\sum\_{j=1}^{n}\alpha\_{j}y\_{j}=0 |  |
  |  |  | 0≤αj≤C,j=1,2,…,n.\displaystyle 0\leq\alpha\_{j}\leq C,\quad j=1,2,\dots,n. |  |

  Here αj\displaystyle\alpha\_{j} is the Lagrange multiplier, C\displaystyle C is a hyperparameter that controls the trade-off between the flatness of the function and the amount by which deviations larger than ϵ\displaystyle\epsilon are tolerated, K​(𝒙j,𝒙k)\displaystyle K(\bm{x}\_{j},\bm{x}\_{k}) is the kernel function, yj\displaystyle y\_{j} is rYi(t−w+j−1)\displaystyle r\_{Y\_{i}}^{(t-w+j-1)} in the training window, and 𝒙j\displaystyle\bm{x}\_{j} is its corresponding vector of predictors [rX1(t−w+j−1−l),…,rXn(t−w+j−1−l)]⊺\displaystyle[r\_{X\_{1}}^{(t-w+j-1-l)},\dots,r\_{X\_{n}}^{(t-w+j-1-l)}]^{\intercal}.
* •

  Extreme Gradient Boosting (XGBoost):
  XGBoost is a scalable end-to-end tree boosting method (chen2016xgboost). It implements parallel and distributed computing to accelerate training. The model is defined by the following equation:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | y^j=ϕ​(𝒙j)=∑kfk​(𝒙j),fk∈ℱ,\hat{y}\_{j}=\phi(\bm{x}\_{j})=\sum\_{k}f\_{k}(\bm{x}\_{j}),\quad f\_{k}\in\mathcal{F}, |  | (12) |

  where ℱ\displaystyle\mathcal{F} is the space of regression trees, and fk\displaystyle f\_{k} is one independent tree. The objective function is given by:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | min​∑jl​(y^j,yj)+∑kΩ​(fk),\min{\sum\_{j}l(\hat{y}\_{j},y\_{j})+\sum\_{k}\Omega(f\_{k})}, |  | (13) |

  where

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Ω​(f)=γ​M+12​λ​‖w‖2.\Omega(f)=\gamma M+\frac{1}{2}\lambda\|w\|^{2}. |  | (14) |

  Here l\displaystyle l is a differentiable convex loss function, Ω​(f)\displaystyle\Omega(f) is the regularization term, M\displaystyle M is the number of leaves, w\displaystyle w is the leaf weight, and γ\displaystyle\gamma and λ\displaystyle\lambda are the corresponding regularization parameters.
* •

  Light Gradient Boosting Machine (LGBM):
  LGBM is another gradient boosting method that improves computational efficiency compared with standard gradient boosting tree algorithms (ke2017lightgbm). Two key techniques employed by LGBM are Gradient-Based One-Side Sampling and Exclusive Feature Bundling. The former retains instances with large gradients and randomly samples those with small gradients. The latter combines mutually exclusive sparse features, which never take nonzero values at the same time, into a single combined feature, effectively reducing computational complexity (ke2017lightgbm).
* •

  Random Forests (RF):
  Random forests consist of an ensemble of decision trees. At each node of each tree, the algorithm randomly selects a subset of features to consider for splitting. Each tree is grown using bootstrap sampling of the data (breiman2001random). By combining these de-correlated trees, the final prediction is obtained by averaging their outputs (hastie2009elements).
* •

  Adaptive Boosting (AdaBoost):
  AdaBoost combines multiple weak learners to form a strong learner. Each weaker learner is trained to correct the errors made by the previous learners. The algorithm iteratively reweights training observations based on their absolute prediction errors, so that more emphasis is given to instances with larger errors from earlier learners. The final prediction is obtained by aggregating the weak learners, summing their probabilistic predictions (freund1997decision). We choose a decision tree regressor as the base learner in our experiment.
* •

  Ensemble by results average (ensemble-avg):
  For each stock and each day, we take the average of the prediction results from the eight methods above as the final output.
* •

  Ensemble by results median (ensemble-med):
  Similar to ensemble-avg, we take the median of the prediction results from the eight methods as the final output for each stock on each day.

## 5 Experiments

In this section, we conduct an extensive set of experiments to evaluate the cross-market predictability of individual stock returns and examine the economic relevance of the proposed graph-based framework.
All results are obtained using a rolling-window estimation scheme and evaluated strictly out-of-sample.

### 5.1 Evaluation Metrics

We use Profit and Loss (PnL) and Sharpe Ratio (SR) to evaluate the performance of forecasting methods. We abstract from liquidity-optimized portfolio construction and explicit transaction cost modeling, and therefore interpret reported SRs as pre-cost measures of predictive strength rather than implementable performance.

* •

  Profit and Loss (PnL):
  The PnL on day t\displaystyle t is calculated with the following equation:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | P​n​L(t)=∑isign​(si(t))⋅ri(t)⋅bi(t).PnL^{(t)}=\sum\_{i}\text{sign}(s\_{i}^{(t)})\cdot r\_{i}^{(t)}\cdot b\_{i}^{(t)}. |  | (15) |

  Here si(t)\displaystyle s\_{i}^{(t)} denotes the predicted return of stock i\displaystyle i on day t\displaystyle t, and ri(t)\displaystyle r\_{i}^{(t)} denotes the actual return of stock i\displaystyle i on day t\displaystyle t. bi(t)=min⁡(0.001×m​d​vi(21),L)\displaystyle b\_{i}^{(t)}=\min(0.001\times mdv\_{i}^{(21)},L) is the amount of capital deployed on stock i\displaystyle i, where m​d​vi(21)\displaystyle mdv\_{i}^{(21)} denotes the median daily traded volume of stock i\displaystyle i over the 21-day interval preceding day t\displaystyle t, and L\displaystyle L is the maximum limit to the bid. The parameter L\displaystyle L controls the maximum position size.
  This position-sizing rule serves as a coarse liquidity proxy, limiting exposure in less actively traded names.
  Throughout our experiment, L\displaystyle L is set to 100,000 USD for the U.S. market prediction and 1,500,000 CNY for the Chinese market prediction.
* •

  Sharpe Ratio (SR):
  After computing daily PnLs of all stocks, we calculate the mean and standard deviation of the daily PnL vector with length T\displaystyle T, denoted as μP​n​L(T)\displaystyle\mu\_{PnL}^{(T)} and σP​n​L(T)\displaystyle\sigma\_{PnL}^{(T)}, where T\displaystyle T is the length of predicting period in our experiment. The annualized SR is given by:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | S​R=μP​n​L(T)σP​n​L(T)⋅252.SR=\frac{\mu\_{PnL}^{(T)}}{\sigma\_{PnL}^{(T)}}\cdot\sqrt{252}. |  | (16) |

  Here the scaling accounts for the fact that there are 252 trading days in a calendar year and annualizes daily PnL variability.

Several practical limitations should be noted. First, the graph is obtained via large-scale pairwise screening and therefore may include spurious edges in the presence of multiple testing.
Second, our economic evaluation abstracts from transaction costs, market impact, short-sale constraints, and other trading frictions, so reported SRs reflect pre-cost predictive performance.
Third, we do not implement liquidity-weighted portfolio construction or dynamic capacity controls; position sizes are capped but not optimized with respect to market depth. Consequently, the trading design is stylized rather than fully implementable. As emphasized by cartea2025liquidity, ignoring stock-level capacity constraints can substantially overstate the implementable value of predictive strategies. Our objective is to isolate and quantify directional cross-market predictive asymmetries rather than to construct a production-ready trading strategy.

### 5.2 Experimental Setup

We use a 250-day training window and update both the graphs and the predictive models every 10 days. Prediction begins on the first trading day of 2016 and ends on the last trading day of 2021. All models are re-estimated using a rolling-window scheme to ensure strict out-of-sample evaluation and avoid look-ahead bias.

#### 5.2.1  Graph-Based Cross-Market Prediction

* •

  Predicting the Chinese Market with the U.S. market:
  We let market 𝒳\displaystyle\mathcal{X} denote the U.S. market, and market 𝒴\displaystyle\mathcal{Y} denote the Chinese market. We use the most recent available U.S. returns as predictors to forecast Chinese returns, i.e., l=1\displaystyle l=1, reflecting the non-overlapping trading sessions and the temporal ordering of information flow.
* •

  Predicting the U.S. Market with the Chinese market:
  We let market 𝒳\displaystyle\mathcal{X} denote the Chinese market, and market 𝒴\displaystyle\mathcal{Y} denote the U.S. market. We also use the most recent available returns for forecasting, i.e., l=0\displaystyle l=0, since Chinese trading concludes before the U.S. market opens on the same calendar day.

#### 5.2.2  Baseline

* •

  Non-Graph-Based Same-Market Baseline:
  For each target stock, the previous 25 days of daily return data are used as predictive features. The training window remains 250 days and models are updated every 10 days to ensure comparability with the graph-based specifications.
  This baseline model can be described with the following equation:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | rYi(t)=Fi​(rYi(t−25),rYi(t−24),…,rYi(t−1);θ)+ϵi(t).r\_{Y\_{i}}^{(t)}=F\_{i}(r\_{Y\_{i}}^{(t-25)},r\_{Y\_{i}}^{(t-24)},...,r\_{Y\_{i}}^{(t-1)};\theta)+\epsilon\_{i}^{(t)}. |  | (17) |

  Note that the predictive features rYi(t−25),rYi(t−24),…,rYi(t−1)\displaystyle r\_{Y\_{i}}^{(t-25)},r\_{Y\_{i}}^{(t-24)},...,r\_{Y\_{i}}^{(t-1)} can be either all pvCLCL returns or all OPCL returns, while rYi(t)\displaystyle r\_{Y\_{i}}^{(t)} is an OPCL return.
* •

  Graph-Based Same-Market Baseline: Based on the methodology described in Section [4.1](#S4.SS1 "4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), this baseline sets markets 𝒳\displaystyle\mathcal{X} and 𝒴\displaystyle\mathcal{Y} identical, so that for each stock its predictors are drawn from the same market. The return values of predictors are one-day ahead of the response values, i.e., l=1\displaystyle l=1. This specification isolates the incremental contribution of cross-market information relative to graph-based modeling per se.

### 5.3 Main Results

We begin by evaluating the economic performance of the cross-market forecasting framework. Portfolio sorts based on model-implied signals are standard in the return predictability literature. For each day t\displaystyle t, stocks are ranked by the absolute value of their predicted returns, |r^i(t)|\displaystyle|\hat{r}\_{i}^{(t)}|. To examine how performance varies with signal strength, we construct six nested quantile portfolios:

* •

  quantile 1 (qr1): all stocks;
* •

  quantile 2 (qr2): top 80% of stocks ranked by |r^i(t)|\displaystyle|\hat{r}\_{i}^{(t)}|;
* •

  quantile 3 (qr3): top 60%;
* •

  quantile 4 (qr4): top 40%;
* •

  quantile 5 (qr5): top 20%;
* •

  quantile 6 (qr6): top 10%.

These portfolios are nested, so that qr6⊂qr5⊂qr4⊂qr3⊂qr2⊂qr1\displaystyle\text{qr6}\subset\text{qr5}\subset\text{qr4}\subset\text{qr3}\subset\text{qr2}\subset\text{qr1}. This construction allows us to assess whether stronger model signals translate into improved risk-adjusted performance.
Importantly, the ranking at day t\displaystyle t is based solely on model predictions available at that date and does not use realized returns, thereby avoiding look-ahead bias in portfolio formation. We first document that cross-market information and graph-based modeling contribute to improved forecasting performance.

![Refer to caption](2603.10559v1/my_plots/US_x-ChinaML_y_new_top500_pvCLCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(a) Predictors: U.S. pvCLCL returns.

![Refer to caption](2603.10559v1/my_plots/US_x-ChinaML_y_new_top500_OPCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(b) Predictors: U.S. OPCL returns.

Figure 8: Sharpe Ratios for forecasting Chinese OPCL returns using U.S. pvCLCL and OPCL returns as predictors.

Figure [8](#S5.F8 "Figure 8 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") and Figure [9](#S5.F9 "Figure 9 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") display the results of forecasting in two different directions. According to Figure [8](#S5.F8 "Figure 8 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), when predicting Chinese stocks with U.S. stocks, RIDGE, LGBM, ensemble-avg and ensemble-med yield strong performance. SVM appears less effective for this task, since its SRs are mostly lower than one. For other forecasting methods and most quantiles, SRs exceed one, with some approaching two. Notably, the ensemble-average and ensemble-median methods maintain robust and stable performance, often comparable to the best individual models, highlighting the benefit of model diversification. Using U.S. pvCLCL returns as features performs better than using the U.S. OPCL returns to predict Chinese OPCL returns. The cumulative PnL plots of each method for the former are shown in Figure [10](#S5.F10 "Figure 10 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), where the upward-sloping trajectories indicate economically meaningful profitability.

In contrast, as shown in Figure [9](#S5.F9 "Figure 9 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), when predicting the U.S. stocks with Chinese stocks, SRs are substantially lower across methods and quantiles. Therefore the Chinese market exerts weaker predictive influence than the U.S. market in cross-market return prediction. Since the performance is stronger when predicting Chinese stocks using U.S. pvCLCL returns, we focus on this setting in subsequent experiments and analyses.

![Refer to caption](2603.10559v1/my_plots/ChinaML_x-US_y_new_top500_pvCLCL_MR-OPCL_MR_betl100000_SR_heatmap.jpg)


(a) Predictors: Chinese pvCLCL returns.

![Refer to caption](2603.10559v1/my_plots/ChinaML_x-US_y_new_top500_OPCL_MR-OPCL_MR_betl100000_SR_heatmap.jpg)


(b) Predictors: Chinese OPCL returns.

Figure 9: Sharpe Ratios for forecasting U.S. OPCL returns using Chinese returns as predictors.

![Refer to caption](2603.10559v1/my_plots/new_OLS_LASSO_RIDGE_SVM_XGBoost_LGBM_RF_AdaBoost_ensemble-avg_ensemble-med_top500_pvCLCL_MR-OPCL_MR_betl1500000_cumulative_PnL-sum_plot.png)


Figure 10: Cumulative daily Profit and Loss (PnL) from forecasting Chinese OPCL returns using U.S. pvCLCL returns as predictors. Each panel corresponds to a different machine learning model, and coloured curves represent nested quantile portfolios ranked by the absolute value of predicted returns.

Figure [11](#S5.F11 "Figure 11 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") shows the results of predicting Chinese stocks with Chinese stocks based on graph structures. Figure [12](#S5.F12 "Figure 12 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") summarizes SRs across specifications, comparing graph-based cross-market approaches, graph-based single-market approaches, and the non-graph-based baseline, with pvCLCL returns used as predictors. Figure [13](#S5.F13 "Figure 13 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") reports the corresponding performance differentials (deltas), computed as SRs of graph-based approaches minus those of the non-graph-based baseline. The results indicate that graph-based same-market approaches outperform non-graph-based same-market approaches for most machine learning models under most quantiles, especially for OLS, LGBM, and qr5.

Turning to the incremental value of cross-market information, combining cross-market information with graph information yields the strongest overall performance, outperforming approaches that use graph structures with same-market information only, as well as the non-graph-based baseline relying solely on same-market information.

![Refer to caption](2603.10559v1/my_plots/ChinaML_x-ChinaML_y_new_top500_pvCLCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(a) Predictors: Chinese pvCLCL returns.

![Refer to caption](2603.10559v1/my_plots/ChinaML_x-ChinaML_y_new_top500_OPCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(b) Predictors: Chinese OPCL returns.

Figure 11: Sharpe Ratios for forecasting Chinese OPCL returns using Chinese returns as predictors.

![Refer to caption](2603.10559v1/my_plots/opt3_new4_grouped_bar_SR_top500_pvCLCL_MR-OPCL_MR.jpg)


Figure 12: Comparison of Sharpe Ratios across graph-based cross-market, graph-based same-market, and non-graph-based baseline specifications, using pvCLCL returns as predictors. CN-CN denotes using Chinese stocks to forecast Chinese stocks, while US-CN denotes using U.S. stocks to forecast Chinese stocks.

![Refer to caption](2603.10559v1/my_plots/opt2_new3_delta_heatmap_SR_top500_pvCLCL_MR-OPCL_MR.jpg)


Figure 13: Performance differentials (Sharpe Ratio deltas) relative to the non-graph-based baseline, using pvCLCL returns as predictors. US-CN denotes using U.S. stocks to forecast Chinese stocks, while CN-CN denotes using Chinese stocks to forecast Chinese stocks.

### 5.4 Sensitivity Analysis

We next evaluate the robustness of predictive performance to perturbations in graph structure and temporal alignment when forecasting Chinese returns using U.S. pvCLCL returns.
We first conduct a feature-replacement test, where selected informative stocks are randomly substituted with other stocks. Additionally, we assess temporal sensitivity by varying the recency of input data, using features from earlier days (e.g., t−2\displaystyle t-2, t−3\displaystyle t-3, etc.) instead of the most recent day t−1\displaystyle t-1.

First, we conduct a feature-replacement experiment. Based on graphs built for predicting returns on day t\displaystyle t in the Chinese market using returns on day t−1\displaystyle t-1 in the U.S. market, we maintain the same in-degree of each target node to preserve graph sparsity while randomly changing some of their connections. Only previously unconnected nodes are considered as replacements for the original connections. We randomly replace 20%, 40%, 60%, 80% and all of the edges. For each quantile level, we obtain the median of the results from all the 10 methods.

As shown in Figure [14(a)](#S5.F14.sf1 "Figure 14(a) ‣ Figure 14 ‣ 5.4 Sensitivity Analysis ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), SRs generally decline as a larger fraction of edges is replaced, indicating that predictive gains depend critically on the economically meaningful structure captured by the graph rather than on generic diversification effects. The deterioration is strongest in lower and intermediate quantiles, whereas the highest quantile (qr6) exhibits comparatively greater resilience.

Second, we assess temporal sensitivity by varying the recency of input data. Still based on graphs built for predicting returns on day t\displaystyle t in the Chinese market using returns on day t−1\displaystyle t-1 in the U.S. market, we look into forecasting performance as the temporal gap increases (e.g., two-day, three-day, or longer gaps) between the predictor window and the target return window. As defined in Section [4.2](#S4.SS2 "4.2 Predictive Analysis with Machine Learning ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), when we forecast rYi(t)\displaystyle r\_{Y\_{i}}^{(t)}, the predictors are given by [rX1(t−l),rX2(t−l),…,rXn(t−l)]\displaystyle[r\_{X\_{1}}^{(t-l)},r\_{X\_{2}}^{(t-l)},...,r\_{X\_{n}}^{(t-l)}]. Here we set l=2,3,…\displaystyle l=2,3,... when predicting Chinese stocks. For each quantile level, we also obtain the median of the results from all the 10 methods.

Figure [14(b)](#S5.F14.sf2 "Figure 14(b) ‣ Figure 14 ‣ 5.4 Sensitivity Analysis ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") shows that SRs generally decline as l\displaystyle l increases, consistent with the hypothesis that cross-market predictive content decays with time. The decline is again less pronounced for qr6, suggesting that large-magnitude signals may capture more persistent cross-market effects. A mild stabilization beyond Lag 4 likely reflects weekly trading-cycle effects.

Taken together, these experiments confirm that predictive performance depends critically on both the structural accuracy of the graph and the recency of cross-market information.

![Refer to caption](2603.10559v1/my_plots/new2med_randedge_SR_top500_pvCLCL_MR-OPCL_MR_perf_comparison_general.jpg)


(a) Effect of graph randomization (fraction of edges replaced).

![Refer to caption](2603.10559v1/my_plots/abla_new2med_SR_top500_pvCLCL_MR-OPCL_MR_perf_comparison_general.jpg)


(b) Effect of increasing temporal lag l\displaystyle l.

Figure 14: Median forecasting performance under graph randomization (a) and increasing temporal lag (b).
Panel (a) reports Sharpe Ratios as a function of the fraction of replaced edges while preserving in-degree.
Panel (b) reports Sharpe Ratios as the lag parameter l\displaystyle l increases, measuring the effect of input recency.

## 6 Conclusion and Future Research

This paper investigates cross-market return forecasting at the individual stock level. We develop a graph-based architecture that enables structured information transmission across markets and use it to construct cross-market predictive features. Building on this framework, we implement a range of machine learning models to forecast OPCL returns for each stock.

Empirically, we find that combining cross-market information with graph-based feature selection delivers superior performance relative to both graph-based same-market approaches and non-graph-based baselines. The predictive relationship is asymmetric: U.S. stocks are substantially more informative for forecasting Chinese returns than the reverse. In particular, U.S. pvCLCL returns exhibit stronger predictive power for Chinese OPCL returns than U.S. OPCL returns, highlighting the importance of overnight information transmission. Sensitivity analyses confirm that preserving the economically meaningful bipartite graph structure is crucial for achieving strong risk-adjusted performance. Moreover, forecasting performance deteriorates as the temporal gap between predictor and target returns widens, emphasizing the value of recency.

Several directions for future research emerge. First, extending the analysis to additional regions, including European and other Asian markets, would help assess the generalizability of cross-market predictive linkages. Second, GNNs could be applied directly to the constructed bipartite graph to learn nonlinear cross-market dependencies. Finally, recent advances in time-series-specialized large language models may offer an alternative framework for modeling structured cross-market interactions.

## Conflicts of Interest

The authors declare that they have no competing interests.

## References

## Appendix A Hyperparameter Settings

The OLS method does not involve any hyperparameters.
Table [A.1](#A1.T1 "Table A.1 ‣ Appendix A Hyperparameter Settings ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") reports the performance of the remaining seven machine learning models under alternative hyperparameter configurations.
The SVM model appears relatively insensitive to variations in hyperparameter values, and its SRs remain generally below one across specifications, suggesting limited suitability for this particular forecasting setting.
For the other models, SRs exceed one across most quantiles and hyperparameter choices, indicating that the cross-market forecasting framework delivers robust risk-adjusted performance and is not overly sensitive to specific tuning parameters.

Table A.1: Summary of SR results across different hyperparameter settings (using the most recent U.S. pvCLCL returns to predict Chinese OPCL returns). Values are reported as mean ±\displaystyle\pm standard deviation.

| Methods | Parameters | qr1 | qr2 | qr3 | qr4 | qr5 | qr6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LASSO | λ\displaystyle\lambda={1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000} | 0.848±0.222\displaystyle 0.848\pm 0.222 | 0.969±0.247\displaystyle 0.969\pm 0.247 | 1.238±0.31\displaystyle 1.238\pm 0.31 | 1.65±0.398\displaystyle 1.65\pm 0.398 | 1.821±0.433\displaystyle 1.821\pm 0.433 | 1.777±0.424\displaystyle 1.777\pm 0.424 |
| RIDGE | λ\displaystyle\lambda={1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100, 1000} | 1.238±0.429\displaystyle 1.238\pm 0.429 | 1.293±0.43\displaystyle 1.293\pm 0.43 | 1.437±0.449\displaystyle 1.437\pm 0.449 | 1.715±0.51\displaystyle 1.715\pm 0.51 | 1.668±0.619\displaystyle 1.668\pm 0.619 | 1.55±0.461\displaystyle 1.55\pm 0.461 |
| SVM | C\displaystyle C={0.1, 1, 10, 100, 1000} | 0.743±0.194\displaystyle 0.743\pm 0.194 | 0.751±0.196\displaystyle 0.751\pm 0.196 | 0.782±0.204\displaystyle 0.782\pm 0.204 | 0.719±0.188\displaystyle 0.719\pm 0.188 | 1.02±0.267\displaystyle 1.02\pm 0.267 | 0.836±0.218\displaystyle 0.836\pm 0.218 |
| XGBoost | |  | | --- | | max\_depth = {3,6,9} | | learning\_rate = {0.01, 0.1, 0.2} | | n\_estimators = {50, 100, 300} | | 1.445±0.224\displaystyle 1.445\pm 0.224 | 1.48±0.247\displaystyle 1.48\pm 0.247 | 1.587±0.214\displaystyle 1.587\pm 0.214 | 1.539±0.309\displaystyle 1.539\pm 0.309 | 1.381±0.401\displaystyle 1.381\pm 0.401 | 0.964±0.233\displaystyle 0.964\pm 0.233 |
| LGBM | |  | | --- | | num\_leaves = {10, 31, 90} | | learning\_rate = {0.01, 0.1, 0.2} | | n\_estimators = {50, 100, 300} | | 1.32±0.348\displaystyle 1.32\pm 0.348 | 1.457±0.388\displaystyle 1.457\pm 0.388 | 1.541±0.422\displaystyle 1.541\pm 0.422 | 1.44±0.485\displaystyle 1.44\pm 0.485 | 1.652±0.466\displaystyle 1.652\pm 0.466 | 1.424±0.407\displaystyle 1.424\pm 0.407 |
| RF | |  | | --- | | n\_estimators = {50, 100, 300} | | max\_depth = {5, 10, 50} | | 1.481±0.41\displaystyle 1.481\pm 0.41 | 1.558±0.422\displaystyle 1.558\pm 0.422 | 1.639±0.447\displaystyle 1.639\pm 0.447 | 1.799±0.486\displaystyle 1.799\pm 0.486 | 1.747±0.474\displaystyle 1.747\pm 0.474 | 1.09±0.351\displaystyle 1.09\pm 0.351 |
| AdaBoost | |  | | --- | | max\_depth = {1, 5, 10} | | n\_estimators = {50, 100, 300} | | learning\_rate = {0.01, 0.1, 0.2} | | 1.389±0.358\displaystyle 1.389\pm 0.358 | 1.405±0.385\displaystyle 1.405\pm 0.385 | 1.549±0.436\displaystyle 1.549\pm 0.436 | 1.548±0.419\displaystyle 1.548\pm 0.419 | 1.1±0.305\displaystyle 1.1\pm 0.305 | 0.667±0.187\displaystyle 0.667\pm 0.187 |

* •

  Note: max\_depth is the maximum depth of a tree.
  learning\_rate is the learning rate.
  n\_estimators is the maximum number of estimators at which boosting is terminated.
  num\_leaves is maximum tree leaves for base learners in an LGBM model.

## Appendix B Comparison with Baselines when Predicting with OPCL Returns

Similar to Figure [12](#S5.F12 "Figure 12 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") and Figure [13](#S5.F13 "Figure 13 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"), Figure [B.1](#A2.F1 "Figure B.1 ‣ Appendix B Comparison with Baselines when Predicting with OPCL Returns ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") and Figure [B.2](#A2.F2 "Figure B.2 ‣ Appendix B Comparison with Baselines when Predicting with OPCL Returns ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting") report the performance comparison among the graph-based cross-market approach, the graph-based same-market baseline, and the non-graph-based baseline when OPCL returns are used as predictors.

The results indicate that incorporating graph structure generally improves forecasting performance across most quantiles and machine learning models. However, in contrast to the pvCLCL setting, the incremental contribution of cross-market information is substantially weaker when OPCL returns are used as predictors.

![Refer to caption](2603.10559v1/my_plots/opt3_new4_grouped_bar_SR_top500_OPCL_MR-OPCL_MR.jpg)


Figure B.1: Comparison of Sharpe Ratios across graph-based cross-market, graph-based same-market, and non-graph-based baseline specifications, using OPCL returns as predictors. US-CN denotes using U.S. stocks to forecast Chinese stocks, while CN-CN denotes using Chinese stocks to forecast Chinese stocks.

![Refer to caption](2603.10559v1/my_plots/opt2_new3_delta_heatmap_SR_top500_OPCL_MR-OPCL_MR.jpg)


Figure B.2: Performance differentials (Sharpe Ratio deltas) relative to the non-graph-based baseline, using OPCL returns as predictors. US-CN denotes using U.S. stocks to forecast Chinese stocks, while CN-CN denotes using Chinese stocks to forecast Chinese stocks.

## Appendix C Cross-Market Spillovers under U.S. Market Shocks

To investigate whether cross-market predictability strengthens during periods of heightened U.S. market activity and volatility, we condition the analysis on large movements in the U.S. market. Specifically, we identify days on which the S&P 500 ETF (SPY) exhibits large absolute pvCLCL returns.

We divide the SPY absolute pvCLCL returns into nested quantiles (qr1–qr6), consistent with the earlier quantile construction. For example, qr2 contains the top 80% of days ranked by absolute SPY returns. For each identified SPY shock date ti\displaystyle t\_{i}, we extract the model’s OPCL return forecast for the next trading day ti+1\displaystyle t\_{i}+1 in the Chinese market. We then compute SRs restricted to these subsets of dates. This conditional evaluation allows us to assess whether predictive performance improves during periods of elevated U.S. market volatility, when cross-market information transmission is likely to be stronger.

The results are shown in Figure [C.1](#A3.F1 "Figure C.1 ‣ Appendix C Cross-Market Spillovers under U.S. Market Shocks ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"). Nonlinear ensemble models such as XGBoost, LGBM, RF, and AdaBoost achieve consistently high SRs across quantiles, especially in the upper ranges (qr4–qr6), suggesting that nonlinear models capture state-dependent spillover effects more effectively. OLS also performs well, achieving its highest SR in qr6. In contrast, LASSO and SVM exhibit weaker performance, with SRs turning negative in some quantiles, while RIDGE shows comparatively unstable performance.

![Refer to caption](2603.10559v1/my_plots/US_x-ChinaML_y_new_top500_pvCLCL_MR-OPCL_MR_betl1500000_SR_heatmap_5__in_SPY_bucket.jpg)


Figure C.1: Sharpe Ratios of forecasting models conditional on SPY absolute pvCLCL return nested quantiles, measuring predictive performance following different magnitudes of U.S. market shocks.

## Appendix D Comparison of Sharpe Ratio Results across Sectors

We continue to focus on the setting in which U.S. pvCLCL returns are used to forecast Chinese OPCL returns. The sector-level SR results are reported in Figure [D.1](#A4.F1 "Figure D.1 ‣ Appendix D Comparison of Sharpe Ratio Results across Sectors ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"). Because the number of stocks varies across sectors, these results should be interpreted with caution. Overall, the technology and consumer defensive sectors exhibit relatively higher SRs compared with other sectors, indicating stronger cross-market predictive effects in these segments.

![Refer to caption](2603.10559v1/my_plots/US_x-ChinaML_y_new_top500_pvCLCL_MR-OPCL_MR_betl1500000_SR_heatmap_4__in_sec.jpg)


Figure D.1: Sector-level Sharpe Ratios for cross-market forecasting (using U.S. pvCLCL returns to forecast Chinese OPCL returns).

## Appendix E Predicting Chinese Stocks Using Both U.S. and Chinese Stocks

We extend the analysis by allowing the predictor set 𝒳\displaystyle\mathcal{X} to include all stocks from both the U.S. and Chinese markets, while the target set 𝒴\displaystyle\mathcal{Y} continues to consist of Chinese stocks only. The graph construction phase follows the procedure introduced in Section [4.1](#S4.SS1 "4.1 Directed Bipartite Graph ‣ 4 Methodology ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"). The results are presented in Figure [E.1](#A5.F1 "Figure E.1 ‣ Appendix E Predicting Chinese Stocks Using Both U.S. and Chinese Stocks ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting"). In several specifications, the resulting SRs exceed those obtained when using only U.S. returns as predictors (Figure [8](#S5.F8 "Figure 8 ‣ 5.3 Main Results ‣ 5 Experiments ‣ A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting")), suggesting that combining domestic and cross-market information can further enhance predictive performance.

![Refer to caption](2603.10559v1/my_plots/US+ChinaML_x-ChinaML_y_new_top500_pvCLCL_MR_pvCLCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(a) U.S. pvCLCL + Chinese pvCLCL returns.

![Refer to caption](2603.10559v1/my_plots/US+ChinaML_x-ChinaML_y_new_top500_pvCLCL_MR_OPCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(b) U.S. pvCLCL + Chinese OPCL returns.

![Refer to caption](2603.10559v1/my_plots/US+ChinaML_x-ChinaML_y_new_top500_OPCL_MR_pvCLCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(c) U.S. OPCL + Chinese pvCLCL returns.

![Refer to caption](2603.10559v1/my_plots/US+ChinaML_x-ChinaML_y_new_top500_OPCL_MR_OPCL_MR-OPCL_MR_betl1500000_SR_heatmap.jpg)


(d) U.S. OPCL + Chinese OPCL returns.

Figure E.1: Sharpe Ratios for forecasting Chinese OPCL returns when the predictor set includes both U.S. and Chinese stocks. Panels vary the combination of pvCLCL and OPCL features across the two markets.

BETA