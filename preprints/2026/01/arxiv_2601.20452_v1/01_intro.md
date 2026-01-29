---
authors:
- Bridget Smart
- Ebba Mark
- Anne Bastian
- Josefina Waugh
doc_id: arxiv:2601.20452v1
family_id: arxiv:2601.20452
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Manipulation in Prediction Markets: An Agent-based Modeling Experiment'
url_abs: http://arxiv.org/abs/2601.20452v1
url_html: https://arxiv.org/html/2601.20452v1
venue: arXiv q-fin
version: 1
year: 2026
---


Bridget Smart
Institute for New Economic Thinking, University of Oxford, Manor Road, OX1 3UQ, Oxford, United Kingdom
Mathematical Institute, University of Oxford, Woodstock Road, OX2 6GG, Oxford, United Kingdom


Ebba Mark
Institute for New Economic Thinking, University of Oxford, Manor Road, OX1 3UQ, Oxford, United Kingdom


Anne Bastian
Institute for Globally Distributed Open Research and Education (IGDORE), Gothenburg, Sweden

Josefina Waugh
Economics Institute, Pontifical Catholic University of Chile, Avenida Libertador Bernardo O’Higgins 340, Santiago, Chile

###### Abstract

Prediction markets mobilize financial incentives to forecast binary event outcomes through the aggregation of dispersed beliefs and heterogeneous information. Their growing popularity and demonstrated predictive accuracy in political elections have raised speculation and concern regarding their susceptibility to manipulation and the potential consequences for democratic processes. Using agent-based simulations combined with an analytic characterization of price dynamics, we study how high-budget agents can introduce price distortions in prediction markets. We explore the persistence and stability of these distortions in the presence of herding or stubborn agents, and analyze how agent expertise affects market-price variance. Firstly we propose an agent-based model of a prediction market in which bettors with heterogeneous expertise, noisy private information, variable learning rates and budgets observe the evolution of public opinion on a binary election outcome to inform their betting strategies in the market. The model exhibits stability across a broad parameter space, with complex agent behaviors and price interactions producing self-regulatory price discovery. Second, using this simulation framework, we investigate the conditions under which a highly resourced minority, or “whale” agent, with a biased valuation can distort the market price, and for how long. We find that biased whales can temporarily shift prices, with the magnitude and duration of distortion increasing when non-whale bettors exhibit herding behavior and slow learning. Our theoretical analysis corroborates these results, showing that whales can shift prices proportionally to their share of market capital, with distortion duration depending on non-whale learning rates and herding intensity.

Keywords: prediction markets, agent-based model, betting markets, market manipulation

11footnotetext: Corresponding authors:
Bridget Smart, bridget.smart@maths.ox.ac.uk, and
Ebba Mark, ebba.mark@magd.ox.ac.uk.

## 1. Introduction

