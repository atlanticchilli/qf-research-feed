---
authors:
- Tim J. Boonen
- Engel John C. Dela Vega
doc_id: arxiv:2511.11383v1
family_id: arxiv:2511.11383
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating
  Business Lines: The Case of Excess-of-Loss Reinsurance'
url_abs: http://arxiv.org/abs/2511.11383v1
url_html: https://arxiv.org/html/2511.11383v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tim J. Boonen
Department of Statistics and Actuarial Science, School of Computing and Data Science, University of Hong Kong, China. Email: tjboonen@hku.hk.
  
Engel John C. Dela Vega
Department of Statistics and Actuarial Science, School of Computing and Data Science, University of Hong Kong, China. Email: ejdv@hku.hk.

###### Abstract

This paper considers an insurer with two collaborating business lines that must make three critical decisions: (1) dividend payout, (2) a combination of proportional and excess-of-loss reinsurance coverage, and (3) capital injection between the lines. The reserve level of each line is modeled using a diffusion approximation, with the insurer’s objective being to maximize the weighted total discounted dividends paid until the first ruin time. We obtain the value function and the optimal strategies in closed form. We then prove that the optimal dividend payout strategy for bounded dividend rates is of threshold type, while for unbounded dividend rates it is of barrier type. The optimal combination of proportional and excess-of-loss reinsurance is shown to be pure excess-of-loss reinsurance. We also show that the optimal level of risk ceded to the reinsurer decreases as the aggregate reserve level increases. The optimal capital injection strategy involves transferring reserves to prevent the ruin of one line. Finally, numerical examples are presented to illustrate these optimal strategies.

## 1 Introduction

Optimal dividend payout problems have been a long-standing topic in the field of actuarial science, as dividends serve as a classical metric for assessing a company’s value. In the seminal paper of definetti1957, it is shown that the optimal strategy to distribute dividends is the one that maximizes the total discounted dividends paid to shareholders until bankruptcy time (i.e., the ruin time). This strategy is known as a *barrier strategy*, where dividends are paid only when the reserve level exceeds a certain level, called the barrier. In this framework, the amount of dividends to be paid is the excess of the reserve above the barrier, effectively capping the reserves at this level. Since definetti1957, numerous extensions and variations have been explored (see, e.g., albrecher2009; avanzi2009, for comprehensive reviews). However, it is important to note that most of these papers focus on the univariate case, where the company manages reserves for a single line of business.

We consider an extension of the classical problem studied by definetti1957, involving a company with multiple lines of business, each with its own reserves. This scenario introduces a level of complexity that requires a multivariate approach to understanding the dividend distribution. In this context, defining the ruin time is more complicated. In the univariate case, the ruin time is simply defined as the first time when a company’s reserves fall below zero. However, in the multivariate case, there are several definitions, including: (i) *first* ruin time: the first time when at least one reserve level falls below zero; (ii) *sum* ruin time: the first time when the sum of the reserves across all lines falls below zero; and (iii) *simultaneous* ruin time: the first time when all reserve levels fall below zero simultaneously. Consequently, much of the research in the multivariate case has focused on minimizing the probabilities of ruin (see, e.g., asmussenbook2010, Chapter XIII, and references therein).

Although many studies focus on minimizing the probabilities of ruin in the multivariate case, fewer have specifically aimed to maximize the total discounted dividends paid. To our knowledge, czarna2011 are the first to study the maximization of total discounted dividends for two business lines, using reserve processes that follow the Cramér-Lundberg (CL) model (i.e., a compound Poisson process). Subsequent studies using the CL model include liucheung2014, albrecher2017, azcue2019, azcuemuler2021, and strietzel2022. Reserve levels modeled as diffusion processes in the multivariate setting have been explored in gu2018, grandits2019saj, yang2025, and boonen2025.

In addition to maximizing the total discounted dividends, managing risks across multiple lines of business is essential to ensure the sustainability of dividend payouts. Risk control in the form of reinsurance has also been studied in the multivariate framework of optimal dividend problems. Proportional reinsurance has been explored in the multivariate case, as presented in czarna2011, liucheung2014, azcue2019, strietzel2022, yang2025, and boonen2025.

Given the complexities associated with the management of multiple business lines, effective risk management strategies are essential. One common approach is capital injection, which involves transferring reserves between lines to support a line that is at risk of its reserves falling below zero. This mechanism, sometimes referred to as *collaboration*, not only mitigates the risk of insolvency for individual lines but also improves the company’s capacity to distribute dividends. In albrecher2017, gu2018, and boonen2025, the rule of collaboration states that capital must be transferred from one line to another if a line is at risk of ruin, provided the transfer does not endanger the solvent line. This rule is modified in grandits2019saj, in which the solvent line is not obliged to transfer capital to the insolvent line.

The research agenda of this paper is to determine the optimal dividend payout, reinsurance, and capital injection strategies of an insurer with two business lines, subject to the following constraints: (1) the dividend rate may be bounded or unbounded; (2) the reinsurance contract combines proportional and excess-of-loss reinsurance; and (3) capital injections are used primarily to save
one line from ruin (in the univariate sense). The goal is to maximize the weighted total discounted dividends paid until the first ruin time. The related work of boonen2025 imposes stricter limitations, allowing only a bounded dividend rate and using only proportional reinsurance. We incorporate excess-of-loss reinsurance because it serves as a common alternative risk control mechanism in the univariate context of optimal dividend payout problems. Moreover, asmussen2000 shows that optimal excess-of-loss reinsurance outperforms optimal proportional reinsurance. When studying risk measures of terminal losses without dividends, aboagye2025 derive the optimal design of excess-of-loss reinsurance.

We summarize the main contributions of this paper:

1. 1.

   We show that the optimal combination of proportional and excess-of-loss reinsurance is pure excess-of-loss reinsurance. This finding aligns with the results of centeno1985, zhang2007, and liang2011 in the univariate setting.
2. 2.

   We show that the optimal dividend payout strategy for bounded dividend rates is a *threshold* strategy in which dividends are continuously paid at a fixed rate whenever the aggregate reserve level exceeds a threshold. We also show that for unbounded dividend rates, the optimal strategy is a barrier strategy. These findings are consistent with the results presented in asmussen2000 within the univariate setting.
3. 3.

   In the case of bounded dividend rates, we identify three scenarios based on the following conditions: (a) the sum of the maximum dividend rates of the two lines is “large enough”, (b) the maximum dividend rate of the more important line is “large enough”, and (c) the support of the claim size distribution is finite. This leads to three configurations for the reinsurance threshold level w0w\_{0} and the dividend threshold levels u1u\_{1} and u2u\_{2}: (i) w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2}; (ii) u1<w0≤u2u\_{1}<w\_{0}\leq u\_{2}; and (iii) u1≤u2<w0u\_{1}\leq u\_{2}<w\_{0}. These configurations are similar to those found in boonen2025. We also find that the reinsurance threshold level can exceed exactly one of the dividend threshold levels, which is a possibility ruled out in asmussen2000. For unbounded dividend rates, we identify two scenarios based on whether the support of the claim size distribution is finite.
4. 4.

   We show that the (excess-of-loss) reinsurance level decreases as the aggregate reserve level increases. Moreover, in the bounded support case, the reinsurance levels of both lines remain constant simultaneously when the aggregate reserve level is sufficiently large.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2511.11383v1#S2 "2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") introduces the model and the formulation of the problem. The gain of pure excess-of-loss reinsurance is discussed in Section [3](https://arxiv.org/html/2511.11383v1#S3 "3 The Gain of Pure Excess-of-Loss Reinsurance ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). Section [4](https://arxiv.org/html/2511.11383v1#S4 "4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") presents the main results for the case of bounded dividend rates, while Section [5](https://arxiv.org/html/2511.11383v1#S5 "5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") presents the case of unbounded dividend rates. Numerical examples are provided in Section [6](https://arxiv.org/html/2511.11383v1#S6 "6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). The proofs of the main results are detailed in Section [7](https://arxiv.org/html/2511.11383v1#S7 "7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). Section [8](https://arxiv.org/html/2511.11383v1#S8 "8 Conclusion ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") concludes.

## 2 Model

Consider a complete probability space (Ω,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}), where 𝔽:={ℱt}t≥0\mathbb{F}:=\{\mathcal{F}\_{t}\}\_{t\geq 0} is a right-continuous, ℙ\mathbb{P}-completed filtration to which all processes defined below, including the Brownian motions and the Poisson processes, are adapted.

We consider an insurer with two collaborating lines of business and model each line’s reserve using the classical Cramér-Lundberg model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi​(t)=xi+pi​t−∑k=1Λi​(t)Yi,k,P\_{i}(t)=x\_{i}+p\_{i}t-\sum\_{k=1}^{\Lambda\_{i}(t)}Y\_{i,k}, |  | (2.1) |

where, for i=1,2i=1,2, Λi:={Λi​(t)}t≥0\Lambda\_{i}:=\{\Lambda\_{i}(t)\}\_{t\geq 0} is a Poisson process with intensity λi>0\lambda\_{i}>0 that represents claim arrivals, and {Yi,k}k≥1\{Y\_{i,k}\}\_{k\geq 1} are independent and identically distributed (i.i.d.), nonnegative claim sizes with common distribution FiF\_{i} and finite first and second moments μ~i\widetilde{\mu}\_{i} and σ~i2\widetilde{\sigma}^{2}\_{i}. The premium rate pip\_{i} is assumed to be calculated under the expected value principle, i.e.,

|  |  |  |
| --- | --- | --- |
|  | pi=(1+κi)​λi​μ~i,p\_{i}=(1+\kappa\_{i})\lambda\_{i}\widetilde{\mu}\_{i}, |  |

where κi>0\kappa\_{i}>0 is the relative safety loading of Line ii.

The insurer has to make three decisions regarding the operation of each line:

1. 1.

   Reinsurance decision. The insurer arranges a combination of proportional and excess-of-loss reinsurance in the manner of centeno1985: For each line, the insurer first chooses a proportional retention level θi​(t)∈(0,1]\theta\_{i}(t)\in(0,1], and then chooses an excess-of-loss retention level πi​(t)∈[0,∞]\pi\_{i}(t)\in[0,\infty] such that the insurer’s kkth claim, net of proportional and excess-of-loss reinsurance, can be represented by min⁡{θi​(t)​Yi,k,πi​(t)}=θi​(t)​Yi,k∧πi​(t)\min\{\theta\_{i}(t)Y\_{i,k},\pi\_{i}(t)\}=\theta\_{i}(t)Y\_{i,k}\wedge\pi\_{i}(t). We assume that the reinsurer applies the same expected value principle and relative safety loading κi\kappa\_{i} as the insurer; this is sometimes referred to as “cheap reinsurance”.
2. 2.

   Dividend payout decision. The insurer chooses a dividend strategy to distribute profits to the shareholders of each line. Let Ci​(t)≥0C\_{i}(t)\geq 0 be the cumulative dividends paid by Line ii at time tt. The insurer can consider two types of dividend strategies: (1) an unbounded dividend rate: Ci​(t)C\_{i}(t) is an arbitrary nonnegative and nondecreasing function; and (2) a bounded dividend rate: Ci​(t)C\_{i}(t) satisfies Ci​(t)=∫0tci​(s)​𝑑sC\_{i}(t)=\int\_{0}^{t}c\_{i}(s)ds, where ci​(s)∈[0,c¯i]c\_{i}(s)\in[0,\overline{c}\_{i}] and c¯i>0\overline{c}\_{i}>0 is the maximum possible dividend rate. For the unbounded dividend rates, we treat C1C\_{1} and C2C\_{2} as singular controls.
3. 3.

   Capital injection decision. We assume that the insurer can inject capital from one line to the other without incurring any additional costs. The capital injection allows the insurer to prevent a line from bankruptcy by using the available resources within the company. Let Li​(t)L\_{i}(t) be the cumulative amount of capital transferred to Line ii from Line 3−i3-i. Moreover, we treat L1L\_{1} and L2L\_{2} as singular controls.

After the purchase of reinsurance contracts, the reserve level of Line ii is given by

|  |  |  |
| --- | --- | --- |
|  | Riθ,π​(t)=xi+piθ,π​t−∑k=1Λi​(t)(θi​(t)​Yi,k∧πi​(t)),R^{\theta,\pi}\_{i}(t)=x\_{i}+p\_{i}^{\theta,\pi}t-\sum\_{k=1}^{\Lambda\_{i}(t)}(\theta\_{i}(t)Y\_{i,k}\wedge\pi\_{i}(t)), |  |

where

|  |  |  |
| --- | --- | --- |
|  | piθ,π=pi−(1+κi)​𝔼​[∑k=1Λi​(t)(Yi,k−(θi​(t)​Yi,k∧πi​(t)))]=(1+κi)​λi​𝔼​(θi​(t)​Yi,k∧πi​(t)).p\_{i}^{\theta,\pi}=p\_{i}-(1+\kappa\_{i})\mathbb{E}\left[\sum\_{k=1}^{\Lambda\_{i}(t)}(Y\_{i,k}-(\theta\_{i}(t)Y\_{i,k}\wedge\pi\_{i}(t)))\right]=(1+\kappa\_{i})\lambda\_{i}\mathbb{E}(\theta\_{i}(t)Y\_{i,k}\wedge\pi\_{i}(t)). |  |

Following grandell1977, the diffusion approximation of {Riθ,π​(t)}t≥0\{R^{\theta,\pi}\_{i}(t)\}\_{t\geq 0} is given by

|  |  |  |
| --- | --- | --- |
|  | d​Ri​(t)=λi​κi​θi​(t)​μi​(πi​(t)θi​(t))​d​t+λi​θi​(t)​σi​(πi​(t)θi​(t))​d​Wi​(t),dR\_{i}(t)=\lambda\_{i}\kappa\_{i}\theta\_{i}(t)\mu\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)dt+\sqrt{\lambda\_{i}}\theta\_{i}(t)\sigma\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)dW\_{i}(t), |  |

where W1:={W1​(t)}t≥0W\_{1}:=\{W\_{1}(t)\}\_{t\geq 0} and W2:={W2​(t)}t≥0W\_{2}:=\{W\_{2}(t)\}\_{t\geq 0} are independent Brownian motions and are independent of the Poisson processes Λ1\Lambda\_{1} and Λ2\Lambda\_{2}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | μi​(s):=∫0s[1−Fi​(y)]​𝑑yandσi2​(s):=∫0s2​y​[1−Fi​(y)]​𝑑y.\mu\_{i}(s):=\int\_{0}^{s}[1-{F}\_{i}(y)]dy\quad\mbox{and}\quad\sigma^{2}\_{i}(s):=\int\_{0}^{s}2y[1-{F}\_{i}(y)]dy. |  | (2.2) |

Without loss of generality, we assume λi=1\lambda\_{i}=1. Write F¯i​(y):=1−Fi​(y)\overline{F}\_{i}(y):=1-F\_{i}(y) and define

|  |  |  |
| --- | --- | --- |
|  | Mi:=inf{y≥0:F¯i​(y)=0}≤∞.M\_{i}:=\inf\{y\geq 0:\overline{F}\_{i}(y)=0\}\leq\infty. |  |

By definition, μi​(Mi)=μ~i\mu\_{i}(M\_{i})=\widetilde{\mu}\_{i} and σi2​(Mi)=σ~i2\sigma\_{i}^{2}(M\_{i})=\widetilde{\sigma}\_{i}^{2}. Moreover, we have πi​(t)∈[0,Mi]\pi\_{i}(t)\in[0,M\_{i}].

Let θi:={θi​(t)}t≥0\theta\_{i}:=\{\theta\_{i}(t)\}\_{t\geq 0}, πi:={πi​(t)}t≥0\pi\_{i}:=\{\pi\_{i}(t)\}\_{t\geq 0}, Ci:={Ci​(t)}t≥0C\_{i}:=\{C\_{i}(t)\}\_{t\geq 0}, and Li:={Li​(t)}t≥0L\_{i}:=\{L\_{i}(t)\}\_{t\geq 0} be the proportional reinsurance, excess-of-loss reinsurance, dividend payout, and capital injection strategies, respectively, of Line ii, for i=1,2i=1,2. Given an admissible control u:=(θ1,θ2,π1,π2,C1,C2,L1,L2)u:=(\theta\_{1},\theta\_{2},\pi\_{1},\pi\_{2},C\_{1},C\_{2},L\_{1},L\_{2}), the controlled reserve process of Line ii, denoted by Xi:=XiuX\_{i}:=X\_{i}^{u}, follows the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xi​(t)=κi​θi​(t)​μi​(πi​(t)θi​(t))​d​t+θi​(t)​σi​(πi​(t)θi​(t))​d​Wi​(t)−d​Ci​(t)+d​Li​(t)−d​L3−i​(t),dX\_{i}(t)=\kappa\_{i}\theta\_{i}(t)\mu\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)dt+\theta\_{i}(t)\sigma\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)dW\_{i}(t)-dC\_{i}(t)+dL\_{i}(t)-dL\_{3-i}(t), |  | (2.3) |

where Xi​(0)=xi≥0X\_{i}(0)=x\_{i}\geq 0 is the initial reserve of Line ii. We define the corresponding ruin time as the first ruin time defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ:=inf{t≥0:min⁡{X1​(t),X2​(t)}<0}.\tau:=\inf\{t\geq 0:\min\{X\_{1}(t),X\_{2}(t)\}<0\}. |  | (2.4) |

We formally define admissible strategies as follows:

###### Definition 2.1.

A strategy uu is said to be admissible if uu is adapted to the filtration 𝔽\mathbb{F} and satisfies the following conditions:

* (i)

  θi​(t)∈(0,1]\theta\_{i}(t)\in(0,1] and πi​(t)∈[0,Mi]\pi\_{i}(t)\in[0,M\_{i}] for i=1,2i=1,2 and t≥0t\geq 0;
* (ii)

  CiC\_{i} and LiL\_{i} are nonnegative, nondecreasing, and right continuous with left limits, for i=1,2i=1,2.

Denote by 𝒰\mathcal{U} the set of all admissible strategies.

###### Remark 2.2.

The constraint on the proportional reinsurance variables, θi\theta\_{i}, implies that the business lines cannot cede all risk to the reinsurer; that is, full reinsurance is not allowed. On the other hand, the excess-of-loss retention can take any nonnegative value, including infinity. We say that FiF\_{i} has a bounded support if Mi<∞M\_{i}<\infty, and has unbounded support otherwise. We can interpret πi​(t)=Mi\pi\_{i}(t)=M\_{i} as Line ii retaining all risk; that is, Line ii does not engage in any reinsurance.

The goal of the insurer is to determine optimal dividend, (proportional and excess-of-loss) reinsurance, and capital injection strategies that maximize the weighted average of the dividend payouts from both lines up to the ruin time. That is, the insurer is faced with the following maximization problem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(x1,x2)\displaystyle V(x\_{1},x\_{2}) | :=supu∈𝒰J​(x1,x2;u),\displaystyle=\sup\_{u\in\mathcal{U}}J(x\_{1},x\_{2};u), |  | (2.5) |
|  | J​(x1,x2;u)\displaystyle J(x\_{1},x\_{2};u) | :=𝔼​[a​∫0τe−δ​t​𝑑C1​(t)+(1−a)​∫0τe−δ​t​𝑑C2​(t)],\displaystyle=\mathbb{E}\left[a\int\_{0}^{\tau}e^{-\delta t}dC\_{1}(t)+(1-a)\int\_{0}^{\tau}e^{-\delta t}dC\_{2}(t)\right], |  |

where a∈[0,1]a\in[0,1] is a weighting factor that reflects the relative importance of Line 11 for the company, δ>0\delta>0 is the discount factor, and the expectation 𝔼\mathbb{E} is taken under X1​(0)=x1X\_{1}(0)=x\_{1} and X2​(0)=x2X\_{2}(0)=x\_{2}. We denote the objective function by JJ and the value function by VV.

###### Remark 2.3.

From the definition of the value function VV, we can see that VV is increasing in both arguments x1x\_{1} and x2x\_{2}; that is, VV increases as the initial reserves increase.

## 3 The Gain of Pure Excess-of-Loss Reinsurance

In this section, we will show that an optimal reinsurance, dividend payout, and capital injection strategy is of the form u0:=(1,1,π10,π20,C10,C20,L10,L20)∈𝒰u\_{0}:=(1,1,\pi^{0}\_{1},\pi\_{2}^{0},C\_{1}^{0},C\_{2}^{0},L\_{1}^{0},L\_{2}^{0})\in\mathcal{U}; that is, the optimal combination of proportional and excess-of-loss reinsurance strategies is the pure excess-of-loss reinsurance.

###### Lemma 3.1.

Define

|  |  |  |
| --- | --- | --- |
|  | hi​(s):=σi2​(s)μi2​(s).h\_{i}(s):=\frac{\sigma\_{i}^{2}(s)}{\mu^{2}\_{i}(s)}. |  |

Then, hi​(s)h\_{i}(s) is an increasing function for s>0s>0.

###### Proof.

Taking the derivative yields

|  |  |  |
| --- | --- | --- |
|  | hi′​(s)=2​F¯i​(s)​[s​μi​(s)−σi2​(s)]μi3​(s).h^{\prime}\_{i}(s)=\frac{2\overline{F}\_{i}(s)\left[s\mu\_{i}(s)-\sigma\_{i}^{2}(s)\right]}{\mu\_{i}^{3}(s)}. |  |

Since 0≤Yi,k∧s≤s0\leq Y\_{i,k}\wedge s\leq s, we have 𝔼​(Yi,k∧s)2≤𝔼​(s​(Yi,k∧s))=s​𝔼​(Yi,k∧s)\mathbb{E}(Y\_{i,k}\wedge s)^{2}\leq\mathbb{E}(s(Y\_{i,k}\wedge s))=s\mathbb{E}(Y\_{i,k}\wedge s), and thus

|  |  |  |
| --- | --- | --- |
|  | σi2​(s)=𝔼​(Yi,k∧s)2≤s​𝔼​(Yi,k∧s)=s​μi​(s).\sigma\_{i}^{2}(s)=\mathbb{E}(Y\_{i,k}\wedge s)^{2}\leq s\mathbb{E}(Y\_{i,k}\wedge s)=s\mu\_{i}(s). |  |

This implies that hi′​(s)≥0h\_{i}^{\prime}(s)\geq 0, which completes the proof.
∎

###### Proposition 3.2.

For any fixed admissible control u=(θ1,θ2,π1,π2,C1,C2,L1,L2)u=(\theta\_{1},\theta\_{2},\pi\_{1},\pi\_{2},C\_{1},C\_{2},L\_{1},L\_{2}), where θi​(t)∈(0,1)\theta\_{i}(t)\in(0,1), there exists an admissible control u0=(1,1,π10,π20,C10,C20,L10,L20)u\_{0}=(1,1,\pi^{0}\_{1},\pi\_{2}^{0},C\_{1}^{0},C\_{2}^{0},L\_{1}^{0},L\_{2}^{0}) such that

|  |  |  |
| --- | --- | --- |
|  | J​(x1,x2;u)≤J​(x1,x2;u0).J(x\_{1},x\_{2};u)\leq J(x\_{1},x\_{2};u\_{0}). |  |

###### Proof.

For any fixed θi​(t)∈(0,1)\theta\_{i}(t)\in(0,1), πi​(t)\pi\_{i}(t), Ci​(t)C\_{i}(t), and Li​(t)L\_{i}(t), there exists a unique πi0​(t)\pi\_{i}^{0}(t) such that

|  |  |  |
| --- | --- | --- |
|  | θi​(t)​σi​(πi​(t)θi​(t))=σi​(πi0​(t)),i=1,2.\theta\_{i}(t)\sigma\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)=\sigma\_{i}(\pi\_{i}^{0}(t)),\quad i=1,2. |  |

Since σi\sigma\_{i} is a strictly increasing function and θi​(t)∈(0,1)\theta\_{i}(t)\in(0,1), it follows that πi​(t)θi​(t)>πi0​(t)\frac{\pi\_{i}(t)}{\theta\_{i}(t)}>\pi\_{i}^{0}(t). By Lemma [3.1](https://arxiv.org/html/2511.11383v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3 The Gain of Pure Excess-of-Loss Reinsurance ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"),

|  |  |  |
| --- | --- | --- |
|  | h​(πi0​(t))≤h​(πi​(t)θi​(t)).h(\pi\_{i}^{0}(t))\leq h\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right). |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | θi2​(t)=σi2​(πi0​(t))σi2​(πi​(t)θi​(t))≤μi2​(πi0​(t))μi2​(πi​(t)θi​(t)),\theta\_{i}^{2}(t)=\frac{\sigma^{2}\_{i}(\pi\_{i}^{0}(t))}{\sigma^{2}\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)}\leq\frac{\mu^{2}\_{i}(\pi\_{i}^{0}(t))}{\mu^{2}\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)}, |  |

