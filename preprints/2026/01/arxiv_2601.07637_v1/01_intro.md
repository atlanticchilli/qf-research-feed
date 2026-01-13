---
authors:
- Benjamin Avanzi
- Ronald Richman
- Bernard Wong
- Mario Wüthrich
- Yagebu Xie
doc_id: arxiv:2601.07637v1
family_id: arxiv:2601.07637
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Reinforcement Learning for Micro-Level Claims Reserving
url_abs: http://arxiv.org/abs/2601.07637v1
url_html: https://arxiv.org/html/2601.07637v1
venue: arXiv q-fin
version: 1
year: 2026
---


Benjamin Avanzi
[b.avanzi@unimelb.edu.au](mailto:b.avanzi@unimelb.edu.au)

Ronald Richman
[ronaldrichman@gmail.com](mailto:ronaldrichman@gmail.com)

Bernard Wong
[bernard.wong@unsw.edu.au](mailto:bernard.wong@unsw.edu.au)

Mario Wüthrich
[mario.wuethrich@math.ethz.ch](mailto:mario.wuethrich@math.ethz.ch)

Yagebu Xie
[yagebuxie@gmail.com](mailto:yagebuxie@gmail.com)

###### Abstract

Outstanding claim liabilities are revised repeatedly as claims develop, yet most modern reserving models are trained as one-shot predictors and typically learn only from settled claims. We formulate individual claims reserving as a claim-level Markov decision process in which an agent sequentially updates outstanding claim liability (OCL) estimates over development, using continuous actions and a reward design that balances accuracy with stable reserve revisions. A key advantage of this reinforcement learning (RL) approach is that it can learn from all observed claim trajectories, including claims that remain open at valuation, thereby avoiding the reduced sample size and selection effects inherent in supervised methods trained on ultimate outcomes only. We also introduce practical components needed for actuarial use—initialisation of new claims, temporally consistent tuning via a rolling-settlement scheme, and an importance-weighting mechanism to mitigate portfolio-level underestimation driven by the rarity of large claims. On CAS and SPLICE synthetic property–casualty datasets, the proposed Soft Actor–Critic implementation delivers competitive claim-level accuracy and strong aggregate OCL performance, particularly for the immature claim segments that drive most of the liability.

###### keywords:

Reserving , Neural networks , Reinforcement learning , Outstanding Claim Liability
JEL codes: G22 , C45 , C53 MSC classes:
91G70 , 91G60 , 62P05 , 91B30

## 1 Introduction

### 1.1 Background

The prediction of outstanding claims liabilities (OCL) is a core task that underpins solvency and capital management for all insurers. In non-life insurance, policyholders pay premium(s) to receive coverage for a non-life risk. In the event of an accident, a claim may be incurred, and the insurer is liable to cover some or all of the loss.

