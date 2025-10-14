---
authors:
- Zheng Cao
- Xingran Shao
- Yuheng Yan
- Helyette Geman
doc_id: arxiv:2510.10878v1
family_id: arxiv:2510.10878
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power
  Law Model
url_abs: http://arxiv.org/abs/2510.10878v1
url_html: https://arxiv.org/html/2510.10878v1
venue: arXiv q-fin
version: 1
year: 2025
---


Zheng Cao,
Xingran Shao,
Yuheng Yan,
Helyette Geman
  
(zcao26, xshao12, yyan75)@jh.edu,hgeman1@jhu.edu
  
Department of Applied Mathematics and Statistics
  
Johns Hopkins University
  
All authors contributed equallyCorresponding author

###### Abstract

We propose a novel model, the Hyped Log-Periodic Power Law Model (HLPPL), to the problem of quantifying and detecting financial bubbles, an ever-fascinating one for academics and practitioners alike. Bubble labels are generated using a Log-Periodic Power Law (LPPL) model, sentiment scores, and a hype index we introduced in previous research on NLP forecasting of stock return volatility. Using these tools, a dual-stream transformer model is trained with market data and machine learning methods, resulting in a time series of confidence scores as a Bubble Score. A distinctive feature of our framework is that it captures phases of extreme overpricing and underpricing within a unified structure.

We achieve an average yield of 34.13 percentage annualized return when backtesting U.S. equities during the period 2018 to 2024, while the approach exhibits a remarkable generalization ability across industry sectors. Its conservative bias in predicting bubble periods minimizes false positives, a feature which is especially beneficial for market signaling and decision-making. Overall, this approach utilizes both theoretical and empirical advances for real-time positive and negative bubble identification and measurement with HLPPL signals.

Keywords: NLP, Hype Index, Financial Bubbles, HLPPL Model, Transformer Learning

## 1 Introduction

The notion of a financial “bubble" dates back to the early 18th century South Sea Bubble, where inflated company stocks were described as fragile and insubstantial, like air-filled bubbles destined to burst. Sir Isaac Newton, one of history’s greatest minds, reportedly lost nearly £​20,000£20,000 in the collapse, lamenting that he could “calculate the motions of heavenly bodies, but not the madness of people." Earlier episodes such as the Dutch tulip mania were termed “manias," but the bubble metaphor has since become the dominant way to capture both the rapid inflation and sudden collapse of asset prices.

In financial economics, a bubble refers to a situation where an asset’s price exceeds its fundamental value by a significant margin, driven by expectations of further price increases rather than justified by intrinsic returns.

