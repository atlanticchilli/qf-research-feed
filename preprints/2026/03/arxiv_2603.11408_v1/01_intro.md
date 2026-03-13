---
authors:
- Dehao Dai
- Ding Ma
- Dou Liu
- Kerui Geng
- Yiqing Wang
doc_id: arxiv:2603.11408v1
family_id: arxiv:2603.11408
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil
  Futures Return Prediction'
url_abs: http://arxiv.org/abs/2603.11408v1
url_html: https://arxiv.org/html/2603.11408v1
venue: arXiv q-fin
version: 1
year: 2026
---


Dehao Dai

Ding Ma

Dou Liu

Kerui Geng

Yiqing Wang
[woshilucy712@gmail.com](2603.11408v1/mailto:woshilucy712@gmail.com)

###### Abstract

Forecasting crude oil prices remains challenging because market-relevant information is embedded in large volumes of unstructured news and is not fully captured by traditional polarity-based sentiment measures. This paper examines whether multi-dimensional sentiment signals extracted by large language models improve the prediction of weekly wti crude oil futures returns. Using energy-sector news articles from 2020 to 2025, we construct five sentiment dimensions covering relevance, polarity, intensity, uncertainty, and forwardness based on GPT-4o , Llama 3.2-3b , and two benchmark models, FinBERT and AlphaVantage. We aggregate article-level signals to the weekly level and evaluate their predictive performance in a classification framework. The best results are achieved by combining GPT-4o and FinBERT , suggesting that LLM-based and conventional financial sentiment models provide complementary predictive information. SHAP analysis further shows that intensity- and uncertainty-related features are among the most important predictors, indicating that the predictive value of news sentiment extends beyond simple polarity. Overall, the results suggest that multi-dimensional LLM-based sentiment measures can improve commodity return forecasting and support energy-market risk monitoring.

###### keywords:

wti crude oil futures , large language models , multi-dimensional sentiment, news-based forecasting, SHAP

\affiliation

[author1]organization=University of California San Diego,
city=La Jolla,
state=California,
country=United States
\affiliation[author2]organization=Columbia University,
city=New York,
state=New York,
country=United States
\affiliation[author3]organization=New York University,
city=New York,
state=New York,
country=United States
\affiliation[author4]organization=Tulane University,
city=New Orleans,
state=Louisiana,
country=United States
\affiliation[author5]organization=Southern Methodist University,
city=Dallas,
state=Texas,
country=United States

## 1 Introduction

