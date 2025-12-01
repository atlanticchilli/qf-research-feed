---
authors:
- Eduardo Abi Jaber
- Donatien Hainaut
- Edouard Motte
doc_id: arxiv:2511.23295v1
family_id: arxiv:2511.23295
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Signature approach for pricing and hedging path-dependent options with frictions
url_abs: http://arxiv.org/abs/2511.23295v1
url_html: https://arxiv.org/html/2511.23295v1
venue: arXiv q-fin
version: 1
year: 2025
---


Eduardo Abi Jaber
*eduardo.abi-jaber@polytechnique.edu.* EAJ is grateful for the financial support from the Chaires FiME-FDD and Financial Risks at Ecole Polytechnique.
Ecole Polytechnique, CMAP

Donatien Hainaut
*donatien.hainaut@uclouvain.be*
Université Catholique de Louvain, LIDAM-ISBA

Edouard Motte
*Corresponding author, edouard.motte@uclouvain.be.* EM is grateful for the financial support from the Fonds de la Recherche
Scientifique (F.R.S. - FNRS) through a FRIA grant.
Université Catholique de Louvain, LIDAM-ISBA

###### Abstract

We introduce a novel signature approach for pricing and hedging path-dependent options with instantaneous and permanent market impact under a mean-quadratic variation criterion. Leveraging the expressive power of signatures, we recast an inherently nonlinear and non-Markovian stochastic control problem into a tractable form, yielding hedging strategies in (possibly infinite) linear feedback form in the time-augmented signature of the control variables, with coefficients characterized by non-standard infinite-dimensional Riccati equations on the extended tensor algebra. Numerical experiments demonstrate the effectiveness of these signature-based strategies for pricing and hedging general path-dependent payoffs in the presence of frictions. In particular, market impact naturally smooths optimal trading strategies, making low-truncated signature approximations highly accurate and robust in frictional markets, contrary to the frictionless case.

††footnotetext: We would like to thank Louis-Amand Gérard and Dimitri Sotnikov for fruitful discussions and insightful comments.

Keywords: path-signatures, path-dependent options, market frictions, non-Markovian stochastic control, infinite-dimensional Riccati equations.

## 1 Introduction

Pricing and hedging derivatives is a central problem in quantitative finance. In classical complete models, perfect replication is achieved by trading continuously in the underlying asset, assuming frictionless markets. In practice, however, large trades affect prices. Two types of market impact are typically distinguished: temporary impact, which affects the execution price but not future mid-prices, and permanent impact, which shifts the future mid-price due to supply/demand imbalances. Accounting for these frictions transforms option hedging into a stochastic control problem, where the objective boils down to tracking certain option’s sensitivities (such as the delta) while balancing replication accuracy, trading costs, and market risk. The control problem usually falls outside the tractable linear-quadratic framework.

The majority of existing literature on pricing and hedging with frictions focuses on European payoffs. Solutions are typically characterized via Hamilton-Jacobi-Bellman (HJB) equations as in Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)); Becherer and Bilarev ([2018](https://arxiv.org/html/2511.23295v1#bib.bib11)); Cetin, Soner, and Touzi ([2010](https://arxiv.org/html/2511.23295v1#bib.bib14)); Ekren and Nadtochiy ([2022](https://arxiv.org/html/2511.23295v1#bib.bib22)); Rogers and Singh ([2010](https://arxiv.org/html/2511.23295v1#bib.bib32)); Bouchard, Loeper, and Zou ([2017](https://arxiv.org/html/2511.23295v1#bib.bib13)); Said ([2019](https://arxiv.org/html/2511.23295v1#bib.bib33)); Guéant and Pu ([2017](https://arxiv.org/html/2511.23295v1#bib.bib25)); Lions and Lasry ([2007](https://arxiv.org/html/2511.23295v1#bib.bib29)); Loeper ([2018](https://arxiv.org/html/2511.23295v1#bib.bib30)). While these frameworks provide rigorous insights for European options, they generally do not extend easily to path-dependent derivatives, such as Asian, barrier, or look-back options, whose payoffs depend on the entire trajectory of the underlying. Yet these are among the most common contracts in practice, especially in equity, FX, and commodity markets, making the gap between theory and applications particularly striking. A notable exception is the case of Accelerated Share Repurchase contracts with an Asian-type component studied by Guéant, Pu, and Royer ([2015](https://arxiv.org/html/2511.23295v1#bib.bib26)); Jaimungal, Kinzebulatov, and Rubisov ([2017](https://arxiv.org/html/2511.23295v1#bib.bib27)), where, after approximations and dimension reduction, the problem can be made Markovian in three dimensions. Another exception is the work of Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)), which considers general non-Markovian payoffs, with an instantaneous market impact component but without incorporating transient or permanent impact. In that setting, the problem falls back into the linear-quadratic class (with stochastic coefficients) and can be solved explicitly.

We develop a novel signature approach for hedging path-dependent options under both temporary and permanent impact within a mean-quadratic variation framework as in Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)). Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)) studied the problem of hedging European options,
and relate the optimal hedging strategies to an HJB equation. They obtain explicit solutions for European options with a constant Gamma. We extend their setting to path-dependent options, namely with signature payoffs.
Because the problem is inherently non-Markovian, the classical HJB approach is no longer applicable, which is the first major challenge. To overcome this, we lift the hedging problem into the space of path-signatures, which restores Markovianity. In principle, this leads to an infinite-dimensional HJB equation, but such an equation is numerically intractable, especially since permanent impact makes the control problem highly nonlinear and far beyond the linear-quadratic class.

