---
authors:
- Sebastien Lleo
- Wolfgang Runggaldier
doc_id: arxiv:2603.00738v1
family_id: arxiv:2603.00738
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment
  Management with Reinforcement Learning
url_abs: http://arxiv.org/abs/2603.00738v1
url_html: https://arxiv.org/html/2603.00738v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sébastien Lleo111Finance Department and ‘AI, Data Science & Business’ AE, NEOMA Business School, France.
  
Wolfgang Runggaldier222University of Padova, Italy, and Fellow, Institut Louis Bachelier, Paris, France.

###### Abstract

This paper bridges reinforcement learning (RL) and risk-sensitive stochastic control by introducing a tractable exploration mechanism for policy search in risk-sensitive portfolio management, with known and unknown model parameters, that yields an endogenous relative-entropy regularization. We construct a discrete-time risk-sensitive benchmarked investment model. This model combines a factor-based asset universe with periodic portfolio rebalancing. Exploration is incorporated through user-specified Gaussian perturbations to baseline (exploitative) controls. The risk-sensitive stochastic control problem is solved analytically using the Free Energy-Entropy Duality. The Duality recasts the control problem as a linear-quadratic-Gaussian game and introduces a natural penalty for exploration. This approach yields simple sufficiency conditions for optimality. It also induces intuitive bounds on exploration based on risk sensitivity, asset covariance, and rebalancing frequency. Additionally, the optimal investment strategy can be interpreted through the lens of fractional Kelly strategies. By connecting risk-sensitive control theory and RL, this work provides a principled parametric family for policy-gradient implementations, guiding the design of RL methods.

keywords: risk-sensitive control, fractional Kelly strategies, free energy-entropy duality, stochastic games, Linear Quadratic Gaussian games, exploratory controls, portfolio optimization.

JEL classification: C32; C44; C61; C73; G11; G12.

MSC classes: 68T05; 91G10; 91G80; 93E20; 93E35.

## 1 Introduction

This paper addresses the gap between reinforcement learning and risk-sensitive stochastic control by introducing a tractable exploration mechanism for policy search in risk-sensitive portfolio problems, with known and unknown model parameters, that yields an endogenous relative-entropy regularization. The mechanism mirrors the exploration–exploitation trade-off in reinforcement learning. Reinforcement learning and stochastic control, including risk-sensitive control, trace their roots to Bellman’s dynamic programming principle, but their divergent views on the availability of information and the necessity of exploration have created a significant gap between the two approaches. Reinforcement learning considers environments where there is insufficient information at the outset to estimate a model. The exploration-exploitation trade-off then becomes an essential tool for balancing the pursuit of new information (exploration) with the achievement of a goal based on existing knowledge (exploitation). On the other hand, the theory of stochastic control generally focuses on settings with perfect information about the model’s coefficients. In such settings, exploration is typically unnecessary; the optimal policy is purely exploitative. Our work aims to bridge these perspectives within the setting of risk-sensitive portfolio management.

