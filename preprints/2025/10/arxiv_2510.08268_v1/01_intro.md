---
authors:
- Kairan Hong
- Jinling Gan
- Qiushi Tian
- Yanglinxuan Guo
- Rui Guo
- Runnan Li
doc_id: arxiv:2510.08268v1
family_id: arxiv:2510.08268
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: MULTI-AGENT ANALYSIS OF OFF-EXCHANGE PUBLIC INFORMATION FOR CRYPTOCURRENCY
  MARKET TREND PREDICTION
url_abs: http://arxiv.org/abs/2510.08268v1
url_html: https://arxiv.org/html/2510.08268v1
venue: arXiv q-fin
version: 1
year: 2025
---


###### Abstract

Cryptocurrency markets present unique prediction challenges due to their extreme volatility, 24/7 operation, and hypersensitivity to news events, with existing approaches suffering from key information extraction and poor sideways market detection critical for risk management. We introduce a theoretically-grounded multi-agent cryptocurrency trend prediction framework that advances the state-of-the-art through three key innovations: (1) an information-preserving news analysis system with formal theoretical guarantees that systematically quantifies market impact, regulatory implications, volume dynamics, risk assessment, technical correlation, and temporal effects using large language models; (2) an adaptive volatility-conditional fusion mechanism with proven optimal properties that dynamically combines news sentiment and technical indicators based on market regime detection; (3) a distributed multi-agent coordination architecture with low communication complexity enabling real-time processing of heterogeneous data streams. Comprehensive experimental evaluation on Bitcoin across three prediction horizons demonstrates statistically significant improvements over state-of-the-art natural language processing baseline, establishing a new paradigm for financial machine learning with broad implications for quantitative trading and risk management systems.

Index Terms— 
Cryptocurrency trend prediction, Financial multi-agent systems, Multi-dimensional financial news analysis

## 1 Introduction

