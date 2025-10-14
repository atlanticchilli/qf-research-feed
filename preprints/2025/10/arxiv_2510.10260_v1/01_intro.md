---
authors:
- Junyan Ye
- Hoi Ying Wong
- Kyunghyun Park
doc_id: arxiv:2510.10260v1
family_id: arxiv:2510.10260
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted
  to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from
  the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges
  the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).'
url_abs: http://arxiv.org/abs/2510.10260v1
url_html: https://arxiv.org/html/2510.10260v1
venue: arXiv q-fin
version: 1
year: 2025
---


Junyan Ye
Department of Statistics and Data Science, The Chinese University of Hong Kong, Shatin, N.T., Hong Kong
(, ).
  
Hoi Ying Wong33footnotemark: 3
  
Kyunghyun Park
Division of Mathematical Sciences,
Nanyang Technological University, Singapore
().

###### Abstract

We propose and analyze a continuous-time robust reinforcement learning framework for optimal stopping problems under ambiguity. In this framework, an agent chooses a stopping rule motivated by two objectives: robust decision-making under ambiguity and learning about the unknown environment.
Here, ambiguity refers to considering multiple probability measures dominated by a reference measure, reflecting the agent’s awareness that the reference measure representing her learned belief about the environment would be erroneous.
Using the gg-expectation framework, we reformulate an optimal stopping problem under ambiguity as an entropy-regularized optimal control problem under ambiguity, with Bernoulli distributed controls to incorporate exploration into the stopping rules. We then derive the optimal Bernoulli distributed control characterized by backward stochastic differential equations. Moreover, we establish a policy iteration theorem and implement it as a reinforcement learning algorithm. Numerical experiments demonstrate the convergence and robustness of the proposed algorithm across different levels of ambiguity and exploration.

###### keywords:

optimal stopping, ambiguity, robust optimization, gg-expectation, reinforcement learning, policy iteration.

{MSCcodes}

60G40, 60H10, 68T07, 49L20

## 1 Introduction