We start from a factor model for an investment universe with mm continuously traded assets. Drifts depend on nn valuation factors estimated at discrete times. Investors rebalance portfolios when factors are estimated, leading to a discrete-time control problem with continuous-time asset dynamics between rebalancing dates. This hybrid continuous/discrete-time approach, similar to that of Stettner ([1999](#bib.bib20)), is consistent with the empirical asset pricing literature, which usually estimates factors monthly, even though assets trade throughout the day. Then, we introduce an investment benchmark, as in Davis and Lleo ([2008](#bib.bib3)); Lleo and Runggaldier ([2024](#bib.bib14)), serving as a performance measure that investors aim to outperform, depending on their degree of risk sensitivity. Finally, we incorporate exploration as a randomized control. Exploration is modeled as a user-specified Gaussian perturbation to the baseline (exploitative) control. This modelling choice is consistent with the treatment in Lleo and Runggaldier ([2026b](#bib.bib16)), and with recent literature on continuous-time reinforcement learning (Wang et al., [2020](#bib.bib23); Wang and Zhou, [2020](#bib.bib22); Jia and Zhou, [2022a](#bib.bib10), [b](#bib.bib11), [c](#bib.bib12); Jia, [2024](#bib.bib9)).

Then, we formulate the benchmark investment management model as a risk-sensitive control problem. Risk-sensitive control possesses appealing features for financial applications: it connects neatly to utility theory, provides a dynamic version of mean–variance optimization, converges to the Kelly criterion in the limit as the risk sensitivity θ→0\theta\to 0, and, for θ>0\theta>0, the risk-sensitive criterion coincides with the entropic risk measure (Lleo and MacLean, [2025](#bib.bib17)). However, risk-sensitive investment management problems are not standard, so they cannot be solved directly. Our paper proposes a new solution technique that draws on the Free Energy–Entropy Duality (FEED) of Dai Pra et al. ([1996](#bib.bib2)). We use the FEED to recast the non-standard control problem as an equivalent linear-quadratic-Gaussian (LQG) stochastic game under an equivalent measure, with a relative-entropy-based penalty. This penalty measures the cost implied by the distance between the physical probability measure and the dual measure, as well as the cost of exploration. Under verifiable sufficient conditions, we then derive an explicit analytical solution of the game: we establish the existence of a saddle point, obtain the optimal controls, and provide backward recursions for the value-function coefficients.

Our solution technique differs from Stettner ([1999](#bib.bib20)), who used a duality argument only to a limited extent to rewrite the original risk-sensitive control problem into one amenable to solution via contraction maps, and from Kuroda and Nagai (2002), who applied a change of measure to transform the risk-sensitive control problem into a linear-exponential-of-quadratic (LEQG) problem. It is similar to Lleo and Runggaldier ([2026b](#bib.bib16)), who also apply the FEED to solve a generic, but standard, LEQG problem. By comparison, our approach fully exploits the FEED to produce an analytical solution to our non-standard risk-sensitive control problem with exploratory controls. Our approach is also advantageous because the penalty for exploration arises naturally as a byproduct of the solution technique, whereas in the continuous-time reinforcement learning literature, this penalty must be specified in the model.

Our approach makes four main contributions: it uncovers intuitive insights into the role of exploration, formulates easy-to-check sufficiency conditions for the existence of a solution, interprets the asset allocation, and reveals a clear connection between risk-sensitive control and reinforcement learning.

First, our approach shows that optimal exploration is unbiased and provides an explicit upper bound on the user-specified exploration covariance. The FEED naturally treats the mean of the exploration distribution as a control. We show that at the saddle point, this control equals 0, so optimal exploration is unbiased. Regarding the user-specified covariance, the sufficient conditions provide an intuitive upper bound that depends inversely on the investor’s risk sensitivity, the diffusion matrix of the risky assets, Σ​Σ′\Sigma\Sigma^{\prime}, and the time interval between two rebalancing dates. Investors with greater risk sensitivity explore less, while those with lower risk sensitivity explore more, as one would expect. In the limiting case, Kelly investors face no risk-sensitivity-induced bounds on exploration. Moreover, investors should be more cautious with exploration when the covariance of financial asset returns is high. Intuitively, in a factor model, investors buy assets to achieve optimal exposure to the underlying factors. Thus, asset return volatility creates variability around the factor exposure, resulting in natural exploration. The exploration covariance bound accounts for this exploration naturally. Additionally, investors with shorter time between rebalancing dates can explore more. When rebalancing occurs more frequently, investors learn more from exploration, and they can correct suboptimal asset allocations more rapidly.

Second, the main characterization of the optimal controls provides simple and easily interpretable sufficient conditions: the investment universe cannot have redundant assets (a standard condition in portfolio optimization), and the projected curvature of the value function restricted to the noise subspace has all eigenvalues strictly smaller than one (a standard condition for LQG control problems). Using an alternative characterization of the optimal controls, we also show that these simple sufficient conditions can be recast as a different set of sufficient conditions articulated around the risk-resistance condition (a standard condition in the risk-sensitive control literature Shaiju and Petersen, [2008](#bib.bib19); Whittle, [1990](#bib.bib24)).

Third, using our alternative strategy characterization, we interpret optimal portfolio allocations through the lens of fractional Kelly strategies. In continuous-time investment, fractional Kelly strategies are a fixed-mix investment in the Kelly portfolio, a benchmark-tracking portfolio, and an intertemporal-hedging portfolio (Davis and Lleo, [2008](#bib.bib3); Lleo and Runggaldier, [2026a](#bib.bib15)). In our discrete-time setting, the optimal investment is a rotated and rescaled fractional Kelly strategy, with the mix determined by time-dependent matrices. Moreover, these matrices reflect the risk-resistance condition and the LQG curvature condition.

Finally, our approach bridges risk-sensitive control and reinforcement learning. We illustrate this idea in the policy gradient framework of Hambly et al. ([2021](#bib.bib6), [2023a](#bib.bib7)) and in an actor-critic approach. If our market and model parameters could be estimated with high accuracy, we could solve the risk-sensitive control problem directly using the recursions in Theorem [3.11](#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). However, in practice, estimating the model parameters is notoriously difficult, especially the expected returns. Reinforcement learning bypasses the traditional statistical estimation of the model parameters, learning a parameterized form of the policy and value functions directly from market data. Therefore, the main purpose of our study of the risk-sensitive benchmarked investment model is to capture the essential features of financial markets, to characterize their fundamental relations, and to provide a principled parametric family for policy-gradient implementations. These insights are invaluable in guiding the design of reinforcement learning methods.

## 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem

Let (Ω,ℱ,(ℱs)s∈[0,T],ℙ)\left(\Omega,\mathcal{F},\left(\mathcal{F}\_{s}\right)\_{s\in[0,T]},\mathbb{P}\right) be a filtered complete probability space. We introduce
a ℝd\mathbb{R}^{d}-valued ℱs\mathcal{F}\_{s}-Wiener process WsW\_{s} with components Wsi,i=1,…​dW^{i}\_{s},i=1,\ldots d, with d:=n+m+1d:=n+m+1, where n≥1n\geq 1 is the number of factors, m≥1m\geq 1 is the number of financial assets, and the additional dimension accounts for the residual stochastic component of the benchmark return that cannot be replicated through the traded assets333If the benchmark is perfectly spanned by the traded assets, no additional source of uncertainty is needed and one may take d:=n+md:=n+m..

We consider an investor who rebalances her portfolio on a fixed regular schedule (e.g., daily, weekly, or monthly). Let 0=t0<t1<⋯<tk<…<tK=T0=t\_{0}<t\_{1}<\dots<t\_{k}<\ldots<t\_{K}=T denote the rebalancing dates, and let Δ​t:=tk+1−tk\Delta t:=t\_{k+1}-t\_{k}. We model the investor’s self-financing investment *strategy* as a piecewise constant, right continuous ℱs\mathcal{F}\_{s}-adapted process H=(hs)s∈[0,T]∈ℝmH=\left(h\_{s}\right)\_{s\in[0,T]}\in\mathbb{R}^{m} such that the *control* hs=hkh\_{s}=h\_{k} on each interval [tk,tk+1),k=0,…,K−1[t\_{k},t\_{k+1}),k=0,\ldots,K-1 and hkh\_{k} is chosen at time tkt\_{k}.

### 2.1 Model for the Financial Market

We adopt a hybrid-time specification that combines discrete-time factor dynamics, continuous-time asset prices, and discrete-time control updates. Factors are observed, and controls are updated at the rebalancing dates, while asset and benchmark prices evolve continuously between rebalancing times.

1. Risky Financial Assets
  
The investor can trade mm risky financial assets (Ss1,…,Ssm)=:(Ss)s∈[0,T]\left(S^{1}\_{s},\ldots,S^{m}\_{s}\right)=:\left(S\_{s}\right)\_{s\in[0,T]} to constitute a portfolio. In this paper, we assume that all prices, benchmark level, and wealth are expressed in discounted units, with discounting performed at the prevailing short-term interest rate. The prices of the risky financial assets follow geometric dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StiSti=(a+A​Xk)i​d​t+∑j=1dσi​j​d​Wtj,i=1,…,m;t∈[tk,tk+1),k=0,…,K−1\displaystyle\frac{dS^{i}\_{t}}{S^{i}\_{t}}=(a+AX\_{k})\_{i}dt+\sum\_{j=1}^{d}\sigma\_{ij}dW^{j}\_{t},\quad i=1,\ldots,m;\quad t\in[t\_{k},t\_{k+1}),k=0,\ldots,K-1 |  | (2.1) |

where a∈ℝma\in\mathbb{R}^{m}, A∈ℝm×nA\in\mathbb{R}^{m\times n}, and Σ:=(σi​j)∈ℝm×d\Sigma:=(\sigma\_{ij})\in\mathbb{R}^{m\times d}, and where the factor process XkX\_{k} is defined next. In particular, an application of Itô’s lemma shows that for t∈[tk,tk+1),k=0,…,K−1t\in[t\_{k},t\_{k+1}),k=0,\ldots,K-1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sti=Stki​exp⁡{[(a+A​Xk)i−12​∑j=1dσi​j2]​(t−tk)+∑j=1dσi​j​(Wtj−Wtkj)},i=1,…,m.\displaystyle S^{i}\_{t}=S^{i}\_{t\_{k}}\exp\left\{\left[(a+AX\_{k})\_{i}-\frac{1}{2}\sum\_{j=1}^{d}\sigma\_{ij}^{2}\right](t-t\_{k})+\sum\_{j=1}^{d}\sigma\_{ij}(W^{j}\_{t}-W^{j}\_{t\_{k}})\right\},\quad i=1,\ldots,m. |  | (2.2) |

We assume that no two assets have an identical risk profile:

###### Assumption 2.1.

The matrix Σ​Σ′\Sigma\Sigma^{\prime} is positive definite.

2. Factor Process
  
The nn valuation factors (Xt1,…,Xtn)=:(Xk)t∈{t0,…,tK}\left(X^{1}\_{t},\ldots,X^{n}\_{t}\right)=:\left(X\_{k}\right)\_{t\in\{t\_{0},\ldots,t\_{K}\}} are typically empirical asset pricing factors, macroeconomic factors, fundamental factors, or statistical factors. Following Stettner ([1999](#bib.bib20)), we model the first difference of the factors as a discrete-time first-order autoregressive (AR(1)) process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk+1−Xk=(b+B​Xk)​Δ​t+Λ​wk,\displaystyle X\_{k+1}-X\_{k}=(b+BX\_{k})\Delta t+\Lambda w\_{k}, |  | (2.3) |

where we used the notational shortcut XkX\_{k} for the value XtkX\_{t\_{k}} of the factor process at time tkt\_{k}, and where b∈ℝnb\in\mathbb{R}^{n}, B∈ℝn×nB\in\mathbb{R}^{n\times n}, and Λ∈ℝn×d\Lambda\in\mathbb{R}^{n\times d}. The noise term wk:=(Wk+1−Wk)w\_{k}:=(W\_{k+1}-W\_{k}) is the increment of the Brownian motion WW, where WkW\_{k} denotes WtkW\_{t\_{k}}, the value of the Brownian motion at time tkt\_{k}. Consequently, wkw\_{k} is Gaussian with mean equal to 0 and covariance equal to Δ​t​Id\Delta tI\_{d}, where IdI\_{d} is the dd-dimensional identity matrix. Hence, the drift term is scaled by Δ​t\Delta t, while the innovation term inherits covariance Δ​t​Id\Delta t\,I\_{d} from Brownian increments.

This assumption is less restrictive than it appears. The empirical asset pricing literature typically estimates its models with a monthly frequency. A monthly frequency is also a popular choice in the portfolio optimization literature. However, asset prices evolve continuously.

We clean up the notation by introducing B~:=In+B​Δ​t\tilde{B}:=I\_{n}+B\Delta t to express444No stability restriction on B~\tilde{B} is needed for the finite-horizon analysis below. Stronger assumptions may be imposed in infinite-horizon extensions. ([2.3](#S2.E3 "In 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk+1=b​Δ​t+B~​Xk+Λ​wk.\displaystyle X\_{k+1}=b\Delta t+\tilde{B}X\_{k}+\Lambda w\_{k}. |  | (2.4) |

We shall refer to the process (Xtk)k=0,…,K(X\_{t\_{k}})\_{k=0,\ldots,K} as the *state* process.

3. Benchmark Index
  
The investor manages a portfolio of financial assets against a benchmark index, typically a financial index or a custom-built passive portfolio. We model the benchmark’s (discounted) level (Ls)s∈[0,T]\left(L\_{s}\right)\_{s\in[0,T]} as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​LtLt=(c+C​Xk)​d​t+Ξ′​d​Wt,t∈[tk,tk+1),k=0,…,K−1\displaystyle\frac{dL\_{t}}{L\_{t}}=(c+CX\_{k})dt+\Xi^{\prime}dW\_{t},\quad t\in[t\_{k},t\_{k+1}),k=0,\ldots,K-1 |  | (2.5) |

where c∈ℝc\in\mathbb{R}, C∈ℝnC\in\mathbb{R}^{n}, and Ξ∈ℝd\Xi\in\mathbb{R}^{d}.

### 2.2 Risk-Sensitive Control Problem

1. Wealth Process
  
The wealth process (Vs)s∈[0,T]\left(V\_{s}\right)\_{s\in[0,T]} solves the SDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​VsVs\displaystyle\frac{dV\_{s}}{V\_{s}} | =hk′​(a+A​Xk)​d​s+hk′​Σ​d​Ws,\displaystyle=h\_{k}^{\prime}\left(a+AX\_{k}\right)ds+h\_{k}^{\prime}\Sigma dW\_{s}, |  | (2.6) |

for s∈[tk,tk+1),k=0,…,K−1s\in[t\_{k},t\_{k+1}),k=0,\ldots,K-1 and where hkh\_{k} denotes the value of the control at time tkt\_{k}. A precise admissibility definition for the control is given in Section [3.1](#S3.SS1 "3.1 Exploratory Controls and the Log-Relative Return Process ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). Here hkh\_{k} denotes the vector of portfolio weights in discounted risky assets at time tkt\_{k}. The residual wealth is invested in the numéraire asset, with a discounted price constant at 1. Unless otherwise stated, short-selling and leverage are allowed. Throughout this section, we assume controls are non-anticipative and satisfy the required integrability conditions.

2. Log Price Relative and Log Excess Return
  
To measure the investment portfolio’s cumulative outperformance relative to its benchmark, we first compute the *log price relative* process (Rs)s∈[0,T]\left(R\_{s}\right)\_{s\in[0,T]}, defined as Rs:=ln⁡VsLsR\_{s}:=\ln\frac{V\_{s}}{L\_{s}}. This process solves the SDE:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Rs\displaystyle dR\_{s} | =[(−12​hk′​Σ​Σ′​hk+hk′​a+12​Ξ′​Ξ−c)+(hk′​A−C)​Xk]​d​s+(hk′​Σ−Ξ′)​d​Ws.\displaystyle=\left[\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right]ds+\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)dW\_{s}. |  | (2.7) |

for s∈[tk,tk+1),k=0,…,K−1s\in[t\_{k},t\_{k+1}),k=0,\ldots,K-1. Hence, at the terminal time TT,

|  |  |  |  |
| --- | --- | --- | --- |
|  | RT=\displaystyle R\_{T}= | R0+∑k=0K−1∫tktk+1{(−12​hk′​Σ​Σ′​hk+hk′​a+12​Ξ′​Ξ−c)+(hk′​A−C)​Xk}​𝑑s\displaystyle R\_{0}+\sum\_{k=0}^{K-1}\int\_{t\_{k}}^{t\_{k+1}}\left\{\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right\}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑k=0K−1∫tktk+1(hk′​Σ−Ξ′)​𝑑Ws\displaystyle+\sum\_{k=0}^{K-1}\int\_{t\_{k}}^{t\_{k+1}}\ \left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)dW\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | R0+∑k=0K−1{(−12​hk′​Σ​Σ′​hk+hk′​a+12​Ξ′​Ξ−c)+(hk′​A−C)​Xk}​Δ​t\displaystyle R\_{0}+\sum\_{k=0}^{K-1}\left\{\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right\}\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∑k=0K−1(hk′​Σ−Ξ′)​wk.\displaystyle+\sum\_{k=0}^{K-1}\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)w\_{k}. |  | (2.8) |

Using a benchmarked log-relative process is natural for active portfolio management, as it directly evaluates cumulative outperformance net of the benchmark and yields a state reduction through elimination of wealth. From the log price relative process, we obtain the cumulative *log excess return* of the portfolio over its benchmark as the difference RT−R0R\_{T}-R\_{0} of log price relatives. Conditional on the sequence {Xk,hk}k=0K−1\left\{X\_{k},h\_{k}\right\}\_{k=0}^{K-1}, the increments of Rt−R0R\_{t}-R\_{0} over the rebalancing intervals are independent Gaussian random variables. It follows that RT−R0R\_{T}-R\_{0} is conditionally Gaussian, so its conditional exponential moment admits a closed-form expression.

3. Risk-Sensitive Benchmarked
Criteria
  
The investor seeks to maximize the risk-sensitive benchmarked criterion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(H,θ)\displaystyle J(H,\theta) | :=−1θ​ln⁡𝐄​[e−θ​(RT−R0)]\displaystyle:=-\frac{1}{\theta}\ln\mathbf{E}\left[e^{-\theta(R\_{T}-R\_{0})}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−1θln𝐄[exp{−θ∑k=0K−1{(−12hk′ΣΣ′hk+hk′a+12Ξ′Ξ−c)+(hk′A−C)Xk}Δt\displaystyle=-\frac{1}{\theta}\ln\mathbf{E}\left[\exp\left\{-\theta\sum\_{k=0}^{K-1}\left\{\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right\}\Delta t\right.\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −θ∑k=0K−1(hk′Σ−Ξ′)wk}],\displaystyle\left.\left.-\theta\sum\_{k=0}^{K-1}\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)w\_{k}\right\}\right], |  | (2.9) |

where θ\theta is the risk sensitivity parameter, T<∞T<\infty is a fixed time horizon. Here, we focus on the risk-averse case θ>0\theta>0. Note that the state (factor) process XkX\_{k} is the sufficient state variable. Wealth has been eliminated through the log-relative formulation.

We also introduce the exponentially-transformed criterion I​(H,θ)I(H,\theta) to be minimized,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(H,θ)\displaystyle I(H,\theta) | :=e−θ​J​(H,θ)=𝐄​[e−θ​(RT−R0)].\displaystyle:=e^{-\theta J(H,\theta)}=\mathbf{E}\left[e^{-\theta(R\_{T}-R\_{0})}\right]. |  | (2.10) |

Together, the discrete-time state process at ([2.3](#S2.E3 "In 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and the criteria ([2.2](#S2.Ex4 "2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))-([2.10](#S2.E10 "In 2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) constitute a non-standard discrete-time risk-sensitive control problem.
The criterion is non-standard in two respects: 1) the control does not steer the state dynamics; and 2) the control and Brownian increments interact inside the exponential payoff. Consequently, unlike in more standard formulations, the stochastic integral term cannot be eliminated by taking conditional expectations.

4. Randomized Exploratory Control
  
Up to this point, hkh\_{k} denotes a standard ℱtk\mathcal{F}\_{t\_{k}}-adapted control. We now introduce randomized controls to model exploration in the spirit of reinforcement learning. Specifically, we consider randomized controls of the form hk=h¯k+vkh\_{k}=\bar{h}\_{k}+v\_{k}, where a baseline control h¯k\bar{h}\_{k} is perturbed by a Gaussian shock vk∈ℝmv\_{k}\in\mathbb{R}^{m}, independent of ℱtk\mathcal{F}\_{t\_{k}}, thereby capturing an exploitation, via h¯k\bar{h}\_{k}, and exploration, via vkv\_{k}, within the risk-sensitive benchmarked portfolio problem.

###### Definition 2.2 (Randomized Exploratory Control).

A piecewise-constant ℝm\mathbb{R}^{m}-valued control process (hs)s∈[0,T](h\_{s})\_{s\in[0,T]} is a *randomized exploratory control* if, for each k=0,…,K−1k=0,\dots,K-1 and s∈[tk,tk+1)s\in[t\_{k},t\_{k+1}), it admits the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | hs=h¯k+vk,\displaystyle h\_{s}=\bar{h}\_{k}+v\_{k}, |  | (2.11) |

where h¯k\bar{h}\_{k} is ℱtk\mathcal{F}\_{t\_{k}}-measurable, and vk∼𝒩​(0,Ψk)v\_{k}\sim\mathcal{N}(0,\Psi\_{k}), with deterministic positive definite covariance Ψk∈ℝm×m\Psi\_{k}\in\mathbb{R}^{m\times m}, is serially independent across kk and independent of ℱtk\mathcal{F}\_{t\_{k}}.

In particular, the perturbation vkv\_{k} is independent of wkw\_{k}, and more generally independent of the Brownian motion WW. Hence, exploration does not implicitly anticipate market noise. Additionally, admissible strategies remain non-anticipative and compatible with Markov dynamic programming. Hence, the randomized control is of the form hk=h¯k+vk∼𝒩​(h¯k,Ψk)h\_{k}=\bar{h}\_{k}+v\_{k}\sim\mathcal{N}\left(\bar{h}\_{k},\Psi\_{k}\right) and it admits a representation as a measure π​(d​h;h¯k)∼𝒩​(h¯k,Ψk)\pi\left(dh;\bar{h}\_{k}\right)\sim\mathcal{N}\left(\bar{h}\_{k},\Psi\_{k}\right).

###### Remark 1.

Allowing the covariance matrix Ψk\Psi\_{k} to vary with time tkt\_{k} opens the possibility to reduce the breadth of exploration over time, consistent with the reinforcement learning literature. Exploration is more valuable in early times when little information is available. As more information becomes available, exploration gradually loses its value.

### 2.3 Free Energy, Relative Entropy, and the Energy-Entropy Duality

The following notions from Dai Pra et al. ([1996](#bib.bib2)) will be used in Section [3.2](#S3.SS2 "3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") to reformulate the risk-sensitive control problem with criterion I​(H,θ)I(H,\theta) as an equivalent Linear-Quadratic-Gaussian stochastic differential game.

###### Definition 2.3 (Free Energy).

The *free energy* of a random variable ψ\psi with respect to a reference measure ℙ\mathbb{P} is defined, under the integrability condition 𝐄ℙ​[eψ]<∞\mathbf{E}^{\mathbb{P}}[e^{\psi}]<\infty, as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰℙ​{ψ}:=ln⁡𝐄ℙ​[eψ]=ln⁡(∫eψ​𝑑ℙ).\displaystyle\mathcal{E}^{\mathbb{P}}\{\psi\}:=\ln\mathbf{E}^{\mathbb{P}}\left[e^{\psi}\right]=\ln\left(\int e^{\psi}\,d\mathbb{P}\right). |  | (2.12) |

###### Definition 2.4 (Relative Entropy / Kullback-Leibler Divergence).

Consider a probability measure ℙγ\mathbb{P}^{\gamma} that is *absolutely continuous* with respect to ℙ\mathbb{P}. The *relative entropy* of ℙγ\mathbb{P}^{\gamma} with respect to ℙ\mathbb{P} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(ℙγ∥ℙ):=𝐄γ​[ln⁡d​ℙγd​ℙ]=𝐄γ​[ln⁡ℒγ],\displaystyle D\_{\rm KL}\left(\mathbb{P}^{\gamma}\,\|\,\mathbb{P}\right):=\mathbf{E}^{\gamma}\left[\ln\frac{d\mathbb{P}^{\gamma}}{d\mathbb{P}}\right]=\mathbf{E}^{\gamma}\left[\ln\mathcal{L}^{\gamma}\right], |  | (2.13) |

where ℒγ:=d​ℙγd​ℙ\mathcal{L}^{\gamma}:=\frac{d\mathbb{P}^{\gamma}}{d\mathbb{P}} denotes the Radon-Nikodym derivative and 𝐄γ​[⋅]\mathbf{E}^{\gamma}[\cdot] is the expectation under ℙγ\mathbb{P}^{\gamma}.

###### Proposition 2.5 (Free Energy-Entropy Duality, (Dai Pra et al., [1996](#bib.bib2), Prop. 2.3(ii))).

Let ψ\psi be a measurable random variable such that 𝐄ℙ​[eψ]<∞\mathbf{E}^{\mathbb{P}}[e^{\psi}]<\infty. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰℙ​{ψ}=supℙγ≪ℙ{𝐄γ​[ψ]−DKL​(ℙγ∥ℙ)},\displaystyle\mathcal{E}^{\mathbb{P}}\{\psi\}=\sup\_{\mathbb{P}^{\gamma}\ll\mathbb{P}}\left\{\mathbf{E}^{\gamma}[\psi]-D\_{\rm KL}(\mathbb{P}^{\gamma}\,\|\,\mathbb{P})\right\}, |  | (2.14) |

where the supremum is taken over all probability measures ℙγ\mathbb{P}^{\gamma} absolutely continuous with respect to ℙ\mathbb{P}.

###### Remark 2.

Under suitable conditions, the supremum in ([2.14](#S2.E14 "In Proposition 2.5 (Free Energy-Entropy Duality, (Dai Pra et al., 1996, Prop. 2.3(ii))). ‣ 2.3 Free Energy, Relative Entropy, and the Energy-Entropy Duality ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) is attained at a measure ℙγ∗\mathbb{P}^{\gamma^{\*}} whose Radon-Nikodym derivative with respect to ℙ\mathbb{P} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒγ∗:=d​ℙγ∗d​ℙ=eψ𝐄ℙ​[eψ].\displaystyle\mathcal{L}^{\gamma^{\*}}:=\frac{d\mathbb{P}^{\gamma^{\*}}}{d\mathbb{P}}=\frac{e^{\psi}}{\mathbf{E}^{\mathbb{P}}[e^{\psi}]}. |  | (2.15) |

This expresses the optimal change of measure in terms of the exponential of the random variable ψ\psi and ensures that the transformed measure is properly normalized.

## 3 Solution Via The Free Energy-Entropy Duality

We now derive a solution for the randomized risk-sensitive control problem associated with the criteria ([2.2](#S2.Ex4 "2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))-([2.10](#S2.E10 "In 2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and the state dynamics at ([2.4](#S2.E4 "In 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")). As announced above, we use the energy-entropy duality to associate with the risk-sensitive control problem, set with respect to an initial measure ℙ\mathbb{P}, a risk-neutral randomized stochastic game, set with respect to a transformed measure ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}. This risk-neutral randomized stochastic game turns out to be penalized by an appropriate relative entropy term.

As a reference for the reader, Table [1](#S3.T1 "Table 1 ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") lists the key variables and parameters used in Sections 2 and 3.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Variable/ | Dimension | Update time | Definition | Introduced |
| parameter |  | (discrete/continuous) |  | in section |
| Market variables: | | | | |
| XkX\_{k} | ℝn\mathbb{R}^{n} | Discrete | Valuation factor (state variable) | 2.1 |
| SsS\_{s} | ℝm\mathbb{R}^{m} | Continuous | Financial asset discounted price | 2.1 |
| LsL\_{s} | ℝ\mathbb{R} | Continuous | Benchmark level | 2.1 |
| VsV\_{s} | ℝ\mathbb{R} | Continuous | Wealth process | 2.1 |
| RsR\_{s} | ℝ\mathbb{R} | Continuous | Log price relative Rs:=ln⁡(Vs/Ls)R\_{s}:=\ln\left(V\_{s}/L\_{s}\right) | 2.1 |
| Under the measure ℙ\mathbb{P}: | | Xk+1=b​Δ​t+B~​Xk+Λ​wkX\_{k+1}=b\Delta t+\tilde{B}X\_{k}+\Lambda w\_{k} | | |
|  | | RT−R0=∑k=0K−1{(−12​hk′​Σ​Σ′​hk+hk′​a+12​Ξ′​Ξ−c)+(hk′​A−C)​Xk}​Δ​t+∑k=0K−1(hk′​Σ−Ξ′)​wkR\_{T}-R\_{0}=\sum\_{k=0}^{K-1}\left\{\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right\}\Delta t+\sum\_{k=0}^{K-1}\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)w\_{k} | | |
| WsW\_{s} | ℝd\mathbb{R}^{d} | Continuous | ℱs\mathcal{F}\_{s}-Wiener process on (Ω,ℱ,(ℱs)s∈[0,T],ℙ)\left(\Omega,\mathcal{F},\left(\mathcal{F}\_{s}\right)\_{s\in[0,T]},\mathbb{P}\right) | 2 |
|  | d=n+m+1d=n+m+1 |  |  |  |
| hkh\_{k} | ℝm\mathbb{R}^{m} | Discrete | 1. Generic control for the initial problem | 2.1 |
|  |  |  | 2. Exploratory control: hk=h¯k+vt∼𝒩​(h¯k,Ψk)h\_{k}=\bar{h}\_{k}+v\_{t}\sim\mathcal{N}\left(\bar{h}\_{k},\Psi\_{k}\right) | 2.2 |
| h¯t\bar{h}\_{t} | ℝm\mathbb{R}^{m} | Discrete | Deterministic control | 2.2 |
| vkv\_{k} | ℝm\mathbb{R}^{m} | Discrete | Exploration noise: | 2.2 |
|  |  |  | vk∼𝒩​(0,Ψk)v\_{k}\sim\mathcal{N}\left(0,\Psi\_{k}\right) |  |
| J​(H,θ)J(H,\theta) | ℝ\mathbb{R} | Discrete | Control criterion: J​(H,θ):=−1θ​ln⁡𝐄​[e−θ​(RT−R0)]J(H,\theta):=-\frac{1}{\theta}\ln\mathbf{E}\left[e^{-\theta(R\_{T}-R\_{0})}\right] | 2.1 |
| I​(H,θ)I(H,\theta) | ℝ\mathbb{R} | Discrete | Control criterion: I​(H,θ):=exp⁡{−θ​J​(H,θ)}=𝐄​[e−θ​(RT−R0)]I(H,\theta):=\exp\left\{-\theta J(H,\theta)\right\}=\mathbf{E}\left[e^{-\theta(R\_{T}-R\_{0})}\right] | 2.1 |
| Under the measure ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}: | | Xk+1=b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t+Λ​wkγ¯X\_{k+1}=b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t+\Lambda w^{\bar{\gamma}}\_{k} | | |
|  | | R¯Tπ−R0=∑k=0K−1{(−12(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)−12tr(ΨkΣΣ′)+(h¯k+η¯k)′a+12Ξ′Ξ−c)\bar{R}^{\pi}\_{T}-R\_{0}=\sum\_{k=0}^{K-1}\Bigg\{\left(-\frac{1}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)-\frac{1}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)+\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right) | | |
|  | | +((h¯k+η¯k)′A−C)Xk+((h¯k+η¯k)′Σ−Ξ′)γ¯k}Δt+∑k=0K−1((h¯k+η¯k)′Σ−Ξ′)wγ¯k.\phantom{R\_{T}-R\_{0}=}+\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}+\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}\Bigg\}\Delta t+\sum\_{k=0}^{K-1}\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)w^{\bar{\gamma}}\_{k}. | | |
| γ¯k\bar{\gamma}\_{k} | ℝd\mathbb{R}^{d} | Discrete | Change of measure process (control) | 3.2 |
| η¯k\bar{\eta}\_{k} | ℝm\mathbb{R}^{m} | Discrete | Change of measure process (control) | 3.2 |
| Wsγ¯W^{\bar{\gamma}}\_{s} | ℝd\mathbb{R}^{d} | Continuous | ℱs\mathcal{F}\_{s}-Wiener process Wsγ¯:=Ws−∫0sγ¯u​𝑑u,W^{\bar{\gamma}}\_{s}:=W\_{s}-\int\_{0}^{s}\bar{\gamma}\_{u}\,du, | 3.2 |
| vkη¯v^{\bar{\eta}}\_{k} | ℝm\mathbb{R}^{m} | Continuous | Exploration noise: vkη¯∼𝒩​(η¯k,Ψk)v^{\bar{\eta}}\_{k}\sim\mathcal{N}\left(\bar{\eta}\_{k},\Psi\_{k}\right) | 3.2 |
| Value function for the stochastic differential game: | | | | |
| u0​(x0)u\_{0}(x\_{0}) | ℝ\mathbb{R} | Discrete | Value of the stochastic differential game: | 3.3 |
|  |  |  | u0​(x0):=infh¯∈𝒜¯explHsupγ¯,η¯𝐄γ¯,η¯​[θ​∑k=0K−1g​(Xk,h¯k,η¯k,γ¯k)​Δ​t]u\_{0}(x\_{0}):=\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\sup\_{\bar{\gamma},\bar{\eta}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t\Bigg] |  |
| uk​(Xk)u\_{k}(X\_{k}) | ℝ\mathbb{R} | Discrete | Recursive quadratic expression: | 3.3 |
|  |  |  | uk​(Xk)=infh¯∈𝒜¯explHsupγ¯,η¯{θ​g​(Xk,h¯k,η¯k,γ¯k)​Δ​t+𝐄k,Xkγ¯,η¯​[Vk+1​(Xk+1)]}u\_{k}(X\_{k})=\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\sup\_{\bar{\gamma},\bar{\eta}}\left\{\theta g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t+\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[V\_{k+1}(X\_{k+1})\right]\right\} | 3.3 |
|  |  |  | =Xk′​Pk​Xk+Xk′​pk+rk\phantom{u\_{k}(X\_{k}):}=X\_{k}^{\prime}P\_{k}X\_{k}+X\_{k}^{\prime}p\_{k}+r\_{k} | 3.3 |
| Shorthand notation | | | | |
| 𝒜k+1\mathcal{A}\_{k+1} | ℝd\mathbb{R}^{d} | Discrete | 𝒜k+1=Λ′​Pk+1​Λ​Δ​t−Id\mathcal{A}\_{k+1}=\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d} | 3.3 |
| ℬk+1\mathcal{B}\_{k+1} | ℝd\mathbb{R}^{d} | Discrete | ℬk+1:=θ​Σ′​(Σ​Σ′)−1​Σ−𝒜k+1\mathcal{B}\_{k+1}:=\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma-\mathcal{A}\_{k+1} | 3.3 |
| 𝒞k+1​(θ)\mathcal{C}\_{k+1}\!(\theta) | ℝm\mathbb{R}^{m} | Discrete | 𝒞k+1​(θ)=1θ+1​Σ​[Id−θ​𝒜k+1−1]​Σ′\mathcal{C}\_{k+1}\!(\theta)=\frac{1}{\theta+1}\Sigma\left[I\_{d}-\theta\mathcal{A}\_{k+1}^{-1}\right]\Sigma^{\prime} |  |

Table 1: Key variables and parameters appearing in Sections 2 and 3

### 3.1 Exploratory Controls and the Log-Relative Return Process

We define the class of exploratory *strategies* and derive a policy-averaged representation of the terminal log-relative return that explicitly reveals the effect of exploration.

###### Definition 3.1 (Class of admissible exploratory strategies 𝒜explH\mathcal{A}^{H}\_{\mathrm{expl}}).

A strategy H=(hs)s∈[0,T]H=(h\_{s})\_{s\in[0,T]} with values in ℝm\mathbb{R}^{m}
belongs to the exploratory admissible class 𝒜explH\mathcal{A}^{H}\_{\mathrm{expl}} if the control process hsh\_{s} is ℱs\mathcal{F}\_{s}-measurable and satisfies the following conditions:

1. (i)

   (hs)s∈[0,T](h\_{s})\_{s\in[0,T]} is a *randomized control* according to Definition [2.2](#S2.Thmtheorem2 "Definition 2.2 (Randomized Exploratory Control). ‣ 2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning").
2. (ii)

   *Square-integrability:*

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼​[‖hk‖2]=𝔼​[‖h¯k‖2]+tr​(Ψk)<+∞,k=0,…,K−1,\displaystyle\mathbb{E}[\|h\_{k}\|^{2}]=\mathbb{E}[\|\bar{h}\_{k}\|^{2}]+\mathrm{tr}(\Psi\_{k})<+\infty,\quad k=0,\dots,K-1, |  | (3.1) |

   where ‖hk‖2:=hk′​hk\|h\_{k}\|^{2}:=h\_{k}^{\prime}h\_{k}.

For our finite-horizon discrete-time representation used below, it is convenient to work on a canonical product-space representation and write the collection of Brownian increments and exploration shocks. We denote elements ω∈Ω\omega\in\Omega of the underlying probability space as

|  |  |  |
| --- | --- | --- |
|  | ω=(ωw,ωv):=(w0,…,wK−1,v0,…,vK−1),\displaystyle\omega=(\omega^{w},\omega^{v}):=(w\_{0},\ldots,w\_{K-1},v\_{0},\ldots,v\_{K-1}), |  |

where wk=Wk+1−Wkw\_{k}=W\_{k+1}-W\_{k} are the Brownian increments and vkv\_{k} are the random perturbations from exploration.

Using the randomized control representation in Definition [2.2](#S2.Thmtheorem2 "Definition 2.2 (Randomized Exploratory Control). ‣ 2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), and conditioning on the state process and Brownian increments, we average over the Gaussian exploratory policy at each rebalancing date to obtain the following policy-averaged terminal log-relative return, which we denote by R¯Tπ\bar{R}\_{T}^{\pi}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R¯Tπ=\displaystyle\bar{R}^{\pi}\_{T}= | R0+∑k=0K−1∫ℝm{−12​hk′​Σ​Σ′​hk+hk′​a+12​Ξ′​Ξ−c+(hk′​A−C)​Xk}​π​(d​h;h¯k)​Δ​t\displaystyle R\_{0}+\sum\_{k=0}^{K-1}\int\_{\mathbb{R}^{m}}\Bigg\{-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c+(h\_{k}^{\prime}A-C)X\_{k}\Bigg\}\pi(dh;\bar{h}\_{k})\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑k=0K−1∫ℝm(hk′​Σ−Ξ′)​wk​π​(d​h;h¯k)\displaystyle+\sum\_{k=0}^{K-1}\int\_{\mathbb{R}^{m}}(h\_{k}^{\prime}\Sigma-\Xi^{\prime})w\_{k}\,\pi(dh;\bar{h}\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | R0+∑k=0K−1{−12​h¯k′​Σ​Σ′​h¯k−12​tr​(Ψk​Σ​Σ′)+h¯k′​a+12​Ξ′​Ξ−c+(h¯k′​A−C)​Xk}​Δ​t\displaystyle R\_{0}+\sum\_{k=0}^{K-1}\Bigg\{-\frac{1}{2}\bar{h}\_{k}^{\prime}\Sigma\Sigma^{\prime}\bar{h}\_{k}-\frac{1}{2}\mathrm{tr}(\Psi\_{k}\Sigma\Sigma^{\prime})+\bar{h}\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c+(\bar{h}\_{k}^{\prime}A-C)X\_{k}\Bigg\}\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∑k=0K−1(h¯k′​Σ−Ξ′)​wk.\displaystyle+\sum\_{k=0}^{K-1}(\bar{h}\_{k}^{\prime}\Sigma-\Xi^{\prime})w\_{k}. |  | (3.2) |

###### Remark 3 (Interpretation of Exploration).

The additive term

|  |  |  |  |
| --- | --- | --- | --- |
|  | −12​tr​(Ψk​Σ​Σ′)\displaystyle-\frac{1}{2}\mathrm{tr}(\Psi\_{k}\Sigma\Sigma^{\prime}) |  | (3.3) |

lowers expected log-relative performance and can be interpreted as the instantaneous cost of exploration. The trace term tr​(Ψk​Σ​Σ′)\mathrm{tr}(\Psi\_{k}\Sigma\Sigma^{\prime}) shows that exploration is penalized more strongly when the exploratory covariance Ψk\Psi\_{k} allocates mass to directions with larger asset return volatility, as encoded by Σ​Σ′\Sigma\Sigma^{\prime}.

We define the risk-sensitive benchmarked criteria for the policy-averaged log excess return (R¯Tπ−R0)(\bar{R}^{\pi}\_{T}-R\_{0}) as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Jπ​(H,θ)\displaystyle J^{\pi}(H,\theta) | :=−1θ​ln⁡𝐄​[e−θ​(R¯Tπ−R0)]\displaystyle:=-\frac{1}{\theta}\ln\mathbf{E}\left[e^{-\theta(\bar{R}^{\pi}\_{T}-R\_{0})}\right] |  | (3.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Iπ​(H,θ)\displaystyle I^{\pi}(H,\theta) | :=e−θ​Jπ​(H,θ)=𝐄​[e−θ​(R¯Tπ−R0)].\displaystyle:=e^{-\theta J^{\pi}(H,\theta)}=\mathbf{E}\left[e^{-\theta(\bar{R}^{\pi}\_{T}-R\_{0})}\right]. |  | (3.5) |

From this point onward, we work with the policy-averaged criterion and write J​(H,θ)J(H,\theta) and I​(H,θ)I(H,\theta) for Jπ​(H,θ)J^{\pi}(H,\theta) and Iπ​(H,θ)I^{\pi}(H,\theta) when no confusion arises.

### 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem

We introduce on the measurable space
(Ω,ℱ,(ℱs)s∈[0,T])(\Omega,\mathcal{F},(\mathcal{F}\_{s})\_{s\in[0,T]})
a probability measure ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}},
distinct from ℙ\mathbb{P} and parameterised by two processes:

1. (i)

   *Duality–driven continuous-time shift:*
   a piecewise-constant, right-continuous process
   Γ¯=(γ¯s)s∈[0,T]∈ℝd\bar{\Gamma}=(\bar{\gamma}\_{s})\_{s\in[0,T]}\in\mathbb{R}^{d}
   such that γ¯s\bar{\gamma}\_{s} is constant on each interval
   [tk,tk+1)[t\_{k},t\_{k+1}), k=0,…,K−1k=0,\ldots,K-1.
2. (ii)

   *Exploration–driven discrete mean shift:* discrete-time process
   η¯=(η¯k)k=0,…,K−1∈ℝm\bar{\eta}=(\bar{\eta}\_{k})\_{k=0,\ldots,K-1}\in\mathbb{R}^{m}
   defined on the rebalancing dates.

###### Remark 4 (Piecewise-constant process γ¯\bar{\gamma}).

Since the state XX and control hh are updated only on the discrete rebalancing grid {tk}\{t\_{k}\} and the objective aggregates interval contributions, we restrict attention to piecewise-constant dual drifts γ¯\bar{\gamma}. This is the natural class for the discrete-time dynamic programming formulation developed below.

We first define admissible dual variables and the corresponding equivalent measures. The discrete exploratory noise vkv\_{k} is treated through a finite-dimensional Gaussian mean shift.
Because WW and vv are independent under ℙ\mathbb{P}, the Radon–Nikodym derivative factorises into the product of a continuous-time Girsanov term and a discrete-time exponential of a Gaussian term.

###### Definition 3.2 (Admissible duality strategies 𝒜Γ¯\mathcal{A}^{\bar{\Gamma}}).

A piecewise-constant, right-continuous process
Γ¯=(γ¯s)s∈[0,T]\bar{\Gamma}=(\bar{\gamma}\_{s})\_{s\in[0,T]} belongs to 𝒜Γ¯\mathcal{A}^{\bar{\Gamma}} if,
for each k=0,…,K−1k=0,\ldots,K-1, the value γ¯k:=γ¯tk\bar{\gamma}\_{k}:=\bar{\gamma}\_{t\_{k}} is
ℱtk\mathcal{F}\_{t\_{k}}-measurable, and it satisfies:

1. (i)

   *Piecewise-constant:*
   γ¯s\bar{\gamma}\_{s} is right-continuous and constant on each interval [tk,tk+1)[t\_{k},t\_{k+1}).
2. (ii)

   *Square-integrability:*

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[∥γ¯k∥2]<∞,k=0,…,K−1,\displaystyle\mathbb{E}\big[\lVert\bar{\gamma}\_{k}\rVert^{2}\big]<\infty,\qquad k=0,\ldots,K-1, |  |

   where γ¯k:=γ¯tk\bar{\gamma}\_{k}:=\bar{\gamma}\_{t\_{k}}.
3. (iii)

   *Exponential martingale property:*
   The process

   |  |  |  |
   | --- | --- | --- |
   |  | ℒTγ¯,W:=exp⁡(−12​∫0T∥γ¯s∥2​𝑑s+∫0Tγ¯s′​𝑑Ws)\displaystyle\mathcal{L}^{\bar{\gamma},W}\_{T}:=\exp\!\left(-\frac{1}{2}\int\_{0}^{T}\lVert\bar{\gamma}\_{s}\rVert^{2}ds+\int\_{0}^{T}\bar{\gamma}\_{s}^{\prime}\,dW\_{s}\right) |  |

   is a ℙ\mathbb{P}-exponential martingale.

###### Definition 3.3 (Admissible exploration shifts 𝒜η¯\mathcal{A}^{\bar{\eta}}).

A discrete-time process η¯=(η¯k)k=0,…,K−1∈ℝm\bar{\eta}=(\bar{\eta}\_{k})\_{k=0,\ldots,K-1}\in\mathbb{R}^{m}
belongs to 𝒜η¯\mathcal{A}^{\bar{\eta}} if:

1. (i)

   η¯k\bar{\eta}\_{k} is ℱtk\mathcal{F}\_{t\_{k}}-measurable for k=0,…,K−1k=0,\ldots,K-1.
2. (ii)

   *Square-integrability:*

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[∥η¯k∥2]<∞,k=0,…,K−1.\displaystyle\mathbb{E}\big[\lVert\bar{\eta}\_{k}\rVert^{2}\big]<\infty,\qquad k=0,\ldots,K-1. |  |

For Γ¯∈𝒜Γ¯\bar{\Gamma}\in\mathcal{A}^{\bar{\Gamma}}, the continuous-time change of measure is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙγ¯d​ℙ|ℱT=ℒTγ¯,W.\displaystyle\frac{d\mathbb{P}^{\bar{\gamma}}}{d\mathbb{P}}\Big|\_{\mathcal{F}\_{T}}=\mathcal{L}^{\bar{\gamma},W}\_{T}. |  | (3.6) |

Define the stochastic process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wsγ¯:=Ws−∫0sγ¯u​𝑑u,s∈[0,T].\displaystyle W^{\bar{\gamma}}\_{s}:=W\_{s}-\int\_{0}^{s}\bar{\gamma}\_{u}\,du,\qquad s\in[0,T]. |  | (3.7) |

Then Wγ¯W^{\bar{\gamma}} is a Brownian motion under ℙγ¯\mathbb{P}^{\bar{\gamma}}. Note that in ([3.7](#S3.E7 "In 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), γ¯\bar{\gamma} is piecewise constant, so the integral over [0,s][0,s] reduces to a sum of constant contribution over each interval [tk,tk+1),k=0,…,K−1[t\_{k},t\_{k+1}),k=0,\ldots,K-1.

For η¯∈𝒜η¯\bar{\eta}\in\mathcal{A}^{\bar{\eta}}, define the discrete-time Radon–Nikodym derivative

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​ℙη¯d​ℙ|ℱT\displaystyle\frac{d\mathbb{P}^{\bar{\eta}}}{d\mathbb{P}}\Big|\_{\mathcal{F}\_{T}} | :=∏k=0K−1exp{−12η¯k′Ψk−1η¯k+η¯k′Ψk−1vk}=:ℒη¯,v.\displaystyle:=\prod\_{k=0}^{K-1}\exp\left\{-\frac{1}{2}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}v\_{k}\right\}=:\mathcal{L}^{\bar{\eta},v}. |  | (3.8) |

Under ℙη¯\mathbb{P}^{\bar{\eta}} (and therefore under ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}, since the additional change of measure acts only on WW), conditionally on the filtration ℱtk\mathcal{F}\_{t\_{k}}, the random variable vkη¯v^{\bar{\eta}}\_{k} is Gaussian with mean η¯k\bar{\eta}\_{k} and covariance Ψk\Psi\_{k}, that is,
vkη¯∼𝒩​(η¯k,Ψk)v^{\bar{\eta}}\_{k}\sim\mathcal{N}(\bar{\eta}\_{k},\Psi\_{k}), and with vjη¯v^{\bar{\eta}}\_{j} independent of vkη¯v^{\bar{\eta}}\_{k} for j≠kj\neq k.

Since WW and vv are independent under ℙ\mathbb{P}, the joint Radon–Nikodym derivative is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙγ¯,η¯d​ℙ|ℱT=ℒTγ¯,Wℒη¯,v=:ℒTγ¯,η¯.\displaystyle\frac{d\mathbb{P}^{\bar{\gamma},\bar{\eta}}}{d\mathbb{P}}\Big|\_{\mathcal{F}\_{T}}=\mathcal{L}^{\bar{\gamma},W}\_{T}\,\mathcal{L}^{\bar{\eta},v}=:\mathcal{L}^{\bar{\gamma},\bar{\eta}}\_{T}. |  | (3.9) |

Definition [2.2](#S2.Thmtheorem2 "Definition 2.2 (Randomized Exploratory Control). ‣ 2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") establishes the randomized exploratory control (hs)s∈[0,T](h\_{s})\_{s\in[0,T]} as hk=h¯k+vkh\_{k}=\bar{h}\_{k}+v\_{k} under the measure ℙ\mathbb{P}. Following the change of measure to ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}, we now have hk=h¯k+vkη¯h\_{k}=\bar{h}\_{k}+v\_{k}^{\bar{\eta}}, which therefore depends on the process η¯\bar{\eta} via the noise term vkη¯∼𝒩​(η¯k,Ψk)v^{\bar{\eta}}\_{k}\sim\mathcal{N}\left(\bar{\eta}\_{k},\Psi\_{k}\right). Equivalently, the randomized control can be represented by the measure
π​(d​h;h¯k,η¯k)∼𝒩​(h¯k+η¯k,Ψk)\pi\left(dh;\bar{h}\_{k},\bar{\eta}\_{k}\right)\sim\mathcal{N}\left(\bar{h}\_{k}+\bar{\eta}\_{k},\Psi\_{k}\right).

Under ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}, the state dynamics at ([2.3](#S2.E3 "In 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk+1=b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t+Λ​wkγ¯,\displaystyle X\_{k+1}=b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t+\Lambda w^{\bar{\gamma}}\_{k}, |  | (3.10) |

for k=0,…,K−1k=0,\ldots,K-1, and where wkγ¯=Wk+1γ¯−Wkγ¯w^{\bar{\gamma}}\_{k}=W^{\bar{\gamma}}\_{k+1}-W^{\bar{\gamma}}\_{k}, using the shorthand notation Wkγ¯=Wtkγ¯W^{\bar{\gamma}}\_{k}=W^{\bar{\gamma}}\_{t\_{k}}.

###### Remark 5 (Scaling of exploratory shifts).

In this paper, we model the exploratory perturbations vkη¯v^{\bar{\eta}}\_{k} as instantaneous shocks with

|  |  |  |
| --- | --- | --- |
|  | vkη¯∼𝒩​(η¯k,Ψk),v^{\bar{\eta}}\_{k}\sim\mathcal{N}(\bar{\eta}\_{k},\Psi\_{k}), |  |

that occur before each rebalancing date and are independent of the rebalancing interval length Δ​t\Delta t. Equivalently, η¯k\bar{\eta}\_{k} and Ψk\Psi\_{k} represent the mean and covariance of the instantaneous exploratory shock applied at time tkt\_{k}.

We then compute the *relative entropy* under the product change of measure. We express the relative entropy of ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}} with respect to ℙ\mathbb{P} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(ℙγ¯,η¯∥ℙ)=𝐄γ¯,η¯​[ln⁡(d​ℙγ¯,η¯d​ℙ)]=𝐄γ¯,η¯​[ln⁡ℒTγ¯,W]+𝐄γ¯,η¯​[ln⁡ℒη¯,v].\displaystyle D\_{\rm KL}(\mathbb{P}^{\bar{\gamma},\bar{\eta}}\|\mathbb{P})=\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[\ln\left(\frac{d\mathbb{P}^{\bar{\gamma},\bar{\eta}}}{d\mathbb{P}}\right)\right]=\mathbf{E}^{\bar{\gamma},\bar{\eta}}[\ln\mathcal{L}^{\bar{\gamma},W}\_{T}]+\mathbf{E}^{\bar{\gamma},\bar{\eta}}[\ln\mathcal{L}^{\bar{\eta},v}]. |  | (3.11) |

Using Girsanov’s theorem, the continuous-time part reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄γ¯,η¯​[ln⁡ℒTγ¯,W]\displaystyle\mathbf{E}^{\bar{\gamma},\bar{\eta}}[\ln\mathcal{L}^{\bar{\gamma},W}\_{T}] | =𝐄γ¯,η¯​[−12​∫0T∥γ¯s∥2​𝑑s+∫0Tγ¯s′​𝑑Ws]\displaystyle=\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\frac{1}{2}\int\_{0}^{T}\lVert\bar{\gamma}\_{s}\rVert^{2}ds+\int\_{0}^{T}\bar{\gamma}\_{s}^{\prime}\,dW\_{s}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐄γ¯,η¯​[−12​∫0T∥γ¯s∥2​𝑑s+∫0Tγ¯s′​(d​Wsγ¯+γ¯s​d​s)]\displaystyle=\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\frac{1}{2}\int\_{0}^{T}\lVert\bar{\gamma}\_{s}\rVert^{2}ds+\int\_{0}^{T}\bar{\gamma}\_{s}^{\prime}\left(dW^{\bar{\gamma}}\_{s}+\bar{\gamma}\_{s}ds\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐄γ¯,η¯​[12​∫0T∥γ¯s∥2​𝑑s+∫0Tγ¯s′​𝑑Wsγ¯]\displaystyle=\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[\frac{1}{2}\int\_{0}^{T}\lVert\bar{\gamma}\_{s}\rVert^{2}ds+\int\_{0}^{T}\bar{\gamma}\_{s}^{\prime}\,dW^{\bar{\gamma}}\_{s}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​∑k=0K−1𝐄γ¯,η¯​[‖γ¯k‖2​Δ​t],\displaystyle=\frac{1}{2}\sum\_{k=0}^{K-1}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[\|\bar{\gamma}\_{k}\|^{2}\Delta t\right], |  | (3.12) |

where we used the fact that γ¯\bar{\gamma} is piecewise constant on [tk,tk+1),k=0,…,K−1[t\_{k},t\_{k+1}),k=0,\ldots,K-1, and that Wγ¯W^{\bar{\gamma}} is a ℙγ¯\mathbb{P}^{\bar{\gamma}}-martingale and therefore a ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}-martingale. Notice that since d​ℙγ¯,η¯d​ℙγ¯|ℱT=ℒTη¯,v\frac{d\mathbb{P}^{\bar{\gamma},\bar{\eta}}}{d\mathbb{P}^{\bar{\gamma}}}\big|\_{\mathcal{F}\_{T}}=\mathcal{L}^{\bar{\eta},v}\_{T} is independent of Wγ¯W^{\bar{\gamma}},
the change from ℙγ¯\mathbb{P}^{\bar{\gamma}} to ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}} does not affect the dynamics of Wγ¯W^{\bar{\gamma}}. Therefore Wγ¯W^{\bar{\gamma}}, which is already a ℙγ¯\mathbb{P}^{\bar{\gamma}}-martingale, is also a ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}-martingale.

For the discrete-time exploration part,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄γ¯,η¯​[ln⁡ℒη¯,v]\displaystyle\mathbf{E}^{\bar{\gamma},\bar{\eta}}[\ln\mathcal{L}^{\bar{\eta},v}] | =∑k=0K−1𝐄γ¯,η¯​[−12​η¯k′​Ψk−1​η¯k+η¯k′​Ψk−1​vk]\displaystyle=\sum\_{k=0}^{K-1}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\frac{1}{2}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}v\_{k}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​∑k=0K−1𝐄γ¯,η¯​[η¯k′​Ψk−1​η¯k],\displaystyle=\frac{1}{2}\sum\_{k=0}^{K-1}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right], |  | (3.13) |

where, since η¯k\bar{\eta}\_{k} is ℱtk\mathcal{F}\_{t\_{k}}-measurable and vkv\_{k} has conditional mean η¯k\bar{\eta}\_{k} under ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}, we have 𝐄γ¯,η¯​[η¯k′​Ψk−1​vk]=𝐄γ¯,η¯​[η¯k′​Ψk−1​η¯k]\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}v\_{k}\right]=\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right].

Hence, the total relative entropy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(ℙγ¯,η¯∥ℙ)=12​∑k=0K−1𝐄γ¯,η¯​[‖γ¯k‖2​Δ​t+η¯k′​Ψk−1​η¯k].\displaystyle D\_{\rm KL}(\mathbb{P}^{\bar{\gamma},\bar{\eta}}\|\mathbb{P})=\frac{1}{2}\sum\_{k=0}^{K-1}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Big[\,\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\Big]. |  | (3.14) |

###### Remark 6.

The role of γ¯\bar{\gamma} is to steer Brownian increments in the dual (adversarial) direction, whereas η¯\bar{\eta} biases the exploratory noise distribution. The resulting relative entropy penalty therefore decomposes into a continuous-time quadratic penalty and a discrete-time Mahalanobis penalty.

Next, we rewrite the policy-averaged log-relative return under the ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | R¯Tπ−R0=\displaystyle\bar{R}^{\pi}\_{T}-R\_{0}= | ∑k=0K−1{∫ℝm[(−12hk′ΣΣ′hk+hk′a+12Ξ′Ξ−c)+(hk′A−C)Xk]Δt\displaystyle\sum\_{k=0}^{K-1}\Bigg\{\int\_{\mathbb{R}^{m}}\left[\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right]\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(hk′Σ−Ξ′)(γ¯kΔt+wkγ¯)}π(dh;h¯k,η¯k)\displaystyle+\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)\left(\bar{\gamma}\_{k}\Delta t+w^{\bar{\gamma}}\_{k}\right)\Bigg\}\pi\left(dh;\bar{h}\_{k},\bar{\eta}\_{k}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑k=0K−1∫ℝm{(−12hk′ΣΣ′hk+hk′a+12Ξ′Ξ−c)+(hk′A−C)Xk\displaystyle\sum\_{k=0}^{K-1}\int\_{\mathbb{R}^{m}}\Bigg\{\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(hk′Σ−Ξ′)γ¯k}π(dh;h¯k,η¯k)Δt+∑k=0K−1∫ℝm{(hk′Σ−Ξ′)wkγ¯}π(dh;h¯k,η¯k)\displaystyle+\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}\Bigg\}\pi\left(dh;\bar{h}\_{k},\bar{\eta}\_{k}\right)\Delta t+\sum\_{k=0}^{K-1}\int\_{\mathbb{R}^{m}}\left\{\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)w^{\bar{\gamma}}\_{k}\right\}\pi\left(dh;\bar{h}\_{k},\bar{\eta}\_{k}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑k=0K−1{(−12(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)−12tr(ΨkΣΣ′)+(h¯k+η¯k)′a+12Ξ′Ξ−c)\displaystyle\sum\_{k=0}^{K-1}\Bigg\{\left(-\frac{1}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)-\frac{1}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)+\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +((h¯k+η¯k)′A−C)Xk+((h¯k+η¯k)′Σ−Ξ′)γ¯k}Δt+∑k=0K−1((h¯k+η¯k)′Σ−Ξ′)wγ¯k.\displaystyle+\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}+\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}\Bigg\}\Delta t+\sum\_{k=0}^{K-1}\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)w^{\bar{\gamma}}\_{k}. |  | (3.15) |

In the last equality, we used the Gaussian moments under
π​(d​h;h¯k,η¯k)∼𝒩​(h¯k+η¯k,Ψk)\pi(dh;\bar{h}\_{k},\bar{\eta}\_{k})\sim\mathcal{N}(\bar{h}\_{k}+\bar{\eta}\_{k},\Psi\_{k}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝmh​π​(d​h;h¯k,η¯k)=h¯k+η¯k,\displaystyle\int\_{\mathbb{R}^{m}}h\,\pi(dh;\bar{h}\_{k},\bar{\eta}\_{k})=\bar{h}\_{k}+\bar{\eta}\_{k}, |  | (3.16) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝmh′​Σ​Σ′​h​π​(d​h;h¯k,η¯k)=(h¯k+η¯k)′​Σ​Σ′​(h¯k+η¯k)+tr​(Ψk​Σ​Σ′).\displaystyle\int\_{\mathbb{R}^{m}}h^{\prime}\Sigma\Sigma^{\prime}h\,\pi(dh;\bar{h}\_{k},\bar{\eta}\_{k})=(\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma\Sigma^{\prime}(\bar{h}\_{k}+\bar{\eta}\_{k})+\text{tr}(\Psi\_{k}\Sigma\Sigma^{\prime}). |  | (3.17) |

Moreover, conditional on ℱtk\mathcal{F}\_{t\_{k}}, the Brownian increment wkγ¯w^{\bar{\gamma}}\_{k} is independent of the exploratory shock vkη¯v^{\bar{\eta}}\_{k}, or equivalently, of hkh\_{k} under the measure ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}. Hence wkγ¯w\_{k}^{\bar{\gamma}} can be treated as constant with respect to the integration in hh.

###### Remark 7 (Integrability).

Under the Gaussian state dynamics and the square-integrability conditions in Definitions
[3.1](#S3.Thmtheorem1 "Definition 3.1 (Class of admissible exploratory strategies 𝒜^𝐻ₑₓₚₗ). ‣ 3.1 Exploratory Controls and the Log-Relative Return Process ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), [3.2](#S3.Thmtheorem2 "Definition 3.2 (Admissible duality strategies 𝒜^Γ̄). ‣ 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), and [3.3](#S3.Thmtheorem3 "Definition 3.3 (Admissible exploration shifts 𝒜^𝜂̄). ‣ 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), all expectations appearing below are well-defined. In particular, the quadratic and linear terms entering the policy-averaged log-relative return and the entropy penalties are integrable on the finite horizon [0,T][0,T].

Finally, we apply free energy-entropy duality to represent the risk-sensitive control problem as a stochastic game. Applying the definition of free energy at ([2.12](#S2.E12 "In Definition 2.3 (Free Energy). ‣ 2.3 Free Energy, Relative Entropy, and the Energy-Entropy Duality ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) to ψ:=−θ​(R¯Tπ−R0)\psi:=-\theta(\bar{R}^{\pi}\_{T}-R\_{0}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰℙ​{−θ​(R¯Tπ−R0)}=ln⁡I​(H,θ),\displaystyle\mathcal{E}^{\mathbb{P}}\{-\theta(\bar{R}^{\pi}\_{T}-R\_{0})\}=\ln I(H,\theta), |  | (3.18) |

where II is the risk-sensitive criterion defined at ([3.5](#S3.E5 "In 3.1 Exploratory Controls and the Log-Relative Return Process ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")).

Recalling also the formula for the total entropy at ([3.14](#S3.E14 "In 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), the *free energy-entropy duality* from Proposition [2.5](#S2.Thmtheorem5 "Proposition 2.5 (Free Energy-Entropy Duality, (Dai Pra et al., 1996, Prop. 2.3(ii))). ‣ 2.3 Free Energy, Relative Entropy, and the Energy-Entropy Duality ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") then leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ln⁡I​(H,θ)\displaystyle\ln I(H,\theta) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | supγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[−θ​(R¯Tπ−R0)−12​∑k=0K−1(‖γ¯k‖2​Δ​t+η¯k′​Ψk−1​η¯k)]\displaystyle\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\theta(\bar{R}^{\pi}\_{T}-R\_{0})-\frac{1}{2}\sum\_{k=0}^{K-1}\left(\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right)\right] |  | (3.19) |

At this point, we make the following assumption:

###### Assumption 3.4.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | supℙγ,η𝐄γ¯,η¯​[−θ​(R¯Tπ−R0)−12​∑k=0K−1(‖γ¯k‖2​Δ​t+η¯k′​Ψk−1​η¯k)]\displaystyle\sup\_{\mathbb{P}^{\gamma,\eta}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\theta(\bar{R}^{\pi}\_{T}-R\_{0})-\frac{1}{2}\sum\_{k=0}^{K-1}\left(\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right)\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =supγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[−θ​(R¯Tπ−R0)−12​∑k=0K−1(‖γ¯k‖2​Δ​t+η¯k′​Ψk−1​η¯k)].\displaystyle=\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\theta(\bar{R}^{\pi}\_{T}-R\_{0})-\frac{1}{2}\sum\_{k=0}^{K-1}\left(\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right)\right]. |  | (3.20) |

Theorem [3.11](#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") below justifies this restriction by showing that the optimal controls are within the admissible classes 𝒜Γ¯\mathcal{A}^{\bar{\Gamma}} and 𝒜η¯\mathcal{A}^{\bar{\eta}}.

Under Assumption [3.4](#S3.Thmtheorem4 "Assumption 3.4. ‣ 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ln⁡I​(H,θ)\displaystyle\ln I(H,\theta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | supγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[−θ​(R¯Tπ−R0)−12​∑k=0K−1(‖γ¯k‖2​Δ​t+η¯k′​Ψk−1​η¯k)]\displaystyle\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\theta(\bar{R}^{\pi}\_{T}-R\_{0})-\frac{1}{2}\sum\_{k=0}^{K-1}\left(\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | supγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯[−θ∑k=0K−1{(−12(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)−12tr(ΨkΣΣ′)+(h¯k+η¯k)′a+12Ξ′Ξ−c)\displaystyle\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[-\theta\sum\_{k=0}^{K-1}\Bigg\{\left(-\frac{1}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)-\frac{1}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)+\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +((h¯k+η¯k)′A−C)Xk+((h¯k+η¯k)′Σ−Ξ′)γ¯k}Δt+∑k=0K−1((h¯k+η¯k)′Σ−Ξ′)wγ¯k\displaystyle+\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}+\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}\Bigg\}\Delta t+\sum\_{k=0}^{K-1}\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)w^{\bar{\gamma}}\_{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12∑k=0K−1(∥γ¯k∥2Δt+η¯k′Ψk−1η¯k)]\displaystyle-\frac{1}{2}\sum\_{k=0}^{K-1}\left(\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right)\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | supγ¯∈𝒜Γ¯,η¯∈𝒜η¯{𝐄γ¯,η¯[−θ∑k=0K−1{(−12(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)−12tr(ΨkΣΣ′)+(h¯k+η¯k)′a+12Ξ′Ξ−c)\displaystyle\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\left\{\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[-\theta\sum\_{k=0}^{K-1}\Bigg\{\left(-\frac{1}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)-\frac{1}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)+\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +((h¯k+η¯k)′A−C)Xk+((h¯k+η¯k)′Σ−Ξ′)γ¯k+12​θ∥γ¯k∥2+12​θ​Δ​tη¯k′Ψk−1η¯k}Δt]\displaystyle\left.+\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}+\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}+\frac{1}{2\theta}\|\bar{\gamma}\_{k}\|^{2}+\frac{1}{2\theta\Delta t}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\Bigg\}\Delta t\Bigg]\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ∑k=0K−1𝐄γ¯,η¯​[((h¯k+η¯k)′​Σ−Ξ′)​wkγ¯]⏟=0}\displaystyle\left.-\theta\sum\_{k=0}^{K-1}\underbrace{\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)w^{\bar{\gamma}}\_{k}\Bigg]}\_{=0}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | supγ¯∈𝒜Γ¯,η¯∈𝒜η¯θ∑k=0K−1𝐄γ¯,η¯[{(12(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)+12tr(ΨkΣΣ′)−(h¯k+η¯k)′a−12Ξ′Ξ+c)\displaystyle\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\theta\sum\_{k=0}^{K-1}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\Bigg\{\left(\frac{1}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)+\frac{1}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)-\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a-\frac{1}{2}\Xi^{\prime}\Xi+c\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −((h¯k+η¯k)′A−C)Xk−((h¯k+η¯k)′Σ−Ξ′)γ¯k−12​θ∥γ¯k∥2−12​θ​Δ​tη¯k′Ψk−1η¯k}Δt]\displaystyle-\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}-\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}-\frac{1}{2\theta}\|\bar{\gamma}\_{k}\|^{2}-\frac{1}{2\theta\Delta t}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\Bigg\}\Delta t\Bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | supγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[θ​∑k=0K−1g​(Xk,h¯k,η¯k,γ¯k)​Δ​t]\displaystyle\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t\Bigg] |  | (3.21) |

where we defined the function gg as

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | g​(Xk,h¯k,η¯k,γ¯k)\displaystyle g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (12​(h¯k+η¯k)′​Σ​Σ′​(h¯k+η¯k)+12​tr​(Ψk​Σ​Σ′)−(h¯k+η¯k)′​a−12​Ξ′​Ξ+c)\displaystyle\left(\frac{1}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)+\frac{1}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)-\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a-\frac{1}{2}\Xi^{\prime}\Xi+c\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −((h¯k+η¯k)′​A−C)​Xk−((h¯k+η¯k)′​Σ−Ξ′)​γ¯k−12​θ​‖γ¯k‖2−12​θ​Δ​t​η¯k′​Ψk−1​η¯k,\displaystyle-\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}-\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}-\frac{1}{2\theta}\|\bar{\gamma}\_{k}\|^{2}-\frac{1}{2\theta\Delta t}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}, |  | (3.22) |

and where we used the fact that since h¯k\bar{h}\_{k},η¯k\bar{\eta}\_{k},γ¯k\bar{\gamma}\_{k} and XkX\_{k} are all ℱtk\mathcal{F}\_{t\_{k}}-measurable, and
wkγ¯w\_{k}^{\bar{\gamma}} is a Brownian increment independent of ℱtk\mathcal{F}\_{t\_{k}} under
ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}, we have
𝐄γ¯,η¯​[((h¯k+η¯k)′​Σ−Ξ′)​wkγ¯]=0\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)w\_{k}^{\bar{\gamma}}\right]=0.

We can thus interpret the energy-entropy duality’s infsup\inf\sup as a two-player game against Nature. The agent applies control h¯\bar{h} to minimize the expectation while Nature (via the duality) applies control ν¯:=(γ¯′η¯′)′\bar{\nu}:=\begin{pmatrix}\bar{\gamma}^{\prime}&\bar{\eta}^{\prime}\end{pmatrix}^{\prime} to maximize it. The control γ¯\bar{\gamma} steers market noise while the control η¯\bar{\eta} biases exploration.

We denote by

|  |  |  |
| --- | --- | --- |
|  | 𝒜¯explH:={h¯=(h¯k)k=0,…,K−1:∃H=(hs)s∈[0,T]∈𝒜explH​ such that ​hk=h¯k+vk,k=0,…,K−1}\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}:=\left\{\bar{h}=(\bar{h}\_{k})\_{k=0,\ldots,K-1}\;:\;\exists\,H=(h\_{s})\_{s\in[0,T]}\in\mathcal{A}^{H}\_{\mathrm{expl}}\text{ such that }h\_{k}=\bar{h}\_{k}+v\_{k},\;k=0,\ldots,K-1\right\} |  |

the set of baseline controls induced by admissible exploratory strategies. Taking the infimum over h¯\bar{h} to minimize the logarithm of the criterion II, and with a slight abuse of notation write I​(h¯,θ)I(\bar{h},\theta) for I​(H,θ)I(H,\theta) when HH is any admissible exploratory strategy inducing h¯\bar{h},
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | infh¯∈𝒜¯explHln⁡I​(h¯,θ)=infh¯∈𝒜¯explHsupγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[θ​∑k=0K−1g​(Xk,h¯k,η¯k,γ¯k)​Δ​t]\displaystyle\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\ln I(\bar{h},\theta)=\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | ln​infh¯∈𝒜¯explHI​(h¯,θ)=infh¯∈𝒜¯explHsupγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[θ​∑k=0K−1g​(Xk,h¯k,η¯k,γ¯k)​Δ​t]\displaystyle\ln\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}I(\bar{h},\theta)=\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t\Bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | infh¯∈𝒜¯explHI​(h¯,θ)=exp⁡{infh¯∈𝒜¯explHsupγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[θ​∑k=0K−1g​(Xk,h¯k,η¯k,γ¯k)​Δ​t]},\displaystyle\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}I(\bar{h},\theta)=\exp\left\{\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t\Bigg]\right\}, |  | (3.23) |

