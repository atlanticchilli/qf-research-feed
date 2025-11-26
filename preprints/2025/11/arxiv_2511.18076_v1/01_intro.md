---
authors:
- Fermat Leukam
- Rock Stephane Koffi
- Prudence Djagba
doc_id: arxiv:2511.18076v1
family_id: arxiv:2511.18076
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Reinforcement Learning for Portfolio Optimization with a Financial Goal and
  Defined Time Horizons
url_abs: http://arxiv.org/abs/2511.18076v1
url_html: https://arxiv.org/html/2511.18076v1
venue: arXiv q-fin
version: 1
year: 2025
---


Fermat Leukam
AIMS South Africa /Stellenbosch university, South Africa. 
  
Rock Stephane Koffi
 University of South Africa, South Africa
  
Prudence Djagba
 Michigan State University, USA

###### Abstract

This research proposes an enhancement to the innovative portfolio optimization approach using the G-Learning algorithm, combined with parametric optimization via the GIRL algorithm (G-learning approach to the setting of Inverse Reinforcement Learning) as presented by [dixon2020machine]. The goal is to maximize portfolio value by a target date while minimizing the investor’s periodic contributions. Our model operates in a highly volatile market with a well-diversified portfolio, ensuring a low-risk level for the investor, and leverages reinforcement learning to dynamically adjust portfolio positions over time. Results show that we improved the Sharpe Ratio from 0.42, as suggested by recent studies using the same approach, to a value of 0.483 a notable achievement in highly volatile markets with diversified portfolios. The comparison between G-Learning and GIRL reveals that while GIRL optimizes the reward function parameters (e.g., λ=0.0012\lambda=0.0012 compared to 0.002), its impact on portfolio performance remains marginal. This suggests that reinforcement learning methods, like G-Learning, already enable robust optimization. This research contributes to the growing development of reinforcement learning applications in financial decision-making, demonstrating that probabilistic learning algorithms can effectively align portfolio management strategies with investor needs.

Keywords: Portfolio optimization, Goal-based wealth management,Q-learning, G-Learning, GIRL, G-learner, Reinforcement learning, Dynamic cash flow management, Markov Decision Process (MDP), Benchmark portfolio,geometric Brownian motion (GBM),

## 1 Introduction

Portfolio optimization is a central challenge in finance, with the primary goal of identifying the optimal combination of assets to maximize returns for a given level of risk or minimize risk for a desired level of return. One of the earliest approaches proposed to address this challenge is the Modern Portfolio Theory (MPT), introduced by [markowitz1952modern]. Today, with the advent of artificial intelligence, increasingly effective solutions are emerging. The variant of this problem, which involves optimizing a portfolio to achieve a specific goal, has also gained attention. This problem is essential for both private and institutional investors as it determines their ability to meet specific financial objectives within a given time horizon.

Throughout our lives, we are required to meet financial goals at specific dates. Holding a portfolio that allows us to achieve these goals in a constantly changing financial environment characterized by unpredictable events such as economic crises or pandemics, without excessive effort, is highly relevant, both for individual investors and large organizations. Such disruptions highlight the need for dynamic and adaptive strategies. Therefore, efficient portfolio management is crucial, not only for wealth preservation but also for achieving long-term objectives, such as retirement planning or acquiring major assets.

The importance of this research lies in the need to improve traditional portfolio optimization methods and enhance the effectiveness of supervised learning models. Despite their influence, these methods present several limitations. In particular, the assumptions of normally distributed returns and independent variables often prove inadequate in real-world financial markets, which are marked by extreme volatility and unforeseen shocks. The evolution of reinforcement learning offers more flexible and effective solutions that can adapt to the complex dynamics of financial markets.

The work of Markowitz laid the foundation for portfolio management by introducing the concept of the efficient frontier [markowitz1952modern]. However, scholars like Benoît Mandelbrot and Nassim Nicholas Taleb have shown that financial markets often follow power laws, limiting the application of Markowitz’s approach [hubbard2020failure]. The rise of artificial intelligence has enabled the development of new solutions, with many relying on supervised learning methods [CFAinstitut]. However, a major limitation of these methods is their inability to adapt to external events that impact markets, such as financial crises or pandemics. The evolution of reinforcement learning offers more promising solutions to these challenges. Specifically, direct reinforcement algorithms such as Deep
Deterministic Policy Gradient (DDPG), Soft Actor-Critic (SAC), Proximal Policy Optimization (PPO), Actor-Critic(A2C), and Twin Delayed Deep Deterministic Policy Gradient(TD3) have shown encouraging results [hachaichi2024benchmarking]. Recent studies, such as those by [jiang2017deep], have introduced deep reinforcement learning (DRL), demonstrating its effectiveness in managing dynamic portfolios.

However, most existing research focuses on the formulation of classical problems, maximizing returns or minimizing risk, without considering investor-specific objectives at a given date [jin2016portfolio, jiang2017deep]. Goal-based wealth management has emerged as a more relevant approach, as demonstrated by the work of [browne2000stochastic] and [das2020dynamic]. This approach leverages Markov Decision Processes (MDP) to maximize the probability that the final portfolio value will exceed a target amount. G-Learning has already been applied to dynamic portfolio optimization in [halperin2018market], with further interesting extensions for problems involving cash flows developed in [dixon2020g].

This research aims to develop a dynamic portfolio optimization solution using G-Learning, a probabilistic extension of Q-learning. Unlike traditional and supervised learning approaches, our method takes into account both the evolution of regular contributions and the achievement of a specific goal by a given date. It also adapts to the high volatility and dynamic nature of financial markets. We apply this approach to a practical case: optimizing a portfolio intended to fund the purchase of a vehicle by a specific date, with regular contributions made over time.

The approach consists of:

* •

  Maximizing the portfolio value at the target date.
* •

  Minimizing the investor’s regular contributions throughout the investment period.

We hypothesize that the use of G-Learning can produce a more efficient investment strategy than traditional and supervised learning methods by maximizing returns and minimizing the financial effort required to achieve a goal by a specific date, with low-risk portfolios.

The structure of this report is as follows: In the first section, we will discuss the fundamental concepts related to portfolio optimization and reinforcement learning. Next, we will outline the approach for regularizing Q-learning and the development of the G-Learner and GIRL algorithms, followed by a data simulation. This will be followed by a presentation of the results obtained. Finally, we will provide a discussion and conclusion, along with some future perspectives.

## 2 Background

In this chapter, we will present the fundamental knowledge necessary for understanding the problem we aim to solve and the approach we will use.

### 2.1 Portfolio optimization

Modern Portfolio Theory (MPT) [markowitz1952modern], also known as mean-variance analysis, provides a mathematical approach to constructing a portfolio that aims to maximize returns for a given amount of risk. It builds on the principle of diversification, which suggests that holding a variety of asset types reduces overall risk compared to concentrating investments in a single category [cvitanic2001theory]. A core insight of MPT is that the value of an asset is not in its individual risk and return, but in how it influences the overall performance of the portfolio. This theory was first introduced by Harry Markowitz in his 1952 doctoral thesis, where he developed what is now known as the Markowitz mode.

Portfolio optimization is the process of selecting a combination of assets and determining their respective weights in a way that aligns with the investor’s objectives. This involves balancing the trade-off between risk and return to build a portfolio that maximizes expected returns while minimizing financial risks and other costs. As a multi-objective optimization problem, it seeks to identify the most efficient allocation of assets to achieve the desired performance [milhomem2020analysis].

In the following lines, we define a set of financial concepts that are essential for understanding and solving the portfolio optimization problem.

#### 2.1.1 Asset

An asset refers to any resource with economic value that a company, individual, or nation controls or owns, with the expectation that it will generate future benefits.

In numerous portfolio optimization scenarios, the focus is on financial instruments, such as equities, corporate and government bonds, along with various other forms of securities. A stock represents ownership in a company, with each unit referred to as a share. In contrast, bonds are generally considered lower-risk investments with more modest returns compared to stocks, making them a key component in diversified portfolios, particularly for conservative or older investors seeking stability.

#### 2.1.2 Returns

Before defining the return of a portfolio, it is necessary to understand what the return of an asset is.

Return or Realized Return refers to the profit or loss produced by an investment over a specific period, typically represented as a percentage of the original amount invested.

Here is the formula for calculating Return on Investment (ROI):

|  |  |  |
| --- | --- | --- |
|  | (ROI)=Gain from Investment−Cost of InvestmentCost of Investment.\text{ (ROI)}=\frac{\text{Gain from Investment}-\text{Cost of Investment}}{\text{Cost of Investment}}. |  |

Expected Return refers to the anticipated return on an investment based on historical data, statistical models, or forecasts. It represents the average return that an investor expects or estimates will be achieved in the future, considering the probability of various possible outcomes.

|  |  |  |
| --- | --- | --- |
|  | Expected Return=∑i=1npi×ri.\text{Expected Return}=\sum\_{i=1}^{n}p\_{i}\times r\_{i}. |  |

where:

* •

  pip\_{i} is the probability of it​hi^{th} outcome.
* •

  rir\_{i} denotes the return associated with the it​hi^{th} outcome.
* •

  nn indicates the total number of potential outcomes.

The Portfolio Return (RdR\_{d}) is the total return generated by a portfolio, determined by taking the weighted average of the returns of its individual assets. It reflects the overall performance an investor can anticipate from the combined holdings.

|  |  |  |
| --- | --- | --- |
|  | Rd:=∑a=1mwa​Ra.R\_{d}:=\sum\_{a=1}^{m}w\_{a}R\_{a}. |  |

where:

* •

  RdR\_{d} represents the overall return of the portfolio.
* •

  waw\_{a} signifies the proportion of the at​ha^{th} asset within the portfolio.
* •

  RaR\_{a} indicates the return of the at​ha^{th} asset.
* •

  mm denotes the total count of assets included in the portfolio.

#### 2.1.3 Risk

A widely accepted international definition of risk is the "impact of uncertainty on objectives." The interpretation of risk, along with the techniques for assessment and management, as well as its descriptions and definitions, can vary across different domains. In the financial sector, which is our focus, risk refers to the likelihood that the actual return on an investment will differ from what was anticipated. This encompasses not only "downside risk" (returns falling short of expectations, which may include the potential loss of part or all of the initial investment) but also "upside risk" (returns that exceed initial expectations) [sethi2013survey].

In finance, risk is commonly quantified using variance and standard deviation of returns. These measures help investors understand the volatility or variability in the returns of an investment or portfolio.

The variance of the portfolio return (σp2\sigma\_{p}^{2}) quantifies the spread of returns across the entire portfolio. This measure takes into account the variance of each individual asset as well as the covariance among various assets within the portfolio.

|  |  |  |
| --- | --- | --- |
|  | σp2=∑iwi2​σi2+∑i∑j≠iwi​wj​σi​σj​ρi​j.\sigma\_{p}^{2}=\sum\_{i}w\_{i}^{2}\sigma\_{i}^{2}+\sum\_{i}\sum\_{j\neq i}w\_{i}w\_{j}\sigma\_{i}\sigma\_{j}\rho\_{ij}. |  |

where:

* •

  σp2\sigma\_{p}^{2} represents the variance of the portfolio return.
* •

  wiw\_{i} signifies the proportion of asset ii within the portfolio.
