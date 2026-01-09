---
authors:
- Vrinda Dhingra
- Amita Sharma
- Anubha Goel
doc_id: arxiv:2601.03927v1
family_id: arxiv:2601.03927
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A comprehensive review and analysis of different modeling approaches for financial
  index tracking problem
url_abs: http://arxiv.org/abs/2601.03927v1
url_html: https://arxiv.org/html/2601.03927v1
venue: arXiv q-fin
version: 1
year: 2026
---


\fnmVrinda \surDhingra
[vdmath.iitr@gmail.com](mailto:vdmath.iitr@gmail.com)
  
\fnmAmita \surSharma
[amita.sharma@nsut.ac.in](mailto:amita.sharma@nsut.ac.in)
  


[anubha.goel@tuni.fi](mailto:anubha.goel@tuni.fi)

###### Abstract

Index tracking, also known as passive investing, has gained significant traction in financial markets due to its cost-effective and efficient approach to replicating the performance of a specific market index. This review paper provides a comprehensive overview of the various modeling approaches and strategies developed for index tracking, highlighting the strengths and limitations of each approach. We categorize the index tracking models into three broad frameworks: optimization-based models, statistical-based models and machine learning based data-driven approach. A comprehensive empirical study conducted on the S&P 500 dataset demonstrates that the tracking error volatility model under the optimization-based framework delivers the most precise index tracking, the convex co-integration model, under the statistical-based framework achieves the strongest return-risk balance, and the deep neural network with fixed noise model within the data-driven framework provides a competitive performance with notably low turnover and high computational efficiency. By combining a critical review of the existing literature with comparative empirical analysis, this paper aims to provide insights into the evolving landscape of index tracking and its practical implications for investors and fund managers.

###### keywords:

Index tracking, tracking error minimization, tracking portfolio, cardinality constraints, machine learning, deep learning

## 1 Introduction

Fund management (or investment management) is a core function within financial services that professionally manages assets across multiple asset classes to meet stated investment objectives on behalf of investors. Investors include individuals or institutions, such as insurance companies, pension funds, and corporations. Fund management encompasses activities such as asset selection, trading, monitoring, reporting to stakeholders, and internal auditing/governance. The primary objective is to balance capital growth and income over the medium to long term, subject to risk, cost, and regulatory constraints.

Over the past decades, the landscape of investment has evolved significantly, driven by advancements in financial technology, increasing market complexity, and shifting investor preferences. A key dimension of this evolution is the management of portfolios relative to benchmark indices such as the S&P 500 or the Dow Jones Industrial Average (DJIA). Broadly, investment strategies can be classified into two categories: active and passive management and this review focuses on passive index tracking within this taxonomy. To delineate scope, the empirical illustration uses the S&P 500; the modeling frameworks surveyed are general and apply across asset classes. Below is a description of each:

* (a)

  Active management involves a hands-on approach where fund managers actively make decisions about buying and selling securities with the aim to outperform a specific benchmark index. The goal is to generate higher returns than the benchmark by leveraging the manager’s expertise, research, and market insights. Active strategies can range from traditional stock-picking to more structured approaches such as enhanced indexing, which blends benchmark replication with small, tactical deviations aimed at improving return performance.
* (b)

  Passive management seeks to replicate the performance of a benchmark index, typically by holding the same securities in the same weights—or, when full replication is costly, a representative subset that closely approximates the index. The primary objective is to match benchmark returns with lower fees, reduced turnover, and limited risk of underperforming the benchmark. Common passive investment vehicles include index funds and exchange-traded funds (ETFs).

Table 1: Comparison of Active and Passive Management Strategies

| Aspect | Active Management | Passive Management |
| --- | --- | --- |
| Approach | Research and analysis driven | Index replication |
| Goal | Outperform the market | Match market performance |
| Costs | Higher fees due to active trading and research | Lower fees due to minimal trading and research |
| Risk | Potentially higher risk due to market timing | Generally lower risk with broader diversification |
| Risk Exposure | Company and market risk | Market risk |
| Returns | Potential for higher returns | Typically matches market returns |
| Suitable For | Investors seeking above-market returns | Long-term investors seeking market-matching returns |