and where the first equivalence follows from Lemma 5.3.1 in Meneghini ([1994](#bib.bib18)).

Focusing on the term inside the exponential on the right-hand side of ([3.2](#S3.Ex33 "3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we consider the game with optimal value

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(T;θ):=infh¯∈𝒜¯explHsupγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[θ​∑k=0K−1g​(Xk,h¯k,η¯k,γ¯k)​Δ​t]\displaystyle u(T;\theta):=\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t\Bigg] |  | (3.24) |

so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | infh¯∈𝒜¯explHI​(h¯,θ)=exp⁡{u​(T;θ)}\displaystyle\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}I(\bar{h},\theta)=\exp\left\{u(T;\theta)\right\} |  | (3.25) |

### 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game

We now solve the stochastic game with optimal value u​(T;θ)u(T;\theta) as in ([3.24](#S3.E24 "In 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")). Let uk​(Xk)u\_{k}(X\_{k}) be the optimal value of the game at the generic time tk,k=0,…,K−1t\_{k},\quad k=0,\ldots,K-1 when the state takes the value XkX\_{k}, and denote u0​(X0):=u​(T;θ)u\_{0}(X\_{0}):=u(T;\theta). We apply the Dynamic Programming Principle (DPP) to express the value of the game recursively as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uK​(XK)=\displaystyle u\_{K}(X\_{K})= | 0\displaystyle 0 |  | (3.26) |

and, for k=K−1,…,0k=K-1,\ldots,0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | uk​(Xk)=\displaystyle u\_{k}(X\_{k})= | infh¯ksupγ¯k,η¯k𝐄k,Xkγ¯,η¯​[θ​g​(Xk,h¯k,η¯k,γ¯k)​Δ​t+uk+1​(Xk+1)]\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[\theta g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t+u\_{k+1}(X\_{k+1})\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | infh¯ksupγ¯k,η¯k{θ​g​(Xk,h¯k,η¯k,γ¯k)​Δ​t+𝐄k,Xkγ¯,η¯​[uk+1​(Xk+1)]},\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\left\{\theta g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t+\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[u\_{k+1}(X\_{k+1})\right]\right\}, |  | (3.27) |

where 𝐄k,Xkγ¯,η¯\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}} denotes the expectation with respect to the measure ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}, conditional on time tkt\_{k}, state process value XkX\_{k}, and with admissible controls at time tkt\_{k}. The function gg is defined at ([3.2](#S3.Ex30 "3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")).

In what follows, we shall show that uk​(Xk)u\_{k}(X\_{k}) has a quadratic expression in XkX\_{k} of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | uk​(Xk)=12​Xk′​Pk​Xk+Xk′​pk+rk,u\_{k}(X\_{k})=\frac{1}{2}X\_{k}^{\prime}P\_{k}X\_{k}+X\_{k}^{\prime}p\_{k}+r\_{k}, |  | (3.28) |

and at the same time, we shall derive the expressions for a stationary point (h¯k∗,γ¯k∗,η¯k∗)(\bar{h}\_{k}^{\*},\bar{\gamma}\_{k}^{\*},\bar{\eta}\_{k}^{\*}) as a candidate saddle point.

On the basis of ([3.3](#S3.Ex35 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we define the Hamiltonian ℋ\mathcal{H}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℋ​(Xk,h¯k,γ¯k,η¯k):=\displaystyle\mathcal{H}(X\_{k},\bar{h}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k}):= | θ​g​(Xk,h¯k,η¯k,γ¯k)​Δ​t+𝐄k,Xkγ¯,η¯​[uk+1​(Xk+1)].\displaystyle\theta g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t+\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[u\_{k+1}(X\_{k+1})\right]. |  | (3.29) |

Our main result, Theorem [3.11](#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), is preceded by a lemma of independent interest and four propositions.

First we have

###### Lemma 3.5.

Assuming that, at the generic time tk+1t\_{k+1}, the optimal value uk+1​(Xk+1)u\_{k+1}(X\_{k+1}) has a quadratic expression as in ([3.28](#S3.E28 "In 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), for a control triple (h¯,γ¯,η¯)(\bar{h},\bar{\gamma},\bar{\eta}) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝐄k,Xkγ¯,η¯​[uk+1​(Xk+1)]\displaystyle\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[u\_{k+1}(X\_{k+1})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 12​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​Pk+1​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)\displaystyle\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12​tr​(Λ′​Pk+1​Λ)​Δ​t+(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​pk+1+rk+1\displaystyle+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t+\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}p\_{k+1}+r\_{k+1} |  | (3.30) |

###### Proof.

We use the state dynamics at ([3.10](#S3.E10 "In 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) to obtain an analytic expression for 𝐄k,Xkγ¯,η¯​[uk+1​(Xk+1)]\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[u\_{k+1}(X\_{k+1})\right] in terms of XkX\_{k}. Recalling that under ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}, wkγ¯=Wk+1γ¯−Wkγ¯w^{\bar{\gamma}}\_{k}=W^{\bar{\gamma}}\_{k+1}-W^{\bar{\gamma}}\_{k}, we have 𝐄k,Xkγ¯,η¯​[wkγ¯]=0\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[w^{\bar{\gamma}}\_{k}\right]=0 and 𝐄k,Xkγ¯,η¯​[wkγ¯​(wkγ¯)′]=Δ​t​Id\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[w^{\bar{\gamma}}\_{k}(w^{\bar{\gamma}}\_{k})^{\prime}\right]=\Delta t\ I\_{d}, so

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝐄k,Xkγ¯,η¯​[uk+1​(Xk+1)]\displaystyle\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[u\_{k+1}(X\_{k+1})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝐄k,Xkγ¯,η¯​[12​Xk+1′​Pk+1​Xk+1+Xk+1′​pk+1+rk+1]\displaystyle\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[\frac{1}{2}X\_{k+1}^{\prime}P\_{k+1}X\_{k+1}+X\_{k+1}^{\prime}p\_{k+1}+r\_{k+1}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝐄k,Xkγ¯,η¯[12(bΔt+B~Xk+Λγ¯kΔt+Λwkγ¯)′Pk+1(bΔt+B~Xk+Λγ¯kΔt+Λwkγ¯)\displaystyle\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t+\Lambda w^{\bar{\gamma}}\_{k}\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t+\Lambda w^{\bar{\gamma}}\_{k}\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(bΔt+B~Xk+Λγ¯kΔt+Λwkγ¯)′pk+1+rk+1]\displaystyle\left.+\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t+\Lambda w^{\bar{\gamma}}\_{k}\right)^{\prime}p\_{k+1}+r\_{k+1}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 12​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​Pk+1​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)\displaystyle\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​Pk+1​Λ​𝐄k,Xkγ¯,η¯​[wkγ¯]⏟=0+12​𝐄k,Xkγ¯,η¯​[(wkγ¯)′​Λ′​Pk+1​Λ​wkγ¯]⏟=tr​(Λ′​Pk+1​Λ)​Δ​t\displaystyle\underbrace{+\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}P\_{k+1}\Lambda\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[w^{\bar{\gamma}}\_{k}\right]}\_{=0}+\frac{1}{2}\underbrace{\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[(w^{\bar{\gamma}}\_{k})^{\prime}\Lambda^{\prime}P\_{k+1}\Lambda w^{\bar{\gamma}}\_{k}\right]}\_{=\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​pk+1+𝐄k,Xkγ¯,η¯​[(wkγ¯)′]​Λ′​pk+1⏟=0+rk+1\displaystyle+\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}p\_{k+1}+\underbrace{\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[\left(w^{\bar{\gamma}}\_{k}\right)^{\prime}\right]\Lambda^{\prime}p\_{k+1}}\_{=0}+r\_{k+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 12​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​Pk+1​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)\displaystyle\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12​tr​(Λ′​Pk+1​Λ)​Δ​t+(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​pk+1+rk+1,\displaystyle+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t+\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}p\_{k+1}+r\_{k+1}, |  | (3.31) |

assuming without loss of generality that Pk+1P\_{k+1} is symmetric555Since x′​Pk+1​x=12​x′​(Pk+1+Pk+1′)​xx^{\prime}P\_{k+1}x=\frac{1}{2}x^{\prime}(P\_{k+1}+P\_{k+1}^{\prime})x, we may replace Pk+1P\_{k+1} by its symmetric part without changing the quadratic form. This concludes the proof.
∎

Next, we derive the saddle point for the game and derive two equivalent representations of the optimal controls. The first representation, in Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), yields optimality conditions that are easy to check. These conditions are presented in Assumption [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). The second representation, in Proposition [3.9](#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), produces an optimal asset allocation that is more easily interpretable. We discuss the optimality conditions in Subsection [4.1](#S4.SS1 "4.1 Interpreting Assumptions 2.1 and 3.6 ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and interpretability from the perspective of Fractional Kelly Strategies in Subsection [4.3](#S4.SS3 "4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning").

For notational convenience, we let

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜k+1:=Λ′​Pk+1​Λ​Δ​t−Id,\displaystyle\mathcal{A}\_{k+1}:=\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}, |  | (3.32) |

for k=0,…,K−1k=0,\ldots,K-1.

###### Assumption 3.6.

For k=0,…,K−1k=0,\ldots,K-1, assume

|  |  |  |  |
| --- | --- | --- | --- |
|  | −(𝒜k+100θ​Σ​Σ′​Δ​t−Ψk−1)>0\displaystyle-\begin{pmatrix}\mathcal{A}\_{k+1}&0\\ 0&\theta\Sigma\Sigma^{\prime}\Delta t-\Psi\_{k}^{-1}\end{pmatrix}>0 |  | (3.33) |

Assumption [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), together with Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), provides sufficient conditions for the existence of a saddle point. We defer the interpretation of this condition until Section [4](#S4 "4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning").

For a generic control triple (h¯,γ¯,η¯)(\bar{h},\bar{\gamma},\bar{\eta}) and for given kk, XX, and a set of model parameters, in what follows, we shall also consider the auxiliary function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fk​(h¯,γ¯,η¯;X):=\displaystyle F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X):= | θ2​(h¯+η¯)′​Σ​Σ′​(h¯+η¯)​Δ​t−θ​(h¯+η¯)′​(a+A​X)​Δ​t−θ​((h¯+η¯)′​Σ−Ξ′)​γ¯​Δ​t\displaystyle\frac{\theta}{2}\left(\bar{h}+\bar{\eta}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}+\bar{\eta}\right)\Delta t-\theta\left(\bar{h}+\bar{\eta}\right)^{\prime}(a+AX)\Delta t-\theta\left((\bar{h}+\bar{\eta})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12​γ¯′​𝒜k+1​γ¯​Δ​t+γ¯′​Λ′​[Pk+1​(b​Δ​t+B~​X)+pk+1]​Δ​t−12​η¯′​Ψk−1​η¯\displaystyle+\frac{1}{2}\bar{\gamma}^{\prime}\mathcal{A}\_{k+1}\bar{\gamma}\Delta t+\bar{\gamma}^{\prime}\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\right)+p\_{k+1}\right]\Delta t-\frac{1}{2}\bar{\eta}^{\prime}\Psi\_{k}^{-1}\bar{\eta} |  | (3.34) |

Under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), the search for a saddle point for uk​(Xk)u\_{k}(X\_{k}) reduces to the search for a saddle point for Fk​(h¯,γ¯,η¯;Xk)F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k}), as shown in the next proposition.

###### Proposition 3.7 (Saddle Point Representation).

If Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") hold, then:

1. (i)

   The optimal value function uk​(Xk),k=0,⋯,K−1u\_{k}(X\_{k}),k=0,\cdots,K-1 at ([3.3](#S3.Ex35 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) has the following saddle point representation:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | uk​(Xk)=\displaystyle u\_{k}(X\_{k})= | infh¯ksupγ¯k,η¯k{Fk​(h¯,γ¯,η¯;Xk)}+12​(b​Δ​t+B~​Xk)′​Pk+1​(b​Δ​t+B~​Xk)+(b​Δ​t+B~​Xk)′​pk+1\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\left\{F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\right\}+\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}p\_{k+1} |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  |  | +θ​(c+C​Xk)​Δ​t+θ2​tr​(Ψk​Σ​Σ′)​Δ​t−θ2​Ξ′​Ξ​Δ​t+12​tr​(Λ′​Pk+1​Λ)​Δ​t+rk+1\displaystyle+\theta(c+CX\_{k})\Delta t+\frac{\theta}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)\Delta t-\frac{\theta}{2}\Xi^{\prime}\Xi\Delta t+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t+r\_{k+1} |  | (3.35) |

   where Pk+1,pk+1,rk+1P\_{k+1},p\_{k+1},r\_{k+1} are the coefficients of the quadratic form given at ([3.28](#S3.E28 "In 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")).
2. (ii)

   The minimax condition for the Hamiltonian defined at ([3.29](#S3.E29 "In 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) holds:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | infh¯ksupγ¯k,η¯kℋ​(Xk,h¯k,γ¯k,η¯k)=supγ¯k,η¯kinfh¯kℋ​(Xk,h¯k,γ¯k,η¯k)\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\mathcal{H}(X\_{k},\bar{h}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k})=\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\inf\_{\bar{h}\_{k}}\mathcal{H}(X\_{k},\bar{h}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k}) |  | (3.36) |
3. (iii)

   We have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Fk​(hk∗,γ¯k,η¯k;Xk)≤Fk​(hk∗,γk∗,ηk∗;Xk)≤Fk​(h¯k,γk∗,ηk∗;Xk).\displaystyle F\_{k}(h^{\*}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k};X\_{k})\leq F\_{k}(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k};X\_{k})\leq F\_{k}(\bar{h}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k};X\_{k}). |  | (3.37) |

###### Proof.

1. (i)

   Substituting ([3.2](#S3.Ex30 "3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and ([3.5](#S3.Ex36 "Lemma 3.5. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) into the dynamic programming equation at ([3.3](#S3.Ex35 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we obtain

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | uk​(Xk)=\displaystyle u\_{k}(X\_{k})= | infh¯ksupγ¯k,η¯k{θ​g​(Xk,h¯k,η¯k,γ¯k)​Δ​t+𝐄k,Xkγ¯,η¯​[uk+1​(Xk+1)]}\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\left\{\theta g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t+\mathbf{E}\_{k,X\_{k}}^{\bar{\gamma},\bar{\eta}}\left[u\_{k+1}(X\_{k+1})\right]\right\} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | =\displaystyle= | infh¯ksupγ¯k,η¯k{θ2(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)Δt+θ2tr(ΨkΣΣ′)Δt−θ(h¯k+η¯k)′aΔt−θ2Ξ′ΞΔt\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\Bigg\{\frac{\theta}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)\Delta t+\frac{\theta}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)\Delta t-\theta\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a\Delta t-\frac{\theta}{2}\Xi^{\prime}\Xi\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +θ​c​Δ​t−θ​((h¯k+η¯k)′​A−C)​Xk​Δ​t−θ​((h¯k+η¯k)′​Σ−Ξ′)​γ¯k​Δ​t−12​‖γ¯k‖2​Δ​t−12​η¯k′​Ψk−1​η¯k\displaystyle+\theta c\Delta t-\theta\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}\Delta t-\theta\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}\Delta t-\frac{1}{2}\|\bar{\gamma}\_{k}\|^{2}\Delta t-\frac{1}{2}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +12​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)′​Pk+1​(b​Δ​t+B~​Xk+Λ​γ¯k​Δ​t)\displaystyle+\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +12tr(Λ′Pk+1Λ)Δt+(bΔt+B~Xk+Λγ¯kΔt)′pk+1+rk+1}\displaystyle+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t+\left(b\Delta t+\tilde{B}X\_{k}+\Lambda\bar{\gamma}\_{k}\Delta t\right)^{\prime}p\_{k+1}+r\_{k+1}\Bigg\} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | =\displaystyle= | infh¯ksupγ¯k,η¯k{θ2(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)Δt+θ2tr(ΨkΣΣ′)Δt−θ(h¯k+η¯k)′aΔt\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\Bigg\{\frac{\theta}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)\Delta t+\frac{\theta}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)\Delta t-\theta\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}a\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −θ2​Ξ′​Ξ​Δ​t+θ​c​Δ​t−θ​((h¯k+η¯k)′​A−C)​Xk​Δ​t−θ​((h¯k+η¯k)′​Σ−Ξ′)​γ¯k​Δ​t\displaystyle-\frac{\theta}{2}\Xi^{\prime}\Xi\Delta t+\theta c\Delta t-\theta\left(\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}A-C\right)X\_{k}\Delta t-\theta\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −12​γ¯k′​γ¯k​Δ​t−12​η¯k′​Ψk−1​η¯k+12​γ¯k′​Λ′​Pk+1​Λ​γ¯k​(Δ​t)2+γ¯k′​Λ′​Pk+1​(b​Δ​t+B~​Xk)​Δ​t\displaystyle-\frac{1}{2}\bar{\gamma}\_{k}^{\prime}\bar{\gamma}\_{k}\Delta t-\frac{1}{2}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}+\frac{1}{2}\bar{\gamma}\_{k}^{\prime}\Lambda^{\prime}P\_{k+1}\Lambda\bar{\gamma}\_{k}(\Delta t)^{2}+\bar{\gamma}\_{k}^{\prime}\Lambda^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +12​(b​Δ​t+B~​Xk)′​Pk+1​(b​Δ​t+B~​Xk)+12​tr​(Λ′​Pk+1​Λ)​Δ​t+γ¯k′​Λ′​pk+1​Δ​t\displaystyle+\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t+\bar{\gamma}\_{k}^{\prime}\Lambda^{\prime}p\_{k+1}\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +(bΔt+B~Xk)′pk+1+rk+1}\displaystyle+\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}p\_{k+1}+r\_{k+1}\Bigg\} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | =\displaystyle= | infh¯ksupγ¯k,η¯k{θ2(h¯k+η¯k)′ΣΣ′(h¯k+η¯k)Δt−θ(h¯k+η¯k)′(a+AXk)Δt\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\Bigg\{\frac{\theta}{2}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}\Sigma\Sigma^{\prime}\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)\Delta t-\theta\left(\bar{h}\_{k}+\bar{\eta}\_{k}\right)^{\prime}(a+AX\_{k})\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −θ​((h¯k+η¯k)′​Σ−Ξ′)​γ¯k​Δ​t+12​γ¯k′​𝒜k+1​γ¯k​Δ​t+γ¯k′​Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]​Δ​t\displaystyle-\theta\left((\bar{h}\_{k}+\bar{\eta}\_{k})^{\prime}\Sigma-\Xi^{\prime}\right)\bar{\gamma}\_{k}\Delta t+\frac{1}{2}\bar{\gamma}\_{k}^{\prime}\mathcal{A}\_{k+1}\bar{\gamma}\_{k}\Delta t+\bar{\gamma}\_{k}^{\prime}\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −12η¯k′Ψk−1η¯k}+12(bΔt+B~Xk)′Pk+1(bΔt+B~Xk)+(bΔt+B~Xk)′pk+1\displaystyle-\frac{1}{2}\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\Bigg\}+\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}p\_{k+1} |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  |  | +θ​(c+C​Xk)​Δ​t+θ2​tr​(Ψk​Σ​Σ′)​Δ​t−θ2​Ξ′​Ξ​Δ​t+12​tr​(Λ′​Pk+1​Λ)​Δ​t+rk+1\displaystyle+\theta(c+CX\_{k})\Delta t+\frac{\theta}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)\Delta t-\frac{\theta}{2}\Xi^{\prime}\Xi\Delta t+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t+r\_{k+1} |  | (3.38) |

   from which, using the definition of FkF\_{k} in ([3.3](#S3.Ex46 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we obtain the desired representation of uk​(Xk)u\_{k}(X\_{k}), which proves the first part of the proposition.
2. (ii)

   The function FkF\_{k} at ([3.3](#S3.Ex46 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) is quadratic in the controls h¯\bar{h}, γ¯\bar{\gamma}, and η¯\bar{\eta}. Under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), FkF\_{k} is convex in h¯\bar{h} and concave in γ¯\bar{\gamma} and η¯\bar{\eta}. Moreover, the Hessian is independent of the value of the controls. So FkF\_{k} admits a unique stationary point (h∗,γ∗,η∗)(h^{\*},\gamma^{\*},\eta^{\*}), which is affine in the state XkX\_{k}. Since FkF\_{k} is jointly continuous, convex in h¯\bar{h}, concave in (γ¯,η¯)(\bar{\gamma},\bar{\eta}), and admits a unique stationary point, that stationary point is the unique saddle point of FkF\_{k}. Therefore the minimax equality holds for the Hamiltonian inside ([i](#S3.Ex48 "item i ‣ Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), that is,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | infh¯ksupγ¯k,η¯kℋ​(Xk,h¯k,γ¯k,η¯k)=supγ¯k,η¯kinfh¯kℋ​(Xk,h¯k,γ¯k,η¯k).\displaystyle\inf\_{\bar{h}\_{k}}\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\mathcal{H}(X\_{k},\bar{h}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k})=\sup\_{\bar{\gamma}\_{k},\bar{\eta}\_{k}}\inf\_{\bar{h}\_{k}}\mathcal{H}(X\_{k},\bar{h}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k}). |  | (3.39) |
3. (iii)

   It follows from ([3.36](#S3.E36 "In item ii ‣ Proposition 3.7 (Saddle Point Representation). ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) that we can apply the saddle point condition

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ℋ​(Xk,hk∗,γ¯k,η¯k)≤ℋ​(Xk,hk∗,γk∗,ηk∗)≤ℋ​(Xk,h¯k,γk∗,ηk∗)\displaystyle\mathcal{H}(X\_{k},h^{\*}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k})\leq\mathcal{H}(X\_{k},h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k})\leq\mathcal{H}(X\_{k},\bar{h}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k}) |  | (3.40) |

   to solve the game. Applying ([i](#S3.Ex47 "item i ‣ Proposition 3.7 (Saddle Point Representation). ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) together with the definition of FkF\_{k} at ([3.3](#S3.Ex46 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and the definition of supremum/infimum, the saddle point condition ([3.40](#S3.E40 "In item iii ‣ Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) simplifies to

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Fk​(hk∗,γ¯k,η¯k;Xk)≤Fk​(hk∗,γk∗,ηk∗;Xk)≤Fk​(h¯k,γk∗,ηk∗;Xk).\displaystyle F\_{k}(h^{\*}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k};X\_{k})\leq F\_{k}(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k};X\_{k})\leq F\_{k}(\bar{h}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k};X\_{k}). |  | (3.41) |

   Hence, the search for a saddle point for uk​(Xk)u\_{k}(X\_{k}) reduces to the search for a saddle point for Fk​(h¯,γ¯,η¯;Xk)F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k}).