* •

  σi2\sigma\_{i}^{2} denotes the variance of the return associated with asset ii.
* •

  σi\sigma\_{i} indicates the standard deviation of the return for asset ii.
* •

  ρi​j\rho\_{ij} represents the correlation coefficient between the returns of assets ii and jj.
* •

  The first term (∑iwi2​σi2\sum\_{i}w\_{i}^{2}\sigma\_{i}^{2}) reflects the variance of individual assets.
* •

  The second term (∑i∑j≠iwi​wj​σi​σj​ρi​j\sum\_{i}\sum\_{j\neq i}w\_{i}w\_{j}\sigma\_{i}\sigma\_{j}\rho\_{ij}) accounts for the covariance among different assets.

The standard deviation of the portfolio return (σp\sigma\_{p}) measures the portfolio’s overall volatility. It is simply the square root of the variance of the portfolio return.

#### 2.1.4 Diversification

Diversification is a risk management approach that involves combining different investments within a portfolio. A well-diversified portfolio includes a variety of asset classes and investment options to reduce reliance on any single asset or risk factor. The underlying principle of this strategy is that a portfolio made up of diverse assets will generally provide higher long-term returns while minimizing the risk associated with individual holdings or securities [manganelli2010finance].

#### 2.1.5 Sharpe Ratio

In finance, the Sharpe Ratio is a metric utilised to assess the performance of an investment, such as a securities or portfolio, by contrasting it with a risk-free asset, subsequent to risk adjustment. The Sharpe Ratio is calculated by subtracting the risk-free return from the investment returns and dividing the result by the standard deviation of the investment returns. This ratio signifies the excess return an investor obtains for the increased volatility associated with holding a riskier asset [gatfaoui2015estimating].

|  |  |  |
| --- | --- | --- |
|  | Sharpe Ratio=E​[Ra−Rf]σa.\text{Sharpe Ratio}=\frac{E[R\_{a}-R\_{f}]}{\sigma\_{a}}. |  |

where:

* •

  RaR\_{a} denotes the return on the asset.
* •

  RfR\_{f} represents the return from a risk-free investment.
* •

  E​[Ra−Rf]E[R\_{a}-R\_{f}] signifies the expected value of the asset’s excess return above the risk-free return.
* •

  σa\sigma\_{a} indicates the standard deviation of the asset’s excess return.

#### 2.1.6 Financial markets

A financial market is a venue or system dedicated to the exchange of assets [scott1976teaching]. These markets play an essential role in allocating funds to economic activities with the goal of maximizing returns. They encompass various trading environments such as the stock market, bond market, foreign exchange market, and derivatives market. Therefore, financial markets are fundamental to the smooth operation of capitalist economies.

These markets create financial products that generate returns for investors or lenders with surplus funds while providing borrowers access to the capital they need to finance their projects.

#### 2.1.7 Efficient frontier

