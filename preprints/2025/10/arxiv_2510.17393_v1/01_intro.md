---
authors:
- Kefan Chen
- Hussain Ahmad
- Diksha Goel
- Claudia Szabo
doc_id: arxiv:2510.17393v1
family_id: arxiv:2510.17393
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and
  Selection in Portfolio Optimization'
url_abs: http://arxiv.org/abs/2510.17393v1
url_html: https://arxiv.org/html/2510.17393v1
venue: arXiv q-fin
version: 1
year: 2025
---


Kefan Chen
The University of Adelaide, Australia
[kefan.chen@student.adelaide.edu.au](mailto:kefan.chen@student.adelaide.edu.au)
, 
Hussain Ahmad
The University of Adelaide, Australia
[hussain.ahmad@adelaide.edu.au](mailto:hussain.ahmad@adelaide.edu.au)
, 
Diksha Goel
CSIRO’s Data61, Australia
[diksha.goel@csiro.au](mailto:diksha.goel@csiro.au)
 and 
Claudia Szabo
The University of Adelaide, Australia
[claudia.szabo@adelaide.edu.au](mailto:claudia.szabo@adelaide.edu.au)

(2025)

###### Abstract.

Large Language Models (LLMs) have recently gained popularity in stock trading for their ability to process multimodal financial data. However, most existing methods focus on single-stock trading and lack the capacity to reason over multiple candidates for portfolio construction. Moreover, they typically lack the flexibility to revise their strategies in response to market shifts, limiting their adaptability in real-world trading. To address these challenges, we propose 3S-Trader, a training-free framework that incorporates scoring, strategy, and selection modules for stock portfolio construction. The scoring module summarizes each stock’s recent signals into a concise report covering multiple scoring dimensions, enabling efficient comparison across candidates. The strategy module analyzes historical strategies and overall market conditions to iteratively generate an optimized selection strategy. Based on this strategy, the selection module identifies and assembles a portfolio by choosing stocks with higher scores in relevant dimensions. We evaluate our framework across four distinct stock universes, including the Dow Jones Industrial Average (DJIA) constituents and three sector-specific stock sets. Compared with existing multi-LLM frameworks and time-series-based baselines, 3S-Trader achieves the highest accumulated return of 131.83% on DJIA constituents with a Sharpe ratio of 0.31 and Calmar ratio of 11.84, while also delivering consistently strong results across other sectors.

Stock Trading, Portfolio Management, Large Language Models, Self-Reflective Framework, Explainable AI

††copyright: acmlicensed††journalyear: 2025††doi: 10.1145/XXXXXXX.XXXXXXX††isbn: 978-1-4503-XXXX-X/25/11††ccs: Applied computing Economics††ccs: Computing methodologies Natural language processing
![Refer to caption](pipeline.drawio.png)


Figure 1. 3S-Trader Framework.††:

## 1. Introduction

