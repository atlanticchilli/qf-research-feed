---
authors:
- Albina Danilova
- Valentin Lizhdvoy
doc_id: arxiv:2512.05011v1
family_id: arxiv:2512.05011
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Risk aversion of insider and dynamic asymmetric information.
url_abs: http://arxiv.org/abs/2512.05011v1
url_html: https://arxiv.org/html/2512.05011v1
venue: arXiv q-fin
version: 1
year: 2025
---


Albina Danilova
Department of Mathematics, London School of Economics and Political Science, 10 Houghton St., London, WC2A 2AE
[a.danilova@lse.ac.uk](mailto:a.danilova@lse.ac.uk)
 and 
Valentin Lizhdvoy
Department of Mathematics, Higher School of Economics
[valentin.lizhdvoj@mail.ru](mailto:valentin.lizhdvoj@mail.ru)

(Date: December 4, 2025)

###### Abstract.

This paper studies a Kyle-Back model with a risk-averse insider possessing exponential utility and a dynamic stochastic signal about the asset’s terminal fundamental value. While the existing literature considers either risk-neutral insiders with dynamic signals or risk-averse insiders with static signals, we establish equilibrium when both features are present. Our approach imposes no restrictions on the magnitude of the risk aversion parameter, extending beyond previous work that requires sufficiently small risk aversion. We employ a weak conditioning methodology to construct a Schrödinger bridge between the insider’s signal and the asset price process, an approach that naturally accommodates stochastic signal evolution and removes risk aversion constraints.

We derive necessary conditions for equilibrium, showing that the optimal insider strategy must be continuous with bounded variation. Under these conditions, we characterize the market-maker pricing rule and insider strategy that achieve equilibrium. We obtain explicit closed-form solutions for important cases including deterministic and quadratic signal volatilities, demonstrating the tractability of our framework.

## 1. Introduction

The canonical model of markets with asymmetric information is due to Kyle, which introduced a discrete-time model of insider trading and derived its continuous-time equilibrium as a limiting case. The continuous-time framework was formalized by Back92, establishing the Kyle-Back model. In this type of models there are typically three types of agents participating in the market: non-strategic noise traders, a strategic informed trader (insider) with private information regarding the future fundamental value of the asset, and risk-neutral market makers competing for the total demand. The goal of market makers is to set the pricing rule so that the resulting price is rational. The objective of the insider is to maximize her expected utility given the pricing rule set by the market makers. Thus, this type of modeling can be viewed as a game with asymmetric information between the market makers and the insider and the goal is to find an equilibrium of this game.

The majority of papers in the Kyle-Back literature consider the case when the insider is risk-neutral (see, e.g., HSmult, BCWmult,
CD-GKB). By contrast, the setting of a risk-averse insider with non-linear utility has received significantly less attention despite its economic importance. Early work on risk-averse insiders focused exclusively on models with Gaussian signals (Bar02, ChoRA), a significantly restrictive assumption. This limitation was relaxed in the work of BERA23, who used a fixed point approach coupled with the Fokker-Planck equation and a quasilinear PDE to study models with non-Gaussian insider signals and proved the existence of equilibrium for a broad class of such signals. However, only static type of insider signal was discussed in their work, where the insider knows the asset fundamental value from the onset of trading. Moreover, their approach requires the risk aversion parameter to be sufficiently small for the contraction mapping argument to succeed. BERA24 extended this framework to a multidimensional setting with multiple risky assets, again using the fixed-point methodology with static signals and restricted risk aversion.

The cases of dynamic insider signal, when the fundamental value of the traded asset is revealed through a stochastic process, have so far been studied only for the risk-neutral insider (BP98, D, CCDbp, CCDdef).

To the best of our knowledge, this paper is the first analysis of a Kyle-Back type model with risk-averse insider having exponential utility function and stochastic dynamic signal about the asset fundamental value. Thus, such framework generalizes the previous results for the static insider signal making them a particular case of our setting. Moreover, our method imposes no restrictions on the magnitude of the risk aversion parameter γ\gamma, whereas the fixed-point approach requires it to be sufficiently small.

A key contribution of our work lies in the methodological approach and in the technique used to prove the existence of the equilibrium. Whereas BERA23 and BERA24 relied on a fixed point construction coupling the Fokker-Planck equation with a quasilinear PDE, subject to an optimal transport constraint at maturity, our proof is based on the weak conditioning approach. This method constructs a Schrödinger bridge via weak conditioning between the stochastic processes representing insider signal and the asset price process, closely related to entropic optimal transport on path space. This approach naturally accommodates the evolution of information over time, while extending the fixed-point methodology to handle stochastic signal dynamics would require additional technical machinery.

Our main results can be summarized as follows. First, we characterize the market-maker weight function and insider trading strategy that yield the model equilibrium. The existence of equilibrium is demonstrated by constructing a Schrodinger bridge via weak conditioning between the stochastic processes representing the insider signal and the asset price process. Second, we show that the optimal insider strategy must be continuous with bounded variation and that in equilibrium there should be no jump in the asset price and at maturity the price process converges to the signal process. Third, we obtain explicit closed-form equilibrium solutions in particular cases including deterministic and quadratic signal volatilities, enabling comparative statics analysis across different levels of risk aversion.

