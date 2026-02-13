---
authors:
- Federico Cacciamani
- Roberto Daluiso
- Marco Pinciroli
- Michele Trapletti
- Edoardo Vittori
doc_id: arxiv:2602.12030v1
family_id: arxiv:2602.12030
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Time-inhomogeneous volatility aversion for financial applications of reinforcement
  learning
url_abs: http://arxiv.org/abs/2602.12030v1
url_html: https://arxiv.org/html/2602.12030v1
venue: arXiv q-fin
version: 1
year: 2026
---


Federico Cacciamani
Cross Asset Systematic Trading, IMI Corporate and Investment Banking, Intesa Sanpaolo.
  
Roberto Daluiso
Interest Rates and Credit Models, IMI Corporate and Investment Banking, Intesa Sanpaolo. Corresponding author: roberto.daluiso@intesasanpaolo.com.
  
Marco Pinciroli
XVA Management and KVA Pricing, IMI Corporate and Investment Banking, Intesa Sanpaolo.
  
Michele Trapletti33footnotemark: 3
  
Edoardo Vittori11footnotemark: 1

(February 5, 2026)

###### Abstract

In finance, sequential decision problems are often faced, for which reinforcement learning (RL) emerges as a promising tool for optimisation without the need of analytical tractability. However, the objective of classical RL is the expected cumulated reward, while financial applications typically require a trade-off between return and risk. In this work, we focus on settings where one cares about the time split of the total return, ruling out most risk-aware generalisations of RL which optimise a risk measure defined on the latter. We notice that a preference for homogeneous splits, which we found satisfactory for hedging, can be unfit for other problems, and therefore propose a new risk metric which still penalises uncertainty of the single rewards, but allows for an arbitrary planning of their target levels. We study the properties of the resulting objective and the generalisation of learning algorithms to optimise it. Finally, we show numerical results on toy examples.

Keywords: risk aversion, optimal execution, grid world

## 1 Introduction

In many sequential decision problems, maximisation of expected reward is not the only objective, as risk must be kept under control.
Once one has defined a way to quantify this risk, then by elementary Lagrange multiplier theory, without loss of generality one can maximise a single objective where the risk metric multiplied by a risk aversion coefficient is subtracted from the expected reward.
However, the risk metric should be carefully crafted to both accurately describe the goal and allow efficient optimisation.
The former requirement is in general application-specific.

