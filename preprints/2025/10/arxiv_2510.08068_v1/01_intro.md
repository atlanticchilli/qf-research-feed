---
authors:
- Aadi Singhi
doc_id: arxiv:2510.08068v1
family_id: arxiv:2510.08068
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: An Adaptive Multi-Agent Bitcoin Trading System
url_abs: http://arxiv.org/abs/2510.08068v1
url_html: https://arxiv.org/html/2510.08068v1
venue: arXiv q-fin
version: 1
year: 2025
---


Aadi Singhi
  
UCL Computer Science

###### Abstract

111The original thesis was submitted on 16 May 2025. This paper presents a condensed version of the full 80-page dissertation.

This paper presents a Multi Agent Bitcoin Trading system that utilizes Large Language Models (LLMs) for alpha generation and portfolio management in the cryptocurrencies market. Unlike equities, cryptocurrencies exhibit extreme volatility and are heavily influenced by rapidly shifting market sentiments and regulatory announcements, making them difficult to model using static regression models or neural networks trained solely on historical data [[53](https://arxiv.org/html/2510.08068v1#bib.bib53)].
The proposed framework overcomes this by structuring LLMs into specialised agents for technical analysis, sentiment evaluation, decision-making, and performance reflection. The system improves over time through a novel verbal feedback mechanism where a Reflect agent provides daily and weekly natural-language critiques of trading decisions. These textual evaluations are then injected into future prompts, allowing the system to adjust indicator priorities, sentiment weights, and allocation logic without parameter updates or finetuning. Back-testing on Bitcoin price data from July 2024 to April 2025 shows consistent outperformance across market regimes: the Quantitative agent delivered over 30% higher returns in bullish phases and 15% overall gains versus buy-and-hold, while the sentiment-driven agent turned sideways markets from a small loss into a gain of over 100%. Adding weekly feedback further improved total performance by 31% and reduced bearish losses by 10%. The results demonstrate that verbal feedback represents a new, scalable, and low-cost method of tuning LLMs for financial goals.

## 1 Introduction

This paper introduces an Agentic AI system for managing a Bitcoin-only portfolio powered by an LLM : DeepSeek-r1 [[31](https://arxiv.org/html/2510.08068v1#bib.bib31)]. Conventional machine learning methods, such as regression models and neural networks, perform well in equity markets where recurring historical patterns are linked to fundamentals such as earnings, cash flows, and balance sheet strength. In contrast, Bitcoin’s price is largely driven by non-fundamental forces such as regulatory announcements, influencer statements, and speculative behavior by investors driven by fear and greed. For example, in early January 2021 Bitcoin rose from about $29,000 to over $40,000 in less than a week following positive commentary and Tesla’s $1.5 billion purchase, while in May 2021 it fell nearly 30% within a week after Tesla suspended Bitcoin payments and Chinese regulators reiterated restrictions.

In such conditions, being frequently correct does not necessarily translate into making money. While predictive accuracy is intuitively linked to profitability, the correlation between the two is weak in the case of Bitcoin, which is characterized by asymmetric returns, fat tails, and high noise-to-signal ratios. Theoretically, if a model consistently predicts the correct direction of returns, profitability should follow. However, Accuracy treats all predictions equally, whereas profitability depends on the magnitude and timing of those predictions. A model that is ”often right” can still underperform if it misses major rallies or fails to exit before sharp drawdowns, while another with lower accuracy can outperform by simply capturing large moves. In such conditions, profit depends more on capital allocation, position sizing, and risk management than on raw directional correctness. Moreover, even highly accurate models may fail if execution costs, slippage, or regime shifts negate expected returns, as liquidity and volatility conditions in Bitcoin change rapidly.

What is needed is a mechanism that can reason over unstructured, real-time signals rather than only fit historical patterns. LLMs offer a potential solution to this unpredictability, as they are particularly suited for large-scale textual analysis and pattern recognition. By continuously updating their understanding as new data emerges, they are better able to capture sudden shifts in cryptocurrency prices than models trained solely on historical data.

This promise, however, hinges on how we enable models to evolve without full retraining. Since LLMs do not inherently update their internal knowledge, the key question is how we can refresh or refine their understanding as markets change. Existing research explores methods such as Retrieval-Augmented Generation (RAG) [[38](https://arxiv.org/html/2510.08068v1#bib.bib38)], Supervised Fine-Tuning (SFT) [[39](https://arxiv.org/html/2510.08068v1#bib.bib39)], Reinforcement Learning (RL) [[42](https://arxiv.org/html/2510.08068v1#bib.bib42)], and Multi-Head Reinforcement Learning (MHRL) [[41](https://arxiv.org/html/2510.08068v1#bib.bib41)].
, but these approaches often suffer from information loss when complex human feedback is compressed into a single scalar reward signal. Several studies, including InstructGPT [[42](https://arxiv.org/html/2510.08068v1#bib.bib42)] and Constitutional AI [[43](https://arxiv.org/html/2510.08068v1#bib.bib43)], note that converting rich human feedback into a single scalar reward often omits contextual nuance and can cause models to optimize for the reward itself rather than the true intent of the feedback.
To address this limitation, recent studies propose using verbal feedback: natural-language critiques provided directly to the model during inference, allowing it to retain the full semantic richness of the feedback. For instance, the Reflexion framework enables models to store and reuse their own self-critiques without any parameter updates, leading to more consistent reasoning and improved task success rates across multiple benchmarks [[44](https://arxiv.org/html/2510.08068v1#bib.bib44)]. Similarly, Self-Refine introduces an iterative “generate → critique → revise” process, where the model learns from its own feedback to progressively enhance output quality [[45](https://arxiv.org/html/2510.08068v1#bib.bib45)].
Both studies report substantial performance gains over standard LLM baselines without additional training or fine-tuning. This is especially relevant for crypto trading, where context and justification matter as much as raw predictions.

To build on these capabilities, the framework structures LLMs into specialised agents for technical analysis, sentiment assessment, portfolio decision-making, and strategy evaluation. Adaptability is introduced through a novel dual verbal feedback mechanism in which the Reflect agent produces natural-language evaluations of each agent’s performance at daily and weekly intervals. The trading decisions are evaluated against benchmarks such as a static baseline buy-and-hold portfolio, risk-adjusted measures such as the Sharpe ratio, and profitability indicators such as cumulative returns, regret, and accuracy. These evaluations are then injected into the next day’s or week’s prompts. Rather than adjusting model parameters or retraining, the agents incorporate this feedback as additional context in their reasoning, allowing them to refine indicator prioritisation, sentiment weighting, and allocation choices in subsequent decisions. The system is evaluated not on classification accuracy alone but on its ability to deliver consistent profitability over time, aligning its objectives more closely with real-world investment outcomes.

## 2 Background Research

The background review is organized into two subsections: an in-depth analysis of Bitcoin, followed by a brief summary of the current research on LLMs in finance.

### 2.1 Bitcoin

Bitcoin is a decentralized digital currency introduced in 2009 by the pseudonymous Satoshi Nakamoto [[46](https://arxiv.org/html/2510.08068v1#bib.bib46)]. While Bitcoin is often described as a currency, it is more fundamentally an application of distributed ledger technology (DLT), where transactions are recorded across a decentralized network rather than by a central authority. Within this family of technologies, blockchain represents a specific implementation: a sequential, cryptographically linked chain of blocks that ensures immutability and transparency. Bitcoin was the first large-scale use case of blockchain. Beyond peer-to-peer payments, Bitcoin’s most profound contribution lies in demonstrating that trust can be engineered through code rather than institutions. By solving the double-spending problem via a decentralized consensus mechanism, it eliminated the need for intermediaries in value transfer [[54](https://arxiv.org/html/2510.08068v1#bib.bib54)]. Its open, immutable, and censorship-resistant ledger redefined the notion of digital property rights, allowing individuals to hold and exchange scarce digital assets without reliance on central authorities. Moreover, its rule-based monetary policy and energy-anchored security introduced a new paradigm of programmable, verifiable money that inspired subsequent innovations in blockchain-based finance, from DeFi to asset tokenization.

![Refer to caption](bitcoin_price.png)


Figure 1: Bitcoin price chart

#### 2.1.1 Price

Bitcoin has grown into the world’s most valuable cryptocurrency (Figure [1](https://arxiv.org/html/2510.08068v1#S2.F1 "Figure 1 ‣ 2.1 Bitcoin ‣ 2 Background Research ‣ An Adaptive Multi-Agent Bitcoin Trading System")), breaching $115,000 in 2025 and attaining a market capitalization of roughly $2.3 trillion with daily trading volumes exceeding $61 billion. Its value is sustained by a fixed supply of 21 million coins, a feature often compared to gold, and it has become widely adopted both by retail participants and large institutions. Recent milestones including the approval of spot Bitcoin ETFs and its use as a corporate treasury asset have cemented its role as the benchmark of the digital asset market [[47](https://arxiv.org/html/2510.08068v1#bib.bib47)].
Over the last decade, Bitcoin has outperformed traditional assets by an extraordinary margin, growing roughly 26,900% versus ∼\sim193% for the S&P 500 and ∼\sim126% for gold, with a 10-year CAGR for Bitcoin of 124% compared to 10–13% for equities and gold.

Table 1: CAGR Comparison of Major Assets

| Asset | 10-Year Return (%) | 5-Year Return (%) | Sharpe Ratio |
| --- | --- | --- | --- |
| Gold | 10 | 7 | 0.90 |
| S&P 500 | 13 | 11 | 0.65 |
| Bitcoin | 124 | 155 | 0.96 |

![Refer to caption](volatility_graph.png)


Figure 2: Historical Rolling Annualized Volatility (Standard Deviation) Comparison 2015-2025 for Gold, S&P 500, and Bitcoin

This stark contrast in volatility illustrates that Bitcoin’s price movements are far more unpredictable and prone to sharp swings, making it a substantially higher risk asset relative to the traditional safe haven status of Gold and the diversified equity exposure of the S&P 500. From an investor’s standpoint, Bitcoin rewards those with a high risk tolerance and a long horizon, while Gold is best suited for capital preservation and cushioning drawdowns. The S&P 500 remains the core growth anchor for most portfolios. When combined, these three assets can complement one another Bitcoin driving upside potential, Gold adding stability, and the S&P 500 delivering steady growth resulting in a diversified mix that manages risk while seeking attractive returns. Ultimately, the right balance depends on an investor’s risk appetite and time horizon.

#### 2.1.2 Dominancy

![Refer to caption](btc_dominance_eth.png)


Figure 3: Bitcoin dominance as a share of total cryptocurrency market capitalization.

Bitcoin has remained the dominant force in the cryptocurrency ecosystem since its inception in 2009, consistently accounting for 40–50% of total market capitalization over the past decade (Figure [3](https://arxiv.org/html/2510.08068v1#S2.F3 "Figure 3 ‣ 2.1.2 Dominancy ‣ 2.1 Bitcoin ‣ 2 Background Research ‣ An Adaptive Multi-Agent Bitcoin Trading System")). Unlike the majority of altcoins, many of which have low survivability, speculative use cases, or heavy dependence on external platforms, Bitcoin has endured multiple market cycles without protocol failure. Moreover, empirical evidence, as seen in (Figure [4](https://arxiv.org/html/2510.08068v1#S2.F4 "Figure 4 ‣ 2.1.2 Dominancy ‣ 2.1 Bitcoin ‣ 2 Background Research ‣ An Adaptive Multi-Agent Bitcoin Trading System")), shows that Bitcoin is highly correlated with other cryptocurrencies (0.5–0.8), meaning altcoins tend to follow its price movements, particularly during downturns. The Overall market mostly moves in tandem with Bitcoin with a correlation of 0.63. This systemic co-movement undermines the rationale for intra-crypto diversification, since portfolios spread across tokens still remain overwhelmingly exposed to Bitcoin’s market trajectory. For these reasons, this paper exclusively focuses on Bitcoin, not only because of its dominance but also because it represents the most rational and risk-conscious foundation for building a profitable trading system.

![Refer to caption](correlations_crypto.png)


Figure 4: Average Correlations of different cryptocurrencies with Bitcoin over 5 years

#### 2.1.3 Price Factors

Bitcoin’s price is influenced by a combination of sentiment, technical, and on-chain factors that together capture both market psychology and structural dynamics [[55](https://arxiv.org/html/2510.08068v1#bib.bib55)].
Sentiment plays a decisive role in short-term movements, as shifts in public mood driven by regulation, macroeconomic events, or social media discussions often lead to rapid rallies or declines. Technical indicators derived from price and volume, such as moving averages, momentum oscillators, and volatility bands, provide a systematic way to identify trends, turning points, and risk conditions within this volatility. Alongside these, on-chain data offers a unique perspective by measuring the actual use of the network, with metrics such as transaction volumes and active addresses serving as signals of adoption and liquidity. Each of these dimensions is important: sentiment explains sudden market swings, technical analysis offers structured decision rules, and on-chain metrics capture the underlying health of the system. Together, they form a comprehensive framework for understanding and anticipating Bitcoin’s price behaviour.

### 2.2 Large Language Models in Finance

Large Language Models (LLMs) represent a major advance in natural language processing, built primarily on the Transformer architecture introduced by Vaswani et al. (2017) [[48](https://arxiv.org/html/2510.08068v1#bib.bib48)]. Their defining capability lies in modelling context through self-attention, which allows them to generate coherent text and perform diverse language tasks without task-specific training. As Lee et al. (2024) note in their survey of financial LLMs, this generalization capacity makes LLMs particularly powerful when dealing with unstructured, text-heavy domains [[49](https://arxiv.org/html/2510.08068v1#bib.bib49)]. Domain-specific adaptations highlight this potential: BloombergGPT (Wu et al., 2023) trained a 50-billion-parameter model on a large financial corpus, demonstrating significant gains in sentiment analysis, question answering, and named entity recognition compared to general LLMs [[50](https://arxiv.org/html/2510.08068v1#bib.bib50)]. Similarly, PIXIU (Chen et al., 2023) introduced FinMA, an instruction-tuned variant of LLaMA, together with a benchmark covering forecasting, sentiment, and reasoning tasks, providing evidence that finance-specific instruction tuning improves accuracy and robustness [[51](https://arxiv.org/html/2510.08068v1#bib.bib51)]. Collectively, these efforts show how LLMs can move beyond generic language modeling to capture the nuances of financial text, laying the foundation for their integration into trading and portfolio management systems.

The use of LLMs in finance is not without risk. Three persistent limitations constrain their deployment in trading contexts. First, they are prone to hallucination: generating plausible but false information. In one benchmark, a finance-focused LLM produced fabricated content in 41% of probing test cases, raising concerns about reliability [[49](https://arxiv.org/html/2510.08068v1#bib.bib49)]. Second, their knowledge is temporally bounded by training cutoffs, making them poorly suited to tasks requiring real-time awareness unless supplemented by retrieval or live feeds. Third, they lack interpretability. With billions of parameters, it is often unclear why a particular recommendation is produced, creating difficulties for accountability in financial decision-making. Together, these weaknesses necessitate the design of auxiliary mechanisms to ensure robustness, adaptability, and transparency.

Luo et al. (2025) propose a fine-tuned multi-agent system for automated crypto portfolio management, where agents trained on distinct modalities like technical signals, news, market factors, and risk metrics collaborate to build diversified portfolios [[52](https://arxiv.org/html/2510.08068v1#bib.bib52)]. Their architecture, which integrates expert fine-tuning with inter-agent communication, consistently outperforms both unfine-tuned GPT-4o baselines and traditional benchmarks, achieving superior Sharpe ratios and robustness. The authors argue that decomposing investment tasks into specialized, fine-tuned experts provides scalability and explainability, though at the cost of flexibility in rapidly changing conditions.

## 3 System Design and Methodology

The proposed system is designed not only to evaluate profitability in a portfolio across different market regimes but also to identify the contribution of individual market factors such as technical indicators and sentiment signals in generating profitable trades.

### 3.1 Quantitative Agent (Quants)

The Quants Agent is designed to analyze Bitcoin market data using quantitative methods, providing an objective assessment of market conditions. Its primary role is to process historical and real-time data, which includes price trends, technical indicators, and on-chain metrics, to classify the subsequent day’s market state as bullish, bearish, or neutral. Additionally, it generates a trading strategy (BTC/cash portfolio allocation) based on its own analysis. This strategy is derived purely from technical insights, which can help evaluate whether relying purely on technical indicators can lead to successful trade generations. This recommendation is provided to the reflection agents for evaluation, while the market classification and reasoning are forwarded to the decision agent.

It relies on structured, market-derived data to ground its predictions. This includes OHLCV data (open, high, low, close, and volume) drawn from exchange feeds, as well as a range of technical indicators computed from this data, such as moving averages, MACD, RSI, Bollinger Bands, VWAP, and ADX. To complement these price-based measures, the agent also integrates on-chain metrics sourced directly from the Bitcoin blockchain, including transaction counts, active addresses, and transfer volumes. These inputs ensure that the Quants Agent captures both price mechanics and underlying network activity, enabling it to generate daily market state predictions and suggested portfolio allocations. By combining exchange-based and blockchain-native data, the agent is positioned to balance short-term technical signals with deeper structural insights into adoption and liquidity.

The agent outputs both a probabilistic classification of the next day’s market direction and a suggested BTC/cash split, which are separately routed to the Decision Agent and Reflect Agent.

### 3.2 Sentiment Agent (Signals)

The Signals Agent is responsible for assessing investor sentiment related to Bitcoin. It draws on three primary data sources that capture market psychology and external influences on Bitcoin. First, news data from trusted financial outlets (e.g., CNBC, Yahoo Finance, Forbes, Business Insider, Seeking Alpha, and Fortune) is aggregated via the GNews API, ensuring coverage of regulatory announcements, macroeconomic shifts, and key narratives shaping sentiment. Second, the Fear and Greed Index, obtained from Alternative.me, provides a composite daily score ranging from extreme fear to extreme greed, reflecting crowd mood based on volatility, trading volume, social media, and surveys. Finally, social media sentiment scores are collected through the Senticrypt API, which processes Twitter discussions to quantify retail investor mood in real time. Together, these inputs allow the agent to evaluate both structured and unstructured sentiment signals, ensuring that its predictions incorporate news-driven shocks, aggregated market psychology, and the daily pulse of social platforms. The classification and reasoning are passed to the Decision Agent, while the portfolio is forwarded to the Reflect Agent for evaluation.

### 3.3 Decision Agent

The Decision Agent acts as the central reasoning component that consolidates the outputs of the Quants and Signals agents. It operates by receiving only the predictions and reasoning from both agents without directly inheriting their portfolio recommendations to avoid bias in its own reasoning. It is provided daily with its current portfolio value for context. The output includes a final prediction quantifying market sentiment as bullish, bearish, or neutral, alongside detailed reasoning that justifies its allocation choice. It produces a final trading decision that directly competes against a static baseline (50% BTC–50% cash). The prompt includes a clear instruction to treat daily market inputs as the primary basis for decision-making, with short-term and long-term feedback used only to refine reasoning. This distinction is important to prevent the agent from overfitting to historical mistakes and instead focus on adapting to present conditions. The agent is also explicitly instructed to compete with the baseline performance of 50/50 and get better returns.

### 3.4 Dual Verbal Feedback Mechanism

This section outlines the feedback mechanism that enables agents to improve over time. It consists of two components: the Reflect Agent, which generates daily feedback, and the Long-Term Reflect Agent, which produces weekly evaluations based on historical performance. A key distinction is that while the Reflect Agent relies on LLM-generated reasoning, the Long-Term Reflect Agent’s suggestions are hardcoded, designed to emulate a human-in-the-loop approach to trading assessment.

#### 3.4.1 Reflect Agent (Daily Feedback)

The Reflect Agent represents the first part of the system’s dual feedback mechanism. Its primary role is to provide daily performance reports and suggestions for improvement across agents. It does so by evaluating daily outcomes and generating targeted, context-aware feedback. It also acts as the system’s evaluation layer, calculating the performance metrics for each of the agents’ portfolios. Its central role, however, is to analyze the qualitative reasoning from the Quants, Signals, and Decision agents and critique it with the help of both performance metrics and the agents’ provided reasoning. An important insight is that it has to analyse whether agent decisions were justified based on the reasoning provided, rather than purely on their portfolio performance outcomes.

Reflect Agent evaluates daily predictions by comparing them with realized market movements, measuring returns, Sharpe ratios, regret, accuracy and producing targeted natural-language feedback. Performance metrics such as prediction accuracy, portfolio value change, and performance against the baseline are then computed. These metrics are not used in isolation to judge the agents, but rather to help determine whether their actions were justified given their available data. The logic is to distinguish between poor decisions caused by flawed predictions and reasoning and those due to unpredictable market behavior.

The core of the feedback process lies in the prompt construction, as this daily feedback loop is powered by the LLM: deepseek-r1. This prompt includes all relevant agent outputs, reasoning justifications, actual market returns, and performance metrics. The system prompt provides the context of its responsibility and the data it receives. It then provides precise instructions to the model to evaluate whether each agent’s prediction was logically consistent with their input data and whether the reasoning justified their analysis and trading decisions.

Prompt tuning in this system was particularly challenging because feedback generated by the Reflect Agent often strayed beyond the intended scope. Early experiments showed that the Signals Agent, which is restricted to sentiment and news data, was incorrectly instructed to incorporate technical indicators – data it did not have access to. To correct this, prompts had to be explicitly constrained so that feedback remained independent and tied only to the inputs available to each agent. A similar issue arose when feedback provided direct portfolio advice, such as suggesting the Decision Agent increase its Bitcoin allocation by 10%. Allowing such instructions would undermine the integrity of the reasoning process, as decisions must emerge from data-driven analysis rather than arbitrary adjustments. To address this, prompts were carefully designed to ensure that feedback focused only on critiquing reasoning, identifying errors, and suggesting improvements in analysis, without dictating specific allocations. These constraints made the system significantly harder to scale, since adding more agents or expanding their roles requires increasingly precise prompt design to prevent cross-contamination of inputs and preserve the validity of the reasoning process.

#### 3.4.2 Long Term Reflect Agent (Weekly Feedback)

No autonomous strategy can sustain profitability in the Bitcoin market without some form of oversight. This agent is therefore designed to supply a systematic analogue of that oversight: a weekly evaluation mechanism that mirrors the role of a human supervisor by reviewing agent performance over time, identifying deviations from expected behaviour, and suggesting appropriate corrective actions.

However, daily oversight alone is insufficient. The Reflect Agent provides day-by-day feedback, but single-day evaluations cannot capture slower-moving trends or recurring issues, and the system’s zero-shot prompting means there is no built-in memory across days. Although agents can react to the previous day’s notes, they do not retain awareness of mistakes made earlier in the week or month. To address this, the Long-Term Feedback Agent condenses a full trading week into a single summary that is persisted throughout the following week, effectively compensating for the stateless nature of the language models and supplying a structured form of memory. This weekly context also maintains a broader view of market conditions, guiding and strengthening the agents’ reasoning over time.

## 4 Evaluation Methodology

The system was evaluated on daily Bitcoin data from July 2024 to April 2025. Market regimes were defined using moving average trends to distinguish bullish, bearish, and sideways phases. Performance was measured against baselines including buy-and-hold BTC, a Nasdaq Crypto Index portfolio, and an equal-weighted basket of the top 30 cryptocurrencies. Key evaluation metrics included cumulative returns, Sharpe ratio, prediction accuracy, and regret.

## 5 Results and Discussion

Table 2: Performance of Agents Across Market Regimes and Metrics (Best Values Highlighted)

Regime
Metric
Quants (w/o LTF)
Decision (w/o LTF)
Signals (w/o LTF)
Quants (LTF)
Decision (LTF)
Signals (LTF)
Baseline


All Periods
Total Return (%)
21.05
11.50
21.14
6.73
14.51
23.92
18.27

Daily Return (mean ±\pm std)
0.08 ±\pm 1.582
0.052 ±\pm 1.630
0.08 ±\pm 1.609
0.035 ±\pm 1.519
0.059 ±\pm 1.524
0.088 ±\pm 1.592
0.069 ±\pm 1.379

Sharpe Ratio
0.0504
0.0318
0.0499
0.0227
0.0388
0.0553
0.0497

Accuracy
0.6297
0.6357
0.6358
0.6165
0.6402
0.6467
–

Sideways 1/2
Total Return (%)
-2.02
-3.38
2.99
0.08
1.35
7.13
-0.30

Daily Return (mean ±\pm std)
-0.002 ±\pm 1.417
-0.053 ±\pm 1.602
0.005 ±\pm 1.521
0.01 ±\pm 1.439
-0.005 ±\pm 1.429
0.031 ±\pm 1.436
-0.011 ±\pm 1.366

Sharpe Ratio
-0.0014
-0.0333
0.0033
0.0068
-0.0033
0.0216
-0.0081

Accuracy
0.6533
0.6472
0.6377
0.6561
0.6809
0.6910
–

Bullish
Total Return (%)
36.05
33.34
30.92
21.48
25.48
29.67
27.27

Daily Return (mean ±\pm std)
0.458 ±\pm 1.655
0.456 ±\pm 1.587
0.415 ±\pm 1.610
0.33 ±\pm 1.463
0.374 ±\pm 1.521
0.396 ±\pm 1.637
0.378 ±\pm 1.270

Sharpe Ratio
0.2765
0.2873
0.2578
0.2252
0.2457
0.2417
0.2972

Accuracy
0.6249
0.6313
0.6427
0.5921
0.6177
0.6039
–

Sideways 2
Total Return (%)
6.21
3.01
5.63
9.08
5.83
3.73
5.91

Bearish
Total Return (%)
-18.82
-20.98
-17.66
-23.43
-17.66
-15.87
-14.00

Daily Return (mean ±\pm std)
-0.151 ±\pm 1.701
-0.18 ±\pm 1.652
-0.128 ±\pm 1.701
-0.207 ±\pm 1.648
-0.154 ±\pm 1.618
-0.134 ±\pm 1.719
-0.116 ±\pm 1.445

Sharpe Ratio
-0.0889
-0.1088
-0.0750
-0.1254
-0.0949
-0.0778
-0.0805

Accuracy
0.6033
0.6266
0.6298
0.5852
0.6020
0.6163
–

Empirical evaluation on Bitcoin data (July 2024–April 2025) shows that the system consistently improved on static baselines across market regimes. Without long-term (weekly) feedback, the quantitative agent, as compared to the static buy and hold BTC portfolio, delivered over 30% higher returns in bullish phases and a 15% overall improvement, while the signals agent turned sideways markets from a slight loss into a gain of more than 100%. Introducing long-term weekly feedback amplified these effects: the signals agent achieved a 31% overall improvement as compared to without LTF, boosted sideways performance, and reduced bearish losses by more than 10%. These gains demonstrate that verbal feedback can serve as a scalable alternative to fine-tuning, enhancing both profitability and robustness under regime shifts.

Crucially, the verbal feedback mechanism was found to be decisive. Daily reflections reduced repeated short-term errors, while weekly feedback stabilized long-term strategy formation. Together, they allowed the agents to adapt their focus dynamically, replicating the benefits of human oversight without additional training costs.

## 6 Case Studies

### 6.1 Daily Feedback without Weekly (Long Term) Feedback

![Refer to caption](Picture1.png)


Figure 5: Cumulative Returns of the agents with daily feedback ONLY

On 4 November 2024, the Quants agent leaned heavily on bearish technicals (MACD -76.84, 70% of prices below VWAP, ADX = 27.33) and recommended a conservative 35% BTC / 65% cash allocation. The Signals agent, however, highlighted bullish catalysts: positive sentiment mean (+0.1164) and strong news flow on miner AI integration and $200K price targets, leading it to recommend 70% BTC / 30% cash. The Decision agent synthesized these by overweighting Quants’ technical caution, cutting BTC exposure to 40%, which proved overly conservative since Bitcoin actually gained +2.24% that day.

Reflect feedback was explicit: Quants had overemphasized bearish confluence without giving enough weight to neutral RSI/Bollinger signals, while the Decision agent was criticized for failing to quantify the strength of news catalysts (e.g., $200K targets as asymmetric upside). Signals, by contrast, received positive feedback for identifying the correct bullish call, with only minor suggestions to better calibrate FGI thresholds.

This feedback directly influenced the allocations on 5 November 2024. Quants softened its stance: though MACD remained bearish and ADX weak, it noted VWAP positioning and elevated on-chain activity ($50.58B volume, 528k addresses) as possible accumulation signals, recommending a higher 60% BTC exposure than the day before. Signals doubled down on its bullish framing, prioritizing the Trump election-driven rally to $75k and interpreting FGI=70 as a bullish but not extreme greed signal, leading to 65% BTC. The Decision agent, informed by Reflect’s critique of over-hedging, gave greater weight (65%) to Signals’ event-driven catalysts while still acknowledging Quants’ caution, settling on 55% BTC / 45% cash. This trade aligned with the sharp November rally, showing how the feedback loop enabled adaptation: Quants adjusted away from excessive pessimism, Signals refined its interpretation of sentiment extremity, and the Decision agent corrected its tendency to over-hedge, thereby capturing the upside more effectively.

### 6.2 Daily and Weekly Feedback

![Refer to caption](Picture2.png)


Figure 6: Cumulative Returns of the agents with Daily AND Weekly feedback

The weekly long-term feedback mechanism generates verbal, template-driven guidance at the end of each completed seven-day block. It evaluates performance relative to a passive baseline using regret, Sharpe ratio, and return differentials, and then produces standardised text such as “prioritize high-confidence inputs” or “reconstruct your indicator selection.” Importantly, this feedback does not alter any quantitative parameters: indicator thresholds, weightings, and allocation rules remain fixed. Instead, the generated text is re-introduced into the subsequent week’s prompts as additional context.

This design created an asymmetric effect across agents. The Signals agent, whose reasoning depends on interpreting natural language (news flow, sentiment reports, and textual priors), was able to incorporate such guidance effectively. For example, phrases such as “your signals consistently beat the baseline” reinforced its conviction, while instructions to prioritise high-confidence sources translated directly into more decisive sentiment weighting. This alignment between the form of feedback and the nature of the task explains why Signals exhibited marked improvement, as observed in the weekly narratives where it explicitly referenced feedback when framing its allocation logic.

By contrast, the Quants agent operates on numerical indicators such as VWAP, RSI, MACD, and ADX. Template feedback like “re-evaluate your indicator selection” offered no implementable adjustment to thresholds or weighting schemes, leaving its behaviour largely unchanged across weeks. Similarly, the Decision agent requires explicit allocation rules to balance Quants and Signals outputs. General remarks such as “improve allocation logic” or “reduce over-hedging” lacked the precision needed to modify weighting formulas, leading to continued inconsistencies in cash versus BTC exposure. In short, long-term feedback improved Signals because the guidance was expressed in a medium the agent could directly utilise, while Quants and Decision remained unaffected as they require structured, numeric adaptations rather than high-level prose.

## 7 Contributions and Conclusion

This thesis makes three key contributions:

1. 1.

   Novel Verbal Feedback Mechanism for LLM Optimization:
   Introduces a dual verbal feedback process that combines immediate (daily) and strategic (weekly) adaptation, representing a unique form of “verbal fine-tuning” for large language models.
   Unlike conventional parameter-based fine-tuning, this approach enables models to iteratively improve through natural language reasoning, making it more flexible, transparent, and cost-efficient for dynamic financial environments.
   Empirically, this feedback-driven mechanism enhances trading consistency and achieves superior risk-adjusted returns compared to both buy-and-hold and diversified crypto portfolios.
2. 2.

   Bitcoin Price Driver Framework:
   Establishes a framework that quantifies the impact of technical indicators, sentiment signals, and on-chain metrics on Bitcoin’s price movements, allowing a direct comparison of their contribution to trading performance.
3. 3.

   Modular Multi-Agent Architecture:
   Designs an agentic system that modularizes the trading workflow by sequentially analyzing market factors, generating insights, acting on those insights, evaluating the effectiveness of each action, and iteratively refining the system’s performance.

Limitations include the exclusive focus on Bitcoin, the daily trading frequency which omits intraday dynamics, and the noise inherent in sentiment data. Future work may extend the framework to multi-asset portfolios, integrate higher-frequency data, or explore hybrid strategies that combine verbal feedback with lightweight fine-tuning.

In sum, this thesis shows that an adaptive, feedback-driven multi-agent system can generate consistent Bitcoin trading profits under volatile conditions. By prioritizing profitability over predictive accuracy and employing language-based feedback as its optimization mechanism, the system demonstrates a scalable pathway for deploying LLMs in financial trading.

## References

* [1]

  W. M. Ahmed, “Robust drivers of bitcoin price movements: An extreme bounds analysis,” The North American Journal of Economics and Finance, vol. 62, 2022. [Online]. Available: <https://ideas.repec.org/a/eee/ecofin/v62y2022ics106294082200078x.html>
* [2]

  Y. Luo, Y. Feng, J. Xu, P. Tasca, and Y. Liu, “LLM-powered multi-agent system for automated crypto portfolio management,” 2025. [Online]. Available: <https://arxiv.org/abs/2501.00826>
* [3]

  Y. Li, B. Luo, Q. Wang, N. Chen, X. Liu, and B. He, “CryptoTrade: A reflective LLM-based agent to guide zero-shot cryptocurrency trading,” in Proc. of the 2024 Conference on Empirical Methods in Natural Language Processing, Miami, USA: ACL, 2024, pp. 1094–1106. [Online]. Available: <https://aclanthology.org/2024.emnlp-main.63/>
* [4]

  D. Araci, “FinBERT: Financial sentiment analysis with pre-trained language models,” 2019. [Online]. Available: <https://arxiv.org/abs/1908.10063>
* [5]

  Y. Li, S. Wang, H. Ding, and H. Chen, “Large language models in finance: A survey,” arXiv preprint arXiv:2311.10723, 2023. [Online]. Available: <https://arxiv.org/abs/2311.10723>
* [6]

  J. Lee, N. Stevens, S. C. Han, and M. Song, “A survey of large language models in finance (FinLLMs),” arXiv preprint arXiv:2402.02315, 2024. [Online]. Available: <https://arxiv.org/abs/2402.02315>
* [7]

  Y. Nie, Y. Kong, X. Dong, J. M. Mulvey, H. V. Poor, Q. Wen, and S. Zohren, “A survey of large language models for financial applications: Progress, prospects and challenges,” arXiv preprint arXiv:2406.11903, 2024. [Online]. Available: <https://arxiv.org/abs/2406.11903>
* [8]

  K. Papasotiriou, S. Sood, S. Reynolds, and T. Balch, “AI in investment analysis: LLMs for equity stock ratings,” arXiv preprint arXiv:2411.00856, 2024. [Online]. Available: <https://arxiv.org/abs/2411.00856>
* [9]

  A. Elliott et al., “The impact of large language models in finance: Towards trustworthy adoption,” The Alan Turing Institute, 2024. [Online]. Available: <https://www.turing.ac.uk/news/publications/impact-large-language-models-finance-towards-trustworthy-adoption>
* [10]

  K. Kamble et al., “Expect the unexpected: Failsafe long context QA for finance,” 2025. [Online]. Available: <https://arxiv.org/abs/2502.06329>
* [11]

  Z. Kou, H. Yu, J. Luo, J. Peng, and L. Chen, “Automate strategy finding with LLM in quant investment,” 2025. [Online]. Available: <https://arxiv.org/abs/2409.06289>
* [12]

  H. Yang et al., “FinRobot: An open-source AI agent platform for financial applications using large language models,” 2024. [Online]. Available: <https://arxiv.org/abs/2405.14767>
* [13]

  Bitcoin.org, “Why do bitcoins have value?” 2025. [Online]. Available: <https://bitcoin.org/en/faq#why-do-bitcoins-have-value>
* [14]

  CoinMarketCap, “Cryptocurrencies prices,” 2025. [Online]. Available: <https://coinmarketcap.com/>
* [15]

  Kaiko Research, “Why is ETH still lagging behind BTC?” 2025. [Online]. Available: <https://research.kaiko.com/insights/why-is-eth-still-lagging-behind-btc>
* [16]

  TradingView News, “Crypto graveyard: 50% of tokens have failed in the past 5 years,” 2025. [Online]. Available: <https://www.tradingview.com/news/newsbtc:081cf0629094b:0-crypto-graveyard-50-of-tokens-have-failed-in-the-past-5-years-report/>
* [17]

  Fidelity Digital Assets, “A closer look at Bitcoin’s volatility,” 2025. [Online]. Available: <https://www.fidelitydigitalassets.com/research-and-insights/closer-look-bitcoins-volatility>
* [18]

  M. Zhang, B. Zhu, Z. Li et al., “Relationships among return and liquidity of cryptocurrencies,” Financial Innovation, vol. 10, no. 1, p. 3, 2024. [Online]. Available: <https://doi.org/10.1186/s40854-023-00532-z>
* [19]

  A. S. Kumar and T. Ajaz, “Co-movement in crypto-currency markets: Evidences from wavelet analysis,” Financial Innovation, vol. 5, no. 1, pp. 1–17, 2019. [Online]. Available: <https://ideas.repec.org/a/spr/fininn/v5y2019i1d10.1186_s40854-019-0143-3.html>
* [20]

  M. Watorek, J. Kwapień, and S. Drożdż, “Cryptocurrencies are becoming part of the world global financial market,” Entropy, vol. 25, no. 2, p. 377, 2023. [Online]. Available: <http://dx.doi.org/10.3390/e25020377>
* [21]

  D. Güler, “The impact of investor sentiment on bitcoin returns and conditional volatilities during COVID-19,” Journal of Behavioral Finance, vol. 24, no. 3, pp. 276–289, 2023. [Online]. Available: <https://www.tandfonline.com/doi/full/10.1080/15427560.2021.1975285>
* [22]

  A. Alshamsi et al., “How regulation sentiments influence cryptocurrency? Is crypto a Wall Street darling?” SSRN Electronic Journal, 2022. [Online]. Available: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4080408>
* [23]

  Binance, “Crypto fear & greed index — bitcoin sentiment,” 2025. [Online]. Available: <https://www.binance.com/en/square/fear-and-greed-index>
* [24]

  L. Ante, “How Elon Musk’s Twitter activity moves cryptocurrency markets,” Technological Forecasting and Social Change, vol. 174, p. 121000, 2022. [Online]. Available: <https://www.sciencedirect.com/science/article/abs/pii/S0040162522006333>
* [25]

  J. Frasa, “Benefitting from bitcoin beliefs: Can Twitter sentiment obtained from a textblob analysis help predict bitcoin returns?” Bachelor Thesis, Erasmus University Rotterdam, 2023. [Online]. Available: <https://thesis.eur.nl/pub/73761/Bachelor-Thesis-Jeroen-Frasa.pdf>
* [26]

  Investopedia, “What charts should crypto investors use?” 2022. [Online]. Available: <https://www.investopedia.com/charts-for-crypto-6500665>
* [27]

  A. Hafid, M. Rahouti, L. Kong, M. Ebrahim, and M. A. Serhani, “Predicting bitcoin market trends with enhanced technical indicator integration and classification models,” arXiv preprint arXiv:2410.06935, 2024. [Online]. Available: <https://arxiv.org/abs/2410.06935>
* [28]

  A. E. d. O. Carosia, “Using sentiment and technical analysis to predict bitcoin with machine learning,” arXiv preprint arXiv:2410.14532, 2024. [Online]. Available: <https://arxiv.org/abs/2410.14532>
* [29]

  Amberdata, “How do on-chain metrics explain bitcoin volatility?” 2025. [Online]. Available: <https://blog.amberdata.io/part-1-how-do-on-chain-metrics-explain-bitcoin-volatility>
* [30]

  Investopedia, “The fear & greed index: What it is and how it works,” 2025. [Online]. Available: <https://www.investopedia.com/terms/f/fear-and-greed-index.asp>
* [31]

  Y. Qin et al., “DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning,” 2025. [Online]. Available: <https://arxiv.org/abs/2501.12948>
* [32]

  DeepSeek, “Models & pricing — DeepSeek API Docs,” 2025. [Online]. Available: <https://api-docs.deepseek.com/quick_start/pricing>
* [33]

  OpenAI, “API Pricing,” 2025. [Online]. Available: <https://openai.com/api/pricing/>
* [34]

  Anthropic, “Pricing,” 2025. [Online]. Available: <https://www.anthropic.com/pricing>
* [35]

  Knostic, “DeepSeek’s cutoff date is July 2024: We extracted…,” 2025. [Online]. Available: <https://www.knostic.ai/blog/exposing-deepseek-system-prompts>
* [36]

  Binance, “Binance API Documentation,” 2025. [Online]. Available: <https://www.binance.com/en-GB/binance-api>
* [37]

  Dune Analytics, “Dune Metrics Dashboard,” 2025. [Online]. Available: <https://dune.com/metrics>
* [38]

  Patrick Lewis, Ethan Perez, Aleksandra Piktus, et al.,
  ”Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,”
  arXiv preprint arXiv:2005.11401, 2020.
  [Online]. Available: <https://arxiv.org/abs/2005.11401>
* [39]

  OpenAI,
  ”Supervised Fine-Tuning,”
  OpenAI Documentation, 2023.
  [Online]. Available: <https://platform.openai.com/docs/guides/supervised-fine-tuning>
* [40]

  Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, et al.,
  ”Training language models to follow instructions with human feedback (InstructGPT),”
  arXiv preprint arXiv:2203.02155, 2022.
  [Online]. Available: <https://arxiv.org/abs/2203.02155>
* [41]

  Yue Zhang, Kaixiang Lin, Qiang Liu,
  ”Multi-Head Reinforcement Learning,”
  arXiv preprint arXiv:1909.11939, 2019.
  [Online]. Available: <https://arxiv.org/abs/1909.11939>
* [42]

  Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, et al.,
  ”Training language models to follow instructions with human feedback (InstructGPT),”
  arXiv preprint arXiv:2203.02155, 2022.
  [Online]. Available: <https://arxiv.org/abs/2203.02155>
* [43]

  Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Deep Ganguli, et al.,
  ”Constitutional AI: Harmlessness from AI Feedback,”
  arXiv preprint arXiv:2212.08073, 2022.
  [Online]. Available: <https://arxiv.org/abs/2212.08073>
* [44]

  Noah Shinn, Federico Bianchi, and Percy Liang,
  ”Reflexion: Language Agents with Verbal Reinforcement Learning,”
  arXiv preprint arXiv:2303.11366, 2023.
  [Online]. Available: <https://arxiv.org/abs/2303.11366>
* [45]

  Aman Madaan, Shuyan Zhou, Uri Alon, Yiming Yang, Graham Neubig,
  ”Self-Refine: Iterative Refinement with Self-Feedback,”
  arXiv preprint arXiv:2303.17651, 2023.
  [Online]. Available: <https://arxiv.org/abs/2303.17651>
* [46]

  Satoshi Nakamoto,
  ”Bitcoin: A Peer-to-Peer Electronic Cash System,”
  2008.
  [Online]. Available: <https://bitcoin.org/bitcoin.pdf>
* [47]

  U.S. Securities and Exchange Commission (SEC),
  ”SEC Approves First Spot Bitcoin Exchange-Traded Funds,”
  Press Release No. 2024-4, January 10, 2024.
  [Online]. Available: <https://www.sec.gov/news/press-release/2024-4>
* [48]

  Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin,
  ”Attention Is All You Need,”
  Advances in Neural Information Processing Systems (NeurIPS), 2017.
  [Online]. Available: <https://arxiv.org/abs/1706.03762>
* [49]

  Jaehoon Lee, Nicholas Stevens, Sang C. Han, and Min Song,
  ”A Survey of Large Language Models in Finance (FinLLMs),”
  arXiv preprint arXiv:2402.02315, 2024.
  [Online]. Available: <https://arxiv.org/abs/2402.02315>
* [50]

  Shijie Wu, Steven T. Pierson, Pengcheng Yin, Dragomir Radev, and the Bloomberg AI Team,
  ”BloombergGPT: A Large Language Model for Finance,”
  arXiv preprint arXiv:2303.17564, 2023.
  [Online]. Available: <https://arxiv.org/abs/2303.17564>
* [51]

  Jiaao Chen, Hanwen Zha, Tianyu Gao, Howard Yen, Siyi Chen, Shiyu Chang, and Diyi Yang,
  ”PIXIU: A Large Language Model, Instruction Data and Benchmark for Finance,”
  arXiv preprint arXiv:2306.05443, 2023.
  [Online]. Available: <https://arxiv.org/abs/2306.05443>
* [52]

  Yiming Luo, Yue Feng, Junxian Xu, Paolo Tasca, and Yike Liu,
  ”LLM-Powered Multi-Agent System for Automated Crypto Portfolio Management,”
  arXiv preprint arXiv:2501.00826, 2025.
  [Online]. Available: <https://arxiv.org/abs/2501.00826>
* [53]

  George S. Atsalakis, Konstantinos P. Valavanis, and Evangelos G. Pasiouras,
  ”Forecasting Bitcoin Price Using Neural Networks and Multiple Linear Regression,”
  Expert Systems with Applications, vol. 134, pp. 209–223, 2019.
  [Online]. Available: <https://doi.org/10.1016/j.eswa.2019.05.042>
* [54]

  Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, and Steven Goldfeder,
  ”Bitcoin and Cryptocurrency Technologies: A Comprehensive Introduction,”
  Princeton University Press, 2016.
  [Online]. Available: <https://press.princeton.edu/books/hardcover/9780691171692/bitcoin-and-cryptocurrency-technologies>
* [55]

  Dawei Shen, Xinyu Urquhart, and Xiaotong Zhang,
  ”On the Interlinkages of Bitcoin Price with Sentiment, Technical, and Blockchain Factors,”
  Research in International Business and Finance, vol. 54, 2020.
  [Online]. Available: <https://doi.org/10.1016/j.ribaf.2020.101284>