The key insight is that, for polynomial European payoffs, the HJB equation decouples into a system of non-standard infinite-dimensional Riccati ordinary differential equations (ODE), thanks to the algebraic structure of polynomials, see Section [2.2](https://arxiv.org/html/2511.23295v1#S2.SS2 "2.2 Key observation for Markovian polynomial payoffs ‣ 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). Crucially, this algebraic structure is inherited by signatures, since signatures extend polynomials to path space. We leverage this to transform the nonlinear, path-dependent control problem into an infinite-dimensional yet numerically tractable Markovian framework. We relate the solution to an infinite-dimensional Riccati ODE system on the extended tensor algebra with an optimal hedging strategy given in linear feedback form in the time-extended signature of the control variables, see Theorem [5.9](https://arxiv.org/html/2511.23295v1#S5.Thmthm9 "Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). In short, the time-extended signatures of the control variables serve not only as the state variables of the control problem but also effectively linearize it leading to Riccati-type structures familiar from classical linear-quadratic control.

Our contribution falls naturally within the recent line of work on rough paths and signature methods, which provide hierarchical, finite-dimensional representations for encoding path-dependence.
In mathematical finance, path-signatures, introduced by Chen ([1957](https://arxiv.org/html/2511.23295v1#bib.bib15), [1977](https://arxiv.org/html/2511.23295v1#bib.bib16)), were recently used to solve different problems such as:

* •

  Pricing and hedging: Abi Jaber and Gérard ([2025a](https://arxiv.org/html/2511.23295v1#bib.bib1), [b](https://arxiv.org/html/2511.23295v1#bib.bib2)); Bayer, Pelizzari, and Zhu ([2025b](https://arxiv.org/html/2511.23295v1#bib.bib10)); Cuchiero, Gazzani, Möller, and Svaluto-Ferro ([2025a](https://arxiv.org/html/2511.23295v1#bib.bib19)); Lyons, Nejad, and Perez Arribas ([2020](https://arxiv.org/html/2511.23295v1#bib.bib31)),
* •

  Optimal stopping: Bayer, Hager, Riedel, and Schoenmakers ([2023](https://arxiv.org/html/2511.23295v1#bib.bib8), [2025a](https://arxiv.org/html/2511.23295v1#bib.bib9)),
* •

  Portfolio allocation and trading: Cuchiero and Möller ([2025](https://arxiv.org/html/2511.23295v1#bib.bib17)); Futter, Horvath, and Wiese ([2023](https://arxiv.org/html/2511.23295v1#bib.bib24)); Kalsi, Lyons, and Arribas ([2020](https://arxiv.org/html/2511.23295v1#bib.bib28)).

Moreover, Bank, Bayer, Hager, Riedel, and Nauen ([2025](https://arxiv.org/html/2511.23295v1#bib.bib7)) have recently used signatures to tackle stochastic control problems. They considered two signature-based classes of controls to approximate the class of admissible controls, showed that those classes are dense in the set of admissible controls, and proposed numerical methods to solve the problem. Compared to Bank, Bayer, Hager, Riedel, and Nauen ([2025](https://arxiv.org/html/2511.23295v1#bib.bib7)), we propose a distinct approach. Rather than restricting the optimization to a possibly smaller subset from the outset, we consider a general set of admissible progressively measurable controls. Using the standard martingale optimality principle, we then derive a verification result expressed in terms of an infinite-dimensional system of Riccati equations, which yields the optimal control in feedback form as a (possibly infinite) linear combination of time-extended signature elements, with the time-dependent coefficients given by the solutions of the Riccati equations. In the literature, for instance in Lyons, Nejad, and Perez Arribas ([2020](https://arxiv.org/html/2511.23295v1#bib.bib31)); Bank, Bayer, Hager, Riedel, and Nauen ([2025](https://arxiv.org/html/2511.23295v1#bib.bib7)), only time-independent coefficients have been considered so far when parameterizing the solutions in terms of time-extended signatures. This time-independence implies an approximation by controls that are analytic in the time variable, a property that the true optimal control generally does not satisfy. This provides one explanation for why our approach achieves greater accuracy and numerical stability.

For the first time in the context of stochastic optimal control, we establish this connection between non-Markovian control problems and infinite-dimensional Riccati equations on the extended tensor algebra. We note, however, that similar infinite-dimensional systems of Riccati equations have previously appeared in the literature for solving uncontrolled mathematical finance problems using signatures, to compute the characteristic function associated with signature volatility models and signature SDEs, see Abi Jaber and Gérard ([2025a](https://arxiv.org/html/2511.23295v1#bib.bib1)); Abi Jaber, Li, and Lin ([2024b](https://arxiv.org/html/2511.23295v1#bib.bib4)); Cuchiero, Svaluto-Ferro, and Teichmann ([2023](https://arxiv.org/html/2511.23295v1#bib.bib18)). A general existence and uniqueness theory for such Riccati equations and the associated convergence of the power expansions appears to be intricate and remains an open problem, with certain partial results available for the Riccati equations in Abi Jaber, Li, and Lin ([2024b](https://arxiv.org/html/2511.23295v1#bib.bib4)); Cuchiero, Svaluto-Ferro, and Teichmann ([2023](https://arxiv.org/html/2511.23295v1#bib.bib18)) and for the power series in Abi Jaber, Gérard, and Huang ([2024a](https://arxiv.org/html/2511.23295v1#bib.bib3)); Ben Arous ([1989](https://arxiv.org/html/2511.23295v1#bib.bib12)).

We show that our signature approach offers a flexible, systematic, and computationally feasible route to manage path-dependent payoffs in markets with frictions. In particular, our contributions can be summarized as follows:

* •

  Perfect hedging of signature payoffs in a frictionless market: We derive an explicit solution for the fair price and the perfect hedging strategy for signature payoffs using the Fawcett ([2003](https://arxiv.org/html/2511.23295v1#bib.bib23)) formula, as stated in Theorem [4.2](https://arxiv.org/html/2511.23295v1#S4.Thmthm2 "Theorem 4.2. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions").
* •

  Existence and uniqueness for the stochastic control problem with frictions: We use a variational approach to derive the existence and uniqueness of a solution to the stochastic control problem of hedging signature payoffs with market frictions in a mean-variation quadratic framework. More precisely, Theorem [5.5](https://arxiv.org/html/2511.23295v1#S5.Thmthm5 "Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") states that under a monotonicity condition ([5.16](https://arxiv.org/html/2511.23295v1#S5.E16 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) on the Gâteaux derivative of the gain functional, there exists a unique maximizer of the problem, which is also the unique solution of the first-order condition ([5.17](https://arxiv.org/html/2511.23295v1#S5.E17 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). We also provide two examples (see Proposition [5.6](https://arxiv.org/html/2511.23295v1#S5.Thmthm6 "Proposition 5.6. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") and Proposition [5.7](https://arxiv.org/html/2511.23295v1#S5.Thmthm7 "Proposition 5.7. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) where the monotonicity condition is fulfilled.
* •

  Verification result for the stochastic control problem with frictions: By combining the Itô formula for signatures (Theorem [3.4](https://arxiv.org/html/2511.23295v1#S3.Thmthm4 "Theorem 3.4 (Itô’s formula). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and a square completion approach, we derive a general verification theorem using the martingale optimality principle, see Theorem [5.9](https://arxiv.org/html/2511.23295v1#S5.Thmthm9 "Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). Under some assumptions, including the existence of a suitable solution to an infinite-dimensional system of Riccati equations given by ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and the convergence of the related infinite series, this theorem explicitly characterizes the optimal solution of the stochastic control problem in a feedback form as a linear combination of time-extended signature elements with time-dependent coefficients, see ([5.22](https://arxiv.org/html/2511.23295v1#S5.E22 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Moreover, we provide two concrete examples for which we can establish the existence of an explicit solution to the system of Riccati equations:

  1. (i)

     Proposition [5.15](https://arxiv.org/html/2511.23295v1#S5.Thmthm15 "Proposition 5.15 (No permanent market impact). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") considers the case without permanent impact and allows us to recover the result of (Bank, Soner, and Voß, [2017](https://arxiv.org/html/2511.23295v1#bib.bib6), Theorem 3.1), but applied to signature payoffs.
  2. (ii)

     Proposition [5.16](https://arxiv.org/html/2511.23295v1#S5.Thmthm16 "Proposition 5.16 (European quadratic payoff). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") considers European quadratic payoff, and we retrieve the result of (Almgren and Li, [2016](https://arxiv.org/html/2511.23295v1#bib.bib5), Eq. (25)).
* •

  Numerical illustrations: In Section [6](https://arxiv.org/html/2511.23295v1#S6 "6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we illustrate numerically our signature-based hedging strategies, given by Theorem [5.9](https://arxiv.org/html/2511.23295v1#S5.Thmthm9 "Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") by solving the system of infinite-dimensional Riccati equations ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), demonstrating that our approach can be effectively implemented even in highly path-dependent settings. First, we consider exact signature payoffs, such as European or Asian quadratic options, using sanity checks against explicit solutions to validate both the assumptions of Theorem [5.9](https://arxiv.org/html/2511.23295v1#S5.Thmthm9 "Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") and our numerical implementation. Second, we consider more general path-dependent payoffs, which we approximate by signature payoffs relying on the universal approximation theorem. In the frictional market, we show that the signature-based strategy computed via the Riccati system for the approximate signature payoffs provides a sufficiently accurate approximation of the true optimal strategy, demonstrating a striking improvement compared to signature-based strategies in the frictionless setting. This improvement can be attributed to the fact that market impact naturally smooths the optimal trading strategies, making polynomial approximations more accurate and efficient.
  We also evaluate the impact of the permanent market impact component on both the fair price and the hedging strategies of several path-dependent options.

The paper is outlined as follows. In Section [2](https://arxiv.org/html/2511.23295v1#S2 "2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we introduce the Bachelier framework with both temporary and permanent market impact. Then, Section [3](https://arxiv.org/html/2511.23295v1#S3 "3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions") recalls key results on path-signatures. In Section [4](https://arxiv.org/html/2511.23295v1#S4 "4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we first address the hedging of a signature payoff in frictionless market and we deduce the perfect hedging strategy using the Fawcett ([2003](https://arxiv.org/html/2511.23295v1#bib.bib23)) formula. Section [5](https://arxiv.org/html/2511.23295v1#S5 "5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") is devoted to the stochastic control problem of hedging a signature payoff under market impact within a mean-quadratic variation framework, where we establish an existence and uniqueness result (Section [5.1](https://arxiv.org/html/2511.23295v1#S5.SS1 "5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and provide a verification theorem (Section [5.2](https://arxiv.org/html/2511.23295v1#S5.SS2 "5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Finally, Section [6](https://arxiv.org/html/2511.23295v1#S6 "6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions") presents numerical illustrations.

## 2 Bachelier model with temporary and permanent impact

We fix a finite horizon T>0T>0 and a filtered probability space (Ω,ℱ,(ℱt)0≤t≤T,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{0\leq t\leq T},\mathbb{P})
with filtration (ℱt)0≤t≤T(\mathcal{F}\_{t})\_{0\leq t\leq T} that satisfies the usual conditions. We consider a financial market with a tradable asset (St)t∈[0,T](S\_{t})\_{t\in[0,T]} with dynamic

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=μ​d​t+σ​d​Wt,t≤T,\displaystyle dS\_{t}=\mu dt+\sigma dW\_{t},\penalty 10000\ t\leq T, |  | (2.1) |

with μ∈ℝ,\mu\in\mathbb{R}, σ∈ℝ+\sigma\in\mathbb{R}\_{+} and WW a standard Brownian motion. In this financial market, a trader shorts an option on SS that she aims to hedge. We assume that by trading the asset, the trader incurs both temporary and permanent market impacts which affect her profit and loss (P&L). More precisely, if (Xtθ)t∈[0,T](X\_{t}^{\theta})\_{t\in[0,T]} denotes the number of shares held by the trader through time defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtθ=X0+∫0tθs​𝑑s,X\_{t}^{\theta}=X\_{0}+\int\_{0}^{t}\theta\_{s}ds, |  | (2.2) |

with X0∈ℝX\_{0}\in\mathbb{R} 111As explained in Guéant and Pu ([2017](https://arxiv.org/html/2511.23295v1#bib.bib25)), X0X\_{0} corresponds to the number of shares in the hedging portfolio at inception. In illiquid markets, the client that buys the option may provide an initial number of shares (see Section [5](https://arxiv.org/html/2511.23295v1#S5 "5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Therefore, we could consider X0=0X\_{0}=0 or the case where X0X\_{0} is equal to the Bachelier Δ\Delta of the option sold, depending on the initial agreement with the client., and (θt)t∈[0,T](\theta\_{t})\_{t\in[0,T]} the trading speed, the price of the asset, taking account of permanent impact, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ptθ=St+ν​(Xtθ−X0),t≤T,P\_{t}^{\theta}=S\_{t}+\nu(X\_{t}^{\theta}-X\_{0}),\quad t\leq T, |  | (2.3) |

with ν≥0,\nu\geq 0, the permanent market impact parameter. Moreover, as the trader incurs transaction costs (temporary impact), the effective traded asset price is

|  |  |  |  |
| --- | --- | --- | --- |
|  | P~tθ=Ptθ+η​θt,t≤T,\tilde{P}\_{t}^{\theta}=P\_{t}^{\theta}+\eta\theta\_{t},\quad t\leq T, |  | (2.4) |

with η≥0,\eta\geq 0, the temporary price impact parameter.

### 2.1 The Almgren and Li setup

Before addressing the problem of hedging signature payoffs with market impacts, and to get more insight about our motivation to use a signature approach in this context, let us start from the Markovian framework of Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)). For this, we fix a European option whose frictionless Bachelier delta at time tt is Δ​(t,St)\Delta(t,S\_{t}) and we consider the problem of hedging this option with temporary and permanent market impact. This essentially boils down to tracking the Bachelier delta Δ​(t,Ptθ)\Delta(t,P^{\theta}\_{t}) evaluated with the impacted price PθP^{\theta} given by ([2.3](https://arxiv.org/html/2511.23295v1#S2.E3 "In 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)) consider a mean-quadratic variation criteria on the P&Lθ\mbox{P\&L}^{\theta} generated by the trading strategy θ\theta of the form222The mean-quadratic variation hedging problem is introduced in detail in Section [5](https://arxiv.org/html/2511.23295v1#S5 "5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(P&LTθ−λ2​[P&Lθ,P&Lθ]T),\mathbb{E}\left(\mbox{P\&L}\_{T}^{\theta}-\frac{\lambda}{2}[\mbox{P\&L}^{\theta},\mbox{P\&L}^{\theta}]\_{T}\right), |  |

where λ>0\lambda>0 is the risk aversion of the trader. The aim is to maximize the criterion over the trading strategies θ\theta. Using a dynamic programming approach, they characterized the solution in terms of the solution to a Hamilton-Jacobi-Bellman (HJB) equation. More precisely, they showed that the value function J​(t,p,x)J(t,p,x) depends, at time t<Tt<T, on (Ptθ,Xtθ)(P^{\theta}\_{t},X^{\theta}\_{t}) and satisfies a nonlinear HJB equation of the following form333The HJB equation differs slightly from that in Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)) because, in this paper, we consider a short position to be hedged and XθX^{\theta} as a state variable instead of Yθ:=Xθ−Δ​(t,Pθ)Y^{\theta}:=X^{\theta}-\Delta(t,P^{\theta}). Moreover, we also assume no overnight risk and μ≠0\mu\neq 0.444Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)) do not provide existence or well-posedness results for the HJB equation ([2.5](https://arxiv.org/html/2511.23295v1#S2.E5 "In 2.1 The Almgren and Li setup ‣ 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). For a rigorous analysis of related HJB equations, see Ekren and Nadtochiy ([2022](https://arxiv.org/html/2511.23295v1#bib.bib22)).:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Jt=−λ2​σ2​[x−Δ​(t,p)]2−12​σ2​Jp​p+14​η​[ν​(x−Δ​(t,p))−Jx−ν​Jp]2\displaystyle J\_{t}=-\frac{\lambda}{2}\sigma^{2}\left[x-\Delta(t,p)\right]^{2}-\frac{1}{2}\sigma^{2}J\_{pp}+\frac{1}{4\eta}\left[\nu(x-\Delta(t,p))-J\_{x}-\nu J\_{p}\right]^{2} |  | (2.5) |
|  |  | +μ​[(x−Δ​(t,p))−Jp],\displaystyle\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ +\mu\left[(x-\Delta(t,p))-J\_{p}\right], |  |
|  |  | J​(T,p,x)=0.\displaystyle J(T,p,x)=0. |  |

When the Bachelier Gamma Γ​(t,p)\Gamma(t,p) is constant, i.e. Γ​(t,p)=Γ∈ℝ\Gamma(t,p)=\Gamma\in\mathbb{R}, for all (t,p)∈[0,T]×ℝ+(t,p)\in[0,T]\times\mathbb{R}^{+}, and μ=0\mu=0, they deduced that J​(t,p,x)J(t,p,x) has an explicit form. This explicit solution follows from the fact that, when Γ\Gamma is constant, the problem becomes linear-quadratic: a constant gamma implies that the delta is linear in
pp, and therefore that the payoff is quadratic. A natural idea is thus to extend this observation to more general polynomial payoffs.

### 2.2 Key observation for Markovian polynomial payoffs

In fact, we can go further and obtain a semi-explicit characterization of the solution in terms of infinite dimensional Riccati ordinary differential equations when we consider polynomial payoffs of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | HTθ=∑i=0Mαi​(PTθ)i,(αi)i=1,..,M∈ℝM,M∈ℕ.H\_{T}^{\theta}=\sum\_{i=0}^{M}\alpha\_{i}\left(P\_{T}^{\theta}\right)^{i},\penalty 10000\ (\alpha\_{i})\_{i=1,..,M}\in\mathbb{R}^{M},\penalty 10000\ M\in\mathbb{N}. |  | (2.6) |

Then, there exists (δi​(t))i=0,…,M∈ℝM(\delta\_{i}(t))\_{i=0,...,M}\in\mathbb{R}^{M} such that

|  |  |  |
| --- | --- | --- |
|  | Δ​(t,p)=∑i=0M−1δi​(t)​pi.\Delta(t,p)=\sum\_{i=0}^{M-1}\delta\_{i}(t)p^{i}. |  |

Making an ansatz on the value function of the form of a power series in pp and xx:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,p,x)=∑i,j=0+∞ψti,j​pi​xj,\displaystyle J(t,p,x)=\sum\_{i,j=0}^{+\infty}\psi\_{t}^{i,j}p^{i}x^{j}, |  | (2.7) |

and plugging this ansatz in ([2.5](https://arxiv.org/html/2511.23295v1#S2.E5 "In 2.1 The Almgren and Li setup ‣ 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), the HJB equation decouples into a system of infinite-dimensional Riccati equations given, for i,j∈ℕi,j\in\mathbb{N}, by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ψ˙ti,j=−12​σ2​ψti+2,j−λ2​σ2​(𝜷t∗𝜷t)i,j+14​η​(𝝍~t∗𝝍~t)i,j\displaystyle\dot{\psi}\_{t}^{i,j}=-\frac{1}{2}\sigma^{2}\psi\_{t}^{i+2,j}-\frac{\lambda}{2}\sigma^{2}\left(\bm{\beta}\_{t}\*\bm{\beta}\_{t}\right)^{i,j}+\frac{1}{4\eta}\left(\bm{\tilde{\psi}}\_{t}\*\bm{\tilde{\psi}}\_{t}\right)^{i,j} |  | (2.8) |
|  |  | +μ​[βti,j−(i+1)​ψti+1,j],\displaystyle\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ +\mu\left[\beta\_{t}^{i,j}-(i+1)\psi\_{t}^{i+1,j}\right], |  |
|  |  | ψTi,j=0,\displaystyle\psi\_{T}^{i,j}=0, |  |

with, 𝜷t=(βti,j)i,j≥0\bm{\beta}\_{t}=\left(\beta\_{t}^{i,j}\right)\_{i,j\geq 0} and 𝝍~t=(ψ~ti,j)i,j≥0\bm{\tilde{\psi}}\_{t}=\left(\tilde{\psi}\_{t}^{i,j}\right)\_{i,j\geq 0} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | βti,j\displaystyle\beta\_{t}^{i,j} | :=𝟙{i=0}∩{j=1}−𝟙{i≤M−1}∩{j=0}​δi​(t),\displaystyle:=\mathbb{1}\_{\{i=0\}\cap\{j=1\}}-\mathbb{1}\_{\{i\leq M-1\}\cap\{j=0\}}\delta\_{i}(t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~ti,j\displaystyle\tilde{\psi}\_{t}^{i,j} | :=ν​βti,j−ν​ψti+1,j​(i+1)−ψti,j+1​(j+1),\displaystyle:=\nu\beta\_{t}^{i,j}-\nu\psi\_{t}^{i+1,j}(i+1)-\psi\_{t}^{i,j+1}(j+1), |  |

and the 2​D2D Cauchy product defined, for 𝐚=(ai,j)i,j≥0,𝐛=(bi,j)i,j≥0\mathbf{a}=\left(a^{i,j}\right)\_{i,j\geq 0},\penalty 10000\ \mathbf{b}=\left(b^{i,j}\right)\_{i,j\geq 0}, by

|  |  |  |
| --- | --- | --- |
|  | (𝐚∗𝐛)i,j:=∑m=0i∑n=0jam​n​bi−m,j−n.\left(\mathbf{a}\*\mathbf{b}\right)^{i,j}:=\sum\_{m=0}^{i}\sum\_{n=0}^{j}a^{mn}b^{i-m,j-n}. |  |

Therefore, in the Markovian case (European payoffs), by restricting ourselves to polynomial payoffs, we can semi-explicitly express the optimal solution as a power series in the state variables with deterministic coefficients ψ\psi coming from an infinite-dimensional system of Riccati equations. Since path-signatures play a similar role to polynomials on the path space, by considering signatures payoffs, we can naturally expect to be able to derive the same kind of characterization for the control problem in the non-Markovian case, and this is precisely what is established in our main result, Theorem [5.9](https://arxiv.org/html/2511.23295v1#S5.Thmthm9 "Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions").

## 3 Reminder on signatures

In this section, we provide a reminder about the path-signature theory. We also refer to the first sections in Lyons et al. ([2020](https://arxiv.org/html/2511.23295v1#bib.bib31)); Bayer et al. ([2023](https://arxiv.org/html/2511.23295v1#bib.bib8)); Cuchiero et al. ([2023](https://arxiv.org/html/2511.23295v1#bib.bib18)); Abi Jaber et al. ([2024a](https://arxiv.org/html/2511.23295v1#bib.bib3)).

### 3.1 Tensor algebra

Let d∈ℕd\in\mathbb{N} and denote by ⊗\otimes the tensor product over ℝd\mathbb{R}^{d}, e.g. (x⊗y⊗z)i​j​k=xi​yj​zk(x\otimes y\otimes z)\_{ijk}=x\_{i}y\_{j}z\_{k}, for i,j,k=1,…,di,j,k=1,\dots,d, for x,y,z∈ℝdx,y,z\in\mathbb{R}^{d}. For n≥1n\geq 1, we denote by (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} the space of tensors of order nn and by (ℝd)⊗0=ℝ(\mathbb{R}^{d})^{\otimes 0}=\mathbb{R}. In this paper, we consider path-signatures that are mathematical objects that live on the extended tensor algebra space T​((ℝd))T((\mathbb{R}^{d})) over ℝd\mathbb{R}^{d}, that is the space of (infinite) sequences of tensors defined by

|  |  |  |
| --- | --- | --- |
|  | T​((ℝd)):={ℓ=(ℓn)n=0∞:ℓn∈(ℝd)⊗n}.T((\mathbb{R}^{d})):=\left\{\bm{\ell}=(\bm{\ell}^{n})\_{n=0}^{\infty}:\bm{\ell}^{n}\in(\mathbb{R}^{d})^{\otimes n}\right\}. |  |

For M≥0M\geq 0, we define the truncated tensor algebra TM​(ℝd)T^{M}(\mathbb{R}^{d}) as the space of sequences of tensors of order at most MM defined by

|  |  |  |
| --- | --- | --- |
|  | TM​(ℝd):={ℓ∈T​((ℝd)):ℓn=0, for all ​n>M},T^{M}(\mathbb{R}^{d}):=\left\{\bm{\ell}\in T((\mathbb{R}^{d})):\bm{\ell}^{n}=0,\text{ for all }n>M\right\}, |  |

and the tensor algebra T​(ℝd)T(\mathbb{R}^{d}) as the space of all finite sequences of tensors defined by

|  |  |  |
| --- | --- | --- |
|  | T​(ℝd):=⋃M∈ℕTM​(ℝd).T(\mathbb{R}^{d}):=\bigcup\_{M\in\mathbb{N}}T^{M}(\mathbb{R}^{d}). |  |

For ℓ=(ℓn)n∈ℕ,𝒑=(𝒑n)n∈ℕ∈T​((ℝd))\bm{\ell}=(\bm{\ell}^{n})\_{n\in\mathbb{N}},\penalty 10000\ \bm{p}=(\bm{p}^{n})\_{n\in\mathbb{N}}\in T((\mathbb{R}^{d})) and λ∈ℝ\lambda\in\mathbb{R}, we define the following operations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ+𝒑:\displaystyle\bm{\ell}+\bm{p}: | =(ℓn+𝒑n)n∈ℕ\displaystyle=(\bm{\ell}^{n}+\bm{p}^{n})\_{n\in\mathbb{N}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ⊗𝒑:\displaystyle\bm{\ell}\otimes\bm{p}: | =(∑k=0nℓk⊗𝒑n−k)n∈ℕ\displaystyle=\left(\sum\_{k=0}^{n}\bm{\ell}^{k}\otimes\bm{p}^{n-k}\right)\_{n\in\mathbb{N}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​ℓ:\displaystyle\lambda\bm{\ell}: | =(λ​ℓn)n∈ℕ.\displaystyle=(\lambda\bm{\ell}^{n})\_{n\in\mathbb{N}}. |  |

These operations induce analogous operations on TM​(ℝd)T^{M}(\mathbb{R}^{d}) and T​(ℝd)T(\mathbb{R}^{d}).

Let {e1,…,ed}⊂ℝd\{e\_{1},\dots,e\_{d}\}\subset\mathbb{R}^{d} be the canonical basis of ℝd\mathbb{R}^{d} and Ad={\mathcolor​N​a​v​y​B​l​u​e​𝟏,\mathcolor​N​a​v​y​B​l​u​e​𝟐,…,\mathcolor​N​a​v​y​B​l​u​e​𝐝}{A}\_{d}=\{{\mathcolor{NavyBlue}{\mathbf{1}}},{\mathcolor{NavyBlue}{\mathbf{2}}},\dots,{\mathcolor{NavyBlue}{\mathbf{d}}}\} be the corresponding alphabet. To ease reading, for i∈{1,…,d}i\in\{1,\dots,d\}, we write eie\_{i} as the blue letter \mathcolor​N​a​v​y​B​l​u​e​𝐢{\mathcolor{NavyBlue}{\mathbf{i}}} and for n≥1,i1,…,in∈{1,…,d}n\geq 1,i\_{1},\dots,i\_{n}\in\{1,\dots,d\}, we write ei1⊗⋯⊗eine\_{i\_{1}}\otimes\cdots\otimes e\_{i\_{n}} as the concatenation of letters \mathcolor​N​a​v​y​B​l​u​e​𝐢𝟏​⋯​𝐢𝐧{\mathcolor{NavyBlue}{\mathbf{i\_{1}\cdots i\_{n}}}}, that we call a word of length nn. We note that (ei1⊗⋯⊗ein)(i1,…,in)∈{1,…,d}n(e\_{i\_{1}}\otimes\cdots\otimes e\_{i\_{n}})\_{(i\_{1},\dots,i\_{n})\in\{1,\dots,d\}^{n}} is a basis of (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} that can be identified with the set of words of length nn defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn:={\mathcolor​N​a​v​y​B​l​u​e​𝐢𝟏​⋯​𝐢𝐧:\mathcolor​N​a​v​y​B​l​u​e​𝐢𝐤∈Ad​ for ​k=1,2,…,n}.V\_{n}:=\{{\mathcolor{NavyBlue}{\mathbf{i\_{1}\cdots i\_{n}}}}:{\mathcolor{NavyBlue}{\mathbf{i\_{k}}}}\in{A}\_{d}\text{ for }k=1,2,\dots,n\}. |  | (3.1) |

Moreover, ø denotes the empty word and V0={ø}V\_{0}=\{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}\} serves as a basis for (ℝd)⊗0=ℝ(\mathbb{R}^{d})^{\otimes 0}=\mathbb{R}. It follows that V:=∪n≥0VnV:=\cup\_{n\geq 0}V\_{n} represents the standard basis of T​((ℝd))T((\mathbb{R}^{d})). In this case, every ℓ∈T​((ℝd))\bm{\ell}\in T((\mathbb{R}^{d})), can be decomposed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ=∑n=0∞∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vnℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯​\mathcolor​N​a​v​y​B​l​u​e​𝐯,\bm{\ell}=\sum\_{n=0}^{\infty}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\bm{\ell}^{{\mathcolor{NavyBlue}{\mathbf{v}}}}{\mathcolor{NavyBlue}{\mathbf{v}}}, |  | (3.2) |

where ℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯\bm{\ell}^{\mathcolor{NavyBlue}{\mathbf{v}}} is the real coefficient of ℓ\bm{\ell} at coordinate \mathcolor​N​a​v​y​B​l​u​e​𝐯{\mathcolor{NavyBlue}{\mathbf{v}}}.

We now introduce two important concepts such as the concatenation and the projection. The concatenation ℓ​\mathcolor​N​a​v​y​B​l​u​e​𝐯\bm{\ell}{\mathcolor{NavyBlue}{\mathbf{v}}} of elements ℓ∈T​((ℝd))\bm{\ell}\in T((\mathbb{R}^{d})) and the word \mathcolor​N​a​v​y​B​l​u​e​𝐯=\mathcolor​N​a​v​y​B​l​u​e​𝐢𝟏​⋯​𝐢𝐧{\mathcolor{NavyBlue}{\mathbf{v}}}={\mathcolor{NavyBlue}{\mathbf{i\_{1}\cdots i\_{n}}}} means ℓ⊗ei1⊗⋯⊗ein\bm{\ell}\otimes e\_{i\_{1}}\otimes\cdots\otimes e\_{i\_{n}}. The projection ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐮∈T​((ℝd))\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{u}}}}\in T((\mathbb{R}^{d})) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐮:=∑n=0∞∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vnℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯𝐮​\mathcolor​N​a​v​y​B​l​u​e​𝐯\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{u}}}}:=\sum\_{n=0}^{\infty}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\bm{\ell}^{{\mathcolor{NavyBlue}{\mathbf{vu}}}}{\mathcolor{NavyBlue}{\mathbf{v}}} |  | (3.3) |

for all \mathcolor​N​a​v​y​B​l​u​e​𝐮∈V{\mathcolor{NavyBlue}{\mathbf{u}}}\in V. Moreover, if we consider ξ∈T​((ℝd))\xi\in T((\mathbb{R}^{d})), then we define the projection ℓ|ξ∈T​((ℝd))\bm{\ell}|\_{\xi}\in T((\mathbb{R}^{d})) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ|ξ:=∑n=0∞∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vn[∑m=0∞∑\mathcolor​N​a​v​y​B​l​u​e​𝐮∈Vmℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯𝐮​ξ\mathcolor​N​a​v​y​B​l​u​e​𝐮]​\mathcolor​N​a​v​y​B​l​u​e​𝐯.\bm{\ell}|\_{\xi}:=\sum\_{n=0}^{\infty}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\left[\sum\_{m=0}^{\infty}\sum\_{{\mathcolor{NavyBlue}{\mathbf{u}}}\in V\_{m}}\bm{\ell}^{{\mathcolor{NavyBlue}{\mathbf{vu}}}}\xi^{{\mathcolor{NavyBlue}{\mathbf{u}}}}\right]{\mathcolor{NavyBlue}{\mathbf{v}}}. |  | (3.4) |

The projection plays an important role in the space of iterated integrals as it is closely linked to partial differentiation, in contrast with the concatenation that relates to integration. We now define the bracket between ℓ∈T​(ℝd)\bm{\ell}\in T(\mathbb{R}^{d}), and 𝒑∈T​((ℝd))\bm{p}\in T((\mathbb{R}^{d})) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ℓ,𝒑⟩:=∑n=0∞∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vnℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯​𝒑\mathcolor​N​a​v​y​B​l​u​e​𝐯.\displaystyle\langle\bm{\ell},\bm{p}\rangle:=\sum\_{n=0}^{\infty}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\bm{\ell}^{{\mathcolor{NavyBlue}{\mathbf{v}}}}\bm{p}^{{\mathcolor{NavyBlue}{\mathbf{v}}}}. |  | (3.5) |

We observe that the bracket is well defined since ℓ∈T​(ℝd)\bm{\ell}\in T(\mathbb{R}^{d}) and has therefore finitely many non-zero terms. For ℓ∈T​((ℝd))\bm{\ell}\in T((\mathbb{R}^{d})), the series in ([3.5](https://arxiv.org/html/2511.23295v1#S3.E5 "In 3.1 Tensor algebra ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")) involves infinitely many terms and requires special care to be well defined. We discuss it in Subsection [3.3](https://arxiv.org/html/2511.23295v1#S3.SS3 "3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions"). Finally, we consider another operation on the space of words which is the shuffle product. The shuffle product plays a crucial role for an integration by parts formula on the space of iterated integrals, see Proposition [3.3](https://arxiv.org/html/2511.23295v1#S3.Thmthm3 "Proposition 3.3 (Shuffle property). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions") below.

###### Definition 3.1 (Shuffle product).

The shuffle product ⊔⁣⊔:V×V→T(ℝd)\mathrel{\sqcup\mkern-3.2mu\sqcup}:V\times V\to T(\mathbb{R}^{d}) is defined inductively for all words \mathcolor​N​a​v​y​B​l​u​e​𝐯{\mathcolor{NavyBlue}{\mathbf{v}}} and \mathcolor​N​a​v​y​B​l​u​e​𝐰{\mathcolor{NavyBlue}{\mathbf{w}}} and all letters \mathcolor​N​a​v​y​B​l​u​e​𝐢{\mathcolor{NavyBlue}{\mathbf{i}}} and \mathcolor​N​a​v​y​B​l​u​e​𝐣{\mathcolor{NavyBlue}{\mathbf{j}}} in Ad{A}\_{d} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (\mathcolor​N​a​v​y​B​l​u​e​𝐯​\mathcolor​N​a​v​y​B​l​u​e​𝐢)⊔⁣⊔(\mathcolor​N​a​v​y​B​l​u​e​𝐰​\mathcolor​N​a​v​y​B​l​u​e​𝐣)\displaystyle({\mathcolor{NavyBlue}{\mathbf{v}}}{\mathcolor{NavyBlue}{\mathbf{i}}})\mathrel{\sqcup\mkern-3.2mu\sqcup}({\mathcolor{NavyBlue}{\mathbf{w}}}{\mathcolor{NavyBlue}{\mathbf{j}}}) | =(\mathcolor​N​a​v​y​B​l​u​e​𝐯⊔⁣⊔(\mathcolor​N​a​v​y​B​l​u​e​𝐰​\mathcolor​N​a​v​y​B​l​u​e​𝐣))​\mathcolor​N​a​v​y​B​l​u​e​𝐢+((\mathcolor​N​a​v​y​B​l​u​e​𝐯​\mathcolor​N​a​v​y​B​l​u​e​𝐢)⊔⁣⊔\mathcolor​N​a​v​y​B​l​u​e​𝐰)​\mathcolor​N​a​v​y​B​l​u​e​𝐣,\displaystyle=({\mathcolor{NavyBlue}{\mathbf{v}}}\mathrel{\sqcup\mkern-3.2mu\sqcup}({\mathcolor{NavyBlue}{\mathbf{w}}}{\mathcolor{NavyBlue}{\mathbf{j}}})){\mathcolor{NavyBlue}{\mathbf{i}}}+(({\mathcolor{NavyBlue}{\mathbf{v}}}{\mathcolor{NavyBlue}{\mathbf{i}}})\mathrel{\sqcup\mkern-3.2mu\sqcup}{\mathcolor{NavyBlue}{\mathbf{w}}}){\mathcolor{NavyBlue}{\mathbf{j}}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | \mathcolor​N​a​v​y​B​l​u​e​𝐰⊔⁣⊔ø\displaystyle{\mathcolor{NavyBlue}{\mathbf{w}}}\mathrel{\sqcup\mkern-3.2mu\sqcup}{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}} | =ø⊔⁣⊔\mathcolor​N​a​v​y​B​l​u​e​𝐰=\mathcolor​N​a​v​y​B​l​u​e​𝐰.\displaystyle={\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}\mathrel{\sqcup\mkern-3.2mu\sqcup}{\mathcolor{NavyBlue}{\mathbf{w}}}={\mathcolor{NavyBlue}{\mathbf{w}}}. |  |

With some abuse of notation, the shuffle product on T​((ℝd))T((\mathbb{R}^{d})) induced by the shuffle product on VV is also be denoted by ⊔⁣⊔\mathrel{\sqcup\mkern-3.2mu\sqcup}.

### 3.2 Signatures

We define the (path) signature of a semimartingale process as the sequence of iterated stochastic integrals in the sense of Stratonovich. Notice that, in the paper, we denote the Itô integral by ∫0⋅Yt​𝑑Xt\int\_{0}^{\cdot}Y\_{t}dX\_{t} and the Stratonovich integral by ∫0⋅Yt∘𝑑Xt.\int\_{0}^{\cdot}Y\_{t}\circ dX\_{t}.

###### Definition 3.2.

Fix T>0T>0. Let (Xt)t≥0(X\_{t})\_{t\geq 0} be a continuous semimartingale in ℝd\mathbb{R}^{d} on some filtered probability space (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}). The signature of XX is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕏:Ω×[0,T]\displaystyle\mathbb{X}:\Omega\times[0,T] | →T​((ℝd))\displaystyle\to T((\mathbb{R}^{d})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (ω,t)\displaystyle(\omega,t) | ↦𝕏t​(ω):=(1,𝕏t1​(ω),…,𝕏tn​(ω),…),\displaystyle\mapsto\mathbb{X}\_{t}(\omega):=(1,\mathbb{X}\_{t}^{1}(\omega),\dots,\mathbb{X}\_{t}^{n}(\omega),\dots), |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝕏tn:=∫0<u1<⋯<un<t∘dXu1⊗⋯⊗∘dXun\mathbb{X}\_{t}^{n}:=\int\_{0<u\_{1}<\cdots<u\_{n}<t}\circ dX\_{u\_{1}}\otimes\cdots\otimes\circ dX\_{u\_{n}} |  |

takes value in (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n}, n≥0n\geq 0. Similarly, the truncated signature of order M∈ℕM\in\mathbb{N} is defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝕏≤M:[0,T]\displaystyle\mathbb{X}^{\leq M}:[0,T] | →TM​(ℝd)\displaystyle\to T^{M}(\mathbb{R}^{d}) |  | (3.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (ω,t)\displaystyle(\omega,t) | ↦𝕏t≤M​(ω):=(1,𝕏t1​(ω),…,𝕏tM​(ω),0,…,0,…).\displaystyle\mapsto\mathbb{X}\_{t}^{\leq M}(\omega):=(1,\mathbb{X}\_{t}^{1}(\omega),\dots,\mathbb{X}\_{t}^{M}(\omega),0,\dots,0,\dots). |  | (3.7) |

The signature plays a similar role to polynomials on path-space. Indeed, in dimension d=1d=1, the signature of XX is the sequence of monomials (1n!​(Xt−X0)n)n∈ℕ\left(\frac{1}{n!}(X\_{t}-X\_{0})^{n}\right)\_{n\in\mathbb{N}}. In particular, any finite combination of elements of the signature ⟨ℓ,𝕏t⟩\left\langle\bm{\ell},\mathbb{X}\_{t}\right\rangle, defined in ([3.5](https://arxiv.org/html/2511.23295v1#S3.E5 "In 3.1 Tensor algebra ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")) for ℓ∈TM​(ℝd)\bm{\ell}\in T^{M}(\mathbb{R}^{d}), is a polynomial of degree MM in XtX\_{t}. For example, if d=2d=2 and Xt=W^t:=(t,Wt)X\_{t}=\widehat{W}\_{t}:=(t,W\_{t}) where WW is a 1-dimensional Brownian motion, the first few signature orders are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕎^t0=1,𝕎^t1=(tWt),𝕎^t2=(t22!∫0ts​𝑑Ws∫0tWs​𝑑sWt22!)\widehat{\mathbb{W}}\_{t}^{0}=1,\quad\widehat{\mathbb{W}}\_{t}^{1}=\begin{pmatrix}t\\ W\_{t}\end{pmatrix},\quad\widehat{\mathbb{W}}\_{t}^{2}=\begin{pmatrix}\frac{t^{2}}{2!}&\int\_{0}^{t}sdW\_{s}\\ \int\_{0}^{t}W\_{s}ds&\frac{W\_{t}^{2}}{2!}\end{pmatrix} |  | (3.8) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕎^t3=(t33!∫0ts22!​𝑑Ws∫0t∫0su​𝑑Wu​𝑑s∫0t∫0su​𝑑Wu∘𝑑Ws∫0t∫0sWu​𝑑u​𝑑s∫0t∫0sWu​𝑑u∘𝑑Ws∫0tWs22!​𝑑sWt33!).\widehat{\mathbb{W}}\_{t}^{3}=\begin{pmatrix}\frac{t^{3}}{3!}&\int\_{0}^{t}\frac{s^{2}}{2!}dW\_{s}&\\ \int\_{0}^{t}\int\_{0}^{s}udW\_{u}ds&\int\_{0}^{t}\int\_{0}^{s}udW\_{u}\circ dW\_{s}&\\ &\int\_{0}^{t}\int\_{0}^{s}W\_{u}duds&\int\_{0}^{t}\int\_{0}^{s}W\_{u}du\circ dW\_{s}\\ &\int\_{0}^{t}\frac{W\_{s}^{2}}{2!}ds&\frac{W\_{t}^{3}}{3!}\end{pmatrix}. |  | (3.9) |

### 3.3 Infinite linear combinations of signature elements

In this section, we recall some results on infinite linear combinations ⟨ℓ,𝕏t⟩\langle{\bm{\ell}},\mathbb{X}\_{t}\rangle for certain admissible ℓ∈T​((ℝd))\bm{\ell}\in T((\mathbb{R}^{d})) for which the infinite series makes sense. The crucial ingredients for this paper are the shuffle product (Proposition [3.3](https://arxiv.org/html/2511.23295v1#S3.Thmthm3 "Proposition 3.3 (Shuffle property). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and an Itô’s formula (Theorem [3.4](https://arxiv.org/html/2511.23295v1#S3.Thmthm4 "Theorem 3.4 (Itô’s formula). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Those results are based on Abi Jaber et al. ([2024a](https://arxiv.org/html/2511.23295v1#bib.bib3)), and we refer to this paper for more details.

We first consider the space 𝒜​(𝕏)\mathcal{A}(\mathbb{X}) of admissible elements ℓ\bm{\ell} below, using the associated semi-norm:

|  |  |  |
| --- | --- | --- |
|  | ‖ℓ‖t𝒜​(𝕏):=∑n=0∞|∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vnℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯​𝕏t\mathcolor​N​a​v​y​B​l​u​e​𝐯|,t≥0,||\bm{\ell}||\_{t}^{\mathcal{A}(\mathbb{X})}:=\sum\_{n=0}^{\infty}\left|\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\bm{\ell}^{\mathcolor{NavyBlue}{\mathbf{v}}}\mathbb{X}^{\mathcolor{NavyBlue}{\mathbf{v}}}\_{t}\right|,\quad t\geq 0, |  |

recall the definition of VnV\_{n} in ([3.1](https://arxiv.org/html/2511.23295v1#S3.E1 "In 3.1 Tensor algebra ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and the decomposition ([3.2](https://arxiv.org/html/2511.23295v1#S3.E2 "In 3.1 Tensor algebra ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
Whenever, ‖ℓ‖t𝒜​(𝕏)<∞||\bm{\ell}||\_{t}^{\mathcal{A}(\mathbb{X})}<\infty a.s., the infinite linear combination

|  |  |  |
| --- | --- | --- |
|  | ⟨ℓ,𝕏t⟩=∑n=0∞∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vnℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯​𝕏\mathcolor​N​a​v​y​B​l​u​e​𝐯\langle{\bm{\ell}},{\mathbb{X}}\_{t}\rangle=\sum\_{n=0}^{\infty}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\bm{\ell}^{{\mathcolor{NavyBlue}{\mathbf{v}}}}\mathbb{X}^{{\mathcolor{NavyBlue}{\mathbf{v}}}} |  |

is well defined. This leads to the following definition for the admissible set 𝒜​(𝕏)\mathcal{A}(\mathbb{X}):

|  |  |  |
| --- | --- | --- |
|  | 𝒜​(𝕏):={ℓ∈T​((ℝd)):‖ℓ‖t𝒜​(𝕏)<∞​ for all ​t∈[0,T]​ a.s.}.\mathcal{A}(\mathbb{X}):=\left\{\bm{\ell}\in T((\mathbb{R}^{d})):||\bm{\ell}||\_{t}^{\mathcal{A}(\mathbb{X})}<\infty\text{ for all }t\in[0,T]\text{ a.s.}\right\}. |  |

Note that T​(ℝd)⊂𝒜​(𝕏)T(\mathbb{R}^{d})\subset\mathcal{A}(\mathbb{X}) and that ⟨ℓ,𝕏t⟩\langle{\bm{\ell}},\mathbb{X}\_{t}\rangle is an extension of ([3.5](https://arxiv.org/html/2511.23295v1#S3.E5 "In 3.1 Tensor algebra ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")), as the two bracket operations ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle coincide whenever ℓ∈T​(ℝd)\bm{\ell}\in T(\mathbb{R}^{d}). The admissible set 𝒜​(𝕏)\mathcal{A}(\mathbb{X}) enables us to linearize polynomials on infinite linear combination of the signature. This is what is commonly referred to in the literature as the linearization power of the signature.

###### Proposition 3.3 (Shuffle property).

If ℓ1,ℓ2∈𝒜​(𝕏)\bm{\ell}\_{1},\bm{\ell}\_{2}\in\mathcal{A}(\mathbb{X}), then ℓ1⊔⁣⊔ℓ2∈𝒜​(𝕏)\bm{\ell}\_{1}\mathrel{\sqcup\mkern-3.2mu\sqcup}\bm{\ell}\_{2}\in\mathcal{A}(\mathbb{X}) and

|  |  |  |
| --- | --- | --- |
|  | ⟨ℓ1,𝕏t⟩​⟨ℓ2,𝕏t⟩=⟨ℓ1⊔⁣⊔ℓ2,𝕏t⟩.\langle{\bm{\ell}\_{1}},{\mathbb{X}}\_{t}\rangle\langle{\bm{\ell}\_{2}},{\mathbb{X}}\_{t}\rangle=\langle\bm{\ell}\_{1}\mathrel{\sqcup\mkern-3.2mu\sqcup}\bm{\ell}\_{2},{\mathbb{X}}\_{t}\rangle. |  |

By the definition of the admissible set 𝒜​(𝕏)\mathcal{A}(\mathbb{X}), we know that, for elements ℓ∈𝒜​(𝕏)\bm{\ell}\in\mathcal{A}(\mathbb{X}), the process (⟨ℓ,𝕏t⟩)t≤T(\langle\bm{\ell},\mathbb{X}\_{t}\rangle)\_{t\leq T} is well defined. This naturally raises the question of when it is a semimartingale and how to obtain its Itô decomposition. For elements ℓ\bm{\ell} in the set ℐ​(𝕏)\mathcal{I}(\mathbb{X}) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(𝕏):={ℓ∈𝒜​(𝕏):for every \mathcolor​N​a​v​y​B​l​u​e​𝐢∈Ad​ and \mathcolor​N​a​v​y​B​l​u​e​𝐣∈𝒬\mathcolor​N​a​v​y​B​l​u​e​𝐢​(X),ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐢,ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐣𝐢∈𝒜​(𝕏)​ and ∫0T(||ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐢||t𝒜​(𝕏)​d​|X\mathcolor​N​a​v​y​B​l​u​e​𝐢|t+||ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐣𝐢||t𝒜​(𝕏)​d​[X\mathcolor​N​a​v​y​B​l​u​e​𝐢,X\mathcolor​N​a​v​y​B​l​u​e​𝐣]t+(||ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐢||t𝒜​(𝕏))2​d​[X\mathcolor​N​a​v​y​B​l​u​e​𝐢,X\mathcolor​N​a​v​y​B​l​u​e​𝐣]t)<∞​ a.s.},\mathcal{I}(\mathbb{X}):=\left\{\begin{array}[]{l}\bm{\ell}\in\mathcal{A}(\mathbb{X}):\\ \text{for every }{\mathcolor{NavyBlue}{\mathbf{i}}}\in A\_{d}\text{ and }{\mathcolor{NavyBlue}{\mathbf{j}}}\in\mathcal{Q}\_{\mathcolor{NavyBlue}{\mathbf{i}}}(X),\penalty 10000\ \bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}},\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{ji}}}}\in\mathcal{A}(\mathbb{X})\text{ and }\\ \int\_{0}^{T}\left(||\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}}||\_{t}^{\mathcal{A}(\mathbb{X})}d|X^{\mathcolor{NavyBlue}{\mathbf{i}}}|\_{t}+||\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{ji}}}}||\_{t}^{\mathcal{A}(\mathbb{X})}d[X^{\mathcolor{NavyBlue}{\mathbf{i}}},X^{\mathcolor{NavyBlue}{\mathbf{j}}}]\_{t}+\left(||\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}}||\_{t}^{\mathcal{A}(\mathbb{X})}\right)^{2}d[X^{\mathcolor{NavyBlue}{\mathbf{i}}},X^{\mathcolor{NavyBlue}{\mathbf{j}}}]\_{t}\right)<\infty\text{ a.s.}\end{array}\right\}, |  | (3.10) |

where 𝒬\mathcolor​N​a​v​y​B​l​u​e​𝐢​(X)\mathcal{Q}\_{{\mathcolor{NavyBlue}{\mathbf{i}}}}(X) defines the set of coordinates of XX that have a
non-zero quadratic covariation with X\mathcolor​N​a​v​y​B​l​u​e​𝐢X^{\mathcolor{NavyBlue}{\mathbf{i}}}

|  |  |  |
| --- | --- | --- |
|  | 𝒬\mathcolor​N​a​v​y​B​l​u​e​𝐢​(X):={\mathcolor​N​a​v​y​B​l​u​e​𝐣∈Ad:[X\mathcolor​N​a​v​y​B​l​u​e​𝐣,X\mathcolor​N​a​v​y​B​l​u​e​𝐢]t≠0,on a set of non-zero ​d​t⊗d​ℙ​ measure},\displaystyle\mathcal{Q}\_{{\mathcolor{NavyBlue}{\mathbf{i}}}}(X):=\left\{{\mathcolor{NavyBlue}{\mathbf{j}}}\in A\_{d}:[X^{\mathcolor{NavyBlue}{\mathbf{j}}},X^{\mathcolor{NavyBlue}{\mathbf{i}}}]\_{t}\neq 0,\text{on a set of non-zero }dt\otimes d\mathbb{P}\text{ measure}\right\}, |  |

then, we can prove that (⟨ℓ,𝕏t⟩)t≤T(\langle\bm{\ell},\mathbb{X}\_{t}\rangle)\_{t\leq T} is a semimartingale and we can compute its Itô decomposition. Notice that, for M>0M>0, we have TM​(ℝd)∈ℐ​(𝕏)T^{M}(\mathbb{R}^{d})\in\mathcal{I}(\mathbb{X}), i.e. showing that finite linear combinations of the signature are always semimartingales. More generally, we recall the result for time-dependent linear combinations (⟨ℓt,𝕏t⟩)t≤T(\langle\bm{\ell}\_{t},\mathbb{X}\_{t}\rangle)\_{t\leq T} with ℓ:[0,T]→𝒜​(𝕏)\bm{\ell}:[0,T]\to\mathcal{A}(\mathbb{X}) in the set

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ′​(𝕏):={ℓ:[0,T]→𝒜​(𝕏):for every \mathcolor​N​a​v​y​B​l​u​e​𝐯∈V,ℓ\mathcolor​N​a​v​y​B​l​u​e​𝐯∈C1​([0,T],ℝ),for every \mathcolor​N​a​v​y​B​l​u​e​𝐢∈Ad​ and \mathcolor​N​a​v​y​B​l​u​e​𝐣∈𝒬\mathcolor​N​a​v​y​B​l​u​e​𝐢​(X)​ and for all ​t∈[0,T],ℓt|\mathcolor​N​a​v​y​B​l​u​e​𝐢,ℓt|\mathcolor​N​a​v​y​B​l​u​e​𝐣𝐢,ℓt˙∈𝒜​(𝕏)​ and ∫0T(||ℓt|\mathcolor​N​a​v​y​B​l​u​e​𝐢||t𝒜​(𝕏)​d​|X\mathcolor​N​a​v​y​B​l​u​e​𝐢|t+||ℓt|\mathcolor​N​a​v​y​B​l​u​e​𝐣𝐢||t𝒜​(𝕏)​d​[X\mathcolor​N​a​v​y​B​l​u​e​𝐢,X\mathcolor​N​a​v​y​B​l​u​e​𝐣]t+(||ℓt|\mathcolor​N​a​v​y​B​l​u​e​𝐢||t𝒜​(𝕏))2​d​[X\mathcolor​N​a​v​y​B​l​u​e​𝐢,X\mathcolor​N​a​v​y​B​l​u​e​𝐣]t)<∞},\mathcal{I}^{{}^{\prime}}(\mathbb{X}):=\left\{\penalty 10000\ \begin{array}[]{l}\bm{\ell}:[0,T]\to\mathcal{A}(\mathbb{X}):\\ \text{for every }{\mathcolor{NavyBlue}{\mathbf{v}}}\in V,\>\bm{\ell}^{\mathcolor{NavyBlue}{\mathbf{v}}}\in C^{1}([0,T],\mathbb{R}),\\ \text{for every }{\mathcolor{NavyBlue}{\mathbf{i}}}\in A\_{d}\text{ and }{\mathcolor{NavyBlue}{\mathbf{j}}}\in\mathcal{Q}\_{\mathcolor{NavyBlue}{\mathbf{i}}}(X)\text{ and for all }t\in[0,T],\penalty 10000\ \bm{\ell}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}},\bm{\ell}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{ji}}}},\dot{\bm{\ell}\_{t}}\in\mathcal{A}(\mathbb{X})\text{ and }\\ \int\_{0}^{T}\left(||\bm{\ell}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}}||\_{t}^{\mathcal{A}(\mathbb{X})}d|X^{\mathcolor{NavyBlue}{\mathbf{i}}}|\_{t}+||\bm{\ell}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{ji}}}}||\_{t}^{\mathcal{A}(\mathbb{X})}d[X^{\mathcolor{NavyBlue}{\mathbf{i}}},X^{\mathcolor{NavyBlue}{\mathbf{j}}}]\_{t}+\left(||\bm{\ell}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}}||\_{t}^{\mathcal{A}(\mathbb{X})}\right)^{2}d[X^{\mathcolor{NavyBlue}{\mathbf{i}}},X^{\mathcolor{NavyBlue}{\mathbf{j}}}]\_{t}\right)<\infty\end{array}\right\}, |  | (3.11) |

where ℓt˙:=∑n=0∞∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vndd​t​ℓt\mathcolor​N​a​v​y​B​l​u​e​𝐯​\mathcolor​N​a​v​y​B​l​u​e​𝐯\dot{\bm{\ell}\_{t}}:=\sum\_{n=0}^{\infty}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\frac{d}{dt}\bm{\ell}\_{t}^{\mathcolor{NavyBlue}{\mathbf{v}}}{\mathcolor{NavyBlue}{\mathbf{v}}} for all t∈[0,T]t\in[0,T].

###### Theorem 3.4 (Itô’s formula).

Let ℓ∈ℐ​(𝕏)\bm{\ell}\in\mathcal{I}(\mathbb{X}), then ⟨ℓ,𝕏t⟩\langle\bm{\ell},{\mathbb{X}}\_{t}\rangle is an Itô process such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ℓ,𝕏t⟩=ℓø+∑i∈Ad∫0t⟨ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐢,𝕏s⟩​𝑑Xsi+12​∑i∈Ad∑j∈Ad∫0t⟨ℓ|\mathcolor​N​a​v​y​B​l​u​e​𝐣𝐢,𝕏s⟩​d​[Xj,Xi]s,t≤T.\displaystyle\langle{\bm{\ell}},{\mathbb{X}}\_{t}\rangle=\bm{\ell}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}+\sum\_{i\in A\_{d}}\int\_{0}^{t}\langle{\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}},\mathbb{X}\_{s}\rangle dX\_{s}^{i}+\tfrac{1}{2}\sum\_{i\in A\_{d}}\sum\_{j\in A\_{d}}\int\_{0}^{t}\langle\bm{\ell}|\_{{\mathcolor{NavyBlue}{\mathbf{ji}}}}},{\mathbb{X}}\_{s}\rangle d[X^{j},X^{i}]\_{s},\penalty 10000\ t\leq T. |  | (3.12) |

Moreover, if ℓ∈ℐ′​(𝕏)\bm{\ell}\in\mathcal{I}^{{}^{\prime}}(\mathbb{X}), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ℓt,𝕏t⟩=ℓtø+∑i∈Ad∫0t⟨ℓs|\mathcolor​N​a​v​y​B​l​u​e​𝐢,𝕏s⟩​𝑑Xsi+12​∑i∈Ad∑j∈Ad∫0t⟨ℓs|\mathcolor​N​a​v​y​B​l​u​e​𝐣𝐢,𝕏s⟩​d​[Xj,Xi]s+∫0t⟨ℓ˙s,𝕏s⟩​𝑑s,t≤T.\displaystyle\langle{\bm{\ell}\_{t}},{\mathbb{X}}\_{t}\rangle=\bm{\ell}\_{t}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}+\sum\_{i\in A\_{d}}\int\_{0}^{t}\langle{\bm{\ell}\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{i}}}},\mathbb{X}\_{s}\rangle dX\_{s}^{i}+\tfrac{1}{2}\sum\_{i\in A\_{d}}\sum\_{j\in A\_{d}}\int\_{0}^{t}\langle\bm{\ell}\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{ji}}}}},{\mathbb{X}}\_{s}\rangle d[X^{j},X^{i}]\_{s}+\int\_{0}^{t}\langle\dot{\bm{\ell}}\_{s},\mathbb{X}\_{s}\rangle ds,\penalty 10000\ t\leq T. |  | (3.13) |