Mathematical approaches to portfolio optimization rely on the concept of the Efficient Frontier  Fig. [1](https://arxiv.org/html/2511.18076v1#S2.F1 "Figure 1 ‣ 2.1.7 Efficient frontier ‣ 2.1 Portfolio optimization ‣ 2 Background ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") [beste2002markowitz], which is a hyperbolic curve representing the set of optimal portfolios formed from various combinations of assets. These portfolios are defined by two key principles: they either aim to minimize risk for a specific target return or seek to maximize returns for a predetermined level of risk [DissUMMTO]. Optimizing the portfolio within this framework, therefore, consists of selecting the portfolio on this frontier that meets the desired requirements.

![Refer to caption](images/Efficient_Frontier.png)


Figure 1: Visualization of the concept of the Efficient Frontier.

In approaches based on reinforcement learning, the goal is to define a reference portfolio. In our case, we will use the Benchmark portfolio.

#### 2.1.8 Benchmark portfolio

A benchmark portfolio is a model portfolio used as a point of comparison to evaluate the performance of an actual portfolio [maleyeff2003benchmarking]. It serves several essential functions:

* •

  Passive exposure: It acts as a template for investors seeking to passively track the performance of a specific market segment.
* •

  Performance evaluation: It measures the added value generated by active managers by comparing their results with those of the benchmark portfolio.

### 2.2 Reinforcement Learning

The first concepts that come to mind when discussing machine learning are supervised learning and unsupervised learning. Let’s first clarify the difference between these types of learning and reinforcement learning.

Supervised learning involves training an agent to produce an output based on a given input, using examples provided by a "teacher" in the form of input-output pairs. The agent’s goal is to generalize from these examples, meaning to find a function that generates the correct outputs from the corresponding inputs.

Unsupervised learning refers to a category of machine learning where algorithms are trained using data that lacks explicit labels or defined outcomes. The objective is for the model to autonomously discover hidden patterns, structures, or relationships within the dataset.

Reinforcement Learning (RL) is another form of machine learning in which an agent learns to make decisions through interactions with an environment to maximize a cumulative reward. The agent takes various actions, observes the outcomes, and modifies its behavior based on feedback (rewards or penalties) to enhance its performance over time [dixon2020machine]. From a mathematical perspective, this process can be framed as a problem of maximizing a specific objective function.

To understand the concept of reinforcement learning, it is essential to define the various elements involved in this concept and to present the different versions of this learning approach.

#### 2.2.1 Markov Decision Processes

Markov Decision Processes (MDPs) [markowitz1952modern] provide a mathematical framework for representing decision-making scenarios in which outcomes are influenced by both random factors and the actions of an agent. They build upon traditional Markov models by incorporating extra variables to capture the actions or controls implemented by the agent. Specifically, in the realm of reinforcement learning, MDPs are crucial as they establish a structure to model the interactions between an agent and its surrounding environment.

An MDP is characterized by a series of discrete time intervals t0,t1,…,tnt\_{0},t\_{1},\ldots,t\_{n} and a tuple (S,A,p,R,γ)(S,A,p,R,\gamma), where:

* •

  SS: Represents the collection of all potential states of the environment. At each time interval tt, the system resides in a specific state St∈SS\_{t}\in S. This collection can either be continuous or discrete.
* •

  AA: Set of possible actions that the agent can take. The choice of an action depends on the current state St=sS\_{t}=s. This set can also be discrete or continuous.
* •

  p​(s′|s,a)p(s^{\prime}|s,a): These are the transition probabilities, which indicate the likelihood of reaching a new state s′s^{\prime} from the current state ss after performing an action aa. This concept outlines how the environment changes in reaction to the actions taken by the agent.
* •

  RR: Reward function that assigns a value to the transition between states based on the action taken: R​(s,a,s′)R(s,a,s^{\prime}). It indicates the expected reward when the agent moves from ss to s′s^{\prime} after taking action aa.
* •

  γ\gamma: This is the discount factor, which is a value ranging from 0 to 1 that assesses the significance of future rewards in comparison to present rewards. A γ\gamma value approaching 1 places greater emphasis on future rewards, whereas a value nearing 0 prioritizes immediate rewards.

One of the important characteristics of Markov Decision Processes is that the conditional distribution of st+1s\_{t+1}, given the past (i.e., knowing (Sk)0≤k≤t\left(S\_{k}\right)\_{0\leq k\leq t}, depends only on sts\_{t}:

|  |  |  |
| --- | --- | --- |
|  | P(St+1=st+1∣S0=s0,S1=s1,…,St=st)=P(St+1=st+1∣St=st).P(S\_{t+1}=s\_{t+1}\mid S\_{0}=s\_{0},S\_{1}=s\_{1},\dots,S\_{t}=s\_{t})=P(S\_{t+1}=s\_{t+1}\mid S\_{t}=s\_{t}). |  |

The MDP approach provides a formal framework for the reinforcement learning process, modeling the dynamics of the environment and the outcomes of actions. Through algorithms such as Q-learning, MDPs enable the agent to estimate the value of different actions and improve its policy to maximize the expected reward.

#### 2.2.2 Elements of Reinforcement Learning

The use of reinforcement learning to address the portfolio optimization problem requires a specification of the reinforcement learning elements related to this issue, as illustrated in  Fig. [2](https://arxiv.org/html/2511.18076v1#S2.F2 "Figure 2 ‣ 2.2.2 Elements of Reinforcement Learning ‣ 2.2 Reinforcement Learning ‣ 2 Background ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") [li2024deep].

![Refer to caption](images/RL_Portfolio.png)


Figure 2: Emphasizing the elements of reinforcement learning for portfolio optimization.

Therefore, it is essential to define these key elements of reinforcement learning in order to better identify them within the context of our problem.The basic elements of reinforcement learning are: Environment, agent, policy, reward function, value function, and action-value function.

1. 1.

   Environment and Agent
   Reinforcement learning (RL) consists of two primary components: the environment and the agent. The environment refers to the setting in which the agent operates, while the agent is the entity that engages with the environment. RL environments possess several key features, including the state of the environment, the possible actions available to the agent, and the rewards received by the agent following any transition between states. The state encapsulates all relevant information about the environment at a specific moment. As the agent takes actions, the state of the environment changes, leading to a transition and the provision of a reward to the agent.
2. 2.

   Policy function

   A policy function πt​(St)\pi\_{t}(S\_{t}) outlines the actions an agent should take at time tt based on the current state StS\_{t} of the environment. This policy can either be deterministic, providing a specific action for each state, or it can represent a probability distribution over the available actions, depending on StS\_{t}.
3. 3.

   Reward function

   A reward function in reinforcement learning defines the goal of the agent by assigning a numerical reward signal based on the current state, action, or transition between states. It quantifies the immediate benefit or penalty of taking an action in a specific state, guiding the agent towards achieving its objectives.

   Mathematically, the reward function R​(s,a,s′)R(s,a,s^{\prime}) yields a reward rr for the transition from state ss to state s′s^{\prime} following action aa. Typically, the reward function can be influenced by the current state ss, the action aa, and the resulting state s′s^{\prime}. The agent aims to maximize its total rewards over time, making the reward function essential for guiding its learning and behavior.
4. 4.

   Value function

   The state-value function Vtπ​(s)V^{\pi}\_{t}(s) represents the anticipated discounted return when beginning from state ss, meaning St=sS\_{t}=s, and then consistently adhering to policy π\pi. In simpler terms, this function assesses the quality or desirability of being in a specific state
   [dixon2020machine].

   |  |  |  |
   | --- | --- | --- |
   |  | Vtπ​(s)=𝔼tπ​[∑i=0T−t−1γi​R​(St+i,at+i,St+i+1)∣St=s].V^{\pi}\_{t}(s)=\mathbb{E}^{\pi}\_{t}\left[\sum\_{i=0}^{T-t-1}\gamma^{i}R(S\_{t+i},a\_{t+i},S\_{t+i+1})\mid S\_{t}=s\right]. |  |

   In this context, R​(St+i,at+i,St+i+1)R(S\_{t+i},a\_{t+i},S\_{t+i+1}) denotes the reward obtained at time t+it+i. The variable TT signifies the planning horizon (with T=∞T=\infty indicating an infinite-horizon scenario). Additionally, 𝔼tπ[⋅∣St=s]\mathbb{E}^{\pi}\_{t}[\cdot\mid S\_{t}=s] indicates the conditional expectation across all potential future states, assuming actions are determined by policy π\pi. Finally, γ\gamma represents the discount factor, constrained within the range 0≤γ≤10\leq\gamma\leq 1.

   A simple transformation of this expression gives us the recurring formulation below, known as the Bellman equation, which is much more interesting in practice.

   |  |  |  |
   | --- | --- | --- |
   |  | Vtπ​(s)=𝔼π​[R​(s,at,St+1)+γ​Vt+1π​(St+1)|St=s].V^{\pi}\_{t}(s)=\mathbb{E}^{\pi}\left[R(s,a\_{t},S\_{t+1})+\gamma V^{\pi}\_{t+1}(S\_{t+1})\;\Big|\;S\_{t}=s\right]. |  |

   AndThe optimal value function Vt∗V\_{t}^{\*} signifies the maximum value for a given state across all potential policies, achieved when following the optimal policy π∗\pi^{\*} [dixon2020machine]:

   |  |  |  |
   | --- | --- | --- |
   |  | Vt∗​(s):=Vtπ∗​(s)=maxπ⁡Vtπ​(s),∀s∈S.V^{\*}\_{t}(s):=V^{\pi^{\*}}\_{t}(s)=\max\_{\pi}V^{\pi}\_{t}(s),\quad\forall s\in S. |  |
5. 5.

   Action-Value Function.
   The action-value function Q​(s,a)Q(s,a) (also known as Q-value) reflects the worth of executing a specific action in a given state. It evaluates the anticipated future rewards achievable by beginning in that state, performing the action, and subsequently adhering to an optimal policy[Reward].

   |  |  |  |
   | --- | --- | --- |
   |  | Qtπ​(s,a)=𝔼tπ​[∑i=0T−t−1γi​R​(St+i,at+i,St+i+1)∣St=s,At=a].Q^{\pi}\_{t}(s,a)=\mathbb{E}^{\pi}\_{t}\left[\sum\_{i=0}^{T-t-1}\gamma^{i}R\left(S\_{t+i},a\_{t+i},S\_{t+i+1}\right)\mid S\_{t}=s,A\_{t}=a\right]. |  |

   Its optimal Bellman expression in relation to the value function is given by:

   |  |  |  |
   | --- | --- | --- |
   |  | Qt∗​(s,a)=𝔼t∗​[Rt​(s,a,s′)]+γ​𝔼t∗​[Vt+1∗​(s′)].Q^{\*}\_{t}(s,a)=\mathbb{E}^{\*}\_{t}\left[R\_{t}(s,a,s^{\prime})\right]+\gamma\,\mathbb{E}^{\*}\_{t}\left[V^{\*}\_{t+1}(s^{\prime})\right]. |  |

   This concept plays a crucial role in reinforcement learning, particularly within Q-learning. It facilitates the creation of the Q-table a lookup table where each entry predicts the total reward accrued by taking a specific action in a particular state and subsequently adhering to the optimal strategy.

#### 2.2.3 Q-learning

Before presenting Q-learning, which will be the focus of our study later, let’s first introduce the taxonomy of reinforcement learning methods  Fig. [3](https://arxiv.org/html/2511.18076v1#S2.F3 "Figure 3 ‣ 2.2.3 Q-learning ‣ 2.2 Reinforcement Learning ‣ 2 Background ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") [salvador2021my]. These methods are divided into two main families.
On one hand, we have Model-Free methods, where the agent learns to make decisions solely based on its direct experiences with the environment. On the other hand, Model-Based methods rely on the agent’s ability to learn or have access to a model of the environment, which can predict state transitions and rewards.
These two families are further divided into subcategories. The first distinction is based on the availability of the model: the agent either learns the model from experience or has the model provided. The second distinction concerns the availability of the policy, with methods focusing either on policy optimization or Q-learning.These different subfamilies include very recent and widely used algorithms in reinforcement learning.

![Refer to caption](images/RL-Taxonomy-created-by-openAI.png)


Figure 3: Taxonomy of RL models.

Q-learning is a reinforcement learning technique designed to discover the best action-selection strategy for a finite Markov decision process (MDP). It enables an agent to optimize cumulative rewards by interacting with the environment repeatedly, even in cases where the underlying dynamics of the environment remain unknown [salvador2021my].This is a very popular algorithm in reinforcement learning, proposed by [watkins1992q]. Before explaining how it works, let’s start by recalling the two groups of learning methods, depending on policy. These are the on-policy and off-policy algorithms.

On-policy algorithms operate under the assumption that the policy generating the data for learning is already optimal, aiming to derive the best policy function from that dataset. Conversely, off-policy algorithms do not require the data-generating policy to be optimal; it can even be sub-optimal or random. The goal of off-policy methods is to identify an optimal policy using data collected under a different, potentially non-ideal, policy.

Q-learning is therefore an off-policy reinforcement learning algorithm, so the data is used to update the Q-table in order to determine the policy.Let us recall that the dataset is a set of trajectories comprising tuples (st,at,Rt,st+1)(s\_{t},a\_{t},R\_{t},s\_{t+1}) that have been collected through the observation of an agent in the environment we want to study, or in a similar environment, under a set of various policies.
It works as follows:

### a. Learning and Updating Q-values

The algorithm stores a table of Q-values corresponding to each state-action pair. These Q-values indicate the anticipated utility of executing a specific action within a particular state, followed by adherence to the optimal policy. Initially, the Q-values are assigned arbitrary values and are progressively refined through iterative updates based on the agent’s accumulated experiences.

### b. Q-value Update Rule

The Q-values are refined through the following equation:

|  |  |  |
| --- | --- | --- |
|  | Q​(s,a)←Q​(s,a)+α​[r+γ​maxa′⁡Q​(s′,a′)−Q​(s,a)].Q(s,a)\leftarrow Q(s,a)+\alpha\left[r+\gamma\max\_{a^{\prime}}Q(s^{\prime},a^{\prime})-Q(s,a)\right]. |  |

Where:

* •

  a′a^{\prime} denotes a potential action from the next state s′s^{\prime}.
* •

  α\alpha is the learning rate, with 0<α≤10<\alpha\leq 1.

### c. Policy Derivation

The policy defines the action to execute in each state and is guided by the Q-values. In most cases, it selects the action with the highest Q-value for a given state (exploitation). However, to encourage exploration, it may occasionally opt for a suboptimal action.

### d. Exploration vs. Exploitation

Q-learning balances the need to explore new strategies with the goal of exploiting known ones. This trade-off is typically handled through techniques like the epsilon-greedy strategy, where the agent primarily selects the most favorable action based on prior experience but occasionally opts for a random action to uncover alternative solutions.

### e. Convergence

Given specific conditions, such as guaranteeing that every state action pair is explored infinitely, Q-learning will eventually converge toward the optimal policy and the corresponding Q values, yielding the highest expected reward for each state, regardless of the circumstances.

## 3 Methods

In this chapter, we will present the reinforcement learning method for portfolio optimization proposed by [dixon2020g], where they develop two algorithms, G-Learner and GIRL, derived from an entropy regularization of Q-learning method.

### 3.1 G-learning: Mathematical Foundations and Algorithms

G-Learning is an extension of Q-learning, tailored to complex financial environments. Models a sequential decision-making process in which an agent must make choices at each time step to optimize a long-term objective, such as maximizing portfolio wealth.

#### 3.1.1 Mathematical Approach of G-learning and its Algorithms G-learner and GIRL

We will demonstrate here, from a mathematical point of view, how G-learning is established through regularization of the Q-learning method. We will also explain the construction of the G-learner and GIRL algorithms.

### a. Regularization of Q-learning.

The objective of Reinforcement Learning (RL) is to address the Bellman optimality equation using data samples.

In the context of Q- learning, we pose Vt∗​(s)=maxa⁡Qt∗​(s,a)V^{\*}\_{t}(s)=\max\_{a}Q^{\*}\_{t}(s,a) and πt∗​(at∣xt)=arg⁡maxat⁡Qt∗​(xt,at)\pi^{\*}\_{t}(a\_{t}\mid x\_{t})=\arg\max\_{a\_{t}}Q^{\*}\_{t}(x\_{t},a\_{t})
However, in the context of G-learning, which is a probabilistic extension of Q-learning, it is necessary to regularize the Q function to obtain the expression of the action value function to be used. We will call this function G in what follows.

We begin by rewriting Bellman’s optimality equation for the value function.

Let P={π:π≥0; 1T​π=1}P=\{\pi:\pi\geq 0;\ \mathbf{1}^{T}\pi=1\}, which is a Fenchel-type representation of Vt∗V^{\*}\_{t}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∗​(xt)=maxπ(.|y)∈P​∑at∈Atπ​(at|xt)​[Rt∗​(xt,at)+γ​𝔼t,at​[Vt+1​(xt+1)]].V^{\*}\_{t}(x\_{t})=\max\_{\pi(.|y)\in P}\sum\_{a\_{t}\in A\_{t}}\pi(a\_{t}|x\_{t})\left[R^{\*}\_{t}(x\_{t},a\_{t})+\gamma\mathbb{E}\_{t,a\_{t}}\left[V\_{t+1}(x\_{t+1})\right]\right]. |  | (1) |

In fact, this follows from the fact that maxi∈{1,…,n}⁡xi=maxπ≥0;‖π‖1≤1⁡πT​x\max\_{i\in\{1,\dots,n\}}x\_{i}=\max\_{\pi\geq 0;\|\pi\|\_{1}\leq 1}\pi^{T}x.
Now, let us use regularized entropy to construct our G function from this expression. For simplicity, we will represent the expectation.
𝔼xt+1|xt,at​[⋅]\mathbb{E}\_{x\_{t+1}|x\_{t},a\_{t}}[\cdot]
as 𝔼t,a​[⋅]\mathbb{E}\_{t,a}[\cdot] in the following.

This new formulation of the value function is more interesting for the rest of our work. We also need to define the following concepts:

* •

  One-step information cost measures how much the learned policy π​(at|xt)\pi(a\_{t}|x\_{t}) differs from a reference policy π0​(at|xt)\pi\_{0}(a\_{t}|x\_{t}) for a given state xtx\_{t} and action ata\_{t}. It is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | gπ​(xt,at):=log⁡π​(at|xt)π0​(at|xt).g^{\pi}(x\_{t},a\_{t}):=\log\frac{\pi(a\_{t}|x\_{t})}{\pi\_{0}(a\_{t}|x\_{t})}. |  | (2) |
* •

  Expected information cost is the average of the one-step information cost over all possible actions, weighted by the probability of those actions under the learned policy. Mathematically, this is the Kullback-Leibler (KL) divergence between the learned policy π​(at|xt)\pi(a\_{t}|x\_{t}) and the reference policy π0​(at|xt)\pi\_{0}(a\_{t}|x\_{t}):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼π[gπ(xt,at)|xt]=KL[π||π0](xt):=∑atπ(at|xt)logπ​(at|xt)π0​(at|xt).\mathbb{E}\_{\pi}[g^{\pi}(x\_{t},a\_{t})|x\_{t}]=\text{KL}[\pi||\pi\_{0}](x\_{t}):=\sum\_{a\_{t}}\pi(a\_{t}|x\_{t})\log\frac{\pi(a\_{t}|x\_{t})}{\pi\_{0}(a\_{t}|x\_{t})}. |  | (3) |
* •

  Total discounted information cost is the cumulative information cost over a series of actions (trajectory) from time step tt to the terminal time step TT. It is discounted by a factor γ∈[0,1]\gamma\in[0,1], where future costs are valued less than immediate ones:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Iπ​(xt):=∑t′=tTγt′−t​𝔼tπ​[gπ​(xt′,at′)|xt].I^{\pi}(x\_{t}):=\sum\_{t^{\prime}=t}^{T}\gamma^{t^{\prime}-t}\mathbb{E}^{\pi}\_{t}\left[g^{\pi}(x\_{t^{\prime}},a\_{t^{\prime}})|x\_{t}\right]. |  | (4) |
* •

  Free energy function combines the standard value function Vtπ​(xt)V\_{t}^{\pi}(x\_{t}) with a penalty for the total discounted information cost Iπ​(xt)I^{\pi}(x\_{t}), weighted by a regularization parameter 1β\frac{1}{\beta}. This regularization ensures that the learned policy remains close to the reference policy while optimizing rewards. The free energy function is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Ftπ​(xt):=Vtπ​(xt)−1β​Iπ​(xt).F\_{t}^{\pi}(x\_{t}):=V\_{t}^{\pi}(x\_{t})-\frac{1}{\beta}I^{\pi}(x\_{t}). |  | (5) |

  Using the expression for Vtπ​(xt)V\_{t}^{\pi}(x\_{t}) and relation Eq. ([5](https://arxiv.org/html/2511.18076v1#S3.E5 "Equation 5 ‣ 4th item ‣ a. Regularization of Q-learning. ‣ 3 Methods ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons"))
  this can be expanded as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Ftπ​(xt)=∑t′=tTγt′−t​𝔼π​[Rt′​(xt′,at′)−1β​gπ​(xt′,at′)].F\_{t}^{\pi}(x\_{t})=\sum\_{t^{\prime}=t}^{T}\gamma^{t^{\prime}-t}\mathbb{E}\_{\pi}\left[R\_{t^{\prime}}(x\_{t^{\prime}},a\_{t^{\prime}})-\frac{1}{\beta}g^{\pi}(x\_{t^{\prime}},a\_{t^{\prime}})\right]. |  | (6) |

  Here, β\beta controls the trade-off between optimizing rewards (through Vtπ​(xt)V\_{t}^{\pi}(x\_{t})) and minimizing the divergence from the reference policy (through Iπ​(xt)I^{\pi}(x\_{t})).

The free energy Ftπ​(xt)F\_{t}^{\pi}(x\_{t}) is thus the value function regularized by entropy. It replaces the value function in the G-learning approach

Its Bellman equation is given by :

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ftπ​(xt)=𝔼at|xt​[R^t​(xt,at)−1β​gπ​(xt,at)+γ​𝔼t,a​[Ft+1π​(xt+1)]].F\_{t}^{\pi}(x\_{t})=\mathbb{E}\_{a\_{t}|x\_{t}}\left[\hat{R}\_{t}(x\_{t},a\_{t})-\frac{1}{\beta}g^{\pi}(x\_{t},a\_{t})+\gamma\mathbb{E}\_{t,a}\left[F\_{t+1}^{\pi}(x\_{t+1})\right]\right]. |  | (7) |

In the same way as the value action function is defined in the Q-learning approach, we define our state action free energy function as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gtπ​(xt,at)=R^t​(xt,at)+γ​𝔼​[Ft+1π​(xt+1)∣xt,at].G\_{t}^{\pi}(x\_{t},a\_{t})=\hat{R}\_{t}(x\_{t},a\_{t})+\gamma\mathbb{E}\left[F\_{t+1}^{\pi}(x\_{t+1})\mid x\_{t},a\_{t}\right]. |  | (8) |

By substituting Ft+1π​(xt+1)F\_{t+1}^{\pi}(x\_{t+1}) with its value from Eq. ([6](https://arxiv.org/html/2511.18076v1#S3.E6 "Equation 6 ‣ 4th item ‣ a. Regularization of Q-learning. ‣ 3 Methods ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons")), we obtain:

|  |  |  |
| --- | --- | --- |
|  | Gtπ​(xt,at)=R^t​(xt,at)+γ​𝔼t,a​[∑t′=t+1Tγt′−t−1​(R^t′​(xt′,at′)−1β​gπ​(xt′,at′))].G\_{t}^{\pi}(x\_{t},a\_{t})=\hat{R}\_{t}(x\_{t},a\_{t})+\gamma\mathbb{E}\_{t,a}\left[\sum\_{t^{\prime}=t+1}^{T}\gamma^{t^{\prime}-t-1}\left(\hat{R}\_{t^{\prime}}(x\_{t^{\prime}},a\_{t^{\prime}})-\frac{1}{\beta}g^{\pi}(x\_{t^{\prime}},a\_{t^{\prime}})\right)\right]. |  |

Defining our optimal policy as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(at|xt)=π0​(at|xt)​eβ​(Gtπ​(xt,at)−Ftπ​(xt)).\pi(a\_{t}|x\_{t})=\pi\_{0}(a\_{t}|x\_{t})e^{\beta(G\_{t}^{\pi}(x\_{t},a\_{t})-F\_{t}^{\pi}(x\_{t}))}. |  | (9) |

we obtain the following expression for GG:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gtπ​(x;a)=R^​(xt;at)+𝔼t,a​[γβ​log⁡(∑at+1π0​(at+1|xt+1)​eβ​Gt+1π​(xt+1;at+1))].G\_{t}^{\pi}\left(x;a\right)=\hat{R}\left(x\_{t};a\_{t}\right)+\mathbb{E}\_{t,a}\left[\frac{\gamma}{\beta}\log\left(\sum\_{a\_{t+1}}\pi\_{0}\left(a\_{t+1}|x\_{t+1}\right)e^{\beta G\_{t+1}^{\pi}\left(x\_{t+1};a\_{t+1}\right)}\right)\right]. |  | (10) |

At this level, we need to determine the expression of the reward function R^t​(xt,at)\hat{R}\_{t}(x\_{t},a\_{t}) for our example of portfolio optimization for the purchase of a car on a fixed date. So that we can use GG in the sequel to determine our optimal policy.

### b. Construction of the reward function

We consider a discrete-time framework comprising TT steps, where TT represents the time horizon as an integer. The investor or planner manages wealth across NN assets, with xtx\_{t} indicating the vector of dollar values assigned to various assets at time tt, and utu\_{t} representing the vector of alterations in these positions.

Additionally, we assume that the first asset, identified as n=1n=1, is a risk-free bond, while the remaining assets carry risk with uncertain returns rtr\_{t}, whose expected values are denoted as r¯t\bar{r}\_{t}. The returns’ covariance matrix is Σr\Sigma\_{r}, which has dimensions of (N−1)×(N−1)(N-1)\times(N-1).

Let ctc\_{t} represent the cash contribution made to the plan at time tt. Consequently, the combination (ct,ut)(c\_{t},u\_{t}) can be viewed as the action variables in a dynamic optimization problem related to our problem.

Furthermore, we assume that at each time step tt, a predetermined target value P^t+1\hat{P}\_{t+1} exists for the portfolio at the subsequent time t+1t+1.

Let us emphasize again what the optimization task consists of in our problem.

* •

  Minimize the contributions required to achieve a certain objective on a given date, while ensuring that the portfolio generates sufficient returns.
* •

  Maximize the future value of the portfolio by optimally allocating contributions among different assets, taking into account transaction costs and the risks associated with these choices.

To achieve this objective, our reward function will aim to penalize situations where the agent injects capital ctc\_{t} into the portfolio. Additionally, it will set a very high target value P^t+1\hat{P}\_{t+1} and penalize situations where this target value P^t+1\hat{P}\_{t+1} at step tt exceeds the value at the next step Vt+1=(1+rt)​(xt+ut)V\_{t+1}=(1+r\_{t})(x\_{t}+u\_{t}) of the portfolio (penalty for underperformance relative to this objective).

More formally, we have:

1. 1.

   −ct-c\_{t}: The cost of the contribution.

   This term represents the cost of the cash contribution you make at the beginning of the period. The more you contribute, the higher this cost, which reduces the reward.However, this contribution is necessary to accumulate the capital needed to achieve the objective.
2. 2.

   −λ​𝔼t​[(P^t+1−(1+rt)​(xt+ut))+]-\lambda\mathbb{E}\_{t}\left[(\hat{P}\_{t+1}-(1+r\_{t})(x\_{t}+u\_{t}))\_{+}\right]: Penalty for underperformance.

   This term penalizes the gap between the actual performance of the portfolio and the target value set for the next period. If the actual value of the portfolio at the end of the period Vt+1=(1+rt)​(xt+ut)V\_{t+1}=(1+r\_{t})(x\_{t}+u\_{t}) is lower than the target P^t+1\hat{P}\_{t+1}, you receive a penalty proportional to this gap.
3. 3.

   −utT​Ω​ut-u\_{t}^{T}\Omega u\_{t}: Transaction costs.

   This term corresponds to the cost of transactions. Each change in the positions in the portfolio utu\_{t} (buying or selling assets) incurs costs, such as brokerage fees or costs of adjusting the portfolio. Ω\Omega is a weighting matrix that controls the magnitude of the costs according to the size and type of transactions.

This gives us the following reward function.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt​(xt,ut,ct)=−ct−λ​𝔼t​[(P^t+1−(1+rt)​(xt+ut))+]−utT​Ω​ut.R\_{t}\left(x\_{t},u\_{t},c\_{t}\right)=-c\_{t}-\lambda\mathbb{E}\_{t}\left[(\hat{P}\_{t+1}-(1+r\_{t})(x\_{t}+u\_{t}))\_{+}\right]-u\_{t}^{T}\Omega u\_{t}. |  | (11) |

However, this function lacks analytical significance because of the rectified non-linearity (⋅)+:=max⁡(⋅,0)(\cdot)\_{+}:=\max(\cdot,0) within the expectation. We also have the following relation between the variation vector of these positions utu\_{t} and the cash contribution ctc\_{t} at time tt:

|  |  |  |
| --- | --- | --- |
|  | ∑n=1Nut​n=ct;\sum\_{n=1}^{N}u\_{tn}=c\_{t}; |  |

So we modify the reward in two ways and we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt​(xt,ut)=−∑n=1Nut​n−λ​𝔼t​[(P^t+1−(1+rt)​(xt+ut))2]−utT​Ω​ut.R\_{t}\left(x\_{t},u\_{t}\right)=-\sum\_{n=1}^{N}u\_{tn}-\lambda\mathbb{E}\_{t}\left[(\hat{P}\_{t+1}-(1+r\_{t})(x\_{t}+u\_{t}))^{2}\right]-u\_{t}^{T}\Omega u\_{t}. |  | (12) |

The squaring of the expression (P^t+1−(1+rt)​(xt+ut))2\left(\hat{P}\_{t+1}-(1+r\_{t})(x\_{t}+u\_{t})\right)^{2} introduces a symmetry that penalizes both cases where Vt+1≫P^t+1V\_{t+1}\gg\hat{P}\_{t+1} and those where Vt+1≪P^t+1V\_{t+1}\ll\hat{P}\_{t+1}. In reality, our goal is to penalize only the latter scenarios. To address this concern, we can choose target values P^t+1\hat{P}\_{t+1} that are substantially higher than the expected portfolio value at time tt for the upcoming period. Consequently, we construct this target following the methodology suggested by [Reward], wherein they describe P^t+1\hat{P}\_{t+1} as a linear combination of a benchmark BtB\_{t} that is independent of the portfolio and a proportional increase in the current portfolio η​1T​xt\eta 1^{T}x\_{t}. Here, η\eta represents the desired growth rate, and 1T​xt1^{T}x\_{t} signifies the present portfolio value. Therefore, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P^t+1=(1−ρ)​Bt+ρ​η​1T​xt,\hat{P}\_{t+1}=(1-\rho)B\_{t}+\rho\eta 1^{T}x\_{t}, |  | (13) |

Where ρ\rho is a parameter between 0 and 1, which controls the relative importance of the benchmark component (portfolio-independent) and the portfolio-dependent component.

By representing the asset returns as rt=r¯t+ϵ~tr\_{t}=\bar{r}\_{t}+\tilde{\epsilon}\_{t}, where the initial component r¯0​(t)=rf\bar{r}\_{0}(t)=r\_{f} denotes the risk-free rate (given that the first asset is risk-free), and ϵ~t=(0,ϵt)\tilde{\epsilon}\_{t}=(0,\epsilon\_{t}), with ϵt\epsilon\_{t} being an idiosyncratic noise, we can substitute Eq. ([13](https://arxiv.org/html/2511.18076v1#S3.E13 "Equation 13 ‣ b. Construction of the reward function ‣ 3 Methods ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons")) into Eq. ([12](https://arxiv.org/html/2511.18076v1#S3.E12 "Equation 12 ‣ b. Construction of the reward function ‣ 3 Methods ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons")) and expand it to derive the following expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt​(xt,ut)\displaystyle R\_{t}(x\_{t},u\_{t}) | =−λ​P^t+12−utT​1+2​λ​P^t+1​(xt+ut)T​(1+r¯t)−λ​(xt+ut)T​Σ^t​(xt+ut)−utT​Ω​ut\displaystyle=-\lambda\hat{P}^{2}\_{t+1}-u\_{t}^{T}1+2\lambda\hat{P}\_{t+1}(x\_{t}+u\_{t})^{T}(1+\bar{r}\_{t})-\lambda(x\_{t}+u\_{t})^{T}\hat{\Sigma}\_{t}(x\_{t}+u\_{t})-u\_{t}^{T}\Omega u\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =xtT​Rt(x​x)​xt+utT​Rt(u​x)​xt+utT​Rt(u​u)​ut+xtT​Rt(x)+utT​Rt(u)+Rt(0).\displaystyle=x\_{t}^{T}R^{(xx)}\_{t}x\_{t}+u\_{t}^{T}R^{(ux)}\_{t}x\_{t}+u\_{t}^{T}R^{(uu)}\_{t}u\_{t}+x\_{t}^{T}R^{(x)}\_{t}+u\_{t}^{T}R^{(u)}\_{t}+R^{(0)}\_{t}. |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ^t\displaystyle\hat{\Sigma}\_{t} | =(000Σr)+(1+r¯t)​(1+r¯t)T\displaystyle=\begin{pmatrix}0&0\\ 0&\Sigma\_{r}\end{pmatrix}+(1+\bar{r}\_{t})(1+\bar{r}\_{t})^{T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt(x​x)\displaystyle R^{(xx)}\_{t} | =−λ​η2​ρ2​11T+2​λ​η​ρ​(1+r¯t)​1T−λ​Σ^t\displaystyle=-\lambda\eta^{2}\rho^{2}1^{T}+2\lambda\eta\rho(1+\bar{r}\_{t})1^{T}-\lambda\hat{\Sigma}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt(u​x)\displaystyle R^{(ux)}\_{t} | =2​λ​η​ρ​(1+r¯t)​1T−2​λ​Σ^t\displaystyle=2\lambda\eta\rho(1+\bar{r}\_{t})1^{T}-2\lambda\hat{\Sigma}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt(u​u)\displaystyle R^{(uu)}\_{t} | =−λ​Σ^t−Ω\displaystyle=-\lambda\hat{\Sigma}\_{t}-\Omega |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt(x)\displaystyle R^{(x)}\_{t} | =−2​λ​η​ρ​(1−ρ)​Bt​1+2​λ​(1−ρ)​Bt​(1+r¯t)\displaystyle=-2\lambda\eta\rho(1-\rho)B\_{t}1+2\lambda(1-\rho)B\_{t}(1+\bar{r}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt(u)\displaystyle R^{(u)}\_{t} | =−1+2​λ​(1−ρ)​Bt​(1+r¯t)\displaystyle=-1+2\lambda(1-\rho)B\_{t}(1+\bar{r}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt(0)\displaystyle R^{(0)}\_{t} | =−(1−ρ)2​λ​Bt2.\displaystyle=-(1-\rho)^{2}\lambda B\_{t}^{2}. |  |

If we consider the expected returns r¯t\bar{r}\_{t}, the covariance matrix Σr\Sigma\_{r}, and the benchmark BtB\_{t} as constant, the vector of free parameters that characterize the reward function can be expressed as θ:=(λ,η,ρ,Ω)\theta:=(\lambda,\eta,\rho,\Omega).

At this stage, our objective is to determine the optimal policy. The G-learner algorithm, whose mathematical approach is described below, uses the previously defined functions FF and GG to achieve this goal.

### c. Optimal Policy Determination: G-learner

G-learner is an algorithm proposed by [dixon2020machine] for optimal policy determination in G-learning. In this section, we describe the steps of this algorithm.

In order to facilitate the exploitation of the free energy function FtπF^{\pi}\_{t}, it is necessary to transform it into a quadratic functional form. This transformation is made possible by the quadratic nature of the reward function. Thus, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ftπ​(xt)=xtT​Ft(x​x)​xt+xtT​Ft(x)+Ft(0),F^{\pi}\_{t}(x\_{t})=x\_{t}^{T}F^{(xx)}\_{t}x\_{t}+x\_{t}^{T}F^{(x)}\_{t}+F^{(0)}\_{t}, |  | (14) |

where Ft(x​x)F^{(xx)}\_{t}, Ft(x)F^{(x)}\_{t}, and Ft(0)F^{(0)}\_{t} are parameters that can depend on time via their dependence on the target values P^t+1\hat{P}\_{t+1} and the expected returns r¯t\bar{r}\_{t}.

To determine the coefficients of this expression, we also transform the G function into a quadratic form as follows:

|  |  |  |
| --- | --- | --- |
|  | Gtπ​(xt,ut)=xt⊤​Qt(x​x)​xt+ut⊤​Qt(u​x)​xt+ut⊤​Qt(u​u)​ut+xt⊤​Qt(x)+ut⊤​Qt(u)+Qt(0).G\_{t}^{\pi}(x\_{t},u\_{t})=x\_{t}^{\top}Q\_{t}^{(xx)}x\_{t}+u\_{t}^{\top}Q\_{t}^{(ux)}x\_{t}+u\_{t}^{\top}Q\_{t}^{(uu)}u\_{t}+x\_{t}^{\top}Q\_{t}^{(x)}+u\_{t}^{\top}Q\_{t}^{(u)}+Q\_{t}^{(0)}. |  |

Here, Qt(x​x)Q\_{t}^{(xx)}, Qt(u​x)Q\_{t}^{(ux)},Qt(u​u)Q\_{t}^{(uu)},Qt(x)Q\_{t}^{(x)},Qt(u)Q\_{t}^{(u)}, and Qt(0)Q\_{t}^{(0)} are easily determined by expanding the equation Eq. ([10](https://arxiv.org/html/2511.18076v1#S3.E10 "Equation 10 ‣ a. Regularization of Q-learning. ‣ 3 Methods ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons")).

We also assume that the reference policy π0\pi\_{0} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π0​(ut∣xt)=1(2π)n|Σp|​e−12​(ut−u^t)⊤​Σp−1​(ut−u^t),\pi\_{0}(u\_{t}\mid x\_{t})=\frac{1}{\sqrt{(2\pi)^{n}\lvert\Sigma\_{p}\lvert}}e^{-\frac{1}{2}(u\_{t}-\hat{u}\_{t})^{\top}\Sigma\_{p}^{-1}(u\_{t}-\hat{u}\_{t})}, |  | (15) |

where u^t\hat{u}\_{t} is an adjusted mean as follows:
u^t=u¯t+v¯t​xt\hat{u}\_{t}=\bar{u}\_{t}+\bar{v}\_{t}x\_{t}
These elements allow us to obtain the following coefficients for the function FtπF^{\pi}\_{t}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft(x​x)\displaystyle F\_{t}^{(xx)} | =Qt(x​x)+12​β​(Ut⊤​Σp−1​Ut−v¯t⊤​Σp−1​v¯t)\displaystyle=Q\_{t}^{(xx)}+\frac{1}{2\beta}\left(U\_{t}^{\top}\Sigma\_{p}^{-1}U\_{t}-\bar{v}\_{t}^{\top}\Sigma\_{p}^{-1}\bar{v}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft(x)\displaystyle F\_{t}^{(x)} | =Qt(x)+1β​(Ut⊤​Σp−1​Wt−v¯t⊤​Σp−1​u¯t)\displaystyle=Q\_{t}^{(x)}+\frac{1}{\beta}\left(U\_{t}^{\top}\Sigma\_{p}^{-1}W\_{t}-\bar{v}\_{t}^{\top}\Sigma\_{p}^{-1}\bar{u}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft​(0)\displaystyle F\_{t}(0) | =Qt​(0)+12​β​(Wt⊤​Σp−1​Wt−u¯t⊤​Σp−1​u¯t)−12​β​log⁡|Σp|+log⁡|Σ¯p|.\displaystyle=Q\_{t}(0)+\frac{1}{2\beta}\left(W\_{t}^{\top}\Sigma\_{p}^{-1}W\_{t}-\bar{u}\_{t}^{\top}\Sigma\_{p}^{-1}\bar{u}\_{t}\right)-\frac{1}{2\beta}\log|\Sigma\_{p}|+\log|\bar{\Sigma}\_{p}|. |  |

where we use the auxiliary parameters:

|  |  |  |
| --- | --- | --- |
|  | Ut=β​Qt(u​x)+Σp−1​v¯t​Wt=β​Qt(u)+Σp−1​u¯t​Σ¯p=Σp−1−2​β​Qt(u​u).\displaystyle U\_{t}=\beta Q\_{t}^{(ux)}+\Sigma\_{p}^{-1}\bar{v}\_{t}W\_{t}=\beta Q\_{t}^{(u)}+\Sigma\_{p}^{-1}\bar{u}\_{t}\bar{\Sigma}\_{p}=\Sigma\_{p}^{-1}-2\beta Q\_{t}^{(uu)}. |  |

The optimal policy for the given step is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(ut|xt)=π0​(ut|xt)​eβ​(Gtπ​(xt,ut)−Ftπ​(xt)).\pi(u\_{t}|x\_{t})=\pi\_{0}(u\_{t}|x\_{t})e^{\beta\left(G^{\pi}\_{t}(x\_{t},u\_{t})-F^{\pi}\_{t}(x\_{t})\right)}. |  | (16) |

By substituting π0​(ut|xt)\pi\_{0}(u\_{t}|x\_{t}) and Gtπ​(xt,ut)G^{\pi}\_{t}(x\_{t},u\_{t}) into this expression, we obtain:

|  |  |  |
| --- | --- | --- |
|  | π​(ut|xt)=1(2​π)n/2​|Σ~p|1/2​e−12​(ut−u~t−v~t​xt)⊤​Σ~p−1​(ut−u~t−v~t​xt).\pi(u\_{t}|x\_{t})=\frac{1}{(2\pi)^{n/2}|\tilde{\Sigma}\_{p}|^{1/2}}e^{-\frac{1}{2}(u\_{t}-\tilde{u}\_{t}-\tilde{v}\_{t}x\_{t})^{\top}\tilde{\Sigma}\_{p}^{-1}(u\_{t}-\tilde{u}\_{t}-\tilde{v}\_{t}x\_{t})}. |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ~p−1\displaystyle\tilde{\Sigma}\_{p}^{-1} | =Σp−1−2​β​Qu​u,t\displaystyle=\Sigma\_{p}^{-1}-2\beta Q\_{uu,t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u~t\displaystyle\tilde{u}\_{t} | =Σ~p​(Σp−1​u¯t+β​Qu,t)\displaystyle=\tilde{\Sigma}\_{p}(\Sigma\_{p}^{-1}\bar{u}\_{t}+\beta Q\_{u,t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | v~t\displaystyle\tilde{v}\_{t} | =Σ~p​(Σp−1​v¯t+β​Qu​x,t).\displaystyle=\tilde{\Sigma}\_{p}(\Sigma\_{p}^{-1}\bar{v}\_{t}+\beta Q\_{ux,t}). |  |

The process necessary for learning GG in this context includes determining the optimal liquidity contribution at each step while adhering to the budget constraint. Given that the learning GG generates Gaussian actions utu\_{t}, the optimal contribution at time tt, denoted as ctc\_{t}, is expected to follow a Gaussian distribution with a mean of c¯t=1⊤​(u¯t+v¯t​xt)\bar{c}\_{t}=1^{\top}(\bar{u}\_{t}+\bar{v}\_{t}x\_{t}). Thus, the expected optimal contribution c¯t\bar{c}\_{t} comprises a component ∼u¯t\sim\bar{u}\_{t} that is independent of the portfolio value, alongside a component ∼v¯t\sim\bar{v}\_{t} that is contingent on the current portfolio.

Since the reward function depends on several parameters, two approaches can be considered for applying our G-learner:

1. 1.

   Direct Parameter Setting:

   * •

     In this first approach, the parameters of the reward function are directly defined.
   * •

     G-learner is then applied to find the optimal policy.
2. 2.

   Parameter Learning via Imitation:

   * •

     The second approach involves learning the parameters by imitating the behavior of a G-learning agent that has produced good results.
   * •

     The parameters are optimized before applying the G-learner algorithm to determine the optimal policy.
   * •

     The algorithm used for this approach is known as GIRL.

### d. Learning reward function parameters: GIRL

Application of the G-learner framework is appropriate when the investor clearly specifies his reward function and knows the values of the parameters θ:=(λ,η,ρ,Ω)\theta:=(\lambda,\eta,\rho,\Omega). However, in many scenarios, as is currently the case, the reward function remains unknown and depends on a set of parameters. Such situations, where rewards are not accessible, fall within the domain of inverse reinforcement learning (IRL), which aims to determine both the agent’s reward function and the optimal policy.

We seek to demonstrate how to deduce the reward function based on the observed actions of an agent. For this purpose, we assume access to a collection of trajectories. Furthermore, we possess historical data on asset prices and anticipated returns for every asset within the investor’s universe.

The principle is therefore to start from this set of supposedly independent trajectories, generated by a G-learner agent in our case, and try to reconstitute the hidden reward function by minimising the log likelihood of these trajectories. Mathematically, we have:

Assume we possess a collection of DD trajectories ζi\zeta\_{i} where i=1,…,Di=1,\ldots,D, each consisting of state-action pairs (xt,ut)(x\_{t},u\_{t}). Each trajectory ii begins at a specific time t0it\_{0}^{i} and continues until time TiT\_{i}. Now, consider one trajectory ζ\zeta from this set, setting its starting point at t=0t=0 and its endpoint at TT. We posit that the dynamics are Markovian with respect to the pair (xt,ut)(x\_{t},u\_{t}), described by a generative model given by
pθ​(xt+1,ut∣xt)=πθ​(ut∣xt)​pθ​(xt+1∣xt,ut)p\_{\theta}(x\_{t+1},u\_{t}\mid x\_{t})=\pi\_{\theta}(u\_{t}\mid x\_{t})p\_{\theta}(x\_{t+1}\mid x\_{t},u\_{t}), where Θ\Theta represents a vector of model parameters, and πθ\pi\_{\theta} is the action policy defined by Eq. ([9](https://arxiv.org/html/2511.18076v1#S3.E9 "Equation 9 ‣ a. Regularization of Q-learning. ‣ 3 Methods ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons")).

The likelihood of witnessing trajectory ζ\zeta can be expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(x,u∣Θ)=p0​(x0)​∏t=0T−1πθ​(ut∣xt)​pθ​(xt+1∣xt,ut),P\left(x,u\mid\Theta\right)=p\_{0}\left(x\_{0}\right)\prod\_{t=0}^{T-1}\pi\_{\theta}\left(u\_{t}\mid x\_{t}\right)p\_{\theta}\left(x\_{t+1}\mid x\_{t},u\_{t}\right), |  | (17) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​L​(θ):=log⁡P​(x,u∣Θ)=∑t∈ζ(log⁡πθ​(ut∣xt)+log⁡pθ​(xt+1∣xt,ut)).{LL}\left(\theta\right):=\log P\left(x,u\mid\Theta\right)=\sum\_{t\in\zeta}\left(\log\pi\_{\theta}\left(u\_{t}\mid x\_{t}\right)+\log p\_{\theta}\left(x\_{t+1}\mid x\_{t},u\_{t}\right)\right). |  | (18) |

Using the expression xt+1=At​(xt+ut)+(xt+ut)∘ϵ~tx\_{t+1}=A\_{t}(x\_{t}+u\_{t})+(x\_{t}+u\_{t})\circ\tilde{\epsilon}\_{t} with At:=diag​(1+r¯t)A\_{t}:=\text{diag}(1+\bar{r}\_{t}), we can express the transition probability as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ​(xt+1∣xt;ut)=e−12​ΔtT​Σr−1​Δt(2​π)N​|Σr|​δ​(xt+1(0)−(1+rf)​xt(0)),p\_{\theta}\left(x\_{t+1}\mid x\_{t};u\_{t}\right)=\frac{e^{-\frac{1}{2}\Delta\_{t}^{T}\Sigma\_{r}^{-1}\Delta\_{t}}}{\sqrt{\left(2\pi\right)^{N}|\Sigma\_{r}|}}\delta\left(x^{(0)}\_{t+1}-\left(1+r\_{f}\right)x^{(0)}\_{t}\right), |  | (19) |

|  |  |  |
| --- | --- | --- |
|  | Δt:=xt+1(r)xt(r)+ut(r)−At(r).\Delta\_{t}:=\frac{x^{(r)}\_{t+1}}{x^{(r)}\_{t}+u^{(r)}\_{t}}-{A^{(r)}\_{t}}. |  |

The term δ​(xt+1(0)−(1+rf)​xt(0))\delta\left(x^{(0)}\_{t+1}-\left(1+r\_{f}\right)x^{(0)}\_{t}\right) represents the deterministic behavior of the bond component within the portfolio.

These expressions allow us to derive the log-likelihood that the trajectory ζ\zeta was generated by the parameters πθ\pi\_{\theta} as follows:

|  |  |  |
| --- | --- | --- |
|  | L​L​(θ)=∑t∈ζ[β​Gtπ​(xt;ut)−Ftπ​(xt)−12​log⁡|Σr|−12​ΔtT​Σr−1​Δt],LL\left(\theta\right)=\sum\_{t\in\zeta}\left[\beta G\_{t}^{\pi}\left(x\_{t};u\_{t}\right)-F\_{t}^{\pi}\left(x\_{t}\right)-\frac{1}{2}\log|\Sigma\_{r}|-\frac{1}{2}\Delta\_{t}^{T}\Sigma\_{r}^{-1}\Delta\_{t}\right], |  |

Similarly, the likelihood of all the trajectories in the set DD is computed. The loss function to be used will then be obtained by summing these log-likelihoods.

#### 3.1.2 Implementation Process of G-learning

To implement our G-learning, we adopt two main approaches. The first approach involves defining the parameters of the reward function, using a G-learner agent to determine the optimal policy, and finally constructing the optimal portfolio. The second approach is based on inverse reinforcement learning, where the parameters of the reward function are learned using the GIRL algorithm, followed by the same steps as in the first approach. In these approaches, the key algorithms used are G-learner and GIRL. Below, we outline the different steps of the G-learning implementation before describing these two algorithms.
The following steps outline the implementation of our G-learning model:

* •

  Initialize the parameters of the initial policy (prior).
* •

  Initialize the reference portfolio (benchmark\_portf).
* •

  Invoke the G-learner to determine the optimal policy if the parameters are already known; otherwise, use GIRL first to learn the parameters.
* •

  Generate the action utu\_{t} by sampling from a normal distribution with mean μt\mu\_{t} and covariance Σprior​[t]\Sigma\_{\text{prior}}[t].
* •

  Update the portfolio state.
* •

  Simulate the returns of risky assets based on a one-factor model.
* •

  Update the returns and states.
* •

  Add (xt,ut)(x\_{t},u\_{t}) to the current trajectory.
* •

  Store the trajectory and returns in the respective lists.

## a.G-Learner Algorithm

The G-Learner is an algorithm that computes an optimal policy using the GG and FF functions. Below are its main steps:

* •

  Initialization: Both GG and FF functions are initially set to zero.
* •

  Calculate the reward function: for each given time t.
* •

  Updating GG and FF Values: These values are updated at every step, aiming to maximize long-term rewards.
* •

  Update the policy at each time step .
* •

  Convergence or Iteration Limit: The algorithm stops either when the GG and FF functions converge or when a maximum number of iterations is reached.

Algorithm for G-learner implementation.

Algorithm 1  G-learner Algorithm

1: Input:

* •

  num\_steps: number of time steps
* •

  x\_vals\_init: initial state (initial portfolio value)
* •

  reward\_params: parameters of the reward function
* •

  beta: discount factor
* •

  gamma: risk aversion
* •

  num\_risky\_assets: number of risky assets
* •

  riskfree\_rate: risk-free rate
* •

  expected\_risky\_returns: expected returns of risky assets
* •

  Sigma\_r: covariance matrix of risky assets
* •

  max\_iter\_RL: maximum number of iterations for convergence
* •

  eps: convergence tolerance

2: Output: Optimal policy π∗​(xt)\pi^{\*}(x\_{t}) and the optimized functions G∗G^{\*} and F∗F^{\*}.

3: Initialize the values for Gt​(xt,ut)G\_{t}(x\_{t},u\_{t}) and Ft​(xt)F\_{t}(x\_{t}) to 0 for all tt, xtx\_{t}, and utu\_{t}.

4: for nn from 0 to max\_iter\_RL do

5:  for tt from 0 num\_steps do

6:   Calculate the reward function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt​(xt,ut)\displaystyle R\_{t}(x\_{t},u\_{t}) | =−λ​P^t+12−utT​1+2​λ​P^t+1​(xt+ut)T​(1+r¯t)−λ​(xt+ut)T​Σ^t​(xt+ut)−utT​Ω​ut\displaystyle=-\lambda\hat{P}^{2}\_{t+1}-u\_{t}^{T}1+2\lambda\hat{P}\_{t+1}(x\_{t}+u\_{t})^{T}(1+\bar{r}\_{t})-\lambda(x\_{t}+u\_{t})^{T}\hat{\Sigma}\_{t}(x\_{t}+u\_{t})-u\_{t}^{T}\Omega u\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =xtT​Rt(x​x)​xt+utT​Rt(u​x)​xt+utT​Rt(u​u)​ut+xtT​Rt(x)+utT​Rt(u)+Rt(0).\displaystyle=x\_{t}^{T}R^{(xx)}\_{t}x\_{t}+u\_{t}^{T}R^{(ux)}\_{t}x\_{t}+u\_{t}^{T}R^{(uu)}\_{t}u\_{t}+x\_{t}^{T}R^{(x)}\_{t}+u\_{t}^{T}R^{(u)}\_{t}+R^{(0)}\_{t}. |  |

7:   Update the functions GG and FF using the backward Bellman algorithm to optimize future actions:

* •

  Gtπ​(xt,ut)=xt⊤​Qt(x​x)​xt+ut⊤​Qt(u​x)​xt+ut⊤​Qt(u​u)​ut+xt⊤​Qt(x)+ut⊤​Qt(u)+Qt(0)G\_{t}^{\pi}(x\_{t},u\_{t})=x\_{t}^{\top}Q\_{t}^{(xx)}x\_{t}+u\_{t}^{\top}Q\_{t}^{(ux)}x\_{t}+u\_{t}^{\top}Q\_{t}^{(uu)}u\_{t}+x\_{t}^{\top}Q\_{t}^{(x)}+u\_{t}^{\top}Q\_{t}^{(u)}+Q\_{t}^{(0)}.
* •

  Ft​(xt)=maxu⁡Gt​(xt,u)F\_{t}(x\_{t})=\max\_{u}G\_{t}(x\_{t},u).

8:   Update the policy at each time step:

|  |  |  |
| --- | --- | --- |
|  | π​(ut|xt)=1(2​π)n/2​|Σ~p|1/2​e−12​(ut−u~t−v~t​xt)⊤​Σ~p−1​(ut−u~t−v~t​xt).\pi(u\_{t}|x\_{t})=\frac{1}{(2\pi)^{n/2}|\tilde{\Sigma}\_{p}|^{1/2}}e^{-\frac{1}{2}(u\_{t}-\tilde{u}\_{t}-\tilde{v}\_{t}x\_{t})^{\top}\tilde{\Sigma}\_{p}^{-1}(u\_{t}-\tilde{u}\_{t}-\tilde{v}\_{t}x\_{t})}. |  |

9:  end for

10:  Exit the iteration loops once the tolerated error (error\_tol) is reached

11: end for

## b.GIRL Algorithm

The GIRL (Gradient Inverse Reinforcement Learning) algorithm infers the reward function based on observed behaviors. It aims to minimize a loss function that measures the discrepancy between observed trajectories and those generated by the estimated reward function. Below are the main steps of its implementation:

* •

  Initialization of Parameters:
  Initialization of the reward function parameters θ\theta.
* •

  Policy Estimation:
  GIRL utilizes the G-Learner algorithm to compute the optimal policy πθ\pi\_{\theta} for the current reward parameters.
* •

  Likelihood Calculation:
  For each observed trajectory, GIRL evaluates the probability that this trajectory was generated by the policy πθ\pi\_{\theta}.
* •

  Loss Minimization:
  GIRL updates θ\theta by minimizing the loss function (negative likelihood of the observed trajectories) using the gradient descent method.
* •

  Convergence: The process is repeated until the policy πθ\pi\_{\theta} is sufficiently close to the one that generated the observed trajectories.

Algorithm for GIRL implementation.

Algorithm 2  Inverse Reinforcement Learning (GIRL) Algorithm

1: Input:

* •

  τ\tau : observed trajectories (observed states and actions)
* •

  num\_sim: number of simulation
* •

  num\_steps: number of time steps
* •

  initial\_reward\_params: initial parameters of the reward function
* •

  beta: discount factor
* •

  gamma: risk aversion
* •

  max\_iter\_RL: maximum number of iterations for G-Learner
* •

  eps: tolerance for gradient (for gradient calculations)
* •

  learning\_rate: learning rate for updating reward function parameters

2: Output: Optimal reward function parameters θ∗\theta^{\*} explaining observed behaviors.

3: Initialize θ=initial\_reward\_params\theta=\text{initial\\_reward\\_params} (initial reward function parameters).

4: for each iteration until convergence or reaching the maximum number of iterations do

5:  Use the G-Learner to compute the policies πθ\pi\_{\theta} for the parameters θ\theta.

6:  for each observed trajectory τ={(xt,ut)}t=1T\tau=\{(x\_{t},u\_{t})\}\_{t=1}^{T} do

7:   Compute log-likelihood L​L​(θ)=∑t∈ζ[β​Gtπ​(xt;ut)−Ftπ​(xt)−12​log⁡|Σr|−12​ΔtT​Σr−1​Δt]LL\left(\theta\right)=\sum\_{t\in\zeta}\left[\beta G\_{t}^{\pi}\left(x\_{t};u\_{t}\right)-F\_{t}^{\pi}\left(x\_{t}\right)-\frac{1}{2}\log|\Sigma\_{r}|-\frac{1}{2}\Delta\_{t}^{T}\Sigma\_{r}^{-1}\Delta\_{t}\right] that πθ\pi\_{\theta} generated this trajectory.

8:  end for

9:  Compute the loss function (sum negative log-likelihood):

|  |  |  |
| --- | --- | --- |
|  | L​o​s​s​(θ)=−∑ζ∈τ∑t∈ζ[β​Gtπ​(xt;ut)−Ftπ​(xt)−12​log⁡|Σr|−12​ΔtT​Σr−1​Δt]{Loss}(\theta)=-\sum\_{\zeta\in\tau}\sum\_{t\in\zeta}\left[\beta G\_{t}^{\pi}\left(x\_{t};u\_{t}\right)-F\_{t}^{\pi}\left(x\_{t}\right)-\frac{1}{2}\log|\Sigma\_{r}|-\frac{1}{2}\Delta\_{t}^{T}\Sigma\_{r}^{-1}\Delta\_{t}\right] |  |

10:  Update the reward function parameters:

* •

  Compute the gradients ∇θL​o​s​s​(θ)\nabla\_{\theta}{Loss}(\theta) of the loss function with respect to θ\theta.
* •

  |  |  |  |
  | --- | --- | --- |
  |  | θ←θ−learning\_rate⋅∇θL​o​s​s​(θ)\theta\leftarrow\theta-\text{learning\\_rate}\cdot\nabla\_{\theta}{Loss}(\theta) |  |

11:  Check for convergence (if the loss function or gradients are close to a tolerance ϵ\epsilon).

12: end for

### 3.2 Description of data and simulation principle

Our study aims to demonstrate the effectiveness of reinforcement learning in solving real-world portfolio optimization problems with defined contributions. To achieve this, we rely on popular financial models, known for their ability to accurately replicate the dynamics of financial markets, to generate our data.

#### 3.2.1 Market and Asset Modeling

To model our market, we start with the assumption that the evolution of assets follows a Markov process. This means that the future price of an asset depends solely on its current price, without considering its historical price. This assumption accurately reflects the reality of financial markets. In fact, it is characteristic of geometric Brownian motion (GBM), which is widely used in mathematical finance to model stock prices, particularly in the Black-Scholes model. This model is the most commonly used to represent the behavior of stock prices and, more generally, that of financial markets.

Mathematically, this process is defined by the following relationship:

|  |  |  |
| --- | --- | --- |
|  | St=St−1×exp⁡((μ−12​σ2)​Δ​t+σ​Δt​Z)S\_{t}=S\_{t-1}\times\exp\left(\left(\mu-\frac{1}{2}\sigma^{2}\right)\Delta t+\sigma\sqrt{\Delta\_{t}}\,Z\right) |  |

Where:

* •

  StS\_{t} is the market value at time tt.
* •

  St−1S\_{t-1} is the market value at the previous time step t−1t-1.
* •

  μ\mu is the drift term or the expected return of the market.
* •

  σ\sigma is the volatility or standard deviation of the market returns.
* •

  Δt\Delta\_{t} is the time increment.
* •

  ZZ is a random variable drawn from a standard normal distribution, i.e., Z∼𝒩​(0,1)Z\sim\mathcal{N}(0,1).

For the market return at time t, denoted rtr\_{t}, we use a log-return to model it. This gives the following relationship.

|  |  |  |
| --- | --- | --- |
|  | rt=νM​Δt+σ​Δ​t​Zt\quad r\_{t}=\nu\_{M}\Delta\_{t}+\sigma\sqrt{\Delta t}Z\_{t} |  |

Where : νM\nu\_{M} is market drift

For risky assets, we have two developments of returns over time: one is the expected return, and the other is the return generated due to market impact (realized return)

### a.The expected risky asset returns, r¯t,i\bar{r}\_{t,i}, are given by:

|  |  |  |
| --- | --- | --- |
|  | rt,i=r¯t,i+βi0​(rM−μM​d​t)+σi​1−(βi0)2​d​Wt,i,i∈{1,…,N−1},r\_{t,i}=\bar{r}\_{t,i}+\beta^{0}\_{i}(r\_{M}-\mu\_{M}dt)+\sigma\_{i}\sqrt{1-(\beta^{0}\_{i})^{2}}dW\_{t,i},\quad i\in\{1,\dots,N-1\}, |  |

where μM=0.05\mu\_{M}=0.05 represents the drift of the market, rMr\_{M} denotes the market returns generated under a geometric Brownian motion (GBM) framework with a volatility of σM=0.25\sigma\_{M}=0.25. Additionally, βi0\beta^{0}\_{i} signifies the beta coefficient of the ii-th asset. The term σi≡σ=0.05\sigma\_{i}\equiv\sigma=0.05 indicates the idiosyncratic volatility, and d​WtdW\_{t} is a Brownian motion that drives the system and is correlated with the market noise, with d​t=0.25dt=0.25.

### b.realized returns r¯t\bar{r}\_{t} is assumed to be given by the CAPM:

|  |  |  |
| --- | --- | --- |
|  | r¯t=α+β0​[(1−c)​μM​d​t+c​rM],c∈[0,1],\bar{r}\_{t}=\alpha+\beta^{0}\left[(1-c)\mu\_{M}dt+cr\_{M}\right],\quad c\in[0,1], |  |

where we select the oracle coefficient c=0.2c=0.2.

We consider α\alpha and β0\beta^{0} as uniformly distributed random variables across all risky assets, defined as:

|  |  |  |
| --- | --- | --- |
|  | α∼U​([−0.05,0.15]),β0∼U​([0.05,0.85]).\alpha\sim U([-0.05,0.15]),\quad\beta^{0}\sim U([0.05,0.85]). |  |

These relationships enable the simulation of returns and values for risky assets within a single-factor model, where the returns are influenced by both market returns (weighted by a beta coefficient unique to each asset) and an idiosyncratic component (the specific volatility associated with each asset).

#### 3.2.2 Simulation

We therefore use the information from Tab. [1](https://arxiv.org/html/2511.18076v1#Sx2.T1 "Table 1 ‣ 3.2.2 Simulation ‣ b.realized returns 𝑟̄_𝑡 is assumed to be given by the CAPM: ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") below to simulate our data. This information is mainly related to the initial value of our market, the number of risky assets, the duration of our investment, the market return, the market volatility, and the risk-free rate.

| Financial Context Name | Value |
| --- | --- |
| Expected Market Return | 0.050.05 |
| Market Volatility | 0.250.25 |
| Initial Market Value | 100.0100.0 |
| Risk-Free Rate | 0.020.02 |
| Number of Time Steps | 2525 |
| Time Increment (Quarterly) | 0.250.25 |
| Number of Risky Assets | 9999 |

Table 1: Table of market and asset modeling parameters.

We can therefore observe the behavior of our market over time (based on variations in the Return of this market and variations in its value).

![Refer to caption](images/image_1.png)


Figure 4: Variation of Market returns and Market value over time

We can also observe the behavior of some simulated risky assets on this market.

![Refer to caption](images/image_2.png)


Figure 5: This figure shows the difference between the realized return and the expected return on a number of risky assets.

Fig. [4](https://arxiv.org/html/2511.18076v1#Sx2.F4 "Figure 4 ‣ 3.2.2 Simulation ‣ b.realized returns 𝑟̄_𝑡 is assumed to be given by the CAPM: ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") shows a significant variation in the return and value of our market over time, which is generally the case in most financial markets. We can directly observe the impact of this high market volatility on the realized returns of our assets, which completely deviate from the expected returns, as shown in Fig. [5](https://arxiv.org/html/2511.18076v1#Sx2.F5 "Figure 5 ‣ 3.2.2 Simulation ‣ b.realized returns 𝑟̄_𝑡 is assumed to be given by the CAPM: ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons").

The main task of our reinforcement learning model is to learn how to anticipate sudden changes in the returns of various assets caused by market volatility. The goal is to adjust the portfolio before each new fluctuation to maintain the balance required to reach the target at the defined horizon.

The results obtained with our model will be presented in the next section.

### 3.3 Results

### 3.4 Presentation of G-learning and GIRL performances

#### 3.4.1 Portfolio performance after direct optimization with G-learning

After applying a set of random parameters in a well-defined range to our G-learner , we obtained the best result with the following parameter values: θ:=(λ=0.002,η=1.3,ρ=0.5,Ω=1.1)\theta:=(\lambda=0.002,\eta=1.3,\rho=0.5,\Omega=1.1)

Indeed, with these parameters, our G-learning model was able to adjust the evolution of our portfolio’s return to produce a Shape Ratio of =0.481=0.481. According to the work of [schmid2010statistical], in high-volatility financial markets, Shape Ratio values vary between 0.20.2 and 0.70.7, and a Shape Ratio value of 0.30.3 is already considered relevant. In view of the high volatility of our market, we can conclude that our model produces a fairly interesting result. Fig. [6](https://arxiv.org/html/2511.18076v1#Sx2.F6 "Figure 6 ‣ 3.4.1 Portfolio performance after direct optimization with G-learning ‣ 3.4 Presentation of G-learning and GIRL performances ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") shows the evolution of the portfolio return optimized by our G-learner money and the value of the shape ratio obtained.

![Refer to caption](images/G-learner.png)


Figure 6: Adjusted portfolio returns over time using the G-learning model with fixed parameters.

#### 3.4.2 Parameters learned by the GIRL algorithm

We then use the G-learner agent, developed during the previous G-learning implementation, to simulate a set of trajectories (representing the changes in portfolio positions over time). The GIRL algorithm leverages these trajectories to infer and optimize the parameters of the reward function that was used to build the G-learner agent. Fig. [7](https://arxiv.org/html/2511.18076v1#Sx2.F7 "Figure 7 ‣ 3.4.2 Parameters learned by the GIRL algorithm ‣ 3.4 Presentation of G-learning and GIRL performances ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") below shows the values of the optimal parameters obtained. Tab. [2](https://arxiv.org/html/2511.18076v1#Sx2.T2 "Table 2 ‣ 3.4.2 Parameters learned by the GIRL algorithm ‣ 3.4 Presentation of G-learning and GIRL performances ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") compares the values learned by GIRL with the initial parameters used to construct our G-learner agent, highlighting GIRL’s ability to reconstruct and refine a reward function.

Table 2: Comparison of Parameters Learned by GIRL

| Parameters | G-learning | GIRL |
| --- | --- | --- |
| λ\lambda | 0.002 | 0.0012 |
| ω\omega | 1.1 | 1.01 |
| η\eta | 1.3 | 1.5 |
| ρ\rho | 0.5 | 0.4 |

![Refer to caption](images/loss_2.png)


Figure 7: Parameters learning curves using the GIRL model.

#### 3.4.3 Comparison of G-learning and GIRL returns

The Fig. [8](https://arxiv.org/html/2511.18076v1#Sx2.F8 "Figure 8 ‣ 3.4.3 Comparison of G-learning and GIRL returns ‣ 3.4 Presentation of G-learning and GIRL performances ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") below shows that the difference in performance between the portfolio optimized by our initial G-learning model and the one optimized using the parameters estimated by GIRL is negligible. However, we observe that GIRL achieves a slightly higher Sharpe ratio.

![Refer to caption](images/GIRL_and_G-learning.png)


Figure 8: Adjust portfolio returns over time using the G-learner model.

### 3.5 Presentation of portfolio optimisation results

For the analytical aspects of our reward function, recall that the reference portfolio (benchmark) was designed to follow exponential growth. As the value of our portfolio increases, the objective becomes progressively more ambitious. This approach also offers an advantage: it allows our portfolio to grow rapidly, even if the agent struggles to keep pace with the benchmark’s performance over time. Fig.  [9](https://arxiv.org/html/2511.18076v1#Sx2.F9 "Figure 9 ‣ 3.5 Presentation of portfolio optimisation results ‣ b.GIRL Algorithm ‣ Reinforcement Learning for Portfolio Optimization with a Financial Goal and Defined Time Horizons") below illustrates the evolution of our portfolio over time.

![Refer to caption](images/portfolio.png)


Figure 9: Evolution of the portfolio over time and regular contributions CtC\_{t}

Applying our model to a specific case of a portfolio with an initial value of $1000, equally distributed across our various assets at time t=0t=0, reveals a significant growth in portfolio value, closely aligning with the investor’s target (benchmark portfolio) at the end of the investment period. This was achieved with minimal investor contributions ctc\_{t} at each time step tt. We can thus conclude that our model effectively establishes a robust portfolio management strategy, allowing us to efficiently manage assets over time to reach our objectives namely, maximizing portfolio value while minimizing investor contributions ctc\_{t} throughout the period.

In the following sections, we will analyze our approach and the results obtained, describe future research directions, and provide a general conclusion for the overall work conducted.

## 4 Discussion

The results of this research show that portfolio optimization using G-Learning and the GIRL algorithm effectively maximizes portfolio value at the target date while minimizing regular contributions. The developed model achieved a Sharpe ratio of 0.483, which, according to [schmid2010statistical], is significant for a highly diversified portfolio in markets characterized by high volatility. This ratio indicates that our method provides a good balance between return and risk in an uncertain environment, producing a relatively high Sharpe ratio with a well-diversified portfolio and, therefore, a reduced risk level.

The success of G-Learning lies in its ability to account not only for market fluctuations but also for periodic contributions. Compared to traditional approaches based on supervised learning or classical techniques such as Modern Portfolio Theory, our method is more flexible and dynamic. Our results also align with the findings of [dixon2020g], demonstrating that reinforcement learning-based techniques are better suited to complex markets and highly diversified portfolios.

However, we found that the optimal parameters obtained using the GIRL model (e.g., λ=0.0012\lambda=0.0012 compared to an initial value of 0.002) result in only a marginal improvement in the Sharpe ratio. This suggests that although GIRL effectively adjusts the reward function parameters, its overall impact on portfolio performance remains limited. A possible reason for this performance is that the existing agent is already efficient and therefore simulates portfolio evolutions that are quite similar, reducing the effect of parameter adjustments on GIRL’s overall profitability. It tends to produce portfolio evolutions close to those simulated, leading to a minimal optimization of the Sharpe Ratio. It would be interesting to test this approach in less volatile markets or with longer investment horizons to better evaluate the impact of the optimized parameters.

Our results also emphasize that the goal-based formulation (focused on specific objectives) is better aligned with investors’ needs than Markowitz’s classical approaches. By considering specific financial objectives at a given date, our model provides more targeted management, in line with the work of [browne2000stochastic] and [das2020dynamic].

## 5 Conclusion

This research proposes an enhancement of the innovative portfolio optimization approach based on the G-Learning algorithm and parametric optimization using GIRL, as introduced by [dixon2020machine]. The objective was to maximize portfolio value by a target date while minimizing periodic contributions from the investor within a highly diversified portfolio. The results demonstrate that our method achieves a significant Sharpe ratio in a volatile market environment, underscoring the relevance of reinforcement learning for dynamic financial problems. Our study offers a solution to goal-based optimization, enabling investment decisions to align more closely with the investor’s specific needs, such as funding a purchase by a given date. This approach surpasses the limitations of traditional models like Modern Portfolio Theory by incorporating greater flexibility and adaptability to market shifts. The importance of this research lies in demonstrating that probabilistic reinforcement learning is not only applicable but also effective in asset management. By providing a framework that considers both regular contributions and market fluctuations, this method serves as a valuable tool for portfolio managers and individual investors .

### 5.1 Recommendations

For future research, we first suggest exploring the construction of a reward function that could further enhance performance, or alternatively, considering a different approach to regularizing Q-learning. Secondly, we recommend applying G-Learning to other asset classes and in various macroeconomic contexts. Integrating exogenous data and developing real-time adaptive approaches could also open promising new avenues.

## 6 Acknowledgments

This work constitutes my final thesis at the African Institute of Mathematical Sciences (AIMS) in South Africa and Stellenbosch University. I would first like to express my deep gratitude to my supervisors, Dr. Rock Stephane Koffi and Dr. Prudence Djagba, for the confidence they placed in me, as well as for their support, guidance, comments, and encouragement throughout the writing of this thesis. I am deeply thankful to them. I would also like to thank my academic director, Prof. Claire David, and the head of the AI for Science program tutors, Emmanuel Ahenkan, for their valuable advice, time management recommendations, presence, and support during the writing of this thesis and throughout the academic year. To the team at Google DeepMind, without whom this dream would not have been possible, I express my sincere gratitude for their financial support and for the arrangements made for this program. Finally, to everyone who contributed in one way or another to the completion of this work and to the success of this academic year, I extend my deepest thanks.