In particular, classical risk measures defined on the total return do not completely align with the needs of trading applications, as they are insensitive to the time distribution of profits and losses, which financial institutions care about for reasons related to financing, budgeting, etc.
To overcome this issue, Bisi et al.,  ([2020](https://arxiv.org/html/2602.12030v1#bib.bib3)) proposed to measure risk as a variance across both time and population (which they call “reward volatility”), thus expressing a preference not only for low randomness of the return, but also for a homogeneous split thereof over time steps.

This preference for homogeneity has proven practically appropriate for hedging applications, see e.g. Vittori et al.,  ([2020](https://arxiv.org/html/2602.12030v1#bib.bib31)); Mandelli et al.,  ([2023](https://arxiv.org/html/2602.12030v1#bib.bib18)); [Daluiso et al., 2023b](https://arxiv.org/html/2602.12030v1#bib.bib8) ; although the extended version of the latter ([Daluiso et al., 2023a,](https://arxiv.org/html/2602.12030v1#bib.bib7) ) already underlines that when the horizon is random, one must carefully define in which sense the dispersion of rewards should be homogeneous across realisations.
However, in fixed-horizon problems, which are a fortiori non stationary, forcing comparable returns at different times may introduce an undesired distortion into the objective function.111Note that the hedging problems in the above papers are themselves formulated with finite horizons; in those specific applications, good policies are nonetheless expected to produce uniform reward histories, so that volatility-penalised optimisation is appropriate, but in a sense, this is an accident.
For instance, in so-called optimal execution tasks which consist in the liquidation of a large amount of an asset, when marking-to-market the value of the residual position, the impact of transactions on prices can easily introduce a larger *expected* loss at the beginning, when most of the asset to be liquidated is still in the portfolio: plain reward volatility optimisation would improperly strive to counterbalance this natural pattern, and we believe one should not (see [Section 3.2](https://arxiv.org/html/2602.12030v1#S3.SS2 "3.2 Deterministic-horizon example: optimal execution ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") for details).

In this paper, we design a different family of risk-aware objective functions, which retains a tractable policy gradient to be used in advanced policy search or actor-critic algorithms, and still penalises risk (in the sense of probabilistic uncertainty) of the *single* rewards, but allows for an arbitrary planning of their *individual* target values. The rationale is that a completely deterministic reward path known in advance should not be considered “risky” in any financially meaningful sense, whatever its time profile.

After a review of relevant literature in [Section 1.1](https://arxiv.org/html/2602.12030v1#S1.SS1 "1.1 Related literature ‣ 1 Introduction ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"), the body of the paper is organised in two main sections.
In [Section 2](https://arxiv.org/html/2602.12030v1#S2 "2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") we define the proposed objective functions and study their properties, introducing reinforcement learning based algorithms to optimise them.
In [Section 3](https://arxiv.org/html/2602.12030v1#S3 "3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") we observe the behaviour of the optimal policies on three example problems: the first one is an artificial example solvable in closed form which should clarify the difference between our concept of risk aversion and existing alternatives; the second one is a financial example showing the efficacy of our setup on a problem with a fixed deterministic horizon; while the third one is a classical non financial reinforcement learning test case, where some unanticipated effects of stochastic horizons can be appreciated.
[Section 4](https://arxiv.org/html/2602.12030v1#S4 "4 Conclusion ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") concludes the paper with some final considerations.

### 1.1 Related literature

By the present day, there is a large literature on risk aversion in the machine learning subfield dedicated to sequential decision problems, known as Reinforcement Learning (RL): we refer to García and Fernández,  ([2015](https://arxiv.org/html/2602.12030v1#bib.bib13)) for a comprehensive review. For our purpose, we only attempt a broad conceptual categorisation of the optimisation criteria and list only a few notable papers for each category, just as examples and starting points for the interested reader.

The simplest approach is to apply a non-linear transformation to each realised reward (see e.g. Shen et al., , [2014](https://arxiv.org/html/2602.12030v1#bib.bib27)); Conceptually, such a path-by-path transformation represents more a subjective weighting of the objective outcomes (e.g., a different relevance given to monetary profits and losses), than a measure of “risk” in the proper financial meaning of the term, namely a preference ordering on the probability distribution of rewards.

A more principled approach is to apply a non-linear risk measure to the random variable representing the sum of discounted rewards (see e.g. Moody and Saffell, , [2001](https://arxiv.org/html/2602.12030v1#bib.bib21); Di Castro et al., , [2012](https://arxiv.org/html/2602.12030v1#bib.bib9); Morimura et al., , [2010](https://arxiv.org/html/2602.12030v1#bib.bib23); Tamar and Mannor, , [2013](https://arxiv.org/html/2602.12030v1#bib.bib30); Prashanth and Ghavamzadeh, , [2014](https://arxiv.org/html/2602.12030v1#bib.bib26); Tamar et al., , [2015](https://arxiv.org/html/2602.12030v1#bib.bib28), [2017](https://arxiv.org/html/2602.12030v1#bib.bib29); Chow et al., , [2017](https://arxiv.org/html/2602.12030v1#bib.bib5)). In such setting, unless one finds a clever algorithm crafted for a very specific choice of risk measure, generally speaking the problem becomes very unsuitable for genuine RL approaches, as one is forced to attribute the full result to the last timestep of the episode, with no intermediate rewards. For instance, Neagu et al.,  ([2025](https://arxiv.org/html/2602.12030v1#bib.bib25)) tries different state-of-the-art algorithms for hedging in this formulation, and empirically finds satisfactory results only with direct policy search (in a way, more a supervised than a reinforcement learning algorithm). However, gradient descent on policy parameters is only possible if the full environment is a differentiable function of actions, which is often not the case in other applications, or daunting to implement even when theoretically true.

Approaches where the time split of rewards matters are less common: besides the already discussed Bisi et al.,  ([2020](https://arxiv.org/html/2602.12030v1#bib.bib3)), we mention the proposals based on dynamic risk measures (Coache and Jaimungal, , [2023](https://arxiv.org/html/2602.12030v1#bib.bib6); Marzban et al., , [2023](https://arxiv.org/html/2602.12030v1#bib.bib19)), which are designed to have time-consistent optimal policies, i.e. optimal also for the conditional risk measure as seen from any future state which can be reached. This means that these approaches take care of the risk of *co-terminal* problems, which is complementary to the view of the present paper where our focus on planning/budgeting could in some sense be understood more in terms of *co-starting* risk. This also explains why we are not particularly interested in consistency properties, as obviously in such settings the starting time is righteously special as the occasion when agents lay down their plans. See also [Section 3.1](https://arxiv.org/html/2602.12030v1#S3.SS1 "3.1 Toy example ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") for a comparison on a toy example.

To conclude on risk-aware generalisations of RL beyond the scope of finance, it is worth mentioning the growing literature in robust reinforcement learning: see Moos et al.,  ([2022](https://arxiv.org/html/2602.12030v1#bib.bib22)) for a review. Here “risk” takes yet another meaning related to prudent optimisation under a *set* of candidate probability measures, which in financial jargon would map to the concepts of “model risk” and “Knightian uncertainty”, while here we hope to manage *market* risk.

Turning to finance-specific contributions, one of the richest streams is related to the problem of dynamic hedging of a derivative portfolio. Within such field often named “deep hedging”, some more works looking into stepwise rewards represented by the period Profit and Loss (PnL) can be found, as doing so is clearly more aligned with real-life practice. Such papers can usually introduce risk in interesting but *ad hoc* ways given their scoping to this specific application. In particular, Kolm and Ritter,  ([2019](https://arxiv.org/html/2602.12030v1#bib.bib17)); Du et al.,  ([2020](https://arxiv.org/html/2602.12030v1#bib.bib10)) justify a reward which is a linear-quadratic transformation of the PnL by heuristically first proxying the mean-variance with the sum of the mean-variances of the rewards, and then proxying the variance of the reward by its expected square, guessing that the square of the mean period PnL should be small. Halperin,  ([2019](https://arxiv.org/html/2602.12030v1#bib.bib14), [2020](https://arxiv.org/html/2602.12030v1#bib.bib15)) instead penalises the conditional co-terminal variance of the value of the hedging portfolio, arguing that the value of the derivative should be defined by the hedging process itself. Finally, among the deep hedging papers introducing more traditionally a risk measure on the final return, we just mention Mueller et al.,  ([2024](https://arxiv.org/html/2602.12030v1#bib.bib24)) because they also feel the need to cleanup the penalised variance from a component of reward which is not a direct measure of residual market risk, namely transaction costs; however, this modification is very specific to the application, and would not coincide with our definition even on a single-step problem, as costs introduce genuine variability also at each fixed time due to the randomness of the rebalancing amounts, whose risk is still penalised in our objective functions.

Finally, as already anticipated, one of the key ingredients in our definitions is the tuning of deterministic targets to the single rewards, and a similar idea of setting a unique target for the full return can be recognised in previous works, including at least the seminal Buehler et al.,  ([2019](https://arxiv.org/html/2602.12030v1#bib.bib4)) and the recent Han et al.,  ([2025](https://arxiv.org/html/2602.12030v1#bib.bib16)).

## 2 Theory

### 2.1 Definitions and properties

This section presents our proposed risk-aware reinforcement learning formulation, by first proposing a modification of the mean-volatility criterion, and then recognizing that it can be seen as an instance of a larger family of objective functions.

We work in the context of an inhomogeneous Markov Decision Process and intentionally generalise the homogeneous notation of [Daluiso et al., 2023a](https://arxiv.org/html/2602.12030v1#bib.bib7) , as the definitions and proofs will be similar. In particular, we denote by (si)i≥0(s\_{i})\_{i\geq 0} the sequence of states in the state space 𝒮\mathcal{S}; by (ai)i≥0(a\_{i})\_{i\geq 0} the sequence of actions in the action space 𝒜\mathcal{A}; by μ\mu the initial state distribution; by ε∈(0,∞]\varepsilon\in(0,\infty] the number of steps; by γ\gamma the discount factor, and by Γ\Gamma their cumulated value ∑i=1εγi−1\sum\_{i=1}^{\varepsilon}\gamma^{i-1}; by (ri)i>0(r\_{i})\_{i>0} the sequence of real-valued rewards, and by 𝒢\mathcal{G} the return ∑i=1εγi−1​ri\sum\_{i=1}^{\varepsilon}\gamma^{i-1}r\_{i}. We assume without loss of generality that the Markov chain ss is extended to time steps beyond ε\varepsilon in a way that ε<i\varepsilon<i is a function of sis\_{i}, e.g. by introduction of an absorbing post-episode-end state.

On the other hand, to account for time inhomogeneity, the law of si+1s\_{i+1} given the state sis\_{i} and the action aia\_{i} at the ii-th time step will be indexed by ii, using the notation 𝒫i(⋅|si,ai)\mathcal{P}\_{i}(\cdot|s\_{i},a\_{i}). Similarly, the model for ri+1r\_{i+1} will be described by a conditional law ℛi(⋅|si,ai,si+1)\mathcal{R}\_{i}(\cdot|s\_{i},a\_{i},s\_{i+1}), and the randomised policy π\pi by the conditional laws πi(⋅|si)\pi\_{i}(\cdot|s\_{i}) of aia\_{i} given the state sis\_{i} at the ii-th step.

We now introduce some new definitions. The expected value of the ii-th reward is

|  |  |  |  |
| --- | --- | --- | --- |
|  | r¯π,i:=𝔼π⁡[ri|ε≥i],\bar{r}\_{\pi,i}:=\operatorname\*{\mathbb{E}\_{\pi}}[r\_{i}|\varepsilon\geq i], |  | (2.1) |

and we define a risk metric which penalises deviation from this value:

###### Definition 2.1 (Inhomogeneous reward volatility).

The inhomogeneous reward volatility or inhomogeneous reward variance is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ςπ2\displaystyle\varsigma^{2}\_{\pi} | =𝔼π⁡[∑i=1εγi−1​(ri−r¯π,i)2]\displaystyle=\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\left(r\_{i}-\bar{r}\_{\pi,i}\right)^{2}\right] |  | (2.2) |

###### Definition 2.2 (Inhomogeneous mean-volatility).

Given a risk aversion coefficient β≥0{\beta\geq 0}, the ranking criterion for policies is the inhomogeneous mean-volatility functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | π→𝔼π⁡[𝒢]−β​ςπ2.\pi\rightarrow\operatorname\*{\mathbb{E}\_{\pi}}\left[\mathcal{G}\right]-\beta\varsigma^{2}\_{\pi}. |  | (2.3) |

###### Remark 2.3 (Comparison to homogeneous definitions).

The above differ from unnormalised reward volatility and mean-volatility as defined in [Daluiso et al., 2023a](https://arxiv.org/html/2602.12030v1#bib.bib7)

|  |  |  |
| --- | --- | --- |
|  | ν^π2=𝔼π⁡[∑i=1εγi−1​(ri−Jπ)2]⁡ and ​𝔼π⁡[𝒢]−β​ν^π2, where ​Jπ:=𝔼π⁡[Γ−1​𝒢]\hat{\nu}^{2}\_{\pi}=\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\left(r\_{i}-J\_{\pi}\right)^{2}\right]\text{ and }\operatorname\*{\mathbb{E}\_{\pi}}\left[\mathcal{G}\right]-\beta\hat{\nu}^{2}\_{\pi},\quad\text{ where }J\_{\pi}:=\operatorname\*{\mathbb{E}\_{\pi}}\left[\Gamma^{-1}\mathcal{G}\right] |  |

precisely in that the latter subtract a common average value JπJ\_{\pi} from each reward rir\_{i}, while in ([2.2](https://arxiv.org/html/2602.12030v1#S2.E2 "Equation 2.2 ‣ Definition 2.1 (Inhomogeneous reward volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) we have a different central value r¯π,i\bar{r}\_{\pi,i} for each time step ii.

###### Remark 2.4 (Irreducibility to classical RL).

The simpler way to introduce risk aversion in a sequential decision problem is to apply a nonlinear transformation to the reward profile and then use a classical RL formulation. Sometimes this is even conceptually equivalent to more complex formulations, though maybe less efficient algorithmically. For instance, a Pareto-optimal mean-variance policy maximises variance among all policies with given expected return, and hence also maximises 𝔼π⁡[𝒢2]\operatorname\*{\mathbb{E}\_{\pi}}[\mathcal{G}^{2}] for fixed 𝔼π⁡[𝒢]\operatorname\*{\mathbb{E}\_{\pi}}[\mathcal{G}]: therefore, to determine the Pareto frontier, instead of using an ad hoc algorithm to optimise 𝔼π⁡[𝒢]−β​𝕍​arπ​[𝒢]\operatorname\*{\mathbb{E}\_{\pi}}[\mathcal{G}]-\beta\,\mathbb{V}\mathrm{ar}\_{\pi}[\mathcal{G}], one may in principle optimise classically the expected value of a modified terminal payoff 𝒢−β′​𝒢2\mathcal{G}-\beta^{\prime}\mathcal{G}^{2}, where we introduced a new symbol β′\beta^{\prime} to clarify that the solution to the original problem for fixed β\beta will be found for a different and a priori unknown value β′\beta^{\prime} of the Lagrange multiplier. Analogously, with homogeneous mean-volatility in fixed horizon problems where ε\varepsilon is almost surely constant, the risk criterion is

|  |  |  |
| --- | --- | --- |
|  | ν^π2=∑i=1εγi−1​𝔼π⁡[ri2]+∑i=1εγi−1​Jπ2−2​∑i=1εγi−1​𝔼π⁡[ri]⁡Jπ=𝔼π⁡[∑i=1εγi−1​ri2]−Γ​Jπ2,\hat{\nu}\_{\pi}^{2}=\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\operatorname\*{\mathbb{E}\_{\pi}}\left[r\_{i}^{2}\right]+\sum\_{i=1}^{\varepsilon}\gamma^{i-1}J\_{\pi}^{2}-2\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\operatorname\*{\mathbb{E}\_{\pi}}\left[r\_{i}\right]J\_{\pi}=\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=1}^{\varepsilon}\gamma^{i-1}r\_{i}^{2}\right]-\Gamma J\_{\pi}^{2}, |  |

where Γ​Jπ=𝔼π⁡[𝒢]\Gamma J\_{\pi}=\operatorname\*{\mathbb{E}\_{\pi}}[\mathcal{G}] is exactly the return criterion: therefore, Pareto-optimal homogeneous mean-volatility policies should be spanned by classical optimisers of the transformed reward ri−β′​ri2r\_{i}-\beta^{\prime}r\_{i}^{2}.

This is not the case for the new objective ([2.3](https://arxiv.org/html/2602.12030v1#S2.E3 "Equation 2.3 ‣ Definition 2.2 (Inhomogeneous mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")). Indeed, even for constant ε\varepsilon, while one can write the risk as ςπ2=∑i=1εγi−1​𝕍​arπ​[ri]\varsigma^{2}\_{\pi}=\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\mathbb{V}\mathrm{ar}\_{\pi}\left[r\_{i}\right],
expanding the variances one gets

|  |  |  |
| --- | --- | --- |
|  | 𝔼π⁡[∑i=1εγi−1​ri2]−∑i=1εγi−1​r¯i,π2\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=1}^{\varepsilon}\gamma^{i-1}r\_{i}^{2}\right]-\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\bar{r}\_{i,\pi}^{2} |  |

and this time the correction term ∑i=1εγi−1​r¯i,π2\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\bar{r}\_{i,\pi}^{2} to the plain return of the squared reward is not a function of the return criterion 𝔼π⁡[𝒢]\operatorname\*{\mathbb{E}\_{\pi}}[\mathcal{G}].

Quantitatively, one can note that the risk definition ([2.2](https://arxiv.org/html/2602.12030v1#S2.E2 "Equation 2.2 ‣ Definition 2.1 (Inhomogeneous reward volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) is weaker than that of reward volatility ν^π2\hat{\nu}^{2}\_{\pi}:

###### Theorem 2.5 (Volatility inequality).

For any policy π\pi, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν^π2≥ςπ2.\hat{\nu}^{2}\_{\pi}\geq\varsigma^{2}\_{\pi}. |  | (2.4) |

###### Proof.

The ii-th addend in ν^π2\hat{\nu}^{2}\_{\pi} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π⁡[γi−1​(ri−Jπ)2​Iε≥i]=γi−1​𝔼π⁡[𝔼π⁡[(ri−Jπ)2|ε≥i]​Iε≥i];\operatorname\*{\mathbb{E}\_{\pi}}\left[\gamma^{i-1}(r\_{i}-J\_{\pi})^{2}I\_{\varepsilon\geq i}\right]=\gamma^{i-1}\operatorname\*{\mathbb{E}\_{\pi}}\left[\operatorname\*{\mathbb{E}\_{\pi}}\left[(r\_{i}-J\_{\pi})^{2}|\varepsilon\geq i\right]I\_{\varepsilon\geq i}\right]; |  | (2.5) |

by applying to the law 𝔼π[⋅|ε≥i]\operatorname\*{\mathbb{E}\_{\pi}}\left[\cdot|\varepsilon\geq i\right] the elementary property that the constant xx which minimises the expectation of the quadratic error (ri−x)2(r\_{i}-x)^{2} is the mean, we get that

|  |  |  |
| --- | --- | --- |
|  | 𝔼π⁡[(ri−Jπ)2|ε≥i]≥𝔼π⁡[(ri−𝔼π⁡[ri|ε≥i])2|ε≥i]=𝔼π⁡[(ri−r¯π,i)2|ε≥i].\operatorname\*{\mathbb{E}\_{\pi}}\left[(r\_{i}-J\_{\pi})^{2}|\varepsilon\geq i\right]\geq\operatorname\*{\mathbb{E}\_{\pi}}\left[(r\_{i}-\operatorname\*{\mathbb{E}\_{\pi}}\left[r\_{i}|\varepsilon\geq i\right])^{2}|\varepsilon\geq i\right]=\operatorname\*{\mathbb{E}\_{\pi}}\left[(r\_{i}-\bar{r}\_{\pi,i})^{2}|\varepsilon\geq i\right]. |  |

Substituting back in ([2.5](https://arxiv.org/html/2602.12030v1#S2.E5 "Equation 2.5 ‣ Proof. ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), we get that the generic addend of ν^π2\hat{\nu}^{2}\_{\pi} is larger than that of ςπ2\varsigma^{2}\_{\pi}, concluding the proof.
∎

The comparison with the standard return variance is less neat, as no inequality holds in general if ε\varepsilon is stochastic. Indeed, a sequence of deterministic rewards stopped at a random episode end step has zero inhomogeneous reward volatility but positive return variance. On the other hand, if the horizon is deterministic as in most problems, then the new risk measure is stricter than the return variance σπ2=𝕍​arπ​[𝒢]\sigma\_{\pi}^{2}=\mathbb{V}\mathrm{ar}\_{\pi}\left[\mathcal{G}\right]:

###### Theorem 2.6 (Variance inequality).

For any policy π\pi, if ε\varepsilon is deterministic (finite or infinite), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | σπ2≤Γ​ςπ2.\sigma^{2}\_{\pi}\leq\Gamma\varsigma^{2}\_{\pi}. |  | (2.6) |

###### Proof.

For deterministic ε\varepsilon, the expected return appearing in the definition of variance is equal to the sum of γi−1​r¯π,i\gamma^{i-1}\bar{r}\_{\pi,i}. Then one can apply to the inner summation in the definition of σπ2\sigma\_{\pi}^{2} a discrete Jensen inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σπ2\displaystyle\sigma\_{\pi}^{2} | =𝔼πs0∼μ⁡[Γ2​(∑i=1εΓ−1​γi−1​(ri−r¯π,i))2]\displaystyle=\operatorname\*{\mathbb{E}\_{\pi}}\_{s\_{0}\sim\mu}\left[\Gamma^{2}\left(\sum\_{i=1}^{\varepsilon}\Gamma^{-1}\gamma^{i-1}(r\_{i}-\bar{r}\_{\pi,i})\right)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼πs0∼μ⁡[Γ2​∑i=1εΓ−1​γi−1​(ri−r¯π,i)2]=Γ​ςπ2.\displaystyle\leq\operatorname\*{\mathbb{E}\_{\pi}}\_{s\_{0}\sim\mu}\left[\Gamma^{2}\sum\_{i=1}^{\varepsilon}\Gamma^{-1}\gamma^{i-1}\left(r\_{i}-\bar{r}\_{\pi,i}\right)^{2}\right]=\Gamma\varsigma^{2}\_{\pi}. |  |

∎

The inhomogeneous mean-volatility criterion in ([2.3](https://arxiv.org/html/2602.12030v1#S2.E3 "Equation 2.3 ‣ Definition 2.2 (Inhomogeneous mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) solves the time-attribution issues of mean-variance and homogeneous mean-volatility, but it retains other drawbacks of using a variance as a risk criterion, which essentially derive from penalizing in the same way positive and negative deviations from the expected reward r¯π,i\bar{r}\_{\pi,i}. In contexts where this is not acceptable, one can use the following generalisation.

###### Definition 2.7 (Inhomogeneous ℓ\ell-volatility).

For any function ℓ:ℝ→ℝ+\ell:\mathbb{R}\to\mathbb{R}^{+} such that ℓ​(0)=0\ell(0)=0 and any policy π\pi, the inhomogeneous ℓ\ell-volatility or inhomogeneous ℓ\ell-variance is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ςπℓ=infr¯ℓ∈ℝℕ𝔼π⁡[∑i=1εγi−1​ℓ​(ri−r¯iℓ)]\varsigma^{\ell}\_{\pi}=\inf\_{\bar{r}^{\ell}\in\mathbb{R}^{\mathbb{N}}}\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\ell\left(r\_{i}-\bar{r}^{\ell}\_{i}\right)\right] |  | (2.7) |

and the inhomogeneous mean-ℓ\ell-volatility is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π⁡[𝒢]−ςπℓ.\operatorname\*{\mathbb{E}\_{\pi}}[\mathcal{G}]-\varsigma^{\ell}\_{\pi}. |  | (2.8) |

One immediately sees that ([2.7](https://arxiv.org/html/2602.12030v1#S2.E7 "Equation 2.7 ‣ Definition 2.7 (Inhomogeneous ℓ-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"))-([2.8](https://arxiv.org/html/2602.12030v1#S2.E8 "Equation 2.8 ‣ Definition 2.7 (Inhomogeneous ℓ-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) reduces to ([2.2](https://arxiv.org/html/2602.12030v1#S2.E2 "Equation 2.2 ‣ Definition 2.1 (Inhomogeneous reward volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"))-([2.3](https://arxiv.org/html/2602.12030v1#S2.E3 "Equation 2.3 ‣ Definition 2.2 (Inhomogeneous mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) for ℓ=β​(⋅)2\ell=\beta(\cdot)^{2}, since in such case the optimal target reward r¯π,iℓ\bar{r}^{\ell}\_{\pi,i} is the conditional mean r¯π,i\bar{r}\_{\pi,i}; while for instance ℓ​(x)=β​|x|\ell(x)=\beta|x| gives a risk penalty equal to a risk aversion coefficient β\beta times the absolute distance of the reward from the conditional median of the reward distribution. On the other hand, the generalised mean-ℓ\ell-volatility can be rewritten as a superposition of conditional performance metrics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π⁡[𝒢]−ςπℓ\displaystyle\operatorname\*{\mathbb{E}\_{\pi}}[\mathcal{G}]-\varsigma^{\ell}\_{\pi} | =∑i=1∞γi−1​ℙ​(ε≥i)​supr¯iℓ∈ℝ𝔼π⁡[ri−ℓ​(ri−r¯iℓ)|ε≥i]\displaystyle=\sum\_{i=1}^{\infty}\gamma^{i-1}\mathbb{P}(\varepsilon\geq i)\sup\_{\bar{r}^{\ell}\_{i}\in\mathbb{R}}\operatorname\*{\mathbb{E}\_{\pi}}\left[r\_{i}-\ell\left(r\_{i}-\bar{r}^{\ell}\_{i}\right)\bigg|\varepsilon\geq i\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑i=1∞γi−1​ℙ​(ε≥i)​supr¯iℓ∈ℝ𝔼π⁡[r¯iℓ+u​(ri−r¯iℓ)|ε≥i]\displaystyle=\sum\_{i=1}^{\infty}\gamma^{i-1}\mathbb{P}(\varepsilon\geq i)\sup\_{\bar{r}^{\ell}\_{i}\in\mathbb{R}}\operatorname\*{\mathbb{E}\_{\pi}}\left[\bar{r}^{\ell}\_{i}+u\left(r\_{i}-\bar{r}^{\ell}\_{i}\right)\bigg|\varepsilon\geq i\right] |  | (2.9) |

where each of suprema can be interpreted as the cash-invariant hull (as defined in Filipović and Kupper, , [2007](https://arxiv.org/html/2602.12030v1#bib.bib11)) of an expected utility computed under a conditional law, offering a link to the literature for good choices of uu and hence of ℓ​(x)=x−u​(x)\ell(x)=x-u(x), as in the below examples.

###### Example 2.8 (Inhomogeneous optimised certainty equivalent).

For an increasing concave uu with u​(0)=0u(0)=0 and u′​(0)=1u^{\prime}(0)=1, each summand becomes an optimised certainty equivalent (OCE) as introduced by Ben-Tal and Teboulle,  ([1986](https://arxiv.org/html/2602.12030v1#bib.bib2)); this was already used in finance for a sequential decision problem at least by the influential Buehler et al.,  ([2019](https://arxiv.org/html/2602.12030v1#bib.bib4)), but computing the OCE on the total return and therefore with a single scalar target, and then optimizing it simultaneously with the policy by direct gradient descent, which needs differentiability of the environment.

###### Example 2.9 (Inhomogeneous monotone mean-volatility).

For uu equal to the monotone hull of quadratic utility (which also fits in the previous example), i.e.

|  |  |  |
| --- | --- | --- |
|  | umβ(x)=min(x,12​β)−βmin(x,12​β)2,u\_{\mathrm{m}}^{\beta}(x)=\min\left(x,\frac{1}{2\beta}\right)-\beta\min\left(x,\frac{1}{2\beta}\right)^{2}, |  |

by trivial generalisation of what Černý,  ([2020](https://arxiv.org/html/2602.12030v1#bib.bib32)) proves with β=1/2\beta=1/2, the cash invariant hull of expected utility which appears in in each term of ([2.9](https://arxiv.org/html/2602.12030v1#S2.E9 "Equation 2.9 ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) has a nice interpretation as the monotone hull of mean-variance, i.e. the minimal correction to mean-variance which ensures that adding a positive random variable does not worsen the measure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supr¯i∈ℝ𝔼π⁡[η+umβ​(X−η)|ε≥i]=supY∈L0+{𝔼π⁡[X−Y|ε≥i]−β​𝕍​arπ​[X−Y|ε≥i]}.\sup\_{\bar{r}\_{i}\in\mathbb{R}}\operatorname\*{\mathbb{E}\_{\pi}}\left[\eta+u\_{\mathrm{m}}^{\beta}\left(X-\eta\right)|\varepsilon\geq i\right]=\sup\_{Y\in L\_{0}^{+}}\left\{\operatorname\*{\mathbb{E}\_{\pi}}[X-Y|\varepsilon\geq i]-\beta\mathbb{V}\mathrm{ar}\_{\pi}[X-Y|\varepsilon\geq i]\right\}. |  | (2.10) |

Note that in our parametrisation, the utility function umβu\_{\mathrm{m}}^{\beta} corresponds to a loss function

|  |  |  |
| --- | --- | --- |
|  | ℓmβ(x)=x−umβ(x)=x−min(x,12​β)+βmin(x,12​β)2={β​x2x≤(2​β)−1x−(4​β)−1x>(2​β)−1\ell\_{\mathrm{m}}^{\beta}(x)=x-u\_{\mathrm{m}}^{\beta}(x)=x-\min\left(x,\frac{1}{2\beta}\right)+\beta\min\left(x,\frac{1}{2\beta}\right)^{2}=\begin{cases}\beta x^{2}&x\leq(2\beta)^{-1}\\ x-(4\beta)^{-1}&x>(2\beta)^{-1}\end{cases} |  |

that switches in a differentiable way from the standard quadratic penalty to a less severe affine penalty when the windfall xx over the target reward exceeds a threshold (2​β)−1(2\beta)^{-1}.

For numerical purposes, the following assumption can be useful.

###### Hypothesis 2.10.

ℓ\ell is a differentiable function with derivative ℓ′\ell^{\prime}, and the suprema in ([2.9](https://arxiv.org/html/2602.12030v1#S2.E9 "Equation 2.9 ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) are attained by a unique maximiser r¯π,iℓ\bar{r}^{\ell}\_{\pi,i} for all i≤ess​sup⁡εi\leq\operatorname\*{ess\,sup}\varepsilon, characterised by the first order condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π⁡[ℓ′​(ri−r¯π,iℓ)|ε≥i]=0\operatorname\*{\mathbb{E}\_{\pi}}[\ell^{\prime}(r\_{i}-\bar{r}^{\ell}\_{\pi,i})|\varepsilon\geq i]=0 |  | (2.11) |

This holds true for most interesting examples, as shown by the following.

###### Proposition 2.11.

Suppose that for all i≤ess​sup⁡εi\leq\operatorname\*{ess\,sup}\varepsilon, there exists some r¯iℓ\bar{r}\_{i}^{\ell} such that 𝔼π⁡[ℓ​(ri−r¯iℓ)|ε≥i]\operatorname\*{\mathbb{E}\_{\pi}}[\ell(r\_{i}-\bar{r}\_{i}^{\ell})|\varepsilon\geq i] is finite. Then [2.10](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem10 "Hypothesis 2.10. ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") holds for:

1. 1.

   The inhomogeneous mean-volatility defined in ([2.3](https://arxiv.org/html/2602.12030v1#S2.E3 "Equation 2.3 ‣ Definition 2.2 (Inhomogeneous mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"));
2. 2.

   The inhomogeneous OCE defined in [Example 2.8](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem8 "Example 2.8 (Inhomogeneous optimised certainty equivalent). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") if u∈C1​(ℝ)u\in C^{1}(\mathbb{R}) is strictly concave;
3. 3.

   The inhomogeneous monotone mean-volatility defined in [Example 2.9](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem9 "Example 2.9 (Inhomogeneous monotone mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning").

###### Proof.

Point 1 is a special case of point 2 for ℓ​(x)=β​x2\ell(x)=\beta x^{2}.

For both points 2 and 3, we start noting that when uu is concave, ℓ\ell is convex, so μi​(r¯iℓ):=𝔼π⁡[ℓ​(ri−r¯iℓ)|ε≥i]\mu\_{i}(\bar{r}\_{i}^{\ell}):=\operatorname\*{\mathbb{E}\_{\pi}}[\ell(r\_{i}-\bar{r}\_{i}^{\ell})|\varepsilon\geq i] also is, and its stationary points are global minimisers. We claim that its derivative is −𝔼π⁡[ℓ′​(ri−r¯iℓ)|ε≥i]-\operatorname\*{\mathbb{E}\_{\pi}}[\ell^{\prime}(r\_{i}-\bar{r}\_{i}^{\ell})|\varepsilon\geq i] at every point inside its domain: indeed, there is an hh such that [r¯iℓ−2​h,r¯iℓ+2​h][\bar{r}\_{i}^{\ell}-2h,\bar{r}\_{i}^{\ell}+2h] is in the domain, which means that for r∈[r¯iℓ−h,r¯iℓ+h]r\in[\bar{r}\_{i}^{\ell}-h,\bar{r}\_{i}^{\ell}+h] the derivative is uniformly bounded below and above by any fixed incremental ratios chosen inside [r¯iℓ−2​h,r¯iℓ−h][\bar{r}\_{i}^{\ell}-2h,\bar{r}\_{i}^{\ell}-h] and [r¯iℓ+h,r¯iℓ+2​h][\bar{r}\_{i}^{\ell}+h,\bar{r}\_{i}^{\ell}+2h] respectively, which are integrable by definition of domain. So stationarity is exactly ([2.11](https://arxiv.org/html/2602.12030v1#S2.E11 "Equation 2.11 ‣ Hypothesis 2.10. ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")).

We now prove that a global minimum or μi\mu\_{i} exists. For this, note that ℓ\ell has a strict global minimum in zero. Then by convexity, ℓ\ell tends to infinity for large negative and positive argument. This easily implies that if μi​(r¯iℓ)<∞\mu\_{i}(\bar{r}\_{i}^{\ell})<\infty, then μi\mu\_{i} is larger than μi​(r¯iℓ)\mu\_{i}(\bar{r}\_{i}^{\ell}) outside a compact interval. By continuity a minimum exists in that compact subset of the domain.

Finally, we prove uniqueness of the minimum. For point 2, this is trivial by strict convexity of μi\mu\_{i}, which is inherited from ℓ\ell. For point 3, the existence of two distinct minima r¯i,r¯i′\bar{r}\_{i},\bar{r}\_{i}^{\prime} would imply that μi\mu\_{i} is linear in the interval, and therefore that ri−r¯ir\_{i}-\bar{r}\_{i} is almost surely inside the interval where ℓmβ\ell\_{\mathrm{m}}^{\beta} is linear: i.e., almost surely greater than (2​β)−1(2\beta)^{-1}. But then r¯i′′=r¯i−(2​β)−1\bar{r}\_{i}^{\prime\prime}=\bar{r}\_{i}-(2\beta)^{-1} would give a strictly smaller penalty almost surely, contradicting minimality of r¯i\bar{r}\_{i}.
∎

### 2.2 Algorithms

One idea to optimise our risk criterion is to note that the optimisation problem can be restated exchanging the order of the suprema:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπsupr¯ℓ∈ℝℕ𝔼π⁡[∑i=1εγi−1​[ri−ℓ​(ri−r¯iℓ)]]=supr¯ℓ∈ℝess​sup⁡εsupπ𝔼π⁡[∑i=1εγi−1​[ri−ℓ​(ri−r¯iℓ)]],\sup\_{\pi}\sup\_{\bar{r}^{\ell}\in\mathbb{R}^{\mathbb{N}}}\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\left[r\_{i}-\ell(r\_{i}-\bar{r}^{\ell}\_{i})\right]\right]=\sup\_{\bar{r}^{\ell}\in\mathbb{R}^{\operatorname\*{ess\,sup}\varepsilon}}\sup\_{\pi}\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=1}^{\varepsilon}\gamma^{i-1}\left[r\_{i}-\ell(r\_{i}-\bar{r}^{\ell}\_{i})\right]\right], |  | (2.12) |

where the inner maximum for fixed r¯ℓ\bar{r}^{\ell} is a plain RL problem with a modified reward function. In simple finite horizon cases, its solution is fast enough to be called at each evaluation of an outer (global) optimisation routine over a finite-dimensional r¯ℓ\bar{r}^{\ell}; note that if the RL algorithm is iterative, then the policy and/or value functions found for the previous candidate r¯ℓ\bar{r}^{\ell} should be a good starting guess for the next candidate r¯ℓ\bar{r}^{\ell} examined by the optimiser.

Alternatively, if all rewards can be implemented as a differentiable function of the actions, one could try direct stochastic gradient descent for ([2.12](https://arxiv.org/html/2602.12030v1#S2.E12 "Equation 2.12 ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) jointly over both a parametrisation of the policy (say the weights of a neural network) and r¯ℓ\bar{r}^{\ell}, which can be seen as a multidimensional generalisation of the idea of Buehler et al.,  ([2019](https://arxiv.org/html/2602.12030v1#bib.bib4)).

Finally, for more complex problems, we can formulate a pathwise estimator of the policy gradient for ςπℓ\varsigma^{\ell}\_{\pi}, allowing a generalisation of the Trust Region Volatility Optimisation (TRVO) algorithm which we will denote by the acronym IVO (Inhomogeneous Volatility Optimisation). To this purpose, assume that [2.10](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem10 "Hypothesis 2.10. ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") holds, and
define the inhomogeneous version of the action-volatility function:

|  |  |  |
| --- | --- | --- |
|  | Xπ,i​(s,a):=𝔼π⁡[∑j=i+1εγj−i−1​ℓ​(rj−r¯π,jℓ)|si=s,ai=a],X\_{\pi,i}(s,a):=\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{j=i+1}^{\varepsilon}\gamma^{j-i-1}\ell(r\_{j}-\bar{r}^{\ell}\_{\pi,j})\,\bigg|\,s\_{i}=s,a\_{i}=a\right], |  |

which is zero if ss is a terminal or post-terminal state. Using the symbol 𝔼π,i{\operatorname\*{\mathbb{E}}}\_{\pi,i} to denote the conditional expectation given the path up to time ii, we can write for it a Bellman-like equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xπ,i​(si,ai)=Iε>i​𝔼π,i[(ri+1−r¯π,i+1)2]+γ​𝔼π,i[Xπ,i+1​(si+1,ai+1)].X\_{\pi,i}(s\_{i},a\_{i})=I\_{\varepsilon>i}{\operatorname\*{\mathbb{E}}}\_{\pi,i}\left[\left(r\_{i+1}-\bar{r}\_{\pi,i+1}\right)^{2}\right]+\gamma{\operatorname\*{\mathbb{E}}}\_{\pi,i}\left[X\_{\pi,i+1}(s\_{i+1},a\_{i+1})\right]. |  | (2.13) |

Then we have the following.

###### Theorem 2.12.

Consider policies that are absolutely continuous with respect to a reference measure π¯\bar{\pi}, such that the density πθ,i(⋅|s)\pi\_{\theta,i}(\cdot|s) at each time step ii depends differentiably on real-valued parameters θ\theta. Assume that ε\varepsilon is almost surely finite and that [2.10](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem10 "Hypothesis 2.10. ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") holds. Then under technical hypotheses (see [Remark 2.13](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem13 "Remark 2.13 (Technical conditions). ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), the gradient of the inhomogeneous reward volatility satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θςπ2=𝔼π⁡[∑i=0ε−1γi​Xπ,i​(si,ai)​∇θlog⁡πθ,i​(ai|si)].\nabla\_{\theta}\varsigma\_{\pi}^{2}=\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=0}^{\varepsilon-1}\gamma^{i}X\_{\pi,i}(s\_{i},a\_{i})\nabla\_{\theta}\log\pi\_{\theta,i}(a\_{i}|s\_{i})\right]. |  | (2.14) |

###### Proof.

We will prove by induction on NN the following equality:222We will follow closely the proof of the analogous claim in [Daluiso et al., 2023a (, Theorem 3.2)](https://arxiv.org/html/2602.12030v1#bib.bib7), which only considers a quadratic penalty, and even for ℓ​(x)=β​x2\ell(x)=\beta x^{2} does not directly apply to our setup, as it is concerned with the time-homogeneous version of the objective function. Hence we provide all details, also for the reader’s convenience and to avoid reliance on the unreviewed extended version of an applied paper.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θςπ2=𝔼π[∑i=0N−1γiXπ,i(si,ai)∇θlogπθ,i(ai|si)−∑i=1N(∇θr¯π,iℓ)Iε≥iγi−1ℓ′(ri−r¯π,iℓ)+γN∇θ𝔼π,N−1[Xπ,N(sN,aN)]].\nabla\_{\theta}\varsigma\_{\pi}^{2}=\operatorname\*{\mathbb{E}\_{\pi}}\left[\sum\_{i=0}^{N-1}\gamma^{i}X\_{\pi,i}(s\_{i},a\_{i})\nabla\_{\theta}\log\pi\_{\theta,i}(a\_{i}|s\_{i})\right.\\ \left.-\sum\_{i=1}^{N}\left(\nabla\_{\theta}\bar{r}\_{\pi,i}^{\ell}\right)I\_{\varepsilon\geq i}\gamma^{i-1}\ell^{\prime}(r\_{i}-\bar{r}\_{\pi,i}^{\ell})+\gamma^{N}\nabla\_{\theta}{\operatorname\*{\mathbb{E}}}\_{\pi,N-1}\left[X\_{\pi,N}(s\_{N},a\_{N})\right]\right]. |  | (2.15) |

Such relation is enough to get the conclusion by letting N→∞N\to\infty, because:

1. 1.

   The first summation converges to ([2.14](https://arxiv.org/html/2602.12030v1#S2.E14 "Equation 2.14 ‣ Theorem 2.12. ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), as Xπ,iX\_{\pi,i} is zero on ε≤i\varepsilon\leq i.
2. 2.

   The second summation has null expected value, as 𝔼π⁡[ℓ′​(ri−r¯π,iℓ)​Iε≥i]=0\operatorname\*{\mathbb{E}\_{\pi}}[\ell^{\prime}(r\_{i}-\bar{r}\_{\pi,i}^{\ell})I\_{\varepsilon\geq i}]=0 by conditioning on ε≥i\varepsilon\geq i followed by application of [2.10](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem10 "Hypothesis 2.10. ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning");
3. 3.

   The third addend is eventually null because it a gradient of an expectation whose integrand is identically null independently of θ\theta on ε<N\varepsilon<N, and ε\varepsilon is a.s. finite.

For the base N=0N=0, the summations disappear and the argument of the outer expected value is the deterministic ∇θ𝔼π[Xπ,0​(s0,a0)]\nabla\_{\theta}{\operatorname\*{\mathbb{E}}}\_{\pi}[X\_{\pi,0}(s\_{0},a\_{0})], where the expected value equals ςπ2\varsigma\_{\pi}^{2} by the definitions and the tower rule.

For the induction step, we analyse the third and residual term of the claim, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θ𝔼π,N−1[Xπ,N​(sN,aN)].\nabla\_{\theta}{\operatorname\*{\mathbb{E}}}\_{\pi,N-1}\left[X\_{\pi,N}(s\_{N},a\_{N})\right]. |  | (2.16) |

We interpret the conditional expected value as a plain expectation over the conditional law of (sN,aN)(s\_{N},a\_{N}). From such a point of view, we see that it depends on θ\theta both distributionally because the conditional law depends on θ\theta, and functionally because for each (sN,aN)(s\_{N},a\_{N}) fixed the integrand is a function of θ\theta via π\pi. Then by elementary probability theory:

1. 1.

   The gradient of the distributional dependence is the expected value 𝔼π,N−1{\operatorname\*{\mathbb{E}}}\_{\pi,N-1} of the integrand times the conditional likelihood ratio weight:

   |  |  |  |
   | --- | --- | --- |
   |  | Xπ,N​(sN,aN)​∇θlog⁡πθ,N​(aN|sN).X\_{\pi,N}(s\_{N},a\_{N})\nabla\_{\theta}\log\pi\_{\theta,N}(a\_{N}|s\_{N}). |  |
2. 2.

   The gradient of the functional dependence is the expected value 𝔼π,N−1{\operatorname\*{\mathbb{E}}}\_{\pi,N-1} of the gradient of the integrand Xπ,NX\_{\pi,N}. We compute it on its Bellman expansion ([2.13](https://arxiv.org/html/2602.12030v1#S2.E13 "Equation 2.13 ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")): the current-step term gives a gradient

   |  |  |  |
   | --- | --- | --- |
   |  | Iε>N​𝔼π,N[−(∇θr¯π,N+1ℓ)​ℓ′​(rN+1−r¯π,N+1ℓ)],I\_{\varepsilon>N}{\operatorname\*{\mathbb{E}}}\_{\pi,N}[-(\nabla\_{\theta}\bar{r}\_{\pi,N+1}^{\ell})\ell^{\prime}(r\_{N+1}-\bar{r}\_{\pi,N+1}^{\ell})], |  |

   while the recursive term gives

   |  |  |  |
   | --- | --- | --- |
   |  | γ​∇θ𝔼π,N[Xπ,N+1​(sN+1,aN+1)].\gamma\nabla\_{\theta}{\operatorname\*{\mathbb{E}}}\_{\pi,N}[X\_{\pi,N+1}(s\_{N+1},a\_{N+1})]. |  |

Now note that in the induction hypothesis, ([2.16](https://arxiv.org/html/2602.12030v1#S2.E16 "Equation 2.16 ‣ Proof. ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) appears within an unconditional expectation 𝔼π\operatorname\*{\mathbb{E}}\_{\pi}, so when substituting points 1. and 2. above into ([2.15](https://arxiv.org/html/2602.12030v1#S2.E15 "Equation 2.15 ‣ Proof. ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), we can remove in both the conditional expectations 𝔼π,N−1{\operatorname\*{\mathbb{E}}}\_{\pi,N-1} by the tower rule. After doing this, 1. gives exactly the new addend in the first summation of the claim; the current-step term in 2. gives the new addend in the second summation of the claim after the removal of 𝔼π,N{\operatorname\*{\mathbb{E}}}\_{\pi,N} by a further application of the tower rule; and the recursive term in 2. gives the new residual exactly as it appears in the claim.
∎

###### Remark 2.13 (Technical conditions).

As in [Daluiso et al., 2023a (, Remark 15)](https://arxiv.org/html/2602.12030v1#bib.bib7), the proof relies on exchanges between expectation and differentiation / limit whose validity can be justified by appeal to standard theorems in concrete settings.

###### Remark 2.14 (Algorithmic implications).

The main difference to the original policy gradient theorem used by TRVO is the need to estimate the target levels r¯π,jℓ\bar{r}^{\ell}\_{\pi,j}. For the inhomogeneous mean-volatility objective, we know that they equal expectations of the reward on scenarios where the episode is still running, and are readily estimated as sample means. For general ℓ\ell, they are defined implicitly as minimisers of conditional expected values, so we can estimate them by numerical minimisation of the empirical counterparts of such expected values.

## 3 Examples

### 3.1 Toy example

In this subsection we define an *ad hoc* environment highlighting the conceptual novelty of the optimality criterion proposed in this paper with respect to the main risk averse formulations in the RL literature.

Specifically, we consider a fixed-horizon problem with ε=2\varepsilon=2 steps and no discounting (γ=1\gamma=1), where both the state space and the action space are given by the set ℝ\mathbb{R} of real numbers. At i=0i=0, the state equals s0=0s\_{0}=0 deterministically. Then action a0a\_{0} determines mean and the variance of a Gaussian random variable according to which the next state is sampled; more precisely, s1∼𝒩​(a0,a02)s\_{1}\sim\mathcal{N}(a\_{0},a\_{0}^{2}). Finally, the state transitions to the deterministic s2=1s\_{2}=1 irrespective of the action a1a\_{1}, and the episode ends. The rewards are computed as state differences, i.e. r1=s1−s0=s1r\_{1}=s\_{1}-s\_{0}=s\_{1} and r2=s2−s1=1−s1r\_{2}=s\_{2}-s\_{1}=1-s\_{1}.

The first remark is that the return is deterministic and independent of the policy:

|  |  |  |
| --- | --- | --- |
|  | 𝒢=s1+(1−s1)=1.\mathcal{G}=s\_{1}+(1-s\_{1})=1. |  |

As a consequence, any policy is equally good not only according to the classical RL goal, but also for the mean-variance criterion and for all risk averse goals defined by a risk measure applied to 𝒢\mathcal{G}.

Time-consistent dynamic risk measures as proposed by Coache and Jaimungal,  ([2023](https://arxiv.org/html/2602.12030v1#bib.bib6)) do not express any preference between policies either, because the objective function in such case is

|  |  |  |
| --- | --- | --- |
|  | ρ0,2=ρ0​(r1+ρ1​(r2))\rho\_{0,2}=\rho\_{0}(r\_{1}+\rho\_{1}(r\_{2})) |  |

where ρ0\rho\_{0} and ρ1\rho\_{1} are risk measures: indeed, for our environment one can write

|  |  |  |
| --- | --- | --- |
|  | ρ0,2=ρ0​(s1+ρ1​(1−s1))=ρ0​(s1+(1−s1))=ρ0​(1)=1,\rho\_{0,2}=\rho\_{0}(s\_{1}+\rho\_{1}(1-s\_{1}))=\rho\_{0}(s\_{1}+(1-s\_{1}))=\rho\_{0}(1)=1, |  |

where we used that ρi​(Zi)\rho\_{i}(Z\_{i}) is equal to ZiZ\_{i} for any random variable known at step ii.

On the other hand, as the expected return does not depend on the policy, homogeneous mean-volatility would minimise the unnormalised reward volatility for any positive risk aversion coefficient, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν^π2\displaystyle\hat{\nu}^{2}\_{\pi} | =𝔼π⁡[(s1−Jπ)2+(1−s1−Jπ)2]=𝔼π⁡[(s1−1/2)2+(1−s1−1/2)2]\displaystyle=\operatorname\*{\mathbb{E}\_{\pi}}\left[\left(s\_{1}-J\_{\pi}\right)^{2}+\left(1-s\_{1}-J\_{\pi}\right)^{2}\right]=\operatorname\*{\mathbb{E}\_{\pi}}\left[\left(s\_{1}-1/2\right)^{2}+\left(1-s\_{1}-1/2\right)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​𝔼π⁡[(s1−1/2)2]=2​𝔼π⁡[(s1−a0)2]+2​(a0−1/2)2=2​a02+2​(a0−1/2)2,\displaystyle=2\operatorname\*{\mathbb{E}\_{\pi}}\left[\left(s\_{1}-1/2\right)^{2}\right]=2\operatorname\*{\mathbb{E}\_{\pi}}\left[\left(s\_{1}-a\_{0}\right)^{2}\right]+2\left(a\_{0}-1/2\right)^{2}=2a\_{0}^{2}+2\left(a\_{0}-1/2\right)^{2}, |  |

whose minimiser is a0=1/4a\_{0}=1/4. This represents a trade-off between the value a0=0a\_{0}=0 zeroing the variance of the only source of uncertainty in the environment which is the Gaussian draw s1∼𝒩​(a0,a02)s\_{1}\sim\mathcal{N}(a\_{0},a\_{0}^{2}), and the value a0=1/2a\_{0}=1/2 splitting the total return 𝒢=1\mathcal{G}=1 homogeneously into two rewards with equal expectation.

Finally, our inhomogeneous mean-volatility objective also reduces to minimisation of the risk criterion, as the expected return is 1 regardless of π\pi. However, in this case we have no homogeneity preference, so we are free to concentrate on probabilistic risk:

|  |  |  |
| --- | --- | --- |
|  | ςπ2=𝕍​arπ​(s1)+𝕍​arπ​(1−s1)=2​a02\varsigma^{2}\_{\pi}=\mathbb{V}\mathrm{ar}\_{\pi}(s\_{1})+\mathbb{V}\mathrm{ar}\_{\pi}(1-s\_{1})=2a\_{0}^{2} |  |

is obviously minimised by a0=0a\_{0}=0.

### 3.2 Deterministic-horizon example: optimal execution

In this subsection, we consider the common problem of an operator which needs to execute a large order on an illiquid asset, i.e., one for which the price that can be agreed for a trade worsens significantly depending on the traded size. For such assets, it is at very least too costly, if not impossible, to complete a sizeable trade without slicing it into smaller ones to be digested by the market over a long period of time. As such slicing incurs the risk of market moves during the non negligible execution time, in this situation the trader must strike a balance between acting faster with a higher negative impact on prices, and accepting higher uncertainty in the total cash-flow.

Specifically, we denote by NtN\_{t} the number of units of asset in the portfolio, and by CtC\_{t} the cash account of the trader, who starts with an exogenous initial position N0N\_{0} and must ensure that NT=0N\_{T}=0 at a certain horizon TT. To the purpose, at each of a discrete set of times ti>0t\_{i}>0, they can add ntin\_{t\_{i}} (signed) units of asset registering a cash-flow of −nti​Pti​(nti)-n\_{t\_{i}}P\_{t\_{i}}(n\_{t\_{i}}) units of currency, where the execution price PP depends on the traded size nn. Therefore, by a generic time tt the portfolio will contain

|  |  |  |
| --- | --- | --- |
|  | Nt=N0+∑0≤ti<tntiN\_{t}=N\_{0}+\sum\_{0\leq t\_{i}<t}n\_{t\_{i}} |  |

units of the asset, while the cash account will be

|  |  |  |
| --- | --- | --- |
|  | Ct=C0−∑0≤ti<tnti​Pti​(nti).C\_{t}=C\_{0}-\sum\_{0\leq t\_{i}<t}n\_{t\_{i}}P\_{t\_{i}}(n\_{t\_{i}}). |  |

As typical in practice, we suppose that the trader computes a mark-to-market of his position using a reference price XtX\_{t} (often this is the mid price):

|  |  |  |
| --- | --- | --- |
|  | Vt=Nti​Xt+Ct,V\_{t}=N\_{t\_{i}}X\_{t}+C\_{t}, |  |

and cares about the profit and loss on each period (ti−1,ti](t\_{i-1},t\_{i}], so that the right reward to describe his objective in reinforcement learning terms is

|  |  |  |
| --- | --- | --- |
|  | Rti=Vti−Vti−1.R\_{t\_{i}}=V\_{t\_{i}}-V\_{t\_{i-1}}. |  |

To be concrete and to have a benchmark, we use the simplest and most famous model for price evolution in an optimal execution context, namely that proposed in the seminal paper Almgren and Chriss,  ([2000](https://arxiv.org/html/2602.12030v1#bib.bib1)), although our reinforcement learning approach is obviously applicable to any dynamics. In particular, we suppose that the mid price XtX\_{t} is additively decomposed as the sum of an unaffected price StS\_{t} and a correction ItI\_{t} depending on past trade sizes ntin\_{t\_{i}}:

|  |  |  |
| --- | --- | --- |
|  | Xt=St+It,X\_{t}=S\_{t}+I\_{t}, |  |

where St=S0+σ​WtS\_{t}=S\_{0}+\sigma W\_{t} is an arithmetic Brownian motion, while It=∑ti≤tg⋅ntiI\_{t}=\sum\_{t\_{i}\leq t}g\cdot n\_{t\_{i}} is a linear permanent impact term. We also follow the classical assumption that actual execution prices are worse than the reference price computed before the permanent impact by an amount which grows linearly with trade size:

|  |  |  |
| --- | --- | --- |
|  | Pti=Xti+sign​(nti)​(ϵ+η​|nti|).P\_{t\_{i}}=X\_{t\_{i}}+\mathrm{sign}(n\_{t\_{i}})(\epsilon+\eta|n\_{t\_{i}}|). |  |

Numerically, we take the very same parameters as in section 3.4 of the original paper, i.e. we put: S0=50​$S\_{0}=50\ \mathdollar, σ=0.95​$​day−1/2\sigma=0.95\ \mathdollar\ \mathrm{day}^{-1/2}, g=2.5×10−7​$g=$2.5\text{\times}{10}^{-7}$\ \mathdollar, ϵ=1/16​$\epsilon=1/16\ \mathdollar, η=2.5×10−6​$\eta=$2.5\text{\times}{10}^{-6}$\ \mathdollar, with its toy low frequency Δ​t=1​day\Delta t=1\ \mathrm{day} and long horizon T=5​dayT=5\ \mathrm{day} to liquidate N0=​106N\_{0}=${10}^{6}$ shares. As for risk aversion coefficients, they will be also varied in a similar range as theirs, even though they do not have the exact same meaning because of the different risk measure; this is because we expect similar coefficients between the two approaches to lead to similar behaviour, since our reward volatility is a discrete-time analog to quadratic variation of VtV\_{t}, and in the continuous limit the Almgren and Chriss,  ([2000](https://arxiv.org/html/2602.12030v1#bib.bib1)) strategy solves the mean-quadratic variation problem, as proved in Forsyth et al.,  ([2012](https://arxiv.org/html/2602.12030v1#bib.bib12)).

Finally, we implement both the TRVO algorithm and the new IVO algorithm to optimise respectively the homogeneous and inhomogeneous mean-volatility, with a state consisting of the normalised time t/Tt/T, the current stock price StS\_{t}, and the current allocation NtN\_{t}, although we conjecture a weak dependence of the optimal policy on the random StS\_{t}, as the optimiser of the classical Almgren-Chriss model is in fact a deterministic function of time only. Indeed, the optimised amounts turn out to be almost the same on all test paths. For this reason, we can simply analyse the residual inventory as a function of time on a representative test path for both algorithms.

The results of TRVO in [Fig. 1](https://arxiv.org/html/2602.12030v1#S3.F1 "In 3.2 Deterministic-horizon example: optimal execution ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") show a clear misbehaviour of homogeneous mean-volatility for this problem: immediate liquidation is never seen as the best policy, even for very high risk aversions. This is because it concentrates PnL in the first step, increasing heterogeneity of rewards and hence path volatility. This signals that this older objective function is not an adequate description of the trader’s goals in this context.

This is fixed by homogeneous mean-volatility, as can be seen in [Fig. 2](https://arxiv.org/html/2602.12030v1#S3.F2 "In 3.2 Deterministic-horizon example: optimal execution ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"). Now we get a more diverse family of execution policies, where the time profile of residual inventory is more and more convex as risk aversion increases: in particular, it ranges from a linear shape for the risk-neutral trader, who splits the trade evenly across timesteps, to full execution in one step for the extremely risk averse trader. This is exactly the qualitative behaviour which makes the solutions in Almgren and Chriss,  ([2000](https://arxiv.org/html/2602.12030v1#bib.bib1)) financially sound.

0112233445500.20.20.40.40.60.60.80.811fraction of shares leftβ=10−1\beta=10^{-1}β=10−5\beta=10^{-5}β=10−6\beta=10^{-6}β=10−7\beta=10^{-7}


Figure 1: Optimal execution paths for different risk aversion coefficients in the (homogeneous) mean-volatility objective, obtained by the TRVO algorithm.

0112233445500.20.20.40.40.60.60.80.811fraction of shares leftβ=10−1\beta=10^{-1}β=10−5\beta=10^{-5}β=10−6\beta=10^{-6}β=10−7\beta=10^{-7}


Figure 2: Optimal execution paths for different risk aversion coefficients in the inhomogeneous mean-volatility objective, obtained by the IVO algorithm.

### 3.3 Stochastic-horizon example: grid world

In this subsection, we test our objective function on an environment used in non financial reinforcement learning literature to test risk averse algorithms. This will show some non intuitive behaviour of our optimal policies when the number of timesteps per episode is stochastic.

The set of states consists of a finite rectangular grid. At each of a finite number of timesteps, the agent chooses a direction: north, south, east, west, or a diagonal direction, for a total of eight possible actions. Noise is introduced by stating that the agent moves in the selected direction only with some probability lower than 100%, while with some residual probability a random action is executed. In both cases, if the selected or drawn action would take the agent out of the grid, the state is unaffected for the time step under consideration. The agent collects a constant small negative reward at each timestep, unless it lands on special terminal states where the episode ends; all of them carry a large negative reward except for one which can be interpreted as a goal state, where it is large and positive. We take the problem instance from Moldovan and Abbeel,  ([2012](https://arxiv.org/html/2602.12030v1#bib.bib20)), where the grid is that of [Fig. 3](https://arxiv.org/html/2602.12030v1#S3.F3 "In 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") with -1 reward on non terminal steps, +35 reward on the terminal green cell, and -35 reward on the terminal red cells; the maximum episode length is 35 steps, the probability that a random action is picked instead of that chosen by the agent is 8%, and the discount factor γ\gamma equals 1.

![Refer to caption](grid.png)


Figure 3: Grid-world instance used in [Section 3.3](https://arxiv.org/html/2602.12030v1#S3.SS3 "3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"), taken from Moldovan and Abbeel,  ([2012](https://arxiv.org/html/2602.12030v1#bib.bib20)). Each episode starts from the cell marked by x and ends when the green cell is reached with reward +35, or a red cell is reached with reward -35. On every other timestep the reward is -1, for a maximum of 35 time steps.

The intuition would be that a risk-neutral agent should take the shortest path to reach the green cell, to pay the -1 cost for as few steps as possible; while a risk averse agent should pay for longer routes to keep far from the red cells, thus reducing the probability of getting their low reward due to noise. Let us see to what extent this is confirmed under some specification of our objective function.

In particular, in the following subsections we optimise mean-ℓ\ell-volatility with different choices of ℓ\ell, each time for a grid of values of the risk aversion coefficient; unless otherwise stated, this is done by the nested approach in ([2.12](https://arxiv.org/html/2602.12030v1#S2.E12 "Equation 2.12 ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), with the inner classical reinforcement learning problem solved exactly by tabular value iteration. Then to get an intuition on the optimised policies, we present graphically their most likely episode, i.e. the path which is followed by the agent when noise does not disturb the action at any timestep.

#### 3.3.1 Inhomogeneous mean-volatility

We begin with the simplest version of our objective function, defined in [Definition 2.2](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem2 "Definition 2.2 (Inhomogeneous mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"). The solutions we obtain for several risk aversion coefficients are in [Fig. 4](https://arxiv.org/html/2602.12030v1#S3.F4 "In 3.3.1 Inhomogeneous mean-volatility ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning").

![Refer to caption](meanvar.png)


Figure 4: Path generated in a noiseless test environment by optimal policies for inhomogeneous mean-volatility ([2.3](https://arxiv.org/html/2602.12030v1#S2.E3 "Equation 2.3 ‣ Definition 2.2 (Inhomogeneous mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), for a selection of values of the risk aversion β\beta.

Their shape for low risk aversions is as expected: when the agent is almost risk neutral, it is optimal to take the shortest path possible. Note that the passage through cell (3,3) is strictly better than a geometrically shorter alternative path through cell (2,3), as the two paths have in fact the same length in terms of number of steps, and the former has lower probability to end in the obstacles by chance.

The shape for high risk aversion, while counter-intuitive at first sight, is also reasonable, and perhaps even more coherent than the path typically produced by other approaches, who still reach the goal cell although with a long detour. Indeed, sufficiently risk averse agents should privilege keeping as far as possible from the red squares over reaching the green one, to the point that they should aim at wandering close to the edges of the grid for the full 35 steps; but then they would get a total reward of -35 very often, and an even worse one in some unlucky episodes where noise interferes. So they are better off getting the full -35 straight away and end the episode by trying to dive into the obstacle immediately, as our agents do.

A less satisfactory behaviour is obtained for intermediate risk aversions. Indeed, the agents still take the quite risky decision of going though the narrow corridor, and the only difference from the risk neutral path is that at the fourth step of the no-noise episode, instead of choosing the action that would immediately lead to the goal state, they make a couple of waiting moves to get the +35 reward slightly later. One of the reasons for this is probably that it is suboptimal to assign a high target r¯π,4\bar{r}\_{\pi,4} to the fourth reward, as there is a non negligible number of episodes which will get delayed by noise in at least one of the first four steps, and which would contribute a strong risk penalisation. But once r¯π,4\bar{r}\_{\pi,4} is set to a low value, due to volatility equally penalizing positive and negative deviations from it, the agents will be incentivised to *not* get the +35 at the fourth step even when they could as in the depicted no-noise scenario: once close enough to the goal, they will rather pay a small -1 penalty for a couple more times, and then get the +35 at the sixth step, where it is safe enough to set a high target r¯π,6\bar{r}\_{\pi,6}, because the green cell can be reached with high probability in six moves even on scenarios where noise interferes.

#### 3.3.2 Inhomogeneous monotone mean-volatility

Although the above reasoning might give a satisfactory intuitive motivation for the diamond-shaped endings in [Fig. 4](https://arxiv.org/html/2602.12030v1#S3.F4 "In 3.3.1 Inhomogeneous mean-volatility ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"), from a human perspective they do not look very rational, so we try to change the objective function. In particular, since we partially blamed the well known flaw according to which mean-variance sometimes prefers to avoid an uncertain significant increase in reward, we try the minimal fix to this incoherence, which was defined in [Example 2.9](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem9 "Example 2.9 (Inhomogeneous monotone mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"). The distinct types of path we get on no-noise scenarios with optimal policies corresponding to varied risk aversions are in [Fig. 5](https://arxiv.org/html/2602.12030v1#S3.F5 "In 3.3.2 Inhomogeneous monotone mean-volatility ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning").

![Refer to caption](monotone.png)


Figure 5: Path generated in a noiseless test environment by optimal policies for inhomogeneous monotone mean-volatility ([Example 2.9](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem9 "Example 2.9 (Inhomogeneous monotone mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), for a selection of values of the risk aversion β\beta.

We can see that the good limiting cases for large and small risk aversions are retained. We also get a slightly more diverse set of optimal paths, in that for some large but not extreme risk aversions, a longer and safer path still reaching the goal state appears. But unfortunately, the main objections raised in [Section 3.3.1](https://arxiv.org/html/2602.12030v1#S3.SS3.SSS1 "3.3.1 Inhomogeneous mean-volatility ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning") carry over: indeed, for moderately small risk aversions, the path makes two unnecessary vertical steps before terminating, while for moderately high risk aversions, the path takes a horizontal round-trip before terminating. Therefore, removing disincentives to large rewards from earlier steps is not enough. Maybe in view of ([2.10](https://arxiv.org/html/2602.12030v1#S2.E10 "Equation 2.10 ‣ Example 2.9 (Inhomogeneous monotone mean-volatility). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), whose interpretation is that monotone mean-variance is the mean-variance one could get having the opportunity to disregard part of the outcome, it is still better for the agent to attain the large target later but in more scenarios, rather than earlier when he must ignore part of it.

#### 3.3.3 Inhomogeneous optimised certainty equivalent

A final attempt to incentivise higher returns at all steps would be to take a strictly monotone utility in the construction in [Example 2.8](https://arxiv.org/html/2602.12030v1#S2.Thmtheorem8 "Example 2.8 (Inhomogeneous optimised certainty equivalent). ‣ 2.1 Definitions and properties ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"). Results for exponential utility, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓβ​(x)=x−1−exp⁡(−β​x)β,{\ell}\_{\beta}(x)=x-\frac{1-\exp(-\beta x)}{\beta}, |  | (3.1) |

are presented in [Fig. 6](https://arxiv.org/html/2602.12030v1#S3.F6 "In 3.3.3 Inhomogeneous optimised certainty equivalent ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning").

![Refer to caption](exponential.png)


Figure 6: Path generated in a noiseless test environment by optimal policies for inhomogeneous mean-ℓ\ell-volatility with ℓ\ell defined by ([3.1](https://arxiv.org/html/2602.12030v1#S3.E1 "Equation 3.1 ‣ 3.3.3 Inhomogeneous optimised certainty equivalent ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")), for a selection of values of β\beta.

The set of paths is even richer than in [Section 3.3.2](https://arxiv.org/html/2602.12030v1#S3.SS3.SSS2 "3.3.2 Inhomogeneous monotone mean-volatility ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"), and the round-trips disappear; but sadly enough, the second graph from the left still features the unnecessary upward steps we noticed in [Fig. 5](https://arxiv.org/html/2602.12030v1#S3.F5 "In 3.3.2 Inhomogeneous monotone mean-volatility ‣ 3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning").

#### 3.3.4 Dynamic monotone hull and IVO

In all the tests of [Section 3.3](https://arxiv.org/html/2602.12030v1#S3.SS3 "3.3 Stochastic-horizon example: grid world ‣ 3 Examples ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning"), the only debatable behaviours seem caused by some form of non monotonicity: the agent prefers a path which is identical except for two additional negatively-rewarded steps. For risk-measures ρ\rho in a non dynamic context, we already mentioned that a known fix is the monotone hull, which allows *throwing away* part of the *return* 𝒢\mathcal{G}:

|  |  |  |
| --- | --- | --- |
|  | sup𝒴∈L0+ρ​(𝒢−𝒴).\sup\_{\mathcal{Y}\in L\_{0}^{+}}\rho(\mathcal{G}-\mathcal{Y}). |  |

This might suggest a generalisation for our setting in which the risk 𝝆{\bm{\rho}} depends on the *sequence* of the rewards rir\_{i}: perhaps instead of simply giving up the reward, in a sequential decision setting we should
allow *reserving* part of it for later steps, by optimizing

|  |  |  |
| --- | --- | --- |
|  | supY0=0,Yi∈L0+​(ℱi)​∀i>0𝝆​((ri−Yi+Yi−1)i≥1).\sup\_{Y\_{0}=0,Y\_{i}\in L\_{0}^{+}(\mathcal{F}\_{i})\ \forall i>0}{\bm{\rho}}\left((r\_{i}-Y\_{i}+Y\_{i-1})\_{i\geq 1}\right). |  |

In principle, this could be implemented by just adding the real-valued reserve YiY\_{i} to the control variables at time step ii. However, with such addition, the exact solution of the inner problem becomes numerically infeasible, and one must give up the nested optimisation approach based on ([2.12](https://arxiv.org/html/2602.12030v1#S2.E12 "Equation 2.12 ‣ 2.2 Algorithms ‣ 2 Theory ‣ Time-inhomogeneous volatility aversion for financial applications of reinforcement learning")) in favour of IVO. But then, as a reinforcement learning algorithm based on function approximation (in our implementation, by feed-forward neural networks), IVO has difficulties in finding the odd slight improvements around the target state which we disliked in the above subsections. Therefore, the only tool we currently have to solve the problem with a reserve, fails to reproduce the glitches we know of even when applied without it. Hence, as of now we cannot numerically verify the conjecture that they would be fixed.

On the other hand, one can also argue more pragmatically that for this very reason, gradient based solvers may be practically effective in automatically giving reasonable solutions that smooth the edges of pathological minima even without complicating the space of actions.

## 4 Conclusion

In this work, we have tried to define a risk averse objective function such that:

1. 1.

   Modern reinforcement learning algorithms can be leveraged without excessive overhead;
2. 2.

   The time distribution of rewards matters, unlike most proposals which define risk on the total return;
3. 3.

   Homogeneous time splits are not favoured, unlike mean-volatility which was satisfactory for hedging.

We have proven that a time-inhomogeneous variant of mean-volatility has all the above properties, and that it can also be generalised using as building block loss functions which are better behaved than mean-variance, including monotone mean-variance and optimised certainty equivalents.

Empirically, we have seen that the proposed approach works well in the financially relevant problem of optimal execution, and we believe that the same would hold for any problem where reward timing is well predictable given the policy. On the other hand, we have observed slightly counter-intuitive optimal policies in a non financial test problem where there may be unexpected or anticipated large windfalls. While this should be quite uncommon in finance, modifications tackling these effects could be the subject of future research.

## Disclaimer

The authors report no potential competing interests. The opinions expressed in this document are solely those of the authors and do not represent in any way those of their present and past employers.

## References

* Almgren and Chriss, (2000)

  Almgren, R. and Chriss, N. (2000).
  Optimal execution of portfolio transactions.
  Journal of Risk, 3(2):5–39.
* Ben-Tal and Teboulle, (1986)

  Ben-Tal, A. and Teboulle, M. (1986).
  Expected utility, penalty functions, and duality in stochastic
  nonlinear programming.
  Management Science, 32(11):1445–1466.
  Publisher: INFORMS.
* Bisi et al., (2020)

  Bisi, L., Sabbioni, L., Vittori, E., Papini, M., and Restelli, M. (2020).
  Risk-averse trust region optimization for reward-volatility
  reduction.
  In Proceedings of the Twenty-Ninth International Joint
  Conference on Artificial Intelligence, IJCAI-20, pages 4583–4589.
* Buehler et al., (2019)

  Buehler, H., Gonon, L., Teichmann, J., and Wood, B. (2019).
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291.
* Chow et al., (2017)

  Chow, Y., Ghavamzadeh, M., Janson, L., and Pavone, M. (2017).
  Risk-constrained reinforcement learning with percentile risk
  criteria.
  Journal of Machine Learning Research, 18(1):6070––6120.
* Coache and Jaimungal, (2023)

  Coache, A. and Jaimungal, S. (2023).
  Reinforcement learning with dynamic convex risk measures.
  Mathematical Finance, pages 1–31.
* (7)

  Daluiso, R., Pinciroli, M., Trapletti, M., and Vittori, E. (2023a).
  CVA hedging by risk-averse stochastic-horizon reinforcement
  learning.
  arXiv preprint arXiv:2312.14044.
* (8)

  Daluiso, R., Pinciroli, M., Trapletti, M., and Vittori, E. (2023b).
  CVA hedging with reinforcement learning.
  In ICAIF ’23: Proceedings of the 4th ACM International
  Conference on AI in Finance, New York, NY, USA. Association for Computing
  Machinery.
* Di Castro et al., (2012)

  Di Castro, D., Tamar, A., and Mannor, S. (2012).
  Policy gradients with variance related risk criteria.
  In ICML ’12: Proceedings of the 29th International Conference
  on Machine Learning, volume 1.
* Du et al., (2020)

  Du, J., Jin, M., Kolm, P. N., Ritter, G., Wang, Y., and Zhang, B. (2020).
  Deep reinforcement learning for option replication and hedging.
  Journal of Financial Data Science, 2(4):44–57.
* Filipović and Kupper, (2007)

  Filipović, D. and Kupper, M. (2007).
  Monotone and cash-invariant convex functions and hulls.
  Insurance: Mathematics and Economics, 41(1):1–16.
* Forsyth et al., (2012)

  Forsyth, P. A., Kennedy, J. S., Tse, S. T., and Windcliff, H. (2012).
  Optimal trade execution: A mean quadratic variation approach.
  Journal of Economic Dynamics and Control, 36(12):1971–1991.
* García and Fernández, (2015)

  García, J. and Fernández, F. (2015).
  A comprehensive survey on safe reinforcement learning.
  Journal of Machine Learning Research, 16:1437–1480.
* Halperin, (2019)

  Halperin, I. (2019).
  The QLBS Q-learner goes NuQLear: Fitted Q iteration,
  inverse RL, and option portfolios.
  Quantitative Finance, 19(9):1543–1553.
* Halperin, (2020)

  Halperin, I. (2020).
  QLBS: Q-learner in the Black-Scholes(-Merton) worlds.
  The Journal of Derivatives, 28(1):99–122.
* Han et al., (2025)

  Han, S., Liu, Y., and Yu, X. (2025).
  Risk-sensitive reinforcement learning based on convex scoring
  functions.
  arXiv preprint arXiv:2505.04553.
* Kolm and Ritter, (2019)

  Kolm, P. N. and Ritter, G. (2019).
  Dynamic replication and hedging: A reinforcement learning approach.
  Journal of Financial Data Science, 1(1):159–171.
* Mandelli et al., (2023)

  Mandelli, F., Pinciroli, M., Trapletti, M., and Vittori, E. (2023).
  Reinforcement learning for credit index option hedging.
  arXiv preprint arXiv:2307.09844.
* Marzban et al., (2023)

  Marzban, S., Delage, E., and Li, J. Y.-M. (2023).
  Deep reinforcement learning for option pricing and hedging under
  dynamic expectile risk measures.
  Quantitative Finance, 23(10):1411–1430.
* Moldovan and Abbeel, (2012)

  Moldovan, T. M. and Abbeel, P. (2012).
  Risk aversion in Markov decision processes via near optimal
  Chernoff bounds.
  In Advances in Neural Information Processing Systems, pages
  3131–3139.
* Moody and Saffell, (2001)

  Moody, J. and Saffell, M. (2001).
  Learning to trade via direct reinforcement.
  IEEE Transactions on Neural Networks, 12(4):875–889.
* Moos et al., (2022)

  Moos, J., Hansel, K., Abdulsamad, H., Stark, S., Clever, D., and Peters, J.
  (2022).
  Robust reinforcement learning: A review of foundations and recent
  advances.
  Machine Learning and Knowledge Extraction, 4(1):276–315.
* Morimura et al., (2010)

  Morimura, T., Sugiyama, M., Kashima, H., Hachiya, H., and Tanaka, T. (2010).
  Nonparametric return distribution approximation for reinforcement
  learning.
  In ICML ’10: Proceedings of the 27th International Conference
  on Machine Learning, pages 799–806.
* Mueller et al., (2024)

  Mueller, K., Akkari, A., Gonon, L., and Wood, B. (2024).
  Fast deep hedging with second-order optimization.
  In ICAIF ’24: Proceedings of the 5th ACM International
  Conference on AI in Finance, ICAIF ’24, pages 319–327, New York, NY,
  USA. Association for Computing Machinery.
* Neagu et al., (2025)

  Neagu, A., Godin, F., and Kosseim, L. (2025).
  Deep reinforcement learning algorithms for option hedging.
  arXiv preprint arXiv:2504.05521.
* Prashanth and Ghavamzadeh, (2014)

  Prashanth, L. A. and Ghavamzadeh, M. (2014).
  Actor-critic algorithms for risk-sensitive reinforcement learning.
  arXiv preprint arXiv:1403.6530.
* Shen et al., (2014)

  Shen, Y., Huang, R., Yan, C., and Obermayer, K. (2014).
  Risk-averse reinforcement learning for algorithmic trading.
  In 2014 IEEE Conference on Computational Intelligence for
  Financial Engineering & Economics (CIFEr), pages 391–398. IEEE.
* Tamar et al., (2015)

  Tamar, A., Chow, Y., Ghavamzadeh, M., and Mannor, S. (2015).
  Policy gradient for coherent risk measures.
  In Advances in Neural Information Processing Systems, pages
  1468–1476.
* Tamar et al., (2017)

  Tamar, A., Chow, Y., Ghavamzadeh, M., and Mannor, S. (2017).
  Sequential decision making with coherent risk.
  IEEE Transactions on Automatic Control, 62(7):3323–3338.
* Tamar and Mannor, (2013)

  Tamar, A. and Mannor, S. (2013).
  Variance adjusted actor critic algorithms.
  arXiv preprint arXiv:1310.3697.
* Vittori et al., (2020)

  Vittori, E., Trapletti, M., and Restelli, M. (2020).
  Option hedging with risk averse reinforcement learning.
  In ICAIF ’20: Proceedings of the 1st ACM International
  Conference on AI in Finance, pages 1–8.
* Černý, (2020)

  Černý, A. (2020).
  Semimartingale theory of monotone mean–variance portfolio
  allocation.
  Mathematical Finance, 30(3):1168–1178.