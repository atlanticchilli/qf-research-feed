---
authors:
- Peng Liu
doc_id: arxiv:2510.21165v1
family_id: arxiv:2510.21165
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The local Gaussian correlation networks among return tails in the Chinese stock
  market
url_abs: http://arxiv.org/abs/2510.21165v1
url_html: https://arxiv.org/html/2510.21165v1
venue: arXiv q-fin
version: 1
year: 2025
---


Peng Liu

###### Abstract

Financial networks based on Pearson correlations have been intensively studied.
However, previous studies may have led to misleading and catastrophic results because of several critical shortcomings of the Pearson correlation.
The local Gaussian correlation coefficient, a new measurement of statistical dependence between variables,
has unique advantages including capturing local nonlinear dependence and handling heavy-tailed distributions.
This study constructs financial networks using the local Gaussian correlation coefficients between tail regions of stock returns in the Shanghai Stock Exchange.
The work systematically analyzes fundamental network metrics including node centrality, average shortest path length, and entropy.
Compared with the local Gaussian correlation network among positive tails and the conventional Pearson correlation network,
the properties of the local Gaussian correlation network among negative tails are more sensitive to the stock market risks.
This finding suggests researchers should prioritize the local Gaussian correlation network among negative tails.
Future work should reevaluate existing findings using the local Gaussian correlation method.
  
  
Keywords: Local Gaussian correlation; Complex financial network; Chinese stock market

## 1 Introduction

