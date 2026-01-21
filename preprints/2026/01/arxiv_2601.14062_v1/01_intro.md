---
authors:
- Payel Sadhukhan
- Samrat Gupta
- Subhasis Ghosh
- Tanujit Chakraborty
doc_id: arxiv:2601.14062v1
family_id: arxiv:2601.14062
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Demystifying the trend of the healthcare index: Is historical price a key
  driver?'
url_abs: http://arxiv.org/abs/2601.14062v1
url_html: https://arxiv.org/html/2601.14062v1
venue: arXiv q-fin
version: 1
year: 2026
---


Payel Sadhukhan

Samrat Gupta

Subhasis Ghosh

Tanujit Chakraborty
Army Institute of Management, Kolkata, India
Indian Institute of Management, Ahmedabad, India
ICFAI University, Tripura, India
SAFIR, Sorbonne University, Abu Dhabi, UAE
Sorbonne Center for AI, Paris, France

###### Abstract

Healthcare sector indices consolidate the economic health of pharmaceutical, biotechnology, and healthcare service firms. The short-term movements in these indices are closely intertwined with capital allocation decisions affecting research and development investment, drug availability, and long-term health outcomes. This research investigates whether historical open–high–low–close (OHLC) index data contain sufficient information for predicting the directional movement of the opening index on the subsequent trading day. The problem is formulated as a supervised classification task involving a one-step-ahead rolling window. A diverse feature set is constructed, comprising original prices, volatility-based technical indicators, and a novel class of nowcasting features derived from mutual OHLC ratios. The framework is evaluated on data from healthcare indices in the U.S. and Indian markets over a five-year period spanning multiple economic phases, including the COVID-19 pandemic. The results demonstrate robust predictive performance, with accuracy exceeding 0.8 and Matthews correlation coefficients above 0.6. Notably, the proposed nowcasting features have emerged as a key determinant of the market movement. We have employed the Shapley-based explainability paradigm to further elucidate the contribution of the features: outcomes reveal the dominant role of the nowcasting features, followed by a more moderate contribution of original prices. This research offers a societal utility: the proposed features and model for short-term forecasting of healthcare indices can reduce information asymmetry and support a more stable and equitable health economy.

###### keywords:

healthcare index , predicting rise or fall of index , nowcasting , technical indicators , machine learning

## 1 Introduction

