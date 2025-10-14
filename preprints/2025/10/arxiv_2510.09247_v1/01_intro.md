---
authors:
- Zofia Bracha
- Paweł Sakowski
- Jakub Michańków
doc_id: arxiv:2510.09247v1
family_id: arxiv:2510.09247
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Abstract
url_abs: http://arxiv.org/abs/2510.09247v1
url_html: https://arxiv.org/html/2510.09247v1
venue: arXiv q-fin
version: 1
year: 2025
---

Application of Deep Reinforcement Learning to At-the-Money S&P 500 Options Hedging

Zofia Bracha1, Paweł Sakowski2, Jakub Michańków3
  
1Faculty of Economic Sciences, University of Warsaw,z.bracha@student.uw.edu.pl
  
2Department of Quantitative Finance and Machine Learning, University of Warsaw,p.sakowski@uw.edu.pl
  
3TripleSun, Krakow, jakub.michankow@triplesun.net

October 2025

## Abstract

This paper explores the application of deep Q-learning to hedging at-the-money options on the S&P 500 index. We develop an agent based on the Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm, trained to simulate hedging decisions without making explicit model assumptions on price dynamics. The agent was trained on historical intraday prices of S&P 500 call options across years 2004 to 2024, using a single time series of six predictor variables: option price, underlying asset price, moneyness, time to maturity, realized volatility, and current hedge position. A walk-forward procedure was applied for training, which lead to nearly 17 years of out-of-sample evaluation. The performance of the deep reinforcement learning (DRL) agent is benchmarked against the Black–Scholes delta hedging strategy over the same time period. We assess both approaches using metrics such as annualized return, volatility, information ratio, and Sharpe ratio. To test models’ adaptability, we performed simulations across varying market conditions and added constraints such as transaction costs and risk-awareness penalties. Our results show that the DRL agent can outperform traditional hedging methods, particularly in volatile or high-cost environments, highlighting its robustness and flexibility in practical trading contexts. While the agent consistently outperforms delta hedging, its performance deteriorates when the risk-awareness parameter is higher. We also observed that the longer the time interval used for volatility estimation, the more stable the results.

Keywords:
  
Deep learning, Reinforcement learning, Double deep Q-networks, options market, options hedging, deep hedging

Thematic classification

C4, C14, C45, C53, C58, G13

## 1 Introduction