Over the past decades,
network science has been widely used to study complex systems from multiple academic fields,
and gained insightful findings that are not accessible with traditional methods.[[1](https://arxiv.org/html/2510.21165v1#bib.bib1), [2](https://arxiv.org/html/2510.21165v1#bib.bib2), [3](https://arxiv.org/html/2510.21165v1#bib.bib3), [4](https://arxiv.org/html/2510.21165v1#bib.bib4), [5](https://arxiv.org/html/2510.21165v1#bib.bib5), [6](https://arxiv.org/html/2510.21165v1#bib.bib6), [7](https://arxiv.org/html/2510.21165v1#bib.bib7), [8](https://arxiv.org/html/2510.21165v1#bib.bib8), [9](https://arxiv.org/html/2510.21165v1#bib.bib9)]
The financial system is a typical complex system.
Therefore, various complex financial networks have been studied since 1999.[[7](https://arxiv.org/html/2510.21165v1#bib.bib7), [8](https://arxiv.org/html/2510.21165v1#bib.bib8), [9](https://arxiv.org/html/2510.21165v1#bib.bib9)]

Among various complex financial networks,
the correlation-based networks in various financial markets have been studied intensively.
[[7](https://arxiv.org/html/2510.21165v1#bib.bib7), [8](https://arxiv.org/html/2510.21165v1#bib.bib8), [9](https://arxiv.org/html/2510.21165v1#bib.bib9), [10](https://arxiv.org/html/2510.21165v1#bib.bib10), [11](https://arxiv.org/html/2510.21165v1#bib.bib11), [12](https://arxiv.org/html/2510.21165v1#bib.bib12), [13](https://arxiv.org/html/2510.21165v1#bib.bib13), [14](https://arxiv.org/html/2510.21165v1#bib.bib14), [15](https://arxiv.org/html/2510.21165v1#bib.bib15), [16](https://arxiv.org/html/2510.21165v1#bib.bib16), [17](https://arxiv.org/html/2510.21165v1#bib.bib17), [18](https://arxiv.org/html/2510.21165v1#bib.bib18), [19](https://arxiv.org/html/2510.21165v1#bib.bib19), [20](https://arxiv.org/html/2510.21165v1#bib.bib20)]
Such networks are crucial in understanding complex financial systems and their systemic risks.
[[7](https://arxiv.org/html/2510.21165v1#bib.bib7), [8](https://arxiv.org/html/2510.21165v1#bib.bib8), [9](https://arxiv.org/html/2510.21165v1#bib.bib9), [10](https://arxiv.org/html/2510.21165v1#bib.bib10), [11](https://arxiv.org/html/2510.21165v1#bib.bib11), [12](https://arxiv.org/html/2510.21165v1#bib.bib12), [13](https://arxiv.org/html/2510.21165v1#bib.bib13), [14](https://arxiv.org/html/2510.21165v1#bib.bib14), [15](https://arxiv.org/html/2510.21165v1#bib.bib15), [16](https://arxiv.org/html/2510.21165v1#bib.bib16), [17](https://arxiv.org/html/2510.21165v1#bib.bib17), [18](https://arxiv.org/html/2510.21165v1#bib.bib18), [19](https://arxiv.org/html/2510.21165v1#bib.bib19), [20](https://arxiv.org/html/2510.21165v1#bib.bib20)]
Previous works often constructed networks based on Pearson correlation coefficients ρ\rho among returns of financial asset prices.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8)]
However, Pearson’s ρ\rho has some critical shortcomings which can lead to misleading and potentially catastrophic results.[[21](https://arxiv.org/html/2510.21165v1#bib.bib21)]

Tjø\o stheim et. al. summarized the shortcomings of Pearson’s ρ\rho as three issues.[[21](https://arxiv.org/html/2510.21165v1#bib.bib21)]
The first one is the non-Gaussian issue.
It works well in the Gaussian case and a few non-Gaussian situations.
However, it is unsuitable for heavy-tailed distributions,
which characterize financial asset returns.[[21](https://arxiv.org/html/2510.21165v1#bib.bib21), [22](https://arxiv.org/html/2510.21165v1#bib.bib22)]
The second one is the robustness issue.
It is well known that Pearson’s ρ\rho is sensitive to outliers.
Even one single outlier in data may cause a damaging change in Pearson’s ρ\rho.
The last one is the nonlinearity issue, which may be the most damaging over other shortcomings.
Consider the case Y=X2Y=X^{2}.
Although the relationship between variables YY and XX is the strongest form of dependence in this case,
Pearson’s ρ\rho between these two variables may be zero.
Pearson’s ρ\rho fails to capture nonlinear asymmetry statistical dependence,
which widely exists among financial markets.[[21](https://arxiv.org/html/2510.21165v1#bib.bib21), [23](https://arxiv.org/html/2510.21165v1#bib.bib23), [24](https://arxiv.org/html/2510.21165v1#bib.bib24), [25](https://arxiv.org/html/2510.21165v1#bib.bib25)]
Therefore, Pearson’s ρ\rho cannot capture the complex statistical dependence for heavy-tailed variables and nonlinear situations in financial markets.

Two stylized facts characterize financial asset returns: (1) distributions of financial asset returns exhibit heavy-tailed properties,[[22](https://arxiv.org/html/2510.21165v1#bib.bib22)]
and (2) correlations among asset returns demonstrate nonlinearity and asymmetry.[[21](https://arxiv.org/html/2510.21165v1#bib.bib21), [23](https://arxiv.org/html/2510.21165v1#bib.bib23), [24](https://arxiv.org/html/2510.21165v1#bib.bib24), [25](https://arxiv.org/html/2510.21165v1#bib.bib25)]
Given these empirical characteristics and the aforementioned limitations of Pearson’s ρ\rho,
its application in measuring statistical dependence between financial asset returns may yield misleading conclusions with potentially catastrophic consequences.[[21](https://arxiv.org/html/2510.21165v1#bib.bib21)]
Consequently, previous studies on the correlation networks constructed using Pearson’s ρ\rho did not accurately capture the true interconnectedness of financial systems,
and thus may have produced misleading findings.

To overcome the weaknesses of Pearson’s ρ\rho,
researchers have proposed alternative methods for measuring nonlinear statistical dependence,
including the copula method, the conditional correlation, the distance covariance, the HSIC (Hilbert-Schmidt Independence Criterion) measure, the mutual information, and the local Gaussian correlation, among others.
For detailed comparisons of these alternatives, this paper refers readers to Refs. [23](https://arxiv.org/html/2510.21165v1#bib.bib23), [24](https://arxiv.org/html/2510.21165v1#bib.bib24), [21](https://arxiv.org/html/2510.21165v1#bib.bib21).
Among these approaches, the local Gaussian correlation proposed by Tjø\o stheim and Hufthammer demonstrates particularly great performance.[[23](https://arxiv.org/html/2510.21165v1#bib.bib23), [24](https://arxiv.org/html/2510.21165v1#bib.bib24), [21](https://arxiv.org/html/2510.21165v1#bib.bib21)]
This measure effectively captures local nonlinear asymmetry dependence and applies to heavy-tailed distributions.[[23](https://arxiv.org/html/2510.21165v1#bib.bib23), [24](https://arxiv.org/html/2510.21165v1#bib.bib24), [25](https://arxiv.org/html/2510.21165v1#bib.bib25), [21](https://arxiv.org/html/2510.21165v1#bib.bib21)]
As this measure has been successfully applied across diverse research domains,[[23](https://arxiv.org/html/2510.21165v1#bib.bib23), [24](https://arxiv.org/html/2510.21165v1#bib.bib24), [25](https://arxiv.org/html/2510.21165v1#bib.bib25), [21](https://arxiv.org/html/2510.21165v1#bib.bib21)]
this study employs this measure to analyze local nonlinear statistical dependence between stock returns in the Chinese stock market.

In finance,
the local nonlinear statistical dependence among tail regions of financial asset returns is of special interest because it plays a crucial role in understanding the market risks and optimizing investment portfolios.[[23](https://arxiv.org/html/2510.21165v1#bib.bib23), [24](https://arxiv.org/html/2510.21165v1#bib.bib24), [25](https://arxiv.org/html/2510.21165v1#bib.bib25), [26](https://arxiv.org/html/2510.21165v1#bib.bib26), [27](https://arxiv.org/html/2510.21165v1#bib.bib27)]
Therefore,
the purpose of this study is to introduce both the negative-tail and positive-tail local Gaussian correlation networks (LGCNETs)
by measuring the local Gaussian correlations among tail regions of stock returns in the Chinese stock market.
This study also aims to compare the LGCNETs with the conventional Pearson correlation networks studied previously.

The remainder of this paper is organized as follows.
Section [2](https://arxiv.org/html/2510.21165v1#S2 "2 Data ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") gives the information on the dataset used in this analysis.
Section [3](https://arxiv.org/html/2510.21165v1#S3 "3 Local Gaussian correlation and network construction ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") briefly introduces the local Gaussian correlation measure and the methodology for constructing LGCNETs among return tails.
Section [4](https://arxiv.org/html/2510.21165v1#S4 "4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") briefly introduces the network metrics analyzed in this study.
Section [5](https://arxiv.org/html/2510.21165v1#S5 "5 Empirical results and discussion ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") presents the empirical results and discussion.
Section [6](https://arxiv.org/html/2510.21165v1#S6 "6 Conclusions ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") concludes this paper.

## 2 Data

This study analyzes the daily closing prices of all stocks traded on the main board of the Shanghai Stock Exchange (SSE) over the period from April 7, 2004 to December 31, 2019.
The dataset comprises 1542 stocks with 3639462 closing price records, sourced from Eastmoney’s official website (<https://quote.eastmoney.com>).
Based on fluctuations in the Shanghai Securities Composite Index (SSCI), which is a benchmark reflecting the overall performance of the Chinese stock market,
this study divides the period into ten periods as shown by Fig. [1](https://arxiv.org/html/2510.21165v1#S2.F1 "Figure 1 ‣ 2 Data ‣ The local Gaussian correlation networks among return tails in the Chinese stock market").
The detailed information of each period is listed in Table [1](https://arxiv.org/html/2510.21165v1#S2.T1 "Table 1 ‣ 2 Data ‣ The local Gaussian correlation networks among return tails in the Chinese stock market").
The stocks with missing logarithmic returns on more than 30 trading days are removed from the datasets in each period.

As shown in Fig. [1](https://arxiv.org/html/2510.21165v1#S2.F1 "Figure 1 ‣ 2 Data ‣ The local Gaussian correlation networks among return tails in the Chinese stock market"),
the study period covers the two most significant crashes in the Chinese stock market in this century: the 2007-2008 global financial crisis and the 2015-2016 domestic stock market turbulence.
It is a common statement that such extreme market events strengthen the correlations among return tails.[[23](https://arxiv.org/html/2510.21165v1#bib.bib23)]
These two crashes provide a unique opportunity to examine how international and domestic financial crises influence the structural dynamics of LGCNETs analyzed in this study.

![Refer to caption](x1.png)

Figure 1: SSCI performance over the period from April 7, 2004 to December 31, 2019.
Based on SSCI fluctuations, the period is segmented into ten periods as colored regions indicate.
Red and green regions represent bear and bull markets, respectively.




Table 1: Information of ten periods.
For each period, detailed information is provided: starting date, ending date, the percentage change of SSCI, number of stocks available to construct the network, and number of trading days.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Period | Starting date | Ending date | Percentage change | Number of stocks | Number of trading days |
| 1 | 20040407 | 20050606 | -44% | 769 | 281 |
| 2 | 20050607 | 20071016 | 514% | 224 | 574 |
| 3 | 20071017 | 20081028 | -73% | 740 | 253 |
| 4 | 20081029 | 20090804 | 109% | 812 | 189 |
| 5 | 20090805 | 20130625 | -47% | 633 | 940 |
| 6 | 20130626 | 20150612 | 180% | 653 | 481 |
| 7 | 20150613 | 20160127 | -49% | 850 | 154 |
| 8 | 20160128 | 20180129 | 36% | 796 | 490 |
| 9 | 20180130 | 20190104 | -32% | 1273 | 226 |
| 10 | 20190105 | 20191231 | 25% | 1446 | 241 |

## 3 Local Gaussian correlation and network construction

The local Gaussian correlation proposed by Tjø\o stheim et. al. is a new measure of statistical dependence between variables.[[23](https://arxiv.org/html/2510.21165v1#bib.bib23), [21](https://arxiv.org/html/2510.21165v1#bib.bib21)]
This new measure effectively captures nonlinear local correlation and is suitable for heavy-tailed variables.[[23](https://arxiv.org/html/2510.21165v1#bib.bib23), [21](https://arxiv.org/html/2510.21165v1#bib.bib21)]
The key idea of this measurement is that
the Gaussian bivariate density approximates locally the empiriccal bivariate density ff for two varibales (X1,X2)\left(X\_{1},X\_{2}\right) in neighborhood of each point x=(x1,x2)x=\left(x\_{1},x\_{2}\right).
The Gaussian bivariate density ψ\psi is defined by Eq. ([1](https://arxiv.org/html/2510.21165v1#S3.E1 "In 3 Local Gaussian correlation and network construction ‣ The local Gaussian correlation networks among return tails in the Chinese stock market")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(x)=12​π​σ1​(x)​σ2​(x)​1−ρ2​(x)​e−12​[1−ρ2​(x)]​{[v1−μ1​(x)σ1​(x)]2+[v2−μ2​(x)σ2​(x)]2−2​ρ​(x)​[v1−μ1​(x)σ1​(x)]​[v2−μ2​(x)σ2​(x)]}\displaystyle\psi\left(x\right)=\frac{1}{2\pi\sigma\_{1}\left(x\right)\sigma\_{2}\left(x\right)\sqrt{1-\rho^{2}\left(x\right)}}e^{-\frac{1}{2\left[1-\rho^{2}\left(x\right)\right]}\left\{\left[\frac{v\_{1}-\mu\_{1}\left(x\right)}{\sigma\_{1}\left(x\right)}\right]^{2}+\left[\frac{v\_{2}-\mu\_{2}\left(x\right)}{\sigma\_{2}\left(x\right)}\right]^{2}-2\rho\left(x\right)\left[\frac{v\_{1}-\mu\_{1}\left(x\right)}{\sigma\_{1}\left(x\right)}\right]\left[\frac{v\_{2}-\mu\_{2}\left(x\right)}{\sigma\_{2}\left(x\right)}\right]\right\}} |  | (1) |

where viv\_{i}, μi​(x)\mu\_{i}\left(x\right), and σi​(x)\sigma\_{i}\left(x\right) (i=1,2)\left(i=1,2\right) are the running variables in the Gaussian distribution,
the local means, and the local standard deviations, respectively.
The ρ​(x)\rho\left(x\right) is the local Gaussian correlation coefficient at the point x=(x1,x2)x=\left(x\_{1},x\_{2}\right),
which is what we need to estimate here.

The theory for estimating ρ​(x)\rho\left(x\right) has been detailed in Ref. [23](https://arxiv.org/html/2510.21165v1#bib.bib23).
The routines for estimating ρ​(x)\rho\left(x\right) have been implemented in the R package localgauss.[[28](https://arxiv.org/html/2510.21165v1#bib.bib28)]
This study uses the localgauss package and the plug-in bandwidth b=1.75​σ​n−16b=1.75\sigma n^{-\frac{1}{6}}
(σ\sigma and nn refer to the standard deviation and the number of observations for a variable, respectively)[[29](https://arxiv.org/html/2510.21165v1#bib.bib29)] to estimate the local Gaussian correlation coefficient ρ​(x)\rho\left(x\right).
This paper also conducts a robustness analysis involving slight variations in bandwidth.
The robustness analysis demonstrates that the findings presented in this paper are robust to changes in bandwidth.

In finance, the correlation between financial asset return tails is of special interest because these tails contain extreme market risks.
By quantifying the local Gaussian correlations among tail regions of the stock returns in the Chinese stock market,
this study constructs LGCNETs both among negative tails and among positive tails.
For each pair of stocks in a period introduced in the previous section,
this study first measures the diagonal local Gaussian correlation,
and then calculates the mean values on the diagonal in the negative tail from quantile 5% to 20% and in the positive tail from quantile 80% to 95%, respectively.
These two mean values are used as the link weights for negative-tail LGCNET and positive-tail LGCNET, respectively.

Based on the link weights mentioned above,
this study employs the Minimum/Maximum Spanning Tree (MST),[[9](https://arxiv.org/html/2510.21165v1#bib.bib9)]
the Planar Maximally Filtered Graph (PMFG),[[10](https://arxiv.org/html/2510.21165v1#bib.bib10)]
and the Triangulated Maximally Filtered Graph (TMFG)[[11](https://arxiv.org/html/2510.21165v1#bib.bib11)] methods
to extract the most important links of LGCNETs.
For correlation-based networks,
the minimum Spanning Tree (Minimum distance between nodes) and Maximum Spanning Tree (Maximum weight of links) generate the same MST network
because a larger link weight means a smaller distance between nodes linked by that link.
These filtering methods are widely used in constructing correlation networks.[[30](https://arxiv.org/html/2510.21165v1#bib.bib30)]
Their technical details can be found in Refs. [9](https://arxiv.org/html/2510.21165v1#bib.bib9), [10](https://arxiv.org/html/2510.21165v1#bib.bib10), [11](https://arxiv.org/html/2510.21165v1#bib.bib11).

To compare with previous studies,
the study also constructs conventional Pearson correlation networks in each period using MST, PMFG, and TMFG filtering methodologies.

## 4 Network metrics

This study analyzes the evolution characteristics of the fundamental metrics of negative-tail LGCNETs, positive-tail LGCNETs, and the Pearson correlation networks under MST, PMFG, and TMFG filtering methodologies.
These metrics include node strength centrality, node eigenvector centrality, average shortest path length, and network entropy (Shannon entropy, Rényi entropy, and Tsallis entropy).

Node centrality quantifies the importance of nodes within a network.
Among various centrality measures available,
this study selects strength centrality and eigenvector centrality for analysis based on their distinct characteristics in capturing different dimensions of node influence.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [31](https://arxiv.org/html/2510.21165v1#bib.bib31), [32](https://arxiv.org/html/2510.21165v1#bib.bib32)]
In correlation-based financial networks,
both strength centrality and eigenvector centrality play crucial roles in risk management, portfolio optimization, and asset price prediction, among others.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [33](https://arxiv.org/html/2510.21165v1#bib.bib33), [34](https://arxiv.org/html/2510.21165v1#bib.bib34)]
Their distributions are also key to understanding the error and attack tolerance of complex financial systems.[[35](https://arxiv.org/html/2510.21165v1#bib.bib35)]

For a correlation-based financial network with NN nodes and weight matrix WW,
the strength centrality sis\_{i} of node ii is defined as Eq. [2](https://arxiv.org/html/2510.21165v1#S4.E2 "In 4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market"),
and the eigenvector centrality viv\_{i} is the iith component of the leading eigenvector vv of weight matrix WW.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [31](https://arxiv.org/html/2510.21165v1#bib.bib31), [32](https://arxiv.org/html/2510.21165v1#bib.bib32)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | si=∑j=1Nwi​j\displaystyle s\_{i}=\sum\limits\_{j=1}^{N}w\_{ij} |  | (2) |

The average shortest path length is a metric that quantifies the typical separation between two nodes in a network, and it is crucial for understanding risk propagation in complex financial systems.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [12](https://arxiv.org/html/2510.21165v1#bib.bib12)]
For a correlation-based financial network with NN nodes and weight matrix WW,
the average shortest path length ⟨L⟩\left<L\right> is defined as Eq. [3](https://arxiv.org/html/2510.21165v1#S4.E3 "In 4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market").[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [12](https://arxiv.org/html/2510.21165v1#bib.bib12)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨L⟩=1N​(N−1)​∑i≠jNli​j\displaystyle\left<L\right>=\frac{1}{N\left(N-1\right)}\sum\limits\_{i\neq j}^{N}l\_{ij} |  | (3) |

where li​jl\_{ij} is the shortest path length between node ii and node jj.
The shortest path is the path that minimizes the total edge distance,
where the distance di​jd\_{ij} between node ii and node jj is defined as di​j=2​(1−wi​j)d\_{ij}=\sqrt{2\left(1-w\_{ij}\right)}.

Network entropy serves as a fundamental metric frequently employed in quantifying financial network resilience,
utilizing methodologies derived from statistical mechanics and ergodic theory.[[12](https://arxiv.org/html/2510.21165v1#bib.bib12)]
For a correlation-based financial network with NN nodes and weight matrix WW,
the Shannon entropy HSi, Rényi entropy HRi, and Tsallis entropy HTi of node ii are defined as Eq. [4](https://arxiv.org/html/2510.21165v1#S4.E4 "In 4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market"), Eq. [5](https://arxiv.org/html/2510.21165v1#S4.E5 "In 4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market"), and Eq. [6](https://arxiv.org/html/2510.21165v1#S4.E6 "In 4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market"), respectively.[[12](https://arxiv.org/html/2510.21165v1#bib.bib12), [20](https://arxiv.org/html/2510.21165v1#bib.bib20), [36](https://arxiv.org/html/2510.21165v1#bib.bib36)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | HSi=−∑j=1Npi​j​log⁡pi​j\displaystyle\text{HS}\_{i}=-\sum\limits\_{j=1}^{N}p\_{ij}\log p\_{ij} |  | (4) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | HRi=11−β​log⁡(∑j=1Npi​jβ)\displaystyle\text{HR}\_{i}=\frac{1}{1-\beta}\log\left(\sum\limits\_{j=1}^{N}p\_{ij}^{\beta}\right) |  | (5) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | HTi=1β−1​log⁡(1−∑j=1Npi​jβ)\displaystyle\text{HT}\_{i}=\frac{1}{\beta-1}\log\left(1-\sum\limits\_{j=1}^{N}p\_{ij}^{\beta}\right) |  | (6) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​j=wi​j∑j=1Nwi​j\displaystyle p\_{ij}=\frac{w\_{ij}}{\sum\limits\_{j=1}^{N}w\_{ij}} |  | (7) |

where pi​jp\_{ij} is the element of transition probability matrix PP, and is defined as Eq. [7](https://arxiv.org/html/2510.21165v1#S4.E7 "In 4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market").
β\beta is an adjustable parameter.
In this study, the results are reported with β\beta equal to 0.1.
This study also varies β\beta in the interval (0, 1) to see how the results change.
Such analysis illustrates that the findings of this paper are robust to parameter β\beta.

Based on the node entropy defined above,
the Shannon entropy HS, Rényi entropy HR, and Tsallis entropy HT of a network
are defined as Eq. [8](https://arxiv.org/html/2510.21165v1#S4.E8 "In 4 Network metrics ‣ The local Gaussian correlation networks among return tails in the Chinese stock market").[[12](https://arxiv.org/html/2510.21165v1#bib.bib12), [20](https://arxiv.org/html/2510.21165v1#bib.bib20), [36](https://arxiv.org/html/2510.21165v1#bib.bib36)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | HS=∑i=1Nπi​HSi,HR=∑i=1Nπi​HRi,HT=∑i=1Nπi​HTi\displaystyle\text{HS}=\sum\limits\_{i=1}^{N}\pi\_{i}\text{HS}\_{i},\,\,\,\,\text{HR}=\sum\limits\_{i=1}^{N}\pi\_{i}\text{HR}\_{i},\,\,\,\,\text{HT}=\sum\limits\_{i=1}^{N}\pi\_{i}\text{HT}\_{i} |  | (8) |

where πi\pi\_{i} is the iith component of the stationary distribution π\pi of the corresponding transition probability matrix PP, which satisfies π=π​P\pi=\pi P.

## 5 Empirical results and discussion

The correlation coefficients calculated to construct networks
are directly related to the network properties.
Therefore, this paper first investigates the distributions of both the local Gaussian correlations (both among negative tails and among positive tails) and Pearson correlation coefficients.
As shown in Fig. [2](https://arxiv.org/html/2510.21165v1#S5.F2 "Figure 2 ‣ 5 Empirical results and discussion ‣ The local Gaussian correlation networks among return tails in the Chinese stock market"), which compares these distributions via boxplots, almost all coefficients are positive.
During both bull and bear periods,
the local Gaussian correlation coefficients among negative tails are statistically larger than those among positive tails.
The relatively large correlation coefficients make us pay more attention to the correlations among negative tails.
During the periods of both the 2007-2008 global financial crisis and the 2015-2016 Chinese stock market turbulence,
the market’s rapid decline has significantly increased the correlation coefficients.
Compared with the global financial crisis, the domestic crash has a more significant impact on the correlations.
Notably,
Pearson’s ρ\rho shows that its distributions are different from the local Gaussian correlation coefficient distributions.
This difference indicates the necessity of studying the LGCNET.

![Refer to caption](x2.png)

Figure 2: Boxplots of correlation coefficients across ten periods.
Green boxes, violet boxes, and gray boxes indicate local Gaussian correlation coefficients among negative tails, local Gaussian correlation coefficients among positive tails, and conventional Pearson correlation coefficients.

Strength centrality and eigenvector centrality are critical metrics for assessing node importance in weighted financial correlation-based networks.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [31](https://arxiv.org/html/2510.21165v1#bib.bib31), [32](https://arxiv.org/html/2510.21165v1#bib.bib32)]
This study conducts a comparative analysis of stock rankings generated by these centrality measures
across three network types: negative-tail LGCNET, positive-tail LGCNET, and conventional Pearson correlation network.
Fig. [3](https://arxiv.org/html/2510.21165v1#S5.F3 "Figure 3 ‣ 5 Empirical results and discussion ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") presents the pairwise overlap of top-ten stocks among filtered variants of the three network types during the last period.
This figure illustrates two key patterns:
(1) the top-ten stocks are highly similar among filtered networks of the same type,
whereas (2) the top-ten stocks are different among the three network types.
This work also examines the comparative results in the remaining nine periods,
showing that the top-ten stocks among these three network types remain distinct in each period.
The findings of this comparative study further demonstrate the necessity of prioritizing LGCNET in analyses.

![Refer to caption](x3.png)

  


Figure 3: Pairwise overlap of top-ten stocks in filtered correlation networks during the last period.
The left and right panels depict strength and eigenvector centrality rankings, respectively.
See main text for details.

The node centrality distribution is directly related to the resilience of complex financial networks.[[35](https://arxiv.org/html/2510.21165v1#bib.bib35)]
Prior research has demonstrated that both degree and strength distributions in financial networks
follow heavy-tailed patterns—a defining topological characteristic critical for understanding the error and attack tolerance of these systems.
Therefore,
by estimating the tail shape parameters of both strength and eigenvector centrality distributions using the Generalized Pareto Distribution (GPD),[[37](https://arxiv.org/html/2510.21165v1#bib.bib37), [38](https://arxiv.org/html/2510.21165v1#bib.bib38), [39](https://arxiv.org/html/2510.21165v1#bib.bib39), [40](https://arxiv.org/html/2510.21165v1#bib.bib40)]
this study examines whether the LGCNETs analyzed here exhibit scale-free properties in terms of strength centrality and eigenvector centrality.

The GPD estimations are shown in Fig. [4](https://arxiv.org/html/2510.21165v1#S5.F4 "Figure 4 ‣ 5 Empirical results and discussion ‣ The local Gaussian correlation networks among return tails in the Chinese stock market").
From this figure, we see that all shape parameters for LGCNETs and Pearson correlation networks are positive.
A positive tail shape parameter indicates a heavy-tailed distribution.
This means that all networks analyzed here are scale-free in terms of both strength centrality and eigenvector centrality.
The figure further demonstrates statistically indistinguishable tail shape parameters across the three network types
under both PMFG and TMFG filtering methodologies.
For the MST filtering methodology, however,
the tail shape parameters of the three network types are statistically different.

![Refer to caption](x4.png)

  


Figure 4: Tail shape parameters of network centrality distributions in ten periods.
The first and second rows are for strength and eigenvector centralities, respectively.
The first, second, and third columns are for MST, PMFG, and TMFG filtering methodologies, respectively.
Red, green, and black data markers are for negative-tail LGCNETs, positive-tail LGCNETs, and Pearson correlation networks, respectively.
Vertical error bars are 95% confidence intervals.
These panels share common legends.

Average shortest path length ⟨L⟩\left<L\right> quantifies the typical distance between two nodes in a complex network.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [12](https://arxiv.org/html/2510.21165v1#bib.bib12)]
This observation can reflect the ability of risk propagation in a financial network.[[8](https://arxiv.org/html/2510.21165v1#bib.bib8), [12](https://arxiv.org/html/2510.21165v1#bib.bib12)]
Fig. [5](https://arxiv.org/html/2510.21165v1#S5.F5 "Figure 5 ‣ 5 Empirical results and discussion ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") presents this measurement for the LGCNETs and Pearson correlation networks across ten periods.
It shows that the ⟨L⟩\left<L\right> values of each network type under three filtering methodologies exhibit similar temporal changing trends.
Compared with the positive-tail LGCNETs and the Pearson correlation networks, the ⟨L⟩\left<L\right> values for the negative-tail LGCNETs are smaller in almost all periods.
The extreme decline events during short periods,
i.e., the 2007–2008 global financial crisis and the 2015–2016 Chinese stock market turbulence,
have significantly decreased the ⟨L⟩\left<L\right>.
Notably, the domestic market crash made the ⟨L⟩\left<L\right> the smallest.
Such findings are in agreement with the results presented in Fig. [1](https://arxiv.org/html/2510.21165v1#S2.F1 "Figure 1 ‣ 2 Data ‣ The local Gaussian correlation networks among return tails in the Chinese stock market").
For all three filtering methodologies, the ⟨L⟩\left<L\right> values of Pearson correlation networks and the negative-tail LGCNETs have a similar changing trend.
However, their values are different.
If we use Pearson correlation networks to estimate the ability of risk propagation in financial complex systems,
the ability will be underestimated.
The findings stated above illustrate that
the negative-tail LGCNETs have a stronger ability in risk propagation and we should pay more attention to them.

![Refer to caption](x5.png)

Figure 5: Network’s average shortest path length across ten periods.
The left, middle, and right panels are for MST, PMFG, and TMFG filtering methodologies, respectively.
Red, green, and black data markers are for negative-tail LGCNETs, positive-tail LGCNETs, and Pearson correlation networks, respectively.
Violet vertical bands indicate the periods of the 2007-2008 global financial crisis and the 2015-2016 Chinese stock market turbulence.
These panels share common legends.

Network entropy is related to network resilience.[[12](https://arxiv.org/html/2510.21165v1#bib.bib12), [20](https://arxiv.org/html/2510.21165v1#bib.bib20), [36](https://arxiv.org/html/2510.21165v1#bib.bib36)]
Higher network entropy generally correlates with enhanced network resilience.
This study systematically analyzes the Shannon entropy, Rényi entropy, and Tsallis entropy of negative-tail LGCNETs, positive-tail LGCNETs, and conventional Pearson correlation networks.
Fig. [6](https://arxiv.org/html/2510.21165v1#S5.F6 "Figure 6 ‣ 5 Empirical results and discussion ‣ The local Gaussian correlation networks among return tails in the Chinese stock market") shows the three entropy measurements of these three network types under MST, PMFG, and TMFG filtering methodologies across ten periods.
Under each filtering methodology,
we see from this figure that the Shannon entropy, Rényi entropy, and Tsallis entropy of negative-tail LGCNETs are all smaller than the corresponding entropies of positive-tail LGCNETs in almost all periods.
This demonstrates that the resilience of negative-tail LGCNETs is worse than that of positive-tail LGCNETs.
Therefore, we should pay more attention to the negative-tail LGCNETs.
The 2007–2008 global financial crisis had no significant impact on the entropy of both negative-tail and positive-tail LGCNETs.
However, the 2015–2016 Chinese stock market turbulence had a significant impact on the entropy of negative-tail LGCNETs.
The domestic market crash significantly decreased the entropy of negative-tail LGCNETs,
and thus dramatically changed the resilience of negative-tail LGCNETs.
Notably,
The smallest entropy for the negative-tail LGCNETs appears in period seven and for the Pearson correlation networks appears in period eight.
This demonstrates that Pearson correlation networks cannot capture the risks of stock market crashes.

![Refer to caption](x6.png)

Figure 6: Network’s entropy across ten periods.
The first, second, and third rows show Shannon entropy, Rényi entropy, and Tsallis entropy, respectively.
The first, second, and third columns are for MST, PMFG, and TMFG filtering methodologies, respectively.
Red, green, and black data markers are for negative-tail LGCNETs, positive-tail LGCNETs, and Pearson correlation networks, respectively.
Violet vertical bands indicate the periods of the 2007-2008 global financial crisis and the 2015-2016 Chinese stock market turbulence.
These panels share common legends.

## 6 Conclusions

The correlation-based financial networks have been intensively studied.
Previous studies used to construct networks based on the Pearson correlation coefficient.
These studies may have led to misleading and catastrophic results because of several critical shortcomings of the Pearson correlation coefficient.
Compared with the Pearson correlation coefficient,
the Local Gaussian correlation coefficient, a new measurement of statistical dependence between variables,
has some new features that can capture local nonlinear correlation and are suitable for heavy-tailed variables.

In finance,
it is of particular interest to look at the local correlations among return tails of financial assets.
Therefore,
this study constructs both negative-tail and positive-tail LGCNETs using the local Gaussian correlation coefficients among tail regions of stock returns in the SSE.
For ease of comparison,
this paper also constructs the networks based on Pearson correlation coefficients.
The time of stock data analyzed in this paper covers the 2007-2008 global financial crisis and the 2015-2016 Chinese stock market turbulence,
which allows us to investigate the effects of the international and domestic market crashes.

This paper compares negative-tail LGCNET, positive-tail LGCNET, and Pearson correlation networks regarding
the tail shape parameters of both strength centrality and eigenvector centrality distributions,
the average shortest path length,
the Shannon entropy, the Rényi entropy, and the Tsallis entropy.
Compared with the positive-tail LGCNET and Pearson correlation network,
these measurements suggest that the negative-tail LGCNET better reflects the stock market risks.
Compared with the 2007-2008 global financial crisis,
the 2015-2016 Chinese stock market turbulence had a stronger impact on the negative-tail LGCNET.
Therefore, we must pay more attention to the negative-tail LGCNET and the domestic crash.

The correlation-based network approach has been applied in various financial markets and has obtained some insightful results.
Future work should reevaluate existing findings using the local Gaussian correlation method.

## Acknowledgements

This work was supported by the Humanities and Social Sciences Youth Foundation of the Ministry of Education of China [grant number 22YJCZH107];
the Shaanxi Science and Technology Department, P.R. China [grant number 2023-JC-QN-0093].
The author would like to thank the reviewers for their valuable comments which make this paper better.

## Declaration of competing interest

The author declares no competing interests.

## Data availability

The data are publicly available on the Eastmoney website (<https://quote.eastmoney.com>) or from the corresponding author upon reasonable request.

## References

* [1]

  A.-L. Barabási, N. Gulbahce and J. Loscalzo, Nature Reviews Genetics
  12, 56 (2011).
* [2]

  S. Pilosof, M. A. Porter, M. Pascual and S. Kéfi, Nature Ecology &
  Evolution 1, p. 0101 (2017).
* [3]

  C. Y.-H. Chen, W. K. Härdle and Y. Okhrin, Journal of Econometrics 208, 282 (2019).
* [4]

  T. Qing, F. Wang, Q. Li, G. Dong, L. Tian and S. Havlin, Communications
  Physics 7, p. 372 (2024).
* [5]

  R. Du, N. Zhang, M. Zhang, Z. Kong et al., Applied Energy 368, p. 123353 (2024).
* [6]

  G. Dong, F. Wang, L. M. Shekhtman, M. M. Danziger et al., PNAS 118, p. e1922831118 (2021).
* [7]

  M. Bardoscia, P. Barucca, S. Battiston, F. Caccioli et al., Nature
  Reviews Physics 3, 490 (2021).
* [8]

  P. Liu, EPL 149, p. 11002 (2025).
* [9]

  R. N. Mantegna, The European Physical Journal B 11, 193 (1999).
* [10]

  M. Tumminello, T. Aste, T. D. Matteo and R. N. Mantegna, PNAS 102,
  10421 (2005).
* [11]

  T. A. Guido Previde Massara, T. Di Matteo, Journal of Complex Networks
  5, 161 (2017).
* [12]

  T. Peron, L. Costa and F. A. Rodrigues, Chaos 22, p. 013117
  (2012).
* [13]

  I. Vodenska, A. P. Becker, D. Zhou, D. Y. Kenett, H. E. Stanley and S. Havlin,
  Risks 4, p. 13 (2016).
* [14]

  L. Zhao, G.-J. Wang, M. Wang, W. Bao, W. Li and H. E. Stanley, Physica A
  506, 1104 (2018).
* [15]

  L. Xia, D. You, X. Jiang and Q. Guo, Physica A 490, 222 (2018).
* [16]

  Q. Nguyen, N. K. Nguyen and L. N. Nguyen, Physica A 514, 235
  (2019).
* [17]

  J. Ardalankia, J. Askari, S. Sheykhali, E. Haven and G. R. Jafari, EPL
  132, p. 58002 (2020).
* [18]

  M. K. So, A. M. Chu and T. W. Chan, Finance Research Letters 38, p.
  101864 (2021).
* [19]

  C. Huang, X. Zhao, R. Su, X. Yang and X. Yang, International Journal of
  Finance & Economics 27, 1962 (2022).
* [20]

  W. Liu, Q. Ma and X. Liu, Finance Research Letters 45, p. 102138
  (2022).
* [21]

  D. Tjøstheim, H. Otneim and B. Støve, Statistical Science 37, 90
  (2022).
* [22]

  P. Liu and Y. Zheng, Entropy 25, p. 36 (2023).
* [23]

  D. Tjøstheim and K. O. Hufthammer, Journal of Econometrics 172, 33
  (2013).
* [24]

  B. Støve, D. Tjøstheim and K. O. Hufthammer, Journal of Empirical
  Finance 25, 62 (2014).
* [25]

  Q. N. Nguyen, S. Aboura, J. Chevallier, L. Zhang and B. Zhu, European
  Journal of Operational Research 285, 306 (2020).
* [26]

  C. Eom, T. Kaizoji, G. Livan and E. Scalas, The North American Journal of
  Economics and Finance 56, p. 101358 (2021).
* [27]

  J. Liu, Journal of Financial Econometrics 21, 959 (2023).
* [28]

  G. D. Berentsen, T. S. Kleppe and D. B. Tjø\o stheim, Journal of
  Statistical Software 56, 1 (2014).
* [29]

  H. Otneim, The R Journal 13, 38 (2021).
* [30]

  H. Esmalifalak and A. Moradi-Motlagh, Journal of Economic Surveys , 1
  (2024).
* [31]

  T. Opsahl, F. Agneessens and J. Skvoretz, Social Networks 32, 245
  (2010).
* [32]

  M. E. J. Newman, Physical Review E 70, p. 056131 (2004).
* [33]

  G.-J. Wang, H. Huai, Y. Zhu, C. Xie and G. S. Uddin, Journal of Management
  Science and Engineering 9, 348 (2024).
* [34]

  Y. Xu and X. Zhao, The North American Journal of Economics and Finance
  73, p. 102163 (2024).
* [35]

  R. Albert, H. Jeong and A.-L. Barabási, Nature 406, 378 (2000).
* [36]

  Z. Pan, Q. Ma, J. Ding and L. Wang, The European Physical Journal B 94, p. 56 (2021).
* [37]

  M. N. Conte and D. L. Kelly, Journal of Environmental Economics and
  Management 92, 677 (2018).
* [38]

  P. Embrechts, C. Klüppelberg and T. Mikosch, Modelling Extremal Events
  for Insurance and Finance (Springer, New York, 1997).
* [39]

  S. Kotz and S. Nadarajah, Extreme Value Distributions: Theory and
  Applications (Imperial College Press, London, 2000).
* [40]

  P. Liu and Y. Zheng, Plos One 18, p. e0294445 (2023).