---
authors:
- Erhan Bayraktar
- Bingyan Han
- Jingjie Zhang
doc_id: arxiv:2510.21650v1
family_id: arxiv:2510.21650
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Goal-based portfolio selection with fixed transaction costs1footnote 11footnote
  1Erhan Bayraktar is partially supported by the National Science Foundation under
  grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported
  by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund
  G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858).
  Jingjie Zhang is supported by the National Natural Science Foundation of China under
  Grant No.12201113.
url_abs: http://arxiv.org/abs/2510.21650v1
url_html: https://arxiv.org/html/2510.21650v1
venue: arXiv q-fin
version: 1
year: 2025
---


Erhan Bayraktar
Department of Mathematics, University of Michigan, Ann Arbor, Email: erhan@umich.edu.
  
Bingyan Han
Thrust of Financial Technology, The Hong Kong University of Science and Technology (Guangzhou), Email: bingyanhan@hkust-gz.edu.cn.
  
Jingjie Zhang
University of International Business and Economics, Email: jingjie.zhang@uibe.edu.cn.

(October 24, 2025)

###### Abstract

We study a goal-based portfolio selection problem in which an investor aims to meet multiple financial goals, each with a specific deadline and target amount. Trading the stock incurs a strictly positive transaction cost. Using the stochastic Perron’s method, we show that the value function is the unique viscosity solution to a system of quasi-variational inequalities. The existence of an optimal trading strategy and goal funding scheme is established. Numerical results reveal complex optimal trading regions and show that the optimal investment strategy differs substantially from the V-shaped strategy observed in the frictionless case.
  
Keywords: Goal-based portfolio selection, viscosity solutions, stochastic Perron’s method, transaction costs.
  
Mathematics Subject Classification: 49L20, 91G10, 49L25, 60H30

## 1 Introduction

Portfolio selection has long been a central topic in financial research. Classical frameworks, including Merton’s utility maximization and Markowitz’s mean-variance model, are built upon several key assumptions. A critical assumption is that investors possess a precise understanding of their own risk aversion and can specify its value without ambiguity. In practice, however, retail investors often find it difficult to quantify their risk preferences. The well-known equity premium puzzle (mehra2003equity) illustrates that it is challenging to identify a reasonable risk aversion coefficient consistent with observed equity premiums and broader economic considerations. Furthermore, a single coefficient is insufficient to capture the diverse investment objectives of individual investors.

Goal-based portfolio selection has emerged as an alternative paradigm for modeling and fulfilling investors’ objectives. In this framework, an investor specifies the timing, required funding levels of financial goals and their relative importance. Compared with risk aversion, investors typically have a clearer understanding of their funding needs and the relative importance of different goals. For instance, an investor may know that purchasing a house within a certain price range before a given date is a priority, while a vacation is a less important objective.

The goal-based paradigm has been considered in both the wealth management industry and academia. Platforms such as Schwab and Betterment enable clients to specify goals including retirement plans and home down payments. gargano2024goal used data from a FinTech application to demonstrate that setting savings goals increases individual savings rates. das2010portfolio investigated separate portfolios for distinct goals and imposed different thresholds on the failure probability associated with each goal. das2022dynamic extended this framework by allowing different deadlines and capturing competition among goals, although their model assumes a finite number of states for both strategy and wealth. capponi2024 introduced a continuous-time framework for multi-goal wealth management, solved using the Hamilton-Jacobi-Bellman (HJB) equation method. bayraktar2025goal incorporated mental accounting behavior by assuming that investors construct separate portfolios for each goal, with penalties applied to fund transfers between goals.

An essential aspect of portfolio selection is the inclusion of transaction costs in stock trading. A substantial body of literature has examined investment decisions under market frictions. Proportional transaction costs were first introduced by magill1976portfolio in the context of Merton’s problem. davis1990portfolio demonstrated that the optimal strategies correspond to the local times of a two-dimensional process at the boundaries of a wedge-shaped region. shreve1994optimal relaxed several assumptions in davis1990portfolio and provided a comprehensive characterization of the value function and optimal strategies. Finite-horizon problems with proportional transaction costs have been investigated in davis1993european; dai2009finite; belak2019finite, among others. In addition to the dynamic programming and HJB equation approaches, the duality method has been widely employed to derive structural results and candidate solutions; see, for example, cvitanic1996hedging; kabanov1999hedging; deelstra2001dual; klein2007duality; Kallsen2010; Czichowsky2016AAP. Another line of research incorporates fixed transaction costs; see altarovici2017optimal; belak2019utility; belak2022optimal; bayraktar2022convergence and references therein. Notably, when transaction costs are small, asymptotic expansions can be derived using homogenization methods (soner2013homogenization; possamai2015homogenization; altarovici2015asymptotics).

A key finding in capponi2024 is the VV-shaped investment strategy, which exhibits a non-monotonic relationship between the risk profile and wealth level (see Figure [1](https://arxiv.org/html/2510.21650v1#S8.F1 "Figure 1 ‣ 8.1 The frictionless case ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") for details). This pattern often results in substantial shifts in stock holdings. Since capponi2024 assumes a frictionless market, a natural question arises as to whether the VV-shaped behavior persists when trading incurs costs. In this work, we adopt the goal-based framework of capponi2024 and consider a financial market with frictions as described in belak2022optimal. The cost structure encompasses fixed costs, fixed-plus-proportional costs, and floored or capped costs, which commonly arise in retail investment settings.

Our main contributions and findings are summarized as follows. We employ the stochastic Perron’s method to establish that the value function is the unique viscosity solution of a quasi-variational inequality (QVI) system. Early developments of the stochastic Perron’s method can be found in bayraktar2012linear; bayraktar2013stochastic; bayraktar2014Dynkin; bayraktar2015stochastic. Several essential differences distinguish our results from existing studies in capponi2024; belak2022optimal:

1. (1)

   Unlike belak2022optimal, demonstrating that the lower stochastic envelope v−v\_{-} is the unique viscosity solution to the QVI system is insufficient in our setting. This distinction stems from the specific structure of the goal-based objective functions.
2. (2)

   The expiration of goals at fixed deadlines complicates the proof of the viscosity solution properties. Further details are provided in Lemmas [A.3](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") and [B.2](https://arxiv.org/html/2510.21650v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
3. (3)

   The construction of a strict classical subsolution in Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") is more delicate, with the difficulty again stemming from the goal-based objectives.

Despite these challenges, one advantage of strictly positive costs is that the existence of an optimal strategy requires only continuity, rather than smoothness, of the value function, similar to the setting in belak2022optimal. This property allows for an explicit construction of an optimal strategy, which is presented in Section [7](https://arxiv.org/html/2510.21650v1#S7 "7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

In the numerical study, we focus on fixed transaction costs and summarize the main findings as follows:

1. (1)

   The investor must consider both stock and bank account holdings, rather than total wealth alone, when determining the optimal stock exposure. The continuation regions exhibit complex geometries and lack symmetry with respect to the target positions. In particular, a straight continuation region arises when the wealth level is close to the amounts required for both goals, as discussed in Section [8.3](https://arxiv.org/html/2510.21650v1#S8.SS3 "8.3 The straight continuation region near 𝐺₁+𝐺₂+𝐶ₘᵢₙ ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
2. (2)

   The optimal strategy in our setting may still allocate the entire wealth to the stock when the total wealth is close to the amount required by the first goal, as shown in Figure [5](https://arxiv.org/html/2510.21650v1#S8.F5 "Figure 5 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). This behavior contrasts with the VV-shaped strategy observed in the frictionless case.
3. (3)

   Within the continuation region, since no transfer occurs, the optimal funding ratio of the first goal is determined based on the bank account. Figure [8](https://arxiv.org/html/2510.21650v1#S8.F8 "Figure 8 ‣ 8.2.3 Time 𝑡=1.0: Funding ratios and importance weights ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that, under fixed costs, the optimal funding ratios exhibit greater variability for a given level of total wealth.

In contrast to the present paper, bayraktar2025goal study a frictionless financial market and introduce penalties for fund transfers between goals. The proof of the viscosity solution property in bayraktar2025goal differs substantially in handling goal deadlines and establishing the comparison principle. Furthermore, the incorporation of mental costs in bayraktar2025goal results in optimal trading regions that differ from those derived in the current study.

The remainder of this paper is structured as follows. Section [2](https://arxiv.org/html/2510.21650v1#S2 "2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") introduces the problem formulation and the financial market. Section [3](https://arxiv.org/html/2510.21650v1#S3 "3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") derives the QVI system and presents the first main result, Theorem [3.4](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), which establishes the viscosity solution property of the value function. Sections [4](https://arxiv.org/html/2510.21650v1#S4 "4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), [5](https://arxiv.org/html/2510.21650v1#S5 "5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), and [6](https://arxiv.org/html/2510.21650v1#S6 "6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") contain the proof of Theorem [3.4](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Section [7](https://arxiv.org/html/2510.21650v1#S7 "7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") constructs the optimal strategy, and Section [8](https://arxiv.org/html/2510.21650v1#S8 "8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") reports the numerical results. All technical proofs are provided in the Appendix.

## 2 Formulation

Assume that an investor has KK goals. Each goal k∈{1,…,K}k\in\{1,\ldots,K\} requires a target amount GkG\_{k} by a predetermined deadline TkT\_{k}. For simplicity, assume that the deadlines are distinct and ordered as T1<…<Tk<…<TKT\_{1}<\ldots<T\_{k}<\ldots<T\_{K}. For convenience, let T0:=0T\_{0}:=0 and T:=TKT:=T\_{K}. The investment problem therefore spans the time horizon [0,T][0,T]. The investor constructs a single portfolio to meet each target GkG\_{k}.

Following the financial market framework in belak2022optimal, we restate the setting here for completeness. Let (Ω,ℱ,ℙ)(\Omega,{\mathcal{F}},\mathbb{P}) be a probability space supporting a one-dimensional Brownian motion W:={W​(t):t∈[0,T]}W:=\{W(t):t\in[0,T]\}. The filtration 𝔽:={ℱt:t∈[0,T]}\mathbb{F}:=\{{\mathcal{F}}\_{t}:t\in[0,T]\} denotes the completion of the natural filtration generated by WW and satisfies the usual conditions. The financial market consists of a risk-free asset and a single risky asset (stock). Denote by rr the constant risk-free interest rate. The stock price process {S​(u):u∈[t,T]}\{S(u):u\in[t,T]\} evolves according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(u)=S​(u)​[μ​d​u+σ​d​W​(u)],dS(u)=S(u)[\mu du+\sigma dW(u)], |  | (2.1) |

where μ∈ℝ\mu\in\mathbb{R} is the constant drift and σ>0\sigma>0 is the constant volatility.

Following belak2022optimal, a trading volume Δ\Delta in the stock is assumed to incur a strictly positive transaction cost denoted by C​(Δ)C(\Delta). Suppose the transaction cost function C​(⋅)C(\cdot) satisfies the following conditions:

1. (1)

   The function C​(Δ)C(\Delta) is continuous and the mapping |Δ|↦C​(|Δ|)|\Delta|\mapsto C(|\Delta|) is increasing, implying that transaction costs rise with trading volume. The minimum cost is attained at Δ=0\Delta=0, with Cmin:=C​(0)>0C\_{\min}:=C(0)>0.
2. (2)

   Suppose the mapping

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Δ↦Δ+C​(Δ)\Delta\mapsto\Delta+C(\Delta) |  | (2.2) |

   is strictly increasing on ℝ\mathbb{R}, and its range contains [0,∞)[0,\infty).
3. (3)

   Transactions of size zero (Δ=0)(\Delta=0) are permitted but still incur a positive cost Cmin>0C\_{\min}>0. This assumption is made for analytical convenience, as it guarantees the compactness of the feasible set of transactions.

Typical examples of C​(Δ)C(\Delta) include fixed costs, fixed-plus-proportional costs, and other specifications discussed in belak2022optimal.

We now introduce the regions representing portfolio positions. Let x0x\_{0} and x1x\_{1} denote the dollar amounts invested in the money market and the stock, respectively. The two-dimensional variable x:=(x0,x1)∈ℝ2x:=(x\_{0},x\_{1})\in\mathbb{R}^{2} represents the investor’s portfolio position. Throughout this paper, short selling is not permitted in either the money market or the stock. The corresponding set of admissible portfolio positions is denoted by 𝒮¯:=[0,∞)2\overline{\mathcal{S}}:=[0,\infty)^{2}. For later use, define 𝒮:=[0,∞)2\{(0,0)}{\mathcal{S}}:=[0,\infty)^{2}\backslash\{(0,0)\}, which excludes the corner point (0,0)(0,0).

Following a transaction of size Δ∈ℝ\Delta\in\mathbb{R}, the portfolio x=(x0,x1)x=(x\_{0},x\_{1}) is updated according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | (x0−Δ−C(Δ),x1+Δ)=:Γ(x,Δ),(x\_{0}-\Delta-C(\Delta),x\_{1}+\Delta)=:\Gamma(x,\Delta), |  | (2.3) |

where Γ​(x,Δ)\Gamma(x,\Delta) is referred to as the rebalancing function in belak2022optimal.

Given a portfolio position x∈𝒮¯x\in\overline{\mathcal{S}}, a transaction Δ\Delta is called feasible if it does not result in short positions in either asset. The set of all feasible transactions is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(x):={Δ∈ℝ:Γ​(x,Δ)∈𝒮¯}.D(x):=\{\Delta\in\mathbb{R}:\Gamma(x,\Delta)\in\overline{\mathcal{S}}\}. |  | (2.4) |

Following belak2022optimal, the feasible set D​(x)D(x) can be simplified. Recall that the mapping Δ↦Δ+C​(Δ)\Delta\mapsto\Delta+C(\Delta) is strictly increasing, and its range covers [0,∞)[0,\infty). Consequently, there exists a continuous and strictly increasing inverse function χ:[0,∞)→ℝ\chi:[0,\infty)\rightarrow\mathbb{R}. The rebalancing position Γ​(x,Δ)\Gamma(x,\Delta) belongs to 𝒮¯\overline{\mathcal{S}} if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | x0−Δ−C​(Δ)≥0andx1+Δ≥0.x\_{0}-\Delta-C(\Delta)\geq 0\quad\text{and}\quad x\_{1}+\Delta\geq 0. |  | (2.5) |

This condition is equivalent to χ​(x0)≥Δ\chi(x\_{0})\geq\Delta and Δ≥−x1\Delta\geq-x\_{1}. Hence, the set of feasible transactions can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(x)=[−x1,χ​(x0)],x∈𝒮¯.D(x)=[-x\_{1},\chi(x\_{0})],\quad x\in\overline{\mathcal{S}}. |  | (2.6) |

When χ​(x0)<−x1\chi(x\_{0})<-x\_{1}, no feasible transaction exists. The set of portfolio positions without feasible transactions is denoted by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮∅:={x∈𝒮¯:χ​(x0)<−x1}.{\mathcal{S}}\_{\emptyset}:=\{x\in\overline{\mathcal{S}}:\chi(x\_{0})<-x\_{1}\}. |  | (2.7) |

The representation ([2.6](https://arxiv.org/html/2510.21650v1#S2.E6 "In 2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) implies that D​(x)≠∅D(x)\neq\emptyset if and only if −x1∈D​(x)-x\_{1}\in D(x), which is equivalent to x0+x1≥C​(−x1)x\_{0}+x\_{1}\geq C(-x\_{1}); in other words, there is sufficient budget to liquidate the stock position. As noted by belak2022optimal, this yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮∅={x∈𝒮¯:x0+x1<C​(−x1)}⊇{x∈𝒮¯:x0+x1<Cmin}.{\mathcal{S}}\_{\emptyset}=\{x\in\overline{\mathcal{S}}:x\_{0}+x\_{1}<C(-x\_{1})\}\supseteq\{x\in\overline{\mathcal{S}}:x\_{0}+x\_{1}<C\_{\min}\}. |  | (2.8) |

Therefore, 𝒮∅{\mathcal{S}}\_{\emptyset} is open relative to 𝒮¯\overline{\mathcal{S}}. The 𝒮¯\overline{\mathcal{S}}-relative boundary of 𝒮∅{\mathcal{S}}\_{\emptyset} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝒮∅={x∈𝒮¯:x0+x1=C​(−x1)}.\partial{\mathcal{S}}\_{\emptyset}=\{x\in\overline{\mathcal{S}}:x\_{0}+x\_{1}=C(-x\_{1})\}. |  | (2.9) |

The closure of 𝒮∅{\mathcal{S}}\_{\emptyset} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮∅¯={x∈𝒮¯:x0+x1≤C​(−x1)}.\overline{{\mathcal{S}}\_{\emptyset}}=\{x\in\overline{\mathcal{S}}:x\_{0}+x\_{1}\leq C(-x\_{1})\}. |  | (2.10) |

When transaction costs are bounded below by a strictly positive constant, the investor can only trade discretely, as continuous trading would lead to immediate bankruptcy. An investment strategy is represented by a sequence Λ:={(τn,Δn)}n=1∞\Lambda:=\{(\tau\_{n},\Delta\_{n})\}^{\infty}\_{n=1}, where {τn}n=1∞\{\tau\_{n}\}^{\infty}\_{n=1} is an increasing sequence of 𝔽\mathbb{F}-stopping times representing trading times, and Δn\Delta\_{n} is an ℱτn{\mathcal{F}}\_{\tau\_{n}}-measurable random variable denoting the volume of the nn-th trade. In addition to the investment strategy, the investor also needs to determine the dollar amounts allocated to each goal. Let θk≥0\theta\_{k}\geq 0 denote the ℱTk{\mathcal{F}}\_{T\_{k}}-measurable random variable representing the amount withdrawn from the money account to finance goal kk.

Starting at time 0 with an initial portfolio position x=(x0,x1)∈𝒮¯x=(x\_{0},x\_{1})\in\overline{\mathcal{S}}, the portfolio dynamics (X0​(s),X1​(s))s∈[0,T](X\_{0}(s),X\_{1}(s))\_{s\in[0,T]} are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X0​(s)\displaystyle X\_{0}(s) | =x0+∫0sr​X0​(u)​𝑑u−∑n=1∞[Δn+C​(Δn)]​𝟏{τn≤s}−∑l=1Kθl​𝟏{Tl≤s},\displaystyle=x\_{0}+\int^{s}\_{0}rX\_{0}(u)du-\sum^{\infty}\_{n=1}[\Delta\_{n}+C(\Delta\_{n})]\mathbf{1}\_{\{\tau\_{n}\leq s\}}-\sum^{K}\_{l=1}\theta\_{l}\mathbf{1}\_{\{T\_{l}\leq s\}}, |  | (2.11) |
|  | X1​(s)\displaystyle X\_{1}(s) | =x1+∫0sμ​X1​(u)​𝑑u+∫0sσ​X1​(u)​𝑑W​(u)+∑n=1∞Δn​𝟏{τn≤s},s∈[0,T].\displaystyle=x\_{1}+\int^{s}\_{0}\mu X\_{1}(u)du+\int^{s}\_{0}\sigma X\_{1}(u)dW(u)+\sum^{\infty}\_{n=1}\Delta\_{n}\mathbf{1}\_{\{\tau\_{n}\leq s\}},\quad s\in[0,T]. |  |

For notational simplicity, let X​(s):=(X0​(s),X1​(s))X(s):=(X\_{0}(s),X\_{1}(s)). Since trading at time 0 is allowed, the initial condition is interpreted as X​(0−)=xX(0-)=x.

In the general case where the initial time is t∈[0,T]t\in[0,T] and X​(t−)=xX(t-)=x, the dynamics are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X0​(s)\displaystyle X\_{0}(s) | =x0+∫tsr​X0​(u)​𝑑u−∑n=1∞[Δn+C​(Δn)]​𝟏{t≤τn≤s}−∑l=1Kθl​𝟏{t≤Tl≤s},\displaystyle=x\_{0}+\int^{s}\_{t}rX\_{0}(u)du-\sum^{\infty}\_{n=1}[\Delta\_{n}+C(\Delta\_{n})]\mathbf{1}\_{\{t\leq\tau\_{n}\leq s\}}-\sum^{K}\_{l=1}\theta\_{l}\mathbf{1}\_{\{t\leq T\_{l}\leq s\}}, |  | (2.12) |
|  | X1​(s)\displaystyle X\_{1}(s) | =x1+∫tsμ​X1​(u)​𝑑u+∫tsσ​X1​(u)​𝑑W​(u)+∑n=1∞Δn​𝟏{t≤τn≤s},s∈[t,T].\displaystyle=x\_{1}+\int^{s}\_{t}\mu X\_{1}(u)du+\int^{s}\_{t}\sigma X\_{1}(u)dW(u)+\sum^{\infty}\_{n=1}\Delta\_{n}\mathbf{1}\_{\{t\leq\tau\_{n}\leq s\}},\quad s\in[t,T]. |  |

In particular, at each goal deadline TkT\_{k} for k=1,…,Kk=1,\ldots,K, the portfolio dynamics satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X0​(Tk)\displaystyle X\_{0}(T\_{k}) | =X0​(Tk−)−∑n=1∞[Δn+C​(Δn)]​𝟏{τn=Tk}−θk,\displaystyle=X\_{0}(T\_{k}-)-\sum^{\infty}\_{n=1}[\Delta\_{n}+C(\Delta\_{n})]\mathbf{1}\_{\{\tau\_{n}=T\_{k}\}}-\theta\_{k}, |  | (2.13) |
|  | X1​(Tk)\displaystyle X\_{1}(T\_{k}) | =X1​(Tk−)+∑n=1∞Δn​𝟏{τn=Tk}.\displaystyle=X\_{1}(T\_{k}-)+\sum^{\infty}\_{n=1}\Delta\_{n}\mathbf{1}\_{\{\tau\_{n}=T\_{k}\}}. |  |

The wealth processes jump due to the withdrawal θk\theta\_{k} and transfers between the money account and the stock. Depending on the cost structure, executing several smaller trades may be less costly than making a single large trade.

For the final goal KK, it is assumed that the investor liquidates her stock position whenever doing so does not incur a net loss. The liquidation value of a portfolio x∈𝒮¯x\in\overline{\mathcal{S}} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(x):=x0+(x1−C​(−x1))+.L(x):=x\_{0}+(x\_{1}-C(-x\_{1}))^{+}. |  | (2.14) |

Accordingly, the investor is assumed to meet the last goal using the liquidation value.

###### Definition 2.1 (Admissible strategies).

Consider the initial time t∈[Tk−1,Tk]t\in[T\_{k-1},T\_{k}] for some k=1,…,Kk=1,\ldots,K and the initial portfolio position x=(x0,x1)∈𝒮¯x=(x\_{0},x\_{1})\in\overline{\mathcal{S}}. A trading strategy consists of the withdrawal sequence θk:K={θl}l=kK\theta\_{k:K}=\{\theta\_{l}\}^{K}\_{l=k}, where θK\theta\_{K} equals to the liquidation value, and the investment strategy Λ={(τn,Δn)}n=1∞\Lambda=\{(\tau\_{n},\Delta\_{n})\}^{\infty}\_{n=1} with τ1≥t\tau\_{1}\geq t. The strategy is called admissible if it does not involve short positions in either the money account or the stock. The set of admissible strategies is denoted by 𝒜​(t,x;k)\mathcal{A}(t,x;k).

In Definition [2.1](https://arxiv.org/html/2510.21650v1#S2.Thmtheorem1 "Definition 2.1 (Admissible strategies). ‣ 2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), when k≤K−1k\leq K-1, the set 𝒜​(Tk,x;k)\mathcal{A}(T\_{k},x;k) corresponds to the problem immediately before the expiration of goal kk and therefore includes θk\theta\_{k}. In contrast, 𝒜​(Tk,x;k+1)\mathcal{A}(T\_{k},x;k+1) only contains θk+1:K\theta\_{k+1:K} and applies to the problem immediately after the expiration of goal kk. This distinction is crucial for defining the value functions.

For each k=1,…,Kk=1,\ldots,K, a pair (τ¯,ξ)(\bar{\tau},\xi) is called a random initial condition for the portfolio process ([2.12](https://arxiv.org/html/2510.21650v1#S2.E12 "In 2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) if τ¯∈[Tk−1,T]\bar{\tau}\in[T\_{k-1},T] is an 𝔽\mathbb{F}-stopping time and ξ\xi is an ℱτ¯{\mathcal{F}}\_{\bar{\tau}}-measurable random variable satisfying ℙ​(ξ∈𝒮¯)=1\mathbb{P}(\xi\in\overline{\mathcal{S}})=1. For an admissible strategy (θk:K,Λ):=(θk:K,{(τn,Δn)}n=1∞)(\theta\_{k:K},\Lambda):=(\theta\_{k:K},\{(\tau\_{n},\Delta\_{n})\}^{\infty}\_{n=1}) with τ1≥τ¯\tau\_{1}\geq\bar{\tau}, let {X​(t;τ¯,ξ,θk:K,Λ)}t∈[τ¯,T]\{X(t;\bar{\tau},\xi,\theta\_{k:K},\Lambda)\}\_{t\in[\bar{\tau},T]} denote the solution of the portfolio process ([2.12](https://arxiv.org/html/2510.21650v1#S2.E12 "In 2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")). The random initial condition (τ¯,ξ)(\bar{\tau},\xi) is said to be satisfied if

|  |  |  |
| --- | --- | --- |
|  | X​(τ¯−;τ¯,ξ,θk:K,Λ)=ξ.X(\bar{\tau}-;\bar{\tau},\xi,\theta\_{k:K},\Lambda)=\xi. |  |

The strategy (θk:K,Λ)(\theta\_{k:K},\Lambda) is called (τ¯,ξ)(\bar{\tau},\xi)-admissible if

|  |  |  |
| --- | --- | --- |
|  | ℙ​(X​(t;τ¯,ξ,θk:K,Λ)∈𝒮¯,τ¯≤t≤T)=1.\mathbb{P}(X(t;\bar{\tau},\xi,\theta\_{k:K},\Lambda)\in\overline{\mathcal{S}},\;\bar{\tau}\leq t\leq T)=1. |  |

When there is no transfer between the money account and the stock, and only withdrawals θk:K\theta\_{k:K} are permitted, denote by {X​(t;τ¯,ξ,θk:K,∅)}t∈[τ¯,T]\{X(t;\bar{\tau},\xi,\theta\_{k:K},\emptyset)\}\_{t\in[\bar{\tau},T]} the corresponding solution of the portfolio process ([2.12](https://arxiv.org/html/2510.21650v1#S2.E12 "In 2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")). For later reference, we consider the solution on the interval [τ¯,Tk][\bar{\tau},T\_{k}] with τ¯≤Tk\bar{\tau}\leq T\_{k}. Denote by {X​(t;τ¯,ξ,∅,Λ)}t∈[τ¯,Tk]\{X(t;\bar{\tau},\xi,\emptyset,\Lambda)\}\_{t\in[\bar{\tau},T\_{k}]} the solution when the withdrawal θk\theta\_{k} has not yet been determined. Similarly, the process {X​(t;τ¯,ξ,∅,∅)}t∈[τ¯,Tk]\{X(t;\bar{\tau},\xi,\emptyset,\emptyset)\}\_{t\in[\bar{\tau},T\_{k}]} represents the uncontrolled state process.

For clarity, we distinguish between processes initialized at time TkT\_{k}. In the process {X(t;Tk,x\{X(t;T\_{k},x, θk:K,Λ)}t∈[Tk,T]\theta\_{k:K},\Lambda)\}\_{t\in[T\_{k},T]}, the control variable θk\theta\_{k} remains active, and the initial position xx represents the state before the withdrawal of θk\theta\_{k}. In contrast, in the process {X​(t;Tk,x,θk+1:K,Λ)}t∈[Tk,T]\{X(t;T\_{k},x,\theta\_{k+1:K},\Lambda)\}\_{t\in[T\_{k},T]}, the initial position xx corresponds to the state after the withdrawal of θk\theta\_{k}. Other analogous notations with TkT\_{k} as the initial time are interpreted in the same manner.

Under the admissibility and no-arbitrage conditions, belak2019utility shows that the investor trades only finitely many times almost surely within a finite time interval. Moment estimates for X​(⋅;t,x,θk:K,Λ)X(\cdot;t,x,\theta\_{k:K},\Lambda) can be obtained similarly to belak2022optimal.

The investor seeks to minimize the shortfalls between the target levels GkG\_{k} and the funding amounts θk\theta\_{k}, weighted by the importance parameters wk>0w\_{k}>0:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | inf(θ1:K,Λ)∈𝒜​(0,x;1)𝔼[\displaystyle\inf\_{(\theta\_{1:K},\Lambda)\in\mathcal{A}(0,x;1)}\mathbb{E}\Big[ | ∑k=1Kwk(Gk−θk)+].\displaystyle\sum^{K}\_{k=1}w\_{k}(G\_{k}-\theta\_{k})^{+}\Big]. |  | (2.15) |

As a benchmark, the weight for goal 11 is set as w1=1.0w\_{1}=1.0. To avoid trivial cases, we assume wk>0w\_{k}>0 and Gk>0G\_{k}>0 for all k=1,…,Kk=1,\ldots,K.

For time t∈[Tk−1,Tk]t\in[T\_{k-1},T\_{k}] with k=1,…,Kk=1,\ldots,K, the value function is defined as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vk(t,x):=inf(θk:K,Λ)∈𝒜​(t,x;k)𝔼[\displaystyle V\_{k}(t,x)=\inf\_{(\theta\_{k:K},\Lambda)\in\mathcal{A}(t,x;k)}\mathbb{E}\Big[ | ∑i=kKwi(Gi−θi)+|X(t−;t,x,θk:K,Λ)=x].\displaystyle\sum^{K}\_{i=k}w\_{i}(G\_{i}-\theta\_{i})^{+}\Big|X(t-;t,x,\theta\_{k:K},\Lambda)=x\Big]. |  | (2.16) |

The value function Vk​(t,x)V\_{k}(t,x) applies when the goals k,…,Kk,\ldots,K are active. At the deadline TkT\_{k} with k≤K−1k\leq K-1, both Vk​(Tk,x)V\_{k}(T\_{k},x) and Vk+1​(Tk,x)V\_{k+1}(T\_{k},x) are defined, representing the optimal objective values immediately before and after the deadline TkT\_{k}, respectively. Specifically, Vk​(Tk,x)V\_{k}(T\_{k},x) optimizes over (θk:K,Λ)∈𝒜​(Tk,x;k)(\theta\_{k:K},\Lambda)\in\mathcal{A}(T\_{k},x;k), while Vk+1​(Tk,x)V\_{k+1}(T\_{k},x) optimizes over (θk+1:K,Λ)∈𝒜​(Tk,x;k+1)(\theta\_{k+1:K},\Lambda)\in\mathcal{A}(T\_{k},x;k+1).

## 3 The QVI system

In contrast to capponi2024, we define the value function as an array of ([2.16](https://arxiv.org/html/2510.21650v1#S2.E16 "In 2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({V1​(t,x)}t∈[0,T1],…,{Vk​(t,x)}t∈[Tk−1,Tk],…,{VK​(t,x)}t∈[TK−1,T]),(\{V\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{V\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{V\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}), |  | (3.1) |

which facilitates the analysis of terminal conditions at TkT\_{k}, k=1,…,K−1k=1,\ldots,K-1. Under the framework of capponi2024, our Vk​(Tk,x)V\_{k}(T\_{k},x) corresponds to V​(Tk−,x)V(T\_{k}-,x) in their notation.

To introduce the QVI system, we define the infinitesimal generator as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​[Vk]​(t,x):=−∂Vk∂t−r​x0​∂Vk∂x0−μ​x1​∂Vk∂x1−12​σ2​x12​∂2Vk∂x12.{\mathcal{L}}[V\_{k}](t,x):=-\frac{\partial V\_{k}}{\partial t}-rx\_{0}\frac{\partial V\_{k}}{\partial x\_{0}}-\mu x\_{1}\frac{\partial V\_{k}}{\partial x\_{1}}-\frac{1}{2}\sigma^{2}x^{2}\_{1}\frac{\partial^{2}V\_{k}}{\partial x^{2}\_{1}}. |  | (3.2) |

For a locally bounded function Vk​(t,x)V\_{k}(t,x), the intervention operator is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​[Vk]​(t,x)={infΔ∈D​(x)Vk​(t,Γ​(x,Δ)), if ​D​(x)≠∅,+∞, if ​D​(x)=∅.\displaystyle{\mathcal{M}}[V\_{k}](t,x)=\left\{\begin{array}[]{rcl}&\inf\_{\Delta\in D(x)}V\_{k}(t,\Gamma(x,\Delta)),&\text{ if }D(x)\neq\emptyset,\\ &+\infty,&\text{ if }D(x)=\emptyset.\end{array}\right. |  | (3.5) |

Through a heuristic derivation, the QVI system is given as follows:

1. (1)

   For time t∈[Tk−1,Tk)t\in[T\_{k-1},T\_{k}) with k=1,…,Kk=1,\ldots,K, the goals k,…,Kk,\ldots,K are active. The corresponding QVI is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | max⁡{ℒ​[Vk]​(t,x),Vk​(t,x)−ℳ​[Vk]​(t,x)}=0,(t,x)∈[Tk−1,Tk)×𝒮.\max\Big\{{\mathcal{L}}[V\_{k}](t,x),V\_{k}(t,x)-{\mathcal{M}}[V\_{k}](t,x)\Big\}=0,\quad(t,x)\in[T\_{k-1},T\_{k})\times{\mathcal{S}}. |  | (3.6) |
2. (2)

   At time TkT\_{k} with k=1,…,K−1k=1,\ldots,K-1, the boundary condition connecting Vk​(Tk,x)V\_{k}(T\_{k},x) and Vk+1​(Tk,x)V\_{k+1}(T\_{k},x) is

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | Vk​(Tk,x)−inf0≤θk≤x0[wk​(Gk−θk)++Vk+1​(Tk,x0−θk,x1)],\displaystyle V\_{k}(T\_{k},x)-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+V\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right], |  | (3.7) |
   |  |  | Vk(Tk,x)−ℳ[Vk](Tk,x)}=0,x∈𝒮.\displaystyle V\_{k}(T\_{k},x)-{\mathcal{M}}[V\_{k}](T\_{k},x)\Big\}=0,\quad x\in{\mathcal{S}}. |  |
3. (3)

   At time TKT\_{K}, the terminal condition is

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | VK​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+,\displaystyle V\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  | (3.8) |
   |  |  | VK(TK,x)−ℳ[VK](TK,x)}=0,x∈𝒮.\displaystyle V\_{K}(T\_{K},x)-{\mathcal{M}}[V\_{K}](T\_{K},x)\Big\}=0,\quad x\in{\mathcal{S}}. |  |
4. (4)

   At the portfolio position x=(0,0)x=(0,0), the boundary condition is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Vk​(t,0)=∑i=kKwi​Gi,t∈[Tk−1,Tk],k=1,…,K.V\_{k}(t,0)=\sum^{K}\_{i=k}w\_{i}G\_{i},\quad t\in[T\_{k-1},T\_{k}],\quad k=1,\ldots,K. |  | (3.9) |

Since this is the only QVI system considered in the paper, we refer to it simply as the QVI system.

The first main result of this paper characterizes the value function defined in ([3.1](https://arxiv.org/html/2510.21650v1#S3.E1 "In 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) with ([2.16](https://arxiv.org/html/2510.21650v1#S2.E16 "In 2 Formulation ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) as the unique viscosity solution of the QVI system. We adopt standard notation from the theory of viscosity solutions. For a locally bounded function vkv\_{k}, denote vk∗v^{\*}\_{k} as its upper semicontinuous (USC) envelope and vk,∗v\_{k,\*} as its lower semicontinuous (LSC) envelope. See crandall1992user for the precise definition.

###### Definition 3.1 (Viscosity subsolution).

Consider an array of functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({v1​(t,x)}t∈[0,T1],…,{vk​(t,x)}t∈[Tk−1,Tk],…,{vK​(t,x)}t∈[TK−1,T]),(\{v\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{v\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{v\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}), |  | (3.10) |

where vk​(t,x):[Tk−1,Tk]×𝒮¯→ℝv\_{k}(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is locally bounded for each k=1,…,Kk=1,\ldots,K. The array ([3.10](https://arxiv.org/html/2510.21650v1#S3.E10 "In Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is a viscosity subsolution of the QVI system if the following conditions hold:

1. (1)

   For each k=1,…,Kk=1,\ldots,K,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | max⁡{ℒ​[φ]​(t¯,x¯),vk∗​(t¯,x¯)−ℳ​[vk∗]∗​(t¯,x¯)}≤0,\max\Big\{{\mathcal{L}}[\varphi](\bar{t},\bar{x}),v^{\*}\_{k}(\bar{t},\bar{x})-{\mathcal{M}}[v^{\*}\_{k}]^{\*}(\bar{t},\bar{x})\Big\}\leq 0, |  | (3.11) |

   for all (t¯,x¯)∈[Tk−1,Tk)×𝒮(\bar{t},\bar{x})\in[T\_{k-1},T\_{k})\times{\mathcal{S}} and for all φ∈C1,2​([Tk−1,Tk)×𝒮)\varphi\in C^{1,2}([T\_{k-1},T\_{k})\times{\mathcal{S}}) such that (t¯,x¯)(\bar{t},\bar{x}) is a maximum point of vk∗−φv^{\*}\_{k}-\varphi.
2. (2)

   For each TkT\_{k} with k=1,…,K−1k=1,\ldots,K-1,

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | vk∗​(Tk,x)−inf0≤θk≤x0[wk​(Gk−θk)++vk+1∗​(Tk,x0−θk,x1)],\displaystyle v^{\*}\_{k}(T\_{k},x)-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v^{\*}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right], |  | (3.12) |
   |  |  | vk∗(Tk,x)−ℳ[vk∗]∗(Tk,x)}≤0,\displaystyle v^{\*}\_{k}(T\_{k},x)-{\mathcal{M}}[v^{\*}\_{k}]^{\*}(T\_{k},x)\Big\}\leq 0, |  |

   for all x∈𝒮x\in{\mathcal{S}}.
3. (3)

   At the terminal time TKT\_{K},

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | vK∗​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+,\displaystyle v^{\*}\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  | (3.13) |
   |  |  | vK∗(TK,x)−ℳ[vK∗]∗(TK,x)}≤0,\displaystyle v^{\*}\_{K}(T\_{K},x)-{\mathcal{M}}[v^{\*}\_{K}]^{\*}(T\_{K},x)\Big\}\leq 0, |  |

   for all x∈𝒮x\in{\mathcal{S}}.
4. (4)

   At the boundary x=(0,0)x=(0,0),

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk∗​(t,0)≤∑i=kKwi​Gi,t∈[Tk−1,Tk],k=1,…,K.v^{\*}\_{k}(t,0)\leq\sum^{K}\_{i=k}w\_{i}G\_{i},\quad t\in[T\_{k-1},T\_{k}],\quad k=1,\ldots,K. |  | (3.14) |

###### Definition 3.2 (Viscosity supersolution).

Consider an array of functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({v1​(t,x)}t∈[0,T1],…,{vk​(t,x)}t∈[Tk−1,Tk],…,{vK​(t,x)}t∈[TK−1,T]),(\{v\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{v\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{v\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}), |  | (3.15) |

where vk​(t,x):[Tk−1,Tk]×𝒮¯→ℝv\_{k}(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is locally bounded for each k=1,…,Kk=1,\ldots,K. The array ([3.15](https://arxiv.org/html/2510.21650v1#S3.E15 "In Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is a viscosity supersolution of the QVI system if the following conditions hold:

1. (1)

   For each k=1,…,Kk=1,\ldots,K,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | max⁡{ℒ​[φ]​(t¯,x¯),vk,∗​(t¯,x¯)−ℳ​[vk,∗]∗​(t¯,x¯)}≥0,\displaystyle\max\Big\{{\mathcal{L}}[\varphi](\bar{t},\bar{x}),v\_{k,\*}(\bar{t},\bar{x})-{\mathcal{M}}[v\_{k,\*}]\_{\*}(\bar{t},\bar{x})\Big\}\geq 0, |  | (3.16) |

   for all (t¯,x¯)∈[Tk−1,Tk)×𝒮(\bar{t},\bar{x})\in[T\_{k-1},T\_{k})\times{\mathcal{S}} and for all φ∈C1,2​([Tk−1,Tk)×𝒮)\varphi\in C^{1,2}([T\_{k-1},T\_{k})\times{\mathcal{S}}) such that (t¯,x¯)(\bar{t},\bar{x}) is a minimum point of vk,∗−φv\_{k,\*}-\varphi.
2. (2)

   For each TkT\_{k} with k=1,…,K−1k=1,\ldots,K-1,

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | vk,∗​(Tk,x)−inf0≤θk≤x0[wk​(Gk−θk)++vk+1,∗​(Tk,x0−θk,x1)],\displaystyle v\_{k,\*}(T\_{k},x)-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,\*}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right], |  | (3.17) |
   |  |  | vk,∗(Tk,x)−ℳ[vk,∗]∗(Tk,x)}≥0,\displaystyle v\_{k,\*}(T\_{k},x)-{\mathcal{M}}[v\_{k,\*}]\_{\*}(T\_{k},x)\Big\}\geq 0, |  |

   for all x∈𝒮x\in{\mathcal{S}}.
3. (3)

   At the terminal time TKT\_{K},

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | vK,∗​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+,\displaystyle v\_{K,\*}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  | (3.18) |
   |  |  | vK,∗(TK,x)−ℳ[vK,∗]∗(TK,x)}≥0,\displaystyle v\_{K,\*}(T\_{K},x)-{\mathcal{M}}[v\_{K,\*}]\_{\*}(T\_{K},x)\Big\}\geq 0, |  |

   for all x∈𝒮x\in{\mathcal{S}}.
4. (4)

   At the boundary x=(0,0)x=(0,0),

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk,∗​(t,0)≥∑i=kKwi​Gi,t∈[Tk−1,Tk],k=1,…,K.v\_{k,\*}(t,0)\geq\sum^{K}\_{i=k}w\_{i}G\_{i},\quad t\in[T\_{k-1},T\_{k}],\quad k=1,\ldots,K. |  | (3.19) |

###### Definition 3.3 (Viscosity solution).

Consider an array of functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({v1​(t,x)}t∈[0,T1],…,{vk​(t,x)}t∈[Tk−1,Tk],…,{vK​(t,x)}t∈[TK−1,T]),(\{v\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{v\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{v\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}), |  | (3.20) |

where vk​(t,x):[Tk−1,Tk]×𝒮¯→ℝv\_{k}(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is locally bounded for each k=1,…,Kk=1,\ldots,K. The array ([3.20](https://arxiv.org/html/2510.21650v1#S3.E20 "In Definition 3.3 (Viscosity solution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is a viscosity solution of the QVI system if it is a viscosity subsolution under Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") and a viscosity supersolution under Definition [3.2](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem2 "Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

The first main result of this paper is stated as follows:

###### Theorem 3.4.

The value function array defined in ([3.1](https://arxiv.org/html/2510.21650v1#S3.E1 "In 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is the unique viscosity solution of the QVI system. For each k=1,…,Kk=1,\ldots,K, the function Vk​(t,x)V\_{k}(t,x) is continuous and bounded on [Tk−1,Tk]×𝒮¯[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}.

The proof relies on the stochastic Perron’s method developed in bayraktar2013stochastic; bayraktar2015stochastic. The main advantage of this approach is that it avoids the need to establish the dynamic programming principle (DPP) a priori, instead deriving it after demonstrating that the value function satisfies the viscosity solution property. This method circumvents the technical difficulties and potential gaps in DPP proofs.

Theorem [3.4](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") is proved in three steps:

1. (1)

   In Section [4](https://arxiv.org/html/2510.21650v1#S4 "4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), stochastic supersolutions are defined to bound the value function from above. The infimum of them is called the upper stochastic envelope and is shown to be a viscosity subsolution.
2. (2)

   In Section [5](https://arxiv.org/html/2510.21650v1#S5 "5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), stochastic subsolutions are defined to bound the value function from below. The supremum of them is called the lower stochastic envelope and is shown to be a viscosity supersolution.
3. (3)

   In Section [6](https://arxiv.org/html/2510.21650v1#S6 "6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), a comparison argument is applied to complete the proof of Theorem [3.4](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

## 4 Stochastic supersolution

In this paper, we fix a constant p0∈(0,1)p\_{0}\in(0,1), which serves as the growth rate.

###### Definition 4.1 (Stochastic supersolution).

Consider an array of functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({v1​(t,x)}t∈[0,T1],…,{vk​(t,x)}t∈[Tk−1,Tk],…,{vK​(t,x)}t∈[TK−1,T]).(\{v\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{v\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{v\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}). |  | (4.1) |

The array ([4.1](https://arxiv.org/html/2510.21650v1#S4.E1 "In Definition 4.1 (Stochastic supersolution). ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is a stochastic supersolution of the QVI system if the following conditions hold:

1. (1)

   For each k=1,…,Kk=1,\ldots,K, the function vk​(t,x):[Tk−1,Tk]×𝒮¯→ℝv\_{k}(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is USC.
2. (2)

   There exists a constant c>0c>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | |vk​(t,x)|≤c​(1+|x|p0),(t,x)∈[Tk−1,Tk]×𝒮¯,k=1,…,K.|v\_{k}(t,x)|\leq c(1+|x|^{p\_{0}}),\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}},\quad k=1,\ldots,K. |  |
3. (3)

   For each k=1,…​Kk=1,\ldots K, consider any random initial condition (τ¯,ξ)(\bar{\tau},\xi) with τ¯∈[Tk−1,Tk]\bar{\tau}\in[T\_{k-1},T\_{k}], ξ∈ℱτ¯\xi\in{\mathcal{F}}\_{\bar{\tau}} and ℙ​(ξ∈𝒮¯)=1\mathbb{P}(\xi\in\overline{\mathcal{S}})=1. There exists a (τ¯,ξ)(\bar{\tau},\xi)-admissible strategy (θk:K,Λ)(\theta\_{k:K},\Lambda), such that for all stopping time ρ∈[τ¯,T]\rho\in[\bar{\tau},T], we have

   |  |  |  |
   | --- | --- | --- |
   |  | vk​(τ¯,ξ)≥𝔼​[ℋ​([τ¯,ρ],vk:K,X​(⋅;τ¯,ξ,θk:K,Λ))|ℱτ¯],v\_{k}(\bar{\tau},\xi)\geq\mathbb{E}\big[\mathcal{H}\big([\bar{\tau},\rho],v\_{k:K},X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\Lambda)\big)\big|{\mathcal{F}}\_{\bar{\tau}}\big], |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ℋ​([τ¯,ρ],vk:K,X​(⋅;τ¯,ξ,θk:K,Λ))\displaystyle\mathcal{H}\big([\bar{\tau},\rho],v\_{k:K},X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\Lambda)\big) |  | (4.2) |
   |  |  |  |
   | --- | --- | --- |
   |  | :=vk​(ρ,X​(ρ;τ¯,ξ,θk:K,Λ))​𝟏{τ¯≤ρ<Tk}\displaystyle\quad:=v\_{k}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{k:K},\Lambda))\mathbf{1}\_{\{\bar{\tau}\leq\rho<T\_{k}\}} |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +∑l=kK−1{vl+1​(ρ,X​(ρ;τ¯,ξ,θk:K,Λ))+∑i=klwi​(Gi−θi)+}​𝟏{Tl≤ρ<Tl+1}\displaystyle\qquad+\sum^{K-1}\_{l=k}\Big\{v\_{l+1}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{k:K},\Lambda))+\sum^{l}\_{i=k}w\_{i}(G\_{i}-\theta\_{i})^{+}\Big\}\mathbf{1}\_{\{T\_{l}\leq\rho<T\_{l+1}\}} |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +{∑i=kKwi​(Gi−θi)+}​𝟏{ρ=T}.\displaystyle\qquad+\Big\{\sum^{K}\_{i=k}w\_{i}(G\_{i}-\theta\_{i})^{+}\Big\}\mathbf{1}\_{\{\rho=T\}}. |  |

   We refer to (θk:K,Λ)(\theta\_{k:K},\Lambda) as a suitable strategy for vkv\_{k} (and vk+1:Kv\_{k+1:K} in ([4.1](https://arxiv.org/html/2510.21650v1#S4.E1 "In Definition 4.1 (Stochastic supersolution). ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) with the random initial condition (τ¯,ξ)(\bar{\tau},\xi).

Denote by 𝒱+{\mathcal{V}}^{+} the set of stochastic supersolutions. Write v:=(v1,…,vk,…,vK)v:=(v\_{1},\ldots,v\_{k},\ldots,v\_{K}) and use v∈𝒱+v\in{\mathcal{V}}^{+} to indicate that vv is a stochastic supersolution.

The set 𝒱+{\mathcal{V}}^{+} is nonempty because

|  |  |  |  |
| --- | --- | --- | --- |
|  | vk​(t,x)=∑i=kKwi​Gi,(t,x)∈[Tk−1,Tk]×𝒮¯v\_{k}(t,x)=\sum^{K}\_{i=k}w\_{i}G\_{i},\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}} |  | (4.3) |

is a stochastic supersolution.

For k=1,…,Kk=1,\ldots,K and (t,x)∈[Tk−1,Tk]×𝒮¯(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | vk,+​(t,x):=inf{vk​(t,x)|vk​ is the k-th element of some ​v∈𝒱+}.v\_{k,+}(t,x):=\inf\big\{v\_{k}(t,x)|\;v\_{k}\text{ is the $k$-th element of some }v\in{\mathcal{V}}^{+}\big\}. |  | (4.4) |

The upper stochastic envelope is denoted by v+:=(v1,+,…,vk,+,…,vK,+)v\_{+}:=(v\_{1,+},\ldots,v\_{k,+},\ldots,v\_{K,+}). By definition, we can show that v+v\_{+} is an upper bound of the value function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vk,+​(t,x)≥Vk​(t,x),(t,x)∈[Tk−1,Tk]×𝒮¯.v\_{k,+}(t,x)\geq V\_{k}(t,x),\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}. |  | (4.5) |

Lemma [4.2](https://arxiv.org/html/2510.21650v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") below establishes that the family 𝒱+{\mathcal{V}}^{+} of stochastic supersolutions is stable under taking the minimum. The proof follows directly from the definition and is therefore omitted.

###### Lemma 4.2.

If (v11,…,vk1,…,vK1)(v^{1}\_{1},\ldots,v^{1}\_{k},\ldots,v^{1}\_{K}) and (v12,…,vk2,…,vK2)(v^{2}\_{1},\ldots,v^{2}\_{k},\ldots,v^{2}\_{K}) are stochastic supersolutions, then (v11∧v12,…,vk1∧vk2,…,vK1∧vK2)(v^{1}\_{1}\wedge v^{2}\_{1},\ldots,v^{1}\_{k}\wedge v^{2}\_{k},\ldots,v^{1}\_{K}\wedge v^{2}\_{K}) is also a stochastic supersolution.

We now prove the viscosity subsolution property of v+v\_{+} in Proposition [4.3](https://arxiv.org/html/2510.21650v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proposition 4.3.

The upper stochastic envelope v+v\_{+} is a viscosity subsolution of the QVI system under Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proof.

The proof proceeds as follows:

1. (1)

   Since ([4.3](https://arxiv.org/html/2510.21650v1#S4.E3 "In 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is a stochastic supersolution and vk,+v\_{k,+} is the infimum, Condition (4) at x=(0,0)x=(0,0) holds.
2. (2)

   Condition (3) at TKT\_{K} is established in Lemma [A.2](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
3. (3)

   Condition (2) at TkT\_{k}, for k=1,…,K−1k=1,\ldots,K-1, is proved in Lemma [A.3](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
4. (4)

   Lemma [A.4](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem4 "Lemma A.4. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") verifies Condition (1) in Definition [3.2](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem2 "Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), concerning the viscosity supersolution property on [Tk−1,Tk)×𝒮[T\_{k-1},T\_{k})\times{\mathcal{S}}.

∎

## 5 Stochastic subsolution

###### Definition 5.1 (Stochastic subsolution).

Consider an array of functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({v1​(t,x)}t∈[0,T1],…,{vk​(t,x)}t∈[Tk−1,Tk],…,{vK​(t,x)}t∈[TK−1,T]).(\{v\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{v\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{v\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}). |  | (5.1) |

The array ([5.1](https://arxiv.org/html/2510.21650v1#S5.E1 "In Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is a stochastic subsolution of the QVI system if the following conditions hold:

1. (1)

   For each k=1,…,Kk=1,\ldots,K, the function vk​(t,x):[Tk−1,Tk]×𝒮¯→ℝv\_{k}(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is LSC.
2. (2)

   There exists a constant c>0c>0 such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |vk​(t,x)|≤c​(1+|x|p0),(t,x)∈[Tk−1,Tk]×𝒮¯,k=1,…,K.|v\_{k}(t,x)|\leq c(1+|x|^{p\_{0}}),\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}},\quad k=1,\ldots,K. |  | (5.2) |
3. (3)

   The function vkv\_{k} is nondecreasing in the direction of transactions, that is,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk​(t,x)≤ℳ​[vk]​(t,x),(t,x)∈[Tk−1,Tk]×𝒮¯,k=1,…,K.v\_{k}(t,x)\leq{\mathcal{M}}[v\_{k}](t,x),\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}},\quad k=1,\ldots,K. |  | (5.3) |
4. (4)

   For each k=1,…​Kk=1,\ldots K, consider any random initial condition (τ¯,ξ)(\bar{\tau},\xi) with τ¯∈[Tk−1,Tk]\bar{\tau}\in[T\_{k-1},T\_{k}], ξ∈ℱτ¯\xi\in{\mathcal{F}}\_{\bar{\tau}} and ℙ​(ξ∈𝒮¯)=1\mathbb{P}(\xi\in\overline{\mathcal{S}})=1. For any (τ¯,ξ)(\bar{\tau},\xi)-admissible withdrawals θk:K\theta\_{k:K}, the following inequality holds:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk​(τ¯,ξ)≤𝔼​[ℋ​([τ¯,ρ],vk:K,X​(⋅;τ¯,ξ,θk:K,∅))|ℱτ¯]v\_{k}(\bar{\tau},\xi)\leq\mathbb{E}\big[\mathcal{H}\big([\bar{\tau},\rho],v\_{k:K},X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset)\big)\big|{\mathcal{F}}\_{\bar{\tau}}\big] |  | (5.4) |

   for any stopping time ρ∈[τ¯,T]\rho\in[\bar{\tau},T], where ℋ​([τ¯,ρ],vk:K,X​(⋅;τ¯,ξ,θk:K,∅))\mathcal{H}([\bar{\tau},\rho],v\_{k:K},X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset)) is defined in ([4.2](https://arxiv.org/html/2510.21650v1#S4.E2 "In item (3) ‣ Definition 4.1 (Stochastic supersolution). ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")).

Denote the set of stochastic subsolutions as 𝒱−{\mathcal{V}}^{-}.

Condition (4) implies the following terminal condition for vKv\_{K} when τ¯=T\bar{\tau}=T, ξ=x∈𝒮¯\xi=x\in\overline{\mathcal{S}}, and ρ=T\rho=T:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vK​(T,x)≤wK​[GK−x0−(x1−C​(−x1))+]+,x∈𝒮¯.v\_{K}(T,x)\leq w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+},\quad x\in\overline{\mathcal{S}}. |  | (5.5) |

This result uses the assumption that θK\theta\_{K} liquidates the stock position whenever it does not generate a net loss.

For brevity, we write v∈𝒱−v\in{\mathcal{V}}^{-} to indicate that vv is a stochastic subsolution. Lemma [5.2](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem2 "Lemma 5.2. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") below shows that the family 𝒱−{\mathcal{V}}^{-} is stable under taking the maximum. The proof is omitted since it follows directly from the definition.

###### Lemma 5.2.

If (v11,…,vk1,…,vK1)(v^{1}\_{1},\ldots,v^{1}\_{k},\ldots,v^{1}\_{K}) and (v12,…,vk2,…,vK2)(v^{2}\_{1},\ldots,v^{2}\_{k},\ldots,v^{2}\_{K}) are stochastic subsolutions, then (v11∨v12,…,vk1∨vk2,…,vK1∨vK2)(v^{1}\_{1}\vee v^{2}\_{1},\ldots,v^{1}\_{k}\vee v^{2}\_{k},\ldots,v^{1}\_{K}\vee v^{2}\_{K}) is also a stochastic subsolution.

The following example is useful for constructing a strict classical subsolution and proving the comparison principle. The result in Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") remains valid if the constant 22 in CkC\_{k} is replaced by a larger constant.

###### Lemma 5.3.

Let constants a∈{0,1}a\in\{0,1\}, q∈(0,1)q\in(0,1), λ>q​max⁡{r,μ,0}\lambda>q\max\{r,\mu,0\}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ck=∑i=kK2​wi​Gi1−q​eλ​(Ti−Tk).C\_{k}=\sum^{K}\_{i=k}2w\_{i}G^{1-q}\_{i}e^{\lambda(T\_{i}-T\_{k})}. |  | (5.6) |

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fka​(t,x)=∑i=kKwi​Gi−Ck​(a+x0+x1)q​eλ​(Tk−t).F^{a}\_{k}(t,x)=\sum^{K}\_{i=k}w\_{i}G\_{i}-C\_{k}(a+x\_{0}+x\_{1})^{q}e^{\lambda(T\_{k}-t)}. |  | (5.7) |

Then there exist continuous functions {κkc​(x)}k=1K\{\kappa^{c}\_{k}(x)\}^{K}\_{k=1} and {κkb​(x)}k=1K\{\kappa^{b}\_{k}(x)\}^{K}\_{k=1}, satisfying

|  |  |  |
| --- | --- | --- |
|  | κkc​(x)≤0,κkb​(x)≤0,x∈𝒮¯,\displaystyle\kappa^{c}\_{k}(x)\leq 0,\;\kappa^{b}\_{k}(x)\leq 0,\quad x\in\overline{\mathcal{S}}, |  |
|  |  |  |
| --- | --- | --- |
|  | κkc​(x)<0,κkb​(x)<0,x∈𝒮.\displaystyle\kappa^{c}\_{k}(x)<0,\;\kappa^{b}\_{k}(x)<0,\quad x\in{\mathcal{S}}. |  |

Moreover, the following conditions hold:

1. (1)

   For each k=1,…,Kk=1,\ldots,K,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | max⁡{ℒ​[Fka]​(t,x),Fka​(t,x)−ℳ​[Fka]​(t,x)}≤κkc​(x)<0,\max\Big\{{\mathcal{L}}[F^{a}\_{k}](t,x),F^{a}\_{k}(t,x)-{\mathcal{M}}[F^{a}\_{k}](t,x)\Big\}\leq\kappa^{c}\_{k}(x)<0, |  | (5.8) |

   for all (t,x)∈[Tk−1,Tk)×𝒮(t,x)\in[T\_{k-1},T\_{k})\times{\mathcal{S}}.
2. (2)

   For each TkT\_{k} with k=1,…,K−1k=1,\ldots,K-1,

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | Fka​(Tk,x)−inf0≤θk≤x0[wk​(Gk−θk)++Fk+1a​(Tk,x0−θk,x1)],\displaystyle F^{a}\_{k}(T\_{k},x)-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+F^{a}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right], |  | (5.9) |
   |  |  | Fka(Tk,x)−ℳ[Fka](Tk,x)}≤κbk(x)<0,\displaystyle F^{a}\_{k}(T\_{k},x)-{\mathcal{M}}[F^{a}\_{k}](T\_{k},x)\Big\}\leq\kappa^{b}\_{k}(x)<0, |  |

   for all x∈𝒮x\in{\mathcal{S}}.
3. (3)

   At the terminal time TKT\_{K},

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | FKa​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+,\displaystyle F^{a}\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  | (5.10) |
   |  |  | FKa(TK,x)−ℳ[FKa](TK,x)}≤κbK(x)<0,\displaystyle F^{a}\_{K}(T\_{K},x)-{\mathcal{M}}[F^{a}\_{K}](T\_{K},x)\Big\}\leq\kappa^{b}\_{K}(x)<0, |  |

   for all x∈𝒮x\in{\mathcal{S}}.

Based on Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), an example of stochastic subsolutions is given as follows.

###### Lemma 5.4.

The array of functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | F0:=({F10​(t,x)}t∈[0,T1],…,{Fk0​(t,x)}t∈[Tk−1,Tk],…,{FK0​(t,x)}t∈[TK−1,T]),F^{0}:=(\{F^{0}\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{F^{0}\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{F^{0}\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}), |  | (5.11) |

where each element is defined in ([5.7](https://arxiv.org/html/2510.21650v1#S5.E7 "In Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) with q=p0q=p\_{0} and a=0a=0, is a stochastic subsolution to the QVI system.

For each k=1,…,Kk=1,\ldots,K and (t,x)∈[Tk−1,Tk]×𝒮¯(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | vk,−​(t,x):=sup{vk​(t,x)|vk​ is the k-th element of some ​v∈𝒱−}.v\_{k,-}(t,x):=\sup\big\{v\_{k}(t,x)\big|\;v\_{k}\text{ is the $k$-th element of some }v\in{\mathcal{V}}^{-}\big\}. |  | (5.12) |

The supremum in ([5.12](https://arxiv.org/html/2510.21650v1#S5.E12 "In 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is taken over all vkv\_{k} that can form part of a stochastic subsolution together with some (v1,…,vk−1,vk+1,…,vK)(v\_{1},\ldots,v\_{k-1},v\_{k+1},\ldots,v\_{K}). Denote the lower stochastic envelope as

|  |  |  |
| --- | --- | --- |
|  | v−:=(v1,−,…,vk,−,…,vK,−).v\_{-}:=(v\_{1,-},\ldots,v\_{k,-},\ldots,v\_{K,-}). |  |

The following properties hold for the lower stochastic envelope v−v\_{-}:

1. (1)

   Stochastic subsolutions do not exceed the value function. For any v∈𝒱−v\in{\mathcal{V}}^{-}, applying Fatou’s lemma yields

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | vk(t,x)≤𝔼[\displaystyle v\_{k}(t,x)\leq\mathbb{E}\Big[ | ∑i=kKwi(Gi−θi)+|X(t−)=x],\displaystyle\sum^{K}\_{i=k}w\_{i}(G\_{i}-\theta\_{i})^{+}\Big|X(t-)=x\Big], |  | (5.13) |

   for any admissible (θk:K,Λ)∈𝒜​(t,x;k)(\theta\_{k:K},\Lambda)\in\mathcal{A}(t,x;k). Taking the infimum over all admissible controls (θk:K,Λ)∈𝒜​(t,x;k)(\theta\_{k:K},\Lambda)\in\mathcal{A}(t,x;k) gives

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk​(t,x)≤Vk​(t,x),(t,x)∈[Tk−1,Tk]×𝒮¯.v\_{k}(t,x)\leq V\_{k}(t,x),\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}. |  | (5.14) |

   Taking the supremum on the left-hand side then implies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk,−​(t,x)≤Vk​(t,x),(t,x)∈[Tk−1,Tk]×𝒮¯.v\_{k,-}(t,x)\leq V\_{k}(t,x),\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}. |  | (5.15) |

   Since the value function is bounded, ([5.14](https://arxiv.org/html/2510.21650v1#S5.E14 "In item (1) ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) also shows that stochastic subsolutions are bounded above. Therefore, Condition (2) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") can be imposed on the lower side only.
2. (2)

   The supremum in ([5.12](https://arxiv.org/html/2510.21650v1#S5.E12 "In 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is attained and v−∈𝒱−v\_{-}\in{\mathcal{V}}^{-}. The proof follows the argument of belak2017impulse, which relies on the result of bayraktar2012linear ensuring that the supremum can be chosen to be countable.
3. (3)

   Since Lemma [5.4](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem4 "Lemma 5.4. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") establishes that F0F^{0} in ([5.11](https://arxiv.org/html/2510.21650v1#S5.E11 "In Lemma 5.4. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is a stochastic subsolution, the following boundary condition holds:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk,−​(t,0)≥∑i=kKwi​Gi,t∈[Tk−1,Tk],k=1,…,K.v\_{k,-}(t,0)\geq\sum^{K}\_{i=k}w\_{i}G\_{i},\quad t\in[T\_{k-1},T\_{k}],\quad k=1,\ldots,K. |  | (5.16) |

   Combining this with ([5.15](https://arxiv.org/html/2510.21650v1#S5.E15 "In item (1) ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) gives

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vk,−​(t,0)=∑i=kKwi​Gi,t∈[Tk−1,Tk],k=1,…,K.v\_{k,-}(t,0)=\sum^{K}\_{i=k}w\_{i}G\_{i},\quad t\in[T\_{k-1},T\_{k}],\quad k=1,\ldots,K. |  | (5.17) |

We prove the viscosity supersolution property of v−v\_{-} in Proposition [5.5](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem5 "Proposition 5.5. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proposition 5.5.

The lower stochastic envelope v−v\_{-} is a viscosity supersolution of the QVI system under Definition [3.2](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem2 "Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proof.

The proof proceeds as follows:

1. (1)

   Condition (4) at x=(0,0)x=(0,0) has been verified in ([5.17](https://arxiv.org/html/2510.21650v1#S5.E17 "In item (3) ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")).
2. (2)

   Condition (3) at TKT\_{K} is established in Lemma [B.1](https://arxiv.org/html/2510.21650v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
3. (3)

   Condition (2) at TkT\_{k}, for k=1,…,K−1k=1,\ldots,K-1, is proved in Lemma [B.2](https://arxiv.org/html/2510.21650v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
4. (4)

   Following arguments similar to those in bayraktar2013stochastic, Condition (1) in Definition [3.2](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem2 "Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), which concerns the viscosity supersolution property on [Tk−1,Tk)×𝒮[T\_{k-1},T\_{k})\times{\mathcal{S}}, can be established. The detailed proof is omitted.

∎

## 6 Comparison principle

This section establishes a comparison principle that guarantees the continuity and uniqueness of viscosity solutions to the QVI system. The proof follows the standard approach based on Ishii’s lemma (pham2009book, Section 4.4) and the treatment of the intervention operator ℳ{\mathcal{M}} described in belak2019utility; belak2022optimal. The result is included here for completeness.

###### Proposition 6.1 (Terminal comparison at TkT\_{k}).

Let k=1,…,K−1k=1,\ldots,K-1 and consider a continuous and bounded function f​(t,x):[Tk,Tk+1]×𝒮¯→ℝf(t,x):[T\_{k},T\_{k+1}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R}. Suppose that the following conditions hold:

1. (1)

   The function u​(t,x):[Tk−1,Tk]×𝒮¯→ℝu(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is USC and satisfies

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | u​(Tk,x)−inf0≤θk≤x0[wk​(Gk−θk)++f​(Tk,x0−θk,x1)],\displaystyle u(T\_{k},x)-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right], |  | (6.1) |
   |  |  | u(Tk,x)−ℳ[u]∗(Tk,x)}≤0,x∈𝒮.\displaystyle u(T\_{k},x)-{\mathcal{M}}[u]^{\*}(T\_{k},x)\Big\}\leq 0,\quad x\in{\mathcal{S}}. |  |
2. (2)

   The function v​(t,x):[Tk−1,Tk]×𝒮¯→ℝv(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is LSC and satisfies

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | v​(Tk,x)−inf0≤θk≤x0[wk​(Gk−θk)++f​(Tk,x0−θk,x1)],\displaystyle v(T\_{k},x)-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right], |  | (6.2) |
   |  |  | v(Tk,x)−ℳ[v]∗(Tk,x)}≥0,x∈𝒮.\displaystyle v(T\_{k},x)-{\mathcal{M}}[v]\_{\*}(T\_{k},x)\Big\}\geq 0,\quad x\in{\mathcal{S}}. |  |
3. (3)

   At the corner 0,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | u​(Tk,0)≤v​(Tk,0),v​(Tk,0)=∑i=kKwi​Gi.u(T\_{k},0)\leq v(T\_{k},0),\quad v(T\_{k},0)=\sum^{K}\_{i=k}w\_{i}G\_{i}. |  | (6.3) |

   Furthermore, for any x∈𝒮¯x\in\overline{\mathcal{S}},

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | 0\displaystyle 0 | ≤u​(Tk,x)≤∑i=kKwi​Gi,\displaystyle\leq u(T\_{k},x)\leq\sum^{K}\_{i=k}w\_{i}G\_{i}, |  | (6.4) |
   |  | −c​(1+|x|p0)\displaystyle-c(1+|x|^{p\_{0}}) | ≤v​(Tk,x)≤∑i=kKwi​Gi with some constant ​c>0.\displaystyle\leq v(T\_{k},x)\leq\sum^{K}\_{i=k}w\_{i}G\_{i}\quad\text{ with some constant }c>0. |  |

Then it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(Tk,x)≤v​(Tk,x),∀x∈𝒮¯.u(T\_{k},x)\leq v(T\_{k},x),\quad\forall\;x\in\overline{\mathcal{S}}. |  | (6.5) |

###### Proposition 6.2 (Terminal comparison at TKT\_{K}).

Suppose that the following conditions hold:

1. (1)

   The function u​(t,x):[TK−1,TK]×𝒮¯→ℝu(t,x):[T\_{K-1},T\_{K}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is USC and satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | u​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+,\displaystyle u(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | u(TK,x)−ℳ[u]∗(TK,x)}≤0,x∈𝒮.\displaystyle u(T\_{K},x)-{\mathcal{M}}[u]^{\*}(T\_{K},x)\Big\}\leq 0,\quad x\in{\mathcal{S}}. |  |
2. (2)

   The function v​(t,x):[TK−1,TK]×𝒮¯→ℝv(t,x):[T\_{K-1},T\_{K}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R} is LSC and satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | max{\displaystyle\max\Big\{ | v​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+,\displaystyle v(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | v(TK,x)−ℳ[v]∗(TK,x)}≥0,x∈𝒮.\displaystyle v(T\_{K},x)-{\mathcal{M}}[v]\_{\*}(T\_{K},x)\Big\}\geq 0,\quad x\in{\mathcal{S}}. |  |
3. (3)

   At the corner 0,

   |  |  |  |
   | --- | --- | --- |
   |  | u​(TK,0)≤v​(TK,0),v​(TK,0)=wK​GK.u(T\_{K},0)\leq v(T\_{K},0),\quad v(T\_{K},0)=w\_{K}G\_{K}. |  |

   Furthermore, for any x∈𝒮¯x\in\overline{\mathcal{S}},

   |  |  |  |
   | --- | --- | --- |
   |  | 0≤u​(TK,x)≤wK​GK,−c​(1+|x|p0)≤v​(TK,x)≤wK​GK​with some constant c>0.\displaystyle 0\leq u(T\_{K},x)\leq w\_{K}G\_{K},\quad-c(1+|x|^{p\_{0}})\leq v(T\_{K},x)\leq w\_{K}G\_{K}\;\text{with some constant $c>0$.} |  |

Then it follows that

|  |  |  |
| --- | --- | --- |
|  | u​(TK,x)≤v​(TK,x),∀x∈𝒮¯.u(T\_{K},x)\leq v(T\_{K},x),\quad\forall\;x\in\overline{\mathcal{S}}. |  |

###### Proposition 6.3 (Comparison principle: t∈[Tk−1,Tk)t\in[T\_{k-1},T\_{k})).

Let k=1,…,Kk=1,\ldots,K. Suppose that the following conditions hold:

1. (1)

   The function u∈U​S​C​([Tk−1,Tk]×𝒮¯)u\in USC([T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}) is a viscosity subsolution of ([3.6](https://arxiv.org/html/2510.21650v1#S3.E6 "In item (1) ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) on [Tk−1,Tk)×𝒮[T\_{k-1},T\_{k})\times{\mathcal{S}}, that is, the USC function uu satisfies ([3.11](https://arxiv.org/html/2510.21650v1#S3.E11 "In item (1) ‣ Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) in Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
2. (2)

   The function v∈L​S​C​([Tk−1,Tk]×𝒮¯)v\in LSC([T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}) is a viscosity supersolution of ([3.6](https://arxiv.org/html/2510.21650v1#S3.E6 "In item (1) ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) on [Tk−1,Tk)×𝒮[T\_{k-1},T\_{k})\times{\mathcal{S}}, that is, the LSC function vv satisfies ([3.16](https://arxiv.org/html/2510.21650v1#S3.E16 "In item (1) ‣ Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) in Definition [3.2](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem2 "Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
3. (3)

   There exists a constant c>0c>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | −c​(1+|x|p0)≤v​(t,x)≤∑i=kKwi​Gi,(t,x)∈[Tk−1,Tk]×𝒮¯.-c(1+|x|^{p\_{0}})\leq v(t,x)\leq\sum^{K}\_{i=k}w\_{i}G\_{i},\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}. |  |

   Furthermore,

   |  |  |  |
   | --- | --- | --- |
   |  | 0≤u​(t,x)≤∑i=kKwi​Gi,(t,x)∈[Tk−1,Tk]×𝒮¯,\displaystyle 0\leq u(t,x)\leq\sum^{K}\_{i=k}w\_{i}G\_{i},\quad(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}, |  |
   |  |  |  |
   | --- | --- | --- |
   |  | u​(t,0)≤v​(t,0)=∑i=kKwi​Gi,t∈[Tk−1,Tk],\displaystyle u(t,0)\leq v(t,0)=\sum^{K}\_{i=k}w\_{i}G\_{i},\quad t\in[T\_{k-1},T\_{k}], |  |
   |  |  |  |
   | --- | --- | --- |
   |  | u​(Tk,x)≤v​(Tk,x),x∈𝒮¯.\displaystyle u(T\_{k},x)\leq v(T\_{k},x),\quad x\in\overline{\mathcal{S}}. |  |

Then it follows that

|  |  |  |
| --- | --- | --- |
|  | u​(t,x)≤v​(t,x),∀(t,x)∈[Tk−1,Tk]×𝒮¯.u(t,x)\leq v(t,x),\quad\forall\;(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}. |  |

We now provide the proof of the viscosity solution properties of the value function.

###### Proof of Theorem [3.4](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

The argument proceeds by backward induction.

1. (1)

   At the terminal time TKT\_{K}, Lemma [B.1](https://arxiv.org/html/2510.21650v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that vK,−v\_{K,-} is an LSC viscosity supersolution, and Lemma [A.2](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that vK,+v\_{K,+} is a USC viscosity subsolution. Moreover, vK,−v\_{K,-} and vK,+v\_{K,+} satisfy the boundary and growth conditions required in Condition (3) of Proposition [6.2](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem2 "Proposition 6.2 (Terminal comparison at 𝑇_𝐾). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), which yields

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vK,+​(TK,x)≤vK,−​(TK,x),x∈𝒮¯.v\_{K,+}(T\_{K},x)\leq v\_{K,-}(T\_{K},x),\quad x\in\overline{{\mathcal{S}}}. |  | (6.6) |

   As established earlier, vK,−​(TK,x)≤VK​(TK,x)≤vK,+​(TK,x)v\_{K,-}(T\_{K},x)\leq V\_{K}(T\_{K},x)\leq v\_{K,+}(T\_{K},x) fo all x∈𝒮¯x\in\overline{{\mathcal{S}}}. Therefore,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vK,−​(TK,x)=vK,+​(TK,x)=VK​(TK,x),x∈𝒮¯.v\_{K,-}(T\_{K},x)=v\_{K,+}(T\_{K},x)=V\_{K}(T\_{K},x),\;x\in\overline{{\mathcal{S}}}. |  | (6.7) |

   Moreover, VK​(TK,⋅)V\_{K}(T\_{K},\cdot) is continuous and bounded on 𝒮¯\overline{{\mathcal{S}}}.
2. (2)

   On the interval [TK−1,TK)[T\_{K-1},T\_{K}), the functions vK,−v\_{K,-} and vK,+v\_{K,+} satisfy the boundary condition at 0, the growth condition, and the viscosity supersolution and subsolution properties, respectively. By ([6.6](https://arxiv.org/html/2510.21650v1#S6.E6 "In item (1) ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and Proposition [6.3](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem3 "Proposition 6.3 (Comparison principle: 𝑡∈[𝑇_{𝑘-1},𝑇_𝑘)). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), it follows that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vK,+​(t,x)≤vK,−​(t,x),(t,x)∈[TK−1,TK]×𝒮¯.v\_{K,+}(t,x)\leq v\_{K,-}(t,x),\quad(t,x)\in[T\_{K-1},T\_{K}]\times\overline{{\mathcal{S}}}. |  | (6.8) |

   Since vK,−​(t,x)≤VK​(t,x)≤vK,+​(t,x)v\_{K,-}(t,x)\leq V\_{K}(t,x)\leq v\_{K,+}(t,x), we obtain

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | vK,−​(t,x)=vK,+​(t,x)=VK​(t,x),(t,x)∈[TK−1,TK]×𝒮¯.v\_{K,-}(t,x)=v\_{K,+}(t,x)=V\_{K}(t,x),\quad(t,x)\in[T\_{K-1},T\_{K}]\times\overline{{\mathcal{S}}}. |  | (6.9) |

   Moreover, VK​(t,x)V\_{K}(t,x) is continuous and bounded on [TK−1,TK]×𝒮¯[T\_{K-1},T\_{K}]\times\overline{{\mathcal{S}}}.
3. (3)

   We repeat the previous steps for each k=K−1,…,1k=K-1,\ldots,1. Consequently, the value function array ([3.1](https://arxiv.org/html/2510.21650v1#S3.E1 "In 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is the unique viscosity solution of the QVI system. Moreover, the value function Vk​(t,x)V\_{k}(t,x) is continuous and bounded on [Tk−1,Tk]×𝒮¯[T\_{k-1},T\_{k}]\times\overline{{\mathcal{S}}}.

∎

In contrast to belak2022optimal, we prove that the value function VkV\_{k} is the unique viscosity solution to the QVI system, instead of focusing on the lower stochastic envelope v−v\_{-} only. This choice is motivated by the fact that the positivity of v−v\_{-} cannot be established directly from its definition. When perturbing the continuation and intervention regions to construct optimal strategies, the non-negativity of VkV\_{k} becomes essential. Importantly, the existence of an optimal strategy requires only the continuity, rather than the smoothness, of the value function.

## 7 Construction of optimal strategies

First, we introduce several optimizers that will be used to construct an optimal strategy. Given i=1,…,Ki=1,\ldots,K, recall that Vi​(t,x)V\_{i}(t,x) is the continuous value function with t∈[Ti−1,Ti]t\in[T\_{i-1},T\_{i}]. The continuation region 𝒞i{\mathcal{C}}\_{i} and the intervention region ℐi{\mathcal{I}}\_{i} are defined as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒞i\displaystyle{\mathcal{C}}\_{i} | :={(t,x)∈[Ti−1,Ti]×𝒮¯:Vi​(t,x)<ℳ​[Vi]​(t,x)},\displaystyle:=\{(t,x)\in[T\_{i-1},T\_{i}]\times\overline{\mathcal{S}}:V\_{i}(t,x)<{\mathcal{M}}[V\_{i}](t,x)\}, |  | (7.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℐi\displaystyle{\mathcal{I}}\_{i} | :={(t,x)∈[Ti−1,Ti]×𝒮¯:Vi​(t,x)=ℳ​[Vi]​(t,x)}.\displaystyle:=\{(t,x)\in[T\_{i-1},T\_{i}]\times\overline{\mathcal{S}}:V\_{i}(t,x)={\mathcal{M}}[V\_{i}](t,x)\}. |  | (7.2) |

By schal1974selection, there exists a Borel measurable optimizer gi:[Ti−1,Ti]×(𝒮¯∖𝒮∅)→ℝg\_{i}:[T\_{i-1},T\_{i}]\times(\overline{\mathcal{S}}\setminus{\mathcal{S}}\_{\emptyset})\rightarrow\mathbb{R} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | gi​(t,x)∈D​(x)andℳ​[Vi]​(t,x)=Vi​(t,Γ​(x,gi​(t,x))),g\_{i}(t,x)\in D(x)\quad\text{and}\quad{\mathcal{M}}[V\_{i}](t,x)=V\_{i}(t,\Gamma(x,g\_{i}(t,x))), |  | (7.3) |

for all (t,x)∈[Ti−1,Ti]×(𝒮¯∖𝒮∅)(t,x)\in[T\_{i-1},T\_{i}]\times(\overline{\mathcal{S}}\setminus{\mathcal{S}}\_{\emptyset}).

For i≠Ki\neq K, another application of schal1974selection yields a Borel measurable optimizer Θi​(x):𝒮¯→ℝ\Theta\_{i}(x):\overline{\mathcal{S}}\rightarrow\mathbb{R}, such that Θi​(x)∈[0,x0]\Theta\_{i}(x)\in[0,x\_{0}] and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | inf0≤θi≤x0[wi​(Gi−θi)++Vi+1​(Ti,x0−θi,x1)]\displaystyle\inf\_{0\leq\theta\_{i}\leq x\_{0}}\left[w\_{i}(G\_{i}-\theta\_{i})^{+}+V\_{i+1}(T\_{i},x\_{0}-\theta\_{i},x\_{1})\right] |  | (7.4) |
|  |  | =wi​(Gi−Θi​(x))++Vi+1​(Ti,x0−Θi​(x),x1)\displaystyle\quad=w\_{i}(G\_{i}-\Theta\_{i}(x))^{+}+V\_{i+1}(T\_{i},x\_{0}-\Theta\_{i}(x),x\_{1}) |  |

for all x∈𝒮¯x\in\overline{\mathcal{S}}.

Given k=1,…,Kk=1,\ldots,K and (t,x)∈[Tk−1,Tk]×𝒮¯(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}, our goal is to construct an admissible strategy (θk:K∗,Λ∗)∈𝒜​(t,x;k)(\theta^{\*}\_{k:K},\Lambda^{\*})\in\mathcal{A}(t,x;k), such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vk(t,x)=𝔼[\displaystyle V\_{k}(t,x)=\mathbb{E}\Big[ | ∑i=kKwi(Gi−θi∗)+|X∗(t−)=x].\displaystyle\sum^{K}\_{i=k}w\_{i}(G\_{i}-\theta^{\*}\_{i})^{+}\Big|X^{\*}(t-)=x\Big]. |  | (7.5) |

This implies that (θk:K∗,Λ∗)(\theta^{\*}\_{k:K},\Lambda^{\*}) is an optimal strategy. Here, we denote the corresponding wealth process as X∗​(s):=X​(s;t,x,θk:K∗,Λ∗)X^{\*}(s):=X(s;t,x,\theta^{\*}\_{k:K},\Lambda^{\*}), s∈[t,T]s\in[t,T]. Note that Vk​(Tk,x)V\_{k}(T\_{k},x) includes the funding amount θk∗\theta^{\*}\_{k} for goal kk, whereas Vk+1​(Tk,x)V\_{k+1}(T\_{k},x) excludes θk∗\theta^{\*}\_{k} since goal kk has expired.

The candidate optimal strategy is constructed recursively. The investment strategy Λ∗\Lambda^{\*} is partitioned by goal deadlines as Λ∗:=(Λk∗,…,ΛK∗)\Lambda^{\*}:=(\Lambda^{\*}\_{k},\ldots,\Lambda^{\*}\_{K}), where Λi∗:={(τn∗,i,Δn∗,i)}n=1∞\Lambda^{\*}\_{i}:=\{(\tau^{\*,i}\_{n},\Delta^{\*,i}\_{n})\}^{\infty}\_{n=1} is specified as follows. For Λk∗\Lambda^{\*}\_{k}, the initial position is set to (τ0∗,k,ξ0∗,k)=(t,x)(\tau^{\*,k}\_{0},\xi^{\*,k}\_{0})=(t,x). For n=1,2,…n=1,2,\ldots, define iteratively

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | τn∗,k\displaystyle\tau^{\*,k}\_{n} | :=inf{u∈[τn−1∗,k,Tk]:X​(u;τn−1∗,k,ξn−1∗,k,∅,∅)∈ℐk},\displaystyle=\inf\{u\in[\tau^{\*,k}\_{n-1},T\_{k}]:X(u;\tau^{\*,k}\_{n-1},\xi^{\*,k}\_{n-1},\emptyset,\emptyset)\in{\mathcal{I}}\_{k}\}, |  | (7.6) |
|  | Δn∗,k\displaystyle\Delta^{\*,k}\_{n} | :=gk​(τn∗,k,X​(τn∗,k;τn−1∗,k,ξn−1∗,k,∅,∅))​𝟏{τn∗,k≤Tk},\displaystyle=g\_{k}(\tau^{\*,k}\_{n},X(\tau^{\*,k}\_{n};\tau^{\*,k}\_{n-1},\xi^{\*,k}\_{n-1},\emptyset,\emptyset))\mathbf{1}\_{\{\tau^{\*,k}\_{n}\leq T\_{k}\}}, |  |
|  | ξn∗,k\displaystyle\xi^{\*,k}\_{n} | :=Γ​(X​(τn∗,k;τn−1∗,k,ξn−1∗,k,∅,∅),Δn∗,k).\displaystyle=\Gamma(X(\tau^{\*,k}\_{n};\tau^{\*,k}\_{n-1},\xi^{\*,k}\_{n-1},\emptyset,\emptyset),\Delta^{\*,k}\_{n}). |  |

If k≠Kk\neq K, the candidate optimal supporting amount for goal kk is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | θk∗:=Θk​(X​(Tk;τ0∗,k,ξ0∗,k,∅,Λk∗)).\theta^{\*}\_{k}:=\Theta\_{k}(X(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\emptyset,\Lambda^{\*}\_{k})). |  | (7.7) |

The next component Λk+1∗\Lambda^{\*}\_{k+1} is constructed with the initial position

|  |  |  |  |
| --- | --- | --- | --- |
|  | (τ0∗,k+1,ξ0∗,k+1)=(Tk,X​(Tk;τ0∗,k,ξ0∗,k,θk∗,Λk∗)),(\tau^{\*,k+1}\_{0},\xi^{\*,k+1}\_{0})=(T\_{k},X(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\theta^{\*}\_{k},\Lambda^{\*}\_{k})), |  | (7.8) |

which satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | X0​(Tk;τ0∗,k,ξ0∗,k,θk∗,Λk∗)\displaystyle X\_{0}(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\theta^{\*}\_{k},\Lambda^{\*}\_{k}) | =X0​(Tk;τ0∗,k,ξ0∗,k,∅,Λk∗)−θk∗,\displaystyle=X\_{0}(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\emptyset,\Lambda^{\*}\_{k})-\theta^{\*}\_{k}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | X1​(Tk;τ0∗,k,ξ0∗,k,θk∗,Λk∗)\displaystyle X\_{1}(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\theta^{\*}\_{k},\Lambda^{\*}\_{k}) | =X1​(Tk;τ0∗,k,ξ0∗,k,∅,Λk∗).\displaystyle=X\_{1}(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\emptyset,\Lambda^{\*}\_{k}). |  |

For n=1,2,…n=1,2,\ldots, the terms τn∗,k+1\tau^{\*,k+1}\_{n}, Δn∗,k+1\Delta^{\*,k+1}\_{n}, and ξn∗,k+1\xi^{\*,k+1}\_{n} are defined as in ([7.6](https://arxiv.org/html/2510.21650v1#S7.E6 "In 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), with kk replaced by k+1k+1.

This recursive procedure continues until the final goal KK. The supporting amount for the last goal is determined by the liquidation value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θK∗=L​(X​(TK;τ0∗,K,ξ0∗,K,∅,ΛK∗)).\theta^{\*}\_{K}=L(X(T\_{K};\tau^{\*,K}\_{0},\xi^{\*,K}\_{0},\emptyset,\Lambda^{\*}\_{K})). |  | (7.9) |

To verify that the strategy constructed above is indeed optimal, two technical results are required: Lemma [7.1](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem1 "Lemma 7.1. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") and Lemma [7.2](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem2 "Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). These results are instrumental in establishing Theorem [7.3](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem3 "Theorem 7.3. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). The proof of Lemma [7.1](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem1 "Lemma 7.1. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") follows similar arguments to those in pham2009book and belak2022optimal.

###### Lemma 7.1.

Consider an array of functions given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ({h1​(t,x)}t∈[0,T1],…,{hk​(t,x)}t∈[Tk−1,Tk],…,{hK​(t,x)}t∈[TK−1,T]),(\{h\_{1}(t,x)\}\_{t\in[0,T\_{1}]},\ldots,\{h\_{k}(t,x)\}\_{t\in[T\_{k-1},T\_{k}]},\ldots,\{h\_{K}(t,x)\}\_{t\in[T\_{K-1},T]}), |  | (7.10) |

where hk​(t,x):[Tk−1,Tk]×𝒮¯→ℝh\_{k}(t,x):[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R}, k=1,…,Kk=1,\ldots,K is Borel measurable and satisfies hk​(t,x)≤Cgh\_{k}(t,x)\leq C\_{g} for a generic constant CgC\_{g}. If ([7.10](https://arxiv.org/html/2510.21650v1#S7.E10 "In Lemma 7.1. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) satisfies Conditions (2), (3), and (4) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), then ([7.10](https://arxiv.org/html/2510.21650v1#S7.E10 "In Lemma 7.1. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) also satisfies the viscosity subsolution properties (1), (2), and (3) in Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Lemma 7.2.

For each k=1,…,Kk=1,\ldots,K, consider any random initial condition (τ¯,ξ)(\bar{\tau},\xi) with τ¯∈[Tk−1,Tk]\bar{\tau}\in[T\_{k-1},T\_{k}], ξ∈ℱτ¯\xi\in{\mathcal{F}}\_{\bar{\tau}}, and ℙ​(ξ∈𝒮¯)=1\mathbb{P}(\xi\in\overline{\mathcal{S}})=1. Then for any stopping time ρ∈[τ¯,Tk]\rho\in[\bar{\tau},T\_{k}], the value function VkV\_{k} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(τ¯,ξ)≤𝔼​[Vk​(ρ,X​(ρ;τ¯,ξ,∅,∅))|ℱτ¯].V\_{k}(\bar{\tau},\xi)\leq\mathbb{E}\big[V\_{k}(\rho,X(\rho;\bar{\tau},\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\bar{\tau}}\big]. |  | (7.11) |

The second main result establishes the existence of an optimal strategy, as stated in Theorem [7.3](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem3 "Theorem 7.3. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") below.

###### Theorem 7.3.

Consider k=1,…,Kk=1,\ldots,K and (t,x)∈[Tk−1,Tk]×𝒮¯(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}. The strategy (θk:K∗,Λ∗)(\theta^{\*}\_{k:K},\Lambda^{\*}) is admissible and optimal, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (θk:K∗,Λ∗)∈𝒜​(t,x;k) and Vk​(t,x)=𝔼​[∑i=kKwi​(Gi−θi∗)+|X∗​(t−)=x].(\theta^{\*}\_{k:K},\Lambda^{\*})\in\mathcal{A}(t,x;k)\quad\text{ and }\quad V\_{k}(t,x)=\mathbb{E}\Big[\sum^{K}\_{i=k}w\_{i}(G\_{i}-\theta^{\*}\_{i})^{+}\Big|X^{\*}(t-)=x\Big]. |  | (7.12) |

The corresponding wealth process is denoted by X∗​(s):=X​(s;t,x,θk:K∗,Λ∗)X^{\*}(s):=X(s;t,x,\theta^{\*}\_{k:K},\Lambda^{\*}), s∈[t,T]s\in[t,T].

## 8 Numerical analysis

In this section, we present numerical results for the optimal investment strategies. For simplicity, consider an investor with two goals, G1=3G\_{1}=3 and G2=6G\_{2}=6, with respective deadlines T1=1T\_{1}=1 and T2=2T\_{2}=2. In the benchmark setting, the goal importance weights are w1=1w\_{1}=1 and w2=0.2w\_{2}=0.2, which are close to those in capponi2024 after appropriate adjustments.

For the financial market, unless stated otherwise, the parameters are set as follows: the interest rate r=0r=0, the expected stock return μ=0.3\mu=0.3, and the volatility σ=0.4\sigma=0.4. In this numerical study, we consider only fixed transaction costs, specified by C​(Δ)≡Cmin>0C(\Delta)\equiv C\_{\min}>0. The benchmark case assumes Cmin=0.02C\_{\min}=0.02. The algorithm employs a classical finite difference method combined with a penalty scheme; further details can be found in azimzadeh2017. Following the rationale of belak2022optimal, the computations are conducted on a triangular grid rather than the square grid used in azimzadeh2017. For positions satisfying x0+x1≥G1+G2+Cminx\_{0}+x\_{1}\geq G\_{1}+G\_{2}+C\_{\min}, the value function equals zero. Therefore, the computational domain is restricted to the triangular region where x0+x1≤9+Cminx\_{0}+x\_{1}\leq 9+C\_{\min}. The wealth grid size is set to Δ​x=(9+Cmin)/200\Delta x=(9+C\_{\min})/200, which equals 0.0451 in the benchmark case. The tick size in all heatmap figures such as Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") is set to 10​Δ​x10\Delta x, and the axis labels are rounded to two decimal places. For comparison, Figure [9](https://arxiv.org/html/2510.21650v1#S8.F9 "Figure 9 ‣ 8.3 The straight continuation region near 𝐺₁+𝐺₂+𝐶ₘᵢₙ ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") is computed with a coarser grid size of 9.02/509.02/50 and a tick size of 2×9.02/502\times 9.02/50. The time step is fixed at Δ​t=0.01\Delta t=0.01.

### 8.1 The frictionless case

Before presenting the fixed-cost case, we first reproduce the VV-shaped investment behavior observed in capponi2024. Figure [1](https://arxiv.org/html/2510.21650v1#S8.F1 "Figure 1 ‣ 8.1 The frictionless case ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows the optimal proportion invested in the stock, given by x1/(x0+x1)x\_{1}/(x\_{0}+x\_{1}), over time. The results indicate that the optimal strategy reduces the stock proportion when total wealth approaches G1G\_{1}, the level required to meet the first goal, and increases it once wealth exceeds G1G\_{1}. This VV-shaped adjustment reflects an investor’s tendency to reduce risk near the target level to avoid missing the primary goal. Figure [2](https://arxiv.org/html/2510.21650v1#S8.F2 "Figure 2 ‣ 8.1 The frictionless case ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") illustrates the optimal funding ratio θ1∗/G1\theta^{\*}\_{1}/G\_{1} for goal 1. Since this goal has a significantly higher weight, the investor allocates all available funds to it until the target amount is achieved.

![Refer to caption](x1.png)


Figure 1: Optimal stock proportions without transaction costs.

![Refer to caption](x2.png)


Figure 2: Optimal funding ratio without transaction costs.

We now propose a conjecture regarding the optimal strategy under fixed costs. When the fixed cost is sufficiently small, the optimal stock exposure x1/(x0+x1)x\_{1}/(x\_{0}+x\_{1}) should closely resemble that in the frictionless case for the same total wealth x0+x1x\_{0}+x\_{1}. The continuation region is expected to lie near the frictionless optimal investment proportion, within which the portfolio evolves without adjustment. Due to market fluctuations, the portfolio may occasionally reach the trading boundaries, prompting the investor to buy or sell the stock to reposition the portfolio onto the target set.

The analysis of the fixed-cost case proceeds in two steps. First, we consider a given level of total wealth. Second, by comparing with the frictionless optimal strategy, we identify trading regions that indicate whether to buy or sell when the current position deviates substantially from the target portfolio.

The following aspects are the main focus of our analysis:

1. (1)

   the effect of fixed costs on the portfolio’s risk profile, particularly the relationship between stock investment and total wealth;
2. (2)

   the effect of fixed costs on the funding ratios required to meet investment goals.

In addition, we discuss how these relationships evolve over time, as well as how they change when fixed costs increase or expected stock returns decrease.

### 8.2 The benchmark case with Cmin=0.02C\_{\min}=0.02

This subsection examines the properties of the optimal strategies when the fixed transaction cost is Cmin=0.02C\_{\min}=0.02.

#### 8.2.1 Time t=0.0t=0.0

![Refer to caption](transfer_c0_t0.png)


Figure 3: Optimal trading regions at t=0.0t=0.0 with Cmin=0.02C\_{\min}=0.02.

![Refer to caption](x3.png)


Figure 4: Stock proportions corresponding to the red target points in Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

In figures such as Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), which illustrate the optimal trading regions, the blue area corresponds to selling the stock, the red area corresponds to buying, and the red points mark the target portfolio positions. These red points may represent target positions from either side or from both sides. Since each trade reduces total wealth by CminC\_{\min}, this property can be used to identify the correspondence between the red target points and the positions within the trading regions. A deeper color indicates a larger trade.

The white area denotes the continuation region, where the portfolio evolves uncontrolled. The shape of this region differs significantly from that in Merton’s problem with fixed transaction costs; see belak2022optimal. As shown in Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), the continuation region is not approximately VV-shaped and is not symmetric with respect to the red target positions.

The behavior of the optimal strategies varies with total wealth, as summarized below:

1. (1)

   When x0+x1≥G1+G2+Cminx\_{0}+x\_{1}\geq G\_{1}+G\_{2}+C\_{\min}, it is optimal to sell the stock so that the bank account holds the required amount G1+G2G\_{1}+G\_{2} to meet both goals.
2. (2)

   When total wealth is slightly below G1+G2+CminG\_{1}+G\_{2}+C\_{\min}, Figure [1](https://arxiv.org/html/2510.21650v1#S8.F1 "Figure 1 ‣ 8.1 The frictionless case ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that the optimal stock ratio in the frictionless case remains low. If the current stock holding x1x\_{1} is high, one might expect selling to be optimal; however, after selling, the remaining stock position would be very small since the target level in the frictionless case is close to zero. In this case, even with a positive stock return μ\mu, the potential gain from such a small stock holding is unlikely to offset the fixed cost CminC\_{\min}. Hence, the optimal strategy is not to trade when x1x\_{1} is high and the total wealth is just below G1+G2+CminG\_{1}+G\_{2}+C\_{\min}, which corresponds to the white region in the upper-left corner of Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Conversely, when x1x\_{1} is low, buying the stock becomes optimal since otherwise it is difficult to exceed G1+G2+CminG\_{1}+G\_{2}+C\_{\min} with very small x1x\_{1}. This behavior corresponds to the red area in the lower-right corner of Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").
3. (3)

   When total wealth is lower than G1+G2+CminG\_{1}+G\_{2}+C\_{\min} but above 7.67.6, Figure [1](https://arxiv.org/html/2510.21650v1#S8.F1 "Figure 1 ‣ 8.1 The frictionless case ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that the optimal stock ratio in the frictionless case is higher than before. The investor can now offset the fixed cost through sufficient stock returns, leading to stock sales in the upper-left region of Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), different from the previous case. This implies a non-monotonic relationship between risk exposure and wealth level in this range, resulting from the presence of fixed costs.
4. (4)

   When total wealth is below 7.67.6, a distinct pattern appears for x0+x1∈[7.0,7.6]x\_{0}+x\_{1}\in[7.0,7.6]. A red vertical bar in the middle of Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") indicates that the agent reserves roughly 3.03.0 for goal 1. This corresponds to the increased stock proportion shown in Figure [4](https://arxiv.org/html/2510.21650v1#S8.F4 "Figure 4 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") for the same wealth range, which is the only region where the stock proportion rises.

   In the frictionless case, Figure [1](https://arxiv.org/html/2510.21650v1#S8.F1 "Figure 1 ‣ 8.1 The frictionless case ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that the optimal stock ratio is lower than 100%100\% at t=0t=0 when total wealth exceeds 5.55.5. Under fixed costs, however, if the bank balance is high, the optimal strategy is to allocate all wealth to the stock, for example when x0+x1∈[5.0,6.0]x\_{0}+x\_{1}\in[5.0,6.0]. This suggests more aggressive behavior compared with the frictionless case, as potential transaction costs reduce overall profits. Moreover, for x1∈[4.8,6.6]x\_{1}\in[4.8,6.6] and x0∈[0.6,1.4]x\_{0}\in[0.6,1.4], the optimal decision is to refrain from trading.

#### 8.2.2 Time t=0.5t=0.5 and t=0.9t=0.9

![Refer to caption](transfer_c0_t1.png)


(a) t=0.5t=0.5

![Refer to caption](transfer_c0_t2.png)


(b) t=0.9t=0.9

Figure 5: Optimal trading regions at t=0.5t=0.5 and t=0.9t=0.9 with Cmin=0.02C\_{\min}=0.02.



![Refer to caption](x4.png)


(a) t=0.5t=0.5

![Refer to caption](x5.png)


(b) t=0.9t=0.9

Figure 6: Stock proportions for red target points in Figure [5](https://arxiv.org/html/2510.21650v1#S8.F5 "Figure 5 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

This subsection analyzes the optimal strategies at t=0.5t=0.5 and t=0.9t=0.9. The main observations are as follows:

1. (1)

   Comparing Figure [5](https://arxiv.org/html/2510.21650v1#S8.F5 "Figure 5 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") with Figure [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), the red vertical bar near x0=3.0x\_{0}=3.0 becomes longer as time approaches the deadline T1T\_{1}. This indicates that the investor increasingly prioritizes reserving the required amount of 3.03.0, investing only the excess wealth in the stock. Consequently, Figure [6](https://arxiv.org/html/2510.21650v1#S8.F6 "Figure 6 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that the interval where the stock proportion increases with total wealth also widens. The red vertical bar in the middle originates from the right side when the amount x0x\_{0} in the bank account is high.

   In contrast, when x0+x1∈[3.6,6.6]x\_{0}+x\_{1}\in[3.6,6.6], which is below the total wealth corresponding to the central red bar, the optimal decision is to invest fully in the stock if x0x\_{0} is large. This provides another example where the optimal risk exposure is not monotonic in wealth levels.
2. (2)

   A distinct feature is the wedge-shaped white area in the lower-left corner of Figure [5](https://arxiv.org/html/2510.21650v1#S8.F5 "Figure 5 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") when x0+x1x\_{0}+x\_{1} is near 3.03.0. This reflects a behavior different from the VV-shaped investment strategy described in capponi2024.

   At t=0.5t=0.5, when x0=3.0x\_{0}=3.0 and x1=0.0x\_{1}=0.0, the optimal choice is to invest entirely in the stock. As shown in Figure [6](https://arxiv.org/html/2510.21650v1#S8.F6 "Figure 6 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), the target position allocates nearly 100%100\% to the stock around total wealth 3.03.0, in contrast to the VV-shaped strategy in the frictionless case. However, if the current position lies within the white wedge area, the optimal decision is to refrain from trading.

   At t=0.9t=0.9, a similar continuation region appears near the equi-wealth line x0+x1=3.0x\_{0}+x\_{1}=3.0. Consequently, the investor must consider both the stock and bank account holdings, rather than total wealth alone, when determining the optimal stock exposure.

#### 8.2.3 Time t=1.0t=1.0: Funding ratios and importance weights

![Refer to caption](transfer_c0_t3.png)


(a) w1=5​w2w\_{1}=5w\_{2}

![Refer to caption](transfer_c4_t3.png)


(b) w1=w2w\_{1}=w\_{2}

Figure 7: Optimal trading regions at the deadline T1T\_{1} under different goal weights.

At the deadline T1T\_{1}, the following observations can be made:

1. (1)

   The weight configuration w1=5​w2w\_{1}=5w\_{2} indicates that the first goal is substantially more important than the second. As shown in Figure [7](https://arxiv.org/html/2510.21650v1#S8.F7 "Figure 7 ‣ 8.2.3 Time 𝑡=1.0: Funding ratios and importance weights ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), the agent allocates all available funds to support the first goal, similar to the frictionless case in Figure [2](https://arxiv.org/html/2510.21650v1#S8.F2 "Figure 2 ‣ 8.1 The frictionless case ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). The importance of the first goal outweighs the potential additional returns from investing in the stock for another year. In this case, the fixed transaction cost has little influence on the optimal funding ratio.
2. (2)

   When the weights are equal, w1=w2w\_{1}=w\_{2}, the impact of fixed costs on the optimal funding ratio becomes more pronounced, especially when the total wealth ranges between 4.04.0 and 6.06.0. Figure [8](https://arxiv.org/html/2510.21650v1#S8.F8 "Figure 8 ‣ 8.2.3 Time 𝑡=1.0: Funding ratios and importance weights ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") illustrates that, in the absence of transaction costs, no funding is allocated to goal 1 when the total wealth is below 3.63.6. For wealth between 3.63.6 and 6.66.6, approximately 3.63.6 is retained in the stock, and the remainder is allocated to goal 1. The horizontal red bar in Figure [7](https://arxiv.org/html/2510.21650v1#S8.F7 "Figure 7 ‣ 8.2.3 Time 𝑡=1.0: Funding ratios and importance weights ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") is close to this critical threshold of 3.63.6. The continuation region around this line highlights the influence of fixed costs. The optimal funding amount is determined by considering only the bank account, as no transfer occurs within the continuation region. Each point in Figure [8](https://arxiv.org/html/2510.21650v1#S8.F8 "Figure 8 ‣ 8.2.3 Time 𝑡=1.0: Funding ratios and importance weights ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") represents the corresponding funding ratio θ1∗/G1\theta^{\*}\_{1}/G\_{1} for positions in the continuation region. The results indicate that the optimal funding ratios exhibit greater variability at a given level of total wealth when fixed costs are present.

![Refer to caption](x6.png)


(a) Cmin=0C\_{\min}=0

![Refer to caption](x7.png)


(b) Cmin=0.02C\_{\min}=0.02

Figure 8: Optimal funding ratios under equal weights.

### 8.3 The straight continuation region near G1+G2+CminG\_{1}+G\_{2}+C\_{\min}

The straight continuation region at the wealth level just below G1+G2+CminG\_{1}+G\_{2}+C\_{\min}, illustrated as the narrow strip between the blue regions in the top-left panels of Figures [3](https://arxiv.org/html/2510.21650v1#S8.F3 "Figure 3 ‣ 8.2.1 Time 𝑡=0.0 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") and [5](https://arxiv.org/html/2510.21650v1#S8.F5 "Figure 5 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), is a distinctive feature that arises under the fixed-cost formulation. A closer examination of this pattern is provided below:

1. (1)

   As a consistency check, we verify that this phenomenon is not caused by discretization errors. Indeed, as shown in Figure [9](https://arxiv.org/html/2510.21650v1#S8.F9 "Figure 9 ‣ 8.3 The straight continuation region near 𝐺₁+𝐺₂+𝐶ₘᵢₙ ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), the pattern disappears when a coarser wealth grid is used. The explanation is straightforward: with a larger grid size, fixed costs become relatively less significant. Therefore, a finer grid is required to achieve higher numerical accuracy and to capture this behavior properly.
2. (2)

   When the stock return decreases, the straight continuation region becomes wider, as illustrated in Figure [9](https://arxiv.org/html/2510.21650v1#S8.F9 "Figure 9 ‣ 8.3 The straight continuation region near 𝐺₁+𝐺₂+𝐶ₘᵢₙ ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). This can be interpreted as follows. A lower expected return motivates the agent to hold a larger proportion of wealth in the stock to achieve the investment goals, reducing the likelihood of selling the asset. From another perspective, it also becomes more difficult to generate sufficient returns to offset the fixed transaction cost. Both effects contribute to a broader straight continuation region in the top-left area of Figure [9](https://arxiv.org/html/2510.21650v1#S8.F9 "Figure 9 ‣ 8.3 The straight continuation region near 𝐺₁+𝐺₂+𝐶ₘᵢₙ ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

![Refer to caption](x8.png)


(a) Larger wealth grid size (Δ​x=0.2\Delta x=0.2)

![Refer to caption](transfer_small_mu_c0_t0.png)


(b) Lower stock return (μ=0.1\mu=0.1)

Figure 9: The straight continuation region near G1+G2+CminG\_{1}+G\_{2}+C\_{\min}.

### 8.4 Higher fixed costs

![Refer to caption](transfer_c1_t0.png)


(a) t=0.0t=0.0

![Refer to caption](transfer_c1_t2.png)


(b) t=0.9t=0.9

Figure 10: Optimal trading regions at different times with Cmin=0.2C\_{\min}=0.2.

When the fixed cost increases from 0.020.02 to 0.20.2, several phenomena can be observed in Figure [10](https://arxiv.org/html/2510.21650v1#S8.F10 "Figure 10 ‣ 8.4 Higher fixed costs ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."):

1. (1)

   The continuation region becomes substantially wider. The higher fixed cost discourages trading activity, acting as a barrier to stock transactions. Consequently, the blue region in the upper left of Figure [10](https://arxiv.org/html/2510.21650v1#S8.F10 "Figure 10 ‣ 8.4 Higher fixed costs ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), corresponding to wealth levels below G1+G2+CminG\_{1}+G\_{2}+C\_{\min}, disappears, and the red region shrinks in size.
2. (2)

   The red vertical bar near x0=3.0x\_{0}=3.0 becomes considerably longer, indicating that it is now more common to reserve the cash amount required for the first goal.
3. (3)

   A higher fixed cost may either reduce or increase exposure to the stock, depending on the specific situation:

   * •

     For (x0,x1)=(6.0,0.0)(x\_{0},x\_{1})=(6.0,0.0) at t=0.9t=0.9, the target position is (x0,x1)=(0.0,5.98)(x\_{0},x\_{1})=(0.0,5.98) when Cmin=0.02C\_{\min}=0.02, as shown in Figure [5](https://arxiv.org/html/2510.21650v1#S8.F5 "Figure 5 ‣ 8.2.2 Time 𝑡=0.5 and 𝑡=0.9 ‣ 8.2 The benchmark case with 𝐶ₘᵢₙ=0.02 ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). In contrast, when Cmin=0.2C\_{\min}=0.2, Figure [10](https://arxiv.org/html/2510.21650v1#S8.F10 "Figure 10 ‣ 8.4 Higher fixed costs ‣ 8 Numerical analysis ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") shows that the target position from (6.03,0.0)(6.03,0.0) is around (3.05,2.77)(3.05,2.77), corresponding to a lower stock exposure.
   * •

     For (x0,x1)=(0.0,8.48)(x\_{0},x\_{1})=(0.0,8.48) in the upper-left region at t=0.9t=0.9, the higher cost case remains at the same position, while the lower cost case involves selling some stock. This illustrates a scenario where a higher fixed cost leads to higher stock exposure.

## Appendix A Proofs of the stochastic supersolution

Lemma [A.1](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") gives some useful properties of the minimum operator ℳ{\mathcal{M}}. The proof is similar to belak2022optimal and thus omitted.

###### Lemma A.1.

Let k=1,…,Kk=1,\ldots,K and f:[Tk−1,Tk]×𝒮¯→ℝf:[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}\rightarrow\mathbb{R}. Then:

1. (1)

   If ff is LSC, then ℳ​[f]∗​(t,x)=ℳ​[f]​(t,x){\mathcal{M}}[f]\_{\*}(t,x)={\mathcal{M}}[f](t,x) for all (t,x)∈[Tk−1,Tk]×𝒮¯(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}.
2. (2)

   If ff is USC, then ℳ​[f]∗​(t,x)=ℳ​[f]​(t,x){\mathcal{M}}[f]^{\*}(t,x)={\mathcal{M}}[f](t,x) for all (t,x)∈[Tk−1,Tk]×(𝒮¯∖𝒮∅¯)(t,x)\in[T\_{k-1},T\_{k}]\times(\overline{\mathcal{S}}\setminus\overline{{\mathcal{S}}\_{\emptyset}}).

###### Lemma A.2.

The upper stochastic envelope v+v\_{+} satisfies the viscosity subsolution property ([3.13](https://arxiv.org/html/2510.21650v1#S3.E13 "In item (3) ‣ Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) at TKT\_{K}, under Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proof.

Since vK,+v\_{K,+} is USC, it follows that vK,+∗=vK,+v^{\*}\_{K,+}=v\_{K,+}. For any x¯∈𝒮\bar{x}\in{\mathcal{S}}, we aim to prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  | max{\displaystyle\max\Big\{ | vK,+​(TK,x¯)−wK​[GK−x¯0−(x¯1−C​(−x¯1))+]+,\displaystyle v\_{K,+}(T\_{K},\bar{x})-w\_{K}\left[G\_{K}-\bar{x}\_{0}-(\bar{x}\_{1}-C(-\bar{x}\_{1}))^{+}\right]^{+}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | vK,+(TK,x¯)−ℳ[vK,+]∗(TK,x¯)}≤0.\displaystyle v\_{K,+}(T\_{K},\bar{x})-{\mathcal{M}}[v\_{K,+}]^{\*}(T\_{K},\bar{x})\Big\}\leq 0. |  |

Assume on the contrary that the left-hand side is strictly positive. There are two possible cases.

Case 1. vK,+​(TK,x¯)−wK​[GK−x¯0−(x¯1−C​(−x¯1))+]+>0v\_{K,+}(T\_{K},\bar{x})-w\_{K}\left[G\_{K}-\bar{x}\_{0}-(\bar{x}\_{1}-C(-\bar{x}\_{1}))^{+}\right]^{+}>0.

Since the terminal value is continuous in xx, there exists a small ε>0\varepsilon>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | vK,+​(TK,x¯)−wK​[GK−x0−(x1−C​(−x1))+]+≥ε,v\_{K,+}(T\_{K},\bar{x})-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}\geq\varepsilon, |  | (A.1) |

for x∈B​(x¯,ε)¯x\in\overline{B(\bar{x},\varepsilon)}, which is the closure of B​(x¯,ε):={x:|x−x¯|<ε}B(\bar{x},\varepsilon):=\{x:|x-\bar{x}|<\varepsilon\}.

For later use, define the sets

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟​(TK,x¯,ε)\displaystyle\mathcal{D}(T\_{K},\bar{x},\varepsilon) | :=(TK−ε,TK]×B​(x¯,ε),\displaystyle:=(T\_{K}-\varepsilon,T\_{K}]\times B(\bar{x},\varepsilon), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(ε)\displaystyle E(\varepsilon) | :=𝒟​(TK,x¯,ε)¯\𝒟​(TK,x¯,ε/2),\displaystyle:=\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}\backslash\mathcal{D}(T\_{K},\bar{x},\varepsilon/2), |  |

where 𝒟¯\overline{\mathcal{D}} denotes the closure of 𝒟\mathcal{D}.

Note that vK,+v\_{K,+} is USC and E​(ε)E(\varepsilon) is compact. Then vK,+v\_{K,+} is bounded from above on E​(ε)E(\varepsilon). For a small enough η>0\eta>0, we have

|  |  |  |
| --- | --- | --- |
|  | sup(t,x)∈E​(ε)vK,+​(t,x)−vK,+​(TK,x¯)<ε24​η−ε.\sup\_{(t,x)\in E(\varepsilon)}v\_{K,+}(t,x)-v\_{K,+}(T\_{K},\bar{x})<\frac{\varepsilon^{2}}{4\eta}-\varepsilon. |  |

As this inequality is strict, bayraktar2012linear and bayraktar2014Dynkin ensure that there exists vKnv^{n}\_{K}, which corresponds to a stochastic supersolution vn=(v1n,…,vKn)v^{n}=(v^{n}\_{1},\ldots,v^{n}\_{K}) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(t,x)∈E​(ε)vKn​(t,x)−vK,+​(TK,x¯)<ε24​η−ε.\sup\_{(t,x)\in E(\varepsilon)}v^{n}\_{K}(t,x)-v\_{K,+}(T\_{K},\bar{x})<\frac{\varepsilon^{2}}{4\eta}-\varepsilon. |  | (A.2) |

For p>0p>0, define

|  |  |  |
| --- | --- | --- |
|  | ψε,η,p​(t,x):=vK,+​(TK,x¯)+|x−x¯|2η+p​(TK−t).\psi^{\varepsilon,\eta,p}(t,x):=v\_{K,+}(T\_{K},\bar{x})+\frac{|x-\bar{x}|^{2}}{\eta}+p(T\_{K}-t). |  |

With a large enough pp, we can ensure that

|  |  |  |
| --- | --- | --- |
|  | ℒ​[ψε,η,p]​(t,x)>0 on ​𝒟​(TK,x¯,ε)¯.{\mathcal{L}}[\psi^{\varepsilon,\eta,p}](t,x)>0\quad\text{ on }\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  |

Thanks to the definition of E​(ε)E(\varepsilon), the inequality ([A.2](https://arxiv.org/html/2510.21650v1#A1.E2 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), and a large enough pp, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψε,η,p​(t,x)\displaystyle\psi^{\varepsilon,\eta,p}(t,x) | ≥vK,+​(TK,x¯)+ε24​η>ε+sup(t,x)∈E​(ε)vKn​(t,x)\displaystyle\geq v\_{K,+}(T\_{K},\bar{x})+\frac{\varepsilon^{2}}{4\eta}>\varepsilon+\sup\_{(t,x)\in E(\varepsilon)}v^{n}\_{K}(t,x) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥ε+vKn​(t,x) on ​E​(ε).\displaystyle\geq\varepsilon+v^{n}\_{K}(t,x)\quad\text{ on }E(\varepsilon). |  | (A.3) |

Besides, for any t≤TKt\leq T\_{K} and x∈B​(x¯,ε)¯x\in\overline{B(\bar{x},\varepsilon)}, ([A.1](https://arxiv.org/html/2510.21650v1#A1.E1 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψε,η,p​(t,x)\displaystyle\psi^{\varepsilon,\eta,p}(t,x) | ≥vK,+​(TK,x¯)\displaystyle\geq v\_{K,+}(T\_{K},\bar{x}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥wK​[GK−x0−(x1−C​(−x1))+]++ε.\displaystyle\geq w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}+\varepsilon. |  | (A.4) |

Let 0<δ<ε0<\delta<\varepsilon and set ψp,δ:=ψε,η,p−δ\psi^{p,\delta}:=\psi^{\varepsilon,\eta,p}-\delta. Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | vKp,δ​(t,x):={vKn​(t,x)∧ψp,δ​(t,x)on ​𝒟​(TK,x¯,ε)¯,vKn​(t,x),otherwise.v^{p,\delta}\_{K}(t,x):=\left\{\begin{array}[]{ c l }v^{n}\_{K}(t,x)\wedge\psi^{p,\delta}(t,x)&\text{on }\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)},\\ v^{n}\_{K}(t,x),&\text{otherwise}.\end{array}\right. |  | (A.5) |

Next, we show that (v1n,…,vK−1n,vKp,δ)(v^{n}\_{1},\ldots,v^{n}\_{K-1},v^{p,\delta}\_{K}) is a stochastic supersolution, which leads to the following contradiction:

|  |  |  |
| --- | --- | --- |
|  | vKp,δ​(TK,x¯)=vK,+​(TK,x¯)−δ<vK,+​(TK,x¯).v^{p,\delta}\_{K}(T\_{K},\bar{x})=v\_{K,+}(T\_{K},\bar{x})-\delta<v\_{K,+}(T\_{K},\bar{x}). |  |

Clearly, (v1n,…,vK−1n,vKp,δ)(v^{n}\_{1},\ldots,v^{n}\_{K-1},v^{p,\delta}\_{K}) satisfies Conditions (1) and (2) in Definition [4.1](https://arxiv.org/html/2510.21650v1#S4.Thmtheorem1 "Definition 4.1 (Stochastic supersolution). ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). For the supermartingale property in Definition [4.1](https://arxiv.org/html/2510.21650v1#S4.Thmtheorem1 "Definition 4.1 (Stochastic supersolution). ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") (3), we first verify it when the random initial condition (τ¯,ξ)(\bar{\tau},\xi) satisfies τ¯∈[TK−1,TK]\bar{\tau}\in[T\_{K-1},T\_{K}].

Define the event

|  |  |  |
| --- | --- | --- |
|  | A:={(τ¯,ξ)∈𝒟​(TK,x¯,ε/2)}∩{ψp,δ​(τ¯,ξ)<vKn​(τ¯,ξ)}.A:=\{(\bar{\tau},\xi)\in\mathcal{D}(T\_{K},\bar{x},\varepsilon/2)\}\cap\{\psi^{p,\delta}(\bar{\tau},\xi)<v^{n}\_{K}(\bar{\tau},\xi)\}. |  |

Then A∈ℱτ¯A\in{\mathcal{F}}\_{\bar{\tau}}.

Let U0:=(θK0,Λ0):=(L​(X​(TK;τ¯,ξ,∅,Λ0)),{(τn0,Δn0)}n=1∞)U^{0}:=(\theta^{0}\_{K},\Lambda^{0}):=(L(X(T\_{K};\bar{\tau},\xi,\emptyset,\Lambda^{0})),\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}) be a suitable control for vKnv^{n}\_{K} with the random initial condition (τ¯,ξ)(\bar{\tau},\xi). Here, we recall that {X​(t;τ¯,ξ,∅,Λ0)}t∈[τ¯,T]\{X(t;\bar{\tau},\xi,\emptyset,\Lambda^{0})\}\_{t\in[\bar{\tau},T]} denotes the solution where Λ0\Lambda^{0} is used while θK\theta\_{K} is not determined.

Define a new control U1:=(θK1,Λ1)U^{1}:=(\theta^{1}\_{K},\Lambda^{1}) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | θK1:=𝟏A​∅+𝟏Ac​θK0,Λ1={(τn1,Δn1)}n=1∞:=𝟏Ac​{(τn0,Δn0)}n=1∞.\theta^{1}\_{K}:=\mathbf{1}\_{A}\emptyset+\mathbf{1}\_{A^{c}}\theta^{0}\_{K},\quad\Lambda^{1}=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\}^{\infty}\_{n=1}:=\mathbf{1}\_{A^{c}}\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}. |  | (A.6) |

Here, if AA happens, we do not conduct any transactions between the stock and the bank account. The funding amount θK\theta\_{K} is also to be determined. Instead, if AcA^{c} happens, then vKp,δ​(τ¯,ξ)=vKn​(τ¯,ξ)v^{p,\delta}\_{K}(\bar{\tau},\xi)=v^{n}\_{K}(\bar{\tau},\xi). Hence, U1U^{1} follows a suitable control for vKnv^{n}\_{K}. Denote {X​(t;τ¯,ξ,U1)}t∈[τ¯,T]\{X(t;\bar{\tau},\xi,U^{1})\}\_{t\in[\bar{\tau},T]} as the solution of the state process with the random initial condition (τ¯,ξ)(\bar{\tau},\xi) under the control U1U^{1}. Then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(X​(t;τ¯,ξ,U1)∈𝒮¯,τ¯≤t≤T)=1.\mathbb{P}(X(t;\bar{\tau},\xi,U^{1})\in\overline{{\mathcal{S}}},\;\bar{\tau}\leq t\leq T)=1. |  |

Define the exit time and position as

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ′\displaystyle\tau^{\prime} | :=inf{t∈[τ¯,TK]|(t,X​(t;τ¯,ξ,U1))∉𝒟​(TK,x¯,ε/2)}∧TK,\displaystyle:=\inf\{t\in[\bar{\tau},T\_{K}]\,|\,(t,X(t;\bar{\tau},\xi,U^{1}))\notin\mathcal{D}(T\_{K},\bar{x},\varepsilon/2)\}\wedge T\_{K}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ′\displaystyle\xi^{\prime} | :=X​(τ′;τ¯,ξ,U1)∈ℱτ′.\displaystyle:=X(\tau^{\prime};\bar{\tau},\xi,U^{1})\in{\mathcal{F}}\_{\tau^{\prime}}. |  |

There is a suitable control U2:=(θK2,Λ2):=(L​(X​(TK;τ′,ξ′,∅,Λ2)),{(τn2,Δn2)}n=1∞)U^{2}:=(\theta^{2}\_{K},\Lambda^{2}):=(L(X(T\_{K};\tau^{\prime},\xi^{\prime},\emptyset,\Lambda^{2})),\{(\tau^{2}\_{n},\Delta^{2}\_{n})\}^{\infty}\_{n=1}) for vKnv^{n}\_{K} with the random initial condition (τ′,ξ′)(\tau^{\prime},\xi^{\prime}). This control U2U^{2} will only be used when τ′<TK\tau^{\prime}<T\_{K} happens. Finally, define a control U:=(θK,Λ)U:=(\theta\_{K},\Lambda) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ\displaystyle\Lambda | :={(τn1,Δn1)​𝟏{τn1≤τ′}}n=1∞+{(τn2,Δn2)​𝟏{τ′≤τn2}∩{τ′<TK}}n=1∞,\displaystyle:=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\mathbf{1}\_{\{\tau^{1}\_{n}\leq\tau^{\prime}\}}\}^{\infty}\_{n=1}+\{(\tau^{2}\_{n},\Delta^{2}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{2}\_{n}\}\cap\{\tau^{\prime}<T\_{K}\}}\}^{\infty}\_{n=1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θK\displaystyle\theta\_{K} | :=L​(X​(TK;τ¯,ξ,∅,Λ)).\displaystyle:=L(X(T\_{K};\bar{\tau},\xi,\emptyset,\Lambda)). |  |

The control UU satisfies

|  |  |  |
| --- | --- | --- |
|  | ℙ​(X​(t;τ¯,ξ,U)∈𝒮¯,τ¯≤t≤T)=1.\mathbb{P}(X(t;\bar{\tau},\xi,U)\in\overline{{\mathcal{S}}},\;\bar{\tau}\leq t\leq T)=1. |  |

We verify that UU is suitable for vKp,δv^{p,\delta}\_{K} with (τ¯,ξ)(\bar{\tau},\xi).

Consider a stopping time ρ∈[τ¯,TK]\rho\in[\bar{\tau},T\_{K}]. Applying the Itô’s formula to ψp,δ\psi^{p,\delta} from τ\tau to ρ∧τ′\rho\wedge\tau^{\prime} under the event AA and control U1U^{1}, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​vKp,δ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A}v^{p,\delta}\_{K}(\bar{\tau},\xi) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏A​ψp,δ​(τ¯,ξ)\displaystyle=\mathbf{1}\_{A}\psi^{p,\delta}(\bar{\tau},\xi) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏A​ψp,δ​(τ¯,X​(τ¯;τ¯,ξ,U1))\displaystyle=\mathbf{1}\_{A}\psi^{p,\delta}(\bar{\tau},X(\bar{\tau};\bar{\tau},\xi,U^{1})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥𝔼​[𝟏A∩{ρ<τ′}​ψp,δ​(ρ,X​(ρ;τ¯,ξ,U1))+𝟏A∩{ρ≥τ′}​ψp,δ​(τ′,ξ′)|ℱτ¯].\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\rho<\tau^{\prime}\}}\psi^{p,\delta}(\rho,X(\rho;\bar{\tau},\xi,U^{1}))+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}}\psi^{p,\delta}(\tau^{\prime},\xi^{\prime})\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  | (A.7) |

Moreover, ([A.3](https://arxiv.org/html/2510.21650v1#A1.E3 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([A.4](https://arxiv.org/html/2510.21650v1#A1.E4 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) lead to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝟏A∩{ρ≥τ′}​ψp,δ​(τ′,ξ′)≥\displaystyle\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}}\psi^{p,\delta}(\tau^{\prime},\xi^{\prime})\geq | 𝟏A∩{ρ≥τ′}∩{τ′<TK}​vKn​(τ′,ξ′)\displaystyle\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{K}\}}v^{n}\_{K}(\tau^{\prime},\xi^{\prime}) |  | (A.8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏A∩{ρ≥τ′}∩{τ′=TK}​wK​(GK−ξ0′−(ξ1′−C​(−ξ1′))+)+.\displaystyle+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}}w\_{K}(G\_{K}-\xi^{\prime}\_{0}-(\xi^{\prime}\_{1}-C(-\xi^{\prime}\_{1}))^{+})^{+}. |  |

Combining ([A.7](https://arxiv.org/html/2510.21650v1#A1.E7 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([A.8](https://arxiv.org/html/2510.21650v1#A1.E8 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), since vKp,δ≤ψp,δv^{p,\delta}\_{K}\leq\psi^{p,\delta} on 𝒟​(TK,x¯,ε)¯\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​vKp,δ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A}v^{p,\delta}\_{K}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥𝔼[𝟏A∩{ρ<τ′}vKp,δ(ρ,X(ρ;τ¯,ξ,U1))\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\rho<\tau^{\prime}\}}v^{p,\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,U^{1})) |  | (A.9) |
|  |  |  |
| --- | --- | --- |
|  | +𝟏A∩{ρ≥τ′}∩{τ′<TK}​vKn​(τ′,ξ′)\displaystyle\qquad+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{K}\}}v^{n}\_{K}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏A∩{ρ≥τ′}∩{τ′=TK}wK(GK−ξ0′−(ξ1′−C(−ξ1′))+)+|ℱτ¯]\displaystyle\qquad+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}}w\_{K}(G\_{K}-\xi^{\prime}\_{0}-(\xi^{\prime}\_{1}-C(-\xi^{\prime}\_{1}))^{+})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼[𝟏A∩{ρ<τ′}vKp,δ(ρ,X(ρ;τ¯,ξ,U))\displaystyle=\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\rho<\tau^{\prime}\}}v^{p,\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,U)) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏A∩{ρ≥τ′}∩{τ′<TK}vKn(τ′,ξ′)+𝟏A∩{ρ≥τ′}∩{τ′=TK}wK(GK−θK)+|ℱτ¯].\displaystyle\qquad+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{K}\}}v^{n}\_{K}(\tau^{\prime},\xi^{\prime})+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

In the last equality, we use the definition of UU and the fact that θK=L​(ξ′)\theta\_{K}=L(\xi^{\prime}) under the event A∩{ρ≥τ′}∩{τ′=TK}A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}.

Under the event AcA^{c}, because U1U^{1} is a suitable control for vKnv^{n}\_{K} with the random initial condition (τ¯,ξ)(\bar{\tau},\xi), we have

|  |  |  |
| --- | --- | --- |
|  | 𝟏Ac​vKp,δ​(τ¯,ξ)=𝟏Ac​vKn​(τ¯,ξ)\displaystyle\mathbf{1}\_{A^{c}}v^{p,\delta}\_{K}(\bar{\tau},\xi)=\mathbf{1}\_{A^{c}}v^{n}\_{K}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥𝔼[𝟏Ac∩{ρ<τ′}vKn(ρ,X(ρ;τ¯,ξ,U1))\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A^{c}\cap\{\rho<\tau^{\prime}\}}v^{n}\_{K}(\rho,X(\rho;\bar{\tau},\xi,U^{1})) |  | (A.10) |
|  |  |  |
| --- | --- | --- |
|  | +𝟏Ac∩{ρ≥τ′}∩{τ′<TK}vKn(τ′,ξ′)+𝟏Ac∩{ρ≥τ′}∩{τ′=TK}wK(GK−θK1)+|ℱτ¯]\displaystyle\qquad+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{K}\}}v^{n}\_{K}(\tau^{\prime},\xi^{\prime})+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}}w\_{K}(G\_{K}-\theta^{1}\_{K})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼[𝟏Ac∩{ρ<τ′}vKn(ρ,X(ρ;τ¯,ξ,U))\displaystyle=\mathbb{E}\Big[\mathbf{1}\_{A^{c}\cap\{\rho<\tau^{\prime}\}}v^{n}\_{K}(\rho,X(\rho;\bar{\tau},\xi,U)) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏Ac∩{ρ≥τ′}∩{τ′<TK}vKn(τ′,ξ′)+𝟏Ac∩{ρ≥τ′}∩{τ′=TK}wK(GK−θK)+|ℱτ¯].\displaystyle\qquad+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{K}\}}v^{n}\_{K}(\tau^{\prime},\xi^{\prime})+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

Here, we use θK1=θK\theta^{1}\_{K}=\theta\_{K} under Ac∩{ρ≥τ′}∩{τ′=TK}A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}. As vKn≥vKp,δv^{n}\_{K}\geq v^{p,\delta}\_{K} everywhere, the definition of UU, ([A.9](https://arxiv.org/html/2510.21650v1#A1.E9 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), and ([A.10](https://arxiv.org/html/2510.21650v1#A1.E10 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) yield

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vKp,δ(τ¯,ξ)≥𝔼[\displaystyle v^{p,\delta}\_{K}(\bar{\tau},\xi)\geq\mathbb{E}\Big[ | 𝟏{ρ<τ′}​vKp,δ​(ρ,X​(ρ;τ¯,ξ,U))\displaystyle\mathbf{1}\_{\{\rho<\tau^{\prime}\}}v^{p,\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,U)) |  | (A.11) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏{ρ≥τ′}∩{τ′<TK}vKn(τ′,ξ′)+𝟏{ρ≥τ′}∩{τ′=TK}wK(GK−θK)+|ℱτ¯].\displaystyle+\mathbf{1}\_{\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{K}\}}v^{n}\_{K}(\tau^{\prime},\xi^{\prime})+\mathbf{1}\_{\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

Since U2U^{2} is a suitable control for vKnv^{n}\_{K} with the random initial condition (τ′,ξ′)(\tau^{\prime},\xi^{\prime}), ([A.11](https://arxiv.org/html/2510.21650v1#A1.E11 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and the definition of UU yield the desired result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vKp,δ(τ¯,ξ)≥𝔼[\displaystyle v^{p,\delta}\_{K}(\bar{\tau},\xi)\geq\mathbb{E}\Big[ | 𝟏{τ¯≤ρ<TK}vKp,δ(ρ,X(ρ;τ¯,ξ,U))+𝟏{ρ=TK}wK(GK−θK)+|ℱτ¯].\displaystyle\mathbf{1}\_{\{\bar{\tau}\leq\rho<T\_{K}\}}v^{p,\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,U))+\mathbf{1}\_{\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

It is direct to verify the supermartingale property when τ∈[Tk−1,Tk]\tau\in[T\_{k-1},T\_{k}], k≠Kk\neq K. We omit it here.

Case 2. vK,+​(TK,x¯)−ℳ​[vK,+]∗​(TK,x¯)>0v\_{K,+}(T\_{K},\bar{x})-{\mathcal{M}}[v\_{K,+}]^{\*}(T\_{K},\bar{x})>0.

Because ℳ​[vK,+]∗​(TK,x){\mathcal{M}}[v\_{K,+}]^{\*}(T\_{K},x) equals to infinity when x∈𝒮∅x\in{\mathcal{S}}\_{\emptyset}, we should have x¯∉𝒮∅\bar{x}\notin{\mathcal{S}}\_{\emptyset}. Moreover, if x¯∈∂𝒮∅\bar{x}\in\partial{\mathcal{S}}\_{\emptyset}, then there exists a sequence {xk}k=1∞⊂𝒮∅\{x\_{k}\}^{\infty}\_{k=1}\subset{\mathcal{S}}\_{\emptyset} and xk→x¯x\_{k}\rightarrow\bar{x} when k→∞k\rightarrow\infty, such that ℳ​[vK,+]∗​(TK,x¯){\mathcal{M}}[v\_{K,+}]^{\*}(T\_{K},\bar{x}) equals to infinity. It implies that x¯∉∂𝒮∅\bar{x}\notin\partial{\mathcal{S}}\_{\emptyset}. Therefore, we have x¯∈𝒮¯∖𝒮∅¯\bar{x}\in\overline{\mathcal{S}}\setminus\overline{{\mathcal{S}}\_{\emptyset}} and ℳ​[vK,+]∗​(TK,x¯)=ℳ​[vK,+]​(TK,x¯){\mathcal{M}}[v\_{K,+}]^{\*}(T\_{K},\bar{x})={\mathcal{M}}[v\_{K,+}](T\_{K},\bar{x}) by Lemma [A.1](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Since vK,+​(TK,x¯)−ℳ​[vK,+]​(TK,x¯)>0v\_{K,+}(T\_{K},\bar{x})-{\mathcal{M}}[v\_{K,+}](T\_{K},\bar{x})>0 and ℳ​[vK,+]{\mathcal{M}}[v\_{K,+}] is USC when (t,x)∈[TK−1,TK]×(𝒮¯∖𝒮¯∅)(t,x)\in[T\_{K-1},T\_{K}]\times(\overline{\mathcal{S}}\setminus\overline{{\mathcal{S}}}\_{\emptyset}), there exists ε>0\varepsilon>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | vK,+​(TK,x¯)−ℳ​[vK,+]​(t,x)≥ε,(t,x)∈𝒟​(TK,x¯,ε)¯.v\_{K,+}(T\_{K},\bar{x})-{\mathcal{M}}[v\_{K,+}](t,x)\geq\varepsilon,\quad(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  | (A.12) |

Suppose B​(x¯,ε)⊂𝒮¯∖𝒮∅¯B(\bar{x},\varepsilon)\subset\overline{\mathcal{S}}\setminus\overline{{\mathcal{S}}\_{\emptyset}} by choosing ε\varepsilon small, which implies that D​(x)≠∅D(x)\neq\emptyset for all x∈B​(x¯,ε)x\in B(\bar{x},\varepsilon). Note that after any admissible transaction Δ\Delta, the total wealth is reduced by at least CminC\_{\min}. We can further assume that the radius ε>0\varepsilon>0 is small enough, such that the rebalancing position Γ​(x,Δ)\Gamma(x,\Delta) is out of B​(x¯,ε)B(\bar{x},\varepsilon) for all x∈B​(x¯,ε)x\in B(\bar{x},\varepsilon) and Δ∈D​(x)\Delta\in D(x).

Denote the set of all positions that can be reached by x∈B​(x¯,ε)¯x\in\overline{B(\bar{x},\varepsilon)} as

|  |  |  |
| --- | --- | --- |
|  | IΓ:={Γ​(x,Δ)|x∈B​(x¯,ε)¯​ and ​Δ∈D​(x)}.I\_{\Gamma}:=\big\{\Gamma(x,\Delta)\;\big|\;x\in\overline{B(\bar{x},\varepsilon)}\text{ and }\Delta\in D(x)\big\}. |  |

By Dini’s argument, for δ′>0\delta^{\prime}>0, there exists a stochastic supersolution vKnv^{n}\_{K} such that

|  |  |  |
| --- | --- | --- |
|  | 0≤vKn​(t,x)−vK,+​(t,x)≤δ′,(t,x)∈[TK−ε,TK]×IΓ¯.0\leq v^{n}\_{K}(t,x)-v\_{K,+}(t,x)\leq\delta^{\prime},\quad(t,x)\in[T\_{K}-\varepsilon,T\_{K}]\times\overline{I\_{\Gamma}}. |  |

We can prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤ℳ​[vKn]​(t,x)−ℳ​[vK,+]​(t,x)≤δ′,(t,x)∈𝒟​(TK,x¯,ε)¯.0\leq{\mathcal{M}}[v^{n}\_{K}](t,x)-{\mathcal{M}}[v\_{K,+}](t,x)\leq\delta^{\prime},\quad(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  | (A.13) |

Define ψ​(t,x):=vK,+​(TK,x¯)\psi(t,x):=v\_{K,+}(T\_{K},\bar{x}). With ([A.12](https://arxiv.org/html/2510.21650v1#A1.E12 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([A.13](https://arxiv.org/html/2510.21650v1#A1.E13 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), we obtain

|  |  |  |
| --- | --- | --- |
|  | ψ​(t,x)−ℳ​[vKn]​(t,x)≥ε−δ′,(t,x)∈𝒟​(TK,x¯,ε)¯.\displaystyle\psi(t,x)-{\mathcal{M}}[v^{n}\_{K}](t,x)\geq\varepsilon-\delta^{\prime},\quad(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  |

By rieder1978measurable, for δ′′>0\delta^{\prime\prime}>0, there exists a Borel measurable δ′′\delta^{\prime\prime}-minimizer for ℳ​[vKn]​(t,x){\mathcal{M}}[v^{n}\_{K}](t,x) on 𝒟​(TK,x¯,ε)¯\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}, denoted as Δ∗​(t,x)\Delta^{\*}(t,x), such that

|  |  |  |
| --- | --- | --- |
|  | ℳ​[vKn]​(t,x)≥vKn​(t,Γ​(x,Δ∗​(t,x)))−δ′′,(t,x)∈𝒟​(TK,x¯,ε)¯.{\mathcal{M}}[v^{n}\_{K}](t,x)\geq v^{n}\_{K}(t,\Gamma(x,\Delta^{\*}(t,x)))-\delta^{\prime\prime},\quad(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  |

If we take δ′=δ′′=ε/4\delta^{\prime}=\delta^{\prime\prime}=\varepsilon/4, then

|  |  |  |
| --- | --- | --- |
|  | ψ​(t,x)≥vKn​(t,Γ​(x,Δ∗​(t,x)))+ε/2,(t,x)∈𝒟​(TK,x¯,ε)¯.\psi(t,x)\geq v^{n}\_{K}(t,\Gamma(x,\Delta^{\*}(t,x)))+\varepsilon/2,\quad(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  |

Let 0<η<ε/20<\eta<\varepsilon/2 and set ψη​(t,x):=ψ​(t,x)−η\psi^{\eta}(t,x):=\psi(t,x)-\eta. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψη​(t,x)≥vKn​(t,Γ​(x,Δ∗​(t,x))),(t,x)∈𝒟​(TK,x¯,ε)¯.\psi^{\eta}(t,x)\geq v^{n}\_{K}(t,\Gamma(x,\Delta^{\*}(t,x))),\quad(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  | (A.14) |

Define

|  |  |  |
| --- | --- | --- |
|  | vKη​(t,x):={vKn​(t,x)∧ψη​(t,x)on ​𝒟​(TK,x¯,ε)¯,vKn​(t,x),otherwise.v^{\eta}\_{K}(t,x):=\left\{\begin{array}[]{ c l }v^{n}\_{K}(t,x)\wedge\psi^{\eta}(t,x)&\text{on }\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)},\\ v^{n}\_{K}(t,x),&\text{otherwise}.\end{array}\right. |  |

We verify the supermartingale property in Definition [4.1](https://arxiv.org/html/2510.21650v1#S4.Thmtheorem1 "Definition 4.1 (Stochastic supersolution). ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") (3) when the random initial condition (τ¯,ξ)(\bar{\tau},\xi) satisfies τ¯∈[TK−1,TK]\bar{\tau}\in[T\_{K-1},T\_{K}].

Similarly, define the event

|  |  |  |
| --- | --- | --- |
|  | A:={(τ¯,ξ)∈𝒟​(TK,x¯,ε/2)}∩{ψη​(τ¯,ξ)<vKn​(τ¯,ξ)}.A:=\{(\bar{\tau},\xi)\in\mathcal{D}(T\_{K},\bar{x},\varepsilon/2)\}\cap\{\psi^{\eta}(\bar{\tau},\xi)<v^{n}\_{K}(\bar{\tau},\xi)\}. |  |

Let U0:=(θK0,Λ0):=(L​(X​(TK;τ¯,ξ,∅,Λ0)),{(τn0,Δn0)}n=1∞)U^{0}:=(\theta^{0}\_{K},\Lambda^{0}):=(L(X(T\_{K};\bar{\tau},\xi,\emptyset,\Lambda^{0})),\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}) be a suitable control for vKnv^{n}\_{K} with the random initial condition (τ¯,ξ)(\bar{\tau},\xi). Define a new control U1:=(θK1,Λ1)U^{1}:=(\theta^{1}\_{K},\Lambda^{1}) by

|  |  |  |
| --- | --- | --- |
|  | θK1:=𝟏A​∅+𝟏Ac​θK0,Λ1:={(τn1,Δn1)}n=1∞:=𝟏A​(τ¯,Δ∗​(τ¯,ξ))+𝟏Ac​{(τn0,Δn0)}n=1∞.\theta^{1}\_{K}:=\mathbf{1}\_{A}\emptyset+\mathbf{1}\_{A^{c}}\theta^{0}\_{K},\quad\Lambda^{1}:=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\}^{\infty}\_{n=1}:=\mathbf{1}\_{A}(\bar{\tau},\Delta^{\*}(\bar{\tau},\xi))+\mathbf{1}\_{A^{c}}\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}. |  |

Let

|  |  |  |
| --- | --- | --- |
|  | τ′:=inf{t∈[τ¯,TK]|(t,X​(t;τ¯,ξ,U1))∉𝒟​(TK,x¯,ε/2)}∧TK\displaystyle\tau^{\prime}:=\inf\{t\in[\bar{\tau},T\_{K}]\,|\,(t,X(t;\bar{\tau},\xi,U^{1}))\notin\mathcal{D}(T\_{K},\bar{x},\varepsilon/2)\}\wedge T\_{K} |  |

be the exit time and ξ′:=X​(τ′;τ¯,ξ,U1)∈ℱτ′\xi^{\prime}:=X(\tau^{\prime};\bar{\tau},\xi,U^{1})\in{\mathcal{F}}\_{\tau^{\prime}} be the exit position.

There is a suitable control U2:=(θK2,Λ2):=(L​(X​(TK;τ′,ξ′,∅,Λ2)),{(τn2,Δn2)}n=1∞)U^{2}:=(\theta^{2}\_{K},\Lambda^{2}):=(L(X(T\_{K};\tau^{\prime},\xi^{\prime},\emptyset,\Lambda^{2})),\{(\tau^{2}\_{n},\Delta^{2}\_{n})\}^{\infty}\_{n=1}) for vKnv^{n}\_{K} with the random initial condition (τ′,ξ′)(\tau^{\prime},\xi^{\prime}). This control will only be used when Ac∩{τ′<TK}A^{c}\cap\{\tau^{\prime}<T\_{K}\} or AA happens. Finally, define a control U:=(θK,Λ)U:=(\theta\_{K},\Lambda) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ\displaystyle\Lambda | :={(τn1,Δn1)​𝟏{τn1≤τ′}}n=1∞+{(τn2,Δn2)​𝟏{τ′≤τn2}∩{Ac∩{τ′<TK}​ or ​A}}n=1∞,\displaystyle:=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\mathbf{1}\_{\{\tau^{1}\_{n}\leq\tau^{\prime}\}}\}^{\infty}\_{n=1}+\{(\tau^{2}\_{n},\Delta^{2}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{2}\_{n}\}\cap\{A^{c}\cap\{\tau^{\prime}<T\_{K}\}\text{ or }A\}}\}^{\infty}\_{n=1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θK\displaystyle\theta\_{K} | :=L​(X​(TK;τ¯,ξ,∅,Λ)).\displaystyle:=L(X(T\_{K};\bar{\tau},\xi,\emptyset,\Lambda)). |  |

We verify that UU is suitable for vKηv^{\eta}\_{K} with (τ¯,ξ)(\bar{\tau},\xi).

Consider a stopping time ρ∈[τ¯,TK]\rho\in[\bar{\tau},T\_{K}]. Under the event AA and control U1U^{1}, ([A.14](https://arxiv.org/html/2510.21650v1#A1.E14 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) leads to

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​vKη​(τ¯,ξ)=𝟏A​ψη​(τ¯,ξ)≥𝟏A​vKn​(τ¯,Γ​(ξ,Δ∗​(τ¯,ξ)))=𝟏A​vKn​(τ′,ξ′).\mathbf{1}\_{A}v^{\eta}\_{K}(\bar{\tau},\xi)=\mathbf{1}\_{A}\psi^{\eta}(\bar{\tau},\xi)\geq\mathbf{1}\_{A}v^{n}\_{K}(\bar{\tau},\Gamma(\xi,\Delta^{\*}(\bar{\tau},\xi)))=\mathbf{1}\_{A}v^{n}\_{K}(\tau^{\prime},\xi^{\prime}). |  |

Here, we note that the rebalancing position Γ​(ξ,Δ∗​(τ¯,ξ))\Gamma(\xi,\Delta^{\*}(\bar{\tau},\xi)) exits B​(x¯,ε)B(\bar{x},\varepsilon) immediately and hence τ′=τ¯\tau^{\prime}=\bar{\tau}. Since U2U^{2} is a suitable control for vKnv^{n}\_{K} with (τ′,ξ′)(\tau^{\prime},\xi^{\prime}), we have

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​vKn​(τ′,ξ′)\displaystyle\mathbf{1}\_{A}v^{n}\_{K}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥𝔼​[𝟏A∩{τ¯≤ρ<TK}​vKn​(ρ,X​(ρ;τ′,ξ′,U2))+𝟏A∩{ρ=TK}​wK​(GK−θK2)+|ℱτ¯]\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\bar{\tau}\leq\rho<T\_{K}\}}v^{n}\_{K}(\rho,X(\rho;\tau^{\prime},\xi^{\prime},U^{2}))+\mathbf{1}\_{A\cap\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta^{2}\_{K})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big] |  | (A.15) |
|  |  |  |
| --- | --- | --- |
|  | ≥𝔼​[𝟏A∩{τ¯≤ρ<TK}​vKη​(ρ,X​(ρ;τ¯,ξ,U))+𝟏A∩{ρ=TK}​wK​(GK−θK)+|ℱτ¯].\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\bar{\tau}\leq\rho<T\_{K}\}}v^{\eta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,U))+\mathbf{1}\_{A\cap\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

The second inequality uses the definition of UU and the fact that vKn≥vKηv^{n}\_{K}\geq v^{\eta}\_{K} everywhere.

For the AcA^{c} case, we apply the control U2U^{2} on Ac∩{τ′<TK}A^{c}\cap\{\tau^{\prime}<T\_{K}\} after obtaining the counterpart inequality of ([A.10](https://arxiv.org/html/2510.21650v1#A1.E10 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")). Combining with ([A.15](https://arxiv.org/html/2510.21650v1#A1.E15 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), the result follows as desired.

It is direct to verify the supermartingale property when τ∈[Tk−1,Tk]\tau\in[T\_{k-1},T\_{k}], k≠Kk\neq K. We omit the detail.
∎

###### Lemma A.3.

The upper stochastic envelope v+v\_{+} satisfies the viscosity subsolution property ([3.12](https://arxiv.org/html/2510.21650v1#S3.E12 "In item (2) ‣ Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) at TkT\_{k}, k=1,…,K−1k=1,\ldots,K-1, under Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proof.

As vk,+v\_{k,+} is USC, we obtain vk,+∗=vk,+v^{\*}\_{k,+}=v\_{k,+}. Assume on the contrary that, there exists x¯∈𝒮\bar{x}\in{\mathcal{S}}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | max{\displaystyle\max\Big\{ | vk,+​(Tk,x¯)−inf0≤θk≤x¯0[wk​(Gk−θk)++vk+1,+​(Tk,x¯0−θk,x¯1)],\displaystyle v\_{k,+}(T\_{k},\bar{x})-\inf\_{0\leq\theta\_{k}\leq\bar{x}\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,+}(T\_{k},\bar{x}\_{0}-\theta\_{k},\bar{x}\_{1})\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | vk,+(Tk,x¯)−ℳ[vk,+]∗(Tk,x¯)}>0.\displaystyle v\_{k,+}(T\_{k},\bar{x})-{\mathcal{M}}[v\_{k,+}]^{\*}(T\_{k},\bar{x})\Big\}>0. |  |

Case 1. vk,+​(Tk,x¯)−inf0≤θk≤x¯0[wk​(Gk−θk)++vk+1,+​(Tk,x¯0−θk,x¯1)]>0v\_{k,+}(T\_{k},\bar{x})-\inf\_{0\leq\theta\_{k}\leq\bar{x}\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,+}(T\_{k},\bar{x}\_{0}-\theta\_{k},\bar{x}\_{1})\right]>0.

By aliprantis2006infinite, the function given by

|  |  |  |
| --- | --- | --- |
|  | (x0,x1)↦inf0≤θk≤x0[wk​(Gk−θk)++vk+1,+​(Tk,x0−θk,x1)](x\_{0},x\_{1})\mapsto\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,+}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right] |  |

is USC. Then there exists ε>0\varepsilon>0 small enough, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | vk,+​(Tk,x¯)−inf0≤θk≤x0[wk​(Gk−θk)++vk+1,+​(Tk,x0−θk,x1)]≥ε, for ​x∈B​(x¯,ε)¯.v\_{k,+}(T\_{k},\bar{x})-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,+}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right]\geq\varepsilon,\quad\text{ for }x\in\overline{B(\bar{x},\varepsilon)}. |  | (A.16) |

We introduce the set of positions that can be reached by withdrawing θk\theta\_{k}:

|  |  |  |
| --- | --- | --- |
|  | Iθ:={(x0−θk,x1)|x∈B​(x¯,ε)¯​ and ​0≤θk≤x0}.I\_{\theta}:=\big\{(x\_{0}-\theta\_{k},x\_{1})\big|x\in\overline{B(\bar{x},\varepsilon)}\text{ and }0\leq\theta\_{k}\leq x\_{0}\big\}. |  |

By bayraktar2012linear, there exists a nonincreasing sequence of stochastic supersolutions vk+1n↘vk+1,+v^{n}\_{k+1}\searrow v\_{k+1,+}. Moreover, every vk+1nv^{n}\_{k+1} has a corresponding stochastic supersolution vn=(v1n,…,vKn)v^{n}=(v^{n}\_{1},\ldots,v^{n}\_{K}). By bayraktar2014Dynkin, for δ′>0\delta^{\prime}>0, there exists a large enough n1n\_{1} such that

|  |  |  |
| --- | --- | --- |
|  | 0≤vk+1n1​(Tk,x)−vk+1,+​(Tk,x)≤δ′,x∈Iθ¯.0\leq v^{n\_{1}}\_{k+1}(T\_{k},x)-v\_{k+1,+}(T\_{k},x)\leq\delta^{\prime},\quad x\in\overline{I\_{\theta}}. |  |

By a minimizing sequence argument, we can show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | vk,+​(Tk,x¯)−inf0≤θk≤x0[wk​(Gk−θk)++vk+1n1​(Tk,x0−θk,x1)]≥ε−δ′, for ​x∈B​(x¯,ε)¯.v\_{k,+}(T\_{k},\bar{x})-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v^{n\_{1}}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right]\geq\varepsilon-\delta^{\prime},\;\text{ for }x\in\overline{B(\bar{x},\varepsilon)}. |  | (A.17) |

Besides, vk+1n1v^{n\_{1}}\_{k+1} corresponds to a stochastic supersolution vn1=(v1n1,…v^{n\_{1}}=(v^{n\_{1}}\_{1},\ldots, vKn1)v^{n\_{1}}\_{K}).

With a slight abuse of notation, we define sets

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟​(Tk,x¯,ε)\displaystyle\mathcal{D}(T\_{k},\bar{x},\varepsilon) | :=(Tk−ε,Tk]×B​(x¯,ε),\displaystyle:=(T\_{k}-\varepsilon,T\_{k}]\times B(\bar{x},\varepsilon), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(ε)\displaystyle E(\varepsilon) | :=𝒟​(Tk,x¯,ε)¯\𝒟​(Tk,x¯,ε/2).\displaystyle:=\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}\backslash\mathcal{D}(T\_{k},\bar{x},\varepsilon/2). |  |

Similar to Lemma [A.2](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), for a small η>0\eta>0, we can find vkn2v^{n\_{2}}\_{k}, which corresponds to a stochastic supersolution vn2=(v1n2,…,vKn2)v^{n\_{2}}=(v^{n\_{2}}\_{1},\ldots,v^{n\_{2}}\_{K}), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(t,x)∈E​(ε)vkn2​(t,x)−vk,+​(Tk,x¯)<ε24​η−ε.\sup\_{(t,x)\in E(\varepsilon)}v^{n\_{2}}\_{k}(t,x)-v\_{k,+}(T\_{k},\bar{x})<\frac{\varepsilon^{2}}{4\eta}-\varepsilon. |  | (A.18) |

Finally, we take

|  |  |  |
| --- | --- | --- |
|  | vn:=(v1n,…,vKn):=(v1n1∧v1n2,…,vKn1∧vKn2),v^{n}:=(v^{n}\_{1},\ldots,v^{n}\_{K}):=(v^{n\_{1}}\_{1}\wedge v^{n\_{2}}\_{1},\ldots,v^{n\_{1}}\_{K}\wedge v^{n\_{2}}\_{K}), |  |

which is a stochastic supersolution by Lemma [4.2](https://arxiv.org/html/2510.21650v1#S4.Thmtheorem2 "Lemma 4.2. ‣ 4 Stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). The inequalities ([A.17](https://arxiv.org/html/2510.21650v1#A1.E17 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([A.18](https://arxiv.org/html/2510.21650v1#A1.E18 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) also hold for vk+1nv^{n}\_{k+1} and vknv^{n}\_{k}, respectively.

By rieder1978measurable, for δ′′>0\delta^{\prime\prime}>0, there exists a Borel measurable δ′′\delta^{\prime\prime}-minimizer θk∗​(x)\theta^{\*}\_{k}(x), such that

|  |  |  |
| --- | --- | --- |
|  | inf0≤θk≤x0[wk​(Gk−θk)++vk+1n​(Tk,x0−θk,x1)]\displaystyle\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v^{n}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥wk​(Gk−θk∗​(x))++vk+1n​(Tk,x0−θk∗​(x),x1)−δ′′,x∈𝒮¯.\displaystyle\quad\geq w\_{k}(G\_{k}-\theta^{\*}\_{k}(x))^{+}+v^{n}\_{k+1}(T\_{k},x\_{0}-\theta^{\*}\_{k}(x),x\_{1})-\delta^{\prime\prime},\quad x\in\overline{{\mathcal{S}}}. |  | (A.19) |

With p>0p>0, we introduce

|  |  |  |
| --- | --- | --- |
|  | ψε,η,p​(t,x):=vk,+​(Tk,x¯)+|x−x¯|2η+p​(Tk−t).\psi^{\varepsilon,\eta,p}(t,x):=v\_{k,+}(T\_{k},\bar{x})+\frac{|x-\bar{x}|^{2}}{\eta}+p(T\_{k}-t). |  |

Let δ′=δ′′=ε/4\delta^{\prime}=\delta^{\prime\prime}=\varepsilon/4 and 0<δ<ε20<\delta<\frac{\varepsilon}{2}. Define ψp,δ:=ψε,η,p−δ\psi^{p,\delta}:=\psi^{\varepsilon,\eta,p}-\delta. With a large enough p>0p>0, we can ensure that ψp,δ\psi^{p,\delta} satisfies the following properties:

* •

  ℒ​[ψp,δ]​(t,x)>0 on ​𝒟​(Tk,x¯,ε)¯{\mathcal{L}}[\psi^{p,\delta}](t,x)>0\quad\text{ on }\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}.
* •

  By ([A.18](https://arxiv.org/html/2510.21650v1#A1.E18 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and the definition of vknv^{n}\_{k},

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψp,δ​(t,x)≥vkn​(t,x) on ​E​(ε).\psi^{p,\delta}(t,x)\geq v^{n}\_{k}(t,x)\quad\text{ on }E(\varepsilon). |  | (A.20) |
* •

  By ([A.16](https://arxiv.org/html/2510.21650v1#A1.E16 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), ([A.17](https://arxiv.org/html/2510.21650v1#A1.E17 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), and ([A.19](https://arxiv.org/html/2510.21650v1#A1.E19 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")),

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψp,δ​(t,x)≥wk​(Gk−θk∗​(x))++vk+1n​(Tk,x0−θk∗​(x),x1),(t,x)∈𝒟​(Tk,x¯,ε)¯.\psi^{p,\delta}(t,x)\geq w\_{k}(G\_{k}-\theta^{\*}\_{k}(x))^{+}+v^{n}\_{k+1}(T\_{k},x\_{0}-\theta^{\*}\_{k}(x),x\_{1}),\quad(t,x)\in\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}. |  | (A.21) |

Hence, we define

|  |  |  |
| --- | --- | --- |
|  | vkp,δ​(t,x):={vkn​(t,x)∧ψp,δ​(t,x)on ​𝒟​(Tk,x¯,ε)¯,vkn​(t,x),otherwise.v^{p,\delta}\_{k}(t,x):=\left\{\begin{array}[]{ c l }v^{n}\_{k}(t,x)\wedge\psi^{p,\delta}(t,x)&\text{on }\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)},\\ v^{n}\_{k}(t,x),&\text{otherwise}.\end{array}\right. |  |

Next, we show that (v1n,…,vk−1n,vkp,δ,vk+1n,…,vKn)(v^{n}\_{1},\ldots,v^{n}\_{k-1},v^{p,\delta}\_{k},v^{n}\_{k+1},\ldots,v^{n}\_{K}) is a stochastic supersolution. Only the supermartingale property with τ¯∈[Tk−1,Tk]\bar{\tau}\in[T\_{k-1},T\_{k}] is non-trivial. Define the event

|  |  |  |
| --- | --- | --- |
|  | A:={(τ¯,ξ)∈𝒟​(Tk,x¯,ε/2)}∩{ψp,δ​(τ¯,ξ)<vkn​(τ¯,ξ)}.A:=\{(\bar{\tau},\xi)\in\mathcal{D}(T\_{k},\bar{x},\varepsilon/2)\}\cap\{\psi^{p,\delta}(\bar{\tau},\xi)<v^{n}\_{k}(\bar{\tau},\xi)\}. |  |

Let U0:=(θk:K0,Λ0):=(θk:K0,{(τn0,Δn0)}n=1∞)U^{0}:=(\theta^{0}\_{k:K},\Lambda^{0}):=(\theta^{0}\_{k:K},\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}) be a suitable control for vknv^{n}\_{k} with the random initial condition (τ¯,ξ)(\bar{\tau},\xi). Define a new control U1:=(θk:K1,Λ1)U^{1}:=(\theta^{1}\_{k:K},\Lambda^{1}) by

|  |  |  |
| --- | --- | --- |
|  | θk:K1:=𝟏A​∅+𝟏Ac​θk:K0,Λ1:={(τn1,Δn1)}n=1∞:=𝟏Ac​{(τn0,Δn0)}n=1∞.\theta^{1}\_{k:K}:=\mathbf{1}\_{A}\emptyset+\mathbf{1}\_{A^{c}}\theta^{0}\_{k:K},\quad\Lambda^{1}:=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\}^{\infty}\_{n=1}:=\mathbf{1}\_{A^{c}}\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}. |  |

Here, if AA happens, we do not conduct any transactions. Let

|  |  |  |
| --- | --- | --- |
|  | τ′:=inf{t∈[τ¯,Tk]|(t,X​(t;τ¯,ξ,U1))∉𝒟​(Tk,x¯,ε/2)}∧Tk\displaystyle\tau^{\prime}:=\inf\{t\in[\bar{\tau},T\_{k}]\,|\,(t,X(t;\bar{\tau},\xi,U^{1}))\notin\mathcal{D}(T\_{k},\bar{x},\varepsilon/2)\}\wedge T\_{k} |  |

be the exit time and ξ′:=X​(τ′;τ¯,ξ,U1)∈ℱτ′\xi^{\prime}:=X(\tau^{\prime};\bar{\tau},\xi,U^{1})\in{\mathcal{F}}\_{\tau^{\prime}} be the exit position.

There is a suitable control U2:=(θk:K2,Λ2):=(θk:K2,{(τn2,Δn2)}n=1∞)U^{2}:=(\theta^{2}\_{k:K},\Lambda^{2}):=(\theta^{2}\_{k:K},\{(\tau^{2}\_{n},\Delta^{2}\_{n})\}^{\infty}\_{n=1}) for vknv^{n}\_{k} with the random initial condition (τ′,ξ′)(\tau^{\prime},\xi^{\prime}). Since τ′≤Tk\tau^{\prime}\leq T\_{k}, the tuple (Tk,ξ0′−θk∗​(ξ′),ξ1′)(T\_{k},\xi^{\prime}\_{0}-\theta^{\*}\_{k}(\xi^{\prime}),\xi^{\prime}\_{1}) is also a random initial condition. Similarly, there is a suitable control U3:=(θk+1:K3,Λ3):=(θk+1:K3,{(τn3,Δn3)}n=1∞)U^{3}:=(\theta^{3}\_{k+1:K},\Lambda^{3}):=(\theta^{3}\_{k+1:K},\{(\tau^{3}\_{n},\Delta^{3}\_{n})\}^{\infty}\_{n=1}) for vk+1nv^{n}\_{k+1} with the random initial condition (Tk,ξ0′−θk∗​(ξ′),ξ1′)(T\_{k},\xi^{\prime}\_{0}-\theta^{\*}\_{k}(\xi^{\prime}),\xi^{\prime}\_{1}). In the same manner, we introduce a suitable control U4:=(θk+1:K4,Λ4):=(θk+1:K4,{(τn4,Δn4)}n=1∞)U^{4}:=(\theta^{4}\_{k+1:K},\Lambda^{4}):=(\theta^{4}\_{k+1:K},\{(\tau^{4}\_{n},\Delta^{4}\_{n})\}^{\infty}\_{n=1}) for vk+1nv^{n}\_{k+1} with the random initial condition (Tk,ξ′)(T\_{k},\xi^{\prime}). Define a control U:=(θk:K,Λ)U:=(\theta\_{k:K},\Lambda) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ:=\displaystyle\Lambda:= | {(τn1,Δn1)​𝟏{τn1≤τ′}}n=1∞+{(τn2,Δn2)​𝟏{τ′≤τn2}∩{τ′<Tk}}n=1∞\displaystyle\{(\tau^{1}\_{n},\Delta^{1}\_{n})\mathbf{1}\_{\{\tau^{1}\_{n}\leq\tau^{\prime}\}}\}^{\infty}\_{n=1}+\{(\tau^{2}\_{n},\Delta^{2}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{2}\_{n}\}\cap\{\tau^{\prime}<T\_{k}\}}\}^{\infty}\_{n=1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +{(τn3,Δn3)​𝟏{τ′≤τn3}∩A∩{τ′=Tk}}n=1∞+{(τn4,Δn4)​𝟏{τ′≤τn4}∩Ac∩{τ′=Tk}}n=1∞,\displaystyle+\{(\tau^{3}\_{n},\Delta^{3}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{3}\_{n}\}\cap A\cap\{\tau^{\prime}=T\_{k}\}}\}^{\infty}\_{n=1}+\{(\tau^{4}\_{n},\Delta^{4}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{4}\_{n}\}\cap A^{c}\cap\{\tau^{\prime}=T\_{k}\}}\}^{\infty}\_{n=1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θk:=\displaystyle\theta\_{k}:= | θk0​𝟏Ac∩{τ′=Tk}+θk∗​(ξ′)​𝟏A∩{τ′=Tk}+θk2​𝟏{τ′<Tk},\displaystyle\theta^{0}\_{k}\mathbf{1}\_{A^{c}\cap\{\tau^{\prime}=T\_{k}\}}+\theta^{\*}\_{k}(\xi^{\prime})\mathbf{1}\_{A\cap\{\tau^{\prime}=T\_{k}\}}+\theta^{2}\_{k}\mathbf{1}\_{\{\tau^{\prime}<T\_{k}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θk+1:K:=\displaystyle\theta\_{k+1:K}:= | θk+1:K2​𝟏{τ′<Tk}+θk+1:K3​𝟏A∩{τ′=Tk}+θk+1:K4​𝟏Ac∩{τ′=Tk}.\displaystyle\theta^{2}\_{k+1:K}\mathbf{1}\_{\{\tau^{\prime}<T\_{k}\}}+\theta^{3}\_{k+1:K}\mathbf{1}\_{A\cap\{\tau^{\prime}=T\_{k}\}}+\theta^{4}\_{k+1:K}\mathbf{1}\_{A^{c}\cap\{\tau^{\prime}=T\_{k}\}}. |  |

The control UU is constructed as follows. First, U1U^{1} is applied on [τ¯,τ′][\bar{\tau},\tau^{\prime}]. Then:

* •

  It the event A∩{τ′=Tk}A\cap\{\tau^{\prime}=T\_{k}\} occurs, ξ′\xi^{\prime} is the position before the kk-th withdrawal. We use the amount θk∗​(ξ′)\theta^{\*}\_{k}(\xi^{\prime}) to support goal GkG\_{k}. After that, we follow U3U^{3} on [τ′,TK][\tau^{\prime},T\_{K}].
* •

  If the event Ac∩{τ′=Tk}A^{c}\cap\{\tau^{\prime}=T\_{k}\} occurs, it means that the amount θk0\theta^{0}\_{k} is used and ξ′\xi^{\prime} is the position after supporting GkG\_{k} already. Then we continue to use U4U^{4} on [τ′,TK][\tau^{\prime},T\_{K}].
* •

  If the event τ′<Tk\tau^{\prime}<T\_{k} occurs, the control U2U^{2} is applied on [τ′,TK][\tau^{\prime},T\_{K}].

We verify that UU is suitable for vkp,δv^{p,\delta}\_{k} with (τ¯,ξ)(\bar{\tau},\xi).

Consider a stopping time ρ∈[τ¯,TK]\rho\in[\bar{\tau},T\_{K}]. Applying the Itô’s formula to ψp,δ\psi^{p,\delta} from τ\tau to ρ∧τ′\rho\wedge\tau^{\prime} under the event AA with the control U1U^{1}, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​vkp,δ​(τ¯,ξ)=𝟏A​ψp,δ​(τ¯,ξ)=𝟏A​ψp,δ​(τ¯,X​(τ¯;τ¯,ξ,U1))\displaystyle\mathbf{1}\_{A}v^{p,\delta}\_{k}(\bar{\tau},\xi)=\mathbf{1}\_{A}\psi^{p,\delta}(\bar{\tau},\xi)=\mathbf{1}\_{A}\psi^{p,\delta}(\bar{\tau},X(\bar{\tau};\bar{\tau},\xi,U^{1})) |  |
|  |  |  |
| --- | --- | --- |
|  | ≥𝔼​[𝟏A∩{ρ<τ′}​ψp,δ​(ρ,X​(ρ;τ¯,ξ,U1))+𝟏A∩{ρ≥τ′}​ψp,δ​(τ′,ξ′)|ℱτ¯].\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\rho<\tau^{\prime}\}}\psi^{p,\delta}(\rho,X(\rho;\bar{\tau},\xi,U^{1}))+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}}\psi^{p,\delta}(\tau^{\prime},\xi^{\prime})\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

Moreover, ([A.20](https://arxiv.org/html/2510.21650v1#A1.E20 "In 2nd item ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([A.21](https://arxiv.org/html/2510.21650v1#A1.E21 "In 3rd item ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) lead to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏A∩{ρ≥τ′}​ψp,δ​(τ′,ξ′)≥\displaystyle\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}}\psi^{p,\delta}(\tau^{\prime},\xi^{\prime})\geq | 𝟏A∩{ρ≥τ′}∩{τ′<Tk}​vkn​(τ′,ξ′)\displaystyle\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{k}\}}v^{n}\_{k}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏A∩{ρ≥τ′}∩{τ′=Tk}​(wk​(Gk−θk∗​(ξ′))++vk+1n​(Tk,ξ0′−θk∗​(ξ′),ξ1′)).\displaystyle+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}}\Big(w\_{k}(G\_{k}-\theta^{\*}\_{k}(\xi^{\prime}))^{+}+v^{n}\_{k+1}(T\_{k},\xi^{\prime}\_{0}-\theta^{\*}\_{k}(\xi^{\prime}),\xi^{\prime}\_{1})\Big). |  |

Since vkp,δ≤ψp,δv^{p,\delta}\_{k}\leq\psi^{p,\delta} on 𝒟​(Tk,x¯,ε)¯\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​vkp,δ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A}v^{p,\delta}\_{k}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥𝔼[𝟏A∩{ρ<τ′}vkp,δ(ρ,X(ρ;τ¯,ξ,U1))\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\rho<\tau^{\prime}\}}v^{p,\delta}\_{k}(\rho,X(\rho;\bar{\tau},\xi,U^{1})) |  | (A.22) |
|  |  |  |
| --- | --- | --- |
|  | +𝟏A∩{ρ≥τ′}∩{τ′<Tk}​vkn​(τ′,ξ′)\displaystyle\qquad+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{k}\}}v^{n}\_{k}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏A∩{ρ≥τ′}∩{τ′=Tk}(wk(Gk−θk∗(ξ′))++vk+1n(Tk,ξ0′−θk∗(ξ′),ξ1′))|ℱτ¯]\displaystyle\qquad+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}}\Big(w\_{k}(G\_{k}-\theta^{\*}\_{k}(\xi^{\prime}))^{+}+v^{n}\_{k+1}(T\_{k},\xi^{\prime}\_{0}-\theta^{\*}\_{k}(\xi^{\prime}),\xi^{\prime}\_{1})\Big)\Big|{\mathcal{F}}\_{\bar{\tau}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =𝔼[𝟏A∩{ρ<τ′}vkp,δ(ρ,X(ρ;τ¯,ξ,U))\displaystyle=\mathbb{E}\Big[\mathbf{1}\_{A\cap\{\rho<\tau^{\prime}\}}v^{p,\delta}\_{k}(\rho,X(\rho;\bar{\tau},\xi,U)) |  | (A.23) |
|  |  |  |
| --- | --- | --- |
|  | +𝟏A∩{ρ≥τ′}∩{τ′<Tk}​vkn​(τ′,ξ′)\displaystyle\qquad+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{k}\}}v^{n}\_{k}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏A∩{ρ≥τ′}∩{τ′=Tk}(wk(Gk−θk)++vk+1n(Tk,ξ0′−θk,ξ1′))|ℱτ¯].\displaystyle\qquad+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}}\Big(w\_{k}(G\_{k}-\theta\_{k})^{+}+v^{n}\_{k+1}(T\_{k},\xi^{\prime}\_{0}-\theta\_{k},\xi^{\prime}\_{1})\Big)\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

In the last equality, we use the definition of UU and the fact that θk=θk∗​(ξ′)\theta\_{k}=\theta^{\*}\_{k}(\xi^{\prime}) under the event A∩{ρ≥τ′}∩{τ′=Tk}A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}.

Similar to Lemma [A.2](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), under the event AcA^{c}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝟏Ac​vkp,δ​(τ¯,ξ)=𝟏Ac​vkn​(τ¯,ξ)\displaystyle\mathbf{1}\_{A^{c}}v^{p,\delta}\_{k}(\bar{\tau},\xi)=\mathbf{1}\_{A^{c}}v^{n}\_{k}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥𝔼[𝟏Ac∩{ρ<τ′}vkn(ρ,X(ρ;τ¯,ξ,U1))\displaystyle\geq\mathbb{E}\Big[\mathbf{1}\_{A^{c}\cap\{\rho<\tau^{\prime}\}}v^{n}\_{k}(\rho,X(\rho;\bar{\tau},\xi,U^{1})) |  | (A.24) |
|  |  |  |
| --- | --- | --- |
|  | +𝟏Ac∩{ρ≥τ′}∩{τ′<Tk}​vkn​(τ′,ξ′)\displaystyle\qquad+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{k}\}}v^{n}\_{k}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏Ac∩{ρ≥τ′}∩{τ′=Tk}(wk(Gk−θk0)++vk+1n(Tk,ξ′))|ℱτ¯]\displaystyle\qquad+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}}\Big(w\_{k}(G\_{k}-\theta^{0}\_{k})^{+}+v^{n}\_{k+1}(T\_{k},\xi^{\prime})\Big)\Big|{\mathcal{F}}\_{\bar{\tau}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼[𝟏Ac∩{ρ<τ′}vkn(ρ,X(ρ;τ¯,ξ,U))\displaystyle=\mathbb{E}\Big[\mathbf{1}\_{A^{c}\cap\{\rho<\tau^{\prime}\}}v^{n}\_{k}(\rho,X(\rho;\bar{\tau},\xi,U)) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏Ac∩{ρ≥τ′}∩{τ′<Tk}​vkn​(τ′,ξ′)\displaystyle\qquad+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{k}\}}v^{n}\_{k}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏Ac∩{ρ≥τ′}∩{τ′=Tk}(wk(Gk−θk)++vk+1n(Tk,ξ′))|ℱτ¯].\displaystyle\qquad+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}}\Big(w\_{k}(G\_{k}-\theta\_{k})^{+}+v^{n}\_{k+1}(T\_{k},\xi^{\prime})\Big)\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

These two inequalities yield

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vkp,δ(τ¯,ξ)≥𝔼[\displaystyle v^{p,\delta}\_{k}(\bar{\tau},\xi)\geq\mathbb{E}\Big[ | 𝟏{ρ<τ′}​vkp,δ​(ρ,X​(ρ;τ¯,ξ,U))\displaystyle\mathbf{1}\_{\{\rho<\tau^{\prime}\}}v^{p,\delta}\_{k}(\rho,X(\rho;\bar{\tau},\xi,U)) |  | (A.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏{ρ≥τ′}∩{τ′<Tk}​vkn​(τ′,ξ′)\displaystyle+\mathbf{1}\_{\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}<T\_{k}\}}v^{n}\_{k}(\tau^{\prime},\xi^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏A∩{ρ≥τ′}∩{τ′=Tk}​(wk​(Gk−θk)++vk+1n​(Tk,ξ0′−θk,ξ1′))\displaystyle+\mathbf{1}\_{A\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}}\Big(w\_{k}(G\_{k}-\theta\_{k})^{+}+v^{n}\_{k+1}(T\_{k},\xi^{\prime}\_{0}-\theta\_{k},\xi^{\prime}\_{1})\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏Ac∩{ρ≥τ′}∩{τ′=Tk}(wk(Gk−θk)++vk+1n(Tk,ξ′))|ℱτ¯].\displaystyle+\mathbf{1}\_{A^{c}\cap\{\rho\geq\tau^{\prime}\}\cap\{\tau^{\prime}=T\_{k}\}}\Big(w\_{k}(G\_{k}-\theta\_{k})^{+}+v^{n}\_{k+1}(T\_{k},\xi^{\prime})\Big)\Big|{\mathcal{F}}\_{\bar{\tau}}\Big]. |  |

The definition of UU leads to the desired result:

|  |  |  |
| --- | --- | --- |
|  | vkp,δ​(τ¯,ξ)≥𝔼​[ℋ​([τ¯,ρ],(vkp,δ,vk+1:K),X​(⋅;τ¯,ξ,θk:K,Λ))|ℱτ¯].v^{p,\delta}\_{k}(\bar{\tau},\xi)\geq\mathbb{E}\big[\mathcal{H}\big([\bar{\tau},\rho],(v^{p,\delta}\_{k},v\_{k+1:K}),X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\Lambda)\big)\big|{\mathcal{F}}\_{\bar{\tau}}\big]. |  |

Case 2. vk,+​(Tk,x¯)−ℳ​[vk,+]∗​(Tk,x¯)>0.v\_{k,+}(T\_{k},\bar{x})-{\mathcal{M}}[v\_{k,+}]^{\*}(T\_{k},\bar{x})>0.

This case is similar to Lemma [A.2](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). We report the control UU only. Let U0U^{0} be a suitable control for vknv^{n}\_{k} with (τ¯,ξ)(\bar{\tau},\xi). Define U1:=(θk:K1,Λ1)U^{1}:=(\theta^{1}\_{k:K},\Lambda^{1}) by

|  |  |  |
| --- | --- | --- |
|  | θk:K1:=𝟏A​∅+𝟏Ac​θk:K0,Λ1:={(τn1,Δn1)}n=1∞:=𝟏A​(τ¯,Δ∗​(τ¯,ξ))+𝟏Ac​{(τn0,Δn0)}n=1∞,\theta^{1}\_{k:K}:=\mathbf{1}\_{A}\emptyset+\mathbf{1}\_{A^{c}}\theta^{0}\_{k:K},\quad\Lambda^{1}:=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\}^{\infty}\_{n=1}:=\mathbf{1}\_{A}(\bar{\tau},\Delta^{\*}(\bar{\tau},\xi))+\mathbf{1}\_{A^{c}}\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}, |  |

where Δ∗​(t,x)\Delta^{\*}(t,x) is defined similarly as in Lemma [A.2](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Let (τ′,ξ′)(\tau^{\prime},\xi^{\prime}) be the exit time and position as before. There is a suitable control U2:=(θk:K2,Λ2):=(θk:K2,{(τn2,Δn2)}n=1∞)U^{2}:=(\theta^{2}\_{k:K},\Lambda^{2}):=(\theta^{2}\_{k:K},\{(\tau^{2}\_{n},\Delta^{2}\_{n})\}^{\infty}\_{n=1}) for vknv^{n}\_{k} with the random initial condition (τ′,ξ′)(\tau^{\prime},\xi^{\prime}). Besides, we introduce a suitable control U4:=(θk+1:K4,Λ4):=(θk+1:K4,{(τn4,Δn4)}n=1∞)U^{4}:=(\theta^{4}\_{k+1:K},\Lambda^{4}):=(\theta^{4}\_{k+1:K},\{(\tau^{4}\_{n},\Delta^{4}\_{n})\}^{\infty}\_{n=1}) for vk+1nv^{n}\_{k+1} with the random initial condition (Tk,ξ′)(T\_{k},\xi^{\prime}). Define a control U:=(θk:K,Λ)U:=(\theta\_{k:K},\Lambda) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ:=\displaystyle\Lambda:= | {(τn1,Δn1)​𝟏{τn1≤τ′}}n=1∞+{(τn2,Δn2)​𝟏{τ′≤τn2}∩{Ac∩{τ′<Tk}​ or ​A}}n=1∞\displaystyle\{(\tau^{1}\_{n},\Delta^{1}\_{n})\mathbf{1}\_{\{\tau^{1}\_{n}\leq\tau^{\prime}\}}\}^{\infty}\_{n=1}+\{(\tau^{2}\_{n},\Delta^{2}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{2}\_{n}\}\cap\{A^{c}\cap\{\tau^{\prime}<T\_{k}\}\text{ or }A\}}\}^{\infty}\_{n=1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +{(τn4,Δn4)​𝟏{τ′≤τn4}∩Ac∩{τ′=Tk}}n=1∞,\displaystyle+\{(\tau^{4}\_{n},\Delta^{4}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{4}\_{n}\}\cap A^{c}\cap\{\tau^{\prime}=T\_{k}\}}\}^{\infty}\_{n=1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θk:=\displaystyle\theta\_{k}:= | θk0​𝟏Ac∩{τ′=Tk}+θk2​𝟏{Ac∩{τ′<Tk}​ or ​A},\displaystyle\theta^{0}\_{k}\mathbf{1}\_{A^{c}\cap\{\tau^{\prime}=T\_{k}\}}+\theta^{2}\_{k}\mathbf{1}\_{\{A^{c}\cap\{\tau^{\prime}<T\_{k}\}\text{ or }A\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θk+1:K:=\displaystyle\theta\_{k+1:K}:= | θk+1:K4​𝟏Ac∩{τ′=Tk}+θk+1:K2​𝟏{Ac∩{τ′<Tk}​ or ​A}.\displaystyle\theta^{4}\_{k+1:K}\mathbf{1}\_{A^{c}\cap\{\tau^{\prime}=T\_{k}\}}+\theta^{2}\_{k+1:K}\mathbf{1}\_{\{A^{c}\cap\{\tau^{\prime}<T\_{k}\}\text{ or }A\}}. |  |

The control UU is suitable for vkp,δv^{p,\delta}\_{k} with (τ¯,ξ)(\bar{\tau},\xi).
∎

###### Lemma A.4.

The upper stochastic envelope v+v\_{+} satisfies the interior viscosity subsolution property ([3.11](https://arxiv.org/html/2510.21650v1#S3.E11 "In item (1) ‣ Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) on [Tk−1,Tk)×𝒮[T\_{k-1},T\_{k})\times{\mathcal{S}}, k=1,…,Kk=1,\ldots,K, under Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proof.

Let (t¯,x¯)∈[Tk−1,Tk)×𝒮(\bar{t},\bar{x})\in[T\_{k-1},T\_{k})\times{\mathcal{S}}. Consider a test function φ∈C1,2​([Tk−1,Tk)×𝒮)\varphi\in C^{1,2}([T\_{k-1},T\_{k})\times{\mathcal{S}}), such that vk,+−φv\_{k,+}-\varphi attains a strict local maximum of zero at (t¯,x¯)(\bar{t},\bar{x}). Assume on the contrary that

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{ℒ​[φ]​(t¯,x¯),vk,+​(t¯,x¯)−ℳ​[vk,+]∗​(t¯,x¯)}>0.\max\Big\{{\mathcal{L}}[\varphi](\bar{t},\bar{x}),v\_{k,+}(\bar{t},\bar{x})-{\mathcal{M}}[v\_{k,+}]^{\*}(\bar{t},\bar{x})\Big\}>0. |  | (A.26) |

Case 1. ℒ​[φ]​(t¯,x¯)>0{\mathcal{L}}[\varphi](\bar{t},\bar{x})>0.

The proof is similar to bayraktar2013stochastic. We give the main steps and omit similar arguments. With a small η>0\eta>0, we define φη​(t,x):=φ​(t,x)−η\varphi^{\eta}(t,x):=\varphi(t,x)-\eta. Moreover, φη\varphi^{\eta} satisfies the following properties:

* •

  ℒ​[φη]​(t,x)>0​ on ​B​(t¯,x¯,ε)¯{\mathcal{L}}[\varphi^{\eta}](t,x)>0\text{ on }\overline{B(\bar{t},\bar{x},\varepsilon)}.
* •

  φη​(t,x)≥vkn​(t,x)​ on ​B​(t¯,x¯,ε)¯∖B​(t¯,x¯,ε/2)\varphi^{\eta}(t,x)\geq v^{n}\_{k}(t,x)\text{ on }\overline{B(\bar{t},\bar{x},\varepsilon)}\setminus B(\bar{t},\bar{x},\varepsilon/2).
* •

  φη​(t¯,x¯)<vk,+​(t¯,x¯)\varphi^{\eta}(\bar{t},\bar{x})<v\_{k,+}(\bar{t},\bar{x}).

We introduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | vkη​(t,x):={vkn​(t,x)∧φη​(t,x)on ​B​(t¯,x¯,ε)¯,vkn​(t,x),otherwise.v^{\eta}\_{k}(t,x):=\left\{\begin{array}[]{ c l }v^{n}\_{k}(t,x)\wedge\varphi^{\eta}(t,x)&\text{on }\overline{B(\bar{t},\bar{x},\varepsilon)},\\ v^{n}\_{k}(t,x),&\text{otherwise}.\end{array}\right. |  | (A.27) |

To show that (v1n,…,vk−1n,vkη,vk+1n,…,vKn)(v^{n}\_{1},\ldots,v^{n}\_{k-1},v^{\eta}\_{k},v^{n}\_{k+1},\ldots,v^{n}\_{K}) is a stochastic supersolution, we only need to consider the case with τ¯∈[Tk−1,Tk]\bar{\tau}\in[T\_{k-1},T\_{k}]. Define the event

|  |  |  |
| --- | --- | --- |
|  | A:={(τ¯,ξ)∈B​(t¯,x¯,ε/2)}∩{φη​(τ¯,ξ)<vkn​(τ¯,ξ)}.A:=\{(\bar{\tau},\xi)\in B(\bar{t},\bar{x},\varepsilon/2)\}\cap\{\varphi^{\eta}(\bar{\tau},\xi)<v^{n}\_{k}(\bar{\tau},\xi)\}. |  |

Let U0:=(θk:K0,Λ0):=(θk:K0,{(τn0,Δn0)}n=1∞)U^{0}:=(\theta^{0}\_{k:K},\Lambda^{0}):=(\theta^{0}\_{k:K},\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}) be a suitable control for vknv^{n}\_{k} with the random initial condition (τ¯,ξ)(\bar{\tau},\xi). Define a new control U1:=(θk:K1,Λ1)U^{1}:=(\theta^{1}\_{k:K},\Lambda^{1}) by

|  |  |  |
| --- | --- | --- |
|  | θk:K1:=𝟏A​∅+𝟏Ac​θk:K0,Λ1:={(τn1,Δn1)}n=1∞:=𝟏Ac​{(τn0,Δn0)}n=1∞.\theta^{1}\_{k:K}:=\mathbf{1}\_{A}\emptyset+\mathbf{1}\_{A^{c}}\theta^{0}\_{k:K},\quad\Lambda^{1}:=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\}^{\infty}\_{n=1}:=\mathbf{1}\_{A^{c}}\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}. |  |

Let

|  |  |  |
| --- | --- | --- |
|  | τ′:=inf{t∈[τ¯,Tk]|(t,X​(t;τ¯,ξ,U1))∉B​(t¯,x¯,ε/2)}∧Tk\displaystyle\tau^{\prime}:=\inf\{t\in[\bar{\tau},T\_{k}]\,|\,(t,X(t;\bar{\tau},\xi,U^{1}))\notin B(\bar{t},\bar{x},\varepsilon/2)\}\wedge T\_{k} |  |

be the exit time and ξ′:=X​(τ′;τ¯,ξ,U1)∈ℱτ′\xi^{\prime}:=X(\tau^{\prime};\bar{\tau},\xi,U^{1})\in{\mathcal{F}}\_{\tau^{\prime}} be the exit position.

We introduce a suitable control U2:=(θk:K2,Λ2):=(θk:K2,{(τn2,Δn2)}n=1∞)U^{2}:=(\theta^{2}\_{k:K},\Lambda^{2}):=(\theta^{2}\_{k:K},\{(\tau^{2}\_{n},\Delta^{2}\_{n})\}^{\infty}\_{n=1}) for vknv^{n}\_{k} with (τ′,ξ′)(\tau^{\prime},\xi^{\prime}), and a suitable control U4:=(θk+1:K4,Λ4):=(θk+1:K4,{(τn4,Δn4)}n=1∞)U^{4}:=(\theta^{4}\_{k+1:K},\Lambda^{4}):=(\theta^{4}\_{k+1:K},\{(\tau^{4}\_{n},\Delta^{4}\_{n})\}^{\infty}\_{n=1}) for vk+1nv^{n}\_{k+1} with (Tk,ξ′)(T\_{k},\xi^{\prime}). Define U:=(θk:K,Λ)U:=(\theta\_{k:K},\Lambda) by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Λ:=\displaystyle\Lambda= | {(τn1,Δn1)​𝟏{τn1≤τ′}}n=1∞+{(τn2,Δn2)​𝟏{τ′≤τn2}∩{Ac∩{τ′<Tk}​ or ​A}}n=1∞\displaystyle\{(\tau^{1}\_{n},\Delta^{1}\_{n})\mathbf{1}\_{\{\tau^{1}\_{n}\leq\tau^{\prime}\}}\}^{\infty}\_{n=1}+\{(\tau^{2}\_{n},\Delta^{2}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{2}\_{n}\}\cap\{A^{c}\cap\{\tau^{\prime}<T\_{k}\}\text{ or }A\}}\}^{\infty}\_{n=1} |  | (A.28) |
|  |  | +{(τn4,Δn4)​𝟏{τ′≤τn4}∩Ac∩{τ′=Tk}}n=1∞,\displaystyle+\{(\tau^{4}\_{n},\Delta^{4}\_{n})\mathbf{1}\_{\{\tau^{\prime}\leq\tau^{4}\_{n}\}\cap A^{c}\cap\{\tau^{\prime}=T\_{k}\}}\}^{\infty}\_{n=1}, |  |
|  | θk:=\displaystyle\theta\_{k}= | θk0​𝟏Ac∩{τ′=Tk}+θk2​𝟏{Ac∩{τ′<Tk}​ or ​A},\displaystyle\theta^{0}\_{k}\mathbf{1}\_{A^{c}\cap\{\tau^{\prime}=T\_{k}\}}+\theta^{2}\_{k}\mathbf{1}\_{\{A^{c}\cap\{\tau^{\prime}<T\_{k}\}\text{ or }A\}}, |  |
|  | θk+1:K:=\displaystyle\theta\_{k+1:K}= | θk+1:K4​𝟏Ac∩{τ′=Tk}+θk+1:K2​𝟏{Ac∩{τ′<Tk}​ or ​A}.\displaystyle\theta^{4}\_{k+1:K}\mathbf{1}\_{A^{c}\cap\{\tau^{\prime}=T\_{k}\}}+\theta^{2}\_{k+1:K}\mathbf{1}\_{\{A^{c}\cap\{\tau^{\prime}<T\_{k}\}\text{ or }A\}}. |  |

Then the remaining proof follows similarly.

Case 2. vk,+​(t¯,x¯)−ℳ​[vk,+]∗​(t¯,x¯)>0v\_{k,+}(\bar{t},\bar{x})-{\mathcal{M}}[v\_{k,+}]^{\*}(\bar{t},\bar{x})>0.

Again, we report the control UU only. Let U0U^{0} be a suitable control for vknv^{n}\_{k} with (τ¯,ξ)(\bar{\tau},\xi). Define U1:=(θk:K1,Λ1)U^{1}:=(\theta^{1}\_{k:K},\Lambda^{1}) by

|  |  |  |
| --- | --- | --- |
|  | θk:K1:=𝟏A​∅+𝟏Ac​θk:K0,Λ1:={(τn1,Δn1)}n=1∞:=𝟏A​(τ¯,Δ∗​(τ¯,ξ))+𝟏Ac​{(τn0,Δn0)}n=1∞,\theta^{1}\_{k:K}:=\mathbf{1}\_{A}\emptyset+\mathbf{1}\_{A^{c}}\theta^{0}\_{k:K},\quad\Lambda^{1}:=\{(\tau^{1}\_{n},\Delta^{1}\_{n})\}^{\infty}\_{n=1}:=\mathbf{1}\_{A}(\bar{\tau},\Delta^{\*}(\bar{\tau},\xi))+\mathbf{1}\_{A^{c}}\{(\tau^{0}\_{n},\Delta^{0}\_{n})\}^{\infty}\_{n=1}, |  |

where Δ∗​(t,x)\Delta^{\*}(t,x) is defined similarly as in Lemma [A.2](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Then UU can be constructed as in ([A.28](https://arxiv.org/html/2510.21650v1#A1.E28 "In Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")).
∎

## Appendix B Proofs of the stochastic subsolution

###### Proof of Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Step 1. We prove the inequality ([5.10](https://arxiv.org/html/2510.21650v1#S5.E10 "In item (3) ‣ Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) at TKT\_{K} first. Consider the first term in ([5.10](https://arxiv.org/html/2510.21650v1#S5.E10 "In item (3) ‣ Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")). Since (x1−C​(−x1))+≤x1(x\_{1}-C(-x\_{1}))^{+}\leq x\_{1}, we have GK−x0−(x1−C​(−x1))+≥GK−x0−x1G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\geq G\_{K}-x\_{0}-x\_{1}, which further implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | [GK−x0−(x1−C​(−x1))+]+≥(GK−x0−x1)+.[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}]^{+}\geq(G\_{K}-x\_{0}-x\_{1})^{+}. |  | (B.1) |

If x0+x1>GKx\_{0}+x\_{1}>G\_{K}, then

|  |  |  |
| --- | --- | --- |
|  | FKa​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+\displaystyle F^{a}\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤FKa​(TK,x)−wK​[GK−x0−x1]+\displaystyle\leq F^{a}\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-x\_{1}\right]^{+} |  |
|  |  |  |
| --- | --- | --- |
|  | =FKa​(TK,x)\displaystyle=F^{a}\_{K}(T\_{K},x) |  |
|  |  |  |
| --- | --- | --- |
|  | =wK​GK−2​wK​GK1−q​(a+x0+x1)q\displaystyle=w\_{K}G\_{K}-2w\_{K}G^{1-q}\_{K}(a+x\_{0}+x\_{1})^{q} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤wK​GK−2​wK​GK1−q​GKq=−wK​GK<0.\displaystyle\leq w\_{K}G\_{K}-2w\_{K}G^{1-q}\_{K}G^{q}\_{K}=-w\_{K}G\_{K}<0. |  |

If x0+x1≤GKx\_{0}+x\_{1}\leq G\_{K} and (x0,x1)≠(0,0)(x\_{0},x\_{1})\neq(0,0), we obtain

|  |  |  |
| --- | --- | --- |
|  | FKa​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+\displaystyle F^{a}\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤FKa​(TK,x)−wK​[GK−x0−x1]+\displaystyle\leq F^{a}\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-x\_{1}\right]^{+} |  |
|  |  |  |
| --- | --- | --- |
|  | =FKa​(TK,x)−wK​GK+wK​(x0+x1)\displaystyle=F^{a}\_{K}(T\_{K},x)-w\_{K}G\_{K}+w\_{K}(x\_{0}+x\_{1}) |  |
|  |  |  |
| --- | --- | --- |
|  | =wK​GK−2​wK​GK1−q​(a+x0+x1)q−wK​GK+wK​(x0+x1)\displaystyle=w\_{K}G\_{K}-2w\_{K}G^{1-q}\_{K}(a+x\_{0}+x\_{1})^{q}-w\_{K}G\_{K}+w\_{K}(x\_{0}+x\_{1}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤−2​wK​GK1−q​(x0+x1)q+wK​(x0+x1)\displaystyle\leq-2w\_{K}G^{1-q}\_{K}(x\_{0}+x\_{1})^{q}+w\_{K}(x\_{0}+x\_{1}) |  |
|  |  |  |
| --- | --- | --- |
|  | =wK​(x0+x1)q​[−2​GK1−q+(x0+x1)1−q]\displaystyle=w\_{K}(x\_{0}+x\_{1})^{q}[-2G^{1-q}\_{K}+(x\_{0}+x\_{1})^{1-q}] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤wK​(x0+x1)q​[−2​GK1−q+GK1−q]=−wK​(x0+x1)q​GK1−q<0.\displaystyle\leq w\_{K}(x\_{0}+x\_{1})^{q}[-2G^{1-q}\_{K}+G^{1-q}\_{K}]=-w\_{K}(x\_{0}+x\_{1})^{q}G^{1-q}\_{K}<0. |  |

Combining these two inequalities together,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | FKa​(TK,x)−wK​[GK−x0−(x1−C​(−x1))+]+\displaystyle F^{a}\_{K}(T\_{K},x)-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+} |  | (B.2) |
|  |  | ≤−wK​(min⁡{x0+x1,GK})q​GK1−q<0,x∈𝒮.\displaystyle\leq-w\_{K}(\min\{x\_{0}+x\_{1},G\_{K}\})^{q}G^{1-q}\_{K}<0,\quad x\in{\mathcal{S}}. |  |

For the second term in ([5.10](https://arxiv.org/html/2510.21650v1#S5.E10 "In item (3) ‣ Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), if x∈𝒮∅x\in{\mathcal{S}}\_{\emptyset}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | FKa​(TK,x)−ℳ​[FKa]​(TK,x)=−∞.F^{a}\_{K}(T\_{K},x)-{\mathcal{M}}[F^{a}\_{K}](T\_{K},x)=-\infty. |  | (B.3) |

If x∉𝒮∅x\notin{\mathcal{S}}\_{\emptyset}, then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | FKa​(TK,x)−ℳ​[FKa]​(TK,x)\displaystyle F^{a}\_{K}(T\_{K},x)-{\mathcal{M}}[F^{a}\_{K}](T\_{K},x) |  | (B.4) |
|  |  | =wK​GK−2​wK​GK1−q​(a+x0+x1)q\displaystyle=w\_{K}G\_{K}-2w\_{K}G^{1-q}\_{K}(a+x\_{0}+x\_{1})^{q} |  |
|  |  | −infΔ∈D​(x)[wK​GK−2​wK​GK1−q​(a+x0+x1−C​(Δ))q]\displaystyle\quad-\inf\_{\Delta\in D(x)}[w\_{K}G\_{K}-2w\_{K}G^{1-q}\_{K}(a+x\_{0}+x\_{1}-C(\Delta))^{q}] |  |
|  |  | ≤2​wK​GK1−q​[(a+x0+x1−Cmin)q−(a+x0+x1)q]<0.\displaystyle\leq 2w\_{K}G^{1-q}\_{K}[(a+x\_{0}+x\_{1}-C\_{\min})^{q}-(a+x\_{0}+x\_{1})^{q}]<0. |  |

Clearly, a continuous function κKb​(x)\kappa^{b}\_{K}(x) exists, with κKb​(x)≤0\kappa^{b}\_{K}(x)\leq 0 for x∈𝒮¯x\in\overline{\mathcal{S}} and κKb​(x)<0\kappa^{b}\_{K}(x)<0 for x∈𝒮x\in{\mathcal{S}}.

Step 2. Next, we prove ([5.8](https://arxiv.org/html/2510.21650v1#S5.E8 "In item (1) ‣ Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")). Clearly, the term Fka​(t,x)−ℳ​[Fka]​(t,x)F^{a}\_{k}(t,x)-{\mathcal{M}}[F^{a}\_{k}](t,x) can be handled as in the Step 1. For the infinitesimal generator term, we have

|  |  |  |
| --- | --- | --- |
|  | ℒ​[Fka]​(t,x)\displaystyle{\mathcal{L}}[F^{a}\_{k}](t,x) |  |
|  |  |  |
| --- | --- | --- |
|  | =Ck​eλ​(Tk−t)​(a+x0+x1)q​{−λ+q​r​x0a+x0+x1+q​μ​x1a+x0+x1+q​(q−1)​σ2​x122​(a+x0+x1)2}\displaystyle\quad=C\_{k}e^{\lambda(T\_{k}-t)}(a+x\_{0}+x\_{1})^{q}\Big\{-\lambda+\frac{qrx\_{0}}{a+x\_{0}+x\_{1}}+\frac{q\mu x\_{1}}{a+x\_{0}+x\_{1}}+\frac{q(q-1)\sigma^{2}x^{2}\_{1}}{2(a+x\_{0}+x\_{1})^{2}}\Big\} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Ck​eλ​(Tk−t)​(a+x0+x1)q​(−λ+q​max⁡{r,μ,0})<0, if ​x∈𝒮.\displaystyle\quad\leq C\_{k}e^{\lambda(T\_{k}-t)}(a+x\_{0}+x\_{1})^{q}(-\lambda+q\max\{r,\mu,0\})<0,\;\text{ if }x\in{\mathcal{S}}. |  |

Then we can find κkc​(x)\kappa^{c}\_{k}(x) satisfying required properties.

Step 3. For the inequality at TkT\_{k}, we only need to consider the first term:

|  |  |  |
| --- | --- | --- |
|  | Fka​(Tk,x)−inf0≤θk≤x0[wk​(Gk−θk)++Fk+1a​(Tk,x0−θk,x1)]\displaystyle F^{a}\_{k}(T\_{k},x)-\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+F^{a}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Fka​(Tk,x)−wk​(Gk−x0−x1)+−Fk+1a​(Tk,x0−0,x1)\displaystyle\quad\leq F^{a}\_{k}(T\_{k},x)-w\_{k}(G\_{k}-x\_{0}-x\_{1})^{+}-F^{a}\_{k+1}(T\_{k},x\_{0}-0,x\_{1}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=kKwi​Gi−Ck​(a+x0+x1)q−wk​(Gk−x0−x1)+\displaystyle\quad=\sum^{K}\_{i=k}w\_{i}G\_{i}-C\_{k}(a+x\_{0}+x\_{1})^{q}-w\_{k}(G\_{k}-x\_{0}-x\_{1})^{+} |  |
|  |  |  |
| --- | --- | --- |
|  | −{∑i=k+1Kwi​Gi−Ck+1​(a+x0+x1)q​eλ​(Tk+1−Tk)}\displaystyle\qquad-\Big\{\sum^{K}\_{i=k+1}w\_{i}G\_{i}-C\_{k+1}(a+x\_{0}+x\_{1})^{q}e^{\lambda(T\_{k+1}-T\_{k})}\Big\} |  |
|  |  |  |
| --- | --- | --- |
|  | =wk​Gk−wk​(Gk−x0−x1)+−2​wk​Gk1−q​(a+x0+x1)q\displaystyle\quad=w\_{k}G\_{k}-w\_{k}(G\_{k}-x\_{0}-x\_{1})^{+}-2w\_{k}G^{1-q}\_{k}(a+x\_{0}+x\_{1})^{q} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤wk​Gk−wk​(Gk−x0−x1)+−2​wk​Gk1−q​(x0+x1)q.\displaystyle\quad\leq w\_{k}G\_{k}-w\_{k}(G\_{k}-x\_{0}-x\_{1})^{+}-2w\_{k}G^{1-q}\_{k}(x\_{0}+x\_{1})^{q}. |  |

Similar to the Step 1, if x0+x1>Gkx\_{0}+x\_{1}>G\_{k}, then

|  |  |  |
| --- | --- | --- |
|  | wk​Gk−wk​(Gk−x0−x1)+−2​wk​Gk1−q​(x0+x1)q≤−wk​Gk<0.\displaystyle w\_{k}G\_{k}-w\_{k}(G\_{k}-x\_{0}-x\_{1})^{+}-2w\_{k}G^{1-q}\_{k}(x\_{0}+x\_{1})^{q}\leq-w\_{k}G\_{k}<0. |  |

If x0+x1≤Gkx\_{0}+x\_{1}\leq G\_{k} and (x0,x1)≠(0,0)(x\_{0},x\_{1})\neq(0,0), we have

|  |  |  |
| --- | --- | --- |
|  | wk​Gk−wk​(Gk−x0−x1)+−2​wk​Gk1−q​(x0+x1)q≤−wk​Gk1−q​(x0+x1)q<0.\displaystyle w\_{k}G\_{k}-w\_{k}(G\_{k}-x\_{0}-x\_{1})^{+}-2w\_{k}G^{1-q}\_{k}(x\_{0}+x\_{1})^{q}\leq-w\_{k}G^{1-q}\_{k}(x\_{0}+x\_{1})^{q}<0. |  |

Hence, there exists κkb​(x)\kappa^{b}\_{k}(x) with desired properties.
∎

###### Proof of Lemma [5.4](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem4 "Lemma 5.4. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Since Fk0F^{0}\_{k} is continuous, Condition (1) on the LSC property holds. The growth condition (2) also holds directly. Condition (3) is verified in the proof of Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), in the same spirit of ([B.3](https://arxiv.org/html/2510.21650v1#A2.E3 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([B.4](https://arxiv.org/html/2510.21650v1#A2.E4 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")).

Finally, we verify Condition (4). At the goal deadline TkT\_{k}, where k=1,…,K−1k=1,\ldots,K-1, Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") indicates that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fk0​(Tk,x)≤wk​(Gk−θk)++Fk+10​(Tk,x0−θk,x1),F^{0}\_{k}(T\_{k},x)\leq w\_{k}(G\_{k}-\theta\_{k})^{+}+F^{0}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1}), |  | (B.5) |

for all x∈𝒮x\in{\mathcal{S}} and admissible θk\theta\_{k}. At the last deadline TKT\_{K}, ([B.2](https://arxiv.org/html/2510.21650v1#A2.E2 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) in the proof for Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") and FK0​(TK,0)=wK​GKF^{0}\_{K}(T\_{K},0)=w\_{K}G\_{K} imply that

|  |  |  |  |
| --- | --- | --- | --- |
|  | FK0​(TK,x)≤wK​[GK−x0−(x1−C​(−x1))+]+,F^{0}\_{K}(T\_{K},x)\leq w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  | (B.6) |

for all x∈𝒮¯x\in\overline{\mathcal{S}}.

Between goal deadlines, we can apply the Itô’s formula together with the property ℒ​[Fk0]​(t,x)<0{\mathcal{L}}[F^{0}\_{k}](t,x)<0 for x∈𝒮x\in{\mathcal{S}}. As a demonstration, we consider the case when k=K−1k=K-1, τ¯∈[TK−2,TK−1]\bar{\tau}\in[T\_{K-2},T\_{K-1}], and TK−1≤ρ≤TT\_{K-1}\leq\rho\leq T. If the random initial value ξ≠0\xi\neq 0, then a recursive application of the properties mentioned above shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | FK−10​(τ¯,ξ)\displaystyle F^{0}\_{K-1}(\bar{\tau},\xi) | =FK−10​(TK−1,X​(TK−1−))\displaystyle=F^{0}\_{K-1}(T\_{K-1},X(T\_{K-1}-)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫τ¯TK−1ℒ​[FK−10]​(t,X​(t))​𝑑t−∫τ¯TK−1σ​X1​(t)​∂FK−10∂x1​(t,X​(t))​𝑑W​(t)\displaystyle\quad+\int^{T\_{K-1}}\_{\bar{\tau}}{\mathcal{L}}[F^{0}\_{K-1}](t,X(t))dt-\int^{T\_{K-1}}\_{\bar{\tau}}\sigma X\_{1}(t)\frac{\partial F^{0}\_{K-1}}{\partial x\_{1}}(t,X(t))dW(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤wK−1​(GK−1−θK−1)++FK0​(TK−1,X0​(TK−1−)−θK−1,X1​(TK−1))\displaystyle\leq w\_{K-1}(G\_{K-1}-\theta\_{K-1})^{+}+F^{0}\_{K}(T\_{K-1},X\_{0}(T\_{K-1}-)-\theta\_{K-1},X\_{1}(T\_{K-1})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫τ¯TK−1ℒ​[FK−10]​(t,X​(t))​𝑑t−∫τ¯TK−1σ​X1​(t)​∂FK−10∂x1​(t,X​(t))​𝑑W​(t)\displaystyle\quad+\int^{T\_{K-1}}\_{\bar{\tau}}{\mathcal{L}}[F^{0}\_{K-1}](t,X(t))dt-\int^{T\_{K-1}}\_{\bar{\tau}}\sigma X\_{1}(t)\frac{\partial F^{0}\_{K-1}}{\partial x\_{1}}(t,X(t))dW(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =wK−1​(GK−1−θK−1)++FK0​(ρ,X​(ρ−))\displaystyle=w\_{K-1}(G\_{K-1}-\theta\_{K-1})^{+}+F^{0}\_{K}(\rho,X(\rho-)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫TK−1ρℒ​[FK0]​(t,X​(t))​𝑑t−∫TK−1ρσ​X1​(t)​∂FK0∂x1​(t,X​(t))​𝑑W​(t)\displaystyle\quad+\int^{\rho}\_{T\_{K-1}}{\mathcal{L}}[F^{0}\_{K}](t,X(t))dt-\int^{\rho}\_{T\_{K-1}}\sigma X\_{1}(t)\frac{\partial F^{0}\_{K}}{\partial x\_{1}}(t,X(t))dW(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫τ¯TK−1ℒ​[FK−10]​(t,X​(t))​𝑑t−∫τ¯TK−1σ​X1​(t)​∂FK−10∂x1​(t,X​(t))​𝑑W​(t),\displaystyle\quad+\int^{T\_{K-1}}\_{\bar{\tau}}{\mathcal{L}}[F^{0}\_{K-1}](t,X(t))dt-\int^{T\_{K-1}}\_{\bar{\tau}}\sigma X\_{1}(t)\frac{\partial F^{0}\_{K-1}}{\partial x\_{1}}(t,X(t))dW(t), |  |

where X​(t)X(t) represents X​(t;τ¯,ξ,θK−1:K,∅)X(t;\bar{\tau},\xi,\theta\_{K-1:K},\emptyset). Thanks to ([B.6](https://arxiv.org/html/2510.21650v1#A2.E6 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | FK0​(ρ,X​(ρ−))\displaystyle F^{0}\_{K}(\rho,X(\rho-)) | =FK0​(ρ,X​(ρ))​𝟏{ρ<T}+FK0​(T,X​(T−))​𝟏{ρ=T}\displaystyle=F^{0}\_{K}(\rho,X(\rho))\mathbf{1}\_{\{\rho<T\}}+F^{0}\_{K}(T,X(T-))\mathbf{1}\_{\{\rho=T\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤FK0​(ρ,X​(ρ))​𝟏{ρ<T}+wK​[GK−θK]+​𝟏{ρ=T}.\displaystyle\leq F^{0}\_{K}(\rho,X(\rho))\mathbf{1}\_{\{\rho<T\}}+w\_{K}\left[G\_{K}-\theta\_{K}\right]^{+}\mathbf{1}\_{\{\rho=T\}}. |  |

Combining these two inequalities together, a localization argument with Fatou’s lemma yields the corresponding Condition (4) when ξ≠0\xi\neq 0. If ξ=0\xi=0, both X0X\_{0} and X1X\_{1} stay at zero and Condition (4) follows from the explicit value of Fk0​(t,0)F^{0}\_{k}(t,0). The proof for the general kk and ρ∈[τ¯,T]\rho\in[\bar{\tau},T] is in the same spirit while lengthy.
∎

###### Lemma B.1.

The lower stochastic envelope v−v\_{-} satisfies the viscosity supersolution property ([3.18](https://arxiv.org/html/2510.21650v1#S3.E18 "In item (3) ‣ Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) at TKT\_{K}, under Definition [3.2](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem2 "Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proof.

Since vK,−v\_{K,-} itself is also LSC, we have vK,−,∗=vK,−v\_{K,-,\*}=v\_{K,-} and ℳ​[vK,−]∗=ℳ​[vK,−]{\mathcal{M}}[v\_{K,-}]\_{\*}={\mathcal{M}}[v\_{K,-}] by Lemma [A.1](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Assume on the contrary that there exists x¯:=(x¯0,x¯1)∈𝒮\bar{x}:=(\bar{x}\_{0},\bar{x}\_{1})\in{\mathcal{S}}, such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | max{\displaystyle\max\Big\{ | vK,−​(TK,x¯)−wK​[GK−x¯0−(x¯1−C​(−x¯1))+]+,\displaystyle v\_{K,-}(T\_{K},\bar{x})-w\_{K}\left[G\_{K}-\bar{x}\_{0}-(\bar{x}\_{1}-C(-\bar{x}\_{1}))^{+}\right]^{+}, |  | (B.7) |
|  |  | vK,−(TK,x¯)−ℳ[vK,−](TK,x¯)}<0.\displaystyle v\_{K,-}(T\_{K},\bar{x})-{\mathcal{M}}[v\_{K,-}](T\_{K},\bar{x})\Big\}<0. |  |

For ε>0\varepsilon>0 small enough, we define several sets for later use:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | B​(x¯,ε)\displaystyle B(\bar{x},\varepsilon) | :={x|x∈𝒮¯​ and ​|x−x¯|<ε},\displaystyle=\{x|x\in\overline{\mathcal{S}}\text{ and }|x-\bar{x}|<\varepsilon\}, |  | (B.8) |
|  | 𝒟​(TK,x¯,ε)\displaystyle\mathcal{D}(T\_{K},\bar{x},\varepsilon) | :=(TK−ε,TK]×B​(x¯,ε),\displaystyle=(T\_{K}-\varepsilon,T\_{K}]\times B(\bar{x},\varepsilon), |  |
|  | E​(ε)\displaystyle E(\varepsilon) | :=𝒟​(TK,x¯,ε)¯∖𝒟​(TK,x¯,ε/2).\displaystyle=\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}\setminus\mathcal{D}(T\_{K},\bar{x},\varepsilon/2). |  |

Since ℳ​[vK,−]{\mathcal{M}}[v\_{K,-}] is LSC and [GK−x0−(x1−C​(−x1))+]+\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+} is continuous, there exists ε>0\varepsilon>0 small enough, such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | max{\displaystyle\max\Big\{ | vK,−​(TK,x¯)−wK​[GK−x0−(x1−C​(−x1))+]+,\displaystyle v\_{K,-}(T\_{K},\bar{x})-w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}, |  | (B.9) |
|  |  | vK,−(TK,x¯)−ℳ[vK,−](t,x)}≤−ε,\displaystyle v\_{K,-}(T\_{K},\bar{x})-{\mathcal{M}}[v\_{K,-}](t,x)\Big\}\leq-\varepsilon, |  |

when (t,x)∈𝒟​(TK,x¯,ε)¯(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}.

As vK,−v\_{K,-} is LSC and E​(ε)E(\varepsilon) is compact, the function vK,−v\_{K,-} is bounded from below on E​(ε)E(\varepsilon). With a small enough η>0\eta>0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −inf(t,x)∈E​(ε)vK,−​(t,x)+vK,−​(TK,x¯)<ε24​η−ε.-\inf\_{(t,x)\in E(\varepsilon)}v\_{K,-}(t,x)+v\_{K,-}(T\_{K},\bar{x})<\frac{\varepsilon^{2}}{4\eta}-\varepsilon. |  | (B.10) |

Note that v−∈𝒱−v\_{-}\in{\mathcal{V}}^{-}. For p>0p>0, we define

|  |  |  |
| --- | --- | --- |
|  | ψε,η,p​(t,x):=vK,−​(TK,x¯)−|x−x¯|2η−p​(TK−t).\psi^{\varepsilon,\eta,p}(t,x):=v\_{K,-}(T\_{K},\bar{x})-\frac{|x-\bar{x}|^{2}}{\eta}-p(T\_{K}-t). |  |

With a large enough pp,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​[ψε,η,p]​(t,x)<0​ holds for ​(t,x)∈𝒟​(TK,x¯,ε)¯.{\mathcal{L}}[\psi^{\varepsilon,\eta,p}](t,x)<0\text{ holds for }(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. |  | (B.11) |

By the definition of E​(ε)E(\varepsilon), the property of vK,−v\_{K,-} in ([B.10](https://arxiv.org/html/2510.21650v1#A2.E10 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), and making pp sufficiently large, we obtain the following inequality when (t,x)∈E​(ε)(t,x)\in E(\varepsilon):

|  |  |  |
| --- | --- | --- |
|  | ψε,η,p​(t,x)<vK,−​(TK,x¯)−ε24​η<inf(t,x)∈E​(ε)vK,−​(t,x)−ε≤vK,−​(t,x)−ε.\displaystyle\psi^{\varepsilon,\eta,p}(t,x)<v\_{K,-}(T\_{K},\bar{x})-\frac{\varepsilon^{2}}{4\eta}<\inf\_{(t,x)\in E(\varepsilon)}v\_{K,-}(t,x)-\varepsilon\leq v\_{K,-}(t,x)-\varepsilon. |  |

Besides, ([B.9](https://arxiv.org/html/2510.21650v1#A2.E9 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψε,η,p​(t,x)≤vK,−​(TK,x¯)≤wK​[GK−x0−(x1−C​(−x1))+]+−ε,\psi^{\varepsilon,\eta,p}(t,x)\leq v\_{K,-}(T\_{K},\bar{x})\leq w\_{K}\left[G\_{K}-x\_{0}-(x\_{1}-C(-x\_{1}))^{+}\right]^{+}-\varepsilon, |  | (B.12) |

when (t,x)∈𝒟​(TK,x¯,ε)¯(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}.

Let 0<δ<ε0<\delta<\varepsilon be small enough and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | vKδ​(t,x)={vK,−​(t,x)∨(ψε,η,p​(t,x)+δ)on ​𝒟​(TK,x¯,ε)¯,vK,−​(t,x),otherwise.v^{\delta}\_{K}(t,x)=\left\{\begin{array}[]{cl}v\_{K,-}(t,x)\vee(\psi^{\varepsilon,\eta,p}(t,x)+\delta)&\text{on }\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)},\\ v\_{K,-}(t,x),&\text{otherwise}.\end{array}\right. |  | (B.13) |

We verify that (v1,−,…,vK−1,−,vKδ)(v\_{1,-},\ldots,v\_{K-1,-},v^{\delta}\_{K}) is a stochastic subsolution under Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Since vKδv^{\delta}\_{K} is LSC and satisfies the polynomial growth condition with order p0∈(0,1)p\_{0}\in(0,1), Conditions (1) and (2) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") are satisfied.

For Condition (3), we only need to verify it for vKδv^{\delta}\_{K}. As vKδ≥vK,−v^{\delta}\_{K}\geq v\_{K,-} everywhere, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | vKδ​(t,x)−ℳ​[vKδ]​(t,x)≤vKδ​(t,x)−ℳ​[vK,−]​(t,x).v^{\delta}\_{K}(t,x)-{\mathcal{M}}[v^{\delta}\_{K}](t,x)\leq v^{\delta}\_{K}(t,x)-{\mathcal{M}}[v\_{K,-}](t,x). |  | (B.14) |

If vKδ​(t,x)=vK,−​(t,x)v^{\delta}\_{K}(t,x)=v\_{K,-}(t,x), then Condition (3) is satisfied. If vKδ​(t,x)=ψε,η,p​(t,x)+δv^{\delta}\_{K}(t,x)=\psi^{\varepsilon,\eta,p}(t,x)+\delta instead, then it must be (t,x)∈𝒟​(TK,x¯,ε)¯(t,x)\in\overline{\mathcal{D}(T\_{K},\bar{x},\varepsilon)}. It leads to

|  |  |  |
| --- | --- | --- |
|  | ψε,η,p​(t,x)+δ−ℳ​[vK,−]​(t,x)\displaystyle\psi^{\varepsilon,\eta,p}(t,x)+\delta-{\mathcal{M}}[v\_{K,-}](t,x) |  |
|  |  |  |
| --- | --- | --- |
|  | =vK,−​(TK,x¯)−|x−x¯|2η−p​(TK−t)+δ−ℳ​[vK,−]​(t,x)\displaystyle=v\_{K,-}(T\_{K},\bar{x})-\frac{|x-\bar{x}|^{2}}{\eta}-p(T\_{K}-t)+\delta-{\mathcal{M}}[v\_{K,-}](t,x) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤vK,−​(TK,x¯)−ℳ​[vK,−]​(t,x)+δ\displaystyle\leq v\_{K,-}(T\_{K},\bar{x})-{\mathcal{M}}[v\_{K,-}](t,x)+\delta |  |
|  |  |  |
| --- | --- | --- |
|  | ≤−ε+δ<0,\displaystyle\leq-\varepsilon+\delta<0, |  |

where ([B.9](https://arxiv.org/html/2510.21650v1#A2.E9 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is used. Therefore, vKδv^{\delta}\_{K} satisfies Condition (3).

For Condition (4), as (v1,−,…,vK−1,−)(v\_{1,-},\ldots,v\_{K-1,-}) satisfies Condition (4) and vKδ≥vK,−v^{\delta}\_{K}\geq v\_{K,-} everywhere, we only need to prove it for vKδv^{\delta}\_{K}. Consider any random initial condition (τ¯,ξ)(\bar{\tau},\xi) with τ¯∈[TK−1,TK]\bar{\tau}\in[T\_{K-1},T\_{K}], ξ∈ℱτ¯\xi\in{\mathcal{F}}\_{\bar{\tau}}, and ℙ​(ξ∈𝒮¯)=1\mathbb{P}(\xi\in\overline{\mathcal{S}})=1. Note that the last withdrawal θK\theta\_{K} is specified by the liquidation. Define the event

|  |  |  |  |
| --- | --- | --- | --- |
|  | A:={(τ¯,ξ)∈𝒟​(TK,x¯,ε/2)}∩{ψε,η,p​(τ¯,ξ)+δ>vK,−​(τ¯,ξ)}.A:=\{(\bar{\tau},\xi)\in\mathcal{D}(T\_{K},\bar{x},\varepsilon/2)\}\cap\{\psi^{\varepsilon,\eta,p}(\bar{\tau},\xi)+\delta>v\_{K,-}(\bar{\tau},\xi)\}. |  | (B.15) |

Then A∈ℱτ¯A\in{\mathcal{F}}\_{\bar{\tau}}. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ1:=inf{t∈[τ¯,TK]|\displaystyle\tau^{1}:=\inf\big\{t\in[\bar{\tau},T\_{K}]\,\big| | (t,X(t;τ¯,ξ,θK,∅))∉𝒟(TK,x¯,ε/2)}∧TK\displaystyle(t,X(t;\bar{\tau},\xi,\theta\_{K},\emptyset))\notin\mathcal{D}(T\_{K},\bar{x},\varepsilon/2)\big\}\wedge T\_{K} |  |

be the exit time and denote

|  |  |  |
| --- | --- | --- |
|  | ξ1:=(ξ01,ξ11):=X​(τ1;τ¯,ξ,θK,∅)∈ℱτ1\displaystyle\xi^{1}:=(\xi^{1}\_{0},\xi^{1}\_{1}):=X(\tau^{1};\bar{\tau},\xi,\theta\_{K},\emptyset)\in{\mathcal{F}}\_{\tau^{1}} |  |

as the exit position. Since it is possible that τ1=T\tau^{1}=T, we also introduce

|  |  |  |
| --- | --- | --- |
|  | ξ1−:=(ξ01−,ξ11−):=X​(τ1−;τ¯,ξ,θK,∅)\displaystyle\xi^{1-}:=(\xi^{1-}\_{0},\xi^{1-}\_{1}):=X(\tau^{1}-;\bar{\tau},\xi,\theta\_{K},\emptyset) |  |

as the position that excludes any jump caused by θK\theta\_{K}.

Let ρ∈[τ¯,T]\rho\in[\bar{\tau},T] be another stopping time. For notational simplicity, denote

|  |  |  |
| --- | --- | --- |
|  | ψδ​(τ¯,ξ):=ψε,η,p​(τ¯,ξ)+δ.\psi^{\delta}(\bar{\tau},\xi):=\psi^{\varepsilon,\eta,p}(\bar{\tau},\xi)+\delta. |  |

Under the event AA,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏A​vKδ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A}v^{\delta}\_{K}(\bar{\tau},\xi) | =𝟏A​ψδ​(τ¯,ξ)\displaystyle=\mathbf{1}\_{A}\psi^{\delta}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[𝟏A​ψδ​(τ1∧ρ,X​((τ1∧ρ)−;τ¯,ξ,θK,∅))|ℱτ¯]\displaystyle\leq\mathbb{E}[\mathbf{1}\_{A}\psi^{\delta}(\tau^{1}\wedge\rho,X((\tau^{1}\wedge\rho)-;\bar{\tau},\xi,\theta\_{K},\emptyset))|{\mathcal{F}}\_{\bar{\tau}}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​[𝟏A∩{ρ<τ1}​ψδ​(ρ,X​(ρ;τ¯,ξ,θK,∅))|ℱτ¯]+𝔼​[𝟏A∩{ρ≥τ1}​ψδ​(τ1,ξ1−)|ℱτ¯].\displaystyle=\mathbb{E}[\mathbf{1}\_{A\cap\{\rho<\tau^{1}\}}\psi^{\delta}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))|{\mathcal{F}}\_{\bar{\tau}}]+\mathbb{E}[\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}}\psi^{\delta}(\tau^{1},\xi^{1-})|{\mathcal{F}}\_{\bar{\tau}}]. |  | (B.16) |

The first line follows from the definition of AA. The second line is from applying Itô’s formula to ψδ​(t,X)\psi^{\delta}(t,X) from τ¯\bar{\tau} to (τ1∧ρ)−(\tau^{1}\wedge\rho)-, together with ([B.11](https://arxiv.org/html/2510.21650v1#A2.E11 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")). The third line uses the definition of ξ1−\xi^{1-}.

When the event A∩{ρ<τ1}A\cap\{\rho<\tau^{1}\} happens, we have (ρ,X​(ρ;τ¯,ξ,θK,∅))∈𝒟​(TK,x¯,ε/2)(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))\in\mathcal{D}(T\_{K},\bar{x},\varepsilon/2). By the definition of vKδv^{\delta}\_{K},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏A∩{ρ<τ1}​ψδ​(ρ,X​(ρ;τ¯,ξ,θK,∅))≤𝟏A∩{ρ<τ1}​vKδ​(ρ,X​(ρ;τ¯,ξ,θK,∅)).\mathbf{1}\_{A\cap\{\rho<\tau^{1}\}}\psi^{\delta}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))\leq\mathbf{1}\_{A\cap\{\rho<\tau^{1}\}}v^{\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset)). |  | (B.17) |

For the second term in ([B.16](https://arxiv.org/html/2510.21650v1#A2.E16 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), we separate it into two cases. When τ1=TK\tau^{1}=T\_{K}, ([B.12](https://arxiv.org/html/2510.21650v1#A2.E12 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏A∩{ρ≥τ1}∩{τ1=TK}​ψδ​(τ1,ξ1−)≤𝟏A∩{ρ≥τ1}∩{τ1=TK}​wK​(GK−θK)+.\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap\{\tau^{1}=T\_{K}\}}\psi^{\delta}(\tau^{1},\xi^{1-})\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap\{\tau^{1}=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}. |  | (B.18) |

If τ1<TK\tau^{1}<T\_{K}, then

|  |  |  |
| --- | --- | --- |
|  | 𝟏A∩{ρ≥τ1}∩{τ1<TK}​ψδ​(τ1,ξ1−)\displaystyle\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap\{\tau^{1}<T\_{K}\}}\psi^{\delta}(\tau^{1},\xi^{1-}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩{τ1<TK}​vK,−​(τ1,ξ1−)\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap\{\tau^{1}<T\_{K}\}}v\_{K,-}(\tau^{1},\xi^{1-}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩{τ1<TK}​𝔼​[𝟏{ρ<TK}​vK,−​(ρ,X​(ρ;τ1,ξ1−,θK,∅))+𝟏{ρ=TK}​wK​(GK−θK)+|ℱτ1]\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap\{\tau^{1}<T\_{K}\}}\mathbb{E}[\mathbf{1}\_{\{\rho<T\_{K}\}}v\_{K,-}(\rho,X(\rho;\tau^{1},\xi^{1-},\theta\_{K},\emptyset))+\mathbf{1}\_{\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}|{\mathcal{F}}\_{\tau^{1}}] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏A∩{ρ≥τ1}∩{τ1<TK}​𝔼​[𝟏{ρ<TK}​vK,−​(ρ,X​(ρ;τ¯,ξ,θK,∅))+𝟏{ρ=TK}​wK​(GK−θK)+|ℱτ1]\displaystyle=\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap\{\tau^{1}<T\_{K}\}}\mathbb{E}[\mathbf{1}\_{\{\rho<T\_{K}\}}v\_{K,-}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))+\mathbf{1}\_{\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}|{\mathcal{F}}\_{\tau^{1}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩{τ1<TK}​𝔼​[𝟏{ρ<TK}​vKδ​(ρ,X​(ρ;τ¯,ξ,θK,∅))+𝟏{ρ=TK}​wK​(GK−θK)+|ℱτ1].\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap\{\tau^{1}<T\_{K}\}}\mathbb{E}[\mathbf{1}\_{\{\rho<T\_{K}\}}v^{\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))+\mathbf{1}\_{\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}|{\mathcal{F}}\_{\tau^{1}}]. |  | (B.19) |

The first inequality uses ξ1−∈∂B​(x¯,ε/2)\xi^{1-}\in\partial B(\bar{x},\varepsilon/2) when τ1<TK\tau^{1}<T\_{K}. The second inequality follows from the submartingale property of vK,−v\_{K,-}, with the random initial condition (τ1,ξ1−)(\tau^{1},\xi^{1-}). The equality uses the definition of X​(⋅;τ¯,ξ,θK,∅)X(\cdot;\bar{\tau},\xi,\theta\_{K},\emptyset). The last inequality is from the fact that vKδ≥vK,−v^{\delta}\_{K}\geq v\_{K,-} everywhere.

Combining ([B.18](https://arxiv.org/html/2510.21650v1#A2.E18 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([B.19](https://arxiv.org/html/2510.21650v1#A2.E19 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and taking expectation conditional on ℱτ¯{\mathcal{F}}\_{\bar{\tau}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝟏A∩{ρ≥τ1}​ψδ​(τ1,ξ1−)|ℱτ¯]\displaystyle\mathbb{E}[\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}}\psi^{\delta}(\tau^{1},\xi^{1-})|{\mathcal{F}}\_{\bar{\tau}}] |  | (B.20) |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A​𝔼​[𝟏{ρ≥τ1}∩{ρ<TK}​vKδ​(ρ,X​(ρ;τ¯,ξ,θK,∅))+𝟏{ρ≥τ1}∩{ρ=TK}​wK​(GK−θK)+|ℱτ¯].\displaystyle\leq\mathbf{1}\_{A}\mathbb{E}[\mathbf{1}\_{\{\rho\geq\tau^{1}\}\cap\{\rho<T\_{K}\}}v^{\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))+\mathbf{1}\_{\{\rho\geq\tau^{1}\}\cap\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}|{\mathcal{F}}\_{\bar{\tau}}]. |  |

With ([B.17](https://arxiv.org/html/2510.21650v1#A2.E17 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([B.20](https://arxiv.org/html/2510.21650v1#A2.E20 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), ([B.16](https://arxiv.org/html/2510.21650v1#A2.E16 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) reduces to

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​vKδ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A}v^{\delta}\_{K}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤𝟏A​𝔼​[𝟏{ρ<TK}​vKδ​(ρ,X​(ρ;τ¯,ξ,θK,∅))+𝟏{ρ=TK}​wK​(GK−θK)+|ℱτ¯].\displaystyle\leq\mathbf{1}\_{A}\mathbb{E}[\mathbf{1}\_{\{\rho<T\_{K}\}}v^{\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))+\mathbf{1}\_{\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}|{\mathcal{F}}\_{\bar{\tau}}]. |  | (B.21) |

Under the event AcA^{c}, we use the definition of AA, the submartingale property of vK,−v\_{K,-}, and vK,−≤vKδv\_{K,-}\leq v^{\delta}\_{K} everywhere, to derive

|  |  |  |
| --- | --- | --- |
|  | 𝟏Ac​vKδ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A^{c}}v^{\delta}\_{K}(\bar{\tau},\xi) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏Ac​vK,−​(τ¯,ξ)\displaystyle=\mathbf{1}\_{A^{c}}v\_{K,-}(\bar{\tau},\xi) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏Ac​𝔼​[𝟏{ρ<TK}​vK,−​(ρ,X​(ρ;τ¯,ξ,θK,∅))+𝟏{ρ=TK}​wK​(GK−θK)+|ℱτ¯]\displaystyle\leq\mathbf{1}\_{A^{c}}\mathbb{E}[\mathbf{1}\_{\{\rho<T\_{K}\}}v\_{K,-}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))+\mathbf{1}\_{\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}|{\mathcal{F}}\_{\bar{\tau}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤𝟏Ac​𝔼​[𝟏{ρ<TK}​vKδ​(ρ,X​(ρ;τ¯,ξ,θK,∅))+𝟏{ρ=TK}​wK​(GK−θK)+|ℱτ¯].\displaystyle\leq\mathbf{1}\_{A^{c}}\mathbb{E}[\mathbf{1}\_{\{\rho<T\_{K}\}}v^{\delta}\_{K}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{K},\emptyset))+\mathbf{1}\_{\{\rho=T\_{K}\}}w\_{K}(G\_{K}-\theta\_{K})^{+}|{\mathcal{F}}\_{\bar{\tau}}]. |  | (B.22) |

Putting ([B.21](https://arxiv.org/html/2510.21650v1#A2.E21 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([B.22](https://arxiv.org/html/2510.21650v1#A2.E22 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) together, we obtain Condition (4) as desired.

Hence, (v1,−,…,vK−1,−,vKδ)(v\_{1,-},\ldots,v\_{K-1,-},v^{\delta}\_{K}) is a stochastic subsolution under Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). However,

|  |  |  |
| --- | --- | --- |
|  | vKδ​(TK,x¯)=vK,−​(TK,x¯)+δ>vK,−​(TK,x¯),v^{\delta}\_{K}(T\_{K},\bar{x})=v\_{K,-}(T\_{K},\bar{x})+\delta>v\_{K,-}(T\_{K},\bar{x}), |  |

which contradicts with the definition of vK,−v\_{K,-} as a supremum.
∎

###### Lemma B.2.

The lower stochastic envelope v−v\_{-} satisfies the viscosity supersolution property ([3.17](https://arxiv.org/html/2510.21650v1#S3.E17 "In item (2) ‣ Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) at TkT\_{k}, k=1,…,K−1k=1,\ldots,K-1, under Definition [3.2](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem2 "Definition 3.2 (Viscosity supersolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

###### Proof.

Note that we also have vk,−,∗=vk,−v\_{k,-,\*}=v\_{k,-}, vk+1,−,∗=vk+1,−v\_{k+1,-,\*}=v\_{k+1,-}, and ℳ​[vk,−]∗=ℳ​[vk,−]{\mathcal{M}}[v\_{k,-}]\_{\*}={\mathcal{M}}[v\_{k,-}]. Assume on the contrary that there exists x¯:=(x¯0,x¯1)∈𝒮\bar{x}:=(\bar{x}\_{0},\bar{x}\_{1})\in{\mathcal{S}}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | max{\displaystyle\max\Big\{ | vk,−​(Tk,x¯)−inf0≤θk≤x¯0[wk​(Gk−θk)++vk+1,−​(Tk,x¯0−θk,x¯1)],\displaystyle v\_{k,-}(T\_{k},\bar{x})-\inf\_{0\leq\theta\_{k}\leq\bar{x}\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,-}(T\_{k},\bar{x}\_{0}-\theta\_{k},\bar{x}\_{1})\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | vk,−(Tk,x¯)−ℳ[vk,−](Tk,x¯)}<0.\displaystyle v\_{k,-}(T\_{k},\bar{x})-{\mathcal{M}}[v\_{k,-}](T\_{k},\bar{x})\Big\}<0. |  |

Since vk+1,−v\_{k+1,-} is LSC and the correspondence (x0,x1)↦↠{θk|0≤θk≤x0}(x\_{0},x\_{1})\mathrel{\mapstochar\twoheadrightarrow}\{\theta\_{k}|0\leq\theta\_{k}\leq x\_{0}\} is upper hemicontinuous, we obtain that

|  |  |  |
| --- | --- | --- |
|  | (x0,x1)↦inf0≤θk≤x0[wk​(Gk−θk)++vk+1,−​(Tk,x0−θk,x1)](x\_{0},x\_{1})\mapsto\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,-}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right] |  |

is LSC by aliprantis2006infinite.

For ε>0\varepsilon>0 small enough, with a slight abuse of notation, we define several sets for later use:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(x¯,ε)\displaystyle B(\bar{x},\varepsilon) | :={x|x∈𝒮¯​ and ​|x−x¯|<ε},\displaystyle=\{x|x\in\overline{\mathcal{S}}\text{ and }|x-\bar{x}|<\varepsilon\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟​(Tk,x¯,ε)\displaystyle\mathcal{D}(T\_{k},\bar{x},\varepsilon) | :=(Tk−ε,Tk]×B​(x¯,ε),\displaystyle=(T\_{k}-\varepsilon,T\_{k}]\times B(\bar{x},\varepsilon), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(ε)\displaystyle E(\varepsilon) | :=𝒟​(Tk,x¯,ε)¯∖𝒟​(Tk,x¯,ε/2).\displaystyle=\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}\setminus\mathcal{D}(T\_{k},\bar{x},\varepsilon/2). |  |

By the LSC property, there exists ε>0\varepsilon>0 small enough, such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | vk,−​(Tk,x¯)+ε≤inf0≤θk≤x0[wk​(Gk−θk)++vk+1,−​(Tk,x0−θk,x1)],\displaystyle v\_{k,-}(T\_{k},\bar{x})+\varepsilon\leq\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,-}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right], |  | (B.23) |
|  |  | vk,−​(Tk,x¯)+ε≤ℳ​[vk,−]​(t,x),\displaystyle v\_{k,-}(T\_{k},\bar{x})+\varepsilon\leq{\mathcal{M}}[v\_{k,-}](t,x), |  |

when (t,x)∈𝒟​(Tk,x¯,ε)¯(t,x)\in\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}.

Similarly, with a large enough p>0p>0 and small enough η>0\eta>0, we can define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψε,η,p​(t,x):=vk,−​(Tk,x¯)−|x−x¯|2η−p​(Tk−t).\psi^{\varepsilon,\eta,p}(t,x):=v\_{k,-}(T\_{k},\bar{x})-\frac{|x-\bar{x}|^{2}}{\eta}-p(T\_{k}-t). |  | (B.24) |

It satisfies the following properties:

* •

  For (t,x)∈𝒟​(Tk,x¯,ε)¯(t,x)\in\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)},

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ℒ​[ψε,η,p]​(t,x)<0.{\mathcal{L}}[\psi^{\varepsilon,\eta,p}](t,x)<0. |  | (B.25) |
* •

  When (t,x)∈E​(ε)(t,x)\in E(\varepsilon),

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ψε,η,p​(t,x)<vk,−​(Tk,x¯)−ε24​η<inf(t,x)∈E​(ε)vk,−​(t,x)−ε≤vk,−​(t,x)−ε.\displaystyle\psi^{\varepsilon,\eta,p}(t,x)<v\_{k,-}(T\_{k},\bar{x})-\frac{\varepsilon^{2}}{4\eta}<\inf\_{(t,x)\in E(\varepsilon)}v\_{k,-}(t,x)-\varepsilon\leq v\_{k,-}(t,x)-\varepsilon. |  | (B.26) |
* •

  Besides, ([B.23](https://arxiv.org/html/2510.21650v1#A2.E23 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([B.24](https://arxiv.org/html/2510.21650v1#A2.E24 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) imply that

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | ψε,η,p​(t,x)\displaystyle\psi^{\varepsilon,\eta,p}(t,x) | ≤inf0≤θk≤x0[wk​(Gk−θk)++vk+1,−​(Tk,x0−θk,x1)]−ε,\displaystyle\leq\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,-}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right]-\varepsilon, |  | (B.27) |
  |  | ψε,η,p​(t,x)\displaystyle\psi^{\varepsilon,\eta,p}(t,x) | ≤ℳ​[vk,−]​(t,x)−ε,\displaystyle\leq{\mathcal{M}}[v\_{k,-}](t,x)-\varepsilon, |  |

  when (t,x)∈𝒟​(Tk,x¯,ε)¯(t,x)\in\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}.

Let 0<δ<ε0<\delta<\varepsilon be small enough and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | vkδ​(t,x)={vk,−​(t,x)∨(ψε,η,p​(t,x)+δ)on ​𝒟​(Tk,x¯,ε)¯,vk,−​(t,x),otherwise.v^{\delta}\_{k}(t,x)=\left\{\begin{array}[]{cl}v\_{k,-}(t,x)\vee(\psi^{\varepsilon,\eta,p}(t,x)+\delta)&\text{on }\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)},\\ v\_{k,-}(t,x),&\text{otherwise}.\end{array}\right. |  | (B.28) |

We show that (v1,−,…,vk−1,−,vkδ,vk+1,−,…,vK,−)(v\_{1,-},\ldots,v\_{k-1,-},v^{\delta}\_{k},v\_{k+1,-},\ldots,v\_{K,-}) is a stochastic subsolution under Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Conditions (1), (2), (3) can be verified similarly as before.

For Condition (4), since vkδ≥vk,−v^{\delta}\_{k}\geq v\_{k,-} everywhere, we only need to prove it for τ¯∈[Tk−1,Tk]\bar{\tau}\in[T\_{k-1},T\_{k}]. Consider any random initial condition (τ¯,ξ)(\bar{\tau},\xi) with ξ∈ℱτ¯\xi\in{\mathcal{F}}\_{\bar{\tau}} and ℙ​(ξ∈𝒮¯)=1\mathbb{P}(\xi\in\overline{\mathcal{S}})=1 and any (τ¯,ξ)(\bar{\tau},\xi)-admissible withdrawals θk:K\theta\_{k:K}. Define the event

|  |  |  |
| --- | --- | --- |
|  | A:={(τ¯,ξ)∈𝒟​(Tk,x¯,ε/2)}∩{ψε,η,p​(τ¯,ξ)+δ>vk,−​(τ¯,ξ)}.A:=\{(\bar{\tau},\xi)\in\mathcal{D}(T\_{k},\bar{x},\varepsilon/2)\}\cap\{\psi^{\varepsilon,\eta,p}(\bar{\tau},\xi)+\delta>v\_{k,-}(\bar{\tau},\xi)\}. |  |

Then A∈ℱτ¯A\in{\mathcal{F}}\_{\bar{\tau}}. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ1:=inf{t∈[τ¯,Tk]|\displaystyle\tau^{1}:=\inf\big\{t\in[\bar{\tau},T\_{k}]\,\big| | (t,X(t;τ¯,ξ,θk:K,∅))∉𝒟(Tk,x¯,ε/2)}∧Tk\displaystyle(t,X(t;\bar{\tau},\xi,\theta\_{k:K},\emptyset))\notin\mathcal{D}(T\_{k},\bar{x},\varepsilon/2)\big\}\wedge T\_{k} |  |

be the exit time. Since it is possible that τ1=Tk\tau^{1}=T\_{k}, we introduce

|  |  |  |
| --- | --- | --- |
|  | ξ1−:=(ξ01−,ξ11−):=X​(τ1−;τ¯,ξ,θk:K,∅)\displaystyle\xi^{1-}:=(\xi^{1-}\_{0},\xi^{1-}\_{1}):=X(\tau^{1}-;\bar{\tau},\xi,\theta\_{k:K},\emptyset) |  |

as the position that excludes a possible jump at τ1\tau^{1}.

Let ρ∈[τ¯,T]\rho\in[\bar{\tau},T] be another stopping time. For notational simplicity, denote

|  |  |  |
| --- | --- | --- |
|  | ψδ​(τ¯,ξ):=ψε,η,p​(τ¯,ξ)+δ.\psi^{\delta}(\bar{\tau},\xi):=\psi^{\varepsilon,\eta,p}(\bar{\tau},\xi)+\delta. |  |

Under the event AA,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏A​vkδ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A}v^{\delta}\_{k}(\bar{\tau},\xi) | =𝟏A​ψδ​(τ¯,ξ)\displaystyle=\mathbf{1}\_{A}\psi^{\delta}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[𝟏A​ψδ​(τ1∧ρ,X​((τ1∧ρ)−;τ¯,ξ,θk:K,∅))|ℱτ¯]\displaystyle\leq\mathbb{E}[\mathbf{1}\_{A}\psi^{\delta}(\tau^{1}\wedge\rho,X((\tau^{1}\wedge\rho)-;\bar{\tau},\xi,\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\bar{\tau}}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​[𝟏A∩{ρ<τ1}​ψδ​(ρ,X​(ρ;τ¯,ξ,θk:K,∅))|ℱτ¯]+𝔼​[𝟏A∩{ρ≥τ1}​ψδ​(τ1,ξ1−)|ℱτ¯].\displaystyle=\mathbb{E}[\mathbf{1}\_{A\cap\{\rho<\tau^{1}\}}\psi^{\delta}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\bar{\tau}}]+\mathbb{E}[\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}}\psi^{\delta}(\tau^{1},\xi^{1-})|{\mathcal{F}}\_{\bar{\tau}}]. |  | (B.29) |

The inequality is from applying Itô’s formula to ψδ​(t,X)\psi^{\delta}(t,X) from τ¯\bar{\tau} to (τ1∧ρ)−(\tau^{1}\wedge\rho)-, together with ([B.25](https://arxiv.org/html/2510.21650v1#A2.E25 "In 1st item ‣ Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")).

When the event A∩{ρ<τ1}A\cap\{\rho<\tau^{1}\} happens, we have (ρ,X​(ρ;τ¯,ξ,θk:K,∅))∈𝒟​(TK,x¯,ε/2)(\rho,X(\rho;\bar{\tau},\xi,\theta\_{k:K},\emptyset))\in\mathcal{D}(T\_{K},\bar{x},\varepsilon/2). By the definition of vkδv^{\delta}\_{k},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏A∩{ρ<τ1}​ψδ​(ρ,X​(ρ;τ¯,ξ,θk:K,∅))≤𝟏A∩{ρ<τ1}​vkδ​(ρ,X​(ρ;τ¯,ξ,θk:K,∅)).\mathbf{1}\_{A\cap\{\rho<\tau^{1}\}}\psi^{\delta}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{k:K},\emptyset))\leq\mathbf{1}\_{A\cap\{\rho<\tau^{1}\}}v^{\delta}\_{k}(\rho,X(\rho;\bar{\tau},\xi,\theta\_{k:K},\emptyset)). |  | (B.30) |

For the second term in ([B.29](https://arxiv.org/html/2510.21650v1#A2.E29 "In Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), we introduce two events:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q1\displaystyle Q\_{1} | :={τ1<Tk}∪{τ1=Tk​ and ​ξ1−∉B​(x¯,ε/2)},\displaystyle:=\{\tau^{1}<T\_{k}\}\cup\{\tau^{1}=T\_{k}\text{ and }\xi^{1-}\notin B(\bar{x},\varepsilon/2)\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Q2\displaystyle Q\_{2} | :={τ1=Tk​ and ​ξ1−∈B​(x¯,ε/2)}.\displaystyle:=\{\tau^{1}=T\_{k}\text{ and }\xi^{1-}\in B(\bar{x},\varepsilon/2)\}. |  |

For Q1Q\_{1}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝟏A∩{ρ≥τ1}∩Q1​ψδ​(τ1,ξ1−)\displaystyle\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{1}}\psi^{\delta}(\tau^{1},\xi^{1-}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩Q1​vk,−​(τ1,ξ1−)\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{1}}v\_{k,-}(\tau^{1},\xi^{1-}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩Q1​𝔼​[ℋ​([τ1,ρ],vk:K,−,X​(⋅;τ1,ξ1−,θk:K,∅))|ℱτ1]\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{1}}\mathbb{E}[\mathcal{H}([\tau^{1},\rho],v\_{k:K,-},X(\cdot;\tau^{1},\xi^{1-},\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\tau^{1}}] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩Q1​𝔼​[ℋ​([τ1,ρ],(vkδ,vk+1:K,−),X​(⋅;τ1,ξ1−,θk:K,∅))|ℱτ1]\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{1}}\mathbb{E}[\mathcal{H}([\tau^{1},\rho],(v^{\delta}\_{k},v\_{k+1:K,-}),X(\cdot;\tau^{1},\xi^{1-},\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\tau^{1}}] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏A∩{ρ≥τ1}∩Q1​𝔼​[ℋ​([τ1,ρ],(vkδ,vk+1:K,−),X​(⋅;τ¯,ξ,θk:K,∅))|ℱτ1].\displaystyle=\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{1}}\mathbb{E}[\mathcal{H}([\tau^{1},\rho],(v^{\delta}\_{k},v\_{k+1:K,-}),X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\tau^{1}}]. |  |

The first inequality follows from ([B.26](https://arxiv.org/html/2510.21650v1#A2.E26 "In 2nd item ‣ Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and (τ1,ξ1−)∈E​(ε)(\tau^{1},\xi^{1-})\in E(\varepsilon). The second inequality uses the submartingale property of vk,−v\_{k,-}, with the random initial condition (τ1,ξ1−)(\tau^{1},\xi^{1-}). The third inequality is due to vk,−≤vkδv\_{k,-}\leq v^{\delta}\_{k} everywhere. The last equality is from the definition of X​(⋅;τ¯,ξ,θk:K,∅)X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset).

For Q2Q\_{2}, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝟏A∩{ρ≥τ1}∩Q2​ψδ​(τ1,ξ1−)\displaystyle\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{2}}\psi^{\delta}(\tau^{1},\xi^{1-}) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏A∩{ρ≥τ1}∩Q2​ψδ​(Tk,ξ1−)\displaystyle=\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{2}}\psi^{\delta}(T\_{k},\xi^{1-}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩Q2​𝔼​[wk​(Gk−θk)++vk+1,−​(Tk,ξ01−−θk,ξ11−)|ℱτ1]\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{2}}\mathbb{E}[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,-}(T\_{k},\xi^{1-}\_{0}-\theta\_{k},\xi^{1-}\_{1})|{\mathcal{F}}\_{\tau^{1}}] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏A∩{ρ≥τ1}∩Q2​𝔼​[wk​(Gk−θk)++vk+1,−​(Tk,ξ1)|ℱτ1]\displaystyle=\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{2}}\mathbb{E}[w\_{k}(G\_{k}-\theta\_{k})^{+}+v\_{k+1,-}(T\_{k},\xi^{1})|{\mathcal{F}}\_{\tau^{1}}] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝟏A∩{ρ≥τ1}∩Q2​𝔼​[wk​(Gk−θk)++ℋ​([Tk,ρ],vk+1:K,−,X​(⋅;Tk,ξ1,θk+1:K,∅))|ℱτ1]\displaystyle\leq\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{2}}\mathbb{E}[w\_{k}(G\_{k}-\theta\_{k})^{+}+\mathcal{H}([T\_{k},\rho],v\_{k+1:K,-},X(\cdot;T\_{k},\xi^{1},\theta\_{k+1:K},\emptyset))|{\mathcal{F}}\_{\tau^{1}}] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏A∩{ρ≥τ1}∩Q2​𝔼​[wk​(Gk−θk)++ℋ​([Tk,ρ],vk+1:K,−,X​(⋅;τ¯,ξ,θk:K,∅))|ℱτ1].\displaystyle=\mathbf{1}\_{A\cap\{\rho\geq\tau^{1}\}\cap Q\_{2}}\mathbb{E}[w\_{k}(G\_{k}-\theta\_{k})^{+}+\mathcal{H}([T\_{k},\rho],v\_{k+1:K,-},X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\tau^{1}}]. |  |

The first equality uses τ1=Tk\tau^{1}=T\_{k}. The first inequality follows from ([B.27](https://arxiv.org/html/2510.21650v1#A2.E27 "In 3rd item ‣ Appendix B Proofs of the stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and the fact that (Tk,ξ1−)∈𝒟​(Tk,x¯,ε)¯(T\_{k},\xi^{1-})\in\overline{\mathcal{D}(T\_{k},\bar{x},\varepsilon)}. The second equality holds due to the definition of ξ1−\xi^{1-} and ξ1\xi^{1}. The last two lines use the submartingale property of vk+1,−v\_{k+1,-}, with the random initial condition (Tk,ξ1)(T\_{k},\xi^{1}) and the definition of X​(⋅;τ¯,ξ,θk:K,∅)X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset).

Under the event AcA^{c}, it is direct to show

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏Ac​vkδ​(τ¯,ξ)\displaystyle\mathbf{1}\_{A^{c}}v^{\delta}\_{k}(\bar{\tau},\xi) | =𝟏Ac​vk,−​(τ¯,ξ)\displaystyle=\mathbf{1}\_{A^{c}}v\_{k,-}(\bar{\tau},\xi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝟏Ac​𝔼​[ℋ​([τ¯,ρ],vk:K,−,X​(⋅;τ¯,ξ,θk:K,∅))|ℱτ¯]\displaystyle\leq\mathbf{1}\_{A^{c}}\mathbb{E}[\mathcal{H}([\bar{\tau},\rho],v\_{k:K,-},X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\bar{\tau}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝟏Ac​𝔼​[ℋ​([τ¯,ρ],(vkδ,vk+1:K,−),X​(⋅;τ¯,ξ,θk:K,∅))|ℱτ¯].\displaystyle\leq\mathbf{1}\_{A^{c}}\mathbb{E}[\mathcal{H}([\bar{\tau},\rho],(v^{\delta}\_{k},v\_{k+1:K,-}),X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\bar{\tau}}]. |  |

Putting these inequalities together, we obtain the following Condition (4) as desired:

|  |  |  |
| --- | --- | --- |
|  | vkδ​(τ¯,ξ)≤𝔼​[ℋ​([τ¯,ρ],(vkδ,vk+1:K,−),X​(⋅;τ¯,ξ,θk:K,∅))|ℱτ¯].\displaystyle v^{\delta}\_{k}(\bar{\tau},\xi)\leq\mathbb{E}[\mathcal{H}([\bar{\tau},\rho],(v^{\delta}\_{k},v\_{k+1:K,-}),X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset))|{\mathcal{F}}\_{\bar{\tau}}]. |  |

Hence, (v1,−,…,vk−1,−,vkδ,vk+1,−,…,vK,−)(v\_{1,-},\ldots,v\_{k-1,-},v^{\delta}\_{k},v\_{k+1,-},\ldots,v\_{K,-}) is a stochastic subsolution under Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). However, vkδ​(Tk,x¯)=vk,−​(Tk,x¯)+δ>vk,−​(Tk,x¯)v^{\delta}\_{k}(T\_{k},\bar{x})=v\_{k,-}(T\_{k},\bar{x})+\delta>v\_{k,-}(T\_{k},\bar{x}), which contradicts with the definition of vk,−v\_{k,-} as a supremum.
∎

## Appendix C Proofs of the comparison principle

###### Proof of Proposition [6.1](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem1 "Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Choose q∈(p0,1)q\in(p\_{0},1) in Fk1​(t,x)F^{1}\_{k}(t,x). Moreover, we replace the constant 2 in CkC\_{k} by a sufficiently large constant specified later. For any η>1\eta>1, define

|  |  |  |
| --- | --- | --- |
|  | uη​(Tk,x):=η+1η​u​(Tk,x)+1η​Fk1​(Tk,x),vη​(Tk,x):=η−1η​v​(Tk,x)−1η​Fk1​(Tk,x).u\_{\eta}(T\_{k},x):=\frac{\eta+1}{\eta}u(T\_{k},x)+\frac{1}{\eta}F^{1}\_{k}(T\_{k},x),\quad v\_{\eta}(T\_{k},x):=\frac{\eta-1}{\eta}v(T\_{k},x)-\frac{1}{\eta}F^{1}\_{k}(T\_{k},x). |  |

The idea is to show uη​(Tk,x)−vη​(Tk,x)≤0u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x)\leq 0 for all η>1\eta>1 and x∈𝒮¯x\in\overline{\mathcal{S}}, which implies u​(Tk,x)−v​(Tk,x)≤0u(T\_{k},x)-v(T\_{k},x)\leq 0 when η→∞\eta\rightarrow\infty.

Assume on the contrary that, there exist x∗∈𝒮¯x^{\*}\in\overline{\mathcal{S}} and η>1\eta>1 such that

|  |  |  |
| --- | --- | --- |
|  | uη​(Tk,x∗)−vη​(Tk,x∗)>0.u\_{\eta}(T\_{k},x^{\*})-v\_{\eta}(T\_{k},x^{\*})>0. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | Cη:=supx∈𝒮¯{uη​(Tk,x)−vη​(Tk,x)}>0.C\_{\eta}:=\sup\_{x\in\overline{\mathcal{S}}}\big\{u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x)\big\}>0. |  |

For each n≥0n\geq 0, define

|  |  |  |
| --- | --- | --- |
|  | Φn​(x,x′):=uη​(Tk,x)−vη​(Tk,x′)−n2​|x−x′|2,x,x′∈𝒮¯.\Phi\_{n}(x,x^{\prime}):=u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x^{\prime})-\frac{n}{2}|x-x^{\prime}|^{2},\quad x,x^{\prime}\in\overline{\mathcal{S}}. |  |

We note that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | <uη​(Tk,x∗)−vη​(Tk,x∗)≤supx∈𝒮¯{uη​(Tk,x)−vη​(Tk,x)}\displaystyle<u\_{\eta}(T\_{k},x^{\*})-v\_{\eta}(T\_{k},x^{\*})\leq\sup\_{x\in\overline{\mathcal{S}}}\big\{u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x)\big\} |  | (C.1) |
|  |  | ≤supx,x′∈𝒮¯Φn+1​(x,x′)≤supx,x′∈𝒮¯Φn​(x,x′)≤supx,x′∈𝒮¯Φ0​(x,x′).\displaystyle\leq\sup\_{x,x^{\prime}\in\overline{\mathcal{S}}}\Phi\_{n+1}(x,x^{\prime})\leq\sup\_{x,x^{\prime}\in\overline{\mathcal{S}}}\Phi\_{n}(x,x^{\prime})\leq\sup\_{x,x^{\prime}\in\overline{\mathcal{S}}}\Phi\_{0}(x,x^{\prime}). |  |

Under the growth condition ([6.4](https://arxiv.org/html/2510.21650v1#S6.E4 "In item (3) ‣ Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and q>p0q>p\_{0} in Fk1​(t,x)F^{1}\_{k}(t,x), we have Φn​(x,x′)→−∞\Phi\_{n}(x,x^{\prime})\rightarrow-\infty when |(x,x′)|→+∞|(x,x^{\prime})|\rightarrow+\infty in 𝒮¯×𝒮¯\overline{\mathcal{S}}\times\overline{\mathcal{S}}. Together with the USC property of uη−vηu\_{\eta}-v\_{\eta}, then supx,x′∈𝒮¯Φn​(x,x′)\sup\_{x,x^{\prime}\in\overline{\mathcal{S}}}\Phi\_{n}(x,x^{\prime}) is attained at some (xn,xn′)(x\_{n},x^{\prime}\_{n}). The inequality ([C.1](https://arxiv.org/html/2510.21650v1#A3.E1 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) indicates that {(xn,xn′)}n=1∞\{(x\_{n},x^{\prime}\_{n})\}^{\infty}\_{n=1} is in the following set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(x,x′)∈𝒮¯×𝒮¯|uη​(Tk,x)−vη​(Tk,x′)≥0}.\big\{(x,x^{\prime})\in\overline{\mathcal{S}}\times\overline{\mathcal{S}}\;\big|\;u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x^{\prime})\geq 0\big\}. |  | (C.2) |

The USC property of uη​(Tk,x)−vη​(Tk,x′)u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x^{\prime}) shows that the set ([C.2](https://arxiv.org/html/2510.21650v1#A3.E2 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is closed. Since uη​(Tk,x)−vη​(Tk,x′)→−∞u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x^{\prime})\rightarrow-\infty when |(x,x′)|→+∞|(x,x^{\prime})|\rightarrow+\infty, the set ([C.2](https://arxiv.org/html/2510.21650v1#A3.E2 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is bounded. Therefore, the set ([C.2](https://arxiv.org/html/2510.21650v1#A3.E2 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is compact. Up to a subsequence, we can assume that {(xn,xn′)}n=1∞\{(x\_{n},x^{\prime}\_{n})\}^{\infty}\_{n=1} is convergent. Then ([C.1](https://arxiv.org/html/2510.21650v1#A3.E1 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) yields

|  |  |  |
| --- | --- | --- |
|  | 0<uη​(Tk,x∗)−vη​(Tk,x∗)≤uη​(Tk,xn)−vη​(Tk,xn′)−n2​|xn−xn′|2,0<u\_{\eta}(T\_{k},x^{\*})-v\_{\eta}(T\_{k},x^{\*})\leq u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},x^{\prime}\_{n})-\frac{n}{2}|x\_{n}-x^{\prime}\_{n}|^{2}, |  |

which means that

|  |  |  |
| --- | --- | --- |
|  | uη​(Tk,xn)−vη​(Tk,xn′)−{uη​(Tk,x∗)−vη​(Tk,x∗)}≥n2​|xn−xn′|2.u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},x^{\prime}\_{n})-\{u\_{\eta}(T\_{k},x^{\*})-v\_{\eta}(T\_{k},x^{\*})\}\geq\frac{n}{2}|x\_{n}-x^{\prime}\_{n}|^{2}. |  |

When n→∞n\rightarrow\infty, the left-hand side is bounded because of the USC property. Then we must have

|  |  |  |
| --- | --- | --- |
|  | limn→∞|xn−xn′|2=0.\lim\_{n\rightarrow\infty}|x\_{n}-x^{\prime}\_{n}|^{2}=0. |  |

Hence, there exists x¯∈𝒮¯\bar{x}\in\overline{\mathcal{S}} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞xn=limn→∞xn′=x¯.\lim\_{n\rightarrow\infty}x\_{n}=\lim\_{n\rightarrow\infty}x^{\prime}\_{n}=\bar{x}. |  | (C.3) |

By definition, we have

|  |  |  |
| --- | --- | --- |
|  | supx,x′∈𝒮¯Φn​(x,x′)=uη​(Tk,xn)−vη​(Tk,xn′)−n2​|xn−xn′|2.\sup\_{x,x^{\prime}\in\overline{\mathcal{S}}}\Phi\_{n}(x,x^{\prime})=u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},x^{\prime}\_{n})-\frac{n}{2}|x\_{n}-x^{\prime}\_{n}|^{2}. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≤lim supn→∞n2​|xn−xn′|2=lim supn→∞{uη​(Tk,xn)−vη​(Tk,xn′)−supx,x′∈𝒮¯Φn​(x,x′)}\displaystyle\leq\limsup\_{n\rightarrow\infty}\frac{n}{2}|x\_{n}-x^{\prime}\_{n}|^{2}=\limsup\_{n\rightarrow\infty}\Big\{u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},x^{\prime}\_{n})-\sup\_{x,x^{\prime}\in\overline{\mathcal{S}}}\Phi\_{n}(x,x^{\prime})\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤lim supn→∞{uη​(Tk,xn)−vη​(Tk,xn′)}+lim supn→∞{−supx,x′∈𝒮¯Φn​(x,x′)}\displaystyle\leq\limsup\_{n\rightarrow\infty}\Big\{u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},x^{\prime}\_{n})\Big\}+\limsup\_{n\rightarrow\infty}\Big\{-\sup\_{x,x^{\prime}\in\overline{\mathcal{S}}}\Phi\_{n}(x,x^{\prime})\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤uη​(Tk,x¯)−vη​(Tk,x¯)−supx∈𝒮¯{uη​(Tk,x)−vη​(Tk,x)}\displaystyle\leq u\_{\eta}(T\_{k},\bar{x})-v\_{\eta}(T\_{k},\bar{x})-\sup\_{x\in\overline{\mathcal{S}}}\big\{u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x)\big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤0.\displaystyle\leq 0. |  |

Here, we use the USC property and ([C.1](https://arxiv.org/html/2510.21650v1#A3.E1 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) in the second to last inequality. Hence, all the inequalities should be equalities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞n2​|xn−xn′|2=0 and uη​(Tk,x¯)−vη​(Tk,x¯)=supx∈𝒮¯{uη​(Tk,x)−vη​(Tk,x)}.\lim\_{n\rightarrow\infty}\frac{n}{2}|x\_{n}-x^{\prime}\_{n}|^{2}=0\quad\text{ and }\quad u\_{\eta}(T\_{k},\bar{x})-v\_{\eta}(T\_{k},\bar{x})=\sup\_{x\in\overline{\mathcal{S}}}\big\{u\_{\eta}(T\_{k},x)-v\_{\eta}(T\_{k},x)\big\}. |  | (C.4) |

It also implies that, up to another subsequence (still indexed with nn),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uη​(Tk,x¯)\displaystyle u\_{\eta}(T\_{k},\bar{x}) | =lim supn→∞uη​(Tk,xn)=limn→∞uη​(Tk,xn),\displaystyle=\limsup\_{n\rightarrow\infty}u\_{\eta}(T\_{k},x\_{n})=\lim\_{n\rightarrow\infty}u\_{\eta}(T\_{k},x\_{n}), |  | (C.5) |
|  | vη​(Tk,x¯)\displaystyle v\_{\eta}(T\_{k},\bar{x}) | =lim infn→∞vη​(Tk,xn′)=limn→∞vη​(Tk,xn′).\displaystyle=\liminf\_{n\rightarrow\infty}v\_{\eta}(T\_{k},x^{\prime}\_{n})=\lim\_{n\rightarrow\infty}v\_{\eta}(T\_{k},x^{\prime}\_{n}). |  |

We claim that x¯≠0\bar{x}\neq 0. In fact,

|  |  |  |
| --- | --- | --- |
|  | uη​(Tk,0)−vη​(Tk,0)=u​(Tk,0)−v​(Tk,0)+1η​(u​(Tk,0)+v​(Tk,0)+2​Fk1​(Tk,0)).\displaystyle u\_{\eta}(T\_{k},0)-v\_{\eta}(T\_{k},0)=u(T\_{k},0)-v(T\_{k},0)+\frac{1}{\eta}\Big(u(T\_{k},0)+v(T\_{k},0)+2F^{1}\_{k}(T\_{k},0)\Big). |  |

The assumption ([6.3](https://arxiv.org/html/2510.21650v1#S6.E3 "In item (3) ‣ Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) ensures that, when the constant 22 in CkC\_{k} from Fk1​(t,x)F^{1}\_{k}(t,x) is replaced by a sufficiently large constant, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(Tk,0)−v​(Tk,0)\displaystyle u(T\_{k},0)-v(T\_{k},0) | ≤0,\displaystyle\leq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(Tk,0)+v​(Tk,0)+2​Fk1​(Tk,0)\displaystyle u(T\_{k},0)+v(T\_{k},0)+2F^{1}\_{k}(T\_{k},0) | ≤4​∑i=kKwi​Gi−2​Ck<0.\displaystyle\leq 4\sum^{K}\_{i=k}w\_{i}G\_{i}-2C\_{k}<0. |  |

Then uη​(Tk,0)−vη​(Tk,0)<0u\_{\eta}(T\_{k},0)-v\_{\eta}(T\_{k},0)<0, which implies that x¯≠0\bar{x}\neq 0. Hence, we can assume that xn≠0x\_{n}\neq 0 and xn′≠0x^{\prime}\_{n}\neq 0 when nn is large enough.

By belak2019utility and ([5.9](https://arxiv.org/html/2510.21650v1#S5.E9 "In item (2) ‣ Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) in Lemma [5.3](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem3 "Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | max{\displaystyle\max\Big\{ | uη​(Tk,xn)−inf0≤θk≤xn,0[wk​(Gk−θk)++f​(Tk,xn,0−θk,xn,1)],\displaystyle u\_{\eta}(T\_{k},x\_{n})-\inf\_{0\leq\theta\_{k}\leq x\_{n,0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x\_{n,0}-\theta\_{k},x\_{n,1})\right], |  | (C.6) |
|  |  | uη(Tk,xn)−ℳ[uη]∗(Tk,xn)}≤−κ¯η,\displaystyle u\_{\eta}(T\_{k},x\_{n})-{\mathcal{M}}[u\_{\eta}]^{\*}(T\_{k},x\_{n})\Big\}\leq-\frac{\bar{\kappa}}{\eta}, |  |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | max{\displaystyle\max\Big\{ | vη​(Tk,xn′)−inf0≤θk≤xn,0′[wk​(Gk−θk)++f​(Tk,xn,0′−θk,xn,1′)],\displaystyle v\_{\eta}(T\_{k},x^{\prime}\_{n})-\inf\_{0\leq\theta\_{k}\leq x^{\prime}\_{n,0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x^{\prime}\_{n,0}-\theta\_{k},x^{\prime}\_{n,1})\right], |  | (C.7) |
|  |  | vη(Tk,xn′)−ℳ[vη]∗(Tk,xn′)}≥κ¯η.\displaystyle v\_{\eta}(T\_{k},x^{\prime}\_{n})-{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},x^{\prime}\_{n})\Big\}\geq\frac{\bar{\kappa}}{\eta}. |  |

Here, κ¯:=infnmin⁡{κkb​(xn),κkb​(xn′)}>0\bar{\kappa}:=\inf\_{n}\min\{\kappa^{b}\_{k}(x\_{n}),\kappa^{b}\_{k}(x^{\prime}\_{n})\}>0, where κkb​(⋅)\kappa^{b}\_{k}(\cdot) is defined in ([5.9](https://arxiv.org/html/2510.21650v1#S5.E9 "In item (2) ‣ Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")).

Suppose vη​(Tk,xn′)−inf0≤θk≤xn,0′[wk​(Gk−θk)++f​(Tk,xn,0′−θk,xn,1′)]≥κ¯/ηv\_{\eta}(T\_{k},x^{\prime}\_{n})-\inf\_{0\leq\theta\_{k}\leq x^{\prime}\_{n,0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x^{\prime}\_{n,0}-\theta\_{k},x^{\prime}\_{n,1})\right]\geq\bar{\kappa}/\eta does not hold for infinitely many nn. Then there exists NN large enough, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | vη​(Tk,xn′)−ℳ​[vη]∗​(Tk,xn′)≥κ¯η,n≥N.v\_{\eta}(T\_{k},x^{\prime}\_{n})-{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},x^{\prime}\_{n})\geq\frac{\bar{\kappa}}{\eta},\quad n\geq N. |  | (C.8) |

We proceed to obtain a contradiction. In the following steps, the threshold NN may vary line by line. First, by the definition of ℳ​[⋅]{\mathcal{M}}[\cdot], ([C.8](https://arxiv.org/html/2510.21650v1#A3.E8 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) implies that xn′∉𝒮∅x^{\prime}\_{n}\notin{\mathcal{S}}\_{\emptyset}. Since 𝒮∅{\mathcal{S}}\_{\emptyset} is open, it further implies that x¯∉𝒮∅\bar{x}\notin{\mathcal{S}}\_{\emptyset}.

By the convergence result in ([C.5](https://arxiv.org/html/2510.21650v1#A3.E5 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | uη​(Tk,x¯)−vη​(Tk,x¯)≤uη​(Tk,xn)−vη​(Tk,xn′)+κ¯4​η,n≥N.u\_{\eta}(T\_{k},\bar{x})-v\_{\eta}(T\_{k},\bar{x})\leq u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},x^{\prime}\_{n})+\frac{\bar{\kappa}}{4\eta},\quad n\geq N. |  | (C.9) |

The LSC property of ℳ​[vη]∗{\mathcal{M}}[v\_{\eta}]\_{\*} on 𝒮¯\overline{\mathcal{S}} leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​[vη]∗​(Tk,xn′)≥ℳ​[vη]∗​(Tk,x¯)−κ¯4​η,n≥N.{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},x^{\prime}\_{n})\geq{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},\bar{x})-\frac{\bar{\kappa}}{4\eta},\quad n\geq N. |  | (C.10) |

Besides, since vηv\_{\eta} is LSC, Lemma [A.1](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") proves that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​[vη]∗​(Tk,xn′)=ℳ​[vη]​(Tk,xn′) and ℳ​[vη]∗​(Tk,x¯)=ℳ​[vη]​(Tk,x¯).{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},x^{\prime}\_{n})={\mathcal{M}}[v\_{\eta}](T\_{k},x^{\prime}\_{n})\quad\text{ and }\quad{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},\bar{x})={\mathcal{M}}[v\_{\eta}](T\_{k},\bar{x}). |  | (C.11) |

As x¯∉𝒮∅\bar{x}\notin{\mathcal{S}}\_{\emptyset}, the LSC property of vηv\_{\eta} ensures the existence of an optimizer Δ∈D​(x¯)\Delta\in D(\bar{x}), such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​[vη]​(Tk,x¯)=vη​(Tk,Γ​(x¯,Δ)).{\mathcal{M}}[v\_{\eta}](T\_{k},\bar{x})=v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta)). |  | (C.12) |

Putting these results together, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uη​(Tk,x¯)−vη​(Tk,x¯)≤\displaystyle u\_{\eta}(T\_{k},\bar{x})-v\_{\eta}(T\_{k},\bar{x})\leq | uη​(Tk,xn)−vη​(Tk,xn′)+κ¯4​η\displaystyle u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},x^{\prime}\_{n})+\frac{\bar{\kappa}}{4\eta} | (by ([C.9](https://arxiv.org/html/2510.21650v1#A3.E9 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | uη​(Tk,xn)−ℳ​[vη]∗​(Tk,xn′)−κ¯η+κ¯4​η\displaystyle u\_{\eta}(T\_{k},x\_{n})-{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},x^{\prime}\_{n})-\frac{\bar{\kappa}}{\eta}+\frac{\bar{\kappa}}{4\eta} | (by ([C.8](https://arxiv.org/html/2510.21650v1#A3.E8 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | uη​(Tk,xn)−ℳ​[vη]∗​(Tk,x¯)+κ¯4​η−κ¯η+κ¯4​η\displaystyle u\_{\eta}(T\_{k},x\_{n})-{\mathcal{M}}[v\_{\eta}]\_{\*}(T\_{k},\bar{x})+\frac{\bar{\kappa}}{4\eta}-\frac{\bar{\kappa}}{\eta}+\frac{\bar{\kappa}}{4\eta} | (by ([C.10](https://arxiv.org/html/2510.21650v1#A3.E10 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | uη​(Tk,xn)−ℳ​[vη]​(Tk,x¯)−κ¯2​η\displaystyle u\_{\eta}(T\_{k},x\_{n})-{\mathcal{M}}[v\_{\eta}](T\_{k},\bar{x})-\frac{\bar{\kappa}}{2\eta} | (by ([C.11](https://arxiv.org/html/2510.21650v1#A3.E11 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | uη​(Tk,xn)−vη​(Tk,Γ​(x¯,Δ))−κ¯2​η,n≥N.\displaystyle u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta))-\frac{\bar{\kappa}}{2\eta},\quad n\geq N. | (by ([C.12](https://arxiv.org/html/2510.21650v1#A3.E12 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |

Next, we show that x¯∉𝒮∅¯∖𝒮∅\bar{x}\notin\overline{{\mathcal{S}}\_{\emptyset}}\setminus{\mathcal{S}}\_{\emptyset}. Indeed, if not, then Γ​(x¯,Δ)=0\Gamma(\bar{x},\Delta)=0 and

|  |  |  |
| --- | --- | --- |
|  | uη​(Tk,xn)−vη​(Tk,Γ​(x¯,Δ))\displaystyle u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta)) |  |
|  |  |  |
| --- | --- | --- |
|  | =uη​(Tk,xn)−vη​(Tk,0)\displaystyle\quad=u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},0) |  |
|  |  |  |
| --- | --- | --- |
|  | =u​(Tk,xn)−v​(Tk,0)+1η​{u​(Tk,xn)+v​(Tk,0)+Fk1​(Tk,xn)+Fk1​(Tk,0)}.\displaystyle\quad=u(T\_{k},x\_{n})-v(T\_{k},0)+\frac{1}{\eta}\big\{u(T\_{k},x\_{n})+v(T\_{k},0)+F^{1}\_{k}(T\_{k},x\_{n})+F^{1}\_{k}(T\_{k},0)\big\}. |  |

The assumptions ([6.3](https://arxiv.org/html/2510.21650v1#S6.E3 "In item (3) ‣ Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and ([6.4](https://arxiv.org/html/2510.21650v1#S6.E4 "In item (3) ‣ Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) guarantee that u​(Tk,xn)≤v​(Tk,0)u(T\_{k},x\_{n})\leq v(T\_{k},0). Moreover,

|  |  |  |
| --- | --- | --- |
|  | u​(Tk,xn)+v​(Tk,0)+Fk1​(Tk,xn)+Fk1​(Tk,0)≤4​∑i=kKwi​Gi−2​Ck<0.u(T\_{k},x\_{n})+v(T\_{k},0)+F^{1}\_{k}(T\_{k},x\_{n})+F^{1}\_{k}(T\_{k},0)\leq 4\sum^{K}\_{i=k}w\_{i}G\_{i}-2C\_{k}<0. |  |

Then it leads to uη​(Tk,xn)−vη​(Tk,Γ​(x¯,Δ))<0u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta))<0, which contradicts with the previous inequality.

We simplify uη​(Tk,xn)u\_{\eta}(T\_{k},x\_{n}) as follows:

* •

  ([C.6](https://arxiv.org/html/2510.21650v1#A3.E6 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) shows that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | uη​(Tk,xn)−ℳ​[uη]∗​(Tk,xn)≤−κ¯/η.u\_{\eta}(T\_{k},x\_{n})-{\mathcal{M}}[u\_{\eta}]^{\*}(T\_{k},x\_{n})\leq-\bar{\kappa}/\eta. |  | (C.13) |
* •

  Since x¯∉𝒮∅¯\bar{x}\notin\overline{{\mathcal{S}}\_{\emptyset}}, Lemma [A.1](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") proves that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ℳ​[uη]∗​(Tk,x¯)=ℳ​[uη]​(Tk,x¯).{\mathcal{M}}[u\_{\eta}]^{\*}(T\_{k},\bar{x})={\mathcal{M}}[u\_{\eta}](T\_{k},\bar{x}). |  | (C.14) |

  Moreover, since Γ​(x¯,Δ)\Gamma(\bar{x},\Delta) is feasible,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ℳ​[uη]​(Tk,x¯)≤uη​(Tk,Γ​(x¯,Δ)).{\mathcal{M}}[u\_{\eta}](T\_{k},\bar{x})\leq u\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta)). |  | (C.15) |
* •

  The USC property of ℳ​[uη]∗{\mathcal{M}}[u\_{\eta}]^{\*} yields

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ℳ​[uη]∗​(Tk,xn)≤ℳ​[uη]∗​(Tk,x¯)+κ¯2​η,n≥N.{\mathcal{M}}[u\_{\eta}]^{\*}(T\_{k},x\_{n})\leq{\mathcal{M}}[u\_{\eta}]^{\*}(T\_{k},\bar{x})+\frac{\bar{\kappa}}{2\eta},\quad n\geq N. |  | (C.16) |

Hence,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0<\displaystyle 0< | uη​(Tk,x¯)−vη​(Tk,x¯)\displaystyle u\_{\eta}(T\_{k},\bar{x})-v\_{\eta}(T\_{k},\bar{x}) | (by ([C.4](https://arxiv.org/html/2510.21650v1#A3.E4 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | uη​(Tk,xn)−vη​(Tk,Γ​(x¯,Δ))−κ¯2​η\displaystyle u\_{\eta}(T\_{k},x\_{n})-v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta))-\frac{\bar{\kappa}}{2\eta} |  | |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ℳ​[uη]∗​(Tk,xn)−κ¯η−vη​(Tk,Γ​(x¯,Δ))−κ¯2​η\displaystyle{\mathcal{M}}[u\_{\eta}]^{\*}(T\_{k},x\_{n})-\frac{\bar{\kappa}}{\eta}-v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta))-\frac{\bar{\kappa}}{2\eta} | (by ([C.13](https://arxiv.org/html/2510.21650v1#A3.E13 "In 1st item ‣ Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ℳ​[uη]∗​(Tk,x¯)+κ¯2​η−κ¯η−vη​(Tk,Γ​(x¯,Δ))−κ¯2​η\displaystyle{\mathcal{M}}[u\_{\eta}]^{\*}(T\_{k},\bar{x})+\frac{\bar{\kappa}}{2\eta}-\frac{\bar{\kappa}}{\eta}-v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta))-\frac{\bar{\kappa}}{2\eta} | (by ([C.16](https://arxiv.org/html/2510.21650v1#A3.E16 "In 3rd item ‣ Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | uη​(Tk,Γ​(x¯,Δ))−vη​(Tk,Γ​(x¯,Δ))−κ¯η\displaystyle u\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta))-v\_{\eta}(T\_{k},\Gamma(\bar{x},\Delta))-\frac{\bar{\kappa}}{\eta} | (by ([C.15](https://arxiv.org/html/2510.21650v1#A3.E15 "In 2nd item ‣ Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."))) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | uη​(Tk,x¯)−vη​(Tk,x¯)−κ¯η,\displaystyle u\_{\eta}(T\_{k},\bar{x})-v\_{\eta}(T\_{k},\bar{x})-\frac{\bar{\kappa}}{\eta}, |  | |

which is a contradiction. Therefore, we must have

|  |  |  |
| --- | --- | --- |
|  | vη​(Tk,xn′)−inf0≤θk≤xn,0′[wk​(Gk−θk)++f​(Tk,xn,0′−θk,xn,1′)]≥κ¯/ηv\_{\eta}(T\_{k},x^{\prime}\_{n})-\inf\_{0\leq\theta\_{k}\leq x^{\prime}\_{n,0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x^{\prime}\_{n,0}-\theta\_{k},x^{\prime}\_{n,1})\right]\geq\bar{\kappa}/\eta |  |

for infinitely many nn. Up to another subsequence, ([C.6](https://arxiv.org/html/2510.21650v1#A3.E6 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | vη​(Tk,xn′)−inf0≤θk≤xn,0′[wk​(Gk−θk)++f​(Tk,xn,0′−θk,xn,1′)]\displaystyle v\_{\eta}(T\_{k},x^{\prime}\_{n})-\inf\_{0\leq\theta\_{k}\leq x^{\prime}\_{n,0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x^{\prime}\_{n,0}-\theta\_{k},x^{\prime}\_{n,1})\right] |  | (C.17) |
|  |  | ≥κ¯η>0>−κ¯η≥uη​(Tk,xn)−inf0≤θk≤xn,0[wk​(Gk−θk)++f​(Tk,xn,0−θk,xn,1)].\displaystyle\geq\frac{\bar{\kappa}}{\eta}>0>-\frac{\bar{\kappa}}{\eta}\geq u\_{\eta}(T\_{k},x\_{n})-\inf\_{0\leq\theta\_{k}\leq x\_{n,0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x\_{n,0}-\theta\_{k},x\_{n,1})\right]. |  |

Since ff is continuous and bounded,

|  |  |  |
| --- | --- | --- |
|  | x=(x0,x1)↦inf0≤θk≤x0[wk​(Gk−θk)++f​(Tk,x0−θk,x1)]\displaystyle x=(x\_{0},x\_{1})\mapsto\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+f(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right] |  |

is a continuous function.

Letting n→∞n\rightarrow\infty in ([C.17](https://arxiv.org/html/2510.21650v1#A3.E17 "In Appendix C Proofs of the comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")), we obtain vη​(Tk,x¯)>uη​(Tk,x¯)v\_{\eta}(T\_{k},\bar{x})>u\_{\eta}(T\_{k},\bar{x}), which is also a contradiction. Then the claim follows as desired.
∎

###### Proof of Proposition [6.2](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem2 "Proposition 6.2 (Terminal comparison at 𝑇_𝐾). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Thanks to the strict classical subsolution property of FK1​(TK,x)F^{1}\_{K}(T\_{K},x) at x∈𝒮x\in{\mathcal{S}}, we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | vη​(TK,xn′)−wK​[GK−xn,0′−(xn,1′−C​(−xn,1′))+]+\displaystyle v\_{\eta}(T\_{K},x^{\prime}\_{n})-w\_{K}\left[G\_{K}-x^{\prime}\_{n,0}-(x^{\prime}\_{n,1}-C(-x^{\prime}\_{n,1}))^{+}\right]^{+} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥κ¯η>0>−κ¯η≥uη​(TK,xn)−wK​[GK−xn,0−(xn,1−C​(−xn,1))+]+,\displaystyle\geq\frac{\bar{\kappa}}{\eta}>0>-\frac{\bar{\kappa}}{\eta}\geq u\_{\eta}(T\_{K},x\_{n})-w\_{K}\left[G\_{K}-x\_{n,0}-(x\_{n,1}-C(-x\_{n,1}))^{+}\right]^{+}, |  |

with the same proof procedure in Proposition [6.1](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem1 "Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Letting n→∞n\rightarrow\infty, we have a contradiction as vη​(TK,x¯)−uη​(TK,x¯)>0v\_{\eta}(T\_{K},\bar{x})-u\_{\eta}(T\_{K},\bar{x})>0.
∎

###### Proof of Proposition [6.3](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem3 "Proposition 6.3 (Comparison principle: 𝑡∈[𝑇_{𝑘-1},𝑇_𝑘)). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

The claim follows directly from modifying the proof of Proposition [6.1](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem1 "Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") and applying Ishii’s lemma, which is similar to belak2022optimal. We also note that the strict classical subsolution property of Fk1​(t,x)F^{1}\_{k}(t,x) in ([5.8](https://arxiv.org/html/2510.21650v1#S5.E8 "In item (1) ‣ Lemma 5.3. ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is used to apply belak2019utility.
∎

## Appendix D Proofs of optimal strategies

###### Proof of Lemma [7.1](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem1 "Lemma 7.1. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Step 1. For any (t,x)∈[Tk−1,Tk]×𝒮¯(t,x)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}, k=1,…,Kk=1,\ldots,K, Condition (3) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") leads to

|  |  |  |
| --- | --- | --- |
|  | hk​(t,x)≤ℳ​[hk]​(t,x)≤ℳ​[hk∗]​(t,x)≤ℳ​[hk∗]∗​(t,x).\displaystyle h\_{k}(t,x)\leq{\mathcal{M}}[h\_{k}](t,x)\leq{\mathcal{M}}[h^{\*}\_{k}](t,x)\leq{\mathcal{M}}[h^{\*}\_{k}]^{\*}(t,x). |  |

Since ℳ​[hk∗]∗{\mathcal{M}}[h^{\*}\_{k}]^{\*} is USC, taking lim sup\limsup shows that hk∗​(t,x)≤ℳ​[hk∗]∗​(t,x)h^{\*}\_{k}(t,x)\leq{\mathcal{M}}[h^{\*}\_{k}]^{\*}(t,x), as required by the viscosity subsolution property.

Step 2. Fix x∈𝒮x\in{\mathcal{S}} and TkT\_{k}, k=1,…,K−1k=1,\ldots,K-1. Consider a sequence (sn,yn)→(Tk,x)(s\_{n},y\_{n})\rightarrow(T\_{k},x) where sn≤Tks\_{n}\leq T\_{k}, such that

|  |  |  |
| --- | --- | --- |
|  | limn→∞hk​(sn,yn)=hk∗​(Tk,x).\lim\_{n\rightarrow\infty}h\_{k}(s\_{n},y\_{n})=h^{\*}\_{k}(T\_{k},x). |  |

Recall that x0x\_{0} is the wealth in the bank account. For any constant θk∈[0,x0]\theta\_{k}\in[0,x\_{0}], define the (random) withdrawal for goal kk as

|  |  |  |
| --- | --- | --- |
|  | Θn:=min⁡{θk,X0​(Tk;sn,yn,∅,∅)},\Theta\_{n}:=\min\{\theta\_{k},X\_{0}(T\_{k};s\_{n},y\_{n},\emptyset,\emptyset)\}, |  |

which is ℱTk{\mathcal{F}}\_{T\_{k}}-measurable. The submartingale property (4) of hkh\_{k} yields

|  |  |  |
| --- | --- | --- |
|  | hk∗​(Tk,x)\displaystyle h^{\*}\_{k}(T\_{k},x) |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞hk​(sn,yn)\displaystyle=\lim\_{n\rightarrow\infty}h\_{k}(s\_{n},y\_{n}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤lim supn→∞𝔼​[wk​(Gk−Θn)++hk+1​(Tk,X0​(Tk;sn,yn,∅,∅)−Θn,X1​(Tk;sn,yn,∅,∅))]\displaystyle\leq\limsup\_{n\rightarrow\infty}\mathbb{E}\Big[w\_{k}(G\_{k}-\Theta\_{n})^{+}+h\_{k+1}(T\_{k},X\_{0}(T\_{k};s\_{n},y\_{n},\emptyset,\emptyset)-\Theta\_{n},X\_{1}(T\_{k};s\_{n},y\_{n},\emptyset,\emptyset))\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤lim supn→∞𝔼​[wk​(Gk−Θn)++hk+1∗​(Tk,X0​(Tk;sn,yn,∅,∅)−Θn,X1​(Tk;sn,yn,∅,∅))]\displaystyle\leq\limsup\_{n\rightarrow\infty}\mathbb{E}\Big[w\_{k}(G\_{k}-\Theta\_{n})^{+}+h^{\*}\_{k+1}(T\_{k},X\_{0}(T\_{k};s\_{n},y\_{n},\emptyset,\emptyset)-\Theta\_{n},X\_{1}(T\_{k};s\_{n},y\_{n},\emptyset,\emptyset))\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼​[lim supn→∞(wk​(Gk−Θn)++hk+1∗​(Tk,X0​(Tk;sn,yn,∅,∅)−Θn,X1​(Tk;sn,yn,∅,∅)))]\displaystyle\leq\mathbb{E}\Big[\limsup\_{n\rightarrow\infty}\Big(w\_{k}(G\_{k}-\Theta\_{n})^{+}+h^{\*}\_{k+1}(T\_{k},X\_{0}(T\_{k};s\_{n},y\_{n},\emptyset,\emptyset)-\Theta\_{n},X\_{1}(T\_{k};s\_{n},y\_{n},\emptyset,\emptyset))\Big)\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼​[wk​(Gk−θk)++hk+1∗​(Tk,x0−θk,x1)]\displaystyle\leq\mathbb{E}[w\_{k}(G\_{k}-\theta\_{k})^{+}+h^{\*}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})] |  |
|  |  |  |
| --- | --- | --- |
|  | =wk​(Gk−θk)++hk+1∗​(Tk,x0−θk,x1).\displaystyle=w\_{k}(G\_{k}-\theta\_{k})^{+}+h^{\*}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1}). |  |

Here, the second line uses the submartingale property (4) from sns\_{n} to TkT\_{k}. Note that Θn\Theta\_{n} is admissible. The third line follows from hk+1≤hk+1∗h\_{k+1}\leq h^{\*}\_{k+1}. The fourth line is from Fatou’s lemma and the fact that hk+1h\_{k+1} is bounded from above. The fifth line holds because XX has continuous paths, hk+1∗h^{\*}\_{k+1} is USC, and limn→∞Θn=θk\lim\_{n\rightarrow\infty}\Theta\_{n}=\theta\_{k}. The last line holds since these terms are deterministic. As θk∈[0,x0]\theta\_{k}\in[0,x\_{0}] is arbitrary, we obtain

|  |  |  |
| --- | --- | --- |
|  | hk∗​(Tk,x)≤inf0≤θk≤x0(wk​(Gk−θk)++hk+1∗​(Tk,x0−θk,x1)).h^{\*}\_{k}(T\_{k},x)\leq\inf\_{0\leq\theta\_{k}\leq x\_{0}}\Big(w\_{k}(G\_{k}-\theta\_{k})^{+}+h^{\*}\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\Big). |  |

The case for TKT\_{K} follows similarly by replacing Θn\Theta\_{n} with the liquidation value.

Step 3. Finally, fix (t,x)∈[Tk−1,Tk)×𝒮(t,x)\in[T\_{k-1},T\_{k})\times{\mathcal{S}}, k=1,…,Kk=1,\ldots,K. Consider (sn,yn)⊂[Tk−1,Tk)×𝒮(s\_{n},y\_{n})\subset[T\_{k-1},T\_{k})\times{\mathcal{S}}, such that (sn,yn)→(t,x)(s\_{n},y\_{n})\rightarrow(t,x) when n→∞n\rightarrow\infty and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞hk​(sn,yn)=hk∗​(t,x).\lim\_{n\rightarrow\infty}h\_{k}(s\_{n},y\_{n})=h^{\*}\_{k}(t,x). |  | (D.1) |

Define a test function φ∈C1,2​([Tk−1,Tk)×𝒮)\varphi\in C^{1,2}([T\_{k-1},T\_{k})\times{\mathcal{S}}), such that (t,x)(t,x) is a maximum point of hk∗−φh^{\*}\_{k}-\varphi, with

|  |  |  |
| --- | --- | --- |
|  | hk∗​(t,x)=φ​(t,x) and hk​(s,y)≤hk∗​(s,y)≤φ​(s,y)​ when ​(s,y)∈[Tk−1,Tk)×𝒮.h^{\*}\_{k}(t,x)=\varphi(t,x)\quad\text{ and }\quad h\_{k}(s,y)\leq h^{\*}\_{k}(s,y)\leq\varphi(s,y)\text{ when }(s,y)\in[T\_{k-1},T\_{k})\times{\mathcal{S}}. |  |

Set γn:=φ​(sn,yn)−hk​(sn,yn)\gamma\_{n}:=\varphi(s\_{n},y\_{n})-h\_{k}(s\_{n},y\_{n}). As φ\varphi is continuous and ([D.1](https://arxiv.org/html/2510.21650v1#A4.E1 "In Appendix D Proofs of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) holds, we have

|  |  |  |
| --- | --- | --- |
|  | 0≤γn→0, when ​n→∞.0\leq\gamma\_{n}\rightarrow 0,\quad\text{ when }n\rightarrow\infty. |  |

We introduce another sequence {δn}n\{\delta\_{n}\}\_{n} of strictly positive real numbers, satisfying

|  |  |  |
| --- | --- | --- |
|  | limn→∞δn=0andlimn→∞γnδn=0.\lim\_{n\rightarrow\infty}\delta\_{n}=0\quad\text{and}\quad\lim\_{n\rightarrow\infty}\frac{\gamma\_{n}}{\delta\_{n}}=0. |  |

Let ε>0\varepsilon>0 and define

|  |  |  |
| --- | --- | --- |
|  | ρn:=inf{t∈[sn,Tk]:|X​(t;sn,yn,∅,∅)−yn|≥ε}∧(sn+δn)∧Tk.\rho\_{n}:=\inf\{t\in[s\_{n},T\_{k}]:|X(t;s\_{n},y\_{n},\emptyset,\emptyset)-y\_{n}|\geq\varepsilon\}\wedge(s\_{n}+\delta\_{n})\wedge T\_{k}. |  |

For nn large enough, we have sn+δn<Tks\_{n}+\delta\_{n}<T\_{k} and ρn<Tk\rho\_{n}<T\_{k}. We apply the submartingale property of hkh\_{k}, the fact that hk≤φh\_{k}\leq\varphi, and Itô’s formula to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk​(sn,yn)≤\displaystyle h\_{k}(s\_{n},y\_{n})\leq | 𝔼​[hk​(ρn,X​(ρn;sn,yn,∅,∅))]\displaystyle\mathbb{E}[h\_{k}(\rho\_{n},X(\rho\_{n};s\_{n},y\_{n},\emptyset,\emptyset))] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​[φ​(ρn,X​(ρn;sn,yn,∅,∅))]\displaystyle\mathbb{E}[\varphi(\rho\_{n},X(\rho\_{n};s\_{n},y\_{n},\emptyset,\emptyset))] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | φ​(sn,yn)−𝔼​[∫snρnℒ​[φ]​(u,X​(u;sn,yn,∅,∅))​𝑑u].\displaystyle\varphi(s\_{n},y\_{n})-\mathbb{E}\Big[\int^{\rho\_{n}}\_{s\_{n}}{\mathcal{L}}[\varphi](u,X(u;s\_{n},y\_{n},\emptyset,\emptyset))du\Big]. |  |

Rearranging the terms and dividing by δn\delta\_{n}, we have

|  |  |  |
| --- | --- | --- |
|  | 1δn​𝔼​[∫snρnℒ​[φ]​(u,X​(u;xn,yn,∅,∅))​𝑑u]−γnδn≤0.\frac{1}{\delta\_{n}}\mathbb{E}\Big[\int^{\rho\_{n}}\_{s\_{n}}{\mathcal{L}}[\varphi](u,X(u;x\_{n},y\_{n},\emptyset,\emptyset))du\Big]-\frac{\gamma\_{n}}{\delta\_{n}}\leq 0. |  |

Sending n→∞n\rightarrow\infty, the dominated convergence theorem and mean value theorem show that

|  |  |  |
| --- | --- | --- |
|  | ℒ​[φ]​(t,x)≤0,(t,x)∈[Tk−1,Tk)×𝒮.{\mathcal{L}}[\varphi](t,x)\leq 0,\quad(t,x)\in[T\_{k-1},T\_{k})\times{\mathcal{S}}. |  |

∎

###### Proof of Lemma [7.2](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem2 "Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

If τ¯=Tk\bar{\tau}=T\_{k}, ([7.11](https://arxiv.org/html/2510.21650v1#S7.E11 "In Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) is trivial. Then we only need to prove

|  |  |  |
| --- | --- | --- |
|  | Vk​(τ¯,ξ)​𝟏{τ¯<Tk}≤𝔼​[Vk​(ρ,X​(ρ;τ¯,ξ,∅,∅))​𝟏{τ¯<Tk}|ℱτ¯].V\_{k}(\bar{\tau},\xi)\mathbf{1}\_{\{\bar{\tau}<T\_{k}\}}\leq\mathbb{E}\big[V\_{k}(\rho,X(\rho;\bar{\tau},\xi,\emptyset,\emptyset))\mathbf{1}\_{\{\bar{\tau}<T\_{k}\}}\big|{\mathcal{F}}\_{\bar{\tau}}\big]. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | ηn=min⁡{ρ,max⁡{Tk−1/n,τ¯}},n≥N.\eta\_{n}=\min\{\rho,\max\{T\_{k}-1/n,\bar{\tau}\}\},\quad n\geq N. |  |

Here, constant NN is large enough, such that Tk−1/N>0T\_{k}-1/N>0. Note that ηn\eta\_{n} is a stopping time. Moreover, τ¯≤ηn≤ρ\bar{\tau}\leq\eta\_{n}\leq\rho. If τ¯<Tk\bar{\tau}<T\_{k}, then ηn<Tk\eta\_{n}<T\_{k}. Instead, if τ¯=Tk\bar{\tau}=T\_{k}, then ηn=Tk\eta\_{n}=T\_{k}. Also, limn→∞ηn=ρ\lim\_{n\rightarrow\infty}\eta\_{n}=\rho.

Since VkV\_{k} is a stochastic subsolution and τ¯≤ηn<Tk\bar{\tau}\leq\eta\_{n}<T\_{k} when τ¯<Tk\bar{\tau}<T\_{k}, ([5.4](https://arxiv.org/html/2510.21650v1#S5.E4 "In item (4) ‣ Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") leads to

|  |  |  |
| --- | --- | --- |
|  | Vk​(τ¯,ξ)​𝟏{τ¯<Tk}≤𝔼​[Vk​(ηn,X​(ηn;τ¯,ξ,∅,∅))​𝟏{τ¯<Tk}|ℱτ¯].V\_{k}(\bar{\tau},\xi)\mathbf{1}\_{\{\bar{\tau}<T\_{k}\}}\leq\mathbb{E}\big[V\_{k}(\eta\_{n},X(\eta\_{n};\bar{\tau},\xi,\emptyset,\emptyset))\mathbf{1}\_{\{\bar{\tau}<T\_{k}\}}\big|{\mathcal{F}}\_{\bar{\tau}}\big]. |  |

Since VkV\_{k} is bounded and continuous and X​(⋅;τ¯,ξ,∅,∅)X(\cdot;\bar{\tau},\xi,\emptyset,\emptyset) has continuous paths, dominated convergence theorem shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(τ¯,ξ)​𝟏{τ¯<Tk}≤\displaystyle V\_{k}(\bar{\tau},\xi)\mathbf{1}\_{\{\bar{\tau}<T\_{k}\}}\leq | limn→∞𝔼​[Vk​(ηn,X​(ηn;τ¯,ξ,∅,∅))​𝟏{τ¯<Tk}|ℱτ¯]\displaystyle\lim\_{n\rightarrow\infty}\mathbb{E}\big[V\_{k}(\eta\_{n},X(\eta\_{n};\bar{\tau},\xi,\emptyset,\emptyset))\mathbf{1}\_{\{\bar{\tau}<T\_{k}\}}\big|{\mathcal{F}}\_{\bar{\tau}}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Vk​(ρ,X​(ρ;τ¯,ξ,∅,∅))​𝟏{τ¯<Tk}|ℱτ¯].\displaystyle\mathbb{E}\big[V\_{k}(\rho,X(\rho;\bar{\tau},\xi,\emptyset,\emptyset))\mathbf{1}\_{\{\bar{\tau}<T\_{k}\}}\big|{\mathcal{F}}\_{\bar{\tau}}\big]. |  |

Hence, the claim ([7.11](https://arxiv.org/html/2510.21650v1#S7.E11 "In Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) holds.
∎

###### Proof of Theorem [7.3](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem3 "Theorem 7.3. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.").

Clearly, (θk:K∗,Λ∗)(\theta^{\*}\_{k:K},\Lambda^{\*}) is admissible by construction. We only need to prove the optimality.

Denote constant λ∈(0,1)\lambda\in(0,1) and Wg>∑i=1Kwi​GiW\_{g}>\sum^{K}\_{i=1}w\_{i}G\_{i}. Consider the perturbed continuation and intervention regions defined as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒞i,λ\displaystyle{\mathcal{C}}\_{i,\lambda} | :={(t,x)∈[Ti−1,Ti]×𝒮¯:Vi​(t,x)+Wg​(1−λ)/λ<ℳ​[Vi]​(t,x)},\displaystyle:=\left\{(t,x)\in[T\_{i-1},T\_{i}]\times\overline{\mathcal{S}}:V\_{i}(t,x)+W\_{g}(1-\lambda)/\lambda<{\mathcal{M}}[V\_{i}](t,x)\right\}, |  | (D.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℐi,λ\displaystyle{\mathcal{I}}\_{i,\lambda} | :={(t,x)∈[Ti−1,Ti]×𝒮¯:Vi​(t,x)+Wg​(1−λ)/λ≥ℳ​[Vi]​(t,x)}.\displaystyle:=\left\{(t,x)\in[T\_{i-1},T\_{i}]\times\overline{\mathcal{S}}:V\_{i}(t,x)+W\_{g}(1-\lambda)/\lambda\geq{\mathcal{M}}[V\_{i}](t,x)\right\}. |  | (D.3) |

By Lemma [A.1](https://arxiv.org/html/2510.21650v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proofs of the stochastic supersolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."), ℳ​[Vi]{\mathcal{M}}[V\_{i}] is LSC on [Ti−1,Ti]×𝒮¯[T\_{i-1},T\_{i}]\times\overline{\mathcal{S}}. Then 𝒞i,λ{\mathcal{C}}\_{i,\lambda} is open and ℐi,λ{\mathcal{I}}\_{i,\lambda} is closed, respectively. We note that 𝒞i,λ{\mathcal{C}}\_{i,\lambda} can be empty when λ\lambda is close to zero. ℐi,λ{\mathcal{I}}\_{i,\lambda} is decreasing in λ\lambda and ℐi{\mathcal{I}}\_{i} in ([7.2](https://arxiv.org/html/2510.21650v1#S7.E2 "In 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) satisfies

|  |  |  |
| --- | --- | --- |
|  | ℐi=⋂λ∈(0,1)ℐi,λ.{\mathcal{I}}\_{i}=\bigcap\_{\lambda\in(0,1)}{\mathcal{I}}\_{i,\lambda}. |  |

Step 1. Given λ∈(0,1)\lambda\in(0,1) and (s,y)∈[Tk−1,Tk]×𝒮¯(s,y)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}, we define a stopping time as

|  |  |  |
| --- | --- | --- |
|  | ρλ,k,s,y:=inf{u∈[s,Tk]:(u,X​(u;s,y,∅,∅))∈ℐk,λ}∧Tk,\rho^{\lambda,k,s,y}:=\inf\{u\in[s,T\_{k}]:(u,X(u;s,y,\emptyset,\emptyset))\in{\mathcal{I}}\_{k,\lambda}\}\wedge T\_{k}, |  |

and two functions as

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk​(s,y)\displaystyle h\_{k}(s,y) | :=𝔼​[Vk​(ρλ,k,s,y,X​(ρλ,k,s,y;s,y,∅,∅))],\displaystyle:=\mathbb{E}\big[V\_{k}(\rho^{\lambda,k,s,y},X(\rho^{\lambda,k,s,y};s,y,\emptyset,\emptyset))\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | hk,λ​(s,y)\displaystyle h\_{k,\lambda}(s,y) | :=λ​Vk​(s,y)+(1−λ)​hk​(s,y).\displaystyle:=\lambda V\_{k}(s,y)+(1-\lambda)h\_{k}(s,y). |  |

Since 0≤Vk<Wg0\leq V\_{k}<W\_{g}, we have 0≤hk<Wg0\leq h\_{k}<W\_{g} and 0≤hk,λ<Wg0\leq h\_{k,\lambda}<W\_{g}.

Step 2. When k≠Kk\neq K, we verify that hk,λ∗h^{\*}\_{k,\lambda} is a USC viscosity subsolution on [Tk−1,Tk]×𝒮¯[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}, that is, it satisfies Conditions (1), (2), and (4) in Definition [3.1](https://arxiv.org/html/2510.21650v1#S3.Thmtheorem1 "Definition 3.1 (Viscosity subsolution). ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Since the value function VkV\_{k} is a viscosity supersolution, the comparison principle in Propositions [6.3](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem3 "Proposition 6.3 (Comparison principle: 𝑡∈[𝑇_{𝑘-1},𝑇_𝑘)). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") and [6.1](https://arxiv.org/html/2510.21650v1#S6.Thmtheorem1 "Proposition 6.1 (Terminal comparison at 𝑇_𝑘). ‣ 6 Comparison principle ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") yields that hk,λ≤hk,λ∗≤Vkh\_{k,\lambda}\leq h^{\*}\_{k,\lambda}\leq V\_{k} on [Tk−1,Tk]×𝒮¯[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}.

The idea is to show that Lemma [7.1](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem1 "Lemma 7.1. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") can be applied here.

* •

  Lemma [7.2](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem2 "Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") yields the submartingale property, where ρλ,k,s,y=Tk\rho^{\lambda,k,s,y}=T\_{k} is allowed:

  |  |  |  |
  | --- | --- | --- |
  |  | Vk​(s,y)≤𝔼​[Vk​(ρλ,k,s,y,X​(ρλ,k,s,y;s,y,∅,∅))]≤hk​(s,y),(s,y)∈[Tk−1,Tk]×𝒮¯.V\_{k}(s,y)\leq\mathbb{E}\big[V\_{k}(\rho^{\lambda,k,s,y},X(\rho^{\lambda,k,s,y};s,y,\emptyset,\emptyset))\big]\leq h\_{k}(s,y),\quad(s,y)\in[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}. |  |

  It implies that Vk≤hk,λV\_{k}\leq h\_{k,\lambda}.
* •

  The growth condition (2) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") of stochastic subsolutions holds since 0≤hk,λ<Wg0\leq h\_{k,\lambda}<W\_{g}.
* •

  Condition (3) about the non-decreasing property in transactions can be shown as follows. First,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ℳ​[hk,λ]​(s,y)\displaystyle{\mathcal{M}}[h\_{k,\lambda}](s,y) | ≥λ​ℳ​[Vk]​(s,y)+(1−λ)​ℳ​[hk]​(s,y)\displaystyle\geq\lambda{\mathcal{M}}[V\_{k}](s,y)+(1-\lambda){\mathcal{M}}[h\_{k}](s,y) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≥λ​ℳ​[Vk]​(s,y)+(1−λ)​ℳ​[Vk]​(s,y)\displaystyle\geq\lambda{\mathcal{M}}[V\_{k}](s,y)+(1-\lambda){\mathcal{M}}[V\_{k}](s,y) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =ℳ​[Vk]​(s,y).\displaystyle={\mathcal{M}}[V\_{k}](s,y). |  |

  Here, the second inequality uses hk≥Vkh\_{k}\geq V\_{k}.

  If (s,y)∈ℐk,λ(s,y)\in{\mathcal{I}}\_{k,\lambda}, then the stopping time ρλ,k,s,y=s\rho^{\lambda,k,s,y}=s, which leads to hk​(s,y)=Vk​(s,y)h\_{k}(s,y)=V\_{k}(s,y) and hk,λ​(s,y)=Vk​(s,y)h\_{k,\lambda}(s,y)=V\_{k}(s,y). Hence,

  |  |  |  |
  | --- | --- | --- |
  |  | ℳ​[hk,λ]​(s,y)≥ℳ​[Vk]​(s,y)≥Vk​(s,y)=hk,λ​(s,y), for ​(s,y)∈ℐk,λ.\displaystyle{\mathcal{M}}[h\_{k,\lambda}](s,y)\geq{\mathcal{M}}[V\_{k}](s,y)\geq V\_{k}(s,y)=h\_{k,\lambda}(s,y),\quad\text{ for }(s,y)\in{\mathcal{I}}\_{k,\lambda}. |  |

  The second inequality holds since VkV\_{k} satisfies Condition (3).

  Instead, if (s,y)∈𝒞k,λ(s,y)\in{\mathcal{C}}\_{k,\lambda}, then Vk​(s,y)+Wg​(1−λ)/λ<ℳ​[Vk]​(s,y)V\_{k}(s,y)+W\_{g}(1-\lambda)/\lambda<{\mathcal{M}}[V\_{k}](s,y). It yields

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ℳ​[hk,λ]​(s,y)\displaystyle{\mathcal{M}}[h\_{k,\lambda}](s,y) | ≥λ​ℳ​[Vk]​(s,y)+(1−λ)​ℳ​[hk]​(s,y)\displaystyle\geq\lambda{\mathcal{M}}[V\_{k}](s,y)+(1-\lambda){\mathcal{M}}[h\_{k}](s,y) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≥λ​Vk​(s,y)+Wg​(1−λ)+(1−λ)​ℳ​[hk]​(s,y)\displaystyle\geq\lambda V\_{k}(s,y)+W\_{g}(1-\lambda)+(1-\lambda){\mathcal{M}}[h\_{k}](s,y) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≥λ​Vk​(s,y)+(1−λ)​hk​(s,y)\displaystyle\geq\lambda V\_{k}(s,y)+(1-\lambda)h\_{k}(s,y) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =hk,λ​(s,y).\displaystyle=h\_{k,\lambda}(s,y). |  |

  The third inequality holds since Wg>hkW\_{g}>h\_{k} and (1−λ)​ℳ​[hk]​(s,y)≥0(1-\lambda){\mathcal{M}}[h\_{k}](s,y)\geq 0.
* •

  We show that (hk,λ,Vk+1:K)(h\_{k,\lambda},V\_{k+1:K}) satisfies the submartingale condition (4) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Since hk,λh\_{k,\lambda} is a linear combination of VkV\_{k} and hkh\_{k}, we only need to show that (hk,Vk+1:K)(h\_{k},V\_{k+1:K}) satisfies this condition. Consider a random initial condition (τ¯,ξ)(\bar{\tau},\xi) with τ¯∈[Tk−1,Tk]\bar{\tau}\in[T\_{k-1},T\_{k}]. Fix a stopping time ρ¯∈[τ¯,T]\bar{\rho}\in[\bar{\tau},T] and (τ¯,ξ)(\bar{\tau},\xi)-admissible withdrawals θk:K\theta\_{k:K}. For notational simplicity, we introduce the uncontrolled wealth process stopped at ρ¯∧Tk\bar{\rho}\wedge T\_{k} and TkT\_{k} as follows:

  |  |  |  |
  | --- | --- | --- |
  |  | η¯:=X​(ρ¯∧Tk;τ¯,ξ,∅,∅),ηTk:=X​(Tk;τ¯,ξ,∅,∅).\displaystyle\bar{\eta}:=X(\bar{\rho}\wedge T\_{k};\bar{\tau},\xi,\emptyset,\emptyset),\qquad\eta\_{T\_{k}}:=X(T\_{k};\bar{\tau},\xi,\emptyset,\emptyset). |  |

  Replacing (s,y)(s,y) in ρλ,k,s,y\rho^{\lambda,k,s,y} with random initial conditions, we define

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ρ1\displaystyle\rho\_{1} | :=ρλ,k,τ¯,ξ,η1:=X​(ρ1;τ¯,ξ,∅,∅),\displaystyle:=\rho^{\lambda,k,\bar{\tau},\xi},\quad\qquad\eta\_{1}:=X(\rho\_{1};\bar{\tau},\xi,\emptyset,\emptyset), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ρ2\displaystyle\rho\_{2} | :=ρλ,k,ρ¯∧Tk,η¯,η2:=X​(ρ2;ρ1,η1,∅,∅).\displaystyle:=\rho^{\lambda,k,\bar{\rho}\wedge T\_{k},\bar{\eta}},\qquad\eta\_{2}:=X(\rho\_{2};\rho\_{1},\eta\_{1},\emptyset,\emptyset). |  |

  We note that ρ1≤ρ2\rho\_{1}\leq\rho\_{2} since τ¯≤ρ¯∧Tk\bar{\tau}\leq\bar{\rho}\wedge T\_{k}.

  The submartingale property can be shown as follows:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | hk​(τ¯,ξ)=\displaystyle h\_{k}(\bar{\tau},\xi)= | 𝔼​[Vk​(ρ1,η1)|ℱτ¯]\displaystyle\mathbb{E}\big[V\_{k}(\rho\_{1},\eta\_{1})\big|{\mathcal{F}}\_{\bar{\tau}}\big] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ≤\displaystyle\leq | 𝔼​[𝟏{ρ¯<Tk}​Vk​(ρ2,η2)+𝟏{ρ¯≥Tk}​Vk​(Tk,X​(Tk;ρ1,η1,∅,∅))|ℱτ¯]\displaystyle\mathbb{E}\big[\mathbf{1}\_{\{\bar{\rho}<T\_{k}\}}V\_{k}(\rho\_{2},\eta\_{2})+\mathbf{1}\_{\{\bar{\rho}\geq T\_{k}\}}V\_{k}(T\_{k},X(T\_{k};\rho\_{1},\eta\_{1},\emptyset,\emptyset))\big|{\mathcal{F}}\_{\bar{\tau}}\big] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | =\displaystyle= | 𝔼​[𝟏{ρ¯<Tk}​Vk​(ρ2,X​(ρ2;ρ¯,η¯,∅,∅))+𝟏{ρ¯≥Tk}​Vk​(Tk,X​(Tk;τ¯,ξ,∅,∅))|ℱτ¯]\displaystyle\mathbb{E}\big[\mathbf{1}\_{\{\bar{\rho}<T\_{k}\}}V\_{k}(\rho\_{2},X(\rho\_{2};\bar{\rho},\bar{\eta},\emptyset,\emptyset))+\mathbf{1}\_{\{\bar{\rho}\geq T\_{k}\}}V\_{k}(T\_{k},X(T\_{k};\bar{\tau},\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\bar{\tau}}\big] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | =\displaystyle= | 𝔼​[𝟏{ρ¯<Tk}​hk​(ρ¯,η¯)+𝟏{ρ¯≥Tk}​Vk​(Tk,X​(Tk;τ¯,ξ,∅,∅))|ℱτ¯]\displaystyle\mathbb{E}\big[\mathbf{1}\_{\{\bar{\rho}<T\_{k}\}}h\_{k}(\bar{\rho},\bar{\eta})+\mathbf{1}\_{\{\bar{\rho}\geq T\_{k}\}}V\_{k}(T\_{k},X(T\_{k};\bar{\tau},\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\bar{\tau}}\big] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ≤\displaystyle\leq | 𝔼​[𝟏{ρ¯<Tk}​hk​(ρ¯,η¯)+𝟏{ρ¯≥Tk}​ℋ​([Tk,ρ¯],Vk+1:K,X​(⋅;Tk,ηTk,θk:K,∅))|ℱτ¯]\displaystyle\mathbb{E}\big[\mathbf{1}\_{\{\bar{\rho}<T\_{k}\}}h\_{k}(\bar{\rho},\bar{\eta})+\mathbf{1}\_{\{\bar{\rho}\geq T\_{k}\}}\mathcal{H}([T\_{k},\bar{\rho}],V\_{k+1:K},X(\cdot;T\_{k},\eta\_{T\_{k}},\theta\_{k:K},\emptyset))\big|{\mathcal{F}}\_{\bar{\tau}}\big] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | =\displaystyle= | 𝔼​[ℋ​([τ¯,ρ¯],(hk,Vk+1:K),X​(⋅;τ¯,ξ,θk:K,∅))|ℱτ¯].\displaystyle\mathbb{E}\big[\mathcal{H}([\bar{\tau},\bar{\rho}],(h\_{k},V\_{k+1:K}),X(\cdot;\bar{\tau},\xi,\theta\_{k:K},\emptyset))\big|{\mathcal{F}}\_{\bar{\tau}}\big]. |  |

  The first line is from the strong Markov property. The second line uses Lemma [7.2](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem2 "Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") from ρ1\rho\_{1} to ρ2\rho\_{2}. The third line uses the pathwise uniqueness:

  |  |  |  |
  | --- | --- | --- |
  |  | η2=X​(ρ2;ρ1,η1,∅,∅)=X​(ρ2;ρ¯,η¯,∅,∅) when ​ρ¯<Tk,\displaystyle\eta\_{2}=X(\rho\_{2};\rho\_{1},\eta\_{1},\emptyset,\emptyset)=X(\rho\_{2};\bar{\rho},\bar{\eta},\emptyset,\emptyset)\quad\text{ when }\bar{\rho}<T\_{k}, |  |
  |  |  |  |
  | --- | --- | --- |
  |  | X​(Tk;ρ1,η1,∅,∅)=X​(Tk;τ¯,ξ,∅,∅).\displaystyle X(T\_{k};\rho\_{1},\eta\_{1},\emptyset,\emptyset)=X(T\_{k};\bar{\tau},\xi,\emptyset,\emptyset). |  |

  Th fourth line uses the strong Markov property:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | hk​(ρ¯∧Tk,η¯)\displaystyle h\_{k}(\bar{\rho}\wedge T\_{k},\bar{\eta}) | =𝔼​[Vk​(ρ2,X​(ρ2;ρ¯∧Tk,η¯,∅,∅))|ℱρ¯∧Tk],\displaystyle=\mathbb{E}\big[V\_{k}(\rho\_{2},X(\rho\_{2};\bar{\rho}\wedge T\_{k},\bar{\eta},\emptyset,\emptyset))\big|{\mathcal{F}}\_{\bar{\rho}\wedge T\_{k}}\big], |  |

  and the tower property. The fifth line is from the submartingale property of VkV\_{k} from TkT\_{k} to ρ¯\bar{\rho}. The last line uses the pathwise uniqueness and the definition of ℋ\mathcal{H}.

Moreover, the boundary condition at 0 is satisfied as

|  |  |  |
| --- | --- | --- |
|  | hk,λ∗​(t,0)≤∑i=kKwi​Gi,t∈[Tk−1,Tk].h^{\*}\_{k,\lambda}(t,0)\leq\sum^{K}\_{i=k}w\_{i}G\_{i},\;t\in[T\_{k-1},T\_{k}]. |  |

Hence, the conditions to apply comparison principle are satisfied. We have hk,λ≤hk,λ∗≤Vkh\_{k,\lambda}\leq h^{\*}\_{k,\lambda}\leq V\_{k} on [Tk−1,Tk]×𝒮¯[T\_{k-1},T\_{k}]\times\overline{\mathcal{S}}.

Step 3. Fix n∈{0,1,2,…}n\in\{0,1,2,\ldots\}. For notational simplicity, we write

|  |  |  |
| --- | --- | --- |
|  | (τ,ξ):=(τn∗,k,ξn∗,k),ρλ:=ρλ,k,τ,ξ.(\tau,\xi):=(\tau^{\*,k}\_{n},\xi^{\*,k}\_{n}),\quad\rho^{\lambda}:=\rho^{\lambda,k,\tau,\xi}. |  |

The strong Markov property leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk​(τ,ξ)=\displaystyle h\_{k}(\tau,\xi)= | 𝔼​[Vk​(ρλ,k,s,y,X​(ρλ,k,s,y;s,y,∅,∅))]|(s,y)=(τ,ξ)\displaystyle\mathbb{E}\big[V\_{k}(\rho^{\lambda,k,s,y},X(\rho^{\lambda,k,s,y};s,y,\emptyset,\emptyset))\big]\big|\_{(s,y)=(\tau,\xi)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Vk​(ρλ,X​(ρλ;τ,ξ,∅,∅))|ℱτ] when ​τ≤Tk.\displaystyle\mathbb{E}\big[V\_{k}(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\tau}\big]\qquad\text{ when }\tau\leq T\_{k}. |  |

With Vk≥hk,λV\_{k}\geq h\_{k,\lambda}, we have

|  |  |  |
| --- | --- | --- |
|  | Vk​(τ,ξ)≥hk,λ​(τ,ξ)=λ​Vk​(τ,ξ)+(1−λ)​𝔼​[Vk​(ρλ,X​(ρλ;τ,ξ,∅,∅))|ℱτ] when ​τ≤Tk.V\_{k}(\tau,\xi)\geq h\_{k,\lambda}(\tau,\xi)=\lambda V\_{k}(\tau,\xi)+(1-\lambda)\mathbb{E}\big[V\_{k}(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\tau}\big]\quad\text{ when }\tau\leq T\_{k}. |  |

It yields

|  |  |  |
| --- | --- | --- |
|  | Vk​(τ,ξ)≥𝔼​[Vk​(ρλ,X​(ρλ;τ,ξ,∅,∅))|ℱτ] when ​τ≤Tk.V\_{k}(\tau,\xi)\geq\mathbb{E}\big[V\_{k}(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\tau}\big]\quad\text{ when }\tau\leq T\_{k}. |  |

Lemma [7.2](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem2 "Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.") gives another side of inequality. Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(τ,ξ)=𝔼​[Vk​(ρλ,X​(ρλ;τ,ξ,∅,∅))|ℱτ] when ​τ≤Tk.V\_{k}(\tau,\xi)=\mathbb{E}\big[V\_{k}(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\tau}\big]\quad\text{ when }\tau\leq T\_{k}. |  | (D.4) |

Step 4. By definition, ρλ≤τn+1∗,k∧Tk\rho^{\lambda}\leq\tau^{\*,k}\_{n+1}\wedge T\_{k}. Moreover, ρλ\rho^{\lambda} is nondecreasing in λ\lambda. Then the limit ρ:=limλ↑1ρλ\rho:=\lim\_{\lambda\uparrow 1}\rho^{\lambda} exists and ρ≤τn+1∗,k∧Tk\rho\leq\tau^{\*,k}\_{n+1}\wedge T\_{k}. Define two events

|  |  |  |
| --- | --- | --- |
|  | B1:={τ≤Tk}∩{τn+1∗,k≤Tk}={τn+1∗,k≤Tk},B2:={τ≤Tk}∩{τn+1∗,k>Tk}.B\_{1}:=\{\tau\leq T\_{k}\}\cap\{\tau^{\*,k}\_{n+1}\leq T\_{k}\}=\{\tau^{\*,k}\_{n+1}\leq T\_{k}\},\quad B\_{2}:=\{\tau\leq T\_{k}\}\cap\{\tau^{\*,k}\_{n+1}>T\_{k}\}. |  |

We obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​[Vk]​(ρ,X​(ρ;τ,ξ,∅,∅))≥\displaystyle{\mathcal{M}}[V\_{k}](\rho,X(\rho;\tau,\xi,\emptyset,\emptyset))\geq | Vk​(ρ,X​(ρ;τ,ξ,∅,∅))\displaystyle V\_{k}(\rho,X(\rho;\tau,\xi,\emptyset,\emptyset)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | limλ↑1Vk​(ρλ,X​(ρλ;τ,ξ,∅,∅))\displaystyle\lim\_{\lambda\uparrow 1}V\_{k}(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | lim infλ↑1(ℳ​[Vk]​(ρλ,X​(ρλ;τ,ξ,∅,∅))−Wg​(1−λ)/λ)\displaystyle\liminf\_{\lambda\uparrow 1}\Big({\mathcal{M}}[V\_{k}](\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))-W\_{g}(1-\lambda)/\lambda\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | ℳ​[Vk]​(ρ,X​(ρ;τ,ξ,∅,∅)) on ​B1.\displaystyle{\mathcal{M}}[V\_{k}](\rho,X(\rho;\tau,\xi,\emptyset,\emptyset))\qquad\text{ on }B\_{1}. |  |

Here, the first line is due to that VkV\_{k} satisfies Condition (3) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.E1 "In Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). The second line holds since VkV\_{k} is continuous and XX has continuous paths. The third line uses the definition of ℐk,λ{\mathcal{I}}\_{k,\lambda} and the fact that (ρλ,X​(ρλ;τ,ξ,∅,∅))∈ℐk,λ(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\in{\mathcal{I}}\_{k,\lambda} when B1B\_{1} happens. The last line relies on the LSC property of ℳ​[Vk]{\mathcal{M}}[V\_{k}]. It implies that all inequalities are equalities and ρ=τn+1∗,k\rho=\tau^{\*,k}\_{n+1} on B1B\_{1}. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(τ,ξ)=\displaystyle V\_{k}(\tau,\xi)= | limλ↑1𝔼​[Vk​(ρλ,X​(ρλ;τ,ξ,∅,∅))|ℱτ]\displaystyle\lim\_{\lambda\uparrow 1}\mathbb{E}\big[V\_{k}(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\tau}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | lim infλ↑1𝔼​[ℳ​[Vk]​(ρλ,X​(ρλ;τ,ξ,∅,∅))−Wg​(1−λ)/λ|ℱτ]\displaystyle\liminf\_{\lambda\uparrow 1}\mathbb{E}\Big[{\mathcal{M}}[V\_{k}](\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))-W\_{g}(1-\lambda)/\lambda\Big|{\mathcal{F}}\_{\tau}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | 𝔼​[ℳ​[Vk]​(τn+1∗,k,X​(τn+1∗,k;τ,ξ,∅,∅))|ℱτ]\displaystyle\mathbb{E}\Big[{\mathcal{M}}[V\_{k}](\tau^{\*,k}\_{n+1},X(\tau^{\*,k}\_{n+1};\tau,\xi,\emptyset,\emptyset))\Big|{\mathcal{F}}\_{\tau}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | 𝔼​[Vk​(τn+1∗,k,X​(τn+1∗,k;τ,ξ,∅,∅))|ℱτ]\displaystyle\mathbb{E}\Big[V\_{k}(\tau^{\*,k}\_{n+1},X(\tau^{\*,k}\_{n+1};\tau,\xi,\emptyset,\emptyset))\Big|{\mathcal{F}}\_{\tau}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | Vk​(τ,ξ) on ​B1.\displaystyle V\_{k}(\tau,\xi)\qquad\text{ on }B\_{1}. |  |

The first line uses ([D.4](https://arxiv.org/html/2510.21650v1#A4.E4 "In Appendix D Proofs of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")). The second line is again from the fact that (ρλ,X​(ρλ;τ,ξ,∅,∅))∈ℐk,λ(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\in{\mathcal{I}}\_{k,\lambda} when B1B\_{1} happens. The third line follows from Fatou’s lemma and the LSC property of ℳ​[Vk]{\mathcal{M}}[V\_{k}]. The fourth line holds because VkV\_{k} satisfies the non-decreasing property (3) in Definition [5.1](https://arxiv.org/html/2510.21650v1#S5.Thmtheorem1 "Definition 5.1 (Stochastic subsolution). ‣ 5 Stochastic subsolution ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). The last line uses Lemma [7.2](https://arxiv.org/html/2510.21650v1#S7.Thmtheorem2 "Lemma 7.2. ‣ 7 Construction of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113."). Then the inequalities are all equalities. By the definition of ξn+1∗,k\xi^{\*,k}\_{n+1}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(τn∗,k,ξn∗,k)=\displaystyle V\_{k}(\tau^{\*,k}\_{n},\xi^{\*,k}\_{n})= | 𝔼​[ℳ​[Vk]​(τn+1∗,k,X​(τn+1∗,k;τ,ξ,∅,∅))|ℱτn∗,k]\displaystyle\mathbb{E}\Big[{\mathcal{M}}[V\_{k}](\tau^{\*,k}\_{n+1},X(\tau^{\*,k}\_{n+1};\tau,\xi,\emptyset,\emptyset))\Big|{\mathcal{F}}\_{\tau^{\*,k}\_{n}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Vk​(τn+1∗,k,ξn+1∗,k)|ℱτn∗,k] on ​B1.\displaystyle\mathbb{E}\Big[V\_{k}(\tau^{\*,k}\_{n+1},\xi^{\*,k}\_{n+1})\Big|{\mathcal{F}}\_{\tau^{\*,k}\_{n}}\Big]\qquad\text{ on }B\_{1}. |  |

Instead, on B2B\_{2}, ρ=Tk\rho=T\_{k}. By dominated convergence theorem, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(τ,ξ)=\displaystyle V\_{k}(\tau,\xi)= | limλ↑1𝔼​[Vk​(ρλ,X​(ρλ;τ,ξ,∅,∅))|ℱτ]\displaystyle\lim\_{\lambda\uparrow 1}\mathbb{E}\big[V\_{k}(\rho^{\lambda},X(\rho^{\lambda};\tau,\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\tau}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Vk​(Tk,X​(Tk;τ,ξ,∅,∅))|ℱτ] on ​B2.\displaystyle\mathbb{E}\big[V\_{k}(T\_{k},X(T\_{k};\tau,\xi,\emptyset,\emptyset))\big|{\mathcal{F}}\_{\tau}\big]\quad\text{ on }B\_{2}. |  |

Putting them together, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vk(τn∗,k,ξn∗,k)𝟏{τn∗,k≤Tk}=𝔼[\displaystyle V\_{k}(\tau^{\*,k}\_{n},\xi^{\*,k}\_{n})\mathbf{1}\_{\{\tau^{\*,k}\_{n}\leq T\_{k}\}}=\mathbb{E}\Big[ | Vk​(τn+1∗,k,ξn+1∗,k)​𝟏{τn+1∗,k≤Tk}\displaystyle V\_{k}(\tau^{\*,k}\_{n+1},\xi^{\*,k}\_{n+1})\mathbf{1}\_{\{\tau^{\*,k}\_{n+1}\leq T\_{k}\}} |  | (D.5) |
|  |  | +Vk(Tk,X(Tk;τn∗,k,ξn∗,k,∅,∅))𝟏{τn∗,k≤Tk}∩{τn+1∗,k>Tk}|ℱτn∗,k].\displaystyle+V\_{k}(T\_{k},X(T\_{k};\tau^{\*,k}\_{n},\xi^{\*,k}\_{n},\emptyset,\emptyset))\mathbf{1}\_{\{\tau^{\*,k}\_{n}\leq T\_{k}\}\cap\{\tau^{\*,k}\_{n+1}>T\_{k}\}}\Big|{\mathcal{F}}\_{\tau^{\*,k}\_{n}}\Big]. |  |

Iteratively applying this equality on n=0,1,…n=0,1,\ldots, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(t,x)=\displaystyle V\_{k}(t,x)= | limn→∞𝔼​[Vk​(τn∗,k,ξn∗,k)​𝟏{τn∗,k≤Tk}+Vk​(Tk,X​(Tk;τ0∗,k,ξ0∗,k,∅,Λk∗))​𝟏{τn∗,k>Tk}]\displaystyle\lim\_{n\rightarrow\infty}\mathbb{E}\Big[V\_{k}(\tau^{\*,k}\_{n},\xi^{\*,k}\_{n})\mathbf{1}\_{\{\tau^{\*,k}\_{n}\leq T\_{k}\}}+V\_{k}(T\_{k},X(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\emptyset,\Lambda^{\*}\_{k}))\mathbf{1}\_{\{\tau^{\*,k}\_{n}>T\_{k}\}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[Vk​(Tk,X​(Tk;τ0∗,k,ξ0∗,k,∅,Λk∗))]\displaystyle\mathbb{E}\Big[V\_{k}(T\_{k},X(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\emptyset,\Lambda^{\*}\_{k}))\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[wi​(Gi−θk∗)++Vk+1​(Tk,X​(Tk;τ0∗,k,ξ0∗,k,θk∗,Λk∗))].\displaystyle\mathbb{E}\Big[w\_{i}(G\_{i}-\theta^{\*}\_{k})^{+}+V\_{k+1}(T\_{k},X(T\_{k};\tau^{\*,k}\_{0},\xi^{\*,k}\_{0},\theta^{\*}\_{k},\Lambda^{\*}\_{k}))\Big]. |  |

Here, the first line uses ([D.5](https://arxiv.org/html/2510.21650v1#A4.E5 "In Appendix D Proofs of optimal strategies ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) and the definition of Λ∗\Lambda^{\*}. The second line follows from the dominated convergence theorem and the fact that ℙ​(limn→∞τn∗,k>Tk)=1\mathbb{P}(\lim\_{n\rightarrow\infty}\tau^{\*,k}\_{n}>T\_{k})=1. The last line relies on the definition of θk∗\theta^{\*}\_{k} and the following fact: Since VkV\_{k} is a viscosity solution of ([3.7](https://arxiv.org/html/2510.21650v1#S3.E7 "In item (2) ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) at TkT\_{k} with the boundary condition ([3.9](https://arxiv.org/html/2510.21650v1#S3.E9 "In item (4) ‣ 3 The QVI system ‣ Goal-based portfolio selection with fixed transaction costs1footnote 11footnote 1Erhan Bayraktar is partially supported by the National Science Foundation under grant DMS-2507940 and by the Susan M. Smith chair. Bingyan Han is partially supported by The Hong Kong University of Science and Technology (Guangzhou) Start-up Fund G0101000197 and the Guangzhou-HKUST(GZ) Joint Funding Scheme (No. 2025A03J3858). Jingjie Zhang is supported by the National Natural Science Foundation of China under Grant No.12201113.")) at x=0x=0, we have

|  |  |  |
| --- | --- | --- |
|  | Vk​(Tk,x)=minn∈{0,1,2,…}⁡ℳn​[Uk]​(x),x∈𝒮¯,V\_{k}(T\_{k},x)=\min\_{n\in\{0,1,2,\ldots\}}{\mathcal{M}}^{n}[U\_{k}](x),\quad x\in\overline{\mathcal{S}}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uk​(x):=\displaystyle U\_{k}(x)= | inf0≤θk≤x0[wk​(Gk−θk)++Vk+1​(Tk,x0−θk,x1)],x∈𝒮¯.\displaystyle\inf\_{0\leq\theta\_{k}\leq x\_{0}}\left[w\_{k}(G\_{k}-\theta\_{k})^{+}+V\_{k+1}(T\_{k},x\_{0}-\theta\_{k},x\_{1})\right],\quad x\in\overline{\mathcal{S}}. |  |

Step 5. We repeat Step 1 to 4 above, until k=Kk=K. Only the terminal condition at TT is different and requires slight modifications. Then we finally have the desired result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(t,x)=\displaystyle V\_{k}(t,x)= | 𝔼​[∑i=kKwi​(Gi−θk∗)+].\displaystyle\mathbb{E}\Big[\sum^{K}\_{i=k}w\_{i}(G\_{i}-\theta^{\*}\_{k})^{+}\Big]. |  |

∎