The paper is structured in the following way. Section 2 introduces the model, specifies the market participants and formulates the market-maker pricing rule along with the insider’s utility optimization problem. Section 3 defines admissible pricing rules, admissible insider strategies and model equilibrium. Section 4 presents the main theoretical results of the work – the Theorem [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") and Lemma [4.2](https://arxiv.org/html/2512.05011v1#S4.Thmlemma2 "Lemma 4.2. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information."), which identify the necessary conditions for the equilibrium and describe under what pricing rule and insider strategy it can be achieved. Section 5 illustrates the theoretical results from Section 4 with particular cases, where an equilibrium can be obtained in closed form.

## 2. Description of the market model

In our model we will assume that all processes are defined on the filtered probability space

|  |  |  |
| --- | --- | --- |
|  | (Ω,ℱ,{ℱt}t∈[0,1],ℚb​a​s​e)\left(\Omega,{\mathcal{F}},\{{\mathcal{F}}\_{t}\}\_{t\in[0,1]},\mathbb{Q}^{base}\right) |  |

satisfying the usual conditions. Moreover, this space is assumed to be large enough to support two independent Brownian motions BB and β\beta as well as a standard normal random variable, Z0Z\_{0}, independent of σ​(B,β)\sigma(B,\beta).

The financial market we study consists of a risk-less and a risky asset, both traded continuously on the interval [0,1][0,1]. The price of the risk-less asset is normalized to be a constant, whereas the price of the risky asset is determined in the equilibrium. At the time 11 the fundamental value of the risky asset, VV, will be released. It is given by V=Z1V=Z\_{1} where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt=ηV​(t)Z\_{t}=\eta\_{V(t)} |  | (2.1) |

with η\eta being the unique strong solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt=∫0ta​(s,ηs)​𝑑βs.\eta\_{t}=\int\_{0}^{t}a(s,\eta\_{s})d\beta\_{s}. |  | (2.2) |

In the rest of the paper we impose the following conditions on the structure of the fundamental signal:

###### Assumption 2.1.

There exists unique strong solution to ([2.2](https://arxiv.org/html/2512.05011v1#S2.E2 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")) on [0,1][0,1] with the state space I:=(l,u)I:=(l,u) with l,u∈ℝ¯l,u\in\bar{\mathbb{R}} and 0∈I0\in I that admits a transition density and

1. (1)

   a∈C1,2​([0,1],I)a\in C^{1,2}([0,1],I) is positive,
   satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ata2​(t,x)+ax​x2​(t,x)=−γ\frac{a\_{t}}{a^{2}}(t,x)+\frac{a\_{xx}}{2}(t,x)=-\gamma |  | (2.3) |

   and for any tt the function ∫0x1a​(t,y)​𝑑y,x∈I\int\_{0}^{x}\frac{1}{a(t,y)}dy,\hskip 5.69054ptx\in I has the whole ℝ\mathbb{R} as its range.
2. (2)

   σ​(s)\sigma(s) is continuous on [0,1][0,1] and is separated from 0. Moreover, it satisfies the following conditions:

   1. (a)

      V​(t):=v0+∫0tσ2​(s)​𝑑s,v0≥0V(t):=v\_{0}+\int\_{0}^{t}\sigma^{2}(s)ds,v\_{0}\geq 0 satisfies V​(1)=1V(1)=1 and V​(t)>tV(t)>t on [0,1)[0,1),
   2. (b)

      limt→1D2​(t)​Λ​(t)​log⁡Λ​(t)=0\lim\_{t\to 1}D^{2}(t)\Lambda(t)\log{\Lambda(t)}=0 where D​(t)=exp⁡{−∫0t1V​(s)−s​𝑑s}D(t)=\exp\left\{-\int\_{0}^{t}\frac{1}{V(s)-s}ds\right\} and Λ​(t)=∫0t1+σ2​(s)D2​(s)​𝑑s\Lambda(t)=\int\_{0}^{t}\frac{1+\sigma^{2}(s)}{D^{2}(s)}ds.

###### Remark 1.

Note that the condition ([2.3](https://arxiv.org/html/2512.05011v1#S2.E3 "In item 1 ‣ Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")) does not necessarily require that the signal must have the volatility satisfying the PDE. Indeed, as it is shown in Section [5.1](https://arxiv.org/html/2512.05011v1#S5.SS1 "5.1. Deterministic volatility of the signal ‣ 5. Examples ‣ Risk aversion of insider and dynamic asymmetric information.") any signal with deterministic volatility can be represented as a signal satisfying condition ([2.3](https://arxiv.org/html/2512.05011v1#S2.E3 "In item 1 ‣ Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")). Thus, this constraint postulates that the signal can be represented in this form rather than requiring that it is given in this form.

###### Remark 2.

Note that the assumption that η0=0\eta\_{0}=0 is without loss of generality. Indeed, if η0\eta\_{0} is some constant different from 0, one can shift the process ηt\eta\_{t} by the η0\eta\_{0} and modify a​(t,x)a(t,x) to a​(t,x−η0)a(t,x-\eta\_{0}). Then the process ZZ will have the representation given by ([2.1](https://arxiv.org/html/2512.05011v1#S2.E1 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information."))-([2.2](https://arxiv.org/html/2512.05011v1#S2.E2 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")).

Moreover, as

|  |  |  |
| --- | --- | --- |
|  | ηV​(t)=∫0V​(t)a​(s,ηs)​𝑑βs,\eta\_{V(t)}=\int\_{0}^{V(t)}a(s,\eta\_{s})d\beta\_{s}, |  |

by employing a time change one can obtain

|  |  |  |
| --- | --- | --- |
|  | d​Zs=σ​(s)​a​(V​(s),Zs)​d​β~s,dZ\_{s}=\sigma(s)a(V(s),Z\_{s})d\tilde{\beta}\_{s}, |  |

where β~s\tilde{\beta}\_{s} is the time-changed Brownian motion defined by β~s=∫0s1σ​(u)​𝑑βV​(u)\tilde{\beta}\_{s}=\int\_{0}^{s}\frac{1}{\sigma(u)}d\beta\_{V(u)}.

This yields

|  |  |  |
| --- | --- | --- |
|  | Zt=Z0+∫0tσ​(s)​a​(V​(s),Zs)​𝑑β~s,Z0=ηV​(0)=∫0V​(0)a​(t,ηt)​𝑑βt,Z\_{t}=Z\_{0}+\int\_{0}^{t}\sigma(s)a(V(s),Z\_{s})d\tilde{\beta}\_{s},\hskip 14.22636ptZ\_{0}=\eta\_{V(0)}=\int\_{0}^{V(0)}a(t,\eta\_{t})d\beta\_{t}, |  |

which can be viewed as an alternative representation of the insider signal.

There are three types of agents populating the market: noise trader, market maker and insider. They are differentiated not only by their optimization problems, but also by the information they have access to, hence by filtrations their actions are adapted to. In particular:

*Noise Traders* trade for reasons other than maximizing their utilities, and we assume that their cumulative demand follows a standard Brownian motion, BB.

*Market Maker* observes total cumulated orders, Yt=θt+BtY\_{t}=\theta\_{t}+B\_{t}, where θt\theta\_{t} is the insider’s cumulated order by time tt.
The market maker’s filtration at time tt, ℱtM{\mathcal{F}}\_{t}^{M}, is defined as ℱtM:=ℱtY{\mathcal{F}}\_{t}^{M}:={\mathcal{F}}\_{t}^{Y} for t∈[0,1)t\in[0,1) and ℱ1M:=ℱ1Y,Z{\mathcal{F}}\_{1}^{M}:={\mathcal{F}}\_{1}^{Y,Z}.

The market maker sets the asset price, PP, which in principle can depend on the whole path of YY. We will restrict our attention to the price processes of the form

|  |  |  |
| --- | --- | --- |
|  | Pt=ξt+c​ for any ​t∈[0,1]P\_{t}=\xi\_{t}+c\mbox{ for any }t\in[0,1] |  |

where c∈ℝc\in\mathbb{R} is a constant and ξ\xi satisfies the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ξt=w​(t,ξt−)​d​Ytc+d​Ct+Jt,ξ0=0a.s.,d\xi\_{t}=w(t,\xi\_{t-})dY\_{t}^{c}+dC\_{t}+J\_{t},\quad\xi\_{0}=0\quad a.s., |  | (2.4) |

where

|  |  |  |
| --- | --- | --- |
|  | d​Ct=wx​(t,ξt−)2​w​(t,ξt−)​(d​[Y,Y]tc−d​t),dC\_{t}=\frac{w\_{x}(t,\xi\_{t-})}{2}w(t,\xi\_{t-})\left(d[Y,Y]\_{t}^{c}-dt\right), |  |

|  |  |  |
| --- | --- | --- |
|  | Jt=Kw−1​(t,Kw​(t,ξt−)+Δ​Yt)−ξt−,Kw​(t,x)=∫0x1w​(t,y)​𝑑y+∫0twx​(s,0)2​𝑑s.J\_{t}=K\_{w}^{-1}(t,K\_{w}(t,\xi\_{t-})+\Delta Y\_{t})-\xi\_{t-},\quad K\_{w}(t,x)=\int\_{0}^{x}\frac{1}{w(t,y)}dy+\int\_{0}^{t}\frac{w\_{x}(s,0)}{2}ds. |  |

This pricing rule was initially proposed in Cetin, Danilova (2021) as a generalization of previous pricing rules, which does not lead to infinite insider profit. Moreover, we can notice that if insider strategy is absolutely continuous, then this SDE will have the form

|  |  |  |
| --- | --- | --- |
|  | d​ξt=w​(t,ξt)​d​Yt.d\xi\_{t}=w(t,\xi\_{t})dY\_{t}. |  |

In above ww is called weighting function which satisfies admissibility conditions of Definition ([3.1](https://arxiv.org/html/2512.05011v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3. Admissibility and Equilibrium ‣ Risk aversion of insider and dynamic asymmetric information.")).
These admissibility conditions, together with the ones imposed on θ\theta in Definition ([3.3](https://arxiv.org/html/2512.05011v1#S3.Thmdefinition3 "Definition 3.3. ‣ 3. Admissibility and Equilibrium ‣ Risk aversion of insider and dynamic asymmetric information.")) will ensure that SDE ([2.4](https://arxiv.org/html/2512.05011v1#S2.E4 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")) admits a unique strong Markov solution.

Consider P0,zP^{0,z} – the time 0 law of the process (ξ,Z)(\xi,Z) starting from (0,z)(0,z). Then the market maker’s measure ℙ\mathbb{P}, defined on (Ω,ℱ1Y,Z)\left(\Omega,{\mathcal{F}}\_{1}^{Y,Z}\right), is given by

|  |  |  |
| --- | --- | --- |
|  | ℙ​(E)=∫ℝP0,z​(E)​μ​(d​z),∀E∈ℱ1Y,Z.\mathbb{P}(E)=\int\_{\mathbb{R}}P^{0,z}(E)\mu(dz),\quad\forall E\in{\mathcal{F}}\_{1}^{Y,Z}. |  |

*Insider* observes the price process PP and signal process ZZ up to any time tt, thus, her filtration is given by ℱtI=ℱ1P,Z{\mathcal{F}}\_{t}^{I}={\mathcal{F}}\_{1}^{P,Z}. Insider’s objective is to maximise the expected utility of final wealth, i.e.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supθ∈𝒜​(w,c)𝔼0,z​[−1γ​exp⁡{−γ​W1θ}],\sup\_{\theta\in{\mathcal{A}}(w,c)}\mathbb{E}^{0,z}\left[-\frac{1}{\gamma}\exp\left\{-\gamma W\_{1}^{\theta}\right\}\right], |  | (2.5) |

where γ\gamma is given in ([2.3](https://arxiv.org/html/2512.05011v1#S2.E3 "In item 1 ‣ Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")) and 𝒜​(w,c){\mathcal{A}}(w,c) is the set of admissible trading strategies for pricing rule (w,c)(w,c) specified in Definition ([3.3](https://arxiv.org/html/2512.05011v1#S3.Thmdefinition3 "Definition 3.3. ‣ 3. Admissibility and Equilibrium ‣ Risk aversion of insider and dynamic asymmetric information.")). The expectation is taken under the measure P0,zP^{0,z} defined above.

We denote by W1θW^{\theta}\_{1} an insider’s wealth at terminal time if she chooses to follow the trading strategy θ\theta. It is comprised of the continuous gain over the time interval [0,1)[0,1) and gain from the possible price discrepancy at terminal time t=1t=1, i.e.

|  |  |  |
| --- | --- | --- |
|  | W1θ=∫01−θt−​𝑑Pt+(Z1−P1−)​θ1−.W\_{1}^{\theta}=\int\_{0}^{1-}\theta\_{t-}dP\_{t}+(Z\_{1}-P\_{1-})\theta\_{1-}. |  |

## 3. Admissibility and Equilibrium

The above market model suggests a feedback mechanism for the insider, as her trading strategy will be reflected upon the asset price which in turn will influence her trading strategy itself. In this paper, we focus on finding the equilibrium of such market model in the following sense:

1. (1)

   given the pricing rule, insider’s trading strategy is optimal;
2. (2)

   given the trading strategy, there exists a unique strong solution for SDE ([2.4](https://arxiv.org/html/2512.05011v1#S2.E4 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")) over [0,1)[0,1) and the pricing rule is rational, i.e., martingale over [0,1)[0,1).

To formalize the definition of equilibrium and rational pricing, we need to define the sets of admissible pricing rules and admissible trading strategies.

###### Definition 3.1.

An admissible pricing rule is a measurable weighting function ww and a constant c:

1. (1)

   ww is defined on [0,1]×I[0,1]\times I, where II is given in Assumption [2.1](https://arxiv.org/html/2512.05011v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.").
2. (2)

   w∈𝒞1,2​([0,1]×I)w\in{\mathcal{C}}^{1,2}\left([0,1]\times I\right) and is positive.
3. (3)

   The weighting function satisfies:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | wtw2​(t,ξ)+wξ​ξ​(t,ξ)2=−γ.\frac{w\_{t}}{w^{2}}(t,\xi)+\frac{w\_{\xi\xi}(t,\xi)}{2}=-\gamma. |  | (3.6) |
4. (4)

   There exists a unique strong solution ξ\xi to the SDE

   |  |  |  |
   | --- | --- | --- |
   |  | d​ξt=w​(t,ξt)​d​Bt,ξ0=0a.s.d\xi\_{t}=w(t,\xi\_{t})dB\_{t},\quad\xi\_{0}=0\quad a.s. |  |

   in (Ω,ℱ,(ℱt)t∈[0,1),ℚb​a​s​e)\left(\Omega,{\mathcal{F}},({\mathcal{F}}\_{t})\_{t\in[0,1)},\mathbb{Q}^{base}\right).

###### Remark 3.

It can be shown, following the methodology developed in CD-GKB, that in order for the equilibrium to exist the weighting function ww should satisfy ([3.6](https://arxiv.org/html/2512.05011v1#S3.E6 "In item 3 ‣ Definition 3.1. ‣ 3. Admissibility and Equilibrium ‣ Risk aversion of insider and dynamic asymmetric information.")). Thus, the condition (3) is necessary for the existence of equilibrium.

###### Remark 4.

The condition (4), in essence, states that the market maker should chose the weighting function such that the market price is well defined if insider refrains from trading.

###### Definition 3.2.

We will call an admissible pricing rule rational if it satisfies

|  |  |  |
| --- | --- | --- |
|  | Pt=𝔼​[Zt|ℱtY]P\_{t}=\mathbb{E}\left[Z\_{t}\left|{\mathcal{F}}\_{t}^{Y}\right.\right] |  |

for a given admissible trading strategy θ\theta.

Next, we turn to the definition of insider’s admissible strategy. The minimal requirement for the admissibility is that the market price is well defined, i.e. SDE ([2.4](https://arxiv.org/html/2512.05011v1#S2.E4 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")) has the unique strong solution. Whereas the definition of admissible pricing rule ensures that the market price is well defined in the absence of the insider trading, the insider can only choose a trading strategy that results in the unique price. Thus, the set of insider’s admissible strategies is determined by the admissible pricing rule chosen by the market maker. The formal definition is as follows.

###### Definition 3.3.

Given an admissible pricing rule ww, an admissible insider’s trading strategy (denoted as θ∈𝒜​(w)\theta\in{\mathcal{A}}(w)) is ℱξ,Z{\mathcal{F}}^{\xi,Z} adapted process satisfying:

1. (1)

   θ\theta is a semi-martingale with summable jumps on the filtration produced by BB and ZZ.
2. (2)

   There exists a unique strong solution of SDE ([2.4](https://arxiv.org/html/2512.05011v1#S2.E4 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")) in (Ω,ℱ,(ℱt)t∈[0,1),ℚb​a​s​e)\left(\Omega,{\mathcal{F}},({\mathcal{F}}\_{t})\_{t\in[0,1)},\mathbb{Q}^{base}\right).
3. (3)

   (ξ,Z)(\xi,Z) is a Markov process adapted to (ℱt)t∈[0,1)({\mathcal{F}}\_{t})\_{t\in[0,1)} with measure P0,zP^{0,z};
4. (4)

   𝔼0,z​[exp⁡{−γ​∫01Pt​𝑑Bt−γ22​∫01Pt2​𝑑t}]=1\mathbb{E}^{0,z}\left[\exp\left\{-\gamma\int\_{0}^{1}P\_{t}dB\_{t}-\frac{\gamma^{2}}{2}\int\_{0}^{1}P\_{t}^{2}dt\right\}\right]=1.

###### Definition 3.4.

A pair ((w,c),θ)((w,c),\theta) is an equilibrium if (w,c)(w,c) is an admissible pricing rule, θ\theta is an admissible insider strategy and:

1. (1)

   Given θ\theta, (w,c)(w,c) is rational pricing rule (according to the Definition ([3.2](https://arxiv.org/html/2512.05011v1#S3.Thmdefinition2 "Definition 3.2. ‣ 3. Admissibility and Equilibrium ‣ Risk aversion of insider and dynamic asymmetric information.")));
2. (2)

   Given (w,c)(w,c), θ\theta maximizes the expected utility of insider final wealth ([2.5](https://arxiv.org/html/2512.05011v1#S2.E5 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")).

## 4. General Result

###### Theorem 4.1.

The equilibrium is given by c=0c=0,

|  |  |  |
| --- | --- | --- |
|  | w​(t,x)=a​(t,x)w(t,x)=a(t,x) |  |

and

|  |  |  |
| --- | --- | --- |
|  | d​θt=αt​d​t,αt=w​(t,ξt)​ρx​(t,ξt,V​(t),Zt)ρ​(t,ξt,V​(t),Zt),\displaystyle d\theta\_{t}=\alpha\_{t}dt,\hskip 14.22636pt\alpha\_{t}=w(t,\xi\_{t})\frac{\rho\_{x}(t,\xi\_{t},V(t),Z\_{t})}{\rho(t,\xi\_{t},V(t),Z\_{t})}, |  |

where ρ\rho is the transition density of the process η\eta, solving ([2.2](https://arxiv.org/html/2512.05011v1#S2.E2 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information."))

We will prove the Theorem via a sequence of Lemmata that will establish the result. We start with the proof that the candidate equilibrium insider’s strategy yields the unique strong solution for the SDE governing market price process. Moreover, we will demonstrate that this price is fully revealing at time 11.

###### Lemma 4.1.

Let ρ\rho be the transition density of the process given by ([2.2](https://arxiv.org/html/2512.05011v1#S2.E2 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")).
The SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ξt=w​(t,ξt)​ρx​(t,ξt,V​(t),Zt)ρ​(t,ξt,V​(t),Zt)​d​t+w​(t,ξt)​d​Bt,d\xi\_{t}=w(t,\xi\_{t})\frac{\rho\_{x}(t,\xi\_{t},V(t),Z\_{t})}{\rho(t,\xi\_{t},V(t),Z\_{t})}dt+w(t,\xi\_{t})dB\_{t}, |  | (4.7) |

admits the unique strong solution in (Ω,ℱ,(ℱt)t∈[0,1),ℚb​a​s​e)\left(\Omega,{\mathcal{F}},({\mathcal{F}}\_{t})\_{t\in[0,1)},\mathbb{Q}^{base}\right) on [0,1)[0,1). Moreover, the solution satisfies ξ1=Z1\xi\_{1}=Z\_{1} ℚb​a​s​e\mathbb{Q}^{base}-a.s.. Furthermore,

|  |  |  |
| --- | --- | --- |
|  | Yt=ρx​(t,ξt,V​(t),Zt)ρ​(t,ξt,V​(t),Zt)​d​t+d​BtY\_{t}=\frac{\rho\_{x}(t,\xi\_{t},V(t),Z\_{t})}{\rho(t,\xi\_{t},V(t),Z\_{t})}dt+dB\_{t} |  |

is a Brownian Motion in the filtration (ℱtξ)t∈[0,1]\left({\mathcal{F}}^{\xi}\_{t}\right)\_{t\in[0,1]}.

###### Proof.

Consider the following function

|  |  |  |
| --- | --- | --- |
|  | v​(t,x)=∫0x1a​(t,y)​𝑑y+∫0tax​(s,0)2​𝑑s,x∈I.v(t,x)=\int\_{0}^{x}\frac{1}{a(t,y)}dy+\int\_{0}^{t}\frac{a\_{x}(s,0)}{2}ds,\hskip 14.22636ptx\in I. |  |

Due to the Assumption [2.1](https://arxiv.org/html/2512.05011v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.") the range of function vv is ℝ\mathbb{R}. It is continuous and strictly increasing in xx, thus, admits a continuous increasing inverse. Denote this inverse as λ:[0,1]×ℝ→I\lambda:[0,1]\times\mathbb{R}\rightarrow I, i.e.

|  |  |  |
| --- | --- | --- |
|  | v​(t,λ​(t,y))=y​ and ​λ​(t,v​(t,z))=z​ for any ​y∈ℝ,z∈I.v(t,\lambda(t,y))=y\mbox{ and }\lambda(t,v(t,z))=z\mbox{ for any }y\in\mathbb{R},z\in I. |  |

Let κt=v​(t,ηt)\kappa\_{t}=v(t,\eta\_{t}) – this process does not explode on [0,1][0,1].
Indeed, suppose κ\kappa explodes and consider the sequences of stopping times τnu=min⁡{t≥0:κt>n}\tau^{u}\_{n}=\min\{t\geq 0:\kappa\_{t}>n\} and τnl=min⁡{t≥0:κt<−n}\tau^{l}\_{n}=\min\{t\geq 0:\kappa\_{t}<-n\}. Let τi=limn→∞τni\tau^{i}=\lim\_{n\to\infty}\tau\_{n}^{i}, i=l,ui=l,u. Then either ℚb​a​s​e​[τl≤1]>0\mathbb{Q}^{base}[\tau^{l}\leq 1]>0 or ℚb​a​s​e​[τu≤1]>0\mathbb{Q}^{base}[\tau^{u}\leq 1]>0. Suppose, wlog, ℚb​a​s​e​[τu≤1]>0\mathbb{Q}^{base}[\tau^{u}\leq 1]>0, then for ω∈{τu≤1}\omega\in\{\tau^{u}\leq 1\} we will have

|  |  |  |
| --- | --- | --- |
|  | ητu=limn→∞ητnu=limn→∞λ​(τnu,κτnu)=limn→∞λ​(τnu,n)=λ​(τu,+∞)=u,\eta\_{\tau^{u}}=\lim\_{n\to\infty}\eta\_{\tau^{u}\_{n}}=\lim\_{n\to\infty}\lambda(\tau^{u}\_{n},\kappa\_{\tau^{u}\_{n}})=\lim\_{n\to\infty}\lambda(\tau^{u}\_{n},n)=\lambda(\tau^{u},+\infty)=u, |  |

which contradicts the assumption that the domain of η\eta is (l,u)(l,u). Thus, we conclude that τu>1\tau^{u}>1 a.s.. Similar arguments yield τl>1\tau^{l}>1 a.s. and therefore κ\kappa does not explode on [0,1][0,1].

Direct application of Ito lemma yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​κt\displaystyle d\kappa\_{t} | =\displaystyle= | (vt​(t,ηt)+a2​(t,ηt)2​vx​x​(t,ηt))​d​t+a​(t,ηt)​vx​(t,ηt)​d​βt\displaystyle(v\_{t}(t,\eta\_{t})+\frac{a^{2}(t,\eta\_{t})}{2}v\_{xx}(t,\eta\_{t}))dt+a(t,\eta\_{t})v\_{x}(t,\eta\_{t})d\beta\_{t} |  |
|  |  | =\displaystyle= | d​βt+(∫0ηt(γ+ax​x​(t,y)2)​𝑑y+ax​(t,0)2−ax​(t,ηt)2)​d​t\displaystyle d\beta\_{t}+\left(\int\_{0}^{\eta\_{t}}\left(\gamma+\frac{a\_{xx}(t,y)}{2}\right)dy+\frac{a\_{x}(t,0)}{2}-\frac{a\_{x}(t,\eta\_{t})}{2}\right)dt |  |
|  |  | =\displaystyle= | d​βt+γ​ηt​d​t.\displaystyle d\beta\_{t}+\gamma\eta\_{t}dt. |  |

Thus, κ\kappa solves SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​κt=d​βt+γ​λ​(t,κt)​d​t.\displaystyle d\kappa\_{t}=d\beta\_{t}+\gamma\lambda(t,\kappa\_{t})dt. |  | (4.8) |

This SDE has the unique strong solution. The existence of strong solution is obvious as κt=v​(t,ηt)\kappa\_{t}=v(t,\eta\_{t}) is a solution. As for uniqueness, suppose there is another strong solution κt~\tilde{\kappa\_{t}}. Consider a process ηt~=λ​(t,κt~)\tilde{\eta\_{t}}=\lambda(t,\tilde{\kappa\_{t}}). Due to direct application of Ito lemma it will satisfy ([2.2](https://arxiv.org/html/2512.05011v1#S2.E2 "In 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")), so due to the Assumption [2.1](https://arxiv.org/html/2512.05011v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.") η~≡η\tilde{\eta}\equiv\eta and therefore κ~\tilde{\kappa} will coincide with κ\kappa as vv is strictly monotone.

Next we will show that the SDE ([4.8](https://arxiv.org/html/2512.05011v1#S4.E8 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) can be viewed as a weak conditioning of a Brownian Motion (see, e.g. Theorem 4.1 from DMB-CD) which will allow us to characterize its transitional density.

First, we define the function

|  |  |  |
| --- | --- | --- |
|  | u​(t,x)=exp⁡{∫0xγ​λ​(t,y)​𝑑y−∫0t(γ​λx​(s,0)2+γ2​λ2​(s,0)2)​𝑑s+C0},u(t,x)=\exp\left\{\int\_{0}^{x}\gamma\lambda(t,y)dy-\int\_{0}^{t}\left(\frac{\gamma\lambda\_{x}(s,0)}{2}+\frac{\gamma^{2}\lambda^{2}(s,0)}{2}\right)ds+C\_{0}\right\}, |  |

where C0C\_{0} is some constant.

This function satisfies γ​λ​(t,x)=ux​(t,x)u​(t,x)\gamma\lambda(t,x)=\frac{u\_{x}(t,x)}{u(t,x)}, thus, we can rewrite

|  |  |  |
| --- | --- | --- |
|  | d​κt=d​βt+ux​(t,κt)u​(t,κt)​d​t.d\kappa\_{t}=d\beta\_{t}+\frac{u\_{x}(t,\kappa\_{t})}{u(t,\kappa\_{t})}dt. |  |

It is evident that u​(t,x)∈𝒞1,2​([0,1),ℝ)u(t,x)\in{\mathcal{C}}^{1,2}([0,1),\mathbb{R}) and is strictly positive in this domain.

Moreover, u​(t,B~t)u(t,\tilde{B}\_{t}), where B~\tilde{B} is a Brownian motion, is a true martingale. Indeed, due to the Lemma [6.1](https://arxiv.org/html/2512.05011v1#S6.Thmlemma1 "Lemma 6.1. ‣ 6.1. Auxiliary results for main theorem ‣ 6. Appendix ‣ Risk aversion of insider and dynamic asymmetric information.") the fact there exists unique strong solution to ([4.8](https://arxiv.org/html/2512.05011v1#S4.E8 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) and d​κ~t=d​βtd\tilde{\kappa}\_{t}=d\beta\_{t} implies that

|  |  |  |
| --- | --- | --- |
|  | Lt=exp⁡{∫0tux​(s,βs)u​(s,βs)​𝑑βs−12​∫0tux2​(s,βs)u2​(s,βs)​𝑑s}L\_{t}=\exp\left\{\int\_{0}^{t}\frac{u\_{x}(s,\beta\_{s})}{u(s,\beta\_{s})}d\beta\_{s}-\frac{1}{2}\int\_{0}^{t}\frac{u^{2}\_{x}(s,\beta\_{s})}{u^{2}(s,\beta\_{s})}ds\right\} |  |

is a martingale.

Direct calculations yield

|  |  |  |
| --- | --- | --- |
|  | λt​(t,x)+12​λx​x​(t,x)=−γ​λ​(t,x)​λx​(t,x)\lambda\_{t}(t,x)+\frac{1}{2}\lambda\_{xx}(t,x)=-\gamma\lambda(t,x)\lambda\_{x}(t,x) |  |

and

|  |  |  |
| --- | --- | --- |
|  | ut​(t,x)+ux​x​(t,x)2=0,\displaystyle u\_{t}(t,x)+\frac{u\_{xx}(t,x)}{2}=0, |  |

thus,

|  |  |  |
| --- | --- | --- |
|  | d​log⁡(u​(s,βs))=ux​(s,βs)u​(s,βs)​d​βs−12​ux2​(s,βs)u2​(s,βs)​d​sd\log(u(s,\beta\_{s}))=\frac{u\_{x}(s,\beta\_{s})}{u(s,\beta\_{s})}d\beta\_{s}-\frac{1}{2}\frac{u^{2}\_{x}(s,\beta\_{s})}{u^{2}(s,\beta\_{s})}ds |  |

implying

|  |  |  |
| --- | --- | --- |
|  | Lt=u​(t,βt)u​(0,0)L\_{t}=\frac{u(t,\beta\_{t})}{u(0,0)} |  |

which leads to the claimed result.

Similarly, an application of Lemma [6.1](https://arxiv.org/html/2512.05011v1#S6.Thmlemma1 "Lemma 6.1. ‣ 6.1. Auxiliary results for main theorem ‣ 6. Appendix ‣ Risk aversion of insider and dynamic asymmetric information.") with the inverted roles of processes κ\kappa and κ~\tilde{\kappa} yield that 1u​(t,κt)\frac{1}{u(t,\kappa\_{t})} is a true martingale.

Since u​(t,x)u(t,x) satisfies the conditions of hh-function in the Theorem 4.1 of DMB-CD, the ([4.8](https://arxiv.org/html/2512.05011v1#S4.E8 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) is indeed the SDE of a Brownian motion weakly conditioned by uu. In particular, the transition density of the process κ\kappa, p(.)p(.), satisfies

|  |  |  |
| --- | --- | --- |
|  | p​(s,x;t,y)=1u​(s,x)​u​(t,y)​Γ​(s,x,t,y),p(s,x;t,y)=\frac{1}{u(s,x)}u(t,y)\Gamma(s,x,t,y), |  |

where Γ\Gamma is the transition density of a standard Brownian motion.

Consider the process

|  |  |  |
| --- | --- | --- |
|  | Ut=v​(V​(t),Zt)=v​(V​(t),ηV​(t))=κV​(t).U\_{t}=v(V(t),Z\_{t})=v(V(t),\eta\_{V(t)})=\kappa\_{V(t)}. |  |

Direct change of time yields that SDE for UU is:

|  |  |  |
| --- | --- | --- |
|  | d​Ut=σ​(t)​d​β~t+γ​λ​(V​(t),Ut)​σ2​(t)​d​t.\displaystyle dU\_{t}=\sigma(t)d\tilde{\beta}\_{t}+\gamma\lambda(V(t),U\_{t})\sigma^{2}(t)dt. |  |

where β~\tilde{\beta} is defined in the Remark [2](https://arxiv.org/html/2512.05011v1#Thmremark2 "Remark 2. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.").

Now we are in the position to prove that the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Rt=d​Bt+γ​λ​(t,Rt)​d​t+px​(t,Rt,V​(t),Ut)p​(t,Rt,V​(t),Ut)​d​t,\displaystyle dR\_{t}=dB\_{t}+\gamma\lambda(t,R\_{t})dt+\frac{p\_{x}(t,R\_{t},V(t),U\_{t})}{p(t,R\_{t},V(t),U\_{t})}dt, |  | (4.9) |

admits a unique strong solution and R1=U1R\_{1}=U\_{1} ℚb​a​s​e\mathbb{Q}^{base}-a.s..

First, using the relation between p(.)p(.) and the transition density of Brownian motion we can represent

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | px​(t,Rt,V​(t),Ut)p​(t,Rt,V​(t),Ut)\displaystyle\frac{p\_{x}(t,R\_{t},V(t),U\_{t})}{p(t,R\_{t},V(t),U\_{t})} | =\displaystyle= | Γx​(t,Rt,V​(t),Ut)Γ​(t,Rt,V​(t),Ut)−ux​(t,Rt)u​(t,Rt)\displaystyle\frac{\Gamma\_{x}(t,R\_{t},V(t),U\_{t})}{\Gamma(t,R\_{t},V(t),U\_{t})}-\frac{u\_{x}(t,R\_{t})}{u(t,R\_{t})} |  |
|  |  | =\displaystyle= | Ut−RtV​(t)−t−ux​(t,Rt)u​(t,Rt).\displaystyle\frac{U\_{t}-R\_{t}}{V(t)-t}-\frac{u\_{x}(t,R\_{t})}{u(t,R\_{t})}. |  |

Thus, the equation ([4.9](https://arxiv.org/html/2512.05011v1#S4.E9 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) becomes:

|  |  |  |
| --- | --- | --- |
|  | d​Rt=d​Bt+Ut−RtV​(t)−t​d​t.\displaystyle dR\_{t}=dB\_{t}+\frac{U\_{t}-R\_{t}}{V(t)-t}dt. |  |

And therefore we have the following system of equations:

|  |  |  |
| --- | --- | --- |
|  | {d​Ut=σ​(t)​d​β~t+γ​λ​(V​(t),Ut)​σ2​(t)​d​t,d​Rt=d​Bt+Ut−RtV​(t)−t​d​t.\begin{cases}dU\_{t}=\sigma(t)d\tilde{\beta}\_{t}+\gamma\lambda(V(t),U\_{t})\sigma^{2}(t)dt,\\ dR\_{t}=dB\_{t}+\frac{U\_{t}-R\_{t}}{V(t)-t}dt.\end{cases} |  |

Consider a new probability measure defined by

|  |  |  |
| --- | --- | --- |
|  | d​ℙ~d​ℚb​a​s​e|ℱ1β~,B=u​(v0,U0)u​(1,U1)=(v0,κv0)u​(1,κ1)\left.\frac{d\tilde{\mathbb{P}}}{d\mathbb{Q}^{base}}\right|\_{\mathcal{F}^{\tilde{\beta},B}\_{1}}=\frac{u(v\_{0},U\_{0})}{u(1,U\_{1})}=\frac{(v\_{0},\kappa\_{v\_{0}})}{u(1,\kappa\_{1})} |  |

which is an equivalent to ℚb​a​s​e\mathbb{Q}^{base} since 1u​(t,κt)\frac{1}{u(t,\kappa\_{t})} is a true martingale due to the above considerations. This change of measure yields:

|  |  |  |
| --- | --- | --- |
|  | {d​Ut=σ​(t)​d​βtℙ~,d​Rt=d​Btℙ~+Ut−RtV​(t)−t​d​t.\begin{cases}dU\_{t}=\sigma(t)d\beta^{\tilde{\mathbb{P}}}\_{t},\\ dR\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-R\_{t}}{V(t)-t}dt.\end{cases} |  |

Due to Theorem 5.2 in DMB-CD this system has the unique strong solution and R1=U1R\_{1}=U\_{1} ℙ~\tilde{\mathbb{P}}-a.s.. Since the two measures are equivalent, the equation ([4.9](https://arxiv.org/html/2512.05011v1#S4.E9 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) has the unique strong solution and R1=U1R\_{1}=U\_{1} ℚb​a​s​e\mathbb{Q}^{base}-a.s., as claimed.

Now we are in position to establish the existence and uniqueness of solution of ([4.7](https://arxiv.org/html/2512.05011v1#S4.E7 "In Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) and the fact that ξ1=Z1\xi\_{1}=Z\_{1}. Consider ξ~t=λ​(t,Rt)\tilde{\xi}\_{t}=\lambda(t,R\_{t}) and observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​ξ~t\displaystyle d\tilde{\xi}\_{t} | =\displaystyle= | d​λ​(t,Rt)=(λt​(t,Rt)+12​λx​x​(t,Rt))​d​t+λx​(t,Rt)​d​Rt\displaystyle d\lambda(t,R\_{t})=\left(\lambda\_{t}(t,R\_{t})+\frac{1}{2}\lambda\_{xx}(t,R\_{t})\right)dt+\lambda\_{x}(t,R\_{t})dR\_{t} |  |
|  |  | =\displaystyle= | −γ​λ​(t,Rt)​λx​(t,Rt)​d​t+λx​(t,Rt)​d​Bt+γ​λ​(t,Rt)​λx​(t,Rt)​d​t\displaystyle-\gamma\lambda(t,R\_{t})\lambda\_{x}(t,R\_{t})dt+\lambda\_{x}(t,R\_{t})dB\_{t}+\gamma\lambda(t,R\_{t})\lambda\_{x}(t,R\_{t})dt |  |
|  |  |  | +λx​(t,Rt)​px​(t,Rt,V​(t),Ut)p​(t,Rt,V​(t),Ut)​d​t\displaystyle+\lambda\_{x}(t,R\_{t})\frac{p\_{x}(t,R\_{t},V(t),U\_{t})}{p(t,R\_{t},V(t),U\_{t})}dt |  |
|  |  | =\displaystyle= | w​(t,ξ~t)​d​Bt+w​(t,ξ~t)​px​(t,Rt,V​(t),Ut)p​(t,Rt,V​(t),Ut)​d​t\displaystyle w(t,\tilde{\xi}\_{t})dB\_{t}+w(t,\tilde{\xi}\_{t})\frac{p\_{x}(t,R\_{t},V(t),U\_{t})}{p(t,R\_{t},V(t),U\_{t})}dt |  |

since

|  |  |  |
| --- | --- | --- |
|  | λx​(t,Rt)=λx​(t,λ−1​(t,ξ~t))=1vx(t,λ(t,λ−1(t,ξ~t))=w​(t,ξ~t).\lambda\_{x}(t,R\_{t})=\lambda\_{x}(t,\lambda^{-1}(t,\tilde{\xi}\_{t}))=\frac{1}{v\_{x}(t,\lambda(t,\lambda^{-1}(t,\tilde{\xi}\_{t}))}=w(t,\tilde{\xi}\_{t}). |  |

As Zt=λ​(V​(t),Ut)Z\_{t}=\lambda(V(t),U\_{t}), ξ~1=Z1\tilde{\xi}\_{1}=Z\_{1} ℚb​a​s​e\mathbb{Q}^{base}-a.s.. Moreover, as ℱtR=ℱtξ{\mathcal{F}}\_{t}^{R}={\mathcal{F}}\_{t}^{\xi} for t∈[0,1)t\in[0,1),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(t,Rt,V​(t),z)​d​z\displaystyle p(t,R\_{t},V(t),z)dz | =\displaystyle= | ℙ​[Ut∈d​z|ℱtR]=ℙ​[Zt∈d​λ​(V​(t),z)|ℱtξ]=\displaystyle\mathbb{P}\left[U\_{t}\in dz\left|{\mathcal{F}}\_{t}^{R}\right.\right]=\mathbb{P}\left[Z\_{t}\in d\lambda(V(t),z)\left|{\mathcal{F}}\_{t}^{\xi}\right.\right]= |  |
|  |  | =\displaystyle= | ρ​(t,ξ~t,V​(t),λ​(V​(t),z))​d​λ​(V​(t),z)\displaystyle\rho(t,\tilde{\xi}\_{t},V(t),\lambda(V(t),z))d\lambda(V(t),z) |  |
|  |  | =\displaystyle= | ρ​(t,ξ~t,V​(t),λ​(V​(t),z))​w​(V​(t),λ​(V​(t),z))​d​z\displaystyle\rho(t,\tilde{\xi}\_{t},V(t),\lambda(V(t),z))w(V(t),\lambda(V(t),z))dz |  |
|  |  | =\displaystyle= | ρ​(t,λ​(t,Rt),V​(t),λ​(V​(t),z))​w​(V​(t),λ​(V​(t),z))​d​z.\displaystyle\rho(t,\lambda(t,R\_{t}),V(t),\lambda(V(t),z))w(V(t),\lambda(V(t),z))dz. |  |

That is,

|  |  |  |
| --- | --- | --- |
|  | ρ​(t,y,V​(t),z)=p​(t,λ−1​(t,y),V​(t),λ−1​(V​(t),z))w​(V​(t),z).\displaystyle\rho(t,y,V(t),z)=\frac{p(t,\lambda^{-1}(t,y),V(t),\lambda^{-1}(V(t),z))}{w(V(t),z)}. |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ξ~t=w​(t,ξ~t)​d​Bt+w2​(t,ξ~t)​ρx​(t,ξ~t,V​(t),Zt)ρ​(t,ξ~t,V​(t),Zt)​d​t,\displaystyle d\tilde{\xi}\_{t}=w(t,\tilde{\xi}\_{t})dB\_{t}+w^{2}(t,\tilde{\xi}\_{t})\frac{\rho\_{x}(t,\tilde{\xi}\_{t},V(t),Z\_{t})}{\rho(t,\tilde{\xi}\_{t},V(t),Z\_{t})}dt, |  | (4.10) |

Since the SDE for RtR\_{t} has the unique strong solution, ξ~t=λ​(t,Rt)\tilde{\xi}\_{t}=\lambda(t,R\_{t}), and λ​(t,x)\lambda(t,x) is continuous and strictly increasing in xx, the SDE ([4.10](https://arxiv.org/html/2512.05011v1#S4.E10 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) has the unique strong solution. Hence there exists the unique strong solution of ([4.7](https://arxiv.org/html/2512.05011v1#S4.E7 "In Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) and ξ1=Z1\xi\_{1}=Z\_{1} ℚb​a​s​e\mathbb{Q}^{base}-a.s., as claimed.

Finally, observe that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[w​(t,ξt)​ρx​(t,ξt,V​(t),f​(Zt))ρ​(t,ξt,V​(t),f​(Zt))|ℱtξ]=𝔼​[px​(t,Rt,V​(t),Ut)p​(t,Rt,V​(t),Ut)|ℱtR]\displaystyle\mathbb{E}\left[\left.w(t,\xi\_{t})\frac{\rho\_{x}(t,\xi\_{t},V(t),f(Z\_{t}))}{\rho(t,\xi\_{t},V(t),f(Z\_{t}))}\right|{\mathcal{F}}\_{t}^{\xi}\right]=\mathbb{E}\left[\left.\frac{p\_{x}(t,R\_{t},V(t),U\_{t})}{p(t,R\_{t},V(t),U\_{t})}\right|{\mathcal{F}}\_{t}^{R}\right] |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[px​(t,Rt,V​(t),Ut)p​(t,Rt,V​(t),Ut)|ℱtR]=∫ℝpx​(t,Rt,V​(t),u)​𝑑u=0,\displaystyle\mathbb{E}\left[\left.\frac{p\_{x}(t,R\_{t},V(t),U\_{t})}{p(t,R\_{t},V(t),U\_{t})}\right|{\mathcal{F}}\_{t}^{R}\right]=\int\_{\mathbb{R}}p\_{x}(t,R\_{t},V(t),u)du=0, |  |

thus,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ρx​(t,ξt,V​(t),f​(Zt))ρ​(t,ξt,V​(t),f​(Zt))|ℱtξ]=1w​(t,ξt)​𝔼​[w​(t,ξt)​ρx​(t,ξt,V​(t),f​(Zt))ρ​(t,ξt,V​(t),f​(Zt))|ℱtξ]=0\mathbb{E}\left[\left.\frac{\rho\_{x}(t,\xi\_{t},V(t),f(Z\_{t}))}{\rho(t,\xi\_{t},V(t),f(Z\_{t}))}\right|{\mathcal{F}}\_{t}^{\xi}\right]=\frac{1}{w(t,\xi\_{t})}\mathbb{E}\left[\left.w(t,\xi\_{t})\frac{\rho\_{x}(t,\xi\_{t},V(t),f(Z\_{t}))}{\rho(t,\xi\_{t},V(t),f(Z\_{t}))}\right|{\mathcal{F}}\_{t}^{\xi}\right]=0 |  |

and YY is a Brownian Motion as claimed.
∎

###### Lemma 4.2.

Let (w,c)(w,c) be a pricing rule satisfying the Definition [3.1](https://arxiv.org/html/2512.05011v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3. Admissibility and Equilibrium ‣ Risk aversion of insider and dynamic asymmetric information."). Suppose there exists an absolutely continuous insider’s strategy θ^∈𝒜​(w,c)\hat{\theta}\in{\mathcal{A}}(w,c) such that Z1=P1Z\_{1}=P\_{1} a.s.. Then for any θ∈𝒜​(w,c)\theta\in{\mathcal{A}}(w,c) we will have

|  |  |  |
| --- | --- | --- |
|  | E0,z​[U​(W1θ^)]≥E0,z​[U​(W1θ)],\displaystyle E^{0,z}\left[U\left(W\_{1}^{\hat{\theta}}\right)\right]\geq E^{0,z}\left[U\left(W\_{1}^{\theta}\right)\right], |  |

i.e. this insider’s strategy is optimal.

###### Proof.

Consider the function Ψa​(t,x)\Psi^{a}(t,x):

|  |  |  |
| --- | --- | --- |
|  | Ψa​(t,x)=∫a−cxu−(a−c)w​(t,u)​𝑑u+12​∫t1w​(s,a−c)​𝑑s.\displaystyle\Psi^{a}(t,x)=\int\_{a-c}^{x}\frac{u-(a-c)}{w(t,u)}du+\frac{1}{2}\int\_{t}^{1}w(s,a-c)ds. |  |

As w​(t,x)w(t,x) is positive we have

|  |  |  |
| --- | --- | --- |
|  | Ψa​(1−,x)≥0​ and ​Ψa​(1−,x)=0⇔x+c=a.\Psi^{a}(1-,x)\geq 0\mbox{ and }\Psi^{a}(1-,x)=0\Leftrightarrow x+c=a. |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψta​(t,x)+w2​(t,x)2​Ψx​xa​(t,x)=γ2​(x−(a−c))2.\Psi\_{t}^{a}(t,x)+\frac{w^{2}(t,x)}{2}\Psi\_{xx}^{a}(t,x)=\frac{\gamma}{2}(x-(a-c))^{2}. |  | (4.11) |

Indeed, direct calculations yield

|  |  |  |
| --- | --- | --- |
|  | {Ψta=−∫a−cx(u−(a−c))​wt​(t,u)w2​(t,u)​𝑑u−12​w​(t,a−c)Ψxa=x−(a−c)w​(t,x)Ψx​xa=1w​(t,x)−(x−(a−c))​wx​(t,x)w2​(t,x).\begin{cases}\Psi\_{t}^{a}=-\int\_{a-c}^{x}\frac{(u-(a-c))w\_{t}(t,u)}{w^{2}(t,u)}du-\frac{1}{2}w(t,a-c)\\ \Psi\_{x}^{a}=\frac{x-(a-c)}{w(t,x)}\\ \Psi\_{xx}^{a}=\frac{1}{w(t,x)}-\frac{(x-(a-c))w\_{x}(t,x)}{w^{2}(t,x)}.\end{cases} |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | Ψta​(t,x)+w2​(t,x)2​Ψx​xa​(t,x)=\displaystyle\Psi\_{t}^{a}(t,x)+\frac{w^{2}(t,x)}{2}\Psi\_{xx}^{a}(t,x)= |  |
|  |  |  |
| --- | --- | --- |
|  | =−∫a−cx(u−(a−c))​wt​(t,u)w2​(t,u)​𝑑u−w​(t,a−c)2+w​(t,x)2−(x−(a−c))​wx​(t,x)2.\displaystyle=-\int\_{a-c}^{x}\frac{(u-(a-c))w\_{t}(t,u)}{w^{2}(t,u)}du-\frac{w(t,a-c)}{2}+\frac{w(t,x)}{2}-\frac{(x-(a-c))w\_{x}(t,x)}{2}. |  |

Using Definition [3.1](https://arxiv.org/html/2512.05011v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3. Admissibility and Equilibrium ‣ Risk aversion of insider and dynamic asymmetric information.") and integration by parts yields

|  |  |  |
| --- | --- | --- |
|  | −∫(a−c)x(u−(a−c))​wt​(t,u)w2​(t,u)​𝑑u=∫(a−c)x(u−(a−c))​(γ+wx​x​(t,u)2)​𝑑u=γ​∫(a−c)x(u−(a−c))​𝑑u+(x−(a−c))​wx​(t,x)2−∫(a−c)xwx​(t,u)2​𝑑u\begin{array}[]{ll}-\int\_{(a-c)}^{x}\frac{(u-(a-c))w\_{t}(t,u)}{w^{2}(t,u)}du&=\int\_{(a-c)}^{x}(u-(a-c))\left(\gamma+\frac{w\_{xx}(t,u)}{2}\right)du\\ &=\gamma\int\_{(a-c)}^{x}(u-(a-c))du+(x-(a-c))\frac{w\_{x}(t,x)}{2}-\int\_{(a-c)}^{x}\frac{w\_{x}(t,u)}{2}du\end{array} |  |

which establishes ([4.11](https://arxiv.org/html/2512.05011v1#S4.E11 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")).

Next, applying Theorem 32 in Pro to Ψa​(t,ξt)\Psi^{a}(t,\xi\_{t}) as well as ([4.11](https://arxiv.org/html/2512.05011v1#S4.E11 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) yields

|  |  |  |
| --- | --- | --- |
|  | W1θ=ΨZ1​(0,0)−ΨZ1​(1−,ξ1−)−12​∫01−ω​(t,ξt−)​d​[θ,θ]tc+\displaystyle W\_{1}^{\theta}=\Psi^{Z\_{1}}(0,0)-\Psi^{Z\_{1}}(1-,\xi\_{1-})-\frac{1}{2}\int\_{0}^{1-}\omega(t,\xi\_{t-})d[\theta,\theta]\_{t}^{c}+ |  |
|  |  |  |
| --- | --- | --- |
|  | +∑0<t<1{ΨZ1​(t,ξt)−ΨZ1​(t,ξt−)−(ξt+c−Z1)​Δ​θt}+\displaystyle+\sum\_{0<t<1}\{\Psi^{Z\_{1}}(t,\xi\_{t})-\Psi^{Z\_{1}}(t,\xi\_{t-})-(\xi\_{t}+c-Z\_{1})\Delta\theta\_{t}\}+ |  |
|  |  |  |
| --- | --- | --- |
|  | +∫01−(ξt−+c−Z1)​𝑑Bt+∫01−γ2​(ξt−+c−Z1)2​𝑑t,\displaystyle+\int\_{0}^{1-}(\xi\_{t-}+c-Z\_{1})dB\_{t}+\int\_{0}^{1-}\frac{\gamma}{2}(\xi\_{t-}+c-Z\_{1})^{2}dt, |  |

in view of the representation for the insider final wealth as

|  |  |  |
| --- | --- | --- |
|  | W1θ=∫01−(Z1−ξt−−c)​𝑑θt−∫01−w​(t,ξt−)​{d​[B,θ]t+[θ,θ]tc}.\displaystyle W\_{1}^{\theta}=\int\_{0}^{1-}(Z\_{1}-\xi\_{t-}-c)d\theta\_{t}-\int\_{0}^{1-}w(t,\xi\_{t-})\{d[B,\theta]\_{t}+[\theta,\theta]\_{t}^{c}\}. |  |

Thus, the insider maximization problem becomes

|  |  |  |
| --- | --- | --- |
|  | 1+supθ∈𝒜​(ω,c)E0,z​[−1γ​e−γ​W1θ]=1−1γ​infθ∈𝒜​(ω,c)E0,z​[e−γ​(ΨZ1​(0,0)−ΨZ1​(1−,ξ1−)−M1−+∑0<t<1Dt+ζ1−)].\displaystyle 1+\sup\_{\theta\in\mathcal{A}(\omega,c)}E^{0,z}\left[-\frac{1}{\gamma}e^{-\gamma W\_{1}^{\theta}}\right]=1-\frac{1}{\gamma}\inf\_{\theta\in\mathcal{A}(\omega,c)}E^{0,z}\left[e^{-\gamma\left(\Psi^{Z\_{1}}(0,0)-\Psi^{Z\_{1}}(1-,\xi\_{1-})-M\_{1-}+\sum\_{0<t<1}D\_{t}+\zeta\_{1-}\right)}\right]. |  |

where

|  |  |  |
| --- | --- | --- |
|  | M1−=12​∫01−w​(t,ξt−)​d​[θ,θ]tc≥0,\displaystyle M\_{1-}=\frac{1}{2}\int\_{0}^{1-}w(t,\xi\_{t-})d[\theta,\theta]\_{t}^{c}\geq 0, |  |
|  |  |  |
| --- | --- | --- |
|  | Dt=ΨZ1​(t,ξt)−ΨZ1​(t,ξt−)−(ξt+c−Z1)​Δ​θt,\displaystyle D\_{t}=\Psi^{Z\_{1}}(t,\xi\_{t})-\Psi^{Z\_{1}}(t,\xi\_{t-})-(\xi\_{t}+c-Z\_{1})\Delta\theta\_{t}, |  |
|  |  |  |
| --- | --- | --- |
|  | ζt=∫0t(ξs−+c−Z1)​𝑑Bs+∫0tγ2​(ξs−+c−Z1)2​𝑑s.\displaystyle\zeta\_{t}=\int\_{0}^{t}(\xi\_{s-}+c-Z\_{1})dB\_{s}+\int\_{0}^{t}\frac{\gamma}{2}(\xi\_{s-}+c-Z\_{1})^{2}ds. |  |

Observe that

|  |  |  |
| --- | --- | --- |
|  | Dt=∫ξt−ξtu+c−Z1w​(t,u)​𝑑u−(ξt+c−Z1)​Δ​θt≤\displaystyle D\_{t}=\int\_{\xi\_{t-}}^{\xi\_{t}}\frac{u+c-Z\_{1}}{w(t,u)}du-(\xi\_{t}+c-Z\_{1})\Delta\theta\_{t}\leq |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(ξt+c−Z1)​∫ξt−ξt1w​(t,u)​𝑑u−(ξt+c−Z1)​Δ​θt=0,\displaystyle\leq(\xi\_{t}+c-Z\_{1})\int\_{\xi\_{t-}}^{\xi\_{t}}\frac{1}{w(t,u)}du-(\xi\_{t}+c-Z\_{1})\Delta\theta\_{t}=0, |  |

since at each jump at time t−t- we have ∫ξt−ξt1w​(t,u)​𝑑u=Kw​(t,ξt)−Kw​(t,ξt−)=Δ​Yt=Δ​θt\int\_{\xi\_{t-}}^{\xi\_{t}}\frac{1}{w(t,u)}du=K\_{w}(t,\xi\_{t})-K\_{w}(t,\xi\_{t-})=\Delta Y\_{t}=\Delta\theta\_{t} according to the chosen pricing rule.

Thus, in view of positivity of M1−M\_{1-}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1+supθ∈𝒜​(ω,c)E0,z​[−1γ​e−γ​W1θ]≤1−1γ​infθ∈𝒜​(ω,c)E0,z​[e−γ​ΨZ1​(0,c)​e−γ​ζ1−].1+\sup\_{\theta\in\mathcal{A}(\omega,c)}E^{0,z}\left[-\frac{1}{\gamma}e^{-\gamma W\_{1}^{\theta}}\right]\leq 1-\frac{1}{\gamma}\inf\_{\theta\in\mathcal{A}(\omega,c)}E^{0,z}\left[e^{-\gamma\Psi^{Z\_{1}}(0,c)}e^{-\gamma\zeta\_{1-}}\right]. |  | (4.12) |

Note that in the above the equality reached only if θ\theta is absolutely continuous and P1=Z1P\_{1}=Z\_{1} as this will imply M1−=0M\_{1-}=0 and Dt≡0D\_{t}\equiv 0.

Consider a change of measure given by (recall that Pt=ξt+cP\_{t}=\xi\_{t}+c)

|  |  |  |
| --- | --- | --- |
|  | d​Q0,zd​P0,z=e−γ​∫01Pt​𝑑Bt−γ22​∫01Pt2​𝑑t\frac{dQ^{0,z}}{dP^{0,z}}=e^{-\gamma\int\_{0}^{1}P\_{t}dB\_{t}-\frac{\gamma^{2}}{2}\int\_{0}^{1}P^{2}\_{t}dt} |  |

It is an equivalent change of measure for any admissible strategy and under measure Q0,zQ^{0,z} the processes d​B^t=d​Bt+γ​Pt​d​td\hat{B}\_{t}=dB\_{t}+\gamma P\_{t}dt and β\beta are independent Brownian motions. Thus,

|  |  |  |
| --- | --- | --- |
|  | 1−1γ​infθ∈𝒜​(ω,c)E0,z​[e−γ​ΨZ1​(0,c)​e−γ​ζ1−]=1−1γ​infθ∈𝒜​(ω,c)EQ0,z​[e−γ​ΨZ1​(0,c)+γ​Z1​B^1−γ22​Z12]\displaystyle 1-\frac{1}{\gamma}\inf\_{\theta\in\mathcal{A}(\omega,c)}E^{0,z}\left[e^{-\gamma\Psi^{Z\_{1}}(0,c)}e^{-\gamma\zeta\_{1-}}\right]=1-\frac{1}{\gamma}\inf\_{\theta\in\mathcal{A}(\omega,c)}E^{Q^{0,z}}\left[e^{-\gamma\Psi^{Z\_{1}}(0,c)+\gamma Z\_{1}\hat{B}\_{1}-\frac{\gamma^{2}}{2}Z\_{1}^{2}}\right] |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | 1−1γ​infθ∈𝒜​(ω,c)EQ0,z​[e−γ​ΨZ1​(0,c)+γ​Z1​B^1−γ22​Z12]==1−1γ​infθ∈𝒜​(ω,c)EQ0,z​[e−γ​ΨZ1​(0,c)​EQ0,z​[eγ​Z1​B^1−γ22​Z12∣ℱ0∨σ​(Z1)]].1-\frac{1}{\gamma}\inf\_{\theta\in\mathcal{A}(\omega,c)}E^{Q^{0,z}}\left[e^{-\gamma\Psi^{Z\_{1}}(0,c)+\gamma Z\_{1}\hat{B}\_{1}-\frac{\gamma^{2}}{2}Z\_{1}^{2}}\right]=\\ =1-\frac{1}{\gamma}\inf\_{\theta\in\mathcal{A}(\omega,c)}E^{Q^{0,z}}\left[e^{-\gamma\Psi^{Z\_{1}}(0,c)}E^{Q^{0,z}}\left[e^{\gamma Z\_{1}\hat{B}\_{1}-\frac{\gamma^{2}}{2}Z\_{1}^{2}}\mid\mathcal{F}\_{0}\vee\sigma(Z\_{1})\right]\right]. |  |

Observe that in the enlarged filtration B^\hat{B} is a Brownian motion as it is independent of β\beta. Hence EQ0,z​[eγ​Z1​B^1−γ22​Z12|ℱ0∨σ​(Z1)]=1E^{Q^{0,z}}\left[\left.e^{\gamma Z\_{1}\hat{B}\_{1}-\frac{\gamma^{2}}{2}Z\_{1}^{2}}\right|\mathcal{F}\_{0}\vee\sigma(Z\_{1})\right]=1 and distribution of Z1Z\_{1} under Q0,zQ^{0,z} is the same as under P0,zP^{0,z}. Thus,

|  |  |  |
| --- | --- | --- |
|  | 1−1γ​infθ∈𝒜​(ω,c)E0,z​[e−γ​ΨZ1​(0,c)​e−γ​ζ1−]=1+E0,z​[−1γ​e−γ​ΨZ1​(0,c)]1-\frac{1}{\gamma}\inf\_{\theta\in\mathcal{A}(\omega,c)}E^{0,z}\left[e^{-\gamma\Psi^{Z\_{1}}(0,c)}e^{-\gamma\zeta\_{1-}}\right]=1+E^{0,z}\left[-\frac{1}{\gamma}e^{-\gamma\Psi^{Z\_{1}}(0,c)}\right] |  |

Combining this with ([4.12](https://arxiv.org/html/2512.05011v1#S4.E12 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) yields

|  |  |  |
| --- | --- | --- |
|  | 1+supθ∈𝒜​(ω,c)E0,z​[−1γ​e−γ​W1θ]≤1+E0,z​[−1γ​e−γ​ΨZ1​(0,c)]1+\sup\_{\theta\in\mathcal{A}(\omega,c)}E^{0,z}\left[-\frac{1}{\gamma}e^{-\gamma W\_{1}^{\theta}}\right]\leq 1+E^{0,z}\left[-\frac{1}{\gamma}e^{-\gamma\Psi^{Z\_{1}}(0,c)}\right] |  |

Moreover, in view of discussion after equation ([4.12](https://arxiv.org/html/2512.05011v1#S4.E12 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) we obtain

|  |  |  |
| --- | --- | --- |
|  | 1+E0,z​[−1γ​e−γ​W1θ^]=1+E0,z​[−1γ​e−γ​ΨZ1​(0,c)]1+E^{0,z}\left[-\frac{1}{\gamma}e^{-\gamma W\_{1}^{\hat{\theta}}}\right]=1+E^{0,z}\left[-\frac{1}{\gamma}e^{-\gamma\Psi^{Z\_{1}}(0,c)}\right] |  |

for θ^\hat{\theta} in the statement of the Lemma. Comparing the last two equations completes the proof.
∎

The above two lemmata establish the result of Theorem [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") provided that the strategy considered in Lemma [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmlemma1 "Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") is admissible. Indeed, Lemma [4.2](https://arxiv.org/html/2512.05011v1#S4.Thmlemma2 "Lemma 4.2. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") proves that an absolutely continuous admissible strategy such that P1=Z1P\_{1}=Z\_{1} is optimal for the insider. On the other hand, Lemma [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmlemma1 "Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") provides a constructive example of such a strategy. Thus, if this strategy is admissible, the proof of Theorem [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") is complete.

###### Proof.

of Theorem [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")
Due to the above discussion to establish the result it remains to show that the strategy α\alpha is admissible. Verification of admissibility will follow closely the proof of Lemma [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmlemma1 "Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") and we will freely use the notation from it.

Observe that, due to the result of Lemma [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmlemma1 "Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") the admissibility will follow once we demonstrate that

|  |  |  |
| --- | --- | --- |
|  | 1=𝔼0,z​[e−γ​∫01Pt​𝑑Bt−γ22​∫01Pt2​𝑑t]1=\mathbb{E}^{0,z}\left[e^{-\gamma\int\_{0}^{1}P\_{t}dB\_{t}-\frac{\gamma^{2}}{2}\int\_{0}^{1}P^{2}\_{t}dt}\right] |  |

where Pt=ξt=λ​(t,Rt)P\_{t}=\xi\_{t}=\lambda(t,R\_{t}) and ξ\xi solves ([4.7](https://arxiv.org/html/2512.05011v1#S4.E7 "In Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")).

Let us consider the process Xt=−γ​Pt=−γ​ξt=−γ​λ​(t,Rt)X\_{t}=-\gamma P\_{t}=-\gamma\xi\_{t}=-\gamma\lambda(t,R\_{t}). We need to prove that Doleans-Dade exponential ℰ​(X)t\mathcal{E}(X)\_{t} defines Q0,zQ^{0,z} – probability measure equivalent to P0,zP^{0,z}.
We know that P0,zP^{0,z} is already equivalent to the measure P~\tilde{P} defined in Lemma [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmlemma1 "Lemma 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") via u​(0,0)u​(1,U1)\frac{u(0,0)}{u(1,U\_{1})}, so it is sufficient to prove that the measure Q0,zQ^{0,z} is equivalent to the measure P~\tilde{P}.

Following the proof of the Lemma [6.1](https://arxiv.org/html/2512.05011v1#S6.Thmlemma1 "Lemma 6.1. ‣ 6.1. Auxiliary results for main theorem ‣ 6. Appendix ‣ Risk aversion of insider and dynamic asymmetric information."), the required result is established once it is shown that the two dimensional SDEs

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Ut=σ​(t)​d​βtℙ~,U0=0,d​R~t=d​Btℙ~+Ut−R~tV​(t)−t​d​t,R0=0,\begin{cases}dU\_{t}=\sigma(t)d\beta^{\tilde{\mathbb{P}}}\_{t},\quad U\_{0}=0,\\ d\tilde{R}\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-\tilde{R}\_{t}}{V(t)-t}dt,\quad R\_{0}=0,\end{cases} |  | (4.13) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Ut=σ​(t)​d​βtℙ~,U0=0,d​Rt=d​Btℙ~+Ut−RtV​(t)−t​d​t−γ​λ​(t,Rt)​d​t,R0=0.\begin{cases}dU\_{t}=\sigma(t)d\beta^{\tilde{\mathbb{P}}}\_{t},\quad U\_{0}=0,\\ dR\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-R\_{t}}{V(t)-t}dt-\gamma\lambda(t,R\_{t})dt,\quad R\_{0}=0.\end{cases} |  | (4.14) |

have unique strong solutions.

The first SDE has the unique strong solution on [0,1][0,1] due to Theorem 5.2 in DMB-CD. Moreover, this solution doesn’t explode on the interval [0,1][0,1].

As to the second SDE, as its coefficients are locally Lipschitz and locally bounded, it admits unique strong solution up to the explosion time in view of Theorem 2.8 in DMB-CD. So, it is left to prove that there is no explosion on [0,1][0,1].

To demonstrate that, let Ω1⊆Ω\Omega\_{1}\subseteq\Omega be a set of ω∈Ω\omega\in\Omega such that: 1) solution of ([4.13](https://arxiv.org/html/2512.05011v1#S4.E13 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) exists and continuous, and 2) there exists continuous RR solving ([4.14](https://arxiv.org/html/2512.05011v1#S4.E14 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) until stopping time τ​(ω)\tau(\omega). Observe that
ℙ~​(Ω1)=1\tilde{\mathbb{P}}(\Omega\_{1})=1. Fix any ω∗∈Ω1\omega^{\*}\in\Omega\_{1} and suppose τ​(ω∗)<1\tau(\omega^{\*})<1. We have that u​(t)=Rt−R~tu(t)=R\_{t}-\tilde{R}\_{t} is continuous and solves

|  |  |  |
| --- | --- | --- |
|  | u′​(t)=−u​(t)V​(t)−t​d​t−γ​λ​(t,u​(t)+R~t​(ω∗))​d​t,u​(0)=0u^{\prime}(t)=-\frac{u(t)}{V(t)-t}dt-\gamma\lambda(t,u(t)+\tilde{R}\_{t}(\omega^{\*}))dt,\quad u(0)=0 |  |

on [0,τ​(ω∗))[0,\tau(\omega^{\*})) and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | (u2​(t))′=−u2​(t)2​(V​(t)−t)​d​t−γ2​u​(t)​λ​(t,u​(t)+R~t​(ω∗))​d​t(u^{2}(t))^{\prime}=-\frac{u^{2}(t)}{2(V(t)-t)}dt-\frac{\gamma}{2}u(t)\lambda(t,u(t)+\tilde{R}\_{t}(\omega^{\*}))dt |  | (4.15) |

on [0,τ​(ω∗))[0,\tau(\omega^{\*})).

Since λ​(t,x)\lambda(t,x) is smooth enough, the function n​(t)n(t), defined by λ​(t,n​(t))=0\lambda(t,n(t))=0, is continuous, and therefore bounded on [0,1].
Thus, n​(t)−R~t​(ω∗)n(t)-\tilde{R}\_{t}(\omega^{\*}) is bounded on [0,1][0,1] and therefore

|  |  |  |
| --- | --- | --- |
|  | −∞<N∗=mint∈[0,1]⁡(n​(t)−R~t​(ω∗))≤maxt∈[0,1]⁡(n​(t)−R~t​(ω∗))=N∗<∞.-\infty<N\_{\*}=\min\_{t\in[0,1]}(n(t)-\tilde{R}\_{t}(\omega^{\*}))\leq\max\_{t\in[0,1]}(n(t)-\tilde{R}\_{t}(\omega^{\*}))=N^{\*}<\infty. |  |

As λ​(t,⋅)\lambda(t,\cdot) is increasing, x​λ​(t,x+R~t​(ω∗))>0x\lambda(t,x+\tilde{R}\_{t}(\omega^{\*}))>0 on x∈ℝ\[−(N∗)−,(N∗)+]x\in\mathbb{R}\backslash[-(N\_{\*})^{-},(N^{\*})^{+}], hence

|  |  |  |
| --- | --- | --- |
|  | mint∈[0,1],x∈ℝ⁡x​λ​(t,x+R~t​(ω∗))=mint∈[0,1],x∈[−(N∗)−,(N∗)+]⁡x​λ​(t,x+R~t​(ω∗))=−C>−∞\min\_{t\in[0,1],x\in\mathbb{R}}x\lambda(t,x+\tilde{R}\_{t}(\omega^{\*}))=\min\_{t\in[0,1],x\in[-(N\_{\*})^{-},(N^{\*})^{+}]}x\lambda(t,x+\tilde{R}\_{t}(\omega^{\*}))=-C>-\infty |  |

and it follows from ([4.15](https://arxiv.org/html/2512.05011v1#S4.E15 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) that on [0,τ​(ω∗))[0,\tau(\omega^{\*}))

|  |  |  |
| --- | --- | --- |
|  | (u2​(t))′≤−u2​(t)2​(V​(t)−t)​d​t+c​d​t\displaystyle(u^{2}(t))^{\prime}\leq-\frac{u^{2}(t)}{2(V(t)-t)}dt+cdt |  |

where c=γ​C2c=\frac{\gamma C}{2}. Due to Gronwall’s inequality we obtain

|  |  |  |
| --- | --- | --- |
|  | u2​(t)≤c​e−∫0t12​(V​(u)−u)​𝑑u​∫0te∫0s12​(V​(u)−u)​𝑑u​𝑑s≤c~​(ω∗)​ for all ​t∈[0,τ​(ω∗)).u^{2}(t)\leq ce^{-\int\_{0}^{t}\frac{1}{2(V(u)-u)}du}\int\_{0}^{t}e^{\int\_{0}^{s}\frac{1}{2(V(u)-u)}du}ds\leq\tilde{c}(\omega^{\*})\mbox{ for all }t\in[0,\tau(\omega^{\*})). |  |

Note that c~​(ω∗)\tilde{c}(\omega^{\*}) is a finite constant as V​(t)−tV(t)-t is bounded away from zero on t∈[0,τ​(ω∗)]t\in[0,\tau(\omega^{\*})] as τ​(ω∗)<1\tau(\omega^{\*})<1. As c~​(ω∗)\tilde{c}(\omega^{\*}) does not depend on tt and R~⋅​(ω∗)\tilde{R}\_{\cdot}(\omega^{\*}) in bounded on [0,1][0,1] it leads to contradiction. Therefore τ​(ω)≥1\tau(\omega)\geq 1 for all ω∈Ω1\omega\in\Omega\_{1}.

Thus, we are left to establish that the solution of ([4.14](https://arxiv.org/html/2512.05011v1#S4.E14 "In 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.")) does not explode at 11.

To this end consider two processes

|  |  |  |
| --- | --- | --- |
|  | {d​Rtn+=d​Btℙ~+Ut−Rtn+V​(t)−t​d​t−γ​λ​(t,−n)​d​t.d​Rtn−=d​Btℙ~+Ut−Rtn−V​(t)−t​d​t−γ​λ​(t,n)​d​t.\begin{cases}dR^{n+}\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-R^{n+}\_{t}}{V(t)-t}dt-\gamma\lambda(t,-n)dt.\\ dR^{n-}\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-R^{n-}\_{t}}{V(t)-t}dt-\gamma\lambda(t,n)dt.\end{cases} |  |

Observe that until τn=τn+∧τn−\tau\_{n}=\tau\_{n}^{+}\wedge\tau\_{n}^{-}, where τn+=inf{t≥0:Rtn+>n}\tau\_{n}^{+}=\inf\{t\geq 0:R^{n+}\_{t}>n\} and τn−=inf{t≥0:Rtn−<n}\tau\_{n}^{-}=\inf\{t\geq 0:R^{n-}\_{t}<n\} we have, in view of Theorem 2.9 in DMB-CD,
Rtn−≤Rt≤Rtn+R^{n-}\_{t}\leq R\_{t}\leq R^{n+}\_{t} and therefore

|  |  |  |
| --- | --- | --- |
|  | Rt∧τnn−≤Rt∧τn≤Rt∧τnn+R^{n-}\_{t\wedge\tau\_{n}}\leq R\_{t\wedge\tau\_{n}}\leq R^{n+}\_{t\wedge\tau\_{n}} |  |

Note that for

|  |  |  |
| --- | --- | --- |
|  | R~tn+=Rtn++γ​e−∫0t1V​(s)−s​𝑑s​∫0tλ​(s,−n)​e∫0s1V​(u)−u​𝑑u​𝑑s\tilde{R}^{n+}\_{t}=R^{n+}\_{t}+\gamma e^{-\int\_{0}^{t}\frac{1}{V(s)-s}ds}\int\_{0}^{t}\lambda(s,-n)e^{\int\_{0}^{s}\frac{1}{V(u)-u}du}ds |  |

and

|  |  |  |
| --- | --- | --- |
|  | R~tn−=Rtn−+γ​e−∫0t1V​(s)−s​𝑑s​∫0tλ​(s,n)​e∫0s1V​(u)−u​𝑑u​𝑑s\tilde{R}^{n-}\_{t}=R^{n-}\_{t}+\gamma e^{-\int\_{0}^{t}\frac{1}{V(s)-s}ds}\int\_{0}^{t}\lambda(s,n)e^{\int\_{0}^{s}\frac{1}{V(u)-u}du}ds |  |

we obtain the following SDEs

|  |  |  |
| --- | --- | --- |
|  | {d​R~tn+=d​Btℙ~+Ut−R~tn+V​(t)−t​d​t.d​R~tn−=d​Btℙ~+Ut−R~tn−V​(t)−t​d​t.\begin{cases}d\tilde{R}^{n+}\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-\tilde{R}^{n+}\_{t}}{V(t)-t}dt.\\ d\tilde{R}^{n-}\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-\tilde{R}^{n-}\_{t}}{V(t)-t}dt.\end{cases} |  |

Due to the Theorem 5.2 in DMB-CD we conclude that R~1n+=R~1n−=U1\tilde{R}^{n+}\_{1}=\tilde{R}^{n-}\_{1}=U\_{1} and therefore R1n+=R1n−=U1R^{n+}\_{1}=R^{n-}\_{1}=U\_{1} (due to application of L’Hospital rule to e−∫0t1V​(s)−s​𝑑s∫0tλ(t,.)e∫0s1V​(u)−u​𝑑udse^{-\int\_{0}^{t}\frac{1}{V(s)-s}ds}\int\_{0}^{t}\lambda(t,.)e^{\int\_{0}^{s}\frac{1}{V(u)-u}du}ds) for any nn.

Thus, we have

|  |  |  |
| --- | --- | --- |
|  | 1[τn≥1]​U1≤1[τn≥1]​limt→1Rt≤1[τn≥1]​U1.1\_{[\tau\_{n}\geq 1]}U\_{1}\leq 1\_{[\tau\_{n}\geq 1]}\lim\_{t\rightarrow 1}R\_{t}\leq 1\_{[\tau\_{n}\geq 1]}U\_{1}. |  |

As ℙ~​[limn→∞τn≥1]=1\tilde{\mathbb{P}}[\lim\_{n\rightarrow\infty}\tau\_{n}\geq 1]=1 we conclude that limt→1Rt=U1\lim\_{t\rightarrow 1}R\_{t}=U\_{1} and in particular the solution of SDE does not explode on [0,1][0,1].

∎

## 5. Examples

### 5.1. Deterministic volatility of the signal

Consider the signal of the form

|  |  |  |
| --- | --- | --- |
|  | d​Zt=Σ​(t)​d​βt,Z0∼N​(0,q),Σ​(t)≥0.dZ\_{t}=\Sigma(t)d\beta\_{t},\quad Z\_{0}\sim N(0,q),\quad\Sigma(t)\geq 0. |  |

Suppose that Σ​(t)\Sigma(t) is continuously differentiable function on [0,1][0,1], q∈ℝ,q≥0q\in\mathbb{R},\,q\geq 0, which satisfies on [0,1)[0,1)

|  |  |  |
| --- | --- | --- |
|  | q+∫0tΣ2​(s)​𝑑s>tC​(C+γ​t)q+\int\_{0}^{t}\Sigma^{2}(s)ds>\frac{t}{C(C+\gamma t)} |  |

and

|  |  |  |
| --- | --- | --- |
|  | Σ​(1)≠1C−γ​q−γ​∫01Σ2​(s)​𝑑s\Sigma(1)\neq\frac{1}{C}-\gamma q-\gamma\int\_{0}^{1}\Sigma^{2}(s)ds |  |

for

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=−γ+γ2+4q+∫01Σ2​(t)​𝑑t2>0.C=\frac{-\gamma+\sqrt{\gamma^{2}+\frac{4}{q+\int\_{0}^{1}\Sigma^{2}(t)dt}}}{2}>0. |  | (5.16) |

###### Remark 5.

For instance, one of the signals satisfying the assumption stated above is the signal with constant volatility Σ​(t)=Σ\Sigma(t)=\Sigma, for which

|  |  |  |
| --- | --- | --- |
|  | (Σ2​t+q)​(C​γ​t+C2)>t,t∈[0,1)\left(\Sigma^{2}t+q)(C\gamma t+C^{2}\right)>t,\quad t\in[0,1) |  |

.
We can see that on the left side of this inequality we have parabola with roots −qΣ2-\frac{q}{\Sigma^{2}} and −Cγ-\frac{C}{\gamma} and, moreover, we can notice that this inequality becomes equality at t=1t=1.
In this case the inequality is equivalent to the condition of the derivative of the left part being equal or less than 1 at t=1t=1 or equivalently:

|  |  |  |
| --- | --- | --- |
|  | 2​Σ2​C​γ+C​q​γ+Σ2​C2≤1.2\Sigma^{2}C\gamma+Cq\gamma+\Sigma^{2}C^{2}\leq 1. |  |

This in its turn, may be true for example if Σ=q\Sigma=q and is sufficiently small, which shows us that our initial assumption can be achieved.

This signal can be rewritten in the form

|  |  |  |
| --- | --- | --- |
|  | d​Zt=σ​(t)​a​(V​(t))​d​βt,Z0=∫0V​(0)a​(s)​𝑑β~sdZ\_{t}=\sigma(t)a(V(t))d\beta\_{t},\quad Z\_{0}=\int\_{0}^{V(0)}a(s)d\tilde{\beta}\_{s} |  |

where β~\tilde{\beta} is independent of β\beta,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(t)\displaystyle V(t) | =\displaystyle= | 1γC−γ2​q−γ2​∫0tΣ2​(s)​𝑑s−Cγ,V​(0)=q​C21−γ​q​C>0\displaystyle\frac{1}{\frac{\gamma}{C}-\gamma^{2}q-\gamma^{2}\int\_{0}^{t}\Sigma^{2}(s)ds}-\frac{C}{\gamma},\quad V(0)=\frac{qC^{2}}{1-\gamma qC}>0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ​(t)\displaystyle\sigma(t) | =\displaystyle= | V′​(t)=Σ​(t)1C−γ​q−γ​∫0tΣ2​(s)​𝑑s\displaystyle\sqrt{V^{\prime}(t)}=\frac{\Sigma(t)}{\frac{1}{C}-\gamma q-\gamma\int\_{0}^{t}\Sigma^{2}(s)ds} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a​(t)\displaystyle a(t) | =\displaystyle= | 1γ​t+C\displaystyle\frac{1}{\gamma t+C} |  |

and CC is given by ([5.16](https://arxiv.org/html/2512.05011v1#S5.E16 "In 5.1. Deterministic volatility of the signal ‣ 5. Examples ‣ Risk aversion of insider and dynamic asymmetric information.")). Those satisfy the assumption ([2.1](https://arxiv.org/html/2512.05011v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")), since the above assumption on Σ​(t)\Sigma(t) gives us that V​(t)>tV(t)>t on [0,1)[0,1). Thus, it is left to check that applying L’Hopital’s rule we get

|  |  |  |
| --- | --- | --- |
|  | limt→1D2​(t)​Λ​(t)​log⁡Λ​(t)=0.\lim\_{t\to 1}D^{2}(t)\Lambda(t)\log{\Lambda(t)}=0. |  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limt→1D2​(t)​Λ​(t)​log⁡Λ​(t)\displaystyle\lim\_{t\to 1}D^{2}(t)\Lambda(t)\log{\Lambda(t)} | =\displaystyle= | limt→1log⁡Λ​(t)1D2​(t)​Λ​(t)=\displaystyle\lim\_{t\to 1}\frac{\log{\Lambda(t)}}{\frac{1}{D^{2}(t)\Lambda(t)}}= |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limt→1V​(t)−t21+σ2​(t)−V​(t)−tD2​(t)​Λ​(t)\displaystyle\lim\_{t\to 1}\frac{V(t)-t}{\frac{2}{1+\sigma^{2}(t)}-\frac{V(t)-t}{D^{2}(t)\Lambda(t)}} | =\displaystyle= | 0,\displaystyle 0, |  |

since again due to L’Hopital’s rule in our assumptions we have

|  |  |  |
| --- | --- | --- |
|  | limt→1V​(t)−tD2​(t)​Λ​(t)=limt→1(σ2​(t)−1)​D2​(t)+2​D2​(t)D4​(t)1+σ2​(t)D2​(t)=1.\lim\_{t\to 1}\frac{V(t)-t}{D^{2}(t)\Lambda(t)}=\lim\_{t\to 1}\frac{\frac{(\sigma^{2}(t)-1)D^{2}(t)+2D^{2}(t)}{D^{4}(t)}}{\frac{1+\sigma^{2}(t)}{D^{2}(t)}}=1. |  |

Our theorem states that in this case the equilibrium is given by c=0c=0,

|  |  |  |
| --- | --- | --- |
|  | w​(t,x)=a​(t,x)=1γ​t+Cw(t,x)=a(t,x)=\frac{1}{\gamma t+C} |  |

and

|  |  |  |
| --- | --- | --- |
|  | d​θt=αt​d​t,αt=w​(t,ξt)​ρx​(t,ξt,V​(t),Zt)ρ​(t,ξt,V​(t),Zt),\displaystyle d\theta\_{t}=\alpha\_{t}dt,\hskip 14.22636pt\alpha\_{t}=w(t,\xi\_{t})\frac{\rho\_{x}(t,\xi\_{t},V(t),Z\_{t})}{\rho(t,\xi\_{t},V(t),Z\_{t})}, |  |

ρ​()\rho() is transition density of the process given by

|  |  |  |
| --- | --- | --- |
|  | d​ηt=1γ​t+C​d​βt.d\eta\_{t}=\frac{1}{\gamma t+C}d\beta\_{t}. |  |

Denoting

|  |  |  |
| --- | --- | --- |
|  | G​(s,t)=∫st1(γ​τ+C)2​𝑑τ=t−s(γ​s+C)​(γ​t+C)G(s,t)=\int\_{s}^{t}\frac{1}{(\gamma\tau+C)^{2}}d\tau=\frac{t-s}{(\gamma s+C)(\gamma t+C)} |  |

we get

|  |  |  |
| --- | --- | --- |
|  | ρ​(s,y,t,x)=12​π​G​(s,t)​e−(x−y)22​G​(s,t).\rho(s,y,t,x)=\frac{1}{\sqrt{2\pi G(s,t)}}e^{\frac{-(x-y)^{2}}{2G(s,t)}}. |  |

### 5.2. Quadratic volatility of signal

Consider the signal of the form

|  |  |  |
| --- | --- | --- |
|  | d​Zt=(−δ​Zt2+b​Zt+d)​d​β^t,0<|δ|<γ,dδ>0,Z0=ηt0,dZ\_{t}=(-\delta Z\_{t}^{2}+bZ\_{t}+d)d\hat{\beta}\_{t},\quad 0<|\delta|<\gamma,\quad\frac{d}{\delta}>0,\quad Z\_{0}=\eta\_{t\_{0}}, |  |

where t0=1−δ2γ2t\_{0}=1-\frac{\delta^{2}}{\gamma^{2}} and η\eta is the unique strong solution of

|  |  |  |
| --- | --- | --- |
|  | d​ηt=(−γ​ηt2+γ​bδ​ηt+γ​dδ)​d​βt,η0=0.d\eta\_{t}=\left(-\gamma\eta\_{t}^{2}+\frac{\gamma b}{\delta}\eta\_{t}+\frac{\gamma d}{\delta}\right)d\beta\_{t},\quad\eta\_{0}=0. |  |

We can notice that it is possible to represent this signal as

|  |  |  |
| --- | --- | --- |
|  | d​Zt=σ​(t)​a​(V​(t),Zt)​d​βtdZ\_{t}=\sigma(t)a(V(t),Z\_{t})d\beta\_{t} |  |

where we set βt=s​i​g​n​(δ)​β^t\beta\_{t}=sign(\delta)\hat{\beta}\_{t} and denote

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(t)\displaystyle V(t) | =\displaystyle= | γ2−δ2γ2+δ2γ2​t\displaystyle\frac{\gamma^{2}-\delta^{2}}{\gamma^{2}}+\frac{\delta^{2}}{\gamma^{2}}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ​(t)\displaystyle\sigma(t) | =\displaystyle= | |δ|γ\displaystyle\frac{|\delta|}{\gamma} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a​(t,x)\displaystyle a(t,x) | =\displaystyle= | −γ​x2+γ​bδ​x+γ​dδ.\displaystyle-\gamma x^{2}+\frac{\gamma b}{\delta}x+\frac{\gamma d}{\delta}. |  |

Direct calculations show that this will satisfy the Assumption [2.1](https://arxiv.org/html/2512.05011v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.").
Thus, due to Theorem [4.1](https://arxiv.org/html/2512.05011v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4. General Result ‣ Risk aversion of insider and dynamic asymmetric information.") the equilibrium is given by c=0c=0,

|  |  |  |
| --- | --- | --- |
|  | w​(t,x)=a​(t,x)=−γ​x2+γ​bδ​x+γ​dδw(t,x)=a(t,x)=-\gamma x^{2}+\frac{\gamma b}{\delta}x+\frac{\gamma d}{\delta} |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​θt=αt​d​t,αt=w​(t,ξt)​ρx​(t,ξt,V​(t),Zt)ρ​(t,ξt,V​(t),Zt),\displaystyle d\theta\_{t}=\alpha\_{t}dt,\hskip 14.22636pt\alpha\_{t}=w(t,\xi\_{t})\frac{\rho\_{x}(t,\xi\_{t},V(t),Z\_{t})}{\rho(t,\xi\_{t},V(t),Z\_{t})}, |  | (5.17) |

where ρ\rho is transition density of the process ZZ. An explicit form of this density function can be seen as Expression (11) in Ingersoll, ”Valuing Foreign Exchange Rate Derivatives with a Bounded Exchange Process”.

### 5.3. Static insider signal

|  |  |  |
| --- | --- | --- |
|  | Zt=Z1=η1,Z\_{t}=Z\_{1}=\eta\_{1}, |  |

where η\eta is the unique strong solution of

|  |  |  |
| --- | --- | --- |
|  | ηt=∫0ta​(s,ηs)​𝑑βs.\displaystyle\eta\_{t}=\int\_{0}^{t}a(s,\eta\_{s})d\beta\_{s}. |  |

and
a​(t,x)a(t,x) satisfies assumption ([2.1](https://arxiv.org/html/2512.05011v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")).

###### Remark 6.

It can be noticed that the two different cases of such Z1Z\_{1} have already been described in the literature:

1. (1)

   The case of static bounded Z1Z\_{1} was described in the work of Shi (2013),
2. (2)

   The case of static Z1Z\_{1}, where γ\gamma for a​(t,x)a(t,x) is sufficiently small, has been described in the work of Bose, Ekren (2023).

In this case we can consider as a new insider signal Zt~=ηV​(t)\tilde{Z\_{t}}=\eta\_{V(t)} for some V​(t)V(t) satisfying Assumption 2.1 and base insider strategy on Zt~\tilde{Z\_{t}}. Thus, obtained insider signal will satisfy the Theorem 4.1.

This shows us that there can be achieved equilibria, each for different V​(t)V(t).
These equilibria according to the achieved results will only differ by the insider strategy, but will have same weighting function and same ultimate benefit for the insider.

###### Remark 7.

Though the example of static insider signal does not formally satisfy our assumptions for the main theorem due to σ​(t)=0\sigma(t)=0 for this case, it is possible to directly apply the same approach.

First, let us take V​(t)=1V(t)=1 so it will satisfy other parts of the assumption ([2.1](https://arxiv.org/html/2512.05011v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2. Description of the market model ‣ Risk aversion of insider and dynamic asymmetric information.")), in which terms

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | D​(t)\displaystyle D(t) | =\displaystyle= | 1−t\displaystyle 1-t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Λ​(t)\displaystyle\Lambda(t) | =\displaystyle= | t1−t\displaystyle\frac{t}{1-t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limt→1D2​(t)​Λ​(t)​log⁡Λ​(t)\displaystyle\lim\_{t\to 1}D^{2}(t)\Lambda(t)\log{\Lambda(t)} | =\displaystyle= | 0.\displaystyle 0. |  |

Second, we can notice that a new probability measure defined in standard setting by

|  |  |  |
| --- | --- | --- |
|  | d​ℙ~d​ℚb​a​s​e|ℱ1β~,B=u​(v0,U0)u​(1,U1)=(v0,κv0)u​(1,κ1)\left.\frac{d\tilde{\mathbb{P}}}{d\mathbb{Q}^{base}}\right|\_{\mathcal{F}^{\tilde{\beta},B}\_{1}}=\frac{u(v\_{0},U\_{0})}{u(1,U\_{1})}=\frac{(v\_{0},\kappa\_{v\_{0}})}{u(1,\kappa\_{1})} |  |

will be unnecessary and the Theorem 5.2 from DMB-CD can be applied directly.

The final substantial difference from the standard apporoach in the case of static insider signal will consist in the application of Lemma 6.1 for the SDEs

|  |  |  |
| --- | --- | --- |
|  | {d​Ut=σ​(t)​d​βtℙ~,d​Rt=d​Btℙ~+Ut−RtV​(t)−t​d​t,\begin{cases}dU\_{t}=\sigma(t)d\beta^{\tilde{\mathbb{P}}}\_{t},\\ dR\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-R\_{t}}{V(t)-t}dt,\end{cases} |  |

and

|  |  |  |
| --- | --- | --- |
|  | {d​Ut=σ​(t)​d​βtℙ~,d​Rt=d​Btℙ~+Ut−RtV​(t)−t​d​t−γ​λ​(t,Rt)​d​t.\begin{cases}dU\_{t}=\sigma(t)d\beta^{\tilde{\mathbb{P}}}\_{t},\\ dR\_{t}=dB^{\tilde{\mathbb{P}}}\_{t}+\frac{U\_{t}-R\_{t}}{V(t)-t}dt-\gamma\lambda(t,R\_{t})dt.\end{cases} |  |

Now, since σ​(t)=0\sigma(t)=0, it will be enough to apply the Lemma 6.1 to
Following the proof of the Lemma [6.1](https://arxiv.org/html/2512.05011v1#S6.Thmlemma1 "Lemma 6.1. ‣ 6.1. Auxiliary results for main theorem ‣ 6. Appendix ‣ Risk aversion of insider and dynamic asymmetric information."), the required result is established

|  |  |  |
| --- | --- | --- |
|  | d​Rt=d​Bt+U1−RtV​(t)−t​d​t,dR\_{t}=dB\_{t}+\frac{U\_{1}-R\_{t}}{V(t)-t}dt, |  |

and

|  |  |  |
| --- | --- | --- |
|  | d​Rt=d​Bt+U1−RtV​(t)−t​d​t−γ​λ​(t,Rt)​d​t.dR\_{t}=dB\_{t}+\frac{U\_{1}-R\_{t}}{V(t)-t}dt-\gamma\lambda(t,R\_{t})dt. |  |

## 6. Appendix

### 6.1. Auxiliary results for main theorem

Here we present some auxiliary result that is required to prove the lemmas that establish the statement of the main theorem.

###### Lemma 6.1.

Consider filtered probability space (Ω,ℱ,{ℱt}t∈[0,1],ℚb​a​s​e)\left(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\in[0,1]},\mathbb{Q}^{base}\right) rich enough to support a dd-dimensional Brownian motion BB. Suppose that the following two SDEs

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=σ​(t)​d​Bt+μX​(t,Xt)​d​t,dX\_{t}=\sigma(t)dB\_{t}+\mu^{X}(t,X\_{t})dt, |  | (6.18) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=σ​(t)​d​Bt+μY​(t,Yt)​d​tdY\_{t}=\sigma(t)dB\_{t}+\mu^{Y}(t,Y\_{t})dt |  | (6.19) |

have unique strong solution on [0,1][0,1], where μX,Y\mu^{X,Y} are dd-dimensional continuous column functions on [0,1)×ℝd[0,1)\times\mathbb{R}^{d} and σ\sigma is continuous d∗dd\*d-matrix on [0,1)×ℝd×ℝd[0,1)\times\mathbb{R}^{d}\times\mathbb{R}^{d}. Assume further that

|  |  |  |
| --- | --- | --- |
|  | μ​(t,x):=μY​(t,x)−μX​(t,x)\mu(t,x):=\mu^{Y}(t,x)-\mu^{X}(t,x) |  |

is a dd-dimensional continuous column function on [0,1]×ℝd[0,1]\times\mathbb{R}^{d} and α−1​(t)\alpha^{-1}(t) is continuous d∗dd\*d-matrix on [0,1)×ℝd×ℝd[0,1)\times\mathbb{R}^{d}\times\mathbb{R}^{d} for αi​j​(t)=∑k=1dσi​k​(t)​σk​j​(t)\alpha\_{ij}(t)=\sum\_{k=1}^{d}\sigma\_{ik}(t)\sigma\_{kj}(t). Then

|  |  |  |
| --- | --- | --- |
|  | Lt=exp⁡{∫0t(α−1​(s)​μ​(s,Xs))T​σ​(s)​𝑑Bs−12​∫0t(α−1​(s)​μ​(s,Xs))T​μ​(s)​𝑑s}L\_{t}=\exp\left\{\int\_{0}^{t}(\alpha^{-1}(s)\mu(s,X\_{s}))^{T}\sigma(s)dB\_{s}-\frac{1}{2}\int\_{0}^{t}(\alpha^{-1}(s)\mu(s,X\_{s}))^{T}\mu(s)ds\right\} |  |

is a martingale on [0,1][0,1].

###### Proof.

Consider a canonical filtered space (C​([0,1],ℝd),(ℬt)t∈[0,1],ℬ1)(C([0,1],\mathbb{R}^{d}),({\mathcal{B}}\_{t})\_{t\in[0,1]},{\mathcal{B}}\_{1}) and 2 infinitesimal generators associated with the 2 systems of SDEs:

|  |  |  |
| --- | --- | --- |
|  | AtX=12​∑i,jdαi​j​(t)​∂2∂xi​∂xj+∑i=1dμiX​(t,x)​∂∂xi,A^{X}\_{t}=\frac{1}{2}\sum\_{i,j}^{d}\alpha\_{ij}(t)\frac{\partial^{2}}{\partial x\_{i}\partial x\_{j}}+\sum\_{i=1}^{d}\mu^{X}\_{i}(t,x)\frac{\partial}{\partial x\_{i}}, |  |

|  |  |  |
| --- | --- | --- |
|  | AtY=12​∑i,jdαi​j​(t)​∂2∂xi​∂xj+∑i=1dμiY​(t,x)​∂∂xi.A^{Y}\_{t}=\frac{1}{2}\sum\_{i,j}^{d}\alpha\_{ij}(t)\frac{\partial^{2}}{\partial x\_{i}\partial x\_{j}}+\sum\_{i=1}^{d}\mu^{Y}\_{i}(t,x)\frac{\partial}{\partial x\_{i}}. |  |

The martingale problems for (AX,δ0)(A^{X},\delta\_{0}) and (AY,δ0)(A^{Y},\delta\_{0}) are well-posed, since both respective SDEs have a strong unique solution (see Corollary 2.5 in DMB-CD). Denote the solutions of those martingale problems as PXP^{X} and PYP^{Y} respectively.

In view of Theorem 3.3 in Ruf15, due to continuity of μ\mu and α−1​(t)\alpha^{-1}(t)

|  |  |  |
| --- | --- | --- |
|  | PY​(∫01(α−1​(s)​μ​(s,Xs))T​μ​(s)​𝑑s<∞)=1P^{Y}\left(\int\_{0}^{1}(\alpha^{-1}(s)\mu(s,X\_{s}))^{T}\mu(s)ds<\infty\right)=1 |  |

the process

|  |  |  |
| --- | --- | --- |
|  | L~t=exp⁡{∫0t(α−1​(s)​μ​(s,Xs))T​(d​Xs−μX​(s,Xs)​d​s)−12​∫0t(α−1​(s)​μ​(s,Xs))T​μ​(s)​𝑑s}\tilde{L}\_{t}=\exp\left\{\int\_{0}^{t}(\alpha^{-1}(s)\mu(s,X\_{s}))^{T}(dX\_{s}-\mu^{X}(s,X\_{s})ds)-\frac{1}{2}\int\_{0}^{t}(\alpha^{-1}(s)\mu(s,X\_{s}))^{T}\mu(s)ds\right\} |  |

is a martingale under PXP^{X} on [0,1][0,1].

Next, consider the original filtered probability space (Ω,ℱ,{ℱt}t∈[0,1],ℚb​a​s​e)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\in[0,1]},\mathbb{Q}^{base}). As XX is the strong solution of ([6.18](https://arxiv.org/html/2512.05011v1#S6.E18 "In Lemma 6.1. ‣ 6.1. Auxiliary results for main theorem ‣ 6. Appendix ‣ Risk aversion of insider and dynamic asymmetric information.")), (X,B),(Ω,ℱ,ℚb​a​s​e),{ℱt}t∈[0,1](X,B),(\Omega,\mathcal{F},\mathbb{Q}^{base}),\{\mathcal{F}\_{t}\}\_{t\in[0,1]} is also a weak solution of ([6.18](https://arxiv.org/html/2512.05011v1#S6.E18 "In Lemma 6.1. ‣ 6.1. Auxiliary results for main theorem ‣ 6. Appendix ‣ Risk aversion of insider and dynamic asymmetric information.")). Thus, due to the Corollary 2.3 in DMB-CD, PX=ℚb​a​s​e​X−1P^{X}=\mathbb{Q}^{base}X^{-1}. Therefore LL is indeed a martingale on [0,1][0,1].
∎