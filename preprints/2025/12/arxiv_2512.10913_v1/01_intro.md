---
authors:
- Mohammad Rezoanul Hoque
- Md Meftahul Ferdaus
- M. Kabir Hassan
doc_id: arxiv:2512.10913v1
family_id: arxiv:2512.10913
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Reinforcement Learning in Financial Decision Making: A Systematic Review of
  Performance, Challenges, and Implementation Strategies'
url_abs: http://arxiv.org/abs/2512.10913v1
url_html: https://arxiv.org/html/2512.10913v1
venue: arXiv q-fin
version: 1
year: 2025
---


Mohammad Rezoanul Hoque

Md Meftahul Ferdaus

M. Kabir Hassan

###### Abstract

Reinforcement learning (RL) is an innovative approach to financial decision making, offering specialized solutions to complex investment problems where traditional methods fail. This review analyzes 167 articles from 2017–2025, focusing on market making, portfolio optimization, and algorithmic trading. It identifies key performance issues and challenges in RL for finance. Generally, RL offers advantages over traditional methods, particularly in market making. This study proposes a unified framework to address common concerns such as explainability, robustness, and deployment feasibility. Empirical evidence with synthetic data suggests that implementation quality and domain knowledge often outweigh algorithmic complexity. The study highlights the need for interpretable RL architectures for regulatory compliance, enhanced robustness in nonstationary environments, and standardized benchmarking protocols. Organizations should focus less on algorithm sophistication and more on market microstructure, regulatory constraints, and risk management in decision-making.

###### keywords:

Reinforcement Learning , Financial Decision Making , Market Making , Algorithmic Trading

## 1 Introduction

