---
authors:
- Giorgio Ferrari
- Tim Niclas Schütz
doc_id: arxiv:2603.02820v1
family_id: arxiv:2603.02820
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the
  Kim-Omberg Model
url_abs: http://arxiv.org/abs/2603.02820v1
url_html: https://arxiv.org/html/2603.02820v1
venue: arXiv q-fin
version: 1
year: 2026
---


Giorgio Ferraria,1
 and 
Tim Niclas Schütza,2

(Date: March 3, 2026)

###### Abstract.

In this paper, we study an intertemporal utility maximization problem in which an investor chooses consumption and portfolio strategies in the presence of a stochastic factor and a no-borrowing constraint. In the spirit of the Kim–Omberg model, the stochastic factor represents the excess return of the risky asset and follows an Ornstein–Uhlenbeck process, capturing the mean reversion of expected excess returns—a feature well supported by empirical evidence in financial markets. The investor seeks to maximize expected utility from consumption, subject to the constraint that wealth remains nonnegative at all times. To address the dynamic no-borrowing constraint, we use Lagrange duality to transform the primal problem into a singular control problem in the dual space. We then characterize the solution to the dual singular control problem via an auxiliary two-dimensional optimal stopping problem featuring stochastic volatility, and subsequently retrieve the primal value function as well as the optimal portfolio and consumption plans. Finally, a numerical study is conducted to derive economic and financial implications.

a Bielefeld University, Center for Mathematical Economics (IMW), Bielefeld (Germany).

1 E-mail: [giorgio.ferrari@uni-bielefeld.de](2603.02820v1/mailto:giorgio.ferrari@uni-bielefeld.de).
  
2 E-mail: [tim.schuetz@uni-bielefeld.de](2603.02820v1/mailto:tim.schuetz@uni-bielefeld.de).

Keywords:
optimal consumption and portfolio choice, Kim-Omberg model, no-borrowing constraint, singular stochastic control, optimal stopping, stochastic volatility.

AMS subject classification: 91G15, 91G30, 49N15, 90C39, 60G40, 93E20

## 1. Introduction

We study an infinite-horizon optimal consumption and investment problem in which an agent chooses how much to consume and how to allocate wealth in a financial market. The agent receives a constant stream of labor income and faces a no-borrowing constraint, meaning that wealth must remain nonnegative at all times. This rules out borrowing either in financial markets or against future labor income, so that all decisions must be financed by current resources.

