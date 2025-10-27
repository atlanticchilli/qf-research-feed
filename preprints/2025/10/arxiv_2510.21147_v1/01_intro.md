---
authors:
- Chujun He
- Zhonghao Huang
- Xiangguo Li
- Ye Luo
- Kewei Ma
- Yuxuan Xiong
- Xiaowei Zhang
- Mingyang Zhao
doc_id: arxiv:2510.21147v1
family_id: arxiv:2510.21147
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2510.21147v1
url_html: https://arxiv.org/html/2510.21147v1
venue: arXiv q-fin
version: 1
year: 2025
---

\OneAndAHalfSpacedXI\TheoremsNumberedThrough\ECRepeatTheorems\EquationsNumberedThrough\MANUSCRIPTNO

\RUNAUTHOR

He et al.

\RUNTITLE

Hierarchical AI Multi-Agent Investing

\TITLE

Hierarchical AI Multi-Agent Fundamental Investing: Evidence from China’s A‑Share Market

\ARTICLEAUTHORS\AUTHOR

Chujun He, Zhonghao Huang, Xiangguo Li, Ye Luo, Kewei Ma \AFFFaculty of Business and Economics, University of Hong Kong \EMAILskylar@connect.hku.hk, huangzh0624@connect.hku.hk, u3590480@connect.hku.hk, kurtluo@hku.hk, u3596913@connect.hku.hk
\AUTHORYuxuan Xiong \AFFDepartment of Mathematics, University of Hong Kong \EMAILu3637747@connect.hku.hk
\AUTHORXiaowei Zhang, Mingyang Zhao \AFFDepartment of Industrial Engineering and Decision Analytics, Hong Kong University of Science and Technology \EMAILxiaoweiz@ust.hk, mingyang.zhao@connect.ust.hk

\ABSTRACT

We present a multi-agent, AI-driven framework for fundamental investing that integrates macro indicators, industry-level and firm-specific information to construct optimized equity portfolios. The architecture comprises: (i) a Macro agent that dynamically screens and weights sectors based on evolving economic indicators and industry performance; (ii) four firm-level agents—Fundamental, Technical, Report, and News—that conduct in-depth analyses of individual firms to ensure both breadth and depth of coverage; (iii) a Portfolio agent that uses reinforcement learning to combine the agent outputs into a unified policy to generate the trading strategy; and (iv) a Risk Control agent that adjusts portfolio positions in response to market volatility.
We evaluate the system on the constituents by the CSI 300 Index of China’s A-share market and find that it consistently outperforms standard benchmarks and a state-of-the-art multi-agent trading system on risk-adjusted returns and drawdown control.
Our core contribution is a hierarchical multi-agent design that links top-down macro screening with bottom-up fundamental analysis, offering a robust and extensible approach to factor-based portfolio construction.

\KEYWORDS

Multi-agent system, artificial intelligence, large language models, reinforcement learning, fundamental investing, robo-advisor

## 1 Introduction

