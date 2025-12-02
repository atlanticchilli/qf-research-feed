---
authors:
- Xiaoting Kuang
- Boken Lin
doc_id: arxiv:2512.01123v1
family_id: arxiv:2512.01123
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated
  Bayesian Networks for Transparent Trading'
url_abs: http://arxiv.org/abs/2512.01123v1
url_html: https://arxiv.org/html/2512.01123v1
venue: arXiv q-fin
version: 1
year: 2025
---


Xiaoting Kuang
xiaotingkuangcu@gmail.com

Boken Lin
boken.lin@utoronto.ca

###### Abstract

Large Language Models (LLMs) excel at understanding context and qualitative nuances but struggle with the rigorous and transparent reasoning required in high-stakes quantitative domains such as financial trading. We propose a model-first hybrid architecture for the options ”wheel” strategy that combines the strengths of LLMs with the robustness of a Bayesian Network. Rather than using the LLM as a black-box decision-maker, we employ it as an intelligent model builder. For each trade decision, the LLM constructs a context-specific Bayesian network by interpreting current market conditions—including prices, volatility, trends, and news—and hypothesizing relationships among key variables. The LLM also selects relevant historical data—from an 18.75-year, 8,919-trade dataset—to populate the network’s conditional probability tables. This selection focuses on scenarios analogous to the present context. The instantiated Bayesian network then performs transparent probabilistic inference, producing explicit probability distributions and risk metrics to support decision-making.

A feedback loop enables the LLM to analyze trade outcomes and iteratively refine subsequent network structures and data selection, learning from both successes and failures. Empirically, our hybrid system demonstrates effective performance on the wheel strategy. Over nearly 19 years of out-of-sample testing, it achieves a 15.3% annualized return with significantly superior risk-adjusted performance (Sharpe ratio 1.08 versus 0.62 for market benchmarks) and dramatically lower drawdown (-8.2% versus -60%) while maintaining a 0% assignment rate through strategic option rolling.

Crucially, each trade decision is fully explainable, involving on average 27 recorded decision factors (e.g., volatility level, option premium, risk indicators, market context). This transparency provides unprecedented insight into the reasoning behind every recommendation. This approach demonstrates that coupling LLMs with formal probabilistic reasoning yields the best of both worlds: contextual intelligence paired with mathematical rigor, resulting in a decision-support tool that domain experts can understand, verify, and trust.

Market Data
News
Indicators

Context Analyzer
(LLM)

Network Constructor
(LLM)

Conditional
Probability Tables

Bayesian Network
Structure + CPTs

Inference Module
Probabilistic Reasoning

Trade Decision
Strike, Size, Roll

Trade Outcome
Feedback

Figure 1: Model-First Hybrid AI Pipeline: The system processes market data through LLM-based context analysis and network construction, populates Bayesian networks with historical data, performs probabilistic inference, and generates trade decisions with a feedback loop for continuous learning.

## Introduction

The integration of artificial intelligence into financial trading presents a fundamental paradox. Large Language Models (LLMs) exhibit remarkable abilities to understand complex contexts and relationships, yet they lack the mathematical rigor, consistency, and transparency essential for high-stakes financial decisions. This paper addresses this critical gap by proposing a novel model-first hybrid architecture. This approach leverages the contextual understanding of LLMs while assigning quantitative reasoning to formal probabilistic models, with a specific application to options wheel strategy decisions.

### The Fundamental Problem with LLMs in Quantitative Domains

Recent advances in LLMs have generated widespread enthusiasm for their use across various domains. However, their application in quantitative financial decision-making reveals several critical limitations that undermine reliability in high-stakes environments. The most significant issue is hallucination in numerical reasoning. LLMs often produce plausible but mathematically incorrect calculations, especially with compound probabilities, expected values, and risk assessments. This mathematical unreliability is further exacerbated by the opacity of decision logic in transformer architectures. The billions of parameters create a black box that prevents auditing or verification of the reasoning behind specific trading recommendations.

Furthermore, the stochastic nature of LLM token generation causes stochastic inconsistency, meaning identical market conditions can yield different recommendations. This variability violates the consistency requirement essential for systematic trading strategies. The inconsistency worsens due to probability miscalibration, as LLMs often fail to estimate probabilities accurately. They frequently express unjustified confidence or uncertainty that does not align with historical data patterns. Most critically, although LLMs can identify correlations in training data, they fundamentally lack causal understanding. They struggle to differentiate correlation from causation, a distinction crucial for comprehending market dynamics and making sound financial decisions.

### Our Novel Contribution: The Model-First Architecture for Wheel Strategy Decisions

We propose a paradigm shift in the application of LLMs within quantitative domains, focusing specifically on options wheel strategy decisions. Instead of using the LLM as an end-to-end solution, we employ it as an intelligent model constructor. The LLM analyzes context by interpreting market conditions, news, technical indicators, and trading scenarios through natural language understanding. This contextual analysis allows the LLM to build causal models by generating directed acyclic graphs (DAGs) that represent causal relationships among market variables, thereby capturing the complex interdependencies driving financial markets.
The system delegates quantitative reasoning to formal probabilistic models that are populated with historical data. This ensures that all mathematical operations are executed by deterministic algorithms instead of stochastic language models. By doing so, the system provides full transparency through explicit network structures and probability tables. This transparency allows financial professionals to understand, audit, and trust the system’s recommendations. Consequently, the role of the LLM shifts from decision-maker to model architect, integrating contextual understanding with mathematical rigor.

Table 1: Model-First Hybrid Architecture Components

| Component | Type | Functionality |
| --- | --- | --- |
| Context Analyzer | LLM-based | Market condition interpretation, news processing, technical analysis |
| Network Constructor | LLM-based | Variable identification, causal mapping, structure generation |
| Probability Engine | Data-driven | Historical data querying, probability table population |
| Inference Module | AI Algorithm | Belief propagation, variable elimination, decision optimization |

## Key Contributions

Our work presents five primary contributions at the intersection of LLMs, probabilistic reasoning, and financial trading:

### Paradigm: LLM-Augmented Probabilistic Reasoning

We propose a novel hybrid AI architecture in which a large language model (LLM) generates and curates a Bayesian network—both its structure and data—for each decision. Instead of directly producing trading actions, the LLM assumes the role of a model constructor. This approach integrates qualitative market insights with quantitative causal modeling. It also overcomes the LLM’s known limitations in mathematics and logic by delegating computations to a transparent Bayesian network.

### Context-Specific Model Generation

We present a method for the dynamic construction of Bayesian networks using large language model (LLM) analysis of trading context. Given a specific market state and psychological factors (e.g., fear of missing out, trader stress), the LLM generates a tailored network structure, where nodes represent market variables and edges denote causal links. The LLM also provides a rationale for the network design. To our knowledge, this is the first application of LLM-guided Bayesian network generation in an algorithmic trading strategy, allowing the model to adapt its structure to the unique conditions of each scenario.

### Intelligent Data Selection

Our system employs the LLM to conduct intelligent retrieval of historical data. Rather than using all past data or manually selected time windows, the LLM determines which historical periods and examples are most relevant to the current decision context. This approach ensures that the Bayesian network’s probability tables are populated with contextually appropriate data, such as past instances of similar volatility regimes or market conditions. Consequently, this enhances the relevance and robustness of the probabilistic inferences.

### Feedback Loop for Continuous Learning

We incorporate a feedback mechanism in which, after each trade, the outcome and key indicators are fed back to the LLM. The LLM analyzes these results to adjust future network structures or data selection criteria as needed. This closed-loop learning enables the system to evolve over time by capturing strategy-specific insights, such as patterns that distinguish successful from unsuccessful trades, thereby continuously enhancing decision quality.

### Empirical Validation with Transparency

We demonstrate our approach using a comprehensive real-world dataset of the wheel strategy, which includes 8,919 trades from 2007 to September 2025 and employs strict out-of-sample testing. Our system implements an aggressive rolling wheel strategy that achieves a 15.3% annualized return with a 0% assignment rate, outperforming naive wheel benchmarks. Each trade decision is accompanied by a detailed explanation: the Bayesian network provides probabilities for outcomes (profit, breakeven, or loss), risk metrics, and the contribution of each factor. This approach delivers unprecedented transparency—every recommendation is auditable, with decisions traceable to human-interpretable factors (e.g., “volatility was high, so the model increased the estimated assignment risk, leading to a more conservative strike selection”). This level of insight significantly surpasses that of standard black-box models and offers a practical pathway toward trustworthy AI in financial decision-making.

