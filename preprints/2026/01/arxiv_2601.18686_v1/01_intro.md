---
authors:
- Stefano Corti
- Roberto Daluiso
- Andrea Pallavicini
doc_id: arxiv:2601.18686v1
family_id: arxiv:2601.18686
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote
  1The authors report no potential competing interests. The opinions expressed in
  this document are solely those of the authors and do not represent in any way those
  of their present and past employers.
url_abs: http://arxiv.org/abs/2601.18686v1
url_html: https://arxiv.org/html/2601.18686v1
venue: arXiv q-fin
version: 1
year: 2026
---


S. Corti,
R. Daluiso,
A. Pallavicini
Politecnico di Milano, Department of Mathematics. Address: Piazza Leonardo da Vinci 32, Milano 20133, Italy. Email address: stefano7.corti@mail.polimi.it.Intesa Sanpaolo, Financial Engineering. Address: largo Mattioli 3, Milano 20121, Italy. Email address: roberto.daluiso@intesasanpaolo.com.Intesa Sanpaolo, Financial Engineering. Address: largo Mattioli 3, Milano 20121, Italy. Email address: andrea.pallavicini@intesasanpaolo.com.

(
First Version: December 9, 2025. This version: January 26, 2026)

###### Abstract

In recent decades, companies have frequently adopted share repurchase programs to return capital to shareholders or for other strategic purposes, instructing investment banks to rapidly buy back shares on their behalf. When the executing institution is allowed to hedge its exposure, it encounters several challenges due to the intrinsic features of the product. Moreover, contractual clauses or market regulations on trading activity may make it infeasible to rely on Greeks. In this work, we address the hedging of these products by developing a machine-learning framework that determines the optimal execution of the buyback while explicitly accounting for the bank’s actual trading capabilities. This unified treatment of execution and hedging yields substantial performance improvements, resulting in an optimized policy that provides a feasible and realistic hedging approach. The pricing of these programs can be framed in terms of the discount that banks offer to the client on the price at which the shares are delivered. Since, in our framework, risk measures serve as objective functions, we exploit the concept of indifference pricing to compute this discount, thereby capturing the actual execution performance.

JEL classification codes: C63, G13.
  
AMS classification codes: 65C05, 91G20, 91G60.
  
Keywords: Repurchase programs, deep hedging, hedging, machine learning, neural networks

## 1 Introduction

