---
authors:
- Eunjung Noh
doc_id: arxiv:2601.09872v1
family_id: arxiv:2601.09872
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A continuous-time Kyle model with price-responsive traders
url_abs: http://arxiv.org/abs/2601.09872v1
url_html: https://arxiv.org/html/2601.09872v1
venue: arXiv q-fin
version: 1
year: 2026
---


Eunjung Noh
Department of Mathematics and Computer Science, Rollins College, Winter Park, Florida 32789, USA
[enoh@rollins.edu](mailto:enoh@rollins.edu)

###### Abstract.

Classical Kyle-type models of informed trading typically treat noise trader demand as purely exogenous. In reality, many market participants react to price movements and news, generating feedback effects that can significantly alter market dynamics. This paper develops a continuous-time Kyle framework in which two types of price-responsive traders (momentum and contrarian traders) adjust their demand in response to price signals. This extension yields a finite-dimensional Kalman filter for price discovery and leads to a forward–backward Riccati system characterizing equilibrium. We show that when feedback is weak, equilibrium exists and is unique as a smooth perturbation of the classical Kyle solution, allowing us to derive explicit comparative statics for insider profits and price informativeness. For stronger feedback, the model generates rich dynamics, including potential multiplicity of equilibria and amplification effects. Our framework thus bridges the gap between purely exogenous noise and more realistic, behaviorally motivated trading.

###### Key words and phrases:

Market microstructure, Kyle model, price-responsive traders, filtering

###### 1991 Mathematics Subject Classification:

91G80, 91B26, 93E11

## 1. Introduction

