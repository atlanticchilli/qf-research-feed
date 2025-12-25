---
authors:
- Suparna Biswas
- Rituparna Sen
doc_id: arxiv:2512.21092v1
family_id: arxiv:2512.21092
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK
  AND CARBON FOOTPRINT
url_abs: http://arxiv.org/abs/2512.21092v1
url_html: https://arxiv.org/html/2512.21092v1
venue: arXiv q-fin
version: 1
year: 2025
---


\nameSuparna Biswas and Rituparna Sen
CONTACT Suparna Biswas. Email: suparnabsws4@gmail.com

###### Abstract

Historically, financial risk management has mostly addressed risk factors that arise from the financial environment. Climate risks present a novel and significant challenge for companies and financial markets. Investors aiming for avoidance of firms with high carbon footprints require suitable risk measures and portfolio management strategies. This paper presents the construction of decarbonized indices for tracking the S & P-500 index of the U.S. stock market, as well as the Indian index NIFTY-50, employing two distinct methodologies and study their performances. These decarbonized indices optimize the portfolio weights by minimizing the mean-VaR and mean-ES and seek to reduce the risk of significant financial losses while still pursuing decarbonization goals. Investors can thereby find a balance between financial performance and environmental responsibilities. Ensuring transparency in the development of these indices will encourage the excluded and under-weighted asset companies to lower their carbon footprints through appropriate action plans. For long-term passive investors, these indices may present a more favourable option than green stocks.

###### keywords:

Climate risk; Decarbonized indices; Risk measures; Portfolio optimization

## 1 Introduction