∎

###### Remark 8.

Because FkF\_{k} is quadratic with constant Hessian and is convex-concave under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), the stationary point can be computed by solving the first-order conditions in any order of the variables.

###### Proposition 3.8.

Under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), the candidate optimal controls are given by the stationary point (hk∗,γk∗,ηk∗),k=0,…​K−1(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k}),k=0,\ldots K-1 of the quadratic function
Fk​(h¯,γ¯,η¯;Xk)F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k}) at ([3.3](#S3.Ex46 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and can be explicitly expressed as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hk∗=\displaystyle h^{\*}\_{k}= | (Σ​Σ′)−1​{{Im−θ​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1}​(a+A​Xk)+Σ​ℬk+1−1​{Λ′​Pk+1​(b​Δ​t+B~​Xk)+Λ′​pk+1+θ​Ξ}}\displaystyle\left(\Sigma\Sigma^{\prime}\right)^{-1}\Bigg\{\left\{I\_{m}-\theta\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\right\}(a+AX\_{k})+\Sigma\mathcal{B}\_{k+1}^{-1}\left\{\Lambda^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\}\Bigg\} |  | (3.42) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γk∗=\displaystyle\gamma^{\*}\_{k}= | ℬk+1−1​{−θ​Σ′​(Σ​Σ′)−1​(a+A​Xk)+Λ′​Pk+1​(b​Δ​t+B~​Xk)+Λ′​pk+1+θ​Ξ}\displaystyle\mathcal{B}\_{k+1}^{-1}\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k})+\Lambda^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\} |  | (3.43) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ηk∗=\displaystyle\eta^{\*}\_{k}= | 0.\displaystyle 0. |  | (3.44) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬk+1:=θ​Σ′​(Σ​Σ′)−1​Σ−𝒜k+1,\displaystyle\mathcal{B}\_{k+1}:=\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma-\mathcal{A}\_{k+1}, |  | (3.45) |

for k=0,…,K−1k=0,\ldots,K-1.

###### Proof.

According to the proof of the previous Proposition, it suffices to look for a saddle point for Fk​(h¯,γ¯,η¯;Xk)F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k}). By the first order condition, h∗h^{\*} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Fk∂h¯​(h¯,γ¯,η¯;Xk)|h¯=h∗,γ¯=γ∗,η¯=η∗=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{h}}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=\eta^{\*}}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | θ​Σ​Σ′​(h∗+η∗)​Δ​t−θ​(a+A​Xk)​Δ​t−θ​Σ​γ∗​Δ​t=0\displaystyle\theta\Sigma\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)\Delta t-\theta(a+AX\_{k})\Delta t-\theta\Sigma\gamma^{\*}\Delta t=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | (h∗+η∗)=(Σ​Σ′)−1​[(a+A​Xk)+Σ​γ∗],\displaystyle\left(h^{\*}+\eta^{\*}\right)=\left(\Sigma\Sigma^{\prime}\right)^{-1}\left[(a+AX\_{k})+\Sigma\gamma^{\*}\right], |  | (3.46) |

Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") ensures that FkF\_{k} reaches a minimum in its argument h¯\bar{h} at h∗h^{\*}.