Table [1](https://arxiv.org/html/2601.03927v1#S1.T1 "Table 1 ‣ 1 Introduction ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") summarizes the key differences between active and passive management across key dimensions. Over the years, passive investing has gained widespread popularity among investors and asset managers due to its simplicity, transparency, stability, and cost-effectiveness (see Figure [1](https://arxiv.org/html/2601.03927v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")). Empirical studies consistently show that a large proportion of actively managed funds fail to outperform their benchmarks over long horizons and net of fees, underscoring the appeal of passive alternatives (Malkiel, [2003](https://arxiv.org/html/2601.03927v1#bib.bib45), Prondzinski and Miller, [2018](https://arxiv.org/html/2601.03927v1#bib.bib52), Anadu et al., [2020](https://arxiv.org/html/2601.03927v1#bib.bib3)). Within this context, index tracking—constructing a portfolio to replicate a benchmark’s risk–return profile while keeping tracking error and tracking difference small—has emerged as one of the most prominent passive investment approaches, offering a systematic and efficient means of replicating benchmark performance.

![Refer to caption](Activepassive-pie.png)


Figure 1: Share of active and passive investment over three decades (Source: Morningstar).

Index tracking portfolios such as index funds (IFs) and exchange-traded funds (ETFs) are the most widely adopted vehicles. An index fund is a pooled investment that mirrors a benchmark’s returns, typically via full or partial replication of its constituents, and prices once per day at net asset value (NAV). ETFs, by contrast, are similar in objective but differ in structure: they trade on stock exchanges throughout the day and use a creation–redemption process that keeps market prices close to NAV. In the market, one can invest in many different types of ETFs such as sector-based IF, broad market IF, market capitalization IF, Equal weighted IF, Smart Beta IF, International IF, and Debt IF among others.

The origins of index tracking are commonly traced to the mid-1970s, when John Bogle of Vanguard Group launched the first index fund in 1976 (Bogle, [2011](https://arxiv.org/html/2601.03927v1#bib.bib10)). Designed to replicate the performance of the S&P 500, this fund provided a simple, low-cost way to obtain diversified exposure to the U.S. equity market. At the time, the concept marked a clear break from prevailing practices that emphasized active management and stock selection. Since then, index tracking has scaled globally, with providers offering products that track domestic and international benchmarks across equities, fixed income, and other asset classes. The product set broadened further with the advent of exchange-traded funds in the 1990s—e.g., the SPDR S&P 500 Trust (SPY) in 1993—followed by regional and single-country exposures such as the U.S.-listed iShares MSCI Germany (EWG), alongside mutual-fund offerings like the Motilal Oswal Nifty 50 Index Fund (India).

The scale of passive investing or index tracking specifically, has expanded markedly worldwide. As shown in Figure [2](https://arxiv.org/html/2601.03927v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"), the number of ETFs increased from 276 in 2003 to 8,754 in 2022 worldwide, reflecting a structural shift toward low-cost, index-based vehicles. In the U.S., the share of actively managed funds declined from 81% in 2010 to 52% in 2023, while index mutual funds and ETFs collectively grew to nearly 60% of the equity fund market.111Source: <https://www.americancentury.com/institutional-investors/insights/has-passive-investing-gotten-too-big/> Parallel growth is evident in emerging economies. For instance, in India, ETF trading volume expanded from about 51 thousand crore INR in FY 2019–20 to 3.83 lakh crore INR in FY 2024–25, a more than sevenfold increase over five years.222Source: <https://www.zerodhafundhouse.com/blog/a-comprehensive-guide-to-exchange-traded-funds-etfs-in-india/> These patterns highlight the global diffusion of passive investing, well established in developed markets and rapidly expanding in developing ones.

![Refer to caption](globalETFs_2024.png)

![Refer to caption](activepassive_distribution.png)

Figure 2: Growth of passive investment over the years. Source: Statista 2025

Who should invest in index tracking portfolio?
Index tracking portfolio aims to track market benchmark index, so their returns point to match those of the underlying index, with small differences due to fees and trading frictions. They are therefore, attractive to investors seeking predictable, broad market exposure with low costs and minimal portfolio management. These strategies offer an accessible and beneficial investment option for every investors, experienced or begineer. Unlike actively managed funds, which typically trade more and incur higher management fees as well as discretionary decisions, index funds are passively managed and provide diversification at scale. Because they are designed to match rather than beat the benchmark, these funds are efficient vehicle for long-term wealth accumulation and are particularly suited for cost-conscious, long-horizon investors or as the core allocation in a diversified equity portfolio. Investors should still expect full market ups and downs—these index trackers are not capital-protected.

How are index tracking portfolios formed?
The development of index tracking as a research area has its roots in the portfolio optimization literature, where the problem was first formalized as minimizing the tracking error between a constructed portfolio and its benchmark index. In practice, index replication can be achieved through two primary approaches: full replication and partial replication. Full replication involves holding all the securities in the benchmark index in the same proportions; it is feasible for narrow, liquid universes but becomes costly for broad indices with many constituents due to transaction, administrative, and liquidity frictions (see Beasley et al. ([2003](https://arxiv.org/html/2601.03927v1#bib.bib8)), Canakgoz and Beasley ([2009](https://arxiv.org/html/2601.03927v1#bib.bib13)) for a discussion).

Consequently, many index-tracking portfolios adopt partial replication, selecting a representative subset of securities to approximate the index. This selection is typically governed by a cardinality constraint that limits the number of assets in the portfolio, reducing trading costs and operational complexity while maintaining close alignment with the benchmark. The inclusion of such constraints renders the problem combinatorial and NP-hard, necessitating advanced computational methods and careful turnover control during rebalancing.

The earliest and most widely adopted formulation measures tracking error as the root mean squared error (RMSE) of excess returns, leading to a least-squares quadratic programming (QP) framework (Beasley et al., [2003](https://arxiv.org/html/2601.03927v1#bib.bib8)). Over time, heuristic and metaheuristic techniques—genetic algorithms, simulated annealing, tabu search—have been proposed to handle these complex formulations efficiently (Beasley et al., [2003](https://arxiv.org/html/2601.03927v1#bib.bib8), Guastaroba and Speranza, [2012](https://arxiv.org/html/2601.03927v1#bib.bib35), Derigs and Nickel, [2003](https://arxiv.org/html/2601.03927v1#bib.bib20), Krink et al., [2009](https://arxiv.org/html/2601.03927v1#bib.bib39), Sant’Anna et al., [2017](https://arxiv.org/html/2601.03927v1#bib.bib62)). For a comprehensive review of heuristic-based methods, see Silva and de Almeida Filho ([2024](https://arxiv.org/html/2601.03927v1#bib.bib65)).

The optimization framework has also been extended through alternative definitions of tracking error, including linear (Rudolf et al., [1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) or absolute deviations (Guastaroba and Speranza, [2012](https://arxiv.org/html/2601.03927v1#bib.bib35)), as well as risk-based measures such as conditional value-at-risk (Goel et al., [2018](https://arxiv.org/html/2601.03927v1#bib.bib28)). These developments aim to balance tractability, interpretability, and robustness—and to mitigate sensitivity to outliers and model misspecification. In parallel, statistical frameworks emerged that leverage relationships between index and constituent returns without necessarily solving a global optimization problem. Regression-based formulations (Canakgoz and Beasley, [2009](https://arxiv.org/html/2601.03927v1#bib.bib13), Li, [2020](https://arxiv.org/html/2601.03927v1#bib.bib43)), regularization techniques (Wu et al., [2014a](https://arxiv.org/html/2601.03927v1#bib.bib76), Fastrich et al., [2014](https://arxiv.org/html/2601.03927v1#bib.bib24)), and cointegration (Sant’Anna et al., [2017](https://arxiv.org/html/2601.03927v1#bib.bib58), [2020b](https://arxiv.org/html/2601.03927v1#bib.bib60)) or factor-based approaches (Corielli and Marcellino, [2006](https://arxiv.org/html/2601.03927v1#bib.bib17)) expanded the toolkit, often yielding sparse, implementable portfolios suitable for high-dimensional settings.

More recently, artificial intelligence techniques have significantly broadened the methodological landscape of index tracking. Neural networks (Ouyang et al., [2019](https://arxiv.org/html/2601.03927v1#bib.bib49), Zheng et al., [2020a](https://arxiv.org/html/2601.03927v1#bib.bib86)), random forests (Yuanyuan Cao and Yang, [2022](https://arxiv.org/html/2601.03927v1#bib.bib80)), and deep autoencoders (Zhang et al., [2020](https://arxiv.org/html/2601.03927v1#bib.bib82)) have been applied to capture complex, nonlinear dependencies between asset and index returns, allowing for more adaptive and potentially more efficient portfolio construction. Dai and Li ([2024](https://arxiv.org/html/2601.03927v1#bib.bib18)) design a deep learning framework that learns dynamic trading policies under benchmark constraints and delivers superior out-of-sample tracking performance on S&P 500 data. Peng et al. ([2023a](https://arxiv.org/html/2601.03927v1#bib.bib50)) frame the problem using reinforcement learning, treating index tracking as an infinite-horizon sequential decision-making task with transaction costs; their deep reinforcement learning (RL) agent outperforms traditional models in long-run tracking accuracy and cost efficiency. Zheng et al. ([2020b](https://arxiv.org/html/2601.03927v1#bib.bib87)) propose a stochastic neural network that incorporates cardinality constraints directly via reparameterization, enabling sparse and realistic index replicating portfolios with state-of-the-art tracking accuracy. In parallel, researchers have explored explainable artificial intelligence (XAI): Zhang and De Smedt ([2024](https://arxiv.org/html/2601.03927v1#bib.bib85)) integrate SHAP (Shapley Additive Explanations) with deep autoencoders to produce interpretable stock selection mechanisms, showing improved performance and model transparency. Attention has also turned to robustness, Bradrania et al. ([2022](https://arxiv.org/html/2601.03927v1#bib.bib12)) introduce market-state aware models that adapt to structural shifts in market regimes, enhancing the resilience of index tracking strategies. These advances exemplify how cutting-edge AI methods—spanning deep learning, reinforcement learning, model interpretability, and adaptive generalization—can improve performance under real-world constraints, aligning index tracking with central challenges in modern AI research such as learning under structure, distributional shift, and constraint-aware inference.

What do we offer in this article for passive management?
In this review, we aim to provide a comprehensive analysis of the modeling approaches for index tracking (IFs/ETFs) developed over the past three decades. From traditional optimization-based methods to recent data-driven techniques, this paper not only chronicles the evolution of index tracking but also empirically evaluates these approaches using S&P 500 data under common evaluation metrics (e.g., tracking error and turnover). A recent contribution by Silva and de Almeida Filho ([2024](https://arxiv.org/html/2601.03927v1#bib.bib65)) provides a systematic review of solution methodologies for index tracking, covering exact and heuristic approaches through a bibliometric analysis of journals and focus areas. In contrast, the present review emphasizes the modeling frameworks themselves rather than the algorithmic solution techniques. Furthermore, our study complements the literature by providing an empirical comparison of these frameworks on real data, thereby offering practical insights into the relative effectiveness of different methodologies. An additional contribution of this article is the open access to the code, enabling transparency, reproducibility, and a standardized benchmark against which future researchers can compare their strategies. For the empirical comparison, we report daily results over almost 10 decades, starting from October 2012 to November 2022 and rebalance after every 3 months. All replication code and data-processing scripts are available at <https://github.com/vrindadhingra/index-tracking-review->. This paper is thus intended as both a scholarly synthesis and a practical resource for academics and practitioners in passive investment, particularly index tracking.

The remainder of the article is organized as follows. Section [2](https://arxiv.org/html/2601.03927v1#S2 "2 Review Methodology ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") outlines the review methodology and article selection criteria. Section [3](https://arxiv.org/html/2601.03927v1#S3 "3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") discusses the evolution of index tracking approaches, categorizing milestones into optimization-based, statistical-based, and data-driven frameworks. Section [4](https://arxiv.org/html/2601.03927v1#S4 "4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the empirical evaluation of representative models, and Section [5](https://arxiv.org/html/2601.03927v1#S5 "5 Conclusion ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") concludes with key findings, implications, and directions for future research.

## 2 Review Methodology

The methodology adopted in this review consists of three main stages:
(i) a systematic search for relevant research articles using well-defined keywords in a scientific database;
(ii) a structured filtering and screening process to obtain a final corpus of studies; and
(iii) a comprehensive empirical evaluation of the most prominent modeling frameworks for index tracking identified from the reviewed literature. The overall design of the review process is inspired by established survey methodologies in the artificial intelligence and financial optimization literature, particularly those adopted in Goodell et al. ([2021](https://arxiv.org/html/2601.03927v1#bib.bib32)) and Silva and de Almeida Filho ([2024](https://arxiv.org/html/2601.03927v1#bib.bib65)).

### 2.1 Selection and filtering of articles for review

![Refer to caption](SC.jpg)


Figure 3: Search and filtering of articles for review

The initial step in constructing a comprehensive review involves identifying and selecting relevant research articles that have made significant contributions to the field of index tracking. As depicted in Figure [3](https://arxiv.org/html/2601.03927v1#S2.F3 "Figure 3 ‣ 2.1 Selection and filtering of articles for review ‣ 2 Review Methodology ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"), the process for article selection is structured into three main stages: the Search Step, the Filtering Step, and the Screening Step. Each stage plays a critical role in narrowing the literature to a focused and high-quality set of studies that are directly aligned with the objectives of this review.

1. 1.

   Search Step: In the first stage, we conducted a broad literature search using the SCOPUS database, chosen for its extensive coverage of peer-reviewed journals across finance, operations research, artificial intelligence, and applied mathematics. To ensure a comprehensive capture of index tracking–related research, two complementary search criteria were employed.

   * •

     Search Criterion-I (SC-I): A keyword-based search was performed using the term “index tracking portfolios” within the article title, abstract, and keywords. This primary search yielded 446 articles, capturing studies that explicitly address index tracking portfolio construction.
   * •

     Search Criterion-II (SC-II):
     To further expand the search and capture articles with alternative but related terminology, we conduct a secondary search using the keywords “index tracking” or “tracking error”. This search was more focused, specifically targeting the article title and keywords sections to ensure a higher relevance of articles discussing these core concepts. The secondary search yielded 470 articles.

   By applying these two criteria, we aim to ensure that all important and relevant articles on index tracking (IT) are included in the study.
2. 2.

   Filtering step: Following the initial search, the collected articles were refined using SCOPUS’s built-in filtering tools to eliminate studies outside the scope of this review. Specifically:

   * •

     Only articles published in the English language were retained to ensure consistency in interpretation and analysis.
   * •

     As shown in Figure [3](https://arxiv.org/html/2601.03927v1#S2.F3 "Figure 3 ‣ 2.1 Selection and filtering of articles for review ‣ 2 Review Methodology ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"), articles were further filtered based on subject area and article type, focusing on research that aligns with the scope of IT methodologies and financial analysis.

   As a result of this filtering process, non-academic publications and studies not directly related to IT were excluded. After this stage, the literature set was reduced to 594 articles, comprising 375 articles from SC-I and 219 articles from SC-II.
3. 3.

   Screening step: This is the final and most crucial stage in the selection process, ensuring that the articles included in this review are both unique and relevant. In this step:

   * •

     Duplicate articles appearing across both search criteria or multiple filtered categories were removed.
   * •

     Each remaining article was examined to assess its relevance to pure index tracking. Studies focusing exclusively on enhanced indexation, unrelated portfolio optimization problems, or broader asset allocation frameworks were excluded.
   * •

     To incorporate the most recent developments, preprints indexed by SCOPUS were also reviewed. Of the 66 available preprints, 14 articles were identified as directly relevant to IT and not overlapping with already published works. These were included to ensure the review reflects the latest research trends.

The systematic application of the search, filtering, and screening steps resulted in a final set of 233 articles, forming a comprehensive and up-to-date body of literature on index tracking. Figure [4](https://arxiv.org/html/2601.03927v1#S2.F4 "Figure 4 ‣ 2.1 Selection and filtering of articles for review ‣ 2 Review Methodology ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the year-wise distribution of the selected articles, highlighting the steady growth and increasing research interest in index tracking over time. In addition, Table [2](https://arxiv.org/html/2601.03927v1#S2.T2 "Table 2 ‣ 2.1 Selection and filtering of articles for review ‣ 2 Review Methodology ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") reports the most highly cited articles within the selected corpus, offering insight into seminal contributions and influential studies that have shaped the field.

![Refer to caption](Pubcount.png)


Figure 4: Year-wise publication count




Table 2: Top articles on index tracking based on citation count

| Author(s) | Title | TC |
| --- | --- | --- |
| Beasley et al. ([2003](https://arxiv.org/html/2601.03927v1#bib.bib8)) | An evolutionary heuristic for the index tracking problem | 266 |
| Canakgoz and Beasley ([2009](https://arxiv.org/html/2601.03927v1#bib.bib13)) | Mixed-integer programming approaches for index tracking and enhanced | 192 |
|  | indexation |  |
| Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) | A linear model for tracking error minimization | 141 |
| Guastaroba and Speranza ([2012](https://arxiv.org/html/2601.03927v1#bib.bib35)) | Kernel Search: An application to the index tracking problem | 139 |
| Dose and Cincotti ([2005](https://arxiv.org/html/2601.03927v1#bib.bib21)) | Clustering of financial time series with application to index and enhanced | 120 |
|  | index tracking portfolio |  |
| Frino and Gallagher ([2001](https://arxiv.org/html/2601.03927v1#bib.bib26)) | Tracking S&P 500 Index Funds | 109 |
| Gaivoronski et al. ([2005](https://arxiv.org/html/2601.03927v1#bib.bib27)) | Optimal portfolio selection and dynamic benchmark tracking | 102 |
| Ruiz-Torrubiano and Suárez ([2009](https://arxiv.org/html/2601.03927v1#bib.bib57)) | Bond portfolio optimization problems and their applications to index | 97 |
|  | tracking: A partial optimization approach |  |
| Wu et al. ([2014b](https://arxiv.org/html/2601.03927v1#bib.bib77)) | Nonnegative-lasso and application in index tracking | 79 |
| Konno and Watanabe ([1996](https://arxiv.org/html/2601.03927v1#bib.bib38)) | A hybrid optimization approach to index tracking | 77 |
| Benidis et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib9)) | Sparse Portfolios for High-Dimensional Financial Index Tracking | 70 |
| Corielli and Marcellino ([2006](https://arxiv.org/html/2601.03927v1#bib.bib17)) | Factor based index tracking | 68 |
| Chen and Kwon ([2012](https://arxiv.org/html/2601.03927v1#bib.bib16)) | Robust portfolio selection for index tracking | 67 |
| Krink et al. ([2009](https://arxiv.org/html/2601.03927v1#bib.bib39)) | Differential evolution and combinatorial search for constrained index-tracking | 62 |
| Strub and Baumann ([2018](https://arxiv.org/html/2601.03927v1#bib.bib66)) | Optimal construction and rebalancing of index-tracking portfolios | 59 |
| Takeda et al. ([2013](https://arxiv.org/html/2601.03927v1#bib.bib68)) | Simultaneous pursuit of out-of-sample performance and sparsity in index | 58 |
|  | tracking portfolios |  |
| Focardi and Fabozzi ([2004](https://arxiv.org/html/2601.03927v1#bib.bib25)) | A methodology for index tracking based on time-series clustering | 53 |
| Fastrich et al. ([2014](https://arxiv.org/html/2601.03927v1#bib.bib24)) | Cardinality versus q-norm constraints for index tracking | 48 |
| Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib62)) | Index tracking with controlled number of assets using a hybrid heuristic | 39 |
| combining genetic algorithm and non-linear programming |  |

### 2.2 Sorting articles

With the refined corpus of articles obtained from the screening process, the next step is to categorize and organize the literature according to the modeling frameworks employed for index tracking. Based on the methodological foundations adopted by prior studies, we broadly classify the selected articles into three major categories: optimization-based frameworks, statistical-based frameworks, and data-driven frameworks.

* •

  Optimization-based frameworks: This category comprises studies that formulate the IT problem as a mathematical optimization task. The primary objective in these approaches is to construct a tracking portfolio that closely replicates the benchmark index by minimizing a specified measure of tracking error or deviation, subject to constraints such as budget, cardinality, and risk exposure.
  The literature in this stream explores a wide range of optimization techniques, including linear programming, quadratic programming, and combinatorial optimization. Commonly used tracking error measures include the mean squared error, sum of squared errors, standard deviation of tracking error, and mean absolute deviation. Depending on the choice of error metric and constraints, the resulting optimization problems may be linear or non-linear, often leading to computational challenges, particularly in large-scale settings.
* •

  Statistical-based frameworks: This category includes studies that adopt statistical and econometric methodologies to design and analyze IT portfolios. These approaches focus on modeling the underlying relationship between asset returns and the benchmark index using techniques such as regression analysis, factor models, and cointegration methods.
  Statistical-based frameworks emphasize interpretability and inference, enabling the identification of long-run equilibrium relationships, common risk factors, and explanatory variables that drive index movements. By exploiting the statistical structure of asset returns, these models aim to achieve effective tracking while maintaining economically meaningful portfolio compositions.
* •

  Data-driven frameworks: This category encompasses research that leverages data-centric and machine learning methodologies for IT. Data-driven frameworks emphasize adaptability and predictive modeling, allowing for the dynamic incorporation of market information, historical data, and economic indicators. Studies in this stream employ a variety of machine learning techniques, including clustering algorithms, random forest models combined with regression, support vector regression, deep autoencoders, and neural networks. These approaches are particularly effective in capturing non-linear relationships and complex dependencies between asset returns and the benchmark index, and are often designed to enhance tracking performance under dynamic and volatile market conditions.

This classification is used to organize the subsequent review of index tracking methodologies.

## 3 Evolution of Index Tracking framework

The intellectual foundations of index tracking are rooted in modern portfolio theory and equilibrium asset pricing. The mean–variance framework of Markowitz ([1952](https://arxiv.org/html/2601.03927v1#bib.bib46)) established the mathematical basis for constructing efficient portfolios, while the Capital Asset Pricing Model (CAPM) of Sharpe ([1964](https://arxiv.org/html/2601.03927v1#bib.bib64)) formalized the market portfolio as the optimal passive investment under equilibrium assumptions. These developments were further reinforced by the efficient market hypothesis of Fama ([1970](https://arxiv.org/html/2601.03927v1#bib.bib23)), which argues that, in informationally efficient markets, persistent excess returns from active management are difficult to achieve. Empirical evidence supporting this view was provided by Jensen ([1968](https://arxiv.org/html/2601.03927v1#bib.bib36)), who documented that actively managed mutual funds systematically underperformed market benchmarks on a risk-adjusted basis.

Together, these theoretical and empirical insights laid the groundwork for passive investment strategies and directly motivated the emergence of index funds. This paradigm shift culminated in the launch of the Vanguard Index Fund in 1976, designed to replicate the performance of the S&P 500 index. The success of this fund marked a turning point in asset management, establishing IT as a viable and cost-efficient alternative to active portfolio management.

Building on these conceptual foundations, Roll ([1992](https://arxiv.org/html/2601.03927v1#bib.bib54)) introduced the first formal optimization-based framework for IT by defining tracking error volatility (TEV) as the variance of the difference between portfolio and benchmark returns. By minimizing this quadratic deviation, Roll recast IT as a well-defined mean–variance optimization problem, thereby establishing a rigorous mathematical formulation for benchmark replication. This contribution marked a turning point, reframing IT as a precise mathematical optimization problem within the mean–variance paradigm.

Subsequent research extended this framework by proposing alternative measures of tracking error. In particular, Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) introduced linear tracking error metrics, including mean absolute deviation, mean absolute downside deviation, maximum deviation, and maximum downside deviation between the tracking portfolio and the benchmark. These formulations offered increased robustness to outliers and asymmetric return distributions. Nevertheless, quadratic tracking error measures—such as TEV—continued to dominate both academic studies and industry applications, owing to their smooth differentiability, analytical tractability, and compatibility with convex optimization techniques.

A major step toward practical IT was taken by Beasley et al. ([2003](https://arxiv.org/html/2601.03927v1#bib.bib8)), who incorporated transaction costs and cardinality constraints into a root mean squared tracking error (RMSE) minimization framework. By explicitly limiting the number of assets held in the tracking portfolio, their formulation captured key real-world considerations faced by fund managers. However, the inclusion of cardinality and turnover constraints transformed the problem into a mixed-integer nonlinear program, rendering it NP-hard. To address this computational challenge, the authors proposed evolutionary population-based heuristics, demonstrating that near-optimal tracking portfolios could be obtained efficiently despite the combinatorial nature of the problem.

This contribution motivated a growing body of research on heuristic and metaheuristic solution methods for IT. Early developments include the simulated annealing approach of Derigs and Nickel ([2003](https://arxiv.org/html/2601.03927v1#bib.bib20)), which employed a linear multi-factor model to estimate returns and covariances, and the factor-driven construction heuristic proposed by Corielli and Marcellino ([2006](https://arxiv.org/html/2601.03927v1#bib.bib17)), where assets were selected sequentially based on their factor loadings relative to the benchmark. Subsequently, Zhu et al. ([2010](https://arxiv.org/html/2601.03927v1#bib.bib88)) introduced particle swarm optimization (PSO) to navigate the high-dimensional search space of IT portfolios more effectively.

Subsequent research extended these early heuristic approaches by developing hybrid algorithms that combine global exploration with local refinement, aiming to improve both convergence speed and solution quality. Scozzari et al. ([2013](https://arxiv.org/html/2601.03927v1#bib.bib63)) proposed a hybrid evolutionary–local search framework for minimizing mean squared tracking error, demonstrating that embedding local improvement steps within evolutionary operators significantly enhances tracking accuracy. Their results highlighted the importance of balancing diversification and exploitation in large-scale IT problems.

Building on this idea, Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib62)) introduced a family of specialized heuristics that integrate regression-based asset pre-selection with adaptive local search mechanisms. By reducing the dimensionality of the candidate asset universe prior to optimization, their approach achieved competitive tracking performance across multiple benchmark indices while substantially lowering computational time. More recent contributions continue this trend toward hybridization and algorithmic specialization. For example, Álvaro Rubio-García et al. ([2024](https://arxiv.org/html/2601.03927v1#bib.bib55)) developed a hybrid simulated annealing framework tailored to cardinality-constrained IT, while Ayón et al. ([2024](https://arxiv.org/html/2601.03927v1#bib.bib7)) proposed a harmony search–based metaheuristic employing problem-specific search operators and dual population initialization schemes to accelerate convergence in large asset universes.

Collectively, these studies establish heuristic and metaheuristic optimization as a central pillar of practical IT, particularly in settings where exact mixed-integer formulations become computationally infeasible. They also illustrate a gradual shift from generic metaheuristics toward domain-aware hybrid algorithms that explicitly exploit financial structure, sparsity, and benchmark dependence.

Alongside heuristic developments, another important research direction focused on improving the tractability of IT models through reformulation and convexification. In particular, several studies sought to replace quadratic tracking-error measures with linear or piecewise-linear alternatives, thereby transforming non-linear mixed-integer programs into linear or convex optimization problems that are easier to solve. A notable contribution in this direction is Guastaroba and Speranza ([2012](https://arxiv.org/html/2601.03927v1#bib.bib35)), which enabled more efficient solution methods while maintaining the integrity of the tracking objective.

While quadratic tracking error measures such as tracking error volatility remained dominant, alternative quadratic formulations were also explored to enhance numerical stability and computational efficiency. In particular, Xu et al. ([2016](https://arxiv.org/html/2601.03927v1#bib.bib78)) proposed the sum of errors squared (SES) as an alternative tracking objective, defined as the squared deviation between portfolio and benchmark returns aggregated over time. The resulting optimization model retains a quadratic structure but differs from TEV in its aggregation of deviations. To solve the associated problem efficiently, the authors developed a non-monotone projected gradient algorithm and demonstrated its effectiveness on large-scale IT instances. Despite its computational appeal, subsequent studies have observed that SES-based formulations may lead to highly concentrated portfolios when combined with cardinality constraints, highlighting a trade-off between numerical tractability and diversification.

In parallel with optimization-based formulations, a substantial body of literature has developed statistical frameworks for IT that exploit empirical relationships between index returns and constituent asset returns, often without explicitly solving a global tracking-error minimization problem. These approaches emphasize inference, interpretability, and structural dependence rather than direct optimization. One of the earliest contributions in this direction is the factor-based IT framework of Corielli and Marcellino ([2006](https://arxiv.org/html/2601.03927v1#bib.bib17)), which models both the benchmark index and its constituents as being driven by a small number of latent common factors and idiosyncratic components. By identifying assets whose factor loadings closely resemble those of the index, the resulting portfolios are constructed to replicate index dynamics through shared systematic exposures rather than direct return matching.

Regression-based formulations constitute another prominent class of statistical IT models. These approaches seek to approximate benchmark returns as a linear combination of selected constituent asset returns, thereby aligning portfolio behavior with the index in expectation. A seminal contribution is due to Canakgoz and Beasley ([2009](https://arxiv.org/html/2601.03927v1#bib.bib13)), who proposed a mixed-integer regression-based framework in which portfolio weights are chosen such that the regression of portfolio returns on index returns yields an intercept close to zero and a slope close to one.

Subsequent research extended regression-based IT by incorporating robustness and distributional considerations. In particular, quantile regression has been employed to address the limitations of least squares estimation under heavy-tailed and asymmetric return distributions. Early contributions by Mezali and Beasley ([2013](https://arxiv.org/html/2601.03927v1#bib.bib47)) demonstrated that quantile-based tracking portfolios provide improved downside protection by focusing on conditional quantiles rather than mean behavior. This line of work was further developed in high-dimensional settings by Li ([2020](https://arxiv.org/html/2601.03927v1#bib.bib43)), who introduced sparse quantile regression formulations that enable effective asset selection while maintaining robustness to extreme market movements. More recent studies, such as Aguilar et al. ([2022](https://arxiv.org/html/2601.03927v1#bib.bib2)), explored multi-quantile and tail-probability tracking objectives, highlighting the relevance of quantile-based methods for risk-sensitive index replication.

Another influential strand of statistical IT research is built on regularization and sparse learning principles. These methods impose explicit penalties on portfolio weights to induce sparsity, thereby achieving asset selection without introducing binary decision variables. Early work by Wu et al. ([2014a](https://arxiv.org/html/2601.03927v1#bib.bib76)) applied non-negative Lasso regression to IT, ensuring economically interpretable long-only portfolios while automatically controlling portfolio size. Extensions using Elastic Net penalties (Wu and Yang, [2014](https://arxiv.org/html/2601.03927v1#bib.bib75)) balance sparsity and stability by combining ℓ1\ell\_{1} and ℓ2\ell\_{2} regularization, mitigating the instability of pure Lasso solutions in the presence of highly correlated assets. More generally, qq-norm regularization frameworks (Fastrich et al., [2014](https://arxiv.org/html/2601.03927v1#bib.bib24)) allow flexible control over sparsity levels and tracking accuracy. From an artificial intelligence perspective, these approaches can be viewed as early forms of supervised sparse learning in finance, where regularization plays a central role in preventing overfitting and enhancing generalization in high-dimensional asset spaces.

Cointegration-based approaches form another important class of statistical IT models, particularly suited for capturing long-run equilibrium relationships between asset prices and benchmark indices. Rather than matching short-term return fluctuations, these methods focus on identifying subsets of assets whose price processes share common stochastic trends with the index. Early contributions by Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib58)) demonstrated that portfolios constructed from cointegrated assets exhibit strong long-term tracking properties, even when short-run deviations are present. This framework was further extended in Sant’Anna et al. ([2020b](https://arxiv.org/html/2601.03927v1#bib.bib60)), which introduced convex cointegration formulations that improve numerical stability and scalability while preserving long-run alignment with the benchmark. Cointegration-based tracking portfolios are especially attractive in markets characterized by persistent common movements, as they provide robustness to transitory shocks and reduce sensitivity to short-term noise.

While early IT models primarily emphasized minimizing tracking error, subsequent research highlighted the importance of explicitly controlling downside risk and tail behavior, particularly during periods of market stress. To this end, several studies integrated coherent risk measures into the tracking framework. Wang et al. ([2012](https://arxiv.org/html/2601.03927v1#bib.bib71)) introduced conditional value-at-risk (CVaR) constraints within a mean absolute deviation formulation, showing that downside risk could be effectively limited without materially degrading tracking accuracy. Building on this idea, Goel et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib28)) proposed a two-tail mixed CVaR (TMCVaR) model that simultaneously penalizes extreme positive and negative deviations from the benchmark, thereby controlling both over- and under-performance. This formulation aggregates CVaR measures across multiple confidence levels, yielding improved robustness and more stable tracking behavior. More recent contributions, such as Sant’Anna et al. ([2022](https://arxiv.org/html/2601.03927v1#bib.bib61)) and Anis et al. ([2023](https://arxiv.org/html/2601.03927v1#bib.bib5)), further integrate dynamic or adaptive risk measures to jointly enhance tracking performance and risk resilience in volatile market environments.

In parallel with optimization- and statistical-based formulations, recent years have seen a growing body of research adopting data-driven and ML approaches for IT. This shift has been driven by the increasing availability of high-dimensional financial data and the need to model nonlinear, temporal, and structural dependencies among asset returns that are difficult to capture within classical parametric frameworks. Early data-driven contributions primarily relied on clustering techniques to identify representative subsets of assets whose collective behavior approximates that of the benchmark index. Notable examples include the hierarchical clustering approaches of Focardi and Fabozzi ([2004](https://arxiv.org/html/2601.03927v1#bib.bib25)) and Dose and Cincotti ([2005](https://arxiv.org/html/2601.03927v1#bib.bib21)), which used Euclidean- and correlation-based distance measures to construct sparse tracking portfolios with reduced dimensionality.

Subsequent research extended these ideas by introducing more flexible similarity measures and richer representations of asset dynamics. Tang and Li ([2014](https://arxiv.org/html/2601.03927v1#bib.bib69)) proposed soft subspace clustering, allowing assets to be grouped using adaptive feature weights rather than uniform distance metrics, thereby improving robustness in high-dimensional settings. Temporal structure was incorporated through k-medoids clustering with dynamic time warping (DTW) distances in Zhang et al. ([2021](https://arxiv.org/html/2601.03927v1#bib.bib84)), enabling improved alignment of return trajectories across time. More recently, Goel et al. ([2024](https://arxiv.org/html/2601.03927v1#bib.bib29)) introduced topological data analysis (TDA) to IT, using persistent homology to extract stable geometric features from asset return paths and form tracking portfolios based on structural similarity rather than pointwise distance.

A complementary strand of data-driven research focuses on learning nonlinear mappings between constituent asset returns and benchmark indices using supervised and unsupervised ML models. Autoencoder-based approaches (Zhang et al., [2020](https://arxiv.org/html/2601.03927v1#bib.bib82)) learn low-dimensional latent representations that summarize common market structure, while deep latent representation models (Kim and Kim, [2020](https://arxiv.org/html/2601.03927v1#bib.bib37)) and neural networks—including feedforward, stochastic, and recurrent architectures (Zheng et al., [2020a](https://arxiv.org/html/2601.03927v1#bib.bib86), Kwak et al., [2021](https://arxiv.org/html/2601.03927v1#bib.bib40), Wang et al., [2024](https://arxiv.org/html/2601.03927v1#bib.bib73))—capture complex nonlinear and temporal dependencies. In parallel, tree-based and kernel methods have been explored for IT: random forests enable nonlinear interaction modeling and implicit feature selection (Cao et al., [2022](https://arxiv.org/html/2601.03927v1#bib.bib14)), support vector regression (SVR) provides margin-based generalization in high-dimensional spaces (Teng et al., [2017](https://arxiv.org/html/2601.03927v1#bib.bib70)), and reinforcement learning frameworks sequentially adapt portfolio weights using reward signals linked to tracking performance (Peng et al., [2023b](https://arxiv.org/html/2601.03927v1#bib.bib51)).

Beyond prediction-oriented ML models, a growing literature emphasizes structural learning approaches that exploit similarity, geometry, and spectral properties of asset returns. Zhang et al. ([2025](https://arxiv.org/html/2601.03927v1#bib.bib83)) provide a systematic comparison of clustering techniques—including K-means, K-medoids, hierarchical clustering, and DTW-based methods—and show that while regression-based models often achieve superior tracking accuracy, correlation-based hierarchical clustering tends to generate portfolios with lower risk. Advances in TDA-based tracking have continued with sparse formulations that use persistent homology to guide regularization and asset selection without extensive cross-validation (Goel et al., [2026](https://arxiv.org/html/2601.03927v1#bib.bib31)). Other recent contributions incorporate network, spectral, and factor-learning representations, such as combining Random Matrix Theory with network centrality measures to filter correlation matrices and identify influential assets (Grassetti, [2025](https://arxiv.org/html/2601.03927v1#bib.bib34)), eigenvalue-matching approaches based on structured PCA for low-turnover tracking (Cesarone et al., [2025](https://arxiv.org/html/2601.03927v1#bib.bib15)), and network-based models that embed adaptive community information to enhance risk-adjusted performance (Xu et al., [2026](https://arxiv.org/html/2601.03927v1#bib.bib79)). Complementing these structural approaches, sparse learning methods—including non-convex ℓp\ell\_{p} regularization (Zapata Quimbayo and Moreno Trujillo, [2025](https://arxiv.org/html/2601.03927v1#bib.bib81)) and penalized Huber-loss regression (Li et al., [2025](https://arxiv.org/html/2601.03927v1#bib.bib44)), continue to offer computationally efficient and robust solutions for high-dimensional IT.

The development of IT models reflects a gradual progression from early optimization-based formulations toward more flexible statistical and data-driven frameworks, shaped by both theoretical insights and practical implementation constraints. As discussed above, the existing literature can be organized into three broad and partially overlapping modeling paradigms: optimization-based approaches, statistical-based approaches, and data-driven or machine learning–based approaches. Each paradigm addresses the IT problem from a distinct methodological perspective and gives rise to different trade-offs in terms of tracking accuracy, interpretability, computational complexity, and scalability.

![Refer to caption](Evolution.png)


Figure 5: A roadmap of the evolution of index tracking models: from theoretical development to AI (developed using Notebook LM)

In the remainder of this section, we review the principal modeling frameworks within each of these categories using a unified notation. Consider a universe of nn assets observed over TT time periods (or scenarios). Let pi,tp\_{i,t} denote the historical price of asset ii at time tt, for t=1,2,…,Tt=1,2,\ldots,T. The return of asset ii at time tt is defined as
ri,t=pi,t−pi,t−1pi,t−1.\displaystyle r\_{i,t}=\frac{p\_{i,t}-p\_{i,t-1}}{p\_{i,t-1}}.
Let R=[ri,t]∈ℝT×nR=[r\_{i,t}]\in\mathbb{R}^{T\times n} denote the matrix of asset returns. A tracking portfolio is represented by the weight vector w=(w1,w2,…,wn)w=(w\_{1},w\_{2},\ldots,w\_{n}), where wiw\_{i} denotes the proportion of capital invested in asset ii. Denoting by ItI\_{t} the return of the benchmark index at time tt, the return of the tracking portfolio at time tt is given by
Rw,t=∑i=1nri,t​wi.\displaystyle R\_{w,t}=\sum\_{i=1}^{n}r\_{i,t}w\_{i}.

### 3.1 Optimization based framework

In this section, we discuss the important index tracking models developed over the years that use an optimization based framework for determining the index tracking portfolio. Table [3](https://arxiv.org/html/2601.03927v1#S3.T3 "Table 3 ‣ 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") lists the best articles based on different tracking error metrics according to their citation score. We explain all these methods in details with their mathematical modeling. Typically, an optimization-based index tracking problem aims at minimizing the tracking error between the returns of the portfolio and the benchmark index.

Table 3: Classification of top articles under optimization-based approaches for index tracking based on different tracking error metrics used

|  |  |  |  |
| --- | --- | --- | --- |
| Tracking Error | Author(s) | Title | TC |
| RMSE | Beasley et al. ([2003](https://arxiv.org/html/2601.03927v1#bib.bib8)) | An evolutionary heuristic for the index tracking problem | 266 |
| Gaivoronski et al. ([2005](https://arxiv.org/html/2601.03927v1#bib.bib27)) | Optimal portfolio selection and dynamic benchmark tracking | 102 |
| Krink et al. ([2009](https://arxiv.org/html/2601.03927v1#bib.bib39)) | Differential evolution and combinatorial search for constrained | 62 |
|  | index-tracking |  |
| MSE | Ruiz-Torrubiano and Suárez ([2009](https://arxiv.org/html/2601.03927v1#bib.bib57)) | A hybrid optimization approach to index tracking | 77 |
| Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib62)) | Index tracking with controlled number of assets using a hybrid | 39 |
|  | heuristic combining genetic algorithm and non-linear programming |  |
| Scozzari et al. ([2013](https://arxiv.org/html/2601.03927v1#bib.bib63)) | Exact and heuristic approaches for the index tracking problem | 46 |
|  | with UCITS constraints |  |
| SES | Xu et al. ([2016](https://arxiv.org/html/2601.03927v1#bib.bib78)) | An efficient optimization approach for a cardinality-constrained | 42 |
|  | index tracking problem |  |
| Wang et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib72)) | An index tracking model with stratified sampling and optimal | 6 |
|  | allocation |  |
| TEV/TESD | Derigs and Nickel ([2003](https://arxiv.org/html/2601.03927v1#bib.bib20)) | Meta-heuristic based decision support for portfolio optimization | 39 |
|  | with a case study on tracking error minimization in passive |  |
|  | portfolio management |  |
| Mutunge and Haugland ([2018](https://arxiv.org/html/2601.03927v1#bib.bib48)) | Minimizing the tracking error of cardinality constrained portfolios | 37 |
| MAD/AD | Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) | A linear model for tracking error minimization | 141 |
| Guastaroba and Speranza ([2012](https://arxiv.org/html/2601.03927v1#bib.bib35)) | Kernel Search: An application to the index tracking problem | 139 |
| MADD | Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) | A linear model for tracking error minimization | 141 |
| Min-Max | Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) | A linear model for tracking error minimization | 141 |
| DMin-Max | Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) | A linear model for tracking error minimization | 141 |
| MCVaR | Goel et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib28)) | Index tracking and enhanced indexing using mixed conditional | 28 |
|  | value-at-risk |  |

The standard optimization-based index tracking problem (IT-OPT), limiting the number of assets in the tracking portfolio is a mixed integer programming problem, given as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (IT-OPT)   MinTE​(Rw​t,It)\qquad\ \text{(IT-OPT) \ \qquad Min}\quad\text{TE}(R\_{wt},I\_{t})\qquad\qquad\qquad\qquad\qquad |  | (1) |

subject to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵi​zi≤wi≤δi​zi,i=1,…,n,\qquad\qquad\qquad\qquad\epsilon\_{i}z\_{i}\leq w\_{i}\leq\delta\_{i}z\_{i},\ \ i=1,\ldots,n, |  | (2) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nwi=1,\quad\sum\limits\_{i=1}^{n}w\_{i}=1, |  | (3) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nzi≤K,\quad\sum\limits\_{i=1}^{n}z\_{i}\leq K, |  | (4) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi∈{0,1},i=1,…,n.\qquad\qquad\qquad\ z\_{i}\in\{0,1\},\ \ i=1,\ldots,n. |  | (5) |

Here, the objective in ([1](https://arxiv.org/html/2601.03927v1#S3.E1 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")) aims to minimize the tracking error function TE(Rw​t,It)(R\_{wt},I\_{t}) between the returns of the index ItI\_{t} and the that of the tracking portfolio Rw​t;t=1,2,…,TR\_{wt};\,t=1,2,\ldots,T. The constraint in ([4](https://arxiv.org/html/2601.03927v1#S3.E4 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")) is the cardinality constraint that limits the number of assets in the tracking portfolio to be KK, where 0<K<n0<K<n. The variables ziz\_{i} are binary variables; if zi=1,z\_{i}=1, then asset ii is included in the portfolio, and zi=0z\_{i}=0 implies asset ii is not included in the portfolio. The constraint ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")) is called the holding constraint or the size constraint that ensures that if asset ii is included in the portfolio, then the weight wiw\_{i} is bounded between user defined parameters, ϵi\epsilon\_{i} and δi.\delta\_{i}.

These constraints are present in almost all mathematical models associated with the index tracking problem. What changes is the TE function TE(Rw​t,It)(R\_{wt},I\_{t}), which can take different structure forms, linear to non-convex. We now describe some commonly used TE functions, shortlisted from the literature, as described in Table [3](https://arxiv.org/html/2601.03927v1#S3.T3 "Table 3 ‣ 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem").

#### Different tracking error functions and their corresponding optimization framework

1. 1.

   Tracking Error Variance (TEV):
   The variance-based tracking error is the earliest and most widely adopted measure of tracking performance in index tracking literature (Roll, [1992](https://arxiv.org/html/2601.03927v1#bib.bib54), Larsen and Resnick, [1998](https://arxiv.org/html/2601.03927v1#bib.bib42), Rudolf et al., [1999](https://arxiv.org/html/2601.03927v1#bib.bib56)). It quantifies the variability of the difference between the portfolio return and the benchmark return over time, reflecting the consistency of the replication. The tracking error variance (TEV) is defined as

   |  |  |  |
   | --- | --- | --- |
   |  | TEV=σ2​(Rw​t−It),\text{TEV}=\sigma^{2}(R\_{wt}-I\_{t}), |  |

   and its square root, the tracking error standard deviation (TESD), is given by

   |  |  |  |
   | --- | --- | --- |
   |  | TESD=σ2​(Rw​t−It).\text{TESD}=\sqrt{\sigma^{2}(R\_{wt}-I\_{t})}. |  |

   In matrix form, if x=w−b∈ℝnx=w-b\in\mathbb{R}^{n} denotes the vector of active portfolio weights, where b∈ℝnb\in\mathbb{R}^{n} is the weight vector of the benchmark index and Σ∈ℝn×n\Sigma\in\mathbb{R}^{n\times n} the covariance matrix of asset returns, then TEV can be written as

   |  |  |  |
   | --- | --- | --- |
   |  | TEV=x⊤​Σ​x,\text{TEV}=x^{\top}\Sigma x, |  |

   subject to the standard portfolio constraints

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1nwi=∑i=1nbi=1,0≤wi≤1\sum\_{i=1}^{n}w\_{i}=\sum\_{i=1}^{n}b\_{i}=1,\quad 0\leq w\_{i}\leq 1 |  |

   which translates into

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1nxi=0,and−bi≤xi≤1−bifor ​i=1,2,…,n.\sum\_{i=1}^{n}x\_{i}=0,\text{and}-b\_{i}\leq x\_{i}\leq 1-b\_{i}\quad\text{for }i=1,2,\ldots,n. |  |

   Thus, the final model that minimizes TEV (or equivalently, TESD) takes the following form:

   |  |  |  |
   | --- | --- | --- |
   |  | (TEV)   Min ​x⊤​Σ​x\qquad\ \text{(TEV) \ \qquad Min \quad}x^{\top}\Sigma x\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   subject to

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1nxi=0,\sum\_{i=1}^{n}x\_{i}=0,\qquad\qquad\qquad\qquad |  |

   |  |  |  |
   | --- | --- | --- |
   |  | −bi≤xi≤1−bi,i=1,2,…,n-b\_{i}\leq x\_{i}\leq 1-b\_{i},\ i=1,2,\ldots,n |  |

   ([4](https://arxiv.org/html/2601.03927v1#S3.E4 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))—([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))

   Minimizing TEV (or equivalently, TESD) yields a portfolio that minimizes the volatility of its deviation from the benchmark index. Despite subsequent criticism for ignoring systematic bias, variance-based measures remain central in both academic research and industry practice due to their convexity, interpretability, and empirical robustness in realistic index tracking applications.
2. 2.

   Mean Squared Error (MSE):
   While variance-based tracking error measures such as TEV gained early popularity due to their simplicity and analytical tractability, they were later criticized for being “centered” measures—that is, they quantify the dispersion of the portfolio’s excess return around its mean, rather than around zero. As a result, a portfolio with a consistent bias (i.e., one that systematically over or under performs the index by a constant amount) could exhibit a low variance-based tracking error despite failing to accurately replicate the benchmark. To address this limitation, Beasley et al. ([2003](https://arxiv.org/html/2601.03927v1#bib.bib8)) introduced a generalized tracking error function that measures deviations directly from the benchmark returns without centering around the mean. This family of measures is expressed as

   |  |  |  |
   | --- | --- | --- |
   |  | TEα=1T​[∑t=1T|It−Rw​t|α](1/α),\text{TE}\_{\alpha}=\dfrac{1}{T}\left[\sum\_{t=1}^{T}\left|I\_{t}-R\_{wt}\right|^{\alpha}\right]^{(1/\alpha)}, |  |

   where α\alpha determines the degree of penalization for large deviations. A commonly adopted special case is the Root Mean Squared Error (RMSE), corresponding to α=2\alpha=2, defined as

   |  |  |  |
   | --- | --- | --- |
   |  | RMSE=1T​∑t=1T(It−Rw​t)2.\text{RMSE}=\sqrt{\frac{1}{T}\sum\_{t=1}^{T}\left(I\_{t}-R\_{wt}\right)^{2}}. |  |

   The inclusion of the square root renders the RMSE function non-linear and non-convex, leading to a mixed-integer non-linear programming (MINLP) formulation. Consequently, heuristic or metaheuristic algorithms are typically employed to obtain near-optimal solutions. For instance, Beasley et al. ([2003](https://arxiv.org/html/2601.03927v1#bib.bib8)) proposed a population-based heuristic for RMSE minimization, and subsequent studies have adopted similar approaches (Gaivoronski et al., [2005](https://arxiv.org/html/2601.03927v1#bib.bib27), Krink et al., [2009](https://arxiv.org/html/2601.03927v1#bib.bib39), Zhu et al., [2010](https://arxiv.org/html/2601.03927v1#bib.bib88), Andriosopoulos et al., [2013](https://arxiv.org/html/2601.03927v1#bib.bib4)). Another variant of RMSE is the mean squared error (MSE) tracking error function, which is given as

   |  |  |  |
   | --- | --- | --- |
   |  | MSE=1T​∑t=1T(It−Rw​t)2=1T​∑t=1T(It−∑j=1nrj​t​wj)2.\text{MSE}=\frac{1}{T}\sum\_{t=1}^{T}\left(I\_{t}-R\_{wt}\right)^{2}=\frac{1}{T}\sum\_{t=1}^{T}\left(I\_{t}-\sum\_{j=1}^{n}r\_{jt}w\_{j}\right)^{2}. |  |

   This objective function is convex and quadratic, resulting in the following convex quadratic programming problem:

   |  |  |  |
   | --- | --- | --- |
   |  | (MSE)   Min ​1T​∑t=1T(It−∑j=1nrj​t​wj)2\qquad\ \text{(MSE) \ \qquad Min \quad}\frac{1}{T}\sum\_{t=1}^{T}\left(I\_{t}-\sum\_{j=1}^{n}r\_{jt}w\_{j}\right)^{2}\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")).

   We consider the MSE minimization problem for the empirical study in this review.
3. 3.

   Sum of Errors Squared (SES): The SES measure quantifies the deviation between the portfolio and benchmark returns by first aggregating all period-wise errors and then squaring the total. Specifically, the error in each period, defined as the difference between the benchmark index return and the portfolio return is summed across the entire investment horizon, and the square of this cumulative deviation forms the SES tracking error function. Mathematically, the SES function is expressed as

   |  |  |  |
   | --- | --- | --- |
   |  | SES=1T​[∑t=1T(It−Rw​t)]2.\text{SES}=\frac{1}{T}\left[\sum\_{t=1}^{T}\left(I\_{t}-R\_{wt}\right)\right]^{2}. |  |

   and the corresponding tracking model becomes:

   |  |  |  |
   | --- | --- | --- |
   |  | (SES)   Min ​1T​[∑t=1T(It−Rw​t)]2\qquad\ \text{(SES) \ \qquad Min \quad}\frac{1}{T}\left[\sum\_{t=1}^{T}\left(I\_{t}-R\_{wt}\right)\right]^{2}\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")).

   Unlike the MSE objective, which penalizes deviations period by period, the SES measure emphasizes overall directional consistency between the portfolio and the benchmark. The function remains convex and quadratic in form; however, the inclusion of a cardinality constraint renders the optimization problem (SES), a NP-hard. Xu et al. ([2016](https://arxiv.org/html/2601.03927v1#bib.bib78)) addressed this challenge by employing a non-monotone projected gradient (NPG) algorithm, demonstrating its computational efficiency in identifying near-optimal tracking portfolios under the SES minimization.

   These quadratic loss functions (TEV, MSE, and SES) often overemphasize large deviations and may not accurately align with investor preferences. Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) argued that, due to the linear nature of fund managers’ performance fees, linear deviations provide a more accurate representation of an investor’s risk attitude than squared deviations. Motivated by this reasoning, Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) proposed four linear tracking errors for index tracking, described in detail in the following.
4. 4.

   Mean absolute deviation (MAD): The first linear tracking error proposed by Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) minimizes the mean absolute deviations (MAD) between the tracking portfolio’s returns and the benchmark returns, defined as

   |  |  |  |
   | --- | --- | --- |
   |  | MAD=1T​∑t=1T|Rw​t−It|.\textbf{MAD}=\dfrac{1}{T}\sum\limits\_{t=1}^{T}|R\_{wt}-I\_{t}|. |  |

   Because the absolute value function is non-differentiable, it is linearized by introducing two non-negative auxiliary variables, yt+y\_{t}^{+} and yt−y\_{t}^{-}, which respectively represents the positive and negative deviations of the tracking portfolio return from the index returns.
   It follows that if

   |  |  |  |
   | --- | --- | --- |
   |  | Rw​t>It,thenyt+=Rw​t−It(with ​yt−=0​),R\_{wt}>I\_{t},\quad\text{then}\quad y\_{t}^{+}=R\_{wt}-I\_{t}\quad\text{(with }y\_{t}^{-}=0\text{)}, |  |

   representing over performance of the tracking portfolio than the index, and if

   |  |  |  |
   | --- | --- | --- |
   |  | Rw​t<It,thenyt−=It−Rw​t(with ​yt+=0​),R\_{wt}<I\_{t},\quad\text{then}\quad y\_{t}^{-}=I\_{t}-R\_{wt}\quad\text{(with }y\_{t}^{+}=0\text{)}, |  |

   representing under performance of the tracking portfolio than the index. Since only one of yt+y\_{t}^{+} or yt−y\_{t}^{-} is positive at any time tt, these conditions can be combined into the single constraint as

   |  |  |  |
   | --- | --- | --- |
   |  | Rw​t−yt++yt−=It,t=1,2,…,T.R\_{wt}-y\_{t}^{+}+y\_{t}^{-}=I\_{t},\quad t=1,2,\ldots,T. |  |

   Thus, the index tracking problem using MAD as the objective is formulated as the following linear programming problem:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (MAD)   Min ​1T​∑t=1T(yt++yt−)\qquad\ \text{(MAD) \ \qquad Min \quad}\dfrac{1}{T}\sum\limits\_{t=1}^{T}(y\_{t}^{+}+y\_{t}^{-})\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  | (6) |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Rw​t−yt++yt−=It;t=1,2,…,TR\_{wt}-y\_{t}^{+}+y\_{t}^{-}=I\_{t};\ t=1,2,\ldots,T\quad |  | (7) |

   This formulation being linear is convex and is amenable to solution via standard linear programming techniques, ensuring that the tracking portfolio closely replicates the index returns.
5. 5.

   Mean absolute downside deviation (MADD): While MAD accounts for both positive and negative deviations between portfolio and index returns, in many practical scenarios only the downside (or underperformance) of the index is of concern. In such cases, the tracking error is measured by the mean absolute downside deviation (MADD), as introduced in Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) that focuses on minimizing only the negative deviations in the MAD model, taking the following form:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (MADD)   Min ​∑t=1Tyt−\qquad\ \text{(MADD) \ \qquad Min \quad}\sum\limits\_{t=1}^{T}y\_{t}^{-}\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  | (8) |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Rw​t+yt−≥It;t=1,2,…,TR\_{wt}+y\_{t}^{-}\geq I\_{t};\ t=1,2,\ldots,T\qquad |  | (9) |

   This linear programming formulation emphasizes reducing the downside deviation, thus providing a robust metric for scenarios where it is critical to avoid under-performance relative to the benchmark index.
6. 6.

   MinMax: The third linear tracking error introduced by Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) is the MinMax. This tracking error aims at minimizing the maximum (largest absolute) deviation between the portfolio and the index returns, representing a robust “worst-case” optimization approach. Mathematically, this tracking error metric is defined as

   |  |  |  |
   | --- | --- | --- |
   |  | MinMax=min⁡maxt⁡|Rw​t−It|.\text{MinMax}=\min\max\_{t}|R\_{wt}-I\_{t}|. |  |

   This formulation can be reformulated as a linear programming (LP) problem by introducing an auxiliary variable ξ\xi that bounds the absolute deviations,

   |  |  |  |
   | --- | --- | --- |
   |  | maxt⁡|Rw​t−It|=ξ⟺|Rw​t−It|≤ξ⟺Rw​t−ξ≤It,Rw​t+ξ≥It,∀t=1,2,…,T.\max\_{t}|R\_{wt}-I\_{t}|=\xi\Longleftrightarrow|R\_{wt}-I\_{t}|\leq\xi\quad\Longleftrightarrow\quad R\_{wt}-\xi\leq I\_{t},\quad R\_{wt}+\xi\geq I\_{t},\quad\forall\,t=1,2,\ldots,T. |  |

   Thus, the MinMax optimization problem is expressed as the following linear program:

   |  |  |  |
   | --- | --- | --- |
   |  | (MinMax)   Min ​ξ\qquad\ \text{(MinMax) \ \qquad Min \quad}\xi\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))

   |  |  |  |
   | --- | --- | --- |
   |  | Rw​t−ξ≤It;t=1,2,…,T,R\_{wt}-\xi\leq I\_{t};\ t=1,2,\ldots,T,\qquad |  |

   |  |  |  |
   | --- | --- | --- |
   |  | Rw​t+ξ≥It;t=1,2,…,T.R\_{wt}+\xi\geq I\_{t};\ t=1,2,\ldots,T.\qquad |  |

   This LP formulation minimizes the worst possible tracking deviation over the entire period, yielding a robust tracking portfolio that limits extreme deviations from the index, making it particularly useful for conservative investors with strong aversion to large single-period errors.
7. 7.

   Downside MinMax (DMinMax): The fourth linear tracking error by Rudolf et al. ([1999](https://arxiv.org/html/2601.03927v1#bib.bib56)) is the Downside MinMax. This approach minimizes the maximum downside deviation, specifically focusing on scenarios where the tracking portfolio under-performs the benchmark index. This optimization emphasizes controlling the worst-case under-performance, providing a conservative strategy designed to minimize the largest observed negative deviations. Mathematically, the DMinMax tracking error is formulated as:

   |  |  |  |
   | --- | --- | --- |
   |  | DMinMax=minmaxt(It−Rw​t)+.\text{DMinMax}=\min\max\_{t}(I\_{t}-R\_{wt})^{+}. |  |

   This can be modeled as a linear programming problem by introducing an auxiliary variable ξ\xi representing the maximum downside deviation, and imposing constraints only on downside scenarios, that is,Rw​t≤ItR\_{wt}\leq I\_{t}:

   |  |  |  |
   | --- | --- | --- |
   |  | (DMinMax)   Min ​ξ\qquad\ \text{(DMinMax) \ \qquad Min \quad}\xi\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))

   |  |  |  |
   | --- | --- | --- |
   |  | Rw​t+ξ≥It;t=1,2,…,T.R\_{wt}+\xi\geq I\_{t};\ t=1,2,\ldots,T.\qquad |  |

   This linear formulation directly limits the worst-case underperformance of the portfolio relative to the benchmark index. The DMinMax model is particularly suitable for risk-averse investors seeking to minimize substantial downside deviations from the index returns.
8. 8.

   Mixed CVaR based index tracking model: Conditional Value-at-Risk (CVaR) is a coherent downside risk measure that captures the expected loss beyond a specified confidence level α\alpha (Rockafellar and Uryasev, [2002](https://arxiv.org/html/2601.03927v1#bib.bib53)). Unlike variance-based measures, which treat all deviations symmetrically, CVaR focuses on the tail of the loss distribution, thus directly accounting for extreme downside risk. In portfolio optimization, minimizing CVaR ensures robustness against rare but severe market losses, making it a natural choice for risk-aware index tracking. However, as noted by Goel et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib28)), reliance on a single confidence level α\alpha may overlook other parts of the return distribution. In this regard, the mixed CVaR (MCVaR) framework aggregates multiple CVaR values across several confidence levels, thereby incorporating richer distributional information while retaining convexity and coherence.

   Goel et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib28)) further extend this framework by proposing the two-tail mixed CVaR (TMCVaR) model for index tracking. The approach penalizes both downside and upside deviations of the tracking portfolio relative to the benchmark, corresponding respectively to under and over performance, thereby promoting balanced replication of the benchmark’s return dynamics. The two components are combined using a weight parameter δ∈(0,1)\delta\in(0,1), which controls the relative emphasis on each tail:

   |  |  |  |
   | --- | --- | --- |
   |  | δ​MCVaR​(−Xw​t)+(1−δ)​MCVaR​(Xw​t),\delta\,\text{MCVaR}(-X\_{wt})+(1-\delta)\,\text{MCVaR}(X\_{wt}), |  |

   where Xw​t=It−Rw​tX\_{wt}=I\_{t}-R\_{wt} denotes the excess return of the index ItI\_{t} over the tracking portfolio Rw​tR\_{wt}.

   Each MCVaR component is defined as a weighted sum of CVaR measures evaluated at mm different confidence levels, given as:

   |  |  |  |
   | --- | --- | --- |
   |  | MCVaR​(Xw​t)=∑k=1mλkU​CVaRαkU​(Xw​t),\text{MCVaR}(X\_{wt})=\sum\_{k=1}^{m}\lambda^{U}\_{k}\text{CVaR}\_{\alpha^{U}\_{k}}(X\_{wt}), |  |

   |  |  |  |
   | --- | --- | --- |
   |  | MCVaR​(−Xw​t)=∑k=1mλkD​CVaRαkD​(−Xw​t),\text{MCVaR}(-X\_{wt})=\sum\_{k=1}^{m}\lambda^{D}\_{k}\text{CVaR}\_{\alpha^{D}\_{k}}(-X\_{wt}), |  |

   where λU=(λkU,k=1,…,m)\lambda^{U}=(\lambda^{U}\_{k},k=1,\dots,m) and λD=(λkD,k=1,…,m)\lambda^{D}=(\lambda^{D}\_{k},k=1,\dots,m) are non-negative weights satisfying
     
   ∑k=1mλkU=∑k=1mλkD=1\sum\limits\_{k=1}^{m}\lambda^{U}\_{k}=\sum\limits\_{k=1}^{m}\lambda^{D}\_{k}=1. Using the linearization of CVaR, Goel et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib28)) obtain the following optimization problem that minimizes the weighted two-tail MCVaR measure as a function of the portfolio weights:

   |  |  |  |
   | --- | --- | --- |
   |  | (TMCVaR)minβ,wδ​(∑k=1mλkU​[βkU+1(1−αkU)​T​∑j=1Tuj​kU])+(1−δ)​(∑k=1mλkD​[βkD+1(1−αkD)​T​∑j=1Tuj​kD])\textbf{(TMCVaR)}\quad\min\_{\beta,w}\quad\delta\left(\sum\_{k=1}^{m}\lambda^{U}\_{k}\left[\beta^{U}\_{k}+\frac{1}{(1-\alpha^{U}\_{k})T}\sum\_{j=1}^{T}u^{U}\_{jk}\right]\right)+(1-\delta)\left(\sum\_{k=1}^{m}\lambda^{D}\_{k}\left[\beta^{D}\_{k}+\frac{1}{(1-\alpha^{D}\_{k})T}\sum\_{j=1}^{T}u^{D}\_{jk}\right]\right) |  |

   subject to

   |  |  |  |
   | --- | --- | --- |
   |  | uj​kU+(∑i=1nri​j​wi−Ij)+βkU≥0for ​k=1,…,m,j=1,…,T,u^{U}\_{jk}+\left(\sum\_{i=1}^{n}r\_{ij}w\_{i}-I\_{j}\right)+\beta^{U}\_{k}\geq 0\quad\text{for }k=1,\dots,m,\,j=1,\dots,T, |  |

   |  |  |  |
   | --- | --- | --- |
   |  | uj​kD−(∑i=1nri​j​wi−Ij)+βkD≥0for ​k=1,…,m,j=1,…,T,u^{D}\_{jk}-\left(\sum\_{i=1}^{n}r\_{ij}w\_{i}-I\_{j}\right)+\beta^{D}\_{k}\geq 0\quad\text{for }k=1,\dots,m,\,j=1,\dots,T, |  |

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1nwi=1,\sum\_{i=1}^{n}w\_{i}=1,\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   |  |  |  |
   | --- | --- | --- |
   |  | wi≥0for ​i=1,…,n,w\_{i}\geq 0\quad\text{for }i=1,\dots,n,\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   |  |  |  |
   | --- | --- | --- |
   |  | uj​kU,uj​kD≥0for ​k=1,…,m,j=1,…,T.u^{U}\_{jk},u^{D}\_{jk}\geq 0\quad\text{for }k=1,\dots,m,\,j=1,\dots,T.\qquad\qquad\qquad\qquad |  |

   ([4](https://arxiv.org/html/2601.03927v1#S3.E4 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))—([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))

   where the variables βkU\beta^{U}\_{k} and βkD\beta^{D}\_{k} correspond to the value-at-risk (VaR) thresholds associated with the upper (upside) and lower (downside) tails at confidence levels αkU\alpha^{U}\_{k} and αkD\alpha^{D}\_{k}, respectively. uj​kUu^{U}\_{jk} and uj​kDu^{D}\_{jk} are non-negative auxiliary variables representing the deviations of portfolio returns beyond the corresponding VaR thresholds in the upper and lower tails for each scenario jj and confidence level kk. Thus, uj​kUu^{U}\_{jk} and uj​kDu^{D}\_{jk} linearize the piecewise CVaR components, while βkU\beta^{U}\_{k} and βkD\beta^{D}\_{k} capture the conditional quantiles of the loss distribution for the upside and downside risks, respectively.

   The above model is a linear program, thus retains computational tractability while capturing both tails of the deviation distribution. By minimizing the two-tail MCVaR, the framework effectively balances over- and under-performance relative to the benchmark, ensuring tighter replication with controlled tail risk. Empirically, Goel et al. ([2018](https://arxiv.org/html/2601.03927v1#bib.bib28)) report that the proposed TMCVaR-based index tracking model outperforms variance- and MAD-based formulations in terms of higher correlation with the benchmark and lower tracking error across multiple global indices.

Table 4: Thematic clusters of different statistical based approaches for index tracking

|  |  |  |  |
| --- | --- | --- | --- |
| Theme | Author(s) | Title | TC |
| Least squares regression | Canakgoz and Beasley ([2009](https://arxiv.org/html/2601.03927v1#bib.bib13)) | Mixed-integer programming approaches for index tracking and | 192 |
|  |  | enhanced indexation |  |
| Cointegration | Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib58)) | Index tracking and enhanced indexing using cointegration | 26 |
|  | and correlation with endogenous portfolio selection |
| Acosta-González et al. ([2015](https://arxiv.org/html/2601.03927v1#bib.bib1)) | On the index tracking and the statistical arbitrage choosing | 12 |
|  | the stocks by means of cointegration: the role of stock picking |
| Sant’Anna et al. ([2020b](https://arxiv.org/html/2601.03927v1#bib.bib60)) | Solving the index tracking problem based on a convex | 5 |
|  | reformulation for cointegration |  |
| Regularization | Wu et al. ([2014a](https://arxiv.org/html/2601.03927v1#bib.bib76)) | Nonnegative-lasso and application in index tracking | 79 |
| Fastrich et al. ([2014](https://arxiv.org/html/2601.03927v1#bib.bib24)) | Cardinality versus q-norm constraints for index tracking | 48 |
| Wu and Yang ([2014](https://arxiv.org/html/2601.03927v1#bib.bib75)) | Nonnegative Elastic Net and application in index tracking | 44 |
| Sant’Anna et al. ([2020a](https://arxiv.org/html/2601.03927v1#bib.bib59)) | Lasso-based index tracking and statistical arbitrage long-short | 23 |
|  |  | strategies |  |
| Factor based | Corielli and Marcellino ([2006](https://arxiv.org/html/2601.03927v1#bib.bib17)) | Factor based index tracking | 68 |
| Kwon and Wu ([2017](https://arxiv.org/html/2601.03927v1#bib.bib41)) | Factor-based robust index tracking | 15 |
| Quantile Regression | Mezali and Beasley ([2013](https://arxiv.org/html/2601.03927v1#bib.bib47)) | Quantile regression for index tracking and enhanced indexation | 33 |
| Li ([2020](https://arxiv.org/html/2601.03927v1#bib.bib43)) | Efficient sparse portfolios based on composite quantile | 5 |
|  | regression for high-dimensional index tracking |  |
| Aguilar et al. ([2022](https://arxiv.org/html/2601.03927v1#bib.bib2)) | Creating better tracking portfolios with quantiles | 2 |

### 3.2 Statistical based index tracking optimization models

Statistical modeling approaches leverage regression-based techniques and statistical properties inherent in financial data to construct index-tracking portfolios. Unlike traditional optimization models, these approaches focus on establishing statistical relationships between asset returns and the benchmark index, offering robust performance in capturing complex dependencies. Prominent methods in this category include least squares regression, quantile regression, co-integration analysis, and regularized regression models such as LASSO and Elastic Net; with top articles listed in Table [4](https://arxiv.org/html/2601.03927v1#S3.T4 "Table 4 ‣ Different tracking error functions and their corresponding optimization framework ‣ 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"). In the following, we briefly describe each of these statistical methodologies and discuss their formulations and applications in the index-tracking literature.

1. 1.

   Regression based models: Regression-based methods provide a natural and intuitive framework for modeling the relationship between individual asset returns and the benchmark index. By expressing each asset’s return as a linear function of the index return, regression captures how closely the asset co-moves with the market—quantified through the slope and intercept coefficients. In the context of index tracking, this approach is particularly valuable because it enables the construction of portfolios whose aggregated return dynamics mimic those of the benchmark. Such regression-based formulations thus bridge statistical estimation and portfolio optimization, offering both interpretability and tractability. Two popular regression based approaches include the least squares regression (LSR) and quantile regression (QR), discussed below.

   #### (a) Least squares regression approach

   The LSR approach, proposed by Canakgoz and Beasley ([2009](https://arxiv.org/html/2601.03927v1#bib.bib13)), formulates the index tracking problem as a regression-based optimization model. Initially, each asset’s returns are individually regressed against the benchmark index returns, resulting in a linear regression equation for each asset as:

   |  |  |  |
   | --- | --- | --- |
   |  | ri​t=αi+βi​It+ϵi​t,i=1,2,…,n;t=1,2,…,T,r\_{it}=\alpha\_{i}+\beta\_{i}I\_{t}+\epsilon\_{it},\quad i=1,2,\ldots,n;\quad t=1,2,\ldots,T, |  |

   where αi\alpha\_{i} and βi\beta\_{i} are respectively the intercept and slope coefficients for asset ii, and ϵi​t\epsilon\_{it} is the regression residual. From these asset-specific regressions, the tracking portfolio’s overall intercept (α^)(\hat{\alpha}) and slope (β^)(\hat{\beta}) are defined as weighted sums of individual intercepts and slopes:

   |  |  |  |
   | --- | --- | --- |
   |  | α^=∑i=1nwi​αi,β^=∑i=1nwi​βi.\hat{\alpha}=\sum\_{i=1}^{n}w\_{i}\alpha\_{i},\quad\hat{\beta}=\sum\_{i=1}^{n}w\_{i}\beta\_{i}. |  |

   The goal of the LSR model for index tracking is to find an optimal subset of KK assets whose weighted returns replicate the benchmark index as closely as possible, ideally achieving a portfolio intercept of zero (α^=0)(\hat{\alpha}=0) and slope of one (β^=1)(\hat{\beta}=1). However, for real-life data this may not be achievable. To achieve this, the authors suggest a number of ways, one of which they adopt is a two-stage approach, where the primary objective is to attain the desired intercept of zero and the secondary objective is to achieve the desired slope of one, that is : first minimize |α^−0||\hat{\alpha}-0| and then minimize |β^−1|.|\hat{\beta}-1|. Though the modulus objectives are non-linear, they can be linearized by introducing auxiliary variables dd and ee, such that

   |  |  |  |
   | --- | --- | --- |
   |  | d≥α^,d≥−α^,e≥β^−1,e≥−β^+1,d≥0,e≥0\displaystyle d\geq\hat{\alpha},\qquad d\geq-\hat{\alpha},\qquad e\geq\hat{\beta}-1,\qquad\ e\geq-\hat{\beta}+1,\qquad d\geq 0,\qquad e\geq 0 |  |

   The problem thus reduces into two linear programs, solved in two stages as follows:
     
   Stage 1 (Minimizing Intercept): In the first stage, the intercept α^\hat{\alpha} is minimized subject to cardinality and holding constraints:

   |  |  |  |
   | --- | --- | --- |
   |  | (LSR1)   Min ​d\qquad\ \text{(LSR1) \ \qquad Min \quad}d\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")),

   |  |  |  |
   | --- | --- | --- |
   |  | d≥∑i=1nwi​αi,d≥−∑i=1nwi​αi.d\geq\sum\limits\_{i=1}^{n}w\_{i}\alpha\_{i},\quad d\geq-\sum\limits\_{i=1}^{n}w\_{i}\alpha\_{i}.\quad |  |

   The optimal intercept value from this stage is denoted as αopt\alpha^{\text{opt}}.
     
   Stage 2 (Minimizing Slope Deviation): In the second stage, the model minimizes the deviation of the portfolio slope β^\hat{\beta} from one, given that the intercept is fixed at its optimal value from Stage 1:

   |  |  |  |
   | --- | --- | --- |
   |  | (LSR2)   Min ​e\qquad\ \text{(LSR2) \ \qquad Min \quad}e\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")),  α^=αopt,\hat{\alpha}=\alpha^{\text{opt}},

   |  |  |  |
   | --- | --- | --- |
   |  | e≥∑i=1nwi​βi−1,e≥−∑i=1nwi​βi+1.e\geq\sum\limits\_{i=1}^{n}w\_{i}\beta\_{i}-1,\quad e\geq-\sum\limits\_{i=1}^{n}w\_{i}\beta\_{i}+1. |  |

   The final portfolio obtained from Stage 2 provides the least squares regression-based tracking portfolio, which closely replicates the benchmark index by minimizing deviations in both intercept and slope.

   #### (b) Quantile regression approach

   Quantile regression (QR) extends the standard least squares regression by modeling the quantiles of a response variable as a function of the independent variables. This approach allows one to capture distributional characteristics of asset returns beyond the conditional mean, making it particularly useful in the presence of skewness or heteroskedasticity. For a given quantile level τ∈(0,1)\tau\in(0,1), the τ\tau-th conditional quantile of the return on asset ii at time tt is modeled as

   |  |  |  |
   | --- | --- | --- |
   |  | Qτ​(ri​t∣It)=αi​τ+βi​τ​It,i=1,…,n;t=1,…,T,Q\_{\tau}(r\_{it}\mid I\_{t})=\alpha\_{i\tau}+\beta\_{i\tau}I\_{t},\quad i=1,\dots,n;\quad t=1,\dots,T, |  |

   where αi​τ\alpha\_{i\tau} represents the intercept and βi​τ\beta\_{i\tau} represents the slope of the τ\tau-th quantile regression line. For each asset ii, the coefficients αi​τ\alpha\_{i\tau} and βi​τ\beta\_{i\tau} are obtained by
   minimizing the quantile loss function:

   |  |  |  |
   | --- | --- | --- |
   |  | minαi,βi⁡[τ​∑t:ut≥0|ut|+(1−τ)​∑t:ut<0|ut|],\min\_{\alpha\_{i},\beta\_{i}}\left[\tau\sum\_{t:u\_{t}\geq 0}|u\_{t}|+(1-\tau)\sum\_{t:u\_{t}<0}|u\_{t}|\right], |  |

   where ut=ri​t−αi​τ−βi​τ​Itu\_{t}=r\_{it}-\alpha\_{i\tau}-\beta\_{i\tau}I\_{t} are the quantile regression residuals. This asymmetric loss penalizes underestimation and overestimation differently, depending on τ\tau.
   The problem can be expressed equivalently as a linear program by introducing nonnegative variables ut+u\_{t}^{+} and ut−u\_{t}^{-}, representing the positive and negative parts of the residuals such that ut=ut+−ut−u\_{t}=u\_{t}^{+}-u\_{t}^{-}:

   |  |  |  |
   | --- | --- | --- |
   |  | minαi​τ,βi​τ,ut+,ut−⁡[τ​∑t=1Tut++(1−τ)​∑t=1Tut−]\min\_{\alpha\_{i\tau},\beta\_{i\tau},u\_{t}^{+},u\_{t}^{-}}\left[\tau\sum\_{t=1}^{T}u\_{t}^{+}+(1-\tau)\sum\_{t=1}^{T}u\_{t}^{-}\right] |  |

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | s.t.ut+\displaystyle\text{s.t.}\quad u\_{t}^{+} | ≥ri​t−αi​τ−βi​τ​It,\displaystyle\geq r\_{it}-\alpha\_{i\tau}-\beta\_{i\tau}I\_{t}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ut−\displaystyle u\_{t}^{-} | ≥−(ri​t−αi​τ−βi​τ​It),\displaystyle\geq-(r\_{it}-\alpha\_{i\tau}-\beta\_{i\tau}I\_{t}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ut+\displaystyle u\_{t}^{+} | ,ut−≥0.\displaystyle,\ u\_{t}^{-}\geq 0. |  |

   Solving the linear problem yields the asset-specific optimal coefficients αi​τ\alpha\_{i\tau} and βi​τ\beta\_{i\tau}. At the portfolio level, the aggregated quantile regression line at level τ\tau is approximated as a weighted combination of the asset-specific estimates:

   |  |  |  |
   | --- | --- | --- |
   |  | α^​(τ)=∑i=1nwi​αi​τ,β^​(τ)=∑i=1nwi​βi​τ,\hat{\alpha}(\tau)=\sum\_{i=1}^{n}w\_{i}\alpha\_{i\tau},\quad\hat{\beta}(\tau)=\sum\_{i=1}^{n}w\_{i}\beta\_{i\tau}, |  |

   These aggregated values provide a linear approximation to the τ\tau-th quantile of the portfolio return, allowing us to construct portfolios for index tracking (τ=0.5\tau=0.5) or enhanced indexation (τ<0.5\tau<0.5) (Mezali and Beasley, [2013](https://arxiv.org/html/2601.03927v1#bib.bib47)).

   The objective is to construct a tracking portfolio whose intercept is as close to zero as possible, and whose slope approximates to one at the chosen quantile level τ\tau. Following a two-stage optimization analogous to the least squares method (Canakgoz and Beasley, [2009](https://arxiv.org/html/2601.03927v1#bib.bib13)), the formulation takes a two stage formulation to first minimize |α^​(τ)−0||\hat{\alpha}(\tau)-0| and then minimize |β​(τ)^−1||\hat{\beta(\tau)}-1|, both linear programs.

   Stage 1 (Minimizing intercept at quantile τ\tau):
   The first stage minimizes the absolute intercept deviation |α^​(τ)−0||\hat{\alpha}(\tau)-0| to find a portfolio with a quantile regressed intercept as close to zero as possible. Similar to LSR, the problem is linearized by introducing auxiliary variable d≥0d\geq 0 and solving:

   |  |  |  |
   | --- | --- | --- |
   |  | (QR1)   Min ​d\qquad\ \text{(QR1) \ \qquad Min \quad}d\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")),

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1nwi​αi​τ−d≤0,∑i=1nwi​αi​τ+d≥0.\sum\_{i=1}^{n}w\_{i}\alpha\_{i\tau}-d\leq 0,\quad\sum\_{i=1}^{n}w\_{i}\alpha\_{i\tau}+d\geq 0.\quad |  |

   Let d∗d^{\*} denote the optimal intercept deviation from Stage 1.

   Stage 2 (Minimizing slope deviation at quantile τ\tau): The second stage minimizes |β^​(τ)−1||\hat{\beta}(\tau)-1| to find a portfolio with a quantile regressed slope as close to one as possible, while retaining the optimal intercept deviation of d∗d^{\*} from stage 1. Again, linearizing the problem by introducing variable e≥0e\geq 0 and solving:

   |  |  |  |
   | --- | --- | --- |
   |  | (QR2)   Min ​e\qquad\ \text{(QR2) \ \qquad Min \quad}e\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad |  |

   subject to ([2](https://arxiv.org/html/2601.03927v1#S3.E2 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))-([5](https://arxiv.org/html/2601.03927v1#S3.E5 "In 3.1 Optimization based framework ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")),  ∑i=1nwi​αi​τ=d∗,\sum\_{i=1}^{n}w\_{i}\alpha\_{i\tau}=d^{\*},

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1nwi​βi​τ−e≤1,∑i=1nwi​βi​τ+e≥1.\sum\_{i=1}^{n}w\_{i}\beta\_{i\tau}-e\leq 1,\quad\sum\_{i=1}^{n}w\_{i}\beta\_{i\tau}+e\geq 1. |  |

   This two-stage quantile regression framework provides a robust tracking portfolio designed to replicate benchmark index returns at specific quantiles, allowing investors to better manage distributional risks. It can further accommodate transaction costs and other realistic constraints, demonstrating flexibility for practical portfolio management applications.
2. 2.

   Regression with regularization models: Regression models with regularization techniques have gained considerable attention in index tracking literature due to their ability to efficiently handle high-dimensional datasets and prevent overfitting. Regularization introduces penalty terms into the objective function, promoting sparse solutions that result in simpler, more interpretable portfolios. Popular regularization methods in portfolio selection include LASSO (Least Absolute Shrinkage and Selection Operator) and elastic net, which enforce sparsity by penalizing portfolio weights through ℓ1\ell\_{1} and combined ℓ1\ell\_{1}-ℓ2\ell\_{2} norms, respectively. Such approaches are particularly beneficial for constructing sparse portfolios from large market indices by selecting a limited subset of representative assets while maintaining tracking accuracy. In what follows, ∥⋅∥1\|\cdot\|\_{1} and ∥⋅∥2\|\cdot\|\_{2} denote the ℓ1\ell\_{1} and ℓ2\ell\_{2} norms, respectively, where

   |  |  |  |
   | --- | --- | --- |
   |  | ‖x‖1=∑i=1n|xi|and‖x‖2=∑ixi2.\|x\|\_{1}=\sum\_{i=1}^{n}|x\_{i}|\quad\text{and}\quad\|x\|\_{2}=\sqrt{\sum\_{i}x\_{i}^{2}}. |  |

   #### (a) Non-negative LASSO

   Non-negative LASSO, introduced by Wu et al. ([2014a](https://arxiv.org/html/2601.03927v1#bib.bib76)), presents an effective two-stage approach for sparse portfolio construction in the index tracking context. The central idea is to first select a subset of KK representative assets (where KK is the desired cardinality) from a large pool, and subsequently determine the optimal weights that track the benchmark index efficiently.

   In the first stage, asset selection is performed using the following non-negative LASSO regression model:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (NNL)minw≥0⁡1T​‖I−Rw‖22+λ​‖w‖1,\text{(NNL)}\qquad\qquad\min\_{w\geq 0}\frac{1}{T}\|I-R\_{w}\|\_{2}^{2}+\lambda\|w\|\_{1}, |  | (10) |

   The parameter λ≥0\lambda\geq 0 controls the trade-off between portfolio sparsity (asset selection) and the accuracy of tracking the index returns. The model minimizes the mean squared tracking error between the portfolio and index returns while enforcing sparsity through the ℓ1\ell\_{1} penalty. Since the objective combines a convex quadratic loss term with a linear regularization term under non-negativity constraints, this stage constitutes a convex quadratic programming problem. Since the choice of λ\lambda significantly affects asset selection, it is determined via a bisection search algorithm. This iterative approach begins with an interval [λmin,λmax][\lambda\_{\text{min}},\lambda\_{\text{max}}], systematically narrowing this interval by repeatedly solving the non-negative LASSO problem at midpoint values λmid\lambda\_{\text{mid}}, until a portfolio of the desired cardinality is obtained.

   Once the set of candidate assets is selected from the first stage, the second stage involves refining portfolio weights by solving the following non-negative least squares regression problem:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (NNLS)minw𝒮≥0⁡1T​‖I−R𝒮‖22,\text{(NNLS)}\qquad\qquad\min\_{w\_{\small{\mathcal{S}}}\geq 0}\frac{1}{T}\|I-R^{\mathcal{S}}\|\_{2}^{2}, |  | (11) |

   where R𝒮R\_{\mathcal{S}} denotes the portfolio return corresponding to the assets selected in stage one, and w𝒮w\_{\mathcal{S}} are their proportional weights. This formulation minimizes the mean squared tracking error between the portfolio returns of the selected subset and the index returns. The problem remains a convex quadratic program, solvable efficiently using standard numerical solvers. In our implementation, we employ the nnls() function from the nnls package in R, which computes the non-negative least squares solution through an active-set algorithm. The coefficients are subsequently normalized for the portfolio weights to sum to one. This second-stage optimization improves tracking accuracy by determining the optimal allocation among the pre-selected assets.

   The two-stage non-negative LASSO methodology thus achieves a sparse, interpretable, and practically efficient index tracking portfolio, making it especially suitable for high-dimensional indexes such as the S&P 500 and Russell 2000.

   #### (b) Non-negative elastic net

   While the non-negative Lasso is effective for selecting a sparse set of assets, it may face challenges in scenarios where predictors are highly correlated. To address this limitation, Wu and Yang ([2014](https://arxiv.org/html/2601.03927v1#bib.bib75)) introduced the non-negative Elastic Net (NN-EN), which combines the ℓ1\ell\_{1} and ℓ2\ell\_{2} penalties of the Lasso and ridge regressions, respectively. The general formulation of the non-negative Elastic Net is given as:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (NN-EN)minw≥0⁡‖I−Rw‖22+λ1​‖w‖1+λ2​‖w‖22,\text{(NN-EN)}\qquad\min\_{w\geq 0}\left\|I-R\_{w}\right\|\_{2}^{2}+\lambda\_{1}\|w\|\_{1}+\lambda\_{2}\|w\|\_{2}^{2}, |  | (12) |

   where λ1,λ2≥0\lambda\_{1},\lambda\_{2}\geq 0 are the regularization parameters controlling sparsity and shrinkage, respectively. The ℓ1\ell\_{1} norm (‖w‖1\|w\|\_{1}) encourages sparsity, and the ℓ2\ell\_{2} norm (‖w‖22\|w\|\_{2}^{2}) helps stabilize the solution by grouping correlated predictors, thereby enhancing the robustness of asset selection.

   Similar to the non-negative Lasso, the NN-EN estimator typically involves a two-stage optimization strategy for index tracking:

   * •

     Stage 1 (Asset selection): The (NN-EN) problem in Eqn. ([12](https://arxiv.org/html/2601.03927v1#S3.E12 "In (b) Non-negative elastic net ‣ (a) Non-negative LASSO ‣ item 2 ‣ 3.2 Statistical based index tracking optimization models ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")) is solved to identify a sparse subset of candidate assets. The tuning parameters λ1\lambda\_{1} and λ2\lambda\_{2} are optimized through a grid-and-bisection search: for each λ2\lambda\_{2} in a predefined grid, a bisection search is performed over λ1\lambda\_{1} to ensure that the number of selected assets does not exceed a cardinality constraint KK. This adaptive search mechanism ensures that the final model yields at most KK non-zero weights, balancing sparsity and accuracy.
   * •

     Stage 2 (Optimal weight estimation): Once the subset assets are selected, the optimal weights are computed by solving a constrained non-negative least squares (NNLS) problem (i.e. Eq. ([11](https://arxiv.org/html/2601.03927v1#S3.E11 "In (a) Non-negative LASSO ‣ item 2 ‣ 3.2 Statistical based index tracking optimization models ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"))). This step (solving (NNLS) problem) determines the optimal portfolio weights that best replicate the index returns, using only the assets selected in Stage 1.

   This hybrid NN-EN + NNLS procedure leverages the strength of NN-EN to select assets with stable, correlated return series while retaining interpretability through non-negativity and sparsity. Empirical results in Wu and Yang ([2014](https://arxiv.org/html/2601.03927v1#bib.bib75)) demonstrate that the NN-EN approach achieves superior tracking performance relative to the non-negative Lasso, particularly in markets where asset returns exhibit strong cross-correlation.
3. 3.

   Co-integration based models: Co-integration is a statistical concept, originally introduced by Granger ([1981](https://arxiv.org/html/2601.03927v1#bib.bib33)), and further developed by Engle and Granger ([1987](https://arxiv.org/html/2601.03927v1#bib.bib22)) that builds on the concept that a linear combination of two or more non-stationary time series might be stationary, indicating a shared long-term trend. In financial markets, where stock prices often exhibit non-stationary behavior, co-integration helps in determining a common trend among different stocks, facilitating in predicting future movements. In simpler words, if two stocks are co-integrated, it means they move together over time. Within the context of index tracking, co-integration can be applied to identify stocks whose prices move closely with respect to the market index. For time series XtX\_{t} and YtY\_{t}, if a linear combination β1​Xt+β2​Yt\beta\_{1}X\_{t}+\beta\_{2}Y\_{t} is stationary, then XtX\_{t} and YtY\_{t} are said to be co-integrated. We investigate the following two methods that utilize co-integration to generate tracking portfolios, proposed by Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib58)) and Sant’Anna et al. ([2020b](https://arxiv.org/html/2601.03927v1#bib.bib60)).

   #### (a) Simulations based co-integration approach

   The theoretical foundation of cointegration, introduced by Engle and Granger ([1987](https://arxiv.org/html/2601.03927v1#bib.bib22)) showed that even though individual time series may be non-stationary, certain linear combinations of them can be stationary. This implies that a portfolio composed of such assets maintains a long-term equilibrium with the benchmark index. Following this principle, Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib58)) proposed a simulation-based co-integration framework for index tracking. The approach assumes that both the index and the constituent asset price series are integrated of order one, i.e., I​(1)I(1), and that their logarithms can be linearly related through a co-integrating vector. Formally, the long-run relationship is modeled as:

   |  |  |  |
   | --- | --- | --- |
   |  | log⁡(Jt)=β0+∑i=1nβi​log⁡(pi​t)+εt,\log(J\_{t})=\beta\_{0}+\sum\_{i=1}^{n}\beta\_{i}\log(p\_{it})+\varepsilon\_{t}, |  |

   where JtJ\_{t} denotes the index price level at time tt, pi,tp\_{i,t} is the price of asset ii, βi\beta\_{i} are the co-integration coefficients, and εt\varepsilon\_{t} represents the deviation from the long-run equilibrium. If the residual series εt\varepsilon\_{t} is stationary, then the index and the selected assets are said to be co-integrated.

   The methodology developed by Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib58)) consists of repeatedly selecting random subsets of assets and testing whether the corresponding linear combination with the index satisfies the co-integration condition. Specifically, the approach involves the following steps, performed over each training window:

   1. (1)

      Random asset selection: Randomly select a subset SS of KK assets from the full universe of nn assets (where KK is the desired cardinality).
   2. (2)

      Co-integration regression: Estimate the long-run relationship for the selected subset SS using ordinary least squares:

      |  |  |  |
      | --- | --- | --- |
      |  | log⁡(Jt)=β0+log⁡(PtS)​β+εt,\log(J\_{t})=\beta\_{0}+\log(P^{S}\_{t})\beta+\varepsilon\_{t}, |  |

      where log⁡(Pt𝒮)\log(P^{\mathcal{S}}\_{t}) are the log prices of selected assets in SS and εt\varepsilon\_{t} captures deviations from the long-run equilibrium between the index and the selected assets.
   3. (3)

      Stationarity test: The stationarity of the residuals εt\varepsilon\_{t} is tested using the Augmented Dickey–Fuller (ADF) test. Subsets for which the null of a unit root is rejected at the 5%5\% level (p<0.05p<0.05) are retained as candidate co-integrated portfolios.
   4. (4)

      Simulations based portfolio selection: The above procedure is repeated for a sufficiently large number of iterations (random subsets). Among all subsets that satisfy the ADF stationarity condition, the optimal portfolio is chosen as the one with the smallest sum of squared residuals (SSR), i.e., min​∑tεt2\min\sum\_{t}\varepsilon\_{t}^{2}. The regression coefficients βj\beta\_{j} from the optimal regression are then normalized to determine the portfolio weights as

      |  |  |  |
      | --- | --- | --- |
      |  | wj=βj∑i=1Kβi,j=1,…,K.w\_{j}=\frac{\beta\_{j}}{\sum\_{i=1}^{K}\beta\_{i}},\quad j=1,\ldots,K. |  |

      The normalized weights wjw\_{j} are assigned to the corresponding selected subset of assets, while all non-selected assets receive a weight of zero.

   The simulation-based search allows for an efficient exploration of possible asset combinations, accommodating large universes where exhaustive co-integration testing would be computationally infeasible. The resulting co-integrated portfolios have been shown to provide stable tracking performance and improved out-of-sample behavior, particularly in non-stationary markets where traditional variance-based approaches fail to capture long-run dependencies.

   #### (b) Convex co-integration model

   To overcome the limitation of the traditional co-integration based index tracking model that require an ex-ante stock selection, Sant’Anna et al. ([2020b](https://arxiv.org/html/2601.03927v1#bib.bib60)) developed a convex mixed-integer non-linear programming (MINLP) formulation that endogenously determines the composition of the tracking portfolio. The model extends the framework of Sant’Anna et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib58)) by embedding a cardinality constraint directly within the optimization problem, thereby allowing simultaneous estimation of the co-integrating vector and the subset of assets included in the portfolio.

   Starting from the co-integration regression framework introduced earlier,

   |  |  |  |
   | --- | --- | --- |
   |  | log⁡(Jt)=β0+∑i=1nβi​log⁡(pi​t)+εt,\log(J\_{t})=\beta\_{0}+\sum\_{i=1}^{n}\beta\_{i}\log(p\_{it})+\varepsilon\_{t}, |  |

   the residual term εt\varepsilon\_{t} represents deviations from the long-run equilibrium. The optimization objective is to minimize the sum of squared residuals over all time periods, ensuring that the selected assets jointly produce a stationary combination with the benchmark index. This leads to the following convex MINLP formulation

   |  |  |  |
   | --- | --- | --- |
   |  | (Cvx-CoInt) min​∑t=1T[log⁡(Jt)−β0−∑i=1nβi​log⁡(pi​t)]2\text{(Cvx-CoInt) \ }\quad\min\;\sum\_{t=1}^{T}\left[\log(J\_{t})-\beta\_{0}-\sum\_{i=1}^{n}\beta\_{i}\log(p\_{it})\right]^{2}\qquad\qquad\qquad\qquad\qquad |  |

   subject to

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1nμi=K,μi∈{0,1},βi≥0,βi≤μi,i=1,…,n,\qquad\quad\quad\qquad\sum\_{i=1}^{n}\mu\_{i}=K,\quad\mu\_{i}\in\{0,1\},\quad\beta\_{i}\geq 0,\quad\beta\_{i}\leq\mu\_{i},\quad i=1,\ldots,n, |  |

   where μi\mu\_{i} is a binary decision variable indicating whether asset ii is included in the tracking portfolio, and KK specifies the desired number of assets. The non-negativity constraints on βi\beta\_{i} enforces a no short-selling restriction, ensuring practical applicability.

   The convexity of the objective function can be established by expressing it in a matrix form as

   |  |  |  |
   | --- | --- | --- |
   |  | y=A​x+b,y=Ax+b, |  |

   where y=log⁡(J)y=\log(J), A=log⁡(P)A=\log(P) is the matrix of log-prices of nn assets, and x=βx=\beta is the coefficient vector. Defining the least-squares objective function as

   |  |  |  |
   | --- | --- | --- |
   |  | f​(x)=‖y−A​x‖22=(y−A​x)⊤​(y−A​x),f(x)=\|y-Ax\|\_{2}^{2}=(y-Ax)^{\top}(y-Ax), |  |

   the Gradient and Hessian with respect to xx are given by

   |  |  |  |
   | --- | --- | --- |
   |  | ∇f​(x)=−2​A⊤​(y−A​x),∇2f​(x)=2​A⊤​A.\nabla f(x)=-2A^{\top}(y-Ax),\qquad\nabla^{2}f(x)=2A^{\top}A. |  |

   The second-order conditions confirm that the problem is convex for any AA since A⊤​AA^{\top}A is positive semi-definite (Boyd and Vandenberghe, [2004](https://arxiv.org/html/2601.03927v1#bib.bib11)). The resulting convex MINLP reformulation eliminates the random selection step used in the earlier simulation-based approach, producing tracking portfolios that are both stable and computationally efficient. Empirical evidence presented by Sant’Anna et al. ([2020b](https://arxiv.org/html/2601.03927v1#bib.bib60)) shows that this convex optimization-based formulation achieves lower turnover and smaller tracking errors, both in-sample and out-of-sample, compared to traditional co-integration portfolios.
4. 4.

   Factor-based model: Factor based models, introduced by Corielli and Marcellino ([2006](https://arxiv.org/html/2601.03927v1#bib.bib17)) represent a powerful statistical framework for constructing low-dimensional index tracking portfolios. These models exploit the idea that a small number of latent common factors drive the co-movements of asset prices, enabling the construction of parsimonious tracking portfolios that effectively replicate the benchmark index’s behavior. By identifying the assets most closely aligned with these factors, one can build portfolios that effectively replicate the benchmark index. Unlike traditional optimization based models that operate directly on returns, this approach first models the underlying structure of log prices to identify representative assets before performing the final tracking optimization using simple returns.

   Formally, let XX be the (T×n)(T\times n) matrix representing the log prices of nn candidate assets observed over TT time periods. Principal Component Analysis (PCA) is applied to extract the primary common factors affecting asset prices:

   |  |  |  |
   | --- | --- | --- |
   |  | X=F​LT+E,X=FL^{T}+E, |  |

   where FF is the (T×k)(T\times k) matrix of common factors (principal components), LL is the (n×k)(n\times k) matrix of factor loadings, and EE denotes the T×nT\times n matrix of idiosyncratic errors. The number of extracted factors kk is typically chosen in such a way that they explain a substantial portion of the variation in asset prices. The factor-based index tracking procedure involves the following detailed steps:

   1. (a)

      Factor extraction: PCA is first applied to the log-price matrix XX, yielding the factor matrix FF. These extracted factors capture systematic market behavior and serve as the basis for asset selection.
   2. (b)

      Asset selection via linear regression: For asset selection, each asset’s log prices XiX\_{i} are regressed against the extracted factor series FF using ordinary least squares (OLS) regression

      |  |  |  |
      | --- | --- | --- |
      |  | Xi=F​βi+εi,i=1,…,N,X\_{i}=F\beta\_{i}+\varepsilon\_{i},\quad i=1,\dots,N, |  |

      where βi\beta\_{i} denotes the asset-specific loadings onto common factors and εi\varepsilon\_{i} represents idiosyncratic component, typically assumed to follow a zero-mean noise process. The coefficient of determination Ri2R^{2}\_{i} from each regression quantifies the degree to which the factors explain the iith asset’s price movements, i=1,…,Ni=1,\ldots,N. Assets are ranked by their Ri2R\_{i}^{2} values, and the top KK ( where KK is the desired cardinality) assets are selected and indexed by the subset

      |  |  |  |
      | --- | --- | --- |
      |  | 𝒮={i1,…,iK}.\mathcal{S}=\{i\_{1},\dots,i\_{K}\}. |  |

      This ensures that only assets most closely aligned with the underlying factor structure are retained.
   3. (c)

      Determining final optimal weights: Once the representative assets are identified, their simple returns are used to determine the final portfolio weights. The final portfolio weights ww are obtained by solving the MSE minimization problem:

      |  |  |  |
      | --- | --- | --- |
      |  | minw⁡‖Rt𝒮​w−It‖22,subject towi≥0,∑i∈𝒮wi=1,\min\_{w}\;\|R^{\mathcal{S}}\_{t}w-I\_{t}\|\_{2}^{2},\quad\text{subject to}\quad w\_{i}\geq 0,\quad\sum\_{i\in\mathcal{S}}w\_{i}=1, |  |

        

      where R𝒮R^{\mathcal{S}} is the matrix of returns of the selected assets.

   The factor-based method offers robust and interpretable tracking portfolios, particularly effective in high-dimensional contexts, as demonstrated empirically by Corielli and Marcellino ([2006](https://arxiv.org/html/2601.03927v1#bib.bib17)). This approach effectively combines dimensionality reduction, data-driven asset selection, and constrained optimization, enhancing both in-sample explanatory power and out-of-sample tracking performance. We next explain data-driven methods for index tracking.

   Table 5: Thematic clusters of different statistical and machine learning based approaches for index tracking

   | Theme | Author(s) | Title | TC |
   | --- | --- | --- | --- |
   | Clustering | Dose and Cincotti ([2005](https://arxiv.org/html/2601.03927v1#bib.bib21)) | Clustering of financial time series with application to | 120 |
   |  | index and enhanced index tracking portfolio |
   | Focardi and Fabozzi ([2004](https://arxiv.org/html/2601.03927v1#bib.bib25)) | A methodology for index tracking based on time-series | 53 |
   |  | clustering |  |
   |  | Wu et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib74)) | A constrained cluster-based approach for tracking | 22 |
   |  |  | the S&P 500 index |  |
   | Deep learning | Kim and Kim ([2020](https://arxiv.org/html/2601.03927v1#bib.bib37)) | Index tracking through deep latent representation learning | 33 |
   | Ouyang et al. ([2019](https://arxiv.org/html/2601.03927v1#bib.bib49)) | Index tracking based on deep neural network | 29 |
   | Neural networks | Zheng et al. ([2020a](https://arxiv.org/html/2601.03927v1#bib.bib86)) | Index tracking with cardinality constraints: A stochastic neural | 21 |
   |  | networks approach |  |
   | Kwak et al. ([2021](https://arxiv.org/html/2601.03927v1#bib.bib40)) | Neural network with fixed noise for index-tracking portfolio | 24 |
   |  | optimization |  |
   | Random forest | Yuanyuan Cao and Yang ([2022](https://arxiv.org/html/2601.03927v1#bib.bib80)) | Combining random forest and multicollinearity | 2 |
   |  | modeling for index tracking |  |
   | Topological learning | Goel et al. ([2025](https://arxiv.org/html/2601.03927v1#bib.bib30)) | Sparse Portfolio Selection via topological data |  |
   |  | analysis based clustering |  |
   | Goel et al. ([2026](https://arxiv.org/html/2601.03927v1#bib.bib31)) | Risk reduced sparse index tracking portfolio: A topological |  |
   |  | data analysis approach |  |

### 3.3 Data-driven models for index tracking

In this section, we explore various data-driven methodologies that have emerged prominently in the index tracking literature. Specifically, we focus on selected state-of-the-art approaches spanning deep learning techniques, factor-based models, clustering techniques, random forests, and support vector regression. Table [5](https://arxiv.org/html/2601.03927v1#S3.T5 "Table 5 ‣ item 4 ‣ 3.2 Statistical based index tracking optimization models ‣ 3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") outlines the top data-driven models for index tracking, based on their citations. We now detail the few techniques we have short-listed for the analysis in our review.

1. 1.

   Clustering based approach
     
   Clustering analysis, also known as data segmentation is a technique employed to group assets into homogeneous clusters based on similarity, ensuring that assets within each cluster behave more similarly than those in different clusters. Early works by Focardi and Fabozzi ([2004](https://arxiv.org/html/2601.03927v1#bib.bib25)) and Dose and Cincotti ([2005](https://arxiv.org/html/2601.03927v1#bib.bib21)) introduced clustering techniques into index tracking and enhanced indexing frameworks. In particular, Dose and Cincotti ([2005](https://arxiv.org/html/2601.03927v1#bib.bib21)) applied hierarchical clustering to the data set S&P 500, using two key similarity measures, as follows:

   * •

     Correlation distance on returns: This measure evaluates the similarity of asset return series using the metric

     |  |  |  |
     | --- | --- | --- |
     |  | d​(X,Y)=2​(1−cX​Y),d(X,Y)=\sqrt{2\,(1-c\_{XY})}, |  |

     where cX​Yc\_{XY} is the correlation coefficient between the returns of assets X=(xt)X=\left(x\_{t}\right) and Y=(yt),t=1,2,…,TY=\left(y\_{t}\right),\ t=1,2,\ldots,T.
   * •

     Percentage difference of prices: This alternative measure focuses on asset price levels by comparing percentage differences. The distance is defined as

     |  |  |  |
     | --- | --- | --- |
     |  | d​(X,Y)=min⁡{d1​(X,Y),d2​(X,Y)},d(X,Y)=\min\{d\_{1}(X,Y),d\_{2}(X,Y)\}, |  |

     with

     |  |  |  |
     | --- | --- | --- |
     |  | d1​(X,Y)=mina∈ℝ⁡1T​∑t=1T(xt−a​ytxt)2,d\_{1}(X,Y)=\min\_{a\in\mathbb{R}}\frac{1}{T}\sum\_{t=1}^{T}\left(\frac{x\_{t}-ay\_{t}}{x\_{t}}\right)^{2}, |  |

     and

     |  |  |  |
     | --- | --- | --- |
     |  | d2​(X,Y)=mina∈ℝ⁡1T​∑t=1T(xt−a​yta​yt)2.d\_{2}(X,Y)=\min\_{a\in\mathbb{R}}\frac{1}{T}\sum\_{t=1}^{T}\left(\frac{x\_{t}-ay\_{t}}{ay\_{t}}\right)^{2}. |  |

   Hierarchical clustering starts with each asset in its own cluster and then repeatedly merges the most similar pairs of clusters until there is just one cluster containing all the assets. The results of this process are represented in a diagram called a dendogram. Based on the clustering output, asset selection is carried out using one of two approaches:

   * •

     Clust1: The assets are partitioned into KK clusters, where KK is the desired cardinality and then one asset is randomly chosen from each cluster, giving equal representation to each.
   * •

     Clust2: The assets are grouped into fewer than KK clusters, and selections are made from them in proportion to the cluster size.

   Both clustering-based asset selection methods use the correlation distance metric defined as

   |  |  |  |
   | --- | --- | --- |
   |  | di​j=2​(1−ρi​j),d\_{ij}=\sqrt{2\left(1-\rho\_{ij}\right)}, |  |

   where ρi​j\rho\_{ij} denotes the Pearson correlation between the return series of assets ii and jj. This distance captures similarities in return co-movements and is scale-invariant. Hierarchical clustering is performed using complete linkage, which forms compact and well-separated clusters.
   This clustering-based selection is then followed by an optimization step that minimizes the mean-squared tracking error between the returns of the selected assets and that of the index.
   Indexing the selected set of assets by SS, the final portfolio weights ww are obtained by solving the following MSE minimization problem as:

   |  |  |  |
   | --- | --- | --- |
   |  | minw∥Rt𝒮w−It∥22,subject to∑i∈𝒮wi=1wi≥0,;i∈𝒮\min\_{w}\;\|R^{\mathcal{S}}\_{t}w-I\_{t}\|\_{2}^{2},\quad\text{subject to}\quad\sum\_{i\in\mathcal{S}}w\_{i}=1\;\;w\_{i}\geq 0,;i\in\mathcal{S}\,\quad |  |

     

   where R𝒮R^{\mathcal{S}} is the matrix of returns of the selected assets. This approach thus combines data-driven segmentation with mathematical programming to construct a robust tracking portfolio.
2. 2.

   Sparse support vector regression
     
   Support vector regression (SVR), an extension of support vector machine (SVM) for regression tasks, is built upon the principle of structural risk minimization and is well known for its ability to achieve high generalization performance even with limited data. Owing to its flexibility in modeling non-linear relationships, SVR has been widely used in various fields such as text categorization, image processing, and biomedical data analysis. In the context of index tracking, Takeda et al. ([2010](https://arxiv.org/html/2601.03927v1#bib.bib67)) applied the SVR model to index tracking while De Leone ([2011](https://arxiv.org/html/2601.03927v1#bib.bib19)) formulated a corresponding 0–1 mixed-integer version to insure cardinality restrictions. However, both of these formulations suffered from scalability issues. To address this, Teng et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib70)) proposed two sparse SVR models that incorporate explicit cardinality constraints to construct parsimonious and computationally efficient tracking portfolios.

   1. (a)

      Sparse ϵ\epsilon-SVR model:
        
      The sparse ϵ\epsilon-SVR model aims to minimize the tracking error while enforcing sparsity through an ℓ0\ell\_{0}-norm constraint. The model is formulated as

      |  |  |  |  |
      | --- | --- | --- | --- |
      |  | (SVR-IT)\displaystyle(\text{SVR-IT})\quad | minw,ξ⁡12​‖w‖22+C1​∑t=1T(c​(ξtu)+c​(ξtl))\displaystyle\min\_{w,\,\xi}\;\frac{1}{2}\|w\|\_{2}^{2}+C\_{1}\sum\_{t=1}^{T}\left(c(\xi\_{t}^{u})+c(\xi\_{t}^{l})\right) |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | subject to |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | Rw​t​w−It≤ϵ+ξtu,\displaystyle R\_{wt}w-I\_{t}\leq\epsilon+\xi\_{t}^{u}, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | It−Rw​t​w≤ϵ+ξtl,\displaystyle I\_{t}-R\_{wt}w\leq\epsilon+\xi\_{t}^{l}, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | ξtl,ξtu≥0,t=1,…,T,\displaystyle\xi\_{t}^{l},\xi\_{t}^{u}\geq 0,\quad t=1,\ldots,T, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | eT​w=1,\displaystyle e^{T}w=1, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | ‖w‖0≤K,\displaystyle\|w\|\_{0}\leq K, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | 0≤wj≤u,j=1,…,n.\displaystyle 0\leq w\_{j}\leq u,\quad j=1,\dots,n. |  |

      where ξtu\xi\_{t}^{u} and ξtl\xi\_{t}^{l} are slack variables capturing deviations from the allowable error tolerance. ϵ≥0\epsilon\geq 0 denotes the maximum deviation tolerance where the parameter C1>0C\_{1}>0 is the weight of the deviations larger than a given ϵ\epsilon, c​(ξ)c(\xi) is the loss function of deviation ξ∈ℝ+,\xi\in\mathbb{R}\_{+}, and uu represents an upper bound on asset weights (typically set to prevent excessive concentration). The term ‖w‖0\|w\|\_{0} denotes the number of non-zero elements in ww, enforcing sparsity by limiting the number of assets in the portfolio.

      For convenience, the loss function c​(ξ)c(\xi) adopts the Gaussian form c​(ξ)=12​ξ2c(\xi)=\frac{1}{2}\xi^{2}, yielding a smooth quadratic optimization landscape, resulting in the following optimization model

      |  |  |  |  |
      | --- | --- | --- | --- |
      |  | (ϵ​-SVR)\displaystyle(\epsilon\text{-SVR})\quad | minw,ξ12​‖w‖2+C1​∑t=1T[(Rw​t​w−It−ϵ)+2+(It−Rw​t​w−ϵ)+2]\displaystyle\min\_{w,\xi}\quad\frac{1}{2}\|w\|^{2}+C\_{1}\sum\_{t=1}^{T}\left[(R\_{wt}w-I\_{t}-\epsilon)\_{+}^{2}+(I\_{t}-R\_{wt}w-\epsilon)\_{+}^{2}\right] |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | subject to |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | eT​w=1,\displaystyle e^{T}w=1, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | ‖w‖0≤K,\displaystyle\|w\|\_{0}\leq K, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | 0≤wj≤u,j=1,…,n.\displaystyle 0\leq w\_{j}\leq u,\quad j=1,\dots,n. |  |

      In the ϵ\epsilon-SVR model, the maximum deviation tolerance ϵ\epsilon is a prior parameter. If there does not exist a good estimation of ϵ\epsilon, then this parameter can be treated as a variable, leading to a new model, ν\nu-SVR, explained below.
   2. (b)

      Sparse ν\nu-SVR model:
        
      The second variant introduces flexibility by treating the tolerance level ϵ\epsilon as a decision variable, balancing its value against tracking accuracy through an additional parameter C2C\_{2}. This yields the following sparse version of the ν\nu-SVR model:

      |  |  |  |  |
      | --- | --- | --- | --- |
      |  | (ν​-SVR)\displaystyle(\nu\text{-SVR})\quad | minw,ϵ,ξ12​‖w‖2+C1​∑t=1T[(Rw​t​w−It−ϵ)+2+(It−Rw​t​w−ϵ)+2]+C2​ϵ\displaystyle\min\_{w,\epsilon,\xi}\quad\frac{1}{2}\|w\|^{2}+C\_{1}\sum\_{t=1}^{T}\left[(R\_{wt}w-I\_{t}-\epsilon)\_{+}^{2}+(I\_{t}-R\_{wt}w-\epsilon)\_{+}^{2}\right]+C\_{2}\epsilon |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | subject to |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | eT​w=1,\displaystyle e^{T}w=1, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | ‖w‖0≤K,\displaystyle\|w\|\_{0}\leq K, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | ϵ≥0,\displaystyle\epsilon\geq 0, |  |
      |  |  |  |  |
      | --- | --- | --- | --- |
      |  |  | 0≤wj≤u,j=1,…,n.\displaystyle 0\leq w\_{j}\leq u,\quad j=1,\dots,n. |  |

   In this second formulation, the parameter C2C\_{2} explicitly controls the trade-off between tracking accuracy and model complexity by regulating the allowable tolerance ϵ\epsilon.

   Both sparse-SVR models are inherently non-convex due to the presence of the ℓ0\ell\_{0}-norm. To efficiently solve them, Teng et al. ([2017](https://arxiv.org/html/2601.03927v1#bib.bib70)) adopted the penalty proximal alternating linear minimization (PALM) algorithm combined with a sparse projection operator. This iterative procedure alternates between solving convex subproblems in ww and thresholding to maintain sparsity, achieving convergence to a stationary point. This sparse SVR methodology provides effective and computationally practical solutions to index tracking problems, particularly beneficial in scenarios demanding precise control over portfolio cardinality and tracking accuracy.
3. 3.

   Random forest
     
   Combining machine learning and statistical modeling techniques provides powerful tools for constructing sparse and efficient portfolios, particularly suited for high-dimensional index tracking problems. While SVR offers one such approach to generate sparse tracking portfolios, another promising machine learning framework is based on random forest (RF). Owing to their ensemble nature, RF models can effectively capture nonlinear dependencies, handle multicollinearity, and provide built-in measures of variable importance, making them highly suitable for identifying a small subset of influential assets in large financial universes.

   In this context, Cao et al. ([2022](https://arxiv.org/html/2601.03927v1#bib.bib14)) proposed two hybrid two-stage methodologies that integrate the predictive power of RF with the stability of Ridge regression. The first approach combines RF-based clustering with ridge regression, whereas the second employs RF regression followed by ridge regression. In both strategies, the RF model serves as the machine-learning component that performs asset selection or grouping, while ridge regression constitutes the statistical modeling stage used to estimate optimal portfolio weights. These hybrid frameworks illustrate how the fusion of ensemble learning and regularized regression can yield sparse, robust, and computationally efficient index-tracking portfolios.

   ##### Notation

   Let {h​(R,θk),k=1,2,…,K}\{h(R,\theta\_{k}),\,k=1,2,\ldots,K\} denote the ensemble of KK decision trees in the RF, where R∈ℝT×nR\in\mathbb{R}^{T\times n} represents the matrix of asset returns across TT time periods, and θk\theta\_{k} denotes the parameters of the kk-th tree. Each tree h​(R,θk)h(R,\theta\_{k}) is trained on a bootstrap sample drawn with replacement from the original data. At each node of a decision tree, a random subset of mm features (m≪nm\ll n) is selected, and the feature that maximizes an impurity-reduction criterion, such as information gain, Gini index, or mean squared error (Ayllón-Gavilán et al., [2024](https://arxiv.org/html/2601.03927v1#bib.bib6)) is used for splitting.

   The aggregated RF prediction for an observation RtR\_{t} is obtained by averaging the outputs of all KK trees:

   |  |  |  |
   | --- | --- | --- |
   |  | H​(Rt)=1K​∑k=1Kh​(Rt,θk).H(R\_{t})=\frac{1}{K}\sum\_{k=1}^{K}h(R\_{t},\theta\_{k}). |  |

   The RF model provides a measure of variable (feature) importance by assessing the contribution of each feature to the overall prediction accuracy. This feature-importance ranking serves as the basis for asset selection in the subsequent hybrid RF-based index tracking models.

   #### Random forest clustering combined with ridge regression (RF cluster+ridge)

   The RF cluster + ridge model proposed by Cao et al. ([2022](https://arxiv.org/html/2601.03927v1#bib.bib14)) integrates ensemble learning with penalized regression to identify influential assets and determine stable portfolio weights. The RF component captures nonlinear dependencies and performs feature selection via clustering and variable-importance measures, while ridge regression serves as the statistical optimization step for estimating smooth and robust portfolio weights.

   ##### Step 1. Random forest classification for asset selection

   A RF classifier is trained to predict the direction of the index return (i.e., whether it is positive or negative) using the historical returns comprising of all nn assets. Each input instance consists of a vector of asset returns on a given day, and the corresponding output label is defined as 1 if the index return is positive, and 0 otherwise.

   The classifier is an ensemble of LL decision trees {h​(Rt,θl),l=1,2,…,L}\{h(R\_{t},\theta\_{l}),\,l=1,2,\ldots,L\}, where θl\theta\_{l} denotes the parameters of the ll-th tree. Each tree is trained on a bootstrap sample drawn with replacement from the original data. At every node of a tree, a random subset of m≪nm\ll n features is selected, and the feature that maximizes an impurity-reduction criterion (e.g., the Gini index or classification error) is chosen for splitting.

   For a given observation RtR\_{t}, the final prediction of the ensemble is made by majority voting over all trees:

   |  |  |  |
   | --- | --- | --- |
   |  | H​(Rt)=arg⁡maxy∈{0,1}​∑l=1LI​(h​(Rt,θl)=y),H(R\_{t})=\arg\max\_{y\in\{0,1\}}\sum\_{l=1}^{L}I\big(h(R\_{t},\theta\_{l})=y\big), |  |

   where I​(⋅)I(\cdot) is the indicator function. This ensemble construction reduces variance and avoids overfitting while providing the foundation for feature-importance estimation.

   ##### Step 2. Feature-importance evaluation

   Once the RF classifier is trained, the importance of each asset is quantified using the Mean Decrease in Accuracy (MDA). This metric measures the drop in predictive accuracy when the values of a particular feature (i.e., asset return series) are randomly permuted, thus breaking their relationship with the target variable. Formally, for asset ii, the MDA score is computed as

   |  |  |  |
   | --- | --- | --- |
   |  | MDAi=Accbase−Accperm(i),\text{MDA}\_{i}=\text{Acc}\_{\text{base}}-\text{Acc}\_{\text{perm}}^{(i)}, |  |

   where Accbase\text{Acc}\_{\text{base}} is the baseline accuracy of the RF on the validation data, and Accperm(i)\text{Acc}\_{\text{perm}}^{(i)} is the accuracy obtained after randomly permuting the ii-th feature across the samples. A higher MDAi\text{MDA}\_{i} implies greater relevance of asset ii in predicting index return direction.

   ##### Step 3. Asset-subset selection

   Assets are ranked in descending order of their MDAi\text{MDA}\_{i} scores, and the top KK assets (where KK is the desired cardinality) are selected to form the reduced candidate set 𝒮⊆{1,2,…,n}\mathcal{S}\subseteq\{1,2,\ldots,n\}, where |𝒮|=K|\mathcal{S}|=K.
   This subset represents the assets most strongly associated with index performance.

   ##### Step 4. Ridge regression for portfolio optimization

   Using the selected asset subset 𝒮\mathcal{S}, ridge regression is employed to estimate the optimal tracking portfolio weights by minimizing the mean-squared tracking error with an ℓ2\ell\_{2} penalty to control multicollinearity.
   The optimization problem is formulated as

   |  |  |  |
   | --- | --- | --- |
   |  | w^𝒮=arg⁡minw𝒮≥0⁡{1T​∑t=1T(It−∑i∈𝒮ri​t​wi)2+λ​∑i∈𝒮wi2},\hat{w}\_{\mathcal{S}}=\arg\min\_{w\_{\mathcal{S}}\geq 0}\left\{\frac{1}{T}\sum\_{t=1}^{T}\left(I\_{t}-\sum\_{i\in\mathcal{S}}r\_{it}w\_{i}\right)^{2}+\lambda\sum\_{i\in\mathcal{S}}w\_{i}^{2}\right\}, |  |

   where λ>0\lambda>0 is a regularization parameter controlling shrinkage.

   The regularization parameter λ\lambda is selected via kk-fold cross-validation by minimizing the out-of-sample mean-squared error.
   The resulting weight estimates w^𝒮\hat{w}\_{\mathcal{S}} are then normalized to satisfy the portfolio constraints

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i∈𝒮w^i=1,w^i≥0,\sum\_{i\in\mathcal{S}}\hat{w}\_{i}=1,\qquad\hat{w}\_{i}\geq 0, |  |

   ensuring a fully invested and long-only portfolio.

   This integrated RF cluster + ridge framework exploits the feature-selection ability of RF to identify the most informative assets while using ridge regression to produce stable and interpretable portfolio weights. The combination effectively captures nonlinear dependencies in asset returns and yields sparse yet robust tracking portfolios, making it particularly suitable for high-dimensional index-tracking problems.

   #### Random forest regression combined with ridge regression (RF regression+ridge)

   Similar to the clustering-based method, the RF regression combined with ridge regression approach proposed by Cao et al. ([2022](https://arxiv.org/html/2601.03927v1#bib.bib14)) employs a two-stage strategy that integrates the nonlinear predictive capability of RF with the robustness of ridge regression. Unlike the classification-based strategy, this model directly performs regression to predict the magnitude of index returns, thereby capturing both linear and nonlinear dependencies between asset returns and benchmark index performance.

   ##### Step 1. Random forest regression for asset selection

   A RF regression model is trained to predict the index return series {It}t=1T\{I\_{t}\}\_{t=1}^{T} using historical asset returns {ri​t}\{r\_{it}\} as predictors.
   Let {h​(R,θl),l=1,2,…,L}\{h(R,\theta\_{l}),\,l=1,2,\ldots,L\} denote the ensemble of LL regression trees, each fitted on a bootstrap sample of R∈ℝT×nR\in\mathbb{R}^{T\times n} (the matrix of asset returns).
   For a given observation RtR\_{t}, the predicted index return is obtained by averaging the outputs of all LL trees

   |  |  |  |
   | --- | --- | --- |
   |  | I^t=1L​∑l=1Lh​(Rt,θl).\hat{I}\_{t}=\frac{1}{L}\sum\_{l=1}^{L}h(R\_{t},\theta\_{l}). |  |

   This ensemble approach enables the model to learn complex, nonlinear relationships and interactions among the asset returns, while maintaining generalization through bootstrap aggregation and random feature selection. As in the classification-based approach, the trained model also provides feature-importance scores, which are used to identify a sparse subset of assets for the next stage of the model.

   ##### Step 2. Feature-importance evaluation:

   The contribution of each asset to predicting the index is quantified via the percentage increase in mean squared error (PIM), which evaluates how prediction accuracy deteriorates when the ii-th feature is randomly permuted.
   Formally, for asset ii, the PIMi score is given by

   |  |  |  |
   | --- | --- | --- |
   |  | PIMi=100×1L​∑l=1LMSEl(i,perm)−MSElMSEl,\text{PIM}\_{i}=100\times\frac{1}{L}\sum\_{l=1}^{L}\frac{\text{MSE}\_{l}^{(i,\mathrm{perm})}-\text{MSE}\_{l}}{\text{MSE}\_{l}}, |  |

   where MSEl\text{MSE}\_{l} denotes the mean squared error of the ll-th regression tree, and MSEl(i,perm)\text{MSE}\_{l}^{(i,\mathrm{perm})} is the error after permuting the ii-th feature. Higher PIMi\text{PIM}\_{i} values indicate stronger predictive influence of asset ii on index returns; i=1,…,ni=1,\ldots,n.

   ##### Step 3. Asset-subset selection

   Assets are ranked according to their PIMi\text{PIM}\_{i} values, and the top KK assets are selected to form the subset 𝒮⊆{1,2,…,n}\mathcal{S}\subseteq\{1,2,\ldots,n\} with |𝒮|=K|\mathcal{S}|=K.
   This data-driven selection identifies the most informative assets for replicating the benchmark index.

   ##### Step 4. Ridge regression for portfolio optimization

   Portfolio weights are estimated using the same ridge-regularized tracking error minimization procedure described in the RF cluster + ridge framework.

   By coupling the nonlinear predictive power of RF regression with the regularization strength of ridge regression, this hybrid model produces sparse yet highly stable index-tracking portfolios.
   It efficiently identifies influential assets, mitigates multicollinearity, and improves out-of-sample tracking performance, making it particularly suitable for large-scale, high-dimensional index-tracking applications.
4. 4.

   Deep autoencoders
     
   Autoencoders are a type of neural network designed to learn efficient representations of data. This is achieved by compressing high-dimensional input data into a low-dimensional latent space and then reconstructing the original data from this compressed form. The training process aims to minimize information loss, which can be measured using various loss functions. A common choice is the ℓ2\ell\_{2} -norm difference between the input and output vectors, although other loss functions can also be used (Ouyang et al. ([2019](https://arxiv.org/html/2601.03927v1#bib.bib49)); Kim and Kim ([2020](https://arxiv.org/html/2601.03927v1#bib.bib37)); Zhang et al. ([2020](https://arxiv.org/html/2601.03927v1#bib.bib82))).

   In the context of index tracking, autoencoders are trained using return data from stocks that make up a market index. For a given period tt, the return data is represented as a vector 𝐫t=[r1​t,r2​t,…,rn​t]\mathbf{r}\_{t}=[r\_{1t},r\_{2t},\ldots,r\_{nt}] where ri​tr\_{it} is a return from iith asset at tt.

   The overall loss function for training the autoencoder is defined as the sum of the squared differences (ℓ2\ell\_{2}-norm) between the original return vectors and the reconstructed return vectors across all time periods:

   |  |  |  |
   | --- | --- | --- |
   |  | L=∑t=1T‖𝐫t−𝐫^t‖22L=\sum\_{t=1}^{T}\|\mathbf{r}\_{t}-\hat{\mathbf{r}}\_{t}\|\_{2}^{2} |  |

   where tt is the index for the training samples, 𝐫t\mathbf{r}\_{t} is the original vector of returns for time period tt, and 𝐫^t\hat{\mathbf{r}}\_{t} is the reconstructed vector of returns for time period tt.

   To evaluate the contribution of each stock to the reconstruction, the individual reconstruction loss for each stock is calculated. This helps identify which stocks carry the most communal information related to the benchmark index. The individual loss for stock ii is given by:

   |  |  |  |
   | --- | --- | --- |
   |  | Li=∑t=1T‖ri​t−r^i​t‖22L\_{i}=\sum\_{t=1}^{T}\|r\_{it}-\hat{r}\_{it}\|\_{2}^{2} |  |

   where r^i​t\hat{r}\_{it} is the reconstructed return of asset ii at time tt. The smaller the LiL\_{i} value, the less information is lost for the ii-th asset, indicating it is more similar to the overall index. This information is used to rank the assets based on their communal information with the benchmark index. By selecting the top KK assets with the highest communal information, one can construct a tracking portfolio of KK assets that closely mimics the index. In Zhang et al. ([2020](https://arxiv.org/html/2601.03927v1#bib.bib82)), the authors consider six autoencoder architectures for asset selection, discussed as follows:

   1. (a)

      Single hidden layer autoencoder (SH-AE): This baseline model consists of an encoder–decoder structure with a single hidden (bottleneck) layer comprising of fewer neurons than the input layer. The encoder compresses the standardized asset return data into a low-dimensional latent representation, while the decoder attempts to reconstruct the original inputs from this compressed code. The reconstruction error, measured as the MSE between the input and reconstructed outputs for each asset, serves as a ranking criterion—assets with the lowest reconstruction errors are considered most representative of the underlying market structure.
   2. (b)

      Sparse autoencoder (SP-AE): This model retains the same structure as the single hidden layer autoencoder but introduces an ℓ1\ell\_{1} penalty on the hidden-layer activations to enforce sparsity. This encourages only a few neurons to be active for any given input, thereby promoting feature selectivity and reducing redundancy. By emphasizing the most salient features of asset returns, the sparse autoencoder improves the robustness and interpretability of asset ranking.
   3. (c)

      Contractive autoencoder (CON-AE):
      The contractive autoencoder incorporates a Jacobian-based penalty into the loss function to make the learned representations invariant to small perturbations in the input. Specifically, it penalizes the sensitivity of the encoder to changes in the input by adding a contraction term proportional to the Frobenius norm of the encoder’s Jacobian matrix:

      |  |  |  |
      | --- | --- | --- |
      |  | ‖∂h​(𝐫t)∂𝐫t‖F2,\left\|\frac{\partial h(\mathbf{r}\_{t})}{\partial\mathbf{r}\_{t}}\right\|\_{F}^{2}, |  |

      where h​(⋅)h(\cdot) denotes the encoder mapping. In practice, this Jacobian norm is approximated by the squared Frobenius norm of the encoder weight matrix, serving as an efficient surrogate for local sensitivity. This regularization promotes stability and smoothness in the latent space, making the model particularly effective in identifying assets whose return dynamics exhibit consistent long-term structure.
   4. (d)

      Stacked autoencoder (STCK-AE):
      The stacked autoencoder extends the basic autoencoder architecture by employing multiple nonlinear hidden layers in both the encoder and decoder components. This hierarchical deep structure—typically comprising successive layers of sizes 64, 32, and 16 neurons in the encoder enables the model to extract complex, higher-order correlations among asset returns. By progressively compressing the input data through multiple nonlinear transformations, the model captures both global and local structures in the return dynamics, providing richer latent representations that enhance the identification of assets contributing most to the market’s underlying structure.
   5. (e)

      Denoising autoencoder (DEN-AE):
      The denoising autoencoder enhances robustness by deliberately corrupting the input data with random noise and training the network to reconstruct the original, uncorrupted version. Let the corrupted input be represented as

      |  |  |  |
      | --- | --- | --- |
      |  | 𝐫~t=𝐫t+ηt,\tilde{\mathbf{r}}\_{t}=\mathbf{r}\_{t}+\eta\_{t}, |  |

      where ηt∼𝒩​(0,σ2)\eta\_{t}\sim\mathcal{N}(0,\sigma^{2}) denotes the Gaussian noise added to the original return vector 𝐫t\mathbf{r}\_{t}. The network is trained to minimize the reconstruction error between 𝐫~t\tilde{\mathbf{r}}\_{t} and 𝐫t\mathbf{r}\_{t}, thereby learning noise-invariant and stable representations of asset returns. This process improves the model’s generalization capability and resilience to stochastic fluctuations commonly observed in financial time series.
   6. (f)

      Variational autoencoder (VAR-AE):
      The variational autoencoder introduces a probabilistic latent representation by learning an encoder that maps inputs to a distribution over latent variables rather than a single code. Given a standardized return vector 𝐫t∈ℝn\mathbf{r}\_{t}\in\mathbb{R}^{n}, the encoder outputs the mean and log-variance of a Gaussian latent distribution,

      |  |  |  |
      | --- | --- | --- |
      |  | (𝝁t,log⁡𝝈t2)=fϕ​(𝐫t),(\boldsymbol{\mu}\_{t},\log\boldsymbol{\sigma}^{2}\_{t})=f\_{\phi}(\mathbf{r}\_{t}), |  |

      and a latent sample is obtained via the reparameterization trick,

      |  |  |  |
      | --- | --- | --- |
      |  | 𝐳t=𝝁t+exp⁡(12​log⁡𝝈t2)⊙ϵt,ϵt∼𝒩​(𝟎,I).\mathbf{z}\_{t}=\boldsymbol{\mu}\_{t}+\exp\!\big(\tfrac{1}{2}\log\boldsymbol{\sigma}^{2}\_{t}\big)\odot\boldsymbol{\epsilon}\_{t},\qquad\boldsymbol{\epsilon}\_{t}\sim\mathcal{N}(\mathbf{0},I). |  |

      Here, II is an identity matrix. The decoder gθg\_{\theta} maps 𝐳t\mathbf{z}\_{t} back to the input space to reconstruct 𝐫^t=gθ​(𝐳t)\hat{\mathbf{r}}\_{t}=g\_{\theta}(\mathbf{z}\_{t}).

      Training minimizes a reconstruction term plus a Kullback–Leibler divergence that regularizes the latent distribution towards the standard normal:

      |  |  |  |
      | --- | --- | --- |
      |  | ℒVAE​(θ,ϕ)=∑t=1T‖𝐫t−𝐫^t‖22⏟reconstruction+λKL​∑j=1d12​(μt,j2+σt,j2−log⁡σt,j2−1)⏟KL​(𝒩​(𝝁t,diag​(𝝈t2))∥𝒩​(𝟎,I)),\mathcal{L}\_{\text{VAE}}(\theta,\phi)=\sum\_{t=1}^{T}\underbrace{\big\|\mathbf{r}\_{t}-\hat{\mathbf{r}}\_{t}\big\|\_{2}^{2}}\_{\text{reconstruction}}\;+\;\lambda\_{\mathrm{KL}}\,\underbrace{\sum\_{j=1}^{d}\tfrac{1}{2}\!\left(\mu\_{t,j}^{2}+\sigma\_{t,j}^{2}-\log\sigma\_{t,j}^{2}-1\right)}\_{\mathrm{KL}\big(\mathcal{N}(\boldsymbol{\mu}\_{t},\mathrm{diag}(\boldsymbol{\sigma}^{2}\_{t}))\,\|\,\mathcal{N}(\mathbf{0},I)\big)}, |  |

      where dd is the latent dimension, and λKL>0\lambda\_{\mathrm{KL}}>0 controls the strength of the KL regularization (in code: lambda\_kl).
      This probabilistic bottleneck encourages smooth, disentangled latent factors that capture common market structure while preventing overfitting.

      In implementation, we use a two-layer encoder to produce (𝝁t,log⁡𝝈t2)(\boldsymbol{\mu}\_{t},\log\boldsymbol{\sigma}^{2}\_{t}), apply the reparameterization 𝐳t\mathbf{z}\_{t}, and a two-layer decoder to reconstruct 𝐫^t\hat{\mathbf{r}}\_{t}.

   All autoencoder variants follow the same training and selection pipeline. The models are trained using standardized asset return data, minimizing the mean squared reconstruction error between original and reconstructed returns. For each asset, the average reconstruction loss is computed and used to rank assets according to their similarity to the overall market structure. To balance representativeness and diversity, a mixed selection rule is applied—selecting 70% of assets with the smallest reconstruction errors (communal) and 30% with the largest errors (idiosyncratic). The final selected assets are then passed to the portfolio optimization stage for weight estimation.

   Once a subset of assets is selected (denote by the set as 𝒮\mathcal{S}), the tracking portfolio is determined by an optimization model that minimizes the MSE between the benchmark index returns and the returns generated by the selected assets (see MSE minimization in Section [3](https://arxiv.org/html/2601.03927v1#S3 "3 Evolution of Index Tracking framework ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem")).
5. 5.

   Deep Learning Recently, deep learning techniques, particularly deep neural networks (DNNs), have emerged as powerful tools for asset selection and portfolio construction in index tracking. In this context, Ouyang et al. ([2019](https://arxiv.org/html/2601.03927v1#bib.bib49)) proposed a hybrid two-stage approach integrating deep autoencoders and deep neural networks. This method leverages the representation power of autoencoders for asset selection and the predictive capability of neural networks for portfolio optimization. The framework involves the following sequential steps:

   #### Deep neural network framework

   Ouyang et al. ([2019](https://arxiv.org/html/2601.03927v1#bib.bib49)) propose a deep learning-based two-stage method for index tracking, combining asset selection via a deep autoencoder and portfolio optimization through a deep neural network (DNN). The methodology consists of the following steps:

   1. (a)

      Asset selection with a deep autoencoder

      A deep autoencoder is employed to identify representative assets by reconstructing historical asset returns and selecting those with minimal reconstruction errors. Specifically, given historical asset returns R∈ℝT×nR\in\mathbb{R}^{T\times n}, the autoencoder learns parameters θ\theta that minimize the reconstruction loss:

      |  |  |  |
      | --- | --- | --- |
      |  | minθ⁡‖R−R^‖F2,\min\_{\theta}\|R-\hat{R}\|^{2}\_{F}, |  |

      where R^=gθ​(R)\hat{R}=g\_{\theta}(R) denotes the reconstructed returns, parameterized by weights and biases θ\theta. After training, the reconstruction error for each asset ii is computed as:

      |  |  |  |
      | --- | --- | --- |
      |  | di=1T​∑t=1T(ri​t−r^i​t)2.d\_{i}=\frac{1}{T}\sum\_{t=1}^{T}(r\_{it}-\hat{r}\_{it})^{2}. |  |

      The top hh assets with the lowest reconstruction errors did\_{i} are selected to form the reduced candidate set 𝒮\mathcal{S}.
   2. (b)

      Portfolio weight optimization using DNN

      Using the selected assets 𝒮\mathcal{S}, a feed-forward (DNN) is trained to predict benchmark index returns from the corresponding asset returns. The network parameters ϕ\phi are optimized by minimizing the mean squared error loss:

      |  |  |  |
      | --- | --- | --- |
      |  | minϕ⁡1T​∑t=1T(It−fϕ​(Rt,𝒮))2,\min\_{\phi}\frac{1}{T}\sum\_{t=1}^{T}(I\_{t}-f\_{\phi}(R\_{t,\mathcal{S}}))^{2}, |  |

      where Rt,𝒮R\_{t,\mathcal{S}} denotes the returns of selected assets at time tt, and fϕ​(⋅)f\_{\phi}(\cdot) the DNN prediction function parameterized by ϕ\phi. This step enables the model to capture complex nonlinear dependencies between the selected assets and the benchmark index.
   3. (c)

      Determining portfolio weights through sensitivity analysis

      The trained network is then used to obtain portfolio weights by performing a gradient-based sensitivity of the predicted index return with respect to each input feature. The average absolute gradient for asset ii is computed as

      |  |  |  |
      | --- | --- | --- |
      |  | si=1T​∑t=1T|∂fϕ​(Rt,𝒮)∂ri​t|,i∈𝒮.s\_{i}=\frac{1}{T}\sum\_{t=1}^{T}\left|\frac{\partial f\_{\phi}(R\_{t,\mathcal{S}})}{\partial r\_{it}}\right|,\quad i\in\mathcal{S}. |  |

      These sensitivity scores are normalized to obtain portfolio weights satisfying

      |  |  |  |
      | --- | --- | --- |
      |  | wi=si∑j∈𝒮sj,∑i∈𝒮wi=1,wi≥0.w\_{i}=\frac{s\_{i}}{\sum\_{j\in\mathcal{S}}s\_{j}},\qquad\sum\_{i\in\mathcal{S}}w\_{i}=1,\quad w\_{i}\geq 0. |  |

   This approach effectively leverages deep learning to dynamically select and weight assets, demonstrating strong empirical performance with significantly reduced tracking error and portfolio complexity compared to traditional methods.

   #### Deep neural network with fixed noise (Deep NNF)

   The DNN with fixed noise (Deep-NNF) approach, introduced by Kwak et al. ([2021](https://arxiv.org/html/2601.03927v1#bib.bib40)), provides an innovative method for portfolio selection and index tracking. Unlike conventional feed-forward neural networks that take asset returns as direct inputs, the Deep-NNF model generates portfolio weights through a latent noise vector that is independent of the observed market data. This framework uniquely removes dependency on explicit asset returns as inputs, instead using a fixed, random noise vector as the sole input to a DNN. This noise-driven method inherently emphasizes portfolio diversification and prevents overfitting to historical data.

   The Deep-NNF methodology involves two principal stages, detailed as follows:

   Stage 1: Asset selection via fixed-noise neural network.
     
   Initially, a deep feed-forward neural network f​(⋅)f(\cdot) is constructed with a fixed, randomly generated noise vector ξ∈ℝn\mathbf{\xi}\in\mathbb{R}^{n} serving as its only input. The network architecture consists of multiple fully connected layers with dropout and ReLU activations, formulated as:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝐰=f​(ξ;θ),\mathbf{w}=f(\mathbf{\xi};\theta), |  |

   where θ\theta denotes the network parameters (weights and biases). The output layer employs a softmax activation function to generate valid portfolio weights:

   |  |  |  |
   | --- | --- | --- |
   |  | wi=eui∑j=1Neuj,i=1,…,N,w\_{i}=\frac{e^{u\_{i}}}{\sum\_{j=1}^{N}e^{u\_{j}}},\quad i=1,\dots,N, |  |

   where uiu\_{i} represents the pre-activation output of the final layer for asset ii.
   The network parameters θ\theta are learned by minimizing the mean squared error between the realized portfolio return and the benchmark index return as

   |  |  |  |
   | --- | --- | --- |
   |  | ℒ​(θ)=1T​∑t=1T(It−Rw​t)2.\mathcal{L}(\theta)=\frac{1}{T}\sum\_{t=1}^{T}\big(I\_{t}-R\_{wt}\big)^{2}. |  |

   After training, the top hh assets are selected based on the magnitude of their corresponding portfolio weights.

   Stage 2: Partial replication and portfolio refinement.
     
   In the second stage, the neural network is re-trained exclusively on the returns of the selected hh assets. Specifically, the asset return matrix 𝐫t(h)∈ℝh\mathbf{r}\_{t}^{(h)}\in\mathbb{R}^{h} corresponding to the chosen assets is used, along with a new fixed noise vector ξ(h)∈ℝh\mathbf{\xi}^{(h)}\in\mathbb{R}^{h}. The model again minimizes the mean squared tracking error:

   |  |  |  |
   | --- | --- | --- |
   |  | minθh⁡1T​∑t=1T(It−𝐰h⊤​𝐫t(h))2,\min\_{\theta\_{h}}\frac{1}{T}\sum\_{t=1}^{T}\left(I\_{t}-\mathbf{w}\_{h}^{\top}\mathbf{r}\_{t}^{(h)}\right)^{2}, |  |

   to obtain the refined optimal portfolio weights 𝐰h\mathbf{w}\_{h}.
   Finally, these optimized weights are expanded back into the full-dimensional asset space by assigning zeros to the unselected assets, thus completing the partial replication strategy.
   This two-stage Deep-NNF framework leverages the randomness inherent in the fixed-noise input and the flexibility of deep neural networks to achieve robust and diversified portfolios, demonstrating superior tracking accuracy and generalization compared to traditional index-tracking methods (Kwak et al., [2021](https://arxiv.org/html/2601.03927v1#bib.bib40)).

## 4 Numerical study

To illustrate the practical implications of the reviewed index tracking (IT) models, we conduct a comparative numerical study on the S&P 500 index. The sample comprises daily closing prices of the index and its constituents over a ten-year horizon, from 10 December 2012 to 11 August 2022, covering T=2524T=2524 trading days. For asset i∈{1,…,n}i\in\{1,\ldots,n\} and trading day t∈{1,…,T}t\in\{1,\ldots,T\}, let pi,tp\_{i,t} denote the closing price, with simple daily return

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t=pi,t−pi,t−1pi,t−1.r\_{i,t}=\frac{p\_{i,t}-p\_{i,t-1}}{p\_{i,t-1}}\,. |  | (13) |

Constituents with complete price histories over this horizon are retained, yielding n=462n=462 assets. The period was chosen to maximize the number of constituents with data availability.

### 4.1 Methodology

We evaluate 2929 representative IT models spanning three modeling paradigms: (i) optimization-based approaches (88 models), (ii) statistical-based methods (77 models), and (iii) data-driven methods (1414 models). Each model is evaluated using a rolling-window design: a two-year in-sample window (504504 trading days) followed by a three-month out-of-sample test window (6363 trading days). The window advances by 6363 days, producing a total of 3232 evaluation windows. To ensure comparability, we impose a uniform cardinality constraint of K=45K=45 (approximately 10%10\% of the total number of assets).

Out-of-sample performance is assessed using multiple measures detailed below. In addition, we perform pairwise statistical tests on model tracking errors to evaluate whether observed performance differences are significant. Finally, we conduct a two-stage comparison: (i) within-paradigm assessment to identify the leading model in each class, followed by (ii) a cross-paradigm evaluation of the best representatives. This approach highlights not only absolute performance but also the relative strengths and limitations of optimization-, statistical-, and data-driven frameworks in index tracking.

### 4.2 Performance Metrics

The performance of the tracking portfolios is evaluated using five complementary categories of measures: (i) tracking performance, (ii) return performance, (iii) risk performance, (iv) risk-adjusted performance, and (v) asset-weight characteristics. Let rp,tr\_{p,t} and rb,tr\_{b,t} denote the portfolio and benchmark returns at time tt, respectively, over an out-of-sample evaluation horizon of length HH. The average portfolio return is denoted by r¯p=1H​∑t=1Hrp,t\bar{r}\_{p}=\tfrac{1}{H}\sum\_{t=1}^{H}r\_{p,t}.

1. 1.

   Tracking Performance: To evaluate how closely the portfolio replicates the S&P 500, we use two complementary measures: (i) tracking error, which captures the magnitude of deviations, and (ii) correlation, which reflects directional co-movement.

   1. (a)

      Tracking error (TE):
      TE measures the variability of the active return series (rp,t−rb,t)(r\_{p,t}-r\_{b,t}), i.e., how much the portfolio deviates from the benchmark on average.
      It is given by

      |  |  |  |
      | --- | --- | --- |
      |  | TE=1H−1​∑t=1H((rp,t−rb,t)−(rp−rb)¯)2,\text{TE}=\sqrt{\frac{1}{H-1}\sum\_{t=1}^{H}\Big((r\_{p,t}-r\_{b,t})-\overline{(r\_{p}-r\_{b})}\Big)^{2}}, |  |

      where (rp−rb)¯=1H​∑t=1H(rp,t−rb,t)\overline{(r\_{p}-r\_{b})}=\tfrac{1}{H}\sum\_{t=1}^{H}(r\_{p,t}-r\_{b,t}).
      Smaller TE values indicate closer replication of the benchmark.
   2. (b)

      Correlation with the index:
      Correlation assesses the strength of linear co-movement between the portfolio and the benchmark.
      It is computed as

      |  |  |  |
      | --- | --- | --- |
      |  | ρ​(rp,rb)=Cov⁡(rp,rb)σp​σb,\rho(r\_{p},r\_{b})=\frac{\operatorname{Cov}(r\_{p},r\_{b})}{\sigma\_{p}\sigma\_{b}}, |  |

      where σp\sigma\_{p} and σb\sigma\_{b} are the standard deviations of rp,tr\_{p,t} and rb,tr\_{b,t}.
2. 2.

   Return Performance: To assess the growth potential of the tracking portfolio, we report three simple measures: the average return, the worst observed return, and the best observed return over the evaluation horizon.

   1. (a)

      Average return:
      The mean return r¯p\bar{r}\_{p} (already defined above) provides a measure of the typical performance delivered by the tracking portfolio.
   2. (b)

      Minimum return:
      The lowest single-period return observed,

      |  |  |  |
      | --- | --- | --- |
      |  | rmin=min1≤t≤H⁡rp,t,r\_{\min}=\min\_{1\leq t\leq H}r\_{p,t}, |  |

      capturing the downside extremum.
   3. (c)

      Maximum return:
      The highest single-period return observed,

      |  |  |  |
      | --- | --- | --- |
      |  | rmax=max1≤t≤H⁡rp,t,r\_{\max}=\max\_{1\leq t\leq H}r\_{p,t}, |  |

      indicating the best realized outcome.
3. 3.

   Risk Performance: To evaluate the stability of the tracking portfolio, we consider two measures: volatility (overall variability of returns) and average drawdown (typical losses from peak values).

   1. (a)

      Standard Deviation: A measure of the portfolio’s return volatility, denoted by σp\sigma\_{p}, is calculated as

      |  |  |  |
      | --- | --- | --- |
      |  | σp=1H−1​∑t=1H(rp,t−r¯p)2.\sigma\_{p}=\sqrt{\frac{1}{H-1}\sum\_{t=1}^{H}(r\_{p,t}-\bar{r}\_{p})^{2}}. |  |

      Lower values indicate greater stability in portfolio performance.
   2. (b)

      Average drawdown:
      Let the cumulative wealth process be Wt=∏s=1t(1+rp,s)W\_{t}=\prod\_{s=1}^{t}(1+r\_{p,s}).
      The drawdown at time tt is defined as

      |  |  |  |
      | --- | --- | --- |
      |  | D​Dt=Wt−max1≤s≤t⁡Wsmax1≤s≤t⁡Ws≤0.DD\_{t}=\frac{W\_{t}-\max\_{1\leq s\leq t}W\_{s}}{\max\_{1\leq s\leq t}W\_{s}}\leq 0. |  |

      The average drawdown is then

      |  |  |  |
      | --- | --- | --- |
      |  | D​D¯=1H​∑t=1H|D​Dt|,\overline{DD}=\frac{1}{H}\sum\_{t=1}^{H}|DD\_{t}|, |  |

      which reflects the mean proportional loss from peak levels over the evaluation horizon.
4. 4.

   Risk-adjusted performance:
   Absolute returns alone can be misleading without accounting for risk exposure.
   To obtain a fairer comparison, we evaluate performance ratios that relate excess return to different notions of risk. All ratios are interpreted meaningfully only when the portfolio achieves a positive excess return.

   1. (a)

      Sharpe ratio:
      Relates average excess return to standard deviation,

      |  |  |  |
      | --- | --- | --- |
      |  | Sharpe Ratio=r¯p−rfσp,r¯p−rf>0,\text{Sharpe Ratio}=\frac{\bar{r}\_{p}-r\_{f}}{\sigma\_{p}},\quad\bar{r}\_{p}-r\_{f}>0, |  |

      where σp\sigma\_{p} is the portfolio standard deviation. Higher values indicate better risk-adjusted returns overall.
   2. (b)

      Sortino ratio:
      Focuses on downside risk by replacing total volatility with downside deviation,

      |  |  |  |
      | --- | --- | --- |
      |  | Sortino Ratio=r¯p−rfσd,r¯p−rf>0,\text{Sortino Ratio}=\frac{\bar{r}\_{p}-r\_{f}}{\sigma\_{d}},\quad\bar{r}\_{p}-r\_{f}>0, |  |

      where σd\sigma\_{d} is the standard deviation of negative returns. Larger values emphasize protection against losses.
   3. (c)

      Treynor ratio:
      Measures excess return per unit of systematic risk,

      |  |  |  |
      | --- | --- | --- |
      |  | Treynor Ratio=r¯p−rfβp,r¯p−rf>0,\text{Treynor Ratio}=\frac{\bar{r}\_{p}-r\_{f}}{\beta\_{p}},\quad\bar{r}\_{p}-r\_{f}>0, |  |

      where βp\beta\_{p} is the portfolio beta with respect to the benchmark. It highlights performance relative to market exposure.
   4. (d)

      Information ratio:
      Evaluates active return relative to tracking error,

      |  |  |  |
      | --- | --- | --- |
      |  | Information Ratio=r¯p−r¯bTE,r¯p−r¯b>0,\text{Information Ratio}=\frac{\bar{r}\_{p}-\bar{r}\_{b}}{\text{TE}},\quad\bar{r}\_{p}-\bar{r}\_{b}>0, |  |

      where r¯b\bar{r}\_{b} is the average benchmark return. Higher values imply more efficient benchmark outperformance.
5. 5.

   Turnover and time complexity: To evaluate cost efficiency and sparsity of the constructed portfolios, we consider three measures, two based on the portfolio weights and one based on the time taken.

   1. (a)

      Turnover ratio:
      Captures the average trading activity across rebalancing windows.
      Higher turnover implies greater transaction costs. It is defined as

      |  |  |  |
      | --- | --- | --- |
      |  | TR=1N−1​∑k=1N−1∑i=1n|wi,k+1−wi,k|,\text{TR}=\frac{1}{N-1}\sum\_{k=1}^{N-1}\sum\_{i=1}^{n}\big|w\_{i,k+1}-w\_{i,k}\big|, |  |

      where wi,kw\_{i,k} is the weight of asset ii in the kk-th window and NN is the total number of rolling windows.
   2. (b)

      No. of Assets:
      The average number of assets with non-zero weights in the tracking portfolio. This reflects portfolio sparsity, with smaller values indicating more concentrated portfolios.
   3. (c)

      Solver time: The total CPU time taken by the solver to obtain optimal or near-optimal solutions across all rolling windows. This metric reflects the computational tractability and scalability of each modeling framework, thus providing a practical perspective on the trade-off between model complexity and real-world applicability.

### 4.3 Statistical test

To assess whether differences in tracking error across models are statistically significant,
we perform pairwise one-sided paired tt-tests.
For each model pair (i,j)(i,j), let TEi,k\text{TE}\_{i,k} and TEj,k\text{TE}\_{j,k} denote the out-of-sample tracking errors in window kk, for k=1,…,Nk=1,\ldots,N.
The null and alternative hypotheses are specified as

|  |  |  |
| --- | --- | --- |
|  | H0:TE¯i=TE¯jvs.HA:TE¯i<TE¯j,H\_{0}:\bar{\text{TE}}\_{i}=\bar{\text{TE}}\_{j}\quad\text{vs.}\quad H\_{A}:\bar{\text{TE}}\_{i}<\bar{\text{TE}}\_{j}, |  |

where TE¯i=1N​∑k=1NTEi,k\bar{\text{TE}}\_{i}=\tfrac{1}{N}\sum\_{k=1}^{N}\text{TE}\_{i,k} is the mean tracking error of model ii.

The paired setting accounts for temporal dependence, since both models are evaluated on the same rolling windows.
The resulting pp-values are summarized in a matrix, which highlights statistically significant dominance relationships among competing models.

### 4.4 S&P 500 Index Features

We characterize the S&P 500 index and its constituents over the study period
(12 October 2012 to 8 November 2022) using three descriptive statistics: mean returns, standard deviation (volatities), and correlations with the index.

1. 1.

   Distribution of daily mean returns: Figure [6](https://arxiv.org/html/2601.03927v1#S4.F6 "Figure 6 ‣ item 1 ‣ 4.4 S&P 500 Index Features ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") reports the cross-sectional distribution of mean daily returns across all constituents. Most assets cluster around modest positive levels, with the distribution right-skewed due to a small number of high-return outliers. The vertical dashed lines indicate the cross-sectional mean (red) and cross-sectional median (blue) of constituent mean returns. The fact that the median lies below the mean reflects the influence of a few extreme outliers in pulling the average upward, suggesting that relatively few stocks drive the right tail of the return distribution while the majority deliver more modest performance.

   ![Refer to caption](SP500_MeanReturns.png)


   Figure 6: Distribution of mean daily returns for the S&P 500 constituents over the sample period 2012-12-10 to 2022-08-11. The red dashed line denotes the cross-sectional mean of constituent mean returns, while the blue dashed line denotes the cross-sectional median.
2. 2.

   Distribution of daily volatility: Figure [7](https://arxiv.org/html/2601.03927v1#S4.F7 "Figure 7 ‣ item 2 ‣ 4.4 S&P 500 Index Features ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") shows the distribution of standard deviation of daily returns, serving as a measure of asset volatility. Most assets exhibit volatility between 0.2 and 0.5, while the distribution is right-skewed with a small number of highly volatile stocks exhibiting standard deviations greater than 1. The vertical dashed lines denote the cross-sectional mean (red) and median (blue) volatilities across constituents. The fact that the mean lies to the right of the median highlights the impact of a few extreme outliers in inflating the average, while the median better represents the typical stock’s volatility level.

   ![Refer to caption](SP500_SD.png)


   Figure 7: Distribution of daily return volatilities (standard deviations) for the S&P 500 constituents over the sample period 2012-12-10 to 2022-08-11. The red dashed line denotes the cross-sectional mean volatility across constituents, while the blue dashed line denotes the cross-sectional median volatility
3. 3.

   Distribution of asset correlations: Figure [8](https://arxiv.org/html/2601.03927v1#S4.F8 "Figure 8 ‣ item 3 ‣ 4.4 S&P 500 Index Features ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") displays the distribution of correlations between each asset’s returns and the S&P 500 index return. Most constituents exhibit relatively high correlations in the range of 0.6 to 0.9, indicating strong co-movement with the market benchmark. The distribution is moderately left-skewed, with a non-trivial number of assets displaying weak or even negative correlations. The vertical dashed lines denote the cross-sectional mean (red) and median (blue) correlations across assets. The median lying slightly below the mean highlights the influence of a subset of highly correlated assets in pulling the average upward.

   ![Refer to caption](SP500_Corr.png)


   Figure 8: Distribution of daily asset correlations with the S&P 500 index over the 10-year period from 10-12-2012 to 11-08-2022. The red dashed line denotes the mean correlation, and the blue dashed line denotes the median correlation across assets.

### 4.5 Out-of-sample analysis

We now turn to the comparative evaluation of index-tracking models.
The analysis focuses on out-of-sample performance, assessed over the rolling windows described earlier.
For clarity, Table [6](https://arxiv.org/html/2601.03927v1#S4.T6 "Table 6 ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") provides a complete listing of the models considered, grouped into three broad paradigms: optimization-based, statistical, and data-driven approaches and Table [7](https://arxiv.org/html/2601.03927v1#S4.T7 "Table 7 ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") provides the model specifications, listing the parameter values and other specifications considered for the empirical study.

Table 6: Index-tracking models evaluated in the study, grouped into three categories: optimization-based, statistical, and data-driven.
This taxonomy provides the framework for the comparative out-of-sample analysis.

| Optimization models | Statistical models | Data-driven models |
| --- | --- | --- |
| 1. Mean Squared Error (MSE) | 1. Least Squares Regression (LSR) | 1. Clustering model 1 (Clust 1) |
| 2. Sum of Errors Squared (SES) | 2. Quantile Regression (QR) | 2. Clustering model 2 (Clust 2) |
| 3. Mean Absolute Deviation (MAD) | 3. Regression + Non-Negative LASSO (NNL) | 3. Sparse ϵ\epsilon-SVR model (ϵ\epsilon-SVR) |
| 4. Mean Absolute Downside Deviation (MADD) | 4. Regression + Elastic Net (NNEN) | 4. Sparse ν\nu-SVR model (ν\nu-SVR) |
| 5. MinMax | 5. Co-integration + Simulation (Coint-Sim) | 5. RF clustering + ridge (RF-Clust) |
| 6. Downside MinMax (DMinMax) | 6. Convex Co-integration (Cvx-CoInt) | 6. RF regression + ridge (RF-Reg) |
| 7. Tracking Error Variance (TEV) | 7. Factor-Based Model (FBM) | 7. Deep Autoencoders (six variants: SH-AE, Con-AE, DEN-AE, SP-AE, STCK-AE, VAR-AE) |
| 8. Tailed Mixed CVaR (TMCVaR) |  | 8. Deep Neural Network (DNN) |
|  |  | 9. DNN with Fixed Noise (DNNF) |




Table 7: Index-tracking models evaluated in the study with their specifications

| Model Name | Model Specifications |
| --- | --- |
| MSE | Cardinality constraint (no. of assets), K=45K=45 |
| SES | Cardinality constraint (no. of assets), K=45K=45 |
| MAD | Cardinality constraint (no. of assets), K=45K=45 |
| MADD | Cardinality constraint (no. of assets), K=45K=45 |
| MinMax | Cardinality constraint (no. of assets), K=45K=45 |
| DMinMax | Cardinality constraint (no. of assets), K=45K=45 |
| TEV | K=45K=45, benchmark index weights are chosen using least squares regression and then normalized |
| TMCVaR | K=45K=45, α=(0.9,0.75,0.5,0.1,0.01)\alpha=(0.9,0.75,0.5,0.1,0.01), δ=0.5\delta=0.5 |
| LSR | K=45K=45 |
| QR | K=45K=45, τ=0.5\tau=0.5 |
| NNL | Cardinality K=45K=45, regularization parameter λ\lambda obtained using bisection method, starting with 0 and 100100 |
| NNEN | Cardinality K=45K=45, |
| FBM | Number of factors, k=5k=5, Cardinality, K=45K=45 assets |
| Coint-Sim | K=45K=45, number of iterations=10000=10000, significance level for ADF test =0.05=0.05, maximum lag in ADF test=1=1, autolag criterion in ADF test=’AIC’ |
| Cvx-CoInt | Cardinality, K=45K=45; convex MIQP solved using Gurobi |
| Clust 1 | Number of clusters, K=45K=45 |
| Clust 2 | Number of clusters, K=45K=45 |
| ϵ\epsilon-SVR | K=45,C1={0.1,1,10,50},ϵ={0.001,0.005,0.01,0.05}K=45,C\_{1}=\{0.1,1,10,50\},\epsilon=\{0.001,0.005,0.01,0.05\} |
| ν\nu-SVR | K=45,C1={0.1,1,10,50},ϵ={0.001,0.005,0.01,0.05},C2=1K=45,C\_{1}=\{0.1,1,10,50\},\epsilon=\{0.001,0.005,0.01,0.05\},C\_{2}=1 |
| RF-Clust | number of trees=100, cardinality K=45K=45, α=[10−4,10−2]\alpha=[10^{-4},10^{-2}], cross-validation folds=5 |
| RF-Reg | number of trees=100, cardinality K=45K=45, α=[10−4,10−2]\alpha=[10^{-4},10^{-2}], cross-validation folds=5 |
| SH-AE | Hidden layer: 16 neurons (ReLU), optimizer: Adam, loss: MSE, epochs: 50, batch size: 32, K=45K=45 |
| SP-AE | Hidden layer: 16 neurons (ReLU), sparsity penalty λ=10−4\lambda=10^{-4} (L1), epochs: 50, batch size: 32, K=45K=45 |
| CON-AE | Hidden layer: 16 neurons (ReLU), contractive penalty λ=10−4\lambda=10^{-4}, epochs: 50, batch size: 32, K=45K=45 |
| STCK-AE | Encoder: [64, 32, 16], decoder: [32, 64], activation: ReLU, epochs: 50, batch size: 32, K=45K=45 |
| DEN-AE | Hidden layer: 16 neurons (ReLU), Gaussian noise (0.1), epochs: 50, batch size: 32, K=45K=45 |
| VAR-AE | Latent dimension: 16, KL regularization λK​L=10−4\lambda\_{KL}=10^{-4}, epochs: 50, batch size: 32, K=45K=45 |
| DNN | Asset selection via stacked autoencoder (encoder: 64,32,16; decoder: 32,64; activation: ReLU); optimizer: Adam; loss: MSE; epochs: 100; batch size: 32; |
|  | Deep NN (layers: 64,32,1; activation: ReLU); optimizer: Adam (lr = 0.01); loss: MSE; epochs: 100; batch size: 16 |
| DNNF | K=45K=45, hidden layers=6, neurons per layer=64, activation=ReLU, dropout=0.5, optimizer=Adam (lr=0.01), epochs=100, batch size=16, output=Softmax normalization |

Note that for fair comparison, each machine learning model was trained under its own empirically optimal configuration, ensuring convergence of training loss. The number of epochs and batch sizes were not forced to be identical across models, as the learning objectives and convergence characteristics differ by architecture. However, all models were evaluated on identical rolling windows, same cardinality constraint and benchmarked using consistent evaluation metrics, as described in Section [4.2](https://arxiv.org/html/2601.03927v1#S4.SS2 "4.2 Performance Metrics ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"). Across all optimization models, the values of ϵi​0\epsilon\_{i}0 and δi\delta\_{i} is set to 0 and 1, respectively for all assets ii.

#### 4.5.1 Performance evaluation of optimization-based models

Table [8](https://arxiv.org/html/2601.03927v1#S4.T8 "Table 8 ‣ 4.5.1 Performance evaluation of optimization-based models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") reports the out-of-sample performance of the eight optimization-based index-tracking portfolios.
For clarity, the discussion below highlights key results grouped by performance criteria mentioned previously.

Table 8: Out-of-sample performance of optimization-based index-tracking portfolios.
Panel I reports performance measures for the models; Panel II reports pairwise pp-values from one-sided paired tt-tests on tracking error.
Best values are shown in bold and worst in italics.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Panel I: Out-of-sample performance | | | | | | | | |  |
| Models | MSE | SES | MAD | MADD | MinMax | DMinMax | TEV | TMCVaR | S&P 500 |
| Tracking performance | | | | | | | | | |
| Tracking error | 0.00146 | 0.01490 | 0.00146 | 0.00150 | 0.00145 | 0.00148 | 0.00142 | 0.00159 | 0.00000 |
| Correlation | 99.19% | 69.21% | 99.19% | 99.18% | 99.20% | 99.18% | 99.25% | 99.09% | 100% |
| Return performance | | | | | | | | | |
| Average return | 0.00050 | 0.00124 | 0.00045 | 0.00047 | 0.00048 | 0.00046 | 0.00044 | 0.00044 | 0.00042 |
| Minimum return | -0.11905 | -0.17794 | -0.12037 | -0.12355 | -0.12187 | -0.11693 | -0.12619 | -0.12235 | -0.11984 |
| Maximum return | 0.10101 | 0.18139 | 0.09855 | 0.10533 | 0.09841 | 0.09811 | 0.10090 | 0.10920 | 0.09383 |
| Risk performance | | | | | | | | | |
| Standard deviation | 0.01147 | 0.02032 | 0.01143 | 0.01168 | 0.01154 | 0.01154 | 0.01162 | 0.01172 | 0.01142 |
| Average drawdown | 0.03496 | 0.08524 | 0.03618 | 0.03586 | 0.03584 | 0.03562 | 0.03675 | 0.03735 | 0.03835 |
| Risk-adjusted performance | | | | | | | | | |
| Sharpe ratio | 0.04316 | 0.06084 | 0.03944 | 0.04054 | 0.04175 | 0.04004 | 0.03816 | 0.03791 | 0.03650 |
| Sortino ratio | 0.05872 | 0.08670 | 0.05349 | 0.05525 | 0.05689 | 0.05435 | 0.05179 | 0.05191 | 0.04931 |
| Treynor ratio | 0.00050 | 0.00100 | 0.00045 | 0.00047 | 0.00048 | 0.00046 | 0.00044 | 0.00044 | 0.00042 |
| Information ratio | 0.05365 | 0.05499 | 0.02348 | 0.03779 | 0.04484 | 0.03064 | 0.01875 | 0.01742 | – |
| Turnover and Time complexity | | | | | | | | | |
| Turnover (TR) | 1.15647 | 1.91312 | 1.18348 | 1.13976 | 1.21212 | 1.23969 | 1.18920 | 1.31755 | – |
| No. of assets | 45 | 2 | 45 | 45 | 45 | 45 | 45 | 45 | – |
| Solver time | 17.52h | 1.81s | 17.58h | 17.52h | 17.76h | 18.04h | 18.01h | 18.22h | – |
| Panel II: Pairwise pp-values of tracking error tt-tests | | | | | | | | |  |
| pp-values | MSE | SES | MAD | MADD | MinMax | DMinMax | TEV | TMCVaR |  |
| MSE | \*\*\*\*\*\* | 1.00000 | 0.55610 | 0.95268 | 0.68441 | 0.67954 | 0.06967 | 0.89609 |  |
| SES | 1.4E-16 | \*\*\*\*\*\* | 2.3E-16 | 1.8E-16 | 1.6E-16 | 1.4E-16 | 1.3E-16 | 1.4E-16 |  |
| MAD | 0.44390 | 1.00000 | \*\*\*\*\*\* | 0.92645 | 0.62114 | 0.64187 | 0.06082 | 0.89603 |  |
| MADD | 0.04732 | 1.00000 | 0.07355 | \*\*\*\*\*\* | 0.09033 | 0.12427 | 0.00278 | 0.61012 |  |
| MinMax | 0.31559 | 1.00000 | 0.37886 | 0.90967 | \*\*\*\*\*\* | 0.55783 | 0.06581 | 0.85050 |  |
| DMinMax | 0.32046 | 1.00000 | 0.35813 | 0.87573 | 0.44217 | \*\*\*\*\*\* | 0.06129 | 0.83036 |  |
| TEV | 0.93033 | 1.00000 | 0.93918 | 0.99722 | 0.93419 | 0.93871 | \*\*\*\*\*\* | 0.98849 |  |
| TMCVaR | 0.10391 | 1.00000 | 0.10397 | 0.38988 | 0.14950 | 0.16964 | 0.01151 | \*\*\*\*\*\* |  |

1. 1.

   Tracking performance:

   * •

     With the exception of SES, all models achieve tight tracking errors in the range 0.0014–0.0016. The TEV model records the lowest TE (0.00142), followed by MinMax (0.00145). In contrast, SES performs poorly, with a TE of 0.01490.
   * •

     Consistent with the TE results, most models exhibit very high correlations (above 99%) with the S&P 500 index.
     TEV again performs best (99.25%), closely followed by MinMax.
     SES is the clear outlier, with correlation dropping to 69.21%.
2. 2.

   Return performance:

   * •

     Owing to its very small portfolio size, the SES model achieves the highest average return (0.00124) and maximum return (0.18139) among all optimization models. However, it also records the lowest minimum return (−0.17794-0.17794), corresponding to the largest maximum loss. This combination reflects a highly volatile and unstable return profile compared to its peers.
   * •

     For the remaining models, average returns are tightly clustered around the index mean return of 0.00042, with values between 0.00044 and 0.00050. The MSE portfolio records the highest mean return (0.00050), followed by MinMax (0.00048). Similarly, maximum returns range narrowly from 0.098 to 0.109, and minimum returns from −0.116-0.116 to −0.126-0.126, closely matching the benchmark values (0.0938 and −0.1198-0.1198). This demonstrates that, aside from SES, the optimization-based portfolios reproduce the benchmark’s return profile with only small deviations.
   * •

     Notably, the TEV portfolio, which achieved the lowest tracking error and highest correlation, also produces an average return (0.00044) that is very close to the index mean, reinforcing its consistency across both tracking and return dimensions.
3. 3.

   Risk performance:

   * •

     The SES model again stands out as an outlier, producing the largest volatility (0.02032), almost double that of the index and the other optimization portfolios (0.0114–0.0117). It also suffers the largest drawdown (0.08524). These results are linked to its extremely sparse asset selection (two assets despite the cardinality constraint), which limits diversification and increases instability.
   * •

     In contrast, all other portfolios exhibit volatilities comparable to the index value of 0.01142. The MSE portfolio has the lowest volatility (0.01147), while MADD records the highest (0.01168). Average drawdowns are also consistently smaller than the index benchmark of 0.03835, ranging from 0.03496 (MSE) to 0.03735 (TMCVaR). This illustrates the benefit of optimization-based selection, which produces diversified portfolios with lower downside risk than holding the full index.
4. 4.

   Risk-adjusted performance:

   * •

     The SES portfolio attains the highest values across all risk-adjusted ratios (Sharpe 0.06080.0608, Sortino 0.08670.0867, Treynor 0.00100.0010, Information 0.05500.0550), largely because of its unusually high mean return. Nevertheless, SES is not a desirable tracker: its extreme concentration (two holdings) results in materially higher risk, both volatility (0.02030.0203) and drawdown (0.08520.0852), reflecting poor diversification.
   * •

     Among the remaining, more stable trackers, MSE delivers the strongest set of ratios overall (Sharpe 0.04320.0432, Sortino 0.05870.0587, Treynor 0.000500.00050, Information 0.05370.0537), followed by MinMax; TMCVaR tends to be the weakest (e.g., Information 0.01740.0174). Excluding SES, all optimization portfolios exceed the index on Sharpe, Sortino, and Treynor (ranges 0.03790.0379–0.04320.0432, 0.05180.0518–0.05870.0587, and 0.000440.00044–0.000500.00050 versus 0.03650.0365, 0.04930.0493, and 0.000420.00042, respectively), supporting the effectiveness of optimization-based selection out of sample. Within this group, TEV and TMCVaR track the index’s ratios most closely.
5. 5.

   Turnover and asset count:
   All optimization-based portfolios satisfy the cardinality constraint of 45 assets, except SES, which selects only two assets.
   This extreme concentration explains SES’s unstable performance despite favorable risk-adjusted ratios. SES also exhibits the highest turnover (1.913), indicating frequent rebalancing, whereas the other models maintain turnover in a narrower range of approximately 1.14–1.32.
6. 6.

   Computational efficiency: We evaluate the computational efficiency of the optimization-based models in terms of their total runtime over 32 rolling windows. All optimization models were coded in R and solved using the Gurobi Optimizer through its R library interface, with a uniform time limit of 1800 seconds per rolling window. With the exception of the SES model, all optimization models consistently reached this time limit in each window, yielding an average runtime of approximately 1800 seconds per window. This amounts to a cumulative computational effort of about 16 hours across 32 windows. In practice, the observed wall-clock time was slightly higher (17–18 hours) due to solver overhead and system resource allocation. As a result, these models are computationally expensive333For the cardinality-constrained TMCVaR model, each rolling window was solved with the 1800-second time limit. While most windows produced feasible portfolios with the desired cardinality of 45 assets, three windows (8, 10, and 28) yielded degenerate solutions with significantly fewer assets. When these windows were re-run independently, full-cardinality solutions were obtained, suggesting that the batch run terminated prematurely due to time-limited convergence. This highlights both the sensitivity of mixed-integer portfolio models to solver resource constraints and the numerical conditioning of certain windows. under the current resource setting . It is worth noting that, since all underlying formulations are convex programs, the solutions reported are globally optimal when convergence occurs. With access to more sophisticated computing infrastructure, the runtime burden could be substantially reduced.
7. 7.

   Statistical significance (Panel II):
   Panel II reports the pp-values from the pairwise one-sided tt-tests described in Section [4.3](https://arxiv.org/html/2601.03927v1#S4.SS3 "4.3 Statistical test ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"), evaluating whether one portfolio achieves a lower tracking error than another. A model with many significant entries in its column is interpreted as dominating other portfolios in terms of tracking accuracy. The TEV column contains multiple significant entries: its tracking error is lower than SES, MADD, and TMCVaR at the 5% level, and lower than MSE, MAD, MinMax, and DMinMax at the 10% level.
   At the same time, the TEV row shows no significant rejections, confirming that no competing model outperforms it. Together, these results indicate that TEV achieves the most robust tracking accuracy among the optimization-based formulations at conventional significance levels.

As a synthesis of the findings, clear distinctions emerge among the eight optimization-based portfolios.
The SES model is the weakest tracker: with only two holdings, it achieves limited diversification and records a correlation of just 69.21% with the index. Its exceptionally high mean return is offset by elevated volatility and drawdown, making it unstable and unreliable.

Among the remaining portfolios, MSE delivers the strongest overall performance on mean return and risk-adjusted ratios, followed closely by MinMax. However, their statistical advantage in tracking error is limited, being significantly better only relative to SES and MADD.

By contrast, TEV consistently dominates. It achieves the lowest tracking error, the highest correlation (99.25%), and statistically outperforms all peers in terms of tracking accuracy. At the same time, its return and risk profile closely match that of the index, making TEV the most effective and reliable optimization-based index-tracking model in this comparison.

![Refer to caption](Box_Corr_OPT.png)


Figure 9: Boxplots of correlations between the S&P 500 index and optimization-based tracking portfolios across 32 rolling out-of-sample windows.

![Refer to caption](Box_TE_OPT.png)


Figure 10: Boxplots of tracking errors for optimization-based index-tracking portfolios across 32 rolling out-of-sample windows.

Figure [9](https://arxiv.org/html/2601.03927v1#S4.F9 "Figure 9 ‣ 4.5.1 Performance evaluation of optimization-based models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the distribution of correlations with the index for the optimization-based models across rolling windows.
SES is excluded because its correlations are dispersed over a much wider range, which would distort the visualization. For the remaining models, correlations are tightly clustered around 0.99, indicating consistently strong tracking accuracy. Among them, TMCVaR attains the highest median correlation, while TEV exhibits the narrowest interquartile range, reflecting greater stability across windows. The correlation ranges of TEV and TMCVaR overlap; TEV is more stable, whereas TMCVaR has a slightly higher median value. By comparison, models such as DMinMax, MAD, and MSE show slightly wider spreads and lower minima, pointing to weaker performance in certain windows. Overall, while all models (excluding SES) deliver robust results, TEV stands out as the most reliable tracker, with TMCVaR in second place.

Figure [10](https://arxiv.org/html/2601.03927v1#S4.F10 "Figure 10 ‣ 4.5.1 Performance evaluation of optimization-based models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the distribution of tracking errors for the optimization-based models across rolling windows, with SES excluded due to its extremely large error range. All remaining portfolios achieve very low errors, generally clustered between 0.001 and 0.0015, underscoring their effectiveness in replicating the benchmark index. Among them, TEV and MinMax record the lowest median errors with relatively narrow spreads, indicating strong and consistent performance.
TEV stands out further, as its full range lies below that of MinMax, making it the most accurate tracker in terms of error minimization. By contrast, MSE and TMCVaR exhibit greater variability and occasional high outliers, suggesting less stable performance across windows. MAD, MADD, and DMinMax occupy the middle ground, with tracking errors that are stable but not among the best. Overall, excluding SES, all optimization models demonstrate credible tracking accuracy, with TEV emerging as the most reliable, followed by MinMax, while MSE and TMCVaR are comparatively more dispersed.

Having examined the optimization-based formulations, we next evaluate the statistical-based models.

#### 4.5.2 Performance evaluation of Statistical based index tracking optimization models

Table 9: Out-of-sample performance of statistical-based index-tracking portfolios.
Panel I reports performance measures, while Panel II shows pairwise pp-values from one-sided paired tt-tests on tracking error.
Within each block, the best values among Lasso- and Elastic-Net–type penalties are in bold, and the overall best values are in italics.

| Panel I: Out-of-sample performance | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Models | LSR | QR | NNL | NNEN | Factor | CoInt-Sim | Cvx-CoInt | Index |
| Tracking performance | | | | | | | | |
| Tracking error | 0.01322 | 0.01307 | 0.00303 | 0.00206 | 0.00312 | 0.00246 | 0.00148 | 0.00000 |
| Correlation | 63.00% | 64.70% | 97.77% | 98.73% | 96.75% | 98.01% | 99.17% | 100% |
| Return performance | | | | | | | | |
| Average return | 0.00069 | 0.00105 | 0.00055 | 0.00050 | 0.00053 | 0.00047 | 0.00049 | 0.00042 |
| Minimum return | -0.13449 | -0.09626 | -0.12917 | -0.12493 | -0.11511 | -0.12531 | -0.11753 | -0.11984 |
| Maximum return | 0.18836 | 0.16664 | 0.12265 | 0.11057 | 0.10422 | 0.11434 | 0.09713 | 0.09383 |
| Risk performance | | | | | | | | |
| Volatility | 0.01700 | 0.01713 | 0.01301 | 0.01225 | 0.01223 | 0.01214 | 0.01148 | 0.01142 |
| Avg drawdown | 0.21365 | 0.08094 | 0.04244 | 0.03771 | 0.04687 | 0.04270 | 0.03626 | 0.03835 |
| Risk-adjusted performance | | | | | | | | |
| Sharpe ratio | 0.04077 | 0.06146 | 0.04217 | 0.04056 | 0.04297 | 0.03836 | 0.04226 | 0.03650 |
| Sortino ratio | 0.05964 | 0.08938 | 0.05775 | 0.05556 | 0.05808 | 0.05205 | 0.05740 | 0.04931 |
| Treynor ratio | 0.00074 | 0.00108 | 0.00049 | 0.00047 | 0.00051 | 0.00045 | 0.00049 | 0.00042 |
| Information ratio | 0.02091 | 0.04869 | 0.04357 | 0.03889 | 0.03493 | 0.01998 | 0.04629 | – |
| Turnover and complexity | | | | | | | | |
| Turnover (TR) | 1.49575 | 1.17703 | 0.56941 | 0.58561 | 1.04997 | 2.02480 | 1.12265 | – |
| No. of assets | 3 | 3 | 32 | 38 | 38 | 43 | 45 | – |
| Solver time | 3.98s | 6.02s | 1.90s | 7.46s | 7.62s | 19.49m | 18.10h | – |
| Panel II: Pairwise pp-values of tracking error tt-tests | | | | | | | |  |
| pp-values | LSR | QR | NNL | NNEN | Factor | CoInt-Sim | Cvx-CoInt |  |
| LSR | \*\*\*\*\*\* | 0.64100 | 1.4E-12 | 6.3E-13 | 2.4E-12 | 3.5E-13 | 1.2E-13 |  |
| QR | 0.35900 | \*\*\*\*\*\* | 4.8E-16 | 2.0E-16 | 4.4E-16 | 8.5E-17 | 6.0E-17 |  |
| NNL | 1.00000 | 1.00000 | \*\*\*\*\*\* | 4.5E-07 | 0.81668 | 5.6E-09 | 1.6E-10 |  |
| NNEN | 1.00000 | 1.00000 | 1.00000 | \*\*\*\*\*\* | 1.00000 | 0.99830 | 2.4E-10 |  |
| Factor | 1.00000 | 1.00000 | 0.18332 | 3.4E-10 | \*\*\*\*\*\* | 1.3E-05 | 5.7E-14 |  |
| CoInt-Sim | 1.00000 | 1.00000 | 0.99994 | 0.00169 | 0.99998 | \*\*\*\*\*\* | 2.8E-10 |  |
| Cvx-CoInt | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | \*\*\*\*\*\* |  |

Table [9](https://arxiv.org/html/2601.03927v1#S4.T9 "Table 9 ‣ 4.5.2 Performance evaluation of Statistical based index tracking optimization models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") reports the out-of-sample performance of the seven statistical-based index-tracking models introduced in Table [6](https://arxiv.org/html/2601.03927v1#S4.T6 "Table 6 ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem"). Several clear patterns emerge from the results.

1. 1.

   Tracking performance:

   * •

     Tracking error: The convex co-integration model (Cvx\_CoInt) achieves the lowest tracking error (0.00148), followed by the NNEN model (0.00206). The cointegration with simulations also delivers a comparably low error (0.00246). In contrast, regression-based baselines such as LSR and QR record substantially higher errors, reflecting their limited diversification and weaker ability to replicate index movements.
   * •

     Correlation with the index: Unlike the optimization-based models, where correlations with the benchmark consistently exceed 99%, only Cvx\_CoInt approaches this level in the statistical group (99.17%). NNEN and CoInt\_Sim follow with correlations of 98.73% and 98.01%, respectively. By contrast, LSR and QR again perform poorly, with correlations of only 63–65%, underscoring their inability to capture index dynamics reliably. Intermediate performance is observed for NNL and the Factor model, which achieve correlations in the 96–98% range.
2. 2.

   Return performance:

   * •

     The regression-based models (LSR and QR) stand out with unusually high average returns, with QR recording the highest among all models (0.00105). However, this comes at the cost of poor diversification, as both models select only three assets across rolling windows. Consequently, they exhibit extreme outcomes, with LSR attaining the largest maximum return (0.18836) but also the deepest minimum return (−0.13449-0.13449).
   * •

     In contrast, the remaining five models yield average returns within a narrow range (≈0.00047\approx 0.00047–0.00055), moderately above the index average (0.00042). Among these, NNL produces the highest mean return, closely followed by the Factor model. NNL also achieves the strongest maximum return (0.12265) within this diversified group, though it simultaneously suffers the most severe loss, indicating greater volatility in its outcomes.
   * •

     Notably, Cvx\_CoInt, which already demonstrates the best tracking accuracy, also provides the closest alignment with the index in terms of return distribution. Its average return (0.00049) lies just above the benchmark’s (0.00042), and both its maximum and minimum returns remain tightly clustered around those of the index. This indicates that the Cvx\_CoInt portfolio not only minimizes tracking error but also replicates the benchmark’s return profile more faithfully than its peers.
3. 3.

   Risk performance:

   * •

     The regression-based models (LSR and QR), constrained by their limited diversification, exhibit the highest volatility and drawdowns. Their concentrated asset allocations expose them to large swings in portfolio value, underscoring their fragility as index trackers.
   * •

     Among the diversified portfolios, NNL emerges as the riskiest, reporting the highest standard deviation (0.01301) and the second-largest average drawdown (0.04244).
   * •

     By contrast, the co-integration–based approaches (Cvx\_CoInt and CoInt\_Sim) and the NNEN record the lowest and most stable risk values. In particular, Cvx\_CoInt not only outperforms its peers but also aligns most closely with the benchmark index, reinforcing its reliability in terms of stability.
4. 4.

   Risk-adjusted performance:

   * •

     Driven by its exceptionally high average return, QR attains the highest Sharpe, Sortino, and Treynor ratios. However, these elevated ratios are misleading, as they arise from extreme return realizations combined with poor diversification and high volatility. LSR, on the other hand, fails to deliver competitive ratios: its low mean return relative to elevated risk prevents it from achieving meaningful risk-adjusted gains.
   * •

     Within the well-diversified group, the Factor model and Cvx\_CoInt delivers the strongest performance across all risk-adjusted measures, closely followed by the NNL. Notably, all five diversified trackers surpass the benchmark in terms of Sharpe, Sortino, and Treynor ratios. This demonstrates the ability of statistical frameworks, when properly specified, to provide superior risk-adjusted performance compared to direct index replication.
5. 5.

   Turnover and asset count:
   Although the desired cardinality was set at 45 assets, the regression-based portfolios (LSR and QR) consistently select only 2–3 assets. This limited diversification inflates their turnover ratios, reflecting frequent and concentrated reallocations. By contrast, the remaining five models allocate between 32 and 45 assets, resulting in substantially lower transaction costs. Among these, NNL and NNEN deliver the most favorable turnover values. Notably, Cvx\_CoInt stands out within the co-integration family, as it both attains relatively low turnover and reliably selects the full 45 assets, thereby adhering most closely to the cardinality constraint.
6. 6.

   Computational efficiency:
   The regression-based models (LSR and QR) and the penalized regressions (NNL and NNEN) are extremely fast, producing solutions within only a few seconds across all rolling windows. By contrast, the co-integration-based models are considerably more computationally demanding. CoInt\_Sim requires on average about 20 minutes to solve across 32 windows, while Cvx\_CoInt frequently hits the maximum solver time limit of 30 minutes per window. This disparity highlights an important trade-off: while co-integration models provide superior tracking accuracy and stability, they do so at the expense of substantially higher computational costs.
7. 7.

   Statistical significance (Panel II):
   The pp-value matrix reveals that Cvx\_CoInt delivers statistically lower tracking errors than nearly all competing models, with highly significant rejections (p<0.05p<0.05 and often p<0.001p<0.001) against regression-based baselines (LSR, QR) and other statistical trackers (NNL, NNEN, Factor). Crucially, the row corresponding to Cvx\_CoInt contains no significant rejections, confirming that no alternative model consistently surpasses it. NNEN emerges as the second-strongest performer, showing significant improvements in TE relative to most trackers but not relative to Cvx\_CoInt. Finally, CoInt\_Sim demonstrates competitive performance, producing significantly lower errors than several peers but falling short of the NNEN and its convex counterpart.

![Refer to caption](Stat_Corr_Updated.png)


Figure 11: Box plot distribution of correlation with index for the statistical-based index tracking models

Overall, the analysis of the statistical-based index tracking models highlights clear contrasts in performance. The regression-based approaches (LSR and QR) fail to construct diversified portfolios, allocating to only a handful of assets and thereby achieving correlations of merely 63–65% with the benchmark. Among the five well-diversified models, the co-integration-based portfolios emerge as the most effective trackers, with Cvx\_CoInt consistently outperforming its peers. While the NNL model delivers the highest average return, this comes at the cost of elevated volatility and drawdowns, reducing its attractiveness as a practical strategy. In contrast, both Cvx\_CoInt and CoInt\_Sim generate lower risk values, with Cvx\_CoInt offering the closest alignment with the index across return and risk measures. The statistical significance tests further reinforce this dominance: Cvx\_CoInt produces significantly lower tracking errors than all competitors, with no model found to outperform it. Taken together, these findings establish Cvx\_CoInt as the strongest candidate for index-tracking funds within the statistical modeling paradigm. From an investment perspective, these results suggest that co-integration-based strategies, particularly Cvx\_CoInt, provide the most reliable replication of the index. While they demand greater computational resources, they deliver statistically validated tracking advantages that regression-based approaches cannot match.

Figure [11](https://arxiv.org/html/2601.03927v1#S4.F11 "Figure 11 ‣ 4.5.2 Performance evaluation of Statistical based index tracking optimization models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") shows the distribution of correlations with the index for the statistical-based models, excluding LSR and QR to avoid distortion from their substantially lower correlations. Among the remaining trackers, the co-integration models (CoInt\_Sim and Cvx\_CoInt) exhibit high correlations but with different stability. Cvx\_CoInt demonstrates the most robust behavior, with tightly clustered correlations around 0.99, and a narrow interquartile range compared to CoInt\_Sim. NNEN and NNL also achieve strong median correlations near 0.98, though they exhibit slightly wider variability and a few downward outliers. By contrast, the Factor model shows a broader distribution and a lower median correlation (around 0.96), underscoring its weaker and less stable tracking ability. Overall, co-integration-based models deliver the most reliable correlation performance in this category, with Cvx\_CoInt clearly setting the benchmark.

![Refer to caption](TE_Stat_Upd.png)


Figure 12: Box plot distribution of tracking error for the statistical-based index tracking models

Next, Figure [12](https://arxiv.org/html/2601.03927v1#S4.F12 "Figure 12 ‣ 4.5.2 Performance evaluation of Statistical based index tracking optimization models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the distribution of tracking errors for the statistical-based models, again excluding LSR and QR to avoid distortion from their much larger error ranges. Among the remaining approaches, Cvx\_CoInt achieves the lowest median tracking error and the narrowest interquartile spread, underscoring its reliability as the most effective statistical formulation. CoInt\_Sim also performs well, though with slightly higher variability, it still maintains consistently low error levels. In contrast, the Factor, NNEN, and NNL exhibit higher medians, wider dispersions, with more frequent outliers, indicating weaker accuracy and less stability relative to the co-integration models.

Taken together, the graphical evidence confirms that while CoInt\_Sim is a competitive tracker, Cvx\_CoInt clearly delivers the most accurate and consistent tracking performance among all statistical-based methods. The next subsection turns to the data-driven category, where machine learning algorithms provide alternative approaches to index tracking.

#### 4.5.3 Performance evaluation of Data-driven index tracking models

Table 10: Out-of-sample performance of data-driven index-tracking portfolios.
Panel I reports performance measures; Panel II shows pairwise pp-values from one-sided paired tt-tests on tracking error.
Best values are shown in bold and worst in italics.

| Panel I: Out-of-sample performance | | | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Models | SH-AE | Con-AE | DEN-AE | SP-AE | STCK-AE | VAR-AE | ϵ\epsilon-SVR | ν\nu-SVR | RF-Clust | RF-Reg | DeepNN | DeepNNF | Clust1 | Clust2 | Index |
| Tracking performance | | | | | | | | | | | | | | | |
| Tracking error | 0.00402 | 0.00403 | 0.00406 | 0.00415 | 0.00388 | 0.00380 | 0.00475 | 0.00405 | 0.00288 | 0.00271 | 0.00498 | 0.00153 | 0.00271 | 0.00262 | 0.00000 |
| Correlation (%) | 94.10 | 93.99 | 94.12 | 93.71 | 94.48 | 94.70 | 91.60 | 93.51 | 97.22 | 98.10 | 90.14 | 99.11 | 97.23 | 97.39 | 100.00 |
| Return performance | | | | | | | | | | | | | | | |
| Average return | 0.00053 | 0.00053 | 0.00049 | 0.00062 | 0.00057 | 0.00046 | 0.00046 | 0.00047 | 0.00056 | 0.00049 | 0.00040 | 0.00047 | 0.00042 | 0.00045 | 0.00042 |
| Minimum return | -0.13007 | -0.12409 | -0.13379 | -0.12429 | -0.12524 | -0.12589 | -0.11366 | -0.09710 | -0.13389 | -0.12335 | -0.12952 | -0.11643 | -0.11955 | -0.11149 | -0.11984 |
| Maximum return | 0.12554 | 0.12444 | 0.12906 | 0.12884 | 0.12376 | 0.11690 | 0.12005 | 0.09370 | 0.10342 | 0.12204 | 0.10793 | 0.10149 | 0.11475 | 0.09608 | 0.09383 |
| Risk performance | | | | | | | | | | | | | | | |
| Volatility | 0.01186 | 0.01175 | 0.01202 | 0.01187 | 0.01182 | 0.01182 | 0.01171 | 0.01057 | 0.01216 | 0.01277 | 0.01086 | 0.01144 | 0.01156 | 0.01152 | 0.01142 |
| Avg drawdown | 0.04079 | 0.03891 | 0.04438 | 0.03478 | 0.03780 | 0.04365 | 0.04230 | 0.03528 | 0.03885 | 0.04385 | 0.03782 | 0.03650 | 0.03859 | 0.03870 | 0.03835 |
| Risk-adjusted performance | | | | | | | | | | | | | | | |
| Sharpe ratio | 0.04443 | 0.04522 | 0.04113 | 0.05234 | 0.04846 | 0.03891 | 0.03960 | 0.04405 | 0.04586 | 0.03838 | 0.03725 | 0.04065 | 0.03635 | 0.03892 | 0.03650 |
| Sortino ratio | 0.06085 | 0.06192 | 0.05635 | 0.07198 | 0.06668 | 0.05325 | 0.05429 | 0.05919 | 0.06151 | 0.05257 | 0.05099 | 0.05537 | 0.04938 | 0.05308 | 0.04931 |
| Treynor ratio | 0.00054 | 0.00055 | 0.00050 | 0.00064 | 0.00059 | 0.00047 | 0.00049 | 0.00054 | 0.00054 | 0.00045 | 0.00047 | 0.00047 | 0.00043 | 0.00046 | 0.00042 |
| Information ratio | 0.02742 | 0.02843 | 0.01910 | 0.04925 | 0.04022 | 0.01141 | 0.00989 | 0.01215 | 0.04907 | 0.02702 | -0.00247 | 0.03167 | 0.00133 | 0.01214 | – |
| Turnover and complexity | | | | | | | | | | | | | | | |
| Turnover (TR) | 0.82699 | 0.85497 | 0.82795 | 0.81242 | 0.85659 | 0.87958 | 1.72386 | 1.68549 | 1.26397 | 1.11341 | 0.59538 | 0.59882 | 1.77349 | 1.85803 | – |
| No. of assets | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 42 | 40 | – |
| Solver time | 32.05s | 31.79s | 32.01s | 33.08s | 46.67s | 43.14s | 27.84s | 48.91s | 34.47s | 37.46s | 2.20m | 51.63m | 4.99s | 5.02s | – |
| Panel II: Pairwise pp-values of tracking error tt-tests | | | | | | | | | | | | | | | |
| pp-values | SH-AE | Con-AE | DEN-AE | SP-AE | STCK-AE | VAR-AE | ϵ\epsilon-SVR | ν\nu-SVR | RF-Clust | RF-Reg | DeepNN | DeepNNF | Clust1 | Clust2 |  |
| SH-AE | \*\*\*\*\*\* | 0.45387 | 0.34268 | 0.84042 | 0.06520 | 0.19645 | 0.94554 | 0.71912 | 2.52E-05 | 1.95E-07 | 0.99999 | 4.27E-11 | 3.90E-07 | 1.80E-06 |  |
| Con-AE | 0.54613 | \*\*\*\*\*\* | 0.37443 | 0.88885 | 0.10054 | 0.21707 | 0.92788 | 0.74956 | 1.29E-04 | 8.34E-07 | 0.99999 | 8.68E-11 | 8.73E-07 | 3.03E-06 |  |
| DEN-AE | 0.65732 | 0.62557 | \*\*\*\*\*\* | 0.93842 | 0.19752 | 0.30417 | 0.96628 | 0.77674 | 2.14E-04 | 3.05E-06 | 0.99999 | 8.03E-10 | 3.82E-06 | 2.37E-05 |  |
| SP-AE | 0.15958 | 0.11115 | 0.06158 | \*\*\*\*\*\* | 0.02025 | 0.06822 | 0.90975 | 0.55734 | 5.20E-05 | 1.09E-06 | 0.99997 | 1.64E-10 | 7.19E-07 | 3.33E-06 |  |
| STCK-AE | 0.93480 | 0.89946 | 0.80248 | 0.97975 | \*\*\*\*\*\* | 0.60735 | 0.98350 | 0.92454 | 3.38E-04 | 6.74E-07 | 1.00000 | 1.59E-10 | 2.81E-06 | 1.35E-05 |  |
| VAR-AE | 0.80355 | 0.78293 | 0.69583 | 0.93178 | 0.39265 | \*\*\*\*\*\* | 0.95216 | 0.89787 | 2.01E-05 | 6.30E-07 | 0.99999 | 1.70E-13 | 2.92E-08 | 1.29E-08 |  |
| Eps-SVR | 0.05446 | 0.07212 | 0.03372 | 0.09025 | 0.01650 | 0.04784 | \*\*\*\*\*\* | 0.15963 | 1.16E-04 | 1.22E-05 | 0.98727 | 6.56E-08 | 2.32E-05 | 1.06E-04 |  |
| Nu-SVR | 0.28088 | 0.25044 | 0.22326 | 0.44266 | 0.07546 | 0.10213 | 0.84037 | \*\*\*\*\*\* | 1.40E-06 | 2.58E-07 | 0.99991 | 7.58E-13 | 1.15E-09 | 4.42E-08 |  |
| RF-Clust | 0.99997 | 0.99987 | 0.99979 | 0.99995 | 0.99966 | 0.99998 | 0.99988 | 0.99999 | \*\*\*\*\*\* | 0.04684 | 1.00000 | 1.06E-12 | 0.05163 | 0.05130 |  |
| RF-Reg | 1.00000 | 1.00000 | 0.99999 | 0.99999 | 0.99999 | 0.99999 | 0.99999 | 1.00000 | 0.95316 | \*\*\*\*\*\* | 1.00000 | 1.78E-09 | 0.63888 | 0.53653 |  |
| DeepNN | 7.73E-06 | 5.61E-06 | 4.58E-06 | 3.19E-05 | 5.75E-07 | 3.38E-06 | 0.01273 | 8.53E-05 | 1.21E-09 | 5.94E-12 | \*\*\*\*\*\* | 7.30E-14 | 4.14E-12 | 4.21E-10 |  |
| DeepNNF | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 | \*\*\*\*\*\* | 1.00000 | 1.00000 |  |
| Clust1 | 1.00000 | 1.00000 | 0.99999 | 0.99999 | 0.99999 | 1.00000 | 0.99998 | 1.00000 | 0.94837 | 0.36112 | 1.00000 | 6.77E-12 | \*\*\*\*\*\* | 0.38878 |  |
| Clust2 | 1.00000 | 1.00000 | 0.99998 | 0.99999 | 0.99999 | 1.00000 | 0.99989 | 1.00000 | 0.94870 | 0.46347 | 1.00000 | 9.91E-15 | 0.61122 | \*\*\*\*\*\* |  |

Table [10](https://arxiv.org/html/2601.03927v1#S4.T10 "Table 10 ‣ 4.5.3 Performance evaluation of Data-driven index tracking models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") reports the out-of-sample performance of 14 data-driven index-tracking portfolios, spanning five methodological families: clustering (Clust 1, Clust 2), support-vector regression (ϵ\epsilon-SVR, ν\nu-SVR), random forests (RF-Clust, RF-Reg), deep autoencoders (SH-AE, Con-AE, DEN-AE, SP-AE, STCK-AE, VAR-AE), and deep learning (DNN, DNNF). In contrast to regression-based models in the previous section, all data-driven approaches produce well-diversified portfolios, typically allocating to 40–45 assets per window. The detailed tracking performance is summarized below.

1. 1.

   Tracking performance:
   Among these models, DNNF delivers the strongest results, achieving the lowest tracking error (0.00153) and the highest correlation with the index (99.11%), thereby standing out as the best data-driven tracker. RF-Reg ranks second, with a TE of 0.00271 and a correlation of 98.10%, showcasing the effectiveness of tree-based ensemble methods in capturing nonlinear relationships.

   By contrast, the baseline deep neural network (DNN) performs poorly relative to its enhanced counterpart, with the highest TE (0.00498) and the lowest correlation (90.14%). The SVR-based models also underperform, recording relatively high tracking errors (ϵ\epsilon-SVR: 0.00475; ν\nu-SVR: 0.00405) and weaker correlations (91.60% and 93.51%, respectively).

   Within the autoencoder family, VAR-AE emerges as the best variant, with the lowest TE (0.00380) and the highest correlation (94.70%), followed closely by STCK-AE (0.00388). The remaining autoencoder variants exhibit comparable performance, with correlations clustered in the 94–95% range, offering moderate improvements over SVR but falling short of RF-Reg and DNNF.
2. 2.

   Return performance:
   Similar to the optimization and statistical based portfolios, nearly all data-driven models (with the exception of DNN) generate higher average returns than the index. The strongest performer is SP-AE, which achieves the highest mean return of 0.00062, followed by STCK-AE at 0.00057.

   In terms of extreme outcomes, the SVR-based models deliver relatively mild downside risk, with ϵ\epsilon-SVR and ν\nu-SVR recording the least severe minimum returns (−0.1137-0.1137 and −0.0971-0.0971, respectively). By contrast, RF-Clust exhibits the deepest drawdown, with a minimum return of −0.1339-0.1339. On the upside, DEN-AE produces the highest maximum return (0.1291), closely followed by SP-AE (0.1288), reflecting the potential of autoencoder architectures to capture strong return episodes.

   Notably, DNNF—the best tracker in terms of TE and correlation closely mirrors the benchmark’s return profile, with an average return of 0.00047, a maximum of 0.1015, and a minimum of −0.1164-0.1164. Clust 2, one of the clustering-based methods, also aligns closely with the index across all return measures, making it a stable, though less distinctive performer in this category.
3. 3.

   Risk performance:
   Among the data-driven models, ν\nu-SVR achieves the lowest volatility, with a standard deviation of 0.01057, while SP-AE records the smallest average drawdown at 0.03478. The deep learning portfolios also perform well on risk measures: DNN and DNNF register standard deviations of 0.01086 and 0.01144, respectively, placing them second and third overall. Both models also rank among the portfolios with lower drawdowns, with DNNF in particular aligning closely with the benchmark’s volatility (index: 0.01142).

   By contrast, the random forest models are more volatile, with RF-Reg showing the highest standard deviation (0.01277), making it the riskiest portfolio in this group. The autoencoder-based trackers fall within a moderate range (0.01175–0.0120), with Con-AE at the lower end and DEN-AE at the upper end. Notably, DEN-AE not only exhibits the highest standard deviation among the autoencoders (0.01202) but also suffers the largest drawdowns, reflecting greater exposure to downside risk.
4. 4.

   Risk-adjusted performance:
   Across the board, all data-driven models outperform the index on risk-adjusted metrics (Sharpe, Sortino, Treynor, and Information ratios), underscoring their ability to generate superior returns relative to risk. SP-AE stands out as the top performer, achieving the highest values across all ratios (Sharpe =0.0523=0.0523, Sortino =0.0720=0.0720, Treynor =0.00064=0.00064, Information =0.0493=0.0493). Its strong performance reflects the combination of elevated mean returns with relatively moderate risk levels, making it the most attractive model in this category from an investment perspective.

   STCK-AE emerges as the closest competitor, consistently ranking second across the ratios. Indeed, most autoencoder-based models (except VAR-AE) maintain above-average ratio values, largely attributable to their higher mean returns.

   At the other end of the spectrum, Clust 1 records the weakest performance, with the lowest Sharpe, Sortino, and Treynor ratios. The baseline DNN also underperforms, as its average return falls below that of the index, rendering its Information ratio undefined. In contrast, DNNF provides more balanced outcomes: although its Sharpe (0.0407), Sortino (0.0554), and Treynor (0.00047) ratios are mid-ranked, it achieves the fourth-best Information ratio (0.0317), confirming its stable and well-diversified profile.
5. 5.

   Turnover and asset count:
   The autoencoder-based portfolios maintain relatively moderate turnover ratios (≈0.81​–​0.88\approx 0.81–0.88), reflecting stable allocation dynamics across windows. By contrast, the clustering-based models incur the highest turnover costs (Clust 1 ==1.77, Clust 2 == 1.86), and the SVR-based models also lie on the higher side (≈1.68​–​1.72\approx 1.68–1.72).

   The deep learning models (DNN and DNNF) stand out with the lowest turnover values (≈\approx 0.60), making them the most cost-efficient strategies among all 14 portfolios. Importantly, all models satisfy the cardinality constraint of 45 assets, except the clustering approaches, which allocate to slightly fewer stocks (42 for Clust 1, 40 for Clust 2). This limited diversification, combined with their elevated turnover, highlights the relative inefficiency of clustering-based trackers in a practical investment setting.
6. 6.

   Computational efficiency:
   Solver times vary substantially across the 14 data-driven approaches. Clustering models are the fastest (≈5\approx 5s per window), while most autoencoder, SVR, and random forest models solve within a practical range of 27–49s. By contrast, the deep learning models are considerably more demanding: DNN requires 2.2 minutes, and DNNF takes as long as 51.6 minutes across all 32 windows. These results highlight the computational trade-off in training deep architectures, which offer improved tracking precision but at significantly higher time costs relative to shallower machine learning or statistical learners.
7. 7.

   Statistical significance (Panel II):
   The pp-value matrix demonstrates that DNNF clearly dominates this category: its column contains overwhelmingly small values (p<10−10p<10^{-10}) against all competitors, confirming its significant superiority in terms of tracking error. Within the autoencoder family, SP-AE achieves statistically significant improvements over several peers (p<0.05p<0.05 in multiple comparisons), reinforcing its strong relative performance. In contrast, the baseline DNN fails to statistically outperform any model, consistent with its weak empirical results. RF-Reg delivers mixed outcomes, performing competitively against some autoencoders but falling short of DNNF, illustrating that while ensemble methods are robust, they cannot match the precision of deep learning with noise regularization.

![Refer to caption](Box_Corr_ML.png)


Figure 13: Box plot distribution of correlation with index for the data-driven index tracking models

Overall, DNNF emerges as the most effective data-driven index-tracking model, combining the lowest tracking error, the highest correlation, strong statistical significance, and the lowest turnover cost. SP-AE stands out within the autoencoder family, balancing close tracking accuracy with superior Sharpe and Sortino ratios, supported by statistical validation. ν\nu-SVR and RF-Reg appear as competitive alternatives, though both incur higher turnover costs. By contrast, the baseline DNN consistently underperforms across metrics, and is the only model to generate an average return lower than the index.

Figure [13](https://arxiv.org/html/2601.03927v1#S4.F13 "Figure 13 ‣ 4.5.3 Performance evaluation of Data-driven index tracking models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the distribution of correlations with the index across the 14 data-driven models. DNNF clearly dominates, with correlations clustering tightly above 0.98, reflecting exceptional reliability across all evaluation windows. The clustering-based approaches (Clust 1 and Clust 2) also perform strongly, maintaining stable correlations in the range of 0.93–0.97. Similarly, RF-Reg and RF-Clust achieve median correlations around 0.95, comparable to clustering methods.

The autoencoder variants (Con-AE, SH-AE, SP-AE, STCK-AE, VAR-AE, DEN-AE) and the SVR-based models (ϵ\epsilon-SVR and ν\nu-SVR) deliver moderately high correlations (0.90-0.95), but with wider dispersion and more variability than DNNF. In contrast, the baseline DNN exhibits the weakest performance, with highly unstable behavior and occasional outliers below 0.5. Taken together, these results highlight DNNF as the most robust and reliable data-driven tracker, followed by clustering- and random forest-based approaches, while simpler autoencoders and SVRs remain middle-tier options.

![Refer to caption](Box_TE_ML.png)


Figure 14: Box plot distribution of out-of-sample tracking error for the data-driven index tracking models

Figure [14](https://arxiv.org/html/2601.03927v1#S4.F14 "Figure 14 ‣ 4.5.3 Performance evaluation of Data-driven index tracking models ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the distribution of tracking errors for the data-driven models. DNNF clearly outperforms all others, achieving the lowest and most stable tracking error, with values tightly concentrated around very small magnitudes—underscoring its robustness across evaluation windows. The clustering-based models (Clust 1 and Clust 2) also perform competitively, maintaining low medians with modest spreads. In contrast, DNN and the SVR-based approaches (ϵ\epsilon-SVR and ν\nu-SVR) record higher median errors alongside wide variability and numerous outliers, indicating weaker and less reliable tracking accuracy. The autoencoder-based variants (SH-AE, SP-AE, STCK-AE, VAR-AE, Con-AE, DEN-AE) fall in the middle, producing acceptable but clearly inferior error distributions compared to DNNF and clustering methods.

Taken together, these results reinforce DNNF as the most accurate and stable data-driven tracker, closely followed by clustering-based approaches, while SVR and baseline DNN remain the least effective within this category.

Which modeling framework is generally better suited for tracking the S&P 500?
We now provide a comparative perspective across the three modeling paradigms—optimization-based models (8 variants), statistical-based models (7 variants), and data-driven models (14 variants)—to assess their relative effectiveness in replicating the S&P 500 index.

* •

  Tracking error and correlation with the index:
  Excluding SES, which is insufficiently diversified (allocating to only 2–3 assets), the remaining optimization-based portfolios achieve exceptionally tight tracking errors in the range 0.001420.00142–0.001590.00159 (median =0.00146=0.00146) and very high correlations of 99.09%–99.25% (median =99.09%=99.09\%).
  Statistical-based models (excluding the poorly diversified LSR and QR) deliver somewhat weaker performance, with TE values between 0.001480.00148–0.003030.00303 (median =0.00206=0.00206) and correlations of 96.75%–99.17% (median =98.64%=98.64\%).
  Data-driven models are the most heterogeneous: while the best (DNNF) achieves TE =0.00153=0.00153 and correlation =99.11%=99.11\%, the category overall spans a wider TE range of 0.001530.00153–0.004980.00498 (median =0.00388=0.00388) and correlation range of 90.14%–99.11% (median =94.3%=94.3\%).
  These results indicate that optimization formulations, as a group, provide the most accurate and consistent index replication, with statistical approaches ranking second and data-driven approaches showing greater variability despite some standout performers.
* •

  Information ratio:
  In terms of risk-adjusted excess return, optimization models generate information ratios between 0.01740.0174–0.05500.0550 (median =0.0342=0.0342), while statistical models achieve 0.02090.0209–0.05450.0545 (median =0.0436=0.0436). Data-driven models, by contrast, span 0.00990.0099–0.04930.0493 (median =0.0270=0.0270).
  Although the single highest information ratio is produced by an optimization-based model, the statistical frameworks provide the strongest performance overall, delivering the highest median and a tighter concentration of values. This suggests that statistical formulations are particularly effective when the objective is not just tight index replication, but also improving risk-adjusted returns.
* •

  Turnover ratio:
  Turnover, a proxy for transaction costs, further differentiates the paradigms. Optimization-based portfolios fall in the range 1.141.14–1.911.91 (median =1.20=1.20), implying frequent rebalancing and higher trading costs. Statistical-based models report a similar but slightly lower median of 1.181.18. In contrast, data-driven models are substantially more cost-efficient, spanning 0.600.60–1.861.86 with a median of 0.870.87.
  These results highlight a fundamental trade-off: optimization models achieve the tightest tracking but at the expense of higher turnover, whereas data-driven models strike a better balance between tracking accuracy and cost efficiency.
* •

  Computational efficiency:
  A final distinction emerges in solver times. All optimization models (except SES) are computationally intensive, requiring 17–18 hours on average per evaluation window due to the complexity of cardinality-constrained formulations. Among statistical models, only Cvx\_CoInt incurs comparable costs (18 hours), while the others are solved in seconds. Data-driven models are generally the most efficient, with clustering, random forest, SVR, and autoencoder methods completing in seconds, though deep learning models (DNN and DNNF) remain computationally demanding, requiring minutes rather than seconds.
  From an implementation standpoint, statistical and most machine learning methods are far more practical for large-scale or high-frequency applications, whereas optimization-based formulations may be prohibitive without access to substantial computing resources.

Taken together, the comparative evidence reveals clear trade-offs across the three paradigms: optimization models deliver the most precise index replication but at high turnover and computational cost; statistical models stand out in risk-adjusted performance, particularly information ratios; and data-driven methods offer scalable, low-cost solutions with moderate tracking accuracy. The “best” framework thus depends on the investor’s priority, tight replication, enhanced return–risk trade-offs, or efficiency and scalability. The next section sharpens these contrasts through a head-to-head comparison of the top-performing models from each category.

#### 4.5.4 Comparative analysis of the best models from the three paradigms

This section compares the strongest performers from each modeling paradigm—optimization, statistical, and data-driven—based on their out-of-sample tracking ability, return–risk characteristics, and statistical robustness. The three models identified are: (1) TEV from optimization-based formulations, (2) Cvx\_CoInt from statistical approaches, and (3) DNNF from data-driven methods.

Table 11: Comparison of the best index-tracking models across modeling paradigms (optimization: TEV; statistical: Cvx-CoInt; data-driven: DNNF) and the S&P 500 index.
Panel I reports performance measures; Panel II shows pairwise pp-values from one-sided paired tt-tests on tracking error.
Best values among the models are in bold; worst are in italics.

| Panel I: Out-of-sample performance | | | | |
| --- | --- | --- | --- | --- |
| Models | TEV | Cvx\_CoInt | DNNF | S&P 500 |
| Tracking performance | | | | |
| Tracking error | 0.00142 | 0.00148 | 0.00153 | – |
| Correlation (%) | 99.25 | 99.17 | 99.11 | – |
| Return performance | | | | |
| Average return | 0.00044 | 0.00049 | 0.00047 | 0.00042 |
| Minimum return | -0.12619 | -0.11753 | -0.11643 | -0.11984 |
| Maximum return | 0.10090 | 0.09713 | 0.10149 | 0.09383 |
| Risk performance | | | | |
| Volatility | 0.01162 | 0.01148 | 0.01144 | 0.01142 |
| Avg drawdown | 0.03675 | 0.03626 | 0.03650 | 0.03835 |
| Risk-adjusted performance | | | | |
| Sharpe ratio | 0.03816 | 0.04226 | 0.04065 | 0.03650 |
| Sortino ratio | 0.05179 | 0.05740 | 0.05537 | 0.04931 |
| Treynor ratio | 0.00044 | 0.00049 | 0.00047 | 0.00042 |
| Information ratio | 0.01875 | 0.04629 | 0.03167 | – |
| Turnover and complexity | | | | |
| Turnover (TR) | 1.18920 | 1.20571 | 0.59882 | – |
| No. of assets | 45 | 45 | 45 | – |
| Solver time | 18.01h | 18.10h | 51.63m | – |
| Panel II: Pairwise pp-values of tracking error tt-tests | | | | |
| pp-values | TEV | Cvx\_CoInt | DNNF |  |
| TEV | \*\*\*\*\*\* | 0.95202 | 0.99344 |  |
| Cvx\_CoInt | 0.04798 | \*\*\*\*\*\* | 0.81170 |  |
| DNNF | 0.00656 | 0.18829 | \*\*\*\*\*\* |  |

Table [11](https://arxiv.org/html/2601.03927v1#S4.T11 "Table 11 ‣ 4.5.4 Comparative analysis of the best models from the three paradigms ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") reports their comparative performance. All three deliver very tight replication of the S&P 500, with correlations exceeding 99% and extremely low tracking errors. Among them, the optimization model TEV provides the most accurate benchmark replication, achieving both the lowest tracking error (0.00142) and the highest correlation (99.25%). The statistical model Cvx\_CoInt follows closely, but distinguishes itself with the best balance of return and risk, recording the highest Sharpe, Sortino, and Information ratios. The data-driven DNNF model, while slightly weaker on pure tracking precision, is the most cost-effective and computationally efficient, combining low turnover with solver times in minutes rather than hours. The lower panel of Table [11](https://arxiv.org/html/2601.03927v1#S4.T11 "Table 11 ‣ 4.5.4 Comparative analysis of the best models from the three paradigms ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") presents the pairwise pp-values from the tracking error tests. At the 5% significance level, TEV statistically outperforms both Cvx\_CoInt (p=0.04798p=0.04798) and DNNF (p=0.00656p=0.00656). The difference between Cvx\_CoInt and DNNF is not statistically significant (p=0.18829p=0.18829), indicating that their tracking errors are comparable in practice. Taken together, TEV is the most precise replicator, Cvx\_CoInt the strongest risk-adjusted performer, and DNNF the most efficient in cost and computation.

![Refer to caption](CR_best.png)


Figure 15: Cumulative returns of the best tracking portfolios across the three modeling paradigms for index tracking along with the S&P 500 index

Figure [15](https://arxiv.org/html/2601.03927v1#S4.F15 "Figure 15 ‣ 4.5.4 Comparative analysis of the best models from the three paradigms ‣ 4.5 Out-of-sample analysis ‣ 4 Numerical study ‣ A comprehensive review and analysis of different modeling approaches for financial index tracking problem") illustrates the cumulative returns of the S&P 500 index alongside the three benchmark models over 2019 trading days (December 2014–August 2022). All three models track the index closely, moving almost in lockstep. TEV remains the closest to the benchmark throughout, underscoring its superior replication precision. Cvx\_CoInt consistently compounds slightly higher returns during prolonged market upswings, reflecting its stronger risk–return balance. DNNF traces a trajectory nearly identical to Cvx\_CoInt, albeit with slightly lower peaks, while offering the lowest turnover and fastest computation. Overall, this head-to-head comparison confirms that each paradigm brings distinct strengths: TEV sets the standard in pure tracking accuracy, Cvx\_CoInt achieves the most favorable return–risk trade-off, and DNNF demonstrates how modern machine learning can achieve competitive accuracy with unparalleled cost and computational efficiency.

## 5 Conclusion

This review has examined the literature on index tracking by systematically classifying existing approaches into three paradigms: optimization-based models, statistical frameworks, and data-driven machine learning methods. Each paradigm contributes distinct strengths: optimization-based models provide rigorous formulations for precise benchmark replication; statistical methods exploit structural relationships in asset returns; and data-driven approaches introduce flexibility and scalability to capture nonlinear dependencies and complex market dynamics.

Alongside the conceptual survey, a large-scale empirical analysis was conducted on 29 representative models applied to the S&P 500 index. The findings reveal clear contrasts across paradigms. The tracking-error variance (TEV) model delivers the most accurate replication, achieving the lowest tracking error and the highest correlation with the index. The convex cointegration (Cvx\_CoInt) model attains the strongest risk-adjusted performance, as reflected in superior Sharpe, Sortino, and information ratios. In contrast, the deep neural network with fixed noise (DNNF) achieves competitive replication accuracy while offering substantial advantages in terms of turnover and computational efficiency. These results highlight that the optimal choice of methodology depends on the investor’s objective, whether minimizing replication error, maximizing return–risk trade-offs, or improving scalability.

The review also identifies several promising directions for future research. Important extensions include dynamic model selection across market regimes, explicit incorporation of transaction costs and liquidity constraints, and the development of multi-period rebalancing policies. Moreover, explainable and robust machine learning approaches remain largely unexplored in this context and represent a natural avenue for further study.

To encourage reproducibility and comparability, we provide an open-source repository containing implementations of the models reviewed here together with the experimental framework. This resource allows researchers and practitioners to benchmark new methods directly against established ones, supporting continued progress in the design and evaluation of index-tracking strategies.

## Data Declaration

The data that support the findings of this study were sourced from Bloomberg data stream and are available from the corresponding author on reasonable request. The codes (R/python) used for the analysis are publicly accessible through the project’s GitHub repository <https://github.com/vrindadhingra/index-tracking-review>.

## Declaration of Generative AI and AI-assisted technologies in the writing process

While preparing this work, the authors used GPT-5 to refine the language and enhance the clarity of the manuscript. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication.

## Disclosure of Interest

The authors declare no conflict of interest.

## References

* \bibcommenthead
* Acosta-González et al. (2015)

  Acosta-González E, Armas-Herrera R, Fernández-Rodríguez F (2015) On the index tracking and the statistical arbitrage choosing the stocks by means of cointegration: the role of stock picking. Quantitative Finance 15(6):1075 – 1091. [10.1080/14697688.2014.940604](https:/doi.org/10.1080/14697688.2014.940604)
* Aguilar et al. (2022)

  Aguilar M, Custovic A, Huang Z, et al. (2022) Creating better tracking portfolios with quantiles. Investment Management and Financial Innovations 19(1):14 – 31. [10.21511/imfi.19(1).2022.02](https:/doi.org/10.21511/imfi.19(1).2022.02)
* Anadu et al. (2020)

  Anadu K, Mathias K, Patrick M, et al. (2020) The shift from active to passive investing: Risks to financial stability? Financial Analysts Journal 76(4):23–39. [10.1080/0015198X.2020.1779498](https:/doi.org/10.1080/0015198X.2020.1779498)
* Andriosopoulos et al. (2013)

  Andriosopoulos K, Doumpos M, Papapostolou NC, et al. (2013) Portfolio optimization and index tracking for the shipping stock and freight markets using evolutionary algorithms. Transportation Research Part E: Logistics and Transportation Review 52:16 – 34. [10.1016/j.tre.2012.11.006](https:/doi.org/10.1016/j.tre.2012.11.006), URL <https://www.scopus.com/inward/record.uri?eid=2-s2.0-84872076455&doi=10.1016%2fj.tre.2012.11.006&partnerID=40&md5=0e472a368373f02a5bf8fe47e8f306ff>
* Anis et al. (2023)

  Anis HT, Costa G, Kwon RH (2023) Risk-allocation-based index tracking. Computers and Operations Research 154. [10.1016/j.cor.2023.106219](https:/doi.org/10.1016/j.cor.2023.106219)
* Ayllón-Gavilán et al. (2024)

  Ayllón-Gavilán R, Martínez-Estudillo FJ, Guijo-Rubio D, et al. (2024) Splitting criteria for ordinal decision trees: an experimental study. arXiv:2412.13697
* Ayón et al. (2024)

  Ayón JAD, de Lourdes Sandoval Solis M, Velázquez RG, et al. (2024) Harmony search based metaheuristic for the index tracking problem. In: Workshop on Engineering Applications, Springer, pp 15–26, [10.1007/978-3-031-74598-0\_2](https:/doi.org/10.1007/978-3-031-74598-0_2)
* Beasley et al. (2003)

  Beasley J, Meade N, Chang TJ (2003) An evolutionary heuristic for the index tracking problem. European Journal of Operational Research 148(3):621 – 643. [10.1016/S0377-2217(02)00425-3](https:/doi.org/10.1016/S0377-2217(02)00425-3)
* Benidis et al. (2018)

  Benidis K, Feng Y, Palomar DP (2018) Sparse portfolios for high-dimensional financial index tracking. IEEE Transactions on Signal Processing 66(1):155 – 170. [10.1109/TSP.2017.2762286](https:/doi.org/10.1109/TSP.2017.2762286)
* Bogle (2011)

  Bogle JC (2011) How the index fund was born. Wall Street Journal—Eastern Edition 258:A15
* Boyd and Vandenberghe (2004)

  Boyd S, Vandenberghe L (2004) Convex Optimization. Cambridge University Press, Cambridge, UK
* Bradrania et al. (2022)

  Bradrania R, Pirayesh Neghab D, Shafizadeh M (2022) State-dependent stock selection in index tracking: a machine learning approach. Financial Markets and Portfolio Management 36(1):1–28
* Canakgoz and Beasley (2009)

  Canakgoz N, Beasley J (2009) Mixed-integer programming approaches for index tracking and enhanced indexation. European Journal of Operational Research 196(1):384 – 399. [10.1016/j.ejor.2008.03.015](https:/doi.org/10.1016/j.ejor.2008.03.015)
* Cao et al. (2022)

  Cao Y, Li H, Yang Y (2022) Combining random forest and multicollinearity modeling for index tracking. Communications in Statistics: Simulation and Computation [10.1080/03610918.2022.2116050](https:/doi.org/10.1080/03610918.2022.2116050)
* Cesarone et al. (2025)

  Cesarone F, Paolo AD, Bufalo M, et al. (2025) A benchmark-asset principal component factorization for index tracking on large investment universes. Finance Research Letters 79:107,244. [10.1016/j.frl.2025.107244](https:/doi.org/10.1016/j.frl.2025.107244)
* Chen and Kwon (2012)

  Chen C, Kwon RH (2012) Robust portfolio selection for index tracking. Computers and Operations Research 39(4):829 – 837. [10.1016/j.cor.2010.08.019](https:/doi.org/10.1016/j.cor.2010.08.019)
* Corielli and Marcellino (2006)

  Corielli F, Marcellino M (2006) Factor based index tracking. Journal of Banking and Finance 30(8):2215 – 2233. [10.1016/j.jbankfin.2005.07.012](https:/doi.org/10.1016/j.jbankfin.2005.07.012)
* Dai and Li (2024)

  Dai Z, Li L (2024) Deep learning for enhanced index tracking. Quantitative Finance 24(5):569–591
* De Leone (2011)

  De Leone R (2011) Support vector regression for time series analysis. In: Operations Research Proceedings 2010, Springer, Berlin, Heidelberg, [10.1007/978-3-642-20009-0\_6](https:/doi.org/10.1007/978-3-642-20009-0_6), URL <https://doi.org/10.1007/978-3-642-20009-0_6>
* Derigs and Nickel (2003)

  Derigs U, Nickel NH (2003) Meta-heuristic based decision support for portfolio optimization with a case study on tracking error minimization in passive portfolio management. OR Spectrum 25(3):345 – 378. [10.1007/s00291-003-0127-5](https:/doi.org/10.1007/s00291-003-0127-5)
* Dose and Cincotti (2005)

  Dose C, Cincotti S (2005) Clustering of financial time series with application to index and enhanced index tracking portfolio. Physica A: Statistical Mechanics and its Applications 355(1):145 – 151. [10.1016/j.physa.2005.02.078](https:/doi.org/10.1016/j.physa.2005.02.078)
* Engle and Granger (1987)

  Engle RF, Granger CWJ (1987) Co-integration and error correction: Representation, estimation, and testing. Econometrica 55(2):251–276. [10.2307/1913236](https:/doi.org/10.2307/1913236)
* Fama (1970)

  Fama EF (1970) Efficient capital markets: A review of theory and empirical work. The Journal of Finance 25(2):383–417
* Fastrich et al. (2014)

  Fastrich B, Paterlini S, Winker P (2014) Cardinality versus q-norm constraints for index tracking. Quantitative Finance 14(11):2019 – 2032. [10.1080/14697688.2012.691986](https:/doi.org/10.1080/14697688.2012.691986)
* Focardi and Fabozzi (2004)

  Focardi SM, Fabozzi FJ (2004) A methodology for index tracking based on time-series clustering. Quantitative Finance 4(4):417 – 425. [10.1080/14697680400008668](https:/doi.org/10.1080/14697680400008668)
* Frino and Gallagher (2001)

  Frino A, Gallagher DR (2001) Tracking s&p 500 index funds. Journal of Portfolio Management 28(1):44 – 55. [10.3905/jpm.2001.319822](https:/doi.org/10.3905/jpm.2001.319822)
* Gaivoronski et al. (2005)

  Gaivoronski AA, Krylov S, Van Der Wijst N (2005) Optimal portfolio selection and dynamic benchmark tracking. European Journal of Operational Research 163(1):115 – 131. [10.1016/j.ejor.2003.12.001](https:/doi.org/10.1016/j.ejor.2003.12.001)
* Goel et al. (2018)

  Goel A, Sharma A, Mehra A (2018) Index tracking and enhanced indexing using mixed conditional value-at-risk. Journal of Computational and Applied Mathematics 335:361 – 380. [10.1016/j.cam.2017.12.015](https:/doi.org/10.1016/j.cam.2017.12.015)
* Goel et al. (2024)

  Goel A, Filipović D, Pasricha P (2024) Sparse portfolio selection via topological data analysis based clustering. URL <https://arxiv.org/abs/2401.16920>, <2401.16920>
* Goel et al. (2025)

  Goel A, Filipović D, Pasricha P (2025) Sparse portfolio selection via topological data analysis based clustering. Quantitative Finance 25(8):1261–1291. [10.1080/14697688.2025.2544762](https:/doi.org/10.1080/14697688.2025.2544762)
* Goel et al. (2026)

  Goel A, Pasricha P, Kanniainen J (2026) Risk reduced sparse index tracking portfolio: A topological data analysis approach. Omega 138:103,432. [10.1016/j.omega.2025.103432](https:/doi.org/10.1016/j.omega.2025.103432)
* Goodell et al. (2021)

  Goodell JW, Kumar S, Lim WM, et al. (2021) Artificial intelligence and machine learning in finance: Identifying foundations, themes, and research clusters from bibliometric analysis. Journal of Behavioral and Experimental Finance 32:100,577. [https://doi.org/10.1016/j.jbef.2021.100577](https:/doi.org/https://doi.org/10.1016/j.jbef.2021.100577)
* Granger (1981)

  Granger CWJ (1981) Some properties of time series data and their use in econometric model specification. Journal of Econometrics 16(1):121–130. [10.1016/0304-4076(81)90079-8](https:/doi.org/10.1016/0304-4076(81)90079-8)
* Grassetti (2025)

  Grassetti F (2025) Optimizing index tracking: A random matrix theory approach to portfolio selection. Physica A: Statistical Mechanics and its Applications 674:130,747. [10.1016/j.physa.2025.130747](https:/doi.org/10.1016/j.physa.2025.130747)
* Guastaroba and Speranza (2012)

  Guastaroba G, Speranza M (2012) Kernel search: An application to the index tracking problem. European Journal of Operational Research 217(1):54 – 68. [10.1016/j.ejor.2011.09.004](https:/doi.org/10.1016/j.ejor.2011.09.004)
* Jensen (1968)

  Jensen MC (1968) The performance of mutual funds in the period 1945–1964. The Journal of Finance 23(2)
* Kim and Kim (2020)

  Kim S, Kim S (2020) Index tracking through deep latent representation learning. Quantitative Finance 20(4):639 – 652. [10.1080/14697688.2019.1683599](https:/doi.org/10.1080/14697688.2019.1683599)
* Konno and Watanabe (1996)

  Konno H, Watanabe H (1996) Bond portfolio optimization problems and their applications to index tracking: A partial optimization approach. Journal of the Operations Research Society of Japan 39(3):295 – 306. [10.15807/jorsj.39.295](https:/doi.org/10.15807/jorsj.39.295)
* Krink et al. (2009)

  Krink T, Mittnik S, Paterlini S (2009) Differential evolution and combinatorial search for constrained index-tracking. Annals of Operations Research 172(1):153 – 176. [10.1007/s10479-009-0552-1](https:/doi.org/10.1007/s10479-009-0552-1)
* Kwak et al. (2021)

  Kwak Y, Song J, Lee H (2021) Neural network with fixed noise for index-tracking portfolio optimization. Expert Systems with Applications 183. [10.1016/j.eswa.2021.115298](https:/doi.org/10.1016/j.eswa.2021.115298)
* Kwon and Wu (2017)

  Kwon RH, Wu D (2017) Factor-based robust index tracking. Optimization and Engineering 18(2):443 – 466. [10.1007/s11081-016-9314-5](https:/doi.org/10.1007/s11081-016-9314-5)
* Larsen and Resnick (1998)

  Larsen GA, Resnick BG (1998) Empirical insights on indexing: how capitalization, stratification and weighting can affect tracking error. Journalof Portfolio Management 25(1):51
* Li (2020)

  Li N (2020) Efficient sparse portfolios based on composite quantile regression for high-dimensional index tracking. Journal of Statistical Computation and Simulation 90(8):1466 – 1478. [10.1080/00949655.2020.1731750](https:/doi.org/10.1080/00949655.2020.1731750)
* Li et al. (2025)

  Li N, Zhu G, Niu Y, et al. (2025) Fast and stable portfolios through huber’s criterion for constrained index tracking. The Engineering Economist 70(1-2):57–71. [10.1080/0013791X.2025.2489362](https:/doi.org/10.1080/0013791X.2025.2489362)
* Malkiel (2003)

  Malkiel B (2003) Passive investment strategies and efficient markets. European Financial Management 9:1–10. [10.1111/1468-036X.00205](https:/doi.org/10.1111/1468-036X.00205)
* Markowitz (1952)

  Markowitz H (1952) Portfolio selection. The Journal of Finance 7(1):77–91
* Mezali and Beasley (2013)

  Mezali H, Beasley J (2013) Quantile regression for index tracking and enhanced indexation. Journal of the Operational Research Society 64(11):1676 – 1692. [10.1057/jors.2012.186](https:/doi.org/10.1057/jors.2012.186)
* Mutunge and Haugland (2018)

  Mutunge P, Haugland D (2018) Minimizing the tracking error of cardinality constrained portfolios. Computers and Operations Research 90:33 – 41. [10.1016/j.cor.2017.09.002](https:/doi.org/10.1016/j.cor.2017.09.002)
* Ouyang et al. (2019)

  Ouyang H, Zhang X, Yan H (2019) Index tracking based on deep neural network. Cognitive Systems Research 57:107 – 114. [10.1016/j.cogsys.2018.10.022](https:/doi.org/10.1016/j.cogsys.2018.10.022)
* Peng et al. (2023a)

  Peng X, Gong C, He XD (2023a) Reinforcement learning for financial index tracking. arXiv preprint arXiv:230802820
* Peng et al. (2023b)

  Peng X, Gong C, He XD (2023b) Reinforcement learning for financial index tracking. URL <https://arxiv.org/abs/2308.02820>, <2308.02820>
* Prondzinski and Miller (2018)

  Prondzinski D, Miller M (2018) Active versus passive investing: Evidence from the 2009-2017 market. Journal of Accounting and Finance 18(8):119–143
* Rockafellar and Uryasev (2002)

  Rockafellar R, Uryasev S (2002) Conditional value-at-risk for general loss distributions. Journal of Banking and Finance 26(7):1443 – 1471. [10.1016/S0378-4266(02)00271-6](https:/doi.org/10.1016/S0378-4266(02)00271-6), URL <https://www.scopus.com/inward/record.uri?eid=2-s2.0-0036076694&doi=10.1016%2fS0378-4266%2802%2900271-6&partnerID=40&md5=2bc00d8a616831f8a9c454c8ef9bbe7c>
* Roll (1992)

  Roll R (1992) A mean/variance analysis of tracking error. Journal of Portfolio Management 18(4):13–22
* Álvaro Rubio-García et al. (2024)

  Álvaro Rubio-García, Fernández-Lorenzo S, García-Ripoll JJ, et al. (2024) Accurate solution of the index tracking problem with a hybrid simulated annealing algorithm. Physica A: Statistical Mechanics and its Applications 639. [10.1016/j.physa.2024.129637](https:/doi.org/10.1016/j.physa.2024.129637)
* Rudolf et al. (1999)

  Rudolf M, Wolter HJ, Zimmermann H (1999) A linear model for tracking error minimization. Journal of Banking and Finance 23(1):85 – 103. [10.1016/S0378-4266(98)00076-4](https:/doi.org/10.1016/S0378-4266(98)00076-4)
* Ruiz-Torrubiano and Suárez (2009)

  Ruiz-Torrubiano R, Suárez A (2009) A hybrid optimization approach to index tracking. Annals of Operations Research 166(1):57 – 71. [10.1007/s10479-008-0404-4](https:/doi.org/10.1007/s10479-008-0404-4)
* Sant’Anna et al. (2017)

  Sant’Anna LR, Filomena TP, Caldeira JF (2017) Index tracking and enhanced indexing using cointegration and correlation with endogenous portfolio selection. Quarterly Review of Economics and Finance 65:146 – 157. [10.1016/j.qref.2016.08.008](https:/doi.org/10.1016/j.qref.2016.08.008)
* Sant’Anna et al. (2020a)

  Sant’Anna LR, Caldeira JF, Filomena TP (2020a) Lasso-based index tracking and statistical arbitrage long-short strategies. North American Journal of Economics and Finance 51. [10.1016/j.najef.2019.101055](https:/doi.org/10.1016/j.najef.2019.101055)
* Sant’Anna et al. (2020b)

  Sant’Anna LR, de Oliveira AD, Filomena TP, et al. (2020b) Solving the index tracking problem based on a convex reformulation for cointegration. Finance Research Letters 37. [10.1016/j.frl.2019.101356](https:/doi.org/10.1016/j.frl.2019.101356)
* Sant’Anna et al. (2022)

  Sant’Anna LR, Righi MB, Müller FM, et al. (2022) Risk measure index tracking model. International Review of Economics and Finance 80:361 – 383. [10.1016/j.iref.2022.02.032](https:/doi.org/10.1016/j.iref.2022.02.032)
* Sant’Anna et al. (2017)

  Sant’Anna LR, Filomena TP, Guedes PC, et al. (2017) Index tracking with controlled number of assets using a hybrid heuristic combining genetic algorithm and non-linear programming. Annals of Operations Research 258(2):849 – 867. [10.1007/s10479-016-2111-x](https:/doi.org/10.1007/s10479-016-2111-x)
* Scozzari et al. (2013)

  Scozzari A, Tardella F, Paterlini S, et al. (2013) Exact and heuristic approaches for the index tracking problem with ucits constraints. Annals of Operations Research 205(1):235 – 250. [10.1007/s10479-012-1207-1](https:/doi.org/10.1007/s10479-012-1207-1)
* Sharpe (1964)

  Sharpe WF (1964) Capital asset prices: A theory of market equilibrium under conditions of risk. The Journal of Finance 19(3):425–442
* Silva and de Almeida Filho (2024)

  Silva JCS, de Almeida Filho AT (2024) A systematic literature review on solution approaches for the index tracking problem. IMA Journal of Management Mathematics 35(2):163 – 196. [10.1093/imaman/dpad007](https:/doi.org/10.1093/imaman/dpad007)
* Strub and Baumann (2018)

  Strub O, Baumann P (2018) Optimal construction and rebalancing of index-tracking portfolios. European Journal of Operational Research 264(1):370 – 387. [10.1016/j.ejor.2017.06.055](https:/doi.org/10.1016/j.ejor.2017.06.055), URL <https://www.scopus.com/inward/record.uri?eid=2-s2.0-85025479826&doi=10.1016%2fj.ejor.2017.06.055&partnerID=40&md5=857faa5a95faada118f9f79319c58492>
* Takeda et al. (2010)

  Takeda A, Gotoh JY, Sugiama M (2010) Support vector regression as conditional value-at-risk minimization with application to financial time-series analysis. p 118 – 123, [10.1109/MLSP.2010.5589245](https:/doi.org/10.1109/MLSP.2010.5589245)
* Takeda et al. (2013)

  Takeda A, Niranjan M, Gotoh Jy, et al. (2013) Simultaneous pursuit of out-of-sample performance and sparsity in index tracking portfolios. Computational Management Science 10(1):21 – 49. [10.1007/s10287-012-0158-y](https:/doi.org/10.1007/s10287-012-0158-y)
* Tang and Li (2014)

  Tang R, Li P (2014) Index optimization replication algorithm by using the soft subspace clustering method. In: 2014 IEEE 7th Joint International Information Technology and Artificial Intelligence Conference, ITAIC 2014, p 414 – 418, [10.1109/ITAIC.2014.7065082](https:/doi.org/10.1109/ITAIC.2014.7065082)
* Teng et al. (2017)

  Teng Y, Yang L, Yuan K, et al. (2017) Index tracking by using sparse support vector regression. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics) 10559 LNCS:293 – 315. [10.1007/978-3-319-67777-4\_26](https:/doi.org/10.1007/978-3-319-67777-4_26)
* Wang et al. (2012)

  Wang M, Xu C, Xu F, et al. (2012) A mixed 0-1 lp for index tracking problem with cvar risk constraints. Annals of Operations Research 196(1):591 – 609. [10.1007/s10479-011-1042-9](https:/doi.org/10.1007/s10479-011-1042-9)
* Wang et al. (2018)

  Wang M, Xu F, Dai YH (2018) An index tracking model with stratified sampling and optimal allocation. Applied Stochastic Models in Business and Industry 34(2):144 – 157. [10.1002/asmb.2287](https:/doi.org/10.1002/asmb.2287)
* Wang et al. (2024)

  Wang YJ, Wu LH, Wu LC (2024) An integrative extraction approach for index-tracking portfolio construction and forecasting under a deep learning framework. Journal of Supercomputing 80(2):2047 – 2066. [10.1007/s11227-023-05538-z](https:/doi.org/10.1007/s11227-023-05538-z)
* Wu et al. (2017)

  Wu D, Kwon RH, Costa G (2017) A constrained cluster-based approach for tracking the s&p 500 index. International Journal of Production Economics 193:222 – 243. [10.1016/j.ijpe.2017.07.018](https:/doi.org/10.1016/j.ijpe.2017.07.018)
* Wu and Yang (2014)

  Wu L, Yang Y (2014) Nonnegative elastic net and application in index tracking. Applied Mathematics and Computation 227:541 – 552. [10.1016/j.amc.2013.11.049](https:/doi.org/10.1016/j.amc.2013.11.049)
* Wu et al. (2014a)

  Wu L, Yang Y, Liu H (2014a) Nonnegative-lasso and application in index tracking. Computational Statistics and Data Analysis 70:116 – 126. [10.1016/j.csda.2013.08.012](https:/doi.org/10.1016/j.csda.2013.08.012)
* Wu et al. (2014b)

  Wu L, Yang Y, Liu H (2014b) Nonnegative-lasso and application in index tracking. Computational Statistics and Data Analysis 70:116 – 126. [10.1016/j.csda.2013.08.012](https:/doi.org/10.1016/j.csda.2013.08.012)
* Xu et al. (2016)

  Xu F, Lu Z, Xu Z (2016) An efficient optimization approach for a cardinality-constrained index tracking problem. Optimization Methods and Software 31(2):258 – 271. [10.1080/10556788.2015.1062891](https:/doi.org/10.1080/10556788.2015.1062891)
* Xu et al. (2026)

  Xu F, Li B, Ma J, et al. (2026) Network-based index tracking using asset dependency structures. International Transactions of Operational Research 33:1498–1524. [doi.org/10.1111/itor.70100](https:/doi.org/doi.org/10.1111/itor.70100)
* Yuanyuan Cao and Yang (2022)

  Yuanyuan Cao HL, Yang Y (2022) Combining random forest and multicollinearity modeling for index tracking. Communications in Statistics - Simulation and Computation 0(0):1–12. [10.1080/03610918.2022.2116050](https:/doi.org/10.1080/03610918.2022.2116050)
* Zapata Quimbayo and Moreno Trujillo (2025)

  Zapata Quimbayo C, Moreno Trujillo J (2025) Index tracking based on norm-constraints and regularization. In: Applied Computer Sciences in Engineering. WEA 2024. Communications in Computer and Information Science, vol 2222. Springer, Cham, [10.1007/978-3-031-74598-0\_7](https:/doi.org/10.1007/978-3-031-74598-0_7)
* Zhang et al. (2020)

  Zhang C, Liang S, Lyu F, et al. (2020) Stock-index tracking optimization using auto-encoders. Frontiers in Physics 8. [10.3389/fphy.2020.00388](https:/doi.org/10.3389/fphy.2020.00388)
* Zhang et al. (2025)

  Zhang F, Lyu Q, Wang J (2025) Regression-based index tracking versus clustering-based index tracking: An empirical study. In: Advances in Neural Networks – ISNN 2025: 19th International Symposium on Neural Networks, Zhangye, China, August 22–24, 2025, Proceedings, p 51–62, [10.1007/978-981-95-1233-1\_5](https:/doi.org/10.1007/978-981-95-1233-1_5), URL <https://doi.org/10.1007/978-981-95-1233-1_5>
* Zhang et al. (2021)

  Zhang R, Li H, Wang J (2021) Index tracking based on dynamic time warping and constrained k-medoids clustering. In: 11th International Conference on Intelligent Control and Information Processing, ICICIP 2021, p 352 – 359, [10.1109/ICICIP53388.2021.9642192](https:/doi.org/10.1109/ICICIP53388.2021.9642192)
* Zhang and De Smedt (2024)

  Zhang Y, De Smedt J (2024) Index tracking using shapley additive explanations and one-dimensional pointwise convolutional autoencoders. International Review of Financial Analysis 95:103,487
* Zheng et al. (2020a)

  Zheng Y, Chen B, Hospedales TM, et al. (2020a) Index tracking with cardinality constraints: A stochastic neural networks approach. In: AAAI 2020 - 34th AAAI Conference on Artificial Intelligence, p 1242 – 1249
* Zheng et al. (2020b)

  Zheng Y, Chen B, Hospedales TM, et al. (2020b) Index tracking with cardinality constraints: A stochastic neural networks approach. In: Proceedings of the AAAI conference on artificial intelligence, pp 1242–1249
* Zhu et al. (2010)

  Zhu H, Chen Y, Wang K (2010) A particle swarm optimization heuristic for the index tacking problem. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics) 6063 LNCS(PART 1):238 – 245. [10.1007/978-3-642-13278-0\_31](https:/doi.org/10.1007/978-3-642-13278-0_31), URL <https://www.scopus.com/inward/record.uri?eid=2-s2.0-77954428629&doi=10.1007%2f978-3-642-13278-0_31&partnerID=40&md5=3529b1d0030d487aab7e36b258d4fdff>