which implies that

|  |  |  |
| --- | --- | --- |
|  | θi​(t)​μi​(πi​(t)θi​(t))≤μi​(πi0​(t)).\theta\_{i}(t)\mu\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)\leq\mu\_{i}(\pi\_{i}^{0}(t)). |  |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci0​(t)\displaystyle C^{0}\_{i}(t) | :=Ci​(t)+κi​∫0t[μi​(πi0​(s))−θi​(s)​μi​(πi​(s)θi​(s))]​𝑑s≥Ci​(t),\displaystyle=C\_{i}(t)+\kappa\_{i}\int\_{0}^{t}\left[\mu\_{i}(\pi\_{i}^{0}(s))-\theta\_{i}(s)\mu\_{i}\left(\frac{\pi\_{i}(s)}{\theta\_{i}(s)}\right)\right]ds\geq C\_{i}(t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Li0​(t)\displaystyle L^{0}\_{i}(t) | :=Li​(t).\displaystyle=L\_{i}(t). |  |

Then u0u\_{0} is an admissible control and

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xiu0​(t)\displaystyle dX^{u\_{0}}\_{i}(t) | =κi​μi​(πi0​(t))​d​t+σi​(πi0​(t))​d​Wi​(t)−d​Ci0​(t)+d​Li0​(t)−d​L3−i0​(t)\displaystyle=\kappa\_{i}\mu\_{i}(\pi\_{i}^{0}(t))\mathrm{d}t+\sigma\_{i}(\pi\_{i}^{0}(t))\mathrm{d}W\_{i}(t)-\mathrm{d}C^{0}\_{i}(t)+\mathrm{d}L^{0}\_{i}(t)-\mathrm{d}L^{0}\_{3-i}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =κi​θi​(t)​μi​(πi​(t)θi​(t))​d​t+θi​(t)​σi​(πi​(t)θi​(t))​d​Wi​(t)−d​Ci​(t)+d​Li​(t)−d​L3−i​(t).\displaystyle=\kappa\_{i}\theta\_{i}(t)\mu\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)\mathrm{d}t+\theta\_{i}(t)\sigma\_{i}\left(\frac{\pi\_{i}(t)}{\theta\_{i}(t)}\right)\mathrm{d}W\_{i}(t)-\mathrm{d}C\_{i}(t)+\mathrm{d}L\_{i}(t)-\mathrm{d}L\_{3-i}(t). |  |

Hence, Xiu0​(t)​=𝒟​Xiu​(t)X^{u\_{0}}\_{i}(t)\overset{\mathscr{D}}{=}X^{u}\_{i}(t) while Ci0​(t)≥Ci​(t)C^{0}\_{i}(t)\geq C\_{i}(t) and Li0​(t)=Li​(t)L^{0}\_{i}(t)=L\_{i}(t) for all tt. The result then follows.
∎

Write u1:=(1,1,π1,π2,C1,C2,L1,L2)∈𝒰u\_{1}:=(1,1,\pi\_{1},\pi\_{2},C\_{1},C\_{2},L\_{1},L\_{2})\in\mathcal{U}. The above proposition implies the following:

|  |  |  |
| --- | --- | --- |
|  | V​(x1,x2)=supu1∈𝒰J​(x1,x2;u1).V(x\_{1},x\_{2})=\sup\_{u\_{1}\in\mathcal{U}}J(x\_{1},x\_{2};u\_{1}). |  |