Noise traders play a central role in modern models of financial markets by masking informative order flow and thereby enabling trade in the presence of asymmetric information. In the classical Kyle model [[26](https://arxiv.org/html/2601.09872v1#bib.bib59 "Continuous auctions and insider trading")] and its continuous-time extension by Back [[5](https://arxiv.org/html/2601.09872v1#bib.bib18 "Insider trading in continuous time")], noise trading is modeled as purely exogenous and price-inelastic: random orders arrive independently of fundamentals, prices, or past market activity. This assumption delivers analytical tractability and a sharp characterization of equilibrium, but abstracts from a key empirical observation: a substantial fraction of order flow in real markets reacts mechanically to price movements.

A large and growing empirical literature documents that many market participants, including trend-following hedge funds, certain classes of retail traders, and portfolio rules embedded in algorithmic execution, systematically adjust their holdings in response to recent price innovations rather than to underlying fundamentals. Such feedback trading generates endogenous correlation between prices and future order flow, influences the rate at which information is impounded into prices, and can amplify or dampen volatility depending on the strength and direction of the feedback. Despite its importance, the dynamic interaction between informed trading, price-responsive noise traders, and rational market-maker learning remains poorly understood in continuous time.

This paper develops a continuous-time Kyle model with endogenous, price-responsive noise traders. Instead of following a purely exogenous Brownian motion, aggregate noise trading incorporates mechanical responses to price changes through two economically distinct channels:

- momentum traders, who buy following price increases and sell after declines, and

- contrarian traders, who trade in the opposite direction.

These traders do not observe fundamentals and do not behave strategically. Their positions evolve according to linear mean-reverting dynamics driven by price innovations, allowing their behavior to be embedded within the inferential structure of the Kyle framework.

A central challenge in introducing endogenous feedback into continuous-time microstructure models is preserving finite-dimensional filtering. In the classical Back model, the market maker infers the latent fundamental directly from aggregate order flow, and the filtering problem remains one-dimensional. When order flow itself reacts to prices, the state space becomes endogenous and, a priori, infinite dimensional. This paper shows that by modeling momentum and contrarian positions as linear controlled diffusions, the market maker’s inference problem remains linear-Gaussian and can be solved through a finite-dimensional Kalman-Bucy filter. The resulting conditional covariance matrix satisfies a matrix Riccati equation, which couples with the insider’s optimal trading problem to produce a forward-backward Riccati system characterizing equilibrium.

This modeling innovation allows for a fully analytic treatment of feedback effects in continuous time. The presence of price-responsive traders distorts the informational content of order flow: prices now reflect not only private information revealed gradually through inconspicuous insider trading, but also mechanical trading that responds to past prices. The resulting feedback loop modifies the strength and timing of price discovery and introduces new stability considerations absent in the classical Kyle setting.

The main contributions of the paper are as follows.
First, we introduce a new continuous-time microstructure model in which aggregate noise trading depends on price innovations. Despite the endogeneity, the system remains linear–Gaussian, and all inference takes place in a finite-dimensional state space.
Second, when feedback parameters are small, equilibrium exists and is unique as a smooth perturbation of the classical Kyle solution. We derive explicit first-order comparative statics for price informativeness, insider trading intensity, and expected insider profits, showing how momentum or contrarian behavior affects information revelation through the filtering channel rather than through ad hoc changes in noise volatility.
As feedback strengthens, on the other hand, the stability properties that guarantee the Kyle equilibrium begin to fail. We identify three mathematically distinct breakdown mechanisms:
(i) finite-time divergence of the Riccati flow;
(ii) loss of contraction of the equilibrium fixed-point mapping; and
(iii) instability of the Kalman–Bucy filter.
These failures correspond to economically meaningful amplification effects and generate the possibility of equilibrium multiplicity.

Taken together, these results bridge the gap between classical Kyle models with exogenous noise and behavioral or algorithmic trading models with endogenous feedback. By preserving analytical tractability while incorporating mechanically price-responsive order flow, the model provides a flexible platform for studying learning, information aggregation, and stability in markets where nonstrategic traders react to prices.

The next section reviews prior studies. Section [3](https://arxiv.org/html/2601.09872v1#S3 "3. Model ‣ A continuous-time Kyle model with price-responsive traders") details the model. In Section [4](https://arxiv.org/html/2601.09872v1#S4 "4. Equilibrium Analysis ‣ A continuous-time Kyle model with price-responsive traders"), by exploiting the linear-Gaussian structure, we use Kalman-Bucy filter to obtain a coupled forward-backward system of equations that characterizes equilibrium. In Section [5](https://arxiv.org/html/2601.09872v1#S5 "5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders"), for small feedback parameter, we prove local existence and uniqueness of equilibrium, and provide a sufficient local condition for stability. In Section [6](https://arxiv.org/html/2601.09872v1#S6 "6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders"), amplification and potential multiplicity of equilibria is possible when feedback is strong. Then, we conclude in Section [7](https://arxiv.org/html/2601.09872v1#S7 "7. Conclusion ‣ A continuous-time Kyle model with price-responsive traders").

## 2. Literature review

The starting point of our analysis is the seminal model of Kyle [[26](https://arxiv.org/html/2601.09872v1#bib.bib59 "Continuous auctions and insider trading")], in which a privately informed insider trades strategically against competitive market makers who observe only aggregate order flow from noise traders. In continuous time, Back [[5](https://arxiv.org/html/2601.09872v1#bib.bib18 "Insider trading in continuous time")] shows that the insider’s optimal strategy is inconspicuous, that prices reveal the fundamental gradually, and that equilibrium can be characterized through a scalar Riccati equation for the conditional variance of the asset value.
Many other extensions of the problem while retaining the exogeneity of noise trading have been studied [[1](https://arxiv.org/html/2601.09872v1#bib.bib27 "Imperfect competition among informed traders"), [2](https://arxiv.org/html/2601.09872v1#bib.bib83 "Optimal transport and risk aversion in Kyle’s model of informed trading"), [3](https://arxiv.org/html/2601.09872v1#bib.bib79 "Activism, strategic trading, and liquidity"), [4](https://arxiv.org/html/2601.09872v1#bib.bib19 "Long-lived information and intraday patterns"), [6](https://arxiv.org/html/2601.09872v1#bib.bib20 "Insider trading and risk aversion"), [8](https://arxiv.org/html/2601.09872v1#bib.bib23 "Kyle–Back models with risk aversion and non-Gaussian beliefs"), [9](https://arxiv.org/html/2601.09872v1#bib.bib22 "Multidimensional Kyle–Back model with a risk averse informed trader"), [12](https://arxiv.org/html/2601.09872v1#bib.bib24 "Insider trading in an equilibrium model with default: a passage from reduced-form to structural modelling"), [11](https://arxiv.org/html/2601.09872v1#bib.bib25 "Dynamic Markov bridges motivated by models of insider trading"), [16](https://arxiv.org/html/2601.09872v1#bib.bib80 "Financial equilibrium with asymmetric information and random horizon"), [14](https://arxiv.org/html/2601.09872v1#bib.bib29 "Markovian Nash equilibrium in financial markets with asymmetric information and related forward–backward systems"), [15](https://arxiv.org/html/2601.09872v1#bib.bib30 "On pricing rules and optimal strategies in general Kyle-Back models"), [18](https://arxiv.org/html/2601.09872v1#bib.bib70 "Solvability of the Gaussian Kyle model with imperfect information and risk aversion"), [17](https://arxiv.org/html/2601.09872v1#bib.bib82 "Informed trading via Monge–Kantorovich duality"), [19](https://arxiv.org/html/2601.09872v1#bib.bib81 "Trading constraints in continuous-time Kyle models"), [20](https://arxiv.org/html/2601.09872v1#bib.bib47 "Insider trading, stochastic liquidity, and equilibrium prices"), [21](https://arxiv.org/html/2601.09872v1#bib.bib78 "Kyle-Back’s model with Lévy noise"), [24](https://arxiv.org/html/2601.09872v1#bib.bib46 "Kyle’s model with stochastic liquidity")].

A core limitation of this literature is that noise traders are modeled as price-inelastic and behaviorally featureless. The present paper extends the Kyle paradigm by introducing endogenous price-responsive noise traders while preserving continuous-time tractability through a finite-dimensional Kalman–Bucy filtering structure. This departs from existing extensions in which tractability relies heavily on exogenous Brownian noise.

A second strand of literature examines price–order flow feedback. Cespa and Vives [[13](https://arxiv.org/html/2601.09872v1#bib.bib4 "Dynamic trading and asset prices: keynes vs. Hayek")] show that prices serve as both information carriers and coordination devices, potentially generating amplification and multiplicity when investors place weight on public signals. Relatedly, He and Krishnamurthy [[25](https://arxiv.org/html/2601.09872v1#bib.bib5 "Intermediary asset pricing")], Xiong [[30](https://arxiv.org/html/2601.09872v1#bib.bib11 "Convergence trading with wealth effects: an amplification mechanism in financial markets")], and Brunnermeier [[10](https://arxiv.org/html/2601.09872v1#bib.bib12 "Asset pricing under asymmetric information: bubbles, crashes, technical analysis, and herding")] study feedback loops in which beliefs or risk constraints cause price movements to reinforce themselves. Collin-Dufresne and Fos [[20](https://arxiv.org/html/2601.09872v1#bib.bib47 "Insider trading, stochastic liquidity, and equilibrium prices")] analyzes equilibria with stochastic liquidity, generating time-varying market depth and rich price–volume comovement. However, these frameworks do not specify mechanical trading rules tied directly to price innovations, nor do they modify the filtering structure in which private information is inferred from order flow.

Behavioral finance challenges the classical view of noise traders as passive liquidity providers, emphasizing instead that such agents often behave as if they have information when they do not [[7](https://arxiv.org/html/2601.09872v1#bib.bib17 "Noise")]. These traders commonly rely on technical rules or “popular models” [[28](https://arxiv.org/html/2601.09872v1#bib.bib1 "Stock prices and social dynamics"), [29](https://arxiv.org/html/2601.09872v1#bib.bib2 "Speculative prices and popular models")] and may exhibit price-responsive feedback behavior, including positive-feedback or trend-chasing strategies [[23](https://arxiv.org/html/2601.09872v1#bib.bib10 "Positive feedback investment strategies and destabilizing rational speculation")] as well as misguided contrarianism. Such trading induces serial correlation in returns [[27](https://arxiv.org/html/2601.09872v1#bib.bib8 "Feedback traders and stock return autocorrelations: evidence from a century of daily data")] and, as agent-based simulations show, can amplify volatility and distort prices [[22](https://arxiv.org/html/2601.09872v1#bib.bib14 "Noise traders in an agent-based artificial stock market")].
While these studies demonstrate the prevalence of price-based trading, they rely on discrete-time or reduced-form settings. The present paper incorporates these momentum and contrarian forces directly into a structural continuous-time microstructure equilibrium, showing how mechanical rules alter the filtering channel through which private information is reflected in prices.

## 3. Model

We consider a continuous-time version of the Kyle (1985) market in which a single risky asset is traded over the time interval [0,T][0,T]. All stochastic processes are defined on a filtered probability space
(Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) satisfying the usual conditions. The terminal fundamental value of the asset, denoted vv, is a normally distributed random variable with mean 0 and variance σv2\sigma\_{v}^{2}. Three types of agents interact in the market: an informed trader, a population of price-responsive noise traders, and a competitive market maker.

The informed trader observes the value vv at time 0 and trades continuously at a rate θt\theta\_{t}. Her cumulative position satisfies

|  |  |  |
| --- | --- | --- |
|  | d​Θt=θt​d​t,Θ0=0.d\Theta\_{t}=\theta\_{t}dt,\quad\Theta\_{0}=0\ . |  |

In contrast to the classical setting, we assume that there are two distinct types of price-responsive traders: *trend followers (momentum traders)* and *contrarians*. Let ZtZ\_{t} denote their cumulative order flow, which evolves according to

|  |  |  |
| --- | --- | --- |
|  | d​Zt=μt​d​t+σz​d​Wt,dZ\_{t}=\mu\_{t}dt+\sigma\_{z}dW\_{t}\ , |  |

where WtW\_{t} is a standard Brownian motion capturing exogenous random orders, and the drift μt\mu\_{t} represents systematic (possibly price-dependent) behavior, with

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | μt=γF​mt+γC​ct+σε​εt.\mu\_{t}=\gamma\_{F}m\_{t}+\gamma\_{C}c\_{t}+\sigma\_{\varepsilon}\varepsilon\_{t}\ . |  |

Here, mtm\_{t} is the aggregate position of trend followers, ctc\_{t} is the aggregate position of contrarians, γF,γC∈ℝ\gamma\_{F},\gamma\_{C}\in\mathbb{R} are exposure parameters,
and εt\varepsilon\_{t} is a mean-zero Brownian-driven noise term (scale σε\sigma\_{\varepsilon}) independent of other sources.

The dynamics of mtm\_{t} and ctc\_{t} follow linear mean-reverting processes driven by price innovations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.2) |  | d​mt\displaystyle dm\_{t} | =−αm​mt​d​t+κm​d​Pt+σm​d​Btm,\displaystyle=-\alpha\_{m}m\_{t}\,dt+\kappa\_{m}\,dP\_{t}+\sigma\_{m}\,dB^{m}\_{t}\ , |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.3) |  | d​ct\displaystyle dc\_{t} | =−αc​ct​d​t−κc​d​Pt+σc​d​Btc,\displaystyle=-\alpha\_{c}c\_{t}\,dt-\kappa\_{c}\,dP\_{t}+\sigma\_{c}\,dB^{c}\_{t}\ , |  |

where
αm,αc>0\alpha\_{m},\alpha\_{c}>0 are mean-reversion rates,
κm,κc≥0\kappa\_{m},\kappa\_{c}\geq 0 measure sensitivity to price changes (trend followers respond positively, contrarians negatively),
and Btm,BtcB^{m}\_{t},B^{c}\_{t} are independent Brownian motions, independent of the asset value and other noise.

The market maker observes only the total order flow

|  |  |  |
| --- | --- | --- |
|  | Yt=Θt+Zt,Y\_{t}=\Theta\_{t}+Z\_{t}\ , |  |

and sets the market-clearing price PtP\_{t} based on ℱtY=σ(Ys:s≤t)\mathcal{F}\_{t}^{Y}=\sigma(Y\_{s}:s\leq t).
The insider’s information at time tt is given by

|  |  |  |
| --- | --- | --- |
|  | ℱt:=σ​(v)∨ℱtY,\mathcal{F}\_{t}:=\sigma(v)\vee\mathcal{F}\_{t}^{Y}, |  |

while the market maker and all other traders condition only on ℱtY\mathcal{F}\_{t}^{Y}.
All endogenous order flow components are assumed to be ℱtY\mathcal{F}\_{t}^{Y}-adapted, so that prices remain measurable with respect to the public filtration.

###### Remark 3.1.

In contrast to classical Kyle models, the price-responsive traders introduced here are endogenous and generate order flow that depends on prices. As such, they do not provide purely exogenous liquidity. To ensure gradual information revelation and to preserve a well-defined filtering problem, we retain an exogenous noise component WtW\_{t} in aggregate order flow ZtZ\_{t}. This residual noise captures liquidity-motivated trading unrelated to prices or fundamentals and plays the same informational role as noise traders in the classical Kyle framework.

Under rational expectations, the price equals the conditional expectation of the asset value given public information

|  |  |  |
| --- | --- | --- |
|  | Pt=𝔼​[v|ℱtY].P\_{t}=\mathbb{E}[v|\mathcal{F}\_{t}^{Y}]\ . |  |

Following the usual linear–Gaussian formulation,
price dynamics can be written as

|  |  |  |
| --- | --- | --- |
|  | d​Pt=λt​d​Yt,dP\_{t}=\lambda\_{t}dY\_{t}\ , |  |

where λt\lambda\_{t} is the price impact coefficient determined endogenously in equilibrium.

The informed trader chooses her trading strategy to maximize expected terminal wealth

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U​(XT)|ℱ0],XT=∫0T(v−Pt)​θt​𝑑t,\mathbb{E}[U(X\_{T})|\mathcal{F}\_{0}]\ ,\quad X\_{T}=\int\_{0}^{T}(v-P\_{t})\theta\_{t}dt\ , |  |

where XTX\_{T} is the terminal wealth and UU is a utility function. Unless otherwise noted, we assume risk neutrality U​(x)=xU(x)=x.

###### Definition 3.2.

(Admissible Strategies)
An informed trader’s trading strategy is a real-valued process θ=(θt)t∈[0,T]\theta=(\theta\_{t})\_{t\in[0,T]} representing the rate of order submission.
A strategy θ\theta is said to be *admissible* if it satisfies the following conditions:

1. (1)

   Adaptedness.
   θ\theta is progressively measurable with respect to the insider’s information filtration
   ℱt=σ​(v)∨ℱtY.\mathcal{F}\_{t}=\sigma(v)\vee\mathcal{F}\_{t}^{Y}.
2. (2)

   Integrability.
   θ\theta is square-integrable in the sense that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[∫0Tθt2​𝑑t]<∞.\mathbb{E}\!\left[\int\_{0}^{T}\theta\_{t}^{2}\,dt\right]<\infty. |  |
3. (3)

   Well-defined order flow.
   The resulting order flow process
   ∫0tθs​𝑑s\int\_{0}^{t}\theta\_{s}\,ds
   is of finite variation and the aggregate order flow YY is well-defined.

The set of admissible strategies is denoted by 𝒜\mathcal{A}.

###### Definition 3.3.

(Equilibrium)
An equilibrium consists of a pricing rule P∗P^{\*} and a trading strategy θ∗\theta^{\*} such that

* (a)

  (Optimality) Given the pricing rule P∗P^{\*}, the informed trader’s trading strategy θ∗\theta^{\*} maximizes expected terminal wealth

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼​[XT|ℱ0],XT=∫0T(v−Pt)​θt​𝑑t.\mathbb{E}[X\_{T}|\mathcal{F}\_{0}],\quad X\_{T}=\int\_{0}^{T}(v-P\_{t})\theta\_{t}dt\ . |  |
* (b)

  (Rational pricing) Given the informed trader’s trading strategy θ∗\theta^{\*}, the market maker sets prices P∗P^{\*} according to rational expectations

  |  |  |  |
  | --- | --- | --- |
  |  | Pt=𝔼[v|ℱtY],ℱtY=σ(Ys:s≤t),P\_{t}=\mathbb{E}[v|\mathcal{F}\_{t}^{Y}],\quad\mathcal{F}\_{t}^{Y}=\sigma(Y\_{s}:s\leq t)\ , |  |

  where YtY\_{t} denotes aggregate order flow.

This specification preserves the linear-Gaussian structure, enabling a finite-dimensional Kalman-Bucy filter for price inference and tractable equilibrium analysis.

The next section reformulates this equilibrium problem as a self-consistent filtering fixed point linking the insider’s strategy, the market maker’s inference, and the feedback dynamics of price-responsive traders.

## 4. Equilibrium Analysis

### 4.1. State-space representation and price filtering

With momentum and contrarian traders, the system state becomes finite-dimensional. Define

|  |  |  |
| --- | --- | --- |
|  | xt:=(v,mt,ct)⊤,x\_{t}:=(v,m\_{t},c\_{t})^{\top}\ , |  |

where vv is the terminal asset value, and mt,ctm\_{t},c\_{t} are the positions of trend followers and contrarians. The dynamics are linear

|  |  |  |
| --- | --- | --- |
|  | d​xt=A​xt​d​t+B​d​Wt+ut​d​t,dx\_{t}=Ax\_{t}\,dt+B\,dW\_{t}+u\_{t}\,dt\ , |  |

where
A=(0000−αm000−αc)A=\begin{pmatrix}0&0&0\\
0&-\alpha\_{m}&0\\
0&0&-\alpha\_{c}\end{pmatrix} is the drift matrix,
BB collects diffusion coefficients from (σm,σc,σε)(\sigma\_{m},\sigma\_{c},\sigma\_{\varepsilon}),
and utu\_{t} represents deterministic inputs from price-dependent drifts.

The observation equation for total order flow is

|  |  |  |
| --- | --- | --- |
|  | d​Yt=θt​d​t+μt​d​t+σz​d​Wt,dY\_{t}=\theta\_{t}\,dt+\mu\_{t}\,dt+\sigma\_{z}\,dW\_{t}\ , |  |

where μt=γF​mt+γC​ct+σε​εt\mu\_{t}=\gamma\_{F}m\_{t}+\gamma\_{C}c\_{t}+\sigma\_{\varepsilon}\varepsilon\_{t}.

Because the system is linear and Gaussian, the market maker can compute the filtered state x^t=𝔼​[xt∣ℱtY]\hat{x}\_{t}=\mathbb{E}[x\_{t}\mid\mathcal{F}^{Y}\_{t}] and its covariance

|  |  |  |
| --- | --- | --- |
|  | Σt=Cov⁡(xt−x^t∣ℱtY)=(Σv​v​(t)Σv​m​(t)Σv​c​(t)Σv​m​(t)Σm​m​(t)Σm​c​(t)Σv​c​(t)Σm​c​(t)Σc​c​(t)),Σ0=(σv2000Var⁡(m0)000Var⁡(c0)).\Sigma\_{t}=\operatorname{Cov}(x\_{t}-\hat{x}\_{t}\mid\mathcal{F}^{Y}\_{t})=\begin{pmatrix}\Sigma\_{vv}(t)&\Sigma\_{vm}(t)&\Sigma\_{vc}(t)\\ \Sigma\_{vm}(t)&\Sigma\_{mm}(t)&\Sigma\_{mc}(t)\\ \Sigma\_{vc}(t)&\Sigma\_{mc}(t)&\Sigma\_{cc}(t)\end{pmatrix},\qquad\Sigma\_{0}=\begin{pmatrix}\sigma\_{v}^{2}&0&0\\ 0&\operatorname{Var}(m\_{0})&0\\ 0&0&\operatorname{Var}(c\_{0})\end{pmatrix}. |  |

The covariance evolves according to the matrix Riccati equation

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | Σ˙t=A​Σt+Σt​A⊤+Q−Σt​Ct⊤​R−1​Ct​Σt,\dot{\Sigma}\_{t}=A\Sigma\_{t}+\Sigma\_{t}A^{\top}+Q-\Sigma\_{t}C\_{t}^{\top}R^{-1}C\_{t}\Sigma\_{t}\ , |  |

where
Q=diag⁡(0,σm2,σc2)Q=\operatorname{diag}(0,\sigma\_{m}^{2},\sigma\_{c}^{2}) is the state-noise covariance,
Ct=(βt,γF,γC)C\_{t}=(\beta\_{t},\gamma\_{F},\gamma\_{C}) is the measurement row vector capturing how (v,m,c)(v,m,c) enter the drift of YtY\_{t},
and R=σz2R=\sigma\_{z}^{2} is the observation noise variance.

The Kalman gain is

|  |  |  |
| --- | --- | --- |
|  | Kt=Σt​Ct⊤​R−1,K\_{t}=\Sigma\_{t}C\_{t}^{\top}R^{-1}\ , |  |

and the price evolves as

|  |  |  |
| --- | --- | --- |
|  | d​Pt=e1⊤​Kt​σz​d​W~t,dP\_{t}=e\_{1}^{\top}K\_{t}\,\sigma\_{z}\,d\tilde{W}\_{t}\ , |  |

where e1=(1,0,0)⊤e\_{1}=(1,0,0)^{\top} and W~t\tilde{W}\_{t} is the innovation process defined by

|  |  |  |
| --- | --- | --- |
|  | d​W~t=d​Yt−𝔼​[d​Yt∣ℱtY]σz.d\tilde{W}\_{t}=\frac{dY\_{t}-\mathbb{E}[dY\_{t}\mid\mathcal{F}^{Y}\_{t}]}{\sigma\_{z}}\ . |  |

This formulation preserves the linear-Gaussian structure, enabling explicit computation of the filtering equations and equilibrium conditions.

### 4.2. Equilibrium restriction and inconspicuous trading

In principle, one could allow the informed trader to choose a general adapted trading rate θt\theta\_{t}, so that d​Θt=θt​d​td\Theta\_{t}=\theta\_{t}dt. However, in the present setting such general strategies would lead to a nonlinear filtering problem for the market maker and destroy the Gaussian structure of beliefs. As a consequence, prices would no longer admit a tractable representation, and equilibrium characterization would require solving a fully nonlinear stochastic control and filtering problem.

We therefore restrict attention to linear strategies of the form

|  |  |  |
| --- | --- | --- |
|  | θt=βt​(v−Pt),\theta\_{t}=\beta\_{t}(v-P\_{t})\ , |  |

where βt\beta\_{t} is deterministic and locally square-integrable. Within the linear-Gaussian class, such strategies are optimal, yield inconspicuous trading under rational pricing, and lead to a closed finite-dimensional characterization of equilibrium via Kalman-Bucy filtering and Riccati equations.

In the following lemma, we introduce and prove the inconspicuousness of a trading strategy in our model setup. It’s not something we assume to start, but a simple result we have as many other continuous-time Kyle models.

###### Lemma 4.1.

(Inconspicuousness of linear strategies)
Suppose the informed trader follows a linear strategy of the form

|  |  |  |
| --- | --- | --- |
|  | θt=βt​(v−Pt),\theta\_{t}=\beta\_{t}(v-P\_{t})\ , |  |

where βt\beta\_{t} is deterministic and locally square-integrable. Then, under rational pricing, the informed trader’s order flow is inconspicuous in the sense that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[θt|ℱtY]=0for allt∈[0,T].\mathbb{E}[\theta\_{t}|\mathcal{F}\_{t}^{Y}]=0\quad\text{for all}\quad t\in[0,T]\ . |  |

###### Proof.

By rational pricing,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[v−Pt|ℱtY]=0.\mathbb{E}[v-P\_{t}|\mathcal{F}\_{t}^{Y}]=0\ . |  |

Since βt\beta\_{t} is deterministic, the result follows immediately.
∎

###### Remark 4.2.

In contrast to classical Kyle models with purely exogenous noise, aggregate order flow in the present model includes endogenous, price-responsive components and therefore does not have the same law as exogenous noise. Inconspicuousness here refers instead to the absence of predictable drift in the informed trader’s orders conditional on public information, which is sufficient to sustain gradual information revelation and rational pricing.

### 4.3. Informed trader’s optimization problem

Under risk neutrality, the terminal wealth of the insider is, by integration by parts,

|  |  |  |
| --- | --- | --- |
|  | XT=ΘT​(v−PT)+∫0TΘt​𝑑Pt=∫0Tβt​(v−Pt)2​𝑑t.X\_{T}=\Theta\_{T}(v-P\_{T})+\int\_{0}^{T}\Theta\_{t}dP\_{t}=\int\_{0}^{T}\beta\_{t}(v-P\_{t})^{2}\,dt\ . |  |

For a given deterministic β\beta, the expected profit is

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[XT∣ℱ0]=∫0Tβt​Σv​v​(t)​𝑑t,\mathbb{E}[X\_{T}\mid\mathcal{F}\_{0}]=\int\_{0}^{T}\beta\_{t}\Sigma\_{vv}(t)\,dt\ , |  |

where Σv​v​(t)=Var⁡(v−Pt∣ℱtY)\Sigma\_{vv}(t)=\operatorname{Var}(v-P\_{t}\mid\mathcal{F}\_{t}^{Y}) is the (1,1)(1,1) entry of the covariance matrix Σt\Sigma\_{t}. The insider chooses β\beta to maximize this integral subject to the Riccati dynamics for Σt\Sigma\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxβ\displaystyle\max\_{\beta} | J​(β):=∫0Tβt​Σv​v​(t)​𝑑t,\displaystyle J(\beta)=\int\_{0}^{T}\beta\_{t}\Sigma\_{vv}(t)\,dt\ , |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | Σ˙t=A​Σt+Σt​A⊤+Q−Σt​Ct⊤​R−1​Ct​Σt,\displaystyle\dot{\Sigma}\_{t}=A\Sigma\_{t}+\Sigma\_{t}A^{\top}+Q-\Sigma\_{t}C\_{t}^{\top}R^{-1}C\_{t}\Sigma\_{t}\ , |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Σ0⪰0,Σv​v​(T)=0.\displaystyle\Sigma\_{0}\succeq 0,\quad\Sigma\_{vv}(T)=0\ . |  |

This is a two-point boundary value problem. To apply Pontryagin’s Maximum Principle, define the Hamiltonian

|  |  |  |
| --- | --- | --- |
|  | H​(t,Σt,βt,Λt)=βt​Σv​v​(t)+⟨Λt,Σ˙t⟩,H(t,\Sigma\_{t},\beta\_{t},\Lambda\_{t})=\beta\_{t}\Sigma\_{vv}(t)+\langle\Lambda\_{t},\dot{\Sigma}\_{t}\rangle\ , |  |

where Λt\Lambda\_{t} is the adjoint matrix and ⟨A,B⟩=t​r​a​c​e​(AT​B)\langle A,B\rangle=trace{(A^{T}B)} is the inner product of matrices.
The first-order condition (FOC) for βt\beta\_{t} is

|  |  |  |
| --- | --- | --- |
|  | ∂H∂βt=Σv​v​(t)+⟨Λt,∂Σ˙t∂βt⟩=0.\frac{\partial H}{\partial\beta\_{t}}=\Sigma\_{vv}(t)+\langle\Lambda\_{t},\frac{\partial\dot{\Sigma}\_{t}}{\partial\beta\_{t}}\rangle=0\ . |  |

The adjoint Λt\Lambda\_{t} satisfies the backward ODE

|  |  |  |
| --- | --- | --- |
|  | −Λ˙t=∂H∂Σt,ΛT=(p,0,…,0),-\dot{\Lambda}\_{t}=\frac{\partial H}{\partial\Sigma\_{t}}\ ,\qquad\Lambda\_{T}=(p,0,\dots,0)\ , |  |

where pp is a Lagrange multiplier enforcing Σv​v​(T)=0\Sigma\_{vv}(T)=0. Together, the system consists of

* •

  Forward Riccati ODE for Σt\Sigma\_{t},
* •

  Backward adjoint ODE for Λt\Lambda\_{t},
* •

  Pointwise algebraic FOC for βt\beta\_{t},
* •

  Terminal condition Σv​v​(T)=0\Sigma\_{vv}(T)=0.

This defines the equilibrium as a coupled forward-backward system.

### 4.4. Covariance dynamics and Riccati system

Writing out the Riccati equation ([4.1](https://arxiv.org/html/2601.09872v1#S4.E1 "In 4.1. State-space representation and price filtering ‣ 4. Equilibrium Analysis ‣ A continuous-time Kyle model with price-responsive traders")) component-wise gives the following system of ODEs

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ˙v​v\displaystyle\dot{\Sigma}\_{vv} | =−1σz2​(βt2​Σv​v2+2​βt​γF​Σv​v​Σv​m+2​βt​γC​Σv​v​Σv​c),\displaystyle=-\frac{1}{\sigma\_{z}^{2}}\big(\beta\_{t}^{2}\Sigma\_{vv}^{2}+2\beta\_{t}\gamma\_{F}\Sigma\_{vv}\Sigma\_{vm}+2\beta\_{t}\gamma\_{C}\Sigma\_{vv}\Sigma\_{vc}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ˙v​m\displaystyle\dot{\Sigma}\_{vm} | =−αm​Σv​m−1σz2​(βt2​Σv​v​Σv​m+βt​γF​(Σv​m2+Σv​v​Σm​m)+βt​γC​(Σv​m​Σv​c+Σv​v​Σm​c)),\displaystyle=-\alpha\_{m}\Sigma\_{vm}-\frac{1}{\sigma\_{z}^{2}}\big(\beta\_{t}^{2}\Sigma\_{vv}\Sigma\_{vm}+\beta\_{t}\gamma\_{F}(\Sigma\_{vm}^{2}+\Sigma\_{vv}\Sigma\_{mm})+\beta\_{t}\gamma\_{C}(\Sigma\_{vm}\Sigma\_{vc}+\Sigma\_{vv}\Sigma\_{mc})\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ˙v​c\displaystyle\dot{\Sigma}\_{vc} | =−αc​Σv​c−1σz2​(βt2​Σv​v​Σv​c+βt​γF​(Σv​m​Σv​c+Σv​v​Σm​c)+βt​γC​(Σv​c2+Σv​v​Σc​c)),\displaystyle=-\alpha\_{c}\Sigma\_{vc}-\frac{1}{\sigma\_{z}^{2}}\big(\beta\_{t}^{2}\Sigma\_{vv}\Sigma\_{vc}+\beta\_{t}\gamma\_{F}(\Sigma\_{vm}\Sigma\_{vc}+\Sigma\_{vv}\Sigma\_{mc})+\beta\_{t}\gamma\_{C}(\Sigma\_{vc}^{2}+\Sigma\_{vv}\Sigma\_{cc})\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ˙m​m\displaystyle\dot{\Sigma}\_{mm} | =−2​αm​Σm​m+σm2−1σz2​(γF2​Σm​m2+2​γF​γC​Σm​m​Σm​c+βt​γF​(2​Σv​m​Σm​m)),\displaystyle=-2\alpha\_{m}\Sigma\_{mm}+\sigma\_{m}^{2}-\frac{1}{\sigma\_{z}^{2}}\big(\gamma\_{F}^{2}\Sigma\_{mm}^{2}+2\gamma\_{F}\gamma\_{C}\Sigma\_{mm}\Sigma\_{mc}+\beta\_{t}\gamma\_{F}(2\Sigma\_{vm}\Sigma\_{mm})\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ˙c​c\displaystyle\dot{\Sigma}\_{cc} | =−2​αc​Σc​c+σc2−1σz2​(γC2​Σc​c2+2​γF​γC​Σc​c​Σm​c+βt​γC​(2​Σv​c​Σc​c)),\displaystyle=-2\alpha\_{c}\Sigma\_{cc}+\sigma\_{c}^{2}-\frac{1}{\sigma\_{z}^{2}}\big(\gamma\_{C}^{2}\Sigma\_{cc}^{2}+2\gamma\_{F}\gamma\_{C}\Sigma\_{cc}\Sigma\_{mc}+\beta\_{t}\gamma\_{C}(2\Sigma\_{vc}\Sigma\_{cc})\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ˙m​c\displaystyle\dot{\Sigma}\_{mc} | =−(αm+αc)Σm​c−1σz2(γF2Σm​mΣm​c+γC2Σc​cΣm​c+γFγC(Σm​c2+Σm​mΣc​c)\displaystyle=-(\alpha\_{m}+\alpha\_{c})\Sigma\_{mc}-\frac{1}{\sigma\_{z}^{2}}\big(\gamma\_{F}^{2}\Sigma\_{mm}\Sigma\_{mc}+\gamma\_{C}^{2}\Sigma\_{cc}\Sigma\_{mc}+\gamma\_{F}\gamma\_{C}(\Sigma\_{mc}^{2}+\Sigma\_{mm}\Sigma\_{cc}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +βt(γFΣv​mΣm​c+γCΣv​cΣm​c)).\displaystyle\qquad+\beta\_{t}(\gamma\_{F}\Sigma\_{vm}\Sigma\_{mc}+\gamma\_{C}\Sigma\_{vc}\Sigma\_{mc})\big). |  |

This system governs the evolution of the six independent entries of Σt\Sigma\_{t}. For any deterministic βt∈Lloc2​([0,T))\beta\_{t}\in L^{2}\_{\text{loc}}([0,T)), the right-hand side is locally Lipschitz, so the system admits a unique solution on [0,T][0,T].

###### Proposition 4.3 (Well-posedness of the covariance Riccati system).

Fix T<∞T<\infty and let β:[0,T]→ℝ\beta:[0,T]\to\mathbb{R} be a deterministic, bounded function. Consider the componentwise Riccati system for the six entries of Σt\Sigma\_{t} given above, with initial condition Σ0⪰0\Sigma\_{0}\succeq 0. Then,

1. (1)

   There exists a unique solution Σt\Sigma\_{t} on [0,T][0,T].
2. (2)

   Σt\Sigma\_{t} remains symmetric and positive semidefinite for all t∈[0,T]t\in[0,T].

###### Proof.

Step 1: Local existence and uniqueness.
The Riccati system can be written as an ODE on ℝ6\mathbb{R}^{6}

|  |  |  |
| --- | --- | --- |
|  | S˙​(t)=F​(S​(t),t),S​(0)=S0,\dot{S}(t)=F(S(t),t)\ ,\qquad S(0)=S\_{0}\ , |  |

where S​(t)=(Σv​v,Σv​m,Σv​c,Σm​m,Σm​c,Σc​c)⊤S(t)=(\Sigma\_{vv},\Sigma\_{vm},\Sigma\_{vc},\Sigma\_{mm},\Sigma\_{mc},\Sigma\_{cc})^{\top} and FF is the right-hand side defined by the componentwise equations. For fixed βt\beta\_{t}, FF is a polynomial in the entries of SS with coefficients depending continuously on tt. Therefore, FF is locally Lipschitz in SS. By the Picard-Lindelöf theorem, there exists a unique local solution on some interval [0,τ)[0,\tau).

Step 2: Global existence on [0,T][0,T].
To extend the solution globally, we show that no finite-time blow-up occurs. Observe that each equation has the form

|  |  |  |
| --- | --- | --- |
|  | Σ˙i​j=(linear terms in Σ)+(quadratic terms in Σ)+constant noise term (for diagonals).\dot{\Sigma}\_{ij}=\text{(linear terms in $\Sigma$)}+\text{(quadratic terms in $\Sigma$)}+\text{constant noise term (for diagonals)}. |  |

The quadratic terms are negative definite because they appear with a factor −1σz2-\frac{1}{\sigma\_{z}^{2}} and involve squares of Σ\Sigma entries. For example,

|  |  |  |
| --- | --- | --- |
|  | Σ˙v​v=−1σz2​(βt2​Σv​v2+⋯)≤0.\dot{\Sigma}\_{vv}=-\frac{1}{\sigma\_{z}^{2}}(\beta\_{t}^{2}\Sigma\_{vv}^{2}+\cdots)\leq 0\ . |  |

Thus, the diagonal entries Σv​v,Σm​m,Σc​c\Sigma\_{vv},\Sigma\_{mm},\Sigma\_{cc} are non-increasing up to additive positive constants from QQ. By Grönwall’s inequality, all entries remain bounded on [0,T][0,T]. Therefore, the solution extends uniquely to [0,T][0,T].

Step 3: Symmetry and positive semidefiniteness.
The Riccati flow preserves symmetry because the right-hand side is derived from the matrix equation

|  |  |  |
| --- | --- | --- |
|  | Σ˙=A​Σ+Σ​A⊤+Q−Σ​C⊤​R−1​C​Σ,\dot{\Sigma}=A\Sigma+\Sigma A^{\top}+Q-\Sigma C^{\top}R^{-1}C\Sigma\ , |  |

which is symmetric whenever Σ\Sigma is symmetric. Positive semidefiniteness is preserved because the Riccati equation for covariance matrices is monotone and Q⪰0Q\succeq 0, R>0R>0. Therefore, Σt⪰0\Sigma\_{t}\succeq 0 for all tt.

Combining steps 1-3, the solution exists uniquely on [0,T][0,T] and remains symmetric positive semi-definite.
∎

###### Remark 4.4 (Well-posedness and Economic Interpretation).

The well-posedness result ensures that the covariance matrix Σt\Sigma\_{t} remains bounded and positive semi-definite for all t∈[0,T]t\in[0,T]. Mathematically, this means the Riccati flow does not blow up and preserves symmetry and non-negativity of variances and covariances. These properties are essential for the Kalman–Bucy filter to operate correctly, since the market maker’s price update depends on Σt\Sigma\_{t} through the Kalman gain.

Economically, boundedness of Σt\Sigma\_{t} guarantees that the market maker can consistently update beliefs about the asset value and the positions of momentum and contrarian traders without the filtering process becoming unstable. If Σt\Sigma\_{t} were to diverge or lose positive semi-definiteness, prices would cease to reflect information rationally, and the informed trader’s optimization problem would become ill-posed because the variance term Σv​v​(t)\Sigma\_{vv}(t) would be undefined.

Thus, well-posedness ensures that feedback effects from misinformed traders remain contained, preserving market efficiency and enabling equilibrium analysis.

Let’s take a closer look at the ODE for (1,1)-component Σv​v\Sigma\_{vv}

|  |  |  |
| --- | --- | --- |
|  | Σ˙v​v=−1σz2​(βt2​Σv​v2+2​βt​γF​Σv​v​Σv​m+2​βt​γC​Σv​v​Σv​c).\dot{\Sigma}\_{vv}=-\frac{1}{\sigma\_{z}^{2}}\big(\beta\_{t}^{2}\Sigma\_{vv}^{2}+2\beta\_{t}\gamma\_{F}\Sigma\_{vv}\Sigma\_{vm}+2\beta\_{t}\gamma\_{C}\Sigma\_{vv}\Sigma\_{vc}\big)\ . |  |

It shows that the rate at which Σv​v​(t)=Var​(v−Pt∣ℱtY)\Sigma\_{vv}(t)=\text{Var}(v-P\_{t}\mid\mathcal{F}\_{t}^{Y}) falls. That is, the speed of price discovery depends not only on the insider’s trading intensity βt\beta\_{t} but also on the feedback parameters γF\gamma\_{F} and γC\gamma\_{C}. Positive feedback (γF>0\gamma\_{F}>0) strengthens the linkage between price innovations and future order flow, increasing the information extracted from trades and accelerating the decline of Σv​v​(t)\Sigma\_{vv}(t). This modifies both the strength and timing of price discovery relative to the classical Kyle model.

## 5. Weak Feedback

### 5.1. Local existence and uniqueness of equilibrium

We now establish that for sufficiently small feedback parameters, a unique equilibrium exists.

###### Theorem 5.1.

Let h:=(κm,κc,γF,γC,σε)h:=(\kappa\_{m},\kappa\_{c},\gamma\_{F},\gamma\_{C},\sigma\_{\varepsilon}) be the feedback parameter vector.
Denote β(0)\beta^{(0)} as the classical Kyle’s equilibrium intensity corresponding to h=0h=0. Then, there exists ε>0\varepsilon>0 such that for all hh with ‖h‖<ε||h||<\varepsilon,

1. (1)

   there exists a unique equilibrium trading intensity β∗​(h)\beta^{\*}(h) on [0,T)[0,T), which depends smoothly on hh and satisfies β∗​(h)→β(0)\beta^{\*}(h)\rightarrow\beta^{(0)} as h→0h\rightarrow 0.
2. (2)

   there exists a unique equilibrium pair (θ∗,P∗)(\theta^{\*},P^{\*}) satisfying Definition [3.3](https://arxiv.org/html/2601.09872v1#S3.Thmthm3 "Definition 3.3. ‣ 3. Model ‣ A continuous-time Kyle model with price-responsive traders") with θt∗=βt∗​(h)​(v−Pt∗)\theta^{\*}\_{t}=\beta\_{t}^{\*}(h)(v-P\_{t}^{\*}) and P∗P^{\*} given by the Kalman-Bucy filter.

###### Proof.

Recall that the informed trader’s expected profit is

|  |  |  |
| --- | --- | --- |
|  | J​(β)=∫0Tβt​Σv​v​(t)​𝑑t,J(\beta)=\int\_{0}^{T}\beta\_{t}\,\Sigma\_{vv}(t)\,dt\ , |  |

and she chooses β\beta to maximize J​(β)J(\beta) subject to the Riccati dynamics. Define the best-response mapping G​(β;h)G(\beta;h) as follows:

1. (1)

   Given β\beta, solve the Riccati ODE for Σt\Sigma\_{t}.
2. (2)

   Compute the adjoint system from Pontryagin’s Maximum Principle.
3. (3)

   Apply the first-order condition ∂H/∂βt=0\partial H/\partial\beta\_{t}=0 to obtain β~=G​(β;h)\widetilde{\beta}=G(\beta;h).

Define the operator F:ℬ×ℝ5→ℬF:\mathcal{B}\times\mathbb{R}^{5}\to\mathcal{B} on a Banach space ℬ\mathcal{B} of deterministic intensity functions by

|  |  |  |
| --- | --- | --- |
|  | F​(β;h):=β−G​(β;h).F(\beta;h):=\beta-G(\beta;h)\ . |  |

An equilibrium corresponds to a fixed point β∗\beta^{\*} of GG, i.e.,

|  |  |  |
| --- | --- | --- |
|  | F​(β;h):=β−G​(β;h)=0.F(\beta;h):=\beta-G(\beta;h)=0\ . |  |

At h=0h=0, the model reduces to the classical Kyle setting with unique solution β(0)\beta^{(0)}. The mapping FF is Fréchet-differentiable near (β(0),0)(\beta^{(0)},0), and its derivative with respect to β\beta at (β(0),0)(\beta^{(0)},0) is

|  |  |  |
| --- | --- | --- |
|  | Dβ​F​(β(0);0)=I−Dβ​G​(β(0);0),D\_{\beta}F(\beta^{(0)};0)=I-D\_{\beta}G(\beta^{(0)};0)\ , |  |

where Dβ​FD\_{\beta}F is the Fréchet derivative of FF with respect to β\beta.
Invertibility of Dβ​FD\_{\beta}F follows from the uniqueness of the Kyle equilibrium and the fact that the linearized two-point boundary value problem has only the trivial solution. By the Implicit Function Theorem in Banach spaces, there exists ε>0\varepsilon>0 such that for ‖h‖<ε\|h\|<\varepsilon, a unique root β∗​(h)\beta^{\*}(h) exists and depends smoothly on hh.

Set θt∗=βt∗​(v−Pt∗)\theta\_{t}^{\*}=\beta\_{t}^{\*}(v-P\_{t}^{\*}), where P∗P^{\*} is the price process generated by the Kalman filter using β∗\beta^{\*}. By construction,

* •

  θ∗\theta^{\*} maximizes expected terminal wealth given P∗P^{\*},
* •

  P∗P^{\*} satisfies Pt∗=𝔼​[v∣ℱtY]P\_{t}^{\*}=\mathbb{E}[v\mid\mathcal{F}^{Y}\_{t}].

Thus, (θ∗,P∗)(\theta^{\*},P^{\*}) satisfies Definition [3.3](https://arxiv.org/html/2601.09872v1#S3.Thmthm3 "Definition 3.3. ‣ 3. Model ‣ A continuous-time Kyle model with price-responsive traders").

Smooth dependence in the Banach space ℬ=Lloc2​([0,T])\mathcal{B}=L^{2}\_{\text{loc}}([0,T]) implies

|  |  |  |
| --- | --- | --- |
|  | β∗​(h)⟶β(0)in ​Lloc2​([0,T]) as ​h→0,\beta^{\*}(h)\longrightarrow\beta^{(0)}\quad\text{in }L^{2}\_{\text{loc}}([0,T])\quad\text{ as }h\to 0\ , |  |

completing the proof.
∎

Throughout the paper, the distinction between weak and strong feedback refers to the magnitude of the feedback parameter vector
h=(κm,κc,γF,γC,σε).h=(\kappa\_{m},\kappa\_{c},\gamma\_{F},\gamma\_{C},\sigma\_{\varepsilon}).
Weak feedback corresponds to parameter values for which endogenous price-responsive order flow remains small relative to exogenous noise, so that the Kyle equilibrium is only mildly perturbed.
Strong feedback arises when price responsiveness or exposure is sufficiently large that endogenous order flow dominates noise, generating amplification effects and potentially destabilizing price discovery.

Theorem [5.1](https://arxiv.org/html/2601.09872v1#S5.Thmthm1 "Theorem 5.1. ‣ 5.1. Local existence and uniqueness of equilibrium ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders") provides an economically transparent characterization of how price-responsive trading interacts with informed trading. When feedback effects from momentum and contrarian traders are sufficiently weak, the equilibrium of the classical Kyle model is preserved in a robust sense: prices continue to aggregate information gradually, the market maker’s inference remains well-behaved, and the informed trader’s optimal strategy adjusts smoothly rather than discontinuously.

The key mechanism is that weak feedback does not overwhelm the informational role of exogenous liquidity trading. Although price-responsive traders introduce endogenous drift into aggregate order flow, their influence remains second-order relative to the noise component. As a result, the market maker can still disentangle informed trading from noise using a finite-dimensional Kalman–Bucy filter, and the informed trader optimally trades on the unexpected component of fundamentals relative to public beliefs, as in the classical Kyle logic.

From the informed trader’s perspective, Theorem [5.1](https://arxiv.org/html/2601.09872v1#S5.Thmthm1 "Theorem 5.1. ‣ 5.1. Local existence and uniqueness of equilibrium ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders") implies that behavioral trading affects profitability in a continuous manner. Small increases in feedback intensity alter the speed of information revelation and price impact, but do not qualitatively change the informed trader’s trading incentives. In particular, insider advantage varies smoothly with the strength of momentum or contrarian trading, allowing for meaningful comparative statics on equilibrium trading intensity, price informativeness, and expected insider profits.

This result stands in sharp contrast to regimes with strong feedback, where endogenous price responsiveness can dominate mean reversion and noise, potentially destabilizing the filtering process.
In such regimes, price changes feed back aggressively into order flow, amplifying fluctuations and undermining the market maker’s ability to infer fundamentals. The model then admits the possibility of equilibrium multiplicity, instability, or explosive dynamics, as reflected in the stability conditions derived below. Theorem [5.1](https://arxiv.org/html/2601.09872v1#S5.Thmthm1 "Theorem 5.1. ‣ 5.1. Local existence and uniqueness of equilibrium ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders") therefore delineates a boundary between a Kyle-like regime with stable price discovery and a feedback-dominated regime in which classical microstructure intuition breaks down.

### 5.2. Sufficient stability condition

The following provides a sufficient local condition for stability of the linearized equilibrium price dynamics.

###### Theorem 5.2 (Sufficient Stability Condition).

Let xt=(v,mt,ct)⊤x\_{t}=(v,m\_{t},c\_{t})^{\top} be the state vector, where vv is constant and (mt,ct)(m\_{t},c\_{t}) satisfy ([3.2](https://arxiv.org/html/2601.09872v1#S3.E2 "In 3. Model ‣ A continuous-time Kyle model with price-responsive traders"))-([3.3](https://arxiv.org/html/2601.09872v1#S3.E3 "In 3. Model ‣ A continuous-time Kyle model with price-responsive traders")).
Assume the price admits the linear representation

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | Pt=Pt(v)+Gm​mt+Gc​ct+Mt,P\_{t}=P^{(v)}\_{t}+G\_{m}m\_{t}+G\_{c}c\_{t}+M\_{t}\ , |  |

where Gm,Gc∈ℝG\_{m},G\_{c}\in\mathbb{R} are deterministic coefficients and MtM\_{t} is an ℱY\mathcal{F}^{Y}-martingale. Then, the deterministic part of (mt,ct)(m\_{t},c\_{t}) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (5.2) |  | dd​t​(mtct)=Aeff​(mtct),Aeff:=(−αm+κm​Gmκm​Gc−κc​Gm−αc−κc​Gc).\frac{d}{dt}\begin{pmatrix}m\_{t}\\ c\_{t}\end{pmatrix}=A\_{\text{eff}}\begin{pmatrix}m\_{t}\\ c\_{t}\end{pmatrix},\qquad A\_{\text{eff}}:=\begin{pmatrix}-\alpha\_{m}+\kappa\_{m}G\_{m}&\kappa\_{m}G\_{c}\\ -\kappa\_{c}G\_{m}&-\alpha\_{c}-\kappa\_{c}G\_{c}\end{pmatrix}. |  |

Define the feedback matrix

|  |  |  |
| --- | --- | --- |
|  | F:=(κm​Gmκm​Gc−κc​Gm−κc​Gc).F:=\begin{pmatrix}\kappa\_{m}G\_{m}&\kappa\_{m}G\_{c}\\ -\kappa\_{c}G\_{m}&-\kappa\_{c}G\_{c}\end{pmatrix}. |  |

If

|  |  |  |  |
| --- | --- | --- | --- |
| (5.3) |  | ρ​(F)<min⁡{αm,αc},\rho(F)<\min\{\alpha\_{m},\alpha\_{c}\}, |  |

where ρ​(F)\rho(F) is the spectral radius of FF, then the closed-loop system is exponentially stable in mean square, and in particular

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼​[mt2+ct2]<∞.\sup\_{t\in[0,T]}\mathbb{E}[m\_{t}^{2}+c\_{t}^{2}]<\infty. |  |

###### Proof.

From ([3.2](https://arxiv.org/html/2601.09872v1#S3.E2 "In 3. Model ‣ A continuous-time Kyle model with price-responsive traders"))-([3.3](https://arxiv.org/html/2601.09872v1#S3.E3 "In 3. Model ‣ A continuous-time Kyle model with price-responsive traders")) and ([5.1](https://arxiv.org/html/2601.09872v1#S5.E1 "In Theorem 5.2 (Sufficient Stability Condition). ‣ 5.2. Sufficient stability condition ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders")), ignoring martingale and noise terms, the deterministic dynamics are

|  |  |  |
| --- | --- | --- |
|  | x˙​(t)=Aeff​x​(t),x​(t):=(mt,ct)⊤.\dot{x}(t)=A\_{\text{eff}}x(t),\qquad x(t):=(m\_{t},c\_{t})^{\top}\ . |  |

Write Aeff=−D+FA\_{\text{eff}}=-D+F with D:=diag​(αm,αc)D:=\text{diag}(\alpha\_{m},\alpha\_{c}) and FF as above. The solution is

|  |  |  |
| --- | --- | --- |
|  | x​(t)=eAeff​t​x​(0).x(t)=e^{A\_{\text{eff}}t}x(0)\ . |  |

Stability requires that all eigenvalues of AeffA\_{\text{eff}} have negative real part. Since Aeff=−D+FA\_{\text{eff}}=-D+F, Gershgorin’s theorem and standard perturbation bounds imply that if ‖F‖<min⁡{αm,αc}\|F\|<\min\{\alpha\_{m},\alpha\_{c}\} in any induced norm, then AeffA\_{\text{eff}} is Hurwitz. In particular, if ρ​(F)<min⁡{αm,αc}\rho(F)<\min\{\alpha\_{m},\alpha\_{c}\}, then all eigenvalues satisfy

|  |  |  |
| --- | --- | --- |
|  | ℜ⁡(λ​(Aeff))≤−min⁡{αm,αc}+ρ​(F)<0,\Re(\lambda(A\_{\text{eff}}))\leq-\min\{\alpha\_{m},\alpha\_{c}\}+\rho(F)<0\ , |  |

where ℜ⁡(λ)\Re(\lambda) denotes the real part of the eigenvalue λ\lambda.
Thus, the deterministic system is exponentially stable. For the full SDE, write the variation-of-constants formula

|  |  |  |
| --- | --- | --- |
|  | x​(t)=eAeff​t​x​(0)+∫0teAeff​(t−s)​D​𝑑Bs,x(t)=e^{A\_{\text{eff}}t}x(0)+\int\_{0}^{t}e^{A\_{\text{eff}}(t-s)}D\,dB\_{s}\ , |  |

where D=diag​(σm,σc)D=\text{diag}(\sigma\_{m},\sigma\_{c}). Exponential stability of eAeff​te^{A\_{\text{eff}}t} implies that the stochastic convolution has finite second moment on [0,T][0,T]. Therefore

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼​[‖x​(t)‖2]<∞.\sup\_{t\in[0,T]}\mathbb{E}[\|x(t)\|^{2}]<\infty\ . |  |

∎

###### Corollary 5.3 (Induced Norm Condition).

For the feedback matrix

|  |  |  |
| --- | --- | --- |
|  | F=(κm​Gmκm​Gc−κc​Gm−κc​Gc),F=\begin{pmatrix}\kappa\_{m}G\_{m}&\kappa\_{m}G\_{c}\\ -\kappa\_{c}G\_{m}&-\kappa\_{c}G\_{c}\end{pmatrix}, |  |

the induced norms are

|  |  |  |
| --- | --- | --- |
|  | ‖F‖∞=max⁡{κm​(|Gm|+|Gc|),κc​(|Gm|+|Gc|)},\|F\|\_{\infty}=\max\big\{\kappa\_{m}(|G\_{m}|+|G\_{c}|),\kappa\_{c}(|G\_{m}|+|G\_{c}|)\big\}\ , |  |

|  |  |  |
| --- | --- | --- |
|  | ‖F‖1=max⁡{|Gm|​(κm+κc),|Gc|​(κm+κc)}.\|F\|\_{1}=\max\big\{|G\_{m}|(\kappa\_{m}+\kappa\_{c}),|G\_{c}|(\kappa\_{m}+\kappa\_{c})\big\}\ . |  |

Since ρ​(F)≤‖F‖p\rho(F)\leq\|F\|\_{p} for any induced norm, a sufficient condition for stability is

|  |  |  |  |
| --- | --- | --- | --- |
| (5.4) |  | ‖F‖∞<min⁡{αm,αc}or‖F‖1<min⁡{αm,αc}.\|F\|\_{\infty}<\min\{\alpha\_{m},\alpha\_{c}\}\quad\text{or}\quad\|F\|\_{1}<\min\{\alpha\_{m},\alpha\_{c}\}. |  |

###### Remark 5.4.

The stability condition derived in this section is local and sufficient. It is obtained from a linearized representation of the equilibrium price dynamics around the steady-state filtering solution and relies on equilibrium coefficients such as GmG\_{m} and GcG\_{c}, which are themselves functions of underlying primitives through the equilibrium mapping. As such, the condition should not be interpreted as a global characterization of equilibrium existence or stability.

Failure of the condition does not imply that equilibrium ceases to exist, nor that price dynamics necessarily become explosive. Rather, the condition provides a conservative criterion under which endogenous price-responsive trading is guaranteed not to destabilize price discovery.

###### Remark 5.5.

Condition ([5.3](https://arxiv.org/html/2601.09872v1#S5.E3 "In Theorem 5.2 (Sufficient Stability Condition). ‣ 5.2. Sufficient stability condition ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders")) or ([5.4](https://arxiv.org/html/2601.09872v1#S5.E4 "In Corollary 5.3 (Induced Norm Condition). ‣ 5.2. Sufficient stability condition ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders")) ensures that mean reversion dominates feedback amplification. Economically:

* •

  Small κm,κc\kappa\_{m},\kappa\_{c} (weak trend/contrarian sensitivity),
* •

  Large αm,αc\alpha\_{m},\alpha\_{c} (fast mean reversion),
* •

  Small Gm,GcG\_{m},G\_{c} (weak price impact of agent positions)

promote stability.
Violations of the condition typically correspond to economically extreme scenarios, such as unusually strong momentum trading or large exposures that cause endogenous order flow to react more strongly to price changes than prices respond to fundamentals.

In such regimes, price movements may become self-reinforcing, amplifying rather than dissipating shocks. While the present framework does not characterize equilibrium behavior beyond this boundary, the condition highlights a natural economic trade-off between feedback intensity and informational stability.

###### Remark 5.6 (Computation of Gm,GcG\_{m},G\_{c}).

The coefficients Gm,GcG\_{m},G\_{c} arise from the Kalman-Bucy filter in Section [4.1](https://arxiv.org/html/2601.09872v1#S4.SS1 "4.1. State-space representation and price filtering ‣ 4. Equilibrium Analysis ‣ A continuous-time Kyle model with price-responsive traders"). Writing the observation equation

|  |  |  |
| --- | --- | --- |
|  | d​Yt=βt​(v−Pt)​d​t+γF​mt+γC​ct​d​t+σε​εt​d​t+σz​d​Wt,dY\_{t}=\beta\_{t}(v-P\_{t})dt+\gamma\_{F}m\_{t}+\gamma\_{C}c\_{t}\,dt+\sigma\_{\varepsilon}\varepsilon\_{t}dt+\sigma\_{z}\,dW\_{t}\ , |  |

the filter computes x^t=E​[xt∣ℱtY]\hat{x}\_{t}=E[x\_{t}\mid\mathcal{F}^{Y}\_{t}] and updates via

|  |  |  |
| --- | --- | --- |
|  | d​x^t=A​x^t​d​t+Kt​(d​Yt−Ct​x^t​d​t),d\hat{x}\_{t}=A\hat{x}\_{t}\,dt+K\_{t}\big(dY\_{t}-C\_{t}\hat{x}\_{t}\,dt\big)\ , |  |

where Ct=(βt,γF,γC)C\_{t}=(\beta\_{t},\gamma\_{F},\gamma\_{C}) and Kt=Σt​Ct⊤​R−1K\_{t}=\Sigma\_{t}C\_{t}^{\top}R^{-1}. The price is Pt=e1⊤​x^tP\_{t}=e\_{1}^{\top}\hat{x}\_{t} with e1=(1,0,0)⊤e\_{1}=(1,0,0)^{\top}. Linearizing the mapping from (mt,ct)(m\_{t},c\_{t}) to PtP\_{t} yields

|  |  |  |
| --- | --- | --- |
|  | Gm=∂Pt∂mt,Gc=∂Pt∂ct,G\_{m}=\frac{\partial P\_{t}}{\partial m\_{t}}\ ,\qquad G\_{c}=\frac{\partial P\_{t}}{\partial c\_{t}}\ , |  |

which can be computed from the Kalman gain and Riccati solution Σt\Sigma\_{t} numerically or analytically in special cases.

### 5.3. First-order comparative statics for small feedback

We study how equilibrium outcomes respond to small amounts of price-responsive trading by exploiting the local structure of equilibrium characterized in Theorem [5.1](https://arxiv.org/html/2601.09872v1#S5.Thmthm1 "Theorem 5.1. ‣ 5.1. Local existence and uniqueness of equilibrium ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders"). Because the equilibrium mapping is smooth in the feedback parameters, equilibrium objects admit well-defined first-order expansions around the classical Kyle benchmark.

We focus on perturbations in γF\gamma\_{F}, which scales the aggregate exposure of momentum traders and provides a natural one-dimensional measure of feedback intensity. The same argument applies to other feedback parameters, such as γC\gamma\_{C}, κm\kappa\_{m}, or κc\kappa\_{c}, and we view the analysis below as representative rather than exhaustive.

Effect on price informativeness.
Introducing a small amount of momentum exposure strengthens the statistical link between order flow and the fundamental, increasing the signal content of observed trades and accelerating the market maker’s Bayesian learning. As a result, price informativeness measured by the posterior variance of the fundamental Σv​v​(t)\Sigma\_{vv}(t) improves. That being said, ∂Σv​v​(t)∂γF<0\frac{\partial\Sigma\_{vv}(t)}{\partial\gamma\_{F}}<0 for all t>0t>0 (see Appendix [A](https://arxiv.org/html/2601.09872v1#A1 "Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders")).

Effect on insider trading intensity.
The reduction in informational rents translates into lower expected insider profits at first order. While momentum traders increase trading volume and short-run price responsiveness, their presence erodes the insider’s ability to exploit private information over time.

Mathematically, we write

|  |  |  |
| --- | --- | --- |
|  | ∂βt∂γF=∂βt∂Σv​v​(t)⋅∂Σv​v​(t)∂γF<0\frac{\partial\beta\_{t}}{\partial\gamma\_{F}}=\frac{\partial\beta\_{t}}{\partial\Sigma\_{vv}(t)}\cdot\frac{\partial\Sigma\_{vv}(t)}{\partial\gamma\_{F}}<0 |  |

since ∂Σv​v​(t)∂γF<0\frac{\partial\Sigma\_{vv}(t)}{\partial\gamma\_{F}}<0 from Appendix [A](https://arxiv.org/html/2601.09872v1#A1 "Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders"), and ∂βt∂Σv​v​(t)>0\frac{\partial\beta\_{t}}{\partial\Sigma\_{vv}(t)}>0 as lower Σv​v​(t)\Sigma\_{vv}(t) means prices reveal more information about vv.
This effect is continuous and proportional to γF\gamma\_{F} for small feedback, reflecting the reduced marginal value of private information when prices incorporate information more rapidly.

Effect on insider profits.
Faster information revelation induced by momentum trading reduces the insider’s informational rents and translates into lower expected profits at first order. In equilibrium, expected insider profits can be expressed as

|  |  |  |
| --- | --- | --- |
|  | J=∫0Tβt​Σv​v​(t)​𝑑t,J=\int\_{0}^{T}\beta\_{t}\,\Sigma\_{vv}(t)\,dt\ , |  |

so that a marginal increase in γF\gamma\_{F} yields

|  |  |  |
| --- | --- | --- |
|  | ∂J∂γF|h=0=∫0T(∂βt∗∂γF|h=0​Σv​v(0)​(t)+βt(0)​∂Σv​v​(t)∂γF|h=0)​𝑑t.\frac{\partial J}{\partial\gamma\_{F}}\Big|\_{h=0}=\int\_{0}^{T}\left(\frac{\partial\beta\_{t}^{\*}}{\partial\gamma\_{F}}\Big|\_{h=0}\,\Sigma\_{vv}^{(0)}(t)+\beta\_{t}^{(0)}\,\frac{\partial\Sigma\_{vv}(t)}{\partial\gamma\_{F}}\Big|\_{h=0}\right)dt\ . |  |

The second term is negative because momentum exposure accelerates Bayesian learning, reducing the posterior variance Σv​v​(t)\Sigma\_{vv}(t). Moreover, since the insider’s trading intensity βt\beta\_{t} is decreasing in the remaining informational advantage, the first term is also negative. As a result, small momentum exposure lowers expected insider profits by eroding informational rents along both margins.

## 6. Strong Feedback and Breakdown of Equilibrium

The analysis in Section [5](https://arxiv.org/html/2601.09872v1#S5 "5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders") establishes that for sufficiently small feedback
parameters h=(κm,κc,γF,γC,σε)h=(\kappa\_{m},\kappa\_{c},\gamma\_{F},\gamma\_{C},\sigma\_{\varepsilon}),
the Kyle equilibrium is well defined, unique, and smoothly perturbes
from the classical benchmark.
In this section, we show that when feedback becomes sufficiently large,
the structure sustaining equilibrium can break down in three distinct ways:
(i) loss of global existence of the Riccati equation,
(ii) failure of the equilibrium fixed-point mapping to remain a contraction,
and (iii) local instability of the filtering dynamics.
These results provide structural justification for the amplification and
potential multiplicity of equilibria discussed in the introduction.

Throughout this section, we let h→∞h\to\infty denote a regime in which the
feedback sensitivities (γF,γC)(\gamma\_{F},\gamma\_{C}) or (κm,κc)(\kappa\_{m},\kappa\_{c})
become large relative to the stabilizing mean-reversion parameters
(αm,αc)(\alpha\_{m},\alpha\_{c}).
Our objective is not to characterize global equilibrium under strong feedback
but to show that the mathematical structure supporting equilibrium fails
beyond a well-defined threshold.

### 6.1. Loss of global existence of the Riccati equation

Recall that the conditional covariance matrix Σt\Sigma\_{t} satisfies the
Riccati equation

|  |  |  |  |
| --- | --- | --- | --- |
| (6.1) |  | Σ˙t=A​Σt+Σt​A⊤+Q−Σt​Ct⊤​R−1​Ct​Σt,Ct=(βt,γF,γC).\dot{\Sigma}\_{t}=A\Sigma\_{t}+\Sigma\_{t}A^{\top}+Q-\Sigma\_{t}C\_{t}^{\top}R^{-1}C\_{t}\Sigma\_{t}\ ,\qquad C\_{t}=(\beta\_{t},\gamma\_{F},\gamma\_{C}). |  |

For simplicity, define

|  |  |  |
| --- | --- | --- |
|  | H:=γF2+γC2.H:=\gamma\_{F}^{2}+\gamma\_{C}^{2}. |  |

Large feedback corresponds to H≫1H\gg 1.
The following shows that when HH exceeds a computable bound,
the Riccati equation cannot be solved globally on [0,T][0,T].

###### Lemma 6.1 (Finite-time breakdown of the Riccati flow).

There exists H∗>0H^{\ast}>0 depending on (A,Q,R,T)(A,Q,R,T) such that if
γF2+γC2>H∗\gamma\_{F}^{2}+\gamma\_{C}^{2}>H^{\ast}, then the Riccati equation
([6.1](https://arxiv.org/html/2601.09872v1#S6.E1 "In 6.1. Loss of global existence of the Riccati equation ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders")) admits no global solution on [0,T][0,T].
In particular, either
(a) Σt\Sigma\_{t} loses positive semidefiniteness, or
(b) at least one entry of Σt\Sigma\_{t} diverges to +∞+\infty
in finite time.

###### Proof.

The negative quadratic term in ([6.1](https://arxiv.org/html/2601.09872v1#S6.E1 "In 6.1. Loss of global existence of the Riccati equation ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders")) satisfies

|  |  |  |
| --- | --- | --- |
|  | Σt​Ct⊤​R−1​Ct​Σt⪰Hσz2​(0000Σm​m​(t)2Σm​m​(t)​Σm​c​(t)0Σm​c​(t)​Σm​m​(t)Σc​c​(t)2).\Sigma\_{t}C\_{t}^{\top}R^{-1}C\_{t}\Sigma\_{t}\;\succeq\;\frac{H}{\sigma\_{z}^{2}}\begin{pmatrix}0&0&0\\ 0&\Sigma\_{mm}(t)^{2}&\Sigma\_{mm}(t)\Sigma\_{mc}(t)\\ 0&\Sigma\_{mc}(t)\Sigma\_{mm}(t)&\Sigma\_{cc}(t)^{2}\end{pmatrix}. |  |

Thus the (m,m)(m,m) component of ([6.1](https://arxiv.org/html/2601.09872v1#S6.E1 "In 6.1. Loss of global existence of the Riccati equation ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders")) satisfies

|  |  |  |
| --- | --- | --- |
|  | Σ˙m​m​(t)≤−2​αm​Σm​m​(t)+σm2−Hσz2​Σm​m​(t)2.\dot{\Sigma}\_{mm}(t)\;\leq\;-2\alpha\_{m}\Sigma\_{mm}(t)+\sigma\_{m}^{2}-\frac{H}{\sigma\_{z}^{2}}\Sigma\_{mm}(t)^{2}. |  |

The right-hand side becomes strictly negative for
Σm​m​(t)>σz2​H−1\Sigma\_{mm}(t)>\sigma\_{z}^{2}H^{-1}, so Σm​m\Sigma\_{mm} solves a
logistic-type ODE with finite-time blowup when HH is sufficiently large.
The remaining claims follow from standard comparison principles for
matrix Riccati equations.
∎

###### Remark 6.2.

Lemma [6.1](https://arxiv.org/html/2601.09872v1#S6.Thmthm1 "Lemma 6.1 (Finite-time breakdown of the Riccati flow). ‣ 6.1. Loss of global existence of the Riccati equation ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders") shows that strong feedback overwhelms the
stabilizing mean-reversion in (mt,ct)(m\_{t},c\_{t}) and forces the conditional
covariance matrix to exit the state space of symmetric positive
semidefinite matrices.
Since equilibrium pricing requires the Kalman-Bucy filter,
loss of the Riccati solution implies that no rational-expectations price
can be defined.

### 6.2. Loss of uniqueness of the equilibrium fixed point

From the insider’s optimization problem in Section [4.3](https://arxiv.org/html/2601.09872v1#S4.SS3 "4.3. Informed trader’s optimization problem ‣ 4. Equilibrium Analysis ‣ A continuous-time Kyle model with price-responsive traders"), the first-order condition for the linear trading strategy θt=βt​(v−Pt)\theta\_{t}=\beta\_{t}(v-P\_{t}) implies

|  |  |  |
| --- | --- | --- |
|  | βt=12​λt,\beta\_{t}=\frac{1}{2\lambda\_{t}}\ , |  |

where λt\lambda\_{t} is the price-impact coefficient in the pricing rule
d​Pt=λt​d​YtdP\_{t}=\lambda\_{t}dY\_{t}.

On the other hand, under rational pricing and Kalman-Bucy filtering, we have

|  |  |  |
| --- | --- | --- |
|  | λt​(β,h)=Σv​v​(t)​βt,\lambda\_{t}(\beta,h)=\Sigma\_{vv}(t)\beta\_{t}\ , |  |

where Σv​v\Sigma\_{vv} is the conditional variance of v−Ptv-P\_{t} and solves the Riccati equation,
whose coefficients depend on the feedback parameter hh and the intensity β\beta.

It is therefore natural to rewrite equilibrium as the fixed-point problem

|  |  |  |  |
| --- | --- | --- | --- |
| (6.2) |  | βt=ℱh​(β)t:=12​λt​(β,h),λt​(β,h):=Σv​v​(t)​βt.\beta\_{t}=\mathcal{F}\_{h}(\beta)\_{t}:=\frac{1}{2\lambda\_{t}(\beta,h)}\ ,\qquad\lambda\_{t}(\beta,h):=\Sigma\_{vv}(t)\beta\_{t}\ . |  |

The mapping β↦ℱh​(β)\beta\mapsto\mathcal{F}\_{h}(\beta) is a contraction for
small hh by Theorem [5.1](https://arxiv.org/html/2601.09872v1#S5.Thmthm1 "Theorem 5.1. ‣ 5.1. Local existence and uniqueness of equilibrium ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders").
We show that this contraction property fails when feedback is large.

###### Proposition 6.3 (Loss of contraction).

Let L​(h)L(h) denote the Lipschitz constant of the fixed-point mapping
β↦ℱh​(β)\beta\mapsto\mathcal{F}\_{h}(\beta) in the Banach space Lloc2​([0,T])L^{2}\_{\mathrm{loc}}([0,T]).
Then

|  |  |  |
| --- | --- | --- |
|  | limh→∞L​(h)=∞.\lim\_{h\to\infty}L(h)=\infty\ . |  |

In particular, there exists hmulti>0h^{\mathrm{multi}}>0 such that
for ‖h‖>hmulti\|h\|>h^{\mathrm{multi}},

|  |  |  |
| --- | --- | --- |
|  | L​(h)>1,L(h)>1\ , |  |

and the fixed-point mapping is not a contraction.
Consequently, equilibrium is not unique.

###### Proof.

Differentiating ([6.2](https://arxiv.org/html/2601.09872v1#S6.E2 "In 6.2. Loss of uniqueness of the equilibrium fixed point ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders")) yields

|  |  |  |
| --- | --- | --- |
|  | ∂ℱh∂βt=−12​λt​(β,h)2​∂λt​(β,h)∂βt.\frac{\partial\mathcal{F}\_{h}}{\partial\beta\_{t}}=-\frac{1}{2\lambda\_{t}(\beta,h)^{2}}\frac{\partial\lambda\_{t}(\beta,h)}{\partial\beta\_{t}}\ . |  |

Since λt​(β,h)=Σv​v​(t)​βt\lambda\_{t}(\beta,h)=\Sigma\_{vv}(t)\beta\_{t},

|  |  |  |
| --- | --- | --- |
|  | ∂λt∂βt=Σv​v​(t)+βt​∂Σv​v​(t)∂h⋅∂h∂βt.\frac{\partial\lambda\_{t}}{\partial\beta\_{t}}=\Sigma\_{vv}(t)+\beta\_{t}\frac{\partial\Sigma\_{vv}(t)}{\partial h}\cdot\frac{\partial h}{\partial\beta\_{t}}\ . |  |

Lemma [6.1](https://arxiv.org/html/2601.09872v1#S6.Thmthm1 "Lemma 6.1 (Finite-time breakdown of the Riccati flow). ‣ 6.1. Loss of global existence of the Riccati equation ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders") implies
|∂Σv​v/∂h|→∞|\partial\Sigma\_{vv}/\partial h|\to\infty as h→∞h\to\infty,
so the derivative above becomes arbitrarily large in magnitude.
Therefore L​(h)→∞L(h)\to\infty, proving the claim.
∎

###### Remark 6.4.

Proposition [6.3](https://arxiv.org/html/2601.09872v1#S6.Thmthm3 "Proposition 6.3 (Loss of contraction). ‣ 6.2. Loss of uniqueness of the equilibrium fixed point ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders") does not assert the
*existence* of multiple equilibria, but shows that
the contraction argument guaranteeing uniqueness breaks down.
This opens the door to equilibrium multiplicity, consistent with the
amplification phenomena discussed in Cespa and Vives (2012) [[13](https://arxiv.org/html/2601.09872v1#bib.bib4 "Dynamic trading and asset prices: keynes vs. Hayek")].

### 6.3. Instability of the filtering dynamics

Let et=xt−x^te\_{t}=x\_{t}-\hat{x}\_{t} be the estimation error. Linearizing the
Kalman-Bucy filter gives

|  |  |  |  |
| --- | --- | --- | --- |
| (6.3) |  | e˙t=Mt​(h)​et,Mt​(h):=A−Kt​(h)​Ct.\dot{e}\_{t}=M\_{t}(h)e\_{t},\qquad M\_{t}(h):=A-K\_{t}(h)C\_{t}. |  |

The stability of the filtering process is governed by the
time-varying matrix Mt​(h)M\_{t}(h), whose eigenvalues depend
on the feedback parameters hh through both CtC\_{t} and the Kalman gain
Kt​(h)=Σt​(h)​Ct⊤​R−1K\_{t}(h)=\Sigma\_{t}(h)C\_{t}^{\top}R^{-1}.

###### Proposition 6.5 (Filtering instability under strong feedback).

Assume that t↦Mt​(h)t\mapsto M\_{t}(h) is continuous on [0,T][0,T] and define

|  |  |  |
| --- | --- | --- |
|  | Λ​(h):=supt∈[0,T]λmax​(Mt​(h)),\Lambda(h):=\sup\_{t\in[0,T]}\lambda\_{\max}\!\left(M\_{t}(h)\right), |  |

where λmax​(⋅)\lambda\_{\max}(\cdot) denotes the largest real part of its eigenvalues.

If

|  |  |  |
| --- | --- | --- |
|  | Λ​(h)>0,\Lambda(h)>0, |  |

then the Kalman-Bucy filter is unstable. That is, there exists c>0c>0 such that for every nonzero
initial error e0e\_{0},

|  |  |  |
| --- | --- | --- |
|  | ‖et‖≥c​eΛ​(h)​t​‖e0‖,t∈[0,T].\|e\_{t}\|\;\geq\;c\,e^{\,\Lambda(h)t}\|e\_{0}\|\ ,\qquad t\in[0,T]. |  |

In particular, the filtering error grows exponentially and does not converge.

Moreover, if Λ​(h)→+∞\Lambda(h)\to+\infty as h→∞h\to\infty, then sufficiently strong feedback
violates well-posedness of the market maker’s inference problem: the covariance Σt\Sigma\_{t}
blows up in finite time, the Kalman gain KtK\_{t} diverges, and the pricing rule
d​Pt=λt​d​YtdP\_{t}=\lambda\_{t}dY\_{t} ceases to be well defined. Hence, no equilibrium exists for such hh.

###### Proof.

Let Φ​(t,s)\Phi(t,s) denote the principal matrix solution of Φ˙​(t,s)=Mt​(h)​Φ​(t,s)\dot{\Phi}(t,s)=M\_{t}(h)\Phi(t,s),
Φ​(s,s)=I\Phi(s,s)=I.
Classical results for linear ODEs imply

|  |  |  |
| --- | --- | --- |
|  | ‖Φ​(t,0)‖≥exp⁡(∫0tλmax​(Ms​(h))​𝑑s).\|\Phi(t,0)\|\;\geq\;\exp\!\left(\int\_{0}^{t}\lambda\_{\max}\!\left(M\_{s}(h)\right)ds\right)\ . |  |

By the definition of Λ​(h)\Lambda(h),

|  |  |  |
| --- | --- | --- |
|  | ∫0tλmax​(Ms​(h))​𝑑s≥t​Λ​(h).\int\_{0}^{t}\lambda\_{\max}\!\left(M\_{s}(h)\right)ds\;\geq\;t\,\Lambda(h)\ . |  |

Hence, for any nonzero e0e\_{0},

|  |  |  |
| --- | --- | --- |
|  | ‖et‖=‖Φ​(t,0)​e0‖≥eΛ​(h)​t​‖e0‖.\|e\_{t}\|=\|\Phi(t,0)e\_{0}\|\;\geq\;e^{\,\Lambda(h)t}\|e\_{0}\|\ . |  |

This proves instability when Λ​(h)>0\Lambda(h)>0.

If additionally Λ​(h)→∞\Lambda(h)\to\infty as h→∞h\to\infty, then the exponential divergence of ete\_{t}
forces the conditional covariance Σt\Sigma\_{t} to blow up (by the duality between error growth
and Riccati evolution in linear-Gaussian filtering).
Consequently, the Kalman gain Kt=Σt​Ct⊤​R−1K\_{t}=\Sigma\_{t}C\_{t}^{\top}R^{-1} diverges, implying that the price
impact λt=Kt​Ct\lambda\_{t}=K\_{t}C\_{t} becomes unbounded. In this case, the pricing rule cannot be
defined and no equilibrium exists.
∎

###### Remark 6.6.

The instability above is analogous to the blowup of extended
Kalman filters under strong feedback.
Economically, large price responsiveness can cause price changes to induce
order-flow responses strong enough to overwhelm the informational role of
noise, making the public belief-update process unstable.

Taken together, Lemma [6.1](https://arxiv.org/html/2601.09872v1#S6.Thmthm1 "Lemma 6.1 (Finite-time breakdown of the Riccati flow). ‣ 6.1. Loss of global existence of the Riccati equation ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders"),
Proposition [6.3](https://arxiv.org/html/2601.09872v1#S6.Thmthm3 "Proposition 6.3 (Loss of contraction). ‣ 6.2. Loss of uniqueness of the equilibrium fixed point ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders"), and
Proposition [6.5](https://arxiv.org/html/2601.09872v1#S6.Thmthm5 "Proposition 6.5 (Filtering instability under strong feedback). ‣ 6.3. Instability of the filtering dynamics ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders")
show that sufficiently strong price-responsive trading destroys the
analytical structure that sustains equilibrium.
While a full characterization of the strong-feedback regime is beyond the
scope of this paper, these results provide rigorous foundations for the
intuition that large momentum or contrarian forces can amplify shocks,
destabilize filtering, and generate the possibility of equilibrium
multiplicity.

## 7. Conclusion

This paper develops a continuous-time Kyle model in which aggregate noise trading is no longer purely exogenous, but instead reflects mechanically price-responsive behavior. By modeling momentum and contrarian traders as linear diffusions driven by price innovations, we embed endogenous feedback into a tractable linear–Gaussian structure. The market maker’s inference problem remains finite-dimensional and is governed by a Kalman–Bucy filter whose conditional covariance matrix satisfies a coupled Riccati equation. The insider’s optimization problem leads to a forward–backward system derived from Pontryagin’s Maximum Principle, yielding a fully analytic characterization of equilibrium.

Within this framework we identify two regimes. Under weak feedback, the classical Kyle equilibrium is preserved in a robust sense: locally equilibrium exists and is unique, trading intensity and price informativeness depend smoothly on feedback parameters, and the filtering channel remains well behaved. This allows for explicit first-order comparative statics that quantify how price-responsive noise trading accelerates Bayesian learning and alters the insider’s informational rents. Importantly, these effects arise not from ad hoc changes in noise volatility, but from endogenous interactions between order flow, price impact, and inference.

Under strong feedback, the analytical structure sustaining equilibrium can break down. We show that sufficiently large momentum or contrarian sensitivities can cause finite-time blowup of the Riccati equation, loss of contraction of the equilibrium fixed-point mapping, or instability of the Kalman–Bucy filter. These phenomena have clear economic interpretations: feedback amplification can overwhelm the informational role of liquidity trading, distort the market maker’s inference, and generate the possibility of multiple or unstable equilibria in which prices no longer aggregate information reliably. These results illustrate how feedback trading can fundamentally alter the dynamics of price discovery in continuous time.

The framework developed here provides a foundation for several promising extensions. One avenue is to incorporate risk aversion or inventory costs for market makers, which would interact nontrivially with feedback-driven volatility. Another is to allow for multiple strategic informed traders or to examine settings with public signals or attention constraints, in which feedback may amplify or dampen the value of information. Finally, the linear specification for momentum and contrarian traders may be enriched to study nonlinear or regime-switching rules.

By integrating behavioral trading rules into a tractable continuous-time microstructure equilibrium, this paper bridges classical asymmetric-information theory with modern models of mechanically driven order flow. The analysis reveals both the robustness and the fragility of the Kyle framework in the presence of feedback and highlights new mathematical mechanisms through which price-responsive trading can shape market stability and informational efficiency.

## Appendix A Perturbation of the Riccati Equation

This appendix derives the first-order sensitivity of the conditional covariance matrix with respect to the feedback parameter γF\gamma\_{F}.

### A.1. Setup

Let Σt​(γF)\Sigma\_{t}(\gamma\_{F}) denote the conditional covariance matrix of the state vector, which solves the Riccati equation

|  |  |  |  |
| --- | --- | --- | --- |
| (A.1) |  | Σ˙t=At​Σt+Σt​At⊤+Qt−Σt​Ct⊤​R−1​Ct​Σt,\dot{\Sigma}\_{t}=A\_{t}\Sigma\_{t}+\Sigma\_{t}A\_{t}^{\top}+Q\_{t}-\Sigma\_{t}C\_{t}^{\top}R^{-1}C\_{t}\Sigma\_{t}, |  |

where
Ct=(βt,γF,γC)C\_{t}=(\beta\_{t},\gamma\_{F},\gamma\_{C}) and R=σz2.R=\sigma\_{z}^{2}.

Only the quadratic term in ([A.1](https://arxiv.org/html/2601.09872v1#A1.E1 "In A.1. Setup ‣ Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders")) depends on γF\gamma\_{F}.

### A.2. First-Order expansion

Under the local existence and uniqueness result in Theorem [5.1](https://arxiv.org/html/2601.09872v1#S5.Thmthm1 "Theorem 5.1. ‣ 5.1. Local existence and uniqueness of equilibrium ‣ 5. Weak Feedback ‣ A continuous-time Kyle model with price-responsive traders"), the solution Σt​(γF)\Sigma\_{t}(\gamma\_{F}) depends smoothly on γF\gamma\_{F} in a neighborhood of γF=0\gamma\_{F}=0. We therefore expand

|  |  |  |  |
| --- | --- | --- | --- |
| (A.2) |  | Σt​(γF)=Σt(0)+γF​Σt(1)+o​(γF),\Sigma\_{t}(\gamma\_{F})=\Sigma\_{t}^{(0)}+\gamma\_{F}\Sigma\_{t}^{(1)}+o(\gamma\_{F})\ , |  |

where

|  |  |  |
| --- | --- | --- |
|  | Σt(0):=Σt​(0),Σt(1):=∂Σt∂γF|γF=0.\Sigma\_{t}^{(0)}:=\Sigma\_{t}(0)\ ,\qquad\Sigma\_{t}^{(1)}:=\left.\frac{\partial\Sigma\_{t}}{\partial\gamma\_{F}}\right|\_{\gamma\_{F}=0}\ . |  |

### A.3. Linearized Riccati equation

Define the mapping

|  |  |  |
| --- | --- | --- |
|  | F​(Σ,γF)=At​Σ+Σ​At⊤+Qt−Σ​C​(γF)⊤​R−1​C​(γF)​Σ.F(\Sigma,\gamma\_{F})=A\_{t}\Sigma+\Sigma A\_{t}^{\top}+Q\_{t}-\Sigma C(\gamma\_{F})^{\top}R^{-1}C(\gamma\_{F})\Sigma\ . |  |

Then Σ˙t​(γF)=F​(Σt​(γF),γF)\dot{\Sigma}\_{t}(\gamma\_{F})=F(\Sigma\_{t}(\gamma\_{F}),\gamma\_{F}).

Differentiating with respect to γF\gamma\_{F} at γF=0\gamma\_{F}=0 yields

|  |  |  |  |
| --- | --- | --- | --- |
| (A.3) |  | Σ˙t(1)=∂ΣF​(Σt(0),0)​[Σt(1)]+∂γFF​(Σt(0),0),Σ0(1)=0.\dot{\Sigma}\_{t}^{(1)}=\partial\_{\Sigma}F(\Sigma\_{t}^{(0)},0)\big[\Sigma\_{t}^{(1)}\big]+\partial\_{\gamma\_{F}}F(\Sigma\_{t}^{(0)},0)\ ,\qquad\Sigma\_{0}^{(1)}=0\ . |  |

The linearized Riccati operator ℒt:=∂ΣF​(Σt(0),0)\mathcal{L}\_{t}:=\partial\_{\Sigma}F(\Sigma\_{t}^{(0)},0) acts on a matrix HH as

|  |  |  |  |
| --- | --- | --- | --- |
| (A.4) |  | ℒt​[H]=At​H+H​At⊤−H​C0⊤​R−1​C0​Σt(0)−Σt(0)​C0⊤​R−1​C0​H,\mathcal{L}\_{t}[H]=A\_{t}H+HA\_{t}^{\top}-HC\_{0}^{\top}R^{-1}C\_{0}\Sigma\_{t}^{(0)}-\Sigma\_{t}^{(0)}C\_{0}^{\top}R^{-1}C\_{0}H\ , |  |

where

|  |  |  |
| --- | --- | --- |
|  | C0=(βt(0),0,0).C\_{0}=(\beta\_{t}^{(0)},0,0). |  |

Moreover, since ∂C/∂γF=(0,1,0)\partial C/\partial\gamma\_{F}=(0,1,0), the forcing term is

|  |  |  |  |
| --- | --- | --- | --- |
| (A.5) |  | ∂γFF​(Σt(0),0)=−Σt(0)​(∂C⊤∂γF​R−1​C0+C0⊤​R−1​∂C∂γF)​Σt(0).\partial\_{\gamma\_{F}}F(\Sigma\_{t}^{(0)},0)=-\Sigma\_{t}^{(0)}\left(\frac{\partial C^{\top}}{\partial\gamma\_{F}}R^{-1}C\_{0}+C\_{0}^{\top}R^{-1}\frac{\partial C}{\partial\gamma\_{F}}\right)\Sigma\_{t}^{(0)}. |  |

Equations ([A.3](https://arxiv.org/html/2601.09872v1#A1.E3 "In A.3. Linearized Riccati equation ‣ Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders"))–([A.5](https://arxiv.org/html/2601.09872v1#A1.E5 "In A.3. Linearized Riccati equation ‣ Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders")) define a linear nonhomogeneous matrix ODE for Σt(1)\Sigma\_{t}^{(1)}.

### A.4. Solution via variation of constants

Let Φ​(t,s)\Phi(t,s) denote the fundamental solution associated with the homogeneous equation

|  |  |  |
| --- | --- | --- |
|  | H˙t=ℒt​[Ht],Φ​(s,s)=I.\dot{H}\_{t}=\mathcal{L}\_{t}[H\_{t}],\qquad\Phi(s,s)=I. |  |

That is, for any matrix HsH\_{s}, the function Ht=Φ​(t,s)​[Hs]H\_{t}=\Phi(t,s)[H\_{s}] solves the homogeneous equation.

Then, the solution to ([A.3](https://arxiv.org/html/2601.09872v1#A1.E3 "In A.3. Linearized Riccati equation ‣ Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (A.6) |  | Σt(1)=∫0tΦ​(t,s)​[∂γFF​(Σs(0),0)]​𝑑s.\Sigma\_{t}^{(1)}=\int\_{0}^{t}\Phi(t,s)\big[\partial\_{\gamma\_{F}}F(\Sigma\_{s}^{(0)},0)\big]\,ds\ . |  |

Substituting ([A.5](https://arxiv.org/html/2601.09872v1#A1.E5 "In A.3. Linearized Riccati equation ‣ Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders")) into ([A.6](https://arxiv.org/html/2601.09872v1#A1.E6 "In A.4. Solution via variation of constants ‣ Appendix A Perturbation of the Riccati Equation ‣ A continuous-time Kyle model with price-responsive traders")) yields

|  |  |  |
| --- | --- | --- |
|  | ∂Σv​v​(t)∂γF=−∫0tΦ​(t,s)​(2​βs(0)​Σv​v(0)​(s)​Σv​m(0)​(s)/σz2)​𝑑s.\frac{\partial\Sigma\_{vv}(t)}{\partial\gamma\_{F}}=-\int\_{0}^{t}\Phi(t,s)\,\big(2\beta^{(0)}\_{s}\Sigma\_{vv}^{(0)}(s)\Sigma\_{vm}^{(0)}(s)/\sigma\_{z}^{2}\big)\,ds\ . |  |

Typically, Σv​m(0)​(s)>0\Sigma\_{vm}^{(0)}(s)>0 (positive correlation between vv and momentum state). So, we have ∂Σv​v​(t)∂γF<0\frac{\partial\Sigma\_{vv}(t)}{\partial\gamma\_{F}}<0, reducing price informativeness.

## References

* [1]
  K. Back, C. H. Cao, and G. A. Willard (2000)
  Imperfect competition among informed traders.
  The journal of finance 55 (5),  pp. 2117–2155.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [2]
  K. Back, F. Cocquemas, I. Ekren, and A. Lioui (2021)
  Optimal transport and risk aversion in Kyle’s model of informed trading.
  arXiv preprint arXiv:2006.09518.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [3]
  K. Back, P. Collin-Dufresne, V. Fos, T. Li, and A. Ljungqvist (2018)
  Activism, strategic trading, and liquidity.
  Econometrica 86 (4),  pp. 1431–1463.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [4]
  K. Back and H. Pedersen (1998)
  Long-lived information and intraday patterns.
  Journal of financial markets 1 (3-4),  pp. 385–402.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [5]
  K. Back (1992)
  Insider trading in continuous time.
  The Review of Financial Studies 5 (3),  pp. 387–409.
  Cited by: [§1](https://arxiv.org/html/2601.09872v1#S1.p1.1 "1. Introduction ‣ A continuous-time Kyle model with price-responsive traders"),
  [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [6]
  S. Baruch (2002)
  Insider trading and risk aversion.
  Journal of Financial Markets 5 (4),  pp. 451–464.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [7]
  F. Black (1986)
  Noise.
  The Journal of Finance 41 (3),  pp. 528–543.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/j.1540-6261.1986.tb04513.x),
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1986.tb04513.x),
  https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1540-6261.1986.tb04513.x
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p4.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [8]
  S. Bose and I. Ekren (2023)
  Kyle–Back models with risk aversion and non-Gaussian beliefs.
  The Annals of Applied Probability 33 (6A),  pp. 4238–4271.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [9]
  S. Bose and I. Ekren (2024)
  Multidimensional Kyle–Back model with a risk averse informed trader.
  SIAM Journal on Financial Mathematics 15 (1),  pp. 93–120.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [10]
  M. K. Brunnermeier (2001-01)
  Asset pricing under asymmetric information: bubbles, crashes, technical analysis, and herding.
   Oxford University Press.
  External Links: ISBN 9780198296980,
  [Document](https://dx.doi.org/10.1093/0198296983.001.0001)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p3.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [11]
  L. Campi, U. Cetin, and A. Danilova (2011)
  Dynamic Markov bridges motivated by models of insider trading.
  Stochastic Processes and their Applications 121 (3),  pp. 534–567.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [12]
  L. Campi and U. Cetin (2007)
  Insider trading in an equilibrium model with default: a passage from reduced-form to structural modelling.
  Finance and stochastics 11 (4),  pp. 591–602.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [13]
  G. Cespa and X. Vives (2012)
  Dynamic trading and asset prices: keynes vs. Hayek.
  The Review of Economic Studies 79 (2),  pp. 539–580.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p3.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders"),
  [Remark 6.4](https://arxiv.org/html/2601.09872v1#S6.Thmthm4.p1.1.1 "Remark 6.4. ‣ 6.2. Loss of uniqueness of the equilibrium fixed point ‣ 6. Strong Feedback and Breakdown of Equilibrium ‣ A continuous-time Kyle model with price-responsive traders").
* [14]
  U. Çetin and A. Danilova (2016)
  Markovian Nash equilibrium in financial markets with asymmetric information and related forward–backward systems.
  The Annals of Applied Probability 26 (4),  pp. 1996–2029.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [15]
  U. Çetin and A. Danilova (2018)
  On pricing rules and optimal strategies in general Kyle-Back models.
  arXiv preprint arXiv:1812.07529.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [16]
  U. Çetin (2018)
  Financial equilibrium with asymmetric information and random horizon.
  Finance and Stochastics (1).
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [17]
  R. Chhaibi, I. Ekren, E. Noh, and L. Vy (2022)
  Informed trading via Monge–Kantorovich duality.
  External Links: 2210.17384,
  [Link](https://arxiv.org/abs/2210.17384)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [18]
  R. Chhaibi, I. Ekren, and E. Noh (2025)
  Solvability of the Gaussian Kyle model with imperfect information and risk aversion.
  arXiv preprint arXiv:2501.16488.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [19]
  J. H. Choi, H. Kwon, and K. Larsen (2023)
  Trading constraints in continuous-time Kyle models.
  SIAM Journal on Control and Optimization 61 (3),  pp. 1494–1512.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [20]
  P. Collin-Dufresne and V. Fos (2016)
  Insider trading, stochastic liquidity, and equilibrium prices.
  Econometrica 84 (4),  pp. 1441–1475.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders"),
  [§2](https://arxiv.org/html/2601.09872v1#S2.p3.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [21]
  J. M. Corcuera, G. Farkas, G. Di Nunno, and B. Oksendal (2010)
  Kyle-Back’s model with Lévy noise.
  Preprint series in pure mathematics.
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [22]
  X. Dai, J. Zhang, and V. Chang (2025)
  Noise traders in an agent-based artificial stock market.
  Annals of Operations Research 352 (3),  pp. 715–744.
  External Links: [Document](https://dx.doi.org/10.1007/s10479-023-05528-7),
  ISBN 1572-9338,
  [Link](https://doi.org/10.1007/s10479-023-05528-7)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p4.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [23]
  J. B. de Long, A. Shleifer, L. H. Summers, and R. J. Waldmann (1990)
  Positive feedback investment strategies and destabilizing rational speculation.
  The Journal of Finance 45 (2),  pp. 379–395.
  External Links: ISSN 00221082, 15406261
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p4.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [24]
  I. Ekren, B. Mostowski, and G. Žitković (2025/10/01)
  Kyle’s model with stochastic liquidity.
  Finance and Stochastics 29 (4),  pp. 1195–1231.
  External Links: [Document](https://dx.doi.org/10.1007/s00780-025-00574-4),
  ISBN 1432-1122,
  [Link](https://doi.org/10.1007/s00780-025-00574-4)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [25]
  Z. He and A. Krishnamurthy (2013-04)
  Intermediary asset pricing.
  American Economic Review 103 (2),  pp. 732–70.
  External Links: [Document](https://dx.doi.org/10.1257/aer.103.2.732)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p3.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [26]
  A. S. Kyle (1985)
  Continuous auctions and insider trading.
  Econometrica: Journal of the Econometric Society,  pp. 1315–1335.
  Cited by: [§1](https://arxiv.org/html/2601.09872v1#S1.p1.1 "1. Introduction ‣ A continuous-time Kyle model with price-responsive traders"),
  [§2](https://arxiv.org/html/2601.09872v1#S2.p1.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [27]
  E. Sentana and S. Wadhwani (1992)
  Feedback traders and stock return autocorrelations: evidence from a century of daily data.
  The Economic Journal 102 (411),  pp. 415–425.
  External Links: ISSN 00130133, 14680297,
  [Link](http://www.jstor.org/stable/2234525)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p4.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [28]
  R. J. Shiller, S. Fischer, and B. M. Friedman (1984)
  Stock prices and social dynamics.
  Brookings Papers on Economic Activity 1984 (2),  pp. 457–510.
  External Links: ISSN 00072303, 15334465,
  [Link](http://www.jstor.org/stable/2534436)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p4.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [29]
  R. J. Shiller (1990)
  Speculative prices and popular models.
  The Journal of Economic Perspectives 4 (2),  pp. 55–65.
  External Links: ISSN 08953309,
  [Link](http://www.jstor.org/stable/1942890)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p4.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").
* [30]
  W. Xiong (2001)
  Convergence trading with wealth effects: an amplification mechanism in financial markets.
  Journal of Financial Economics 62 (2),  pp. 247–292.
  External Links: ISSN 0304-405X,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/S0304-405X%2801%2900078-2)
  Cited by: [§2](https://arxiv.org/html/2601.09872v1#S2.p3.1 "2. Literature review ‣ A continuous-time Kyle model with price-responsive traders").