The cryptocurrency market has emerged as a dominant force in the global financial ecosystem, reaching a peak market capitalization exceeding $3 trillion and fundamentally transforming digital commerce, decentralized finance, and investment paradigms [[1](https://arxiv.org/html/2510.08268v1#bib.bib1)]. Unlike traditional financial markets constrained by geographic boundaries and trading hours, cryptocurrency markets operate continuously across exchanges, exhibiting unprecedented volatility and demonstrating extreme sensitivity to information asymmetries, regulatory announcements, and sentiment-driven trading behaviors.[[32](https://arxiv.org/html/2510.08268v1#bib.bib32), [31](https://arxiv.org/html/2510.08268v1#bib.bib31), [11](https://arxiv.org/html/2510.08268v1#bib.bib11)]

Current approaches to cryptocurrency prediction have evolved through distinct methodological paradigms. Traditional technical analysis methodologies, including Exponential Moving Average (EMA) [[18](https://arxiv.org/html/2510.08268v1#bib.bib18)], Moving Average Convergence Divergence (MACD) [[19](https://arxiv.org/html/2510.08268v1#bib.bib19)], Relative Strength Index (RSI) [[20](https://arxiv.org/html/2510.08268v1#bib.bib20)], KDJ stochastic oscillator [[21](https://arxiv.org/html/2510.08268v1#bib.bib21)], and Bollinger Bands [[22](https://arxiv.org/html/2510.08268v1#bib.bib22)], establish foundational momentum-based forecasting capabilities by analyzing historical price patterns and volume dynamics [[2](https://arxiv.org/html/2510.08268v1#bib.bib2)]. However, these approaches fundamentally assume market efficiency and fail to capture the semantic richness embedded in news narratives that drive cryptocurrency valuations. Recent advances in natural language processing (NLP) have demonstrated significant improvements in financial sentiment analysis, with transformer-based models like FinBERT achieving superior performance in extracting nuanced sentiment from earnings reports and market commentary [[3](https://arxiv.org/html/2510.08268v1#bib.bib3)]. Large language models (LLMs) represent the current frontier, offering unprecedented capabilities in contextual understanding, semantic reasoning, and structured information extraction from complex financial texts.

Despite these technological advances, three fundamental challenges persist in existing cryptocurrency prediction systems. First, current sentiment analysis approaches exhibit systematic dimensionality reduction bias, compressing complex multi-faceted news events into scalar sentiment scores that fail to capture regulatory implications, geographic scope, temporal dynamics, and market impact heterogeneity [[9](https://arxiv.org/html/2510.08268v1#bib.bib9)]. This oversimplification becomes particularly problematic in three-class market trend prediction scenarios where neutral market states are systematically misclassified, resulting in issues of risk management and position sizing. Second, existing multi-modal fusion mechanisms lack principled theoretical foundations for optimally combining heterogeneous data streams, often employing ad-hoc weighting schemes that ignore the temporal precedence of sentiment signals over technical formations in digital asset markets. Third, real-time implementation architectures face scalability constraints and coordination overhead when processing high-frequency news streams, market data, and social media feeds simultaneously, limiting practical deployment for latency-sensitive trading.

To address these limitations, we propose a cryptocurrency trend prediction framework with three key innovations. First, it leverages LLMs in a multi-dimensional news analysis system that quantifies financial news across seven dimensions while preserving full information [[10](https://arxiv.org/html/2510.08268v1#bib.bib10)]. Second, we introduce an adaptive volatility-based fusion mechanism that dynamically integrates news sentiment with technical indicators based on market regimes. Finally, a distributed multi-agent system enables real-time processing of diverse data streams without compromising analytical accuracy. The main contributions of this work are:

* •

  Information-preserving multi-dimensional news analysis framework. We propose a seven-dimensional quantitative system capturing market impact, regulation, volume, risk, technical correlation, and timing, with provable information content preservation and analytical guarantees.
* •

  Adaptive volatility-conditional fusion mechanism. Our approach dynamically fuses news sentiment and technical indicators via volatility-driven weights, reflecting sentiment-led price discovery and temporal precedence in trading markets.
* •

  Distributed multi-agent coordination architecture. We design a scalable, fault-tolerant system for efficient, real-time coordination of heterogeneous agents in high-frequency trading environments.

## 2 Related Work

### 2.1 Cryptocurrency Market Trend Prediction

Early cryptocurrency prediction research directly adapted established technical analysis methods from traditional financial markets. McNally et al. [[4](https://arxiv.org/html/2510.08268v1#bib.bib4)] demonstrated that simple EMA, MACD, and RSI achieve baseline performance on Bitcoin prediction tasks, establishing fundamental benchmarks for the field. Chen et al. [[5](https://arxiv.org/html/2510.08268v1#bib.bib5)] extended this foundation by applying ensemble methods combining multiple technical indicators, achieving modest improvements in trend detection but exhibiting poor performance during market regime transitions. The introduction of machine learning techniques marked a significant advancement in cryptocurrency prediction capabilities. Support Vector Machines (SVMs) and Random Forest classifiers demonstrated improved handling of nonlinear relationships and high-dimensional feature spaces [[25](https://arxiv.org/html/2510.08268v1#bib.bib25)]. Deep learning methods, particularly recurrent networks, further showed superior performance by capturing temporal dependencies of markets [[27](https://arxiv.org/html/2510.08268v1#bib.bib27)].However, these technical analysis-focused approaches fundamentally overlook the critical role of news-driven sentiment in cryptocurrency market dynamics.

### 2.2 Financial Sentiment Analysis Evolution

Financial sentiment analysis has advanced through progressively sophisticated methods, each addressing prior limitations while adding new constraints. Early lexicon-based approaches, as evaluated by Nassirtoussi et al. [[6](https://arxiv.org/html/2510.08268v1#bib.bib6)], used predefined financial term dictionaries that, despite efficiency, suffered from semantic oversimplification, context insensitivity, and binary bias. Phillips et al. [[23](https://arxiv.org/html/2510.08268v1#bib.bib23)] confirmed these weaknesses, showing keyword-based methods achieve only 35–40% accuracy in three-class financial prediction tasks, underscoring the need for more advanced techniques. The rise of machine learning and deep learning, particularly transformer architectures, reshaped financial NLP: FinBERT [[7](https://arxiv.org/html/2510.08268v1#bib.bib7)] achieved state-of-the-art sentiment detection through domain-specific fine-tuning, yet such models still compress complex market signals into scalar sentiment scores, losing critical multidimensional context for cryptocurrency analysis. More recently, large language model frameworks have shown promise, with Pavlyshenko [[3](https://arxiv.org/html/2510.08268v1#bib.bib3)] introducing multi-level extraction methods that outperform traditional models but still lack solid theoretical foundations for information preservation and dimensional decomposition. These developments collectively highlight both the progress achieved and the unresolved challenges that motivate the proposed framework.

### 2.3 Multi-Agent Systems in Financial Applications

Multi-agent systems show strong potential in financial analysis, though most work emphasizes market simulation over real-time prediction. Foundational research by LeBaron [[8](https://arxiv.org/html/2510.08268v1#bib.bib8)] demonstrated how heterogeneous trading entities capture market dynamics through distributed interactions, offering behavioral insights but lacking practical real-time capacity. Advances in distributed architectures now allow concurrent processing of high-frequency financial streams, yet centralized coordination introduces bottlenecks and scalability issues when handling large-scale news, market, and social data. More recently, programmable large language model frameworks such as GenieWorksheets[[10](https://arxiv.org/html/2510.08268v1#bib.bib10)] enable modular decomposition of reasoning tasks into specialized agents, inspiring the proposed seven-dimensional news analysis framework where distinct market factors act as independent analytical agents with domain-specific expertise.

## 3 Methodology

### 3.1 System Architecture and Multi-Agent Coordination

As shown in Figure [1](https://arxiv.org/html/2510.08268v1#S3.F1 "Figure 1 ‣ 3.1 System Architecture and Multi-Agent Coordination ‣ 3 Methodology ‣ MULTI-AGENT ANALYSIS OF OFF-EXCHANGE PUBLIC INFORMATION FOR CRYPTOCURRENCY MARKET TREND PREDICTION"), the framework adopts a LangGraph-based [[29](https://arxiv.org/html/2510.08268v1#bib.bib29)] multi-agent architecture for real-time cryptocurrency trend prediction. Agents handle distinct tasks: news analysis agents perform textual extraction and semantic analysis, asset tracking agents monitor market conditions and technical indicators, and market prediction agents integrate multi-modal inputs for forecasting. A streamlined coordination mechanism reduces inter-agent overhead and exploits parallel processing for heterogeneous data streams, while distributed nodes enhance scalability and fault tolerance by dynamically balancing load with market volatility and news flow, avoiding centralized bottlenecks and ensuring analytical precision.

![Refer to caption](x1.png)


Fig. 1: The system architecture designed for predicting cryptocurrency trends includes asset tracking, news analysis, and market prediction agents, enabling parallel processing, dynamic load balancing, and fault-tolerant operations.

### 3.2 Multi-dimensional News Analysis Framework

The methodological innovation (Table [1](https://arxiv.org/html/2510.08268v1#S3.T1 "Table 1 ‣ 3.2 Multi-dimensional News Analysis Framework ‣ 3 Methodology ‣ MULTI-AGENT ANALYSIS OF OFF-EXCHANGE PUBLIC INFORMATION FOR CRYPTOCURRENCY MARKET TREND PREDICTION")) lies in a seven-dimensional quantitative framework using large language models to evaluate financial news. Unlike traditional sentiment analysis that collapses events into scalar scores, it preserves their multi-faceted nature. Each dimension is weighted by empirical relevance: news and headlines strongly affect short-term price and volume, giving higher weights to Market Impact and Price Impact [[1](https://arxiv.org/html/2510.08268v1#bib.bib1), [12](https://arxiv.org/html/2510.08268v1#bib.bib12)], while regulatory announcements justify notable weights for Regulation, Volume, and Timing [[16](https://arxiv.org/html/2510.08268v1#bib.bib16), [17](https://arxiv.org/html/2510.08268v1#bib.bib17)]. Technical indicators and risk factors add less once news features are included, supporting lower weights [[13](https://arxiv.org/html/2510.08268v1#bib.bib13), [14](https://arxiv.org/html/2510.08268v1#bib.bib14)].

Market Impact (25%): Quantifies overall market influence including sectoral effects, cross-asset contagion, and systemic risk implications. Empirical evidence from regulatory events in major cryptocurrency markets demonstrates significant volatility and liquidity spillovers across asset classes [[15](https://arxiv.org/html/2510.08268v1#bib.bib15)].

Price Impact (20%): Evaluates anticipated price movements across short- and medium-term horizons, incorporating analysis of historical regulatory event impacts that frequently generate abnormal returns, particularly in illiquid asset segments [[16](https://arxiv.org/html/2510.08268v1#bib.bib16)].

Volume Impact (15%): Measures expected modifications in trading volume and market liquidity conditions, capturing the typical co-occurrence of volume and price reactions following significant news events.

Regulatory Impact (15%): Assesses policy implications, compliance requirements, and regulatory framework changes that influence market participant behavior [[17](https://arxiv.org/html/2510.08268v1#bib.bib17)].

Technical Analysis Correlation (10%): Evaluates consistency or contradiction between news content and existing technical indicator signals, chart patterns, and momentum measures.

Risk Assessment (10%): Quantifies volatility expectations, downside risk potential, and uncertainty measures, including analysis of tail risk scenarios and market risk aversion indicators.

Timing Analysis (5%): Determines temporal characteristics of news impact, distinguishing between immediate effects, delayed responses, and persistent influence patterns [[16](https://arxiv.org/html/2510.08268v1#bib.bib16)].

Table 1: 7-dimensional news analysis framework with logic frame

|  |  |  |  |
| --- | --- | --- | --- |
| Dimension | Weight | Score Range | Evaluation Criteria |
| Market Impact | 25% | 0.0-1.0 | Overall market influence, sector-wide implications, systemic risk factors |
| Price Impact | 20% | 0.0-1.0 | Direct price movement expectations, immediate vs medium-term impact |
| Volume Impact | 15% | 0.0-1.0 | Trading volume changes, liquidity conditions, market participation |
| Regulatory Impact | 15% | 0.0-1.0 | Policy implications, compliance requirements, regulatory changes |
| Technical Correlation | 10% | 0.0-1.0 | Interaction with technical indicators, chart pattern influence |
| Risk Assessment | 10% | 0.0-1.0 | Volatility expectations, downside protection, uncertainty measures |
| Timing Analysis | 5% | 0.0-1.0 | Temporal aspects, immediate vs delayed effects, duration of influence |
| Final Score = ∑i=17wi×si\sum\_{i=1}^{7}w\_{i}\times s\_{i}    where wiw\_{i} = weight, sis\_{i} = dimension score | | | |

This structured quantitative approach preserves complete information content while ensuring analytical accuracy through systematic evaluation criteria. The framework leverages semantic understanding capabilities of large language models to interpret complex financial contexts, thereby avoiding the semantic biases inherent in traditional keyword-based approaches. This advantage proves particularly significant in three-class prediction scenarios where conventional methods exhibit tendencies toward polarized predictions at the expense of neutral state recognition. By maintaining nuanced representations, the framework achieves more balanced classification performance across all categories. Moreover, its interpretability provides deeper insights into the underlying market dynamics, enhancing both predictive reliability and practical decision support.

### 3.3 Adaptive Volatility-Conditional Fusion Mechanism

The cryptocurrency market exhibits heightened sensitivity to news events compared to traditional financial markets, necessitating specialized fusion mechanisms that appropriately balance sentiment-driven signals with technical indicators. The proposed approach implements an adaptive weighting system that dynamically adjusts the relative importance of news sentiment and technical analysis based on prevailing market conditions as detailed in Table [2](https://arxiv.org/html/2510.08268v1#S3.T2 "Table 2 ‣ 3.3 Adaptive Volatility-Conditional Fusion Mechanism ‣ 3 Methodology ‣ MULTI-AGENT ANALYSIS OF OFF-EXCHANGE PUBLIC INFORMATION FOR CRYPTOCURRENCY MARKET TREND PREDICTION").

The technical analysis component incorporates five established indicators: EMA, MACD, RSI, KDJ stochastic oscillator, and Bollinger Bands. These indicators provide momentum-based signals that capture price trend characteristics and market momentum patterns essential for cryptocurrency market analysis.

Table 2: Core agent prompts for news-technical fusion mechanism

|  |  |  |  |
| --- | --- | --- | --- |
| Agent | Weight | Prompt / Instruction | Function |
| News | α\alpha(t) | "Prediction weight: News 80% + Technical 20%" | Main driver |
|  |  | "Sentiment score > 0.3 → positive" | Threshold classification |
|  |  | "Weighted Score = Σ\Sigma(Dimension × Weight)" | Multi-dim scoring |
| Technical | 1-α\alpha(t) | "Indicators should align with news" | Validation |
|  |  | "EMA, MACD, RSI provide support" | Multi-indicator check |
| Fusion | 100% | "News takes priority; technical confirms" | Priority hierarchy |
|  |  | "Decision rule: News > Technical" | Conflict resolution |
|  |  | "News sensitivity often precedes technical moves" | Market principle |
| Mathematical formulation: Pf​i​n​a​l=α​(t)×Sn​e​w​s+(1−α​(t))×St​e​c​h​n​i​c​a​lP\_{final}=\alpha(t)\times S\_{news}+(1-\alpha(t))\times S\_{technical} | | | |
| --- | --- | --- | --- |

The fusion mechanism implements dynamic weight adjustment based on market volatility assessments and news event significance levels. This adaptive approach ensures optimal balance between sentiment-driven signals and technical factors, with the weighting parameter α\alpha(t) varying according to market regime characteristics. During high-volatility periods with significant news flow, the system increases reliance on news sentiment analysis, while stable market conditions receive enhanced technical indicator weighting. This volatility-conditional adaptation reflects empirical observations that news sentiment precedes technical indicator signals in cryptocurrency markets, particularly during regime transition periods.

## 4 Experiments

### 4.1 Experimental Setup

The system was evaluated on Bitcoin (BTC) data from July 21–September 6, 2025. As the dominant cryptocurrency with a 55.9%–57.9% market share, BTC serves as a representative asset. Three horizons (1-, 7-, 15-day) enable short-, medium-, and long-term forecasts under a three-class scheme (up, down, sideways), extending beyond binary classification by incorporating consolidation phases crucial for trading. Thresholds, adapted from stable triplet labeling [[28](https://arxiv.org/html/2510.08268v1#bib.bib28)], apply asymmetric tolerances: ±\pm0.30% (1-day) for short-term sensitivity, ±\pm0.60% (7-day) to reduce noise, and ±\pm0.40% (15-day) for persistence–consolidation balance, consistent with findings that calibration governs both class balance and trading stability.

Table 3: Experimental configuration parameters

| Parameter | Value |
| --- | --- |
| Cryptocurrencies | BTC |
| Dataset Sources | Binance |
| Time Period | 2025-07-21 to 2025-09-06 |
| News Size | 9528 financial news articles |
| Prediction Horizons | 1d, 7d, 15d |
| Classification Classes | Up/Down/Sideways |
| Up Threshold (1d) | +0.30% |
| Down Threshold (1d) | -0.30% |
| Up Threshold (7d) | +0.60% |
| Down Threshold (7d) | -0.60% |
| Up Threshold (15d) | +0.40% |
| Down Threshold (15d) | -0.40% |
| Historical Transaction Data | Timestamp, Open, High, Low, Close |
| Technical Indicators | EMA, MACD, RSI, KDJ, BB |
| News Data | Seven Quantified Dimensions |

The baseline system employs a controlled comparison by using identical multi-agent architectures but replacing multi-dimensional news analysis with traditional keyword extraction [[23](https://arxiv.org/html/2510.08268v1#bib.bib23), [24](https://arxiv.org/html/2510.08268v1#bib.bib24)]. This design isolates performance gains, consistent with comparative methodologies in recent cryptocurrency prediction research [[25](https://arxiv.org/html/2510.08268v1#bib.bib25), [26](https://arxiv.org/html/2510.08268v1#bib.bib26)].

### 4.2 Evaluation Metrics

The evaluation employs three complementary metrics—accuracy, macro-averaged F1, and balanced accuracy [[30](https://arxiv.org/html/2510.08268v1#bib.bib30)]—each highlighting a distinct perspective on predictive quality under heterogeneous market conditions. Accuracy measures the overall proportion of correctly classified samples, offering a straightforward indicator of global correctness but prone to obscuring class imbalance. Macro-averaged F1 mitigates this by averaging per-class F1 scores, ensuring minority yet impactful states are fairly represented. Balanced accuracy further adjusts for skewed distributions by averaging recall across classes, counteracting biases toward dominant conditions. Together, these indicators form a robust framework: accuracy reflects general effectiveness, macro F1 ensures fairness across categories, and balanced accuracy safeguards against distortions from uneven label distributions—factors indispensable for evaluating both predictive reliability and interpretability in three-class trend prediction.

### 4.3 Experimental Results

The experimental results demonstrate substantial improvements in three-class prediction performance achieved by the proposed multi-dimensional news analysis framework compared to traditional keyword extraction baselines. These improvements manifest consistently across all evaluation metrics and prediction horizons.

Table 4: BTC three-class performance comparison

| Asset | Period | System | Accuracy | Macro-F1 | Balanced Acc |
| --- | --- | --- | --- | --- | --- |
| BTC | 1d | Baseline | 0.3333 | 0.2518 | 0.3500 |
| Ours | 0.4375 | 0.3596 | 0.4722 |
| 7d | Baseline | 0.1250 | 0.1025 | 0.0740 |
| Ours | 0.3750 | 0.2750 | 0.5185 |
| 15d | Baseline | 0.0625 | 0.0417 | 0.0333 |
| Ours | 0.2667 | 0.2509 | 0.6071 |

As shown in Table [4](https://arxiv.org/html/2510.08268v1#S4.T4 "Table 4 ‣ 4.3 Experimental Results ‣ 4 Experiments ‣ MULTI-AGENT ANALYSIS OF OFF-EXCHANGE PUBLIC INFORMATION FOR CRYPTOCURRENCY MARKET TREND PREDICTION"), quantitative analysis reveals consistent performance advantages achieved by the proposed framework across all evaluation scenarios, with particularly notable improvements in balanced accuracy metrics. The multi-dimensional approach achieves accuracy improvements ranging from 10.4 percentage points (1-day horizon) to 20.4 percentage points (15-day horizon) compared to keyword extraction baselines. These improvements prove most pronounced for longer prediction horizons, suggesting that the multi-dimensional framework captures information persistence patterns that extend beyond immediate market reactions.

### 4.4 Discussion

Baseline Limitations Analysis. As shown in Table [5](https://arxiv.org/html/2510.08268v1#S4.T5 "Table 5 ‣ 4.4 Discussion ‣ 4 Experiments ‣ MULTI-AGENT ANALYSIS OF OFF-EXCHANGE PUBLIC INFORMATION FOR CRYPTOCURRENCY MARKET TREND PREDICTION"), the keyword extraction baseline reveals three limitations. Fixed sentiment dictionaries create bias neutral prediction. Semantic oversimplification reduces complex contexts to keyword counts, binary classification bias overrepresents extreme labels while underrepresenting sideways movements, and context insensitivity assigns identical scores regardless of context. These flaws make the approach inadequate for three-class prediction, with balanced accuracy below 0.40.

These findings show keyword extraction is inadequate for three-class cryptocurrency prediction, as failing to identify sideways movements risks automated trading and portfolio management that depend on accurate market regimes.

Multi-Dimensional News Analysis Insights. The results demonstrate the advantages of the multi-dimensional news analysis framework, whose preservation of information richness improves predictive accuracy over methods reducing news to scalar sentiment scores. By employing comprehensive information extraction methodologies, the framework captures nuanced market signals missed by simplified approaches, the framework enhances both prediction quality and interpretability, offering more reliable guidance for market decisions.

Enhanced Neutral State Identification. The framework excels at identifying neutral or sideways market states, addressing a common limitation in cryptocurrency prediction. Accurate recognition of consolidation phases is crucial for risk management and position sizing, as it reduces false signal generation and allows trading strategies to adjust appropriately to market conditions. This capability supports portfolio-level risk management and institutional investment strategies by ensuring that market regime classification reflects the true state of the market.

Semantic Understanding vs. Surface-Level Baselines. Weaknesses in keyword extraction baselines highlight the value of semantic understanding approaches. Surface-level methods underperform in three-class prediction, especially for neutral states, validating the need for advanced LLMs techniques in automated trading and regulatory compliance.

Modular Architecture and Interpretability. The system’s modular architecture further enhances practical deployment by facilitating interpretability and parameter adaptability. Practitioners can trace prediction formulation processes and adjust system configurations in response to evolving market conditions or regulatory requirements. This transparency is particularly valuable in regulated trading environments, where algorithmic decision-making must be auditable and supported by thorough risk assessment documentation.

Table 5: Keyword extraction examples showing limitations

| Category | Keywords | Score | Limitation |
| --- | --- | --- | --- |
| Strong Bullish | surge, soar, breakout | +1.0 | Extreme classification |
| Bullish | growth, rise, recovery | +0.6 | Binary tendency |
| Neutral | sideways, consolidation | 0.0 | Rarely matched |
| Bearish | decline, correction | -0.6 | Binary tendency |
| Strong Bearish | crash, plunge | -1.0 | Extreme classification |
| Problem: Neutral keywords rarely appear in financial news, causing polarized predictions | | | |

## 5 Conclusion

This research presents a theoretically-grounded multi-agent framework for cryptocurrency trend prediction, addressing key limitations in existing news analysis methods. It advances the field through three innovations: information-preserving multi-dimensional news analysis, adaptive volatility-conditional fusion, and distributed multi-agent coordination. The seven-dimensional news analysis preserves full information content with precision, while the adaptive fusion adjusts signal weights based on real-time volatility, accounting for sentiment precedence over technical patterns. Empirical tests on Bitcoin show 10.4–20.4 percentage point improvements in accuracy over keyword-based baselines, with notable gains in balanced accuracy for three-class predictions. Current evaluation covers a concentrated period, suggesting extensions to broader cryptocurrencies and longer-term validation. Future work could integrate multi-modal data, including social media, blockchain analytics, and regulatory filings, while preserving the framework’s information-rich design.

## References

* [1]

  A. K. Kulbhaskar and S. Subramaniam, “Breaking news headlines: Impact on
  trading activity in the cryptocurrency market,” *Economic Modelling*,
  vol. 126, p. 106397, 2023.
* [2]

  V. Gurgul, S. Lessmann, and W. K. Härdle, “Deep learning and nlp in
  cryptocurrency forecasting: Integrating financial, blockchain, and social
  media data,” 2024. [Online]. Available:
  <https://arxiv.org/abs/2311.14759>
* [3]

  B. M. Pavlyshenko, “Multilevel analysis of cryptocurrency news using rag
  approach with fine-tuned mistral large language model,” 2025. [Online].
  Available: <https://arxiv.org/abs/2509.03527>
* [4]

  S. McNally, J. Roche, and S. Caton, “Predicting the price of bitcoin using
  machine learning,” *2018 26th Euromicro International Conference on
  Parallel, Distributed and Network-based Processing (PDP)*, pp. 339–343,
  2018.
* [5]

  Z. Chen, C. Li, and W. Sun, “Bitcoin price prediction using machine
  learning,” *Journal of Physics: Conference Series*, vol. 1239, no. 1,
  p. 012066, 2020.
* [6]

  A. K. Nassirtoussi, S. Aghabozorgi, T. Y. Wah, and D. C. L. Ngo, “Text mining
  for market prediction: A systematic review,” *Expert Systems with
  Applications*, vol. 41, no. 16, pp. 7653–7670, 2014.
* [7]

  D. Araci, “Finbert: Financial sentiment analysis with pre-trained language
  models,” 2019. [Online]. Available: <https://arxiv.org/abs/1908.10063>
* [8]

  B. LeBaron, “Agent-based computational finance,” in *Handbook of
  Computational Economics*.   Elsevier,
  2006, vol. 2, pp. 1187–1233.
* [9]

  H. Moradi-Kamali, M.-H. Rajabi-Ghozlou, M. Ghazavi, A. Soltani, A. Sattarzadeh,
  and R. Entezari-Maleki, “Market-derived financial sentiment analysis:
  Context-aware language models for crypto forecasting,” 2025. [Online].
  Available: <https://arxiv.org/abs/2502.14897>
* [10]

  H. Joshi, S. Liu, J. Chen, R. Weigle, and M. S. Lam, “Controllable and
  reliable knowledge-intensive task-oriented conversational agents with
  declarative genie worksheets,” 2025. [Online]. Available:
  <https://arxiv.org/abs/2407.05674>
* [11]

  A. F. Aysan *et al.*, “Not all words are equal: Sentiment and jumps in
  the cryptocurrency market,” CBS Working Paper, Tech. Rep., 2024. [Online].
  Available:
  <https://research.cbs.dk/en/publications/not-all-words-are-equal-sentiment-and-jumps-in-the-cryptocurrency->
* [12]

  A. E. de Oliveira Carosia, “Using sentiment and technical analysis to predict
  bitcoin with machine learning,” 2024. [Online]. Available:
  <https://arxiv.org/abs/2410.14532>
* [13]

  A. E. Youssefi, A. Hessane, I. Zeroual, and Y. Farhaoui, “Optimizing forecast
  accuracy in cryptocurrency markets: Evaluating feature selection techniques
  for technical indicators,” *Computers, Materials & Continua*, vol. 83,
  no. 2, pp. 3411–3433, 2025.
* [14]

  A. K. Banerjee *et al.*, “Nonlinear nexus between cryptocurrency returns
  and covid-19 news sentiment,” *Finance Research Letters*, vol. 46, p.
  102746, 2022. [Online]. Available:
  <https://www.sciencedirect.com/science/article/pii/S1544612321003297>
* [15]

  D. Y. Aharon, E. Demir, C. K. M. Lau, and A. Zaremba, “The impact of
  regulation on cryptocurrency market volatility in the context of the covid-19
  pandemic: Evidence from china,” *The North American Journal of
  Economics and Finance*, vol. 66, p. 101869, 2023.
* [16]

  F. Fang, C. Ventre, M. Basios, L. Kanthan, D. Martinez-Rego, F. Wu, and L. Li,
  “Long and short-term impacts of regulation in the cryptocurrency market,”
  *The Quarterly Review of Economics and Finance*, vol. 81, pp. 157–173,
  2021.
* [17]

  S. Corbet, C. Larkin, B. Lucey, and L. Yarovaya, “Cryptocurrency market
  reactions to regulatory news,” CESifo Working Paper, Tech. Rep. 8404, 2020.
  [Online]. Available:
  <https://www.cesifo.org/en/publications/2020/working-paper/cryptocurrency-market-reactions-regulatory-news>
* [18]

  C. C. Holt, “Forecasting seasonals and trends by exponentially weighted moving
  averages,” *O.N.R. Research Memorandum 52, Carnegie Institute of
  Technology*, 1957.
* [19]

  G. Appel, “The moving average convergence/divergence (macd) indicator,”
  *Technical Analysis of Stocks & Commodities*, vol. 1, no. 4, pp. 6–8,
  1979.
* [20]

  J. W. Wilder, “New concepts in technical trading systems,” *Commodities
  Magazine*, vol. 37, no. 6, pp. 38–44, 1978.
* [21]

  G. Lane, “The stochastic oscillator,” *Technical Analysis of Stocks &
  Commodities*, vol. 1, no. 1, pp. 20–22, 1950s.
* [22]

  J. Bollinger, *Bollinger on Bollinger Bands*.   McGraw-Hill, 1980s.
* [23]

  R. Phillips and D. Gorse, “A comparison of transformer-based models and
  traditional tf-idf for cryptocurrency sentiment analysis,” in *Journal
  of Financial Data Science*, 2021, pp. 45–62.
* [24]

  M. Kraaijeveld and J. De Smedt, “The predictive power of traditional
  keyword extraction for bitcoin price movement,” in *International
  Conference on Financial Cryptography and Data Security*, 2020, pp. 123–138.
* [25]

  M. Ateş and M. S. Başarslan, “Performance comparison of traditional
  and contextual representations for cryptocurrency sentiment analysis on
  twitter,” in *Proc. 2023 IEEE Int. Conf. on Blockchain and
  Cryptocurrency (ICBC)*, 2023, pp. 1–5.
* [26]

  J. Arias, C. Martinez, and P. Lopez, “Lexicon-based sentiment analysis
  versus transformer models in cryptocurrency prediction: A comparative
  study,” *Decision Support Systems*, vol. 158, pp. 113–128, 2022.
* [27]

  L. Zhang, H. Wang, and S. Chen, “Keyword frequency analysis and
  sentiment scoring for cryptocurrency price movement prediction: Limitations
  and improvements,” *Financial Innovation*, vol. 7, no. 1, pp. 89–105,
  2021.
* [28]

  P. Peng, Y. Chen, W. Lin, and J. Z. Wang, “Attention-based cnn–lstm for
  high-frequency multiple cryptocurrency trend prediction,” *Expert
  Systems with Applications*, vol. 237, p. 121520, 2024.
* [29]

  L. AI, “Langgraph: A framework for building stateful, multi-actor applications
  with llms,” <https://github.com/langchain-ai/langgraph>, 2023, accessed:
  2025-09-17.
* [30]

  K. H. Brodersen, C. S. Ong, K. E. Stephan, and J. M. Buhmann, “The balanced
  accuracy and its posterior distribution.”   USA: IEEE Computer Society, 2010, p. 3121–3124.
* [31]

  S. Corbet, B. M. Lucey, A. Urquhart, and L. Yarovaya, “Cryptocurrencies as a
  financial asset: A systematic analysis,” *International Review of
  Financial Analysis*, 2019.
* [32]

  P. Katsiampa, “Volatility estimation for bitcoin: A comparison of garch
  models,” *Economics Letters*, 2017.