Next, we apply the first order condition to η¯\bar{\eta}:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Fk∂η¯​(h¯,γ¯,η¯;Xk)|h¯=h∗,γ¯=γ∗,η¯=η∗=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{\eta}}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=\eta^{\*}}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | θ​Σ​Σ′​(h∗+η∗)​Δ​t−θ​(a+A​Xk)​Δ​t−θ​Σ​γ∗​Δ​t−Ψk−1​η∗=0\displaystyle\theta\Sigma\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)\Delta t-\theta(a+AX\_{k})\Delta t-\theta\Sigma\gamma^{\*}\Delta t-\Psi\_{k}^{-1}\eta^{\*}=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | Ψk−1​η∗=θ​Σ​Σ′​(h∗+η∗)​Δ​t−θ​(a+A​Xk)​Δ​t−θ​Σ​γ∗​Δ​t⏟=0​ by ([3.3](#S3.Ex61 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))=0\displaystyle\Psi\_{k}^{-1}\eta^{\*}=\underbrace{\theta\Sigma\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)\Delta t-\theta(a+AX\_{k})\Delta t-\theta\Sigma\gamma^{\*}\Delta t}\_{=0\text{ by }\eqref{eq:hstar:1}}=0 |  | (3.47) |

Hence, the candidate exploratory bias η∗=0\eta^{\*}=0. By Assumption [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), FkF\_{k} reaches a maximum in its argument η¯\bar{\eta} at η∗=0\eta^{\*}=0.

Finally,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Fk∂γ¯​(h¯,γ¯,η¯;Xk)|h¯=h∗,γ¯=γ∗,η¯=η∗=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{\gamma}}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=\eta^{\*}}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | −θ​(Σ′​(h∗+η∗)−Ξ)​Δ​t+𝒜k+1​γ∗​Δ​t+Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]​Δ​t=0\displaystyle-\theta\left(\Sigma^{\prime}(h^{\*}+\eta^{\*})-\Xi\right)\Delta t+\mathcal{A}\_{k+1}\gamma^{\*}\Delta t+\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\Delta t=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | 𝒜k+1​γ∗−θ​Σ′​(h∗+η∗)+θ​Ξ+Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]=0\displaystyle\mathcal{A}\_{k+1}\gamma^{\*}-\theta\Sigma^{\prime}(h^{\*}+\eta^{\*})+\theta\Xi+\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]=0 |  | (3.48) |

By Assumption [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), FkF\_{k} reaches a maximum in its argument γ¯\bar{\gamma} at γ∗\gamma^{\*}.