Hedging is a risk management technique, used to mitigate potential losses resulting from adverse price movements in assets [Hull, [2018](https://arxiv.org/html/2510.09247v1#bib.bib26)]. In the context of derivatives like options, hedging typically involves dynamically trading the underlying asset to offset the risk exposure introduced by holding the option. The most common approach is called delta hedging, which tries to offset the sensitivity of an option’s value to movements in the underlying by maintaining a position proportional to the option’s delta.

In theory, this continuous rebalancing of the position eliminates all local risk associated with small price fluctuations of the underlying. However, the effectiveness of the hedge depends critically on the frequency of rebalancing, since in reality trading is discrete and subject to frictions, trading costs or liquidity constraints. Additionally, empirical asset returns often exhibit features such as jumps, heavy tails, and volatility clustering. In practice, the theoretical assumptions rarely hold and delta hedging in high cost or volatile environments can lead to losses. This has motivated the search for alternative hedging approaches that are better suited to real-world market dynamics.

In line with the growing interest in developing alternatives to classical methods, reinforcement learning (RL) approach has recently been introduced. Reinforcement learning is a machine learning technique that employs an agent to learn sequential decision-making under uncertainty. In RL, an agent interacts with environment by taking actions based on received feedback and then transferring to the next state, and
gradually learning a policy that maximizes expected return over the whole
period [Sutton and Barto, [2018](https://arxiv.org/html/2510.09247v1#bib.bib48)]. In financial markets applications, this framing is natural: the agent corresponds to the trader, the environment to the market, and the reward function reflects a trade-off between risk reduction and transaction costs. Deep reinforcement learning extends this paradigm by employing deep neural networks to approximate value functions, enabling agents to handle high-dimensional and nonlinear state spaces that arise in realistic market settings.

Early work on applying deep reinforcement learning (DRL) to option hedging was pioneered by Buehler et al. [[2019](https://arxiv.org/html/2510.09247v1#bib.bib8)]. They introduced the Deep Hedging framework, demonstrating that deep neural networks can learn effective hedging policies in simulated markets, even when faced with frictions such as transaction costs, discrete rebalancing, and nonlinearities. Their results highlighted the flexibility of DRL methods compared to traditional stochastic control approaches, particularly when market imperfections complicate classical solutions.

Subsequent works have expanded this line of research, for instance by enriching the simulated environment with additional frictions and multiple hedging instruments or by incorporating utility-based objective in the model Cao et al. [[2021](https://arxiv.org/html/2510.09247v1#bib.bib11)]. They analysed the returns and stability of different functions. Additionally, François [[2025](https://arxiv.org/html/2510.09247v1#bib.bib17)] incorporated the full implied-volatility surface into the simulated market, demonstrating that DRL strategies can substantially outperform classical methods.

Despite these promising simulation based results, most implementations rely on carefully constructed environments or synthetic data, leading to questions about parameters selection and applicability in the real-world market. Addressing this gap, Mikkilä and Kanniainen [[2023](https://arxiv.org/html/2510.09247v1#bib.bib33)] presented one of the first empirical studies, training a DRL model directly on historical S&P 500 index option data. In their paper, they extracted thousands of short time series, then trained the model on the segmented episodes and benchmarked it against classic delta hedging. Their findings indicate that deep hedging strategies can outperform traditional delta hedging, particularly when accounting for transaction costs and liquidity effects.

While research on deep hedging with empirically observed data remains relatively limited, this study seeks to extend the literature by exploring a novel approach. We construct a single, continuous time series of prices of at-the-money call options on S&P 500 with maturity of approximately 30 days. Our goal is to demonstrate that a DRL agent can outperform classical delta hedging method, without a careful path selection process like in Mikkilä and Kanniainen [[2023](https://arxiv.org/html/2510.09247v1#bib.bib33)] paper. Additionally, we aim to showcase the superiority of our model over the benchmark across different trading cost levels and risk aversion of the agent.

The research question is:

* •

  Can the DRL agent achieve superior performance relative to traditional delta hedging strategy across varying market conditions?

The paper is structured in a following way: section 1 provides an introduction, followed by a review of the relevant literature in section 2. Section 3 presents the theoretical background of the study, while section 4 outlines the methodology of the project. Section 5 reports the empirical results, and section 6 concludes.

## 2 Literature review

### 2.1 Alternative hedging

The literature on alternative hedging approaches is broad, reflecting the fact that perfect replication in the Black-Scholes framework is rarely feasible in practice. While this paper concentrates on recent deep reinforcement learning methods, it’s important to recognise the abundance of alternatives to classical delta hedging. One prominent example is variance-optimal hedging Schweizer [[1995](https://arxiv.org/html/2510.09247v1#bib.bib44)], which minimizes the mean-squared hedging error in incomplete markets. This approach provides a systematic way to construct hedges when perfect replication is impossible, and it has been widely applied in quadratic hedging theory. Closely related are utility-based approaches like Pham [[2000](https://arxiv.org/html/2510.09247v1#bib.bib39)], in which the investor selects hedging strategies that maximize the expected utility of terminal wealth. By explicitly modeling preferences and risk aversion, these methods link hedging to portfolio optimization and provide a more economically grounded rationale for trading decisions.

Another important line of research is local risk minimization approach by Föllmer and Sondermann [[1986](https://arxiv.org/html/2510.09247v1#bib.bib16)], Föllmer and Schweizer [[1991](https://arxiv.org/html/2510.09247v1#bib.bib15)], which focuses on minimizing conditional risk at each time step rather than in an overall expected sense. This makes it particularly relevant in discrete-time and incomplete markets, where global variance minimization may not capture the hedger’s real constraints. A further development of this idea is quantile hedging studied by Föllmer and Leukert [[1999](https://arxiv.org/html/2510.09247v1#bib.bib14)], which recognizes frequent limitations of exact replication. Instead of insisting on sure replication, quantile hedging maximizes the probability of meeting the payoff subject to cost constraints, providing a natural trade-off between hedge effectiveness and affordability.

Beyond these rather classical approaches, the more modern frameworks treat hedging as a stochastic control problem. Bertsimas et al. [[2001](https://arxiv.org/html/2510.09247v1#bib.bib5)], applies dynamic programming techniques to derive optimal hedging rules. These models account for transaction costs, or other market frictions. Alternatively, risk measure based hedging approaches directly minimize coherent risk measures such as Conditional Value-at-Risk, thereby aligning hedging objectives with regulatory and risk management practice [Rockafellar and Uryasev, [2000](https://arxiv.org/html/2510.09247v1#bib.bib40)].

### 2.2 Machine learning in hedging

Building on classical approaches, the use of machine learning models for hedging emerges as a natural next step in the research advancement. While classical methods rely on explicit probabilistic models, machine learning offers a data-driven way to create effective strategies directly from observed market dynamics. Early contributions of Hutchinson et al. [[1994](https://arxiv.org/html/2510.09247v1#bib.bib27)] demonstrated that neural networks and non-parametric regressions were able to approximate option prices with high accuracy and generate hedging strategies that frequently outperformed the Black–Scholes delta. This work provided some of the first evidence that data-driven methods could capture non-linearities and market features that traditional parametric models miss.

More recently, Ruf [[2022](https://arxiv.org/html/2510.09247v1#bib.bib41)] offered a systematic perspective on applying machine learning to hedging, with a focus on interpretable and computationally efficient methods. In particular, regression techniques, support vector regression, and tree-based ensembles were highlighted as effective tools to model hedging errors in empirical option data. Their findings indicate that these machine learning methods can yield smaller mean-squared hedging errors than simple linear regression, while retaining greater transparency and robustness compared to deep neural networks. Together, these contributions illustrate the potential of simpler frameworks that do not involve building neural networks to enhance hedging beyond the classical delta-based approaches.

Recent research has extended these insights with a focus on robustness. Wu [[2023](https://arxiv.org/html/2510.09247v1#bib.bib51)] propose risk-aware hedging techniques that explicitly account for model misspecification and regime changes, showing that their method achieves smaller tail losses compared to variance-optimal hedges. Similarly, Hirano [[2023](https://arxiv.org/html/2510.09247v1#bib.bib25)] introduce a method to learn hedging rules directly from data without specifying the underlying price process. Their results suggest that this approach delivers more stable hedging errors across market conditions, particularly when compared against delta hedging under misspecified dynamics. In parallel, Ruf and Wang [[2021](https://arxiv.org/html/2510.09247v1#bib.bib43)] investigate the performance of an artificial neural network (ANN). They propose a HedgeNet and evaluate it against traditional delta hedging and linear regression benchmark. All tested strategies aimed to minimize the hedging error. While the outperformance of the proposed ANN over the benchmarks was significant, the difference between the deep learning approach and linear regression was relatively small. The authors suggest that this may be due to the ANN framework’s superior ability to capture leverage effects.

### 2.3 Deep hedging

The term of Deep hedging was introduced by Buehler et al. [[2019](https://arxiv.org/html/2510.09247v1#bib.bib8)], who proposed a novel framework for optimal hedging based on deep reinforcement learning. The introduced strategy aims to maximize the reward function under a convex risk measure. The generality of this framework enable wide range of objective functions. Buehler et al. [[2019](https://arxiv.org/html/2510.09247v1#bib.bib8)] proposed agent implementation that uses a policy-gradient approach, which directly estimates the hedging policy as a function of state variables. The article clearly demonstrates the great potential of deep hedging and sets foundation for further research. He strengthened and further elaborated his idea in the following studies Bühler et al. [[2021](https://arxiv.org/html/2510.09247v1#bib.bib10)], Murray et al. [[2022](https://arxiv.org/html/2510.09247v1#bib.bib35)], Buehler et al. [[2022](https://arxiv.org/html/2510.09247v1#bib.bib9)].

Following this work, Cao et al. [[2021](https://arxiv.org/html/2510.09247v1#bib.bib11)] extended the framework by investigating alternative objective functions and methods for calculating returns. They compared two perspectives: an accounting approach, in which the P&L reflects the mark-to-market value of the portfolio, and a cash-flow approach, in which only realized inflows and outflows from trades are considered. Their experiments showed that the accounting approach delivers superior results, though they ultimately adopted a hybrid method that balances the two. In addition, they implemented an actor–critic algorithm with two critics: one estimating expected costs and the other estimating the squared value of costs. This design improved robustness by enabling the agent to control not only average performance but also its variability.

Several subsequent studies emphasize how objective design shapes hedging behavior. For instance, François et al. [[2025](https://arxiv.org/html/2510.09247v1#bib.bib19)] show that when risk measures insufficiently penalize adverse outcomes, the difference between deep- and delta hedged portfolios can resemble statistical arbitrage rather than pure risk reduction. Using more conservative risk measures such as CVaR eliminates this effect and produces genuine hedging policies. Along related lines, Neagu et al. [[2025](https://arxiv.org/html/2510.09247v1#bib.bib36)] apply deep hedging under a GJR–GARCH(1,1) model and benchmark a range of reinforcement learning algorithms. They find that Monte Carlo policy-gradient methods consistently outperform value-based approaches in terms of hedging error, with policy-gradient methods being the only ones to surpass the Black–Scholes delta baseline.

Alternative methodological novelties have also appeared. Halperin [[2020](https://arxiv.org/html/2510.09247v1#bib.bib22)] sets the discrete time Black–Scholes-Merton model as a risk-adjusted Markov Decision Process and solve it with Q-learning. Unlike the policy-gradient methods common in deep hedging, their value-based RL approach learns an action–value function that jointly provides option prices and hedging strategies. In frictionless settings, QLBS mimics delta hedging, while remaining extensible to alternative objectives and frictions. As a continuation of this line, Halperin [[2022](https://arxiv.org/html/2510.09247v1#bib.bib23)], develops further machine learning applications to pricing and hedging problems in discrete time. In parallel, Ruf and Wang [[2020](https://arxiv.org/html/2510.09247v1#bib.bib42)] and Ruf and Wang [[2021](https://arxiv.org/html/2510.09247v1#bib.bib43)] study related deep learning approaches and provide a comprehensive literature review of these methods for option pricing and hedging.

Other contributions extend the scope of deep hedging to more complex environments. For example, Kolm et al. [[2020](https://arxiv.org/html/2510.09247v1#bib.bib28)] propose reinforcement learning based dynamic hedging policies that explicitly account for regime switching and microstructure effects. Their results suggest that regime aware hedging adapts more effectively to volatility shifts than static strategies, thereby reducing exposure during turbulent periods. In contrast to such simulator-based approaches, Mikkilä and Kanniainen [[2023](https://arxiv.org/html/2510.09247v1#bib.bib33)] pursue a purely data-driven strategy by training hedging agents directly on high-frequency historical stock–option data. In this paper, the model was trained on a 5 trading day long period of intra-day prices. In this project the considered prices of call options on S&P 500 index with maturity varying from 5 to 70 days. They show that empirical deep hedging achieves robust out-of-sample improvements relative to classical baselines, demonstrating the feasibility of real data training without specifying a volatility model. By comparison, sim-to-real frameworks such as Francois et al. [[2024](https://arxiv.org/html/2510.09247v1#bib.bib18)] have reported promising results, but remain restricted to training on simulated paths rather than full historical datasets.

## 3 Theoretical background

### 3.1 Black-Scholes model (BSM) and hedging

One of the most important model in the financial industry was introduced by Black and Scholes [Black and Scholes, [1973](https://arxiv.org/html/2510.09247v1#bib.bib6)], and independently extended by Merton in 1973 [Merton, [1973](https://arxiv.org/html/2510.09247v1#bib.bib32)]. It assumes a market with constant volatility and interest rates, allowance of continuous trading without transaction costs or liquidity constraints. It is formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=μ​St​d​t+σ​St​d​Wt,dS\_{t}=\mu S\_{t}dt+\sigma S\_{t}dW\_{t}, |  | (1) |

where μ\mu is the drift, σ\sigma the volatility, and WtW\_{t} a standard Brownian motion, and StS\_{t} a stock price. The arbitrage-free price of a European call option at time tt with strike KK, maturity TT, and risk-free rate rr is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(St,t)=St​Φ​(d1)−K​e−r​(T−t)​Φ​(d2),C(S\_{t},t)=S\_{t}\Phi(d\_{1})-Ke^{-r(T-t)}\Phi(d\_{2}), |  | (2) |

where:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d1=ln⁡(StK)+(r+12​σ2)​(T−t)σ​T−t,d2=d1−σ​T−t,d\_{1}=\frac{\ln\!\left(\frac{S\_{t}}{K}\right)+\left(r+\tfrac{1}{2}\sigma^{2}\right)(T-t)}{\sigma\sqrt{T-t}},\quad d\_{2}=d\_{1}-\sigma\sqrt{T-t}, |  | (3) |

and Φ​(⋅)\Phi(\cdot) denotes the standard normal cumulative distribution function.

An important derivation from the BSM model is option delta (Δ\Delta), defined as the sensitivity of the option price with respect to changes in the underlying asset price:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ=∂C∂St\Delta=\frac{\partial C}{\partial S\_{t}} |  | (4) |

For European style call option, Δ=Φ​(d1)\Delta=\Phi(d\_{1}).

From this derivation, we can interpret delta as a hedge ratio that offsets the exposure of a short option position to small movements in StS\_{t}. In other words, this entails holding −Δ-\Delta units of the underlying per option written. As the underlying asset price evolves over time, Δ\Delta changes accordingly, requiring the hedge position to be continuously rebalanced to preserve neutrality. Such strategy is called delta hedging and it is the most common approach to hedging.

In theory, this continuous rebalancing eliminates all local risk associated with small price fluctuations of the underlying. The effectiveness of the hedge, however, depends critically on the frequency of rebalancing, since in reality trading is discrete and subject to frictions. The underlying model was introduced Under these idealized conditions, the model delivers a theoretically perfect hedging strategy through continuous delta rebalancing, such that a riskless portfolio can be constructed and replicated by dynamically adjusting exposure to the underlying asset.

### 3.2 Volatility

Volatility, defined as the magnitude of fluctuations in the price of a financial asset, plays a central role in asset pricing, risk management, and portfolio allocation. Since it’s an unobservable quantity, numerous methodologies have been developed to estimate and forecast volatility.
The three main methods of estimating volatility are: realized (historical) volatility, implied volatility and stochastic volatility.

#### 3.2.1 Realized volatility

It is usually calculated as a statistical measure of past fluctuations in asset returns, most commonly as the standard deviation of log-returns over a specified window. The advantage of using this method is its simplicity in both understanding as well as implementation. However, realized volatility is calculated using past data and it may be inaccurate in reflecting sudden changes in current market conditions. Andersen et al. [[2003](https://arxiv.org/html/2510.09247v1#bib.bib2)]

#### 3.2.2 Implied volatility

In contrast, implied volatility is a measure considering future outlook. It is calculated from the prices of traded options under an assumed pricing model such as BSM model. It represents the market’s expectation of future variability, embedding both the statistical expectation of variance and a risk premium demanded by option sellers. Because implied volatility reflects current market sentiment and expectations, it is often more responsive to new information than historical measures. However, its estimation is inherently model-dependent and may vary across strikes and maturities, leading to volatility smiles and surfaces.

#### 3.2.3 Stochastic volatility

In this framework, volatility is modeled as a stochastic process, meaning it is treated as a latent random variable that evolves over time. Prominent examples include the GARCH family of models [Engle, [1982](https://arxiv.org/html/2510.09247v1#bib.bib13)], [Bollerslev, [1986](https://arxiv.org/html/2510.09247v1#bib.bib7)], the Heston model [Heston, [1993](https://arxiv.org/html/2510.09247v1#bib.bib24)], and the SABR [Hagan et al., [2002](https://arxiv.org/html/2510.09247v1#bib.bib21)] model, each of which captures different aspects of volatility dynamics such as persistence, mean reversion, or stochastic skew. A key challenge in their practical implementation is the calibration of model parameters, as accurate estimation is crucial for ensuring that the model reliability.

Over the years, multiple studies investigated efficiencies of all of these types in different settings (Christensen and Prabhala [[1998](https://arxiv.org/html/2510.09247v1#bib.bib12)], Ammann et al. [[2009](https://arxiv.org/html/2510.09247v1#bib.bib1)], Sjöberg [[2023](https://arxiv.org/html/2510.09247v1#bib.bib46)]). In deep hedging, different approaches were used to estiamte volatility inlcuding implied volatility or simulated with deifferent models. To evaluate a more simplistic approach, in this paper we have decided to use realized volatility to estimate hedge ratio.

### 3.3 Reinforcement Learning

Reinforcement Learning is a machine learning technique in which an agent interacts with an environment over a sequence of discrete time steps [Sutton and Barto, [2018](https://arxiv.org/html/2510.09247v1#bib.bib48)]. At the core of RL is the concept of learning through trial and error, guided by a reward signal. In other words, the model tries to maximise a defined cumulative reward objective function GtG\_{t} over the time period T. At each time step t∈{0,1,2,…}t\in\{0,1,2,\ldots\}, the agent observes the current state st∈𝒮s\_{t}\in\mathcal{S}, selects an action at∈𝒜a\_{t}\in\mathcal{A}, and receives a scalar reward rt∈ℝr\_{t}\in\mathbb{R}. The environment then transitions to a new state st+1s\_{t+1} according to its dynamics P​(s​’∣s,a)P(s’\mid s,a)

The goal of the agent is to learn a policy π\pi, a function mapping states to actions, that maximizes the expected cumulative return. As introduced in Sutton and Barto [[2018](https://arxiv.org/html/2510.09247v1#bib.bib48)], the cumulative return GtG\_{t} is typically defined as the discounted sum of future rewards:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=∑k=0∞γk​rt+k+1.G\_{t}=\sum\_{k=0}^{\infty}\gamma^{k}r\_{t+k+1}. |  | (5) |

#### 3.3.1 Markov Decision Process (MDP)

The formal model underlying reinforcement learning is the Markov decision process, defined as a tuple of 4 variables ℳ=(𝒮,𝒜,P,R)\mathcal{M}=(\mathcal{S},\mathcal{A},P,R),
where each element is defined as follows:

* •

  State space 𝒮\mathcal{S}: the set of all possible states
* •

  Action space 𝒜\mathcal{A}: the set of actions available to the agent
* •

  Transition kernel P​(s​’|s,a)P(s’|s,a): the probability of transitioning to state s​’∈𝒮s’\in\mathcal{S} when action a∈𝒜a\in\mathcal{A} is taken in state s
* •

  Reward function R(s,a): the expected reward obtained at time t immediately after taking action a at state s

Figure [1](https://arxiv.org/html/2510.09247v1#S3.F1 "Rysunek 1 ‣ 3.3.1 Markov Decision Process (MDP) ‣ 3.3 Reinforcement Learning ‣ 3 Theoretical background") below from Sutton and Barto [[2018](https://arxiv.org/html/2510.09247v1#bib.bib48)] illustrates the interactions between different variables.

![Refer to caption](Picture_2.png)


Rysunek 1: Interactions between objects in RL from Sutton and Barto [[2018](https://arxiv.org/html/2510.09247v1#bib.bib48)]

An MDP satisfies the Markov property that states that next state depends only on the current state and action:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡(st+1|s0,a0,s1,a1,…,st,at)=Pr⁡(st+1|st,at)\Pr(s\_{t+1}|s\_{0},a\_{0},s\_{1},a\_{1},\ldots,s\_{t},a\_{t})=\Pr(s\_{t+1}|s\_{t},a\_{t}) |  | (6) |

To evaluate policies and determine actions, we can define value functions that quantify the expected return:

* •

  The state-value function Vπ​(s)V^{\pi}(s) denotes the expected return starting from state s and following a policy π\pi:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Vπ(s)=𝔼π[Gt|st=s]V^{\pi}(s)=\mathbb{E}\_{\pi}\left[G\_{t}\,\middle|\,s\_{t}=s\right] |  | (7) |
* •

  The action-value function Qπ​(s,a)Q^{\pi}(s,a) represents the expected return from state s, when taking action a, and then following policy π\pi:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Qπ(s,a)=𝔼π[Gt|st=s,at=a]Q^{\pi}(s,a)=\mathbb{E}\_{\pi}\left[G\_{t}\,\middle|\,s\_{t}=s,\,a\_{t}=a\right] |  | (8) |

The optimal values for these functions are then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(s)=maxπ⁡Vπ​(s),Q​(s,a)=maxπ⁡Qπ​(s,a).V(s)=\max\_{\pi}V^{\pi}(s),\quad Q(s,a)=\max\_{\pi}Q^{\pi}(s,a). |  | (9) |

And the optimal policy π​(s)\pi(s) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π∗​(s)=arg⁡maxa∈𝒜⁡Q∗​(s,a)\pi^{\*}(s)=\arg\max\_{a\in\mathcal{A}}Q^{\*}(s,a) |  | (10) |

#### 3.3.2 Bellman equations

Another key puzzle in the reinforcement learning frameworks are Bellman equations, which express a recursive relationship between the two value functions Bellman [[1952](https://arxiv.org/html/2510.09247v1#bib.bib4)]. For any policy π\pi, the Bellman equations are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vπ​(s)=∑a∈𝒜π​(a|s)​[R​(s,a)+γ​∑s​’∈𝒮P​(s​’|s,a)​Vπ​(s​’)],V^{\pi}(s)=\sum\_{a\in\mathcal{A}}\pi(a|s)\Big[R(s,a)+\gamma\sum\_{s’\in\mathcal{S}}P(s’|s,a)V^{\pi}(s’)\Big], |  | (11) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qπ​(s,a)=R​(s,a)+γ​∑s​’∈𝒮P​(s​’|s,a)​∑a​’∈𝒜π​(a​’|s​’)​Qπ​(s​’,a​’)Q^{\pi}(s,a)=R(s,a)+\gamma\sum\_{s’\in\mathcal{S}}P(s’|s,a)\sum\_{a’\in\mathcal{A}}\pi(a’|s’)Q^{\pi}(s’,a’) |  | (12) |

  

And the Bellman optimality equations are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗(s)=maxa∈𝒜[R(s,a)+γ∑s​’∈𝒮P(s’|s,a)V(s’)],V^{\*}(s)=\max\_{a\in\mathcal{A}}\Big[R(s,a)+\gamma\sum\_{s’\in\mathcal{S}}P(s’|s,a)V^{(}s’)\Big], |  | (13) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q∗(s,a)=R(s,a)+γ∑s​’∈𝒮P(s’|s,a)maxa​’∈𝒜Q(s’,a’)Q^{\*}(s,a)=R(s,a)+\gamma\sum\_{s’\in\mathcal{S}}P(s’|s,a)\max\_{a’\in\mathcal{A}}Q^{(}s’,a’) |  | (14) |

#### 3.3.3 Temporal Difference Learning

Temporal difference learning is a foundational approach to estimate value functions that doesn’t require complete model of the environment to make predictions. Unlike Monte Carlo methods, which require complete episodes to update value estimates, TD learning updates its predictions incrementally at each time step using bootstrapping Sutton [[1988](https://arxiv.org/html/2510.09247v1#bib.bib47)]. TD learning underpins widely used algorithms such as TD(0), SARSA, and Q-learning, and is particularly well-suited for financial modelling.
  
The simplest form, TD(0), updates the state-value function as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(st)←V​(st)+α​[rt+γ​V​(st+1)−V​(st)],V(s\_{t})\leftarrow V(s\_{t})+\alpha\Big[r\_{t}+\gamma V(s\_{t+1})-V(s\_{t})\Big], |  | (15) |

where α\alpha is the learning rate. The term in brackets is the TD error

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt=rt+γ​V​(st+1)−V​(st),\delta\_{t}=r\_{t}+\gamma V(s\_{t+1})-V(s\_{t}), |  | (16) |

which quantifies the difference between predicted and observed returns.

#### 3.3.4 Q-learning

Introduced by Watkins and Dayan [[1992](https://arxiv.org/html/2510.09247v1#bib.bib50)], Q-learning is an off-policy temporal difference learning framework, which directly estimates the optimal action-value function Q∗​(s,a)Q^{\*}(s,a):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(st,at)←Q​(st,at)+α​[rt+γ​maxa′⁡Q​(st+1,a′)−Q​(st,at)]Q(s\_{t},a\_{t})\leftarrow Q(s\_{t},a\_{t})+\alpha\Big[r\_{t}+\gamma\max\_{a^{\prime}}Q(s\_{t+1},a^{\prime})-Q(s\_{t},a\_{t})\Big] |  | (17) |

In reinforcement learning, off-policy means that the agent learns about the target policy π\pi, while following a different behavior policy β\beta to generate experience. While the methods above provide strong promises, in practice they suffer from scalability issues in environments with large or continuous state and action spaces. To address this, reinforcement learning has been combined with deep learning techniques, giving rise to deep reinforcement learning, where neural networks approximate policies and value functions.

### 3.4 Deep Reinforcement learning

Classical reinforcement learning methods such as dynamic programming or tabular temporal-difference learning rely on explicit representations of value functions and policies. While effective in small state and action spaces, these methods become intractable in high dimensional or continuous domains due to the curse of dimensionality. To overcome this limitation, reinforcement learning has been combined with deep learning techniques, resulting in the field of Deep Reinforcement Learning [Mnih et al., [2015](https://arxiv.org/html/2510.09247v1#bib.bib34)].

Deep RL leverages deep neural networks as function approximators for the value function, action-value function, or policy. Instead of storing values for every state-action pair in a table, a parameterized neural network Q​(s,a;θ)Q(s,a;\theta) or π​(a|s;θ)\pi(a|s;\theta) is trained, where θ\theta denotes the network parameters. This enables generalization across large state spaces and allows learning in complex environments such as video games, robotics, or financial markets.

#### 3.4.1 Deep Q-Networks (DQN)

One of the first major model combining deep learning and reinforcment learning was the Deep Q-Network (DQN), introduced by Mnih et al. [[2015](https://arxiv.org/html/2510.09247v1#bib.bib34)]. DQN approximates the optimal action-value function Q∗​(s,a)Q^{\*}(s,a) using a deep neural network. The update rule extends the classical Q-learning update:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ←θ+α​[yt−Q​(st,at;θ)]​∇θQ​(st,at;θ),\theta\leftarrow\theta+\alpha\Big[y\_{t}-Q(s\_{t},a\_{t};\theta)\Big]\nabla\_{\theta}Q(s\_{t},a\_{t};\theta), |  | (18) |

where the target yty\_{t} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=rt+γ​maxa′⁡Q​(st+1,a′;θ−).y\_{t}=r\_{t}+\gamma\max\_{a^{\prime}}Q(s\_{t+1},a^{\prime};\theta^{-}). |  | (19) |

One drawback of DQN is the systematic overestimation of action values due to the maximization operator applied to noisy value estimates. To mitigate this bias, van Hasselt et al. [[2015](https://arxiv.org/html/2510.09247v1#bib.bib49)] proposed double DQN that separates action selection and evaluation and reduces bias and improve stability:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=rt+1+γ​Q​(st+1,arg⁡maxa′⁡Q​(st+1,a′;θ);θ−)y\_{t}=r\_{t+1}+\gamma\,Q\!\left(s\_{t+1},\arg\max\_{a^{\prime}}Q(s\_{t+1},a^{\prime};\theta)\,;\,\theta^{-}\right) |  | (20) |

#### 3.4.2 Deep Deterministic Policy Gradient (DDPG)

While double DQN are effective in discrete action spaces, computing maxa′⁡Q​(s′,a′)\max\_{a^{\prime}}Q(s^{\prime},a^{\prime}) is impossible in continuous setting, hence the motivation for using policy-based and actor-critic methods. The Deep Deterministic Policy Gradient (DDPG) algorithm, introduced by Lillicrap et al. [[2016](https://arxiv.org/html/2510.09247v1#bib.bib29)], extends the deterministic policy gradient framework by leveraging deep neural networks and key stabilizing techniques from DQN.
DDPG employs two neural networks:

* •

  Actor network μθ​(s)\mu\_{\theta}(s): outputs a deterministic action given state ss.
* •

  Critic network Qϕ​(s,a)Q\_{\phi}(s,a): approximates the action-value function for the current policy.

To improve stability, DDPG uses:

* •

  Target networks μθ′\mu\_{\theta^{\prime}} and Qϕ′Q\_{\phi^{\prime}}, which are slowly updated copies of the actor and critic used to compute stable targets.
* •

  Experience replay buffer 𝒟\mathcal{D}, from which minibatches of past transitions (s,a,r,s′)(s,a,r,s^{\prime}) are sampled to break temporal correlations.

The critic parameters ϕ\phi are updated by minimizing the TD error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(ϕ)=𝔼(s,a,r,s′)∼𝒟​[(Qϕ​(s,a)−y)2],L(\phi)=\mathbb{E}\_{(s,a,r,s^{\prime})\sim\mathcal{D}}\left[\Big(Q\_{\phi}(s,a)-y\Big)^{2}\right], |  | (21) |

with target:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=r+γ​Qϕ′​(s′,μθ′​(s′)).y=r+\gamma Q\_{\phi^{\prime}}(s^{\prime},\mu\_{\theta^{\prime}}(s^{\prime})). |  | (22) |

The actor is updated using the deterministic policy gradient:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θJ​(θ)≈𝔼s∼𝒟​[∇θμθ​(s)​∇aQϕ​(s,a)|a=μθ​(s)].\nabla\_{\theta}J(\theta)\approx\mathbb{E}\_{s\sim\mathcal{D}}\Big[\nabla\_{\theta}\mu\_{\theta}(s)\,\nabla\_{a}Q\_{\phi}(s,a)\big|\_{a=\mu\_{\theta}(s)}\Big]. |  | (23) |

Although DDPG was a major step forward in continuous control, it suffers from several issues:

* •

  Overestimation bias in the critic due to using a single Q-function.
* •

  High variance and instability in learning when the critic is poorly estimated.
* •

  Sensitivity to hyperparameters such as learning rates, noise scale, and target update rate.

These shortcomings motivated the development of more robust actor–critic algorithms, such as Twin Delayed Deep Deterministic Policy Gradient (TD3).

#### 3.4.3 Twin Delayed Deep Deterministic Policy Gradient (TD3)

TD3 introduced by Fujimoto et al. [[2018](https://arxiv.org/html/2510.09247v1#bib.bib20)] represents a significant improvement in stability and performance over earlier actor–critic methods. The three main modifications made to DDPG to address its limitations are:

* •

  Double Q-learning clipping: two critics, Qϕ1Q\_{\phi\_{1}} and Qϕ2Q\_{\phi\_{2}}, are trained in parallel. The target is computed using the minimum of their estimates to reduce overestimation bias:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | yt=rt+1+γ​mini=1,2⁡Qϕi​’​(st+1,μθ​’​(st+1)+ϵ),y\_{t}=r\_{t+1}+\gamma\min\_{i=1,2}Q\_{\phi\_{i}’}(s\_{t+1},\mu\_{\theta’}(s\_{t+1})+\epsilon), |  | (24) |

  where ϵ\epsilon is clipped Gaussian noise
* •

  Target policy smoothing: the action in the target is perturbed by ϵ∼𝒩​(0,σ2)\epsilon\sim\mathcal{N}(0,\sigma^{2}), clipped to a range [-c, c]. This prevents the critic from overfitting. The bounds in this project are [-1,1]
* •

  Delayed policy updates: the actor and target networks are updated less frequently, reducing the likelihood that the policy is updated based on untrained critics.

TD3 retains the off-policy nature of DDPG, using experience replay and noisy behavior policies for exploration, but vastly improves robustness and sample efficiency. These properties make TD3 especially suitable in environments where robustness to noisy estimates and stability of training are critical.

## 4 Methodology

### 4.1 Problem formulation

In this project we model dynamic option hedging as a finite‑horizon Markov Decision Process Markov decision process ℳ=(𝒮,𝒜,P,R)\mathcal{M}=(\mathcal{S},\mathcal{A},P,R) indexed by trading times t=1,…,Tt=1,\dots,T aligned with a historical price path. The agent holds a short option position and trades the underlying to hedge. At time t, the state sts\_{t} summarizes market observed variables and the current hedge; the action at∈ℝa\_{t}\in\mathbb{R} adjusts the hedge position; and the reward rtr\_{t} is the risk‑adjusted incremental hedging PnL. We define the problem as follows:

* •

  State space: 6-dimensional observation vector at each step: option price, underlying price, time-to-maturity, moneyness, realized volatility, current hedge position. These features are predictor variables for the DRL model.
* •

  Action space: actions are one-dimensional and represent a new hedge ratio. They are clipped to [-1, 1] and mapped to a bounded change in position.
* •

  Dynamics: Transitions are driven by the supplied market time series and the internal portfolio recursion. The environment is episodic and advances deterministically through timestamps
* •

  Reward: Risk-adjusted cumulative reward (PnL) described in details later.

#### 4.1.1 Objective function

One of the most important step is the objective function selection. There have been multiple approaches to this topic. Cao et al. [[2021](https://arxiv.org/html/2510.09247v1#bib.bib11)] discussed different PnL calculation techniques for objective function. François [[2025](https://arxiv.org/html/2510.09247v1#bib.bib17)] used a different approach and included risk measures in the objective function. Mikkilä and Kanniainen [[2023](https://arxiv.org/html/2510.09247v1#bib.bib33)] discussed using variance or standard deviation of temporal rewards. Based on this, we have decided to define the maximisation problem as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡𝔼​[wT]−ξ​S​D​(wT),\max\mathbb{E}[w\_{T}]-\xi SD(w\_{T}), |  | (25) |

which is estimated at each step as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=P​n​Lt−ξ​|P​n​Lt|,R\_{t}=PnL\_{t}-\xi|PnL\_{t}|, |  | (26) |

where ξ\xi denotes the linear risk penalty parameter applied to discourage extreme outcomes. This general approach of maximizing risk-adjusted profit originates from the mean–variance utility framework introduced by Markowitz [[1952](https://arxiv.org/html/2510.09247v1#bib.bib30)] and further developed in Markowitz [[1959](https://arxiv.org/html/2510.09247v1#bib.bib31)].

The P​n​LtPnL\_{t} is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PnLt=H​Ot⋅(Ct−Ct−1)+H​St−1⋅(St−St−1)−c⋅|St|⋅|Δ​H​St|\text{PnL}\_{t}=HO\_{t}\cdot(C\_{t}-C\_{t-1})+HS\_{t-1}\cdot(S\_{t}-S\_{t-1})-c\cdot|S\_{t}|\cdot|\Delta HS\_{t}| |  | (27) |

where c represents transaction costs, HS holding of stock, S stock price, HO holding of option, and finally C represents option price.

### 4.2 Model implementation

In this paper we used Twin Delayed Deep Deterministic Policy Gradient (TD3) framework that was introduced in the previous section. As a benchmark model we use traditional delta hedging model, which means that at each time step we adjust our hedge position based on the current prices. Across all periods we assumed 2% risk free rate. The model was implemented using Pytorch library Paszke et al. [[2019](https://arxiv.org/html/2510.09247v1#bib.bib38)]. While the description below should present all details of the implementation, we include a link to the project Github repository with more details at the end of the article.
In this project, similar networks structure was used to Mikkilä and Kanniainen [[2023](https://arxiv.org/html/2510.09247v1#bib.bib33)]. The actor network is a deterministic feed-forward function mapping states to continuous actions. It consists of two hidden layers of size 256 with LeakyReLU activations (negative slope 0.05) and a final Tanh output that ensures the raw action lies within (-1,1).

Both critic networks approximate the state-action value function. They take as input both the state vector and action and process them through three hidden layers of size 256, each followed by LeakyReLU activation function with slope parameter 0.05. The networks terminate in a single linear output representing the scalar Q-value.

The Mean Squared Error (MSE) loss function is used to assess the quality of the critics’ Q-value approximation, while the Adam optimizer updates the actor and critic network weights via gradient descent to reduce this loss and improve the model’s predictive power.

#### 4.2.1 Exploration noise

As highlighted earlier, in models like TD3 exploration must be introduced explicitly because the policy itself is deterministic. Noise is a small stochastic incremanet added to the action that was predicted by the model. In the present framework, two complementary sources of noise were used. The primary mechanism is an Ornstein–Uhlenbeck (OU) process introduced by Ornstein and Uhlenbeck [[1930](https://arxiv.org/html/2510.09247v1#bib.bib37)] applied directly to the agent’s actions. Formally, the Ornstein–Uhlenbeck is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=θ​(μ−Xt)​d​t+σ​d​WtdX\_{t}=\theta(\mu-X\_{t})dt+\sigma dW\_{t} |  | (28) |

where XtX\_{t} denotes the noise state, μ\mu the long-term mean, θ\theta the rate of mean reversion, σ\sigma the volatility parameter, and WtW\_{t} a standard Wiener process.
This process generates smooth and continuous trajectories, thus ensuring that successive actions remain temporally correlated with mean-reverting properties.
Additionally, the added noise decreases over time. Early in training, the larger perturbations encourage broad exploration of the action space, while in later stages the reduced scale allows the agent to stabilize its strategy. The OU noise is scaled by current parameter ata\_{t}, which moves form initial high noise a0a\_{0} to am​i​na\_{min} defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αt=α0−(α0−αmin)⋅min⁡(1,tNdecay).\alpha\_{t}=\alpha\_{0}-(\alpha\_{0}-\alpha\_{\min})\cdot\min\left(1,\frac{t}{N\_{\text{decay}}}\right). |  | (29) |

Similar noise approach was used in Lillicrap et al. [[2016](https://arxiv.org/html/2510.09247v1#bib.bib29)].

The second noise mechanism operates within the TD3 training procedure itself, when the algorithm adds a small Gaussian perturbation to the target policy’s action while computing Bellman targets for the critics. Such noise is also clipped to lie within defined bounds (here [-1,1]). This policy smoothing prevents the critics from overfitting to sharp peaks in their value estimates, thereby reducing overestimation bias and encouraging more conservative learning. Together, these two sources of noise at action selection and smoothing noise in target evaluation provide both good exploration and robustness against critic instability.

#### 4.2.2 Replay buffer

To complement exploration, the agent employs a replay buffer, which is central to off-policy reinforcement learning. The buffer stores past interactions with the environment as a tuple of transitions (st,at,rt,st+1)(s\_{t},a\_{t},r\_{t},s\_{t+1}), where sts\_{t} is the state, ata\_{t} the action taken, rtr\_{t} the resulting reward, st+1s\_{t+1} the next state. The buffer has defined capacity (10000) and operates under a first-in–first-out replacement scheme, so that older experiences are gradually replaced by more recent ones. During training, minibatches of fixed size are drawn uniformly at random from the buffer. This procedure breaks the strong temporal correlations that naturally exist in financial time series, producing approximately i.i.d. samples that are better suited for stochastic gradient descent updates. The replay buffer prevents the critic networks from overfitting to spikes, preserves exploratory actions from early training and prevents harmful feedback loops that could lead to actor overfitting.

#### 4.2.3 Volatility estimation

In this paper we employ a realized volatility framework . First, asset prices PtP\_{t} are transformed into log-returns, defined as
rt=ln⁡(PtPt−1)r\_{t}=\ln\left(\frac{P\_{t}}{P\_{t-1}}\right).
Then the volatility is computed using a rolling standard deviation of log-returns over a specified window length of ww data points. Formally, the realized volatility at time tt is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt=A⋅S​D​(rt−w+1,…,rt),\sigma\_{t}=\sqrt{A}\cdot SD\left(r\_{t-w+1},\ldots,r\_{t}\right), |  | (30) |

where AA is an annualization factor to scale volatility estimates to an annualized level.
  
At the beginning of a time period, when there is less data points than w, the volatility is calculated on rolling basis. Since the volatility is calculated using returns, the first volatility value is impossible to be calculated hence it is replaced with a randomly drawn volatility from a uniform distribution from range [0.02, 0.10]. Volatility window is one of the parameters, on which we perform sensitivity analysis.

### 4.3 Data

For the project we used historical prices of at-the-money call options on S&P 500 with 30 day maturity and S&P 500 itself from years 2004-2024. The data was sourced from CBOE DataShop. For the purpose of this project we have decided to use 30 min frequency for rebalancing. For each time step, the most representative option contract was selected that had the smallest deviations from 30-day maturity and at-the-money moneyness (m​o​n​e​y​n​e​s​s≈1moneyness\approx 1), thus ensuring consistency in option characteristics. This selection criterion mitigates noise and structural shifts due to varying contract availability. To address potential anomalies and discontinuities in price series, a forward-filling mechanism was applied to replace invalid or zero values with the first valid observation, followed by a price-capping procedure that constrained daily price movements within a ±20 % band relative to the previous value. This capping method reduces the influence of outliers that are more likely to be an input error rather than a real observation. Additionally, before training the models, all input data was normalized using Z-score normalisation to improve training.

### 4.4 Training

#### 4.4.1 Walk forward approach

The walk-forward approach is a common technique for training and evaluating machine learning models on time series data [Baranochnikov and Slepaczuk, [2023](https://arxiv.org/html/2510.09247v1#bib.bib3)]. Unlike conventional data splitting methods, which partition the available dataset into fixed and disjoint training, validation, and testing subsets, the walk forward method relies on an iterative scheme that more closely reflects the nature of real-world forecasting tasks.

In this framework, the model is trained on an initial window of historical data and subsequently validated on the immediately following time interval. After evaluation, the training window is rolled forward to include this validation segment, and the process is repeated (Fig. [2](https://arxiv.org/html/2510.09247v1#S4.F2 "Rysunek 2 ‣ 4.4.1 Walk forward approach ‣ 4.4 Training ‣ 4 Methodology")). In each iteration, the model is re-estimated using the most recent information, and performance is assessed on the next unseen period. This procedure continues until the end of the dataset is reached, resulting in a sequence of out-of-sample forecasts that collectively provide a robust estimate of the model’s predictive power.

Such approach offers several advantages:

* •

  Ensures no future information is used to predict past outcomes (temporal leakage risk).
* •

  Allows the model to continuously adapt to evolving data-generating processes, which is particularly valuable in non-stationary environments where structural breaks, regime shifts, or gradual drifts may occur.
* •

  Due to combining multiple out-of-sample periods, the method reduces the variance associated with performance evaluation compared to a single fixed test set, giving more reliable insights into model generalizability.

![Refer to caption](Picture_1.png)


Rysunek 2: Ilustration of a walk forward approach produced using Excel

#### 4.4.2 Hyperperameter tunning

Within each window, hyperparameter tunning is conducted to ensure the model parameters are well adjusted. The hyperparameters that were tunned are presented in the table [1](https://arxiv.org/html/2510.09247v1#S4.T1 "Tabela 1 ‣ 4.4.2 Hyperperameter tunning ‣ 4.4 Training ‣ 4 Methodology") and include exploration parameters, TD3 parameters, and others. reasonable ranges of parameters for tunning were selected during initial tests performed on first window (years 2004-2008). In this project we employ the hyperparameter tunning in each window. Hyperparameters are tuned exclusively on the training and validation time periods to avoid information leakage, with the validation year performance serving as the criterion for selecting the best configuration. To explore the hyperparameter space efficiently, we implement a randomized search procedure in which five candidate parameter sets are drawn from the predefined ranges provided in Table [1](https://arxiv.org/html/2510.09247v1#S4.T1 "Tabela 1 ‣ 4.4.2 Hyperperameter tunning ‣ 4.4 Training ‣ 4 Methodology"). The best-performing configuration, as determined by validation performance, is then retained and evaluated on the subsequent test year. This process is repeated at each walk-forward step, ensuring that the model is continuously adjusted in response to new data.

|  |  |
| --- | --- |
| Parameter | Range |
| TD3 Algorithm | |
| Soft update coefficient (τ\tau) | (0.001,0.01)(0.001,0.01) |
| Discount factor (γ\gamma) | (0.95,0.999)(0.95,0.999) |
| Policy noise | (0.1,0.3)(0.1,0.3) |
| Noise clip | (0.2,0.5)(0.2,0.5) |
| Policy update frequency | (1,5)(1,5) |
| Learning Rates | |
| Actor learning rate | (10−7,10−3)(10^{-7},10^{-3}) |
| Critic learning rate | (10−7,10−3)(10^{-7},10^{-3}) |
| Batch size | (64,512)(64,512) |
| Exploration | |
| Initial noise | (0.2,0.5)(0.2,0.5) |
| Final noise | (0.01,0.1)(0.01,0.1) |
| Noise decay steps | (50,000,200,000)(50{,}000,200{,}000) |
| Ornstein–Uhlenbeck θ\theta | (0.1,0.3)(0.1,0.3) |
| Ornstein–Uhlenbeck σ\sigma | (0.1,0.3)(0.1,0.3) |
| Environment | |
| Initial volatility | (0.10,0.40)(0.10,0.40) |
| Minimum initial volatility | (0.01,0.07)(0.01,0.07) |
| Maximum initial volatility | (0.10,0.40)(0.10,0.40) |

Tabela 1: Hyperparameter ranges

### 4.5 Performance metrics

The performance of the model is measured in multiple ways. We calculate cumulative PnL as described in equation ([27](https://arxiv.org/html/2510.09247v1#S4.E27 "In 4.1.1 Objective function ‣ 4.1 Problem formulation ‣ 4 Methodology")) combined across all out-of-sample periods, normalized by notional=1000$, so the value of 100 represents 100% return on the notional. This approach enables comparison across different option strategies, time periods, and market conditions while maintaining computational stability. In the analysis, we do not account for margin requirements in the case of negative returns. As a result, cumulative return values may reach levels that would be unrealistic in a real-world hedging. Additionally, we compute following performance measures:

#### 4.5.1 Maximum drawdown (MDD)

The maximum drawdown measures the largest observed loss from a peak to a trough of a portfolio’s value before a new peak is attained. It quantifies downside risk over a specified time horizon.

|  |  |  |  |
| --- | --- | --- | --- |
|  | MDD=maxt∈[0,T]⁡(maxτ∈[0,t]⁡V​(τ)−V​(t)maxτ∈[0,t]⁡V​(τ))\text{MDD}=\max\_{t\in[0,T]}\left(\frac{\max\_{\tau\in[0,t]}V(\tau)-V(t)}{\max\_{\tau\in[0,t]}V(\tau)}\right) |  | (31) |

where V(t) is the portfolio value at time t, and T is the investment horizon.

#### 4.5.2 Annualized rate of return (ARC)

The annualized rate of return is the geometric average return per year over the investment horizon.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ARC=(V​(T)V​(0))1Y−1\text{ARC}=\left(\frac{V(T)}{V(0)}\right)^{\tfrac{1}{Y}}-1 |  | (32) |

#### 4.5.3 Annualized Standard Deviation (ASD)

The annualized standard deviation measures the volatility of returns on an annual basis. If returns are observed at frequency m, the scaling is applied as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ASD=σr⋅m\text{ASD}=\sigma\_{r}\cdot\sqrt{m} |  | (33) |

where:

* •

  σr\sigma\_{r} is the standard deviation of periodic returns,
* •

  m is the number of periods per year.

#### 4.5.4 Information ratio

The Information Ratio measures the consistency of active returns relative to a benchmark by dividing average active return by the tracking error.

|  |  |  |  |
| --- | --- | --- | --- |
|  | IR=E​[Rp−Rb]σ​(Rp−Rb)\text{IR}=\frac{E[R\_{p}-R\_{b}]}{\sigma(R\_{p}-R\_{b})} |  | (34) |

where:

* •

  RpR\_{p} is the portfolio return,
* •

  RbR\_{b} is the benchmark return,
* •

  σ​(Rp−Rb)\sigma(R\_{p}-R\_{b}) is the standard deviation of active returns.

Delta hedging strategy performance was used as benchmark in Information ratios calculations.

#### 4.5.5 Adjusted information ratio

The Adjusted Information Ratio (AIR) used here is a custom performance metric that modifies the traditional Information Ratio by explicitly penalizing returns for risk through both volatility and drawdowns. It is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​I​R=I​R⋅A​R​C2−sign⁡(A​R​C)A​S​D⋅|M​D|AIR=IR\cdot\frac{ARC^{2}-\operatorname{sign}(ARC)}{ASD\cdot|MD|} |  | (35) |

where:

* •

  A​R​CARC is the Annualized Return Compounded,
* •

  A​S​DASD is the Annualized Standard Deviation of returns,
* •

  M​DMD is the maximum drawdown,
* •

  IR is information ratio

#### 4.5.6 Sharpe ratio (SR)

The Sharpe Ratio was introduced by Sharpe [[1966](https://arxiv.org/html/2510.09247v1#bib.bib45)]. It evaluates the excess return per unit of total risk, where risk is measured by the standard deviation of portfolio returns.

|  |  |  |  |
| --- | --- | --- | --- |
|  | SR=E​[Rp−Rf]σ​(Rp−Rf)\text{SR}=\frac{E[R\_{p}-R\_{f}]}{\sigma(R\_{p}-R\_{f})} |  | (36) |

where:

* •

  RpR\_{p} is the portfolio return,
* •

  RfR\_{f} is the risk-free rate,
* •

  σ​(Rp−Rf)\sigma(R\_{p}-R\_{f}) is the standard deviation of excess returns.

## 5 Results

### 5.1 Base case

At first we run the comparison with trading cost (c) set to 0.1%, risk penalty parameter (ξ\xi) 1%, and volatility computed using 50 data steps. We performed hyperparameter tuning with 5 random combinations of parameters from defined ranges. Figure [3](https://arxiv.org/html/2510.09247v1#S5.F3 "Rysunek 3 ‣ 5.1 Base case ‣ 5 Results") below represents the cumulative return calculated for each out-of-sample period and combined together in one chart. The statistics included in the tables contain averages of the metrics calculated during each out-of-sample period. Results at Figure [3](https://arxiv.org/html/2510.09247v1#S5.F3 "Rysunek 3 ‣ 5.1 Base case ‣ 5 Results") show that DRL model outperformed the benchmark, even though the return is negative. Additionally, we can observe worse performance of the model in years 2017-2024. We believe that in order for the DRL agent to adapt to the change in market dynamics, more extensive hyperparameter search could be required.

![Refer to caption](01_cumulative_pnl_comparison_baza.png)


Rysunek 3: Cumulative return

The results in the Table [2](https://arxiv.org/html/2510.09247v1#S5.T2 "Tabela 2 ‣ 5.1 Base case ‣ 5 Results") show superior performance of the DRL agent over the classical delta hedging benchmark model. The DRL managed to get positive Information ratio, despite heavy drawdowns and negative returns.

Tabela 2: Comparison of DRL vs. Benchmark in base case scenario

| Metric | DRL | Benchmark (DH) |
| --- | --- | --- |
| Annualized return (ARC) | -0.40% | -0.63% |
| Annualized Std. dev. (ASD) | 0.0576 | 0.0629 |
| Sharpe Ratio | -0.417 | -0.418 |
| Information Ratio | 0.0325 | — |
| Adj. Information Ratio | 23.06 | — |
| Max Drawdown | -75.26% | -81.90% |
| Final PnL (%) | -45.51% | -85.64% |

### 5.2 Transaction costs

In this part we tried varying the transaction cost parameter, which would penalise frequent large changes in position. The tested parameters were as follows: Scenario 1 - C1=0.1%C\_{1}=0.1\%, Scenario 2 - C2=0.05%C\_{2}=0.05\% and Scenario 3 - C3=0.01%C\_{3}=0.01\%.
  
Table [3](https://arxiv.org/html/2510.09247v1#S5.T3 "Tabela 3 ‣ 5.2 Transaction costs ‣ 5 Results") showcases the extended effect of transaction cost on the PnL. While in Scenario 1 both models loose money, the performance significantly improves in the following runs. When the costs are low, the benchmark performs better both in terms of returns or information ratio, but also experiences lower drawdowns. Figures [4](https://arxiv.org/html/2510.09247v1#S5.F4 "Rysunek 4 ‣ 5.2 Transaction costs ‣ 5 Results"), [5](https://arxiv.org/html/2510.09247v1#S5.F5 "Rysunek 5 ‣ 5.2 Transaction costs ‣ 5 Results"), and [6](https://arxiv.org/html/2510.09247v1#S5.F6 "Rysunek 6 ‣ 5.2 Transaction costs ‣ 5 Results") showcase the behaviour of the models across the years.

| Metric | Scenario 1 | | Scenario 2 | | Scenario 3 | |
| --- | --- | --- | --- | --- | --- | --- |
|  | DRL | DH | DRL | DH | DRL | DH |
| Annualized return (ARC) | -1.99% | -10.83% | 1.29% | 0.52% | 1.75% | 4.15% |
| Annualized Std. dev. (ASD) | 0.0607 | 0.0629 | 0.0591 | 0.0630 | 0.0603 | 0.0629 |
| Sharpe Ratio | -0.3285 | -1.7208 | 0.2185 | 0.0819 | 0.2903 | 0.6592 |
| Information Ratio | 0.0501 | — | 0.0188 | — | -0.0909 | — |
| Adj. Information Ratio | 1.11 | — | -0.67 | — | 2.55 | — |
| Max Drawdown | -74.35% | -81.90% | -47.05% | -59.56% | -58.96% | -35.85% |
| Final PnL (%) | -28.88% | -85.64% | 24.28% | 9.11% | 34.17% | 98.99% |

Tabela 3: Comparison of DRL performance vs. delta hedging benchmark across three parameter settings (C1C\_{1} - C3C\_{3}).

![Refer to caption](01_cumulative_pnl_comparison_50.png)


Rysunek 4: Cumulative Return for C1C\_{1}=0.1%

![Refer to caption](01_cumulative_pnl_comparison_mc2.png)


Rysunek 5: Cumulative Return for C2C\_{2}=0.05%

![Refer to caption](01_cumulative_pnl_comparison_lc.png)


Rysunek 6: Cumulative Return for C3C\_{3}=0.01%

Finally, we would like to present an extreme case when costs are equal to 1% Figure [7](https://arxiv.org/html/2510.09247v1#S5.F7 "Rysunek 7 ‣ 5.2 Transaction costs ‣ 5 Results"). The DRL performs significantly better than benchmark, yet still the agent ends up with huge losses - more than 750% on the initial investment.

![Refer to caption](01_cumulative_pnl_comparison_hc.png)


Rysunek 7: Cumulative Return for C4C\_{4}=1%

### 5.3 Volatility window

One of the parameters we would like to analyze in more details is a choice of volatility window. When the window is shorter, the model reacts faster to changes in market regimes, which can lead to model taking action on spikes, rather than actual trends. On the other hand, longer window slows down model reaction and can lead to lower robustness. Given the data is in 30-min frequency, we tested windows of length 20, 50, 100, 150 and 300 steps, which correspond to approximately 1.5, 4, 7.5, 11.5, and 23 trading days. The results are in the Table [4](https://arxiv.org/html/2510.09247v1#S5.T4 "Tabela 4 ‣ 5.3 Volatility window ‣ 5 Results") for DRL model and table [5](https://arxiv.org/html/2510.09247v1#S5.T5 "Tabela 5 ‣ 5.3 Volatility window ‣ 5 Results") for benchmark.

Tabela 4: Performance of DRL strategy across different volatility windows

| Metric | w=300w=300 | w=150w=150 | w=100w=100 | w=50w=50 | w=20w=20 |
| --- | --- | --- | --- | --- | --- |
| Annualized return (ARC) | -0.52% | -0.43% | -0.57% | -0.34% | -0.58% |
| Annualized Std. dev. (ASD) | 0.0612 | 0.0567 | 0.0570 | 0.0607 | 0.0579 |
| Sharpe Ratio | -0.412 | -0.429 | -0.450 | -0.385 | -0.446 |
| Information Ratio | 0.000 | 0.029 | -0.014 | 0.050 | 0.005 |
| Adj. Information Ratio | 21.46 | 24.71 | 21.35 | 22.17 | 20.48 |
| Max Drawdown | -76.11% | -71.32% | -82.15% | -74.35% | -84.39% |
| Final PnL (%) | -65.20% | -52.87% | -79.69% | -28.88% | -80.65% |




Tabela 5: Performance of Delta Hedging (benchmark) across different volatility windows

| Metric | w=300w=300 | w=150w=150 | w=100w=100 | w=50w=50 | w=20w=20 |
| --- | --- | --- | --- | --- | --- |
| Annualized return (ARC) | -0.57% | -0.59% | -0.61% | -0.63% | -0.71% |
| Annualized Std. dev. (ASD) | 0.0630 | 0.0630 | 0.0629 | 0.0629 | 0.0630 |
| Sharpe Ratio | -0.408 | -0.412 | -0.415 | -0.418 | -0.430 |
| Information Ratio | — | — | — | — | — |
| Adj. Information Ratio | — | — | — | — | — |
| Max Drawdown | -79.89% | -80.59% | -81.13% | -81.90% | -83.98% |
| Final PnL (%) | -73.00% | -77.51% | -80.64% | -85.64% | -101.03% |

For delta hedging, the performance clearly deteriorates as the window gets smaller. We observe decrease in annual returns, Sharpe ratio. We also observe higher drawdowns. For DRL, the results are less clear. While we also observe overall trend of decrease in returns and increase in standard deviation or drawdowns, we observe the highest returns for w=50w=50 and lowest drawdowns for w=150w=150. Given the results, we have decided to use w=50w=50 for base case model. Figure [8](https://arxiv.org/html/2510.09247v1#S5.F8 "Rysunek 8 ‣ 5.3 Volatility window ‣ 5 Results") showcases the models performance across the years.

![Refer to caption](01_cumulative_pnl_comparison_20.png)


(a) w=20w=20

![Refer to caption](01_cumulative_pnl_comparison_100.png)


(b) w=100w=100

![Refer to caption](01_cumulative_pnl_comparison_150.png)


(c) w=150w=150

![Refer to caption](01_cumulative_pnl_comparison_300.png)


(d) w=300w=300

Rysunek 8: Cumulative returns for different realized volatility windows (w) - blue represents DRL performance, red - benchmark delta hedging

### 5.4 Risk penalty parameter

At first we have tried varying the penalty parameter ξ\xi in a reward function. We tried values of 0.1, 0.005, 0.001 and additionally 0.01 in base case. We have observed that with the higher risk penalty parameter, the performance of the DRL agent was worse (Figures [10](https://arxiv.org/html/2510.09247v1#S5.F10 "Rysunek 10 ‣ 5.4 Risk penalty parameter ‣ 5 Results"), [3](https://arxiv.org/html/2510.09247v1#S5.F3 "Rysunek 3 ‣ 5.1 Base case ‣ 5 Results") [9](https://arxiv.org/html/2510.09247v1#S5.F9 "Rysunek 9 ‣ 5.4 Risk penalty parameter ‣ 5 Results"). During all those runs trading costs were set to 0.1%.

Tabela 6: Comparison of DRL strategy vs. delta hedging benchmark across three different risk penalty values ξ1=0.001\xi\_{1}=0.001, ξ2=0.005\xi\_{2}=0.005, ξ3=0.1\xi\_{3}=0.1

| Metric | Scenario 1 | | Scenario 2 | | Scenario 3 | |
| --- | --- | --- | --- | --- | --- | --- |
|  | DRL | DH | DRL | DH | DRL | DH |
| Annualized return (ARC) | -0.54% | -0.63% | -0.39% | -0.63% | -0.24% | -0.63% |
| Annualized Std. dev. (ASD) | 0.0553 | 0.0629 | 0.0549 | 0.0629 | 0.0738 | 0.0629 |
| Sharpe Ratio | -0.460 | -0.418 | -0.435 | -0.418 | -0.304 | -0.418 |
| Information Ratio | -0.0108 | — | 0.0527 | — | 0.0541 | — |
| Adj. Information Ratio | 0.17 | — | -0.05 | — | -0.05 | — |
| Max Drawdown | -81.41% | -81.90% | -72.86% | -81.90% | -76.93% | -81.90% |
| Final PnL (%) | -76.66% | -85.64% | -46.12% | -85.64% | 8.19% | -85.64% |

The results in table [6](https://arxiv.org/html/2510.09247v1#S5.T6 "Tabela 6 ‣ 5.4 Risk penalty parameter ‣ 5 Results") indicate that both models on average loose money. Both models also experience very significant drawdowns. Nevertheless, the agent managed to have multiple positive PnL periods, and overall has positive Information ratio. Despite negative returns, we can say that DRL outperformed the benchmark. Figures [9](https://arxiv.org/html/2510.09247v1#S5.F9 "Rysunek 9 ‣ 5.4 Risk penalty parameter ‣ 5 Results"), [10](https://arxiv.org/html/2510.09247v1#S5.F10 "Rysunek 10 ‣ 5.4 Risk penalty parameter ‣ 5 Results"), and [11](https://arxiv.org/html/2510.09247v1#S5.F11 "Rysunek 11 ‣ 5.4 Risk penalty parameter ‣ 5 Results") present graphically results for different values of ξ\xi. We can clearly see the better performance of the DRL model with smaller risk penalty. The deterioration is the most visible in the last few year of the out-of-sample period, when the volatility of prices was significant.

![Refer to caption](01_cumulative_pnl_comparison_hr.png)


Rysunek 9: Cumulative Return for ξ\xi=0.1

![Refer to caption](01_cumulative_pnl_comparison_mr.png)


Rysunek 10: Cumulative Return for ξ\xi=0.005

![Refer to caption](01_cumulative_pnl_comparison_lr.png)


Rysunek 11: Cumulative Return for ξ\xi=0.001

The final observation concluding this sensitivity analysis is that while all parameters for which we performed sensitivity analysis do impact the models’ performance, the impact trading costs level have is far more significant, mostly due to benchmark performance drastically decreasing.

## 6 Conclusions

The goal of this project was to showcase whether the deep reinforcement learning model trained on single historical continuous time series of option prices can outperform a Black-Scholes delta hedging strategy. In order to do this, we gathered data of option prices on S&P 500 index from years 2004-2024 and and at each time step selected at-the-money option with maturity close to 30 days. We implemented Twin Delayed Deep Deterministic Policy Gradient framework using Pytorch and trained the model with walk-forward approach. On the 17 years long out-of-sample period the DRL agent and delta hedging performance was evaluated using cumulative PnL and additional performance metrics such as information ratio, max drawdown or Sharpe ratio.

The general observation from the study is that the DRL model outperforms the delta hedging strategy and achieves higher returns in all but one scenarios. The agent on average had higher Sharpe ratio and lower max drawdown. The deep hedging framework’s advantage is particularly evident in high-cost environments, when the agent tends to adapt to market conditions, while the benchmark’s performance deteriorates sharply. However, we observe that the DRL model is also very sensitive to environment parameters, such as volatility, transaction costs and risk-awareness. During the sensitivity analysis, we observed that the increase in risk aversion reduces returns, while shorter volatility estimation intervals make the model more responsive to jumps and also lower performance. Similarly, higher transaction cost parameter decrease the DRL model’s performance. This issue could be potentially mitigated by less frequent rebalancing, as current setup of trading every 30 minutes drastically increase the costs. Moreover, we would like to highlight that the number of different model parameters to be tuned makes it difficult to reach the full potential of the DRL framework. In this paper, we have made some assumptions about the methodology such as network architecture or PnL and reward accounting method. While this study adds new perspective to deep hedging, by introducing an agent trained on single time series, we believe that further research needs to be done to examine the full range of opportunities of applying deep reinforcement learning to options hedging.

The analysis conducted in this paper allows us to affirmatively answer the research question. The DRL model outperforms traditional delta hedging. Our results showcase sufficient robustness of the framework. Long out-of-sample period and frequency of trading further affirms our conclusion on adaptability and superiority, despite the significant drawdowns of the DRL strategy.

This study presented successful implementation of a deep hedging framework to historical S&P 500 data. We evaluated the results in different market conditions across long period of time. The further research could involve extended empirical experiments with multiple instruments in a portfolio, employing a risk measure in the objective function or extension of the methodology to other markets or derivative types. To extend the existing methodology, further research could include analysing different predictor variables or evaluating different rebalancing frequencies.

## Source code

The complete code can be found and downloaded from Github repository:
  
https://github.com/zof-br/DRL\_hedging

## Literatura

* Ammann et al. [2009]

  Manuel Ammann, David Skovmand, and Michael Verhofen.
  Predicting implied volatility: Cross-sectional efficiency and information content.
  *Review of Derivatives Research*, 12:1–20, 2009.
* Andersen et al. [2003]

  Torben G. Andersen, Tim Bollerslev, Francis X. Diebold, and Paul Labys.
  Modeling and forecasting realized volatility.
  *Econometrica*, 71(2):579–625, March 2003.
  doi: 10.1111/1468-0262.00418.
* Baranochnikov and Slepaczuk [2023]

  Illia Baranochnikov and Robert Slepaczuk.
  A comparison of long short-term memory and gated recurrent unit models’ architectures with novel walk-forward approach to algorithmic investment strategy.
  *SSRN Electronic Journal*, 01 2023.
  doi: 10.2139/ssrn.4628576.
* Bellman [1952]

  Richard Bellman.
  On the theory of dynamic programming.
  *Proceedings of the National Academy of Sciences of the United States of America*, 38(8):716–719, 1952.
  doi: 10.1073/pnas.38.8.716.
* Bertsimas et al. [2001]

  Dimitris Bertsimas, Leonid Kogan, and Andrew W. Lo.
  Hedging derivative securities and incomplete markets: an ε\varepsilon-arbitrage approach.
  *Operations Research*, 49(3):372–397, 2001.
* Black and Scholes [1973]

  Fischer Black and Myron Scholes.
  The pricing of options and corporate liabilities.
  *Journal of Political Economy*, 81(3):637–654, 1973.
* Bollerslev [1986]

  Tim Bollerslev.
  Generalized autoregressive conditional heteroskedasticity.
  *Journal of Econometrics*, 31(3):307–327, 1986.
  doi: 10.1016/0304-4076(86)90063-1.
* Buehler et al. [2019]

  Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood.
  Deep hedging.
  *Quantitative Finance*, 19(8):1271–1291, 2019.
* Buehler et al. [2022]

  Hans Buehler, Phillip Murray, and Ben Wood.
  Deep bellman hedging.
  *arXiv preprint arXiv:2207.00932*, 2022.
* Bühler et al. [2021]

  Hans Bühler, Phillip Murray, Mikko S. Pakkanen, and Ben Wood.
  Deep hedging: Learning to remove the drift under trading frictions with minimal equivalent near-martingale measures.
  *arXiv preprint arXiv:2111.07844*, 2021.
* Cao et al. [2021]

  Jay Cao, Jacky Chen, John Hull, and Zissis Poulos.
  Deep hedging of derivatives using reinforcement learning.
  *arXiv preprint arXiv:2103.16409*, 2021.
* Christensen and Prabhala [1998]

  Bent J Christensen and Nagpurnanand P Prabhala.
  The relation between implied and realized volatility.
  *Journal of Financial Economics*, 50(2):125–150, 1998.
* Engle [1982]

  Robert F. Engle.
  Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation.
  *Econometrica*, 50(4):987–1007, 1982.
  doi: 10.2307/1912773.
* Föllmer and Leukert [1999]

  Hans Föllmer and Peter Leukert.
  Quantile hedging.
  *Finance and Stochastics*, 3(3):251–273, 1999.
* Föllmer and Schweizer [1991]

  Hans Föllmer and Martin Schweizer.
  Hedging of contingent claims under incomplete information.
  *Applied Stochastic Analysis*, pages 389–414, 1991.
* Föllmer and Sondermann [1986]

  Hans Föllmer and Dieter Sondermann.
  Hedging of non-redundant contingent claims.
  *Contributions to Mathematical Economics*, pages 205–223, 1986.
* François [2025]

  P. François.
  Deep hedging with options using the implied volatility surface.
  *arXiv preprint arXiv:2504.06208*, 2025.
* Francois et al. [2024]

  Pascal Francois, Geneviève Gauthier, Frédéric Godin, and Carlos Mendoza.
  Enhancing deep hedging of options with implied volatility surface feedback information.
  07 2024.
  doi: 10.2139/ssrn.4910867.
* François et al. [2025]

  Pascal François, Geneviève Gauthier, Frédéric Godin, and Carlos Octavio Pérez Mendoza.
  Is the difference between deep hedging and delta hedging a statistical arbitrage?
  *Finance Research Letters*, 73:106590, 2025.
* Fujimoto et al. [2018]

  Scott Fujimoto, Herke van Hoof, and David Meger.
  Addressing function approximation error in actor-critic methods.
  2018.
  URL <https://arxiv.org/abs/1802.09477>.
* Hagan et al. [2002]

  Patrick S. Hagan, Deep Kumar, Andrew S. Lesniewski, and Diana E. Woodward.
  Managing smile risk.
  *Wilmott Magazine*, pages 84–108, July 2002.
  First introduction of the SABR model.
* Halperin [2020]

  Igor Halperin.
  Qlbs: Q-learner in the black–scholes(-merton) worlds.
  *Journal of Risk and Financial Management*, 13(2):20, 2020.
* Halperin [2022]

  Igor Halperin.
  *Machine Learning in Finance: From Theory to Practice*.
  Risk Books, 2022.
* Heston [1993]

  Steven L. Heston.
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  *The Review of Financial Studies*, 6(2):327–343, 1993.
  doi: 10.1093/rfs/6.2.327.
* Hirano [2023]

  M Hirano.
  Learning to hedge without price process modeling.
  In *Proceedings of the 4th ACM International Conference on AI in Finance*, pages 1–9. ACM, 2023.
* Hull [2018]

  John C Hull.
  *Options, Futures, and Other Derivatives*.
  Pearson Education, 10 edition, 2018.
* Hutchinson et al. [1994]

  James M. Hutchinson, Andrew W. Lo, and Tomaso Poggio.
  A nonparametric approach to pricing and hedging derivative securities via learning networks.
  *The Journal of Finance*, 49(3):851–889, 1994.
* Kolm et al. [2020]

  Petter N. Kolm, Gordon Ritter, and Patrik Sandås.
  Dynamic replication and hedging: A reinforcement learning approach.
  *Journal of Financial Data Science*, 2(2), 2020.
* Lillicrap et al. [2016]

  Timothy P Lillicrap, Jonathan J Hunt, Alexander Pritzel, et al.
  Continuous control with deep reinforcement learning.
  *International Conference on Learning Representations (ICLR)*, 2016.
* Markowitz [1952]

  Harry Markowitz.
  Portfolio selection.
  *The Journal of Finance*, 7(1):77–91, 1952.
* Markowitz [1959]

  Harry Markowitz.
  *Portfolio Selection: Efficient Diversification of Investments*.
  Yale University Press, New Haven, CT, 1959.
* Merton [1973]

  Robert C Merton.
  Theory of rational option pricing.
  *Bell Journal of Economics and Management Science*, 4(1):141–183, 1973.
* Mikkilä and Kanniainen [2023]

  Oskari Mikkilä and Juho Kanniainen.
  Empirical deep hedging.
  *Quantitative Finance*, 23(1):111–122, 2023.
* Mnih et al. [2015]

  Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, et al.
  Human-level control through deep reinforcement learning.
  *Nature*, 518(7540):529–533, 2015.
* Murray et al. [2022]

  Phillip Murray, Ben Wood, Hans Bühler, Magnus Wiese, and Mikko S. Pakkanen.
  Deep hedging: Continuous reinforcement learning for hedging of general portfolios across multiple risk aversions.
  *arXiv preprint arXiv:2207.07467*, 2022.
* Neagu et al. [2025]

  Andrei Neagu, Frédéric Godin, and Leila Kosseim.
  Deep reinforcement learning algorithms for option hedging.
  2025.
  URL <https://arxiv.org/abs/2504.05521>.
* Ornstein and Uhlenbeck [1930]

  Leonard Ornstein and George E. Uhlenbeck.
  On the theory of brownian motion.
  *Physical Review*, 1930.
  Introduced the Ornstein–Uhlenbeck process as a mean-reverting solution to Langevin’s equation.
* Paszke et al. [2019]

  Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Köpf, Edward Yang, Zach DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala.
  Pytorch: An imperative style, high-performance deep learning library.
  2019.
* Pham [2000]

  Huyen Pham.
  On quadratic hedging in continuous time.
  *Mathematics of Operations Research*, 25(2):290–315, 2000.
  doi: 10.1287/moor.25.2.290.12218.
* Rockafellar and Uryasev [2000]

  R. Tyrrell Rockafellar and Stanislav Uryasev.
  Optimization of conditional value-at-risk.
  *Journal of Risk*, 2:21–41, 2000.
* Ruf [2022]

  Johannes Ruf.
  Machine learning approaches to hedging.
  In *Proceedings of the Fields Institute Workshop on AI in Finance*. Fields Institute, 2022.
* Ruf and Wang [2020]

  Johannes Ruf and Weiguan Wang.
  Neural networks for option pricing and hedging: a literature review.
  2020.
  URL <https://arxiv.org/abs/1911.05620>.
* Ruf and Wang [2021]

  Johannes Ruf and Weiguan Wang.
  Hedging with linear regressions and neural networks.
  *Journal of Business & Economic Statistics*, 39(1):1–18, 2021.
* Schweizer [1995]

  Martin Schweizer.
  Variance-optimal hedging in discrete time.
  *Mathematics of Operations Research*, 20(1):1–32, 1995.
  doi: 10.1287/moor.20.1.1.
* Sharpe [1966]

  William F. Sharpe.
  Mutual fund performance.
  *The Journal of Business*, 39(S1):119–138, 1966.
  doi: 10.1086/294846.
* Sjöberg [2023]

  Emil Sjöberg.
  The predictive power of implied and realized volatility on the swedish market.
  Bachelor Thesis, Uppsala University, 2023.
  URL <https://www.diva-portal.org/smash/get/diva2%3A1781413/FULLTEXT01.pdf>.
* Sutton [1988]

  Richard S. Sutton.
  Learning to predict by the methods of temporal differences.
  *Machine Learning*, 3(1):9–44, 1988.
  doi: 10.1007/BF00115009.
* Sutton and Barto [2018]

  Richard S Sutton and Andrew G Barto.
  *Reinforcement Learning: An Introduction*.
  MIT press, 2 edition, 2018.
* van Hasselt et al. [2015]

  Hado van Hasselt, Arthur Guez, and David Silver.
  Deep reinforcement learning with double q-learning.
  2015.
  URL <https://arxiv.org/abs/1509.06461>.
* Watkins and Dayan [1992]

  Christopher J. C. H. Watkins and Peter Dayan.
  Q-learning.
  *Machine Learning*, 8(3-4):279–292, 1992.
  doi: 10.1007/BF00992698.
* Wu [2023]

  D Wu.
  Robust risk-aware option hedging.
  *Applied Financial Economics*, 2023.