Hence, we only need to consider pure excess-of-loss reinsurance strategies to solve the maximization problem in ([2.5](https://arxiv.org/html/2511.11383v1#S2.E5 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

## 4 Bounded Dividend Rates

In this section, we consider the case in which the dividend rate of Line ii is bounded above by some constant c¯i∈(0,∞)\overline{c}\_{i}\in(0,\infty). In this case, we can represent Ci​(t)C\_{i}(t) as

|  |  |  |
| --- | --- | --- |
|  | Ci​(t)=∫0tci​(s)​ds,ci​(s)∈[0,c¯i].C\_{i}(t)=\int\_{0}^{t}c\_{i}(s)\,\mathrm{d}s,\quad c\_{i}(s)\in[0,\overline{c}\_{i}]. |  |

We henceforth represent the dividend control by the rates c1c\_{1} and c2c\_{2}. Using the results of the previous section, we can then rewrite the reserve process of Line ii given in ([2.3](https://arxiv.org/html/2511.11383v1#S2.E3 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) as

|  |  |  |
| --- | --- | --- |
|  | d​Xi​(t)=[κi​μi​(πi​(t))−ci​(t)]​d​t+σi​(πi​(t))​d​Wi​(t)+d​Li​(t)−d​L3−i​(t),dX\_{i}(t)=\left[\kappa\_{i}\mu\_{i}(\pi\_{i}(t))-c\_{i}(t)\right]dt+\sigma\_{i}(\pi\_{i}(t))dW\_{i}(t)+dL\_{i}(t)-dL\_{3-i}(t), |  |

and the value function defined in ([2.5](https://arxiv.org/html/2511.11383v1#S2.E5 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x1,x2)=supu1∈𝒰𝔼​[a​∫0τe−δ​t​c1​(t)​𝑑t+(1−a)​∫0τe−δ​t​c2​(t)​𝑑t].V(x\_{1},x\_{2})=\sup\_{u\_{1}\in\mathcal{U}}\mathbb{E}\left[a\int\_{0}^{\tau}e^{-\delta t}c\_{1}(t)dt+(1-a)\int\_{0}^{\tau}e^{-\delta t}c\_{2}(t)dt\right]. |  | (4.1) |

###### Remark 4.1.

For the case of bounded dividend rates, we can immediately observe that as the initial reserves become sufficiently large, the lines pay the maximum dividend rates and VV approaches the limit a​c¯1+(1−a)​c¯2δ\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}.

For all πi∈[0,Mi]\pi\_{i}\in[0,M\_{i}] and ci∈[0,c¯i]c\_{i}\in[0,\overline{c}\_{i}], define the generator ℒπ,c​(ϕ)\mathcal{L}^{\pi,c}(\phi) for some C2,2C^{2,2} function ϕ\phi by

|  |  |  |
| --- | --- | --- |
|  | ℒπ,c​(ϕ)=∑i=12[[κi​μi​(πi)−ci]​∂ϕ∂xi+12​σi2​(πi)​∂2ϕ∂xi2]−δ​ϕ+a​c1+(1−a)​c2.\mathcal{L}^{\pi,c}(\phi)=\sum\_{i=1}^{2}\left[\left[\kappa\_{i}\mu\_{i}(\pi\_{i})-c\_{i}\right]\frac{\partial\phi}{\partial x\_{i}}+\frac{1}{2}\sigma\_{i}^{2}(\pi\_{i})\frac{\partial^{2}\phi}{\partial x\_{i}^{2}}\right]-\delta\phi+ac\_{1}+(1-a)c\_{2}. |  |

We solve the problem in ([4.1](https://arxiv.org/html/2511.11383v1#S4.E1 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) via the dynamic programming principle. Using arguments similar to those in schmidli2007book, we can characterize the value function VV as a solution to the following Hamilton-Jacobi-Bellman (HJB) equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup{supπi∈[0,Mi],ci∈[0,c¯i]ℒπ,c​(V),∂V∂x1−∂V∂x2,∂V∂x2−∂V∂x1}=0,\sup\left\{\sup\_{\pi\_{i}\in[0,M\_{i}],c\_{i}\in[0,\overline{c}\_{i}]}\mathcal{L}^{\pi,c}(V),\frac{\partial V}{\partial x\_{1}}-\frac{\partial V}{\partial x\_{2}},\frac{\partial V}{\partial x\_{2}}-\frac{\partial V}{\partial x\_{1}}\right\}=0, |  | (4.2) |

with boundary condition V​(0,0)=0V(0,0)=0.
If we can find a classical solution to the HJB equation ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we can use a standard verification lemma, such as the one presented in schmidli2007book. This lemma essentially states that if a function satisfies the HJB equation and its boundary conditions, then the function is equal to the value function associated with the optimization problem. In this case, the classical solution we obtain will correspond to VV defined in ([4.1](https://arxiv.org/html/2511.11383v1#S4.E1 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

We begin the analysis by supposing that a classical solution VV to the HJB equation in ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) exists. Since both ∂V∂x1−∂V∂x2≤0\frac{\partial V}{\partial x\_{1}}-\frac{\partial V}{\partial x\_{2}}\leq 0 and ∂V∂x2−∂V∂x1≤0\frac{\partial V}{\partial x\_{2}}-\frac{\partial V}{\partial x\_{1}}\leq 0 must hold by ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), it follows that ∂V∂x1=∂V∂x2\frac{\partial V}{\partial x\_{1}}=\frac{\partial V}{\partial x\_{2}}. Hence, there exists a univariate function g:x∈ℝ+↦ℝg:x\in\mathbb{R}\_{+}\mapsto\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | g​(x)=V​(x1,x2), with ​x:=x1+x2≥0.g(x)=V(x\_{1},x\_{2}),\text{ with }x:=x\_{1}+x\_{2}\geq 0. |  |

We then have the following

|  |  |  |
| --- | --- | --- |
|  | g′​(x)=∂V∂xi​(x1,x2)andg′′​(x)=∂2V∂xi​∂xj​(x1,x2),i,j=1,2.g^{\prime}(x)=\frac{\partial V}{\partial x\_{i}}(x\_{1},x\_{2})\quad\mbox{and}\quad g^{\prime\prime}(x)=\frac{\partial^{2}V}{\partial x\_{i}\partial x\_{j}}(x\_{1},x\_{2}),\quad i,j=1,2. |  |

To solve the optimization problem supπi∈[0,Mi],ci∈[0,c¯i]ℒπ,c​(V)\sup\_{\pi\_{i}\in[0,M\_{i}],c\_{i}\in[0,\overline{c}\_{i}]}\mathcal{L}^{\pi,c}(V), we first isolate the optimization over the dividend payout variable cic\_{i}:

|  |  |  |
| --- | --- | --- |
|  | supc1∈[0,c¯1],c2∈[0,c¯2]{(a−g′​(x))​c1+(1−a−g′​(x))​c2}.\sup\_{c\_{1}\in[0,\overline{c}\_{1}],c\_{2}\in[0,\overline{c}\_{2}]}\left\{(a-g^{\prime}(x))c\_{1}+(1-a-g^{\prime}(x))c\_{2}\right\}. |  |

This yields the following candidate optimal dividend rates

|  |  |  |
| --- | --- | --- |
|  | c^1​(x)={0,if g′​(x)>a,c¯1,if g′​(x)<a,andc^2​(x)={0,if g′​(x)>1−a,c¯2,if g′​(x)<1−a.\widehat{c}\_{1}(x)=\begin{cases}0,&\mbox{if $g^{\prime}(x)>a$},\\ \overline{c}\_{1},&\mbox{if $g^{\prime}(x)<a$},\end{cases}\quad\mbox{and}\quad\widehat{c}\_{2}(x)=\begin{cases}0,&\mbox{if $g^{\prime}(x)>1-a$},\\ \overline{c}\_{2},&\mbox{if $g^{\prime}(x)<1-a$}.\end{cases} |  |

Define the two constants u1u\_{1} and u2u\_{2} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | u1:=inf{u:g′​(u)=1−a}andu2:=inf{u:g′​(u)=a}.u\_{1}:=\inf\{u:g^{\prime}(u)=1-a\}\quad\mbox{and}\quad u\_{2}:=\inf\{u:g^{\prime}(u)=a\}. |  | (4.3) |

We first hypothesize that gg is a concave function; that is, g′′​(x)<0g^{\prime\prime}(x)<0 for all xx. By symmetry and without loss of generality, we assume a≤12a\leq\frac{1}{2}. Since gg is concave and a≤12a\leq\frac{1}{2}, we have u1≤u2u\_{1}\leq u\_{2}. We then have the following candidate for the optimal dividend strategies:

|  |  |  |
| --- | --- | --- |
|  | (c^1​(x),c^2​(x))={(0,0),if x<u1,(0,c¯2),if u1<x<u2,(c¯1,c¯2),if x>u2.\left(\widehat{c}\_{1}(x),\widehat{c}\_{2}(x)\right)=\begin{cases}(0,0),&\mbox{if $x<u\_{1}$},\\ (0,\overline{c}\_{2}),&\mbox{if $u\_{1}<x<u\_{2}$},\\ (\overline{c}\_{1},\overline{c}\_{2}),&\mbox{if $x>u\_{2}$}.\end{cases} |  |

Next, we solve the optimization over the reinsurance variable πi\pi\_{i}:

|  |  |  |
| --- | --- | --- |
|  | supπ1∈[0,M1],π2∈[0,M2]∑i=12[κi​μi​(πi)​g′​(x)+12​σi2​(πi)​g′′​(x)].\sup\_{\pi\_{1}\in[0,M\_{1}],\pi\_{2}\in[0,M\_{2}]}\sum\_{i=1}^{2}\left[\kappa\_{i}\mu\_{i}(\pi\_{i})g^{\prime}(x)+\frac{1}{2}\sigma\_{i}^{2}(\pi\_{i})g^{\prime\prime}(x)\right]. |  |

We then have the following candidate maximizer:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^1​(x)=−κ1​g′​(x)g′′​(x)andπ^2​(x)=−κ2​g′​(x)g′′​(x).\widehat{\pi}\_{1}(x)=-\kappa\_{1}\frac{g^{\prime}(x)}{g^{\prime\prime}(x)}\quad\mbox{and}\quad\widehat{\pi}\_{2}(x)=-\kappa\_{2}\frac{g^{\prime}(x)}{g^{\prime\prime}(x)}. |  | (4.4) |

We can express π^2\widehat{\pi}\_{2} as

|  |  |  |
| --- | --- | --- |
|  | π^2​(x)=κ2κ1​π^1​(x).\widehat{\pi}\_{2}(x)=\frac{\kappa\_{2}}{\kappa\_{1}}\widehat{\pi}\_{1}(x). |  |

Since the capital injection decision (L1,L2)(L\_{1},L\_{2}) is represented as a singular control, the first-order conditions do not apply, unlike for the reinsurance and dividend controls. We will determine the optimal capital injection strategy later by examining the boundaries of specified regions.

We define w0w\_{0} such that it satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^1​(w0)=M1.\widehat{\pi}\_{1}(w\_{0})=M\_{1}. |  | (4.5) |

The existence of w0w\_{0} will be studied in Theorems [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), and [4.4](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance").
By definition, we can interpret w0w\_{0} as the aggregate reserve level at which the insurer chooses *zero reinsurance* for Line 1. We refer to w0w\_{0} as the *reinsurance threshold level*. Without loss of generality, we assume that M2M1≥κ2κ1\frac{M\_{2}}{M\_{1}}\geq\frac{\kappa\_{2}}{\kappa\_{1}}. This assumption, combined with ([4.4](https://arxiv.org/html/2511.11383v1#S4.E4 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), implies that the threshold for the insurer to retain all risk for Line 1 is not greater than that of Line 2.

We introduce the following notations that will be used in the discussion:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | N¯1​(y)\displaystyle\overline{N}\_{1}(y) | :=κ1​μ1​(y)+κ2​μ2​(κ2κ1​y),N¯2​(y):=σ12​(y)+σ22​(κ2κ1​y),\displaystyle=\kappa\_{1}\mu\_{1}(y)+\kappa\_{2}\mu\_{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}y\right),\qquad\qquad\qquad\qquad\overline{N}\_{2}(y)=\sigma\_{1}^{2}(y)+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}y\right), |  | (4.6) |
|  | γ¯2±​(y)\displaystyle\overline{\gamma}\_{2\pm}(y) | :=−N¯1​(y)±N¯1​(y)2+2​δ​N¯2​(y)N¯2​(y),\displaystyle=\frac{-\overline{N}\_{1}(y)\pm\sqrt{\overline{N}\_{1}(y)^{2}+2\delta\overline{N}\_{2}(y)}}{\overline{N}\_{2}(y)}, |  |
|  | γ¯3±​(y)\displaystyle\overline{\gamma}\_{3\pm}(y) | :=−(N¯1​(y)−c¯2)±(N¯1​(y)−c¯2)2+2​δ​N¯2​(y)N¯2​(y),\displaystyle=\frac{-(\overline{N}\_{1}(y)-\overline{c}\_{2})\pm\sqrt{(\overline{N}\_{1}(y)-\overline{c}\_{2})^{2}+2\delta\overline{N}\_{2}(y)}}{\overline{N}\_{2}(y)}, |  |
|  | γ¯4−​(y)\displaystyle\overline{\gamma}\_{4-}(y) | :=−(N¯1​(y)−c¯1−c¯2)−(N¯1​(y)−c¯1−c¯2)2+2​δ​N¯2​(y)N¯2​(y).\displaystyle=\frac{-(\overline{N}\_{1}(y)-\overline{c}\_{1}-\overline{c}\_{2})-\sqrt{(\overline{N}\_{1}(y)-\overline{c}\_{1}-\overline{c}\_{2})^{2}+2\delta\overline{N}\_{2}(y)}}{\overline{N}\_{2}(y)}. |  |

Write Ni:=N¯i​(M1)N\_{i}:=\overline{N}\_{i}(M\_{1}), γ2±:=γ¯2±​(M1)\gamma\_{2\pm}:=\overline{\gamma}\_{2\pm}(M\_{1}), γ3±:=γ¯3±​(M1)\gamma\_{3\pm}:=\overline{\gamma}\_{3\pm}(M\_{1}), and γ4−:=γ¯4−​(M1)\gamma\_{4-}:=\overline{\gamma}\_{4-}(M\_{1}). In addition, we define two functions ψ,ζ:(−∞,0)↦ℝ\psi,\zeta:(-\infty,0)\mapsto\mathbb{R} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψ​(z)\displaystyle\psi(z) | :=(1−a−γ3−​z)​eγ3+​ζ​(z)+γ3−​z​eγ3−​ζ​(z)−a,\displaystyle=(1-a-\gamma\_{3-}z)e^{\gamma\_{3+}\,\zeta(z)}+\gamma\_{3-}ze^{\gamma\_{3-}\,\zeta(z)}-a, |  | (4.7) |
|  | ζ​(z)\displaystyle\zeta(z) | :=1γ3+−γ3−​ln⁡[γ3−​(γ4−−γ3−)​z(1−a−γ3−​z)​(γ3+−γ4−)].\displaystyle=\frac{1}{\gamma\_{3+}-\gamma\_{3-}}\ln\left[\frac{\gamma\_{3-}(\gamma\_{4-}-\gamma\_{3-})z}{(1-a-\gamma\_{3-}z)(\gamma\_{3+}-\gamma\_{4-})}\right]. |  |

We can now present the main results. The reinsurance threshold level w0w\_{0} plays an important role in the results. Its position relative to the dividend threshold levels u1u\_{1} and u2u\_{2} yields three mutually exclusive cases: (i) w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2} (Theorem [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), (ii) u1<w0≤u2u\_{1}<w\_{0}\leq u\_{2} (Theorem [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), and (iii) u1≤u2<w0u\_{1}\leq u\_{2}<w\_{0} (Theorem [4.4](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Each case has its corresponding analytical form of the value function and a dividend-reinsurance strategy (π1∗,π2∗,c1∗,c2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*},c\_{1}^{\*},c\_{2}^{\*}). Since the capital injection strategies L1∗L\_{1}^{\*} and L2∗L\_{2}^{\*} are modeled as singular controls, we obtain a uniform optimal strategy as discussed in Theorem [4.5](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). The main results also cover whether F1F\_{1} has bounded or unbounded support (i.e., M1<∞M\_{1}<\infty or M1=∞M\_{1}=\infty).

###### Theorem 4.2.

Suppose (i) M1<∞M\_{1}<\infty, (ii) c¯1+c¯2≥N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} and (iii) ψ​(αL​B)≤0\psi(\alpha\_{LB})\leq 0, where ψ\psi is defined by ([4.7](https://arxiv.org/html/2511.11383v1#S4.E7 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | αL​B\displaystyle\alpha\_{LB} | :=[(1−aγ3−−α0)​𝟙{c¯2≥N1−κ1​N22​M1+δ​M1κ1}+α0]​𝟙{N1>κ1​N22​M1}\displaystyle=\left[\left(\frac{1-a}{\gamma\_{3-}}-\alpha\_{0}\right)\mathds{1}\_{\left\{\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}\right\}}+\alpha\_{0}\right]\mathds{1}\_{\left\{N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}}\right\}} |  | (4.8) |
|  |  | +[(1−aγ3−−α¯)​𝟙{c¯2≥δ​N22​N1}+α¯]​𝟙{N1≤κ1​N22​M1},\displaystyle\qquad+\left[\left(\frac{1-a}{\gamma\_{3-}}-\underline{\alpha}\right)\mathds{1}\_{\left\{\overline{c}\_{2}\geq\frac{\delta N\_{2}}{2N\_{1}}\right\}}+\underline{\alpha}\right]\mathds{1}\_{\left\{N\_{1}\leq\frac{\kappa\_{1}N\_{2}}{2M\_{1}}\right\}}, |  |
|  | α0\displaystyle\alpha\_{0} | :=(1−a)​γ3+γ3+−γ3−​[N1δ−κ1​N22​δ​M1−1γ3+−c¯2δ],\displaystyle=\frac{(1-a)\gamma\_{3+}}{\gamma\_{3+}-\gamma\_{3-}}\left[\frac{N\_{1}}{\delta}-\frac{\kappa\_{1}N\_{2}}{2\delta M\_{1}}-\frac{1}{\gamma\_{3+}}-\frac{\overline{c}\_{2}}{\delta}\right], |  |
|  | α¯\displaystyle\underline{\alpha} | :=−(1−a)​γ3+γ3+−γ3−​(1γ3++c¯2δ).\displaystyle=-\frac{(1-a)\gamma\_{3+}}{\gamma\_{3+}-\gamma\_{3-}}\left(\frac{1}{\gamma\_{3+}}+\frac{\overline{c}\_{2}}{\delta}\right). |  |

We have the following results:

1. 1.

   w0w\_{0} defined in ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) exists and is given by

   |  |  |  |
   | --- | --- | --- |
   |  | w0=G​(M1),w\_{0}=G(M\_{1}), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | G​(y):=∫0yσ12​(z)+σ22​(κ2κ1​z)2​κ1​z​μ1​(z)+2​κ2​z​μ2​(κ2κ1​z)+2​δκ1​z2−κ1​(σ12​(z)+σ22​(κ2κ1​z))​𝑑z,G(y):=\int\_{0}^{y}\frac{\sigma\_{1}^{2}(z)+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}z\right)}{2\kappa\_{1}z\mu\_{1}(z)+2\kappa\_{2}z\mu\_{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}z\right)+\frac{2\delta}{\kappa\_{1}}z^{2}-\kappa\_{1}\left(\sigma\_{1}^{2}(z)+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}z\right)\right)}dz, |  | (4.9) |

   and u1u\_{1} and u2u\_{2}, defined in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), are explicitly given by

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | u1\displaystyle u\_{1} | =w0+1γ2+−γ2−​ln⁡(α2−​(γ2−​α3−1)α2+​(1−γ2+​α3)),\displaystyle=w\_{0}+\frac{1}{\gamma\_{2+}-\gamma\_{2-}}\ln\left(\frac{\alpha\_{2-}(\gamma\_{2-}\alpha\_{3}-1)}{\alpha\_{2+}(1-\gamma\_{2+}\alpha\_{3})}\right), |  | (4.10) |
   |  | andu2\displaystyle\text{and}\quad u\_{2} | =u1+1γ3+−γ3−​ln⁡(K3−​γ3−​(γ4−−γ3−)K3+​γ3+​(γ3+−γ4−)),\displaystyle=u\_{1}+\frac{1}{\gamma\_{3+}-\gamma\_{3-}}\ln\left(\frac{K\_{3-}\gamma\_{3-}(\gamma\_{4-}-\gamma\_{3-})}{K\_{3+}\gamma\_{3+}(\gamma\_{3+}-\gamma\_{4-})}\right), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | α2+:=−γ2−−κ1M1γ2+​(γ2+−γ2−),α2−:=γ2++κ1M1γ2−​(γ2+−γ2−),\alpha\_{2+}:=\frac{-\gamma\_{2-}-\frac{\kappa\_{1}}{M\_{1}}}{\gamma\_{2+}(\gamma\_{2+}-\gamma\_{2-})},\quad\alpha\_{2-}:=\frac{\gamma\_{2+}+\frac{\kappa\_{1}}{M\_{1}}}{\gamma\_{2-}(\gamma\_{2+}-\gamma\_{2-})}, |  | (4.11) |

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | α3:=1γ3++c¯2δ+(1−γ3−γ3+)​K3−1−a,K3+:=1γ3+​(1−a−K3−​γ3−),\alpha\_{3}:=\frac{1}{\gamma\_{3+}}+\frac{\overline{c}\_{2}}{\delta}+\left(1-\frac{\gamma\_{3-}}{\gamma\_{3+}}\right)\frac{K\_{3-}}{1-a},\quad K\_{3+}:=\frac{1}{\gamma\_{3+}}\left(1-a-K\_{3-}\gamma\_{3-}\right), |  | (4.12) |

   and K3−K\_{3-} is the unique solution to ψ​(z)=0\psi(z)=0 on (αL​B,αU​B)\left(\alpha\_{LB},\alpha\_{UB}\right) with

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | αU​B:=(1−a)​(γ3+−γ4−)γ3−​(γ3+−γ3−).\alpha\_{UB}:=\frac{(1-a)(\gamma\_{3+}-\gamma\_{4-})}{\gamma\_{3-}(\gamma\_{3+}-\gamma\_{3-})}. |  | (4.13) |

   The relation w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2} holds.
2. 2.

   The function gg, defined by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g​(x)={K1​∫0xexp⁡[∫zw0κ1G−1​(y)​𝑑y]​𝑑zif x<w0,K1​[α2+​eγ2+​(x−w0)+α2−​eγ2−​(x−w0)]if w0≤x<u1,K3+​eγ3+​(x−u1)+K3−​eγ3−​(x−u1)+(1−a)​c¯2δif u1≤x<u2,aγ4−​eγ4−​(x−u2)+a​c¯1+(1−a)​c¯2δif x≥u2,g(x)=\begin{cases}K\_{1}\int\_{0}^{x}\exp\left[\int^{w\_{0}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<w\_{0}$,}\\ K\_{1}\left[\alpha\_{2+}e^{\gamma\_{2+}(x-w\_{0})}+\alpha\_{2-}e^{\gamma\_{2-}(x-w\_{0})}\right]&\mbox{if $w\_{0}\leq x<u\_{1}$,}\\ K\_{3+}e^{\gamma\_{3+}(x-u\_{1})}+K\_{3-}e^{\gamma\_{3-}(x-u\_{1})}+\frac{(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $u\_{1}\leq x<u\_{2}$,}\\ \frac{a}{\gamma\_{4-}}e^{\gamma\_{4-}(x-u\_{2})}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $x\geq u\_{2}$,}\end{cases} |  | (4.14) |

   where G−1G^{-1} is the inverse of GG defined in ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"))
   and

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | K1=(1−a)​[α2+​γ2+​eγ2+​(u1−w0)+α2−​γ2−​eγ2−​(u1−w0)]−1,K\_{1}=(1-a)\left[\alpha\_{2+}\gamma\_{2+}e^{\gamma\_{2+}(u\_{1}-w\_{0})}+\alpha\_{2-}\gamma\_{2-}e^{\gamma\_{2-}(u\_{1}-w\_{0})}\right]^{-1}, |  | (4.15) |

   is a classical solution to the HJB equation in ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and thus equals the value function VV of the optimization problem in ([2.5](https://arxiv.org/html/2511.11383v1#S2.E5 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Moreover, gg is strictly concave.
3. 3.

   The optimal reinsurance and dividend strategies (π1∗,π2∗,c1∗,c2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*},c\_{1}^{\*},c\_{2}^{\*}) are given by

   |  |  |  |
   | --- | --- | --- |
   |  | (π1∗,π2∗,c1∗,c2∗)​(x)={(G−1​(x),κ2κ1​G−1​(x),0,0)if x<w0,(M1,κ2κ1​M1,0,0)if w0≤x<u1,(M1,κ2κ1​M1,0,c¯2)if u1≤x<u2,(M1,κ2κ1​M1,c¯1,c¯2)if x≥u2.(\pi\_{1}^{\*},\pi\_{2}^{\*},c\_{1}^{\*},c\_{2}^{\*})(x)=\begin{cases}\left(G^{-1}(x),\frac{\kappa\_{2}}{\kappa\_{1}}G^{-1}(x),0,0\right)&\mbox{if $x<w\_{0}$,}\\ \left(M\_{1},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{1},0,0\right)&\mbox{if $w\_{0}\leq x<u\_{1}$,}\\ \left(M\_{1},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{1},0,\overline{c}\_{2}\right)&\mbox{if $u\_{1}\leq x<u\_{2}$,}\\ \left(M\_{1},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{1},\overline{c}\_{1},\overline{c}\_{2}\right)&\mbox{if $x\geq u\_{2}$.}\end{cases} |  |

We first discuss the optimal dividend strategies (c1∗,c2∗)(c\_{1}^{\*},c\_{2}^{\*}). When the aggregate reserve level is low (i.e., x<u1x<u\_{1}), the lines do not distribute dividends. Recall that we assume greater importance assigned to Line 2 (i.e., a≤12a\leq\frac{1}{2}). As soon as the first threshold u1u\_{1} is crossed, Line 2 pays dividends at the maximum rate and Line 1 has to wait until the second threshold u2u\_{2} is crossed.

For the optimal reinsurance strategy (π1∗,π2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*}), recall that we also assume that M2M1≥κ2κ1\frac{M\_{2}}{M\_{1}}\geq\frac{\kappa\_{2}}{\kappa\_{1}}. This ensures that Line 1 does not purchase excess-of-loss reinsurance while Line 2 retains a constant level of risk on incoming claims when the aggregate reserve level is sufficiently large (i.e., x>w0x>w\_{0}).

Under condition (i), the distribution function F1F\_{1} has bounded support, which implies that Line 1 has bounded claim sizes. A sufficient condition for conditions (ii) and (iii) is c¯2>N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}>N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. This suggests that the maximum dividend rate of Line 1 can be relatively low while still satisfying the total maximum dividend rate condition. We also remark that the unique root of ψ\psi ensures that gg is differentiable at x=u2x=u\_{2}.

The next theorem discusses the case when conditions (i) and (ii) of Theorem [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") are still satisfied, while condition (iii) is not.

###### Theorem 4.3.

Suppose (i) M1<∞M\_{1}<\infty, (ii) c¯1+c¯2≥N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} and (iii) ψ​(αL​B)>0\psi(\alpha\_{LB})>0, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | αL​B:=(α0−α¯)​𝟙{c¯2>δ​N22​N1}+α¯.\alpha\_{LB}:=\left(\alpha\_{0}-\underline{\alpha}\right)\mathds{1}\_{\left\{\overline{c}\_{2}>\frac{\delta N\_{2}}{2N\_{1}}\right\}}+\underline{\alpha}. |  | (4.16) |

Here, α0\alpha\_{0} and α¯\underline{\alpha} are defined as in Theorem [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). We then have the following results:

1. 1.

   w0w\_{0} defined in ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) exists and is given by H​(w0)=M1H(w\_{0})=M\_{1}, where HH satisfies the following differential equation

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | dd​x​H​(x)=2​κ1​z​μ1​(H​(x))+2​κ2​z​μ2​(κ2κ1​H​(x))+2​δκ1​[H​(x)]2−2​c¯2​H​(x)σ12​(H​(x))+σ22​(κ2κ1​H​(x))−κ1,\frac{\mathrm{d}}{\mathrm{d}x}H(x)=\frac{2\kappa\_{1}z\mu\_{1}(H(x))+2\kappa\_{2}z\mu\_{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}H(x)\right)+\frac{2\delta}{\kappa\_{1}}\left[H(x)\right]^{2}-2\overline{c}\_{2}H(x)}{\sigma\_{1}^{2}(H(x))+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}H(x)\right)}-\kappa\_{1}, |  | (4.17) |

   and u1u\_{1} and u2u\_{2} defined in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) are explicitly given by

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | u1\displaystyle u\_{1} | =w0−1γ3+−γ3−​ln⁡(K3−​γ3−​(γ3−+κ1M1)K3+​γ3+​(−κ1M1−γ3+)),and\displaystyle=w\_{0}-\frac{1}{\gamma\_{3+}-\gamma\_{3-}}\ln\left(\frac{K\_{3-}\gamma\_{3-}\left(\gamma\_{3-}+\frac{\kappa\_{1}}{M\_{1}}\right)}{K\_{3+}\gamma\_{3+}\left(-\frac{\kappa\_{1}}{M\_{1}}-\gamma\_{3+}\right)}\right),\text{and} |  | (4.18) |
   |  | u2\displaystyle u\_{2} | =w0+1γ3+−γ3−​ln⁡((γ4−−γ3−)​(−κ1M1−γ3+)(γ3+−γ4−)​(γ3−+κ1M1)),\displaystyle=w\_{0}+\frac{1}{\gamma\_{3+}-\gamma\_{3-}}\ln\left(\frac{(\gamma\_{4-}-\gamma\_{3-})\left(-\frac{\kappa\_{1}}{M\_{1}}-\gamma\_{3+}\right)}{(\gamma\_{3+}-\gamma\_{4-})\left(\gamma\_{3-}+\frac{\kappa\_{1}}{M\_{1}}\right)}\right), |  |

   where K3+K\_{3+} is defined in ([4.12](https://arxiv.org/html/2511.11383v1#S4.E12 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and K3−K\_{3-} is the unique solution to ψ​(z)=0\psi(z)=0 on (1−aγ3−,αL​B)\left(\frac{1-a}{\gamma\_{3-}},\alpha\_{LB}\right). Moreover, the relation u1<w0≤u2u\_{1}<w\_{0}\leq u\_{2} holds.
2. 2.

   The function gg, defined by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g​(x)={(1−a)​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zif x<u1,(1−a)​[∫u1xexp⁡[∫zu1κ1H​(y)​𝑑y]​𝑑z+∫0u1exp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑z]if u1≤x<w0,K3+​eγ3+​(x−u1)+K3−​eγ3−​(x−u1)+(1−a)​c¯2δif w0≤x<u2,aγ4−​eγ4−​(x−u2)+a​c¯1+(1−a)​c¯2δif x≥u2,g(x)=\begin{cases}(1-a)\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<u\_{1}$,}\\ (1-a)\left[\int\_{u\_{1}}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{H(y)}dy\right]dz+\int\_{0}^{u\_{1}}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz\right]&\mbox{if $u\_{1}\leq x<w\_{0}$,}\\ K\_{3+}e^{\gamma\_{3+}(x-u\_{1})}+K\_{3-}e^{\gamma\_{3-}(x-u\_{1})}+\frac{(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $w\_{0}\leq x<u\_{2}$,}\\ \frac{a}{\gamma\_{4-}}e^{\gamma\_{4-}(x-u\_{2})}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $x\geq u\_{2}$,}\end{cases} |  | (4.19) |

   where G−1G^{-1} is the inverse of GG defined in ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), is a classical solution to the HJB equation in ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and thus equals the value function VV of the optimization problem in ([2.5](https://arxiv.org/html/2511.11383v1#S2.E5 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). In addition, gg is strictly concave.
3. 3.

   The optimal reinsurance and dividend strategies (π1∗,π2∗,c1∗,c2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*},c\_{1}^{\*},c\_{2}^{\*}) are given by

   |  |  |  |
   | --- | --- | --- |
   |  | (π1∗,π2∗,c1∗,c2∗)​(x)={(G−1​(x),κ2κ1​G−1​(x),0,0)if x<u1,(H​(x),κ2κ1​H​(x),0,c¯2)if u1≤x<w0,(M1,κ2κ1​M1,0,c¯2)if w0≤x<u2,(M1,κ2κ1​M1,c¯1,c¯2)if x≥u2.(\pi\_{1}^{\*},\pi\_{2}^{\*},c\_{1}^{\*},c\_{2}^{\*})(x)=\begin{cases}\left(G^{-1}(x),\frac{\kappa\_{2}}{\kappa\_{1}}G^{-1}(x),0,0\right)&\mbox{if $x<u\_{1}$,}\\ \left(H(x),\frac{\kappa\_{2}}{\kappa\_{1}}H(x),0,\overline{c}\_{2}\right)&\mbox{if $u\_{1}\leq x<w\_{0}$,}\\ \left(M\_{1},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{1},0,\overline{c}\_{2}\right)&\mbox{if $w\_{0}\leq x<u\_{2}$,}\\ \left(M\_{1},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{1},\overline{c}\_{1},\overline{c}\_{2}\right)&\mbox{if $x\geq u\_{2}$.}\end{cases} |  |

By comparing Theorems [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), we can observe notable similarities in the optimal reinsurance and dividend strategies in both cases. The main distinction is the form of the retention level when the aggregate reserve level is between w0w\_{0} and u1u\_{1}. Moreover, Theorem [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") provides an explicit expression for w0w\_{0}, whereas in Theorem [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), w0w\_{0} is presented implicitly.

In this scenario, a necessary condition is 0<c¯2<N1−κ1​N22​M1+δ​M1κ10<\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}, which means that the maximum dividend rate of Line 1, c¯1\overline{c}\_{1}, must adequately compensate for the balance arising from the maximum dividend rate of Line 2 to achieve a minimum total of N1−κ1​N22​M1+δ​M1κ1N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. This suggests that Line 1 may have a larger maximum dividend rate than Line 2, which could be strategically advantageous in improving overall financial performance by setting a higher maximum dividend rate.

It is important to note that asmussen2000 show that having a reinsurance threshold level that exceeds the dividend threshold level is not possible in the univariate case. However, in our case, this scenario is possible.

The next theorem discusses the case in which either condition (i) or condition (ii) of Theorems [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") does not hold.

###### Theorem 4.4.

Suppose that either (i) M1=∞M\_{1}=\infty or (ii) c¯1+c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{1}+\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} holds. We have the following results:

1. 1.

   w0w\_{0} defined in ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is infinite (w0=∞w\_{0}=\infty), u1u\_{1} defined in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is the unique solution to

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫u2xκ1H​(y)​𝑑y=ln⁡(a1−a)\int\_{u\_{2}}^{x}\frac{\kappa\_{1}}{H(y)}dy=\ln\left(\frac{a}{1-a}\right) |  | (4.20) |

   in (0,u2)(0,u\_{2}), and u2u\_{2} defined in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | H​(u2)=M0,H(u\_{2})=M\_{0}, |  | (4.21) |

   where HH satisfies ([4.17](https://arxiv.org/html/2511.11383v1#S4.E17 "In item 1 ‣ Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and M0M\_{0} is a solution to

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | −κ1y=γ¯4−​(y)-\frac{\kappa\_{1}}{y}=\overline{\gamma}\_{4-}(y) |  | (4.22) |

   in (0,M1)(0,M\_{1}). Moreover, the relation u1≤u2<w0u\_{1}\leq u\_{2}<w\_{0} holds.
2. 2.

   The function gg, defined by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g​(x)={(1−a)​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zif x<u1,(1−a)​[∫u1xexp⁡[∫zu1κ1H​(y)​𝑑y]​𝑑z+∫0u1exp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑z]if u1≤x<u2,aγ¯4−​(M0)​eγ¯4−​(M0)​(x−u2)+a​c¯1+(1−a)​c¯2δif x≥u2,g(x)=\begin{cases}(1-a)\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<u\_{1}$,}\\ (1-a)\left[\int\_{u\_{1}}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{H(y)}dy\right]dz+\int\_{0}^{u\_{1}}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz\right]&\mbox{if $u\_{1}\leq x<u\_{2}$,}\\ \frac{a}{\overline{\gamma}\_{4-}(M\_{0})}e^{\overline{\gamma}\_{4-}(M\_{0})(x-u\_{2})}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $x\geq u\_{2}$,}\end{cases} |  | (4.23) |

   where G−1G^{-1} is the inverse of GG defined in ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), is a classical solution to the HJB equation in ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and thus equals the value function VV of the optimization problem in ([2.5](https://arxiv.org/html/2511.11383v1#S2.E5 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). In addition, gg is strictly concave.
3. 3.

   The optimal reinsurance and dividend strategies (π1∗,π2∗,c1∗,c2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*},c\_{1}^{\*},c\_{2}^{\*}) are given by

   |  |  |  |
   | --- | --- | --- |
   |  | (π1∗,π2∗,c1∗,c2∗)​(x)={(G−1​(x),κ2κ1​G−1​(x),0,0)if x<u1,(H​(x),κ2κ1​H​(x),0,c¯2)if u1≤x<u2,(M0,κ2κ1​M0,c¯1,c¯2)if x≥u2.(\pi\_{1}^{\*},\pi\_{2}^{\*},c\_{1}^{\*},c\_{2}^{\*})(x)=\begin{cases}\left(G^{-1}(x),\frac{\kappa\_{2}}{\kappa\_{1}}G^{-1}(x),0,0\right)&\mbox{if $x<u\_{1}$,}\\ \left(H(x),\frac{\kappa\_{2}}{\kappa\_{1}}H(x),0,\overline{c}\_{2}\right)&\mbox{if $u\_{1}\leq x<u\_{2}$,}\\ \left(M\_{0},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{0},\overline{c}\_{1},\overline{c}\_{2}\right)&\mbox{if $x\geq u\_{2}$.}\end{cases} |  |

Under condition (i), the support of the distribution function F1F\_{1} is unbounded, which implies that w0w\_{0} defined in ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) does not exist. Under condition (ii), the two lines can pay at most N1−κ1​N22​M1+δ​M1κ1N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} in total. This frees up some of the reserves, allowing the insurer to purchase more reinsurance.
Similar to the results in asmussen2000, a reinsurance threshold that exceeds all dividend thresholds is not possible.

We now discuss the optimal capital injection strategy. We partition the domain of the reserve level pair (x1,x2)∈ℝ+2(x\_{1},x\_{2})\in\mathbb{R}\_{+}^{2} into seven regions (see Figure [1](https://arxiv.org/html/2511.11383v1#S4.F1 "Figure 1 ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Define the constants δi\delta\_{i}, i=0,1,2i=0,1,2, corresponding to each of the three cases in Theorems [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), and [4.4](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (δ0,δ1,δ2)={(w0,u1,u2)if w0≤u1≤u2,(u1,w0,u2)if u1<w0≤u2,(u1,u1,u2)if u1≤u2<w0.(\delta\_{0},\delta\_{1},\delta\_{2})=\begin{cases}(w\_{0},u\_{1},u\_{2})&\mbox{if $w\_{0}\leq u\_{1}\leq u\_{2}$,}\\ (u\_{1},w\_{0},u\_{2})&\mbox{if $u\_{1}<w\_{0}\leq u\_{2}$,}\\ (u\_{1},u\_{1},u\_{2})&\mbox{if $u\_{1}\leq u\_{2}<w\_{0}$}.\end{cases} |  | (4.24) |

The seven regions AiA\_{i}, i=1,2,⋯,7i=1,2,\cdots,7, are defined as follows (see Figure [1](https://arxiv.org/html/2511.11383v1#S4.F1 "Figure 1 ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")):

* •

  A1={(x1,x2):x1≥0,x2>δ2},A\_{1}=\{(x\_{1},x\_{2}):x\_{1}\geq 0,x\_{2}>\delta\_{2}\},
* •

  A2={(x1,x2):x1>0,x2∈[0,δ2],x1+x2>δ2},A\_{2}=\{(x\_{1},x\_{2}):x\_{1}>0,x\_{2}\in[0,\delta\_{2}],x\_{1}+x\_{2}>\delta\_{2}\},
* •

  A3={(x1,x2):x1≥0,x2∈(δ1,δ2],x1+x2≤δ2},A\_{3}=\{(x\_{1},x\_{2}):x\_{1}\geq 0,x\_{2}\in(\delta\_{1},\delta\_{2}],x\_{1}+x\_{2}\leq\delta\_{2}\},
* •

  A4={(x1,x2):x1>0,x2∈[0,δ1],x1+x2∈(δ1,δ2]},A\_{4}=\{(x\_{1},x\_{2}):x\_{1}>0,x\_{2}\in[0,\delta\_{1}],x\_{1}+x\_{2}\in(\delta\_{1},\delta\_{2}]\},
* •

  A5={(x1,x2):x1≥0,x2∈(δ0,δ1],x1+x2≤δ1},A\_{5}=\{(x\_{1},x\_{2}):x\_{1}\geq 0,x\_{2}\in(\delta\_{0},\delta\_{1}],x\_{1}+x\_{2}\leq\delta\_{1}\},
* •

  A6={(x1,x2):x1>0,x2∈[0,δ0],x1+x2∈(δ0,δ1]},A\_{6}=\{(x\_{1},x\_{2}):x\_{1}>0,x\_{2}\in[0,\delta\_{0}],x\_{1}+x\_{2}\in(\delta\_{0},\delta\_{1}]\},
* •

  A7={(x1,x2):x1≥0,x2≥0,x1+x2≤δ0}.A\_{7}=\{(x\_{1},x\_{2}):x\_{1}\geq 0,x\_{2}\geq 0,x\_{1}+x\_{2}\leq\delta\_{0}\}.

x1x\_{1}x2x\_{2}(0,δ2)(0,\delta\_{2})(δ2,0)(\delta\_{2},0)(0,δ1)(0,\delta\_{1})(δ1,0)(\delta\_{1},0)(0,δ0)(0,\delta\_{0})(δ0,0)(\delta\_{0},0)x2=δ2x\_{2}=\delta\_{2}A7A\_{7}A6A\_{6}A4A\_{4}A5A\_{5}A2A\_{2}A3A\_{3}A1A\_{1}x1+x2=δ0x\_{1}+x\_{2}=\delta\_{0}x1+x2=δ1x\_{1}+x\_{2}=\delta\_{1}x1+x2=δ2x\_{1}+x\_{2}=\delta\_{2}x2=δ1x\_{2}=\delta\_{1}x2=δ0x\_{2}=\delta\_{0}


Figure 1: Regions for Capital Injection Decisions

###### Theorem 4.5.

The optimal capital injection strategy is given by one of the following cases:

1. 1.

   If x∈A1x\in A\_{1} and Line 1 reaches zero, Line 2 transfers an amount of x2−δ2x\_{2}-\delta\_{2} to Line 1, and we proceed to region A2A\_{2}. If Line 1 does not reach zero, we remain in A1A\_{1} until we move to region A2A\_{2} or A3A\_{3}.
2. 2.

   If x∈A2x\in A\_{2} and Line 2 reaches zero, Line 1 transfers an amount of x1−δ2x\_{1}-\delta\_{2} to Line 2. We remain in A2A\_{2} until we move to region A1A\_{1}, A3A\_{3}, or A4A\_{4}, regardless of whether Line 2 reaches zero.
3. 3.

   If x∈A3x\in A\_{3} and Line 1 reaches zero, Line 2 transfers an amount of x2−δ1x\_{2}-\delta\_{1} to Line 1, and we proceed to region A4A\_{4}. If Line 1 does not reach zero, we remain in A3A\_{3} until we move to region A2A\_{2}, A4A\_{4}, or A5A\_{5}.
4. 4.

   If x∈A4x\in A\_{4} and Line 2 reaches zero, Line 1 transfers an amount of x1−δ1x\_{1}-\delta\_{1} to Line 2. We remain in A4A\_{4} until we move to region A2A\_{2}, A3A\_{3}, A5A\_{5}, or A6A\_{6}, regardless of whether Line 2 reaches zero.
5. 5.

   If x∈A5x\in A\_{5} and Line 1 reaches zero, Line 2 transfers an amount of x2−δ0x\_{2}-\delta\_{0} to Line 1, and we proceed to region A6A\_{6}. If Line 1 does not reach zero, we stay in A5A\_{5} until we move to region A4A\_{4}, A6A\_{6}, or A7A\_{7}.
6. 6.

   If x∈A6x\in A\_{6} and Line 2 reaches zero, Line 1 transfers an amount of x1−δ0x\_{1}-\delta\_{0} to Line 2. We remain in A6A\_{6} until we move to region A4A\_{4}, A5A\_{5}, or A7A\_{7}, regardless of whether Line 2 reaches zero.
7. 7.

   If x∈A7x\in A\_{7}, we remain in A7A\_{7} until we move to region A6A\_{6}. The problem ends when the reserves exit the nonnegative quadrant.

## 5 Unbounded Dividend Rates

In this section, we consider the case in which there are no restrictions on the dividend rates of both lines. The corresponding HJB equation is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup{supπi∈[0,Mi]ℒπ​(V),∂V∂x1−∂V∂x2,∂V∂x2−∂V∂x1,a−∂V∂x1,1−a−∂V∂x2}=0,\sup\left\{\sup\_{\pi\_{i}\in[0,M\_{i}]}\mathcal{L}^{\pi}(V),\quad\frac{\partial V}{\partial x\_{1}}-\frac{\partial V}{\partial x\_{2}},\quad\frac{\partial V}{\partial x\_{2}}-\frac{\partial V}{\partial x\_{1}},a-\frac{\partial V}{\partial x\_{1}},1-a-\frac{\partial V}{\partial x\_{2}}\right\}=0, |  | (5.1) |

with boundary condition V​(0,0)=0V(0,0)=0 and

|  |  |  |
| --- | --- | --- |
|  | ℒπ​(ϕ):=∑i=12[κi​μi​(πi)​∂ϕ∂xi+12​σi2​(πi)​∂2ϕ∂xi2],ϕ∈C2,2.\mathcal{L}^{\pi}(\phi):=\sum\_{i=1}^{2}\left[\kappa\_{i}\mu\_{i}(\pi\_{i})\frac{\partial\phi}{\partial x\_{i}}+\frac{1}{2}\sigma\_{i}^{2}(\pi\_{i})\frac{\partial^{2}\phi}{\partial x\_{i}^{2}}\right],\quad\phi\in C^{2,2}. |  |

The first, fourth, and fifth terms within the outer supremum function can be handled using arguments similar to those in schmidli2007book. The second and third terms arise from the capital injection strategies modeled as singular controls.

As in the previous section, a standard verification lemma for unbounded dividend rates implies that a classical solution, if it exists, is the value function that solves the associated optimization problem.

We now present the main results for the unbounded dividend rates. Two cases arise depending on whether M1M\_{1} is finite (Theorem [5.1](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) or infinite (Theorem [5.2](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). As in the previous section, each case has its corresponding analytical form of the value function and a reinsurance strategy (π1∗,π2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*}). Since the dividend payout strategies C1C\_{1} and C2C\_{2} are also modeled as singular controls, similar to the capital injection strategies, we obtain a uniform optimal strategy (C1∗,C2∗,L1∗,L2∗)(C\_{1}^{\*},C\_{2}^{\*},L\_{1}^{\*},L\_{2}^{\*}) in Theorem [5.3](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem3 "Theorem 5.3. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance").

###### Theorem 5.1.

Suppose M1<∞M\_{1}<\infty. We have the following results:

1. 1.

   w0w\_{0} defined in ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) exists and is given by

   |  |  |  |
   | --- | --- | --- |
   |  | w0=G​(M1),w\_{0}=G(M\_{1}), |  |

   where GG is defined in ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), and u1u\_{1} defined in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is explicitly given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | u1=w0+1γ2+−γ2−​ln⁡(γ2−​(κ1+γ2+​M1)γ2+​(κ1+γ2−​M1)),u\_{1}=w\_{0}+\frac{1}{\gamma\_{2+}-\gamma\_{2-}}\ln\left(\frac{\gamma\_{2-}(\kappa\_{1}+\gamma\_{2+}M\_{1})}{\gamma\_{2+}(\kappa\_{1}+\gamma\_{2-}M\_{1})}\right), |  | (5.2) |

   where γ2±\gamma\_{2\pm} equals γ2±​(M1)\gamma\_{2\pm}(M\_{1}) given in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The relation w0≤u1w\_{0}\leq u\_{1} holds.
2. 2.

   The function gg, defined by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g​(x)={K1​∫0xexp⁡[∫zw0κ1G−1​(y)​𝑑y]​𝑑zif x<w0,1−aγ2+​γ2−​(γ2+−γ2−)​[γ2+2​eγ2−​(x−u1)−γ2−2​eγ2+​(x−u1)]if w0≤x<u1,(1−a)​[x−u1+N1δ]if x≥u1,g(x)=\begin{cases}K\_{1}\int\_{0}^{x}\exp\left[\int^{w\_{0}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<w\_{0}$,}\\ \frac{1-a}{\gamma\_{2+}\gamma\_{2-}(\gamma\_{2+}-\gamma\_{2-})}\left[\gamma\_{2+}^{2}e^{\gamma\_{2-}(x-u\_{1})}-\gamma\_{2-}^{2}e^{\gamma\_{2+}(x-u\_{1})}\right]&\mbox{if $w\_{0}\leq x<u\_{1}$,}\\ (1-a)\left[x-u\_{1}+\frac{N\_{1}}{\delta}\right]&\mbox{if $x\geq u\_{1}$,}\end{cases} |  | (5.3) |

   where G−1G^{-1} is the inverse of GG defined in ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), N1N\_{1} equals N¯1​(M1)\overline{N}\_{1}(M\_{1}) defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")),
   and

   |  |  |  |
   | --- | --- | --- |
   |  | K1=1−aγ2+−γ2−​[γ2+​eγ2−​(w0−u1)−γ2−​eγ2+​(w0−u1)],K\_{1}=\frac{1-a}{\gamma\_{2+}-\gamma\_{2-}}\left[\gamma\_{2+}e^{\gamma\_{2-}(w\_{0}-u\_{1})}-\gamma\_{2-}e^{\gamma\_{2+}(w\_{0}-u\_{1})}\right], |  |

   is a classical solution to the HJB equation in ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and thus equals the value function VV of the optimization problem in ([2.5](https://arxiv.org/html/2511.11383v1#S2.E5 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Moreover, gg is concave.
3. 3.

   The optimal reinsurance strategy (π1∗,π2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*}) is given by

   |  |  |  |
   | --- | --- | --- |
   |  | (π1∗,π2∗)​(x)={(G−1​(x),κ2κ1​G−1​(x))if x<w0,(M1,κ2κ1​M1)if x≥w0.(\pi\_{1}^{\*},\pi\_{2}^{\*})(x)=\begin{cases}\left(G^{-1}(x),\frac{\kappa\_{2}}{\kappa\_{1}}G^{-1}(x)\right)&\mbox{if $x<w\_{0}$,}\\ \left(M\_{1},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{1}\right)&\mbox{if $x\geq w\_{0}$.}\end{cases} |  |

Similar to the bounded case where w0≤u1w\_{0}\leq u\_{1}, Theorem [5.1](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") shows that the optimal reinsurance strategy remains constant for both lines when the aggregate reserve levels reach the threshold w0w\_{0}.

###### Theorem 5.2.

Suppose M1=∞M\_{1}=\infty. We have the following results:

1. 1.

   w0w\_{0} defined in ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is infinite (w0=∞w\_{0}=\infty) and u1u\_{1} defined in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is explicitly given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | u1=G​(∞):=limy→∞G​(y),u\_{1}=G(\infty):=\lim\_{y\to\infty}G(y), |  | (5.4) |

   where GG is defined by ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The relation u1<w0u\_{1}<w\_{0} holds.
2. 2.

   The function gg, defined by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g​(x)={(1−a)​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zif x<u1,(1−a)​[x−u1+N1δ]if x≥u1,g(x)=\begin{cases}(1-a)\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<u\_{1}$,}\\ (1-a)\left[x-u\_{1}+\frac{N\_{1}}{\delta}\right]&\mbox{if $x\geq u\_{1}$,}\end{cases} |  | (5.5) |

   where G−1G^{-1} is the inverse of GG defined in ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and N1N\_{1} equals N¯1​(M1)\overline{N}\_{1}(M\_{1}) defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), is a classical solution to the HJB equation in ([4.2](https://arxiv.org/html/2511.11383v1#S4.E2 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and thus equals the value function VV of the optimization problem in ([2.5](https://arxiv.org/html/2511.11383v1#S2.E5 "In 2 Model ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Moreover, gg is concave.
3. 3.

   The optimal reinsurance strategy (π1∗,π2∗)(\pi\_{1}^{\*},\pi\_{2}^{\*}) is given by

   |  |  |  |
   | --- | --- | --- |
   |  | (π1∗,π2∗)​(x)=(G−1​(x),κ2κ1​G−1​(x)),x<u1.(\pi\_{1}^{\*},\pi\_{2}^{\*})(x)=\left(G^{-1}(x),\frac{\kappa\_{2}}{\kappa\_{1}}G^{-1}(x)\right),\quad x<u\_{1}. |  |

Theorem [5.2](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), in conjunction with Theorem [5.3](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem3 "Theorem 5.3. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") below, implies that the aggregate reserve level must remain below x=u1x=u\_{1} since the aggregate reserves above u1u\_{1} are transferred between lines and are immediately paid as dividends.

For the optimal dividend payout and capital injection strategy, we partition the domain of the reserve level pair (x1,x2)∈ℝ+2(x\_{1},x\_{2})\in\mathbb{R}\_{+}^{2} into 3 regions (see Figure [2](https://arxiv.org/html/2511.11383v1#S5.F2 "Figure 2 ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The three regions AiA\_{i}, i=1,2,3i=1,2,3, are defined as follows:

* •

  A1={(x1,x2):x2≥0,x1>u1},A\_{1}=\{(x\_{1},x\_{2}):x\_{2}\geq 0,x\_{1}>u\_{1}\},
* •

  A2={(x1,x2):x1∈[0,u1],x2>0,x1+x2>u1},A\_{2}=\{(x\_{1},x\_{2}):x\_{1}\in[0,u\_{1}],x\_{2}>0,x\_{1}+x\_{2}>u\_{1}\},
* •

  A3={(x1,x2):x1≥0,x2≥0,x1+x2≤u1}.A\_{3}=\{(x\_{1},x\_{2}):x\_{1}\geq 0,x\_{2}\geq 0,x\_{1}+x\_{2}\leq u\_{1}\}.

x1x\_{1}x2x\_{2}(0,u1)(0,u\_{1})(u1,0)(u\_{1},0)A1A\_{1}A2A\_{2}A3A\_{3}x1+x2=u1x\_{1}+x\_{2}=u\_{1}x1=u1x\_{1}=u\_{1}


Figure 2: Regions for Dividend Payout and Capital Injection Decisions

###### Theorem 5.3.

The optimal dividend payout and capital injection strategy is given by one of the following cases:

1. 1.

   If x∈A1x\in A\_{1}, Line 1 transfers an amount x1−u1x\_{1}-u\_{1} to Line 2, and we proceed to region A2A\_{2}.
2. 2.

   If x∈A2x\in A\_{2}, Line 2 pays x1+x2−u1x\_{1}+x\_{2}-u\_{1} directly as dividends, and we proceed to region A1A\_{1}.
3. 3.

   If x∈A3x\in A\_{3}, no dividends are paid and we remain in A3A\_{3} until we move to region A2A\_{2}. The problem ends when the reserves exit the nonnegative quadrant.

## 6 Numerical Examples

In this section, we present several numerical examples to gain further insight into the main results in Sections [4](https://arxiv.org/html/2511.11383v1#S4 "4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [5](https://arxiv.org/html/2511.11383v1#S5 "5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). Since the capital injection strategies were presented in Theorems [4.5](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem5 "Theorem 4.5. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [5.3](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem3 "Theorem 5.3. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and the dividend payout strategy is a threshold strategy in the bounded-dividend case and a singular control in the unbounded-dividend case, we focus on illustrating the optimal (excess-of-loss) reinsurance strategies for each of the main results, along with their corresponding value functions.

We fix the following parameters: κ1=4\kappa\_{1}=4, κ2=2\kappa\_{2}=2, δ=0.5\delta=0.5, and a=0.3a=0.3. For the claim size distributions F1F\_{1} and F2F\_{2} in the bounded support case, we use uniform distributions on [0,1][0,1] and [0,1.5][0,1.5], respectively, which correspond to M1=1M\_{1}=1 and M2=1.5M\_{2}=1.5. In the unbounded support case (M1=M2=∞)(M\_{1}=M\_{2}=\infty), we use exponential distributions with parameters 11 and 1.51.5. Figures [3](https://arxiv.org/html/2511.11383v1#S6.F3 "Figure 3 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") to [7](https://arxiv.org/html/2511.11383v1#S6.F7 "Figure 7 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") display the value functions on the left and the reinsurance strategies on the right. The vertical dotted lines represent the threshold levels.

With these parameters, the optimal reinsurance (retention) level for Line 2 is exactly half that of Line 1: κ2κ1=12\frac{\kappa\_{2}}{\kappa\_{1}}=\frac{1}{2}. For uniformly distributed claim sizes, those in Lines 1 and 2 are capped at M1=1M\_{1}=1 and M2=1.5M\_{2}=1.5, respectively. This means that if the optimal excess-of-loss retention level for Line 1 is equal to 1, then the insurer retains all risk. For an exponential distribution, claim sizes have no upper bound and can take any value in [0,∞)[0,\infty).

Figures [3](https://arxiv.org/html/2511.11383v1#S6.F3 "Figure 3 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") to [5](https://arxiv.org/html/2511.11383v1#S6.F5 "Figure 5 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") correspond to the main results for the bounded dividend rates in Section [4](https://arxiv.org/html/2511.11383v1#S4 "4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). The maximum dividend rates of the business lines vary, and their sum decreases noticeably across the three figures. Figures [6](https://arxiv.org/html/2511.11383v1#S6.F6 "Figure 6 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [7](https://arxiv.org/html/2511.11383v1#S6.F7 "Figure 7 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") correspond to the main results for the unbounded dividend rates in Section [5](https://arxiv.org/html/2511.11383v1#S5 "5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). The optimal excess-of-loss retention level increases as the aggregate reserve level increases across all examples. Equivalently, the amount of risk ceded to the reinsurer decreases as the aggregate reserve level increases.

By definition, the reinsurance threshold level w0w\_{0} indicates that the insurer should retain all risks of Line 1 once the aggregate reserve level exceeds it. This is evident in Figures [3](https://arxiv.org/html/2511.11383v1#S6.F3 "Figure 3 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [4](https://arxiv.org/html/2511.11383v1#S6.F4 "Figure 4 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), and [6](https://arxiv.org/html/2511.11383v1#S6.F6 "Figure 6 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), where the retention levels for both lines remain constant (i.e., flat) when the aggregate reserve level is greater than w0w\_{0}. In the scenario where w0w\_{0} does not exist, as stated in Theorem [4.4](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), the insurer must always transfer a portion of the risk to the reinsurer, regardless of the aggregate reserve level. Figure [5](https://arxiv.org/html/2511.11383v1#S6.F5 "Figure 5 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") illustrates this scenario, where the retained risk for Line 1 is capped at M0=0.71M\_{0}=0.71.

In Figure [7](https://arxiv.org/html/2511.11383v1#S6.F7 "Figure 7 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), it is worth noting that the level of retained risk increases without bound, with x=u1=1.25x=u\_{1}=1.25 acting as a vertical asymptote for the reinsurance level. As stated in Theorem [5.3](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem3 "Theorem 5.3. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"),
the aggregate reserve level must remain below u1u\_{1} since any reserve above u1u\_{1} is allocated to dividends and capital transfers between lines.

The value functions are all increasing and concave. For the bounded dividend rates (Figures [3](https://arxiv.org/html/2511.11383v1#S6.F3 "Figure 3 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") to [5](https://arxiv.org/html/2511.11383v1#S6.F5 "Figure 5 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), they approach the limit a​c¯1+(1−a)​c¯2δ\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}. In particular, the value function in Figure [5](https://arxiv.org/html/2511.11383v1#S6.F5 "Figure 5 ‣ 6 Numerical Examples ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") approaches this limit more quickly than in the other cases, attributed to the smaller values of u1u\_{1} and u2u\_{2}.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 3: Uniformly distributed claims: κ1=4\kappa\_{1}=4, κ2=2\kappa\_{2}=2, δ=0.5\delta=0.5, a=0.3a=0.3, c¯1=3\overline{c}\_{1}=3, c¯2=2\overline{c}\_{2}=2
  
(M1=1M\_{1}=1, M2=1.5M\_{2}=1.5, w0=0.19<u1=0.24<u2=0.87w\_{0}=0.19<u\_{1}=0.24<u\_{2}=0.87, corresponding to Theorem [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"))



![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 4: Uniformly distributed claims: κ1=4\kappa\_{1}=4, κ2=2\kappa\_{2}=2, δ=0.5\delta=0.5, a=0.3a=0.3, c¯1=3\overline{c}\_{1}=3, c¯2=1\overline{c}\_{2}=1
  
(M1=1M\_{1}=1, M2=1.5M\_{2}=1.5, u1=0.17<w0=0.22<u2=0.57u\_{1}=0.17<w\_{0}=0.22<u\_{2}=0.57, corresponding to Theorem [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"))



![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 5: Uniformly distributed claims: κ1=4\kappa\_{1}=4, κ2=2\kappa\_{2}=2, δ=0.5\delta=0.5, a=0.3a=0.3, c¯1=1\overline{c}\_{1}=1, c¯2=0.5\overline{c}\_{2}=0.5
  
(M0=0.71M\_{0}=0.71, M1=1M\_{1}=1, M2=1.5M\_{2}=1.5, u1=0.09<u2=0.19u\_{1}=0.09<u\_{2}=0.19, corresponding to Theorem [4.4](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"))



![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 6: Uniformly distributed claims: κ1=4\kappa\_{1}=4, κ2=2\kappa\_{2}=2, δ=0.5\delta=0.5, a=0.3a=0.3
  
(M1=1M\_{1}=1, M2=1.5M\_{2}=1.5, w0=0.19<u1=0.52w\_{0}=0.19<u\_{1}=0.52, corresponding to Theorem [5.1](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"))



![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 7: Exponentially distributed claims: κ1=4\kappa\_{1}=4, κ2=2\kappa\_{2}=2, δ=0.5\delta=0.5, a=0.3a=0.3
  
(M1=∞M\_{1}=\infty, M2=∞M\_{2}=\infty, u1=1.25u\_{1}=1.25, corresponding to Theorem [5.2](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"))

## 7 Proof of Main Results

In this section, we provide the proofs of Theorems [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [4.4](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [5.1](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), and [5.2](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance").

### 7.1 Proof of Theorem [4.2](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")

#### Deriving the analytical solution

Suppose for now that w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2} and that w0w\_{0} exists. In the region {x<w0}\{x<w\_{0}\}, we have π1∗​(x)=π^1​(x)\pi^{\*}\_{1}(x)=\widehat{\pi}\_{1}(x), where π^1\widehat{\pi}\_{1} is given in ([4.4](https://arxiv.org/html/2511.11383v1#S4.E4 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), and the corresponding HJB equation becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =[κ1​μ1​(π1∗​(x))+κ2​μ2​(κ2κ1​π1∗​(x))−κ12​π1∗​(x)​(σ12​(π1∗​(x))+σ22​(κ2κ1​π1∗​(x)))]​g′​(x)−δ​g​(x).\displaystyle=\left[\kappa\_{1}\mu\_{1}(\pi^{\*}\_{1}(x))+\kappa\_{2}\mu\_{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)-\frac{\kappa\_{1}}{2\pi^{\*}\_{1}(x)}\left(\sigma\_{1}^{2}(\pi^{\*}\_{1}(x))+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)\right)\right]g^{\prime}(x)-\delta g(x). |  | (7.1) |

Differentiating with respect to xx leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =[κ1​d​π1∗​(x)d​x2​(π1∗​(x))2​(σ12​(π1∗​(x))+σ22​(κ2κ1​π1∗​(x)))−δ]​g′​(x)\displaystyle=\left[\frac{\kappa\_{1}\frac{\mathrm{d}\pi^{\*}\_{1}(x)}{\mathrm{d}x}}{2(\pi\_{1}^{\*}(x))^{2}}\left(\sigma\_{1}^{2}(\pi^{\*}\_{1}(x))+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)\right)-\delta\right]g^{\prime}(x) |  | (7.2) |
|  |  | +[κ1​μ1​(π1∗​(x))+κ2​μ2​(κ2κ1​π1∗​(x))−κ12​π1∗​(x)​(σ12​(π1∗​(x))+σ22​(κ2κ1​π1∗​(x)))]​g′′​(x).\displaystyle\quad+\left[\kappa\_{1}\mu\_{1}(\pi^{\*}\_{1}(x))+\kappa\_{2}\mu\_{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)-\frac{\kappa\_{1}}{2\pi^{\*}\_{1}(x)}\left(\sigma\_{1}^{2}(\pi^{\*}\_{1}(x))+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)\right)\right]g^{\prime\prime}(x). |  |

Using ([4.4](https://arxiv.org/html/2511.11383v1#S4.E4 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) once more yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=[κ12+κ1​d​π1∗​(x)d​x2​(π1∗​(x))2​(σ12​(π1∗​(x))+σ22​(κ2κ1​π1∗​(x)))−κ12π1∗​(x)​μ1​(π1∗​(x))−κ1​κ2π1∗​(x)​μ2​(κ2κ1​π1∗​(x))−δ]​g′​(x).0=\left[\frac{\kappa\_{1}^{2}+\kappa\_{1}\frac{\mathrm{d}\pi^{\*}\_{1}(x)}{\mathrm{d}x}}{2(\pi^{\*}\_{1}(x))^{2}}\left(\sigma\_{1}^{2}(\pi^{\*}\_{1}(x))+\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)\right)-\frac{\kappa\_{1}^{2}}{\pi^{\*}\_{1}(x)}\mu\_{1}(\pi^{\*}\_{1}(x))-\frac{\kappa\_{1}\kappa\_{2}}{\pi^{\*}\_{1}(x)}\mu\_{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)-\delta\right]g^{\prime}(x). |  | (7.3) |

Since gg is assumed to be strictly increasing and concave, we obtain the following differential equation for π1∗\pi^{\*}\_{1}:

|  |  |  |
| --- | --- | --- |
|  | d​π1∗​(x)d​x=d​G​(y)d​y|y=π1∗​(x),\frac{\mathrm{d}\pi^{\*}\_{1}(x)}{\mathrm{d}x}=\frac{\mathrm{d}G(y)}{\mathrm{d}y}\Bigg|\_{y=\pi^{\*}\_{1}(x)}, |  |

where GG is defined by ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). It can be shown that GG is continuous and strictly increasing; hence, its inverse, denoted by G−1G^{-1}, exists. Since π1∗​(0)=0\pi^{\*}\_{1}(0)=0, we then obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | π1∗​(x)=G−1​(x).\pi^{\*}\_{1}(x)=G^{-1}(x). |  | (7.4) |

Moreover, since d​π1∗​(x)d​x>0\frac{\mathrm{d}\pi^{\*}\_{1}(x)}{\mathrm{d}x}>0 and π1∗​(0)=0\pi^{\*}\_{1}(0)=0, there exists an xM1>0x\_{M\_{1}}>0 such that π1∗​(xM1)=M1\pi^{\*}\_{1}(x\_{M\_{1}})=M\_{1}. Choosing w0=xM1w\_{0}=x\_{M\_{1}} proves the existence of w0w\_{0} defined in ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and that w0=G​(M1)w\_{0}=G(M\_{1}). From ([4.4](https://arxiv.org/html/2511.11383v1#S4.E4 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we can see that −κ1π1∗​(x)=g′′​(x)g′​(x)=dd​x​ln⁡g′​(x)-\frac{\kappa\_{1}}{\pi^{\*}\_{1}(x)}=\frac{g^{\prime\prime}(x)}{g^{\prime}(x)}=\frac{\mathrm{d}}{\mathrm{d}x}\ln g^{\prime}(x). Hence, a solution to the HJB equation ([7.1](https://arxiv.org/html/2511.11383v1#S7.E1 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) that satisfies g​(0)=0g(0)=0 is given by

|  |  |  |
| --- | --- | --- |
|  | g​(x)=K1​∫0xexp⁡[∫zw0κ1G−1​(y)​𝑑y]​𝑑z,g(x)=K\_{1}\int\_{0}^{x}\exp\left[\int\_{z}^{w\_{0}}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz, |  |

where K1>0K\_{1}>0 is an unknown constant.

By the definition of w0w\_{0} and the constraint π1∈[0,M1]\pi\_{1}\in[0,M\_{1}], it follows that π1∗​(x)=M1\pi\_{1}^{\*}(x)=M\_{1} for x≥w0x\geq w\_{0}. It is easy to see that (π1∗,π2∗)​(x)=(M1,κ2κ1​M1)(\pi\_{1}^{\*},\pi\_{2}^{\*})(x)=\left(M\_{1},\frac{\kappa\_{2}}{\kappa\_{1}}M\_{1}\right) since M2M1≥κ2κ1\frac{M\_{2}}{M\_{1}}\geq\frac{\kappa\_{2}}{\kappa\_{1}} holds. Hence, in the region {w0<x<u1}\{w\_{0}<x<u\_{1}\}, the HJB equation becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=12​N2​g′′​(x)+N1​g′​(x)−δ​g​(x),0=\frac{1}{2}N\_{2}g^{\prime\prime}(x)+N\_{1}g^{\prime}(x)-\delta g(x), |  | (7.5) |

where N1=N¯1​(M1)N\_{1}=\overline{N}\_{1}(M\_{1}) and N2=N¯2​(M1)N\_{2}=\overline{N}\_{2}(M\_{1}) are defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The solution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g2​(x)=K2+​eγ2+​(x−w0)+K2−​eγ2−​(x−w0),g\_{2}(x)=K\_{2+}e^{\gamma\_{2+}(x-w\_{0})}+K\_{2-}e^{\gamma\_{2-}(x-w\_{0})}, |  | (7.6) |

where γ2±:=γ¯2±​(M1)\gamma\_{2\pm}:=\overline{\gamma}\_{2\pm}(M\_{1}) are given by ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and K2±K\_{2\pm} are unknown constants.

In the region {u1<x<u2}\{u\_{1}<x<u\_{2}\}, the HJB equation becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=12​N2​g′′​(x)+(N1−c¯2)​g′​(x)−δ​g​(x)+(1−a)​c¯2,0=\frac{1}{2}N\_{2}g^{\prime\prime}(x)+(N\_{1}-\overline{c}\_{2})g^{\prime}(x)-\delta g(x)+(1-a)\overline{c}\_{2}, |  | (7.7) |

whose solution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g3​(x)=K3+​eγ3+​(x−u1)+K3−​eγ3−​(x−u1)+(1−a)​c¯2δ,g\_{3}(x)=K\_{3+}e^{\gamma\_{3+}(x-u\_{1})}+K\_{3-}e^{\gamma\_{3-}(x-u\_{1})}+\frac{(1-a)\overline{c}\_{2}}{\delta}, |  | (7.8) |

where γ3±:=γ¯3±​(M1)\gamma\_{3\pm}:=\overline{\gamma}\_{3\pm}(M\_{1}) are given by ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and K3±K\_{3\pm} are unknown constants.

In the region {x>u2}\{x>u\_{2}\}, the HJB equation becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=12​N2​g′′​(x)+(N1−c¯1−c¯2)​g′​(x)−δ​g​(x)+a​c¯1+(1−a)​c¯2,0=\frac{1}{2}N\_{2}g^{\prime\prime}(x)+(N\_{1}-\overline{c}\_{1}-\overline{c}\_{2})g^{\prime}(x)-\delta g(x)+a\overline{c}\_{1}+(1-a)\overline{c}\_{2}, |  | (7.9) |

whose solution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g4​(x)=K4−​eγ4−​(x−u2)+a​c¯1+(1−a)​c¯2δ,g\_{4}(x)=K\_{4-}e^{\gamma\_{4-}(x-u\_{2})}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}, |  | (7.10) |

where γ4−:=γ¯4−​(M1)\gamma\_{4-}:=\overline{\gamma}\_{4-}(M\_{1}) is defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). We conjecture the following solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)={K1​∫0xexp⁡[∫zw0κ1G−1​(y)​𝑑y]​𝑑zif x<w0,K2+​eγ2+​(x−w0)+K2−​eγ2−​(x−w0)if w0<x<u1,K3+​eγ3+​(x−u1)+K3−​eγ3−​(x−u1)+(1−a)​c¯2δif u1<x<u2,K4−​eγ4−​(x−u2)+a​c¯1+(1−a)​c¯2δif x>u2,g(x)=\begin{cases}K\_{1}\int\_{0}^{x}\exp\left[\int^{w\_{0}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<w\_{0}$,}\\ K\_{2+}e^{\gamma\_{2+}(x-w\_{0})}+K\_{2-}e^{\gamma\_{2-}(x-w\_{0})}&\mbox{if $w\_{0}<x<u\_{1}$,}\\ K\_{3+}e^{\gamma\_{3+}(x-u\_{1})}+K\_{3-}e^{\gamma\_{3-}(x-u\_{1})}+\frac{(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $u\_{1}<x<u\_{2}$,}\\ K\_{4-}e^{\gamma\_{4-}(x-u\_{2})}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $x>u\_{2}$,}\end{cases} |  | (7.11) |

where w0=G​(M1)w\_{0}=G(M\_{1}) and K1,K2±,K3±,K4−,u1,u2K\_{1},\,K\_{2\pm},\,K\_{3\pm},\,K\_{4-},\,u\_{1},\,u\_{2} are yet to be determined.

We now solve for the unknowns using the principle of smooth fit. At x=w0x=w\_{0}, we have the following system of equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K1\displaystyle K\_{1} | =K2+​γ2++K2−​γ2−\displaystyle=K\_{2+}\gamma\_{2+}+K\_{2-}\gamma\_{2-} |  | (7.12) |
|  | −K1​κ1M1\displaystyle-K\_{1}\frac{\kappa\_{1}}{M\_{1}} | =K2+​γ2+2+K2−​γ2−2,\displaystyle=K\_{2+}\gamma\_{2+}^{2}+K\_{2-}\gamma\_{2-}^{2}, |  |

whose solution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | K2+=K1​α2+andK2−=K1​α2−,K\_{2+}=K\_{1}\alpha\_{2+}\quad\mbox{and}\quad K\_{2-}=K\_{1}\alpha\_{2-}, |  | (7.13) |

where α2±\alpha\_{2\pm} are given in ([4.11](https://arxiv.org/html/2511.11383v1#S4.E11 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Recall that γ2−<0<γ2+\gamma\_{2-}<0<\gamma\_{2+}. It is then easy to see that α2−<0\alpha\_{2-}<0. To prove α2+>0\alpha\_{2+}>0, it suffices to show that −γ2−−κ1M1>0-\gamma\_{2-}-\frac{\kappa\_{1}}{M\_{1}}>0. This result is proved in the following lemma.

###### Lemma 7.1.

−κ1γ2−<M1-\frac{\kappa\_{1}}{\gamma\_{2-}}<M\_{1}.

###### Proof.

It holds that

|  |  |  |
| --- | --- | --- |
|  | σ~12=σ12​(M1)=∫0M1x2​dF1​(x)<M1​∫0M1x​dF1​(x)=M1​μ1​(M1)=M1​μ~1\widetilde{\sigma}\_{1}^{2}=\sigma\_{1}^{2}(M\_{1})=\int\_{0}^{M\_{1}}x^{2}\,\mathrm{d}F\_{1}(x)<M\_{1}\int\_{0}^{M\_{1}}x\,\mathrm{d}F\_{1}(x)=M\_{1}\mu\_{1}(M\_{1})=M\_{1}\widetilde{\mu}\_{1} |  |

and

|  |  |  |
| --- | --- | --- |
|  | σ22​(M1​κ2κ1)=∫0M1​κ2κ1x2​dF2​(x)<2​M1​κ2κ1​∫0M1​κ2κ1x​dF2​(x)=2​M1​κ2κ1​μ2​(M1​κ2κ1),\sigma\_{2}^{2}\left(\frac{M\_{1}\kappa\_{2}}{\kappa\_{1}}\right)=\int\_{0}^{\frac{M\_{1}\kappa\_{2}}{\kappa\_{1}}}x^{2}\,\mathrm{d}F\_{2}(x)<\frac{2M\_{1}\kappa\_{2}}{\kappa\_{1}}\int\_{0}^{\frac{M\_{1}\kappa\_{2}}{\kappa\_{1}}}x\,\mathrm{d}F\_{2}(x)=\frac{2M\_{1}\kappa\_{2}}{\kappa\_{1}}\mu\_{2}\left(\frac{M\_{1}\kappa\_{2}}{\kappa\_{1}}\right), |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | −κ1γ2−=κ1​N2N1+N12+2​δ​N2<κ1​N22​N1<M1​[N1+κ2​μ2​(M1​κ2κ1)]2​N1<M1,\displaystyle-\frac{\kappa\_{1}}{\gamma\_{2-}}=\frac{\kappa\_{1}N\_{2}}{N\_{1}+\sqrt{N\_{1}^{2}+2\delta N\_{2}}}<\frac{\kappa\_{1}N\_{2}}{2N\_{1}}<\frac{M\_{1}\left[N\_{1}+\kappa\_{2}\mu\_{2}\left(\frac{M\_{1}\kappa\_{2}}{\kappa\_{1}}\right)\right]}{2N\_{1}}<M\_{1}, |  |

which proves the result.
∎

We can then rewrite g2g\_{2} as

|  |  |  |
| --- | --- | --- |
|  | g2​(x)=K1​[α2+​eγ2+​(x−w0)+α2−​eγ2−​(x−w0)],g\_{2}(x)=K\_{1}\left[\alpha\_{2+}e^{\gamma\_{2+}(x-w\_{0})}+\alpha\_{2-}e^{\gamma\_{2-}(x-w\_{0})}\right], |  |

where K1>0K\_{1}>0 is still unknown.

By the definition of u1u\_{1} in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we have g′​(u1)=1−ag^{\prime}(u\_{1})=1-a. Hence,

|  |  |  |
| --- | --- | --- |
|  | 1−a=g3′​(u1)=K3+​γ3++K3−​γ3−,1-a=g^{\prime}\_{3}(u\_{1})=K\_{3+}\gamma\_{3+}+K\_{3-}\gamma\_{3-}, |  |

which is equivalent to K3+K\_{3+} defined in ([4.12](https://arxiv.org/html/2511.11383v1#S4.E12 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). It suffices to show that g2​(u1)=g3​(u1)g\_{2}(u\_{1})=g\_{3}(u\_{1}) and g2′​(u1)=g3′​(u1)g^{\prime}\_{2}(u\_{1})=g^{\prime}\_{3}(u\_{1}) to ensure that gg is twice continuously differentiable at x=u1x=u\_{1}. We then have the following system of equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K1​[α2+​eγ2+​(u1−w0)+α2−​eγ2−​(u1−w0)]\displaystyle K\_{1}\left[\alpha\_{2+}e^{\gamma\_{2+}(u\_{1}-w\_{0})}+\alpha\_{2-}e^{\gamma\_{2-}(u\_{1}-w\_{0})}\right] | =(1−a)​α3\displaystyle=(1-a)\alpha\_{3} |  | (7.14) |
|  | K1​[α2+​γ2+​eγ2+​(u1−w0)+α2−​γ2−​eγ2−​(u1−w0)]\displaystyle K\_{1}\left[\alpha\_{2+}\gamma\_{2+}e^{\gamma\_{2+}(u\_{1}-w\_{0})}+\alpha\_{2-}\gamma\_{2-}e^{\gamma\_{2-}(u\_{1}-w\_{0})}\right] | =(1−a),\displaystyle=(1-a), |  |

where α3\alpha\_{3} is defined in ([4.12](https://arxiv.org/html/2511.11383v1#S4.E12 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). From the second equation in ([7.14](https://arxiv.org/html/2511.11383v1#S7.E14 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we obtain K1K\_{1} defined in ([4.15](https://arxiv.org/html/2511.11383v1#S4.E15 "In item 2 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Dividing the first equation in ([7.14](https://arxiv.org/html/2511.11383v1#S7.E14 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) by the second equation yields

|  |  |  |
| --- | --- | --- |
|  | α2+​eγ2+​(u1−w0)+α2−​eγ2−​(u1−w0)α2+​γ2+​eγ2+​(u1−w0)+α2−​γ2−​eγ2−​(u1−w0)=α3,\frac{\alpha\_{2+}e^{\gamma\_{2+}(u\_{1}-w\_{0})}+\alpha\_{2-}e^{\gamma\_{2-}(u\_{1}-w\_{0})}}{\alpha\_{2+}\gamma\_{2+}e^{\gamma\_{2+}(u\_{1}-w\_{0})}+\alpha\_{2-}\gamma\_{2-}e^{\gamma\_{2-}(u\_{1}-w\_{0})}}=\alpha\_{3}, |  |

which is equivalent to u1u\_{1} defined in ([4.10](https://arxiv.org/html/2511.11383v1#S4.E10 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). We point out that we have yet to establish that u1u\_{1} is well defined.

By the definition of u2u\_{2}, we have g′​(u2)=ag^{\prime}(u\_{2})=a. Hence,

|  |  |  |
| --- | --- | --- |
|  | a=g4′​(u2)=K4−​α4−,a=g^{\prime}\_{4}(u\_{2})=K\_{4-}\alpha\_{4-}, |  |

or, equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | K4−=aγ4−.K\_{4-}=\frac{a}{\gamma\_{4-}}. |  | (7.15) |

It suffices to show that g3′​(u2)=g4′​(u2)g^{\prime}\_{3}(u\_{2})=g^{\prime}\_{4}(u\_{2}) and g3′′​(u2)=g4′′​(u2)g^{\prime\prime}\_{3}(u\_{2})=g^{\prime\prime}\_{4}(u\_{2}) to ensure that gg is twice continuously differentiable at x=u2x=u\_{2}. We then have the following system of equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K3+​γ3+​eγ3+​(u2−u1)+K3−​γ3−​eγ3−​(u2−u1)\displaystyle K\_{3+}\gamma\_{3+}e^{\gamma\_{3+}(u\_{2}-u\_{1})}+K\_{3-}\gamma\_{3-}e^{\gamma\_{3-}(u\_{2}-u\_{1})} | =a\displaystyle=a |  | (7.16) |
|  | K3+​γ3+2​eγ3+​(u2−u1)+K3−​γ3−2​eγ3−​(u2−u1)\displaystyle K\_{3+}\gamma\_{3+}^{2}e^{\gamma\_{3+}(u\_{2}-u\_{1})}+K\_{3-}\gamma\_{3-}^{2}e^{\gamma\_{3-}(u\_{2}-u\_{1})} | =a​γ4−.\displaystyle=a\gamma\_{4-}. |  |

Dividing the second equation by the first equation yields

|  |  |  |
| --- | --- | --- |
|  | K3+​γ3+2​eγ3+​(u2−u1)+K3−​γ3−2​eγ3−​(u2−u1)K3+​γ3+​eγ3+​(u2−u1)+K3−​γ3−​eγ3−​(u2−u1)=γ4−,\frac{K\_{3+}\gamma\_{3+}^{2}e^{\gamma\_{3+}(u\_{2}-u\_{1})}+K\_{3-}\gamma\_{3-}^{2}e^{\gamma\_{3-}(u\_{2}-u\_{1})}}{K\_{3+}\gamma\_{3+}e^{\gamma\_{3+}(u\_{2}-u\_{1})}+K\_{3-}\gamma\_{3-}e^{\gamma\_{3-}(u\_{2}-u\_{1})}}=\gamma\_{4-}, |  |

which is equivalent to u2u\_{2} defined in ([4.10](https://arxiv.org/html/2511.11383v1#S4.E10 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), where K3−K\_{3-} is still unknown. Thus, we have obtained the form of the value function in ([4.14](https://arxiv.org/html/2511.11383v1#S4.E14 "In item 2 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The next steps are (i) to establish that the formulas for u1u\_{1} and u2u\_{2} in ([4.10](https://arxiv.org/html/2511.11383v1#S4.E10 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) are well defined, (ii) to guarantee that w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2}, and (iii) to show that gg is increasing and concave.

#### Establishing the bounds for K3−K\_{3-}

We now establish the bounds for K3−K\_{3-}. Since the candidate value function gg must be positive for x>0x>0, we must have α3>0\alpha\_{3}>0 from the first equation in ([7.14](https://arxiv.org/html/2511.11383v1#S7.E14 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Since α2−<0<α2+\alpha\_{2-}<0<\alpha\_{2+}, we must have 1−γ2+​α3>01-\gamma\_{2+}\alpha\_{3}>0 for u1u\_{1} in ([4.10](https://arxiv.org/html/2511.11383v1#S4.E10 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) to be well defined. Combining these inequalities for α3\alpha\_{3} yields 0<α3<1γ2+0<\alpha\_{3}<\frac{1}{\gamma\_{2+}}, which is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | α¯<K3−<(1−a)​γ3+γ3+−γ3−(1γ2+−1γ3+−c¯2δ)=:α¯,\underline{\alpha}<K\_{3-}<\frac{(1-a)\gamma\_{3+}}{\gamma\_{3+}-\gamma\_{3-}}\left(\frac{1}{\gamma\_{2+}}-\frac{1}{\gamma\_{3+}}-\frac{\overline{c}\_{2}}{\delta}\right)=:\overline{\alpha}, |  | (7.17) |

where α¯\underline{\alpha} is defined in ([4.8](https://arxiv.org/html/2511.11383v1#S4.E8 "In Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). It is clear that α¯<α¯\underline{\alpha}<\overline{\alpha} since 1γ2+>0\frac{1}{\gamma\_{2+}}>0.

We have now established conditions under which ([4.10](https://arxiv.org/html/2511.11383v1#S4.E10 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is well defined; however, these conditions do not guarantee that w0≤u1w\_{0}\leq u\_{1}. The following lemma provides necessary and sufficient conditions for α0\alpha\_{0}, defined in ([4.8](https://arxiv.org/html/2511.11383v1#S4.E8 "In Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), to be a lower bound of K3−K\_{3-} that is greater than α¯\underline{\alpha}.

###### Lemma 7.2.

α0>α¯\alpha\_{0}>\underline{\alpha} if and only if

|  |  |  |
| --- | --- | --- |
|  | N1−κ1​N22​M1>0.N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}>0. |  |

###### Proof.

From ([7.17](https://arxiv.org/html/2511.11383v1#S7.E17 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and ([4.8](https://arxiv.org/html/2511.11383v1#S4.E8 "In Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), it follows that α0>α¯\alpha\_{0}>\underline{\alpha} if and only if N1δ−κ1​N22​δ​M1>0\frac{N\_{1}}{\delta}-\frac{\kappa\_{1}N\_{2}}{2\delta M\_{1}}>0. The result follows directly.
∎

The following lemma proves that α0\alpha\_{0} does not exceed the upper bound α¯\overline{\alpha}.

###### Lemma 7.3.

α0<α¯\alpha\_{0}<\overline{\alpha}.

###### Proof.

We can rewrite N1δ−κ1​N22​δ​M1<1γ2+\frac{N\_{1}}{\delta}-\frac{\kappa\_{1}N\_{2}}{2\delta M\_{1}}<\frac{1}{\gamma\_{2+}} as

|  |  |  |
| --- | --- | --- |
|  | (2​N1−κ1M1​N2)​(N12+2​δ​N2−N1)<2​δ​N2,\left(2N\_{1}-\frac{\kappa\_{1}}{M\_{1}}N\_{2}\right)\left(\sqrt{N\_{1}^{2}+2\delta N\_{2}}-N\_{1}\right)<2\delta N\_{2}, |  |

which immediately holds if N1<κ1​N22​M1N\_{1}<\frac{\kappa\_{1}N\_{2}}{2M\_{1}}. Suppose N1≥κ1​N22​M1N\_{1}\geq\frac{\kappa\_{1}N\_{2}}{2M\_{1}}. We can then rewrite the above inequality as

|  |  |  |
| --- | --- | --- |
|  | (2​N1−κ1M1​N2)​N12+2​δ​N2<2​δ​N2+2​N12−κ1M1​N1​N2.\left(2N\_{1}-\frac{\kappa\_{1}}{M\_{1}}N\_{2}\right)\sqrt{N\_{1}^{2}+2\delta N\_{2}}<2\delta N\_{2}+2N\_{1}^{2}-\frac{\kappa\_{1}}{M\_{1}}N\_{1}N\_{2}. |  |

Squaring both sides yields N1−κ1​N22​M1+δ​M1κ1>0N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}>0, which proves the result.
∎

The following result gives a necessary and sufficient condition to ensure that w0≤u1w\_{0}\leq u\_{1}.

###### Lemma 7.4.

w0≤u1w\_{0}\leq u\_{1} if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | α¯+(α0−α¯)⋅𝟙{N1>κ1​N22​M1}<K3−<α¯.\underline{\alpha}+\left(\alpha\_{0}-\underline{\alpha}\right)\cdot\mathds{1}\_{\{N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}}\}}<K\_{3-}<\overline{\alpha}. |  | (7.18) |

###### Proof.

From ([4.10](https://arxiv.org/html/2511.11383v1#S4.E10 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), w0≤u1w\_{0}\leq u\_{1} is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | α2−​(γ2−​α3−1)α2+​(1−γ2+​α3)≥1.\frac{\alpha\_{2-}(\gamma\_{2-}\alpha\_{3}-1)}{\alpha\_{2+}(1-\gamma\_{2+}\alpha\_{3})}\geq 1. |  | (7.19) |

Moreover, K3−<α¯K\_{3-}<\overline{\alpha} is equivalent to 1−γ2+​α3>01-\gamma\_{2+}\alpha\_{3}>0, and K3−>α¯K\_{3-}>\underline{\alpha} is equivalent to α3>0\alpha\_{3}>0. Hence, we can rewrite ([7.19](https://arxiv.org/html/2511.11383v1#S7.E19 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) as

|  |  |  |
| --- | --- | --- |
|  | α3≥N1δ−κ1​N22​δ​M1,\alpha\_{3}\geq\frac{N\_{1}}{\delta}-\frac{\kappa\_{1}N\_{2}}{2\delta M\_{1}}, |  |

or, equivalently,

|  |  |  |
| --- | --- | --- |
|  | K3−≥α0.K\_{3-}\geq\alpha\_{0}. |  |

Using Lemma [7.2](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem2 "Lemma 7.2. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") completes the proof.
∎

We now determine the signs of K3±K\_{3\pm}. First, we note that a sufficient condition such that gg is increasing, particularly in the region {u1<x<u2}\{u\_{1}<x<u\_{2}\}, is K3−≤0≤K3+K\_{3-}\leq 0\leq K\_{3+}. The following lemma proves that K3−<0K\_{3-}<0.

###### Lemma 7.5.

K3−<0K\_{3-}<0.

###### Proof.

From ([7.17](https://arxiv.org/html/2511.11383v1#S7.E17 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), it suffices to prove that

|  |  |  |
| --- | --- | --- |
|  | c¯2δ≥1γ2+−1γ3+.\frac{\overline{c}\_{2}}{\delta}\geq\frac{1}{\gamma\_{2+}}-\frac{1}{\gamma\_{3+}}. |  |

Write k:=2​δ​N2>0k:=2\delta N\_{2}>0. Suppose otherwise that c¯2δ<1γ2+−1γ3+\frac{\overline{c}\_{2}}{\delta}<\frac{1}{\gamma\_{2+}}-\frac{1}{\gamma\_{3+}}. This is equivalent to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 2​c¯2​(N1−c¯2)2+k⋅N12+k−c¯2​(k−2​N1​(N1−c¯2))\displaystyle 2\overline{c}\_{2}\sqrt{(N\_{1}-\overline{c}\_{2})^{2}+k}\cdot\sqrt{N\_{1}^{2}+k}-\overline{c}\_{2}\left(k-2N\_{1}(N\_{1}-\overline{c}\_{2})\right) |  | (7.20) |
|  |  | <(2​N1​c¯2+k)​(N1−c¯2)2+k+(2​c¯2​(N1−c¯2)−k)​N12+k.\displaystyle<(2N\_{1}\overline{c}\_{2}+k)\sqrt{(N\_{1}-\overline{c}\_{2})^{2}+k}+(2\overline{c}\_{2}(N\_{1}-\overline{c}\_{2})-k)\sqrt{N\_{1}^{2}+k}. |  |

The left-hand side of ([7.20](https://arxiv.org/html/2511.11383v1#S7.E20 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) can be shown to be always positive. If the right-hand side of ([7.20](https://arxiv.org/html/2511.11383v1#S7.E20 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is negative, it results in a contradiction. Otherwise, we can square both sides and get

|  |  |  |
| --- | --- | --- |
|  | c¯22​k<0,\overline{c}\_{2}^{2}k<0, |  |

which is also a contradiction. The proof is complete.
∎

We now show that K3+≥0K\_{3+}\geq 0. Using ([4.12](https://arxiv.org/html/2511.11383v1#S4.E12 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we must have the following:

|  |  |  |
| --- | --- | --- |
|  | K3−≥1−aγ3−.K\_{3-}\geq\frac{1-a}{\gamma\_{3-}}. |  |

The following lemma proves that 1−aγ3−\frac{1-a}{\gamma\_{3-}} does not exceed the upper bound α¯\overline{\alpha}.

###### Lemma 7.6.

1−aγ3−<α¯\frac{1-a}{\gamma\_{3-}}<\overline{\alpha}.

###### Proof.

It suffices to prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  | c¯2δ<1γ2+−1γ3−.\frac{\overline{c}\_{2}}{\delta}<\frac{1}{\gamma\_{2+}}-\frac{1}{\gamma\_{3-}}. |  | (7.21) |

From the elementary inequality

|  |  |  |
| --- | --- | --- |
|  | A2+B−A<B2​A,A,B>0,\sqrt{A^{2}+B}-A<\frac{B}{2A},\quad A,B>0, |  |

we obtain the following:

|  |  |  |
| --- | --- | --- |
|  | γ2+<δN1⇔1γ2+>N1δ.\gamma\_{2+}<\frac{\delta}{N\_{1}}\Leftrightarrow\frac{1}{\gamma\_{2+}}>\frac{N\_{1}}{\delta}. |  |

If N1−c¯2≤0N\_{1}-\overline{c}\_{2}\leq 0, then

|  |  |  |
| --- | --- | --- |
|  | −γ3−<δc¯2−N1⇔−1γ3−>c¯2−N1δ,-\gamma\_{3-}<\frac{\delta}{\overline{c}\_{2}-N\_{1}}\Leftrightarrow-\frac{1}{\gamma\_{3-}}>\frac{\overline{c}\_{2}-N\_{1}}{\delta}, |  |

and ([7.21](https://arxiv.org/html/2511.11383v1#S7.E21 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) follows. If N1−c¯2>0N\_{1}-\overline{c}\_{2}>0, then

|  |  |  |
| --- | --- | --- |
|  | γ2+<δN1<δc¯2⇔c¯2δ<1γ2+,\gamma\_{2+}<\frac{\delta}{N\_{1}}<\frac{\delta}{\overline{c}\_{2}}\Leftrightarrow\frac{\overline{c}\_{2}}{\delta}<\frac{1}{\gamma\_{2+}}, |  |

and ([7.21](https://arxiv.org/html/2511.11383v1#S7.E21 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) follows since γ3−<0\gamma\_{3-}<0. The proof is complete.
∎

We now determine the conditions under which 1−aγ3−\frac{1-a}{\gamma\_{3-}}, α0\alpha\_{0}, or α¯\underline{\alpha} serves as the lower bound for K3−K\_{3-} via the lemma below.

###### Lemma 7.7.

1. (i)

   1−aγ3−>α¯\frac{1-a}{\gamma\_{3-}}>\underline{\alpha} if and only if

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | c¯2>δ​N22​N1.\overline{c}\_{2}>\frac{\delta N\_{2}}{2N\_{1}}. |  | (7.22) |
2. (ii)

   1−aγ3−>α0\frac{1-a}{\gamma\_{3-}}>\alpha\_{0} if and only if

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | c¯2>N1−κ1​N22​M1+δ​M1κ1.\overline{c}\_{2}>N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. |  | (7.23) |

###### Proof.

1−aγ3−>α¯\frac{1-a}{\gamma\_{3-}}>\underline{\alpha} is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​N2−c¯2​(N1−c¯2)<c¯2​(N1−c¯2)2+2​δ​N2.\delta N\_{2}-\overline{c}\_{2}(N\_{1}-\overline{c}\_{2})<\overline{c}\_{2}\sqrt{(N\_{1}-\overline{c}\_{2})^{2}+2\delta N\_{2}}. |  | (7.24) |

The inequality holds when δ​N2−c¯2​(N1−c¯2)<0\delta N\_{2}-\overline{c}\_{2}(N\_{1}-\overline{c}\_{2})<0, or, equivalently, N1​c¯2>δ​N2+c¯22N\_{1}\overline{c}\_{2}>\delta N\_{2}+\overline{c}\_{2}^{2}. Squaring both sides of ([7.24](https://arxiv.org/html/2511.11383v1#S7.E24 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) yields ([7.22](https://arxiv.org/html/2511.11383v1#S7.E22 "In item (i) ‣ Lemma 7.7. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), which is equivalent to N1​c¯2>δ​N22N\_{1}\overline{c}\_{2}>\frac{\delta N\_{2}}{2}. Since δ​N2+c¯22>δ​N22\delta N\_{2}+\overline{c}\_{2}^{2}>\frac{\delta N\_{2}}{2}, then (i)(i) follows.

1−aγ3−>α0\frac{1-a}{\gamma\_{3-}}>\alpha\_{0} is equivalent to

|  |  |  |
| --- | --- | --- |
|  | 1<γ3−​(N1−c¯2δ−κ1​N22​δ​M1).1<\gamma\_{3-}\left(\frac{N\_{1}-\overline{c}\_{2}}{\delta}-\frac{\kappa\_{1}N\_{2}}{2\delta M\_{1}}\right). |  |

A necessary condition for the above inequality to hold is that c¯2>N1−κ1​N22​M1\overline{c}\_{2}>N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}. Moreover, the inequality is equivalent to the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​δ​M1​N2+2​M1​(N1−c¯2)2−κ1​N2​(N1−c¯2)<(κ1​N2−2​M1​(N1−c¯2))​(N1−c¯2)2+2​δ​N2.2\delta M\_{1}N\_{2}+2M\_{1}(N\_{1}-\overline{c}\_{2})^{2}-\kappa\_{1}N\_{2}(N\_{1}-\overline{c}\_{2})<(\kappa\_{1}N\_{2}-2M\_{1}(N\_{1}-\overline{c}\_{2}))\sqrt{(N\_{1}-\overline{c}\_{2})^{2}+2\delta N\_{2}}. |  | (7.25) |

The above inequality is immediately satisfied when 2​M1​(N1−c¯2)2−κ1​N2​(N1−c¯2)<−2​δ​M1​N22M\_{1}(N\_{1}-\overline{c}\_{2})^{2}-\kappa\_{1}N\_{2}(N\_{1}-\overline{c}\_{2})<-2\delta M\_{1}N\_{2} (i.e., the left-hand side is negative) and c¯2>N1−κ1​N22​M1\overline{c}\_{2}>N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}} (i.e., the right-hand side is positive). We call this scenario the “trivial” case.

Squaring both sides of ([7.25](https://arxiv.org/html/2511.11383v1#S7.E25 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) yields ([7.23](https://arxiv.org/html/2511.11383v1#S7.E23 "In item (ii) ‣ Lemma 7.7. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), which satisfies the necessary condition. It must be noted that squaring both sides of ([7.25](https://arxiv.org/html/2511.11383v1#S7.E25 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is valid if N1−c¯2<0N\_{1}-\overline{c}\_{2}<0. Moreover, if N1−c¯2>0N\_{1}-\overline{c}\_{2}>0, we can rewrite ([7.23](https://arxiv.org/html/2511.11383v1#S7.E23 "In item (ii) ‣ Lemma 7.7. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) as 2​M1​(N1−c¯2)2−κ1​N2​(N1−c¯2)<−2​δ​M12​(N1−c¯2)κ12M\_{1}(N\_{1}-\overline{c}\_{2})^{2}-\kappa\_{1}N\_{2}(N\_{1}-\overline{c}\_{2})<-\frac{2\delta M\_{1}^{2}(N\_{1}-\overline{c}\_{2})}{\kappa\_{1}}. Since −2​δ​M1​N2<−2​δ​M12​(N1−c¯2)κ1-2\delta M\_{1}N\_{2}<-\frac{2\delta M\_{1}^{2}(N\_{1}-\overline{c}\_{2})}{\kappa\_{1}} if 0<N1−c¯2<κ1​N2M10<N\_{1}-\overline{c}\_{2}<\frac{\kappa\_{1}N\_{2}}{M\_{1}}, then the trivial case is covered by (i​i)(ii). The proof is complete.
∎

Before presenting the formula for the lower bound of K3−K\_{3-}, we state the following lemma which is useful in bridging the results of Lemmas [7.4](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem4 "Lemma 7.4. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [7.7](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem7 "Lemma 7.7. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"):

###### Lemma 7.8.

δ​N22​N1<N1−κ1​N22​M1+δ​M1κ1\frac{\delta N\_{2}}{2N\_{1}}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} if and only if

|  |  |  |
| --- | --- | --- |
|  | N1>κ1​N22​M1.N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}}. |  |

###### Proof.

δ​N22​N1≤N1−κ1​N22​M1+δ​M1κ1\frac{\delta N\_{2}}{2N\_{1}}\leq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} is equivalent to

|  |  |  |
| --- | --- | --- |
|  | 2​κ1​M1​N12+(2​δ​M12−κ12​N2)​N1−δ​κ1​M1​N2>0.2\kappa\_{1}M\_{1}N\_{1}^{2}+(2\delta M\_{1}^{2}-\kappa\_{1}^{2}N\_{2})N\_{1}-\delta\kappa\_{1}M\_{1}N\_{2}>0. |  |

Solving the inequality with respect to N1N\_{1} yields

|  |  |  |
| --- | --- | --- |
|  | N1>κ1​N22​M1orN1<−δ​M1κ1.N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}}\quad\mbox{or}\quad N\_{1}<-\frac{\delta M\_{1}}{\kappa\_{1}}. |  |

Since N1>0N\_{1}>0, the result follows.
∎

Following the results of Lemmas [7.4](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem4 "Lemma 7.4. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [7.7](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem7 "Lemma 7.7. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), and [7.8](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem8 "Lemma 7.8. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), we now present the four cases that yield the expression for the lower bound of K3−K\_{3-} (denoted by αL​B\alpha\_{LB}):

* (i)

  If N1>κ1​N22​M1N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2≥N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}, then αL​B=1−aγ3−>α0>α¯\alpha\_{LB}=\frac{1-a}{\gamma\_{3-}}>\alpha\_{0}>\underline{\alpha}.
* (ii)

  If N1>κ1​N22​M1N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}, then αL​B=α0>(α¯∨1−aγ3−)\alpha\_{LB}=\alpha\_{0}>\left(\underline{\alpha}\vee\frac{1-a}{\gamma\_{3-}}\right).
* (iii)

  If N1≤κ1​N22​M1N\_{1}\leq\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2≥δ​N22​N1\overline{c}\_{2}\geq\frac{\delta N\_{2}}{2N\_{1}}, then αL​B=1−aγ3−>α¯>α0\alpha\_{LB}=\frac{1-a}{\gamma\_{3-}}>\underline{\alpha}>\alpha\_{0}.
* (iv)

  If N1≤κ1​N22​M1N\_{1}\leq\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2<δ​N22​N1\overline{c}\_{2}<\frac{\delta N\_{2}}{2N\_{1}}, then αL​B=α¯>(α0∨1−aγ3−)\alpha\_{LB}=\underline{\alpha}>\left(\alpha\_{0}\vee\frac{1-a}{\gamma\_{3-}}\right).

For case (iii), we used Lemma [7.8](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem8 "Lemma 7.8. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") to combine the inequalities c¯2≥N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} and c¯2≥δ​N22​N1\overline{c}\_{2}\geq\frac{\delta N\_{2}}{2N\_{1}}. For case (iv), we also used Lemma [7.8](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem8 "Lemma 7.8. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") to combine two subcases: (1) N1−κ1​N22​M1+δ​M1κ1≤c¯2<δ​N22​N1N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}\leq\overline{c}\_{2}<\frac{\delta N\_{2}}{2N\_{1}} and (2) c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. Hence, we obtain the formula for αL​B\alpha\_{LB} given in ([4.8](https://arxiv.org/html/2511.11383v1#S4.E8 "In Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Thus, K3−<0<K3+K\_{3-}<0<K\_{3+} and w0≤u1w\_{0}\leq u\_{1} if the following inequalities hold:

|  |  |  |
| --- | --- | --- |
|  | αL​B<K3−<α¯.\alpha\_{LB}<K\_{3-}<\overline{\alpha}. |  |

###### Remark 7.9.

It follows that gg is strictly increasing in the region {u1<x<u2}\{u\_{1}<x<u\_{2}\}. It can easily be shown that gg is also strictly increasing in the other regions. By the continuity of the first derivative, gg is strictly increasing for all x>0x>0.

It can also be easily shown that gg is strictly concave in the regions {x<w0}\{x<w\_{0}\} and {x>u2}\{x>u\_{2}\}. Since g′′′>0g^{\prime\prime\prime}>0 in the regions {w0<x<u1}\{w\_{0}<x<u\_{1}\} and {u1<x<u2}\{u\_{1}<x<u\_{2}\}, then, by the continuity of the second derivative, gg is strictly concave on [w0,u2][w\_{0},u\_{2}].

It can be shown that γ4−−γ3−>0\gamma\_{4-}-\gamma\_{3-}>0. Hence, u2u\_{2} is well defined. We now require that u1≤u2u\_{1}\leq u\_{2}. The following lemma gives a necessary and sufficient condition such that u1≤u2u\_{1}\leq u\_{2}.

###### Lemma 7.10.

u1≤u2u\_{1}\leq u\_{2} if and only if

|  |  |  |
| --- | --- | --- |
|  | K3−≤(1−a)​(γ3+−γ4−)γ3−​(γ3+−γ3−)=:αU​B.K\_{3-}\leq\frac{(1-a)(\gamma\_{3+}-\gamma\_{4-})}{\gamma\_{3-}(\gamma\_{3+}-\gamma\_{3-})}=:\alpha\_{UB}. |  |

###### Proof.

From ([4.10](https://arxiv.org/html/2511.11383v1#S4.E10 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), u1≤u2u\_{1}\leq u\_{2} is equivalent to

|  |  |  |
| --- | --- | --- |
|  | K3−​γ3−​(γ4−−γ3−)K3+​γ3+​(γ3+−γ4−)≥1.\frac{K\_{3-}\gamma\_{3-}(\gamma\_{4-}-\gamma\_{3-})}{K\_{3+}\gamma\_{3+}(\gamma\_{3+}-\gamma\_{4-})}\geq 1. |  |

Using ([4.12](https://arxiv.org/html/2511.11383v1#S4.E12 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) yields the result.
∎

The following lemma proves that αU​B\alpha\_{UB} is a lower upper bound of K3−K\_{3-}.

###### Lemma 7.11.

αU​B≤α¯\alpha\_{UB}\leq\overline{\alpha}.

###### Proof.

αU​B≤α¯\alpha\_{UB}\leq\overline{\alpha} is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | N12+2​δ​N2​(N1−c¯1−c¯2)2+2​δ​N2≥−N1​(N1−c¯1−c¯2)−2​δ​N2.\sqrt{N\_{1}^{2}+2\delta N\_{2}}\sqrt{(N\_{1}-\overline{c}\_{1}-\overline{c}\_{2})^{2}+2\delta N\_{2}}\geq-N\_{1}(N\_{1}-\overline{c}\_{1}-\overline{c}\_{2})-2\delta N\_{2}. |  | (7.26) |

The above inequality is always true if c¯1+c¯2<N1+2​δ​N2N1\overline{c}\_{1}+\overline{c}\_{2}<N\_{1}+\frac{2\delta N\_{2}}{N\_{1}}. Suppose c¯1+c¯2≥N1+2​δ​N2N1\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}+\frac{2\delta N\_{2}}{N\_{1}}. Squaring both sides of the inequality ([7.26](https://arxiv.org/html/2511.11383v1#S7.E26 "In Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) yields

|  |  |  |
| --- | --- | --- |
|  | (c¯1+c¯2)2≥0,(\overline{c}\_{1}+\overline{c}\_{2})^{2}\geq 0, |  |

which is always true. The result is proved.
∎

The following lemma gives a necessary and sufficient condition such that αL​B≤αU​B\alpha\_{LB}\leq\alpha\_{UB}.

###### Lemma 7.12.

αL​B≤αU​B\alpha\_{LB}\leq\alpha\_{UB} if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | c¯1+c¯2≥N1−κ1​N22​M1+δ​M1κ1.\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. |  | (7.27) |

###### Proof.

Suppose N1>κ1​N22​M1N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2≥N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. Then, αL​B=1−aγ3−\alpha\_{LB}=\frac{1-a}{\gamma\_{3-}} and αL​B≤αU​B\alpha\_{LB}\leq\alpha\_{UB} are equivalent to

|  |  |  |
| --- | --- | --- |
|  | γ3−−γ4−≤0,\gamma\_{3-}-\gamma\_{4-}\leq 0, |  |

which can be shown to be always true. Since c¯1>0\overline{c}\_{1}>0, then ([7.27](https://arxiv.org/html/2511.11383v1#S7.E27 "In Lemma 7.12. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) follows. For the case N1≤κ1​N22​M1N\_{1}\leq\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2≥δ​N22​N1\overline{c}\_{2}\geq\frac{\delta N\_{2}}{2N\_{1}}, we also obtain the equivalence between αL​B≤αU​B\alpha\_{LB}\leq\alpha\_{UB} and γ3−−γ4−≤0\gamma\_{3-}-\gamma\_{4-}\leq 0. By Lemma [7.8](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem8 "Lemma 7.8. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), δ​N22​N1≥N1−κ1​N22​M1+δ​M1κ1\frac{\delta N\_{2}}{2N\_{1}}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}, which implies ([7.27](https://arxiv.org/html/2511.11383v1#S7.E27 "In Lemma 7.12. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

Suppose N1>κ1​N22​M1N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. Then, αL​B=α0\alpha\_{LB}=\alpha\_{0} and αL​B≤αU​B\alpha\_{LB}\leq\alpha\_{UB} are equivalent to

|  |  |  |
| --- | --- | --- |
|  | −(N1−c¯1−c¯2)+κ1​N2M1≥(N1−c¯1−c¯2)2+2​δ​N2,-(N\_{1}-\overline{c}\_{1}-\overline{c}\_{2})+\frac{\kappa\_{1}N\_{2}}{M\_{1}}\geq\sqrt{(N\_{1}-\overline{c}\_{1}-\overline{c}\_{2})^{2}+2\delta N\_{2}}, |  |

which holds only if c¯1+c¯2≥N1−κ1​N2M1\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{M\_{1}}. Squaring both sides of the above inequality yields

|  |  |  |
| --- | --- | --- |
|  | c¯1+c¯2≥N1−κ1​N22​M1+δ​M1κ1>N1−κ1​N2M1,\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}>N\_{1}-\frac{\kappa\_{1}N\_{2}}{M\_{1}}, |  |

which proves the result for when αL​B=α0\alpha\_{LB}=\alpha\_{0}.

Suppose N1≤κ1​N22​M1N\_{1}\leq\frac{\kappa\_{1}N\_{2}}{2M\_{1}} and c¯2<δ​N22​N1\overline{c}\_{2}<\frac{\delta N\_{2}}{2N\_{1}}. Then, αL​B=α¯\alpha\_{LB}=\underline{\alpha} and αL​B≤αU​B\alpha\_{LB}\leq\alpha\_{UB} are equivalent to

|  |  |  |
| --- | --- | --- |
|  | N1+c¯1+c¯2≥(N1−c¯1+c¯2)2+2​δ​N2.N\_{1}+\overline{c}\_{1}+\overline{c}\_{2}\geq\sqrt{(N\_{1}-\overline{c}\_{1}+\overline{c}\_{2})^{2}+2\delta N\_{2}}. |  |

Squaring both sides yields

|  |  |  |
| --- | --- | --- |
|  | c¯1+c¯2≥δ​N22​N1>N1−κ1​N22​M1+δ​M1κ1,\overline{c}\_{1}+\overline{c}\_{2}\geq\frac{\delta N\_{2}}{2N\_{1}}>N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}, |  |

where the second inequality follows from Lemma [7.8](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem8 "Lemma 7.8. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). The proof is complete.
∎

We now state the following result which gives a necessary and sufficient condition such that w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2}.

###### Lemma 7.13.

w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2} if and only if K3−∈(αL​B,αU​B)K\_{3-}\in(\alpha\_{LB},\alpha\_{UB}).

###### Proof.

This is a direct consequence of Lemmas [7.4](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem4 "Lemma 7.4. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), [7.10](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem10 "Lemma 7.10. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), and [7.12](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem12 "Lemma 7.12. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance").
∎

#### Solving for K3−K\_{3-}

It remains to prove the existence of K3−K\_{3-}. We do this via the first equation in ([7.16](https://arxiv.org/html/2511.11383v1#S7.E16 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), which ensures that the first derivative at x=u2x=u\_{2} is continuous. The following lemma gives a necessary and sufficient condition such that K3−K\_{3-} exists and is unique.

###### Lemma 7.14.

K3−K\_{3-} is the unique solution to ψ​(z)=0\psi(z)=0 in (αL​B,αU​B)(\alpha\_{LB},\alpha\_{UB}) if and only if ψ​(αL​B)≤0\psi(\alpha\_{LB})\leq 0, where ψ\psi is defined in ([4.7](https://arxiv.org/html/2511.11383v1#S4.E7 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

###### Proof.

We can rewrite ψ\psi as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(z)\displaystyle\psi(z) | =(1−a−γ3−​z)​[γ3−​(γ4−−γ3−)​z(1−a−γ3−​z)​(γ3+−γ4−)]γ3+γ3+−γ3−+γ3−​z​eγ3−​ζ​(z)−a\displaystyle=(1-a-\gamma\_{3-}z)\left[\frac{\gamma\_{3-}(\gamma\_{4-}-\gamma\_{3-})z}{(1-a-\gamma\_{3-}z)(\gamma\_{3+}-\gamma\_{4-})}\right]^{\frac{\gamma\_{3+}}{\gamma\_{3+}-\gamma\_{3-}}}+\gamma\_{3-}ze^{\gamma\_{3-}\zeta(z)}-a |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−a−γ3−​z)−γ3−γ3+−γ3−​[γ3−​(γ4−−γ3−)​zγ3+−γ4−]γ3+γ3+−γ3−+γ3−​z​eγ3−​ζ​(z)−a.\displaystyle=(1-a-\gamma\_{3-}z)^{-\frac{\gamma\_{3-}}{\gamma\_{3+}-\gamma\_{3-}}}\left[\frac{\gamma\_{3-}(\gamma\_{4-}-\gamma\_{3-})z}{\gamma\_{3+}-\gamma\_{4-}}\right]^{\frac{\gamma\_{3+}}{\gamma\_{3+}-\gamma\_{3-}}}+\gamma\_{3-}ze^{\gamma\_{3-}\zeta(z)}-a. |  |

Since γ3−<0\gamma\_{3-}<0 and limz↓1−aγ3−ζ​(z)=+∞\lim\_{z\downarrow\frac{1-a}{\gamma\_{3-}}}\zeta(z)=+\infty, then limz↓1−aγ3−ψ​(z)=−a<0\lim\_{z\downarrow\frac{1-a}{\gamma\_{3-}}}\psi(z)=-a<0. From Lemma [7.10](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem10 "Lemma 7.10. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), ζ​(αU​B)=0\zeta(\alpha\_{UB})=0. Since a≤12a\leq\frac{1}{2}, ψ​(αU​B)=1−2​a>0\psi(\alpha\_{UB})=1-2a>0. Hence, by the intermediate value theorem, there exists a z0∈(1−aγ3−,αU​B)z\_{0}\in\left(\frac{1-a}{\gamma\_{3-}},\alpha\_{UB}\right) such that ψ​(z0)=0\psi(z\_{0})=0. We now prove the uniqueness of z0z\_{0}. From the definitions of ζ\zeta and ψ\psi in ([4.7](https://arxiv.org/html/2511.11383v1#S4.E7 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ′​(z)\displaystyle\zeta^{\prime}(z) | =1−a(γ3+−γ3−)​(1−a−γ3−​z)​z,\displaystyle=\frac{1-a}{(\gamma\_{3+}-\gamma\_{3-})(1-a-\gamma\_{3-}z)z}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ′​(z)\displaystyle\psi^{\prime}(z) | =γ3−​(eγ3−​ζ​(z)−eγ3+​ζ​(z))+1−aγ3+−γ3−​[γ3+z​eγ3+​ζ​(z)+γ3−21−a−γ3−​z​eγ3−​ζ​(z)].\displaystyle=\gamma\_{3-}\left(e^{\gamma\_{3-}\zeta(z)}-e^{\gamma\_{3+}\zeta(z)}\right)+\frac{1-a}{\gamma\_{3+}-\gamma\_{3-}}\left[\frac{\gamma\_{3+}}{z}e^{\gamma\_{3+}\zeta(z)}+\frac{\gamma\_{3-}^{2}}{1-a-\gamma\_{3-}z}e^{\gamma\_{3-}\zeta(z)}\right]. |  |

Since γ3+>γ3−\gamma\_{3+}>\gamma\_{3-}, it holds that

|  |  |  |
| --- | --- | --- |
|  | (γ3+−γ3−)​ζ​(z)=ln⁡(γ3−​(γ4−−γ3−)​z(1−a−γ3−​z)​(γ3+−γ4−))<ln⁡(−γ3−2​zγ3+​(1−a−γ3−​z)).(\gamma\_{3+}-\gamma\_{3-})\zeta(z)=\ln\left(\frac{\gamma\_{3-}(\gamma\_{4-}-\gamma\_{3-})z}{(1-a-\gamma\_{3-}z)(\gamma\_{3+}-\gamma\_{4-})}\right)<\ln\left(\frac{-\gamma\_{3-}^{2}z}{\gamma\_{3+}(1-a-\gamma\_{3-}z)}\right). |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | γ3+z​eγ3+​ζ​(z)>−γ3−21−a−γ3−​z​eγ3−​ζ​(z).\frac{\gamma\_{3+}}{z}e^{\gamma\_{3+}\zeta(z)}>\frac{-\gamma\_{3-}^{2}}{1-a-\gamma\_{3-}z}e^{\gamma\_{3-}\zeta(z)}. |  |

Now using ζ​(z)≥0\zeta(z)\geq 0 for z∈(1−aγ3−,αU​B)z\in\left(\frac{1-a}{\gamma\_{3-}},\alpha\_{UB}\right), we obtain ψ′​(z)>0\psi^{\prime}(z)>0 on (1−aγ3−,αU​B)\left(\frac{1-a}{\gamma\_{3-}},\alpha\_{UB}\right). Hence, z0z\_{0} is unique.

If αL​B=1−aγ3−\alpha\_{LB}=\frac{1-a}{\gamma\_{3-}}, the result immediately follows by choosing z0=α3−z\_{0}=\alpha\_{3-}. Suppose αL​B=α0\alpha\_{LB}=\alpha\_{0} or αL​B=α¯\alpha\_{LB}=\underline{\alpha}. If ψ​(αL​B)≤0\psi(\alpha\_{LB})\leq 0, then the result follows by choosing z0=α3−z\_{0}=\alpha\_{3-}. Suppose ψ​(αL​B)>0\psi(\alpha\_{LB})>0. By the intermediate value theorem and the strict monotonicity of ψ\psi, the unique solution z1z\_{1} of ψ\psi is on the interval (1−aγ3−,αL​B)\left(\frac{1-a}{\gamma\_{3-}},\alpha\_{LB}\right). Hence, there is no solution on the interval (αL​B,αU​B)(\alpha\_{LB},\alpha\_{UB}). The proof is complete.
∎

###### Remark 7.15.

Lemmas [7.14](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem14 "Lemma 7.14. ‣ Solving for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [7.8](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem8 "Lemma 7.8. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") imply that if c¯2≥N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} holds, then the existence (and uniqueness) of K3−K\_{3-} is guaranteed.

### 7.2 Proof of Theorem [4.3](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")

#### Deriving the analytical solution

Suppose for now that u1<w0≤u2u\_{1}<w\_{0}\leq u\_{2} and w0w\_{0} exists. In the region {x<u1}\{x<u\_{1}\}, the HJB equation becomes ([7.1](https://arxiv.org/html/2511.11383v1#S7.E1 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and its solution is given by g1​(x)=K1​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zg\_{1}(x)=K\_{1}\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz, where K1>0K\_{1}>0 is a constant and G−1G^{-1} is the inverse of GG given by ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). We also obtain π1∗​(x)=G−1​(x)\pi\_{1}^{\*}(x)=G^{-1}(x).

In the region {u1<x<w0}\{u\_{1}<x<w\_{0}\}, we have π1∗​(x)=π^1​(x)\pi\_{1}^{\*}(x)=\widehat{\pi}\_{1}(x) and the HJB equation becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=[κ1​μ1​(π1∗​(x))+κ2​μ2​(κ2κ1​π1∗​(x))−c¯2]​g′​(x)+[12​σ12​(π1∗​(x))+12​σ22​(κ2κ1​π1∗​(x))]​g′′​(x)−δ​g​(x)+(1−a)​c¯2.0=\left[\kappa\_{1}\mu\_{1}(\pi^{\*}\_{1}(x))+\kappa\_{2}\mu\_{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)-\overline{c}\_{2}\right]g^{\prime}(x)+\left[\frac{1}{2}\sigma\_{1}^{2}(\pi^{\*}\_{1}(x))+\frac{1}{2}\sigma\_{2}^{2}\left(\frac{\kappa\_{2}}{\kappa\_{1}}\pi^{\*}\_{1}(x)\right)\right]g^{\prime\prime}(x)-\delta g(x)+(1-a)\overline{c}\_{2}. |  | (7.28) |

Using ([4.4](https://arxiv.org/html/2511.11383v1#S4.E4 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we obtain π1∗​(x)=H​(x)\pi\_{1}^{\*}(x)=H(x), where HH satisfies the differential equation in ([4.17](https://arxiv.org/html/2511.11383v1#S4.E17 "In item 1 ‣ Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Hence, w0w\_{0} exists and satisfies H​(w0)=M1H(w\_{0})=M\_{1} via ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Similar to solving ([7.1](https://arxiv.org/html/2511.11383v1#S7.E1 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we obtain the following solution for ([7.28](https://arxiv.org/html/2511.11383v1#S7.E28 "In Deriving the analytical solution ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")):

|  |  |  |
| --- | --- | --- |
|  | g2​(x)=K2+​∫u1xexp⁡[∫zw0κ1H​(y)​𝑑y]​𝑑z+K2−,g\_{2}(x)=K\_{2+}\int\_{u\_{1}}^{x}\exp\left[\int^{w\_{0}}\_{z}\frac{\kappa\_{1}}{H(y)}dy\right]dz+K\_{2-}, |  |

where K2±K\_{2\pm} are unknown constants.

In the region {w0<x<u2}\{w\_{0}<x<u\_{2}\}, the HJB equation becomes ([7.7](https://arxiv.org/html/2511.11383v1#S7.E7 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), whose solution is of the form given in ([7.8](https://arxiv.org/html/2511.11383v1#S7.E8 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). In the region {x>u2}\{x>u\_{2}\}, the HJB equation simplifies to ([7.9](https://arxiv.org/html/2511.11383v1#S7.E9 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), which has a solution described by ([7.10](https://arxiv.org/html/2511.11383v1#S7.E10 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).
We conjecture the following solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)={K1​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zif x<u1,K2+​∫u1xexp⁡[∫zw0κ1H​(y)​𝑑y]​𝑑z+K2−if u1<x<w0,K3+​eγ3+​(x−u1)+K3−​eγ3−​(x−u1)+(1−a)​c¯2δif w0<x<u2,K4−​eγ4−​(x−u2)+a​c¯1+(1−a)​c¯2δif x>u2,g(x)=\begin{cases}K\_{1}\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<u\_{1}$,}\\ K\_{2+}\int\_{u\_{1}}^{x}\exp\left[\int^{w\_{0}}\_{z}\frac{\kappa\_{1}}{H(y)}dy\right]dz+K\_{2-}&\mbox{if $u\_{1}<x<w\_{0}$,}\\ K\_{3+}e^{\gamma\_{3+}(x-u\_{1})}+K\_{3-}e^{\gamma\_{3-}(x-u\_{1})}+\frac{(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $w\_{0}<x<u\_{2}$,}\\ K\_{4-}e^{\gamma\_{4-}(x-u\_{2})}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $x>u\_{2}$,}\end{cases} |  | (7.29) |

where w0=H​(M1)w\_{0}=H(M\_{1}) and K1,K2±,K3±,K4−,u1,u2K\_{1},\,K\_{2\pm},\,K\_{3\pm},\,K\_{4-},\,u\_{1},\,u\_{2} are yet to be determined.

To ensure twice continuous differentiability at x=u1x=u\_{1}, we obtain the following equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K1​∫0u1exp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑z\displaystyle K\_{1}\int\_{0}^{u\_{1}}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz | =K2−,\displaystyle=K\_{2-}, |  | (7.30) |
|  | K1=K2+​exp⁡[∫u1w0κ1H​(y)​𝑑y]\displaystyle K\_{1}=K\_{2+}\exp\left[\int^{w\_{0}}\_{u\_{1}}\frac{\kappa\_{1}}{H(y)}dy\right] | =1−a,\displaystyle=1-a, |  |

which imply the following:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K1\displaystyle K\_{1} | =1−a,\displaystyle=1-a, |  | (7.31) |
|  | K2−\displaystyle K\_{2-} | =(1−a)​∫0u1exp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑z,\displaystyle=(1-a)\int\_{0}^{u\_{1}}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz, |  |
|  | K2+\displaystyle K\_{2+} | =(1−a)​exp⁡[−∫u1w0κ1H​(y)​𝑑y],\displaystyle=(1-a)\exp\left[-\int^{w\_{0}}\_{u\_{1}}\frac{\kappa\_{1}}{H(y)}dy\right], |  |

where u1u\_{1} is still unknown.

To ensure twice continuous differentiability at x=w0x=w\_{0}, we have the following equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | K2+\displaystyle K\_{2+} | =K3+​γ3+​eγ3+​(w0−u1)+K3−​γ3−​eγ3−​(w0−u1),\displaystyle=K\_{3+}\gamma\_{3+}e^{\gamma\_{3+}(w\_{0}-u\_{1})}+K\_{3-}\gamma\_{3-}e^{\gamma\_{3-}(w\_{0}-u\_{1})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −κ1​K2+M\displaystyle-\frac{\kappa\_{1}K\_{2+}}{M} | =K3+​γ3+2​eγ3+​(w0−u1)+K3−​γ3−2​eγ3−​(w0−u1).\displaystyle=K\_{3+}\gamma\_{3+}^{2}e^{\gamma\_{3+}(w\_{0}-u\_{1})}+K\_{3-}\gamma\_{3-}^{2}e^{\gamma\_{3-}(w\_{0}-u\_{1})}. |  |

Dividing the second equation by the first equation yields the formula for u1u\_{1} in ([4.18](https://arxiv.org/html/2511.11383v1#S4.E18 "In item 1 ‣ Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

#### Establishing the bounds for K3−K\_{3-}

We now establish the bounds for K3−K\_{3-}. Since the candidate value function gg must be positive for x>0x>0, then, from ([7.8](https://arxiv.org/html/2511.11383v1#S7.E8 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), we must have α3>0\alpha\_{3}>0, where α3\alpha\_{3} is defined in ([4.12](https://arxiv.org/html/2511.11383v1#S4.E12 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). This implies that K3−>α¯K\_{3-}>\underline{\alpha}, where α¯\underline{\alpha} is defined in ([4.8](https://arxiv.org/html/2511.11383v1#S4.E8 "In Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

Next, we establish the conditions such that the formula for u1u\_{1} in ([4.18](https://arxiv.org/html/2511.11383v1#S4.E18 "In item 1 ‣ Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is well defined. Suppose for now that K3−<0<K3+K\_{3-}<0<K\_{3+}. We then require the following result:

###### Lemma 7.16.

γ3−+κ1M1<0\gamma\_{3-}+\frac{\kappa\_{1}}{M\_{1}}<0 if and only if

|  |  |  |
| --- | --- | --- |
|  | c¯2<N1−κ1​N22​M1+δ​M1κ1andN1>κ1​N22​M1.\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}\quad\mbox{and}\quad N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}}. |  |

###### Proof.

γ3−+κ1M1<0\gamma\_{3-}+\frac{\kappa\_{1}}{M\_{1}}<0 is equivalent to

|  |  |  |
| --- | --- | --- |
|  | (N1−c¯2)2≥κ1​N2M1−(N1−c¯2).\sqrt{(N\_{1}-\overline{c}\_{2})^{2}}\geq\frac{\kappa\_{1}N\_{2}}{M\_{1}}-(N\_{1}-\overline{c}\_{2}). |  |

The inequality holds immediately if 0<c¯2<N1−κ1​N2M10<\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{M\_{1}}. Suppose that c¯2≥N1−κ1​N2M1\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{M\_{1}}. Squaring both sides of the above inequality yields the desired result.
∎

The above lemma implies that u1u\_{1} in ([4.18](https://arxiv.org/html/2511.11383v1#S4.E18 "In item 1 ‣ Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is well defined if c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. We now require that w0>u1w\_{0}>u\_{1}. It can be shown that (1−a)​(κ1M1+γ3+)γ3−​(γ3+−γ3−)=α0\frac{(1-a)\left(\frac{\kappa\_{1}}{M\_{1}}+\gamma\_{3+}\right)}{\gamma\_{3-}(\gamma\_{3+}-\gamma\_{3-})}=\alpha\_{0}. Hence, w0>u1w\_{0}>u\_{1} is equivalent to K3−≤α0K\_{3-}\leq\alpha\_{0}. This also proves that K3−<0K\_{3-}<0. Since ([4.12](https://arxiv.org/html/2511.11383v1#S4.E12 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) still holds, we have K3−≥1−aγ3−K\_{3-}\geq\frac{1-a}{\gamma\_{3-}}, or, equivalently, K3+>0K\_{3+}>0. Since c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} and N1>κ1​N22​M1N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}}, then by Lemmas [7.7](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem7 "Lemma 7.7. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance") and [7.8](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem8 "Lemma 7.8. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), we have (α¯∨1−aγ3−)<α0\left(\underline{\alpha}\vee\frac{1-a}{\gamma\_{3-}}\right)<\alpha\_{0} and the following bounds for K3−K\_{3-}:

|  |  |  |
| --- | --- | --- |
|  | 1−aγ3−<K3−<αL​B,\frac{1-a}{\gamma\_{3-}}<K\_{3-}<\alpha\_{LB}, |  |

where αL​B\alpha\_{LB} is defined in ([4.16](https://arxiv.org/html/2511.11383v1#S4.E16 "In Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

For u2u\_{2} defined in ([4.18](https://arxiv.org/html/2511.11383v1#S4.E18 "In item 1 ‣ Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), it is well defined by Lemma [7.16](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem16 "Lemma 7.16. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). The following lemma gives a necessary and sufficient condition such that u2≥w0u\_{2}\geq w\_{0}.

###### Lemma 7.17.

u2≥w0u\_{2}\geq w\_{0} if and only if

|  |  |  |
| --- | --- | --- |
|  | c¯1+c¯2≥N1−κ1​N22​M1+δ​M1κ1.\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. |  |

###### Proof.

u2≥w0u\_{2}\geq w\_{0} is equivalent to

|  |  |  |
| --- | --- | --- |
|  | (γ4−−γ3−)​(−κ1M1−γ3+)(γ3+−γ4−)​(γ3−+κ1M1)≥1.\frac{(\gamma\_{4-}-\gamma\_{3-})\left(-\frac{\kappa\_{1}}{M\_{1}}-\gamma\_{3+}\right)}{(\gamma\_{3+}-\gamma\_{4-})\left(\gamma\_{3-}+\frac{\kappa\_{1}}{M\_{1}}\right)}\geq 1. |  |

The above inequality is equivalent to γ4−+κ1M1≥0\gamma\_{4-}+\frac{\kappa\_{1}}{M\_{1}}\geq 0, which can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | −(N1−c¯1−c¯2)+κ1​N2M1≥(N1−c¯1−c¯2)2+2​δ​N2.-(N\_{1}-\overline{c}\_{1}-\overline{c}\_{2})+\frac{\kappa\_{1}N\_{2}}{M\_{1}}\geq\sqrt{(N\_{1}-\overline{c}\_{1}-\overline{c}\_{2})^{2}+2\delta N\_{2}}. |  |

A necessary condition for the above inequality to hold is c¯1+c¯2≥N1−κ1​N2M1\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{M\_{1}}. Suppose c¯1+c¯2≥N1−κ1​N2M1\overline{c}\_{1}+\overline{c}\_{2}\geq N\_{1}-\frac{\kappa\_{1}N\_{2}}{M\_{1}}. Squaring both sides of the above inequality yields the desired result.
∎

#### Solving for K3−K\_{3-}

It remains to determine K3−K\_{3-}. Suppose ψ​(αL​B)>0\psi(\alpha\_{LB})>0. By Lemma [7.14](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem14 "Lemma 7.14. ‣ Solving for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), it follows that c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}} and N1>κ1​N22​M1N\_{1}>\frac{\kappa\_{1}N\_{2}}{2M\_{1}}. Since ψ​(1−aγ3−)<0\psi\left(\frac{1-a}{\gamma\_{3-}}\right)<0, we have that K3−K\_{3-} is the unique solution of ψ​(z)=0\psi(z)=0 on (1−aγ3−,αL​B)\left(\frac{1-a}{\gamma\_{3-}},\alpha\_{LB}\right) via Lemma [7.14](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem14 "Lemma 7.14. ‣ Solving for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance").

### 7.3 Proof of Theorem [4.4](https://arxiv.org/html/2511.11383v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")

#### Proving that w0w\_{0} is infinite when M1<∞M\_{1}<\infty

Suppose c¯1+c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{1}+\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. Suppose further that w0<∞w\_{0}<\infty exists. In the region {x>w0}\{x>w\_{0}\}, we get ([7.9](https://arxiv.org/html/2511.11383v1#S7.E9 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), whose solution is given by ([7.10](https://arxiv.org/html/2511.11383v1#S7.E10 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). From ([4.5](https://arxiv.org/html/2511.11383v1#S4.E5 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and the assumption c¯1+c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{1}+\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}, we get

|  |  |  |
| --- | --- | --- |
|  | 0=−κ1​g4′​(w0)g4′′​(w0)−M1=−κ1γ4−−M1<0,0=-\kappa\_{1}\frac{g\_{4}^{\prime}(w\_{0})}{g\_{4}^{\prime\prime}(w\_{0})}-M\_{1}=-\frac{\kappa\_{1}}{\gamma\_{4-}}-M\_{1}<0, |  |

which is a contradiction. Hence, no such w0w\_{0} exists and we write w0=∞w\_{0}=\infty.

#### Deriving the analytical solution for M1<∞M\_{1}<\infty

Suppose for now that u1≤u2<w0=∞u\_{1}\leq u\_{2}<w\_{0}=\infty. In the region {x<u1}\{x<u\_{1}\}, the HJB equation becomes ([7.1](https://arxiv.org/html/2511.11383v1#S7.E1 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) whose solution that satisfies g​(0)=0g(0)=0 is given by g1​(x)=K1​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zg\_{1}(x)=K\_{1}\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz, where K1>0K\_{1}>0 is an unknown constant and G−1G^{-1} is the inverse of the function GG given by ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). In the region {u1<x<u2}\{u\_{1}<x<u\_{2}\}, the HJB equation becomes ([7.28](https://arxiv.org/html/2511.11383v1#S7.E28 "In Deriving the analytical solution ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) whose solution is given by g2​(x)=K2+​∫u1xexp⁡[∫zu2κ1H​(y)​𝑑y]​𝑑z+K2−g\_{2}(x)=K\_{2+}\int\_{u\_{1}}^{x}\exp\left[\int^{u\_{2}}\_{z}\frac{\kappa\_{1}}{H(y)}dy\right]dz+K\_{2-}, where K2±K\_{2\pm} are unknown constants and HH satisfies ([4.17](https://arxiv.org/html/2511.11383v1#S4.E17 "In item 1 ‣ Theorem 4.3. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

Since w0=∞w\_{0}=\infty, we conjecture that π1∗​(x)=M0\pi^{\*}\_{1}(x)=M\_{0} for all x≥u2x\geq u\_{2} and some unknown constant M0∈(0,M1)M\_{0}\in(0,M\_{1}). In the region {x>u2}\{x>u\_{2}\}, the HJB equation then becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=[N¯1​(M0)−c¯1−c¯2]​g′​(x)+12​N¯2​(M0)​g′′​(x)−δ​g​(x)+a​c¯1+(1−a)​c¯2,0=\left[\overline{N}\_{1}(M\_{0})-\overline{c}\_{1}-\overline{c}\_{2}\right]g^{\prime}(x)+\frac{1}{2}\overline{N}\_{2}(M\_{0})g^{\prime\prime}(x)-\delta g(x)+a\overline{c}\_{1}+(1-a)\overline{c}\_{2}, |  | (7.32) |

whose solution that satisfies limx→∞g​(x)=a​c¯1+(1−a)​c¯2δ\lim\_{x\to\infty}g(x)=\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta} is given by

|  |  |  |
| --- | --- | --- |
|  | g3​(x)=K3​eγ¯4−​(M0)​x+a​c¯1+(1−a)​c¯2δ,g\_{3}(x)=K\_{3}e^{\overline{\gamma}\_{4-}(M\_{0})x}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}, |  |

where γ¯4−​(y)\overline{\gamma}\_{4-}(y) is defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). We conjecture the following solution:

|  |  |  |
| --- | --- | --- |
|  | g​(x)={K1​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zif x<u1,K2+​∫u1xexp⁡[∫zu2κ1H​(y)​𝑑y]​𝑑z+K2−if u1<x<u2,K3​eγ¯4−​(M0)​x+a​c¯1+(1−a)​c¯2δif x>u2,g(x)=\begin{cases}K\_{1}\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<u\_{1}$,}\\ K\_{2+}\int\_{u\_{1}}^{x}\exp\left[\int^{u\_{2}}\_{z}\frac{\kappa\_{1}}{H(y)}dy\right]dz+K\_{2-}&\mbox{if $u\_{1}<x<u\_{2}$,}\\ K\_{3}e^{\overline{\gamma}\_{4-}(M\_{0})x}+\frac{a\overline{c}\_{1}+(1-a)\overline{c}\_{2}}{\delta}&\mbox{if $x>u\_{2}$,}\end{cases} |  |

where K1,K2±,K3,M0,u1,u2K\_{1},\,K\_{2\pm},\,K\_{3},\,M\_{0},\,u\_{1},\,u\_{2} are yet to be determined.

To ensure twice continuous differentiability at x=u1x=u\_{1}, we obtain the equations in ([7.30](https://arxiv.org/html/2511.11383v1#S7.E30 "In Deriving the analytical solution ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), which yield the formulas for K1K\_{1} and K2−K\_{2-} in ([7.31](https://arxiv.org/html/2511.11383v1#S7.E31 "In Deriving the analytical solution ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Moreover, we have

|  |  |  |
| --- | --- | --- |
|  | K2+=(1−a)​exp⁡[−∫u1u2κ1H​(y)​𝑑y].K\_{2+}=(1-a)\exp\left[-\int^{u\_{2}}\_{u\_{1}}\frac{\kappa\_{1}}{H(y)}dy\right]. |  |

To ensure twice continuous differentiability at x=u2x=u\_{2}, we obtain the following equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1−a)​exp⁡[∫u2u1κH​(y)​𝑑y]=K3​γ¯4−​(M0)​eγ¯4−​(M0)​u2\displaystyle(1-a)\exp\left[\int\_{u\_{2}}^{u\_{1}}\frac{\kappa}{H(y)}dy\right]=K\_{3}\overline{\gamma}\_{4-}(M\_{0})e^{\overline{\gamma}\_{4-}(M\_{0})u\_{2}} | =a,\displaystyle=a, |  | (7.33) |
|  | −(1−a)​κ1M0​exp⁡[∫u2u1κH​(y)​𝑑y]=K3​γ¯4−2​(M0)​eγ¯4−​(M0)​u2.\displaystyle-\frac{(1-a)\kappa\_{1}}{M\_{0}}\exp\left[\int\_{u\_{2}}^{u\_{1}}\frac{\kappa}{H(y)}dy\right]=K\_{3}\overline{\gamma}\_{4-}^{2}(M\_{0})e^{\overline{\gamma}\_{4-}(M\_{0})u\_{2}}. |  | |

From the first equation, we obtain

|  |  |  |
| --- | --- | --- |
|  | K3=aγ¯4−​(M0)​e−γ¯4−​(M0)​u2.K\_{3}=\frac{a}{\overline{\gamma}\_{4-}(M\_{0})}e^{-\overline{\gamma}\_{4-}(M\_{0})u\_{2}}. |  |

Dividing the second equation in ([7.33](https://arxiv.org/html/2511.11383v1#S7.E33 "In Deriving the analytical solution for 𝑀₁<∞ ‣ 7.3 Proof of Theorem 4.4 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) by the first equation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | −κ1M0=γ¯4−​(M0).-\frac{\kappa\_{1}}{M\_{0}}=\overline{\gamma}\_{4-}(M\_{0}). |  | (7.34) |

We still have to prove that M0M\_{0} exists.

###### Lemma 7.18.

Suppose c¯1+c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{1}+\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}. Then, M0M\_{0} is a solution to

|  |  |  |
| --- | --- | --- |
|  | −κ1y=γ¯4−​(y),y∈(0,M1).-\frac{\kappa\_{1}}{y}=\overline{\gamma}\_{4-}(y),\quad y\in(0,M\_{1}). |  |

###### Proof.

Since N¯1​(0)=N¯2​(0)=0\overline{N}\_{1}(0)=\overline{N}\_{2}(0)=0, we have

|  |  |  |
| --- | --- | --- |
|  | γ¯4−​(0):=limy→0γ¯4−​(y)=limy→0−2​δ−(N¯1​(y)−c¯1−c¯2)+(N¯1​(y)−c¯1−c¯2)2+2​δ​N¯2​(y)=−δc¯1+c¯2.\overline{\gamma}\_{4-}(0):=\lim\_{y\to 0}\overline{\gamma}\_{4-}(y)=\lim\_{y\to 0}\frac{-2\delta}{-(\overline{N}\_{1}(y)-\overline{c}\_{1}-\overline{c}\_{2})+\sqrt{(\overline{N}\_{1}(y)-\overline{c}\_{1}-\overline{c}\_{2})^{2}+2\delta\overline{N}\_{2}(y)}}=\frac{-\delta}{\overline{c}\_{1}+\overline{c}\_{2}}. |  |

Define f​(y):=γ¯4−​(y)+κ1yf(y):=\overline{\gamma}\_{4-}(y)+\frac{\kappa\_{1}}{y}. We have the following:

|  |  |  |
| --- | --- | --- |
|  | limy↓0f​(y)=∞andf​(M1)=γ4−+κ1M1.\lim\_{y\downarrow 0}f(y)=\infty\quad\mbox{and}\quad f(M\_{1})=\gamma\_{4-}+\frac{\kappa\_{1}}{M\_{1}}. |  |

By the intermediate value theorem, ff has a solution in (0,M1)(0,M\_{1}) if γ4−+κ1M1<0\gamma\_{4-}+\frac{\kappa\_{1}}{M\_{1}}<0. From the proof of Lemma [7.17](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem17 "Lemma 7.17. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), γ4−+κ1M1<0\gamma\_{4-}+\frac{\kappa\_{1}}{M\_{1}}<0 is equivalent to c¯1+c¯2<N1−κ1​N22​M1+δ​M1κ1\overline{c}\_{1}+\overline{c}\_{2}<N\_{1}-\frac{\kappa\_{1}N\_{2}}{2M\_{1}}+\frac{\delta M\_{1}}{\kappa\_{1}}, which proves the result.
∎

Similarly to the previous arguments, we have π1∗​(x)=H​(x)\pi\_{1}^{\*}(x)=H(x). Hence, it follows that u2u\_{2} satisfies

|  |  |  |
| --- | --- | --- |
|  | H​(u2)=M0.H(u\_{2})=M\_{0}. |  |

Finally, from the first equation in ([7.33](https://arxiv.org/html/2511.11383v1#S7.E33 "In Deriving the analytical solution for 𝑀₁<∞ ‣ 7.3 Proof of Theorem 4.4 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), u1u\_{1} satisfies ([4.20](https://arxiv.org/html/2511.11383v1#S4.E20 "In item 1 ‣ Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The following lemma proves that u1u\_{1} is the unique solution to the above equation.

###### Lemma 7.19.

u1u\_{1} is the unique solution to ([4.20](https://arxiv.org/html/2511.11383v1#S4.E20 "In item 1 ‣ Theorem 4.4. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) in (0,u2)(0,u\_{2}).

###### Proof.

Define f​(x):=−∫xu2κ1H​(y)​𝑑y−ln⁡(a1−a)f(x):=-\int\_{x}^{u\_{2}}\frac{\kappa\_{1}}{H(y)}dy-\ln\left(\frac{a}{1-a}\right). Since a≤12a\leq\frac{1}{2}, we have f​(u2)=−ln⁡(a1−a)>0f(u\_{2})=-\ln\left(\frac{a}{1-a}\right)>0. Since H​(0)=0H(0)=0, we have

|  |  |  |
| --- | --- | --- |
|  | limx→0f​(x)=−∞.\lim\_{x\to 0}f(x)=-\infty. |  |

Thus, by the intermediate value theorem, there exists a unique x0∈(0,u2)x\_{0}\in(0,u\_{2}) such that f​(x0)=0f(x\_{0})=0. Choosing x0=u1x\_{0}=u\_{1} proves the result.
∎

#### Proving that w0w\_{0} is infinite if M1=∞M\_{1}=\infty

We now consider the case where the support is unbounded (i.e., M1=∞M\_{1}=\infty). We first prove that the configurations w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2} and u1<w0≤u2u\_{1}<w\_{0}\leq u\_{2} do not hold. Suppose the configuration w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2} holds and w0w\_{0} exists. Similar to the bounded support case (i.e., M1<∞M\_{1}<\infty), we obtain the form of the candidate solution in ([7.11](https://arxiv.org/html/2511.11383v1#S7.E11 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The discussion follows with the bounded support case. However, from Lemma [7.12](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem12 "Lemma 7.12. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), we must have c¯1+c¯2≥∞\overline{c}\_{1}+\overline{c}\_{2}\geq\infty for αL​B≤αU​B\alpha\_{LB}\leq\alpha\_{UB} to hold. This implies that K3−K\_{3-} does not exist. Thus, the configuration w0≤u1≤u2w\_{0}\leq u\_{1}\leq u\_{2} is not possible.

Suppose the configuration u1<w0≤u2u\_{1}<w\_{0}\leq u\_{2} holds and w0w\_{0} exists. Similar to the bounded support case, we also obtain the form of the candidate solution in ([7.29](https://arxiv.org/html/2511.11383v1#S7.E29 "In Deriving the analytical solution ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), which leads to Lemma [7.17](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem17 "Lemma 7.17. ‣ Establishing the bounds for 𝐾_limit-from3- ‣ 7.2 Proof of Theorem 4.3 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"). The configuration will hold if and only if c¯1+c¯2≥∞\overline{c}\_{1}+\overline{c}\_{2}\geq\infty, which implies that u1<w0≤u2u\_{1}<w\_{0}\leq u\_{2} does not hold.

#### Deriving the analytical solution when M1=∞M\_{1}=\infty

Suppose now that the configuration u1≤u2<w0u\_{1}\leq u\_{2}<w\_{0} holds. The discussion follows similarly as in the bounded support case. We obtain the equation ([7.34](https://arxiv.org/html/2511.11383v1#S7.E34 "In Deriving the analytical solution for 𝑀₁<∞ ‣ 7.3 Proof of Theorem 4.4 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). The following lemma states that M0M\_{0} is indeed a solution to ([7.34](https://arxiv.org/html/2511.11383v1#S7.E34 "In Deriving the analytical solution for 𝑀₁<∞ ‣ 7.3 Proof of Theorem 4.4 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")):

###### Lemma 7.20.

M0M\_{0} is a solution to

|  |  |  |
| --- | --- | --- |
|  | −κ1y=γ¯4−​(y),y∈(0,M1).-\frac{\kappa\_{1}}{y}=\overline{\gamma}\_{4-}(y),\quad y\in(0,M\_{1}). |  |

###### Proof.

Since N¯1​(0)=N¯2​(0)=0\overline{N}\_{1}(0)=\overline{N}\_{2}(0)=0, then we have

|  |  |  |
| --- | --- | --- |
|  | γ¯4−​(0):=limy→0γ¯4−​(y)=−δc¯1+c¯2.\overline{\gamma}\_{4-}(0):=\lim\_{y\to 0}\overline{\gamma}\_{4-}(y)=\frac{-\delta}{\overline{c}\_{1}+\overline{c}\_{2}}. |  |

Define f​(y):=γ¯4−​(y)+κ1yf(y):=\overline{\gamma}\_{4-}(y)+\frac{\kappa\_{1}}{y}. We have the following:

|  |  |  |
| --- | --- | --- |
|  | limy↓0f​(y)=∞andf​(M1)=γ4−<0.\lim\_{y\downarrow 0}f(y)=\infty\quad\mbox{and}\quad f(M\_{1})=\gamma\_{4-}<0. |  |

By the intermediate value theorem, ff has a solution in (0,M1)(0,M\_{1}).
∎

### 7.4 Proof of Theorem [5.1](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")

Suppose M1<∞M\_{1}<\infty. The candidates for the optimal reinsurance strategies still satisfy ([4.4](https://arxiv.org/html/2511.11383v1#S4.E4 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). In the region {x<u1}\{x<u\_{1}\}, the HJB equation becomes ([7.1](https://arxiv.org/html/2511.11383v1#S7.E1 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), whose solution is given by g1​(x)=K1​∫0xexp⁡[∫zw0κ1G−1​(y)​𝑑y]​𝑑zg\_{1}(x)=K\_{1}\int\_{0}^{x}\exp\left[\int^{w\_{0}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz, where K1>0K\_{1}>0 is an unknown constant and G−1G^{-1} is the inverse of the function GG given by ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). We also obtain π1∗​(x)=G−1​(x)\pi\_{1}^{\*}(x)=G^{-1}(x). Since πi′​(x)>0\pi\_{i}^{\prime}(x)>0 and πi​(0)=0\pi\_{i}(0)=0, w0w\_{0} exists and satisfies w0=G​(M1)w\_{0}=G(M\_{1}).

In the region {w0<x<u1}\{w\_{0}<x<u\_{1}\}, the HJB equation becomes ([7.5](https://arxiv.org/html/2511.11383v1#S7.E5 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), whose solution is given by ([7.6](https://arxiv.org/html/2511.11383v1#S7.E6 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). In the region {x>u1}\{x>u\_{1}\}, we must have g′​(x)=1−ag^{\prime}(x)=1-a. Hence,

|  |  |  |
| --- | --- | --- |
|  | g3​(x)=(1−a)​[x−u1+K3].g\_{3}(x)=(1-a)\left[x-u\_{1}+K\_{3}\right]. |  |

We conjecture the following solution:

|  |  |  |
| --- | --- | --- |
|  | g​(x)={K1​∫0xexp⁡[∫zw0κ1G−1​(y)​𝑑y]​𝑑zif x<w0,K2+​eγ2+​(x−w0)+K2−​eγ2−​(x−w0)if w0<x<u1,(1−a)​[x−u1+K3]if x>u1,g(x)=\begin{cases}K\_{1}\int\_{0}^{x}\exp\left[\int^{w\_{0}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<w\_{0}$,}\\ K\_{2+}e^{\gamma\_{2+}(x-w\_{0})}+K\_{2-}e^{\gamma\_{2-}(x-w\_{0})}&\mbox{if $w\_{0}<x<u\_{1}$,}\\ (1-a)\left[x-u\_{1}+K\_{3}\right]&\mbox{if $x>u\_{1}$,}\end{cases} |  |

where w0=G​(M1)w\_{0}=G(M\_{1}), γ2±:=γ¯2±​(M1)\gamma\_{2\pm}:=\overline{\gamma}\_{2\pm}(M\_{1}) are defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), and K1,K2±,K3,u1K\_{1},\,K\_{2\pm},\,K\_{3},\,u\_{1} are yet to be determined.

We now solve for the unknowns using the principle of smooth fit. At x=u1x=u\_{1}, we have the following system of equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | K2+​eγ2+​u1+K2−​eγ2−​u1\displaystyle K\_{2+}e^{\gamma\_{2+}u\_{1}}+K\_{2-}e^{\gamma\_{2-}u\_{1}} | =(1−a)​K3,\displaystyle=(1-a)K\_{3}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K2+​γ2+​eγ2+​u1+K2−​γ2−​eγ2−​u1\displaystyle K\_{2+}\gamma\_{2+}e^{\gamma\_{2+}u\_{1}}+K\_{2-}\gamma\_{2-}e^{\gamma\_{2-}u\_{1}} | =1−a,\displaystyle=1-a, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | K2+​γ2+2​eγ2+​u1+K2−​γ2−2​eγ2−​u1\displaystyle K\_{2+}\gamma^{2}\_{2+}e^{\gamma\_{2+}u\_{1}}+K\_{2-}\gamma^{2}\_{2-}e^{\gamma\_{2-}u\_{1}} | =0.\displaystyle=0. |  |

From the second and third equations, we obtain

|  |  |  |
| --- | --- | --- |
|  | K2+=−γ2−​(1−a)​e−γ2+​u1γ2+​(γ2+−γ2−)>0andK2−=γ2+​(1−a)​e−γ2−​u1γ2−​(γ2+−γ2−)<0.K\_{2+}=-\frac{\gamma\_{2-}(1-a)e^{-\gamma\_{2+}u\_{1}}}{\gamma\_{2+}(\gamma\_{2+}-\gamma\_{2-})}>0\quad\mbox{and}\quad K\_{2-}=\frac{\gamma\_{2+}(1-a)e^{-\gamma\_{2-}u\_{1}}}{\gamma\_{2-}(\gamma\_{2+}-\gamma\_{2-})}<0. |  |

Substituting it into the first equation yields

|  |  |  |
| --- | --- | --- |
|  | K3=γ2++γ2−γ2+​γ2−=N1δ,K\_{3}=\frac{\gamma\_{2+}+\gamma\_{2-}}{\gamma\_{2+}\gamma\_{2-}}=\frac{N\_{1}}{\delta}, |  |

where N1:=N¯1​(M1)N\_{1}:=\overline{N}\_{1}(M\_{1}) is defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

At x=w0x=w\_{0}, it suffices to show that the derivatives are continuous. We have the following system of equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K1\displaystyle K\_{1} | =1−aγ2+−γ2−​[γ2+​eγ2−​(w0−u1)−γ2−​eγ2+​(w0−u1)],\displaystyle=\frac{1-a}{\gamma\_{2+}-\gamma\_{2-}}\left[\gamma\_{2+}e^{\gamma\_{2-}(w\_{0}-u\_{1})}-\gamma\_{2-}e^{\gamma\_{2+}(w\_{0}-u\_{1})}\right], |  | (7.35) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −κ1M1​K1\displaystyle-\frac{\kappa\_{1}}{M\_{1}}K\_{1} | =(1−a)​γ2+​γ2−γ2+−γ2−​[eγ2−​(w0−u1)−eγ2+​(w0−u1)].\displaystyle=\frac{(1-a)\gamma\_{2+}\gamma\_{2-}}{\gamma\_{2+}-\gamma\_{2-}}\left[e^{\gamma\_{2-}(w\_{0}-u\_{1})}-e^{\gamma\_{2+}(w\_{0}-u\_{1})}\right]. |  | (7.36) |

Combining the two equations yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | e(γ2+−γ2−)​(w0−u1)=γ2+​(κ1+γ2−​M1)γ2−​(κ1+γ2+​M1)=κ1γ2−+M1κ1γ2++M1.e^{(\gamma\_{2+}-\gamma\_{2-})(w\_{0}-u\_{1})}=\frac{\gamma\_{2+}(\kappa\_{1}+\gamma\_{2-}M\_{1})}{\gamma\_{2-}(\kappa\_{1}+\gamma\_{2+}M\_{1})}=\frac{\frac{\kappa\_{1}}{\gamma\_{2-}}+M\_{1}}{\frac{\kappa\_{1}}{\gamma\_{2+}}+M\_{1}}. |  | (7.37) |

Since we assume that w0≤u1w\_{0}\leq u\_{1}, it must be the case that e(γ2+−γ2−)​(w0−u1)∈(0,1)e^{(\gamma\_{2+}-\gamma\_{2-})(w\_{0}-u\_{1})}\in(0,1). Moreover, since γ2−<0\gamma\_{2-}<0, we have κ1γ2−+M1κ1γ2++M1<1\frac{\frac{\kappa\_{1}}{\gamma\_{2-}}+M\_{1}}{\frac{\kappa\_{1}}{\gamma\_{2+}}+M\_{1}}<1. From ([7.37](https://arxiv.org/html/2511.11383v1#S7.E37 "In 7.4 Proof of Theorem 5.1 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) and Lemma [7.1](https://arxiv.org/html/2511.11383v1#S7.Thmtheorem1 "Lemma 7.1. ‣ Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance"), the formula for u1u\_{1} in ([5.2](https://arxiv.org/html/2511.11383v1#S5.E2 "In item 1 ‣ Theorem 5.1. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")) is well defined. It must be noted that since γ2−​(κ1+γ2+​M1)γ2+​(κ1+γ2−​M1)>1\frac{\gamma\_{2-}(\kappa\_{1}+\gamma\_{2+}M\_{1})}{\gamma\_{2+}(\kappa\_{1}+\gamma\_{2-}M\_{1})}>1, it holds that w0≤u1w\_{0}\leq u\_{1}. Thus, we have obtained the form of the value function in ([5.3](https://arxiv.org/html/2511.11383v1#S5.E3 "In item 2 ‣ Theorem 5.1. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Similar arguments from the previous results yield that gg is increasing and concave.

### 7.5 Proof of Theorem [5.2](https://arxiv.org/html/2511.11383v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")

In this scenario, M1=∞M\_{1}=\infty. Hence, we only have one “switching” point, which is u1u\_{1} defined in ([4.3](https://arxiv.org/html/2511.11383v1#S4.E3 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).

In the region {x<u1}\{x<u\_{1}\}, we obtain the HJB equation in ([7.1](https://arxiv.org/html/2511.11383v1#S7.E1 "In Deriving the analytical solution ‣ 7.1 Proof of Theorem 4.2 ‣ 7 Proof of Main Results ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")), whose solution that satisfies g​(0)=0g(0)=0 and g′​(u1)=1−ag^{\prime}(u\_{1})=1-a is given by

|  |  |  |
| --- | --- | --- |
|  | g1​(x)=(1−a)​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑z,g\_{1}(x)=(1-a)\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz, |  |

where G−1G^{-1} is the inverse of the function GG defined in ([4.9](https://arxiv.org/html/2511.11383v1#S4.E9 "In item 1 ‣ Theorem 4.2. ‣ 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")).
In the region {x>u1}\{x>u\_{1}\}, we must have g′​(x)=1−ag^{\prime}(x)=1-a. We conjecture the following solution:

|  |  |  |
| --- | --- | --- |
|  | g​(x)={(1−a)​∫0xexp⁡[∫zu1κ1G−1​(y)​𝑑y]​𝑑zif x<u1,(1−a)​[x−u1+K3]if x>u1,g(x)=\begin{cases}(1-a)\int\_{0}^{x}\exp\left[\int^{u\_{1}}\_{z}\frac{\kappa\_{1}}{G^{-1}(y)}dy\right]dz&\mbox{if $x<u\_{1}$,}\\ (1-a)\left[x-u\_{1}+K\_{3}\right]&\mbox{if $x>u\_{1}$,}\end{cases} |  |

where K3K\_{3} and u1u\_{1} are yet to be determined.

By construction, g′​(x)g^{\prime}(x) is continuous, so we only need to make g​(x)g(x) and g′′​(x)g^{\prime\prime}(x) be continuous at the switching point u1u\_{1}. We first ensure that g′′​(x)g^{\prime\prime}(x) is continuous, that is, we want

|  |  |  |
| --- | --- | --- |
|  | −(1−a)​κ1π1​(u1−)=g′′​(u1−)=0.-\frac{(1-a)\kappa\_{1}}{\pi\_{1}(u\_{1}-)}=g^{\prime\prime}(u\_{1}-)=0. |  |

This implies that π1​(u1−)=∞\pi\_{1}(u\_{1}-)=\infty. Define

|  |  |  |
| --- | --- | --- |
|  | G​(∞):=limy→∞G​(y).G(\infty):=\lim\_{y\to\infty}G(y). |  |

We require the following result to ensure that G​(∞)G(\infty) is finite.

###### Lemma 7.21.

G​(∞)<∞G(\infty)<\infty.

###### Proof.

Since σi2​(z)→σ~i2\sigma\_{i}^{2}(z)\to\widetilde{\sigma}\_{i}^{2} and μi​(z)→μ~i\mu\_{i}(z)\to\widetilde{\mu}\_{i} as z→∞z\to\infty, the integrand of GG converges to zero at the rate of 1z2\frac{1}{z^{2}}, which proves the integrability of G​(∞)G(\infty).
∎

Since g′​(x)g^{\prime}(x) and g′′​(x)g^{\prime\prime}(x) are continuous at x=u1x=u\_{1}, then from the HJB equation, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =12​N¯2​(u1)​g′′​(u1)+[N¯1​(u1)]​g′​(u1)−δ​g​(u1)\displaystyle=\frac{1}{2}\overline{N}\_{2}(u\_{1})g^{\prime\prime}(u\_{1})+\left[\overline{N}\_{1}(u\_{1})\right]g^{\prime}(u\_{1})-\delta g(u\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[κ1​μ~1+κ2​μ~2]​(1−a)−δ​(1−a)​K3,\displaystyle=\left[\kappa\_{1}\widetilde{\mu}\_{1}+\kappa\_{2}\widetilde{\mu}\_{2}\right](1-a)-\delta(1-a)K\_{3}, |  |

where N¯1​(y)\overline{N}\_{1}(y) and N¯2​(y)\overline{N}\_{2}(y) are defined in ([4.6](https://arxiv.org/html/2511.11383v1#S4.E6 "In 4 Bounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). It implies that K3=N1δK\_{3}=\frac{N\_{1}}{\delta}, where N1=N¯1​(M1)N\_{1}=\overline{N}\_{1}(M\_{1}). Thus, we have obtained the form of the candidate value function in ([5.5](https://arxiv.org/html/2511.11383v1#S5.E5 "In item 2 ‣ Theorem 5.2. ‣ 5 Unbounded Dividend Rates ‣ Optimal Dividend, Reinsurance and Capital Injection Strategies for Collaborating Business Lines: The Case of Excess-of-Loss Reinsurance")). Similar to the previous arguments, it can be shown that gg is increasing and concave.

## 8 Conclusion

In this paper, we investigate optimal dividend payout, reinsurance, and capital injection strategies for insurers with two business lines, where reinsurance combines proportional and excess-of-loss coverage. We establish that the optimal reinsurance strategy is pure excess-of-loss and identify distinct, mutually exclusive dividend payout strategies for both bounded and unbounded dividend rates. The optimal capital injection strategy under both bounded and unbounded dividend rates is the same across all scenarios: capital transfers occur only to save one business line from ruin, provided that adequate reserves remain.

Future research could explore alternative types of dividend, such as periodic dividends and immediate dividends that incorporate transaction costs (see, e.g., kelbert2025; avanzi2020; avanzi2021). Alternative processes that model the reserve level, such as Lévy processes, could also be considered (e.g., matalopez2024). The objective function could be modified to account for penalties for early ruin (e.g., strini2023; xu2020). It would also be of interest to investigate deep learning approaches (e.g., cheng2020).