###### Proof.

We refer to (Abi Jaber et al., [2024a](https://arxiv.org/html/2511.23295v1#bib.bib3), Theorem 3.3. and Corollary 3.4.) for the proof.
∎

## 4 Pricing and perfect hedging in frictionless market

In this section, we first show how to price and perfectly replicate a signature payoff in a frictionless market. This perfect hedging strategy will enter in the hedging problem with market impact in Section [5](https://arxiv.org/html/2511.23295v1#S5 "5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). In the absence of market impact, i.e. η=ν=0\eta=\nu=0, the asset traded price is StS\_{t}.
In this context, we consider that the trader wants to hedge a given signature payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | HT=⟨ξ,𝕊^T⟩,H\_{T}=\left\langle\xi,\hat{\mathbb{S}}\_{T}\right\rangle, |  | (4.1) |

for a certain admissible ξ∈T​(ℝ2)\xi\in T(\mathbb{R}^{2}), hence ξ\xi has a finite number of non-zero terms. We start by giving some examples of path-dependent payoffs that can be exactly represented as signature payoffs.

###### Example 4.1.

Signature payoffs include:

* •

  European polynomial payoffs of the form HT=∑k=0Nαk​(ST−K)kH\_{T}=\sum\_{k=0}^{N}\alpha\_{k}(S\_{T}-K)^{k}, for given N∈ℕN\in\mathbb{N}, K∈ℝK\in\mathbb{R} and (αk)k≤N∈ℝN(\alpha\_{k})\_{k\leq N}\in\mathbb{R}^{N}, since HT=⟨∑k=0Nαk​(\mathcolor​N​a​v​y​B​l​u​e​𝟐+ø​(S0−K))⊔⁣⊔k,𝕊^T⟩H\_{T}=\left\langle\sum\_{k=0}^{N}\alpha\_{k}\left({\mathcolor{NavyBlue}{\mathbf{2}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}(S\_{0}-K)\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}k},\hat{\mathbb{S}}\_{T}\right\rangle;
* •

  Asian polynomial payoffs of the form HT=∑k=0Nαk​(1T​∫0TSt​𝑑t−K)kH\_{T}=\sum\_{k=0}^{N}\alpha\_{k}\left(\frac{1}{T}\int\_{0}^{T}S\_{t}dt-K\right)^{k}, for given N∈ℕN\in\mathbb{N}, K∈ℝK\in\mathbb{R} and (αk)k≤N∈ℝN(\alpha\_{k})\_{k\leq N}\in\mathbb{R}^{N}, since HT=⟨∑k=0Nαk​(1T​\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟏−ø​K)⊔⁣⊔k,𝕊^T⟩H\_{T}=\left\langle\sum\_{k=0}^{N}\alpha\_{k}\left(\frac{1}{T}{\mathcolor{NavyBlue}{\mathbf{21}}}-{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}K\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}k},\hat{\mathbb{S}}\_{T}\right\rangle.

■\blacksquare

Let (VtX)t∈[0,T](V\_{t}^{X})\_{t\in[0,T]} denote the hedging portfolio of the trader such that

|  |  |  |
| --- | --- | --- |
|  | d​VtX=Xt​d​St,V0X=V0∈ℝ+.dV\_{t}^{X}=X\_{t}dS\_{t},\quad V\_{0}^{X}=V\_{0}\in\mathbb{R}^{+}. |  |

where XX is an admissible hedging in

|  |  |  |
| --- | --- | --- |
|  | ℒ2:={X:[0,T]×Ω→ℝ​prog. measurable process such that ​𝔼​(∫0TXt2​𝑑t)<∞}.\mathcal{L}^{2}:=\left\{X:[0,T]\times\Omega\rightarrow\mathbb{R}\penalty 10000\ \text{prog. measurable process such that }\mathbb{E}\left(\int\_{0}^{T}X\_{t}^{2}dt\right)<\infty\right\}. |  |

The fair pricing of the option corresponds to V0.V\_{0}. For ℓ∈T​((ℝd))\bm{\ell}\in T((\mathbb{R}^{d})), let us define the tensor product exponential as

|  |  |  |
| --- | --- | --- |
|  | exp⊗⁡(ℓ):=∑k≥0ℓ⊗kk!.\exp\_{\otimes}(\bm{\ell}):=\sum\_{k\geq 0}\frac{\bm{\ell}^{\otimes k}}{k!}. |  |

In the frictionless market, a perfect hedging strategy can be deduced using the quantity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξt:=ξ|ℰT−t,t≤T,\xi\_{t}:=\xi|\_{\mathcal{E}\_{T-t}},\quad t\leq T, |  | (4.2) |

recall the projection defined by ([3.4](https://arxiv.org/html/2511.23295v1#S3.E4 "In 3.1 Tensor algebra ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions")), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt=exp⊗⁡((\mathcolor​N​a​v​y​B​l​u​e​𝟏+σ22​\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐)​t)\displaystyle\mathcal{E}\_{t}=\exp\_{\otimes}\left(\left({\mathcolor{NavyBlue}{\mathbf{1}}}+\frac{\sigma^{2}}{2}{\mathcolor{NavyBlue}{\mathbf{22}}}\right)t\right) |  | (4.3) |

corresponds to the expectation of the signature of the time-augmented stock price SS under the risk-neutral probability measure thanks to the Fawcett ([2003](https://arxiv.org/html/2511.23295v1#bib.bib23)) formula.

###### Theorem 4.2.

Let ξ∈T​(ℝ2)\xi\in T(\mathbb{R}^{2}). Then, (ξt)t≤T\left(\xi\_{t}\right)\_{t\leq T} defined by ([4.2](https://arxiv.org/html/2511.23295v1#S4.E2 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions"))is well defined for all t≤Tt\leq T and belongs to ℐ′​(𝕊^)\mathcal{I}^{\prime}(\widehat{\mathbb{S}}). Furthermore, the option ([4.1](https://arxiv.org/html/2511.23295v1#S4.E1 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) can be perfectly hedged using the portfolio with initial wealth V0=ξ0øV\_{0}=\xi\_{0}^{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}} and strategy Xt=⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,𝕊^t⟩X\_{t}=\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{S}}\_{t}\right\rangle, that is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  |  | VTX=HT=⟨ξ,𝕊^T⟩,\displaystyle V^{X}\_{T}=H\_{T}=\left\langle\xi,\hat{\mathbb{S}}\_{T}\right\rangle, |  | (4.4a) |
| In particular, | | | | |
|  |  | VtX=⟨ξt,𝕊^t⟩,t≤T.\displaystyle V^{X}\_{t}=\langle\xi\_{t},\hat{\mathbb{S}}\_{t}\rangle,\quad t\leq T. |  | (4.4b) |

###### Proof.

The proof follows from two following lemmas. By combining Lemma [4.3](https://arxiv.org/html/2511.23295v1#S4.Thmthm3 "Lemma 4.3. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions") and Lemma [4.4](https://arxiv.org/html/2511.23295v1#S4.Thmthm4 "Lemma 4.4. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we deduce that the signature payoff ⟨ξ,𝕊^T⟩\langle\xi,\hat{\mathbb{S}}\_{T}\rangle can be perfectly replicated using the portfolio with initial wealth V0=ξ0øV\_{0}=\xi\_{0}^{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}} and strategy Xt=⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,𝕊^t⟩X\_{t}=\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{S}}\_{t}\right\rangle.
∎

###### Lemma 4.3.

Let ξ∈T​(ℝ2)\xi\in T(\mathbb{R}^{2}). Assume that there exists (ξt)t∈[0,T]∈ℐ′​(𝕊^)(\xi\_{t})\_{t\in[0,T]}\in\mathcal{I}^{\prime}(\widehat{\mathbb{S}}) satisfying the following equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ˙t=−ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟏−12​σ2​ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐,ξT=ξ.\displaystyle\dot{\xi}\_{t}=-\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}-\frac{1}{2}\sigma^{2}\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}},\quad\xi\_{T}=\xi. |  | (4.5) |

Then, the option ([4.1](https://arxiv.org/html/2511.23295v1#S4.E1 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) can be perfectly hedged using the portfolio with initial wealth V0=ξ0øV\_{0}=\xi\_{0}^{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}} and strategy Xt=⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,𝕊^t⟩X\_{t}=\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{S}}\_{t}\right\rangle, that is ([4.4a](https://arxiv.org/html/2511.23295v1#S4.E4.1 "In 4.4 ‣ Theorem 4.2. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and ([4.4b](https://arxiv.org/html/2511.23295v1#S4.E4.2 "In 4.4 ‣ Theorem 4.2. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) are satisfied.

###### Proof.

First, by applying the Itô’s formula in Theorem [3.4](https://arxiv.org/html/2511.23295v1#S3.Thmthm4 "Theorem 3.4 (Itô’s formula). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions") to (⟨ξt,𝕊^t⟩)t≤T\left(\langle\xi\_{t},\hat{\mathbb{S}}\_{t}\rangle\right)\_{t\leq T} and using ([4.5](https://arxiv.org/html/2511.23295v1#S4.E5 "In Lemma 4.3. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ξT,𝕊^T⟩\displaystyle\langle\xi\_{T},\hat{\mathbb{S}}\_{T}\rangle | =ξ0ø+∫0T⟨ξt˙+ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟏+μ​ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐+12​σ2​ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐,𝕊^t⟩​𝑑t+∫0Tσ​⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,𝕊^t⟩​𝑑Wt,\displaystyle=\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}+\int\_{0}^{T}\langle\dot{\xi\_{t}}+\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}+\mu\penalty 10000\ \xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\frac{1}{2}\sigma^{2}\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}},\hat{\mathbb{S}}\_{t}\rangle dt+\int\_{0}^{T}\sigma\penalty 10000\ \langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{S}}\_{t}\rangle dW\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ξ0ø+∫0T⟨μ​ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,𝕊^t⟩​𝑑t+∫0Tσ​⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,𝕊^t⟩​𝑑Wt.\displaystyle=\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}+\int\_{0}^{T}\langle\mu\penalty 10000\ \xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{S}}\_{t}\rangle dt+\int\_{0}^{T}\sigma\penalty 10000\ \langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{S}}\_{t}\rangle dW\_{t}. |  |

But as

|  |  |  |
| --- | --- | --- |
|  | VTX=V0+∫0Tμ​Xt​𝑑t+σ​∫0TXt​𝑑Wt,\displaystyle V\_{T}^{X}=V\_{0}+\int\_{0}^{T}\mu X\_{t}dt+\sigma\int\_{0}^{T}X\_{t}dW\_{t}, |  |

we observe that by taking

|  |  |  |
| --- | --- | --- |
|  | Xt=⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,𝕊^t⟩​ and ​V0=ξ0ø,\displaystyle X\_{t}=\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{S}}\_{t}\rangle\text{ and }V\_{0}=\xi\_{0}^{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}, |  |

then, we directly obtain ([4.4b](https://arxiv.org/html/2511.23295v1#S4.E4.2 "In 4.4 ‣ Theorem 4.2. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and ([4.4a](https://arxiv.org/html/2511.23295v1#S4.E4.1 "In 4.4 ‣ Theorem 4.2. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
∎

###### Lemma 4.4.

Let ξ∈T​(ℝ2)\xi\in T(\mathbb{R}^{2}). Then, (ξt)t≤T(\xi\_{t})\_{t\leq T} given by ([4.2](https://arxiv.org/html/2511.23295v1#S4.E2 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is well defined, belongs to ℐ′​(𝕊^)\mathcal{I}^{\prime}(\widehat{\mathbb{S}}) and satisfies equation ([4.5](https://arxiv.org/html/2511.23295v1#S4.E5 "In Lemma 4.3. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")).

###### Proof.

First, since ξ∈T​(ℝ2)\xi\in T(\mathbb{R}^{2}), we know that there exists M>0M>0 such that ξ∈TM​(ℝ2)\xi\in T^{M}(\mathbb{R}^{2}). Thus, we deduce that ξt\xi\_{t} has finitely many non-zero terms and is well defined, such that ξt∈ℐ′​(𝕊^)\xi\_{t}\in\mathcal{I}^{\prime}(\hat{\mathbb{S}}). Then, as ξt=ξ|ℰT−t\xi\_{t}=\xi|\_{\mathcal{E}\_{T-t}}, we have that

|  |  |  |
| --- | --- | --- |
|  | ξt=∑n=0M∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vnξt\mathcolor​N​a​v​y​B​l​u​e​𝐯​𝐯,\xi\_{t}=\sum\_{n=0}^{M}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\xi^{{\mathcolor{NavyBlue}{\mathbf{v}}}}\_{t}\mathbf{v}, |  |

with, for each \mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vn,n≤M{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n},\penalty 10000\ n\leq M,

|  |  |  |
| --- | --- | --- |
|  | ξt\mathcolor​N​a​v​y​B​l​u​e​𝐯=∑m=0M−n∑\mathcolor​N​a​v​y​B​l​u​e​𝐰∈Vmξ\mathcolor​N​a​v​y​B​l​u​e​𝐯𝐰​ℰT−t\mathcolor​N​a​v​y​B​l​u​e​𝐰.\xi\_{t}^{\mathcolor{NavyBlue}{\mathbf{v}}}=\sum\_{m=0}^{M-n}\sum\_{{\mathcolor{NavyBlue}{\mathbf{w}}}\in V\_{m}}\xi^{{\mathcolor{NavyBlue}{\mathbf{vw}}}}\mathcal{E}\_{T-t}^{\mathcolor{NavyBlue}{\mathbf{w}}}. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | ℰ˙T−t=−(\mathcolor​N​a​v​y​B​l​u​e​𝟏+12​\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐)⊗ℰT−t,\dot{\mathcal{E}}\_{T-t}=-\left({\mathcolor{NavyBlue}{\mathbf{1}}}+\frac{1}{2}{\mathcolor{NavyBlue}{\mathbf{22}}}\right)\otimes\mathcal{E}\_{T-t}, |  |

we observe that, for each \mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vn,n≤M{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n},\penalty 10000\ n\leq M,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξt˙\mathcolor​N​a​v​y​B​l​u​e​𝐯\displaystyle\dot{\xi\_{t}}^{\mathcolor{NavyBlue}{\mathbf{v}}} | =−∑m=0M−n∑\mathcolor​N​a​v​y​B​l​u​e​𝐰∈Vmξ\mathcolor​N​a​v​y​B​l​u​e​𝐯𝐰​((\mathcolor​N​a​v​y​B​l​u​e​𝟏+σ22​\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐)⊗ℰT−t)\mathcolor​N​a​v​y​B​l​u​e​𝐰\displaystyle=-\sum\_{m=0}^{M-n}\sum\_{{\mathcolor{NavyBlue}{\mathbf{w}}}\in V\_{m}}\xi^{{\mathcolor{NavyBlue}{\mathbf{vw}}}}\left(\left({\mathcolor{NavyBlue}{\mathbf{1}}}+\frac{\sigma^{2}}{2}{\mathcolor{NavyBlue}{\mathbf{22}}}\right)\otimes\mathcal{E}\_{T-t}\right)^{\mathcolor{NavyBlue}{\mathbf{w}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑m=0M−n∑\mathcolor​N​a​v​y​B​l​u​e​𝐰∈Vmξ\mathcolor​N​a​v​y​B​l​u​e​𝐯𝐰​∑l=0m(∑\mathcolor​N​a​v​y​B​l​u​e​𝐰′∈Vl,\mathcolor​N​a​v​y​B​l​u​e​𝟏​\mathcolor​N​a​v​y​B​l​u​e​𝐰′=\mathcolor​N​a​v​y​B​l​u​e​𝐰ℰT−t\mathcolor​N​a​v​y​B​l​u​e​𝐰′+σ22​∑\mathcolor​N​a​v​y​B​l​u​e​𝐰′∈Vl, 22​\mathcolor​N​a​v​y​B​l​u​e​𝐰′=\mathcolor​N​a​v​y​B​l​u​e​𝐰ℰT−t\mathcolor​N​a​v​y​B​l​u​e​𝐰′)\displaystyle=-\sum\_{m=0}^{M-n}\sum\_{{\mathcolor{NavyBlue}{\mathbf{w}}}\in V\_{m}}\xi^{{\mathcolor{NavyBlue}{\mathbf{vw}}}}\sum\_{l=0}^{m}\left(\sum\_{{\mathcolor{NavyBlue}{\mathbf{w}}}^{\prime}\in V\_{l},\penalty 10000\ {\mathcolor{NavyBlue}{\mathbf{1}}}{\mathcolor{NavyBlue}{\mathbf{w}}}^{\prime}={\mathcolor{NavyBlue}{\mathbf{w}}}}\mathcal{E}\_{T-t}^{{\mathcolor{NavyBlue}{\mathbf{w}}}^{\prime}}+\frac{\sigma^{2}}{2}\sum\_{{\mathcolor{NavyBlue}{\mathbf{w}}}^{\prime}\in V\_{l},\penalty 10000\ \mathbf{22}{\mathcolor{NavyBlue}{\mathbf{w}}}^{\prime}={\mathcolor{NavyBlue}{\mathbf{w}}}}\mathcal{E}\_{T-t}^{{\mathcolor{NavyBlue}{\mathbf{w}}}^{\prime}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑l=0M−n∑\mathcolor​N​a​v​y​B​l​u​e​𝐰∈Vl(ξ\mathcolor​N​a​v​y​B​l​u​e​𝐯𝟏𝐰+σ22​ξ\mathcolor​N​a​v​y​B​l​u​e​𝐯𝟐𝟐𝐰)​ℰT−t\mathcolor​N​a​v​y​B​l​u​e​𝐰\displaystyle=-\sum\_{l=0}^{M-n}\sum\_{{\mathcolor{NavyBlue}{\mathbf{w}}}\in V\_{l}}\left(\xi^{{\mathcolor{NavyBlue}{\mathbf{v1w}}}}+\frac{\sigma^{2}}{2}\xi^{{\mathcolor{NavyBlue}{\mathbf{v22w}}}}\right)\mathcal{E}\_{T-t}^{\mathcolor{NavyBlue}{\mathbf{w}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(ξt\mathcolor​N​a​v​y​B​l​u​e​𝐯𝟏+σ22​ξt\mathcolor​N​a​v​y​B​l​u​e​𝐯𝟐𝟐).\displaystyle=-\left(\xi\_{t}^{{\mathcolor{NavyBlue}{\mathbf{v1}}}}+\frac{\sigma^{2}}{2}\xi\_{t}^{\mathcolor{NavyBlue}{\mathbf{v22}}}\right). |  |

Therefore, we infer that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ˙t\displaystyle\dot{\xi}\_{t} | =∑n=0M∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vnξ˙t\mathcolor​N​a​v​y​B​l​u​e​𝐯​\mathcolor​N​a​v​y​B​l​u​e​𝐯=−∑n=0M∑\mathcolor​N​a​v​y​B​l​u​e​𝐯∈Vn(ξt\mathcolor​N​a​v​y​B​l​u​e​𝐯𝟏+σ22​ξt\mathcolor​N​a​v​y​B​l​u​e​𝐯𝟐𝟐)​\mathcolor​N​a​v​y​B​l​u​e​𝐯=−ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟏−σ22​ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐,\displaystyle=\sum\_{n=0}^{M}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\dot{\xi}\_{t}^{\mathcolor{NavyBlue}{\mathbf{v}}}{\mathcolor{NavyBlue}{\mathbf{v}}}=-\sum\_{n=0}^{M}\sum\_{{\mathcolor{NavyBlue}{\mathbf{v}}}\in V\_{n}}\left({\xi}\_{t}^{\mathcolor{NavyBlue}{\mathbf{v1}}}+\frac{\sigma^{2}}{2}\xi\_{t}^{\mathcolor{NavyBlue}{\mathbf{v22}}}\right){\mathcolor{NavyBlue}{\mathbf{v}}}=-\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}-\frac{\sigma^{2}}{2}\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}, |  |

which gives ([4.5](https://arxiv.org/html/2511.23295v1#S4.E5 "In Lemma 4.3. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
∎

## 5 Mean-quadratic variation hedging with market impact

Let us now consider the hedging problem of signature payoffs by assuming both temporary and permanent market impact as in ([2.3](https://arxiv.org/html/2511.23295v1#S2.E3 "In 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and ([2.4](https://arxiv.org/html/2511.23295v1#S2.E4 "In 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). In this case, the trader aims to optimally hedge a signature payoff given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | HTθ=⟨ξ,ℙ^Tθ⟩,H\_{T}^{\theta}=\left\langle\xi,\hat{\mathbb{P}}^{\theta}\_{T}\right\rangle, |  | (5.1) |

with ξ∈TM​(ℝ2)\xi\in T^{M}(\mathbb{R}^{2}), for some M>0M>0. Since we assume permanent price impact, the signature payoff ([5.1](https://arxiv.org/html/2511.23295v1#S5.E1 "In 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) depends now on the time-augmented signature of PθP^{\theta} given by ([2.3](https://arxiv.org/html/2511.23295v1#S2.E3 "In 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) instead of the time-augmented signature of SS (compare with ([4.1](https://arxiv.org/html/2511.23295v1#S4.E1 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions"))). In addition, the hedging strategy will be of finite variation in the form ([2.2](https://arxiv.org/html/2511.23295v1#S2.E2 "In 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), thanks to the regularizing effect of the temporary impact component with coefficient η>0\eta>0 present in ([2.4](https://arxiv.org/html/2511.23295v1#S2.E4 "In 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). In this frictional market, we follow Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)) and we assume that the trader’s P&L is marked to market using the Bachelier option price without friction such that the P&L at time t≤Tt\leq T resulting from the hedging strategy denoted by RtθR\_{t}^{\theta} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rtθ=(V0−X0​S0)+Xtθ​Ptθ−∫0tP~sθ​θs​𝑑s−⟨ξt,ℙ^tθ⟩,t≤T,R\_{t}^{\theta}=(V\_{0}-X\_{0}S\_{0})+X\_{t}^{\theta}P\_{t}^{\theta}-\int\_{0}^{t}\tilde{P}^{\theta}\_{s}\theta\_{s}ds-\langle\xi\_{t},\hat{\mathbb{P}}\_{t}^{\theta}\rangle,\penalty 10000\ t\leq T, |  | (5.2) |

with V0V\_{0} the initial value of the hedging portfolio composed of cash and holdings X0X\_{0} in the traded asset, and (ξt)t∈[0,T](\xi\_{t})\_{t\in[0,T]} defined by ([4.2](https://arxiv.org/html/2511.23295v1#S4.E2 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")). In particular,

|  |  |  |  |
| --- | --- | --- | --- |
|  | RTθ=(V0−X0​S0)+XTθ​PTθ−∫0TP~tθ​θt​𝑑t−HTθ.R\_{T}^{\theta}=(V\_{0}-X\_{0}S\_{0})+X\_{T}^{\theta}P\_{T}^{\theta}-\int\_{0}^{T}\tilde{P}^{\theta}\_{t}\theta\_{t}dt-H\_{T}^{\theta}. |  | (5.3) |

Moreover, we assume that the trader optimally hedges her short position using a mean-quadratic variation criteria in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | supθ∈𝒜𝔼​(RTθ−λ2​[Rθ,Rθ]T),\sup\_{\theta\in\mathcal{A}}\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right), |  | (5.4) |

with λ>0\lambda>0, the risk-aversion parameter, and 𝒜\mathcal{A} the set of admissible trading speed defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜:={θ:[0,T]×Ω→ℝ​prog. meas. process such that ​𝔼​(∫0Tθtp​𝑑t)<∞, for ​p:=2∨2​M~​𝟙{ν>0}},\mathcal{A}:=\left\{\theta:[0,T]\times\Omega\rightarrow\mathbb{R}\penalty 10000\ \text{prog. meas. process such that }\mathbb{E}\left(\int\_{0}^{T}\theta\_{t}^{p}dt\right)<\infty,\text{ for }p:=2\vee 2\tilde{M}\mathbb{1}\_{\{\nu>0\}}\right\}, |  | (5.5) |

M~\tilde{M} being the truncation order of ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}.

Using the optimal strategy from the frictionless market derived in Section [4](https://arxiv.org/html/2511.23295v1#S4 "4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we can rewrite the dynamic of RθR^{\theta} given by ([5.2](https://arxiv.org/html/2511.23295v1#S5.E2 "In 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), which facilitates the computation of its quadratic variation and simplifies the expression of the objective criterion.

###### Lemma 5.1.

Let (ξt)t∈[0,T](\xi\_{t})\_{t\in[0,T]} be defined by ([4.2](https://arxiv.org/html/2511.23295v1#S4.E2 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and θ∈𝒜\theta\in\mathcal{A}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | RTθ=(V0−ξ0ø)+∫0T(μ+ν​θt)​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)​𝑑t−∫0Tη​θt2​𝑑t+σ​∫0T(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)​𝑑Wt,R\_{T}^{\theta}=\left(V\_{0}-\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}\right)+\int\_{0}^{T}(\mu+\nu\theta\_{t})\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)dt-\int\_{0}^{T}\eta\theta\_{t}^{2}dt+\sigma\int\_{0}^{T}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)dW\_{t}, |  | (5.6) |

and its quadratic variation is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​([Rθ,Rθ]T)=σ2​𝔼​(∫0T(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2​𝑑t).\mathbb{E}\left([R^{\theta},R^{\theta}]\_{T}\right)=\sigma^{2}\mathbb{E}\left(\int\_{0}^{T}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2}dt\right). |  |

The stochastic control problem can be rewritten as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supθ∈𝒜𝔼​(RTθ−λ2​[Rθ,Rθ]T)=\displaystyle\sup\_{\theta\in\mathcal{A}}\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right)= | (V0−ξ0ø)+supθ∈𝒜[𝔼(∫0T(μ+νθt)(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)dt−∫0Tηθt2dt)\displaystyle\left(V\_{0}-\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}\right)+\sup\_{\theta\in\mathcal{A}}\bigg[\mathbb{E}\left(\int\_{0}^{T}(\mu+\nu\theta\_{t})\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)dt-\int\_{0}^{T}\eta\theta\_{t}^{2}dt\right) |  | (5.7) |
|  |  | −λ2σ2𝔼(∫0T(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2dt)].\displaystyle\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ -\frac{\lambda}{2}\sigma^{2}\mathbb{E}\bigg(\int\_{0}^{T}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2}dt\bigg)\bigg]. |  |

###### Proof.

An application of Itô formula in Theorem [3.4](https://arxiv.org/html/2511.23295v1#S3.Thmthm4 "Theorem 3.4 (Itô’s formula). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions") to ⟨ξt,ℙ^tθ⟩\langle\xi\_{t},\hat{\mathbb{P}}\_{t}^{\theta}\rangle and ([4.5](https://arxiv.org/html/2511.23295v1#S4.E5 "In Lemma 4.3. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) yields

|  |  |  |
| --- | --- | --- |
|  | HTθ=⟨ξT,ℙ^Tθ⟩=ξ0ø+∫0T(μ+ν​θt)​⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩​𝑑t+σ​∫0T⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩​𝑑Wt,\displaystyle H\_{T}^{\theta}=\left\langle\xi\_{T},\hat{\mathbb{P}}^{\theta}\_{T}\right\rangle=\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}+\int\_{0}^{T}(\mu+\nu\theta\_{t})\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle dt+\sigma\int\_{0}^{T}\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle dW\_{t}, |  |

with ξt\xi\_{t} defined by ([4.2](https://arxiv.org/html/2511.23295v1#S4.E2 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and thus, we can rewrite RTθR\_{T}^{\theta} in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | RTθ=\displaystyle R\_{T}^{\theta}= | V0+∫0T((μ+ν​θt)​Xtθ−η​θt2)​𝑑t+σ​∫0TXtθ​𝑑Wt−⟨ξT,ℙ^Tθ⟩\displaystyle V\_{0}+\int\_{0}^{T}\left((\mu+\nu\theta\_{t})X\_{t}^{\theta}-\eta\theta\_{t}^{2}\right)dt+\sigma\int\_{0}^{T}X\_{t}^{\theta}dW\_{t}-\left\langle\xi\_{T},\hat{\mathbb{P}}^{\theta}\_{T}\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (V0−ξ0ø)+∫0T(μ+ν​θt)​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)​𝑑t−∫0Tη​θt2​𝑑t+σ​∫0T(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)​𝑑Wt.\displaystyle\left(V\_{0}-\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}\right)+\int\_{0}^{T}(\mu+\nu\theta\_{t})\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)dt-\int\_{0}^{T}\eta\theta\_{t}^{2}dt+\sigma\int\_{0}^{T}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)dW\_{t}. |  |

The quadratic-variation of RθR^{\theta} follows from this representation.
∎

###### Remark 5.2.

From the reformulation of the stochastic control problem ([5.7](https://arxiv.org/html/2511.23295v1#S5.E7 "In Lemma 5.1. ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we see that the problem is not Linear-Quadratic, except for the case of ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐=Γ​ø\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}=\Gamma{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}, Γ∈ℝ\Gamma\in\mathbb{R}, which corresponds to the case of payoffs with constant Gamma as studied by Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)).
■\blacksquare

Before tackling the control problem ([5.4](https://arxiv.org/html/2511.23295v1#S5.E4 "In 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")),
it is worth first asking at what price the trader should sell the option in this market with frictions. Indeed, there is no reason for the trader to sell the option at the frictionless Bachelier price. We follow Guéant and Pu ([2017](https://arxiv.org/html/2511.23295v1#bib.bib25)) and consider an indifference pricing approach. More precisely, we assume that at time t=0−t=0^{-} (just before the deal), the trader only holds a cash position C∈ℝC\in\mathbb{R} and has no incentive to take a position on the risky asset. Then, the deal between the client and the trader is done as follows at t=0t=0:

* •

  the trader writes the option with payoff ⟨ξ,ℙ^Tθ⟩\langle\xi,\hat{\mathbb{P}}\_{T}^{\theta}\rangle and the client pays a price π\pi;
* •

  the client gives X0X\_{0} shares to the trader and receives X0​S0X\_{0}S\_{0} in cash from the trader.

As the trader considers a mean-quadratic variation criteria, the value she gives is the solution to the control problem ([5.4](https://arxiv.org/html/2511.23295v1#S5.E4 "In 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) with V0=C+πV\_{0}=C+\pi. Moreover, as at inception (before the deal), the trader only holds cash CC, her utility is simply CC. As a consequence, the trader is indifferent to make the deal if the price π\pi is such that

|  |  |  |
| --- | --- | --- |
|  | supθ∈𝒜𝔼​(RTθ−λ2​[Rθ,Rθ]T)=C,\sup\_{\theta\in\mathcal{A}}\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right)=C, |  |

where V0=C+πV\_{0}=C+\pi. Finally, using ([5.7](https://arxiv.org/html/2511.23295v1#S5.E7 "In Lemma 5.1. ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we deduce that the indifference price π\pi is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π\displaystyle\pi | =ξ0ø−supθ∈𝒜[𝔼(∫0T(μ+νθt)(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)dt−∫0Tηθt2dt)\displaystyle=\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}-\sup\_{\theta\in\mathcal{A}}\bigg[\mathbb{E}\left(\int\_{0}^{T}(\mu+\nu\theta\_{t})\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)dt-\int\_{0}^{T}\eta\theta\_{t}^{2}dt\right) |  | (5.8) |
|  |  | −λ2σ2𝔼(∫0T(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2dt)].\displaystyle\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ -\frac{\lambda}{2}\sigma^{2}\mathbb{E}\bigg(\int\_{0}^{T}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2}dt\bigg)\bigg]. |  |

The indifference price is composed of two terms: the frictionless Bachelier price ξ0ø\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}, and a spread that depends on market impact parameters, so that the indifference price π\pi includes the additional risk incurred by the trader due to market frictions. In particular, when μ=0\mu=0 and ν=0\nu=0, as in Guéant and Pu ([2017](https://arxiv.org/html/2511.23295v1#bib.bib25)), it follows from ([5.8](https://arxiv.org/html/2511.23295v1#S5.E8 "In 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) that π≥ξ0ø\pi\geq\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}} for all η≥0\eta\geq 0, with π=ξ0ø\pi=\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}} for η=0\eta=0. However, when μ>0\mu>0 or ν>0\nu>0, there is no reason why this inequality should hold in all cases, as the trader could exploit a signal or an arbitrage to maximize her risk-adjusted P&L, and therefore require an indifference price that could be lower than ξ0ø\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}.

### 5.1 Existence and uniqueness result

In this section, we study existence and uniqueness result of the stochastic control problem ([5.7](https://arxiv.org/html/2511.23295v1#S5.E7 "In Lemma 5.1. ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). We consider the functional J:𝒜→ℝJ:\mathcal{A}\to\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(θ):=𝔼​(∫0T[(μ+ν​θt)​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)−η​θt2−λ2​σ2​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2]​𝑑t),θ∈𝒜.J(\theta):=\mathbb{E}\left(\int\_{0}^{T}\left[(\mu+\nu\theta\_{t})\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)-\eta\theta\_{t}^{2}-\frac{\lambda}{2}\sigma^{2}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2}\right]dt\right),\quad\theta\in\mathcal{A}. |  | (5.9) |

Following ([5.7](https://arxiv.org/html/2511.23295v1#S5.E7 "In Lemma 5.1. ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), the stochastic control problem can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | supθ∈𝒜𝔼​(RTθ−λ2​[Rθ,Rθ]T)=supθ∈𝒜J​(θ)+(V0−ξ0ø).\sup\_{\theta\in\mathcal{A}}\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right)=\sup\_{\theta\in\mathcal{A}}J(\theta)+\left(V\_{0}-\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}\right). |  | (5.10) |

We are interested in studying the concavity of this functional JJ to deduce an existence and uniqueness result for the control problem. To this end, we define the inner product ⟨.,.⟩L2\langle.,.\rangle\_{L\_{2}} by

|  |  |  |
| --- | --- | --- |
|  | ⟨f,g⟩L2:=𝔼​(∫0Tft​gt​𝑑t),f,g∈𝒜.\langle f,g\rangle\_{L\_{2}}:=\mathbb{E}\left(\int\_{0}^{T}f\_{t}g\_{t}dt\right),\quad f,g\in\mathcal{A}. |  |

We first prove that JJ is Gâteaux differentiable. Then, we deduce an existence and uniqueness theorem under a monotonicity condition on the Gâteaux derivative of the functional JJ.

###### Lemma 5.3.

For any θ,ϕ,υ∈𝒜\theta,\phi,\upsilon\in\mathcal{A} and αt∈Tp​(ℝ2)\alpha\_{t}\in T^{p}(\mathbb{R}^{2}) with p=2∨2​M~​𝟙{ν>0}p=2\vee 2\tilde{M}\mathbb{1}\_{\{\nu>0\}}, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→01ε​𝔼​(υt​⟨αt,ℙ^tθ+ε​ϕ−ℙ^tθ⟩)=ν​∫0t𝔼​(ϕs​υt​⟨αt,ℙ^sθ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗ℙ^s,tθ⟩)​𝑑s,t≤T.\displaystyle\lim\_{\varepsilon\to 0}\frac{1}{\varepsilon}\mathbb{E}\left(\upsilon\_{t}\langle\alpha\_{t},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon\phi}-\hat{\mathbb{P}}\_{t}^{\theta}\rangle\right)=\nu\int\_{0}^{t}\mathbb{E}\left(\phi\_{s}\upsilon\_{t}\left\langle\alpha\_{t},\hat{\mathbb{P}}^{\theta}\_{s}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\otimes\hat{\mathbb{P}}\_{s,t}^{\theta}\right\rangle\right)ds,\quad t\leq T. |  | (5.11) |

###### Proof.

The proof is given in Section [7](https://arxiv.org/html/2511.23295v1#S7 "7 Proofs ‣ Signature approach for pricing and hedging path-dependent options with frictions").
∎

###### Lemma 5.4.

For any θ∈𝒜\theta\in\mathcal{A}, the functional JJ is Gâteaux differentiable. For any h∈𝒜h\in\mathcal{A},

|  |  |  |
| --- | --- | --- |
|  | limε→0J​(θ+ε​h)−J​(θ)ε=⟨∇J​(θ),h⟩L2,\displaystyle\lim\_{\varepsilon\to 0}\frac{J(\theta+\varepsilon h)-J(\theta)}{\varepsilon}=\langle\nabla J(\theta),h\rangle\_{L^{2}}, |  |

with the Gâteaux differential given by

|  |  |  |
| --- | --- | --- |
|  | ∇J​(θ)=−2​η​θ+ν​𝐀​θ−λ​σ2​𝐁​θ+μ​𝐂​θ,\nabla J(\theta)=-2\eta\theta+\nu\mathbf{A}\theta-\lambda\sigma^{2}\mathbf{B}\theta+\mu\mathbf{C}\theta, |  |

where the operators 𝐀:𝒜→𝒜\mathbf{A}:\mathcal{A}\rightarrow\mathcal{A}, 𝐁:𝒜→𝒜\mathbf{B}:\mathcal{A}\rightarrow\mathcal{A} and 𝐂:𝒜→𝒜\mathbf{C}:\mathcal{A}\rightarrow\mathcal{A} are defined, for θ∈𝒜\theta\in\mathcal{A}, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐀​θ)t=Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩+∫tT𝔼​(θs​(1−ν​Γt,sθ)|ℱt)​𝑑s,t≤T,\displaystyle(\mathbf{A}\theta)\_{t}=X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle+\int\_{t}^{T}\mathbb{E}\left(\theta\_{s}\left(1-\nu\Gamma\_{t,s}^{\theta}\right)|\mathcal{F}\_{t}\right)ds,\quad t\leq T, |  | (5.12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐁​θ)t=∫tT𝔼​(Xsθ​(1−ν​Γt,sθ)|ℱt)​𝑑s+∫tT𝔼​(12​ν​Γ~t,sθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩|ℱt)​𝑑s,t≤T,\displaystyle(\mathbf{B}\theta)\_{t}=\int\_{t}^{T}\mathbb{E}\left(X\_{s}^{\theta}\left(1-\nu\Gamma\_{t,s}^{\theta}\right)|\mathcal{F}\_{t}\right)ds+\int\_{t}^{T}\mathbb{E}\left(\frac{1}{2}\nu\tilde{\Gamma}\_{t,s}^{\theta}-\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{s}^{\theta}\rangle|\mathcal{F}\_{t}\right)ds,\quad t\leq T, |  | (5.13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐂​θ)t=(T−t)−∫tT𝔼​(ν​Γt,sθ|ℱt)​𝑑s,t≤T,\displaystyle(\mathbf{C}\theta)\_{t}=(T-t)-\int\_{t}^{T}\mathbb{E}(\nu\Gamma\_{t,s}^{\theta}|\mathcal{F}\_{t})ds,\quad t\leq T, |  | (5.14) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γt,sθ\displaystyle\Gamma\_{t,s}^{\theta} | :=⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗ℙ^t,sθ⟩,Γ~t,sθ:=⟨(ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2,ℙ^tθ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗ℙ^t,sθ⟩,t<s≤T.\displaystyle:=\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\otimes\hat{\mathbb{P}}\_{t,s}^{\theta}\right\rangle,\quad\tilde{\Gamma}\_{t,s}^{\theta}:=\left\langle\left(\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2},\hat{\mathbb{P}}^{\theta}\_{t}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\otimes\hat{\mathbb{P}}\_{t,s}^{\theta}\right\rangle,\quad t<s\leq T. |  |

###### Proof.

The proof is given in Section [7](https://arxiv.org/html/2511.23295v1#S7 "7 Proofs ‣ Signature approach for pricing and hedging path-dependent options with frictions").
∎

We are now ready to prove the existence and uniqueness result. To this end, we use general results of convex optimization in infinite dimensional spaces and we show that under suitable monotonicity conditions, the functional JJ is strongly concave. We recall that, given a positive constant β>0\beta>0, a map 𝒯:𝒜→ℝ\mathcal{T}:\mathcal{A}\to\mathbb{R} is β−\beta-strongly concave if, for every θ,ϕ∈𝒜\theta,\phi\in\mathcal{A}, the following inequality holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯​(α​θ+(1−α)​ϕ)≥α​𝒯​(θ)+(1−α)​𝒯​(ϕ)+β​α​(1−α)2​‖θ−ϕ‖𝒜2,α∈[0,1],\displaystyle\mathcal{T}\left(\alpha\theta+(1-\alpha)\phi\right)\geq\alpha\mathcal{T}(\theta)+(1-\alpha)\mathcal{T}(\phi)+\frac{\beta\alpha(1-\alpha)}{2}||\theta-\phi||\_{\mathcal{A}}^{2},\penalty 10000\ \alpha\in[0,1], |  | (5.15) |

with ‖θ‖𝒜:=𝔼​(∫0Tθsp​𝑑s)1/p||\theta||\_{\mathcal{A}}:=\mathbb{E}\left(\int\_{0}^{T}\theta\_{s}^{p}ds\right)^{1/p}, p:=2∨2​M~​𝟙{ν>0}p:=2\vee 2\tilde{M}\mathbb{1}\_{\{\nu>0\}}.

###### Theorem 5.5.

For a given ε>0\varepsilon>0, assume that the operators 𝐀,\mathbf{A}, 𝐁\mathbf{B} and 𝐂\mathbf{C}, defined by ([5.12](https://arxiv.org/html/2511.23295v1#S5.E12 "In Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), ([5.13](https://arxiv.org/html/2511.23295v1#S5.E13 "In Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and ([5.14](https://arxiv.org/html/2511.23295v1#S5.E14 "In Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), satisfy the following monotonicity condition, for θ,ϕ∈𝒜,\theta,\phi\in\mathcal{A},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⟨−2η(θ−ϕ)+ε(||θ||𝒜2−pθp−1−||ϕ||𝒜2−pϕp−1)+ν(𝐀(θ)−𝐀(ϕ))−λσ2(𝐁(θ)−𝐁(ϕ))\displaystyle\bigg\langle-2\eta(\theta-\phi)+\varepsilon\left(||\theta||\_{\mathcal{A}}^{2-p}\theta^{p-1}-||\phi||\_{\mathcal{A}}^{2-p}\phi^{p-1}\right)+\nu\left(\mathbf{A}(\theta)-\mathbf{A}(\phi)\right)-\lambda\sigma^{2}\left(\mathbf{B}(\theta)-\mathbf{B}(\phi)\right) |  | (5.16) |
|  |  | +μ(𝐂(θ)−𝐂(ϕ)),θ−ϕ⟩L2≤0.\displaystyle+\mu\left(\mathbf{C}(\theta)-\mathbf{C}(\phi)\right),\theta-\phi\bigg\rangle\_{L\_{2}}\leq 0. |  |

Then, JJ is ε\varepsilon-strongly concave in the sense of ([5.15](https://arxiv.org/html/2511.23295v1#S5.E15 "In 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), and there exists a unique admissible optimal control θ∗∈𝒜\theta^{\*}\in\mathcal{A} satisfying ([5.10](https://arxiv.org/html/2511.23295v1#S5.E10 "In 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), which is also the unique solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇J​(θ∗)=0.\displaystyle\nabla J(\theta^{\*})=0. |  | (5.17) |

###### Proof.

The proof of the theorem statements are consequences of well-known results of convex analysis in Banach spaces that can be found in Ekeland and Temam ([1999](https://arxiv.org/html/2511.23295v1#bib.bib21)). First, let us prove that JJ is ε−\varepsilon-strongly concave. To this end, we define the functional J~\tilde{J} by

|  |  |  |
| --- | --- | --- |
|  | J~​(θ):=−J​(θ)−ε2​‖θ‖𝒜2.\displaystyle\tilde{J}(\theta):=-J(\theta)-\frac{\varepsilon}{2}||\theta||\_{\mathcal{A}}^{2}. |  |

If we now prove that J~\tilde{J} is convex then, we deduce that JJ is ε−\varepsilon-strongly concave. By Lemma [5.4](https://arxiv.org/html/2511.23295v1#S5.Thmthm4 "Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we know that JJ is Gâteaux differentiable, therefore J~\tilde{J} is also Gâteaux differentiable. In this case, (Ekeland and Temam, [1999](https://arxiv.org/html/2511.23295v1#bib.bib21), Proposition 5.5. of Chapter I) gives an equivalence between the convexity of J~\tilde{J} and the monotonicity of the Gâteaux differential ∇J~​(θ)\nabla\tilde{J}(\theta) defined as

|  |  |  |
| --- | --- | --- |
|  | ⟨∇J~​(θ),h⟩L2=limε→0J~​(θ+ε​h)−J~​(θ)ε,h∈𝒜.\left\langle\nabla\tilde{J}(\theta),h\right\rangle\_{L\_{2}}=\lim\_{\varepsilon\to 0}\frac{\tilde{J}(\theta+\varepsilon h)-\tilde{J}(\theta)}{\varepsilon},\penalty 10000\ h\in\mathcal{A}. |  |

In fact, J~\tilde{J} is convex if, for θ,ϕ∈𝒜\theta,\phi\in\mathcal{A},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨∇J~​(θ)−∇J~​(ϕ),θ−ϕ⟩L2≥0.\displaystyle\left\langle\nabla\tilde{J}(\theta)-\nabla\tilde{J}(\phi),\theta-\phi\right\rangle\_{L\_{2}}\geq 0. |  | (5.18) |

Using Lemma [5.4](https://arxiv.org/html/2511.23295v1#S5.Thmthm4 "Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"), under our monotonicity assumption given by ([5.16](https://arxiv.org/html/2511.23295v1#S5.E16 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we deduce that ([5.18](https://arxiv.org/html/2511.23295v1#S5.E18 "In 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied, and therefore, we obtain that J~\tilde{J} is convex as well as JJ is ε−\varepsilon-strongly concave. As we prove that JJ is ε−\varepsilon-strongly concave, we have that JJ is strictly concave and coercive, thus by relying on (Ekeland and Temam, [1999](https://arxiv.org/html/2511.23295v1#bib.bib21), Proposition 1.2. of Chapter II), we immediately have that there exists a unique admissible optimal control θ∗∈𝒜\theta^{\*}\in\mathcal{A} satisfying ([5.10](https://arxiv.org/html/2511.23295v1#S5.E10 "In 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Finally, since JJ is Gâteaux differentiable, from (Ekeland and Temam, [1999](https://arxiv.org/html/2511.23295v1#bib.bib21), Proposition 2.1. of Chapter II), we know that the set of optimal strategies satisfying ([5.10](https://arxiv.org/html/2511.23295v1#S5.E10 "In 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) coincides with the set of solutions to ([5.17](https://arxiv.org/html/2511.23295v1#S5.E17 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and therefore, we deduce that the unique optimal control θ∗∈𝒜\theta^{\*}\in\mathcal{A}, is also the unique solution of ([5.17](https://arxiv.org/html/2511.23295v1#S5.E17 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
∎

###### Proposition 5.6.

If ν=0\nu=0, then the monotonicity condition ([5.16](https://arxiv.org/html/2511.23295v1#S5.E16 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied.

###### Proof.

The proof is given in Section [7](https://arxiv.org/html/2511.23295v1#S7 "7 Proofs ‣ Signature approach for pricing and hedging path-dependent options with frictions").
∎

###### Proposition 5.7.

Let us consider that ν>0\nu>0 and for all t≤Tt\leq T, ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐∈T≤1​(ℝ2)\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\in T^{\leq 1}(\mathbb{R}^{2}). Moreover, let us assume that, for a given 0<ε<2​η0<\varepsilon<2\eta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1ν​(1−2​η−εT​ν)≤ξt\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐≤1ν,t≤T.\frac{1}{\nu}\left(1-\frac{2\eta-\varepsilon}{T\nu}\right)\leq\xi\_{t}^{{\mathcolor{NavyBlue}{\mathbf{22}}}}\leq\frac{1}{\nu},\quad t\leq T. |  | (5.19) |

Then, the monotonicity condition ([5.16](https://arxiv.org/html/2511.23295v1#S5.E16 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied.

###### Proof.

The proof is given in Section [7](https://arxiv.org/html/2511.23295v1#S7 "7 Proofs ‣ Signature approach for pricing and hedging path-dependent options with frictions").
∎

###### Remark 5.8.

The class of payoffs concerned by Proposition [5.7](https://arxiv.org/html/2511.23295v1#S5.Thmthm7 "Proposition 5.7. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") (i.e. ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐∈T≤1​(ℝ2)\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\in T^{\leq 1}(\mathbb{R}^{2})) includes all signature payoffs with ξ∈T≤2​(ℝ2)\xi\in T^{\leq 2}(\mathbb{R}^{2}), but also some signature payoffs with ξ∈T>2​(ℝ2)\xi\in T^{>2}(\mathbb{R}^{2}) such as, for example, Asian quadratic payoffs.
■\blacksquare

Theorem [5.5](https://arxiv.org/html/2511.23295v1#S5.Thmthm5 "Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") gives a general existence and uniqueness result, and characterizes the optimal control through the first order condition ([5.17](https://arxiv.org/html/2511.23295v1#S5.E17 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). However, this is intricate to deduce the optimal control using this condition. In the next section, we provide a more tractable verification result to derive the optimal control.

### 5.2 Verification result using infinite-dimensional Riccati equations

In this section, we consider a verification result for the stochastic control problem. We first give a general verification theorem such that, under given assumptions, including the existence of a solution to an infinite-dimensional system of Riccati equations, the optimal control associated with the mean-quadratic variation hedging problem can be written in a feedback form, as a linear combination of elements of the signature with time-dependent coefficients. Then, we provide two examples for which the assumptions of the verification theorem are satisfied and for which we have an explicit solution to the system of infinite-dimensional Riccati equations.

#### 5.2.1 General verification theorem

The following theorem provides a verification result, with a semi-explicit solution for the mean-quadratic variation hedging problem of signature payoffs when the trader incurs both temporary and permanent market impact, in terms of the infinite-dimensional system of Riccati equations on the extended tensor algebra space T​((ℝ3))T((\mathbb{R}^{3})):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝝍t˙=−𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟏−12​σ2​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐−λ2​σ2​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)⊔⁣⊔2+14​η​[ν​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)−(ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)]⊔⁣⊔2\displaystyle\dot{\bm{\psi}\_{t}}=-\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}-\frac{1}{2}\sigma^{2}\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}-\frac{\lambda}{2}\sigma^{2}({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\frac{1}{4\eta}\bigg[\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})\bigg]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2} |  | (5.20) |
|  |  | +μ​[(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)−𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐],\displaystyle\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ +\mu\left[({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right], |  |
|  |  | 𝝍T=0,\displaystyle\bm{\psi}\_{T}=0, |  |

where ξ~t\tilde{\xi}\_{t} is defined, for all 𝐰=\mathcolor​N​a​v​y​B​l​u​e​𝐢𝟏​…​\mathcolor​N​a​v​y​B​l​u​e​𝐢𝐧\mathbf{w}={\mathcolor{NavyBlue}{\mathbf{i\_{1}}}}...{\mathcolor{NavyBlue}{\mathbf{i\_{n}}}} with n∈ℕn\in\mathbb{N}, by

|  |  |  |
| --- | --- | --- |
|  | ξ~t\mathcolor​N​a​v​y​B​l​u​e​𝐰:={0,if​∃k∈{1,…,n}​such that​\mathcolor​N​a​v​y​B​l​u​e​𝐢𝐤=\mathcolor​N​a​v​y​B​l​u​e​𝟑,(ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐)\mathcolor​N​a​v​y​B​l​u​e​𝐰,if​∄​k∈{1,…,n}​such that​\mathcolor​N​a​v​y​B​l​u​e​𝐢𝐤=\mathcolor​N​a​v​y​B​l​u​e​𝟑,\tilde{\xi}\_{t}^{{\mathcolor{NavyBlue}{\mathbf{w}}}}:=\begin{cases}0,&\text{if}\penalty 10000\ \exists k\in\{1,...,n\}\penalty 10000\ \text{such that}\penalty 10000\ {\mathcolor{NavyBlue}{\mathbf{i\_{k}}}}={\mathcolor{NavyBlue}{\mathbf{3}}},\\ \left(\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right)^{{\mathcolor{NavyBlue}{\mathbf{w}}}},&\text{if}\penalty 10000\ \nexists k\in\{1,...,n\}\penalty 10000\ \text{such that}\penalty 10000\ {\mathcolor{NavyBlue}{\mathbf{i\_{k}}}}={\mathcolor{NavyBlue}{\mathbf{3}}},\end{cases} |  |

with ξt\xi\_{t} given by ([4.2](https://arxiv.org/html/2511.23295v1#S4.E2 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")).

###### Theorem 5.9.

Let us define Z^tθ:=(t,Ptθ,Xtθ)\hat{Z}\_{t}^{\theta}:=(t,P\_{t}^{\theta},X\_{t}^{\theta}) and suppose that there exists (𝛙t)t∈[0,T](\bm{\psi}\_{t})\_{t\in[0,T]} solution of the following infinite-dimensional system of Riccati equations ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Moreover, let us assume that, for all θ∈𝒜\theta\in\mathcal{A}, (𝛙t)t∈[0,T]∈ℐ′​(ℤ^θ)(\bm{\psi}\_{t})\_{t\in[0,T]}\in\mathcal{I}^{{}^{\prime}}(\hat{\mathbb{Z}}^{\theta}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(∫0T⟨ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℤ^tθ⟩2​𝑑t)<∞,\mathbb{E}\left(\int\_{0}^{T}\langle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\rangle^{2}dt\right)<\infty, |  | (5.21) |

and that there exists θ∗∈𝒜\theta^{\*}\in\mathcal{A} satisfying the feedback equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | θt∗=12​η​[ν​(Xtθ∗−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ∗⟩)−⟨ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℤ^tθ∗⟩].\displaystyle\theta\_{t}^{\*}=\frac{1}{2\eta}\left[\nu\left(X\_{t}^{\theta^{\*}}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta^{\*}}\_{t}\right\rangle\right)-\left\langle\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}},\hat{\mathbb{Z}}\_{t}^{\theta^{\*}}\right\rangle\right]. |  | (5.22) |

Then, the value of the mean-quadratic variation hedging problem is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | supθ∈𝒜𝔼​(RTθ−λ2​[Rθ,Rθ]T)=(V0−ξ0ø)−𝝍0ø,\displaystyle\sup\_{\theta\in\mathcal{A}}\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right)=\left(V\_{0}-\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}\right)-\bm{\psi}\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}, |  | (5.23) |

and the optimum is attained for θ∗\theta^{\*}.

###### Proof.

Assume that there exists (𝝍t)t∈[0,T]∈ℐ′​(ℤ^θ)(\bm{\psi}\_{t})\_{t\in[0,T]}\in\mathcal{I}^{{}^{\prime}}(\hat{\mathbb{Z}}^{\theta}) solution of the infinite-dimensional system of Riccati equations ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and define, for any θ∈𝒜\theta\in\mathcal{A}, the process (Utθ)t∈[0,T](U\_{t}^{\theta})\_{t\in[0,T]} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Utθ=∫0t[(μ+ν​θs)​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)−η​θs2−λ2​σ2​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)2]​𝑑s−⟨𝝍t,ℤ^tθ⟩,t≤T.U\_{t}^{\theta}=\int\_{0}^{t}\left[(\mu+\nu\theta\_{s})\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)-\eta\theta\_{s}^{2}-\frac{\lambda}{2}\sigma^{2}\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)^{2}\right]ds-\left\langle\bm{\psi}\_{t},\hat{\mathbb{Z}}^{\theta}\_{t}\right\rangle,\penalty 10000\ t\leq T. |  | (5.24) |

Since, ψ∈ℐ′​(ℤ^tθ)\psi\in\mathcal{I}^{\prime}(\hat{\mathbb{Z}}\_{t}^{\theta}), an application of Ito’s lemma in Theorem [3.4](https://arxiv.org/html/2511.23295v1#S3.Thmthm4 "Theorem 3.4 (Itô’s formula). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions") leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Utθ=\displaystyle dU\_{t}^{\theta}= | [(μ+ν​θt)​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)−η​θt2−λ2​σ2​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2]​d​t−d​⟨𝝍t,ℤ^tθ⟩\displaystyle\bigg[(\mu+\nu\theta\_{t})\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)-\eta\theta\_{t}^{2}-\frac{\lambda}{2}\sigma^{2}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2}\bigg]dt-d\left\langle\bm{\psi}\_{t},\hat{\mathbb{Z}}^{\theta}\_{t}\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | [νθt(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)−ηθt2−λ2σ2(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2\displaystyle\bigg[\nu\theta\_{t}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)-\eta\theta\_{t}^{2}-\frac{\lambda}{2}\sigma^{2}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −⟨𝝍˙t+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟏+μ𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+θt(ν𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)+12σ2𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐,ℤ^tθ⟩]dt\displaystyle-\left\langle\dot{\bm{\psi}}\_{t}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}+\mu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\theta\_{t}(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})+\frac{1}{2}\sigma^{2}\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle\bigg]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −σ​⟨𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℤ^tθ⟩​d​Wt.\displaystyle-\sigma\left\langle\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle dW\_{t}. |  |

By a square completion, we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Utθ=\displaystyle dU\_{t}^{\theta}= | [−η(θt−12​η[ν(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)−⟨ν𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℤ^tθ⟩])2\displaystyle\bigg[-\eta\left(\theta\_{t}-\frac{1}{2\eta}\left[\nu\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)-\left\langle\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle\right]\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +14​η​(ν​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)−⟨ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℤ^tθ⟩)2\displaystyle+\frac{1}{4\eta}\left(\nu\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)-\left\langle\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −λ2​σ2​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2−⟨𝝍˙t+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟏+μ​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+12​σ2​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐,ℤ^tθ⟩\displaystyle-\frac{\lambda}{2}\sigma^{2}\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2}-\left\langle\dot{\bm{\psi}}\_{t}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}+\mu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\frac{1}{2}\sigma^{2}\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +μ(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)]dt−σ⟨𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℤ^tθ⟩dWt.\displaystyle+\mu\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)\bigg]dt-\sigma\left\langle\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle dW\_{t}. |  |

As, for t≤Tt\leq T, ξ~t∈𝒜​(ℤ^θ)\tilde{\xi}\_{t}\in\mathcal{A}{(\hat{\mathbb{Z}}^{\theta})} and (ν​ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐+ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟑)∈𝒜​(ℤ^θ)\left(\nu\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}}\right)\in\mathcal{A}{(\hat{\mathbb{Z}}^{\theta})}, since ξ~∈ℐ′​(ℤ^θ)\tilde{\xi}\in\mathcal{I}^{\prime}(\hat{\mathbb{Z}}^{\theta}) and ψ∈ℐ′​(ℤ^θ)\psi\in\mathcal{I}^{\prime}(\hat{\mathbb{Z}}^{\theta}), using the shuffle property of Proposition [3.3](https://arxiv.org/html/2511.23295v1#S3.Thmthm3 "Proposition 3.3 (Shuffle property). ‣ 3.3 Infinite linear combinations of signature elements ‣ 3 Reminder on signatures ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we deduce that

|  |  |  |
| --- | --- | --- |
|  | (Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)2=⟨(𝟑+ø​X0−ξ~t)⊔⁣⊔2,ℤ^tθ⟩,\displaystyle\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)^{2}=\left\langle\left(\mathbf{3}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle, |  |

and

|  |  |  |
| --- | --- | --- |
|  | (ν​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)−⟨ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℤ^tθ⟩)2=⟨(ν​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)−(ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑))⊔⁣⊔2,ℤ^tθ⟩.\displaystyle\left(\nu\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)-\left\langle\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle\right)^{2}=\left\langle\left(\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle. |  |

Moreover, using the Riccati equation ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) satisfied by 𝝍t\bm{\psi}\_{t}, we get that

|  |  |  |
| --- | --- | --- |
|  | d​Utθ=−η​(θt−𝒯t​(θ))2​d​t−σ​⟨𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℤ^tθ⟩​d​Wt,\displaystyle dU\_{t}^{\theta}=-\eta(\theta\_{t}-\mathcal{T}\_{t}(\theta))^{2}dt-\sigma\left\langle\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle dW\_{t}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | 𝒯t​(θ):=12​η​[ν​(Xtθ−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)−⟨ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℤ^tθ⟩].\mathcal{T}\_{t}(\theta):=\frac{1}{2\eta}\left[\nu\left(X\_{t}^{\theta}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\right\rangle\right)-\left\langle\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\right\rangle\right]. |  |

Let us now define (Mtθ)t∈[0,T](M\_{t}^{\theta})\_{t\in[0,T]} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mtθ:=\displaystyle M\_{t}^{\theta}:= | Utθ+η​∫0t(θs−𝒯s​(θ))2​𝑑s=−⟨𝝍0,ℤ^0θ⟩−σ​∫0t⟨𝝍s|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℤ^sθ⟩​𝑑Ws.\displaystyle U\_{t}^{\theta}+\eta\int\_{0}^{t}(\theta\_{s}-\mathcal{T}\_{s}(\theta))^{2}ds=-\left\langle\bm{\psi}\_{0},\hat{\mathbb{Z}}^{\theta}\_{0}\right\rangle-\sigma\int\_{0}^{t}\left\langle\bm{\psi}\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{Z}}^{\theta}\_{s}\right\rangle dW\_{s}. |  |

Since we assume ([5.21](https://arxiv.org/html/2511.23295v1#S5.E21 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we have that (Mtθ)t∈[0,T](M\_{t}^{\theta})\_{t\in[0,T]} is a true martingale. In this case, since 𝔼​(MTθ|ℱt)=Mtθ\mathbb{E}(M\_{T}^{\theta}|\mathcal{F}\_{t})=M\_{t}^{\theta} and ⟨𝝍T,ℤ^Tθ⟩=0\left\langle\bm{\psi}\_{T},\hat{\mathbb{Z}}^{\theta}\_{T}\right\rangle=0, we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝝍t,ℤ^tθ⟩=\displaystyle\left\langle\bm{\psi}\_{t},\hat{\mathbb{Z}}^{\theta}\_{t}\right\rangle= | −𝔼​(MTθ|ℱt)+∫0t[ν​θs​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)−η​θs2−λ2​σ2​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)2]​𝑑s\displaystyle-\mathbb{E}(M\_{T}^{\theta}|\mathcal{F}\_{t})+\int\_{0}^{t}\left[\nu\theta\_{s}\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)-\eta\theta\_{s}^{2}-\frac{\lambda}{2}\sigma^{2}\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)^{2}\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +η​∫0t(θs−𝒯s​(θ))2​𝑑s.\displaystyle+\eta\int\_{0}^{t}(\theta\_{s}-\mathcal{T}\_{s}(\theta))^{2}ds. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −𝔼​(∫tT[ν​θs​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)−η​θs2−λ2​σ2​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)2]​𝑑s|ℱt)\displaystyle-\mathbb{E}\left(\int\_{t}^{T}\left[\nu\theta\_{s}\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)-\eta\theta\_{s}^{2}-\frac{\lambda}{2}\sigma^{2}\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)^{2}\right]ds\bigg|\mathcal{F}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −η​𝔼​(∫tT(θs−𝒯s​(θ))2​𝑑s|ℱt).\displaystyle-\eta\mathbb{E}\left(\int\_{t}^{T}(\theta\_{s}-\mathcal{T}\_{s}(\theta))^{2}ds\bigg|\mathcal{F}\_{t}\right). |  |

By defining Jt​(θ)J\_{t}(\theta) as

|  |  |  |
| --- | --- | --- |
|  | Jt​(θ):=𝔼​(∫tT[ν​θs​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)−η​θs2−λ2​σ2​(Xsθ−⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩)2]​𝑑s|ℱt),\displaystyle J\_{t}(\theta):=\mathbb{E}\left(\int\_{t}^{T}\left[\nu\theta\_{s}\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)-\eta\theta\_{s}^{2}-\frac{\lambda}{2}\sigma^{2}\left(X\_{s}^{\theta}-\left\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{s}\right\rangle\right)^{2}\right]ds\bigg|\mathcal{F}\_{t}\right), |  |

we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt​(θ)+⟨𝝍t,ℤ^tθ⟩=−η​𝔼​(∫tT(θs−𝒯s​(θ))2​𝑑s|ℱt).\displaystyle J\_{t}(\theta)+\left\langle\bm{\psi}\_{t},\hat{\mathbb{Z}}^{\theta}\_{t}\right\rangle=-\eta\mathbb{E}\left(\int\_{t}^{T}(\theta\_{s}-\mathcal{T}\_{s}(\theta))^{2}ds\bigg|\mathcal{F}\_{t}\right). |  | (5.25) |

We observe that the right hand side of ([5.25](https://arxiv.org/html/2511.23295v1#S5.E25 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is always nonpositive and vanishes for θt=𝒯t​(θ)\theta\_{t}=\mathcal{T}\_{t}(\theta), i.e. θt=θt∗\theta\_{t}=\theta\_{t}^{\*} with θt∗\theta\_{t}^{\*} given by ([5.22](https://arxiv.org/html/2511.23295v1#S5.E22 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). As we assume that there exists an admissible control process θ∗∈𝒜\theta^{\*}\in\mathcal{A} such that ([5.22](https://arxiv.org/html/2511.23295v1#S5.E22 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) holds, then the proof is complete. In fact, in this case, for fixed t≤Tt\leq T, we have that, ⟨𝝍t,ℤ^tθ∗⟩=⟨𝝍t,ℤ^tθ′⟩\left\langle\bm{\psi}\_{t},\hat{\mathbb{Z}}^{\theta^{\*}}\_{t}\right\rangle=\left\langle\bm{\psi}\_{t},\hat{\mathbb{Z}}^{\theta^{{}^{\prime}}}\_{t}\right\rangle, for all θ′∈𝒜t​(θ∗):={θ∈𝒜:θs=θs∗,for​s≤t}\theta^{{}^{\prime}}\in\mathcal{A}\_{t}(\theta^{\*}):=\left\{\theta\in\mathcal{A}:\theta\_{s}=\theta\_{s}^{\*},\penalty 10000\ \text{for}\penalty 10000\ s\leq t\right\}.
Therefore, from ([5.25](https://arxiv.org/html/2511.23295v1#S5.E25 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we deduce that

|  |  |  |
| --- | --- | --- |
|  | supθ∈𝒜t​(θ∗)Jt​(θ)=Jt​(θ∗)=−⟨𝝍t,ℤ^tθ∗⟩,\sup\_{\theta\in\mathcal{A}\_{t}(\theta^{\*})}J\_{t}(\theta)=J\_{t}(\theta^{\*})=-\left\langle\bm{\psi}\_{t},\hat{\mathbb{Z}}^{\theta^{\*}}\_{t}\right\rangle, |  |

which shows that θ∗\theta^{\*} is an optimal control. In particular, for t=0t=0, we have that

|  |  |  |
| --- | --- | --- |
|  | supθ∈𝒜J0​(θ)=J0​(θ∗)=−𝝍0ø,\displaystyle\sup\_{\theta\in\mathcal{A}}J\_{0}(\theta)=J\_{0}(\theta^{\*})=-\bm{\psi}\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}, |  |

and as

|  |  |  |
| --- | --- | --- |
|  | supθ∈𝒜𝔼​(RTθ−λ2​[Rθ,Rθ]T)=(V0−⟨ξ0,ℙ^0θ⟩)+supθ∈𝒜J0​(θ),\displaystyle\sup\_{\theta\in\mathcal{A}}\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right)=\left(V\_{0}-\left\langle\xi\_{0},\hat{\mathbb{P}}^{\theta}\_{0}\right\rangle\right)+\sup\_{\theta\in\mathcal{A}}J\_{0}(\theta), |  |

we finally obtain ([5.23](https://arxiv.org/html/2511.23295v1#S5.E23 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
∎

###### Remark 5.10 (Interpretation of θ∗\theta^{\*}).

θ∗\theta^{\*} has a feedback form in ℤ^tθ∗\hat{\mathbb{Z}}\_{t}^{\theta^{\*}} that can be decomposed into two terms:

* •

  The first term 12​η​ν​(Xtθ∗−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ∗⟩)\frac{1}{2\eta}\nu\left(X\_{t}^{\theta^{\*}}-\left\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta^{\*}}\_{t}\right\rangle\right) corresponds to an arbitrage opportunity. Since P&L is marked-to-market, when ν>0\nu>0, the trader benefits from pushing the price upward by buying more, when her inventory XtθX\_{t}^{\theta} is larger than the the perfect hedging strategy ⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{t}\rangle. Similarly, she benefits from pushing the price downward by selling if it is smaller. This can be clearly seen by examining the expression of RTθR\_{T}^{\theta} given by ([5.6](https://arxiv.org/html/2511.23295v1#S5.E6 "In Lemma 5.1. ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). When ν>0\nu>0, the trader can deliberately move the market to make her current position more valuable.
* •

  The second term −12​η​⟨ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℤ^tθ∗⟩-\frac{1}{2\eta}\left\langle\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}},\hat{\mathbb{Z}}\_{t}^{\theta^{\*}}\right\rangle expresses the trader’s incentive to adjust both her inventory XθX^{\theta} and, when ν>0\nu>0, the public traded price PθP^{\theta} in the direction that increases her utility at time t<Tt<T.

■\blacksquare

###### Remark 5.11.

Assumptions of Theorem [5.9](https://arxiv.org/html/2511.23295v1#S5.Thmthm9 "Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") are intricate to prove in general, especially concerning the existence of a solution to the infinite-dimensional system of Riccati equations. Nevertheless, in the next section, we provide two concrete examples for which the existence of an explicit solution to the infinite-dimensional system of Riccati equations can be established.
■\blacksquare

###### Remark 5.12 (Polynomial payoffs).

If ξ=(\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗m)m=0,…​M\xi=\left({\mathcolor{NavyBlue}{\mathbf{2}}}^{\otimes m}\right)\_{m=0,...M}, then we can show that the infinite-dimensional system of Riccati equations reduces to ([2.8](https://arxiv.org/html/2511.23295v1#S2.E8 "In 2.2 Key observation for Markovian polynomial payoffs ‣ 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
■\blacksquare

###### Remark 5.13 (Numerical implementation).

Care should be taken regarding the numerical resolution of the system of Riccati equations and the choice of the truncation order associated to ψ\psi. In fact, the shuffle product ⊔⁣⊔\mathrel{\sqcup\mkern-3.2mu\sqcup} cannot be exact since at each discretization steps of the ODE, it will double the truncation order of 𝝍\bm{\psi}. If we assume that ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐∈TM~​(ℝ2)\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\in T^{\tilde{M}}(\mathbb{R}^{2}), then, as in Abi Jaber and Gérard ([2025a](https://arxiv.org/html/2511.23295v1#bib.bib1)), we decide to fix, at each step, the truncation order of ψ\psi to 2​M~2\tilde{M}, and to consider the shuffle product projected on T2​M~​(ℝ3)T^{2\tilde{M}}(\mathbb{R}^{3}) defined as ⊔⁣⊔~:(T2​M~​(ℝ3))2→T2​M~​(ℝ3)\widetilde{\mathrel{\sqcup\mkern-3.2mu\sqcup}}:(T^{2\tilde{M}}(\mathbb{R}^{3}))^{2}\to T^{2\tilde{M}}(\mathbb{R}^{3}). Hence, given ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐∈TM~​(ℝ2)\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\in T^{\tilde{M}}(\mathbb{R}^{2}), ψ\psi is an element of T2​M~​(ℝ3)T^{2\tilde{M}}(\mathbb{R}^{3}). We refer to (Abi Jaber and Gérard, [2025a](https://arxiv.org/html/2511.23295v1#bib.bib1), Section 5.1.) for a more in-depth discussion, and an analysis of the quality of convergence given different truncation orders for 𝝍\bm{\psi}.
■\blacksquare

#### 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples

We now consider two examples for which the infinite-dimensional system of Riccati equations admits an explicit solution and for which the assumptions of the verification theorem are satisfied. The first example is the case without permanent impact i.e. ν=0\nu=0. In this case, we fall back into the Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)) framework, so it is not surprising to obtain an existence result for the system of Riccati equations. The second example is the case where we restrict ourselves to European quadratic payoff such that ξ=Γ​\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐\xi=\Gamma{\mathcolor{NavyBlue}{\mathbf{22}}} with Γ∈ℝ\Gamma\in\mathbb{R}, and we retrieve the result of Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)). Furthermore, for both examples, we also deduce the explicit form of the optimal trading speed θ∗\theta^{\*}.

Before discussing the two examples, we consider a lemma that gives us a sufficient condition for the existence and admissibility of θ∗\theta^{\*}.

###### Lemma 5.14.

Assume that there exists (𝛙t)t∈[0,T]∈ℐ′​(ℤ^θ)(\bm{\psi}\_{t})\_{t\in[0,T]}\in\mathcal{I}^{{}^{\prime}}(\hat{\mathbb{Z}}^{\theta}) solution of ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) such that ([5.21](https://arxiv.org/html/2511.23295v1#S5.E21 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) holds. Moreover, assume there exists a constant C>0C>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |12​η⟨(ν(\mathcolorNavyBlue𝟑+øX0−ξ~t)−(ν𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)),ℤ^sθ⊗(ν\mathcolorNavyBlue𝟐+\mathcolorNavyBlue𝟑)⊗ℤ^s,tϕ⟩|≤C,s<t≤T and θ,ϕ∈𝒜.\bigg|\frac{1}{2\eta}\left\langle\left(\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})\right),\hat{\mathbb{Z}}\_{s}^{\theta}\otimes\left(\nu{\mathcolor{NavyBlue}{\mathbf{2}}}+{\mathcolor{NavyBlue}{\mathbf{3}}}\right)\otimes\hat{\mathbb{Z}}\_{s,t}^{\phi}\right\rangle\bigg|\leq C,\penalty 10000\ s<t\leq T\text{ and }\theta,\phi\in\mathcal{A}. |  | (5.26) |

Then, there exists θ∗∈𝒜\theta^{\*}\in\mathcal{A} satisfying ([5.22](https://arxiv.org/html/2511.23295v1#S5.E22 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).

###### Proof.

First, for a given α>0\alpha>0, we define the Banach space ℒp​(α)\mathcal{L}^{p}(\alpha) by

|  |  |  |
| --- | --- | --- |
|  | ℒp​(α):={θ:[0,T]×Ω→ℝ​prog. measurable process such that ​‖θ‖ℒp​(α)p:=𝔼​(∫0Te−α​t​|θt|p​𝑑t)<∞},\mathcal{L}^{p}(\alpha):=\left\{\theta:[0,T]\times\Omega\rightarrow\mathbb{R}\penalty 10000\ \text{prog. measurable process such that }||\theta||\_{\mathcal{L}^{p}(\alpha)}^{p}:=\mathbb{E}\left(\int\_{0}^{T}e^{-\alpha t}|\theta\_{t}|^{p}dt\right)<\infty\right\}, |  |

with p=2∨2​M~​𝟙{ν>0}p=2\vee 2\tilde{M}\mathbb{1}\_{\{\nu>0\}}. To prove the existence of θ∗\theta^{\*}, we use a fixed point approach. Namely, we prove that, for θ∈ℒp​(α)\theta\in\mathcal{L}^{p}(\alpha), the functional FF defined such as, for t≤Tt\leq T,

|  |  |  |
| --- | --- | --- |
|  | F​(θ)t:=12​η​⟨ν​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)−(ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑),ℤ^tθ⟩,F(\theta)\_{t}:=\frac{1}{2\eta}\langle\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}}),\hat{\mathbb{Z}}^{\theta}\_{t}\rangle, |  |

is a contraction. As done in the proof of Lemma [5.3](https://arxiv.org/html/2511.23295v1#S5.Thmthm3 "Lemma 5.3. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"), using a variation of constant approach, we observe that, for θ\theta, ϕ∈ℒp​(α)\phi\in\mathcal{L}^{p}(\alpha) and t≤Tt\leq T,

|  |  |  |
| --- | --- | --- |
|  | ℤ^tθ−ℤ^tϕ=∫0t[ℤ^sθ⊗(ν​\mathcolor​N​a​v​y​B​l​u​e​𝟐+\mathcolor​N​a​v​y​B​l​u​e​𝟑)⊗ℤ^s,tϕ]​(θs−ϕs)​𝑑s.\displaystyle\hat{\mathbb{Z}}^{\theta}\_{t}-\hat{\mathbb{Z}}^{\phi}\_{t}=\int\_{0}^{t}\left[\hat{\mathbb{Z}}\_{s}^{\theta}\otimes\left(\nu{\mathcolor{NavyBlue}{\mathbf{2}}}+{\mathcolor{NavyBlue}{\mathbf{3}}}\right)\otimes\hat{\mathbb{Z}}\_{s,t}^{\phi}\right](\theta\_{s}-\phi\_{s})\penalty 10000\ ds. |  |

Therefore, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F​(θ)t−F​(ϕ)t|\displaystyle|F(\theta)\_{t}-F(\phi)\_{t}| | =|∫0t12​η⟨ν(\mathcolorNavyBlue𝟑+øX0−ξ~t)−(ν𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑),ℤ^sθ⊗(ν\mathcolorNavyBlue𝟐+\mathcolorNavyBlue𝟑)⊗ℤ^s,tϕ⟩(θs−ϕs)ds|,\displaystyle=\left|\int\_{0}^{t}\frac{1}{2\eta}\langle\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}}),\hat{\mathbb{Z}}\_{s}^{\theta}\otimes\left(\nu{\mathcolor{NavyBlue}{\mathbf{2}}}+{\mathcolor{NavyBlue}{\mathbf{3}}}\right)\otimes\hat{\mathbb{Z}}\_{s,t}^{\phi}\rangle\penalty 10000\ (\theta\_{s}-\phi\_{s})\penalty 10000\ ds\right|, |  |

and as we assume ([5.26](https://arxiv.org/html/2511.23295v1#S5.E26 "In Lemma 5.14. ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), using Hölder’s inequality, we observe that, for t≤Tt\leq T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F​(θ)t−F​(ϕ)t|p\displaystyle|F(\theta)\_{t}-F(\phi)\_{t}|^{p} | ≤Cp​tp−1​∫0t(θs−ϕs)p​𝑑s.\displaystyle\leq C^{p}t^{p-1}\int\_{0}^{t}(\theta\_{s}-\phi\_{s})^{p}\penalty 10000\ ds. |  |

In this case, we infer that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖F​(θ)−F​(ϕ)‖ℒp​(α)p\displaystyle||F(\theta)-F(\phi)||^{p}\_{\mathcal{L}^{p}(\alpha)} | =𝔼​(∫0Te−α​t​|F​(θ)t−F​(ϕ)t|p​𝑑t)\displaystyle=\mathbb{E}\left(\int\_{0}^{T}e^{-\alpha t}\left|F(\theta)\_{t}-F(\phi)\_{t}\right|^{p}dt\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cp​𝔼​(∫0Te−α​t​tp−1​∫0t(θs−ϕs)p​𝑑s​𝑑t)\displaystyle\leq C^{p}\mathbb{E}\left(\int\_{0}^{T}e^{-\alpha t}t^{p-1}\int\_{0}^{t}(\theta\_{s}-\phi\_{s})^{p}\penalty 10000\ dsdt\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Cp​Tp−1α​‖θ−ϕ‖ℒp​(α)p.\displaystyle\leq\frac{C^{p}T^{p-1}}{\alpha}||\theta-\phi||^{p}\_{\mathcal{L}^{p}(\alpha)}. |  |

Then, there exists α>0,\alpha>0, such that FF is a contraction for θ∈ℒp​(α)\theta\in\mathcal{L}^{p}(\alpha). Therefore, using the Banach fixed-point theorem, there exists a unique θ∗\theta^{\*} that satisfies ([5.22](https://arxiv.org/html/2511.23295v1#S5.E22 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Since there exists α>0\alpha>0 such that θ∗∈ℒp​(α),\theta^{\*}\in\mathcal{L}^{p}(\alpha), we deduce that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(∫0T|θt∗|p​𝑑t)≤eα​T​‖θ∗‖ℒp​(α)p<∞,\displaystyle\mathbb{E}\left(\int\_{0}^{T}|\theta^{\*}\_{t}|^{p}dt\right)\leq e^{\alpha T}||\theta^{\*}||^{p}\_{\mathcal{L}^{p}(\alpha)}<\infty, |  |

and then θ∗∈𝒜\theta^{\*}\in\mathcal{A}.
∎

###### Proposition 5.15 (No permanent market impact).

Let us assume that ν=0\nu=0 and μ=0\mu=0. Let us define the time-dependent functions f​(t)f(t) and K​(t,s)K(t,s) as, for t<Tt<T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t):=c​tanh⁡(c​(T−t)η),f(t):=c\tanh\left(\frac{c(T-t)}{\eta}\right), |  | (5.27) |

with c:=λ​σ2​η2c:=\sqrt{\frac{\lambda\sigma^{2}\eta}{2}} and, for t<s<Tt<s<T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | K​(t,s):=cη​cosh⁡(c​(T−s)η)sinh⁡(c​(T−t)η).K(t,s):={\frac{c}{\eta}}\frac{\cosh\left(\frac{c(T-s)}{\eta}\right)}{\sinh\left(\frac{c(T-t)}{\eta}\right)}. |  | (5.28) |

Moreover, let us define ℰ~t\tilde{\mathcal{E}}\_{t} such that for all \mathcolor​N​a​v​y​B​l​u​e​𝐰=\mathcolor​N​a​v​y​B​l​u​e​𝐢𝟏​…​\mathcolor​N​a​v​y​B​l​u​e​𝐢𝐧{\mathcolor{NavyBlue}{\mathbf{w}}}={\mathcolor{NavyBlue}{\mathbf{i\_{1}}}}...{\mathcolor{NavyBlue}{\mathbf{i\_{n}}}} with n∈ℕn\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | ℰ~t\mathcolor​N​a​v​y​B​l​u​e​𝐰:={0,if​∃k∈{1,…,n}​such that​\mathcolor​N​a​v​y​B​l​u​e​𝐢𝐤=\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℰt\mathcolor​N​a​v​y​B​l​u​e​𝐰,if​∄​k∈{1,…,n}​such that​\mathcolor​N​a​v​y​B​l​u​e​𝐢𝐤=\mathcolor​N​a​v​y​B​l​u​e​𝟑,\tilde{\mathcal{E}}\_{t}^{{\mathcolor{NavyBlue}{\mathbf{w}}}}:=\begin{cases}0,&\text{if}\penalty 10000\ \exists k\in\{1,...,n\}\penalty 10000\ \text{such that}\penalty 10000\ {\mathcolor{NavyBlue}{\mathbf{i\_{k}}}}={\mathcolor{NavyBlue}{\mathbf{3}}},\\ \mathcal{E}\_{t}^{{\mathcolor{NavyBlue}{\mathbf{w}}}},&\text{if}\penalty 10000\ \nexists k\in\{1,...,n\}\penalty 10000\ \text{such that}\penalty 10000\ {\mathcolor{NavyBlue}{\mathbf{i\_{k}}}}={\mathcolor{NavyBlue}{\mathbf{3}}},\end{cases} |  |

with ℰt\mathcal{E}\_{t} given by ([4.3](https://arxiv.org/html/2511.23295v1#S4.E3 "In 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions")), and ξ^t\hat{\xi}\_{t} such as, for t<Tt<T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ^t:=∫tTK​(t,s)​ξ~s|ℰ~s−t​d​s.\hat{\xi}\_{t}:=\int\_{t}^{T}K(t,s)\tilde{\xi}\_{s}|\_{\tilde{\mathcal{E}}\_{s-t}}ds. |  | (5.29) |

Then, ψt\psi\_{t} defined, for t<Tt<T, by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψt\displaystyle\psi\_{t} | =f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔2+λ​σ22​∫tT(ξ~s−ξ^s)⊔⁣⊔2|ℰ~s−t​d​s\displaystyle=f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\frac{\lambda\sigma^{2}}{2}\int\_{t}^{T}\left(\tilde{\xi}\_{s}-\hat{\xi}\_{s}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}\bigg|\_{\tilde{\mathcal{E}}\_{s-t}}ds |  | (5.30) |
|  |  | +σ2​∫tTf​(s)​(ξ^s|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2|ℰ~s−t​d​s,\displaystyle+\sigma^{2}\int\_{t}^{T}f(s)\left(\hat{\xi}\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}\bigg|\_{\tilde{\mathcal{E}}\_{s-t}}ds, |  |

is a solution to the infinite-dimensional system of Riccati equation ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) belongs to ℐ′​(ℤ^θ)\mathcal{I}^{\prime}(\hat{\mathbb{Z}}^{\theta}), and satisfies ([5.21](https://arxiv.org/html/2511.23295v1#S5.E21 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Moreover, there exists θ∗∈𝒜\theta^{\*}\in\mathcal{A} solution to

|  |  |  |  |
| --- | --- | --- | --- |
|  | θt∗=1η​f​(t)​(⟨ξ^t,ℤ^tθ∗⟩−Xtθ∗),t≤T,\theta\_{t}^{\*}=\frac{1}{\eta}f(t)\left(\langle\hat{\xi}\_{t},\hat{\mathbb{Z}}\_{t}^{\theta^{\*}}\rangle-X\_{t}^{\theta^{\*}}\right),\quad t\leq T, |  | (5.31) |

and θ∗\theta^{\*} is the optimal control.

###### Proof.

First, let us define, for t<s<Tt<s<T, ℓt,s1:=(ξ^s|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2|ℰ~s−t\bm{\ell}^{1}\_{t,s}:=\left(\hat{\xi}\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}\bigg|\_{\tilde{\mathcal{E}}\_{s-t}} and ℓt,s2:=(ξ~s−ξ^s)⊔⁣⊔2|ℰ~s−t\bm{\ell}^{2}\_{t,s}:=\left(\tilde{\xi}\_{s}-\hat{\xi}\_{s}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}\bigg|\_{\tilde{\mathcal{E}}\_{s-t}}. Then, we observe that

|  |  |  |
| --- | --- | --- |
|  | ψ˙t=f˙​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔2−2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔ξ^˙t−σ2​f​(t)​(ξ^t|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2\displaystyle\dot{\psi}\_{t}=\dot{f}(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}-2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]\mathrel{\sqcup\mkern-3.2mu\sqcup}\dot{\hat{\xi}}\_{t}-\sigma^{2}{f}(t)\left(\hat{\xi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2} |  |
|  |  |  |
| --- | --- | --- |
|  | +σ2​∫tTf​(s)​ℓ˙t,s1​𝑑s−λ​σ22​(ξ~t−ξ^t)⊔⁣⊔2+λ​σ22​∫tTℓ˙t,s2​𝑑s\displaystyle+\sigma^{2}\int\_{t}^{T}f(s)\dot{\bm{\ell}}^{1}\_{t,s}\penalty 10000\ ds-\frac{\lambda\sigma^{2}}{2}\left(\tilde{\xi}\_{t}-\hat{\xi}\_{t}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\frac{\lambda\sigma^{2}}{2}\int\_{t}^{T}\dot{\bm{\ell}}^{2}\_{t,s}\penalty 10000\ ds |  |
|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟏=−2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔ξ^t|\mathcolor​N​a​v​y​B​l​u​e​𝟏+σ2​∫tTf​(s)​ℓt,s1|\mathcolor​N​a​v​y​B​l​u​e​𝟏​d​s+λ​σ22​∫tTℓt,s2|\mathcolor​N​a​v​y​B​l​u​e​𝟏​d​s\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}=-2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]\mathrel{\sqcup\mkern-3.2mu\sqcup}\hat{\xi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}+\sigma^{2}\int\_{t}^{T}f(s){\bm{\ell}}^{1}\_{t,s}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}ds+\frac{\lambda\sigma^{2}}{2}\int\_{t}^{T}{\bm{\ell}}^{2}\_{t,s}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}ds |  |
|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐=−2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔ξ^t|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐+2​f​(t)​(ξ^t|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2+σ2​∫tTf​(s)​ℓt,s1|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐​d​s+λ​σ22​∫tTℓt,s2|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐​d​s\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}=-2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]\mathrel{\sqcup\mkern-3.2mu\sqcup}\hat{\xi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}+2f(t)(\hat{\xi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\sigma^{2}\int\_{t}^{T}f(s){\bm{\ell}}^{1}\_{t,s}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}ds+\frac{\lambda\sigma^{2}}{2}\int\_{t}^{T}{\bm{\ell}}^{2}\_{t,s}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}ds |  |
|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟑=2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t],\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}}=2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right], |  |

with

|  |  |  |
| --- | --- | --- |
|  | ξ^˙t=−K​(t,t)​ξ~t+∫tT(K˙​(t,s)​ξ~s|ℰ~s−t+K​(t,s)​ξ~˙s|ℰ~s,t)​𝑑s.\dot{\hat{\xi}}\_{t}=-K(t,t)\tilde{\xi}\_{t}+\int\_{t}^{T}\left(\dot{K}(t,s)\tilde{\xi}\_{s}|\_{\tilde{\mathcal{E}}\_{s-t}}+K(t,s)\dot{\tilde{\xi}}\_{s}|\_{\tilde{\mathcal{E}}\_{s,t}}\right)ds. |  |

Using similar arguments as in the proof of Lemma [4.4](https://arxiv.org/html/2511.23295v1#S4.Thmthm4 "Lemma 4.4. ‣ 4 Pricing and perfect hedging in frictionless market ‣ Signature approach for pricing and hedging path-dependent options with frictions"), we have that for a given ℓ∈T​(ℝ3)\bm{\ell}\in T(\mathbb{R}^{3}) then, for t<st<s,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ|˙ℰ~s−t=−(ℓ|˙ℰ~s−t)|\mathcolor​N​a​v​y​B​l​u​e​𝟏−12​σ2​(ℓ|˙ℰ~s−t)|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐.\dot{\bm{\ell}|}\_{\tilde{\mathcal{E}}\_{s-t}}=-\left(\dot{\bm{\ell}|}\_{\tilde{\mathcal{E}}\_{s-t}}\right)|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}-\frac{1}{2}\sigma^{2}\left(\dot{\bm{\ell}|}\_{\tilde{\mathcal{E}}\_{s-t}}\right)|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}. |  | (5.32) |

Therefore, we observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟏−12​σ2​ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐=\displaystyle-\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}-\frac{1}{2}\sigma^{2}\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}= | −2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔∫tTK​(t,s)​ξ~˙s|ℰ~s,t​d​s\displaystyle-2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]\mathrel{\sqcup\mkern-3.2mu\sqcup}\int\_{t}^{T}K(t,s)\dot{\tilde{\xi}}\_{s}|\_{\tilde{\mathcal{E}}\_{s,t}}ds |  | (5.33) |
|  |  | −σ2​f​(t)​(ξ^t|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2+σ2​∫tTf​(s)​ℓ˙t,s1​𝑑s+λ​σ22​∫tTℓ˙t,s2​𝑑s.\displaystyle-\sigma^{2}{f}(t)\left(\hat{\xi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\sigma^{2}\int\_{t}^{T}f(s)\dot{\bm{\ell}}^{1}\_{t,s}ds+\frac{\lambda\sigma^{2}}{2}\int\_{t}^{T}\dot{\bm{\ell}}^{2}\_{t,s}ds. |  |

Moreover, we also have that

|  |  |  |
| --- | --- | --- |
|  | f˙​(t)=1η​f​(t)2−λ2​σ2,K˙​(t,s)=K​(t,s)​K​(t,t),\displaystyle\dot{f}(t)=\frac{1}{\eta}f(t)^{2}-\frac{\lambda}{2}\sigma^{2},\quad\dot{K}(t,s)=K(t,s)K(t,t), |  |

with K​(t,t)=c2η​f​(t)=λ​σ22​1f​(t)K(t,t)=\frac{c^{2}}{{{\eta}}f(t)}={\frac{\lambda\sigma^{2}}{2}}\frac{1}{f(t)}.
Thus, we infer that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | f˙​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔2−2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔[−K​(t,t)​ξ~t+∫tTK˙​(t,s)​ξ~s|ℰ~s−t​d​s]−λ​σ22​(ξ~t−ξ^t)⊔⁣⊔2\displaystyle\dot{f}(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}-2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]\mathrel{\sqcup\mkern-3.2mu\sqcup}\left[-K(t,t)\tilde{\xi}\_{t}+\int\_{t}^{T}\dot{K}(t,s)\tilde{\xi}\_{s}|\_{\tilde{\mathcal{E}}\_{s-t}}ds\right]-\frac{\lambda\sigma^{2}}{2}\left(\tilde{\xi}\_{t}-\hat{\xi}\_{t}\right)^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2} |  | (5.34) |
|  |  | =f˙​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔2−λ2​σ2​[(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)⊔⁣⊔2−(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t)⊔⁣⊔2]\displaystyle=\dot{f}(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}-\frac{\lambda}{2}\sigma^{2}\left[({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}-({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}\right] |  |
|  |  | =−λ2​σ2​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)⊔⁣⊔2+14​η​(𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)⊔⁣⊔2.\displaystyle=-\frac{\lambda}{2}\sigma^{2}({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\frac{1}{4\eta}(\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}. |  |

Putting together ([5.33](https://arxiv.org/html/2511.23295v1#S5.E33 "In 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and ([5.34](https://arxiv.org/html/2511.23295v1#S5.E34 "In 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we obtain that ψt\psi\_{t} satisfies the system of Riccati equations ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). As K​(t,s)K(t,s) is bounded for t<s<Tt<s<T, ξ^t∈T​(ℝ3)\hat{\xi}\_{t}\in T(\mathbb{R}^{3}) for all t<Tt<T, then, since f​(t)f(t) is also bounded for all t<Tt<T, ψt\psi\_{t} is well defined, has finitely many non-zero terms and belongs to ℐ′​(ℤ^θ)\mathcal{I}^{\prime}(\hat{\mathbb{Z}}^{\theta}). We also observe that, as ξ^t∈T​(ℝ3)\hat{\xi}\_{t}\in T(\mathbb{R}^{3}) and f​(t)f(t) is bounded, there exists a positive bounded time-dependent function C​(t)C(t) such that, for θ∈𝒜\theta\in\mathcal{A},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(∫0T⟨ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℤ^tθ⟩2​𝑑t)\displaystyle\mathbb{E}\left(\int\_{0}^{T}\langle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\rangle^{2}dt\right) | =𝔼​(∫0T⟨2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t]⊔⁣⊔ξ^t|\mathcolor​N​a​v​y​B​l​u​e​𝟐−σ2​∫tTf​(s)​ℓt,s1|\mathcolor​N​a​v​y​B​l​u​e​𝟐​d​s−λ​σ22​∫tTℓt,s2|\mathcolor​N​a​v​y​B​l​u​e​𝟐​d​s,ℤ^tθ⟩2​𝑑t)\displaystyle=\mathbb{E}\left(\int\_{0}^{T}\langle 2f(t)[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}]\mathrel{\sqcup\mkern-3.2mu\sqcup}\hat{\xi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}-\sigma^{2}\int\_{t}^{T}f(s){\bm{\ell}}^{1}\_{t,s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}ds-\frac{\lambda\sigma^{2}}{2}\int\_{t}^{T}{\bm{\ell}}^{2}\_{t,s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}ds,\hat{\mathbb{Z}}\_{t}^{\theta}\rangle^{2}dt\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​(∫0TC​(t)​(1+|Xtθ|2+|St|4​M~)​𝑑t)<∞,\displaystyle\leq\mathbb{E}\left(\int\_{0}^{T}C(t)\left(1+|X\_{t}^{\theta}|^{2}+|S\_{t}|^{4\tilde{M}}\right)dt\right)<\infty, |  |

and hence ([5.21](https://arxiv.org/html/2511.23295v1#S5.E21 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied. Furthermore, using the explicit form of ψt\psi\_{t}, the feedback equation ([5.22](https://arxiv.org/html/2511.23295v1#S5.E22 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) reduces

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θt∗\displaystyle\theta\_{t}^{\*} | =−f​(t)η​⟨\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t,ℤ^tθ∗⟩=f​(t)η​(⟨ξ^t,ℤ^tθ∗⟩−Xtθ∗).\displaystyle=-\frac{f(t)}{\eta}\langle{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t},\hat{\mathbb{Z}}\_{t}^{\theta^{\*}}\rangle=\frac{f(t)}{\eta}\left(\langle\hat{\xi}\_{t},\hat{\mathbb{Z}}\_{t}^{\theta^{\*}}\rangle-X\_{t}^{\theta^{\*}}\right). |  | (5.35) |

It remains to show that there exists θ∗\theta^{\*} satisfying ([5.35](https://arxiv.org/html/2511.23295v1#S5.E35 "In 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and belonging to 𝒜\mathcal{A}. For that, it is sufficient to show that the assumption ([5.26](https://arxiv.org/html/2511.23295v1#S5.E26 "In Lemma 5.14. ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) of Lemma [5.14](https://arxiv.org/html/2511.23295v1#S5.Thmthm14 "Lemma 5.14. ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") is satisfied. But as we have that

|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟑=2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t],\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}}=2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right], |  |

with f​(t)f(t) bounded, then we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |12​η⟨𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑,ℤ^sθ⊗\mathcolorNavyBlue𝟑⊗ℤ^s,tϕ⟩|\displaystyle\bigg|\frac{1}{2\eta}\left\langle\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}},\hat{\mathbb{Z}}\_{s}^{\theta}\otimes{\mathcolor{NavyBlue}{\mathbf{3}}}\otimes\hat{\mathbb{Z}}\_{s,t}^{\phi}\right\rangle\bigg| | =1η​|f​(t)|≤1η​supt≤T|f​(t)|,\displaystyle=\frac{1}{\eta}|f(t)|\leq\frac{1}{\eta}\sup\_{t\leq T}|f(t)|, |  |

and thus the assumption ([5.26](https://arxiv.org/html/2511.23295v1#S5.E26 "In Lemma 5.14. ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied.
∎

###### Proposition 5.16 (European quadratic payoff).

Let us assume that μ=0\mu=0, ν<2​η​λ​σ2\nu<\sqrt{2\eta\lambda\sigma^{2}}, and ξ=Γ​\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐\xi=\Gamma{\mathcolor{NavyBlue}{\mathbf{22}}} with Γ∈ℝ\Gamma\in\mathbb{R} such that |ν​Γ|<1|\nu\Gamma|<1. Moreover, let us consider the time-dependent function f​(t)f(t) given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t)=12​(1−ν​Γ)​[ν+c​tanh⁡(c​(1−ν​Γ)2​η​(T−t)−12​ln⁡(c+νc−ν))],f(t)=\frac{1}{2(1-\nu\Gamma)}\left[\nu+c\tanh\left(\frac{c(1-\nu\Gamma)}{2\eta}(T-t)-\frac{1}{2}\ln\left(\frac{c+\nu}{c-\nu}\right)\right)\right], |  | (5.36) |

with c:=2​η​λ​σ2c:=\sqrt{2\eta\lambda\sigma^{2}}. Then, ψt\psi\_{t} defined as, for t<Tt<T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψt=f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t]⊔⁣⊔2+σ2​ø​∫tTf​(s)​Γ2​𝑑s\psi\_{t}=f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t}\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\sigma^{2}{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}\int\_{t}^{T}f(s)\Gamma^{2}ds |  | (5.37) |

is a solution to the infinite-dimensional system of Riccati equation ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), belongs to ℐ′​(ℤ^θ)\mathcal{I}^{\prime}(\hat{\mathbb{Z}}^{\theta}), and satisfies ([5.21](https://arxiv.org/html/2511.23295v1#S5.E21 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Moreover, there exists θ∗∈𝒜\theta^{\*}\in\mathcal{A} solution to

|  |  |  |  |
| --- | --- | --- | --- |
|  | θt∗=ν−2​f​(t)​(1−ν​Γ)2​η​(Xtθ∗−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ∗⟩),\theta\_{t}^{\*}=\frac{\nu-2f(t)(1-\nu\Gamma)}{2\eta}\left(X\_{t}^{\theta^{\*}}-\langle{\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}},\hat{\mathbb{P}}\_{t}^{\theta^{\*}}\rangle\right), |  | (5.38) |

and θ∗\theta^{\*} is the optimal control.

###### Proof.

First, we observe that, since ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐=Γ​\mathcolor​N​a​v​y​B​l​u​e​𝟐\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}=\Gamma{\mathcolor{NavyBlue}{\mathbf{2}}}, then ξ~˙t=0\dot{\tilde{\xi}}\_{t}=0, ξ~t|\mathcolor​N​a​v​y​B​l​u​e​𝟐=Γ​ø{\tilde{\xi}}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}=\Gamma{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}} and ξ~t|\mathcolor​N​a​v​y​B​l​u​e​𝟏=ξ~t|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐=0{\tilde{\xi}}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}={\tilde{\xi}}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}=0. In this case,

|  |  |  |
| --- | --- | --- |
|  | ψ˙t=f˙​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t]⊔⁣⊔2−σ2​f​(t)​Γ2​ø\displaystyle\dot{\psi}\_{t}=\dot{f}(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t}\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}-\sigma^{2}{f}(t)\Gamma^{2}{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟏=0\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}=0 |  |
|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐=−2​Γ​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t]\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}=-2\Gamma f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐=2​f​(t)​Γ2​ø\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}=2f(t)\Gamma^{2}{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟑=2​f​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t].\displaystyle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}}=2f(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t}\right]. |  |

We deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | −σ2​f​(t)​Γ2​ø=−𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟏−12​σ2​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐.-\sigma^{2}{f}(t)\Gamma^{2}{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}=-\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{1}}}}-\frac{1}{2}\sigma^{2}\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{22}}}}. |  | (5.39) |

Moreover, we also observe that

|  |  |  |
| --- | --- | --- |
|  | 14​η​[ν​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)−(ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)]⊔⁣⊔2=14​η​(ν−2​f​(t)​(1−Γ​ν))2​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)⊔⁣⊔2.\displaystyle\frac{1}{4\eta}\left[\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}=\frac{1}{4\eta}(\nu-2f(t)(1-\Gamma\nu))^{2}({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}. |  |

Thus, using the form of f​(t)f(t) given by ([5.36](https://arxiv.org/html/2511.23295v1#S5.E36 "In Proposition 5.16 (European quadratic payoff). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | f˙​(t)=14​η​(ν−2​f​(t)​(1−ν​Γ))2−λ2​σ2,t<T​ and ​f​(T)=0,\displaystyle\dot{f}(t)=\frac{1}{4\eta}\left(\nu-2f(t)(1-\nu\Gamma\right))^{2}-\frac{\lambda}{2}\sigma^{2},\penalty 10000\ t<T\text{ and }f(T)=0, |  |

and we infer that

|  |  |  |
| --- | --- | --- |
|  | f˙​(t)​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t]⊔⁣⊔2=−λ2​σ2​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)⊔⁣⊔2+14​η​[ν​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)−(ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)]⊔⁣⊔2.\dot{f}(t)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t}\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}=-\frac{\lambda}{2}\sigma^{2}({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}+\frac{1}{4\eta}\left[\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})\right]^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2}. |  |

Putting all together, we deduce that ψt\psi\_{t} satisfies the system of Riccati equations ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Since f​(t)f(t) is bounded for all t<Tt<T, ψt\psi\_{t} is well defined, has finitely many non-zero terms and belongs to ℐ′​(ℤ^θ)\mathcal{I}^{\prime}(\hat{\mathbb{Z}}^{\theta}).
We also have that ([5.21](https://arxiv.org/html/2511.23295v1#S5.E21 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied since, for θ∈𝒜\theta\in\mathcal{A},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(∫0T⟨ψt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℤ^tθ⟩2​𝑑t)=4​Γ2​𝔼​(∫0Tf​(t)2​(Xtθ−Γ​Ptθ)2​𝑑t)<∞.\displaystyle\mathbb{E}\left(\int\_{0}^{T}\langle\psi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{Z}}\_{t}^{\theta}\rangle^{2}dt\right)=4\Gamma^{2}\mathbb{E}\left(\int\_{0}^{T}f(t)^{2}\left(X\_{t}^{\theta}-\Gamma P\_{t}^{\theta}\right)^{2}dt\right)<\infty. |  |

Furthermore, using the explicit form of ψt\psi\_{t}, the feedback equation ([5.22](https://arxiv.org/html/2511.23295v1#S5.E22 "In Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) reduces

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θt∗\displaystyle\theta\_{t}^{\*} | =ν−2​f​(t)​(1−ν​Γ)2​η​(Xtθ∗−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ∗⟩).\displaystyle=\frac{\nu-2f(t)(1-\nu\Gamma)}{2\eta}\left(X\_{t}^{\theta^{\*}}-\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta^{\*}}\rangle\right). |  | (5.40) |

It remains to show that there exists θ∗\theta^{\*} satisfying ([5.40](https://arxiv.org/html/2511.23295v1#S5.E40 "In 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and belonging to 𝒜\mathcal{A}. For that, it is sufficient to show that the assumption ([5.26](https://arxiv.org/html/2511.23295v1#S5.E26 "In Lemma 5.14. ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) of Lemma [5.14](https://arxiv.org/html/2511.23295v1#S5.Thmthm14 "Lemma 5.14. ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") is satisfied. As

|  |  |  |
| --- | --- | --- |
|  | ν​(\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ~t)−(ν​𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)=(ν−2​f​(t)​(1−ν​Γ))​[\mathcolor​N​a​v​y​B​l​u​e​𝟑+ø​X0−ξ^t],\displaystyle\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})=\left(\nu-2f(t)(1-\nu\Gamma)\right)\left[{\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\hat{\xi}\_{t}\right], |  |

with f​(t)f(t) bounded, ξ~t|\mathcolor​N​a​v​y​B​l​u​e​𝟐=Γ​ø\tilde{\xi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}=\Gamma{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}, then we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |12​η⟨(ν(\mathcolorNavyBlue𝟑+øX0−ξ~t)−(ν𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟐+𝝍t|\mathcolor​N​a​v​y​B​l​u​e​𝟑)),ℤ^sθ⊗(ν\mathcolorNavyBlue𝟐+\mathcolorNavyBlue𝟑)⊗ℤ^s,tϕ⟩|\displaystyle\bigg|\frac{1}{2\eta}\left\langle\left(\nu({\mathcolor{NavyBlue}{\mathbf{3}}}+{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}X\_{0}-\tilde{\xi}\_{t})-(\nu\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}+\bm{\psi}\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{3}}}})\right),\hat{\mathbb{Z}}\_{s}^{\theta}\otimes\left(\nu{\mathcolor{NavyBlue}{\mathbf{2}}}+{\mathcolor{NavyBlue}{\mathbf{3}}}\right)\otimes\hat{\mathbb{Z}}\_{s,t}^{\phi}\right\rangle\bigg| | =12​η​|(ν−2​f​(t)​(1−ν​Γ))​(1−ν​Γ)|\displaystyle=\frac{1}{2\eta}|\left(\nu-2f(t)(1-\nu\Gamma)\right)(1-\nu\Gamma)| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​η​supt≤T|(ν−2​f​(t)​(1−ν​Γ))​(1−ν​Γ)|,\displaystyle\leq\frac{1}{2\eta}\sup\_{t\leq T}|\left(\nu-2f(t)(1-\nu\Gamma)\right)(1-\nu\Gamma)|, |  |

and the assumption ([5.26](https://arxiv.org/html/2511.23295v1#S5.E26 "In Lemma 5.14. ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied.
∎

## 6 Numerical illustration

In this section, we illustrate numerically the signature-based hedging strategies given by Theorem [5.9](https://arxiv.org/html/2511.23295v1#S5.Thmthm9 "Theorem 5.9. ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") by solving numerically the system of infinite-dimensional Riccati equations ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). First we consider exact signature payoffs such as European or Asian quadratic options and then we take more general path-dependent payoffs that we approximate by signature payoffs relying on the universal approximation theorem.

Moreover, we compare the signature-based strategy taking into account both temporary and permanent market impact with the optimal hedging strategy that only accounts for temporary market impact deduced for general path-dependent payoffs in Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)).

For our numerical results, we set the initial inventory X0X\_{0} equal to the Bachelier Δ\Delta. For signature payoffs, this reduces to X0=(ξ0|\mathcolor​N​a​v​y​B​l​u​e​𝟐)øX\_{0}=\left(\xi\_{0}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\right)^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}. Moreover, we assume that the initial portfolio value V0V\_{0} is equal to this indifference price π\pi defined in Section [5](https://arxiv.org/html/2511.23295v1#S5 "5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). Therefore, the initial portfolio value will vary depending on the choice of market impact parameters η\eta and ν\nu, which will impact the final value of the P&L but not the trading speed. It reduces to V0=ξ0ø−ψ0V\_{0}=\xi\_{0}^{{\color[rgb]{0.0600000000000001,0.46,1}\definecolor[named]{pgfstrokecolor}{rgb}{0.0600000000000001,0.46,1}\pgfsys@color@cmyk@stroke{0.94}{0.54}{0}{0}\pgfsys@color@cmyk@fill{0.94}{0.54}{0}{0}\textup{{\o {}}}}}-\psi\_{0} for signature payoffs. Finally, recall that, as explained in Remark [5.13](https://arxiv.org/html/2511.23295v1#S5.Thmthm13 "Remark 5.13 (Numerical implementation). ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"), when we solve numerically the Riccati equation ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we consider the shuffle product projected on T2​M~​(ℝ3)T^{2\tilde{M}}(\mathbb{R}^{3}) defined as ⊔⁣⊔~:(T2​M~​(ℝ3))2→T2​M~​(ℝ3)\widetilde{\mathrel{\sqcup\mkern-3.2mu\sqcup}}:(T^{2\tilde{M}}(\mathbb{R}^{3}))^{2}\to T^{2\tilde{M}}(\mathbb{R}^{3}), such that 𝝍t∈T2​M~​(ℝ3)\bm{\psi}\_{t}\in T^{2\tilde{M}}(\mathbb{R}^{3}), M~\tilde{M} being the truncation order ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐∈TM~​(ℝ2)\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\in T^{\tilde{M}}(\mathbb{R}^{2}). Unless otherwise stated, we consider the following parameters for our numerical results:

|  |  |  |
| --- | --- | --- |
|  | S0=10,μ=0,σ=2,T=0.2,η=0.001,ν=0.001,λ=0.01.S\_{0}=10,\penalty 10000\ \mu=0,\penalty 10000\ \sigma=2,\penalty 10000\ T=0.2,\penalty 10000\ \eta=0.001,\penalty 10000\ \nu=0.001,\penalty 10000\ \lambda=0.01. |  |

### 6.1 Signature payoffs

We consider two particular signature payoffs:

* •

  European quadratic payoff: HTθ=N×(PTθ−K)2H\_{T}^{\theta}=N\times\ (P\_{T}^{\theta}-K)^{2},
* •

  Asian quadratic payoff: HTθ=N×(1T​∫0TPtθ​𝑑t−K)2H\_{T}^{\theta}=N\times\left(\frac{1}{T}\int\_{0}^{T}P\_{t}^{\theta}dt-K\right)^{2},

where NN corresponds to a given nominal.

First, since the European quadratic payoff has a constant Gamma, an application of Proposition [5.16](https://arxiv.org/html/2511.23295v1#S5.Thmthm16 "Proposition 5.16 (European quadratic payoff). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") yields an explicit expression for the optimal trading speed, in the spirit of Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)). Thus, this allows us to perform a sanity check on the stability of the numerical solution of the Riccati equation ([5.20](https://arxiv.org/html/2511.23295v1#S5.E20 "In 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
Figure [1](https://arxiv.org/html/2511.23295v1#S6.F1 "Figure 1 ‣ 6.1 Signature payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions") compares a sample path of trading speed obtained for a given European quadratic option. As expected, we see that the optimal strategy obtained by numerically solving the Riccati equation perfectly matches the closed form expression deduced in Proposition [5.16](https://arxiv.org/html/2511.23295v1#S5.Thmthm16 "Proposition 5.16 (European quadratic payoff). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). This suggests that the numerical resolution of the equation appears to be stable.

![Refer to caption](Figures/compa_eu_quadratic_options_07_10_0005.png)

![Refer to caption](Figures/compa_eu_quadratic_options_07_10_001.png)

Figure 1:  Sample path of trading speed for the European quadratic payoff: explicit expression given by Proposition [5.16](https://arxiv.org/html/2511.23295v1#S5.Thmthm16 "Proposition 5.16 (European quadratic payoff). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions") vs numerical resolution of Riccati equation with truncated shuffle product. Parameters: M=2M=2, K=S0K=S\_{0} and N=200N=200.

Moving to Asian quadratic options, we no longer have an explicit expression for the optimal trading speed, except for ν=0\nu=0, as stated by Proposition [5.15](https://arxiv.org/html/2511.23295v1#S5.Thmthm15 "Proposition 5.15 (No permanent market impact). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"), where we retrieve the same strategy as in Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)). Therefore, for ν>0\nu>0, numerically solving the Riccati equation becomes essential to determine the optimal strategy.
As a sanity check, as ν→0\nu\to 0, the solution obtained from the Riccati system is expected to converge to the explicit solution. This is illustrated in Figure [2](https://arxiv.org/html/2511.23295v1#S6.F2 "Figure 2 ‣ 6.1 Signature payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions"), which shows a sample path of the optimal trading speed and inventory for a given Asian quadratic option under different permanent market impact parameters. We clearly observe the convergence phenomenon as ν→0\nu\to 0, providing an additional validation of our numerical implementation of the Riccati equations. When permanent market impact is introduced (ν>0\nu>0), a gap appears whose magnitude increases with the value of the permanent impact parameter ν\nu. As expected, the larger ν\nu is, the slower and flatter the resulting trading speed becomes.

![Refer to caption](Figures/compa_asian_quadratic_options_28_10.png)


Figure 2: Sample path of trading speed and inventory for Asian quadratic payoff. Solid line: explicit hedging strategy assuming ν=0\nu=0 given by Proposition [5.15](https://arxiv.org/html/2511.23295v1#S5.Thmthm15 "Proposition 5.15 (No permanent market impact). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"); dashed lines: signature-based strategies obtained by numerically solving the Riccati equations with projected shuffle product. Parameters: M=4M=4, K=S0K=S\_{0}, and N=200N=200.

Moreover, to highlight the benefits of incorporating the permanent market impact information into the trading strategy, we compare the P&L generated by two traders, when ν>0\nu>0. The first one is aware of the permanent market impact, incorporates this information into her strategy and follows the optimal trading speed for ν>0\nu>0. The second one ignores the permanent impact and follows the explicit trading strategy assuming ν=0\nu=0 given by Proposition [5.15](https://arxiv.org/html/2511.23295v1#S5.Thmthm15 "Proposition 5.15 (No permanent market impact). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). We assume that both traders have the same risk aversion and ask an indifference price to hedge the option. Therefore, the trader assuming ν>0\nu>0 asks a price π​(ν>0)\pi(\nu>0) while the second trader, ignoring the permanent impact, asks π​(ν=0)\pi(\nu=0). Both traders’ strategies are evaluated using the same criterion with ν>0\nu>0: the first trader’s strategy is optimal, whereas the second trader’s is not. Results are shown in Figure [3](https://arxiv.org/html/2511.23295v1#S6.F3 "Figure 3 ‣ 6.1 Signature payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions"). We can see that, when there is a permanent market impact, there is an advantage to be gained by incorporating this information into the hedging strategy and following the signature-based strategy assuming ν>0\nu>0, rather than the strategy assuming only a temporary impact. Obviously, this information gain depends on the size of the permanent impact parameter ν\nu and will be higher when the permanent impact is higher. The gap between the two P&Ls can be attributed to two things:

* •

  the trader omitting the permanent impact will misprice the option, underestimates the risk she takes (see Table [1](https://arxiv.org/html/2511.23295v1#S6.T1 "Table 1 ‣ 6.1 Signature payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions")). This will affect the final value of her P&L,
* •

  the trader who overlooks the permanent impact will trade too aggressively (see Figure [2](https://arxiv.org/html/2511.23295v1#S6.F2 "Figure 2 ‣ 6.1 Signature payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions")), and push the price further in the wrong direction, which will adversely impact her P&L over time. The optimal strategy with ν>0\nu>0, taking into account this impact, attempts to push the price in the right direction (see Remark [5.10](https://arxiv.org/html/2511.23295v1#S5.Thmthm10 "Remark 5.10 (Interpretation of 𝜃^∗). ‣ 5.2.1 General verification theorem ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).

![Refer to caption](Figures/hist_asian_quadratic_options_12_11_nu_0005.png)

![Refer to caption](Figures/hist_asian_quadratic_options_12_11_nu_001.png)

![Refer to caption](Figures/hist_asian_quadratic_options_12_11_nu_0015.png)

Figure 3: Histogram of RTθR\_{T}^{\theta} for Asian quadratic payoff with ν>0\nu>0: signature-based strategy vs explicit hedging strategy assuming ν=0\nu=0 given by Proposition [5.15](https://arxiv.org/html/2511.23295v1#S5.Thmthm15 "Proposition 5.15 (No permanent market impact). ‣ 5.2.2 Explicit solution to the infinite-dimensional system of Riccati equations: two examples ‣ 5.2 Verification result using infinite-dimensional Riccati equations ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"). Other parameters: M=4M=4, K=S0K=S\_{0}, and N=200N=200. M​Q​V​(θ)=𝔼​(RTθ−λ2​[Rθ,Rθ]T)MQV(\theta)=\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right).



| Bachelier price | ν=0\nu=0 | ν=0.0005\nu=0.0005 | ν=0.001\nu=0.001 | ν=0.0015\nu=0.0015 |
| --- | --- | --- | --- | --- |
| 53.333 | 79.559 | 80.559 | 81.218 | 81.617 |

Table 1: Indifference prices π\pi for Asian quadratic payoff with respect to ν\nu. Other parameters: M=4M=4, K=S0K=S\_{0}, and N=200N=200.

### 6.2 Non-signature path-dependent payoffs

We consider now payoffs that cannot be exactly represented as signature payoffs as it is the case for European, Asian or barrier call options. By relying on the universal linearization property of signatures, see Lyons, Nejad, and Perez Arribas ([2020](https://arxiv.org/html/2511.23295v1#bib.bib31)); Cuchiero, Primavera, and Svaluto-Ferro ([2025b](https://arxiv.org/html/2511.23295v1#bib.bib20)), we can approximate those path-dependent payoffs by signature payoffs, i.e. by linear combination of time-augmented signature elements. More precisely, for a continuous functional FF, a continuous semimartingale (Yt)t∈[0,T](Y\_{t})\_{t\in[0,T]} valued in ℝd\mathbb{R}^{d}, and a given truncation order M>0M>0, there exists ℓ∈TM​(ℝ𝕕+𝟙)\bm{\ell}\in T^{M}(\mathbb{R^{d+1}}) such that

|  |  |  |
| --- | --- | --- |
|  | F​((t,Yt)t≤T)≈⟨ℓ,𝕐^t⟩.F\left((t,Y\_{t})\_{t\leq T}\right)\approx\langle\bm{\ell},\hat{\mathbb{Y}}\_{t}\rangle. |  |

This means that the semi-explicit signature-based hedging strategy can also be used to hedge general (non-signature) path-dependent payoffs. However, to apply the signature-based hedging strategy, we first have to regress those path-dependent payoffs against truncated signature payoffs to determine ℓ\bm{\ell}, and then solve the infinite-dimensional Riccati equation associated with the signature approximate payoff ⟨ℓ,𝕐^t⟩\langle\bm{\ell},\hat{\mathbb{Y}}\_{t}\rangle. Algorithm [1](https://arxiv.org/html/2511.23295v1#algorithm1 "Algorithm 1 ‣ 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions") explicitly states how to get a linear signature representation for a given path-dependent payoff. Furthermore, as we consider non-signature payoffs, the indifference price π\pi does not have an explicit form and should also be approximated. In this sense, we approximate the indifference price by π~\tilde{\pi} such that it satisfies the following equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(RTθs​i​g∗−λ2​[Rθs​i​g∗,Rθs​i​g∗]T)=0,\mathbb{E}\left(R\_{T}^{\theta^{\*}\_{sig}}-\frac{\lambda}{2}[R^{\theta^{\*}\_{sig}},R^{\theta^{\*}\_{sig}}]\_{T}\right)=0, |  | (6.1) |

where

|  |  |  |
| --- | --- | --- |
|  | Rtθs​i​g∗=(π~−X0​S0)+Xtθs​i​g∗​Ptθs​i​g∗−∫0tP~sθs​i​g∗​(θs​i​g∗)s​𝑑s−h​((s,Psθs​i​g∗)s≤t),t≤T,R\_{t}^{\theta^{\*}\_{sig}}=(\tilde{\pi}-X\_{0}S\_{0})+X\_{t}^{\theta^{\*}\_{sig}}P\_{t}^{\theta^{\*}\_{sig}}-\int\_{0}^{t}\tilde{P}^{\theta^{\*}\_{sig}}\_{s}{(\theta^{\*}\_{sig})}\_{s}ds-h\left(\left(s,P\_{s}^{\theta^{\*}\_{sig}}\right)\_{s\leq t}\right),\penalty 10000\ t\leq T, |  |

with h​((s,Psθs​i​g∗)s≤t)h\left(\left(s,P\_{s}^{\theta^{\*}\_{sig}}\right)\_{s\leq t}\right) the Bachelier price of the path-dependent payoff at time t<Tt<T, and θs​i​g∗\theta^{\*}\_{sig} the optimal trading speed associated to the regressed signature payoff.

Algorithm 1  Regression of path-dependent payoffs against truncated signature payoffs

Consider a payoff of the following form

|  |  |  |
| --- | --- | --- |
|  | HT=F​((t,Yt)t≤T),H\_{T}=F\left((t,Y\_{t})\_{t\leq T}\right), |  |

with (Yt)t∈[0,T](Y\_{t})\_{t\in[0,T]} a given stochastic process valued in ℝ\mathbb{R}.

Input:

* •

  Fix J>0J>0 the number of points in the discretization of [0,T][0,T],
* •

  Fix L>0L>0 the number of realisations of trajectory of YY,
* •

  Fix M≥0M\geq 0 the truncation order of ℓ\bm{\ell},

Online:

1. 1.

   Generate LL realizations of the YY, denoted by Y(1),…,Y(L)Y^{(1)},\ldots,Y^{(L)},
2. 2.

   For each realization l=1,…,Ll=1,\ldots,L, compute HT(l)H\_{T}^{(l)} and the truncated signature 𝕐^T(l),≤M\hat{\mathbb{Y}}\_{T}^{(l),\penalty 10000\ \leq M} up to order MM for t∈[0,T]t\in[0,T],
3. 3.

   Regress (HT(l))1≤l≤L(H\_{T}^{(l)})\_{1\leq l\leq L} against (𝕐^T(l),≤M)1≤l≤L(\hat{\mathbb{Y}}\_{T}^{(l),\penalty 10000\ \leq M})\_{1\leq l\leq L} to learn the coefficients of ℓ∈TM​(ℝ2)\bm{\ell}\in T^{M}(\mathbb{R}^{2}) that minimize

   |  |  |  |
   | --- | --- | --- |
   |  | ℒ=1L​∑l=1L|HT(l)−⟨ℓ,𝕐^T(l),≤M⟩|2.\mathcal{L}=\frac{1}{L}\sum\_{l=1}^{L}\left|H^{(l)}\_{T}-\left\langle\bm{\ell},\hat{\mathbb{Y}}\_{T}^{(l),\penalty 10000\ \leq M}\right\rangle\right|^{2}. |  |

Let us move on to some numerical illustrations. We consider different types of payoffs:

* •

  European call: HTθ=N×(PTθ−K)+H\_{T}^{\theta}=N\times(P\_{T}^{\theta}-K)\_{+},
* •

  Asian call: HTθ=N×(1T​∫0TPsθ​𝑑s−K)+H\_{T}^{\theta}=N\times(\frac{1}{T}\int\_{0}^{T}P\_{s}^{\theta}ds-K)\_{+},
* •

  One-touch max: HTθ=N×𝟙{maxt<T⁡Ptθ≥H}H\_{T}^{\theta}=N\times\mathbb{1}\_{\{\max\_{t<T}P\_{t}^{\theta}\geq H\}},
* •

  Look-back call with floating strike: HTθ=N×(PTθ−min{t<T}⁡Ptθ)H\_{T}^{\theta}=N\times\left(P\_{T}^{\theta}-\min\_{\{t<T\}}P\_{t}^{\theta}\right),

where NN corresponds to a given nominal.
  
  
First, recall that, for general European options, Almgren and Li ([2016](https://arxiv.org/html/2511.23295v1#bib.bib5)) characterized the optimal hedging strategy as a solution to the HJB equation given by ([2.5](https://arxiv.org/html/2511.23295v1#S2.E5 "In 2.1 The Almgren and Li setup ‣ 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Using this information, for an European call payoff, we compare the signature-based strategy associated to the regressed signature payoff with the optimal strategy obtained by numerically solving the corresponding HJB equation given by ([2.5](https://arxiv.org/html/2511.23295v1#S2.E5 "In 2.1 The Almgren and Li setup ‣ 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). This allows us to see whether, in this context of market impact, the signature-based strategies are able to well approximate the optimal strategy when payoffs do not admit an exact signature representation.

We consider two types of market: a frictionless market with η=ν=0\eta=\nu=0 and a frictional market with η>0\eta>0 and ν>0\nu>0.
In the frictionless market, see Figure [4](https://arxiv.org/html/2511.23295v1#S6.F4 "Figure 4 ‣ 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions"), the signature-based strategy provides a close approximation of the perfect hedging strategy for small times tt, but it fails to recover the correct behavior as t→Tt\to T. The discrepancy is primarily due to the strong nonlinearity of the perfect hedging strategy for call options near maturity. This observation mitigates the conclusion of (Lyons, Nejad, and Perez Arribas, [2020](https://arxiv.org/html/2511.23295v1#bib.bib31), Section 7.1) regarding the ability of signature-based strategies to accurately recover the perfect hedging strategy in a frictionless setting. By contrast, in the presence of market frictions, see Figure [5](https://arxiv.org/html/2511.23295v1#S6.F5 "Figure 5 ‣ 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions"), the signature approximation performs significantly better. In this case, the sample paths of trading speeds and inventories generated by the signature-based approach are much closer to those of the optimal strategy. This improvement can be attributed to two effects: first, market impact naturally smoothens the optimal trading speeds; second, the signature-approximated payoff leads to a smoother (target) perfect hedging strategy compared to the call payoff. Together, these effects mitigate approximation errors and enhance the accuracy of the signature-based strategy. Thus, in the frictional market, the signature-based strategy can be considered a sufficiently accurate approximation of the optimal strategy, showing a striking improvement compared to the frictionless setting (compare the error on the inventory in Figures [4](https://arxiv.org/html/2511.23295v1#S6.F4 "Figure 4 ‣ 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions") and [5](https://arxiv.org/html/2511.23295v1#S6.F5 "Figure 5 ‣ 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Clearly, in the absence of frictions, approximating the payoff of a call option by a fifth-order polynomial is not sufficiently accurate for pricing and hedging. However, once market frictions are introduced, the fifth-order polynomial approximation becomes significantly more accurate, even though it additionally requires truncating and numerically solving infinite-dimensional Riccati equations.

![Refer to caption](Figures/compa_eu_call_options_error_perfect_13_11_M_5.png)


Figure 4: Sample paths of inventory XtθX\_{t}^{\theta} for European call payoff with η=ν=0\eta=\nu=0: signature-based approximated strategy vs Bachelier Delta hedging strategy. Parameters: M=5M=5, K=S0K=S\_{0}, and N=200N=200.

![Refer to caption](Figures/compa_eu_call_options_paths_error_friction_13_11_M_5.png)


Figure 5: Sample paths of trading speed θt\theta\_{t} and inventory XtθX\_{t}^{\theta} for European call payoff with η=ν=0.001\eta=\nu=0.001: signature-based approximated strategy vs optimal hedging strategy by solving the HJB equation ([2.5](https://arxiv.org/html/2511.23295v1#S2.E5 "In 2.1 The Almgren and Li setup ‣ 2 Bachelier model with temporary and permanent impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Parameters: M=5M=5, K=S0K=S\_{0}, and N=200N=200.

We now emphasize the relevance of signature-based strategies to hedge non-signature path-dependent payoffs when ν>0\nu>0. To this end, we consider different types of options: European call, Asian call, one-touch and look-back call with floating strike. As in the previous subsection, we compare the P&L generated by two types of traders: the first one is aware of the permanent market impact and follows the signature-based strategy for ν>0\nu>0, while the second one ignores the permanent impact and follows the trading strategy of Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)), which consists of tracking the Bachelier Delta of the non-signature payoffs. Both traders’ strategies are evaluated using the same criterion with ν>0\nu>0.

Figure [6](https://arxiv.org/html/2511.23295v1#S6.F6 "Figure 6 ‣ 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions") shows the histograms of the P&L at maturity generated by two strategies for different types of payoffs. Looking at the histograms, we remark that even though the signature-based strategy is an approximation of the optimal strategy, it seems very relevant for hedging non-signature payoffs in the presence of market frictions. Furthermore, if we compare the mean-quadratic variation functional M​Q​V​(θ)MQV(\theta), we observe that the signature-based strategy outperforms the Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)) strategy that does not take into account the permanent impact. Thus, we see that there is therefore a substantial advantage in favoring the signature-based hedging strategy. The discrepancy between the P&Ls can be attributed to the same factors as in the case of Asian quadratic payoff. At inception, the trader that follows Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)) strategy misprices the options regarding the risk she takes when ν>0\nu>0 (see Table [2](https://arxiv.org/html/2511.23295v1#S6.T2 "Table 2 ‣ 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Moreover, during the trading period, the trader that does not take into account the permanent impact will trade too aggressively, and this will more adversely impact her P&L over time.

![Refer to caption](Figures/hist_call_options_compa_12_11.png)

![Refer to caption](Figures/hist_asian_call_options_12_11.png)

![Refer to caption](Figures/hist_one_touch_options_12_11.png)

![Refer to caption](Figures/hist_lookback_min_floating_12_11.png)

Figure 6: Histogram of RTθR\_{T}^{\theta} for different payoffs: signature-based hedging strategy vs Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)) hedging strategy (ν=0)\nu=0). Parameters: M=5M=5, K=S0K=S\_{0}, H=1.05×S0H=1.05\times S\_{0} and N=200N=200. M​Q​V​(θ)=𝔼​(RTθ−λ2​[Rθ,Rθ]T)MQV(\theta)=\mathbb{E}\left(R\_{T}^{\theta}-\frac{\lambda}{2}[R^{\theta},R^{\theta}]\_{T}\right).



| Payoff | Bachelier price | Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)) (ν=0\nu=0) | Sig-approx. (ν=0.001\nu=0.001) |
| --- | --- | --- | --- |
| European call | 71.3649 | 84.3719 | 84.9214 |
| Asian call | 41.2025 | 56.3211 | 56.9731 |
| One-touch | 115.2300 | 156.5044 | 156.9042 |
| Look-back | 142.7299 | 178.6318 | 180.2740 |

Table 2: Indifference prices for different payoffs: Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)) indifference price is obtained by using the Bank, Soner, and Voß ([2017](https://arxiv.org/html/2511.23295v1#bib.bib6)) strategy with Bachelier Delta as tracking strategy; the indifference price for ν=0.001\nu=0.001 is approximated by π~\tilde{\pi} using ([6.1](https://arxiv.org/html/2511.23295v1#S6.E1 "In 6.2 Non-signature path-dependent payoffs ‣ 6 Numerical illustration ‣ Signature approach for pricing and hedging path-dependent options with frictions")). Parameters: M=5M=5, K=S0K=S\_{0}, H=1.05×S0H=1.05\times S\_{0}, and N=200N=200.

## 7 Proofs

### 7.1 Proof of Lemma [5.3](https://arxiv.org/html/2511.23295v1#S5.Thmthm3 "Lemma 5.3. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")

###### Proof.

First, for given θ,ϕ∈𝒜\theta,\phi\in\mathcal{A}, we have that

|  |  |  |
| --- | --- | --- |
|  | d​ℙ^tθ=ℙ^tθ⊗d​P^tθ,d​ℙ^tθ+ε​ϕ=ℙ^tθ+ε​ϕ⊗d​P^tθ+ν​ε​ϕt​ℙ^tθ+ε​ϕ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐​d​t.\displaystyle d\hat{\mathbb{P}}^{\theta}\_{t}=\hat{\mathbb{P}}\_{t}^{\theta}\otimes d\hat{P}\_{t}^{\theta},\quad d\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{t}=\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon\phi}\otimes d\hat{P}\_{t}^{\theta}+\nu\varepsilon\phi\_{t}\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{t}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\penalty 10000\ dt. |  |

Therefore, we infer that

|  |  |  |
| --- | --- | --- |
|  | d​[ℙ^tθ+ε​ϕ−ℙ^tθε]=ℙ^tθ+ε​ϕ−ℙ^tθε⊗d​P^tθ+ν​ϕt​ℙ^tθ+ε​ϕ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐​d​t.\displaystyle d\left[\frac{\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{t}-\hat{\mathbb{P}}^{\theta}\_{t}}{\varepsilon}\right]=\frac{\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{t}-\hat{\mathbb{P}}^{\theta}\_{t}}{\varepsilon}\otimes d\hat{{P}}^{\theta}\_{t}+\nu\phi\_{t}\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{t}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\penalty 10000\ dt. |  |

Let us now define 𝕐t\mathbb{Y}\_{t} and βt\beta\_{t} by

|  |  |  |
| --- | --- | --- |
|  | 𝕐t:=ℙ^tθ+ε​ϕ−ℙ^tθε,βt=ν​ϕt​ℙ^tθ+ε​ϕ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐.\displaystyle\mathbb{Y}\_{t}:=\frac{\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{t}-\hat{\mathbb{P}}^{\theta}\_{t}}{\varepsilon},\quad\beta\_{t}=\nu\phi\_{t}\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{t}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}. |  |

Then, we have that

|  |  |  |
| --- | --- | --- |
|  | d​𝕐t=𝕐t​d​P^tθ+βt​d​t.\displaystyle d\mathbb{Y}\_{t}=\mathbb{Y}\_{t}\penalty 10000\ d\hat{{P}}^{\theta}\_{t}+\beta\_{t}dt. |  |

In this case, we observe that

|  |  |  |
| --- | --- | --- |
|  | d​(𝕐t⊗(ℙ^tθ)−1)=d​𝕐t⊗(ℙ^tθ)−1+𝕐t⊗d​(ℙ^tθ)−1,\displaystyle d\left(\mathbb{Y}\_{t}\otimes(\hat{\mathbb{P}}^{\theta}\_{t})^{-1}\right)=d\mathbb{Y}\_{t}\otimes(\hat{\mathbb{P}}^{\theta}\_{t})^{-1}+\mathbb{Y}\_{t}\otimes d(\hat{\mathbb{P}}^{\theta}\_{t})^{-1}, |  |

and thus

|  |  |  |
| --- | --- | --- |
|  | 𝕐t⊗(ℙ^tθ)−1=∫0tβs⊗(ℙ^sθ)−1​𝑑s.\displaystyle\mathbb{Y}\_{t}\otimes(\hat{\mathbb{P}}^{\theta}\_{t})^{-1}=\int\_{0}^{t}\beta\_{s}\otimes\left(\hat{\mathbb{P}}^{\theta}\_{s}\right)^{-1}ds. |  |

Thus, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕐t\displaystyle\mathbb{Y}\_{t} | =∫0tβs⊗(ℙ^sθ)−1⊗(ℙ^tθ)​𝑑s=∫0tβs⊗ℙ^s,tθ​𝑑s=ν​∫0t(ϕs​ℙ^sθ+ε​ϕ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗ℙ^s,tθ)​𝑑s.\displaystyle=\int\_{0}^{t}\beta\_{s}\otimes\left(\hat{\mathbb{P}}^{\theta}\_{s}\right)^{-1}\otimes\left(\hat{\mathbb{P}}^{\theta}\_{t}\right)ds=\int\_{0}^{t}\beta\_{s}\otimes\hat{\mathbb{P}}^{\theta}\_{s,t}ds=\nu\int\_{0}^{t}\left(\phi\_{s}\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{s}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\otimes\hat{\mathbb{P}}^{\theta}\_{s,t}\right)ds. |  |

By the Fubini’s theorem and dominated convergence theorem, since θ,ϕ,υ∈𝒜\theta,\phi,\upsilon\in\mathcal{A} and αt∈Tp​(ℝ2)\alpha\_{t}\in T^{p}(\mathbb{R}^{2}), we have that

|  |  |  |
| --- | --- | --- |
|  | limε→01ε​𝔼​(υt​⟨αt,ℙ^tθ+ε​ϕ−ℙ^tθ⟩)=ν​∫0tlimε→0𝔼​(ϕs​υt​⟨αt,ℙ^sθ+ε​ϕ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗ℙ^s,tθ⟩)​d​s.\lim\_{\varepsilon\to 0}\frac{1}{\varepsilon}\mathbb{E}\left(\upsilon\_{t}\langle\alpha\_{t},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon\phi}-\hat{\mathbb{P}}\_{t}^{\theta}\rangle\right)=\nu\int\_{0}^{t}\lim\_{\varepsilon\to 0}\mathbb{E}\left(\phi\_{s}\upsilon\_{t}\left\langle\alpha\_{t},\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{s}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\otimes\hat{\mathbb{P}}\_{s,t}^{\theta}\right\rangle\right)ds. |  |

Finally, as θ,ϕ,υ∈𝒜\theta,\phi,\upsilon\in\mathcal{A} and αt∈Tp​(ℝ2)\alpha\_{t}\in T^{p}(\mathbb{R}^{2}), we observe that there exists p~>1\tilde{p}>1 such that, for all s<t<Ts<t<T,

|  |  |  |
| --- | --- | --- |
|  | supε>0𝔼​(|ϕs​υt​⟨αt,ℙ^sθ+ε​ϕ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗ℙ^s,tθ⟩|p~)<∞,\sup\_{\varepsilon>0}\mathbb{E}\left(\left|\phi\_{s}\upsilon\_{t}\left\langle\alpha\_{t},\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{s}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\otimes\hat{\mathbb{P}}\_{s,t}^{\theta}\right\rangle\right|^{\tilde{p}}\right)<\infty, |  |

hence, (ϕs​υt​⟨αt,ℙ^sθ+ε​ϕ⊗\mathcolor​N​a​v​y​B​l​u​e​𝟐⊗ℙ^s,tθ⟩)ε>0\left(\phi\_{s}\upsilon\_{t}\left\langle\alpha\_{t},\hat{\mathbb{P}}^{\theta+\varepsilon\phi}\_{s}\otimes{\mathcolor{NavyBlue}{\mathbf{2}}}\otimes\hat{\mathbb{P}}\_{s,t}^{\theta}\right\rangle\right)\_{\varepsilon>0} is Lp~L^{\tilde{p}} bounded with p~>1\tilde{p}>1, and then uniformly integrable. Therefore, we deduce ([5.11](https://arxiv.org/html/2511.23295v1#S5.E11 "In Lemma 5.3. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
∎

### 7.2 Proof of Lemma [5.4](https://arxiv.org/html/2511.23295v1#S5.Thmthm4 "Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")

###### Proof.

First, we can rewrite the functional JJ as

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(θ)=\displaystyle J(\theta)= | −η​⟨θ,θ⟩L2+⟨μ+ν​θ,Xθ−⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩⟩L2−λ2​σ2​⟨Xθ−⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩,Xθ−⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩⟩L2\displaystyle-\eta\langle\theta,\theta\rangle\_{L\_{2}}+\langle\mu+\nu\theta,X^{\theta}-\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle\rangle\_{L\_{2}}-\frac{\lambda}{2}\sigma^{2}\langle X^{\theta}-\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle,X^{\theta}-\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle\rangle\_{L\_{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −η⟨θ,θ⟩L2+ν⟨θ,Xθ⟩L2−ν⟨θ,⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩⟩L2−λ2σ2⟨Xθ,Xθ⟩L2−λ2σ2⟨⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩,⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩⟩L2\displaystyle-\eta\langle\theta,\theta\rangle\_{L\_{2}}+\nu\langle\theta,X^{\theta}\rangle\_{L\_{2}}-\nu\langle\theta,\langle\xi.|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle\rangle\_{L\_{2}}-\frac{\lambda}{2}\sigma^{2}\langle X^{\theta},X^{\theta}\rangle\_{L\_{2}}-\frac{\lambda}{2}\sigma^{2}\langle\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle,\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle\rangle\_{L\_{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​σ2​⟨Xθ,⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩⟩L2+⟨μ,Xθ−⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩⟩L2\displaystyle+\lambda\sigma^{2}\langle X^{\theta},\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle\rangle\_{L\_{2}}+\langle\mu,X^{\theta}-\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle\rangle\_{L\_{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =:\displaystyle=: | ∑i=17Ji​(θ).\displaystyle\sum\_{i=1}^{7}J\_{i}(\theta). |  |

For i=1,…,7,i=1,...,7, let us compute the Gâteaux derivatives of JiJ\_{i} for h∈𝒜h\in\mathcal{A}, such that

|  |  |  |
| --- | --- | --- |
|  | ⟨∇Ji​(θ),h⟩L2:=limε→0Ji​(θ+ε​h)−Ji​(θ)ε.\langle\nabla J\_{i}(\theta),h\rangle\_{L\_{2}}:=\lim\_{\varepsilon\to 0}\frac{J\_{i}(\theta+\varepsilon h)-J\_{i}(\theta)}{\varepsilon}. |  |

First, we easily observe that

|  |  |  |
| --- | --- | --- |
|  | ⟨∇J1​(θ),h⟩L2=−2​η​⟨θ,h⟩L2,\displaystyle\langle\nabla J\_{1}(\theta),h\rangle\_{L\_{2}}=-2\eta\langle\theta,h\rangle\_{L\_{2}}, |  |
|  |  |  |
| --- | --- | --- |
|  | ⟨∇J4​(θ),h⟩L2=−λ​σ2​⟨∫.T𝔼​(Xsθ|ℱt)​𝑑s,h⟩L2.\displaystyle\langle\nabla J\_{4}(\theta),h\rangle\_{L\_{2}}=-\lambda\sigma^{2}\langle\int\_{.}^{T}\mathbb{E}(X^{\theta}\_{s}|\mathcal{F}\_{t})ds,h\rangle\_{L\_{2}}. |  |

Then, for i=2i=2, we get that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J2​(θ+ε​h)−J2​(θ)ε=\displaystyle\frac{J\_{2}(\theta+\varepsilon h)-J\_{2}(\theta)}{\varepsilon}= | 1ε​[ν​𝔼​(∫0T((θt+ε​ht)​Xtθ+ε​h)​𝑑t)−ν​𝔼​∫0T(θt​Xtθ​d​t)]\displaystyle\frac{1}{\varepsilon}\Bigg[\nu\mathbb{E}\left(\int\_{0}^{T}\left((\theta\_{t}+\varepsilon h\_{t})X\_{t}^{\theta+\varepsilon h}\right)dt\right)-\nu\mathbb{E}\int\_{0}^{T}\left(\theta\_{t}X\_{t}^{\theta}dt\right)\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1ε​ν​[𝔼​(∫0Tε​ht​Xtθ+ε​h​𝑑t)+𝔼​(∫0Tθt​(Xtθ+ε​h−Xtθ)​𝑑t)],\displaystyle\frac{1}{\varepsilon}\nu\left[\mathbb{E}\left(\int\_{0}^{T}\varepsilon h\_{t}X\_{t}^{\theta+\varepsilon h}dt\right)+\mathbb{E}\left(\int\_{0}^{T}\theta\_{t}\left(X\_{t}^{\theta+\varepsilon h}-X\_{t}^{\theta}\right)dt\right)\right], |  |

thus, by the tower property of the conditional expectation and Fubini’s theorem, taking limε→0\lim\_{\varepsilon\to 0} gives,

|  |  |  |
| --- | --- | --- |
|  | ⟨∇J2​(θ),h⟩L2=ν​⟨X.θ+∫.T𝔼​(θs|ℱ.)​𝑑s,h⟩L2.\displaystyle\langle\nabla J\_{2}(\theta),h\rangle\_{L\_{2}}=\nu\langle X\_{.}^{\theta}+\int\_{.}^{T}\mathbb{E}(\theta\_{s}|\mathcal{F}\_{.})ds,h\rangle\_{L\_{2}}. |  |

For i=3i=3,

|  |  |  |  |
| --- | --- | --- | --- |
|  | J3​(θ+ε​h)−J3​(θ)ε\displaystyle\frac{J\_{3}(\theta+\varepsilon h)-J\_{3}(\theta)}{\varepsilon} | =1ε​ν​[−𝔼​(∫0T(θt+ε​ht)​⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ+ε​h⟩​𝑑t)+𝔼​(∫0Tθt​⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩​𝑑t)]\displaystyle=\frac{1}{\varepsilon}\nu\left[-\mathbb{E}\left(\int\_{0}^{T}(\theta\_{t}+\varepsilon h\_{t})\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon h}\rangle dt\right)+\mathbb{E}\left(\int\_{0}^{T}\theta\_{t}\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta}\rangle dt\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−1ε​ν​𝔼​(∫0Tθt​(⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ+ε​h⟩−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)​𝑑t)−ν​⟨⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ+ε​h⟩,h⟩L2.\displaystyle=-\frac{1}{\varepsilon}\nu\mathbb{E}\left(\int\_{0}^{T}\theta\_{t}\left(\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon h}\rangle-\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta}\rangle\right)dt\right)-\nu\langle\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta+\varepsilon h}\_{.}\rangle,h\rangle\_{L\_{2}}. |  |

Since θ,h∈𝒜\theta,h\in\mathcal{A}, using Lemma [5.3](https://arxiv.org/html/2511.23295v1#S5.Thmthm3 "Lemma 5.3. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions"), the dominated convergence theorem and Fubini’s theorem, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→01ε​𝔼​(∫0Tθt​(⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ+ε​h⟩−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)​𝑑t)\displaystyle\lim\_{\varepsilon\to 0}\frac{1}{\varepsilon}\mathbb{E}\left(\int\_{0}^{T}\theta\_{t}\left(\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon h}\rangle-\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta}\rangle\right)dt\right) | =𝔼​(∫0Tht​∫tT𝔼​(θs​ν​Γt,sθ|ℱt)​𝑑s​𝑑t).\displaystyle=\mathbb{E}\left(\int\_{0}^{T}h\_{t}\int\_{t}^{T}\mathbb{E}\left(\theta\_{s}\nu\Gamma\_{t,s}^{\theta}|\mathcal{F}\_{t}\right)dsdt\right). |  |

Therefore, we infer that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨∇J3​(θ),h⟩L2\displaystyle\langle\nabla J\_{3}(\theta),h\rangle\_{L\_{2}} | =−ν​[⟨∫.T𝔼​(θs​ν​Γ.,sθ|ℱ.)​𝑑s+⟨ξ.|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^.θ⟩,h⟩L2].\displaystyle=-\nu\left[\langle\int\_{.}^{T}\mathbb{E}\left(\theta\_{s}\nu\Gamma\_{.,s}^{\theta}|\mathcal{F}\_{.}\right)ds+\langle\xi\_{.}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}^{\theta}\_{.}\rangle,h\rangle\_{L\_{2}}\right]. |  |

Using similar arguments, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J5​(θ+ε​h)−J5​(θ)ε\displaystyle\frac{J\_{5}(\theta+\varepsilon h)-J\_{5}(\theta)}{\varepsilon} | =−1ε​λ2​σ2​𝔼​(∫0T(⟨(ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2,ℙ^tθ+ε​h⟩−⟨(ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐)⊔⁣⊔2,ℙ^tθ⟩)​𝑑t),\displaystyle=-\frac{1}{\varepsilon}\frac{\lambda}{2}\sigma^{2}\mathbb{E}\left(\int\_{0}^{T}\left(\langle(\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon h}\rangle-\langle(\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}})^{\mathrel{\sqcup\mkern-3.2mu\sqcup}2},\hat{\mathbb{P}}\_{t}^{\theta}\rangle\right)dt\right), |  |

taking limε→0\lim\_{\varepsilon\to 0} leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0J5​(θ+ε​h)−J5​(θ)ε\displaystyle\lim\_{\varepsilon\to 0}\frac{J\_{5}(\theta+\varepsilon h)-J\_{5}(\theta)}{\varepsilon} | =−λ2​σ2​⟨∫.T𝔼​(ν​Γ~.,sθ|ℱ.)​𝑑s,h⟩L2.\displaystyle=-\frac{\lambda}{2}\sigma^{2}\langle\int\_{.}^{T}\mathbb{E}\left(\nu\tilde{\Gamma}\_{.,s}^{\theta}|\mathcal{F}\_{.}\right)ds,h\rangle\_{L\_{2}}. |  |

For i=6i=6, we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J6​(θ+ε​h)−J6​(θ)ε=\displaystyle\frac{J\_{6}(\theta+\varepsilon h)-J\_{6}(\theta)}{\varepsilon}= | λσ2[𝔼(∫0T⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ+ε​h⟩∫0thsdsdt)\displaystyle\lambda\sigma^{2}\bigg[\mathbb{E}\left(\int\_{0}^{T}\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon h}\rangle\int\_{0}^{t}h\_{s}dsdt\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1ε𝔼(∫0T(⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ+ε​h⟩−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩)Xtθdt)]\displaystyle+\frac{1}{\varepsilon}\mathbb{E}\left(\int\_{0}^{T}\left(\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon h}\rangle-\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta}\rangle\right)X\_{t}^{\theta}dt\right)\bigg] |  |

taking the limit limε→0\lim\_{\varepsilon\to 0} leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0J6​(θ+ε​h)−J6​(θ)ε\displaystyle\lim\_{\varepsilon\to 0}\frac{J\_{6}(\theta+\varepsilon h)-J\_{6}(\theta)}{\varepsilon} | =λ​σ2​⟨∫.T𝔼​(⟨ξs|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^sθ⟩+Xsθ​ν​Γ.,sθ|ℱ.)​𝑑s,h⟩L2.\displaystyle=\lambda\sigma^{2}\langle\int\_{.}^{T}\mathbb{E}\left(\langle\xi\_{s}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{s}^{\theta}\rangle+X\_{s}^{\theta}\nu\Gamma\_{.,s}^{\theta}|\mathcal{F}\_{.}\right)ds,h\rangle\_{L\_{2}}. |  |

Finally, for i=7i=7, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J7​(θ+ε​h)−J7​(θ)ε\displaystyle\frac{J\_{7}(\theta+\varepsilon h)-J\_{7}(\theta)}{\varepsilon} | =1ε​μ​[𝔼​∫0T((Xtθ+ε​h−Xtθ)−(⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ+ε​h⟩−⟨ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐,ℙ^tθ⟩))​𝑑t],\displaystyle=\frac{1}{\varepsilon}\mu\left[\mathbb{E}\int\_{0}^{T}\left((X\_{t}^{\theta+\varepsilon h}-X\_{t}^{\theta})-(\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta+\varepsilon h}\rangle-\langle\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}},\hat{\mathbb{P}}\_{t}^{\theta}\rangle)\right)dt\right], |  |

and using similar arguments, we obtain that

|  |  |  |
| --- | --- | --- |
|  | ⟨∇J7(θ),h⟩L2=μ⟨(T−.)−∫.T𝔼(νΓ.,sθ|ℱ.)ds,h⟩L2.\displaystyle\langle\nabla J\_{7}(\theta),h\rangle\_{L\_{2}}=\mu\langle(T-.)-\int\_{.}^{T}\mathbb{E}\left(\nu\Gamma\_{.,s}^{\theta}|\mathcal{F}\_{.}\right)ds,h\rangle\_{L\_{2}}. |  |

Taking all together, we finally get that

|  |  |  |
| --- | --- | --- |
|  | ⟨∇J​(θ),h⟩L2=∑i=17⟨∇Ji​(θ),h⟩L2=⟨−2​η​θ+ν​𝐀​θ−λ​σ2​𝐁​θ+μ​𝐂​θ,h⟩L2,\displaystyle\langle\nabla J(\theta),h\rangle\_{L\_{2}}=\sum\_{i=1}^{7}\langle\nabla J\_{i}(\theta),h\rangle\_{L\_{2}}=\langle-2\eta\theta+\nu\mathbf{A}\theta-\lambda\sigma^{2}\mathbf{B}\theta+\mu\mathbf{C}\theta,h\rangle\_{L\_{2}}, |  |

with the operators 𝐀\mathbf{A}, 𝐁\mathbf{B} and 𝐂\mathbf{C} defined by ([5.12](https://arxiv.org/html/2511.23295v1#S5.E12 "In Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) and ([5.13](https://arxiv.org/html/2511.23295v1#S5.E13 "In Lemma 5.4. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")).
∎

### 7.3 Proof of Proposition [5.6](https://arxiv.org/html/2511.23295v1#S5.Thmthm6 "Proposition 5.6. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")

Since ν=0\nu=0, then p=2p=2 and then the monotonicity condition reduces to

|  |  |  |
| --- | --- | --- |
|  | ⟨−(2​η−ε)​(θ−ϕ)−λ​σ2​(𝐁​(θ)−𝐁​(ϕ))+μ​(𝐂​(θ)−𝐂​(ϕ)),θ−ϕ⟩L2≤0.\left\langle-(2\eta-\varepsilon)(\theta-\phi)-\lambda\sigma^{2}\left(\mathbf{B}(\theta)-\mathbf{B}(\phi)\right)+\mu\left(\mathbf{C}(\theta)-\mathbf{C}(\phi)\right),\theta-\phi\right\rangle\_{L\_{2}}\leq 0. |  |

Moreover, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(𝐁​(θ)−𝐁​(ϕ)),θ−ϕ⟩L2\displaystyle\left\langle(\mathbf{B}(\theta)-\mathbf{B}(\phi)),\theta-\phi\right\rangle\_{L\_{2}} | =𝔼​(∫0T(Xtθ−Xtϕ)2​𝑑t)and⟨μ​(𝐂​(θ)−𝐂​(ϕ)),θ−ϕ⟩L2=0.\displaystyle=\mathbb{E}\left(\int\_{0}^{T}(X^{\theta}\_{t}-X^{\phi}\_{t})^{2}dt\right)\quad\text{and}\quad\left\langle\mu(\mathbf{C}(\theta)-\mathbf{C}(\phi)),\theta-\phi\right\rangle\_{L\_{2}}=0. |  |

Hence, for any ε>0\varepsilon>0 such that 0<ε<2​η0<\varepsilon<2\eta, we infer that

|  |  |  |
| --- | --- | --- |
|  | ⟨−(2​η−ε)​(θ−ϕ)−λ​σ2​(𝐁​(θ)−𝐁​(ϕ))+μ​(𝐂​(θ)−𝐂​(ϕ)),θ−ϕ⟩L2\displaystyle\left\langle-(2\eta-\varepsilon)(\theta-\phi)-\lambda\sigma^{2}\left(\mathbf{B}(\theta)-\mathbf{B}(\phi)\right)+\mu\left(\mathbf{C}(\theta)-\mathbf{C}(\phi)\right),\theta-\phi\right\rangle\_{L\_{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(−(2​η−ε))​𝔼​(∫0T(θt−ϕt)2​𝑑t)−λ​σ2​𝔼​(∫0T(Xtθ−Xtϕ)2​𝑑t)\displaystyle\leq\left(-(2\eta-\varepsilon)\right)\mathbb{E}\left(\int\_{0}^{T}(\theta\_{t}-\phi\_{t})^{2}dt\right)-\lambda\sigma^{2}\mathbb{E}\left(\int\_{0}^{T}(X\_{t}^{\theta}-X\_{t}^{\phi})^{2}dt\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤0\displaystyle\leq 0 |  |

and the monotonicity condition ([5.16](https://arxiv.org/html/2511.23295v1#S5.E16 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied.

### 7.4 Proof of Proposition [5.7](https://arxiv.org/html/2511.23295v1#S5.Thmthm7 "Proposition 5.7. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")

###### Proof.

First, since M~≤1\tilde{M}\leq 1, then p=2p=2 and the monotonicity condition reduces to

|  |  |  |
| --- | --- | --- |
|  | ⟨−(2​η−ε)​(θ−ϕ)+ν​(𝐀​(θ)−𝐀​(ϕ))−λ​σ2​(𝐁​(θ)−𝐁​(ϕ))+μ​(𝐂​(θ)−𝐂​(ϕ)),θ−ϕ⟩L2≤0.\left\langle-(2\eta-\varepsilon)(\theta-\phi)+\nu\left(\mathbf{A}(\theta)-\mathbf{A}(\phi)\right)-\lambda\sigma^{2}\left(\mathbf{B}(\theta)-\mathbf{B}(\phi)\right)+\mu\left(\mathbf{C}(\theta)-\mathbf{C}(\phi)\right),\theta-\phi\right\rangle\_{L\_{2}}\leq 0. |  |

Moreover, since ξt|\mathcolor​N​a​v​y​B​l​u​e​𝟐∈T≤1​(ℝ2)\xi\_{t}|\_{{\mathcolor{NavyBlue}{\mathbf{2}}}}\in T^{\leq 1}(\mathbb{R}^{2}), we observe that

|  |  |  |
| --- | --- | --- |
|  | Γt,sθ=ξs\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐,Γ~t,sθ=2​ξs\mathcolor​N​a​v​y​B​l​u​e​𝟐​ξs\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐+2​Psθ​(ξs\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐)2+2​ξs\mathcolor​N​a​v​y​B​l​u​e​𝟏𝟐​ξs\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟏​s.\displaystyle\Gamma\_{t,s}^{\theta}=\xi\_{s}^{{\mathcolor{NavyBlue}{\mathbf{22}}}},\quad\tilde{\Gamma}\_{t,s}^{\theta}=2\xi\_{s}^{{\mathcolor{NavyBlue}{\mathbf{2}}}}\xi\_{s}^{{\mathcolor{NavyBlue}{\mathbf{22}}}}+2P\_{s}^{\theta}\left(\xi\_{s}^{{\mathcolor{NavyBlue}{\mathbf{22}}}}\right)^{2}+2\xi\_{s}^{{\mathcolor{NavyBlue}{\mathbf{12}}}}\xi\_{s}^{{\mathcolor{NavyBlue}{\mathbf{21}}}}s. |  |

In this case, by Cauchy-Schwarz inequality, as we assume ([5.19](https://arxiv.org/html/2511.23295v1#S5.E19 "In Proposition 5.7. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")), we infer that

|  |  |  |
| --- | --- | --- |
|  | ⟨ν​(𝐀​(θ)−𝐀​(ϕ)),θ−ϕ⟩L2≤(2​η−ε)ν​𝔼​(∫0T(θt−ϕt)2​𝑑t),\displaystyle\left\langle\nu(\mathbf{A}(\theta)-\mathbf{A}(\phi)),\theta-\phi\right\rangle\_{L\_{2}}\leq\frac{(2\eta-\varepsilon)}{\nu}\mathbb{E}\left(\int\_{0}^{T}(\theta\_{t}-\phi\_{t})^{2}dt\right), |  |

as well as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(𝐁​(θ)−𝐁​(ϕ)),θ−ϕ⟩L2\displaystyle\left\langle(\mathbf{B}(\theta)-\mathbf{B}(\phi)),\theta-\phi\right\rangle\_{L\_{2}} | =𝔼​(∫0T(1−ν​ξt\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐)2​(Xtθ−Xtϕ)2​𝑑t),\displaystyle=\mathbb{E}\left(\int\_{0}^{T}(1-\nu\xi\_{t}^{{\mathcolor{NavyBlue}{\mathbf{22}}}})^{2}(X^{\theta}\_{t}-X^{\phi}\_{t})^{2}dt\right), |  |

and finally

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨μ​(𝐂​(θ)−𝐂​(ϕ)),θ−ϕ⟩L2\displaystyle\left\langle\mu(\mathbf{C}(\theta)-\mathbf{C}(\phi)),\theta-\phi\right\rangle\_{L\_{2}} | =0.\displaystyle=0. |  |

Hence, we readily infer that

|  |  |  |
| --- | --- | --- |
|  | ⟨−(2​η−ε)​(θ−ϕ)+ν​(𝐀​(θ)−𝐀​(ϕ))−λ​σ2​(𝐁​(θ)−𝐁​(ϕ))+μ​(𝐂​(θ)−𝐂​(ϕ)),θ−ϕ⟩L2\displaystyle\left\langle-(2\eta-\varepsilon)(\theta-\phi)+\nu\left(\mathbf{A}(\theta)-\mathbf{A}(\phi)\right)-\lambda\sigma^{2}\left(\mathbf{B}(\theta)-\mathbf{B}(\phi)\right)+\mu\left(\mathbf{C}(\theta)-\mathbf{C}(\phi)\right),\theta-\phi\right\rangle\_{L\_{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤−λ​σ2​𝔼​(∫0T(1−ν​ξt\mathcolor​N​a​v​y​B​l​u​e​𝟐𝟐)2​(Xtθ−Xtϕ)2​𝑑t)\displaystyle\leq-\lambda\sigma^{2}\mathbb{E}\left(\int\_{0}^{T}(1-\nu\xi\_{t}^{{\mathcolor{NavyBlue}{\mathbf{22}}}})^{2}(X\_{t}^{\theta}-X\_{t}^{\phi})^{2}dt\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤0,\displaystyle\leq 0, |  |

and therefore the monotonicity condition ([5.16](https://arxiv.org/html/2511.23295v1#S5.E16 "In Theorem 5.5. ‣ 5.1 Existence and uniqueness result ‣ 5 Mean-quadratic variation hedging with market impact ‣ Signature approach for pricing and hedging path-dependent options with frictions")) is satisfied.
∎

## Conflicts of Interest

The authors declare no conflicts of interest.

## Data Availability Statement

Data sharing is not applicable to this article as no new data were created or analyzed in this study.

## References

* Abi Jaber and Gérard (2025a)

  Eduardo Abi Jaber and Louis-Amand Gérard.
  Signature volatility models: pricing and hedging with Fourier.
  *SIAM Journal on Financial Mathematics*, 16(2):606–642, 2025a.
* Abi Jaber and Gérard (2025b)

  Eduardo Abi Jaber and Louis-Amand Gérard.
  Hedging with memory: shallow and deep learning with signatures.
  *arXiv preprint arXiv:2508.02759*, 2025b.
* Abi Jaber et al. (2024a)

  Eduardo Abi Jaber, Louis-Amand Gérard, and Yuxing Huang.
  Path-dependent processes from signatures.
  *arXiv preprint arXiv:2407.04956*, 2024a.
* Abi Jaber et al. (2024b)

  Eduardo Abi Jaber, Shaun Li, and Lin.
  Fourier-Laplace transforms in polynomial Ornstein-Uhlenbeck volatility models.
  *arXiv preprint arXiv:2405.02170, to appear in Finance and Stochastics*, 2024b.
* Almgren and Li (2016)

  Robert Almgren and Tianhui Michael Li.
  Option hedging with smooth market impact.
  *Market microstructure and liquidity*, 2(01):1650002, 2016.
* Bank et al. (2017)

  Peter Bank, H Mete Soner, and Moritz Voß.
  Hedging with temporary price impact.
  *Mathematics and financial economics*, 11:215–239, 2017.
* Bank et al. (2025)

  Peter Bank, Christian Bayer, Paul P Hager, Sebastian Riedel, and Tobias Nauen.
  Stochastic control with signatures.
  *SIAM Journal on Control and Optimization*, 63(5):3189–3218, 2025.
* Bayer et al. (2023)

  Christian Bayer, Paul P Hager, Sebastian Riedel, and John Schoenmakers.
  Optimal stopping with signatures.
  *The Annals of Applied Probability*, 33(1):238–273, 2023.
* Bayer et al. (2025a)

  Christian Bayer, Luca Pelizzari, and John Schoenmakers.
  Primal and dual optimal stopping with signatures.
  *Finance and Stochastics*, pages 1–34, 2025a.
* Bayer et al. (2025b)

  Christian Bayer, Luca Pelizzari, and Jia-Jie Zhu.
  Pricing american options under rough volatility using deep-signatures and signature-kernels.
  *arXiv preprint arXiv:2501.06758*, 2025b.
* Becherer and Bilarev (2018)

  Dirk Becherer and Todor Bilarev.
  *Hedging with transient price impact for non-covered and covered options*.
  SSRN, 2018.
* Ben Arous (1989)

  Gérard Ben Arous.
  Flots et séries de Taylor stochastiques.
  *Probability Theory and Related Fields*, 81(1):29–77, 1989.
* Bouchard et al. (2017)

  Bruno Bouchard, Grégoire Loeper, and Yiyi Zou.
  Hedging of covered options with linear market impact and gamma constraint.
  *SIAM Journal on Control and Optimization*, 55(5):3319–3348, 2017.
* Cetin et al. (2010)

  Umut Cetin, H Mete Soner, and Nizar Touzi.
  Option hedging for small investors under liquidity costs.
  *Finance and Stochastics*, 14(3):317–341, 2010.
* Chen (1957)

  Kuo-Tsai Chen.
  Integration of paths, geometric invariants and a generalized Baker-Hausdorff formula.
  *Annals of Mathematics*, 65(1):163–178, 1957.
* Chen (1977)

  Kuo-Tsai Chen.
  Iterated path integrals.
  *Bulletin of the American Mathematical Society*, 83(5):831–879, 1977.
* Cuchiero and Möller (2025)

  Christa Cuchiero and Janka Möller.
  Signature methods in stochastic portfolio theory.
  *SIAM Journal on Financial Mathematics*, 16(4):1239–1303, 2025.
* Cuchiero et al. (2023)

  Christa Cuchiero, Sara Svaluto-Ferro, and Josef Teichmann.
  Signature sdes from an affine and polynomial perspective.
  *arXiv preprint arXiv:2302.01362*, 2023.
* Cuchiero et al. (2025a)

  Christa Cuchiero, Guido Gazzani, Janka Möller, and Sara Svaluto-Ferro.
  Joint calibration to SPX and VIX options with signature-based models.
  *Mathematical Finance*, 35(1):161–213, 2025a.
* Cuchiero et al. (2025b)

  Christa Cuchiero, Francesca Primavera, and Sara Svaluto-Ferro.
  Universal approximation theorems for continuous functions of cadlag paths and Lévy-type signature models.
  *Finance and Stochastics*, pages 1–54, 2025b.
* Ekeland and Temam (1999)

  Ivar Ekeland and Roger Temam.
  *Convex analysis and variational problems*.
  SIAM, 1999.
* Ekren and Nadtochiy (2022)

  Ibrahim Ekren and Sergey Nadtochiy.
  Utility-based pricing and hedging of contingent claims in Almgren-Chriss model with temporary price impact.
  *Mathematical Finance*, 32(1):172–225, 2022.
* Fawcett (2003)

  Thomas Fawcett.
  *Problems in stochastic analysis. Connections between rough paths and non-commutative harmonic analysis*.
  PhD thesis, University of Oxford, 2003.
* Futter et al. (2023)

  Owen Futter, Blanka Horvath, and Magnus Wiese.
  Signature trading: A path-dependent extension of the mean-variance framework with exogenous signals.
  *arXiv preprint arXiv:2308.15135*, 2023.
* Guéant and Pu (2017)

  Olivier Guéant and Jiang Pu.
  Option pricing and hedging with execution costs and market impact.
  *Mathematical Finance*, 27(3):803–831, 2017.
  doi: 10.1111/mafi.12102.
* Guéant et al. (2015)

  Olivier Guéant, Jiang Pu, and Guillaume Royer.
  Accelerated share repurchase: pricing and execution strategy.
  *International Journal of Theoretical and Applied Finance*, 18(03):1550019, 2015.
* Jaimungal et al. (2017)

  Sebastian Jaimungal, Damir Kinzebulatov, and DH Rubisov.
  Optimal accelerated share repurchases.
  *Applied Mathematical Finance*, 24(3):216–245, 2017.
* Kalsi et al. (2020)

  Jasdeep Kalsi, Terry Lyons, and Imanol Perez Arribas.
  Optimal execution with rough path signatures.
  *SIAM Journal on Financial Mathematics*, 11(2):470–493, 2020.
* Lions and Lasry (2007)

  Pierre-Louis Lions and Jean-Michel Lasry.
  Large investor trading impacts on volatility. Annales de l’IHP Analyse non linéaire. vol. 24, no. 2, pp. 311-323, 2007.
* Loeper (2018)

  Gregoire Loeper.
  Option pricing with linear market impact and nonlinear Black–Scholes equations.
  *The Annals of Applied Probability*, 28(5):2664–2726, 2018.
* Lyons et al. (2020)

  Terry Lyons, Sina Nejad, and Imanol Perez Arribas.
  Non-parametric pricing and hedging of exotic derivatives.
  *Applied Mathematical Finance*, 27(6):457–494, 2020.
* Rogers and Singh (2010)

  Leonard CG Rogers and Surbjeet Singh.
  The cost of illiquidity and its effects on hedging.
  *Mathematical Finance: An International Journal of Mathematics, Statistics and Financial Economics*, 20(4):597–615, 2010.
* Said (2019)

  Emilio Said.
  How option hedging shapes market impact.
  *arXiv preprint arXiv:1910.05056*, 2019.