Financial markets present some of the most challenging environments for algorithmic decision making, characterized by high dimensionality, non-stationarity, and complex dependencies that traditional methods struggle to capture effectively Cont, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib19)). The evolution of financial theory has witnessed a significant transformation from classical approaches to more sophisticated methodologies that acknowledge the limitations of traditional assumptions. As documented by Agudelo Aguirre and Agudelo Aguirre Agudelo Aguirre and Agudelo Aguirre, ([2024](https://arxiv.org/html/2512.10913v1#bib.bib1)), behavioral finance has emerged from the divergences observed in traditional theories of finance, serving as a supplement to classical finance by introducing behavioral aspects to decision-making. This evolution reflects a broader recognition that financial markets are complex adaptive systems where traditional econometric approaches may prove insufficient.

Reinforcement learning (RL), as an emerging paradigm in artificial intelligence, provides an adaptive, data-driven approach to address these challenges by learning optimal strategies directly from market interactions Sutton and Barto, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib65)). The application of machine learning methods to financial decision making has gained particular prominence in addressing what Bagnara Bagnara, ([2022](https://arxiv.org/html/2512.10913v1#bib.bib6)) identifies as the "factor zoo" problem in empirical asset pricing. This latest development in empirical asset pricing demonstrates how machine learning techniques offer great flexibility and prediction accuracy, though they require special care as they strongly depart from traditional econometrics. The integration of RL within this broader machine learning framework represents a natural progression toward more adaptive and responsive financial decision-making systems.

The theoretical foundation for applying adaptive learning approaches in finance is further strengthened by empirical evidence regarding the evolution of market efficiency over time. Lim and Brooks Lim and Brooks, ([2011](https://arxiv.org/html/2512.10913v1#bib.bib45)) provide a systematic review of weak-form market efficiency literature, demonstrating that market efficiency is not a static property but evolves dynamically over time. This time-varying nature of market efficiency creates opportunities for adaptive algorithms like RL to exploit temporary inefficiencies while adapting to changing market conditions. The evidence of evolving market efficiency directly supports the rationale for employing learning-based approaches that can continuously adapt their strategies based on observed market behavior.

The application of RL to financial decision making has gained significant momentum in recent years, driven by several converging factors. First, the unprecedented availability of financial data, including high-frequency trading data, alternative data sources, and real-time streaming feeds, provides the rich information environment that RL algorithms require for effective learning Aldridge, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib2)); [Tsantekidis et al., 2017a](https://arxiv.org/html/2512.10913v1#bib.bib68) . Second, advances in deep learning architectures have enabled RL methods to handle the high-dimensional state and action spaces characteristic of financial applications Goodfellow et al., ([2016](https://arxiv.org/html/2512.10913v1#bib.bib30)); Heaton et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib37)). Third, the increasing accessibility and cost-effectiveness of cloud computing resources have made sophisticated RL implementations feasible for a broader range of financial institutions.

The foundational work in applying RL to finance can be traced to Moody and Saffell’s pioneering research on direct reinforcement learning for trading systems Moody and Saffell, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib55)). Their approach demonstrated that RL could optimize trading performance directly without requiring explicit forecasting models, establishing a paradigm that continues to influence contemporary research. This direct optimization approach aligns with the broader trend in financial machine learning identified by Bagnara Bagnara, ([2022](https://arxiv.org/html/2512.10913v1#bib.bib6)), where methods are grouped into categories including regularization, dimension reduction, regression trees/random forest, neural networks, and comparative analyses. More recently, Jiang et al. introduced deep reinforcement learning frameworks specifically designed for portfolio management problems, showing how modern neural network architectures could be effectively combined with RL principles for financial applications Jiang et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib38)).

The integration of RL within the broader landscape of financial machine learning represents a significant departure from traditional econometric approaches. As noted in the comprehensive survey by Bagnara Bagnara, ([2022](https://arxiv.org/html/2512.10913v1#bib.bib6)), machine learning methods in asset pricing require particular attention to their economic interpretation, providing hints for future developments. This emphasis on economic interpretability is particularly crucial for RL applications in finance, where the learned policies must not only achieve superior performance but also provide insights that can be understood and validated by financial practitioners and regulators.

Despite these promising developments, the practical implementation of RL in finance faces numerous unique challenges compared to other domains where RL has achieved success Dulac-Arnold et al., ([2019](https://arxiv.org/html/2512.10913v1#bib.bib22)); García and Fernández, ([2015](https://arxiv.org/html/2512.10913v1#bib.bib27)). These challenges stem from the inherent characteristics of financial environments: markets are fundamentally non-stationary, with dynamics that shift due to regulatory changes, technological innovations, and evolving market participant behavior Cont, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib19)); Farmer and Skouras, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib24)). The evidence presented by Lim and Brooks Lim and Brooks, ([2011](https://arxiv.org/html/2512.10913v1#bib.bib45)) regarding the evolution of market efficiency over time further emphasizes the dynamic nature of financial markets and the need for adaptive approaches that can respond to changing conditions.

The cost of exploration in financial environments can be prohibitively high, as poor decisions result in real financial losses rather than abstract performance penalties. Additionally, financial applications operate under strict regulatory oversight, necessitating decision processes that are explainable and auditable Doshi-Velez and Kim, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib21)); [Gomber et al., 2017b](https://arxiv.org/html/2512.10913v1#bib.bib29) . The behavioral finance perspective highlighted by Agudelo Aguirre and Agudelo Aguirre Agudelo Aguirre and Agudelo Aguirre, ([2024](https://arxiv.org/html/2512.10913v1#bib.bib1)) adds another layer of complexity, as RL systems must account for psychological aspects, cognitive biases, and other behavioral factors that influence market dynamics and investor decision-making.

The regulatory landscape presents both challenges and opportunities for RL adoption in finance. Recent developments in AI governance frameworks emphasize the need for explainable and auditable decision-making systems, driving research toward interpretable RL architectures Puiutta and Veith, ([2020](https://arxiv.org/html/2512.10913v1#bib.bib57)). The evolving regulatory environment requires RL systems to balance innovation with compliance, necessitating new approaches to model validation and risk management McNeil et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib51)). This regulatory focus on interpretability aligns with the broader emphasis on economic interpretation in financial machine learning identified by Bagnara Bagnara, ([2022](https://arxiv.org/html/2512.10913v1#bib.bib6)), suggesting that successful RL implementations must prioritize both performance and explainability.

This comprehensive review addresses these challenges by conducting a systematic analysis of the current literature to identify patterns and insights regarding the effectiveness of RL in financial applications. The analysis reveals several important findings that challenge common assumptions about RL effectiveness in finance. The emergence of hybrid approaches that combine RL with traditional quantitative methods shows particular promise, achieving significant performance improvements over pure RL implementations Fischer and Krauss, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib26)). This trend toward hybrid methodologies reflects the broader evolution in financial machine learning, where the integration of different approaches often yields superior results compared to single-method implementations.

Market making applications consistently demonstrate strong performance improvements, followed by cryptocurrency trading, while traditional portfolio optimization shows signs of maturation Spooner et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib64)). The need for robust validation frameworks becomes increasingly critical as RL systems are deployed in production environments where model failures can have significant financial consequences Bailey et al., ([2014](https://arxiv.org/html/2512.10913v1#bib.bib7)). The time-varying nature of market efficiency documented by Lim and Brooks Lim and Brooks, ([2011](https://arxiv.org/html/2512.10913v1#bib.bib45)) further emphasizes the importance of continuous validation and adaptation in RL systems deployed in financial markets.

This review delivers contributions in four key areas. Firstly, it presents a detailed classification of how RL is applied within finance, sorting existing literature by application areas, algorithmic strategies, and performance traits. This classification builds upon the categorization framework established in the broader financial machine learning literature Bagnara, ([2022](https://arxiv.org/html/2512.10913v1#bib.bib6)); Shi, ([2025](https://arxiv.org/html/2512.10913v1#bib.bib63)), extending it specifically to RL applications. Secondly, it performs thorough analyses to pinpoint elements that critically impact RL outcomes and provides data-driven suggestions for professionals. These analyses incorporate insights from the evolution of market efficiency Lim and Brooks, ([2011](https://arxiv.org/html/2512.10913v1#bib.bib45)) and behavioral finance considerations Agudelo Aguirre and Agudelo Aguirre, ([2024](https://arxiv.org/html/2512.10913v1#bib.bib1)) to provide a comprehensive understanding of the factors influencing RL performance in financial contexts.

Thirdly, the issue of proprietary performance data in finance is tackled by rigorously examining publicly accessible studies. This approach addresses one of the key challenges in financial machine learning research, where the proprietary nature of trading strategies and performance data often limits the availability of comprehensive empirical evidence. Lastly, it suggests practical implementation models that confront real-world deployment hurdles while adhering to regulatory standards and risk management protocols. These implementation models incorporate lessons learned from the broader evolution of financial theory and practice, including the transition from classical to behavioral finance approaches and the integration of machine learning methods in asset pricing.

The analysis demonstrates that successful RL implementation in finance depends more critically on implementation quality, domain expertise, and data preprocessing than on algorithmic sophistication. This finding aligns with the broader trends in financial machine learning identified by Bagnara Bagnara, ([2022](https://arxiv.org/html/2512.10913v1#bib.bib6)), where the economic interpretation and practical applicability of results often outweigh pure algorithmic complexity. The findings provide both researchers and practitioners with evidence-based guidance for developing effective RL systems in financial contexts, highlighting the importance of interdisciplinary collaboration between machine learning researchers, financial practitioners, and regulatory experts.

The integration of insights from behavioral finance Agudelo Aguirre and Agudelo Aguirre, ([2024](https://arxiv.org/html/2512.10913v1#bib.bib1)) and market efficiency evolution Lim and Brooks, ([2011](https://arxiv.org/html/2512.10913v1#bib.bib45)) provides a more comprehensive foundation for understanding the role of RL in financial decision making. This interdisciplinary approach recognizes that successful RL implementations must account for the complex interplay between market dynamics, participant behavior, regulatory constraints, and technological capabilities. The evidence suggests that the future of RL in finance lies not in replacing traditional methods entirely, but in creating sophisticated hybrid systems that leverage the strengths of both adaptive learning and established financial theory.

## 2 BACKGROUND AND PROBLEM DEFINITION

Reinforcement Learning (RL) in finance adapts machine learning and control theory for quantitative finance, transforming traditional strategies into adaptive, data-driven models. To clarify shared concepts and the theory behind financial RL, this section begins with the fundamental Machine Learning (ML) definition by Mitchell et al. Mitchell, ([1997](https://arxiv.org/html/2512.10913v1#bib.bib52)) and Mohri et al. Mohri et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib54)).

###### Definition 1 (Machine Learning Mitchell, ([1997](https://arxiv.org/html/2512.10913v1#bib.bib52)); Mohri et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib54))).

A computer program is said to learn from experience EE with respect to some class of tasks TT and performance measure PP if its performance can improve with EE on TT measured by PP.

This fundamental idea underlies Reinforcement Learning (RL), a learning approach centered on sequential decision-making, where an agent develops optimal policies by interacting with an environment. Sutton and Barto Sutton and Barto, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib65)) define this framework as follows:

###### Definition 2 (Reinforcement Learning Sutton and Barto, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib65))).

Reinforcement Learning is a computational approach to learning from interaction, where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward over time.

The shift from ML to RL is crucial for financial decision making due to the complex nature of financial markets, which involve high dimensionality, non-stationarity, and complex dependencies. The goal is to optimize investment strategies, portfolio allocations, and trading decisions to maximize risk-adjusted returns while adhering to constraints and regulations.

The formal RL framework is defined in the context of a Markov Decision Process (MDP), which provides the mathematical foundation for modeling sequential decision making under uncertainty. The financial RL framework is defined as follows.

###### Definition 3 (Financial Markov Decision Process).

A Financial Markov Decision Process is defined as a tuple (S,A,P,R,γ)(S,A,P,R,\gamma), where:

* 1.

  SS is the state space representing relevant market information, portfolio positions, and environmental conditions
* 2.

  AA is the action space of possible trading decisions, allocation changes, or strategic choices
* 3.

  P:S×A×S→[0,1]P:S\times A\times S\rightarrow[0,1] represents the transition probabilities between market states
* 4.

  R:S×A→ℝR:S\times A\rightarrow\mathbb{R} is the reward function encoding investment objectives and risk considerations
* 5.

  γ∈[0,1]\gamma\in[0,1] is the discount factor for future expected rewards

In financial applications, the state space SS comprises diverse information sources, carefully engineered to reflect market dynamics and remain computationally feasible. Effective representations merge multiple hierarchies: foundational price-based features, technical indicators from price and volume, fundamental data on company and economy, and alternative data for extra insights. The state space’s dimensionality and composition crucially affect RL systems’ learning efficiency and implementation.

The action space AA varies widely in financial applications, mirroring the diversity in financial decision-making. In portfolio optimization, actions represent portfolio weights or allocation changes, typically constrained by regulations and risk management. Algorithmic trading might use discrete action spaces for buy, sell, or hold decisions, or continuous ones for order sizes and timing. Market making often relies on continuous action spaces for bid-ask spread adjustments and inventory management. Choosing between discrete and continuous action spaces significantly affects algorithm selection, convergence, and performance.

The reward function RR is crucial and complex in financial RL, needing to encode investment objectives while balancing various factors. Effective functions must incorporate return maximization, risk control, transaction cost reduction, regulatory compliance, and market impact. Designing them requires domain expertise and attention to the specific financial context.

###### Definition 4 (Financial Reward Function).

A Financial Reward Function R​(st,at)R(s\_{t},a\_{t}) at time tt typically incorporates multiple components:

|  |  |  |
| --- | --- | --- |
|  | R​(st,at)=α⋅Rreturn​(st,at)−β⋅Rrisk​(st,at)−γ⋅Rcost​(st,at)+δ⋅Rcompliance​(st,at)R(s\_{t},a\_{t})=\alpha\cdot R\_{\text{return}}(s\_{t},a\_{t})-\beta\cdot R\_{\text{risk}}(s\_{t},a\_{t})-\gamma\cdot R\_{\text{cost}}(s\_{t},a\_{t})+\delta\cdot R\_{\text{compliance}}(s\_{t},a\_{t}) |  |

where α,β,γ,δ\alpha,\beta,\gamma,\delta are weighting parameters that balance different objectives.

The policy π:S→A\pi:S\rightarrow A represents the decision-making strategy that maps market states to actions. In financial contexts, the policy must be robust to market volatility, adaptable to changing conditions, and interpretable for regulatory compliance. The optimal policy π∗\pi^{\*} maximizes the expected cumulative discounted reward:

|  |  |  |
| --- | --- | --- |
|  | π∗=arg⁡maxπ⁡𝔼​[∑t=0∞γt​R​(st,at)|π]\pi^{\*}=\arg\max\_{\pi}\mathbb{E}\left[\sum\_{t=0}^{\infty}\gamma^{t}R(s\_{t},a\_{t})|\pi\right] |  |

The value function Vπ​(s)V^{\pi}(s) represents the expected cumulative reward from state ss following policy π\pi, while the action-value function Qπ​(s,a)Q^{\pi}(s,a) represents the expected cumulative reward from taking action aa in state ss and then following policy π\pi. These functions satisfy the Bellman equations:

|  |  |  |
| --- | --- | --- |
|  | Vπ​(s)=𝔼a∼π​(s)​[R​(s,a)+γ​∑s′P​(s′|s,a)​Vπ​(s′)]V^{\pi}(s)=\mathbb{E}\_{a\sim\pi(s)}\left[R(s,a)+\gamma\sum\_{s^{\prime}}P(s^{\prime}|s,a)V^{\pi}(s^{\prime})\right] |  |

|  |  |  |
| --- | --- | --- |
|  | Qπ​(s,a)=R​(s,a)+γ​∑s′P​(s′|s,a)​Vπ​(s′)Q^{\pi}(s,a)=R(s,a)+\gamma\sum\_{s^{\prime}}P(s^{\prime}|s,a)V^{\pi}(s^{\prime}) |  |

### 2.1 Theoretical Foundations of RL Algorithms in Financial Decision Making

The landscape of RL algorithms applicable to financial decision making can be systematically categorized based on their fundamental learning paradigms and architectural characteristics. This taxonomy provides a structured framework for understanding the strengths, limitations, and appropriate applications of different algorithmic approaches in financial contexts.

Value-based methods form the foundation of many financial RL applications, particularly those involving discrete decision spaces. These algorithms learn value functions that approximate the expected return of state-action pairs, enabling optimal decision making through value maximization. Deep Q-Networks (DQN) and their extensions represent the most widely adopted value-based approaches in financial applications.

###### Definition 5 (Q-Learning for Financial Applications).

The Q-learning update rule for financial decision making is given by:

|  |  |  |
| --- | --- | --- |
|  | Q​(st,at)←Q​(st,at)+α​[rt+1+γ​maxa′⁡Q​(st+1,a′)−Q​(st,at)]Q(s\_{t},a\_{t})\leftarrow Q(s\_{t},a\_{t})+\alpha\left[r\_{t+1}+\gamma\max\_{a^{\prime}}Q(s\_{t+1},a^{\prime})-Q(s\_{t},a\_{t})\right] |  |

where α\alpha is the learning rate, rt+1r\_{t+1} is the immediate financial reward, and γ\gamma is the discount factor.

Policy-based methods learn optimal policy functions that map states directly to actions, making them particularly suitable for continuous action spaces common in portfolio optimization and market making applications. Policy gradient methods optimize the policy parameters directly by following the gradient of expected returns.

###### Definition 6 (Policy Gradient for Financial Applications).

The policy gradient theorem for financial RL is expressed as:

|  |  |  |
| --- | --- | --- |
|  | ∇θJ​(θ)=𝔼πθ​[∑t=0T∇θlog⁡πθ​(at|st)⋅Gt]\nabla\_{\theta}J(\theta)=\mathbb{E}\_{\pi\_{\theta}}\left[\sum\_{t=0}^{T}\nabla\_{\theta}\log\pi\_{\theta}(a\_{t}|s\_{t})\cdot G\_{t}\right] |  |

where J​(θ)J(\theta) is the expected return, πθ\pi\_{\theta} is the parameterized policy, and GtG\_{t} is the return from time tt.

Actor-critic methods combine the advantages of both value-based and policy-based approaches by maintaining separate networks for policy estimation (actor) and value function approximation (critic). These methods have shown particular effectiveness in financial applications requiring continuous control and stable learning. Model-based methods learn explicit models of market dynamics and use these models for planning and decision making. While less common in financial applications due to the difficulty of accurately modeling market dynamics, these approaches offer advantages in terms of sample efficiency and interpretability. Multi-agent RL addresses scenarios with multiple interacting participants, which is particularly relevant for financial markets where multiple agents compete and collaborate. These approaches explicitly model strategic interactions and can provide insights into market dynamics and systemic effects.

Hierarchical RL methods address the multi-scale temporal structure of financial decision making by learning policies at multiple levels of abstraction. These approaches are particularly valuable for applications spanning multiple time horizons, from short-term execution decisions to long-term strategic allocation choices.The theoretical convergence properties of RL algorithms in financial contexts require special consideration due to the non-stationary nature of financial markets. Traditional convergence guarantees may not hold in environments where the underlying dynamics change over time. Robust optimization techniques and adaptive learning approaches have been developed to address these theoretical challenges.

The exploration-exploitation trade-off in financial RL requires careful theoretical analysis due to the potential for significant losses during exploration. Safe exploration techniques, such as constrained policy optimization and uncertainty-aware exploration, provide theoretical frameworks for balancing learning and risk management.The sample complexity of financial RL algorithms is a critical theoretical consideration given the high cost of data collection and experimentation in financial environments. Theoretical bounds on sample complexity and techniques for improving sample efficiency are essential for practical implementation. The generalization properties of financial RL systems are particularly important given the need to perform well on unseen market conditions. Theoretical frameworks for understanding and improving generalization in non-stationary environments are active areas of research. This comprehensive background and problem definition establishes the theoretical foundation necessary for understanding the challenges, opportunities, and methodological considerations involved in applying reinforcement learning to financial decision making. The systematic implementation challenges and practical considerations are analyzed in detail in Section 8.

## 3 Methodology

This section outlines the systematic methodology employed to conduct a comprehensive review of reinforcement learning applications in financial decision making. The review follows established guidelines for systematic literature reviews in information systems research and adopts a structured approach to ensure reproducibility and minimize selection bias.

### 3.1 Research Questions

The systematic review is guided by several research questions: RQ1 focuses on identifying the current applications of reinforcement learning in financial decision making and their distribution across different financial domains. RQ2 examines the most commonly employed reinforcement learning algorithms and methodologies in financial applications and their relative performance characteristics. RQ3 analyzes the key factors that influence the performance of reinforcement learning systems in financial environments. RQ4 addresses the primary challenges and limitations faced in implementing reinforcement learning solutions for financial decision making. Lastly, RQ5 explores the emerging trends and future research directions in the application of reinforcement learning to finance.

### 3.2 Search Strategy and Data Sources

To identify relevant literature published between January 2020 and December 2025, a comprehensive search strategy was employed. This involved an extensive search across multiple academic databases to ensure thorough coverage of the subject matter. Primary databases included IEEE Xplore, ACM Digital Library, ScienceDirect, SpringerLink, and Wiley Online Library. Specialized databases such as JSTOR for finance journals, SSRN for social science research, and RePEc for economics research were also utilized. Additionally, preprint servers like arXiv.org, particularly focusing on the cs.LG and q-fin sections, and SSRN Working Papers were examined. Conference proceedings explored included those from NeurIPS, ICML, ICLR, AAAI, IJCAI, KDD, and the ACM International Conference on AI in Finance (ICAIF).

The search strategy employed a combination of keywords related to reinforcement learning and financial applications. The combined search string was:

("reinforcement learning" OR "deep reinforcement learning" OR "RL" OR "DRL") AND ("finance" OR "financial" OR "trading" OR "investment" OR "portfolio" OR "market making" OR "algorithmic trading" OR "quantitative finance") AND ("decision making" OR "optimization" OR "strategy" OR "policy")

### 3.3 Study Selection Process

The study selection process followed a systematic multi-stage approach as illustrated in Figure [1](https://arxiv.org/html/2512.10913v1#S3.F1 "Figure 1 ‣ 3.3 Study Selection Process ‣ 3 Methodology ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"). The process was designed to minimize bias and ensure comprehensive coverage while maintaining quality standards.

![Refer to caption](methodology_flowchart.png)


Figure 1: Methodology for systematic selection of articles for the review. The flowchart illustrates the four-stage systematic review process following PRISMA guidelines, showing the number of studies at each stage and the reasons for exclusion. The process resulted in 167 high-quality studies included in the final meta-analysis.

Stage 1: Initial Search and Deduplication
The initial search across all databases yielded 2,847 potentially relevant publications. After removing duplicates using both automated tools and manual verification, 1,923 unique publications remained for further screening.

Stage 2: Title and Abstract Screening
Two independent reviewers screened the titles and abstracts of all 1,923 publications against the inclusion and exclusion criteria. Disagreements were resolved through discussion and, when necessary, consultation with a third reviewer. This stage resulted in the exclusion of 1,456 publications that did not meet the relevance criteria, leaving 467 publications for full-text review.

Stage 3: Full-Text Assessment
The remaining 467 publications underwent full-text assessment for eligibility. This stage involved detailed examination of methodology, contribution, and relevance to the research questions. Publications were excluded if they lacked sufficient technical detail, did not present novel contributions, or did not adequately address financial applications. This process resulted in the exclusion of 300 additional publications.

Stage 4: Quality Assessment and Final Selection
The remaining 167 publications were assessed using quality criteria adapted from established frameworks for systematic reviews in information systems research. All publications met the quality threshold and were included in the final review.

### 3.4 Empirical Validation Framework

To validate the meta-analysis findings, a synthetic dataset was developed that reproduces key statistical patterns observed in the literature. This empirical validation approach addresses the challenge of confidential performance data in financial applications while enabling rigorous statistical analysis of factors influencing RL performance. The synthetic dataset includes 167 studies with variables representing feature dimensions, number of assets, training periods, algorithm types, application domains, and performance metrics. The data generation process preserves the statistical relationships observed in the literature while enabling controlled analysis of performance drivers.

## 4 Applications of RL in Financial Domains

### 4.1 Portfolio Management and Optimization

Portfolio management is well-suited for RL in finance due to its sequential nature. The review of 45 publications shows that RL methods generally outperform traditional methods with modest gains. In Table [2](https://arxiv.org/html/2512.10913v1#S5.T2 "Table 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"), hybrid approaches like LSTM-DDPG demonstrate moderate to high performance by integrating fundamental and technical data. In portfolio management, RL often views the problem as an MDP, with states reflecting market conditions and portfolio attributes, actions as allocation choices, and rewards as risk-adjusted returns. State spaces may include current and historical price data, price-based technical indicators, company fundamentals, and macroeconomic factors. The dimensionality varies in the literature, from single price-dimension features to complex multi-modal data sets. Recent portfolio optimization research focuses on incorporating realistic limitations, such as transaction costs, into RL frameworks. Mean-variance optimizations often yield high turnover rates, which are unrealistic market assumptions. The RL approach enables objective optimization by considering transaction costs and market impact constraints through explicit reward structure constraints, along with legal and regulatory constraints using effectively designed reward functions.

Due to DDPG’s capability with continuous action spaces for portfolio weights, it is utilized in optimizing portfolio management. As per Table [1](https://arxiv.org/html/2512.10913v1#S5.T1 "Table 1 ‣ 5.1 Comparative Performance of Algorithm Families ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"), DDPG is an Actor-Critic algorithm, learning deterministic policies from market states to portfolio weights. TD3, compared to DDPG, offers similar benefits with additional advantages in reducing overestimation bias and enhancing learning stability, demonstrated by its strong performance in options trading (see Table [2](https://arxiv.org/html/2512.10913v1#S5.T2 "Table 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies")).

The meta-analysis in Figure [2](https://arxiv.org/html/2512.10913v1#S5.F2 "Figure 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows that portfolio optimization performance is more influenced by feature quality than quantity, with a weak correlation between dimensionality and RL improvements (slope = 0.171, p-value = 0.499). Additionally, RL benefits do not scale significantly with increased asset complexity (slope = 0.010, p-value = 0.362), highlighting RL’s adaptive learning as a key advantage. Table [3](https://arxiv.org/html/2512.10913v1#S5.T3 "Table 3 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows the evolution of portfolio management applications, with deep RL frameworks enhancing performance and risk-return optimization. Table [4](https://arxiv.org/html/2512.10913v1#S5.T4 "Table 4 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") outlines challenges like managing multi-asset complexity via hierarchical decomposition and addressing scalability in high-dimensional states with feature selection and dimensionality reduction. Table [5](https://arxiv.org/html/2512.10913v1#S7.T5 "Table 5 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows that LSTM-RL methods significantly outperform pure RL in portfolio optimization, demonstrating the benefits of integrating temporal modeling with reinforcement learning for portfolio management.

### 4.2 Algorithmic Trading and Execution

The literature review found that algorithmic trading, with 62 publications on high-frequency trading, momentum strategies, and execution optimization, was the largest category. Performance improvements surpassed those in corporate risk management and portfolio optimization, with most reporting substantial outperformance over traditional methods. Table [2](https://arxiv.org/html/2512.10913v1#S5.T2 "Table 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows that deep RL methods like PPO, SAC, and Rainbow DQN achieved high to moderate-high performance in algorithmic trading.

HFT applications leverage RL to swiftly adapt to market microstructure changes by identifying short-term patterns missed by traditional approaches. The state space includes the order book, recent price movements, and microstructure indicators like bid-ask spreads and trading volumes. Actions are discrete, involving decisions to place, modify, or cancel orders.

The DQN algorithms are highly effective in HFT applications, as they manage discrete action spaces and learn from complex patterns in high-dimensional states. As shown in Table [1](https://arxiv.org/html/2512.10913v1#S5.T1 "Table 1 ‣ 5.1 Comparative Performance of Algorithm Families ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"), DQN, DDQN, and Rainbow DQN excel in discrete trading and high-frequency trading, offering stable learning at medium to high complexity levels. The experience replay in DQN mitigates the financial markets’ non-stationarity by consolidating previous experiences for learning despite market changes. Recent advances in algorithmic trading, shown in Table [3](https://arxiv.org/html/2512.10913v1#S5.T3 "Table 3 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"), reveal a shift from basic to advanced deep RL methods achieving better risk-adjusted returns. Implementation challenges, detailed in Table [4](https://arxiv.org/html/2512.10913v1#S5.T4 "Table 4 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"), involve handling real-time constraints via model compression and edge computing, and tackling high-dimensional states through feature selection and dimensionality reduction.

Figure [5](https://arxiv.org/html/2512.10913v1#S5.F5 "Figure 5 ‣ 5.3 Empirical Validation of Meta-Analysis Findings ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows algorithmic trading applications perform competitively, but below market making applications. Figure [2](https://arxiv.org/html/2512.10913v1#S5.F2 "Figure 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") illustrates that the choice of algorithm family (Panel f) has little impact on performance, suggesting that implementation quality and domain expertise are more critical than specific algorithm selection.

### 4.3 Market Making and Liquidity Provision

Market making applications exhibit the highest performance gains in the meta-analysis, indicated by the highest RL premium (0.488) in Figure [5](https://arxiv.org/html/2512.10913v1#S5.F5 "Figure 5 ‣ 5.3 Empirical Validation of Meta-Analysis Findings ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"). This improvement likely results from the adaptability and continuous nature of RL methods, which better capture the dynamic market microstructure and efficiently solve complex multi-objective functions that are difficult for traditional market making methods.

Market making involves managing inventory risk to maintain security levels within a target range while profiting from the bid-ask spread. Table [2](https://arxiv.org/html/2512.10913v1#S5.T2 "Table 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") indicates that DDPG excels in market making with high-frequency data, making it ideal for bid-ask spread optimization in continuous action spaces. Traditional market making methods are limited by simplistic assumptions about bid-ask spreads and inventory control. In contrast, RL methods adapt to market conditions and manage multiple objectives like bid-ask spread capture, inventory, and risk. Table [1](https://arxiv.org/html/2512.10913v1#S5.T1 "Table 1 ‣ 5.1 Comparative Performance of Algorithm Families ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") indicates that DDPG from the Actor-Critic family excels with high performance and medium-high complexity, making it ideal for continuous action spaces in market making.

Table [6](https://arxiv.org/html/2512.10913v1#S7.T6 "Table 6 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows that market making is a key hub for transferring techniques to other financial areas, with strong transfer to portfolio optimization, cryptocurrency trading, risk management, and execution trading. Techniques like inventory management, bid-ask optimization, dynamic hedging, and order flow modeling have been effectively applied in these domains. Figure [8](https://arxiv.org/html/2512.10913v1#S6.F8 "Figure 8 ‣ 6.1 Performance Evolution Over Time ‣ 6 Temporal Evolution and Emerging Trends ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows that market making applications have achieved the highest performance improvements from 2020 to 2025. Table [4](https://arxiv.org/html/2512.10913v1#S5.T4 "Table 4 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") highlights implementation challenges, such as managing market impact and addressing liquidity constraints, essential for complying with market abuse regulations and best execution requirements.

## 5 Meta-Analysis of Performance and Methodologies

This section presents a comprehensive meta-analysis of reinforcement learning applications in financial decision making, synthesizing findings from 167 high-quality studies published between 2017 and 2025. The analysis examines algorithmic approaches, performance characteristics, implementation challenges, and emerging trends in the field.

### 5.1 Comparative Performance of Algorithm Families

The landscape of reinforcement learning algorithms applied to finance has evolved significantly, with deep reinforcement learning methods dominating recent applications. Table [1](https://arxiv.org/html/2512.10913v1#S5.T1 "Table 1 ‣ 5.1 Comparative Performance of Algorithm Families ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") presents a comprehensive taxonomy of RL algorithms used in financial applications, organized by algorithmic family and showing their relative performance characteristics.

Table 1: Comprehensive RL Algorithm Taxonomy for Financial Applications (2020-2025)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Algorithm Family | Specific Methods | Financial Applications | Performance Level | Complexity | Key Advantages | References |
| Value-Based | DQN, DDQN | Portfolio optimization, Asset allocation | Moderate | Medium | Stable learning, discrete actions | Jiang et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib38)) |
| Dueling DQN | Algorithmic trading, Order execution | Moderate-High | Medium-High | Better value estimation | Lei et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib41)) |
| Rainbow DQN | High-frequency trading | Moderate | High | Combines multiple improvements | Zhang et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib77)) |
| C51, QR-DQN | Risk management | Moderate | High | Distributional value learning | Charpentier et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib16)) |
| Policy-Based | REINFORCE | Portfolio rebalancing | Low-Moderate | Low | Simple implementation | Almahdi and Yang, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib3)) |
| PPO | Cryptocurrency trading | High | Medium | Stable policy updates | [Li et al., 2019a](https://arxiv.org/html/2512.10913v1#bib.bib42) |
| TRPO | ESG investing | Moderate | Medium-High | Theoretical guarantees | Benhamou et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib9)) |
| A2C | Multi-asset trading | Moderate | Medium | Synchronous updates | Wang et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib71)) |
| Actor-Critic | DDPG | Market making | High | Medium-High | Continuous action spaces | Spooner et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib64)) |
| TD3 | Options trading | High | High | Reduced overestimation bias | Kolm and Rémi, ([2019](https://arxiv.org/html/2512.10913v1#bib.bib40)) |
| SAC | Forex trading | High | High | Maximum entropy framework | Théate and Ernst, ([2021](https://arxiv.org/html/2512.10913v1#bib.bib67)) |
| A3C | Decentralized finance | Moderate-High | Medium | Asynchronous learning | Qin et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib58)) |
| Model-Based | PETS | Derivative pricing | Moderate | Very High | Sample efficiency | Halperin, ([2020](https://arxiv.org/html/2512.10913v1#bib.bib32)) |
| MPC-RL | Risk-constrained trading | Moderate | Very High | Explicit constraints | [Carapuço et al., 2018a](https://arxiv.org/html/2512.10913v1#bib.bib13) |
| Dyna-Q | Backtesting optimization | Low-Moderate | Medium | Planning integration | Moody and Saffell, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib55)) |
| Multi-Agent | MADDPG | Market simulation | Moderate | Very High | Multi-participant modeling | [Lussange et al., 2021a](https://arxiv.org/html/2512.10913v1#bib.bib48) |
| QMIX | Competitive trading | Moderate-High | Very High | Centralized training | Yuan et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib75)) |
| COMA | Collaborative investing | Moderate | Very High | Credit assignment | Chen et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib17)) |
| Hierarchical | HAC | Long-term investing | Moderate | High | Temporal abstraction | Liu et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib46)) |
| FuN | Strategic asset allocation | Moderate | High | Goal-conditioned learning | [Hambly et al., 2023a](https://arxiv.org/html/2512.10913v1#bib.bib33) |
| Option-Critic | Multi-timeframe trading | Moderate | High | Automatic skill discovery | Ritter, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib59)) |

* 1.

  Note: Performance levels represent qualitative assessments. Citations refer to papers that specifically apply these RL algorithms to the mentioned financial applications.

The taxonomy reveals several key insights. Actor-critic methods, particularly DDPG and its variants, demonstrate strong performance in market making applications, reflecting their suitability for continuous action spaces common in financial decision making. Policy-based methods show robust performance in cryptocurrency trading, with PPO achieving high performance levels across different market conditions. Value-based methods, while showing more modest improvements, offer greater stability and are preferred for applications requiring discrete decision making.

### 5.2 Comparative Performance Analysis

Table [2](https://arxiv.org/html/2512.10913v1#S5.T2 "Table 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") provides a detailed comparison of RL approaches across different financial applications. The performance metrics represent aggregated results from the meta-analysis of 167 studies, with Sharpe ratios reflecting typical performance ranges observed across multiple implementations within each algorithm-application category rather than results from individual studies.

Table 2: Performance Comparison of RL Approaches in Finance with Literature Citations

| Method Category | Algorithm | Application | Dataset Type | Performance Level | Complexity | Key Findings | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Deep RL | DDPG | Market Making | High-frequency | High | High | Best for continuous actions | Spooner et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib64)) |
| Deep RL | PPO | Crypto Trading | Daily OHLCV | High | Medium | Robust across markets | [Li et al., 2019b](https://arxiv.org/html/2512.10913v1#bib.bib43) |
| Deep RL | SAC | Forex Trading | Minute-level | High | High | Handles volatility well | Théate and Ernst, ([2021](https://arxiv.org/html/2512.10913v1#bib.bib67)) |
| Deep RL | TD3 | Options Trading | Options chain | Moderate-High | High | Reduces overestimation | Buehler et al., ([2019](https://arxiv.org/html/2512.10913v1#bib.bib12)) |
| Hybrid | LSTM-DDPG | Portfolio Mgmt | Fundamental + Technical | Moderate-High | Very High | Combines memory + RL | Zhang et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib77)) |
| Traditional RL | Q-Learning | Asset Allocation | Monthly returns | Moderate | Low | Simple but limited | Moody and Saffell, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib55)) |
| Multi-Agent | MADDPG | Market Simulation | Synthetic | Moderate | Very High | Models interactions | [Lussange et al., 2021b](https://arxiv.org/html/2512.10913v1#bib.bib49) |
| Model-Based | PETS | Risk Management | Historical VaR | Moderate | Very High | Sample efficient | Halperin, ([2020](https://arxiv.org/html/2512.10913v1#bib.bib32)) |
| Ensemble | Rainbow DQN | Algorithmic Trading | Multi-asset | Moderate-High | High | Robust performance | Lei et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib41)) |
| Hierarchical | HAC | Long-term Investing | Quarterly data | Moderate | High | Strategic planning | Liu et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib46)) |

* 1.

  Note: Performance levels represent qualitative assessments based on reported results in the cited literature. Specific quantitative metrics vary by study methodology and evaluation criteria.




Table 3: Recent Studies in RL for Financial Decision Making (2017-2024)

| Application | RL Method | Dataset | Key Contribution | Performance Metric | Reference |
| --- | --- | --- | --- | --- | --- |
| Portfolio Management | DDPG, PPO | Cryptocurrency data | Deep RL framework | Outperformed benchmarks | Jiang et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib38)) |
| Market Making | DDPG | Order book simulation | Optimal bid-ask spread | Improved profitability | Spooner et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib64)) |
| Algorithmic Trading | PPO, A3C | Stock market data | Robust deep RL | Superior risk-adjusted returns | [Li et al., 2019b](https://arxiv.org/html/2512.10913v1#bib.bib43) |
| Portfolio Optimization | Deep RL ensemble | Multi-asset data | Deep learning approach | Enhanced Sharpe ratios | Zhang et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib77)) |
| Quantitative Trading | Imitative RL | Stock market data | Adaptive trading strategy | Improved performance | Liu et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib46)) |
| Algorithmic Trading | Deep RL | Financial time series | Practical implementation | Positive returns | Théate and Ernst, ([2021](https://arxiv.org/html/2512.10913v1#bib.bib67)) |
| Portfolio Management | Deep RL | Market data | Markowitz-RL bridge | Risk-return optimization | Benhamou et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib9)) |
| General Finance | Various RL methods | Multiple datasets | Comprehensive survey | Theoretical framework | Charpentier et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib16)) |
| Mathematical Finance | RL theory | Theoretical analysis | Mathematical foundations | Convergence guarantees | [Hambly et al., 2023b](https://arxiv.org/html/2512.10913v1#bib.bib34) |
| Forex Trading | Q-learning, SARSA | Currency pairs | RL for forex | Profitable strategies | [Carapuço et al., 2018b](https://arxiv.org/html/2512.10913v1#bib.bib14) |
| Portfolio Trading | Recurrent RL | Stock data | Risk-return optimization | Maximum drawdown control | Almahdi and Yang, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib3)) |
| Derivative Pricing | Q-learning | Options data | QLBS framework | Black-Scholes enhancement | Halperin, ([2020](https://arxiv.org/html/2512.10913v1#bib.bib32)) |

* 1.

  Note: Performance metrics are as reported in original studies. Specific quantitative results vary by methodology and evaluation criteria used by each research group.




Table 4: Implementation Challenges and Solutions in Financial RL with Literature Citations

| Challenge Category | Specific Issues | Proposed Solutions | Solution Maturity | Regulatory Considerations | Reference |
| --- | --- | --- | --- | --- | --- |
| Data Quality | Non-stationarity | Domain adaptation, transfer learning | Moderate | Data governance compliance | [Tsantekidis et al., 2017b](https://arxiv.org/html/2512.10913v1#bib.bib69) |
| Missing data | Imputation with uncertainty | Moderate | Data completeness requirements | Heaton et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib37)) |
| Survivorship bias | Bias-aware sampling | High | Historical data accuracy | Harvey et al., ([2016](https://arxiv.org/html/2512.10913v1#bib.bib35)) |
| Model Robustness | Overfitting | Regularization, early stopping | High | Model validation standards | Liang et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib44)) |
| Distribution shift | Robust optimization | Moderate | Stress testing requirements | Cont, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib19)) |
| Adversarial attacks | Defensive training | Low | Security compliance | García and Fernández, ([2015](https://arxiv.org/html/2512.10913v1#bib.bib27)) |
| Scalability | High-dimensional states | Feature selection, dimensionality reduction | High | Computational transparency | Aldridge, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib2)) |
| Real-time constraints | Model compression, edge computing | Moderate | Latency requirements | Fabozzi et al., ([2010](https://arxiv.org/html/2512.10913v1#bib.bib23)) |
| Multi-asset complexity | Hierarchical decomposition | Moderate | Portfolio size limits | Kolm and Rémi, ([2019](https://arxiv.org/html/2512.10913v1#bib.bib40)) |
| Interpretability | Black-box decisions | Attention mechanisms, SHAP | Low-Moderate | Explainability mandates | Doshi-Velez and Kim, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib21)) |
| Risk attribution | Gradient-based explanations | Moderate | Risk reporting standards | Puiutta and Veith, ([2020](https://arxiv.org/html/2512.10913v1#bib.bib57)) |
| Regulatory compliance | Rule-based constraints | High | Audit trail requirements | [Gomber et al., 2017b](https://arxiv.org/html/2512.10913v1#bib.bib29) |
| Risk Management | Tail risk exposure | Distributional RL, CVaR optimization | Moderate | Risk limit compliance | McNeil et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib51)) |
| Model risk | Ensemble methods, validation | High | Model risk frameworks | [Roncalli, 2020a](https://arxiv.org/html/2512.10913v1#bib.bib60) |
| Operational risk | Monitoring systems, circuit breakers | High | Operational controls | Aldridge, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib2)) |
| Market Impact | Price manipulation | Market impact models | Moderate | Market abuse regulations | Cartea et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib15)) |
| Liquidity constraints | Volume-aware execution | High | Best execution requirements | Almgren and Chriss, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib5)) |
| Systemic risk | Coordination mechanisms | Low | Systemic risk monitoring | Cont et al., ([2010](https://arxiv.org/html/2512.10913v1#bib.bib20)) |

* 1.

  Note: Solution maturity levels represent qualitative assessments based on literature review. Specific effectiveness varies by implementation context and market conditions.

Market making applications typically exhibit the highest performance gains, as demonstrated in Figure [5](https://arxiv.org/html/2512.10913v1#S5.F5 "Figure 5 ‣ 5.3 Empirical Validation of Meta-Analysis Findings ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") where market making shows the highest RL premium among all application domains. The superior performance aligns well with the fact that market making is usually a continuous control problem, and that, of course, is as tightly connected to the order book and optimization of the bid/ask spread as it can be. Cryptocurrency trading applications follow as the second-highest performing domain, likely due to the greater reactive volatility and inefficiencies in these markets, which can be effectively exploited with RL algorithms. To investigate these performance discrepancies in a systematic way, a formal statistical meta-analysis of all 167 studies was conducted and the results shed light on what really matters for RL to work in financial applications. The comprehensive analysis presented in Figure [2](https://arxiv.org/html/2512.10913v1#S5.F2 "Figure 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") reveals important insights about the factors influencing RL performance across different financial applications and market conditions.

![Refer to caption](meta_analysis_figure.png)


Figure 2: RL premium analysis. (a) Linear regression to analyze the relationship between the RL premium and feature dimensions. (b) Linear regression to analyze the relationship between the RL premium and number of assets. (c) Box plots comparing the RL premium based on whether the reward model uses return or shaped return. (d) Linear regression to analyze the relationship between the RL premium and years of training period. (e) Box plots comparing the RL premium based on whether the training period includes a recession. (f) Box plot analysis of the RL premium, contrasting outcomes from the RL PG and DQN strategies. Abbreviations: DQN, deep Q-network; PG, policy gradient; RL, reinforcement learning.

Figure [2](https://arxiv.org/html/2512.10913v1#S5.F2 "Figure 2 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") presents a comprehensive meta-analysis of factors influencing reinforcement learning (RL) performance across 167 financial applications published between 2020-2025. Each panel examines a different potential performance driver through statistical analysis.

Panel (a) examines the relationship between RL performance premium and feature dimensionality through linear regression analysis. The weak positive slope (0.171) and high p-value (0.499) indicate no statistically significant relationship between the number of features used and RL performance improvements, challenging the common assumption that higher-dimensional state spaces necessarily lead to better results.

Panel (b) analyzes the correlation between RL premium and portfolio complexity measured by the number of assets. The minimal slope (0.010) and non-significant p-value (0.362) suggest that RL benefits do not scale with portfolio size, indicating that the advantages of RL may be more related to adaptive learning capabilities than to handling high-dimensional optimization problems.

Panel (c) compares RL performance between studies using simple return-based rewards versus shaped reward functions through box plot analysis. The modest difference and non-significant p-value (0.120) suggest that sophisticated reward engineering may provide less benefit than commonly assumed, with both approaches showing similar median performance.

Panel (d) investigates the relationship between training period length and RL performance. The weak correlation (slope = 0.023, p-value = 0.591) indicates that longer training periods do not necessarily lead to better performance, suggesting that training efficiency and data quality may be more important than training duration.

Panel (e) examines whether including recession periods in training data affects RL performance. The comparison between studies covering the Great Recession versus those that do not shows no significant difference (p-value = 0.604), indicating that RL algorithms may be robust to different market regimes when properly implemented.

Panel (f) contrasts performance between Policy Gradient (PG) and Deep Q-Network (DQN) algorithm families. The similar distributions and non-significant difference (p-value = 0.640) support the finding that algorithm choice is less critical than implementation quality and domain-specific enhancements.

Aligning with the previously determined findings, the results suggest that RL successfulness in finance is mostly the result of implementation quality, data pre-processing, and domain knowledge instead of algorithmic complexity or feature engineering.

Recent RL studies in finance emphasize diverse methodologies and applications. Table [3](https://arxiv.org/html/2512.10913v1#S5.T3 "Table 3 ‣ 5.2 Comparative Performance Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") outlines influential studies (2017-2024), detailing notable contributions and outcomes across financial applications. Key advancements include ensemble methods for cryptocurrency trading, market making optimization, deep RL for portfolio management, and adaptive quantitative trading strategies. These studies demonstrate the diversity of RL applications and potential for performance gains through tailored implementations and high-quality execution.

### 5.3 Empirical Validation of Meta-Analysis Findings

Synthetic data mirroring key statistical patterns was used to validate the meta-analysis findings, addressing confidential data concerns and allowing thorough statistical validation.

![Refer to caption](figures/correlation_matrix_performance_factors.png)


Figure 3: Correlation matrix analysis of performance factors in RL financial applications. The analysis confirms weak correlations between technical factors (feature dimensions, training years, number of assets) and RL performance, validating meta-analysis findings. Sample size shows the strongest correlation (r=0.2) with performance, emphasizing data quality over algorithmic sophistication.

Figure [3](https://arxiv.org/html/2512.10913v1#S5.F3 "Figure 3 ‣ 5.3 Empirical Validation of Meta-Analysis Findings ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") presents the correlation matrix analysis that validates the meta-analysis findings, confirming the weak correlations identified in the literature review: feature dimensions with r = -0.0054 (confirming p = 0.499), training years with r = -0.0086 (confirming p = 0.591), number of assets with r = 0.06 (confirming p = 0.362), and sample size with r = 0.2 represents the strongest correlation, emphasizing data quality.

![Refer to caption](figures/feature_importance_random_forest.png)


Figure 4: Feature importance analysis using Random Forest regression. Complexity score and market making domain emerge as the most important predictors of RL performance, while algorithmic factors show minimal importance. This analysis supports the conclusion that implementation quality and domain-specific factors dominate over algorithmic sophistication.

Figure [4](https://arxiv.org/html/2512.10913v1#S5.F4 "Figure 4 ‣ 5.3 Empirical Validation of Meta-Analysis Findings ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") presents a feature importance analysis via Random Forest regression. The complexity score (0.31) is the top predictor, signifying implementation quality, followed closely by the market making domain (0.28), highlighting domain-specific dominance. Sample size (0.19) emphasizes data quality over algorithm choice, while algorithm family (0.08) is least important, aligning with meta-analysis results.

![Refer to caption](figures/performance_analysis_by_categories.png)


Figure 5: Performance analysis by application domain and algorithm family. Market making shows the highest RL premium (0.488), followed by cryptocurrency trading (0.375). Algorithm family differences are minimal within domains, supporting the finding that domain expertise matters more than algorithmic choice.

Figure [5](https://arxiv.org/html/2512.10913v1#S5.F5 "Figure 5 ‣ 5.3 Empirical Validation of Meta-Analysis Findings ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") illustrates domain effects influencing RL performance differences. Market making shows the highest RL premium (0.488), confirming the meta-analysis. Small variations among algorithm families within domains suggest that implementation quality and domain expertise surpass algorithmic complexity.

### 5.4 Advanced Statistical Analysis

![Refer to caption](figures/pca_analysis_features_algorithms.png)


Figure 6: Principal Component Analysis (PCA) of features and algorithms. The analysis reveals no clear algorithmic clustering, with performance variation explained primarily by implementation and domain factors rather than algorithm choice. This finding supports the meta-analysis conclusion that algorithm selection is less critical than commonly assumed.

Figure [6](https://arxiv.org/html/2512.10913v1#S5.F6 "Figure 6 ‣ 5.4 Advanced Statistical Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows the PCA analysis of RL performance factors. It highlights that implementation quality and domain-specific factors are more crucial than algorithm choice, with the first two components explaining 67% of the variance.

![Refer to caption](figures/risk_adjusted_performance_analysis.png)


Figure 7: Risk-adjusted performance analysis across different RL applications. The analysis shows that while returns vary significantly, risk-adjusted metrics (Sharpe ratios) provide more stable performance comparisons. Market making and cryptocurrency applications maintain superior risk-adjusted performance, validating the robustness of the findings.

Figure [7](https://arxiv.org/html/2512.10913v1#S5.F7 "Figure 7 ‣ 5.4 Advanced Statistical Analysis ‣ 5 Meta-Analysis of Performance and Methodologies ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") demonstrates the importance of risk-adjusted performance metrics in evaluating RL applications. The analysis shows that while raw returns vary significantly across applications, risk-adjusted metrics provide more stable and meaningful comparisons. Market making and cryptocurrency applications maintain their superior performance even after risk adjustment.

## 6 Temporal Evolution and Emerging Trends

### 6.1 Performance Evolution Over Time

The temporal analysis of RL performance in financial applications reveals important trends in algorithmic development and adoption patterns. Figure [8](https://arxiv.org/html/2512.10913v1#S6.F8 "Figure 8 ‣ 6.1 Performance Evolution Over Time ‣ 6 Temporal Evolution and Emerging Trends ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows the evolution of RL performance across different application domains from 2017 to 2025.

![Refer to caption](figures/temporal_performance_analysis.png)


Figure 8: Temporal evolution of RL performance across financial applications (2020-2025). The analysis shows steady improvement in market making and cryptocurrency applications, with ESG investing emerging as a high-growth area. Performance improvements have plateaued in traditional portfolio optimization, suggesting market maturity.

The temporal analysis highlights several key trends: Market making applications have consistently shown the highest performance improvements, with Sharpe ratio increases from 0.35 in 2020 to 0.52 in 2025. Cryptocurrency trading applications have experienced rapid performance improvements, especially after 2022, due to market maturation and algorithmic advances. ESG (Environmental, Social, and Governance) investing has emerged as a high-growth area, with notable performance improvements accelerating after 2023. In contrast, traditional portfolio optimization has plateaued, indicating market maturity and the need for innovative approaches.

### 6.2 Market Regime Analysis

![Refer to caption](figures/market_regime_analysis.png)


Figure 9: RL performance analysis across different market regimes. The analysis shows that RL algorithms maintain robust performance across bull, bear, and volatile market conditions, with market making showing particular resilience during volatile periods. This robustness supports the practical viability of RL approaches in real-world financial environments.

Figure [9](https://arxiv.org/html/2512.10913v1#S6.F9 "Figure 9 ‣ 6.2 Market Regime Analysis ‣ 6 Temporal Evolution and Emerging Trends ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") examines RL performance across different market regimes, revealing important insights about the robustness of RL approaches. Market making applications show particular resilience during volatile periods, while cryptocurrency trading benefits from high volatility environments. Traditional portfolio optimization shows more sensitivity to market conditions, suggesting the need for regime-aware approaches.

## 7 Advanced Insights and Comprehensive Analysis

### 7.1 Multidimensional Performance Analysis

The comprehensive analysis of RL performance in financial applications requires examination of multiple dimensions simultaneously. Figure [10](https://arxiv.org/html/2512.10913v1#S7.F10 "Figure 10 ‣ 7.1 Multidimensional Performance Analysis ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") provides a holistic view of the factors influencing RL success across different applications and market conditions.

![Refer to caption](figures/comprehensive_dashboard_visualizations.png)


Figure 10: Comprehensive dashboard of RL performance factors in financial applications. The multi-panel analysis provides a holistic view of performance drivers, showing the dominance of domain-specific factors over algorithmic sophistication. The dashboard integrates correlation analysis, feature importance, temporal trends, and risk-adjusted performance metrics.

The comprehensive dashboard analysis reveals several key insights: Application domain emerges as the strongest predictor of RL performance, with market making and cryptocurrency trading consistently outperforming other applications. The complexity score, representing implementation sophistication, shows a strong correlation with performance across all domains. Sample size and data quality metrics display a consistent positive correlation with performance, highlighting the importance of high-quality training data. Minimal differences between algorithm families within domains confirm that implementation quality matters more than algorithmic choice.

### 7.2 Network Effects and Emergent Patterns

The analysis reveals emergent patterns in RL adoption and performance that suggest network effects and knowledge spillovers between different application domains. Figure [11](https://arxiv.org/html/2512.10913v1#S7.F11 "Figure 11 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") provides comprehensive evidence for these phenomena, demonstrating both the quantitative performance advantages and the structural patterns of knowledge transfer across financial RL applications.

![Refer to caption](figures/Network_Effects_Hybrid_Analysis.png)


Figure 11: Network Effects, Knowledge Spillovers, and Hybrid Approaches in Financial RL. (a) Performance comparison between hybrid and pure RL approaches, showing 15-20% improvements for hybrid methods across different algorithms. (b) Knowledge spillover network diagram illustrating market making as the central hub for technique transfer to other financial domains. (c) Temporal adoption trends showing increasing hybrid approach adoption from 15% in 2020 to 42% in 2025. (d) Performance versus complexity analysis demonstrating optimal trade-offs for hybrid approaches (Sharpe ratio 1.57) compared to pure RL (1.35) and traditional methods (0.95). (e) Cross-domain transfer matrix quantifying knowledge spillover strengths between financial applications, with market making showing highest transfer rates (0.6-0.9). (f) Critical success factors for hybrid approaches, highlighting implementation quality (0.92) and domain expertise (0.85) as most important determinants. The analysis demonstrates that hybrid approaches combining RL with traditional quantitative methods achieve superior performance while leveraging cross-domain knowledge spillovers, particularly from market making innovations.

Effective market making has influenced various fields by sharing ideas and methods. As shown in Panel (b) of Figure [11](https://arxiv.org/html/2512.10913v1#S7.F11 "Figure 11 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies"), it serves as a central hub in a spillover network, strongly connecting to portfolio optimization, cryptocurrency trading, risk management, and execution trading. Panel e in Figure [11](https://arxiv.org/html/2512.10913v1#S7.F11 "Figure 11 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") displays the transfer matrix, indicating strong transfer strengths from market making to other domains, ranging from 0.6 to 0.9, which are notably higher than other domain pairs.

Table [6](https://arxiv.org/html/2512.10913v1#S7.T6 "Table 6 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") provides evidence of significant spillover between domains, where market making practices enhanced performance. Inventory management techniques improved portfolio optimization by 12% in risk-adjusted returns, and bid-ask optimization in cryptocurrency trading increased execution efficiency by 18%. Knowledge transfer mainly occurred from 2020-2022, reflecting rapid dissemination of market making innovations.

Hybrid methods combining RL with traditional quantitative techniques show a significant trend, enhancing performance by 15-20% over standard RL. Figure [11](https://arxiv.org/html/2512.10913v1#S7.F11 "Figure 11 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") Panel (a) highlights LSTM-DQN with a 15.4% gain in portfolio optimization, CNN-PPO with a 17.9% increase in cryptocurrency trading, and Attention-DDPG with a 16.3% boost in market making.

Table [5](https://arxiv.org/html/2512.10913v1#S7.T5 "Table 5 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows performance data for eight hybrid methods, with consistent performance improvements between 15.4% and 19.2% for financial applications. It also lists knowledge sources, illustrating how computer vision (CNN), natural language processing (attention mechanisms), and time series (LSTM) were integrated with RL algorithms to enhance financial decision making.

Panel (c) of Figure [11](https://arxiv.org/html/2512.10913v1#S7.F11 "Figure 11 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") shows that hybrid approach adoption increased from 15% in 2020 to 42% in 2025, while pure RL adoption decreased from 85% to 58% in the same period. This suggests the field’s maturation and recognition that combining domain knowledge with adaptive learning outperforms either alone.

Table [7](https://arxiv.org/html/2512.10913v1#S7.T7 "Table 7 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") highlights that implementation quality (0.92) and domain knowledge (0.85) are the key success factors for hybrid approaches, while algorithm choice is less important (0.45). This supports the meta-analysis conclusion that practical implementation is more crucial than designing sophisticated algorithms. Enhancing implementation quality can increase system reliability by up to 25% and performance by 5-20% with domain knowledge.

Table [6](https://arxiv.org/html/2512.10913v1#S7.T6 "Table 6 ‣ 7.2 Network Effects and Emergent Patterns ‣ 7 Advanced Insights and Comprehensive Analysis ‣ Reinforcement Learning in Financial Decision Making: A Systematic Review of Performance, Challenges, and Implementation Strategies") illustrates the systematic transfer of innovations across financial RL applications. The impact of market making innovations on behavior showed the highest transfer effects. Dynamic hedging, order flow modeling, and bid-ask dynamics were adapted for risk management, execution trading, and cryptocurrency applications, respectively, resulting in performance impacts of 5-18%, indicating significant value creation through cross-domain spillover.

Table 5: Hybrid Approaches vs Pure RL: Methodological Analysis with Literature Citations

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Approach Type | Specific Method | Application Domain | Performance Level | Relative Improvement | Key Innovation | Reference |
| Pure RL | DQN | Portfolio Optimization | Moderate | Baseline | Deep Q-learning | Jiang et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib38)) |
| PPO | Cryptocurrency Trading | Moderate-High | Baseline | Policy optimization | [Li et al., 2019b](https://arxiv.org/html/2512.10913v1#bib.bib43) |
| DDPG | Market Making | High | Baseline | Continuous control | Spooner et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib64)) |
| SAC | Forex Trading | Moderate-High | Baseline | Maximum entropy | Théate and Ernst, ([2021](https://arxiv.org/html/2512.10913v1#bib.bib67)) |
| TD3 | Options Trading | Moderate-High | Baseline | Twin critics | Buehler et al., ([2019](https://arxiv.org/html/2512.10913v1#bib.bib12)) |
| A3C | Multi-asset Trading | Moderate | Baseline | Asynchronous learning | Mnih et al., ([2016](https://arxiv.org/html/2512.10913v1#bib.bib53)) |
| Hybrid Approaches | LSTM-RL | Portfolio Optimization | High | Significant | Temporal modeling | Fischer and Krauss, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib26)) |
| CNN-RL | Pattern Recognition | High | Significant | Feature extraction | Sezer et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib62)) |
| Attention-RL | Market Making | High | Moderate | Feature selection | Zhang et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib76)) |
| Transformer-RL | Time Series Analysis | High | Significant | Sequence modeling | Wu et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib73)) |
| GAN-RL | Data Augmentation | Moderate-High | Moderate | Synthetic data | Yoon et al., ([2019](https://arxiv.org/html/2512.10913v1#bib.bib74)) |
| Graph-RL | Multi-asset Trading | Moderate-High | Moderate | Relationship modeling | Feng et al., ([2019](https://arxiv.org/html/2512.10913v1#bib.bib25)) |
| Ensemble-RL | Risk Management | High | Significant | Robustness | Zhang et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib77)) |
| Meta-RL | Cross-market Trading | Moderate-High | Moderate | Fast adaptation | Wang et al., ([2016](https://arxiv.org/html/2512.10913v1#bib.bib72)) |

* 1.

  Note: Performance levels and improvements are qualitative assessments based on reported results in cited literature. Specific quantitative metrics vary by study methodology and evaluation criteria.




Table 6: Knowledge Spillover Patterns and Cross-Domain Technique Transfer with Literature Citations

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Source Domain | Target Domain | Transferred Technique | Transfer Strength | Key Innovation | Reference |
| Market Making | Portfolio Optimization | Inventory management | High | Risk-aware position sizing | Cartea et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib15)) |
| Cryptocurrency Trading | Bid-ask optimization | Very High | Spread optimization strategies | Spooner et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib64)) |
| Risk Management | Dynamic hedging | Moderate | Real-time risk adjustment | Almgren and Chriss, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib5)) |
| Execution Trading | Order flow modeling | High | Market microstructure insights | Hasbrouck, ([2007](https://arxiv.org/html/2512.10913v1#bib.bib36)) |
| Portfolio Optimization | Risk Management | Constraint optimization | High | Multi-objective frameworks | Markowitz, ([1952](https://arxiv.org/html/2512.10913v1#bib.bib50)) |
| Execution Trading | Multi-objective optimization | Moderate | Trade-off management | Bertsimas and Lo, ([1998](https://arxiv.org/html/2512.10913v1#bib.bib10)) |
| Cryptocurrency Trading | Rebalancing strategies | Low | Dynamic allocation methods | Benhamou et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib9)) |
| Cryptocurrency Trading | Execution Trading | High-frequency patterns | Moderate | Pattern recognition techniques | [Li et al., 2019b](https://arxiv.org/html/2512.10913v1#bib.bib43) |
| Portfolio Optimization | Volatility modeling | Low | Risk estimation methods | Zhang et al., ([2020](https://arxiv.org/html/2512.10913v1#bib.bib77)) |
| Risk Management | Extreme event handling | Low | Tail risk methodologies | McNeil et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib51)) |
| Risk Management | Portfolio Optimization | Stress testing | High | Robustness evaluation | Jorion, ([2007](https://arxiv.org/html/2512.10913v1#bib.bib39)) |
| Execution Trading | Risk-aware execution | Moderate | Risk-constrained optimization | Almgren, ([2003](https://arxiv.org/html/2512.10913v1#bib.bib4)) |
| Market Making | Regulatory compliance | High | Compliance frameworks | [Gomber et al., 2017b](https://arxiv.org/html/2512.10913v1#bib.bib29) |
| Execution Trading | Market Making | Order book dynamics | High | Microstructure modeling | Gould et al., ([2013](https://arxiv.org/html/2512.10913v1#bib.bib31)) |
| Portfolio Optimization | Transaction cost modeling | Moderate | Cost-aware optimization | Perold, ([1988](https://arxiv.org/html/2512.10913v1#bib.bib56)) |
| Risk Management | Real-time monitoring | Moderate | Dynamic risk assessment | Aldridge, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib2)) |

* 1.

  Note: Transfer strength levels represent qualitative assessments based on literature review of cross-domain applications. Specific effectiveness varies by implementation context and market conditions.




Table 7: Critical Success Factors for Hybrid RL Approaches in Finance with Literature Citations

| Success Factor | Importance Level | Implementation Challenges | Best Practices | Reference |
| --- | --- | --- | --- | --- |
| Implementation Quality | Critical | Integration complexity, debugging | Modular design, extensive testing | Lopez de Prado, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib47)) |
| Domain Expertise | High | Knowledge acquisition, validation | Expert collaboration, domain adaptation | Kolm and Rémi, ([2019](https://arxiv.org/html/2512.10913v1#bib.bib40)) |
| Data Quality | High | Multi-source integration, cleaning | Robust preprocessing, validation | Harvey et al., ([2016](https://arxiv.org/html/2512.10913v1#bib.bib35)) |
| Risk Management | Moderate-High | Dynamic risk assessment, control | Adaptive limits, monitoring | McNeil et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib51)) |
| Algorithm Choice | Moderate | Selection criteria, optimization | Systematic evaluation, benchmarking | Charpentier et al., ([2021](https://arxiv.org/html/2512.10913v1#bib.bib16)) |
| Model Interpretability | High | Black-box nature, explainability | Attention mechanisms, SHAP analysis | Doshi-Velez and Kim, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib21)) |
| Regulatory Compliance | Critical | Evolving requirements, documentation | Audit trails, compliance frameworks | [Gomber et al., 2017b](https://arxiv.org/html/2512.10913v1#bib.bib29) |
| Computational Efficiency | Moderate-High | Real-time constraints, scalability | Model compression, parallel processing | Aldridge, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib2)) |
| Market Regime Adaptation | High | Non-stationarity, regime changes | Transfer learning, adaptive models | Cont, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib19)) |
| Backtesting Rigor | High | Overfitting, data snooping | Walk-forward analysis, out-of-sample testing | Bailey et al., ([2014](https://arxiv.org/html/2512.10913v1#bib.bib7)) |

* 1.

  Note: Importance levels represent qualitative assessments based on literature review and practitioner insights. Specific impact varies by implementation context and market conditions.

Network effects and patterns impact research and practice. For researchers, innovation in one area can apply broadly to financial RL, highlighting the importance of collaboration and knowledge sharing. For practitioners, a hybrid approach combining traditional quantitative methods with adaptive RL is supported, stressing implementation quality and domain expertise over algorithm complexity.

### 7.3 Implementation Frameworks and Practical Considerations

#### 7.3.1 System Architecture and Design Principles

Deploying RL systems in finance requires advanced architectures that meet market challenges while keeping RL’s flexibility. Key principles include modular design for independent development and testing, layered architecture with data processing, feature engineering, RL decision-making, execution, risk management, and compliance. The data layer should manage diverse data types and ensure quality and consistency, using distributed frameworks for high-volume, real-time applications. Risk management must adapt dynamically to RL strategies with proper oversight, replacing static systems.

#### 7.3.2 Deployment and Monitoring Considerations

Deploying RL systems in production requires specialized strategies for reliable operation and regulatory compliance. Their adaptive nature demands advanced monitoring and validation beyond traditional financial systems. Real-time monitoring must track execution latency, decision accuracy, and profitability, providing alerts for performance issues or anomalies. Model drift detection is essential for identifying when RL models underperform due to market changes or degradation. Validating RL systems needs methods tailored to their adaptability, as traditional backtesting isn’t suitable, requiring new validation approaches to evaluate adaptive behavior under varied conditions.

## 8 Challenges and Limitations

Reinforcement learning in financial decision-making encounters fundamental challenges affecting its practicality and adoption, due to the unique nature of financial markets and the strict demands of financial applications, unlike other RL domains.

### 8.1 Non-Stationarity and Market Dynamics

A key challenge in applying RL to financial markets is their non-stationary nature. Traditional RL algorithms assume stationary environments with constant dynamics, but financial markets evolve due to changing behavior, regulations, technology, and macroeconomic shifts Moody and Saffell, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib55)). This non-stationarity can degrade RL performance.

Tsantekidis et al. [Tsantekidis et al., 2017a](https://arxiv.org/html/2512.10913v1#bib.bib68)  show that changing market microstructure patterns hinder RL agents’ consistent performance, as strategies optimized for one period often fail later due to evolving dynamics. Similarly, Jiang et al. Jiang et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib38)) find that deep RL models trained on historical data degrade significantly in live trading due to market non-stationarity. Non-stationarity is exacerbated by adaptive financial markets, where new algorithms change dynamics and reduce the effectiveness of existing strategies. Farmer and Skouras Farmer and Skouras, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib24)) note this "arms race," where popular strategies become less profitable as they are widely adopted, requiring continuous adaptation and evolution of RL strategies.

### 8.2 Sample Efficiency and Data Limitations

Sample efficiency is a major limitation in financial RL, as data collection is costly and experimenting entails financial risks. Unlike domains with cheap simulated environments, financial RL relies on limited historical data or costly real-world interactions Sutton and Barto, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib65)). Liang et al. Liang et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib44)) address the sample efficiency issue in deep RL applications in finance, observing that financial institutions hesitate to permit extensive experimentation with actual capital due to the risk of losses. This restriction curbs RL agents’ exploration, possibly obstructing their discovery of optimal strategies. Complex temporal dependencies and regime changes in financial data require large datasets for effective learning. Heaton et al. Heaton et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib37)) show that deep RL models need more training data than traditional machine learning for similar performance, highlighting sample efficiency as a key practical issue. Financial data quality and availability pose challenges. Historical data often have biases like survivorship and look-ahead, causing overly optimistic backtesting outcomes Harvey et al., ([2016](https://arxiv.org/html/2512.10913v1#bib.bib35)). These issues can heavily affect the training and real-world performance of RL agents.

### 8.3 Exploration-Exploitation Trade-off in High-Stakes Environments

The exploration-exploitation trade-off poses challenges in finance, as exploration can lead to significant losses. Random exploration in traditional RL is often unsuitable, favoring conservative strategies in financial settings García and Fernández, ([2015](https://arxiv.org/html/2512.10913v1#bib.bib27)). García and Fernández García and Fernández, ([2015](https://arxiv.org/html/2512.10913v1#bib.bib27)) survey safe reinforcement learning techniques, highlighting the importance of secure exploration in financial domains to avoid failures and significant monetary losses due to random action selection.

The challenge is compounded by financial markets’ extreme events and tail risks, which are hard to predict during training. Cont Cont, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib19)) shows that financial returns have heavy-tailed distributions and more frequent extreme events than normal distributions predict, hindering RL agents from learning effective risk management strategies through exploration alone. Researchers have developed safe exploration methods for finance. Moody and Saffell Moody and Saffell, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib55)) introduce risk-adjusted measures to penalize excessive risk, while Almahdi and Yang Almahdi and Yang, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib3)) suggest adaptive strategies that vary exploration rates with market volatility and uncertainty.

### 8.4 Regulatory Compliance and Interpretability Requirements

The regulatory landscape for RL in finance poses challenges for responsible innovation and market integrity. Financial regulations demand that automated trading systems be explainable and auditable, conflicting with the opaque nature of deep RL methods Doshi-Velez and Kim, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib21)). The EU’s Markets in Financial Instruments Directive (MiFID II) and similar global regulations mandate that financial institutions explain their algorithmic trading strategies and ensure they don’t cause market manipulation or instability [Gomber et al., 2017a](https://arxiv.org/html/2512.10913v1#bib.bib28) . This is challenging for deep RL systems, which tend to be "black boxes" with limited interpretability.

Doshi-Velez and Kim Doshi-Velez and Kim, ([2017](https://arxiv.org/html/2512.10913v1#bib.bib21)) highlight that in finance, interpretability is crucial because of the systemic risks from algorithmic trading. Financial RL systems need to not only excel in performance but also clearly explain decisions to meet regulations and uphold public trust. Interpretability in RL is challenging due to the evolving nature of policies as agents learn and adapt. Static model interpretability methods may not suit dynamic RL policies, requiring novel approaches tailored for RL systems Puiutta and Veith, ([2020](https://arxiv.org/html/2512.10913v1#bib.bib57)).

### 8.5 Market Microstructure and Impact Modeling

Market microstructure effects complicate high-frequency trading and market making. The influence of trades on prices, order book dynamics, and participant interactions must be modeled in RL frameworks Cartea et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib15)). Cartea et al. Cartea et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib15)) highlight that overlooking market impact results in poor trading strategies, especially in high-frequency, large-volume trades. They stress that RL agents need to balance execution speed and market impact through advanced market microstructure modeling. Market impact varies with market conditions, time of day, and specific assets, complicating its integration into RL frameworks. Almgren and Chriss Almgren and Chriss, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib5)) offer a theoretical framework for accounting for market impact, but adapting it to RL is challenging due to the complex, dynamic market microstructure. Spooner et al. Spooner et al., ([2018](https://arxiv.org/html/2512.10913v1#bib.bib64)) propose a multi-agent RL approach to model strategic interactions in financial markets, emphasizing the limitations of single-agent RL in capturing market complexities and the need to consider participants’ adaptive behavior.

### 8.6 Risk Management Integration

Incorporating risk management into RL is crucial and sets financial applications apart from others. Static limits and preset scenarios in traditional risk management may not suit adaptive RL strategies that evolve over time McNeil et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib51)). McNeil et al. McNeil et al., ([2015](https://arxiv.org/html/2512.10913v1#bib.bib51)) argue that traditional risk management frameworks, suited for static strategies, fail to address the risks of adaptive RL systems. They highlight the need for dynamic approaches to manage changing behaviors while ensuring oversight and control. In portfolio management, RL agents face challenges in balancing objectives such as return maximization, risk control, and regulatory compliance. Kolm et al. Kolm and Rémi, ([2019](https://arxiv.org/html/2512.10913v1#bib.bib40)) show that adding multiple risk constraints complicates the learning process and may need specialized constrained optimization algorithms. The dynamic nature of RL strategies results in changing risk profiles, challenging traditional risk management. This calls for new frameworks specialized for adaptive RL systems [Roncalli, 2020b](https://arxiv.org/html/2512.10913v1#bib.bib61) .

### 8.7 Evaluation and Validation Challenges

Evaluating financial RL systems is challenging because of the market’s non-stationarity and overfitting risks. Traditional backtesting may fail to accurately assess adaptive systems in dynamic conditions Bailey et al., ([2014](https://arxiv.org/html/2512.10913v1#bib.bib7)). Bailey et al. Bailey et al., ([2014](https://arxiv.org/html/2512.10913v1#bib.bib7)) show that traditional backtesting often inflates performance estimates due to multiple testing bias and overfitting. They note this issue is acute in RL systems, which may adjust behaviors to historical patterns unlikely to persist.

RL systems have complex temporal dependencies and regime-specific behaviors that are hard to assess with standard statistical methods. Lopez de Prado Lopez de Prado, ([2018](https://arxiv.org/html/2512.10913v1#bib.bib47)) suggests advanced backtesting techniques like purged and combinatorial purged cross-validation for machine learning strategies, but these might not suffice for complex RL systems. Out-of-sample testing in financial markets is challenging due to the lack of independent test data. Financial markets offer a single realization of the stochastic process, making it hard to achieve statistically significant out-of-sample results Harvey et al., ([2016](https://arxiv.org/html/2512.10913v1#bib.bib35)).

### 8.8 Computational and Scalability Challenges

Financial RL systems face deployment challenges, especially in high-frequency applications needing sub-millisecond decisions. Processing large, high-dimensional data in real-time with low latency is a significant technical hurdle Aldridge, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib2)). Aldridge Aldridge, ([2013](https://arxiv.org/html/2512.10913v1#bib.bib2)) shows that achieving necessary performance in high-frequency trading systems demands specialized hardware and software. Integrating RL algorithms introduces extra computational overhead that must be managed to stay competitive.

Scalability is challenged by managing multiple assets, time frames, and market conditions concurrently. Portfolio optimization must account for numerous assets, each with unique dynamics and constraints, necessitating advanced distributed computing architectures Fabozzi et al., ([2010](https://arxiv.org/html/2512.10913v1#bib.bib23)). Training deep RL models is computationally intensive, demanding substantial resources and time. This may hinder financial institutions from quickly adjusting strategies to market changes, potentially reducing their competitive edge Heaton et al., ([2017](https://arxiv.org/html/2512.10913v1#bib.bib37)).

### 8.9 Data Quality and Preprocessing Challenges

In financial RL, data quality and preprocessing are crucial due to noisy, incomplete data. Missing data, outliers, and biases can greatly affect RL agents’ training and performance Tsay, ([2005](https://arxiv.org/html/2512.10913v1#bib.bib70)). Tsay Tsay, ([2005](https://arxiv.org/html/2512.10913v1#bib.bib70)) overviews data quality challenges in financial time series, highlighting the need for proper preprocessing and cleaning. RL applications face acute challenges due to their sensitivity to data quality, relying on temporal patterns and sequential decisions.

Survivorship bias is a major issue in financial data, as historical datasets often only include assets or strategies that have survived, resulting in overly optimistic performance estimates Brown et al., ([1992](https://arxiv.org/html/2512.10913v1#bib.bib11)). This can greatly affect RL agents’ training and their real-world performance. Integrating diverse data sources in different formats, frequencies, and quality levels poses challenges for RL systems. Sources like news sentiment, social media, and satellite imagery offer valuable information but need advanced preprocessing and integration techniques Chinco et al., ([2019](https://arxiv.org/html/2512.10913v1#bib.bib18)).

### 8.10 Model Robustness and Generalization

Financial RL systems must be robust and generalize well to handle unseen market conditions and extreme events. Markets can experience sudden regime changes, black swan events, and other extremes not well-represented in historical data Taleb, ([2007](https://arxiv.org/html/2512.10913v1#bib.bib66)). Taleb Taleb, ([2007](https://arxiv.org/html/2512.10913v1#bib.bib66)) highlights that financial models often overlook extreme events with catastrophic effects, stressing the need for robust design and stress testing. This is crucial for RL systems susceptible to adversarial attacks or unforeseen market conditions not faced during training. The generalization challenge is further complicated by constantly evolving financial markets, with new instruments, regulations, and participants regularly introduced. RL systems must adapt while maintaining robust performance across various market conditions Cont, ([2001](https://arxiv.org/html/2512.10913v1#bib.bib19)).

Researchers have proposed techniques to enhance financial RL system robustness, like domain adaptation, transfer learning, and robust optimization. These methods entail trade-offs in performance and computational complexity, necessitating careful evaluation of application needs Ben-David et al., ([2010](https://arxiv.org/html/2512.10913v1#bib.bib8)). This section emphasizes the complexity of applying RL systems in finance, necessitating specialized methods for market-specific challenges. Despite progress, many issues persist, impacting RL’s practical use in finance.

## 9 Future Research Directions

### 9.1 Methodological Advances

The future development of RL in financial decision making requires significant methodological advances to address current limitations and unlock new capabilities. Interpretable reinforcement learning represents one of the most pressing needs, requiring the development of RL algorithms that can provide clear explanations for their decisions while maintaining competitive performance. Safe exploration techniques represent another critical area for future research, particularly for financial applications where exploration can result in substantial losses. Future research should focus on developing exploration strategies that can learn effectively while minimizing downside risk through techniques such as constrained policy optimization and uncertainty-aware exploration. Robust reinforcement learning methods that can maintain performance across different market regimes and conditions represent another important research direction. Financial markets are characterized by non-stationarity and regime changes that can significantly impact RL performance, requiring algorithms that can detect and adapt to changing conditions while maintaining robust performance.

### 9.2 Technology Integration and Emerging Applications

The integration of RL with emerging technologies presents significant opportunities for advancing financial decision making capabilities. Quantum computing integration could potentially provide exponential speedups for certain types of optimization problems central to financial decision making, though significant challenges remain in developing practical quantum RL algorithms. Edge computing integration represents a more immediate opportunity for improving the performance and scalability of financial RL applications through ultra-low latency decision making and reduced dependence on centralized computing resources. Environmental, Social, and Governance (ESG) investing represents another emerging application where RL techniques could provide significant value through optimization of multi-objective investment strategies that balance financial returns with sustainability objectives.

## 10 Conclusion

This review and meta-analysis of reinforcement learning in financial decision-making offers key contributions to research and practice. Analyzing 167 publications from 2020-2025 and validating with synthetic data, this study highlights patterns that challenge common beliefs about RL’s effectiveness in finance. The meta-analysis indicates that successful RL in finance relies more on quality implementation, domain expertise, and data quality than complex algorithms. Weak correlations between feature dimensionality, training duration, and algorithm choice with outcomes suggest focusing on domain-specific adaptations and solid implementation over complex algorithms. Empirical validation supports these findings, highlighting factors influencing RL performance. Market making and cryptocurrency trading are key applications, consistently outperforming across various market conditions. Temporal analysis shows significant trends in algorithm development, with ESG investing as a high-growth area. These findings significantly impact researchers and practitioners. Researchers are advised to prioritize interpretability, robustness, and regulatory compliance over algorithmic advancements. Practitioners gain evidence-based guidance for algorithm selection, implementation, and resource allocation.

The analysis highlights key challenges for future research: the need for interpretable RL architectures, robust exploration strategies, and comprehensive regulatory frameworks. These barriers to adoption require collaborative efforts from researchers, practitioners, and regulators. The integration of RL with emerging technologies offers significant potential for enhancing financial decision-making. The evolution of regulatory frameworks and industry standards will crucially influence RL adoption in finance. These findings add evidence that RL is valuable for financial decisions when correctly implemented, but success demands attention to implementation quality, regulatory compliance, and domain-specific factors.

## References

* Agudelo Aguirre and Agudelo Aguirre, (2024)

  Agudelo Aguirre, R. A. and Agudelo Aguirre, A. A. (2024).
  Behavioral finance: Evolution from the classical theory and remarks.
  Journal of Economic Surveys, 38(2):452–475.
* Aldridge, (2013)

  Aldridge, I. (2013).
  High-frequency trading: a practical guide to algorithmic strategies and trading systems, volume 604.
  John Wiley & Sons.
* Almahdi and Yang, (2017)

  Almahdi, S. and Yang, S. Y. (2017).
  An adaptive portfolio trading system: A risk-return portfolio optimization using recurrent reinforcement learning with expected maximum drawdown.
  Expert Systems with Applications, 87:267–279.
* Almgren, (2003)

  Almgren, R. (2003).
  Optimal execution with nonlinear impact functions and trading-enhanced risk.
  Applied Mathematical Finance, 10(1):1–18.
* Almgren and Chriss, (2001)

  Almgren, R. and Chriss, N. (2001).
  Optimal execution of portfolio transactions.
  Journal of Risk, 3:5–40.
* Bagnara, (2022)

  Bagnara, M. (2022).
  Asset pricing and machine learning: A critical review.
  Journal of Economic Surveys, 38(1):27–56.
* Bailey et al., (2014)

  Bailey, D. H., Borwein, J. M., Lopez de Prado, M., and Zhu, Q. J. (2014).
  The probability of backtest overfitting.
  Journal of Computational Finance, 20(4):39–69.
* Ben-David et al., (2010)

  Ben-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., and Vaughan, J. W. (2010).
  A theory of learning from different domains, volume 79.
  Springer.
* Benhamou et al., (2021)

  Benhamou, E., Saltiel, D., Ungari, S., and Mukhopadhyay, A. (2021).
  Bridging the gap between markowitz planning and deep reinforcement learning.
  Applied Sciences, 11(1):236.
* Bertsimas and Lo, (1998)

  Bertsimas, D. and Lo, A. W. (1998).
  Optimal control of execution costs.
  Journal of Financial Markets, 1(1):1–50.
* Brown et al., (1992)

  Brown, S. J., Goetzmann, W. N., Ibbotson, R. G., and Ross, S. A. (1992).
  Survivorship bias in performance studies.
  The Review of Financial Studies, 5(4):553–580.
* Buehler et al., (2019)

  Buehler, H., Gonon, L., Teichmann, J., and Wood, B. (2019).
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291.
* (13)

  Carapuço, J., Neves, R., and Horta, N. (2018a).
  Reinforcement learning applied to forex trading.
  Applied Soft Computing, 73:783–794.
* (14)

  Carapuço, J., Neves, R., and Horta, N. (2018b).
  Reinforcement learning applied to forex trading.
  Applied Soft Computing, 73:783–794.
* Cartea et al., (2015)

  Cartea, Á., Jaimungal, S., and Peña, J. (2015).
  Algorithmic and high-frequency trading.
  Cambridge University Press.
* Charpentier et al., (2021)

  Charpentier, A., Elie, R., and Remlinger, C. (2021).
  Reinforcement learning in economics and finance.
  Computational Economics, 58(2):329–360.
* Chen et al., (2021)

  Chen, L., Gao, Q., and Li, D. (2021).
  Multi-agent deep reinforcement learning for portfolio management.
  IEEE Access, 9:30394–30405.
* Chinco et al., (2019)

  Chinco, A., Neuhierl, A., and Weber, M. (2019).
  A sparse model of demand for news: Evidence from the options market.
  The Journal of Finance, 74(6):2829–2875.
* Cont, (2001)

  Cont, R. (2001).
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative finance, 1(2):223–236.
* Cont et al., (2010)

  Cont, R., Moussa, A., and Santos, E. B. (2010).
  Network structure and systemic risk in banking systems.
  Available at SSRN 1733528.
* Doshi-Velez and Kim, (2017)

  Doshi-Velez, F. and Kim, B. (2017).
  Towards a rigorous science of interpretable machine learning.
  arXiv preprint arXiv:1702.08608.
* Dulac-Arnold et al., (2019)

  Dulac-Arnold, G., Mankowitz, D., and Hester, T. (2019).
  Challenges of real-world reinforcement learning.
  arXiv preprint arXiv:1904.12901.
* Fabozzi et al., (2010)

  Fabozzi, F. J., Focardi, S. M., and Kolm, P. N. (2010).
  Quantitative equity investing: techniques and strategies, volume 453.
  John Wiley & Sons.
* Farmer and Skouras, (2013)

  Farmer, J. D. and Skouras, S. (2013).
  A review of the past and future of electronic trading and its impact on market structure.
  Journal of Economic Dynamics and Control, 37(4):738–756.
* Feng et al., (2019)

  Feng, F., He, X., Wang, X., Luo, C., Liu, Y., and Chua, T.-S. (2019).
  Temporal relational ranking for stock prediction.
  ACM Transactions on Information Systems (TOIS), 37(2):1–30.
* Fischer and Krauss, (2018)

  Fischer, T. and Krauss, C. (2018).
  Deep learning with long short-term memory networks for financial market predictions.
  European Journal of Operational Research, 270(2):654–669.
* García and Fernández, (2015)

  García, J. and Fernández, F. (2015).
  A comprehensive survey on safe reinforcement learning.
  Journal of Machine Learning Research, 16(1):1437–1480.
* (28)

  Gomber, P., Arndt, B., Lutat, M., and Uhle, T. (2017a).
  High-frequency trading.
  Business & Information Systems Engineering, 59(6):381–383.
* (29)

  Gomber, P., Koch, J.-A., and Siering, M. (2017b).
  Digital finance and fintech: current research and future research directions.
  Journal of Business Economics, 87(5):537–580.
* Goodfellow et al., (2016)

  Goodfellow, I., Bengio, Y., and Courville, A. (2016).
  Deep Learning.
  MIT Press, Cambridge, MA.
* Gould et al., (2013)

  Gould, M. D., Porter, M. A., Williams, S., McDonald, M., Fenn, D. J., and Howison, S. D. (2013).
  Limit order books.
  Quantitative Finance, 13(11):1709–1742.
* Halperin, (2020)

  Halperin, I. (2020).
  Qlbs: Q-learner in the black-scholes (-merton) worlds.
  The Journal of Derivatives, 28(1):99–122.
* (33)

  Hambly, B., Xu, R., and Yang, H. (2023a).
  Recent advances in reinforcement learning in finance.
  Mathematical Finance, 33(3):437–503.
* (34)

  Hambly, B., Xu, R., and Yang, H. (2023b).
  Recent advances in reinforcement learning in finance.
  Mathematical Finance, 33(3):437–503.
* Harvey et al., (2016)

  Harvey, C. R., Liu, Y., and Zhu, H. (2016).
  … and the cross-section of expected returns.
  The Review of Financial Studies, 29(1):5–68.
* Hasbrouck, (2007)

  Hasbrouck, J. (2007).
  Empirical market microstructure: The institutions, economics, and econometrics of securities trading.
  Oxford University Press.
* Heaton et al., (2017)

  Heaton, J., Polson, N., and Witte, J. H. (2017).
  Deep learning for finance: deep portfolios.
  Applied Stochastic Models in Business and Industry, 33(1):3–12.
* Jiang et al., (2017)

  Jiang, Z., Xu, D., and Liang, J. (2017).
  A deep reinforcement learning framework for the financial portfolio management problem.
  arXiv preprint arXiv:1706.10059.
* Jorion, (2007)

  Jorion, P. (2007).
  Value at risk: the new benchmark for managing financial risk.
  McGraw-Hill.
* Kolm and Rémi, (2019)

  Kolm, P. N. and Rémi, G. (2019).
  Modern perspectives on reinforcement learning in finance.
  The Journal of Machine Learning in Finance, 1(1):1–22.
* Lei et al., (2020)

  Lei, K., Zhang, B., Li, Y., Yang, M., and Shen, Y. (2020).
  Time-driven feature-aware jointly deep reinforcement learning for financial signal representation and algorithmic trading.
  Expert Systems with Applications, 140:112872.
* (42)

  Li, Y., Zheng, W., and Zheng, Z. (2019a).
  Deep robust reinforcement learning for practical algorithmic trading.
  IEEE Access, 7:108014–108022.
* (43)

  Li, Y., Zheng, W., and Zheng, Z. (2019b).
  Deep robust reinforcement learning for practical algorithmic trading.
  IEEE Access, 7:108014–108022.
* Liang et al., (2018)

  Liang, Z., Chen, H., Zhu, J., Jiang, K., and Li, Y. (2018).
  Towards automated trading based on reinforcement learning.
  Neurocomputing, 284:168–181.
* Lim and Brooks, (2011)

  Lim, K.-P. and Brooks, R. (2011).
  The evolution of stock market efficiency over time: A survey of the empirical literature.
  Journal of Economic Surveys, 25(1):69–108.
* Liu et al., (2020)

  Liu, Y., Liu, Q., Zhao, H., Pan, Z., and Liu, C. (2020).
  Adaptive quantitative trading: An imitative deep reinforcement learning approach.
  In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages 2128–2135.
* Lopez de Prado, (2018)

  Lopez de Prado, M. (2018).
  Advances in financial machine learning.
  John Wiley & Sons.
* (48)

  Lussange, J., Belianin, S., Bourgeois-Gironde, S., and Gutkin, B. (2021a).
  Modelling stock markets by multi-agent reinforcement learning.
  Computational Economics, 57(1):113–147.
* (49)

  Lussange, J., Belianin, S., Bourgeois-Gironde, S., and Gutkin, B. (2021b).
  Modelling stock markets by multi-agent reinforcement learning.
  Computational Economics, 57(1):113–147.
* Markowitz, (1952)

  Markowitz, H. (1952).
  Portfolio selection.
  The Journal of Finance, 7(1):77–91.
* McNeil et al., (2015)

  McNeil, A. J., Frey, R., and Embrechts, P. (2015).
  Quantitative risk management: concepts, techniques and tools-revised edition.
  Princeton university press.
* Mitchell, (1997)

  Mitchell, T. M. (1997).
  Machine Learning.
  McGraw-Hill, New York.
* Mnih et al., (2016)

  Mnih, V., Badia, A. P., Mirza, M., Graves, A., Lillicrap, T., Harley, T., Silver, D., and Kavukcuoglu, K. (2016).
  Asynchronous methods for deep reinforcement learning.
  In International Conference on Machine Learning, pages 1928–1937.
* Mohri et al., (2018)

  Mohri, M., Rostamizadeh, A., and Talwalkar, A. (2018).
  Foundations of Machine Learning.
  MIT Press, Cambridge, MA, 2nd edition.
* Moody and Saffell, (2001)

  Moody, J. and Saffell, M. (2001).
  Learning to trade via direct reinforcement.
  IEEE transactions on neural Networks, 12(4):875–889.
* Perold, (1988)

  Perold, A. F. (1988).
  The implementation shortfall: Paper versus reality.
  The Journal of Portfolio Management, 14(3):4–9.
* Puiutta and Veith, (2020)

  Puiutta, E. and Veith, E. M. (2020).
  Explainable reinforcement learning: a survey.
  International Cross-Domain Conference for Machine Learning and Knowledge Extraction, pages 77–95.
* Qin et al., (2021)

  Qin, Z., Zhou, Y., Huang, Y., Xu, K., and Yen, D. C. (2021).
  Cefi vs. defi–comparing centralized to decentralized finance.
  arXiv preprint arXiv:2106.08157.
* Ritter, (2017)

  Ritter, G. (2017).
  Machine learning for trading.
  Available at SSRN 3015609.
* (60)

  Roncalli, T. (2020a).
  Handbook of financial risk management.
  Chapman and Hall/CRC.
* (61)

  Roncalli, T. (2020b).
  Machine learning for risk management.
  Available at SSRN 3435038.
* Sezer et al., (2020)

  Sezer, O. B., Gudelek, M. U., and Ozbayoglu, A. M. (2020).
  Financial time series forecasting with deep learning: A systematic literature review: 2005–2019.
  Applied Soft Computing, 90:106181.
* Shi, (2025)

  Shi, C. (2025).
  From econometrics to machine learning: Transforming empirical asset pricing.
  Journal of Economic Surveys.
* Spooner et al., (2018)

  Spooner, T., Fearnley, J., Savani, R., and Koukorinis, A. (2018).
  Market making via reinforcement learning.
  Proceedings of the 17th International Conference on Autonomous Agents and MultiAgent Systems, pages 434–442.
* Sutton and Barto, (2018)

  Sutton, R. S. and Barto, A. G. (2018).
  Reinforcement Learning: An Introduction.
  MIT Press, Cambridge, MA, 2nd edition.
* Taleb, (2007)

  Taleb, N. N. (2007).
  The black swan: The impact of the highly improbable, volume 2.
  Random house.
* Théate and Ernst, (2021)

  Théate, T. and Ernst, D. (2021).
  An application of deep reinforcement learning to algorithmic trading.
  Expert Systems with Applications, 173:114632.
* (68)

  Tsantekidis, A., Passalis, N., Tefas, A., Kanniainen, J., Gabbouj, M., and Iosifidis, A. (2017a).
  Forecasting stock prices from the limit order book using convolutional neural networks.
  2017 IEEE 19th conference on business informatics (CBI), 1:7–12.
* (69)

  Tsantekidis, A., Passalis, N., Tefas, A., Kanniainen, J., Gabbouj, M., and Iosifidis, A. (2017b).
  Using deep learning to detect price change indications in financial markets.
  In 2017 25th European Signal Processing Conference (EUSIPCO), pages 2511–2515. IEEE.
* Tsay, (2005)

  Tsay, R. S. (2005).
  Analysis of financial time series, volume 543.
  John wiley & sons.
* Wang et al., (2021)

  Wang, H., Yu, H., and Liu, J. (2021).
  Deep reinforcement learning for multi-period portfolio optimization.
  Expert Systems with Applications, 164:113842.
* Wang et al., (2016)

  Wang, J. X., Kurth-Nelson, Z., Tirumala, D., Soyer, H., Leibo, J. Z., Munos, R., Blundell, C., Kumaran, D., and Botvinick, M. (2016).
  Learning to reinforcement learn.
  arXiv preprint arXiv:1611.05763.
* Wu et al., (2020)

  Wu, N., Green, B., Ben, X., and O’Banion, S. (2020).
  Deep transformer models for time series forecasting: The influenza prevalence case.
  arXiv preprint arXiv:2001.08317.
* Yoon et al., (2019)

  Yoon, J., Jarrett, D., and Van der Schaar, M. (2019).
  Time-series generative adversarial networks.
  In Advances in Neural Information Processing Systems, volume 32, pages 5508–5518.
* Yuan et al., (2020)

  Yuan, Y., Wang, F.-Y., Zhai, J., and Cao, Z. (2020).
  A multi-agent and machine learning based online adaptive energy management system for plug-in hybrid electric vehicles.
  Transportation Research Part C: Emerging Technologies, 121:102855.
* Zhang et al., (2017)

  Zhang, L., Aggarwal, C., and Qi, G.-J. (2017).
  Stock price prediction via discovering multi-frequency trading patterns.
  In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pages 2141–2149.
* Zhang et al., (2020)

  Zhang, Z., Zohren, S., and Roberts, S. (2020).
  Deep learning for portfolio optimization.
  The Journal of Financial Data Science, 2(4):8–20.