Optimal stopping is a class of decision problems in which one seeks to choose a time to take a certain action so as to maximize an expected reward. It is applied in various fields, for instance to analyze the optimality of the sequential probability ratio test in statistics (e.g., [[65](https://arxiv.org/html/2510.10260v1#bib.bib65)]), to study consumption habits in economics (e.g., [[18](https://arxiv.org/html/2510.10260v1#bib.bib18)]), and notably to derive American option pricing (e.g., [[55](https://arxiv.org/html/2510.10260v1#bib.bib55)]). A common challenge arising in all these fields is finding the best model to describe the underlying process or probability measure, which is usually unknown. Although significant efforts have been made to propose and analyze general stochastic models with improved estimation techniques, a margin of error in estimation inherently exists.

In response to such model misspecification and estimation errors, recent works, Dai et al. [[15](https://arxiv.org/html/2510.10260v1#bib.bib15)] and Dong [[17](https://arxiv.org/html/2510.10260v1#bib.bib17)], have cast optimal stopping problems within the continuous time reinforcement learning (RL) framework of Wang et al. [[66](https://arxiv.org/html/2510.10260v1#bib.bib66)] and Wang and Zhou [[67](https://arxiv.org/html/2510.10260v1#bib.bib67)]. Arguably, the exploratory (or randomized) optimal stopping framework is viewed as model-free, since agents, even without knowledge of the true model or underlying dynamics of the environment, can learn from observed data and determine a stopping rule that yields the best outcome. In this sense, the framework provides a systematic way to balance exploration and exploitation in optimal stopping.

However, the model-free view of the exploratory RL framework has a pitfall: the learning environment reflected in observed data often differs from the actual deployment environment (e.g., due to distributional or domain shifts). Consequently, a stopping rule derived from the learning process may fail in practice. Indeed, Chen and Epstein [[11](https://arxiv.org/html/2510.10260v1#bib.bib11)] explicitly ask: “Would ambiguity not disappear eventually as the agent learns about her environment?” In response, Epstein and Schneider [[22](https://arxiv.org/html/2510.10260v1#bib.bib22)] and Marinacci [[42](https://arxiv.org/html/2510.10260v1#bib.bib42)] stress that the link between empirical frequencies (i.e., observed data) and asymptotic beliefs (updated through learning) can be weakened by the degree of ambiguity in the agent’s prior beliefs about the environment. This suggests that ambiguity can persist even with extensive learning, limiting the reliability of a purely model-free framework. Such limitations have been recognized in the RL literature, leading to significant developments in robust RL frameworks such as [[9](https://arxiv.org/html/2510.10260v1#bib.bib9), [45](https://arxiv.org/html/2510.10260v1#bib.bib45), [48](https://arxiv.org/html/2510.10260v1#bib.bib48), [59](https://arxiv.org/html/2510.10260v1#bib.bib59), [69](https://arxiv.org/html/2510.10260v1#bib.bib69)].

The aim of this article is to propose and analyze a continuous-time RL framework for optimal stopping under ambiguity. Our framework starts with revisiting the following optimal stopping problem under gg-expectation (Coquet et al. [[12](https://arxiv.org/html/2510.10260v1#bib.bib12)], Peng [[53](https://arxiv.org/html/2510.10260v1#bib.bib53)]):
Let Tt{\mathcal{}T}\_{t} be the set of all stopping times with values in [t,T][t,T]. Denote by Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot] the (conditional) gg-expectation with driver g:Ω×[0,T]×ℝd→ℝg:\Omega\times[0,T]\times\mathbb{R}^{d}\to\mathbb{R} (satisfying certain regularity and integrability conditions; see Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), which is a filtration-consistent adverse nonlinear expectation whose representing set of probability measures is dominated by a reference measure ℙ\mathbb{P} (see Remark [2.2](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem2 "Remark 2.2. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Then, the optimal stopping problem under ambiguity is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (1.1) |  | Vtx:=ess​supτ∈Tt⁡Etg​[∫tτe−∫tsβu​𝑑u​r​(Xsx)​𝑑s+e−∫tτβu​𝑑u​R​(Xτx)],\displaystyle V\_{t}^{x}:=\operatorname\*{ess\,sup}\_{\tau\in{\mathcal{}T}\_{t}}{\mathcal{}E}^{g}\_{t}\bigg[\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}r(X\_{s}^{x})ds+e^{-\int\_{t}^{\tau}\beta\_{u}du}R(X\_{\tau}^{x})\bigg], |  |

where (βt)t∈[0,T](\beta\_{t})\_{t\in[0,T]} is the discount rate, r:ℝd→ℝr:\mathbb{R}^{d}\to\mathbb{R} and R:ℝd→ℝR:\mathbb{R}^{d}\to\mathbb{R} are reward functions, and (Xtx)t∈[0,T](X\_{t}^{x})\_{t\in[0,T]} is an Itô semimartingale given by Xtx:=x+∫0tbso​𝑑s+∫0tσso​𝑑BsX^{x}\_{t}:=x+\int\_{0}^{t}b\_{s}^{o}ds+\int\_{0}^{t}\sigma\_{s}^{o}dB\_{s} on the reference measure ℙ\mathbb{P}, where (Bs)s∈[0,T](B\_{s})\_{s\in[0,T]} is a dd-dimensional Brownian motion on ℙ\mathbb{P}, (bso,σso)s∈[0,T](b\_{s}^{o},\sigma\_{s}^{o})\_{s\in[0,T]} are baseline parameters, and x∈ℝdx\in\mathbb{R}^{d} is the initial state.

We then combine the penalization method of [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), [39](https://arxiv.org/html/2510.10260v1#bib.bib39), [54](https://arxiv.org/html/2510.10260v1#bib.bib54)] (used to establish the well-posedness of reflected backward stochastic differential equations (BSDEs) characterizing ([1.1](https://arxiv.org/html/2510.10260v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))) with the entropy regularization framework of [[66](https://arxiv.org/html/2510.10260v1#bib.bib66), [67](https://arxiv.org/html/2510.10260v1#bib.bib67)] to propose and analyze the following optimal exploratory control problem under ambiguity:

|  |  |  |  |
| --- | --- | --- | --- |
| (1.2) |  | V¯tx;N,λ:=ess​supπ∈Π⁡Etg[∫tTe−∫ts(βu+N​πu)​𝑑u(r(Xsx)+R(Xsx)Nπs−λH(πs))+e−∫tT(βu+N​πu)​𝑑uR(XTx)],\displaystyle\begin{aligned} \overline{V}\_{t}^{x;N,\lambda}:=\operatorname\*{ess\,sup}\_{\pi\in\Pi}{\mathcal{}E}^{g}\_{t}&[\int\_{t}^{T}e^{-\int\_{t}^{s}(\beta\_{u}+N\pi\_{u})du}\big(r(X\_{s}^{x})+R(X\_{s}^{x})\,N\pi\_{s}-\lambda{\mathcal{}H}(\pi\_{s})\big)\\ &\quad+e^{-\int\_{t}^{T}(\beta\_{u}+N\pi\_{u})du}R(X\_{T}^{x})],\end{aligned} |  |

where Π\Pi is the set of all progressively measurable processes with values in [0,1][0,1], representing Bernoulli-distributed controls randomizing stopping rules (see Remark [3.2](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), H:[0,1]→ℝ{\mathcal{}H}:[0,1]\to\mathbb{R} denotes the binary differential entropy (see ([3.1](https://arxiv.org/html/2510.10260v1#S3.E1 "Equation 3.1 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))), λ>0\lambda>0 represents the level of exploration to learn the unknown environment, and N∈ℕN\in\mathbb{N} represents the penalization level (used for approximation of ([1.1](https://arxiv.org/html/2510.10260v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))).

In Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), we show that if (bo,σo)(b^{o},\sigma^{o}) are sufficiently integrable (see Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), rr and RR has certain regularity and growth properties, and β\beta is uniformly bounded (see Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), then V¯x;N,λ\overline{V}^{x;N,\lambda} in ([1.2](https://arxiv.org/html/2510.10260v1#S1.E2 "Equation 1.2 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) can be characterized by a solution of a BSDE. In particular, the optimal Bernoulli-distributed control of ([1.2](https://arxiv.org/html/2510.10260v1#S1.E2 "Equation 1.2 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (1.3) |  | πt∗,x;N,λ:=logit⁡(Nλ​(R​(Xtx)−V¯tx;N,λ))=[1+e−Nλ​(R​(Xtx)−V¯tx;N,λ)]−1\displaystyle\pi^{\*,x;N,\lambda}\_{t}:=\operatorname{logit}(\frac{N}{\lambda}(R(X\_{t}^{x})-\overline{V}\_{t}^{x;N,\lambda}))=[1+e^{-\frac{N}{\lambda}(R(X\_{t}^{x})-\overline{V}\_{t}^{x;N,\lambda})}]^{-1} |  |

where logit⁡(x):=(1+exp⁡(−x))−1\operatorname{logit}(x):=(1+\exp(-x))^{-1}, x∈ℝx\in\mathbb{R}, denotes the standard logistic function.

It is noteworthy that a similar logistic form as in ([1.3](https://arxiv.org/html/2510.10260v1#S1.E3 "Equation 1.3 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) can also be observed in the non-robust setting in [[15](https://arxiv.org/html/2510.10260v1#bib.bib15)]; however, our value process V¯x;N,λ\overline{V}^{x;N,\lambda} is established through nonlinear expectation calculations. Moreover, the BSDE techniques of El Karoui et al. [[21](https://arxiv.org/html/2510.10260v1#bib.bib21)] are instrumental in the verification theorem for our maxmin problems (see Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Lastly, our BSDE arguments enable a sensitivity analysis of V¯x;N,λ\overline{V}^{x;N,\lambda} with respect to the level of exploration; see Theorem [3.5](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and Corollary [3.6](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem6 "Corollary 3.6. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

Next, under the same assumptions on bo,σo,r,R,βb^{o},\sigma^{o},r,R,\beta, Theorem [4.1](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") establishes a policy iteration result. Specifically, at each step we evaluate the gg-expectation value function under the control π∈Π\pi\in\Pi from the previous iteration and then update the control in the logistic form driven by this evaluated gg-expectation value (as in ([1.3](https://arxiv.org/html/2510.10260v1#S1.E3 "Equation 1.3 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))). This iterative process ensures that the resulting sequence of value functions and controls converge to the solution of ([1.2](https://arxiv.org/html/2510.10260v1#S1.E2 "Equation 1.2 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) as the number of iterations goes to infinity.

As an application of Theorem [4.1](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), under Markovian conditions on bo,σo,r,R,βb^{o},\sigma^{o},r,R,\beta (so that the assumptions made before hold), we devise an RL algorithm (see Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) in which policy evaluation at each iteration, characterized by a PDE (see Corollary [4.3](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), can be implemented by the deep splitting method of Beck et al. [[5](https://arxiv.org/html/2510.10260v1#bib.bib5)].

Finally, in order to illustrate all our theoretical results, we provide two numerical examples, American put-type and call-type stopping problems (see Section [5](https://arxiv.org/html/2510.10260v1#S5 "5 Experiments ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). We are able to observe policy improvement and convergence under several ambiguity degrees. Stability analysis for our exploratory BSDEs solution is also conducted with respect to ambiguity degree ε\varepsilon, temperature parameter λ\lambda and penalty factor NN using put-type stopping problem, while robustness is shown by call-type stopping decision-making under different level of dividend rate misspecification.

### 1.1 Related literature

Sutton and Barto [[63](https://arxiv.org/html/2510.10260v1#bib.bib63)] opened up the field of RL, which has since gained significant attention, with successful applications [[29](https://arxiv.org/html/2510.10260v1#bib.bib29), [44](https://arxiv.org/html/2510.10260v1#bib.bib44), [40](https://arxiv.org/html/2510.10260v1#bib.bib40), [60](https://arxiv.org/html/2510.10260v1#bib.bib60), [61](https://arxiv.org/html/2510.10260v1#bib.bib61)]. In continuous-time settings, [[66](https://arxiv.org/html/2510.10260v1#bib.bib66), [67](https://arxiv.org/html/2510.10260v1#bib.bib67)] introduced an RL framework based on relaxed controls, motivating subsequent development of RL schemes [[32](https://arxiv.org/html/2510.10260v1#bib.bib32), [35](https://arxiv.org/html/2510.10260v1#bib.bib35), [36](https://arxiv.org/html/2510.10260v1#bib.bib36), [37](https://arxiv.org/html/2510.10260v1#bib.bib37)], applications and extensions [[13](https://arxiv.org/html/2510.10260v1#bib.bib13), [14](https://arxiv.org/html/2510.10260v1#bib.bib14), [31](https://arxiv.org/html/2510.10260v1#bib.bib31), [64](https://arxiv.org/html/2510.10260v1#bib.bib64), [68](https://arxiv.org/html/2510.10260v1#bib.bib68)].

Our formulation of exploratory stopping problems under ambiguity aligns with, and can be viewed as, a robust analog of [[15](https://arxiv.org/html/2510.10260v1#bib.bib15), [17](https://arxiv.org/html/2510.10260v1#bib.bib17)], who combine the penalization method for variational inequalities with the exploratory framework of [[66](https://arxiv.org/html/2510.10260v1#bib.bib66), [67](https://arxiv.org/html/2510.10260v1#bib.bib67)] in the PDE setting. Recently, an exploratory stopping-time framework based on a singular control formulation has also been proposed by [[16](https://arxiv.org/html/2510.10260v1#bib.bib16)].

While some proof techniques in our work bear similarities to those in [[15](https://arxiv.org/html/2510.10260v1#bib.bib15), [17](https://arxiv.org/html/2510.10260v1#bib.bib17)], the consideration of ambiguity introduces substantial differences. In particular, due to the Itô semimartingale setting of XxX^{x} and the nonlinearity induced by the gg-expectation, PDE-based arguments cannot be applied directly. Instead, we establish a robust (i.e., max–min) verification theorem using BSDE techniques. Building on this, we derive a policy iteration theorem by analyzing a priori estimates for iterative BSDEs. A related recent work of [[26](https://arxiv.org/html/2510.10260v1#bib.bib26)] proposes and analyzes an exploratory optimal stopping framework under discrete stopping times but without ambiguity. Lastly, we refer to [[6](https://arxiv.org/html/2510.10260v1#bib.bib6), [7](https://arxiv.org/html/2510.10260v1#bib.bib7), [57](https://arxiv.org/html/2510.10260v1#bib.bib57)] for machine learning (ML) approaches to optimal stopping.

Moving away from the continuous-time RL (or ML) results to the literature on continuous-time optimal stopping under ambiguity, we refer to [[3](https://arxiv.org/html/2510.10260v1#bib.bib3), [4](https://arxiv.org/html/2510.10260v1#bib.bib4), [47](https://arxiv.org/html/2510.10260v1#bib.bib47), [51](https://arxiv.org/html/2510.10260v1#bib.bib51), [52](https://arxiv.org/html/2510.10260v1#bib.bib52), [58](https://arxiv.org/html/2510.10260v1#bib.bib58)]. More recently, [[43](https://arxiv.org/html/2510.10260v1#bib.bib43)] proposes a framework for optimal stopping that incorporates both ambiguity and learning. Rather than adopting a worst-case approach, as in the above references, the framework employs the smooth ambiguity-aversion model of Klibanoff et al. [[38](https://arxiv.org/html/2510.10260v1#bib.bib38)] in combination with Bayesian learning.

### 1.2 Notations and preliminaries

Fix d∈ℕd\in\mathbb{N}. We endow ℝd\mathbb{R}^{d} and ℝd×d\mathbb{R}^{d\times d} with the Euclidean inner product ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle and the Frobenius inner product ⟨⋅,⋅⟩F\langle\cdot,\cdot\rangle\_{\operatorname{F}}, respectively. Moreover, we denote by |⋅||\cdot| the Euclidean norm and denote by ∥⋅∥F\|\cdot\|\_{\operatorname{F}} the Frobenius norm.

Let (Ω,F,ℙ)(\Omega,{\mathcal{}F},\mathbb{P}) be a probability space and let B:=(Bt)t≥0B:=(B\_{t})\_{t\geq 0} be a dd-dimensional standard Brownian motion starting with B0=0B\_{0}=0. Fix T>0T>0 a finite time horizon, and let 𝔽:=(Ft)t∈[0,T]\mathbb{F}:=({\mathcal{}F}\_{t})\_{t\in[0,T]} be the usual augmentation of the natural filtration generated by BB, i.e., Ft:=σ​(Bs;s≤t)∨N{\mathcal{}F}\_{t}:=\sigma(B\_{s};s\leq t)\vee{\mathcal{}N}, where N{\mathcal{}N} is the set of all ℙ\mathbb{P}-null subsets.

For any probability measure ℚ\mathbb{Q} on (Ω,F)(\Omega,{\mathcal{}F}), we write 𝔼ℚ​[⋅]\mathbb{E}^{\mathbb{Q}}[\cdot] for the expectation under ℚ\mathbb{Q} and 𝔼tℚ[⋅]:=𝔼ℚ[⋅|Ft]\mathbb{E}^{\mathbb{Q}}\_{t}[\cdot]:=\mathbb{E}^{\mathbb{Q}}[\cdot|{\mathcal{}F}\_{t}] for the conditional expectation under ℚ\mathbb{Q} with respect to Ft{\mathcal{}F}\_{t} at time t≥0t\geq 0. Moreover, we set 𝔼​[⋅]:=𝔼ℙ​[⋅]\mathbb{E}[\cdot]:=\mathbb{E}^{\mathbb{P}}[\cdot] and 𝔼t​[⋅]:=𝔼tℙ​[⋅]\mathbb{E}\_{t}[\cdot]:=\mathbb{E}^{\mathbb{P}}\_{t}[\cdot] for t≥0t\geq 0. For any p≥1p\geq 1, k∈ℕk\in\mathbb{N} and t∈[0,T]t\in[0,T], consider the following sets:

* •

  Lp​(Ft;ℝk)L^{p}({\mathcal{}F}\_{t};\mathbb{R}^{k}) is the set of all ℝk\mathbb{R}^{k}-valued, Ft{\mathcal{}F}\_{t}-measurable random variables ξ\xi such that ‖ξ‖Lpp:=𝔼​[|ξ|p]<∞\|\xi\|\_{L^{p}}^{p}:=\mathbb{E}[|\xi|^{p}]<\infty;
* •

  𝕃p​(ℝk)\mathbb{L}^{p}(\mathbb{R}^{k}) is the set of all ℝk\mathbb{R}^{k}-valued, 𝔽\mathbb{F}-predictable processes Z=(Zt)t∈[0,T]Z=(Z\_{t})\_{t\in[0,T]} such that ‖Z‖𝕃pp:=𝔼​[∫0T|Zt|p​𝑑t]<∞\|Z\|^{p}\_{\mathbb{L}^{p}}:=\mathbb{E}[\int\_{0}^{T}|Z\_{t}|^{p}dt]<\infty;
* •

  𝕊p​(ℝk)\mathbb{S}^{p}(\mathbb{R}^{k}) is the set of all ℝk\mathbb{R}^{k}-valued, 𝔽\mathbb{F}-progressively measurable càdlàg (i.e., right-continuous with left-limits) processes Y=(Yt)t∈[0,T]Y=(Y\_{t})\_{t\in[0,T]} such that ‖Y‖𝕊pp:=𝔼​[supt∈[0,T]|Yt|p]<∞\|Y\|\_{\mathbb{S}^{p}}^{p}:=\mathbb{E}[\sup\_{t\in[0,T]}|Y\_{t}|^{p}]<\infty;
* •

  Tt{\mathcal{}T}\_{t} is the set of all 𝔽\mathbb{F}-stopping times τ\tau with values in [t,T][t,T].

## 2 Optimal stopping under ambiguity

Consider the optimal stopping time choice of an agent facing ambiguity, where the agent is ambiguity-averse and his/her stopping time is determined by observing an ambiguous underlying state process in a continuous-time environment. We model the agent’s preference and the environment by using the gg-expectation Eg​[⋅]{\mathcal{}E}^{g}[\cdot] (see [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), [53](https://arxiv.org/html/2510.10260v1#bib.bib53)]) defined as follows.

###### Definition 2.1.

Let the driver term g:Ω×[0,T]×ℝd→ℝg:\Omega\times[0,T]\times\mathbb{R}^{d}\to\mathbb{R} be a mapping such that the following conditions hold:

* (i)

  for z∈ℝdz\in\mathbb{R}^{d}, (g​(t,z))t∈[0,T](g(t,z))\_{t\in[0,T]} is 𝔽\mathbb{F}-progressively measurable with ‖g​(⋅,z)‖𝕃2<∞\|g(\cdot,z)\|\_{\mathbb{L}^{2}}<\infty;
* (ii)

  there exists some constant κ>0\kappa>0 such that for every (ω,t)∈Ω×[0,T](\omega,t)\in\Omega\times[0,T] and z,z′∈ℝdz,z^{\prime}\in\mathbb{R}^{d} |g​(ω,t,z)−g​(ω,t,z′)|≤κ​|z−z′|;\big|g(\omega,t,z)-g(\omega,t,z^{\prime})\big|\leq\kappa|z-z^{\prime}|;
* (iii)

  for every (ω,t)∈Ω×[0,T](\omega,t)\in\Omega\times[0,T], g​(ω,t,⋅):ℝd→ℝg(\omega,t,\cdot):\mathbb{R}^{d}\to\mathbb{R} is concave and g​(ω,t,0)=0g(\omega,t,0)=0.

Then we define Eg:L2​(FT;ℝ)∋ξ→Eg​[ξ]∈ℝ{\mathcal{}E}^{g}:L^{2}({\mathcal{}F}\_{T};\mathbb{R})\ni\xi\to{\mathcal{}E}^{g}[\xi]\in\mathbb{R} as Eg​[ξ]:=Y0,{\mathcal{}E}^{g}[\xi]:=Y\_{0},
where (Y,Z)∈𝕊2​(ℝ)×𝕃2​(ℝd)(Y,Z)\in\mathbb{S}^{2}(\mathbb{R})\times\mathbb{L}^{2}(\mathbb{R}^{d}) is the unique solution of the following BSDE (see [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Theorem 3.1]):

|  |  |  |
| --- | --- | --- |
|  | Yt=ξ+∫tTg​(s,Zs)​𝑑s−∫tTZs​𝑑Bs,\displaystyle Y\_{t}=\xi+\int\_{t}^{T}g(s,Z\_{s})ds-\int\_{t}^{T}Z\_{s}dB\_{s}, |  |

where (Bt)t∈[0,T](B\_{t})\_{t\in[0,T]} is the fixed dd-dimensional Brownian motion on (Ω,F,ℙ)(\Omega,{\mathcal{}F},\mathbb{P}). Moreover, its conditional gg-expectation with respect to Ft{\mathcal{}F}\_{t} is defined by
Etg​[ξ]:=Yt{\mathcal{}E}^{g}\_{t}[\xi]:=Y\_{t} for t∈[0,T]t\in[0,T],
which can be extended into 𝔽\mathbb{F}-stopping times τ∈T0\tau\in{\mathcal{}T}\_{0}, i.e., Eτg​[ξ]:=Yτ.{\mathcal{}E}^{g}\_{\tau}[\xi]:=Y\_{\tau}.

###### Remark 2.2.

The gg-expectation defined above coincides with a variational representation in the following sense (see [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Proposition 3.6], [[23](https://arxiv.org/html/2510.10260v1#bib.bib23), Proposition A.1]): Define g^:Ω×[0,T]×ℝd∋(ω,t,z^)→g^​(ω,t,z^):=supz∈ℝd(g​(ω,t,z)−⟨z,z^⟩)∈ℝ,\hat{g}:\Omega\times[0,T]\times\mathbb{R}^{d}\ni(\omega,t,\hat{z})\to\hat{g}(\omega,t,\hat{z}):=\sup\_{z\in\mathbb{R}^{d}}\big(g(\omega,t,z)-\langle z,\hat{z}\rangle\big)\in\mathbb{R},
i.e., the convex conjugate function of g​(ω,t,⋅)g(\omega,t,\cdot). Denote by Bg{\mathcal{}B}^{g} the set of all 𝔽\mathbb{F} progressively measurable processes ϑ=(ϑt)t∈[0,T]\vartheta=(\vartheta\_{t})\_{t\in[0,T]} such that ‖g^​(⋅,ϑ⋅)‖𝕃2<∞\|\hat{g}(\cdot,\vartheta\_{\cdot})\|\_{\mathbb{L}^{2}}<\infty.

For any τ∈Tt\tau\in{\mathcal{}T}\_{t} and t∈[0,T]t\in[0,T], the following representation holds:

|  |  |  |
| --- | --- | --- |
|  | Etg​[ξ]=ess​infϑ∈Bg⁡𝔼tℙϑ​[ξ+∫tτg^​(s,ϑs)​𝑑s]for​ξ∈L2​(Fτ;ℝd),\displaystyle{\mathcal{}E}\_{t}^{g}[\xi]=\operatorname\*{ess\,inf}\_{\vartheta\in{\mathcal{}B}^{g}}\mathbb{E}\_{t}^{\mathbb{P}^{\vartheta}}\bigg[\xi+\int\_{t}^{\tau}\hat{g}(s,\vartheta\_{s})ds\bigg]\quad\mbox{for}\;\;\xi\in L^{2}({\mathcal{}F}\_{\tau};\mathbb{R}^{d}), |  |

where ℙϑ\mathbb{P}^{\vartheta} is defined on (Ω,FT)(\Omega,{\mathcal{}F}\_{T}) through d​ℙϑd​ℙ|FT:=exp⁡(−12​∫0T|ϑs|2​𝑑s+∫0Tϑs​𝑑Bs).\frac{d\mathbb{P}^{\vartheta}}{d\mathbb{P}}|\_{{\mathcal{}F}\_{T}}:=\exp(-\frac{1}{2}\int\_{0}^{T}|\vartheta\_{s}|^{2}ds+\int\_{0}^{T}\vartheta\_{s}dB\_{s}).

For (sufficiently integrable) 𝔽\mathbb{F}-predictable processes (bso)s∈[0,T](b\_{s}^{o})\_{s\in[0,T]} and (σso)s∈[0,T](\sigma\_{s}^{o})\_{s\in[0,T]} taking values in ℝd\mathbb{R}^{d} and ℝd×d\mathbb{R}^{d\times d} respectively, we consider an Itô (𝔽,ℙ)(\mathbb{F},\mathbb{P})-semimartingale Xx:=(Xtx)t∈[0,T]X^{x}:=(X^{x}\_{t})\_{t\in[0,T]} given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | Xtx:=x+∫0tbso​𝑑s+∫0tσso​𝑑Bs,t∈[0,T],\displaystyle X\_{t}^{x}:=x+\int\_{0}^{t}b^{o}\_{s}ds+\int\_{0}^{t}\sigma^{o}\_{s}dB\_{s},\quad t\in[0,T], |  |

where x∈ℝdx\in\mathbb{R}^{d} is fixed and does not depend on bob^{o} and σo\sigma^{o}.

We note that bob^{o} and σo\sigma^{o} correspond to the baseline parameters (e.g., the estimators) and XxX^{x} corresponds to the reference underlying state process. We assume the certain integrability condition on the baseline parameters. To that end, for any p≥1p\geq 1, let 𝕃p​(ℝd)\mathbb{L}^{p}(\mathbb{R}^{d}) be defined as in Section [1.2](https://arxiv.org/html/2510.10260v1#S1.SS2 "1.2 Notations and preliminaries ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and let 𝕃Fp​(ℝd×d)\mathbb{L}\_{\operatorname{F}}^{p}(\mathbb{R}^{d\times d}) be the set of all ℝd×d\mathbb{R}^{d\times d}-valued, 𝔽\mathbb{F}-predictable processes H=(Ht)t∈[0,T]H=(H\_{t})\_{t\in[0,T]} such that ‖H‖𝕃Fpp:=𝔼​[(∫0T‖Ht‖F2​𝑑t)p2]<∞\|H\|^{p}\_{\mathbb{L}\_{\operatorname{F}}^{p}}:=\mathbb{E}[(\int\_{0}^{T}\|H\_{t}\|\_{\operatorname{F}}^{2}dt)^{\frac{p}{2}}]<\infty.
{as}
bo∈𝕃p​(ℝd)b^{o}\in\mathbb{L}^{p}(\mathbb{R}^{d}) and σo∈𝕃Fp​(ℝd×d)\sigma^{o}\in\mathbb{L}\_{\operatorname{F}}^{p}(\mathbb{R}^{d\times d}) for some p≥2p\geq 2.

###### Remark 2.3.

Either one of the following conditions is sufficient for Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") to hold true [[2](https://arxiv.org/html/2510.10260v1#bib.bib2), Lemma 2.3]:

* (i)

  bob^{o} and σo\sigma^{o} are uniformly bounded, i.e., there exists some constant Cb,σ>0C\_{b,\sigma}>0 such that |bto|+‖σto‖F≤Cb,σ|b^{o}\_{t}|+\|\sigma\_{t}^{o}\|\_{\operatorname{F}}\leq C\_{b,\sigma} ℙ⊗d​t\mathbb{P}\otimes dt-a.e..
* (ii)

  bob^{o} and σo\sigma^{o} are of the following form: bto=b~o​(t,Xtx),b\_{t}^{o}=\widetilde{b}^{o}(t,X\_{t}^{x}), σto=σ~o​(t,Xtx)\sigma\_{t}^{o}=\widetilde{\sigma}^{o}(t,X\_{t}^{x}) ℙ⊗d​t\mathbb{P}\otimes dt-a.e.,
  where
  b~o:[0,T]×ℝd→ℝd\widetilde{b}^{o}:[0,T]\times\mathbb{R}^{d}\rightarrow\mathbb{R}^{d} and σ~o:[0,T]×ℝd→ℝd×d\widetilde{\sigma}^{o}:[0,T]\times\mathbb{R}^{d}\rightarrow\mathbb{R}^{d\times d} are Borel functions satisfying that |b~o(t,y)−b~o(t,y^)|+∥σ~o(t,y)−σ~o(t,y^)∥F≤Cb~,σ~|y−y^|\lvert\widetilde{b}^{o}(t,y)-\widetilde{b}^{o}(t,\hat{y})\lvert+\lVert\widetilde{\sigma}^{o}(t,y)-\widetilde{\sigma}^{o}(t,\hat{y})\rVert\_{\operatorname{F}}\leq C\_{\widetilde{b},\widetilde{\sigma}}\lvert y-\hat{y}\rvert and |b~o(t,y)|+∥σ~o(t,y)∥F≤Cb~,σ~(1+|y|)\lvert\widetilde{b}^{o}(t,y)\lvert+\lVert\widetilde{\sigma}^{o}(t,y)\rVert\_{\operatorname{F}}\leq C\_{\widetilde{b},\widetilde{\sigma}}(1+\lvert y\rvert) for every t∈[0,T]t\in[0,T] and y,y^∈ℝdy,\hat{y}\in\mathbb{R}^{d},
  with some constant Cb~,σ~>0C\_{\widetilde{b},\widetilde{\sigma}}>0.

###### Remark 2.4.

* (i)

  Under Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), a straightforward application of the Burkholder Davis Gundy (BDG) inequality shows that ‖Xx‖𝕊p<∞\|X^{x}\|\_{\mathbb{S}^{p}}<\infty.
* (ii)

  In fact, both sufficient conditions given in Remark [2.3](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem3 "Remark 2.3. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") ensure that Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") holds for all p≥2p\geq 2 (see [[41](https://arxiv.org/html/2510.10260v1#bib.bib41), Theorems 2.3.1 and 2.4.1])

Having completed the descriptions of the gg-expectation and underlying process, we describe the decision-maker’s optimal stopping problem Vx:=(Vtx)t∈[0,T]V^{x}:=(V\_{t}^{x})\_{t\in[0,T]} under ambiguity: for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | Vtx:=ess​supτ∈Tt⁡Etg​[Itx;τ];Itx;τ:=∫tτe−∫tsβu​𝑑u​r​(Xsx)​𝑑s+e−∫tτβu​𝑑u​R​(Xτx),\displaystyle\begin{aligned} &V\_{t}^{x}:=\operatorname\*{ess\,sup}\_{\tau\in{\mathcal{}T}\_{t}}{\mathcal{}E}^{g}\_{t}[\operatorname{I}\_{t}^{x;\tau}];\qquad\operatorname{I}\_{t}^{x;\tau}:=\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}r(X\_{s}^{x})ds+e^{-\int\_{t}^{\tau}\beta\_{u}du}R(X\_{\tau}^{x}),\end{aligned} |  |

where both r:ℝd→ℝr:\mathbb{R}^{d}\to\mathbb{R} and R:ℝd→ℝR:\mathbb{R}^{d}\to\mathbb{R}
are some Borel functions (representing the intermediate and stopping reward functions), and (βu)u∈[0,T](\beta\_{u})\_{u\in[0,T]} is an 𝔽\mathbb{F}-progressively measurable process taking positive values (representing the subjective discount rate).

{as}

* (i)

  RR is continuous. Moreover, there exists some constant Cr,R>0C\_{r,R}>0 such that for every y∈ℝdy\in\mathbb{R}^{d}, |r​(y)|+|R​(y)|≤Cr,R​(1+|y|)|r(y)|+|R(y)|\leq C\_{r,R}(1+|y|).
* (ii)

  There is some Cβ>0C\_{\beta}>0 such that 0≤βt​(ω)≤Cβ0\leq\beta\_{t}(\omega)\leq C\_{\beta} for all (ω,t)∈Ω×[0,T](\omega,t)\in\Omega\times[0,T].

###### Remark 2.5.

Under Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), it holds for every t∈[0,T]t\in[0,T] and τ∈Tt\tau\in{\mathcal{}T}\_{t} that the integrand Itx;τ\operatorname{I}\_{t}^{x;\tau} given in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is in L2​(Fτ;ℝ)L^{2}({\mathcal{}F}\_{\tau};\mathbb{R}). Indeed, by the triangle inequality and the positiveness of (βu)u∈[0,T](\beta\_{u})\_{u\in[0,T]}, 𝔼​[|Itx;τ|]≤Cr,R​(T+1)​‖Xx‖𝕊1;\mathbb{E}[|\operatorname{I}\_{t}^{x;\tau}|]\leq C\_{r,R}(T+1)\|X^{x}\|\_{\mathbb{S}^{1}};
see also Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."). Moreover, since ‖Xx‖𝕊p<∞\|X^{x}\|\_{\mathbb{S}^{p}}<\infty with the exponent p≥2p\geq 2 (see Remark [2.4](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i)), an application of the Jensen’s inequality with exponent 22 ensures the claim to hold. As a direct consequence, VxV^{x} in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is well-defined.

Let us that the VxV^{x} given in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) corresponds to a reflected BSDE with a lower obstacle. To that end, set for every (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d} by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | Ftx​(ω,y,z):=r​(Xtx​(ω))−βt​(ω)​y+g​(ω,t,z),\displaystyle F\_{t}^{x}(\omega,y,z):=r(X\_{t}^{x}(\omega))-\beta\_{t}(\omega)y+g(\omega,t,z), |  |

where g:Ω×[0,T]×ℝd→ℝg:\Omega\times[0,T]\times\mathbb{R}^{d}\to\mathbb{R} is defined as in Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), (Xtx)t∈[0,T](X\_{t}^{x})\_{t\in[0,T]} is given in ([2.1](https://arxiv.org/html/2510.10260v1#S2.E1 "Equation 2.1 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), and (βt)t∈[0,T](\beta\_{t})\_{t\in[0,T]} is the discount rate appearing in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Denote by (Ytx,Ztx,Ktx)t∈[0,T](Y\_{t}^{x},Z\_{t}^{x},K^{x}\_{t})\_{t\in[0,T]} a triplet of processes satisfying that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | Ytx=R​(XTx)+∫tTFsx​(Ysx,Zsx)​𝑑s−∫tTZsx​𝑑Bs+KTx−Ktx,for​t∈[0,T],\displaystyle Y\_{t}^{x}=R(X\_{T}^{x})+\int\_{t}^{T}F\_{s}^{x}(Y\_{s}^{x},Z\_{s}^{x})ds-\int\_{t}^{T}Z\_{s}^{x}dB\_{s}+K\_{T}^{x}-K\_{t}^{x},\;\;\mbox{for}\;t\in[0,T], |  |

We then introduce the notion of the reflected BSDE (see [[39](https://arxiv.org/html/2510.10260v1#bib.bib39), Definition 2.1]). For this, recall the sets 𝕊2​(ℝ)\mathbb{S}^{2}(\mathbb{R}) and 𝕃2​(ℝd)\mathbb{L}^{2}(\mathbb{R}^{d}) given in Section [1.2](https://arxiv.org/html/2510.10260v1#S1.SS2 "1.2 Notations and preliminaries ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

###### Definition 2.6.

A triplet (Yx,Zx,Kx)(Y^{x},Z^{x},K^{x}) is said to be a solution
to the reflected BSDE ([2.4](https://arxiv.org/html/2510.10260v1#S2.E4 "Equation 2.4 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) with the lower obstacle (R​(Xtx))t∈[0,T](R(X\_{t}^{x}))\_{t\in[0,T]} if the following conditions hold:

* (i)

  Yx∈𝕊2​(ℝ)Y^{x}\in\mathbb{S}^{2}(\mathbb{R}), Zx∈𝕃2​(ℝd)Z^{x}\in\mathbb{L}^{2}(\mathbb{R}^{d}) and Kx∈𝕊2​(ℝ)K^{x}\in\mathbb{S}^{2}(\mathbb{R}) which is nondecreasing and starts with K0x=0K\_{0}^{x}=0. Moreover, (Yx,Zx,Kx)(Y^{x},Z^{x},K^{x}) satisfies ([2.4](https://arxiv.org/html/2510.10260v1#S2.E4 "Equation 2.4 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."));
* (ii)

  Ytx≥R​(Xtx)Y\_{t}^{x}\geq R(X\_{t}^{x}) ℙ\mathbb{P}-a.s., for all t≥0t\geq 0;
* (iii)

  ∫0T(Yt−x−R​(Xt−x))​𝑑Ktx=0\int\_{0}^{T}(Y\_{t-}^{x}-R(X\_{t-}^{x}))dK\_{t}^{x}=0 ℙ\mathbb{P}-a.s..

###### Remark 2.7.

Under Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), there exists a unique solution (Ytx(Y\_{t}^{x}, Ztx,Ktx)t∈[0,T]Z\_{t}^{x},K^{x}\_{t})\_{t\in[0,T]} of the reflected BSDE ([2.4](https://arxiv.org/html/2510.10260v1#S2.E4 "Equation 2.4 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) with the lower obstacle (R​(Xtx))t∈[0,T](R(X\_{t}^{x}))\_{t\in[0,T]} (see Definition [2.6](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem6 "Definition 2.6. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Indeed, one can easily show that the parameters of the reflected BSDE satisfy the conditions (i)–(iii) given in [[39](https://arxiv.org/html/2510.10260v1#bib.bib39), Section 2], which enables to apply [[39](https://arxiv.org/html/2510.10260v1#bib.bib39), Theorem 3.3] to ensures its existence and uniqueness to hold.

The following proposition establishes that the solution to the reflected BSDE ([2.4](https://arxiv.org/html/2510.10260v1#S2.E4 "Equation 2.4 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) coincides with the Snell envelope of the optimal stopping problem under ambiguity given in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). This result can be seen as a robust analogue of [[20](https://arxiv.org/html/2510.10260v1#bib.bib20), Proposition 2.3] and [[39](https://arxiv.org/html/2510.10260v1#bib.bib39), Proposition 3.1]. Several properties of (conditional) gg-expectation developed in [[12](https://arxiv.org/html/2510.10260v1#bib.bib12)] are useful in the proof presented in Section [6.1](https://arxiv.org/html/2510.10260v1#S6.SS1 "6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

###### Proposition 2.8.

Suppose that Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") hold. Let (Vtx)t∈[0,T](V\_{t}^{x})\_{t\in[0,T]} be given in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (see Remark [2.5](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and let (Ytx)t∈[0,T](Y\_{t}^{x})\_{t\in[0,T]} be the first component of the unique solution to the reflected BSDE ([2.4](https://arxiv.org/html/2510.10260v1#S2.E4 "Equation 2.4 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) with the lower obstacle (R​(Xtx))t∈[0,T](R(X\_{t}^{x}))\_{t\in[0,T]} (see Remark [2.7](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem7 "Remark 2.7. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Then, Vtx=YtxV\_{t}^{x}=Y\_{t}^{x}, ℙ\mathbb{P}-a.s. for all t∈[0,T]t\in[0,T]. In particular, the stopping time τt∗,x∈Tt\tau\_{t}^{\*,x}\in{\mathcal{}T}\_{t}, defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.5) |  | τt∗,x:=inf{s≥t|Ytx≤R​(Xtx)}∧T,\displaystyle\tau\_{t}^{\*,x}:=\inf\{s\geq t\,|\,Y\_{t}^{x}\leq R(X\_{t}^{x})\}\wedge T, |  |

is optimal to the robust stopping problem VxV^{x}.

The penalization method is a standard approach for establishing the existence of solutions to reflected BSDEs (see, e.g., [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), [39](https://arxiv.org/html/2510.10260v1#bib.bib39), [54](https://arxiv.org/html/2510.10260v1#bib.bib54)]). We introduce a sequence of penalized BSDEs and remark on the convergence of their solutions to that of the reflected BSDE given ([2.4](https://arxiv.org/html/2510.10260v1#S2.E4 "Equation 2.4 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

To that end, set for every N∈ℕN\in\mathbb{N} and (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d} by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.6) |  | Ftx;N​(ω,y,z):=Ftx​(ω,y,z)+N​(R​(Xtx​(ω))−y)+,\displaystyle F\_{t}^{x;N}(\omega,y,z):=F\_{t}^{x}(\omega,y,z)+N(R\big(X\_{t}^{x}(\omega)\big)-y)^{+}, |  |

where FxF^{x} is given in ([2.3](https://arxiv.org/html/2510.10260v1#S2.E3 "Equation 2.3 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and (a)+:=max⁡{a,0}(a)^{+}:=\max\{a,0\} for a∈ℝa\in\mathbb{R}. Then we denote for every N∈ℕN\in\mathbb{N} by (Ytx;N,Ztx;N)t∈[0,T](Y\_{t}^{x;N},Z\_{t}^{x;N})\_{t\in[0,T]} a couple of processes satisfying that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | Ytx;N=R​(XTx)+∫tTFsx;N​(Ysx;N,Zsx;N)​𝑑s−∫tTZsx;N​𝑑Bs,for t∈[0,T].\displaystyle Y\_{t}^{x;N}=R(X\_{T}^{x})+\int\_{t}^{T}F\_{s}^{x;N}(Y\_{s}^{x;N},Z\_{s}^{x;N})ds-\int\_{t}^{T}Z\_{s}^{x;N}dB\_{s},\;\;\mbox{for $t\in[0,T]$}. |  |

###### Remark 2.9.

Under Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), the parameters of the BSDE ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfy all the conditions given in [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Section 3]. Hence, we recognize:

* (i)

  For every N∈ℕN\in\mathbb{N} there exists a unique solution (Ytx;N,Ztx;N)t∈[0,T]∈𝕊2​(ℝ)×𝕃2​(ℝd)(Y^{x;N}\_{t},Z\_{t}^{x;N})\_{t\in[0,T]}\in\mathbb{S}^{2}(\mathbb{R})\times\mathbb{L}^{2}(\mathbb{R}^{d}) of the BSDE ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (see [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Theorem 3.1]).
* (ii)

  Moreover, if we set Ktx;N:=N​∫0t(R​(Xsx)−Ysx;N)+​𝑑sK\_{t}^{x;N}:=N\int\_{0}^{t}(R(X\_{s}^{x})-Y\_{s}^{x;N})^{+}ds for t∈[0,T]t\in[0,T], then it follows from
  [[20](https://arxiv.org/html/2510.10260v1#bib.bib20), Section 6., Eq. (16)] that there exists some constant C>0C>0 such that for every N∈ℕN\in\mathbb{N}, ‖Yx;N‖𝕊22+‖Zx;N‖𝕃22+‖KTx;N‖L22≤C.\|Y^{x;N}\|\_{\mathbb{S}^{2}}^{2}+\|Z^{x;N}\|\_{\mathbb{L}^{2}}^{2}+\|K\_{T}^{x;N}\|\_{L^{2}}^{2}\leq C.
* (iii)

  Lastly, we recall that (Ytx,Ztx,Ktx)t∈[0,T](Y\_{t}^{x},Z\_{t}^{x},K\_{t}^{x})\_{t\in[0,T]} is the unique solution to the reflected gg-BSDE ([2.4](https://arxiv.org/html/2510.10260v1#S2.E4 "Equation 2.4 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (see Remark [2.7](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem7 "Remark 2.7. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Then, it follows from [[39](https://arxiv.org/html/2510.10260v1#bib.bib39), Lemma 3.2 & Theorem 3.3] that111We say Z∈𝕃2​(ℝd)Z\in\mathbb{L}^{2}(\mathbb{R}^{d}) is the weak limit of (Zn)n∈ℕ⊆𝕃2​(ℝd)(Z^{n})\_{n\in\mathbb{N}}\subseteq\mathbb{L}^{2}(\mathbb{R}^{d}) if for every ϕ∈𝕃2​(ℝd)\phi\in\mathbb{L}^{2}(\mathbb{R}^{d}), it holds that ⟨Zn,ϕ⟩ℙ⊗d​t→⟨Z,ϕ⟩ℙ⊗d​t\langle Z^{n},\phi\rangle\_{\mathbb{P}\otimes dt}\to\langle Z,\phi\rangle\_{\mathbb{P}\otimes dt} as n→∞n\to\infty, where the inner product is defined by ⟨L,M⟩ℙ⊗d​t:=𝔼​[∫0T⟨Lt,Mt⟩​𝑑t]\langle L,M\rangle\_{\mathbb{P}\otimes dt}:=\mathbb{E}[\int\_{0}^{T}\langle L\_{t},M\_{t}\rangle dt] for L,M∈𝕃2​(ℝd)L,M\in\mathbb{L}^{2}(\mathbb{R}^{d}). Similarly, the weak limit in L2​(Ft;ℝd)L^{2}({\mathcal{}F}\_{t};\mathbb{R}^{d}) is defined w.r.t. the inner product ⟨ξ,η⟩ℙ:=𝔼​[⟨ξ,η⟩]\langle\xi,\eta\rangle\_{\mathbb{P}}:=\mathbb{E}[\langle\xi,\eta\rangle] for ξ,η∈L2​(Ft;ℝd)\xi,\eta\in L^{2}({\mathcal{}F}\_{t};\mathbb{R}^{d}). YxY^{x} is the strong limit of (Yx;N)N∈ℕ(Y^{x;N})\_{N\in\mathbb{N}} in 𝕃2​(ℝ)\mathbb{L}^{2}(\mathbb{R}) (i.e., as N→∞N\to\infty
  ‖Yx;N−Yx‖𝕃2→0\|Y^{x;N}-Y^{x}\|\_{\mathbb{L}^{2}}\to 0),
  ZxZ^{x} is the weak limit of (Zx;N)N∈ℕ(Z^{x;N})\_{N\in\mathbb{N}} in 𝕃2​(ℝd)\mathbb{L}^{2}(\mathbb{R}^{d}), and for each t∈[0,T]t\in[0,T] KtxK\_{t}^{x} is the weak limit of Ktx;NK\_{t}^{x;N} in L2​(Ft;ℝ){L}^{2}({\mathcal{}F}\_{t};\mathbb{R}).

The following proposition shows that for each N∈ℕN\in\mathbb{N} the solution to the penalized BSDE ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) can be represented by a certain optimal stochastic control problem under ambiguity. The corresponding proof is presented in Section [6.1](https://arxiv.org/html/2510.10260v1#S6.SS1 "6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

###### Proposition 2.10.

Suppose that Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") hold. Let N∈ℕN\in\mathbb{N} be given. Denote by Yx;NY^{x;N} the first component of the unique solution to ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Then Yx;NY^{x;N} admits a representation of the robust control optimization problem in the following sense:
Let A{\mathcal{}A} be the set of all 𝔽\mathbb{F}-progressively measurable processes α=(αt)t∈[0,T]\alpha=(\alpha\_{t})\_{t\in[0,T]} with values in {0,1}\{0,1\}. Set for every t∈[0,T]t\in[0,T] and N∈ℕN\in\mathbb{N}

|  |  |  |
| --- | --- | --- |
|  | Itx;N,α:=∫tTe−∫ts(βu+N​αu)​𝑑u​(r​(Xsx)+R​(Xsx)​N​αs)​𝑑s+e−∫tT(βu+N​αu)​𝑑u​R​(XTx).\operatorname{I}\_{t}^{x;N,\alpha}:=\int\_{t}^{T}e^{-\int\_{t}^{s}(\beta\_{u}+N\alpha\_{u})du}\big(r(X\_{s}^{x})+R(X\_{s}^{x})\,N\alpha\_{s}\big)ds+e^{-\int\_{t}^{T}(\beta\_{u}+N\alpha\_{u})du}R(X\_{T}^{x}). |  |

Then it holds for every t∈[0,T]t\in[0,T] that Ytx;N=ess​supα∈A⁡Etg​[Itx;N,α]=Etg​[Itx;N,α∗,x;N],Y\_{t}^{x;N}=\operatorname\*{ess\,sup}\_{\alpha\in{\mathcal{}A}}{\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;N,\alpha}]={\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;N,\alpha^{\*,x;N}}], ℙ\mathbb{P}-a.s., where α∗,x;N:=(αt∗,x;N)t∈[0,T]∈A\alpha^{\*,x;N}:=(\alpha^{\*,x;N}\_{t})\_{t\in[0,T]}\in{\mathcal{}A} is the optimizer given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | αt∗,x;N:=𝟏{R​(Xtx)>Ytx;N}for t∈[0,T].\displaystyle\alpha^{\*,x;N}\_{t}:={\bf 1}\_{\{R(X\_{t}^{x})>Y\_{t}^{x;N}\}}\quad\mbox{for $t\in[0,T]$}. |  |

## 3 Exploratory framework: approximation of optimal stopping under ambiguity

Based on the results in Section [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), we are able to show that
for sufficiently large N∈ℕN\in\mathbb{N}, the optimal stopping problem Vx(=Yx)V^{x}(=Y^{x}) under ambiguity in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (see also Proposition [2.8](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem8 "Proposition 2.8. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) can be approximated by the optimal stochastic control problem Yx;NY^{x;N} under ambiguity (see Proposition [2.10](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). The proofs of all the results in this section are presented in Section [6.2](https://arxiv.org/html/2510.10260v1#S6.SS2 "6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

We introduce an exploratory framework of [[66](https://arxiv.org/html/2510.10260v1#bib.bib66), [67](https://arxiv.org/html/2510.10260v1#bib.bib67)] into Yx;NY^{x;N}. In particular, we aim to study a robust analogue of the optimal exploratory stopping framework in [[15](https://arxiv.org/html/2510.10260v1#bib.bib15)]. To that end, let Π\Pi be the set of all 𝔽\mathbb{F}-progressively measurable processes π=(πt)t∈[0,T]\pi=(\pi\_{t})\_{t\in[0,T]} taking values in [0,1][0,1], i.e., an exploratory version of the {0,1}\{0,1\}-valued controls set A{\mathcal{}A} appearing in Proposition [2.10](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

Then let H:[0,1]∋a→H​(a)∈ℝ{\mathcal{}H}:[0,1]\ni a\to{\mathcal{}H}(a)\in\mathbb{R} be the binary differential entropy defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | H​(a):=a​log⁡(a)+(1−a)​log⁡(1−a)for a∈(0,1),\displaystyle{\mathcal{}H}(a):=a\log(a)+(1-a)\log(1-a)\quad\mbox{for $a\in(0,1)$}, |  |

with the convention that H​(0):=lima↓0H​(a)=0{\mathcal{}H}(0):=\lim\_{a\downarrow 0}{\mathcal{}H}(a)=0 and H​(1):=lima↑1H​(a)=0{\mathcal{}H}(1):=\lim\_{a\uparrow 1}{\mathcal{}H}(a)=0.

Finally, let λ>0\lambda>0 denote the temperature parameter reflecting the trade-off between exploration and exploitation.

We can then describe the decision-maker’s optimal exploratory control problem V¯x;N,λ:=(V¯tx;N,λ)t∈[0,T]\overline{V}^{x;N,\lambda}:=(\overline{V}\_{t}^{x;N,\lambda})\_{t\in[0,T]} under ambiguity
for any N∈ℕN\in\mathbb{N} and λ>0\lambda>0:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | V¯tx;N,λ:=ess​supπ∈Π⁡Etg​[J¯tx;N,λ,π],for t∈[0,T],\displaystyle\overline{V}\_{t}^{x;N,\lambda}:=\operatorname\*{ess\,sup}\_{\pi\in\Pi}{\mathcal{}E}\_{t}^{g}[\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi}],\quad\mbox{for $t\in[0,T]$}, |  |

where for each π∈Π\pi\in\Pi, the integrand J¯tx;N,λ,π\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | J¯tx;N,λ,π:=\displaystyle\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi}:= | ∫tTe−∫ts(βu+N​πu)​𝑑u​(r​(Xsx)+R​(Xsx)​N​πs−λ​H​(πs))\displaystyle\int\_{t}^{T}e^{-\int\_{t}^{s}(\beta\_{u}+N\pi\_{u})du}\big(r(X\_{s}^{x})+R(X\_{s}^{x})\,N\pi\_{s}-\lambda{\mathcal{}H}(\pi\_{s})\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−∫tT(βu+N​πu)​𝑑u​R​(XTx),\displaystyle\quad+e^{-\int\_{t}^{T}(\beta\_{u}+N\pi\_{u})du}R(X\_{T}^{x}), |  |

where XxX^{x} is given in ([2.1](https://arxiv.org/html/2510.10260v1#S2.E1 "Equation 2.1 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and (βt)t∈[0,T](\beta\_{t})\_{t\in[0,T]} is the discount rate appearing in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

###### Remark 3.1.

We note that the differential entropy H{\mathcal{}H} given in ([3.1](https://arxiv.org/html/2510.10260v1#S3.E1 "Equation 3.1 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is strictly convex and bounded on [0,1][0,1]. Moreover, since all the exploratory control π∈Π\pi\in\Pi is uniformly bounded by [0,1][0,1], by using the same arguments presented for Remark [2.5](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), we have that J¯tx;N,λ,π∈L2​(FT;ℝ)\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi}\in L^{2}({\mathcal{}F}\_{T};\mathbb{R}) for all N∈ℕN\in\mathbb{N}, λ>0\lambda>0, and π∈Π\pi\in\Pi. Therefore, V¯x;N,λ\overline{V}^{x;N,\lambda} given in ([3.2](https://arxiv.org/html/2510.10260v1#S3.E2 "Equation 3.2 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is well-defined for all N∈ℕN\in\mathbb{N} and λ>0\lambda>0.

###### Remark 3.2.

Assume that the probability space (Ω,F,ℙ)(\Omega,{\mathcal{}F},\mathbb{P}) supports a uniformly distributed random variable UU with values in [0,1][0,1] which is independent of the fixed Brownian motion BB. Then we are able to see that each exploratory control π∈Π\pi\in\Pi generates a Bernoulli-distributed (randomized) process under drift ambiguity. Indeed, we recall the variational characterization of gg-expectation in Remark [2.2](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem2 "Remark 2.2. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") with the map g^:Ω×[0,T]×ℝd→ℝ\hat{g}:\Omega\times[0,T]\times\mathbb{R}^{d}\to\mathbb{R} and the set Bg{\mathcal{}B}^{g}. Then, for all N∈ℕN\in\mathbb{N}, λ>0\lambda>0, and t∈[0,T]t\in[0,T], we can rewrite the conditional gg-expectation value Etg​[J¯tx;N,λ,π]{\mathcal{}E}\_{t}^{g}[\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi}] given in ([3.2](https://arxiv.org/html/2510.10260v1#S3.E2 "Equation 3.2 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) as the following strong formulation for drift ambiguity under ℙ\mathbb{P} (see [[1](https://arxiv.org/html/2510.10260v1#bib.bib1), Section 5]):

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | Etg​[J¯tx;N,λ,π]=ess​infϑ∈Bg⁡𝔼t​[J¯tx;N,λ,π,ϑ+∫tTg^​(s,ϑs)​𝑑s],\displaystyle{\mathcal{}E}\_{t}^{g}[\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi}]=\operatorname\*{ess\,inf}\_{\vartheta\in{\mathcal{}B}^{g}}\mathbb{E}\_{t}[\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi,\vartheta}+\int\_{t}^{T}\hat{g}(s,\vartheta\_{s})ds], |  |

where for each π∈Π\pi\in\Pi and ϑ∈Bg\vartheta\in{\mathcal{}B}^{g}, the term J¯tx;N,λ,π,ϑ\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi,\vartheta} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | J¯tx;N,λ,π,ϑ:=\displaystyle\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi,\vartheta}:= | ∫tTe−∫ts(βu+N​πu)​𝑑u​(r​(Xsx;ϑ)+R​(Xsx;ϑ)​N​πs−λ​H​(πs))​𝑑s\displaystyle\int\_{t}^{T}e^{-\int\_{t}^{s}(\beta\_{u}+N\pi\_{u})du}\big(r(X\_{s}^{x;\vartheta})+R(X\_{s}^{x;\vartheta})\,N\pi\_{s}-\lambda{\mathcal{}H}(\pi\_{s})\big)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−∫tT(βu+N​πu)​𝑑u​R​(XTx;ϑ),\displaystyle\quad+e^{-\int\_{t}^{T}(\beta\_{u}+N\pi\_{u})du}R(X\_{T}^{x;\vartheta}), |  |

where (Xtx;ϑ)t∈[0,T](X^{x;\vartheta}\_{t})\_{t\in[0,T]} is given by Xtx;ϑ:=x+∫0t(bso+σso​ϑs)​𝑑s+∫0tσso​𝑑Bs,X\_{t}^{x;\vartheta}:=x+\int\_{0}^{t}\big(b^{o}\_{s}+\sigma\_{s}^{o}\vartheta\_{s}\big)ds+\int\_{0}^{t}\sigma^{o}\_{s}dB\_{s}, for t∈[0,T]t\in[0,T],
and (bo,σo)(b^{o},\sigma^{o}) are the baseline parameters appearing in ([2.1](https://arxiv.org/html/2510.10260v1#S2.E1 "Equation 2.1 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Then by using the random variable UU and its independence with the filtration 𝔽\mathbb{F} generated by BB, we can apply the Blackwell–Dubins lemma (see [[8](https://arxiv.org/html/2510.10260v1#bib.bib8)]) to ensure that there exists a (randomized) process (α~t)t∈[0,T](\widetilde{\alpha}\_{t})\_{t\in[0,T]} such that for every t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s.,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(α~t=1|Ft)=πt=1−ℙ​(α~t=0|Ft),\mathbb{P}(\widetilde{\alpha}\_{t}=1\,|\,{\mathcal{}F}\_{t})=\pi\_{t}=1-\mathbb{P}(\widetilde{\alpha}\_{t}=0\,|\,{\mathcal{}F}\_{t}), |  |

i.e., α~t\widetilde{\alpha}\_{t} is a Bernoulli distributed random variable with probability πt\pi\_{t} given Ft{\mathcal{}F}\_{t}.

In order to characterize V¯x;N,λ\overline{V}^{x;N,\lambda} given in ([3.2](https://arxiv.org/html/2510.10260v1#S3.E2 "Equation 3.2 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we first collect several preliminary results concerning the following auxiliary BSDE formulations: Recall that FxF^{x} is given in ([2.3](https://arxiv.org/html/2510.10260v1#S2.E3 "Equation 2.3 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Set for every π∈Π\pi\in\Pi and (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d}

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | F¯tx;N,λ,π​(ω,y,z):=Ftx​(ω,y,z)+N​(R​(Xtx​(ω))−y)​πt​(ω)−λ​H​(πt​(ω)).\displaystyle\overline{F}^{x;N,\lambda,\pi}\_{t}(\omega,y,z):=F^{x}\_{t}(\omega,y,z)+N(R\big(X\_{t}^{x}(\omega)\big)-y)\pi\_{t}(\omega)-\lambda{\mathcal{}H}(\pi\_{t}(\omega)). |  |

Then, consider the (controlled) processes (Y¯tx;N,λ,π,Z¯tx;N,λ,π)t∈[0,T](\overline{Y}\_{t}^{x;N,\lambda,\pi},\overline{Z}\_{t}^{x;N,\lambda,\pi})\_{t\in[0,T]} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | Y¯tx;N,λ,π=R​(XTx)+∫tTF¯sx;N,λ,π​(Y¯sx;N,λ,π,Z¯sx;N,λ,π)​𝑑s−∫tTZ¯sx;N,λ,π​𝑑Bs,\displaystyle\overline{Y}\_{t}^{x;N,\lambda,\pi}=R(X\_{T}^{x})+\int\_{t}^{T}\overline{F}\_{s}^{x;N,\lambda,\pi}(\overline{Y}\_{s}^{x;N,\lambda,\pi},\overline{Z}\_{s}^{x;N,\lambda,\pi})ds-\int\_{t}^{T}\overline{Z}\_{s}^{x;N,\lambda,\pi}dB\_{s}, |  |

###### Remark 3.3.

Under Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), the following statements hold for all π∈Π\pi\in\Pi, N∈ℕN\in\mathbb{N} and λ>0\lambda>0:

* (i)

  Since (πt)t∈[0,T]∈Π(\pi\_{t})\_{t\in[0,T]}\in\Pi and (H​(πt))t∈[0,T]({\mathcal{}H}(\pi\_{t}))\_{t\in[0,T]} are uniformly bounded (see Remark [3.1](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem1 "Remark 3.1. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we are able to see that the parameters of ([3.5](https://arxiv.org/html/2510.10260v1#S3.E5 "Equation 3.5 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfy all the conditions given in [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Section 3]. Therefore, there exists a unique solution (Y¯tx;N,λ,π,Z¯tx;N,λ,π)t∈[0,T]∈𝕊2​(ℝ)×𝕃2​(ℝd)(\overline{Y}\_{t}^{x;N,\lambda,\pi},\overline{Z}\_{t}^{x;N,\lambda,\pi})\_{t\in[0,T]}\in\mathbb{S}^{2}(\mathbb{R})\times\mathbb{L}^{2}(\mathbb{R}^{d}) to ([3.5](https://arxiv.org/html/2510.10260v1#S3.E5 "Equation 3.5 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).
* (ii)

  Since Y¯tx;N,λ,π∈L2​(Ft;ℝ)\overline{Y}\_{t}^{x;N,\lambda,\pi}\in L^{2}({\mathcal{}F}\_{t};\mathbb{R}) and J¯tx;N,λ,π∈L2​(FT;ℝ)\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi}\in L^{2}({\mathcal{}F}\_{T};\mathbb{R}) (see Remark [3.1](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem1 "Remark 3.1. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we can use the same arguments presented for Proposition [2.10](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") to have that

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.6) |  | Y¯tx;N,λ,π=Etg​[J¯tx;N,λ,π],ℙ-a.s. for all t∈[0,T].\displaystyle\overline{Y}\_{t}^{x;N,\lambda,\pi}={\mathcal{}E}\_{t}^{g}[\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi}],\quad\mbox{$\mathbb{P}$-a.s. for all $t\in[0,T]$}. |  |

Moreover, set for every N∈ℕN\in\mathbb{N}, λ>0\lambda>0, and (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d} by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.7) |  | F¯tx;N,λ​(ω,y,z):=Ftx​(ω,y,z)+Gtx;N,λ​(ω,y),where​Gtx;N,λ​(ω,y):=N​(R​(Xtx​(ω))−y)+λ​log⁡(e−Nλ​{R​(Xtx​(ω))−y}+1).\displaystyle\begin{aligned} &\overline{F}\_{t}^{x;N,\lambda}(\omega,y,z):=F\_{t}^{x}(\omega,y,z)+G\_{t}^{x;N,\lambda}(\omega,y),\\ &\;\;\mbox{where}\;\;G\_{t}^{x;N,\lambda}(\omega,y):=N\Big(R\big(X\_{t}^{x}(\omega)\big)-y\Big)+\lambda\log\Big(e^{-\frac{N}{\lambda}\{R(X\_{t}^{x}(\omega))-y\}}+1\Big).\end{aligned} |  |

Then consider the couple of processes (Y¯tx;N,λ,Z¯tx;N,λ)t∈[0,T](\overline{Y}\_{t}^{x;N,\lambda},\overline{Z}\_{t}^{x;N,\lambda})\_{t\in[0,T]} satisfying

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.8) |  | Y¯tx;N,λ=\displaystyle\overline{Y}\_{t}^{x;N,\lambda}= | R​(XTx)+∫tTF¯sx;N,λ​(Y¯sx;N,λ,Z¯sx;N,λ)​𝑑s−∫tTZ¯sx;N,λ​𝑑Bs.\displaystyle R(X\_{T}^{x})+\int\_{t}^{T}\overline{F}\_{s}^{x;N,\lambda}(\overline{Y}\_{s}^{x;N,\lambda},\overline{Z}\_{s}^{x;N,\lambda})ds-\int\_{t}^{T}\overline{Z}\_{s}^{x;N,\lambda}dB\_{s}. |  |

In the following theorem, the optimal exploratory control problem V¯x;N,λ\overline{V}^{x;N,\lambda} under ambiguity and its optimal control are characterized via the auxiliary BSDE given in ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

###### Theorem 3.4.

Suppose that Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") hold. Recall the logistic function logit⁡(⋅)\operatorname{logit}(\cdot) in ([1.3](https://arxiv.org/html/2510.10260v1#S1.E3 "Equation 1.3 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).
The following statements hold for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0.

* (i)

  There exists a unique solution (Y¯x;N,λ,Z¯x;N,λ)∈𝕊2​(ℝ)×𝕃2​(ℝd)(\overline{Y}^{x;N,\lambda},\overline{Z}^{x;N,\lambda})\in\mathbb{S}^{2}(\mathbb{R})\times\mathbb{L}^{2}(\mathbb{R}^{d}) of ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).
* (ii)

  Moreover, recall V¯x;N,λ\overline{V}^{x;N,\lambda} is given in ([3.2](https://arxiv.org/html/2510.10260v1#S3.E2 "Equation 3.2 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Then it holds for every t∈[0,T]t\in[0,T] that Y¯tx;N,λ=V¯tx;N,λ=Etg​[J¯tx;N,λ,π∗,x;N,λ]\overline{Y}\_{t}^{x;N,\lambda}=\overline{V}\_{t}^{x;N,\lambda}={\mathcal{}E}\_{t}^{g}[\overline{\operatorname{J}}\_{t}^{x;N,\lambda,\pi^{\*,x;N,\lambda}}] ℙ\mathbb{P}-a.s., where the optimizer π∗,x;N,λ:=(πt∗,x;N,λ)t∈[0,T]∈Π\pi^{\*,x;N,\lambda}:=(\pi^{\*,x;N,\lambda}\_{t})\_{t\in[0,T]}\in\Pi is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.9) |  | πt∗,x;N,λ:=logit⁡(Nλ​(R​(Xtx)−Y¯tx;N,λ)),t∈[0,T].\displaystyle\pi^{\*,x;N,\lambda}\_{t}:=\operatorname{logit}\Big(\frac{N}{\lambda}(R(X\_{t}^{x})-\overline{Y}\_{t}^{x;N,\lambda})\Big),\quad t\in[0,T]. |  |

The following theorem is devoted to showing the comparison and stability results between the exploratory and non-exploratory optimal control problems characterized in Proposition [2.10](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

###### Theorem 3.5.

Suppose that Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") hold. For each N∈ℕN\in\mathbb{N} and λ>0\lambda>0, let (Yx;N,Zx;N)(Y^{x;N},Z^{x;N}) and (Y¯x;N,λ,Z¯x;N,λ)(\overline{Y}^{x;N,\lambda},\overline{Z}^{x;N,\lambda}) be the unique solution to the BSDEs ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), respectively. Then it holds that for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.10) |  | Ytx;N≤Y¯tx;N,λ,ℙ-a.s., for all t≥0,\displaystyle Y\_{t}^{x;N}\leq\overline{Y}\_{t}^{x;N,\lambda},\quad\mbox{$\mathbb{P}$-a.s., for all $t\geq 0$, } |  |

In particular, there exists some constant C>0C>0 (that does not depend on N∈ℕN\in\mathbb{N} and λ>0\lambda>0 but on T>0T>0) such that for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.11) |  | ‖Yx;N−Y¯x;N,λ‖𝕊2+‖Zx;N−Z¯x;N,λ‖𝕃2≤C​λ,\displaystyle\|Y^{x;N}-\overline{Y}^{x;N,\lambda}\|\_{\mathbb{S}^{2}}+\|Z^{x;N}-\overline{Z}^{x;N,\lambda}\|\_{\mathbb{L}^{2}}\leq C\lambda, |  |

This implies that for any N∈ℕN\in\mathbb{N}, Y¯x;N,λ\overline{Y}^{x;N,\lambda} strongly converges to Yx;NY^{x;N} in 𝕊2​(ℝ)\mathbb{S}^{2}(\mathbb{R}), as λ↓0\lambda\downarrow 0.

As a consequence of Theorem [3.5](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), the following corollary establishes the asymptotic behavior of the optimal exploratory control derived in Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") into the optimal non-exploratory control derived in Proposition [2.10](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

###### Corollary 3.6.

Suppose that Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") hold. For each N∈ℕN\in\mathbb{N} and λ>0\lambda>0, let α∗,x;N∈A\alpha^{\*,x;N}\in{\mathcal{}A} and π∗,x;N,λ∈Π\pi^{\*,x;N,\lambda}\in\Pi be defined as in ([2.8](https://arxiv.org/html/2510.10260v1#S2.E8 "Equation 2.8 ‣ Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([3.9](https://arxiv.org/html/2510.10260v1#S3.E9 "Equation 3.9 ‣ item (ii) ‣ Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), respectively. Then it holds that for every N∈ℕN\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
| (3.12) |  | ‖α∗,x;N−π∗,x;N,λ‖𝕃1→0as λ↓0,\displaystyle\big\|\alpha^{\*,x;N}-\pi^{\*,x;N,\lambda}\big\|\_{\mathbb{L}^{1}}\to 0\quad\mbox{as $\lambda\downarrow 0$}, |  |

i.e., for any N∈ℕN\in\mathbb{N}, π∗,x;N,λ\pi^{\*,x;N,\lambda} strongly converges to α∗,x;N\alpha^{\*,x;N} in the set of all 𝔽\mathbb{F} progressively measurable processes endowed with the norm ∥⋅∥𝕃1\|\cdot\|\_{\mathbb{L}^{1}}, as λ↓0\lambda\downarrow 0.

## 4 Policy iteration theorem & RL algorithm

A typical RL approach to finding the optimal strategy is based on policy iteration, where the strategy is successively refined through iterative updates. In this section, we establish the policy iteration theorem based on the verification result in Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), and then provide the corresponding reinforcement learning algorithm.

Throughout this section, we fix a sufficiently large N∈ℕN\in\mathbb{N} and a small λ>0\lambda>0 so that Y¯x;N,λ\overline{Y}^{x;N,\lambda} serves as an accurate approximation of YxY^{x} (see Remark [2.9](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem9 "Remark 2.9. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and Theorem [3.5](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). The proofs of all theorems in this section can be found in Section [6.3](https://arxiv.org/html/2510.10260v1#S6.SS3 "6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

For any πn∈Π\pi^{n}\in\Pi and n∈ℕn\in\mathbb{N}, denote by (Y¯x;N,λ,πn,Z¯x;N,λ,πn)∈𝕊2​(ℝ)×𝕃2​(ℝd)(\overline{Y}^{x;N,\lambda,\pi^{n}},\overline{Z}^{x;N,\lambda,\pi^{n}})\in\mathbb{S}^{2}(\mathbb{R})\times\mathbb{L}^{2}(\mathbb{R}^{d}) the unique solution of ([3.5](https://arxiv.org/html/2510.10260v1#S3.E5 "Equation 3.5 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) under the exploratory control πn\pi^{n} (see Remark [3.3](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem3 "Remark 3.3. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i)).
Recall the logistic function logit⁡(⋅)\operatorname{logit}(\cdot) in ([1.3](https://arxiv.org/html/2510.10260v1#S1.E3 "Equation 1.3 ‣ 1 Introduction ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).
Then one can construct πn+1∈Π\pi^{n+1}\in\Pi as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | πtn+1:=logit⁡(Nλ​(R​(Xtx)−Y¯tx;N,λ,πn)),t∈[0,T].\displaystyle\pi^{n+1}\_{t}:=\operatorname{logit}(\frac{N}{\lambda}(R(X\_{t}^{x})-\overline{Y}\_{t}^{x;N,\lambda,\pi^{n}})),\quad t\in[0,T]. |  |

###### Theorem 4.1.

Suppose that Assumptions [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") hold. Let Y¯x;N,λ\overline{Y}^{x;N,\lambda} be the first component of the unique solution of ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (see Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Let π1∈Π\pi^{1}\in\Pi be given. Let (Y¯x;N,λ,π1,Z¯x;N,λ,π1)(\overline{Y}^{x;N,\lambda,\pi^{1}},\overline{Z}^{x;N,\lambda,\pi^{1}}) be the unique solution of ([3.5](https://arxiv.org/html/2510.10260v1#S3.E5 "Equation 3.5 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) under π1\pi^{1}. For every n∈ℕn\in\mathbb{N}, let πn+1\pi^{n+1} be defined iteratively according to ([4.1](https://arxiv.org/html/2510.10260v1#S4.E1 "Equation 4.1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and let (Y¯x;N,λ,πn+1,Z¯x;N,λ,πn+1)(\overline{Y}^{x;N,\lambda,\pi^{n+1}},\overline{Z}^{x;N,\lambda,\pi^{n+1}}) be the unique solution of ([3.5](https://arxiv.org/html/2510.10260v1#S3.E5 "Equation 3.5 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) under πn+1\pi^{n+1}. Then the following hold for every n∈ℕn\in\mathbb{N}:

* (i)

  Y¯tx;N,λ≥Y¯tx;N,λ,πn+1≥Y¯tx;N,λ,πn\overline{Y}\_{t}^{x;N,\lambda}\geq\overline{Y}\_{t}^{x;N,\lambda,\pi^{n+1}}\geq\overline{Y}\_{t}^{x;N,\lambda,\pi^{n}}, ℙ\mathbb{P}-a.s., for all t∈[0,T]t\in[0,T];
* (ii)

  Set Δ​(x;N,λ,π1):=‖Y¯x;N,λ−Y¯x;N,λ,π1‖𝕊22\Delta({x;N,\lambda,\pi^{1}}):=\|\overline{Y}^{x;N,\lambda}-\overline{Y}^{x;N,\lambda,\pi^{1}}\|\_{\mathbb{S}^{2}}^{2}. There exists some constant C>0{C}>0 (that depends on N,T,dN,T,d but not on n,λn,\lambda) such that

  |  |  |  |
  | --- | --- | --- |
  |  | ‖Y¯x;N,λ−Y¯x;N,λ,πn+1‖𝕊22+‖Z¯x;N,λ−Z¯x;N,λ,πn+1‖𝕃22≤Cnn!​Δ​(x;N,λ,π1),\displaystyle\|\overline{Y}^{x;N,\lambda}-\overline{Y}^{x;N,\lambda,\pi^{n+1}}\|\_{\mathbb{S}^{2}}^{2}+\|\overline{Z}^{x;N,\lambda}-\overline{Z}^{x;N,\lambda,\pi^{n+1}}\|\_{\mathbb{L}^{2}}^{2}\leq\frac{{C}^{n}}{n!}\Delta({x;N,\lambda,\pi^{1}}), |  |
  |  |  |  |
  | --- | --- | --- |
  |  | ‖πn+1−π∗‖𝕊22≤Nλ​Cn−1(n−1)!​Δ​(x;N,λ,π1).\displaystyle\|{\pi}^{n+1}-{\pi}^{\*}\|\_{\mathbb{S}^{2}}^{2}\leq\frac{N}{\lambda}\frac{{C}^{n-1}}{(n-1)!}\Delta({x;N,\lambda,\pi^{1}}). |  |

In particular, Y¯tx;N,λ,πn↑Y¯tx;N,λ\overline{Y}^{x;N,\lambda,\pi^{n}}\_{t}\uparrow\overline{Y}^{x;N,\lambda}\_{t} and πtn↑πt∗\pi^{n}\_{t}\uparrow\pi^{\*}\_{t} ℙ\mathbb{P}-a.s. for all t∈[0,T]t\in[0,T] as n→∞n\to\infty.

Let us mention some Markovian properties of the BSDEs arising in the policy iteration result given in Theorem [4.1](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), as well as how these properties can be leveraged to implement the policy iteration algorithm using neural networks.
To that end, in the remainder of this section, we consider the following specification:
{setting}

* (i)

  The map gg given in Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") is deterministic, i.e., for every ω1,ω2∈Ω\omega^{1},\omega^{2}\in\Omega, g​(ω1,⋅,⋅)=g​(ω2,⋅,⋅)g(\omega^{1},\cdot,\cdot)=g(\omega^{2},\cdot,\cdot).
* (ii)

  The baseline parameters bob^{o} and σo\sigma^{o} appearing in ([2.1](https://arxiv.org/html/2510.10260v1#S2.E1 "Equation 2.1 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) are of the form given in Remark [2.3](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem3 "Remark 2.3. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii), so that Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") holds.
* (iii)

  The reward functions RR and rr satisfy all the conditions in Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i). Furthermore, rr is continuous. Lastly, the discount rate process (βt)t∈[0,T](\beta\_{t})\_{t\in[0,T]} is deterministic and bounded by the constant Cβ>0C\_{\beta}>0 in Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii).

Denote by Πˇ\check{\Pi} the set of all Borel measurable maps
πˇ:[0,T]×ℝd∋(t,x~)→πˇt​(x~)∈[0,1],\check{\pi}:[0,T]\times\mathbb{R}^{d}\ni(t,\tilde{x})\to\check{\pi}\_{t}(\tilde{x})\in[0,1],
so that πˇ​(Xx):=(πˇt​(Xtx))t∈[0,T]∈Π\check{\pi}(X^{x}):=(\check{\pi}\_{t}(X\_{t}^{x}))\_{t\in[0,T]}\in\Pi, i.e., Πˇ\check{\Pi} is the closed loop policy set.

Under Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."),
set for every πˇ∈Πˇ\check{\pi}\in\check{\Pi} and (t,x~,y,z)∈[0,T]×ℝd×ℝ×ℝd(t,\tilde{x},y,z)\in[0,T]\times\mathbb{R}^{d}\times\mathbb{R}\times\mathbb{R}^{d},

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | FˇtN,λ;πˇ​(x~,y,z):=r​(x~)−βt​y+g​(t,z)+N​(R​(x~)−y)​πˇt​(x~)−λ​ℋ​(πˇt​(x~)),\displaystyle\check{F}\_{t}^{N,\lambda;\check{\pi}}(\tilde{x},y,z):=r(\tilde{x})-\beta\_{t}y+g(t,z)+N(R(\tilde{x})-y)\check{\pi}\_{t}(\tilde{x})-\lambda\mathcal{H}\big(\check{\pi}\_{t}(\tilde{x})\big), |  |

so that (FˇtN,λ,πˇ​(⋅,⋅,⋅))t∈[0,T](\check{F}\_{t}^{N,\lambda,\check{\pi}}(\cdot,\cdot,\cdot))\_{t\in[0,T]} is deterministic and Fˇ⋅N,λ,πˇ​(⋅,⋅,⋅)\check{F}\_{\cdot}^{N,\lambda,\check{\pi}}(\cdot,\cdot,\cdot) is Borel measurable.

###### Remark 4.2.

Under Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), recall (Y¯x;N,λ,Z¯x;N,λ)(\overline{Y}^{x;N,\lambda},\overline{Z}^{x;N,\lambda}) satisfying ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")); see also Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Then set for every (t,x~,y,z)∈[0,T]×ℝd×ℝ×ℝd(t,\tilde{x},y,z)\in[0,T]\times\mathbb{R}^{d}\times\mathbb{R}\times\mathbb{R}^{d}

|  |  |  |
| --- | --- | --- |
|  | FˇtN,λ​(x~,y,z):=r​(x~)−βt​y+g​(t,z)+N​(R​(x~)−y)+λ​log⁡(e−Nλ​{R​(x~)−y}+1).\displaystyle\check{F}\_{t}^{N,\lambda}(\tilde{x},y,z):=r(\tilde{x})-\beta\_{t}y+g(t,z)+N(R(\tilde{x})-y)+\lambda\log(e^{-\frac{N}{\lambda}\{R(\tilde{x})-y\}}+1). |  |

Clearly, FˇtN,λ​(Xtx,y,z)=F¯tx;N,λ​(y,z)\check{F}\_{t}^{N,\lambda}(X\_{t}^{x},y,z)=\overline{F}^{x;N,\lambda}\_{t}(y,z) for (t,x,y,z)∈[0,T]×ℝd×ℝ×ℝd(t,x,y,z)\in[0,T]\times\mathbb{R}^{d}\times\mathbb{R}\times\mathbb{R}^{d}; see ([3.7](https://arxiv.org/html/2510.10260v1#S3.E7 "Equation 3.7 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Moreover, Fˇ⋅N,λ​(⋅,⋅,⋅)\check{F}\_{\cdot}^{N,\lambda}(\cdot,\cdot,\cdot) and R​(⋅)R(\cdot) satisfy the conditions (M1b) and (M1bc\textrm{M1b}^{c}) given in [[19](https://arxiv.org/html/2510.10260v1#bib.bib19)]. Therefore, an application of [[19](https://arxiv.org/html/2510.10260v1#bib.bib19), Theorem 8.12] ensures the existence of a viscosity solution222We refer to [[19](https://arxiv.org/html/2510.10260v1#bib.bib19), Definition 8.11] for the definition of a viscosity solution of ([4.3](https://arxiv.org/html/2510.10260v1#S4.E3 "Equation 4.3 ‣ Remark 4.2. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) with setting the terminal condition R↷ΨR\curvearrowright\Psi and the generator Fˇ⋅N,λ↷g\check{F}^{N,\lambda}\_{\cdot}\curvearrowright g therein. vˇN,λ\check{v}^{N,\lambda} of the following PDE:,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | (∂tv+ℒ​v)​(t,x)+FˇtN,λ​(x,v​(t,x),((σ~o)⊤​∇v)​(t,x))=0​(t,x)∈[0,T)×ℝd,\displaystyle(\partial\_{t}v+\mathcal{L}v)(t,x)+\check{F}^{N,\lambda}\_{t}\big(x,v(t,x),((\widetilde{\sigma}^{o})^{\top}\nabla v)(t,x)\big)=0\;\;\;(t,x)\in[0,T)\times\mathbb{R}^{d}, |  |

with v​(T,⋅)=R​(⋅)v(T,\cdot)=R(\cdot), where the infinitesimal operator ℒ\mathcal{L} of XxX^{x} under the measure ℙ\mathbb{P} is given by ℒ​v​(t,x):=12​∑i,j=1d((σ~o)⊤​σ~o​(t,x))i,j​∂2v​(t,x)∂xi​∂xj+∑i=1db~io​(t,x)​∂v​(t,x)∂xi\mathcal{L}v(t,x):=\frac{1}{2}\sum\_{i,j=1}^{d}((\widetilde{\sigma}^{o})^{\top}\widetilde{\sigma}^{o}(t,x))\_{i,j}\frac{\partial^{2}v(t,x)}{\partial x\_{i}\partial x\_{j}}+\sum\_{i=1}^{d}\widetilde{b}^{o}\_{i}(t,x)\frac{\partial v(t,x)}{\partial x\_{i}}. In particular, it holds that Y¯tx;N,λ=vˇN,λ​(t,Xtx)\overline{Y}\_{t}^{x;N,\lambda}=\check{v}^{N,\lambda}(t,X\_{t}^{x}), ℙ⊗d​t\mathbb{P}\otimes dt-a.e., for all t∈[0,T]t\in[0,T].

We now have a sequence of closed-loop policies in Πˇ\check{\Pi} deriving the policy iteration.

###### Corollary 4.3.

Under Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), let πˇ1∈Πˇ\check{\pi}^{1}\in\check{\Pi} be given.

* (i)

  There exists two sequences of Borel measurable functions (vN,λ,n)n∈ℕ(v^{N,\lambda,n})\_{n\in\mathbb{N}} and (wN,λ,n)n∈ℕ(w^{N,\lambda,n})\_{n\in\mathbb{N}} defined on [0,T]×ℝd[0,T]\times\mathbb{R}^{d} (having values in ℝ\mathbb{R} and ℝd\mathbb{R}^{d}, respectively) such that for every n∈ℕn\in\mathbb{N} and every t∈[0,T]t\in[0,T], ℙ⊗d​t\mathbb{P}\otimes dt-a.e.,

  |  |  |  |
  | --- | --- | --- |
  |  | Y¯tx;N,λ,πˇn​(Xx)=vN,λ,n​(t,Xtx),Z¯sx;N,λ,πˇn​(Xx)=((σ~o)⊤​wN,λ,n)​(t,Xtx),\displaystyle\overline{Y}\_{t}^{x;N,\lambda,\check{\pi}^{n}(X^{x})}=v^{N,\lambda,n}(t,X\_{t}^{x}),\qquad\overline{Z}\_{s}^{x;N,\lambda,\check{\pi}^{n}(X^{x})}=\big((\widetilde{\sigma}^{o})^{\top}w^{N,\lambda,n}\big)(t,X\_{t}^{x}), |  |

  with πˇn​(Xx):=(πˇtn​(Xtx))t∈[0,T]∈Π\check{\pi}^{n}(X^{x}):=(\check{\pi}^{n}\_{t}(X\_{t}^{x}))\_{t\in[0,T]}\in\Pi, where for any n≥2n\geq 2, πˇn∈Πˇ\check{\pi}^{n}\in\check{\Pi} is defined iteratively as for (t,x~)∈[0,T]×ℝd(t,\tilde{x})\in[0,T]\times\mathbb{R}^{d}

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (4.4) |  | πˇtn​(x~):=logit⁡(Nλ​(R​(x~)−vN,λ,n−1​(t,x~))).\displaystyle\check{\pi}^{n}\_{t}(\tilde{x}):=\operatorname{logit}\Big(\frac{N}{\lambda}\big(R(\tilde{x})-v^{N,\lambda,n-1}(t,\tilde{x})\big)\Big). |  |
* (ii)

  If πˇt1​(⋅)\check{\pi}\_{t}^{1}(\cdot) is continuous on ℝd\mathbb{R}^{d} for any t∈[0,T]t\in[0,T], one can find a sequence of functions (vN,λ,n)n∈ℕ(v^{N,\lambda,n})\_{n\in\mathbb{N}} which satisfies all the properties given in (i) and each vN,λ,nv^{N,\lambda,n}, n∈ℕn\in\mathbb{N}, is a viscosity solution of the following PDE:

  |  |  |  |
  | --- | --- | --- |
  |  | (∂tv+ℒ​v)​(t,x)+FˇtN,λ,πˇn​(x,v​(t,x),((σ~o)⊤​∇v)​(t,x))=0​(t,x)∈[0,T)×ℝd,(\partial\_{t}v+\mathcal{L}v)(t,x)+\check{F}^{N,\lambda,\check{\pi}^{n}}\_{t}(x,v(t,x),((\widetilde{\sigma}^{o})^{\top}\nabla v)(t,x))=0\;\;\;(t,x)\in[0,T)\times\mathbb{R}^{d}, |  |

  with v​(T,⋅)=R​(⋅)v(T,\cdot)=R(\cdot), where πˇn∈Πˇ\check{\pi}^{n}\in\check{\Pi} is defined iteratively as in ([4.4](https://arxiv.org/html/2510.10260v1#S4.E4 "Equation 4.4 ‣ item (i) ‣ Corollary 4.3. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

The core logic of the policy iteration given in
Theorem [4.1](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and Corollary [4.3](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") consists of two steps at each iteration. The first is the policy update, given in ([4.1](https://arxiv.org/html/2510.10260v1#S4.E1 "Equation 4.1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) or ([4.4](https://arxiv.org/html/2510.10260v1#S4.E4 "Equation 4.4 ‣ item (i) ‣ Corollary 4.3. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). The second is the policy evaluation, which corresponds to derive either the solution (Y¯x;N,λ,πn,Z¯x;N,λ,πn)(\overline{Y}^{x;N,\lambda,\pi^{n}},\overline{Z}^{x;N,\lambda,\pi^{n}}) of the BSDE ([3.5](https://arxiv.org/html/2510.10260v1#S3.E5 "Equation 3.5 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) under the updated policy πn\pi^{n}, or equivalently, the solution vN,λ,nv^{N,\lambda,n} of the PDE under πˇn\check{\pi}^{n} as given in Corollary [4.3](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii).

In what follows, we develop an RL scheme, relying on the deep splitting method of Beck et al. [[5](https://arxiv.org/html/2510.10260v1#bib.bib5)] and Frey and Köck [[25](https://arxiv.org/html/2510.10260v1#bib.bib25)], to implement the policy evaluation step at each iteration. For this purpose, we first introduce some notation, omitting the dependence on (N,λ)(N,\lambda) (even though the objects still depend on them).

{setting}

Denote by I∈ℕI\in\mathbb{N} the number of steps in the time discretization and denote by Θ⊂ℝp\Theta\subset\mathbb{R}^{p} (with some p∈ℕp\in\mathbb{N}) the parameter spaces for neural networks in.

1. (i)

   Let ti=i​Δ​tt\_{i}=i\Delta t and Δ​Bi:=Bti+1−Bti\Delta B\_{i}:=B\_{t\_{i+1}}-B\_{t\_{i}} for i={0,…,I−1}i=\{0,\dots,I-1\} with Δ​t:=T/I\Delta t:=T/I. Then the Euler scheme of ([2.1](https://arxiv.org/html/2510.10260v1#S2.E1 "Equation 2.1 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) under Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii) is given by: Xˇ0x:=x\check{X}^{x}\_{0}:=x,

   |  |  |  |
   | --- | --- | --- |
   |  | Xˇi+1x:=Xˇix+b~o​(ti,Xˇix)​Δ​t+σ~o​(ti,Xˇix)​Δ​Bi,i∈{0,…,I−1}.\displaystyle\check{X}^{x}\_{i+1}:=\check{X}^{x}\_{i}+\widetilde{b}^{o}(t\_{i},\check{X}^{x}\_{i})\Delta t+\widetilde{\sigma}^{o}(t\_{i},\check{X}^{x}\_{i})\Delta B\_{i},\quad i\in\{0,\ldots,I-1\}. |  |
2. (ii)

   The initial closed-loop policy πˇ1\check{\pi}^{1} is given by πˇi1​(⋅):=logit⁡(Nλ​(R​(⋅)−vi0​(⋅)))\check{\pi}^{1}\_{i}(\cdot):=\operatorname{logit}(\frac{N}{\lambda}(R(\cdot)-v^{0}\_{i}(\cdot))), i∈{0,…,I−1}i\in\{0,\dots,I-1\},
   with some function (at least continuous) vi0:ℝd→ℝv^{0}\_{i}:\mathbb{R}^{d}\to\mathbb{R}.
3. (iii)

   For each n∈ℕn\in\mathbb{N} and i∈{0,…,I−1}i\in\{0,\dots,I-1\}, let vin​(⋅;ϑin):ℝd→ℝv\_{i}^{n}(\,\cdot\,;\vartheta^{n}\_{i}):\mathbb{R}^{d}\to\mathbb{R}
   be neural realizations of vN,λ,n​(ti,⋅)v^{N,\lambda,n}(t\_{i},\cdot)
   parameterized by ϑin∈Θ\vartheta^{n}\_{i}\in\Theta (e.g., feed-forward networks (FNNs) with C1C^{1}-regularity or Lipschitz continuous with weak derivative).
4. (vi)

   For each n∈ℕn\in\mathbb{N}, the time-discretized, n+1n+1-th updated, closed-loop policy πˇn+1​(⋅;ϑin)\check{\pi}^{n+1}(\cdot;\vartheta\_{i}^{n}) (that depends on the parameter ϑin\vartheta^{n}\_{i} appearing in (iii)) is given by
   πˇin+1​(⋅;ϑin):=logit⁡(Nλ​(R​(⋅)−vin​(⋅;ϑin)))\check{\pi}^{n+1}\_{i}(\cdot;\vartheta\_{i}^{n}):=\operatorname{logit}(\frac{N}{\lambda}(R(\cdot)-v^{n}\_{i}(\cdot;\vartheta^{n}\_{i}))), i∈{0,…,I−1}.i\in\{0,\dots,I-1\}.
5. (v)

   For each n∈ℕn\in\mathbb{N}, set for every (x~,y,z)∈ℝd×ℝ×ℝd(\tilde{x},y,z)\in\mathbb{R}^{d}\times\mathbb{R}\times\mathbb{R}^{d},

   |  |  |  |
   | --- | --- | --- |
   |  | Fˇin​(x~,y,z;ϑin−1):=r​(x~)−βti​y+g​(t,z)+N​(R​(x~)−y)​πˇin​(x~;ϑin−1)−λ​ℋ​(πˇin​(x~;ϑin−1)),\displaystyle\begin{aligned} \check{F}\_{i}^{n}(\tilde{x},y,z;\vartheta\_{i}^{n-1})&:=r(\tilde{x})-\beta\_{t\_{i}}y+g(t,z)+N(R(\tilde{x})-y)\check{\pi}\_{i}^{n}(\tilde{x};\vartheta\_{i}^{n-1})\\ &\qquad-\lambda\mathcal{H}\big(\check{\pi}\_{i}^{n}(\tilde{x};\vartheta\_{i}^{n-1})\big),\end{aligned} |  |

   with the convention that πˇ1​(⋅;ϑi0)≡πˇi1​(⋅)\check{\pi}^{1}(\cdot;\vartheta\_{i}^{0})\equiv\check{\pi}\_{i}^{1}(\cdot) for any ϑi0∈Θ\vartheta\_{i}^{0}\in\Theta (see (ii)) so that Fˇi1​(⋅,⋅,⋅)\check{F}^{1}\_{i}(\cdot,\cdot,\cdot) is not parametrized over Θ\Theta but depends only on the form πˇi1\check{\pi}\_{i}^{1}.

To apply the deep splitting method, one needs σ~o​(ti,Xˇix)\widetilde{\sigma}^{o}(t\_{i},\check{X}^{x}\_{i}) in the loss function calculation (given in ([4.6](https://arxiv.org/html/2510.10260v1#S4.E6 "Equation 4.6 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))), which is unknown to an RL agent before learning the environment but can be learned from from the realized quadratic covariance of observed data333The mapping ℝd×d∋A↦A12∈ℝd×d\mathbb{R}^{d\times d}\ni A\mapsto A^{\frac{1}{2}}\in\mathbb{R}^{d\times d} denotes the symmetric positive-definite square root of a positive semidefinite matrix AA.

|  |  |  |
| --- | --- | --- |
|  | Σ​(Xˇi:i+1x):=1Δ​t​((Xˇi+1x−Xˇix)​(Xˇi+1x−Xˇix)⊤)12,\Sigma({\check{X}^{x}\_{i:i+1}}):=\frac{1}{\sqrt{\Delta t}}\big((\check{X}^{x}\_{i+1}-\check{X}^{x}\_{i})(\check{X}^{x}\_{i+1}-\check{X}^{x}\_{i})^{\top}\big)^{\frac{1}{2}}, |  |

so that Σ​(Xˇi:i+1x)​Σ​(Xˇi:i+1x)⊤​Δ​t→σ~o​(ti,Xˇix)​σ~o​(ti,Xˇix)⊤​Δ​t\Sigma({\check{X}^{x}\_{i:i+1}})\Sigma({\check{X}^{x}\_{i:i+1}})^{\top}\Delta t\to\widetilde{\sigma}^{o}(t\_{i},\check{X}^{x}\_{i})\widetilde{\sigma}^{o}(t\_{i},\check{X}^{x}\_{i})^{\top}\Delta t as Δ​t↓0\Delta t\downarrow 0 in probability ℙ\mathbb{P}; see e.g., [[34](https://arxiv.org/html/2510.10260v1#bib.bib34), Chapter I, Theorem 4.47] and [[56](https://arxiv.org/html/2510.10260v1#bib.bib56), Section 6, Theorem 22].

Algorithm 1  Policy iteration algorithm

0: Batch size M∈ℕM\in\mathbb{N}; Number of policy iterations n¯∈ℕ\overline{n}\in\mathbb{N}; Number of epochs ℓ¯∈ℕ\overline{\ell}\in\mathbb{N} for policy evaluation; Learning rate α∈(0,1)\alpha\in(0,1).

1: Set the initial closed loop policy πˇi1​(⋅)\check{\pi}^{1}\_{i}(\cdot), i∈{0,…,I−1}i\in\{0,\ldots,I-1\}, as in Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii).

2: Initialize ϑi0,∗∈Θ\vartheta\_{i}^{0,\*}\in\Theta, i∈{0,1,…,I}i\in\{0,1,\dots,I\}.

3: for n=1,…,n¯n=1,\ldots,\bar{n} do

4:  Initialize ϑin∈Θ\vartheta^{n}\_{i}\in\Theta, i∈{0,…,I−1}i\in\{0,\ldots,I-1\}, and ϑIn,∗∈Θ\vartheta\_{I}^{n,\*}\in\Theta.

5:  for l=1,…,ℓ¯l=1,\ldots,\bar{\ell} do

6:   Generate MM trajectories of (Xˇix)i=0I(\check{X}^{x}\_{i})\_{i=0}^{I}; see Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i).

7:   for i=I−1,…,0i=I-1,\ldots,0 do

8:    Minimize ([4.6](https://arxiv.org/html/2510.10260v1#S4.E6 "Equation 4.6 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) over ϑin∈Θ\vartheta^{n}\_{i}\in\Theta by using SGD with learning rate α\alpha.

9:   end for

10:  end for

11:  Denote by ϑin,∗\vartheta^{n,\*}\_{i} the lastly updated parameters at tit\_{i}, i∈{0,…,I−1}i\in\{0,\ldots,I-1\}.

12: end for

With all this notation set in place, for each iteration n∈ℕn\in\mathbb{N}, we present the policy evaluation as the following iterative minimization problem: for i∈{0,…,I−1}i\in\{0,\dots,I-1\}

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | ϑin,∗∈arg​minϑin∈Θ⁡𝔏n​(ϑin;ϑin−1,∗,ϑi+1n,∗),\displaystyle\vartheta^{n,\*}\_{i}\in\operatorname\*{arg\,min}\_{\vartheta^{n}\_{i}\in\Theta}\mathfrak{L}^{n}(\vartheta^{n}\_{i};\vartheta\_{i}^{n-1,\*},\vartheta\_{i+1}^{n,\*}), |  |

where 𝔏in​(⋅;ϑin−1,∗,ϑi+1n,∗):Θ→ℝ\mathfrak{L}\_{i}^{n}(\cdot;\vartheta\_{i}^{n-1,\*},\vartheta\_{i+1}^{n,\*}):\Theta\to\mathbb{R} is the (parameterized) L2L^{2}-loss function given by

|  |  |  |
| --- | --- | --- |
|  | 𝔏n(ϑin;ϑin−1,∗,ϑi+1n,∗):=𝔼[|vi+1n(Xˇi+1x;ϑi+1n,∗)−vin(Xˇix;ϑin)\displaystyle\mathfrak{L}^{n}(\vartheta^{n}\_{i};\vartheta\_{i}^{n-1,\*},\vartheta\_{i+1}^{n,\*}):=\mathbb{E}\Big[\big|v^{n}\_{i+1}(\check{X}^{x}\_{i+1};\vartheta^{n,\*}\_{i+1})-v^{n}\_{i}(\check{X}^{x}\_{i};\vartheta^{n}\_{i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | +Fˇin(Xˇi+1x,vi+1n(Xˇi+1x;θi+1n,∗),Σ(Xˇi:i+1x)∇vi+1n(Xˇi+1x;θi+1n,∗);ϑin−1,∗)Δt|2],\displaystyle\quad\quad+\check{F}^{n}\_{i}\big(\check{X}^{x}\_{i+1},v^{n}\_{i+1}(\check{X}^{x}\_{i+1};\theta^{n,\*}\_{i+1}),\Sigma({\check{X}^{x}\_{i:i+1}})\nabla v^{n}\_{i+1}(\check{X}^{x}\_{i+1};\theta^{n,\*}\_{i+1});\vartheta\_{i}^{n-1,\*}\big)\Delta t\big|^{2}\Big], |  |

with the convention that vIn​(XˇIx;ϑIn,∗):=R​(XˇIx){v}^{n}\_{I}(\check{X}\_{I}^{x};\vartheta\_{I}^{n,\*}):=R(\check{X}\_{I}^{x}) with an arbitrary ϑIn,∗∈Θ\vartheta\_{I}^{n,\*}\in\Theta, and that Fˇi1\check{F}^{1}\_{i} is not parametrized over Θ\Theta (see Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (v); hence ϑi0,∗∈Θ\vartheta\_{i}^{0,\*}\in\Theta is also an arbitrary).

We numerically solve the problem given in ([4.5](https://arxiv.org/html/2510.10260v1#S4.E5 "Equation 4.5 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) by using stochastic gradient descent (SGD) algorithms (see, e.g., [[28](https://arxiv.org/html/2510.10260v1#bib.bib28), Section 4.3]). Then we provide a pseudo-code in Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") to show how the policy iteration can be implemented.

###### Remark 4.4.

Note that the deep splitting method of [[5](https://arxiv.org/html/2510.10260v1#bib.bib5), [25](https://arxiv.org/html/2510.10260v1#bib.bib25)] is not the only neural realization of our policy evaluation; instead deep BSDEs / PDEs schemes of [[30](https://arxiv.org/html/2510.10260v1#bib.bib30), [33](https://arxiv.org/html/2510.10260v1#bib.bib33), [62](https://arxiv.org/html/2510.10260v1#bib.bib62)] can be an alternative. More recently, several articles, including [[27](https://arxiv.org/html/2510.10260v1#bib.bib27), [46](https://arxiv.org/html/2510.10260v1#bib.bib46)], provide the error analyses for such methods. To obtain a full error-analysis of our policy iteration algorithm, one would need to relax the standard Lipschitz and Hölder conditions on BSDE generators in the mentioned articles so as to cover the generator
FˇN,λ,πˇn\check{F}^{N,\lambda,\check{\pi}^{n}} in ([4.2](https://arxiv.org/html/2510.10260v1#S4.E2 "Equation 4.2 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), and then incorporate the policy evaluation errors from the neural approximations (under such relaxed conditions) into the convergence rate established in Theorem [4.1](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."). We defer this direction to a future work.

## 5 Experiments

In this section,444All computations were performed using PyTorch on a Mac Mini with Apple M4 Pro processor and 64GB RAM. The complete code is available at: <https://github.com/GEOR-TS/Exploratory_Robust_Stopping_RL>.
we analyze some examples to support the applicability of Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").
Let us fix g​(t,z)≡−ε​|z|g(t,z)\equiv-\varepsilon|z| for (t,z)∈[0,T]×ℝd(t,z)\in[0,T]\times\mathbb{R}^{d}, where ε≥0\varepsilon\geq 0 represents the degree of ambiguity. By Remark [2.2](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem2 "Remark 2.2. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), for any ξ∈L2​(ℱτ;ℝd)\xi\in L^{2}(\mathcal{F}\_{\tau};\mathbb{R}^{d}), it holds that ℰtg​[ξ]=ess​supϑ∈ℬε⁡𝔼tℙϑ​[ξ]\mathcal{E}^{g}\_{t}[\xi]=\operatorname\*{ess\,sup}\_{\vartheta\in\mathcal{B}^{\varepsilon}}\mathbb{E}\_{t}^{\mathbb{P}^{\vartheta}}[\xi], where ℬε\mathcal{B}^{\varepsilon} includes all 𝔽\mathbb{F}-progressively measurable processes (ϑt)t∈[0,T](\vartheta\_{t})\_{t\in[0,T]} such that |ϑt|≤ε|\vartheta\_{t}|\leq\varepsilon ℙ⊗d​t\mathbb{P}\otimes dt-a.e..

In the training phase, following Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (vi),
we parametrize vN,λ,n​(ti,x)v^{N,\lambda,n}(t\_{i},x) by

|  |  |  |
| --- | --- | --- |
|  | vin​(x;ϑin)=R​(x)+𝒩​𝒩1​(x,R​(x);ϑin),x∈ℝd,v^{n}\_{i}(x;\vartheta^{n}\_{i})=R(x)+\mathcal{NN}^{1}(x,R(x);\vartheta^{n}\_{i}),\quad x\in\mathbb{R}^{d}, |  |

where 𝒩​𝒩1​(⋅,⋅;ϑin):ℝd×ℝ→ℝ\mathcal{NN}^{1}(\cdot,\cdot;\vartheta^{n}\_{i}):\mathbb{R}^{d}\times\mathbb{R}\to\mathbb{R} denotes an FNN of depth 22, width 20+d20+d, and ReLU\mathrm{ReLU} activation, and ϑin∈Θ\vartheta^{n}\_{i}\in\Theta denotes the parameters of the FNN. In all experiments, the number of policy iterations, epochs and the training batch size is set to n¯=10\overline{n}=10, ℓ¯=1000\overline{\ell}=1000 and 2102^{10}, respectively. For numerical stability and training efficiency, we apply batch normalization before the input and at each hidden layer, together with Xavier normal initialization and the ADAM optimizer.
To make dependencies explicit, we denote by (viN,λ,⋆;ε)i=0I(v^{N,\lambda,\star;\varepsilon}\_{i})\_{i=0}^{I}, obtained after sufficient policy iterations, under penalty factor NN, temperature λ\lambda, and ambiguity degree ε\varepsilon.

We conduct experiments on the American put and call holder’s stopping problems to illustrate the policy improvement, convergence, stability, and robustness of Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").
The simulation settings are as follows: under Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), we let the running reward r​(⋅)≡0r(\cdot)\equiv 0, the discounting factor βt≡r∗\beta\_{t}\equiv r\_{\*}, the volatility σ~o​(t,xˇ)=0.4​xˇ\widetilde{\sigma}^{o}(t,\check{x})=0.4\check{x}, the initial price and strike price x=Γ=40x=\Gamma=40, and

* (i)

  (Put)
  T=1T=1, I=50I=50,
  the interest rate r∗=0.06r\_{\*}=0.06,
  the payoff R​(x)=(Γ−x)+R(x)=(\Gamma-x)^{+}, the drift b~o​(t,x)=r∗​x\widetilde{b}^{o}(t,x)=r\_{\*}x;
* (ii)

  (Call)
  T=0.5T=0.5, I=100I=100,
  the dividend rates in the training simulator δtrain=0.05{\delta}\_{\mathrm{train}}=0.05 and in the testing simulator δ\delta
  ∈{0,0.05,0.1,0.15,0.2,0.25}\in\{0,0.05,0.1,0.15,0.2,0.25\}, the interest rate r∗=0.05r\_{\*}=0.05, the payoff R​(x)=(x−Γ)+R(x)=(x-\Gamma)^{+}, the drift b~o​(t,x)=(r∗−δ)​x\widetilde{b}^{o}(t,x)=(r\_{\*}-\delta)x.

We first examine the policy improvement and convergence of Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."). For the put-type stopping problem, we fix λ=1\lambda=1 and N=10N=10, and consider several ambiguity degrees ε∈{0,0.2,0.4}\varepsilon\in\{0,0.2,0.4\}. The reference values RεrefR^{\mathrm{ref}}\_{\varepsilon} for ε∈{0,0.2,0.4}\varepsilon\in\{0,0.2,0.4\} are obtained by solving the BSDE ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) for the corresponding optimal value function using the deep backward scheme of Huré et al. [[33](https://arxiv.org/html/2510.10260v1#bib.bib33)], yielding R0ref=5.302R^{\mathrm{ref}}\_{0}=5.302, R0.2ref=4.420R^{\mathrm{ref}}\_{0.2}=4.420, R0.4ref=3.725R^{\mathrm{ref}}\_{0.4}=3.725.
The results illustrating the policy improvement and convergence are shown in Figure [1](https://arxiv.org/html/2510.10260v1#S5.F1 "Figure 1 ‣ 5 Experiments ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), which align well with the theoretical findings in Theorem [4.1](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

Similarly, for the call-type stopping problem, we again fix λ=1,N=10\lambda=1,N=10 and consider the same several ambiguity degrees. The reference values RεrefR^{\mathrm{ref}}\_{\varepsilon} computed by the deep backward scheme are R0ref=4.378R^{\mathrm{ref}}\_{0}=4.378, R0.2ref=3.677R^{\mathrm{ref}}\_{0.2}=3.677, R0.4ref=3.130R^{\mathrm{ref}}\_{0.4}=3.130. The corresponding policy improvement and convergence results are depicted in Figure [1](https://arxiv.org/html/2510.10260v1#S5.F1 "Figure 1 ‣ 5 Experiments ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1: Policy improvement and convergence in Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") under several ambiguity levels.

To examine the stability of Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), we vary the penalty, temperature and ambiguity levels as N∈{5,10,20}N\in\{5,10,20\}, λ∈{0.01,1,5}\lambda\in\{0.01,1,5\}, and ε∈{0,0.2,0.4}\varepsilon\in\{0,0.2,0.4\}, and present the corresponding values of v0N,λ,⋆;εv^{N,\lambda,\star;\varepsilon}\_{0} in Table [1](https://arxiv.org/html/2510.10260v1#S5.T1 "Table 1 ‣ 5 Experiments ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (obtained after at-least 10 iterations of the policy improvement; see Figure [1](https://arxiv.org/html/2510.10260v1#S5.F1 "Figure 1 ‣ 5 Experiments ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).
These results align with the stability analysis w.r.t. λ\lambda given in Theorem [3.5](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and the sensitivity analysis of robust optimization problems w.r.t. ambiguity level examined in [[2](https://arxiv.org/html/2510.10260v1#bib.bib2), Theorem 2.13], [[10](https://arxiv.org/html/2510.10260v1#bib.bib10), Corollary 5.4].

Table 1: Stability analysis of Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") w.r.t. the penalty, temperature and ambiguity levels.

| ε\varepsilon | v0N,λ,⋆;ε​(40)v^{N,\lambda,\star;\varepsilon}\_{0}(40) | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N=5N=5 | | | N=10N=10 | | | N=20N=20 | | |
| λ=0.01\lambda=0.01 | λ=1\lambda=1 | λ=5\lambda=5 | λ=0.01\lambda=0.01 | λ=1\lambda=1 | λ=5\lambda=5 | λ=0.01\lambda=0.01 | λ=1\lambda=1 | λ=5\lambda=5 |
| 0 | 5.2225.222 | 5.2785.278 | 6.1136.113 | 5.2335.233 | 5.2795.279 | 5.7885.788 | 5.2395.239 | 5.2965.296 | 5.5705.570 |
| 0.20.2 | 4.3114.311 | 4.4134.413 | 5.2585.258 | 4.4124.412 | 4.4574.457 | 4.9584.958 | 4.4254.425 | 4.4964.496 | 4.7654.765 |
| 0.40.4 | 3.5963.596 | 3.6713.671 | 4.4974.497 | 3.7023.702 | 3.7683.768 | 4.2214.221 | 3.7923.792 | 3.8143.814 | 4.1014.101 |



![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 2: Robustness performance under unknown testing environments.

Lastly, we examine the robustness of Algorithm [1](https://arxiv.org/html/2510.10260v1#alg1 "Algorithm 1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") in the call-type stopping problem. In particular, to assess the out-of-sample performance under an unknown testing environment, we re-simulate new state trajectories (Xˇix,δ)i=0I(\check{X}^{x,\delta}\_{i})\_{i=0}^{I} as in Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i) under different dividend rates δ∈{0,0.05,0.1,0.15,0.2,0.25}\delta\in\{0,0.05,0.1,0.15,0.2,0.25\}, where the number of simulated trajectories is set to 2202^{20}.
We fix N=10N=10 and consider configuration ε∈{0,0.1,0.2,0.3}\varepsilon\in\{0,0.1,0.2,0.3\} both for λ=1\lambda=1 and λ=5\lambda=5. Using the trained value functions (vi10,λ,⋆;ε​(⋅))i=0I(v^{10,\lambda,\star;\varepsilon}\_{i}(\cdot))\_{i=0}^{I}, the stopping policy τδε,λ\tau\_{\delta}^{\varepsilon,\lambda} and corresponding
discounted expected reward Rˇδε,λ\check{R}^{\varepsilon,\lambda}\_{\delta} under such unknown environment are defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | τδε,λ\displaystyle\tau^{\varepsilon,\lambda}\_{\delta} | :=inf{ti:vi10,λ,⋆;ε​(Xˇix,δ)≤R​(Xˇix,δ),i=0,…,I},\displaystyle:=\inf\big\{t\_{i}:v^{10,\lambda,\star;\varepsilon}\_{i}(\check{X}^{x,\delta}\_{i})\leq R(\check{X}^{x,\delta}\_{i}),\;i=0,\ldots,I\big\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Rˇδε,λ\displaystyle\check{R}^{\varepsilon,\lambda}\_{\delta} | :=𝔼​[e−r∗​τδε,λ​R​(Xˇix,δ)].\displaystyle:=\mathbb{E}\big[e^{-r\_{\*}\tau^{\varepsilon,\lambda}\_{\delta}}R(\check{X}^{x,\delta}\_{i})\big]. |  |

For each δ\delta, the corresponding American call option price represents the optimal value for the call-type stopping problem, which can be computed using the implicit finite-difference method of Forsyth and Vetzal [[24](https://arxiv.org/html/2510.10260v1#bib.bib24)]. We therefore use the option prices computed by this method as reference values RδrefR^{\mathrm{ref}}\_{\delta} for each δ\delta, yielding R0ref=4.954,R^{\mathrm{ref}}\_{0}=4.954, R0.05ref=4.410R^{\mathrm{ref}}\_{0.05}=4.410, R0.1ref=3.990R^{\mathrm{ref}}\_{0.1}=3.990, R0.15ref=3.634R^{\mathrm{ref}}\_{0.15}=3.634, R2ref=3.324R^{\mathrm{ref}}\_{2}=3.324, R0.25ref=3.052R^{\mathrm{ref}}\_{0.25}=3.052. The relative errors are then computed as |Rˇδε,λ−Rδref|/Rδref{|\check{R}^{\varepsilon,\lambda}\_{\delta}-R^{\mathrm{ref}}\_{\delta}|}/{R^{\mathrm{ref}}\_{\delta}}.

In Figure [2](https://arxiv.org/html/2510.10260v1#S5.F2 "Figure 2 ‣ 5 Experiments ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), when the dividend rate in the testing environment does not deviate significantly from that of the trained environment (near δ=0.05\delta=0.05), the non-robust value function (i.e., with ε=0\varepsilon=0) performs comparably well. However, as the discrepancy between the training and testing environments increases, the benefit of incorporating ambiguity into the framework becomes evident, as reflected by lower relative errors for higher ambiguity levels (e.g., ε=0.2,0.3\varepsilon=0.2,0.3).

## 6 Proofs

### 6.1 Proof of results in Section [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")

###### Proof 6.1 (Proof of Proposition [2.8](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem8 "Proposition 2.8. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Step 1. Fix t∈[0,T]t\in[0,T] and let τ∈Tt\tau\in{\mathcal{}T}\_{t}. An application of Itô’s formula into (e−∫tsβu​𝑑u​Ysx)s∈[t,T](e^{-\int\_{t}^{s}\beta\_{u}du}Y\_{s}^{x})\_{s\in[t,T]} ensures that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.1) |  | Ytx=e−∫tτβu​𝑑u​Yτx+∫tτe−∫tsβu​𝑑u​(r​(Xsx)+g​(s,Zsx))​𝑑s−∫tτe−∫tsβu​𝑑u​Zsx​𝑑Bs+∫tτe−∫tsβu​𝑑u​𝑑Ksx.\displaystyle\begin{aligned} Y\_{t}^{x}=&e^{-\int\_{t}^{\tau}\beta\_{u}du}Y\_{\tau}^{x}+\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}\big(r(X\_{s}^{x})+g(s,Z\_{s}^{x})\big)ds\\ &-\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}+\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}dK\_{s}^{x}.\end{aligned} |  |

Since Itx;τ∈L2​(Fτ;ℝ)\operatorname{I}\_{t}^{x;\tau}\in L^{2}({\mathcal{}F}\_{\tau};\mathbb{R}) (see Remark [2.5](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), d​Ksx≥0dK\_{s}^{x}\geq 0 for all s≥[t,τ]s\geq[t,\tau] (as KxK^{x} is nondecreasing) and Yτx≥R​(Xτx)Y\_{\tau}^{x}\geq R(X\_{\tau}^{x}) ℙ\mathbb{P}-a.s. (see Definition [2.6](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem6 "Definition 2.6. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), it holds that ℙ\mathbb{P}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Etg​[Itx;τ]\displaystyle{\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;\tau}] | ≤Etg​[Ytx−∫tτe−∫tsβu​𝑑u​g​(s,Zsx)​𝑑s+∫tτe−∫tsβu​𝑑u​Zsx​𝑑Bs]\displaystyle\leq{\mathcal{}E}\_{t}^{g}\bigg[Y\_{t}^{x}-\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}g(s,Z\_{s}^{x})ds+\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6.2) |  |  | =Ytx+Etg[−∫tτe−∫tsβu​𝑑ug(s,Zsx)ds+∫tτe−∫tsβu​𝑑uZsxdBs]=:Ytx+IIt,\displaystyle=Y\_{t}^{x}+{\mathcal{}E}^{g}\_{t}\bigg[-\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}g(s,Z\_{s}^{x})ds+\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}\bigg]=:Y\_{t}^{x}+\operatorname{II}\_{t}, |  |

where the equality holds by the property of Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot] given in [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Lemma 2.1].

Since it holds that −g​(s,Zsx)≤|g​(s,Zsx)|≤κ​|Zsx|-g(s,Z\_{s}^{x})\leq|g(s,Z\_{s}^{x})|\leq\kappa|Z\_{s}^{x}| for all s∈[t,τ]s\in[t,\tau] (see Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii), (iii)), by the monotonicity of Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot] (see [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Proposition 2.2 (iii)]),

|  |  |  |  |
| --- | --- | --- | --- |
| (6.3) |  | IIt≤Etg[κ∫tτe−∫tsβu​𝑑u|Zsx|ds+∫tτe−∫tsβu​𝑑uZsxdBs]=:IIIt.\displaystyle\operatorname{II}\_{t}\leq{\mathcal{}E}\_{t}^{g}\bigg[\kappa\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}|Z\_{s}^{x}|ds+\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}\bigg]=:\operatorname{III}\_{t}. |  |

We note that Eg:L2​(FT;ℝ)→ℝ{\mathcal{}E}^{g}:L^{2}({\mathcal{}F}\_{T};\mathbb{R})\to\mathbb{R} given in Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") is an F{\mathcal{}F}-expectation555A nonlinear expectation E:L2​(FT;ℝ)→ℝ{\mathcal{}E}:L^{2}({\mathcal{}F}\_{T};\mathbb{R})\to\mathbb{R} is called F{\mathcal{}F}-expectation if for each ξ∈L2​(FT;ℝ)\xi\in L^{2}({\mathcal{}F}\_{T};\mathbb{R}) and t∈[0,T]t\in[0,T] there exists a random variable η∈L2​(Ft;ℝ)\eta\in L^{2}({\mathcal{}F}\_{t};\mathbb{R}) such that E​[ξ​𝟏A]=E​[η​𝟏A]{\mathcal{}E}[\xi{\bf 1}\_{A}]={\mathcal{}E}[\eta{\bf 1}\_{A}] for all A∈FtA\in{\mathcal{}F}\_{t}. Moreover, given μ>0\mu>0, we say that an F{\mathcal{}F}-expectation E{\mathcal{}E} is dominated by Eμ{\mathcal{}E}^{\mu} if for all ξ,η∈L2​(FT;ℝ)\xi,\eta\in L^{2}({\mathcal{}F}\_{T};\mathbb{R}) E​(ξ+η)−E​(ξ)≤Eμ​[η];{\mathcal{}E}(\xi+\eta)-{\mathcal{}E}(\xi)\leq{\mathcal{}E}^{\mu}[\eta]; see [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Definitions 3.2 and 4.1].. Moreover, by [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Remark 4.1] it is dominated by a gg-expectation Eκ:L2​(FT;ℝ)→ℝ{\mathcal{}E}^{\kappa}:L^{2}({\mathcal{}F}\_{T};\mathbb{R})\to\mathbb{R} which is defined by setting that g​(ω,t,z):=κ​|z|g(\omega,t,z):=\kappa|z| for all (ω,t,z)∈Ω×[0,T]×ℝd(\omega,t,z)\in\Omega\times[0,T]\times\mathbb{R}^{d}, where the constant κ>0\kappa>0 appears in Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii).

Hence, an application of [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Lemma 4.4] ensures that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.4) |  | IIIt≤Etκ​[κ​∫tτe−∫tsβu​𝑑u​|Zsx|​𝑑s+∫tτe−∫tsβu​𝑑u​Zsx​𝑑Bs]=0,\displaystyle\operatorname{III}\_{t}\leq{\mathcal{}E}\_{t}^{\kappa}\bigg[\kappa\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}|Z\_{s}^{x}|ds+\int\_{t}^{\tau}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}\bigg]=0, |  |

where the equality holds because (e−∫tsβu​𝑑u​Zsx)s∈[t,T](e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x})\_{s\in[t,T]} is 𝔽\mathbb{F}-predictable and satisfies 𝔼​[∫tT|e−∫tsβu​𝑑u​Zsx|2​𝑑s]<∞\mathbb{E}[\int\_{t}^{T}|e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}|^{2}ds]<\infty (noting that Zx∈𝕃2​(ℝd)Z^{x}\in\mathbb{L}^{2}(\mathbb{R}^{d}) and βt≥0\beta\_{t}\geq 0 for all t∈[0,T]t\in[0,T]; see Definition [2.6](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem6 "Definition 2.6. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii)), hence the integrand given in ([6.4](https://arxiv.org/html/2510.10260v1#S6.E4 "Equation 6.4 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is Eκ{\mathcal{}E}^{\kappa}-martingale and the corresponding gg-expectation equals zero; see [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Lemma 5.5].

Combining ([6.2](https://arxiv.org/html/2510.10260v1#S6.E2 "Equation 6.2 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), ([6.3](https://arxiv.org/html/2510.10260v1#S6.E3 "Equation 6.3 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([6.4](https://arxiv.org/html/2510.10260v1#S6.E4 "Equation 6.4 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we obtain that Etg​[Itx;τ]≤Ytx{\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;\tau}]\leq Y\_{t}^{x} ℙ\mathbb{P}-a.s.. Since τ∈Tt\tau\in{\mathcal{}T}\_{t} is chosen some arbitrary, we have Vtx=ess​supτ∈Tt⁡Etg​[Itx;τ]≤Ytx.V\_{t}^{x}=\operatorname\*{ess\,sup}\_{\tau\in{\mathcal{}T}\_{t}}{\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;\tau}]\leq Y\_{t}^{x}.

Step 2. We now claim that Ytx≤VtxY\_{t}^{x}\leq V\_{t}^{x}. Let τt∗,x∈Tt\tau\_{t}^{\*,x}\in{\mathcal{}T}\_{t} be defined as in ([2.5](https://arxiv.org/html/2510.10260v1#S2.E5 "Equation 2.5 ‣ Proposition 2.8. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Since ∫0τt∗,x(Ys−x−R​(Xs−x))​𝑑Ksx=0\int\_{0}^{\tau\_{t}^{\*,x}}(Y\_{s-}^{x}-R(X\_{s-}^{x}))dK\_{s}^{x}=0 ℙ\mathbb{P}-a.s. (see Definition [2.6](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem6 "Definition 2.6. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (iv)) and Ys−x>R​(Xs−x)Y\_{s-}^{x}>R(X\_{s-}^{x}) for all s∈(0,τt∗,x)s\in(0,\tau\_{t}^{\*,x}) (by definition of τt∗,x\tau\_{t}^{\*,x}), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.5) |  | d​Ksx=0ℙ-a.s., for all s∈(0,τt∗,x).\displaystyle dK\_{s}^{x}=0\quad\mbox{$\mathbb{P}$-a.s., for all $s\in(0,\tau\_{t}^{\*,x})$}. |  |

Applying Itô’s formula as given in ([6.1](https://arxiv.org/html/2510.10260v1#S6.E1 "Equation 6.1 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and using ([6.5](https://arxiv.org/html/2510.10260v1#S6.E5 "Equation 6.5 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we obtain that ℙ\mathbb{P}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (6.6) |  | Ytx=e−∫tτt∗,xβu​𝑑u​Yτt∗,xx+∫tτt∗,xe−∫tsβu​𝑑u​(r​(Xsx)+g​(s,Zsx))​𝑑s−∫tτt∗,xe−∫tsβu​𝑑u​Zsx​𝑑Bs.\displaystyle\begin{aligned} Y\_{t}^{x}=&e^{-\int\_{t}^{\tau\_{t}^{\*,x}}\beta\_{u}du}Y\_{\tau\_{t}^{\*,x}}^{x}+\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}\Big(r(X\_{s}^{x})+g(s,Z\_{s}^{x})\Big)ds\\ &-\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}.\end{aligned} |  |

By putting ∫tτt∗,xe−∫tsβu​𝑑u​g​(s,Zsx)​𝑑s−∫tτt∗,x(e−∫tsβu​𝑑u​Zsx)⊤​𝑑Bs\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}g(s,Z\_{s}^{x})ds-\int\_{t}^{\tau\_{t}^{\*,x}}(e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x})^{\top}dB\_{s} into the left-hand side of ([6.6](https://arxiv.org/html/2510.10260v1#S6.E6 "Equation 6.6 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and taking the conditional gg-expectation Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot], ℙ\mathbb{P}-a.s.,

|  |  |  |  |
| --- | --- | --- | --- |
| (6.7) |  | IIItx:=Etg​[∫tτt∗,xe−∫tsβu​𝑑u​r​(Xsx)​𝑑s+e−∫tτt∗,xβu​𝑑u​Yτ∗x]=Ytx+Etg​[−∫tτt∗,xe−∫tsβu​𝑑u​g​(s,Zsx)​𝑑s+∫tτt∗,xe−∫tsβu​𝑑u​Zsx​𝑑Bs]=:Ytx+IVtx,\displaystyle\begin{aligned} \operatorname{III}\_{t}^{x}&:={\mathcal{}E}\_{t}^{g}\bigg[\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}r(X\_{s}^{x})ds+e^{-\int\_{t}^{\tau\_{t}^{\*,x}}\beta\_{u}du}Y\_{\tau^{\*}}^{x}\bigg]\\ &\;=Y\_{t}^{x}+{\mathcal{}E}\_{t}^{g}\bigg[-\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}g(s,Z\_{s}^{x})ds+\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}\bigg]\\ &\;=:Y\_{t}^{x}+\operatorname{IV}\_{t}^{x},\end{aligned} |  |

where we have used the property of Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot] given in [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Lemma 2.1].

Since Yτt∗,xx≤R​(Xτt∗,xx)Y\_{\tau\_{t}^{\*,x}}^{x}\leq R(X\_{\tau\_{t}^{\*,x}}^{x}) on {τt∗,x<T}\{\tau\_{t}^{\*,x}<T\}; Yτt∗,xx=R​(Xτt∗,xx)Y\_{\tau\_{t}^{\*,x}}^{x}=R(X\_{\tau\_{t}^{\*,x}}^{x}) on {τt∗,x=T}\{\tau\_{t}^{\*,x}=T\}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (6.8) |  | IIItx≤Etg​[∫tτt∗,xe−∫tsβu​𝑑u​r​(Xsx)​𝑑s+e−∫tτt∗,xβu​𝑑u​R​(Xτt∗,xx)]=Etg​[Itx;τt∗,x],\displaystyle\begin{aligned} \operatorname{III}\_{t}^{x}&\leq{\mathcal{}E}\_{t}^{g}\bigg[\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}r(X\_{s}^{x})ds+e^{-\int\_{t}^{\tau\_{t}^{\*,x}}\beta\_{u}du}R(X\_{\tau\_{t}^{\*,x}}^{x})\bigg]={\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;\tau\_{t}^{\*,x}}],\end{aligned} |  |

where Itx;τt∗,x∈L2​(Fτ∗;ℝ)\operatorname{I}\_{t}^{x;\tau\_{t}^{\*,x}}\in L^{2}({\mathcal{}F}\_{\tau^{\*}};\mathbb{R}) is given in ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (under the setting τ=τt∗,x\tau=\tau\_{t}^{\*,x}) and the last inequality follows from the positiveness of (βu)u∈[0,T](\beta\_{u})\_{u\in[0,T]}.

Let E−κ:L2​(FT;ℝ)→ℝ{\mathcal{}E}^{-\kappa}:L^{2}({\mathcal{}F}\_{T};\mathbb{R})\to\mathbb{R} be a gg-expectation defined by setting g​(ω,t,z):=−κ​|z|g(\omega,t,z):=-\kappa|z| for all (ω,t,z)∈Ω×[0,T]×ℝd(\omega,t,z)\in\Omega\times[0,T]\times\mathbb{R}^{d}. Then since it holds that −g​(s,Zsx)≥−|g​(s,Zsx)|≥−κ​|Zsx|-g(s,Z\_{s}^{x})\geq-|g(s,Z\_{s}^{x})|\geq-\kappa|Z\_{s}^{x}| for all s∈[t,τt∗,x]s\in[t,\tau\_{t}^{\*,x}] (see Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii), (iii)),

|  |  |  |  |
| --- | --- | --- | --- |
| (6.9) |  | IVtx≥Etg​[−κ​∫tτt∗,xe−∫tsβu​𝑑u​|Zsx|​𝑑s+∫tτt∗,xe−∫tsβu​𝑑u​Zsx​𝑑Bs]≥Et−κ​[−κ​∫tτt∗,xe−∫tsβu​𝑑u​|Zsx|​𝑑s+∫tτt∗,xe−∫tsβu​𝑑u​Zsx​𝑑Bs]=0,\displaystyle\begin{aligned} \operatorname{IV}\_{t}^{x}&\geq{\mathcal{}E}\_{t}^{g}\bigg[-\kappa\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}|Z\_{s}^{x}|ds+\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}\bigg]\\ &\geq{\mathcal{}E}\_{t}^{-\kappa}\bigg[-\kappa\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}|Z\_{s}^{x}|ds+\int\_{t}^{\tau\_{t}^{\*,x}}e^{-\int\_{t}^{s}\beta\_{u}du}Z\_{s}^{x}dB\_{s}\bigg]=0,\end{aligned} |  |

where the first inequality follows from the monotonicity of Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot] (see [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Proposition 2.2 (iii)]), the second inequality follows from [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Lemma 4.4], and the last equality follows from the same arguments presented for the equality given in ([6.4](https://arxiv.org/html/2510.10260v1#S6.E4 "Equation 6.4 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Combining ([6.7](https://arxiv.org/html/2510.10260v1#S6.E7 "Equation 6.7 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))–([6.9](https://arxiv.org/html/2510.10260v1#S6.E9 "Equation 6.9 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we obtain that Ytx≤Etg​[Itx;τt∗,x]Y\_{t}^{x}\leq{\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;\tau\_{t}^{\*,x}}], ℙ\mathbb{P}-a.s.. As τt∗,x=inf{s≥t|Ysx≤R​(Xsx)}∧T∈Tt\tau\_{t}^{\*,x}=\inf\{s\geq t\,|\,Y\_{s}^{x}\leq R(X\_{s}^{x})\}\wedge T\in{\mathcal{}T}\_{t}, we have Ytx≤Vtx=ess​supτ∈Tt⁡Etg​[Itx;τ],Y\_{t}^{x}\leq V\_{t}^{x}=\operatorname\*{ess\,sup}\_{\tau\in{\mathcal{}T}\_{t}}{\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;\tau}], ℙ\mathbb{P}-a.s.,
as claimed. Therefore, τt∗,x\tau\_{t}^{\*,x} given in ([2.5](https://arxiv.org/html/2510.10260v1#S2.E5 "Equation 2.5 ‣ Proposition 2.8. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is optimal to ([2.2](https://arxiv.org/html/2510.10260v1#S2.E2 "Equation 2.2 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). This completes the proof.

###### Proof 6.2 (Proof of Proposition [2.10](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem10 "Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Step 1. Let N∈ℕN\in\mathbb{N} and α∈A\alpha\in{\mathcal{}A} be given.
Recalling FxF^{x} given in ([2.3](https://arxiv.org/html/2510.10260v1#S2.E3 "Equation 2.3 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we denote for every (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝ𝕕(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R^{d}} by

|  |  |  |  |
| --- | --- | --- | --- |
| (6.10) |  | F~tx;N,α​(ω,y,z):=Ftx​(ω,y,z)+N​αt​(ω)​(R​(Xtx​(ω))−y).\displaystyle\widetilde{F}\_{t}^{x;N,\alpha}(\omega,y,z):=F\_{t}^{x}(\omega,y,z)+N\alpha\_{t}(\omega)\,\big(R(X\_{t}^{x}(\omega))-y\big). |  |

Then consider the following controlled BSDE: for t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
| (6.11) |  | Y~tx;N,α=R​(XTx)+∫tTF~sx;N,α​(Y~sx;N,α,Z~sx;N,α)​𝑑s−∫tTZ~sx;N,α​𝑑Bs.\displaystyle\widetilde{Y}\_{t}^{x;N,\alpha}=R(X\_{T}^{x})+\int\_{t}^{T}\widetilde{F}^{x;N,\alpha}\_{s}\big(\widetilde{Y}\_{s}^{x;N,\alpha},\widetilde{Z}\_{s}^{x;N,\alpha}\big)ds-\int\_{t}^{T}\widetilde{Z}\_{s}^{x;N,\alpha}dB\_{s}. |  |

Since α\alpha is uniformly bounded (noting that it has values only in {0,1}\{0,1\}), one can deduce that the parameters of the BSDE ([6.11](https://arxiv.org/html/2510.10260v1#S6.E11 "Equation 6.11 ‣ Proof 6.2 (Proof of Proposition 2.10). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfies all the conditions given in [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Section 3]. Hence,
there exists a unique solution (Y~tx;N,α,Z~tx;N,α)t∈[0,T]∈𝕊2​(ℝ)×𝕃2​(ℝd)(\widetilde{Y}\_{t}^{x;N,\alpha},\widetilde{Z}\_{t}^{x;N,\alpha})\_{t\in[0,T]}\in\mathbb{S}^{2}(\mathbb{R})\times\mathbb{L}^{2}(\mathbb{R}^{d}) to the controlled BSDE ([6.11](https://arxiv.org/html/2510.10260v1#S6.E11 "Equation 6.11 ‣ Proof 6.2 (Proof of Proposition 2.10). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

We now claim that Y~tx;N,α=Etg​[Itx;N,α]\widetilde{Y}\_{t}^{x;N,\alpha}={\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;N,\alpha}] for all t∈[0,T]t\in[0,T]. Indeed, applying Itô’s formula into (e−∫ts(βu+N​αu)​𝑑u​Y~sx;N,α)s∈[t,T](e^{-\int\_{t}^{s}(\beta\_{u}+N\alpha\_{u})du}\widetilde{Y}\_{s}^{x;N,\alpha})\_{s\in[t,T]} and then taking Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot] yield,

|  |  |  |
| --- | --- | --- |
|  | Etg​[Itx;N,α]−Y~tx;N,α\displaystyle{\mathcal{}E}\_{t}^{g}[\operatorname{I}\_{t}^{x;N,\alpha}]-\widetilde{Y}\_{t}^{x;N,\alpha} |  |
|  |  |  |
| --- | --- | --- |
|  | =Etg​[−∫tTe−∫ts(βu+N​αu)​𝑑u​g​(s,Z~sx;N,α)​𝑑s+∫tTe−∫ts(βu+N​αu)​𝑑u​Z~sx;N,α​𝑑Bs],\displaystyle\quad={\mathcal{}E}\_{t}^{g}\bigg[-\int\_{t}^{T}e^{-\int\_{t}^{s}(\beta\_{u}+N\alpha\_{u})du}g(s,\widetilde{Z}\_{s}^{x;N,\alpha})ds+\int\_{t}^{T}e^{-\int\_{t}^{s}(\beta\_{u}+N\alpha\_{u})du}\widetilde{Z}\_{s}^{x;N,\alpha}dB\_{s}\bigg], |  |

where we have used the property of Etg​[⋅]{\mathcal{}E}\_{t}^{g}[\cdot] given in [[12](https://arxiv.org/html/2510.10260v1#bib.bib12), Lemma 2.1].

Moreover, by using the same arguments presented for the Eg{\mathcal{}E}^{g}-supermartingale property in ([6.2](https://arxiv.org/html/2510.10260v1#S6.E2 "Equation 6.2 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))–([6.4](https://arxiv.org/html/2510.10260v1#S6.E4 "Equation 6.4 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and the Eg{\mathcal{}E}^{g}-submartingale property in ([6.7](https://arxiv.org/html/2510.10260v1#S6.E7 "Equation 6.7 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([6.9](https://arxiv.org/html/2510.10260v1#S6.E9 "Equation 6.9 ‣ Proof 6.1 (Proof of Proposition 2.8). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (see the proof of Proposition [2.8](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem8 "Proposition 2.8. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) we can deduce that the conditional gg-expectation appearing in the right-hand side of the above equals zero (i.e., the integrand therein is an Eg{\mathcal{}E}^{g}-martingale). Hence the claim holds.

Step 2. It suffices to show that for every t∈[0,T]t\in[0,T] ℙ\mathbb{P}-a.s., Ytx;N=ess​supα∈A⁡Y~tx;N,α.Y\_{t}^{x;N}=\operatorname\*{ess\,sup}\_{\alpha\in{\mathcal{}A}}\widetilde{Y}\_{t}^{x;N,\alpha}.
Indeed, it follows from Step 1 that for every α∈A\alpha\in{\mathcal{}A} the parameters of the BSDE ([6.11](https://arxiv.org/html/2510.10260v1#S6.E11 "Equation 6.11 ‣ Proof 6.2 (Proof of Proposition 2.10). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfies the conditions given in [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Section 3]. Furthermore, the parameters of the BSDE ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) also satisfies the conditions (see Remark [2.9](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem9 "Remark 2.9. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i)).

We recall that Fx;NF^{x;N} given in ([2.6](https://arxiv.org/html/2510.10260v1#S2.E6 "Equation 2.6 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is the generator of ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and that for each α∈A\alpha\in{\mathcal{}A} F~x;N,α\widetilde{F}^{x;N,\alpha} given in ([6.10](https://arxiv.org/html/2510.10260v1#S6.E10 "Equation 6.10 ‣ Proof 6.2 (Proof of Proposition 2.10). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is the generator of ([6.11](https://arxiv.org/html/2510.10260v1#S6.E11 "Equation 6.11 ‣ Proof 6.2 (Proof of Proposition 2.10). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Then for any α∈A\alpha\in{\mathcal{}A}, it holds that for all (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d}

|  |  |  |
| --- | --- | --- |
|  | Ftx;N​(ω,y,z)=Ftx​(ω,y,z)+N​maxa∈{0,1}⁡{(R​(Xtx​(ω))−y)​a}≥F~tx;N,α​(ω,y,z).\displaystyle F\_{t}^{x;N}(\omega,y,z)=F\_{t}^{x}(\omega,y,z)+N\max\_{a\in\{0,1\}}\Big\{\big(R(X\_{t}^{x}(\omega))-y\big)a\Big\}\geq\widetilde{F}\_{t}^{x;N,\alpha}(\omega,y,z). |  |

This ensures that for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
| (6.12) |  | Ftx;N​(Ytx;N,Ztx;N)≥ess​supα∈A⁡F~tx;N,α​(Ytx;N,Ztx;N).\displaystyle F^{x;N}\_{t}\big(Y\_{t}^{x;N},Z\_{t}^{x;N}\big)\geq\operatorname\*{ess\,sup}\_{\alpha\in{\mathcal{}A}}\widetilde{F}\_{t}^{x;N,\alpha}(Y\_{t}^{x;N},Z\_{t}^{x;N}). |  |

Moreover, let α∗,x;N\alpha^{\*,x;N} be defined as in ([2.8](https://arxiv.org/html/2510.10260v1#S2.E8 "Equation 2.8 ‣ Proposition 2.10. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Clearly, it takes values in {0,1}\{0,1\}. Moreover, since Yx;NY^{x;N} is in 𝕊2​(ℝ)\mathbb{S}^{2}(\mathbb{R}) (see Remark [2.9](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem9 "Remark 2.9. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i)) and (R​(Xtx))t∈[0,T](R(X\_{t}^{x}))\_{t\in[0,T]} are 𝔽\mathbb{F}-progressively measurable (noting that XxX^{x} is Itô (𝔽,ℙ)(\mathbb{F},\mathbb{P})-semimartingale and RR is continuous), α∗,x;N\alpha^{\*,x;N} is 𝔽\mathbb{F}-progressively measurable. Therefore, we have that α∗,x;N∈A\alpha^{\*,x;N}\in{\mathcal{}A}.

Moreover, by definition of α∗,x;N\alpha^{\*,x;N}, F~tx;N,α∗,x;N​(Ytx;N,Ztx;N)=Ftx;N​(Ytx;N,Ztx;N).\widetilde{F}\_{t}^{x;N,\alpha^{\*,x;N}}(Y\_{t}^{x;N},Z\_{t}^{x;N})=F\_{t}^{x;N}(Y\_{t}^{x;N},Z\_{t}^{x;N}).
This implies that the inequality given in ([6.12](https://arxiv.org/html/2510.10260v1#S6.E12 "Equation 6.12 ‣ Proof 6.2 (Proof of Proposition 2.10). ‣ 6.1 Proof of results in Section 2 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) holds as equality.

Therefore, an application of [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Proposition 3.1] ensures the claim to hold.

Step 3. Lastly, it follows from [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Corollary 3.3] that the process α∗,x;N∈A\alpha^{\*,x;N}\in{\mathcal{}A} is optimal for the problem given in Step 2., i.e., for all t∈[0,T]t\in[0,T]
ess​supα∈A⁡Y~tx;N,α=Y~tx;N,α∗,x;N.\operatorname\*{ess\,sup}\_{\alpha\in{\mathcal{}A}}\widetilde{Y}\_{t}^{x;N,\alpha}=\widetilde{Y}\_{t}^{x;N,\alpha^{\*,x;N}}.
This completes the proof.

### 6.2 Proof of results in Section [3](https://arxiv.org/html/2510.10260v1#S3 "3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")

###### Proof 6.3 (Proof of Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Let N∈ℕN\in\mathbb{N} and λ>0\lambda>0 be given. We prove (i) by showing that the parameters of the BSDE ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfy all the conditions given in [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Section 3] to ensure its existence and uniqueness to hold.

As rr is a Borel function and both (βt)t∈[0,T](\beta\_{t})\_{t\in[0,T]} and (g​(t,z))t∈[0,T](g(t,z))\_{t\in[0,T]} are 𝔽\mathbb{F}-progressively measurable for all z∈ℝdz\in\mathbb{R}^{d}, (F¯tx;N,λ​(y,z))t∈[0,T](\overline{F}\_{t}^{x;N,\lambda}(y,z))\_{t\in[0,T]} given in ([3.7](https://arxiv.org/html/2510.10260v1#S3.E7 "Equation 3.7 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) is 𝔽\mathbb{F}-progressively measurable for all (y,z)∈ℝ×ℝd(y,z)\in\mathbb{R}\times\mathbb{R}^{d}. Moreover, since g​(ω,t,0)=0g(\omega,t,0)=0 for all (ω,t)∈Ω×[0,T](\omega,t)\in\Omega\times[0,T] (see Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (iii)), by the growth conditions of rr and RR (see Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i)) and Remark [2.4](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i), it holds that ‖F¯⋅x;N,λ​(0,0)‖𝕃2<∞\|\overline{F}^{x;N,\lambda}\_{\cdot}(0,0)\|\_{\mathbb{L}^{2}}<\infty and ‖R​(X⋅x)‖𝕃2<∞\|R(X\_{\cdot}^{x})\|\_{\mathbb{L}^{2}}<\infty.

By the regularity of gg given in Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii) and the boundedness of (βt)t∈[0,T](\beta\_{t})\_{t\in[0,T]} (see Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii)), for every (ω,t)∈Ω×[0,T](\omega,t)\in\Omega\times[0,T], y,y^∈ℝy,\hat{y}\in\mathbb{R} and z,z^∈ℝdz,\hat{z}\in\mathbb{R}^{d}

|  |  |  |  |
| --- | --- | --- | --- |
| (6.13) |  | |Ftx​(ω,y,z)−Ftx​(ω,y^,z^)|≤βt​(ω)​|y−y^|+|g​(ω,t,z)−g​(ω,t,z^)|≤(Cβ+κ)​(|y−y^|+|z−z^|).\displaystyle\begin{aligned} |F\_{t}^{x}(\omega,y,z)-F\_{t}^{x}(\omega,\hat{y},\hat{z})|&\leq\beta\_{t}(\omega)|y-\hat{y}|+|g(\omega,t,z)-g(\omega,t,\hat{z})|\\ &\leq(C\_{\beta}+\kappa)\big(|y-\hat{y}|+|z-\hat{z}|\big).\end{aligned} |  |

Moreover, since the map

|  |  |  |  |
| --- | --- | --- | --- |
| (6.14) |  | hN,λ:ℝ∋s→hN,λ​(s):=λ​log⁡(exp⁡(−N​λ−1​s)+1)∈(0,+∞)\displaystyle h^{N,\lambda}:\mathbb{R}\ni s\to h^{N,\lambda}(s):=\lambda\log(\exp(-N\lambda^{-1}\,s)+1)\in(0,+\infty) |  |

is (strictly) decreasing and N​λ−1N\lambda^{-1}-Lipschitz continuous, we are able to see that
for every ω∈Ω\omega\in\Omega, t∈[0,T]t\in[0,T], and y,y^∈ℝy,\hat{y}\in\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Gtx;N,λ​(ω,y)−Gtx;N,λ​(ω,y^)|\displaystyle|G^{x;N,\lambda}\_{t}(\omega,y)-G^{x;N,\lambda}\_{t}(\omega,\hat{y})| | ≤N​|(R​(Xtx​(ω))−y)−(R​(Xtx​(ω))−y^)|\displaystyle\leq N\Big|\big(R(X\_{t}^{x}(\omega))-y\big)-\big(R(X\_{t}^{x}(\omega))-\hat{y}\big)\Big| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6.15) |  |  | +|hN,λ(R(Xtx(ω))−y)−hN,λ((R(Xtx(ω))−y^)|\displaystyle\quad+\Big|h^{N,\lambda}\big(R(X\_{t}^{x}(\omega))-y\big)-h^{N,\lambda}\big((R(X\_{t}^{x}(\omega))-\hat{y}\big)\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​N​|y−y^|.\displaystyle\leq 2N|y-\hat{y}|. |  |

From ([6.13](https://arxiv.org/html/2510.10260v1#S6.E13 "Equation 6.13 ‣ Proof 6.3 (Proof of Theorem 3.4). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([6.15](https://arxiv.org/html/2510.10260v1#S6.E15 "Equation 6.15 ‣ Proof 6.3 (Proof of Theorem 3.4). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and the definition of F¯x;N,λ\overline{F}^{x;N,\lambda} given in ([3.7](https://arxiv.org/html/2510.10260v1#S3.E7 "Equation 3.7 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), it follows that the desired priori estimate of F¯x;N,λ\overline{F}^{x;N,\lambda} holds. Hence an application of [[49](https://arxiv.org/html/2510.10260v1#bib.bib49), Theorem 3.1] ensures the existence and uniqueness of the solution of ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), as claimed.

We now prove (ii). By the representation given in ([3.6](https://arxiv.org/html/2510.10260v1#S3.E6 "Equation 3.6 ‣ item (ii) ‣ Remark 3.3. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), it suffices to show that ℙ\mathbb{P}-a.s. Y¯tx;N,λ=ess​supπ∈Π⁡Y¯tx;N,λ,π.\overline{Y}\_{t}^{x;N,\lambda}=\operatorname\*{ess\,sup}\_{\pi\in\Pi}\overline{Y}\_{t}^{x;N,\lambda,\pi}.

Since H{\mathcal{}H} is strictly convex on [0,1][0,1] (see Remark [3.1](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem1 "Remark 3.1. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), it holds that for every (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d}

|  |  |  |  |
| --- | --- | --- | --- |
| (6.16) |  | F¯tx;N,λ​(ω,y,z)=Ftx​(ω,y,z)+maxa∈[0,1]⁡{N​(R​(Xtx​(ω))−y)​a−λ​H​(a)},\displaystyle\overline{F}\_{t}^{x;N,\lambda}(\omega,y,z)=F\_{t}^{x}(\omega,y,z)+\max\_{a\in[0,1]}\bigg\{N(R(X\_{t}^{x}(\omega))-y)a-\lambda{\mathcal{}H}(a)\bigg\}, |  |

where the equality holds by the first-order-optimality condition with the corresponding maximizer a∗=(1+e−N​λ−1​(R​(Xtx​(ω))−y))−1∈[0,1].a^{\*}=(1+e^{-{N}{\lambda}^{-1}(R(X\_{t}^{x}(\omega))-y)})^{-1}\in[0,1].

Then it follows from ([6.16](https://arxiv.org/html/2510.10260v1#S6.E16 "Equation 6.16 ‣ Proof 6.3 (Proof of Theorem 3.4). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) that F¯tx;N,λ​(ω,y,z)≥F¯tx;N,λ,π​(ω,y,z)\overline{F}\_{t}^{x;N,\lambda}(\omega,y,z)\geq\overline{F}\_{t}^{x;N,\lambda,\pi}(\omega,y,z) for all π∈Π\pi\in\Pi and (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d}. This ensures that for every t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
| (6.17) |  | F¯tx;N,λ​(Y¯tx;N,λ,Z¯tx;N,λ)≥ess​supπ∈A⁡F¯tx;N,λ,π​(Y¯tx;N,λ,Z¯tx;N,λ).\displaystyle\overline{F}\_{t}^{x;N,\lambda}\big(\overline{Y}\_{t}^{x;N,\lambda},\overline{Z}\_{t}^{x;N,\lambda}\big)\geq\operatorname\*{ess\,sup}\_{\pi\in{\mathcal{}A}}\overline{F}\_{t}^{x;N,\lambda,\pi}(\overline{Y}\_{t}^{x;N,\lambda},\overline{Z}\_{t}^{x;N,\lambda}). |  |

Moreover, let π∗,x;N,λ:=(πt∗,x;N,λ)t∈[0,T]\pi^{\*,x;N,\lambda}:=(\pi^{\*,x;N,\lambda}\_{t})\_{t\in[0,T]} be defined as in ([3.9](https://arxiv.org/html/2510.10260v1#S3.E9 "Equation 3.9 ‣ item (ii) ‣ Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Clearly, it takes values in [0,1][0,1]. Moreover, since Y¯x;N,λ\overline{Y}^{x;N,\lambda} is in 𝕊2​(ℝ)\mathbb{S}^{2}(\mathbb{R}) (see part (i)) and (R​(Xtx))t∈[0,T](R(X\_{t}^{x}))\_{t\in[0,T]} are 𝔽\mathbb{F}-progressively measurable (noting that XxX^{x} is Itô (𝔽,ℙ)(\mathbb{F},\mathbb{P})-semimartingale and RR is continuous), π∗,x;N,λ\pi^{\*,x;N,\lambda} is 𝔽\mathbb{F}-progressively measurable. Therefore, we have that πt∗,x;N,λ∈Π\pi^{\*,x;N,\lambda}\_{t}\in\Pi.

Furthermore, by ([6.16](https://arxiv.org/html/2510.10260v1#S6.E16 "Equation 6.16 ‣ Proof 6.3 (Proof of Theorem 3.4). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and definition of π∗,x;N,λ\pi^{\*,x;N,\lambda}, it holds that

|  |  |  |
| --- | --- | --- |
|  | F¯tx;N,λ,π∗,x;N,λ​(Y¯tx;N,λ,Z¯tx;N,λ)=F¯tx;N,λ​(Y¯tx;N,λ,Z¯tx;N,λ),\overline{F}\_{t}^{x;N,\lambda,\pi^{\*,x;N,\lambda}}(\overline{Y}\_{t}^{x;N,\lambda},\overline{Z}\_{t}^{x;N,\lambda})=\overline{F}\_{t}^{x;N,\lambda}\big(\overline{Y}\_{t}^{x;N,\lambda},\overline{Z}\_{t}^{x;N,\lambda}\big), |  |

which implies that the inequality given in ([6.17](https://arxiv.org/html/2510.10260v1#S6.E17 "Equation 6.17 ‣ Proof 6.3 (Proof of Theorem 3.4). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) holds as equality.

Therefore, an application of [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Proposition 3.1] ensures the claim to hold.

Moreover, a direct application of [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Corollary 3.3] ensures that π∗,x;N,λ\pi^{\*,x;N,\lambda} is optimal for V¯x;N,λ\overline{V}^{x;N,\lambda} given in ([3.2](https://arxiv.org/html/2510.10260v1#S3.E2 "Equation 3.2 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). This completes the proof.

###### Proof 6.4 (Proof of Theorem [3.5](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Let N∈ℕN\in\mathbb{N} and λ>0\lambda>0 be given. Recall that F¯x;N,λ\overline{F}^{x;N,\lambda} and Fx;NF^{x;N}, given in ([3.7](https://arxiv.org/html/2510.10260v1#S3.E7 "Equation 3.7 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([2.6](https://arxiv.org/html/2510.10260v1#S2.E6 "Equation 2.6 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), respectively, are the generators of the BSDEs ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), respectively. Then set for every (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​F¯tx;N,λ​(ω,y,z):=\displaystyle\Delta\overline{F}\_{t}^{x;N,\lambda}(\omega,y,z):= | F¯tx;N,λ​(ω,y,z)−Ftx;N​(ω,y,z)\displaystyle\overline{F}\_{t}^{x;N,\lambda}(\omega,y,z)-F\_{t}^{x;N}(\omega,y,z) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6.18) |  | =\displaystyle= | hN,λ​(R​(Xtx​(ω))−y)+N​(R​(Xtx​(ω))−y)​𝟏{y>R​(Xtx​(ω))},\displaystyle h^{N,\lambda}(R(X\_{t}^{x}(\omega))-y\big)+N\big(R(X\_{t}^{x}(\omega))-y){\bf 1}\_{\{y>R(X\_{t}^{x}(\omega))\}}, |  |

where we recall that the map hN,λh^{N,\lambda} is given in ([6.14](https://arxiv.org/html/2510.10260v1#S6.E14 "Equation 6.14 ‣ Proof 6.3 (Proof of Theorem 3.4). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Since the map hN,λh^{N,\lambda} is positive and satisfies that hN,λ​(s)=−N​s+hN,λ​(−s)h^{N,\lambda}(s)=-Ns+h^{N,\lambda}(-s) for all s∈ℝs\in\mathbb{R}, it holds that for every (ω,t,y,z)∈Ω×[0,T]×ℝ×ℝd(\omega,t,y,z)\in\Omega\times[0,T]\times\mathbb{R}\times\mathbb{R}^{d}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​F¯tx;N,λ​(ω,t,y,z)\displaystyle\Delta\overline{F}\_{t}^{x;N,\lambda}(\omega,t,y,z) | ≥[hN,λ​(R​(Xtx​(ω))−y)+N​(R​(Xtx​(ω))−y)]​𝟏{y>R​(Xtx​(ω))}\displaystyle\geq\bigg[h^{N,\lambda}\big(R(X\_{t}^{x}(\omega))-y\big)+N\big(R(X\_{t}^{x}(\omega))-y\big)\bigg]{\bf 1}\_{\{y>R(X\_{t}^{x}(\omega))\}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6.19) |  |  | =hN,λ​(−(R​(Xtx​(ω))−y))​𝟏{y>R​(Xtx​(ω))}≥0.\displaystyle=h^{N,\lambda}(-(R(X\_{t}^{x}(\omega))-y)){\bf 1}\_{\{y>R(X\_{t}^{x}(\omega))\}}\geq 0. |  |

Moreover, as the terminal conditions of ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) are coincide, it follows from the comparison principle of BSDEs (see, e.g., [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Theorem 2.2]) that ([3.10](https://arxiv.org/html/2510.10260v1#S3.E10 "Equation 3.10 ‣ Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) holds.

It remains to show that ([3.11](https://arxiv.org/html/2510.10260v1#S3.E11 "Equation 3.11 ‣ Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) holds. Set for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0,

|  |  |  |  |
| --- | --- | --- | --- |
| (6.20) |  | Δ​Yx;N,λ:=Y¯x;N,λ−Yx;N,Δ​Zx;N,λ:=Z¯x;N,λ−Zx;N.\displaystyle\Delta{Y}^{x;N,\lambda}:=\overline{Y}^{x;N,\lambda}-Y^{x;N},\qquad\Delta{Z}^{x;N,\lambda}:=\overline{Z}^{x;N,\lambda}-Z^{x;N}. |  |

Since the parameters of the BSDEs ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfy the conditions given in [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Section 5] (with exponent 22) for all N∈ℕN\in\mathbb{N} and λ>0\lambda>0, we are able to apply [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Proposition 5.1] to have the following a priori estimates:666In [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Section 5], the filtration (denoted by (Ft)({\mathcal{}F}\_{t}) therein) is set to be right-continuous and complete (and hence not necessarily the Brownian filtration, as in our case). Nevertheless, we can still apply the stability result given in [[21](https://arxiv.org/html/2510.10260v1#bib.bib21), Proposition 5.1], since the martingales MiM^{i}, i=1,2i=1,2, appearing therein are orthogonal to the Brownian motion. Consequently, the arguments remain valid when the general filtration is replaced with the Brownian one.
for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0

|  |  |  |  |
| --- | --- | --- | --- |
| (6.21) |  | ‖Δ​Yx;N,λ‖𝕊2+‖Δ​Zx;N,λ‖𝕃2≤C​𝔼​[∫0T|Δ​F¯tx;N,λ​(Ytx,N,Ztx;N)|2​𝑑t]12,\displaystyle\|\Delta{Y}^{x;N,\lambda}\|\_{\mathbb{S}^{2}}+\|\Delta{Z}^{x;N,\lambda}\|\_{\mathbb{L}^{2}}\leq C\mathbb{E}\bigg[\int\_{0}^{T}|\Delta\overline{F}\_{t}^{x;N,\lambda}(Y\_{t}^{x,N},Z\_{t}^{x;N})|^{2}dt\bigg]^{\frac{1}{2}}, |  |

with some C>0C>0 (depending on TT but not on NN,λ\lambda), and ΔF¯x;N,λ\Delta\overline{F}{}^{x;N,\lambda} given in ([6.18](https://arxiv.org/html/2510.10260v1#S6.E18 "Equation 6.18 ‣ Proof 6.4 (Proof of Theorem 3.5). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

We note that hN,λ​(s)=λ​log⁡(exp⁡(−N​λ−1​s)+1)≤λ​log⁡2h^{N,\lambda}(s)=\lambda\log(\exp(-N\lambda^{-1}s)+1)\leq\lambda\log 2 for all s≥0s\geq 0. On the other hand, a simple calculation ensures for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0 that the map

|  |  |  |
| --- | --- | --- |
|  | h¯N,λ:[0,∞)∋s→h¯N,λ​(s):=hN,λ​(−s)−N​s=λ​log⁡(exp⁡(N​λ−1​s)+1)−N​s\overline{h}^{N,\lambda}:[0,\infty)\ni s\to\overline{h}^{N,\lambda}(s):=h^{N,\lambda}(-s)-Ns=\lambda\log(\exp({N}{\lambda}^{-1}s)+1)-Ns |  |

is (strictly) decreasing. This implies that h¯N,λ​(s)≤h¯N,λ​(0)=λ​log⁡2\overline{h}^{N,\lambda}(s)\leq\overline{h}^{N,\lambda}(0)=\lambda\log 2 for all s≥0s\geq 0.

From these observations and ([6.19](https://arxiv.org/html/2510.10260v1#S6.E19 "Equation 6.19 ‣ Proof 6.4 (Proof of Theorem 3.5). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we have for every N∈ℕN\in\mathbb{N}, λ>0\lambda>0, and t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤ΔF¯(Ytx,N,Ztx;N)tx;N,λ=\displaystyle 0\leq\Delta\overline{F}{}^{x;N,\lambda}\_{t}(Y\_{t}^{x,N},Z\_{t}^{x;N})= | hN,λ​(−(Ytx,N−R​(Xtx)))​𝟏{Ytx,N≤R​(Xtx)}\displaystyle h^{N,\lambda}\Big(-\big(Y\_{t}^{x,N}-R(X\_{t}^{x})\big)\Big){\bf 1}\_{\{Y\_{t}^{x,N}\leq R(X\_{t}^{x})\}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6.22) |  |  | +h¯N,λ​(Ytx,N−R​(Xtx))​𝟏{Ytx,N>R​(Xtx)}≤λ​log⁡2.\displaystyle+\overline{h}^{N,\lambda}\big(Y\_{t}^{x,N}-R(X\_{t}^{x})\big){\bf 1}\_{\{Y\_{t}^{x,N}>R(X\_{t}^{x})\}}\leq\lambda\log 2. |  |

Combining ([6.22](https://arxiv.org/html/2510.10260v1#S6.E22 "Equation 6.22 ‣ Proof 6.4 (Proof of Theorem 3.5). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) with ([6.21](https://arxiv.org/html/2510.10260v1#S6.E21 "Equation 6.21 ‣ Proof 6.4 (Proof of Theorem 3.5). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) concludes that for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0 the estimate in ([3.11](https://arxiv.org/html/2510.10260v1#S3.E11 "Equation 3.11 ‣ Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) holds,
as claimed. This completes the proof.

###### Proof 6.5 (Proof of Corollary [3.6](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem6 "Corollary 3.6. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Set for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0, Dtx;N:=Ytx;N−R​(Xtx)D\_{t}^{x;N}:=Y\_{t}^{x;N}-R(X\_{t}^{x}) and D¯tx;N,λ:=Y¯tx;N,λ−R​(Xtx)\overline{D}\_{t}^{x;N,\lambda}:=\overline{Y}\_{t}^{x;N,\lambda}-R(X\_{t}^{x}), t∈[0,T]t\in[0,T],
where Yx;NY^{x;N} and Y¯x;N,λ\overline{Y}^{x;N,\lambda} denote the first components of the unique solution to the BSDEs ([2.7](https://arxiv.org/html/2510.10260v1#S2.E7 "Equation 2.7 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and ([3.8](https://arxiv.org/html/2510.10260v1#S3.E8 "Equation 3.8 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), respectively (see also Remark [2.9](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem9 "Remark 2.9. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") and Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i)).

Then for every N∈ℕN\in\mathbb{N} and λ>0\lambda>0 it holds that for every t≥0t\geq 0, ℙ\mathbb{P}-a.s.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |αt∗,x;N−πt∗,x;N,λ|\displaystyle\big|\alpha\_{t}^{\*,x;N}-\pi^{\*,x;N,\lambda}\_{t}\big| | ≤|𝟏{Dtx;N<0}−𝟏{D¯tx;N,λ<0}|+|𝟏{D¯tx;N,λ<0}−11+eNλ​D¯tx;N,λ|\displaystyle\leq\bigg|{\bf 1}\_{\{D\_{t}^{x;N}<0\}}-{\bf 1}\_{\{\overline{D}\_{t}^{x;N,\lambda}<0\}}\bigg|+\bigg|{\bf 1}\_{\{\overline{D}\_{t}^{x;N,\lambda}<0\}}-\frac{1}{1+e^{\frac{N}{\lambda}\overline{D}\_{t}^{x;N,\lambda}}}\bigg| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6.23) |  |  | =𝟏{Dtx;N<0≤D¯tx;N,λ}+11+eN​λ−1​|D¯tx;N,λ|,\displaystyle={\bf 1}\_{\{D\_{t}^{x;N}<0\leq\overline{D}\_{t}^{x;N,\lambda}\}}+\frac{1}{1+e^{{N}{\lambda}^{-1}|\overline{D}\_{t}^{x;N,\lambda}|}}, |  |

where the last equality holds as Dtx;N≤D¯tx;N,λD\_{t}^{x;N}\leq\overline{D}\_{t}^{x;N,\lambda}, ℙ\mathbb{P}-a.s., for all t≥0t\geq 0 (see ([3.10](https://arxiv.org/html/2510.10260v1#S3.E10 "Equation 3.10 ‣ Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))).

By Theorem [3.5](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), for any N∈ℕN\in\mathbb{N}
‖Yx;N−Y¯x;N,λ‖𝕊2=‖Dx;N−D¯x;N,λ‖𝕊2→0\|Y^{x;N}-\overline{Y}^{x;N,\lambda}\|\_{\mathbb{S}^{2}}=\|D^{x;N}-\overline{D}^{x;N,\lambda}\|\_{\mathbb{S}^{2}}\to 0 as λ↓0\lambda\downarrow 0.
This implies that for any N∈ℕN\in\mathbb{N}, |Dtx;N−D¯tx;N,λ|→0|D\_{t}^{x;N}-\overline{D}\_{t}^{x;N,\lambda}|\to 0 ℙ⊗d​t\mathbb{P}\otimes dt-a.e. as λ↓0\lambda\downarrow 0.

Comining this with the a priori estimates given in ([6.23](https://arxiv.org/html/2510.10260v1#S6.E23 "Equation 6.23 ‣ Proof 6.5 (Proof of Corollary 3.6). ‣ 6.2 Proof of results in Section 3 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we have for any N∈ℕN\in\mathbb{N}

|  |  |  |
| --- | --- | --- |
|  | |αt∗,x;N−πt∗,x;N,λ|→0ℙ⊗d​t-a.e., as λ↓0.\displaystyle\big|\alpha\_{t}^{\*,x;N}-\pi^{\*,x;N,\lambda}\_{t}\big|\to 0\quad\mbox{$\mathbb{P}\otimes dt$-a.e., as $\lambda\downarrow 0$.} |  |

Furthermore, since |αt∗,x;N−πt∗,x;N,λ|≤2\big|\alpha\_{t}^{\*,x;N}-\pi^{\*,x;N,\lambda}\_{t}\big|\leq 2, ℙ⊗d​t\mathbb{P}\otimes dt-a.e., for all N∈ℕN\in\mathbb{N} and λ>0\lambda>0 (noting that (α∗,x;N)N∈ℕ⊆A(\alpha^{\*,x;N})\_{N\in\mathbb{N}}\subseteq{\mathcal{}A} and (π∗,x;N,λ)N∈ℕ,λ>0⊆Π(\pi^{\*,x;N,\lambda})\_{N\in\mathbb{N},\lambda>0}\subseteq\Pi), the dominated convergence theorem guarantees that the convergence in ([3.12](https://arxiv.org/html/2510.10260v1#S3.E12 "Equation 3.12 ‣ Corollary 3.6. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) holds for all N∈ℕN\in\mathbb{N}.

### 6.3 Proof of results in Section [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")

###### Proof 6.6 (Proof of Theorem [4.1](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

We start by proving (i). Let n∈ℕn\in\mathbb{N} be given. Since Y¯tx;N,λ≥Y¯tx;N,λ,π\overline{Y}^{x;N,\lambda}\_{t}\geq\overline{Y}^{x;N,\lambda,\pi}\_{t} ℙ\mathbb{P}-a.s., for all t∈[0,T]t\in[0,T] and π∈Π\pi\in\Pi (see Theorem [3.4](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii)), it suffices to show that Y¯tx;N,λ,πn+1≥Y¯tx;N,λ,πn\overline{Y}\_{t}^{x;N,\lambda,\pi^{n+1}}\geq\overline{Y}\_{t}^{x;N,\lambda,\pi^{n}}, ℙ\mathbb{P}-a.s., for all t∈[0,T]t\in[0,T].

For notational simplicity, let (Y¯n,Z¯n):=(Y¯x;N,λ,πn,Z¯x;N,λ,πn)(\overline{Y}^{n},\overline{Z}^{n}):=(\overline{Y}^{x;N,\lambda,\pi^{n}},\overline{Z}^{x;N,\lambda,\pi^{n}}), (Y¯n+1,Z¯n+1):=(Y¯x;N,λ,πn+1,Z¯x;N,λ,πn+1).(\overline{Y}^{n+1},\overline{Z}^{n+1}):=(\overline{Y}^{x;N,\lambda,\pi^{n+1}},\overline{Z}^{x;N,\lambda,\pi^{n+1}}).
In analogy, let
F¯n:=F¯x;N,λ,πn\overline{F}^{n}:=\overline{F}^{x;N,\lambda,\pi^{n}}, F¯n+1:=F¯x;N,λ,πn+1\overline{F}^{n+1}:=\overline{F}^{x;N,\lambda,\pi^{n+1}}.

Then we set for every t∈[0,T]t\in[0,T]

|  |  |  |
| --- | --- | --- |
|  | ϕt:=(F¯tn+1−F¯tn)​(Y¯tn,Z¯tn),Δ​Yt:=Y¯tn+1−Y¯tn,Δ​Zt:=(Δ​Zt,1,…,Δ​Zt,d)⊤,\displaystyle\phi\_{t}:=(\overline{F}\_{t}^{n+1}-\overline{F}\_{t}^{n})(\overline{Y}\_{t}^{n},\overline{Z}\_{t}^{n}),\quad\Delta Y\_{t}:=\overline{Y}\_{t}^{{n+1}}-\overline{Y}\_{t}^{{n}},\quad\Delta Z\_{t}:=(\Delta Z\_{t,1},\dots,\Delta Z\_{t,d})^{\top}, |  |

with Δ​Zt,i:=Z¯t,in+1−Z¯t,in\Delta Z\_{t,i}:=\overline{Z}\_{t,i}^{{n+1}}-\overline{Z}\_{t,i}^{{n}} for i=1,…,d,i=1,\dots,d, where Z¯t,in+1\overline{Z}\_{t,i}^{{n+1}} and Z¯t,in\overline{Z}\_{t,i}^{{n}} denote the ii-th component of Z¯tn+1\overline{Z}\_{t}^{{n+1}} and Z¯tn\overline{Z}\_{t}^{{n}}, respectively.

Moreover, we denote for every t∈[0,T]t\in[0,T] and i=1,…,di=1,\dots,d,

|  |  |  |
| --- | --- | --- |
|  | nt:=1Δ​Yt​(F¯tn+1​(Y¯tn+1,Z¯tn+1)−F¯tn+1​(Y¯tn,Z¯tn+1))​𝟏{Δ​Yt≠0},mt,i:=1Δ​Zt,i(F¯tn+1(Y¯tn+1,(Z¯t,1n,…,Z¯t,i−1n,Z¯t,in+1,…,Z¯t,dn+1)⊤)−F¯tn+1(Y¯tn+1,(Z¯t,1n,…,Z¯t,in,Z¯t,i+1n+1,…,Z¯t,dn+1)⊤))𝟏{Δ​Zt,i≠0}.\displaystyle\begin{aligned} n\_{t}:=&\frac{1}{\Delta Y\_{t}}\Big(\overline{F}\_{t}^{{n+1}}(\overline{Y}\_{t}^{n+1},\overline{Z}\_{t}^{n+1})-\overline{F}\_{t}^{{n+1}}(\overline{Y}\_{t}^{{n}},\overline{Z}\_{t}^{{n+1}})\Big){\bf 1}\_{\{\Delta Y\_{t}\neq 0\}},\\ m\_{t,i}:=&\frac{1}{\Delta Z\_{t,i}}\Big(\overline{F}^{{n+1}}\_{t}(\overline{Y}\_{t}^{n+1},(\overline{Z}\_{t,1}^{n},\dots,\overline{Z}\_{t,i-1}^{n},\overline{Z}\_{t,i}^{n+1},\dots,\overline{Z}\_{t,d}^{n+1})^{\top})\\ &\quad\quad\quad-\overline{F}^{{n+1}}\_{t}(\overline{Y}\_{t}^{n+1},(\overline{Z}\_{t,1}^{n},\dots,\overline{Z}\_{t,i}^{n},\overline{Z}\_{t,i+1}^{n+1},\dots,\overline{Z}\_{t,d}^{n+1})^{\top})\Big){\bf 1}\_{\{\Delta Z\_{t,i}\neq 0\}}.\end{aligned} |  |

Clearly, (Δ​Y,Δ​Z)(\Delta Y,\Delta Z) satisfies the following BSDE: for t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | Δ​Yt=∫tT(ns​Δ​Ys+ms⊤​Δ​Zs+ϕs)​𝑑s−∫tTΔ​Zs​𝑑Bs.\Delta Y\_{t}=\int\_{t}^{T}\left(n\_{s}\Delta Y\_{s}+m\_{s}^{\top}\Delta Z\_{s}+\phi\_{s}\right)ds-\int\_{t}^{T}\Delta Z\_{s}dB\_{s}. |  |

Moreover, by construction ([4.1](https://arxiv.org/html/2510.10260v1#S4.E1 "Equation 4.1 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), πtn+1=argmaxa∈[0,1]​{N​(R​(Xtx)−Y¯tn)​a−λ​H​(a)}{\pi}\_{t}^{n+1}=\mathrm{argmax}\_{a\in[0,1]}\{N(R(X\_{t}^{x})-\overline{Y}\_{t}^{n})a-\lambda{\mathcal{}H}(a)\}, for all t∈[0,T].t\in[0,T]. This ensures that ϕt≥0\phi\_{t}\geq 0 for all t∈[0,T]t\in[0,T].

Clearly, it holds that nt=−(βt+N​πtn+1)​𝟏{Δ​Yt≠0}n\_{t}=-(\beta\_{t}+N\pi\_{t}^{n+1}){\bf 1}\_{\{\Delta Y\_{t}\neq 0\}} for all t∈[0,T]t\in[0,T]. Moreover, by Assumption [2](https://arxiv.org/html/2510.10260v1#S2 "2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii) and the fact that πn+1∈Π\pi^{n+1}\in\Pi has values in [0,1][0,1], (nt)t∈[0,T](n\_{t})\_{t\in[0,T]} is uniformly bounded. Furthermore, by the Lipschitz property of gg (see Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii)), for every i=1,…,di=1,\dots,d, (mt,i)t∈[0,T](m\_{t,i})\_{t\in[0,T]} is uniformly bounded by κ>0\kappa>0.

Therefore, by letting Γt:=exp⁡(∫0tms​𝑑Bs+∫0t(−ns−12​|ms|2)​𝑑s)\Gamma\_{t}:=\exp(\int\_{0}^{t}m\_{s}dB\_{s}+\int\_{0}^{t}(-n\_{s}-\frac{1}{2}|m\_{s}|^{2})ds) for t∈[0,T]t\in[0,T], applying Itô’s formula into (Γt​Δ​Yt)t∈[0,T](\Gamma\_{t}\Delta Y\_{t})\_{t\in[0,T]} and taking the conditional expectation 𝔼t​[⋅]\mathbb{E}\_{t}[\cdot],

|  |  |  |
| --- | --- | --- |
|  | Δ​Yt=Γt−1​𝔼t​[∫tTΓs​ϕs​𝑑s],ℙ-a.s.,for all​t∈[0,T].\Delta Y\_{t}=\Gamma\_{t}^{-1}\mathbb{E}\_{t}\bigg[\int\_{t}^{T}\Gamma\_{s}\phi\_{s}ds\bigg],\quad\mbox{$\mathbb{P}$-a.s.,}\quad\mbox{for all}\;\;t\in[0,T]. |  |

Since ϕ≥0\phi\geq 0, we have Δ​Yt≥0\Delta Y\_{t}\geq 0 ℙ\mathbb{P}-a.s., for all t∈[0,T]t\in[0,T].
Therefore, the part (i) holds.

We now prove (ii). Set for every n∈ℕn\in\mathbb{N}

|  |  |  |
| --- | --- | --- |
|  | F¯:=F¯x;N,λ,Δn+1​F¯:=F¯−F¯n+1,Y¯:=Y¯x;N,λ,Δn​Y¯t:=Y¯t−Y¯tn\overline{F}:=\overline{F}^{{x;N,\lambda}},\quad\Delta^{n+1}\overline{F}:=\overline{F}-\overline{F}^{{n+1}},\quad\overline{Y}:=\overline{Y}^{x;N,\lambda},\quad\Delta^{n}\overline{Y}\_{t}:=\overline{Y}\_{t}-\overline{Y}^{n}\_{t} |  |

In analogy, set Z¯:=Z¯x;N,λ\overline{Z}:=\overline{Z}^{x;N,\lambda} and Δn​Z¯t:=Z¯t−Z¯n\Delta^{n}\overline{Z}\_{t}:=\overline{Z}\_{t}-\overline{Z}^{n}.

We first note that for any n∈ℕn\in\mathbb{N}, ω∈Ω\omega\in\Omega, t∈[0,T]t\in[0,T], y,y^∈ℝy,\hat{y}\in\mathbb{R} and z,z^∈ℝdz,\hat{z}\in\mathbb{R}^{d}

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F¯tn+1​(ω,y,z)−F¯tn+1​(ω,y^,z^)|\displaystyle|\overline{F}\_{t}^{{n+1}}(\omega,y,z)-\overline{F}\_{t}^{{n+1}}(\omega,\hat{y},\hat{z})| | ≤(βt​(ω)+N)​|y−y^|+|g​(ω,t,z)−g​(ω,t,z^)|\displaystyle\leq(\beta\_{t}(\omega)+N)|y-\hat{y}|+|g(\omega,t,z)-g(\omega,t,\hat{z})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(Cβ+κ+N)​(|y−y^|+|z−z^|).\displaystyle\leq(C\_{\beta}+\kappa+N)\big(|y-\hat{y}|+|z-\hat{z}|\big). |  |

Set C1:=Cβ+κ+N>0C\_{1}:=C\_{\beta}+\kappa+N>0. By the a priori estimate in [[70](https://arxiv.org/html/2510.10260v1#bib.bib70), Theorem 4.2.3], there exists some C2>0C\_{2}>0 (that depends on C1,T,dC\_{1},T,d but not on n,λn,\lambda), such that777For any t∈[0,T]t\in[0,T] and Y∈𝕊2​(ℝ)Y\in\mathbb{S}^{2}(\mathbb{R}), denote by ‖Y‖𝕊t22:=𝔼​[sups∈[t,T]|Ys|2]\|Y\|\_{\mathbb{S}^{2}\_{t}}^{2}:=\mathbb{E}[\sup\_{s\in[t,T]}|Y\_{s}|^{2}]. In analogy, for any Z∈𝕃2​(ℝd)Z\in\mathbb{L}^{2}(\mathbb{R}^{d}), denote by ‖Z‖𝕃t22:=𝔼​[∫tT|Zs|2​𝑑s]\|Z\|^{2}\_{\mathbb{L}^{2}\_{t}}:=\mathbb{E}[\int\_{t}^{T}|Z\_{s}|^{2}ds].

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Δn+1​Y¯‖𝕊t22+‖Δn+1​Z¯‖𝕃t22\displaystyle\|\Delta^{n+1}\overline{Y}\|\_{\mathbb{S}^{2}\_{t}}^{2}+\|\Delta^{n+1}\overline{Z}\|\_{\mathbb{L}^{2}\_{t}}^{2} | ≤C2​𝔼​[∫tT|Δn+1​F¯s​(Y¯s,Z¯s)|​𝑑s]2\displaystyle\leq C\_{2}\mathbb{E}\bigg[\int\_{t}^{T}\big|\Delta^{n+1}\overline{F}\_{s}(\overline{Y}\_{s},\overline{Z}\_{s})\big|ds\bigg]^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C2​T​∫tT𝔼​[|Δn+1​F¯s​(Y¯s,Z¯s)|2]​𝑑sfor all t∈[0,T],\displaystyle\leq C\_{2}T\int\_{t}^{T}\mathbb{E}\Big[\big|\Delta^{n+1}\overline{F}\_{s}(\overline{Y}\_{s},\overline{Z}\_{s})\big|^{2}\Big]ds\quad\mbox{for all $t\in[0,T]$}, |  |

where we have used the Jensen’s inequality with exponent 22 for the last inequality.

Moreover, by setting Lsn:=Nλ​(R​(Xsx)−Y¯sn)L^{n}\_{s}:=\frac{N}{\lambda}(R(X^{x}\_{s})-\overline{Y}^{n}\_{s}) and Ls:=Nλ​(R​(Xsx)−Y¯s)L\_{s}:=\frac{N}{\lambda}(R(X^{x}\_{s})-\overline{Y}\_{s}) and noting that πsn+1=(1+e−Lsn)−1\pi\_{s}^{n+1}=(1+e^{-L\_{s}^{n}})^{-1},
we compute that for all s∈[t,T]s\in[t,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Δn+1​F¯s​(Y¯s,Z¯s)|\displaystyle\big|\Delta^{n+1}\overline{F}\_{s}(\overline{Y}\_{s},\overline{Z}\_{s})\big| | =λ​|(Ls−Lsn)−Ls−Lsn1+e−Lsn+log⁡(1+e−Lsn)−log⁡(1+e−Ls)|\displaystyle=\lambda\bigg|(L\_{s}-L^{n}\_{s})-\frac{L\_{s}-L^{n}\_{s}}{1+e^{-L^{n}\_{s}}}+\log(1+e^{-L^{n}\_{s}})-\log(1+e^{-L\_{s}})\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤3​λ​|Ls−Lsn|=3​N​|Δn​Y¯s|\displaystyle\leq 3\lambda|L\_{s}-L^{n}\_{s}|=3N\big|\Delta^{n}\overline{Y}\_{s}\big| |  |

where we have used the fact that |log⁡(1+ex)−log⁡(1+ey)|≤|x−y||\log(1+e^{x})-\log(1+e^{y})|\leq|x-y| for all x,y∈ℝx,y\in\mathbb{R}.

By setting C3:=9​C2​T​N2>0C\_{3}:=9C\_{2}TN^{2}>0, we have shown that for all t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
| (6.24) |  | ‖Δn+1​Y¯‖𝕊t22+‖Δn+1​Z¯‖𝕃t22≤C3​∫tT𝔼​[|Δn​Y¯s|2]​𝑑s≤C3​∫tT‖Δn​Y¯‖𝕊s22​𝑑s.\displaystyle\|\Delta^{n+1}\overline{Y}\|\_{\mathbb{S}^{2}\_{t}}^{2}+\|\Delta^{n+1}\overline{Z}\|\_{\mathbb{L}^{2}\_{t}}^{2}\leq{C}\_{3}\int\_{t}^{T}\mathbb{E}\Big[\big|\Delta^{n}\overline{Y}\_{s}\big|^{2}\Big]ds\leq C\_{3}\int\_{t}^{T}\|\Delta^{n}\overline{Y}\|\_{\mathbb{S}^{2}\_{s}}^{2}ds. |  |

By using the same arguments presented for ([6.24](https://arxiv.org/html/2510.10260v1#S6.E24 "Equation 6.24 ‣ Proof 6.6 (Proof of Theorem 4.1). ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) iteratively,

|  |  |  |
| --- | --- | --- |
|  | ‖Δn+1​Y¯‖𝕊22+‖Δn+1​Z¯‖𝕃22≤C3​∫tT‖Δn​Y¯‖𝕊tn22​𝑑tn\displaystyle\|\Delta^{n+1}\overline{Y}\|\_{\mathbb{S}^{2}}^{2}+\|\Delta^{n+1}\overline{Z}\|\_{\mathbb{L}^{2}}^{2}\leq C\_{3}\int\_{t}^{T}\|\Delta^{n}\overline{Y}\|\_{\mathbb{S}^{2}\_{t\_{n}}}^{2}dt\_{n} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(C3)2​∫0T∫tnT‖Δn−1​Y¯‖𝕊tn−122​𝑑tn−1​𝑑tn\displaystyle\qquad\leq({C\_{3}})^{2}\int\_{0}^{T}\int\_{t\_{n}}^{T}\|\Delta^{n-1}\overline{Y}\|\_{\mathbb{S}^{2}\_{t\_{n-1}}}^{2}dt\_{n-1}\;dt\_{n} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤⋯\displaystyle\qquad\leq\cdots |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(C3)n​∫0T∫tnT⋯​∫t2T‖Δ1​Y¯‖𝕊t122​𝑑t1​⋯​𝑑tn−1​𝑑tn\displaystyle\qquad\leq({C}\_{3})^{n}\int\_{0}^{T}\int\_{t\_{n}}^{T}\cdots\int\_{t\_{2}}^{T}\|\Delta^{1}\overline{Y}\|\_{\mathbb{S}^{2}\_{t\_{1}}}^{2}dt\_{1}\cdots dt\_{n-1}\;dt\_{n} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(C3)n​‖Δ1​Y¯‖𝕊22​∫0T∫tnT⋯​∫t2T1​𝑑t1​⋯​𝑑tn−1​𝑑tn=(C3)n​Tnn!​‖Δ1​Y¯‖𝕊22,\displaystyle\qquad\leq({C}\_{3})^{n}\|\Delta^{1}\overline{Y}\|\_{\mathbb{S}^{2}}^{2}\int\_{0}^{T}\int\_{t\_{n}}^{T}\cdots\int\_{t\_{2}}^{T}1\;dt\_{1}\cdots dt\_{n-1}\;dt\_{n}=({C}\_{3})^{n}\frac{T^{n}}{n!}\|\Delta^{1}\overline{Y}\|\_{\mathbb{S}^{2}}^{2}, |  |

together with the 1-Lipschitz continuity of the logistic function (1+e−x)−1(1+e^{-x})^{-1}, we have

|  |  |  |
| --- | --- | --- |
|  | ‖πn+1−π∗‖𝕊22≤Nλ​𝔼​[supt∈[0,T]|Y¯tx;N,λ,πn−Y¯tx;N,λ|2]=Nλ​‖Δn​Y¯‖𝕊2.\displaystyle\|\pi^{n+1}-\pi^{\*}\|^{2}\_{\mathbb{S}^{2}}\leq\frac{N}{\lambda}\mathbb{E}\bigg[\sup\_{t\in[0,T]}|\overline{Y}^{x;N,\lambda,\pi^{n}}\_{t}-\overline{Y}^{x;N,\lambda}\_{t}|^{2}\bigg]=\frac{N}{\lambda}\|\Delta^{n}\overline{Y}\|\_{\mathbb{S}^{2}}. |  |

The monotonicity of πtn+1\pi^{n+1}\_{t} as n↑∞n\uparrow\infty is obvious from the logistic functional form on Y¯x;N,λ,πn\overline{Y}^{x;N,\lambda,\pi^{n}}, which completes the proof.

Let us consider the following controlled forward-backward SDEs for any πˇ∈Πˇ\check{\pi}\in\check{\Pi}: for any (t,x)∈[0,T]×ℝd(t,x)\in[0,T]\times\mathbb{R}^{d} and s∈[0,T]s\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
| (6.25) |  | Yˇst,x;N,λ,πˇ=R​(XˇTt,x)+∫sTFˇuN,λ,πˇ​(Xˇut,x,Yˇut,x;N,λ,πˇ,Zˇut,x;N,λ,πˇ)​𝟏{u≥t}​𝑑u−∫sTZˇut,x;N,λ,πˇ​𝑑Bu.\displaystyle\begin{aligned} \check{Y}\_{s}^{t,x;N,\lambda,\check{\pi}}&=R(\check{X}\_{T}^{t,x})+\int\_{s}^{T}\check{F}\_{u}^{N,\lambda,\check{\pi}}(\check{X}\_{u}^{t,x},\check{Y}\_{u}^{t,x;N,\lambda,\check{\pi}},\check{Z}\_{u}^{t,x;N,\lambda,\check{\pi}}){\bf 1}\_{\{u\geq t\}}du\\ &\quad-\int\_{s}^{T}\check{Z}\_{u}^{t,x;N,\lambda,\check{\pi}}dB\_{u}.\end{aligned} |  |

where Xˇst,x=x+(∫tsb~o​(s,Xˇst,x)​𝑑s+σ~o​(s,Xˇst,x)​d​Bs)​𝟏{s≥t}\check{X}\_{s}^{t,x}=x+(\int\_{t}^{s}\widetilde{b}^{o}(s,\check{X}\_{s}^{t,x})ds+\widetilde{\sigma}^{o}(s,\check{X}\_{s}^{t,x})dB\_{s}){\bf 1}\_{\{s\geq t\}}.

One can deduce that there exists a unique solution (Yˇt,x;N,λ,πˇ,Zˇt,x;N,λ,πˇ)(\check{Y}^{t,x;N,\lambda,\check{\pi}},\check{Z}^{t,x;N,\lambda,\check{\pi}}) to ([6.25](https://arxiv.org/html/2510.10260v1#S6.E25 "Equation 6.25 ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) (see Remark [3.3](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem3 "Remark 3.3. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). In particular, since Xˇ0,x=Xx\check{X}^{0,x}=X^{x} (see ([2.1](https://arxiv.org/html/2510.10260v1#S2.E1 "Equation 2.1 ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and Remark [2.3](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem3 "Remark 2.3. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii)), (Yˇ0,x;N,λ,πˇ,Zˇ0,x;N,λ,πˇ)(\check{Y}^{0,x;N,\lambda,\check{\pi}},\check{Z}^{0,x;N,\lambda,\check{\pi}}) is the unique solution (Y¯x;N,λ,πˇ​(Xx),Z¯x;N,λ,πˇ​(Xx))(\overline{Y}^{x;N,\lambda,\check{\pi}(X^{x})},\overline{Z}^{x;N,\lambda,\check{\pi}(X^{x})}) to ([3.5](https://arxiv.org/html/2510.10260v1#S3.E5 "Equation 3.5 ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) under πˇ​(Xx)=(πˇt​(Xtx))t∈[0,T]∈Π\check{\pi}(X^{x})=(\check{\pi}\_{t}(X\_{t}^{x}))\_{t\in[0,T]}\in\Pi.

Then we observe the following Markovian representation of ([6.25](https://arxiv.org/html/2510.10260v1#S6.E25 "Equation 6.25 ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

###### Lemma 6.7.

Under Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."), let πˇ∈Πˇ\check{\pi}\in\check{\Pi} be given.

* (i)

  There exist two Borel measurable functions vN,λ,πˇ:[0,T]×ℝd→ℝv^{N,\lambda,\check{\pi}}:[0,T]\times\mathbb{R}^{d}\to\mathbb{R} and wN,λ,πˇ:[0,T]×ℝd→ℝdw^{N,\lambda,\check{\pi}}:[0,T]\times\mathbb{R}^{d}\to\mathbb{R}^{d} such that for every t≤s≤Tt\leq s\leq T, ℙ⊗d​s\mathbb{P}\otimes ds-a.e.,

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (6.26) |  | Yˇst,x;N,λ,πˇ=vN,λ,πˇ​(s,Xˇst,x),Zˇst,x;N,λ,πˇ=((σ~o)⊤​wN,λ,πˇ)​(s,Xˇst,x),\displaystyle\check{Y}\_{s}^{t,x;N,\lambda,\check{\pi}}=v^{N,\lambda,\check{\pi}}(s,\check{X}\_{s}^{t,x}),\quad\check{Z}\_{s}^{t,x;N,\lambda,\check{\pi}}=\big((\widetilde{\sigma}^{o})^{\top}w^{N,\lambda,\check{\pi}}\big)(s,\check{X}\_{s}^{t,x}), |  |

  where (Yˇt,x;N,λ,πˇ,Zˇt,x;N,λ,πˇ)(\check{Y}^{t,x;N,\lambda,\check{\pi}},\check{Z}^{t,x;N,\lambda,\check{\pi}}) is the unique solution of ([6.25](https://arxiv.org/html/2510.10260v1#S6.E25 "Equation 6.25 ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).
* (ii)

  Furthermore, if πˇt​(⋅)\check{\pi}\_{t}(\cdot) is continuous on ℝd\mathbb{R}^{d} for any t∈[0,T]t\in[0,T],
  one can find a function vN,λ,πˇ:[0,T]×ℝd→ℝv^{N,\lambda,\check{\pi}}:[0,T]\times\mathbb{R}^{d}\to\mathbb{R} which satisfies the property given in ([6.26](https://arxiv.org/html/2510.10260v1#S6.E26 "Equation 6.26 ‣ item (i) ‣ Lemma 6.7. ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) and is a viscosity solution of the following PDE:

  |  |  |  |
  | --- | --- | --- |
  |  | (∂tv+ℒ​v)​(t,x)+FˇtN,λ,πˇ​(x,v​(t,x),((σ~o)⊤​∇v)​(t,x))=0,(t,x)∈[0,T)×ℝd,(\partial\_{t}v+\mathcal{L}v)(t,x)+\check{F}^{N,\lambda,\check{\pi}}\_{t}(x,v(t,x),((\widetilde{\sigma}^{o})^{\top}\nabla v)(t,x))=0,\quad(t,x)\in[0,T)\times\mathbb{R}^{d}, |  |

  with v​(T,⋅)=R​(⋅)v(T,\cdot)=R(\cdot), where the infinitesimal operator ℒ\mathcal{L} is defined as in Remark [4.2](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem2 "Remark 4.2. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).").
  In particular, vˇN,λ,πˇ\check{v}^{N,\lambda,\check{\pi}} is locally Lipschitz w.r.t. xx and Hölder continuous w.r.t. tt (Hence, it is continuous on [0,T]×ℝd[0,T]\times\mathbb{R}^{d}).

###### Proof 6.8.

We start with proving (i). According to [[19](https://arxiv.org/html/2510.10260v1#bib.bib19), Theorem 8.9], it suffices to show that the generator Fˇ⋅N,λ,πˇ​(⋅,⋅,⋅)\check{F}\_{\cdot}^{N,\lambda,\check{\pi}}(\cdot,\cdot,\cdot) given in ([4.2](https://arxiv.org/html/2510.10260v1#S4.E2 "Equation 4.2 ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfies the condition (M1b) given in [[19](https://arxiv.org/html/2510.10260v1#bib.bib19)] (noting that Xˇt,x\check{X}^{t,x} given in ([6.25](https://arxiv.org/html/2510.10260v1#S6.E25 "Equation 6.25 ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) satisfies (M1f) therein; see Remark [2.4](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Note that βt\beta\_{t} and πˇt​(x)\check{\pi}\_{t}(x) are uniformly bounded (see Setting [4](https://arxiv.org/html/2510.10260v1#S4 "4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), and gg is uniformly Lipschitz w.r.t. zz (see Definition [2.1](https://arxiv.org/html/2510.10260v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2 Optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Therefore, Fˇ⋅N,λ,πˇ​(⋅,⋅,⋅)\check{F}\_{\cdot}^{N,\lambda,\check{\pi}}(\cdot,\cdot,\cdot) is uniformly Lipschitz w.r.t. (y,z)(y,z) with the corresponding Lipschitz constant depending only on Cβ,λ,NC\_{\beta},\lambda,N (not on t,xt,x). Moreover, for all (t,x)∈[0,T]×ℝd(t,x)\in[0,T]\times\mathbb{R}^{d},

|  |  |  |
| --- | --- | --- |
|  | |FˇtN,λ,πˇ​(x,0,0)|≤|r​(x)|+N​|R​(x)​πˇt​(x)|+λ​|H​(πˇt​(x))|.|\check{F}\_{t}^{N,\lambda,\check{\pi}}(x,0,0)|\leq|r(x)|+N|R(x)\check{\pi}\_{t}(x)|+\lambda\big|{\mathcal{}H}\big(\check{\pi}\_{t}(x)\big)\big|. |  |

Note that |H​(πˇt​(⋅))||{\mathcal{}H}(\check{\pi}\_{t}(\cdot))| is bounded by log⁡2\log 2 (see Remark [3.1](https://arxiv.org/html/2510.10260v1#S3.Thmtheorem1 "Remark 3.1. ‣ 3 Exploratory framework: approximation of optimal stopping under ambiguity ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), and r​(⋅)r(\cdot) and R​(⋅)R(\cdot) are linearly growing. Therefore, there exists a constant CC only depends on Cr,R,N,λC\_{r,R},N,\lambda (not on (t,x)(t,x)) such that |FˇN,λ,πˇ​(t,x,0,0)|≤C​(1+|x|)|\check{F}^{N,\lambda,\check{\pi}}(t,x,0,0)|\leq C(1+|x|) for all (t,x)∈[0,T]×ℝd(t,x)\in[0,T]\times\mathbb{R}^{d}. Thus, (M1b) holds true.

We now prove (ii). As r​(x),R​(x),πˇt​(x)r(x),R(x),\check{\pi}\_{t}(x) are continuous w.r.t xx for all t∈[0,T]t\in[0,T],
the condition (M1bc\mathrm{M1b^{c}}) given in [[19](https://arxiv.org/html/2510.10260v1#bib.bib19)] holds true. Therefore, an application of [[19](https://arxiv.org/html/2510.10260v1#bib.bib19), Theorem 8.12] ensures
that vN,λ,πˇ​(t,x):=Yˇtt,x;N,λ,πˇv^{N,\lambda,\check{\pi}}(t,x):=\check{Y}\_{t}^{t,x;N,\lambda,\check{\pi}} for (t,x)∈[0,T]×ℝd(t,x)\in[0,T]\times\mathbb{R}^{d}
is a viscosity solution
of the PDE given in the statement (ii); see ([6.25](https://arxiv.org/html/2510.10260v1#S6.E25 "Equation 6.25 ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")). Moreover, using the flow property of {Xˇst,x;t≤s≤T,x∈ℝd}\{\check{X}\_{s}^{t,x};t\leq s\leq T,x\in\mathbb{R}^{d}\} and the uniqueness of the solution of ([6.25](https://arxiv.org/html/2510.10260v1#S6.E25 "Equation 6.25 ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")), we have for t≤s≤Tt\leq s\leq T, ℙ⊗d​s\mathbb{P}\otimes ds-a.e., vN,λ,πˇ​(s,Xˇst,x)=Yˇss,Xˇst,x;N,λ,πˇ=Yˇst,x;N,λ,πˇ,v^{N,\lambda,\check{\pi}}(s,\check{X}\_{s}^{t,x})=\check{Y}\_{s}^{s,\check{X}\_{s}^{t,x};N,\lambda,\check{\pi}}=\check{Y}\_{s}^{t,x;N,\lambda,\check{\pi}}, that is, the property in ([6.26](https://arxiv.org/html/2510.10260v1#S6.E26 "Equation 6.26 ‣ item (i) ‣ Lemma 6.7. ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")) holds.
Lastly, the regularity of vN,λ,πˇv^{N,\lambda,\check{\pi}} follows from the argument in the proof of [[19](https://arxiv.org/html/2510.10260v1#bib.bib19), Theorem 8.12], which employs the LpL^{p}-estimation techniques in
the proof of [[50](https://arxiv.org/html/2510.10260v1#bib.bib50), Lemma 2.1 and Corollary 2.10].

###### Proof 6.9 (Proof of Corollary [4.3](https://arxiv.org/html/2510.10260v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).")).

Part (i) follows immediately from an iterative application of Lemma [6.7](https://arxiv.org/html/2510.10260v1#S6.Thmtheorem7 "Lemma 6.7. ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (i). In a similary manner, Part (ii) is obtained by iteratively applying Lemma [6.7](https://arxiv.org/html/2510.10260v1#S6.Thmtheorem7 "Lemma 6.7. ‣ 6.3 Proof of results in Section 4 ‣ 6 Proofs ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175).") (ii). Indeed, as πˇt1​(⋅)\check{\pi}\_{t}^{1}(\cdot) is continuous, the corresponding function vN,λ,1v^{N,\lambda,1} satisfies all the properties in Part (i) and is also a viscosity solution of the PDE given in the statement (with the generator Fˇ⋅N,λ,πˇ1)\check{F}\_{\cdot}^{N,\lambda,\check{\pi}^{1}}). In particular, it is continuous on [0,T]×ℝd[0,T]\times\mathbb{R}^{d}, the next iteration policy πˇt2​(⋅)\check{\pi}\_{t}^{2}(\cdot) ,t∈[0,T]t\in[0,T], (defined as in ([4.4](https://arxiv.org/html/2510.10260v1#S4.E4 "Equation 4.4 ‣ item (i) ‣ Corollary 4.3. ‣ 4 Policy iteration theorem & RL algorithm ‣ ROBUST EXPLORATORY STOPPING UNDER AMBIGUITY IN REINFORCEMENT LEARNING Submitted to the editors October 11, 2025. \fundingH. Y. Wong acknowledges the support from the Research Grants Council of Hong Kong (grant DOI: GRF14308422). K. Park acknowledges the support from the National Research Foundation of Korea (grant DOI: RS-2025-02633175)."))) is also continuous on ℝd\mathbb{R}^{d}. The same argument can therefore be applied at each subsequent iteration. This completes the proof.

## References

* [1]

  D. Bartl, A. Neufeld, and K. Park, Numerical method for nonlinear Kolmogorov PDEs via sensitivity analysis, arXiv preprint arXiv:2403.11910, (2024).
* [2]

  D. Bartl, A. Neufeld, and K. Park, Sensitivity of robust optimization problems under drift and volatility uncertainty, Finance Stoch., arXiv:2311.11248, (2025+).
* [3]

  E. Bayraktar and S. Yao, Optimal stopping for non-linear expectations—Part I, Stochastic Process. Appl., 121 (2011), pp. 185–211.
* [4]

  E. Bayraktar and S. Yao, Optimal stopping for non-linear expectations—Part II, Stochastic Process. Appl., 121 (2011), pp. 212–264.
* [5]

  C. Beck, S. Becker, P. Cheridito, A. Jentzen, and A. Neufeld, Deep splitting method for parabolic PDEs, SIAM J. Sci. Comput., 43 (2021), pp. A3135–A3154.
* [6]

  S. Becker, P. Cheridito, and A. Jentzen, Deep optimal stopping, J. Mach. Learn. Res., 20 (2019), pp. 1–25.
* [7]

  S. Becker, P. Cheridito, A. Jentzen, and T. Welti, Solving high-dimensional optimal stopping problems using deep learning, Eur. J. Appl. Math., 32 (2021), pp. 470–514.
* [8]

  D. Blackwell and L. E. Dubins, An extension of Skorohod’s almost sure representation theorem, Proc. Amer. Math. Soc., 89 (1983), pp. 691–692.
* [9]

  J. Blanchet, M. Lu, T. Zhang, and H. Zhong, Double pessimism is provably efficient for distributionally robust offline reinforcement learning: Generic algorithm and robust partial coverage, Adv. Neural Inf. Process. Syst., 36 (2023), pp. 66845–66859.
* [10]

  K. Chen, K. Park, and H. Y. Wong, Robust dividend policy: Equivalence of Epstein-Zin and Maenhout preferences, arXiv preprint arXiv:2406.12305, (2024).
* [11]

  Z. Chen and L. Epstein, Ambiguity, risk, and asset returns in continuous time, Econometrica, 70 (2002), pp. 1403–1443.
* [12]

  F. Coquet, Y. Hu, J. Mémin, and S. Peng, Filtration-consistent nonlinear expectations and related gg-expectations, Probab. Theory Relat. Fields, 123 (2002), pp. 1–27.
* [13]

  M. Dai, Y. Dong, and Y. Jia, Learning equilibrium mean-variance strategy, Math. Finance, 33 (2023), pp. 1166–1212.
* [14]

  M. Dai, Y. Dong, Y. Jia, and X. Zhou, Learning merton’s strategies in an incomplete market: Recursive entropy regularization and biased gaussian exploration, SSRN Electronic Journal, (2023), <https://doi.org/10.2139/ssrn.4668480>.
* [15]

  M. Dai, Y. Sun, Z. Q. Xu, and X. Y. Zhou, Learning to optimally stop diffusion processes, with financial applications, Manag. Sci., (to appear).
* [16]

  J. Dianetti, G. Ferrari, and R. Xu, Exploratory optimal stopping: A singular control formulation, arXiv preprint arXiv:2408.09335, (2024).
* [17]

  Y. Dong, Randomized optimal stopping problem in continuous time and reinforcement learning algorithm, SIAM J. Control Optim., 62 (2024), pp. 1590–1614.
* [18]

  P. H. Dybvig, Dusenberry’s ratcheting of consumption: optimal dynamic consumption and investment given intolerance for any decline in standard of living, Rev. Econ. Stud., 62 (1995), pp. 287–313.
* [19]

  N. El Karoui, S. Hamadène, and A. Matoussi, Chapter Eight. BSDEs And Applications, Princeton University Press, Princeton, 2009, pp. 267–320.
  In: Indifference Pricing: Theory and Applications.
* [20]

  N. El Karoui, C. Kapoudjian, E. Pardoux, S. Peng, and M.-C. Quenez, Reflected solutions of backward SDE, and related obstacle problems for PDEs, Ann. Probab., 25 (1997), pp. 702–737.
* [21]

  N. El Karoui, S. Peng, and M. C. Quenez, Backward stochastic differential equations in finance, Math. Finance, 7 (1997), pp. 1–71.
* [22]

  L. G. Epstein and M. Schneider, Recursive multiple-priors, J. Econ. Theory, 113 (2003), pp. 1–31.
* [23]

  G. Ferrari, H. Li, and F. Riedel, Optimal consumption with Hindy–Huang–Kreps preferences under nonlinear expectations, Adv. Appl. Probab., 54 (2022), pp. 1222–1251.
* [24]

  P. A. Forsyth and K. R. Vetzal, Quadratic convergence for valuing American options using a penalty method, SIAM J. Sci. Comput., 23 (2002), pp. 2095–2122.
* [25]

  R. Frey and V. Köck, Convergence analysis of the deep splitting scheme: The case of partial integro-differential equations and the associated forward backward SDEs with jumps, SIAM J. Sci. Comput., 47 (2025), pp. A527–A552.
* [26]

  N. Frikha, L. Li, and D. Chee, An entropy regularized BSDE approach to Bermudan options and games, arXiv preprint arXiv:2509.18747, (2025).
* [27]

  M. Germain, H. Pham, and X. Warin, Approximation error analysis of some deep backward schemes for nonlinear pdes, SIAM J. Sci. Comput., 44 (2022), pp. A28–A56.
* [28]

  I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning, MIT Press, 2016.
* [29]

  D. Guo, D. Yang, H. Zhang, et al., Deepseek-r1 incentivizes reasoning in LLMs through reinforcement learning, Nature, 645 (2025), pp. 633–638.
* [30]

  J. Han, A. Jentzen, and W. E, Solving high-dimensional partial differential equations using deep learning, Proc. Natl. Acad. Sci.,, 115 (2018), pp. 8505–8510.
* [31]

  X. Han, R. Wang, and X. Y. Zhou, Choquet regularization for continuous-time reinforcement learning, SIAM J. Control Optim., 61 (2023), pp. 2777–2801.
* [32]

  Y.-J. Huang, Z. Wang, and Z. Zhou, Convergence of policy iteration for entropy-regularized stochastic control problems, SIAM J. Control Optim., 63 (2025), pp. 752–777.
* [33]

  C. Huré, H. Pham, and X. Warin, Deep backward schemes for high-dimensional nonlinear PDEs, Math. Comp., 89 (2020), p. 1.
* [34]

  J. Jacod and A. Shiryaev, Limit theorems for stochastic processes, vol. 288, Springer Science & Business Media, 2013.
* [35]

  Y. Jia and X. Y. Zhou, Policy evaluation and temporal-difference learning in continuous time and space: A martingale approach, J. Mach. Learn. Res., 23 (2022), pp. 1–55.
* [36]

  Y. Jia and X. Y. Zhou, Policy gradient and actor-critic learning in continuous time and space: Theory and algorithms, J. Mach. Learn. Res., 23 (2022), pp. 1–50.
* [37]

  Y. Jia and X. Y. Zhou, q-learning in continuous time, J. Mach. Learn. Res., 24 (2023), pp. 1–61.
* [38]

  P. Klibanoff, M. Marinacci, and S. Mukerji, A smooth model of decision making under ambiguity, Econometrica, 73 (2005), pp. 1849–1892.
* [39]

  J.-P. Lepeltier and M. Xu, Penalization method for reflected backward stochastic differential equations with one r.c.l.l. barrier, Stat. Probab. Lett., 75 (2005), pp. 58–66.
* [40]

  S. Levine, C. Finn, T. Darrell, and P. Abbeel, End-to-end training of deep visuomotor policies, J. Mach. Learn. Res., 17 (2016), p. 1334–1373.
* [41]

  X. Mao, Stochastic differential equations and applications, Elsevier, 2007.
* [42]

  M. Marinacci, Limit laws for non-additive probabilities and their frequentist interpretation, J. Econ. Theory, 84 (1999), pp. 145–195.
* [43]

  A. Mazzon and P. Tankov, Optimal stopping and divestment timing under scenario ambiguity and learning, arXiv preprint arXiv:2408.09349, (2024).
* [44]

  V. Mnih, K. Kavukcuoglu, D. Silver, et al., Human-level control through deep reinforcement learning, Nature, 518 (2015), pp. 529–533.
* [45]

  J. Morimoto and K. Doya, Robust reinforcement learning, Neural Comput., 17 (2005), pp. 335–359.
* [46]

  A. Neufeld, P. Schmocker, and S. Wu, Full error analysis of the random deep splitting method for nonlinear parabolic PDEs and PIDEs, arXiv preprint arXiv:2405.05192, (2024).
* [47]

  M. Nutz and J. Zhang, Optimal stopping under adverse nonlinear expectation and related games, Ann. Appl. Probab., 25 (2015), pp. 2503–2534.
* [48]

  K. Panaganti, Z. Xu, D. Kalathil, and M. Ghavamzadeh, Robust reinforcement learning using offline data, Adv. Neural Inf. Process. Syst., 35 (2022), pp. 32211–32224.
* [49]

  E. Pardoux and S. Peng, Adapted solution of a backward stochastic differential equation, Syst. Control Lett., 14 (1990), pp. 55–61.
* [50]

  E. Pardoux and S. Peng, Backward stochastic differential equations and quasilinear parabolic partial differential equations, in Stochastic Partial Differential Equations and Their Applications: Proceedings of IFIP WG 7/1 International Conference University of North Carolina at Charlotte, NC June 6–8, 1991, Springer, 2005, pp. 200–217.
* [51]

  K. Park, K. Chen, and H. Y. Wong, Irreversible consumption habit under ambiguity: Singular control and optimal GG-stopping time, Ann. Appl. Probab., 35 (2025), pp. 2471–2525.
* [52]

  K. Park and H. Y. Wong, Robust retirement with return ambiguity: Optimal GG-stopping time in dual space, SIAM J. Control Optim., 61 (2023), pp. 1009–1037.
* [53]

  S. Peng, Backward SDE and related gg-expectation, Pitman research notes in mathematics series, (1997), pp. 141–160.
* [54]

  S. Peng and M. Xu, The smallest gg-supermartingale and reflected BSDE with single and double L2L^{2} obstacles, Ann. Inst. H. Poincaré Probab. Statist., 41 (2005), pp. 605–630.
* [55]

  G. Peskir and A. Shiryaev, Optimal stopping and free-boundary problems, Springer, 2006.
* [56]

  P. E. Protter, Stochastic Integration and Differential Equations, Stochastic Modelling and Applied Probability, Springer, Berlin, Heidelberg, 2 ed., 2005.
* [57]

  A. M. Reppen, H. M. Soner, and V. Tissot-Daguette, Neural optimal stopping boundary, Math. Finance, 35 (2025), pp. 441–469.
* [58]

  F. Riedel, Optimal stopping with multiple priors, Econometrica, 77 (2009), pp. 857–908.
* [59]

  A. Roy, H. Xu, and S. Pokutta, Reinforcement learning under model mismatch, Adv. Neural Inf. Process. Syst., 30 (2017).
* [60]

  D. Silver, A. Huang, C. Maddison, et al., Mastering the game of Go with deep neural networks and tree search, Nature, 529 (2016), pp. 484–489.
* [61]

  D. Silver, J. Schrittwieser, K. Simonyan, et al., Mastering the game of Go without human knowledge, Nature, 550 (2017), pp. 354–359.
* [62]

  J. Sirignano and K. Spiliopoulos, DGM: A deep learning algorithm for solving partial differential equations, J. Comput. Phys., 375 (2018), pp. 1339–1364.
* [63]

  R. Sutton and A. Barto, Reinforcement learning: An introduction, IEEE Trans. Neural Netw., 9 (1998), pp. 1054–1054.
* [64]

  W. Tang, Y. P. Zhang, and X. Y. Zhou, Exploratory HJB equations and their convergence, SIAM J. Control Optim., 60 (2022), pp. 3191–3216.
* [65]

  A. Wald and J. Wolfowitz, Optimum character of the sequential probability ratio test, Ann. Math. Stat., (1948), pp. 326–339.
* [66]

  H. Wang, T. Zariphopoulou, and X. Y. Zhou, Reinforcement learning in continuous time and space: A stochastic control approach, J. Mach. Learn. Res., 21 (2020), pp. 1–34.
* [67]

  H. Wang and X. Y. Zhou, Continuous-time mean–variance portfolio selection: A reinforcement learning framework, Math. Finance, 30 (2020), pp. 1273–1308.
* [68]

  B. Wu and L. Li, Reinforcement learning for continuous-time mean-variance portfolio selection in a regime-switching market, J. Econ. Dyn. Control, 158 (2024), p. 104787.
* [69]

  H. Zhang, H. Chen, C. Xiao, B. Li, M. Liu, D. Boning, and C.-J. Hsieh, Robust deep reinforcement learning against adversarial perturbations on state observations, Adv. Neural Inf. Process. Syst., 33 (2020), pp. 21024–21037.
* [70]

  J. Zhang, Backward Stochastic Differential Equations, Springer New York, New York, 2017.