Prediction markets, where participants wager on binary outcomes, have been proposed as effective mechanisms for aggregating dispersed beliefs into accurate predictors in environments characterized by uncertainty and heterogeneous access to information [[44](https://arxiv.org/html/2601.20452v1#bib.bib45 "Political Prediction and the Wisdom of Crowds"), [2](https://arxiv.org/html/2601.20452v1#bib.bib4 "Beauty Contests and Iterated Expectations in Asset Markets")]. Their appeal rests on the idea that traders, motivated by financial incentives, reveal private information through their willingness to buy or sell contracts corresponding to a particular outcome.

Prediction market prices have been found to closely approximate the mean belief about an event’s probability in theoretical settings with well-informed, constrained and risk-adverse traders [[57](https://arxiv.org/html/2601.20452v1#bib.bib55 "Interpreting Prediction Market Prices as Probabilities"), [21](https://arxiv.org/html/2601.20452v1#bib.bib23 "Risk aversion, beliefs, and prediction market equilibrium")]. In several real elections, prediction-market forecasts have matched or outperformed traditional polling or expert judgment [[42](https://arxiv.org/html/2601.20452v1#bib.bib41 "Forecasting Elections: Comparing Prediction Markets, Polls, and Their Biases"), [5](https://arxiv.org/html/2601.20452v1#bib.bib7 "Prediction Market Accuracy in the Long Run"), [55](https://arxiv.org/html/2601.20452v1#bib.bib53 "The Polymarket Effect: How Prediction Markets Are Beating The Experts"), [12](https://arxiv.org/html/2601.20452v1#bib.bib14 "Are betting markets better than polling in predicting political elections?")], although evidence is mixed [[28](https://arxiv.org/html/2601.20452v1#bib.bib30 "Competing Approaches to Forecasting Elections: Economic Models, Opinion Polling and Prediction Markets"), [15](https://arxiv.org/html/2601.20452v1#bib.bib17 "Markets vs. polls as election predictors: An historical assessment")]. Positive examples are sometimes attributed to the “wisdom of crowds”, which relies on assumptions of independence, diversity, and the absence of dominant participants, conditions which are not always satisfied in practice [[48](https://arxiv.org/html/2601.20452v1#bib.bib49 "The wisdom of crowds: why the many are smarter than the few and how collective wisdom shapes business, economies, societies, and nations")].

Much of the empirical evidence supporting prediction-market accuracy comes from markets with strict limits on individual trading positions. Early studies of prediction market accuracy and dynamics largely relied on platforms with strict per-trader position limits, such as the Iowa Electronic Markets [[5](https://arxiv.org/html/2601.20452v1#bib.bib7 "Prediction Market Accuracy in the Long Run")] and PredictIt [[39](https://arxiv.org/html/2601.20452v1#bib.bib40 "Opinion Dynamics Explain Price Formation in Prediction Markets")], where individual exposure was constrained to a few thousand U.S. dollars per market (e.g., $3,500 on PredictIt as of 2025 [[51](https://arxiv.org/html/2601.20452v1#bib.bib29 "CFTC Letter 25-20: Amendment to CFTC Letter No. 14-130 (Victoria University / PredictIt)")]). These caps strictly limited any single participant’s ability to meaningfully influence prices.

In contrast, newer platforms permit substantially larger, contract-specific position limits for eligible participants, in some cases reaching the multi-million-dollar range. Under these conditions, the classic assumption that individual traders are too small to affect prices, and that any attempted manipulation is rapidly arbitraged away [[23](https://arxiv.org/html/2601.20452v1#bib.bib24 "Combinatorial information market design")], is no longer guaranteed to hold. Both theoretical and empirical work shows that when traders are sufficiently capitalized or face strong incentives, prediction markets may sustain non-informational price deviations for meaningful periods [[11](https://arxiv.org/html/2601.20452v1#bib.bib13 "Can Asset Markets Be Manipulated? A Field Experiment With Racetrack Betting"), [2](https://arxiv.org/html/2601.20452v1#bib.bib4 "Beauty Contests and Iterated Expectations in Asset Markets")].

This institutional shift has coincided with a rapid expansion in prediction market activity. During the 2024 U.S. presidential election, market capitalization reached hundreds of millions of USD [[26](https://arxiv.org/html/2601.20452v1#bib.bib2 "Kalshi Data and Analytics"), [36](https://arxiv.org/html/2601.20452v1#bib.bib1 "Explore the Highest Volume Popular Polymarkets")]. For example, weeks prior to the 2024 U.S. presidential election between Donald Trump and Kamala Harris, a consequential ruling by the Commodity Futures Trading Commission legalized KalshiEx [[52](https://arxiv.org/html/2601.20452v1#bib.bib50 "KalshiEX LLC v. CFTC. 24-5205")]. Within days, the platform announced its ability to accommodate individual trades of up to $100 million [[20](https://arxiv.org/html/2601.20452v1#bib.bib22 "Americans Bet $100 Million on Trump v. Harris, but at What Cost?"), [29](https://arxiv.org/html/2601.20452v1#bib.bib31 "It’s Official: You Can Now Trade on the U.S. Presidential Election")], with notional volume exceeding $20 billion in December 2025 [[26](https://arxiv.org/html/2601.20452v1#bib.bib2 "Kalshi Data and Analytics")], marking a departure from smaller, tightly-capped markets.

In this context, a type of market distorter commonly referred to as a “whale”111“Whales” refer to participants in a betting market who control and deploy a volume of capital significantly larger than the average participant, thereby potentially possessing the ability to temporarily influence market prices through their trades or wagers. has been identified across multiple platforms in recent years [[38](https://arxiv.org/html/2601.20452v1#bib.bib39 "A French whale has bet $45 million on a Trump win so far. Who is this?"), [18](https://arxiv.org/html/2601.20452v1#bib.bib20 "What to know about the potential $30 million whale moving betting markets toward trump")]. For example, in 2024, Polymarket identified a $45 million bet placed by a French national to favor Donald Trump, temporarily pushing up his odds in the prediction market [[38](https://arxiv.org/html/2601.20452v1#bib.bib39 "A French whale has bet $45 million on a Trump win so far. Who is this?"), [46](https://arxiv.org/html/2601.20452v1#bib.bib47 "The French Connection to Online Bets on Trump")]. At such levels of capital concentration, salient price movements may interact with heterogeneity in how traders weight prior beliefs, market-external information, and market prices, generating dynamics that differ qualitatively from those observed in smaller, tightly capped markets.

The potential for such market manipulation invites a suite of questions regarding the potential feedback between prediction markets and real-world political outcomes. Their credibility as predictive tools could earn them a higher rank in the information landscape available to voters when shaping their voting decisions. Research on informational cascades and bandwagon effects suggests that shifts in public beliefs triggered by prominent information signals like polls can influence real political outcomes, making endogeneity between market prices and behavior difficult to rule out [[31](https://arxiv.org/html/2601.20452v1#bib.bib33 "What motivates bandwagon voting behavior: Altruism or a desire to win?"), [32](https://arxiv.org/html/2601.20452v1#bib.bib34 "Do Polls Reflect Opinions or Do Opinions Reflect Polls? The Impact of Political Polling on Voters’ Expectations, Preferences, and Behavior"), [8](https://arxiv.org/html/2601.20452v1#bib.bib10 "Can biased polls distort electoral results? Evidence from the lab"), [1](https://arxiv.org/html/2601.20452v1#bib.bib3 "National Polls, Local Preferences and Voters’ Behaviour: Evidence from the UK General Elections"), [40](https://arxiv.org/html/2601.20452v1#bib.bib43 "Are public opinion polls self-fulfilling prophecies?")]. Anecdotal and journalistic evidence indicates that members of the public have begun to rely on prediction market values in addition to polls to form their understanding of public opinion [[16](https://arxiv.org/html/2601.20452v1#bib.bib18 "US election betting online: ‘some consider the data to be real-time polls’"), [20](https://arxiv.org/html/2601.20452v1#bib.bib22 "Americans Bet $100 Million on Trump v. Harris, but at What Cost?")]. Thus, a potential feedback between market price and electorate beliefs raises a logical concern about incentives for strategic manipulation of market price to potentially distort democratic processes.

This motivates our central question: Under what conditions do contemporary prediction markets function as self-correcting information processing mechanisms, and when can they instead temporarily sustain price deviations introduced by a highly resourced, biased minority?

We address this by examining the prediction market as an information-aggregating mechanism and how trader behavior can introduce volatility and error into the market. In particular, we consider how large trades can lead to sustained or fluctuating price movements through a biased large trader (whale) operating among traders who partially herd toward the market price.

### 1.1.  Methodological Approach and Contributions

In this study, we develop an open source Agent-Based Model (ABM) which simulates a prediction market in which betting agents, characterized by heterogeneous learning functions, expertise, biased perceptions, and budgets, bet on the outcome of a binary election. We use this model to consider how wealth distribution, risk aversion, herding and belief dynamics influence prediction market price. Our proposed agent-based model framework exhibits stable performance and accurately predicts the data-informed stylized election outcome across a wide range of parameter values. Furthermore, a decision rule wherein bettors aim to maximize risk-adjusted returns produces reasonable outcomes in terms of prediction market price accuracy (in relation to leading election forecasting models) and where profits accrue to those bettors with more accurate insight into the electoral outcome.

Next, using this model we investigate the relative profit gain between experts and non-experts, the potential for market price manipulation by high-capital investors, and whether the stability of the market depends on the incorporation of herding behavior. We evaluate the performance of this prediction market, defined as the deviation of the market price from public voting preferences, using a regression model to test for lagged correlation dynamics. We demonstrate that, over a particular population size, initial capital allocation, and wide range of parameter values, the market quickly adjusts to counteract the price pressure of whale bettors. However, whale bettors are able to temporarily shift and introduce volatility into the market price, where the magnitude and duration of this shift is proportional to the product of their budget allocation and misvaluation. The introduced error can be amplified in the presence of herding or stubborn behavior from other bettors.

Alongside insights from our ABM, we conduct a theoretical analysis of agent valuation, utility, and market-update functions to examine how the prediction market responds to the presence of whales and herding agents. This analysis reinforces our simulation results, showing that prolonged whale-induced price distortions scale with the whale’s share of total market capital. The decay of these distortions depends on the learning dynamics and herding propensity of other agents. We also demonstrate that market distortions may decay slowly or oscillate in a market with slow belief updates or herding toward the market price.

Beyond this investigation of prediction markets as information aggregators, we contribute analytical tools for future research by making our ABM model open source, available on [GitHub](https://github.com/ebbam/power_prediction/)222<https://github.com/ebbam/power_prediction/>. Additionally, we build a Dash application providing a graphical user interface to the ABM, allowing users to change parameters for agent behavior and investigate the impact of correlations within the model through a graphical user interface. The modular ABM provides considerable flexibility for extensions that could accommodate alternative behavioral rules, parameter variation, exploration of the role of information shocks, and more detailed models of an election process in which the network of an electorate impacts the evolution of voting preferences.

Overall, this work has implications for the regulation and design of prediction markets at a time when their legal contexts are evolving. Our findings motivate consideration of measures that limit potential impacts of concentrated capital, particularly in election prediction market settings where prices may function as public information signals, including restrictions on individual trade sizes or overall budget limits where enforceable. While feedback effects between prediction markets and democratic processes remain empirically unresolved, our results add weight to a precautionary approach. Beyond market design, our findings highlight risks associated with the public framing of election betting market prices as probability forecasts, especially when such prices may be influenced by concentrated capital and subsequently amplified by media coverage or interpreted by voters, campaigns, or other downstream audiences.

### 1.2.  Related Literature

Existing research on prediction markets spans theoretical, experimental, and simulation-based approaches. A substantial body of work examines prediction markets as forecasting tools, drawing on their modern institutional advantages [[58](https://arxiv.org/html/2601.20452v1#bib.bib56 "Using prediction markets to enhance US intelligence capabilities"), [35](https://arxiv.org/html/2601.20452v1#bib.bib37 "Use of Prediction Markets to Forecast Infectious Disease Activity"), [44](https://arxiv.org/html/2601.20452v1#bib.bib45 "Political Prediction and the Wisdom of Crowds"), [42](https://arxiv.org/html/2601.20452v1#bib.bib41 "Forecasting Elections: Comparing Prediction Markets, Polls, and Their Biases"), [47](https://arxiv.org/html/2601.20452v1#bib.bib48 "Sports Forecasting: A Comparison of the Forecast Accuracy of Prediction Markets, Betting Odds and Tipsters")], theoretical motivations such as the efficient market hypothesis [[54](https://arxiv.org/html/2601.20452v1#bib.bib52 "Prediction markets: Theory, evidence and applications"), [5](https://arxiv.org/html/2601.20452v1#bib.bib7 "Prediction Market Accuracy in the Long Run")], empirical evidence of forecasting accuracy [[17](https://arxiv.org/html/2601.20452v1#bib.bib19 "Anatomy of an Experimental Political Stock Market"), [5](https://arxiv.org/html/2601.20452v1#bib.bib7 "Prediction Market Accuracy in the Long Run")], and social-sensing perspectives [[19](https://arxiv.org/html/2601.20452v1#bib.bib21 "Human social sensing is an untapped resource for computational social science")], even as some foundational assumptions have been challenged [[13](https://arxiv.org/html/2601.20452v1#bib.bib15 "Are markets more accurate than polls? The surprising informational value of “just asking”"), [28](https://arxiv.org/html/2601.20452v1#bib.bib30 "Competing Approaches to Forecasting Elections: Economic Models, Opinion Polling and Prediction Markets")]. Experimental studies have probed these mechanisms in controlled settings, examining how institutional design and participant incentives shape price formation [[53](https://arxiv.org/html/2601.20452v1#bib.bib51 "Prediction Markets as institutional forecasting support systems"), [37](https://arxiv.org/html/2601.20452v1#bib.bib38 "A twitter-based prediction market: social network approach")]. Notably, [[22](https://arxiv.org/html/2601.20452v1#bib.bib25 "Information aggregation and manipulation in an experimental market")] showed that small-scale markets can be resistant to manipulation, while [[9](https://arxiv.org/html/2601.20452v1#bib.bib11 "Risk aversion in prediction markets: A framed-field experiment")] linked price dynamics to participants’ risk aversion.

A growing literature employs agent-based or computational models to explore prediction-market dynamics beyond what analytical or experimental methods permit. [[27](https://arxiv.org/html/2601.20452v1#bib.bib27 "Comparing Prediction Market Mechanisms Using An Experiment-Based Multi-Agent Simulation")] Use a multi-agent simulation to evaluate alternative market mechanisms, and [[41](https://arxiv.org/html/2601.20452v1#bib.bib42 "Trading strategies and market microstructure: evidence from a prediction market")] couple empirical data with a single stylized trader to study how individual trading strategies influence performance. Other work embeds prediction-market behavior within social or informational networks, examining how opinion dynamics [[39](https://arxiv.org/html/2601.20452v1#bib.bib40 "Opinion Dynamics Explain Price Formation in Prediction Markets")], social-media-derived signals [[7](https://arxiv.org/html/2601.20452v1#bib.bib9 "Using Social Media to Predict Future Events with Agent-Based Markets")], or simulated electorates [[59](https://arxiv.org/html/2601.20452v1#bib.bib57 "Agent-Based Modeling of the Prediction Markets for Political Elections")] shape prices. [[45](https://arxiv.org/html/2601.20452v1#bib.bib46 "The role of whale investors in the bitcoin market")] develop an agent-based model to study how herding behavior and social network structure interact with agent heterogeneity to generate price volatility in Bitcoin markets.

Unlike prior work, our simulation-based and analytic approach models a prediction market with a well-defined true price and an exogenous noisy information signal. We explicitly incorporate heterogeneous expertise, behavioral learning rates, and budget dispersion, enabling systematic analysis of how behavioral and financial asymmetries affect price stability. By decoupling social-network effects, we can directly characterize how behavioral heterogeneity, noisy information, and concentrated wealth interact to induce persistent distortions and affect market stability.

## 2. Agent-based Model

We introduce an open-source agent-based model (ABM) simulating a prediction market in which NN agents, indexed i=0,1,…​Ni=0,1,\dots N, trade contracts placing bets on the outcome of a binary election over TT discrete time periods indexed t=0,1,…​Tt=0,1,\dots T. The model for the betting agent’s behavior is inspired by [[43](https://arxiv.org/html/2601.20452v1#bib.bib44 "Evaluating Prediction Mechanisms: A Profitability Test")]. In this section, we outline the market structure, agents, and actions taken on the market. Simulation [1](https://arxiv.org/html/2601.20452v1#alg1 "Simulation 1 ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") outlines the full simulation process in pseudo-code.

Simulation 1  Simulation procedure for the agent-based price-first prediction market

1:Input: betting agents 𝒜\mathcal{A}, election time TT, initial market price m0m\_{0}, outcome uncertainty ση2\sigma^{2}\_{\eta}

2:Output: market price trajectory mm, agent budgets BB, portfolios CC, valuations VV, and profit histories

3:Initialize t←0t\leftarrow 0

4:Initialize η0=m0\eta\_{0}=m\_{0}

5:while t<Tt<T do

6:  θt←[]\theta\_{t}\leftarrow[] ⊳\triangleright Generate empty order book

7:  for each betting agent a∈𝒜a\in\mathcal{A} do

8:   Receive private signal Ma,tM\_{a,t} ⊳\triangleright Agent receives fuzzy observation of outcome ([Equation 4](https://arxiv.org/html/2601.20452v1#S2.E4 "4 ‣ Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"))

9:   Propose order volume xa,tx\_{a,t} according to [Equation 6](https://arxiv.org/html/2601.20452v1#S2.E6 "6 ‣ Utility Function & Order Placement ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")

10:   if xa,t≠0x\_{a,t}\neq 0 then

11:     Append order xa,tx\_{a,t} to order book θt\theta\_{t}

12:   end if

13:  end for

14:  Arrange order book in random order

15:  Select matched orders, partially filling orders where necessary

16:  Execute matched orders θ⋆\theta^{\star} ⊳\triangleright Execute matched trades by transferring contracts and cash

17:  Calculate net demand DtD\_{t} normalized by total order volume

18:  Update market price mt←mt+1m\_{t}\leftarrow m\_{t+1} as in [Equation 2](https://arxiv.org/html/2601.20452v1#S2.E2 "2 ‣ 2.2. Market ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")

19:  for each agent a∈𝒜a\in\mathcal{A} do

20:   Update wealth and holdings (Ba,t+1,Ca,t+1)(B\_{a,t+1},C\_{a,t+1})

21:   Update market valuations Va,t+1V\_{a,t+1} ⊳\triangleright [Equation 3](https://arxiv.org/html/2601.20452v1#S2.E3 "3 ‣ Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")

22:  end for

23:  t←t+1t\leftarrow t+1

24:  ηt←ηt+1\eta\_{t}\leftarrow\eta\_{t+1} ⊳\triangleright Update true election outcome [Equation 1](https://arxiv.org/html/2601.20452v1#S2.E1 "1 ‣ 2.1. Election ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")

25:end while

### 2.1.  Election

At each time step tt, agents bet on the outcome of a binary election outcome ηt\eta\_{t}. We represent the true election outcome ηt\eta\_{t} as a random walk:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt=ηt−1+ϵη,ϵη∼𝒩​(0,ση2)\eta\_{t}=\eta\_{t-1}+\epsilon\_{\eta},\quad\epsilon\_{\eta}\sim\mathcal{N}(0,\sigma^{2}\_{\eta}) |  | (1) |

where ηt\eta\_{t} is bounded by [0,1]. ηt\eta\_{t} is a reflection of public opinion at time tt with no knowledge of future movements.

### 2.2.  Market

At each time step, betting agents submit buy or sell orders of a fixed size based at the current market price mtm\_{t}. A central market fulfills these buy and sell orders via random order matching. The market has a bid-ask spread of zero, with a single price acting as both the buy and sell price. Orders are matched using double auction rules. Bettors update their budget and portfolio given orders filled.

The market is responsive to net demand in the order book, setting the next time period’s market price mt+1m\_{t+1} according to [Equation 2](https://arxiv.org/html/2601.20452v1#S2.E2 "2 ‣ 2.2. Market ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | mt+1=mt+λ​DtKt,m\_{t+1}\;=\;m\_{t}\;+\;\lambda\;\dfrac{D\_{t}}{K\_{t}}, |  | (2) |

where DtD\_{t} denotes the net demand, KtK\_{t} the total order volume, and scaling parameter λ\lambda, controlling the maximum step size of a single-tt price update. The market price is constrained to lie within [0,1][0,1] as in real-world prediction markets.

Table 1: Inventory of Bettor Characteristics and Behaviors

|  |  |  |  |
| --- | --- | --- | --- |
| Characteristics | Symbol | Definition | Initial Value |
| Resources |  |  |  |
| Budget | Bi,tB\_{i,t} | Betting agent’s budget at time tt | Bi,0∼U​(100,1000)B\_{i,0}\sim U(100,1000) |
| Market valuation | Vi,tV\_{i,t} | Bettor’s belief about the market value of a particular contract between $0-1. | Vi,0∼N​(0.5,0.05)V\_{i,0}\sim N(0.5,0.05) |
| Portfolio | Ci,tC\_{i,t} | Holding position of each betting agent. A positive (negative) value of Ci,tC\_{i,t} indicates that the betting agent has purchased more (less) contracts than they have sold. | Ci,0=0C\_{i,0}=0 |
| Attributes |  |  |  |
| Stubbornness | sis\_{i} | Bettor’s resistance to updating their internal market valuation Vi,tV\_{i,t} when provided with new information. | si∼N​(0.3,0.05)s\_{i}\sim N(0.3,0.05) |
| Expertise | eie\_{i} | This parameter controls how “clearly” the betting agent can see the true election outcome at each time step. | ei∼N​(0.9,0.04)e\_{i}\sim N(0.9,0.04) |
| Bias | bib\_{i} | This parameter reflects the extent to which the bettor systematically over- or under-estimates the true election outcome. Alternatively, this bias reflects an internal belief that diverges from the true market value signal the bettor receives at each time step. | bi∼0b\_{i}\sim 0 |
| Risk aversion | rir\_{i} | Bettor’s risk preferences. | ri∼U​(0,1)r\_{i}\sim U(0,1) |

* •

  Note: Attributes are all constrained to be between 0 and 1, so clipping is performed to ensure values are valid.
* •

  1 Some of the default values for these parameters are drawn from a uniform (UU) or normal (NN) distribution, while others are constant.
* •

  2 These initial values were chosen to ensure heterogeneous yet realistic agent behavior, providing sufficient diversity in beliefs and trading strategies while maintaining market dynamics that remain consistent with the true election outcome.

### 2.3.  Agents

The betting agents are defined by the following characteristics and behaviors.

#### 2.3.1. Characteristics

First, each betting agent possesses the characteristics listed in [Table 1](https://arxiv.org/html/2601.20452v1#S2.T1 "Table 1 ‣ 2.2. Market ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"), jointly determining how they behave on the prediction market. Attributes are fixed and specified uniquely for each agent at model initialization. Resources change throughout the course of the simulation following market activity.

#### 2.3.2. Behavioral Rules

##### Internal Valuation

At each time step tt, each betting agent updates their individual valuation Vi,tV\_{i,t} of the true election outcome ηt\eta\_{t}. This can analogously be considered the betting agent’s individual belief about ηt\eta\_{t}.

The agent does not observe ηt\eta\_{t} directly. Rather, they receive a “fuzzy” signal Mi,tM\_{i,t} of the true election outcome ηt\eta\_{t} whose variance decreases with their expertise eie\_{i}. Agents with an expertise value closer to 1 will have an expected individual valuation with less variance around the market price, and as ei→0e\_{i}\to 0, the market signal becomes increasingly noisy. This is implemented using a normal distribution centered at ηt\eta\_{t} with variance 1−ei1-e\_{i}. Additionally, each betting agent has a bias bib\_{i} which they detract from signal Mi,tM\_{i,t} when updating their internal valuation. In this set-up, the bias impacts the update value consistently at each time step.

Bettors update their internal valuation of the market price as outlined in [Equation 3](https://arxiv.org/html/2601.20452v1#S2.E3 "3 ‣ Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt+1=(1−si)​(Mi,t−bi)+si​Vi,tV\_{t+1}=(1-s\_{i})(M\_{i,t}-b\_{i})+s\_{i}V\_{i,t} |  | (3) |

![Refer to caption](figures/combined_parameter_plots.png)


Figure 1: Stylized representation of behavioral attributes and their effects on betting agent behavior. Panel (A) represents the buy-sell decision of an individual agent ii at time tt with budget Bi,t=$​100B\_{i,t}=\mathdollar 100 whose internal market valuation Vi,t=$​0.50V\_{i,t}=\mathdollar 0.50. Each line represents their buy-sell decision at various market prices mtm\_{t}, varying their degree of risk aversion where ri→0r\_{i}\rightarrow 0 implies higher levels of risk aversion. Panel (B) represents a high-expertise (ei=0.9e\_{i}=0.9) betting agent’s learning process over 50 time steps. The agent starts the simulation with an internal valuation Vi,0=$​0.10V\_{i,0}=\mathdollar 0.10 receiving a signal of the true value ηt\eta\_{t} (a constant value in this stylized representation). Each line represents the learning trajectory mediated by varying stubbornness sis\_{i}. Panel (C) represents the distribution of signal Mi,tM\_{i,t} where the true value ηt=$​0.50\eta\_{t}=\mathdollar 0.50, varying expertise eie\_{i} and bias bib\_{i}. Each color represents a different level of bias bib\_{i} and each value on the x-axis represents a different level of expertise eie\_{i}. The gray sections represent the limits ([$0,$1]) of any market valuation.

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mi,t∼𝒩​(ηt, 1−ei)M\_{i,t}\sim\mathcal{N}(\eta\_{t},\;1-e\_{i}) |  | (4) |

and Vt−1V\_{t-1} is constrained between [0,1]. Conditional on Vi,tV\_{i,t} and ηt\eta\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi,t+1∣Vi,t,ηt∼𝒩(\displaystyle V\_{i,t+1}\mid V\_{i,t},\eta\_{t}\sim\mathcal{N}\!\big( | (1−si)​(ηt−bi)+si​Vi,t,\displaystyle(1-s\_{i})(\eta\_{t}-b\_{i})+s\_{i}V\_{i,t}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (1−si)2(1−ei)).\displaystyle\;(1-s\_{i})^{2}(1-e\_{i})\big). |  | (5) |

Vi,t+1V\_{i,t+1} is then set to the boundary value if it falls outside of the interval [0,1][0,1].

Whereas bias bib\_{i} and expertise eie\_{i} affect the quality and interpretation of signal Mi,tM\_{i,t}, respectively, stubbornness sis\_{i} affects the agent’s learning rate ([Fig. 1](https://arxiv.org/html/2601.20452v1#S2.F1 "Figure 1 ‣ Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (B) and (C)). Agents are heterogeneous in their willingness to update their market valuation based on this signal of the true election outcome. We represent this stubbornness sis\_{i} as a time-invariant bettor characteristic that affects their relative valuation of signal Mi,tM\_{i,t} and their previous valuation Vi,tV\_{i,t}. Agents whose sis\_{i} are close to 0 mainly form their new market valuation in response to the most recent information signal, whereas agents whose sis\_{i} are close to 11 only incrementally change their valuation in light of new information.

This formulation aligns with canonical adaptive expectations or Bayesian belief updating models that take into account “sticky” or persistent beliefs in opinion or belief formation [[33](https://arxiv.org/html/2601.20452v1#bib.bib35 "Alternatives to Bayesian Updating"), [4](https://arxiv.org/html/2601.20452v1#bib.bib6 "Belief updating: does the ‘good-news, bad-news’ asymmetry extend to purely financial domains?"), [10](https://arxiv.org/html/2601.20452v1#bib.bib12 "Optimism where there is none: Asymmetric belief updating observed with valence-neutral life events"), [3](https://arxiv.org/html/2601.20452v1#bib.bib5 "How much do we learn? Measuring symmetric and asymmetric deviations from Bayesian updating through choices"), [25](https://arxiv.org/html/2601.20452v1#bib.bib26 "Belief adjustment: a double hurdle model and experimental evidence")].

##### Utility Function & Order Placement

Next, given their internal valuation Vi,tV\_{i,t}, budget Bi,tB\_{i,t}, portfolio holdings Ci,tC\_{i,t}, and market price mtm\_{t}, each agent then proposes an optimal order volume xt⋆x^{\star}\_{t}. Agent ii’s proposed order volume at time tt is given by the value xt⋆x^{\star}\_{t} which maximizes the agent’s expected utility function subject to their budget constraint.

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt⋆=arg⁡m​a​xxt​E​[u].x^{\star}\_{t}=\arg max\_{x\_{t}}E[u]. |  | (6) |

Where

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[u]=\displaystyle E[u]= | Vt​u​(Bt−mt​xt+Ct+xt)\displaystyle V\_{t}\;u(B\_{t}-m\_{t}x\_{t}+C\_{t}+x\_{t}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−Vt)​u​(Bt−mt​xt),\displaystyle+(1-V\_{t})\;u(B\_{t}-m\_{t}x\_{t}), |  | (7) |

subject to

|  |  |  |
| --- | --- | --- |
|  | 0≤Bt and 0≤Bt+Ct,0\leq B\_{t}\qquad\text{ and }\qquad 0\leq B\_{t}+C\_{t}, |  |

where u​(⋅)u(\cdot) is a utility function defined by constant relative risk aversion for agents with heterogeneous risk preferences as in [Equation 8](https://arxiv.org/html/2601.20452v1#S2.E8 "8 ‣ Utility Function & Order Placement ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") [[34](https://arxiv.org/html/2601.20452v1#bib.bib36 "A user’s guide to economic utility functions")]. A visualization is shown in [Fig. 1](https://arxiv.org/html/2601.20452v1#S2.F1 "Figure 1 ‣ Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (A).

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(ω)={11−ri​ω1−ri, if ​ri≥0,ri≠1log⁡(ω), if ​ri=1.u(\omega)=\begin{cases}\dfrac{1}{1-r\_{i}}\omega^{1-r\_{i}},\;\;\text{ if }r\_{i}\geq 0,r\_{i}\neq 1\\ \log(\omega),\;\;\text{ if }r\_{i}=1.\end{cases} |  | (8) |

##### Herding Behavior

So far we do not allow the market price to impact the internal valuation of agents. A substantial literature studies herding and social-learning mechanisms in financial markets. However, empirically distinguishing herding from correlated trading driven by shared external information remains difficult, and definitions of herding vary across studies [[14](https://arxiv.org/html/2601.20452v1#bib.bib16 "Informational cascades in financial markets: review and synthesis"), [6](https://arxiv.org/html/2601.20452v1#bib.bib8 "Herd Behavior in Financial Markets")]. Rather than attempting empirical identification, we model herding as a behavioral response to the observed absolute market price. This choice is motivated by the design of binary prediction markets, where prices are commonly interpreted as salient probability signals, in contrast to the relative-price dynamics emphasized in equity markets. We therefore introduce an alternative formulation of [Equation 3](https://arxiv.org/html/2601.20452v1#S2.E3 "3 ‣ Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") incorporating an additional signal of market value in [Equation 9](https://arxiv.org/html/2601.20452v1#S2.E9 "9 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"). hih\_{i} is the agent level parameter which controls the strength of herding, where hi∈[0,1]h\_{i}\in[0,1].

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi,t+1=(1−hi)​((1−si)​(Mi,t−bi)+si​Vi,t)+hi​(mt)V\_{i,t+1}=(1-h\_{i})\big(\big(1-s\_{i}\big)\big(M\_{i,t}-b\_{i}\big)+s\_{i}V\_{i,t}\big)+h\_{i}\big(m\_{t}) |  | (9) |

In [Equation 9](https://arxiv.org/html/2601.20452v1#S2.E9 "9 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"), individuals weight between the valuation calculated as in [Equation 4](https://arxiv.org/html/2601.20452v1#S2.E4 "4 ‣ Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") with the market price by hih\_{i}. We assume independent effects between hih\_{i} and sis\_{i}.

![Refer to caption](x1.png)


Figure 2: Panel A and C show a single simulation from the ABM. Panel A has the true election outcome (red), market price (black) alongside the net supply and demand indicating upward or downward pressure on the market price. The average market valuation of bettors is shown in purple. Panel C visualizes this single run through the number of contracts held across all agents (navy), as well as the net supply and demand (green). Panel (B) shows the validation and robustness checking across the bettor characteristics of expertise, bias, risk aversion, stubbornness and the variance of budgets. The left column shows the mean squared error introduced between the true outcome and the market price across a range of parameter values, and the right column shows the dominant lag. The dominant lag is the single lag ℓ\ell whose one-variable regression of the outcome on the lagged market series yields the strongest statistical fit (lowest p-value). Each simulation has 100 agents over 100 time steps, with an initial price of 0.5 and the variance of the true election outcome 0.05. For each parameter value 30 simulations were performed and default values are Bi,0∼U​(100,1000)B\_{i,0}\sim U(100,1000), Vi,0∼N​(0.5,0.05)V\_{i,0}\sim N(0.5,0.05), Ci,0=0C\_{i,0}=0, si∼𝒩​(0.3,0.05)s\_{i}\sim\mathcal{N}(0.3,0.05), ei∼𝒩​(0.9,0.04)e\_{i}\sim\mathcal{N}(0.9,0.04), ri∼U​(0,1)r\_{i}\sim U(0,1) as shown in [Table 1](https://arxiv.org/html/2601.20452v1#S2.T1 "Table 1 ‣ 2.2. Market ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"). Red lines show the average value across the simulations with a 95% empirical confidence interval. Panel D shows the misclassification probability across different market price and true outcome pairs. As these values are further apart or closer to 0.5, the misclassification probability increases. The diagonal line marks perfect agreement between market and outcome. Regions near ηt=0.5\eta\_{t}=0.5 and mt=0.5m\_{t}=0.5 show a smooth transition between correct and incorrect classification. This transition becomes wider when uncertainty (noise) in either the market price or the true outcome increases, reflecting reduced confidence in whether the market’s implied prediction aligns with the eventual result.

### 2.4.  Modeling Assumptions

This model set-up is defined by the following model assumptions, further influencing our theoretical result outlined in [Section 3.2](https://arxiv.org/html/2601.20452v1#S3.SS2 "3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") later in this work.

1. 1.

   Binary contract payoff: Each contract pays $1 if the target event occurs and $0 otherwise.
2. 2.

   Agent information and signals: Agents are indexed by i=1,…,Ni=1,\dots,N. At each timestep tt agent ii receives a private signal

   |  |  |  |
   | --- | --- | --- |
   |  | Mi,t∼𝒩​(ηt, 1−ei),M\_{i,t}\sim\mathcal{N}(\eta\_{t},\;1-e\_{i}), |  |

   where ηt\eta\_{t} is the underlying (“true”) election value. Signals are assumed independent across agents conditional on ηt\eta\_{t}.
3. 3.

   Price-taking agents (no self-impact): Agents do not account for their own price impact when choosing order sizes. In other words, each agent optimizes while treating the market price mtm\_{t} as exogenous.
4. 4.

   Order matching: The ABM implements randomized order matching. For the analytic derivations below we assume all submitted orders are matched at the market price mtm\_{t}. Under both cases the agent’s expected payoff is consistent with a guaranteed execution at mtm\_{t}.
5. 5.

   Clipping / boundedness: All prices mtm\_{t} and individual valuations Vi,tV\_{i,t} are constrained to the open interval (0,1)(0,1). Any intermediate values outside of (0,1)(0,1) are clipped back into (0,1)(0,1) (hard clipping).
6. 6.

   Feasibility / wealth domain: Agents maintain cash Bi,t≥0B\_{i,t}\geq 0 and holdings Ci,t∈ℝC\_{i,t}\in\mathbb{R}. The utility function requires post-trade cash/wealth arguments to be strictly positive.

### 2.5.  Validation and robustness

Next, we provide evidence of the model’s stability and accuracy across the parameter space by varying the distribution of bettor attributes before applying the ABM to investigate price distortions. Accuracy in this and subsequent sections is defined as the distance between the market price mtm\_{t} and true election outcome ηt\eta\_{t}. We measure how closely the mtm\_{t} tracks ηt\eta\_{t} using two complementary metrics: (1) the mean squared error (MSE) capturing the magnitude of the deviation, and (2) the lag (ℓ\ell) for which the one-variable regression of the true outcome on the lagged market price has the lowest p-value, indicating if there is a lag introduced between market price and true outcome. Respectively, these measure the presence of a non-random relationship between the true and market values and any lags in this relationship, providing insight into the sensitivity and speed of adjustment of the prediction market.

#### 2.5.1. Method

Firstly, we test the performance of our betting market across a range of values for each betting agent attribute. For each agent attribute (stubbornness sis\_{i}, expertise eie\_{i}, bias bib\_{i}, risk aversion rir\_{i}), we iterate across the parameter range in intervals of 0.1, performing 30 simulations for each parameter value while holding all others constant. For each value of the target parameter, every bettor in our prediction market is initialized with the same constant values shown in [Table 1](https://arxiv.org/html/2601.20452v1#S2.T1 "Table 1 ‣ 2.2. Market ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (Bi,0∼U​(100,1000)B\_{i,0}\sim U(100,1000), Vi,0∼N​(0.5,0.05)V\_{i,0}\sim N(0.5,0.05), Ci,0=0C\_{i,0}=0, si∼𝒩​(0.3,0.05)s\_{i}\sim\mathcal{N}(0.3,0.05), ei∼𝒩​(0.9,0.04)e\_{i}\sim\mathcal{N}(0.9,0.04), bi∼0b\_{i}\sim 0, ri∼U​(0,1)r\_{i}\sim U(0,1)).
Note that, in this set of experiments, we do not include herding dynamics; all agents update independently based solely on their internal valuation process.

When we are testing the effect of varying the spread of budgets Bi,0B\_{i,0} across agents we draw the budget for each agent from a normal distribution with variance σB02\sigma^{2}\_{B\_{0}}. This variance is incremented in steps of size $50 to test the impact of a larger spread in the initial budget of the betting agents.

#### 2.5.2. Results

[Fig. 2](https://arxiv.org/html/2601.20452v1#S2.F2 "Figure 2 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (B) demonstrates that the accuracy of the betting market, measured as the MSE between the market price and true election outcome, is robust across majority of the parameter value ranges.

The prediction market is least sensitive to variations in mean levels of risk aversion and budget allocation, with the MSE remaining almost constant in level across all possible values. In the case of both stubbornness and expertise, the MSE only deviates from a stable point at extreme values of each parameter mean. As the value of stubbornness approaches 1, agents approach complete ignorance to any indication of ηt\eta\_{t} causing the market value to deviate significantly from ηt\eta\_{t}. Remarkably, the MSE remains close to zero until very high mean values of stubbornness (greater than 0.8). In the case of expertise, the MSE remains nearly constant around 0.05 until the mean value of expertise approaches 1, at which point bettors are receiving near perfect signals of the true election outcome ηt\eta\_{t} such that the MSE of the market price approaches 0.

However, varying the mean value of bias across the betting population does disturb the predictability of the betting market. As the systematic bias in the beliefs held by the bettors increases or decreases, the MSE of market price increases in magnitude. This result is not surprising as the bias parameter is varied such that it is asymmetric around the true election outcome (i.e. all bettors hold bias in the same direction, either all depreciating or inflating their perception of ηt\eta\_{t}). Further research could investigate the effect of a less asymmetric or heterogeneous bias parameter in the betting population.

These results demonstrate that the information aggregating property of the prediction market ABM exhibits robustness to variation in agent attributes. This has two important implications. First, this demonstrated simulation fidelity suggests that the model of betting agent behavior is sufficiently complex and not sensitive to parameter choices. The model’s stability across parameter ranges allows for considerable modeling flexibility providing a strong foundation for future work. Second, the results are consistent with the characterization of prediction markets as systems that aggregate diverse opinions, a core design motivation emphasized in the prediction markets literature [[56](https://arxiv.org/html/2601.20452v1#bib.bib54 "Prediction Markets")].

While we cannot validate the “accuracy” of prediction markets against realized outcomes until those outcomes occur, we can assess market error ranges relative to observed deviations between leading forecast models and prediction markets. [Fig. 2](https://arxiv.org/html/2601.20452v1#S2.F2 "Figure 2 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") demonstrates that the MSE of our market price and ηt\eta\_{t} ranges from 0.006-0.1 which translates to a mean error of $0.07-$0.30 between our prediction market and ηt\eta\_{t}. For comparison, we use state-level election forecasts from the Economist’s election model for the 2016 and 2020 elections, using forecasts published between May 10, 2016 and November 8, 2016 and March 1, 2020 and November 3, 2020, respectively [[49](https://arxiv.org/html/2601.20452v1#bib.bib59 "U.S. Election Forecast Data, 2016–2020")]. The methodology underlying the Economist forecast model is described in [[24](https://arxiv.org/html/2601.20452v1#bib.bib58 "An updated dynamic Bayesian forecasting model for the US presidential election")]. Our comparison shows that Polymarket prediction prices deviated from these forecasts by a nearly identical range. We provide visual documentation of this validation benchmark in [Section 8.4](https://arxiv.org/html/2601.20452v1#S8.SS4 "8.4. Validation of Market Price Deviation ‣ 8. Supplementary Material ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").

### 2.6.  Relevance of the Price Error to Electoral Outcomes

In empirical research, prices in prediction markets are commonly interpreted as the probability of a future event [[39](https://arxiv.org/html/2601.20452v1#bib.bib40 "Opinion Dynamics Explain Price Formation in Prediction Markets"), [56](https://arxiv.org/html/2601.20452v1#bib.bib54 "Prediction Markets")]. In public settings however, such prices may instead be interpreted using binary decision rules regarding the likely winner, particularly under rapid, headline-level media reporting. Under this interpretation, small deviations around the 0.5 threshold are more likely to flip the implied winner, even when the underlying probabilistic error is small. By treating the market price and true election outcome as normally distributed random variables, we can visualize the probability of misclassification across a range of market and election values [Fig. 2](https://arxiv.org/html/2601.20452v1#S2.F2 "Figure 2 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (D).

## 3. An exploration of market manipulation and volatility

The model provides a tool for researchers to evaluate various mechanisms within prediction markets. We provide the first of such an exploration by stress-testing market resilience to price manipulation. In the remainder of this work we explore how high-budget bettors create sustained market price error, and the interaction between such bettors and herding agents.

### 3.1.  Simulation Study

#### 3.1.1. Method

In order to test the potential for whales to influence the betting market, we simulate the prediction market with 100 betting agents with high expertise (0.95) and introduce a single whale initialized with some proportion of the total budget ρw\rho\_{w}. For a given value of ρw\rho\_{w}, the whale has around 100​ρw/(1−ρw)100\;\rho\_{w}/(1-\rho\_{w}) times the budget of the average non-whale betting agent. The whale has a fixed market valuation above the initial true election outcome. We vary parameter ρw\rho\_{w} in 0.1-size increments to test what, if any, proportion of the total budget (×100\times 100) the whale would require to distort the market price. For each value of ρw\rho\_{w}, 100 simulations were performed. As in the experimental results presented in the previous section, we assess the accuracy of the prediction market using MSE and the lag corresponding to the most significant one-variable regression.

![Refer to caption](x2.png)


Figure 3: Panel A shows the mean squared error between market price and the proportion of budget allocated to a single whale bettor. The whale has a valuation of 0.6 (error of 0.1 above expected election outcome). As with Figure [Fig. 2](https://arxiv.org/html/2601.20452v1#S2.F2 "Figure 2 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (B), each iteration has 100 agents across 100 timesteps. Here, 100 simulations are performed for each parameter value. All agents are initialized with an expertise of 0.95 to reduce the variance of market price. Default values for other attributes are given in [Table 1](https://arxiv.org/html/2601.20452v1#S2.T1 "Table 1 ‣ 2.2. Market ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"). As the proportion of budget allocated to the whale increases, the error increases. Panel (B) shows the profit for non-whale bettors as a proportion of market capital. This plot shows that when a whale is present, the median return for agents with sufficiently high eie\_{i} will increase. Panel (C) shows agreement between theoretical error introduced by a large whale (ρ=0.5\rho=0.5) with varying bias and simulated results from the ABM.

Alongside the error introduced by a single whale, we consider how the presence of a whale affects the non-whale agents by considering the median return for non-whale agents adjusted for market capital.

We also consider how stubbornness and herding affect the recovery of the market price after a whale-induced shock. Herding behavior occurs when agents update their internal valuations according to [Equation 9](https://arxiv.org/html/2601.20452v1#S2.E9 "9 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"). In this setting we consider the absolute error between market price and true election outcome for a system with one whale and 100 non-whale agents. The non-whale agents each have high expertise (ei=0.9e\_{i}=0.9) and homogeneous herding weights from the parameter set hi=0, 0.25, 0.5, 0.75, 1h\_{i}=0,\;0.25,\;0.5,\;0.75,\;1. Whale agents have a fixed valuation set above the market price.

#### 3.1.2. Results

[Fig. 3](https://arxiv.org/html/2601.20452v1#S3.F3 "Figure 3 ‣ 3.1.1. Method ‣ 3.1. Simulation Study ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") demonstrates the results of introducing a whale into the betting market. We summarize these results below.

##### Large Whales Temporarily Distort Market Price

We demonstrate that whales can introduce significant error into the market price, with their effectiveness increasing with budget proportion. Under the outlined parameter set, whales require about 40% of total market capital to induce meaningful error into the market prices. While the minimum budget threshold for inducing error will vary across parameter sets, our results illustrate that prediction markets exhibit meaningful resilience to manipulation by biased agents but are likely to become vulnerable when such agents control sufficient capital.

We see a similar result whether the whale attempts to manipulate the market price downward or upward. Despite the demonstrated resilience of our underlying prediction market model to changes in bettor behavior, these results demonstrate the potential for whales to nonetheless influence prediction market outcomes. However, our results suggest that the relative size of the whale would need to be extremely large to disturb the prediction market outcome.

##### Price Distortions Provide Opportunity for Profit Gain

Additionally, [Fig. 3](https://arxiv.org/html/2601.20452v1#S3.F3 "Figure 3 ‣ 3.1.1. Method ‣ 3.1. Simulation Study ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (B) demonstrates that a temporary price distortion provides an opportunity for considerable profit gain by well-informed bettors (bettors with high expertise ei=0.95e\_{i}=0.95). This profit gain appears to be consistent irrespective of the proportion of total market capital allocated to the whale. This indicates that though the potential distortionary effects of the whale might harm the accuracy of the prediction market, it provides clear opportunity for well-informed bettors to gain profit from the temporarily misaligned market price.

##### Herding and High Stubbornness Compound Distortion Magnitude and Duration

The presence of herding agents influences the decay of a price distortion introduced by a whale. [Fig. 4](https://arxiv.org/html/2601.20452v1#S3.F4 "Figure 4 ‣ 3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") shows how the price distortion introduced by a whale with 30% of market capital in a simulated market with 100 agents with homogeneous herding propensities changes as hih\_{i} increases. Simulated results in panels (A) and (B) show that small to moderate herding strengths do not greatly affect the rate of market recovery, but large values of hih\_{i} can introduce instability characterized by oscillations into the market price. These findings are also explored through theoretical mechanisms in [Section 3.2](https://arxiv.org/html/2601.20452v1#S3.SS2 "3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").

### 3.2.  Theoretical Exploration

To test the results emerging from our simulation-based study, we derive a theoretical solution considering the deterministic behavior of the interacting equations governing our market, its participants, and a high-budget bettor. More precisely, we consider prediction markets as a discrete system where bettor beliefs inform valuations which are transmitted to the market price. By considering the market price update function in [Equation 2](https://arxiv.org/html/2601.20452v1#S2.E2 "2 ‣ 2.2. Market ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"), we will consider how internal valuation and herding affect the magnitude of and decay of error between the market price and true election outcome. Using these two settings, we will consider the impact of the presence of a whale-a biased agent with a fixed market valuation and large budget, and the presence of herding agents in the system.

![Refer to caption](x3.png)


Figure 4: Panel A and B show results for how herding agents impact recovery after a market shock. The system is initialized with a single whale (ρ=0.3\rho=0.3) and 100 agents with high expertise (ei=0.9e\_{i}=0.9 and herding strengths 0, 0.25, 0.5, 0.750,\;0.25,\;0.5,\;0.75 and 11. Instability is visible for hi=1h\_{i}=1 alongside a decreased rate of decay. Panel A shows the absolute market price error across time for each value of hih\_{i} and Panel B shows snapshots at times 20, 50 and 100. For each value of hih\_{i}, 100 simulations were run. Panel C shows a visualization of phase diagram for some values of α\alpha. A purple point labeled hi=1h\_{i}=1 corresponds to the ABM setup with hi=1h\_{i}=1 in panels A and B.

#### 3.2.1. Absent Herding Behavior

Consider a setting where agents i=1,…,Ni=1,\dots,N are *unbiased* with bi=0b\_{i}=0 and budgets Bi,t=(1−ρ)​BΩ/NB\_{i,t}=(1-\rho)B\_{\Omega}/N. To represent a “whale”, let agent N+1N+1 be a *biased* agent with fixed valuation VN+1,t≡WV\_{N+1,t}\equiv W and budget ρ​BΩ\rho B\_{\Omega}. Assume holdings Ci,t=0C\_{i,t}=0 for all agents.

Let time SS correspond to the system being in the steady state, where mS+1=mSm\_{S+1}=m\_{S}. When the market price is stable, the net-demand will be zero, and

|  |  |  |
| --- | --- | --- |
|  | ∑i=1Nxi,S⋆+xN+1,S⋆= 0.\sum\_{i=1}^{N}x\_{i,S}^{\star}+x\_{N+1,S}^{\star}\;=\;0. |  |

To determine the impact of a biased agent on this price update function, we use a linearized version of the order size for each agent ([Equation 10](https://arxiv.org/html/2601.20452v1#S3.E10 "10 ‣ 3.2.1. Absent Herding Behavior ‣ 3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")) (Further details in [Section 8.1](https://arxiv.org/html/2601.20452v1#S8.SS1 "8.1. Order update function in the steady state ‣ 8. Supplementary Material ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi,t⋆=Bi,tmt​(1−mt)​(Vi,t−mt).x\_{i,t}^{\star}\;=\;\frac{B\_{i,t}}{m\_{t}(1-m\_{t})}(V\_{i,t}-m\_{t}). |  | (10) |

Now we can use this to explore the bias introduced into the system of agents with NN unbiased and 1 biased agent. Assuming the unbiased agents’ mean market valuation equals the true value in expectation (i.e. 𝔼​[Vi,S]=ηS\mathbb{E}[V\_{i,S}]=\eta\_{S} under the stated independence assumption and in the absence of bias), we can make the simplification that Vi,S≈ηSV\_{i,S}\approx\eta\_{S} for each unbiased agent. This gives us,

|  |  |  |
| --- | --- | --- |
|  | (1−ρ)​BΩ​(ηS−mS)+ρ​BΩ​(W−mS)= 0.(1-\rho)B\_{\Omega}(\eta\_{S}-m\_{S})\;+\;\rho B\_{\Omega}(W-m\_{S})\;=\;0. |  |

Assuming that δS:=mS−ηS\delta\_{S}:=m\_{S}-\eta\_{S} and ΔS:=W−ηS\Delta\_{S}:=W-\eta\_{S},

|  |  |  |  |
| --- | --- | --- | --- |
|  | δS=ρ​ΔS.\delta\_{S}\;=\;\rho\,\Delta\_{S}. |  | (11) |

Thus, the steady-state price error equals the biased agent’s budget fraction times its valuation error. This gives us the intuitive result that the error introduced into the market price by the presence of a whale is equal to the proportion of the budget which the whale can access and the misvaluation of the whale as validated through our ABM ([Fig. 3](https://arxiv.org/html/2601.20452v1#S3.F3 "Figure 3 ‣ 3.1.1. Method ‣ 3.1. Simulation Study ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") (iii)).

#### 3.2.2. Allowing for Herding Behavior

This potential mechanism for market price manipulation is compounded when agents are endowed with herding behavior. We impose herding behavior as described in [Equation 9](https://arxiv.org/html/2601.20452v1#S2.E9 "9 ‣ Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").

When the market price and true election outcome agree, this herding behavior (hi>0h\_{i}>0) corresponds to increased agreement between agent valuation and market price, since if mt≈ηtm\_{t}\approx\eta\_{t} and conditional on Vi,tV\_{i,t} and ηt\eta\_{t}, the distribution of Vi,t+1∣Vi,t,ηtV\_{i,t+1}\mid V\_{i,t},\eta\_{t} is normal with mean

|  |  |  |
| --- | --- | --- |
|  | (1−hi)​((1−si)​(ηt−bi)+si​Vi,t)+hi​ηt,(1-h\_{i})\big((1-s\_{i})(\eta\_{t}-b\_{i})+s\_{i}V\_{i,t}\big)+h\_{i}\eta\_{t}, |  |

and variance

|  |  |  |
| --- | --- | --- |
|  | (1−hi)2​(1−si)2​(1−ei).(1-h\_{i})^{2}(1-s\_{i})^{2}(1-e\_{i}). |  |

For 0<hi≤10<h\_{i}\leq 1, the variance of this distribution is reduced compared to hi=0h\_{i}=0.

Now consider the system where a shock introduces error between the market price and the true election outcome (i.e. mt=ηt+δtm\_{t}=\eta\_{t}+\delta\_{t}). The shock may occur in the presence of a whale, and we consider how herding agents change how quickly error is removed from the system. In a system of NN agents, the budget-weighted valuation V¯t\bar{V}\_{t} has an expected error of

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V¯t+1−ηt+1∣Vi,t,ηt]=∑i=1Nwi​[(1−hi)​si​(Vi,t−ηt)+hi​δt]\mathbb{E}[\bar{V}\_{t+1}-\eta\_{t+1}\mid V\_{i,t},\eta\_{t}]=\sum\_{i=1}^{N}w\_{i}\big[(1-h\_{i})s\_{i}(V\_{i,t}-\eta\_{t})+h\_{i}\delta\_{t}\big] |  |

where wi=Bi∑i=1NBiw\_{i}=\dfrac{B\_{i}}{\sum\_{i=1}^{N}B\_{i}}. In this budget-weighted average, the average error when δt\delta\_{t} is small shrinks by ∑i=1Nwi​(1−hi)​si\sum\_{i=1}^{N}w\_{i}(1-h\_{i})s\_{i}. So we can see that when the error between the true election outcome and market price is small and agents exhibit more herding and less stubbornness, any error between the internal valuation and true election outcome drop quickly.

For very small δt\delta\_{t}, the expected deviation between an individual agent’s internal valuation and the truth is shrinks with factor (1−hi)​si(1-h\_{i})s\_{i}. For small values of sis\_{i} or large values of hih\_{i}, the internal valuation of the agents corrects to the true value more quickly. A more complete exploration is given in the Supplementary Material ([Section 8.1](https://arxiv.org/html/2601.20452v1#S8.SS1 "8.1. Order update function in the steady state ‣ 8. Supplementary Material ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")).

In general, we can see that large herding weights hih\_{i} increase the strength of the feedback from the market price back into valuations. Large values of sis\_{i} cause the market error to correct more slowly. The interplay of these values with the market step size λ\lambda are important, and may result in unstable or oscillatory behavior if the internal valuation of the agents tends to over correct.

## 4. Discussion

In this work, we build an open-source agent-based model of a prediction market which we use to explore the potential for market manipulation by betting agents with considerable market capital. We find that “whales” are able to temporarily distort price levels in the market. Centrally, we determine that the degree and duration of this distortion depends on the relative budget of the whale agent, stubbornness of non-whale bettors, and the degree to which individuals engage in herding behavior. A theoretical analysis, given in [Section 3.2](https://arxiv.org/html/2601.20452v1#S3.SS2 "3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") supports these findings and identifies explicit relationships between agent attributes and market error and duration.

Recent examples of individuals placing outsized bets in prediction markets have raised questions around the potential consequences for real-world elections. Though our model indicates the potential for diverse agent behavior and competition to self-regulate the market price, we identify conditions under which such manipulation could interfere with these resilient dynamics. Even a temporary distortion caused by a large, stubborn, or strategically biased whale could shape voter expectations, campaign donations, or media narratives. In such cases, market manipulation would not merely affect market accuracy but could feed back into the political process itself, influencing the very outcome being predicted. While we do not incorporate non-market incentives into our whale agent specification, contexts like the U.S., where there is an established pattern of wealthy actors deploying substantial campaign finance contributions to influence elections suggest that such motivations are logically plausible.

Market design and enforcement constrain or enable conditions under which whale-driven price distortions can arise and persist. Earlier prediction markets, such as the Iowa Electronic Markets and PredictIt, typically imposed per-trader caps in the range of hundreds to a few thousand USD per market, which prevented whales through market design. The U.S.-regulated Kalshi platform does not impose a single global position limit; instead, position limits are specified at the contract level, with some markets permitting multi-million-dollar positions for eligible participants under identity-verified participation and CFTC oversight. The current large Polymarket platform represents a further shift in market conditions: participation is pseudonymous and cross-jurisdictional through cryptocurrency use, with no binding per-trader caps, while its price signals are globally visible in real time. Where legal enforcement is limited or fragmented, mitigating manipulation relies more heavily on market design choices.

Our results point to the need for a thoughtfully considered regulatory approach, mainly concerning maximum order sizes, to avoid market price manipulation in election contexts where legal enforcement is feasible. In the US, the Commodity Futures Trading Commission (CFTC) currently oversees federal regulation of prediction markets and has taken a deregulatory approach to election betting in recent years. In a 2024 decision, a federal judge ruled in favor of plaintiff Kalshi, permitting election betting a month prior to the federal election [[52](https://arxiv.org/html/2601.20452v1#bib.bib50 "KalshiEX LLC v. CFTC. 24-5205")]. Within days, Kalshi advertised the legality of election betting on their platform and touted their capacity to handle “individual trades of up to $7 million per contract, while eligible contract participants (ECPs), such as corporations and investment firms can trade up to $100 million” [[29](https://arxiv.org/html/2601.20452v1#bib.bib31 "It’s Official: You Can Now Trade on the U.S. Presidential Election")]. Recently, the CFTC has moved to drop its appeal in this case, further undermining efforts to regulate prediction markets [[30](https://arxiv.org/html/2601.20452v1#bib.bib32 "CFTC moves to drop appeal in Kalshi’s event contracts case"), [50](https://arxiv.org/html/2601.20452v1#bib.bib28 "CFTC Drops Appeal in Kalshi Event Contracts Case")]. Contrary to this trend, our findings suggest the need for a regulatory framework that strikes a balance between recreational freedom and safeguarding democratic integrity.

### 4.1.  Limitations and Further Work

#### 4.1.1. Public Opinion and Belief Formation

The betting agents in our model update their market valuations based on a “true election value.” While unrealistic, this mechanism allows for a simple implementation of a real-world process principally characterized by imperfect or “fuzzy” information. Future work could incorporate more realistic information environments wherein agents integrate global, local, and/or social information. For example, embedding a social network of voting agents within the model, betting agents could formulate beliefs based on their visibility of various communities across the network. Such extensions would not only approach greater realism, but also enable investigation of how misinformation, unbalanced media amplification, and polarization affect information flows from voting constituency to market. This could also enable the use of prediction markets as potential diagnostic tools for understanding evolving social dynamics in electoral contexts.

#### 4.1.2. Market-Election Feedback

Further work should explore the potential feedback between prediction markets and voting behavior. Any non-zero likelihood of market manipulation could have significant implications for the integrity of democratic elections or other real-world outcomes upon which betting markets speculate. Should there exist a potential channel through which a prediction market price could influence voting behavior, public endorsements, campaign finance contributions, or other levers through which a voting population, a political establishment, or a private interest group might affect the outcome of an election, it would raise important questions about the interplay between market-based forecasts and democratic processes. This work does not explore such an interaction. Whether such a link exists would determine the degree of policy concern warranted in light of the results presented in this work.

#### 4.1.3. Bettor Intentions and Non-Pecuniary Utility

In this work, we utilize a complex systems approach, employing a simulation based model to isolate relationships between bettor attributes, behavior and market distortions. This approach does not consider agent intention. Future work could investigate the degree to which agents experiencing non-market utility gains from a political outcome could influence the incentives of biased agents. Careful crafting of such a mechanism could allow whale-like behavior to emerge endogenously. The prevalence of substantial campaign finance contributions deployed to influence electoral results across federal and state jurisdictions in the United States suggests that such incentives may operate within online prediction markets as well.

#### 4.1.4. Market Design

Our ABM implements a random-order, price-first matching prediction market. Alternative market designs include automated market makers or call-market clearing mechanisms. While market design and other modeling choices may affect quantitative outcomes, our implementation reflects the dominant microstructure used in the contemporary prediction market literature and in practice, and results should be interpreted in that context.

## 5. Acknowledgments

We would like to acknowledge thoughtful comments and discussions with fellow participants and faculty mentors of the 2024 Complexity Global School in Bogotá, Colombia. In particular, we would like to thank faculty mentor Rajiv Sethi for early motivating discussions. We would also like to thank Travis Holmes, Jordan Kemp, Will Tracy, and Renaud Lambiotte for important input in later stages of the project.

## 6. Funding

This research was supported by the Emergent Political Economies grant through the Omidyar Network. We would like to thank the Santa Fe Institute for allowing us to conduct this research in the context of the 2024 Complexity Global School in Bogotá, Colombia and 2025 Postdocs in Complexity Conference at the Santa Fe Institute in Santa Fe, New Mexico, USA.

## 7. Author contributions statement

Conceptualization: B.S., E.M., A.B., J.W.; Methodology: B.S., E.M., A.B., J.W.; Software: B.S., E.M.; Validation: B.S., E.M.; Formal analysis: B.S.; Investigation: B.S., E.M., A.B., J.W.; Resources: N/A; Data Curation: B.S., E.M.; Writing - Original Draft: B.S., E.M., J.W.; Writing - Review & Editing: B.S., E.M., A.B., J.W.; Visualization: B.S., E.M.; Supervision: N/A; Project administration: B.S., E.M., A.B., J.W.; Funding acquisition: B.S., E.M., A.B., J.W..

## References

* [1]
  E. Alabrese (2022-12)
  National Polls, Local Preferences and Voters’ Behaviour: Evidence from the UK General Elections.
  Technical report
   Warwick Economics Research Paper Series (TWERPS).
  External Links: [Link](https://ideas.repec.org//p/wrk/warwec/1426.html)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p7.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [2]
  F. Allen, S. Morris, and H. S. Shin (2006-03)
  Beauty Contests and Iterated Expectations in Asset Markets.
  The Review of Financial Studies 19 (3),  pp. 719–752.
  External Links: 3844012,
  ISSN 0893-9454
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p1.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p4.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [3]
  I. Aydogan, A. Baillon, E. Kemel, and C. Li (2025-02)
  How much do we learn? Measuring symmetric and asymmetric deviations from Bayesian updating through choices.
  Quantitative Economics 16 (1),  pp. 329–365.
  External Links: [Document](https://dx.doi.org/10.3982/QE2094),
  [Link](https://onlinelibrary.wiley.com/doi/pdf/10.3982/QE2094)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px1.p8.1 "Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [4]
  K. Barron (2021-03)
  Belief updating: does the ‘good-news, bad-news’ asymmetry extend to purely financial domains?.
  Experimental Economics 24 (1),  pp. 31–58.
  External Links: ISSN 1573-6938,
  [Link](https://doi.org/10.1007/s10683-020-09653-z),
  [Document](https://dx.doi.org/10.1007/s10683-020-09653-z)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px1.p8.1 "Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [5]
  J. E. Berg, F. D. Nelson, and T. A. Rietz (2008-04)
  Prediction Market Accuracy in the Long Run.
  International Journal of Forecasting 24 (2),  pp. 285–300.
  External Links: ISSN 01692070,
  [Document](https://dx.doi.org/10.1016/j.ijforecast.2008.03.007)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p3.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [6]
  S. Bikhchandani and S. Sharma (2001-01)
  Herd Behavior in Financial Markets.
  IMF Staff Papers 47 (3),  pp. 279–310.
  External Links: ISSN 1564-5150,
  [Link](https://doi.org/10.2307/3867650),
  [Document](https://dx.doi.org/10.2307/3867650)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px3.p1.2 "Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [7]
  E. Bothos, D. Apostolou, and G. Mentzas (2010-11)
  Using Social Media to Predict Future Events with Agent-Based Markets.
  IEEE Intelligent Systems 25 (6),  pp. 50–58.
  External Links: ISSN 1541-1672,
  [Document](https://dx.doi.org/10.1109/MIS.2010.152)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p2.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [8]
  A. Boukouras, W. Jennings, L. Li, and Z. Maniadis (2023-06)
  Can biased polls distort electoral results? Evidence from the lab.
  European Journal of Political Economy 78,  pp. 102383.
  External Links: ISSN 0176-2680,
  [Link](https://www.sciencedirect.com/science/article/pii/S0176268023000277),
  [Document](https://dx.doi.org/10.1016/j.ejpoleco.2023.102383)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p7.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [9]
  B. Boulu-Reshef, I. Comeig, R. Donze, and G. D. Weiss (2016-11)
  Risk aversion in prediction markets: A framed-field experiment.
  Journal of Business Research 69 (11),  pp. 5071–5075.
  External Links: ISSN 0148-2963,
  [Document](https://dx.doi.org/10.1016/j.jbusres.2016.04.082)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [10]
  J. W. Burton, A. J. L. Harris, P. Shah, and U. Hahn (2022-01)
  Optimism where there is none: Asymmetric belief updating observed with valence-neutral life events.
  Cognition 218,  pp. 104939.
  External Links: ISSN 0010-0277,
  [Link](https://www.sciencedirect.com/science/article/pii/S0010027721003620),
  [Document](https://dx.doi.org/10.1016/j.cognition.2021.104939)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px1.p8.1 "Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [11]
  C. F. Camerer (1998-12)
  Can Asset Markets Be Manipulated? A Field Experiment With Racetrack Betting.
  Journal of Political Economy 106 (3),  pp. 457–482.
  External Links: 10.1086/250018,
  ISSN 0022-3808,
  [Document](https://dx.doi.org/10.1086/250018)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p4.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [12]
  L. E. Cutting, S. S. Hughes-Berheim, P. M. Johnson, H. Baroud, and B. Goldstein (2025-07)
  Are betting markets better than polling in predicting political elections?.
   arXiv.
  Note: <https://arxiv.org/abs/2507.08921>. Accessed December 2025.
  External Links: [Link](https://arxiv.org/abs/2507.08921)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [13]
  J. Dana, P. Atanasov, P. Tetlock, and B. Mellers (2019-03)
  Are markets more accurate than polls? The surprising informational value of “just asking”.
  Judgment and Decision Making 14 (2),  pp. 135–147.
  External Links: ISSN 1930-2975,
  [Document](https://dx.doi.org/10.1017/S1930297500003375)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [14]
  O. Doherty (2018-03)
  Informational cascades in financial markets: review and synthesis.
  Review of Behavioral Finance 10 (1),  pp. 53–69.
  External Links: ISSN 1940-5979,
  [Document](https://dx.doi.org/10.1108/RBF-05-2016-0030)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px3.p1.2 "Herding Behavior ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [15]
  R. S. Erikson and C. Wlezien (2012-09)
  Markets vs. polls as election predictors: An historical assessment.
  Electoral Studies 31 (3),  pp. 532–539.
  External Links: ISSN 0261-3794,
  [Link](https://www.sciencedirect.com/science/article/pii/S0261379412000467),
  [Document](https://dx.doi.org/10.1016/j.electstud.2012.04.008)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [16]
  P. Escande (2024-10)
  US election betting online: ‘some consider the data to be real-time polls’.
   Le Monde.
  Note: <https://www.lemonde.fr/en/economy/article/2024/10/25/us-election-betting-online-some-consider-the-data-to-be-real-time-polls_6730459_19.html>. Accessed December 2025.
  External Links: [Link](https://www.lemonde.fr/en/economy/article/2024/10/25/us-election-betting-online-some-consider-the-data-to-be-real-time-polls_6730459_19.html)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p7.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [17]
  R. Forsythe, F. Nelson, G. R. Neumann, and J. Wright (1992-12)
  Anatomy of an Experimental Political Stock Market.
  The American Economic Review 82 (5),  pp. 1142–1161.
  External Links: 2117471,
  ISSN 0002-8282
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [18]
  M. Fox (2024-10)
  What to know about the potential $30 million whale moving betting markets toward trump.
   Business Insider.
  Note: <https://www.businessinsider.com/trump-election-odds-polymarket-whale-kamala-harris-polls-betting-markets-2024-10>. Accessed December 2025.
  External Links: [Link](https://www.businessinsider.com/trump-election-odds-polymarket-whale-kamala-harris-polls-betting-markets-2024-10)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p6.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [19]
  M. Galesic, W. Bruine de Bruin, J. Dalege, S. L. Feld, F. Kreuter, H. Olsson, D. Prelec, D. L. Stein, and T. van der Does (2021-07)
  Human social sensing is an untapped resource for computational social science.
  Nature 595 (7866),  pp. 214–222.
  External Links: ISSN 1476-4687,
  [Document](https://dx.doi.org/10.1038/s41586-021-03649-2)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [20]
  L. Garrett (2024-10)
  Americans Bet $100 Million on Trump v. Harris, but at What Cost?.
   NPR.
  Note: <https://www.npr.org/2024/10/29/nx-s1-5132616/election-day-betting-trump-harris>. Accessed December 2025.
  External Links: [Link](https://www.npr.org/2024/10/29/nx-s1-5132616/election-day-betting-trump-harris)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p5.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p7.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [21]
  S. Gjerstad (2004-11)
  Risk aversion, beliefs, and prediction market equilibrium.
  Technical report
   Economic Science Laboratory, University of Arizona.
  External Links: [Link](https://www.researchgate.net/profile/Steven-Gjerstad/publication/23748553_Risk_Aversion_Beliefs_and_Prediction_Market_Equilibrium/links/0deec5231ffeaa2104000000/Risk-Aversion-Beliefs-and-Prediction-Market-Equilibrium.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [22]
  R. Hanson, R. Oprea, and D. Porter (2006-08)
  Information aggregation and manipulation in an experimental market.
  Journal of Economic Behavior & Organization 60 (4),  pp. 449–459.
  External Links: ISSN 0167-2681,
  [Document](https://dx.doi.org/10.1016/j.jebo.2004.09.011)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [23]
  R. Hanson (2003-01)
  Combinatorial information market design.
  Information Systems Frontiers 5 (1),  pp. 107–119.
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p4.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [24]
  Heidemanns, Merlin and Gelman, Andrew and Morris, G Elliott (2020)
  An updated dynamic Bayesian forecasting model for the US presidential election.
  Harvard Data Science Review 2 (4),  pp. 10–1162.
  Cited by: [§2.5.2](https://arxiv.org/html/2601.20452v1#S2.SS5.SSS2.p5.2 "2.5.2. Results ‣ 2.5. Validation and robustness ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [25]
  T. Henckel, G. D. Menzies, P. G. Moffatt, and D. J. Zizzo (2022-02)
  Belief adjustment: a double hurdle model and experimental evidence.
  Experimental Economics 25 (1),  pp. 26–67.
  External Links: ISSN 1573-6938,
  [Link](https://doi.org/10.1007/s10683-021-09701-2),
  [Document](https://dx.doi.org/10.1007/s10683-021-09701-2)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px1.p8.1 "Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [26]
  Kalshi
  Kalshi Data and Analytics.
   Kalshi.
  Note: <https://www.kalshidata.com/>. Accessed December 2025
  External Links: [Link](https://www.kalshidata.com/)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p5.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [27]
  F. M. A. Klingert and M. Meyer (2012-05)
  Comparing Prediction Market Mechanisms Using An Experiment-Based Multi-Agent Simulation.
  In ECMS 2012 Proceedings,
   pp. 654–661.
  External Links: [Document](https://dx.doi.org/10.7148/2012-0654-0661)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p2.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [28]
  A. Leigh and J. Wolfers (2006-09)
  Competing Approaches to Forecasting Elections: Economic Models, Opinion Polling and Prediction Markets.
  Economic Record 82 (258),  pp. 325–340.
  External Links: ISSN 0013-0249, 1475-4932,
  [Document](https://dx.doi.org/10.1111/j.1475-4932.2006.00343.x)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [29]
  T. Mansour (2024-10)
  It’s Official: You Can Now Trade on the U.S. Presidential Election.
   Kalshi.
  Note: <https://news.kalshi.com/p/official-kalshi-makes-history-with-100-legal-election-trading>. Accessed December 2025.
  External Links: [Link](https://news.kalshi.com/p/official-kalshi-makes-history-with-100-legal-election-trading)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p5.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§4](https://arxiv.org/html/2601.20452v1#S4.p4.1 "4. Discussion ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [30]
  L. Matthews and C. Prentice (2025-05)
  CFTC moves to drop appeal in Kalshi’s event contracts case.
  Note: <https://www.reuters.com/markets/commodities/cftc-moves-drop-appeal-kalshis-event-contracts-case-2025-05-05/>. Accessed December 2025.
  External Links: [Link](https://www.reuters.com/markets/commodities/cftc-moves-drop-appeal-kalshis-event-contracts-case-2025-05-05/)
  Cited by: [§4](https://arxiv.org/html/2601.20452v1#S4.p4.1 "4. Discussion ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [31]
  R. B. Morton and K. Ou (2015-12)
  What motivates bandwagon voting behavior: Altruism or a desire to win?.
  European Journal of Political Economy 40,  pp. 224–241.
  External Links: ISSN 0176-2680,
  [Document](https://dx.doi.org/10.1016/j.ejpoleco.2015.04.009)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p7.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [32]
  V. G. Morwitz and C. Pluzinski (1996-06)
  Do Polls Reflect Opinions or Do Opinions Reflect Polls? The Impact of Political Polling on Voters’ Expectations, Preferences, and Behavior.
  Journal of Consumer Research 23 (1),  pp. 53–67.
  External Links: ISSN 0093-5301,
  [Link](https://doi.org/10.1086/209466),
  [Document](https://dx.doi.org/10.1086/209466)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p7.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [33]
  P. Ortoleva (2024-08)
  Alternatives to Bayesian Updating.
  Annual Review of Economics 16,  pp. 545–570.
  External Links: ISSN 1941-1383, 1941-1391,
  [Document](https://dx.doi.org/10.1146/annurev-economics-100223-050352)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px1.p8.1 "Internal Valuation ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [34]
  C. E. Phelps (2024-12)
  A user’s guide to economic utility functions.
  Journal of Risk and Uncertainty 69 (3),  pp. 235–280.
  External Links: ISSN 1573-0476,
  [Link](https://doi.org/10.1007/s11166-024-09443-5),
  [Document](https://dx.doi.org/10.1007/s11166-024-09443-5)
  Cited by: [§2.3.2](https://arxiv.org/html/2601.20452v1#S2.SS3.SSS2.Px2.p1.9 "Utility Function & Order Placement ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [35]
  P. M. Polgreen, F. D. Nelson, G. R. Neumann, and R. A. Weinstein (2007-01)
  Use of Prediction Markets to Forecast Infectious Disease Activity.
  Clinical Infectious Diseases 44 (2),  pp. 272–279.
  External Links: ISSN 1058-4838,
  [Document](https://dx.doi.org/10.1086/510427)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [36]
  Polymarket
  Explore the Highest Volume Popular Polymarkets.
   Polymarket.
  Note: <https://polymarket.com/search?_sort=volume>. Accessed December 2025
  External Links: [Link](https://polymarket.com/search?%5C_sort=volume)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p5.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [37]
  L. Qiu, H. Rui, and A. B. Whinston (2011-12)
  A twitter-based prediction market: social network approach.
  Technical report
  Technical Report 2047846, SSRN.
  External Links: [Document](https://dx.doi.org/10.2139/ssrn.2047846),
  [Link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2047846)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [38]
  M. Quiroz-Gutierrez (2024-10)
  A French whale has bet $45 million on a Trump win so far. Who is this?.
   Fortune.
  Note: <https://fortune.com/2024/10/26/trump-election-polymarket-kamala-harris-bet-us-citizens-crypto/>. Accessed December 2025.
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p6.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [39]
  V. Restocchi, F. McGroarty, E. Gerding, and M. Brede (2023-08)
  Opinion Dynamics Explain Price Formation in Prediction Markets.
  Entropy 25 (8),  pp. 1152.
  External Links: ISSN 1099-4300,
  [Document](https://dx.doi.org/10.3390/e25081152)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p2.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p3.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§2.6](https://arxiv.org/html/2601.20452v1#S2.SS6.p1.1 "2.6. Relevance of the Price Error to Electoral Outcomes ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [40]
  D. Rothschild and N. Malhotra (2014-09)
  Are public opinion polls self-fulfilling prophecies?.
  Research & Politics 1 (2),  pp. 2053168014547667.
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p7.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [41]
  D. Rothschild and R. Sethi (2016-09)
  Trading strategies and market microstructure: evidence from a prediction market.
  The Journal of Prediction Markets 10 (1),  pp. 1–29.
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p2.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [42]
  D. Rothschild (2009-01)
  Forecasting Elections: Comparing Prediction Markets, Polls, and Their Biases.
  Public Opinion Quarterly 73 (5),  pp. 895–916.
  External Links: ISSN 1537-5331, 0033-362X,
  [Document](https://dx.doi.org/10.1093/poq/nfp082)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [43]
  R. Sethi, J. Seager, E. Cai, D. Benjamin, F. Morstatter, O. Bobrownicki, Y. Cheng, A. Kumar, and A. Wanganoo (2024-07)
  Evaluating Prediction Mechanisms: A Profitability Test.
  In Proceedings of the ACM Collective Intelligence Conference,
  CI ’24, New York, NY, USA,  pp. 29–40.
  External Links: [Document](https://dx.doi.org/10.1145/3643562.3672612),
  ISBN 979-8-4007-0554-0
  Cited by: [§2](https://arxiv.org/html/2601.20452v1#S2.p1.4 "2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [44]
  R. Sethi, J. Seager, F. Morstatter, D. Benjamin, A. Hammell, T. Liu, S. Patel, and R. Subramanian (2025-08)
  Political Prediction and the Wisdom of Crowds.
  In Proceedings of the ACM Collective Intelligence Conference,
  CI ’25, New York, NY, USA,  pp. 214–225.
  External Links: [Document](https://dx.doi.org/10.1145/3715928.3737483),
  ISBN 979-8-4007-1489-4
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§1](https://arxiv.org/html/2601.20452v1#S1.p1.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [45]
  D. Shen and G. Shi (2025-06)
  The role of whale investors in the bitcoin market.
  Research in International Business and Finance 78,  pp. 103008.
  External Links: ISSN 0275-5319,
  [Document](https://dx.doi.org/10.1016/j.ribaf.2025.103008)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p2.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [46]
  A. R. Sorkin, R. Mattu, B. Warner, S. Kessler, M. J. d. l. Merced, and L. Hirsch (2024-10)
  The French Connection to Online Bets on Trump.
   The New York Times (en-US).
  External Links: ISSN 0362-4331,
  [Link](https://www.nytimes.com/2024/10/24/business/dealbook/polymarket-trump-trader.html)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p6.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [47]
  M. Spann and B. Skiera (2009-01)
  Sports Forecasting: A Comparison of the Forecast Accuracy of Prediction Markets, Betting Odds and Tipsters.
  Journal of Forecasting 28 (1),  pp. 55–72.
  External Links: ISSN 1099-131X,
  [Document](https://dx.doi.org/10.1002/for.1091)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [48]
  J. Surowiecki (2004-06)
  The wisdom of crowds: why the many are smarter than the few and how collective wisdom shapes business, economies, societies, and nations.
  1. ed edition, Doubleday, New York, NY.
  External Links: ISBN 978-0-385-50386-0
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [49]
  The Economist (2020)
  U.S. Election Forecast Data, 2016–2020.
   The Economist.
  Note: <https://projects.economist.com/us-2020-forecast/president>. Accessed December 2025.
  External Links: [Link](https://projects.economist.com/us-2020-forecast/president)
  Cited by: [§2.5.2](https://arxiv.org/html/2601.20452v1#S2.SS5.SSS2.p5.2 "2.5.2. Results ‣ 2.5. Validation and robustness ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [50]
  Thomson Reuters Practical Law (2025-05)
  CFTC Drops Appeal in Kalshi Event Contracts Case.
   Thomson Reuters Practical Law.
  Note: <https://uk.practicallaw.thomsonreuters.com/w-046-9383>. Accessed December 2025.
  External Links: [Link](https://uk.practicallaw.thomsonreuters.com/w-046-9383)
  Cited by: [§4](https://arxiv.org/html/2601.20452v1#S4.p4.1 "4. Discussion ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [51]
  U.S. Commodity Futures Trading Commission (2025-07-14)
  CFTC Letter 25-20: Amendment to CFTC Letter No. 14-130 (Victoria University / PredictIt).
  Note: <https://www.cftc.gov/node/256156>Accessed January 2026.
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p3.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [52]
  United States Court of Appeals for the District of Columbia Circuit (2024-10)
  KalshiEX LLC v. CFTC. 24-5205.
   Administrative Office of the United States Courts.
  Note: Accession Number: USCOURTS-caDC-24-05205
  Source: DGPO
  External Links: [Link](https://www.govinfo.gov/app/details/USCOURTS-caDC-24-05205)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p5.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§4](https://arxiv.org/html/2601.20452v1#S4.p4.1 "4. Discussion ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [53]
  G. H. Van Bruggen, M. Spann, G. L. Lilien, and B. Skiera (2010-11)
  Prediction Markets as institutional forecasting support systems.
  Decision Support Systems 49 (4),  pp. 404–416.
  External Links: ISSN 0167-9236,
  [Document](https://dx.doi.org/10.1016/j.dss.2010.05.002)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [54]
  L. V. Williams, M. Sung, and J. Johnson (2019-01)
  Prediction markets: Theory, evidence and applications.
  International Journal of Forecasting 35 (1),  pp. 266–270.
  External Links: ISSN 0169-2070,
  [Document](https://dx.doi.org/10.1016/j.ijforecast.2018.11.001)
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [55]
  J. Wingard (2025-11)
  The Polymarket Effect: How Prediction Markets Are Beating The Experts.
   Forbes.
  Note: <https://www.forbes.com/sites/jasonwingard/2025/11/19/the-polymarket-effect-how-prediction-markets-are-beating-the-experts/>. Accessed December 2025.
  External Links: [Link](https://www.forbes.com/sites/jasonwingard/2025/11/19/the-polymarket-effect-how-prediction-markets-are-beating-the-experts/)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [56]
  J. Wolfers and E. Zitzewitz (2004-06)
  Prediction Markets.
  Journal of Economic Perspectives 18 (2),  pp. 107–126.
  External Links: ISSN 0895-3309,
  [Link](https://www.aeaweb.org/articles?id=10.1257/0895330041371321),
  [Document](https://dx.doi.org/10.1257/0895330041371321)
  Cited by: [§2.5.2](https://arxiv.org/html/2601.20452v1#S2.SS5.SSS2.p4.1 "2.5.2. Results ‣ 2.5. Validation and robustness ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"),
  [§2.6](https://arxiv.org/html/2601.20452v1#S2.SS6.p1.1 "2.6. Relevance of the Price Error to Electoral Outcomes ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [57]
  J. Wolfers and E. Zitzewitz (2006-05)
  Interpreting Prediction Market Prices as Probabilities.
  Working Paper
  Technical Report 12200, Working Paper Series, National Bureau of Economic Research.
  External Links: 12200,
  [Document](https://dx.doi.org/10.3386/w12200)
  Cited by: [§1](https://arxiv.org/html/2601.20452v1#S1.p2.1 "1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [58]
  P. F. Yeh (2006-12)
  Using prediction markets to enhance US intelligence capabilities.
  Studies in Intelligence 50 (4).
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p1.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").
* [59]
  T. Yu and S. Chen (2012-02)
  Agent-Based Modeling of the Prediction Markets for Political Elections.
  In Multi-Agent-Based Simulation XII, D. Villatoro, J. Sabater-Mir, and J. S. Sichman (Eds.),
  Berlin, Heidelberg,  pp. 31–43.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-642-28400-7%5F3),
  ISBN 978-3-642-28400-7
  Cited by: [§1.2](https://arxiv.org/html/2601.20452v1#S1.SS2.p2.1 "1.2. Related Literature ‣ 1. Introduction ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").

## 8. Supplementary Material

### 8.1.  Order update function in the steady state

Let time SS correspond to the system being in the steady state, where mS+1=mSm\_{S+1}=m\_{S}. When the market price is stable, the net-demand will be zero, so

|  |  |  |
| --- | --- | --- |
|  | ∑i=1Nxi,S⋆+xN+1,S⋆= 0.\sum\_{i=1}^{N}x\_{i,S}^{\star}+x\_{N+1,S}^{\star}\;=\;0. |  |

To determine the impact of a biased agent on this price update function, we start by finding the expected order size for an agent. Possible orders correspond to maxima of [Equation 7](https://arxiv.org/html/2601.20452v1#S2.E7 "7 ‣ Utility Function & Order Placement ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment"), so begin by taking the derivative with respect to xx ([Equation 8](https://arxiv.org/html/2601.20452v1#S2.E8 "8 ‣ Utility Function & Order Placement ‣ 2.3.2. Behavioral Rules ‣ 2.3. Agents ‣ 2. Agent-based Model ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=\displaystyle 0\;=\; | Vi,t​(1−mt)​u′​(Bi,t−mt​x+Ci,t+x)\displaystyle V\_{i,t}(1-m\_{t})\,u^{\prime}\big(B\_{i,t}-m\_{t}x+C\_{i,t}+x\big)\; |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−Vi,t)​mt​u′​(Bi,t−mt​x).\displaystyle+\;(1-V\_{i,t})m\_{t}\,u^{\prime}\big(B\_{i,t}-m\_{t}x\big). |  | (12) |

The first derivative of the utility function is u′​(ω)=ω−riu^{\prime}(\omega)=\omega^{-r\_{i}} for the non-log case (ri≠1r\_{i}\neq 1), and u′​(ω)=ω−1u^{\prime}(\omega)=\omega^{-1} for the log case (ri=1r\_{i}=1). For general ri≠1r\_{i}\neq 1, [Equation 12](https://arxiv.org/html/2601.20452v1#S8.E12 "12 ‣ 8.1. Order update function in the steady state ‣ 8. Supplementary Material ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") is a nonlinear equation in xx,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =Vi,t​(1−mt)​(Bi,t−mt​x+Ci,t+x)−ri\displaystyle=V\_{i,t}(1-m\_{t})\big(B\_{i,t}-m\_{t}x+C\_{i,t}+x\big)^{-r\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−Vi,t)​mt​(Bi,t−mt​x)−ri.\displaystyle+(1-V\_{i,t})m\_{t}\big(B\_{i,t}-m\_{t}x\big)^{-r\_{i}}. |  |

In the log-case the solutions are

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi,t⋆=mt​(Bi,t+Ci,t−Ci,t​Vi,t)−Bi,t​Vi,tmt​(mt−1).x\_{i,t}^{\star}\;=\;\dfrac{m\_{t}\big(B\_{i,t}+C\_{i,t}-C\_{i,t}V\_{i,t}\big)\;-\;B\_{i,t}V\_{i,t}}{m\_{t}(m\_{t}-1)}. |  | (13) |

To explore the theoretical error introduced by a biased agent, we will use assume that Ci,t=0C\_{i,t}=0. When Ci,t=0C\_{i,t}=0 the expression reduces to the expression shown in [Equation 10](https://arxiv.org/html/2601.20452v1#S3.E10 "10 ‣ 3.2.1. Absent Herding Behavior ‣ 3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment").

Note, we assume mt∉{0,1}m\_{t}\notin\{0,1\} and that xi,t⋆x\_{i,t}^{\star} is a valid solution with respect to the given constraints.

When Ci,t≠0C\_{i,t}\neq 0 or ri≠1r\_{i}\neq 1, we can use a linearized version,

|  |  |  |
| --- | --- | --- |
|  | xi,t⋆​(Vi,t)≈xi,t⋆​(mt)+∂xi,t⋆∂V|V=mt​(Vi,t−mt).x\_{i,t}^{\star}(V\_{i,t})\approx x\_{i,t}^{\star}(m\_{t})+\left.\frac{\partial x\_{i,t}^{\star}}{\partial V}\right|\_{V=m\_{t}}(V\_{i,t}-m\_{t}). |  |

when ∂xi,t⋆∂V|V=mt\left.\frac{\partial x\_{i,t}^{\star}}{\partial V}\right|\_{V=m\_{t}} exists and |Vi,t−mt||V\_{i,t}-m\_{t}| is small.

### 8.2.  Variance of error in the market price

In the specified ABM, each agent has an expertise which controls how clearly they can access information about the market price. This expertise influences the variance of the market price, impacting the uncertainty of the market price around the true election outcome.

Consider a setting with NN agents, each with bias bi=0b\_{i}=0, budget Bi,tB\_{i,t} and internal valuation Vi,tV\_{i,t}. Using the linear order updates for an unbiased agent, we have that

|  |  |  |
| --- | --- | --- |
|  | xi,t⋆=Bi,tmt​(1−mt)​(Vi,t−mt).x\_{i,t}^{\star}\;=\;\frac{B\_{i,t}}{m\_{t}(1-m\_{t})}(V\_{i,t}-m\_{t}). |  |

So if we condition on fixed values of Bi,t,mtB\_{i,t},m\_{t},

|  |  |  |
| --- | --- | --- |
|  | xi,t⋆∣Bi,t,mt,Vi,t−1,bi=0∼𝒩​(β,β2​(1−ei))\displaystyle x\_{i,t}^{\star}\mid B\_{i,t},m\_{t},V\_{i,t-1},b\_{i}=0\sim\mathcal{N}\bigg(\beta,\beta^{2}(1-e\_{i})\bigg) |  |

for β:=Bi,t​ηtmt​(1−mt)​((1−si)+si​Vi,t−1−mt)\beta:=\dfrac{B\_{i,t}\eta\_{t}}{m\_{t}(1-m\_{t})}((1-s\_{i})+s\_{i}V\_{i,t-1}-m\_{t}).

If we consider the net demand across all agents, conditioning on {Bi,t}\{B\_{i,t}\}, {mt}\{m\_{t}\}, and {Vi,t−1}\{V\_{i,t-1}\}, we have that the distribution of DtD\_{t} is approximately

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt∼𝒩(\displaystyle D\_{t}\;\sim\;\mathcal{N}\!\bigg( | ∑i=1NBi,t​ηtmt​(1−mt)​((1−si)+si​Vi,t−1−mt),\displaystyle\sum\_{i=1}^{N}\dfrac{B\_{i,t}\eta\_{t}}{m\_{t}(1-m\_{t})}\big((1-s\_{i})+s\_{i}V\_{i,t-1}-m\_{t}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1N(Bi,tmt​(1−mt))2(1−si)2(1−ei)),\displaystyle\sum\_{i=1}^{N}\left(\dfrac{B\_{i,t}}{m\_{t}(1-m\_{t})}\right)^{\!2}(1-s\_{i})^{2}(1-e\_{i})\bigg), |  |

where we have used the independence of agents’ signals.

From this, the variance of the net demand is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(Dt)=∑i=1N(Bi,tmt​(1−mt))2​(1−si)2​(1−ei).\mathrm{Var}(D\_{t})=\sum\_{i=1}^{N}\left(\dfrac{B\_{i,t}}{m\_{t}(1-m\_{t})}\right)^{\!2}(1-s\_{i})^{2}(1-e\_{i}). |  | (14) |

If the price is a random walk with variance ση2\sigma^{2}\_{\eta}, then the variance of the error between the market price and the true election outcome is a function of the variance of the net demand.

[Equation 14](https://arxiv.org/html/2601.20452v1#S8.E14 "14 ‣ 8.2. Variance of error in the market price ‣ 8. Supplementary Material ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") and [Equation 11](https://arxiv.org/html/2601.20452v1#S3.E11 "11 ‣ 3.2.1. Absent Herding Behavior ‣ 3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") demonstrate that the budget-weighed bias of the agents can introduce bias into the market price, while expertise controls the variance of the error between the market price and true election outcome.

### 8.3.  Stability of price error under herding conditions

To demonstrate the effect which herding has on the market price error over time, assume the linear order update as given in [Equation 10](https://arxiv.org/html/2601.20452v1#S3.E10 "10 ‣ 3.2.1. Absent Herding Behavior ‣ 3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") to find a linear approximation of the error between market price and true election outcome,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt+1=mt+1−ηt+1\displaystyle\delta\_{t+1}=m\_{t+1}-\eta\_{t+1} | =mt+λ​DtKt−ηt+1\displaystyle=m\_{t}+\lambda\dfrac{D\_{t}}{K\_{t}}-\eta\_{t+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≈mt+α​(Vt¯−mt)−ηt\displaystyle\approx m\_{t}+\alpha(\bar{V\_{t}}-m\_{t})-\eta\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−α)​δt+α​(V¯t−ηt).\displaystyle=(1-\alpha)\delta\_{t}+\alpha(\bar{V}\_{t}-\eta\_{t}). |  |

Here, α∝λ​mt​(1−mt)≤0.25​λ\alpha\propto\lambda m\_{t}(1-m\_{t})\leq 0.25\lambda. This assumption holds when ri=1r\_{i}=1 and the market price is sufficiently close to the agent’s valuation.

Combining this with the expected budget weighted valuation across the agents, we can express the market error as an AR(2), with

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt=\displaystyle\delta\_{t}= | [(1−α)+∑iwi​(1−hi)​si]​δt−1\displaystyle\big[(1-\alpha)+\sum\_{i}w\_{i}(1-h\_{i})s\_{i}\big]\,\delta\_{t-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[α​∑iwi​hi−(1−α)​∑iwi​(1−hi)​si]​δt−2.\displaystyle+\big[\alpha\sum\_{i}w\_{i}h\_{i}-(1-\alpha)\sum\_{i}w\_{i}(1-h\_{i})s\_{i}\big]\,\delta\_{t-2}. |  |

Analysis of this AR(2) model gives more precise conditions for when the error between true election outcome and market price will decay to zero. However, in general the error will decay if 1>∑i=1Nwi​[hi+(1−hi)​si]1>\sum\_{i=1}^{N}w\_{i}[h\_{i}+(1-h\_{i})s\_{i}]. For an agent population, this sum can at most be equal to 1, for example if hi=1,si=0h\_{i}=1,s\_{i}=0 for all agents. Hence, for all reasonable parameter values, we will expect the error between the market price and true election outcome to decrease. See [Fig. 4](https://arxiv.org/html/2601.20452v1#S3.F4 "Figure 4 ‣ 3.2. Theoretical Exploration ‣ 3. An exploration of market manipulation and volatility ‣ Manipulation in Prediction Markets: An Agent-based Modeling Experiment") for a more precise visualization of the regions in which the error will decay to zero. A more detailed analysis follows.

The coefficient on δt−1\delta\_{t-1},(1−α)+∑iwi​(1−hi)​si(1-\alpha)+\sum\_{i}w\_{i}(1-h\_{i})s\_{i} is non-negative because α,wi,hi,si≥0\alpha,w\_{i},h\_{i},s\_{i}\geq 0. Note however that being non-negative does not guarantee stable or fast decay. If this coefficient exceeds 1 or when the two coefficients violate stationarity conditions the system can be oscillatory or slowly decaying.

The sign of the coefficient on δt−2\delta\_{t-2},

|  |  |  |
| --- | --- | --- |
|  | α​∑iwi​hi−(1−α)​∑iwi​(1−hi)​si,\alpha\sum\_{i}w\_{i}h\_{i}-(1-\alpha)\sum\_{i}w\_{i}(1-h\_{i})s\_{i}, |  |

can determine if the error dampens or oscilates in time. If the coefficient is smaller than 0 (equivalently
α​∑iwi​hi<(1−α)​∑iwi​(1−hi)​si\alpha\sum\_{i}w\_{i}h\_{i}<(1-\alpha)\sum\_{i}w\_{i}(1-h\_{i})s\_{i},
then δt−2\delta\_{t-2} term tends to dampen the error. In our system, α\alpha tends to be small, so this is generally true.

If the coefficient is greater than zero, for example for some combinations of large α\alpha, large hih\_{i} or small sis\_{i}, the past error tends to reinforce the newer error, increasing persistence and the risk of oscillation or growth. By comparing the coefficient in the AR(2) system, we can see that when feedback from market price into valuations is weak (large hih\_{i} or sis\_{i} small) relative to valuation carry-over then the error induced by the shock decays smoothly. Otherwise, errors will tend to persist or oscillate.

#### 8.3.1. Stability analysis

To derive the stability of AR(2) model for the error between the market price and true election outcome, let

|  |  |  |
| --- | --- | --- |
|  | Sw=∑i=1Nwi​(1−hi)​si,S\_{w}=\sum\_{i=1}^{N}w\_{i}(1-h\_{i})s\_{i}, |  |

and the budget-weighted herding strength average be

|  |  |  |
| --- | --- | --- |
|  | HB¯=∑i=1Nwi​hi\bar{H\_{B}}=\sum\_{i=1}^{N}w\_{i}h\_{i} |  |

. Set

|  |  |  |
| --- | --- | --- |
|  | a:=(1−α)+Sw,b:=α​HB¯−(1−α)​Sw.a:=(1-\alpha)+S\_{w},\qquad b:=\alpha\bar{H\_{B}}-(1-\alpha)S\_{w}. |  |

The error between the market price and true election outcome is then,

|  |  |  |
| --- | --- | --- |
|  | δt=a​δt−1+b​δt−2,\delta\_{t}=a\,\delta\_{t-1}+b\,\delta\_{t-2}, |  |

with characteristic polynomial

|  |  |  |
| --- | --- | --- |
|  | r2−a​r−b=0.r^{2}-ar-b=0. |  |

The two roots are

|  |  |  |  |
| --- | --- | --- | --- |
|  | r1,2\displaystyle r\_{1,2}\; | =a±a2+4​b2\displaystyle=\;\frac{a\pm\sqrt{a^{2}+4b}}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−α)+Sw±((1−α)−Sw)2+4​α​HB¯2.\displaystyle=\;\frac{(1-\alpha)+S\_{w}\pm\sqrt{\big((1-\alpha)-S\_{w}\big)^{2}+4\alpha\bar{H\_{B}}}}{2}. |  |

For a second-order discrete-time polynomial (characteristic polynomial)

|  |  |  |
| --- | --- | --- |
|  | r2−p1​r−p2=0r^{2}-p\_{1}r-p\_{2}=0 |  |

(with p1=a,p2=bp\_{1}=a,\ p\_{2}=b), the necessary and sufficient conditions for the solution to be stable are,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1+p1\displaystyle 1+p\_{1} | >p2,\displaystyle>p\_{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−p1\displaystyle 1-p\_{1} | >p2,\displaystyle>p\_{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p2\displaystyle p\_{2} | >−1.\displaystyle>-1. |  |

The conditions for stability are,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (i) | 1−a>b⟺1>H¯B+Sw\displaystyle 1-a>b\quad\Longleftrightarrow\quad 1>\bar{H}\_{B}+S\_{w} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (ii) | 1+a>b⟺2>α+α​H¯B+(α−2)​Sw,\displaystyle 1+a>b\quad\Longleftrightarrow\quad 2>\alpha+\alpha\bar{H}\_{B}+(\alpha-2)S\_{w}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (iii) | b>−1⟺α>Sw−1H¯B+Sw.\displaystyle b\;>\;-1\quad\Longleftrightarrow\quad\alpha>\dfrac{S\_{w}-1}{\bar{H}\_{B}+S\_{w}}. |  |

We know that 0≤α∝λ​mt​(1−mt)≤0.5​λ0\leq\alpha\propto\lambda\;m\_{t}(1-m\_{t})\leq 0.5\lambda, so we expect α\alpha to be small.

Since Sw=∑i=1Nwi​(1−hi)​siS\_{w}=\sum\_{i=1}^{N}w\_{i}(1-h\_{i})s\_{i}, and the budget-weighted herding strength average be HB¯=∑i=1Nwi​hi\bar{H\_{B}}=\sum\_{i=1}^{N}w\_{i}h\_{i}, for wi,si,hi∈[0,1]w\_{i},s\_{i},h\_{i}\in[0,1], Sw,HB¯∈[0,1]S\_{w},\bar{H\_{B}}\in[0,1].

From these constraints, we see:

1. 1.

   Since α>0\alpha>0 in the model, (i) implies 1>HB+Sw1>H^{B}+S\_{w}.
2. 2.

   For α<1\alpha<1, constraint (ii) will always be satisfied.
3. 3.

   Sw−1≤0S\_{w}-1\leq 0 so (iii) is generally trivial, but care should be taken if SwS\_{w} and H¯B\bar{H}\_{B} are both extremely small or zero.

In simulations, generally α<1\alpha<1, since λ\lambda is small. This means the most informative condition is (i).

### 8.4.  Validation of Market Price Deviation

The following displays the RMSE between the time series of PredictIt market prices (daily closing share price) and Economist forecasts (weekly forecast) of state-level presidential election returns in 2016 (May 10 - November 8) and 2020 (March 1-November 3). We reconcile the periodicity discrepancy between the two data sources by comparing the closing PredictIt share price to the weekly forecast published on the same date. The range of differences between the prediction market price and Economist forecasts are between 5-30 percentage points, indicating stark variability in predictive accuracy. However, this range provides an important benchmark for assessing a feasible price deviation range between our simulated prediction market price and the true electoral preferences.

![Refer to caption](figures/market_price_model_divergence.png)


Figure 5: Root mean squared error between Polymarket market price and Economist Forecast Model of state election returns in the 2016 and 2020 presidential elections.

![Refer to caption](figures/absolute_difference.png)


Figure 6: Absolute difference between Polymarket market price and Economist Forecast Model of state election returns in the 2016 and 2020 presidential elections.

![Refer to caption](figures/Dashapp.png)


Figure 7: Example output from the Dash Application. In this example, each bettor attribute is drawn from a normal distribution with user-specified values. The user can correlate samples for two of these variables, visualizing how these changes affect the prediction market.