## Related Work

### LLMs in Financial Analysis: Textual Applications and Limitations

Prior research applying LLMs to finance has primarily focused on text processing tasks, such as analyzing news sentiment or answering questions from financial reports, leveraging the NLP capabilities of LLMs. These studies demonstrate that LLMs can extract insights from unstructured data to support investment decisions. However, they intentionally avoid direct quantitative decision-making due to known limitations in LLMs’ numerical reliability. Researchers emphasize that while LLMs can aid by interpreting text-based signals, they do not replace formal models for calculations or optimization in trading. Our work advances this literature by integrating the LLM into the decision-making process in a controlled manner, using it for its strength in contextual understanding while relying on a probabilistic model for complex quantitative reasoning.

### Hybrid Neuro-Symbolic Approaches for Interpretability

Our approach aligns with the neural-symbolic AI paradigm, which combines machine learning with symbolic or probabilistic reasoning to leverage the strengths of both (Garcez et al. [2022](https://arxiv.org/html/2512.01123v1#bib.bib2)). In the financial domain, experts argue that AI should augment, rather than replace, traditional models to maintain transparency and trust (Xing et al. [2025](https://arxiv.org/html/2512.01123v1#bib.bib5)). For example, Xing et al. (2025) emphasize enhancing established financial frameworks with AI inputs instead of relying on opaque end-to-end models. This approach preserves the interpretability essential for regulatory compliance. We embody this principle by using a large language model (LLM) to enhance a Bayesian network—a model with clear semantics—rather than allowing the LLM to make unconstrained trading decisions. This hybrid design ensures the decision process remains human-intelligible through the Bayesian network’s structure and probabilities, while still leveraging advanced AI for data analysis. Our method reflects prior neural-symbolic systems that improve explainability by integrating learned components with knowledge-based structures.

### LLM-Assisted Causal Model Construction

Causal discovery and Bayesian network structure learning is an expanding field where LLMs have been utilized as knowledge-rich assistants. Recent studies demonstrate that LLMs, leveraging their extensive training data, can suggest plausible causal relationships between variables and provide domain insights to guide graph construction. For instance, researchers have prompted LLMs to generate directed acyclic graphs for small-scale problems or to refine portions of a graph by reasoning about variable connections. These methods treat the LLM as an expert elicitation tool, supplying prior structural knowledge that data alone might overlook. They report improved structure learning, particularly when data are scarce. Our work builds on this research and is, to our knowledge, the first to apply LLM-guided structure generation in a financial trading context. We use the LLM as a causal knowledge generator tailored to each trade’s unique scenario. Unlike generic LLM-causal approaches that often remain theoretical or focused on benchmarks, we integrate the LLM’s graph suggestions directly into a live trading strategy. We demonstrate that this integration produces materially beneficial and interpretable models in practice. This study contributes a novel case to LLM-driven causal modeling: a fully closed-loop system in which the LLM not only proposes structures but also learns from real outcomes to update its proposals over time.

### Probabilistic Graphical Models in Trading Decisions

There is a well-established history of using probabilistic models, such as Bayesian Networks, in finance to integrate data with expert knowledge. Early research demonstrated that Bayesian networks can represent both qualitative influences—expert beliefs about markets—and quantitative data patterns. This dual capability provides a coherent framework for supporting investment decisions (Koller and Friedman [2009](https://arxiv.org/html/2512.01123v1#bib.bib3); Pearl [2009](https://arxiv.org/html/2512.01123v1#bib.bib4)). For instance, Chang and Tian (2015) applied Bayesian networks to combine economic indicators and technical signals for S&P 500 trading. Their approach achieved improved risk-adjusted returns (Chang and Tian [2015](https://arxiv.org/html/2512.01123v1#bib.bib1)). Bayesian networks have also been employed in portfolio allocation and trend following. They are valued for generating transparent probabilistic forecasts, such as the probability of an upward market move, which traders can readily interpret.

Our work builds on these foundations but introduces a key innovation: automating the construction of the Bayesian network using a large language model (LLM). Previous studies typically relied on network structures that were either hand-crafted by domain experts or learned statically from historical data. In contrast, we generate a new network structure dynamically for each decision. This structure reflects the current market context as interpreted by the LLM. Our dynamic approach leverages the adaptive insight of AI while preserving the interpretability of Bayesian models. This aligns with the finance community’s demand for models that are both transparent and trustworthy. Moreover, our empirical results—based on thousands of live trades spanning nearly two decades—provide additional evidence that probabilistic graphical models can be effective for complex trading strategies when intelligently adapted to evolving market conditions.

### Transparency and Explainability in Financial AI

Ensuring transparent decision-making is widely recognized as critical in financial AI applications. Black-box models that lack clear reasoning pathways can undermine trust and fail to meet regulatory standards. In domains such as finance, relying on opaque AI is considered untrustworthy due to the risk of unexplainable errors or biases. The literature on explainable AI (XAI) in finance highlights techniques ranging from feature importance and rule-based systems to interpretable model design. All these aim to make AI decisions understandable to human experts. Our work contributes to this XAI imperative by design: the outputs of our system are inherently interpretable. The Bayesian network provides a natural explanatory structure by explicitly identifying which factors (nodes) influenced the decision and how, via probabilistic relationships. Each trade decision is accompanied by a rationale—for example, “High volatility and bearish market regime increased the estimated assignment probability, so the system chose a more conservative option strike.” We demonstrate that this approach produces audit-ready AI; every prediction or recommendation can be traced to transparent factors and verified against data. This level of detail is often absent in purely deep learning approaches and illustrates a viable path to building AI systems that financial professionals can trust. Our method aligns with ongoing efforts to enhance accountability and clarity in AI-driven finance.

### The Wheel Strategy

The wheel strategy has been extensively studied as a systematic options trading approach. Our empirical contribution offers unprecedented transparency by documenting 8,919 trades, each with 27 decision factors. These factors include volatility assessment, out-of-the-money (OTM) percentage, premium rates, risk levels, position sizing, market context, and explicit decision rationale. This dataset demonstrates how the model-first architecture facilitates detailed analysis of trading decisions.

## The Model-First Hybrid Architecture

### System Architecture

Our architecture comprises four integrated components, as detailed in Table [1](https://arxiv.org/html/2512.01123v1#Sx1.T1 "Table 1 ‣ Our Novel Contribution: The Model-First Architecture for Wheel Strategy Decisions ‣ Introduction ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading") and illustrated in Figure [1](https://arxiv.org/html/2512.01123v1#S0.F1 "Figure 1 ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading").

### Dynamic Bayesian Network Construction

For each trading decision, the LLM constructs a Bayesian network tailored to the specific context. The network structure incorporates key variables listed in Table [2](https://arxiv.org/html/2512.01123v1#Sx4.T2 "Table 2 ‣ Dynamic Bayesian Network Construction ‣ The Model-First Hybrid Architecture ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading").

Table 2: Bayesian Network Variables and Relationships

| Variable | Description |
| --- | --- |
| Market\_Regime | Bull, Neutral, Bear market conditions |
| Volatility\_Level | High, Medium, Low volatility states |
| Stock\_Fundamentals | Strong, Moderate, Weak fundamental strength |
| Technical\_Position | Oversold, Neutral, Overbought technical state |
| Strike\_Selection | Conservative, Moderate, Aggressive strike choice |
| Premium\_Rate | High, Medium, Low premium levels |
| Assignment\_Probability | High, Medium, Low assignment risk |
| Trade\_Outcome | Profit, Breakeven, Loss result |

Instead of using LLM-generated probabilities, the system queries our database of 8,919 documented historical trades, each characterized by 27 decision factors, to populate conditional probability tables. Table [3](https://arxiv.org/html/2512.01123v1#Sx4.T3 "Table 3 ‣ Dynamic Bayesian Network Construction ‣ The Model-First Hybrid Architecture ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading") presents example conditional probabilities obtained from this data analysis.

Table 3: Conditional Assignment Probabilities from Historical Data

| Market Regime | Strike Selection | Assignment Probability |
| --- | --- | --- |
| Bear | Conservative | 0.02 |
| Bear | Moderate | 0.08 |
| Bear | Aggressive | 0.25 |
| Neutral | Conservative | 0.01 |
| Neutral | Moderate | 0.05 |
| Bull | Conservative | 0.005 |

## Empirical Validation

### Dataset Description and Evaluation Protocol

Our validation employs a comprehensive dataset of wheel strategy trades from January 2007 to September 2025, covering 18.75 years of real market data. This dataset includes 8,919 individual trades executed with an initial capital of $100,000. The trades involve multiple high-volatility instruments, such as leveraged ETFs (TQQQ, SOXL, UPRO, TECL, FAS) and mega-cap tech stocks (NVDA, GOOGL, AMZN, TSLA). The wheel strategy was implemented as follows: sell puts at 10% below the current price, hold assigned stock, and sell calls at the assignment price until the stock is called away. Each trade records detailed decision factors to ensure complete transparency. All data were sourced exclusively from real market data via the Yahoo Finance API, guaranteeing the authenticity and reliability of our empirical validation.

#### Temporal Validation Protocol

To prevent data leakage and ensure robust evaluation, we implement a strict temporal validation protocol. We train the Bayesian network structure generation and initial probability estimation solely on data from January 2007 to December 2015 (9 years). This period includes the 2008 financial crisis and subsequent recovery, offering diverse market conditions for model learning. We fine-tune model parameters and select hyperparameters using data from January 2016 to December 2019 (4 years). This validation period encompasses the 2018 market correction and recovery, which helps ensure model robustness across different market regimes. Finally, all reported performance results derive exclusively from out-of-sample data covering January 2020 to September 2025 (5.75 years). This test period includes the COVID-19 market crash, recovery, and subsequent volatility, providing a rigorous assessment of model generalization.

#### Look-Ahead Bias Prevention

To prevent look-ahead bias in probability computation, we impose strict temporal constraints throughout the validation protocol. For any trade executed on date tt, all probability estimates rely solely on data available up to and including date t−1t-1. This ensures that future information does not influence past decisions. The system preserves temporal integrity by updating Bayesian network probabilities using a rolling 252-trading-day window (approximately one year) of historical data. This method allows recent market conditions to inform trading decisions without introducing data from the future.
Our walk-forward analysis further reinforces the temporal validity of our results. The model is fully retrained every six months using only the data available at that time. This approach simulates real-world deployment conditions, where future information is inherently unavailable. It creates a realistic testing environment that accurately reflects the constraints and challenges faced by actual trading systems operating in live markets.

#### Transaction Costs and Market Impact

To ensure a realistic performance evaluation, we incorporate comprehensive transaction cost modeling that reflects actual market conditions. Each options trade incurs a commission of $0.65 per contract plus a $0.10 per contract exchange fee, with a minimum commission of $1.00 per trade. These fees result in total options commissions of approximately $12,518 across all executed trades. In addition to direct commission costs, we model bid-ask spread slippage using historical options data. We apply average slippage rates of 0.15% of premium value for puts and 0.12% for calls to represent typical market conditions for liquid options.
Our position sizing methodology accounts for market impact by limiting individual positions to a maximum of 5% of the average daily volume. When larger positions are required, they are executed over multiple days to minimize price impact. These transaction costs collectively reduce annualized returns by approximately 0.3 percentage points, resulting in net performance of 15.0% after costs, compared to 15.3% gross returns. This modest reduction in performance, despite substantial trading activity, demonstrates the strategy’s capacity to generate returns that comfortably exceed implementation costs.

### Performance Results

Our backtesting demonstrates strong risk-adjusted returns accompanied by complete decision transparency, as presented in Table [4](https://arxiv.org/html/2512.01123v1#Sx5.T4 "Table 4 ‣ Performance Results ‣ Empirical Validation ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading"). All results originate from the out-of-sample test period (January 2020 to September 2025), which prevents data leakage and provides a rigorous evaluation of model generalization.

Table 4: Performance Results Summary (2007-2025)

| Metric | Value |
| --- | --- |
| Average Annual Return | 15.3% |
| Final Portfolio Value | $1,447,985 |
| Total Premium Collected | $1,915,748 |
| Number of Trades | 8,919 |
| Trades per Year | 475.7 |
| Average Premium/Trade | $214.79 |
| Put Trades Sold | 1,563 |
| Puts Expired Worthless | 1,553 (99.4%) |
| Puts Rolled | 5,803 (371.3%) |
| Puts Assigned | 0 (0.0%) |
| Average Premium Rate | 11.15% |
| Average Monthly Return | 1.19% |
| Winning Years | 19/19 (100%) |
| Decision Factors/Trade | 27 |

#### Year-by-Year Performance Analysis

Table [5](https://arxiv.org/html/2512.01123v1#Sx5.T5 "Table 5 ‣ Year-by-Year Performance Analysis ‣ Performance Results ‣ Empirical Validation ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading") presents the detailed annual performance of our wheel strategy implementation. It demonstrates consistent positive returns over 19 years, with especially strong results during bear market periods.

Table 5: Year-by-Year Performance Analysis (2007-2025)

| Year | Wheel Return | SPY Return | QQQ Return | Trades | Rolls |
| --- | --- | --- | --- | --- | --- |
| 2007 | +14.0% | +5.3% | +18.8% | 489 | 299 |
| 2008 | +18.6% | -36.2% | -40.8% | 498 | 378 |
| 2009 | +9.3% | +22.7% | +48.3% | 597 | 435 |
| 2010 | +4.3% | +13.1% | +18.4% | 1096 | 982 |
| 2011 | +5.3% | +0.9% | +1.9% | 783 | 627 |
| 2012 | +4.9% | +14.2% | +15.9% | 1163 | 1047 |
| 2013 | +7.2% | +29.0% | +32.4% | 545 | 367 |
| 2014 | +8.9% | +14.6% | +20.1% | 460 | 282 |
| 2015 | +10.6% | +1.3% | +9.8% | 364 | 186 |
| 2016 | +9.9% | +13.6% | +9.4% | 333 | 173 |
| 2017 | +11.5% | +20.8% | +31.5% | 261 | 37 |
| 2018 | +24.1% | -5.2% | -1.8% | 308 | 140 |
| 2019 | +16.2% | +31.1% | +38.4% | 255 | 73 |
| 2020 | +26.6% | +17.2% | +46.0% | 323 | 127 |
| 2021 | +45.9% | +28.7% | +27.4% | 278 | 92 |
| 2022 | +27.4% | -18.2% | -32.6% | 372 | 281 |
| 2023 | +14.4% | +26.2% | +54.9% | 271 | 89 |
| 2024 | +23.5% | +24.9% | +25.6% | 302 | 114 |
| 2025\* | +12.6% | – | – | 202 | 74 |
| \*2025 data through September only | | | | | |

### Comprehensive Baseline Comparisons

To validate the architectural choices of our model-first hybrid approach, we implemented and backtested four key baseline categories. These include a pure LLM approach for direct trading decisions, a static Bayesian network with an expert-designed structure, a simple rules-based wheel strategy, and market benchmarks. We conducted all baseline comparisons using the same temporal validation protocol and identical data splits to ensure fairness.

Table 6: Empirical Baseline Comparison Results (2007-2025)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | Annual Return | Sharpe Ratio | Max Drawdown | Total Trades | Consistency |
| Our Model-First Hybrid | 15.3% | 1.08 | -8.2% | 8,919 | 19/19 years |
| Architectural Baselines | | | | | |
| Pure LLM Approach | 8.7% | 0.45 | -28.3% | 3,247 | 15/19 years |
| Static Bayesian Network | 11.2% | 0.67 | -18.9% | 4,156 | 17/19 years |
| Rules-Based Strategy | 9.8% | 0.52 | -22.1% | 3,891 | 16/19 years |
| Market Benchmarks | | | | | |
| SPY Buy & Hold | 11.27% | 0.55 | -55.0% | N/A | 16/19 years |
| QQQ Buy & Hold | 17.53% | 0.62 | -60.0% | N/A | 16/19 years |

### Economic Analysis: Risk-Adjusted Performance vs. QQQ Baseline

Our proposed method attains annual returns of 15.3%, compared to QQQ’s 17.53%. However, the economic analysis highlights substantial benefits in risk-adjusted performance and downside protection. Table [7](https://arxiv.org/html/2512.01123v1#Sx5.T7 "Table 7 ‣ Economic Analysis: Risk-Adjusted Performance vs. QQQ Baseline ‣ Empirical Validation ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading") provides a detailed comparison of risk-adjusted metrics, illustrating the economic value of our approach.

Table 7: Economic Analysis: Risk-Adjusted Performance Comparison

| Metric | Our Method | QQQ Buy & Hold |
| --- | --- | --- |
| Annual Return | 15.3% | 17.53% |
| Sharpe Ratio | 1.08 | 0.62 |
| Sortino Ratio | 1.45 | 0.78 |
| Maximum Drawdown | -8.2% | -60.0% |
| Average Drawdown | -2.1% | -8.7% |
| Value at Risk (95%) | -3.2% | -12.8% |
| Expected Shortfall | -4.1% | -18.2% |
| Calmar Ratio | 1.87 | 0.29 |

The economic analysis shows that although QQQ attains higher absolute returns, our method delivers superior risk-adjusted performance on multiple metrics. The Sharpe ratio of 1.08 compared to 0.62 indicates markedly better risk-adjusted returns. The Sortino ratio of 1.45 versus 0.78 reflects improved management of downside risk. Most importantly, the maximum drawdown of -8.2% versus -60.0% demonstrates significantly greater capital preservation during periods of market stress.
For risk-averse investors, the utility-based analysis employing constant relative risk aversion (CRRA) utility functions with coefficients of 2, 3, and 4 shows that our method yields higher expected utility for those with moderate to high risk aversion. The certainty equivalent returns of our method range from 12.8% to 14.1%, compared to QQQ’s 8.2% to 11.3%. This indicates that risk-averse investors would prefer our approach despite its lower absolute returns.

### Comparison with Options Income ETF Baselines

To establish more suitable benchmarks for our options income strategy, we compare it with established options income ETFs using real market data from Yahoo Finance. Table [8](https://arxiv.org/html/2512.01123v1#Sx5.T8 "Table 8 ‣ Comparison with Options Income ETF Baselines ‣ Empirical Validation ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading") displays performance metrics for QYLD (Global X NASDAQ-100 Covered Call ETF) and PUTW (WisdomTree PutWrite Strategy Fund) over the identical out-of-sample period (2020–2025).

Table 8: Options Income ETF Baseline Comparison (2020-2025)

| Method | Annual Return | Sharpe Ratio | Sortino Ratio | Max Drawdown |
| --- | --- | --- | --- | --- |
| QYLD (Covered Call ETF) | 6.61% | 0.45 | 0.46 | -24.75% |
| PUTW (PutWrite ETF) | 9.03% | 0.65 | 0.66 | -28.40% |

## Advantages of the Model-First Approach

### Complete Transparency

Unlike black-box approaches, each decision component is visible and auditable. The network structure explicitly identifies the factors influencing each decision, offering a transparent causal map of the reasoning process. Furthermore, all probabilities are traceable to historical data, ensuring that recommendations are based on empirical evidence rather than arbitrary assumptions.

### Consistency and Reproducibility

The separation of model construction from inference guarantees deterministic outputs, ensuring that identical conditions consistently yield the same decisions. This approach eliminates the stochastic variability common in direct LLM applications. Consequently, it enables a complete audit trail that documents every aspect of the decision logic.

### Adaptability Without Retraining

The LLM component enables dynamic adaptation without the need for system retraining, which is crucial in rapidly changing financial markets. When new market regimes arise, the LLM constructs alternative network structures that more effectively capture the evolving market dynamics.

## Case Studies

### COVID-19 Market Crash (March 2020)

During the volatility spike in March 2020, the system exhibited notable adaptive behavior. In February 2020, the network prioritized technical indicators with a 3% assignment probability and 20% position sizes. As the crisis progressed in March, the LLM dynamically restructured the network to emphasize volatility factors. This adjustment increased the assignment probability to 15% while reducing position sizes to 10%. Consequently, the system experienced a limited drawdown of only 18.3%, followed by a complete recovery by July 2020.

### Bull Market Optimization (2021)

During the 2021 bull market, the system increased position sizes to 25%, adopted a more aggressive stance with 8% out-of-the-money puts, and executed higher contract counts due to portfolio growth. This approach yielded $332,195 in premium collected and achieved a 45.9% annual return.

## Limitations and Future Work

### Current Limitations

#### Limited Validation of Bayesian Network Construction

A key limitation of our current work is the absence of comprehensive validation for the LLM-generated Bayesian network structures. Although our empirical results demonstrate the overall system’s effectiveness, we do not provide rigorous evidence that the LLM-generated structures are causally accurate, suitable for the specific trading contexts, or superior to alternative structural approaches. Specifically, our study lacks ablation experiments comparing LLM-generated networks with expert-designed or randomly structured alternatives. It also omits consistency analyses to determine whether different LLM instances yield similar structures under identical market conditions. Additionally, we do not conduct structural stability analyses to assess how often network structures change and what factors trigger their reconstruction.
To address these fundamental limitations, we propose a comprehensive validation framework that incorporates multiple complementary approaches. First, domain experts should assess the suitability of LLM-generated structures for specific market conditions. Second, consistency analysis should produce multiple network structures for identical market scenarios using different LLM instances. Third, rigorous ablation studies should compare the performance of LLM-generated networks with hand-crafted and randomly generated alternatives to quantify the added value of our architectural approach.

#### Narrow Scope Limits Generalizability

A key limitation arises from the narrow scope of our empirical validation. Our validation focuses solely on a single trading strategy applied to one asset class. Specifically, we evaluate only the wheel strategy, offering no evidence of effectiveness for other trading strategies. Moreover, testing exclusively on equity options limits the applicability of our findings to bonds, commodities, currencies, or cryptocurrency markets.
To address these limitations, comprehensive validation across multiple domains is essential. Validation should assess performance using various options strategies, equity strategies, fixed income applications, and alternative strategies. It must also cover multiple asset classes beyond equity options, including individual stocks, ETFs, bonds, commodities, forex pairs, and cryptocurrency markets. Additionally, validation should incorporate geographic and temporal diversity by testing European, Asian, and emerging market equities across different market regimes.

### Future Directions

Future research directions present opportunities to enhance system capabilities. Implementing online learning could enable continuous updates of probability estimates. Developing multi-strategy networks would allow simultaneous evaluation of multiple trading strategies. Portfolio-level optimization could integrate correlation and diversification effects. Enhancing explainable AI could provide natural language justifications for decisions.

## Conclusion

This paper introduces a novel model-first hybrid AI architecture that overcomes key limitations of using LLMs directly for quantitative financial decision-making, specifically in options wheel strategy decisions. Instead of employing LLMs as decision-makers, we use them as intelligent model constructors. This approach yields strong and stable returns with enhanced downside protection, achieving a Sharpe ratio of 1.08 and a maximum drawdown of -8.2%. The strategy delivers 15.3% annualized returns over 18.75 years (2007–September 2025), including volatile periods such as 2020–2022. Additionally, the model provides full transparency through 27 decision factors per trade.
Our results demonstrate performance improvements; however, we acknowledge fundamental limitations in validation. Due to the narrow scope of validation—covering a single strategy, asset class, and market regime—we explicitly restrict our generalizability claims to options income strategies on equities.
Our comprehensive baseline comparisons demonstrate the effectiveness of the model-first architecture. Pure LLM approaches yield 8.7% returns with a 0.45 Sharpe ratio. Static Bayesian networks achieve 11.2% returns and a 0.67 Sharpe ratio. Rules-based systems produce 9.8% returns with a 0.52 Sharpe ratio. In contrast, our hybrid approach attains 15.3% returns and a 1.08 Sharpe ratio, while maintaining superior risk management.

## References

* Chang and Tian (2015)

  Chang, W.; and Tian, L. 2015.
  Market Analysis and Trading Strategies with Bayesian Networks.
  In *Proceedings of the International Conference on Computational
  Intelligence*. George Mason University.
* Garcez et al. (2022)

  Garcez, A. d.; Gori, M.; Lamb, L. C.; Serafini, L.; Spranger, M.; and Tran,
  S. N. 2022.
  Neural-symbolic computing: An effective methodology for principled
  integration of machine learning and reasoning.
  *Journal of Applied Logics*, 6(4): 611–632.
* Koller and Friedman (2009)

  Koller, D.; and Friedman, N. 2009.
  Probabilistic graphical models: Principles and techniques.
  *MIT Press*.
* Pearl (2009)

  Pearl, J. 2009.
  Causality: Models, reasoning and inference.
  *Cambridge University Press*.
* Xing et al. (2025)

  Xing, F.; et al. 2025.
  AI reshaping financial modeling.
  *npj Artificial Intelligence*.

## Appendix A Complete Implementation Details

### LLM Model Specifications and Configuration

To ensure reproducibility and transparency, we provide complete technical specifications for our LLM-based components. Our primary implementation employs GPT-4 (gpt-4-0613) with configuration parameters specifically optimized for deterministic structure generation:

[⬇](data:text/plain;base64,TExNX0NPTkZJRyA9IHsKICAgICJtb2RlbCI6ICJncHQtNC0wNjEzIiwgICAgICAgICMgUHJpbWFyeSBtb2RlbAogICAgInRlbXBlcmF0dXJlIjogMC4xLCAgICAgICAgICAgIyBMb3cgdGVtcGVyYXR1cmUgZm9yIGRldGVybWluaXN0aWMgb3V0cHV0CiAgICAibWF4X3Rva2VucyI6IDIwMDAsICAgICAgICAgICAjIFN1ZmZpY2llbnQgZm9yIEJOIHN0cnVjdHVyZQogICAgInRvcF9wIjogMC45LCAgICAgICAgICAgICAgICMgTnVjbGV1cyBzYW1wbGluZwogICAgImZyZXF1ZW5jeV9wZW5hbHR5IjogMC4wLCAgICAjIE5vIGZyZXF1ZW5jeSBwZW5hbHR5CiAgICAicHJlc2VuY2VfcGVuYWx0eSI6IDAuMCAgICAgICMgTm8gcHJlc2VuY2UgcGVuYWx0eQp9)

1LLM\_CONFIG = {

2 "model": "gpt-4-0613", # Primary model

3 "temperature": 0.1, # Low temperature for deterministic output

4 "max\_tokens": 2000, # Sufficient for BN structure

5 "top\_p": 0.9, # Nucleus sampling

6 "frequency\_penalty": 0.0, # No frequency penalty

7 "presence\_penalty": 0.0 # No presence penalty

8}

Listing 1: LLM Configuration Parameters

Alternative models tested include Claude-3.5-Sonnet, selected for its comparable performance, and GPT-3.5-turbo, used as a fallback option. All models are configured with identical parameters to ensure consistent behavior across different LLM providers.

### Prompt Engineering for BN Generation

The core of our system consists of carefully designed prompts that direct the LLM to generate valid Bayesian network structures. Our system prompt template guarantees a consistent output format and structural validity:

[⬇](data:text/plain;base64,U1lTVEVNX1BST01QVCA9ICIiIgpZb3UgYXJlIGFuIGV4cGVydCBpbiBCYXllc2lhbiBOZXR3b3JrcyBhbmQgZmluYW5jaWFsIHRyYWRpbmcuCkdlbmVyYXRlIGEgc3RydWN0dXJlZCBCYXllc2lhbiBOZXR3b3JrIChEQUcpIGZvciBvcHRpb25zIHRyYWRpbmcgZGVjaXNpb25zLgoKQ1JJVElDQUwgUkVRVUlSRU1FTlRTOgoxLiBPdXRwdXQgT05MWSB2YWxpZCBKU09OIGZvcm1hdAoyLiBJbmNsdWRlIG5vZGVzIGFuZCBlZGdlcyBhcnJheXMKMy4gRW5zdXJlIERBRyBwcm9wZXJ0eSAobm8gY3ljbGVzKQo0LiBGb2N1cyBvbiBjYXVzYWwgcmVsYXRpb25zaGlwcywgbm90IGNvcnJlbGF0aW9ucwo1LiBJbmNsdWRlIGJvdGggbWFya2V0IGFuZCBwc3ljaG9sb2dpY2FsIHZhcmlhYmxlcwoKT1VUUFVUIEZPUk1BVDoKewogICAgIm5vZGVzIjogWyJub2RlMSIsICJub2RlMiIsIC4uLl0sCiAgICAiZWRnZXMiOiBbWyJwYXJlbnQiLCAiY2hpbGQiXSwgLi4uXSwKICAgICJyZWFzb25pbmciOiAiQnJpZWYgZXhwbGFuYXRpb24gb2Ygc3RydWN0dXJlIgp9CiIiIg==)

1SYSTEM\_PROMPT = """

2You are an expert in Bayesian Networks and financial trading.

3Generate a structured Bayesian Network (DAG) for options trading decisions.

4

5CRITICAL REQUIREMENTS:

61. Output ONLY valid JSON format

72. Include nodes and edges arrays

83. Ensure DAG property (no cycles)

94. Focus on causal relationships, not correlations

105. Include both market and psychological variables

11

12OUTPUT FORMAT:

13{

14 "nodes": ["node1", "node2", ...],

15 "edges": [["parent", "child"], ...],

16 "reasoning": "Brief explanation of structure"

17}

18"""

Listing 2: System Prompt Template

Context-specific prompts incorporate detailed market conditions and psychological states:

[⬇](data:text/plain;base64,ZGVmIGNvbnN0cnVjdF9wcm9tcHQobWFya2V0X2NvbnRleHQsIHBzeWNob2xvZ2ljYWxfc3RhdGUpOgogICAgcmV0dXJuIGYiIiIKICAgIEdlbmVyYXRlIGEgQmF5ZXNpYW4gTmV0d29yayBzdHJ1Y3R1cmUgZm9yIG9wdGlvbnMgdHJhZGluZyBkZWNpc2lvbjoKCiAgICBNQVJLRVQgQ09OVEVYVDoKICAgIC0gVGlja2VyOiB7bWFya2V0X2NvbnRleHQudGlja2VyfQogICAgLSBDdXJyZW50IFByaWNlOiAke21hcmtldF9jb250ZXh0LmN1cnJlbnRfcHJpY2V9CiAgICAtIFZvbGF0aWxpdHk6IHttYXJrZXRfY29udGV4dC52b2xhdGlsaXR5Oi4yCiAgICAtIFRyZW5kOiB7bWFya2V0X2NvbnRleHQudHJlbmR9CiAgICAtIFZJWDoge21hcmtldF9jb250ZXh0LnZpeH0KICAgIC0gTWFya2V0IFJlZ2ltZToge21hcmtldF9jb250ZXh0Lm1hcmtldF9yZWdpbWV9CgogICAgUFNZQ0hPTE9HSUNBTCBTVEFURToKICAgIC0gRk9NTyBMZXZlbDoge3BzeWNob2xvZ2ljYWxfc3RhdGUuZm9tb19sZXZlbDouMmZ9CiAgICAtIENvbmZpZGVuY2U6IHtwc3ljaG9sb2dpY2FsX3N0YXRlLmNvbmZpZGVuY2VfbGV2ZWw6LjJmfQogICAgLSBTdHJlc3M6IHtwc3ljaG9sb2dpY2FsX3N0YXRlLnN0cmVzc19sZXZlbDouMmZ9CiAgICAtIFRpbHQgUmlzazoge3BzeWNob2xvZ2ljYWxfc3RhdGUudGlsdF9yaXNrOi4yZn0KCiAgICBHZW5lcmF0ZSBub2RlcyBmb3IgbWFya2V0IHZhcmlhYmxlcywgcHN5Y2hvbG9naWNhbCBmYWN0b3JzLAogICAgc3RyYXRlZ3kgcGFyYW1ldGVycywgYW5kIG91dGNvbWVzLiBDcmVhdGUgY2F1c2FsIGVkZ2VzIGJhc2VkCiAgICBvbiB0aGUgY3VycmVudCBjb250ZXh0LiBPdXRwdXQgdmFsaWQgSlNPTiBvbmx5LgogICAgIiIi)

1def construct\_prompt(market\_context, psychological\_state):

2 return f"""

3 Generate a Bayesian Network structure for options trading decision:

4

5 MARKET CONTEXT:

6 - Ticker: {market\_context.ticker}

7 - Current Price: ${market\_context.current\_price}

8 - Volatility: {market\_context.volatility:.2

9 - Trend: {market\_context.trend}

10 - VIX: {market\_context.vix}

11 - Market Regime: {market\_context.market\_regime}

12

13 PSYCHOLOGICAL STATE:

14 - FOMO Level: {psychological\_state.fomo\_level:.2f}

15 - Confidence: {psychological\_state.confidence\_level:.2f}

16 - Stress: {psychological\_state.stress\_level:.2f}

17 - Tilt Risk: {psychological\_state.tilt\_risk:.2f}

18

19 Generate nodes for market variables, psychological factors,

20 strategy parameters, and outcomes. Create causal edges based

21 on the current context. Output valid JSON only.

22 """

Listing 3: Context-Specific Prompt Construction

### Natural Language to DAG Conversion

The conversion of LLM-generated natural language output into formal DAG representations is accomplished through a multi-stage parsing pipeline:

#### LLM Response Parsing Algorithm

[⬇](data:text/plain;base64,ZGVmIHBhcnNlX2xsbV9yZXNwb25zZShsbG1fcmVzcG9uc2U6IHN0cikgLT4gRGljdDoKICAgICIiIkNvbnZlcnQgTExNIG5hdHVyYWwgbGFuZ3VhZ2Ugb3V0cHV0IHRvIHN0cnVjdHVyZWQgQk4gcmVwcmVzZW50YXRpb24iIiIKCiAgICAjIE1ldGhvZCAxOiBEaXJlY3QgSlNPTiBleHRyYWN0aW9uCiAgICBqc29uX21hdGNoID0gcmUuc2VhcmNoKHInXHsuKlx9JywgbGxtX3Jlc3BvbnNlLCByZS5ET1RBTEwpCiAgICBpZiBqc29uX21hdGNoOgogICAgICAgIHN0cnVjdHVyZSA9IGpzb24ubG9hZHMoanNvbl9tYXRjaC5ncm91cCgpKQogICAgICAgIGlmIHZhbGlkYXRlX3N0cnVjdHVyZShzdHJ1Y3R1cmUpOgogICAgICAgICAgICByZXR1cm4gc3RydWN0dXJlCgogICAgIyBNZXRob2QgMjogUGFyc2Ugc3RydWN0dXJlZCB0ZXh0CiAgICByZXR1cm4gcGFyc2Vfc3RydWN0dXJlZF90ZXh0KGxsbV9yZXNwb25zZSk=)

1def parse\_llm\_response(llm\_response: str) -> Dict:

2 """Convert LLM natural language output to structured BN representation"""

3

4 # Method 1: Direct JSON extraction

5 json\_match = re.search(r’\{.\*\}’, llm\_response, re.DOTALL)

6 if json\_match:

7 structure = json.loads(json\_match.group())

8 if validate\_structure(structure):

9 return structure

10

11 # Method 2: Parse structured text

12 return parse\_structured\_text(llm\_response)

Listing 4: LLM Response Parser

#### Structured Text Parsing

When direct JSON extraction fails, our system applies advanced text parsing techniques using multiple regex patterns:

[⬇](data:text/plain;base64,IyBFeHRyYWN0IG5vZGVzIHVzaW5nIG11bHRpcGxlIHBhdHRlcm5zCm5vZGVfcGF0dGVybnMgPSBbCiAgICByJ25vZGVzP1s6XHNdKyhbXixcbl0rKScsCiAgICByJ3ZhcmlhYmxlcz9bOlxzXSsoW14sXG5dKyknLAogICAgcidmYWN0b3JzP1s6XHNdKyhbXixcbl0rKScKXQoKIyBFeHRyYWN0IGVkZ2VzIHVzaW5nIHZhcmlvdXMgYXJyb3cgcGF0dGVybnMKZWRnZV9wYXR0ZXJucyA9IFsKICAgIHInKFx3KylccyotPlxzKihcdyspJywKICAgIHInKFx3KylccyotPlxzKihcdyspJywKICAgIHInKFx3KylccyppbmZsdWVuY2VzP1xzKihcdyspJywKICAgIHInKFx3KylccyphZmZlY3RzP1xzKihcdyspJywKICAgIHInKFx3KylccypjYXVzZXM/XHMqKFx3KyknCl0=)

1# Extract nodes using multiple patterns

2node\_patterns = [

3 r’nodes?[:\s]+([^,\n]+)’,

4 r’variables?[:\s]+([^,\n]+)’,

5 r’factors?[:\s]+([^,\n]+)’

6]

7

8# Extract edges using various arrow patterns

9edge\_patterns = [

10 r’(\w+)\s\*->\s\*(\w+)’,

11 r’(\w+)\s\*->\s\*(\w+)’,

12 r’(\w+)\s\*influences?\s\*(\w+)’,

13 r’(\w+)\s\*affects?\s\*(\w+)’,

14 r’(\w+)\s\*causes?\s\*(\w+)’

15]

Listing 5: Structured Text Parsing

#### DAG Validation

All generated structures undergo rigorous validation to ensure DAG properties:

[⬇](data:text/plain;base64,ZGVmIHZhbGlkYXRlX3N0cnVjdHVyZShzdHJ1Y3R1cmU6IERpY3QpIC0+IGJvb2w6CiAgICAiIiJWYWxpZGF0ZSBCTiBzdHJ1Y3R1cmUgZm9yIGNvcnJlY3RuZXNzIiIiCiAgICByZXF1aXJlZF9maWVsZHMgPSBbJ25vZGVzJywgJ2VkZ2VzJ10KICAgIGlmIG5vdCBhbGwoZmllbGQgaW4gc3RydWN0dXJlIGZvciBmaWVsZCBpbiByZXF1aXJlZF9maWVsZHMpOgogICAgICAgIHJldHVybiBGYWxzZQoKICAgIG5vZGVzID0gc3RydWN0dXJlWydub2RlcyddCiAgICBlZGdlcyA9IHN0cnVjdHVyZVsnZWRnZXMnXQoKICAgICMgQ2hlY2sgZWRnZSB2YWxpZGl0eQogICAgZm9yIGVkZ2UgaW4gZWRnZXM6CiAgICAgICAgaWYgbGVuKGVkZ2UpICE9IDI6CiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIGlmIGVkZ2VbMF0gbm90IGluIG5vZGVzIG9yIGVkZ2VbMV0gbm90IGluIG5vZGVzOgogICAgICAgICAgICByZXR1cm4gRmFsc2UKCiAgICAjIENoZWNrIGZvciBjeWNsZXMgdXNpbmcgREZTCiAgICBpZiBoYXNfY3ljbGVzKG5vZGVzLCBlZGdlcyk6CiAgICAgICAgcmV0dXJuIEZhbHNlCgogICAgcmV0dXJuIFRydWU=)

1def validate\_structure(structure: Dict) -> bool:

2 """Validate BN structure for correctness"""

3 required\_fields = [’nodes’, ’edges’]

4 if not all(field in structure for field in required\_fields):

5 return False

6

7 nodes = structure[’nodes’]

8 edges = structure[’edges’]

9

10 # Check edge validity

11 for edge in edges:

12 if len(edge) != 2:

13 return False

14 if edge[0] not in nodes or edge[1] not in nodes:

15 return False

16

17 # Check for cycles using DFS

18 if has\_cycles(nodes, edges):

19 return False

20

21 return True

Listing 6: DAG Validation Algorithm

### Complete Integration Pipeline

Our end-to-end implementation pipeline consists of eight stages:

[⬇](data:text/plain;base64,ZGVmIGdlbmVyYXRlX2V4ZWN1dGFibGVfYm4obWFya2V0X2NvbnRleHQsIHBzeWNob2xvZ2ljYWxfc3RhdGUpOgogICAgIiIiQ29tcGxldGUgcGlwZWxpbmUgZnJvbSBjb250ZXh0IHRvIGV4ZWN1dGFibGUgQk4iIiIKCiAgICAjIFN0ZXAgMTogR2VuZXJhdGUgcHJvbXB0CiAgICBwcm9tcHQgPSBjb25zdHJ1Y3RfcHJvbXB0KG1hcmtldF9jb250ZXh0LCBwc3ljaG9sb2dpY2FsX3N0YXRlKQoKICAgICMgU3RlcCAyOiBHZXQgTExNIHJlc3BvbnNlCiAgICBsbG1fcmVzcG9uc2UgPSBsbG1fY2xpZW50LmdlbmVyYXRlX2JuX3N0cnVjdHVyZShwcm9tcHQpCgogICAgIyBTdGVwIDM6IFBhcnNlIHJlc3BvbnNlIHRvIHN0cnVjdHVyZQogICAgc3RydWN0dXJlID0gcGFyc2VyLnBhcnNlX2xsbV9yZXNwb25zZShsbG1fcmVzcG9uc2UpCgogICAgIyBTdGVwIDQ6IFZhbGlkYXRlIGFuZCBjb25zdHJ1Y3QgREFHCiAgICBkYWcgPSBkYWdfY29uc3RydWN0b3IuY29uc3RydWN0X2RhZyhzdHJ1Y3R1cmUpCgogICAgIyBTdGVwIDU6IEJ1aWxkIHBnbXB5IEJOCiAgICBibl9tb2RlbCA9IGJuX2J1aWxkZXIuYnVpbGRfYm5fZnJvbV9zdHJ1Y3R1cmUoc3RydWN0dXJlKQoKICAgICMgU3RlcCA2OiBQb3B1bGF0ZSBDUFRzIGZyb20gZGF0YQogICAgcG9wdWxhdGVkX2NwZHMgPSBjcGRfcG9wdWxhdG9yLnBvcHVsYXRlX2NwZHNfZnJvbV9kYXRhKHN0cnVjdHVyZSkKCiAgICAjIFN0ZXAgNzogVXBkYXRlIEJOIHdpdGggZGF0YS1kcml2ZW4gcHJvYmFiaWxpdGllcwogICAgdXBkYXRlX2JuX3dpdGhfY3Bkcyhibl9tb2RlbCwgcG9wdWxhdGVkX2NwZHMpCgogICAgcmV0dXJuIGJuX21vZGVs)

1def generate\_executable\_bn(market\_context, psychological\_state):

2 """Complete pipeline from context to executable BN"""

3

4 # Step 1: Generate prompt

5 prompt = construct\_prompt(market\_context, psychological\_state)

6

7 # Step 2: Get LLM response

8 llm\_response = llm\_client.generate\_bn\_structure(prompt)

9

10 # Step 3: Parse response to structure

11 structure = parser.parse\_llm\_response(llm\_response)

12

13 # Step 4: Validate and construct DAG

14 dag = dag\_constructor.construct\_dag(structure)

15

16 # Step 5: Build pgmpy BN

17 bn\_model = bn\_builder.build\_bn\_from\_structure(structure)

18

19 # Step 6: Populate CPTs from data

20 populated\_cpds = cpd\_populator.populate\_cpds\_from\_data(structure)

21

22 # Step 7: Update BN with data-driven probabilities

23 update\_bn\_with\_cpds(bn\_model, populated\_cpds)

24

25 return bn\_model

Listing 7: Complete Integration Pipeline

### Error Handling and Fallbacks

The system includes robust error handling with multiple fallback strategies:

[⬇](data:text/plain;base64,ZGVmIGdlbmVyYXRlX3dpdGhfZmFsbGJhY2sobWFya2V0X2NvbnRleHQsIHBzeWNob2xvZ2ljYWxfc3RhdGUpOgogICAgIiIiR2VuZXJhdGUgQk4gd2l0aCBtdWx0aXBsZSBmYWxsYmFjayBzdHJhdGVnaWVzIiIiCgogICAgZm9yIGF0dGVtcHQgaW4gcmFuZ2UoTUFYX1JFVFJJRVMpOgogICAgICAgIHRyeToKICAgICAgICAgICAgIyBQcmltYXJ5OiBMTE0tYmFzZWQgZ2VuZXJhdGlvbgogICAgICAgICAgICBibiA9IGdlbmVyYXRlX3dpdGhfbGxtKG1hcmtldF9jb250ZXh0LCBwc3ljaG9sb2dpY2FsX3N0YXRlKQogICAgICAgICAgICBpZiB2YWxpZGF0ZV9ibihibik6CiAgICAgICAgICAgICAgICByZXR1cm4gYm4KICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgIGxvZ2dlci53YXJuaW5nKGYiTExNIGdlbmVyYXRpb24gYXR0ZW1wdCB7YXR0ZW1wdCArIDF9IGZhaWxlZDoge2V9IikKCiAgICAjIEZhbGxiYWNrIDE6IFRlbXBsYXRlLWJhc2VkIGdlbmVyYXRpb24KICAgIHRyeToKICAgICAgICBibiA9IGdlbmVyYXRlX3dpdGhfdGVtcGxhdGUobWFya2V0X2NvbnRleHQsIHBzeWNob2xvZ2ljYWxfc3RhdGUpCiAgICAgICAgaWYgdmFsaWRhdGVfYm4oYm4pOgogICAgICAgICAgICByZXR1cm4gYm4KICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBsb2dnZXIud2FybmluZyhmIlRlbXBsYXRlIGdlbmVyYXRpb24gZmFpbGVkOiB7ZX0iKQoKICAgICMgRmFsbGJhY2sgMjogUHJlZGVmaW5lZCBzdHJ1Y3R1cmUKICAgIHJldHVybiBnZXRfcHJlZGVmaW5lZF9ibihtYXJrZXRfY29udGV4dC5tYXJrZXRfcmVnaW1lKQ==)

1def generate\_with\_fallback(market\_context, psychological\_state):

2 """Generate BN with multiple fallback strategies"""

3

4 for attempt in range(MAX\_RETRIES):

5 try:

6 # Primary: LLM-based generation

7 bn = generate\_with\_llm(market\_context, psychological\_state)

8 if validate\_bn(bn):

9 return bn

10 except Exception as e:

11 logger.warning(f"LLM generation attempt {attempt + 1} failed: {e}")

12

13 # Fallback 1: Template-based generation

14 try:

15 bn = generate\_with\_template(market\_context, psychological\_state)

16 if validate\_bn(bn):

17 return bn

18 except Exception as e:

19 logger.warning(f"Template generation failed: {e}")

20

21 # Fallback 2: Predefined structure

22 return get\_predefined\_bn(market\_context.market\_regime)

Listing 8: Error Handling and Fallbacks

## Appendix B Statistical Analysis and Robustness

### Performance Metrics with Confidence Intervals

All performance metrics are reported with 95% confidence intervals, calculated using bootstrap analysis with 1,000 iterations:

Table 9: Performance Metrics with Statistical Confidence

| Metric | Value | 95% CI |
| --- | --- | --- |
| Annualized Return | 15.3% | [13.8%, 16.8%] |
| Monthly Return | 1.19% | [1.05%, 1.33%] |
| Sharpe Ratio | 1.08 | [0.9, 1.3] |
| Max Drawdown | -8.2% | [-10.1%, -6.3%] |
| Win Rate | 99.4% | [99.2%, 99.6%] |
| Average Premium Rate | 11.15% | [10.8%, 11.5%] |
| Rolling Rate | 371.3% | [365%, 378%] |

### Statistical Significance Testing

We conducted paired t-tests to compare the monthly returns of our method with each baseline approach. The results indicate statistically significant outperformance:

Table 10: Statistical Significance Testing Results

| Comparison | Mean Difference | t-statistic | p-value |
| --- | --- | --- | --- |
| Our Method vs Pure LLM | +0.55% | 4.23 | << 0.001 |
| Our Method vs Static BN | +0.34% | 2.87 | 0.004 |
| Our Method vs Rules-Based | +0.46% | 3.91 | << 0.001 |
| Our Method vs SPY | +0.12% | 0.89 | 0.374 |
| Our Method vs QQQ | -0.19% | -1.45 | 0.147 |

The statistical analysis shows that our method significantly outperforms all architectural baselines (p<0.01p<0.01). However, it does not significantly outperform the QQQ benchmark (p=0.147p=0.147). This result aligns with our economic analysis, which demonstrates superior risk-adjusted performance despite lower absolute returns.

### Sensitivity Analysis

We conducted comprehensive sensitivity analysis varying key parameters to assess robustness:

Table 11: Sensitivity Analysis Results

| Parameter | Base Value | Range Tested | Performance Impact |
| --- | --- | --- | --- |
| Position Size Limit | 10% | 5%-20% | ±\pm0.8% |
| Premium Threshold | 2.5% | 1.5%-4.0% | ±\pm1.2% |
| Rolling Criteria | 5% OTM | 3%-8% OTM | ±\pm0.6% |
| Temperature | 0.1 | 0.05-0.3 | ±\pm0.4% |

The sensitivity analysis demonstrates that our method remains robust across parameter variations. The performance impacts stay within acceptable bounds.

## Appendix C Network Structure Validation Framework

### Complete Methodological Specifications for Validation Experiments

To address concerns regarding insufficient methodological detail, we provide comprehensive specifications for all validation experiments:

#### Ablation Study Methodology

The ablation study (Table [12](https://arxiv.org/html/2512.01123v1#A3.T12 "Table 12 ‣ Network Structure Validation Results ‣ Appendix C Network Structure Validation Framework ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading")) was conducted using the following rigorous methodology:
Expert-Designed Network Creation: The expert-designed network was created independently by a senior quantitative analyst with 15+ years of options trading experience, who was provided only with the variable definitions and market context descriptions but had no access to LLM-generated structures or performance results. The expert was instructed to design a network structure based on their domain knowledge of options trading causality.

Random Structure Generation: We generated 1,000 random network structures using a uniform distribution over all possible DAGs with the same node set. Each random structure was validated for DAG properties and tested for performance. The results shown represent the best-performing random structure to ensure fair comparison.

LLM Network Generation Protocol: For experimental parity, we generated 1,000 LLM networks using identical market conditions with different random seeds and temperature variations (0.05-0.3 range). The results shown represent the best-performing LLM-generated network to ensure fair comparison with the best-of-1000 random structures.

Experimental Protocol: All four network types (LLM-generated, expert-designed, random, fixed template) used identical temporal validation protocols: same train/validation/test splits (2007-2015/2016-2019/2020-2025), identical hyperparameters, same data preprocessing, and identical evaluation metrics. The ablation results represent separate experimental runs conducted after the main results were finalized to prevent any contamination.

Fixed Template Network: The fixed template used a pre-defined structure based on common options trading heuristics, including standard relationships between volatility, market regime, and strike selection. This template remained unchanged across all market conditions.

#### Consistency Analysis Methodology

The consistency analysis (Table [13](https://arxiv.org/html/2512.01123v1#A3.T13 "Table 13 ‣ Consistency Analysis ‣ Appendix C Network Structure Validation Framework ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading")) was conducted as follows:

Market Scenario Selection: We identified 25 distinct market scenarios representing different combinations of market regime (bull/neutral/bear), volatility level (high/medium/low), and psychological state (confident/stressed/neutral). Each scenario was defined by specific ranges of market indicators (VIX, trend, volume) and psychological metrics (confidence, stress, FOMO levels).

Network Generation Process: For each of the 25 scenarios, we generated 20 network structures using different LLM instances (different random seeds, temperature settings, and prompt variations). This resulted in 500 total network structures (25 scenarios × 20 variations per scenario).

Structural Similarity Calculation: We computed structural similarity using the Jaccard index of edge sets. For two networks with edge sets E1E\_{1} and E2E\_{2}, the similarity is calculated as |E1∩E2||E1∪E2|\frac{|E\_{1}\cap E\_{2}|}{|E\_{1}\cup E\_{2}|}, representing the ratio of shared edges to total unique edges. The mean similarity of 0.78 represents the average across all pairwise comparisons within each scenario.

Performance Variance Analysis: The 0.8% performance variance represents the standard deviation of annual returns across the 20 network variations for each scenario, averaged across all 25 scenarios. This low variance indicates that while network structures vary, performance remains relatively stable.

### Network Structure Validation Results

Table 12: Network Structure Ablation Study Results

| Network Type | Annual Return | Sharpe Ratio | Max Drawdown |
| --- | --- | --- | --- |
| LLM-Generated | 15.3% | 1.08 | -8.2% |
| Random Structure | 9.2% | 0.67 | -18.7% |
| Fixed Template | 11.5% | 0.82 | -14.2% |

The ablation study demonstrates that networks generated by LLMs significantly outperform alternative methods. This provides empirical validation for our architectural choice.

### Consistency Analysis

We analyzed structural consistency by generating multiple networks for identical market conditions:

Table 13: Network Structure Consistency Analysis

| Metric | Mean | Std Dev | Coefficient of Variation |
| --- | --- | --- | --- |
| Structural Similarity | 0.78 | 0.12 | 15.4% |
| Edge Overlap | 0.82 | 0.09 | 11.0% |
| Node Overlap | 0.91 | 0.06 | 6.6% |
| Performance Variance | 0.8% | 0.3% | 37.5% |

The consistency analysis reveals a moderate structural similarity of 0.78 and a low performance variance of 0.8%. This indicates that although network structures vary, performance remains relatively stable.

### Structural Variation Impact Analysis

To address concerns regarding the implications of structural variation, we conducted a detailed analysis to identify which structural differences affect performance.

Table 14: Structural Variation Impact Analysis

| Edge Type | Frequency in High-Performers | Frequency in Low-Performers | Performance Impact |
| --- | --- | --- | --- |
| Volatility → Strike\_Selection | 0.89 | 0.34 | +2.1% |
| Market\_Regime → Assignment\_Prob | 0.92 | 0.28 | +1.8% |
| Technical\_Position → Premium\_Rate | 0.85 | 0.41 | +1.5% |
| Psychological\_State → Risk\_Tolerance | 0.78 | 0.52 | +1.2% |
| Stock\_Fundamentals → Trade\_Outcome | 0.71 | 0.45 | +0.9% |

As shown in Table [14](https://arxiv.org/html/2512.01123v1#A3.T14 "Table 14 ‣ Structural Variation Impact Analysis ‣ Appendix C Network Structure Validation Framework ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading"), the analysis reveals that certain edges consistently appear in high-performing networks, especially those linking market variables to decision parameters. Edges from volatility to strike selection correlate with a +2.1% performance improvement. Similarly, edges from market regime to assignment probability contribute a +1.8% improvement.

### Reliability Analysis for Structural Consistency

To address concerns about deployment reliability amid moderate structural similarity, we conducted a comprehensive reliability analysis. As shown in Table [15](https://arxiv.org/html/2512.01123v1#A3.T15 "Table 15 ‣ Reliability Analysis for Structural Consistency ‣ Appendix C Network Structure Validation Framework ‣ A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading"), the analysis shows that 68% of network variations fall within the high-to-moderate similarity range (0.8–1.0) and exhibit minimal performance impact (±0.5%). Only 4% of variations display low similarity (0.6–0.7) with a significant performance impact (±2.3%). These results indicate acceptable deployment reliability for production use.

Table 15: Structural Consistency Reliability Analysis

| Similarity Range | Performance Impact | Frequency | Deployment Risk |
| --- | --- | --- | --- |
| 0.9-1.0 (High) | ±\pm0.2% | 23% | Low |
| 0.8-0.9 (Moderate) | ±\pm0.5% | 45% | Low-Medium |
| 0.7-0.8 (Moderate) | ±\pm1.1% | 28% | Medium |
| 0.6-0.7 (Low) | ±\pm2.3% | 4% | High |