This research makes several significant contributions to the financial bubble detection and quantification literature. First, we introduce the systematic framework for identifying and quantifying negative bubbles, expanding the traditional focus beyond overvaluation episodes. Second, we demonstrate how behavioral finance indicators can be effectively integrated with the technical Log-Periodic Power Law Model (LPPL) analysis to improve bubble detection accuracy. Third, we develop a practical trading strategy that translates bubble signals into actionable investment decisions, providing empirical evidence of the framework’s profitability.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2510.10878v1#S2 "2 Literature Review ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") reviews the relevant literature on financial bubbles, LPPL modeling, Natural Language Processing (NLP) for Finance, and Hype Index. Section [3](https://arxiv.org/html/2510.10878v1#S3 "3 The Hyped Log-Periodic Power Law Model ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents the Hyped Log-Periodic Power Law Model (HLPPL), including the mathematical framework for bidirectional bubble detection and behavioral indicator integration. Section [4](https://arxiv.org/html/2510.10878v1#S4 "4 Transformer Model ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") introduces the transformer model and describes the data sources and empirical implementation. Section [5](https://arxiv.org/html/2510.10878v1#S5 "5 Trading with Bubble Scores ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents comprehensive backtesting results across multiple assets and time periods. Section [6](https://arxiv.org/html/2510.10878v1#S6 "6 Machine Learning Enhanced Trading Strategy ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents the improved model results with Machine Learning (ML) models.
Section [7](https://arxiv.org/html/2510.10878v1#S7 "7 Conclusion ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") concludes with suggestions for future research directions.

The empirical analysis demonstrates that the HLPPL framework generates superior returns compared to traditional buy-and-hold strategies and pure LPPL approaches. The integration of behavioral indicators significantly improves bubble detection accuracy, while the bidirectional framework captures valuable trading opportunities that would be missed by conventional methods. These findings have important implications for portfolio management, risk assessment, and market timing strategies in both institutional and retail investment contexts.

## 2 Literature Review

The detection and prediction of financial bubbles have long been central challenges in financial economics, with significant implications for market stability, risk management, and investment decision-making. Traditional approaches to bubble detection often rely on fundamental valuation metrics or statistical anomalies in price movements. Campbell and Shiller (1987) [[1](https://arxiv.org/html/2510.10878v1#bib.bib1)] show that stock prices deviating from earnings and dividends may signal bubbles, as traditional detection methods rely mainly on fundamentals or price anomalies. However, these methods frequently fail to capture the complex dynamics underlying speculative episodes. This paper introduces an enhanced framework that integrates the Log-Periodic Power Law Singularity (LPPL) model with machine learning to provide a more comprehensive approach to bubble detection and trading strategy development.

The Log-Periodic Power Law Singularity (LPPL) model was first introduced by
Johansen, Ledoit, and Sornette (2000)[[6](https://arxiv.org/html/2510.10878v1#bib.bib6)].
The model captures the dynamics of financial bubbles by describing the
asset price trajectory as a super-exponential power law acceleration
decorated with log-periodic oscillations, reflecting nonlinear positive feedbacks and herding effects among investors.

In its original form, the residuals of the LPPL model were typically treated as white noise without a specific economic structure. A major
advance was later proposed by Lin, Ren, and Sornette (2014)[[7](https://arxiv.org/html/2510.10878v1#bib.bib7)], who introduced the so-called
‘volatility-confined LPPL model’. In this specification, the
residuals are modeled as an Ornstein–Uhlenbeck (O–U) mean-reverting
process, ensuring that deviations from the deterministic LPPL trajectory remain bounded. This modification yields a consistent and
self-contained framework in which the deterministic LPPL component
represents the bubble dynamics, while the residuals account for the
stochastic reassessment of returns by investors.

Jarrow, Protter, and Shimbo (2010)[[5](https://arxiv.org/html/2510.10878v1#bib.bib5)] established the martingale approach to bubbles
in both complete and incomplete markets, showing how strict local
martingales can represent bubble dynamics and affect derivative pricing.

For asset bubbles, Phillips, Shi, and Yu (2015)[[9](https://arxiv.org/html/2510.10878v1#bib.bib9)] introduced the Generalized Sup ADF (GSADF) test to detect explosive behaviors in asset price time series. Their empirical analysis of the S&P 500 revealed that the GSADF test statistic typically begins to diverge significantly about 2 to 3 months before a bubble collapses. This suggests that financial bubbles often exhibit measurable warning signs well before the actual crash.

### 2.1 LPPL Model

This section serves to situate our research within the broader literature on bubble modeling.
We begin by reviewing the Log-Periodic Power Law (LPPL) model developed by Sornette and collaborators, which provides the dominant theoretical framework for characterizing speculative bubbles as faster-than-exponential trajectories decorated with log-periodic oscillations.
We then highlight the gap in this stream of research: while LPPL and its extensions (such as LPPLS) focus on technical price dynamics and the prediction of critical times, they tend to underemphasize behavioral-finance drivers such as investor sentiment and media attention.
Finally, we introduce our own research focus, which aims to complement the LPPL tradition by systematically integrating behavioral signals with residual-based LPPL analysis, thereby transforming bubble detection into a richer and more operational framework.

#### 2.1.1 LPPL model

The Log-Periodic Power Law (LPPL) model, pioneered by Sornette and Johansen, represents a cornerstone in the quantitative analysis of speculative bubbles[[11](https://arxiv.org/html/2510.10878v1#bib.bib11)]. The LPPL framework originates from the analogy between financial markets approaching a crash and critical phase transitions in physical systems, where collective behavior leads to finite-time singularities.

Formally, the LPPL model postulates that the logarithm of the asset price p​(t)p(t) can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡p​(t)=A+B​(tc−t)m+C​(tc−t)m​cos⁡(ω​ln⁡(tc−t)+ϕ),\ln p(t)=A+B(t\_{c}-t)^{m}+C(t\_{c}-t)^{m}\cos\!\Big(\omega\ln(t\_{c}-t)+\phi\Big), |  | (1) |

where AA is the constant baseline level, BB captures the super-exponential growth rate, CC determines the amplitude of oscillations, tct\_{c} is the critical time (the theoretical end of the bubble), m∈(0,1)m\in(0,1) is the critical exponent, ω>0\omega>0 is the log-periodic frequency, and ϕ\phi is the phase.

The equation above can be motivated in two steps:

1. Power-law acceleration.
Suppose that the expected growth of prices follows a nonlinear feedback mechanism such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ln⁡p​(t)d​t∝(tc−t)m−1,0<m<1,\frac{d\ln p(t)}{dt}\propto(t\_{c}-t)^{m-1},\qquad 0<m<1, |  | (2) |

which integrates to a finite-time singularity of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡p​(t)=A+B​(tc−t)m.\ln p(t)=A+B(t\_{c}-t)^{m}. |  | (3) |

2. Discrete scale invariance.
Empirical evidence shows oscillatory corrections to the power law. By assuming that investor herding generates log-periodic fluctuations, the growth term is decorated with an oscillatory modulation leading to (1).

The power-law component (tc−t)m(t\_{c}-t)^{m} encodes the deterministic acceleration of prices as the bubble approaches its critical end point.
The log-periodic term reflects alternating phases of optimism and skepticism among market participants, whose frequency increases as t→tct\to t\_{c}, signaling the growing instability of the bubble regime.
Together, these terms imply that bubbles are not purely exponential but exhibit faster-than-exponential growth punctuated by accelerating oscillations.

This formulation has been widely applied in empirical studies of equity, real estate, and commodity bubbles, providing a theoretical backbone for the quantitative detection of financial instabilities.

#### 2.1.2 Limitations of LPPL Model

Despite significant progress in LPPL methodology and the integration of behavioral finance, several core limitations remain that constrain both practical applicability and theoretical completeness. First, conventional LPPL models primarily emphasize the detection of overvaluation bubbles, while neglecting undervaluation episodes that may represent equally important trading opportunities. Such an asymmetric perspective overlooks the fact that markets can systematically deviate from fair value in both directions. Second, most existing detection frameworks rely almost exclusively on price-based technical indicators, while disregarding the information contained in investor sentiment and market attention measures—factors that behavioral finance theory identifies as central to bubble dynamics. Third, current approaches often lack the dynamic adaptability necessary for real-time trading, producing retrospective assessments rather than actionable forward-looking signals.

Following Sornette’s foundational work, subsequent research has introduced the Log-Periodic Power Law Singularity (LPPLS) model to enhance bubble detection accuracy and improve predictive capabilities. The LPPLS framework incorporates additional parameters to capture the complex oscillatory behavior preceding market crashes, representing a significant methodological advancement in technical bubble detection. However, while these developments have strengthened the mathematical rigor of price-based analysis, they maintain the fundamental limitation of focusing primarily on technical price patterns while neglecting the behavioral and psychological drivers that underlie bubble formation and evolution.

Our research diverges from this purely technical trajectory by prioritizing the systematic integration of behavioral finance principles into quantitative bubble detection frameworks. Rather than solely refining mathematical models of price dynamics, we focus on incorporating the human elements—investor sentiment, media attention, and market psychology—that behavioral finance theory identifies as the fundamental drivers of bubble phenomena. This approach recognizes that bubbles are fundamentally behavioral phenomena that manifest in price patterns, rather than purely mathematical anomalies that can be captured through technical analysis alone.

This study addresses these limitations through a set of theoretical and methodological contributions that advance the state of bubble detection. Our work spans four dimensions: theoretical framework development, methodological design, empirical validation, and practical implementation.

#### 2.1.3 Complementary Research Focus

The Log-Periodic Power Law (LPPL) and its extensions have provided a mathematically rigorous framework for modeling speculative bubbles and their associated crashes. Sornette’s pioneering work has demonstrated how super-exponential trajectories decorated with log-periodic oscillations can capture the collective dynamics of financial markets, leading to the identification of both bubble phases and their mirror images, such as negative bubbles and anti-bubbles. These contributions have established the LPPL family of models as a cornerstone in the quantitative analysis of market instability.

Our research does not aim to challenge or replace this stream of work. Rather, it focuses on a complementary dimension: the behavioral layer that underpins bubble phenomena. While LPPL emphasizes the endogenous dynamics of price trajectories around critical times, our framework seeks to quantify how media attention, investor sentiment, and broader market psychology contribute to deviations from the LPPL-predicted path. In this sense, our study offers an additional behavioral-finance-based perspective that enriches the LPPL tradition.

Specifically, we are interested in identifying what we call negative behaviors—periods during an ongoing bubble trajectory when observed prices fall below the LPPL fit but do not evolve into full-fledged negative bubbles. These episodes often correspond to temporary corrections or oversold phases, which may present actionable trading opportunities. In many cases, such negative-bubble phases are followed by sharp or prolonged overbuy rebounds, pushing the bubble to new highs; indeed, a full bubble trajectory often only collapses after undergoing several rounds of alternating overselling and overbuying. By embedding residual-based measures into a behavioral framework, we extend LPPL modeling toward a more comprehensive detection system that highlights both overpricing and underpricing dynamics.

In this sense, our research represents a bridge between technical modeling and behavioral finance. Whereas the LPPL family formalizes the mathematical structure of bubbles, our contribution lies in integrating sentiment analysis, hype indices, and other behavioral indicators into the detection process. This quantitative innovation not only complements existing LPPL-based methodologies but also moves closer to capturing the inherently behavioral nature of financial bubbles.

### 2.2 NLP for Finance

NLP-based news sentiment has proven effective in capturing shifts in market conditions. Shapiro, Sudhof, and Wilson (2017)[[10](https://arxiv.org/html/2510.10878v1#bib.bib10)] develop an economic sentiment index based on real-time financial news, showing that sentiment predicts macro-variables such as consumption and output. Similarly, Tetlock (2007)[[12](https://arxiv.org/html/2510.10878v1#bib.bib12)] constructs a media-based sentiment index from daily Wall Street Journal columns, finding that negative news sentiment significantly predicts lower market returns. These studies highlight how unstructured news content embeds investor sentiment and provides predictive power for asset prices.

Building on this line of research, Maghyereh and Abdoh (2022)[[8](https://arxiv.org/html/2510.10878v1#bib.bib8)] examine whether news-based economic sentiment can predict price bubbles in precious metals markets. Using GSADF tests and probit models, they find that bearish sentiment significantly raises the probability of bubbles in gold and platinum, particularly during crisis periods. This result underscores the predictive value of sentiment signals relative to traditional market indicators.

The role of media attention in asset pricing has long been recognized in financial economics, with early work by Tetlock (2007) demonstrating how media pessimism predicts short-term market returns and trading activity. This line of research was advanced by Glasserman and Mamaysky (2019)[[4](https://arxiv.org/html/2510.10878v1#bib.bib4)], who introduced measures of informational “unusualness” in financial news and linked them to future volatility. Cao and Geman (2025) have shown that using improved sentiment analysis and scoring methods and the change of probability measure can greatly enhance the forecasting accuracy of equity price and volatility directions[[2](https://arxiv.org/html/2510.10878v1#bib.bib2)].

Within this broader literature, the Hype Index was proposed by Cao, Wunkaew, and Geman (2025)[[3](https://arxiv.org/html/2510.10878v1#bib.bib3)] as a novel, NLP-driven measure of investor attention. Unlike traditional sentiment indicators, the Hype Index isolates the intensity of media coverage rather than its tone. By quantifying the share of financial news devoted to a given stock or sector, it provides a direct measure of disproportionate attention that is distinct from sentiment polarity[[2](https://arxiv.org/html/2510.10878v1#bib.bib2)]. The authors further extend the concept through a capitalization-adjusted version, which benchmarks media exposure relative to economic size, thereby identifying firms or sectors that attract excess attention beyond what fundamentals would suggest.

Empirical evaluation shows that the Hype Index is systematically associated with volatility, market-wide stress events, and cross-sector differences in attention. For instance, sectors such as Information Technology and Financials are persistently over-hyped, while Utilities and Real Estate remain under-hyped over long horizons. This framework thus broadens the toolkit for analyzing bubbles, volatility clustering, and behavioral biases, providing an interpretable bridge between unstructured news flows and market dynamics.

## 3 The Hyped Log-Periodic Power Law Model

This section develops the conceptual and methodological foundation of the proposed *Bubble Score*. We integrate financial theory, behavioral measures, and the Log-Periodic Power Law (LPPL) framework to capture both speculative bubbles and protracted undervaluation phases. The Bubble Score is designed as a unified indicator, capable of distinguishing overvaluation (bubble behaviors) from undervaluation (negative behaviors), while embedding market psychology through hype and sentiment.

### 3.1 Financial Bubbles and Negative Bubbles

Financial bubble is generally understood as a phase of accelerating overvaluation in which asset prices grow at a faster-than-exponential rate. This growth is fueled by positive feedback loops among investors, herding behavior, and speculative enthusiasm. Prices are pushed far above levels justified by fundamentals, and the process culminates in a regime shift, often marked by a sharp correction or crash. Within the Log-Periodic Power Law (LPPL) framework of Sornette, bubbles are modeled as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡p​(t)=A+B​(tc−t)m+C​(tc−t)m​cos⁡(ω​ln⁡(tc−t)+ϕ),\ln p(t)=A+B(t\_{c}-t)^{m}+C(t\_{c}-t)^{m}\cos\!\Big(\omega\ln(t\_{c}-t)+\phi\Big), |  | (4) |

where tct\_{c} is the critical time, m∈(0,1)m\in(0,1), and the oscillatory term reflects alternating waves of optimism and skepticism. As t→tct\to t\_{c}, the oscillations compress in time, indicating a growing instability in the system.

a long-lived phase of protracted decline following a crash, modeled in the LPPL framework by reversing the temporal symmetry of the bubble trajectory. However, in this study we do not explicitly model such full-fledged negative bubbles. Instead, our focus remains on the bubble trajectory, while recognizing that prices may temporarily fall below the fitted LPPL path.

We refer to these deviations as negative behaviors: phases in which observed prices lie persistently below the LPPL trajectory, without constituting a structural negative bubble. Negative behaviors are of particular interest because they may signal oversold conditions within an ongoing bubble regime, thereby offering potential buy-in opportunities before the bubble resumes or intensifies. This terminology allows us to capture bearish mispricings in a bubble context, while keeping the analytical framework firmly grounded in the dynamics of the LPPL bubble model.

### 3.2 LPPL Residuals and Normalization

To operationalize deviations from the LPPL benchmark, we define the log-price residual as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ​(t)=ln⁡p​(t)−ln⁡p^​(t),\epsilon(t)=\ln p(t)-\ln\hat{p}(t), |  | (5) |

where p​(t)p(t) is the observed price and ln⁡p^​(t)\ln\hat{p}(t) is the LPPL trajectory as shown in (5).

Within the extended study of Lin, Ren, and Sornette (2014),
these residuals are not treated as random walks, but as mean-reverting
fluctuations around the LPPL path.

Formally, the dynamics of residuals ϵ​(t)\epsilon(t)
can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​ϵ​(t)=ϵ​(t+1)−ϵ​(t)=−α​ϵ​(t)+ut,\Delta\epsilon(t)=\epsilon(t+1)-\epsilon(t)=-\alpha\epsilon(t)+u\_{t}, |  | (6) |

where utu\_{t} is a Gaussian white noise. This AR(1) specification ensures that
ϵ​(t)\epsilon(t) remains stationary, consistently pulling the log-price back towards the
LPPL trajectory.

Equivalently, the log-price process satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡pt+1=ln⁡pt+Δ​ln⁡p^​(t)−α​(ln⁡pt−ln⁡p^​(t))+ut,\ln p\_{t+1}=\ln p\_{t}+\Delta\ln\hat{p}(t)-\alpha\big(\ln p\_{t}-\ln\hat{p}(t)\big)+u\_{t}, |  | (7) |

so that the observed trajectory is composed of a deterministic LPPL drift plus
a mean-reverting residual. This guarantees that explosive LPPL growth is
"confined" by volatility rather than diverging arbitrarily.

For comparability across assets and time windows, we normalize residuals by
their maximum absolute deviation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵnorm​(t)=ϵ​(t)maxs≤t⁡|ϵ​(s)|,ϵnorm​(t)∈[−1,1].\epsilon\_{\text{norm}}(t)=\frac{\epsilon(t)}{\max\_{s\leq t}|\epsilon(s)|},\qquad\epsilon\_{\text{norm}}(t)\in[-1,1]. |  | (8) |

Positive values of ϵnorm​(t)\epsilon\_{\text{norm}}(t) are interpreted as bubble behaviors, where observed prices stand above the LPPL benchmark and exhibit faster-than-exponential growth.
Negative values of ϵnorm​(t)\epsilon\_{\text{norm}}(t) instead signal negative behaviors, corresponding to phases of relative underpricing or incomplete corrections in which prices persist below the LPPL trajectory.

Thus, the residual process provides a mathematically consistent way to capture
short-term mispricings while preserving the global LPPL bubble dynamics.

### 3.3 Sentiment Score

While the Hype Index measures the intensity of media coverage, it does not account for the tone of that coverage. To complement it, we incorporate a Sentiment Score that captures the polarity of news content. This follows a long line of empirical work, beginning with Tetlock (2007), which demonstrates that media pessimism predicts short-term returns and trading volume, and more recent advances in NLP-based sentiment analysis.

Definition. Let each news article kk about stock ii on day tt be assigned a sentiment polarity score si,t,k∈[−1,1]s\_{i,t,k}\in[-1,1], where −1-1 denotes extreme pessimism, 0 neutrality, and +1+1 extreme optimism. Using the Finbert sentiment model, these scores are computed based on lexical and syntactic features of the text. The aggregate Sentiment Score for stock ii on day tt is then defined as the weighted average:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Si,t=∑k=1Ni,twi,t,k​si,t,k∑k=1Ni,twi,t,k,S\_{i,t}=\frac{\sum\_{k=1}^{N\_{i,t}}w\_{i,t,k}\,s\_{i,t,k}}{\sum\_{k=1}^{N\_{i,t}}w\_{i,t,k}}, |  | (9) |

where Ni,tN\_{i,t} is the number of articles about stock ii on day tt, and wi,t,kw\_{i,t,k} is a weight that can reflect article length, source credibility, or recency.

The Sentiment Score is scale-free, bounded in [−1,1][-1,1], and directly comparable across time and assets. It embeds the psychological tone of news flow into the analytical framework, thereby complementing the Hype Index. Together, (Hi,t,Si,t)(H\_{i,t},S\_{i,t}) provide a joint characterization of media attention and tone, enabling richer detection of bubble-related behaviors than price-based signals alone.

### 3.4 Hype Index

The role of media attention in asset pricing has been repeatedly highlighted in the literature. Investor attention is limited, and disproportionate coverage of certain assets creates systematic patterns in both returns and volatility. Building on this idea, Cao, Wunkaew, and Geman (2025) introduce the Hype Index as a quantitative measure of the relative share of media coverage devoted to a given stock or sector. Unlike sentiment indicators that focus on the polarity of news, the Hype Index isolates the intensity of coverage, thereby disentangling how much attention an asset receives from how that attention is framed.

Definition. Let Ni,tN\_{i,t} denote the number of financial news articles that mention stock ii on day tt, and let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nmkt,t=∑j=1MNj,tN\_{\text{mkt},t}=\sum\_{j=1}^{M}N\_{j,t} |  | (10) |

be the aggregate number of articles covering a reference set of MM firms (e.g., the S&P 100 constituents) on the same day. The *Hype Index* for stock ii is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hi,t=Ni,tNmkt,t,∑i=1MHi,t=1.H\_{i,t}=\frac{N\_{i,t}}{N\_{\text{mkt},t}},\qquad\sum\_{i=1}^{M}H\_{i,t}=1. |  | (11) |

This construction makes Hi,tH\_{i,t} a probability measure of media attention allocation across the universe of reference stocks.

A higher value of Hi,tH\_{i,t} indicates disproportionate media focus relative to peers, regardless of the firm’s market capitalization or fundamentals. When Hi,tH\_{i,t} rises sharply, the stock dominates financial news flow, capturing a larger share of scarce investor attention. This aligns with attention-based asset pricing theory, which posits that such concentration of focus can drive both mispricing and volatility clustering.

To differentiate between “natural” attention due to economic importance and “excessive” attention, Cao et al. (2025) also introduce a capitalization-adjusted version:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CapHi,t=Hi,tWi,tcap,Wi,tcap=M​Ci,t∑j=1MM​Cj,t,\mathrm{CapH}\_{i,t}=\frac{H\_{i,t}}{W^{\text{cap}}\_{i,t}},\qquad W^{\text{cap}}\_{i,t}=\frac{MC\_{i,t}}{\sum\_{j=1}^{M}MC\_{j,t}}, |  | (12) |

where M​Ci,tMC\_{i,t} is the market capitalization of firm ii at time tt.
The capitalization-adjusted Hype Index CapHi,t\mathrm{CapH}\_{i,t} can be interpreted as

|  |  |  |  |
| --- | --- | --- | --- |
|  | CapHi,t={>1,excessive hype: media coverage exceeds the stock’s economic weight,<1,under-hype: media coverage falls short of the level implied by capitalization.\mathrm{CapH}\_{i,t}=\begin{cases}>1,&\text{excessive hype: media coverage exceeds the stock’s economic weight},\\ <1,&\text{under-hype: media coverage falls short of the level implied by capitalization}.\end{cases} |  | (13) |

This dual representation allows us to separate absolute media attention from relative overexposure. Persistent deviations of CapHi,t\mathrm{CapH}\_{i,t} above unity are indicative of hype-driven dynamics that can reinforce bubble behaviors, while values below unity suggest neglected or under-covered stocks. The Hype Index thus provides a mathematically grounded, scale-invariant way to quantify the role of media in amplifying both bubble and negative behavior regimes.

### 3.5 Bubble Score

We combine technical mispricing with behavioral signals into a single Bubble Score:

|  |  |  |  |
| --- | --- | --- | --- |
|  | BubbleScorei​(t)={ϵnorm​(t)+α1​Hi,t+α2​Si,t,ϵnorm​(t)>0​(Bubble behavior),ϵnorm​(t)−α1​Hi,t+α2​Si,t,ϵnorm​(t)<0​(Negative behavior).\text{BubbleScore}\_{i}(t)=\begin{cases}\epsilon\_{\text{norm}}(t)+\alpha\_{1}H\_{i,t}+\alpha\_{2}S\_{i,t},&\epsilon\_{\text{norm}}(t)>0\ (\text{Bubble behavior}),\\[6.0pt] \epsilon\_{\text{norm}}(t)-\alpha\_{1}H\_{i,t}+\alpha\_{2}S\_{i,t},&\epsilon\_{\text{norm}}(t)<0\ (\text{Negative behavior}).\end{cases} |  | (14) |

Here, α1\alpha\_{1} and α2\alpha\_{2} are parameters that determine the relative weight of media attention and sentiment. The construction reflects the intuition that hype always amplifies speculative intensity, while sentiment exerts opposite effects in bubble versus negative behavior regimes.

The construction in equation (13) reflects different roles of hype and sentiment.
Hype Hi,tH\_{i,t} amplifies market extremes: it is positive in bubble phases to reinforce overvaluation,
and negative in negative-bubble phases to deepen undervaluation.
Sentiment Si,tS\_{i,t} acts as a corrective buffer: in bubble phases, optimistic sentiment sustains the upward momentum
while pessimistic sentiment dampens it; in negative-bubble phases, optimistic sentiment alleviates undervaluation
while pessimistic sentiment intensifies it.

Overall, the BubbleScore measures the likelihood and intensity of a bubble regime.
Large positive values indicate strong speculative overpricing (normal bubbles),
while large negative values indicate pronounced undervaluation negative bubbles).
The magnitude of the score thus provides a direct quantitative gauge of bubble dynamics.

Positive values indicate speculative overvaluation, while negative values indicate underpricing relative to LPPL expectations. Magnitudes reflect the intensity of deviation.

### 3.6 Case Study: Across Different Individual Stocks in U.S. Market

Before turning to specific examples, we illustrate how the Bubble Score developed in the previous section can be applied as an indicator for empirical analysis. In particular, when the Bubble Score remains above a chosen threshold for a sustained period, we classify the corresponding interval as a normal bubble period, whereas periods of sustained negative values are designated as negative bubble periods. This classification enables us to visualize bubble dynamics directly on daily price trajectories. Otherwise, we call the trajectory during a bubble neutral period.

#### 3.6.1 HOUS Case Study

Figure [1](https://arxiv.org/html/2510.10878v1#S3.F1 "Figure 1 ‣ 3.6.1 HOUS Case Study ‣ 3.6 Case Study: Across Different Individual Stocks in U.S. Market ‣ 3 The Hyped Log-Periodic Power Law Model ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model")–[4](https://arxiv.org/html/2510.10878v1#S3.F4 "Figure 4 ‣ 3.6.1 HOUS Case Study ‣ 3.6 Case Study: Across Different Individual Stocks in U.S. Market ‣ 3 The Hyped Log-Periodic Power Law Model ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") apply our BubbleScore framework to Anywhere Real Estate Inc. (HOUS), a leading U.S. residential real-estate brokerage operating brands such as Century 21 and Coldwell Banker. Because our later trading experiments target housing-related exposures, HOUS is a natural benchmark to validate both relevance and robustness of our methodology in this sector.

![Refer to caption](HOUS_Case_study_less_min_days/LPPL_HOUS_C_residual_only1.png)


Figure 1: LPPL *residual-only* detection for HOUS. The black line shows log prices and the blue dashed curve the LPPL fit. Green (red) bands denote intervals where the observed series is materially above (below) the theoretical path. A clear local peak is detected in mid-2023, followed by a prolonged oversold phase into late-2023; however, short and noisy swings can still trigger event windows under the residual-only approach.

![Refer to caption](HOUS_Case_study_less_min_days/LPPL_HOUS_D_bubblescore_detection.png)


Figure 2: HLPPL (BubbleScore) detection for HOUS. By augmenting residual information with a Hype index and text Sentiment, and enforcing minimum-duration and threshold rules, spurious short-lived windows are filtered out and the alternating bubble/negative-bubble phases over 2022–2024 are delineated more crisply (including the mid-2023 top and the late-2023 to early-2024 rebound).

![Refer to caption](HOUS_Case_study_less_min_days/LPPL_HOUS_E_signal_comparison1.png)


Figure 3: Signal comparison: BubbleScore (with Hype & Sentiment) vs. residual-only. The two signals agree on major turning points, but HLPPL is smoother around decision thresholds (e.g., ±0.4\pm 0.4), produces fewer flips during choppy regimes, and down-weights moves that lack media attention or textual-emotion corroboration—reducing false positives/negatives and improving tradeability.

![Refer to caption](HOUS_Case_study_less_min_days/LPPL_HOUS_F_bubblescore_timeseries1.png)


Figure 4: Daily BubbleScore time series for HOUS with threshold bands and event shading. The sequence of up-crossings in mid-2023, subsequent down-crossings in late-2023, and re-entries above the upper band in early-2024 illustrates the regime rhythm under a unified “behavioral + technical” lens. Peak markers assist rule-based entries, scaling, and profit-taking.

For HOUS, HLPPL (BubbleScore) systematically outperforms a residual-only specification by delivering more robust and tradeable signals. By jointly weighting LPPL residuals with a Hype index and text-based Sentiment, the measure suppresses idiosyncratic fluctuations that typically arise in sideways regimes, thereby lowering false discoveries near decision thresholds. Under a common set of thresholds and minimum-duration constraints, the resulting event windows exhibit sharper temporal boundaries and more consistent lengths, which facilitates rule-based entries, scaling, and exits. Moreover, the framework naturally reconciles technical and behavioral information: when residuals and text indicators align, the score concentrates mass in genuine extremes; when they diverge, the contribution of price-only noise is down-weighted. In aggregate, BubbleScore preserves the sensitivity of LPPL to critical dynamics while producing steadier, operationally actionable signals for housing-exposed strategies.

#### 3.6.2 AMTX Case Study

Aemetis Inc. (AMTX) provides another representative case study for our framework. It is a U.S.-based renewable fuels and biochemicals company founded in 2006 and headquartered in Cupertino, California. It was selected here as an illustrative example due to its unusually large price swings in recent years. From 2018 to 2025, the stock experienced multiple sharp rallies and corrections, making it a natural testbed for assessing the robustness of our BubbleScore methodology on daily data.

![Refer to caption](AMTX_case_study/LPPL_AMTX_C_residual_only.png)


Figure 5: LPPL *residual-only* detection for AMTX. The black line shows the log price and the blue dashed curve the LPPL fit. Green (red) shading marks intervals where prices lie materially above (below) the theoretical path. Distinct positive-bubble episodes appear in 2021–2022, while early-2018 and mid-2020 exhibit pronounced negative-bubble behavior.

![Refer to caption](AMTX_case_study/LPPL_AMTX_D_bubblescore_detection.png)


Figure 6: HLPPL (BubbleScore) detection for AMTX. Relative to residual-only tagging, augmenting with Hype and text-based Sentiment, together with minimum-duration and threshold rules, filters out short-lived spikes and yields cleaner, temporally coherent windows across 2018–2025.

![Refer to caption](AMTX_case_study/LPPL_AMTX_E_signal_comparison.png)


Figure 7: Signal comparison for AMTX: BubbleScore (with Hype & Sentiment) versus residual-only. The series agree on major turning points, but HLPPL is smoother around decision bands (e.g., ±0.4\pm 0.4), exhibits fewer flips in volatile stretches, and down-weights price moves that lack behavioral corroboration—reducing false positives/negatives.

![Refer to caption](AMTX_case_study/LPPL_AMTX_F_bubblescore_timeseries.png)


Figure 8: Daily BubbleScore time series for AMTX with threshold bands and shaded event segments. Peak markers indicate local extremes used for rule-based entries, scaling, and exits; the sequence of up-/down-crossings from 2018 to 2025 reveals a consistent regime structure despite high volatility.

AMTX’s pronounced volatility motivates the use of a longer minimum-duration parameter (min\_days) to prevent short, high-amplitude swings from triggering spurious events. Even under this stricter setting, the framework isolates the core bubble dynamics: BubbleScore identifies the 2021–2022 surges as sustained positive-bubble phases and cleanly separates earlier negative-bubble intervals (early-2018, mid-2020). By jointly weighting LPPL residuals with Hype and Sentiment, BubbleScore preserves sensitivity to LPPL critical dynamics while attenuating noise in choppy markets, delivering sharper window boundaries, fewer threshold flips, and more operationally actionable signals on daily data.

### 3.7 Beyond Technical and Behavioral Indicators

While the Bubble Score integrates LPPL residuals, hype, and sentiment, we acknowledge that certain cases challenge its interpretation. For example, firms with extraordinary fundamentals (e.g., Nvidia between 2018–2022) may exhibit super-exponential price paths that are justified by earnings and innovation rather than speculation. Detecting such “fundamentally supported growth” requires information beyond price dynamics and textual signals.

To address this limitation, we extend the framework in the next section by incorporating machine learning models that combine the Bubble Score with additional market and fundamental features (e.g., valuation ratios, macro indicators). This integration aims to refine detection accuracy, reduce false positives, and identify genuine bubbles versus justified growth trajectories.

## 4 Transformer Model

We develop a supervised learning framework for asset-level bubble detection by integrating traditional econometric tests with deep neural sequence modeling. This hybrid approach captures both statistically-grounded bubble signals and complex temporal patterns embedded in financial time series. The objective of this model is to forecast the bubble intensity (Bubble Score) over the next five trading days.

### 4.1 Model Structure and Training Loss

We begin by constructing a comprehensive set of input features reflecting macroeconomic sentiment, valuation ratios, and market behavior. These include variables such as the Volatility Index (VIX), Hype Index, news sentiment scores (from FinBERT), price-to-earnings (PE) and price-to-book (PB) ratios, as well as raw market signals like closing prices and trading volume. These inputs collectively capture fundamental value, investor psychology, and liquidity dynamics.

Next, the raw time series are normalized and transformed into structured feature matrices to encode temporal dependencies. Each matrix represents a sequence of past values, preserving historical context for downstream modeling.

To fully exploit the heterogeneous nature of the inputs—specifically the coexistence of asset-level features and market-level signals—we employ a Dual-Stream Transformer architecture. One Transformer encoder models stock-specific sequences, while another processes market-wide signals. The dual-stream Transformer framework can jointly models stock-level and market-level information. The input consists of two parallel sequences

|  |  |  |
| --- | --- | --- |
|  | X1:t(s)={x1(s),…,xt(s)},X1:t(m)={x1(m),…,xt(m)},xs(⋅)∈ℝd,X^{(s)}\_{1:t}=\{x^{(s)}\_{1},\ldots,x^{(s)}\_{t}\},\quad X^{(m)}\_{1:t}=\{x^{(m)}\_{1},\ldots,x^{(m)}\_{t}\},\quad x^{(\cdot)}\_{s}\in\mathbb{R}^{d}, |  |

where xs(s)x^{(s)}\_{s} denotes asset-specific features and xs(m)x^{(m)}\_{s} represents market-wide signals.

Each input is linearly projected and enriched with positional information:

|  |  |  |
| --- | --- | --- |
|  | Z(s)=PE​(We(s)​X(s)),Z(m)=PE​(We(m)​X(m)).Z^{(s)}=\mathrm{PE}(W^{(s)}\_{e}X^{(s)}),\qquad Z^{(m)}=\mathrm{PE}(W^{(m)}\_{e}X^{(m)}). |  |

The two sequences are processed by separate Transformer encoders:

|  |  |  |
| --- | --- | --- |
|  | H(s)=Enc(s)​(Z(s)),H(m)=Enc(m)​(Z(m)).H^{(s)}=\mathrm{Enc}^{(s)}(Z^{(s)}),\qquad H^{(m)}=\mathrm{Enc}^{(m)}(Z^{(m)}). |  |

A bi-directional cross-attention mechanism is applied after the independent
encoders to capture interactions between stock-level and market-level
representations. This allows each stream not only to preserve its own temporal
dynamics but also to attend to complementary information from the other,
thereby integrating local asset behavior with broader market context.

Formally, given encoded sequences H(s)H^{(s)} and H(m)H^{(m)}, we compute

|  |  |  |
| --- | --- | --- |
|  | H~(s)=Attn​(H(s)​WQ(s),H(m)​WK(m),H(m)​WV(m)),H~(m)=Attn​(H(m)​WQ(m),H(s)​WK(s),H(s)​WV(s)).\widetilde{H}^{(s)}=\mathrm{Attn}(H^{(s)}W\_{Q}^{(s)},\,H^{(m)}W\_{K}^{(m)},\,H^{(m)}W\_{V}^{(m)}),\qquad\widetilde{H}^{(m)}=\mathrm{Attn}(H^{(m)}W\_{Q}^{(m)},\,H^{(s)}W\_{K}^{(s)},\,H^{(s)}W\_{V}^{(s)}). |  |

The cross-attended representations are then pooled and fused into a joint
feature vector,

|  |  |  |
| --- | --- | --- |
|  | ht=ϕ​(Pool​(H~(s)),Pool​(H~(m))),h\_{t}=\phi\!\big(\mathrm{Pool}(\widetilde{H}^{(s)}),\,\mathrm{Pool}(\widetilde{H}^{(m)})\big), |  |

which serves as the common input for multiple prediction heads that forecast
bubble intensity over the next five trading days:

|  |  |  |
| --- | --- | --- |
|  | y^t+τ=fτ​(ht),τ=1,…,5.\hat{y}\_{t+\tau}=f\_{\tau}(h\_{t}),\qquad\tau=1,\ldots,5. |  |

Model parameters are optimized by minimizing an improved loss function that goes beyond a simple mean squared error and incorporates additional regularization objectives to better capture bubble dynamics. The detailed formulation of this loss will be introduced in a later section.

The architecture explicitly separates stock- and market-level signals, processing them through independent streams before fusing at a later stage.
This design allows the model to capture both fine-grained local dynamics and broader market-wide context in financial time series. To train such a model effectively, we require supervision that not only identifies the presence of bubbles but also reflects their temporal evolution.

For this purpose, we employ the LPPL test to construct continuous labels. The LPPL framework yields a Bubble Score that quantifies the intensity of explosive dynamics in asset prices or trading
volumes. Unlike binary labels, this index captures both bubble and reversal regimes, providing richer supervision and enabling the model to learn nuanced bubble dynamics.

Finally, the fused representations from the dual-stream Transformer are passed to multiple horizon-specific heads, each implemented as a lightweight multi-layer perceptron (MLP) with nonlinear activations and a Tanh output. The MLP serves as a flexible function approximator that maps the high-dimensional hidden representation into scalar Bubble Score forecasts, while its shallow architecture ensures computational efficiency and prevents overfitting. These heads separately forecast the Bubble Score for the next five trading
days, allowing the model to capture horizon-specific dynamics while reducing conflicts in multi-step prediction.

##### Dataset Structure

The dataset is chronologically partitioned into training, evaluation, and test sets in alignment with our three-stage training pipeline. The training set is used exclusively for optimizing model weights. The evaluation set is reserved for hyperparameter tuning, ensuring that parameter choices are not biased by the training data. The test set is employed for final performance assessment. This structured design allows a clear separation of roles—weight learning, hyperparameter selection, and unbiased testing—ensuring methodological rigor and reproducibility.

##### Regularization and Overfitting Prevention

To further enhance generalization under the noisy and volatile conditions of
financial time series, we integrate multiple regularization strategies into
the training process.

First, dropout layers are applied in the input projection, feature fusion,
and prediction heads to reduce neuron co-adaptation, formally:

|  |  |  |
| --- | --- | --- |
|  | h=Dropout​(p)​(f​(x)),p=0.1​–​0.3,h=\mathrm{Dropout}(p)\big(f(x)\big),\qquad p=0.1\text{--}0.3, |  |

where pp denotes the dropout probability.

Second, L2 weight decay is imposed on model parameters to control complexity:

|  |  |  |
| --- | --- | --- |
|  | ℒreg=λ​‖θ‖22,\mathcal{L}\_{\text{reg}}=\lambda\|\theta\|\_{2}^{2}, |  |

which penalizes excessively large weights.

Third, gradient clipping is employed to stabilize updates and prevent exploding
gradients:

|  |  |  |
| --- | --- | --- |
|  | g←g⋅min⁡(1,τ‖g‖2),g\;\leftarrow\;g\cdot\min\!\Big(1,\tfrac{\tau}{\|g\|\_{2}}\Big), |  |

where gg is the raw gradient and τ=0.5\tau=0.5 is the clipping threshold.

In addition, a OneCycleLR schedule dynamically adjusts the learning rate

|  |  |  |
| --- | --- | --- |
|  | ηt=ηmin+12​(ηmax−ηmin)​(1+cos⁡(π​tT)),\eta\_{t}=\eta\_{\min}+\tfrac{1}{2}\big(\eta\_{\max}-\eta\_{\min}\big)\Big(1+\cos(\tfrac{\pi t}{T})\Big), |  |

ensuring smoother convergence. Finally, early stopping monitors validation loss
and halts training once performance plateaus.

Together, these techniques mitigate overfitting and improve the robustness of the learned Bubble Score predictions.

##### Combined Loss Function.

To better capture the complex dynamics of bubbles, we design a combined loss function that integrates multiple complementary objectives rather than relying on a single error metric. Specifically, the overall loss is formulated as a weighted sum of: (i) a Huber loss to provide robustness against outliers, (ii) a correlation loss to encourage alignment between predicted and true temporal patterns, (iii) an R2R^{2}-based loss to directly optimize model fit, (iv) a temporal consistency term to penalize discrepancies in day-to-day changes, and (v) a smoothness regularizer to discourage abrupt fluctuations in predictions. This multi-component formulation improves stability, enhances predictive accuracy, and ensures that the learned Bubble Score trajectories reflect both statistical fidelity and realistic temporal structure.

The overall training objective is defined as a weighted sum of multiple complementary terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=λ1​ℒHuber+λ2​ℒCorr+λ3​ℒR2+λ4​ℒCons+λ5​ℒSmooth,\mathcal{L}=\lambda\_{1}\,\mathcal{L}\_{\text{Huber}}+\lambda\_{2}\,\mathcal{L}\_{\text{Corr}}+\lambda\_{3}\,\mathcal{L}\_{R^{2}}+\lambda\_{4}\,\mathcal{L}\_{\text{Cons}}+\lambda\_{5}\,\mathcal{L}\_{\text{Smooth}}, |  | (15) |

where ℒHuber\mathcal{L}\_{\text{Huber}} denotes the Huber loss for robust regression,
ℒCorr\mathcal{L}\_{\text{Corr}} enforces correlation between predicted and true sequences,
ℒR2\mathcal{L}\_{R^{2}} optimizes the coefficient of determination,
ℒCons\mathcal{L}\_{\text{Cons}} penalizes inconsistency in temporal differences,
and ℒSmooth\mathcal{L}\_{\text{Smooth}} regularizes abrupt changes.

This formulation is motivated by the unique challenges of bubble prediction. Financial bubble dynamics are rare, noisy, and often exhibit abrupt changes, which makes single-objective loss functions insufficient. By combining robustness (Huber), statistical alignment (correlation and R2R^{2}), and temporal structure constraints (consistency and smoothness), the loss function guides the model to not only fit the data accurately but also generate predictions that are stable and economically plausible.

Stock-Level Features(Close Price, Volume,Other Variables)Stock-Level Feature MatrixMarket-Level Features(Hype Index, News Sentiment,Macro Indicators)Market-Level Feature MatrixTransformer ModelMLP HeadsBubble Score PredictionBubble Label(via LPPL)


Figure 9: Transformer-based bubble detection framework with LPPL labeling

As shown in Figure [9](https://arxiv.org/html/2510.10878v1#S4.F9 "Figure 9 ‣ Combined Loss Function. ‣ 4.1 Model Structure and Training Loss ‣ 4 Transformer Model ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model"), stock-level and market-level features are combined into feature matrices and fed into a transformer model. The transformer captures temporal and cross-sectional dependencies, while bubble labels from the LPPL model supervise training. The outputs are then passed to prediction modules.

After the transformer encoder and feature fusion, the model uses multiple lightweight multi-layer perceptron (MLP) heads as prediction modules. Each head is a small feed-forward network that outputs the Bubble Score for one future day. Stacking several heads allows the model to generate multi-day predictions in parallel. In essence, the MLP heads translate the high-dimensional embeddings into task-specific Bubble Score.

### 4.2 Data Processing

This subsection introduces the methodologies processing market and news data for the research.

#### 4.2.1 Sentiment Processing Using FinBERT

To extract sentiment signals from financial news related to the real estate sector, we adopt a structured pipeline that combines BERTopic and FinBERT, as illustrated in Figure [10](https://arxiv.org/html/2510.10878v1#S4.F10 "Figure 10 ‣ 4.2.1 Sentiment Processing Using FinBERT ‣ 4.2 Data Processing ‣ 4 Transformer Model ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model").

WSJ News Corpus(2018–2024)BERTopic Modeling+ Real Estate FilteringFinBERTSentiment ScoringOne-Hot Encoding+ Confidence WeightingDaily AggregatedSentiment VectorTransformer Input


Figure 10: Pipeline for extracting sentiment features using BERTopic and FinBERT.

We begin by applying BERTopic to the WSJ news corpus (2018–2024) to identify and filter news articles relevant to the real estate industry. These filtered articles are then passed to FinBERT, a pre-trained transformer model fine-tuned on financial text, which outputs both a sentiment class prediction y^i,t∈{pos,neu,neg}\hat{y}\_{i,t}\in\{\text{pos},\text{neu},\text{neg}\} and its corresponding confidence score pi,t∈[0,1]p\_{i,t}\in[0,1] for each article ii on date tt.

The predicted class is encoded into a one-hot vector weighted by the model’s confidence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | si,tc={pi,t,if ​y^i,t=c,0,otherwise,for ​c∈{pos,neu,neg}.\displaystyle s\_{i,t}^{c}=\begin{cases}p\_{i,t},&\text{if }\hat{y}\_{i,t}=c,\\ 0,&\text{otherwise},\end{cases}\quad\text{for }c\in\{\text{pos},\text{neu},\text{neg}\}. |  | (16) |

We then aggregate the one-hot weighted vectors across all articles published on day tt to form a daily sentiment feature, normalized by total confidence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Stc=∑i∈Dtsi,tc∑i∈Dtpi,t,for ​c∈{pos,neu,neg}.\displaystyle S\_{t}^{c}=\frac{\sum\limits\_{i\in D\_{t}}s\_{i,t}^{c}}{\sum\limits\_{i\in D\_{t}}p\_{i,t}},\quad\text{for }c\in\{\text{pos},\text{neu},\text{neg}\}. |  | (17) |

where DtD\_{t} is the set of articles published on date tt.

The resulting sentiment vector St=[Stpos,Stneu,Stneg]S\_{t}=[S\_{t}^{\text{pos}},S\_{t}^{\text{neu}},S\_{t}^{\text{neg}}] is used as input to the Transformer model, representing the collective market sentiment derived from the news on that day.

#### 4.2.2 Labeling

Our enhanced framework generates precise temporal labels for bubble episodes through a systematic identification process based on the Bubble Score metric. The labeling methodology operates on two key principles: threshold-based detection and temporal continuity requirements, ensuring robust identification of genuine bubble periods while filtering out transient market noise.

The detection of bubble episodes follows a set of consistent principles:

1. 1.

   Thresholding: A period is flagged whenever |B​u​b​b​l​e​S​c​o​r​e​(t)|>τ|BubbleScore(t)|>\tau, with τ\tau denoting the significance cutoff. In practice, τ\tau is commonly fixed at 0.8 based on empirical calibration.
2. 2.

   Direction Assignment: Normal bubbles are defined when B​u​b​b​l​e​S​c​o​r​e​(t)>−τBubbleScore(t)>-\tau (positive side), whereas negative bubbles are identified when B​u​b​b​l​e​S​c​o​r​e​(t)<−τBubbleScore(t)<-\tau (negative side).
3. 3.

   Persistence: To prevent short-lived fluctuations from being classified as bubbles, only intervals lasting at least dm​i​nd\_{min} trading days (typically dm​i​n=10d\_{min}=10) are retained.
4. 4.

   Persistence: To prevent short-lived fluctuations from being classified as bubbles, only intervals lasting at least dm​i​nd\_{min} trading days (typically dm​i​n=10d\_{min}=10) are retained.
5. 5.

   Episode Construction: Consecutive qualifying days are consolidated into distinct episodes, each described by its start and end dates, duration, and intensity.

Formally, a bubble episode can be represented as

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​u​b​b​l​e​P​e​r​i​o​di={ts,te,t​y​p​e,i​n​t​e​n​s​i​t​y},BubblePeriod\_{i}=\{t\_{s},t\_{e},type,intensity\}, |  | (18) |

where tst\_{s} and tet\_{e} denote the start and end dates, t​y​p​e∈{normal,negative}type\in\{\text{normal},{\text{negative}\}} specifies the bubble orientation, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | i​n​t​e​n​s​i​t​y=maxt∈[ts,te]⁡|B​u​b​b​l​e​S​c​o​r​e​(t)|intensity=\max\_{t\in[t\_{s},t\_{e}]}|{BubbleScore}(t)| |  | (19) |

captures the maximum magnitude observed within the episode.

### 4.3 Feature Selection

The input features are organized into two distinct levels:stock-level features and market-level features. This dual-level design enables the model to simultaneously capture asset-specific dynamics and macro-level market conditions that may jointly drive bubble formation. The training and testing period spans from 2018-01-01 to 2024-12-31.

Stock-level features are designed to reflect short-term price dynamics, trading intensity, and firm-specific valuation signals. Market-level features, on the other hand, capture broader economic sentiment and sector-level fluctuations that can influence speculative behavior across assets.

All numerical features are normalized over the training window. Temporal variables such as year, month, and day are retained as integer-coded features to preserve calendar-related effects. Financial ratios (e.g., P/E, P/S, ROE) are dropped if missing to ensure data integrity.

Sentiment variables derived from FinBERT are encoded as three separate one-hot vectors: sentiment\_Negative, sentiment\_Neutral, and sentiment\_Positive. These are aggregated daily and integrated as market-level signals. This formulation enables the model to detect shifts in investor sentiment polarity and understand market mood.

Table 1: Stock-level feature set used in the Transformer input

| Description | Preprocessing | Normalized |
| --- | --- | --- |
| Closing price of the stock | Log transformation | Yes |
| Trading volume; reflects liquidity and participation | Log transformation | Yes |
| Daily log return: log⁡(Pt/Pt−1)\log(P\_{t}/P\_{t-1}) | Calculated from price | Yes |
| Book-to-market ratio | Drop if missing | No |
| P/E ratio (extraordinary income included) | Drop if missing | No |
| Price-to-sales ratio | Drop if missing | No |
| Return on equity | Drop if missing | No |
| Month extracted from date | Integer encoded | No |
| Day of month | Integer encoded | No |




Table 2: Market-level feature set used in the Transformer input

| Description | Preprocessing | Normalized |
| --- | --- | --- |
| CBOE Volatility Index; market risk proxy | Drop if missing | Yes |
| Mean gross profitability across firms | Drop if missing | Yes |
| Mean ROE across firms | Drop if missing | Yes |
| Sector exposure indicator from Hype Index | Drop if missing | Yes |
| One-hot: negative sentiment (FinBERT) | Aggregated by date | No |
| One-hot: neutral sentiment (FinBERT) | Aggregated by date | No |
| One-hot: positive sentiment (FinBERT) | Aggregated by date | No |

Note: All market-level features (except Hype Index and FinBERT sentiment scores) are sourced from WRDS (Wharton Research Data Services).

This final combination of carefully selected raw metrics and derived valuation/sentiment signals enables the model to capture short-term price and volume fluctuations, valuation shifts, and speculative dynamics, while also retaining calendar and macroeconomic context. The ablation process ensures that only impactful features are retained, avoiding redundancy and improving model generalization.

### 4.4 Performance

The proposed Transformer model was comprehensively evaluated on the held-out test set using multiple complementary metrics to ensure robustness of performance assessment. The evaluation criteria included Pearson correlation, mean squared error (MSE), mean absolute error (MAE), root mean squared error (RMSE), and mean absolute percentage error (MAPE). Each metric provides a different perspective: correlation measures the linear relationship between predicted and actual values, MSE penalizes large deviations more heavily due to squaring, MAE captures the average magnitude of absolute deviations, RMSE reflects error magnitude on the original scale of the data, while MAPE provides interpretability in terms of percentage error.

The model achieved an average Pearson correlation of 0.625 across the five forecast horizons, suggesting that it captures a moderate degree of bubble dynamics. The average MSE and MAE were relatively low at 0.087 and 0.236, respectively, while the RMSE remained at 0.295, demonstrating stable predictive power with respect to absolute deviations. Although the MAPE value was somewhat distorted by near-zero denominators, the other error metrics consistently indicated reasonable predictive accuracy.

Table 3: Performance of Transformer model across evaluation metrics

| Metric | Value |
| --- | --- |
| Correlation | 0.625 |
| Mean Squared Error (MSE) | 0.087 |
| Mean Absolute Error (MAE) | 0.236 |
| Root Mean Squared Error (RMSE) | 0.295 |

![Refer to caption](Transformer/Corr.png)


Figure 11: Scatter plots of predicted versus true Bubble Score values for forecast Day 1 through Day 5.

Furthermore, Figure [11](https://arxiv.org/html/2510.10878v1#S4.F11 "Figure 11 ‣ 4.4 Performance ‣ 4 Transformer Model ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents scatter plots of predicted versus true Bubble Score values for horizons one through five. The observed correlations are relatively stable, ranging from 0.628 on Day 1 to 0.609 on Day 5. This stability suggests that the Transformer model retains predictive capability even at longer horizons. Importantly, the predicted points are closely aligned along the diagonal, implying that the model is capable of accurately capturing both the direction and the magnitude of bubble fluctuations, despite the inherent noise and volatility in financial time series data.

## 5 Trading with Bubble Scores

This section presents the trading strategy and results built on Bubble Score.

### 5.1 BubbleScore Trading Strategy

Building upon our comprehensive Bubble Score framework, we implement a systematic trading strategy that capitalizes on both normal and negative bubble episodes across real estate sector stocks. The strategy leverages our bidirectional bubble detection capability to generate trading signals during periods of systematic mispricing.

#### 5.1.1 Bubble Score-Based Trading Rules

Our trading strategy is driven by threshold-based signals derived from the BubbleScore metric:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​u​b​b​l​e​S​c​o​r​e​(t)​{>0,→Normal Bubble,<0,→Negative Bubble.BubbleScore(t)\begin{cases}\;\;>0,\quad\rightarrow&\text{Normal Bubble},\\ \;\;<0,\quad\rightarrow&\text{Negative Bubble}.\end{cases} |  | (20) |

Positive values indicate normal bubbles, negative values indicate negative bubbles.

where BubbleScore integrates LPPL residuals with behavioral finance indicators, as defined previously.

we define BtB\_{t} as the Bubble Score at time t, trading signals are generated by applying thresholds θ1=0.7\theta\_{1}=0.7 and θ2=0.3\theta\_{2}=0.3 to the normalized Bubble Score series:

1. 1.

   Long Entry: A long position is initiated at time tt if Bt≤−θ1B\_{t}\leq-\theta\_{1}
2. 2.

   Short Entry: A short position is entered at time tt if Bt≥θ1B\_{t}\geq\theta\_{1}.
3. 3.

   Long Exit: Active long positions are closed once the predicted index satisfies Bt≥−θ2B\_{t}\geq-\theta\_{2}.
4. 4.

   Short Exit: Active short positions are closed once the predicted index satisfies Bt≤θ2B\_{t}\leq\theta\_{2}.
5. 5.

   Risk Management: The strategy enforces a 15% stop-loss, caps maximum position size at 50% of capital, and incorporates transaction costs of 0.1%.

### 5.2 Backtest Results

We conduct an extensive backtest across all eligible real estate sector stocks using daily data from CRSP combined with our sentiment and hype indices. Each stock requires a minimum of 100 daily observations to ensure statistical reliability of the LPPL fitting process.

To further validate the effectiveness of our Bubble Score trading strategy, we compare the performance of BBX , CAR, and CSGP, over the same observation window. Figure [12](https://arxiv.org/html/2510.10878v1#S5.F12 "Figure 12 ‣ 5.2 Backtest Results ‣ 5 Trading with Bubble Scores ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents normalized equity curves for both the Bubble Score strategy and the buy-and-hold benchmark across the three stocks.

![Refer to caption](BBX_vs_Peers_SinglePlot.png)


Figure 12: Strategy vs Buy&Hold comparison for 3 selected peers. Solid lines represent strategy returns, while dashed lines represent buy-and-hold portfolio value.

The results highlight several important insights. First, BBX demonstrates outstanding performance, with the Bubble Score strategy consistently and significantly outperforming the buy-and-hold benchmark. This is primarily attributable to BBX’s decreasing trajectory being dominated by normal-bubble. In these regimes, our strategy systematically identified overvaluation and generated profitable short entries, while avoiding prolonged drawdowns. Fundamentally, BBX has also undergone periods of financial distress and restructuring, amplifying the extent of mispricing and thereby increasing the strategy’s relative advantage.

By contrast, the performance of the two peers is less satisfactory. For CSGP, the underlying price trajectory is persistently upward-sloping. While this reflects a fundamentally strong growth story, such monotonic increases reduce the likelihood of detecting large mispricing episodes, limiting the strategy’s profitability relative to buy-and-hold. For CAR, the trajectory is much sharper and more volatile, producing multiple large swings. Although this could, in principle, generate trading opportunities, in practice such sharp oscillations often trigger early exit conditions due to heightened sentiment and hype signals, curtailing the gains that might otherwise accrue.

This comparison underscores both the strengths and limitations of a pure Bubble Score rules-based strategy. It excels in cases such as BBX, where undervaluation episodes are extended and systematic, but struggles in monotonic growth stocks or highly volatile names. These limitations motivate our subsequent development of a machine-learning–enhanced framework, designed to refine signal quality and better adapt to diverse market dynamics.

Table [4](https://arxiv.org/html/2510.10878v1#S5.T4 "Table 4 ‣ 5.2 Backtest Results ‣ 5 Trading with Bubble Scores ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents the performance metrics for the five best-performing stocks under our Bubble Score trading strategy.

Table 4: Top 5 Performing Stocks - Bubble Score Trading Strategy

| Stock | Annualized Return | Max drawdown | Win Rate | Sharpe Ratio |
| --- | --- | --- | --- | --- |
| AMTX | 43.10% | 34.35% | 54.72% | 0.83 |
| BBX | 41.20% | 4.02% | 85.71% | 2.33 |
| HOUS | 39.66% | 21.48% | 66.67% | 1.10 |
| BEEP | 37.64% | 3.38% | 83.33% | 1.44 |
| MP | 32.48% | 11.93% | 82.35% | 1.50 |

Note: all results have been discounted at a continuously compounded rate of 2% per annum to obtain its present value.

Table [5](https://arxiv.org/html/2510.10878v1#S5.T5 "Table 5 ‣ 5.2 Backtest Results ‣ 5 Trading with Bubble Scores ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") summarizes the comprehensive performance across all backtested real estate stocks.

Table 5: Overall Bubble Score Strategy Performance Summary

| Performance Metric | Value |
| --- | --- |
| Total Stocks Analyzed | 32 |
| Stocks with Positive Returns | 30 (93.75%) |
| Stocks with Negative Returns | 2 (6.25%) |
| Average Annualized Return | 16.64% |
| Average Win Rate | 67.41% |
| Average Sharpe Ratio | 0.72 |

The comprehensive backtest results demonstrate exceptional strategy effectiveness with a 93.8% success rate across all tested stocks. The average annualized return of 16.64% significantly outperforms typical market benchmarks, while the average win rate of 67.41% indicates consistent signal quality.

The top-performing stocks showcase the strategy’s potential, with AMTX achieving 43.10% annualized returns and BBX demonstrating exceptional risk-management performance with a Sharpe ratio of 2.33. The strategy successfully captures both overvaluation and undervaluation episodes through our bidirectional Bubble Score framework, validating the integration of behavioral finance indicators with traditional LPPL modeling.

These results provide strong empirical evidence that our enhanced Bubble Score framework translates theoretical bubble detection capabilities into practical investment performance, establishing a robust foundation for systematic trading strategies in the real estate sector.

## 6 Machine Learning Enhanced Trading Strategy

Building upon our traditional Bubble Score methodology, we develop a supervised learning framework that integrates econometric bubble detection with deep neural sequence modeling. Specifically, our machine learning model is a dual-stream Transformer, where one stream processes stock-level temporal dynamics and the other stream encodes market- and sentiment-level information. This hybrid design captures both statistically-grounded bubble signals and complex temporal patterns embedded in financial time series data.

We conduct a backtest to evaluate the effectiveness of the proposed bubble-aware trading strategy on real estate sector stocks. The stock-level daily price and return data are sourced from the CRSP database via WRDS, while the news sentiment signals are derived from the Wall Street Journal (WSJ). Both datasets span the period from January 1, 2018 to December 31, 2024, and are aligned at a daily frequency.

To focus on the real estate industry, we filter firms based on their SIC codes, specifically selecting those with SIC values in 6500, 6512, 6513, 6519, 6531, 6541, 6552, 6798. Here, SIC (Standard Industrial Classification) codes are a four-digit system used by U.S. government agencies to classify industries; the selected codes correspond to real estate operators, developers, agents, and real estate investment trusts (REITs).The backtesting window is set from November 2023 to December 2024, during which the model generates daily trading signals and executes positions accordingly.

### 6.1 Multi-Horizon Prediction Strategy

The forecasting part of the research is carried out using a Transoformer network, a recurrent neural network architecture specifically designed to capture temporal dependencies and long-range patterns in sequential financial data.

Our machine learning framework produces forecasts of the Bubble Score over multiple horizons h∈{1,2,3,4,5}h\in\{1,2,3,4,5\}, where B^t+h\hat{B}\_{t+h} denotes the predicted Bubble Score hh trading days ahead.
This multi-horizon structure allows the strategy to adaptively capture both short-term
transients and medium-term bubble dynamics.

Trading signals are generated by applying symmetric thresholds θ1=0.7\theta\_{1}=0.7 and θ2=0.3\theta\_{2}=0.3 to the normalized prediction series, for a specific h∈{1,2,3,4,5}h\in\{1,2,3,4,5\}:

1. 1.

   Long Entry: A long position is initiated at time tt if B^t+h≤−θ1\hat{B}\_{t+h}\leq-\theta\_{1}, where B^t+h\hat{B}\_{t+h} denotes the machine learning forecast of the Bubble Score hh days ahead.
2. 2.

   Short Entry: A short position is entered at time tt if B^t+h≥θ\hat{B}\_{t+h}\geq\theta.
3. 3.

   Long Exit: Active long positions are closed once the predicted index satisfies B^t+h≥−θ2\hat{B}\_{t+h}\geq-\theta\_{2}.
4. 4.

   Short Exit: Active short positions are closed once the predicted index satisfies B^t+h≤θ2\hat{B}\_{t+h}\leq\theta\_{2}.
5. 5.

   Risk Management: The strategy enforces a 15% stop-loss, caps maximum position size at 50% of capital, and incorporates transaction costs of 0.1%.

   An additional prediction reversal exit is triggered if

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | B^t+h⋅B^t+h+1<0,\hat{B}\_{t+h}\cdot\hat{B}\_{t+h+1}<0, |  | (21) |

   indicating that consecutive forecasts flip signs across horizons. This condition closes any active position to prevent losses from sudden regime shifts.

To evaluate the predictive power of our framework, we implement a multi-horizon backtesting design. For each stock and each trading day tt, the model generates forecasts of the Bubble Score at horizons h∈{1,2,3,4,5}h\in\{1,2,3,4,5\}, corresponding to predictions 11 through 55 trading days ahead. Each horizon-specific forecast B^t+h\hat{B}\_{t+h} is then converted into trading signals using the same symmetric entry and exit thresholds as in the baseline rules, together with stop-loss and transaction cost adjustments. This setup yields five parallel equity curves per stock, allowing us to identify the optimal prediction horizon ex post and to analyze the distribution of horizon-specific performance across the cross-section of assets.

### 6.2 Machine Learning Results

Table [6](https://arxiv.org/html/2510.10878v1#S6.T6 "Table 6 ‣ 6.2 Machine Learning Results ‣ 6 Machine Learning Enhanced Trading Strategy ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents the comprehensive performance metrics for our dual-stream transformer enhanced trading strategy across all eligible real estate sector stocks.

Table 6: Machine Learning Strategy Performance Summary

| Performance Metric | Value |
| --- | --- |
| Average Annualized Return | 34.13% |
| Median Annualized Return | 21.49% |
| Average Win Rate | 72.30% |
| Average Sharpe Ratio | 1.19 |

The machine learning enhanced strategy demonstrates superior performance compared to traditional approaches, achieving an average annualized return of 34.13% with an average Win rate of 72.30%. The median return of 21.49% indicates robust performance across the majority of tested stocks, while the average Sharpe ratio of 1.19 reflects strong return efficiency.

Table [7](https://arxiv.org/html/2510.10878v1#S6.T7 "Table 7 ‣ 6.2 Machine Learning Results ‣ 6 Machine Learning Enhanced Trading Strategy ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") presents the distribution of optimal prediction horizons across all analyzed stocks, revealing strategic insights into market timing preferences.

| Prediction Horizon | Percentage of Stocks |
| --- | --- |
| Day 1 | 16.7% |
| Day 2 | 20.8% |
| Day 3 | 8.3% |
| Day 4 | 25.0% |
| Day 5 | 29.2% |

Table 7: Distribution of Optimal Prediction Horizons across analyzed stocks.

The analysis shows that Day 5 predictions account for the largest share (29.2%) of optimal horizons, suggesting that slightly longer short-term forecasts are particularly effective in capturing market dynamics. Day 4 horizons follow closely at 25.0%, highlighting that medium-range signals also provide substantial predictive value. By contrast, Day 1 and Day 3 horizons represent only 16.7% and 8.3% of cases respectively, implying that very short-term forecasts may capture only transient inefficiencies. Overall, the distribution indicates that the strategy performs most effectively when focusing on horizons of 4–5 days, where temporary mispricings and behavioral patterns are more reliably detected and exploited.

#### 6.2.1 Exceptional Performance Case Study: HOUS

Our empirical analysis demonstrates that certain individual stocks exhibit exceptional responsiveness to machine learning–enhanced bubble detection. HOUS serves as a particularly compelling case study, achieving outstanding returns across multiple prediction horizons and consistently outperforming both buy-and-hold and the S&P 500 benchmark.

Table [8](https://arxiv.org/html/2510.10878v1#S6.T8 "Table 8 ‣ 6.2.1 Exceptional Performance Case Study: HOUS ‣ 6.2 Machine Learning Results ‣ 6 Machine Learning Enhanced Trading Strategy ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") reports the comprehensive performance analysis of HOUS across all five prediction horizons, together with benchmark comparisons.

Table 8: HOUS Performance Across All Prediction Horizons and Benchmarks

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Strategy | Cumulative | Annualized | Max | Sharpe | Win | Trades |
|  | Return | Return | Drawdown | Ratio | Count | Count |
| Day 1 | 92.58% | 79.29% | 7.03% | 2.36 | 3 | 3 |
| Day 2 | 92.58% | 79.29% | 7.03% | 2.36 | 3 | 3 |
| Day 3 | 52.51% | 45.64% | 2.51% | 1.81 | 2 | 2 |
| Day 4 | 98.62% | 84.29% | 7.03% | 2.45 | 3 | 3 |
| Day 5 | 100.45% | 85.80% | 7.03% | 2.49 | 3 | 3 |
| Buy-hold | -35.63% | -32.46% | 62.40% | -0.54 | – | – |
| S&P 500 Benchmark | 31.73% | 27.22% | 8.49% | 1.87 | – | – |

This case study highlights the transformative potential of integrating behavioral indicators and machine learning into bubble-based trading strategies. HOUS achieves nearly triple-digit cumulative returns across all horizons, with Sharpe ratios exceeding 2.0 in multiple cases, a performance level that far surpasses traditional benchmarks. Notably, the strategy maintains very shallow drawdowns (below 8%) despite the high level of return, showcasing superior risk-adjusted resilience.

Equally important, the consistency of results across all five horizons suggests that the model captures robust underlying dynamics rather than isolated statistical artifacts. Compared to the buy-and-hold strategy and the S&P 500, which yield modest annualized returns of around 11–13% with substantially higher drawdowns, the machine learning–enhanced approach demonstrates clear superiority. This evidence underscores both the robustness and the practical applicability of our framework, particularly in stock-specific optimization where stocks like HOUS exhibit exceptional alignment with bubble-based predictive signals.

### 6.3 Strategy Result and Comparison

Table [9](https://arxiv.org/html/2510.10878v1#S6.T9 "Table 9 ‣ 6.3 Strategy Result and Comparison ‣ 6 Machine Learning Enhanced Trading Strategy ‣ Identifying and Quantifying Financial Bubbles with the Hyped Log-Periodic Power Law Model") compares the performance metrics between our traditional Bubble Score strategy and the machine learning enhanced approach.

Table 9: Strategy Performance Comparison

| Performance Metric | Traditional Strategy | ML Enhanced Strategy |
| --- | --- | --- |
| Average Annualized Return | 16.64% | 34.13% |
| Average Win Rate | 67.41% | 72.30% |
| Average Sharpe Ratio | 0.72 | 1.19 |
| Average Max Drawdown | 15.54% | 11.35% |

The machine learning enhanced strategy achieves a 17.49% improvement in average annualized returns (34.13% vs 16.64%) while achieving a higher Sharpe ratio (1.19 vs 0.72 ). the ML approach generates higher absolute returns when successful, resulting in superior overall performance.

## 7 Conclusion

This study introduces the Hyped Log-Periodic Power Law (HLPPL) Model, a unified framework for detecting bubbles and negative bubbles by integrating LPPL residual dynamics with media attention and sentiment indicators through a dual-stream Transformer. The empirical analysis shows that the prediction module achieves a mean Pearson correlation of 0.625 with the Bubble Score (MSE = 0.087; RMSE = 0.295), reflecting stable alignment with the targeted dynamics. When implemented as a trading strategy, the machine-learning–enhanced approach generates an average annualized return of 34.13% with an average Sharpe ratio of 1.19, significantly outperforming the traditional Bubble Score rules strategy, which delivers 16.64% annualized return and a Sharpe ratio of 0.72. Sector-wide validation further confirms robustness, with positive returns in 30 out of 32 tested stocks, while stock-specific optimization yields striking outcomes: for instance, the strategy attains a 85.80% annualized return (Sharpe 2.49) for HOUS.

Beyond performance, the HLPPL framework advances bubble research by shifting from retrospective detection to forward-looking prediction, enabling proactive risk management and more reliable signal extraction. By embedding behavioral and textual dimensions into the LPPL structure, the methodology provides a statistically grounded yet practically actionable tool for investors and policymakers. Future extensions will broaden the empirical scope beyond real estate, refine prediction horizons, and incorporate additional macro-financial indicators to further enhance real-time monitoring and decision-making.

## References

* [1]

  John Y. Campbell and Robert J. Shiller.
  Stock Prices, Earnings, and Expected Dividends.
  The Journal of Finance 43(3):661–676, 1987.
* [2]

  Zheng Cao and Helyette Geman.
  A Hype-Adjusted Probability Measure for NLP Stock Return Forecasting.
  Frontiers in Artificial Intelligence 8:1527180, 2025.
  doi:10.3389/frai.2025.1527180.
* [3]

  Zheng Cao, Wanchaloem Wunkaew, and Helyette Geman.
  The Hype Index: an NLP-driven Measure of Market News Attentions.
  arXiv preprint arXiv:2506.06329, 2025.
* [4]

  Paul Glasserman and Harry Mamaysky.
  Does Unusual News Forecast Market Stress?
  The Journal of Financial and Quantitative Analysis 54(5):1937–1974, 2019.
* [5]

  Robert A. Jarrow, Philip Protter, and Kazuhiro Shimbo.
  Asset Price Bubbles in Incomplete Markets.
  Mathematical Finance 20(2):145–185, 2010.
* [6]

  Anders Johansen, Olivier Ledoit, and Didier Sornette.
  Crashes as critical points.
  International Journal of Theoretical and Applied Finance 3(2):219–255, 2000.
* [7]

  L. Lin, R. E. Ren, and D. Sornette.
  The volatility-confined LPPL model: A consistent model of ‘explosive’ financial bubbles with mean-reverting residuals.
  International Review of Financial Analysis 33:210–225, 2014.
  doi:10.1016/j.irfa.2014.02.012.
* [8]

  Aktham Maghyereh and Hussein Abdoh.
  Can news-based economic sentiment predict bubbles in precious metal markets?
  Financial Innovation 8(1):1–20, 2022.
  doi:10.1186/s40854-022-00341-w.
* [9]

  Peter C. B. Phillips, Shuping Shi, and Jun Yu.
  Testing for multiple bubbles: Historical episodes of exuberance and collapse in the S&P 500.
  International Economic Review 56(4):1043–1078, 2015.
  doi:10.1111/iere.12132.
* [10]

  Adam Hale Shapiro, Moritz Sudhof, and Daniel Wilson.
  Measuring News Sentiment.
  Working Paper 2017-01, Federal Reserve Bank of San Francisco, 2017.
  https://www.frbsf.org/wp-content/uploads/wp2017-01.pdf.
* [11]

  Didier Sornette and Peter Cauwels.
  Financial Bubbles: Mechanisms and Diagnostics.
  Review of Behavioral Economics 4(3):279–305, 2017.
  doi:10.1561/105.00000066.
* [12]

  Paul C. Tetlock.
  Giving Content to Investor Sentiment: The Role of Media in the Stock Market.
  The Journal of Finance 62(3):1139–1168, 2007.
  doi:10.1111/j.1540-6261.2007.01232.x.