Crude oil remains a cornerstone strategic resource for modern economies and plays a fundamental role in sustaining economic growth and social stability (Hamilton, [1983](#bib.bib33 "Oil and the macroeconomy since world war ii"); Barsky and Kilian, [2002](#bib.bib34 "Oil and the macroeconomy since the 1970s"); Ma et al., [2020](#bib.bib16 "Jumps and oil futures volatility forecasting: a new insight")). As the most actively traded energy commodity, crude oil prices influence inflation, industrial production, transportation costs, and financial market dynamics.
Accordingly, crude oil futures markets have become the primary venues for price discovery, and accurate forecasting of crude oil price remains a persistent challenge for market participants. There is a considerable literature to address this challenge including traditional statistical frameworks used in high-dimensional time series like ARIMA and GARCH
(Xiang and Zhuang, [2013](#bib.bib35 "Application of arima model in short-term prediction of international crude oil price"); Agnolucci, [2009](#bib.bib36 "Volatility in crude oil futures: a comparison of the predictive ability of garch and implied volatility models")), feature selection (Zhang and Wang, [2022](#bib.bib17 "Forecasting crude oil futures market returns: A principal component analysis combination approach"); Song et al., [2023](#bib.bib32 "Forecasting crude oil prices: a reduced-rank approach")) and modern machine learning techniques such as LSTM networks and deep learning models (Zhao et al., [2017](#bib.bib37 "A deep learning ensemble approach for crude oil price forecasting"); Guo et al., [2023](#bib.bib38 "Forecasting crude oil futures price using machine learning methods: evidence from china")). These models emphasize quantitative analysis of structured data to provide well-performed crude oil price forecasting and have also been widely applied to broader equity markets. However, their forecasting accuracy is constrained due to lack of the crude oil markets’ intrinsic features.

Different from equity markets, which are largely driven by firm-level fundamentals, crude oil futures markets are highly sensitive to expectation-driven risk factors, including supply disruptions, geopolitical conflicts, policy interventions, and global demand uncertainty (Ames et al., [2020](#bib.bib12 "Which risk factors drive oil futures price curves?")).
In contrast to numerical data, text data like news, reports and social media can provide a new framework to forecast crude oil prices by extracting market signals. These resources encode timely sentiment, capture shifts in expectations, and often contain policy or geopolitical cues that influence oil price dynamics. Recent work on effective crude oil price forecasting using text-based and big-data-driven models further supports this direction (Wu et al., [2021](#bib.bib39 "Effective crude oil price forecasting using new text-based and big-data-driven model")).

There is a substantial literature evaluating the role of media tone and news sentiment in asset return prediction. Early studies on textual sentiment rely on dictionary-based approaches that quantify the frequency of positive and negative words to measure tone (Tetlock, [2007](#bib.bib20 "Giving Content to Investor Sentiment: The Role of Media in the Stock Market"); Chen et al., [2018a](#bib.bib11 "NTUSD-fin: a market sentiment dictionary for financial social media data applications")). More recent work employs transformer-based models such as FinBERT to classify financial text polarity (Yahia et al., [2024](#bib.bib10 "Impact of sentiment analysis on energy sector stock prices: a finbert approach"))and forecast both returns and volatility (Li et al., [2024](#bib.bib41 "A novel secondary decomposition method for forecasting crude oil price with twitter sentiment")). Although these tools have improved sentiment measurement accuracy, they primarily focus on directional tone (positive versus negative) and sentiment intensity. However, oil futures pricing is driven not only by directional sentiment but also by forward-looking uncertainty and expectation revision. A news article may be neutral in tone yet signal elevated uncertainty or significant forward guidance regarding future supply conditions. Polarity-based measures are therefore structurally limited in capturing these economically relevant dimensions.

Recent advances in large language models (LLMs) provide an alternative framework for semantic decomposition. Unlike traditional tools, LLMs can extract multi-dimensional attributes from text, including relevance, polarity, intensity, uncertainty, and forward-looking orientation. These dimensions may better align with the theoretical drivers of commodity pricing, (Kim et al., [2023](#bib.bib42 "LLMs analyzing the analysts: do bert and gpt extract more value from financial analyst reports?"); Wang et al., [2025a](#bib.bib43 "A novel forecasting framework leveraging large language model and machine learning for methanol price"); Jeong and Ahn, [2025](#bib.bib40 "Energy organization sentiment and oil return forecast")) particularly in markets where geopolitical risk and expectation formation play central roles. Building on this insight, we examine whether LLM-derived signals offer incremental predictive value for wti crude oil futures.

In this papeinvestigates whether multi-dimensional sentiment signals extracted by LLMs provide incremental predictive power for weekly returns of wti crude oil futures. Using energy-related news articles from 2020 to 2025 from AlphaVantage, we construct weekly aggregated sentiment features generated by three models: GPT-4o , Llama 3.2-3b , and FinBERT . We compare their predictive performance using a LightGBM classifier and evaluate feature contributions through SHAP-based explainability analysis.

Our findings suggest that LLM-derived uncertainty and forward-looking dimensions exhibit statistically and economically significant predictive power beyond traditional polarity measures. Multi-dimensional
LLM-based sentiment measures can improve commodity return forecasting
and support energy-market risk monitoring.Our findings contribute to the emerging area of LLM applications in financial economics and provide new evidence on the importance of multi-dimensional textual signals in commodity futures forecasting.

The remainder of the paper is organized as follows. Section [2](#S2 "2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") reviews related work. Section [3](#S3 "3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") describes the end-to-end workflow pipeline from data collection to prediction modeling evaluation. Section [4](#S4 "4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") reports empirical results, and Section [5](#S5 "5 Conclusions ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") discusses the results and future directions.

## 2 Related Literature

### 2.1 Crude Oil Futures Forecasting

Predicting crude oil price movements has drawn scholars’ interest due to the oil market’s economic importance and the naturally high volatility of crude oil prices. Early economic approaches rely on traditional econometric and statistical models, including ARIMA, volatility models, and market-based predictors. Short-term forecasting with ARIMA and linear time series models remains a common benchmark (Xiang and Zhuang, [2013](#bib.bib35 "Application of arima model in short-term prediction of international crude oil price"); Nasir et al., [2023](#bib.bib58 "A new approach for forecasting crude oil prices based on stochastic and deterministic influences of lmd using arima and lstm models")). Earlier volatility-oriented studies, such as Cunado and Perez De Gracia ([2005](#bib.bib14 "Oil prices, economic activity and inflation: evidence for some Asian countries")), highlighted the strong macro-financial linkages surrounding oil price dynamics, and Agnolucci ([2009](#bib.bib36 "Volatility in crude oil futures: a comparison of the predictive ability of garch and implied volatility models")) showed that conditional heteroskedastic models provide important insights into the time-varying uncertainty of crude oil futures markets.

There is also considerable literature that emphasizes machine learning and deep learning methods to capture the strong nonlinearity, regime dependence, and complex maturity structure of oil futures markets. For example, Baruník and Malinska ([2016](#bib.bib56 "Forecasting the term structure of crude oil futures prices with neural networks")) modeled the crude oil futures curve through a dynamic Nelson–Siegel framework enhanced by neural networks, showing that nonlinear methods can improve forecasts of the term structure. Focusing on the Chinese market, Guo et al. ([2023](#bib.bib38 "Forecasting crude oil futures price using machine learning methods: evidence from china")) and Zhai et al. ([2025](#bib.bib57 "Research on crude oil futures price prediction methods: a perspective based on quantum deep learning")) further developed the framework of deep learning to exploit historical prices, volatility, and other nonlinear features to enhance crude oil futures forecasting accuracy, while Zhao et al. ([2017](#bib.bib37 "A deep learning ensemble approach for crude oil price forecasting")) and Guan and Gong ([2023](#bib.bib61 "A new hybrid deep learning model for monthly oil prices forecasting")) proposed deep neural and hybrid learning models in extracting latent patterns from highly volatile oil price series.

Moreover, recent studies adopt hybrid and multi-step forecasting frameworks to improve predictive performance over longer horizons. For instance, Duan et al. ([2022](#bib.bib59 "A novel dynamic time-delay grey model of energy prices and its application in crude oil price forecasting")) developed a novel crude oil futures forecasting approach that combines multiple modeling stages, and Chen et al. ([2018b](#bib.bib60 "Multi-step-ahead crude oil price forecasting using a hybrid grey wave model")) showed that hybrid designs can achieve superior performance in multi-step-ahead prediction by integrating complementary information from different model classes.

A consistent finding across this literature is that energy markets are highly sensitive to expectation-driven shocks, like geopolitical events, OPEC+ policy announcements, and demand uncertainty, which has motivated researchers to integrate news-based information into forecasting models. For example, Cepni et al. ([2022](#bib.bib62 "News media and attention spillover across energy markets: a powerful predictor of crude oil futures prices")) adopted news media and attention spillovers across energy markets to possess significant predictive content for crude oil futures prices; Li et al. ([2019](#bib.bib63 "Text-based crude oil price forecasting: a deep learning approach")) proposed a text-based deep learning approach that exploits information embedded in online news media to improve crude oil price forecasting performance; Sadik et al. ([2020](#bib.bib64 "Forecasting crude oil futures prices using global macroeconomic news sentiment")) incorporated macroeconomic news into a predictive model for forecasting crude oil futures prices.

### 2.2 Sentiment Analysis in Finance

Sentiment analysis (Medhat et al., [2014](#bib.bib71 "Sentiment analysis algorithms and applications: a survey")) has become an important research area in finance to analyze how people’s opinions and emotions affect financial decisions. Earlier studies used a traditional “word count” approach (Guo et al., [2016](#bib.bib66 "Textual analysis and machine leaning: crack unstructured data in finance and accounting"); Loughran and McDonald, [2016](#bib.bib70 "Textual analysis in accounting and finance: a survey")) to employ sentiment analysis techniques. The most popular word lists used in finance research are the Harvard IV psychosocial word lists (Kearney and Liu, [2014](#bib.bib65 "Textual sentiment in finance: a survey of methods and models")), which have also been developed in academic finance (Tetlock, [2007](#bib.bib20 "Giving Content to Investor Sentiment: The Role of Media in the Stock Market"); Tetlock et al., [2008](#bib.bib72 "More than words: quantifying language to measure firms’ fundamentals"); Twedt and Rees, [2012](#bib.bib73 "Reading between the lines: an empirical examination of qualitative attributes of financial analysts’ reports")). Bollen et al. ([2011](#bib.bib24 "Twitter mood predicts the stock market")) and Siganos et al. ([2017](#bib.bib74 "Divergence of sentiment and stock market trading")) used general dictionaries to test for relationships between sentiment from social media and stock index returns.

In recent years, machine learning has challenged traditional approaches due to the lack of accuracy in dictionary methods (Guo et al., [2016](#bib.bib66 "Textual analysis and machine leaning: crack unstructured data in finance and accounting"); Renault, [2017](#bib.bib69 "Intraday online investor sentiment and return patterns in the us stock market"); McGurk et al., [2020](#bib.bib68 "Stock returns and investor sentiment: textual analysis and social media")). A commonly used ML algorithm is the probabilistic Naive Bayesian classifier to detect sentiment in finance (Antweiler and Frank, [2004](#bib.bib75 "Is all that talk just noise? the information content of internet stock message boards"); Li, [2010](#bib.bib76 "The information content of forward-looking statements in corporate filings—a naïve bayesian machine learning approach"); Sprenger et al., [2014](#bib.bib77 "Tweets and trades: the information content of stock microblogs")). Some other works adopted the Reuters NewsScope Sentiment Engine (Groß-Klußmann and Hautsch, [2011](#bib.bib80 "When machines read the news: using automated text analytics to quantify high frequency news-implied market reactions"); Sun et al., [2016](#bib.bib78 "Stock return predictability and investor sentiment: a high-frequency perspective"); Audrino and Tetereva, [2019](#bib.bib79 "Sentiment spillover effects for us and european companies")). Recent work introduced the transformer architecture (Sun et al., [2019](#bib.bib81 "How to fine-tune bert for text classification?"); Hiew et al., [2019](#bib.bib82 "BERT-based financial sentiment index and lstm-based stock return predictability"); Huang et al., [2023](#bib.bib7 "FinBERT: a large language model for extracting information from financial text"); Lopez-Lira and Tang, [2023](#bib.bib55 "Can chatgpt forecast stock price movements? return predictability and large language models"); Touvron et al., [2023](#bib.bib54 "Llama: open and efficient foundation language models")) to analyze the sentiment in the finance domain, which is also a highlight technique in natural language processing. More discussions can be followed in Todd et al. ([2024](#bib.bib83 "Text-based sentiment analysis in finance: synthesising the existing literature and exploring future directions")).

### 2.3 Multi-Dimensional Sentiment and Uncertainty

The multi-dimensionality of sentiment has been further emphasized by studies distinguishing between rational uncertainty and behavioral sentiment.
Saravanaraj et al. ([2025](#bib.bib85 "Sentimental analysis to predict stock market using in neutrosophic time series.")); Kang ([2025](#bib.bib84 "Multidimensional investor sentiment and stock market volatility in china: measurement, mechanisms and applications")); Eckhaus ([2026](#bib.bib86 "Data-driven insights: leveraging sentiment analysis and latent profile analysis for financial market forecasting")) proposed a multidimensional sentiment model to examine the varying influence of investor sentiment on stock market volatility and stock returns. Modern machine learning techniques are also used in multi-dimensional sentiment analysis. For example, Wang et al. ([2025b](#bib.bib87 "Deep learning-based multi-dimensional investor sentiment and stock liquidity: evidence from china")) proposed a deep learning-based model to fuse various investor sentiment information represented through financial texts.

Uncertainty is also a crucial factor in financial asset pricing. Merton ([1973](#bib.bib88 "An intertemporal capital asset pricing model")) introduced the uncertain shifts in investment opportunities into the traditional capital asset pricing model. Under this framework, there are considerable works to study the relationship between uncertainty and pricing (Rigotti and Shannon, [2005](#bib.bib89 "Uncertainty and risk in financial markets"); Jiang et al., [2005](#bib.bib90 "Information uncertainty and expected returns"); Zhang, [2006](#bib.bib91 "Information uncertainty and analyst forecast behavior"); Arnold and Vrugt, [2008](#bib.bib92 "Fundamental uncertainty and stock market volatility"); Dash et al., [2021](#bib.bib94 "Economic policy uncertainty and stock market liquidity: evidence from g7 countries"); Asgharian et al., [2023](#bib.bib95 "The effect of uncertainty on stock market volatility and correlation")). Some recent studies have extended previous research. For example, Birru and Young ([2022](#bib.bib97 "Sentiment and uncertainty")) first investigated the interaction between investor sentiment and uncertainty and introduced the volatility index to measure the dynamic uncertainty in the market. Seok et al. ([2024](#bib.bib96 "Dual effects of investor sentiment and uncertainty in financial markets")) concluded that the effect of daily sentiment on short-term returns is more significant when uncertainty is increased. More recent discussions on uncertainty can be found in Arnold and Vrugt ([2010](#bib.bib93 "Treasury bond volatility and uncertainty about monetary policy")); Segal et al. ([2015](#bib.bib98 "Good and bad uncertainty: macroeconomic and financial market implications")); Manela and Moreira ([2017](#bib.bib99 "News implied volatility and disaster concerns")).

## 3 Methodology

### 3.1 Data Source and Cleaning

We extract energy-sector news articles from the AlphaVantage News Sentiment
API (Alpha Vantage Inc., [2026](#bib.bib9 "Alpha vantage api: financial market data and news sentiment")). AlphaVantage is a financial data provider offering market data APIs covering equities, commodities, news, and other information. The available news dataset is accompanied by topic and ticker tags to facilitate filtering. To restrict to crude oil-related content, we only extract news with the energy\_transportation topic tag.

The full sample comprises news articles spanning six years, from 1 January 2020 to 31 December 2025, yielding 29,153 articles after deduplication. To accommodate the API’s constraint of 1,000 articles per call, articles were retrieved on a monthly basis and stored in raw JSON format prior to processing. Subject to budget and computational constraints, we draw a stratified random sample of 20%20\% of the full corpus (8,639 articles) for sentiment analysis extraction. Stratification is performed by calendar month, ensuring uniform temporal coverage across the whole sample window from 2020 to 2025. The same sample is used for all three extraction models to ensure comparability. Table [1](#S3.T1 "Table 1 ‣ 3.1 Data Source and Cleaning ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") provides descriptive statistics for the
article corpus.

Table 1: News Article Corpus: Summary Statistics

|  |  |  |
| --- | --- | --- |
|  | Full Sample | Sentiment Sample (20%) |
| Total number of articles | 29,153 | 8,639 |
| Date range | 01/01/2020–12/31/2025 | |
| Avg. articles/week | 93 | 28 |

Daily closing prices for the front-month wti crude oil futures contract (CL=F) are obtained from Yahoo Finance via the yfinance Python library.
We compute weekly log returns as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=ln⁡(PtPt−1),r\_{t}=\ln\!\left(\frac{P\_{t}}{P\_{t-1}}\right), |  | (1) |

where PtP\_{t} denotes the closing price on the last trading day of week tt.

The full sample spans 1,509 trading days covering 314 weeks. The mean of weekly log return is 0.18%0.18\% with standard deviation 6.37%6.37\%. The minimum return happened at week 16 March 2020 to 20 March 2020 with −29.31%-29.31\% log return while the maximum happened at week 30 March 2020 to 30 April 2020 with 31.75%31.75\% log return. Out of 314 weeks, the first week (12/30/2019 - 01/03/2020) does not yield a valid weekly return, 166 weeks (52.87%) are classified as up-weeks with positive weekly log return and 147 weeks (46.82%) as down-weeks with negative values.

The binary prediction target is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=𝟏​[rt+1>0],y\_{t}=\mathbf{1}\!\left[r\_{t+1}>0\right], |  | (2) |

i.e., whether the wti weekly log return in week t+1t+1 is positive.
All sentiment features used to predict yty\_{t} are constructed from news
articles published no later than the end of week tt to prevent
look-ahead bias.

### 3.2 Sentiment Extraction

We consider three models to extract sentiment signals, including GPT-4o (Achiam et al., [2023](#bib.bib8 "Gpt-4 technical report")), Llama 3.2-3b (Grattafiori et al., [2024](#bib.bib6 "The llama 3 herd of models")), and
FinBERT (Huang et al., [2023](#bib.bib7 "FinBERT: a large language model for extracting information from financial text")). The three models represent a
spectrum of architectural approaches. GPT-4o serves as a
state-of-the-art instruction-tuned large language model with strong semantic reasoning capabilities; Llama 3.2-3b provides a lightweight open-source alternative that enables cost-efficient inference; and FinBERT offers a domain-specific encoder fine-tuned on financial text, serving as a competitive supervised baseline.

Given a structured prompt (see  [A](#A1 "Appendix A System Prompts ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction")),GPT-4o and Llama 3.2-3b produce five sentiment dimensions for each article:

* •

  Relevance: measures whether an article contains information pertinent to wti crude oil markets or the broader energy sector, ranging from 0 (no relevance) to 1 (highly relevant).
* •

  Polarity: captures the directional sentiment of an article, reflecting whether the content conveys a bullish or bearish outlook for crude oil prices, ranging from −1-1 (extremely bearish) to 11 (extremely bullish).
* •

  Intensity: quantifies the strength or conviction of the expressed sentiment, distinguishing between mildly and strongly worded articles of the same polarity, ranging from 0 (weak) to 1 (strong).
* •

  Uncertainty: reflects the degree to which an article expresses ambiguity, risk, or lack of clarity about future market outcomes. It captures hedging language and contested forecasts, ranging from 0 (certain) to 1 (highly uncertain).
* •

  Forwardness: measures the extent to which an article contains forward-looking language, such as projections, expectations, or policy outlooks, ranging from 0 (past events) to 1 (future outlook).

FinBERT , by contrast, is a classification model fine-tuned for
sentiment analysis in the financial domain and provides only polarity and intensity scores. The AlphaVantage API supplies a polarity score for each article without additional dimensions.
Table [2](#S3.T2 "Table 2 ‣ 3.2 Sentiment Extraction ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") provides an overview of the sentiment
dimensions available from each model.

Table 2: Sentiment Dimensions by Model

| Model | Relevance | Polarity | Intensity | Uncertainty | Forwardness |
| --- | --- | --- | --- | --- | --- |
| Range | [0, 1] | [-1, 1] | [0, 1] | [0, 1] | [0, 1] |
| GPT-4o | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Llama 3.2-3b | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| FinBERT |  | ✓\checkmark | ✓\checkmark |  |  |
| AlphaVantage |  | ✓\checkmark |  |  |  |

Formally, for article ii published in week tt, each model produces a
score vector:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐬t,i=(r​et,i,pt,i,ιt,i,ut,i,ft,i)\mathbf{s}\_{t,i}=(re\_{t,i},\;p\_{t,i},\;\iota\_{t,i},\;u\_{t,i},\;f\_{t,i}) |  | (3) |

where r​et,ire\_{t,i} denotes relevance, pt,ip\_{t,i} denotes polarity, ιt,i\iota\_{t,i} denotes intensity,
ut,iu\_{t,i} denotes uncertainty, and ft,if\_{t,i} denotes forwardness.
All dimensions are elicited on a continuous scale via structured
prompts.

To aggregate article-level scores to the weekly level, we compute a relevance-weighted mean for each sentiment dimension:

|  |  |  |  |
| --- | --- | --- | --- |
|  | w¯t=∑i∈𝒜tr​et,i⋅wt,i∑i∈𝒜tr​et,i,w∈{p,ι,u,f},\bar{w}\_{t}=\frac{\sum\_{i\in\mathcal{A}\_{t}}re\_{t,i}\cdot w\_{t,i}}{\sum\_{i\in\mathcal{A}\_{t}}re\_{t,i}},\quad w\in\{p,\iota,u,f\}, |  | (4) |

where 𝒜t\mathcal{A}\_{t} is the set of articles published in week tt. Relevance scores serve as aggregation weights on the grounds that articles with stronger topical alignment to wti markets should exert greater influence on the weekly signal. As relevance is already incorporated into the weighting scheme, no additional relevance filtering is applied.

Following the weekly aggregated means, we additionally construct two dispersion features, the within-week standard deviation of polarity and the within-week standard deviation of uncertainty, to capture the degree of disagreement across articles within each week. A high standard deviation of polarity indicates that the market is simultaneously receiving conflicting signals, reflecting bullish opinion in some articles and bearish opinion in others. Similarly, a high standard deviation of uncertainty indicates that articles within the same week express markedly different levels of ambiguity, which may carry information about the informativeness of the prevailing news flow.

In addition to weekly level features, we construct first-difference momentum terms for polarity, uncertainty, and forwardness as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​w¯t=w¯t−w¯t−1,w∈{p,u,f},\Delta\bar{w}\_{t}=\bar{w}\_{t}-\bar{w}\_{t-1},\quad w\in\{p,u,f\}, |  | (5) |

The rationale for including momentum is grounded in the behavioral finance literature, which documents that sentiment trends, rather than sentiment levels alone, carry predictive information about asset returns (Baker and Wurgler, [2006](#bib.bib4 "Investor sentiment and the cross-section of stock returns"); Uhl et al., [2015](#bib.bib5 "What’s in the news? using news sentiment momentum for tactical asset allocation"))
A sustained shift in polarity, for instance, may signal an emerging consensus that is not yet reflected in prices, while a sudden reversal may indicate that the prevailing narrative is losing credibility.

We select these three features for momentum construction is due to their distinct temporal dynamics. Polarity captures the directional tone of market sentiment, whose trend is directly relevant to price momentum. Uncertainty momentum reflects whether market ambiguity is rising or falling week-on-week, a signal that is particularly informative around supply shocks and geopolitical events when the information environment is rapidly evolving. Forwardness momentum captures shifts in the degree to which news coverage is oriented toward future expectations versus past events, which we interpret as a proxy for changing market attention.

In contrast, momentum terms for relevance and intensity are excluded. Relevance is related to news connection to the market and its week-on-week change does not carry an interpretable market meaning. Intensity, while useful as a weekly level feature, does not have a well-defined directional implication. An increase in emotional strength across articles is not systematically associated with a particular price direction.

In total, we construct 31 features as the candidate independent features and the full list is provided in [B](#A2 "Appendix B Feature List ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction")

### 3.3 Prediction Model

We consider LightGBM (Ke et al., [2017](#bib.bib51 "Lightgbm: a highly efficient gradient boosting decision tree")) as the prediction model, a gradient boosting framework well-suited for tabular dataset with moderate sample size and robust to feature scale differences (Grinsztajn et al., [2022](#bib.bib2 "Why do tree-based models still outperform deep learning on typical tabular data?"); Shwartz-Ziv and Armon, [2022](#bib.bib3 "Tabular data: deep learning is not all you need")).

Regarding feature selection, we consider six sets of different feature combinations as follows.

* •

  Set AV Baseline: features from AlphaVantage only, serving as the benchmark as it relies solely on the proprietary AlphaVantage score.
* •

  Set Tradition:features from AlphaVantage and FinBERT , representing a conventional multi-source combination without LLM-derived dimensions.
* •

  Set GPT: features from GPT-4o only.
* •

  Set Llama: features from Llama 3.2-3b only.
* •

  Set LLM: features from GPT-4o and Llama 3.2-3b combined
* •

  Set GPT-FinBert: features from GPT-4o and FinBERT combined

We train separate LightGBM models for each feature set. To optimize hyperparameters, we employ Optuna (Akiba et al., [2019](#bib.bib49 "Optuna: a next-generation hyperparameter optimization framework")), a hyperparameter optimization framework based on the Tree-structured Parzen Estimator (TPE) algorithm (Bergstra et al., [2011](#bib.bib50 "Algorithms for hyper-parameter optimization")). TPE constructs two probabilistic models p​(x)p(x) and g​(x)g(x) over the hyperparameter space, representing the densities of configurations that yield above- and below-threshold performance respectively, and selects candidates by maximizing the ratio p​(x)g​(x)\frac{p(x)}{g(x)}, which is equivalent to maximizing the Expected Improvement. This approach is more sample-efficient than grid search or random search, particularly in high-dimensional hyperparameter spaces. The whole tuning process is performed via time-series cross-validation with K=5K=5 expanding windows, using Area Under the Receiver Operating Characteristic Curve (AUROC) as the optimization criteria.

To evaluate model performance, we consider three metrics as follows:

* •

  Area Under the Receiver Operating Characteristic Curve (AUROC): It summaries classification performance across all possible decision thresholds by plotting the true positive rate against the false positive rate. A value of 0.5 is equivalent to random guessing, while a value of 1.0 indicates perfect discriminative ability.
* •

  Accuracy: It measures the proportion of weeks for which the predicted direction matches the realized direction. Unlike AUROC, it evaluates the binary classification decision at a fixed threshold rather than across all thresholds. Given that positive-return weeks is approximately 53.03%53.03\% of the sample, we set the classification threshold to match the empirical class distribution.
* •

  Information Coefficient (IC):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | IC=ρs(p^t,,rt)=1−6​∑dt2T​(T2−1)\text{IC}=\rho\_{s}\left(\hat{p}\_{t},,r\_{t}\right)=1-\frac{6\sum d\_{t}^{2}}{T(T^{2}-1)} |  | (6) |

  where p^t\hat{p}\_{t} is the predicted probability of a positive return in week tt, rtr\_{t} is the realized week return, and dtd\_{t} is the difference in ranks between p^t\hat{p}\_{t} and rtr\_{t}. IC measures the rank correlation between predicted probabilities and actual returns, capturing whether weeks assigned higher predicted probabilities tend to realized higher returns. Unlike AUC and Accuracy, IC evaluates the quality of the full predicted distribution rather than the binary classification decision.

### 3.4 SHAP-Based Interpretation of Feature Importance

To interpret the contribution of sentiment features to the predictive model,
we use SHapley Additive exPlanations (SHAP) (Lundberg and Lee, [2017](#bib.bib1 "A unified approach to interpreting model predictions")) for the fitted LightGBM classifier. SHAP is a post-hoc explainability framework grounded in cooperative game theory. It attributes a model’s prediction to individual input features through Shapley values, which quantify each feature’s margnial contribution to the model output.

Formally, the Shapley value for feature jj is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕj=∑S⊆F∖{j}|S|!​(|F|−|S|−1)!|F|!​[fS∪{j}​(xS∪{j})−fS​(xS)]\phi\_{j}=\sum\_{S\subseteq F\setminus\{j\}}\frac{|S|!(|F|-|S|-1)!}{|F|!}\left[f\_{S\cup\{j\}}(x\_{S\cup\{j\}})-f\_{S}(x\_{S})\right] |  | (7) |

where FF denotes the full set of features, and SS represents a subset of
features excluding feature ii. The term fS​(xS)f\_{S}(x\_{S}) denotes the model
output when only the feature subset SS is observed, while
fS∪{j}​(xS∪{j})f\_{S\cup\{j\}}(x\_{S\cup\{j\}}) represents the prediction when feature
jj is added to the subset. The difference between the two terms therefore captures the marginal contribution of feature jj, averaged over all possibile feature coalitions.

SHAP provides both local and global interpretability. At the local
level, the value ϕi,j\phi\_{i,j} quantifies the contribution of
feature jj to the prediction for observation ii. A positive SHAP value
indicates that the feature pushes the prediction toward the positive class, while a negative value indicates a downward contribution. At the global level, the overall feature importance is evaluated by the mean absolute SHAP value across all observations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φj=1N​∑i=1N|ϕi,j|\Phi\_{j}=\frac{1}{N}\sum\_{i=1}^{N}|\phi\_{i,j}| |  | (8) |

where NN is the total number of observations. Features with larger mean absolute SHAP values exert greater influence on the model’s predictions and are therefore interpreted as more important drivers of weekly wti futures return direction.

## 4 Results

### 4.1 Inter-Model Agreement

Table 3: Distributional Properties of Polarity Scores Across Models

|  | GPT-4o | Llama 3.2 | FinBERT | AlphaVantage |
| --- | --- | --- | --- | --- |
| Mean | 0.2952 | 0.1109 | 0.3050 | 0.2177 |
| Stand Deviation | 0.4323 | 0.3458 | 0.6801 | 0.2818 |
| Min | -0.9000 | -1.0000 | -0.9772 | -0.9144 |
| Q​25%Q25\% | 0.0000 | 0.0000 | 0.0000 | 0.0368 |
| Median | 0.3000 | 0.0000 | 0.6491 | 0.2758 |
| Q​75%Q75\% | 0.7000 | 0.2000 | 0.9000 | 0.4218 |
| Max | 0.9000 | 0.9000 | 0.9616 | 0.9419 |

Table [3](#S4.T3 "Table 3 ‣ 4.1 Inter-Model Agreement ‣ 4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") summarizes the distribution of polarity scores across approaches. All approaches yield positive mean polarity scores, ranging from 0.11 for Llama 3.2-3b to 0.31 FinBERT , suggesting that energy news carries a modest positive tone on average. Among those approaches, Llama 3.2-3b exhibits the most conservative scoring pattern, with both the 25%25\% quartile and the median as zero. In fact, 3608 out of 8639 news (41.7%41.7\%) receives a polarity score of zero under Llama 3.2-3b .

FinBERT exhibits a substantially different distribution from the LLM-based measures. Its median polarity is 0.65 and the third quartile is 0.90, indicating that many articles are assigned strongly positive scores, although the distribution also includes a long negative tail, with a minimum of -0.98. This pattern is consistent with the distinct architecture of this model. As a classification model, FinBERT produces polarity scores derived from class probabilities, which tend to place greater mass near the extremes. By contrast, GPT-4o and Llama 3.2-3b produce smoother and more graduated polarity assessments.

![Refer to caption](2603.11408v1/polarity_correlation_heatmap.png)


Figure 1: Pairwise Polarity Correlation Across Models

Figure [1](#S4.F1 "Figure 1 ‣ 4.1 Inter-Model Agreement ‣ 4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") presents the pairwise Pearson correlation among polarity scores generated by the four sentiment sources. All correlations are positive and moderate, ranging from 47%47\% to 68%68\%. This pattern indicates that the models share a common directional signal, but also retain substantial cross-model variation.GPT-4o and Llama 3.2-3b exhibit the highest correlation (68.1%68.1\%), which is consistent with the fact that both are instruction-tuned language models evaluated under the same prompt design. By contrast, Llama 3.2-3b shows the weakest agreement with FinBERT (47.0%47.0\%) and AlphaVantage (47.4%47.4\%), suggesting that the smaller language model captures a somewhat different component of sentiment from both the larger LLM and the more conventional approach. Overall, the moderate correlation motivates for treating these sentiment signals as complementary inputs rather than redundant proxies, leading the multi-model feature construction in Section [3.3](#S3.SS3 "3.3 Prediction Model ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").

Figure [2](#S4.F2 "Figure 2 ‣ 4.1 Inter-Model Agreement ‣ 4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") compares the weekly aggregated sentiment dimensions by GPT-4o and Llama 3.2-3b . GPT-4o consistently yields higher average scores across all five dimensions, suggesting greater sensitivity to sentiment-related cues in energy news. Polarity displays the strongest alignment with correlation 52.7%52.7\%, indicating the two models capture broadly similar directional sentiment. Conversely, the differences become more pronounced for other dimensions, particularly forwardness and intensity, where Llama 3.2-3b exhibits substantially greater dispersion. Taken together, these findings indicate that GPT-4o and Llama 3.2-3b are not interchangeable sentiment sources. Instead, each appears to preserve distinct information, provideing empirical support for combining them in the predictive feature set.

![Refer to caption](2603.11408v1/dimension_boxplot_with_rho.png)


Figure 2: Sentiment Dimension Distributions: GPT-4o vs Llama 3.2

### 4.2 Directional Prediction Performance

Figure [3](#S4.F3 "Figure 3 ‣ 4.2 Directional Prediction Performance ‣ 4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") and Table [4](#S4.T4 "Table 4 ‣ 4.2 Directional Prediction Performance ‣ 4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") report the out-of-sample performance of the six feature sets under five-fold time series cross-validation. All models achieve AUC values above the benchmark baseline of 0.5, indicating that sentiment-based features contain meaningful predictive information for wti weekly return direction.
The AV Baseline, sourced from AlphaVantage proprietary sentiment scores, has an AUC of 0.569 and an IC of 0.091, making it weakest performance. Expanding the baseline with FinBERT signals improves the performance with AUC of 0.620 and IC of 0.157. This improvement suggests that combining multiple sentiment sources adds incremental predictive information.

Among the LLM-based sources, GPT-4o alone achieves a mean AUC of 0.634 and the highest mean IC of 0.249, outperforming both Llama 3.2-3b and the LLM Ensemble. This pattern is consistent with the earlier score distribution evidence in Section [4.1](#S4.SS1 "4.1 Inter-Model Agreement ‣ 4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"), where Llama 3.2-3b displays less stable sentiment scoring across all the five dimensions. Notably, combining GPT-4o and Llama 3.2-3b does not improve upon GPT-4o alone, suggesting that signals from Llama 3.2-3b may introduce noise rather than complementary information.

The highest AUC is obtained by the combination of GPT-4o and FinBERT . Although its IC is slighly lower than that of GPT-4o alone (0.228 versus 0.249), the difference is small and should be interpreted cautiously. Overall, these results suggest that FinBERT signal provide additional information helpful for classification performance, which is not captured by GPT-4o alone.

Table 4: Cross-Validation Prediction Performance Across Feature Sets

| Model | AUC | | Accuracy | | IC | |
| --- | --- | --- | --- | --- | --- | --- |
|  | Mean | Std | Mean | Std | Mean | Std |
| AV Baseline | 0.5694 | 0.0349 | 0.4902 | 0.0328 | 0.0910 | 0.0894 |
| Tradition | 0.6200 | 0.0666 | 0.5216 | 0.0505 | 0.1571 | 0.1398 |
| GPT-4o | 0.6336 | 0.0563 | 0.5373 | 0.0490 | 0.2490 | 0.0372 |
| Llama 3.2 | 0.5892 | 0.1013 | 0.5137 | 0.0454 | 0.1147 | 0.1586 |
| LLM Ensemble | 0.5974 | 0.0439 | 0.5804 | 0.0697 | 0.2118 | 0.0620 |
| GPT + FinBERT | 0.6515 | 0.0546 | 0.5608 | 0.0686 | 0.2283 | 0.0987 |

![Refer to caption](2603.11408v1/phase3_model_comparison.png)


Figure 3: Model Comparisons

### 4.3 SHAP Feature Importance

![Refer to caption](2603.11408v1/phase3_shap_analysis.png)


Figure 4: SHAP Analyais

Figure [4](#S4.F4 "Figure 4 ‣ 4.3 SHAP Feature Importance ‣ 4 Results ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction") presents the SHAP-based feature importance analysis for the GPT + FinBERT model, computed on the held-out test set. The left panel reports mean absolute SHAP values, while the right panel shows the direction and magnitude of each feature’s contribution to the model output.The two most important features are gpt\_intensity\_mean and finbert\_polarity\_std, followed by gpt\_uncertainty\_momentum. The prominence of intensity and uncertainty, rather than polarity, suggests that dimensions beyond directional sentiment contain meaningful predictive information for wti weekly return direction. Notably, finbert\_polarity\_std ranks second overall, suggesting that cross-article sentiment variation is the primary channel through which FinBERT contributes to the ensemble. This findings is consistent with the multi-model design, as GPT-4o and FinBERT appear to capture distinct aspects of the information environment. However, gpt\_article\_count and finbert\_article\_count have negligible contribution, indicating that article volume alone adds little incremental predictive content once sentiment features are included.

The SHAP summary plot provides additional insight into the direction of feature effects. High values of gpt\_intensity\_mean are associated with positive SHAP contributions, indicating that weeks with stronger overall intensity are more likely to be classified as up-weeks. In contrast, higher gpt\_uncertainty\_mean is associated with negative SHAP values, suggesting that elevated aggregate uncertainty pushes predictions to down-weeks. Interestingly, gpt\_uncertainty\_momentum exhibits the opposite pattern, with rising uncertainty associated with positive SHAP contributions. This observation suggests that the level and the change in uncertanity may convey different predictive information to the model.

## 5 Conclusions

This paper examines whether multi-dimensional sentiment signals extracted by large language models provide incremental predictive content for weekly wti crude oil futures returns. Using energy-sector news articles from 2020 to 2025, we construct five sentiment dimensions, including relevance, polarity, intensity, uncertainty, and forwardness, based on GPT-4o and Llama 3.2-3b , and benchmark them against FinBERT and the AlphaVantage sentiment measures.

Our findings are twofold. First, the combination of GPT-4o and FinBERT delivers the strongest overall predictive performance among the feature sets considered, indicating that richer model-based sentiment representations contain incremental forecasting information. Second, the SHAP analysis shows that intensity and uncertainty-related features rank among the most important predictors, suggesting that the predictive content of news sentiment extends beyond polarity alone.

From a practical perspective, the results suggest that commodity investors, trading desks, and risk managers may benefit from supplementing traditional sentiment monitoring with LLM-based measures of uncertainty and sentiment intensity. More broadly, the evidence indicates that multi-dimensional sentiment extraction can improve the informational value of news-based signals in commodity return prediction.

This study has several limitations. The analysis focuses on a single commodity and a single news source, and the weekly forecasting horizon may not generalize to higher-frequency settings. Future research could extend the framework to other energy commodities, incorporate additional data sources such as shipping or satellite information, and evaluate performance at shorter horizons. The choice of GPT-4o and Llama 3.2-3b are based to a cost-performance tradeoff that merits further investigation as LLM models continue to improve.

## Acknowledgments

During the preparation of this manuscript, the authors used ChatGPT for the purposes of manuscript polishing only. The authors have reviewed and edited the manuscript and take full responsibility for the content of this publication.

## Appendix A System Prompts

Below is the system prompt designed for five dimension extraction using LLM models.

[⬇](data:text/plain;base64,WW91IGFyZSBhIGZpbmFuY2lhbCBuZXdzIGFuYWx5c3Qgc3BlY2lhbGl6aW5nIGluIGVuZXJneSBtYXJrZXRzLgoKQW5hbHl6ZSB0aGUgZm9sbG93aW5nIG5ld3MgYXJ0aWNsZSBhbmQgcmV0dXJuIGEgSlNPTiBvYmplY3Qgd2l0aCBleGFjdGx5IHRoZXNlIGZpZWxkczoKCnsKICAicmVsZXZhbmNlIjogZmxvYXQsICAgICAgLy8gUmVsZXZhbmNlIHRvIGVuZXJneSBtYXJrZXRzIChvaWwsIGdhcywgY29hbCwgZW5lcmd5IHBvbGljeSk6IDAuMCAodW5yZWxhdGVkKSB0byAxLjAgKGRpcmVjdGx5IHJlbGV2YW50KQogICJwb2xhcml0eSI6IGZsb2F0LCAgICAgICAvLyBPdmVyYWxsIHNlbnRpbWVudCB0b3dhcmQgZW5lcmd5IG1hcmtldHM6IC0xLjAgKHZlcnkgbmVnYXRpdmUpIHRvICsxLjAgKHZlcnkgcG9zaXRpdmUpCiAgImludGVuc2l0eSI6IGZsb2F0LCAgICAgIC8vIFN0cmVuZ3RoIG9mIHNlbnRpbWVudDogMC4wIChuZXV0cmFsL3dlYWspIHRvIDEuMCAodmVyeSBzdHJvbmcpCiAgInVuY2VydGFpbnR5IjogZmxvYXQsICAgIC8vIERlZ3JlZSBvZiB1bmNlcnRhaW50eS9hbWJpZ3VpdHk6IDAuMCAoY2VydGFpbikgdG8gMS4wICh2ZXJ5IHVuY2VydGFpbikKICAiZm9yd2FyZG5lc3MiOiBmbG9hdCAgICAgLy8gRm9yd2FyZC1sb29raW5nIHZzIGJhY2t3YXJkLWxvb2tpbmc6IDAuMCAocGFzdCBldmVudHMpIHRvIDEuMCAoZnV0dXJlIG91dGxvb2spCn0KClJ1bGVzOgotIEV2YWx1YXRlIHJlbGV2YW5jZSBGSVJTVC4gSWYgcmVsZXZhbmNlIDwgMC4xLCBzZXQgYWxsIG90aGVyIGZpZWxkcyB0byBudWxsLgotIHBvbGFyaXR5IGFuZCBpbnRlbnNpdHkgYXJlIGluZGVwZW5kZW50OiBhIHN0cm9uZ2x5IHdvcmRlZCBuZWdhdGl2ZSBhcnRpY2xlIGhhcyBwb2xhcml0eT0tMC45LCBpbnRlbnNpdHk9MC45Ci0gdW5jZXJ0YWludHkgcmVmbGVjdHMgaGVkZ2Ugd29yZHM6ICJtYXkiLCAiY291bGQiLCAidW5jZXJ0YWluIiwgImF0IHJpc2siLCAidW5jbGVhciIKLSBmb3J3YXJkbmVzcyByZWZsZWN0cyBmdXR1cmUgdGVuc2UsIGZvcmVjYXN0cywgZXhwZWN0YXRpb25zLCBwcm9qZWN0aW9ucyB2cyByZXBvcnRlZCBwYXN0IGV2ZW50cwotIFJldHVybiBvbmx5IHRoZSBKU09OIG9iamVjdCwgbm8gZXhwbGFuYXRpb24u)

You are a financial news analyst specializing in energy markets.

Analyze the following news article and return a JSON object with exactly these fields:

{

"relevance": float, // Relevance to energy markets (oil, gas, coal, energy policy): 0.0 (unrelated) to 1.0 (directly relevant)

"polarity": float, // Overall sentiment toward energy markets: -1.0 (very negative) to +1.0 (very positive)

"intensity": float, // Strength of sentiment: 0.0 (neutral/weak) to 1.0 (very strong)

"uncertainty": float, // Degree of uncertainty/ambiguity: 0.0 (certain) to 1.0 (very uncertain)

"forwardness": float // Forward-looking vs backward-looking: 0.0 (past events) to 1.0 (future outlook)

}

Rules:

- Evaluate relevance FIRST. If relevance < 0.1, set all other fields to null.

- polarity and intensity are independent: a strongly worded negative article has polarity=-0.9, intensity=0.9

- uncertainty reflects hedge words: "may", "could", "uncertain", "at risk", "unclear"

- forwardness reflects future tense, forecasts, expectations, projections vs reported past events

- Return only the JSON object, no explanation.

## Appendix B Feature List

Table 5: Full Feature List with Descriptions and Ranges

| Feature Name | Model | Range | Description |
| --- | --- | --- | --- |
| gpt\_article\_count | GPT-4o | (4, 394) | Number of sampled articles in the week |
| gpt\_relevance\_mean | GPT-4o | (0.18, 0.8) | Mean relevance to energy markets, used as aggregation weight |
| gpt\_polarity\_mean | GPT-4o | (-0.35, 0.71) | Relevance-weighted mean sentiment polarity |
| gpt\_intensity\_mean | GPT-4o | (0.42, 0.72) | Relevance-weighted mean sentiment intensity |
| gpt\_uncertainty\_mean | GPT-4o | (0.13, 0.41) | Relevance-weighted mean degree of uncertainty |
| gpt\_forwardness\_mean | GPT-4o | (0.33, 0.83) | Relevance-weighted mean forward-looking orientation |
| gpt\_polarity\_std | GPT-4o | (0.22, 0.65) | Cross-article dispersion of polarity within the week |
| gpt\_uncertainty\_std | GPT-4o | (0.05, 0.26) | Cross-article dispersion of uncertainty within the week |
| gpt\_polarity\_momentum | GPT-4o | (-0.82, 0.73) | Week-on-week change in polarity mean |
| gpt\_uncertainty\_momentum | GPT-4o | (-0.16, 0.17) | Week-on-week change in uncertainty mean |
| gpt\_forwardness\_momentum | GPT-4o | (-0.31, 0.39) | Week-on-week change in forwardness mean |
| llama\_article\_count | Llama 3.2 | (4,394){(}4,394{)} | Number of sampled articles in the week |
| llama\_relevance\_mean | Llama 3.2 | (0, 0.67) | Mean relevance to energy markets |
| llama\_polarity\_mean | Llama 3.2 | (-0.4, 0.7) | Relevance-weighted mean sentiment polarity |
| llama\_intensity\_mean | Llama 3.2 | (0.36, 0.9) | Relevance-weighted mean sentiment intensity |
| llama\_uncertainty\_mean | Llama 3.2 | (0.03, 0.4) | Relevance-weighted mean degree of uncertainty |
| llama\_forwardness\_mean | Llama 3.2 | (0.02, 1) | Relevance-weighted mean forward-looking orientation |
| llama\_polarity\_std | Llama 3.2 | (0, 0.55) | Cross-article dispersion of polarity within the week |
| llama\_uncertainty\_std | Llama 3.2 | (0, 0.29) | Cross-article dispersion of uncertainty within the week |
| llama\_polarity\_momentum | Llama 3.2 | (-0.65, 0.82) | Week-on-week change in polarity mean |
| llama\_uncertainty\_momentum | Llama 3.2 | (-0.27, 0.25) | Week-on-week change in uncertainty mean |
| llama\_forwardness\_momentum | Llama 3.2 | (-0.57, 0.76) | Week-on-week change in forwardness mean |
| finbert\_article\_count | FinBERT | (4, 394) | Number of sampled articles in the week |
| finbert\_polarity\_mean | FinBERT | (-0.44, 0.82) | Equal-weighted mean sentiment polarity |
| finbert\_polarity\_std | FinBERT | (0.12, 0.87) | Cross-article dispersion of polarity within the week |
| finbert\_intensity\_mean | FinBERT | (0.17, 0.88) | Equal-weighted mean sentiment intensity |
| finbert\_polarity\_momentum | FinBERT | (-0.77, 0.86) | Week-on-week change in polarity mean |
| av\_article\_count | AlphaVantage | (4, 394) | Number of articles in the week |
| av\_polarity\_mean | AlphaVantage | (-0.17, 0.41) | Equal-weighted mean AV sentiment score |
| av\_polarity\_std | AlphaVantage | (0.12, 0.47) | Cross-article dispersion of AV sentiment score |
| av\_polarity\_momentum | AlphaVantage | (-37, 0.49) | Week-on-week change in polarity mean |

## References

* J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. (2023)
  Gpt-4 technical report.
  arXiv preprint arXiv:2303.08774.
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Sentiment Extraction ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* P. Agnolucci (2009)
  Volatility in crude oil futures: a comparison of the predictive ability of garch and implied volatility models.
  Energy Economics 31 (2),  pp. 316–321.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"),
  [§2.1](#S2.SS1.p1.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama (2019)
  Optuna: a next-generation hyperparameter optimization framework.
  In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining,
   pp. 2623–2631.
  Cited by: [§3.3](#S3.SS3.p3.4 "3.3 Prediction Model ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Alpha Vantage Inc. (2026)
  Alpha vantage api: financial market data and news sentiment.
  Note: <https://www.alphavantage.co/>Accessed: 2026-01-15
  Cited by: [§3.1](#S3.SS1.p1.1 "3.1 Data Source and Cleaning ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* M. Ames, G. Bagnarosa, T. Matsui, G. W. Peters, and P. V. Shevchenko (2020)
  Which risk factors drive oil futures price curves?.
  Energy Economics 87,  pp. 104676 (en).
  External Links: ISSN 01409883,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S0140988320300153),
  [Document](https://dx.doi.org/10.1016/j.eneco.2020.104676)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* W. Antweiler and M. Z. Frank (2004)
  Is all that talk just noise? the information content of internet stock message boards.
  The Journal of finance 59 (3),  pp. 1259–1294.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* I. J. Arnold and E. B. Vrugt (2008)
  Fundamental uncertainty and stock market volatility.
  Applied Financial Economics 18 (17),  pp. 1425–1440.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* I. J. Arnold and E. B. Vrugt (2010)
  Treasury bond volatility and uncertainty about monetary policy.
  Financial Review 45 (3),  pp. 707–728.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* H. Asgharian, C. Christiansen, and A. J. Hou (2023)
  The effect of uncertainty on stock market volatility and correlation.
  Journal of Banking & Finance 154,  pp. 106929.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* F. Audrino and A. Tetereva (2019)
  Sentiment spillover effects for us and european companies.
  Journal of Banking & Finance 106,  pp. 542–567.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* M. Baker and J. Wurgler (2006)
  Investor sentiment and the cross-section of stock returns.
  The journal of Finance 61 (4),  pp. 1645–1680.
  Cited by: [§3.2](#S3.SS2.p8.1 "3.2 Sentiment Extraction ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* R. B. Barsky and L. Kilian (2002)
  Oil and the macroeconomy since the 1970s.
  Journal of Economic Perspectives 18 (4),  pp. 115–134.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Baruník and B. Malinska (2016)
  Forecasting the term structure of crude oil futures prices with neural networks.
  Applied energy 164,  pp. 366–379.
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Bergstra, R. Bardenet, Y. Bengio, and B. Kégl (2011)
  Algorithms for hyper-parameter optimization.
  Advances in neural information processing systems 24.
  Cited by: [§3.3](#S3.SS3.p3.4 "3.3 Prediction Model ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Birru and T. Young (2022)
  Sentiment and uncertainty.
  Journal of Financial Economics 146 (3),  pp. 1148–1169.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Bollen, H. Mao, and X. Zeng (2011)
  Twitter mood predicts the stock market.
  Journal of Computational Science 2 (1),  pp. 1–8.
  Note: arXiv:1010.3003 [cs]
  External Links: ISSN 18777503,
  [Link](http://arxiv.org/abs/1010.3003),
  [Document](https://dx.doi.org/10.1016/j.jocs.2010.12.007)
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* O. Cepni, D. K. Nguyen, and A. Sensoy (2022)
  News media and attention spillover across energy markets: a powerful predictor of crude oil futures prices.
  The Energy Journal 43 (1\_suppl),  pp. 1–30.
  Cited by: [§2.1](#S2.SS1.p4.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* C. Chen, H. Huang, and H. Chen (2018a)
  NTUSD-fin: a market sentiment dictionary for financial social media data applications.
  In Proceedings of the 1st financial narrative processing workshop (FNP 2018),
   pp. 37–43.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Y. Chen, C. Zhang, K. He, and A. Zheng (2018b)
  Multi-step-ahead crude oil price forecasting using a hybrid grey wave model.
  Physica A: Statistical Mechanics and its Applications 501,  pp. 98–110.
  Cited by: [§2.1](#S2.SS1.p3.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Cunado and F. Perez De Gracia (2005)
  Oil prices, economic activity and inflation: evidence for some Asian countries.
  The Quarterly Review of Economics and Finance 45 (1),  pp. 65–83 (en).
  External Links: ISSN 10629769,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S1062976904000833),
  [Document](https://dx.doi.org/10.1016/j.qref.2004.02.003)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* S. R. Dash, D. Maitra, B. Debata, and J. Mahakud (2021)
  Economic policy uncertainty and stock market liquidity: evidence from g7 countries.
  International Review of Finance 21 (2),  pp. 611–626.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* H. Duan, Y. Liu, and G. Wang (2022)
  A novel dynamic time-delay grey model of energy prices and its application in crude oil price forecasting.
  Energy 251,  pp. 123968.
  Cited by: [§2.1](#S2.SS1.p3.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* E. Eckhaus (2026)
  Data-driven insights: leveraging sentiment analysis and latent profile analysis for financial market forecasting.
  Big Data and Cognitive Computing 10 (1),  pp. 24.
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, et al. (2024)
  The llama 3 herd of models.
  arXiv preprint arXiv:2407.21783.
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Sentiment Extraction ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* L. Grinsztajn, E. Oyallon, and G. Varoquaux (2022)
  Why do tree-based models still outperform deep learning on typical tabular data?.
  Advances in neural information processing systems 35,  pp. 507–520.
  Cited by: [§3.3](#S3.SS3.p1.1 "3.3 Prediction Model ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* A. Groß-Klußmann and N. Hautsch (2011)
  When machines read the news: using automated text analytics to quantify high frequency news-implied market reactions.
  Journal of Empirical Finance 18 (2),  pp. 321–340.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* K. Guan and X. Gong (2023)
  A new hybrid deep learning model for monthly oil prices forecasting.
  Energy Economics 128,  pp. 107136.
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* L. Guo, F. Shi, and J. Tu (2016)
  Textual analysis and machine leaning: crack unstructured data in finance and accounting.
  The Journal of Finance and Data Science 2 (3),  pp. 153–170.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"),
  [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* L. Guo, X. Huang, Y. Li, and H. Li (2023)
  Forecasting crude oil futures price using machine learning methods: evidence from china.
  Energy Economics 127,  pp. 107089.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"),
  [§2.1](#S2.SS1.p2.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. D. Hamilton (1983)
  Oil and the macroeconomy since world war ii.
  Journal of political economy 91 (2),  pp. 228–248.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Z. G. Hiew, X. Huang, H. Mou, D. Li, Q. Wu, and Y. Xu (2019)
  BERT-based financial sentiment index and lstm-based stock return predictability.
  arXiv preprint arXiv:1906.09024.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* A. H. Huang, H. Wang, and Y. Yang (2023)
  FinBERT: a large language model for extracting information from financial text.
  Contemporary Accounting Research 40 (2),  pp. 806–841.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"),
  [§3.2](#S3.SS2.p1.1 "3.2 Sentiment Extraction ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* M. Jeong and K. Ahn (2025)
  Energy organization sentiment and oil return forecast.
  Energy Economics 141,  pp. 108105.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* G. Jiang, C. M. Lee, and Y. Zhang (2005)
  Information uncertainty and expected returns.
  Review of Accounting Studies 10 (2),  pp. 185–221.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* M. Kang (2025)
  Multidimensional investor sentiment and stock market volatility in china: measurement, mechanisms and applications.
  In ITM Web of Conferences,
  Vol. 80,  pp. 04006.
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T. Liu (2017)
  Lightgbm: a highly efficient gradient boosting decision tree.
  Advances in neural information processing systems 30.
  Cited by: [§3.3](#S3.SS3.p1.1 "3.3 Prediction Model ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* C. Kearney and S. Liu (2014)
  Textual sentiment in finance: a survey of methods and models.
  International Review of Financial Analysis 33,  pp. 171–185.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* S. Kim, S. Kim, Y. Kim, J. Park, S. Kim, M. Kim, C. H. Sung, J. Hong, and Y. Lee (2023)
  LLMs analyzing the analysts: do bert and gpt extract more value from financial analyst reports?.
  In Proceedings of the Fourth ACM International Conference on AI in Finance,
   pp. 383–391.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* F. Li (2010)
  The information content of forward-looking statements in corporate filings—a naïve bayesian machine learning approach.
  Journal of accounting research 48 (5),  pp. 1049–1102.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Li, S. Qian, L. Li, Y. Guo, J. Wu, and L. Tang (2024)
  A novel secondary decomposition method for forecasting crude oil price with twitter sentiment.
  Energy 290,  pp. 129954.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* X. Li, W. Shang, and S. Wang (2019)
  Text-based crude oil price forecasting: a deep learning approach.
  International Journal of Forecasting 35 (4),  pp. 1548–1560.
  Cited by: [§2.1](#S2.SS1.p4.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* A. Lopez-Lira and Y. Tang (2023)
  Can chatgpt forecast stock price movements? return predictability and large language models.
  arXiv preprint arXiv:2304.07619.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* T. Loughran and B. McDonald (2016)
  Textual analysis in accounting and finance: a survey.
  Journal of accounting research 54 (4),  pp. 1187–1230.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* S. M. Lundberg and S. Lee (2017)
  A unified approach to interpreting model predictions.
  Advances in neural information processing systems 30.
  Cited by: [§3.4](#S3.SS4.p1.1 "3.4 SHAP-Based Interpretation of Feature Importance ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* F. Ma, C. Liang, Q. Zeng, and H. Li (2020)
  Jumps and oil futures volatility forecasting: a new insight.
  Quantitative Finance.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* A. Manela and A. Moreira (2017)
  News implied volatility and disaster concerns.
  Journal of Financial Economics 123 (1),  pp. 137–162.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Z. McGurk, A. Nowak, and J. C. Hall (2020)
  Stock returns and investor sentiment: textual analysis and social media.
  Journal of Economics and Finance 44 (3),  pp. 458–485.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* W. Medhat, A. Hassan, and H. Korashy (2014)
  Sentiment analysis algorithms and applications: a survey.
  Ain Shams engineering journal 5 (4),  pp. 1093–1113.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* R. C. Merton (1973)
  An intertemporal capital asset pricing model.
  Econometrica: Journal of the Econometric Society,  pp. 867–887.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* J. Nasir, M. Aamir, Z. U. Haq, S. Khan, M. Y. Amin, and M. Naeem (2023)
  A new approach for forecasting crude oil prices based on stochastic and deterministic influences of lmd using arima and lstm models.
  IEEe Access 11,  pp. 14322–14339.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* T. Renault (2017)
  Intraday online investor sentiment and return patterns in the us stock market.
  Journal of Banking & Finance 84,  pp. 25–40.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* L. Rigotti and C. Shannon (2005)
  Uncertainty and risk in financial markets.
  Econometrica 73 (1),  pp. 203–243.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Z. A. Sadik, P. M. Date, and G. Mitra (2020)
  Forecasting crude oil futures prices using global macroeconomic news sentiment.
  IMA Journal of Management Mathematics 31 (2),  pp. 191–215.
  Cited by: [§2.1](#S2.SS1.p4.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* S. Saravanaraj, V. Govindan, S. Broumi, et al. (2025)
  Sentimental analysis to predict stock market using in neutrosophic time series..
  International Journal of Neutrosophic Science (IJNS) 25 (2).
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* G. Segal, I. Shaliastovich, and A. Yaron (2015)
  Good and bad uncertainty: macroeconomic and financial market implications.
  Journal of Financial Economics 117 (2),  pp. 369–397.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* S. Seok, H. Cho, and D. Ryu (2024)
  Dual effects of investor sentiment and uncertainty in financial markets.
  The Quarterly Review of Economics and Finance 95,  pp. 300–315.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* R. Shwartz-Ziv and A. Armon (2022)
  Tabular data: deep learning is not all you need.
  Information fusion 81,  pp. 84–90.
  Cited by: [§3.3](#S3.SS3.p1.1 "3.3 Prediction Model ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* A. Siganos, E. Vagenas-Nanos, and P. Verwijmeren (2017)
  Divergence of sentiment and stock market trading.
  Journal of Banking & Finance 78,  pp. 130–141.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Y. Song, M. He, Y. Wang, and Y. Zhang (2023)
  Forecasting crude oil prices: a reduced-rank approach.
  International Review of Economics & Finance 88,  pp. 698–711.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* T. O. Sprenger, A. Tumasjan, P. G. Sandner, and I. M. Welpe (2014)
  Tweets and trades: the information content of stock microblogs.
  European Financial Management 20 (5),  pp. 926–957.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* C. Sun, X. Qiu, Y. Xu, and X. Huang (2019)
  How to fine-tune bert for text classification?.
  In China national conference on Chinese computational linguistics,
   pp. 194–206.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* L. Sun, M. Najand, and J. Shen (2016)
  Stock return predictability and investor sentiment: a high-frequency perspective.
  Journal of banking & finance 73,  pp. 147–164.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* P. C. Tetlock, M. Saar-Tsechansky, and S. Macskassy (2008)
  More than words: quantifying language to measure firms’ fundamentals.
  The journal of finance 63 (3),  pp. 1437–1467.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* P. C. Tetlock (2007)
  Giving Content to Investor Sentiment: The Role of Media in the Stock Market.
  The Journal of Finance 62 (3),  pp. 1139–1168 (en).
  External Links: ISSN 0022-1082, 1540-6261,
  [Link](https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2007.01232.x),
  [Document](https://dx.doi.org/10.1111/j.1540-6261.2007.01232.x)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"),
  [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* A. Todd, J. Bowden, and Y. Moshfeghi (2024)
  Text-based sentiment analysis in finance: synthesising the existing literature and exploring future directions.
  Intelligent Systems in Accounting, Finance and Management 31 (1),  pp. e1549.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al. (2023)
  Llama: open and efficient foundation language models.
  arXiv preprint arXiv:2302.13971.
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* B. Twedt and L. Rees (2012)
  Reading between the lines: an empirical examination of qualitative attributes of financial analysts’ reports.
  Journal of Accounting and Public Policy 31 (1),  pp. 1–21.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Sentiment Analysis in Finance ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* M. W. Uhl, M. Pedersen, and O. Malitius (2015)
  What’s in the news? using news sentiment momentum for tactical asset allocation.
  Journal of Portfolio Management 41 (2),  pp. 100.
  Cited by: [§3.2](#S3.SS2.p8.1 "3.2 Sentiment Extraction ‣ 3 Methodology ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* W. Wang, Y. Luo, M. Ma, J. Wang, and C. Sui (2025a)
  A novel forecasting framework leveraging large language model and machine learning for methanol price.
  Energy 320,  pp. 135123.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Z. Wang, J. Guo, G. Wang, and X. Shen (2025b)
  Deep learning-based multi-dimensional investor sentiment and stock liquidity: evidence from china.
  Quantitative Finance and Economics 9 (4),  pp. 745.
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* B. Wu, L. Wang, S. Lv, and Y. Zeng (2021)
  Effective crude oil price forecasting using new text-based and big-data-driven model.
  Measurement 168,  pp. 108468.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Y. Xiang and X. H. Zhuang (2013)
  Application of arima model in short-term prediction of international crude oil price.
  Advanced materials research 798,  pp. 979–982.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"),
  [§2.1](#S2.SS1.p1.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* S. B. Yahia, J. A. G. Sanchez, and R. H. Kaffel (2024)
  Impact of sentiment analysis on energy sector stock prices: a finbert approach.
  Working paper.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* D. Zhai, T. Zhang, G. Liang, and B. Liu (2025)
  Research on crude oil futures price prediction methods: a perspective based on quantum deep learning.
  Energy 320,  pp. 135080.
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* X. F. Zhang (2006)
  Information uncertainty and analyst forecast behavior.
  Contemporary accounting research 23 (2),  pp. 565–590.
  Cited by: [§2.3](#S2.SS3.p2.1 "2.3 Multi-Dimensional Sentiment and Uncertainty ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Y. Zhang and Y. Wang (2022)
  Forecasting crude oil futures market returns: A principal component analysis combination approach.
  International Journal of Forecasting 39.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2022.01.010)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").
* Y. Zhao, J. Li, and L. Yu (2017)
  A deep learning ensemble approach for crude oil price forecasting.
  Energy Economics 66,  pp. 9–16.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"),
  [§2.1](#S2.SS1.p2.1 "2.1 Crude Oil Futures Forecasting ‣ 2 Related Literature ‣ Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction").

BETA