Investment opportunities vary over time because the expected excess return of the risky asset is driven by a stochastic factor (βt)t(\beta\_{t})\_{t}. Empirical evidence (see, e.g., [[14](#bib.bib1 "Dividend yields and expected stock returns")] and [[37](#bib.bib5 "Mean reversion in stock prices: evidence and implications")]) suggests that expected excess returns are predictable and mean-reverting. Motivated by this finding, we model (βt)t(\beta\_{t})\_{t} as a mean-reverting Ornstein–Uhlenbeck process, following the so-called Kim–Omberg model introduced in [[27](#bib.bib17 "Dynamic nonmyopic portfolio behavior")]. Furthermore, we allow the Brownian motion driving this stochastic factor to be correlated with the Brownian motion driving the risky asset’s returns.

We derive optimal consumption and portfolio policies, as well as regularity results for the value function. As discussed in more detail below, this is achieved by means of a Lagrange duality approach, which allows us to connect the (primal) dynamic optimization problem with a no-borrowing constraint to a singular stochastic control problem. The latter is then analyzed through an auxiliary genuinely two-dimensional optimal stopping problem, in which one of the state variables exhibits stochastic volatility. In particular, we establish continuous differentiability of the optimal stopping problem’s value function and characterize the optimal stopping time in terms of an excess-return-dependent free boundary. These properties are then instrumental in obtaining the complete solution to the original optimal consumption and portfolio choice problem.

Methodology and Results. The no-borrowing constraint requires that the agent’s wealth (Xt)t(X\_{t})\_{t} remain nonnegative at all times, almost surely. Such a restriction affects the set of admissible consumption and portfolio choices and, when the agent’s optimization problem is addressed via dynamic programming, it complements the Hamilton–Jacobi–Bellman equation with an appropriate boundary condition.

Inspired by [[12](#bib.bib7 "Optimization of consumption with labor income")], [[22](#bib.bib20 "Labor income, borrowing constraints, and equilibrium asset prices")], and the more recent [[24](#bib.bib6 "The finite-horizon retirement problem with borrowing constraint: a zero-sum stopper vs. singular-controller game")], we instead adopt a duality-based approach to handle the no-borrowing constraint. Instead of enforcing Xt≥0X\_{t}\geq 0 dynamically at every point in time, we reformulate it as a single static budget constraint. This transformation is achieved by introducing a non-increasing, càdlàg process (Dt)t(D\_{t})\_{t} that acts as an endogenous dynamic Lagrange multiplier designed to ensure Xt≥0X\_{t}\geq 0 at all times t≥0t\geq 0 almost surely. This dual formulation allows us to express the problem in terms of an auxiliary process (Zt)t(Z\_{t})\_{t} rather than the wealth process itself. Consequently, the dual problem is recast as a two-dimensional singular control problem in the state variables (Zt,βt)t(Z\_{t},\beta\_{t})\_{t}, where (Zt)t=(ZtD)t(Z\_{t})\_{t}=(Z\_{t}^{D})\_{t} is controlled through the monotone control (Dt)t(D\_{t})\_{t}. Crucially, because the stochastic factor (βt)t(\beta\_{t})\_{t} directly drives the diffusion of the dual state, the system inherently features stochastic volatility. It is worth noticing that directly approaching the dynamic programming principle (Hamilton-Jacobi-Bellmann, HJB) equation related to the primal problem is particularly challenging in our setting, because of a non-geometric wealth dynamics due to the presence of labor income. As a matter of fact, in many classical settings, the wealth process is geometric, and the positivity of wealth is automatically guaranteed. In presence of power utility functions, this geometric structure also allows the value function to be scaled with wealth, reducing the HJB equation to a one-dimensional nonlinear ODE (see, e.g., [[32](#bib.bib47 "Lifetime portfolio selection under uncertainty: the continuous-time case")] and [[31](#bib.bib46 "Optimum consumption and portfolio rules in a continuous-time model")] for earlier works or the recent [[18](#bib.bib54 "A variational approach to portfolio choice")] and [[19](#bib.bib21 "Optimal investment and consumption in a stochastic factor model")]). In our setting, however, the usual scaling arguments break down, the no-borrowing constraint must be enforced explicitly, and a duality approach is needed (see also Remark [2.3](#S2.Thmtheorem3 "Remark 2.3. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") below).

A key methodological step in our analysis is relating the dual singular stochastic control problem to an equivalent two-dimensional optimal stopping problem–which inherits state variables featuring stochastic volatility–using probabilistic arguments. Through this approach, our main results provide a complete characterization of the investor’s optimal behavior under stochastic investment opportunities, labor income, and a binding no-borrowing constraint.

First, we establish that the auxiliary two-dimensional optimal stopping problem features a lower-semicontinuous free boundary β↦z∗​(β)\beta\mapsto z^{\*}(\beta) that strictly separates the continuation and stopping regions, thereby defining the optimal stopping time. We then prove that the stopping value function vv is locally Lipschitz continuous across the entire state space and infinitely differentiable within both the continuation region and the interior of the stopping region. This latter regularity result is obtained by showing that – despite the degeneracy of the second-order differential operator ℒ\mathcal{L} associated with the optimal stopping problem’s state process and the stochastic volatility of one state variable – Hörmander’s condition holds. Consequently, ℒ\mathcal{L} is hypoelliptic, and vv is a classical solution to the associated partial differential equation within the continuation region. Hörmander’s condition also has the important implication that the optimal stopping problem’s state process admits a smooth transition density. This, in turn, guarantees, via an application of a result in [[23](#bib.bib3 "Local times, optimal stopping and semimartingales")], that vv is continuously differentiable across the entire state space.

By connecting the optimal stopping problem back to the dual singular control problem, we show that the dual value function is precisely the integral of the stopping value function with respect to the first component of the state process. This critical relationship allows us to uniquely characterize the optimal singular control (Dt∗)t(D^{\*}\_{t})\_{t}, which is the minimal process (à la Skorokhod) that keeps the dual state process (Zt,βt)t(Z\_{t},\beta\_{t})\_{t} within the region {(z,β):z<z∗​(β)}\{(z,\beta):z<z^{\*}(\beta)\}. Finally, we prove that strong duality holds, demonstrating that the primal value function can be recovered from the dual value function, and vice versa. Using these results, we are then able to retrieve the optimal consumption plan (ct∗)t(c^{\*}\_{t})\_{t}, the optimal portfolio strategy (πt∗)t(\pi^{\*}\_{t})\_{t}, and the optimal wealth process (Xt∗)t(X^{\*}\_{t})\_{t}, which, as required, adheres to the dynamic no-borrowing constraint.

Economically, these mathematical results offer a clear interpretation of the system’s dynamics. The process (Dt∗)t(D^{\*}\_{t})\_{t} represents a shadow price, reflecting the marginal cost of relaxing the wealth constraint. When consumption increases significantly, it exerts pressure on the borrowing constraint as wealth depletes more quickly. To maintain feasibility, (Dt∗)t(D^{\*}\_{t})\_{t} adjusts downward, reflecting the reduced capacity to fund future consumption or investments. Concurrently, strong duality will imply that (ZtD∗)t(Z^{D^{\*}}\_{t})\_{t} represents the marginal value of an additional unit of wealth. As wealth becomes scarce and approaches zero, its marginal value naturally rises, causing (ZtD∗)t(Z^{D^{\*}}\_{t})\_{t} to increase. Specifically, as the wealth process approaches zero, the marginal value process (ZtD∗)t(Z^{D^{\*}}\_{t})\_{t} freely evolves upward until it hits the state-dependent free boundary z∗z^{\*}. Exactly at the point where (ZtD∗)t(Z^{D^{\*}}\_{t})\_{t} touches this boundary, the singular control (Dt∗)t(D^{\*}\_{t})\_{t} activates and decreases, pushing (ZtD∗)t(Z^{D^{\*}}\_{t})\_{t} downward. By the established strong duality, this reflection of the dual state corresponds precisely to the wealth process being reflected upward, preventing bankruptcy and ensuring that the no-borrowing constraint is strictly satisfied.

Related Literature. The study of optimal consumption and investment problems with labor income and no-borrowing constraints dates back to 1993, when [[22](#bib.bib20 "Labor income, borrowing constraints, and equilibrium asset prices")] developed a duality approach to study an individual’s optimal consumption and portfolio policy when borrowing against future labor income is limited. Similar to [[22](#bib.bib20 "Labor income, borrowing constraints, and equilibrium asset prices")], [[12](#bib.bib7 "Optimization of consumption with labor income")] addresses an optimal consumption problem for an agent facing stochastic labor income and a strict no-borrowing constraint. They also utilize a duality approach to transform the constrained problem into a solvable, unconstrained dual problem. The resulting optimal strategy is characterized as a singular control problem, where the agent’s actions near the wealth boundary (Xt=0X\_{t}=0) are described by a local time component. Crucially, the constrained optimal wealth is shown to be equivalent to the unconstrained wealth minus the value of an American put option, establishing a direct link between the portfolio problem and optimal stopping theory. However, while these earlier works include labor income and borrowing constraints, they do not feature a stochastic factor. Recent studies such as [[24](#bib.bib6 "The finite-horizon retirement problem with borrowing constraint: a zero-sum stopper vs. singular-controller game")] study optimal consumption, investment, and early retirement decisions for an agent under a finite-time horizon and a strict no-borrowing constraint against future labor income. Using the dual-martingale method, the problem is uniquely formulated as a two-person zero-sum game between a singular controller (managing the borrowing constraint) and a discretionary stopper (choosing the retirement time). The solution is governed by a min-max parabolic variational inequality that results in two time-varying free boundaries: one for optimal retirement and one for the active wealth binding constraint. While [[24](#bib.bib6 "The finite-horizon retirement problem with borrowing constraint: a zero-sum stopper vs. singular-controller game")] considers a related singular control structure, it again operates without a stochastic factor.

Optimal consumption and investment problems in the presence of a stochastic factor have also been widely studied. For example, [[33](#bib.bib26 "Optimal consumption and investment strategies with stochastic interest rates")] consider an optimal consumption problem involving stochastic interest rates, while [[20](#bib.bib24 "An optimal consumption problem for general factor models")] study a Merton consumption and portfolio problem with stochastic asset returns and volatilities (see also [[21](#bib.bib25 "Optimal consumption and investment problem using a power utility function under a general nonlinear stochastic factor model")]). Closely related to our work is the Kim-Omberg model [[27](#bib.bib17 "Dynamic nonmyopic portfolio behavior")], which studies the dynamic non-myopic portfolio behavior of an investor trading a risk-free and a risky asset, with expected excess returns following a mean-reverting Ornstein-Uhlenbeck process. Extending this framework to include intermediate consumption, [[40](#bib.bib48 "Portfolio and consumption decisions under mean-reverting returns: an exact solution for complete markets")] derives exact optimal portfolio and consumption rules. However, unlike our model, [[40](#bib.bib48 "Portfolio and consumption decisions under mean-reverting returns: an exact solution for complete markets")] assumes complete markets by driving both the asset return and the stochastic factor with the same Brownian motion, does not incorporate labor income, and enforces the non-negativity constraint on wealth only at the terminal time TT. Furthermore, [[18](#bib.bib54 "A variational approach to portfolio choice")] derive optimal consumption and investment policies in a complete market featuring a stochastic factor, modeled as a general scalar diffusion that drives investment opportunities. In their framework, the absence of labor income ensures that the wealth dynamics remain purely geometric. This in turn allows the value function to be scaled by wealth, thereby reducing the dimension of the HJB equation. Lastly, [[19](#bib.bib21 "Optimal investment and consumption in a stochastic factor model")] consider an optimal consumption and investment model with general stochastic factors. They address optimal investment and consumption for a power utility investor using an incomplete stochastic factor model on an infinite horizon and provide a complete characterization for a finite state space. When the factor follows a diffusion process, they develop a new theoretical framework to prove existence and bound the HJB solution, verifying models like the Heston model rigorously for the first time. Conversely to our approach, [[19](#bib.bib21 "Optimal investment and consumption in a stochastic factor model")] allows for general stochastic factors, including the Kim-Omberg setting, but assumes geometric wealth without labor income, which automatically enforces the non-negativity of wealth and crucially permits dimension reduction of the associated HJB equation.

In our analysis, the study of a stationary two-dimensional optimal stopping problem plays a crucial role. For optimal stopping problems involving multi-dimensional processes, the standard guess-and-verify approach is generally no longer applicable. This is because the free boundary separating the continuation and stopping regions is no longer a simple scalar threshold, but rather a complex curve or surface, making it practically infeasible to postulate a parameterized closed-form solution for both the value function and the boundary simultaneously. Consequently, a direct study of the problem’s value function and the corresponding variational inequality must be performed on a case-by-case basis via probabilistic methods and/or techniques from the theory of partial differential equations. Notable contributions in this direction, with applications ranging from optimal dividend distribution to public debt reduction and quickest detection, include [[4](#bib.bib45 "Optimal dividend payout under stochastic discounting")], [[5](#bib.bib32 "Optimal reduction of public debt under partial observation of the economic growth")], [[7](#bib.bib50 "On optimal stopping of multidimensional diffusions")], [[9](#bib.bib40 "Optimal boundary surface for irreversible investment with stochastic costs")], [[16](#bib.bib39 "On the optimal management of public debt: a singular stochastic control problem")], and [[25](#bib.bib49 "Quickest detection problems for Bessel processes")], among others.

A major mathematical hurdle in our analysis arises from the presence of the stochastic factor, which explicitly introduces stochastic volatility into the optimal stopping problem. Beyond our specific model, optimal stopping under stochastic volatility is known to be highly challenging in general. In standard problems driven by uniformly elliptic diffusions, the value function typically enjoys strong smoothing properties across the entire state space. However, stochastic volatility breaks uniform ellipticity, rendering the associated infinitesimal generator degenerate. This degeneracy makes it particularly challenging to establish the global regularity of the value function and to rigorously characterize the behavior of the free boundary. For example, comparison theorems for solutions to SDEs, which are usually employed in optimal stopping theory to show monotonicity of the optimal stopping boundary, are generally not helpful in settings with stochastic volatility. As a consequence, it is particularly difficult to provide fine smoothness properties of the optimal stopping problem’s value function.

Because of these severe analytical challenges, the overall body of literature addressing optimal stopping under stochastic volatility remains relatively sparse, with a few notable contributions. [[1](#bib.bib53 "Monotonicity of the value function for a two-dimensional optimal stopping problem")] proves, via purely probabilistic techniques, the monotonicity and continuity of the value function for an optimal stopping problem featuring stochastic volatility; [[17](#bib.bib51 "Superreplication in stochastic volatility models and optimal stopping")] discusses the superreplication of derivatives in a stochastic volatility model under the additional assumption that the volatility follows a bounded process; [[39](#bib.bib37 "American options exercise boundary when the volatility changes randomly")] considers a stochastic volatility model for the asset price underlying an American option, extending regularity results for the American put option price function and proving that the optimal exercise boundary is a decreasing function of the current volatility process realization. Finally, [[29](#bib.bib38 "Variational formulation of american option prices in the heston model")] provides an analytical characterization of the price function of an American option in Heston-type models using an approach based on variational inequalities, while [[28](#bib.bib2 "Properties of the american price function in the heston-type models")] studies important properties of the American option price in the stochastic volatility Heston model, including monotonicity and smoothness of the value function, as well as its early-exercise-premium representation.

Structure of the Paper. The rest of the paper is organized as follows. In Section [2](#S2 "2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we introduce the primal problem and show how the no-borrowing constraint can be transformed into a static budget constraint. Section [3](#S3 "3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") derives the associated dual problem using duality principles and obtains the corresponding singular control formulation. We also establish a probabilistic link between this singular control problem and an auxiliary optimal stopping problem, which is fully analyzed in Sections [3.2](#S3.SS2 "3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), [3.3](#S3.SS3 "3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") and [3.4](#S3.SS4 "3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"). Section [4](#S4 "4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") uses the dual formulation to recover the optimal consumption and investment strategies in the primal problem. Finally, we provide numerical illustrations in Section [5](#S5 "5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").

## 2. The Primal Problem

### 2.1. The Financial Market and the Agent’s Problem

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a complete probability space and denote by 𝔼​[⋅]\mathbb{E}[\cdot] the expectation under ℙ\mathbb{P}. Consider an agent whose goal is to maximize the intertemporal expected utility functional given by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t],\mathbb{E}\left[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})\,dt\right], |  |

where δ>0\delta>0 denotes the discount rate, and the utility function uu is of power type; that is,

|  |  |  |
| --- | --- | --- |
|  | u​(c)=c1−γ1−γ,u(c)=\frac{c^{1-\gamma}}{1-\gamma}, |  |

where γ>1\gamma>1 represents the agent’s risk aversion. This value of γ\gamma is supported by empirical evidence on individual time preferences. Numerous studies, such as those by [[6](#bib.bib28 "By force of habit: a consumption-based explanation of aggregate stock market behavior")] and [[30](#bib.bib27 "The equity premium: a puzzle")], document risk aversion rates well above 1 based on experimental and survey data. This behavior reflects strong present-biased preferences, which aligns with the assumption γ>1\gamma>1 in our model.
  
The market is described by the so-called Kim-Omberg model (see [[27](#bib.bib17 "Dynamic nonmyopic portfolio behavior")]), as it follows. The agent can invest in a risk-free asset with a risk-free rate r>0r>0 as well as a risky asset (St)t(S\_{t})\_{t} whose dynamics are given by

|  |  |  |
| --- | --- | --- |
|  | d​St=(r+βt)​St​d​t+σ​St​d​Wt,t>0,S0=s>0,dS\_{t}=(r+\beta\_{t})S\_{t}\,dt+\sigma S\_{t}\,dW\_{t},\quad t>0,\quad S\_{0}=s>0, |  |

where (Wt)t(W\_{t})\_{t} is a standard Brownian motion on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) generating the filtration (completed by ℙ​-null sets of​ℱ\mathbb{P}\text{-null sets of}\;\mathcal{F}) 𝔽W:=(ℱtW)t\mathbb{F}^{W}:=(\mathcal{F}\_{t}^{W})\_{t}, and σ>0\sigma>0 denotes the volatility of the risky asset. The expected return of the risky asset is μ​(βt):=r+βt\mu(\beta\_{t}):=r+\beta\_{t}, where the process (βt)t(\beta\_{t})\_{t} represents the expected excess return of (St)t(S\_{t})\_{t}. Asset pricing studies suggest that expected excess returns are predictable and tend to revert to their long-run mean (see [[14](#bib.bib1 "Dividend yields and expected stock returns")] and [[37](#bib.bib5 "Mean reversion in stock prices: evidence and implications")], among others). To capture this mean-reversion, we define (βt)t(\beta\_{t})\_{t} as

|  |  |  |
| --- | --- | --- |
|  | d​βt=κ​(β¯−βt)​d​t+σβ​d​Wtβ,t>0,β0=β∈ℝ,d\beta\_{t}=\kappa(\overline{\beta}-\beta\_{t})\,dt+\sigma\_{\beta}\,dW\_{t}^{\beta},\quad t>0,\quad\beta\_{0}=\beta\in\mathbb{R}, |  |

where κ>0\kappa>0 is the speed of mean reversion, β¯>0\overline{\beta}>0 is the equilibrium level, and σβ>0\sigma\_{\beta}>0 is the volatility of (βt)t(\beta\_{t})\_{t}. The standard Brownian motion (Wtβ)t(W^{\beta}\_{t})\_{t} on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) is correlated with (Wt)t(W\_{t})\_{t} with correlation parameter ρ∈[−1,1]\rho\in[-1,1], and generates the filtration (completed by ℙ​-null sets of​ℱ\mathbb{P}\text{-null sets of}\;\mathcal{F}) 𝔽Wβ:=(ℱtWβ)t\mathbb{F}^{W^{\beta}}:=(\mathcal{F}\_{t}^{W^{\beta}})\_{t}. Due to correlation, we may write, for t≥0t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | Wt=ρ​Wtβ+1−ρ2​Wt1,⟂,W\_{t}=\rho W^{\beta}\_{t}+\sqrt{1-\rho^{2}}W^{1,\perp}\_{t}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Wtβ=ρ​Wt+1−ρ2​Wt2,⟂,W^{\beta}\_{t}=\rho W\_{t}+\sqrt{1-\rho^{2}}W^{2,\perp}\_{t}, |  |

where the independent standard Brownian motions (Wt1,⟂)t(W^{1,\perp}\_{t})\_{t} and (Wt2,⟂)t(W^{2,\perp}\_{t})\_{t} are such that WW is independent of W2,⟂W^{2,\perp}, and WβW^{\beta} is independent of W1,⟂W^{1,\perp}. By definition, the excess return (βt)t(\beta\_{t})\_{t} reverts to its long-run average β¯\overline{\beta}.
  
The agent chooses a consumption plan (ct)t(c\_{t})\_{t}, with ct≥0c\_{t}\geq 0, and an investment strategy for the risky asset, denoted by (πt)t(\pi\_{t})\_{t}. Additionally, the agent receives a flow of constant labor income ℓ>0\ell>0. The agent’s wealth (Xt)t(X\_{t})\_{t} thus follows the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | d​Xt=(r​Xt+βt​πt−ct+ℓ)​d​t+σ​πt​d​Wt,t>0,dX\_{t}=\left(rX\_{t}+\beta\_{t}\pi\_{t}-c\_{t}+\ell\right)\,dt+\sigma\pi\_{t}\,dW\_{t},\quad t>0, |  |

with initial wealth X0=x>0X\_{0}=x>0.
  
As usual, we define the market price of risk as

|  |  |  |
| --- | --- | --- |
|  | θ​(βt):=μ​(βt)−rσ=βtσ,t≥0,\theta(\beta\_{t}):=\frac{\mu(\beta\_{t})-r}{\sigma}=\frac{\beta\_{t}}{\sigma},\quad t\geq 0, |  |

and we also introduce the process (ℋt)t(\mathcal{H}\_{t})\_{t}, which acts as a stochastic discount factor, as follows

|  |  |  |
| --- | --- | --- |
|  | ℋt:=exp⁡(−∫0t[r+12​βs2σ2]​𝑑s−∫0tβsσ​𝑑Ws),t≥0;\mathcal{H}\_{t}:=\exp\left(-\int\_{0}^{t}\left[r+\frac{1}{2}\frac{\beta\_{s}^{2}}{\sigma^{2}}\right]ds-\int\_{0}^{t}\frac{\beta\_{s}}{\sigma}\,dW\_{s}\right),\quad t\geq 0; |  |

equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | d​ℋt=−r​ℋt​d​t−βtσ​ℋt​d​Wt,t>0,ℋ0=1.d\mathcal{H}\_{t}=-r\mathcal{H}\_{t}\,dt-\frac{\beta\_{t}}{\sigma}\mathcal{H}\_{t}\,dW\_{t},\quad t>0,\quad\mathcal{H}\_{0}=1. |  |

We denote by 𝔽¯:=(ℱ¯t)t\bar{\mathbb{F}}:=(\bar{\mathcal{F}}\_{t})\_{t} the completed filtration jointly generated by WW and WβW^{\beta}, that is, 𝔽¯:=𝔽W∨𝔽β\bar{\mathbb{F}}:=\mathbb{F}^{W}\vee\mathbb{F}^{\beta}, and make the following standing assumption.

###### Assumption 2.1.

We assume κ​σ>σβ\kappa\sigma>\sigma\_{\beta}.

The requirement κ​σ>σβ\kappa\sigma>\sigma\_{\beta} in Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") implies (by the Novikov condition; see, e.g., Corollary 5.13 on p. 199 in [[26](#bib.bib29 "Brownian motion and stochastic calculus")]) that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | Mt:=exp⁡(−∫0t12​βs2σ2​𝑑s−∫0tβsσ​𝑑Ws)=er​t​ℋtM\_{t}:=\exp\bigg(-\int\_{0}^{t}\frac{1}{2}\frac{\beta\_{s}^{2}}{\sigma^{2}}ds-\int\_{0}^{t}\frac{\beta\_{s}}{\sigma}\,dW\_{s}\bigg)=e^{rt}\mathcal{H}\_{t} |  |

is an 𝔽¯\bar{\mathbb{F}}- martingale under ℙ\mathbb{P}, with (ℋt)t(\mathcal{H}\_{t})\_{t} as in ([2.2](#S2.E2 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).
  
The agent faces a no-borrowing constraint; that is, Xt≥0X\_{t}\geq 0 ℙ\mathbb{P}-a.s. for all t≥0t\geq 0. This implies that the agent cannot borrow against future labor income and motivates the following definition of admissible controls.

###### Definition 2.2.

We call the pair of controls (π,c)(\pi,c) admissible if:

1. (1)

   (ct)t(c\_{t})\_{t} and (πt)t(\pi\_{t})\_{t} are 𝔽¯\bar{\mathbb{F}}-progressively measurable, and are such that ct≥0c\_{t}\geq 0 ℙ\mathbb{P}-a.s. for all t≥0t\geq 0, ∫0Tcs​𝑑s<∞\int\_{0}^{T}c\_{s}\,ds<\infty and ∫0Tπs2​𝑑s<∞\int\_{0}^{T}\pi\_{s}^{2}\,ds<\infty ℙ\mathbb{P}-a.s. for all T>0T>0.
2. (2)

   Xt≥0X\_{t}\geq 0 for all t≥0t\geq 0 ℙ\mathbb{P}-a.s.

We denote by 𝒜​(x)\mathcal{A}(x) the set of admissible controls.

The agent’s optimization problem then reads as

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | sup(π,c)∈𝒜​(x)𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t].\sup\_{(\pi,c)\in\mathcal{A}(x)}\mathbb{E}\left[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})\,dt\right]. |  |

###### Remark 2.3.

The recent [[19](#bib.bib21 "Optimal investment and consumption in a stochastic factor model")] treats a general stochastic-factor model (including the Kim–Omberg setting) but works in a geometric-wealth framework without labor income. This framework automatically ensures the nonnegativity of wealth and allows for a dimension reduction of the associated HJB equation. By contrast, since we consider total investment and consumption and explicitly include labor income, these simplifications are no longer available. Consequently, we adopt the duality–singular control–optimal stopping approach developed in the following sections.

### 2.2. From a Dynamic to a Static Budget Constraint

Following [[24](#bib.bib6 "The finite-horizon retirement problem with borrowing constraint: a zero-sum stopper vs. singular-controller game")] (see also [[12](#bib.bib7 "Optimization of consumption with labor income")] and [[22](#bib.bib20 "Labor income, borrowing constraints, and equilibrium asset prices")] for earlier studies), we now transform the dynamic budget constraint Xt≥0X\_{t}\geq 0 ℙ\mathbb{P}-a.s. ∀\forall t≥0t\geq 0 into a single, static budget constraint. To that end, we define

|  |  |  |  |
| --- | --- | --- | --- |
| (2.5) |  | 𝒟:={(Dt)t≥0:D​ is ​𝔽¯​-adapted, nonnegative, nonincreasing, càdlàg, and ​D0−=1​ℙ​-a.s.},\mathcal{D}:=\Big\{(D\_{t})\_{t\geq 0}:D\text{ is }\bar{\mathbb{F}}\text{-adapted, nonnegative, nonincreasing, càdlàg, and }D\_{0^{-}}=1\;\mathbb{P}\text{-a.s.}\Big\}, |  |

and we then have the following result.

###### Proposition 2.4.

1. (1)

   Let (ct)t(c\_{t})\_{t} be a consumption plan such that (π,c)∈𝒜​(x)(\pi,c)\in\mathcal{A}(x). Then it also satisfies the constraint

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (2.6) |  | supD∈𝒟𝔼​[∫0∞ℋt​Dt​(ct−ℓ)​𝑑t]≤x.\sup\_{D\in\mathcal{D}}\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)\,dt\right]\leq x. |  |

   Moreover, we have 𝔼​[∫0∞ℋt​|ct−ℓ|​𝑑t]<∞\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}|c\_{t}-\ell|\,dt\right]<\infty.
2. (2)

   For any nonnegative 𝔽¯\bar{\mathbb{F}}-progressively measurable (ct)t(c\_{t})\_{t} with ∫0Tcs​𝑑s<∞\int\_{0}^{T}c\_{s}\,ds<\infty ℙ\mathbb{P}-a.s. for all T>0T>0, and such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (2.7) |  | supD∈𝒟𝔼​[∫0∞ℋt​Dt​(ct−ℓ)​𝑑t]=x,\sup\_{D\in\mathcal{D}}\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)\,dt\right]=x, |  |

   there exists a process (πt)t(\pi\_{t})\_{t} such that (π,c)∈𝒜​(x)(\pi,c)\in\mathcal{A}(x).

###### Proof.

The proof borrows arguments from [[24](#bib.bib6 "The finite-horizon retirement problem with borrowing constraint: a zero-sum stopper vs. singular-controller game")].
  
*Proof of (1).* Let (ct)t(c\_{t})\_{t} be a consumption plan such that (π,c)∈𝒜​(x)(\pi,c)\in\mathcal{A}(x) and let D∈𝒟D\in\mathcal{D}. An application of Itô’s formula for semimartingales (see Theorem 32 on p. 78 in [[38](#bib.bib30 "Stochastic integration and differential equations")]) yields

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | d​(ℋt​Xt​Dt−)=ℋt​Dt​(ℓ−ct)​d​t+ℋt​Dt​(σ​πt−βtσ​Xt)​d​Wt+ℋt​Xt​d​Dt−.d(\mathcal{H}\_{t}X\_{t}D\_{t-})=\mathcal{H}\_{t}D\_{t}(\ell-c\_{t})dt+\mathcal{H}\_{t}D\_{t}(\sigma\pi\_{t}-\frac{\beta\_{t}}{\sigma}X\_{t})dW\_{t}+\mathcal{H}\_{t}X\_{t}dD\_{t-}. |  |

Next, we define the localizing sequence of stopping times

|  |  |  |
| --- | --- | --- |
|  | τn:=inf{s≥0:∫0sℋt2​Dt2​|σ​πt−βtσ​Xt|2​𝑑t≥n},n∈ℕ,\tau\_{n}:=\inf\bigg\{s\geq 0:\int\_{0}^{s}\mathcal{H}^{2}\_{t}D^{2}\_{t}\bigg|\sigma\pi\_{t}-\frac{\beta\_{t}}{\sigma}X\_{t}\bigg|^{2}dt\geq n\bigg\},\quad n\in\mathbb{N}, |  |

and note that τn→∞\tau\_{n}\rightarrow\infty a.s., as n→∞n\rightarrow\infty. Integrating ([2.8](#S2.E8 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and rearranging terms we find

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0τnℋs​Ds​(cs−ℓ)​𝑑s−x\displaystyle\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}D\_{s}(c\_{s}-\ell)ds-x | =∫0τnℋs​Ds​(σ​πs−βsσ​Xs)​𝑑Ws\displaystyle=\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}D\_{s}(\sigma\pi\_{s}-\frac{\beta\_{s}}{\sigma}X\_{s})dW\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0τnℋs​Xs​𝑑Ds−−ℋτn​Xτn​Dτn−,\displaystyle\quad+\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}X\_{s}dD\_{s-}-\mathcal{H}\_{\tau\_{n}}X\_{\tau\_{n}}D\_{\tau\_{n}-}, |  |

from which, by taking expectations,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[∫0τnℋs​Ds​(cs−ℓ)​𝑑s]−x\displaystyle\mathbb{E}\bigg[\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}D\_{s}(c\_{s}-\ell)ds\bigg]-x |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.9) |  |  | =𝔼​[∫0τnℋs​Ds​(σ​πs−βsσ​Xs)​𝑑Ws+∫0τnℋs​Xs​𝑑Ds−−ℋτn​Xτn​Dτn−]\displaystyle\qquad=\mathbb{E}\bigg[\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}D\_{s}(\sigma\pi\_{s}-\frac{\beta\_{s}}{\sigma}X\_{s})dW\_{s}+\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}X\_{s}dD\_{s-}-\mathcal{H}\_{\tau\_{n}}X\_{\tau\_{n}}D\_{\tau\_{n}-}\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0τnℋs​Ds​(σ​πs−βsσ​Xs)​𝑑Ws]⏟=0+𝔼​[∫0τnℋs​Xs​𝑑Ds−]⏟≤0−𝔼​[ℋτn​Xτn​Dτn−]⏟≥0\displaystyle\qquad=\underbrace{\mathbb{E}\bigg[\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}D\_{s}(\sigma\pi\_{s}-\frac{\beta\_{s}}{\sigma}X\_{s})dW\_{s}\bigg]}\_{=0}+\underbrace{\mathbb{E}\bigg[\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}X\_{s}dD\_{s-}\bigg]}\_{\leq 0}-\underbrace{\mathbb{E}\bigg[\mathcal{H}\_{\tau\_{n}}X\_{\tau\_{n}}D\_{\tau\_{n}-}\bigg]}\_{\geq 0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤0.\displaystyle\qquad\leq 0. |  |

Here we used the facts that ℋt≥0\mathcal{H}\_{t}\geq 0, Xt≥0X\_{t}\geq 0 since (π,c)∈𝒜​(x)(\pi,c)\in\mathcal{A}(x), and that DD is nonincreasing and nonnegative. Applying Fatou’s lemma for lower bounded functions, together with ([2.2](#S2.Ex12 "Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0∞ℋs​Ds​(cs−ℓ)​𝑑s]−x\displaystyle\mathbb{E}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{s}D\_{s}(c\_{s}-\ell)ds\bigg]-x | =𝔼​[lim infn→∞∫0τnℋs​Ds​(cs−ℓ)​𝑑s]−x\displaystyle=\mathbb{E}\bigg[\liminf\_{n\rightarrow\infty}\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}D\_{s}(c\_{s}-\ell)ds\bigg]-x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤lim infn→∞𝔼​[∫0τnℋs​Ds​(cs−ℓ)​𝑑s]−x≤0;\displaystyle\leq\liminf\_{n\rightarrow\infty}\mathbb{E}\bigg[\int\_{0}^{\tau\_{n}}\mathcal{H}\_{s}D\_{s}(c\_{s}-\ell)ds\bigg]-x\leq 0; |  |

hence,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0∞ℋt​Dt​(ct−ℓ)​𝑑t]≤x,\mathbb{E}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)dt\bigg]\leq x, |  |

and by arbitrariness of D∈𝒟D\in\mathcal{D}, we obtain ([2.6](#S2.E6 "In item 1 ‣ Proposition 2.4. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")); that is,

|  |  |  |
| --- | --- | --- |
|  | supD∈𝒟𝔼​[∫0∞ℋt​Dt​(ct−ℓ)​𝑑t]≤x.\sup\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)dt\bigg]\leq x. |  |

In particular, since 1∈𝒟1\in\mathcal{D}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0∞ℋt​(ct−ℓ)​𝑑t]≤x.\mathbb{E}\!\left[\int\_{0}^{\infty}\mathcal{H}\_{t}(c\_{t}-\ell)\,dt\right]\leq x. |  |

Using the fact that ℋt=e−r​t​Mt\mathcal{H}\_{t}=e^{-rt}M\_{t}, where (Mt)t(M\_{t})\_{t} is the martingale given by ([2.3](#S2.E3 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we also find

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0∞ℋt​ct​𝑑t]≤x+𝔼​[∫0∞e−r​t​ℓ​Mt​𝑑t]=x+ℓr,\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}c\_{t}\,dt\right]\leq x+\mathbb{E}\left[\int\_{0}^{\infty}e^{-rt}\ell M\_{t}\,dt\right]=x+\frac{\ell}{r}, |  |

and therefore,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.10) |  | 𝔼​[∫0∞ℋt​|ct−ℓ|​𝑑t]≤x+2​ℓr<∞.\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}|c\_{t}-\ell|\,dt\right]\leq x+\frac{2\ell}{r}<\infty. |  |

*Proof of (2).* For T>0T>0 arbitrary but fixed, consider now the reflected backward stochastic differential equation (RBSDE):

|  |  |  |  |
| --- | --- | --- | --- |
| (2.11) |  | {X~s=∫sTℋt​(ct−ℓ)​𝑑t−∫sTZ~t​𝑑Wt+∫sT𝑑K~t,∀s≥0,X~t≥0,∫0TX~t​𝑑K~t=0.\begin{cases}\tilde{X}\_{s}=\int\_{s}^{T}\mathcal{H}\_{t}(c\_{t}-\ell)\,dt-\int\_{s}^{T}\tilde{Z}\_{t}\,dW\_{t}+\int\_{s}^{T}d\tilde{K}\_{t},\quad\forall s\geq 0,\\ \tilde{X}\_{t}\geq 0,\quad\int\_{0}^{T}\tilde{X}\_{t}\,d\tilde{K}\_{t}=0.\end{cases} |  |

Following [[15](#bib.bib8 "L1 solutions of non-reflected BSDEs and reflected BSDEs with one and two continuous barriers under general assumptions")], an L1L^{1}-solution to ([2.11](#S2.E11 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is a triple (X~,Z~,K~)(\tilde{X},\tilde{Z},\tilde{K}) of 𝔽¯\bar{\mathbb{F}}-progressively measurable processes such that K~\tilde{K} is continuous and increasing with K~0=0\tilde{K}\_{0}=0 ℙ\mathbb{P}-a.s. and 𝔼​[K~T]<∞\mathbb{E}[\tilde{K}\_{T}]<\infty, X~\tilde{X} is continuous and belongs to Class D111A process (ζt)t(\zeta\_{t})\_{t} is of Class (D) if the family of random variables {ζτ:τ<∞​ℙ​-a.s. is a stopping time}\left\{\zeta\_{\tau}:\tau<\infty\;\mathbb{P}\text{-a.s.\ is a stopping time}\right\}
is uniformly integrable., ∫0TZ~t2​𝑑t<∞\int\_{0}^{T}\tilde{Z}^{2}\_{t}dt<\infty ℙ\mathbb{P}-a.s. for all T>0T>0, and for every ν∈(0,1)\nu\in(0,1), one has

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T]|X~t|ν]<∞and𝔼​[(∫0T|Z~t|2​𝑑t)ν/2]<∞.\mathbb{E}\left[\sup\_{t\in[0,T]}|\tilde{X}\_{t}|^{\nu}\right]<\infty\quad\text{and}\quad\mathbb{E}\left[\left(\int\_{0}^{T}|\tilde{Z}\_{t}|^{2}\,dt\right)^{\nu/2}\right]<\infty. |  |

Note that the driver of the RBSDE ([2.11](#S2.E11 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), namely ℋt​(ct−ℓ)\mathcal{H}\_{t}(c\_{t}-\ell), does not depend on Z~\tilde{Z} and X~\tilde{X}. Furthermore, due to ([2.10](#S2.E10 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we have for all T>0T>0

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0Tℋt​|ct−ℓ|​𝑑t]<∞.\mathbb{E}\left[\int\_{0}^{T}\mathcal{H}\_{t}|c\_{t}-\ell|\,dt\right]<\infty. |  |

Hence, by Theorem 5.1 in [[15](#bib.bib8 "L1 solutions of non-reflected BSDEs and reflected BSDEs with one and two continuous barriers under general assumptions")], there exists a unique L1L^{1}-solution (X~,Z~,K~)(\tilde{X},\tilde{Z},\tilde{K}) to ([2.11](#S2.E11 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).
  
Let then D∈𝒟D\in\mathcal{D} and define the sequence of localizing stopping times

|  |  |  |
| --- | --- | --- |
|  | ϑn:=inf{s≥0:∫0sZ~u2​Du2​𝑑u≥n},n∈ℕ.\vartheta\_{n}:=\inf\left\{s\geq 0:\int\_{0}^{s}\tilde{Z}\_{u}^{2}D\_{u}^{2}\,du\geq n\right\},\quad n\in\mathbb{N}. |  |

Note that ϑn→∞\vartheta\_{n}\to\infty ℙ\mathbb{P}-a.s. as n→∞n\to\infty. Using Itô’s formula on the interval [0,T∧ϑn][0,T\wedge\vartheta\_{n}] and taking expectations,
we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.12) |  | X~0\displaystyle\tilde{X}\_{0} | =𝔼​[X~T∧ϑn​DT∧ϑn+∫0T∧ϑnℋt​Dt​(ct−ℓ)​𝑑t]\displaystyle=\mathbb{E}\left[\tilde{X}\_{T\wedge\vartheta\_{n}}D\_{T\wedge\vartheta\_{n}}+\int\_{0}^{T\wedge\vartheta\_{n}}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)\,dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[∫0T∧ϑnDt−​𝑑K~t−∫0T∧ϑnX~t​𝑑Dt−].\displaystyle\quad+\mathbb{E}\left[\int\_{0}^{T\wedge\vartheta\_{n}}D\_{t-}\,d\tilde{K}\_{t}-\int\_{0}^{T\wedge\vartheta\_{n}}\tilde{X}\_{t}\,dD\_{t-}\right]. |  |

Since DD is decreasing and K~\tilde{K} is increasing, we have from ([2.12](#S2.E12 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))

|  |  |  |
| --- | --- | --- |
|  | X~0≥𝔼​[∫0T∧ϑnℋt​Dt​(ct−ℓ)​𝑑t],\tilde{X}\_{0}\geq\mathbb{E}\left[\int\_{0}^{T\wedge\vartheta\_{n}}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)\,dt\right], |  |

and letting n→∞n\to\infty and T→∞T\to\infty, ([2.10](#S2.E10 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) allows us to invoke the Dominated Convergence Theorem to obtain

|  |  |  |
| --- | --- | --- |
|  | X~0≥𝔼​[∫0∞ℋt​Dt​(ct−ℓ)​𝑑t].\tilde{X}\_{0}\geq\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)\,dt\right]. |  |

Since D∈𝒟D\in\mathcal{D} was arbitrary, it follows from ([2.7](#S2.E7 "In item 2 ‣ Proposition 2.4. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.13) |  | X~0≥x.\tilde{X}\_{0}\geq x. |  |

On the other hand, let

|  |  |  |
| --- | --- | --- |
|  | D~s:=𝟏{s<η~},s≥0,η~:=inf{s≥0:X~s≤0}∧(T∧ϑn).\tilde{D}\_{s}:=\mathbf{1}\_{\{s<\tilde{\eta}\}},\;s\geq 0,\quad\tilde{\eta}:=\inf\left\{s\geq 0:\tilde{X}\_{s}\leq 0\right\}\wedge(T\wedge\vartheta\_{n}). |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | X~η~​𝟏{η~<T∧ϑn}=0,K~t=0on0≤t<η~,\tilde{X}\_{\tilde{\eta}}\mathbf{1}\_{\{\tilde{\eta}<T\wedge\vartheta\_{n}\}}=0,\quad\tilde{K}\_{t}=0\quad\text{on}\quad 0\leq t<\tilde{\eta}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∫0T∧ϑnD~t−​𝑑K~t=∫0T∧ϑnX~t​𝑑D~t−=0,\int\_{0}^{T\wedge\vartheta\_{n}}\tilde{D}\_{t-}\,d\tilde{K}\_{t}=\int\_{0}^{T\wedge\vartheta\_{n}}\tilde{X}\_{t}\,d\tilde{D}\_{t-}=0, |  |

so that ([2.12](#S2.E12 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) implies

|  |  |  |  |
| --- | --- | --- | --- |
| (2.14) |  | X~0=𝔼​[X~T∧ϑn​D~T∧ϑn+∫0T∧ϑnℋt​D~t​(ct−ℓ)​𝑑t].\tilde{X}\_{0}=\mathbb{E}\left[\tilde{X}\_{T\wedge\vartheta\_{n}}\tilde{D}\_{T\wedge\vartheta\_{n}}+\int\_{0}^{T\wedge\vartheta\_{n}}\mathcal{H}\_{t}\tilde{D}\_{t}(c\_{t}-\ell)\,dt\right]. |  |

Since X~\tilde{X} belongs to the Class D, we have limn→∞𝔼​[X~T∧ϑn]=𝔼​[X~T]=0\lim\_{n\to\infty}\mathbb{E}\left[\tilde{X}\_{T\wedge\vartheta\_{n}}\right]=\mathbb{E}\left[\tilde{X}\_{T}\right]=0. Hence, using the Dominated Convergence Theorem again to take limits as n→∞n\rightarrow\infty and T→∞T\rightarrow\infty in ([2.14](#S2.E14 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (2.15) |  | X~0≤𝔼​[∫0∞ℋt​D~t​(ct−ℓ)​𝑑t]≤x,\tilde{X}\_{0}\leq\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}\tilde{D}\_{t}(c\_{t}-\ell)\,dt\right]\leq x, |  |

where we used the fact that D~∈𝒟\tilde{D}\in\mathcal{D}. Therefore, combining ([2.13](#S2.E13 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([2.15](#S2.E15 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we conclude that X~0=x\tilde{X}\_{0}=x.
  
From the RBSDE ([2.11](#S2.E11 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we know that X~\tilde{X} satisfies

|  |  |  |
| --- | --- | --- |
|  | 0≤X~s+∫0s𝑑K~t=x+∫0sℋt​(ℓ−ct)​𝑑t+∫0sZ~t​𝑑Wt,∀s≥0.0\leq\tilde{X}\_{s}+\int\_{0}^{s}d\tilde{K}\_{t}=x+\int\_{0}^{s}\mathcal{H}\_{t}(\ell-c\_{t})\,dt+\int\_{0}^{s}\tilde{Z}\_{t}\,dW\_{t},\quad\forall s\geq 0. |  |

If we now choose π\pi defined as

|  |  |  |  |
| --- | --- | --- | --- |
| (2.16) |  | πt:=1σ​ℋt​(Z~t+βtσ​Xtπ,c​ℋt),t≥0,\pi\_{t}:=\frac{1}{\sigma\mathcal{H}\_{t}}\left(\tilde{Z}\_{t}+\frac{\beta\_{t}}{\sigma}X^{\pi,c}\_{t}\mathcal{H}\_{t}\right),\quad t\geq 0, |  |

where (Xtπ,c)t(X^{\pi,c}\_{t})\_{t} is the wealth process controlled through (π,c)(\pi,c), we obtain for any s≥0s\geq 0

|  |  |  |
| --- | --- | --- |
|  | 0≤X~s+∫0s𝑑K~t=x+∫0sℋt​(ℓ−ct)​𝑑t+∫0sℋt​(σ​πt−βtσ​Xtπ,c)​𝑑Wt.0\leq\tilde{X}\_{s}+\int\_{0}^{s}d\tilde{K}\_{t}=x+\int\_{0}^{s}\mathcal{H}\_{t}(\ell-c\_{t})\,dt+\int\_{0}^{s}\mathcal{H}\_{t}\left(\sigma\pi\_{t}-\frac{\beta\_{t}}{\sigma}X^{\pi,c}\_{t}\right)\,dW\_{t}. |  |

We need to check that such a π\pi is indeed such that (π,c)∈𝒜​(x)(\pi,c)\in\mathcal{A}(x). Observe that the expression on the right-hand side of the last display equation is exactly the discounted wealth Xsπ,c​ℋsX^{\pi,c}\_{s}\mathcal{H}\_{s}. Since ℋs\mathcal{H}\_{s} is strictly positive for all s≥0s\geq 0, we thus get Xsπ,c≥0X^{\pi,c}\_{s}\geq 0 for all s≥0s\geq 0.
  
Let us now check that

|  |  |  |
| --- | --- | --- |
|  | ∫0Tπt2​𝑑t<∞ℙ−a.s.for all​T>0.\int\_{0}^{T}\pi\_{t}^{2}\,dt<\infty\quad\mathbb{P}-a.s.\ \text{for all}\;T>0. |  |

Since Xtπ,c=ℋt−1​(X~t+K~t)X\_{t}^{\pi,c}=\mathcal{H}\_{t}^{-1}(\tilde{X}\_{t}+\tilde{K}\_{t}), by substituting this expression into ([2.16](#S2.E16 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we find

|  |  |  |
| --- | --- | --- |
|  | πt=1σ​ℋt​(Z~t+βtσ​(X~t+K~t)).\pi\_{t}=\frac{1}{\sigma\mathcal{H}\_{t}}\left(\tilde{Z}\_{t}+\frac{\beta\_{t}}{\sigma}(\tilde{X}\_{t}+\tilde{K}\_{t})\right). |  |

As (ℋt)t(\mathcal{H}\_{t})\_{t}, (βt)t(\beta\_{t})\_{t}, (X~t)t(\tilde{X}\_{t})\_{t} and (K~t)t(\tilde{K}\_{t})\_{t} are continuous, these processes are ℙ\mathbb{P}-a.s. locally bounded. Furthermore, ∫0TZ~t2​𝑑t<∞\int\_{0}^{T}\tilde{Z}\_{t}^{2}dt<\infty ℙ\mathbb{P}-a.s. for all T>0T>0, by definition of the L1L^{1}-solution to ([2.11](#S2.E11 "In Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). Thus, ∫0Tπt2​𝑑t<∞\int\_{0}^{T}\pi\_{t}^{2}dt<\infty ℙ\mathbb{P}-a.s. for all T>0T>0, which implies (π,c)∈𝒜​(x)(\pi,c)\in\mathcal{A}(x).
∎

###### Remark 2.5.

Note that since 1∈𝒟1\in\mathcal{D}, we in particular have from Proposition [2.4](#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")-(1)(1)

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0∞ℋt​(ct−ℓ)​𝑑t]≤x.\mathbb{E}\left[\int\_{0}^{\infty}\mathcal{H}\_{t}(c\_{t}-\ell)\,dt\right]\leq x. |  |

This means that the present value of discounted consumption, net of labor income, cannot exceed the agent’s initial wealth. However, this condition alone does not guarantee that the wealth process remains nonnegative with probability one at all times. Therefore, we need a stronger requirement, which is achieved by using the processes DD as in Proposition [2.4](#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") above.

## 3. The Dual Problem as a Singular Control Problem

### 3.1. Derivation of the Dual Problem

In this section, we derive the dual problem expected to be associated to ([3.11](#S3.E11 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). Because (cf. ([2.6](#S2.E6 "In item 1 ‣ Proposition 2.4. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")))

|  |  |  |
| --- | --- | --- |
|  | supD∈𝒟𝔼​[∫0∞ℋt​Dt​(ct−ℓ)​𝑑t]≤x,\sup\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)dt\bigg]\leq x, |  |

with (ℋt)t(\mathcal{H}\_{t})\_{t} as in ([2.2](#S2.E2 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), for a given z>0z>0 we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t]\displaystyle\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})dt\bigg] | ≤𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t]+z​(x−supD∈𝒟𝔼​[∫0∞ℋt​Dt​(ct−ℓ)​𝑑t])\displaystyle\leq\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})dt\bigg]+z\bigg(x-\sup\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)dt\bigg]\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.1) |  |  | =𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t]+z​x+infD∈𝒟𝔼​[−∫0∞z​ℋt​Dt​(ct−ℓ)​𝑑t]\displaystyle=\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})dt\bigg]+zx+\inf\_{D\in\mathcal{D}}\mathbb{E}\bigg[-\int\_{0}^{\infty}z\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)dt\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =infD∈𝒟𝔼​[∫0∞e−δ​t​(u​(ct)−eδ​t​z​ℋt​Dt​(ct−ℓ))​𝑑t]+z​x.\displaystyle=\inf\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(u(c\_{t})-e^{\delta t}z\mathcal{H}\_{t}D\_{t}(c\_{t}-\ell)\big)dt\bigg]+zx. |  |

To simplify notation, in the following we set

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | ZtD:=eδ​t​z​ℋt​Dt,Z0−=z>0.Z^{D}\_{t}:=e^{\delta t}z\mathcal{H}\_{t}D\_{t},\quad Z\_{0^{-}}=z>0. |  |

Given that the Legendre–Fenchel transform of the utility function uu is such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | u~​(z):=supc≥0(u​(c)−z​c)=supc≥0(c1−γ1−γ−z​c)=γ1−γ​z−1−γγ,\tilde{u}(z):=\sup\_{c\geq 0}\left(u(c)-zc\right)=\sup\_{c\geq 0}\bigg(\frac{c^{1-\gamma}}{1-\gamma}-zc\bigg)=\frac{\gamma}{1-\gamma}z^{-\frac{1-\gamma}{\gamma}}, |  |

using u​(ct)−ZtD​ct≤u~​(ZtD)u(c\_{t})-Z^{D}\_{t}c\_{t}\leq\tilde{u}(Z^{D}\_{t}) in ([3.1](#S3.Ex2 "3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | 𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t]≤infD∈𝒟𝔼​[∫0∞e−δ​t​(u~​(ZtD)+ℓ​ZtD)​𝑑t]+z​x,\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})dt\bigg]\leq\inf\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big)dt\bigg]+zx, |  |

which, by arbitrariness of z>0z>0, in turn yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t]≤infz>0D∈𝒟(𝔼​[∫0∞e−δ​t​(u~​(ZtD)+ℓ​ZtD)​𝑑t]+z​x).\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})dt\bigg]\leq\inf\_{\begin{subarray}{c}z>0\\ D\in\mathcal{D}\end{subarray}}\bigg(\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big)dt\bigg]+zx\bigg). |  |

Hence, we have the weak duality

|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | sup(π,c)∈𝒜​(x)𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t]≤infz>0(infD∈𝒟𝔼​[∫0∞e−δ​t​(u~​(ZtD)+ℓ​ZtD)​𝑑t]+z​x).\displaystyle\sup\_{(\pi,c)\in\mathcal{A}(x)}\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})dt\bigg]\leq\inf\_{z>0}\bigg(\inf\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big)dt\bigg]+zx\bigg). |  |

  

In the subsequent analysis, we shall focus on the problem

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | infD∈𝒟𝔼​[∫0∞e−δ​t​(u~​(ZtD)+ℓ​ZtD)​𝑑t],\inf\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big)dt\bigg], |  |

with the aim of proving that actually the strong duality

|  |  |  |  |
| --- | --- | --- | --- |
| (3.7) |  | sup(π,c)∈𝒜​(x)𝔼​[∫0∞e−δ​t​u​(ct)​𝑑t]=infz>0(infD∈𝒟𝔼​[∫0∞e−δ​t​(u~​(ZtD)+ℓ​ZtD)​𝑑t]+z​x)\sup\_{(\pi,c)\in\mathcal{A}(x)}\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})dt\bigg]=\inf\_{z>0}\bigg(\inf\_{D\in\mathcal{D}}\mathbb{E}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big)dt\bigg]+zx\bigg) |  |

holds true. Problem ([3.6](#S3.E6 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is a singular stochastic control problem for the two-dimensional state process

|  |  |  |  |
| --- | --- | --- | --- |
| (3.8) |  | d​ZtD=(δ−r)​ZtD​d​t−βtσ​ZtD​d​Wt+ZtD​d​DtDt,t>0,Z0−D=z>0,dZ^{D}\_{t}=(\delta-r)Z^{D}\_{t}\,dt-\frac{\beta\_{t}}{\sigma}Z^{D}\_{t}\,dW\_{t}+Z^{D}\_{t}\frac{dD\_{t}}{D\_{t}},\quad t>0,\quad Z\_{0^{-}}^{D}=z>0, |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (3.9) |  | d​βt=κ​(β¯−βt)​d​t+σβ​d​Wtβ,t>0,β0=β∈ℝ,d\beta\_{t}=\kappa(\overline{\beta}-\beta\_{t})\,dt+\sigma\_{\beta}\,dW\_{t}^{\beta},\quad t>0,\quad\beta\_{0}=\beta\in\mathbb{R}, |  |

with D∈𝒟D\in\mathcal{D}. Notice that the dynamics of (ZtD)t(Z\_{t}^{D})\_{t} is easily obtained from ([3.2](#S3.E2 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) via Itô’s formula.
  
Given the Markovian structure, from now on we stress the dependency of the value of ([3.6](#S3.E6 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) with respect to the problem’s initial data and write

|  |  |  |  |
| --- | --- | --- | --- |
| (3.10) |  | V~​(z,β):=infD∈𝒟𝔼z,β​[∫0∞e−δ​t​(u~​(ZtD)+ℓ​ZtD)​𝑑t],\tilde{V}(z,\beta):=\inf\_{D\in\mathcal{D}}\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big)\,dt\bigg], |  |

where 𝔼z,β[⋅]=𝔼[⋅|Z0−D=z,β0=β]\mathbb{E}\_{z,\beta}[\;\cdot\;]=\mathbb{E}[\;\cdot\;|Z\_{0^{-}}^{D}=z,\beta\_{0}=\beta] denotes the expectation under ℙz,β(⋅):=ℙ(⋅|Z0−D=z,β0=β)\mathbb{P}\_{z,\beta}(\cdot):=\mathbb{P}(\;\cdot\;|\;Z^{D}\_{0-}=z,\;\beta\_{0}=\beta). For later use, we notice that limz↓0V~​(z,β)=0\lim\_{z\downarrow 0}\tilde{V}(z,\beta)=0. Analagously, in the following, we shall write (cf. ([2.4](#S2.E4 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")))

|  |  |  |  |
| --- | --- | --- | --- |
| (3.11) |  | V​(x,β):=max(π,c)∈𝒜​(x)⁡𝔼x,β​[∫0∞e−δ​t​u​(ct)​𝑑t],V(x,\beta):=\max\_{(\pi,c)\in\mathcal{A}(x)}\mathbb{E}\_{x,\beta}\left[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})\,dt\right], |  |

where 𝔼x,β​[⋅]\mathbb{E}\_{x,\beta}[\cdot] denotes the expectation under ℙx,β(⋅):=ℙ(⋅|X0=x,β0=β)\mathbb{P}\_{x,\beta}(\cdot):=\mathbb{P}(\;\cdot\;|\;X\_{0}=x,\;\beta\_{0}=\beta).
  
  
In Proposition [4.4](#S4.Thmtheorem4 "Proposition 4.4. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") below we will show that

|  |  |  |
| --- | --- | --- |
|  | V​(x,β)=infz>0(V~​(z,β)+z​x),V(x,\beta)=\inf\_{z>0}\bigg(\tilde{V}(z,\beta)+zx\bigg), |  |

so that ([3.7](#S3.E7 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) indeed holds true. This will be achieved through a series of intermediate results aimed at characterizing the optimal policy of problem ([3.6](#S3.E6 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). A major ingredient towards this characterization is the identification of an optimal stopping problem whose value coincides with V~z\tilde{V}\_{z}. Such an optimal stopping problem is introduced and studied in the following sections.

### 3.2. Derivation of the Auxiliary Optimal Stopping Problem

Denote by (Zt1)t(Z^{1}\_{t})\_{t} the uncontrolled state process (i.e., ZDZ^{D} as in ([3.8](#S3.E8 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) with D≡1D\equiv 1) satisfying

|  |  |  |  |
| --- | --- | --- | --- |
| (3.12) |  | d​Zt1=(δ−r)​Zt1​d​t−βtσ​Zt1​d​Wt,t>0,Z01=z>0.dZ^{1}\_{t}=(\delta-r)Z^{1}\_{t}\,dt-\frac{\beta\_{t}}{\sigma}Z^{1}\_{t}\,dW\_{t},\quad t>0,\quad Z\_{0}^{1}=z>0. |  |

Furthermore, to simplify notation, set 𝒪:=(0,∞)×ℝ\mathcal{O}:=(0,\infty)\times\mathbb{R}.
  
  
Inspired by [[2](#bib.bib16 "Irreversible investment and industry equilibrium")], [[5](#bib.bib32 "Optimal reduction of public debt under partial observation of the economic growth")] and [[16](#bib.bib39 "On the optimal management of public debt: a singular stochastic control problem")] we introduce the optimal stopping problem

|  |  |  |  |
| --- | --- | --- | --- |
| (3.13) |  | v​(z,β):=infτ𝔼z,β​[∫0τe−r​t​Mt​(u~′​(Zt1)+ℓ)​𝑑t],v(z,\beta):=\inf\_{\tau}\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\tau}e^{-rt}M\_{t}\,(\tilde{u}^{\prime}(Z\_{t}^{1})+\ell)\,dt\bigg], |  |

where u~′​(z)=−z1/γ\tilde{u}^{\prime}(z)=-z^{1/\gamma}, and where we take the infimum over 𝔽¯\bar{\mathbb{F}}-stopping times τ≥0\tau\geq 0, Z1Z^{1} evolves as in ([3.12](#S3.E12 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), and β\beta as in ([3.9](#S3.E9 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). We expect vv to be such that V~z=v\tilde{V}\_{z}=v on 𝒪\mathcal{O}. Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") below will indeed prove that such a relation holds true and that an optimizer for vv is in one-to-one correspondence to an optimizer for V~\tilde{V}. In the following, we shall study ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and characterize its optimal policy. In order to achieve this, it is convenient to perform a change of measure to remove the martingale (Mt)t(M\_{t})\_{t} (cf. ([2.3](#S2.E3 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))) from the stopping functional. This leads to the next proposition whose proof is postponed to the appendix.

###### Proposition 3.1.

For vv as in ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.14) |  | v​(z,β)=infτ𝔼z,βℚ​[∫0τe−r​t​(u~′​(Z^t)+ℓ)​𝑑t],v(z,\beta)=\inf\_{\tau}\mathbb{E}\_{z,\beta}^{\mathbb{Q}}\bigg[\int\_{0}^{\tau}e^{-rt}\,(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)\,dt\bigg], |  |

for a suitable probability measure ℚ\mathbb{Q} on a suitable measurable space (Ω^,ℱ^)(\hat{\Omega},\hat{\mathcal{F}}). The dynamics of the state processes (Z^t)t(\hat{Z}\_{t})\_{t} and (β^t)t(\hat{\beta}\_{t})\_{t} are given under ℚ\mathbb{Q} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Z^t\displaystyle d\hat{Z}\_{t} | =−β^tσ​Z^t​d​Wtℚ+Z^t​(δ−r+β^t2σ2)​d​t,t>0,Z^0=z>0,\displaystyle=-\frac{\hat{\beta}\_{t}}{\sigma}\hat{Z}\_{t}\,dW^{\mathbb{Q}}\_{t}+\hat{Z}\_{t}\bigg(\delta-r+\frac{\hat{\beta}\_{t}^{2}}{\sigma^{2}}\bigg)\,dt,\quad t>0,\quad\hat{Z}\_{0}=z>0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​β^t\displaystyle d\hat{\beta}\_{t} | =σβ​d​Wtβ,ℚ+(κ​(β¯−β^t)−ρ​β^tσ​σβ)​d​t,t>0,β^0=β∈ℝ.\displaystyle=\sigma\_{\beta}\,dW^{\beta,\mathbb{Q}}\_{t}+\bigg(\kappa(\overline{\beta}-\hat{\beta}\_{t})-\rho\,\frac{\hat{\beta}\_{t}}{\sigma}\sigma\_{\beta}\bigg)\,dt,\quad t>0,\quad\hat{\beta}\_{0}=\beta\in\mathbb{R}. |  |

Here, (Wtℚ)t(W^{\mathbb{Q}}\_{t})\_{t} and (Wtβ,ℚ)t(W^{\beta,\mathbb{Q}}\_{t})\_{t} are two standard Brownian motions on (Ω^,ℱ^,ℚ)(\hat{\Omega},\hat{\mathcal{F}},\mathbb{Q}), generating the filtrations (completed by ℚ​-null sets of​ℱ^\mathbb{Q}\text{-null sets of}\;\hat{\mathcal{F}}) 𝔽W,ℚ:=(ℱtW,ℚ)t\mathbb{F}^{W,\mathbb{Q}}:=(\mathcal{F}\_{t}^{W,\mathbb{Q}})\_{t} and 𝔽Wβ,ℚ:=(ℱtWβ,ℚ)t\mathbb{F}^{W^{\beta},\mathbb{Q}}:=(\mathcal{F}\_{t}^{W^{\beta},\mathbb{Q}})\_{t}, respectively, and 𝔼z,βℚ​[⋅]\mathbb{E}\_{z,\beta}^{\mathbb{Q}}[\;\cdot\;] is the expectation under ℚz,β=ℚ(⋅∣Z^0=z,β^0=β)\mathbb{Q}\_{z,\beta}=\mathbb{Q}(\;\cdot\mid\hat{Z}\_{0}=z,\;\hat{\beta}\_{0}=\beta). Finally, the optimization in ([3.14](#S3.E14 "In Proposition 3.1. ‣ 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is performed over the stopping times of the filtration 𝔽^:=(ℱ^t)t\hat{\mathbb{F}}:=(\hat{\mathcal{F}}\_{t})\_{t}, where ℱ^t:=ℱtW,ℚ∨ℱtWβ,ℚ\hat{\mathcal{F}}\_{t}:=\mathcal{F}\_{t}^{W,\mathbb{Q}}\vee\mathcal{F}\_{t}^{W^{\beta},\mathbb{Q}}, t≥0t\geq 0.

###### Proof.

See Appendix [A.1](#A1.SS1 "A.1. Proof of Proposition 3.1 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
∎

With reference to Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we therefore now turn our attention to characterizing the solution to the optimal stopping problem

|  |  |  |  |
| --- | --- | --- | --- |
| (3.15) |  | v​(z,β):=infτ𝔼z,βℚ​[∫0τe−r​t​(u~′​(Z^t)+ℓ)​𝑑t],v(z,\beta):=\inf\_{\tau}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\tau}e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)dt\bigg], |  |

subject to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.16) |  | d​Z^t\displaystyle d\hat{Z}\_{t} | =−β^tσ​Z^t​d​Wtℚ+Z^t​(δ−r+β^t2σ2)​d​t,t>0,Z^0=z>0,\displaystyle=-\frac{\hat{\beta}\_{t}}{\sigma}\hat{Z}\_{t}dW^{\mathbb{Q}}\_{t}+\hat{Z}\_{t}(\delta-r+\frac{\hat{\beta}\_{t}^{2}}{\sigma^{2}})dt,\quad t>0,\quad\hat{Z}\_{0}=z>0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.17) |  | d​β^t\displaystyle d\hat{\beta}\_{t} | =σβ​d​Wtβ,ℚ+(κ​(β¯−β^t)−ρ​β^tσ​σβ)​d​t,t>0,β^0=β∈ℝ.\displaystyle=\sigma\_{\beta}dW\_{t}^{\beta,\mathbb{Q}}+(\kappa(\overline{\beta}-\hat{\beta}\_{t})-\rho\frac{\hat{\beta}\_{t}}{\sigma}\sigma\_{\beta})dt,\quad t>0,\quad\hat{\beta}\_{0}=\beta\in\mathbb{R}. |  |

In the following, when needed, we stress the dependence of the unique strong solution to ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))-([3.17](#S3.E17 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) on the initial data (z,β)∈𝒪(z,\beta)\in\mathcal{O} by writing (Z^tz,β)t(\hat{Z}\_{t}^{z,\beta})\_{t} and (β^tβ)t(\hat{\beta}\_{t}^{\beta})\_{t}.

### 3.3. Preliminary Properties of the Optimal Stopping Value Function

In this subsection, we establish preliminary properties of the value function ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). For the proof of those, we make the following assumption on the model’s parameters. Such requirement in particular ensures well-posedness of vv as in ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and, together with Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), it will be a standing assumption throughout the rest of the paper.

###### Assumption 3.2.

We assume that

|  |  |  |
| --- | --- | --- |
|  | γ>max⁡{1,|ρ|​σβσ​(κ+ρ​σβσ)}.\gamma>\max\bigg\{1,\frac{|\rho|\sigma\_{\beta}}{\sigma\bigg(\kappa+\frac{\rho\sigma\_{\beta}}{\sigma}\bigg)}\bigg\}. |  |

Notice that κ+ρ​σβσ>0\kappa+\frac{\rho\sigma\_{\beta}}{\sigma}>0 due to Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"). We then have the following first preliminary finding.

###### Proposition 3.3.

It holds

|  |  |  |
| --- | --- | --- |
|  | 𝔼z,βℚ​[∫0∞e−r​t​|u~′​(Z^t)+ℓ|​𝑑t]<∞.\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}|\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell|\,dt\bigg]<\infty. |  |

Moreover, one has

|  |  |  |  |
| --- | --- | --- | --- |
| (3.18) |  | 𝔼z,βℚ​[Z^t−1γ]≤z−1γ​exp⁡(−1γ​(δ−r)​t).\mathbb{E}^{\mathbb{Q}}\_{z,\beta}[\hat{Z}\_{t}^{-\frac{1}{\gamma}}]\leq z^{-\frac{1}{\gamma}}\exp\bigg(-\tfrac{1}{\gamma}(\delta-r)t\bigg). |  |

###### Proof.

See Appendix [A.2](#A1.SS2 "A.2. Proof of Proposition 3.3 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
∎

The next result directly follows from the expression of vv as in ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and the fact that z↦Z^tz,βz\mapsto\hat{Z}^{z,\beta}\_{t} is ℚ\mathbb{Q}-a.s. increasing for all t≥0t\geq 0.

###### Proposition 3.4.

One has that z↦v​(z,β)z\mapsto v(z,\beta) is nondecreasing for all β∈ℝ\beta\in\mathbb{R}.

###### Remark 3.5.

Note that the monotonicity of β↦v​(z,β)\beta\mapsto v(z,\beta) is not clear, since the process (β^t)t(\hat{\beta}\_{t})\_{t} also affects the volatility of (Z^t)t(\hat{Z}\_{t})\_{t}, and therefore comparison theorems for solutions to SDEs do not apply.

The next results provide useful bounds and limit behavior of the value function vv. Their proofs are given in the Appendix.

###### Proposition 3.6.

We have

|  |  |  |
| --- | --- | --- |
|  | −𝔼z,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]≤v​(z,β)≤0.-\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}\_{t}^{-\frac{1}{\gamma}}dt\bigg]\leq v(z,\beta)\leq 0. |  |

###### Proof.

See Appendix [A.3](#A1.SS3 "A.3. Proof of Proposition 3.6 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
∎

###### Proposition 3.7.

It holds that

|  |  |  |
| --- | --- | --- |
|  | limz→0v​(z,β)=−∞andlimz→∞v​(z,β)=0.\lim\_{z\to 0}v(z,\beta)=-\infty\quad\text{and}\quad\lim\_{z\to\infty}v(z,\beta)=0. |  |

###### Proof.

See Appendix [A.4](#A1.SS4 "A.4. Proof of Proposition 3.7 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
∎

###### Proposition 3.8.

The value function v​(z,β)v(z,\beta) is continuous for all (z,β)∈𝒪(z,\beta)\in\mathcal{O}.

###### Proof.

Step 1. We first show that (z,β)↦v​(z,β)(z,\beta)\mapsto v(z,\beta) is upper semicontinuous for all (z,β)∈𝒪(z,\beta)\in\mathcal{O}. Given ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), it suffices to show that

|  |  |  |
| --- | --- | --- |
|  | 𝒥​(τ;z,β):=𝔼z,βℚ​[∫0τe−r​t​(−Z^t−1γ+ℓ)​𝑑t]\mathcal{J}(\tau;z,\beta):=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\tau}e^{-rt}\big(-\hat{Z}\_{t}^{-\frac{1}{\gamma}}+\ell\big)dt\bigg] |  |

is continuous for all (z,β)∈𝒪(z,\beta)\in\mathcal{O} and fixed τ≥0\tau\geq 0.
  
Fix (z0,β0)∈𝒪(z\_{0},\beta\_{0})\in\mathcal{O} and let (zn,βn)⊆𝒪(z\_{n},\beta\_{n})\subseteq\mathcal{O} be a sequence converging to (z0,β0)(z\_{0},\beta\_{0}). Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.19) |  | |𝒥​(τ;zn,βn)−𝒥​(τ;z0,β0)|\displaystyle{}\big|\mathcal{J}(\tau;z\_{n},\beta\_{n})-\mathcal{J}(\tau;z\_{0},\beta\_{0})\big| | ≤|𝒥​(τ;zn,βn)−𝒥​(τ;z0,βn)|\displaystyle\leq\big|\mathcal{J}(\tau;z\_{n},\beta\_{n})-\mathcal{J}(\tau;z\_{0},\beta\_{n})\big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|𝒥​(τ;z0,βn)−𝒥​(τ;z0,β0)|.\displaystyle\quad+\big|\mathcal{J}(\tau;z\_{0},\beta\_{n})-\mathcal{J}(\tau;z\_{0},\beta\_{0})\big|. |  |

For the first term on the right-hand side in ([3.19](#S3.E19 "In Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝒥​(τ;zn,βn)−𝒥​(τ;z0,βn)|\displaystyle\big|\mathcal{J}(\tau;z\_{n},\beta\_{n})-\mathcal{J}(\tau;z\_{0},\beta\_{n})\big| | ≤𝔼ℚ​[∫0∞e−r​t​|(z0​Z~t)−1γ−(zn​Z~t)−1γ|​𝑑t]\displaystyle\leq\mathbb{E}^{\mathbb{Q}}\bigg[\int\_{0}^{\infty}e^{-rt}\big|(z\_{0}\tilde{Z}\_{t})^{-\frac{1}{\gamma}}-(z\_{n}\tilde{Z}\_{t})^{-\frac{1}{\gamma}}\big|dt\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.20) |  |  | =|z0−1γ−zn−1γ|​𝔼ℚ​[∫0∞e−r​t​Z~t−1γ​𝑑t]\displaystyle=|z\_{0}^{-\frac{1}{\gamma}}-z\_{n}^{-\frac{1}{\gamma}}|\,\mathbb{E}^{\mathbb{Q}}\bigg[\int\_{0}^{\infty}e^{-rt}\tilde{Z}\_{t}^{-\frac{1}{\gamma}}dt\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|z0−1γ−zn−1γ|​∫0∞e−r​t​e−1γ​(δ−r)​t​𝑑t,\displaystyle\leq|z\_{0}^{-\frac{1}{\gamma}}-z\_{n}^{-\frac{1}{\gamma}}|\int\_{0}^{\infty}e^{-rt}e^{-\frac{1}{\gamma}(\delta-r)t}dt, |  |

where we have set

|  |  |  |  |
| --- | --- | --- | --- |
| (3.21) |  | Z~t:=exp⁡(∫0t(δ−r+12​β^s2σ2)​𝑑s−∫0tβ^sσ​𝑑Wsℚ),\tilde{Z}\_{t}:=\exp\Big(\int\_{0}^{t}(\delta-r+\tfrac{1}{2}\tfrac{\hat{\beta}\_{s}^{2}}{\sigma^{2}})ds-\int\_{0}^{t}\frac{\hat{\beta}\_{s}}{\sigma}dW\_{s}^{\mathbb{Q}}\Big), |  |

for t≥0t\geq 0, and we have used ([3.18](#S3.E18 "In Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) upon noticing that Z~t=Z^tz\tilde{Z}\_{t}=\frac{\hat{Z}\_{t}}{z}. Given that the integral on the right-hand side of ([3.3](#S3.Ex14 "Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is finite as r+1γ​(δ−r)>0r+\frac{1}{\gamma}(\delta-r)>0 because γ>1\gamma>1, we find

|  |  |  |  |
| --- | --- | --- | --- |
| (3.22) |  | lim(zn,βn)→(z0,β0)|𝒥​(τ;zn,βn)−𝒥​(τ;z0,βn)|=0.\lim\_{(z\_{n},\beta\_{n})\to(z\_{0},\beta\_{0})}\big|\mathcal{J}(\tau;z\_{n},\beta\_{n})-\mathcal{J}(\tau;z\_{0},\beta\_{n})\big|=0. |  |

  

For the second term in ([3.19](#S3.E19 "In Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), Fubini-Tonelli Theorem yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.23) |  | |𝒥​(τ;z0,βn)−𝒥​(τ;z0,β0)|\displaystyle\big|\mathcal{J}(\tau;z\_{0},\beta\_{n})-\mathcal{J}(\tau;z\_{0},\beta\_{0})\big| | ≤∫0∞e−r​t​𝔼ℚ​[|(Z^tz0,β0)−1γ−(Z^tz0,βn)−1γ|]​𝑑t.\displaystyle\leq\int\_{0}^{\infty}e^{-rt}\,\mathbb{E}^{\mathbb{Q}}\Big[\big|(\hat{Z}\_{t}^{z\_{0},\beta\_{0}})^{-\frac{1}{\gamma}}-(\hat{Z}\_{t}^{z\_{0},\beta\_{n}})^{-\frac{1}{\gamma}}\big|\Big]dt. |  |

By the same arguments used in the proof of Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") (see Appendix [A.2](#A1.SS2 "A.2. Proof of Proposition 3.3 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), one can show that

|  |  |  |
| --- | --- | --- |
|  | e−r​t​𝔼ℚ​[|(Z^tz0,β0)−1γ−(Z^tz0,βn)−1γ|]≤2​z0−1γ​e−(r+1γ​(δ−r))​t,e^{-rt}\,\mathbb{E}^{\mathbb{Q}}\Big[\big|(\hat{Z}\_{t}^{z\_{0},\beta\_{0}})^{-\frac{1}{\gamma}}-(\hat{Z}\_{t}^{z\_{0},\beta\_{n}})^{-\frac{1}{\gamma}}\big|\Big]\leq 2z\_{0}^{-\frac{1}{\gamma}}e^{-(r+\frac{1}{\gamma}(\delta-r))t}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | ∫0∞2​z0−1γ​e−(r+1γ​(δ−r))​t​𝑑t<∞,\int\_{0}^{\infty}2z\_{0}^{-\frac{1}{\gamma}}e^{-(r+\frac{1}{\gamma}(\delta-r))t}dt<\infty, |  |

given that r+1γ​(δ−r)>0r+\frac{1}{\gamma}(\delta-r)>0 by γ>1\gamma>1. Hence, an application of the Dominated Convergence Theorem in ([3.23](#S3.E23 "In Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.24) |  |  | lim(zn,βn)→(z0,β0)∫0∞e−r​t​𝔼ℚ​[|(Z^tz0,β0)−1γ−(Z^tz0,βn)−1γ|]​𝑑t\displaystyle\lim\_{(z\_{n},\beta\_{n})\to(z\_{0},\beta\_{0})}\int\_{0}^{\infty}e^{-rt}\mathbb{E}^{\mathbb{Q}}\Big[\big|(\hat{Z}\_{t}^{z\_{0},\beta\_{0}})^{-\frac{1}{\gamma}}-(\hat{Z}\_{t}^{z\_{0},\beta\_{n}})^{-\frac{1}{\gamma}}\big|\Big]dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.25) |  |  | =∫0∞lim(zn,βn)→(z0,β0)e−r​t​𝔼ℚ​[|(Z^tz0,β0)−1γ−(Z^tz0,βn)−1γ|]​d​t.\displaystyle=\int\_{0}^{\infty}\lim\_{(z\_{n},\beta\_{n})\to(z\_{0},\beta\_{0})}e^{-rt}\mathbb{E}^{\mathbb{Q}}\Big[\big|(\hat{Z}\_{t}^{z\_{0},\beta\_{0}})^{-\frac{1}{\gamma}}-(\hat{Z}\_{t}^{z\_{0},\beta\_{n}})^{-\frac{1}{\gamma}}\big|\Big]dt. |  |

Finally, by exploiting arguments as in the proof of Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") again, we have under Assumption [3.2](#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") that

|  |  |  |
| --- | --- | --- |
|  | 𝔼z,βℚ​[(Z^tβ)−p/γ]≤z0−p/γ​e−pγ​(δ−r)​t<∞,\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\big[(\hat{Z}\_{t}^{\beta})^{-p/\gamma}\big]\leq z\_{0}^{-p/\gamma}e^{-\frac{p}{\gamma}(\delta-r)t}<\infty, |  |

where pp is chosen such that

|  |  |  |
| --- | --- | --- |
|  | 1<p<min⁡{γ,γ​σ​(κ+ρ​σβσ)|ρ|​σβ},1<p<\min\bigg\{\gamma,\frac{\gamma\sigma\bigg(\kappa+\frac{\rho\sigma\_{\beta}}{\sigma}\bigg)}{|\rho|\sigma\_{\beta}}\bigg\}, |  |

upon noticing that, by Assumption [3.2](#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we have γ​σ​(κ+ρ​σβσ)>|ρ|​σβ\gamma\sigma\bigg(\kappa+\frac{\rho\sigma\_{\beta}}{\sigma}\bigg)>|\rho|\sigma\_{\beta}. Therefore, by Vitali’s Convergence Theorem and continuity of β↦Z^tz,β\beta\mapsto\hat{Z}\_{t}^{z,\beta}, we conclude that

|  |  |  |
| --- | --- | --- |
|  | lim(zn,βn)→(z0,β0)𝔼ℚ​[|(Z^tz0,β0)−1γ−(Z^tz0,βn)−1γ|]=0,\lim\_{(z\_{n},\beta\_{n})\to(z\_{0},\beta\_{0})}\mathbb{E}^{\mathbb{Q}}\Big[\big|(\hat{Z}\_{t}^{z\_{0},\beta\_{0}})^{-\frac{1}{\gamma}}-(\hat{Z}\_{t}^{z\_{0},\beta\_{n}})^{-\frac{1}{\gamma}}\big|\Big]=0, |  |

which implies due to ([3.23](#S3.E23 "In Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.24](#S3.E24 "In Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.26) |  | lim(zn,βn)→(z0,β0)|𝒥​(τ;z0,βn)−𝒥​(τ;z0,β0)|=0.\lim\_{(z\_{n},\beta\_{n})\to(z\_{0},\beta\_{0})}\big|\mathcal{J}(\tau;z\_{0},\beta\_{n})-\mathcal{J}(\tau;z\_{0},\beta\_{0})\big|=0. |  |

Finally, by combining ([3.22](#S3.E22 "In Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.26](#S3.E26 "In Proof. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we obtain

|  |  |  |
| --- | --- | --- |
|  | lim(zn,βn)→(z0,β0)𝒥​(τ;zn,βn)=𝒥​(τ;z0,β0).\lim\_{(z\_{n},\beta\_{n})\to(z\_{0},\beta\_{0})}\mathcal{J}(\tau;z\_{n},\beta\_{n})=\mathcal{J}(\tau;z\_{0},\beta\_{0}). |  |

Step 2. Fix again (z0,β0)∈𝒪(z\_{0},\beta\_{0})\in\mathcal{O} and let (zn,βn)⊆𝒪(z\_{n},\beta\_{n})\subseteq\mathcal{O} be a sequence converging to (z0,β0)(z\_{0},\beta\_{0}) as n→∞n\to\infty. For each (zn,βn)(z\_{n},\beta\_{n}), let τn\tau\_{n} be an ε\varepsilon-optimal stopping time for (zn,βn)(z\_{n},\beta\_{n}), with ε>0\varepsilon>0; that is,

|  |  |  |
| --- | --- | --- |
|  | v​(zn,βn)≥𝒥​(τn;zn,βn)−ε.v(z\_{n},\beta\_{n})\geq\mathcal{J}(\tau\_{n};z\_{n},\beta\_{n})-\varepsilon. |  |

Since τn\tau\_{n} is suboptimal for (z0,β0)(z\_{0},\beta\_{0}), we have v​(z0,β0)≤𝒥​(τn;z0,β0)v(z\_{0},\beta\_{0})\leq\mathcal{J}(\tau\_{n};z\_{0},\beta\_{0}).
  
Defining

|  |  |  |
| --- | --- | --- |
|  | Δn:=𝒥​(τn;zn,βn)−𝒥​(τn;z0,β0),\Delta\_{n}:=\mathcal{J}(\tau\_{n};z\_{n},\beta\_{n})-\mathcal{J}(\tau\_{n};z\_{0},\beta\_{0}), |  |

it then holds

|  |  |  |
| --- | --- | --- |
|  | |Δn|≤|𝒥​(τn;zn,βn)−𝒥​(τn;z0,βn)|+|𝒥​(τn;z0,βn)−𝒥​(τn;z0,β0)|.|\Delta\_{n}|\leq|\mathcal{J}(\tau\_{n};z\_{n},\beta\_{n})-\mathcal{J}(\tau\_{n};z\_{0},\beta\_{n})|+|\mathcal{J}(\tau\_{n};z\_{0},\beta\_{n})-\mathcal{J}(\tau\_{n};z\_{0},\beta\_{0})|. |  |

By arguments as in Step 1 above, we have Δn→0\Delta\_{n}\to 0 as n→∞n\to\infty. Hence,

|  |  |  |
| --- | --- | --- |
|  | v​(zn,βn)≥𝒥​(τn;zn,βn)−ε=𝒥​(τn;z0,β0)+Δn−ε≥v​(z0,β0)+Δn−ε,\displaystyle v(z\_{n},\beta\_{n})\geq\mathcal{J}(\tau\_{n};z\_{n},\beta\_{n})-\varepsilon=\mathcal{J}(\tau\_{n};z\_{0},\beta\_{0})+\Delta\_{n}-\varepsilon\geq v(z\_{0},\beta\_{0})+\Delta\_{n}-\varepsilon, |  |

which, by taking the limit as n→∞n\to\infty, yields

|  |  |  |
| --- | --- | --- |
|  | lim infn→∞v​(zn,βn)≥v​(z0,β0)−ε.\liminf\_{n\to\infty}v(z\_{n},\beta\_{n})\geq v(z\_{0},\beta\_{0})-\varepsilon. |  |

Since ε>0\varepsilon>0 was arbitrary, we have that vv is lower-semicontinuous.
  
  
Step 3. Combining Step 1 and Step 2, we conclude that vv is continuous on 𝒪\mathcal{O}.
∎

As it is customary in optimal stopping, we now define the continuation (waiting) and stopping regions as

|  |  |  |  |
| --- | --- | --- | --- |
| (3.27) |  | 𝒲:={(z,β)∈𝒪:v​(z,β)<0},𝒮:={(z,β)∈𝒪:v​(z,β)=0}.\mathcal{W}:=\{(z,\beta)\in\mathcal{O}:v(z,\beta)<0\},\quad\mathcal{S}:=\{(z,\beta)\in\mathcal{O}:v(z,\beta)=0\}. |  |

By the continuity of vv (see Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), 𝒲\mathcal{W} is open and 𝒮\mathcal{S} is closed.
Furthermore, the stopping time

|  |  |  |  |
| --- | --- | --- | --- |
| (3.28) |  | τ∗​(z,β):=inf{s≥0:(Z^s,β^s)∈𝒮}\tau^{\*}(z,\beta):=\inf\{s\geq 0:(\hat{Z}\_{s},\hat{\beta}\_{s})\in\mathcal{S}\} |  |

is optimal (see Corollary 2.9 in Chapter 1 of [[35](#bib.bib18 "Optimal stopping and free-boundary problems")]).

###### Proposition 3.9.

The stopping region 𝒮\mathcal{S} is non-empty; that is, 𝒮≠∅\mathcal{S}\neq\emptyset.

###### Proof.

Suppose 𝒮=∅\mathcal{S}=\emptyset. Then for all (z,β)∈𝒪(z,\beta)\in\mathcal{O} we have by ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), the fact that u~′​(Z^t)=−Z^t−1γ\tilde{u}^{\prime}(\hat{Z}\_{t})=-\hat{Z}\_{t}^{-\frac{1}{\gamma}} (cf. ([3.3](#S3.E3 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))), and ([3.18](#S3.E18 "In Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0>v​(z,β)=𝔼z,βℚ​[∫0∞e−r​t​(−Z^t−1γ+ℓ)​𝑑t]\displaystyle 0>v(z,\beta)=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\big(-\hat{Z}\_{t}^{-\frac{1}{\gamma}}+\ell\big)dt\bigg] | =ℓr−𝔼z,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]\displaystyle=\frac{\ell}{r}-\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}\_{t}^{-\frac{1}{\gamma}}dt\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥ℓr−z−1γ​∫0∞e−(1γ​(δ−r)+r)​t​𝑑t\displaystyle\geq\frac{\ell}{r}-z^{-\frac{1}{\gamma}}\int\_{0}^{\infty}e^{-(\frac{1}{\gamma}(\delta-r)+r)t}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℓr−z−1γ1γ​(δ−r)+r.\displaystyle=\frac{\ell}{r}-\frac{z^{-\frac{1}{\gamma}}}{\frac{1}{\gamma}(\delta-r)+r}. |  |

However, the last expression is strictly positive if

|  |  |  |  |
| --- | --- | --- | --- |
| (3.29) |  | z>(ℓr​(1γ​(δ−r)+r))−γ>0,z>\Big(\frac{\ell}{r}\big(\frac{1}{\gamma}(\delta-r)+r\big)\Big)^{-\gamma}>0, |  |

which gives the desired contradiction.
∎

### 3.4. Optimal Stopping Boundary and Regularity of the Value Function

In this section, we establish the existence of a lower-semicontinuous optimal stopping boundary (free boundary) that separates continuation and stopping regions and prove further regularity of the value function of the optimal stopping problem.
  
We first show that the boundary ∂𝒲\partial\mathcal{W} can be represented by a function
z∗:ℝ→[ℓ−γ,∞]z^{\*}:\mathbb{R}\rightarrow[\ell^{-\gamma},\infty] and establish connectedness of 𝒲\mathcal{W} and 𝒮\mathcal{S}
with respect to the zz-variable.

###### Lemma 3.10.

There exists a free boundary z∗:ℝ→[0,∞]z^{\*}:\mathbb{R}\rightarrow[0,\infty] such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.30) |  | 𝒮={(z,β)∈𝒪:z≥z∗​(β)}.\mathcal{S}=\{(z,\beta)\in\mathcal{O}:z\geq z^{\*}(\beta)\}. |  |

Moreover, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.31) |  | 0<ℓ−γ≤z∗​(β)for all ​β∈ℝ,0<\ell^{-\gamma}\leq z^{\*}(\beta)\quad\text{for all }\beta\in\mathbb{R}, |  |

and β↦z∗​(β)\beta\mapsto z^{\*}(\beta) is lower-semicontinuous.

###### Proof.

By Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we have that z↦v​(z,β)z\mapsto v(z,\beta) is nondecreasing for all β∈ℝ\beta\in\mathbb{R}.
Hence, by defining

|  |  |  |  |
| --- | --- | --- | --- |
| (3.32) |  | z∗​(β):=inf{z>0:v​(z,β)≥0}z^{\*}(\beta):=\inf\{z>0:v(z,\beta)\geq 0\} |  |

(with the convention inf∅=+∞\inf\emptyset=+\infty), it follows from ([3.27](#S3.E27 "In 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that

|  |  |  |
| --- | --- | --- |
|  | 𝒮={(z,β)∈𝒪:z≥z∗​(β)},and𝒲={(z,β)∈𝒪:z<z∗​(β)}.\mathcal{S}=\{(z,\beta)\in\mathcal{O}:z\geq z^{\*}(\beta)\},\quad\text{and}\quad\mathcal{W}=\{(z,\beta)\in\mathcal{O}:z<z^{\*}(\beta)\}. |  |

For the lower bound of z∗z^{\*}, we have from ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and u~′​(z)=−z−1γ\tilde{u}^{\prime}(z)=-z^{-\frac{1}{\gamma}} that, if −z−1γ+ℓ<0-z^{-\frac{1}{\gamma}}+\ell<0, it is optimal to continue, as stopping immediately yields 0 while continuing for a short time yields a negative contribution to the cost functional. Hence, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(z,β)∈𝒪∣−z−1γ+ℓ<0}⊆𝒲\displaystyle\{(z,\beta)\in\mathcal{O}\mid-z^{-\frac{1}{\gamma}}+\ell<0\}\subseteq\mathcal{W} | ⇔{(z,β)∈𝒪∣−z−1γ+ℓ≥0}⊇𝒮\displaystyle\iff\{(z,\beta)\in\mathcal{O}\mid-z^{-\frac{1}{\gamma}}+\ell\geq 0\}\supseteq\mathcal{S} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔{(z,β)∈𝒪∣z≥ℓ−γ}⊇𝒮.\displaystyle\iff\{(z,\beta)\in\mathcal{O}\mid z\geq\ell^{-\gamma}\}\supseteq\mathcal{S}. |  |

It then follows from ([3.32](#S3.E32 "In Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that z∗​(β)≥ℓ−γ>0,for all​β∈ℝ.z^{\*}(\beta)\geq\ell^{-\gamma}>0,\;\text{for all}\;\beta\in\mathbb{R}.
  
Finally, lower-semicontinuity of z∗z^{\*} is due to the fact that ([3.30](#S3.E30 "In Lemma 3.10. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is closed thanks to ([3.27](#S3.E27 "In 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and continuity of vv (cf. Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).
∎

We continue by proving (local) Lipschitz continuity of vv and probabilistic representations of its weak derivatives.

###### Proposition 3.11.

The value function vv is (locally) Lipschitz continuous on 𝒪\mathcal{O}. Moreover, its weak derivatives, denoted by vzv\_{z} and vβv\_{\beta}, admit the following probabilistic representations:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.33) |  | vz​(z,β)=𝔼z,βℚ​[∫0τ∗e−r​t​1γ​z−1​Z^t−1γ​𝑑t],v\_{z}(z,\beta)=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\Big[\int\_{0}^{\tau^{\*}}e^{-rt}\frac{1}{\gamma}z^{-1}\hat{Z}\_{t}^{-\frac{1}{\gamma}}dt\Big], |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (3.34) |  | vβ​(z,β)=𝔼z,βℚ​[∫0τ∗e−r​t​(1γ​(Z^t)−1γ​(∫0te−a​s​β^sβσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝑑t],v\_{\beta}(z,\beta)=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\left[\int\_{0}^{\tau^{\*}}e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)dt\right], |  |

where a:=κ+ρ​σβσ>0a:=\kappa+\rho\frac{\sigma\_{\beta}}{\sigma}>0 by Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").

###### Proof.

See Appendix [A.5](#A1.SS5 "A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
∎

Standard results in optimal stopping theory (cf. Chapter 3 in [[35](#bib.bib18 "Optimal stopping and free-boundary problems")]) together with the previous findings imply that the couple (v,z∗)(v,z^{\*}) satisfies the free boundary problem

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| (3.35) |  |  | ℒ​v−r​v+u~′​(z)+ℓ=0\displaystyle\mathcal{L}v-rv+\tilde{u}^{\prime}(z)+\ell=0 | on 0<z<z∗​(β)0<z<z^{\*}(\beta) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | v=0\displaystyle v=0 | on z≥z∗​(β)z\geq z^{\*}(\beta), |  |

where ℒ\mathcal{L} is the infinitesimal generator of the process (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.36) |  | (ℒ​v)​(z,β)=12​β2σ2​(2​z​vz+z2​vz​z)+12​σβ2​vβ​β+(δ−r)​z​vz+κ​(β¯−β)​vβ−ρ​βσ​σβ​(vβ+z​vz​β),(\mathcal{L}v)(z,\beta)=\frac{1}{2}\frac{\beta^{2}}{\sigma^{2}}(2zv\_{z}+z^{2}v\_{zz})+\frac{1}{2}\sigma\_{\beta}^{2}v\_{\beta\beta}+(\delta-r)zv\_{z}+\kappa(\overline{\beta}-\beta)v\_{\beta}-\rho\frac{\beta}{\sigma}\sigma\_{\beta}\,(v\_{\beta}+zv\_{z\beta}), |  |

and the PDE above is intended in the sense of Schwartz distributions (see Corollary 5 in [[36](#bib.bib19 "Weak solutions in the sense of Schwartz to Dynkin’s characteristic operator equation")]). In Proposition [3.13](#S3.Thmtheorem13 "Proposition 3.13. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") below we will show that vv actually solves ([3.35](#S3.E35 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) in the classical sense. In order to achieve this, we need the following result.

###### Lemma 3.12.

The process (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t}, given by ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.17](#S3.E17 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), is strong Feller.

###### Proof.

Given that C​o​r​r​(Wtℚ,Wtβ,ℚ)=ρ​tCorr(W\_{t}^{\mathbb{Q}},W\_{t}^{\beta,\mathbb{Q}})=\rho t, ρ∈[−1,1]\rho\in[-1,1], we can write

|  |  |  |
| --- | --- | --- |
|  | Wtβ,ℚ=ρ​Wtℚ+1−ρ2​W^t2,⟂,t≥0,W\_{t}^{\beta,\mathbb{Q}}=\rho\,W\_{t}^{\mathbb{Q}}+\sqrt{1-\rho^{2}}\,\widehat{W}\_{t}^{2,\perp},\quad t\geq 0, |  |

where W^2,⟂\widehat{W}^{2,\perp} is a standard Brownian motion independent of WℚW^{\mathbb{Q}}. Then (cf. ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.17](#S3.E17 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))),

|  |  |  |
| --- | --- | --- |
|  | d​Z^t=−β^tσ​Z^t​d​Wtℚ+Z^t​(δ−r+β^t2σ2)​d​t,t>0,Z^0=z>0,d\hat{Z}\_{t}=-\frac{\hat{\beta}\_{t}}{\sigma}\hat{Z}\_{t}\,dW\_{t}^{\mathbb{Q}}+\hat{Z}\_{t}\bigg(\delta-r+\frac{\hat{\beta}\_{t}^{2}}{\sigma^{2}}\bigg)dt,\quad t>0,\quad\hat{Z}\_{0}=z>0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | d​β^t=σβ​ρ​d​Wtℚ+σβ​1−ρ2​d​W^t2,⟂+(κ​(β¯−β^t)−ρ​β^tσ​σβ)​d​t,t>0,β^0=β∈ℝ.d\hat{\beta}\_{t}=\sigma\_{\beta}\rho\,dW\_{t}^{\mathbb{Q}}+\sigma\_{\beta}\sqrt{1-\rho^{2}}\,d\widehat{W}\_{t}^{2,\perp}+\bigg(\kappa(\overline{\beta}-\hat{\beta}\_{t})-\rho\frac{\hat{\beta}\_{t}}{\sigma}\sigma\_{\beta}\bigg)dt,\quad t>0,\quad\hat{\beta}\_{0}=\beta\in\mathbb{R}. |  |

Notice that ([3.36](#S3.E36 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is not uniformly elliptic. As a matter of fact, denoting by Σ​(z,β)\Sigma(z,\beta) the diffusion matrix associated to ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))-([3.17](#S3.E17 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) one has det(Σ​ΣT​(z,β))=β2​z2​σβ2σ2​(1−ρ2)\det(\Sigma\Sigma^{T}(z,\beta))=\frac{\beta^{2}z^{2}\sigma\_{\beta}^{2}}{\sigma^{2}}(1-\rho^{2}), which vanishes for β=0\beta=0. We therefore now check that the process (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} satisfies the so-called Hörmander’s condition (see, e.g., condition (H) in Section 2.3.2 in [[34](#bib.bib33 "The malliavin calculus and related topics")]). This implies that the second-order infinitesimal generator ℒ\mathcal{L} of (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} as in ([3.36](#S3.E36 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is hypoelliptic and therefore that (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} is a strong Feller process (see Proposition 4 in [[13](#bib.bib34 "Quickest real-time detection of multiple brownian drifts")]).
  
For (z,β)∈𝒪(z,\beta)\in\mathcal{O}, arbitrary but fixed, we then define the Stratonovich-corrected drift vector field and the diffusion vector fields driven by WℚW^{\mathbb{Q}} and W^2,⟂\widehat{W}^{2,\perp} as follows:

|  |  |  |
| --- | --- | --- |
|  | V(0)​(z,β)=(z​(β2+ρ​σ​σβ+2​σ2​(δ−r))2​σ2−β​ρ​σβ+κ​σ​(β¯−β)σ),V(1)​(z,β)=(−βσ​zσβ​ρ),V^{(0)}(z,\beta)=\begin{pmatrix}\dfrac{z\big(\beta^{2}+\rho\sigma\sigma\_{\beta}+2\sigma^{2}(\delta-r)\big)}{2\sigma^{2}}\\[8.0pt] \dfrac{-\beta\rho\sigma\_{\beta}+\kappa\sigma(\overline{\beta}-\beta)}{\sigma}\end{pmatrix},\qquad V^{(1)}(z,\beta)=\begin{pmatrix}-\dfrac{\beta}{\sigma}z\\[4.0pt] \sigma\_{\beta}\rho\end{pmatrix}, |  |

|  |  |  |
| --- | --- | --- |
|  | V(2)​(z,β)=(0σβ​1−ρ2).V^{(2)}(z,\beta)=\begin{pmatrix}0\\[4.0pt] \sigma\_{\beta}\sqrt{1-\rho^{2}}\end{pmatrix}. |  |

First, consider the case |ρ|<1|\rho|<1. We denote by D​V(i)DV^{(i)} the Jacobian matrix of the vector V(i)V^{(i)}, i=0,1,2i=0,1,2.
The Lie-bracket between V(1)V^{(1)} and V(2)V^{(2)}, denoted by [V(1),V(2)][V^{(1)},V^{(2)}], is such that

|  |  |  |
| --- | --- | --- |
|  | [V(1),V(2)]​(z,β):=−D​V(1)​V(2)​(z,β)=−(−βσ−zσ00)​(0σβ​1−ρ2)=(σβ​1−ρ2σ​z0).[V^{(1)},V^{(2)}](z,\beta):=-DV^{(1)}V^{(2)}(z,\beta)=-\begin{pmatrix}-\frac{\beta}{\sigma}&-\frac{z}{\sigma}\\[6.0pt] 0&0\end{pmatrix}\begin{pmatrix}0\\[6.0pt] \sigma\_{\beta}\sqrt{1-\rho^{2}}\end{pmatrix}=\begin{pmatrix}\dfrac{\sigma\_{\beta}\sqrt{1-\rho^{2}}}{\sigma}z\\[6.0pt] 0\end{pmatrix}. |  |

Since z>0z>0, σβ>0\sigma\_{\beta}>0, and |ρ|<1|\rho|<1, the vectors V(2)​(z,β)V^{(2)}(z,\beta) and [V(1),V(2)]​(z,β)[V^{(1)},V^{(2)}](z,\beta) are linearly independent and therefore span 𝒪\mathcal{O}.
  
Now consider the case |ρ|=1|\rho|=1. The Lie bracket between V(0)V^{(0)} and V(1)V^{(1)} is

|  |  |  |
| --- | --- | --- |
|  | [V(0),V(1)]​(z,β):=D​V(1)​V(0)​(z,β)−D​V(0)​V(1)​(z,β)=(−z​κ​(β¯−β)σρ​σβσ​(κ​σ+ρ​σβ)).[V^{(0)},V^{(1)}](z,\beta):=DV^{(1)}V^{(0)}(z,\beta)-DV^{(0)}V^{(1)}(z,\beta)=\begin{pmatrix}-\dfrac{z\kappa(\overline{\beta}-\beta)}{\sigma}\\[6.0pt] \dfrac{\rho\sigma\_{\beta}}{\sigma}\big(\kappa\sigma+\rho\sigma\_{\beta}\big)\end{pmatrix}. |  |

Since det(V(1),[V(0),V(1)])\det(V^{(1)},[V^{(0)},V^{(1)}]) is not necessarily non-zero, we proceed to the next bracket. Therefore, we compute

|  |  |  |
| --- | --- | --- |
|  | [V(1),[V(0),V(1)]]​(z,β)=D​[V(0),V(1)]​V(1)​(z,β)−D​V(1)​[V(0),V(1)]=(ρ​σβ​zσ2​(2​κ​σ+ρ​σβ)0),[V^{(1)},[V^{(0)},V^{(1)}]](z,\beta)=D[V^{(0)},V^{(1)}]V^{(1)}(z,\beta)-DV^{(1)}[V^{(0)},V^{(1)}]=\begin{pmatrix}\dfrac{\rho\sigma\_{\beta}z}{\sigma^{2}}\big(2\kappa\sigma+\rho\sigma\_{\beta}\big)\\[6.0pt] 0\end{pmatrix}, |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | det(V(1),[V(1),[V(0),V(1)]])=−ρ2​σβ2​zσ2​(2​κ​σ+ρ​σβ)<0,\det(V^{(1)},[V^{(1)},[V^{(0)},V^{(1)}]])=-\dfrac{\rho^{2}\sigma\_{\beta}^{2}z}{\sigma^{2}}\big(2\kappa\sigma+\rho\sigma\_{\beta}\big)<0, |  |

where the last inequality is due to

|  |  |  |
| --- | --- | --- |
|  | 2​κ​σ+ρ​σβ>(2+ρ)​σβ>0,2\kappa\sigma+\rho\sigma\_{\beta}>(2+\rho)\sigma\_{\beta}>0, |  |

where Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") has been used. Hence, V(1)V^{(1)} and [V(1),[V(0),V(1)]][V^{(1)},[V^{(0)},V^{(1)}]] are linearly independent and thus span 𝒪\mathcal{O}.
Hörmander’s condition is therefore verified and we conclude that the process (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} is indeed strong Feller.
∎

###### Proposition 3.13.

v∈C∞​(𝒲)v\in C^{\infty}(\mathcal{W}) and it solves in the classical sense

|  |  |  |
| --- | --- | --- |
|  | ℒ​v−r​v+u~′​(z)+ℓ=0on𝒲,\mathcal{L}v-rv+\tilde{u}^{\prime}(z)+\ell=0\quad\text{on}\quad\mathcal{W}, |  |

where the second-order differential operator ℒ\mathcal{L} is defined as in ([3.36](#S3.E36 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).

###### Proof.

Since the infinitesimal generator of the process (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} is hypoelliptic (satisfying Hörmander’s conditions; cf. the proof of Proposition [3.12](#S3.Thmtheorem12 "Lemma 3.12. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), the drift and volatilities of (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} belong to C∞​(𝒲)C^{\infty}(\mathcal{W}), and u~′​(z)+ℓ∈C∞​(𝒲)\tilde{u}^{\prime}(z)+\ell\in C^{\infty}(\mathcal{W}), Corollary 7 in [[36](#bib.bib19 "Weak solutions in the sense of Schwartz to Dynkin’s characteristic operator equation")] implies that vv is not just a solution to ([3.35](#S3.E35 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) in the sense of Schwartz distributions but v∈C∞​(𝒲)v\in C^{\infty}(\mathcal{W}) and thus solves ([3.35](#S3.E35 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) in the classical sense.
∎

The next proposition states that the value function vv is not only locally Lipschitz continuous, but actually continuously differentiable. Its proof is based on an application of [[23](#bib.bib3 "Local times, optimal stopping and semimartingales")], upon noticing that the Hörmander’s condition, verified in the proof of Lemma [3.12](#S3.Thmtheorem12 "Lemma 3.12. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), gives existence of a smooth transition density for the process (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t}.

###### Proposition 3.14.

One has v∈C1​(𝒪)v\in C^{1}(\mathcal{O}).

###### Proof.

An application of strong Markov property allows to write

|  |  |  |
| --- | --- | --- |
|  | v​(z,β)=g​(z,β)−f​(z,β),(z,β)∈𝒪,v(z,\beta)=g(z,\beta)-f(z,\beta),\quad(z,\beta)\in\mathcal{O}, |  |

where, for any (z,β)∈𝒪(z,\beta)\in\mathcal{O}, we have set

|  |  |  |  |
| --- | --- | --- | --- |
| (3.37) |  | g​(z,β):=𝔼z,βℚ​[∫0∞e−r​t​(u~′​(Z^t)+ℓ)​𝑑t],g(z,\beta):=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)dt\bigg], |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (3.38) |  | f​(z,β):=supτ𝔼z,βℚ​[e−r​τ​g​(Z^τ,β^τ)].f(z,\beta):=\sup\_{\tau}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\Big[e^{-r\tau}g(\hat{Z}\_{\tau},\hat{\beta}\_{\tau})\Big]. |  |

Hence, the C1C^{1}-property of vv reduces to check that for gg and ff.

By the proof of Lemma [3.12](#S3.Thmtheorem12 "Lemma 3.12. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we know that the process (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} satisfies the Hörmander’s condition. Given that (modulo a change of measure to remove the quadratic term in β^\hat{\beta} appearing in the drift of the dynamics for Z^\hat{Z}) the coefficients of the evolution of (Z^t,β^t)t(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} are linear and infinitely many times differentiable (see ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.17](#S3.E17 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))), it thus follows from Theorem 9-(iii) and Remark 11 in [[3](#bib.bib4 "An elementary introduction to malliavin calculus")] or Theorem 2.3.3 in [[34](#bib.bib33 "The malliavin calculus and related topics")], among others, that, for any t>0t>0, (Z^t,βt)t(\hat{Z}\_{t},\beta\_{t})\_{t} admits a transition density that is infinitely many times differentiable in its arguments.

An application of the Dominated Convergence Theorem then shows that g∈C1​(𝒪)g\in C^{1}(\mathcal{O}). It thus remains to check the continuous differentiability of ff. With reference to the notation in [[23](#bib.bib3 "Local times, optimal stopping and semimartingales")], for any t≥0t\geq 0, we set ξt:=(Z^t,β^t)\xi\_{t}:=(\hat{Z}\_{t},\hat{\beta}\_{t}),

|  |  |  |
| --- | --- | --- |
|  | Xt:=e−r​t​g​(ξt)=𝔼z,βℚ​[∫t∞e−r​s​(u~′​(Z^s)+ℓ)​𝑑s|ℱ^t],X\_{t}:=e^{-rt}g(\xi\_{t})=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{t}^{\infty}e^{-rs}(\tilde{u}^{\prime}(\hat{Z}\_{s})+\ell)ds\,\Big|\,\hat{\mathcal{F}}\_{t}\bigg], |  |

and we can write Xt=Mt+AtX\_{t}=M\_{t}+A\_{t},
where

|  |  |  |
| --- | --- | --- |
|  | Mt:=𝔼z,βℚ​[∫0∞e−r​s​(u~′​(Z^s)+ℓ)​𝑑s|ℱ^t],andAt:=−∫0te−r​s​(u~′​(Z^s)+ℓ)​𝑑s.M\_{t}:=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rs}(\tilde{u}^{\prime}(\hat{Z}\_{s})+\ell)ds\,\Big|\,\hat{\mathcal{F}}\_{t}\bigg],\quad\text{and}\quad A\_{t}:=-\int\_{0}^{t}e^{-rs}(\tilde{u}^{\prime}(\hat{Z}\_{s})+\ell)ds. |  |

Notice that, since 𝔼z,βℚ​[∫0∞e−r​s​|u~′​(Z^s)+ℓ|​𝑑s]<∞\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rs}|\tilde{u}^{\prime}(\hat{Z}\_{s})+\ell|\;ds\bigg]<\infty by Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), (Mt)t(M\_{t})\_{t} is a uniformly integrable 𝔽^\hat{\mathbb{F}}-martingale and d​At=d​At++d​At−dA\_{t}=dA^{+}\_{t}+dA^{-}\_{t} with

|  |  |  |
| --- | --- | --- |
|  | d​At−:=−e−r​t​(u~′​(Z^t)+ℓ)+​d​tandd​At+:=e−r​t​(u~′​(Z^t)+ℓ)−​d​t,dA^{-}\_{t}:=-e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)^{+}dt\quad\text{and}\quad dA^{+}\_{t}:=e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)^{-}dt, |  |

which are clearly absolutely continuous with respect to the Lebesgue measure d​m2:=d​tdm\_{2}:=dt. Moreover, the set ∂𝒟\partial\mathcal{D} in [[23](#bib.bib3 "Local times, optimal stopping and semimartingales")] reads in our case {(z,β):z=z∗​(β)}\{(z,\beta):\,z=z^{\*}(\beta)\}, which has zero measure with respect to d​m1=d​z​d​βdm\_{1}=dzd\beta. Finally, as already noted, the process (ξt)t=(Z^t,β^t)t(\xi\_{t})\_{t}=(\hat{Z}\_{t},\hat{\beta}\_{t})\_{t} admits a density with respect to d​m1dm\_{1} having spatial derivatives which are (locally) uniformly continuous in 𝒪×[t0,t1]\mathcal{O}\times[t\_{0},t\_{1}], for any 0<t0<t1<∞0<t\_{0}<t\_{1}<\infty. Hence, Corollary 7 in [[23](#bib.bib3 "Local times, optimal stopping and semimartingales")] holds, f∈C1​(𝒪)f\in C^{1}(\mathcal{O}), and the proof is complete.
∎

An immediate consequence of Propositions [3.13](#S3.Thmtheorem13 "Proposition 3.13. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), [3.14](#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), ([3.36](#S3.E36 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), and the fact that v=0v=0 in the interior of 𝒮\mathcal{S}, denoted by 𝒮̊\mathring{\mathcal{S}}, is the following Corollary.

###### Corollary 3.15.

One has v∈C1​(𝒪)∩C∞​(𝒲∪𝒮̊)v\in C^{1}(\mathcal{O})\cap C^{\infty}(\mathcal{W}\cup\mathring{\mathcal{S}}). Furthermore, 12​β2σ2​z2​vz​z+12​σβ2​vβ​β−ρ​σβσ​β​z​vz​β\frac{1}{2}\frac{\beta^{2}}{\sigma^{2}}z^{2}v\_{zz}+\frac{1}{2}\sigma\_{\beta}^{2}v\_{\beta\beta}-\frac{\rho\sigma\_{\beta}}{\sigma}\,\beta zv\_{z\beta} admits a continuous extension to 𝒲¯\overline{\mathcal{W}}.

###### Remark 3.16.

The proof of Proposition [3.14](#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") employs the probabilistic approach developed in [[23](#bib.bib3 "Local times, optimal stopping and semimartingales")] (and recently used in [[16](#bib.bib39 "On the optimal management of public debt: a singular stochastic control problem")] and [[28](#bib.bib2 "Properties of the american price function in the heston-type models")]) to establish continuous differentiability of the value function vv in the optimal stopping problem in the presence of a smooth transition density for the underlying state process.

An alternative approach to C1C^{1}-regularity in optimal stopping was developed in [[8](#bib.bib13 "Global C1 regularity of the value function in optimal stopping problems")], where continuous differentiability of the value function is linked to the probabilistic regularity of points on the stopping boundary. In our setting, however, following the approach of [[8](#bib.bib13 "Global C1 regularity of the value function in optimal stopping problems")] is challenging, as it is not clear how to prove the probabilistic regularity of the free boundary. Indeed, such a property is typically established in the literature when one can show either monotonicity or (local) Lipschitz continuity of the free boundary. However, proving these properties is highly non-trivial in our framework because the stochastic factor (β^t)t(\hat{\beta}\_{t})\_{t} acts explicitly as stochastic volatility for the state process (Z^t)t(\hat{Z}\_{t})\_{t} (cf. ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))). This intrinsic stochastic volatility makes it difficult to exploit ([3.33](#S3.E33 "In Proposition 3.11. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.34](#S3.E34 "In Proposition 3.11. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) to establish monotonicity of z∗z^{\*} or to derive the uniform bounds required to prove that the free boundary is Lipschitz continuous (cf. [[10](#bib.bib42 "On Lipschitz continuous optimal stopping boundaries")]).

To conclude this section, we summarize the results obtained so far in the following theorem.

###### Theorem 3.17.

Recall the optimal stopping problem (cf. ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")))

|  |  |  |
| --- | --- | --- |
|  | v​(z,β):=infτ𝔼z,βℚ​[∫0τe−r​t​(u~′​(Z^t)+ℓ)​𝑑t],v(z,\beta):=\inf\_{\tau}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\tau}e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)dt\bigg], |  |

where the procesess (Z^t,βt^)t(\hat{Z}\_{t},\hat{\beta\_{t}})\_{t} are given by ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.17](#S3.E17 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).
  
There exists a lower-semicontinuous free boundary

|  |  |  |
| --- | --- | --- |
|  | z∗:ℝ→[ℓ−γ,∞]z^{\*}:\mathbb{R}\rightarrow[\ell^{-\gamma},\infty] |  |

such that the stopping and continuation regions (cf. ([3.27](#S3.E27 "In 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))) are given by

|  |  |  |
| --- | --- | --- |
|  | 𝒮={(z,β)∈𝒪:z≥z∗​(β)},and𝒲={(z,β)∈𝒪:z<z∗​(β)},\mathcal{S}=\{(z,\beta)\in\mathcal{O}:z\geq z^{\*}(\beta)\},\quad\text{and}\quad\mathcal{W}=\{(z,\beta)\in\mathcal{O}:z<z^{\*}(\beta)\}, |  |

and the optimal stopping time (cf. ([3.28](#S3.E28 "In 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))) is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.39) |  | τ∗​(z,β)=inf{s≥0:Z^s≥z∗​(β^s)},ℚz,β​-a.s.\tau^{\*}(z,\beta)=\inf\{s\geq 0:\hat{Z}\_{s}\geq z^{\*}(\hat{\beta}\_{s})\},\quad\mathbb{Q}\_{z,\beta}\text{-a.s.} |  |

Additionally, v∈C1​(𝒪)∩C∞​(𝒲∪𝒮̊)v\in C^{1}(\mathcal{O})\cap C^{\infty}(\mathcal{W}\cup\mathring{\mathcal{S}}) and the couple (v,z∗)(v,z^{\*}) satisfies (in the classical sense) the free boundary problem:

|  |  |  |
| --- | --- | --- |
|  | {ℒ​v−r​v+u~′​(z)+ℓ=0,on ​𝒲,v=0,on ​𝒮,vz​(z∗​(β),β)=0=vβ​(z∗​(β),β),β∈ℝ,\begin{cases}\mathcal{L}v-rv+\tilde{u}^{\prime}(z)+\ell=0,&\text{on }\mathcal{W},\\ v=0,&\text{on }\mathcal{S},\\ v\_{z}(z^{\*}(\beta),\beta)=0=v\_{\beta}(z^{\*}(\beta),\beta),&\beta\in\mathbb{R},\end{cases} |  |

where the infinitesimal generator ℒ\mathcal{L} is given by ([3.36](#S3.E36 "In 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).

## 4. Back to the Primal Problem

In the previous section, we characterized the solution to the auxiliary optimal stopping problem given in ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), and hence also for the problem ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) due to Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"). The following result establishes a connection between the singular control problem ([3.6](#S3.E6 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and the auxiliary optimal stopping problem ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) using probabilistic arguments as in [[2](#bib.bib16 "Irreversible investment and industry equilibrium")], [[5](#bib.bib32 "Optimal reduction of public debt under partial observation of the economic growth")] and [[16](#bib.bib39 "On the optimal management of public debt: a singular stochastic control problem")].

###### Theorem 4.1.

It holds that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | V~​(z,β)=∫0zv​(y,β)​𝑑y,(z,β)∈𝒪,\tilde{V}(z,\beta)=\int\_{0}^{z}v(y,\beta)\,dy,\quad(z,\beta)\in\mathcal{O}, |  |

where V~\tilde{V} and vv are given by ([3.10](#S3.E10 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) (equivalently, ([3.14](#S3.E14 "In Proposition 3.1. ‣ 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))). Furthermore, the optimal singular control for ([3.10](#S3.E10 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | Dt∗=exp⁡(−ξt∗),t>0,D0−∗=1,D\_{t}^{\*}=\exp(-\xi\_{t}^{\*}),\quad t>0,\quad D\_{0^{-}}^{\*}=1, |  |

where, for (z,β)∈𝒪(z,\beta)\in\mathcal{O},

|  |  |  |
| --- | --- | --- |
|  | ξt∗:=sup{y≥0∣τ∗​(z​e−y,β)<t},t>0,ξ0−∗=0,\xi\_{t}^{\*}:=\sup\left\{y\geq 0\mid\tau^{\*}(ze^{-y},\beta)<t\right\},\quad t>0,\quad\xi\_{0^{-}}^{\*}=0, |  |

and τ∗​(z,β)\tau^{\*}(z,\beta) is the optimal stopping time for ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) given in ([3.39](#S3.E39 "In Theorem 3.17. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).

###### Proof.

Let us define the candidate value function U​(z,β):=∫0zv​(y,β)​𝑑yU(z,\beta):=\int\_{0}^{z}v(y,\beta)\,dy with vv as in ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). We need to show U​(z,β)=V~​(z,β)U(z,\beta)=\tilde{V}(z,\beta) for all (z,β)∈𝒪(z,\beta)\in\mathcal{O}.
  
  
Step 1. In this step, we establish U​(z,β)≤V~​(z,β)U(z,\beta)\leq\tilde{V}(z,\beta) for all (z,β)∈𝒪(z,\beta)\in\mathcal{O}. To that end, let D∈𝒟D\in\mathcal{D} be an arbitrary admissible singular control and we define its left-continuous inverse process τD\tau^{D} as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | τD​(α):=inf{t≥0∣Dt<α},α∈(0,1].\tau^{D}(\alpha):=\inf\{t\geq 0\mid D\_{t}<\alpha\},\quad\alpha\in(0,1]. |  |

The process τD:={τD​(α)∣α∈(0,1]}\tau^{D}:=\{\tau^{D}(\alpha)\mid\alpha\in(0,1]\} has nonincreasing, left-continuous sample paths and hence it admits right-limits τ+D​(α):=inf{t≥0∣Dt≤α}\tau^{D}\_{+}(\alpha):=\inf\{t\geq 0\mid D\_{t}\leq\alpha\}. The set of points α∈(0,1]\alpha\in(0,1] at which τD​(α)​(ω)≠τ+D​(α)​(ω)\tau^{D}(\alpha)(\omega)\neq\tau^{D}\_{+}(\alpha)(\omega) is countable for a.e. ω∈Ω\omega\in\Omega. Since (Dt)t(D\_{t})\_{t} is right-continuous and τD​(α)\tau^{D}(\alpha) is the first entry time of an open set, it is an ℱ¯t+\bar{{\mathcal{F}}}\_{t+}-stopping time for any given and fixed α∈(0,1]\alpha\in(0,1]. However, (ℱ¯t)t(\bar{\mathcal{F}}\_{t})\_{t} is right-continuous, hence τD​(α)\tau^{D}(\alpha) is an 𝔽¯\bar{\mathbb{F}}-stopping time. For a fixed z>0z>0 and y∈(0,z]y\in(0,z], we consider α=yz\alpha=\frac{y}{z} in the following. Upon using sub-optimality of τD​(yz)\tau^{D}(\frac{y}{z}) for ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | v​(y,β)≤𝔼z,β​[∫0τD​(yz)e−r​t​Mt​(u~′​(yz​Zt1)+ℓ)​𝑑t].v(y,\beta)\leq\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\tau^{D}(\frac{y}{z})}e^{-rt}M\_{t}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dt\bigg]. |  |

Integrating ([4.4](#S4.E4 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) with respect to yy over [0,z][0,z] then yields

|  |  |  |
| --- | --- | --- |
|  | U​(z,β)=∫0zv​(y,β)​𝑑y≤∫0z𝔼z,β​[∫0τD​(yz)e−r​t​Mt​(u~′​(yz​Zt1)+ℓ)​𝑑t]​𝑑y.U(z,\beta)=\int\_{0}^{z}v(y,\beta)\,dy\leq\int\_{0}^{z}\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\tau^{D}(\frac{y}{z})}e^{-rt}M\_{t}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dt\bigg]\,dy. |  |

By Fubini’s Theorem, the previous inequality is equivalent to

|  |  |  |
| --- | --- | --- |
|  | U​(z,β)≤𝔼z,β​[∫0z(∫0∞𝟏{t<τD​(yz)}​e−r​t​Mt​(u~′​(yz​Zt1)+ℓ)​𝑑t)​𝑑y].U(z,\beta)\leq\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{z}\bigg(\int\_{0}^{\infty}\mathbf{1}\_{\{t<\tau^{D}(\frac{y}{z})\}}e^{-rt}M\_{t}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dt\bigg)\,dy\bigg]. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | t<τD​(yz)⇔Dt≥yz⇔y≤z​Dt,t<\tau^{D}(\frac{y}{z})\iff D\_{t}\geq\frac{y}{z}\iff y\leq zD\_{t}, |  |

we then have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | U​(z,β)≤𝔼z,β​[∫0∞e−r​t​Mt​(∫0z​Dt(u~′​(yz​Zt1)+ℓ)​𝑑y)​𝑑t].U(z,\beta)\leq\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}M\_{t}\bigg(\int\_{0}^{zD\_{t}}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dy\bigg)dt\bigg]. |  |

For the inner integral on the right-hand side of ([4.5](#S4.E5 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), upon setting w=yz​Zt1w=\frac{y}{z}Z^{1}\_{t} and noticing that, by ([3.2](#S3.E2 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), ZtD=Zt1​DtZ^{D}\_{t}=Z^{1}\_{t}D\_{t} with Zt1=eδ​t​z​ℋtZ\_{t}^{1}=e^{\delta t}z\mathcal{H}\_{t}, we have

|  |  |  |
| --- | --- | --- |
|  | ∫0z​Dt(u~′​(yz​Zt1)+ℓ)​𝑑y=zZt1​∫0ZtD(u~′​(w)+ℓ)​𝑑w=zZt1​(u~​(ZtD)+ℓ​ZtD).\int\_{0}^{zD\_{t}}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dy=\frac{z}{Z^{1}\_{t}}\int\_{0}^{Z^{D}\_{t}}(\tilde{u}^{\prime}(w)+\ell)\,dw=\frac{z}{Z^{1}\_{t}}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big). |  |

Substituting this back into ([4.5](#S4.E5 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and using the relation e−r​t​Mt​zZt1=e−δ​te^{-rt}M\_{t}\frac{z}{Z^{1}\_{t}}=e^{-\delta t} (cf. ([2.3](#S2.E3 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.2](#S3.E2 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))), we obtain

|  |  |  |
| --- | --- | --- |
|  | U​(z,β)≤𝔼z,β​[∫0∞e−δ​t​(u~​(ZtD)+ℓ​ZtD)​𝑑t].U(z,\beta)\leq\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D}\_{t})+\ell Z^{D}\_{t}\big)\,dt\bigg]. |  |

Since D∈𝒟D\in\mathcal{D} was arbitrary, we conclude U​(z,β)≤V~​(z,β)U(z,\beta)\leq\tilde{V}(z,\beta) for all (z,β)∈𝒪(z,\beta)\in\mathcal{O}.
  
  
Step 2. Let τ∗​(z,β)\tau^{\*}(z,\beta) denote the optimal stopping time for the problem ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) with initial data (z,β)(z,\beta) which is given by ([3.39](#S3.E39 "In Theorem 3.17. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). Since z↦v​(z,β)z\mapsto v(z,\beta) is nondecreasing (cf. Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), z↦τ∗​(z,β)z\mapsto\tau^{\*}(z,\beta) is nonincreasing, and therefore η↦τ∗​(z​e−η,β)\eta\mapsto\tau^{\*}(ze^{-\eta},\beta) is nondecreasing on (0,∞)(0,\infty), for all (z,β)∈𝒪(z,\beta)\in\mathcal{O}. Hence, we can define the process ξ∗\xi^{\*} as the generalized inverse

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | ξt∗:=sup{η≥0∣τ∗​(z​e−η,β)<t},t>0,ξ0−∗=0.\xi^{\*}\_{t}:=\sup\left\{\eta\geq 0\mid\tau^{\*}(ze^{-\eta},\beta)<t\right\},\quad t>0,\quad\xi\_{0^{-}}^{\*}=0. |  |

We now take Dt∗=exp⁡(−ξt∗)D^{\*}\_{t}=\exp(-\xi^{\*}\_{t}), with (ξt∗)t(\xi\_{t}^{\*})\_{t} as in ([4.6](#S4.E6 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) (cf. ([4.2](#S4.E2 "In Theorem 4.1. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) as well). Optimality of τ∗​(y,β)\tau^{\*}(y,\beta) for the optimal stopping problem ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) then implies

|  |  |  |
| --- | --- | --- |
|  | v​(y,β)=𝔼z,β​[∫0τ∗​(y,β)e−r​t​Mt​(u~′​(yz​Zt1)+ℓ)​𝑑t].v(y,\beta)=\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\tau^{\*}(y,\beta)}e^{-rt}M\_{t}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dt\bigg]. |  |

Since we have from ([4.6](#S4.E6 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))

|  |  |  |
| --- | --- | --- |
|  | Dt∗<yz⇔ξt∗>ln⁡(zy)⇔τ∗​(z​e−ln⁡(zy),β)<t⇔τ∗​(y,β)<t,\displaystyle D\_{t}^{\*}<\frac{y}{z}\iff\xi\_{t}^{\*}>\ln(\frac{z}{y})\iff\tau^{\*}(ze^{-\ln(\frac{z}{y})},\beta)<t\iff\tau^{\*}(y,\beta)<t, |  |

recalling ([4.3](#S4.E3 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) for D=D∗D=D^{\*}, we obtain
τD∗​(yz)=τ∗​(y,β)\tau^{D^{\*}}(\frac{y}{z})=\tau^{\*}(y,\beta) for all y∈(0,z]y\in(0,z]. Hence, integrating over [0,z][0,z] yields

|  |  |  |
| --- | --- | --- |
|  | U​(z,β)=∫0z𝔼z,β​[∫0τD∗​(yz)e−r​t​Mt​(u~′​(yz​Zt1)+ℓ)​𝑑t]​𝑑y.U(z,\beta)=\int\_{0}^{z}\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\tau^{D^{\*}}(\frac{y}{z})}e^{-rt}M\_{t}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dt\bigg]\,dy. |  |

As before, an application of Fubini’s Theorem leads to

|  |  |  |
| --- | --- | --- |
|  | U​(z,β)=𝔼z,β​[∫0z(∫0∞𝟏{t<τD∗​(yz)}​e−r​t​Mt​(u~′​(yz​Zt1)+ℓ)​𝑑t)​𝑑y].U(z,\beta)=\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{z}\bigg(\int\_{0}^{\infty}\mathbf{1}\_{\{t<\tau^{D^{\*}}(\frac{y}{z})\}}e^{-rt}M\_{t}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dt\bigg)\,dy\bigg]. |  |

Observing that t<τD∗​(yz)t<\tau^{D^{\*}}(\frac{y}{z}) is equivalent to y≤z​Dt∗y\leq zD^{\*}\_{t} then yields

|  |  |  |  |
| --- | --- | --- | --- |
| (4.7) |  | U​(z,β)=𝔼z,β​[∫0∞e−r​t​Mt​(∫0z​Dt∗(u~′​(yz​Zt1)+ℓ)​𝑑y)​𝑑t].U(z,\beta)=\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}M\_{t}\bigg(\int\_{0}^{zD^{\*}\_{t}}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dy\bigg)\,dt\bigg]. |  |

For the inner integral in ([4.7](#S4.E7 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) we use again the change of variables w:=yz​Zt1w:=\frac{y}{z}Z^{1}\_{t}, which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0z​Dt∗(u~′​(yz​Zt1)+ℓ)​𝑑y\displaystyle\int\_{0}^{zD^{\*}\_{t}}\big(\tilde{u}^{\prime}(\tfrac{y}{z}Z^{1}\_{t})+\ell\big)\,dy | =zZt1​∫0ZtD∗(u~′​(w)+ℓ)​𝑑w\displaystyle=\frac{z}{Z^{1}\_{t}}\int\_{0}^{Z^{D^{\*}}\_{t}}\big(\tilde{u}^{\prime}(w)+\ell\big)\,dw |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.8) |  |  | =zZt1​(u~​(ZtD∗)+ℓ​ZtD∗),\displaystyle=\frac{z}{Z^{1}\_{t}}\big(\tilde{u}(Z^{D^{\*}}\_{t})+\ell Z^{D^{\*}}\_{t}\big), |  |

and, upon using e−r​t​Mt​zZt1=e−δ​te^{-rt}M\_{t}\frac{z}{Z^{1}\_{t}}=e^{-\delta t} (cf. ([2.3](#S2.E3 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.2](#S3.E2 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))), we obtain thanks to ([4.7](#S4.E7 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([4](#S4.Ex11 "Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that

|  |  |  |
| --- | --- | --- |
|  | U​(z,β)=𝔼z,β​[∫0∞e−δ​t​(u~​(ZtD∗)+ℓ​ZtD∗)​𝑑t]≥V~​(z,β),U(z,\beta)=\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(\tilde{u}(Z^{D^{\*}}\_{t})+\ell Z^{D^{\*}}\_{t}\big)\,dt\bigg]\geq\tilde{V}(z,\beta), |  |

where we used that D∗∈𝒟D^{\*}\in\mathcal{D} since (ξt∗)t(\xi\_{t}^{\*})\_{t} is nondecreasing, càdlàg, and 𝔽¯\bar{\mathbb{F}}-adapted.
  
  
Step 3. Combining Step 1 and Step 2, we finally have V~​(z,β)=U​(z,β)=∫0zv​(y,β)​𝑑y\tilde{V}(z,\beta)=U(z,\beta)=\int\_{0}^{z}v(y,\beta)dy for all (z,β)∈𝒪(z,\beta)\in\mathcal{O} and that (Dt∗)t(D^{\*}\_{t})\_{t} as in ([4.2](#S4.E2 "In Theorem 4.1. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is the optimal singular control.
∎

A direct consequence of Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") and Corollary [3.15](#S3.Thmtheorem15 "Corollary 3.15. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") is the following Corollary.

###### Corollary 4.2.

For V~\tilde{V} as in ([3.10](#S3.E10 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and vv as in ([3.13](#S3.E13 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) (equivalently, ([3.14](#S3.E14 "In Proposition 3.1. ‣ 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))), we have

|  |  |  |
| --- | --- | --- |
|  | V~z​(z,β)=v​(z,β),(z,β)∈𝒪.\tilde{V}\_{z}(z,\beta)=v(z,\beta),\quad(z,\beta)\in\mathcal{O}. |  |

Consequently, it holds that V~∈C1​(𝒪)\tilde{V}\in C^{1}(\mathcal{O}) with V~z∈C1​(𝒪)∩C∞​(𝒲∪𝒮̊)\tilde{V}\_{z}\in C^{1}(\mathcal{O})\cap C^{\infty}(\mathcal{W}\cup\mathring{\mathcal{S}}).

The next proposition further characterizes the optimal singular control of problem ([3.6](#S3.E6 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).

###### Proposition 4.3.

Recall ([4.2](#S4.E2 "In Theorem 4.1. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). Then D∗D^{\*} admits the representation

|  |  |  |  |
| --- | --- | --- | --- |
| (4.9) |  | Dt∗=inf0≤s≤t(z∗​(βs)Zs1∧1),t≥0,D0−∗=1.D\_{t}^{\*}=\inf\_{0\leq s\leq t}\left(\frac{z^{\*}(\beta\_{s})}{Z\_{s}^{1}}\wedge 1\right),\quad t\geq 0,\quad D\_{0^{-}}^{\*}=1. |  |

###### Proof.

By ([4.2](#S4.E2 "In Theorem 4.1. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), D0−∗=1D^{\*}\_{0^{-}}=1 and for any t≥0t\geq 0 one has

|  |  |  |
| --- | --- | --- |
|  | Dt∗=exp⁡(−ξt∗),D\_{t}^{\*}=\exp(-\xi\_{t}^{\*}), |  |

where ξt∗=sup{y≥0∣τ∗​(z​e−y,β)<t}\xi\_{t}^{\*}=\sup\left\{y\geq 0\mid\tau^{\*}(ze^{-y},\beta)<t\right\} and τ∗​(z,β)=inf{s≥0:Z^sz,β≥z∗​(β^sβ)}\tau^{\*}(z,\beta)=\inf\{s\geq 0:\hat{Z}^{z,\beta}\_{s}\geq z^{\*}(\hat{\beta}^{\beta}\_{s})\} (cf. ([3.39](#S3.E39 "In Theorem 3.17. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))). We then obtain the following chain of equivalences for t≥0t\geq 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ∗​(z​e−y,β)<t\displaystyle\tau^{\*}(ze^{-y},\beta)<t | ⇔∃s∈[0,t]:e−yZs1≥z∗(βs)⇔∃s∈[0,t]:y≤ln(Zs1z∗​(βs))\displaystyle\iff\exists s\in[0,t]:e^{-y}Z\_{s}^{1}\geq z^{\*}(\beta\_{s})\iff\exists s\in[0,t]:y\leq\ln(\frac{Z\_{s}^{1}}{z^{\*}(\beta\_{s})}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔ξt∗=sup0≤s≤t[ln⁡(Zs1z∗​(βs))]+.\displaystyle\iff\xi\_{t}^{\*}=\sup\_{0\leq s\leq t}\left[\ln\left(\frac{Z\_{s}^{1}}{z^{\*}(\beta\_{s})}\right)\right]^{+}. |  |

Finally, substituting this into Dt∗=exp⁡(−ξt∗)D\_{t}^{\*}=\exp(-\xi\_{t}^{\*}) and observing that exp⁡(−(ln⁡x)+)=min⁡(1,1x)\exp(-(\ln x)^{+})=\min(1,\frac{1}{x}), we obtain ([4.9](#S4.E9 "In Proposition 4.3. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")).
  
Clearly, D∗D^{\*} as in ([4.9](#S4.E9 "In Proposition 4.3. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) is nonincreasing and càdlàg given the lower-semicontinuity of z∗z^{\*} (cf. Lemma [3.10](#S3.Thmtheorem10 "Lemma 3.10. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). As a matter of fact, t↦Dt∗t\mapsto D\_{t}^{\*} admits left-limits at any point since it is nonincreasing. To show that D∗D^{\*} has right-continuous sample paths, we follow the proof of Proposition 5.8 in [[9](#bib.bib40 "Optimal boundary surface for irreversible investment with stochastic costs")] and first notice that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.10) |  | lim infs↓t(z∗​(βs)Zs1∧1)≥z∗​(βt)Zt1∧1,\liminf\_{s\downarrow t}\left(\frac{z^{\*}(\beta\_{s})}{Z\_{s}^{1}}\wedge 1\right)\geq\frac{z^{\*}(\beta\_{t})}{Z\_{t}^{1}}\wedge 1, |  |

by the lower-semicontinuity of z∗z^{\*} (cf. Lemma [3.10](#S3.Thmtheorem10 "Lemma 3.10. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and the continuity of the state processes (Zt1,βt)t(Z\_{t}^{1},\beta\_{t})\_{t}. Moreover, from ([4.10](#S4.E10 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | lims↓tDs∗\displaystyle\lim\_{s\downarrow t}D\_{s}^{\*} | =Dt∗∧lims↓tinft<u≤s(z∗​(βu)Zu1∧1)\displaystyle=D\_{t}^{\*}\wedge\lim\_{s\downarrow t}\inf\_{t<u\leq s}\left(\frac{z^{\*}(\beta\_{u})}{Z\_{u}^{1}}\wedge 1\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.11) |  |  | =Dt∗∧lim infs↓t(z∗​(βs)Zs1∧1)\displaystyle=D\_{t}^{\*}\wedge\liminf\_{s\downarrow t}\left(\frac{z^{\*}(\beta\_{s})}{Z\_{s}^{1}}\wedge 1\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥Dt∗∧(z∗​(βt)Zt1∧1)=Dt∗.\displaystyle\geq D\_{t}^{\*}\wedge\left(\frac{z^{\*}(\beta\_{t})}{Z\_{t}^{1}}\wedge 1\right)=D\_{t}^{\*}. |  |

Since lims↓tDs∗≤Dt∗\lim\_{s\downarrow t}D\_{s}^{\*}\leq D\_{t}^{\*} by the monotonicity of t↦Dt∗t\mapsto D\_{t}^{\*}, ([4](#S4.Ex17 "Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) implies right continuity.
∎

We now have all the necessary ingredients to derive the optimal controls for our primal optimization problem (cf. ([3.11](#S3.E11 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")))

|  |  |  |
| --- | --- | --- |
|  | V​(x,β)=max(π,c)∈𝒜​(x)⁡𝔼x,β​[∫0∞e−δ​t​u​(ct)​𝑑t].V(x,\beta)=\max\_{(\pi,c)\in\mathcal{A}(x)}\mathbb{E}\_{x,\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})\,dt\bigg]. |  |

In the following, when needed, we stress the dependence of the unique strong solution to ([3.8](#S3.E8 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) on the initial data (z,β)∈𝒪(z,\beta)\in\mathcal{O} and on D∈𝒟D\in\mathcal{D} by writing Zz,β,DZ^{z,\beta,D}.

###### Proposition 4.4.

Let V~\tilde{V} as in ([3.10](#S3.E10 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) (see also ([4.1](#S4.E1 "In Theorem 4.1. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))). We have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.12) |  | V​(x,β)=infz>0(V~​(z,β)+z​x),(x,β)∈𝒪,V(x,\beta)=\inf\_{z>0}\big(\tilde{V}(z,\beta)+zx\big),\quad(x,\beta)\in\mathcal{O}, |  |

and for all (x,β)∈𝒪(x,\beta)\in\mathcal{O}, there exists z^:=z^​(x,β)>0\hat{z}:=\hat{z}(x,\beta)>0 such that V~z​(z^,β)=−x\tilde{V}\_{z}(\hat{z},\beta)=-x. Furthermore, the optimal primal controls for ([3.11](#S3.E11 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) are given by

|  |  |  |
| --- | --- | --- |
|  | ct∗=(Ztz^,β,D∗)−1γandπt∗=βtσ2​Ztz^,β,D∗​V~z​z​(Ztz^,β,D∗,βt)−ρ​σβσ​V~z​β​(Ztz^,β,D∗,βt),t≥0,c\_{t}^{\*}=(Z\_{t}^{\hat{z},\beta,D^{\*}})^{-\frac{1}{\gamma}}\qquad\text{and}\qquad\pi\_{t}^{\*}=\frac{\beta\_{t}}{\sigma^{2}}Z\_{t}^{\hat{z},\beta,D^{\*}}\tilde{V}\_{zz}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t})-\frac{\rho\sigma\_{\beta}}{\sigma}\tilde{V}\_{z\beta}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t}),\quad t\geq 0, |  |

where (Dt∗)t(D^{\*}\_{t})\_{t} is the optimal singular control for problem ([3.6](#S3.E6 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")); that is

|  |  |  |
| --- | --- | --- |
|  | Dt∗=inf0≤s≤t(z∗​(βs)Zs1)∧1,t≥0,D0−∗=1.D\_{t}^{\*}=\inf\_{0\leq s\leq t}\left(\frac{z^{\*}(\beta\_{s})}{Z\_{s}^{1}}\right)\wedge 1,\quad t\geq 0,\quad D\_{0^{-}}^{\*}=1. |  |

Finally, the optimal wealth process is such that

|  |  |  |
| --- | --- | --- |
|  | Xt∗=−V~z​(Ztz^,β,D∗,βt),t≥0,X\_{t}^{\*}=-\tilde{V}\_{z}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t}),\quad t\geq 0, |  |

with (Xt∗)t≥0:=(Xtπ∗,c∗)t≥0(X\_{t}^{\*})\_{t\geq 0}:=(X\_{t}^{\pi^{\*},c^{\*}})\_{t\geq 0}.

###### Proof.

Step 1. We first establish the existence of z^\hat{z} such that V~z​(z^,β)=−x\tilde{V}\_{z}(\hat{z},\beta)=-x for all x>0x>0. Notice that the minimization problem infz>0(V~​(z,β)+z​x)\inf\_{z>0}(\tilde{V}(z,\beta)+zx) is equivalent to solving

|  |  |  |  |
| --- | --- | --- | --- |
| (4.13) |  | v​(z,β)=−x,v(z,\beta)=-x, |  |

upon using the identity V~z=v\tilde{V}\_{z}=v given by Corollary [4.2](#S4.Thmtheorem2 "Corollary 4.2. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
Since vv is continuous (see Proposition [3.8](#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), nondecreasing in zz (see Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), by Proposition [3.7](#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") satisfies

|  |  |  |
| --- | --- | --- |
|  | limz→0v​(z,β)=−∞,\lim\_{z\to 0}v(z,\beta)=-\infty, |  |

as well as v​(z,β)=0v(z,\beta)=0 for any z≥z∗​(β)z\geq z^{\*}(\beta) and z↦v​(z,β)z\mapsto v(z,\beta) is strictly increasing on 𝒲\mathcal{W}, there exists a unique 0<z^<z∗​(β)0<\hat{z}<z^{\*}(\beta) such that V~z​(z^,β)=−x\tilde{V}\_{z}(\hat{z},\beta)=-x.
  
  
Step 2. Next, we prove that the strong duality relation ([4.12](#S4.E12 "In Proposition 4.4. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) indeed holds. Since we have already shown the weak-duality (cf. ([3.5](#S3.E5 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))), namely

|  |  |  |  |
| --- | --- | --- | --- |
| (4.14) |  | V​(x,β)≤infz>0(V~​(z,β)+z​x),V(x,\beta)\leq\inf\_{z>0}\bigg(\tilde{V}(z,\beta)+zx\bigg), |  |

it suffices to consider the reverse inequality. Recall the optimal singular control to problem ([3.6](#S3.E6 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))(\ref{SCP}), given by ([4.9](#S4.E9 "In Proposition 4.3. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), and define ct∗:=(Ztz,β,D∗)−1γc\_{t}^{\*}:=(Z\_{t}^{z,\beta,D^{\*}})^{-\frac{1}{\gamma}} as the candidate optimal consumption plan. Then, we set

|  |  |  |
| --- | --- | --- |
|  | χ​(z):=𝔼z,β​[∫0∞ℋt​Dt∗​(ct∗−ℓ)​𝑑t],\chi(z):=\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}^{\*}(c\_{t}^{\*}-\ell)\,dt\bigg], |  |

with the aim of showing that actually χ​(z)=−V~z​(z,β)\chi(z)=-\tilde{V}\_{z}(z,\beta) for all (z,β)∈𝒪(z,\beta)\in\mathcal{O}. To that end, we fix (z,β)∈𝒪(z,\beta)\in\mathcal{O} and ε>0\varepsilon>0 (small enough), and note that D∗D^{\*} is independent of ε\varepsilon. Since D∗D^{\*} is suboptimal for V~​(z+ε,β)\tilde{V}(z+\varepsilon,\beta), we find

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~​(z+ε,β)−V~​(z,β)\displaystyle\tilde{V}(z+\varepsilon,\beta)-\tilde{V}(z,\beta) | ≤𝔼​[∫0∞e−δ​t​((u~​(Ztz+ε,β,D∗)−u~​(Ztz,β,D∗))+ℓ​(Ztz+ε,β,D∗−Ztz,β,D∗))​𝑑t]\displaystyle\leq\mathbb{E}\Big[\int\_{0}^{\infty}e^{-\delta t}\Big(\big(\tilde{u}(Z\_{t}^{z+\varepsilon,\beta,D^{\*}})-\tilde{u}(Z\_{t}^{z,\beta,D^{\*}})\big)+\ell\big(Z\_{t}^{z+\varepsilon,\beta,D^{\*}}-Z\_{t}^{z,\beta,D^{\*}}\big)\Big)dt\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =((z+ε)−1−γγ−z−1−γγ)​𝔼​[∫0∞e−δ​t​u~​(Zt1,β,D∗)​𝑑t]\displaystyle=\Big((z+\varepsilon)^{-\frac{1-\gamma}{\gamma}}-z^{-\frac{1-\gamma}{\gamma}}\Big)\mathbb{E}\Big[\int\_{0}^{\infty}e^{-\delta t}\tilde{u}\Big(Z\_{t}^{1,\beta,D^{\*}}\Big)dt\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ε​ℓ​𝔼​[∫0∞e−δ​t​Zt1,β,D∗​𝑑t].\displaystyle\quad+\varepsilon\,\ell\,\mathbb{E}\Big[\int\_{0}^{\infty}e^{-\delta t}Z\_{t}^{1,\beta,D^{\*}}dt\Big]. |  |

Dividing by ε\varepsilon and letting ε→0\varepsilon\to 0 gives

|  |  |  |  |
| --- | --- | --- | --- |
| (4.15) |  | lim supε→0V~​(z+ε,β)−V~​(z,β)ε≤𝔼​[∫0∞e−δ​t​(−(Ztz,β,D∗)−1γ+ℓ)​Zt1,β,D∗​𝑑t].\limsup\_{\varepsilon\to 0}\frac{\tilde{V}(z+\varepsilon,\beta)-\tilde{V}(z,\beta)}{\varepsilon}\leq\mathbb{E}\Big[\int\_{0}^{\infty}e^{-\delta t}\Big(-(Z\_{t}^{z,\beta,D^{\*}})^{-\frac{1}{\gamma}}+\ell\Big)Z\_{t}^{1,\beta,D^{\*}}dt\Big]. |  |

A symmetric argument applied to V~​(z,β)−V~​(z−ε,β)\tilde{V}(z,\beta)-\tilde{V}(z-\varepsilon,\beta), by using now that D∗D^{\*} is suboptimal for the problem starting at (z−ε,β)(z-\varepsilon,\beta), gives

|  |  |  |  |
| --- | --- | --- | --- |
| (4.16) |  | lim infε→0V~​(z,β)−V~​(z−ε,β)ε≥𝔼​[∫0∞e−δ​t​(−(Ztz,β,D∗)−1γ+ℓ)​Zt1,β,D∗​𝑑t].\liminf\_{\varepsilon\to 0}\frac{\tilde{V}(z,\beta)-\tilde{V}(z-\varepsilon,\beta)}{\varepsilon}\geq\mathbb{E}\Big[\int\_{0}^{\infty}e^{-\delta t}\Big(-(Z\_{t}^{z,\beta,D^{\*}})^{-\frac{1}{\gamma}}+\ell\Big)Z\_{t}^{1,\beta,D^{\*}}dt\Big]. |  |

Upon using that V~z\tilde{V}\_{z} exists and is continuous (as V~z=v\tilde{V}\_{z}=v), ([4.15](#S4.E15 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([4.16](#S4.E16 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) imply

|  |  |  |
| --- | --- | --- |
|  | V~z​(z,β)=𝔼​[∫0∞e−δ​t​(−(Ztz,β,D∗)−1γ+ℓ)​Zt1,β,D∗​𝑑t].\tilde{V}\_{z}(z,\beta)=\mathbb{E}\Big[\int\_{0}^{\infty}e^{-\delta t}\Big(-(Z\_{t}^{z,\beta,D^{\*}})^{-\frac{1}{\gamma}}+\ell\Big)Z\_{t}^{1,\beta,D^{\*}}dt\Big]. |  |

Since now (Ztz,β,D∗)−1γ=ct∗(Z\_{t}^{z,\beta,D^{\*}})^{-\frac{1}{\gamma}}=c\_{t}^{\*} and e−δ​t​Zt1,β,D∗=ℋt​Dt∗e^{-\delta t}Z\_{t}^{1,\beta,D^{\*}}=\mathcal{H}\_{t}D\_{t}^{\*} (cf. ([3.2](#S3.E2 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))), we have

|  |  |  |
| --- | --- | --- |
|  | −V~z​(z,β)=𝔼z,β​[∫0∞ℋt​Dt∗​(ct∗−ℓ)​𝑑t]=χ​(z).-\tilde{V}\_{z}(z,\beta)=\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}^{\*}(c\_{t}^{\*}-\ell)\,dt\bigg]=\chi(z). |  |

In particular, for z^\hat{z} as in Step 1, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.17) |  | −V~z​(z^,β)=𝔼z^,β​[∫0∞ℋt​Dt∗​(ct∗−ℓ)​𝑑t]=χ​(z^),-\tilde{V}\_{z}(\hat{z},\beta)=\mathbb{E}\_{\hat{z},\beta}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}^{\*}(c\_{t}^{\*}-\ell)\,dt\bigg]=\chi(\hat{z}), |  |

which, combined with x=−V~z​(z^,β)x=-\tilde{V}\_{z}(\hat{z},\beta), yields x=χ​(z^)x=\chi(\hat{z}).
  
The previous findings and ([3.2](#S3.E2 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) yield the following chain of equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | z^​𝔼z^,β​[∫0∞ℋt​Dt∗​(ct∗−ℓ)​𝑑t]\displaystyle\hat{z}\mathbb{E}\_{\hat{z},\beta}\bigg[\int\_{0}^{\infty}\mathcal{H}\_{t}D\_{t}^{\*}(c\_{t}^{\*}-\ell)\,dt\bigg] | =𝔼z^,β​[∫0∞e−δ​t​ZtD∗​(ct∗−ℓ)​𝑑t]\displaystyle=\mathbb{E}\_{\hat{z},\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}Z\_{t}^{D^{\*}}(c\_{t}^{\*}-\ell)\,dt\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼z^,β​[∫0∞e−δ​t​(u​(ct∗)−u~​(ZtD∗))​𝑑t]−𝔼z^,β​[∫0∞e−δ​t​ℓ​ZtD∗​𝑑t],\displaystyle=\mathbb{E}\_{\hat{z},\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}\big(u(c\_{t}^{\*})-\tilde{u}(Z\_{t}^{D^{\*}})\big)\,dt\bigg]-\mathbb{E}\_{\hat{z},\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}\ell Z\_{t}^{D^{\*}}\,dt\bigg], |  |

and hence, by using ([4.14](#S4.E14 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~​(z^,β)+z^​x\displaystyle\tilde{V}(\hat{z},\beta)+\hat{z}x | =𝔼z^,β​[∫0∞e−δ​t​u​(ct∗)​𝑑t]≤sup(π,c)∈𝒜​(x)𝔼x,β​[∫0∞e−δ​t​u​(ct)​𝑑t]\displaystyle=\mathbb{E}\_{\hat{z},\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t}^{\*})\,dt\bigg]\leq\sup\_{(\pi,c)\in\mathcal{A}(x)}\mathbb{E}\_{x,\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t})\,dt\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.18) |  |  | ≤infz>0(V~​(z,β)+z​x)≤V~​(z^,β)+z^​x.\displaystyle\leq\inf\_{z>0}\big(\tilde{V}(z,\beta)+zx\big)\leq\tilde{V}(\hat{z},\beta)+\hat{z}x. |  |

This in turn yields the strong duality

|  |  |  |
| --- | --- | --- |
|  | V​(x,β)=infz>0(V~​(z,β)+z​x)=V~​(z^,β)+z^​x.V(x,\beta)=\inf\_{z>0}(\tilde{V}(z,\beta)+zx)=\tilde{V}(\hat{z},\beta)+\hat{z}x. |  |

Step 3. In this step, we derive the optimal primal controls associated to the stochastic control problem ([3.11](#S3.E11 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). It follows from ([4](#S4.Ex32 "Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that

|  |  |  |
| --- | --- | --- |
|  | V​(x,β)=𝔼z^,β​[∫0∞e−δ​t​u​(ct∗)​𝑑t],V(x,\beta)=\mathbb{E}\_{\hat{z},\beta}\bigg[\int\_{0}^{\infty}e^{-\delta t}u(c\_{t}^{\*})\,dt\bigg], |  |

so that ct∗=(Ztz^,β,D∗)−1γc\_{t}^{\*}=(Z\_{t}^{\hat{z},\beta,D^{\*}})^{-\frac{1}{\gamma}} is optimal. By Proposition [2.6](#S2.E6 "In item 1 ‣ Proposition 2.4. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), there exists an investment strategy π∗\pi^{\*} such that (π∗,c∗)∈𝒜​(x)(\pi^{\*},c^{\*})\in\mathcal{A}(x). Moreover, by the strong Markov property and x=−V~z​(z^,β)x=-\tilde{V}\_{z}(\hat{z},\beta), we have

|  |  |  |
| --- | --- | --- |
|  | Xt∗=−V~z​(Ztz^,β,D∗,βt).X\_{t}^{\*}=-\tilde{V}\_{z}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t}). |  |

Recalling the regularity of V~z=v\tilde{V}\_{z}=v as in Corollary [3.15](#S3.Thmtheorem15 "Corollary 3.15. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), noticing that ℙ​((Ztz^,β,𝒟∗,βt)∈𝒲)=1\mathbb{P}((Z\_{t}^{\hat{z},\beta,\mathcal{D}^{\*}},\beta\_{t})\in\mathcal{W})=1 for all t≥0−t\geq 0-, and that the support of the random measure d​D⋅∗dD^{\*}\_{\cdot} is {t≥0:V~z​z​(z∗​(βt),βt)=0}\{t\geq 0:\,\tilde{V}\_{zz}(z^{\*}(\beta\_{t}),\beta\_{t})=0\} (due to V~z​z=vz\tilde{V}\_{zz}=v\_{z} and Proposition [3.14](#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), an application of Itô-Meyer’s formula leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.19) |  | d​Xt∗=\displaystyle dX\_{t}^{\*}= | −V~z​z​(Ztz^,β,D∗,βt)​[(δ−r)​Ztz^,β,D∗​d​t−βtσ​Ztz^,β,D∗​d​Wt]\displaystyle-\tilde{V}\_{zz}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t})\left[(\delta-r)Z\_{t}^{\hat{z},\beta,D^{\*}}\,dt-\frac{\beta\_{t}}{\sigma}Z\_{t}^{\hat{z},\beta,D^{\*}}\,dW\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −V~z​β​(Ztz^,β,D∗,βt)​[κ​(β¯−βt)​d​t+σβ​d​Wtβ]\displaystyle-\tilde{V}\_{z\beta}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t})\left[\kappa(\overline{\beta}-\beta\_{t})\,dt+\sigma\_{\beta}\,dW\_{t}^{\beta}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​βt2σ2​(Ztz^,β,D∗)2​V~z​z​z​(Ztz^,β,D∗,βt)​d​t\displaystyle-\frac{1}{2}\frac{\beta\_{t}^{2}}{\sigma^{2}}(Z\_{t}^{\hat{z},\beta,D^{\*}})^{2}\tilde{V}\_{zzz}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t})\;dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​σβ2​V~z​β​β​(Ztz^,β,D∗,βt)​d​t+βtσ​Ztz^,β,D∗​σβ​ρ​V~z​z​β​(Ztz^,β,D∗,βt)​d​t,t≥0.\displaystyle-\frac{1}{2}\sigma\_{\beta}^{2}\tilde{V}\_{z\beta\beta}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t})\,dt+\frac{\beta\_{t}}{\sigma}Z\_{t}^{\hat{z},\beta,D^{\*}}\sigma\_{\beta}\rho\tilde{V}\_{zz\beta}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t})\,dt,\quad t\geq 0. |  |

Recalling that d​Wtβ=ρ​d​Wt+1−ρ2​d​Wt2,⟂dW^{\beta}\_{t}=\rho dW\_{t}+\sqrt{1-\rho^{2}}dW^{2,\perp}\_{t} due to C​o​r​r​(Wt,Wtβ)=ρ​tCorr(W\_{t},W^{\beta}\_{t})=\rho t, comparing the d​WtdW\_{t} terms in ([2.1](#S2.E1 "In 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([4.19](#S4.E19 "In Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) finally gives

|  |  |  |
| --- | --- | --- |
|  | πt∗=βtσ2​Ztz^,β,D∗​V~z​z​(Ztz^,β,D∗,βt)−ρ​σβσ​V~z​β​(Ztz^,β,D∗,βt),t≥0,\pi\_{t}^{\*}=\frac{\beta\_{t}}{\sigma^{2}}Z\_{t}^{\hat{z},\beta,D^{\*}}\tilde{V}\_{zz}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t})-\frac{\rho\sigma\_{\beta}}{\sigma}\tilde{V}\_{z\beta}(Z\_{t}^{\hat{z},\beta,D^{\*}},\beta\_{t}),\quad t\geq 0, |  |

which completes the proof.
∎

## 5. Numerical Illustrations

In this section, we provide numerical illustrations of our results. In order to illustrate the singular control mechanism and how (Dt∗)t(D^{\*}\_{t})\_{t} ensures the nonnegativity of the wealth process, in Figure [1](#S5.F1 "Figure 1 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we simulate the optimal primal state process (Xtπ∗,c∗)t(X\_{t}^{\pi^{\*},c^{\*}})\_{t}, the optimal dual state process (Ztz^,D∗)t(Z^{\hat{z},D^{\*}}\_{t})\_{t}, and the optimal singular control (Dt∗)t(D^{\*}\_{t})\_{t}. For this simulation, we fix the parameters: r=0.03r=0.03, δ=0.04\delta=0.04, ℓ=0.6\ell=0.6, γ=1.5\gamma=1.5, κ=0.25\kappa=0.25, β¯=0.05\bar{\beta}=0.05, σβ=0.03\sigma\_{\beta}=0.03, σ=0.18\sigma=0.18, and ρ=0.6\rho=0.6.
  
Figure [1(a)](#S5.F1.sf1 "In Figure 1 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") depicts a path of the controlled dual state process (Ztz^,D∗)t(Z^{\hat{z},D^{\*}}\_{t})\_{t} (black line) and the (moving stochastic) free boundary (z∗​(βt))t(z^{\*}(\beta\_{t}))\_{t} (red line). Observe that each time the dual state hits the free boundary, it is reflected and pushed downward. This action is driven by the singular control (Dt∗)t(D^{\*}\_{t})\_{t}. Indeed, from Figure [1(b)](#S5.F1.sf2 "In Figure 1 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we see that each time the free boundary is reached, the decreasing singular control jumps to keep the process below the boundary. Crucially, in Figure [1(c)](#S5.F1.sf3 "In Figure 1 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we see that the points where the dual state touches the free boundary correspond exactly to the wealth process hitting zero. At these points, the wealth is reflected upward, ensuring that the no-borrowing constraint is satisfied.

![Refer to caption](2603.02820v1/Plots/Simulation_Z.png)


(a) Simulation of dual state (Zt∗)t(Z^{\*}\_{t})\_{t}.

![Refer to caption](2603.02820v1/Plots/SimulationD.png)


(b) Simulation of optimal singular control (Dt∗)t(D^{\*}\_{t})\_{t}.

![Refer to caption](2603.02820v1/Plots/SimulationX.png)


(c) Simulation of optimal wealth (Xt∗)t(X^{\*}\_{t})\_{t}.

Figure 1. Simulation of optimal state processes.

One of the main contributions of this paper is the inclusion of the stochastic factor (βt)t(\beta\_{t})\_{t}, representing the expected excess return of the risky asset. In contrast to the standard Merton model, where (βt)t(\beta\_{t})\_{t} is constant, we model it as a stochastic process. Figure [2](#S5.F2 "Figure 2 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") compares the optimal wealth trajectories under these two frameworks.
  
For this comparison, we fix the parameters: r=0.03r=0.03, δ=0.04\delta=0.04, ℓ=0.6\ell=0.6, γ=1.5\gamma=1.5, β¯=0.05\bar{\beta}=0.05, and σ=0.18\sigma=0.18. In the stochastic case, we additionally set κ=0.25\kappa=0.25 and σβ=0.03\sigma\_{\beta}=0.03, while in the constant case we set κ=0=σβ\kappa=0=\sigma\_{\beta} and β0=β¯\beta\_{0}=\bar{\beta} to ensure that (βt)t≡β¯(\beta\_{t})\_{t}\equiv\bar{\beta}. We perform the comparison for three distinct correlation parameters: ρ∈{−0.6,0,0.6}\rho\in\{-0.6,0,0.6\}. To isolate the impact of the stochastic factor (βt)t(\beta\_{t})\_{t}, we fix the same path for the Brownian motion (Wt)t(W\_{t})\_{t} driving the risky asset price in both cases. For the agent who assumes a stochastic (βt)t(\beta\_{t})\_{t}, we simulate 10,00010,000 paths of the Brownian motion (Wtβ)t(W^{\beta}\_{t})\_{t} driving the stochastic factor, and plot the optimal wealth as the average over these paths (blue line). The red line depicts the wealth of the agent who assumes a constant (βt)t(\beta\_{t})\_{t}. In the following, we denote by *Stochastic Agent* the agent with stochastic (βt)t(\beta\_{t})\_{t}, and by *Constant Agent* the agent with constant (βt)t(\beta\_{t})\_{t}.
  
In all scenarios, the Stochastic Agent systematically accumulates greater long-term wealth. This outcome is driven by a universal mechanism: The Stochastic Agent’s strategic asset allocation, namely increasing exposure to the risky asset when expected returns are high (that is, when βt\beta\_{t} is high), generates substantial excess returns. As a result, the Stochastic Agent’s wealth exceeds that of the Constant Agent in the long-run. In contrast, the Constant Agent lacks this flexibility and is confined to a rigid strategy that systematically fails to exploit time-varying risk premia, leading to inferior wealth accumulation.

![Refer to caption](2603.02820v1/Plots/comparison_rho-0.6.png)


(a) Case ρ=−0.6\rho=-0.6: Comparison of the optimal wealth trajectories for the Stochastic Agent and the Constant Agent ((βt)t≡β¯(\beta\_{t})\_{t}\equiv\bar{\beta}).

![Refer to caption](2603.02820v1/Plots/comparison_rho0.png)


(b) Case ρ=0\rho=0: Comparison of the optimal wealth trajectories for the Stochastic Agent and the Constant Agent ((βt)t≡β¯(\beta\_{t})\_{t}\equiv\bar{\beta}).

![Refer to caption](2603.02820v1/Plots/Comparison_rho0.6.png)


(c) Case ρ=0.6\rho=0.6: Comparison of the optimal wealth trajectories for the Stochastic Agent and the Constant Agent ((βt)t≡β¯(\beta\_{t})\_{t}\equiv\bar{\beta}).

Figure 2. Comparison of optimal wealth trajectories between the Stochastic Agent and the Constant Agent (βt≡β¯\beta\_{t}\equiv\bar{\beta}) for different values of ρ\rho. The Brownian path of (Wt)t(W\_{t})\_{t} is fixed across both cases, while the Stochastic Agent’s wealth is averaged over 10,000 Brownian paths of (Wtβ)t(W^{\beta}\_{t})\_{t}.

While this long-run dominance is consistent across all regimes, short-run dynamics differ. For nonnegative correlations (ρ=0\rho=0 and ρ=0.6\rho=0.6), the advantage materializes immediately, and the Stochastic Agent maintains wealth consistently above that of the Constant Agent throughout the simulation. In contrast, the regime with ρ=−0.6\rho=-0.6 exhibits a distinct crossing pattern. In this case, the negative correlation provides a natural hedge, as market downturns signal improved future investment opportunities. This added safety reduces the agent’s precautionary savings motive and induces a positive income effect, effectively making the agent feel wealthier and optimally consume more in the present. The resulting higher initial consumption causes the Stochastic Agent to temporarily lag behind the Constant Agent. However, as the benefits of flexible investment decisions accumulate, the wealth paths eventually cross, confirming that the long-run advantage of adapting to (βt)t(\beta\_{t})\_{t} ultimately dominates.
  
  
Next, we illustrate the optimal control strategies (πt∗)t(\pi^{\*}\_{t})\_{t} and (ct∗)t(c^{\*}\_{t})\_{t} given by Proposition [4.4](#S4.Thmtheorem4 "Proposition 4.4. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") for different parameter choices. To visualize the controls effectively, we plot the optimal strategies as functions of wealth XtX\_{t}, while fixing βt\beta\_{t} at its equilibrium level β¯\bar{\beta}. It is important to note that, while the stochastic factor is held constant in these figures, the policy functions and underlying value functions are derived from the full dynamic model. Thus, the agent explicitly accounts for the stochastic evolution of (βt)t(\beta\_{t})\_{t} throughout the optimization, and the plots represent a cross-section of this dynamic strategy.
  
In Figure [3](#S5.F3 "Figure 3 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we compare the optimal control strategies (πt∗)t(\pi^{\*}\_{t})\_{t} and (ct∗)t(c^{\*}\_{t})\_{t} for different values of labor income ℓ∈{0.2,0.6,1}\ell\in\{0.2,0.6,1\}, while we fix the other parameters as: r=0.03,δ=0.04,γ=1.5,κ=0.25,β¯=0.05,σβ=0.03,σ=0.18r=0.03,\;\delta=0.04,\;\gamma=1.5,\;\kappa=0.25,\;\bar{\beta}=0.05,\;\sigma\_{\beta}=0.03,\;\sigma=0.18, and ρ=0.6\rho=0.6.
  
We observe that both consumption and risky investment are increasing in wealth XtX\_{t} and labor income ℓ\ell. This is consistent with standard economic intuition: higher levels of wealth and labor income increase the agent’s total effective wealth, thereby relaxing the budget constraint. Consequently, the agent increases both consumption and their allocation to the risky asset.

![Refer to caption](2603.02820v1/Plots/investment_labor.png)


(a) Optimal investment policy πt∗\pi^{\*}\_{t} for different values of labor income ℓ\ell.

![Refer to caption](2603.02820v1/Plots/income_consumption.png)


(b) Optimal consumption policy ct∗c^{\*}\_{t} for different values of labor income ℓ\ell.

Figure 3. Optimal policies for different values of labor income ℓ\ell.

In Figure [4](#S5.F4 "Figure 4 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we compare the optimal control strategies (πt∗)t(\pi^{\*}\_{t})\_{t} and (ct∗)t(c^{\*}\_{t})\_{t} for different values of risk aversion γ∈{1.2,1.5,2}\gamma\in\{1.2,1.5,2\}, while we fix the other parameters as: r=0.03,δ=0.04,ℓ=0.6,κ=0.25,β¯=0.05,σβ=0.03,σ=0.18r=0.03,\;\delta=0.04,\;\ell=0.6,\;\kappa=0.25,\;\bar{\beta}=0.05,\;\sigma\_{\beta}=0.03,\;\sigma=0.18, and ρ=0.6\rho=0.6.
  
As before, we observe that both optimal consumption (ct∗)t(c^{\*}\_{t})\_{t} and risky investment (πt∗)t(\pi^{\*}\_{t})\_{t} are strictly increasing in wealth XtX\_{t} since the agent has more money to allocate. Regarding the effect of risk preferences, the risky investment (πt∗)t(\pi^{\*}\_{t})\_{t} is decreasing in the risk aversion parameter γ\gamma. This inverse relationship is consistent with Merton’s classic results, reflecting that more risk-averse agents fear market volatility more and consequently reduce their exposure to the risky asset.
  
Conversely, the consumption policy (ct∗)t(c^{\*}\_{t})\_{t} roughly shifts upward as γ\gamma increases. This behavior is driven by the Intertemporal Elasticity of Substitution (IES). Agents with lower risk aversion (higher IES) are more willing to postpone current consumption to capitalize on investment opportunities, whereas highly risk-averse agents (lower IES) invest less and choose to consume larger amounts of their current wealth.

![Refer to caption](2603.02820v1/Plots/riskaversion_investment.png)


(a) Optimal investment policy πt∗\pi^{\*}\_{t} for different values of risk aversion γ\gamma.

![Refer to caption](2603.02820v1/Plots/riskaversion_consumption.png)


(b) Optimal consumption policy ct∗c^{\*}\_{t} for different values of risk aversion γ\gamma.

Figure 4. Optimal policies for different values of risk aversion γ\gamma.

In Figure [5](#S5.F5 "Figure 5 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"), we compare the optimal control strategies (πt∗)t(\pi^{\*}\_{t})\_{t} and (ct∗)t(c^{\*}\_{t})\_{t} for different values of the correlation parameter ρ∈{−0.6,0,0.6}\rho\in\{-0.6,0,0.6\}, while we fix the other parameters as: r=0.03,δ=0.04,ℓ=0.6,γ=1.5,κ=0.25,β¯=0.05,σβ=0.03r=0.03,\;\delta=0.04,\;\ell=0.6,\;\gamma=1.5,\;\kappa=0.25,\;\bar{\beta}=0.05,\;\sigma\_{\beta}=0.03, and σ=0.18\sigma=0.18.
  
We observe that the consumption policy (ct∗)t(c\_{t}^{\*})\_{t} is increasing in ρ\rho. In particular, the agent with positive correlation (ρ=0.6\rho=0.6) consumes the most, while the agent with negative correlation (ρ=−0.6\rho=-0.6) consumes the least. This pattern reflects the precautionary savings motive. When ρ<0\rho<0, the risky asset acts as an intertemporal hedge, encouraging the agent to take a highly leveraged position. This leverage increases portfolio volatility, and to guard against risk and avoid breaching the borrowing constraint, the agent reduces current consumption. By contrast, when ρ>0\rho>0, the asset offers weaker hedging benefits, leading to lower risky exposure, reduced volatility, and a weaker precautionary savings motive, allowing the agent to consume more.
  
The investment policy (πt∗)t(\pi\_{t}^{\*})\_{t} is non-monotonic with respect to ρ\rho. It rises with ρ\rho up to a wealth level of roughly Xt≈6.5X\_{t}\approx 6.5, and then declines for higher wealth. In the high-wealth region, the policy follows standard Merton intuition: the negatively correlated agent (ρ=−0.6\rho=-0.6) invests more aggressively to exploit the asset’s hedging properties, while investment declines with ρ\rho. At lower wealth levels (Xt<6.5X\_{t}<6.5), however, the pattern flips. The hedging agent’s highly leveraged strategy becomes too risky because of the threat of immediate bankruptcy, forcing sharp deleveraging. Meanwhile, the positively correlated agent (ρ=0.6\rho=0.6), who naturally maintains a more conservative position, is less constrained and thus holds a higher allocation in the low-wealth region.

![Refer to caption](2603.02820v1/Plots/rho_investment.png)


(a) Optimal investment policy πt∗\pi^{\*}\_{t} for different values of correlation ρ\rho.

![Refer to caption](2603.02820v1/Plots/rho_consumption.png)


(b) Optimal consumption policy ct∗c^{\*}\_{t} for different values of correlation ρ\rho.

Figure 5. Optimal policies for different values of correlation ρ\rho.

Continuing with our cross-sectional approach, Figure [6](#S5.F6 "Figure 6 ‣ 5. Numerical Illustrations ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") compares the optimal control policies (πt∗)t(\pi^{\*}\_{t})\_{t} and (ct∗)t(c^{\*}\_{t})\_{t} for different values of expected excess returns βt∈{0.02,0.05,0.12}\beta\_{t}\in\{0.02,0.05,0.12\}, while we fix the other parameters as: r=0.03,δ=0.04,ℓ=0.6,γ=1.5,κ=0.25,β¯=0.05,σβ=0.03,σ=0.18r=0.03,\;\delta=0.04,\;\ell=0.6,\;\gamma=1.5,\;\kappa=0.25,\;\bar{\beta}=0.05,\;\sigma\_{\beta}=0.03,\;\sigma=0.18, and ρ=0.6\rho=0.6.
  
We observe that the investment policy (πt∗)t(\pi\_{t}^{\*})\_{t} is strictly increasing in the expected excess return βt\beta\_{t}. When the risk premium is high, the agent aggressively leverages the portfolio to capitalize on favorable investment opportunities. Conversely, when the premium is low, the agent substantially reduces exposure to the risky asset.
  
The consumption policy (ct∗)t(c\_{t}^{\*})\_{t} displays a non-monotonic relationship with βt\beta\_{t}. At low wealth levels (Xt<3X\_{t}<3), consumption decreases as βt\beta\_{t} increases. In this region, the agent seeks to accumulate wealth more rapidly. Since a higher βt\beta\_{t} implies more profitable investment opportunities, the agent optimally cuts current consumption in order to finance larger risky positions. At higher wealth levels, however, the agent has sufficient capital to fully exploit the high expected returns. This relaxes the need for aggressive saving and allows consumption to rise, eventually exceeding the level observed in the low-βt\beta\_{t} state.

![Refer to caption](2603.02820v1/Plots/beta_investment.png)


(a) Cross-sections of the optimal investment policy πt∗\pi^{\*}\_{t} for different fixed realizations of the expected excess return βt\beta\_{t}.

![Refer to caption](2603.02820v1/Plots/consumption_beta.png)


(b) Cross-sections of the optimal consumption policy ct∗c^{\*}\_{t} for different fixed realizations of the expected excess return βt\beta\_{t}.

Figure 6. Cross-sections of the optimal policies for different fixed realizations of the expected excess return βt\beta\_{t}.

## 6. Conclusions

In this paper, we have studied the infinite-horizon consumption and portfolio problem of an investor subject to a no-borrowing constraint and labor income, in a market where expected excess returns follow a mean-reverting Ornstein-Uhlenbeck process. Using a Lagrange duality approach, we have formulated the dual problem as a two-dimensional singular control problem involving the marginal value of wealth and the stochastic factor. The solution is governed by an auxiliary optimal stopping problem, which features a free boundary separating the continuation and stopping regions. We have provided a detailed probabilistic analysis for this optimal stopping problem and established properties of the free boundary and of the value function. Finally, we have retrieved the solutions to the primal optimization problem via duality and provided numerical illustrations.
  
  
Acknowledgements. Financial support by the German Research Foundation (DFG) [RTG
  
2865/1 - 492988838] is gratefully acknowledged.

## Appendix A Technical Proofs

### A.1. Proof of Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")

###### Proof.

Since (Mt)t(M\_{t})\_{t} is a martingale, we can fix a finite time horizon T≥0T\geq 0 and define the new measure ℙ¯\mathbb{\bar{P}} on (Ω,ℱ)(\Omega,\mathcal{F}) via

|  |  |  |
| --- | --- | --- |
|  | d​ℙ¯d​ℙ|ℱ^t=Mt,t∈[0,T].\frac{d\mathbb{\bar{P}}}{d\mathbb{P}}\bigg|\_{\hat{\mathcal{F}}\_{t}}=M\_{t},\quad t\in[0,T]. |  |

Using Girsanov’s Theorem, we introduce a new standard Brownian motion (Wtℙ¯)t(W^{\mathbb{\bar{P}}}\_{t})\_{t} under ℙ¯\mathbb{\bar{P}} such that d​Wtℙ¯=d​Wt+βtσ​d​tdW\_{t}^{\mathbb{\bar{P}}}=dW\_{t}+\frac{\beta\_{t}}{\sigma}\,dt. Then, the dynamics of the state processes (Zt1)t(Z^{1}\_{t})\_{t} and (βt)t(\beta\_{t})\_{t} are given under ℙ¯\bar{\mathbb{P}} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zt1\displaystyle dZ^{1}\_{t} | =−βtσ​Zt1​d​Wtℙ¯+Zt1​(δ−r+βt2σ2)​d​t,t>0,Z01=z>0,\displaystyle=-\frac{\beta\_{t}}{\sigma}Z^{1}\_{t}\,dW^{\mathbb{\bar{P}}}\_{t}+Z^{1}\_{t}\bigg(\delta-r+\frac{\beta\_{t}^{2}}{\sigma^{2}}\bigg)\,dt,\quad t>0,\quad Z^{1}\_{0}=z>0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​βt\displaystyle d\beta\_{t} | =σβ​d​Wtβ,ℙ¯+(κ​(β¯−βt)−ρ​βtσ​σβ)​d​t,t>0,β0=β∈ℝ,\displaystyle=\sigma\_{\beta}\,dW\_{t}^{\beta,\mathbb{\bar{P}}}+\bigg(\kappa(\overline{\beta}-\beta\_{t})-\rho\,\frac{\beta\_{t}}{\sigma}\sigma\_{\beta}\bigg)\,dt,\quad t>0,\quad\beta\_{0}=\beta\in\mathbb{R}, |  |

where Wtβ,ℙ¯:=ρ​Wtℙ¯+1−ρ2​Wt2,⟂W^{\beta,\mathbb{\bar{P}}}\_{t}:=\rho W\_{t}^{\mathbb{\bar{P}}}+\sqrt{1-\rho^{2}}W^{2,\perp}\_{t} is a standard Brownian motion on (Ω,ℱ,ℙ¯)(\Omega,\mathcal{F},\mathbb{\bar{P}}). Under ℙ¯\mathbb{\bar{P}}, we then have for any 𝔽¯\bar{\mathbb{F}}-stopping time τ\tau:

|  |  |  |  |
| --- | --- | --- | --- |
| (A.1) |  | 𝔼z,β​[∫0τ∧Te−r​t​Mt​(u~′​(Zt1)+ℓ)​𝑑t]=𝔼z,βℙ¯​[∫0τ∧Te−r​t​(u~′​(Zt1)+ℓ)​𝑑t],\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\tau\wedge T}e^{-rt}M\_{t}\,(\tilde{u}^{\prime}(Z\_{t}^{1})+\ell)\,dt\bigg]=\mathbb{E}\_{z,\beta}^{\mathbb{\bar{P}}}\bigg[\int\_{0}^{\tau\wedge T}e^{-rt}\,(\tilde{u}^{\prime}(Z^{1}\_{t})+\ell)\,dt\bigg], |  |

where 𝔼z,βℙ¯​[⋅]\mathbb{E}^{\mathbb{\bar{P}}}\_{z,\beta}[\cdot] denotes the expectation under ℙ¯z,β(⋅)=ℙ¯(⋅|Z01=z,β0=β)\mathbb{\bar{P}}\_{z,\beta}(\cdot)=\mathbb{\bar{P}}(\;\cdot\;|\;Z^{1}\_{0}=z,\;\beta\_{0}=\beta). As the measure ℙ¯\mathbb{\bar{P}} depends on TT, we cannot directly let T→∞T\to\infty. To bypass this problem, we proceed as in [[5](#bib.bib32 "Optimal reduction of public debt under partial observation of the economic growth")] (see also [[11](#bib.bib36 "Optimal dividends with partial information and stopping of a degenerate reflecting diffusion")]). We observe that the coefficients of the SDEs for Z1Z^{1} and β\beta do not depend on the horizon TT. Therefore, the law of the process (Z1,β)(Z^{1},\beta) on [0,T][0,T] under ℙ¯\mathbb{\bar{P}} is consistent for any TT. This allows us to introduce a new auxiliary probability space (Ω^,ℱ^,ℚ)(\hat{\Omega},\hat{\mathcal{F}},\mathbb{Q}) equipped with two standard Brownian motions (Wtℚ)t(W^{\mathbb{Q}}\_{t})\_{t} and (Wtβ,ℚ)t(W^{\beta,\mathbb{Q}}\_{t})\_{t}, generating the filtrations (completed by ℚ​-null sets of​ℱ^\mathbb{Q}\text{-null sets of}\;\hat{\mathcal{F}}) 𝔽W,ℚ:=(ℱtW,ℚ)t\mathbb{F}^{W,\mathbb{Q}}:=(\mathcal{F}\_{t}^{W,\mathbb{Q}})\_{t} and 𝔽Wβ,ℚ:=(ℱtWβ,ℚ)t\mathbb{F}^{W^{\beta},\mathbb{Q}}:=(\mathcal{F}\_{t}^{W^{\beta},\mathbb{Q}})\_{t}, that satisfy Wtβ,ℚ=ρ​Wtℚ+1−ρ2​W^t2,⟂W^{\beta,\mathbb{Q}}\_{t}=\rho W\_{t}^{\mathbb{Q}}+\sqrt{1-\rho^{2}}\widehat{W}^{2,\perp}\_{t}. On this space, we let (Z^t)t(\hat{Z}\_{t})\_{t} and (β^t)t(\hat{\beta}\_{t})\_{t} be the unique strong solutions to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Z^t\displaystyle d\hat{Z}\_{t} | =−β^tσ​Z^t​d​Wtℚ+Z^t​(δ−r+β^t2σ2)​d​t,t>0,Z^0=z>0,\displaystyle=-\frac{\hat{\beta}\_{t}}{\sigma}\hat{Z}\_{t}\,dW^{\mathbb{Q}}\_{t}+\hat{Z}\_{t}\bigg(\delta-r+\frac{\hat{\beta}\_{t}^{2}}{\sigma^{2}}\bigg)\,dt,\quad t>0,\quad\hat{Z}\_{0}=z>0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​β^t\displaystyle d\hat{\beta}\_{t} | =σβ​d​Wtβ,ℚ+(κ​(β¯−β^t)−ρ​β^tσ​σβ)​d​t,t>0,β^0=β∈ℝ.\displaystyle=\sigma\_{\beta}\,dW^{\beta,\mathbb{Q}}\_{t}+\bigg(\kappa(\overline{\beta}-\hat{\beta}\_{t})-\rho\,\frac{\hat{\beta}\_{t}}{\sigma}\sigma\_{\beta}\bigg)\,dt,\quad t>0,\quad\hat{\beta}\_{0}=\beta\in\mathbb{R}. |  |

We set 𝔽^:=(ℱ^t)t\hat{\mathbb{F}}:=(\hat{\mathcal{F}}\_{t})\_{t}, where ℱ^t:=ℱtW,ℚ∨ℱtWβ,ℚ\hat{\mathcal{F}}\_{t}:=\mathcal{F}\_{t}^{W,\mathbb{Q}}\vee\mathcal{F}\_{t}^{W^{\beta},\mathbb{Q}}, t≥0t\geq 0. We then define the following value functions (where the infimum is taken over all 𝔽^\hat{\mathbb{F}}-stopping times)

|  |  |  |
| --- | --- | --- |
|  | vℚ​(z,β;T):=infτ𝔼z,βℚ​[∫0τ∧Te−r​t​(u~′​(Z^t)+ℓ)​𝑑t],v^{\mathbb{Q}}(z,\beta;T):=\inf\_{\tau}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\left[\int\_{0}^{\tau\wedge T}e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)\,dt\right], |  |

and

|  |  |  |
| --- | --- | --- |
|  | vℚ​(z,β):=infτ𝔼z,βℚ​[∫0τe−r​t​(u~′​(Z^t)+ℓ)​𝑑t].v^{\mathbb{Q}}(z,\beta):=\inf\_{\tau}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\left[\int\_{0}^{\tau}e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)\,dt\right]. |  |

By using the Dominated Convergence Theorem (whose application is justified by using arguments as those in the proof of the upcoming Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (A.2) |  | limT→∞vℚ​(z,β;T)=vℚ​(z,β),limT→∞v​(z,β;T)=v​(z,β),\lim\_{T\to\infty}v^{\mathbb{Q}}(z,\beta;T)=v^{\mathbb{Q}}(z,\beta),\quad\lim\_{T\to\infty}v(z,\beta;T)=v(z,\beta), |  |

where we have set

|  |  |  |
| --- | --- | --- |
|  | v​(z,β;T):=infτ𝔼z,β​[∫0τ∧Te−r​t​Mt​(u~′​(Ztz,1)+ℓ)​𝑑t].v(z,\beta;T):=\inf\_{\tau}\mathbb{E}\_{z,\beta}\bigg[\int\_{0}^{\tau\wedge T}e^{-rt}M\_{t}\,(\tilde{u}^{\prime}(Z\_{t}^{z,1})+\ell)\,dt\bigg]. |  |

Since now

|  |  |  |
| --- | --- | --- |
|  | infτ𝔼z,βℙ¯​[∫0τ∧Te−r​t​(u~′​(Zt1)+ℓ)​𝑑t]=infτ𝔼z,βℚ​[∫0τ∧Te−r​t​(u~′​(Z^t)+ℓ)​𝑑t],\inf\_{\tau}\mathbb{E}\_{z,\beta}^{\bar{\mathbb{P}}}\bigg[\int\_{0}^{\tau\wedge T}e^{-rt}\,(\tilde{u}^{\prime}(Z^{1}\_{t})+\ell)\,dt\bigg]=\inf\_{\tau}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\tau\wedge T}e^{-rt}\,(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)\,dt\bigg], |  |

the equivalence in law of the processes (Zt1,βt,Wtℙ¯,Wtβ,ℙ¯)t(Z^{1}\_{t},\beta\_{t},W\_{t}^{\bar{\mathbb{P}}},W\_{t}^{\beta,\bar{\mathbb{P}}})\_{t} under ℙ¯\bar{\mathbb{P}} and (Z^t,β^t,Wtℚ,Wtβ,ℚ)t(\hat{Z}\_{t},\hat{\beta}\_{t},W\_{t}^{\mathbb{Q}},W\_{t}^{\beta,\mathbb{Q}})\_{t} under ℚ\mathbb{Q} on [0,T][0,T], and ([A.1](#A1.E1 "In Proof. ‣ A.1. Proof of Proposition 3.1 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) allow us to write

|  |  |  |
| --- | --- | --- |
|  | vℚ​(z,β)=limT→∞vℚ​(z,β;T)=limT→∞v​(z,β;T)=v​(z,β),v^{\mathbb{Q}}(z,\beta)=\lim\_{T\to\infty}v^{\mathbb{Q}}(z,\beta;T)=\lim\_{T\to\infty}v(z,\beta;T)=v(z,\beta), |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | v​(z,β)=infτ𝔼z,βℚ​[∫0τe−r​t​(u~′​(Z^t)+ℓ)​𝑑t].v(z,\beta)=\inf\_{\tau}\mathbb{E}\_{z,\beta}^{\mathbb{Q}}\bigg[\int\_{0}^{\tau}e^{-rt}\,(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)\,dt\bigg]. |  |

∎

### A.2. Proof of Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")

###### Proof.

It follows from ([3.3](#S3.E3 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that u~′​(Z^t)=−Z^t−1γ\tilde{u}^{\prime}(\hat{Z}\_{t})=-\hat{Z}^{-\frac{1}{\gamma}}\_{t}. Therefore,

|  |  |  |
| --- | --- | --- |
|  | 𝔼z,βℚ​[∫0∞e−r​t​|−Z^t−1γ+ℓ|​𝑑t]≤𝔼z,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]+ℓ​∫0∞e−r​t​𝑑t.\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}|-\hat{Z}^{-\frac{1}{\gamma}}\_{t}+\ell|dt\bigg]\leq\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}^{-\frac{1}{\gamma}}\_{t}dt\bigg]+\ell\int\_{0}^{\infty}e^{-rt}dt. |  |

Hence, in order to prove that v​(z,β)∈ℝv(z,\beta)\in\mathbb{R} it suffices to show that

|  |  |  |
| --- | --- | --- |
|  | 𝔼z,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]<∞.\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}^{-\frac{1}{\gamma}}\_{t}dt\bigg]<\infty. |  |

By Fubini-Tonelli Theorem, we may write

|  |  |  |
| --- | --- | --- |
|  | 𝔼z,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]=∫0∞e−r​t​𝔼z,βℚ​[Z^t−1γ]​𝑑t,\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}^{-\frac{1}{\gamma}}\_{t}dt\bigg]=\int\_{0}^{\infty}e^{-rt}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}[\hat{Z}\_{t}^{-\frac{1}{\gamma}}]\,dt, |  |

and we recall that

|  |  |  |
| --- | --- | --- |
|  | Wtℚ=ρ​Wtβ,ℚ+1−ρ2​W^t1,⟂,t≥0,W\_{t}^{\mathbb{Q}}=\rho\,W\_{t}^{\beta,\mathbb{Q}}+\sqrt{1-\rho^{2}}\,\widehat{W}^{1,\perp}\_{t},\quad t\geq 0, |  |

due to the correlation between WℚW^{\mathbb{Q}} and Wβ,ℚW^{\beta,\mathbb{Q}}, where W^1,⟂\widehat{W}^{1,\perp} is a Brownian motion independent of Wβ,ℚW^{\beta,\mathbb{Q}}. By using the explicit representation of the strong solution to ([3.16](#S3.E16 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we find

|  |  |  |
| --- | --- | --- |
|  | 𝔼z,βℚ​[Z^t−1γ]=z−1γ​𝔼1,βℚ​[exp⁡(−1γ​∫0t(δ−r+12​β^s2σ2)​𝑑s+1γ​∫0tβ^sσ​𝑑Wsℚ)]\displaystyle\mathbb{E}^{\mathbb{Q}}\_{z,\beta}[\hat{Z}\_{t}^{-\frac{1}{\gamma}}]=z^{-\frac{1}{\gamma}}\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\exp\bigg(-\frac{1}{\gamma}\int\_{0}^{t}(\delta-r+\tfrac{1}{2}\tfrac{\hat{\beta}\_{s}^{2}}{\sigma^{2}})ds+\frac{1}{\gamma}\int\_{0}^{t}\tfrac{\hat{\beta}\_{s}}{\sigma}dW\_{s}^{\mathbb{Q}}\bigg)\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =z−1γ​𝔼1,βℚ​[exp⁡(−1γ​∫0t(δ−r+12​β^s2σ2)​𝑑s+1γ​ρ​∫0tβ^sσ​𝑑Wsβ,ℚ+1γ​1−ρ2​∫0tβ^sσ​𝑑W^s1,⟂)]\displaystyle=z^{-\frac{1}{\gamma}}\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\exp\bigg(-\frac{1}{\gamma}\int\_{0}^{t}(\delta-r+\tfrac{1}{2}\tfrac{\hat{\beta}\_{s}^{2}}{\sigma^{2}})ds+\frac{1}{\gamma}\rho\int\_{0}^{t}\tfrac{\hat{\beta}\_{s}}{\sigma}dW^{\beta,\mathbb{Q}}\_{s}+\frac{1}{\gamma}\sqrt{1-\rho^{2}}\int\_{0}^{t}\tfrac{\hat{\beta}\_{s}}{\sigma}d\widehat{W}^{1,\perp}\_{s}\bigg)\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =z−1γ𝔼1,βℚ[𝔼ℚ[exp(−1γ∫0t(δ−r+12β^s2σ2)ds\displaystyle=z^{-\frac{1}{\gamma}}\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\mathbb{E}^{\mathbb{Q}}\bigg[\exp\bigg(-\frac{1}{\gamma}\int\_{0}^{t}(\delta-r+\tfrac{1}{2}\tfrac{\hat{\beta}\_{s}^{2}}{\sigma^{2}})ds |  |
|  |  |  |
| --- | --- | --- |
|  | +1γρ∫0tβ^sσdWsβ,ℚ+1γ1−ρ2∫0tβ^sσdW^s1,⟂)|ℱtWβ,ℚ]]\displaystyle\quad+\frac{1}{\gamma}\rho\int\_{0}^{t}\tfrac{\hat{\beta}\_{s}}{\sigma}dW^{\beta,\mathbb{Q}}\_{s}+\frac{1}{\gamma}\sqrt{1-\rho^{2}}\int\_{0}^{t}\tfrac{\hat{\beta}\_{s}}{\sigma}d\widehat{W}^{1,\perp}\_{s}\bigg)\bigg|\mathcal{F}\_{t}^{W^{\beta},\mathbb{Q}}\bigg]\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =z−1γ​𝔼1,βℚ​[exp⁡(−1γ​∫0t(δ−r+12​β^s2σ2)​𝑑s+1γ​ρ​∫0tβ^sσ​𝑑Wsβ,ℚ+12​1γ2​(1−ρ2)​∫0tβ^s2σ2​𝑑s)]\displaystyle=z^{-\frac{1}{\gamma}}\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\exp\bigg(-\frac{1}{\gamma}\int\_{0}^{t}(\delta-r+\tfrac{1}{2}\tfrac{\hat{\beta}\_{s}^{2}}{\sigma^{2}})ds+\frac{1}{\gamma}\rho\int\_{0}^{t}\tfrac{\hat{\beta}\_{s}}{\sigma}dW^{\beta,\mathbb{Q}}\_{s}+\tfrac{1}{2}\frac{1}{\gamma^{2}}(1-\rho^{2})\int\_{0}^{t}\tfrac{\hat{\beta}\_{s}^{2}}{\sigma^{2}}ds\bigg)\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =z−1γ​𝔼1,βℚ​[exp⁡(−1γ​(δ−r)​t−12​σ2​γ​∫0tβ^s2​𝑑s+(1−ρ2)2​σ2​γ2​∫0tβ^s2​𝑑s+ρσ​γ​∫0tβ^s​𝑑Wsβ,ℚ)]\displaystyle=z^{-\frac{1}{\gamma}}\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\exp\bigg(-\frac{1}{\gamma}(\delta-r)t-\tfrac{1}{2\sigma^{2}\gamma}\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds+\tfrac{(1-\rho^{2})}{2\sigma^{2}\gamma^{2}}\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds+\tfrac{\rho}{\sigma\gamma}\int\_{0}^{t}\hat{\beta}\_{s}dW^{\beta,\mathbb{Q}}\_{s}\bigg)\bigg]\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | =z−1γ​exp⁡(−1γ​(δ−r)​t)\displaystyle=z^{-\frac{1}{\gamma}}\exp\big(-\frac{1}{\gamma}(\delta-r)t\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ⋅𝔼1,βℚ​[exp⁡((1γ2​(1−ρ2)−1γ2​σ2)​∫0tβ^s2​𝑑s+ρσ​γ​∫0tβ^s​𝑑Wsβ,ℚ−12​ρ2σ2​γ2​∫0tβ^s2​𝑑s+12​ρ2σ2​γ2​∫0tβ^s2​𝑑s)]\displaystyle\quad\cdot\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\exp\bigg(\bigg(\tfrac{\frac{1}{\gamma^{2}}(1-\rho^{2})-\frac{1}{\gamma}}{2\sigma^{2}}\bigg)\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds+\tfrac{\rho}{\sigma\gamma}\int\_{0}^{t}\hat{\beta}\_{s}dW^{\beta,\mathbb{Q}}\_{s}-\tfrac{1}{2}\tfrac{\rho^{2}}{\sigma^{2}\gamma^{2}}\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds+\tfrac{1}{2}\tfrac{\rho^{2}}{\sigma^{2}\gamma^{2}}\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds\bigg)\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | =z−1γ​exp⁡(−1γ​(δ−r)​t)\displaystyle=z^{-\frac{1}{\gamma}}\exp\big(-\frac{1}{\gamma}(\delta-r)t\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ⋅𝔼1,βℚ​[exp⁡(1−γ2​σ2​γ2​∫0tβ^s2​𝑑s)​exp⁡(ρσ​γ​∫0tβ^s​𝑑Wsβ,ℚ−12​ρ2σ2​γ2​∫0tβ^s2​𝑑s)].\displaystyle\quad\cdot\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\exp\bigg(\tfrac{1-\gamma}{2\sigma^{2}\gamma^{2}}\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds\bigg)\exp\bigg(\tfrac{\rho}{\sigma\gamma}\int\_{0}^{t}\hat{\beta}\_{s}dW^{\beta,\mathbb{Q}}\_{s}-\tfrac{1}{2}\tfrac{\rho^{2}}{\sigma^{2}\gamma^{2}}\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds\bigg)\bigg]. |  |

The process

|  |  |  |
| --- | --- | --- |
|  | Nt:=exp⁡(ρσ​γ​∫0tβ^s​𝑑Wsβ,ℚ−12​ρ2σ2​γ2​∫0tβ^s2​𝑑s)N\_{t}:=\exp\bigg(\tfrac{\rho}{\sigma\gamma}\int\_{0}^{t}\hat{\beta}\_{s}dW^{\beta,\mathbb{Q}}\_{s}-\tfrac{1}{2}\tfrac{\rho^{2}}{\sigma^{2}\gamma^{2}}\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds\bigg) |  |

defines a martingale under ℚ\mathbb{Q} by Assumption [3.2](#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"). Hence, Girsanov’s Theorem allows us to define a new probability measure by

|  |  |  |
| --- | --- | --- |
|  | d​ℚ′d​ℚ|ℱ^t=Nt,\frac{d\mathbb{Q^{\prime}}}{d\mathbb{Q}}\bigg|\_{\hat{\mathcal{F}}\_{t}}=N\_{t}, |  |

and to obtain, as γ>1\gamma>1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼z,βℚ​[Z^t−1γ]\displaystyle\mathbb{E}^{\mathbb{Q}}\_{z,\beta}[\hat{Z}\_{t}^{-\frac{1}{\gamma}}] | =z−1γ​exp⁡(−1γ​(δ−r)​t)​𝔼1,βℚ′​[exp⁡((1−γ2​σ2​γ2)​∫0tβ^s2​𝑑s)]\displaystyle=z^{-\frac{1}{\gamma}}\exp\big({-\frac{1}{\gamma}}(\delta-r)t\big)\mathbb{E}^{\mathbb{Q^{\prime}}}\_{1,\beta}\bigg[\exp\bigg(\bigg(\tfrac{1-\gamma}{2\sigma^{2}\gamma^{2}}\bigg)\int\_{0}^{t}\hat{\beta}\_{s}^{2}ds\bigg)\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤z−1γ​exp⁡(−1γ​(δ−r)​t),\displaystyle\leq z^{-\frac{1}{\gamma}}\exp\bigg(-\tfrac{1}{\gamma}(\delta-r)t\bigg), |  |

which proves ([3.18](#S3.E18 "In Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")). Overall,

|  |  |  |  |
| --- | --- | --- | --- |
| (A.3) |  | 𝔼z,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]=∫0∞e−r​t​𝔼z,βℚ​[Z^t−1γ]​𝑑t≤z−1γ​∫0∞e−(r+1γ​(δ−r))​t​𝑑t<∞,\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}^{{-\frac{1}{\gamma}}}\_{t}dt\bigg]=\int\_{0}^{\infty}e^{-rt}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}[\hat{Z}\_{t}^{-\frac{1}{\gamma}}]dt\leq z^{-\frac{1}{\gamma}}\int\_{0}^{\infty}e^{-(r+\frac{1}{\gamma}(\delta-r))t}\,dt<\infty, |  |

since r+1γ​(δ−r)>0r+\frac{1}{\gamma}(\delta-r)>0 as γ>1\gamma>1.
∎

### A.3. Proof of Proposition [3.6](#S3.Thmtheorem6 "Proposition 3.6. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")

###### Proof.

Taking the suboptimal stopping time τ=0\tau=0 in ([3.15](#S3.E15 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) clearly yields v​(z,β)≤0v(z,\beta)\leq 0 for all (z,β)(z,\beta) on 𝒪\mathcal{O}. As for the lower bound, using that u~′​(Z^t)=−Z^t−1γ\tilde{u}^{\prime}(\hat{Z}\_{t})=-\hat{Z}\_{t}^{-\frac{1}{\gamma}} by ([3.3](#S3.E3 "In 3.1. Derivation of the Dual Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we have for any (z,β)∈𝒪(z,\beta)\in\mathcal{O} and any stopping time τ\tau

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼z,βℚ​[∫0τe−r​t​(u~′​(Z^t)+ℓ)​𝑑t]\displaystyle\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\tau}e^{-rt}(\tilde{u}^{\prime}(\hat{Z}\_{t})+\ell)dt\bigg] | ≥−𝔼z,βℚ​[∫0τe−r​t​Z^t−1γ​𝑑t]\displaystyle\geq-\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\tau}e^{-rt}\hat{Z}\_{t}^{-\frac{1}{\gamma}}dt\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥−𝔼z,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]>−∞,\displaystyle\geq-\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}\_{t}^{-\frac{1}{\gamma}}dt\bigg]>-\infty, |  |

where the last inequality is due ([3.18](#S3.E18 "In Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and the fact that r+1γ​(δ−r)>0r+\frac{1}{\gamma}(\delta-r)>0 as γ>1\gamma>1. Arbitrariness of τ≥0\tau\geq 0 then implies the result.
∎

### A.4. Proof of Proposition [3.7](#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")

###### Proof.

We have

|  |  |  |  |
| --- | --- | --- | --- |
| (A.4) |  | 0≥limz→∞v​(z,β)≥limz→∞(−z−1γ​𝔼1,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t])=0,0\geq\lim\_{z\to\infty}v(z,\beta)\geq\lim\_{z\to\infty}\left(-z^{-\frac{1}{\gamma}}\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}\_{t}^{-\frac{1}{\gamma}}dt\bigg]\right)=0, |  |

where we have used that the expectation in the right-hand side of ([A.4](#A1.E4 "In Proof. ‣ A.4. Proof of Proposition 3.7 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) does not depend on zz. Similarly, one also obtains

|  |  |  |  |
| --- | --- | --- | --- |
|  | limz→0v​(z,β)\displaystyle\lim\_{z\to 0}v(z,\beta) | ≤limz→0𝔼z,βℚ​[∫0∞e−r​t​(−Z^t−1γ+ℓ)​𝑑t]\displaystyle\leq\lim\_{z\to 0}\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}(-\hat{Z}\_{t}^{-\frac{1}{\gamma}}+\ell)dt\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limz→0(−z−1γ​𝔼1,βℚ​[∫0∞e−r​t​Z^t−1γ​𝑑t]+ℓr)=−∞.\displaystyle=\lim\_{z\to 0}\left(-z^{-\frac{1}{\gamma}}\mathbb{E}^{\mathbb{Q}}\_{1,\beta}\bigg[\int\_{0}^{\infty}e^{-rt}\hat{Z}\_{t}^{-\frac{1}{\gamma}}dt\bigg]+\frac{\ell}{r}\right)=-\infty. |  |

∎

### A.5. Proof of Proposition [3.11](#S3.Thmtheorem11 "Proposition 3.11. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")

###### Proof.

The proof is divided into two steps and borrows arguments from [[10](#bib.bib42 "On Lipschitz continuous optimal stopping boundaries")].
  
  
Step 1. We first show that the value function vv is (locally) Lipschitz continuous in the zz-variable and derive the probabilistic representation for the weak derivative vzv\_{z}. To that end, we fix (z,β)∈𝒪(z,\beta)\in\mathcal{O} and ε>0\varepsilon>0, and let τ∗\tau^{\*} be the optimal stopping time for the problem with initial data (z,β)(z,\beta) (independent of ε\varepsilon).
  
For the purpose of showing the Lipschitz property, we may restrict to ε≤ε0\varepsilon\leq\varepsilon\_{0} with ε0∈(0,1)\varepsilon\_{0}\in(0,1) such that z−ε>0z-\varepsilon>0. Using u~′​(Z^t)=−Z^t−1γ\tilde{u}^{\prime}(\hat{Z}\_{t})=-\hat{Z}\_{t}^{-\frac{1}{\gamma}} and the Mean-Value Theorem, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v​(z+ε,β)−v​(z,β)|\displaystyle|v(z+\varepsilon,\beta)-v(z,\beta)| | ≤𝔼ℚ​[∫0∞e−r​t​(Z^t1,β)−1γ​|z−1γ−(z+ε)−1γ|​𝑑t]\displaystyle\leq\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\infty}e^{-rt}(\hat{Z}^{1,\beta}\_{t})^{-\frac{1}{\gamma}}|z^{-\frac{1}{\gamma}}-(z+\varepsilon)^{-\frac{1}{\gamma}}|dt\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.5) |  |  | =|z−1γ−(z+ε)−1γ|​𝔼ℚ​[∫0∞e−r​t​(Z^t1,β)−1γ​𝑑t]\displaystyle=|z^{-\frac{1}{\gamma}}-(z+\varepsilon)^{-\frac{1}{\gamma}}|\,\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\infty}e^{-rt}(\hat{Z}^{1,\beta}\_{t})^{-\frac{1}{\gamma}}dt\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1γ​ξ−1γ−1​ε​𝔼ℚ​[∫0∞e−r​t​(Z^t1,β)−1γ​𝑑t],\displaystyle=\frac{1}{\gamma}\xi^{-\frac{1}{\gamma}-1}\,\varepsilon\,\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\infty}e^{-rt}(\hat{Z}^{1,\beta}\_{t})^{-\frac{1}{\gamma}}dt\Big], |  |

for some ζ∈[z,z+ε]\zeta\in[z,z+\varepsilon]. Upon setting

|  |  |  |
| --- | --- | --- |
|  | c​(z,β):=1γ​z−1γ−1​𝔼ℚ​[∫0∞e−r​t​(Z^t1,β)−1γ​𝑑t],c(z,\beta):=\frac{1}{\gamma}z^{-\frac{1}{\gamma}-1}\,\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\infty}e^{-rt}(\hat{Z}^{1,\beta}\_{t})^{-\frac{1}{\gamma}}dt\Big], |  |

we thus obtain from ([A.5](#A1.Ex34 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"))

|  |  |  |
| --- | --- | --- |
|  | |v​(z+ε,β)−v​(z,β)|≤c​(z,β)​ε,|v(z+\varepsilon,\beta)-v(z,\beta)|\leq c(z,\beta)\,\varepsilon, |  |

and by symmetry,

|  |  |  |
| --- | --- | --- |
|  | |v​(z,β)−v​(z−ε,β)|≤c​(z,β)​ε.|v(z,\beta)-v(z-\varepsilon,\beta)|\leq c(z,\beta)\,\varepsilon. |  |

Since c​(z,β)>0c(z,\beta)>0 is finite by Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model") and can be taken uniformly on compact sets, we conclude that v​(⋅,β)v(\cdot,\beta) is (locally) Lipschitz continuous in zz.
  
In order to derive the probabilistic representation of the weak derivative vzv\_{z}, we note that τ∗\tau^{\*} is suboptimal for v​(z+ε,β)v(z+\varepsilon,\beta), and thus we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(z+ε,β)−v​(z,β)\displaystyle v(z+\varepsilon,\beta)-v(z,\beta) | ≤𝔼ℚ​[∫0τ∗e−r​t​(Z^t1,β)−1γ​(z−1γ−(z+ε)−1γ)​𝑑t]\displaystyle\leq\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\tau^{\*}}e^{-rt}(\hat{Z}^{1,\beta}\_{t})^{-\frac{1}{\gamma}}\big(z^{-\frac{1}{\gamma}}-(z+\varepsilon)^{-\frac{1}{\gamma}}\big)dt\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(z−1γ−(z+ε)−1γ)​𝔼ℚ​[∫0τ∗e−r​t​(Z^t1,β)−1γ​𝑑t].\displaystyle=\big(z^{-\frac{1}{\gamma}}-(z+\varepsilon)^{-\frac{1}{\gamma}}\big)\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\tau^{\*}}e^{-rt}(\hat{Z}^{1,\beta}\_{t})^{-\frac{1}{\gamma}}dt\Big]. |  |

Dividing by ε\varepsilon and then letting ε→0\varepsilon\to 0 yields

|  |  |  |  |
| --- | --- | --- | --- |
| (A.6) |  | lim supε→0v​(z+ε,β)−v​(z,β)ε≤𝔼ℚ​[∫0τ∗e−r​t​1γ​z−1​(Z^tz,β)−1γ​𝑑t].\limsup\_{\varepsilon\to 0}\frac{v(z+\varepsilon,\beta)-v(z,\beta)}{\varepsilon}\leq\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\tau^{\*}}e^{-rt}\frac{1}{\gamma}z^{-1}(\hat{Z}^{z,\beta}\_{t})^{-\frac{1}{\gamma}}dt\Big]. |  |

A symmetric argument applied to v​(z,β)−v​(z−ε,β)v(z,\beta)-v(z-\varepsilon,\beta) gives the reverse inequality

|  |  |  |  |
| --- | --- | --- | --- |
| (A.7) |  | lim infε→0v​(z,β)−v​(z−ε,β)ε≥𝔼ℚ​[∫0τ∗e−r​t​1γ​z−1​(Z^tz,β)−1γ​𝑑t].\liminf\_{\varepsilon\to 0}\frac{v(z,\beta)-v(z-\varepsilon,\beta)}{\varepsilon}\geq\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\tau^{\*}}e^{-rt}\frac{1}{\gamma}z^{-1}(\hat{Z}^{z,\beta}\_{t})^{-\frac{1}{\gamma}}dt\Big]. |  |

Hence, since vv is (locally) Lipschitz continuous in zz, it follows from ([A.6](#A1.E6 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([A.7](#A1.E7 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that for any point zz of differentiability (belonging to a set of full measure) the weak derivative vzv\_{z} is given by

|  |  |  |
| --- | --- | --- |
|  | vz​(z,β)=𝔼ℚ​[∫0τ∗e−r​t​1γ​z−1​(Z^tz,β)−1γ​𝑑t].v\_{z}(z,\beta)=\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{\tau^{\*}}e^{-rt}\frac{1}{\gamma}z^{-1}(\hat{Z}^{z,\beta}\_{t})^{-\frac{1}{\gamma}}dt\Big]. |  |

  

Step 2. In this step, we show that vv is (locally) Lipschitz continuous in the β\beta-variable and derive the probabilistic representation for the weak derivative vβv\_{\beta}. Again, let (z,β)∈𝒪(z,\beta)\in\mathcal{O}, and to simplify notation, we set

|  |  |  |
| --- | --- | --- |
|  | a:=κ+ρ​σβσ>0(by Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")),b:=κ​β¯a,a:=\kappa+\rho\frac{\sigma\_{\beta}}{\sigma}>0\quad\text{(by Assumption \ref{assumption\_novikov})},\quad b:=\frac{\kappa\overline{\beta}}{a}, |  |

so that the unique strong solution to ([3.17](#S3.E17 "In 3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
| (A.8) |  | β^tβ=β​e−a​t+b​(1−e−a​t)+σβ​∫0te−a​(t−s)​𝑑Wsβ,ℚ,\hat{\beta}^{\beta}\_{t}=\beta e^{-at}+b(1-e^{-at})+\sigma\_{\beta}\int\_{0}^{t}e^{-a(t-s)}dW\_{s}^{\beta,\mathbb{Q}}, |  |

and it readily follows that ∂β^tβ∂β=e−a​t\frac{\partial\hat{\beta}^{\beta}\_{t}}{\partial\beta}=e^{-at}. Since

|  |  |  |
| --- | --- | --- |
|  | Z^tz,β=z​exp⁡(∫0t(δ−r+12​(β^sβ)2σ2)​𝑑s−∫0tβ^sβσ​𝑑Wsℚ),\hat{Z}^{z,\beta}\_{t}=z\exp\Bigg(\int\_{0}^{t}\big(\delta-r+\frac{1}{2}\frac{(\hat{\beta}^{\beta}\_{s})^{2}}{\sigma^{2}}\big)ds-\int\_{0}^{t}\frac{\hat{\beta}^{\beta}\_{s}}{\sigma}dW\_{s}^{\mathbb{Q}}\Bigg), |  |

we have by Theorem V​.7.39V.7.39 in [[38](#bib.bib30 "Stochastic integration and differential equations")]

|  |  |  |  |
| --- | --- | --- | --- |
| (A.9) |  | ∂Z^t∂β=Z^t​(∫0te−a​s​β^sσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ),\frac{\partial\hat{Z}\_{t}}{\partial\beta}=\hat{Z}\_{t}\Bigg(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\Bigg), |  |

upon using that, due to ([A.8](#A1.E8 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), one has almost surely

|  |  |  |
| --- | --- | --- |
|  | ∂β(∫0tβ^sβσ​𝑑Wsℚ):=limε→0∫0tβ^sβ+εσ​𝑑Wsℚ−∫0tβ^sβσ​𝑑Wsℚε=∫0te−a​sσ​𝑑Wsℚ.\partial\_{\beta}\Big(\int\_{0}^{t}\frac{\hat{\beta}^{\beta}\_{s}}{\sigma}dW\_{s}^{\mathbb{Q}}\Big):=\lim\_{\varepsilon\to 0}\frac{\int\_{0}^{t}\frac{\hat{\beta}\_{s}^{\beta+\varepsilon}}{\sigma}dW\_{s}^{\mathbb{Q}}-\int\_{0}^{t}\frac{\hat{\beta}\_{s}^{\beta}}{\sigma}dW\_{s}^{\mathbb{Q}}}{\varepsilon}=\int\_{0}^{t}\frac{e^{-as}}{\sigma}dW\_{s}^{\mathbb{Q}}. |  |

As in Step 1, we may restrict to ε≤ε0\varepsilon\leq\varepsilon\_{0} for some ε0∈(0,1)\varepsilon\_{0}\in(0,1), and by the Mean-Value Theorem and ([A.9](#A1.E9 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v​(z,β+ε)−v​(z,β)|\displaystyle\big|v(z,\beta+\varepsilon)-v(z,\beta)\big| | ≤∫0∞e−r​t​𝔼ℚ​[|(Z^tz,β)−1γ−(Z^tz,β+ε)−1γ|]​𝑑t\displaystyle\leq\int\_{0}^{\infty}e^{-rt}\mathbb{E}^{\mathbb{Q}}\Big[\big|(\hat{Z}\_{t}^{z,\beta})^{-\frac{1}{\gamma}}-(\hat{Z}\_{t}^{z,\beta+\varepsilon})^{-\frac{1}{\gamma}}\big|\Big]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =εγ​∫0∞e−r​t​𝔼ℚ​[(Z^tz,βε)−1γ​|∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ|]​𝑑t,\displaystyle=\frac{\varepsilon}{\gamma}\int\_{0}^{\infty}e^{-rt}\mathbb{E}^{\mathbb{Q}}\Big[(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\Big|\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\Big|\Big]dt, |  |

where βε∈(β,β+ε)\beta\_{\varepsilon}\in(\beta,\beta+\varepsilon).
  
Let

|  |  |  |
| --- | --- | --- |
|  | 1<p<min⁡{γ,γ​σ​(κ+ρ​σβσ)|ρ|​σβ}1<p<\min\bigg\{\gamma,\frac{\gamma\sigma\bigg(\kappa+\frac{\rho\sigma\_{\beta}}{\sigma}\bigg)}{|\rho|\sigma\_{\beta}}\bigg\} |  |

and q>1q>1 with 1p+1q=1\frac{1}{p}+\frac{1}{q}=1. Hölder’s inequality and ([3.18](#S3.E18 "In Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) then yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v​(z,β+ε)−v​(z,β)|\displaystyle\big|v(z,\beta+\varepsilon)-v(z,\beta)\big| | ≤εγ​∫0∞e−r​t​𝔼ℚ​[(Z^tz,βε)−pγ]1/p​𝔼ℚ​[|∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ|q]1/q​𝑑t\displaystyle\leq\frac{\varepsilon}{\gamma}\int\_{0}^{\infty}e^{-rt}\mathbb{E}^{\mathbb{Q}}[(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{p}{\gamma}}]^{1/p}\mathbb{E}^{\mathbb{Q}}\Big[\Big|\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\Big|^{q}\Big]^{1/q}dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.10) |  |  | ≤εγ​z−1γ​∫0∞e(−1γ​(δ−r)−r)​t​𝔼ℚ​[|∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ|q]1/q​𝑑t.\displaystyle\leq\frac{\varepsilon}{\gamma}z^{-\frac{1}{\gamma}}\int\_{0}^{\infty}e^{(-\frac{1}{\gamma}(\delta-r)-r)t}\mathbb{E}^{\mathbb{Q}}\Big[\Big|\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\Big|^{q}\Big]^{1/q}dt. |  |

We define ϕ:=1γ​(δ−r)+r>0\phi:=\frac{1}{\gamma}(\delta-r)+r>0 and Atε:=∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑WsℚA^{\varepsilon}\_{t}:=\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}, so that the inequality ([A.5](#A1.Ex48 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) then reads as

|  |  |  |  |
| --- | --- | --- | --- |
| (A.11) |  | |v​(z,β+ε)−v​(z,β)|≤εγ​z−1γ​∫0∞e−ϕ​t​‖Atε‖Lq​𝑑t,\big|v(z,\beta+\varepsilon)-v(z,\beta)\big|\leq\frac{\varepsilon}{\gamma}z^{-\frac{1}{\gamma}}\int\_{0}^{\infty}e^{-\phi t}\left\lVert{A^{\varepsilon}\_{t}}\right\rVert\_{L^{q}}dt, |  |

where we have set ∥⋅∥Lq=𝔼[|⋅|q]1q\left\lVert{\cdot}\right\rVert\_{L^{q}}=\mathbb{E}[|\cdot|^{q}]^{\frac{1}{q}}.
We now decompose AtεA^{\varepsilon}\_{t} into a deterministic part GtεG^{\varepsilon}\_{t} and a stochastic part BtB\_{t}. That is,

|  |  |  |  |
| --- | --- | --- | --- |
| (A.12) |  | Atε=Gtε+Bt,A^{\varepsilon}\_{t}=G^{\varepsilon}\_{t}+B\_{t}, |  |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.13) |  | Gtε\displaystyle G^{\varepsilon}\_{t} | :=1σ2​∫0te−a​s​(βε​e−a​s+b​(1−e−a​s))​𝑑s,\displaystyle:=\frac{1}{\sigma^{2}}\int\_{0}^{t}e^{-as}(\beta\_{\varepsilon}e^{-as}+b(1-e^{-as}))ds, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.14) |  | Bt\displaystyle B\_{t} | :=σβσ2​∫0te−a​s​(∫0se−a​(s−u)​𝑑Wuβ,ℚ)​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ.\displaystyle:=\frac{\sigma\_{\beta}}{\sigma^{2}}\int\_{0}^{t}e^{-as}\Big(\int\_{0}^{s}e^{-a(s-u)}dW\_{u}^{\beta,\mathbb{Q}}\Big)ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}. |  |

A direct calculation yields

|  |  |  |
| --- | --- | --- |
|  | Gtε=1σ2​(βε−b2​a​(1−e−2​a​t)+ba​(1−e−a​t)),G^{\varepsilon}\_{t}=\frac{1}{\sigma^{2}}\bigg(\frac{\beta\_{\varepsilon}-b}{2a}(1-e^{-2at})+\frac{b}{a}(1-e^{-at})\bigg), |  |

which implies

|  |  |  |  |
| --- | --- | --- | --- |
| (A.15) |  | |Gtε|≤1σ2​a(|βε−b|2+|b|)≤1σ2​a(|β|+1+|b|2+|b|)=:CG(β),|G^{\varepsilon}\_{t}|\leq\frac{1}{\sigma^{2}a}\bigg(\frac{|\beta\_{\varepsilon}-b|}{2}+|b|\bigg)\leq\frac{1}{\sigma^{2}a}\left(\frac{|\beta|+1+|b|}{2}+|b|\right)=:C\_{G}(\beta), |  |

with CG​(β)C\_{G}(\beta) independent of ε>0\varepsilon>0. For BtB\_{t}, an application of Stochastic Fubini Theorem (cf., e.g., Theorem 6565 in section IV of [[38](#bib.bib30 "Stochastic integration and differential equations")]) leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bt\displaystyle B\_{t} | =σβσ2​∫0t(∫ute−a​s​e−a​(s−u)​𝑑s)​𝑑Wuβ,ℚ−1σ​∫0te−a​u​𝑑Wuℚ\displaystyle=\frac{\sigma\_{\beta}}{\sigma^{2}}\int\_{0}^{t}\left(\int\_{u}^{t}e^{-as}e^{-a(s-u)}ds\right)dW\_{u}^{\beta,\mathbb{Q}}-\frac{1}{\sigma}\int\_{0}^{t}e^{-au}dW\_{u}^{\mathbb{Q}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.16) |  |  | =σβ2​a​σ2​∫0t(e−a​u−e−2​a​t+a​u)​𝑑Wuβ,ℚ−1σ​∫0te−a​u​𝑑Wuℚ\displaystyle=\frac{\sigma\_{\beta}}{2a\sigma^{2}}\int\_{0}^{t}\left(e^{-au}-e^{-2at+au}\right)dW\_{u}^{\beta,\mathbb{Q}}-\frac{1}{\sigma}\int\_{0}^{t}e^{-au}dW\_{u}^{\mathbb{Q}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =σβ​ρ2​a​σ2​∫0t(e−a​u−e−2​a​t+a​u)​𝑑Wuℚ+σβ​1−ρ22​a​σ2​∫0t(e−a​u−e−2​a​t+a​u)​𝑑Wu2,⟂\displaystyle=\frac{\sigma\_{\beta}\rho}{2a\sigma^{2}}\int\_{0}^{t}\left(e^{-au}-e^{-2at+au}\right)dW\_{u}^{\mathbb{Q}}+\frac{\sigma\_{\beta}\sqrt{1-\rho^{2}}}{2a\sigma^{2}}\int\_{0}^{t}\left(e^{-au}-e^{-2at+au}\right)dW\_{u}^{2,\perp} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −1σ​∫0te−a​u​𝑑Wuℚ\displaystyle\quad-\frac{1}{\sigma}\int\_{0}^{t}e^{-au}dW\_{u}^{\mathbb{Q}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t(σβ​ρ2​a​σ2​(e−a​u−e−2​a​t+a​u)−1σ​e−a​u)⏟=⁣:f​(u,t)​𝑑Wuℚ+∫0tσβ​1−ρ22​a​σ2​(e−a​u−e−2​a​t+a​u)⏟=⁣:g​(u,t)​𝑑W^u2,⟂,\displaystyle=\int\_{0}^{t}\underbrace{\left(\frac{\sigma\_{\beta}\rho}{2a\sigma^{2}}(e^{-au}-e^{-2at+au})-\frac{1}{\sigma}e^{-au}\right)}\_{=:f(u,t)}dW\_{u}^{\mathbb{Q}}+\int\_{0}^{t}\underbrace{\frac{\sigma\_{\beta}\sqrt{1-\rho^{2}}}{2a\sigma^{2}}\left(e^{-au}-e^{-2at+au}\right)}\_{=:g(u,t)}d\widehat{W}\_{u}^{2,\perp}, |  |

where we used Wuβ,ℚ=ρ​Wuℚ+1−ρ2​W^u2,⟂W\_{u}^{\beta,\mathbb{Q}}=\rho W\_{u}^{\mathbb{Q}}+\sqrt{1-\rho^{2}}\widehat{W}\_{u}^{2,\perp} due to C​o​r​r​(Wuℚ,Wuβ,ℚ)=ρ​uCorr(W\_{u}^{\mathbb{Q}},W\_{u}^{\beta,\mathbb{Q}})=\rho u. The deterministic functions f​(u,t)f(u,t) and g​(u,t)g(u,t) in ([A.16](#A1.E16 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) can be bounded as follows

|  |  |  |
| --- | --- | --- |
|  | |f(u,t)|≤e−a​u(σβ​|ρ|2​a​σ2+1σ)=:Cfe−a​u,|g(u,t)|≤σβ​1−ρ22​a​σ2e−a​u=:Cge−a​u,|f(u,t)|\leq e^{-au}\left(\frac{\sigma\_{\beta}|\rho|}{2a\sigma^{2}}+\frac{1}{\sigma}\right)=:C\_{f}e^{-au},\quad|g(u,t)|\leq\frac{\sigma\_{\beta}\sqrt{1-\rho^{2}}}{2a\sigma^{2}}e^{-au}=:C\_{g}e^{-au}, |  |

and since WℚW^{\mathbb{Q}} is independent of W^2,⟂\widehat{W}^{2,\perp}, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.17) |  | Var​(Bt)\displaystyle\mathrm{Var}(B\_{t}) | =∫0tf(u,t)2du+∫0tg(u,t)2du≤Cf2+Cg22​a=:K.\displaystyle=\int\_{0}^{t}f(u,t)^{2}du+\int\_{0}^{t}g(u,t)^{2}du\leq\frac{C\_{f}^{2}+C\_{g}^{2}}{2a}=:K. |  |

Upon noticing that BtB\_{t} is Gaussian with mean 0 and variance Var​(Bt)≤K\mathrm{Var}(B\_{t})\leq K, we may write Bt=Var​(Bt)​YB\_{t}=\sqrt{\mathrm{Var}(B\_{t})}Y, where Y∼𝒩​(0,1)Y\sim\mathcal{N}(0,1). Therefore, using ([A.17](#A1.E17 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (A.18) |  | ∥Bt∥Lq=Var​(Bt)∥Y∥Lq≤K∥Y∥Lq=:Cq.\|B\_{t}\|\_{L^{q}}=\sqrt{\mathrm{Var}(B\_{t})}\|Y\|\_{L^{q}}\leq\sqrt{K}\|Y\|\_{L^{q}}=:C\_{q}. |  |

The fact that Y∼𝒩​(0,1)Y\sim\mathcal{N}(0,1) implies ‖Y‖Lq<∞\|Y\|\_{L^{q}}<\infty for all q≥1q\geq 1. Hence, ([A.15](#A1.E15 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([A.18](#A1.E18 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) imply

|  |  |  |  |
| --- | --- | --- | --- |
| (A.19) |  | ∥Atε∥Lq≤∥Gtε∥Lq+∥Bt∥Lq=|Gtε|+∥Bt∥Lq≤CG(β)+Cq=:Mq(β),\|A^{\varepsilon}\_{t}\|\_{L^{q}}\leq\|G^{\varepsilon}\_{t}\|\_{L^{q}}+\|B\_{t}\|\_{L^{q}}=|G^{\varepsilon}\_{t}|+\|B\_{t}\|\_{L^{q}}\leq C\_{G}(\beta)+C\_{q}=:M\_{q}(\beta), |  |

where Mq​(β)M\_{q}(\beta) is independent of ε>0\varepsilon>0. Inequalities ([A.11](#A1.E11 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([A.19](#A1.E19 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) in turn lead to

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v​(z,β+ε)−v​(z,β)|≤εγ​z−1γ​∫0∞e−ϕ​t​‖Atε‖Lq​𝑑t\displaystyle\big|v(z,\beta+\varepsilon)-v(z,\beta)\big|\leq\frac{\varepsilon}{\gamma}z^{-\frac{1}{\gamma}}\int\_{0}^{\infty}e^{-\phi t}\left\lVert{A^{\varepsilon}\_{t}}\right\rVert\_{L^{q}}dt | ≤εγ​z−1γ​Mq​(β)​∫0∞e−ϕ​t​𝑑t\displaystyle\leq\frac{\varepsilon}{\gamma}z^{-\frac{1}{\gamma}}M\_{q}(\beta)\int\_{0}^{\infty}e^{-\phi t}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Mq​(β)ϕ​γz−1γε=:c(z,β)ε,\displaystyle=\frac{M\_{q}(\beta)}{\phi\gamma}z^{-\frac{1}{\gamma}}\varepsilon=:c(z,\beta)\varepsilon, |  |

where we have 0<c​(z,β)<∞0<c(z,\beta)<\infty. A symmetric argument also yields

|  |  |  |
| --- | --- | --- |
|  | |v​(z,β)−v​(z,β−ε)|≤c​(z,β)​ε.\big|v(z,\beta)-v(z,\beta-\varepsilon)\big|\leq c(z,\beta)\varepsilon. |  |

Therefore, the value function v​(z,⋅)v(z,\cdot) is (locally) Lipschitz continuous in β\beta, with a constant that can be taken uniform over compact sets.
  
Next, we derive the probabilistic representation for the weak derivative vβv\_{\beta}, which exists for almost every β∈ℝ\beta\in\mathbb{R}. Suppose that β\beta is a point of differentiability and denote by τ∗\tau^{\*} the optimal
stopping time for the problem with initial data (z,β)(z,\beta) (independent of ε\varepsilon).
Since τ∗\tau^{\*} is suboptimal for v​(z,β+ε)v(z,\beta+\varepsilon), we obtain

|  |  |  |
| --- | --- | --- |
|  | v​(z,β+ε)−v​(z,β)≤𝔼ℚ​[∫0τ∗e−r​t​((Z^tz,β)−1γ−(Z^tz,β+ε)−1γ)​𝑑t].\displaystyle v(z,\beta+\varepsilon)-v(z,\beta)\leq\mathbb{E}^{\mathbb{Q}}\!\left[\int\_{0}^{\tau^{\*}}e^{-rt}\Big((\hat{Z}\_{t}^{z,\beta})^{-\frac{1}{\gamma}}-(\hat{Z}\_{t}^{z,\beta+\varepsilon})^{-\frac{1}{\gamma}}\Big)\,dt\right]. |  |

Dividing by ε\varepsilon and using the Mean Value Theorem yields

|  |  |  |  |
| --- | --- | --- | --- |
| (A.20) |  | v​(z,β+ε)−v​(z,β)ε≤𝔼ℚ​[∫0τ∗e−r​t​1γ​(Z^tz,βε)−1γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ)​𝑑t],\frac{v(z,\beta+\varepsilon)-v(z,\beta)}{\varepsilon}\leq\mathbb{E}^{\mathbb{Q}}\!\left[\int\_{0}^{\tau^{\*}}e^{-rt}\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}\,ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}\,dW\_{s}^{\mathbb{Q}}\right)dt\right], |  |

where βε∈(β,β+ε)\beta\_{\varepsilon}\in(\beta,\beta+\varepsilon).
Since

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[∫0∞e−r​t​1γ​(Z^tz,βε)−1γ​|∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ|​𝑑t]<∞,\mathbb{E}^{\mathbb{Q}}\!\left[\int\_{0}^{\infty}e^{-rt}\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left|\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}\,ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}\,dW\_{s}^{\mathbb{Q}}\right|dt\right]<\infty, |  |

which follows from the same arguments used in the proof of (local) Lipschitz continuity of vv in the β\beta-variable, using Fubini’s Theorem, the right-hand side of ([A.20](#A1.E20 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
| (A.21) |  | ∫0∞𝔼ℚ​[e−r​t​(1γ​(Z^tz,βε)−1γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝟏{t≤τ∗}]​𝑑t.\int\_{0}^{\infty}\mathbb{E}^{\mathbb{Q}}\!\left[e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)\mathbf{1}\_{\{t\leq\tau^{\*}\}}\right]dt. |  |

As before, we may restrict to ε≤ε0\varepsilon\leq\varepsilon\_{0} for some ε0∈(0,1)\varepsilon\_{0}\in(0,1). Again, exploiting the arguments from the proof of the Lipschitz continuity of vv in the β\beta-variable, we can bound

|  |  |  |
| --- | --- | --- |
|  | |𝔼ℚ​[e−r​t​(1γ​(Z^tz,βε)−1γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝟏{t≤τ∗}]|\left|\mathbb{E}^{\mathbb{Q}}\!\left[e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)\mathbf{1}\_{\{t\leq\tau^{\*}\}}\right]\right| |  |

by a function that is independent of ε\varepsilon and Lebesgue-integrable over (0,∞)(0,\infty). Therefore, Dominated
Convergence Theorem implies

|  |  |  |
| --- | --- | --- |
|  | limε→0∫0∞𝔼ℚ​[e−r​t​(1γ​(Z^tz,βε)−1γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝟏{t≤τ∗}]​𝑑t\displaystyle\lim\_{\varepsilon\to 0}\int\_{0}^{\infty}\mathbb{E}^{\mathbb{Q}}\!\left[e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)\mathbf{1}\_{\{t\leq\tau^{\*}\}}\right]dt |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0∞limε→0𝔼ℚ​[e−r​t​(1γ​(Z^tz,βε)−1γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝟏{t≤τ∗}]​d​t.\displaystyle=\int\_{0}^{\infty}\lim\_{\varepsilon\to 0}\mathbb{E}^{\mathbb{Q}}\!\left[e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)\mathbf{1}\_{\{t\leq\tau^{\*}\}}\right]dt. |  |

Next, we show that the family

|  |  |  |  |
| --- | --- | --- | --- |
| (A.22) |  | {|(Z^tβε)−1/γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ)|​𝟏{t≤τ∗}}ε∈(0,ε0)\bigg\{\left|(\hat{Z}\_{t}^{\beta\_{\varepsilon}})^{-1/\gamma}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right|\mathbf{1}\_{\{t\leq\tau^{\*}\}}\bigg\}\_{\varepsilon\in(0,\varepsilon\_{0})} |  |

is uniformly integrable. We let

|  |  |  |
| --- | --- | --- |
|  | 1<p~<min⁡{γ,γ​σ​(κ+ρ​σβσ)|ρ|​σβ},1<\tilde{p}<\min\bigg\{\gamma,\frac{\gamma\sigma\bigg(\kappa+\frac{\rho\sigma\_{\beta}}{\sigma}\bigg)}{|\rho|\sigma\_{\beta}}\bigg\}, |  |

m∈(1,p~)m\in(1,\tilde{p}), and we define
p:=p~m>1p:=\frac{\tilde{p}}{m}>1 and q>1q>1 with 1p+1q=1\frac{1}{p}+\frac{1}{q}=1.
Hölder’s inequality then yields

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼ℚ​[(Z^tz,βε)−mγ​|(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ)|m]\displaystyle\mathbb{E}^{\mathbb{Q}}\!\left[(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{m}{\gamma}}\left|\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right|^{m}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.23) |  |  | ≤𝔼ℚ​[(Z^tz,βε)−p~γ]1p​𝔼ℚ​[|∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ|m​q]1q.\displaystyle\qquad\leq\mathbb{E}^{\mathbb{Q}}\!\left[(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{\tilde{p}}{\gamma}}\right]^{\frac{1}{p}}\,\mathbb{E}^{\mathbb{Q}}\!\left[\left|\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right|^{mq}\right]^{\frac{1}{q}}. |  |

Now, recalling ([A.12](#A1.E12 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and using the arguments used for the derivation of ([A.19](#A1.E19 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), we find

|  |  |  |  |
| --- | --- | --- | --- |
| (A.24) |  | ‖At‖Lm​q≤Mm​q​(β),\|A\_{t}\|\_{L^{mq}}\leq M\_{mq}(\beta), |  |

since m​q>1mq>1, which is uniform in ε\varepsilon. Hence, combining ([A.5](#A1.Ex64 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")), ([A.24](#A1.E24 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([3.18](#S3.E18 "In Proposition 3.3. ‣ 3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) gives

|  |  |  |
| --- | --- | --- |
|  | supε≤ε0𝔼ℚ​[|(Z^tz,βε)−1γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ)|m​𝟏{t≤τ∗}]≤z−sγ​e−sγ​(δ−r)​t​Mm​q​(β)m,\sup\_{\varepsilon\leq\varepsilon\_{0}}\mathbb{E}^{\mathbb{Q}}\!\left[\left|(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right|^{m}\mathbf{1}\_{\{t\leq\tau^{\*}\}}\right]\leq z^{-\frac{s}{\gamma}}\,e^{-\frac{s}{\gamma}(\delta-r)t}M\_{mq}(\beta)^{m}, |  |

and thus the uniform integrability of the family ([A.22](#A1.E22 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) follows. Vitali’s Convergence Theorem, together with the continuities of β↦Z^z,β\beta\mapsto\hat{Z}^{z,\beta} and β↦β^β\beta\mapsto\hat{\beta}^{\beta}, then imply

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limε→0𝔼ℚ​[∫0τ∗e−r​t​(1γ​(Z^tz,βε)−1γ​(∫0te−a​s​β^sβεσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝑑t]\displaystyle\lim\_{\varepsilon\to 0}\mathbb{E}^{\mathbb{Q}}\!\left[\int\_{0}^{\tau^{\*}}e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta\_{\varepsilon}})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta\_{\varepsilon}}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.25) |  |  | =𝔼ℚ​[∫0τ∗e−r​t​(1γ​(Z^tz,β)−1γ​(∫0te−a​s​β^sβσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝑑t].\displaystyle\quad=\mathbb{E}^{\mathbb{Q}}\!\left[\int\_{0}^{\tau^{\*}}e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)dt\right]. |  |

Using ([A.5](#A1.Ex66 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) into ([A.20](#A1.E20 "In Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | lim supε→0v​(z,β+ε)−v​(z,β)ε\displaystyle\limsup\_{\varepsilon\to 0}\frac{v(z,\beta+\varepsilon)-v(z,\beta)}{\varepsilon} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.26) |  |  | ≤𝔼z,βℚ​[∫0τ∗e−r​t​(1γ​(Z^tz,β)−1γ​(∫0te−a​s​β^sβσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝑑t],\displaystyle\leq\mathbb{E}\_{z,\beta}^{\mathbb{Q}}\left[\int\_{0}^{\tau^{\*}}e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)dt\right], |  |

and, arguing symmetrically, also

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | lim infε→0v​(z,β)−v​(z,β−ε)ε\displaystyle\liminf\_{\varepsilon\to 0}\frac{v(z,\beta)-v(z,\beta-\varepsilon)}{\varepsilon} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.27) |  |  | ≥𝔼z,βℚ​[∫0τ∗e−r​t​(1γ​(Z^tz,β)−1γ​(∫0te−a​s​β^sβσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝑑t].\displaystyle\geq\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\left[\int\_{0}^{\tau^{\*}}e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)dt\right]. |  |

Hence, since vv is (locally) Lipschitz continuous in β\beta, it follows from ([A.5](#A1.Ex67 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) and ([A.5](#A1.Ex68 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model")) that for almost every β∈ℝ\beta\in\mathbb{R} the weak derivative vβv\_{\beta} is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (A.28) |  | vβ​(z,β)=𝔼z,βℚ​[∫0τ∗e−r​t​(1γ​(Z^tz,β)−1γ​(∫0te−a​s​β^sβσ2​𝑑s−1σ​∫0te−a​s​𝑑Wsℚ))​𝑑t].v\_{\beta}(z,\beta)=\mathbb{E}^{\mathbb{Q}}\_{z,\beta}\left[\int\_{0}^{\tau^{\*}}e^{-rt}\left(\frac{1}{\gamma}(\hat{Z}\_{t}^{z,\beta})^{-\frac{1}{\gamma}}\left(\int\_{0}^{t}e^{-as}\frac{\hat{\beta}\_{s}^{\beta}}{\sigma^{2}}ds-\frac{1}{\sigma}\int\_{0}^{t}e^{-as}dW\_{s}^{\mathbb{Q}}\right)\right)dt\right]. |  |

∎

## References

* [1]
  S. Assing, S. Jacka, and A. Ocejo (2014)
  Monotonicity of the value function for a two-dimensional optimal stopping problem.
  The Annals of Applied Probability 24 (4),  pp. 1554–1584.
  External Links: ISSN 1050-5164,2168-8737,
  [Document](https://dx.doi.org/10.1214/13-AAP956),
  [Link](https://doi.org/10.1214/13-AAP956),
  [MathReview (Ł. Stettner)](https://www.ams.org/mathscinet-getitem?mr=3211004)
  Cited by: [§1](#S1.p14.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [2]
  F. M. Baldursson and I. Karatzas (1996)
  Irreversible investment and industry equilibrium.
  Finance and Stochastics 1 (1),  pp. 69–89.
  Cited by: [§3.2](#S3.SS2.p1.4 "3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§4](#S4.p1.1 "4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [3]
  V. Bally (2003)
  An elementary introduction to malliavin calculus.
  Lecture Notes.
  Cited by: [§3.4](#S3.SS4.6.p2.6 "Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [4]
  E. Bandini, T. De Angelis, G. Ferrari, and F. Gozzi (2022)
  Optimal dividend payout under stochastic discounting.
  Mathematical Finance. An International Journal of Mathematics,
  Statistics and Financial Economics 32 (2),  pp. 627–677.
  External Links: ISSN 0960-1627,1467-9965,
  [Document](https://dx.doi.org/10.1111/mafi.12339),
  [Link](https://doi.org/10.1111/mafi.12339),
  [MathReview (John P. Lehoczky)](https://www.ams.org/mathscinet-getitem?mr=4398652)
  Cited by: [§1](#S1.p12.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [5]
  G. Callegaro, C. Ceci, and G. Ferrari (2020)
  Optimal reduction of public debt under partial observation of the economic growth.
  Finance and Stochastics 24 (4),  pp. 1083–1132.
  Cited by: [§A.1](#A1.SS1.1.p1.36 "Proof. ‣ A.1. Proof of Proposition 3.1 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§1](#S1.p12.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.2](#S3.SS2.p1.4 "3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§4](#S4.p1.1 "4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [6]
  J. Y. Campbell and J. H. Cochrane (1999)
  By force of habit: a consumption-based explanation of aggregate stock market behavior.
  Journal of Political Economy 107 (2),  pp. 205–251.
  Cited by: [§2.1](#S2.SS1.p3.5 "2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [7]
  S. Christensen, F. Crocce, E. Mordecki, and P. Salminen (2019)
  On optimal stopping of multidimensional diffusions.
  Stochastic Processes and their Applications 129 (7),  pp. 2561–2581.
  External Links: ISSN 0304-4149,1879-209X,
  [Document](https://dx.doi.org/10.1016/j.spa.2018.07.014),
  [Link](https://doi.org/10.1016/j.spa.2018.07.014),
  [MathReview Entry](https://www.ams.org/mathscinet-getitem?mr=3958442)
  Cited by: [§1](#S1.p12.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [8]
  T. De Angelis and G. Peskir (2020)
  Global C1C^{1} regularity of the value function in optimal stopping problems.
  The Annals of Applied Probability 30 (3),  pp. 1007–1031.
  External Links: ISSN 1050-5164,2168-8737,
  [Document](https://dx.doi.org/10.1214/19-AAP1517),
  [Link](https://doi.org/10.1214/19-AAP1517),
  [MathReview Entry](https://www.ams.org/mathscinet-getitem?mr=4133366)
  Cited by: [Remark 3.16](#S3.Thmtheorem16.p2.4.4 "Remark 3.16. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [9]
  T. De Angelis, S. Federico, and G. Ferrari (2017)
  Optimal boundary surface for irreversible investment with stochastic costs.
  Mathematics of Operations Research 42 (4),  pp. 1135–1161.
  Cited by: [§1](#S1.p12.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§4](#S4.2.p1.11 "Proof. ‣ 4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [10]
  T. De Angelis and G. Stabile (2019)
  On Lipschitz continuous optimal stopping boundaries.
  SIAM Journal on Control and Optimization 57 (1),  pp. 402–436.
  External Links: ISSN 0363-0129,1095-7138,
  [Document](https://dx.doi.org/10.1137/17M1113709),
  [Link](https://doi.org/10.1137/17M1113709),
  [MathReview (Zuoquan Xu)](https://www.ams.org/mathscinet-getitem?mr=3904414)
  Cited by: [§A.5](#A1.SS5.1.p1.12 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [Remark 3.16](#S3.Thmtheorem16.p2.4.4 "Remark 3.16. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [11]
  T. De Angelis (2020)
  Optimal dividends with partial information and stopping of a degenerate reflecting diffusion.
  Finance and Stochastics 24 (1),  pp. 71–123.
  Cited by: [§A.1](#A1.SS1.1.p1.36 "Proof. ‣ A.1. Proof of Proposition 3.1 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [12]
  N. El Karoui and M. Jeanblanc-Picqué (1998)
  Optimization of consumption with labor income.
  Finance and Stochastics 2 (4),  pp. 409–440.
  Cited by: [§1](#S1.p10.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§1](#S1.p5.9 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.2](#S2.SS2.p1.4 "2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [13]
  P. A. Ernst, H. Mei, and G. Peskir (2024)
  Quickest real-time detection of multiple brownian drifts.
  SIAM Journal on Control and Optimization 62 (3),  pp. 1832–1856.
  Cited by: [§3.4](#S3.SS4.3.p1.14 "Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [14]
  E. F. Fama and K. R. French (1988)
  Dividend yields and expected stock returns.
  Journal of Financial Economics 22 (1),  pp. 3–25.
  Cited by: [§1](#S1.p2.2 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.1](#S2.SS1.p4.9 "2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [15]
  S. Fan (2019)
  L1L^{1} solutions of non-reflected BSDEs and reflected BSDEs with one and two continuous barriers under general assumptions.
  Electronic Journal of Probability 24,  pp. 1–48.
  External Links: ISSN 1083-6489,
  [Document](https://dx.doi.org/10.1214/19-ejp345),
  [Link](https://doi.org/10.1214/19-ejp345),
  [MathReview (Ruili Song)](https://www.ams.org/mathscinet-getitem?mr=4003141)
  Cited by: [§2.2](#S2.SS2.1.p1.26 "Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.2](#S2.SS2.1.p1.33 "Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [16]
  G. Ferrari (2018)
  On the optimal management of public debt: a singular stochastic control problem.
  SIAM Journal on Control and Optimization 56 (3),  pp. 2036–2073.
  Cited by: [§1](#S1.p12.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.2](#S3.SS2.p1.4 "3.2. Derivation of the Auxiliary Optimal Stopping Problem ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [Remark 3.16](#S3.Thmtheorem16.p1.1.1 "Remark 3.16. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§4](#S4.p1.1 "4. Back to the Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [17]
  R. Frey (2000)
  Superreplication in stochastic volatility models and optimal stopping.
  Finance and Stochastics 4 (2),  pp. 161–187.
  External Links: ISSN 0949-2984,1432-1122,
  [Document](https://dx.doi.org/10.1007/s007800050010),
  [Link](https://doi.org/10.1007/s007800050010),
  [MathReview (Jakša Cvitanić)](https://www.ams.org/mathscinet-getitem?mr=1780325)
  Cited by: [§1](#S1.p14.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [18]
  P. Guasoni, E. Lawless, and H. M. Tai (2025)
  A variational approach to portfolio choice.
  Available at SSRN 5669613.
  Cited by: [§1](#S1.p11.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§1](#S1.p5.9 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [19]
  F. Gutekunst, M. Herdegen, and D. Hobson (2025)
  Optimal investment and consumption in a stochastic factor model.
  arXiv preprint arXiv:2509.09452.
  Cited by: [§1](#S1.p11.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§1](#S1.p5.9 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [Remark 2.3](#S2.Thmtheorem3.p1.1.1 "Remark 2.3. ‣ 2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [20]
  H. Hata, H. Nagai, and S. Sheu (2018)
  An optimal consumption problem for general factor models.
  SIAM Journal on Control and Optimization 56 (5),  pp. 3149–3183.
  Cited by: [§1](#S1.p11.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [21]
  H. Hata (2025)
  Optimal consumption and investment problem using a power utility function under a general nonlinear stochastic factor model.
  SIAM Journal on Control and Optimization 63 (5),  pp. 3588–3617.
  Cited by: [§1](#S1.p11.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [22]
  H. He and H. F. Pages (1993)
  Labor income, borrowing constraints, and equilibrium asset prices.
  Economic Theory 3 (4),  pp. 663–696.
  Cited by: [§1](#S1.p10.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§1](#S1.p5.9 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.2](#S2.SS2.p1.4 "2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [23]
  S. Jacka (1993)
  Local times, optimal stopping and semimartingales.
  The Annals of Probability,  pp. 329–339.
  Cited by: [§1](#S1.p7.6 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.4](#S3.SS4.7.p3.18 "Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.4](#S3.SS4.7.p3.4 "Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.4](#S3.SS4.p5.2 "3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [Remark 3.16](#S3.Thmtheorem16.p1.1.1 "Remark 3.16. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [24]
  J. Jeon, T. Kim, and Z. Yang (2025)
  The finite-horizon retirement problem with borrowing constraint: a zero-sum stopper vs. singular-controller game.
  SSRN Electronic Journal.
  Note: Available at SSRN
  External Links: [Document](https://dx.doi.org/10.2139/ssrn.4364441)
  Cited by: [§1](#S1.p10.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§1](#S1.p5.9 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.2](#S2.SS2.1.p1.3 "Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.2](#S2.SS2.p1.4 "2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [25]
  P. Johnson and G. Peskir (2017)
  Quickest detection problems for Bessel processes.
  The Annals of Applied Probability 27 (2),  pp. 1003–1056.
  External Links: ISSN 1050-5164,2168-8737,
  [Document](https://dx.doi.org/10.1214/16-AAP1223),
  [Link](https://doi.org/10.1214/16-AAP1223),
  [MathReview (Robert C. Dalang)](https://www.ams.org/mathscinet-getitem?mr=3655860)
  Cited by: [§1](#S1.p12.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [26]
  I. Karatzas and S. Shreve (2014)
  Brownian motion and stochastic calculus.
   Springer.
  Cited by: [§2.1](#S2.SS1.p10.1 "2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [27]
  T. S. Kim and E. Omberg (1996)
  Dynamic nonmyopic portfolio behavior.
  The Review of Financial Studies 9 (1),  pp. 141–161.
  Cited by: [§1](#S1.p11.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§1](#S1.p2.2 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.1](#S2.SS1.p3.5 "2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [28]
  D. Lamberton and G. Terenzi (2019)
  Properties of the american price function in the heston-type models.
  arXiv preprint arXiv:1904.01653.
  Cited by: [§1](#S1.p14.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [Remark 3.16](#S3.Thmtheorem16.p1.1.1 "Remark 3.16. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [29]
  D. Lamberton and G. Terenzi (2019)
  Variational formulation of american option prices in the heston model.
  SIAM Journal on Financial Mathematics 10 (1),  pp. 261–308.
  External Links: ISSN 1945-497X,
  [Document](https://dx.doi.org/10.1137/17M1158872),
  [Link](https://doi.org/10.1137/17M1158872),
  [MathReview (Wasim Ul-Haq)](https://www.ams.org/mathscinet-getitem?mr=3928342)
  Cited by: [§1](#S1.p14.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [30]
  R. Mehra and E. C. Prescott (1985)
  The equity premium: a puzzle.
  Journal of Monetary Economics 15 (2),  pp. 145–161.
  Cited by: [§2.1](#S2.SS1.p3.5 "2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [31]
  R. C. Merton (1971)
  Optimum consumption and portfolio rules in a continuous-time model.
  Journal of Economic Theory 3 (4),  pp. 373–413.
  External Links: ISSN 0022-0531,1095-7235,
  [Document](https://dx.doi.org/10.1016/0022-0531%2871%2990038-X),
  [Link](https://doi.org/10.1016/0022-0531(71)90038-X),
  [MathReview Entry](https://www.ams.org/mathscinet-getitem?mr=456373)
  Cited by: [§1](#S1.p5.9 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [32]
  R. C. Merton (1969)
  Lifetime portfolio selection under uncertainty: the continuous-time case.
  The Review of Economics and Statistics,  pp. 247–257.
  Cited by: [§1](#S1.p5.9 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [33]
  C. Munk and C. Sørensen (2004)
  Optimal consumption and investment strategies with stochastic interest rates.
  Journal of Banking & Finance 28 (8),  pp. 1987–2013.
  Cited by: [§1](#S1.p11.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [34]
  D. Nualart (2006)
  The malliavin calculus and related topics.
   Springer.
  Cited by: [§3.4](#S3.SS4.3.p1.14 "Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.4](#S3.SS4.6.p2.6 "Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [35]
  G. Peskir and A. Shiryaev (2006)
  Optimal stopping and free-boundary problems.
   Springer.
  Cited by: [§3.3](#S3.SS3.p5.5 "3.3. Preliminary Properties of the Optimal Stopping Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.4](#S3.SS4.p3.1 "3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [36]
  G. Peskir (2025)
  Weak solutions in the sense of Schwartz to Dynkin’s characteristic operator equation.
  Potential Analysis 63 (4),  pp. 1887–1905.
  External Links: ISSN 0926-2601,1572-929X,
  [Document](https://dx.doi.org/10.1007/s11118-025-10225-0),
  [Link](https://doi.org/10.1007/s11118-025-10225-0),
  [MathReview Entry](https://www.ams.org/mathscinet-getitem?mr=4990506)
  Cited by: [§3.4](#S3.SS4.4.p1.6 "Proof. ‣ 3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§3.4](#S3.SS4.p4.3 "3.4. Optimal Stopping Boundary and Regularity of the Value Function ‣ 3. The Dual Problem as a Singular Control Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [37]
  J. M. Poterba and L. H. Summers (1988)
  Mean reversion in stock prices: evidence and implications.
  Journal of Financial Economics 22 (1),  pp. 27–59.
  Cited by: [§1](#S1.p2.2 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.1](#S2.SS1.p4.9 "2.1. The Financial Market and the Agent’s Problem ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [38]
  P. E. Protter (2005)
  Stochastic integration and differential equations.
  Second edition, Stochastic Modelling and Applied Probability, Vol. 21, Springer-Verlag, Berlin.
  Note: Corrected third printing
  External Links: ISBN 3-540-00313-4,
  [Document](https://dx.doi.org/10.1007/978-3-662-10061-5),
  [Link](https://doi.org/10.1007/978-3-662-10061-5),
  [MathReview (Evelyn Buckwar)](https://www.ams.org/mathscinet-getitem?mr=2273672)
  Cited by: [§A.5](#A1.SS5.1.p1.32 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§A.5](#A1.SS5.1.p1.47 "Proof. ‣ A.5. Proof of Proposition 3.11 ‣ Appendix A Technical Proofs ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model"),
  [§2.2](#S2.SS2.1.p1.3 "Proof. ‣ 2.2. From a Dynamic to a Static Budget Constraint ‣ 2. The Primal Problem ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [39]
  N. Touzi (1999)
  American options exercise boundary when the volatility changes randomly.
  Applied Mathematics and Optimization 39 (3),  pp. 411–422.
  Cited by: [§1](#S1.p14.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").
* [40]
  J. A. Wachter (2002)
  Portfolio and consumption decisions under mean-reverting returns: an exact solution for complete markets.
  Journal of Financial and Quantitative Analysis 37 (1),  pp. 63–91.
  Cited by: [§1](#S1.p11.1 "1. Introduction ‣ Optimal Consumption and Portfolio Choice with No-Borrowing Constraint in the Kim-Omberg Model").

BETA