Early chain ladder models (e.g., Mack, [1993](https://arxiv.org/html/2601.07637v1#bib.bib44)) were limited by low computational power, and hence relied on strong homogeneity assumptions and followed macro-level reserving formulations, which deal with aggregate claims data. Limitations to storage capacity meant that data was stored at the aggregate level as well with no easy way to extract individual claims data. With improvements to computational power came progressively more complex reserving models. These improvements came in two major forms. Firstly, the introduction of micro-level reserving formulations (individual claims level reserving) by Arjas ([1989](https://arxiv.org/html/2601.07637v1#bib.bib3)) and Norberg ([1993](https://arxiv.org/html/2601.07637v1#bib.bib52), [1999](https://arxiv.org/html/2601.07637v1#bib.bib53)) proposed initial ideas to work with individual level claims data. Aggregate data are not necessarily sufficient statistics for the estimation of model parameters, and hence the additional granularity and incorporation of claim-level covariates within a micro-level reserving model can yield improvements in predictive power. Antonio and Plat ([2012](https://arxiv.org/html/2601.07637v1#bib.bib2)) implemented the framework of Norberg ([1993](https://arxiv.org/html/2601.07637v1#bib.bib52), [1999](https://arxiv.org/html/2601.07637v1#bib.bib53)) and showed micro-level results outperformed traditional macro-level methods in their case study. Avanzi et al. ([2015](https://arxiv.org/html/2601.07637v1#bib.bib10)) extends this by relaxing the impractical Poisson distribution assumption. Secondly, machine learning has become an active area of research in developing state-of-the-art reserving models for both macro- and micro-level formulations. With increasing computational power, the reserving literature commonly explores the techniques of GLMs (Taylor and McGuire, [2016](https://arxiv.org/html/2601.07637v1#bib.bib65); England and Verrall, [2002](https://arxiv.org/html/2601.07637v1#bib.bib26); Wüthrich and Merz, [2008](https://arxiv.org/html/2601.07637v1#bib.bib68)), decision trees (Baudry and Robert, [2019](https://arxiv.org/html/2601.07637v1#bib.bib12); Lopez et al., [2019](https://arxiv.org/html/2601.07637v1#bib.bib43); Duval and Pigeon, [2019](https://arxiv.org/html/2601.07637v1#bib.bib25)), and neural networks (Gabrielli et al., [2018](https://arxiv.org/html/2601.07637v1#bib.bib29); Kuo, [2019](https://arxiv.org/html/2601.07637v1#bib.bib39); Delong and Wüthrich, [2020](https://arxiv.org/html/2601.07637v1#bib.bib21); Gabrielli, [2021](https://arxiv.org/html/2601.07637v1#bib.bib28)).

An insurer, in any given calendar period, must make a decision on how much to hold in reserve to meet its outstanding claims liabilities (OCL). Regulators (APRA in Australia) require insurers to produce central estimates of the OCL. This task should be performed using the latest available claims information, and the decision is made sequentially every calendar period. This motivates the natural representation of the reserving problem as a Markov Decision Process (MDP) (Howard, [1960](https://arxiv.org/html/2601.07637v1#bib.bib34)), which in turn, motivates the use of RL techniques. Note that in most jurisdictions, calculation of a risk margin is also required to reflect aleatoric and epistemic uncertainty; this isn’t considered here.

The application of RL in the actuarial literature is still nascent, and particularly so for reserving. Dong and Finlay ([2025](https://arxiv.org/html/2601.07637v1#bib.bib24)) propose a discrete action space framework for aggregate reserving using proximal policy optimisation (PPO), targeting a conditional value-at-risk (CVaR) objective. Their model is trained on two CAS datasets and tested on simulated data obtained through a random draw with a random Gaussian macroeconomic shock applied. They report a boost in performance across all metrics compared to the chain ladder, Bornhuetter-Ferguson, and a stochastic bootstrap method. To the best of our knowledge, this is the only work that applies RL to reserving in the literature. Our contribution is distinct in that we propose a reserving approach working at the transactional level, targeting a central estimate of the OCL. Moreover, we allow smooth adjustments to OCL estimates over developments rather than discrete aggregate reserve adjustments. Finally, we detail implementational mechanisms to address data splitting, hyperparameter tuning, and downward bias correction relevant to micro-level reserving. Outside reserving, Krasheninnikova et al. ([2019](https://arxiv.org/html/2601.07637v1#bib.bib38)) applied RL to find an insurance renewal pricing strategy in discrete state space and action space. Palmborg and Lindskog ([2023](https://arxiv.org/html/2601.07637v1#bib.bib54)) extends this to a more general premium control formulation and generalises to a non-finite state space with a tabular learning approach called SARSA. Chong et al. ([2023](https://arxiv.org/html/2601.07637v1#bib.bib18)) apply deep RL to hedge variable annuities, while Wekwete et al. ([2023](https://arxiv.org/html/2601.07637v1#bib.bib66)) apply deep RL to reduce the need for human judgment in asset liability management. It is worthwhile to mention that the field of RL originated largely from optimal control theory, which is not new in the actuarial literature (e.g., Gerber, [1979](https://arxiv.org/html/2601.07637v1#bib.bib30); Asmussen and Taksar, [1997](https://arxiv.org/html/2601.07637v1#bib.bib4); Martin-Löf, [1983](https://arxiv.org/html/2601.07637v1#bib.bib45), [1994](https://arxiv.org/html/2601.07637v1#bib.bib46), and the references therein). With greater computational power, RL can work with far more complex dynamic systems than in traditional optimal control theory, and particularly when there is no model of the underlying environment dynamics. Palmborg and Lindskog ([2023](https://arxiv.org/html/2601.07637v1#bib.bib54)) in particular take heavy inspiration from [Martin-Löf](https://arxiv.org/html/2601.07637v1#bib.bib45)’s ([1983](https://arxiv.org/html/2601.07637v1#bib.bib45); [1994](https://arxiv.org/html/2601.07637v1#bib.bib46)) formulation of an optimal premium rule in simple settings. Applications of RL have been explored more so in other non-actuarial literature, such as algorithmic trading (Moody and Saffell, [2001](https://arxiv.org/html/2601.07637v1#bib.bib49); Deng et al., [2017](https://arxiv.org/html/2601.07637v1#bib.bib22)), finance (Buehler et al., [2019](https://arxiv.org/html/2601.07637v1#bib.bib15); Hambly et al., [2023](https://arxiv.org/html/2601.07637v1#bib.bib33)), inventory management (Boute et al., [2022](https://arxiv.org/html/2601.07637v1#bib.bib14); Moor et al., [2022](https://arxiv.org/html/2601.07637v1#bib.bib50)), and even particle physics (Meier et al., [2012](https://arxiv.org/html/2601.07637v1#bib.bib47)).

### 1.2 Motivations for using RL

As we argued above, the recursive nature of RL makes it a natural solution to the reserving problem. There are several potential advantages (some purely theoretical) to using RL for reserving, which are elaborated in this section.

While standard/vanilla RL algorithms are not theoretically robust to non-stationarity (Sutton and Barto, [2018](https://arxiv.org/html/2601.07637v1#bib.bib62)), an educated choice of design and features for the RL implementation may give it an edge compared to supervised methods when dealing with gradual shifts (rather than abrupt regime changes). RL is a sequential approach, and its implementation will likely be such that the model gets data input (approximately) chronologically. This is particularly so in the soft actor-critic (SAC) algorithm that we use (see also Section [2](https://arxiv.org/html/2601.07637v1#S2 "2 Introduction to Reinforcement Learning ‣ Reinforcement Learning for Micro-Level Claims Reserving") below). The SAC resamples recent past experiences, so that more emphasis is placed on recent experiences rather than distant past experiences.

Importantly, an RL approach allows learning from open claims. In contrast, supervised learning approaches require claims to be settled before we can learn from them, since their “supervision” requires a target – here the actual ultimate loss (UL) or equivalently outstanding claims liability (OCL). Some supervised methods have attempted to circumvent this constraint by predicting a series of sequential payments rather than the UL or OCL (e.g., Gabrielli, [2021](https://arxiv.org/html/2601.07637v1#bib.bib28); Schwab and Schneider, [2024](https://arxiv.org/html/2601.07637v1#bib.bib58)), but this approach can be controversial as errors may compound. Approaches that do target the UL/OCL use exclusively settled claims for training, which does not make full use of the available data, and leads to biases (mainly towards quick-to-settle claims; see also [A](https://arxiv.org/html/2601.07637v1#A1 "Appendix A Causes of Downward Bias ‣ Reinforcement Learning for Micro-Level Claims Reserving")). RL avoids this issue altogether as it is not a supervised learning algorithm, and hence does not require targets to train on.

Additionally, RL conceptually allows for a continuously learning model without the need to retrain every time new data is received.
In contrast, supervised learning methods require periodic refitting with an updated dataset in order to mitigate concept drift. An attractive idea with RL is that it can (theoretically) continue to integrate new experiences over time through gradient updates, without the need to retrain the model. This is very much an adjacent idea to the first advantage pertaining to non-stationarity. However, this idealistic, continuously learning model is still likely a pipe dream due to a problem known as “catastrophic forgetting”, where neural networks can tend to forget quickly what it has learned in the past upon learning something new (French, [1999](https://arxiv.org/html/2601.07637v1#bib.bib27)). Although not explored in this paper, this idea endows RL with potential that can be tested in future work.

A further motivation for reinforcement learning, beyond its sequential structure, is that it provides a principled framework for *temporal credit assignment*. In reserving, the quality of an estimate at an early development period can only be fully assessed once the claim eventually settles. However, the ability to design rewards in an RL approach allows intermediate feedback to the model before a claim is ever settled. Through well-designed rewards, reinforcement learning naturally propagates information about accuracy backward through time via “temporal-difference” updates. This allows early-period estimation behaviour to be shaped by long-horizon outcomes without requiring intermediate labels. From this perspective, reinforcement learning can be viewed as a generalisation of classical reserving techniques that update estimates recursively, but with function approximation and optimisation driven directly by long-run estimation performance.

Relatedly, the ability to design the reward structure with which the model learns can be very powerful. One can incorporate expert knowledge and judgment, as well as potentially tailor a model to specific characteristics of a portfolio. While the design requires some creativity and experimentation, the ability to directly influence the behaviour of the model is essentially unmatched in supervised learning techniques.

In this paper, we develop an implementation of RL for micro-level reserving with detailed benchmarking to demonstrate its feasibility. While the performance is already competitive with benchmarks, it opens the door to many exciting possible improvements to the approach by bringing in more advanced techniques within the RL literature. Our contributions are detailed in the next section.

### 1.3 Contributions

In this paper, we develop a broad conceptual framework to apply RL on the micro-level reserving problem, including core definitions for its Markov Decision Process (MDP) representation. As is usual in the micro-level reserving literature, we focus on forecasting the OCL for open claims (RBNS), but as explained above, we do make use of open claims data.
In our framework, the RL algorithm learns over time from a sequence of regularly time-spaced observations (e.g., quarters, but this could be arbitrarily adjusted).

We benchmark the performance of our RL approach against that of the chain ladder and a vanilla feed-forward neural network (FNN). We first compare all three models on a property casualty synthetic dataset from the Casualty Actuarial Society (CAS, [2025](https://arxiv.org/html/2601.07637v1#bib.bib16)), which is designed to “replicate selected modelling problems that are commonly faced by members of the CAS”. To properly study the properties of the models, we then use simulated data from the SPLICE simulator (Avanzi et al., [2021b](https://arxiv.org/html/2601.07637v1#bib.bib8), [2023](https://arxiv.org/html/2601.07637v1#bib.bib7), [a](https://arxiv.org/html/2601.07637v1#bib.bib6)). Because data are simulated, we can benchmark those models using “actuals” (simulated beyond the valuation date), and importantly, results can be averaged over multiple simulations. With simulated data of low complexity (agreeing with chain ladder assumptions), we show that the RL performs decently relative to chain ladder. We then run all three models on high complexity data (also from SPLICE), and show that RL is able to remain competitive (if not better) relative to the FNN model.

The implementation of this framework is far from trivial, and required us to address a number of critical issues, including (but not limited to) the following ones:

* 1.

  Design decisions made in the MDP are critical in determining how performant the RL model will be. The most important component here is the design of reward signals from which the RL model learns. This involved developing a reward function that encourages accurate predictions while also developing additional reward components that encourage ideal behaviour of stable predictions over the lifetime of a claim.
* 2.

  When a claim is notified and first “passed” through the RL algorithm, it needs to be initialised. We discuss how to do so in depth. A good initialisation is particularly material for shorter claims, because the model will have only a few opportunities to adjust a poor starting estimate. We propose a credibility-like approach (balancing period of origin data with whole past data, depending on the maturity of that period of origin), with explicit adjustment for any potential changing claims mix over the training period.
* 3.

  We introduce a “rolling settlement” tuning procedure, whereby temporal splitting of data is carefully performed to prevent data leakage during training and validation. Traditionally, RL does not have a need for data splitting to facilitate validation and testing, as data is typically plentiful. However, there is such a need in the reserving context for hyperparameter tuning and for comparisons with supervised methods.
* 4.

  Optimising average claim-level accuracy alone can lead to systematic underestimation of aggregate outstanding liabilities due to the rarity and materiality of large claims; we explicitly address this issue through an ‘OCL’ importance-weighting mechanism.
  The same adjustment is applied to FNN, and hence does not affect the comparability of these two methods.

### 1.4 Outline of Paper

The paper is structured as follows. Section [2](https://arxiv.org/html/2601.07637v1#S2 "2 Introduction to Reinforcement Learning ‣ Reinforcement Learning for Micro-Level Claims Reserving") provides a relatively non-technical introduction to RL before we formulate the framework for applying RL to micro-level reserving at a high level in Section [3](https://arxiv.org/html/2601.07637v1#S3 "3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving"). While Section [3](https://arxiv.org/html/2601.07637v1#S3 "3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving") discusses only the crucial elements of the formulation, there are many implementational decisions necessary for a performant RL model that we develop in Section [4](https://arxiv.org/html/2601.07637v1#S4 "4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving"). We then develop a novel data splitting approach for the purposes of validation and evaluation in Section [5](https://arxiv.org/html/2601.07637v1#S5 "5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving"). In the initial evaluation of our models, we encountered a significant downward bias in the portfolio-level predictions, which we discuss and propose solutions for in Section [6](https://arxiv.org/html/2601.07637v1#S6 "6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving"). In Section [7](https://arxiv.org/html/2601.07637v1#S7 "7 Evaluation of Model Performance ‣ Reinforcement Learning for Micro-Level Claims Reserving"), we discuss the evaluation procedure of the RL model against benchmark models, with performance on simulated property–casualty datasets from CAS (CAS, [2025](https://arxiv.org/html/2601.07637v1#bib.bib16)) in Section [8.1](https://arxiv.org/html/2601.07637v1#S8.SS1 "8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") and SPLICE (Avanzi et al., [2023](https://arxiv.org/html/2601.07637v1#bib.bib7)) data presented in Section [8.2](https://arxiv.org/html/2601.07637v1#S8.SS2 "8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving"). We conclude by summarising and discussing the main results in Section [9](https://arxiv.org/html/2601.07637v1#S9 "9 Conclusion ‣ Reinforcement Learning for Micro-Level Claims Reserving").

## 2 Introduction to Reinforcement Learning

Reinforcement learning (RL) is a field of study that concerns optimal sequential decision-making (Silver, [2015](https://arxiv.org/html/2601.07637v1#bib.bib59)). The RL approach entails a learning agent that interacts with an environment and learns through reward/penalty signals. Through the objective of wanting to maximise rewards (or minimise penalties), the agent improves its behaviour towards some optimal policy of behaviour. Famous examples of RL results include models that can play Atari games (Mnih et al., [2013](https://arxiv.org/html/2601.07637v1#bib.bib48)) and beat the best human players at Go and Chess (Silver et al., [2017](https://arxiv.org/html/2601.07637v1#bib.bib60)). Below, we give a brief introduction to the general ideas of RL, but for a more comprehensive treatment, we refer the reader to Sutton ([1988](https://arxiv.org/html/2601.07637v1#bib.bib61)), Silver ([2015](https://arxiv.org/html/2601.07637v1#bib.bib59)), and Wuthrich et al. ([2025](https://arxiv.org/html/2601.07637v1#bib.bib67)).

### 2.1 Overview

In a very simple (and classic) illustration to capture the essence of this concept (adapted from lecture 1 of Silver, [2015](https://arxiv.org/html/2601.07637v1#bib.bib59)), a rat (the agent) learns from trial and error in an experiment. The environment in this scenario might be a researcher who provides stimuli, such as ringing a bell. If the rat pulls the lever after the sound of the bell ringing, it is rewarded with some cheese, while if it pulls the lever before the bell rings, it is given a shock. Without any training, the rat is unaware of these reward signals and environment dynamics. However, over time, it will learn that the bell ringing is an important environmental signal, and that pulling the lever after the bell maximises its reward (optimal policy). For simplicity, let us assume this example world operates in discrete time steps, such that if the bell rings, the rat can, at the earliest, pull the lever one time step later. This is so that the speed at which the rat reacts is not a consideration.

RL concerns “sequential decision making”, which requires that the problem at hand be formulated as a Markov Decision Process (MDP) ⟨𝒮,𝒜,𝒫,ℛ,γ⟩\langle\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma\rangle (Howard, [1960](https://arxiv.org/html/2601.07637v1#bib.bib34)). The discrete-time RL formulation is such that when the agent interacts with the environment, it observes a state st∈𝒮s\_{t}\in\mathcal{S}, decides to take an action at∈𝒜a\_{t}\in\mathcal{A} as per its policy, and receives a reward signal rt∈ℛr\_{t}\in\mathcal{R}. Subsequently, the environment evolves according to some unknown underlying dynamics 𝒫\mathcal{P} (denoting transition probabilities) due (at least partly) to the agent’s action ata\_{t}, and the agent will then observe the next state st+1s\_{t+1}, repeating the cycle. Lastly, γ∈(0,1)\gamma\in(0,1) is a discount factor that controls how much less the agent should value tomorrow’s reward compared to today’s.

While this interaction with the environment occurs, the agent’s behaviour is called the policy π​(a∣s):=ℙ​(At=a∣St=s)\pi(a\mid s):=\mathbb{P}(A\_{t}=a\mid S\_{t}=s). The core objective is for the agent to reach some deterministic optimal policy π∗\pi^{\*} that maximises rewards. To achieve this, the RL model either directly optimises a parameterised policy (policy-based), or optimises estimates of “value functions” (value-based):

* 1.

  The (state)-value function vπ​(s)v\_{\pi}(s) is the expected present value of total future rewards given we are currently in state ss and continue to follow the policy π\pi hereinafter. That is,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | vπ​(s)=𝔼π​[Gt∣St=s],Gt=∑k=0∞γk​rt+k+1.v\_{\pi}(s)=\mathbb{E}\_{\pi}[G\_{t}\mid S\_{t}=s],\quad G\_{t}=\sum\_{k=0}^{\infty}\gamma^{k}r\_{t+k+1}. |  | (2.1) |

  where GtG\_{t} denotes the “goal” (i.e., objective) the agent wants to maximise.
* 2.

  The action-value function qπ​(s,a)q\_{\pi}(s,a) is the expected present value (EPV) of total future rewards given we are currently in state ss, take action aa, and then continue to follow the policy π\pi hereinafter. In this case, we have then

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | qπ​(s,a)=𝔼π​[Gt∣St=s,At=a].q\_{\pi}(s,a)=\mathbb{E}\_{\pi}[G\_{t}\mid S\_{t}=s,A\_{t}=a]. |  | (2.2) |

The intuition here is that value-based methods preference actions based on some underlying computed expected future value that the action will yield, whereas policy-based methods simply increase the probability of an action that yielded good returns. In our example, if the rat is policy-based, it would increase its probability of pulling the lever after the bell upon getting cheese. If it is value-based, then it would intrinsically compute some underlying value associated with pulling the lever at any point in time. Modern methods often combine these approaches in the actor–critic framework (Sutton and Barto, [2018](https://arxiv.org/html/2601.07637v1#bib.bib62); Konda and Tsitsiklis, [1999](https://arxiv.org/html/2601.07637v1#bib.bib37)), which separately implements both policy improvement (actor) and value estimation (critic). In “deep RL”, these are typically represented by two separate neural networks. By having both a policy and a value function approximation, we get the best of both worlds. In practice, this yields faster and more stable convergence due to variance reduction and greater sample efficiency (Konda and Tsitsiklis, [1999](https://arxiv.org/html/2601.07637v1#bib.bib37); Xu et al., [2021](https://arxiv.org/html/2601.07637v1#bib.bib71)).

At every time step, the agent faces two choices: either exploit its policy’s current best known action to get a known maximum EPV, or take a risk and explore some action whose consequences are unknown to the model in the hopes of finding a better policy. This is known as the exploration vs exploitation trade-off in RL; see also Remark [3.5](https://arxiv.org/html/2601.07637v1#S3.Thmremark5 "Remark 3.5. ‣ 3.4 Description of one iteration ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving") for additional commentary specific to our reserving context. Using the rat example, suppose now that there are multiple stimuli, such as a flash of light in addition to the bell. Further, suppose that if the rat pulls the lever after a flash of light, it has a 75% chance of getting some cheese, and 25% chance of being shocked, whereas if it pulls the lever after the bell, it will get some cheese with 100% chance. If the rat discovers the pattern behind the flash of light first, then it has the option to continue exploiting this newfound pattern, or to explore something new, like waiting until after the bell rings. Exploration could backfire, but in this case, it would lead to the discovery of a new optimum. In the context of micro-level reserving, suppose that there is a structural break at some point in time that increases settlement speed of claims. Prior to this structural break, the agent may tend to adjust the OCL estimate downward at a slow pace on average. After the structural break, if the agent continues to exploit its pre-break policy, it will still be rewarded, but if the agent undertakes exploration, it could, by chance, discover that a faster rate of OCL estimate reduction is better.

Of course, because the value functions pertain to the expected (discounted) future gains, they must in practice be estimated since the underlying environment dynamics are not known. There are two broad methods to do so – Monte Carlo (MC) and temporal differencing (TD), with TD being more widely adopted. We refer to the aforementioned sources for a more detailed discussion of these methods. In short, TD gives us the ability to perform updates before a learning episode terminates (or in cases where there is no termination). An episode is simply one run of interaction between the agent and the environment, e.g., a single claim’s development until settlement is one episode. Using the example of a claim, TD performs updates at each time step before the claim is ever settled, whereas MC would do all the updates upon settlement. There is a bias-variance trade-off here: MC estimation is unbiased, but has high variance, whereas TD estimation has low variance, but introduces bias.

The state and action spaces (𝒮,𝒜\mathcal{S},\mathcal{A}) simply pertain to the range of possible values for the state and actions, and these can be either discrete or continuous. At its simplest, for discrete, finite state and action spaces (e.g., the rat example), combinations of states and actions mapping to a value function can be stored in a table (called tabular learning). However, as the size of these spaces grow (or become infinite), this tabular approach quickly becomes untenable. For a claim, its outstanding claims liabilities can, in theory, be any dollar amount in ℝ+\mathbb{R}^{+} (up to some maximum). We cannot represent this continuous range of possible OCL in a table. Hence, a far more practical approach is to approximate this mapping via some function, known as functional approximation. In deep RL, this functional approximation uses neural networks (Mnih et al., [2013](https://arxiv.org/html/2601.07637v1#bib.bib48)). For a review on neural networks, we refer to Wuthrich et al. ([2025](https://arxiv.org/html/2601.07637v1#bib.bib67)) and Goodfellow et al. ([2017](https://arxiv.org/html/2601.07637v1#bib.bib31)).

After specifying an MDP for the problem, we must use an RL algorithm to train the model. RL algorithms specify

* 1.

  a representation for the policy and value functions (typically neural networks);
* 2.

  whether the learning process is on-policy or off-policy. On-policy algorithms are such that the models learns policy π\pi while also following the same policy π\pi, whereas off-policy algorithms learn a policy π\pi by sampling the experiences of another different policy μ\mu;
* 3.

  how the agent conducts exploration.

### 2.2 RL algorithms

In this section, we briefly cover two popular RL algorithms: proximal policy optimisation (PPO Schulman et al., [2017b](https://arxiv.org/html/2601.07637v1#bib.bib57)) and soft actor-critic (SAC Haarnoja et al., [2018](https://arxiv.org/html/2601.07637v1#bib.bib32)). Before that, we note that the most significant difference between these two algorithms is that fact that PPO is an on-policy algorithm, while SAC is an off-policy algorithm. Because off-policy algorithms can learn from a different policy, they are able to employ experience replay (Lin, [1992](https://arxiv.org/html/2601.07637v1#bib.bib42)), whereby past experiences are stored in a replay buffer (essentially a list) to learn from later. This technique boosts sample efficiency by re-using past experiences and breaks temporal correlation to potentially help improve training stability.

#### 2.2.1 PPO

Proximal Policy Optimisation (PPO, Schulman et al., [2017b](https://arxiv.org/html/2601.07637v1#bib.bib57)) and its predecessor, Trust Region Policy Optimisation (TRPO, Schulman et al., [2017a](https://arxiv.org/html/2601.07637v1#bib.bib56)) are on-policy methods. Schulman et al. ([2017a](https://arxiv.org/html/2601.07637v1#bib.bib56)) espouse that policy optimisation can be classified into three broad categories: policy iteration, policy gradient, and gradient-free methods. Policy iteration is simply the value-based method of optimisation described previously. For policy-based methods, it can be further broken down into those that optimise a differentiable objective using the gradient (policy gradient methods) vs those that do not use the gradient (gradient-free methods). In particular, prior to TRPO, gradient-based methods were not able to consistently beat out gradient-free methods despite having better sample efficiency. In practice, TRPO and PPO are popular because they are “effective for optimising large nonlinear policies such as neural networks” (Schulman et al., [2017a](https://arxiv.org/html/2601.07637v1#bib.bib56)).

PPO is generally considered an improvement to TRPO because it retains many benefits of TRPO, yet is much simpler to implement, and enjoys better sample efficiency empirically. The innovation of PPO (and TRPO) is that it only allows small changes to the policy within a small and safe range at each step of gradient update. While TRPO has stronger theoretical guarantees, PPO enjoys more stable convergence and better performance empirically thanks to its more parsimonious approach, while retaining the core idea of limiting the size of policy updates.

#### 2.2.2 SAC

Soft Actor-Critic (SAC) is an off-policy method that aims to maximise the expected gain plus an entropy term, where higher entropy means more exploration. In the words of Haarnoja et al. ([2018](https://arxiv.org/html/2601.07637v1#bib.bib32)), SAC aims to “succeed at the task while acting as randomly as possible”. Prior deep RL methods based on the “maximum entropy” approach were restricted to discrete actions, while SAC is able to handle continuous actions. SAC was able to outperform many previous on-policy and off-policy methods, with the additional empirical benefit that it is stable in the sense that it achieves similar performance across different random seeds.

The general maximum entropy objective that the agent seeks to maximise (Ziebart and Fox, [2010](https://arxiv.org/html/2601.07637v1#bib.bib74)) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J(π)=𝔼[∑t=0Tγt{r(st,at)+αℋ(π(⋅∣st))}],J(\pi)=\mathbb{E}\left[\sum\_{t=0}^{T}\gamma^{t}\{r(s\_{t},a\_{t})+\alpha\mathcal{H}(\pi(\cdot\mid s\_{t}))\}\right], |  | (2.3) |

where γ\gamma is the discount factor, r​(st,at)r(s\_{t},a\_{t}) is the reward given action ata\_{t} taken in state sts\_{t}, ℋ(π(⋅∣s))\mathcal{H}(\pi(\cdot\mid s)) is the entropy term, and α>0\alpha>0 is the “temperature” coefficient that controls how much the agent is encouraged to explore. An agent that explores more will have higher entropy ℋ\mathcal{H}, and thus be rewarded for it since it would increase the objective function. We show this objective to demonstrate that the crux of the idea is that a maximum entropy objective is designed to prefer policies that achieve high reward while also being as stochastic as possible; the agent must maximise the cumulative discounted sum of the rewards of its actions, r​(st,at)r(s\_{t},a\_{t}), and the amount of exploration it undertook (ℋ\mathcal{H}). Note that entropy originates from information theory as a measure of average uncertainty, where high entropy denotes high uncertainty (stochasticity) (Cover and Thomas, [2006](https://arxiv.org/html/2601.07637v1#bib.bib19)).

## 3 Micro-reserving RL Formulation

### 3.1 Overarching RL Framework

Let us define the following notation: t=1,…t=1,... denotes the calendar period; i=1,…,Ii=1,...,I denotes the accident period; j=1,…,Jj=1,...,J denotes the development period since accident; and τ=1,…\tau=1,... denote the periods since notification of the claim. Hence, t=i+j−1<I+Jt=i+j-1<I+J. This convention is adopted throughout the paper unless stated otherwise.

We address the application of reinforcement learning to micro-level reserving through a modular and extensible framework. The reserving problem is first cast as a Markov decision process (MDP) ⟨𝒮,𝒜,𝒫,ℛ,γ⟩\langle\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma\rangle, which formalises claim development as a sequential estimation problem with delayed feedback. Within this representation, an RL agent learns to update outstanding claim liability estimates over time by interacting with transactional claim data. We then specify an appropriate reinforcement learning algorithm for this setting and discuss how its design choices align with actuarial reserving objectives. Finally, the proposed framework should be evaluated empirically to assess its ability to produce accurate and stable claim-level and portfolio-level reserve estimates relative to established benchmarks, and any results fed back into the design of the framework.

![Refer to caption](figs/micro_formulation.png)


Figure 3.1: Illustration of the micro-level reserving formulation in action

### 3.2 Micro-level Framework Design and MDP Formulation

A micro-reserving framework approaches the formulation on the basis of claim-level transactional data. Consequently, this works for reported but not settled (RBNS) claims only. In practice, a settled/closed claim can also reopen. However, we do not consider this possibility in our paper.

To prime our micro-level reserving framework, it is useful to consider an analogy of a chessbot learning from many concurrently occurring games: every move made on every board up to the current time will have contributed to updating the bot’s strategy. Each board would be a realisation of the environment. For reserving, this is very much a similar idea: we can consider each claim to be a game where the objective is to guess the outstanding claims liabilities (OCL) as accurately as possible at each development for claims developing concurrently. There is the added complication that these reserving “games” do not start or finish at the same time. We formalise this in Figure [3.1](https://arxiv.org/html/2601.07637v1#S3.F1 "Figure 3.1 ‣ 3.1 Overarching RL Framework ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving"), which illustrates an example of an insurer with many developing claims in calendar time, with the present time (i.e., valuation period) being the end of calendar period 7. The agent then would have seen the developments of all notified claims up to this time, and can learn from these to predict the OCL for each currently open claim.

A subtle but important point to make clear is that our predictions target the OCL in settlement year dollars (so that base and superimposed inflation are accounted for). To use the OCL was a deliberate choice over targeting the ultimate loss (UL) for technical reasons. In the implementation, we need to specify the bounds for the target. It is easy and clean to specify zero as the lower bound for the OCL, whereas there is no easy way to specify a lower bound for targeting the UL, since this lower bound would naturally be in line with cumulative payments, and those can change at every time step.

A natural question is where “control” arises in our formulation, since the insurer’s reserve estimates do not influence the physical evolution of claims. In our framework, actions do not control claim outcomes; instead, they control the *sequence of estimates* produced by the model.
The action at each development period determines how the previous OCL estimate is updated, and this updated estimate becomes part of the next state observed by the agent. The environment transition is therefore deterministic with respect to the agent’s action, even though claim evolution itself is exogenous. This reframes the problem as *sequential prediction with delayed feedback*, where reinforcement learning is used as a temporal-difference learning mechanism to optimise a sequence of interdependent predictions rather than a physical control system. Such “prediction-as-control” formulations are common in reinforcement learning when the objective is to optimise long-horizon forecasting accuracy under partial and delayed information rather than to intervene in the environment directly. In a more complex setting, one could argue that reserving decisions may have an indirect impact on the state space, but we are not considering this here.

### 3.3 Markov Decision Process (MDP)

We now develop the environment and reward formulations as per the framework described above. Formally, every claim follows an MDP ⟨𝒮,𝒜,𝒫,ℛ,γ⟩\langle\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma\rangle (Howard, [1960](https://arxiv.org/html/2601.07637v1#bib.bib34)), which we develop below. In this section, we focus only on the general, theoretical formulation, and leave specific choices made in the implementation of this paper to Section [4.1](https://arxiv.org/html/2601.07637v1#S4.SS1 "4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving").

Note: Elements of the MDP are indexed by time (since they evolve over time). It is sometimes more convenient to index by the time since notification τ\tau (such as in Figure [3.1](https://arxiv.org/html/2601.07637v1#S3.F1 "Figure 3.1 ‣ 3.1 Overarching RL Framework ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving")), and other times more convenient to index by the development period jj (such as in the formulation below). It will be clear which we are using, but it is useful to keep in mind that the indexing is merely anchoring the MDP to a particular calendar period in time.

###### Remark 3.1.

𝒫\mathcal{P} denotes the underlying environment dynamics (transition probabilities of the Markov Chain). We assume this to be unknown, and do not explicitly estimate them (as is generally standard in RL), so they are not further discussed.

###### Remark 3.2.

This paper formulates the reserving problem in a discrete time, continuous state and continuous action space setting. A discrete action space will also work (as in Dong and Finlay, [2025](https://arxiv.org/html/2601.07637v1#bib.bib24); Moody and Saffell, [2001](https://arxiv.org/html/2601.07637v1#bib.bib49)), and is a simpler problem to solve at the cost of less fine-grained control. If fine-grain control is not necessary, it could make more sense to reduce the complexity of the problem. Although not explored in this paper, this adaptation should be rather simple as one only needs to restrict the action space to a set of discrete values, e.g., 𝒜={−0.10,−0.066,−0.033,0,0.033,0.066,0.10}\mathcal{A}=\{-0.10,-0.066,-0.033,0,0.033,0.066,0.10\} in Dong and Finlay ([2025](https://arxiv.org/html/2601.07637v1#bib.bib24)).

#### 3.3.1 State space 𝒮\mathcal{S}

The state space 𝒮\mathcal{S} contains information about the environment for the agent to observe. There are three things that must be included: the accident period (AP), development period (DP), and the previous OCL estimate. Therefore, the bare minimum state space at development period jj is

|  |  |  |  |
| --- | --- | --- | --- |
|  | {A​P=i,D​P=j,OCL^j−1},\{AP=i,DP=j,\hat{\text{OCL}}\_{j-1}\}, |  | (3.1) |

where OCL^j\hat{\text{OCL}}\_{j} is the OCL predicted at development period jj with OCL^0\hat{\text{OCL}}\_{0} initialisation. Note that the initialisation is quite important, because we can see that at development period j=1j=1, our state space starts with the initialisation value OCL^0\hat{\text{OCL}}\_{0}. This means that the sequential predictions for RL begin with how we choose to initialise it. A naive zero or constant initialisation produces poor results because it is not suitable for claims of different sizes. One can imagine an extreme example in which if a claim with OCL $1000 is initialised at $1 million, then it would be difficult to adjust quickly (because the action space is restricted; refer to the next section). As such, we consider initialisation at length in Section [4.2](https://arxiv.org/html/2601.07637v1#S4.SS2 "4.2 Initialisation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving").

As aforementioned, we must include the previously predicted OCL in the state space so that the environment is designed such that the action taken is an adjustment to the previous prediction. This is to satisfy the requirement of the MDP formulation, whereby actions taken should impact the state; see also the last paragraph of Section [3.2](https://arxiv.org/html/2601.07637v1#S3.SS2 "3.2 Micro-level Framework Design and MDP Formulation ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving"). The inclusion of the accident and development periods is standard and necessary in all reserving models because claim sizes vary between accident periods, and the OCL is, of course, generally decreasing as the claim develops.

It goes without saying that simply using the bare minimum state space in ([3.1](https://arxiv.org/html/2601.07637v1#S3.E1 "In 3.3.1 State space 𝒮 ‣ 3.3 Markov Decision Process (MDP) ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving")) will not yield very good results because it is too simplistic. We discuss our choices for the full state space in Section [4.1](https://arxiv.org/html/2601.07637v1#S4.SS1 "4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving").

#### 3.3.2 Action space 𝒜\mathcal{A}

As we discussed above, we want to design the system such that the action taken by the agent is an adjustment to the previous OCL estimate. We choose to define

|  |  |  |  |
| --- | --- | --- | --- |
|  | OCL^j=OCL^j−1⋅exp⁡(aj),\hat{\text{OCL}}\_{j}=\hat{\text{OCL}}\_{j-1}\cdot\exp(a\_{j}), |  | (3.2) |

where aj∈𝒜a\_{j}\in\mathcal{A} is a scaling factor applied to the previous OCL estimate and the initialisation of OCL^0\hat{\text{OCL}}\_{0} is discussed in Section [4.2](https://arxiv.org/html/2601.07637v1#S4.SS2 "4.2 Initialisation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving").

We define the action space to be 𝒜=[−ln⁡(K),+ln⁡(K)],K∈ℝ\mathcal{A}=[-\ln(K),+\ln(K)],\;K\in\mathbb{R} to (arbitrarily) impose the constraint that in any single development period, the OCL estimate cannot increase or decrease by more than a factor of KK. A constraint of KK is imposed for stability purposes so that the RL agent doesn’t get stuck at low estimates or suddenly explode with a huge OCL estimate when the agent is undertaking exploration.

Treating the action as a scaling factor is an existing approach (e.g. Xu et al., [2019](https://arxiv.org/html/2601.07637v1#bib.bib72)) because it is straightforward and is percentage-change based rather than being based on absolute-dollar-change.
Furthermore, we work in the log-space and then exponentiate so that the action space is symmetrical about zero, with the intention that exploration should not be unbalanced in one direction or the other simply because of the action space definition. A multiplicative action is thus required.

###### Remark 3.3.

KK is a tunable hyperparameter for which there is a tradeoff: for larger KK, there is greater model flexibility at the cost of a larger action space to explore, while for smaller KK, there is a smaller action space to explore, but more constraints in how much the model can adjust estimates per development period. We observed that K=2K=2 often led to better performance than larger values of KK, which introduces a high degree of restrictiveness. However, a larger action space may lead to more instability, and the state space is not rich enough and/or the volume of data is not large enough for the model to learn as well.

To assess the stability of the learned policy, we examined the empirical distribution of actions taken by the trained agent across all claims and development periods; see Figures [G.1](https://arxiv.org/html/2601.07637v1#A7.F1 "Figure G.1 ‣ Appendix G Histograms of actions taken during testing of the RL model ‣ Reinforcement Learning for Micro-Level Claims Reserving") and [G.3](https://arxiv.org/html/2601.07637v1#A7.F3 "Figure G.3 ‣ Appendix G Histograms of actions taken during testing of the RL model ‣ Reinforcement Learning for Micro-Level Claims Reserving") in the Appendix. We find that actions are tightly concentrated around zero (exponentiation of the action concentrated around 1), indicating that the policy predominantly makes small incremental adjustments to OCL estimates. Clipping at the action bounds occurs infrequently during testing (where exploration is turned off). In fact, large adjustments are largely confined to early development periods, where initial uncertainty is highest (see Figures [G.2](https://arxiv.org/html/2601.07637v1#A7.F2 "Figure G.2 ‣ Appendix G Histograms of actions taken during testing of the RL model ‣ Reinforcement Learning for Micro-Level Claims Reserving") and [G.4](https://arxiv.org/html/2601.07637v1#A7.F4 "Figure G.4 ‣ Appendix G Histograms of actions taken during testing of the RL model ‣ Reinforcement Learning for Micro-Level Claims Reserving")). In later development periods, large adjustments are rare, suggesting that the constrained action space primarily acts as a stabilisation device during learning rather than a binding restriction at convergence. These diagnostics support the interpretation that the learned policy operates well within the admissible action range and that the choice of action bounds does not materially distort the learned reserving behaviour.

###### Remark 3.4.

The current action space formulation, where actions are multiplicative adjustments, assumes that the OCL is strictly positive. For circumstances where negative OCLs need to be considered, there are no theoretical reasons why it could not be accommodated. However, an alternative definition for how the action adjusts the previous OCL would be required. This is not further considered in our paper.

#### 3.3.3 Reward signal ℛ\mathcal{R}

ℛ\mathcal{R} is the reward function that the agent seeks to maximise. This is a critical design choice, as it drives how the agent learns. It can be difficult to develop in practice, and will require some trial and error even beyond theoretical grounding. Our reward signal ℛ\mathcal{R} will be a combination of multiple components.

Evidently, there must be a signal for the accuracy of the model’s predictions upon settlement so that the model knows how well it performed for the given claim. However, as the accuracy signal will be very sparse (only available upon settlement of the claim), the model will find it difficult to converge to an optimal policy. Furthermore, we encourage stable evolutions in the model’s prediction of ultimate loss (UL) over time (calculated as the sum of the predicted OCL and cumulative paid) by rewarding small adjustments over large adjustments. This imposes a cost to large adjustments to the implicit UL, so the agent would not do this unless it has high “confidence”. This is a desirable property for a reserving model from a financial management perspective, but also, it allows for denser reward signals during the development of the claim, which helps learning.

While the specific reward formulas are given in Section [4.1.2](https://arxiv.org/html/2601.07637v1#S4.SS1.SSS2 "4.1.2 Reward function ℛ ‣ 4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving"), we will use the following analogy to tease out our main ideas. Suppose we are training an RL agent to play chess. Just like how we want to correctly predict a claim, we want the chess bot to win games. Therefore, upon the end of a game, we can assign a reward of +1+1 for a win, −1-1 for a loss, and 0 for a draw. However, with only this reward signal at the end of the game, it can be difficult for the agent to “understand” how it won. That is, what moves were good and what moves were bad. In this sense, we may employ some human knowledge about the underlying theory of the game of chess to create intermediary rewards during the course of a game to reward “good” moves and penalise “bad” moves with, say, +/−0.5+/-0.5 respectively. In the same way, we reward stability of estimates for our reserving model.

There are many possible reward signals that would be available in practice for a reserving model. Inclusion of covariates into the model could allow for many informative reward signals.
Additionally, case estimates make for useful proxies of the true unknown OCL, with which we can build denser reward signals before the claim is settled.

#### 3.3.4 Discount γ\gamma

The discount factor γ\gamma can be chosen or tuned. In practice, this may be determined by risk appetite rather than tuning, as it reflects how much we value correct predictions early compared to later. In our context, correct predictions are valuable at all times, but more so early when there is more OCL at stake. This translates to a large but less than 1 value for γ\gamma.

### 3.4 Description of one iteration

We describe here one iteration of learning from calendar period tt to t+1t+1 for a single claim. This is a walkthrough of the learning process for a single claim in Figure [3.1](https://arxiv.org/html/2601.07637v1#S3.F1 "Figure 3.1 ‣ 3.1 Overarching RL Framework ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving"). We provide a concrete numerical example of this process in [F](https://arxiv.org/html/2601.07637v1#A6 "Appendix F Example of Iteration through State Space ‣ Reinforcement Learning for Micro-Level Claims Reserving"), based on our choices outlined in Section [4.1](https://arxiv.org/html/2601.07637v1#S4.SS1 "4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving").

Assume we are currently in calendar period tt. Let Cn​(t,in)C\_{n}(t,i\_{n}) denote claim nn with accident period ini\_{n} at development period jn:=t+1−inj\_{n}:=t+1-i\_{n}. Steps are then as follows:

1. 1.

   The agent observes the current state space {A​P=in,D​P=jn,OCL^jn−1,…}\{AP=i\_{n},DP=j\_{n},\hat{\text{OCL}}\_{j\_{n}-1},...\};
2. 2.

   The agent takes an action ajna\_{j\_{n}} based on the state space observed, that is, the predicted OCL at development period jnj\_{n} becomes OCL^jn=OCL^jn−1⋅exp⁡(ajn)\hat{\text{OCL}}\_{j\_{n}}=\hat{\text{OCL}}\_{j\_{n}-1}\cdot\exp(a\_{j\_{n}});
3. 3.

   The agent then receives a reward signal rjnr\_{j\_{n}} for its prediction of OCL^jn\hat{\text{OCL}}\_{j\_{n}};
4. 4.

   Then, at the next development period jn+1j\_{n+1}, the agent observes the state space {A​P=in+1,D​P=jn+1,OCL^jn,…}\{AP=i\_{n+1},DP=j\_{n+1},\hat{\text{OCL}}\_{j\_{n}},...\} and the cycle repeats.

###### Remark 3.5.

Given there are adverse financial consequences to inaccurate estimates, once the insurer has a reasonably trained model M1M\_{1} at present calendar period tt to deploy, they may choose to exploit model M1M\_{1} deterministically (as opposed to allowing exploration) at calendar period t+1t+1 and beyond. However, this would mean M1M\_{1} lose the ability to learn from the new incoming data since we are no longer exploring. We briefly describe some possible ways to get around this.

First, the simplest workaround is to run 2 parallel agents/models. When a model M1M\_{1} is to be frozen for deployment, duplicate it, and the clone M2M\_{2} will continue to be able to explore and learn from the incoming data. The agent and its clone will then be periodically evaluated, and the production agent can be replaced if the clone starts to perform better. The drawback of this approach is that subtle shifts in underlying dynamics may take too long to manifest as a noticeable difference in performance between the production agent and its clone. There will need to be a certain level of judgment as to when the clone should replace its original.

Alternatively, one could define a tight set of constraints to allow exploration in some tolerably safe manner to address the issue of timeliness, at the cost of taking on some risk of exploration.

Though not explored further in this paper, these are worthwhile to investigate in future work.

## 4 Implementational Choices

In this section, we discuss important and nuanced topics regarding the choices involved in the MDP formulation, how to initialise the model at the start of a claim, and which RL algorithm to use.

### 4.1 Choices in the MDP Formulation

This section continues on from the development of the MDP in Section [3.2](https://arxiv.org/html/2601.07637v1#S3.SS2 "3.2 Micro-level Framework Design and MDP Formulation ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving") and develops the key choices involved in the MDP formulation.

#### 4.1.1 State space 𝒮\mathcal{S}

We augment the bare minimum state space of accident period, development period, and previous OCL prediction with the following additions to the state space are derived from the information available to us at each point in time for a claim’s development; see [C](https://arxiv.org/html/2601.07637v1#A3 "Appendix C Data Description ‣ Reinforcement Learning for Micro-Level Claims Reserving") for a description of the data we used. Firstly, for the CAS data:

* 1.

  PjP\_{j} is the cumulative amount paid by development period jj
* 2.

  repdel=⌈notification time⌉−A​P\text{repdel}=\lceil\text{notification time}\rceil-AP is the claim’s reporting delay. This is potentially an important predictor because it may be the case that claims with longer reporting delays can have larger claim sizes.
* 3.

  past predictionsj\text{past predictions}\_{j} is the (up to) past nn predictions made by the model (where nn is tunable), with zero-padding when there are less than nn previous predictions. We remark that the nn past predictions are not necessary, but rather an extension we tested and found to slightly improve performance. This is easily implemented for RL, but not implemented for FNN, which is another minor technical advantage of RL being a sequential approach.

Therefore, the state space at development period jj is

|  |  |  |  |
| --- | --- | --- | --- |
|  | {A​P=i,D​P=j,OCL^j−1,Pj,repdel,past predictionsj}\{AP=i,DP=j,\hat{\text{OCL}}\_{j-1},P\_{j},\text{repdel},\text{past predictions}\_{j}\} |  | (4.1) |

The SPLICE data allows for a richer state space, as it contains case estimates, and allows us to set the time unit to quarters rather than years. It has the following additions to the state space

* 1.

  txn\_typesj\text{txn\\_types}\_{j} are the (one-hot-encoded) transaction types for transactions that occurred in development period jj.
* 2.

  njpayn\_{j}^{\text{pay}} is the number of payments made so far by development period jj, with n1pay=0n\_{1}^{\text{pay}}=0.
* 3.

  AQ∈{1,2,3,4}\text{AQ}\in\{1,2,3,4\} is the quarter of the year of the accident period. The idea of including the quarter of the accident period is that it could capture any cyclical differences in claim mixtures that would not be detectable with just the accident period. Note that we are working with quarters as the time unit in our implementation, but this can be generalised to an arbitrary time unit easily.
* 4.

  DQj∈{1,2,3,4}\text{DQ}\_{j}\in\{1,2,3,4\} is the quarter of the current development period jj. The idea here is similar as that of AQ; it can help capture any cyclical differences in claim development patterns.
* 5.

  casej\text{case}\_{j} is the case estimate of the OCL at development period jj.

Therefore, the state space at development period jj for the SPLICE data in general is

|  |  |  |  |
| --- | --- | --- | --- |
|  | {A​P=i,D​P=j,OCL^j−1,txn\_typesj,Pj,repdel,njpay,AQ,DQj,past predictionsj,casej}\{AP=i,DP=j,\hat{\text{OCL}}\_{j-1},\text{txn\\_types}\_{j},P\_{j},\text{repdel},n^{\text{pay}}\_{j},\text{AQ},\text{DQ}\_{j},\text{past predictions}\_{j},\text{case}\_{j}\} |  | (4.2) |

However, for complexity 1, the SPLICE-generated data is simple and consistent with chain-ladder assumptions; therefore, such a state space is too complex and leads to subpar results. Instead, we reduce the state space to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {A​P=i,D​P=j,OCL^j−1,Pj}\{AP=i,DP=j,\hat{\text{OCL}}\_{j-1},P\_{j}\} |  | (4.3) |

###### Remark 4.1.

While signals like covariates and case estimates are easy to include here in the state space without much thought, there are many possible ways to make use of them in the design of the RL framework, such as inclusion in the state space or the reward space or both, and it is not obvious what the best approach would be.
We have chosen to leave the inclusion of such additional reward signals to future work so that our formulation remains as foundational as possible, and to keep the paper to a reasonable length.

Nevertheless, our formulation and implementation without these additional informative reward signals already performs remarkably well on simulated data. It is likely that this performance could be further improved.

#### 4.1.2 Reward function ℛ\mathcal{R}

Finally, we discuss the components of the reward function ℛ\mathcal{R} that the agent seeks to maximise. From a reserving perspective, the reward is designed to encourage reserve revisions that are accurate at settlement, while avoiding unnecessary volatility during periods with no new payment information. In particular, reserve changes are penalised unless justified by observed claim activity, reflecting the practical preference for stable reserves that adjust primarily when payments occur.

To construct reward terms, we will use the function h​(y,y^)=1−g​(y,y^)h(y,\hat{y})=1-g(y,\hat{y}) (yy is the actual value, y^\hat{y} is the predicted value), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(y,y^)=|y^−y|(|y|+|y^|)/2g(y,\hat{y})=\frac{\lvert\hat{y}-y\rvert}{(\lvert y\rvert+\lvert\hat{y}\rvert)/2} |  | (4.4) |

is the summand of the sMAPE metric (symmetric mean absolute percentage error), and is used because it penalises under- and over-estimation equally (symmetry) and it is also bounded, which is desirable for RL reward formulations. The function hh simply maps gg to [−1,1][-1,1], which is preferable for RL.

The reward signal consists of an accuracy component calculated at settlement time τ=Tn\tau=T\_{n}, as well as stability and smoothing components calculated in periods before settlement τ=1,…,Tn−1\tau=1,...,T\_{n}-1. The high-level idea is that the accuracy component rewards how good the predictions were at each development period, the stability component rewards the agent the more it keeps its implied ultimate loss estimate stable, and the smoothing component, which progressively penalises large adjustments/actions in later periods to encourage the agent to “make up its mind” early rather than leaving it till later.

* 1.

  Accuracy component raccr\_{\text{acc}}: At settlement of the claim nn (τ=Tn)(\tau=T\_{n}), We have

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | racc=C⋅∑τ=1Tn−1γτ−1⋅h​(OCLτ,OCL^τ)∑τ=1Tn−1γτ−1,r\_{\text{acc}}=C\cdot\frac{\sum\_{\tau=1}^{T\_{n}-1}\gamma^{\tau-1}\cdot h\left(\text{OCL}\_{\tau},\hat{\text{OCL}}\_{\tau}\right)}{\sum\_{\tau=1}^{T\_{n}-1}\gamma^{\tau-1}}, |  | (4.5) |

  where OCLτ\text{OCL}\_{\tau} is the true OCL, and OCL^τ\hat{\text{OCL}}\_{\tau} is the predicted OCL as at τ\tau periods since notification. The reason we divide by ∑τ=1Tn−1γτ−1\sum\_{\tau=1}^{T\_{n}-1}\gamma^{\tau-1} is to remove the imbalance of signal strength for longer vs shorter claims since notification. Just because a claim has been developing for a long time since notification doesn’t mean it should be more important than a claim that hasn’t been developing for a long time since notification.

  Note that intermediate true OCL values cannot be observed. As a consequence, raccr\_{\text{acc}} is evaluated at settlement using realised payments and the ultimate claim amount, and interpreted as a terminal reward that attributes estimation accuracy backward to the full prediction path OCL^1:Tn−1\hat{\mathrm{OCL}}\_{1:T\_{n}-1}. The formulation above should therefore be understood as a path-based accuracy reward evaluated ex post, rather than as requiring intermediate targets in practice.

  In implementation, we multiply raccr\_{\text{acc}} by a (tuned) factor of CC to increase the size of the accuracy component relative to the subsequent smoothing and payment components.
* 2.

  Stability component rstab,τr\_{\text{stab},\tau}: We have, for claim nn,

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | rstab,τ\displaystyle r\_{\text{stab},\tau} | =\displaystyle= | −αstab,τ​(|aτ|ln⁡K)2,τ=1;\displaystyle-\alpha\_{\text{stab},\tau}\left(\frac{|a\_{\tau}|}{\ln K}\right)^{2},\quad\tau=1; |  | (4.6) |
  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  |  | =\displaystyle= | αstab,τ​[γ​h​(UL^τ,UL^τ−1)−h​(UL^τ−1,UL^τ−2)],τ=2,…,Tn−2;\displaystyle\alpha\_{\text{stab},\tau}\left[\gamma h\left(\hat{\text{UL}}\_{\tau},\hat{\text{UL}}\_{\tau-1}\right)-h\left(\hat{\text{UL}}\_{\tau-1},\hat{\text{UL}}\_{\tau-2}\right)\right],\quad\tau=2,...,T\_{n}-2; |  | (4.7) |
  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  |  | =\displaystyle= | αstab,τ​[0−h​(UL^τ−1,UL^τ−2)],τ=Tn−1.\displaystyle\alpha\_{\text{stab},\tau}\left[0-h\left(\hat{\text{UL}}\_{\tau-1},\hat{\text{UL}}\_{\tau-2}\right)\right],\quad\tau=T\_{n}-1. |  | (4.8) |

  where

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | αstab,τ={1,if there is no payment in period ​τ;0,if there are payments in period ​τ.\alpha\_{\text{stab},\tau}=\begin{cases}1,&\text{if there is no payment in period }\tau;\\ 0,&\text{if there are payments in period }\tau.\end{cases} |  | (4.9) |

  The first ([4.6](https://arxiv.org/html/2601.07637v1#S4.E6 "In item 2 ‣ 4.1.2 Reward function ℛ ‣ 4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving")) ∈[−1,0]\in[-1,0] discourages overly large movements at the onset (recall that KK defined the action space bounds). The expression in square brackets in ([4.7](https://arxiv.org/html/2601.07637v1#S4.E7 "In item 2 ‣ 4.1.2 Reward function ℛ ‣ 4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving")) follows the potential-based reward-shaping formulation proposed by Ng et al. ([1999](https://arxiv.org/html/2601.07637v1#bib.bib51)), such that when added to the accuracy component of the reward, it will not change the optimal policy under only the accuracy reward component, since it cancels out as a telescoping sum; see also ([4.8](https://arxiv.org/html/2601.07637v1#S4.E8 "In item 2 ‣ 4.1.2 Reward function ℛ ‣ 4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving")). As such, this is simply a reward shaping term that helps the agent reach the optimal policy more efficiently. Note that rstab,τr\_{\text{stab},\tau} is formulated in terms of UL rather than OCL, as UL does not change over time, whereas OCL does.

  Operationally, this means that the agent is discouraged from revising reserves in quiet development periods, while being allowed to react more aggressively when payments provide new information.

  ###### Remark 4.2.

  The stability reward is motivated by potential-based reward shaping (Ng et al., [1999](https://arxiv.org/html/2601.07637v1#bib.bib51)), in which differences of a potential function are added to the reward without altering the optimal policy. In our setting, however, the stability term is multiplied by a gating factor αstab\alpha\_{\text{stab}} that switches off once claim payments occur. This modification breaks the strict theoretical invariance guarantees of potential-based shaping. We therefore use the shaping interpretation heuristically: the stability term is designed to improve empirical learning stability and prevent erratic reserve revisions in early development periods, rather than to preserve policy invariance in a formal sense.
* 3.

  Smoothing component rsmooth,τr\_{\text{smooth},\tau}: At development periods τ=1,2,…,Tn−1\tau=1,2,...,T\_{n}-1 for claim nn,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | rsmooth,τ=−αsmooth,τ⋅(|aτ|ln⁡K)2,αsmooth,τ={min⁡(1,m+1M),if there is no payment in period ​τ;0,if there are payments in period ​τ.r\_{\text{smooth},\tau}=-\alpha\_{\text{smooth},\tau}\cdot\left(\frac{|a\_{\tau}|}{\ln K}\right)^{2},\quad\alpha\_{\text{smooth},\tau}=\begin{cases}\min(1,\frac{m+1}{M}),&\text{if there is no payment in period }\tau;\\[4.0pt] 0,&\text{if there are payments in period }\tau.\end{cases} |  | (4.10) |

  where mm is the number of predictions made for the claim since notification, and MM is the tuned number of warm-up steps. While the agent tries to maximise the large but delayed lump-sum reward raccr\_{\text{acc}}, rsmoothr\_{\text{smooth}} encourages more stability in its adjustments by penalising any action, with less penalty on smaller actions through a quadratic reward term. However, we want to remove this penalty whenever there is a payment, so that the agent is free to make adjustments without penalty. Moreover, αsmooth\alpha\_{\text{smooth}} ramps up from 0 to 11 over the first MM predictions so that the agent is encouraged to settle near the correct UL estimate early, so that it doesn’t need to adjust much later on.

Both the stability reward rstabr\_{\text{stab}} and the smoothing penalty rsmoothr\_{\text{smooth}} discourage abrupt changes in predicted OCL, but they operate at different levels. The stability term penalises deviations relative to a reference ultimate loss estimate, whereas the smoothing term penalises period-to-period variability and enforces temporal regularity in the prediction path, that is, it increases the resistance to taking action (adjusting OCL) in later claim developments.

#### 4.1.3 Discount factor γ\gamma

The discount factor γ=0.99\gamma=0.99 is arbitrarily chosen so that we value correct predictions now slightly more than correct predictions in the future, but not by too much; refer to ([2.1](https://arxiv.org/html/2601.07637v1#S2.E1 "In item 1 ‣ 2.1 Overview ‣ 2 Introduction to Reinforcement Learning ‣ Reinforcement Learning for Micro-Level Claims Reserving")) and Section [3.3.4](https://arxiv.org/html/2601.07637v1#S3.SS3.SSS4 "3.3.4 Discount 𝛾 ‣ 3.3 Markov Decision Process (MDP) ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving").

#### 4.1.4 Example

An example of calculations over the full length of one claim, as well as for an iteration of learning, is provided in [F](https://arxiv.org/html/2601.07637v1#A6 "Appendix F Example of Iteration through State Space ‣ Reinforcement Learning for Micro-Level Claims Reserving").

### 4.2 Initialisation

Initialisation of the RL model is an important aspect of the implementation. A poor initialisation can destabilise training and lead to the model failing to learn in time.

In practice, the reserving actuary will either have case estimates available as an initial value, or an estimate derived from the underwriting process (e.g., premium and expected loss ratio). Insurers generally have an a priori estimate of the expected cost of claims associated to a policy when they sell it.

However, as we are working with synthetic data, we don’t have access to these priors. They may also be costly to obtain or derive. Hence, we develop an initialisation scheme based on historical data only. We develop a linear-credibility-like approach (similar to Bornhuetter and Ferguson ([1972](https://arxiv.org/html/2601.07637v1#bib.bib13)), but using an overall mean in place of an arbitrary prior) to initialise a claim with accident period ii using historical data of all claims settled by valuation calendar period of TT. The historical data consists of all available settled training claims.

#### 4.2.1 Credibility mixing

The idea is that we want to get an accident-period-specific mean ULi0{}\_{0}\text{UL}\_{i} by mixing the empirical (individual) mean of the accident period UL¯i​Σ\bar{\text{UL}}\_{i\Sigma} (row in a claims triangle), with the overall (collective) mean UL¯Σ​Σ\bar{\text{UL}}\_{\Sigma\Sigma} (whole triangle):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ULi0=zi​UL¯i​Σ+(1−zi)​UL¯Σ​Σ,{}\_{0}\text{UL}\_{i}=z\_{i}\bar{\text{UL}}\_{i\Sigma}+(1-z\_{i})\bar{\text{UL}}\_{\Sigma\Sigma}, |  | (4.11) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | UL¯Σ​Σ=∑i=1Iwi​UL¯i​Σ,wi=ninsettled training claims=no. settled training claims from accident period ​ino. settled training claims.\bar{\text{UL}}\_{\Sigma\Sigma}=\sum\_{i=1}^{I}w\_{i}\bar{\text{UL}}\_{i\Sigma},\quad w\_{i}=\frac{n\_{i}}{n\_{\text{settled training claims}}}=\frac{\text{no. settled training claims from accident period }i}{\text{no. settled training claims}}. |  | (4.12) |

In practice, the actuary could replace UL¯Σ​Σ\bar{\text{UL}}\_{\Sigma\Sigma} with their a priori estimate of the ultimate claim size; we use ([4.12](https://arxiv.org/html/2601.07637v1#S4.E12 "In 4.2.1 Credibility mixing ‣ 4.2 Initialisation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving")). The actuary may even use their a priori estimate to initialise ULi0{}\_{0}\text{UL}\_{i} directly.

The “credibility” weight ziz\_{i} should be large for earlier accident periods when we have more settled claims in the training set (more data, hence more credible), and decrease for later accident periods, where there may only be a few settled claims and so we must rely on the overall mean. Such an objective can be achieved by using the formula from Taylor ([2000](https://arxiv.org/html/2601.07637v1#bib.bib64))

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi=1πi,z\_{i}=\frac{1}{\pi\_{i}}, |  | (4.13) |

where πi\pi\_{i} is the (chain ladder) age-to-ultimate factor for claims with accident period ii at the valuation period TT for a cumulative paid triangle. Earlier accident periods will have smaller πi\pi\_{i} at valuation period TT, and hence larger credibility ziz\_{i}.

#### 4.2.2 Adjustment to claims mix

The credibility factor ([4.13](https://arxiv.org/html/2601.07637v1#S4.E13 "In 4.2.1 Credibility mixing ‣ 4.2 Initialisation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving")) stems from a vanilla chain ladder estimation procedure, which can present issues. A feature of the simulated data we use in this paper (outlined in Section [8.2](https://arxiv.org/html/2601.07637v1#S8.SS2 "8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving")) is that longer claims progressively become larger in size over time, even in real terms. This is a problem because claims with later accident periods in the settled training set will tend to be biased towards claims that settle quickly, and hence may grossly under-represent the potential size of the claim being initialised. This issue of a changing mix of claims leads to worse and worse underestimation for later accident period claims. It should be noted that the issue here is not necessarily that the initialisation is bad, but rather that the initialisation deteriorates for more recent accident periods, and we can’t expect RL to pick up on that since it’s a feature of how the data was split. To address this issue, we adapt the PPCI (payments per claim incurred) triangle of Taylor ([2000](https://arxiv.org/html/2601.07637v1#bib.bib64)):

1. 1.

   Using the training set of settled claims by valuation period TT, we construct a PPCI triangle of average claim amounts. Rather than the cumulative paid amount in each cell, we have the payments per claim incurred by dividing Ci,jC\_{i,j} by the number of claims incurred to date Ni,jN\_{i,j}.
2. 2.

   For each AP ii in the PPCI triangle, we have an age-to-ultimate factor for the PPCI triangle πi′\pi^{\prime}\_{i} (where ′ is to differentiate from the cumulative paid triangle’s age-to-ultimate factor from earlier), which “develops” the PPCI to an ultimate level. We can use this to “correct” for the difference in mixture of claims. Specifically,

   * (a)

     The AP mean should be adjusted to UL¯i​Σadj=πi′⋅UL¯i​Σ\bar{\text{UL}}\_{i\Sigma}^{\text{adj}}=\pi^{\prime}\_{i}\cdot\bar{\text{UL}}\_{i\Sigma}
   * (b)

     The overall mean UL¯Σ​Σ\bar{\text{UL}}\_{\Sigma\Sigma} should also be adjusted to

     |  |  |  |  |
     | --- | --- | --- | --- |
     |  | UL¯Σ​Σadj=1ntraining claims​∑i=1Iπi′⋅ULi​Σ.\bar{\text{UL}}\_{\Sigma\Sigma}^{\text{adj}}=\frac{1}{n\_{\text{training claims}}}\sum\_{i=1}^{I}\pi^{\prime}\_{i}\cdot\text{UL}\_{i\Sigma}. |  | (4.14) |

The initialisation now becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ULi0=zi⋅UL¯i​Σadj+(1−zi)​UL¯Σ​Σadj,{}\_{0}\text{UL}\_{i}=z\_{i}\cdot\bar{\text{UL}}\_{i\Sigma}^{\text{adj}}+(1-z\_{i})\bar{\text{UL}}\_{\Sigma\Sigma}^{\text{adj}}, |  | (4.15) |

and OCLi0{}\_{0}\text{OCL}\_{i} is simply ULi0{}\_{0}\text{UL}\_{i} minus the cumulative paid at notification.

If ULi0{}\_{0}\text{UL}\_{i} is less than the cumulative paid, then OCLi0<0{}\_{0}\text{OCL}\_{i}<0, which would condemn the RL algorithm to negative predictions forever after. Hence, we pragmatically initialise with a small (but not too small) UL¯Σ​Σadj/K2\bar{\text{UL}}\_{\Sigma\Sigma}^{\text{adj}}/K^{2}, where KK is the action space constraint. Essentially, this allows RL, in two periods, to scale the claim to get back to the average adjusted ultimate loss in two periods, or down to something really small.

###### Remark 4.3.

The estimate ULi0{}\_{0}\text{UL}\_{i} could potentially be used to calculate an IBNR estimate in conjunction with a projection of counts, in a fashion similar to PPCI. This is a very rudimentary idea that is in line with how IBNRs are estimated for micro-level reserving in general, that is, by multiplying an expected severity by (expected) IBNR claim counts (e.g., Antonio and Plat, [2012](https://arxiv.org/html/2601.07637v1#bib.bib2); Avanzi et al., [2015](https://arxiv.org/html/2601.07637v1#bib.bib10)).

### 4.3 RL Algorithm Choice

The PPO and SAC algorithms described in [2](https://arxiv.org/html/2601.07637v1#S2 "2 Introduction to Reinforcement Learning ‣ Reinforcement Learning for Micro-Level Claims Reserving") both support a continuous action space. The most significant difference is that PPO is an on-policy algorithm, while SAC is off-policy. This means that the SAC is able to keep a replay buffer of past experience, which makes it more sample efficient. Given that we are working with potentially limited data for reserving purposes, we decided to use the SAC algorithm.

## 5 Data Splitting for Evaluation and Tuning

In this section, we thoroughly develop the procedure of splitting the data for validation and testing purposes. This results in a novel approach born from the intersection of RL and micro-level reserving.

Traditionally, RL does not have a concept of train-test-split. There usually is no need to carefully define a training, validation and test set because RL applications often stem from games or other contexts where data scarcity is not a concern. In contrast, reserving data is often scarce. Moreover, the reserving “game” faces changing rules (claims characteristics and their payment patterns) over time. Therefore, we needed to develop our own bespoke approach, called “rolling settlement”, because existing approaches in the reserving literature for splitting the data either do not respect the temporal nature of the data, or do not utilise RL’s advantage of being able to learn from open (yet to settle) claims.

There are really two (related) splitting procedures to discuss in this section. Focusing on model evaluation (on a test set) first, we precisely define and discuss the existing techniques for splitting the overall data into a training and test set that we are aware of. We are unaware of such a comprehensive summary and comparison in the existing literature. Focusing on hyperparameter tuning next, we explain and argue that none of the existing techniques used in reserving are appropriate for RL hyperparameter tuning. Consequently, we develop a new approach, which we have called “rolling settlement”.

### 5.1 Train-Test-Split for Model Evaluation

Let us first define a list of data splitting techniques for ease of comparison and reference in Table [5.1](https://arxiv.org/html/2601.07637v1#S5.T1 "Table 5.1 ‣ 5.1 Train-Test-Split for Model Evaluation ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving").

Table 5.1: Splitting Approaches: given nn claims in a dataset, possible ways to partition the claims

|  |  |
| --- | --- |
| Splitting Technique | Description |
| Naïve Split by Claim (NSC) | Randomly split the nn claims into kk groups (e.g., by claim ID). This ignores the temporal nature of development and leads to data leakage. For example, if k=2k=2 such that we naively split the data into a training and test set in this way, the training set would include information (e.g., the ultimate loss) that in practice would be from the future, and so would be unrealistic. |
| Censored Split by Claim (CSC) | First split by calendar time into kk groups; within each group keep only claims that settle by the end of that group. Example: if calendar periods [1,80][1,80] are split into [1,40][1,40] and [41,80][41,80], then claims settling within [1,40][1,40] form the training set, while the rest form the test set. |
| Temporal Split (TS) | A temporal split involves splitting by calendar time into kk groups, similar to the CSC, but this time, the developments of a claim are assigned to the calendar time that it falls into. For example, a claim with accident period 3535 settling in period 5050 contributes its developments up to 4040 to the training set [1,40][1,40], while developments in [41,50][41,50] belong to the test set. |

The key distinction between CSC and TS is that when targeting the OCL, the former is suitable for supervised methods, while the latter is suitable for RL such that a claim can be partitioned and attributed to multiple splits. TS is natural for RL because it takes advantage of RL’s ability to learn from still-developing claims (whereas they are useless for supervised methods as the target is unknown). CSC is suitable for supervised methods targeting the OCL, but not for RL, since it removes open claims and hence does not allow RL to work with the still-open claims. To the best of our knowledge, in the current literature, TS is seen only when targeting a sequence of payments rather than the OCL.

For our approach in this work, we construct the train and test set by splitting the overall data using a TS for RL, and a CSC for the feed-forward neural network. Formally, let t=1t=1 denote the accident period of the earliest claim (calendar period 1), and t=Mt=M denote the accident period of the latest starting claim in the dataset (calendar period MM) and N≥MN\geq M to be the latest possible calendar period observed (determined by the maximum observation periods after accident), so that all claims start in a calendar period t∈{1,2,…,M}t\in\{1,2,...,M\}, and have settled by calendar period NN. For our dataset, M=40M=40 and NN is technically unbounded. We decide that the time interval {1,2,…,M}\{1,2,...,M\} will constitute the training set, and {M+1,…,N}\{M+1,...,N\} will constitute the test set. That is, we are pretending that the insurer is currently at calendar period M=40M=40, and would like to predict the OCL for all open claims at the current time.

### 5.2 Rolling Settlement Approach to Hyperparameter Tuning

We next consider data splitting for the purposes of hyperparameter tuning. The innovation of this section is to motivate and develop the extension of temporal splitting to incorporate validation, not just train-test-split. We first discuss what is done in the RL literature, then consider several alternatives from the reserving literature and why they are not suitable for us, and finally, we present the rolling settlement approach that we use for our RL reserving model.

###### Remark 5.1.

“Validation” in this section pertains to hyperparameter tuning purposes. This is not to be confused with validation for variance reduction purposes to prevent supervised methods from overfitting over too many training epochs. We will discuss early stopping after developing the rolling settlement approach for hyperparameter tuning purposes.

#### 5.2.1 Validation in the RL Literature

Hyperparameter tuning is generally an afterthought in the RL literature, because many problems being tackled (e.g., games and robotics) are such that the cost of interacting with the environment is negligible (or there are simulations of the environment). In these cases, multiple agents with different hyperparameter combinations are trained on different instances of the environment (different seeds), and the highest average performance configuration is chosen (Schulman et al., [2017b](https://arxiv.org/html/2601.07637v1#bib.bib57); Haarnoja et al., [2018](https://arxiv.org/html/2601.07637v1#bib.bib32)).

There are also some other novel approaches like population-based training (Jaderberg et al., [2017](https://arxiv.org/html/2601.07637v1#bib.bib35)), and meta-gradient approaches (Xu et al., [2018](https://arxiv.org/html/2601.07637v1#bib.bib73)) that could be explored, but we have decided to leave this for potential future work, as this is not the central focus of this paper.

#### 5.2.2 Validation in the Reserving Literature

Cross-Validation (CV)

Traditionally, for non-time-series data, one performs kk-fold cross-validation for hyperparameter tuning (Kohavi, [1995](https://arxiv.org/html/2601.07637v1#bib.bib36)). This approach would involve a naive split into kk groups called folds, iterating through each fold as the validation set, training on the remaining k−1k-1 folds, and taking the average loss through all folds as the score for a given hyperparameter configuration.

However, this uses the NSC approach, which leads to temporal leakage.

Furthermore, cross-validation would split the training set into folds by claim ID or transaction rather than time, which isn’t the same problem as what we are tackling in reality. In reality, we want to use *past* claims data to predict the current OCL (*future* payments). This inherently motivates a temporal split. However, cross-validation necessitates a split by training observation (claim ID or transaction time), which means that the problem is actually using some claims data to predict other claims, without respecting the temporal nature of the claims. Because of this mismatch, this would mean the best hyperparameter combination we find is not guaranteed to actually be best for the real problem at hand, even notwithstanding the bigger issue of temporal leakage.

This issue motivates the next approach of censored hold-one-out validation.

Censored Hold-One-Out Validation (CHOOV)

To alleviate these issues, one may consider splitting the training set by claim settlement time as in the CSC approach. The entire calendar time of the training set {1,2,…,M}\{1,2,...,M\} is partitioned into two parts by time t1t\_{1}. That is, claims that settle in {1,…,t1}\{1,...,t\_{1}\} comprise the training set and {t1+1,M}\{t\_{1}+1,M\} comprise the validation set. This is essentially applying the CSC technique twice. In this way, no future information is leaked to the past splits. Avanzi et al. ([2025](https://arxiv.org/html/2601.07637v1#bib.bib5)) adopt this approach.

Specifically, we illustrate how this would look for RL and supervised learning methods to help build up to the rolling settlement approach:

* 1.

  For supervised methods, it is a straightforward CSC, where only claims settled in [0,t1][0,t\_{1}] comprise the training set. If a training claim settles over 10 development periods, then it contributes 10 samples to the training set. Once the model is trained, it is fed claims development data spanning [0,t1][0,t\_{1}] for claims that settle in (t1,M](t\_{1},M]. This is repeated for different hyperparameter combinations, and the best-performing combination is selected.
* 2.

  For RL, the difference lies in that we can extend the hold-one-out validation approach to use TS. The training set now contains all claim developments taking place during [0,t1][0,t\_{1}] rather than only the claims that settle during this time, since the model is able to learn without needing a target. The ensuing steps remain the same.

However, taking this approach sacrifices the averaging of folds that CV does, which may make the hyperparameter tuning less robust.

Note that the “one” held out here refers to *one fold* being held out and used for validation, not that one claim is being held out.

Rolling Origin Validation (ROV)

The rolling origin validation approach (Tashman, [2000](https://arxiv.org/html/2601.07637v1#bib.bib63)) respects the temporal ordering of time series data. Suppose the full calendar time of the dataset [1,N][1,N] is split such that the training set comprises claims starting in [1,t∗][1,t^{\*}] (t∗=Mt^{\*}=M from our earlier notation is often called the valuation date, but in the context of rolling origin, t∗t^{\*} is often used). The approach starts by defining an initial training “window” (or fold 1), as [1,t0][1,t\_{0}] with t0<t∗t\_{0}<t^{\*}, to be used to fit the model. Then (t0,t∗](t\_{0},t^{\*}] is used to validate.

Then, for the expanding window approach, for fold ii, train on [1,t0+w​(i−1)][1,t\_{0}+w(i-1)], where ww is the width of each window expansion. Correspondingly, validate on (t0+w​(i−1),t∗](t\_{0}+w(i-1),t^{\*}]. The average loss across all folds is then used to choose the best hyperparameter configuration.

There is also a sliding window approach, where the width of the training window is fixed, and slides along rather than expanding for each fold.

This approach is, however, only used with aggregate triangles in the literature (Balona and Richman, [2020](https://arxiv.org/html/2601.07637v1#bib.bib11); Al-Mudafer et al., [2022](https://arxiv.org/html/2601.07637v1#bib.bib1)). Hence, “origin” refers to the origin of payments in the triangle (diagonals), rather than the origin of claims (rows). Each successive “fold” includes new diagonal(s) compared to the previous fold in the training set, such that we effectively “roll forward” in time. This makes sense in an aggregate triangles context, but for our micro-level reserving problem where we are working at a claims-level, “origin” can only refer to either the accident period or the period of notification for the claim. In both cases, we cannot split based on the “origin” of the claim, because it does not consider the future developments of the claim. This motivates development of a rolling *settlement* approach.

#### 5.2.3 Rolling Settlement Validation (RSV)

The idea of the ROV approach is suitable for our purposes, except that in the micro-level reserving context, it makes sense to split by the settlement time rather than the “origin” (accident period or period of notification), so that we respect the development of the full claim instead of just when it originated. Hence, we term our approach Rolling Settlement Validation (RSV) instead.

The idea of rolling settlement is essentially repeated applications of TS in the case of RL, and CSC for supervised methods.

For the train-test-split, recall that we have decided to split the entire calendar time of the dataset [0,N][0,N] into the training set [0,M][0,M] and the test set (M,N](M,N]. For our dataset, M=40M=40. The goal now is to describe the rolling settlement approach, which acts on the training set.

We can partition the training time interval [0,M]\left[0,M\right] into kk equal length time intervals S1,…,SkS\_{1},...,S\_{k}. We need to know the actual OCL for claims to evaluate performance, so for RL, each interval should include only claims that settle during the next immediate interval; see Figure [5.1](https://arxiv.org/html/2601.07637v1#S5.F1 "Figure 5.1 ‣ 5.2.3 Rolling Settlement Validation (RSV) ‣ 5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving"), and supervised method folds should contain claims settling in that interval. Therefore, for each hyperparameter combination, we train on S1S\_{1} to predict the OCL for development periods of claims that settle in S2S\_{2}, then train on S1+S2S\_{1}+S\_{2} and predict for S3S\_{3}, and so on. The kk results are averaged to compare across all hyperparameter combinations.

![Refer to caption](figs/rolling_settlement.png)


Figure 5.1: RL vs supervised methods illustration for the rolling settlement approach

This is best understood by referring to the simple diagram in Figure [5.1](https://arxiv.org/html/2601.07637v1#S5.F1 "Figure 5.1 ‣ 5.2.3 Rolling Settlement Validation (RSV) ‣ 5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving"), which summarises both splits for evaluation and tuning purposes. For simplicity and because we are working with a small dataset, we choose k=3k=3 (Figure [5.1](https://arxiv.org/html/2601.07637v1#S5.F1 "Figure 5.1 ‣ 5.2.3 Rolling Settlement Validation (RSV) ‣ 5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving") depicts k=2k=2).

1. 1.

   For RL, we are simply applying one more temporal split on the training set [0,40][0,40]. All claims that are reported (known) in S1S\_{1} are used to train, including still-open claims, and the performance is evaluated by looking at claims that were notified in S1S\_{1} and have settled in S2S\_{2}.
2. 2.

   For supervised methods such as a feed-forward neural network, we take each successive sequence of transactions for claims settling in S1S\_{1} to train on, then evaluate on all sequences of claims that are settled in S2S\_{2} to train the model (S2S\_{2} is now the “validation” set in the sense of Remarks [5.1](https://arxiv.org/html/2601.07637v1#S5.Thmremark1 "Remark 5.1. ‣ 5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving")–[5.2](https://arxiv.org/html/2601.07637v1#S5.Thmremark2 "Remark 5.2. ‣ 5.2.3 Rolling Settlement Validation (RSV) ‣ 5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving")).

There are two important considerations:

* 1.

  There is a limit to how large kk can be depending on the size of the data, since we should have a sufficient number of claims settling in each interval S1,…,SkS\_{1},...,S\_{k} for the validation results to be stable.
* 2.

  If the data spans a long enough time frame such that there is possibly non-stationarity across calendar time, then kk needs to be smaller (or discard earlier times) so that the initial folds aren’t completely outdated.

###### Remark 5.2.

As already mentioned in Remark [5.1](https://arxiv.org/html/2601.07637v1#S5.Thmremark1 "Remark 5.1. ‣ 5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving"), it is important, in many machine learning applications, to implement early stopping in both training and validation for variance reduction and to avoid overfitting across too many epochs (complete passes over the training data). However, this doesn’t apply to RL since it only takes one pass through the training data. For supervised methods, this is done easily by an 80-20 split of the rolling-settlement fold, where the 20% sub-fold can be used for early stopping. In our case of Figure [5.1](https://arxiv.org/html/2601.07637v1#S5.F1 "Figure 5.1 ‣ 5.2.3 Rolling Settlement Validation (RSV) ‣ 5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving"), we would train on the first 80% of S1S\_{1} and use the remaining 20% of S1S\_{1} for early stopping, then evaluate on claims that settle in S2S\_{2} for the validation results.

## 6 Downward Bias Adjustment

While individual-claim accuracy is important, actuarial reserving ultimately requires aggregate consistency at the portfolio level. In the absence of an explicit constraint or weighting mechanism, models optimised for average claim-level accuracy may systematically understate total OCL due to the rarity of large claims, much like class imbalance issues in classification tasks. We observed in our experiments that models suffer from a large and consistent downward bias, whereby they underestimate the aggregate OCL at the portfolio level. We further discuss the possible underlying reasons in detail in [A](https://arxiv.org/html/2601.07637v1#A1 "Appendix A Causes of Downward Bias ‣ Reinforcement Learning for Micro-Level Claims Reserving").

We propose an OCL importance weighting idea to address the issue. This approach can be interpreted as aligning the learning objective with a materiality-weighted loss function, where errors on larger claims carry proportionally greater financial significance.
From this perspective, the weighting scheme is not an ex post correction, but an explicit articulation of the actuarial objective that portfolio-level estimates should be approximately unbiased in expectation.

A natural idea to address the rarity of large claims problem is to simply assign greater importance to larger claim developments by weighting claims proportionally to their true OCL. The next two sections implement this idea for supervised methods and RL, respectively.

It is worth emphasising that we are implementing the same fundamental OCL importance weighting idea for both RL and supervised learning methods, though there are some nuances that arise for RL when dealing with RBNS (open) claims.

### 6.1 Bias correction for supervised methods

For supervised methods, we can optimise a weighted MSE objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1Kwk​(OCL^k−OCLk)2∑k=1Kwk,\frac{\sum\_{k=1}^{K}w\_{k}(\hat{\text{OCL}}\_{k}-\text{OCL}\_{k})^{2}}{\sum\_{k=1}^{K}w\_{k}}, |  | (6.1) |

where OCLk\text{OCL}\_{k} is the true OCL and OCL^k\hat{\text{OCL}}\_{k} is the predicted OCL for the kkth training observation (where an observation is specified by a (claim,development period)(\text{claim},\text{development period}) tuple). All we have added here is the weight

|  |  |  |  |
| --- | --- | --- | --- |
|  | wk=exp⁡(α​ln⁡OCLks),s=OCL¯,w\_{k}=\exp\left(\alpha\ln\frac{\text{OCL}\_{k}}{s}\right),\quad s=\bar{\text{OCL}}, |  | (6.2) |

where ss is the scaling factor, and the idea is that larger-than-average OCL steps should be assigned more weight than 1. The (tuned) temperature α\alpha controls the convexity, and tapers the growth of the weight for increasing OCL if set to be less than one.

### 6.2 Bias correction for RL

For RL, the correction is achieved by simply increasing the size of the accuracy reward signal for claim developments with larger OCL. The multiplier wτw\_{\tau} acts on each development period of the claim, to “inflate” raccr\_{\text{acc}} for claims with more high-OCL-periods. This idea of using the reward magnitude to control where the agent pays more attention to is well-founded in the RL literature to deal with class imbalance issues (see, e.g. Lin et al., [2020](https://arxiv.org/html/2601.07637v1#bib.bib41), and the references therein). Hence, ([4.5](https://arxiv.org/html/2601.07637v1#S4.E5 "In item 1 ‣ 4.1.2 Reward function ℛ ‣ 4.1 Choices in the MDP Formulation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | racc=C​∑τ=1Tn−1wτ⋅γτ−1∑τ=1Tn−1γτ−1⋅h​(OCLτ,OCL^τ),r\_{\text{acc}}=C\sum\_{\tau=1}^{T\_{n}-1}{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}w\_{\tau}}\cdot\frac{\gamma^{\tau-1}}{\sum\_{\tau=1}^{T\_{n}-1}\gamma^{\tau-1}}\cdot h\left(\text{OCL}\_{\tau},\hat{\text{OCL}}\_{\tau}\right), |  | (6.3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | wτ={exp⁡(α​ln⁡OCLτs),if the claim is settled in the training set;(max(Pτcurr,0UL)−Pτs)α,if the claim is not settled in the training set;w\_{\tau}=\begin{cases}\exp\left(\alpha\ln\frac{\text{OCL}\_{\tau}}{s}\right),&\text{if the claim is settled in the training set};\\ \left(\frac{\max(P\_{\tau\_{\text{curr}}},\;\_{0}\text{UL})-P\_{\tau}}{s}\right)^{\alpha},&\text{if the claim is not settled in the training set};\end{cases} |  | (6.4) |

and where τcurr<Tn\tau\_{\text{curr}}<T\_{n} denote the current periods since notification for the claim at the valuation (cutoff) date, PτP\_{\tau} denote the cumulative paid amount at the jjth period since notification, and UL0{}\_{0}\text{UL} is the initial ultimate loss value (see Section [4.2](https://arxiv.org/html/2601.07637v1#S4.SS2 "4.2 Initialisation ‣ 4 Implementational Choices ‣ Reinforcement Learning for Micro-Level Claims Reserving")).

The multiplier wτw\_{\tau} is defined in the same way as for supervised methods for settled claims in ([6.2](https://arxiv.org/html/2601.07637v1#S6.E2 "In 6.1 Bias correction for supervised methods ‣ 6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving")). The caveat here with RL is that for claim developments seen during training for claims that do not settle during the training interval, we cannot set wτw\_{\tau} in the same way since the true OCL is not yet known.
Instead of naively setting wτ=1w\_{\tau}=1 for these claims, we can do something more informative as in the second part of ([6.4](https://arxiv.org/html/2601.07637v1#S6.E4 "In 6.2 Bias correction for RL ‣ 6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving")). The idea is that the last known cumulative paid amount for the claim is PτcurrP\_{\tau\_{\text{curr}}}, so we know that the ultimate claim size for the claim should be at least this much. By using this as the estimate of ultimate, we can get a lower bound on the true OCL for all previous developments τ<τcurr\tau<\tau\_{\text{curr}} to use for assigning a more informative weight. The issue with just using Pτcurr−PτP\_{\tau\_{\text{curr}}}-P\_{\tau} as the estimate of true OCL, however, is that for immature claims and/or long-tailed claims, PτcurrP\_{\tau\_{\text{curr}}} can be small, and hence underestimate the ultimate. This would mean the weight wτw\_{\tau} under-emphasises the importance of the claim. To reduce the impact of this shortcoming, we will instead use our initial estimate of claim size UL0\text{UL}\_{0} in these cases.

###### Remark 6.1.

Note that we do not further normalise with wτw\_{\tau} in ([6.3](https://arxiv.org/html/2601.07637v1#S6.E3 "In 6.2 Bias correction for RL ‣ 6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving")), that is, the definition of raccr\_{\text{acc}} does not have γτ−1​wτ\gamma^{\tau-1}w\_{\tau} in the denominator because this would erase the effect of scaling between claims (small and large claims would have comparable raccr\_{\text{acc}}).

###### Remark 6.2.

We also considered using a conditional value-at-risk (CVaR) objective (Rockafellar and Uryasev, [2002](https://arxiv.org/html/2601.07637v1#bib.bib55)). Instead of assigning larger weights to larger OCLs, one then takes the perspective of controlling the tail risk of mis-estimation. This was the objective used by Dong and Finlay ([2025](https://arxiv.org/html/2601.07637v1#bib.bib24)) in their RL formulation. There are several reasons for choosing the OCL importance weighting idea over a CVaR objective. Firstly, importance weighting is a simpler method, and it also ostensibly produces better results in our tests. Additionally, CVaR controls for the tail risk, which is not aligned with our objective of targeting the central estimate.

## 7 Evaluation of Model Performance

We briefly discuss here benchmark models, as well as the evaluation metrics we use to evaluate and compare model performance.

### 7.1 Benchmark models

We will compare RL with a feed-forward neural network (FNN) as well as the chain ladder. Details for these models are discussed in [B](https://arxiv.org/html/2601.07637v1#A2 "Appendix B Benchmark Models ‣ Reinforcement Learning for Micro-Level Claims Reserving"), but we mention here that the chain ladder approach must be stripped of IBNRs to be comparable to individual claims reserving models, for which we adopt the procedure of Delong and Wüthrich ([2020](https://arxiv.org/html/2601.07637v1#bib.bib21), described in [B.1](https://arxiv.org/html/2601.07637v1#A2.SS1 "B.1 Chain-Ladder ‣ Appendix B Benchmark Models ‣ Reinforcement Learning for Micro-Level Claims Reserving")).

### 7.2 Evaluation Metrics

We will use two metrics to compare the model performance of RL against FNN and chain ladder.

1. 1.

   Relative OCL: Focusing on aggregate performance, we define

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | relative OCL=predicted OCLtrue OCL.\text{relative OCL}=\frac{\text{predicted OCL}}{\text{true OCL}}. |  | (7.1) |

   It should be made clear that this metric is aggregated at some pre-specified level. For example, if the level specified is the entire test set, then the relative OCL is calculated by aggregating the predicted and true OCLs for all claims, and taking the ratio. If the level specified is per accident period, then the predicted and true OCLs are aggregated, and the quotient is taken for claims in each accident period.
2. 2.

   RMSE: Focusing now on (average) performance at the individual claim level, we will consider the

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | R​M​S​E=1N​∑n=1N(OCL^n−OCLn)2,RMSE=\sqrt{\frac{1}{N}\sum\_{n=1}^{N}(\hat{\text{OCL}}\_{n}-\text{OCL}\_{n})^{2}}, |  | (7.2) |

   where nn denotes the nn-th claim, OCL^n\hat{\text{OCL}}\_{n} denotes the predicted OCL for the claim, and OCLn\text{OCL}\_{n} denotes the true OCL. Of course, we want the RMSE to be as small as possible (if seeking the mean); a zero RMSE would be achieved by a “saturated” model.

It should be said that the primary metric of interest is the relative OCL, as we first and foremost want the predictions to be accurate at an aggregate level. The RMSE complements our analysis by giving insight into how the model fares at an individual claims level given some level of aggregate performance.

### 7.3 Hyperparameter tuning and subsequent training and testing

Choosing an optimality criterion for the hyperparameters deserves some thought. A first idea would be to use the weighted MSE ([6.1](https://arxiv.org/html/2601.07637v1#S6.E1 "In 6.1 Bias correction for supervised methods ‣ 6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving")). However, it includes the hyperparameter α\alpha which we would like to tune. Even though one could use a fixed point type approach, we prefer avoiding such a manual procedure (which additionally has no guarantee of reaching an equilibrium).

Another option (which we decided to implement here) is to focus on the aggregate performance measured by the ratio ([7.1](https://arxiv.org/html/2601.07637v1#S7.E1 "In item 1 ‣ 7.2 Evaluation Metrics ‣ 7 Evaluation of Model Performance ‣ Reinforcement Learning for Micro-Level Claims Reserving")); more specifically, to choose the set of hyperparameters that leads to a predicted (overall) OCL that is the closest to its actual value. This ‘aggregate’ focus aligns nicely with the real problem at hand. Note that each set of hyperparameters leads to a single value of ([7.1](https://arxiv.org/html/2601.07637v1#S7.E1 "In item 1 ‣ 7.2 Evaluation Metrics ‣ 7 Evaluation of Model Performance ‣ Reinforcement Learning for Micro-Level Claims Reserving")), but this ratio is the (scaled) sum of all our predictions, and hence is likely to be relatively stable (and symmetrical) due to the central limit theorem. Nevertheless, we did try to tune hyperparameters using ([6.1](https://arxiv.org/html/2601.07637v1#S6.E1 "In 6.1 Bias correction for supervised methods ‣ 6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving")) and α=1\alpha=1, and obtained very similar (in some cases such as SPLICE complexity 5, identical) results.

Following standard practice, after the best set of hyperparameters is obtained, we fix them and do one last training pass through the full training set to obtain the final model to use for testing. Finally, for testing purposes, we “freeze” the RL model so that it does not perform exploration; refer to Remark [3.5](https://arxiv.org/html/2601.07637v1#S3.Thmremark5 "Remark 3.5. ‣ 3.4 Description of one iteration ‣ 3 Micro-reserving RL Formulation ‣ Reinforcement Learning for Micro-Level Claims Reserving") for a more detailed discussion on this.

## 8 Empirical results on CAS and SPLICE synthetic data

Models are first evaluated on 5 simulated property casualty insurance datasets provided online by the Casualty Actuarial Society (CAS, [2025](https://arxiv.org/html/2601.07637v1#bib.bib16)). While we observe an extremely good performance by RL on these datasets, we cannot provide deep analysis, as we don’t have any information on the underlying claim dynamics behind the data. Therefore, we proceeded to conduct a simulation study using data generated using the SynthETIC (Avanzi et al., [2021b](https://arxiv.org/html/2601.07637v1#bib.bib8), [c](https://arxiv.org/html/2601.07637v1#bib.bib9)) and SPLICE (Avanzi et al., [2023](https://arxiv.org/html/2601.07637v1#bib.bib7), [2021a](https://arxiv.org/html/2601.07637v1#bib.bib6)) generators. SynthETIC is a continuous-time individual claims experience simulator, that, for each claim, simulates a claim occurrence date, the total claim size, the notification and settlement dates, and partial payment amounts and distribution. SPLICE extends this to also include case estimates. We use simulated data for two reasons: firstly, there is no real publicly available transactional-level individual claims data, and secondly, it allows us to examine the performance of models across multiple datasets with the same underlying mechanisms. For details on the data structures for the CAS and SPLICE datasets, refer to [C](https://arxiv.org/html/2601.07637v1#A3 "Appendix C Data Description ‣ Reinforcement Learning for Micro-Level Claims Reserving").

The CAS datasets are quite small, containing only 5 datasets spanning 16 periods (years), with each dataset containing around 1700 claims in total. The datasets contained unsettled claims and non-claims (claims with zero loss), which we removed. The CAS website states that the claim activity can be affected by a variety of changes that are common problems faced by members of CAS. The five datasets correspond to one or a combination of those challenges.

For our simulation study using SPLICE, we simulated 30 small datasets with parameters of on average 2500 claims per period, and 40 accident periods with both complexity 1 and complexity 5 (maximum complexity) settings. Complexity 1 is the simplest type of data (no base or superimposed inflation), where chain-ladder is the perfect model. We use this to benchmark in particular against the chain ladder to demonstrate the feasibility of the RL approach. Complexity 5 is the most complex type of data that breaches assumptions underlying the chain-ladder, including a structural break at calendar period 20, and varying levels of inflation. In fact, it was designed to have a broad resemblance to the experience of a real Auto Bodily Injury portfolio. For more details on what the underlying mechanisms are for each level of data complexity, we refer to Table 4 in Avanzi et al. ([2023](https://arxiv.org/html/2601.07637v1#bib.bib7)).

To evaluate the performance, we selected a valuation (cut-off) period of 15 and 40 for the CAS and SPLICE datasets, respectively. This means that all transactions prior to the end of year 15 and quarter 40 for CAS and SPLICE, respectively, are in the training set, while unsettled claims by the valuation date constitute test claims.

Below, we present several results based on the data complexity and model comparisons. We slice the data in several ways to classify results in terms of maturity of each claim, where mature claims correspond to claims with earlier accident periods/later periods since notification, and immature claims correspond to claims with later accident periods/earlier periods since notification.

To this end, it is more important to first understand the share of the outstanding OCL dollars by accident period and periods since notification to understand where the bulk of the outstanding liability lies. In particular, accident periods up to and including 25 account for only roughly 20% of all outstanding claims in the SPLICE data. As a result, the vast majority of the liability (roughly 80%) is associated with the 15 last accident periods. Observations are similar in the CAS datasets, although they are lighter-tailed; see [D](https://arxiv.org/html/2601.07637v1#A4 "Appendix D Cumulative Share of Outstanding OCL Graphs ‣ Reinforcement Learning for Micro-Level Claims Reserving"). Furthermore, case estimates of immature claims are less likely to be accurate, which further stresses how important their estimation is. All in all, the prediction performance of immature claims is the most material, and we will focus on those in our analysis.

![Refer to caption](figs/errors_RMSE_AP_PSN_CAS.png)


Figure 8.1: RMSE Performance of RL and FNN on CAS Test Data



![Refer to caption](figs/OCL_ratio_AQ_CAS.png)


(a) Boxplots of the relative OCL by accident period

![Refer to caption](figs/OCL_ratio_QSN_CAS.png)


(b) Boxplots of the relative OCL by periods since notification

![Refer to caption](figs/TOTALS_relative_OCL_CAS.png)


(c) Boxplots of the aggregate relative OCL across all periods

Figure 8.2: Relative OCL Performance of RL, FNN, and CL on CAS Test Data

### 8.1 Performance of RL and Benchmark Models on CAS Test Data

We first briefly describe the graphical results. Figure [2(a)](https://arxiv.org/html/2601.07637v1#S8.F2.sf1 "In Figure 8.2 ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") slices the data by the accident period (AP) of claim, and plots the relative OCL in aggregate for all claims with the same accident period. Figure [2(b)](https://arxiv.org/html/2601.07637v1#S8.F2.sf2 "In Figure 8.2 ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") depicts the relative OCL by periods since notification (PSN) slices. Similarly, Figure [8.1](https://arxiv.org/html/2601.07637v1#S8.F1 "Figure 8.1 ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") depicts the RMSE by the AP and PSN slices. Finally, Figure [2(c)](https://arxiv.org/html/2601.07637v1#S8.F2.sf3 "In Figure 8.2 ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") shows the aggregate relative OCL performance across all claims in the test set. Note that we have modified the boxplots to display the mean rather than the median, as this corresponds to the central estimate required in most jurisdictions.

RL performs remarkably well on the CAS datasets, with an essentially perfect aggregate performance for two out of the five CAS datasets. We also observe the desirable property that performance is good for immature claims, with RL predicting quite accurately for the accident periods 8-15, which accounts for ≈90%\approx 90\% of the cumulative outstanding OCL. This is promising because, as we discussed earlier, immature claims are where predictive models can add a lot of value over case estimates. Slicing the data by periods since notification view in Figure [2(b)](https://arxiv.org/html/2601.07637v1#S8.F2.sf2 "In Figure 8.2 ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") is similarly impressive, with performance deteriorating substantially only for latter four periods.

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | RL | FNN | CL |
| Average Relative OCL | 92.26% | 123.00% | 150.99% |
| Average RMSE | 4698 | 4528 |  |

Table 8.1: Model comparison at valuation: RL vs FNN vs CL on CAS Test Data

We observe that the chain ladder (stripped of IBNRs) is failing on the CAS dataset, which indicates that the underlying dynamics of the CAS data do not adhere to chain ladder assumptions. The FNN posts a respectable performance in aggregate, but noticeably falls short for the important group of immature claims, particularly for accident period 15 and the first period since notification.

In terms of individual claim performance, RL and FNN have comparable RMSEs; refer to Table [8.1](https://arxiv.org/html/2601.07637v1#S8.T1 "Table 8.1 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") and Figure [8.1](https://arxiv.org/html/2601.07637v1#S8.F1 "Figure 8.1 ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving"). It stands that RL has a desirable performance in the sense that it is equal or better than FNN for the important immature claims, though worse for the mature claims.

As we don’t know the underlying dynamics of the CAS dataset, it is difficult to derive further insights with these results. Therefore, we shift our attention to a simulation study using SPLICE-generated data in Section [8.2](https://arxiv.org/html/2601.07637v1#S8.SS2 "8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving").

![Refer to caption](figs/AGG_ratio_ocl_AQ_per_claim.png)


(a) Boxplots of the relative OCL by accident period

![Refer to caption](figs/AGG_ratio_ocl_QSN_per_claim.png)


(b) Boxplots of the relative OCL by periods since notification

![Refer to caption](figs/TOTALS_relative_OCL.png)


(c) Boxplots of the aggregate relative OCL across all periods

Figure 8.3: Relative OCL Performance of RL, FNN, and CL on Complexity 1 Test Data

### 8.2 Simulation Study on the Test Set of SPLICE Generated Data

#### 8.2.1 Complexity 1 - RL vs FNN vs CL

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | RL | FNN | CL |
| Average Relative OCL | 101.84% | 98.54% | 101.95% |
| Average RMSE | 1182792 | 409841 |  |

Table 8.2: Model comparison at valuation: RL vs FNN vs CL on complexity 1 Test Data

![Refer to caption](figs/RMSE_AQ_QSN_COMPLEX_1.png)


Figure 8.4: RMSE Performance of RL and FNN for Complexity 1 Test Data

We are first interested in benchmarking the performance of RL (and FNN) against the chain ladder model as a proof of concept and to ascertain that they are able to perform on a simple, well-behaved and well-known data structure where chain ladder is the perfect model. Before discussing RL and FNN, it is worthwhile to briefly examine chain-ladder’s performance; in green in Figure [8.3](https://arxiv.org/html/2601.07637v1#S8.F3 "Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving"). Firstly, recall that the chain ladder (CL) here is stripped of IBNRs in an estimation procedure. This procedure may be unstable for earlier accident periods, where most claims have already settled. Chain ladder does not have a large systematic downward bias because it is a macro-level method, and so it doesn’t suffer from our postulated rarity of large claims hypothesis ([A](https://arxiv.org/html/2601.07637v1#A1 "Appendix A Causes of Downward Bias ‣ Reinforcement Learning for Micro-Level Claims Reserving")). Finally, we remark that CL is not present in Figure [3(b)](https://arxiv.org/html/2601.07637v1#S8.F3.sf2 "In Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") because periods since notification requires us to be working on an individual claims basis.

Now, let us turn our attention to the comparative performance of RL and FNN in Figure [8.3](https://arxiv.org/html/2601.07637v1#S8.F3 "Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") in terms of relative OCL. It is hard to beat the CL results because they are essentially perfect, but it is promising that RL (and FNN) performs almost as well at the aggregate level (Figure [3(c)](https://arxiv.org/html/2601.07637v1#S8.F3.sf3 "In Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving")) in terms of getting the mean correct across datasets. All three methods closely identify the correct mean relative OCL of one, with the superior performance of chain ladder showing through the low variance of its predictions. Aside from one outlier for RL, it has similar variation in predictions to the FNN. We believe that the reason behind the outlier, and indeed, the overall volatililty of RL and FNN can be largely explained by the models struggling to adjust sharply enough to final payments. We investigate this in [E](https://arxiv.org/html/2601.07637v1#A5 "Appendix E Effect of Final Payments ‣ Reinforcement Learning for Micro-Level Claims Reserving").

When we investigate the more granular AP and PSN breakdowns of predictions (Figures [3(a)](https://arxiv.org/html/2601.07637v1#S8.F3.sf1 "In Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") and [3(b)](https://arxiv.org/html/2601.07637v1#S8.F3.sf2 "In Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving"), respectively), RL and FNN are comparable for the immature claims, with RL underestimating slightly more so than FNN. The exception is the last AP and the first PSN, where RL is better than FNN. However, the good performance by RL here is more so attributable to the initialisation procedure being suitable for complexity 1 data.

Additionally, we can observe in Figures [3(a)](https://arxiv.org/html/2601.07637v1#S8.F3.sf1 "In Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") and [3(b)](https://arxiv.org/html/2601.07637v1#S8.F3.sf2 "In Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") that RL has significantly higher variance in predictions for mature claims and tends to overestimate substantially. While this means that the RL model is not useful for these periods, it can also be viewed as a good thing as it shows that RL is able to “recognise” the fact that estimates are volatile for mature claims. There are some periods where there are only a couple of claims being predicted in total, and this uncertainty is not being recognised by FNN. A reason why RL tends to overestimate may be that claims tend to have a sharp decrease in OCL when the final payment is made, and the constrained action space is unable to capture this abrupt decline in OCL. Furthermore, the OCL importance weighting adjustment could compound this effect as it decreases the importance of getting these smaller OCL predictions correct.

It is not surprising that RL has a higher RMSE (recall that this is the average per-claim RMSE) than FNN. RL has large variations for mature claims, which evidently is the major source of the higher RMSE; see Figure [8.4](https://arxiv.org/html/2601.07637v1#S8.F4 "Figure 8.4 ‣ 8.2.1 Complexity 1 - RL vs FNN vs CL ‣ 8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving"). However, the RMSE is approximately the same for the immature claims, which indicates that RL and FNN tend to make similarly-sized mistakes on a per-claim basis for the important immature claims.

#### 8.2.2 Complexity 5 - RL vs FNN

Much of our observations in complexity 1 remain true for complexity 5. As we can see in Figure [8.6](https://arxiv.org/html/2601.07637v1#S8.F6 "Figure 8.6 ‣ 8.2.2 Complexity 5 - RL vs FNN ‣ 8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving"), RL and FNN are still comparable in terms of aggregate performance, with RL possessing higher variance than FNN for mature claims, and RMSE again indicates that both RL and FNN predict similarly on a per-claim basis for the immature claims (Figure [8.5](https://arxiv.org/html/2601.07637v1#S8.F5 "Figure 8.5 ‣ 8.2.2 Complexity 5 - RL vs FNN ‣ 8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving")).

There are, however, some interesting nuances to discuss. Firstly, RL appears to perform well for the mature claims up until around accident period 25 (albeit with a higher variance than FNN). This is very different to what we had observed for complexity 1. This is likely because for complexity 1, there are only around 300 RBNS claims from the first accident periods, whereas for complexity 5, there are around 1300. With the scarcity of claims, it is expected that there be a lot of volatility across datasets for complexity 1. What is very interesting about RL is that the decrease in performance (underestimation in later accident periods) correspond to the structural break at calendar period 20 on complexity 5 data. This indicates that our current formulation or algorithm choice are not perfectly equipped to deal with sudden changes to the underlying environment dynamics, which is to be expected. In comparison, FNN appears to systematically underestimate for all claims in all periods.

We can see that the chain ladder fails quite severely on the complex data, and is systematically overestimating. This overestimation is consistent with the results of Figure 5 in the original SPLICE paper (Avanzi et al., [2023](https://arxiv.org/html/2601.07637v1#bib.bib7)).

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | RL | FNN | CL |
| Average Relative OCL | 73.91% | 82.30% | 135.68% |
| Average RMSE | 452121 | 323463 |  |

Table 8.3: Model comparison at valuation: RL vs FNN vs CL on complexity 5 Test Data

![Refer to caption](figs/RMSE_AQ_QSN_C5.png)


Figure 8.5: RMSE Performance of RL and FNN on Complexity 5 Test Data



![Refer to caption](figs/OCL_ratio_Acc_C5.png)


(a) Boxplots of the relative OCL by accident period

![Refer to caption](figs/OCL_ratio_QSN_C5.png)


(b) Boxplots of the relative OCL by periods since notification

![Refer to caption](figs/Relative_UL_OCL_C5.png)


(c) Boxplots of the aggregate relative OCL across all periods

Figure 8.6: Relative OCL Performance of RL, FNN, and CL on Complexity 5 Test Data

### 8.3 Discussion and Limitations

In this paper, we have formulated a framework to apply RL to micro-level reserving, and implemented it with benchmarking against the chain-ladder model and a vanilla FNN model. Section [8.1](https://arxiv.org/html/2601.07637v1#S8.SS1 "8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") demonstrates superior RL performance on more short-tailed simulated data. Section [8.2](https://arxiv.org/html/2601.07637v1#S8.SS2 "8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") conducts a simulation study that demonstrates RL is a feasible approach to the micro-level reserving problem as it shows comparable performance to FNN and chain ladder on complexity 1 data in terms of the mean predictions across datasets. While RL is more volatile than FNN in the aggregate, this is purely due to high volatility in earlier accident periods rather than later. We discussed that this may, in fact, be a positive sign that RL is able to “recognise” the uncertainty associated with these periods, with only a small number of claims remaining. That being said, it is also true that RL tends to have higher variance in its predictions compared to their traditional supervised learning counterparts simply due to its underlying assumptions and structure. FNN assumes (incorrectly) i.i.d. observations, whereas RL uses a Markov model of dependence for claim developments. Part of the high variance could also be due to the fact that we have sparse reward signals for accuracy.

Additionally, we observed comparable performances of RL and FNN on complexity 5 data, with RL performing well on the mature claims. For the immature claims, we postulated that the current implementation is ill-equipped to deal with structural breaks where the underlying environment dynamics change abruptly. More complex RL algorithms and augmenting the MDP representation of the reserving problem to relax the stationarity assumptions could be possible ways to alleviate the problem.

Our experience on complexity 5 seems to indicate that inclusion of case estimates is comparatively more beneficial to RL’s performance than FNN, as FNN is still systematically underestimating for all periods. It is plausible that additions of covariates to the model input could similarly be more advantageous for RL compared to supervised methods because of RL’s capacity to learn from yet to settle claims. Currently, only the accuracy component of the reward is an informative signal, while the other components simply aid learning. One can imagine that RL could benefit significantly with the introduction of reward components that use case estimates and covariates to boost the density of informative reward signals. However, this would likely take some experimentation and expert knowledge. It is also possible that there will be less/no need for importance weighting to correct for the downward bias if there are discriminatory covariates available to the models.

## 9 Conclusion

In this paper, we developed and implemented a reinforcement learning framework for claims reserving at the individual claim level, with a particular focus on modelling the sequential nature of reserve updates over claim development. By formulating outstanding claim liability (OCL) estimation as a Markov decision process, we move beyond static, one-shot prediction approaches and instead model reserving as a controlled, dynamic decision problem that evolves as new information becomes available.

A central advantage of this formulation is that it allows the learning algorithm to exploit information from *all observed claim trajectories*, including claims that remain open at valuation. This contrasts with supervised learning approaches trained on ultimate outcomes, which necessarily restrict attention to settled claims and may therefore suffer from reduced sample sizes and selection effects, especially in long-tailed portfolios. By learning from partial claim histories, the proposed approach better reflects actuarial reserving practice and makes more efficient use of available data.

Several methodological choices were required to make reinforcement learning viable and meaningful in a reserving context. We proposed a continuous action space that updates OCL estimates multiplicatively, ensuring positivity and interpretability of reserves, and designed a reward function that balances accuracy at settlement with stability of reserve revisions over time. In particular, the reward structure penalises unnecessary reserve volatility in periods without new payment information, while allowing responsive adjustments when payments occur. Although inspired by potential-based reward shaping, the proposed reward design is tailored to the realities of claims development and reserving practice.

To support actuarial implementation, we also introduced a number of practical components that are often absent from generic RL applications. These include an explicit initialisation mechanism for new claims entering the portfolio, ensuring sensible starting reserves, and a temporally consistent validation and hyperparameter tuning strategy based on a rolling-settlement scheme. This evaluation framework respects the chronological structure of claims data and avoids information leakage, providing a more realistic assessment of out-of-sample reserving performance.

An important empirical finding of the paper is that optimising claim-level accuracy alone can lead to systematic underestimation of aggregate outstanding liabilities, driven by the rarity and materiality of large claims. This phenomenon is particularly relevant in a reinforcement learning setting, where the objective function directly shapes learning. To address this issue, we proposed an importance-weighting mechanism that increases the influence of large claims during training. Empirically, this adjustment substantially improves aggregate OCL estimates while preserving competitive claim-level performance, highlighting the importance of aligning learning objectives with portfolio-level reserving goals.

The proposed framework was evaluated on synthetic property–casualty datasets from the CAS and SPLICE libraries. Across these experiments, the reinforcement learning approach delivered strong performance at both the individual-claim and aggregate levels. In particular, the method performed well for immature claims and recent accident periods, which account for the largest share of outstanding liabilities and are typically the most challenging to reserve accurately. These results suggest that reinforcement learning is especially well suited to the segments of the portfolio that matter most for reserve adequacy.

While the results are encouraging, several avenues for future research remain. The current framework assumes a largely stationary claims environment, and further work is needed to address structural breaks and regime changes, for example through richer state representations or calendar-time effects. More informative intermediate rewards, potentially incorporating case estimates or expert judgments, may further improve learning efficiency and interpretability. Finally, extensions to real-world datasets and hybrid approaches combining reinforcement learning with traditional actuarial models represent promising directions for future investigation.

Overall, this paper demonstrates that reinforcement learning provides a flexible and powerful framework for individual claims reserving, capable of capturing the sequential nature of reserve updates while addressing practical actuarial concerns such as stability, aggregation, and validation. We hope that this work helps bridge the gap between modern reinforcement learning techniques and actuarial reserving practice, and encourages further exploration of sequential decision-making methods in insurance analytics.

## Acknowledgments

Benjamin Avanzi and Bernard Wong acknowledge support from the Australian Research Council’s Discovery Project funding scheme (DP200101859). The views expressed herein are those of the authors and do not necessarily reflect those of the supporting organisations.

## References

## References

* Al-Mudafer et al. (2022)

  Al-Mudafer, M.T., Avanzi, B.,
  Taylor, G., Wong, B.,
  2022.
  Stochastic loss reserving with mixture density neural
  networks.
  Insurance: Mathematics and Economics
  105, 144–174.
  doi:[10.1016/j.insmatheco.2022.03.010](http://dx.doi.org/10.1016/j.insmatheco.2022.03.010).
* Antonio and Plat (2012)

  Antonio, K., Plat, R.,
  2012.
  Micro-level stochastic loss reserving for general
  insurance.
  Technical Report.
  URL: <https://ssrn.com/abstract=1620446>.
* Arjas (1989)

  Arjas, E., 1989.
  The claims reserving problem in non-life insurance:
  Some structural ideas.
  ASTIN Bulletin 19,
  139–152.
  doi:[10.2143/ast.19.2.2014905](http://dx.doi.org/10.2143/ast.19.2.2014905).
* Asmussen and Taksar (1997)

  Asmussen, S., Taksar, M.,
  1997.
  Controlled diffusion models for optimal dividend
  pay-out.
  Technical Report.
* Avanzi et al. (2025)

  Avanzi, B., Lambrianidis, M.,
  Taylor, G., Wong, B.,
  2025.
  On the use of case estimate and transactional payment
  data in neural networks for individual loss reserving.
  URL: <https://arxiv.org/abs/2601.05274>,
  doi:[10.48550/arXiv.2601.05274](http://dx.doi.org/10.48550/arXiv.2601.05274).
* Avanzi et al. (2021a)

  Avanzi, B., Taylor, G.,
  Wang, M., 2021a.
  SPLICE: Synthetic paid loss and incurred
  cost experience (splice) simulator.
  <https://CRAN.R-project.org/package=SPLICE>.
* Avanzi et al. (2023)

  Avanzi, B., Taylor, G.,
  Wang, M., 2023.
  Splice: A synthetic paid loss and incurred cost
  experience simulator.
  Annals of Actuarial Science 17,
  7–35.
  doi:[10.1017/S1748499522000057](http://dx.doi.org/10.1017/S1748499522000057).
* Avanzi et al. (2021b)

  Avanzi, B., Taylor, G.,
  Wang, M., Wong, B.,
  2021b.
  Synthetic: An individual insurance claim simulator
  with feature control.
  Insurance: Mathematics and Economics
  100, 296–308.
  doi:[10.1016/j.insmatheco.2021.06.004](http://dx.doi.org/10.1016/j.insmatheco.2021.06.004).
* Avanzi et al. (2021c)

  Avanzi, B., Taylor, G.,
  Wang, M., Wong, B.,
  2021c.
  SynthETIC: Synthetic experience tracking
  insurance claims.
  <https://CRAN.R-project.org/package=SynthETIC>.
  R package version 1.0.1.
* Avanzi et al. (2015)

  Avanzi, B., Wong, B.,
  Yang, X., 2015.
  A micro-level claim count model with overdispersion
  and reporting delays.
  SSRN Electronic Journal
  doi:[10.2139/ssrn.2705241](http://dx.doi.org/10.2139/ssrn.2705241).
* Balona and Richman (2020)

  Balona, C., Richman, R.,
  2020.
  The Actuary and IBNR Techniques: A Machine Learning
  Approach.
  Technical Report.
  URL: <https://ssrn.com/abstract=3697256>.
* Baudry and Robert (2019)

  Baudry, M., Robert, C.Y.,
  2019.
  A machine learning approach for individual claims
  reserving in insurance.
  Applied Stochastic Models in Business and Industry
  35, 1127–1155.
  doi:[10.1002/asmb.2455](http://dx.doi.org/10.1002/asmb.2455).
* Bornhuetter and Ferguson (1972)

  Bornhuetter, R.L., Ferguson, R.E.,
  1972.
  The actuary and ibnr.
  Proceedings of the Casualty Actuarial Society
  LIX, 181–195.
* Boute et al. (2022)

  Boute, R.N., Gijsbrechts, J.,
  van Jaarsveld, W., Vanvuchelen, N.,
  2022.
  Deep reinforcement learning for inventory control: A
  roadmap.
  European Journal of Operational Research
  298, 401–412.
  doi:[10.1016/j.ejor.2021.07.016](http://dx.doi.org/10.1016/j.ejor.2021.07.016).
* Buehler et al. (2019)

  Buehler, H., Gonon, L.,
  Teichmann, J., Wood, B.,
  2019.
  Deep hedging.
  Quantitative Finance 19,
  1271–1291.
  doi:[10.1080/14697688.2019.1571683](http://dx.doi.org/10.1080/14697688.2019.1571683).
* CAS (2025)

  CAS, 2025.
  Data sets now available for research rfp on
  forecasting future loss payments from policies sold in the past.
  URL: <https://www.casact.org/article/data-sets-now-available-research-rfp-forecasting-future-loss-payments-policies-sold-past>.
* Chaoubi et al. (2023)

  Chaoubi, I., Besse, C.,
  Cossette, H., Côté, M.P.,
  2023.
  Micro-level reserving for general insurance claims
  using a long short-term memory network.
  Applied Stochastic Models in Business and Industry
  39, 382–407.
  doi:[10.1002/asmb.2750](http://dx.doi.org/10.1002/asmb.2750).
* Chong et al. (2023)

  Chong, W.F., Cui, H., Li,
  Y., 2023.
  Pseudo-model-free hedging for variable annuities via
  deep reinforcement learning.
  Annals of Actuarial Science 18.
  doi:[10.1017/S1748499523000027](http://dx.doi.org/10.1017/S1748499523000027).
* Cover and Thomas (2006)

  Cover, T.M., Thomas, J.A.,
  2006.
  Elements of information theory.
  Wiley-Interscience.
* Delong et al. (2022)

  Delong, L., Lindholm, M.,
  Wüthrich, M.V., 2022.
  Collective reserving using individual claims data.
  Scandinavian Actuarial Journal
  2022, 1–28.
  doi:[10.1080/03461238.2021.1921836](http://dx.doi.org/10.1080/03461238.2021.1921836).
* Delong and Wüthrich (2020)

  Delong, L., Wüthrich, M.V.,
  2020.
  Neural networks for the joint development of
  individual payments and claim incurred.
  Risks 8.
  doi:[10.3390/risks8020033](http://dx.doi.org/10.3390/risks8020033).
* Deng et al. (2017)

  Deng, Y., Bao, F., Kong,
  Y., Ren, Z., Dai, Q.,
  2017.
  Deep direct reinforcement learning for financial
  signal representation and trading.
  IEEE Transactions on Neural Networks and Learning
  Systems 28, 653–664.
  doi:[10.1109/TNNLS.2016.2522401](http://dx.doi.org/10.1109/TNNLS.2016.2522401).
* Denuit et al. (2021)

  Denuit, M., Charpentier, A.,
  Trufin, J., 2021.
  Autocalibration and tweedie-dominance for insurance
  pricing with machine learning.
  Insurance: Mathematics and Economics
  101, 485–497.
  doi:[10.1016/j.insmatheco.2021.09.001](http://dx.doi.org/10.1016/j.insmatheco.2021.09.001).
* Dong and Finlay (2025)

  Dong, S.C., Finlay, J.R.,
  2025.
  Adaptive insurance reserving with cvar-constrained
  reinforcement learning under macroeconomic regimes URL: <http://arxiv.org/abs/2504.09396>.
* Duval and Pigeon (2019)

  Duval, F., Pigeon, M.,
  2019.
  Individual loss reserving using a gradient
  boosting-based approach.
  Risks 7.
  doi:[10.3390/risks7030079](http://dx.doi.org/10.3390/risks7030079).
* England and Verrall (2002)

  England, P.D., Verrall, R.J.,
  2002.
  STOCHASTIC CLAIMS RESERVING IN GENERAL INSURANCE.
  Technical Report.
* French (1999)

  French, R., 1999.
  Catastrophic forgetting in connectionist networks.
  Trends in Cognitive Sciences 3,
  128–135.
  doi:[10.1016/S1364-6613(99)01294-2](http://dx.doi.org/10.1016/S1364-6613(99)01294-2).
* Gabrielli (2021)

  Gabrielli, A., 2021.
  An individual claims reserving model for reported
  claims.
  European Actuarial Journal 11,
  541–577.
  doi:[10.1007/s13385-021-00271-4](http://dx.doi.org/10.1007/s13385-021-00271-4).
* Gabrielli et al. (2018)

  Gabrielli, A., Richman, R.,
  Wüthrich, M.V., 2018.
  Neural Network Embedding of the Over-Dispersed
  Poisson Reserving Model.
  Technical Report.
  URL: <https://ssrn.com/abstract=3288454>.
* Gerber (1979)

  Gerber, H.U., 1979.
  An introduction to mathematical risk theory.
  S.S. Huebner Foundation for Insurance Education,
  Wharton School, University of Pennsylvania ; Distributed by R.D. Irwin.
* Goodfellow et al. (2017)

  Goodfellow, I., Bengio, Y.,
  Courville, A., 2017.
  Deep learning.
  The MIT Press.
* Haarnoja et al. (2018)

  Haarnoja, T., Zhou, A.,
  Abbeel, P., Levine, S.,
  2018.
  Soft actor-critic: Off-policy maximum entropy deep
  reinforcement learning with a stochastic actor URL: <http://arxiv.org/abs/1801.01290>.
* Hambly et al. (2023)

  Hambly, B., Xu, R., Yang,
  H., 2023.
  Recent advances in reinforcement learning in
  finance.
  Mathematical Finance 33,
  437–503.
  doi:[10.1111/mafi.12382](http://dx.doi.org/10.1111/mafi.12382).
* Howard (1960)

  Howard, R., 1960.
  Dynamic Programming and Markov Processes.
  Technical Report.
* Jaderberg et al. (2017)

  Jaderberg, M., Dalibard, V.,
  Osindero, S., Czarnecki, W.M.,
  Donahue, J., Razavi, A.,
  Vinyals, O., Green, T.,
  Dunning, I., Simonyan, K.,
  Fernando, C., Kavukcuoglu, K.,
  2017.
  Population based training of neural networks
  URL: <http://arxiv.org/abs/1711.09846>.
* Kohavi (1995)

  Kohavi, R., 1995.
  A Study of Cross-Validation and Bootstrap for
  Accuracy Estimation and Model Selection.
  Technical Report.
  URL: [http//roboticsStanfordedu/"ronnyk](http//roboticsStanfordedu/%22ronnyk).
* Konda and Tsitsiklis (1999)

  Konda, V.R., Tsitsiklis, J.N.,
  1999.
  Actor-Critic Algorithms.
  Technical Report.
* Krasheninnikova et al. (2019)

  Krasheninnikova, E., García, J.,
  Maestre, R., Fernández, F.,
  2019.
  Reinforcement learning for pricing strategy
  optimization in the insurance industry.
  Engineering Applications of Artificial
  Intelligence 80, 8–19.
  doi:[10.1016/j.engappai.2019.01.010](http://dx.doi.org/10.1016/j.engappai.2019.01.010).
* Kuo (2019)

  Kuo, K., 2019.
  Deeptriangle: A deep learning approach to loss
  reserving.
  Risks 7.
  doi:[10.3390/risks7030097](http://dx.doi.org/10.3390/risks7030097).
* Kuo (2020)

  Kuo, K., 2020.
  Individual Claims Forecasting with Bayesian Mixture
  Density Networks.
  Technical Report.
* Lin et al. (2020)

  Lin, E., Chen, Q., Qi,
  X., 2020.
  Deep reinforcement learning for imbalanced
  classification.
  Applied Intelligence 50,
  2488–2502.
  doi:[10.1007/s10489-020-01637-z](http://dx.doi.org/10.1007/s10489-020-01637-z).
* Lin (1992)

  Lin, L.J., 1992.
  Self-Improving Reactive Agents Based On Reinforcement
  Learning, Planning and Teaching.
  Technical Report.
* Lopez et al. (2019)

  Lopez, O., Milhaud, X.,
  Thérond, P.E., 2019.
  Erratum: A tree-based algorithm adapted to microlevel
  reserving and long development claims (astin bulletin (2019) (1-22) doi:
  10.1017/asb.2019.12).
  doi:[10.1017/asb.2019.21](http://dx.doi.org/10.1017/asb.2019.21).
* Mack (1993)

  Mack, T., 1993.
  Distribution-free calculation of the standard error
  of chain ladder reserve estimates.
  ASTIN Bulletin 23,
  213–225.
  doi:[10.2143/ast.23.2.2005092](http://dx.doi.org/10.2143/ast.23.2.2005092).
* Martin-Löf (1983)

  Martin-Löf, A., 1983.
  Premium control in an insurance system, an approach
  using linear control theory.
  Scandinavian Actuarial Journal
  1983, 1–27.
  doi:[10.1080/03461238.1983.10408686](http://dx.doi.org/10.1080/03461238.1983.10408686).
* Martin-Löf (1994)

  Martin-Löf, A., 1994.
  Lectures on the use of control theory in insurance.
  Scandinavian Actuarial Journal
  1994, 1–25.
  doi:[10.1080/03461238.1994.10413927](http://dx.doi.org/10.1080/03461238.1994.10413927).
* Meier et al. (2012)

  Meier, E., LeBlanc, G.,
  Tan, Y.E., 2012.
  Orbit correction studies using neural networks, in:
  Proc. IPAC’12 (3rd Int. Particle Accelerator Conf.),
  JACoW Publishing, Geneva, Switzerland.
  URL: <https://proceedings.jacow.org/IPAC2012/papers/weppp057.pdf>.
* Mnih et al. (2013)

  Mnih, V., Kavukcuoglu, K.,
  Silver, D., Graves, A.,
  Antonoglou, I., Wierstra, D.,
  Riedmiller, M., 2013.
  Playing atari with deep reinforcement learning
  URL: <http://arxiv.org/abs/1312.5602>.
* Moody and Saffell (2001)

  Moody, J., Saffell, M.,
  2001.
  Learning to trade via direct reinforcement.
  IEEE Transactions on Neural Networks
  12, 875–889.
  doi:[10.1109/72.935097](http://dx.doi.org/10.1109/72.935097).
* Moor et al. (2022)

  Moor, B.J.D., Gijsbrechts, J.,
  Boute, R.N., 2022.
  Reward shaping to improve the performance of deep
  reinforcement learning in perishable inventory management.
  European Journal of Operational Research
  301, 535–545.
  doi:[10.1016/j.ejor.2021.10.045](http://dx.doi.org/10.1016/j.ejor.2021.10.045).
* Ng et al. (1999)

  Ng, A.Y., Harada, D.,
  Russell, S., 1999.
  Policy invariance under reward transformations:
  Theory and application to reward shaping.
  Technical Report.
* Norberg (1993)

  Norberg, R., 1993.
  Prediction of outstanding liabilities in non-life
  insurance.
  ASTIN Bulletin 23,
  95–115.
  doi:[10.2143/ast.23.1.2005103](http://dx.doi.org/10.2143/ast.23.1.2005103).
* Norberg (1999)

  Norberg, R., 1999.
  Prediction of outstanding liabilities ii. model
  variations and extensions.
  ASTIN Bulletin 29,
  5–25.
  doi:[10.2143/ast.29.1.504603](http://dx.doi.org/10.2143/ast.29.1.504603).
* Palmborg and Lindskog (2023)

  Palmborg, L., Lindskog, F.,
  2023.
  Premium control with reinforcement learning.
  ASTIN Bulletin 53,
  233–257.
  doi:[10.1017/asb.2023.13](http://dx.doi.org/10.1017/asb.2023.13).
* Rockafellar and Uryasev (2002)

  Rockafellar, R., Uryasev, S.,
  2002.
  Conditional value-at-risk for general loss
  distributions.
  Journal of Banking & Finance
  26, 1443–1471.
  doi:[10.1016/S0378-4266(02)00271-6](http://dx.doi.org/10.1016/S0378-4266(02)00271-6).
* Schulman et al. (2017a)

  Schulman, J., Levine, S.,
  Moritz, P., Jordan, M.I.,
  Abbeel, P., 2017a.
  Trust region policy optimization URL: <http://arxiv.org/abs/1502.05477>.
* Schulman et al. (2017b)

  Schulman, J., Wolski, F.,
  Dhariwal, P., Radford, A.,
  Klimov, O., 2017b.
  Proximal policy optimization algorithms URL: <http://arxiv.org/abs/1707.06347>.
* Schwab and Schneider (2024)

  Schwab, B., Schneider, J.C.,
  2024.
  Advancing loss reserving: A hybrid neural network
  approach for individual claim development prediction.
  SSRN Electronic Journal
  doi:[10.2139/ssrn.4769020](http://dx.doi.org/10.2139/ssrn.4769020).
* Silver (2015)

  Silver, D., 2015.
  Lectures on reinforcement learning.
* Silver et al. (2017)

  Silver, D., Hubert, T.,
  Schrittwieser, J., Antonoglou, I.,
  Lai, M., Guez, A.,
  Lanctot, M., Sifre, L.,
  Kumaran, D., Graepel, T.,
  Lillicrap, T., Simonyan, K.,
  Hassabis, D., 2017.
  Mastering chess and shogi by self-play with a general
  reinforcement learning algorithm URL: <http://arxiv.org/abs/1712.01815>.
* Sutton (1988)

  Sutton, R.S., 1988.
  Learning to Predict by the Methods of Temporal
  Differences.
  Technical Report.
* Sutton and Barto (2018)

  Sutton, R.S., Barto, A.G.,
  2018.
  Reinforcement Learning: An Introduction Second
  edition, in progress.
  Technical Report.
* Tashman (2000)

  Tashman, L.J., 2000.
  Out-of-sample tests of forecasting accuracy: an
  analysis and review.
  Technical Report.
  URL: <www.elsevier.com/locate/ijforecast>.
* Taylor (2000)

  Taylor, G., 2000.
  Loss Reserving. volume 21.
  Springer US.
  doi:[10.1007/978-1-4615-4583-5](http://dx.doi.org/10.1007/978-1-4615-4583-5).
* Taylor and McGuire (2016)

  Taylor, G., McGuire, G.,
  2016.
  Stochastic Loss Reserving Using Generalized Linear
  Models.
  Casualty Actuarial Society.
  URL: <https://www.casact.org/sites/default/files/2021-02/03-Taylor.pdf>.
* Wekwete et al. (2023)

  Wekwete, T.A., Kufakunesu, R.,
  van Zyl, G., 2023.
  Application of deep reinforcement learning in asset
  liability management.
  Intelligent Systems with Applications
  20.
  doi:[10.1016/j.iswa.2023.200286](http://dx.doi.org/10.1016/j.iswa.2023.200286).
* Wuthrich et al. (2025)

  Wuthrich, M.V., Richman, R.,
  Avanzi, B., Lindholm, M.,
  Mayer, M., Schelldorfer, J.,
  Scognamiglio, S., 2025.
  Ai tools for actuaries.
  doi:[10.2139/ssrn.5162304](http://dx.doi.org/10.2139/ssrn.5162304).
* Wüthrich and Merz (2008)

  Wüthrich, M.V., Merz, M.,
  2008.
  Stochastic claims reserving methods in insurance.
  John Wiley & Sons.
* Wüthrich (2020)

  Wüthrich, M.V., 2020.
  Bias regularization in neural network models for
  general insurance pricing.
  European Actuarial Journal 10,
  179–202.
  doi:[10.1007/s13385-019-00215-z](http://dx.doi.org/10.1007/s13385-019-00215-z).
* Wüthrich and Ziegel (2024)

  Wüthrich, M.V., Ziegel, J.,
  2024.
  Isotonic recalibration under a low signal-to-noise
  ratio.
  Scandinavian Actuarial Journal
  2024, 279–299.
  doi:[10.1080/03461238.2023.2246743](http://dx.doi.org/10.1080/03461238.2023.2246743).
* Xu et al. (2021)

  Xu, T., Wang, Z., Liang,
  Y., 2021.
  Improving sample complexity bounds for (natural)
  actor-critic algorithms URL: <http://arxiv.org/abs/2004.12956>.
* Xu et al. (2019)

  Xu, Z., Dai, A.M., Kemp,
  J., Metz, L., 2019.
  Learning an adaptive learning rate schedule.
  URL: <https://arxiv.org/abs/1909.09712>,
  doi:[10.48550/arXiv.1909.09712](http://dx.doi.org/10.48550/arXiv.1909.09712).
* Xu et al. (2018)

  Xu, Z., van Hasselt, H.,
  Silver, D., 2018.
  Meta-gradient reinforcement learning URL: <http://arxiv.org/abs/1805.09801>.
* Ziebart and Fox (2010)

  Ziebart, B.D., Fox, D.,
  2010.
  Modeling Purposeful Adaptive Behavior with the
  Principle of Maximum Causal Entropy.
  Technical Report.

## Appendix A Causes of Downward Bias

We observed in our experiments that models suffer from a large and consistent downward bias, whereby they underestimate the aggregate OCL at the portfolio level. We investigate this issue further through a series of hypotheses. To the best of our knowledge, this issue has not been reported anywhere else in the reserving literature, but has been discussed in the pricing literature (e.g., Denuit et al., [2021](https://arxiv.org/html/2601.07637v1#bib.bib23); Wüthrich and Ziegel, [2024](https://arxiv.org/html/2601.07637v1#bib.bib70); Wüthrich, [2020](https://arxiv.org/html/2601.07637v1#bib.bib69)), which we will discuss below in the 5th hypothesis.

Note that in our investigation of hypotheses, we need to show some preliminary results using the relative OCL, which is defined formally in section [7](https://arxiv.org/html/2601.07637v1#S7 "7 Evaluation of Model Performance ‣ Reinforcement Learning for Micro-Level Claims Reserving"). It is simply the ratio of the aggregate predicted OCL to the true aggregate OCL. Hence, the aim to to be as close to a relative OCL of 1 as possible.

1. 1.

   Rarity of Large Claims: We postulate that a key contributing cause to the downward bias is the imbalance between small vs large claims, sort of like a class imbalance problem for classification tasks. In the absence of context that the aggregate prediction should be unbiased, the model will treat every claim as having the same training “power”, so the most frequent claims (i.e., the small claims) take most of the model’s attention.

   We find evidence that supports this hypothesis in Figure [A.1](https://arxiv.org/html/2601.07637v1#A1.F1 "Figure A.1 ‣ item 1 ‣ Appendix A Causes of Downward Bias ‣ Reinforcement Learning for Micro-Level Claims Reserving"), whereby we can see that without any adjustment, the larger claims are severely underestimated, which drives down the overall portfolio level estimate. In fact, FNN suffers substantially more so than RL for the small and medium claims.

   ![Refer to caption](figs/AGG_OCL_ratio_by_size_and_overall.png)


   Figure A.1: Performance of models on different-sized claims. Small, medium and large claims are simply claims split in thirds by their ultimate claim size. Note that this is using 10 datasets of complexity 1 test data (without bias correction from section [6](https://arxiv.org/html/2601.07637v1#S6 "6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving")), which is the simplest data where chain ladder assumptions hold; see section [8.2](https://arxiv.org/html/2601.07637v1#S8.SS2 "8.2 Simulation Study on the Test Set of SPLICE Generated Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving") for more detail.
2. 2.

   Lack of (Informative) Covariates: Another likely contributing cause is the lack of covariates. With essentially just the accident period, development period, payment information, and case estimates, it is difficult to discern whether there is a little or a lot of OCL. This is in contrast to existing works (Gabrielli, [2021](https://arxiv.org/html/2601.07637v1#bib.bib28); Kuo, [2020](https://arxiv.org/html/2601.07637v1#bib.bib40)) using a different claims simulator and/or real data that includes potentially more discriminatory covariates like the injured body part. As we are more interested in the formulation of the RL model itself, we have decided to work without covariates, and leave this for future work.
3. 3.

   Train-test Split Construction: We noticed that a feature of SPLICE simulated data, when split temporally, is such that the claim sizes for claims in the test set are, on average, larger than those in the training set. An explanation for this is that by construction of our train-test split, the claims in the test set are those that have been reported in the training set time interval, but not yet settled. These would, on average, be claims with longer duration until settlement, and hence, tend to also be larger claims. Although realistic, this need not hold in practice, as these characteristics would depend on the line of business, but nonetheless, it appears to hold for the SPLICE simulated data. If we are to believe the rarity of large claims hypothesis, then this means that we would also underestimate the test set simply because it consists of larger claims than average.
4. 4.

   Pricing Literature & Auto-Calibration: There is a strand of literature that discusses bias for pricing, and we discuss two things here. Firstly, there is a strand of literature pertaining to auto-calibration (Denuit et al., [2021](https://arxiv.org/html/2601.07637v1#bib.bib23); Wüthrich and Ziegel, [2024](https://arxiv.org/html/2601.07637v1#bib.bib70)). This is concerned primarily with addressing “cross-financing”, where some lines of business (LoBs) are overestimated and while others are underestimated. The objective of auto-calibration is then not to correct a large global bias, but instead to correct these biases between LoBs so that there is less/no cross-financing. This is not applicable in our case since we are concerned with an overall bias rather than, say, varying biases between accident periods. In a sort of adjacent paper, Wüthrich ([2020](https://arxiv.org/html/2601.07637v1#bib.bib69)) considers bias in pricing as well, but in an overall sense rather than just relating to cross-financing. Specifically, it is asserted that mechanisms like early-stopping cause neural networks to violate the balance property, and results in bias at the aggregate level. The proposed solution involves using an additional GLM step with the last hidden layer nodes as covariate inputs to the GLM. This may be worthwhile to pursue as an extension, but we do not consider it in this paper as it is not straightforward to adapt to the RL framework.

## Appendix B Benchmark Models

### B.1 Chain-Ladder

To compare the RL model’s performance against Chain ladder, we use complexity 1 data generated from SPLICE, where chain ladder is expected to perform very well. Given that the RL model concerns RBNS claims only, we must strip out the IBNR claims from the chain ladder predictions for a fair comparison. For this, we follow the approach set out by Delong and Wüthrich ([2020](https://arxiv.org/html/2601.07637v1#bib.bib21)).

1. 1.

   Aggregate the data into cumulative triangles for claim counts and cumulative paid amounts.
2. 2.

   Fit a simple Chain Ladder model.
3. 3.

   Project the ultimate paid and ultimate counts for each accident year ii, then compute the average ultimate claim size μi\mu\_{i} for each accident year by taking the quotient.
4. 4.

   However, claims with longer reporting delays are often larger on average. So we fit a GAM to all the claims incurred (case estimates) available at the cutoff date T∗T^{\*} that gives the scaling factor s​(d)s(d) standardised for s​(0)=1s(0)=1. That is, given a reporting delay dd, how much do we need to scale the average ultimate claims size μi\mu\_{i} by compared to if there was zero delay.
5. 5.

   For each accident period, the number of IBNR claims is the projected ultimate count less the currently already observed count. Multiply this by μ×s​(d)\mu\times s(d), where dd is the reporting delay for the IBNR amount outstanding. I.e., the estimate of IBNR amount outstanding for accident period ii is:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∑j(the incremental number of claims for each development period ​j)×μi×s​(d)\sum\_{j}(\text{the incremental number of claims for each development period }j)\times\mu\_{i}\times s(d) |  | (B.1) |

   where d=j−1d=j-1.
6. 6.

   The total RBNS portion of the UL is simply the total UL less the IBNR portion of the UL. However, this is the RBNS ultimate loss for all claims, which includes those that have already settled. We need to remove the claims that settle in the training set when comparing with RL.

Once we have done this, we can compare the RBNS portion of the OCL (UL less cumulative paid) in chain ladder with the RL predictions by accident year aggregates.

### B.2 FNN

We refer to Wuthrich et al. ([2025](https://arxiv.org/html/2601.07637v1#bib.bib67)) and Goodfellow et al. ([2017](https://arxiv.org/html/2601.07637v1#bib.bib31)) for details on feed-forward neural networks.

We fit a fully-connected FNN to the same claims dataset that the RL model sees. For a direct comparison, the train test split used for RL is also used for FNN. However, because the FNN targets the OCL, it can only train on claims that have already been fully settled in the training set (so that we have targets to work with). As such, we strip the training set of any claims that are not settled by the end of the training interval. We are training the FNN to minimise the importance weighted MSE ([6.1](https://arxiv.org/html/2601.07637v1#S6.E1 "In 6.1 Bias correction for supervised methods ‣ 6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving")).

Each claim can contribute multiple observations to the training set. If a claim has JJ development periods and its reporting delay is dd periods, then it contributes J−dJ-d observations to the training set since we can use each known development of the claim to train. This is a practice done in the literature in various forms when working with individual claims data (Schwab and Schneider, [2024](https://arxiv.org/html/2601.07637v1#bib.bib58); Gabrielli, [2021](https://arxiv.org/html/2601.07637v1#bib.bib28); Delong et al., [2022](https://arxiv.org/html/2601.07637v1#bib.bib20); Chaoubi et al., [2023](https://arxiv.org/html/2601.07637v1#bib.bib17)), and is necessary for good performance. Of course, the shortcoming of this approach is that the FNN assumes all training observations are independent, when they clearly are not.

The input nodes for the FNN correspond to the state space of our RL model, except for the past predictions as it is difficult to embed within a vanilla FNN. This is yet another (minor) advantage of RL due to its sequential nature. The number of hidden layers and the number of nodes in a hidden layer are hyperparameters to be tuned. However, it is typical in practice to assume the same number of nodes in every hidden layer to reduce the complexity of hyperparameter tuning. Lastly, there is one output node corresponding to the model’s prediction of the UL.

The FNN hyperparameters that we tune are: the number of hidden layers and how many nodes are in each hidden layer, the batch size, the dropout rate, and the learning rate. The validation procedure for tuning hyperparameters is described in section [5.2](https://arxiv.org/html/2601.07637v1#S5.SS2 "5.2 Rolling Settlement Approach to Hyperparameter Tuning ‣ 5 Data Splitting for Evaluation and Tuning ‣ Reinforcement Learning for Micro-Level Claims Reserving").

## Appendix C Data Description

### C.1 SPLICE Data for the Simulated Study

Simulated data was generated using the default generate\_data() function of SPLICE (Avanzi et al., [2021a](https://arxiv.org/html/2601.07637v1#bib.bib6), [2023](https://arxiv.org/html/2601.07637v1#bib.bib7)), which means we are using the default simulation assumptions outlined in the paper. Each row in the data corresponds to one transaction of a claim, with the following columns. We refer to the original papers by Avanzi et al. ([2021a](https://arxiv.org/html/2601.07637v1#bib.bib6), [2023](https://arxiv.org/html/2601.07637v1#bib.bib7)) for technical details.

* 1.

  claim\_no: the claim number
* 2.

  claim\_size: the ultimate loss (without inflation) of the claim
* 3.

  txn\_time: the continuous transaction time at which the transaction occurred
* 4.

  txn\_type: the transaction type can be one of

  + (a)

    Mi: minor revision to the case estimate
  + (b)

    Ma: major revision to the case estimate
  + (c)

    P: (partial) claim payment
  + (d)

    PMi: payment and minor revision
  + (e)

    PMa: payment and major revision
* 5.

  incurred: the case estimate of the ultimate claim size
* 6.

  OCL: the case estimate of the outstanding claim liabilities
* 7.

  cumpaid: the cumulative amount paid for the claim so far
* 8.

  accident\_period: the accident period of the claim

### C.2 CAS Data

The CAS datasets contain only a subset of the SPLICE features: claim\_no, claim\_size, txn\_time, cumpaid, and accident\_period.

Note that txn\_time is discrete in the CAS datasets (as opposed to continuous in the SPLICE datasets).

## Appendix D Cumulative Share of Outstanding OCL Graphs

![Refer to caption](figs/Cumulative_OCL_share_AP_QSN_CAS.png)


Figure D.1: Cumulative share of outstanding OCL for CAS test data.

![Refer to caption](figs/Cumulative_OCL_share_AP_QSN.png)


Figure D.2: Cumulative share of outstanding OCL for complexity 5 test data (complexity 1 is essentially identical). Note: the periods since notification graph is cut off at 40 for visual purposes, but there are (rare) claims that have not settled by 40 periods since notification.

## Appendix E Effect of Final Payments

Figure [E.1](https://arxiv.org/html/2601.07637v1#A5.F1 "Figure E.1 ‣ Appendix E Effect of Final Payments ‣ Reinforcement Learning for Micro-Level Claims Reserving") shows the relative OCLs for the top 100 claims by size of RL prediction at valuation for dataset 17 (the outlying dataset with an aggregate relative OCL of 2.56 in Figure [3(c)](https://arxiv.org/html/2601.07637v1#S8.F3.sf3 "In Figure 8.3 ‣ 8.1 Performance of RL and Benchmark Models on CAS Test Data ‣ 8 Empirical results on CAS and SPLICE synthetic data ‣ Reinforcement Learning for Micro-Level Claims Reserving")). We compare this to dataset 15, which had an aggregate relative OCL of 1.02. These two graphs suggest that dataset 17 is so outlying because a large proportion of these top 100 predictions happen to overestimate significantly as they were unable to adjust to the final payment that occurred close to the valuation date. Only 36 of the 100 claims in dataset 17 had final payments after the valuation, while there were 56 from dataset 15.

While we think this is a large reason behind dataset 17 being an outlier, in practice, this phenomenon would often be of little significance to insurers since the fact that these are final payments will likely be known to the insurer for most claims.

A related consideration is that we think a large portion of the volatility for RL and FNN is a result of this phenomenon. Without external signals, it is difficult for a method to adjust to a large and sudden change in OCL. This will be interesting to explore in future research.

![Refer to caption](figs/dataset17_rel_ocl.png)


Figure E.1: Relative OCL developments for the top 100 claims predicted by RL at valuation for Dataset 17

![Refer to caption](figs/dataset15_rel_ocl.png)


Figure E.2: Relative OCL developments for the top 100 claims predicted by RL at valuation for Dataset 15

## Appendix F Example of Iteration through State Space

See the Excel file “Single Claim Example” (available upon request
) for an example of evolution through one claim from SPLICE complexity 5 data (claim nn). We also include the table at the bottom of this section. Below, we take just the final development of the claim before its settlement to illustrate the calculations.

1. 1.

   Suppose the current state space that the agent observes is

   State componentCurrent State Space at ​jnA​P=in34D​P=jn13OCL^jn−1$​675621.39txn​\_​typesjn[P]Pjn$​333857repdel1njnpay8AQ3DQjn1past​predictionsjn[332401,436967,448354,556969,675621]casejn$​30615.11\begin{array}[]{ll}\text{State component}&\text{Current State Space at }j\_{n}\\[6.0pt]
   \hline\cr AP=i\_{n}&34\\[4.0pt]
   DP=j\_{n}&13\\[4.0pt]
   \hat{\mathrm{OCL}}\_{j\_{n}-1}&\mathdollar 675621.39\\[4.0pt]
   \mathrm{txn\\_types}\_{j\_{n}}&[P]\\[4.0pt]
   P\_{j\_{n}}&\mathdollar 333857\\[4.0pt]
   \mathrm{repdel}&1\\[4.0pt]
   n\_{j\_{n}}^{\mathrm{pay}}&8\\[4.0pt]
   \mathrm{AQ}&3\\[4.0pt]
   \mathrm{DQ}\_{j\_{n}}&1\\[6.0pt]
   \mathrm{past\ predictions}\_{j\_{n}}&[332401,436967,448354,556969,675621]\\[4.0pt]
   \mathrm{case}\_{j\_{n}}&\mathdollar 30615.11\end{array}

   and the agent predicts OCL^jn=$​675411.78\hat{\text{OCL}}\_{j\_{n}}=\mathdollar 675411.78.
2. 2.

   The agent takes an action ajna\_{j\_{n}} based on the state space observed. This action is obtained from the underlying RL algorithm using what it has learnt so far. Because OCL^j=OCL^j−1​exp⁡(aj)\hat{\text{OCL}}\_{j}=\hat{\text{OCL}}\_{j-1}\exp(a\_{j}) we can back out the action taken as:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ajn=ln⁡(OCL^jnOCL^jn−1)=−0.0003a\_{j\_{n}}=\ln\left(\frac{\hat{\text{OCL}}\_{j\_{n}}}{\hat{\text{OCL}}\_{j\_{n}-1}}\right)=-0.0003 |  | (F.1) |
3. 3.

   The agent then receives a reward signal rτ=12r\_{\tau=12}.

   * (a)

     The claim has not yet settled (it will settle next period), hence, we need to calculate the stability and smoothing reward components. Now, as there is a payment, rstab,12=rsmooth,12=0r\_{\text{stab},12}=r\_{\text{smooth},12}=0. However, we show how they would be calculated if there wasn’t a payment made.

     + i.

       We are at τ=Tn−1=12\tau=T\_{n}-1=12 (one period before settlement), hence

       |  |  |  |
       | --- | --- | --- |
       |  | rstab,12=0−h​(675621+57577,556968+48219)r\_{\text{stab},12}=0-h\left(675621+57577,556968+48219\right) |  |

       Note that the inputs to h​(⋅)h(\cdot) need to be the ultimate losses; therefore, we are doing predicted OCL + cumulative paid to obtain the UL.
     + ii.

       The smoothing reward component is easy to calculate. Just note that more than the warm up number of predictions have been made, and the action space constraint is K=2K=2 in this example. Hence

       |  |  |  |
       | --- | --- | --- |
       |  | rsmooth,12=−1⋅(|−0.0003|ln⁡(2))2r\_{\text{smooth},12}=-1\cdot\left(\frac{\lvert-0.0003\rvert}{\ln(2)}\right)^{2} |  |
   * (b)

     In the coding of the RL environment, as there are no predictions to be made at the settlement period of a claim, raccr\_{\text{acc}} is implemented to be given as at τ=T−1\tau=T-1 periods since notification instead of τ=T\tau=T (settlement).

     Firstly, with C=5C=5 in this example, we have the following accuracy reward without OCL importance weighting.

     |  |  |  |
     | --- | --- | --- |
     |  | racc=5⋅∑τ=112γτ−1⋅h​(OCLτ,OCL^τ)∑τ=112γτ−1r\_{\text{acc}}=5\cdot\frac{\sum\_{\tau=1}^{12}\gamma^{\tau-1}\cdot h\left(\text{OCL}\_{\tau},\hat{\text{OCL}}\_{\tau}\right)}{\sum\_{\tau=1}^{12}\gamma^{\tau-1}} |  |

     where OCLt\text{OCL}\_{t} is the true OCL remaining after tt periods since notification (only known upon settlement).

     However, we then need to apply the OCL importance weighting, so the raccr\_{\text{acc}} component is actually:

     |  |  |  |
     | --- | --- | --- |
     |  | racc=5⋅∑τ=112wτ⋅γτ−1∑τ=112γτ−1⋅h​(OCLτ,OCL^τ)=3.75r\_{\text{acc}}=5\cdot\sum\_{\tau=1}^{12}{w\_{\tau}}\cdot\frac{\gamma^{\tau-1}}{\sum\_{\tau=1}^{12}\gamma^{\tau-1}}\cdot h\left(\text{OCL}\_{\tau},\hat{\text{OCL}}\_{\tau}\right)=3.75 |  |

     Please refer back to Section [6](https://arxiv.org/html/2601.07637v1#S6 "6 Downward Bias Adjustment ‣ Reinforcement Learning for Micro-Level Claims Reserving") for details and definitions.

Table F.1: Example of how RL works with one claim (Note: AQ and DQ are arbitrarily chosen here for illustrative purposes)

AP
 


DP
 


prev

OCL
 


txn

types
 


cum

paid
 


rep

delay
 


n\_pay
 


AQ
 


DQ


 


past preds
 


case

OCL
 


RL

pred
 


True

OCL
 


R

stab
 


R

smooth
 


R

acc

34
2
499175.5
Ma
0.0
1
0
3
2


[0,0,0,0,499175]
289257.2
519377.1
364472.9
-0.0033
-0.0003
0.0000

34
3
519377.1
P
6768.9
1
1
3
2


[0,0,0,499175,519377]
282488.3
484056.6
357704.0
0.0000
0.0000
0.0000

34
4
484056.6

6768.9
1
1
3
4


[0,0,499175,519377,484057]
282488.3
489150.9
357704.0
0.0363
-0.0001
0.0000

34
5
489150.9
P
12678.5
1
2
3
4


[0,499175,519377,484057,489151]
276578.7
348606.7
351794.4
0.0000
0.0000
0.0000

34
6
348606.7
PMi
19322.9
1
3
3
4


[499175,519377,484057,489151,348607]
320783.0
269355.0
345150.0
0.0000
0.0000
0.0000

34
7
269355.0

19322.9
1
3
3
3


[519377,484057,489151,348607,269355]
320783.0
277343.3
345150.0
0.1864
-0.0011
0.0000

34
8
277343.3
P
27497.3
1
4
3
3


[484057,489151,348607,269355,277343]
312608.5
332400.9
336975.5
0.0000
0.0000
0.0000

34
9
332400.9
PMi
37795.6
1
5
3
3


[489151,348607,269355,277343,332401]
326677.3
436967.4
326677.3
0.0000
0.0000
0.0000

34
10
436967.4

37795.6
1
5
3
2


[348607,269355,277343,332401,436967]
326677.3
448353.7
326677.3
0.2418
-0.0012
0.0000

34
11
448353.7
P
48219.6
1
6
3
2


[269355,277343,332401,436967,448354]
316253.3
556969.0
316253.3
0.0000
0.0000
0.0000

34
12
556969.0
P
57578.0
1
7
3
1


[277343,332401,436967,448354,556969]
306894.9
675621.4
306894.9
0.0000
0.0000
0.0000

34
13
675621.4
P
333857.8
1
8
3
1


[332401,436967,448354,556969,675621]
30615.1
675411.8
30615.1
0.0000
0.0000
3.7502

## Appendix G Histograms of actions taken during testing of the RL model

Figures [G.1](https://arxiv.org/html/2601.07637v1#A7.F1 "Figure G.1 ‣ Appendix G Histograms of actions taken during testing of the RL model ‣ Reinforcement Learning for Micro-Level Claims Reserving")–[G.2](https://arxiv.org/html/2601.07637v1#A7.F2 "Figure G.2 ‣ Appendix G Histograms of actions taken during testing of the RL model ‣ Reinforcement Learning for Micro-Level Claims Reserving") were obtained from a complexity 1 SPLICE dataset.

![Refer to caption](figs/action_hist.png)


Figure G.1: exp⁡(aj)∈[0.5,2]\exp(a\_{j})\in[0.5,2] undertaken during training
  
We obtained this graph by plotting the exponential of the actions taken when RL predicted the remaining periods of the complexity 1 test claims

![Refer to caption](figs/hist_exp_action_by_qsn_1_to_10.png)


Figure G.2: exp⁡(aj)∈[0.5,2]\exp(a\_{j})\in[0.5,2] undertaken during training for the first 10 quarters since notification for the complexity 1 test claims

Similarly, for complexity 5 of the SPLICE dataset:

![Refer to caption](figs/action_hist_C5.png)


Figure G.3: exp⁡(aj)∈[0.5,2]\exp(a\_{j})\in[0.5,2] undertaken during training
  
We obtained this graph by plotting the exponential of the actions taken when RL predicted the remaining periods of the complexity 5 test claims

![Refer to caption](figs/action_hist_qsn_C5.png)


Figure G.4: exp⁡(aj)∈[0.5,2]\exp(a\_{j})\in[0.5,2] undertaken during training for the first 10 quarters since notification for the complexity 5 test claims