From ([3.3](#S3.Ex61 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​Σ′​(h∗+η∗)=θ​Σ′​(Σ​Σ′)−1​[(a+A​Xk)+Σ​γ∗],\displaystyle\theta\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)=\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left[(a+AX\_{k})+\Sigma\gamma^{\*}\right], |  | (3.49) |

thus ([3.3](#S3.Ex65 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝒜k+1​γ∗−θ​Σ′​(Σ​Σ′)−1​[(a+A​Xk)+Σ​γ∗]+θ​Ξ+Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]=0\displaystyle\mathcal{A}\_{k+1}\gamma^{\*}-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left[(a+AX\_{k})+\Sigma\gamma^{\*}\right]+\theta\Xi+\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | [Λ′​Pk+1​Λ​Δ​t−Id−θ​Σ′​(Σ​Σ′)−1​Σ]​γ∗−θ​Σ′​(Σ​Σ′)−1​(a+A​Xk)+θ​Ξ+Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]=0\displaystyle\left[\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\right]\gamma^{\*}-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k})+\theta\Xi+\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | γ∗=[Λ′​Pk+1​Λ​Δ​t−Id−θ​Σ′​(Σ​Σ′)−1​Σ]−1​{θ​Σ′​(Σ​Σ′)−1​(a+A​Xk)−θ​Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}\displaystyle\gamma^{\*}=\left[\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\right]^{-1}\left\{\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k})-\theta\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\} |  | (3.50) |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ∗=ℬk+1−1​{−θ​Σ′​(Σ​Σ′)−1​(a+A​Xk)+Λ′​Pk+1​(b​Δ​t+B~​Xk)+Λ′​pk+1+θ​Ξ},\displaystyle\gamma^{\*}=\mathcal{B}\_{k+1}^{-1}\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k})+\Lambda^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\}, |  | (3.51) |

with ℬk+1\mathcal{B}\_{k+1} defined at ([3.45](#S3.E45 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")).

Under Assumption [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), FkF\_{k} reaches a maximum in its argument γ¯\bar{\gamma} at γ∗\gamma^{\*}. Substituting η∗=0\eta^{\*}=0 and ([3.51](#S3.E51 "In Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) into ([3.3](#S3.Ex61 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h∗=\displaystyle h^{\*}= | (ΣΣ′)−1{(a+AXk)+Σℬk+1−1{−θΣ′(ΣΣ′)−1(a+AXk)+θΞ+Λ′[Pk+1(bΔt+B~Xk)+pk+1]}\displaystyle\left(\Sigma\Sigma^{\prime}\right)^{-1}\Bigg\{(a+AX\_{k})+\Sigma\mathcal{B}\_{k+1}^{-1}\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k})+\theta\Xi+\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (Σ​Σ′)−1​{{Im−θ​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1}​(a+A​Xk)+Σ​ℬk+1−1​{Λ′​Pk+1​(b​Δ​t+B~​Xk)+Λ′​pk+1+θ​Ξ}}\displaystyle\left(\Sigma\Sigma^{\prime}\right)^{-1}\Bigg\{\left\{I\_{m}-\theta\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\right\}(a+AX\_{k})+\Sigma\mathcal{B}\_{k+1}^{-1}\left\{\Lambda^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\}\Bigg\} |  | (3.52) |

∎

The following Proposition presents an alternative characterization of the candidate controls which will prove convenient to interpret the optimal asset allocation as a Fractional Kelly Strategy in Section [4.3](#S4.SS3 "4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") below.

###### Proposition 3.9.

Under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), the candidate optimal controls are given by the stationary point (hk∗,γk∗,ηk∗),k=0,…​K−1(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k}),k=0,\ldots K-1 of the quadratic function
Fk​(h¯,γ¯,η¯;Xk)F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k}) at ([3.3](#S3.Ex46 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and can be explicitly expressed as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hk∗=\displaystyle h^{\*}\_{k}= | 1θ+1​𝒞k+1−1​(θ)​[(a+A​Xk)+θ​𝒜k+1−1​Σ​{Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}]\displaystyle\frac{1}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\Bigg[(a+AX\_{k})+\theta\mathcal{A}\_{k+1}^{-1}\Sigma\left\{\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Bigg] |  | (3.53) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | γk∗=\displaystyle\gamma^{\*}\_{k}= | 𝒜k+1−1{θθ+1Σ′𝒞k+1−1(θ)(a+AXk)+θ(θθ+1Σ′𝒞k+1−1(θ)𝒜k+1−1−Id)ΣΞ\displaystyle\mathcal{A}\_{k+1}^{-1}\Bigg\{\frac{\theta}{\theta+1}\Sigma^{\prime}\mathcal{C}\_{k+1}^{-1}\!(\theta)(a+AX\_{k})+\theta\left(\frac{\theta}{\theta+1}\Sigma^{\prime}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}-I\_{d}\right)\Sigma\Xi |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(θθ+1Σ′𝒞k+1−1(θ)𝒜k+1−1Σ+Id)Λ′[Pk+1(bΔt+B~Xk)+pk+1]}.\displaystyle-\left(\frac{\theta}{\theta+1}\Sigma^{\prime}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma+I\_{d}\right)\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\Bigg\}. |  | (3.54) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ηk∗=\displaystyle\eta^{\*}\_{k}= | 0.\displaystyle 0. |  | (3.55) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞k+1​(θ):=1θ+1​Σ​[Id−θ​𝒜k+1−1]​Σ′,\displaystyle\mathcal{C}\_{k+1}\!(\theta):=\frac{1}{\theta+1}\Sigma\left[I\_{d}-\theta\mathcal{A}\_{k+1}^{-1}\right]\Sigma^{\prime}, |  | (3.56) |

for k=0,…,K−1k=0,\ldots,K-1.

###### Proof.

Propositions [3.7](#S3.Thmtheorem7 "Proposition 3.7 (Saddle Point Representation). ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") already showed that FkF\_{k} is convex in h¯\bar{h} and concave in γ¯\bar{\gamma} and η¯\bar{\eta} provided that Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") hold.

To prove Proposition [3.9](#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), we proceed in the reverse order of Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), applying the first order condition with respect to γ¯\bar{\gamma} and then with respect to h¯\bar{h}:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Fk∂γ¯​(h∗,γ¯,η∗;Xk)|h¯=h∗,γ¯=γ∗,η¯=η∗=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{\gamma}}(h^{\*},\bar{\gamma},\eta^{\*};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=\eta^{\*}}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | 𝒜k+1​γ∗−θ​Σ′​(h∗+η∗)+θ​Ξ+Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]=0\displaystyle\mathcal{A}\_{k+1}\gamma^{\*}-\theta\Sigma^{\prime}(h^{\*}+\eta^{\*})+\theta\Xi+\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | γ∗=𝒜k+1−1​{θ​Σ′​(h∗+η∗)−θ​Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]},\displaystyle\gamma^{\*}=\mathcal{A}\_{k+1}^{-1}\left\{\theta\Sigma^{\prime}(h^{\*}+\eta^{\*})-\theta\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}, |  | (3.57) |

By Assumption [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), 𝒜k+1<0\mathcal{A}\_{k+1}<0, hence it is invertible. The function FkF\_{k} reaches a maximum in its argument γ¯\bar{\gamma} if 𝒜k+1<0\mathcal{A}\_{k+1}<0. In the following, we also assume that Pk+1P\_{k+1} is symmetric to be able to write x′​Pk+1​y=y′​Pk+1​xx^{\prime}P\_{k+1}y=y^{\prime}P\_{k+1}x.

We substitute this expression into FkF\_{k}

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Fk​(h∗,γ∗,η∗;Xk)\displaystyle F\_{k}(h^{\*},\gamma^{\*},\eta^{\*};X\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | θ2​(h∗+η∗)′​Σ​Σ′​(h∗+η∗)​Δ​t−θ​(h∗+η∗)′​(a+A​Xk)​Δ​t\displaystyle\frac{\theta}{2}\left(h^{\*}+\eta^{\*}\right)^{\prime}\Sigma\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)\Delta t-\theta\left(h^{\*}+\eta^{\*}\right)^{\prime}(a+AX\_{k})\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​((h∗+η∗)′​Σ−Ξ′)​𝒜k+1−1​{θ​Σ′​(h∗+η∗)−θ​Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}​Δ​t\displaystyle-\theta\left((h^{\*}+\eta^{\*})^{\prime}\Sigma-\Xi^{\prime}\right)\mathcal{A}\_{k+1}^{-1}\left\{\theta\Sigma^{\prime}(h^{\*}+\eta^{\*})-\theta\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​{θ​Σ′​(h∗+η∗)−θ​Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}′\displaystyle+\frac{1}{2}\left\{\theta\Sigma^{\prime}(h^{\*}+\eta^{\*})-\theta\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅𝒜k+1−1​𝒜k+1​𝒜k+1−1​{θ​Σ′​(h∗+η∗)−θ​Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}​Δ​t\displaystyle\cdot\cancel{\mathcal{A}\_{k+1}^{-1}}\cancel{\mathcal{A}\_{k+1}}\mathcal{A}\_{k+1}^{-1}\left\{\theta\Sigma^{\prime}(h^{\*}+\eta^{\*})-\theta\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[Pk+1​(b​Δ​t+B~​Xk)+pk+1]′​Λ​𝒜k+1−1​{θ​Σ′​(h∗+η∗)−θ​Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}​Δ​t\displaystyle+\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]^{\prime}\Lambda\mathcal{A}\_{k+1}^{-1}\left\{\theta\Sigma^{\prime}(h^{\*}+\eta^{\*})-\theta\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​(η∗)′​Ψk−1​η∗\displaystyle-\frac{1}{2}(\eta^{\*})^{\prime}\Psi\_{k}^{-1}\eta^{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | θ2​(h∗+η∗)′​Σ​{Id−θ​𝒜k+1−1}​Σ′​(h∗+η∗)​Δ​t\displaystyle\frac{\theta}{2}\left(h^{\*}+\eta^{\*}\right)^{\prime}\Sigma\left\{I\_{d}-\theta\mathcal{A}\_{k+1}^{-1}\right\}\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​(h∗+η∗)′​[(a+A​Xk)+θ​𝒜k+1−1​Σ​{Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}]​Δ​t−θ22​Ξ′​𝒜k+1−1​Ξ​Δ​t\displaystyle-\theta\left(h^{\*}+\eta^{\*}\right)^{\prime}\Bigg[(a+AX\_{k})+\theta\mathcal{A}\_{k+1}^{-1}\Sigma\left\{\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Bigg]\Delta t-\frac{\theta^{2}}{2}\Xi^{\prime}\mathcal{A}\_{k+1}^{-1}\Xi\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −12​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]′​Λ​𝒜k+1−1​Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]​Δ​t−12​(η∗)′​Ψk−1​η∗\displaystyle-\frac{1}{2}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]^{\prime}\Lambda\mathcal{A}\_{k+1}^{-1}\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\Delta t-\frac{1}{2}(\eta^{\*})^{\prime}\Psi\_{k}^{-1}\eta^{\*} |  | (3.58) |

By the first order condition, h∗h^{\*} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Fk∂h¯​(h¯,γ¯,η¯;Xk)|h¯=h∗,γ¯=γ∗,η¯=η∗=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{h}}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=\eta^{\*}}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | θ​Σ​{Id−θ​𝒜k+1−1}​Σ′​(h∗+η∗)​Δ​t\displaystyle\theta\Sigma\left\{I\_{d}-\theta\mathcal{A}\_{k+1}^{-1}\right\}\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −θ​[(a+A​Xk)+θ​𝒜k+1−1​Σ​{Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}]​Δ​t=0\displaystyle-\theta\Bigg[(a+AX\_{k})+\theta\mathcal{A}\_{k+1}^{-1}\Sigma\left\{\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Bigg]\Delta t=0 |  | (3.59) |

and η∗\eta^{\*} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Fk∂η¯​(h¯,γ¯,η¯;Xk)|h¯=h∗,γ¯=γ∗,η¯=η∗=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{\eta}}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=\eta^{\*}}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | θ​Σ​{Id−θ​𝒜k+1−1}​Σ′​(h∗+η∗)​Δ​t\displaystyle\theta\Sigma\left\{I\_{d}-\theta\mathcal{A}\_{k+1}^{-1}\right\}\Sigma^{\prime}\left(h^{\*}+\eta^{\*}\right)\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​[(a+A​Xk)+θ​𝒜k+1−1​Σ​{Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}]​Δ​t−Ψk−1​η∗=0\displaystyle-\theta\Bigg[(a+AX\_{k})+\theta\mathcal{A}\_{k+1}^{-1}\Sigma\left\{\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Bigg]\Delta t-\Psi\_{k}^{-1}\eta^{\*}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | ∂Fk∂h¯​(h¯,γ¯,η¯;Xk)|h¯=h∗,γ¯=γ∗,η¯=η∗−Ψk−1​η∗=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{h}}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=\eta^{\*}}-\Psi\_{k}^{-1}\eta^{\*}=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | Ψk−1​η∗=0\displaystyle\Psi\_{k}^{-1}\eta^{\*}=0 |  | (3.60) |

which shows that η∗=0\eta^{\*}=0, as expected. Here, η∗\eta^{\*} maximizes FkF\_{k} in its argument η¯\bar{\eta} if

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​Σ​{Id−θ​𝒜k+1−1}​Σ′​Δ​t−Ψk−1<0.\displaystyle\theta\Sigma\left\{I\_{d}-\theta\mathcal{A}\_{k+1}^{-1}\right\}\Sigma^{\prime}\Delta t-\Psi\_{k}^{-1}<0. |  | (3.61) |

With η∗=0\eta^{\*}=0, the first order condition for h¯\bar{h} becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∂Fk∂h¯​(h¯,γ¯,η¯;Xk)|h¯=h∗,γ¯=γ∗,η¯=0=0\displaystyle\frac{\partial F\_{k}}{\partial\bar{h}}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\Big|\_{\bar{h}=h^{\*},\bar{\gamma}=\gamma^{\*},\bar{\eta}=0}=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | h∗=1θ+1​𝒞k+1−1​(θ)​[(a+A​Xk)+θ​𝒜k+1−1​Σ​{Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}]\displaystyle h^{\*}=\frac{1}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\Bigg[(a+AX\_{k})+\theta\mathcal{A}\_{k+1}^{-1}\Sigma\left\{\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Bigg] |  | (3.62) |

with 𝒞k+1​(θ)\mathcal{C}\_{k+1}\!(\theta) defined at ([3.56](#S3.E56 "In Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")). The function FkF\_{k} reaches a minimum in its argument h¯\bar{h} if

|  |  |  |  |
| --- | --- | --- | --- |
|  | (θ+1)​𝒞k+1​(θ)=Σ​[Id−θ​(Λ′​Pk+1​Λ​Δ​t−Id)−1]​Σ′>0.\displaystyle(\theta+1)\mathcal{C}\_{k+1}\!(\theta)=\Sigma\left[I\_{d}-\theta\left(\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}\right)^{-1}\right]\Sigma^{\prime}>0. |  | (3.63) |

This condition ensures strict convexity of FkF\_{k} in
h¯\bar{h}, hence uniqueness of h∗h^{\*}.

To get ([3.9](#S3.Ex70 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we substitute the expression we obtained for h∗h^{\*} and η∗=0\eta^{\*}=0 into ([3.3](#S3.Ex71 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), concluding the proof.

∎

Although Proposition [3.9](#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") is stated under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), the derivation naturally reveals the equivalent sufficient conditions ([3.63](#S3.E63 "In Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), ([3.61](#S3.E61 "In Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and 𝒜k+1<0\mathcal{A}\_{k+1}<0, which are summarized in the remark below.

###### Remark 9.

The conditions at ([3.63](#S3.E63 "In Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and ([3.61](#S3.E61 "In Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), together with the condition 𝒜k+1<0\mathcal{A}\_{k+1}<0, provide a set of sufficient conditions for the existence of a saddle point that is equivalent to the sufficient conditions stated in Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). Section [4](#S4 "4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") discusses the intuition and implications of these conditions.

### 3.4 Main Result

Before proving the main result, we use the first characterization of the controls in Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") to derive a quadratic representation of FkF\_{k} at the saddle point (hk∗,γk∗,ηk∗)(h\_{k}^{\*},\gamma\_{k}^{\*},\eta\_{k}^{\*}).

###### Proposition 3.10.

Under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), at the saddle point (hk∗,γk∗,ηk∗)(h\_{k}^{\*},\gamma\_{k}^{\*},\eta\_{k}^{\*}), the function Fk​(h¯k,γ¯k,η¯k;Xk)F\_{k}(\bar{h}\_{k},\bar{\gamma}\_{k},\bar{\eta}\_{k};X\_{k}) from ([3.3](#S3.Ex46 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) has the quadratic representation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Fk​(hk∗,γk∗,ηk∗;Xk)=\displaystyle F\_{k}(h\_{k}^{\*},\gamma\_{k}^{\*},\eta\_{k}^{\*};X\_{k})= | 12​Xk′​𝔔k+1​Xk+Xk′​𝔮k+1+𝔩k+1,\displaystyle\frac{1}{2}X\_{k}^{\prime}\mathfrak{Q}\_{k+1}X\_{k}+X\_{k}^{\prime}\mathfrak{q}\_{k+1}+\mathfrak{l}\_{k+1}, |  | (3.64) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔔k+1=\displaystyle\mathfrak{Q}\_{k+1}= | −θ​A′​(Σ​Σ′)−1​A​Δ​t+θ2​A′​(Σ​Σ′)−1​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1​A​Δ​t\displaystyle-\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}A\Delta t+\theta^{2}A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}A\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −2​θ​A′​(Σ​Σ′)−1​Σ​ℬk+1−1​Λ′​Pk+1​B~​Δ​t+B~′​Pk+1​Λ​ℬk+1−1​Λ′​Pk+1​B~​Δ​t,\displaystyle-2\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Lambda^{\prime}P\_{k+1}\tilde{B}\Delta t+\tilde{B}^{\prime}P\_{k+1}\Lambda\mathcal{B}\_{k+1}^{-1}\Lambda^{\prime}P\_{k+1}\tilde{B}\Delta t, |  | (3.65) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔮k+1=\displaystyle\mathfrak{q}\_{k+1}= | −θ​A′​(Σ​Σ′)−1​a​Δ​t+{−θ​A′​(Σ​Σ′)−1​Σ+B~′​Pk+1​Λ}​ℬk+1−1\displaystyle-\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a\Delta t+\left\{-\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma+\tilde{B}^{\prime}P\_{k+1}\Lambda\right\}\mathcal{B}\_{k+1}^{-1} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⋅{−θ​Σ′​(Σ​Σ′)−1​a+Λ′​[Pk+1​b​Δ​t+pk+1]+θ​Ξ}​Δ​t\displaystyle\cdot\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a+\Lambda^{\prime}\left[P\_{k+1}b\Delta t+p\_{k+1}\right]+\theta\Xi\right\}\Delta t |  | (3.66) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔩k+1=\displaystyle\mathfrak{l}\_{k+1}= | −θ2​a′​(Σ​Σ′)−1​a​Δ​t+12​{−θ​a′​(Σ​Σ′)−1​Σ+b′​Pk+1​Λ​Δ​t+pk+1′​Λ+θ​Ξ′}​ℬk+1−1\displaystyle-\frac{\theta}{2}a^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a\Delta t+\frac{1}{2}\left\{-\theta a^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma+b^{\prime}P\_{k+1}\Lambda\Delta t+p\_{k+1}^{\prime}\Lambda+\theta\Xi^{\prime}\right\}\mathcal{B}\_{k+1}^{-1} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⋅{−θ​Σ′​(Σ​Σ′)−1​a+Λ′​Pk+1​b​Δ​t+Λ′​pk+1+θ​Ξ}​Δ​t\displaystyle\cdot\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a+\Lambda^{\prime}P\_{k+1}b\Delta t+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\}\Delta t |  | (3.67) |

###### Proof.

We start from the definition of γ∗\gamma^{\*} at ([3.43](#S3.E43 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and write, for convenience

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γk∗\displaystyle\gamma^{\*}\_{k} | =𝔎k+1​Xk+𝔨k+1,\displaystyle=\mathfrak{K}\_{k+1}X\_{k}+\mathfrak{k}\_{k+1}, |  | (3.68) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔎k+1\displaystyle\mathfrak{K}\_{k+1} | =ℬk+1−1​{−θ​Σ′​(Σ​Σ′)−1​A+Λ′​Pk+1​B~}\displaystyle=\mathcal{B}\_{k+1}^{-1}\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}A+\Lambda^{\prime}P\_{k+1}\tilde{B}\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔨k+1\displaystyle\mathfrak{k}\_{k+1} | =ℬk+1−1​{−θ​Σ′​(Σ​Σ′)−1​a+Λ′​Pk+1​b​Δ​t+Λ′​pk+1+θ​Ξ}.\displaystyle=\mathcal{B}\_{k+1}^{-1}\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a+\Lambda^{\prime}P\_{k+1}b\Delta t+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\}. |  | (3.69) |

Next, we use equation ([3.3](#S3.Ex61 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) to express h∗h^{\*} in terms of γ∗\gamma^{\*}. Recalling that η∗=0\eta^{\*}=0, equation ([3.3](#S3.Ex61 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=\displaystyle h^{\*}\_{k}= | (Σ​Σ′)−1​[(a+A​Xk)+Σ​γ∗]\displaystyle\left(\Sigma\Sigma^{\prime}\right)^{-1}\left[(a+AX\_{k})+\Sigma\gamma^{\*}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (Σ​Σ′)−1​[(A+Σ​𝔎k+1)​Xk+(a+Σ​𝔨k+1)]\displaystyle\left(\Sigma\Sigma^{\prime}\right)^{-1}\left[\left(A+\Sigma\mathfrak{K}\_{k+1}\right)X\_{k}+\left(a+\Sigma\mathfrak{k}\_{k+1}\right)\right] |  | (3.70) |

Then, at the saddle point (hk∗,γk∗,ηk∗)(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k}), we express the function FkF\_{k}, which was defined at ([3.3](#S3.Ex46 "3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), as:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Fk​(hk∗,γk∗,ηk∗;Xk)\displaystyle F\_{k}(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k};X\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | Xk′{θ2(A+Σ𝔎k+1)′(ΣΣ′)−1(A+Σ𝔎k+1)Δt−θA′(ΣΣ′)−1(A+Σ𝔎k+1)Δt\displaystyle X\_{k}^{\prime}\Bigg\{\frac{\theta}{2}\left(A+\Sigma\mathfrak{K}\_{k+1}\right)^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(A+\Sigma\mathfrak{K}\_{k+1}\right)\Delta t-\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(A+\Sigma\mathfrak{K}\_{k+1}\right)\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​(A+Σ​𝔎k+1)′​(Σ​Σ′)−1​Σ​𝔎k+1​Δ​t+12​𝔎k+1′​[Λ′​Pk+1​Λ​Δ​t−Id]​𝔎k+1​Δ​t\displaystyle-\theta\left(A+\Sigma\mathfrak{K}\_{k+1}\right)^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathfrak{K}\_{k+1}\Delta t+\frac{1}{2}\mathfrak{K}\_{k+1}^{\prime}\left[\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}\right]\mathfrak{K}\_{k+1}\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔎k+1′Λ′Pk+1B~Δt}Xk\displaystyle+\mathfrak{K}\_{k+1}^{\prime}\Lambda^{\prime}P\_{k+1}\tilde{B}\Delta t\Bigg\}X\_{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +{θ(a+Σ𝔨k+1)′(ΣΣ′)−1(A+Σ𝔎k+1)Δt−θ(a+Σ𝔨k+1)′(ΣΣ′)−1AΔt\displaystyle+\Bigg\{\theta\left(a+\Sigma\mathfrak{k}\_{k+1}\right)^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(A+\Sigma\mathfrak{K}\_{k+1}\right)\Delta t-\theta\left(a+\Sigma\mathfrak{k}\_{k+1}\right)^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}A\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​a′​(Σ​Σ′)−1​(A+Σ​𝔎k+1)​Δ​t−θ​𝔨k+1′​Σ′​(Σ​Σ′)−1​(A+Σ​𝔎k+1)​Δ​t\displaystyle-\theta a^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(A+\Sigma\mathfrak{K}\_{k+1}\right)\Delta t-\theta\mathfrak{k}\_{k+1}^{\prime}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(A+\Sigma\mathfrak{K}\_{k+1}\right)\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​(a+Σ​𝔨k+1)′​(Σ​Σ′)−1​Σ​𝔎k+1​Δ​t+θ​Ξ′​𝔎k+1​Δ​t\displaystyle-\theta\left(a+\Sigma\mathfrak{k}\_{k+1}\right)^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathfrak{K}\_{k+1}\Delta t+\theta\Xi^{\prime}\mathfrak{K}\_{k+1}\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔨k+1′​[Λ′​Pk+1​Λ​Δ​t−Id]​𝔎k+1​Δ​t+[Pk+1​b​Δ​t+pk+1]′​Λ​𝔎k+1​Δ​t\displaystyle+\mathfrak{k}\_{k+1}^{\prime}\left[\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}\right]\mathfrak{K}\_{k+1}\Delta t+\left[P\_{k+1}b\Delta t+p\_{k+1}\right]^{\prime}\Lambda\mathfrak{K}\_{k+1}\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔨k+1′Λ′Pk+1B~Δt}Xk\displaystyle+\mathfrak{k}\_{k+1}^{\prime}\Lambda^{\prime}P\_{k+1}\tilde{B}\Delta t\Bigg\}X\_{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +{θ2(a+Σ𝔨k+1)′(ΣΣ′)−1(a+Σ𝔨k+1)Δt−θa′(ΣΣ′)−1(a+Σ𝔨k+1)Δt\displaystyle+\Bigg\{\frac{\theta}{2}\left(a+\Sigma\mathfrak{k}\_{k+1}\right)^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(a+\Sigma\mathfrak{k}\_{k+1}\right)\Delta t-\theta a^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(a+\Sigma\mathfrak{k}\_{k+1}\right)\Delta t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θ​(a+Σ​𝔨k+1)′​(Σ​Σ′)−1​Σ​𝔨k+1​Δ​t+θ​Ξ′​𝔨k+1​Δ​t\displaystyle-\theta\left(a+\Sigma\mathfrak{k}\_{k+1}\right)^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathfrak{k}\_{k+1}\Delta t+\theta\Xi^{\prime}\mathfrak{k}\_{k+1}\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12𝔨k+1′[Λ′Pk+1ΛΔt−Id]𝔨k+1Δt+𝔨k+1′Λ′[Pk+1bΔt+pk+1]Δt}\displaystyle+\frac{1}{2}\mathfrak{k}\_{k+1}^{\prime}\left[\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}\right]\mathfrak{k}\_{k+1}\Delta t+\mathfrak{k}\_{k+1}^{\prime}\Lambda^{\prime}\left[P\_{k+1}b\Delta t+p\_{k+1}\right]\Delta t\Bigg\} |  | (3.71) |

The function FkF\_{k} is quadratic in XkX\_{k} at the saddle point (hk∗,γk∗,ηk∗)(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k}). We can write it as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Fk​(hk∗,γk∗,ηk∗;Xk)=\displaystyle F\_{k}(h\_{k}^{\*},\gamma\_{k}^{\*},\eta\_{k}^{\*};X\_{k})= | 12​Xk′​𝔔k+1​Xk+Xk′​𝔮k+1+𝔩k+1\displaystyle\frac{1}{2}X\_{k}^{\prime}\mathfrak{Q}\_{k+1}X\_{k}+X\_{k}^{\prime}\mathfrak{q}\_{k+1}+\mathfrak{l}\_{k+1} |  | (3.72) |

where 𝔔k+1\mathfrak{Q}\_{k+1}, 𝔮k+1\mathfrak{q}\_{k+1}, and 𝔩k+1\mathfrak{l}\_{k+1} are respectively the coefficients of the quadratic term, linear term, and zeroth-order term in ([3.4](#S3.Ex94 "Proof. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")).

Identifying coefficients of the quadratic, linear, and constant terms in ([3.4](#S3.Ex94 "Proof. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and then substituting the expressions for 𝔎k+1\mathfrak{K}\_{k+1} and 𝔨k+1\mathfrak{k}\_{k+1}, gives ([3.10](#S3.Ex89 "Proposition 3.10. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))–([3.10](#S3.Ex91 "Proposition 3.10. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")).

∎

We can now state our main result.

###### Theorem 3.11.

Under Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), the value function uu has, as mentioned in ([3.28](#S3.E28 "In 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), a quadratic form of the type

|  |  |  |  |
| --- | --- | --- | --- |
|  | uk​(Xk)=12​Xk′​Pk​Xk+Xk′​pk+rk,k=0,…,K.\displaystyle u\_{k}(X\_{k})=\frac{1}{2}X\_{k}^{\prime}P\_{k}X\_{k}+X\_{k}^{\prime}p\_{k}+r\_{k},\quad k=0,\ldots,K. |  | (3.73) |

where PkP\_{k}, pkp\_{k}, and rkr\_{k} are deterministic and satisfy the following backward recursions

1. (i)

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Pk=\displaystyle P\_{k}= | −θ​A′​(Σ​Σ′)−1​A​Δ​t+θ2​A′​(Σ​Σ′)−1​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1​A​Δ​t\displaystyle-\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}A\Delta t+\theta^{2}A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}A\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −2​θ​A′​(Σ​Σ′)−1​Σ​ℬk+1−1​Λ′​Pk+1​B~​Δ​t+B~′​Pk+1​Λ​ℬk+1−1​Λ′​Pk+1​B~​Δ​t\displaystyle-2\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Lambda^{\prime}P\_{k+1}\tilde{B}\Delta t+\tilde{B}^{\prime}P\_{k+1}\Lambda\mathcal{B}\_{k+1}^{-1}\Lambda^{\prime}P\_{k+1}\tilde{B}\Delta t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +B~′​Pk+1​B~,\displaystyle+\tilde{B}^{\prime}P\_{k+1}\tilde{B}, |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | PT\displaystyle P\_{T} | =0,\displaystyle=0, |  | (3.74) |
2. (ii)

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | pk=\displaystyle p\_{k}= | −θ​A′​(Σ​Σ′)−1​a​Δ​t+{−θ​A′​(Σ​Σ′)−1​Σ+B~′​Pk+1​Λ}​ℬk+1−1\displaystyle-\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a\Delta t+\left\{-\theta A^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma+\tilde{B}^{\prime}P\_{k+1}\Lambda\right\}\mathcal{B}\_{k+1}^{-1} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ⋅{−θ​Σ′​(Σ​Σ′)−1​a+Λ′​[Pk+1​b​Δ​t+pk+1]+θ​Ξ}​Δ​t+[B~′​(Pk+1​b+pk+1​1Δ​t)+θ​C′]​Δ​t,\displaystyle\cdot\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a+\Lambda^{\prime}\left[P\_{k+1}b\Delta t+p\_{k+1}\right]+\theta\Xi\right\}\Delta t+\left[\tilde{B}^{\prime}\left(P\_{k+1}b+p\_{k+1}\frac{1}{\Delta t}\right)+\theta C^{\prime}\right]\Delta t, |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | pT=\displaystyle p\_{T}= | 0,\displaystyle 0, |  | (3.75) |
3. (iii)

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | rk=\displaystyle r\_{k}= | rk+1−θ2​a′​(Σ​Σ′)−1​a​Δ​t+12​{−θ​a′​(Σ​Σ′)−1​Σ+b′​Pk+1​Λ​Δ​t+pk+1′​Λ+θ​Ξ′}​ℬk+1−1\displaystyle r\_{k+1}-\frac{\theta}{2}a^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a\Delta t+\frac{1}{2}\left\{-\theta a^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma+b^{\prime}P\_{k+1}\Lambda\Delta t+p\_{k+1}^{\prime}\Lambda+\theta\Xi^{\prime}\right\}\mathcal{B}\_{k+1}^{-1} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ⋅{−θ​Σ′​(Σ​Σ′)−1​a+Λ′​Pk+1​b​Δ​t+Λ′​pk+1+θ​Ξ}​Δ​t,\displaystyle\cdot\left\{-\theta\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}a+\Lambda^{\prime}P\_{k+1}b\Delta t+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\}\Delta t, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +[12​b′​Pk+1​b​Δ​t+b′​pk+1+θ​c+θ2​tr​(Ψk​Σ​Σ′)−θ2​Ξ′​Ξ+12​tr​(Λ′​Pk+1​Λ)]​Δ​t\displaystyle+\left[\frac{1}{2}b^{\prime}P\_{k+1}b\Delta t+b^{\prime}p\_{k+1}+\theta c+\frac{\theta}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)-\frac{\theta}{2}\Xi^{\prime}\Xi+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\right]\Delta t |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  |  | rT=0.\displaystyle r\_{T}=0. |  | (3.76) |

Furthermore, the candidate optimal controls are given by the saddle point (h∗,γ∗,η∗)(h^{\*},\gamma^{\*},\eta^{\*}) of F​(h¯,γ¯,η¯)F(\bar{h},\bar{\gamma},\bar{\eta}) according to Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") (formulas at ([3.42](#S3.E42 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))-([3.44](#S3.E44 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))).

###### Proof.

From Propositions [3.7](#S3.Thmtheorem7 "Proposition 3.7 (Saddle Point Representation). ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.10](#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uk​(Xk)=\displaystyle u\_{k}(X\_{k})= | infh¯supγ¯,η¯{Fk​(h¯,γ¯,η¯;Xk)}+12​(b​Δ​t+B~​Xk)′​Pk+1​(b​Δ​t+B~​Xk)+(b​Δ​t+B~​Xk)′​pk+1\displaystyle\inf\_{\bar{h}}\sup\_{\bar{\gamma},\bar{\eta}}\left\{F\_{k}(\bar{h},\bar{\gamma},\bar{\eta};X\_{k})\right\}+\frac{1}{2}\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\left(b\Delta t+\tilde{B}X\_{k}\right)^{\prime}p\_{k+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +θ​(c+C​Xk)​Δ​t+θ2​tr​(Ψk​Σ​Σ′)​Δ​t−θ2​Ξ′​Ξ​Δ​t+12​tr​(Λ′​Pk+1​Λ)​Δ​t+rk+1\displaystyle+\theta(c+CX\_{k})\Delta t+\frac{\theta}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)\Delta t-\frac{\theta}{2}\Xi^{\prime}\Xi\Delta t+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\Delta t+r\_{k+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 12​Xk′​𝔔k+1​Xk+Xk′​𝔮k+1+𝔩k+1+12​Xk′​B~′​Pk+1​B~​Xk+[b′​Pk+1​B~+pk+1′​B~​1Δ​t+θ​C]​Xk​Δ​t\displaystyle\frac{1}{2}X\_{k}^{\prime}\mathfrak{Q}\_{k+1}X\_{k}+X\_{k}^{\prime}\mathfrak{q}\_{k+1}+\mathfrak{l}\_{k+1}+\frac{1}{2}X\_{k}^{\prime}\tilde{B}^{\prime}P\_{k+1}\tilde{B}X\_{k}+\left[b^{\prime}P\_{k+1}\tilde{B}+p\_{k+1}^{\prime}\tilde{B}\frac{1}{\Delta t}+\theta C\right]X\_{k}\Delta t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +[12​b′​Pk+1​b​Δ​t+b′​pk+1+θ​c+θ2​tr​(Ψk​Σ​Σ′)−θ2​Ξ′​Ξ+12​tr​(Λ′​Pk+1​Λ)]​Δ​t+rk+1\displaystyle+\left[\frac{1}{2}b^{\prime}P\_{k+1}b\Delta t+b^{\prime}p\_{k+1}+\theta c+\frac{\theta}{2}\text{tr}\left(\Psi\_{k}\Sigma\Sigma^{\prime}\right)-\frac{\theta}{2}\Xi^{\prime}\Xi+\frac{1}{2}\text{tr}\left(\Lambda^{\prime}P\_{k+1}\Lambda\right)\right]\Delta t+r\_{k+1} |  | (3.77) |

with 𝔔k+1\mathfrak{Q}\_{k+1}, 𝔮k+1\mathfrak{q}\_{k+1}, 𝔩k+1\mathfrak{l}\_{k+1} given at ([3.10](#S3.Ex89 "Proposition 3.10. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))–([3.10](#S3.Ex91 "Proposition 3.10. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")). Equate this expression with the quadratic form at ([3.73](#S3.E73 "In Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")). The recursions for PkP\_{k}, pkp\_{k}, and rkr\_{k} at ([i](#S3.Ex105 "item i ‣ Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))-([iii](#S3.Ex110 "item iii ‣ Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) follow.

Moreover, the candidate controls given by the saddle point (h∗,γ∗,η∗)(h^{\*},\gamma^{\*},\eta^{\*}) of F​(h¯,γ¯,η¯)F(\bar{h},\bar{\gamma},\bar{\eta}) given at ([3.42](#S3.E42 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))-([3.44](#S3.E44 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) are admissible, in the sense that h∗∈𝒜¯explHh^{\*}\in\bar{\mathcal{A}}^{H}\_{\text{expl}}, γ∗∈𝒜¯Γ¯\gamma^{\*}\in\bar{\mathcal{A}}^{\bar{\Gamma}}, and η∗∈𝒜¯η¯\eta^{\*}\in\bar{\mathcal{A}}^{\bar{\eta}}, so they are optimal. Consequently,

|  |  |  |
| --- | --- | --- |
|  | supγ¯,η¯𝐄γ¯,η¯​[−θ​(R¯Tπ−R0)−12​∑k=0K−1(‖γ¯k‖2​Δ​t+η¯k′​Ψk−1​η¯k)]\displaystyle\sup\_{\bar{\gamma},\bar{\eta}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\theta(\bar{R}^{\pi}\_{T}-R\_{0})-\frac{1}{2}\sum\_{k=0}^{K-1}\left(\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =supγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[−θ​(R¯Tπ−R0)−12​∑k=0K−1(‖γ¯k‖2​Δ​t+η¯k′​Ψk−1​η¯k)],\displaystyle=\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\left[-\theta(\bar{R}^{\pi}\_{T}-R\_{0})-\frac{1}{2}\sum\_{k=0}^{K-1}\left(\|\bar{\gamma}\_{k}\|^{2}\Delta t+\bar{\eta}\_{k}^{\prime}\Psi\_{k}^{-1}\bar{\eta}\_{k}\right)\right], |  | (3.78) |

which shows that Assumption [3.4](#S3.Thmtheorem4 "Assumption 3.4. ‣ 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") holds.
∎

###### Corollary 3.12.

We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | infh¯∈𝒜¯explHI​(H,θ)=exp⁡{12​X0′​P0​X0+X0′​p0+r0}\displaystyle\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}I(H,\theta)=\exp\left\{\frac{1}{2}X\_{0}^{\prime}P\_{0}X\_{0}+X\_{0}^{\prime}p\_{0}+r\_{0}\right\} |  | (3.79) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | suph¯∈𝒜¯explHJ​(H,θ)=−1θ​(12​X0′​P0​X0+X0′​p0+r0)\displaystyle\sup\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}J(H,\theta)=-\frac{1}{\theta}\left(\frac{1}{2}X\_{0}^{\prime}P\_{0}X\_{0}+X\_{0}^{\prime}p\_{0}+r\_{0}\right) |  | (3.80) |

with PkP\_{k}, pkp\_{k}, and rkr\_{k} given by ([i](#S3.Ex105 "item i ‣ Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")),([ii](#S3.Ex108 "item ii ‣ Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and ([iii](#S3.Ex110 "item iii ‣ Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and optimal controls given by the saddle point (h∗,γ∗,η∗)(h^{\*},\gamma^{\*},\eta^{\*}) according to Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning").

###### Proof.

Start from the criterion II:

|  |  |  |  |
| --- | --- | --- | --- |
|  | infh¯∈𝒜¯explHI​(H,θ)\displaystyle\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}I(H,\theta) | =([3.2](#S3.Ex33 "3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))​exp⁡{infh¯∈𝒜¯explHsupγ¯∈𝒜Γ¯,η¯∈𝒜η¯𝐄γ¯,η¯​[θ​∑k=0K−1g​(Xk,h¯k,η¯k,γ¯k)​Δ​t]}\displaystyle\underset{\eqref{eq:EEDuality:inf}}{=}\exp\left\{\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\sup\_{\bar{\gamma}\in\mathcal{A}^{\bar{\Gamma}},\bar{\eta}\in\mathcal{A}^{\bar{\eta}}}\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(X\_{k},\bar{h}\_{k},\bar{\eta}\_{k},\bar{\gamma}\_{k})\Delta t\Bigg]\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =([3.24](#S3.E24 "In 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))​exp⁡{u0​(X0)}\displaystyle\underset{\eqref{eq:criterion:I:Pbar}}{=}\exp\left\{u\_{0}(X\_{0})\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =([3.73](#S3.E73 "In Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))​at​k=0​exp⁡{12​X0′​P0​X0+X0′​p0+r0},\displaystyle\underset{\eqref{eq:Phi:quadform}\,\text{at}\,k=0}{=}\exp\left\{\frac{1}{2}X\_{0}^{\prime}P\_{0}X\_{0}+X\_{0}^{\prime}p\_{0}+r\_{0}\right\}, |  | (3.81) |

which gives ([3.79](#S3.E79 "In Corollary 3.12. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")). Furthermore,

|  |  |  |
| --- | --- | --- |
|  | ln​infh¯∈𝒜¯explHI​(H,θ)​=([3.2](#S3.Ex33 "3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))​infh¯∈𝒜¯explHln⁡I​(H,θ)​=([2.10](#S2.E10 "In 2.2 Risk-Sensitive Control Problem ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"))​infh¯∈𝒜¯explH−θ​J​(H,θ)=−θ​suph¯∈𝒜¯explHJ​(H,θ)\displaystyle\ln\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}I(H,\theta)\underset{\eqref{eq:EEDuality:inf}}{=}\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}\ln I(H,\theta)\underset{\eqref{eq:I}}{=}\inf\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}-\theta J(H,\theta)=-\theta\sup\_{\bar{h}\in\bar{\mathcal{A}}^{H}\_{\mathrm{expl}}}J(H,\theta) |  |

from which ([3.80](#S3.E80 "In Corollary 3.12. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) follows.
∎

### 3.5 Limiting Case: The Kelly Criterion

The Kelly portfolio allocation problem involves the maximization of the expected log utility. It leads to a stochastic control problem that can be seen either as the limiting case of the Linear-Quadratic-Gaussian problem studied above when θ→0\theta\to 0 or as an LQG control problem with the criterion

|  |  |  |  |
| --- | --- | --- | --- |
|  | JKelly​(H)\displaystyle J^{\text{Kelly}}(H) | :=𝐄​[RT−R0]\displaystyle:=\mathbf{E}\left[R\_{T}-R\_{0}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐄[∑k=0K−1{(−12hk′ΣΣ′hk+hk′a+12Ξ′Ξ−c)+(hk′A−C)Xk}Δt\displaystyle=\mathbf{E}\left[\sum\_{k=0}^{K-1}\left\{\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right\}\Delta t\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑k=0K−1(hk′Σ−Ξ′)wk]\displaystyle\left.+\sum\_{k=0}^{K-1}\left(h\_{k}^{\prime}\Sigma-\Xi^{\prime}\right)w\_{k}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝐄​[∑k=0K−1{(−12​hk′​Σ​Σ′​hk+hk′​a+12​Ξ′​Ξ−c)+(hk′​A−C)​Xk}​Δ​t].\displaystyle=\mathbf{E}\left[\sum\_{k=0}^{K-1}\left\{\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}\right\}\Delta t\right]. |  | (3.83) |

The instantaneous reward function has a quadratic structure, so the control problem is LQG. We can solve it directly under the measure ℙ\mathbb{P}.

We define the optimal value function uKellyu^{\text{Kelly}} for the Kelly portfolio allocation problem as

|  |  |  |  |
| --- | --- | --- | --- |
|  | u0Kelly​(X0):=supH∈𝒜H𝐄​[RT−R0]=supH∈𝒜H𝐄​[∑k=0K−1gKelly​(Xk,hk)​Δ​t].\displaystyle u^{\text{Kelly}}\_{0}(X\_{0}):=\sup\_{H\in\mathcal{A}^{H}}\mathbf{E}\left[R\_{T}-R\_{0}\right]=\sup\_{H\in\mathcal{A}^{H}}\mathbf{E}\left[\sum\_{k=0}^{K-1}g^{\text{Kelly}}\left(X\_{k},h\_{k}\right)\Delta t\right]. |  | (3.84) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | gKelly​(Xk,hk):=(−12​hk′​Σ​Σ′​hk+hk′​a+12​Ξ′​Ξ−c)+(hk′​A−C)​Xk.\displaystyle g^{\text{Kelly}}\left(X\_{k},h\_{k}\right):=\left(-\frac{1}{2}h\_{k}^{\prime}\Sigma\Sigma^{\prime}h\_{k}+h\_{k}^{\prime}a+\frac{1}{2}\Xi^{\prime}\Xi-c\right)+\left(h\_{k}^{\prime}A-C\right)X\_{k}. |  | (3.85) |

The state process XX evolves according to ([2.3](#S2.E3 "In 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk+1=b​Δ​t+B~​Xk+Λ​wk.\displaystyle X\_{k+1}=b\Delta t+\tilde{B}X\_{k}+\Lambda w\_{k}. |  | (3.86) |

Importantly, the state is uncontrolled.

We apply the Dynamic Programming Principle (DPP) to express the value function recursively as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uTKelly​(XT)=\displaystyle u^{\text{Kelly}}\_{T}(X\_{T})= | 0,\displaystyle 0, |  | (3.87) |

and, for k=K−1,⋯,0k=K-1,\cdots,0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ukKelly​(Xk)=\displaystyle u^{\text{Kelly}}\_{k}(X\_{k})= | suphk𝐄k,Xk​[gKelly​(Xk,hk)​Δ​t+uk+1Kelly​(Xk+1)]\displaystyle\sup\_{h\_{k}}\mathbf{E}\_{k,X\_{k}}\left[g^{\text{Kelly}}\left(X\_{k},h\_{k}\right)\Delta t+u^{\text{Kelly}}\_{k+1}(X\_{k+1})\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | suphk{gKelly​(Xk,hk)​Δ​t+𝐄k,Xk​[uk+1Kelly​(Xk+1)]}.\displaystyle\sup\_{h\_{k}}\left\{g^{\text{Kelly}}\left(X\_{k},h\_{k}\right)\Delta t+\mathbf{E}\_{k,X\_{k}}\left[u^{\text{Kelly}}\_{k+1}(X\_{k+1})\right]\right\}. |  | (3.88) |

We can show that ukKelly​(Xk)u^{\text{Kelly}}\_{k}(X\_{k}) has a quadratic expression in XkX\_{k} of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ukKelly​(Xk)=12​Xk′​PkKelly​Xk+Xk′​pkKelly+rkKelly,u^{\text{Kelly}}\_{k}(X\_{k})=\frac{1}{2}X\_{k}^{\prime}P^{\text{Kelly}}\_{k}X\_{k}+X\_{k}^{\prime}p^{\text{Kelly}}\_{k}+r^{\text{Kelly}}\_{k}, |  | (3.89) |

where PkKellyP^{\text{Kelly}}\_{k}, pkKellyp^{\text{Kelly}}\_{k}, and rkKellyr^{\text{Kelly}}\_{k} can be computed recursively.

Since Xk+1X\_{k+1} does not depend on hkh\_{k}, the continuation value uk+1Kelly​(Xk+1)u^{\text{Kelly}}\_{k+1}(X\_{k+1}) does not affect the first-order condition. Therefore, we can get the optimal control directly from a pointwise maximization of the function gKellyg^{\text{Kelly}}. We obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkKelly=(Σ​Σ′)−1​(a+A​Xk).\displaystyle h^{\text{Kelly}}\_{k}=\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k}). |  | (3.90) |

## 4 Interpreting the Risk-Sensitive Investment Management Model

### 4.1 Interpreting Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")

Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") are necessary for Propositions [3.7](#S3.Thmtheorem7 "Proposition 3.7 (Saddle Point Representation). ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") to hold.

Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") is a standard condition in portfolio optimization. It prevents the investment universe from containing assets with identical risk profiles, such as a commodity and a futures contract on that commodity (e.g., oil and oil futures), or the S&P 500 alongside its value and growth subindices.

Assumption [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") requires the block matrix to be negative definite, which is equivalent to satisfying both 𝒜k+1=Λ′​Pk+1​Λ​Δ​t−Id<0\mathcal{A}\_{k+1}=\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}<0 and θ​Σ​Σ′​Δ​t−Ψk−1<0\theta\Sigma\Sigma^{\prime}\Delta t-\Psi\_{k}^{-1}<0. The first subcondition, Λ′​Pk+1​Λ​Δ​t−Id<0\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}<0, is equivalent to Λ′​Pk+1​Λ​Δ​t<Id\Lambda^{\prime}P\_{k+1}\Lambda\Delta t<I\_{d}. The term Λ′​Pk+1​Λ\Lambda^{\prime}P\_{k+1}\Lambda represents the curvature of the value function projected onto the state-noise directions. Hence, the first subcondition requires that the projected curvature of the value function, when restricted to the noise subspace and scaled by Δ​t\Delta t, has all eigenvalues strictly smaller than one. This is a regularity constraint on the propagation of the state noise through the curvature of the value function.

The second subcondition, θ​Σ​Σ′​Δ​t−Ψk−1<0\theta\Sigma\Sigma^{\prime}\Delta t-\Psi\_{k}^{-1}<0, imposes the following constraint on the inverse of the covariance matrix of exploration Ψk\Psi\_{k}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψk−1>θ​Σ​Σ′​Δ​t.\displaystyle\Psi\_{k}^{-1}>\theta\Sigma\Sigma^{\prime}\Delta t. |  | (4.1) |

So Ψk\Psi\_{k} is inversely proportional to the investor’s risk sensitivity, θ\theta, the diffusion matrix of the asset returns, Σ​Σ′\Sigma\Sigma^{\prime}, and the time step, Δ​t\Delta t. These relations admit a clear economic interpretation.

Exploration increases the variability of portfolio weights, so more risk-sensitive investors will explore less. As their risk sensitivity declines, investors have more freedom to explore. In the limit as θ→0\theta\to 0, the exploration constraint becomes independent of risk sensitivity, so Kelly investors do not face a risk-sensitivity-induced upper bound on exploration.

Asset return volatility already induces variability in portfolio weights and therefore generates indirect exploration of the state variable. Therefore, investors should explore less if their investment universe contains highly volatile securities.

When the time interval between rebalancings is short, investors can afford greater exploration because they can adjust their asset allocation more frequently. With a longer time interval between rebalancings, departures from the optimal asset allocation become costlier.

### 4.2 Optimality Conditions Implied by Proposition [3.9](#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")

Equation ([3.63](#S3.E63 "In Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) in the proof of Proposition [3.9](#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") implies that at the saddle point (hk∗,γk∗,ηk∗)(h^{\*}\_{k},\gamma^{\*}\_{k},\eta^{\*}\_{k}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞k+1​(θ)>0\displaystyle\mathcal{C}\_{k+1}\!(\theta)>0 |  | (4.2) |

Recalling the definition of 𝒞k+1\mathcal{C}\_{k+1} at ([3.56](#S3.E56 "In Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we rewrite this inequality using the initial data for the control problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1θ+1​Σ​[Id−θ​(Λ′​Pk+1​Λ​Δ​t−Id)−1]​Σ′>0.\displaystyle\frac{1}{\theta+1}\Sigma\left[I\_{d}-\theta\left(\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}\right)^{-1}\right]\Sigma^{\prime}>0. |  | (4.3) |

This condition is a generalized *risk-resistance condition*, a condition typically required to solve risk-sensitive control problems (Shaiju and Petersen, [2008](#bib.bib19); Whittle, [1990](#bib.bib24)). Specifically, the term Id−θ​(Λ′​Pk+1​Λ​Δ​t−Id)−1I\_{d}-\theta\left(\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}\right)^{-1} plays the role of a risk-resistance factor in noise space. The pre- and post-multiplication by
Σ\Sigma and Σ′\Sigma^{\prime} map this noise-space condition into portfolio space. This operation is intuitive. In our setup, investors control the state variable (the risk factors) through their holdings of risky assets. Moreover, the state variable noise and the noise associated with the risky asset are correlated.

Additionally, equation ([3.61](#S3.E61 "In Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) in the proof of Proposition [3.9](#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") gives an upper bound for the covariance of exploration in terms of the risk-resistance condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψk−1>θ​Σ​{Id−θ​(Λ′​Pk+1​Λ​Δ​t−Id)−1}​Σ′​Δ​t.\displaystyle\Psi\_{k}^{-1}>\theta\Sigma\left\{I\_{d}-\theta\left(\Lambda^{\prime}P\_{k+1}\Lambda\Delta t-I\_{d}\right)^{-1}\right\}\Sigma^{\prime}\Delta t. |  | (4.4) |

To conclude, both sets of conditions ultimately compare the curvature of the value function with the intrinsic geometry of Gaussian noise. Moreover, an important advantage of applying the Free Energy-Entropy Duality is that it only requires Assumptions [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Model for the Financial Market ‣ 2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3.6](#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). These assumptions are both weaker and more directly verifiable than the classical risk-resistance condition, which typically requires recursive spectral bounds at each step.

### 4.3 Optimal Investment Strategies as Kelly Strategies

We now turn our attention to interpreting the optimal asset allocation h∗h^{\*}. We start by showing that h∗h^{\*} can be represented as an allocation to the Kelly portfolio hKellyh^{\text{Kelly}} from ([3.90](#S3.E90 "In 3.5 Limiting Case: The Kelly Criterion ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), penalized by the control γ∗\gamma^{\*} that is induced by the free energy-entropy duality penalization and the choice of an optimal measure ℙγ∗,η∗\mathbb{P}^{\gamma^{\*},\eta^{\*}}:

###### Corollary 4.1 (Corollary to Proposition [3.7](#S3.Thmtheorem7 "Proposition 3.7 (Saddle Point Representation). ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") - Kelly Strategy, Part I: Penalized Kelly Allocation).

The optimal investment strategy is to invest in both the Kelly portfolio and an allocation
(Σ​Σ′)−1​Σ​γ∗\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\gamma^{\*} related to the penalizing control γ∗\gamma^{\*} defined at ([3.43](#S3.E43 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=hkKelly+(Σ​Σ′)−1​Σ​γk∗,\displaystyle h^{\*}\_{k}=h^{\text{Kelly}}\_{k}+\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\gamma^{\*}\_{k}, |  | (4.5) |

###### Proof.

Equation ([3.3](#S3.Ex61 "Proof. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) in the proof of Proposition [3.7](#S3.Thmtheorem7 "Proposition 3.7 (Saddle Point Representation). ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") gives the following expression for the mean (h∗+η∗)(h^{\*}+\eta^{\*}) of the distribution of exploratory policies under ℙγ¯,η¯\mathbb{P}^{\bar{\gamma},\bar{\eta}}:

|  |  |  |
| --- | --- | --- |
|  | (h∗+η∗)=(Σ​Σ′)−1​[(a+A​Xk)+Σ​γk∗]\displaystyle\left(h^{\*}+\eta^{\*}\right)=\left(\Sigma\Sigma^{\prime}\right)^{-1}\left[(a+AX\_{k})+\Sigma\gamma^{\*}\_{k}\right] |  |

Since η∗=0\eta^{\*}=0, and applying the definition of the Kelly portfolio at ([3.90](#S3.E90 "In 3.5 Limiting Case: The Kelly Criterion ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=(Σ​Σ′)−1​(a+A​Xk)+(Σ​Σ′)−1​Σ​γk∗=hkKelly+(Σ​Σ′)−1​Σ​γk∗,\displaystyle h^{\*}\_{k}=\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k})+\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\gamma^{\*}\_{k}=h^{\text{Kelly}}\_{k}+\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\gamma^{\*}\_{k}, |  | (4.6) |

which proves the claim.
∎

Intuitively, the structure of equation ([4.5](#S4.E5 "In Corollary 4.1 (Corollary to Proposition 3.7 - Kelly Strategy, Part I: Penalized Kelly Allocation). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) mirrors that of the free energy-entropy duality. The duality expresses a risk-sensitive control problem as a risk-neutral LQG problem, penalized by the antagonistic control γ¯\bar{\gamma}. The optimal investment strategy at ([4.5](#S4.E5 "In Corollary 4.1 (Corollary to Proposition 3.7 - Kelly Strategy, Part I: Penalized Kelly Allocation). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) is the Kelly strategy, which is the optimal control for the risk-neutral LQG problem, penalized by a term related to the optimal antagonistic control γ∗\gamma^{\*}. This penalty term, (Σ​Σ′)−1​Σ​γ∗\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\gamma^{\*}, also has a clean geometric interpretation. It is the image of the ℝd\mathbb{R}^{d}-dimensional optimal antagonistic control γ∗\gamma^{\*} through the linear map (Σ​Σ′)−1​Σ(\Sigma\Sigma^{\prime})^{-1}\Sigma, providing an intuitive connection with least-squares-type linear mappings.

The next result is inspired by the continuous-time risk-sensitive asset management literature and motivates an interpretation of the optimal asset allocation as a fractional Kelly strategy. For later comparison, we first recall the standard definition of fractional Kelly strategies obtained in continuous-time problems (see in particular Davis and Lleo, [2008](#bib.bib3), [2014](#bib.bib4); Lleo and Runggaldier, [2026a](#bib.bib15)):

###### Proposition 4.2 (Fractional Kelly Strategy (FKS) for Risk-Sensitive Benchmarked Investment Management in Continuous Time - adapted from Proposition 2.10 in (Lleo and Runggaldier, [2026a](#bib.bib15))).

The continuous-time optimal benchmarked investment strategy h∗​(s,Xs),s∈[t,T]h^{\*}(s,X\_{s}),s\in[t,T] consists of an allocation between three funds: hKellyh^{\text{Kelly}}, hBenchh^{\text{Bench}}, and hI​H​Ph^{IHP}.

1. (i)

   The fund hKellyh^{\text{Kelly}} is a Kelly portfolio with factor-dependent allocation

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | hKelly​(Xs):=(Σ​Σ′)−1​(a+A​Xs).\displaystyle h^{\text{Kelly}}(X\_{s}):=\left(\Sigma\Sigma^{\prime}\right)^{-1}\left(a+AX\_{s}\right). |  | (4.7) |
2. (ii)

   The fund hBenchh^{\text{Bench}} is a benchmark-tracking portfolio with constant allocation

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | hBench:=(Σ​Σ′)−1​Σ​Ξ′.\displaystyle h^{\text{Bench}}:=\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\Xi^{\prime}. |  | (4.8) |
3. (iii)

   The fund hI​H​Ph^{IHP} is an Intertemporal Hedging Portfolio (IHP) with factor-dependent allocation

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | hI​H​P​(s,Xs):=(Σ​Σ′)−1​Σ​Λ′​D​uc​(s,Xs),\displaystyle h^{IHP}(s,X\_{s}):=\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\Lambda^{\prime}Du^{\text{c}}(s,X\_{s}), |  | (4.9) |

   where ucu^{\text{c}} is the optimal value function for the continuous-time risk-sensitive benchmarked investment management problem and where (D​uc)′​(s,x)=(∂uc∂x1​(s,x),…,∂uc∂xn​(s,x))(Du^{\text{c}})^{\prime}(s,x)=\left(\frac{\partial u^{\text{c}}}{\partial x\_{1}}(s,x),\ldots,\frac{\partial u^{\text{c}}}{\partial x\_{n}}(s,x)\right).

Moreover, the relative allocation of the funds is constant at f:=1θ+1f:=\frac{1}{\theta+1} for hKellyh^{\text{Kelly}}, 1−f1-f for hBenchh^{\text{Bench}}, and f−1f-1 for hI​H​Ph^{IHP}.

In our setting with continuously-priced stocks and discretely-estimated factors, the optimal asset allocation ([3.53](#S3.E53 "In Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) in Proposition [3.9](#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") can be rewritten as a *rotated and rescaled* fractional Kelly strategy, as shown in the next proposition.

###### Proposition 4.3 (Rotated and Rescaled Fractional Kelly Strategy).

The optimal investment strategy h∗h^{\*} at ([3.53](#S3.E53 "In Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) consists of a rotated and rescaled allocation to the Kelly portfolio hKellyh^{\text{Kelly}} defined at ([4.7](#S4.E7 "In item i ‣ Proposition 4.2 (Fractional Kelly Strategy (FKS) for Risk-Sensitive Benchmarked Investment Management in Continuous Time - adapted from Proposition 2.10 in (Lleo and Runggaldier, 2026a)). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) but here evaluated at discrete time kk, benchmark-tracking portfolio hBenchh^{\text{Bench}} defined at ([4.8](#S4.E8 "In item ii ‣ Proposition 4.2 (Fractional Kelly Strategy (FKS) for Risk-Sensitive Benchmarked Investment Management in Continuous Time - adapted from Proposition 2.10 in (Lleo and Runggaldier, 2026a)). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and a discrete-time intertemporal hedging portfolio hIHPh^{\text{IHP}}, defined as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hkIHP:=\displaystyle h\_{k}^{\text{IHP}}:= | (Σ​Σ′)−1​Σ​Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]\displaystyle\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right] |  | (4.10) |

Moreover, the rotation and rescaling of these portfolios is performed within the optimal investment strategy h∗h^{\*} as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=1θ+1​𝒞k+1−1​(θ)​Σ​Σ′​hkKelly+θθ+1​𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′​hBench−θθ+1​𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′​hkIHP,\displaystyle h^{\*}\_{k}=\frac{1}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\Sigma\Sigma^{\prime}h^{\text{Kelly}}\_{k}+\frac{\theta}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime}h^{\text{Bench}}-\frac{\theta}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime}h^{\text{IHP}}\_{k}, |  | (4.11) |

where 𝒞k+1−1​(θ)​Σ​Σ′\mathcal{C}\_{k+1}^{-1}\!(\theta)\Sigma\Sigma^{\prime} is the rescaling factor for the Kelly portfolio and θθ+1​𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′\frac{\theta}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime} is the rescaling factor for the benchmark-tracking and intertemporal hedging portfolioss.

###### Proof.

We recall the optimal asset allocation given at ([3.53](#S3.E53 "In Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hk∗=\displaystyle h^{\*}\_{k}= | 1θ+1​𝒞k+1−1​(θ)​[(a+A​Xk)+θ​𝒜k+1−1​Σ​{Ξ−Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]}],\displaystyle\frac{1}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\Bigg[(a+AX\_{k})+\theta\mathcal{A}\_{k+1}^{-1}\Sigma\left\{\Xi-\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]\right\}\Bigg], |  | (4.12) |

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkKelly~:=𝒞k+1−1​(θ)​(a+A​Xk),\displaystyle h^{\widetilde{\text{Kelly}}}\_{k}:=\mathcal{C}\_{k+1}^{-1}\!(\theta)(a+AX\_{k}), |  | (4.13) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkBench~:=𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Ξ.\displaystyle h^{\widetilde{\text{Bench}}}\_{k}:=\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Xi. |  | (4.14) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkIHP~:=−𝒞k+1−1(θ)𝒜k+1−1ΣΛ′[Pk+1(bΔt+B~Xk)+pk+1]\displaystyle h^{\widetilde{\text{IHP}}}\_{k}:=-\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right] |  | (4.15) |

With these definitions, we express the optimal asset allocation at ([3.53](#S3.E53 "In Proposition 3.9. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=1θ+1​hkKelly~+θθ+1​hkBench~+θθ+1​hkIHP~.\displaystyle h^{\*}\_{k}=\frac{1}{\theta+1}h^{\widetilde{\text{Kelly}}}\_{k}+\frac{\theta}{\theta+1}h^{\widetilde{\text{Bench}}}\_{k}+\frac{\theta}{\theta+1}h^{\widetilde{\text{IHP}}}\_{k}. |  | (4.16) |

Next, we relate hKelly~h^{\widetilde{\text{Kelly}}}, and hBench~h^{\widetilde{\text{Bench}}}, and hIHP~h^{\widetilde{\text{IHP}}} with the continuous-time Kelly portfolio hKellyh^{\text{Kelly}} defined at ([4.7](#S4.E7 "In item i ‣ Proposition 4.2 (Fractional Kelly Strategy (FKS) for Risk-Sensitive Benchmarked Investment Management in Continuous Time - adapted from Proposition 2.10 in (Lleo and Runggaldier, 2026a)). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), the continuous-time benchmark-tracking portfolio hBenchh^{\text{Bench}} defined at ([4.8](#S4.E8 "In item ii ‣ Proposition 4.2 (Fractional Kelly Strategy (FKS) for Risk-Sensitive Benchmarked Investment Management in Continuous Time - adapted from Proposition 2.10 in (Lleo and Runggaldier, 2026a)). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and the discrete-time intertemporal hedging portfolio hIHPh^{\text{IHP}}, defined at ([4.10](#S4.E10 "In Proposition 4.3 (Rotated and Rescaled Fractional Kelly Strategy). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")).

We start with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkKelly~=𝒞k+1−1​(θ)​(a+A​Xk)=𝒞k+1−1​(θ)​(Σ​Σ′)​(Σ​Σ′)−1​(a+A​Xk)=𝒞k+1−1​(θ)​Σ​Σ′​hkKelly.\displaystyle h^{\widetilde{\text{Kelly}}}\_{k}=\mathcal{C}\_{k+1}^{-1}\!(\theta)(a+AX\_{k})=\mathcal{C}\_{k+1}^{-1}\!(\theta)(\Sigma\Sigma^{\prime})(\Sigma\Sigma^{\prime})^{-1}(a+AX\_{k})=\mathcal{C}\_{k+1}^{-1}\!(\theta)\Sigma\Sigma^{\prime}h^{\text{Kelly}}\_{k}. |  | (4.17) |

Similarly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkBench~=𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Ξ=𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′​hBench\displaystyle h^{\widetilde{\text{Bench}}}\_{k}=\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Xi=\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime}h^{\text{Bench}} |  | (4.18) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkIHP~=−𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Λ′​[Pk+1​(b​Δ​t+B~​Xk)+pk+1]=−𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′​hkIHP.\displaystyle h^{\widetilde{\text{IHP}}}\_{k}=-\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Lambda^{\prime}\left[P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right]=-\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime}h^{\text{IHP}}\_{k}. |  | (4.19) |

Substituting into ([4.16](#S4.E16 "In Proof. ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=1θ+1​𝒞k+1−1​(θ)​Σ​Σ′​hkKelly+θθ+1​𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′​hBench−θθ+1​𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′​hkIHP,\displaystyle h^{\*}\_{k}=\frac{1}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\Sigma\Sigma^{\prime}h^{\text{Kelly}}\_{k}+\frac{\theta}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime}h^{\text{Bench}}-\frac{\theta}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime}h^{\text{IHP}}\_{k}, |  | (4.20) |

which proves the claim.
∎

###### Remark 10.

Note that hBenchh^{\text{Bench}} is constant because Σ\Sigma and Ξ\Xi are both assumed constant. By contrast, hkBench~h^{\widetilde{\text{Bench}}}\_{k} depends on the time index kk via the matrices 𝒞k+1−1​(θ)\mathcal{C}\_{k+1}^{-1}\!(\theta) and 𝒜k+1−1\mathcal{A}\_{k+1}^{-1}.

Therefore, the optimal asset allocation in our model can be interpreted as a fractional Kelly strategy, but with the relative asset allocations of the constituent portfolios—Kelly, benchmark-tracking, and intertemporal hedging—rotated and rescaled by the inverse of the risk-resistance matrix 𝒞k+1−1​(θ)\mathcal{C}\_{k+1}^{-1}\!(\theta), discussed above in Section [4.1](#S4.SS1 "4.1 Interpreting Assumptions 2.1 and 3.6 ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). Geometrically, this inverse transformation shrinks directions associated with higher resistance (larger eigenvalues of 𝒞k+1​(θ)\mathcal{C}\_{k+1}\!(\theta)) and amplifies directions associated with lower resistance.

Specifically, the rotation and rescaling factor for the Kelly portfolio is 1θ+1​𝒞k+1−1​(θ)​Σ​Σ′\frac{1}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\Sigma\Sigma^{\prime}, while that for the other two constituent portfolios is θθ+1​𝒞k+1−1​(θ)​𝒜k+1−1​Σ​Σ′\frac{\theta}{\theta+1}\mathcal{C}\_{k+1}^{-1}\!(\theta)\mathcal{A}\_{k+1}^{-1}\Sigma\Sigma^{\prime}. So the rotation and rescaling for the benchmark-tracking and intertemporal hedging portfolios depend also on the inverse of the matrix 𝒜k+1\mathcal{A}\_{k+1}, discussed above in Section [4.1](#S4.SS1 "4.1 Interpreting Assumptions 2.1 and 3.6 ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning").

For completeness, we also propose a Kelly-like strategy based on the asset allocation in Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"):

###### Proposition 4.4 (Rotated and Rescaled Fractional Kelly Strategy - Part II).

The optimal investment strategy h∗h^{\*} at ([3.42](#S3.E42 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) admits a decomposition into three components: a rotated and rescaled allocation to the Kelly portfolio hKellyh^{\text{Kelly}}, a benchmark-tracking component, and an intertemporal hedging component. It can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=1θ+1​hkKelly~+θθ+1​hkBench~+θθ+1​hkIHP~.\displaystyle h^{\*}\_{k}=\frac{1}{\theta+1}h^{\widetilde{\text{Kelly}}}\_{k}+\frac{\theta}{\theta+1}h^{\widetilde{\text{Bench}}}\_{k}+\frac{\theta}{\theta+1}h^{\widetilde{\text{IHP}}}\_{k}. |  | (4.21) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkKelly~:=(θ+1)​{Im−θ​(Σ​Σ′)−1​Σ​ℬk+1−1​Σ′}​hkKelly,\displaystyle h^{\widetilde{\text{Kelly}}}\_{k}:=(\theta+1)\left\{I\_{m}-\theta\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\right\}h^{\text{Kelly}}\_{k}, |  | (4.22) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkBench~:=(θ+1)​(Σ​Σ′)−1​Σ​ℬk+1−1​Ξ,\displaystyle h^{\widetilde{\text{Bench}}}\_{k}:=(\theta+1)\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Xi, |  | (4.23) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkIHP~:=θ+1θ​(Σ​Σ′)−1​Σ​ℬk+1−1​Λ′​{Pk+1​(b​Δ​t+B~​Xk)+pk+1}\displaystyle h^{\widetilde{\text{IHP}}}\_{k}:=\frac{\theta+1}{\theta}\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Lambda^{\prime}\left\{P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+p\_{k+1}\right\} |  | (4.24) |

###### Proof.

The decomposition follows directly from equations ([3.42](#S3.E42 "In Proposition 3.8. ‣ 3.3 Saddle Point Representation and Optimal Controls for the Penalized Stochastic Game ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), that is,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hk∗=\displaystyle h^{\*}\_{k}= | (Σ​Σ′)−1​{{Im−θ​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1}​(a+A​Xk)+Σ​ℬk+1−1​{Λ′​Pk+1​(b​Δ​t+B~​Xk)+Λ′​pk+1+θ​Ξ}}.\displaystyle\left(\Sigma\Sigma^{\prime}\right)^{-1}\Bigg\{\left\{I\_{m}-\theta\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\right\}(a+AX\_{k})+\Sigma\mathcal{B}\_{k+1}^{-1}\left\{\Lambda^{\prime}P\_{k+1}\left(b\Delta t+\tilde{B}X\_{k}\right)+\Lambda^{\prime}p\_{k+1}+\theta\Xi\right\}\Bigg\}. |  | (4.25) |

Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkKelly~:=(θ+1)​(Σ​Σ′)−1​{Im−θ​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1}​(a+A​Xk),\displaystyle h^{\widetilde{\text{Kelly}}}\_{k}:=(\theta+1)\left(\Sigma\Sigma^{\prime}\right)^{-1}\left\{I\_{m}-\theta\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\right\}(a+AX\_{k}), |  | (4.26) |

hkBench~h^{\widetilde{\text{Bench}}}\_{k} according to ([4.23](#S4.E23 "In Proposition 4.4 (Rotated and Rescaled Fractional Kelly Strategy - Part II). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), and hkIHP~h^{\widetilde{\text{IHP}}}\_{k} according to ([4.24](#S4.E24 "In Proposition 4.4 (Rotated and Rescaled Fractional Kelly Strategy - Part II). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")). With these definitions, we can express the optimal asset allocation as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk∗=1θ+1​hkKelly~+θθ+1​hkBench~+θθ+1​hkIHP~.\displaystyle h^{\*}\_{k}=\frac{1}{\theta+1}h^{\widetilde{\text{Kelly}}}\_{k}+\frac{\theta}{\theta+1}h^{\widetilde{\text{Bench}}}\_{k}+\frac{\theta}{\theta+1}h^{\widetilde{\text{IHP}}}\_{k}. |  | (4.27) |

We proceed as in the proof of Proposition [4.3](#S4.Thmtheorem3 "Proposition 4.3 (Rotated and Rescaled Fractional Kelly Strategy). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and relate hKelly~h^{\widetilde{\text{Kelly}}} with the Kelly portfolio hKellyh^{\text{Kelly}}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkKelly~\displaystyle h^{\widetilde{\text{Kelly}}}\_{k} | =(θ+1)​(Σ​Σ′)−1​{Im−θ​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1}​(a+A​Xk)\displaystyle=(\theta+1)\left(\Sigma\Sigma^{\prime}\right)^{-1}\left\{I\_{m}-\theta\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\right\}(a+AX\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(θ+1)​(Σ​Σ′)−1​{Im−θ​Σ​ℬk+1−1​Σ′​(Σ​Σ′)−1}​(Σ​Σ′)​(Σ​Σ′)−1​(a+A​Xk)\displaystyle=(\theta+1)\left(\Sigma\Sigma^{\prime}\right)^{-1}\left\{I\_{m}-\theta\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\left(\Sigma\Sigma^{\prime}\right)^{-1}\right\}\left(\Sigma\Sigma^{\prime}\right)\left(\Sigma\Sigma^{\prime}\right)^{-1}(a+AX\_{k}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(θ+1)​{Im−θ​(Σ​Σ′)−1​Σ​ℬk+1−1​Σ′}​hkKelly.\displaystyle=(\theta+1)\left\{I\_{m}-\theta\left(\Sigma\Sigma^{\prime}\right)^{-1}\Sigma\mathcal{B}\_{k+1}^{-1}\Sigma^{\prime}\right\}h^{\text{Kelly}}\_{k}. |  | (4.28) |

This proves the decomposition and the representation ([4.22](#S4.E22 "In Proposition 4.4 (Rotated and Rescaled Fractional Kelly Strategy - Part II). ‣ 4.3 Optimal Investment Strategies as Kelly Strategies ‣ 4 Interpreting the Risk-Sensitive Investment Management Model ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) of the rotated and rescaled Kelly component.
∎

## 5 Numerical Solution via Reinforcement Learning

So far, we have implicitly assumed that the market model introduced in Section [2](#S2 "2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") is an exact representation of financial markets and that all its parameters can be estimated with high accuracy. When these assumptions hold, we can use the recursions in Theorem [3.11](#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.4 Main Result ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") to numerically solve the risk-sensitive benchmarked investment management problem. However, in reality, estimating the parameters with sufficient accuracy is extremely difficult. The parameters determining expected returns are a typical example. Accordingly, the main purpose of the market model constructed in Sections [2](#S2 "2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") and [3](#S3 "3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning") is to capture the essential features of financial markets, to characterize their fundamental relations, and to provide a functional form for the policies and value functions.

We can then use these insights to engineer a reinforcement learning (RL) method that will learn the investment strategy and, possibly, the value function, directly through interactions with the market. One major class of RL techniques is based on policy gradient methods, which start from parametrized families of controls and value functions, where the parameters have to be learned through interaction with the market. On the other hand, for the given model structure in Section [2](#S2 "2 Setting Up the Risk-Sensitive Benchmarked Asset Management Problem ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"), and assuming that the model parameters are known, we derived explicit expressions for the value functions and the control policies in Section [3](#S3 "3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). This gives us an indication of how to choose parametrized expressions for the value functions and controls with parameters that have to be learned from observing the market. To learn these parameters, we shall apply policy gradient methods. These parametrized expressions are actually approximations to the actual expressions for the value function and controls, and a great deal of the literature is devoted to studying their convergence. In the present section, we discuss how to implement policy gradient methods to solve our investment problem numerically when only the model structure, but not the parameters, is assumed to be known.

Policy gradient methods have gained popularity in recent years following groundbreaking advances in the field of reinforcement learning and a series of successful applications, most notably to Go. We refer the reader to Chapter 13 in the classic text by Sutton and Barto ([2018](#bib.bib21)). All policy gradient methods follow the same essential steps. First, approximate the policy using a conveniently parametrized function. Second, compute the gradient of a given performance measure, usually a value function, with respect to the parameters of the function approximating the controls. Third, update the parameters by performing a gradient descent update if the aim is to minimize the performance measure, or a gradient ascent update if the aim is to maximize the performance measure.

In this section, we use the typewriter font for the learnable parameter matrices and vectors
𝙳,𝚍,𝙴,𝚎,𝙵,𝚏\mathtt{D},\mathtt{d},\mathtt{E},\mathtt{e},\mathtt{F},\mathtt{f}, and we use ϕk\phi\_{k} and 𝚽\boldsymbol{\Phi} to denote parameter blocks and their horizon-wise collection.

### 5.1 Simple Policy Gradient Approach

A natural approach to implementing a policy gradient method in our context is to extend the approach by Hambly et al. ([2021](#bib.bib6), [2023b](#bib.bib8)). Their work on policy gradient methods for linear quadratic regulators and linear-quadratic games captures the essential features of LQG control problems and games, namely the quadratic cost in the state and controls, and the linear dynamics of the state variable. It also provides strong convergence results. However, this work ignores some features that are important for financial applications, such as the interaction between the state and control in the cost function, first-order terms in the cost function, and the possibility of a mean reversion to a long-term mean different from 0 for the state. Hence, further work is necessary.

#### 5.1.1 Application to the LQG Game

In the general case θ>0\theta>0, we derived an LQG game under an auxiliary measure and showed that its optimal controls are affine in the state, and that the value function is quadratic. We can therefore use the following parametrization666Note that this is a full parametrization. We could use the fact that η∗=0\eta^{\*}=0 to substantially simplify the mathematical exposition and reduce the amount of numerical work.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk=𝙳k​Xk+𝚍kγ¯k=𝙴k​Xk+𝚎kη¯k=𝙵k​Xk+𝚏k\displaystyle h\_{k}=\mathtt{D}\_{k}X\_{k}+\mathtt{d}\_{k}\qquad\bar{\gamma}\_{k}=\mathtt{E}\_{k}X\_{k}+\mathtt{e}\_{k}\qquad\bar{\eta}\_{k}=\mathtt{F}\_{k}X\_{k}+\mathtt{f}\_{k} |  | (5.1) |

for k=0,…,K−1k=0,\ldots,K-1, where 𝙳k∈ℝm×n\mathtt{D}\_{k}\in\mathbb{R}^{m\times n}, 𝚍k∈ℝm\mathtt{d}\_{k}\in\mathbb{R}^{m}, 𝙴k∈ℝd×n\mathtt{E}\_{k}\in\mathbb{R}^{d\times n}, 𝚎k∈ℝd\mathtt{e}\_{k}\in\mathbb{R}^{d}, 𝙵k∈ℝm×n\mathtt{F}\_{k}\in\mathbb{R}^{m\times n}, 𝚏k∈ℝm\mathtt{f}\_{k}\in\mathbb{R}^{m}. Let ϕk:=(𝙳k,𝚍k,𝙴k,𝚎k,𝙵k,𝚏k)\phi\_{k}:=\left(\mathtt{D}\_{k},\mathtt{d}\_{k},\mathtt{E}\_{k},\mathtt{e}\_{k},\mathtt{F}\_{k},\mathtt{f}\_{k}\right). Further define 𝐃:=(𝙳0,…,𝙳K−1)\mathtt{\mathbf{D}}:=\left(\mathtt{D}\_{0},\ldots,\mathtt{D}\_{K-1}\right) with similar definitions for 𝐝,𝐄,𝐞,𝐅,𝐟\mathtt{\mathbf{d}},\mathtt{\mathbf{E}},\mathtt{\mathbf{e}},\mathtt{\mathbf{F}},\mathtt{\mathbf{f}}, and let 𝚽=(𝐃,𝐝,𝐄,𝐞,𝐅,𝐟)\boldsymbol{\Phi}=\left(\mathtt{\mathbf{D}},\mathtt{\mathbf{d}},\mathtt{\mathbf{E}},\mathtt{\mathbf{e}},\mathtt{\mathbf{F}},\mathtt{\mathbf{f}}\right).

Based on ([3.2](#S3.Ex20 "3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and ([3.24](#S3.E24 "In 3.2 Free Energy-Entropy Duality for the Randomized Risk-Sensitive Investment Management Problem ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), the objective function CC, as a function of the policy parameters, is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | C​(𝙳,𝚍,𝙴,𝚎,𝙵,𝚏)\displaystyle C(\mathtt{D},\mathtt{d},\mathtt{E},\mathtt{e},\mathtt{F},\mathtt{f}) |  | (5.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝐄γ¯,η¯​[θ​∑k=0K−1g​(𝙳,𝚍,𝙴,𝚎,𝙵,𝚏;Xk)​Δ​t]\displaystyle\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[\theta\sum\_{k=0}^{K-1}g(\mathtt{D},\mathtt{d},\mathtt{E},\mathtt{e},\mathtt{F},\mathtt{f};X\_{k})\Delta t\Bigg] |  | (5.3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝐄γ¯,η¯[−θ(RT(𝙳,𝚍,𝙴,𝚎;X0:K−1)−R0)−12∑k=0K−1{(𝙴kXk+𝚎k)′(𝙴kXk+𝚎k)Δt\displaystyle\mathbf{E}^{\bar{\gamma},\bar{\eta}}\Bigg[-\theta\left(R\_{T}(\mathtt{D},\mathtt{d},\mathtt{E},\mathtt{e};X\_{0:K-1})-R\_{0}\right)-\frac{1}{2}\sum\_{k=0}^{K-1}\left\{\left(\mathtt{E}\_{k}X\_{k}+\mathtt{e}\_{k}\right)^{\prime}\left(\mathtt{E}\_{k}X\_{k}+\mathtt{e}\_{k}\right)\Delta t\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(𝙵kXk+𝚏k)′Ξk−1(𝙵kXk+𝚏k)}],\displaystyle\left.+\left(\mathtt{F}\_{k}X\_{k}+\mathtt{f}\_{k}\right)^{\prime}\Xi\_{k}^{-1}\left(\mathtt{F}\_{k}X\_{k}+\mathtt{f}\_{k}\right)\right\}\Bigg], |  | (5.4) |

which we also denote more succinctly as C​(𝚽)C(\boldsymbol{\Phi}) when we do not need to identify each parameter. With this notation, Hambly et al.’s so-called *Natural Policy Gradient* (extended to include a zeroth-order term) for a sequence of episodes ℓ=1,…,M\ell=1,\ldots,M produces the following *online* update:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕk(ℓ+1)=ϕk(ℓ)±δℓ​∇^ϕk​C​(𝚽(ℓ))​(Λ^k(ℓ))−1,\displaystyle\phi^{(\ell+1)}\_{k}=\phi^{(\ell)}\_{k}\pm\delta\_{\ell}\,\widehat{\nabla}\_{\phi\_{k}}C\!\left(\boldsymbol{\Phi}^{(\ell)}\right)\,\left(\widehat{\Lambda}^{(\ell)}\_{k}\right)^{-1}, |  | (5.5) |

for k=0,1,…,K−1k=0,1,\ldots,K-1 and where δℓ\delta\_{\ell} is the step size. In the case of unknown model parameters, ∇^ϕk​C\widehat{\nabla}\_{\phi\_{k}}C\! denotes the empirical policy gradient of CC with respect to the parameter block ϕk\phi\_{k}, and Λ^k(ℓ)\widehat{\Lambda}^{(\ell)}\_{k} is an empirical estimate for the state covariance matrix Λk:=𝐄​[Xk​Xk′]\Lambda\_{k}:=\mathbf{E}\left[X\_{k}X\_{k}^{\prime}\right] at time kk. Here, the preconditioning by (Λ^k(ℓ))−1(\widehat{\Lambda}^{(\ell)}\_{k})^{-1} is understood blockwise on the coefficients multiplying XkX\_{k}; for the zeroth-order terms, the corresponding natural-gradient scaling is defined analogously (equivalently, by augmenting the state with a constant feature).

The update sign ±\pm is understood componentwise by parameter block. It is negative (descent) for the minimizing controller parameters (𝙳,𝚍)(\mathtt{D},\mathtt{d}) and positive (ascent) for the adversarial parameters (𝙴,𝚎,𝙵,𝚏)(\mathtt{E},\mathtt{e},\mathtt{F},\mathtt{f}). Thus, the learning problem is a finite-dimensional saddle-point problem in the policy parameters, with minimization over (𝙳,𝚍)(\mathtt{D},\mathtt{d}) and maximization over (𝙴,𝚎,𝙵,𝚏)(\mathtt{E},\mathtt{e},\mathtt{F},\mathtt{f}).

#### 5.1.2 Application to the Kelly Portfolio

When θ→0\theta\to 0, we obtain the Kelly portfolio, as discussed in Section [3.5](#S3.SS5 "3.5 Limiting Case: The Kelly Criterion ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning"). Here, the implementation is simpler than in the general case for three reasons. First, the problem is set under the initial measure ℙ\mathbb{P}. Second, the problem is a standard LQG control problem, not a game. Third, the optimal control does not depend on the parameters of the value function.

As was the case for the LQG game, the optimal control is affine in the state. We can therefore use the following affine parametrization to set up the policy gradient method:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hkKelly=𝙳kKelly​Xk+𝚍kKelly\displaystyle h^{\text{Kelly}}\_{k}=\mathtt{D}^{\text{Kelly}}\_{k}X\_{k}+\mathtt{d}^{\text{Kelly}}\_{k} |  | (5.6) |

for k=0,…,K−1k=0,\ldots,K-1, where 𝙳kKelly∈ℝm×n\mathtt{D}^{\text{Kelly}}\_{k}\in\mathbb{R}^{m\times n}, 𝚍kKelly∈ℝm\mathtt{d}^{\text{Kelly}}\_{k}\in\mathbb{R}^{m}, and ϕkKelly:=(𝙳kKelly,𝚍kKelly)\phi^{\text{Kelly}}\_{k}:=\left(\mathtt{D}^{\text{Kelly}}\_{k},\mathtt{d}^{\text{Kelly}}\_{k}\right). As earlier, we define 𝐃Kelly:=(𝙳0Kelly,…,𝙳K−1Kelly)\mathtt{\mathbf{D}}^{\text{Kelly}}:=\left(\mathtt{D}^{\text{Kelly}}\_{0},\ldots,\mathtt{D}^{\text{Kelly}}\_{K-1}\right) with similar definitions for 𝐝\mathtt{\mathbf{d}}, and we let 𝚽Kelly=(𝐃Kelly,𝐝Kelly)\boldsymbol{\Phi}^{\text{Kelly}}=\left(\mathtt{\mathbf{D}}^{\text{Kelly}},\mathtt{\mathbf{d}}^{\text{Kelly}}\right).

Based on ([3.84](#S3.E84 "In 3.5 Limiting Case: The Kelly Criterion ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")) and ([3.5](#S3.Ex121 "3.5 Limiting Case: The Kelly Criterion ‣ 3 Solution Via The Free Energy-Entropy Duality ‣ Exploratory Randomization for Discrete-Time Risk-Sensitive Benchmarked Investment Management with Reinforcement Learning")), the objective function CC, as a function of the policy parameters, is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | CKelly​(𝙳Kelly,𝚍Kelly)\displaystyle C^{\text{Kelly}}(\mathtt{D}^{\text{Kelly}},\mathtt{d}^{\text{Kelly}}) |  | (5.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝐄​[∑k=0K−1gKelly​(𝙳Kelly,𝚍Kelly;Xk)​Δ​t]\displaystyle\mathbf{E}\Bigg[\sum\_{k=0}^{K-1}g^{\text{Kelly}}(\mathtt{D}^{\text{Kelly}},\mathtt{d}^{\text{Kelly}};X\_{k})\Delta t\Bigg] |  | (5.8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝐄​[(RT​(𝙳Kelly,𝚍Kelly;X0:K−1)−R0)]\displaystyle\mathbf{E}\left[\left(R\_{T}(\mathtt{D}^{\text{Kelly}},\mathtt{d}^{\text{Kelly}};X\_{0:K-1})-R\_{0}\right)\right] |  | (5.9) |

Then Hambly et al.’s so-called *Natural Policy Gradient* updating rule (extended here as well to include a zeroth-order term) for a sequence of episodes ℓ=1,…,M\ell=1,\ldots,M is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕkKelly,(ℓ+1)=ϕkKelly,(ℓ)+δℓ​∇^ϕk​CKelly​(𝚽Kelly,(ℓ))​(Λ^k(ℓ))−1,\displaystyle\phi\_{k}^{\text{Kelly},(\ell+1)}=\phi\_{k}^{\text{Kelly},(\ell)}+\delta\_{\ell}\,\widehat{\nabla}\_{\phi\_{k}}C^{\text{Kelly}}\!\left(\boldsymbol{\Phi}^{\text{Kelly},(\ell)}\right)\,\left(\widehat{\Lambda}^{(\ell)}\_{k}\right)^{-1}, |  | (5.10) |

for k=0,1,…,K−1k=0,1,\ldots,K-1. Here again, the preconditioning by (Λ^k(ℓ))−1(\widehat{\Lambda}^{(\ell)}\_{k})^{-1} is understood blockwise on the coefficients multiplying XkX\_{k}; for the zeroth-order term, the corresponding natural-gradient scaling is defined analogously (equivalently, by augmenting the state with a constant feature). This is a gradient-ascent update for the maximizing controller parameters (𝙳Kelly,𝚍Kelly)(\mathtt{D}^{\text{Kelly}},\mathtt{d}^{\text{Kelly}}).

### 5.2 From Policy Gradient to Actor-Critic

Actor-critic methods build on this approach to update both the policy and the value function. The *actor* performs the three policy gradient steps to update the parameters of the policy, at the current estimate for the value function, while the *critic* performs three similar steps to update the parameters of the value function, at the current estimate for the policy.

In the general case of the LQG game, we take the critic as

|  |  |  |  |
| --- | --- | --- | --- |
|  | uk​(Xk)=12​Xk′​𝙿k​Xk+Xk′​𝚙k+𝚛k,\displaystyle u\_{k}(X\_{k})=\frac{1}{2}X\_{k}^{\prime}\mathtt{P}\_{k}X\_{k}+X\_{k}^{\prime}\mathtt{p}\_{k}+\mathtt{r}\_{k}, |  | (5.11) |

where 𝙿k∈ℝn×n,𝚙k∈ℝn\mathtt{P}\_{k}\in\mathbb{R}^{n\times n},\mathtt{p}\_{k}\in\mathbb{R}^{n}, and 𝚛k∈ℝ\mathtt{r}\_{k}\in\mathbb{R}.

The critic parameters (𝙿k,𝚙k,𝚛k)(\mathtt{P}\_{k},\mathtt{p}\_{k},\mathtt{r}\_{k}) are updated on a faster timescale by *temporal-difference* methods. The key here is to establish that the joint gradient updates will converge to the optimal controls and the optimal value function.

Finally, we note that global convergence results exist for policy-gradient methods for LQR problems— see (Fazel et al., [2018](#bib.bib5); Hambly et al., [2021](#bib.bib6)) for control problems and Hambly et al. ([2023b](#bib.bib8)) for linear-quadratic games. On the actor-critic front, Alacaoglu et al. ([2022](#bib.bib1)) obtained promising results for two-player Markov games.

In the special case of the Kelly portfolio, the policy does not depend on the value function. Hence, adding a critic does not improve the speed or accuracy of the policy estimation. Therefore, a critic only needs to be included if an estimate of the value function is of independent interest to the investor.

## 6 Conclusions

We have considered a risk-sensitive benchmarked asset management problem in the form of a non-standard LEQG problem. The problem falls outside the classic LEQG template because the state process is uncontrolled, and the noise appears linearly within an exponential. The assets and the benchmark are modeled as continuous-time processes, but portfolio rebalancing occurs at a fixed discrete time schedule, leading to a discrete-time stochastic control problem. Furthermore, the dynamics of the assets and the benchmark are affected by a factor process that can be observed at the discrete rebalancing times. In this discrete-time setup, it was rather straightforward to introduce randomized controls for exploration.

We applied the free energy-entropy duality to connect the risk-sensitive control problem, set with respect to an initial measure, to a risk-neutral randomized stochastic game, defined with respect to a transformed measure. This approach automatically implies a penalization in the risk-neutral problem. The penalization is given by the relative entropy of the transformed measure with respect to the original one. This connection also offers a theoretical justification for penalizing the randomization of controls, which has appeared more ad hoc in the literature.

We have solved the resulting risk-neutral penalized stochastic game, assuming the model coefficients are known. We show that, as functions of the observable factors, the optimal controls are linear and the optimal value function is quadratic. We also considered the limiting case in which the risk-sensitivity parameter tends to zero. This leads to a Kelly portfolio. We have shown that the optimal asset allocation can be rewritten as a rescaled fractional Kelly strategy. We also discussed various implications of the assumptions underlying our results.

For the case where the model parameters are not known, we discussed how to adapt our approach using known Reinforcement Learning methods. In particular, we focused on policy gradient and actor-critic methods. The structure we obtained for the optimal strategies and value, with their linear and quadratic dependence on the factors, indicates the parametrization to use for the controls and the value function. This supports applying policy gradient and actor-critic methods to learn the parameters from market observations.

One fundamental study in risk-sensitive stochastic control appears in the paper by Kuroda and Nagai ([2002](#bib.bib13)). The authors use a change of measure to transform a non-standard discrete-time risk-sensitive LEQG problem, like ours, into a standard discrete-time LEQG problem. This transformation may lead to an alternative two-step approach to our problem. First, the Kuroda-Nagai methodology transforms the non-standard LEQG problem into a standard one. Second, applying the free energy-entropy duality reduces the problem to an equivalent LQG problem. Such a two-step approach has been studied in detail by Lleo and Runggaldier ([2026a](#bib.bib15)), which is formulated entirely in continuous time and does not consider randomized controls from the outset. It is shown there that a one-step approach, as used here, yields the same results as the two-step approach. We could apply a two-step approach to the present setup, following another of our papers, Lleo and Runggaldier ([2026b](#bib.bib16)), but omit it to avoid overburdening this paper.

## References

* Alacaoglu et al. (2022)

  Ahmet Alacaoglu, Luca Viano, Niao He, and Volkan Cevher.
  A Natural Actor-Critic Framework for Zero-Sum Markov Games.
  In *Proceedings of the 39th International Conference on Machine Learning*, pages 307–366. PMLR, June 2022.
* Dai Pra et al. (1996)

  Paolo Dai Pra, Lorenzo Meneghini, and Wolfgang J. Runggaldier.
  Connections between stochastic control and dynamic games.
  *Mathematics of Control, Signals and Systems*, 9(4):303–326, December 1996.
* Davis and Lleo (2008)

  M.H.A. Davis and S. Lleo.
  Risk-sensitive benchmarked asset management.
  *Quantitative Finance*, 8(4):415–426, June 2008.
* Davis and Lleo (2014)

  M.H.A. Davis and S. Lleo.
  *Risk-Sensitive Investment Management*, volume 19 of *Advanced Series on Statistical Science and Applied Probability*.
  World Scientific Publishing, 2014.
* Fazel et al. (2018)

  Maryam Fazel, Rong Ge, Sham Kakade, and Mehran Mesbahi.
  Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator.
  In *Proceedings of the 35th International Conference on Machine Learning*, pages 1467–1476. PMLR, July 2018.
* Hambly et al. (2021)

  Ben Hambly, Renyuan Xu, and Huining Yang.
  Policy Gradient Methods for the Noisy Linear Quadratic Regulator over a Finite Horizon.
  *SIAM Journal on Control and Optimization*, 59(5):3359–3391, January 2021.
* Hambly et al. (2023a)

  Ben Hambly, Renyuan Xu, and Huining Yang.
  Recent advances in reinforcement learning in finance.
  *Mathematical Finance*, 33(3):437–503, 2023a.
* Hambly et al. (2023b)

  Ben M. Hambly, Renyuan Xu, and Huining Yang.
  Policy Gradient Methods Find the Nash Equilibrium in N-player General-sum Linear-quadratic Games.
  *Journal of Machine Learning Research*, 24(139):1–56, 2023b.
* Jia (2024)

  Yanwei Jia.
  Continuous-time Risk-sensitive Reinforcement Learning via Quadratic Variation Penalty, April 2024.
  URL <http://arxiv.org/abs/2404.12598>.
  arXiv:2404.12598 [cs].
* Jia and Zhou (2022a)

  Yanwei Jia and Xun Yu Zhou.
  q-Learning in Continuous Time, 2022a.
* Jia and Zhou (2022b)

  Yanwei Jia and Xunyu Zhou.
  Policy Evaluation and Temporal-Difference Learning in Continuous Time and Space: A Martingale Approach.
  *Journal of Machine Learning Research*, 23(154):1–55, 2022b.
* Jia and Zhou (2022c)

  Yanwei Jia and Xunyu Zhou.
  Policy Gradient and Actor–Critic Learning in Continuous Time and Space: Theory and Algorithms.
  *Journal of Machine Learning Research*, 23(275):1–50, 2022c.
* Kuroda and Nagai (2002)

  K. Kuroda and H. Nagai.
  Risk-sensitive portfolio optimization on infinite time horizon.
  *Stochastics and Stochastics Reports*, 73:309–331, 2002.
* Lleo and Runggaldier (2024)

  S. Lleo and W.J. Runggaldier.
  On the separation of estimation and control in risk-sensitive investment problems under incomplete observation.
  *European Journal of Operational Research*, 316(1):200–214, July 2024.
* Lleo and Runggaldier (2026a)

  S. Lleo and W.J. Runggaldier.
  The role of entropy regularization in linking reinforcement learning and risk-sensitive investment management.
  Preprint, 2026a.
* Lleo and Runggaldier (2026b)

  S. Lleo and W.J. Runggaldier.
  Exploratory randomization for discrete-time linear exponential quadratic gaussian (LEQG) problem.
  *Pure and Applied Functional Analysis*, (forthcoming), 2026b.
* Lleo and MacLean (2025)

  Sébastien Lleo and Leonard C. MacLean.
  Dual dominance: how Harry Markowitz and William Ziemba impacted portfolio management.
  *Annals of Operations Research*, 346(1):181–216, March 2025.
* Meneghini (1994)

  L. Meneghini.
  *Modelli Risolvibili per Problemi di Controllo di Sistemi Dinamici Imprecisi Multivariati*.
  PhD thesis, Università Degli Studi Di Padova, 1994.
* Shaiju and Petersen (2008)

  A. Shaiju and I. Petersen.
  Formulas for discrete time LQR, LQG, LEQG and minimax LQG optimal control problems.
  In *Proceedings of the 17th World Congress*, pages 8773–8778. The International Federation of Automatic Control, 2008.
* Stettner (1999)

  Lukasz Stettner.
  Risk sensitive portfolio optimization.
  *Mathematical Methods of Operations Research*, 50(3):463–474, December 1999.
* Sutton and Barto (2018)

  R.S. Sutton and A.G. Barto.
  *Reinforcement Learning, second edition: An Introduction*.
  Adaptive Computation and Machine Learning series. Bradford Books, 2 edition, 2018.
* Wang and Zhou (2020)

  Haoran Wang and Xun Yu Zhou.
  Continuous‐time mean–variance portfolio selection: A reinforcement learning framework.
  *Mathematical Finance*, 30(4):1273–1308, October 2020.
* Wang et al. (2020)

  Haoran Wang, Thaleia Zariphopoulou, and Xun Yu Zhou.
  Reinforcement Learning in Continuous Time and Space: A Stochastic Control Approach.
  *Journal of Machine Learning Research*, 21(198):1–34, 2020.
* Whittle (1990)

  P. Whittle.
  *Risk Sensitive Optimal Control*.
  John Wiley and Sons, New York, 1990.

BETA