In the past, financial risk management has mostly dealt with risks that come from the financial world. Nevertheless, non-financial sources of risk have arisen as crucial determinants for the functioning of enterprises and organizations. Climate risks have garnered considerable attention from policymakers, institutions, and investors worldwide. This is due to the growing recognition of the potentially dire consequences of climate change for the financial system, as well as the integration of these risks into decision-making processes (see TCF [[2022](https://arxiv.org/html/2512.21092v1#bib.bib1)]). Climate risks, encompassing both transition and physical risks, present a novel and significant challenge for companies and financial markets (see Breitenstein et al. [[2022](https://arxiv.org/html/2512.21092v1#bib.bib5)]). Extreme weather events like floods and heat waves, as well as changes in climatic patterns like droughts and rising sea levels, are examples of physical risks brought on by climate change that can directly harm organizations and assets. Transition risk refers to the potential financial losses that can arise from the shift towards a low-carbon economy, driven by factors like policy changes, technological advancements, and evolving consumer preferences. Integrating these risks into forecasting and planning processes introduces new complexities (see Capelli et al. [[2023](https://arxiv.org/html/2512.21092v1#bib.bib8)]). Also, climate concerns are not limited to the financial sector and are global in nature. Anecdotal evidence suggests that there is a strong market demand for climate management (see Clark [[2023](https://arxiv.org/html/2512.21092v1#bib.bib9)]). In the past few years, European financial authorities have pushed for investment companies to better include environmental, social, and governance (ESG) risks in their risk management and governance frameworks ((2021) [[EBA](https://arxiv.org/html/2512.21092v1#bib.bib11)]). Certain researchers propose that to mitigate environmental impacts, consumption patterns must transition towards cleaner products Schandl et al. [[2016](https://arxiv.org/html/2512.21092v1#bib.bib22)], while others argue that environmental degradation is inextricably linked to economic growth, necessitating substantial transformations in economies to render degrowth viable Kallis [[2011](https://arxiv.org/html/2512.21092v1#bib.bib13)]. Both perspectives indicate that financial systems must undergo significant adjustments to align with the new paradigm, necessitating that investors identify suitable strategies for sustainable investment to mitigate their risks while facilitating the economy’s transition from unsustainable production methods.

Investors and financial institutions must therefore engage in the global push to decarbonize economies. For investors to accurately assess which organizations to invest in, relevant indicators and measures must exist that reflect both the qualitative and quantitative effects of firms’ operations on the environment. When appropriate measures are implemented, investors necessitate strategies that can optimize their portfolios in order to mitigate the risk estimated by the risk measures. Markowitz Markowitz [[1952](https://arxiv.org/html/2512.21092v1#bib.bib17)] introduced the optimal portfolio choice theory in 1952, which is based on the risk of variance. Since then, the variance (mean variance) has become a classic and highly influential quantitative measure of financial risks. The computation of variance is straightforward and user-friendly, and the underlying theory has been extensively advanced. Nevertheless, it only takes into account the average deviation, failing to address the prevalent concern of the right tail of the returns. It is desirable for measures of risk to concentrate on the tail of
the distribution of returns, in other words, the extreme losses. Downside risk refers to the potential decrease in an asset’s value due to fluctuations in market conditions. The measures of downside risk, like value-at-risk (VaR) and expected shortfall (ES), are adopted as standard tools to measure the ex-ante financial risk of assets (BCBS, 1996 and Basel III). VaR quantifies the size of loss on a portfolio of assets over a given time horizon at a given probability. ES measures the weighted average of the “extreme” loss beyond the VaR cutoff point. The ES is a coherent risk measure, whereas VaR is not. The VaR method was developed to measure financial market risk in response to the financial disasters of the early 1990s and to address the demerits of VaR, ES was introduced by Artzner et al. [[1999](https://arxiv.org/html/2512.21092v1#bib.bib4)]. Capelli et al. [[2021](https://arxiv.org/html/2512.21092v1#bib.bib7)] saw ESG factors as one of the parts that are missing when VaR is used to measure financial risk.

This research presents methodologies for constructing two decarbonized indices from established benchmarks (see Lakshmi et al. [[2023](https://arxiv.org/html/2512.21092v1#bib.bib15)]), and demonstrates their effectiveness for the Indian and U.S. economies. We demonstrate that the resultant index substantially reduces overall carbon effect, serving as a safeguard against climate hazards. Our approach is based on VaR and ES. The relationship of VaR and ES to ESG has remained largely unexplored in portfolio optimization. In a pertinent work by [Andersson et al., [2016](https://arxiv.org/html/2512.21092v1#bib.bib3)], the presented decarbonized indices were derived from the benchmark by minimizing tracking error while adhering to appropriate limitations related to the carbon footprints of the constituent enterprises. [Mezali and Beasley, [2013](https://arxiv.org/html/2512.21092v1#bib.bib18)] earlier used quantile regression with a mixed-integer linear programming formulation. [Li et al., [2022](https://arxiv.org/html/2512.21092v1#bib.bib16)] developed a comprehensive methodology that optimizes ESG score while concurrently minimizing risk and maximizing revenue.

It is essential to recognize that the current sustainability-oriented indices in the Indian and U.S. stock markets, specifically the S & P BSE GREENEX, BSE Carbonex, NIFTY100 Enhanced ESG Index [Patel and Kumari, [2020](https://arxiv.org/html/2512.21092v1#bib.bib20), Nishad et al., [2021](https://arxiv.org/html/2512.21092v1#bib.bib19)], and S & P-500 Scored & Screened Index Sanchez [[2025, February 12](https://arxiv.org/html/2512.21092v1#bib.bib21)], emphasize monitoring the performance of companies based on their carbon emissions, ESG scores, and initiatives to mitigate climate risk, rather than concentrating on the performance of the parent index. They employ market capitalization for weighting, without attempting to imitate the performance of the excluded equities. To circumvent this, [Andersson et al., [2016](https://arxiv.org/html/2512.21092v1#bib.bib3), Lakshmi et al., [2023](https://arxiv.org/html/2512.21092v1#bib.bib15)] develop an optimized index by minimizing tracking error. To determine how closely a portfolio tracks its benchmark index, tracking error is a crucial tool. Tracking errors, however, don’t provide any indication of the DIs’ risk. Here, we develop an optimized index by minimizing the mean-VaR and mean-ES. It effectively captures lost contributions from dropped stocks by compensating with other highly correlated stocks that remain in the portfolio, while minimizing VaR and ES.

We state the definition and describe the methodology in Section 2. Section 3 provides the data description. The application of the methods on the Indian and the U.S. markets is illustrated in Section 4. We demonstrate how the index aims to establish a connection between theory and practice by using real-time data for both in-sample and out-of-sample computations. The paper ends with a detailed summary and discussion in Section 5.

## 2 Definition and Methodology

In this section we define VaR and ES. We then discuss the methodologies behind the construction of decarbonized indices and then optimize the portfolio weights by minimizing the mean-VaR and mean-ES.

### 2.1 Definitions

Let the random variable XX be the loss of some portfolio. Let FF be the distribution function of XX, then Qp​(X)=inf{x:F​(x)≥p}, 0<p<1Q\_{p}(X)=\inf\{x:F(x)\geq p\},\ 0<p<1 is the quantile function. For, 0<p<q<10<p<q<1, the two risk measures V​a​RpVaR\_{p} and E​SpES\_{p} are defined as

|  |  |  |
| --- | --- | --- |
|  | V​a​Rp=inf{x∈ℝ:F​(x)≥p}VaR\_{p}=\inf\{x\in\mathbb{R}:F(x)\geq p\} |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​Sp=11−p​∫p1V​a​Ru​𝑑u.ES\_{p}=\frac{1}{1-p}\int\_{p}^{1}VaR\_{u}du. |  | (1) |

### 2.2 Methodology

Let NN stocks be arranged from highest to lowest based on their carbon footprints. For the iith stock rir\_{i}, MiM\_{i}, and cic\_{i} denote the return, market capitalization, and carbon footprint, respectively. The portfolio return of the benchmark is Rb=(Wb)T​rR^{b}=(\textbf{W}^{b})^{T}\textbf{r}, where Wb=(Wib)1≤i≤N\textbf{W}^{b}=(W\_{i}^{b})\_{1\leq i\leq N} is the vector of portfolio weights taken to be proportional to the market capitalization,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wib=Mi∑i=1NMi,W\_{i}^{b}=\frac{M\_{i}}{\sum\_{i=1}^{N}M\_{i}}, |  | (2) |

and the bold letters denote the corresponding vector representation. Let Wd\textbf{W}^{d} be the vector of weights for the proposed decarbonized index and RdR^{d} is the corresponding return. We assume that the return rate r∼N​(μ,Σ)\textbf{r}\sim N(\mu,\Sigma), then

|  |  |  |
| --- | --- | --- |
|  | Rb∼N​((Wb)T​μ,(Wb)T​Σ​Wb)R^{b}\sim N((\textbf{W}^{b})^{T}\mu,(\textbf{W}^{b})^{T}\Sigma\textbf{W}^{b}) |  |

and

|  |  |  |
| --- | --- | --- |
|  | Rd∼N​((Wd)T​μ,(Wd)T​Σ​Wd).R^{d}\sim N((\textbf{W}^{d})^{T}\mu,(\textbf{W}^{d})^{T}\Sigma\textbf{W}^{d}). |  |

Our objective is to minimize the mean-VaR and mean-ES and then find

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Wd\displaystyle\textbf{W}^{d} | =\displaystyle= | arg​minW=(Wi)1≤i≤N⁡(V​a​Rp​(WT​r))\displaystyle\operatorname\*{arg\,min}\_{\textbf{W}=(W\_{i})\_{1\leq i\leq N}}(VaR\_{p}(\textbf{W}^{T}\textbf{r})) |  |
|  |  | =\displaystyle= | arg​minW=(Wi)1≤i≤N⁡(WT​μ+T​(p)​WT​Σ​W),\displaystyle\operatorname\*{arg\,min}\_{\textbf{W}=(W\_{i})\_{1\leq i\leq N}}(\textbf{W}^{T}\mu+T(p)\sqrt{\textbf{W}^{T}\Sigma\textbf{W}}), |  |

T​(p)T(p) is the ppth quantile of the standard normal distribution, and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Wd\displaystyle\textbf{W}^{d} | =\displaystyle= | arg​minW=(Wi)1≤i≤N⁡(E​Sp​(WT​r))\displaystyle\operatorname\*{arg\,min}\_{\textbf{W}=(W\_{i})\_{1\leq i\leq N}}(ES\_{p}(\textbf{W}^{T}\textbf{r})) |  |
|  |  | =\displaystyle= | arg​minW=(Wi)1≤i≤N⁡(WT​μ+T1​(p)​WT​Σ​W),\displaystyle\operatorname\*{arg\,min}\_{\textbf{W}=(W\_{i})\_{1\leq i\leq N}}(\textbf{W}^{T}\mu+T\_{1}(p)\sqrt{\textbf{W}^{T}\Sigma\textbf{W}}), |  |

T1​(p)=ϕ​(Φ−1​(p))1−pT\_{1}(p)=\frac{\phi(\Phi^{-1}(p))}{1-p}, where ϕ\phi is the probability density function of the standard normal distribution and Φ\Phi is the cumulative distribution function of the standard normal distribution.

In order to reduce the computations, we use a multi-factor model of aggregate risk to estimate VaR and ES. Next for S & P-500 index, we use the Fama and French [[2012](https://arxiv.org/html/2512.21092v1#bib.bib12)] five-factor model and for the Indian benchmark index Nifty-50, we use the Fama and French [[2012](https://arxiv.org/html/2512.21092v1#bib.bib12)] four-factor model, which allows us to decompose the return into a weighted sum of common factor returns and specific returns. If ri​tr\_{it} and rf​tr\_{ft} denote the return of the iith stock and the risk-free rate at time tt, then the five-factor model is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri​t−rf​t=βi​0+βi​1​(rm​t−rf​t)+βi​2​SMBt+βi​3​HMLt+βi​4​RMWt+βi​5​CMAt+ei​t,r\_{it}-r\_{ft}=\beta\_{i0}+\beta\_{i1}(r\_{mt}-r\_{ft})+\beta\_{i2}\mathrm{SMB}\_{t}+\beta\_{i3}\mathrm{HML}\_{t}+\beta\_{i4}\mathrm{RMW}\_{t}+\beta\_{i5}\mathrm{CMA}\_{t}+e\_{it}, |  | (5) |

and the four-factor model is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri​t−rf​t=βi​0+βi​1​SMBt+βi​2​HMLt+βi​3​WMLt+βi​4​MFt+ei​t,r\_{it}-r\_{ft}=\beta\_{i0}+\beta\_{i1}\mathrm{SMB}\_{t}+\beta\_{i2}\mathrm{HML}\_{t}+\beta\_{i3}\mathrm{WML}\_{t}+\beta\_{i4}\mathrm{MF}\_{t}+e\_{it}, |  | (6) |

where ei​te\_{it} is the error, βi​j\beta\_{ij} denotes the factor loading, and rm​t−rf​tr\_{mt}-r\_{ft} is the market risk premium; SMB\mathrm{SMB}, HML\mathrm{HML}, WML\mathrm{WML}, MF\mathrm{MF}, RMW\mathrm{RMW}, and CMA\mathrm{CMA}, indicate the size effect (small-minus-big), value effect (high-minus-low), momentum factor (winners-minus-losers), market factor, the return spread of the most profitable firms minus the least profitable, and the return spread of firms that invest conservatively minus aggressively. Let FjF\_{j} denote these factors with a dispersion matrix Ω\Omega. Also, let 𝜷\bm{\beta} be the matrix of loadings and Δ\Delta be the diagonal matrix of specific risk variances. Then, the dispersion of the excess returns is 𝜷​Ω​𝜷T+Δ\bm{\beta}\Omega\bm{\beta}^{T}+\Delta. Consequently, the volatility of any portfolio with returns rr and weights w is wT​(𝜷​Ω​𝜷T+Δ)​w\sqrt{\textbf{w}^{T}(\bm{\beta}\Omega\bm{\beta}^{T}+\Delta)\textbf{w}}. Now, equation [2.2](https://arxiv.org/html/2512.21092v1#S2.Ex4 "2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") and [2.2](https://arxiv.org/html/2512.21092v1#S2.Ex5 "2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") can be written as

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Wd\displaystyle\textbf{W}^{d} | =\displaystyle= | arg​minW=(Wi)1≤i≤N⁡(WT​μ+T​(p)​WT​(𝜷​Ω​𝜷T+Δ)​W),\displaystyle\operatorname\*{arg\,min}\_{\textbf{W}=(W\_{i})\_{1\leq i\leq N}}(\textbf{W}^{T}\mu+T(p)\sqrt{\textbf{W}^{T}(\bm{\beta}\Omega\bm{\beta}^{T}+\Delta)\textbf{W}}), |  | (7) |

and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Wd\displaystyle\textbf{W}^{d} | =\displaystyle= | arg​minW=(Wi)1≤i≤N⁡(WT​μ+T1​(p)​WT​(𝜷​Ω​𝜷T+Δ)​W),\displaystyle\operatorname\*{arg\,min}\_{\textbf{W}=(W\_{i})\_{1\leq i\leq N}}(\textbf{W}^{T}\mu+T\_{1}(p)\sqrt{\textbf{W}^{T}(\bm{\beta}\Omega\bm{\beta}^{T}+\Delta)\textbf{W}}), |  | (8) |

In order to achieve a balance between minimizing carbon footprints and maintaining diversity in composition, we utilize two separate methodologies to create decarbonized indices (DIs). These two methodologies have been taken from [Andersson et al., [2016](https://arxiv.org/html/2512.21092v1#bib.bib3), Lakshmi et al., [2023](https://arxiv.org/html/2512.21092v1#bib.bib15)]. Every methodology presents unique benefits and drawbacks, which are detailed below.

The first method involves reweighting the remaining stocks in order to reduce mean-VaR and mean-ES after excluding the kk worst performers in terms of carbon intensity. Here, the DI is constructed using weights WidW^{d}\_{i}, obtained by solving ([7](https://arxiv.org/html/2512.21092v1#S2.E7 "Equation 7 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) and ([8](https://arxiv.org/html/2512.21092v1#S2.E8 "Equation 8 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) subject to the constraints

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1NWid=1,withWid=0,for ​i=1,2,…,k,and​ 0≤Wid≤1,for ​i=k+1,…,N.\begin{split}&\sum\_{i=1}^{N}W\_{i}^{d}=1,\;\text{with}\\ &W\_{i}^{d}=0,\;\text{for }i=1,2,\ldots,k,\;\text{and}\;0\leq W\_{i}^{d}\leq 1,\;\text{for }i=k+1,\dots,N.\end{split} |  | (9) |

The minimization problem is addressed using the Trust-Region Constrained Algorithm (TRCA), which is effective for handling the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimize​f​(x), subject to ​c0l​b≤c0​(x)≤c0u​b,xl​b≤x≤xu​b.\text{minimize}\;f(x),\text{ subject to }c\_{0}^{lb}\leq c\_{0}(x)\leq c\_{0}^{ub},\;x^{lb}\leq x\leq x^{ub}. |  | (10) |

Multiple linear and nonlinear constraints can be accepted as inputs [Conn et al., [2000](https://arxiv.org/html/2512.21092v1#bib.bib10)]. The objective function is estimated using a quadratic model confined to the trust region centered on the initial estimate or the present location. The algorithm operates through a process of iterative refinement of the initial estimate [Kimiaei, [2022](https://arxiv.org/html/2512.21092v1#bib.bib14)]. We exclude the algorithm’s technicalities and direct the reader to Byrd et al. [[1987](https://arxiv.org/html/2512.21092v1#bib.bib6)] for additional information.

Our second methodology includes all stocks without specifically targeting those with high carbon footprints. The minimization problem outlined in ([7](https://arxiv.org/html/2512.21092v1#S2.E7 "Equation 7 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) and ([8](https://arxiv.org/html/2512.21092v1#S2.E8 "Equation 8 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) is addressed by establishing a threshold CC for the total footprint of the index. This method preserves the composition’s diversity while minimizing its footprint. Mathematically, we find the weights in ([7](https://arxiv.org/html/2512.21092v1#S2.E7 "Equation 7 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) and [8](https://arxiv.org/html/2512.21092v1#S2.E8 "Equation 8 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") considering

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1NWid=1,with∑i=1Nci​Wid≤C​and​ 0≤Wid≤1,for ​i=1,…,N.\begin{split}&\sum\_{i=1}^{N}W\_{i}^{d}=1,\;\text{with}\\ &\sum\_{i=1}^{N}c\_{i}W\_{i}^{d}\leq C\;\text{and}\;0\leq W\_{i}^{d}\leq 1,\;\text{for }i=1,\ldots,N.\end{split} |  | (11) |

We now implement the TRCA mentioned above. Hereafter, the first DI index is denoted as DI\_1 and the second index is denoted as DI\_2.

In this context, it is essential to conduct a quick comparison of the ideologies that were used in the building of the indices. One of the potential drawbacks of the first technique is that it might result in a composition of the index that is less diversified. A lower level of diversity results in increased risk and volatility. On the bright side, the prospect of inclusion in the index can perform the function of an incentive for high-emission enterprises to cut their emissions in a proactive manner. When compared to the first strategy, the second approach results in a significant reduction in the overall carbon footprint; however, this reduction is not as great as the first approach.

## 3 Data

The closing price data for the constituent stocks of S & P-500 and NIFTY-50 were obtained from Yahoo! Finance using the Python yfinance module. Similarly, the market cap data for each stock was downloaded using the Python pandas-datareader from Yahoo.

### 3.1 Carbon Data

The carbon emissions data for U.S. equities and Indian equities were obtained from the Bloomberg Terminal of the Indian Institute of Management, Bangalore (IIM-B). It included 14 different emissions measures. We chose the two variables greenhouse gas intensity per sale (GHG) and total carbon dioxide emissions (CO2) as proxies for the carbon footprint of stocks. These variables have lesser missing values for five years from 2017-2022.
The factor data for ([6](https://arxiv.org/html/2512.21092v1#S2.E6 "Equation 6 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) are obtained from the IIM-A Data Library [Agarwalla et al., [2013](https://arxiv.org/html/2512.21092v1#bib.bib2)] and for ([5](https://arxiv.org/html/2512.21092v1#S2.E5 "Equation 5 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) it is available at <https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>. The Fama-French five-factor data used in the regression step for the S & P-500 index
was obtained from Kenneth R. French - Data Library. Weekly and daily data are available in the data library, of which we have used the daily data.

## 4 Investment Portfolio Based on VaR and ES

We consider NIFTY-50 and S & P-500 data for 5 years, from 2017-18 until 2022-23. Then, four DIs are created from each benchmark, using the two methods and the two proxies, GHG and CO2. Comprehensive information about the stocks used for our calculations is reported in [Table 1](https://arxiv.org/html/2512.21092v1#S4.T1 "In 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") and [Table 2](https://arxiv.org/html/2512.21092v1#S4.T2 "In 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT").

Table 1: Number of stocks included (SI), stocks omitted (SO), and corresponding omission percentage of market capitalization MCO in the construction of DI for NIFTY-50.

|  | GHG | | | CO2 | | |
| --- | --- | --- | --- | --- | --- | --- |
| Period | SI | SO | MCO | SI | SO | MCO |
| 2017-18 | 30 | 20 | 35.3% | 32 | 18 | 33.7% |
| 2018-19 | 33 | 17 | 28.5% | 35 | 15 | 26.9% |
| 2019-20 | 34 | 16 | 25.3% | 36 | 14 | 23.7% |
| 2020-21 | 35 | 15 | 23.6% | 38 | 12 | 21.1% |
| 2021-22 | 35 | 15 | 23.6% | 38 | 12 | 21.0% |




Table 2: Number of SI, SO and corresponding MCO in the construction of DI for S & P-500.

|  | GHG | | | CO2 | | |
| --- | --- | --- | --- | --- | --- | --- |
| Period | SI | SO | MCO | SI | SO | MCO |
| 2017-18 | 331 | 171 | 21.0% | 335 | 167 | 20.6% |
| 2018-19 | 366 | 136 | 17.4% | 368 | 134 | 17.7% |
| 2019-20 | 408 | 94 | 13.9% | 410 | 92 | 13.7% |
| 2020-21 | 432 | 70 | 9.3 | 434 | 68 | 10.8% |
| 2021-22 | 435 | 67 | 9.1% | 436 | 66 | 9.57% |

Our analysis is divided into three main components: first, we will determine the optimal values of kk and CC for calculating the two DIs for each proxy and each benchmark; second, we will generate optimal portfolio weights using a one year window over a five year period (in-sample calculations); and third, we will calculate the monthly performance of the DIs and compare their performances against the benchmark (out-of-sample calculations).

The optimal values of kk and CC (refer to ([9](https://arxiv.org/html/2512.21092v1#S2.E9 "Equation 9 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) and ([11](https://arxiv.org/html/2512.21092v1#S2.E11 "Equation 11 ‣ 2.2 Methodology ‣ 2 Definition and Methodology ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"))), are ascertained by evaluating VaR and ES utilizing five years of data. A series of optimizations are conducted for various values of kk (5%-50% of NN) and CC (50%-95%). We plot kk vs VaR and kk vs ES and then find the value kk for which VaR and ES are minimum. Similarly, we choose the optimal carbon footprint threshold by plotting the relation between the percentage of carbon footprint and the VaR and ES of the portfolio and choose the lowest value that considerably reduces the VaR and ES in each case. The plots are not shown here; instead, the obtained optimal values of kk and CC are reported in [Table 3](https://arxiv.org/html/2512.21092v1#S4.T3 "In 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT").

Table 3: Optimal values of kk and CC estimated for each index

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | VaR | | | | ES | | | |
|  | GHG | | CO2 | | GHG | | CO2 | |
| Period | k | C | k | C | k | C | k | C |
| NIFTY-50 | 1 | 95% | 2 | 95% | 1 | 95% | 2 | 95% |
| S & P-500 | 48 | 85% | 32 | 95% | 16 | 95% | 32 | 95% |

Once the optimal kk and CC are obtained, the next step is to construct the DIs and determine the portfolio weights. We use a moving window of one year from April 2017 to March 2022 for in-sample estimations. In the next two sections we discuss the DIs obtained through VaR and ES assessment and our main findings from the in-sample estimation.

### 4.1 DIs through VaR assessment

As evident, we observe that the carbon footprints of the DIs are lower compared to the benchmark indices from [Figure 1](https://arxiv.org/html/2512.21092v1#S4.F1 "In 4.1 DIs through VaR assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") and [Figure 2](https://arxiv.org/html/2512.21092v1#S4.F2 "In 4.1 DIs through VaR assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"). A substantial reduction in the carbon footprint of the DIs is observed in all the cases.

![Refer to caption](Figure2.png)


Figure 1: Comparison of carbon footprints of the considered NIFTY-50 and the DIs

![Refer to caption](Figure3_VaR-SNP_.png)


Figure 2: Comparison of carbon footprints of the considered S & P-500 and the DIs

Now we look into the in-sample estimation of VaR for the four DIs constructed using a moving window of one year. The VaR estimates of the DIs at p=0.95p=0.95 are reported in [Table 4](https://arxiv.org/html/2512.21092v1#S4.T4 "In 4.1 DIs through VaR assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") and [Table 5](https://arxiv.org/html/2512.21092v1#S4.T5 "In 4.1 DIs through VaR assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"). The in-sample estimations indicate substantial reductions in carbon footprint for both methods, accompanied by low VaR estimates relative to the benchmark. Both DI\_1 and DI\_2 have VaR estimates close to each other. However, under some scenarios, VaR estimates of DI\_2 are higher than DI\_1.

Table 4: VaR estimates of the benchmark portfolio (BP) and DIs at p=0.95p=0.95 for NIFTY-50.

|  | GHG | | | CO2 | | |
| --- | --- | --- | --- | --- | --- | --- |
| Period | BP | VaR(DI\_1) | VaR(DI\_2) | BP | VaR(DI\_1) | VaR(DI\_2) |
| 2017-18 | 41.735 | 0.436 | 0.599 | 110.801 | 0.840 | 0.643 |
| 2018-19 | 101.062 | 0.523 | 1.067 | 33.697 | 1.502 | 1.161 |
| 2019-20 | 197.143 | 0.626 | 1.333 | 666.889 | 1.819 | 1.392 |
| 2020-21 | 156.305 | 1.189 | 1.562 | 131.275 | 1.162 | 1.527 |
| 2021-22 | 182.445 | 3.107 | 3.107 | 159.810 | 2.918 | 2.841 |




Table 5: VaR estimates of the BP and DIs at p=0.95p=0.95 for the S & P-500.

|  | GHG | | | CO2 | | |
| --- | --- | --- | --- | --- | --- | --- |
| Period | BP | VaR(DI\_1) | VaR(DI\_2) |  | VaR(DI\_1) | VaR(DI\_2) |
| 2017-18 | 0.387 | -0.021 | -0.021 | 0.385 | -0.021 | -0.022 |
| 2018-19 | 0.476 | -0.011 | -0.012 | 0.559 | -0.012 | -0.012 |
| 2019-20 | 1.936 | -0.002 | -0.005 | 3.429 | -0.004 | -0.005 |
| 2020-21 | 1.500 | 0.038 | 0.037 | 1.835 | 0.037 | 0.037 |
| 2021-22 | 1.512 | 0.006 | 0.007 | 2.876 | 0.006 | 0.007 |

### 4.2 DIs through ES assessment

Similarly, in [Figure 3](https://arxiv.org/html/2512.21092v1#S4.F3 "In 4.2 DIs through ES assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") and [Figure 4](https://arxiv.org/html/2512.21092v1#S4.F4 "In 4.2 DIs through ES assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"), we compare the carbon footprints of the decarbonized indices with the considered benchmark in each case. Similar outcomes can be observed with substantial reduction in the carbon footprint of the DIs in all the cases.

![Refer to caption](Figure5.png)


Figure 3: Comparison of carbon footprints of the considered NIFTY-50 and the DIs

![Refer to caption](Figure4_ES-SNP_.png)


Figure 4: Comparison of carbon footprints of the considered S & P-500 and the DIs

We will now examine the in-sample estimation of ES for the four DIs developed through a one year moving window. The ES estimates of the DIs at p=0.95p=0.95 are reported in [Table 6](https://arxiv.org/html/2512.21092v1#S4.T6 "In 4.2 DIs through ES assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT") and [Table 7](https://arxiv.org/html/2512.21092v1#S4.T7 "In 4.2 DIs through ES assessment ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"). These in-sample estimations reveal significant carbon footprint reductions in both methods, with low ES estimates compared to its benchmark. Both DI\_1 and DI\_2 have ES estimates close to each other. However, under some scenarios, ES values of DI\_2 are higher than DI\_1. Similar observations can also be seen in the case of VaR assessment.

Table 6: ES estimates of the BP and DIs at p=0.95p=0.95 for NIFTY-50.

|  | GHG | | | CO2 | | |
| --- | --- | --- | --- | --- | --- | --- |
| Period | BP | ES(DI\_1) | ES(DI\_2) | BP | ES(DI\_1) | ES(DI\_2) |
| 2017-18 | 52.116 | 1.053 | 0.805 | 138.884 | 0.543 | 0.750 |
| 2018-19 | 126.495 | 1.881 | 1.454 | 42.199 | 0.664 | 1.338 |
| 2019-20 | 247.4026 | 2.338 | 1.795 | 836.774 | 0.816 | 1.722 |
| 2020-21 | 195.351 | 1.420 | 1.899 | 163.990 | 1.446 | 1.915 |
| 2021-22 | 228.522 | 3.650 | 3.552 | 200.213 | 3.866 | 3.866 |




Table 7: ES estimates of the BP and DIs at p=0.95p=0.95 for S & P-500.

|  | GHG | | | CO2 | | |
| --- | --- | --- | --- | --- | --- | --- |
| Period | BP | ES(DI\_1) | ES(DI\_2) | BP | ES(DI\_1) | ES(DI\_2) |
| 2017-18 | 0.472 | -0.017 | -0.017 | 0.469 | -0.017 | -0.018 |
| 2018-19 | 0.589 | -0.009 | -0.009 | 0.691 | -0.009 | -0.009 |
| 2019-20 | 2.436 | 0.003 | 0.003 | 4.304 | 0.003 | 0.003 |
| 2020-21 | 1.826 | 0.042 | 0.042 | 2.251 | 0.043 | 0.042 |
| 2021-22 | 1.885 | 0.011 | 0.011 | 3.577 | 0.011 | 0.011 |

### 4.3 Out-of-sample calculation

In the out-of-sample performance, monthly returns are computed for 2018-19 to 2022-23 using weights 𝑾d\bm{W}^{d} generated from in-sample calculations conducted in the previous year. The monthly returns of a stock jj are estimated using the formula,

|  |  |  |
| --- | --- | --- |
|  | rj=(pj​f​i​n​a​l−pj​i​n​i​t​i​a​l)​100pj​i​n​i​t​i​a​l.r\_{j}=\frac{(p\_{jfinal}-p\_{jinitial})100}{p\_{jinitial}}. |  |

Therefore, the monthly returns of a portfolio consisting of NN stocks are given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=(W​Pf​i​n​a​l−W​Pi​n​i​t​i​a​l)​100W​Pi​n​i​t​i​a​l,R\_{t}=\frac{(WP\_{final}-WP\_{initial})100}{WP\_{initial}}, |  | (12) |

where RtR\_{t} is the percentage return on the portfolio in month tt, WW is the N×1N\times 1 vector of the portfolio weights, Pi​n​i​t​i​a​lP\_{initial} is the vector of stock closing prices at the beginning of the month tt, and Pf​i​n​a​lP\_{final} is the vector of stock closing prices at the end of the month tt. The monthly returns of the newly constructed decarbonized portfolios and the considered benchmark portfolios were estimated using equation ([12](https://arxiv.org/html/2512.21092v1#S4.E12 "Equation 12 ‣ 4.3 Out-of-sample calculation ‣ 4 Investment Portfolio Based on VaR and ES ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT")) and are plotted in [Figure 5](https://arxiv.org/html/2512.21092v1#A1.F5 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"), [Figure 6](https://arxiv.org/html/2512.21092v1#A1.F6 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"), [Figure 7](https://arxiv.org/html/2512.21092v1#A1.F7 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"), and [Figure 8](https://arxiv.org/html/2512.21092v1#A1.F8 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"). We observe that the constructed indices track the considered benchmark closely and, on average, outperform the benchmark index.

We then explore whether, during climate events, the DIs exhibit superior performance compared to their parent benchmark indices. To investigate this effect, we identify and highlight significant climate events from the past few years in the out-of-sample results of our indices. In 2018-2019, COP 24 was held in the month of December, the climate change conference (CCC) in Bonn and Bangkok was held in the months of May and September, and Hurricane Michael caused widespread damage in the state of Florida in October. In 2019-2020, Bonn CCC was held in the month of June, COP 25 was held in December, and the UN summit was held in September. In 2020-2021, Amphan, a devastating tropical cyclone that devastated Bangladesh and Eastern India, particularly West Bengal and Odisha, occurred in May, and the momentum of climate change was held in June. In 2021-2022, UN CCC was held in June, Hurricane Ida caused widespread damage in the U.S. state of Louisiana in August, and COP 26 was in the month of November. In 2022-2023, BON CCC was held in June, hurricanes Ian and Nicole caused widespread damage in the state of Florida in September and November and COP 27 was held in November. Following are the observations from [Figure 5](https://arxiv.org/html/2512.21092v1#A1.F5 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"), [Figure 6](https://arxiv.org/html/2512.21092v1#A1.F6 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"), [Figure 7](https://arxiv.org/html/2512.21092v1#A1.F7 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT"), and [Figure 8](https://arxiv.org/html/2512.21092v1#A1.F8 "In Appendix A Figures ‣ PORTFOLIO OPTIMIZATION FOR INDEX TRACKING WITH CONSTRAINTS ON DOWNSIDE RISK AND CARBON FOOTPRINT").

1. 1.

   NIFTY-50

   * •

     In light of the aforementioned notable climate events, we note that both DIs exceed the standard regarding out-of-sample returns in at least five of the twelve events.
   * •

     DI\_1 of the GHG outperforms the benchmark in 75% of the events.
   * •

     DI\_2 of the GHG and CO2 outperforms the benchmark in 67% of the events.
   * •

     DI\_1 of the CO2 outperforms the benchmark in 42% of the events.
2. 2.

   S&P-500

   * •

     In light of the significant climate events discussed above, it is evident that both DIs exceed the benchmark regarding out-of-sample returns in at least 8 of the fifteen events.
   * •

     DI\_1 of the GHG outperforms the benchmark in 53.4% of the events.
   * •

     DI\_2 of GHG and DI\_1 and DI\_2 of CO2 outperform the benchmark in 60% of the events.

## 5 Summary and Discussion

### 5.1 Summary of the results

Our work basically focuses on the theoretical framework and ideas proposed in the construction of DIs by [Andersson et al., [2016](https://arxiv.org/html/2512.21092v1#bib.bib3), Lakshmi et al., [2023](https://arxiv.org/html/2512.21092v1#bib.bib15)]. Andersson et al. [[2016](https://arxiv.org/html/2512.21092v1#bib.bib3)] constructs the DIs for the S & P-500 and the MSCI Europe benchmark indices, whereas Lakshmi et al. [[2023](https://arxiv.org/html/2512.21092v1#bib.bib15)] constructs DIs for the NIFTY-50 benchmark index. Both these papers involve construction of DIs by minimizing the tracking error. Though tracking error is an essential tool to identify how closely a portfolio follows its benchmark index. However, tracking errors do not give any idea of the risk of the portfolio. Also, we know that the optimal portfolio choice theory by Markowitz [[1952](https://arxiv.org/html/2512.21092v1#bib.bib17)] is based on the mean variance. However, variance takes into account all the deviations from the mean, higher as well as lower, failing to fully address the issue of the right tail of the returns, which is a common concern. Hence, variance is unsuitable as a measure of risk for financial returns. From the literature it is evident that portfolio optimization with respect to the tracking error and the variance is not enough to mitigate the climate risk; we do need the measures of downside risks. In this paper we construct the DIs by minimizing the mean-VaR and mean-ES, which means an investor possessing a DI is protected against the timing risk associated with climate mitigation policies, which are anticipated to adversely affect companies with high carbon footprints. This is due to the design of the DIs, which aim to sustain a low VaR and ES in relation to the benchmark indices. We construct two DIs from the established benchmarks and demonstrate their efficacy for the Indian (NIFTY-50 index) and the U.S. (S & P-500 index) economies.

The DIs obtained through VaR and ES assessment show a substantial reduction in the carbon footprint of the DIs in all the cases as compared to their benchmark indices, NIFTY-50 and S & P-500. Specifically, we show that the resulting index significantly lowers total carbon impact, acting as a hedge against climate risks. In-sample calculations reveal that the VaR and ES estimated at p=0.95p=0.95 of the DIs are very low compared to their benchmark indices. We also observe that the VaR and ES estimates of both the DIs (GHG and CO2) are very close to each other, except for a few instances where the VaR and ES of DI\_2 are higher than DI\_1. On the other hand, out-of-sample results demonstrate that both indices (GHG and CO2) outperform the benchmark indices during major climate events throughout the five years. Specifically, in the NIFTY-50, DI\_1 of the GHG outperforms the benchmark in 75% of the events and DI\_2 of the GHG and DI\_1 and DI\_2 of CO2 outperform the benchmark in 60% of the events. These results show that the DIs relation to the climate events is quite impressive in both the NIFTY-50 and S & P-500.

Both Cyclone Amphan, which resulted in US$14 billion in damages and 103 fatalities in India, and Hurricane Michael, which resulted in US$30 billion in damages and at least 59 fatalities in the U.S., caused severe destruction. Typically, these factors lead to an increase in relative risk. And it is well-known that a higher relative risk for a specific location is associated with an increased combination of hazard, exposure, and vulnerability. Yet, under these scenarios we observe that our proposed DIs outperform the benchmark.

### 5.2 Implications from our study

In the absence of climate mitigation initiatives, these low-carbon indices will yield returns that are generally comparable to the benchmark, occasionally underperforming or outperforming it. During significant climate events, the DIs have surpassed their benchmark. Upon the imposition or anticipation of a carbon penalty, these indices will surpass the actual benchmark in nearly all instances. However, the results indicate that the DIs perform adequately, suggesting that these investors will not incur a significant carbon penalty at this time. However, these distinctions can significantly assist policymakers in estimating carbon pricing. In the most adverse scenario, if carbon pricing is not implemented in the future, investing in low-carbon portfolios may still not result in significant losses for investors. The clear communication of the excluded and included stocks will reward the included companies and also help create a sense of awareness and healthy competition among the excluded companies to get back in the index by reducing their emissions. These indices will also help improve scientific quantification, accounting, and reporting of
emissions by companies.

### 5.3 Limitations

The quantification of company-specific GHG emissions to ascertain the carbon footprint is crucial in the formulation of DIs. A significant problem we encountered was locating dependable carbon data from open sources. Another significant issue was the substantial amount of missing data in the available sources, attributable to inadequate accounting and reporting by the companies. We found it necessary to exclude certain valuable stocks from the benchmark index owing to the lack of available carbon data. The stocks that were not included during the construction phase may represent the more volatile elements of the benchmark index, exhibiting heightened sensitivity to climate change and related policies. Another concern is whether the GHG emissions are accurately measured and reported in accordance with the GHG protocol and if there might be an inherent bias in the measurement process.

The regression results indicate that the Fama-French five variables for the American stock market and the four common components for the Indian market inadequately explain stock returns, which are mostly influenced by stock-specific risks. However, we choose this approach to streamline the issue and minimize errors associated with extensive variance-covariance matrices. And also due to the availability of these factors data in open sources. A further drawback was the unavailability of historical market capitalization data, resulting in the assumption that the weights of the benchmark indices remained constant over the years. The market cap data also depends on the time at which the data was downloaded, as it keeps changing. So slight variations can be observed in the market cap data due to the difference in the timings of data access. We have not followed a sector-by-sector filtering approach for construction of the DIs, due to which the newly constructed indices might have slightly different sector compositions from their parent benchmark index, especially when constructed using Method 1, where we drop kk stocks. We can extend this to factoring in sector compositions as well for better results.

## References

* TCF [2022]

  2022 status report, 2022.
  URL
  <https://assets.bbhub.io/company/sites/60/2022/10/2022-TCFD-Status-Report.pdf>.
* Agarwalla et al. [2013]

  Sobhesh K. Agarwalla, Joshy Jacob, and Jayanth R. Varma.
  Four factor model in Indian equities market.
  Working Paper W.P. No. 2013-09-05, Indian Institute of Management,
  Ahmedabad, 2013.
  URL
  <http://www.iimahd.ernet.in/~jrvarma/Indian-Fama-French-Momentum/four-factors-India-90s-onwards-IIM-WP-Version.pdf>.
* Andersson et al. [2016]

  Mats Andersson, Patrick Bolton, and Frédéric Samama.
  Hedging climate risk.
  *Financial Analysts Journal*, 72(3):13–32,
  2016.
* Artzner et al. [1999]

  Philippe Artzner, Freddy Delbaen, Jean-Marc Eber, and David Heath.
  Coherent measures of risk.
  *Mathematical finance*, 9(3):203–228, 1999.
* Breitenstein et al. [2022]

  Miriam Breitenstein, Carl-Philipp Anke, Duc Khuong Nguyen, and Thomas Walther.
  Stranded asset risk and political uncertainty: the impact of the coal
  phase-out on the german coal industry.
  *The Energy Journal*, 43(5):27–50, 2022.
* Byrd et al. [1987]

  Richard H Byrd, Robert B Schnabel, and Gerald A Shultz.
  A trust region algorithm for nonlinearly constrained optimization.
  *SIAM Journal on Numerical Analysis*, 24(5):1152–1170, 1987.
* Capelli et al. [2021]

  Paolo Capelli, Federica Ielasi, and Angeloantonio Russo.
  Forecasting volatility by integrating financial risk with
  environmental, social, and governance risk.
  *Corporate Social Responsibility and Environmental Management*,
  28(5):1483–1495, 2021.
* Capelli et al. [2023]

  Paolo Capelli, Federica Ielasi, and Angeloantonio Russo.
  Integrating esg risks into value-at-risk.
  *Finance Research Letters*, 55:103875, 2023.
* Clark [2023]

  Pilita Clark.
  A war for climate talent is hotting up.
  *Financial Times*, 2023.
  URL
  <https://www.ft.com/content/8412db41-dce1-44a7-9417-25a3a534ee54>.
* Conn et al. [2000]

  Andrew R Conn, Nicholas IM Gould, and Philippe L Toint.
  *Trust Region Methods*.
  SIAM, 2000.
* [11]

  European Banking Authority (EBA).
  Report on management and supervision of esg risks for credit
  institutions and investment firms.
  2021.
* Fama and French [2012]

  Eugene F Fama and Kenneth R French.
  Size, value, and momentum in international stock returns.
  *Journal of Financial Economics*, 105(3):457–472, 2012.
* Kallis [2011]

  Giorgos Kallis.
  In defence of degrowth.
  *Ecological economics*, 70(5):873–880,
  2011.
* Kimiaei [2022]

  Morteza Kimiaei.
  An active set trust-region method for bound-constrained optimization.
  *Bulletin of the Iranian Mathematical Society*, 48:1–25, 2022.
* Lakshmi et al. [2023]

  MV Lakshmi, Soudeep Deb, and Rituparna Sen.
  Environmentally responsible index tracking: Maintaining performance
  while reducing carbon footprint of the portfolio.
  *Statistics and Applications*, 23(1):217–223, 2023.
* Li et al. [2022]

  Xuepeng Li, Fengmin Xu, and Kui Jing.
  Robust enhanced indexation with esg: An empirical study in the
  chinese stock market.
  *Economic Modelling*, 107:105711, 2022.
* Markowitz [1952]

  H Markowitz.
  Portfolio selection.
  *Journal of Finance*, 7(1):77–91, 1952.
* Mezali and Beasley [2013]

  H Mezali and John E Beasley.
  Quantile regression for index tracking and enhanced indexation.
  *Journal of the Operational Research Society*, 64(11):1676–1692, 2013.
* Nishad et al. [2021]

  T Mohamed Nishad et al.
  Carbon reduction and sustainable investment: A way to sustainable
  development.
  *Energy Economics Letters*, 8(2):134–144,
  2021.
* Patel and Kumari [2020]

  Sanjay Kumar Patel and Poonam Kumari.
  Indian stock market movements and responsiveness of sustainability
  indices: A risk adjusted analysis.
  *International Management Review*, 16(1):55–64, 2020.
* Sanchez [2025, February 12]

  Maria Sanchez.
  What’s in a name? from s&p 500 esg index to s&p 500 scored &
  screened index.
  2025, February 12.
  URL
  <https://www.indexologyblog.com/2025/02/12/whats-in-a-name-from-sp-500-esg-index-to-sp-500-scored-screened-index/>.
* Schandl et al. [2016]

  Heinz Schandl, Steve Hatfield-Dodds, Thomas Wiedmann, Arne Geschke, Yiyong Cai,
  James West, David Newth, Tim Baynes, Manfred Lenzen, and Anne Owen.
  Decoupling global environmental pressure and economic growth:
  scenarios for energy use, materials use and carbon emissions.
  *Journal of cleaner production*, 132:45–56, 2016.

## Appendix A Figures

![Refer to caption](2.png)


Figure 5: Monthly returns of DIs vs Benchmark index for NIFTY-50 (GHG)

![Refer to caption](0.png)


Figure 6: Monthly returns of DIs vs Benchmark index for NIFTY-50 (CO2)

![Refer to caption](R1_GHG_SNP.png)


Figure 7: Monthly returns of DIs vs Benchmark index for S&P-500 (GHG)

![Refer to caption](R1_CO2_SNP.png)


Figure 8: Monthly returns of DIs vs Benchmark index for S&P-500 (CO2)