Equity portfolio management is a multi-source, multi-horizon decision problem facing persistent uncertainty. Practitioners like fund managers synthesize macroeconomic and industry trends, firm fundamentals, price dynamics, and rapidly evolving textual information while contending with regime shifts. Signal fragility and overfitting are perennial risks when statistical models are trained on noisy, path-dependent data.
These challenges are particularly acute for individual investors, who, as a vast body of literature documents, exhibit behavioral biases such as portfolio over-concentration and under-diversification (French and Poterba [1991](https://arxiv.org/html/2510.21147v1#bib.bib22), Huberman [2001](https://arxiv.org/html/2510.21147v1#bib.bib28)).
Meanwhile, risk management and governance demand transparent, attributable decisions rather than opaque end-to-end predictions. These pressures call for architectures that flexibly integrate diverse data modalities, adapt to changing conditions, and remain interpretable—ideally with a hierarchical organization that clarifies how top-level context informs downstream decisions.

Although new technologies are continually adopted in financial investing—most visibly through robo-advising and the broader deployment of machine learning, and existing work largely evaluates them in isolation. Machine learning and deep learning—such as AutoAlpha (Zhang et al. [2020](https://arxiv.org/html/2510.21147v1#bib.bib56)) and AlphaGPT (Wang et al. [2023](https://arxiv.org/html/2510.21147v1#bib.bib48))—are often used for factor discovery or return forecasting; reinforcement learning (RL) is positioned as a direct portfolio policy optimizer (Ye et al. [2020](https://arxiv.org/html/2510.21147v1#bib.bib53)); and natural language processing, including large language models (LLMs) is applied to sentiment extraction from news, filings, or earnings calls (Xing [2025](https://arxiv.org/html/2510.21147v1#bib.bib49)). This single-technology focus yields valuable insights, but it leaves open the question of principled integration: how should macro context, structured signals, market microstructure awareness, and unstructured text be combined so that each technology operates where it adds the most value, conflicts are reconciled, and accountability is preserved? In practice, single-model pipelines centered on structured fundamentals or technical indicators often under utilize unstructured text and macro context, limiting responsiveness to news and policy shocks. Conversely, monolithic deep learning systems that ingest everything end to end can be difficult to diagnose, audit, govern in regulated environments, and often suffer from overfitting.
While recent LLM-based agents, such as FinMem (Yu et al. [2025](https://arxiv.org/html/2510.21147v1#bib.bib55)) and FinAgent (Zhang et al. [2024](https://arxiv.org/html/2510.21147v1#bib.bib57)) demonstrate the value of textual information, they often focus on single-stock trading or lack a comprehensive hierarchical framework for portfolio construction.
Traditional ensemble methods typically combine signals at the feature or model level without explicit role specialization or cross-level coordination, and they can be slow to reweight under regime changes. Our work addresses this gap with a hierarchical, role-based framework that assigns each technology to the level of the decision process where it is most effective and unifies them through adaptive aggregation and risk-aware execution.

We propose an organizing principle inspired by the structure of fundamental investment firms such as mutual funds and macro-fundamental based hedge funds: a hierarchical, role-differentiated multi-(AI)-agent system that mirrors the top-down investment process. Responsibilities of each agent are designed modular as leave-one-out ablation study is easy to carry for us to understand which component plays a bigger role in fundamental investing. The agents are aligned with real-world functions—macro strategy, security analysis, portfolio construction, and risk control—facilitating interpretability, targeted improvements, and clear attribution. Unlike the typical quant strategy that ensembles a parallel set of features by purely statistical machine learning approach, our macro-to-micro flow concentrates modeling capacity where it matters, allowing upstream agents to set context and constraints that downstream agents exploit, while preserving the ability to audit each stage independently.

At a high level, the system comprises five components arranged in a hierarchy. A *Macro agent*, acting as a chief economist, occupies the top layer and analyzes macroeconomic and industry-level signals to identify sectors with favorable conditions, and therefore, allows us to focus our analyze on these particular sectors. Within these sectors, four specialized stock-scoring agents operate at the analysis layer: a *Fundamental agent*, a *Technical agent*, a *News agent*, and a *Report agent*, while the News and Report agents use LLMs to extract signals from unstructured text, and the other two agents depend on traditional numerical analysis. Such an approach addresses the multi-modality issue of data of different frequencies. A *Portfolio agent* sits at the following up allocation layer, aggregating these heterogeneous views by learning dynamic weights over the specialized agents based on state variables such as their recent performances, thereby producing composite scores and constructing the portfolio. Finally, a *Risk Control agent* forms the protective layer, adjusting exposures in response to extreme volatility. Each specialized agent can form a stand alone portfolio by investing in the top decile of its ranked list, and the hierarchical ensemble combines their strengths into a unified, adaptive allocation.

Beyond this overall design, our technical contributions center on how the hierarchy structure assembles heterogeneous technologies in a cohesive pipeline. First, we integrate LLMs for unstructured text ingestion at the analysis layer, enabling the News and Report agents to transform earnings calls, filings, and real-time news into structured signals.
This moves beyond using LLMs for simple sentiment analysis by embedding them in a dynamic, hierarchical workflow, addressing a key challenge in complex financial decision-making (Zhao et al. [2024a](https://arxiv.org/html/2510.21147v1#bib.bib59), Yao et al. [2023b](https://arxiv.org/html/2510.21147v1#bib.bib52), [a](https://arxiv.org/html/2510.21147v1#bib.bib51)).
Rather than treating LLM outputs generally as features, we embed them within the hierarchical workflow to allow them to compare with the structure signals in a dynamic way.

Second, we introduce an adaptive ensembling mechanism at the allocation layer that learns dynamic weights across heterogeneous agents using previously rolling performance metrics. This online reweighting allows the system to respond to regime shifts by reallocating emphasis among fundamentals, technicals, and text-driven insights, while the hierarchical separation ensures that reweighting occurs after sector context has been established. This RL-guided adaptive approach is similar in spirit to recent work applying RL to portfolio management (Ye et al. [2020](https://arxiv.org/html/2510.21147v1#bib.bib53)) but operates at the level of agent weights within a hierarchy.
That is, the allocation process is guided by the instructions of the Macro agent, which resembles the real industry corporate decision process, and maintains robustness without simply collapsing signals into a single monolithic model.

Third, the hierarchy begins with a sector prefiltering stage that narrows the search space and reduces noise. By allowing the Macro agent to select favorable sectors before stock-level analysis, we dynamically focus stock pools where the signal-to-noise ratio could be higher, and create a natural interface for incorporating macro and industry priors. This top-down selection is a key benefit of the hierarchical organization which is grounded in financial theory, such as the well-documented industry momentum effect (Moskowitz and Grinblatt [1999](https://arxiv.org/html/2510.21147v1#bib.bib38)): context is set once, then propagated to lower layers. Besides, compared to existing literature on applying LLM based analysis to stock level files, our approach is more scalable and less costly due to this hierarchy design.

Fourth, we enforce a clear separation of responsibilities across levels—alpha generation by specialized agents, portfolio construction via adaptive aggregation, and risk control through exposure management. This separation improves interpretability and governance by enabling attribution and drill-down diagnostics at each layer. It also supports operational robustness: components can be upgraded, swapped, or extended in a modular way without destabilizing the entire system, provided their interfaces to adjacent layers remain consistent. This modularity satisfies key governance requirements in regulated financial environments and creates a natural interface for human-AI synergy, where human analysts may excel at interpreting intangible factors while AI handles voluminous data (Cao et al. [2024a](https://arxiv.org/html/2510.21147v1#bib.bib12)).

Finally, we position the approach as a general framework for multi-agent coordination in financial investiment rather than a single, fixed model. The hierarchy establishes roles, interfaces, and learning rules that can accommodate new agents—such as order-book microstructure models or alternative data specialists in the future—alongside alternative weighting schemes, including Bayesian model averaging or meta-learning, and extensions to other asset classes. In this way, the hierarchical multi-agent architecture serves as a foundation for ongoing innovation that mimics the operational structure of fundamental/value investing. In principle, this design can allow human-in-the-loop, e.g., replace our LLM-based AI Macro agent with a real experienced macro economist (i.e., a human agent), or they can operate together in a copilot form, and similar to other components of the system.

We evaluate the proposed framework using a comprehensive and challenging dataset comprising the Chinese A-share market from January 1, 2019, to December 31, 2024—a period characterized by pronounced volatility and two major market regime shifts. The dataset integrates detailed macroeconomic indicators, industry-level factors, and firm-specific features, providing a rich empirical foundation. Extensive experiments demonstrate that our framework consistently outperforms all benchmark models in both training and testing sample, while rigorous backtesting further confirms its capacity to generate robust excess returns with reduced volatility. To mitigate risks of hyperparameter overfitting and to assess generalizability, model parameters are trained exclusively on the sample from January 2019 to December 2023, with performance validated on the out-of-sample period covering January to December 2024. Additionally, an ablation study is conducted to systematically examine the contribution of each model component.

### 1.1 Literature Review

#### 1.1.1 Challenges in Individual Investment

Ordinary market participants, particularly the financially unsophisticated, find it intrinsically difficult to make good investment decisions in these financial markets. Despite extensive empirical evidence in the classical finance literature (Badarinza et al. [2016](https://arxiv.org/html/2510.21147v1#bib.bib3)). Tobin ([1958](https://arxiv.org/html/2510.21147v1#bib.bib47)), Markowits ([1952](https://arxiv.org/html/2510.21147v1#bib.bib35)), Campbell and Viceira ([2002](https://arxiv.org/html/2510.21147v1#bib.bib11)), and Fama and French ([2002](https://arxiv.org/html/2510.21147v1#bib.bib20)) document the existence of higher expected returns (risk premiums) in equity markets. Campbell ([2006](https://arxiv.org/html/2510.21147v1#bib.bib10)) finds that only a small share of people at the bottom of the wealth spectrum hold investments in publicly traded stocks.

Beyond the participation puzzle, a vast and ingenious empirical literature investigates the composition of household stock portfolios, often assuming that investors operate with partial information. Individuals tend to exhibit excessive portfolio concentration in local, domestic equities (French and Poterba [1991](https://arxiv.org/html/2510.21147v1#bib.bib22), Huberman [2001](https://arxiv.org/html/2510.21147v1#bib.bib28)) as well as their own company’s stock (Mitchell and Utkus [2004](https://arxiv.org/html/2510.21147v1#bib.bib37)). This behavioral pattern reveals significant limitations in their market comprehension and a pronounced lack of diversification knowledge.
On the contrary, our model can achieve a more comprehensive understanding of market conditions and individual stock information through hierarchical analysis at macro, industry and individual stock levels, while integrating multiple data sources including news, financial statements, equity reports, and price-volume data, thereby enabling the selection of high-quality stocks from a larger stock pool.

A further critical shortcoming of individual investment strategies is suboptimal portfolio construction, manifested as persistent under-diversification. A robust empirical finding indicates that retail investors tend to allocate a disproportionate share of their capital to a concentrated set of risky assets, typically individual equities or poorly-diversified fund products; see Barber and Odean ([2000](https://arxiv.org/html/2510.21147v1#bib.bib4)), Gargano and Rossi ([2018](https://arxiv.org/html/2510.21147v1#bib.bib23)), and D’Acunto et al. ([2019](https://arxiv.org/html/2510.21147v1#bib.bib18)).
Our Risk Control agent enables more effective risk mitigation in investment decision-making. In back-testing results, during periods of adverse market conditions, the model demonstrates significantly lower drawdown magnitudes compared to the benchmark.

#### 1.1.2 Limitations of Human Financial Advisors

Although some may argue that investment advisors can enhance portfolio returns, there is in fact scant empirical evidence in the literature to support this claim.
Gennaioli et al. ([2015](https://arxiv.org/html/2510.21147v1#bib.bib24)) point out that professional financial guidance can help address underdiversification issues and enhance investment performance for individual investors. Providing empirical evidence that greater trust in financial advisers leads to increased risk-taking among investors. However, the higher returns experienced are insufficient to offset the elevated fees. This suggests that investors may either be unaware of the costs associated with advisory services or prioritize factors beyond maximizing portfolio returns in their interactions with financial advisers.

Contrary to the conventional expectation that human investment advisors contribute to superior investment performance, numerous studies indicate that human investment advisors confront significant practical limitations. Recent empirical evidence suggests that conflicts of interest inherent in the advisor-client relationship can lead to a significant distortion of portfolio asset allocation.
Investment accounts managed by financial advisors and mutual funds sold through brokers tend to deliver poorer performance compared to self-managed portfolios (Bergstresser et al. [2008](https://arxiv.org/html/2510.21147v1#bib.bib7), Christoffersen et al. [2013](https://arxiv.org/html/2510.21147v1#bib.bib15), Chalmers and Reuter [2020](https://arxiv.org/html/2510.21147v1#bib.bib14)).
Hackethal et al. ([2012](https://arxiv.org/html/2510.21147v1#bib.bib27)) demonstrate that advised accounts under-perform self-managed portfolios in net returns and risk-adjusted performance (Sharpe ratios), particularly under bank advisors, with elevated trading costs from commission-driven turnover. Linnainmaa et al. ([2021](https://arxiv.org/html/2510.21147v1#bib.bib32)) find that financial advisors exhibit investment behaviors similar to their clients, characterized by frequent trading, return chasing, a preference for expensive actively managed funds, and under-diversification. Investment advisors tend to accommodate the behavioral biases of their clients, prompting them to pursue strong historical performance and invest in actively managed mutual funds (Mullainathan et al. [2012](https://arxiv.org/html/2510.21147v1#bib.bib40)).
Retirement plan administrators tend to prioritize their own proprietary funds when creating investment lineups (Pool et al. [2016](https://arxiv.org/html/2510.21147v1#bib.bib41)). Client behaviors strongly correlate with advisors’ personal strategies (Linnainmaa et al. [2021](https://arxiv.org/html/2510.21147v1#bib.bib32)). In contrast, LLM-derived analytical results can circumvent the subjective biases inherent in human advisory services and remain uninfluenced by personal preferences or individual predispositions.

As a consequence, many individuals exhibit pronounced mistrust towards human financial advisors, driven by apprehensions about being subjected to financially motivated malfeasance (Calcagno and Monticone [2015](https://arxiv.org/html/2510.21147v1#bib.bib9), Lachance and Tang [2012](https://arxiv.org/html/2510.21147v1#bib.bib30), Burke and Hung [2021](https://arxiv.org/html/2510.21147v1#bib.bib8)).

As Reher and Sokolinski ([2024](https://arxiv.org/html/2510.21147v1#bib.bib42)) note, human investment advisors typically serve an exclusive clientele of affluent individuals. In contrast, our system is designed to deliver cost-effective advisory services to a much broader demographic.

#### 1.1.3 Rise of Robo-Advisors

The advent of robo-advisors in the mid-2000s was driven by the shortcomings of traditional financial advisory services.
D’Acunto et al. ([2019](https://arxiv.org/html/2510.21147v1#bib.bib18)) offer empirical evidence that robo-advising tools enhance portfolio diversification, mitigate behavioral biases, and improve investment performance.
D’Acunto and Rossi ([2021](https://arxiv.org/html/2510.21147v1#bib.bib19)) investigate the emergence of robo-advisors, analyzing their classifications, benefits, and challenges while outlining unresolved interdisciplinary issues that will determine the evolution of algorithmic financial advice.
Robo-advisors are capable of serving individuals with significantly lower wealth levels, while human financial advisors, being limited by time, generally focus on catering to more affluent households (Reher and Sokolinski [2024](https://arxiv.org/html/2510.21147v1#bib.bib42)).

In the study of an Automated Financial Management service, Reher and Sun ([2019](https://arxiv.org/html/2510.21147v1#bib.bib43)) finds that portfolios constructed through the service exhibit a higher degree of diversification compared to those that are self-managed. Furthermore, they document that a reduction in the minimum investment threshold required for access is associated with a significant increase in customer fund inflows.
Moreover, in contrast to traditional human advisors who use survey-based approaches to assess investor risk preferences, robo-advising can leverage machine learning algorithms to infer risk tolerance from investors’ historical investment decisions (Alsabah et al. [2021](https://arxiv.org/html/2510.21147v1#bib.bib1)), especially for financially unsophisticated investors.

Several studies compare robo-advisors with human analysts. Coleman et al. ([2022](https://arxiv.org/html/2510.21147v1#bib.bib16)) compares algorithmic (“Robo”) analysts to their human counterparts, finding that robo-analysts produce less optimistic and more frequently revised recommendations with reduced conflicts of interest. Their automated processing of complex disclosures generates long-term investment value, significantly outperforming human analysts’ buy recommendations. Similarly, Cao et al. ([2024a](https://arxiv.org/html/2510.21147v1#bib.bib12)) explores the synergy between human analysts and AI in stock return predictions, noting that while AI excels in handling voluminous data, humans are better at interpreting intangible assets and financial distress. Combined approaches reduce extreme errors, suggesting complementary strengths.

Recent research examines the profiles of early adopters and the industry-wide effects of automated financial advisory platforms.
Based on the FINRA 2015 survey data, Kim et al. ([2019](https://arxiv.org/html/2510.21147v1#bib.bib29)) and Lu et al. ([2023](https://arxiv.org/html/2510.21147v1#bib.bib34)) find that younger age groups, higher disposable income, and greater risk propensity are significantly associated with early adoption of automated financial advisory platforms. Similarly, Baulkaran and Jain ([2023](https://arxiv.org/html/2510.21147v1#bib.bib5)) examines robo-advisor users in India, revealing that typical users are young, male, married, small investors, and professionals. Ben-David et al. ([2022](https://arxiv.org/html/2510.21147v1#bib.bib6)) further notes that robo-advisors significantly reduce demand for human financial advice, especially among distrustful investors, underscoring their disruptive potential in wealth management.
Our framework exhibits strong interactivity and can articulate analytical reasoning and rationale, thereby enhancing accessibility and usability for investors, particularly elderly and non-professional investors.

#### 1.1.4 LLMs for Financial Decision-Making

Substantial research is dedicated to creating versatile LLM-based agents capable of sequential decision-making (Zhao et al. [2024a](https://arxiv.org/html/2510.21147v1#bib.bib59), Yao et al. [2023a](https://arxiv.org/html/2510.21147v1#bib.bib51), [b](https://arxiv.org/html/2510.21147v1#bib.bib52)).
Moreover, scholars have begun to investigate strategies for leveraging LLM agents to achieve enhanced performance in more complex decision-making tasks within the financial domain
(De Curtò et al. [2023](https://arxiv.org/html/2510.21147v1#bib.bib17), Zhao et al. [2024b](https://arxiv.org/html/2510.21147v1#bib.bib60), Liu et al. [2025](https://arxiv.org/html/2510.21147v1#bib.bib33), Cao et al. [2024b](https://arxiv.org/html/2510.21147v1#bib.bib13)), wherein environments exhibit greater volatility, resulting in a multitude of unpredictable factors that hinder the agent’s capacity for precise introspection into the causes of suboptimal decision outcomes. FinMem (Yu et al. [2025](https://arxiv.org/html/2510.21147v1#bib.bib55)) augments performance in single-stock trading by integrating a memory module with its LLM agent to facilitate a cycle of reflection and refinement. FinAgent (Zhang et al. [2024](https://arxiv.org/html/2510.21147v1#bib.bib57)) enhances trading profitability by leveraging an external quantitative tool to counteract market volatility. AlphaGPT (Wang et al. [2023](https://arxiv.org/html/2510.21147v1#bib.bib48)) and AutoAlpha (Zhang et al. [2020](https://arxiv.org/html/2510.21147v1#bib.bib56)) to discover both price-volume and formulaic alpha factors, further underscoring their adaptability across financial applications.

Diverging from conventional rule-based and RL methodologies, which are often constrained to using only price data and typically function as “black boxes” lacking interpretability, our framework leverages a multi-source data integration approach. It provides not only stock recommendations but also the explicit rationales behind them, significantly enhancing the model’s transparency and explainability.

Furthermore, we address the limitations observed in current mainstream models. For instance, models like TradingGPT often focus on single-stock trading tasks and are validated through backtests on a single asset. Similarly, models such as FinAgent and FinCon base their backtesting on a small selection of mainstream stocks. In stark contrast, our framework conducts stock selection and backtesting across a much broader and more representative stock pool—the CSI 300 index—thereby yielding results with substantially greater robustness and generalizability.

While some advanced models like FinCon have begun to incorporate portfolio management, our framework advances this concept further by constructing a hierarchical portfolio that allocates capital from the macro level down to individual stocks. Critically, it adopts a RL mechanism to dynamically adjust the weights among different agents. This process systematically amplifies the influence of agents with superior historical performance in the portfolio construction process, ensuring continuous optimization and adaptation.

Compared to the open-source MASS (Guo et al. [2025](https://arxiv.org/html/2510.21147v1#bib.bib26)), a multi-agent scaling simulation framework designed for portfolio construction, this model demonstrates superior performance in backtesting on the CSI 300 index.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2510.21147v1#S2 "2 Methodology") outlines a detailed description of our proposed methodology, multi-agent system architecture, and the key agents that deals with different kinds of data.
Section [3](https://arxiv.org/html/2510.21147v1#S3 "3 Experiments") introduces data, conducts a comprehensive comparative analysis, benchmarking our model against both standard market indices and other contemporary multi-agent models to demonstrate its efficacy and robustness. Section [4](https://arxiv.org/html/2510.21147v1#S4 "4 Conclusion") concludes.

## 2 Methodology

Our system implements a QuantMental investment framework, following a top-down framework: from macro and industry to the firms analysis; see Figure [2](https://arxiv.org/html/2510.21147v1#S2 "2 Methodology"). At the top level, the Macro agent identifies the most promising industries, serving as a filter to focus subsequent analysis. Within the selected industries, multiple firm-level agents—including the Fundamental agent, Technical agent, News agent, and Report agent generate distinct scores for each stock, capturing diverse aspects such as financial health, market behavior and informational sentiment. The Portfolio agent then dynamically allocates weights across these firm-level signals, optimizing for expected Sharpe ratio and annual return while ensuring diversification between agents. Finally, the Risk Control agent adjusts overall portfolio exposure according to market volatility, helping the system navigate extreme events such as policy shocks or geopolitical crises. By integrating top-down sector analysis with multi-agent stock evaluation and adaptive portfolio management, the system aims to create a prevailing portfolio and manage risk in a dynamic market environment.

\FIGURE![[Uncaptioned image]](figures/Workflow.png)

Multi-Agent Trading System

### 2.1 Data Flow and Obfuscation

The proposed fundamental investing workflow combines a CSI 300 stock pool with industry-level filtering mechanisms and firm-level multi-agent evaluation.
This integrated approach enables the systematic incorporation of multi-level market information, encompassing macroeconomic conditions and industry-level characteristics, firm-specific features, and benchmark-based variables derived from equity indices.

We curate the stock pool from the Chinese A-share market, the CSI 300 index, 𝒮tCSI⊆{1,…,n}\mathcal{S}\_{t}^{\mathrm{CSI}}\subseteq\{1,\dots,n\} at rebalancing date tt. Compared to existing literature on portfolio construction and asset selection frequently suffers from limited scope, either by confining analyses to short time intervals or by focusing exclusively on a small group of high-performing U.S. equities (e.g., Google and Apple), it provides a broader and more representative analysis.

We accord with the China Securities Regulatory Commission (CSRC) Industry Classification for the industry-level features 𝐒∈ℝT×ds\mathbf{S}\in\mathbb{R}^{T\times d\_{s}} over TT trading days with dsd\_{s} features. We collect industry daily return and macro data including CPI, money supply and PMI, so the Macro agent facilitates comprehensive analysis in both macro and industrial perspectives.

The firm-level scoring agents, which incorporate perspectives in parallel from fundamental, technical, news, and analyst report dimensions, operate on firm-level features 𝐅∈ℝN×T×df\mathbf{F}\in\mathbb{R}^{N\times T\times d\_{f}} over TT trading days with dfd\_{f} features and NN assets. The historical price data encompass daily market observations, including opening, high, low, closing, and adjusted closing prices and trading volume. Technical indicators complement the market dynamics with Moving Average Convergence Divergence (MACD), Relative Strength Index (RSI), and Stochastic Oscillator (KDJ)—computed per asset to identify trends, momentum, and potential reversal points. We curated daily news feeds are aggregated from Google and Baidu covering the informational context about the company. Analyst reports offering professional assessments, including investor activities, legal dishonesty details and the company financial activities.

To safeguard sensitive financial information and mitigate the risk of training leakage within the backbone LLM, the firm-level features are deliberately obfuscated prior to their utilization by the scoring agents. This obfuscation process conceals key identifiers and proprietary signals embedded within the raw data, ensuring that the model does not inadvertently internalize asset-specific knowledge that could create unintended information leakage.

After collection and obfuscation, the data are transmitted directly to the agents in order to prevent distortions common in chain-based communication. Such distortions often arise when numerical values are abstracted into summaries, leading to rounding errors, omission of key figures, or even fabricated values. The proposed approach preserves data fidelity, ensuring agents receive accurate and reliable information.

### 2.2 Macro Agent: Industry-Level Filtering

From the basic stock pool, the Macro agent selects industries by integrating
macroeconomic regime signals with industry-level momentum. Building on the Merrill Lynch investment clock Merrill Lynch ([2004](https://arxiv.org/html/2510.21147v1#bib.bib36)), the industry rotation framework Grauer et al. ([1990](https://arxiv.org/html/2510.21147v1#bib.bib25)), and the documented industry momentum effect Moskowitz and Grinblatt ([1999](https://arxiv.org/html/2510.21147v1#bib.bib38)), we classify the economic cycle into four phases: *recovery*, *overheating*, *stagflation*, and *recession*. Industry allocation is determined by a combination of prevailing macroeconomic conditions and systematic industry-level momentum effects, with portfolio adjustments incorporating liquidity conditions.

We use four macroeconomic indicators:

* •

  M1 Money Supply:
  Let
  M​1tM1\_{t}
  represent the money supply at time tt, including currency in circulation and demand deposits, measuring the most liquid components of the money supply.
* •

  M2 Money Supply:
  Let
  M​2tM2\_{t}
  represent the money supply at time tt, including M​1tM1\_{t} plus savings deposits and other near-money assets, capturing broader monetary aggregates.
* •

  CPI year-over-year growth rate:
  πtYoY=CPIt−CPIt−12CPIt−12,\pi\_{t}^{\mathrm{YoY}}=\frac{\mathrm{CPI}\_{t}-\mathrm{CPI}\_{t-12}}{\mathrm{CPI}\_{t-12}},
  measuring long-term inflation pressure.
* •

  Purchasing Managers’ Index (PMI):
  The official index PMIt\mathrm{PMI}\_{t}, where PMIt>50\mathrm{PMI}\_{t}>50 indicates expansion and
  PMIt<50\mathrm{PMI}\_{t}<50 indicates contraction.

Based on (πtYoY,PMIt)(\pi\_{t}^{\mathrm{YoY}},\mathrm{PMI}\_{t}), we classify the economy into one of the four
Merrill Lynch regimes ℛt∈{Recovery,Overheating,Stagflation,Recession}\mathcal{R}\_{t}\in\{\text{Recovery},\text{Overheating},\text{Stagflation},\text{Recession}\}:

|  |  |  |
| --- | --- | --- |
|  | ℛt={Recovery,πtYoY↓,PMIt>50,Overheating,πtYoY↑,PMIt>50,Stagflation,πtYoY↑,PMIt<50,Recession,πtYoY↓,PMIt<50.\mathcal{R}\_{t}=\begin{cases}\text{Recovery},&\pi\_{t}^{\mathrm{YoY}}\downarrow,\;\mathrm{PMI}\_{t}>50,\\ \text{Overheating},&\pi\_{t}^{\mathrm{YoY}}\uparrow,\;\mathrm{PMI}\_{t}>50,\\ \text{Stagflation},&\pi\_{t}^{\mathrm{YoY}}\uparrow,\;\mathrm{PMI}\_{t}<50,\\ \text{Recession},&\pi\_{t}^{\mathrm{YoY}}\downarrow,\;\mathrm{PMI}\_{t}<50.\\ \end{cases} |  |

We use the Purchasing Managers’ Index (PMI) rather than Gross Domestic Product (GDP) as a proxy for economic growth, as PMI is available on a monthly basis, whereas GDP is released only quarterly. This choice ensures consistency with the monthly frequency of the Consumer Price Index (CPI) and enables timely, monthly updates to our allocation decisions.

For each regime ℛt\mathcal{R}\_{t}, we assign a prior weight vector over industries:

|  |  |  |
| --- | --- | --- |
|  | wtmacro=fmacro​(ℛt,Δ​Mt),Δ​Mt=M​1t−M​1t−1M​1t−1−M​2t−M​2t−1M​2t−1,w^{\mathrm{macro}}\_{t}=f\_{\mathrm{macro}}(\mathcal{R}\_{t},\Delta M\_{t}),\qquad\Delta M\_{t}=\frac{M1\_{t}-M1\_{t-1}}{M1\_{t-1}}-\frac{M2\_{t}-M2\_{t-1}}{M2\_{t-1}}, |  |

represent the difference in growth rates between M​1tM1\_{t} and M​2tM2\_{t} at time tt, reflecting relative liquidity dynamics in the market.
The function fmacro​(⋅)f\_{\mathrm{macro}}(\cdot) encodes economic intuition from human expertise, including:

* •

  Recovery: overweight cyclical sectors (technology, industrials, consumer discretionary).
* •

  Overheating: overweight commodities, energy, materials.
* •

  Stagflation: overweight defensive sectors (utilities, staples, healthcare).
* •

  Recession: overweight bonds or defensive equities (staples, healthcare).

For industry jj, we compute multi-horizon momentum as

|  |  |  |
| --- | --- | --- |
|  | Mj,t=∑n∈𝒩wn​Rj,t(n),Rj,t(n)=Pj,t−Pj,t−nPj,t−n,M\_{j,t}=\sum\_{n\in\mathcal{N}}w\_{n}\,R\_{j,t}^{(n)},\quad R\_{j,t}^{(n)}=\frac{P\_{j,t}-P\_{j,t-n}}{P\_{j,t-n}}, |  |

where Pj,tP\_{j,t} is the index level of industry jj, and 𝒩\mathcal{N} is a set of look-back windows.
We then rank industries by Mj,tM\_{j,t} for each horizon nn, select the top-mm industries, and
assign them equal weights:

|  |  |  |
| --- | --- | --- |
|  | wj,tmom={1m,j∈arg⊤m{Mj,t}j=1J,0,otherwise.w^{\mathrm{mom}}\_{j,t}=\begin{cases}\frac{1}{m},&j\in\arg\top\_{m}\{M\_{j,t}\}\_{j=1}^{J},\\ 0,&\text{otherwise}.\end{cases} |  |

The final allocation combines macro-cycle weights and momentum-based weights as:

|  |  |  |
| --- | --- | --- |
|  | wj,tindustry=λ​wj,tmacro+(1−λ)​wj,tmom,w^{\mathrm{industry}}\_{j,t}=\lambda\,w^{\mathrm{macro}}\_{j,t}+(1-\lambda)\,w^{\mathrm{mom}}\_{j,t}, |  |

where λ∈[0,1]\lambda\in[0,1] controls the relative emphasis on macro regime alignment versus industry momentum.

The reduced stock pool is then defined as

|  |  |  |
| --- | --- | --- |
|  | 𝒮tind={i∈𝒮tCSI|industry​(i)∈arg⊤mwj,tfinal}.\mathcal{S}\_{t}^{\mathrm{ind}}=\bigl\{\,i\in\mathcal{S}\_{t}^{\mathrm{CSI}}\;\big|\;\text{industry}(i)\in\arg\top\_{m}w^{\mathrm{final}}\_{j,t}\,\}. |  |

### 2.3 Firm-Level Multi-Agent Scoring

Within the reduced stock pool 𝒮tind\mathcal{S}\_{t}^{\mathrm{ind}}, we evaluate individual stocks using a set of four specialized agents, 𝒜={Fundamental,Technical,News,Report}\mathcal{A}=\{\mathrm{Fundamental},\mathrm{Technical},\mathrm{News},\mathrm{Report}\}. These agents leverage firm-level features to assess the investment potential of each stock and construct an optimized portfolio. For each agent a∈𝒜a\in\mathcal{A}, let X(a)∈ℝn×T×daX^{(a)}\in\mathbb{R}^{n\times T\times d\_{a}} denote the panel of features, and fϕaf\_{\phi\_{a}} the scoring function. Each stock ii receives an agent-specific score:

|  |  |  |
| --- | --- | --- |
|  | zt,i(a)=fϕa​(Xi,t−n:t(a)),i∈𝒮tind.z^{(a)}\_{t,i}=f\_{\phi\_{a}}(X^{(a)}\_{i,t-n:t}),\qquad i\in\mathcal{S}\_{t}^{\mathrm{ind}}. |  |

where Xi,t−n:t(a)X^{(a)}\_{i,t-n:t} represents the panel of features for asset ii over the time window from t−nt-n to tt. The temporal horizon nn varies by agent type: the Fundamental agent requires extensive financial data spanning up to five years to capture long-term trends, while the News agent utilizes a shorter horizon of one month to reflect recent sentiment dynamics.

We then collect all agent scores into

|  |  |  |
| --- | --- | --- |
|  | zt,i=[zt,i(a)]a∈𝒜∈ℝ|𝒜|.z\_{t,i}=\big[z^{(a)}\_{t,i}\big]\_{a\in\mathcal{A}}\in\mathbb{R}^{|\mathcal{A}|}. |  |

#### 2.3.1 Fundamental Agent

The agent analyzes accounting and financial statement data to evaluate the overall financial health, operating efficiency, management quality, intrinsic value, and innovation-driven growth potential of firms. Key variables include return on equity (ROE), net profit, revenue, and the asset-to-debt ratio.
By integrating these metrics, the Fundamental agent provides a score reflecting long-term value creation and the sustainability of firms.

#### 2.3.2 Technical Agent

This agent evaluates stocks based on their historical price and volume data to identify strong technical signals.
It synthesizes dynamic features across multiple temporal horizons, thereby capturing short-term, medium-term, and cross-sectional price dynamics. The indicators include:

1. (i)

   Momentum: Utilizes sustained price trends via indicators like the Exponential Moving Average (EMA).
2. (ii)

   Mean Reversion: Identifies price deviations using the Relative Strength Index (RSI).
3. (iii)

   Volatility: Uses volatility measures such as the Average True Range (ATR).
4. (iv)

   Statistical Arbitrage: Applies quantitative indicators, e.g., Bollinger Bands, Average Directional Index (ADX), and Hurst exponent.

Through a weighted ensemble of these signals, the Technical agent generates a composite score reflecting the relative trading attractiveness of each stock.

#### 2.3.3 News Agent

The News agent functions as a sentiment analyst, focusing on media and news feeds. It analyzes recent news articles for each stock to gauge sentiment intensity. It fetches news data from Baidu and Google and uses the LLM to summarize sentiment. The agent’s reasoning includes identifying dominant news themes for the stock and any signals arising from news. By providing the LLM with an updated working memory that includes current volatility, it generates a sentiment polarity score st,inewss^{\mathrm{news}}\_{t,i}, which quantifies market perception:

|  |  |  |
| --- | --- | --- |
|  | zt,inews=fLLM​(News Articlesi,1:t).z^{\mathrm{news}}\_{t,i}=f\_{\mathrm{LLM}}(\text{News Articles}\_{i,1:t}). |  |

The agent evaluates whether positive or negative media narratives are likely to affect near-term stock performance.

#### 2.3.4 Report Agent

This agent acts as a specialist in fundamental disclosures and analyst reports. It analyzes the reports from five areas: Investor Research and Inquiry Records, Legal Enforcement and Dishonesty Details, Company Financial Performance Analysis, Stock Distribution Plans and Institutional Investor Holding Proportions for each company. From these, it computes composite scores zreportz^{\mathrm{report}} including the analyst interest level, integrity risk, sentiment score of company management, dividend policy quality, and institutional confidence.:

|  |  |  |
| --- | --- | --- |
|  | zt,ireport=fLLM​(Reportsi,1:t),z^{\mathrm{report}}\_{t,i}=f\_{\mathrm{LLM}}(\text{Reports}\_{i,1:t}), |  |

thereby capturing institutional sentiment and professional investor expectations.

### 2.4 Portfolio Agent: Reinforcement Learning for Portfolio Management

We utilize RL to integrate signals from fundamental, technical, news, and reports agents for portfolio optimization. By allocating weights across these agents, the RL aims to maximize expected returns. It incorporates state features, such as performance rankings and return histories, and optimizes actions by simulating diverse potential allocations. The agent’s policy is refined through Proximal Policy Optimization (PPO) with action simulation and behavioral cloning, enhancing both stability and convergence in volatile markets.

The final portfolio 𝒫t\mathcal{P}\_{t} is constructed by reweighting the scores from each agent for each stock into scores:

|  |  |  |
| --- | --- | --- |
|  | 𝒫​t={ρ​(zt,i,𝐰ti​n​d​u​s​t​r​y,𝐰ta​g​e​n​t):i∈𝒮tind}\mathcal{P}t=\Big\{{\rho(z\_{t,i},\mathbf{w}^{industry}\_{t},\mathbf{w}^{agent}\_{t}):i\in\mathcal{S}\_{t}^{\mathrm{ind}}}\Big\} |  |

where ρ​(zt,i,𝐰ti​n​d​u​s​t​r​y,𝐰ta​g​e​n​t)\rho(z\_{t,i},\mathbf{w}^{industry}\_{t},\mathbf{w}^{agent}\_{t}) represents the aggregated score of stock ii obtained using the industry and agent weights 𝐰ti​n​d​u​s​t​r​y\mathbf{w}^{industry}\_{t}, 𝐰ta​g​e​n​t\mathbf{w}^{agent}\_{t}. The generation of agent weight is formalized as an RL problem. At each trading day tt, the RL allocates weights of the fundamental, technical, news-sentiment and report analysis LLM agents. The environment evolves as
st+1∼𝒫(⋅∣st,𝐰ta​g​e​n​t),s\_{t+1}\sim\mathcal{P}(\cdot\mid s\_{t},\mathbf{w}^{agent}\_{t}),
Driven by next-day market data. The objective is to identify the subset of agents with the portfolio with the highest return:

|  |  |  |
| --- | --- | --- |
|  | πθ∗=arg⁡maxπθ⁡[∑t=1∞γt−1​rt​(st,πθ​(st))]=arg⁡maxπθ⁡Q​(st,πθ​(st))\pi^{\*}\_{\theta}=\arg\max\_{\pi\_{\theta}}\left[\sum\_{t=1}^{\infty}\gamma^{t-1}r\_{t}(s\_{t},\pi\_{\theta}(s\_{t}))\right]=\arg\max\_{\pi\_{\theta}}Q\left(s\_{t},\pi\_{\theta}(s\_{t})\right) |  |

with discount factor γ\gamma. Without considering the cost of changing the portfolio, the objective can be viewed as maximizing the return of the next trading day, so the discount factor is set to be close to zero. Considering the noisy reward function and nonstationary environment, a critic that learns the expected immediate reward is proposed to improve the efficiency of the policy gradient.

State st=[xt(a):a∈𝒜]∈𝒮s\_{t}=\big[x\_{t}^{(a)}:a\in\mathcal{A}\big]\in\mathcal{S},
where each xta∈𝒜x^{a\in\mathcal{A}}\_{t} encodes the trading returns of NN trading days ri,t−1:t−Nr\_{i,t-1:t-N}, similar to Ye et al. ([2020](https://arxiv.org/html/2510.21147v1#bib.bib53)), we augmented the state for RL to select the top-k agents, the relative frequency of agent ii being top-k over a sliding window, last action weight wt−1(a)w\_{t-1}^{(a)} and a reference weighting decision wt(a)​r​e​fw\_{t}^{(a)\;ref}.
wt(a)​r​e​fw\_{t}^{(a)\;ref} is formed as the allocation weights across the agents on a rolling basis and determined using K-means clustering. Following modern portfolio theory, the weights
are optimized to maximize the expected Sharpe ratio of the resulting portfolio:

|  |  |  |
| --- | --- | --- |
|  | 𝐰tr​e​f⁣⋆=arg⁡max𝐰tr​e​f⁡𝔼τ≤t​[Rτ​(𝐰tr​e​f,Y(k))]−rfVarτ≤t​[Rτ​(𝐰tr​e​f,Y(k))],\mathbf{w}\_{t}^{ref\star}=\arg\max\_{\mathbf{w}^{ref}\_{t}}\;\frac{\mathbb{E}\_{\tau\leq t}[R\_{\tau}(\mathbf{w}^{ref}\_{t},Y^{(k)})]-r\_{f}}{\sqrt{\mathrm{Var}\_{\tau\leq t}[R\_{\tau}(\mathbf{w}^{ref}\_{t},Y^{(k)})]}}, |  |

where rfr\_{f} denote the (constant) risk-free rate and Rτ​(𝐰tr​e​f,Y(k))R\_{\tau}(\mathbf{w}^{ref}\_{t},Y^{(k)}) denotes the realized return of the portfolio at time τ\tau formed by
combining the four-agent signals with weights 𝐰tr​e​f\mathbf{w}^{ref}\_{t}.

Action at∈𝒜a\_{t}\in\mathcal{A} corresponds to portfolio weights across agents and is generated as a pair of weight vectors:

|  |  |  |
| --- | --- | --- |
|  | 𝐰~ta​g​e​n​t=softmax​(πθ​(st)/τ)𝐰ta​g​e​n​t=Normalize​(TopK⁡(𝐰~ta​g​e​n​t+βr​e​f​𝐰tr​e​f⁣⋆))\tilde{\mathbf{w}}\_{t}^{agent}=\mathrm{softmax}(\pi\_{\theta}(s\_{t})/\tau)\qquad\mathbf{w}\_{t}^{agent}=\mathrm{Normalize}\!\big(\operatorname{TopK}(\tilde{\mathbf{w}}\_{t}^{agent}+\beta\_{ref}\mathbf{w}\_{t}^{ref\star})\big) |  |

Where πθ\pi\_{\theta} the decision policy incorporated with temperature parameter τ\tau, 𝐰~ta​g​e​n​t\tilde{\mathbf{w}}\_{t}^{agent} is the raw softmax distribution, while 𝐰ta​g​e​n​t\mathbf{w}\_{t}^{agent} is the masked Top-kk allocation actually deployed in the portfolio. Both satisfy ∑a∈𝒜wt(a)=1\sum\_{a\in\mathcal{A}}w^{(a)}\_{t}=1.

Reward rt∈ℝNr\_{t}\in\mathbb{R}^{N} denote the agent rewards on day tt:

|  |  |  |
| --- | --- | --- |
|  | rt,i=λ1​(Rt​(𝐰ta​g​e​n​t)−Rtdef)r\_{t,i}\;=\;\lambda\_{1}(R\_{t}(\mathbf{w}\_{t}^{agent})-R\_{t}^{\text{def}}) |  |

with non-negative λ1\lambda\_{1}. The term respectively measures excess performance over equal-weight baseline Rt​(𝐰ta​g​e​n​t)−RtdefR\_{t}(\mathbf{w}\_{t}^{agent})-R\_{t}^{\text{def}}.

#### 2.4.1 Action Simulation and Behavior Cloning

In online learning, where only one state-action pair is updated each trading day, the available samples for training are limited. Inspired by Yang et al. ([2020](https://arxiv.org/html/2510.21147v1#bib.bib50)), Zhuang et al. ([2023](https://arxiv.org/html/2510.21147v1#bib.bib61)), we incorporate action simulation by generating decisions from a mixture of strategies, thereby increasing the sample size. To enhance the sampling efficiency of the Proximal Policy Optimization (PPO) algorithm using off-policy data, we apply behavioral cloning (BC) to minimize the discrepancy between the behavior policy and the current policy.

*Action simulation* explores the action space by generating multiple potential actions for each trading day. These strategies are designed to explore a diverse set of potential allocations: expert weight, specific weight, uniformly sampled weight and current weight. These four types of action distributions are the expert actions from the previous days, a constant weight from the previous observations leading to the highest return, the weight sampled from a uniform distribution for exploring the action space and the weight from the current policy respectively. Candidate actions are evaluated in the environment, and their outcomes are stored in a replay buffer.

*Behavioral cloning* is a supervised learning technique used to encourage the agent to mimic expert actions during training Shafiullah et al. ([2022](https://arxiv.org/html/2510.21147v1#bib.bib45)), Florence et al. ([2022](https://arxiv.org/html/2510.21147v1#bib.bib21)). The expert action is generated from the return by rank the top-k agent returns and reweighted with the sum of one. The BC loss combines mean-squared error (MSE) and cross-entropy (CE):

|  |  |  |
| --- | --- | --- |
|  | LBC=MSE​(𝐰maskpred,𝐰maskexpert)⏟matching sparse allocations+12​CE​(𝐰maskexpert,𝐰maskpred)⏟target-as-weights cross-entropyL\_{\text{BC}}=\underbrace{\mathrm{MSE}\big(\mathbf{w}^{\text{pred}}\_{\text{mask}},\mathbf{w}^{\text{expert}}\_{\text{mask}}\big)}\_{\text{matching sparse allocations}}+\tfrac{1}{2}\underbrace{\mathrm{CE}\big(\mathbf{w}^{\text{expert}}\_{\text{mask}},\mathbf{w}^{\text{pred}}\_{\text{mask}}\big)}\_{\text{target-as-weights cross-entropy}} |  |

Algorithm 1  Single-Actor PPO with Critic for Portfolio Allocation

1:θ,ϕ\theta,\phi; targets θ′←θ\theta^{\prime}\!\leftarrow\!\theta, ϕ′←ϕ\phi^{\prime}\!\leftarrow\!\phi; γ\gamma, τ\tau; ϵ\epsilon; EPPOE\_{\text{PPO}}; Top-kk

2:βPPO\beta\_{\text{PPO}}, βMSE\beta\_{\text{MSE}}, βEntropy\beta\_{\text{Entropy}}, βBC\beta\_{\text{BC}}, βdecay\beta\_{\text{decay}}

3:λ1\lambda\_{1}; (αexpert,αspecific,αuniform,αcurrent)(\alpha\_{\text{expert}},\alpha\_{\text{specific}},\alpha\_{\text{uniform}},\alpha\_{\text{current}})

4:Initialize device-side buffer for (s,𝐰~a​g​e​n​t,𝐰a​g​e​n​t,r,s′,log⁡πold)(s,\tilde{\mathbf{w}}^{agent},\mathbf{w}^{agent},r,s^{\prime},\log\pi\_{\text{old}})

5:for each trading day tt do

6:  Observe st=[xt(a):a∈𝒜]s\_{t}=\big[x\_{t}^{(a)}:a\in\mathcal{A}\big]

7:  Actor: 𝐰ta​g​e​n​t=Normalize​(TopK⁡(𝐰~ta​g​e​n​t+βr​e​f​𝐰tr​e​f⁣⋆))\mathbf{w}\_{t}^{agent}=\mathrm{Normalize}\!\big(\operatorname{TopK}(\tilde{\mathbf{w}}\_{t}^{agent}+\beta\_{ref}\mathbf{w}\_{t}^{ref\star})\big)

8:  Observe rewards rt,i=λ1​Rt​(𝐰ta​g​e​n​t)r\_{t,i}=\lambda\_{1}R\_{t}(\mathbf{w}\_{t}^{agent}), next state st+1s\_{t+1}

9:  Simulate: (st,𝐰(m),rt(m),s(m)​t+1)(s\_{t},\mathbf{w}^{(m)},r\_{t}^{(m)},s^{(m)}{t+1}) using ratios (αexpert,αspecific,αuniform,αcurrent)(\alpha\_{\text{expert}},\alpha\_{\text{specific}},\alpha\_{\text{uniform}},\alpha\_{\text{current}}) with added noise 𝒩​(0,σ2)\mathcal{N}(0,\sigma^{2})

10:  for b=1:⌊buffer/batch⌋b=1:\lfloor\text{buffer}/\text{batch}\rfloor do

11:   Lcritic​(ϕ)=𝔼​[(r+γ​Qϕ′​(st+1,at+1)−Qϕ​(st,at))2]L\_{\text{critic}}(\phi)=\mathbb{E}\left[\big(r+\gamma Q\_{\phi^{\prime}}(s\_{t+1},a\_{t+1})-Q\_{\phi}(s\_{t},a\_{t})\big)^{2}\right]

12:   LPPO​(θ)=−𝔼​[min⁡(ρt​At,clip​(ρt,1−ϵ,1+ϵ)​At)]L\_{\text{PPO}}(\theta)=-\mathbb{E}\left[\min\big(\rho\_{t}A\_{t},\mathrm{clip}(\rho\_{t},1-\epsilon,1+\epsilon)A\_{t}\big)\right]

13:   Lactor=βPPO​LPPO+βMSE​MSE​(𝐰maskpred,𝐰maskbatch)+βEntropy​H​(𝐰~)+βBC​LBCL\_{\text{actor}}=\beta\_{\text{PPO}}L\_{\text{PPO}}+\beta\_{\text{MSE}}\,\mathrm{MSE}\big(\mathbf{w}^{\text{pred}}\_{\text{mask}},\mathbf{w}^{\text{batch}}\_{\text{mask}}\big)+\beta\_{\text{Entropy}}\,H(\tilde{\mathbf{w}})+\beta\_{\text{BC}}L\_{\text{BC}}

14: Update θ←θ−ηactor​∇θLactor\theta\leftarrow\theta-\eta\_{\text{actor}}\nabla\_{\theta}L\_{\text{actor}}

15:  end for

16:  Target updates: θ′←τ​θ+(1−τ)​θ′\theta^{\prime}\leftarrow\tau\theta+(1-\tau)\theta^{\prime}, ϕ′←τ​ϕ+(1−τ)​ϕ′\phi^{\prime}\leftarrow\tau\phi+(1-\tau)\phi^{\prime}

17:end for

#### 2.4.2 Value Function and Policy Gradient

The training process is built around the actor–critic paradigm with Proximal Policy Optimization (PPO).

The *critic* is trained to predict the value function Qϕ​(st,at)Q\_{\phi}(s\_{t},a\_{t}), which represents expected returns from state sts\_{t}. It is optimized by minimizing:

|  |  |  |
| --- | --- | --- |
|  | Lcritic​(ϕ)=𝔼t​[(rt+γ​Qϕ​(st+1,at+1)−Qϕ​(st,at))2].L\_{\text{critic}}(\phi)=\mathbb{E}\_{t}\left[\left(r\_{t}+\gamma Q\_{\phi}\left(s\_{t+1},a\_{t+1}\right)-Q\_{\phi}\left(s\_{t},a\_{t}\right)\right)^{2}\right]. |  |

The *actor* updates its policy πθ​(a|s)\pi\_{\theta}(a|s) using the PPO clipped surrogate loss:

|  |  |  |
| --- | --- | --- |
|  | LPPO​(θ)=𝔼t​[min⁡(ρt​At,clip​(ρt,1−ϵ,1+ϵ)​At)],L\_{\text{PPO}}(\theta)=\mathbb{E}\_{t}\left[\min\left(\rho\_{t}A\_{t},\;\mathrm{clip}(\rho\_{t},1-\epsilon,1+\epsilon)A\_{t}\right)\right], |  |

where: ρt=πθ​(at|st)πθold​(at|st)\rho\_{t}=\frac{\pi\_{\theta}(a\_{t}|s\_{t})}{\pi\_{\theta\_{\text{old}}}(a\_{t}|s\_{t})} is the probability ratio between the new and old policies,
AtA\_{t}:

|  |  |  |
| --- | --- | --- |
|  | At=rt+γ​Qϕ​(st+1,at+1)−Qϕ​(st,at),A\_{t}=r\_{t}+\gamma Q\_{\phi}(s\_{t+1},a\_{t+1})-Q\_{\phi}(s\_{t},a\_{t}), |  |

where Vϕ​(st)V\_{\phi}(s\_{t}) is the value function learned by the critic, and rtr\_{t} is the reward at time tt.

The actor’s total loss integrates PPO, imitation, and entropy regularization:

|  |  |  |
| --- | --- | --- |
|  | Lactor=βP​P​O​LPPO+βM​S​E​MSE​(𝐰maskpred,𝐰maskbatch)+βE​n​t​r​o​p​y​H​(𝐰~)+βB​C​LBCL\_{\text{actor}}=\beta\_{PPO}L\_{\text{PPO}}+\beta\_{MSE}\,\mathrm{MSE}(\mathbf{w}^{\text{pred}}\_{\text{mask}},\mathbf{w}^{\text{batch}}\_{\text{mask}})+\beta\_{Entropy}\,H(\tilde{\mathbf{w}})+\beta\_{\!BC}L\_{\text{BC}} |  |

Performance is evaluated out-of-sample by applying the learned policy to the next day’s returns, typically using closing prices. After the market is closed, the agent is trained using the updated data and decides the weight allocation for the next day. This ensures the model is trained on historical information while tested on unseen market dynamics.

### 2.5 Risk Control Agent

To further investigate the risk-neutral performance of our model, we design a risk scaling agent. Specifically, IF contracts can be traded on the China Financial Futures Exchange as a hedging instrument. This agent manages portfolio exposure by dynamically adjusting positions in response to market volatility. It implements a risk scaling algorithm, which reduces positions when market volatility is extreme and gradually increases them when volatility is moderate (up to a maximum scale of 1).

Specifically, after portfolio construction, the weight of the assets can be generated:

|  |  |  |
| --- | --- | --- |
|  | 𝐩t=fθ​(𝐅:,1:t,:,𝐒1:t,:,𝐁1:t,:),𝐩t∈ℝN,𝟏⊤​𝐩t=1,𝐩t⪰𝟎,\mathbf{p}\_{t}\;=\;f\_{\theta}\!\big(\,\mathbf{F}\_{:,1:t,:},\,\mathbf{S}\_{1:t,:},\,\mathbf{B}\_{1:t,:}\big),\qquad\mathbf{p}\_{t}\in\mathbb{R}^{N},\qquad\mathbf{1}^{\top}\mathbf{p}\_{t}=1,\qquad\mathbf{p}\_{t}\succeq\mathbf{0}, |  |

where fθ​(⋅)f\_{\theta}(\cdot) is a parameterized allocation rule that maps information up to time tt to weights and θ\theta denotes learnable parameters and the nonnegativity enforces long-only allocations.

The Risk Control agent scales exposure dynamically to stabilize portfolio volatility around a pre-specified target level σtgt\sigma\_{\mathrm{tgt}}. Following Zhang et al. ([2019](https://arxiv.org/html/2510.21147v1#bib.bib58)), the scaling factor is defined as

|  |  |  |
| --- | --- | --- |
|  | βt=σtgtσ^t−1,σ^t−12=(1−λ)​∑j=1nλj−1​rt−j2,0<λ<1,\beta\_{t}=\frac{\sigma\_{\mathrm{tgt}}}{\widehat{\sigma}\_{t-1}},\qquad\widehat{\sigma}\_{t-1}^{2}=(1-\lambda)\sum\_{j=1}^{n}\lambda^{\,j-1}r\_{t-j}^{2},\qquad 0<\lambda<1, |  |

where σ^t−1\widehat{\sigma}\_{t-1} is the estimated market volatility at time t−1t-1.
The volatility estimate is computed using an exponentially weighted moving standard deviation of past
returns rtr\_{t} over an nn-day window with λ\lambda being the decay factor.

The final tradable portfolio weights are therefore given by

|  |  |  |
| --- | --- | --- |
|  | 𝐩~t=βt​𝐩t=βt​fθ​(𝐅:,1:t,:,𝐒1:t,:,𝐁1:t,:)\tilde{\mathbf{p}}\_{t}=\beta\_{t}\,\mathbf{p}\_{t}=\beta\_{t}\,f\_{\theta}\!\big(\,\mathbf{F}\_{:,1:t,:},\,\mathbf{S}\_{1:t,:},\,\mathbf{B}\_{1:t,:}\big) |  |

providing a volatility-targeting adjustment, ensuring that position sizes are adaptively scaled—expanded (up to full allocation) in tranquil market conditions and contracted under heightened volatility—thereby improving Sharpe ratio and Calmar ratio.

## 3 Experiments

This section delineates the experimental framework used to assess the performance of our multi-agent trading system. It provides an exposition of the baseline models, LLM configurations, and evaluation metrics utilized to ensure a robust and systematic analysis of the system’s efficacy.

### 3.1 Experimental Setup

We use Qwen3-32B as the foundational LLM as agents’ reasoning core. Recognizing that pretrained models may contain implicit knowledge of financial markets, we obfuscate industry & company identifiers before submission to the model in order to prevent information leakage. To prevent look-ahead bias, agents’ decisions on trading day TT are generated exclusively from masked inputs observed up to day T−1T-1. The outputs are aggregated by a portfolio manager, who proposes the preliminary asset allocation. This allocation is then processed by a dedicated risk manager agent, which incorporates recent volatility dynamics to adjust exposures, thereby aligning the portfolio with risk-control objectives.

##### Training and testing protocol.

We assess the proposed framework through backtesting simulation conducted over the period from January 1, 2019, to December 31, 2024, using the CSI 300 constituent stock pool. We split the data into training and testing periods: from 2019-01-01 to 2023-12-31 as the training period and from 2024-01-01 to 2024-12-31 as the testing period.

In the training period, parameter search is conducted for each agent independently. For each firm-level agent (fundamental, technical, report, and news), we design a time-series optimizer that leverages arbitrage principles to produce daily trading signals, compensating for the low update frequency of financial, news, and report data. Parameter search is carried out within each optimizer. For agent aa,
parameters ϕa\phi\_{a} are optimized to maximize its standalone annualized Sharpe ratio:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕa⋆=arg⁡maxϕa⁡𝔼t​[Rt(a)​(ϕa,Y(k))]−rfVart​[Rt(a)​(ϕa,Y(k))],\phi\_{a}^{\star}=\arg\max\_{\phi\_{a}}\;\frac{\mathbb{E}\_{t}\!\left[R^{(a)}\_{t}(\phi\_{a},Y^{(k)})\right]-r\_{f}}{\sqrt{\mathrm{Var}\_{t}\!\left[R^{(a)}\_{t}(\phi\_{a},Y^{(k)})\right]}}, |  | (1) |

where Rt(a)R^{(a)}\_{t} is the realized portfolio return constructed solely from agent aa’s scores.
The optimized parameters ϕa⋆\phi\_{a}^{\star} are then fixed and directly applied to the testing period
without re-estimation.

### 3.2 Benchmark

To assess the efficacy of our system, we conduct analysis against a range of established baselines across multiple categories. These include conventional proxy indicators—specifically, MACD (Lim et al. [2020](https://arxiv.org/html/2510.21147v1#bib.bib31)), KDJ, RSI, sign(R) (Moskowitz et al. [2012](https://arxiv.org/html/2510.21147v1#bib.bib39)), and SMA—as well as the MASS framework (Guo et al. [2025](https://arxiv.org/html/2510.21147v1#bib.bib26)). Below we introduce a detailed list of benchmarks:

1. (i)

   MASS (Multi-Agent Simulation Scaling for Portfolio Construction): MASS (Guo et al. [2025](https://arxiv.org/html/2510.21147v1#bib.bib26)) is a framework that leverages large-scale collaborative agents to systematically construct and optimize investment portfolios.
2. (ii)

   CSI 300: The CSI 300 Index is a capitalization-weighted stock market index designed to reflect the performance of the top 300 stocks listed on the Shanghai and Shenzhen stock exchanges. It covers a diverse range of industries and serves as a key benchmark for the Chinese A-share market.
3. (iii)

   SMA (Simple Moving Average): This trend-following strategy generates signals from crossovers of a 5-period short-term SMA and a 10-period long-term SMA.
4. (iv)

   RSI (Relative Strength Index): RSI measures price momentum over a 10-period look-back, entering long positions when RSI < 30 (oversold) and closing when RSI > 70 (overbought).
5. (v)

   Sign: This strategy focus only on the sign of the past 20 days return, triggering buy signals when sign(20) > 0 and sell signals when sign(20) < 0.
6. (vi)

   KDJ: This stochastic oscillator uses a 9-period look-back to generate trading signals based on K and D line crossovers, with the J line confirming momentum.
7. (vii)

   MACD (Moving Average Convergence Divergence): This trend-following strategy uses a fast EMA (12 periods), slow EMA (26 periods), and signal line (9 periods) to generate buy/sell signals based on MACD-signal line crossovers.

System performance is quantified using eight key metrics: Cumulative Return (CR), Annualized Return (AR), Annualized Standard Deviation (STD), Downside Deviation (DD) (Ang et al. [2006](https://arxiv.org/html/2510.21147v1#bib.bib2)), Sharpe Ratio (Sharpe [1994](https://arxiv.org/html/2510.21147v1#bib.bib46)), Sortino Ratio (Rollinger and Hoffman [2013](https://arxiv.org/html/2510.21147v1#bib.bib44)), Maximum Drawdown (MDD), and Calmar Ratio (Young [1991](https://arxiv.org/html/2510.21147v1#bib.bib54)). The precise formulations for these metrics are detailed in the e-companion.

Figure 1: Backtesting Results Compared with Baseline Strategies and the CSI 300 Index (Training Sample) (a) Cumulative Returns, (b) Excess Returns Relative to the CSI 300 Index

![Refer to caption](figures/Long_only_training.png)


(a)

![Refer to caption](figures/alpha_training.png)


(b)



\TABLE

Performance in Training Sample

Strategy
CR (%) ↑\uparrow
AR (%) ↑\uparrow
STD (%) ↑\uparrow
DD (%) ↑\uparrow
Sharpe ↑\uparrow
Sortino ↑\uparrow
MDD (%) ↓\downarrow
Calmar ↑\uparrow


SMA
-1.06
-0.21
13.05
9.03
-0.02
-0.02
-46.50
-0.01

RSI
18.61
3.72
13.41
9.61
0.28
0.39
-28.48
0.13

SIGN
17.93
3.59
13.39
9.31
0.27
0.39
-28.82
0.12

KDJ
23.33
4.67
8.23
4.77
0.57
0.98
-17.89
0.26

MACD
24.93
4.99
12.97
8.61
0.38
0.58
-39.41
0.13

Ours
167.52
34.77
18.94
11.41
1.84
3.05
-24.58
1.42



\TABLE

Performance of Excess Returns in Training Sample

Strategy
CR (%) ↑\uparrow
AR (%) ↑\uparrow
STD (%) ↑\uparrow
DD (%) ↓\downarrow
Sharpe ↑\uparrow
Sortino ↑\uparrow
MDD (%) ↑\uparrow
Calmar ↑\uparrow


SMA\_alpha
-23.11
-4.62
14.20
9.85
-0.33
-0.47
-50.55
-0.09

RSI\_alpha
-3.44
-0.69
13.86
9.91
-0.05
-0.07
-49.69
-0.01

SIGN\_alpha
-4.12
-0.82
13.88
9.64
-0.06
-0.09
-29.35
-0.03

KDJ\_alpha
1.28
0.26
17.44
11.86
0.01
0.02
-43.87
0.01

MACD\_alpha
2.88
0.58
14.28
9.57
0.04
0.06
-35.31
0.02

Ours\_alpha
146.10
30.33
16.57
10.07
1.83
3.01
-16.49
1.84




Figure 2: Backtesting Results Compared with Baseline Strategies and the CSI 300 Index (Testing Sample) (a) Cumulative Returns, (b) Excess Returns Relative to the CSI 300 Index

![Refer to caption](figures/Long_only_testing.png)


(a)

![Refer to caption](figures/alpha_testing.png)


(b)



\TABLE

Performance in Testing Sample

Strategy
CR (%) ↑\uparrow
AR (%) ↑\uparrow
STD (%) ↑\uparrow
DD (%) ↑\uparrow
Sharpe ↑\uparrow
Sortino ↑\uparrow
MDD (%) ↓\downarrow
Calmar ↑\uparrow


SMA
-1.53
-1.53
17.68
10.95
-0.09
-0.14
-17.09
-0.09

RSI
0.64
0.64
11.80
7.42
0.05
0.09
-8.64
0.07

SIGN
16.53
16.53
17.98
10.66
0.92
1.55
-11.89
1.39

KDJ
11.91
11.91
15.34
8.54
0.78
1.40
-9.14
1.30

MACD
10.84
10.84
18.19
10.66
0.60
1.02
-11.84
0.92

MASS
7.01
7.01
21.79
14.57
0.32
0.48
-20.41
0.34

Ours
55.41
55.41
28.20
14.90
1.96
3.72
-12.52
4.43



\TABLE

Performance of Excess Returns in Testing Sample

Strategy
CR (%) ↑\uparrow
AR (%) ↑\uparrow
STD (%) ↓\downarrow
DD (%) ↓\downarrow
Sharpe ↑\uparrow
Sortino ↑\uparrow
MDD (%) ↑\uparrow
Calmar ↑\uparrow


SMA\_alpha
-17.40
-17.40
11.94
10.09
-1.46
-1.72
-19.41
-0.90

RSI\_alpha
-15.23
-15.23
17.79
14.51
-0.86
-1.05
-24.94
-0.61

SIGN\_alpha
0.66
0.66
11.49
9.15
0.06
0.07
-12.20
0.05

KDJ\_alpha
-3.96
-3.96
14.85
11.48
-0.27
-0.35
-15.12
-0.26

MACD\_alpha
-5.03
-5.03
11.18
8.77
-0.45
-0.57
-7.43
-0.68

MASS\_alpha
-10.16
-10.16
12.04
9.11
-0.84
-1.12
-21.66
-0.47

Ours\_alpha
39.22
39.22
17.60
10.56
2.23
3.71
-6.44
6.09

### 3.3 Main Results

In contrast to existing multi-agent frameworks, such as MASS, which relies on rule-based optimization without incorporating risk scaling, our proposed system exhibits superior performance.

Figure [1(a)](https://arxiv.org/html/2510.21147v1#S3.F1.sf1 "In Figure 1 ‣ 3.2 Benchmark ‣ 3 Experiments") and Table [3.2](https://arxiv.org/html/2510.21147v1#S3.SS2 "3.2 Benchmark ‣ 3 Experiments") show that our framework consistently outperforms benchmark models in the training period. It achieves a cumulative return (CR) of 167.52%, a Sharpe ratio (SR) of 1.84, a Sortino ratio of 3.05, and a Calmar ratio of 1.42. For excess returns, the system records a cumulative return of 146.10%, with SR, Sortino, and Calmar ratios of 1.83, 3.01, and 1.84, respectively. Compared with both traditional methods (RSI and KDJ) and multi-agent systems such as MASS, ContestTrade demonstrates stronger profitability and improved risk-adjusted performance, confirming the efficacy of its competitive multi-agent design.

The framework also exhibits strong out-of-sample generalization. As presented in Figure [2(a)](https://arxiv.org/html/2510.21147v1#S3.F2.sf1 "In Figure 2 ‣ 3.2 Benchmark ‣ 3 Experiments") and Table [3.2](https://arxiv.org/html/2510.21147v1#S3.SS2 "3.2 Benchmark ‣ 3 Experiments"), it yields a cumulative return of 55.41% in the testing period, outperforming the best baseline by 38.88

As evidenced in Figure [2(b)](https://arxiv.org/html/2510.21147v1#S3.F2.sf2 "In Figure 2 ‣ 3.2 Benchmark ‣ 3 Experiments") and Table [3.2](https://arxiv.org/html/2510.21147v1#S3.SS2 "3.2 Benchmark ‣ 3 Experiments"), our framework demonstrates robust efficacy, consistently achieving enhanced risk-adjusted returns and reduced volatility relative to baseline strategies.

\FIGURE![[Uncaptioned image]](figures/Ablation.png)

Comparative Performance of the Full Model and Ablated Configurations Over Time
“w/o” indicates removing the specified configuration.



\TABLE

Ablation Study of Model Performance

Model
CR (%) ↑\uparrow
AR (%) ↑\uparrow
STD (%) ↑\uparrow
DD (%) ↑\uparrow
Sharpe ↑\uparrow
Sortino ↑\uparrow
MDD (%) ↓\downarrow
Calmar ↑\uparrow


Full Model
185.33
32.08
16.75
10.15
1.92
3.16
-16.49
1.95

w/o Risk Scaling
190.27
32.93
18.05
11.10
1.82
2.97
-16.49
2.00

w/o Combine Opt.
98.56
17.06
13.72
8.94
1.24
1.91
-13.23
1.29

w/o Text Process
143.36
24.81
16.57
10.57
1.50
2.35
-17.16
1.45

w/o Structured Data
87.87
15.21
19.57
12.24
0.78
1.24
-27.81
0.55

w/o All
14.36
2.49
4.99
3.45
0.50
0.72
-13.83
0.18

### 3.4 Ablation Configurations

To rigorously evaluate the contributions of individual components within our AI-based fundamental investing framework, we conduct an ablation study by systematically disabling key modules.

1. (i)

   Without Risk Scaling.
   In this configuration, the risk scaling mechanism is deactivated, resulting in a portfolio without volatility control. This setup isolates the role of risk management in improving the Sortino Ratio and reducing maximum drawdown, highlighting its effectiveness in stabilizing returns.
2. (ii)

   Without Combined Optimization.
   The combined optimization module is excluded, and final trading signals are equally weighted across all assets. This configuration evaluates the incremental benefits of the optimization process in enhancing portfolio performance metrics, such as risk-adjusted returns.
3. (iii)

   Without Text Processing (Remove News and Report agents).
   The text-processing modules, including the Report and News agents, are removed, thereby eliminating the framework’s ability to incorporate textual information. This ablation assesses the value of qualitative data in informing investment decisions.
4. (iv)

   Without Structured Data (Remove Fundamental and Technical agents).
   In this setting, the framework relies exclusively on news and report agents, omitting signals derived from the Fundamental agent and the Technical agent. This configuration quantifies the contribution of structured data to the framework’s predictive accuracy.
5. (v)

   Without All Components.
   All key components—risk scaling, combined optimization, text processing, and structured data—are disabled, resulting in a baseline portfolio that equally weights all constituents of the CSI 300 index. This setup serves as a control, illustrating the collective impact of the proposed innovations on portfolio performance.

As evidenced by Figure [3.3](https://arxiv.org/html/2510.21147v1#S3.SS3 "3.3 Main Results ‣ 3 Experiments") and Table [3.3](https://arxiv.org/html/2510.21147v1#S3.SS3 "3.3 Main Results ‣ 3 Experiments"), the ablation of any individual component substantially impairs the performance of the AI-based fundamental investing framework, with the complete removal of all components resulting in severe degradation of portfolio outcomes. This underscores the critical and synergistic role of each module in achieving optimal results.

## 4 Conclusion

In this paper,
we proposed a hierarchical AI multi-agent framework for fundamental equity investing.
The framework organizes the investment process along a macro–industry–firm path and implements it with a coordinated set of agents. It builds equity portfolios from firm fundamentals and runs a systematic trading workflow that combines fundamental signals, technical timing, sentiment inputs, portfolio optimization, and risk scaling.

The framework integrates specialized agents for research, portfolio construction, and risk control, which supports adaptability and robustness in China’s volatile A-share market. It delivers a unified analysis across financial, technical, and sentiment dimensions. In empirical tests, the system outperforms standard benchmarks and non-hierarchical multi-agent baselines on key metrics, delivering higher cumulative returns, stronger risk-adjusted performance, and lower downside risk.

Future work includes extending the framework to multiple asset classes and international markets to assess robustness across market regimes. Another direction is adding human-in-the-loop oversight so expert judgment can complement algorithmic decisions.

## References

* Alsabah et al. (2021)

  Alsabah H, Capponi A, Ruiz Lacedelli O, Stern M (2021) Robo-advising: Learning investors’ risk preferences via portfolio choices. *Journal of Financial Econometrics* 19(2):369–392.
* Ang et al. (2006)

  Ang A, Chen J, Xing Y (2006) Downside risk. *Review of Financial Studies* 19(4):1191–1239.
* Badarinza et al. (2016)

  Badarinza C, Campbell JY, Ramadorai T (2016) International comparative household finance. *Annual Review of Economics* 8(1):111–144.
* Barber and Odean (2000)

  Barber BM, Odean T (2000) Trading is hazardous to your wealth: The common stock investment performance of individual investors. *Journal of Finance* 55(2):773–806.
* Baulkaran and Jain (2023)

  Baulkaran V, Jain P (2023) Who uses robo-advising and how? *Financial Review* 58(1):65–89.
* Ben-David et al. (2022)

  Ben-David I, Li J, Rossi A, Song Y (2022) What do mutual fund investors really care about? *Review of Financial Studies* 35(4):1723–1774.
* Bergstresser et al. (2008)

  Bergstresser D, Chalmers JM, Tufano P (2008) Assessing the costs and benefits of brokers in the mutual fund industry. *Review of Financial Studies* 22(10):4129–4156.
* Burke and Hung (2021)

  Burke J, Hung AA (2021) Trust and financial advice. *Journal of Pension Economics & Finance* 20(1):9–26.
* Calcagno and Monticone (2015)

  Calcagno R, Monticone C (2015) Financial literacy and the demand for financial advice. *Journal of Banking & Finance* 50:363–380.
* Campbell (2006)

  Campbell JY (2006) Household finance. *Journal of Finance* 61(4):1553–1604.
* Campbell and Viceira (2002)

  Campbell JY, Viceira LM (2002) *Strategic Asset Allocation: Portfolio Choice for Long-Term Investors* (Clarendon Lectures in Economic).
* Cao et al. (2024a)

  Cao S, Jiang W, Wang J, Yang B (2024a) From man vs. machine to man + machine: The art and AI of stock analyses. *Journal of Financial Economics* 160:103910.
* Cao et al. (2024b)

  Cao Y, Chen Z, Pei Q, Dimino F, Ausiello L, Kumar P, Subbalakshmi K, Ndiaye PM (2024b) Risklabs: Predicting financial risk using large language model based on multi-sources data. URL https://arxiv.org/abs/2404.07452.
* Chalmers and Reuter (2020)

  Chalmers J, Reuter J (2020) Is conflicted investment advice better than no advice? *Journal of Financial Economics* 138(2):366–387.
* Christoffersen et al. (2013)

  Christoffersen SE, Evans R, Musto DK (2013) What do consumers’ fund flows maximize? Evidence from their brokers’ incentives. *Journal of Finance* 68(1):201–235.
* Coleman et al. (2022)

  Coleman B, Merkley K, Pacelli J (2022) Human versus machine: A comparison of robo-analyst and traditional research analyst investment recommendations. *Accounting Review* 97(5):221–244.
* De Curtò et al. (2023)

  De Curtò J, de Zarza I, Roig G, Cano JC, Manzoni P, Calafate CT (2023) LLM-informed multi-armed bandit strategies for non-stationary environments. *Electronics* 12(13):2814.
* D’Acunto et al. (2019)

  D’Acunto F, Prabhala N, Rossi AG (2019) The promises and pitfalls of robo-advising. *Review of Financial Studies* 32(5):1983–2020.
* D’Acunto and Rossi (2021)

  D’Acunto F, Rossi AG (2021) *Robo-Advising* (Springer).
* Fama and French (2002)

  Fama EF, French KR (2002) The equity premium. *Journal of Finance* 57(2):637–659.
* Florence et al. (2022)

  Florence P, Lynch C, Zeng A, Ramirez OA, Wahid A, Downs L, Wong A, Lee J, Mordatch I, Tompson J (2022) Implicit behavioral cloning. *Proceedings of the 5th Conference on Robot Learning*, 158–168 (PMLR).
* French and Poterba (1991)

  French KR, Poterba JM (1991) Investor diversification and international equity markets.
* Gargano and Rossi (2018)

  Gargano A, Rossi AG (2018) Does it pay to pay attention? *Review of Financial Studies* 31(12):4595–4649.
* Gennaioli et al. (2015)

  Gennaioli N, Shleifer A, Vishny R (2015) Money doctors. *Journal of Finance* 70(1):91–114.
* Grauer et al. (1990)

  Grauer RR, Hakansson NH, Shen FC (1990) Industry rotation in the U.S. stock market: 1934–1986 returns on passive, semi-passive, and active strategies. *Journal of Banking & Finance* 14(2–3):513–538.
* Guo et al. (2025)

  Guo T, Shen H, Huang J, Mao Z, Luo J, Chen Z, Liu X, Xia B, Liu L, Ma Y, et al. (2025) MASS: Multi-agent simulation scaling for portfolio construction. URL https://arxiv.org/abs/2505.10278.
* Hackethal et al. (2012)

  Hackethal A, Haliassos M, Jappelli T (2012) Financial advisors: A case of babysitters? *Journal of Banking & Finance* 36(2):509–524.
* Huberman (2001)

  Huberman G (2001) Familiarity breeds investment. *Review of Financial Studies* 14(3):659–680.
* Kim et al. (2019)

  Kim SD, Cotwright M, Chatterjee S (2019) Who are robo-advisor users? *Journal of Finance Issues* 18(2):33–50.
* Lachance and Tang (2012)

  Lachance ME, Tang N (2012) Financial advice and trust. *Financial Services Review* 21(3):209.
* Lim et al. (2020)

  Lim B, Zohren S, Roberts S (2020) Enhancing time series momentum strategies using deep neural networks. URL https://arxiv.org/abs/1904.04912.
* Linnainmaa et al. (2021)

  Linnainmaa JT, Melzer BT, Previtero A (2021) The misguided beliefs of financial advisors. *Journal of Finance* 76(2):587–621.
* Liu et al. (2025)

  Liu Z, Zhang X, Yang K, Xie Q, Huang J, Ananiadou S (2025) FMDLlama: Financial misinformation detection based on large language models. *Companion Proceedings of the ACM on Web Conference 2025*, 1153–1157.
* Lu et al. (2023)

  Lu D, Wu H, Liang J, Xu Y, He Q, Geng Y, Han M, Xin Y, Xiao Y (2023) BBT-Fin: Comprehensive construction of chinese financial domain pre-trained language model, corpus and benchmark. URL https://arxiv.org/abs/2302.09432.
* Markowits (1952)

  Markowits HM (1952) Portfolio selection. *Journal of Finance* 7(1):71–91.
* Merrill Lynch (2004)

  Merrill Lynch (2004) The investment clock. Research report, Merrill Lynch & Co., New York.
* Mitchell and Utkus (2004)

  Mitchell OS, Utkus SP (2004) Lessons from behavioral finance for retirement plan design. Mitchell OS, Utkus SP, eds., *Pension Design and Structure: New Lessons from Behavioral Finance*, chapter 1, 82–94 (Oxford University Press).
* Moskowitz and Grinblatt (1999)

  Moskowitz TJ, Grinblatt M (1999) Do industries explain momentum? *Journal of Finance* 54(4):1249–1290.
* Moskowitz et al. (2012)

  Moskowitz TJ, Ooi YH, Pedersen LH (2012) Time series momentum. *Journal of Financial Economics* 104(2):228–250.
* Mullainathan et al. (2012)

  Mullainathan S, Noeth M, Schoar A (2012) The market for financial advice: An audit study. URL https://ssrn.com/abstract=2028263.
* Pool et al. (2016)

  Pool VK, Sialm C, Stefanescu I (2016) It pays to set the menu: Mutual fund investment options in 401 (k) plans. *Journal of Finance* 71(4):1779–1812.
* Reher and Sokolinski (2024)

  Reher M, Sokolinski S (2024) Robo advisors and access to wealth management. *Journal of Financial Economics* 155:103829.
* Reher and Sun (2019)

  Reher M, Sun C (2019) Automated financial management: Diversification and account size flexibility. *Journal of Investment Management* 17(2):63–75.
* Rollinger and Hoffman (2013)

  Rollinger TN, Hoffman ST (2013) *Sortino: A ‘Sharper’ Ratio* (Chicago, Illinois: Red Rock Capital).
* Shafiullah et al. (2022)

  Shafiullah NM, Cui Z, Altanzaya AA, Pinto L (2022) Behavior transformers: Cloning kk modes with one stone. *Advances in Neural Information Processing Systems 35*, 22955–22968.
* Sharpe (1994)

  Sharpe WF (1994) The Sharpe ratio. *The Journal of Portfolio Management* 21(1):49–58.
* Tobin (1958)

  Tobin J (1958) Liquidity preference as behavior towards risk. *Review of Economic Studies* 25(2):65–86.
* Wang et al. (2023)

  Wang S, Yuan H, Zhou L, Ni LM, Shum HY, Guo J (2023) Alpha-GPT: Human-AI interactive alpha mining for quantitative investment. URL https://arxiv.org/abs/2308.00016.
* Xing (2025)

  Xing F (2025) Designing heterogeneous LLM agents for financial sentiment analysis. *ACM Transactions on Management Information Systems* 16(1):1–24.
* Yang et al. (2020)

  Yang H, Liu XY, Zhong S, Walid A (2020) Deep reinforcement learning for automated stock trading: An ensemble strategy. *Proceedings of the First ACM International Conference on AI in Finance*, 1–8.
* Yao et al. (2023a)

  Yao S, Yu D, Zhao J, Shafran I, Griffiths T, Cao Y, Narasimhan K (2023a) Tree of thoughts: Deliberate problem solving with large language models. *Advances in Neural Information Processing Systems 36*, 11809–11822.
* Yao et al. (2023b)

  Yao S, Zhao J, Yu D, Du N, Shafran I, Narasimhan KR, Cao Y (2023b) ReAct: Synergizing reasoning and acting in language models. *The Eleventh International Conference on Learning Representations*, URL https://openreview.net/forum?id=WE\_vluYUL-X.
* Ye et al. (2020)

  Ye Y, Pei H, Wang B, Chen PY, Zhu Y, Xiao J, Li B (2020) Reinforcement-learning based portfolio management with augmented asset movement prediction states. *Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence*, 1112–1119.
* Young (1991)

  Young T (1991) Calmar ratio: A smoother tool. *Futures* 20(8):40–41.
* Yu et al. (2025)

  Yu Y, Li H, Chen Z, Jiang Y, Li Y, Suchow JW, Zhang D, Khashanah K (2025) FinMem: A performance-enhanced LLM trading agent with layered memory and character design. *IEEE Transactions on Big Data*, forthcoming.
* Zhang et al. (2020)

  Zhang T, Li Y, Jin Y, Li J (2020) AutoAlpha: An efficient hierarchical evolutionary algorithm for mining alpha factors in quantitative investment. URL https://arxiv.org/abs/2002.08245.
* Zhang et al. (2024)

  Zhang W, Zhao L, Xia H, Sun S, Sun J, Qin M, Li X, Zhao Y, Zhao Y, Cai X, et al. (2024) A multimodal foundation agent for financial trading: Tool-augmented, diversified, and generalist. *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 4314–4325.
* Zhang et al. (2019)

  Zhang Z, Zohren S, Roberts S (2019) Deep reinforcement learning for trading. URL https://arxiv.org/abs/1911.10107.
* Zhao et al. (2024a)

  Zhao A, Huang D, Xu Q, Lin M, Liu YJ, Huang G (2024a) ExpeL: LLM agents are experiential learners. *Proceedings of the Thirty-Eighth AAAI Conference on Artificial Intelligence*, 19632–19642.
* Zhao et al. (2024b)

  Zhao H, Liu Z, Wu Z, Li Y, Yang T, Shu P, Xu S, Dai H, Zhao L, Mai G, et al. (2024b) Revolutionizing finance with LLMs: An overview of applications and insights. URL https://arxiv.org/abs/2401.11641.
* Zhuang et al. (2023)

  Zhuang Z, LEI K, Liu J, Wang D, Guo Y (2023) Behavior proximal policy optimization. *The Eleventh International Conference on Learning Representations*, URL https://openreview.net/forum?id=3c13LptpIph.

\ECSwitch

\ECHead

Supplementary Material

This supplementary material provides additional details to support the main document. It includes a high-level illustration of our framework and detailed information on dataset construction.

## 5 Performance Metrics

The performance of the portfolio is evaluated using the following metrics:

1. (i)

   Cumulative Return (CR): The total return of the portfolio over a specific period, reflecting the overall growth of the investment.
2. (ii)

   Annualized Return (AR): The average return of the portfolio per year, providing a standardized measure for comparing performance across different time frames.
3. (iii)

   Annualized Standard Deviation (STD): A measure of the portfolio’s volatility, indicating the degree of dispersion of returns around the average return.
4. (iv)

   Downside Deviation (DD): Also known as *downside risk*, this metric measures the volatility of only the negative returns. It focuses on the risk of losses, providing a more specific view of the portfolio’s exposure to adverse movements.
5. (v)

   Sharpe Ratio: A risk-adjusted measure of return, calculated as the annualized return minus the risk-free rate, divided by the annualized standard deviation. A higher Sharpe Ratio indicates a better return for a given level of risk. The formula is:

   |  |  |  |
   | --- | --- | --- |
   |  | Sharpe Ratio=A​R−RfS​T​D\text{Sharpe Ratio}=\frac{AR-R\_{f}}{STD} |  |

   where A​RAR is the annualized return, RfR\_{f} is the risk-free rate, and S​T​DSTD is the annualized standard deviation of portfolio returns. In this study, we assume the risk-free rate (RfR\_{f}) is 0.
6. (vi)

   Sortino Ratio: A variant of the Sharpe Ratio that uses downside deviation instead of total standard deviation as the risk measure. This ratio assesses the return generated per unit of downside risk. The formula is:

   |  |  |  |
   | --- | --- | --- |
   |  | Sortino Ratio=A​R−RfD​D\text{Sortino Ratio}=\frac{AR-R\_{f}}{DD} |  |

   where A​RAR is the annualized return, RfR\_{f} is the risk-free rate, and D​DDD is the annualized downside deviation of portfolio returns.
7. (vii)

   Maximum Drawdown (MDD): This metric represents the largest peak-to-trough decline in the portfolio’s value over a specified period. It shows the maximum observed loss from any peak, serving as an indicator of capital preservation risk.
8. (viii)

   Calmar Ratio: A risk-adjusted performance metric that evaluates the annualized excess return relative to the maximum drawdown, defined as:

   |  |  |  |
   | --- | --- | --- |
   |  | Calmar Ratio=A​R−Rf|M​D​D|\text{Calmar Ratio}=\frac{AR-R\_{f}}{|MDD|} |  |

   where A​RAR is the annualized return, RfR\_{f} is the risk-free rate, and |M​D​D||MDD| is the absolute value of the maximum drawdown.

## 6 Dataset Details

### 6.1 Macro-level Data Details

|  |  |
| --- | --- |
| Variable | Definition |
| CPI Year-over-Year Growth Rate | Calculated as πtYoY=CPIt−CPIt−12CPIt−12\pi\_{t}^{\mathrm{YoY}}=\frac{\mathrm{CPI}\_{t}-\mathrm{CPI}\_{t-12}}{\mathrm{CPI}\_{t-12}}, measuring long-term inflation pressure. |
| M1 Money Supply | Represents the money supply at time tt, including currency in circulation and demand deposits, measuring the most liquid components of the money supply. |
| M2 Money Supply | Represents the money supply at time tt, including M1 plus savings deposits, money market securities, and other near-money assets, capturing broader monetary aggregates. |
| Purchasing Managers’ Index (PMI) | The official index PMIt\mathrm{PMI}\_{t}, where PMIt>50\mathrm{PMI}\_{t}>50 indicates expansion and PMIt<50\mathrm{PMI}\_{t}<50 indicates contraction. |

### 6.2 Industry-level Data Details

|  |  |
| --- | --- |
| Variable | Definition |
| Industry Index Return | Daily return rates of industry index based on the industry classification codes of listed companies published by the China Securities Regulatory Commission. |

### 6.3 Firm-level Data Details

| Variable | Definition |
| --- | --- |
| Capital Expenditures (CapEx) | The money an organization or corporate entity spends to buy, maintain, or improve its fixed assets, such as buildings, vehicles, equipment, or land. |
| Cash & Cash Equivalents | Cash on hand and highly liquid short-term investments. |
| Close |  |
| Current Assets | Assets expected to be converted into cash within one year. |
| Current Liabilities | Short-term obligations due within one year. |
| Dividends paid | Cash or stock payments distributed to shareholders or holders of certain equity-based awards. |
| Earnings Before Interest & Taxes | Company’s operating profit without interest expenses and income taxes. |
| Earnings before tax | The money retained internally by a company before deducting tax expenses. |
| Earnings Per Share (EPS) | Portion of a company’s profit allocated to each outstanding share of common stock. |
| Enterprise Value / EBIT (EV/EBIT) | Valuation ratio that compares a company’s enterprise value (EV) to its earnings before interest and taxes (EBIT). |
| Enterprise Value / EBITDA (EV/EBITDA) | Valuation ratio comparing enterprise value to cash earnings (EBITDA). |
| Free Cash Flow (FCF) | The money that a company has available to repay its creditors or pay dividends and interest to investors. |
| Goodwill | Excess paid in acquisitions above fair value of net assets. |
| Gross Profit Margin | Percentage of revenue that exceeds the cost of goods sold. |
| Intangible Assets | Non-physical assets including intellectual property, patents, and goodwill. |
| Interest Expense | Cost incurred by an entity for borrowing funds. |
| MarketValue | Current value of a publicly traded company, based on the total dollar amount that all of its outstanding shares are worth. |
| Net Income | Remains from a company’s total revenues after deducting all operating costs, taxes, interest, and other expenses. |
| Operating Costs | Daily expenses necessary to maintain, operate, and administer a business. |
| Operating Margin | Profitability ratio that measures revenue after covering the operating and non-operating expenses. |
| Operating Profit | Total earnings from a company’s core business operations excluding deductions of interest and tax. |
| Operating Revenue | The money a company generates from its primary business activities. |
| Paid-in Capital | Capital contributed by shareholders. |
| R&D Expenses | The money companies spend on innovation and improving their products, services, technologies, and processes. |
| Return on Equity (ROE) | Profitability of a business in relation to its equity. |
| Return on Invested Capital | Profitability ratio measuring return relative to invested capital. |
| Revenue | The total amount of income generated by the sale of goods and services related to the primary operations of a business. |
| Shareholders’ Equity | Total amount of assets that a company would retain if it paid all of its debts. |
| Total Assets | Sum of all owned assets (current + non-current). |
| Total Liabilities | All debts and obligations of a company. |




Table 4: Descriptive statistics of our dataset

|  | count | mean | std | min | 25% | 50% | 75% | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPI YoY Growth Rate | 8.40×1018.40\text{\times}{10}^{1} | 1.552 3811.552\,381 | 1.351 4901.351\,490 | −8.00×10−1-8.00\text{\times}{10}^{-1} | 3.75×10−13.75\text{\times}{10}^{-1} | 1.551.55 | 2.47252.4725 | 5.385.38 |
| M1 Money Supply | 8.40×1018.40\text{\times}{10}^{1} | 6.726 956×1056.726\,956\text{\times}{10}^{5} | 1.746 188×1051.746\,188\text{\times}{10}^{5} | 5.170 36×1055.170\,36\text{\times}{10}^{5} | 5.570 53×1055.570\,53\text{\times}{10}^{5} | 6.231 289×1056.231\,289\text{\times}{10}^{5} | 6.744 551×1056.744\,551\text{\times}{10}^{5} | 1.120 12×1061.120\,12\text{\times}{10}^{6} |
| M2 Money Supply | 8.40×1018.40\text{\times}{10}^{1} | 2.366 131×1062.366\,131\text{\times}{10}^{6} | 4.464 552×1054.464\,552\text{\times}{10}^{5} | 1.720 814×1061.720\,814\text{\times}{10}^{6} | 1.950 588×1061.950\,588\text{\times}{10}^{6} | 2.307 211×1062.307\,211\text{\times}{10}^{6} | 2.809 994×1062.809\,994\text{\times}{10}^{6} | 3.135 322×1063.135\,322\text{\times}{10}^{6} |
| Purchasing Managers’ Index (PMI) | 8.40×1018.40\text{\times}{10}^{1} | 4.998 571 4×1014.998\,571\,4\text{\times}{10}^{1} | 1.886 3581.886\,358 | 3.57×1013.57\text{\times}{10}^{1} | 4.94×1014.94\text{\times}{10}^{1} | 5.01×1015.01\text{\times}{10}^{1} | 5.09×1015.09\text{\times}{10}^{1} | 5.26×1015.26\text{\times}{10}^{1} |
| Industry Index Return | 1.321 79×1051.321\,79\text{\times}{10}^{5} | 5.46×10−45.46\text{\times}{10}^{-4} | 2.1171×10−22.1171\text{\times}{10}^{-2} | −1.203 14×10−1-1.203\,14\text{\times}{10}^{-1} | −9.50×10−3-9.50\text{\times}{10}^{-3} | 7.20×10−57.20\text{\times}{10}^{-5} | 1.0181×10−21.0181\text{\times}{10}^{-2} | 2.675 9192.675\,919 |
| Capital Expenditures | 1.40×1041.40\text{\times}{10}^{4} | 2.85×1092.85\text{\times}{10}^{9} | 1.29×10101.29\text{\times}{10}^{10} | 0.000.00 | 1.31×1081.31\text{\times}{10}^{8} | 4.71×1084.71\text{\times}{10}^{8} | 1.60×1091.60\text{\times}{10}^{9} | 3.31×10113.31\text{\times}{10}^{11} |
| Cash & Cash Equivalents | 1.40×1041.40\text{\times}{10}^{4} | 2.67×10102.67\text{\times}{10}^{10} | 1.90×10111.90\text{\times}{10}^{11} | 0.000.00 | 7.38×1087.38\text{\times}{10}^{8} | 2.12×1092.12\text{\times}{10}^{9} | 6.81×1096.81\text{\times}{10}^{9} | 4.04×10124.04\text{\times}{10}^{12} |
| Close | 2.98×1062.98\text{\times}{10}^{6} | 1.78×1021.78\text{\times}{10}^{2} | 7.80×1027.80\text{\times}{10}^{2} | 1.131.13 | 2.05×1012.05\text{\times}{10}^{1} | 5.46×1015.46\text{\times}{10}^{1} | 1.40×1021.40\text{\times}{10}^{2} | 6.58×1046.58\text{\times}{10}^{4} |
| Current Assets | 1.31×1041.31\text{\times}{10}^{4} | 2.66×10102.66\text{\times}{10}^{10} | 9.37×10109.37\text{\times}{10}^{10} | 0.000.00 | 2.32×1092.32\text{\times}{10}^{9} | 6.06×1096.06\text{\times}{10}^{9} | 1.67×10101.67\text{\times}{10}^{10} | 2.28×10122.28\text{\times}{10}^{12} |
| Current Liabilities | 1.31×1041.31\text{\times}{10}^{4} | 2.33×10102.33\text{\times}{10}^{10} | 8.19×10108.19\text{\times}{10}^{10} | 0.000.00 | 1.49×1091.49\text{\times}{10}^{9} | 4.62×1094.62\text{\times}{10}^{9} | 1.44×10101.44\text{\times}{10}^{10} | 1.76×10121.76\text{\times}{10}^{12} |
| Dividends paid | 1.38×1041.38\text{\times}{10}^{4} | 2.31×1092.31\text{\times}{10}^{9} | 1.27×10101.27\text{\times}{10}^{10} | 0.000.00 | 1.13×1081.13\text{\times}{10}^{8} | 3.66×1083.66\text{\times}{10}^{8} | 1.16×1091.16\text{\times}{10}^{9} | 1.13×10121.13\text{\times}{10}^{12} |
| EBIT | 1.40×1041.40\text{\times}{10}^{4} | 4.98×1094.98\text{\times}{10}^{9} | 2.32×10102.32\text{\times}{10}^{10} | −6.52×1010-6.52\text{\times}{10}^{10} | 2.20×1082.20\text{\times}{10}^{8} | 8.06×1088.06\text{\times}{10}^{8} | 2.41×1092.41\text{\times}{10}^{9} | 4.25×10114.25\text{\times}{10}^{11} |
| Earnings before tax | 1.40×1041.40\text{\times}{10}^{4} | 4.60×1094.60\text{\times}{10}^{9} | 2.30×10102.30\text{\times}{10}^{10} | −7.13×1010-7.13\text{\times}{10}^{10} | 1.46×1081.46\text{\times}{10}^{8} | 6.63×1086.63\text{\times}{10}^{8} | 2.07×1092.07\text{\times}{10}^{9} | 4.25×10114.25\text{\times}{10}^{11} |
| EPS | 1.40×1041.40\text{\times}{10}^{4} | 6.13×10−16.13\text{\times}{10}^{-1} | 1.581.58 | −1.65×101-1.65\text{\times}{10}^{1} | 1.10×10−11.10\text{\times}{10}^{-1} | 3.60×10−13.60\text{\times}{10}^{-1} | 8.01×10−18.01\text{\times}{10}^{-1} | 6.86×1016.86\text{\times}{10}^{1} |
| EV/EBIT | 1.40×1041.40\text{\times}{10}^{4} | 1.55×1011.55\text{\times}{10}^{1} | 9.24×1029.24\text{\times}{10}^{2} | −8.85×104-8.85\text{\times}{10}^{4} | 5.675.67 | 1.80×1011.80\text{\times}{10}^{1} | 3.49×1013.49\text{\times}{10}^{1} | 1.65×1041.65\text{\times}{10}^{4} |
| EV/EBITDA | 1.40×1041.40\text{\times}{10}^{4} | 2.30×1012.30\text{\times}{10}^{1} | 4.23×1024.23\text{\times}{10}^{2} | −2.66×104-2.66\text{\times}{10}^{4} | 4.934.93 | 1.44×1011.44\text{\times}{10}^{1} | 2.95×1012.95\text{\times}{10}^{1} | 3.25×1043.25\text{\times}{10}^{4} |
| Free Cash Flow (FCF) | 1.40×1041.40\text{\times}{10}^{4} | −3.79×1010-3.79\text{\times}{10}^{10} | 2.72×10112.72\text{\times}{10}^{11} | −6.09×1012-6.09\text{\times}{10}^{12} | −3.13×109-3.13\text{\times}{10}^{9} | −5.22×108-5.22\text{\times}{10}^{8} | 8.65×1078.65\text{\times}{10}^{7} | 1.60×10111.60\text{\times}{10}^{11} |
| Goodwill | 7.42×1037.42\text{\times}{10}^{3} | 9.57×1089.57\text{\times}{10}^{8} | 3.03×1093.03\text{\times}{10}^{9} | 0.000.00 | 1.31×1071.31\text{\times}{10}^{7} | 9.75×1079.75\text{\times}{10}^{7} | 5.70×1085.70\text{\times}{10}^{8} | 4.61×10104.61\text{\times}{10}^{10} |
| Gross Profit Margin | 1.30×1041.30\text{\times}{10}^{4} | 2.75×1012.75\text{\times}{10}^{1} | 2.03×1012.03\text{\times}{10}^{1} | −3.25×102-3.25\text{\times}{10}^{2} | 1.38×1011.38\text{\times}{10}^{1} | 2.34×1012.34\text{\times}{10}^{1} | 3.77×1013.77\text{\times}{10}^{1} | 1.15×1021.15\text{\times}{10}^{2} |
| Intangible Assets | 1.37×1041.37\text{\times}{10}^{4} | 2.57×1092.57\text{\times}{10}^{9} | 1.09×10101.09\text{\times}{10}^{10} | −1.78×108-1.78\text{\times}{10}^{8} | 1.10×1081.10\text{\times}{10}^{8} | 3.78×1083.78\text{\times}{10}^{8} | 1.32×1091.32\text{\times}{10}^{9} | 2.69×10112.69\text{\times}{10}^{11} |
| Interest Expense | 3.99×1023.99\text{\times}{10}^{2} | 6.51×1086.51\text{\times}{10}^{8} | 2.37×1092.37\text{\times}{10}^{9} | 0.000.00 | 4.69×1064.69\text{\times}{10}^{6} | 3.99×1073.99\text{\times}{10}^{7} | 1.79×1081.79\text{\times}{10}^{8} | 1.92×10101.92\text{\times}{10}^{10} |
| MarketValue | 2.98×1062.98\text{\times}{10}^{6} | 6.04×10106.04\text{\times}{10}^{10} | 1.68×10111.68\text{\times}{10}^{11} | 1.21×1081.21\text{\times}{10}^{8} | 1.04×10101.04\text{\times}{10}^{10} | 2.23×10102.23\text{\times}{10}^{10} | 4.72×10104.72\text{\times}{10}^{10} | 8.05×10128.05\text{\times}{10}^{12} |
| Net Income | 1.40×1041.40\text{\times}{10}^{4} | 3.69×1093.69\text{\times}{10}^{9} | 1.87×10101.87\text{\times}{10}^{10} | −6.87×1010-6.87\text{\times}{10}^{10} | 1.14×1081.14\text{\times}{10}^{8} | 5.39×1085.39\text{\times}{10}^{8} | 1.70×1091.70\text{\times}{10}^{9} | 3.67×10113.67\text{\times}{10}^{11} |
| Operating Costs | 1.40×1041.40\text{\times}{10}^{4} | 3.51×10103.51\text{\times}{10}^{10} | 1.43×10111.43\text{\times}{10}^{11} | −5.74×107-5.74\text{\times}{10}^{7} | 2.19×1092.19\text{\times}{10}^{9} | 6.51×1096.51\text{\times}{10}^{9} | 2.07×10102.07\text{\times}{10}^{10} | 3.23×10123.23\text{\times}{10}^{12} |
| Operating Margin | 1.40×1041.40\text{\times}{10}^{4} | 4.00×10−34.00\text{\times}{10}^{-3} | 1.19×1011.19\text{\times}{10}^{1} | −1.11×103-1.11\text{\times}{10}^{3} | 2.75×10−22.75\text{\times}{10}^{-2} | 8.94×10−28.94\text{\times}{10}^{-2} | 2.07×10−12.07\text{\times}{10}^{-1} | 1.81×1021.81\text{\times}{10}^{2} |
| Operating Profit | 1.40×1041.40\text{\times}{10}^{4} | 4.56×1094.56\text{\times}{10}^{9} | 2.30×10102.30\text{\times}{10}^{10} | −7.16×1010-7.16\text{\times}{10}^{10} | 1.22×1081.22\text{\times}{10}^{8} | 6.26×1086.26\text{\times}{10}^{8} | 1.99×1091.99\text{\times}{10}^{9} | 4.24×10114.24\text{\times}{10}^{11} |
| Operating Revenue | 1.40×1041.40\text{\times}{10}^{4} | 3.93×10103.93\text{\times}{10}^{10} | 1.54×10111.54\text{\times}{10}^{11} | −3.87×108-3.87\text{\times}{10}^{8} | 2.49×1092.49\text{\times}{10}^{9} | 7.23×1097.23\text{\times}{10}^{9} | 2.31×10102.31\text{\times}{10}^{10} | 3.32×10123.32\text{\times}{10}^{12} |
| Paid-in Capital | 1.40×1041.40\text{\times}{10}^{4} | 5.29×1095.29\text{\times}{10}^{9} | 2.44×10102.44\text{\times}{10}^{10} | 4.20×1074.20\text{\times}{10}^{7} | 6.99×1086.99\text{\times}{10}^{8} | 1.42×1091.42\text{\times}{10}^{9} | 3.14×1093.14\text{\times}{10}^{9} | 4.62×10114.62\text{\times}{10}^{11} |
| R&D Expenses | 5.03×1035.03\text{\times}{10}^{3} | 1.08×1091.08\text{\times}{10}^{9} | 3.09×1093.09\text{\times}{10}^{9} | 0.000.00 | 6.72×1076.72\text{\times}{10}^{7} | 2.83×1082.83\text{\times}{10}^{8} | 8.12×1088.12\text{\times}{10}^{8} | 5.32×10105.32\text{\times}{10}^{10} |
| ROE | 1.39×1041.39\text{\times}{10}^{4} | 6.256.25 | 1.06×1021.06\text{\times}{10}^{2} | −7.78×103-7.78\text{\times}{10}^{3} | 3.613.61 | 8.778.77 | 1.50×1011.50\text{\times}{10}^{1} | 1.35×1031.35\text{\times}{10}^{3} |
| ROIC | 1.40×1041.40\text{\times}{10}^{4} | 2.95×10−22.95\text{\times}{10}^{-2} | 1.241.24 | −1.14×102-1.14\text{\times}{10}^{2} | 6.51×10−36.51\text{\times}{10}^{-3} | 3.94×10−23.94\text{\times}{10}^{-2} | 9.03×10−29.03\text{\times}{10}^{-2} | 5.13×1015.13\text{\times}{10}^{1} |
| Revenue | 1.40×1041.40\text{\times}{10}^{4} | 3.94×10103.94\text{\times}{10}^{10} | 1.54×10111.54\text{\times}{10}^{11} | −3.87×108-3.87\text{\times}{10}^{8} | 2.53×1092.53\text{\times}{10}^{9} | 7.36×1097.36\text{\times}{10}^{9} | 2.33×10102.33\text{\times}{10}^{10} | 3.32×10123.32\text{\times}{10}^{12} |
| Shareholders Equity | 1.40×1041.40\text{\times}{10}^{4} | 3.61×10103.61\text{\times}{10}^{10} | 1.62×10111.62\text{\times}{10}^{11} | −2.91×1010-2.91\text{\times}{10}^{10} | 2.87×1092.87\text{\times}{10}^{9} | 7.44×1097.44\text{\times}{10}^{9} | 1.91×10101.91\text{\times}{10}^{10} | 3.99×10123.99\text{\times}{10}^{12} |
| Total Assets | 1.40×1041.40\text{\times}{10}^{4} | 2.51×10112.51\text{\times}{10}^{11} | 1.84×10121.84\text{\times}{10}^{12} | 0.000.00 | 5.66×1095.66\text{\times}{10}^{9} | 1.56×10101.56\text{\times}{10}^{10} | 4.61×10104.61\text{\times}{10}^{10} | 4.88×10134.88\text{\times}{10}^{13} |
| Total Liabilities | 1.40×1041.40\text{\times}{10}^{4} | 2.15×10112.15\text{\times}{10}^{11} | 1.69×10121.69\text{\times}{10}^{12} | 0.000.00 | 2.13×1092.13\text{\times}{10}^{9} | 7.27×1097.27\text{\times}{10}^{9} | 2.74×10102.74\text{\times}{10}^{10} | 4.48×10134.48\text{\times}{10}^{13} |

## 7 Within the Macro Agent: Merrill Lynch Clock vs Industry Momentum

During the training period, the Merrill Lynch Clock:Industry Momentum configuration with a 25:75 weighting was selected for the Macro agent, as it optimally integrates macroeconomic and industry momentum scores. This configuration was chosen based on its superior risk-adjusted performance, demonstrated by the highest combined Sharpe and Sortino ratios (2.514) among the evaluated configurations (see Table [5](https://arxiv.org/html/2510.21147v1#S7.T5 "Table 5 ‣ 7 Within the Macro Agent: Merrill Lynch Clock vs Industry Momentum")). Consequently, this setting was adopted for out-of-sample testing to assess its generalizability.

Table 5: Within the Macro Agent: Merrill Lynch Clock vs Industry Momentum

| Model | CR (%) | AR (%) | STD (%) | DD (%) | Sharpe | Sortino | MDD (%) | Calmar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Merrill Lynch Clock:Industry Momentum = 25:75 | 89.30 | 17.86 | 22.40 | 10.40 | 0.797 | 1.717 | -41.00 | 0.436 |
| Merrill Lynch Clock:Industry Momentum = 50:50 | 88.79 | 17.76 | 22.57 | 11.11 | 0.787 | 1.599 | -41.84 | 0.424 |
| Merrill Lynch Clock:Industry Momentum = 75:25 | 63.22 | 12.65 | 15.65 | 9.25 | 0.808 | 1.367 | -16.48 | 0.767 |

## 8 Notation

Table 6: Key Notation for Problem Formulation

| Symbol | Description |
| --- | --- |
| N,TN,T | Number of assets, number of trading days |
| dm,df,ds,dbd\_{m},d\_{f},d\_{s},d\_{b} | Dimensions of macro-economic, firm, industry, benchmark features |
| 𝐌,𝐅,𝐒,𝐁\mathbf{M},\mathbf{F},\mathbf{S},\mathbf{B} | Macro-, Industry-, Firm-, and benchmark-level data tensors/matrices |
| 𝐑\mathbf{R} | Matrix of realized asset returns |
| 𝐰t\mathbf{w}\_{t} | Portfolio weights at time tt |
| rt,xtr\_{t},x\_{t} | Portfolio return and excess return at time tt |
| rfr\_{f} | Risk-free rate |
| fθf\_{\theta} | Parameterized allocation rule with parameters θ\theta |
| SR​(θ)\mathrm{SR}(\theta) | Sharpe Ratio of the strategy induced by θ\theta |