In the stock market, a portfolio refers to the structured allocation of various stock assets (Markowitz, [1952](https://arxiv.org/html/2510.17393v1#bib.bib35); Fabozzi et al., [2007](https://arxiv.org/html/2510.17393v1#bib.bib19)), carefully selected to achieve specific investment objectives. Compared to single-stock trading, portfolio-based strategies diversify exposure across multiple assets, mitigating the impact of individual stock volatility (Statman, [1987](https://arxiv.org/html/2510.17393v1#bib.bib42)). Constructing an effective portfolio requires analyzing diverse sources of market information, such as price trends, company fundamentals, and macroeconomic signals, to identify the most valuable assets for investment allocation (Connor, [2000](https://arxiv.org/html/2510.17393v1#bib.bib17); Liu et al., [2023](https://arxiv.org/html/2510.17393v1#bib.bib33)). However, this task becomes increasingly challenging as the number of candidate stocks grows, especially when dealing with large volumes of heterogeneous, multi-modal data that must be processed and compared in a coherent manner (Ozbayoglu et al., [2020](https://arxiv.org/html/2510.17393v1#bib.bib40); Kim et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib30)).

With the rapid advancements in AI, particularly LLMs (Haque et al., [2022](https://arxiv.org/html/2510.17393v1#bib.bib26); Ahmad and Goel, [2025](https://arxiv.org/html/2510.17393v1#bib.bib4)), across domains such as cybersecurity (Chopra et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib16); Ahmad et al., [2025c](https://arxiv.org/html/2510.17393v1#bib.bib8); Ullah et al., [2025](https://arxiv.org/html/2510.17393v1#bib.bib43); Goel et al., [2025](https://arxiv.org/html/2510.17393v1#bib.bib23)), software engineering (Goel et al., [2024a](https://arxiv.org/html/2510.17393v1#bib.bib22); Abdulsatar et al., [2025](https://arxiv.org/html/2510.17393v1#bib.bib2)), and cloud computing (Ahmad et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib5), [2025b](https://arxiv.org/html/2510.17393v1#bib.bib7), [2025a](https://arxiv.org/html/2510.17393v1#bib.bib6); Jayalath et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib28)), the technology has also demonstrated significant benefits in the financial sector (Zhang et al., [2025](https://arxiv.org/html/2510.17393v1#bib.bib46)). Equipped with powerful natural language understanding and reasoning capabilities (Brown et al., [2020](https://arxiv.org/html/2510.17393v1#bib.bib15); Achiam et al., [2023](https://arxiv.org/html/2510.17393v1#bib.bib3); Bommasani et al., [2021](https://arxiv.org/html/2510.17393v1#bib.bib12)), LLMs can analyze and summarize both financial texts (Ahmed et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib9)) and indicators in a way similar to that of human experts and incorporate this information into their trading strategies (Kim et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib30); Liu et al., [2023](https://arxiv.org/html/2510.17393v1#bib.bib33)). While the mainstream applications of LLMs in finance have primarily focused on single-stock operations, including price prediction, trend classification (up or down), and position adjustment (Gu et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib25)). Although such applications can offer useful signals, they are often insufficient for guiding actual stock selection for portfolio management. For instance, a model may predict high returns for a particular stock, but fail to account for associated volatility, making it a less desirable choice in practice. Similarly, strategies that recommend buying or selling individual stocks are not capable of allocating capital across multiple stocks. Furthermore, conventional trading models struggle to learn from past behavior and adapt their strategies accordingly. While reinforcement learning (RL) offers a way to guide output optimization (Jiang et al., [2017](https://arxiv.org/html/2510.17393v1#bib.bib29)), it often incurs substantial training costs and heavily relies on carefully crafted reward functions (Mortaji et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib37); Deng et al., [2016](https://arxiv.org/html/2510.17393v1#bib.bib18)). However, due to the highly volatile nature of financial markets, it becomes challenging for RL-based models to learn robust and generalizable strategies (Goel et al., [2024b](https://arxiv.org/html/2510.17393v1#bib.bib24); Goel, [2023](https://arxiv.org/html/2510.17393v1#bib.bib21)).

To tackle the challenges outlined above, we propose 3S-Trader, a training-free framework capable of constructing portfolios directly from candidate stocks’ recent market signals. Moreover, it can iteratively refine its selection strategy by reflecting on past trading decisions, as illustrated in Figure [1](https://arxiv.org/html/2510.17393v1#acmlabel1 "Figure 1 ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization").
The framework consists of four main stages. First, in the Data Analysis stage, three specialized LLM-based agents, the News Agent, Fundamental Agent, and Technical Agent, analyze recent market news, company fundamentals, and technical indicators for each stock to generate textual summaries. Next, the Score Agent evaluates each stock along multiple scoring dimensions such as growth potential, volatility risk, and news sentiment, producing stock-level scoring reports. Based on these reports and the current selection strategy (e.g., favoring financially healthy and low-volatility stocks), the Selector Agent selects a subset of stocks and allocates weights to construct the portfolio. Finally, after each trading round, the Strategy Agent analyzes the relationship between candidate scores and their realized returns to identify which types of stocks the market favors, and adjusts its strategy accordingly. Our major contributions are summarized as follows:

* •

  We propose a training-free and easily deployable trading framework that directly constructs stock portfolios based on recent market information.
* •

  We enhance traditional LLM-based trading pipelines by coupling strategy refinement with multi-dimensional scoring, thereby offering trading strategies a clear adjustment direction, without the need for supervision or rewards.
* •

  We demonstrate the effectiveness and generality of our framework through experiments on stocks from multiple industry sectors, showing its practical value for real-world investment scenarios.

## 2. Related Work

Time-Series Models for Stock Prediction.
A common paradigm in traditional quantitative finance is to model stock trading as a time series forecasting problem. Auto-regressive models such as ARIMA and GARCH(Box and Jenkins, [1990](https://arxiv.org/html/2510.17393v1#bib.bib14); Bollerslev, [1986](https://arxiv.org/html/2510.17393v1#bib.bib11)) are widely adopted for modeling short-term trends and volatility in stock prices. More recently, deep learning techniques have been introduced to model complex temporal dependencies. Long Short-Term Memory (LSTM) networks and Temporal Convolutional Networks (TCNs) have shown promising results in capturing sequential patterns in financial time series (Fischer and Krauss, [2018](https://arxiv.org/html/2510.17393v1#bib.bib20); Borovykh et al., [2017](https://arxiv.org/html/2510.17393v1#bib.bib13)). Transformer-based models like Informer and Stockformer further improve long-range forecasting ability by leveraging attention mechanisms (Zhou et al., [2021](https://arxiv.org/html/2510.17393v1#bib.bib48); Muhammad et al., [2023](https://arxiv.org/html/2510.17393v1#bib.bib38)). While these models achieve promising results in forecasting, they primarily focus on price predictions. As a result, they often overlook portfolio-level considerations such as risk control and cross-asset comparison.

Multi-LLM Framework for Investment Guidance.
LLMs have been proposed to leverage their text processing capabilities in financial tasks such as sentiment analysis, financial question answering, and trend prediction. (Araci, [2019](https://arxiv.org/html/2510.17393v1#bib.bib10); Srivastava et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib41); Koa et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib31)). To achieve a complete pipeline covering the process from information processing to decision generation, frameworks that integrate LLMs with distinct functionalities have been proposed. We categorize these frameworks into two types: Single-Step and Reflective. The Single-Step framework typically aggregates and restructures financial texts over a given period, after which one or more agents summarize the information. A designated output agent then directly relies on this summarized text to generate trading guidance (Zhang et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib45); Zhao et al., [2023](https://arxiv.org/html/2510.17393v1#bib.bib47); Liu et al., [2023](https://arxiv.org/html/2510.17393v1#bib.bib33)). Extending this design, the Reflective framework introduces an additional agent to analyze the model’s recent behavior. The analysis is subsequently fed into the next trading cycle, thereby guiding its decision-making process (Li et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib32); Liu et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib34)).

Building on these works, we upgrade the multi-LLM framework by introducing a multi-dimensional scoring mechanism that simplifies summarized information and enables effective cross-stock comparison. Furthermore, by recording historical strategy trajectories and analyzing the relationship between scores and returns, our framework provides more interpretable and iterative strategy refinement.

## 3. Preliminaries

### 3.1. Problem Formulation

We consider a weekly stock portfolio construction problem. At the beginning of each week tt, a set of stocks 𝒳={x1,x2,…,xn}\mathcal{X}=\{x\_{1},x\_{2},\dots,x\_{n}\} is available for selection. The goal is to construct a portfolio 𝐰t=[wt(1),wt(2),…,wt(n)]⊤\mathbf{w}\_{t}=[w\_{t}^{(1)},w\_{t}^{(2)},\dots,w\_{t}^{(n)}]^{\top}, where wt(i)∈[0,1]w\_{t}^{(i)}\in[0,1] denotes the proportion of capital allocated to stock xix\_{i}. To allow for holding cash, we impose the constraint ∑i=1nwt(i)≤1\sum\_{i=1}^{n}w\_{t}^{(i)}\leq 1.

Trades are executed in the following manner: on the first trading day of week tt, capital is allocated to selected stocks according to 𝐰t\mathbf{w}\_{t} at the opening price; all positions are then liquidated at the closing price on the last trading day of the same week. For each stock xi∈𝒳x\_{i}\in\mathcal{X}, the weekly return rt(i)r\_{t}^{(i)} is calculated as rt(i)=(psell(i)−pbuy(i))/pbuy(i)r\_{t}^{(i)}=(p\_{\text{sell}}^{(i)}-p\_{\text{buy}}^{(i)})/p\_{\text{buy}}^{(i)}, where pbuy(i)p\_{\text{buy}}^{(i)} and psell(i)p\_{\text{sell}}^{(i)} denote the buy and sell prices of stock xix\_{i} in week tt, respectively. Given the return vector 𝐫t=[rt(1),rt(2),…,rt(n)]⊤\mathbf{r}\_{t}=[r\_{t}^{(1)},r\_{t}^{(2)},\dots,r\_{t}^{(n)}]^{\top}, the total portfolio return is computed as Rt=𝐰t⊤​𝐫tR\_{t}=\mathbf{w}\_{t}^{\top}\mathbf{r}\_{t}.

### 3.2. Data Collection

We collect three types of data for each stock: stock price and technical indicators, firm fundamentals, and market news. In this subsection, we describe how each type of data is processed for the portfolio construction task at week tt.

#### 3.2.1. Price and Technical Indicators

The raw price data consists of daily stock prices and trading volume. Based on these time series, we compute several technical indicators, including SMA, ATR, RSI, MACD, and Bollinger Bands. These indicators are commonly used in financial technical analysis (Murphy, [1999](https://arxiv.org/html/2510.17393v1#bib.bib39); Mebane, [2019](https://arxiv.org/html/2510.17393v1#bib.bib36)).

At week tt, we extract the daily closing prices Pricei,d\text{Price}\_{i,d} and technical indicators Indicatorsi,d\text{Indicators}\_{i,d} for stock xix\_{i} over the preceding four calendar weeks 𝒲t−4:t−1\mathcal{W}\_{t-4:t-1}, where dd indexes the days within that range. These values are concatenated into a plain text techi,t\text{tech}\_{i,t}, denoted as the technical input of stock xix\_{i} for week tt:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | techi,t=ConcatText​({Pricei,d,Indicatorsi,d∣d∈𝒲t−4:t−1})\text{tech}\_{i,t}=\text{ConcatText}(\{\text{Price}\_{i,d},\text{Indicators}\_{i,d}\mid d\in\mathcal{W}\_{t-4:t-1}\}) |  |

#### 3.2.2. Market News

The raw news data includes article titles, summaries, and their associated stock symbols. At week tt, we collect all news items related to stock xix\_{i} from the previous week. Similar to Equation ([1](https://arxiv.org/html/2510.17393v1#S3.E1 "In 3.2.1. Price and Technical Indicators ‣ 3.2. Data Collection ‣ 3. Preliminaries ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization")), we define the news input as:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | newsi,t=ConcatText​({RawNewsi,d∣d∈𝒲t−1})\text{news}\_{i,t}=\text{ConcatText}(\{\text{RawNews}\_{i,d}\mid d\in\mathcal{W}\_{t-1}\}) |  |

Here, RawNewsi,d\text{RawNews}\_{i,d} denotes the news content related to stock xix\_{i} published on day dd, and 𝒲t−1\mathcal{W}\_{t-1} represents the calendar week immediately preceding week tt.

#### 3.2.3. Firm Fundamentals

The fundamental data consists of firm-specific earnings reports, balance sheets, and cash flow statements, which are updated on a quarterly basis. To enable trend analysis, we concatenate the fundamental records from the four most recent fiscal quarters released before week tt. The resulting text serves as the fundamental input of stock xix\_{i} at week tt, denoted as:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | fundi,t=ConcatText​({RawFundi,q∣q∈𝒬tq−3:tq})\text{fund}\_{i,t}=\text{ConcatText}(\{\text{RawFund}\_{i,q}\mid q\in\mathcal{Q}\_{t\_{q}-3:t\_{q}}\}) |  |

Here, RawFundi,q\text{RawFund}\_{i,q} represents the fundamental data of stock xix\_{i} reported in fiscal quarter qq, and 𝒬tq−3:tq\mathcal{Q}\_{t\_{q}-3:t\_{q}} refers to the four most recent quarters available before week tt.

## 4. Methodology

In this section, we introduce the architecture of our proposed framework, 3S-Trader. As shown in Figure [1](https://arxiv.org/html/2510.17393v1#acmlabel1 "Figure 1 ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization"), the overall workflow is structured into four main steps. The framework incorporates six LLM-based agents that collaborate across these steps to support adaptive portfolio management. We implement all LLM-based agents using GPT-4o111<https://openai.com/gpt-4o>. In the following subsections, we detail each step and explain how the agents interact to process information, refine strategies, and make investment decisions.

### 4.1. Market Analysis

In this part, we leverage three specialized agents: News Agent, Fundamental Agent, and Technical Agent, to analyze different types of input data. Specifically, at week tt, for each stock xix\_{i}, based on its aggregated news text newsi,t\text{news}\_{i,t} defined in Equation ([2](https://arxiv.org/html/2510.17393v1#S3.E2 "In 3.2.2. Market News ‣ 3.2. Data Collection ‣ 3. Preliminaries ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization")), the News Agent generates an analysis report αi,tnews\alpha^{\text{news}}\_{i,t} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | αi,tnews=agentnews​(newsi,t,promptnews)\alpha^{\text{news}}\_{i,t}=\text{agent}\_{\text{news}}(\text{news}\_{i,t},\text{prompt}\_{\text{news}}) |  |

Similarly, we obtain αi,ttech\alpha^{\text{tech}}\_{i,t} and αi,tfund\alpha^{\text{fund}}\_{i,t} from the Technical Agent and Fundamental Agent, respectively, using corresponding inputs and prompts. These outputs are then concatenated to form the full data overview of stock xix\_{i} at week tt, denoted as oi,to\_{i,t}:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | oi,t=ConcatText​(αi,tnews,αi,ttech,αi,tfund)o\_{i,t}=\text{ConcatText}(\alpha^{\text{news}}\_{i,t},\alpha^{\text{tech}}\_{i,t},\alpha^{\text{fund}}\_{i,t}) |  |

Example prompts used by the corresponding agents are illustrated in Figure [2](https://arxiv.org/html/2510.17393v1#S4.F2 "Figure 2 ‣ 4.1. Market Analysis ‣ 4. Methodology ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization").

![Refer to caption](prompts_analysis.png)


Figure 2. Example prompts used by News Agent, Technical Agent, and Fundamental Agent for market analysis.

### 4.2. Stock Scoring

In this part, the Score Agent performs multi-dimensional scoring based on each stock’s recent market signals. It is instructed to assign a score from 1 to 10 for each dimension, reflecting the stock’s relative strength in that aspect.

In designing the scoring dimensions, we focused on their relevance to the available input data. To ensure that each dimension is grounded in observable evidence, we derive them directly from three primary sources: stock price movements, firm fundamentals, and market news. Based on these, we define the following six dimensions:

* •

  Financial Health: Evaluates a company’s current financial stability. A higher score reflects stronger fundamentals and lower short-term risk.
* •

  Growth Potential: Assesses the company’s future expansion capacity based on investment plans, and industry growth outlook. A higher score suggests stronger long-term earnings potential.
* •

  News Sentiment: Reflects overall sentiment polarity extracted from recent news articles. A higher score implies more positive news coverage and investor perception.
* •

  News Impact: Assesses the breadth and duration of news influence. Higher scores reflect more sustained impacts, e.g., from political events or industry-level shifts.
* •

  Price Momentum: Captures recent upward or downward trends in stock price movement. A higher score reflects a stronger and more consistent upward price trend.
* •

  Volatility Risk: Quantifies the level of recent price fluctuations, indicating risk exposure. A higher score represents higher volatility and less stable price behavior.

For stock selection at week tt, we first obtain the data overview oi,to\_{i,t} for stock xix\_{i} as defined in Equation ([5](https://arxiv.org/html/2510.17393v1#S4.E5 "In 4.1. Market Analysis ‣ 4. Methodology ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization")). This overview is then processed by the Score Agent to produce a textual scoring result, denoted as si,ts\_{i,t}. This scoring process can be formalized as:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | si,t=agentscore​(oi,t,promptscore)s\_{i,t}=\text{agent}\_{\text{score}}(o\_{i,t},\text{prompt}\_{\text{score}}) |  |

An example prompt used by the Score Agent is illustrated in Figure [3](https://arxiv.org/html/2510.17393v1#S4.F3 "Figure 3 ‣ 4.2. Stock Scoring ‣ 4. Methodology ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization").

![Refer to caption](prompt_score.png)


Figure 3. Example prompt used by the Score Agent for stock scoring.

### 4.3. Stock Selection

In this part, the Selector Agent constructs the final portfolio based on two key inputs: the scoring results of all candidate stocks produced by the Score Agent, and the selection strategy provided by the Strategy Agent. For clarity, we will introduce the Strategy Agent later. Here, it suffices to note that the strategy is a textual description πt\pi\_{t} that specifies which types of stocks should be preferred, guiding the Selector Agent to prioritize stocks with higher scores in the relevant dimensions. For example, a strategy πt\pi\_{t} might be:

Increase emphasis on financial health and reduce exposure to high-volatility stocks, as recent returns indicate stronger performance from fundamentally stable companies.

The Selector Agent is tasked with selecting up to five stocks and assigning weights, allowing cash holding to avoid market downturns. Hence, the total portfolio weight may be less than 1. For the portfolio construction task at week tt, the agent receives the scores si,ts\_{i,t} for all candidate stocks xi∈𝒳x\_{i}\in\mathcal{X}, along with the strategy πt\pi\_{t}. The resulting portfolio can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | 𝐰t=agentselect​(ConcatText​({si,t}i=1n),πt,promptselect)\mathbf{w}\_{t}=\text{agent}\_{\text{select}}(\text{ConcatText}(\{s\_{i,t}\}\_{i=1}^{n}),\pi\_{t},\text{prompt}\_{\text{select}}) |  |

where 𝐰t=[wt(1),wt(2),…,wt(n)]⊤\mathbf{w}\_{t}=[w\_{t}^{(1)},w\_{t}^{(2)},\dots,w\_{t}^{(n)}]^{\top} is the portfolio weight vector, with ∑i=1nwt(i)≤1\sum\_{i=1}^{n}w\_{t}^{(i)}\leq 1, and at most 5 elements of 𝐰t\mathbf{w}\_{t} are nonzero. An example prompt used by the Selector Agent is illustrated in Figure [4](https://arxiv.org/html/2510.17393v1#S4.F4 "Figure 4 ‣ 4.3. Stock Selection ‣ 4. Methodology ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization").

![Refer to caption](prompt_selector.png)


Figure 4. Example prompt used by the Selector Agent for stock selection.

### 4.4. Strategy Iteration

In this part, the Strategy Agent refines the current strategy based on the realized price changes of each stock and the historical trajectory of past strategies.

At the end of week tt, following the trading rule defined in Section [3.1](https://arxiv.org/html/2510.17393v1#S3.SS1 "3.1. Problem Formulation ‣ 3. Preliminaries ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization"), we obtain the realized return rt(i)r\_{t}^{(i)} for each stock xix\_{i}. To support strategic refinement, the Strategy Agent receives the realized returns rt(i)r\_{t}^{(i)} of all candidate stocks and their corresponding scoring reports si,ts\_{i,t}. It is tasked with identifying shared characteristics among high- and low-performing stocks, and proposing updated strategies.

To ensure a stable and coherent strategy iteration process, we introduce the trajectory of past strategy updates into the input of the Strategy Agent. This design aims to prevent divergence from previously effective strategies, reduce unnecessary fluctuations in decision-making, and help the agent identify patterns that are indicative of long-term stable returns. The historical trajectory is denoted as:

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | ℋ​t={ConcatText​(πt−k,Rt−kavg,Rt−k)}k=1K\mathcal{H}t=\left\{\text{ConcatText}\left(\pi\_{t-k},R\_{t-k}^{\text{avg}},R\_{t-k}\right)\right\}\_{k=1}^{K} |  |

where πt−k\pi\_{t-k} denotes the strategy adopted in week t−kt-k,
Rt−kavgR\_{t-k}^{\text{avg}} is the universe average return,
and Rt−kR\_{t-k} is the portfolio return. We set K = 10 in our experiments, enabling the review of the previous 10 weeks. Subsequently, the refined strategy for the next week can be defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | πt+1=agentstrategy​(πt,𝐰t,𝐫t,𝐬t,ℋt,promptstrategy)\pi\_{t+1}=\text{agent}\_{\text{strategy}}(\pi\_{t},\mathbf{w}\_{t},\mathbf{r}\_{t},\mathbf{s}\_{t},\mathcal{H}\_{t},\text{prompt}\_{\text{strategy}}) |  |

where 𝐰t\mathbf{w}\_{t} is the portfolio weight vector selected in week tt,
𝐫t=[rt(1),rt(2),…,rt(n)]⊤\mathbf{r}\_{t}=[r\_{t}^{(1)},r\_{t}^{(2)},\dots,r\_{t}^{(n)}]^{\top} is the realized return vector of all candidate stocks,
and 𝐬t={si,t}i=1n\mathbf{s}\_{t}=\{s\_{i,t}\}\_{i=1}^{n} denotes the set of scoring reports for all stocks in week tt.
An example prompt used by the Strategy Agent is illustrated in Figure [5](https://arxiv.org/html/2510.17393v1#S4.F5 "Figure 5 ‣ 4.4. Strategy Iteration ‣ 4. Methodology ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization").

![Refer to caption](prompt_strategy.png)


Figure 5. Example prompt used by the Strategy Agent for strategy iteration.

## 5. Experiments

In this section, we detail our experimental setup and evaluate the proposed framework by conducting portfolio construction across various stock universes. The performance of our framework is compared against several baseline models to demonstrate its effectiveness and applicability.

### 5.1. Experimental Settings

#### 5.1.1. Dataset Description

We construct four distinct candidate stock universes for evaluation. For each universe, we independently conduct experiments to assess the model’s performance under varying market conditions.

* •

  DJIA Constituents: This set includes 30 large-cap U.S. companies from diverse sectors and serves as a representative benchmark of the broader market222<https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average>.
* •

  Technology Sector Stocks: Comprising 44 constituent companies from the NASDAQ-100 Technology Sector Index333<https://indexes.nasdaqomx.com/Index/Weighting/NDXT>.
* •

  Financial Sector Stocks: A subset of 49 major companies with the highest weights in the SPDR Fund for the Financial Select Sector444<https://www.ssga.com/us/en/individual/etfs/the-financial-select-sector-spdr-fund-xlf>.
* •

  Healthcare Sector Stocks: A selection of 46 top-weighted companies from the SPDR Fund for the Select Sector of Health Care555<https://www.ssga.com/us/en/individual/etfs/the-health-care-select-sector-spdr-fund-xlv>.

Data are retrieved from Alpha Vantage 666<https://www.alphavantage.co/>, and preprocessed according to the methodology detailed in Section [3.2](https://arxiv.org/html/2510.17393v1#S3.SS2 "3.2. Data Collection ‣ 3. Preliminaries ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization"). The evaluation period spans from May 16, 2022 to May 27, 2024. For time-series baselines that require training, we provide historical price data covering the period from May 1, 2012 to May 15, 2022 as the training and validation set.

#### 5.1.2. Baselines

We use the equal-weight strategy (1/N) as a market reference and compare our method against three representative categories of models.

* •

  Rule-based methods: Including SMA (Simple Moving Average), MACD (Moving Average Convergence Divergence), and BOLL (Bollinger Bands) (Murphy, [1999](https://arxiv.org/html/2510.17393v1#bib.bib39)). For each indicator, we construct a corresponding factor score and select the top 5 stocks each week, assigning 20% weight to each.
* •

  Deep learning prediction models: We include the classical LSTM model (Hochreiter and Schmidhuber, [1997](https://arxiv.org/html/2510.17393v1#bib.bib27)) as well as two state-of-the-art transformer-based models: Informer (Zhou et al., [2021](https://arxiv.org/html/2510.17393v1#bib.bib48)) and Autoformer (Wu et al., [2021](https://arxiv.org/html/2510.17393v1#bib.bib44)). For each stock ii at week tt, the response variable is the weekly return ri,tr\_{i,t}. The input to the model includes a 4-week time window of technical features, combined with a stock-specific embedding to enable multi-stock prediction. All model hyper-parameters are tuned on a validation set. At each week tt, the top five stocks with the highest predicted returns are assigned an equal weight of 20% each.
* •

  Multi-LLM baselines: We include both a single-step version and a reflective variant as described in Section [2](https://arxiv.org/html/2510.17393v1#S2 "2. Related Work ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization"). The single-step framework, implemented following by TradingAgent (Zhao et al., [2023](https://arxiv.org/html/2510.17393v1#bib.bib47)), directly generates portfolios from summarized information. The reflective version, following the design of CryptoTrade (Li et al., [2024](https://arxiv.org/html/2510.17393v1#bib.bib32)), further incorporates a Reflection Agent that analyzes previous portfolio returns to refine stock selection. For consistency and fair comparison, we make minor adjustments to the input and output structures of both implementations.

#### 5.1.3. Evaluation Metrics

We use three metrics to evaluate portfolio performance: Accumulated Return (AR),
Sharpe Ratio (SR), and Calmar Ratio (CR).

* •

  Accumulated Return (AR): AR is defined as the total compounded return over the evaluation period:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (10) |  | AR=∏t=1T(1+Rt)−1\text{AR}=\prod\_{t=1}^{T}(1+R\_{t})-1 |  |

  where RtR\_{t} denotes the portfolio return at week tt, and TT is the total number of evaluation weeks.
* •

  Sharpe Ratio (SR): SR measures the risk-adjusted return, capturing how efficiently a portfolio converts volatility into excess return. It is calculated as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (11) |  | SR=𝔼​[Rt]σ​(Rt)\text{SR}=\frac{\mathbb{E}[R\_{t}]}{\sigma(R\_{t})} |  |

  assuming a zero risk-free rate. Here, 𝔼​[Rt]\mathbb{E}[R\_{t}] is the mean return and σ​(Rt)\sigma(R\_{t}) is the standard deviation of returns.
* •

  Calmar Ratio (CR): CR evaluates return relative to the worst drawdown observed, providing an indication of how well a strategy balances profitability against downside risk. It is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (12) |  | CR=AR|MDD|\text{CR}=\frac{\text{AR}}{|\text{MDD}|} |  |

  where the maximum drawdown (MDD) is computed as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (13) |  | MDD=mint⁡(Ct−maxi≤t⁡Cimaxi≤t⁡Ci)\text{MDD}=\min\_{t}\left(\frac{C\_{t}-\max\_{i\leq t}C\_{i}}{\max\_{i\leq t}C\_{i}}\right) |  |

  and CtC\_{t} is the accumulated return up to week tt.

### 5.2. Results and Analysis

We summarize the experimental results across different stock universes in a single table, as shown in Table [1](https://arxiv.org/html/2510.17393v1#S5.T1 "Table 1 ‣ 5.2. Results and Analysis ‣ 5. Experiments ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization"). Below, we present our key findings.

Table 1. Performance comparison across different models and stock universes. Red indicates the highest value in each column, and blue indicates the second highest.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Category | Approach | DJIA Constituents | | | Financial Sector | | | Healthcare Sector | | | Technology Sector | | |
| AR(%) | SR | CR | AR(%) | SR | CR | AR(%) | SR | CR | AR(%) | SR | CR |
| Benchmark | 1/N | 39.50 | 0.168 | 2.98 | 52.63 | 0.16 | 3.95 | 27.82 | 0.12 | 2.45 | 72.13 | 0.16 | 3.59 |
| Rule-based | SMA | 70.63 | 0.20 | 4.52 | 33.10 | 0.10 | 2.08 | 17.21 | 0.07 | 1.26 | 67.36 | 0.13 | 1.95 |
| MACD | 46.00 | 0.15 | 3.02 | 61.16 | 0.15 | 3.42 | 20.58 | 0.08 | 1.29 | 116.29 | 0.19 | 4.30 |
| BOLL | 20.09 | 0.08 | 1.20 | 25.09 | 0.06 | 1.60 | 6.82 | 0.04 | 0.51 | 96.98 | 0.16 | 5.16 |
| Deep Learning | LSTM | 88.42 | 0.23 | 4.91 | 61.24 | 0.15 | 3.54 | 59.78 | 0.15 | 3.26 | 193.39 | 0.21 | 5.81 |
| Informer | 68.96 | 0.22 | 3.88 | 89.49 | 0.25 | 8.08 | 44.37 | 0.15 | 3.54 | 98.61 | 0.15 | 3.33 |
| Autoformer | 104.26 | 0.24 | 5.35 | 75.92 | 0.17 | 4.50 | 30.44 | 0.11 | 2.30 | 102.90 | 0.14 | 2.97 |
| Multi-LLM | Single-Step | 91.69 | 0.27 | 8.94 | 34.92 | 0.15 | 3.10 | 31.40 | 0.12 | 3.11 | 152.84 | 0.25 | 9.04 |
| Reflective | 96.61 | 0.28 | 9.90 | 44.86 | 0.17 | 4.56 | 43.73 | 0.18 | 6.51 | 128.27 | 0.21 | 5.41 |
| 3S-Trader | 131.83 | 0.31 | 11.84 | 84.93 | 0.21 | 7.57 | 51.41 | 0.17 | 3.82 | 183.29 | 0.27 | 11.81 |

#### 5.2.1. Overall Performance of 3S-Trader

Our proposed method demonstrates stable performance across diverse market environments, consistently ranking among the top two models across nearly all evaluation metrics. This advantage is most evident in the mixed-sector DJIA constituents, where 3S-Trader achieves the highest accumulated return of 131.83%, significantly outperforming the second-best model. As illustrated in Figure [6](https://arxiv.org/html/2510.17393v1#S5.F6 "Figure 6 ‣ 5.2.1. Overall Performance of 3S-Trader ‣ 5.2. Results and Analysis ‣ 5. Experiments ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization"), the upward trend of 3S-Trader is clearly visible. Moreover, 3S-Trader exhibits no obvious weaknesses across different performance metrics and sectors, indicating a high degree of robustness and stability in its returns.

![Refer to caption](djia.png)


Figure 6. Comparison of accumulated returns for all methods on DJIA constituents.

#### 5.2.2. Comparison with Rule-based Models

Our proposed method significantly outperforms traditional rule-based strategies across all sectors. In many cases, classical technical indicators such as SMA, MACD, and BOLL even underperform the simple 1/N benchmark. This underperformance can be attributed, in part, to the experimental design: to ensure fair comparison and interpretability, we use fixed-factor rule-based strategies with relatively low trading frequency. However, in real-world trading scenarios, the effectiveness of such strategies often depends on dynamic factor selection, regular parameter tuning, and more frequent position adjustments. These complexities are difficult to fully capture within our current experimental framework. By contrast, our LLM-based approach adapts more flexibly to changing market conditions and integrates diverse signals in a coherent and data-driven manner, which explains its consistent advantage over static rule-based methods.

#### 5.2.3. Comparison with Deep Learning Models

Deep learning models demonstrate strong performance in terms of accumulated return, with each of the three sector-specific stock pools featuring a deep learning model as the top performer in this dimension. In particular, the classical sequence prediction model LSTM performs competitively against the more recent state-of-the-art architectures like Informer and Autoformer. In the technology sector, for instance, LSTM achieves an accumulated return of 193.39%, nearly double that of Informer (98.61%) and Autoformer (102.90%), highlighting its capacity to capture strong trends in high-momentum markets.

However, these models exhibit significant limitations in terms of risk control. This is reflected in both the Sharpe and Calmar Ratios, where their performance often falls short compared to LLM-based frameworks. The relatively lower risk-adjusted returns suggest that deep learning models may overfit to past trends or struggle to generalize under market volatility, leading to inconsistent or overly aggressive allocations. In contrast, multi-LLM systems show more balanced performance, with consistently higher Sharpe and Calmar Ratios. This indicates that while deep learning models are good at capturing trends, they often lack the ability to reason and handle complex information. Multi-LLM frameworks, by combining different data sources and using strategy texts, are better at making stable and informed decisions under uncertainty.

#### 5.2.4. Self-Refined Frameworks in Volatile Markets

Both 3S-Trader and the Reflective framework are designed to refine their strategies by learning from past decisions. We focus on their performance in volatile markets such as healthcare and finance, as shown in Figure [7](https://arxiv.org/html/2510.17393v1#S5.F7 "Figure 7 ‣ 5.2.4. Self-Refined Frameworks in Volatile Markets ‣ 5.2. Results and Analysis ‣ 5. Experiments ‣ 3S-Trader: A Multi-LLM Framework for Adaptive Stock Scoring, Strategy, and Selection in Portfolio Optimization"). In the healthcare sector, the performance gap between the two frameworks is not substantial, both demonstrate clear improvements compared to the Single-Step baseline. Notably, the Reflective variant achieves the best stability in this sector, recording the highest SR of 0.18 and CR of 6.51.

However, in the financial sector, the performance gain from the reflection mechanism is less pronounced. The Reflective variant even underperforms both the Single-Step baseline and the market benchmark for most of the validation period, potentially due to over-adjustment or the absence of clear directional guidance during strategy updates. In contrast, 3S-Trader not only incorporates a reflective loop but also leverages a multi-dimensional scoring system that provides explicit and interpretable criteria for strategy refinement. This holistic design enables consistently superior and more stable performance across different market conditions.

![Refer to caption](comparison.png)


Figure 7. Comparison of accumulated returns for 3S-Trader, Reflective and Single-Step Frameworks across Healthcare and Financial sectors.

## 6. Conclusion and Future Work

In this paper, we proposed 3S-Trader, a multi-LLM framework for portfolio construction that is capable of self-adjustment and adapts to diverse market conditions. The framework condenses recent market information into stock-level scoring reports and applies explicit, interpretable selection criteria to guide portfolio allocation. Compared with traditional rule-based and time-series forecasting models, our approach requires no model training or parameter tuning, yet achieves consistently strong performance across different stock universes, delivering competitive returns and robust stability.

For future work, several directions remain open. First, while the current scoring dimensions are designed based on domain expertise, a promising extension is to enable the automatic discovery and learning of scoring factors from data. Second, our experiments are limited to backtesting; validating the framework in live trading environments will be essential to assess its real-world feasibility. Lastly, incorporating broader asset classes and exploring dynamic risk-control mechanisms could further enhance the generalizability and practical value of the proposed system.

## References

* (1)
* Abdulsatar et al. (2025)

  Majid Abdulsatar, Hussain Ahmad, Diksha Goel, and Faheem Ullah. 2025.
  Towards deep learning enabled cybersecurity risk assessment for microservice architectures.
  *Cluster Computing* 28, 6 (2025), 350.
* Achiam et al. (2023)

  Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. 2023.
  Gpt-4 technical report.
  *arXiv preprint arXiv:2303.08774* (2023).
* Ahmad and Goel (2025)

  Hussain Ahmad and Diksha Goel. 2025.
  The future of ai: Exploring the potential of large concept models.
  *arXiv preprint arXiv:2501.05487* (2025).
* Ahmad et al. (2024)

  Hussain Ahmad, Christoph Treude, Markus Wagner, and Claudia Szabo. 2024.
  Smart HPA: A resource-efficient horizontal pod auto-scaler for microservice architectures. In *2024 IEEE 21st International Conference on Software Architecture (ICSA)*. IEEE, 46–57.
* Ahmad et al. (2025a)

  Hussain Ahmad, Christoph Treude, Markus Wagner, and Claudia Szabo. 2025a.
  Resilient Auto-Scaling of Microservice Architectures with Efficient Resource Management.
  *arXiv preprint arXiv:2506.05693* (2025).
* Ahmad et al. (2025b)

  Hussain Ahmad, Christoph Treude, Markus Wagner, and Claudia Szabo. 2025b.
  Towards resource-efficient reactive and proactive auto-scaling for microservice architectures.
  *Journal of Systems and Software* 225 (2025), 112390.
* Ahmad et al. (2025c)

  Hussain Ahmad, Faheem Ullah, and Rehan Jafri. 2025c.
  A survey on immersive cyber situational awareness systems.
  *Journal of Cybersecurity and Privacy* 5, 2 (2025), 33.
* Ahmed et al. (2024)

  Rabbia Ahmed, Sadaf Abdul Rauf, and Seemab Latif. 2024.
  Leveraging large language models and prompt settings for context-aware financial sentiment analysis. In *2024 5th International Conference on Advancements in Computational Sciences (ICACS)*. IEEE, 1–9.
* Araci (2019)

  Dogu Araci. 2019.
  FinBERT: Financial Sentiment Analysis with Pre-trained Language Models.
  *CoRR* (2019).
* Bollerslev (1986)

  Tim Bollerslev. 1986.
  Generalized autoregressive conditional heteroskedasticity.
  *Journal of Econometrics* 31, 3 (1986), 307–327.
* Bommasani et al. (2021)

  Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. 2021.
  On the opportunities and risks of foundation models.
  *arXiv preprint arXiv:2108.07258* (2021).
* Borovykh et al. (2017)

  Anastasia Borovykh, Sander Bohte, and Cornelis W. Oosterlee. 2017.
  Conditional time series forecasting with convolutional neural networks.
  *arXiv preprint arXiv:1703.04691* (2017).
* Box and Jenkins (1990)

  George Edward Pelham Box and Gwilym Jenkins. 1990.
  *Time Series Analysis, Forecasting and Control*.
  Holden-Day, Inc., USA.
* Brown et al. (2020)

  Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020.
  Language models are few-shot learners.
  *Advances in neural information processing systems* 33 (2020), 1877–1901.
* Chopra et al. (2024)

  Shivansh Chopra, Hussain Ahmad, Diksha Goel, and Claudia Szabo. 2024.
  Chatnvd: Advancing cybersecurity vulnerability assessment with large language models.
  *arXiv preprint arXiv:2412.04756* (2024).
* Connor (2000)

  Gregory Connor. 2000.
  Active portfolio management: a quantitative approach to providing superior returns and controlling risk.
* Deng et al. (2016)

  Yuhong Deng, Feng Bao, Yongcheng Kong, Zhiquan Ren, and Qionghai Dai. 2016.
  Deep direct reinforcement learning for financial signal representation and trading.
  *IEEE transactions on neural networks and learning systems* 28, 3 (2016), 653–664.
* Fabozzi et al. (2007)

  Frank J Fabozzi, Petter N Kolm, Dessislava A Pachamanova, and Sergio M Focardi. 2007.
  *Robust Portfolio Optimization and Management*.
  John Wiley & Sons.
* Fischer and Krauss (2018)

  Thomas Fischer and Christopher Krauss. 2018.
  Deep learning with long short-term memory networks for financial market predictions. In *European Journal of Operational Research*, Vol. 270. 654–669.
* Goel (2023)

  Diksha Goel. 2023.
  Enhancing network resilience through machine learning-powered graph combinatorial optimization: Applications in cyber defense and information diffusion.
  *arXiv preprint arXiv:2310.10667* (2023).
* Goel et al. (2024a)

  Diksha Goel, Hussain Ahmad, Ankit Kumar Jain, and Nikhil Kumar Goel. 2024a.
  Machine learning driven smishing detection framework for mobile security.
  *arXiv preprint arXiv:2412.09641* (2024).
* Goel et al. (2025)

  Diksha Goel, Hussain Ahmad, Kristen Moore, and Mingyu Guo. 2025.
  Co-Evolutionary Defence of Active Directory Attack Graphs via GNN-Approximated Dynamic Programming.
  *arXiv preprint arXiv:2505.11710* (2025).
* Goel et al. (2024b)

  Diksha Goel, Kristen Moore, Mingyu Guo, Derui Wang, Minjune Kim, and Seyit Camtepe. 2024b.
  Optimizing cyber defense in dynamic active directories through reinforcement learning. In *European Symposium on Research in Computer Security*. Springer, 332–352.
* Gu et al. (2024)

  Jingyi Gu, Junyi Ye, Guiling Wang, and Wenpeng Yin. 2024.
  Adaptive and explainable margin trading via large language models on portfolio management. In *Proceedings of the 5th ACM International Conference on AI in Finance*. 248–256.
* Haque et al. (2022)

  Mubin Ul Haque, Isuru Dharmadasa, Zarrin Tasnim Sworna, Roshan Namal Rajapakse, and Hussain Ahmad. 2022.
  ” I think this is the most disruptive technology”: Exploring Sentiments of ChatGPT Early Adopters using Twitter Data.
  *arXiv preprint arXiv:2212.05856* (2022).
* Hochreiter and Schmidhuber (1997)

  Sepp Hochreiter and Jürgen Schmidhuber. 1997.
  Long short-term memory.
  *Neural computation* 9, 8 (1997), 1735–1780.
* Jayalath et al. (2024)

  Raveen Kanishka Jayalath, Hussain Ahmad, Diksha Goel, Muhammad Shuja Syed, and Faheem Ullah. 2024.
  Microservice vulnerability analysis: A literature review with empirical insights.
  *IEEE Access* (2024).
* Jiang et al. (2017)

  Zhengyao Jiang, Dixing Xu, and Jinjun Liang. 2017.
  A deep reinforcement learning framework for the financial portfolio management problem.
  *arXiv preprint arXiv:1706.10059* (2017).
* Kim et al. (2024)

  Alex Kim, Maximilian Muhn, and Valeri Nikolaev. 2024.
  Financial statement analysis with large language models.
  *arXiv preprint arXiv:2407.17866* (2024).
* Koa et al. (2024)

  Kelvin JL Koa, Yunshan Ma, Ritchie Ng, and Tat-Seng Chua. 2024.
  Learning to generate explainable stock predictions using self-reflective large language models. In *Proceedings of the ACM Web Conference 2024*. 4304–4315.
* Li et al. (2024)

  Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu, and Bingsheng He. 2024.
  CryptoTrade: A reflective LLM-based agent to guide zero-shot cryptocurrency trading. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*. 1094–1106.
* Liu et al. (2023)

  Xiao-Yang Liu, Guoxuan Wang, Hongyang Yang, and Daochen Zha. 2023.
  Fingpt: Democratizing internet-scale data for financial large language models.
  *arXiv preprint arXiv:2307.10485* (2023).
* Liu et al. (2024)

  Ziyang Liu, Meng Yu, Xueting Ren, Zhaoxin Yu, Zihan Zhang, Yuan Yang, Runzhi Zhang, Jiawei Zhou, Jing Liu, and Jie Tang. 2024.
  FinVision: A Multi-Agent Framework for Stock Market Prediction.
  *arXiv preprint arXiv:2405.18514* (2024).
* Markowitz (1952)

  Harry Markowitz. 1952.
  Portfolio Selection.
  *The Journal of Finance* 7, 1 (1952), 77–91.

  <http://www.jstor.org/stable/2975974>
* Mebane (2019)

  Daniel Mebane. 2019.
  Technical Analysis Library in Python.


  Available at <https://github.com/bukosabino/ta>.
* Mortaji et al. (2024)

  Manale Mortaji, Azeddine Khiat, and Mohamed Benhouad. 2024.
  Reinforcement learning application in portfolio optimization: a comprehensive literature review. In *2024 International Conference on Intelligent Systems and Computer Vision (ISCV)*. IEEE, 1–6.
* Muhammad et al. (2023)

  Tashreef Muhammad, Anika Bintee Aftab, Muhammad Ibrahim, Md Mainul Ahsan, Maishameem Meherin Muhu, Shahidul Islam Khan, and Mohammad Shafiul Alam. 2023.
  Transformer-based deep learning model for stock price prediction: A case study on Bangladesh stock market.
  *International Journal of Computational Intelligence and Applications* 22, 03 (2023), 2350013.
* Murphy (1999)

  John J. Murphy. 1999.
  *Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications*.
  New York Institute of Finance.
* Ozbayoglu et al. (2020)

  Ahmet Murat Ozbayoglu, Mehmet Ugur Gudelek, and Omer Berat Sezer. 2020.
  Deep learning for financial applications: A survey.
  *Applied soft computing* 93 (2020), 106384.
* Srivastava et al. (2024)

  Pragya Srivastava, Manuj Malik, Vivek Gupta, Tanuja Ganu, and Dan Roth. 2024.
  Evaluating LLMs’ Mathematical Reasoning in Financial Document Question Answering.
  *arXiv preprint arXiv:2402.11194* (2024).
* Statman (1987)

  Meir Statman. 1987.
  How many stocks make a diversified portfolio?
  *Journal of Financial and Quantitative Analysis* 22, 3 (1987), 353–363.
* Ullah et al. (2025)

  Faheem Ullah, Xiaohan Ye, Uswa Fatima, Zahid Akhtar, Yuxi Wu, and Hussain Ahmad. 2025.
  What Skills Do Cyber Security Professionals Need?
  *arXiv preprint arXiv:2502.13658* (2025).
* Wu et al. (2021)

  Haixu Wu, Yifan Xu, Jiahui Wang, Guodong Long, Chengqi Zhang, and Lina Yao. 2021.
  Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting. In *Advances in Neural Information Processing Systems (NeurIPS)*, Vol. 34. 22419–22430.
* Zhang et al. (2024)

  Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing Zhao, Yilei Zhao, Xinyu Cai, et al. 2024.
  A multimodal foundation agent for financial trading: Tool-augmented, diversified, and generalist. In *Proceedings of the 30th acm sigkdd conference on knowledge discovery and data mining*. 4314–4325.
* Zhang et al. (2025)

  Yiyao Zhang, Hussain Ahmad, Diksha Goel, and Claudia Szabo. 2025.
  RegimeFolio: A Regime Aware ML System for Sectoral Portfolio Optimization in Dynamic Markets.
  *arXiv preprint arXiv:2510.14986* (2025).
* Zhao et al. (2023)

  Yujia Zhao, Xiaozhong Liu, Yunkai Wang, Zihang Wang, Canwen Xu, Yixin Zhang, et al. 2023.
  TradingAgent: LLMs for Trading via Chain of Thought and Memory.
  *arXiv preprint arXiv:2311.09722* (2023).
* Zhou et al. (2021)

  Haoyi Zhou, Shanghang Zhang, Jiehui Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wancai Zhang. 2021.
  Informer: Beyond efficient transformer for long sequence time-series forecasting. In *Proceedings of AAAI*.