A healthcare index is an aggregate of stocks from leading drug manufacturers, healthcare companies, and biotechnology firms. While its fluctuations primarily interest traders and investors tracking financial markets, the index holds broader relevance for societal well-being (Mazzucato and Parris, [2015](https://arxiv.org/html/2601.14062v1#bib.bib1)). The rise or fall of this class of indices serves as a key indicator for real-time understanding of society’s well-being at large, reflecting and influencing a range of diverse aspects, including public health outcomes, economic consequences, and national security and ethics (Gabe et al., [2015](https://arxiv.org/html/2601.14062v1#bib.bib2)).

It is a powerful indicator and influencer of the state’s and the public’s interest in medical innovation, competency, and societal health (Ward et al., [2021](https://arxiv.org/html/2601.14062v1#bib.bib3); Yach, [2016](https://arxiv.org/html/2601.14062v1#bib.bib4)). A sustained upward trend is often rooted in successful clinical trial results 111<https://www.ainvest.com/news/eli-lilly-stock-soars-10-5-positive-diabetes-drug-trial-market-uncertainty-2508/>, regulatory approvals for new drugs 222<https://brandfinance.com/press-releases/covid-19-vaccine-race-boosts-brand-values-across-pharma-giants> (Pineiro-Chousa et al., [2022](https://arxiv.org/html/2601.14062v1#bib.bib5)), or breakthroughs in treating widespread or life-threatening diseases 333<https://www.investopedia.com/s-and-p-500-gains-and-losses-today-apple-stock-climbs-eli-lilly-slumps-after-disappointing-trial-results-11787193> (Kapar et al., [2022](https://arxiv.org/html/2601.14062v1#bib.bib6)). The persistence of growth can also be attributed to the stability of the economic policies underpinning the domain (Dierks et al., [2016](https://arxiv.org/html/2601.14062v1#bib.bib7); Lakdawalla, [2018](https://arxiv.org/html/2601.14062v1#bib.bib8)).

The understanding of the rise and fall of healthcare index, whether national or global, requires deciphering of two distinct facets: i] long-term events and ii] short-term fluctuations. Long-term events typically stem from foundational changes in the sector’s landscape, including events such as drug approvals, landmark economic policy shifts, new disease prevalence, or major patent expirations. The onset of this class of events and their impact on the index can be anticipated through a qualitative understanding of the demographic and sectoral aspects (Dierks et al., [2016](https://arxiv.org/html/2601.14062v1#bib.bib7)), providing stakeholders with an extended timeframe for strategic response. Conversely, the short-term facets are predominantly driven by day-to-day index movements and fluctuations over a time period. Having a semantical interpretation of these movements and their causation is notably more complex, as they are influenced by a confluence of multidimensional aspects, such as investor sentiment, market reactions, and liquidity conditions (Beniwal et al., [2024](https://arxiv.org/html/2601.14062v1#bib.bib9); Weng et al., [2017](https://arxiv.org/html/2601.14062v1#bib.bib10)).

Given this critical yet challenging nature of short-term fluctuations, we focus on deciphering the randomness in the above-stated *noise element*. Table [1](https://arxiv.org/html/2601.14062v1#S1.T1 "Table 1 ‣ 1 Introduction ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") shows the average diurnal volatilities of different sectoral indices in the USA and the Indian market. The technical formulations for calculating volatility can be found in  [A](https://arxiv.org/html/2601.14062v1#A1 "Appendix A Volatility Computation ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?"). Cyclical sectors, such as banks and the automobile industry, exhibit volatile swings with economic booms and busts (Stratimirović et al., [2018](https://arxiv.org/html/2601.14062v1#bib.bib11); Horvath, [1998](https://arxiv.org/html/2601.14062v1#bib.bib12)). In contrast, healthcare indices exhibit lower volatility due to the ever-lasting requirement for medicines and associated supplies (Li et al., [2024](https://arxiv.org/html/2601.14062v1#bib.bib13)). This inherent stability suggests that the movement of healthcare indices may contain a predictable pattern and is camouflaged by the apparent chaos of the daily movement. Therefore, instead of seeking a semantic interpretation of fluctuations in the long-term movements, we aim to model the movement of the healthcare index by estimating the information contained in the short-term movement of the raw price indices.

Table 1: Sectoral volatilities in USA and Indian markets

|  |  |  |
| --- | --- | --- |
| Sectors | U.S.A. | India |
|  | Close index | Close index |
| Finance | 0.60 | 0.56 |
| IT | 22.06 | 0.52 |
| Oil and Gas | 0.53 | 0.53 |
| Healthcare | 0.42 | 0.39 |

Machine Learning (ML) possesses the capability to understand deep dependencies and patterns among data aspects and is often used in forecasting (Sengupta et al., [2025](https://arxiv.org/html/2601.14062v1#bib.bib14)). ML helps in discovering latent dependencies that may otherwise go unnoticed in human perception (Alpaydin, [2021](https://arxiv.org/html/2601.14062v1#bib.bib15)). The low volatility and non-cyclicality of the healthcare sector lead to reliable and less random patterns (Furnback et al., [2013](https://arxiv.org/html/2601.14062v1#bib.bib16)). These patterns can be efficiently recognized by ML methods and subsequently utilized to make efficient predictions of upcoming trends (Wang et al., [2025](https://arxiv.org/html/2601.14062v1#bib.bib17)). The veracity of predictions can aid in investment-related decision-making, guiding investors on when to invest in stocks from the healthcare domain (Kraus and Feuerriegel, [2017](https://arxiv.org/html/2601.14062v1#bib.bib18)). The development of an ML model that can provide accurate insight into the rise or fall of the next day’s open index for the healthcare sector will have high utility for traders investing in this domain.

The primary research question addressed in this work is — *Can we find out the key drivers of healthcare indices and build interpretable ML models to predict the rise or fall in healthcare indices?*
  
The close intertwining between this sector’s index movement and societal developments, along with the diminished cyclicality of the sector, motivates us to develop an ML model for capturing the association between the historical indices and the upcoming rise or fall of the trend in this sector (Furnback et al., [2013](https://arxiv.org/html/2601.14062v1#bib.bib19)). Our methodology begins by deriving the target class, *rise* or *fall*. This is obtained by computing the difference between the open index of the upcoming trading day and the indices of the current trading day. Although the open index for the upcoming trading day is unknown in practice, we construct a labeled dataset from historical records, thereby framing a supervised classification problem. A model’s performance is fundamentally rooted in its data. For a model to perform well, careful feature engineering is required; features must associate strongly with the target class – in this case, the rise/fall of the indices. To this end, we explore the role of historical momentum as well as current day market context.
We begin by including the raw OHLC prices of the current trading day in the feature set. In addition, we engineer two complementary classes of features from the raw prices as well. One class of these features focuses on raw prices of multiple previous days and includes volatility-focused parameters trusted by traders, namely Bollinger Bands, Keltner Channels, and Donchian Channels. These indicators are built on the statistical summarization of historical data, inherently introducing a lag (Wilms et al., [2021](https://arxiv.org/html/2601.14062v1#bib.bib20)). They provide glimpses of past market behavior, but there is no near-real-time snapshot of current market conditions. To address this limitation and provide a near-real-time snapshot, we design a new class of features. It comprises the mutual ratios of the current day’s index set and serves as a nowcasting tool in the working features set. The ratios provide a detailed picture of the current day’s market movement and serve as a vital clue for predicting the next day’s open index. In essence, the feature set consists of complementary market signals at different temporal scales.

Data source is a foundational component of any meaningful analysis (Sadhukhan and Gupta, [2025](https://arxiv.org/html/2601.14062v1#bib.bib21)). In this research, we have utilized sectoral data from the healthcare domains of the US and Indian Markets. The daily indices (open, close, high, and low) from April 1, 2019, to March 31, 2024, are considered for both countries. This five-year period spans diverse market phases, including the COVID-19 pandemic, thereby providing a comprehensive test of our models. The choice of these two markets is deliberate and is included to enhance the generalizability of our findings. The U.S. healthcare market, valued at approximately USD 640 billion in 2024, is largely driven by breakthrough R&\&D innovations, company mergers, and patent-protected drugs. In contrast, the Indian market, valued at approximately 65 billion the same year, is dominated by generic drug production, rising healthcare needs, lifestyle diseases, and volume-driven sales. These structurally divergent aspects allow us to identify cross-market trends, volatility patterns, and macroeconomic linkages that are crucial for validating the ML models trained on them. An array of diversified classifiers is employed in this study to decipher the relationship between the engineered features and the target class. We have evaluated the correctness of predictions using *accuracy* and *Mathews Correlation Coefficient (MCC) scores*. The latter, in particular, provides a balanced measure of classification performance, particularly when class distributions are imbalanced.
The empirical evaluation shows that our feature-engineered model yields predictions with substantial veracity. The models consistently achieved MCC scores greater than 0.6 and accuracy scores greater than 0.8 on the held-out test data, indicating strong predictive capability beyond random chance. The key contributions of this work do not end with the numbers, as the results democratize the forecasting; the training data is obtained from open OHLC data. Additionally, this research also prioritizes the transparency of the learned model. To this end, we employ Shapley values Lundberg and Lee ([2017](https://arxiv.org/html/2601.14062v1#bib.bib22)), a feature-explainability paradigm, to deconstruct the outputs of our models. This paradigm quantifies the contribution of each feature and helps us understand the utility of different genres of features employed in this research.

The key contributions of this research are multifold. Firstly, to the best of our knowledge, this research is the first to model raw open-high-low-close (OHLC) signals to predict the open index on the next trading day. Secondly, the integration of the Shapley paradigm metamorphoses the procedure from a black box into a transparent tool for understanding the drivers of the healthcare indices. Finally, the research renders societal impact. It democratizes forecasting: the entire dataset is derived from publicly available OHLC data, extending sophisticated analysis to the general public (and beyond the learned stakeholders).

The rest of this paper is organized as follows. In the next section, we describe the related works. In Section 3, we elaborate on the methodology for data sculpting. Sections 4 elaborates on the data source and computational methodology. In Sections 5 and 6, we present the experimental results and their discussion, respectively. We conclude the paper in Section 7.

## 2 Related Works

Stock markets form the backbone of modern economies (Dow and Gorton, [1997](https://arxiv.org/html/2601.14062v1#bib.bib23); Sufian and Chong, [2008](https://arxiv.org/html/2601.14062v1#bib.bib24)), serving as a critical indicator of a nation’s financial health. For decades, researchers have been intrigued by the interplay of factors that drive market fluctuations (Fama, [1965](https://arxiv.org/html/2601.14062v1#bib.bib25); Lin and Marques, [2024](https://arxiv.org/html/2601.14062v1#bib.bib26)), which is akin to a puzzle lying at the intersection of data and human behavior (Daniel et al., [1998](https://arxiv.org/html/2601.14062v1#bib.bib27)). The early days of investigation encompassed aspects like macroeconomic fundamentals and the exploration of investor psychology and market sentiment (Manahov and Hudson, [2013](https://arxiv.org/html/2601.14062v1#bib.bib28); Schmeling, [2009](https://arxiv.org/html/2601.14062v1#bib.bib29); Baker and Wurgler, [2007](https://arxiv.org/html/2601.14062v1#bib.bib30), [2006](https://arxiv.org/html/2601.14062v1#bib.bib31)). (Manahov and Hudson, [2013](https://arxiv.org/html/2601.14062v1#bib.bib28)) explored the herding mentality of investors, which is deemed a significant cause of stock volatility, leptokurtosis, and non-IIDness. (Schmeling, [2009](https://arxiv.org/html/2601.14062v1#bib.bib29)) investigated the association between investors’ sentiment and stock returns and found a negative correlation. Their study suggests that a high confidence rendered a lower return in the future. (Baker and Wurgler, [2007](https://arxiv.org/html/2601.14062v1#bib.bib30)) built their research narrative around investors’ sentiment in a top-down approach, focusing on aggregate sentiment and tracing its effects on the market and individual stocks. Their research reveals a differential effect of sentiment on different stocks: low-capitalization, unprofitable, highly volatile, and young stocks are more vulnerable to investor sentiment. The findings of (Baker and Wurgler, [2006](https://arxiv.org/html/2601.14062v1#bib.bib31)) are in congruence with the former, revealing that investor sentiment shows a stronger effect on securities whose valuations are highly subjective and difficult to arbitrage.

More recently, a paradigm shift has been observed, with researchers increasingly turning to sophisticated quantitative and statistical tools to decode market behavior (Gandhmal and Kumar, [2019](https://arxiv.org/html/2601.14062v1#bib.bib32); Schwert, [1990](https://arxiv.org/html/2601.14062v1#bib.bib33)). This movement, coupled with advances in computational power and the availability of financial datasets, shifted the focus from qualitative theories to the identification of empirical patterns hidden in the noise (Gottschlich and Hinz, [2014](https://arxiv.org/html/2601.14062v1#bib.bib34)). (Bouchaud et al., [2002](https://arxiv.org/html/2601.14062v1#bib.bib35)) investigated three liquid stocks of the Paris Bourse. The study showed that incoming limit order prices follow a scaling behavior around the current price, with a diverging mean. This reflects market participants’ belief that very large price variations can occur within a relatively short period. (Lai and Cho, [2016](https://arxiv.org/html/2601.14062v1#bib.bib36)) focused on comparing the effectiveness of independent indicators — such as price-to-sales, market-to-book, earnings per share, dividend yield, and market capitalization — against the dependent variable of stock returns. The study remained inconclusive regarding the degree of correlation of the factors with the stock returns, but it paved the way for understanding the coaction of the factors. The study in (Bai et al., [2015](https://arxiv.org/html/2601.14062v1#bib.bib37)) explored the applicability of the stochastic dominance statistic for diametrically opposite categories of investors – risk avertors and risk takers, and analyzed the dominance relation in the US and Chinese markets.

Recently, with the advent of computational tools, attention shifted to automating the learning process (Chen et al., [2003](https://arxiv.org/html/2601.14062v1#bib.bib38)). (Kraus and Feuerriegel, [2017](https://arxiv.org/html/2601.14062v1#bib.bib18)) used long-term and short-term memory aspects of RNN for text mining on the organizations’ announcements and their effect on the rise or fall of stock prices. (Jiang et al., [2022](https://arxiv.org/html/2601.14062v1#bib.bib39)) integrated empirical model decomposition and extreme learning machine to render an efficient model for stock prediction. (Kyriakou et al., [2021](https://arxiv.org/html/2601.14062v1#bib.bib40)) used a nonparametric smoother with the covariates (the smoothing parameter selected by cross-validation) to forecast the long-term returns of stocks. A tensor-based framework is introduced in (Li et al., [2016](https://arxiv.org/html/2601.14062v1#bib.bib41)), where the goal is to capture the individual associations between multiple information sources and the rise and fall of stock prices. (Yang et al., [2023](https://arxiv.org/html/2601.14062v1#bib.bib42)) explored the voice calls of managers and used a two-stage deep learning model to reduce the forecast errors, thereby yielding economic advantages in options trading. (Lee et al., [2024](https://arxiv.org/html/2601.14062v1#bib.bib43)) is research along the same line, which incorporates Environmental, Social, and Governance (ESG) sentiment and technical indicators to predict stock market behavior. (Wang et al., [2025](https://arxiv.org/html/2601.14062v1#bib.bib44)) has proposed a self-adaptive trading strategy that is based on ML-based stock prediction. Despite the high volume of research on the aggregated market, its practical utility has often been limited. Consequently, scholars have shifted to sector-specific analysis.

The stock market aggregates stocks from different sectors. The phenomenon of volatility change is not uniform and depends on the sectoral composition. Consequently, a substantial segment of the literature is devoted to unraveling and understanding this variance. Several studies have investigated the sectoral volatility of nation and region-specific exploration. (Hammoudeh et al., [2009](https://arxiv.org/html/2601.14062v1#bib.bib45)) studied the volatility fluctuations of equity sectors of the Gulf market, while (Mensi et al., [2021](https://arxiv.org/html/2601.14062v1#bib.bib46)) explored the impact of geopolitical events on sector-specific volatility spillovers in the US market. The study of volatility and its spillover leads to the demarcation of cyclical and defensive sectors. The defensive sectors are driven by consistent, day-to-day needs like consumer staples and healthcare 444<https://www.alliancebernstein.com/corporate/en/insights/investment-insights/healthcare-stocks-an-innovative-antidote-for-volatile-times.html>. Their low β\beta-value (measures its volatility and systematic risk compared to the overall market) manifests a lower level of fluctuations and weaker co-movement with the whole market (Chen et al., [2018](https://arxiv.org/html/2601.14062v1#bib.bib47)).
In recent years, several studies have examined the factors influencing the movement of healthcare and pharmaceutical stocks (Wang et al., [2025](https://arxiv.org/html/2601.14062v1#bib.bib17)). However, the current literature remains limited in scope: i] It examines only a few individual stocks without considering sectoral dynamics, and ii] It lacks an integrated understanding of the factors influencing sectoral index movements. To bridge this gap, our research aims to understand the role of different types of features related to the index movement of the healthcare sector and to identify those that correlate strongly with it.

## 3 Methodology for data sculpting

### 3.1 Motivation

The accurate prediction of the upcoming movement of the healthcare index through the knowledge of historical data can help investors make informed financial decisions. In this research, we extract information from prior data (indices) and use it to build a model to predict the upcoming trend (increase or decrease) in the open indices. For this task, we consider several feature genres. In our data, each row corresponds to a working day with the market being open, and each column represents a distinct feature used in the task. The upcoming subsections describe how the class label and the features are constructed.

### 3.2 Data labeling

In this work, we predict the rise/ fall of the upcoming trading day’s open index of the healthcare sector with respect to its previous day’s index. Note that there are four sets of indices, and we can obtain four distinct class labels by comparing the indices of a day with the opening index of the next day. Hence, we generate four different class labels –yopop​(t){{y}}\_{\text{op}}^{\text{op}}(t), yhiop​(t){{y}}\_{\text{hi}}^{\text{op}}(t), yloop​(t){{y}}\_{\text{lo}}^{\text{op}}(t), and yclop​(t){y}\_{\text{cl}}^{\text{op}}(t) by comparing the open index of Day (t+1)(t+1) with the open (o​pop), high (h​ihi), low (l​olo) and close (c​lcl) indices of Day (t)(t) respectively. Let Pop​(t)\text{P}\_{\text{op}}(t) denote the open index of Day (t)(t). We will train a dedicated classifier for each class label (elaborated in Section [4.2](https://arxiv.org/html/2601.14062v1#S4.SS2 "4.2 Method ‣ 4 Data Source and Computational Methodology ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?")). The generic formula for obtaining Classopop​(t){\text{Class}}\_{\text{op}}^{\text{op}}(t) is given below.

|  |  |  |  |
| --- | --- | --- | --- |
|  | yopop​(t)={1if Pop​(t+1)>Pop​(t)0otherwise{{y}}\_{\text{op}}^{\text{op}}(t)=\begin{cases}1&\text{if }\text{P}\_{\text{op}}(t+1)>\text{P}\_{\text{op}}(t)\\ 0&\text{otherwise}\end{cases} |  | (1) |

Similarly, we can compute the class labels yhiop​(t){{y}}\_{\textrm{hi}}^{\textrm{op}}(t), yloop​(t){{y}}\_{\textrm{lo}}^{\textrm{op}}(t), and yclop​(t){{y}}\_{\textrm{cl}}^{\textrm{op}}(t) by comparing the Pop​(t+1)\text{P}\_{\text{op}}(t+1) with Phi​(t)\text{P}\_{\text{hi}}(t), Plo​(t)\text{P}\_{\text{lo}}(t) and Pcl​(t)\text{P}\_{\text{cl}}(t), respectively.

Illustration: To generate the class label of Day 1 for open-high difference, denoted by yhiop​(1){{y}}\_{\textrm{hi}}^{\textrm{op}}(1), we compare Pop​(2)\text{P}\_{\text{op}}(2) with Phi​(1)\text{P}\_{\text{hi}}(1): if Pop​(2)>Phi​(1)\text{P}\_{\text{op}}(2)>\text{P}\_{\text{hi}}(1), class label is set to 1, and 0, otherwise.

Note that, while predicting for Day (t+1)(t+1), we will not know the indices of Day (t+1)(t+1) (as they are forthcoming). The task will be to predict if the class label is 1 (if the open index of Day (t+1)(t+1) will exceed the previous day’s index) or 0 (if the open index of Day (t+1)(t+1) will be less than the previous day’s index) based on the previous day’s (Day tt) indices. This data labeling converts the problem of forecasting into a supervised learning one.
  
*Significance*: The model’s significance lies in its predictive timing: it can forecast the direction of the next day’s opening price yop\*(t)){{y}}\_{\text{op}}^{\text{\*}}(t)) as soon as the current trading day closes. It is because the features needed for the next day’s prediction are finalized at the market closing of the current day. The prior information about the market’s movement can help the stakeholders make their investment decisions.

### 3.3 Intrinsic features

The intrinsic features for a day are obtained from the immediately previous day’s open, high, low, and close indices. The indices of Day tt serve as the intrinsic feature for Day tt. With four distinct index types present, we obtain four intrinsic features.
Let the intrinsic feature set of Day tt be denoted by 𝐱int​(t)\mathbf{x}\_{\text{int}}(t).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱int​(t)=[Pop​(t),Phi​(t),Plo​(t),Pcl​(t)]⊤\mathbf{x}\_{\text{int}}(t)=[\textrm{P}\_{\textrm{op}}(t),\textrm{P}\_{\textrm{hi}}(t),\textrm{P}\_{\textrm{lo}}(t),\textrm{P}\_{\textrm{cl}}(t)]^{\top}\quad |  | (2) |

Illustration: If we consider July 19, 2024 (working day) as Day tt, the indices of July 19, 2024, constitute the intrinsic features of Day tt. The task is to predict if the open index will rise or fall at Day (t+1)(t+1). The intrinsic features offer a snapshot of the immediately available market scenario in its crude form. They can offer important facets into the upcoming market scenario, but are usually suboptimal in elucidating the gross market behavior.

### 3.4 Volatility

Volatility in markets is perceived to be a crucial determinant of the index movements by traders (Yousaf and Yarovaya, [2022](https://arxiv.org/html/2601.14062v1#bib.bib48); Yadava, [2024](https://arxiv.org/html/2601.14062v1#bib.bib49)). To this end, we include the volatility of the healthcare market as a feature in our training data. To render a human-interpretable measure of volatility, we compute features using Donchian Channel (Donchian ([1957](https://arxiv.org/html/2601.14062v1#bib.bib50))), Bollinger Bands (Bollinger ([1992](https://arxiv.org/html/2601.14062v1#bib.bib51))), and Keltner Channel (Keltner ([1960](https://arxiv.org/html/2601.14062v1#bib.bib52))), which are standard frameworks in market analysis.

Traders rely on these parameters to assess volatility and trading scenarios, enabling them to make informed financial decisions (Zhu and Sun, [2024](https://arxiv.org/html/2601.14062v1#bib.bib53)). In this research, we calculate these parameters for each trading day and incorporate them as features for our own model-building exercise.

* 1.

  Donchian Channel:

  The Donchian Channel 555<https://www.tradingview.com/chart/IBKR/rO4ruhxQ-Donchian-Channel-Strategy-like-The-Turtles-Traders/>, developed in the 1960s, is a technical indicator that helps traders understand market volatility and identify breakout and reversal points. Technically, it provides three bands: UpperDC​(t)\text{Upper}\_{\text{DC}}(t) – represents the highest high over a specified look-back period (we have taken 20 periods), LowerDC​(t)\text{Lower}\_{\text{DC}}(t) – the lower band captures the lowest low over the same period, and MiddleDC​(t)\text{Middle}\_{\text{DC}}(t), the middle band is calculated as the average of the upper and lower bands. The Donchian Channel encapsulates the index movement within this channel. The bands widen during phases of high volatility and contract during phases of low volatility.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | UpperDC​(t)=max⁡(Phi​(t−n),Phi​(t−n+1),…,Phi​(t)),\displaystyle\text{Upper}\_{\text{DC}}(t)=\max(\textrm{P}\_{\textrm{hi}}(t-n),\textrm{P}\_{\textrm{hi}}(t-n+1),\ldots,\textrm{P}\_{\textrm{hi}}(t))\quad, |  | (3) |
  |  |  | LowerDC​(t)=min⁡(Plo​(t−n),Plo​(t−n+1),…,Plo​(t)),\displaystyle\text{Lower}\_{\text{DC}}(t)=\min(\textrm{P}\_{\textrm{lo}}(t-n),\textrm{P}\_{\textrm{lo}}(t-n+1),\ldots,\textrm{P}\_{\textrm{lo}}(t))\quad, |  |
  |  |  | MiddleDC​(t)=UpperDC​(t)+LowerDC​(t)2\displaystyle\text{Middle}\_{\text{DC}}(t)=\frac{\text{Upper}\_{\text{DC}}(t)+\text{Lower}\_{\text{DC}}(t)}{2}\quad |  |

  Let 𝐱DC​(t)\mathbf{x}\_{\text{DC}}(t) be the band information with respect to the Donchian Channel at Day tt.

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝐱DC​(t)=[UpperDC​(t),LowerDC​(t),MiddleDC​(t)]⊤\mathbf{x}\_{\text{DC}}(t)=[\text{Upper}\_{\text{DC}}(t),\text{Lower}\_{\text{DC}}(t),\text{Middle}\_{\text{DC}}(t)]^{\top}\quad |  | (4) |
* 2.

  Bollinger Bands:
  It is another volatility-capturing tool adopted by traders to assess market conditions, potential breakout opportunities, and overbought or oversold signals 666<https://www.tradingview.com/chart/US500/IavHLFpW-Using-Bollinger-Bands-to-Gauge-Market-Trends-and-Volatility/>. Similar to the Donchian Channel, there are three bands – the middle band is derived from the 20-period simple moving average (SMA), while the upper and lower bands are placed at a set number of standard deviations (usually two) above and below the SMA. The lower and upper bands diverge during high volatility and contract during low volatility. This dynamic movement enables the traders to identify compressions (Bollinger Band squeezes) that often precede significant index breakouts.
  Simple Moving Average (SMA) computes the arithmetic mean of indices over nn periods at Day ii:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | SMAn​(t)=1n​∑i=t−n+1tPcl​(i)\text{SMA}\_{n}(t)=\frac{1}{n}\sum\_{i=t-n+1}^{t}\text{P}\_{\text{cl}}(i) |  | (5) |

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | MiddleBB​(t)=SMAn​(t),σn​(t)=1n​∑i=t−n+1t(Pcl​(i)−SMAn​(i))2,UpperBB​(t)=SMAn​(t)+k​σn​(t),LowerBB​(t)=SMAn​(t)−k​σn​(t).\begin{split}\text{Middle}\_{\text{BB}}(t)&=\text{SMA}\_{n}(t),\\ \sigma\_{n}(t)&=\sqrt{\tfrac{1}{n}\sum\_{i=t-n+1}^{t}\bigl(\text{P}\_{\text{cl}}(i)-\text{SMA}\_{n}(i)\bigr)^{2}},\\ \text{Upper}\_{\text{BB}}(t)&=\text{SMA}\_{n}(t)+k\,\sigma\_{n}(t),\\ \text{Lower}\_{\text{BB}}(t)&=\text{SMA}\_{n}(t)-k\,\sigma\_{n}(t).\end{split} |  | (6) |

    

  , where kk is the weight, usually chosen as 2, or between 1 and 3.

  Let 𝐱BB​(t)\mathbf{x}\_{\text{BB}}(t) be the band information with respect to Bollinger Bands at Day tt.

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝐱BB​(t)=[UpperBB​(t),LowerBB​(t),MiddleBB​(t)]⊤\mathbf{x}\_{\text{BB}}(t)=[\text{Upper}\_{\text{BB}}(t),\text{Lower}\_{\text{BB}}(t),\text{Middle}\_{\text{BB}}(t)]^{\top}\quad |  | (7) |
* 3.

  Keltner Channel:
  It draws an envelope around the moving average of indices, considering a prefixed period (we have taken a 20-day period)888<https://www.ig.com/en/trading-strategies/how-to-trade-using-the-keltner-channel-indicator-191119>. The exponential moving average (EMA) of the prefixed period serves as the middle line for a day, while the upper and lower bands are placed at a distance proportional to the average true range (ATR) over the same period.

  Exponential Moving Average:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | EMAn​(t)=α​Pcl​(t)+(1−α)​EMAt−1​, where ​α=2n+1\text{EMA}\_{n}(t)=\alpha\text{P}\_{\text{cl}}(t)+(1-\alpha)\text{EMA}\_{t-1}\textrm{, where }\alpha=\frac{2}{n+1} |  | (8) |

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | MiddleKC​(t)=EMAn​(t),UpperKC​(t)=MiddleKC​(t)+k⋅ATRn​(t),LowerKC​(t)=MiddleKC​(t)−k⋅ATRn​(t),ATRn​(t)=1n​∑i=t−n+1tTR​(i),TR​(t)=max(Phi(t)−Plo(t),|Phi​(t)−Pcl​(t−1)|,|Plo(t)−Pcl(t−1)|).\begin{split}\text{Middle}\_{\text{KC}}(t)&=\text{EMA}\_{n}(t),\\ \text{Upper}\_{\text{KC}}(t)&=\text{Middle}\_{\text{KC}}(t)+k\cdot\text{ATR}\_{n}(t),\\ \text{Lower}\_{\text{KC}}(t)&=\text{Middle}\_{\text{KC}}(t)-k\cdot\text{ATR}\_{n}(t),\\ \text{ATR}\_{n}(t)&=\frac{1}{n}\sum\_{i=t-n+1}^{t}\text{TR}(i),\\ \text{TR}(t)&=\max\Bigl(\text{P}\_{\text{hi}}(t)-\text{P}\_{\text{lo}}(t),\\ &\quad\left|\text{P}\_{\text{hi}}(t)-\text{P}\_{\text{cl}}(t-1)\right|,\\ &\quad\left|\text{P}\_{\text{lo}}(t)-\text{P}\_{\text{cl}}(t-1)\right|\Bigr).\end{split} |  | (9) |

  Let 𝐱KC​(t)\mathbf{x}\_{\text{KC}}(t) be the band information for the Keltner Channel at Day tt.

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝐱KC​(t)=[UpperKC​(t),LowerKC​(t),MiddleKC​(t)]⊤\mathbf{x}\_{\text{KC}}(t)=[\text{Upper}\_{\text{KC}}(t),\text{Lower}\_{\text{KC}}(t),\text{Middle}\_{\text{KC}}(t)]^{\top}\quad |  | (10) |

  The band information helps in tracking index movements, identifying support/resistance levels, and also signals breakouts when indices move beyond the band levels.

The three tools considered in this work are motivated to capture the volatility in the index movements (and also the historical index movements). Despite this underlying similarity between the three, they provide distinct market insights, each indicative of different trading scenarios. The Donchian channel, the most interpretable among the three, efficiently identifies breakout levels in the market, but is prone to false breakouts (when the low or high index shows sudden changes). Information derived from Bollinger Bands and Keltner Channel is immune to this disadvantage as they rely on moving averages; the contribution of one or a few upward or downward index spikes is dampened by averaging. Bollinger Bands are effective in predicting a surge in indices after a stagnant market scenario; however, they are prone to generating false overbought (or underbought) signals under strong directional momentum. Lastly, by virtue of the exponential function, Keltner Channel is more immune than Bollinger Bands to raising false overbought (or underbought) signals, but is less sensitive to sudden volatility spikes. To have their interpretable but diverse insights in the model, we include bands’ information from all three in the feature set.
Let 𝐱hist​(t)\mathbf{x}\_{\text{hist}}(t) be the historical information about volatility at Day tt. It consists of features extracted from all three bands.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱hist​(t)=[𝐱DC​(t),𝐱BB​(t),𝐱KC​(t)]⊤\mathbf{x}\_{\text{hist}}(t)=[\mathbf{x}\_{\text{DC}}(t),\mathbf{x}\_{\text{BB}}(t),\mathbf{x}\_{\text{KC}}(t)]^{\top}\quad |  | (11) |

### 3.5 Nowcasting Methods

A glimpse of the current market scenario is provided by the intrinsic features, 𝐱int()˙\mathbf{x}\_{\text{int}}(\dot{)} (as discussed in Section 3.3). On the other hand, the features related to historical prices summarization (as discussed in the previous section), 𝐱hist()˙\mathbf{x}\_{\text{hist}}(\dot{)}, give a comprehensive picture of the market’s movement over a past period. They offer a deep understanding of the volatility, stationarity, and movement of the indices. It is important to note that only four distinct indices are known for any trading day, including the current trading session, but the movement in the current day cannot be explicitly inferred from these four data points. Consequently, both categories of features are suboptimal for providing finer details of intraday market momentum on the current trading day. To address this gap and unfold the intraday narrative, we include the logarithm of the index ratios (with respect to open indices) in the feature set. They are l​n​(PhiPop)ln{(\frac{P\_{\textrm{hi}}}{P\_{\textrm{op}}})}, l​n​(PloPop)ln{(\frac{P\_{\textrm{lo}}}{P\_{\textrm{op}}})} and l​n​(PclPop)ln{(\frac{P\_{\textrm{cl}}}{P\_{\textrm{op}}})}.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | ro​ph​i​(t)\displaystyle r\_{op}^{hi}(t) | =l​n​(Phi​(t)Pop​(t)),\displaystyle=ln{\left(\frac{{P}\_{\textrm{hi}}(t)}{{P}\_{\textrm{op}}(t)}\right)}, |  | (12a) |
|  | ro​pl​o​(t)\displaystyle r\_{op}^{lo}(t) | =l​n​(Plo​(t)Pop​(t)),\displaystyle=ln{\left(\frac{P\_{\textrm{lo}}(t)}{P\_{\textrm{op}}(t)}\right)}, |  | (12b) |
|  | ro​pc​l​(t)\displaystyle r\_{op}^{cl}(t) | =l​n​(Pcl​(t)Pop​(t)).\displaystyle=ln{\left(\frac{P\_{\textrm{cl}}(t)}{P\_{\textrm{op}}(t)}\right)}. |  | (12c) |

The three values ro​ph​i​(t),ro​pl​o​(t)r\_{op}^{hi}(t),r\_{op}^{lo}(t), and ro​pc​l​(t)r\_{op}^{cl}(t) serve as nowcasting tools for predicting the rise-or-fall of index on the upcoming trading day. The combinations of their values can provide an array of information about movement in the current trading day’s market, thereby contributing to the robustness of the model. Some of those perceptions are described as follows.

* 1.

  ro​pc​l​(t)>0r\_{op}^{cl}(t)>0 shows that the market closed at a value higher than it opened, ro​pc​l​(t)<0r\_{op}^{cl}(t)<0 indicates the opposite.
* 2.

  ro​pl​o​(t)∼0r\_{op}^{lo}(t)\sim 0 yields that the market remained higher than the opening throughout the day.
* 3.

  ro​ph​i​(t)∼0r\_{op}^{hi}(t)\sim 0 indicates that the market remained lower than the opening throughout the day.
* 4.

  ro​pl​o​(t)<0r\_{op}^{lo}(t)<0 or ro​ph​i​(t)>0r\_{op}^{hi}(t)>0 (by some substantial margin) indicates a considerable movement in the market, where the low index fell below the open index and the high index rose above the open index.
* 5.

  |ro​ph​i​(t)|∼0,|ro​pl​o​(t)|∼0|r\_{op}^{hi}(t)|\sim 0,|r\_{op}^{lo}(t)|\sim 0, and |ro​pc​l​(t)|∼0|r\_{op}^{cl}(t)|\sim 0 indicates a stationary market, where all four indices remain within a small range, thereby, rendering a close to 0 value of their logarithm ratios.

To imbibe these reasoning into our training model, we include them to form a *nowcasting* feature set, 𝐱now​(t)\mathbf{x}\_{\text{now}}(t). From the ML perspective, 𝐱now​(t)\mathbf{x}\_{\text{now}}(t) helps the model focus on the intraday movement and momentum of indices on the current trading day.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱now​(t)=[ro​ph​i​(t),ro​pl​o​(t),ro​pc​l​(t)]⊤\mathbf{x}\_{\text{now}}(t)=[r\_{op}^{hi}(t),r\_{op}^{lo}(t),r\_{op}^{cl}(t)]^{\top}\quad |  | (13) |

The nowcasting features capture the intraday price movements in the immediately previous trading day. This movement has the potential to influence and bridge the price movements in the upcoming trading day, and accordingly, we explore it as a feature for a price movement indicator.

### 3.6 Final set of features

The final set of features is formed by taking the concatenation of the intrinsic features (𝐱int\mathbf{x}\_{\text{int}}), features derived from market’s volatility (𝐱vol\mathbf{x}\_{\text{vol}}), and nowcasting tools (𝐱now\mathbf{x}\_{\text{now}}).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱​(t)=[𝐱int​(t)𝐱hist​(t)𝐱now​(t)]\mathbf{x}(t)=\begin{bmatrix}\mathbf{x}\_{\text{int}}(t)\\ \mathbf{x}\_{\text{hist}}(t)\\ \mathbf{x}\_{\text{now}}(t)\end{bmatrix} |  | (14) |

𝐱​(t)\mathbf{x}(t) is used in building the final classifier. The final set of features encompasses diverse aspects: intrinsic prices of the immediately previous trading day, intraday price movements on the same day, and the historical features that capture the volatility in the twenty-day window. We explore whether this rich feature set can effectively associate with the target class of rise/ fall of prices and predict it for the upcoming trading day.

## 4 Data Source and Computational Methodology

### 4.1 Data Collection

This research focuses on predicting the opening trend of healthcare indices. To study the utility of our method, we include two datasets, which are derived from actual markets – i] Healthcare index from Standard and Poor’s (S&\&P) 500, United States of America, the largest economy of the world (representative of a mature market), and, ii] Healthcare index from Standard and Poor’s (S&\&P) Bombay Stock Exchange (BSE), India, representative of the emerging economies. S&\&P 500 is a stock market index which tracks the stock performance of 500 leading companies listed on stock exchanges in the United States; the market capitalization of the enlisting reached US $\mathdollar 55 trillion in July 2025 101010<https://thetradable.com/stocks/sp-500-market-cap-hits-record-557-trillion-historic-rally-continues-ig>. S&\&P BSE Sensex is an Indian free-float, market-weighted stock market index of 30 stable and financially robust companies listed on the BSE. The total market capitalization of listings in BSE is US $\mathdollar 5.6 trillion as of September 2024 111111<https://www.ceicdata.com/en/indicator/india/market-capitalization>.

For both countries, we have considered five fiscal years, from 1st April 2019 to 31 March 2024. In this period, S&\&P 500 (U.S.A.) recorded 1256 trading days and the same figure was 1237 for BSE (India). Local events and market closures are accountable for the minor variations in trading days. For each trading day tt, their open, high, low, and close indices have served as the intrinsic features. The calculation of historical features requires a window of 20 days, out of which 19 days are before the day of calculation. Hence, we have to exclude the initial 19 days from our calculation. Day tt’s class label is derived by comparing its index (open/ high/ low/ close) with the open index of the next trading day (t+1)(t+1). As said, we cannot compute the class label for the last day of the period (as it depends on the next trading day), so we exclude it. So, a total of 20 trading days is excluded from each dataset. Hence, for S&\&P 500 (U.S.A.) and BSE (India), our datasets consist of 1236 and 1217 trading days, respectively.
The basic description can be found in Table [2](https://arxiv.org/html/2601.14062v1#S4.T2 "Table 2 ‣ 4.1 Data Collection ‣ 4 Data Source and Computational Methodology ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?").

Table 2: Summary of Datasets

|  |  |  |
| --- | --- | --- |
|  | Healthcare index | |
| S&\&P 500, U.S.A. | BSE, India |
| Period | Apr 1, 2019 – Mar 31, 2024 | |
| No. of trading days | 1256 | 1237 |
| No. of days discarded | ——20—— | |
| No. of points in the dataset | 1236 | 1217 |
| No. of training points | 989 | 974 |
| No. of test points | 247 | 234 |

We consider each dataset as a time series, as observations consist of indices, which are ordered chronologically. The first 80%\% days are considered for training the model, and the remaining 20%\% are used to test the model. This allows the model to learn the temporal associations. We have incorporated one-step-ahead rolling window approach for prediction instead of multi-step-ahead forecasting ((Karathanasopoulos et al., [2016](https://arxiv.org/html/2601.14062v1#bib.bib54))). We evaluate the model’s predictive capability by calculating the accuracy and MCC scores on predictions.

### 4.2 Method

In this work, we build ML-based models to predict the rise/ fall of open index of the healthcare index in the upcoming trading day. The datasets for our model are derived from S&\&P 500, U.S.A., and BSE, India. While constructing the feature set, we use the intrinsic indices as well as some derived features, as described in the previous section. Let 𝒟∗\mathcal{D}^{\*} be the dataset, consisting of the points (represented by their features), 𝐱​(⋅)\mathbf{x}(\cdot), and the corresponding class labels y∗o​p​(⋅)y^{op}\_{\*}(\cdot).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟∗={(𝐱(i),y∗o​p(i)}i=1N,N=|𝒟∗|,∗∈{op,hi,lo,cl}\mathcal{D}^{\*}=\{(\mathbf{x}(i),{y}^{op}\_{\*}(i)\}\_{i=1}^{N},\quad N=|\mathcal{D}^{\*}|,\*\in\{op,hi,lo,cl\} |  | (15) |

We split 𝒟∗\mathcal{D}^{\*} into a training set, 𝒟t​r∗\mathcal{D}^{\*}\_{tr} and a test set, 𝒟t​e∗\mathcal{D}^{\*}\_{te}. Points in 𝒟∗\mathcal{D}^{\*} are arranged chronologically, its first 80%80\% points form 𝒟t​r∗\mathcal{D}^{\*}\_{tr} and the remaining (latest) 20%20\% points form 𝒟t​e∗\mathcal{D}^{\*}\_{te}. Note that, depending on ∗\*, the dataset changes. The change happens due to the change in the target class only; the feature set remains the same across all cases.

In this work, we consider four different problem cases by comparing four types of indices of Day tt with the open index of Day (t+1)(t+1). They are – i] comparison of the open indices of Day (t+1)(t+1) and Day tt, ii] comparison of the open index of Day (t+1)(t+1) with the high index of Day tt, iii] comparison of the open index of Day (t+1)(t+1) with the low index of Day tt, and, iv] comparison of the open index of Day (t+1)(t+1) with the close index of Day tt. For each of these subproblems, we train a different classifier model using its dedicated training dataset and obtain predictions on its dedicated test set.

We train model ℳ∗\mathcal{M}^{\*} to predict the increase or decrease of upcoming indices with respect to their corresponding previous day’s ∗\* indices, where ∗∈{op,hi,lo,cl}\*\in\{op,hi,lo,cl\}. We use 𝒟t​r∗\mathcal{D}^{\*}\_{tr} to construct ℳ∗\mathcal{M}^{\*}. As the cardinality of the set {o​p,h​i,l​o,c​l}\{op,hi,lo,cl\} is f​o​u​rfour, we train f​o​u​rfour different models – ℳo​p\mathcal{M}^{op}, ℳh​i\mathcal{M}^{hi}, ℳl​o\mathcal{M}^{lo} and ℳc​l\mathcal{M}^{cl}.

The model M∗M^{\*} is trained on 𝒟t​r∗\mathcal{D}^{\*}\_{tr} which consists of α\alpha points:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M∗=𝒜​({(x​(i),y∗op​(i))}i=1α),M^{\*}=\mathcal{A}\left(\{(x(i),y\_{\*}^{\text{op}}(i))\}\_{i=1}^{\alpha}\right), |  | (16) |

where 𝒜\mathcal{A} is the learning algorithm, x​(i)x(i) is the ii-th input, y∗op​(i)y\_{\*}^{\text{op}}(i) is the corresponding class label of point x​(i)x(i), α\alpha denotes the total number of training points.

### 4.3 Classifiers used

We have employed an array of classifiers to assess the discriminative power of the crafted feature set. When selecting classifiers, we considered a mix of interpretable and black-box models. There are eight different classifier types – four with a substantial degree of interpretability (Decision Tree, Gaussian Naive Bayes, k-Nearest Neighbor, and Logistic Regression), and four with low interpretability (eXtreme Gradient Boosting (XGB), Multi Layer Perceptron (MLP), CatBoost, and ExtraTrees). The choice of classifiers is made to ensure that the prediction model is free of algorithmic bias, thereby revealing the true capabilities of the diverse feature genres.

We used Python implementations of all classifiers (Garreta and Moncecchi ([2013](https://arxiv.org/html/2601.14062v1#bib.bib55))). For the Decision Tree, we set m​a​xd​e​p​t​h=10max\_{d}epth=10 and m​a​xf​e​a​t​u​r​e​s=5max\_{f}eatures=5. Gaussian Naive Bayes is used at its default configuration. The neighborhood size in the kk-nearest neighbor classifier is set to 5, and the liblinear solver is employed in the Logistic Regression Classifier. We have used the default parameter configuration for the XGB Classifier. For the MLP Classifier, we have used 8 hidden layers, relu activation function, and 1000 iterations. We set 1000 iterations and a learning rate of 0.1 for the CatBoost Classifier. For ExtraTreesClassifier, the criterion is set to cross-entropy and the number of estimators is set to 1000.

### 4.4 Evaluation metrics

We measure the veracity of predictions using accuracy scores and Matthews Correlation Coefficient (MCC) scores Chicco and Jurman ([2020](https://arxiv.org/html/2601.14062v1#bib.bib56)); Nguyen et al. ([2024](https://arxiv.org/html/2601.14062v1#bib.bib57)). Accuracy offers an intuitive, widely prevalent, but potentially misleading view of performance, as it can be inflated by market imbalances (for example, always predicting a rise in a bull market or a fall in a bearish market). Compared to accuracy, MCC is a far more robust metric, as it accounts for all classes of predictions. A high MCC score confirms the model’s veracity in all scenarios, which is critical for the practical utility of the outcomes. The formula and reference levels for MCC scores are provided in [C](https://arxiv.org/html/2601.14062v1#A3 "Appendix C Matthews Correlation Coefficient (MCC) scores ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?"). For both metrics, higher scores indicate better performance.

## 5 Results

### 5.1 Performance of the classifiers

In this section, we present the veracity of predictions on the rise or fall of the open index of the upcoming trading day. Like every ML model-building and evaluation process, this work has two principal steps: i] data sculpting from raw data on the open, high, low, and close indices, and ii] developing the underlying architecture of the classifier. An intrinsic data sculpting method is proposed in this work, incorporating three feature genres. We test their individual as well as cumulative efficiencies. A spectrum of different classifiers is explored to find out the one/s with the highest class discerning ability(ies). Figures 1-8 (a) and (b) record the performance of the methods. We present the results in a segregated fashion, with respect to i] index comparison (related to four different classes), ii] classifiers, and iii] features (related to).

* 1.

  For which type of index-comparison, do we get the highest veracity in predictions?
    
  This work explores four different tasks, prediction of the rise or fall of the upcoming trading day’s open index with respect to the current day’s i] open index, ii] high index, iii] low index, and iv] close index.

  Figures [1](https://arxiv.org/html/2601.14062v1#S5.F1 "Figure 1 ‣ item 1 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") and [2](https://arxiv.org/html/2601.14062v1#S5.F2 "Figure 2 ‣ item 1 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") illustrate the accuracy and MCC scores for predicting the next day’s open index movement—rise or fall—relative to the current day’s *open index*, respectively. In this case, the question addressed by the model is – *Will the market open at a higher level than it opened today?* The tabular data shows that the models can provide trustworthy predictions for both the markets (S&\&P 500 and BSE). Many of the classifier architectures and feature combinations have yielded commendable accuracy and MCC scores, with accuracies of 0.800.80 and MCCs of 0.600.60. These data manifest the utility of the proposed framework (with the correct choice of features and classifiers) in predicting the rise or fall of the next day’s open index (relative to the current day’s open index) for the healthcare sector.

  Figures [3](https://arxiv.org/html/2601.14062v1#S5.F3 "Figure 3 ‣ item 1 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") and [4](https://arxiv.org/html/2601.14062v1#S5.F4 "Figure 4 ‣ item 1 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") depict the performance of predicting the next day’s open index movement—rise or fall—relative to the current day’s *high index*, respectively. In this case, the question addressed by the model is – *Will the market open at a higher level than the highest index seen today?*. The tables show that the prediction framework yields reliable results, with MCC and accuracy scores of 0.600.60 and 0.800.80, respectively, across several models. The healthcare index prediction for S&\&P 500 has shown greater reliability than that of BSE, as the MCC scores for the former lie in the range 0.800.80, whereas for the latter they lie in the range 0.650.65.

  Figures [5](https://arxiv.org/html/2601.14062v1#S5.F5 "Figure 5 ‣ item 1 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") and [6](https://arxiv.org/html/2601.14062v1#S5.F6 "Figure 6 ‣ item 1 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") record the performance of predicting the next day’s open index’s rise or fall, relative to the current day’s *low index*. The implication of this task is whether the market will open higher than today’s low. For this class of predictions, the accuracy ranges from 0.90~\tilde{0.90} for both markets, while the MCC scores remain in a moderately reliable range. For S&\&P 500, the MCC scores range in 0.60.6 for most of the well-doing classifiers, with only MLP peaking to >0.8>0.8. For BSE, performance is a notch lower, as the MCC scores remain around 0.6~\tilde{0.6} for the best-performing classifiers as well.

  Lastly, the figures [7](https://arxiv.org/html/2601.14062v1#S5.F7 "Figure 7 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") and [8](https://arxiv.org/html/2601.14062v1#S5.F8 "Figure 8 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") show the performance of predicting the next day’s open index’s rise or fall-relative to the current day’s *close index*. The implication of this prediction – whether the market will open at a higher level tomorrow than today’s closing price. Despite an admissible range of accuracy (0.7−0.8)(0.7-0.8) for a number of classifier-feature pairs (though lower than that of the previous three tasks), the MCC scores lie in the range 0.0−0.1~\tilde{0.0-0.1} for both the market (with only one exception in S&\&P 500).

  Table [3](https://arxiv.org/html/2601.14062v1#S5.T3 "Table 3 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") summarizes the outcomes described above. This table shows the generic reliability of the proposed framework across the four subproblems described above. The table indicates whether an effective classifier existed for each subproblem, as evaluated by the two metrics. For accuracy and MCC scores, we set the reference levels to 0.80.8 and 0.650.65, respectively. The justification for the choices of values is elaborated in Sections [B](https://arxiv.org/html/2601.14062v1#A2 "Appendix B Accuracy ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") and [C](https://arxiv.org/html/2601.14062v1#A3 "Appendix C Matthews Correlation Coefficient (MCC) scores ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?").
  The implications of the outcomes shown in the figures and Table [3](https://arxiv.org/html/2601.14062v1#S5.T3 "Table 3 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") are discussed in detail in Section 6.

  ![Refer to caption](acc-open_us.png)


  (a) S&\&P 500

  ![Refer to caption](acc-open.png)


  (b) BSE

  Figure 1: The plots present the accuracy scores for the *open-open* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the accuracy score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.



  ![Refer to caption](mcc-open_us.png)


  (a) S&\&P 500

  ![Refer to caption](mcc-open.png)


  (b) BSE

  Figure 2: The plots present the MCC scores for the *open-open* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the MCC score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.



  ![Refer to caption](acc-high_us.png)


  (a) S&\&P 500

  ![Refer to caption](acc-high.png)


  (b) BSE

  Figure 3: The plots present the accuracy scores for the *open-high* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the accuracy score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.



  ![Refer to caption](mcc-high_us.png)


  (a) S&\&P 500

  ![Refer to caption](mcc-high.png)


  (b) BSE

  Figure 4: The plots present the MCC scores for the *open-high* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the MCC score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.



  ![Refer to caption](acc-low_us.png)


  (a) S&\&P 500

  ![Refer to caption](acc-low.png)


  (b) BSE

  Figure 5: The plots present the accuracy scores for the *open-low* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the accuracy score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.



  ![Refer to caption](mcc-low_us.png)


  (a) S&\&P 500

  ![Refer to caption](mcc-low.png)


  (b) S&\&P 500

  Figure 6: The plots present the MCC scores for the *open-low* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the MCC score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.
* 2.

  Which class of features is most effective in prediction?

  This work has explored the performance of three different genres of features and their combinations. The set of original indices constitutes the intrinsic feature set, the past volatility of the markets constitutes the historical features, and the indices’ ratios of the current day (with respect to the open index) form the nowcasting features. We report results for intrinsic features and their combinations with historical and nowcasting features.

  As evidenced by the figures and tabular data, the intrinsic features exhibit moderate capability to predict the rise or fall of the open index on the following day. However, the results show inconsistency in this ability across different sub-problems; the range of MCC scores, in particular, has varied substantially. The results reveal significant inconsistency in the feature’s discriminative capability across different sub-problems. The variation is particularly evident through the range of MCC scores, suggesting context-specific utility of intrinsic features. While some sub-problems exhibit strong separability (with MCC scores approaching 0.8), others show markedly weaker performance (MCC value 0~\tilde{0}), indicating potential limitations in generalization capability or the influence of problem-specific factors.

  As indicated by the figures and table, the volatility components obtained from Donchian Channel, Bollinger Bands, and Keltner Channels have failed to show consistent correlation with the rise/ fall of indices. Their inclusion in the feature set has yielded contradictory results: performance improves for certain subproblems, whereas for others it is negligible or even adverse. When predicting the rise or fall of the next day’s open index from the current day’s high and low indices, it has shown improved performance. On the contrary, when predicting the same with respect to the current day’s open index, it has shown adverse effects. Lastly, when predicting the next day’s rise or fall based on the current day’s close index, no measurable performance difference was observed. The cumulative results raise questions about the suitability of this class of features for predicting the rise/ fall of open index.

  The results show that the addition of nowcasting features has elevated the correctness of predictions. For three of the four sub-problems, it has achieved substantial improvements; both accuracy and MCC scores have improved. The incorporation of this class of features has led to a marked improvement in the model’s predictive performance. The sole exception is predicting the next day’s close index, for which all features have failed to yield an admissible output. The nowcasting features have shown utility across multiple subproblems involving predicting with respect to open, high, and low indices. These findings demonstrate the ability of these features to distill meaningful economic signals for predicting the rise/ fall of open index on the subsequent trading day.

![Refer to caption](acc-close_us.png)


(a) S&\&P 500

![Refer to caption](acc-close.png)


(b) BSE

Figure 7: The plots present the accuracy scores for the *open-close* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the accuracy score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.



![Refer to caption](mcc-close_us.png)


(a) S&\&P 500

![Refer to caption](mcc-close.png)


(b) BSE

Figure 8: The plots present the MCC scores for the *open-close* across a feature-classifiers grid. Plots (a) and (b) are dedicated to S&\&P 500 and BSE, respectively. The vertical axis shows different combinations of features, while the horizontal axis lists the classifiers. The higher the MCC score, the better the performance. Consequently, larger circle radii and darker colors indicate better performance.




Table 3: Summary of reliability across different subproblems. An effective classifier is defined as achieving accuracy ≥0.8\geq 0.8 and MCC ≥0.65\geq 0.65. A checkmark (✓\checkmark) indicates that at least one such classifier exists for the subproblem; a dash (–) indicates that none met both thresholds (accuracy and MCC scores).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Task | Implication | S&P 500  BSE | | | |
|  |  | Acc. | | MCC | |
| Open w.r.t. Open | Tomorrow’s open >> today’s open? | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Open w.r.t. High | Tomorrow’s open >> today’s high? | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Open w.r.t. Low | Tomorrow’s open >> today’s low? | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Open w.r.t. Close | Tomorrow’s open >> today’s close? | ✓\checkmark | – | – | – |

### 5.2 Explainability and correlation of the features with the trend

In this subsection, we investigate i] the explainability of the features in the context of the class labels (trend prediction w.r.t. previous day’s open, high, low, and close indices) and ii] the correlation of the different classes of the features with the class label. Despite using an identical feature set across tasks, their influence can vary significantly, depending on the context. To this end, we analyze feature explainability in each of the four tasks (which are described in the previous section). For each task, separate analyses are carried out for the two markets, S&\&P 500 and BSE.

We employ Shapley values (Lundberg and Lee, [2017](https://arxiv.org/html/2601.14062v1#bib.bib22)), a game-theoretic approach, to interpret our model’s predictions and understand the predictive capability of the features. This method quantifies the individual contributions of the features in a prediction task by calculating their average marginal contribution with respect to all possible combinations of features. The method’s modus operandi also allows us to have a transparent and interpretable reckoning of the model’s action. The magnitude of a feature’s Shapley value reflects the strength of its influence on a given prediction. The overall contribution of each feature is determined by aggregating its absolute Shapley values across the entire dataset. This cumulative figure reveals which features consistently exert the strongest influence on the model’s outputs, as well as their complements (weak features with low class-discriminating ability).

![Refer to caption](shap-open_us.png)


(a) S&\&P 500

![Refer to caption](shap-open.png)


(b) BSE

Figure 9: Shapley values obtained in the task of predicting the next day’s open index’s rise or fall, relative to the current day’s *open index*.

Figure [9](https://arxiv.org/html/2601.14062v1#S5.F9 "Figure 9 ‣ 5.2 Explainability and correlation of the features with the trend ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") shows that the ratio of the current day’s close and open indices serves as the most crucial indicator in predicting the rise and fall of the open index in the upcoming trading day (with respect to the current day’s open index). In both the US and the Indian markets, the remaining features exert a negligible influence on the predictions, with the effect being more pronounced in the US market.

![Refer to caption](shap-high_us.png)


(a) S&\&P 500

![Refer to caption](shap-high.png)


(b) BSE

Figure 10: Shapley values obtained in the task of predicting the next day’s open index’s rise or fall, relative to the current day’s *high index*.

Figure [10](https://arxiv.org/html/2601.14062v1#S5.F10 "Figure 10 ‣ 5.2 Explainability and correlation of the features with the trend ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") shows the role of features in predicting the trend of the upcoming trading day’s open index with respect to the current day’s high index. While the close-to-open index ratio and the high-to-open index ratio are the most important features in both markets, their relative importance differs. In the US market, they are nearly equal. On the contrary, in the Indian market, the close-to-open index ratio is significantly more important, while the importance of the high-to-open index ratio substantially diminishes.

![Refer to caption](shap-low_us.png)


(a) S&\&P 500

![Refer to caption](shap-low.png)


(b) BSE

Figure 11: Shapley values obtained in the task of predicting the next day’s open index’s rise or fall, relative to the current day’s *low index*.

Figure [11](https://arxiv.org/html/2601.14062v1#S5.F11 "Figure 11 ‣ 5.2 Explainability and correlation of the features with the trend ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") shows the role of features in predicting the trend of the upcoming trading day’s open index with respect to the current day’s low index. For this task, the US market and the Indian market have shown nearly identical trends for the most important features. In either case, the close-to-open index ratio and the low-to-open index ratio have been identified as the most important features, with the close-to-open ratio taking a slight precedence.

![Refer to caption](shap-close_us.png)


(a) S&\&P 500

![Refer to caption](shap-close.png)


(b) BSE

Figure 12: Shapley values obtained in the task of predicting the next day’s open index’s rise or fall, relative to the current day’s *close index*.

Figures [7](https://arxiv.org/html/2601.14062v1#S5.F7 "Figure 7 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") and [8](https://arxiv.org/html/2601.14062v1#S5.F8 "Figure 8 ‣ 5.1 Performance of the classifiers ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?") show that the proposed modus operandi has shown sub-optimal efficacy in predicting the trend of the upcoming trading day’s open index with respect to the current day’s close index. The result is in contradiction with the performance achieved in the other three sub-problems, for which we achieved an admissible performance.
This performance discrepancy is reflected and in congruence in the feature importance analysis shown in [12](https://arxiv.org/html/2601.14062v1#S5.F12 "Figure 12 ‣ 5.2 Explainability and correlation of the features with the trend ‣ 5 Results ‣ Demystifying the trend of the healthcare index: Is historical price a key driver?"). For the US Market, the lower band of the Keltner Channel emerges as the most important feature, followed by the lower band of the Bollinger Bands. However, the overall importance values are low—the highest is only 0.15, and the narrow range across features indicates a lack of clear discriminatory power. The scenario is more diffuse in the Indian market. The upper band of the Keltner channel, the closing index of the current day, and the moving average of Bollinger Bands emerge as the top contributors, but the importance values are exceptionally low (max ¡ 0.1) and exhibit a near-random distribution. The consistently low feature importance scores across both markets indicate that the available features lack the strong correlations with the class label necessary for effective prediction of the rise-or-fall of the upcoming trading day’s open index with respect to the current day’s close index.

## 6 Discussion

This research challenges the apparent randomness of the healthcare sector’s index and seeks to uncover the underlying factors that contribute to its rise/ fall. The fundamental features that are associated with the index’s directional movement remain poorly understood (Karanasos et al., [2022](https://arxiv.org/html/2601.14062v1#bib.bib58); Li et al., [2005](https://arxiv.org/html/2601.14062v1#bib.bib59)), presenting a significant knowledge gap that this study aims to address. We consider a diversified class of factors to identify those that strongly correlate with the directional movement at market opening and can serve as effective features for modeling the problem. The three types considered are: i] raw index values, ii] historical movement, and iii] nowcasting factors. The results of classifier modeling and feature importance assessment have shown that historical price movement has negligible power in accurately predicting the rise or fall of the opening value of the healthcare index. On the contrary, nowcasting factors or the index’s movement in the prior day (of prediction) show a stronger association with the rise or fall of the index, thereby rendering its correct prediction. The original index values have demonstrated a certain degree of predictive power, yielding acceptable accuracy and MCC scores on several occasions. Experimental results also show that the combination of these two classes of data (nowcasting factors and raw index values) can serve as an effective feature for predicting the indices’ movement.

To ensure the viability and robustness of our exploration, we have conducted the study using data from two different economies: the US and India. We have obtained mostly similar outcomes in the two scenarios; sectoral homogeneity is a contributing factor in this regard. The predictive performance for the US market is slightly better than that of the Indian market, likely due to the greater stability and higher trading volume of the US market 121212<https://www.zyen.com/publications/public-reports/the-global-financial-centres-index-37/>131313<https://www.imf.org/en/Publications/WEO/weo-database/2024/April/groups-and-aggregates>. This stability strengthens the association between features and market movements, increasing the veracity of the predictions. This study is valuable not only to researchers but also to stakeholders across various domains, including finance and healthcare.

### 6.1 Implications in the healthcare and financial sectors

The growth of the healthcare index is closely tied to breakthroughs and developments in the sector: an innovation raises the index, while a setback lowers it. Conversely, a rise in the index can boost fund flows for innovation and development in the sector, while a fall in the index often takes a toll on investor confidence, thereby reducing fund flows. Together, through mutual feedback, they establish a bidirectional causality. In this context, prior knowledge of the rise or fall of the sectoral index can help investors obtain timely financial clues to allocate their funds. The credible clues can build confidence in investors’ perceptions of the sector’s stability and growth. Being able to predict the market can enhance one’s understanding, leading them to make informed decisions about their fund allocations and thereby increasing the flow of funds. Our model’s features are derived from publicly available healthcare index data, making them equally accessible to all. This transparency helps counteract biases that can stem from exclusive access to information (by influential entities). Transparency can prevent insider trading, which is known to have a disastrous effect on finances through capital misallocation and erosion of investor confidence (Hsu, [2024](https://arxiv.org/html/2601.14062v1#bib.bib60); Gu et al., [2021](https://arxiv.org/html/2601.14062v1#bib.bib61)). In the healthcare sector, insider trading can have disastrous effects, like retarded milestones in the health sector by affecting innovations like new drug trials, the launch of new drugs, and vaccines.

### 6.2 Limitations and directions of future research

Despite its contributions, this study has limitations that suggest directions for future research. Firstly, the results of predicting the upcoming trading day’s rise-or-fall of the open index with respect to the current day’s close index are sub-optimal. Two primary factors can explain this outcome: either the chosen features lack association with the rise-or-fall of the upcoming trading day’s open index with respect to the current day’s close index, or the rise-or-fall of the upcoming trading day’s open index with respect to the current day’s closing index itself exhibits a random nature.

The second limitation arises when forecasts serve as a feature in themselves. Before deploying our framework for rise-or-fall prediction, we must consider the following: the act of forecasting can actively shape the future it attempts to foresee. This is commonly referred to as the observer effect, where predictions given by a trusted model become new input to the system. For example, a predicted economic downturn can encourage policy changes that prevent it, or a forecast of high demand can trigger panic buying that creates it. This renders a non-static model validity, which is contingent on how its predictions are integrated into the decision-making ecosystem. As our features and model are crafted from publicly available data, we must be cautious about how its predictions can influence the actual market, particularly if it is adopted on a large scale.

## 7 Conclusion

This research challenges the prevailing perception that short-term movements in healthcare sector indices are mostly random and difficult to predict. Through a systematic investigation of multiple genres of features — raw index values, technical tool-based historical price movement, and nowcasting factors — we demonstrate that an admissible and economically meaningful signal is camouflaged in the apparent noise in daily healthcare index fluctuations. We frame the problem as a supervised classification task involving a one-step-ahead rolling window.

Our empirical findings consistently reveal that nowcasting features, constructed from mutual ratios of open–high–low–close indices in the current trading day, are the dominant contributors to predictive performance at the upcoming trading day. In contrast, historical price movement exhibits negligible predictive association with the directional movement of the opening index, while raw index values offer moderate but inconsistent predictive utility. Importantly, integrating nowcasting features with raw price information yields the most reliable performance, indicating that near-real-time market signals complemented by baseline price level fluctuation provide the most effective representation of short-term healthcare index behavior. Shapley-based feature explainability analysis also reveals the same. The robustness of these findings is validated across two structurally distinct healthcare markets—the United States and India. The slightly stronger predictive performance observed in the U.S. market can plausibly be attributed to greater market depth, liquidity, and stability, which reinforce the association between observed features and subsequent price movements.

Beyond methodological contributions, this research has important implications for both healthcare ecosystems. Short-term predictability of healthcare indices can support more efficient capital allocation, stabilize funding flows for medical research and development, and reduce information asymmetry among market participants of different classes. Our methodology relies exclusively on publicly available data; the proposed framework promotes transparency and equitable access to market intelligence, thereby mitigating the risks of insider trading, which can undermine innovation and question trust in healthcare financing systems.

This work is not devoid of limitations and ethical considerations. One predictive task — the subproblem related to open and close indices — remains underserved. The cause can be intrinsic randomness in the scenario or missing explanatory factors for the subproblem. Additionally, forecasts can influence market behavior. In future research, we will examine the feedback effects of rendering predictions and the systematic implications of deploying predictive models at scale. We will address these interdisciplinary challenges by integrating behavioral, policy, and structural factors into future modeling.

## References

* Mazzucato and Parris (2015)

  M. Mazzucato, S. Parris,
  High-growth firms in changing competitive environments: the us pharmaceutical industry (1963 to 2002),
  Small Business Economics 44 (2015) 145–170.
* Gabe et al. (2015)

  J. Gabe, S. Williams, P. Martin, C. Coveney, Pharmaceuticals and society: Power, promises and prospects, 2015.
* Ward et al. (2021)

  B. W. Ward, M. Sengupta, C. J. DeFrances, D. T. Lau,
  Covid-19 pandemic impact on the national health care surveys,
  American journal of public health 111 (2021) 2141–2148.
* Yach (2016)

  D. Yach,
  Health as a cornerstone of good business and sustainable development,
  American journal of public health 106 (2016) 1758.
* Pineiro-Chousa et al. (2022)

  J. Pineiro-Chousa, M. Á. López-Cabarcos, L. Quinoa-Pineiro, A. M. Perez-Pico,
  Us biopharmaceutical companies’ stock market reaction to the covid-19 pandemic. understanding the concept of the ‘paradoxical spiral’from a sustainability perspective,
  Technological Forecasting and Social Change 175 (2022) 121365.
* Kapar et al. (2022)

  B. Kapar, S. Buigut, F. Rana,
  Winners and losers from pfizer and biontech’s vaccine announcement: Evidence from s&p 500 (sub) sector indices,
  Plos one 17 (2022) e0275773.
* Dierks et al. (2016)

  R. M. L. Dierks, O. Bruyère, J.-Y. Reginster, F.-F. Richy,
  Macro-economic factors influencing the architectural business model shift in the pharmaceutical industry,
  Expert review of pharmacoeconomics & outcomes research 16 (2016) 571–578.
* Lakdawalla (2018)

  D. N. Lakdawalla,
  Economics of the pharmaceutical industry,
  Journal of Economic Literature 56 (2018) 397–449.
* Beniwal et al. (2024)

  M. Beniwal, A. Singh, N. Kumar,
  Forecasting multistep daily stock prices for long-term investment decisions: A study of deep learning models on global indices,
  Engineering Applications of Artificial Intelligence 129 (2024) 107617.
* Weng et al. (2017)

  B. Weng, M. A. Ahmed, F. M. Megahed,
  Stock market one-day ahead movement prediction using disparate data sources,
  Expert systems with applications 79 (2017) 153–163.
* Stratimirović et al. (2018)

  D. Stratimirović, D. Sarvan, V. Miljković, S. Blesić,
  Analysis of cyclical behavior in time series of stock market returns,
  Communications in Nonlinear Science and Numerical Simulation 54 (2018) 21–33.
* Horvath (1998)

  M. Horvath,
  Cyclicality and sectoral linkages: Aggregate fluctuations from independent sectoral shocks,
  Review of Economic Dynamics 1 (1998) 781–808.
* Li et al. (2024)

  Y. Li, R. Gu, D. Zhao,
  Comparative analysis of volatility forecasting for healthcare stock indices amid public health crises: a study based on the bayes-cnn model,
  Frontiers in Public Health 12 (2024) 1476196.
* Sengupta et al. (2025)

  S. Sengupta, T. Chakraborty, S. K. Singh,
  Forecasting cpi inflation under economic policy and geopolitical uncertainties,
  International Journal of Forecasting 41 (2025) 953–981.
* Alpaydin (2021)

  E. Alpaydin, Machine learning, MIT press, 2021.
* Furnback et al. (2013)

  W. Furnback, B. Wang, A. Magyar,
  Are the biotechnology and pharmaceutical sectors defensive relative to the s&p 500?,
  Value in Health 16 (2013) A454.
* Wang et al. (2025)

  H. Wang, Z. Xie, D. K. Chiu, K. K. Ho,
  Multimodal market information fusion for stock price trend prediction in the pharmaceutical sector,
  Applied Intelligence 55 (2025) 77.
* Kraus and Feuerriegel (2017)

  M. Kraus, S. Feuerriegel,
  Decision support from financial disclosures with deep neural networks and transfer learning,
  Decision Support Systems 104 (2017) 38–48.
* Furnback et al. (2013)

  W. Furnback, B. Wang, A. Magyar,
  Are the biotechnology and pharmaceutical sectors defensive relative to the s&p 500?,
  Value in Health 16 (2013) A454.
* Wilms et al. (2021)

  I. Wilms, J. Rombouts, C. Croux,
  Multivariate volatility forecasts for stock market indices,
  International Journal of Forecasting 37 (2021) 484–499.
* Sadhukhan and Gupta (2025)

  P. Sadhukhan, S. Gupta,
  A graph theoretic approach to assess quality of data for classification task,
  Data and Knowledge Engineering 158 (2025) 102421.
* Lundberg and Lee (2017)

  S. M. Lundberg, S.-I. Lee,
  A unified approach to interpreting model predictions,
  Advances in neural information processing systems 30 (2017).
* Dow and Gorton (1997)

  J. Dow, G. Gorton,
  Stock market efficiency and economic efficiency: is there a connection?,
  The Journal of Finance 52 (1997) 1087–1129.
* Sufian and Chong (2008)

  F. Sufian, R. R. Chong,
  Determinants of bank profitability in a developing economy: Empirical evidence from the philippines.,
  Asian Academy of Management Journal of Accounting & Finance 4 (2008).
* Fama (1965)

  E. F. Fama,
  The behavior of stock-market prices,
  The journal of Business 38 (1965) 34–105.
* Lin and Marques (2024)

  C. Y. Lin, J. A. L. Marques,
  Stock market prediction using artificial intelligence: A systematic review of systematic reviews,
  Social Sciences and Humanities Open 9 (2024) 100864.
* Daniel et al. (1998)

  K. Daniel, D. Hirshleifer, A. Subrahmanyam,
  Investor psychology and security market under-and overreactions,
  the Journal of Finance 53 (1998) 1839–1885.
* Manahov and Hudson (2013)

  V. Manahov, R. Hudson,
  Herd behaviour experimental testing in laboratory artificial stock market settings. behavioural foundations of stylised facts of financial returns,
  Physica A: Statistical Mechanics and its Applications 392 (2013) 4351–4372.
* Schmeling (2009)

  M. Schmeling,
  Investor sentiment and stock returns: Some international evidence,
  Journal of empirical finance 16 (2009) 394–408.
* Baker and Wurgler (2007)

  M. Baker, J. Wurgler,
  Investor sentiment in the stock market,
  Journal of economic perspectives 21 (2007) 129–151.
* Baker and Wurgler (2006)

  M. Baker, J. Wurgler,
  Investor sentiment and the cross-section of stock returns,
  The journal of Finance 61 (2006) 1645–1680.
* Gandhmal and Kumar (2019)

  D. P. Gandhmal, K. Kumar,
  Systematic analysis and review of stock market prediction techniques,
  Computer Science Review 34 (2019) 100190.
* Schwert (1990)

  G. W. Schwert,
  Stock returns and real activity: A century of evidence,
  The Journal of Finance 45 (1990) 1237–1257.
* Gottschlich and Hinz (2014)

  J. Gottschlich, O. Hinz,
  A decision support system for stock investment recommendations using collective wisdom,
  Decision support systems 59 (2014) 52–62.
* Bouchaud et al. (2002)

  J.-P. Bouchaud, M. Mézard, M. Potters,
  Statistical properties of stock order books: empirical results and models,
  Quantitative finance 2 (2002) 251.
* Lai and Cho (2016)

  P.-f. B. Lai, K.-y. K. Cho,
  Relationships between stock returns and corporate financial ratios based on a statistical analysis of corporate data from the hong kong stock market,
  Public Finance Quarterly= Pénzügyi Szemle 61 (2016) 110–123.
* Bai et al. (2015)

  Z. Bai, H. Li, M. McAleer, W.-K. Wong,
  Stochastic dominance statistics for risk averters and risk seekers: An analysis of stock preferences for usa and china,
  Quantitative Finance 15 (2015) 889–900.
* Chen et al. (2003)

  A.-S. Chen, M. T. Leung, H. Daouk,
  Application of neural networks to an emerging financial market: forecasting and trading the taiwan stock index,
  Computers & Operations Research 30 (2003) 901–923.
* Jiang et al. (2022)

  M. Jiang, L. Jia, Z. Chen, W. Chen,
  The two-stage machine learning ensemble models for stock price prediction by combining mode decomposition, extreme learning machine and improved harmony search algorithm,
  Annals of Operations Research 309 (2022) 553–585.
* Kyriakou et al. (2021)

  I. Kyriakou, P. Mousavi, J. P. Nielsen, M. Scholz,
  Forecasting benchmarks of long-term stock returns via machine learning,
  Annals of Operations Research 297 (2021) 221–240.
* Li et al. (2016)

  Q. Li, Y. Chen, L. L. Jiang, P. Li, H. Chen,
  A tensor-based information framework for predicting the stock market,
  ACM Transactions on Information Systems (TOIS) 34 (2016) 1–30.
* Yang et al. (2023)

  Y. Yang, Y. Qin, Y. Fan, Z. Zhang,
  Unlocking the power of voice for financial risk prediction: A theory-driven deep learning design approach,
  Mis Quarterly 47 (2023) 63–96.
* Lee et al. (2024)

  H. Lee, J. H. Kim, H. S. Jung,
  Deep-learning-based stock market prediction incorporating esg sentiment and technical indicators,
  Scientific Reports 14 (2024) 10262.
* Wang et al. (2025)

  Y. Wang, P. Huang, J. Luo,
  Predicting stock prices based on machine learning to build self-adaptive trading strategy,
  Computational Economics (2025) 1–25.
* Hammoudeh et al. (2009)

  S. M. Hammoudeh, Y. Yuan, M. McAleer,
  Shock and volatility spillovers among equity sectors of the gulf arab stock markets,
  The Quarterly Review of Economics and Finance 49 (2009) 829–842.
* Mensi et al. (2021)

  W. Mensi, R. Nekhili, X. V. Vo, T. Suleman, S. H. Kang,
  Asymmetric volatility connectedness among us stock sectors,
  The North American Journal of Economics and Finance 56 (2021) 101327.
* Chen et al. (2018)

  H. Chen, J. Estes, W. Pratt,
  Investing in the healthcare sector: mutual funds or etfs,
  Managerial Finance 44 (2018) 495–508.
* Yousaf and Yarovaya (2022)

  I. Yousaf, L. Yarovaya,
  The relationship between trading volume, volatility and returns of non-fungible tokens: evidence from a quantile approach,
  Finance Research Letters 50 (2022) 103175.
* Yadava (2024)

  A. Yadava,
  The impact of ai-driven algorithmic trading on market efficiency and volatility: Evidence from global financial markets,
  Information Sciences 36 (2024) 102015.
* Donchian (1957)

  R. D. Donchian,
  Trend-following methods in commodity price analysis,
  Commodity Year Book (1957) 35–47.
* Bollinger (1992)

  J. Bollinger,
  Using bollinger bands,
  Stocks & Commodities 10 (1992) 47–51.
* Keltner (1960)

  C. W. Keltner,
  How to make money in commodities,
  (No Title) (1960).
* Zhu and Sun (2024)

  Z. Zhu, L. Sun,
  When buffett meets bollinger: An integrated approach to fundamental and technical analysis,
  Accounting & Finance 64 (2024) 2699–2734.
* Karathanasopoulos et al. (2016)

  A. Karathanasopoulos, C. Dunis, S. Khalil,
  Modelling, forecasting and trading with a new sliding window approach: the crack spread example,
  Quantitative Finance 16 (2016) 1875–1886.
* Garreta and Moncecchi (2013)

  R. Garreta, G. Moncecchi, Learning scikit-learn: machine learning in python, volume 2013, Packt Publishing Birmingham, 2013.
* Chicco and Jurman (2020)

  D. Chicco, G. Jurman,
  The advantages of the matthews correlation coefficient (mcc) over f1 score and accuracy in binary classification evaluation,
  BMC genomics 21 (2020) 6.
* Nguyen et al. (2024)

  M. Nguyen, B. Nguyen, M.-l. Liêu,
  Corporate financial distress prediction in a transition economy,
  Journal of Forecasting 43 (2024) 3128–3160.
* Karanasos et al. (2022)

  M. Karanasos, S. Yfanti, J. Hunter,
  Emerging stock market volatility and economic fundamentals: The importance of us uncertainty spillovers, financial and health crises,
  Annals of operations research 313 (2022) 1077–1116.
* Li et al. (2005)

  Q. Li, J. Yang, C. Hsiao, Y.-J. Chang,
  The relationship between stock returns and volatility in international stock markets,
  Journal of Empirical Finance 12 (2005) 650–665.
* Hsu (2024)

  C. Hsu,
  Activity of informed traders and stock returns,
  Managerial Finance 50 (2024) 908–919.
* Gu et al. (2021)

  D. Gu, X. Liu, H. Sun, H. Zhao,
  Strategic insider trading: Disguising order flows to escape trading competition,
  Journal of Corporate Finance 67 (2021) 101891.

## Appendix A Volatility Computation

Volatility gives a normalized measure of index fluctuations over a period. The initial step involves the estimation of the directional and magnitude changes at Day tt, denoted by r​(t)r(t), by taking the logarithm of the consecutive indices P​(t)P(t) and P​(t−1)P(t-1). The mean change is computed through the averaging of r​(t)r(t) over the days in question, followed by computing the variance, which measures the degree of dispersion around this mean. Volatility is obtained by taking the square root of the variance. For computing period-specific volatility (essential for comparing assets across different time frames), daily volatility is weighted by the square root of the number of trading days.

### A.1 1. Logarithmic Returns

Given a index series PtP\_{t}, the logarithmic return at time tt is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r​(t)=ln⁡(P​(t)P​(t−1))r(t)=\ln\left(\frac{P(t)}{P({t-1})}\right) |  | (17) |

### A.2 2. Mean Return

The average return over NN periods:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r¯=1N​∑t=1Nr​(t)\bar{r}=\frac{1}{N}\sum\_{t=1}^{N}r(t) |  | (18) |

### A.3 3. Variance of Returns

The sample variance (unbiased estimator):

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2=1N−1​∑t=1N(r​(t)−r¯)2\sigma^{2}=\frac{1}{N-1}\sum\_{t=1}^{N}(r(t)-\bar{r})^{2} |  | (19) |

### A.4 4. Volatility (Standard Deviation)

Daily volatility is the square root of variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Volatilitydaily=σ2\text{Volatility}\_{\text{daily}}=\sqrt{\sigma^{2}} |  | (20) |

### A.5 5. Periodized Volatility

Scaled by the square root of time (assuming 252 trading days/year):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Volatilityperiodized=Volatilitydaily×No. of days\text{Volatility}\_{\text{periodized}}=\text{Volatility}\_{\text{daily}}\times\sqrt{\text{No. of days}} |  | (21) |

## Appendix B Accuracy

For assessing a classification task, performance is quantified using counts derived from a confusion matrix. The Accuracy (a​c​cacc) metric represents the overall proportion of correct predictions and is formally defined as:

|  |  |  |
| --- | --- | --- |
|  | a​c​c=T​P+T​NT​P+T​N+F​P+F​Nacc=\frac{TP+TN}{TP+TN+FP+FN} |  |

where:
T​PTP = True Positives,
T​NTN = True Negatives,
F​PFP = False Positives,
F​NFN = False Negatives.

## Appendix C Matthews Correlation Coefficient (MCC) scores

It is a robust metric for evaluating binary classification models, effective across varying distributions of classes. The MCC score is high only when a model produces efficient performance for all possible classes.

MCC is calculated as:

|  |  |  |
| --- | --- | --- |
|  | MCC=T​P×T​N−F​P×F​N(T​P+F​P)​(T​P+F​N)​(T​N+F​P)​(T​N+F​N)\text{MCC}=\frac{TP\times TN-FP\times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}} |  |

For a binary classification problem, an accuracy of 0.50.5 is the standard expectation from a random classifier. In this research, we deal with a binary classification task. Accordingly, we set the threshold at 0.80.8 to consider the model to be an effective one.

### C.1 Interpretation of MCC score Ranges

MCC scores can range from (−1≤MCC≤+1-1\leq\text{MCC}\leq+1). MCC=+1\text{MCC}=+1 signifies perfect prediction (all correct, no errors). MCC≥0.7\text{MCC}\geq 0.7 indicates a very strong correlation between ground truth and predictions (excellent model).
0.5≤MCC<0.650.5\leq\text{MCC}<0.65: shows strong correlation between actual labels and predictions (good model).
0.3≤MCC<0.50.3\leq\text{MCC}<0.5: indicates a moderate performance.
0.1≤MCC<0.30.1\leq\text{MCC}<0.3: signifies a significantly weak performance with low correlation between ground truth and predictions (poor model).
MCC<0.1\text{MCC}<0.1: indicates very feeble correlation (unreliable).
MCC=0\text{MCC}=0: signifies no correlation and random prediction. This occurs when the model’s correct predictions (TP, TN) are statistically indistinguishable from its errors (FP, FN), equivalent to random guessing.
MCC=−1\text{MCC}=-1: signifies a flipping of predictions (always wrong). Consequently, we have chosen MCC=0.65\text{MCC}=0.65 as a threshold to identify efficient models.