Payout policies play a significant role in corporate finance literature. Generally, to return capital to their shareholders, companies can use either dividends or share repurchases. Modigliani–Miller [[17](https://arxiv.org/html/2601.18686v1#bib.bib3 "Dividend policy, growth, and the valuation of shares")] theorem states that the two approaches are equivalent in the absence of taxes, market friction, and information asymmetry. However, in practical settings [[1](https://arxiv.org/html/2601.18686v1#bib.bib4 "Payout policy"), [7](https://arxiv.org/html/2601.18686v1#bib.bib5 "Payout policy")], share repurchases are sometimes preferred for strategic reasons, such as tax considerations or to adjust the firm’s capital structure. Furthermore, these programs can signal stock undervaluation and deter takeovers.

Briefly, under these contracts, the company agrees with an investment bank on a predetermined volume of shares to buy within a specified maturity date and on a benchmark price. The bank is responsible for the market operations and earns the difference between the benchmark price, typically an average of prices measured on the repurchase days, often offered at a discount, and the average execution price. The program is usually divided into two phases, the second of which begins when the financial institution is granted the right to suspend trading, leading to the final settlement. The speed with which repurchases are carried out has earned them the name Accelerated Share Repurchases, or ASR.

From an operational point of view, the bank determines daily how many shares to repurchase and when to exercise the termination right. In the literature [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring"), [12](https://arxiv.org/html/2601.18686v1#bib.bib12 "Accelerated share repurchase: pricing and execution strategy"), [13](https://arxiv.org/html/2601.18686v1#bib.bib13 "Optimal execution of accelerated share repurchase contracts with fixed notional")], the entire process is framed as a control problem, since profit maximization requires the executor to behave according to an optimal policy. The framework is characterized by a high-dimensional state space, as the path-dependent payoff makes day-by-day decisions dependent on the underlying asset value and on the variables that determine the final reward, namely the cumulative quantity of shares traded, the total expenditure, and the price process of the benchmark.

From the bank’s perspective, the dependence of the cash flow at the termination date on the equity price creates an exposure to the underlying asset. In some ASR contracts, the financial institution is allowed to hedge its position, a task that proves highly complex due to the barrier-like features embedded in the product. For instance, the payoff structure may suggest a strategy based on sudden switches between extreme repurchase regimes: it may be optimal to buy larger quantities on the market when the value of the underlying falls below its average price while buying the minimum admissible quantity in the opposite scenario. These discontinuities, sometimes also caused by the policy that defines contract termination, make ASR a barrier-type product. Consequently, its Greeks show highly volatile dynamics, with frequent changes in sign and large values in absolute terms, and their computation may be affected by numerical instability. Relying on such highly variable signals can lead to abrupt adjustments in the hedging portfolio, resulting in significant transaction costs due to bid–ask spreads and substantial replication errors when rebalancing is performed at discrete dates.

Furthermore, trading constraints introduce additional limitations to the use of Greeks. While some clauses apply solely to the buyback activity, others simultaneously affect both the units of the underlying asset delivered to the client and those used for risk management, as they limit the total number of shares that can be purchased daily to a percentage of the market volume. As a result, the position suggested by the Greeks, computed ex post, may be infeasible whenever total trading exceeds this threshold. Therefore, the optimal policy should incorporate the agent’s effective operational capacity, which requires embedding the hedging activity directly into the control problem and thereby making it interdependent with the execution of the program.

This work focuses on the full management of share repurchase programs. In particular, we investigate whether a unified framework for handling ASR contracts and their associated hedging can yield meaningful performance improvements in real terms. Moreover, modeling an agent that jointly determines how to manage the contract and how to hedge the resulting position enables the implementation and optimization of policies that explicitly account for actual market constraints. By incorporating trading capacity directly into the control problem, the resulting strategy offers a more feasible and realistic approach to managing the bank’s exposure.

We adopt machine learning techniques, which are naturally suited to handling high-dimensional problems and numerous constraints that often challenge traditional methods. Following an approach similar to [[3](https://arxiv.org/html/2601.18686v1#bib.bib10 "Pricing and managing complex share buy-back contracts: an alternative to optimal control")], we define several classes of strategies characterized by a set of parameters, so that determining the optimal behavior reduces to searching for the optimal parameter vector. Specifically, we delegate both the design of repurchase and hedging policies to neural networks, leveraging their computational capabilities and flexibility, which allows us to feed the state-space variables directly into the control function. In this direction, we build on the work of O. Guéant, I. Manziuk, and J. Pu [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring")], who apply neural networks to ASR programs, and on that of H. Buehler, L. Gonon, J. Teichmann, and B. Wood [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], who exploit them to hedge derivative portfolios.

In a machine learning framework, the optimization procedure relies on the specification of a loss function. In our setting, this role is played by risk measures [[8](https://arxiv.org/html/2601.18686v1#bib.bib14 "Convex measures of risk and trading constraints")], as they provide a natural way to assess the performance of policies. Furthermore, they allow us to incorporate the concept of indifference pricing [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], offering a meaningful alternative to the price obtained using the traditional risk-neutral valuation formula. The latter loses relevance in this context, as it relies on the ability to construct and follow a replicating portfolio defined through the Greeks, an approach that, as previously discussed, is often infeasible due to operational constraints or high transaction costs.

In our analysis, we require the payoff to depend differentiably on the networks’ outputs in order to leverage classical back-propagation algorithms. We adopt the same approach as in [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring")], where the authors introduce a relaxation of the optimal stopping problem by replacing the concept of optimal stopping time with a probabilistic representation. This transforms the exercise decision from discrete to continuous, enabling gradient-based optimization.

From a mathematical perspective, share repurchase programs have been already examined in the literature. In [[15](https://arxiv.org/html/2601.18686v1#bib.bib32 "Optimal accelerated share repurchases")], the authors analyze an ASR contract with a fixed number of shares in a continuous-time model with a quadratic running penalty on remaining shares. The optimal execution policy is reduced to a partial differential equation, which is then solved numerically. Moreover, by considering the ratio between the underlying price and its running average since the inception of the contract, they succeed in reducing the dimensionality of the equation from five to three. A different approach is taken in [[12](https://arxiv.org/html/2601.18686v1#bib.bib12 "Accelerated share repurchase: pricing and execution strategy")], where the optimal execution problem is studied in discrete time by a risk-averse agent within an expected-utility framework. Starting from the Bellman equation, the authors develop a pentanomial tree to determine the optimal strategy. A similar methodology is employed in [[13](https://arxiv.org/html/2601.18686v1#bib.bib13 "Optimal execution of accelerated share repurchase contracts with fixed notional")] for fixed-notional ASR contracts. Finally, as mentioned above, neural network based methods have also been explored for managing these products in [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring")].

The hedging technique based on deep neural networks presented in [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], and usually referred to as "deep hedging", provides the complete theoretical framework for applying machine learning, specifically neural networks, to the hedging problem, relying on the concept of convex risk measures. This approach has been further developed in many directions. For instance, it has been extended beyond traditional delta hedging to manage higher-order risks and implied volatility dynamics. Some examples are [[14](https://arxiv.org/html/2601.18686v1#bib.bib22 "Relationship between deep hedging and delta hedging: leveraging a statistical arbitrage strategy")], comparing deep hedging with risk-neutral delta hedging, [[10](https://arxiv.org/html/2601.18686v1#bib.bib23 "Deep hedging with options using the implied volatility surface")], which applies deep hedging using the implied volatility surface for gamma hedging, [[2](https://arxiv.org/html/2601.18686v1#bib.bib24 "Deep gamma hedging")], focusing specifically on deep gamma hedging, and [[6](https://arxiv.org/html/2601.18686v1#bib.bib25 "Gamma and vega hedging using deep distributional reinforcement learning")], which employs deep distributional reinforcement learning to hedge both gamma and vega effectively.

To our knowledge, deep hedging has only been applied to the hedging of traditional derivative portfolios, obtaining satisfactory results; for example, in [[16](https://arxiv.org/html/2601.18686v1#bib.bib8 "Empirical deep hedging")] the authors deal with options using intra-day data from actual markets, while [[18](https://arxiv.org/html/2601.18686v1#bib.bib17 "Deep hedging bermudan swaptions")] deals with Bermudan swaptions and [[19](https://arxiv.org/html/2601.18686v1#bib.bib16 "Hedging american put options with deep reinforcement learning")] with American put options. We are motivated by the question of whether this technique can be successfully applied to a more complex derivative-like product. If this proves to be the case, then it is straightforward to unify the repurchase strategy and its hedging into a joint optimization framework. As explained above, this would enable a complete workflow to determine optimal behavior, including both market risk protection and contractual constraints.

We conclude by outlining the structure of the article. Section 2 presents the mathematical setting, the contract features, clauses, and the payoff, followed by the formulation and relaxation of the control problem and a discussion of how indifference pricing applies to ASR. Section 3 addresses the management of repurchase programs, implementing policies under the relaxed framework that enables gradient-based optimization. Section 4 then applies the hedging framework to these policies, evaluating the effectiveness of the overall approach.

## 2 The model

### 2.1 Mathematical Setting

In our analysis, in order to simplify the exposition, we assume that buyback operations take place on a discrete set of equally-spaced dates. This assumption induces a discrete time grid with step size δ​t\delta t, which we set to one day. Each point in the grid tn=n⋅δ​tt\_{n}=n\cdot\delta t corresponds to the n​-thn\text{-th} day. The program starts at t1=δ​tt\_{1}=\delta t, while the maturity is denoted by tM​a​x=NM​a​x⋅δ​tt\_{Max}=N\_{Max}\cdot\delta t. The earliest settlement date is tM​i​n=NM​i​n⋅δ​tt\_{Min}=N\_{Min}\cdot\delta t and it sets the beginning of the exercise window.

To simplify the notation, we define the index sets 𝒯={n∈{1,…,NM​a​x}}\mathcal{T}=\{n\in\{1,...,N\_{Max}\}\}, representing the full duration of the program, and ℰ={n∈{NM​i​n,…,NM​a​x}}\mathcal{E}=\{n\in\{N\_{Min},...,N\_{Max}\}\}, corresponding to the exercise window.

We proceed to define the probability space (Ω,ℙ,ℱ)(\Omega,\mathbb{P},\mathcal{F}), where ℙ\mathbb{P} is the physical measure. The underlying asset is modeled by the stochastic process (Sn)n∈𝒯(S\_{n})\_{n\in\mathcal{T}}, adapted to the filtration (ℱn)n∈𝒯(\mathcal{F}\_{n})\_{n\in\mathcal{T}}.

In our numerical experiment, we adopt the Black–Scholes model for the underlying price process (Sn)n∈𝒯(S\_{n})\_{n\in\mathcal{T}}, as our focus is on the design of policies rather than on the specific dynamics of StS\_{t}. This choice also enables efficient sampling from Ω\Omega to construct mutually independent training, validation, and test sets. Following standard practice in the literature [[3](https://arxiv.org/html/2601.18686v1#bib.bib10 "Pricing and managing complex share buy-back contracts: an alternative to optimal control")], we assume that the physical measure ℙ\mathbb{P} coincides with the risk-neutral measure ℚ\mathbb{Q}. Furthermore, since buyback programs typically last only a few months, interest rates have a negligible effect; therefore, we set the risk-free rate rr to zero.

The bank’s repurchases are described by the following two ℱn\mathcal{F}\_{n}-adapted processes and by a ℱn\mathcal{F}\_{n}-stopping time τ=n∗⋅d​t\tau=n^{\*}\cdot dt, with n∗∈ℰn^{\*}\in\mathcal{E}:

* •

  (bn)n∈𝒯(b\_{n})\_{n\in\mathcal{T}}, the number of shares bought each day for the buyback program.
* •

  (hn)n∈𝒯∖{NM​a​x}(h\_{n})\_{n\in\mathcal{T}\setminus\{N\_{Max}\}}, the equity units held at each point along the time grid for hedging purposes.

For each n∈𝒯n\in\mathcal{T}, let QnQ\_{n} and WnW\_{n} denote, respectively, the cumulative number of repurchased shares and the corresponding cash outflow up to and including day nn. We also define the benchmark price process (An)n∈𝒯(A\_{n})\_{n\in\mathcal{T}}, given by the average price starting from t1t\_{1}. The dynamics of these processes are given by:

|  |  |  |
| --- | --- | --- |
|  | Qn=∑k=1nbk,Wn=∑k=1nbk⋅Sk and An=1n⋅∑k=1nSk.Q\_{n}=\sum\_{k=1}^{n}b\_{k},\qquad W\_{n}=\sum\_{k=1}^{n}b\_{k}\cdot S\_{k}\quad\text{ and }\quad A\_{n}=\frac{1}{n}\cdot\sum\_{k=1}^{n}S\_{k}. |  |

In these setting, we are ignoring intraday price movements and transaction costs. In particular, we assume that at the time of the repurchase decision, the price at which the transaction is executed is known exactly and coincides with the price used in the arithmetic average defining the payoff. Ignoring intraday variations is expected to have a negligible impact, as they occur on a much shorter time scale than the duration of the product, while transaction costs can be easily incorporated into the model.

### 2.2 Term Sheet

Before presenting the analytical expression of the Profit and Loss, we first outline the term sheet of the buyback under analysis. We assume that the volume of shares is expressed as the total amount of cash to be spent on the market, though one could repeat the analysis for contracts defining it as the number of shares to repurchase.

We also include one of the most common features in ASR. During the second phase, the bank has the right to exercise when the notional amount falls within a predefined range [WM​i​n, ​WM​a​x][W\_{Min},\text{ }W\_{Max}]. Its width, known as the greenshoe, is one of the most used tools to make ASR more competitive, for example, by offering a larger discount on the benchmark price.

We now briefly consider the timing of share delivery and payments. It is common for the company to gradually provide the necessary funds over the life of the program, while the bank delivers the shares as they are purchased. The final payoff is made at the termination date of the contract, denoted by τ\tau, hence the term post-paid ASR. Alternative delivery mechanisms should have little impact on the pricing of the contract given its comparably low maturity, and would anyway be completely irrelevant under our assumption of zero interest rates.

Finally, we address the trading constraints, which play a major role in our model. Specifically, daily trading is typically limited to a percentage of the volume of the asset exchanged on the market. The processes (ν¯n)n∈𝒯​ and ​(ν¯n)n∈𝒯(\underline{\nu}\_{n})\_{n\in\mathcal{T}}\text{ and }(\overline{\nu}\_{n})\_{n\in\mathcal{T}} denote the lower and upper bounds for the buyback portfolio, and their computation usually excludes end-of-day auctions from the total market volume. Instead, auctions are incorporated into (ν¯nh)n∈𝒯∖{NM​a​x}(\overline{\nu}\_{n}^{h})\_{n\in\mathcal{T}\setminus\{N\_{Max}\}}, which also limits the hedging portfolio and may prevent the implementation of the Greeks. The first resulting limitation is imposed by the ASR contract, while the second arises from market regulations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {bn∈[ν¯n,ν¯n]bn+|hn−hn−1|≤ν¯nh∀n∈𝒯.\left\{\begin{aligned} &b\_{n}\in[\,\underline{\nu}\_{n},\,\overline{\nu}\_{n}]\\[5.0pt] &b\_{n}+|h\_{n}-h\_{n-1}|\leq\overline{\nu}\_{n}^{h}\end{aligned}\right.\qquad\forall n\in\mathcal{T}. |  | (1) |

### 2.3 Profit and Loss

We now introduce the bank’s profit and loss, or P​n​LPnL, which consists of two components: the payoff of the ASR and, when allowed, the result of the hedging activity. The corresponding hedging portfolio is automatically closed once the repurchase program is completed.

Both cash flows occur at the final settlement τ=n∗⋅δ​t\tau=n^{\*}\cdot\delta t. The total profit and loss is therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​n​Lτ=P​n​LτA​S​R+P​n​LτH​e​d​g​e.PnL\_{\tau}=PnL^{ASR}\_{\tau}+PnL^{Hedge}\_{\tau}. |  | (2) |

We now detail the analytical expression of P​n​LτA​S​RPnL^{ASR}\_{\tau}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | {P​n​LτA​S​R=(1−δ)⋅An∗⋅Qn∗−Wn∗Wn∗∈[WM​i​n,WM​a​x]\left\{\begin{aligned} &PnL^{ASR}\_{\tau}=(1-\delta)\cdot A\_{n^{\*}}\cdot Q\_{n^{\*}}-W\_{n^{\*}}\\ &W\_{n^{\*}}\in[W\_{Min},W\_{Max}]\end{aligned}\right. |  | (3) |

The parameter δ\delta denotes the discount offered to the client on the benchmark An∗A\_{n^{\*}}, whose discounted value (1−δ)⋅An∗(1-\delta)\cdot A\_{n^{\*}} can be interpreted as the per-share delivery price and determines the bank’s remuneration. The profit depends on the ability to execute the repurchases bnb\_{n} at favorable prices.

To characterize the dynamics of the problem, we define the state space at time tnt\_{n} as the collection of variables entering the definition of P​n​LA​S​RPnL^{ASR} and containing all the information relevant for managing the contract:

|  |  |  |
| --- | --- | --- |
|  | 𝒮n=(n, ​Sn, ​An, ​Qn−1, ​Wn−1).\mathcal{S}\_{n}=(n,\text{ }S\_{n},\text{ }A\_{n},\text{ }Q\_{n-1},\text{ }W\_{n-1}). |  |

We observe that, in theory, it is not possible to guarantee that ∃n∈ℰ:Wn∈[WM​i​n,WM​a​x]\exists n\in\mathcal{E}:\ W\_{n}\in[W\_{Min},W\_{Max}] with probability ℙ=1\mathbb{P}=1. Indeed, a sharp decline in the value of StS\_{t} may prevent the bank from spending WM​i​nW\_{Min}, as this might require exceeding daily trading limits or, in an extreme scenario, purchasing all outstanding shares.

In our simulations, this may result in a few pathological paths where the condition is not satisfied. In practice, many of these cases correspond to Market Disruption Events, which are typically covered by dedicated contractual clauses. The remaining cases, which are rare under realistic market conditions, can be handled through penalty terms in the optimization problem, as detailed below.

Regarding the hedging portfolio, we follow the same framework described in [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")]. The portfolio is self-financing, and the agent is allowed to trade the firm’s shares to mitigate its exposure. In particular, at time tnt\_{n}, the value of the holdings is given by hn⋅Snh\_{n}\cdot S\_{n}. However, P​n​LnH​e​d​g​ePnL^{Hedge}\_{n} must account for all the cash flows required to rebalance the position in SnS\_{n}. At the final settlement τ\tau, it is expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​n​LτH​e​d​g​e=∑k=1n∗hk​(Sk+1−Sk).PnL^{Hedge}\_{\tau}=\sum\_{k=1}^{n^{\*}}h\_{k}(S\_{k+1}-S\_{k}). |  | (4) |

### 2.4 Control Problem Optimization

In this section, we address the control problem optimization framework based on risk measures, described as functions ρ:χ→ℝ\rho:\chi\to\mathbb{R}, where χ:Ω→ℝ\chi:\Omega\to\mathbb{R} denotes the space of random variables in which P​n​LτA​S​RPnL^{ASR}\_{\tau}, P​n​LτH​e​d​g​ePnL^{Hedge}\_{\tau} and P​n​LτPnL\_{\tau} are defined. Specifically, we rely on the concept of optimized certainty equivalent, or OCE, risk measures [[4](https://arxiv.org/html/2601.18686v1#bib.bib15 "An old-new concept of convex risk measures: the optimized certainty equivalent"), [5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], which allow for efficient computations, as detailed below.

The optimal policy is obtained as the solution of the following control problem [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], which consists of minimizing the chosen risk measure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(P​n​Lτ)=inf𝒫​ ​ρ​(P​n​Lτ)=inf𝒫​ ​ρ​(P​n​LτA​S​R+P​n​LτH​e​d​g​e),\pi(PnL\_{\tau})=\underset{\mathcal{P}}{\inf}\text{ }\rho(PnL\_{\tau})=\underset{\mathcal{P}}{\inf}\text{ }\rho(PnL^{ASR}\_{\tau}+PnL^{Hedge}\_{\tau}), |  | (5) |

where ​𝒫={n∗∈ℰ, ​(hn)n∈{1,…,n∗}, ​(bn)n∈{1,…,n∗}}.\text{where }\mathcal{P}=\{n^{\*}\in\mathcal{E},\text{ }(h\_{n})\_{n\in\{1,...,n^{\*}\}},\text{ }(b\_{n})\_{n\in\{1,...,n^{\*}\}}\}.

In practice, the objective is to identify the optimal values of n∗n^{\*}, (bn)n∈{1,…,n∗}(b\_{n})\_{n\in\{1,...,n^{\*}\}}, (hn)n∈{1,…,n∗}(h\_{n})\_{n\in\{1,...,n^{\*}\}}, where 𝒫\mathcal{P} denotes the set of admissible policies allowed by the contract. Once the program is terminated, the bank must cease both repurchase and hedging activities, which imposes the following conditions:

|  |  |  |
| --- | --- | --- |
|  | bn=0∀n>n∗andhn=0∀n≥n∗.b\_{n}=0\quad\forall n>n^{\*}\qquad\text{and}\qquad h\_{n}=0\quad\forall\ n\geq n^{\*}. |  |

Moreover, since it cannot be guaranteed with certainty that ∃n∈ℰ:Wn∈[WM​i​n,WM​a​x]\exists n\in\mathcal{E}:W\_{n}\in[W\_{Min},W\_{Max}] due to a possible sharp decrease in value of StS\_{t}, we add a quadratic penalty term ΨM​i​n\Psi\_{Min} to the objective function. The parameter βm​i​n\beta\_{min} is a coefficient that aligns the order of magnitude of ΨM​i​n\Psi\_{Min} with that of ρ​(P​n​LτA​S​R)\rho(PnL\_{\tau}^{ASR}), enabling an effective penalization. Once defined ΨM​i​n=((WM​i​n−Wτ)+)2\Psi\_{Min}=((W\_{Min}-W\_{\tau})^{+})^{2}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(P​n​Lτ)=inf𝒫​{ρ​(P​n​Lτ)+βm​i​n⋅ΨM​i​n}.\pi(PnL\_{\tau})=\underset{\mathcal{P}}{\inf}\{\rho(PnL\_{\tau})+\beta\_{min}\cdot\Psi\_{Min}\}. |  | (6) |

We anticipate that in our implementation no penalty is required for exceeding WM​a​xW\_{Max}. Indeed, in the buyback execution strategies detailed in the Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), repurchases automatically cease once WM​a​xW\_{Max} is reached.

Our approach consists in expressing these quantities as parametric functions and subsequently optimizing them. In particular, following [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], hn=fθ​(𝒮n)h\_{n}=f\_{\theta}(\mathcal{S}\_{n}), where fθf\_{\theta} is a neural network and θ\theta denotes its parameters. Analogously, bn=fϕ​(𝒮n)b\_{n}=f\_{\phi}(\mathcal{S}\_{n}), where fϕf\_{\phi} is another parametric function. The domain of the control problem is then translated from 𝒫\mathcal{P} to 𝒫′\mathcal{P^{\prime}}:

|  |  |  |
| --- | --- | --- |
|  | 𝒫′={n∗∈ℰ, ​(hn)n∈{1,…,n∗}, ​(bn)n∈{1,…,n∗}:hn=fθ​(𝒮n), ​bn=fϕ​(𝒮n)​∀n∈{1,…,n∗}}.\mathcal{P^{\prime}}=\{n^{\*}\in\mathcal{E},\text{ }(h\_{n})\_{n\in\{1,...,n^{\*}\}},\text{ }(b\_{n})\_{n\in\{1,...,n^{\*}\}}:h\_{n}=f\_{\theta}(\mathcal{S}\_{n}),\text{ }b\_{n}=f\_{\phi}(\mathcal{S}\_{n})\ \forall n\in\{1,...,n^{\*}\}\}. |  |

Hence, the vector η=[θ; ​ϕ]\eta=[\theta;\text{ }\phi] and n∗n^{\*} fully characterizes the agent’s policy, and the optimization over 𝒫′\mathcal{P^{\prime}} can therefore be reformulated as an optimization problem over [n∗, ​θ, ​ϕ][n^{\*},\text{ }\theta,\text{ }\phi]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(P​n​Lτ)=inf𝒫′​ ​ρ​(P​n​Lτ+βm​i​n⋅ΨM​i​n)=infn∗, ​θ, ​ϕ​ ​ρ​(P​n​Lτ+βm​i​n⋅ΨM​i​n).\pi(PnL\_{\tau})=\underset{\mathcal{P^{\prime}}}{\inf}\text{ }\rho(PnL\_{\tau}+\beta\_{min}\cdot\Psi\_{Min})=\underset{n^{\*},\text{ }\theta,\text{ }\phi}{\inf}\text{ }\rho(PnL\_{\tau}+\beta\_{min}\cdot\Psi\_{Min}). |  | (7) |

The procedure described in [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], where the authors reformulate the search for the optimal policy (hn)n∈{1,…,n∗}(h\_{n})\_{n\in\{1,...,n^{\*}\}} as an optimization over the network parameters θ\theta, is extended here also to the ASR management problem. Optimizing the process (bn)n∈{1,…,n∗}∈ℝn∗(b\_{n})\_{n\in\{1,...,n^{\*}\}}\in\mathbb{R}^{n^{\*}} and τ∈ℰ\tau\in\mathcal{E} is thus transformed into finding the optimal set of parameters ϕ\phi that characterize a parametrized heuristic strategy. For the effectiveness of optimizing heuristic policies to deal with ASR, see [[3](https://arxiv.org/html/2601.18686v1#bib.bib10 "Pricing and managing complex share buy-back contracts: an alternative to optimal control")]. In addition, this framework can be applied exclusively to the execution of the buyback, as done in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."): the optimization is performed only on n∗n^{\*} and ϕ\phi, and P​n​LτPnL\_{\tau} is replaced by P​n​LτA​S​RPnL\_{\tau}^{ASR}.

We now introduce the concept of optimized certainty equivalent by providing its definition [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")].

###### Definition 1 (Optimized Certainty Equivalent Risk Measure).

Let l:ℝ→ℝl:\mathbb{R}\to\mathbb{R} be a loss function that is continuous, non-decreasing and convex, and let Z∈χZ\in\chi. Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(Z)=infw∈ℝ​{w+𝔼​[l​(−w−Z)]}\rho(Z)=\underset{w\in\mathbb{R}}{\inf}\{w+\mathbb{E}[l(-w-Z)]\} |  | (8) |

is an OCE risk measure.

By inserting the OCE definition, which satisfies the property of the convex risk measure [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")], into the control problem formulation, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(P​n​Lτ)=infθ, ​ϕ​infw∈ℝ​{w+𝔼​[l​(−w−P​n​Lτ)]}=infθ, ​ϕ, ​w∈ℝ​{w+𝔼​[l​(−w−P​n​Lτ)]}.\pi(PnL\_{\tau})=\underset{\theta,\text{ }\phi}{\inf}\ \underset{w\in\mathbb{R}}{\inf}\{w+\mathbb{E}[l(-w-PnL\_{\tau})]\}=\underset{\theta,\text{ }\phi,\text{ }w\in\mathbb{R}}{\inf}\{w+\mathbb{E}[l(-w-PnL\_{\tau})]\}. |  | (9) |

The value of ww can be interpreted as a cash injection added to the asset ZZ. Definition [1](https://arxiv.org/html/2601.18686v1#Thmdefinition1 "Definition 1 (Optimized Certainty Equivalent Risk Measure). ‣ 2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") aims to determine the optimal value of ww that minimizes the penalty term w+𝔼​[l​(−w−Z)]w+\mathbb{E}[l(-w-Z)], which accounts for both the cash position ww and the expected loss associated with holding Z+wZ+w.

Thanks to the last representation in equation [9](https://arxiv.org/html/2601.18686v1#S2.E9 "In 2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), the adoption of OCE measures does not require solving an additional minimization problem at each training batch. Instead, it introduces one extra parameter that can be naturally incorporated into the back-propagation process with negligible computational overhead.

In this work, we adopt the OCE version of the expected shortfall. This measure derives from Definition [1](https://arxiv.org/html/2601.18686v1#Thmdefinition1 "Definition 1 (Optimized Certainty Equivalent Risk Measure). ‣ 2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") by setting

|  |  |  |
| --- | --- | --- |
|  | l​(x)=11−α⋅m​a​x​(x, ​0).l(x)=\frac{1}{1-\alpha}\cdot max(x,\text{ }0). |  |

where α∈(0,1)\alpha\in(0,1) is the confidence level [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging"), [9](https://arxiv.org/html/2601.18686v1#bib.bib11 "Stochastic finance: an introduction in discrete time")]. The advantage of this formulation is that, during back-propagation, there is no need to explicitly compute the α\alpha-quantile of the smallest losses.

In order to verify the consistency of our results, we also optimize our policies under the following choice of ll:

|  |  |  |
| --- | --- | --- |
|  | l​(x)=x+12⋅γ⋅x2.l(x)=x+\frac{1}{2}\cdot\gamma\cdot x^{2}. |  |

In this case, the resulting risk measure coincides with the mean-variance, where γ\gamma denotes the risk-aversion coefficient for the variance. Indeed, by substituting this definition of ll into the OCE formula, we obtain:

|  |  |  |
| --- | --- | --- |
|  | ρ​(Z)=infw∈ℝ​{w+𝔼​[l​(−w−Z)]}=infw∈ℝ​{w+𝔼​[−w−Z+12⋅γ⋅(Z+w)2]}=\rho(Z)=\underset{w\in\mathbb{R}}{\inf}\{w+\mathbb{E}[l(-w-Z)]\}=\underset{w\in\mathbb{R}}{\inf}\{w+\mathbb{E}[-w-Z+\frac{1}{2}\cdot\gamma\cdot(Z+w)^{2}]\}= |  |

|  |  |  |
| --- | --- | --- |
|  | infw∈ℝ{𝔼[−Z+12⋅γ⋅(Z+w)2]}=−𝔼[Z]+12⋅γ⋅infw∈ℝ{(Z+w)2]}=\underset{w\in\mathbb{R}}{\inf}\{\mathbb{E}[-Z+\frac{1}{2}\cdot\gamma\cdot(Z+w)^{2}]\}=-\mathbb{E}[Z]+\frac{1}{2}\cdot\gamma\cdot\underset{w\in\mathbb{R}}{\inf}\{(Z+w)^{2}]\}= |  |

|  |  |  |
| --- | --- | --- |
|  | =−𝔼​[Z]+12⋅γ⋅Var​(Z).=-\mathbb{E}[Z]+\frac{1}{2}\cdot\gamma\cdot\mathrm{Var}(Z). |  |

However, since l​(x)l(x) is not a decreasing function, ρ​(P​n​Lτ)\rho(PnL\_{\tau}) does not correspond to an OCE in the formal sense. Specifically, the resulting risk measure does not satisfy the properties of a convex risk measure, although the optimization can still be carried out. We note that the mean-variance approach is also employed in [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring")], where it is computed directly from the sample moments of the profit and loss.

Finally, for numerical stability, the payoff P​n​LτPnL\_{\tau} is normalized by WM​i​nW\_{Min}, which prevents the values from exploding, since the notional amounts involved can be very large.

### 2.5 Problem Relaxation

In practice, in the machine learning framework we develop, the risk measure acts as the loss function and is used to evaluate and update policies. However, to implement neural networks in a unified workflow for the management and hedging of ASR, we require the loss computation to be fully differentiable with respect to the input, namely 𝒮t\mathcal{S}\_{t}. This allows us to rely on standard optimization techniques for networks such as gradient descent.

Once tn∈[tM​i​n, ​tM​a​x]t\_{n}\in[t\_{Min},\text{ }t\_{Max}], the agent must decide whether to close or continue the repurchase. This optionality can be represented by a function of the state space 𝒮n\mathcal{S}\_{n} with values in {0,1}\{0,1\}. As shown in [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring")], this feature constitutes the main obstacle to the gradient flow.

The exercise policy is made differentiable through a stochastic stopping policy (pn)n∈𝒯(p\_{n})\_{n\in\mathcal{T}}, which represents the probability of exercise conditional on ℱn\mathcal{F}\_{n}. It takes values in [0, ​1][0,\text{ }1] and pn=0​ ​∀n∈𝒯∖ℰp\_{n}=0\ \text{ }\forall n\in\mathcal{T}\setminus\mathcal{E}.

The authors link the process (pn)n∈𝒯(p\_{n})\_{n\in\mathcal{T}} to an effective stopping time τ\tau by introducing an extended σ​-algebra ​𝒢⊇ℱNM​a​x\sigma\text{-algebra }\mathcal{G}\supseteq\mathcal{F}\_{N\_{Max}} and the probability space (Ω, ​ℙ, ​𝒢)(\Omega,\text{ }\mathbb{P},\text{ }\mathcal{G}), which supports a family of i.i.di.i.d random variables (ζn)n∈ℰ(\zeta\_{n})\_{n\in\mathcal{E}} uniform in [0,1][0,1] independent of ℱNM​a​x\mathcal{F}\_{N\_{Max}}.

The stopping time τ=n∗⋅δ​t\tau=n^{\*}\cdot\delta t is defined as n∗=min⁡{n∈ℰ​ | ​ζn≤pn},n^{\*}=\min\{n\in\mathcal{E}\text{ }|\text{ }\zeta\_{n}\leq p\_{n}\}, and the exercise decision is given by p^n=𝟏ζn≤pn\hat{p}\_{n}=\mathbf{1}\_{\zeta\_{n}\leq p\_{n}}, which follows a Bernoulli distribution with parameter pnp\_{n}, conditional on ℱn\mathcal{F}\_{n}. Hence, the payoff can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​n​Lτ=∑n=NM​i​nNM​a​x∏k=NM​i​nn−1(1−p^k)⋅p^n⋅P​n​Ln,PnL\_{\tau}=\sum\_{n=N\_{Min}}^{N\_{Max}}\prod\_{k=N\_{Min}}^{n-1}(1-\hat{p}\_{k})\cdot\hat{p}\_{n}\cdot PnL\_{n}, |  | (10) |

where τ\tau depends on the sampling of (ζn)n∈ℰ(\zeta\_{n})\_{n\in\mathcal{E}}. At each date tn∈[TM​i​n, ​TM​a​x]t\_{n}\in[T\_{Min},\text{ }T\_{Max}] is thus associated an unconditional probability of terminating the program equal to p~n=∏k=NM​i​nn−1(1−pk)⋅pn\tilde{p}\_{n}=\prod\_{k=N\_{Min}}^{n-1}(1-p\_{k})\cdot p\_{n}, with ∑n=NM​i​nNM​a​xp~n=1\sum\_{n=N\_{Min}}^{N\_{Max}}\tilde{p}\_{n}=1.

Consequently, differentiability is ensured by weighting the loss term l​(−w−P​n​Ln)l(-w-PnL\_{n}) and the penalty ΨM​i​n\Psi\_{Min} with their unconditional probability. Therefore, the control problem becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(P​n​Lτ)=infθ,ϕ,w​{w+𝔼​[∑n=NminNmaxp~n⋅(l​(−w−P​n​Ln)+βm​i​n⋅((Wmin−Wn)+)2)]}.\pi(PnL\_{\tau})=\underset{\theta,\ \phi,\ w}{\inf}\left\{w+\mathbb{E}\!\left[\sum\_{n=N\_{\min}}^{N\_{\max}}\tilde{p}\_{n}\cdot\left(l(-w-PnL\_{n})+\beta\_{min}\cdot((W\_{\min}-W\_{n})^{+})^{2}\right)\right]\right\}. |  | (11) |

### 2.6 ASR Pricing

In conclusion, we address the pricing of ASR contracts. In a complete market, the risk-neutral valuation formula determines the contract price ΠA​S​R​(t0)\Pi^{ASR}(t\_{0}), which represents the value of the replicating portfolio at time t0t\_{0}. However, this portfolio cannot always be replicated in practice, since it is defined in terms of Greeks that, as discussed in the Introduction, suffer from several limitations and may be infeasible to implement due to the constraints imposed by the term sheet or market regulations. Consequently, the theoretical value ΠA​S​R​(t0)\Pi^{ASR}(t\_{0}) may lose its practical relevance.

To clarify this point, we focus on the discount δ\delta, which is the standard reference in the industry. In the competitive ASR market, banks secure contracts by offering a greater discount than their competitors; as a result, practitioners commonly refer to this discount as the “price” of the buyback program. In practice, the better the performance in the execution, and therefore the higher the value generated by the ASR, the larger the discount that can be offered. Typically, offering a higher discount is made possible either by enriching the term sheet with additional features, such as a greenshoe on the notional amount, or by modifying the payoff structure itself.

If replication through Greeks were possible, the bank would offer the so-called fair discount δf​a​i​r\delta^{fair}, obtained by requiring the contract to be fair. In our settings with interest rates set to zero, the fair discount in the risk-neutral valuation framework corresponds to the value of δ\delta that, substituted into P​n​LτA​S​RPnL^{ASR}\_{\tau}, satisfies 𝔼ℚ​[P​n​LτA​S​R]=0\mathbb{E}^{\mathbb{Q}}[PnL^{ASR}\_{\tau}]=0
where ℚ\mathbb{Q} is a risk-neutral measure. It follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δf​a​i​r=1−𝔼ℚ​[Wn∗]𝔼ℚ​[An∗⋅Qn∗].\delta^{fair}=1-\frac{\mathbb{E}^{\mathbb{Q}}[W\_{n^{\*}}]}{\mathbb{E}^{\mathbb{Q}}[A\_{n^{\*}}\cdot Q\_{n^{\*}}]}. |  | (12) |

The definition of δf​a​i​r\delta^{fair} and the ones that follow hold also in the relaxed settings, where P​n​Lτ, or ​P​n​LτA​S​RPnL\_{\tau},\text{ or }PnL^{ASR}\_{\tau} in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), are distributed over the exercise time window:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​n​L=∑n=NM​i​nNM​a​x∏k=NM​i​nn−1(1−pk)⋅pn⋅P​n​Ln.PnL=\sum\_{n=N\_{Min}}^{N\_{Max}}\prod\_{k=N\_{Min}}^{n-1}(1-p\_{k})\cdot p\_{n}\cdot PnL\_{n}. |  | (13) |

However, since it is not possible to completely eliminate risk, the bank cannot offer the fair discount to its client. An alternative approach is provided by the concept of indifference pricing. Due to the cash-invariance property of convex risk measures, we have:

|  |  |  |
| --- | --- | --- |
|  | ρ​(P​n​Lτ+ρ​(P​n​Lτ))=ρ​(P​n​Lτ)−ρ​(P​n​Lτ)=0.\rho(PnL\_{\tau}+\rho(PnL\_{\tau}))=\rho(PnL\_{\tau})-\rho(PnL\_{\tau})=0. |  |

In particular, ρ​(P​n​Lτ)\rho(PnL\_{\tau}) can be interpreted as the indifference price, that is, the amount of cash required to make the position acceptable according to the risk measure ρ\rho [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")]. Since it is typically negative for ASR contracts, as shown in the following Sections, the bank recognizes an intrinsic value in these products. However, rather than transferring |ρ​(P​n​Lτ)||\rho(PnL\_{\tau})| directly to its client, the bank returns this value in the form of a discount. Consequently, we introduce the concept of the indifference discount, defined as the value δi​n​d\delta^{ind} such that ρ​(P​n​Lτ)=0\rho(PnL\_{\tau})=0.

The quantities δf​a​i​r\delta^{fair} and δi​n​d\delta^{ind} provide valuable insights on the performance of our implementation. Specifically, δf​a​i​r\delta^{fair} denotes the discount that assumes perfect hedging, while δi​n​d\delta^{ind} represents the discount that can be offered given the actual hedging capabilities. It is worth noting that the definition of δf​a​i​r\delta^{fair} involves P​n​LτA​S​RPnL^{ASR}\_{\tau}: once the ASR management strategy is fixed, it measures the discount enabled by that policy. Conversely, δi​n​d\delta^{ind} is obtained by considering the overall profit and loss, P​n​Lτ=P​n​LτA​S​R+P​n​LτH​e​d​g​ePnL\_{\tau}=PnL\_{\tau}^{ASR}+PnL\_{\tau}^{Hedge}, and therefore also reflects the hedging performance. In our numerical analysis, both quantities are estimated on an independent test set. For the fair discount, we approximate the expected values under ℚ\mathbb{Q} by their sample averages, as in our settings ℙ=ℚ\mathbb{P}=\mathbb{Q}.

## 3 ASR Management

### 3.1 Smooth Bang-Bang Strategy

We start our analysis by addressing the execution of the buyback. In this section, we describe the smooth bang-bang policy, which plays the role of the benchmark implementation to be compared to neural network models.

It is based on two almost linear repurchase regimes: the first targeting WM​i​nW\_{Min} at the last termination date NM​a​xN\_{Max}, while the second WM​a​xW\_{Max} at the minimum termination date NM​i​nN\_{Min}.

|  |  |  |
| --- | --- | --- |
|  | {qnm​i​n=max⁡(min⁡(ν¯n, ​(WM​i​n−Wn−1)+), ​WM​i​n−Wn−1Sn⋅(NM​a​x−n+1))qnm​a​x=min⁡(ν¯n, ​WM​a​x−Wn−1Sn⋅max⁡(1,NM​i​n−n+1))\left\{\begin{aligned} &q\_{n}^{min}=\max\left(\min\left(\underline{\nu}\_{n},\text{ }\left(W\_{Min}-W\_{n-1}\right)^{+}\right),\text{ }\frac{W\_{Min}-W\_{n-1}}{S\_{n}\cdot(N\_{Max}-n+1)}\right)\\[5.0pt] &q\_{n}^{max}=\min\left(\overline{\nu}\_{n},\text{ }\frac{W\_{Max}-W\_{n-1}}{S\_{n}\cdot\max(1,N\_{Min}-n+1)}\right)\end{aligned}\right. |  |

The repurchase process (bn)n∈𝒯(b\_{n})\_{n\in\mathcal{T}} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bn​(Sn, ​An)=min⁡(qnm​a​x, ​max⁡(qnm​i​n, ​bn∗​(Sn, ​An)))∀n∈𝒯,b\_{n}(S\_{n},\text{ }A\_{n})=\min\left(q\_{n}^{max},\text{ }\max\left(q\_{n}^{min},\text{ }b\_{n}^{\*}(S\_{n},\text{ }A\_{n})\right)\right)\quad\forall n\in\mathcal{T}, |  | (14) |

wherebn∗​(Sn, ​An)=qnm​a​x+qnm​i​n−qnm​a​xδr⋅(SnAn−(1+ϵr)+δr2).\text{where}\quad b\_{n}^{\*}(S\_{n},\text{ }A\_{n})=q\_{n}^{max}+\frac{q\_{n}^{min}-q\_{n}^{max}}{\delta\_{r}}\cdot\left(\frac{S\_{n}}{A\_{n}}-(1+\epsilon\_{r})+\frac{\delta\_{r}}{2}\right).

The number of shares repurchased at tnt\_{n} can take any value value between the two regimes and depends on SnS\_{n} and AnA\_{n} solely through their ratio, centered at 1+ϵr1+\epsilon\_{r}, while the parameter δr\delta\_{r} controls the slope, as shown in figure [1](https://arxiv.org/html/2601.18686v1#S3.F1 "Figure 1 ‣ 3.1 Smooth Bang-Bang Strategy ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").

![Refer to caption](Section2/orderSizeSmoothBangBang.png)


Figure 1: bn​(Sn, ​An)b\_{n}(S\_{n},\text{ }A\_{n}) function: when the ratio between Sn​ and ​AnS\_{n}\text{ and }A\_{n} falls in the interval [1+ϵr−0.5⋅δr, ​1+ϵr+0.5⋅δr][1+\epsilon\_{r}-0.5\cdot\delta\_{r},\text{ }1+\epsilon\_{r}+0.5\cdot\delta\_{r}], the repurchase bnb\_{n} is determined by a linear interpolation over [qnm​i​n, ​qnm​a​x][q\_{n}^{min},\text{ }q\_{n}^{max}].

The intuition behind this approach is straightforward: when SnS\_{n} falls below AnA\_{n}, it becomes advantageous to accelerate the repurchase, as the underlying asset is dragging down the benchmark value. Moreover, the bank is repurchasing shares at a price lower than the potential compensation, thereby increasing its profit.

As described in Section [2](https://arxiv.org/html/2601.18686v1#S2 "2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), the hedging framework detailed in [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")] requires the flow of gradient. We thus introduce probability process (pn)n∈ℰ(p\_{n})\_{n\in\mathcal{E}}, shifting the problem to the relaxed settings. Furthermore, the definition of pnp\_{n} must ensure that Wn∗∈[WM​i​n,WM​a​x]W\_{n^{\*}}\in[W\_{Min},W\_{Max}] when the exercise time τ\tau is sampled using the variables (ζn)n∈ℰ(\zeta\_{n})\_{n\in\mathcal{E}}. In the relaxed setting, this requirement becomes Wn∈[WM​i​n, ​WM​a​x]∀n∈ℰ:∏k=NM​i​nn−1(1−pk)⋅pn>0.W\_{n}\in[W\_{Min},\text{ }W\_{Max}]\quad\forall n\in\mathcal{E}:\prod\_{k=N\_{Min}}^{n-1}(1-p\_{k})\cdot p\_{n}>0.
For this reason, the conditional probability is expressed as a function of WnW\_{n}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pn​(Wn)=max⁡(0, ​min⁡(1, ​1δp⋅(Wn∗−ϵp+δp2)))∀n∈ℰ,p\_{n}(W\_{n})=\max\left(0,\text{ }\min\left(1,\text{ }\frac{1}{\delta\_{p}}\cdot\left(W\_{n}^{\*}-\epsilon\_{p}+\frac{\delta\_{p}}{2}\right)\right)\right)\quad\forall n\in\mathcal{E}, |  | (15) |

where Wn∗=(Wn−12⋅(WM​i​n+WM​a​x))/(12⋅(WM​a​x−WM​i​n))W\_{n}^{\*}=\left(W\_{n}-\frac{1}{2}\cdot(W\_{Min}+W\_{Max})\right)/\left(\frac{1}{2}\cdot(W\_{Max}-W\_{Min})\right), mapping [WM​i​n,WM​a​x]​ into ​[−1,1].[W\_{Min},W\_{Max}]\text{ into }[-1,1].

The value of pnp\_{n} is centered at ϵp\epsilon\_{p} and linearly interpolated over the interval Iℰ=[ϵp−12​δp, ​ϵp+12​δp]I\_{\mathcal{E}}=[\epsilon\_{p}-\frac{1}{2}\delta\_{p},\text{ }\epsilon\_{p}+\frac{1}{2}\delta\_{p}], with the result capped within [0,1][0,1]. The slope is determined by the parameter δp\delta\_{p}, and at TM​a​xT\_{Max} the agent is forced to close the program. If Iℰ⊆[−1,1]I\_{\mathcal{E}}\subseteq[-1,1], the formulation of pnp\_{n} guarantees a non-zero probability of exercise only when Wn∈[WM​i​n,WM​a​x]W\_{n}\in[W\_{Min},W\_{Max}]. For this strategy, the set of trainable parameter is ϕ=[ϵr, ​δr, ​ϵp, ​δp]\phi=[\epsilon\_{r},\text{ }\delta\_{r},\text{ }\epsilon\_{p},\text{ }\delta\_{p}].

### 3.2 The network strategy

In this section, we address what we refer to as the network strategy. The relationship between the processes (bn)n∈𝒯(b\_{n})\_{n\in\mathcal{T}}, (pn)n∈ℰ(p\_{n})\_{n\in\mathcal{E}} and the full state space (𝒮n)n∈𝒯(\mathcal{S}\_{n})\_{n\in\mathcal{T}} is delegated to a neural network, represented by a function fϕ:ℝ3→[0,1]2f\_{\phi}:\mathbb{R}^{3}\to[0,1]^{2}, with a sigmoid activation function in the output layer. At each time step tnt\_{n}, the network computes

|  |  |  |  |
| --- | --- | --- | --- |
|  | [bn∗, ​pn]=fϕ​(n−NM​i​nNM​i​n​ ​SnAn, ​Wn−1WM​i​n),[b\_{n}^{\*},\text{ }p\_{n}]=f\_{\phi}\left(\frac{n-N\_{Min}}{N\_{Min}}\text{ }\frac{S\_{n}}{A\_{n}},\text{ }\frac{W\_{n-1}}{W\_{Min}}\right), |  | (16) |

with bn=vnm​a​x+(vnm​i​n−vnm​a​x)⋅bn∗∀n∈𝒯b\_{n}=v\_{n}^{max}+\left(v\_{n}^{min}-v\_{n}^{max}\right)\cdot b\_{n}^{\*}\quad\forall n\in\mathcal{T}. The quantities vnm​i​nv\_{n}^{min} and vnm​a​xv\_{n}^{max} are defined in the following.

The inputs of the network are rescaled to have comparable magnitudes, a step that proves crucial for successful training. Furthermore, they are dimensionless, as in [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring")].

Our experiments suggest that the total number of shares already repurchased Qn−1Q\_{n-1} does not contribute significantly once the other state variables in 𝒮n\mathcal{S}\_{n} are taken into account. Similarly, it is sufficient to represent the underlying value SnS\_{n} and its running average AnA\_{n} through their ratio, as including them separately does not offer additional benefit. The number of inputs is thus reduced from five to three, decreasing the model complexity.

Before introducing the expressions for vnm​i​nv\_{n}^{min} and vnm​a​xv\_{n}^{max}, which provide greater flexibility in order to exploit the information contained in the state space, we define the quantity (dn)n∈𝒯∖NM​a​x(d\_{n})\_{n\in\mathcal{T}\setminus{N\_{Max}}}. At time tnt\_{n}, dnd\_{n} denotes the number of days required to reach WM​i​nW\_{Min} when purchasing the maximum number of shares ν¯k\overline{\nu}\_{k} for all k>nk>n up to maturity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dn=⌈dn∗⌉, with dn∗=WM​i​n−Wn−1ν¯n⋅Sn∗.d\_{n}=\lceil d\_{n}^{\*}\rceil,\quad\text{ with }\quad d\_{n}^{\*}=\frac{W\_{Min}-W\_{n-1}}{\overline{\nu}\_{n}\cdot S\_{n}^{\*}}. |  | (17) |

The term Sn∗S\_{n}^{\*} acts as a buffer against a sharp decline in the spot price. Within the Black–Scholes framework employed in our analysis, a possible choice for Sn∗S\_{n}^{\*} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn∗=Sn⋅e−12​σ2​d​t+Φ−1​(γ∗)⋅σ​d​t,S\_{n}^{\*}=S\_{n}\cdot e^{-\frac{1}{2}\sigma^{2}dt\ +\ \Phi^{-1}(\gamma^{\*})\cdot\sigma\sqrt{dt}}, |  | (18) |

where Φ​(x)\Phi(x) denotes the cumulative distribution function of a standard normal random variable. In practice, Sn∗S\_{n}^{\*} represents the worst-case projection of the asset value Sn+1S\_{n+1}, which we compute at a confidence level of γ∗=0.05\gamma^{\*}=0.05.

Finally, we detail the definitions of vnm​i​n​ and ​vnm​a​xv\_{n}^{min}\text{ and }v\_{n}^{max}. In the next section, we show their contribution to the increase of performance and how they would impact the smooth bang-bang. For n∈[1, ​NM​a​x−1]n\in[1,\text{ }N\_{Max}-1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vnm​i​n={ν¯n,if dn<NM​a​x−nmin⁡(ν¯n, ​WM​i​n−Wn−1−ν¯n⋅(NM​a​x−n)⋅Sn∗Sn),if dn≥NM​a​x−n.v\_{n}^{min}=\quad\left\{\begin{aligned} &\underline{\nu}\_{n},&&\text{if }\quad d\_{n}<N\_{Max}-n\\[5.0pt] &\min(\overline{\nu}\_{n},\text{ }\frac{W\_{Min}-W\_{n-1}-\overline{\nu}\_{n}\cdot(N\_{Max}-n)\cdot S^{\*}\_{n}}{S\_{n}}),&&\text{if }\quad d\_{n}\geq N\_{Max}-n\end{aligned}\right.. |  | (19) |

At maturity vNM​a​xm​i​n=max⁡(ν¯n, ​WM​i​n−Wn−1Sn).v\_{N\_{Max}}^{min}=\max\left(\underline{\nu}\_{n},\text{ }\frac{W\_{Min}-W\_{n-1}}{S\_{n}}\right).

Unlike the previous policy, the lower bound for daily repurchases is not defined as an even allocation aimed at reaching WM​i​nW\_{Min} by TM​a​xT\_{Max}, since such a rule would enforce purchases even when they are not advantageous. Instead, the policy allows the bank to make the minimum admissible purchase ν¯n\underline{\nu}\_{n} on most days. At the same time, it continuously monitors the minimum number of days required to reach WM​i​nW\_{Min}. If the remaining time is insufficient to reach the minimum notional amount at the current repurchase rate, the policy increases daily purchases accordingly to ensure that the constraint is met by maturity.

The definition of vnm​a​xv\_{n}^{max} closely follows that of the bang-bang. For n∈[1, ​NM​i​n−1]n\in[1,\text{ }N\_{Min}-1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vnm​a​x={min⁡(ν¯n, ​WM​a​x−Wn−1Sn⋅(NM​i​n−n+1)),if dn<NM​a​x−nmax⁡(vnm​i​n, ​WM​a​x−Wn−1Sn⋅(NM​i​n−n+1)),if dn≥NM​a​x−n.v\_{n}^{max}=\quad\left\{\begin{aligned} &\min(\overline{\nu}\_{n},\text{ }\frac{W\_{Max}-W\_{n-1}}{S\_{n}\cdot(N\_{Min}-n+1)}),&&\text{if }\quad d\_{n}<N\_{Max}-n\\[5.0pt] &\max(v\_{n}^{min},\text{ }\frac{W\_{Max}-W\_{n-1}}{S\_{n}\cdot(N\_{Min}-n+1)}),&&\text{if }\quad d\_{n}\geq N\_{Max}-n\end{aligned}\right.. |  | (20) |

For n∈[TM​i​n, ​TM​a​x]n\in[T\_{Min},\text{ }T\_{Max}], the bank may reach WM​a​xW\_{Max} in a single day:

|  |  |  |
| --- | --- | --- |
|  | vnm​a​x=min⁡(ν¯n, ​WM​a​x−Wn−1Sn).v\_{n}^{max}=\min\left(\overline{\nu}\_{n},\text{ }\frac{W\_{Max}-W\_{n-1}}{S\_{n}}\right). |  |

We now turn to explain how the constraints on the notional are met. We note that, by construction, the network strategy ensures that the notional value WtW\_{t} reaches WM​i​nW\_{Min} before maturity, except the cases where the underlying asset StS\_{t} experiences a sharp decline, while also preventing WtW\_{t} from exceeding WM​a​xW\_{Max}. Nevertheless, the implementation may still assign a non-zero probability of termination when Wn∉[WM​i​n,WM​a​x]W\_{n}\notin[W\_{Min},W\_{Max}], thereby violating the contract terms. This is avoided by checking, for each n∈ℰn\in\mathcal{E}, whether Wn∈[WM​i​n,WM​a​x]W\_{n}\in[W\_{Min},W\_{Max}]. If the notional constraints condition is not met, pnp\_{n} is retrospectively set to 0.

However, the bank must terminate the repurchase. Therefore, we force termination at maturity by setting pNM​a​x=1p\_{N\_{Max}}=1. Consequently, the term ΨM​i​n\Psi\_{Min} can penalize the cases where WNM​a​x<WM​i​nW\_{N\_{Max}}<W\_{Min}, reducing the scenarios in which Wn∉[WM​i​n,WM​a​x]∀n∈ℰ.W\_{n}\notin[W\_{Min},W\_{Max}]\quad\forall n\in\mathcal{E}.

Although retrospectively imposing pnp\_{n} to 0 is non-differentiable, thereby excluding certain paths from the backpropagation step, its impact on the overall optimization is limited. Indeed, the interaction between the policy design, for which the notional usually falls within the target interval, the penalty term ΨM​i​n\Psi\_{Min} for extreme scenarios and the fulfillment of the requirement ∑n=NM​i​nNM​a​xp~n=1\sum\_{n=N\_{Min}}^{N\_{Max}}\tilde{p}\_{n}=1 allows the network to quickly learn the optimal timing for contract closure.

In our implementation, the nearly enforcement of the notional constraints reduces the impact of the penalty term ΨM​i​n\Psi\_{Min} and simplifies the calibration of the parameter βm​i​n\beta\_{min}, whose optimal value depends on the specific characteristics of the contract under analysis and could therefore limit the generalizability of the approach. As shown in the next section, our implementation strikes a balance between the freedom granted to the agent and the guidance of its actions, contributing to a faster and more stable training process.

### 3.3 Smooth Bang-Bang vs Network

We begin by introducing the model and the contract used throughout the work. As discussed above, the price of the underlying share is assumed to follow the Black–Scholes dynamics. Nevertheless, our framework can be applied under any specification adopted for the underlying asset. As discussed in Section [2](https://arxiv.org/html/2601.18686v1#S2 "2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), interest rates are neglected by setting r=0r=0.

| S0S\_{0} [€] | σy​e​a​r\sigma\_{year} | r |
| --- | --- | --- |
| 4545 | 0.210.21 | 0 |

Table 1: Black–Scholes parameters.

The term sheet of the ASR contract is presented in table [2](https://arxiv.org/html/2601.18686v1#S3.T2 "Table 2 ‣ 3.3 Smooth Bang-Bang vs Network ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."):

| TM​i​nT\_{Min} [day] | TM​a​xT\_{Max} [day] | WM​i​nW\_{Min} [€] | WM​a​xW\_{Max} [€] | δ\delta | ν¯n\underline{\nu}\_{n} | ν¯n\overline{\nu}\_{n} |
| --- | --- | --- | --- | --- | --- | --- |
| 2222 | 6363 | 810⋅106810\cdot 10^{6} | 990⋅106990\cdot 10^{6} | 0 | 0 | 1.5⋅1061.5\cdot 10^{6} |

Table 2: ASR term sheet. The values of ν¯n​ and ​ν¯n\underline{\nu}\_{n}\text{ and }\overline{\nu}\_{n} are constant ∀n∈𝒯\forall n\in\mathcal{T}.

As mentioned in Section [2](https://arxiv.org/html/2601.18686v1#S2 "2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), we rely on two risk measures: the expected shortfall, which focuses on the left tail of the P​n​LPnL distribution, and the mean-variance loss, which provides a symmetric assessment of risk. To keep the presentation simple and clear, for δf​a​i​r\delta^{fair} and δi​n​d\delta^{ind}, we report only the values obtained under the expected shortfall optimization. The penalty coefficient of ΨM​i​n\Psi\_{Min} is set to βm​i​n=500\beta\_{min}=500.

| Risk Measure | Symbol | Parameter |
| --- | --- | --- |
| Expected Shortfall | E​S0.75ES\_{0.75} | α=0.75\alpha=0.75 |
| Mean-Variance | M​V2.5⋅102MV\_{2.5\cdot 10^{2}} | γ=2.5⋅102\gamma=2.5\cdot 10^{2} |

Table 3: Specification of the risk measures. Both risk measures are computed using the P​n​LPnL normalized by WminW\_{\min}.

For all the numerical results, we employ the standard machine learning data split into training, validation, and test sets. Specifically, the payoff distributions and evaluation metrics, namely the risk measure and the discounts δf​a​i​r\delta^{fair} and δi​n​d\delta^{ind}, are computed on the test set.

Regarding the network strategy, fϕf\_{\phi} consists of four layers: the first three contain 128 neurons each, followed by ReLU activation functions, while the final layer has two neurons with a sigmoid activation. Normalization layers are not used because the key factor for successful training appears to be the scaling of the inputs.

We first qualitatively assess the performance of the smooth bang-bang and network strategy with the payoff distributions. All the distributions of Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") and Section [4](https://arxiv.org/html/2601.18686v1#S4 "4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") are obtained by optimizing the expected shortfall, and the mean-variance risk measure yields similar outcomes. The figures are obtained on a test set of 3000 cases. Moreover, also the discounts δf​a​i​r​ and ​δi​n​d\delta^{fair}\text{ and }\delta^{ind} come from the expected shortfall optimization.

![Refer to caption](Section3/smoothVSnetwork.png)


Figure 2: Payoff distribution for the smooth bang-bang and network strategy. The payoff is normalized by WM​i​nW\_{Min} and expressed in basis points.

The network model exhibits a more concentrated payoff distribution with a thinner left tail, stabilizing performance, as adverse scenarios are less frequent compared to the smooth bang-bang. Moreover, the higher expected values observed under the network policy, also consistent with the mean-variance optimization, suggest an enhanced ability to manage the repurchase process. These findings are further supported by the numerical results in Table [4](https://arxiv.org/html/2601.18686v1#S3.T4 "Table 4 ‣ 3.3 Smooth Bang-Bang vs Network ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."):

| Strategy | E​S0.75ES\_{0.75} | M​V2.5⋅102MV\_{2.5\cdot 10^{2}} | δf​a​i​r\delta^{fair} | δi​n​d\delta^{ind} |
| --- | --- | --- | --- | --- |
| Smooth Bang-Bang | −94.0-94.0 | −62.8-62.8 | 156.5156.5 | 82.182.1 |
| Network | −136.8-136.8 | −161.1-161.1 | 167.4167.4 | 114.6114.6 |

Table 4: Risk measures and discount for smooth bang-bang and network policies, expressed in basis points.

We observe that the expected shortfall takes negative values, which is consistent with the strictly positive payoff distributions. By definition, the expected shortfall represents the average loss in the 1−α1-\alpha worst-case scenarios. Therefore, a positive value indicates an actual loss, which never occurs. Consequently, when the metric takes negative values, a larger absolute value corresponds to a larger profit rather than a larger loss. This same holds for the mean-variance criterion: considering negative outcomes, a larger value in absolute terms still indicates a more favorable outcome. Indeed, the optimization is formulated as a minimization problem. Hence the reported values correspond to

|  |  |  |
| --- | --- | --- |
|  | −𝔼​[P​n​L]+12⋅γ⋅Var​(P​n​L)=−(𝔼​[P​n​L]−12⋅γ⋅Var​(P​n​L)).-\mathbb{E}[PnL]+\frac{1}{2}\cdot\gamma\cdot\mathrm{Var}(PnL)=-(\mathbb{E}[PnL]-\frac{1}{2}\cdot\gamma\cdot\mathrm{Var}(PnL)). |  |

The network policy exhibits a larger absolute value for both metrics. In other words, both evaluation criteria consistently indicate that the network implementation outperforms the smooth bang-bang policy. Moreover, the higher fair discount, reflecting the greater expected value of the payoff distribution, implies that the former policy generates more value while managing the ASR.

Furthermore, the network policy also exhibits a higher indifference discount δi​n​d\delta^{ind}, which incorporates exposure assessment through the measure ρ\rho. This implies that, even accounting for risk, the bank can still offer a larger discount, providing an alternative to standard pricing that better reflects operational capabilities.

We now turn to investigating the factors driving this performance improvement. In a manner similar to [[11](https://arxiv.org/html/2601.18686v1#bib.bib6 "Accelerated share repurchase and other buyback programs: what neural networks can bring")], where networks are used to introduce a modification from a simpler policy, the network strategy is obtained by improving the smooth bang-bang. The main differences between the two policies are three:

1. 1.

   the use of a neural network to compute bnb\_{n}
2. 2.

   the use of a neural network to compute pnp\_{n}
3. 3.

   the definition of the interval [vnm​i​n,vnm​a​x][v\_{n}^{min},v\_{n}^{max}], which allows for greater flexibility in market repurchases compared to the bounds bn∈[qnm​i​n,qnm​a​x]b\_{n}\in[q\_{n}^{min},q\_{n}^{max}] used in the smooth bang-bang policy.

We address this by designing the following configurations, each derived from the smooth bang-bang policy by modifying one of the aspects listed above. Configuration C, however, involves changes in two aspects.

* •

  Configuration A: the neural network is used to compute bnb\_{n} only
* •

  Configuration B: the neural network is used to compute pnp\_{n} only
* •

  Configuration C: bnb\_{n} remains in [qnm​i​n,qnm​a​x][q\_{n}^{min},q\_{n}^{max}] as in the smooth bang-bang, while both bnb\_{n} and pnp\_{n} are computed according to the implementation [16](https://arxiv.org/html/2601.18686v1#S3.E16 "In 3.2 The network strategy ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") of the network policy.
* •

  Configuration D: bnb\_{n} and pnp\_{n} are computed using the piecewise linear function as in the smooth bang-bang, but bn∈[vnm​i​n,vnm​a​x]b\_{n}\in[v\_{n}^{min},v\_{n}^{max}]

Table [5](https://arxiv.org/html/2601.18686v1#S3.T5 "Table 5 ‣ 3.3 Smooth Bang-Bang vs Network ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") summarizes the characteristics of the configurations and presents the results they achieve. For clarity, a dash (-) indicates that the feature in the column is implemented as in the smooth bang-bang policy, while fϕf\_{\phi} denotes the use of a neural network.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Strategy | bnb\_{n} | pnp\_{n} | bn∈b\_{n}\in | E​S0.75ES\_{0.75} | δf​a​i​r\delta^{fair} | δi​n​d\delta^{ind} |
| Smooth Bang-Bang | - | - | [bnm​i​n, ​bnm​a​x][b\_{n}^{min},\text{ }b\_{n}^{max}] | −94.0-94.0 | 156.5156.5 | 82.182.1 |
| Network | fϕf\_{\phi} | fϕf\_{\phi} | [vnm​i​n, ​vnm​a​x][v\_{n}^{min},\text{ }v\_{n}^{max}] | −136.8-136.8 | 167.4167.4 | 114.6114.6 |
| Config. A | fϕf\_{\phi} | - | [bnm​i​n, ​bnm​a​x][b\_{n}^{min},\text{ }b\_{n}^{max}] | −103.3-103.3 | 156.3156.3 | 87.787.7 |
| Config. B | - | fϕf\_{\phi} | [bnm​i​n, ​bnm​a​x][b\_{n}^{min},\text{ }b\_{n}^{max}] | −97.8-97.8 | 161.4161.4 | 83.783.7 |
| Config. C | fϕf\_{\phi} | fϕf\_{\phi} | [bnm​i​n, ​bnm​a​x][b\_{n}^{min},\text{ }b\_{n}^{max}] | −105.5-105.5 | 156.7156.7 | 89.389.3 |
| Config. D | - | - | [vnm​i​n, ​vnm​a​x][v\_{n}^{min},\text{ }v\_{n}^{max}] | −47.3-47.3 | 133.0133.0 | 40.240.2 |

Table 5: Expected shortfall and benchmark discounts for configurations A–D, expressed in basis points. A dash (-) indicates that the feature in the column is implemented as in the smooth bang-bang, using a piecewise linear function. Neural networks are indicated by fϕf\_{\phi}, whose architecture is the one adopted for the network policy, except for the last layer for configurations A and B, which has only one neuron.

Table [5](https://arxiv.org/html/2601.18686v1#S3.T5 "Table 5 ‣ 3.3 Smooth Bang-Bang vs Network ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") suggests that the performance improvement arises from the interaction of multiple components rather than from any single modification. Among the configurations, using a neural network to compute bnb\_{n}, configuration A, produces the largest individual effect. Nevertheless, this enhancement alone is insufficient to match the performance of the network policy. When the network is also employed to estimate pnp\_{n}, configuration C, the model shows further improvement, whereas configuration B performs comparably to the smooth bang-bang baseline. These results indicate a clear synergistic effect: joint learning of both bnb\_{n} and pnp\_{n} yields better outcomes than optimizing either component separately, and the gains of the network policy cannot be attributed to a single factor.

Furthermore, although configuration D performs noticeably worse, redefining [qnmin, ​qnmax][q\_{n}^{\min},\text{ }q\_{n}^{\max}] into [vnmin, ​vnmax][v\_{n}^{\min},\text{ }v\_{n}^{\max}] contributes to performance enhancement when the repurchases and exercise probabilities are parametrized by networks, as configuration C does not equal the network strategy. This may be explained by the limited information contained in the ratio SnAn\frac{S\_{n}}{A\_{n}}, which appears to be insufficient to exploit the broader range allowed for bnb\_{n}. The inclusion of additional state variables via neural networks enables the model to fully leverage the expanded flexibility.

## 4 ASR Hedging

### 4.1 Sequential and Joint Hedging

We now turn to mitigate the exposure on the underlying by introducing the sequential hedging model, whose purpose is to apply the framework proposed in [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")] and to assess whether it remains effective when used for ASR contracts.

For this reason, a first simplified approach is fixing the repurchase behavior. The financial institution first optimizes the execution of the repurchase as done in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). Once fixed the optimal set of parameters ϕ\phi, the second steps consists on training the set of weights θ\theta.

However, this approach consists of two optimization steps that are handled independently, leading to potential suboptimal outcomes. In the first stage, the executor of the program determines the optimal repurchase policy by minimizing the risk measure ρ\rho, thereby selecting a specific trade-off between profit and risk. In the second stage, however, part of the residual risk is hedged away. As a consequence, the policy chosen in the first step may be overly conservative: the agent might prefer a more aggressive repurchase strategy if it could anticipate that some of the risk would later be mitigated.

This limitation becomes evident from Figure [2](https://arxiv.org/html/2601.18686v1#S3.F2 "Figure 2 ‣ 3.3 Smooth Bang-Bang vs Network ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). The payoff distributions are strictly positive, reflecting the agent’s attempt to minimize losses during the first optimization stage. However, a more permissive policy, which tolerates a heavier left tail, might be optimal once the subsequent hedging step is taken into account, since part of the downside risk would eventually be neutralized.

These considerations motivate the introduction of the joint model, where the execution of the ASR and the hedging strategy are optimized simultaneously, which may lead to a more efficient policy. The bank thus faces the full control problem ([11](https://arxiv.org/html/2601.18686v1#S2.E11 "In 2.5 Problem Relaxation ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.")), described in detail in Section [2](https://arxiv.org/html/2601.18686v1#S2 "2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").

We now detail the implementation of the architecture for hedging. The value of hnh\_{n} is computed by the neural network fθf\_{\theta}, which has a linear activation on the last layer, allowing hn∈ℝh\_{n}\in\mathbb{R} since no constraints are imposed on the hedging portfolio:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hn=λ⋅fθ​(n−NM​i​nNM​i​n, ​SnAn, ​Wn−1WM​i​n)∀n∈𝒯∖{NM​a​x},h\_{n}=\lambda\cdot f\_{\theta}\left(\frac{n-N\_{Min}}{N\_{Min}},\text{ }\frac{S\_{n}}{A\_{n}},\text{ }\frac{W\_{n-1}}{W\_{Min}}\right)\quad\forall n\in\mathcal{T}\setminus\{N\_{Max}\}, |  | (21) |

with λ=(WM​i​n+WM​a​x)/(S0⋅(NM​i​n+NM​a​x))\lambda=(W\_{Min}+W\_{Max})/(S\_{0}\cdot(N\_{Min}+N\_{Max})).

The non-trainable multiplier λ\lambda plays a crucial role from a numerical perspective, as it ensures that all quantities, and, more importantly, their gradients, enter the model at a comparable order of magnitude. The volumes involved in ASR transactions are typically very large, which can overshadow variables operating on a smaller scale. In practice, we observed that, without the multiplier λ\lambda, P​n​LH​e​d​g​ePnL^{Hedge} is initially negligible compared to P​n​LA​S​RPnL^{ASR}, resulting in negligible gradients. Consequently, during training, the model learns to manage the ASR by optimizing the parameters ϕ\phi, while the weights θ\theta remain effectively untrained. This causes the training process to converge to a local minimum equivalent to optimizing only the ASR, as in the previous Section.

We turn to present the performance of our implementation on the contract described in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). The function fθf\_{\theta} consists of six layers. The first five layers each contain 150150 neurons and are followed by a ReLU activation function, while the final layer has a single neuron.

In particular, we first analyze the sequential model, which proves the effectiveness of the hedging framework for ASR. This is confirmed by the results shown table [6](https://arxiv.org/html/2601.18686v1#S4.T6 "Table 6 ‣ 4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."): when P​n​LnH​e​d​g​ePnL^{Hedge}\_{n} is included, both the expected shortfall and the mean-variance decrease, demonstrating the ability of the hedging portfolio to mitigate risk.

| Model | E​S0.75ES\_{0.75} | M​V2.5⋅102MV\_{2.5\cdot 10^{2}} |
| --- | --- | --- |
| Smooth Bang-Bang | −94.0-94.0 | −62.8-62.8 |
| Sequential Smooth Bang-Bang | −147.4-147.4 | −162.2-162.2 |
| Network | −136.8-136.8 | −161.1-161.1 |
| Sequential Network | −158.1-158.1 | −174.5-174.5 |

Table 6: Risk measures for the sequential models hedging the smooth bang-bang and the network policies, expressed in basis points.

The impact of the sequential hedging model is more pronounced on the benchmark smooth bang-bang policy, whose risk measures show a larger reduction compared to those obtained with the network policy. This can be attributed to the fact that, as illustrated in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), the network strategies not only increase the contract’s value but also produce a more peaked distribution, thereby already embedding some degree of protection.

The positive impact of the hedging portfolio is further confirmed by the values of the offered discounts on the benchmark price, which align with the indications provided by the risk measures.

| Model | δf​a​i​r\delta^{fair} | δi​n​d\delta^{ind} | δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind} |
| --- | --- | --- | --- |
| Smooth Bang-Bang | 156.5156.5 | 82.182.1 | 74.474.4 |
| Sequential Smooth Bang-Bang | 156.5156.5 | 126.5126.5 | 30.030.0 |
| Network | 167.4167.4 | 114.6114.6 | 52.852.8 |
| Sequential Network | 167.4167.4 | 132.4132.4 | 35.035.0 |

Table 7: Fair and indifference discounts for the sequential models hedging the smooth bang-bang and the network policies, expressed in basis points.

The increase in the indifference discount δi​n​d\delta^{ind}, for both strategies, confirms that the hedging framework detailed in [[5](https://arxiv.org/html/2601.18686v1#bib.bib7 "Deep hedging")] can be successfully applied to ASR, producing tangible performance improvements. Although the network model still outperforms the baseline, the addition of the hedging portfolio narrows the gap δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind}, making it comparable to, and, in fact, slightly better than, that of the network policy.

It is worth noting that the fair discount δf​a​i​r\delta^{fair} remains unchanged when considering the sequential models, as it depends solely on P​n​LτA​S​RPnL^{ASR}\_{\tau}, which is unaffected once the repurchase strategy has been fixed. Consequently, the distributions of P​n​LτA​S​RPnL^{ASR}\_{\tau} for any given policy and its associated sequential hedging are identical and remain the same as those presented in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). We show in Figure [3](https://arxiv.org/html/2601.18686v1#S4.F3 "Figure 3 ‣ 4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") the distribution of P​n​Lτ=P​n​LτA​S​R+P​n​LτH​e​d​g​ePnL\_{\tau}=PnL^{ASR}\_{\tau}+PnL^{Hedge}\_{\tau}:

![Refer to caption](Section4/seqSmoothVSseqNetwork.png)


Figure 3: Payoff distribution for the sequential model applied to the smooth bang-bang and network policies. The payoff P​n​L=P​n​LA​S​R+P​n​LH​e​d​g​ePnL=PnL^{ASR}+PnL^{Hedge} is normalized by WM​i​nW\_{Min} and expressed in basis points.

As is evident from the figure, the two sequential models exhibit similar distributions, even if for the smooth bang-bang it is slightly more peaked, indicating that the hedging framework achieves comparable final results. This is further supported by the similar values of E​S0.75ES\_{0.75}, M​V2.5⋅102MV\_{2.5\cdot 10^{2}}, and δi​n​d\delta^{ind}. The advantage of the network policy can be attributed to its superior performance in managing the contract, as reflected in the higher δf​a​i​r\delta^{fair}.

We now analyze the results obtained from the joint hedging models, showing the distribution of P​n​LτA​S​RPnL^{ASR}\_{\tau}, excluding P​n​LτH​e​d​g​ePnL^{Hedge}\_{\tau}, as it provides crucial insights. We compare the histogram of the ASR payoff obtained without hedging the repurchase program with the one obtained under joint hedging. In the former case, the agent does not assume that hedging will occur and therefore must search for a trade-off between profit and risk. Specifically, the resulting distribution is the one presented in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), identical to the sequential approach in which the repurchase implementation has been fixed. This comparison allows us to assess whether the possibility of taking risks that will ultimately be hedged away enables the bank to enhance profitability.

Figure [4](https://arxiv.org/html/2601.18686v1#S4.F4 "Figure 4 ‣ 4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") refers to the smooth bang-bang policy. The light-blue distribution, obtained when the bank jointly manages the repurchase and its associated risks, displays a heavier left tail, which can be offset through the portfolio that generates P​n​LτH​e​d​g​ePnL^{Hedge}\_{\tau}. At the same time, the overall distribution becomes less peaked and the right tail is more pronounced. In other words, the joint framework allows for a more flexible and permissive approach to ASR execution. Nevertheless, the values of P​n​LτA​S​RPnL^{ASR}\_{\tau} remain strictly positive, and the increase in the mean value is modest, rising from 180.9180.9 bps to 182.8182.8 bps.

![Refer to caption](Section4/ASRsmoothVSjointSmooth.png)


Figure 4: Distribution of P​n​LA​S​RPnL^{ASR}: in orange it is represented the smooth bang-bang in absence of the hedging portfolio, as in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). In light-blue is represented the joint hedging model. The payoff is normalized by WM​i​nW\_{Min} and expressed in basis points.

Figure [5](https://arxiv.org/html/2601.18686v1#S4.F5 "Figure 5 ‣ 4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), related to the network policy, shows similar effects, but on a larger scale. The distribution becomes significantly flatter, and the left tail now includes negative values. This can be interpreted as a consequence of the greater flexibility provided by the policy itself, which enables the agent to execute repurchases much more aggressively. This is also reflected in the increase in the mean value, which rises from 196.8196.8 bps to 208.1208.1 bps.

![Refer to caption](Section4/ASRnetVSjointNet.png)


Figure 5: Distribution of P​n​LA​S​RPnL^{ASR}: in orange it is represented the network policy in absence of the hedging portfolio, as in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). In light-blue is represented the joint hedging model. The payoff is normalized by WM​i​nW\_{Min} and expressed in basis points.

The tables below summarize the models considered so far, allowing us to assess the effectiveness of the overall framework. As shown in the first two tables, corresponding to the expected shortfall and mean-variance optimizations, respectively, there are two clear directions along which the risk measures decrease.

The first is the horizontal direction: moving from left to right, the network policy consistently outperforms the corresponding model implemented with the smooth bang-bang. This relationship is partly expected, as the former is inherently more complex and relies on a substantially larger set of parameters. However, such added complexity must be justified by tangible improvements, which in practice can be evaluated through the discounts offered to the client.

The second direction of improvement is vertical: moving from top to bottom highlights the advantages of incorporating hedging either on its own or, more effectively, within a unified framework. Nevertheless, the magnitude of the reduction from the sequential to the joint hedging approach depends strongly on the underlying policy, as anticipated by Figures [4](https://arxiv.org/html/2601.18686v1#S4.F4 "Figure 4 ‣ 4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") and [5](https://arxiv.org/html/2601.18686v1#S4.F5 "Figure 5 ‣ 4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). The smooth bang-bang strategy exhibits only a modest decrease, indicating that handling the repurchase and the hedging components jointly does not significantly affect its performance. In contrast, the network policy benefits considerably from an integrated workflow; its greater flexibility leads to a pronounced improvement when both tasks are optimized simultaneously.

| E​S0.75ES\_{0.75} | Smooth Bang-Bang | Network policy |
| --- | --- | --- |
| No Hedging | −94.0-94.0 | −136.8-136.8 |
| Sequential Hedging | −147.4-147.4 | −158.1-158.1 |
| Joint Hedging | −148.3-148.3 | −171.4-171.4 |

Table 8: Expected shortfall for the all hedging models with the smooth bang-bang and the network policies, expressed in basis points. The No Hedging values are those presented in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").



| M​V2.5⋅102MV\_{2.5\cdot 10^{2}} | Smooth Bang-Bang | Network policy |
| --- | --- | --- |
| No Hedging | −62.8-62.8 | −161.1-161.1 |
| Sequential Hedging | −162.2-162.2 | −174.5-174.5 |
| Joint Hedging | −171.6-171.6 | −195.7-195.7 |

Table 9: Mean-variance for the all the hedging models with the smooth bang-bang and the network policies, expressed in basis points. The No Hedging values are those presented in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").

We now turn to the pricing system based on discounts on the benchmark price. The joint hedging model increases the fair discount δf​a​i​r\delta^{fair} for both ASR strategies compared to the sequential approach. As discussed above, this improvement comes from the model’s ability to mitigate risk: by hedging effectively, the agent can afford to take on additional exposure while repurchasing shares in the market. This greater freedom allows for a more aggressive execution, ultimately leading to higher profitability.

| δf​a​i​r\delta^{fair} | Smooth Bang-Bang | Network policy |
| --- | --- | --- |
| No Hedging | 156.5156.5 | 167.4167.4 |
| Sequential Hedging | 156.5156.5 | 167.4167.4 |
| Joint Hedging | 160.8160.8 | 175.3175.3 |

Table 10: Fair discount for the all the hedging models with the smooth bang-bang and the network policies, expressed in basis points. The No Hedging values are those presented in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").

The indifference discount δi​n​d\delta^{ind} follows the same pattern: even when the product is priced incorporating the actual risk faced by the bank through the risk measure ρ\rho, the joint models achieve superior performance, allowing the bank to offer a higher sustainable discount.

Further insights emerge when comparing the two ASR strategies, third column of Table [11](https://arxiv.org/html/2601.18686v1#S4.T11 "Table 11 ‣ 4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). Although the sequential model narrows the difference in indifference discounts, this gap widens once the optimization becomes unified. This confirms our initial intuition: a more flexible policy benefits to a greater extent from a unified optimization process, as the potential to establish a dependence between the two components of the final payoff can be fully realized only if the agent is able to adapt its execution. However, this requires the ability to incorporate and exploit a richer representation of the state space.

| δi​n​d\delta^{ind} | Smooth Bang-Bang | Network policy | Difference |
| --- | --- | --- | --- |
| No Hedging | 82.182.1 | 114.6114.6 | 32.532.5 |
| Sequential Hedging | 126.5126.5 | 132.4132.4 | 5.95.9 |
| Joint Hedging | 127.1127.1 | 142.3142.3 | 15.215.2 |

Table 11: Indifference discount for the all the hedging models with the smooth bang-bang and the network policies, expressed in basis points. The No Hedging values are those presented in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").

We conclude by examining the gap between the optimal theoretical hedging performance and the realized one, measured by δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind}. As previously discussed, the sequential hedging model reduces this gap, yielding comparable values for the two ASR strategies. However, the joint model does not significantly alter the situation, leaving δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind} essentially unchanged. In our view, this is due to the fact that the hedging network architecture is the same across models and therefore has the same computational capacity, limiting the achievable improvement in this dimension.

| δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind} | Smooth Bang-Bang | Network policy |
| --- | --- | --- |
| No Hedging | 74.474.4 | 52.852.8 |
| Sequential Hedging | 30.030.0 | 35.035.0 |
| Joint Hedging | 33.733.7 | 33.033.0 |

Table 12: Difference in discounts for the all the hedging models with the smooth bang-bang and the network policies, expressed in basis points. The No Hedging values are those presented in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").

In conclusion, we can answer positively one of the key questions underlying this work: a unified framework is indeed advantageous for the financial institution, and this advantage becomes increasingly evident as the implementation becomes more flexible. The two plots below show the overall improvement by representing P​n​LτA​S​RPnL^{ASR}\_{\tau} for the policies presented in Section 3 and P​n​Lτ=P​n​LτA​S​R+P​n​LτH​e​d​g​ePnL\_{\tau}=PnL^{ASR}\_{\tau}+PnL^{Hedge}\_{\tau} for the joint models. For the smooth bang-bang:

![Refer to caption](Section4/smoothVSjointSmooth.png)


Figure 6: Distribution of P​n​L=P​n​LA​S​R+P​n​LH​e​d​g​ePnL=PnL^{ASR}+PnL^{Hedge}: in orange it is represented the smooth bang-bang in absence of the hedging portfolio, as in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). In light-blue is represented the joint hedging model. The payoff is normalized by WM​i​nW\_{Min} and expressed in basis points.

while the netowrk one yields:

![Refer to caption](Section4/netVSjointNet.png)


Figure 7: Distribution of P​n​L=P​n​LA​S​R+P​n​LH​e​d​g​ePnL=PnL^{ASR}+PnL^{Hedge}: in orange it is represented the network in absence of the hedging portfolio, as in Section [3](https://arxiv.org/html/2601.18686v1#S3 "3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."). In light-blue is represented the joint hedging model. The payoff is normalized by WM​i​nW\_{Min} and expressed in basis points.

### 4.2 Hedging Constraints

In the final stage of our analysis, we develop a model that incorporates the full set of constraints [1](https://arxiv.org/html/2601.18686v1#S2.E1 "In 2.2 Term Sheet ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") described in Section 2.2. Since the second limitation determines a dependence between the repurchase activity and its associated hedge, it is natural to build upon the joint hedging framework, as the policy can adapt optimally to the contract’s clauses.

Unlike in previous models, the number of shares hnh\_{n} held at time tnt\_{n} can no longer take values in ℝ\mathbb{R}. Instead, it is restricted to the interval:

|  |  |  |
| --- | --- | --- |
|  | hn∈[hn−1−(ν¯nh−bn), ​hn−1+ν¯nh−bn]=ℐnh∀n∈𝒯∖{NM​a​x}.h\_{n}\in[h\_{n-1}-(\overline{\nu}\_{n}^{h}-b\_{n}),\text{ }h\_{n-1}+\overline{\nu}\_{n}^{h}-b\_{n}]=\mathcal{I}\_{n}^{h}\quad\forall n\in\mathcal{T}\setminus\{N\_{Max}\}. |  |

This condition is achieved by capping the output of the hedging network hnh\_{n} to ℐnh\mathcal{I}\_{n}^{h}:

|  |  |  |
| --- | --- | --- |
|  | hn=min⁡(hn−1+ν¯nh−bn, ​max⁡(hn−1−(ν¯nh−bn), ​hn∗)),h\_{n}=\min\left(h\_{n-1}+\overline{\nu}\_{n}^{h}-b\_{n},\text{ }\max\left(h\_{n-1}-(\overline{\nu}\_{n}^{h}-b\_{n}),\text{ }h\_{n}^{\*}\right)\right), |  |

|  |  |  |
| --- | --- | --- |
|  | wherehn∗=λ⋅fθ​(n−NM​i​nNM​i​n, ​SnAn, ​Wn−1WM​i​n)andλ=WM​i​n+WM​a​xS0⋅(NM​i​n+NM​a​x).\text{where}\quad h\_{n}^{\*}=\lambda\cdot f\_{\theta}\left(\frac{n-N\_{Min}}{N\_{Min}},\text{ }\frac{S\_{n}}{A\_{n}},\text{ }\frac{W\_{n-1}}{W\_{Min}}\right)\quad\text{and}\qquad\lambda=\frac{W\_{Min}+W\_{Max}}{S\_{0}\cdot(N\_{Min}+N\_{Max})}. |  |

The architecture of fθf\_{\theta} is the same of the previous section. As an alternative, one may use a bounded activation on the final layer, for example the sigmoid, and map the output to ℐnh\mathcal{I}\_{n}^{h}. However, our experiments suggest that this change in the architecture of fθf\_{\theta} leads to suboptimal outcomes.

We now present the numerical results. Similarly to the processes ν¯n​ and ​ν¯n\underline{\nu}\_{n}\text{ and }\overline{\nu}\_{n}, we consider constant values ν¯nh\overline{\nu}\_{n}^{h} over time, and we examine the scenarios corresponding to ν¯h∈{1.5⋅106, ​2⋅106, ​2.5⋅106}\overline{\nu}^{h}\in\{1.5\cdot 10^{6},\text{ }2\cdot 10^{6},\text{ }2.5\cdot 10^{6}\}. In the first scenario, ν¯h=ν¯\overline{\nu}^{h}=\overline{\nu}, resulting in identical upper bounds for bnb\_{n} and for the sum bn+|hn−hn−1|b\_{n}+|h\_{n}-h\_{n-1}|.

We consider the following three models, whose repurchase activity is delegated to the network policy:

* •

  the free hedging model, corresponding to the joint hedging formulation introduced earlier, in which hn∈ℝh\_{n}\in\mathbb{R}
* •

  the capped hedging model, where the value of hnh\_{n} is obtained by capping the output of the free model to the set ℐnh\mathcal{I}\_{n}^{h}. It is used to assess how an ex post implementation performs
* •

  the constrained hedging model, in which the optimization is performed under the constraint hn∈ℐnhh\_{n}\in\mathcal{I}\_{n}^{h}. The difference with respect to the capped model is that the capping mechanism is now applied at optimization time, allowing the agent to learn to behave optimally under the real trading capabilities.

We first compare the risk measures obtained by the constrained implementation. As shown in Table [13](https://arxiv.org/html/2601.18686v1#S4.T13 "Table 13 ‣ 4.2 Hedging Constraints ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."), the agent experiences worse outcomes in terms of risk when the additional constraints are imposed. The row ν¯h=+∞\overline{\nu}^{h}=+\infty corresponds to the free model.

| ν¯h\overline{\nu}^{h} | E​S0.75ES\_{0.75} | M​V2.5⋅102MV\_{2.5\cdot 10^{2}} |
| --- | --- | --- |
| 1.5⋅1061.5\cdot 10^{6} | −163.3-163.3 | −189.7-189.7 |
| 2⋅1062\cdot 10^{6} | −167.3-167.3 | −192.6-192.6 |
| 2.5⋅1062.5\cdot 10^{6} | −169.4-169.4 | −194.4-194.4 |
| +∞+\infty | −171.4-171.4 | −195.7-195.7 |

Table 13: Risk measures for the constrained hedging models, expressed in basis points. The free corresponds to ν¯h=+∞\overline{\nu}^{h}=+\infty.

Although the increased complexity of the intermediary’s task may directly contribute to the reduction in performance, additional factors may also play a role. We thus consider the expected shortfall and the discounts offered on the benchmark price for each value of ν¯h\overline{\nu}^{h}. We note that the value of δf​a​i​r\delta^{fair} is identical for the free and capped models, as they share the same repurchase strategy parameters ϕ\phi.

| ν¯h=1.5⋅106\overline{\nu}^{h}=1.5\cdot 10^{6} | E​S0.75ES\_{0.75} | δf​a​i​r\delta^{fair} | δi​n​d\delta^{ind} | δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind} |
| --- | --- | --- | --- | --- |
| Free | −171.4-171.4 | 175.3175.3 | 142.3142.3 | 33.033.0 |
| Capped | −127.7-127.7 | 175.3175.3 | 104.5104.5 | 70.870.8 |
| Constrained | −163.3-163.3 | 172.7172.7 | 135.8135.8 | 36.936.9 |

Table 14: Discount for free, capped and constrained hedging models for ν¯h=1.5⋅106\overline{\nu}^{h}=1.5\cdot 10^{6}, in bps



| ν¯h=2⋅106\overline{\nu}^{h}=2\cdot 10^{6} | E​S0.75ES\_{0.75} | δf​a​i​r\delta^{fair} | δi​n​d\delta^{ind} | δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind} |
| --- | --- | --- | --- | --- |
| Free | −171.4-171.4 | 175.3175.3 | 142.3142.3 | 33.033.0 |
| Capped | −163.7-163.7 | 175.3175.3 | 135.0135.0 | 40.340.3 |
| Constrained | −167.3-167.3 | 174.4174.4 | 139.1139.1 | 35.335.3 |

Table 15: Discount for free, capped and constrained hedging models for ν¯h=2⋅106\overline{\nu}^{h}=2\cdot 10^{6}, in bps.



| ν¯h=2.5⋅106\overline{\nu}^{h}=2.5\cdot 10^{6} | E​S0.75ES\_{0.75} | δf​a​i​r\delta^{fair} | δi​n​d\delta^{ind} | δf​a​i​r−δi​n​d\delta^{fair}-\delta^{ind} |
| --- | --- | --- | --- | --- |
| Free | −171.4-171.4 | 175.3175.3 | 142.3142.3 | 33.033.0 |
| Capped | −168.8-168.8 | 175.3175.3 | 139.7139.7 | 35.635.6 |
| Constrained | −169.4-169.4 | 174.9174.9 | 140.7140.7 | 34.234.2 |

Table 16: Discount for free, capped and constrained hedging models for ν¯h=2.5⋅106\overline{\nu}^{h}=2.5\cdot 10^{6}, in bps.

In general, the constrained model outperforms the capped in terms of both expected shortfall and indifference discount for all values of ν¯h\overline{\nu}^{h}. This shows that the agent can extract more value from the buyback if its strategy is optimized while considering trading constraints, rather than imposing them ex post.

Specifically, the improvement in performance of the constrained model becomes increasingly evident as the value of ν¯h\overline{\nu}^{h} decreases. The poor results of the capped implementation reported in Table [14](https://arxiv.org/html/2601.18686v1#S4.T14 "Table 14 ‣ 4.2 Hedging Constraints ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") highlight the inadequacy of enforcing the constraints only ex post. The indifference discount δi​n​d\delta^{ind} drops dramatically compared to δf​a​i​r\delta^{fair}, showing that the latter is a poor performance estimator when the agent operates under restricted capabilities. By contrast, as ν¯h\overline{\nu}^{h} increases, the performance gap decreases.

We present the distribution plots comparing the constrained and capped hedging models for ν¯h=1.5⋅106\overline{\nu}^{h}=1.5\cdot 10^{6}, value for which the two approaches differ the most. However, as ν¯h\overline{\nu}^{h} increases, the two implementation show similar distribution plots. Figure [8](https://arxiv.org/html/2601.18686v1#S4.F8 "Figure 8 ‣ 4.2 Hedging Constraints ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") reports the distribution of P​n​LτA​S​RPnL^{ASR}\_{\tau}. The constrained distribution, shown in orange, is bimodal. The right tale is heavier than the capped and, on the left tail, few are the paths in which the repurchase leads to a negative payoff. This may be a consequence of accounting for the actual limitations on the hedging activity at optimization time, which possibly pushes to the adoption of a more conservative approach.

Figure [9](https://arxiv.org/html/2601.18686v1#S4.F9 "Figure 9 ‣ 4.2 Hedging Constraints ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.") displays the distribution of the total profit and loss, P​n​Lτ=P​n​LτA​S​R+P​n​LτH​e​d​g​ePnL\_{\tau}=PnL^{ASR}\_{\tau}+PnL^{Hedge}\_{\tau}. When the constraint hn∈ℐhh\_{n}\in\mathcal{I}^{h} is imposed ex post, the capped model fails to fully eliminate the exposure, as evidenced by its heavier tails.

![Refer to caption](Section4/buybackConstrainedVSCapped.png)


Figure 8: Distribution of P​n​LA​S​RPnL^{ASR}: in orange it is represented the constrained model, while in light-blue the capped. The payoff is normalized by WM​i​nW\_{Min} and expressed in basis points.

![Refer to caption](Section4/constrainedVSCapped.png)


Figure 9: Distribution of P​n​L=P​n​LA​S​R+P​n​LH​e​d​g​ePnL=PnL^{ASR}+PnL^{Hedge}: in orange it is represented the constrained model, while in light-blue the capped. The payoff is normalized by WM​i​nW\_{Min} and expressed in basis points.

In conclusion, explicitly accounting for hedging constraints increases the complexity of the optimal control problem but provides a meaningful advantage, which is more evident when the agent has less trading capabilities.

## 5 Conclusion

In this work, we address the management of repurchase programs and their corresponding hedging through machine learning techniques, with a particular focus on neural networks. We examine a standard contract that incorporates features commonly found in the buyback market, such as the greenshoe on the notional amount, expressed in cash, and trading constraints.

The flexibility granted to the buyback executor allows us to capture all dependencies between the two activities, showing that a unified framework for both tasks yields substantial performance improvements. This can be effectively leveraged to address trading constraints that simultaneously affect both activities, providing a more realistic hedging approach, in the sense that the bank’s policy is optimized while accounting for actual trading capabilities.

Since policy evaluation is delegated to risk measures, as is standard in the literature, we rely on an alternative and more realistic indifference pricing approach that reflects the trading capacity. The results confirm the effectiveness of a joint optimization framework for simultaneously managing the product and its hedge, also when trading limitations are considered.

Several directions for future research arise from our analysis. The framework can be extended to incorporate exotic contractual features, such as cap and floor structures or performance-sharing mechanisms, which are often present in ASR agreements and pose challenges for standard techniques such as Bellman-based dynamic programming. Another promising avenue is the adoption of more realistic stochastic models, particularly those that include stochastic drivers for volatility, to better capture market dynamics and improve the robustness of the resulting policies.

## Disclaimer

The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.

## References

* [1]
  F. Allen and R. Michaely (2003)
  Payout policy.
  In Handbook of the Economics of Finance, G. M. Constantinides, M. Harris, and R. M. Stulz (Eds.),
  Vol. 1,  pp. 337–429.
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p1.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [2]
  J. Armstrong and G. Tatlow (2024)
  Deep gamma hedging.
  Note: arXiv preprint
  External Links: 2409.13567,
  [Link](https://arxiv.org/abs/2409.13567)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p11.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [3]
  B. Baldacci, P. Bergault, and O. Guéant (2024-08-14)
  Pricing and managing complex share buy-back contracts: an alternative to optimal control.
  Risk.
  Note: Published online
  External Links: [Link](https://www.risk.net/cutting-edge/7959784/pricing-and-managing-complex-share-buy-back-contracts-an-alternative-to-optimal-control)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p7.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.1](https://arxiv.org/html/2601.18686v1#S2.SS1.p4.6 "2.1 Mathematical Setting ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p8.9 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [4]
  A. Ben-Tal and M. Teboulle (2007)
  An old-new concept of convex risk measures: the optimized certainty equivalent.
  Mathematical Finance 17 (3),  pp. 449–476.
  External Links: [Document](https://dx.doi.org/10.1111/j.1467-9965.2007.00311.x)
  Cited by: [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p1.5 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [5]
  H. Buehler, L. Gonon, J. Teichmann, and B. Wood (2019)
  Deep hedging.
  Quantitative Finance 19 (8),  pp. 1271–1291.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2019.1571683)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p11.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§1](https://arxiv.org/html/2601.18686v1#S1.p7.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§1](https://arxiv.org/html/2601.18686v1#S1.p8.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.3](https://arxiv.org/html/2601.18686v1#S2.SS3.p7.5 "2.3 Profit and Loss ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p1.5 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p10.1 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p13.2 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p2.2 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p6.7 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p8.9 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p9.1 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.6](https://arxiv.org/html/2601.18686v1#S2.SS6.p6.5 "2.6 ASR Pricing ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§3.1](https://arxiv.org/html/2601.18686v1#S3.SS1.p5.7 "3.1 Smooth Bang-Bang Strategy ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§4.1](https://arxiv.org/html/2601.18686v1#S4.SS1.p1.1 "4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§4.1](https://arxiv.org/html/2601.18686v1#S4.SS1.p12.2 "4.1 Sequential and Joint Hedging ‣ 4 ASR Hedging ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [6]
  J. Cao, J. Chen, S. Farghadani, J. Hull, Z. Poulos, Z. Wang, and J. Yuan (2023)
  Gamma and vega hedging using deep distributional reinforcement learning.
  Frontiers in Artificial Intelligence 6.
  External Links: [Document](https://dx.doi.org/10.3389/frai.2023.1129370)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p11.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [7]
  J. Farre-Mensa, R. Michaely, and M. Schmalz (2014)
  Payout policy.
  Annual Review of Financial Economics 6 (1),  pp. 75–134.
  External Links: [Document](https://dx.doi.org/10.1146/annurev-financial-110613-034259)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p1.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [8]
  H. Föllmer and A. Schied (2002-09)
  Convex measures of risk and trading constraints.
  Finance and Stochastics 6,  pp. 429–447.
  External Links: [Document](https://dx.doi.org/10.1007/s007800200072)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p8.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [9]
  H. Föllmer and A. Schied (2016)
  Stochastic finance: an introduction in discrete time.
  4 edition, De Gruyter.
  External Links: [Document](https://dx.doi.org/10.1515/9783110463453),
  ISBN 9783110463453
  Cited by: [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p13.2 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [10]
  P. François, G. Gauthier, F. Godin, and C. O. Pérez-Mendoza (2025)
  Deep hedging with options using the implied volatility surface.
  Note: arXiv preprint
  External Links: 2504.06208,
  [Link](https://arxiv.org/abs/2504.06208)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p11.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [11]
  O. Guéant, I. Manziuk, and J. Pu (2020)
  Accelerated share repurchase and other buyback programs: what neural networks can bring.
  Quantitative Finance 20 (8),  pp. 1389–1404.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2020.1729397)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p10.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§1](https://arxiv.org/html/2601.18686v1#S1.p3.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§1](https://arxiv.org/html/2601.18686v1#S1.p7.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§1](https://arxiv.org/html/2601.18686v1#S1.p9.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.4](https://arxiv.org/html/2601.18686v1#S2.SS4.p15.2 "2.4 Control Problem Optimization ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§2.5](https://arxiv.org/html/2601.18686v1#S2.SS5.p2.3 "2.5 Problem Relaxation ‣ 2 The model ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§3.2](https://arxiv.org/html/2601.18686v1#S3.SS2.p2.1 "3.2 The network strategy ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§3.3](https://arxiv.org/html/2601.18686v1#S3.SS3.p11.1 "3.3 Smooth Bang-Bang vs Network ‣ 3 ASR Management ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [12]
  O. Guéant, J. Pu, and G. Royer (2015)
  Accelerated share repurchase: pricing and execution strategy.
  International Journal of Theoretical and Applied Finance 18 (3),  pp. 1–31.
  External Links: [Document](https://dx.doi.org/10.1142/S0219024915500193)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p10.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§1](https://arxiv.org/html/2601.18686v1#S1.p3.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [13]
  O. Guéant (2017)
  Optimal execution of accelerated share repurchase contracts with fixed notional.
  Journal of Risk 19 (5),  pp. 77–99.
  External Links: [Document](https://dx.doi.org/10.21314/JOR.2017.361)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p10.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers."),
  [§1](https://arxiv.org/html/2601.18686v1#S1.p3.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [14]
  H. Horikawa and K. Nakagawa (2024)
  Relationship between deep hedging and delta hedging: leveraging a statistical arbitrage strategy.
  Finance Research Letters 62,  pp. 105101.
  External Links: ISSN 1544-6123,
  [Document](https://dx.doi.org/10.1016/j.frl.2024.105101)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p11.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [15]
  S. Jaimungal, D. Kinzebulatov, and D. H. Rubisov (2017)
  Optimal accelerated share repurchases.
  Applied Mathematical Finance 24 (3),  pp. 216–245.
  External Links: [Document](https://dx.doi.org/10.1080/1350486X.2017.1374870)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p10.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [16]
  O. Mikkilä and J. Kanniainen (2023)
  Empirical deep hedging.
  Quantitative Finance 23 (1),  pp. 111–122.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2022.2136037),
  [Link](https://trepo.tuni.fi/handle/10024/222907)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p12.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [17]
  M. Miller and F. Modigliani (1961)
  Dividend policy, growth, and the valuation of shares.
  The Journal of Business 34,  pp. 411–433.
  External Links: [Document](https://dx.doi.org/10.1086/294442)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p1.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [18]
  K. Oya (2024)
  Deep hedging bermudan swaptions.
  Note: arXiv preprint
  External Links: 2411.10079,
  [Link](https://arxiv.org/abs/2411.10079)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p12.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").
* [19]
  R. Pickard, F. Wredenhagen, J. DeJesus, M. Schlener, and Y. Lawryshyn (2024)
  Hedging american put options with deep reinforcement learning.
  Note: arXiv preprint
  External Links: 2405.06774,
  [Link](https://arxiv.org/abs/2405.06774)
  Cited by: [§1](https://arxiv.org/html/2601.18686v1#S1.p12.1 "1 Introduction ‣ Optimal strategy and deep hedging for share repurchase programs1footnote 11footnote 1The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.").