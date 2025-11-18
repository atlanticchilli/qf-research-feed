---
authors:
- Bohan Li
- Wenyuan Li
- Kenneth Tsz Hin Ng
- Sheung Chi Phillip Yam
doc_id: arxiv:2511.12292v1
family_id: arxiv:2511.12292
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Mean Field Analysis of Mutual Insurance Market
url_abs: http://arxiv.org/abs/2511.12292v1
url_html: https://arxiv.org/html/2511.12292v1
venue: arXiv q-fin
version: 1
year: 2025
---


Bohan Li
Center for Financial Engineering, Soochow University, Suzhou, Jiangsu, China. Email: bhli@suda.edu.cn

Wenyuan Li
Department of Statistics and Actuarial Science, The University of Hong Kong, Pokfulam, Hong Kong. Email: wylsaas@hku.hk

Kenneth Tsz Hin Ng
Department of Mathematics, The Ohio State University, Columbus, Ohio, US. Email: ng.499@osu.edu

Sheung Chi Phillip Yam
Department of Statistics and Data Science, The Chinese University of Hong Kong, Shatin, Hong Kong. Email: scpyam@sta.cuhk.edu.hk

(November 15, 2025)

###### Abstract

A mutual insurance company (MIC) is a type of consumer cooperative owned by its policyholders. By purchasing insurance from an MIC, policyholders effectively become member-owners of the company and are entitled to a share of the surplus, which is determined by their own collective claims and premium contributions. This sharing mechanism creates an interactive environment in which individual insurance strategies are influenced by the actions of others. Given that mutual insurers account for nearly one-third of the global insurance market, the analysis of members’ behavior under such a sharing mechanism is of both practical and theoretical importance. This article presents a first dynamic study of members’ behavior in the prevalent mutual insurance market under the large-population limit. With members’ wealth processes depending on the law of the insurance strategies, we model the surplus-sharing mechanism using an extended mean field game (MFG) framework and address the fundamental question of how strategic interactions in this setting influence individual decisions. Mathematically, we establish the global-in-time existence and uniqueness of the mean field forward-backward stochastic differential equation (MF-FBSDE) characterizing the Nash equilibrium strategy, employing techniques to accommodate realistic insurance constraints.
Computationally, we develop a modified deep BSDE algorithm capable of solving the extended MFG problem with an additional fixed-point structure on the control. Utilizing this scheme, we examine how structural features of the MIC’s design, such as the composition of risk classes and surplus-sharing proportions, reshape members’ decisions and wealth through collective interactions, underscoring the central role of these mechanisms in MICs.

Keywords: Mutual insurance, extended mean field games, mean field forward-backward stochastic differential equations, global in time solution, method of continuation, deep BSDE method

## 1 Introduction

Mutual insurance companies (MICs) are one of the two most prevalent forms of centralized insurance providers in the industry, with a history dating back to the 18th century. Originating as community-based risk-sharing arrangements, early MICs gained traction in response to emerging urban risks, particularly frequent house fires. During the 19th century, industrialization introduced new hazards to high-risk occupations such as railroad workers. In response, U.S. railroad workers formed mutual benefit societies like the Brotherhood of Railroad Trainmen, which pooled member dues to provide life and disability benefits, reflecting the same mutual aid principles found in modern MICs. Today, the global mutual insurance market remains stable, accounting for 26.37% of the global insurance industry and generating approximately USD 1.41 trillion in premiums worldwide.111According to the International Cooperative and Mutual Insurance Federation’s [global mutual market share report in 2024](https://www.icmif.org/mms-2024/)

Unlike shareholder-owned insurance companies (SICs), the other major form of insurance providers, an MIC is owned entirely by its policyholders or members (\@BBOPcite\@BAP\@BBNvaughan2007fundamentals; RejdaMcNamara2016\@BBCP). Consequently, the surplus (or deficit) in an MIC, calculated as the premium income minus claims paid, reserves, and operating expenses, is shared among the members. This surplus may be distributed as dividends, premium adjustments, or other benefits, depending on the practice of the company. Hence, the net price of a policy is known ex post, which is defined as the premium paid minus the shared surplus received. Such a sharing mechanism is absent in SICs, as policyholders are not necessarily the owners of the company. The following table compares these two types of insurance companies.

Table 1: Comparisons between MICs and SICs

|  |  |  |
| --- | --- | --- |
|  | MIC | SIC |
| Ownership | Policyholders | Shareholders |
| Capital Required? | No | Yes |
| Net Price of Policy | Known ex post | Known ex ante |
| Manager’s Earnings | Expense Saving | Investment Profit |

MICs offer several advantages over SICs, with one of the most prominent being the mitigation of the policyholder-agent conflict. This comes as no surprise: employees often work for the best interest of the owners of the company, who, in the case of an MIC, are the members themselves. In addition, the risk and surplus sharing mechanism between members is found to be efficient in diversifying idiosyncratic risks (see \@BBOPcite\@BAP\@BBNcass:individual:mutual:pareto:1996\@BBCP). Evidently, MICs are not always superior to SICs. In particular, the ability to raise capital from the financial market enables SICs to enhance their liquidity and financial flexibility, which therefore allows SICs to expand their operations and innovate more readily compared to MICs. The relative merits of MICs versus SICs constitute an important and long-standing debate in the literature. Over centuries of development, both forms of insurance have evolved and now coexist with significant and enduring presence in the market. Our study takes the relevance of MICs as given and does not further explore this comparative aspect; interested readers are referred to \@BBOPcite\@BAP\@BBNmcnamara1992ownership; cummins:coexistence:1999; BIENER2012454; BRAUN2015875; SCHMEISER202192\@BBCP.

The objective of this article is to provide a quantitative and dynamic analysis of the members’ behavior under the surplus-sharing mechanism of an MIC. To name a few representative studies in the literature, from the perspective of an MIC or a mutual-aid platform, \@BBOPcite\@BAP\@BBNTAPIERO1984241\@BBCP addressed the problem of determining optimal premium rates.
Regarding individual members’ viewpoints, valuation problems were proposed using expected utility, Choquet expected utility and distortion risk measures in \@BBOPcite\@BAP\@BBNALBRECHT2017180\@BBCP; and mean-variance objective in \@BBOPcite\@BAP\@BBNgatzert2012merits\@BBCP. From a community perspective, \@BBOPcite\@BAP\@BBNBAUERLE201837\@BBCP considered socially optimal reinsurance treaties among insurers and a reinsurance company, \@BBOPcite\@BAP\@BBNchen:optimal:2021\@BBCP formulated the optimal risk-sharing to achieve Pareto optimality without a surplus/loss-sharing mechanism. More recently, peer-to-peer (P2P) insurance models, which are built on the principle of mutuality in a decentralized structure, have drawn attention in the study of optimal risk-sharing; see e.g.,
\@BBOPcite\@BAP\@BBNdhaene; dhaene:2021; denuit:comonotonicity:2023\@BBCP.

Despite the rich landscape of inspiring work on mutual and P2P insurances, a fundamental and still underexplored question is how much risk each participant optimally chooses to transfer to the platform in this interactive environment due to the sharing mechanism, especially under a dynamical continuous-time model. Indeed, these individual decisions and loss experiences directly impact the platform’s stability and efficiency, while the distribution of surplus or deficit not only shapes their incentives but also couples their decisions, creating complex interdependencies that deserve careful study. For instance, a member’s behavior may vary across platforms with different compositions of risk class, or when entitled to a larger or smaller share of the surplus/deficit. The major technical challenge arises from the interactions created by the sharing mechanism, which couples members and results in a less mathematically tractable optimal decision problem, especially when the number of members is large. Additionally, since members may incur claims at different times and adjust their insurance choices in response to the evolving collective experience, a continuous-time framework is naturally suited to capturing such dynamic feedback in contrast to discrete-time models, which are less equipped to capture this level of temporal heterogeneity. These complexities call for a modeling framework capable of handling large-population strategic interactions. Recent advances in extended mean field game (MFG) (\@BBOPcite\@BAP\@BBNcarmona:extended:2019; alasseur2020extended; carmona2021probabilistic; munoz2023classical; li:2024:cryptocurrency; bensoussan2025linear\@BBCP) have emerged to meet this need, offering a powerful approach for modeling the optimal control problem from the members’ perspective.

In this article, we formulate the optimal insurance problems for an MIC under an extended MFG framework. Instead of modeling direct interactions among participants, MFGs capture their behavior through interaction with a common macroscopic factor, known as the mean field term, providing an asymptotic approach to solving optimal decision problems involving a large population. Due to their mathematical tractability and practical relevance, MFGs have been applied across various domains, including finance (\@BBOPcite\@BAP\@BBNcasgrain2019algorithmic; HAN2022; bensoussan2022dynamic\@BBCP), machine learning (\@BBOPcite\@BAP\@BBNruthotto2020machine\@BBCP), and cryptocurrency mining (\@BBOPcite\@BAP\@BBNlion:bitcoin:2024; li:2024:cryptocurrency\@BBCP). Recently, MFGs have begun to gain traction in the insurance and actuarial context. For example, \@BBOPcite\@BAP\@BBNBO2024202\@BBCP analyzed the behavior of competitive insurers that interact through relative performance in their objective functions, while their wealth processes evolve independently. In contrast, our work incorporates explicit interactions in participants’ wealth processes, making it one of the first in the actuarial domain to do so. Although our primary focus is on MICs, the model introduced herein can be readily applied to other mutual-aid platforms that share this mutuality and risk/surplus sharing mechanism.

Our model consists of members classified into HH different membership or risk classes, where members are homogeneous within class, and heterogeneous between classes. This classification structure is crucial in insurance pricing and underwriting, as members are often grouped based on various risk and demographic factors, such as age, region of residence, smoking status, and other relevant characteristics. Our model stands out by encompassing the surplus-sharing mechanism in a pro-rata basis, which depends on the insurance strategies and claim experience of all other members within the MIC. Consequently, the wealth process of a member is influenced not only by their own actions but also by the collective strategies of other members within the system. The MFG is termed extended here because it explicitly captures this additional layer of interaction arising from the direct impact of collective strategies within the company. Our model yields important insights into how the surplus-sharing mechanism within an MIC impacts the proportional insurance strategies of individual members, particularly in terms of reaching a Nash equilibrium.

The contributions of the present article are highlighted below. From a mathematical perspective, our work contributes to providing the solution of an extended mean field game characterized by a system of mean field forward-backward stochastic different equations (MF-FBSDEs) associated with games, and establishes
a result of global-in-time existence and uniqueness of the solution. When a practical constraint on the insurance strategy is imposed, the strict monotonicity condition (see e.g. \@BBOPcite\@BAP\@BBNpardoux2014stochastic\@BBCP) for FBSDEs no longer holds due to the non-expansive property of a projection map. To address this, we derive a weaker form of monotonicity by utilizing the properties of the projection map, and employ an adaptation of the celebrated continuation approach to bypass the standard condition to establish a global existence result. Our sufficient condition merely requires a small mean field effect on each member, which is in line with the finding in the literature (see e.g. \@BBOPcite\@BAP\@BBNCHU2025112028\@BBCP).

From a numerical perspective, to address the fact that the MF-FBSDE lacks a closed-form solution under the insurance constraint, we adopt a deep neural network (DNN) approach to solve the equation and implement the resulting optimal insurance strategies. Due to the presence of the mean field terms, standard Monte-Carlo methods are not directly applicable. To address this, we adapt and modify the forward method introduced in ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) (see \@BBOPcite\@BAP\@BBNgermain2022numerical; carmona2022convergence; han2024learning\@BBCP). Our proposed method includes an additional penalty term to match the output of the network with the mean field equilibrium strategy under the extended mean field game framework.In the absence of insurance constraints, the proposed method aligns with the known closed-form solution in the linear-quadratic setting, which demonstrates the accuracy of the algorithm.

From an economic perspective, we conduct a series of sensitivity analyzes to examine how the risk characteristics of members and the surplus-sharing mechanism influence their wealth and insurance strategies. First, we find that as the proportion of highly risk-averse members or those with more volatile loss processes increases, the overall insurance demand within the entire MIC tends to rise. Second, a higher surplus-sharing ratio reduces the effective price of the policies, thereby increasing their insurance demand. Third, by comparing results with and without insurance constraints, we find that the constraints help confine strategies within a practical range and reduce the disparity in insurance strategies across different member classes, ultimately narrowing the resulting wealth gap.

This article is organized as follows. In Section [2](https://arxiv.org/html/2511.12292v1#S2 "2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), we formulate the optimal insurance problem for members within an MIC, under both the NN-player setting and the mean field game framework. In Section [3](https://arxiv.org/html/2511.12292v1#S3 "3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market"), we provide the generic solution of the mean field Nash equilibrium in terms of an MF-FBSDE, whose well-posedness is discussed in Section [4](https://arxiv.org/html/2511.12292v1#S4 "4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"). We then confine ourselves to quadratic rewards in Section [5](https://arxiv.org/html/2511.12292v1#S5 "5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market"), and in Section [5.2](https://arxiv.org/html/2511.12292v1#S5.SS2 "5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market"), we further reduce the MF-FBSDE to simpler Riccati equations when no insurance constraint is imposed. Section [6](https://arxiv.org/html/2511.12292v1#S6 "6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") introduces a DNN architecture to numerically compute the underlying MF-FBSDE. Based on this, we perform a numerical experiments to examine the effect of the risk composition of the MIC and the surplus-sharing mechanism on the members’ optimal insurance strategies under both quadratic and non-quadratic rewards. The article is concluded in Section [7](https://arxiv.org/html/2511.12292v1#S7 "7 Concluding Remarks ‣ Mean Field Analysis of Mutual Insurance Market").

## 2 Model Formulation

We consider a mutual insurance company with HH classes of membership. Members are assumed to be homogeneous in dynamics and parameters within each class, and heterogeneous between different classes. In this section, we first introduce the NN-player problem with a large (but finite) number of members. We then study the mean field formulation of the problem by considering a mutual insurance company (MIC) with infinite number of members. Such a formulation is justified by the notion of ε\varepsilon-Nash equilibrium, see Theorem [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") below.

Notation. We fix a decision horizon [0,T][0,T], where T>0T>0. Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a probability space with 𝔼\mathbb{E} being the expected value taken with respect to ℙ\mathbb{P}. Given an σ\sigma-algebra 𝒢⊆ℱ\mathcal{G}\subseteq\mathcal{F}, we denote by L2​(Ω,𝒢,ℙ)L^{2}(\Omega,\mathcal{G},\mathbb{P}) the collection of all square-integrable, 𝒢\mathcal{G}-measurable random variables. For a generic filtration 𝔾:=(𝒢t)t∈[0,T]\mathbb{G}:=(\mathcal{G}\_{t})\_{t\in[0,T]} defined on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) and a set A⊆ℝA\subseteq\mathbb{R}, we denote by

|  |  |  |
| --- | --- | --- |
|  | L𝔾2​([0,T];A):={(αt)t∈[0,T]:αt∈A, 𝒢t-measurable, and ​𝔼​[∫0T|αt|2​𝑑t]<∞}.L^{2}\_{\mathbb{G}}([0,T];A):=\Bigg\{(\alpha\_{t})\_{t\in[0,T]}:\alpha\_{t}\in A,\text{ $\mathcal{G}\_{t}$-measurable, and }\mathbb{E}\left[\int\_{0}^{T}|\alpha\_{t}|^{2}dt\right]<\infty\Bigg\}. |  |

For any positive integer nn, we denote [n]:={1,…,n}[n]:=\{1,\dots,n\}. For any function ff, we use a subscript to denote the partial derivative of ff with respect to the corresponding variable. We denote by 𝐈{\bf I} the H×HH\times H identity matrix. For any H×HH\times H matrix 𝐀{\bf A}, we define λmin​(𝐀)\lambda\_{\min}({\bf A}) and λmax​(𝐀)\lambda\_{\max}({\bf A}) to be the smallest and largest eigenvalue of (𝐀+𝐀⊤)/2({\bf A}+{\bf A}^{\top})/2, respectively. Finally, for any matrix 𝐁{\bf B}, we let ‖𝐁‖2:=λmax​(𝐁⊤​𝐁)\|{\bf B}\|\_{2}:=\sqrt{\lambda\_{\max}({\bf B}^{\top}{\bf B})} be its spectral norm.

### 2.1 Preliminaries and the NN-Player Problem

Suppose that there are NhN^{h} members for each risk class h∈[H]h\in[H]. In our model, each member represents a company or organization that holds a group insurance policy provided by an MIC for employee benefits such as health, accident, or disability coverage. The losses are retained by the organization itself, which is common in practice for risks such as workers’ injuries, property and casualty losses related to company infrastructure, and disability claims. The accumulated loss process of member ii in Class hh, denoted by Li,h=(Lti,h)t∈[0,T]L^{i,h}=(L^{i,h}\_{t})\_{t\in[0,T]}, is given by

|  |  |  |
| --- | --- | --- |
|  | Lti,h:=∑j=1Mti,hLi,h,j,L^{i,h}\_{t}:=\sum\_{j=1}^{M^{i,h}\_{t}}L^{i,h,j}, |  |

where (Mti,h)t∈[0,T](M^{i,h}\_{t})\_{t\in[0,T]} is a Poisson process with intensity λh>0\lambda^{h}>0 representing the number of claims up to time tt. The claim severities (Li,h,j)i∈[Nh],j≥1(L^{i,h,j})\_{i\in[N^{h}],\,j\geq 1} are assumed to be i.i.d. for each fixed hh, and are independent of the claim count processes (Mti,h)i∈[Nh],t∈[0,T](M^{i,h}\_{t})\_{i\in[N^{h}],\,t\in[0,T]}.

A popular approach in the actuarial literature (see, e.g., \@BBOPcite\@BAP\@BBNiglehart1969diffusion; grandell1991aspects; browne1995optimal\@BBCP) is to approximate Lti,hL^{i,h}\_{t} by the Cramér–Lundberg diffusion model. The accumulated loss process of member ii in class hh, denoted by Ci,h=(Cti,h)t∈[0,T]C^{i,h}=(C^{i,h}\_{t})\_{t\in[0,T]}, is then approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Cti,h=μh​d​t−σh​d​Wti,h,dC^{i,h}\_{t}=\mu^{h}\,dt-\sigma^{h}\,dW^{i,h}\_{t}, |  | (1) |

where (Wti,h)t∈[0,T](W^{i,h}\_{t})\_{t\in[0,T]} is a standard Brownian motion such that {Wi,h:i∈[Nh],h∈[H]}\{W^{i,h}:i\in[N^{h}],\,h\in[H]\} are independent and identically distributed, μh:=λh​𝔼⁡[Li,h,j]\mu^{h}:=\lambda^{h}\operatorname{\mathbb{E}}[L^{i,h,j}], and σh:=λh​𝔼⁡[(Li,h,j)2].\sigma^{h}:=\sqrt{\lambda^{h}\operatorname{\mathbb{E}}[(L^{i,h,j})^{2}]}. Our subsequent analysis shall be based on this diffusion approximation model.

Each member i∈[Nh]i\in[N^{h}] in Class h∈[H]h\in[H] is entitled to choose a proportion vi,h∈𝒜𝔽i,h​(I)v^{i,h}\in\mathcal{A}\_{\mathbb{F}^{i,h}}(I) of the loss to be transferred to the MIC, where 𝒜𝔽i,h​(I):=L𝔽i,h2​([0,T];I)\mathcal{A}\_{\mathbb{F}^{i,h}}(I):=L^{2}\_{\mathbb{F}^{i,h}}([0,T];I) is the admissible set of proportional insurance strategies in the constraint set II. We assume that I⊆ℝI\subseteq\mathbb{R} is a closed interval of the form I=[a,b]I=[a,b], where a,b∈ℝa,b\in\mathbb{R}, b>ab>a, and the filtration 𝔽i,h:=(ℱti,h)t∈[0,T]\mathbb{F}^{i,h}:=(\mathcal{F}^{i,h}\_{t})\_{t\in[0,T]} is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱti,h\displaystyle\mathcal{F}^{i,h}\_{t} | :=σ(ξi,h,Wsi,h:0≤s≤t)∨ℱ^t,\displaystyle:=\sigma\left(\xi^{i,h},W^{i,h}\_{s}:0\leq s\leq t\right)\vee\hat{\mathcal{F}}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ^t\displaystyle\hat{\mathcal{F}}\_{t} | :=σ(∑j=1Nkvsj,kNk:k∈[H], 0≤s≤t)⋁σ(∑i=1Nkysi,kNk:k∈[H],0≤s≤t)∨𝒩,\displaystyle:=\sigma\left(\frac{\sum\_{j=1}^{N^{k}}{v^{j,k}\_{s}}}{N^{k}}:k\in[H],\ 0\leq s\leq t\right)\bigvee\sigma\left(\frac{\sum\_{i=1}^{N^{k}}y^{i,k}\_{s}}{N^{k}}:k\in[H],0\leq s\leq t\right)\vee\mathcal{N}, |  |

where 𝒩\mathcal{N} is the collection of all ℙ\mathbb{P}-null sets, ξi,h\xi^{i,h}, i∈[Nh]i\in[N^{h}], h∈[H]h\in[H], are i.i.d. square-integrable random variables representing the initial wealth of member ii from Class hh, and (yti,h)t∈[0,T](y^{i,h}\_{t})\_{t\in[0,T]} is her wealth process; see ([3](https://arxiv.org/html/2511.12292v1#S2.E3 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) below. Thus, each member makes her decision based on her own wealth, and the public information consisting of the average position and wealth of all other members within the MIC contained in the filtration (ℱ^th)t∈[0,T](\hat{\mathcal{F}}^{h}\_{t})\_{t\in[0,T]}.

A common choice of the constraint would be a=0a=0 and b=1b=1, which indicates that the member is not allowed to transfer more than her actual loss or to take a short position, although our analysis is not limited to this specific case. The rate of premium she has to pay is then given by vti,h​chv^{i,h}\_{t}c^{h}, where ch:=μh​(1+θh)c^{h}:=\mu^{h}(1+\theta^{h}) is the premium rate charged by the MIC, and θh>0\theta^{h}>0 is the safety loading for Class hh. We remark that the insurance constraint limits the instantaneous premium rate payable in the range [a​ch,b​ch][ac^{h},bc^{h}]. This aligns with the practical scenario where the premium rate remains relatively stable without drastic fluctuations. In addition, each member in Class hh is required to pay a membership fee of eh≥0e^{h}\geq 0 to be able to get a share of the surplus.

Let U=(Ut)t≥0U=(U\_{t})\_{t\geq 0} be the surplus of the MIC, which is defined as the aggregate premium income, membership fee, less the shared loss and management costs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ut=∑h=1H∑j=1Nh[(ch−dh)​vtj,h+eh−deh]​d​t⏟premium income and membership fee less expenses−∑h=1H∑j=1Nhvtj,h​d​Ctj,h⏟shared loss,dU\_{t}=\underbrace{\sum\_{h=1}^{H}\sum\_{j=1}^{N^{h}}\left[(c^{h}-d^{h})v^{j,h}\_{t}+e^{h}-d\_{e}^{h}\right]dt}\_{\text{premium income and membership fee less expenses}}-\underbrace{\sum\_{h=1}^{H}\sum\_{j=1}^{N^{h}}v^{j,h}\_{t}dC^{j,h}\_{t}}\_{\text{shared loss}}, |  | (2) |

where dh,deh>0d^{h},d\_{e}^{h}>0 are the common proportional and fixed management fee rate, respectively. Let πh>0\pi^{h}>0 be the proportion of shares acquired by Class hh. The surplus or loss UU will then be distributed according to a simple pro-rate basis, where each member from Class hh receives πh/∑k=1Hπk​Nk\pi^{h}/\sum\_{k=1}^{H}\pi^{k}N^{k} of it. A similar pro-rata sharing mechanism is popular in practice and in the literature. For instance, \@BBOPcite\@BAP\@BBNALBRECHT2017180\@BBCP considered a sharing mechanism where each member receives a proportion of the surplus based on the amount of insurance they purchased. Herein, the parameter πh\pi^{h} can be chosen to reflect the risk exposure, safety loading, and the membership fee rate within each risk class. Since the proportion of insurance vi,hv^{i,h} is bounded within a practical range II and the membership fee rate does not fluctuate significantly, using a fixed parameter πh\pi^{h} provides a stable proxy for the relative premium size. This approach keeps the surplus-sharing mechanism simple and avoids the need for frequent adjustments of sharing ratios, thereby reducing administrative complexity.

In sum, the wealth process yi,hy^{i,h} of member ii from Class hh is governed by the following components. First, she earns a risk-free rate r>0r>0 based on her current wealth. Second, according to her insurance strategy, she needs to pay the premium, and is responsible for the retained loss that has not been transferred to the MIC. Third, in addition to the proceeds from the MIC mentioned in the last paragraph, she also receives an exogenous income of rate l~h\tilde{l}^{h}. Hence, the process yi,hy^{i,h} is governed by the following SDE: y0i,h=ξi,hy\_{0}^{i,h}=\xi^{i,h} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​yti,h\displaystyle dy^{i,h}\_{t} | =(r​yti,h+l~h−eh−ch​vti,h⏟ premium paid)​d​t−(1−vti,h)​d​Cti,h⏟ retained loss\displaystyle=\left(ry^{i,h}\_{t}+\tilde{l}^{h}-e^{h}-\underbrace{c^{h}v^{i,h}\_{t}}\_{\text{ premium paid}}\right)dt-\underbrace{(1-v^{i,h}\_{t})dC^{i,h}\_{t}}\_{\text{ retained loss}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +πh∑l=1Hπl​Nl​(∑k=1H∑j=1Nk[(ck−dk)​vtj,k+ek−dek]​d​t−∑k=1H∑j=1Nkvtj,k​d​Ctj,k)⏟ shared surplus/deficit from MIC\displaystyle\quad+\underbrace{\frac{\pi^{h}}{\sum\_{l=1}^{H}\pi^{l}N^{l}}\left(\sum\_{k=1}^{H}\sum\_{j=1}^{N^{k}}\left[(c^{k}-d^{k})v^{j,k}\_{t}+e^{k}-d\_{e}^{k}\right]dt-\sum\_{k=1}^{H}\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}dC^{j,k}\_{t}\right)}\_{\text{ shared surplus/deficit from MIC}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(r​yti,h+lh−κh​vti,h+πh​∑k=1Hωk​(κk−dk)​∑j=1Nkvtj,kNk)​d​t+σh​(1−vti,h)​d​Wti,h\displaystyle=\left(ry^{i,h}\_{t}+{l}^{h}-\kappa^{h}v^{i,h}\_{t}+\pi^{h}\sum\_{k=1}^{H}\omega^{k}(\kappa^{k}-d^{k})\frac{\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}}{N^{k}}\right)dt+\sigma^{h}(1-v^{i,h}\_{t})dW^{i,h}\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +πh​∑k=1Hσk​ωk​∑j=1Nkvtj,kNk​d​Wtj,k⏟idiosyncratic risk,\displaystyle\quad+\underbrace{\pi^{h}\sum\_{k=1}^{H}\sigma^{k}\omega^{k}\frac{\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}}{N^{k}}dW^{j,k}\_{t}}\_{\text{idiosyncratic risk}}, |  | (3) |

where lh:=l~h−μh−eh+πh∑l=1Hπl​Nl​∑k=1HNk​(ek−dek)l^{h}:=\tilde{l}^{h}-\mu^{h}-e^{h}+\frac{\pi^{h}}{\sum\_{l=1}^{H}\pi^{l}N^{l}}\sum\_{k=1}^{H}N^{k}(e^{k}-d\_{e}^{k}), κh:=μh​θh\kappa^{h}:=\mu^{h}\theta^{h}, and ωh:=Nh/∑k=1Hπk​Nk\omega^{h}:=N^{h}/\sum\_{k=1}^{H}\pi^{k}N^{k}. The parameter ωh\omega^{h} represents the proportion of members in Class hh within the entire MIC, adjusted by the shares acquired by each risk class. We assume that (ωh)h=1H(\omega^{h})\_{h=1}^{H} is independent of the absolute population sizes (Nh)h=1H(N^{h})\_{h=1}^{H}, meaning that even if the population sizes change, this ratio remains constant. Under this assumption, we have

|  |  |  |
| --- | --- | --- |
|  | lh=l~h−μh−eh+πh​∑k=1Hωk​(ek−dek).l^{h}=\tilde{l}^{h}-\mu^{h}-e^{h}+\pi^{h}\sum\_{k=1}^{H}\omega^{k}(e^{k}-d\_{e}^{k}). |  |

In addition, it is clear that ∑h=1Hπh​ωh=1\sum\_{h=1}^{H}\pi^{h}\omega^{h}=1. We also assume that κh−d>0\kappa^{h}-d>0 for all h∈[H]h\in[H] throughout the rest of the article. This condition ensures that the risk premium rate exceeds the expense rate, meaning that the premiums sufficiently cover expenses to sustain meaningful MIC operations and avoid immediate bankruptcy.

###### Remark 2.1.

We assume that members will inject new capital into the MIC in proportion to their shares to avoid it from bankruptcy. This explains why the deficit in ([3](https://arxiv.org/html/2511.12292v1#S2.E3 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) is also shared among members in our setting when Ut<0U\_{t}<0. In practice, when Ut<0U\_{t}<0, an MIC may respond by increasing premiums, which results in a net outflow from members’ wealth. However, because the owners of an MIC are the members themselves, the management of the company does not inject capital into the mutual; instead, they provide services and collect management fees.

Each member ii from Class hh aims to take an insurance strategy vi,h∈𝒜𝔽i,h​(I)v^{i,h}\in\mathcal{A}\_{\mathbb{F}^{i,h}}(I) to maximize the following objective:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝒥i,h​(vi,h):=𝒥i,h​(vi,h;𝐲−i,h,𝐯−i,h)\displaystyle\mathcal{J}^{i,h}(v^{i,h})=\mathcal{J}^{i,h}\left(v^{i,h};{\bf y}^{-i,h},{\bf v}^{-i,h}\right) |  | (4) |
|  |  | :=𝔼​[∫0Tfh​(t,yti,h,∑j=1,j≠iNhytj,hNh−1,vti,h,∑j=1,j≠iNhvtj,hNh−1)​𝑑t+gh​(yTi,h,∑j=1,j≠iNhyTj,hNh−1)],\displaystyle\quad=\mathbb{E}\left[\int\_{0}^{T}f^{h}\left(t,y^{i,h}\_{t},\frac{\sum\_{j=1,j\neq i}^{N^{h}}y^{j,h}\_{t}}{N^{h}-1},v^{i,h}\_{t},\frac{\sum\_{j=1,j\neq i}^{N^{h}}v^{j,h}\_{t}}{N^{h}-1}\right)dt+g^{h}\left(y^{i,h}\_{T},\frac{\sum\_{j=1,j\neq i}^{N^{h}}y^{j,h}\_{T}}{N^{h}-1}\right)\right], |  |

where
𝐯−i,h:=(vj,h)j∈[Nh],j≠i{\bf v}^{-i,h}:=(v^{j,h})\_{j\in[N^{h}],j\neq i}, 𝐲−i,h=(yj,h)j∈[Nh],j≠i{\bf y}^{-i,h}=(y^{j,h})\_{j\in[N^{h}],j\neq i} are the associated wealth processes under the NN-player game; fh:[0,T]×ℝ×ℝ×ℝ×ℝ→ℝf^{h}:[0,T]\times\mathbb{R}\times\mathbb{R}\times\mathbb{R}\times\mathbb{R}\to\mathbb{R} and gh:ℝ×ℝ→ℝg^{h}:\mathbb{R}\times\mathbb{R}\to\mathbb{R}.
In other words, each member within a given risk class shares the same preference, which accounts for her own wealth, her insurance strategy relative to the class average, and the average wealth of members across all classes. Assumptions on fhf^{h} and ghg^{h} are deferred to Section [2.4](https://arxiv.org/html/2511.12292v1#S2.SS4 "2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").

In practice, several factors lead to insurance purchase behavior that depends on the coverage level vi,hv^{i,h} in a non-linear and concave manner, a feature we capture through the reward function fhf^{h} in our model. First, as shown by \@BBOPcite\@BAP\@BBNmossin:1968\@BBCP, full coverage is generally not optimal when premiums include loadings, since diminishing marginal utility of wealth and actuarially unfair pricing produce an interior optimum. Second, regulatory frameworks often impose minimum coverage requirements such as auto third-party liability or workplace injury insurance that members or group managers must meet but are not required to exceed, especially when risks or potential losses are low. For example, rather than fully insuring depreciated equipment or property, members may opt to save on premiums and replace the item if damaged. Third, prospect theory (\@BBOPcite\@BAP\@BBNprospect:1979\@BBCP) suggests that individuals tend to be myopic and underweight low-probability events, or exhibit loss aversion relative to reference wealth levels, which contributes to under-insurance even in situations involving severe but infrequent losses (\@BBOPcite\@BAP\@BBNpauly:neglect:disaster:2004\@BBCP). These considerations motivate the incorporation of vi,hv^{i,h} into the reward function.

Under the setting ([3](https://arxiv.org/html/2511.12292v1#S2.E3 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) and ([4](https://arxiv.org/html/2511.12292v1#S2.E4 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")), the decision problems of members within the MIC are coupled via the surplus/deficit sharing mechanism and their objective functions. Problem [1](https://arxiv.org/html/2511.12292v1#Thmproblem1 "Problem 1. ‣ 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") below formulates the notion of optimal strategies for all members within the MIC in terms of a Nash equilibrium, where a member would be worse-off if she deviates from the equilibrium strategy.

###### Problem 1.

Find a Nash equilibrium strategy (vi,h)h∈[H],i∈[Nh](v^{i,h})\_{h\in[H],i\in[N^{h}]} such that vi,h∈𝒜𝔽i,h​(I)v^{i,h}\in\mathcal{A}\_{\mathbb{F}^{i,h}}(I), and

|  |  |  |
| --- | --- | --- |
|  | 𝒥i,h​(vi,h;𝐲−i,h,𝐯−i,h)≥𝒥i,h​(ui,h;𝐲ˇ−i,h,𝐯−i,h),\mathcal{J}^{i,h}\left(v^{i,h};{\bf y}^{-i,h},{\bf v}^{-i,h}\right)\geq\mathcal{J}^{i,h}\left(u^{i,h};\check{{\bf y}}^{-i,h},{\bf v}^{-i,h}\right), |  |

for any ui,h∈𝒜𝔽i,h​(I)u^{i,h}\in\mathcal{A}\_{\mathbb{F}^{i,h}}(I), and any h∈[H]h\in[H] and i∈[Nh]i\in[N^{h}], where 𝐲ˇ−i,h=(yˇj,h)j∈[Nh],j≠i\check{{\bf y}}^{-i,h}=(\check{y}^{j,h})\_{j\in[N^{h}],j\neq i}, and (yˇj,h)j∈[Nh](\check{y}^{j,h})\_{j\in[N^{h}]} are the associated wealth processes under the NN-player game with strategies (v1,h,…,(v^{1,h},\dots, vi−1,h,ui,h,vi+1,h,…,vNh,h)v^{i-1,h},u^{i,h},v^{i+1,h},\dots,v^{N^{h},h}).

### 2.2 Mean Field Game Formulation

Due to the intricate interactions between members arising from the surplus-sharing mechanism, it is analytically challenging to obtain a Nash equilibrium strategy for Problem [1](https://arxiv.org/html/2511.12292v1#Thmproblem1 "Problem 1. ‣ 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"). To this end, we adopt the mean field formulation of Problem [1](https://arxiv.org/html/2511.12292v1#Thmproblem1 "Problem 1. ‣ 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").

We consider the case where the number of members NhN^{h}, h∈[H]h\in[H], tends to infinity, and suppose that we are given a collection of exogenous and deterministic processes (zh)h∈[H](z^{h})\_{h\in[H]} and (v¯h)h∈[H](\bar{v}^{h})\_{h\in[H]}, where zh=(zth)t∈[0,T]z^{h}=(z^{h}\_{t})\_{t\in[0,T]} and v¯h=(v¯th)t∈[0,T]\bar{v}^{h}=(\bar{v}^{h}\_{t})\_{t\in[0,T]}. For h∈[H]h\in[H] and i∈[Nh]i\in[N^{h}], let xi,h:=(xti,h)t∈[0,T]x^{i,h}:=(x^{i,h}\_{t})\_{t\in[0,T]} be the wealth process of member ii from Class hh, which satisfies the following mean field dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xti,h=(r​xti,h+lh−κh​vti,h+πh​∑k=1Hωk​(κk−dk)​v¯tk)​d​t+σh​(1−vti,h)​d​Wti,h,x0h=ξi,h.dx^{i,h}\_{t}=\left(rx^{i,h}\_{t}+l^{h}-\kappa^{h}v^{i,h}\_{t}+\pi^{h}\sum\_{k=1}^{H}\omega^{k}(\kappa^{k}-d^{k}){\bar{v}^{k}\_{t}}\right)dt+\sigma^{h}(1-v^{i,h}\_{t})dW^{i,h}\_{t},\ x^{h}\_{0}=\xi^{i,h}. |  | (5) |

Each member from Class hh aims to maximize the following objective:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ji,h​(vi,h)\displaystyle J^{i,h}(v^{i,h}) | :=Ji,h​(vi,h;zh,v¯h)=𝔼​[∫0Tfh​(t,xti,h,zth,vti,h,v¯th)​𝑑t+gh​(xTi,h,zTh)].\displaystyle=J^{i,h}\left(v^{i,h};z^{h},\bar{v}^{h}\right)=\mathbb{E}\left[\int\_{0}^{T}f^{h}\left(t,x^{i,h}\_{t},z^{h}\_{t},v^{i,h}\_{t},\bar{v}^{h}\_{t}\right)dt+g^{h}\left(x^{i,h}\_{T},z^{h}\_{T}\right)\right]. |  | (6) |

Since the number of members in each class is indefinite, we have the following observations: (i) the idiosyncratic part in ([3](https://arxiv.org/html/2511.12292v1#S2.E3 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) shall vanish, and (ii) the contribution of each individual on the average terms such as ∑j=1Nvtj,k/Nk\sum\_{j=1}^{N}v^{j,k}\_{t}/N^{k} becomes negligible. This allows us to treat the average wealth and average insurance strategy for each of Class hh to be exogeneously given, which are represented by zhz^{h} and vhv^{h}, respectively. Under this framework, the wealth and objective functions between members are essentially decoupled, which allows us to focus on the decision problem for a single representative member from each risk class. Henceforth, we shall omit the index ii in all the occurrence in the sequel, and simply call xhx^{h} the wealth process of the representative member (or simply member below) from Class hh. We also define the filtrations 𝔽h:=(ℱth)t∈[0,T]\mathbb{F}^{h}:=(\mathcal{F}^{h}\_{t})\_{t\in[0,T]} and 𝔽[H]:=(ℱt[H])t∈[0,T]\mathbb{F}^{[H]}:=(\mathcal{F}^{[H]}\_{t})\_{t\in[0,T]} by ℱth:=σ(ξh,Wsh:0≤s≤t)\mathcal{F}^{h}\_{t}:=\sigma\left(\xi^{h},W^{h}\_{s}:0\leq s\leq t\right) and ℱt[H]:=⋁h=1Hℱth\mathcal{F}^{[H]}\_{t}:=\bigvee\_{h=1}^{H}\mathcal{F}^{h}\_{t}, respectively.

To achieve equilibrium, the deterministic functions zhz^{h} and vhv^{h} should eventually agree with the average wealth and the average strategy when optimality is achieved. This solution approach, often known as the fixed point approach, can be formulated in terms of the following two sub-problems.

###### Problem 2.

Given the deterministic functions (zh)h∈[H](z^{h})\_{h\in[H]} and 𝐯¯:=(v¯h)h∈[H]\bar{\bf v}:=(\bar{v}^{h})\_{h\in[H]}, find the optimal control 𝐯:=(vh)h∈[H]{\bf v}:=(v^{h})\_{h\in[H]} such that for any h∈[H]h\in[H],

|  |  |  |
| --- | --- | --- |
|  | vh=arg⁡maxuh∈𝒜𝔽h​(I)Jh​(uh;zh,v¯h).v^{h}=\mathop{\arg\max}\_{u^{h}\in\mathcal{A}\_{\mathbb{F}^{h}}(I)}J^{h}\left(u^{h};z^{h},\bar{v}^{h}\right). |  |

###### Problem 3.

Find the mean field equilibrium wealth 𝐳=(zh)h∈[H]{\bf z}=(z^{h})\_{h\in[H]} and strategy 𝐯¯=(v¯h)h∈[H]\bar{\bf v}=(\bar{v}^{h})\_{h\in[H]} such that for any t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | (v¯t1,…,v¯tH)=𝔼​[(vt1,…,vtH)]and(zt1,…,ztH)=𝔼​[(xt1,…,xtH)].(\bar{v}^{1}\_{t},\dots,\bar{v}^{H}\_{t})=\mathbb{E}\left[(v^{1}\_{t},\dots,v^{H}\_{t})\right]\quad\text{and}\quad(z^{1}\_{t},\dots,z^{H}\_{t})=\mathbb{E}\left[(x^{1}\_{t},\dots,x^{H}\_{t})\right]. |  |

Since the shared surplus/deficit directly depends on the insurance strategies of the other members, an additional fixed point (v¯t1,…,v¯tH)=𝔼​[(vt1,…,vtH)](\bar{v}^{1}\_{t},\dots,\bar{v}^{H}\_{t})=\mathbb{E}\left[(v^{1}\_{t},\dots,v^{H}\_{t})\right] has to be satisfied in Problem [3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"). This formulation is called an extended mean field game (\@BBOPcite\@BAP\@BBNcarmona2015probabilistic; gomes2014mean\@BBCP) since it includes finding the equilibrium law of the optimal control. Note also that the diffusion term in ([5](https://arxiv.org/html/2511.12292v1#S2.E5 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) is controlled. As documented in \@BBOPcite\@BAP\@BBNbensoussan2023degeneratemeanfieldtype\@BBCP, such control in the MFG context can complicate the representation of the solution and the mathematical analysis, particularly because the control depends on the backward component of the associated BSDE as shown in ([12](https://arxiv.org/html/2511.12292v1#S3.E12 "In Theorem 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")) below.

Theorem [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") below establishes the ε\varepsilon-Nash equilibrium of the mean field game ([5](https://arxiv.org/html/2511.12292v1#S2.E5 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"))-([6](https://arxiv.org/html/2511.12292v1#S2.E6 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) for the original NN-player game ([3](https://arxiv.org/html/2511.12292v1#S2.E3 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"))-([4](https://arxiv.org/html/2511.12292v1#S2.E4 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")). It says that, the optimal strategies obtained in the mean field game is very close to achieving a Nash equilibrium for the NN-player game, where the discrepancy decays with the class sizes in the order of 12\frac{1}{2}.

###### Theorem 2.1.

Let (vi,h)h∈[H],i∈[Nh](v^{i,h})\_{h\in[H],i\in[N^{h}]}, (zh)h∈[H](z^{h})\_{h\in[H]} and (v¯h)h∈[H](\bar{v}^{h})\_{h\in[H]} be the solution of Problems [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")-[3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") with wealth process and objective functions given by ([5](https://arxiv.org/html/2511.12292v1#S2.E5 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) and ([6](https://arxiv.org/html/2511.12292v1#S2.E6 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")), respectively. Consider Problem [1](https://arxiv.org/html/2511.12292v1#Thmproblem1 "Problem 1. ‣ 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") with class size NhN^{h} for each membership class h∈[H]h\in[H].
Then, under Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").A below, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝒥i,h​(vi,h;𝐲−i,h,𝐯−i,h)≥𝒥i,h​(ui,h;𝐲ˇ−i,h,𝐯−i,h)−∑k=1HO​(1Nk),\mathcal{J}^{i,h}\left(v^{i,h};{\bf y}^{-i,h},{\bf v}^{-i,h}\right)\geq\mathcal{J}^{i,h}\left(u^{i,h};\check{{\bf y}}^{-i,h},{\bf v}^{-i,h}\right)-\sum\_{k=1}^{H}O\left(\frac{1}{\sqrt{N^{k}}}\right), |  |

for any ui,h∈𝒜𝔽i,h​(I)u^{i,h}\in\mathcal{A}\_{\mathbb{F}^{i,h}}(I), where 𝐲ˇ−i,h\check{{\bf y}}^{-i,h} is defined as in Problem [1](https://arxiv.org/html/2511.12292v1#Thmproblem1 "Problem 1. ‣ 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").

###### Proof.

The proof is relegated to Appendix [B.1](https://arxiv.org/html/2511.12292v1#A2.SS1 "B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market").
∎

### 2.3 A Discussion of a Members’ Survival Model

In this section, we provide a discussion on extending our model to incorporate a survival framework, allowing for the possibility that members leave the MIC involuntarily, for example, due to discontinuation of business, default, regulatory intervention, or forced lapse. Let τi,h\tau^{i,h} denote the exit time of member ii in Class hh. We assume that the family of exit times (τi,h)i∈[Nh],h∈[H](\tau^{i,h})\_{i\in[N^{h}],\,h\in[H]} is independent, and that for each h∈[H]h\in[H], the collection (τi,h)i∈[Nh](\tau^{i,h})\_{i\in[N^{h}]} is identically distributed. Moreover, each exit time τi,h\tau^{i,h} is independent of the random variables associated with other members and the market variables, and is not determined by the members themselves. Note that now NhN^{h} denotes the initial number of members in Class hh. We shall assume that ℙ​(τh>T)>0\mathbb{P}(\tau^{h}>T)>0 for all h∈[H]h\in[H], where τh\tau^{h} represents the common distribution of τi,h\tau^{i,h}, i∈Nhi\in N^{h}.

Under the survival mode, the surplus process of the MIC is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ut=∑h=1H∑j=1Nh[(ch−dh)​vtj,h+eh−deh]​𝟙{τj,h>t}​d​t−∑h=1H∑j=1Nhvtj,h​𝟙{τj,h>t}​d​Ctj,h,dU\_{t}=\sum\_{h=1}^{H}\sum\_{j=1}^{N^{h}}\left[(c^{h}-d^{h})v^{j,h}\_{t}+e^{h}-d\_{e}^{h}\right]\mathds{1}\_{\{\tau^{j,h}>t\}}dt-\sum\_{h=1}^{H}\sum\_{j=1}^{N^{h}}v^{j,h}\_{t}\mathds{1}\_{\{\tau^{j,h}>t\}}dC^{j,h}\_{t}, |  | (7) |

indicating that only surviving members will purchase insurance, pay the membership fee, and transfer their loss to the MIC. Furthermore, let Nth:=∑j=1Nh𝟙{τj,h>t}N^{h}\_{t}:=\sum\_{j=1}^{N^{h}}\mathds{1}\_{\{\tau^{j,h}>t\}} be the number of surviving members in Class hh. As such,
the wealth process yi,hy^{i,h} of member ii from Class hh is given by, for t∈[0,τi,h∧T]t\in[0,\tau^{i,h}\wedge T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​yti,h\displaystyle dy^{i,h}\_{t} | =(r​yti,h+l~h−ch​vti,h)​d​t−(1−vti,h)​d​Cti,h\displaystyle=\left(ry^{i,h}\_{t}+\tilde{l}^{h}-c^{h}v^{i,h}\_{t}\right)dt-(1-v^{i,h}\_{t})dC^{i,h}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +πh∑l=1Hπl​Ntl​(∑k=1H∑j=1Nk[(ck−dk)​vtj,k+ek−dek]​𝟙{τj,k>t}​d​t−∑k=1H∑j=1Nkvtj,k​𝟙{τj,k>t}​d​Ctj,k)\displaystyle\quad+\frac{\pi^{h}}{\sum\_{l=1}^{H}\pi^{l}N^{l}\_{t}}\left(\sum\_{k=1}^{H}\sum\_{j=1}^{N^{k}}\left[(c^{k}-d^{k})v^{j,k}\_{t}+e^{k}-d\_{e}^{k}\right]\mathds{1}\_{\{\tau^{j,k}>t\}}dt-\sum\_{k=1}^{H}\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}\mathds{1}\_{\{\tau^{j,k}>t\}}dC^{j,k}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(r​yti,h+l~h,N−κh​vti,h+πh​(∑l=1Hπl​Nl∑l=1Hπl​Ntl)​∑k=1Hωk​(κk−dk)​∑j=1Nkvtj,k​𝟙{τj,k>t}Nk)​d​t\displaystyle=\left(ry^{i,h}\_{t}+\tilde{l}^{h,N}-\kappa^{h}v^{i,h}\_{t}+\pi^{h}\left(\frac{\sum\_{l=1}^{H}\pi^{l}N^{l}}{\sum\_{l=1}^{H}\pi^{l}N^{l}\_{t}}\right)\sum\_{k=1}^{H}\omega^{k}(\kappa^{k}-d^{k})\frac{\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}\mathds{1}\_{\{\tau^{j,k}>t\}}}{N^{k}}\right)dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +σh​(1−vti,h)​d​Wti,h+πh​(∑l=1Hπl​Nl∑l=1Hπl​Ntl)​∑k=1Hσk​ωk​∑j=1Nkvtj,k​𝟙{τj,k>t}Nk​d​Wtj,k,\displaystyle\quad+\sigma^{h}(1-v^{i,h}\_{t})dW^{i,h}\_{t}+\pi^{h}\left(\frac{\sum\_{l=1}^{H}\pi^{l}N^{l}}{\sum\_{l=1}^{H}\pi^{l}N^{l}\_{t}}\right)\sum\_{k=1}^{H}\sigma^{k}\omega^{k}\frac{\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}\mathds{1}\_{\{\tau^{j,k}>t\}}}{N^{k}}dW^{j,k}\_{t}, |  | (8) |

where ωh:=Nh/∑k=1Hπk​Nk\omega^{h}:=N^{h}/\sum\_{k=1}^{H}\pi^{k}N^{k}, h=1,…,Hh=1,\dots,H, and

|  |  |  |
| --- | --- | --- |
|  | l~th,N:=l~h−μh+πh​(∑l=1Hπl​Nl∑l=1Hπl​Ntl)​∑k=1Hωk​NtkNk​(ek−dek).\tilde{l}^{h,N}\_{t}:=\tilde{l}^{h}-\mu^{h}+\pi^{h}\left(\frac{\sum\_{l=1}^{H}\pi^{l}N^{l}}{\sum\_{l=1}^{H}\pi^{l}N^{l}\_{t}}\right)\sum\_{k=1}^{H}\omega^{k}\frac{N^{k}\_{t}}{N^{k}}(e^{k}-d\_{e}^{k}). |  |

The objective function for the ii-th member from Class hh under this involuntary exit model is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝒥i,h​(vi,h):=𝒥i,h​(vi,h;𝐲−i,h,𝐯−i,h)\displaystyle\mathcal{J}^{i,h}(v^{i,h})=\mathcal{J}^{i,h}\left(v^{i,h};{\bf y}^{-i,h},{\bf v}^{-i,h}\right) |  | (9) |
|  |  | :=𝔼​[∫0T∧τi,hfh​(t,yti,h,y¯ti,h,τh,v¯ti,h,τh)​𝑑t+𝟙{τi,h>T}​gh​(yTi,h,y¯Ti,h,τh)],\displaystyle\quad=\mathbb{E}\Bigg[\int\_{0}^{T\wedge\tau^{i,h}}f^{h}\left(t,y^{i,h}\_{t},\bar{y}^{i,h,\tau^{h}}\_{t},\bar{v}^{i,h,\tau^{h}}\_{t}\right)dt+\mathds{1}\_{\{\tau^{i,h}>T\}}g^{h}\left(y^{i,h}\_{T},\bar{y}^{i,h,\tau^{h}}\_{T}\right)\Bigg], |  |

where

|  |  |  |
| --- | --- | --- |
|  | y¯ti,h,τh:=∑j=1,j≠iNhytj,h​𝟙{τj,h>t}Nh−1,v¯ti,h,τh:=∑j=1,j≠iNhvtj,h​𝟙{τj,h>t}Nh−1.\bar{y}^{i,h,\tau^{h}}\_{t}:=\frac{\sum\_{j=1,j\neq i}^{N^{h}}y^{j,h}\_{t}\mathbbm{1}\_{\{\tau^{j,h}>t\}}}{N^{h}-1},\ \bar{v}^{i,h,\tau^{h}}\_{t}:=\frac{\sum\_{j=1,j\neq i}^{N^{h}}v^{j,h}\_{t}\mathbbm{1}\_{\{\tau^{j,h}>t\}}}{N^{h}-1}. |  |

The above formulation motivates the following mean field game formulation by passing to the limit Nh→∞N^{h}\to\infty, h∈[H]h\in[H]. Let (z~h)h∈[H](\widetilde{z}^{h})\_{h\in[H]} and (v~h)h∈[H](\widetilde{v}^{h})\_{h\in[H]} be exogeneously given, deterministic functions, and denote sth:=ℙ​(τh>t)s^{h}\_{t}:=\mathbb{P}(\tau^{h}>t). For i∈ℕi\in\mathbb{N} and h∈[H]h\in[H], let (xti,h)t∈[0,T](x^{i,h}\_{t})\_{t\in[0,T]} be the process that satisfies, for t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xti,h=(r​xti,h+l~th−κh​vti,h+πh​∑k=1Hωk​(κk−dk)​v~tk)​d​t+σh​(1−vti,h)​d​Wti,h,x0h=ξi,h,dx^{i,h}\_{t}=\left(rx^{i,h}\_{t}+\widetilde{l}^{h}\_{t}-\kappa^{h}v^{i,h}\_{t}+\pi^{h}\sum\_{k=1}^{H}\omega^{k}(\kappa^{k}-d^{k}){\widetilde{v}^{k}\_{t}}\right)dt+\sigma^{h}(1-v^{i,h}\_{t})dW^{i,h}\_{t},\ x^{h}\_{0}=\xi^{i,h}, |  | (10) |

where

|  |  |  |
| --- | --- | --- |
|  | l~th:=l~h−μh+πh∑l=1Hπl​ωl​stl​∑k=1Hωk​(ek−dek)​stk.\widetilde{l}^{h}\_{t}:=\tilde{l}^{h}-\mu^{h}+\frac{\pi^{h}}{\sum\_{l=1}^{H}\pi^{l}\omega^{l}s^{l}\_{t}}\sum\_{k=1}^{H}\omega^{k}(e^{k}-d\_{e}^{k})s^{k}\_{t}. |  |

Note that by the strong law of large numbers, as Nh→∞N^{h}\to\infty for h∈[H]h\in[H], we have almost surely that Ntk/Nk→stkN^{k}\_{t}/N^{k}\to s^{k}\_{t} and

|  |  |  |
| --- | --- | --- |
|  | ∑l=1Hπl​Nl∑k=1Hπk​Ntk=1∑k=1Hπk​(Nk∑l=1Hπl​Nl)​NtkNk=1∑k=1Hπk​ωk​NtkNk→1∑k=1Hπk​ωk​stk.\frac{\sum\_{l=1}^{H}\pi^{l}N^{l}}{\sum\_{k=1}^{H}\pi^{k}N^{k}\_{t}}=\frac{1}{\sum\_{k=1}^{H}\pi^{k}\left(\frac{N^{k}}{\sum\_{l=1}^{H}\pi^{l}N^{l}}\right)\frac{N^{k}\_{t}}{N^{k}}}=\frac{1}{\sum\_{k=1}^{H}\pi^{k}\omega^{k}\frac{N^{k}\_{t}}{N^{k}}}\to\frac{1}{\sum\_{k=1}^{H}\pi^{k}\omega^{k}s^{k}\_{t}}. |  |

In other words, l~th,N→l~th\tilde{l}^{h,N}\_{t}\to\widetilde{l}^{h}\_{t} a.s. when Nh→∞N^{h}\to\infty, h∈[H]h\in[H].

In light of the independence of (τi,h)i∈ℕ,h∈[H](\tau^{i,h})\_{i\in\mathbb{N},h\in[H]}, (Wi,h)i∈ℕ,h∈[H](W^{i,h})\_{i\in\mathbb{N},h\in[H]}, and (ξi,h)i∈ℕ,h∈[H](\xi^{i,h})\_{i\in\mathbb{N},h\in[H]}, and the fact that members’ dynamically systems are decoupled under the large-population limit, we introduce the following objective under the MFG formulation: for i∈ℕi\in\mathbb{N} and h∈[H]h\in[H],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ji,h​(vi,h)\displaystyle J^{i,h}(v^{i,h}) | :=Ji,h​(vi,h;z~h,v~h)=𝔼​[∫0T∧τi,hfh​(t,xti,h,z~th,vti,h,v~th)​𝑑t+𝟙{τi,h>T}​gh​(xTi,h,z~Th)]\displaystyle=J^{i,h}\left(v^{i,h};\widetilde{z}^{h},\widetilde{v}^{h}\right)=\mathbb{E}\left[\int\_{0}^{T\wedge\tau^{i,h}}f^{h}\left(t,x^{i,h}\_{t},\widetilde{z}^{h}\_{t},v^{i,h}\_{t},\widetilde{v}^{h}\_{t}\right)dt+\mathds{1}\_{\{\tau^{i,h}>T\}}g^{h}\left(x^{i,h}\_{T},\widetilde{z}^{h}\_{T}\right)\right] |  | (11) |
|  |  | =𝔼​[∫0Tf~h​(t,xti,h,z~th,vti,h,v~th)​𝑑t+g~h​(xTi,h,z~Th)],\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\tilde{f}^{h}\left(t,x^{i,h}\_{t},\widetilde{z}^{h}\_{t},v^{i,h}\_{t},\widetilde{v}^{h}\_{t}\right)dt+\tilde{g}^{h}\left(x^{i,h}\_{T},\widetilde{z}^{h}\_{T}\right)\right], |  |

where (z~h)h∈[H](\widetilde{z}^{h})\_{h\in[H]} and (v~h)h∈[H](\widetilde{v}^{h})\_{h\in[H]} are exogeneously given, and

|  |  |  |
| --- | --- | --- |
|  | f~h​(t,x,z,v,v~):=sth​fh​(t,x,z,v,v~)andg~h​(x,z):=sTh​g​(x,z).\tilde{f}^{h}(t,x,z,v,\widetilde{v}):=s^{h}\_{t}f^{h}(t,x,z,v,\widetilde{v})\quad\text{and}\quad\tilde{g}^{h}(x,z):=s^{h}\_{T}g(x,z). |  |

Comparing the mean field dynamics xi,hx^{i,h} with yi,hy^{i,h}, and the mean field objective functions ([11](https://arxiv.org/html/2511.12292v1#S2.E11 "In 2.3 A Discussion of a Members’ Survival Model ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) with ([9](https://arxiv.org/html/2511.12292v1#S2.E9 "In 2.3 A Discussion of a Members’ Survival Model ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")), we observe that z~th\widetilde{z}^{h}\_{t} essentially replaces the empirical average of the surviving members ∑j=1Nhytj,h​𝟙{τj,h>t}Nh−1\frac{\sum\_{j=1}^{N^{h}}y^{j,h}\_{t}\mathds{1}\_{\{\tau^{j,h}>t\}}}{N^{h}-1} under the NN-player game, while v~th\widetilde{v}^{h}\_{t} corresponds to

|  |  |  |
| --- | --- | --- |
|  | ∑l=1Hπl​Nl∑k=1Hπk​Ntk​∑j=1,j≠iNhvtj,h​𝟙{τi,h>t}Nh−1.\frac{\sum\_{l=1}^{H}\pi^{l}N^{l}}{\sum\_{k=1}^{H}\pi^{k}N^{k}\_{t}}\frac{\sum\_{j=1,j\neq i}^{N^{h}}v^{j,h}\_{t}\mathds{1}\_{\{\tau^{i,h}>t\}}}{N^{h}-1}. |  |

These observations naturally lead to the following MFG formulation and the corresponding definition of the mean field terms:

###### Problem 4.

Given the deterministic functions 𝐳~:=(z~h)h∈[H]\widetilde{\bf z}:=(\widetilde{z}^{h})\_{h\in[H]} and 𝐯~:=(v~h)h∈[H]\widetilde{\bf v}:=(\widetilde{v}^{h})\_{h\in[H]}, find the optimal control 𝐯:=(vh)h∈[H]{\bf v}:=(v^{h})\_{h\in[H]} such that for any h∈[H]h\in[H],

|  |  |  |
| --- | --- | --- |
|  | vh=arg⁡maxuh∈𝒜𝔽h​(I)Jh​(uh;z~h,v~h).v^{h}=\mathop{\arg\max}\_{u^{h}\in\mathcal{A}\_{\mathbb{F}^{h}}(I)}J^{h}\left(u^{h};\widetilde{z}^{h},\widetilde{v}^{h}\right). |  |

###### Problem 5.

Find the mean field equilibrium wealth 𝐳~=(z~h)h∈[H]\widetilde{\bf z}=(\widetilde{z}^{h})\_{h\in[H]} and strategy 𝐯~=(v~h)h∈[H]\widetilde{\bf v}=(\widetilde{v}^{h})\_{h\in[H]} such that for any t∈[0,T]t\in[0,T] and h∈[H]h\in[H],

|  |  |  |
| --- | --- | --- |
|  | z~th=𝔼​[xth]​sthandv~th=sth∑k=1Hπk​ωk​stk​𝔼​[vth].\widetilde{z}^{h}\_{t}=\mathbb{E}[x^{h}\_{t}]s^{h}\_{t}\quad\text{and}\quad\widetilde{v}^{h}\_{t}=\frac{s^{h}\_{t}}{\sum\_{k=1}^{H}\pi^{k}\omega^{k}s^{k}\_{t}}\mathbb{E}[v^{h}\_{t}]. |  |

The survival model represents an extension that falls largely under the framework of the original formulation The main differences are that the class weight now becomes time-dependent, and the definition of the mean field terms is revised to account for involuntary exits. Moreover, the independence of the exit times τi,h\tau^{i,h} allows the survival probability to be absorbed into the coefficients fhf^{h} and ghg^{h}. Under suitable conditions on the survival probabilities sths^{h}\_{t}, the analytical results and solution methodology developed in the main formulation remain valid within this extended survival framework.

In light of the above discussions, while our framework can naturally accommodate a more general survival model with involuntary exits, we shall focus on the original formulation given by ([5](https://arxiv.org/html/2511.12292v1#S2.E5 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"))-([6](https://arxiv.org/html/2511.12292v1#S2.E6 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) and Problems [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")-[3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").

### 2.4 Assumptions

In the sequel, we shall impose the following assumptions on the functions fhf^{h} and ghg^{h}.

###### Assumption 2.1.

For each h∈[H]h\in[H], the function fhf^{h} is differentiable in its xx- and vv-arguments, and ghg^{h} is differentiable in its xx-argument. In addition,

1. A.

   (Lipschitz continuity) There exist L,LX,LV>0L,L^{X},L^{V}>0 and Lg≥0L^{g}\geq 0 such that, for any h∈[H]h\in[H], t∈[0,T]t\in[0,T], and any x1,x2,z1,z2∈ℝx\_{1},x\_{2},z\_{1},z\_{2}\in\mathbb{R}, v1,v2,v¯1,v2¯∈Iv\_{1},v\_{2},\bar{v}\_{1},\bar{v\_{2}}\in I,

   1. (i)

      |fh​(t,x1,z1,v1,v¯1)−fh​(t,x2,z2,v2,v¯2)|≤L​(1+|x1|+|z1|+|v1|+|v¯1|+|x2|+|z2|+|v2|+|v¯2|)​(|x1−x2|+|z1−z2|+|v1−v2|+|v¯1−v¯2|)|f^{h}(t,x\_{1},z\_{1},v\_{1},\bar{v}\_{1})-f^{h}(t,x\_{2},z\_{2},v\_{2},\bar{v}\_{2})|\leq L(1+|x\_{1}|+|z\_{1}|+|v\_{1}|+|\bar{v}\_{1}|+|x\_{2}|+|z\_{2}|+|v\_{2}|+|\bar{v}\_{2}|)\left(|x\_{1}-x\_{2}|+|z\_{1}-z\_{2}|+|v\_{1}-v\_{2}|+|\bar{v}\_{1}-\bar{v}\_{2}|\right),
   2. (ii)

      |gh​(x1,z1)−gh​(x2,z2)|≤L​(1+|x1|+|x2|+|z1|+|z2|)​(|x1−x2|+|z1−z2|)|g^{h}(x\_{1},z\_{1})-g^{h}(x\_{2},z\_{2})|\leq L(1+|x\_{1}|+|x\_{2}|+|z\_{1}|+|z\_{2}|)(|x\_{1}-x\_{2}|+|z\_{1}-z\_{2}|),
   3. (iii)

      |fxh​(t,x1,z1,v1,v¯1)−fxh​(t,x2,z2,v2,v¯2)|≤LX​(|x1−x2|+|z1−z2|+|v1−v2|+|v¯1−v¯2|)|f^{h}\_{x}(t,x\_{1},z\_{1},v\_{1},\bar{v}\_{1})-f^{h}\_{x}(t,x\_{2},z\_{2},v\_{2},\bar{v}\_{2})|\leq L^{X}(|x\_{1}-x\_{2}|+|z\_{1}-z\_{2}|+|v\_{1}-v\_{2}|+|\bar{v}\_{1}-\bar{v}\_{2}|),
   4. (iv)

      |fvh​(t,x1,z1,v1,v¯1)−fvh​(t,x2,z2,v2,v¯2)|≤LV​(|x1−x2|+|z1−z2|+|v1−v2|+|v¯1−v¯2|)|f^{h}\_{v}(t,x\_{1},z\_{1},v\_{1},\bar{v}\_{1})-f^{h}\_{v}(t,x\_{2},z\_{2},v\_{2},\bar{v}\_{2})|\leq L^{V}(|x\_{1}-x\_{2}|+|z\_{1}-z\_{2}|+|v\_{1}-v\_{2}|+|\bar{v}\_{1}-\bar{v}\_{2}|),
   5. (v)

      |gxh​(x1,z1)−gxh​(x2,z2)|≤Lg​(|x1−x2|+|z1−z2|)|g^{h}\_{x}(x\_{1},z\_{1})-g^{h}\_{x}(x\_{2},z\_{2})|\leq L^{g}(|x\_{1}-x\_{2}|+|z\_{1}-z\_{2}|);
2. B.

   (α\alpha-concavity) The function v∈I↦fh​(t,x,z,v,v¯)v\in I\mapsto f^{h}(t,x,z,v,\bar{v}) is strictly concave for any t∈[0,T]t\in[0,T], x,z∈ℝx,z\in\mathbb{R}, v¯∈I\bar{v}\in I, and h∈[H]h\in[H]. In addition, there exist α1X>0\alpha^{X}\_{1}>0, α2X≥0\alpha^{X}\_{2}\geq 0, α1V>0,α2V≥0\alpha^{V}\_{1}>0,\alpha^{V}\_{2}\geq 0, and α1g>0,α2g≥0\alpha^{g}\_{1}>0,\alpha^{g}\_{2}\geq 0 such that, for any h∈[H]h\in[H],
   t∈[0,T]t\in[0,T], z1,z2∈ℝ,v¯1,v¯2∈Iz\_{1},z\_{2}\in\mathbb{R},\bar{v}\_{1},\bar{v}\_{2}\in I, and any (Xt1)t∈[0,T](X^{1}\_{t})\_{t\in[0,T]}, (Xt2)t∈[0,T],(Vt1)t∈[0,T](X^{2}\_{t})\_{t\in[0,T]},(V^{1}\_{t})\_{t\in[0,T]}, (Vt2)t∈[0,T]∈L𝔽h2​([0,T];ℝ)(V^{2}\_{t})\_{t\in[0,T]}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}),

   1. (i)

      𝔼​[(fxh​(t,Xt1,z1,Vt1,v¯1)−fxh​(t,Xt2,z2,Vt2,v¯2))​(Xt1−Xt2)]≤−α1X​𝔼​[|Xt1−Xt2|2]+α2X​|z1−z2|2\mathbb{E}\left[\left(f\_{x}^{h}(t,X^{1}\_{t},z\_{1},V^{1}\_{t},\bar{v}\_{1})-f\_{x}^{h}(t,X^{2}\_{t},z\_{2},V^{2}\_{t},\bar{v}\_{2})\right)(X^{1}\_{t}-X^{2}\_{t})\right]\leq-\alpha^{X}\_{1}\mathbb{E}[|X^{1}\_{t}-X^{2}\_{t}|^{2}]+\alpha^{X}\_{2}|z\_{1}-z\_{2}|^{2},
   2. (ii)

      𝔼​[(fvh​(t,Xt1,z1,Vt1,v¯1)−fvh​(t,Xt2,z2,Vt2,v¯2))​(Vt1−Vt2)]≤−α1V​𝔼​[|Vt1−Vt2|2]+α2V​|v¯1−v¯2|2\mathbb{E}\left[\left(f\_{v}^{h}(t,X^{1}\_{t},z\_{1},V^{1}\_{t},\bar{v}\_{1})-f\_{v}^{h}(t,X^{2}\_{t},z\_{2},V^{2}\_{t},\bar{v}\_{2})\right)(V^{1}\_{t}-V^{2}\_{t})\right]\leq-\alpha^{V}\_{1}\mathbb{E}[|V^{1}\_{t}-V^{2}\_{t}|^{2}]+\alpha^{V}\_{2}|\bar{v}\_{1}-\bar{v}\_{2}|^{2},
   3. (iii)

      𝔼​[(gxh​(XT1,z1)−gxh​(XT2,z2))​(XT1−XT2)]≤−α1g​𝔼​[|XT1−XT2|2]+α2g​|z1−z2|2\mathbb{E}[(g^{h}\_{x}(X^{1}\_{T},z\_{1})-g^{h}\_{x}(X^{2}\_{T},z\_{2}))(X^{1}\_{T}-X^{2}\_{T})]\leq-\alpha^{g}\_{1}\mathbb{E}[|X^{1}\_{T}-X^{2}\_{T}|^{2}]+\alpha^{g}\_{2}|z\_{1}-z\_{2}|^{2}.

###### Assumption 2.2.

For each h∈[H]h\in[H], for any t∈[0,T]t\in[0,T] and x,z∈ℝx,z\in\mathbb{R}, v¯∈I\bar{v}\in I, the function fvh​(t,x,z,⋅,v¯)f^{h}\_{v}(t,x,z,\cdot,\bar{v}) admits a unique inverse (fvh)−1​(⋅;t,x,z,v¯)(f^{h}\_{v})^{-1}(\cdot;t,x,z,\bar{v}). In addition, there exists ρh∈(0,1)\rho^{h}\in(0,1) such that, for any t∈[0,T]t\in[0,T] and u,v¯1,v¯2,v∈Iu,\bar{v}\_{1},\bar{v}\_{2},v\in I, x,z∈ℝx,z\in\mathbb{R}

|  |  |  |
| --- | --- | --- |
|  | |(fvh)−1​(u;t,x,z,v¯1)−(fvh)−1​(u;t,x,z,v¯2)|≤ρh​|v¯1−v¯2|.\left|(f^{h}\_{v})^{-1}\left(u;t,x,z,\bar{v}\_{1}\right)-(f^{h}\_{v})^{-1}\left(u;t,x,z,\bar{v}\_{2}\right)\right|\leq\rho^{h}\left|\bar{v}\_{1}-\bar{v}\_{2}\right|. |  |

Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") encompasses the standard Lipschitz and concavity condition that warrants the unique existence of the FBSDEs characterizing the optimal equilibrium solution; see Section [4](https://arxiv.org/html/2511.12292v1#S4 "4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"). These conditions are readily satisfied by quadratic rewards (Section [5](https://arxiv.org/html/2511.12292v1#S5 "5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), and more generally, by revised utility functions; see also Section [6.3](https://arxiv.org/html/2511.12292v1#S6.SS3 "6.3 General Mixture of Reward Functions ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") for an example. Assumption [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") ensures the solvability of the mean field fixed point defined in Problem [3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") below.

###### Remark 2.2.

By the mean value theorem, Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") implies that, for any z∈ℝz\in\mathbb{R}, v¯∈I\bar{v}\in I, and any (Xt1)t∈[0,T](X^{1}\_{t})\_{t\in[0,T]}, (Xt2)t∈[0,T](X^{2}\_{t})\_{t\in[0,T]}, (Vt1)t∈[0,T](V^{1}\_{t})\_{t\in[0,T]}, (Vt2)t∈[0,T]∈L𝔽h2​([0,T];ℝ)(V^{2}\_{t})\_{t\in[0,T]}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[fh​(t,Xt1,z,Vt1,v¯)−fh​(t,Xt2,z,Vt2,v¯)]\displaystyle\mathbb{E}\left[f^{h}(t,X^{1}\_{t},z,V^{1}\_{t},\bar{v})-f^{h}(t,X^{2}\_{t},z,V^{2}\_{t},\bar{v})\right] | ≤𝔼[fxh(t,Xt2,z,Vt2,v¯)(Xt1−Xt2)\displaystyle\leq\mathbb{E}\bigg[f^{h}\_{x}(t,X^{2}\_{t},z,V^{2}\_{t},\bar{v})(X^{1}\_{t}-X^{2}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +fvh(t,Xt2,z,Vt2,v¯)(Vt1−Vt2)],\displaystyle\quad+f^{h}\_{v}(t,X^{2}\_{t},z,V^{2}\_{t},\bar{v})(V^{1}\_{t}-V^{2}\_{t})\bigg], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[gh​(XT1,z)−gh​(XT2,z)]\displaystyle\mathbb{E}\left[g^{h}(X^{1}\_{T},z)-g^{h}(X^{2}\_{T},z)\right] | ≤𝔼​[gxh​(XT2,z)​(XT1−XT2)].\displaystyle\leq\mathbb{E}\left[g^{h}\_{x}(X^{2}\_{T},z)(X^{1}\_{T}-X^{2}\_{T})\right]. |  |

## 3 Optimal Mean Field Insurance Strategy

In this section, we construct the optimal insurance strategy of the representative member of each risk class h∈[H]h\in[H] under the mean field formulation (Problems [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") and [3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")). The proofs of statements in this section are relegated to Appendix [C](https://arxiv.org/html/2511.12292v1#A3 "Appendix C Proofs of Assertions in Section 3 ‣ Mean Field Analysis of Mutual Insurance Market").

By Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), one can verify that Jh​(⋅)J^{h}(\cdot) is concave and coercive, which guarantees the unique existence of optimal control of Problem [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"). The precise statement is formulated below.

###### Lemma 3.1.

Suppose that the mean field terms (zh)h=1H(z^{h})\_{h=1}^{H} and (v¯h)h=1H(\bar{v}^{h})\_{h=1}^{H} are exogeneously given. Under Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), for each h∈[H]h\in[H], the mapping vh∈L𝔽h2​([0,T];ℝ)↦Jh​(vh)v^{h}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R})\mapsto J^{h}(v^{h}) is continuous, strictly concave, and coercive. The last property means that Jh​(vh)→−∞J^{h}(v^{h})\to-\infty as 𝔼​[∫0T|vth|2​𝑑t]→∞\mathbb{E}[\int\_{0}^{T}|v^{h}\_{t}|^{2}dt]\to\infty.

###### Proof.

The proof is relegated to Appendix [C.1](https://arxiv.org/html/2511.12292v1#A3.SS1 "C.1 Proof of Lemma 3.1 ‣ Appendix C Proofs of Assertions in Section 3 ‣ Mean Field Analysis of Mutual Insurance Market").
∎

By Lemma [3.1](https://arxiv.org/html/2511.12292v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market"), if the constraint set II is unbounded, the unique existence of a global maximizer of Jh​(⋅)J^{h}(\cdot) in 𝒜𝔽h​(I)\mathcal{A}\_{\mathbb{F}^{h}}(I) given the mean field terms (zh)h=1H(z^{h})\_{h=1}^{H} and (v¯h)h=1H(\bar{v}^{h})\_{h=1}^{H} is a consequence of Theorem 7.2.12 of \@BBOPcite\@BAP\@BBNdrabek2007methods\@BBCP. On the other hand, if a,b∈ℝa,b\in\mathbb{R}, by the Banach–Alaoglu theorem,
the set 𝒜𝔽h​(I)⊂L𝔽h2​([0,T];ℝ)\mathcal{A}\_{\mathbb{F}^{h}}(I)\subset L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}) is weakly compact. Hence, the unique existence of a global maximizer of Jh​(⋅)J^{h}(\cdot) in 𝒜𝔽h​(I)\mathcal{A}\_{\mathbb{F}^{h}}(I) is an immediate consequence of the extreme value theorem (see Theorem 7.2.4 of \@BBOPcite\@BAP\@BBNdrabek2007methods\@BBCP).

The following statement characterizes the optimal insurance strategy of Problem [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") using the stochastic maximum principle.

###### Theorem 3.1.

Under Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), and given the deterministic functions (zh)h=1H(z^{h})\_{h=1}^{H} and (v¯h)h=1H(\bar{v}^{h})\_{h=1}^{H}, the optimal insurance strategy for the representative member in Class hh, h∈[H]h\in[H], is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | vth=ProjI​[(fvh)−1​(−(κh​pth+σh​ηth);t,xth,zth,v¯th)],v^{h}\_{t}=\textup{Proj}\_{I}\left[\left(f^{h}\_{v}\right)^{-1}\left(-\left(\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right);t,x^{h}\_{t},z^{h}\_{t},\bar{v}^{h}\_{t}\right)\right], |  | (12) |

where
(xh,ph,ηh)∈L𝔽h2​([0,T];ℝ3)(x^{h},p^{h},\eta^{h})\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}^{3}) is the solution of the following FBSDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​xth=(r​xth+l−κh​vth+πh​∑j=1Hωj​(κj−dj)​v¯tj)​d​t+σh​(1−vth)​d​Wth,−d​pth=(r​pth−fxh​(t,xth,zth,vth,v¯th))​d​t−ηth​d​Wth,x0h=ξh,pTh=−gx​(xTh,zTh).\begin{dcases}dx^{h}\_{t}=\left(rx^{h}\_{t}+l-\kappa^{h}v^{h}\_{t}+\pi^{h}\sum\_{j=1}^{H}\omega^{j}(\kappa^{j}-d^{j})\bar{v}^{j}\_{t}\right)dt+\sigma^{h}(1-v^{h}\_{t})dW^{h}\_{t},\\ -dp^{h}\_{t}=\left(rp^{h}\_{t}-f^{h}\_{x}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})\right)dt-\eta^{h}\_{t}dW^{h}\_{t},\\ x^{h}\_{0}=\xi^{h},\\ p^{h}\_{T}=-g\_{x}(x^{h}\_{T},z^{h}\_{T}).\end{dcases} |  | (13) |

###### Proof.

The proof is relegated to Appendix [C.2](https://arxiv.org/html/2511.12292v1#A3.SS2 "C.2 Proof of Theorem 3.1 ‣ Appendix C Proofs of Assertions in Section 3 ‣ Mean Field Analysis of Mutual Insurance Market").
∎

Theorem [3.1](https://arxiv.org/html/2511.12292v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market") presents the solution of Problem [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") given the mean field terms (zh)h=1H(z^{h})\_{h=1}^{H} and (vh)h=1H(v^{h})\_{h=1}^{H}. By taking expectations on ([13](https://arxiv.org/html/2511.12292v1#S3.E13 "In Theorem 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")), we see that the solution of the mean field game is characterized by, for each h∈[H]h\in[H],

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​xth=(r​xth+l−κh​vth+πh​∑j=1Hωj​(κj−dj)​v¯tj)​d​t+σh​(1−vth)​d​Wth,−d​pth=(r​pth−fxh​(t,xth,zth,vth,v¯th))​d​t−ηth​d​Wth,d​zth=(r​zth+l−κh​v¯th+π​∑j=1Hωj​(κj−dj)​v¯tj)​d​t,x0h=ξh,z0h=𝔼​[ξh],pTh=−gx​(xTh,zTh),\left\{\begin{aligned} dx^{h}\_{t}&=\left(rx^{h}\_{t}+l-\kappa^{h}v^{h}\_{t}+\pi^{h}\sum\_{j=1}^{H}\omega^{j}(\kappa^{j}-d^{j})\bar{v}^{j}\_{t}\right)dt+\sigma^{h}(1-v^{h}\_{t})dW^{h}\_{t},\\ -dp^{h}\_{t}&=\left(rp^{h}\_{t}-f^{h}\_{x}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})\right)dt-\eta^{h}\_{t}dW^{h}\_{t},\\ dz^{h}\_{t}&=\left(rz^{h}\_{t}+l-\kappa^{h}\bar{v}^{h}\_{t}+\pi\sum\_{j=1}^{H}\omega^{j}(\kappa^{j}-d^{j})\bar{v}^{j}\_{t}\right)dt,\\ x^{h}\_{0}&=\xi^{h},\\ z^{h}\_{0}&=\mathbb{E}[\xi^{h}],\\ p^{h}\_{T}&=-g\_{x}(x^{h}\_{T},z^{h}\_{T}),\end{aligned}\right. |  | (14) |

where for t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | vth\displaystyle v^{h}\_{t} | =ProjI​[(fvh)−1​(−(κh​pth+σh​ηth);t,xth,zth,v¯th)],\displaystyle=\text{Proj}\_{I}\left[\left(f^{h}\_{v}\right)^{-1}\left(-\left(\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right);t,x^{h}\_{t},z^{h}\_{t},\bar{v}^{h}\_{t}\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯th\displaystyle\bar{v}^{h}\_{t} | =𝔼​[ProjI​[(fvh)−1​(−(κh​pth+σh​ηth);t,xth,zth,v¯th)]].\displaystyle=\mathbb{E}\left[\text{Proj}\_{I}\left[\left(f^{h}\_{v}\right)^{-1}\left(-\left(\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right);t,x^{h}\_{t},z^{h}\_{t},\bar{v}^{h}\_{t}\right)\right]\right]. |  |

Notice that by Assumption [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), for any u,v¯1,v¯2∈Iu,\bar{v}\_{1},\bar{v}\_{2}\in I, x,z∈ℝx,z\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |ProjI​(fvh)−1​(u;t,x,z,v¯1)−ProjI​(fvh)−1​(u;t,x,z,v¯2)|\displaystyle\ \left|\text{Proj}\_{I}(f\_{v}^{h})^{-1}(u;t,x,z,\bar{v}\_{1})-\text{Proj}\_{I}(f\_{v}^{h})^{-1}(u;t,x,z,\bar{v}\_{2})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | |(fvh)−1​(u;t,x,z,v¯1)−(fvh)−1​(u;t,x,z,v¯2)|≤ρh​|v¯1−v¯2|.\displaystyle\ \left|(f\_{v}^{h})^{-1}(u;t,x,z,\bar{v}\_{1})-(f\_{v}^{h})^{-1}(u;t,x,z,\bar{v}\_{2})\right|\leq\rho^{h}|\bar{v}\_{1}-\bar{v}\_{2}|. |  |

Since ρh<1\rho^{h}<1, and the mapping

|  |  |  |
| --- | --- | --- |
|  | v¯h↦𝔼​[ProjI​[(fvh)−1​(−(κh​pth+σh​ηth);t,xth,zth,v¯th)]]\bar{v}^{h}\mapsto\mathbb{E}\left[\text{Proj}\_{I}\left[\left(f^{h}\_{v}\right)^{-1}\left(-\left(\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right);t,x^{h}\_{t},z^{h}\_{t},\bar{v}^{h}\_{t}\right)\right]\right] |  |

is clearly invariant in II, by the Banach fixed point theorem, there exists a unique fixed point v¯h\bar{v}^{h} that solves the last equation of ([14](https://arxiv.org/html/2511.12292v1#S3.E14 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")), provided that the MF-FBSDE is solvable.

Collecting all HH representative members, we obtain the following system of MF-FBSDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝐱t=(r​𝐱t+𝐥−𝐊𝐯t+𝚷​𝐯¯t)​d​t+𝚺​(𝐈−diag​(𝐯t))​d​𝐖t,−d​𝐩t=(r​𝐩t−∂𝐱𝐅​(t,𝐱t,𝐳t,𝐯t,𝐯¯t))​d​t−diag​(𝜼t)​d​𝐖t,𝐱0=(ξ1,…,ξh)⊤,𝐩T=−∂𝐱𝐆​(𝐱T,𝐳T),\left\{\begin{aligned} d{\bf x}\_{t}&=\left(r{\bf x}\_{t}+{\bf l}-{\bf K}{\bf v}\_{t}+{\bf\Pi}\bar{{\bf v}}\_{t}\right)dt+{\bf\Sigma}\left({\bf I}-\text{diag}({\bf v}\_{t})\right)d{\bf W}\_{t},\\ -d{\bf p}\_{t}&=\left(r{\bf p}\_{t}-\partial\_{\bf x}{\bf F}(t,{\bf x}\_{t},{\bf z}\_{t},{\bf v}\_{t},\bar{{\bf v}}\_{t})\right)dt-\text{diag}(\boldsymbol{\eta}\_{t})d{\bf W}\_{t},\\ {\bf x}\_{0}&=(\xi^{1},\dots,\xi^{h})^{\top},\\ {\bf p}\_{T}&=-\partial\_{\bf x}{\bf G}({\bf x}\_{T},{\bf z}\_{T}),\end{aligned}\right. |  | (15) |

where for t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐳t\displaystyle{\bf z}\_{t} | =𝔼​[𝐱t],\displaystyle=\mathbb{E}[{\bf x}\_{t}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐯¯t\displaystyle\bar{{\bf v}}\_{t} | =𝔼​[ProjIH​[(∂𝐯𝐅)−1​(−(𝐊𝐩t+𝚺​𝜼t);t,𝐱t,𝐳t,𝐯¯t)]],\displaystyle=\mathbb{E}\left[\text{Proj}\_{I^{H}}\left[\left(\partial\_{\bf v}{\bf F}\right)^{-1}\left(-\left({\bf K}{\bf p}\_{t}+{\bf\Sigma}\boldsymbol{\eta}\_{t}\right);t,{\bf x}\_{t},{\bf z}\_{t},\bar{{\bf v}}\_{t}\right)\right]\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐯t\displaystyle{\bf v}\_{t} | =ProjIH​[(∂𝐯𝐅)−1​(−(𝐊𝐩t+𝚺​𝜼t);t,𝐱t,𝐳t,𝐯¯t)],\displaystyle=\text{Proj}\_{I^{H}}\left[\left(\partial\_{\bf v}{\bf F}\right)^{-1}\left(-\left({\bf K}{\bf p}\_{t}+{\bf\Sigma}\boldsymbol{\eta}\_{t}\right);t,{\bf x}\_{t},{\bf z}\_{t},\bar{{\bf v}}\_{t}\right)\right], |  |

and the vectors and matrices in ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")) are defined as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝐱t=(xt1⋮xtH),𝐳t=(zt1⋮ztH),𝐩t=(pt1⋮ptH),𝜼t=(ηt1⋮ηtH),𝐯t=(vt1⋮vtH),𝐯¯t=(v¯t1⋮v¯tH),𝐖t=(Wt1⋮WtH),\displaystyle{\bf x}\_{t}=\begin{pmatrix}x^{1}\_{t}\\ \vdots\\ x^{H}\_{t}\end{pmatrix},{\bf z}\_{t}=\begin{pmatrix}z^{1}\_{t}\\ \vdots\\ z^{H}\_{t}\end{pmatrix},{\bf p}\_{t}=\begin{pmatrix}p^{1}\_{t}\\ \vdots\\ p^{H}\_{t}\end{pmatrix},\boldsymbol{\eta}\_{t}=\begin{pmatrix}\eta^{1}\_{t}\\ \vdots\\ \eta^{H}\_{t}\end{pmatrix},{\bf v}\_{t}=\begin{pmatrix}v^{1}\_{t}\\ \vdots\\ v^{H}\_{t}\end{pmatrix},{\bf\bar{v}}\_{t}=\begin{pmatrix}\bar{v}^{1}\_{t}\\ \vdots\\ \bar{v}^{H}\_{t}\end{pmatrix},{\bf W}\_{t}=\begin{pmatrix}W^{1}\_{t}\\ \vdots\\ W^{H}\_{t}\end{pmatrix}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝐥=(l1⋮lH),𝚷=(π1​ω1​(κ1−d1)⋯π1​ωH​(κH−dH)⋮⋮⋮πH​ω1​(κ1−d1)⋯πH​ωH​(κH−dH)),𝐅=(f1⋮fH),𝐆=(g1⋮gH),\displaystyle{\bf l}=\begin{pmatrix}l^{1}\\ \vdots\\ l^{H}\end{pmatrix},\boldsymbol{\Pi}=\begin{pmatrix}\pi^{1}\omega^{1}(\kappa^{1}-d^{1})&\cdots&\pi^{1}\omega^{H}(\kappa^{H}-d^{H})\\ \vdots&\vdots&\vdots\\ \pi^{H}\omega^{1}(\kappa^{1}-d^{1})&\cdots&\pi^{H}\omega^{H}(\kappa^{H}-d^{H})\end{pmatrix},\ {\bf F}=\begin{pmatrix}f^{1}\\ \vdots\\ f^{H}\end{pmatrix},\ {\bf G}=\begin{pmatrix}g^{1}\\ \vdots\\ g^{H}\end{pmatrix}, |  |

𝐊=diag​((κh)h=1H){\bf K}=\text{diag}((\kappa^{h})\_{h=1}^{H}), 𝚺=diag​((σh)h=1H){\bf\Sigma}=\text{diag}((\sigma^{h})\_{h=1}^{H}), ∂𝐱=diag​((∂xh)h=1H)\partial\_{\bf x}=\text{diag}((\partial\_{x^{h}})\_{h=1}^{H}), ∂𝐯=diag​((∂vh)h=1H)\partial\_{\bf v}=\text{diag}((\partial\_{v^{h}})\_{h=1}^{H}), and (∂𝐯𝐅)−1=((fv1)−1,…,(fvH)−1)⊤(\partial\_{\bf v}{\bf F})^{-1}=((f\_{v}^{1})^{-1},\dots,(f\_{v}^{H})^{-1})^{\top}.

## 4 Well-posedness of the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market"))

In this section, we establish the global existence and uniqueness of the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")), which therefore warrants the solvability of Problems [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")-[3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"). In the sequel, the term solution always refers to a triple (𝐱,𝐩,𝜼)({\bf x},{\bf p},\boldsymbol{\eta}) that satisfies ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")) and lies in L𝔽[H]2​([0,T];ℝ3​H)L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{3H}). The proofs of statements in this section are relegated to Appendix [D](https://arxiv.org/html/2511.12292v1#A4 "Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market").

In the technical perspective, canonical results in the literature concerning the global existence of MF-FBSDE cannot be directly applied herein due to two major aspects. First, as a result of the insurance constraint, the coefficients of the MF-FBSDE fail to satisfy the standard monotonicity property. Second, the forward equations depend directly on the mean field insurance strategies of the representative members from the other risk classes under the extended mean field game framework. Our approach thus involves adaptations of the well-known continuation approach (see e.g. \@BBOPcite\@BAP\@BBNbensoussan2017linear\@BBCP) by utilizing the properties of a projection map.

### 4.1 Assumptions for Well-posedness of MF-FBSDE

Before proceeding to the main results and proofs of this section, we introduce the following additional assumptions.

###### Assumption 4.1.

1. (a)

   (Separability) For any h∈[H]h\in[H], fhf^{h} is separable in the following sense:

   |  |  |  |
   | --- | --- | --- |
   |  | fh​(t,x,z,v,v¯)=fX,h​(t,x,z)+fV,h​(t,v,v¯),f^{h}(t,x,z,v,\bar{v})=f^{X,h}(t,x,z)+f^{V,h}(t,v,\bar{v}), |  |

   where fX,h:[0,T]×ℝ×ℝ→ℝ,fV,h:[0,T]×ℝ×ℝ→ℝf^{X,h}:[0,T]\times\mathbb{R}\times\mathbb{R}\to\mathbb{R},f^{V,h}:[0,T]\times\mathbb{R}\times\mathbb{R}\to\mathbb{R}.
2. (b)

   (Lipschitzity of fxX,hf^{X,h}\_{x}) For any h∈[H]h\in[H], t∈[0,T]t\in[0,T] and x1,x2,z1,z2∈ℝx\_{1},x\_{2},z\_{1},z\_{2}\in\mathbb{R},

   |  |  |  |
   | --- | --- | --- |
   |  | |fxX,h​(t,x1,z1)−fxX,h​(t,x2,z2)|≤LX​(|x1−x2|+|z1−z2|),|f^{X,h}\_{x}(t,x\_{1},z\_{1})-f^{X,h}\_{x}(t,x\_{2},z\_{2})|\leq L^{X}(|x\_{1}-x\_{2}|+|z\_{1}-z\_{2}|), |  |

   where LX>0L^{X}>0 is the constant in Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").
3. (c)

   (Convexity, and Lipschitzity of fvV,hf^{V,h}\_{v}) There exist αV,L1V,L2V>0\alpha^{V},L^{V}\_{1},L^{V}\_{2}>0 with αV>L2V\alpha^{V}>L^{V}\_{2} such that, for any h∈[H]h\in[H], t∈[0,T]t\in[0,T], h∈[H]h\in[H], and v,v1,v2,v¯,v¯1,v¯2∈ℝv,v\_{1},v\_{2},\bar{v},\bar{v}\_{1},\bar{v}\_{2}\in\mathbb{R},

   |  |  |  |
   | --- | --- | --- |
   |  | (v1−v2)​(fvV,h​(t,v1,v¯)−fvV,h​(t,v2,v¯))≤−αV​(v1−v2)2,\displaystyle(v\_{1}-v\_{2})(f^{V,h}\_{v}(t,v\_{1},\bar{v})-f^{V,h}\_{v}(t,v\_{2},\bar{v}))\leq-\alpha^{V}(v\_{1}-v\_{2})^{2}, |  |
   |  |  |  |
   | --- | --- | --- |
   |  | |fvV,h​(t,v1,v¯)−fvV,h​(t,v2,v¯)|≤L1V​|v1−v2|,\displaystyle\left|f^{V,h}\_{v}(t,v\_{1},\bar{v})-f^{V,h}\_{v}(t,v\_{2},\bar{v})\right|\leq L^{V}\_{1}|v\_{1}-v\_{2}|, |  |
   |  |  |  |
   | --- | --- | --- |
   |  | |fvV,h​(t,v,v¯1)−fvV,h​(t,v,v¯2)|≤L2V​|v¯1−v¯2|.\displaystyle|f^{V,h}\_{v}(t,v,\bar{v}\_{1})-f^{V,h}\_{v}(t,v,\bar{v}\_{2})|\leq L^{V}\_{2}|\bar{v}\_{1}-\bar{v}\_{2}|. |  |

To introduce the next assumption, we define the matrix 𝐌{\bf M} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐌:=𝚷​(𝚷−𝐊)−1.{\bf M}:={\bf\Pi}\left({\bf\Pi}-{\bf K}\right)^{-1}. |  | (16) |

The following result shows that 𝚷−𝐊{\bf\Pi}-{\bf K} is invertible, whence 𝐌{\bf M} is well-defined.

###### Lemma 4.1.

The matrix 𝚷−𝐊{\bf\Pi}-{\bf K} is invertible.

###### Proof.

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝅:=(π1⋯πh)⊤,𝝊:=(ω1​(κ1−dh)⋯ωh​(κh−dh))⊤.\boldsymbol{\pi}:=\begin{pmatrix}\pi^{1}&\cdots&\pi^{h}\end{pmatrix}^{\!\top},\ \boldsymbol{\upsilon}:=\begin{pmatrix}\omega^{1}(\kappa^{1}-d^{h})&\cdots&\omega^{h}(\kappa^{h}-d^{h})\end{pmatrix}^{\!\top}. |  | (17) |

Note that 𝚷−𝐊=𝝅​𝝊⊤−𝐊{\bf\Pi}-{\bf K}=\boldsymbol{\pi}\boldsymbol{\upsilon}^{\top}-{\bf K}, 𝐊{\bf K} is invertible and 𝝊⊤​𝐊−1​𝝅=∑h=1Hπh​ωh​κh−dκh<∑h=1Hπh​ωh=1\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}\boldsymbol{\pi}=\sum\_{h=1}^{H}\pi^{h}\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}<\sum\_{h=1}^{H}\pi^{h}\omega^{h}=1. By the Sherman–Morrison-Woodbury formula (see Section 2.1.3 on page 50 of \@BBOPcite\@BAP\@BBNgolub2013matrix\@BBCP), 𝚷−𝐊{\bf\Pi}-{\bf K} is invertible and

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝚷−𝐊)−1=−𝐊−1−𝐊−1​𝝅​𝝊⊤​𝐊−11−𝝊⊤​𝐊−1​𝝅.({\bf\Pi}-{\bf K})^{-1}=-{\bf K}^{-1}-\frac{{\bf K}^{-1}\boldsymbol{\pi}\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}}{1-\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}\boldsymbol{\pi}}. |  | (18) |

∎

###### Assumption 4.2.

1. (a)

   λmin​(𝐈−𝐌)>0\lambda\_{\min}({\bf I}-{\bf M})>0;
2. (b)

   There exist α𝐌,α𝐌𝐆>0\alpha\_{\bf M},\alpha^{\bf G}\_{\bf M}>0 such that, for any 𝐱i,𝐯i∈L𝔽[H]2​([0,T];ℝH){\bf x}^{i},{\bf v}^{i}\in L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{H}), i=1,2i=1,2,

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  |  | 𝔼[⟨𝐱t1−𝐱t2−𝐌𝔼[𝐱t1−𝐱t2],∂𝐱𝐅(𝐱t1,𝔼[𝐱t1],𝐯t1,𝔼[𝐯t1])\displaystyle\ \ \ \mathbb{E}\bigg[\bigg\langle{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}-{\bf M}\mathbb{E}[{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}],\partial\_{\bf x}{\bf F}({\bf x}^{1}\_{t},\mathbb{E}[{\bf x}^{1}\_{t}],{\bf v}^{1}\_{t},\mathbb{E}[{\bf v}^{1}\_{t}]) |  | (19) |
   |  |  | −∂𝐱𝐅(𝐱t2,𝔼[𝐱t2],𝐯t2,𝔼[𝐯t2])⟩]≤−α𝐌𝔼[∥𝐱t1−𝐱t2∥2],\displaystyle\quad-\partial\_{\bf x}{\bf F}({\bf x}^{2}\_{t},\mathbb{E}[{\bf x}^{2}\_{t}],{\bf v}^{2}\_{t},\mathbb{E}[{\bf v}^{2}\_{t}])\bigg\rangle\bigg]\leq-\alpha\_{{\bf M}}\mathbb{E}\left[\|{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}\|^{2}\right], |  |
   |  |  | 𝔼​[⟨𝐱T1−𝐱T2−𝐌​𝔼​[𝐱T1−𝐱T2],∂𝐱𝐆​(𝐱T1,𝔼​[𝐱T1])−∂𝐱𝐆​(𝐱T2,𝔼​[𝐱T2])⟩]\displaystyle\ \ \ \mathbb{E}\left[\left\langle{\bf x}^{1}\_{T}-{\bf x}^{2}\_{T}-{\bf M}\mathbb{E}[{\bf x}^{1}\_{T}-{\bf x}^{2}\_{T}],\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},\mathbb{E}[{\bf x}^{1}\_{T}])-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},\mathbb{E}[{\bf x}^{2}\_{T}])\right\rangle\right] |  |
   |  |  | ≤−α𝐌𝐆​𝔼​[‖𝐱T1−𝐱T2‖2].\displaystyle\leq-\alpha\_{\bf M}^{\bf G}\mathbb{E}\left[\|{\bf x}^{1}\_{T}-{\bf x}^{2}\_{T}\|^{2}\right]. |  |

###### Remark 4.1.

Assumption [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") implies Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").A.(iii)-(iv), and B.(ii).

The first condition of Assumption [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") requires the running rewards to be separable into two parts, namely, a state-dependent and a control-dependent component. This aligns with popular choices of rewards where a separate term is included to penalize extreme actions. The third condition requires fvV,hf^{V,h}\_{v} to be Lipschitz in the v¯\bar{v}-variable, where the Lipschitz constant L2VL^{V}\_{2} shall be smaller than the concavity constant αV\alpha^{V} with respect to the vv-variable. This reflects a smaller sensitivity of the representative member’s preference with respect to the mean field term, which thus captures a small mean field effect in practical MFGs.

Assumption [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") loosely requires that the matrix 𝐌{\bf M} has a moderate impact. In Proposition [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") below, we provide equivalent formulations of Assumption [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")(a), along with a sufficient condition on the model parameters that implies it. On the other hand, Assumption [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")(b) can be fulfilled by reward functions satisfying a slightly stronger monotonicity condition; see e.g. Section [5](https://arxiv.org/html/2511.12292v1#S5 "5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market") below. Alternatively, if the concavity constants α1X,α2X,α1g,α2g\alpha^{X}\_{1},\alpha^{X}\_{2},\alpha^{g}\_{1},\alpha^{g}\_{2} in Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").B satisfy α1X>α2X≥0\alpha^{X}\_{1}>\alpha^{X}\_{2}\geq 0 and α1g>α2g≥0\alpha^{g}\_{1}>\alpha^{g}\_{2}\geq 0, then ([19](https://arxiv.org/html/2511.12292v1#S4.E19 "In item (b) ‣ Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) holds if

|  |  |  |  |
| --- | --- | --- | --- |
|  | αX−2​LX​‖𝐌‖2>0,αg−2​Lg​‖𝐌‖2>0,\alpha^{X}-2L^{X}\|{\bf M}\|\_{2}>0,\ \alpha^{g}-2L^{g}\|{\bf M}\|\_{2}>0, |  | (20) |

where αX:=α1X−α2X\alpha^{X}:=\alpha^{X}\_{1}-\alpha^{X}\_{2} and αg:=α1g−α2g\alpha^{g}:=\alpha^{g}\_{1}-\alpha^{g}\_{2}. To see this, for any 𝐱i,𝐯i∈L𝔽[H]2​([0,T];ℝH){\bf x}^{i},{\bf v}^{i}\in L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{H}), i=1,2i=1,2, using Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), and Jensen’s inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨𝐱t1−𝐱t2−𝐌​𝔼​[𝐱t1−𝐱t2],∂𝐱𝐅​(𝐱t1,𝔼​[𝐱t1],𝐯t1,𝔼​[𝐯t1])−∂𝐱𝐅​(𝐱t2,𝔼​[𝐱t2],𝐯t2,𝔼​[𝐯t2])⟩]\displaystyle\ \ \ \ \mathbb{E}\bigg[\bigg\langle{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}-{\bf M}\mathbb{E}[{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}],\partial\_{\bf x}{\bf F}({\bf x}^{1}\_{t},\mathbb{E}[{\bf x}^{1}\_{t}],{\bf v}^{1}\_{t},\mathbb{E}[{\bf v}^{1}\_{t}])-\partial\_{\bf x}{\bf F}({\bf x}^{2}\_{t},\mathbb{E}[{\bf x}^{2}\_{t}],{\bf v}^{2}\_{t},\mathbb{E}[{\bf v}^{2}\_{t}])\bigg\rangle\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤−αX​𝔼​[|𝐱t1−𝐱t2|2]+LX​‖𝐌‖2​𝔼​[|𝐱t1−𝐱t2|​(|𝐱t1−𝐱t2|+|𝔼​[𝐱t1−𝐱t2]|)]\displaystyle\leq-\alpha^{X}\mathbb{E}\left[\left|{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}\right|^{2}\right]+L^{X}\|{\bf M}\|\_{2}\mathbb{E}\left[\left|{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}\right|\left(\left|{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}\right|+\left|\mathbb{E}[{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}]\right|\right)\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤−(αX−2​LX​‖𝐌‖2)​𝔼​[|𝐱t1−𝐱t2|2],\displaystyle\leq-(\alpha^{X}-2L^{X}\|{\bf M}\|\_{2})\mathbb{E}\left[\left|{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}\right|^{2}\right], |  |

so that we can pick α𝐌=αX−2​LX​‖𝐌‖2>0\alpha\_{\bf M}=\alpha^{X}-2L^{X}\|{\bf M}\|\_{2}>0. The second inequality in ([19](https://arxiv.org/html/2511.12292v1#S4.E19 "In item (b) ‣ Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) can be shown in the same manner. Following this idea, if 𝐅{\bf F} and 𝐆{\bf G} are independent of the argument 𝐳{\bf z}, the condition can be further relaxed to requiring

|  |  |  |  |
| --- | --- | --- | --- |
|  | α1X−LX​‖𝐌‖2,α1g−Lg​‖𝐌‖2>0.\alpha^{X}\_{1}-L^{X}\|{\bf M}\|\_{2},\ \alpha^{g}\_{1}-L^{g}\|{\bf M}\|\_{2}>0. |  | (21) |

###### Proposition 4.1.

The following conditions are equivalent:

1. 1.

   λmin​(𝐈−𝐌)>0\lambda\_{\min}({\bf I}-{\bf M})>0.
2. 2.

   λmax​(𝚷​𝐊−1)<1\lambda\_{\max}({\bf\Pi}{\bf K}^{-1})<1;
3. 3.

   ∑h=1Hπh​ωh​(κh−dh)κh+(∑h=1H(πh)2)​(∑h=1H(ωh​(κh−dh)κh)2)<2\sum\_{h=1}^{H}\frac{\pi^{h}\omega^{h}(\kappa^{h}-d^{h})}{\kappa^{h}}+\sqrt{\left(\sum\_{h=1}^{H}(\pi^{h})^{2}\right)\left(\sum\_{h=1}^{H}\left(\frac{\omega^{h}(\kappa^{h}-d^{h})}{\kappa^{h}}\right)^{2}\right)}<2.

In addition, the above conditions hold provided that

1. 4.

   suph∈[H]{πhωh}<infh∈[H]{πhωh​κhκh−d}\sup\_{h\in[H]}\left\{\frac{\pi^{h}}{\omega^{h}}\right\}<\inf\_{h\in[H]}\left\{\frac{\pi^{h}}{\omega^{h}}\frac{\kappa^{h}}{\kappa^{h}-d}\right\}.

###### Proof.

The proof is relegated to Appendix [D.1](https://arxiv.org/html/2511.12292v1#A4.SS1 "D.1 Proof of Proposition 4.1 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market").
∎

Proposition [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") indicates that the condition λmin​(𝐈−𝐌)>0\lambda\_{\min}({\bf I}-{\bf M})>0 is met if and only if the effect of the surplus distribution on members’ wealth, as captured by the magnitude of 𝚷{\bf\Pi}, remains sufficiently moderate relative to the premium rate and safety loading represented by 𝐊{\bf K}. This again echoes the small mean field requirement. In particular, the condition is satisfied when the ratios (πhωh)h=1H(\frac{\pi^{h}}{\omega^{h}})\_{h=1}^{H} do not deviate significantly between classes.

### 4.2 Uniqueness of Solution

We begin by establishing the uniqueness of solutions to the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")). The proof relies on the properties of the projection map (see Lemmas [A.1](https://arxiv.org/html/2511.12292v1#A1.Thmlemma1 "Lemma A.1. ‣ Appendix A Auxiliary Lemmas ‣ Mean Field Analysis of Mutual Insurance Market")–[A.2](https://arxiv.org/html/2511.12292v1#A1.Thmlemma2 "Lemma A.2. ‣ Appendix A Auxiliary Lemmas ‣ Mean Field Analysis of Mutual Insurance Market")), which enable us to derive a weaker form of monotonicity. Combined with Assumption [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), this allows us to bypass the stronger monotonicity conditions commonly assumed in the literature, which no longer hold herein due to the non-expansive nature of the projection map.

###### Theorem 4.1.

Under Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), and [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"),
the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")) admits at most one adapted solution.

###### Proof.

Consider two solutions (𝐱i,𝐩i,𝜼i)({\bf x}^{i},{\bf p}^{i},\boldsymbol{\eta}^{i}), i=1,2i=1,2, and let (𝐱~,𝐩~,𝜼~):=(𝐱1−𝐱2,𝐩1−𝐩2,𝜼1−𝜼2)(\tilde{{\bf x}},\tilde{{\bf p}},\tilde{\boldsymbol{\eta}}):=({\bf x}^{1}-{\bf x}^{2},{\bf p}^{1}-{\bf p}^{2},\boldsymbol{\eta}^{1}-\boldsymbol{\eta}^{2}). By applying Itô’s lemma to ⟨𝐱~t,𝐩~t⟩\langle\tilde{{\bf x}}\_{t},\tilde{{\bf p}}\_{t}\rangle, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​[⟨𝐱~T,∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)⟩]\displaystyle\ \ \ \ -\mathbb{E}\left[\langle\tilde{{\bf x}}\_{T},\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼[∫0T(⟨𝐫𝐱~t−𝐊𝐯~t+𝚷𝔼[𝐯~t],𝐩~t⟩−⟨𝜼~t,𝚺𝐯~t⟩\displaystyle=\mathbb{E}\Bigg[\int\_{0}^{T}\Bigg(\bigg\langle{\bf r}\tilde{\bf x}\_{t}-{\bf K}\tilde{\bf v}\_{t}+{\bf\Pi}\mathbb{E}[\tilde{\bf v}\_{t}],\tilde{{\bf p}}\_{t}\bigg\rangle-\langle\tilde{\boldsymbol{\eta}}\_{t},{\bf\Sigma}\tilde{{\bf v}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −⟨𝐱~t,r𝐩~t−(∂𝐱𝐅(t,𝐱t1,𝐳t1,𝐯t1,𝐯¯t1)−∂𝐱𝐅(t,𝐱t2,𝐳t2,𝐯t2,𝐯¯t2))⟩)dt]\displaystyle\qquad-\left\langle\tilde{{\bf x}}\_{t},r\tilde{{\bf p}}\_{t}-\left(\partial\_{\bf x}{\bf F}(t,{\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\bar{{\bf v}}^{1}\_{t})-\partial\_{\bf x}{\bf F}(t,{\bf x}^{2}\_{t},{\bf z}^{2}\_{t},{\bf v}^{2}\_{t},\bar{{\bf v}}^{2}\_{t})\right)\right\rangle\Bigg)dt\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼[∫0T(⟨𝐱~t,∂𝐱𝐅(t,𝐱t1,𝐳t1,𝐯t1,𝐯¯t1)−∂𝐱𝐅(t,𝐱t2,𝐳t2,𝐯t2,𝐯¯t2)⟩−⟨𝐯~t,𝐊𝐩~t+𝚺𝜼~t⟩\displaystyle=\mathbb{E}\Bigg[\int\_{0}^{T}\Bigg(\langle\tilde{{\bf x}}\_{t},\partial\_{\bf x}{\bf F}(t,{\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\bar{{\bf v}}^{1}\_{t})-\partial\_{\bf x}{\bf F}(t,{\bf x}^{2}\_{t},{\bf z}^{2}\_{t},{\bf v}^{2}\_{t},\bar{{\bf v}}^{2}\_{t})\rangle-\langle\tilde{{\bf v}}\_{t},{\bf K}\tilde{{\bf p}}\_{t}+{\bf\Sigma}\tilde{\boldsymbol{\eta}}\_{t}\rangle |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +⟨𝐩~t,𝚷𝔼[𝐯~t]⟩)dt],\displaystyle\qquad+\langle\tilde{{\bf p}}\_{t},{\bf\Pi}\mathbb{E}[\tilde{\bf v}\_{t}]\rangle\Bigg)dt\Bigg], |  | (22) |

where 𝐯¯ti:=𝔼​[𝐯ti]\bar{\bf v}^{i}\_{t}:=\mathbb{E}[{\bf v}^{i}\_{t}], i=1,2i=1,2.

To proceed, we establish the following weaker form of monotonicity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T⟨𝐯~t,𝐊​𝐩~t+𝚺​𝜼~t⟩​𝑑t]≥0.\mathbb{E}\left[\int\_{0}^{T}\langle\tilde{{\bf v}}\_{t},{\bf K}\tilde{{\bf p}}\_{t}+{\bf\Sigma}\tilde{\boldsymbol{\eta}}\_{t}\rangle dt\right]\geq 0. |  | (23) |

Indeed, for each h∈[H]h\in[H],

|  |  |  |
| --- | --- | --- |
|  | (vth,1−vth,2)​(κh​(pth,1−pth,2)+σh​(ηth,1−ηth,2))\displaystyle\ \ \ \ (v^{h,1}\_{t}-v^{h,2}\_{t})\left(\kappa^{h}(p^{h,1}\_{t}-p^{h,2}\_{t})+\sigma^{h}(\eta^{h,1}\_{t}-\eta^{h,2}\_{t})\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =(vth,1−vth,2)​[fvV,h​(t,v^th,2,v¯th,2)−fvV,h​(t,v^th,1,v¯th,1)],\displaystyle=(v^{h,1}\_{t}-v^{h,2}\_{t})\left[f^{V,h}\_{v}\left(t,\hat{v}^{h,2}\_{t},\bar{v}^{h,2}\_{t}\right)-f^{V,h}\_{v}\left(t,\hat{v}^{h,1}\_{t},\bar{v}^{h,1}\_{t}\right)\right], |  |

where for i=1,2i=1,2,

|  |  |  |
| --- | --- | --- |
|  | v^th,i:=(fvV,h)−1​(−κh​pth,i−σh​ηth,i;t,v¯th,i).\hat{v}^{h,i}\_{t}:=(f^{V,h}\_{v})^{-1}(-\kappa^{h}p^{h,i}\_{t}-\sigma^{h}\eta^{h,i}\_{t};t,\bar{v}^{h,i}\_{t}). |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (vth,1−vth,2)​(κh​(pth,1−pth,2)+σh​(ηth,1−ηth,2))\displaystyle\ \ \ \ (v^{h,1}\_{t}-v^{h,2}\_{t})\left(\kappa^{h}(p^{h,1}\_{t}-p^{h,2}\_{t})+\sigma^{h}(\eta^{h,1}\_{t}-\eta^{h,2}\_{t})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(vth,1−vth,2)​[fvV,h​(t,vth,1,v¯th,1)−fvV,h​(t,vth,2,v¯th,1)]\displaystyle=-(v^{h,1}\_{t}-v^{h,2}\_{t})\left[f^{V,h}\_{v}\left(t,v^{h,1}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,v^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(vth,1−vth,2)[(fvV,h(t,v^th,1,v¯th,1)−fvV,h(t,vth,1,v¯th,1))\displaystyle\quad-(v^{h,1}\_{t}-v^{h,2}\_{t})\Bigg[\left(f^{V,h}\_{v}\left(t,\hat{v}^{h,1}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,v^{h,1}\_{t},\bar{v}^{h,1}\_{t}\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(fvV,h(t,v^th,2,v¯th,1)−fvV,h(t,vth,2,v¯th,1))]\displaystyle\qquad-\left(f^{V,h}\_{v}\left(t,\hat{v}^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,v^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)\right)\Bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(vth,1−vth,2)​[fvV,h​(t,v^th,2,v¯th,1)−fvV,h​(t,v^th,2,v¯th,2)].\displaystyle\quad-(v^{h,1}\_{t}-v^{h,2}\_{t})\left[f^{V,h}\_{v}\left(t,\hat{v}^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,\hat{v}^{h,2}\_{t},\bar{v}^{h,2}\_{t}\right)\right]. |  | (24) |

By Assumption [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −(vth,1−vth,2)​(fvV,h​(t,vth,1,v¯th,1)−fvV,h​(t,vth,2,v¯th,1))≥αV​|vth,1−vth,2|2.\displaystyle-(v^{h,1}\_{t}-v^{h,2}\_{t})\left(f^{V,h}\_{v}\left(t,v^{h,1}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,v^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)\right)\geq\alpha^{V}|v^{h,1}\_{t}-v^{h,2}\_{t}|^{2}. |  | (25) |

On the other hand, by noticing that fvV,h​(t,⋅,v¯)f^{V,h}\_{v}(t,\cdot,\bar{v}) is non-increasing and vth,i=ProjI​[v^th,i]v^{h,i}\_{t}=\text{Proj}\_{I}[\hat{v}^{h,i}\_{t}], using Lemma [A.2](https://arxiv.org/html/2511.12292v1#A1.Thmlemma2 "Lemma A.2. ‣ Appendix A Auxiliary Lemmas ‣ Mean Field Analysis of Mutual Insurance Market"), we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(vth,1−vth,2)[(fvV,h(t,v^th,1,v¯th,1)−fvV,h(t,vth,1,v¯th,1))\displaystyle\ -(v^{h,1}\_{t}-v^{h,2}\_{t})\Bigg[\left(f^{V,h}\_{v}\left(t,\hat{v}^{h,1}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,v^{h,1}\_{t},\bar{v}^{h,1}\_{t}\right)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(fvV,h(t,v^th,2,v¯th,1)−fvV,h(t,vth,2,v¯th,1))]≥0.\displaystyle\qquad-\left(f^{V,h}\_{v}\left(t,\hat{v}^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,v^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)\right)\Bigg]\geq 0. |  | (26) |

Next, by Assumption [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −(vth,1−vth,2)​[fvV,h​(t,v^th,2,v¯th,1)−fvV,h​(t,v^th,2,v¯th,2)]\displaystyle-(v^{h,1}\_{t}-v^{h,2}\_{t})\left[f^{V,h}\_{v}\left(t,\hat{v}^{h,2}\_{t},\bar{v}^{h,1}\_{t}\right)-f^{V,h}\_{v}\left(t,\hat{v}^{h,2}\_{t},\bar{v}^{h,2}\_{t}\right)\right] | ≥−L2V​|vth,1−vth,2|​|v¯th,1−v¯th,2|.\displaystyle\geq-L^{V}\_{2}|v^{h,1}\_{t}-v^{h,2}\_{t}||\bar{v}^{h,1}\_{t}-\bar{v}^{h,2}\_{t}|. |  | (27) |

Hence, by combining ([4.2](https://arxiv.org/html/2511.12292v1#S4.Ex51 "4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"))-([27](https://arxiv.org/html/2511.12292v1#S4.E27 "In 4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) using Jensen’s inequality, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T(vth,1−vth,2)​(κh​(pth,1−pth,2)+σh​(ηth,1−ηth,2))​𝑑t]\displaystyle\ \ \ \ \mathbb{E}\left[\int\_{0}^{T}(v^{h,1}\_{t}-v^{h,2}\_{t})\left(\kappa^{h}(p^{h,1}\_{t}-p^{h,2}\_{t})+\sigma^{h}(\eta^{h,1}\_{t}-\eta^{h,2}\_{t})\right)dt\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≥∫0T(αV​𝔼​[|vth,1−vth,2|2]−L2V​𝔼​[|vth,1−vth,2|​|v¯th,1−v¯th,2|])​𝑑t\displaystyle\geq\int\_{0}^{T}\left(\alpha^{V}\mathbb{E}\left[|v^{h,1}\_{t}-v^{h,2}\_{t}|^{2}\right]-L^{V}\_{2}\mathbb{E}\left[|v^{h,1}\_{t}-v^{h,2}\_{t}||\bar{v}^{h,1}\_{t}-\bar{v}^{h,2}\_{t}|\right]\right)dt |  |
|  |  |  |
| --- | --- | --- |
|  | ≥∫0T(αV−L2V)​𝔼​[|vth,1−vth,2|2]​𝑑t≥0,\displaystyle\geq\int\_{0}^{T}(\alpha^{V}-L^{V}\_{2})\mathbb{E}\left[|v^{h,1}\_{t}-v^{h,2}\_{t}|^{2}\right]dt\geq 0, |  |

and thus ([23](https://arxiv.org/html/2511.12292v1#S4.E23 "In 4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) follows.

Next, by differentiating ⟨𝐌​𝐳~t,𝔼​[𝐩~t]⟩\langle{\bf M}\tilde{{\bf z}}\_{t},\mathbb{E}[\tilde{{\bf p}}\_{t}]\rangle with respect to tt, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T⟨𝔼​[𝐩~t],𝚷​𝔼​[𝐯~t]⟩​𝑑t\displaystyle\int\_{0}^{T}\langle\mathbb{E}[\tilde{{\bf p}}\_{t}],{\bf\Pi}\mathbb{E}[\tilde{\bf v}\_{t}]\rangle dt | =−⟨𝐌​𝐳~T,𝔼​[∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)]⟩\displaystyle=-\langle{\bf M}\tilde{{\bf z}}\_{T},\mathbb{E}\left[\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})\right]\rangle |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫0T⟨𝐌​𝐳~t,𝔼​[∂𝐱𝐅​(t,𝐱t1,𝐳t1,𝐯t1,𝐯¯t1)−∂𝐱𝐅​(t,𝐱t2,𝐳t2,𝐯t2,𝐯¯t2)]⟩​𝑑t.\displaystyle\hskip-28.45274pt-\int\_{0}^{T}\left\langle{\bf M}\tilde{{\bf z}}\_{t},\mathbb{E}\left[\partial\_{\bf x}{\bf F}(t,{\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\bar{{\bf v}}^{1}\_{t})-\partial\_{\bf x}{\bf F}(t,{\bf x}^{2}\_{t},{\bf z}^{2}\_{t},{\bf v}^{2}\_{t},\bar{{\bf v}}^{2}\_{t})\right]\right\rangle dt. |  | (28) |

By combining ([4.2](https://arxiv.org/html/2511.12292v1#S4.Ex44 "4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")), ([23](https://arxiv.org/html/2511.12292v1#S4.E23 "In 4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")), ([4.2](https://arxiv.org/html/2511.12292v1#S4.Ex59 "4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")), and using Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), and [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≥−𝔼​[⟨𝐱~T,∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)⟩]+⟨𝐌​𝐳~T,𝔼​[∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)]⟩\displaystyle\geq-\mathbb{E}\left[\langle\tilde{{\bf x}}\_{T},\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})\rangle\right]+\langle{\bf M}\tilde{{\bf z}}\_{T},\mathbb{E}\left[\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})\right]\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​[∫0T⟨𝐱~t,∂𝐱𝐅​(t,𝐱t1,𝐳t1,𝐯t1,𝐯¯t1)−∂𝐱𝐅​(t,𝐱t2,𝐳t2,𝐯t2,𝐯¯t2)⟩​𝑑t]\displaystyle\quad-\mathbb{E}\left[\int\_{0}^{T}\langle\tilde{{\bf x}}\_{t},\partial\_{\bf x}{\bf F}(t,{\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\bar{{\bf v}}^{1}\_{t})-\partial\_{\bf x}{\bf F}(t,{\bf x}^{2}\_{t},{\bf z}^{2}\_{t},{\bf v}^{2}\_{t},\bar{{\bf v}}^{2}\_{t})\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0T⟨𝐌​𝐳~t,𝔼​[∂𝐱𝐅​(t,𝐱t1,𝐳t1,𝐯t1,𝐯¯t1)−∂𝐱𝐅​(t,𝐱t2,𝐳t2,𝐯t2,𝐯¯t2)]⟩​𝑑t\displaystyle\quad+\int\_{0}^{T}\left\langle{\bf M}\tilde{{\bf z}}\_{t},\mathbb{E}\left[\partial\_{\bf x}{\bf F}(t,{\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\bar{{\bf v}}^{1}\_{t})-\partial\_{\bf x}{\bf F}(t,{\bf x}^{2}\_{t},{\bf z}^{2}\_{t},{\bf v}^{2}\_{t},\bar{{\bf v}}^{2}\_{t})\right]\right\rangle dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−𝔼​[⟨𝐱~T−𝐌​𝐳~T,∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)⟩]\displaystyle=-\mathbb{E}\left[\langle\tilde{{\bf x}}\_{T}-{\bf M}\tilde{{\bf z}}\_{T},\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​[∫0T⟨𝐱~t−𝐌​𝐳~t,∂𝐱𝐅​(t,𝐱t1,𝐳t1,𝐯t1,𝐯¯t1)−∂𝐱𝐅​(t,𝐱t2,𝐳t2,𝐯t2,𝐯¯t2)⟩​𝑑t]\displaystyle\quad-\mathbb{E}\left[\int\_{0}^{T}\langle\tilde{{\bf x}}\_{t}-{\bf M}\tilde{{\bf z}}\_{t},\partial\_{\bf x}{\bf F}(t,{\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\bar{{\bf v}}^{1}\_{t})-\partial\_{\bf x}{\bf F}(t,{\bf x}^{2}\_{t},{\bf z}^{2}\_{t},{\bf v}^{2}\_{t},\bar{{\bf v}}^{2}\_{t})\rangle dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥α𝐌𝐆​𝔼​[|𝐱~T|2]+α𝐌​𝔼​[∫0T|𝐱~t|2​𝑑t].\displaystyle\geq\alpha\_{\bf M}^{{\bf G}}\mathbb{E}\left[|\tilde{\bf x}\_{T}|^{2}\right]+\alpha\_{\bf M}\mathbb{E}\left[\int\_{0}^{T}|\tilde{{\bf x}}\_{t}|^{2}dt\right]. |  | (29) |

By standard a priori estimates of (F)BSDEs (see e.g. ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex255 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")) with δ=0\delta=0 below) and Grönwall’s inequality, we conclude that 𝐩1≡𝐩2{\bf p}^{1}\equiv{\bf p}^{2} and 𝜼1≡𝜼2\boldsymbol{\eta}^{1}\equiv\boldsymbol{\eta}^{2}.

∎

### 4.3 Global Existence of Solution

We proceed to prove the global existence of solution of the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")) by the continuation approach. To this end, we consider the following MF-FBSDE parameterized by μ∈[0,1]\mu\in[0,1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝐱^t=[−(1−μ)​𝐩^t+μ​(r​𝐱^t+𝐥−𝐊​𝐯^t+𝚷​𝔼​[𝐯^t])+ϕt]​d​t+[−(1−μ)​diag​(𝜼^t)+μ​𝚺​(𝐈−diag​(𝐯^t))+𝝍t]​d​𝐖t,−d​𝐩^t=[(1−μ)​𝐱^t+μ​(r​𝐩^t−∂𝐱𝐅​(t,𝐱^t,𝐳^t,𝐯^t,𝔼​[𝐯^t]))+𝝃t]​d​t−diag​(𝜼^t)​d​𝐖t,𝐱^0=𝐱0,𝐩^T=−μ​∂𝐱𝐆​(𝐱^T,𝐳^T)+(1−μ)​𝐱^T+𝜻T,\left\{\begin{aligned} d\hat{{\bf x}}\_{t}&=\left[-(1-\mu)\hat{{\bf p}}\_{t}+\mu\left(r\hat{{\bf x}}\_{t}+{\bf l}-{\bf K}\hat{{\bf v}}\_{t}+{\bf\Pi}\mathbb{E}[\hat{\bf v}\_{t}]\right)+\boldsymbol{\phi}\_{t}\right]dt\\ &\quad+\left[-(1-\mu)\text{diag}(\hat{\boldsymbol{\eta}}\_{t})+\mu{\bf\Sigma}({\bf I}-\text{diag}(\hat{{\bf v}}\_{t}))+\boldsymbol{\psi}\_{t}\right]d{\bf W}\_{t},\\ -d\hat{{\bf p}}\_{t}&=\left[(1-\mu)\hat{{\bf x}}\_{t}+\mu\left(r\hat{{\bf p}}\_{t}-\partial\_{\bf x}{\bf F}(t,\hat{\bf x}\_{t},\hat{\bf z}\_{t},\hat{\bf v}\_{t},\mathbb{E}[\hat{{\bf v}}\_{t}])\right)+\boldsymbol{\xi}\_{t}\right]dt-\text{diag}(\hat{\boldsymbol{\eta}}\_{t})d{\bf W}\_{t},\\ \hat{\bf x}\_{0}&={\bf x}\_{0},\\ \hat{{\bf p}}\_{T}&=-\mu\partial\_{\bf x}{\bf G}(\hat{{\bf x}}\_{T},\hat{{\bf z}}\_{T})+(1-\mu)\hat{{\bf x}}\_{T}+\boldsymbol{\zeta}\_{T},\end{aligned}\right. |  | (30) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐳^t\displaystyle\hat{{\bf z}}\_{t} | =𝔼​[𝐱^t],\displaystyle=\mathbb{E}[\hat{{\bf x}}\_{t}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐯^t\displaystyle\hat{{\bf v}}\_{t} | =ProjIH​[(∂𝐯𝐅)−1​(−(𝐊​𝐩^t+𝚺​𝜼^t);t,𝐱^t,𝐳^t,𝔼​[𝐯^t])],\displaystyle=\text{Proj}\_{I^{H}}\left[\left(\partial\_{\bf v}{\bf F}\right)^{-1}\left(-\left({\bf K}\hat{\bf p}\_{t}+{\bf\Sigma}\hat{\boldsymbol{\eta}}\_{t}\right);t,\hat{\bf x}\_{t},\hat{\bf z}\_{t},\mathbb{E}[\hat{\bf v}\_{t}]\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝐯^t]\displaystyle\mathbb{E}[\hat{\bf v}\_{t}] | =𝔼​[ProjIH​[(∂𝐯𝐅)−1​(−(𝐊​𝐩^t+𝚺​𝜼^t);t,𝐱^t,𝐳^t,𝔼​[𝐯^t])]],\displaystyle=\mathbb{E}\left[\text{Proj}\_{I^{H}}\left[\left(\partial\_{\bf v}{\bf F}\right)^{-1}\left(-\left({\bf K}\hat{\bf p}\_{t}+{\bf\Sigma}\hat{\boldsymbol{\eta}}\_{t}\right);t,\hat{\bf x}\_{t},\hat{\bf z}\_{t},\mathbb{E}[\hat{\bf v}\_{t}]\right)\right]\right], |  |

ϕ,𝝃∈L𝔽[H]2​([0,T];ℝH)\boldsymbol{\phi},\boldsymbol{\xi}\in L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{H}), 𝝍∈L𝔽[H]2​([0,T];ℝH×ℝH)\boldsymbol{\psi}\in L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{H}\times\mathbb{R}^{H}), and 𝜻T∈L2​(Ω,ℱT,ℙ)\boldsymbol{\zeta}\_{T}\in L^{2}(\Omega,\mathcal{F}\_{T},\mathbb{P}).

It is clear that ([30](https://arxiv.org/html/2511.12292v1#S4.E30 "In 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) admits a solution when μ=0\mu=0; see Lemma 2.5 of \@BBOPcite\@BAP\@BBNpeng1999fully\@BBCP. The following lemma establishes a contraction property such that, if the system admits a solution for some μ0∈[0,1)\mu\_{0}\in[0,1), then it also admits a solution for any μ∈[μ0,μ0+δ]\mu\in[\mu\_{0},\mu\_{0}+\delta] for some δ>0\delta>0 independent of μ0\mu\_{0}. Using this property recursively, we can extend the existence of a solution to μ=1\mu=1, thus proving the solvability of ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")).

###### Lemma 4.2.

Assume that there exists a constant μ0∈[0,1)\mu\_{0}\in[0,1) such that, for any ϕ,𝝃∈L𝔽[H]2​([0,T];ℝH)\boldsymbol{\phi},\boldsymbol{\xi}\in L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{H}), 𝝍∈L𝔽[H]2​([0,T];ℝH×ℝH)\boldsymbol{\psi}\in L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{H}\times\mathbb{R}^{H}), 𝜻T∈L2​(Ω,ℱT,ℙ)\boldsymbol{\zeta}\_{T}\in L^{2}(\Omega,\mathcal{F}\_{T},\mathbb{P}), the MF-FBSDE ([30](https://arxiv.org/html/2511.12292v1#S4.E30 "In 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) admits a solution. Then, under Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") and [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), there exists a δ0∈(0,1)\delta\_{0}\in(0,1) which only depends on TT, and independent of μ0\mu\_{0}, such that for any μ∈[μ0,μ0+δ0]\mu\in[\mu\_{0},\mu\_{0}+\delta\_{0}], the MF-FBSDE ([30](https://arxiv.org/html/2511.12292v1#S4.E30 "In 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) admits a solution for any ϕ,𝝃,𝝍\boldsymbol{\phi},\boldsymbol{\xi},\boldsymbol{\psi} and 𝜻T\boldsymbol{\zeta}\_{T}.

###### Proof.

The proof is relegated to Appendix [D.2](https://arxiv.org/html/2511.12292v1#A4.SS2 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market").
∎

As an immediate consequence of Theorem [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") and Lemma [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmlemma2 "Lemma 4.2. ‣ 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), we state the main result of this section.

###### Theorem 4.2.

Under Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") and [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")) admits a unique solution for any T>0T>0.

## 5 Quadratic Rewards

In this section, we consider a particular class of reward functions that are quadratic in representative members’ wealth and strategies, which can be interpreted as simultaneously maximizing wealth while penalizing deviations from a given target. This specification is analytically tractable and has been extensively applied in economics (\@BBOPcite\@BAP\@BBNHANSEN19807; hansen1995discounted; hansen2013recursive\@BBCP), and in the actuarial context (\@BBOPcite\@BAP\@BBNNGWIRA2007283; HUANG2010208; DELONG2019196\@BBCP). To be exact, for h∈[H]h\in[H], we let

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | fh​(t,x,𝐳,v,v¯)\displaystyle f^{h}(t,x,{\bf z},v,\bar{v}) | =fh​(t,x,zh,v,v¯):=−Qth2​(x−Sth​zh)2−Pth2​(v−Rth​v¯)2,\displaystyle=f^{h}(t,x,z^{h},v,\bar{v})=-\frac{Q^{h}\_{t}}{2}\left(x-S^{h}\_{t}z^{h}\right)^{2}-\frac{P^{h}\_{t}}{2}\left(v-R^{h}\_{t}\bar{v}\right)^{2}, |  | (31) |
|  | gh​(x,𝐳)\displaystyle g^{h}(x,{\bf z}) | =gh​(x,zh):=γh​x−QTh2​(x−STh​zh)2,\displaystyle=g^{h}(x,z^{h})=\gamma^{h}x-\frac{Q^{h}\_{T}}{2}\left(x-S^{h}\_{T}z^{h}\right)^{2}, |  |

where γh>0\gamma^{h}>0, and Q⋅h,P⋅h,S⋅hQ^{h}\_{\cdot},P^{h}\_{\cdot},S^{h}\_{\cdot} and R⋅hR^{h}\_{\cdot} are bounded deterministic functions with inft∈[0,T]Qt>0\inf\_{t\in[0,T]}Q\_{t}>0 and inft∈[0,T]Pth>0\inf\_{t\in[0,T]}P^{h}\_{t}>0. In other words, each member aims to maximize her own wealth while taking into account the fluctuations from the average wealth and strategies of other members from the same class, which mirrors a mean-variance objective. To facilitate the subsequent analysis, we define the following ℝH×ℝH\mathbb{R}^{H}\times\mathbb{R}^{H}-valued functions:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝐏t:=diag​((Pth)h=1H),𝐐t:=diag​((Qth)h=1H),\displaystyle{\bf P}\_{t}:=\text{diag}\left((P^{h}\_{t})\_{h=1}^{H}\right),\ {\bf Q}\_{t}:=\text{diag}\left((Q^{h}\_{t})\_{h=1}^{H}\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝐑t:=diag​((Rth)h=1H),𝐒t:=diag​((Sth)h=1H),\displaystyle{\bf R}\_{t}:=\text{diag}\left((R^{h}\_{t})\_{h=1}^{H}\right),\ {\bf S}\_{t}:=\text{diag}\left((S^{h}\_{t})\_{h=1}^{H}\right), |  | (32) |

and a ℝH\mathbb{R}^{H} column vector 𝜸=(γ1,…,γH)⊤\boldsymbol{\gamma}=(\gamma^{1},\dots,\gamma^{H})^{\top}.

### 5.1 Equilibrium Solution

Before stating the equilibrium solution under the quadratic reward functions ([31](https://arxiv.org/html/2511.12292v1#S5.E31 "In 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), we introduce the following assumption.

###### Assumption 5.1.

1. (a)

   supt∈[0,T]|Sth|<1\sup\_{t\in[0,T]}|S^{h}\_{t}|<1 for all h∈[H]h\in[H];
2. (b)

   supt∈[0,T]|Rth|<1\sup\_{t\in[0,T]}|R^{h}\_{t}|<1 for all h∈[H]h\in[H];
3. (c)

   λmin​(𝐈−𝐌)>0\lambda\_{\min}({\bf I}-{\bf M})>0.
4. (d)

   inft∈[0,T]λmin​((𝐈−𝐌⊤)​𝐐t​(𝐈−𝐒t))>0\inf\_{t\in[0,T]}\lambda\_{\min}(({\bf I}-{\bf M}^{\top}){\bf Q}\_{t}({\bf I}-{\bf S}\_{t}))>0.

Under the quadratic rewards ([31](https://arxiv.org/html/2511.12292v1#S5.E31 "In 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), it is clear that Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), and [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") are fulfilled given Assumption [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmassumption1 "Assumption 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")(a)-(b). In addition, Assumption [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") is a consequence of (c) and (d) in Assumption [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmassumption1 "Assumption 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market"). To see this, consider for any 𝐱i,𝐯i∈L𝔽H2​([0,T];ℝH){\bf x}^{i},{\bf v}^{i}\in L^{2}\_{\mathbb{F}^{H}}([0,T];\mathbb{R}^{H}), i=1,2i=1,2, and any t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[⟨𝐱t1−𝐱t2−𝐌​𝔼​[𝐱t1−𝐱t2],∂𝐱𝐅​(t,𝐱t1,𝔼​[𝐱t1],𝐯t1,𝔼​[𝐯t1])−∂𝐱𝐅​(t,𝐱t2,𝔼​[𝐱t2],𝐯t2,𝔼​[𝐯t2])⟩]\displaystyle\ \mathbb{E}\left[\bigg\langle{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}-{\bf M}\mathbb{E}[{\bf x}^{1}\_{t}-{\bf x}^{2}\_{t}],\partial\_{\bf x}{\bf F}(t,{\bf x}^{1}\_{t},\mathbb{E}[{\bf x}^{1}\_{t}],{\bf v}^{1}\_{t},\mathbb{E}[{\bf v}^{1}\_{t}])-\partial\_{\bf x}{\bf F}(t,{\bf x}^{2}\_{t},\mathbb{E}[{\bf x}^{2}\_{t}],{\bf v}^{2}\_{t},\mathbb{E}[{\bf v}^{2}\_{t}])\bigg\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[⟨𝐱~t−𝐌​𝐳~t,−𝐐t​(𝐱~t−𝐒t​𝐳~t)⟩]\displaystyle\ \mathbb{E}\left[\left\langle\tilde{{\bf x}}\_{t}-{\bf M}\tilde{{\bf z}}\_{t},-{\bf Q}\_{t}\left(\tilde{{\bf x}}\_{t}-{\bf S}\_{t}\tilde{{\bf z}}\_{t}\right)\right\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −𝔼​[⟨𝐱~t,𝐐t​𝐱~t⟩]+⟨𝐳~t,(𝐐t​𝐒t+𝐌⊤​𝐐t​(𝐈−𝐒t))​𝐳~t⟩\displaystyle\ -\mathbb{E}\left[\langle\tilde{{\bf x}}\_{t},{\bf Q}\_{t}\tilde{{\bf x}}\_{t}\rangle\right]+\left\langle\tilde{{\bf z}}\_{t},\left({\bf Q}\_{t}{\bf S}\_{t}+{\bf M}^{\top}{\bf Q}\_{t}({\bf I}-{\bf S}\_{t})\right)\tilde{{\bf z}}\_{t}\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | −min⁡{λmin​(𝐐t),λmin​((𝐈−𝐌⊤)​𝐐t​(𝐈−𝐒t))}​𝔼​[|𝐱~t|2],\displaystyle\ -\min\left\{\lambda\_{\min}({\bf Q}\_{t}),\lambda\_{\min}(({\bf I}-{\bf M}^{\top}){\bf Q}\_{t}({\bf I}-{\bf S}\_{t}))\right\}\mathbb{E}\left[|\tilde{{\bf x}}\_{t}|^{2}\right], |  |

where 𝐱~t:=𝐱t1−𝐱t2\tilde{{\bf x}}\_{t}:={\bf x}^{1}\_{t}-{\bf x}^{2}\_{t} and 𝐳~t:=𝐳t1−𝐳t2\tilde{{\bf z}}\_{t}:={\bf z}^{1}\_{t}-{\bf z}^{2}\_{t}, and the last line follows from Lemma [A.3](https://arxiv.org/html/2511.12292v1#A1.Thmlemma3 "Lemma A.3. ‣ Appendix A Auxiliary Lemmas ‣ Mean Field Analysis of Mutual Insurance Market"). By Assumption [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmassumption1 "Assumption 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")(d), we can take

|  |  |  |
| --- | --- | --- |
|  | α𝐌:=inft∈[0,T]{λmin​(𝐐t),λmin​((𝐈−𝐌⊤)​𝐐t​(𝐈−𝐒t))}>0.\alpha\_{\bf M}:=\inf\_{t\in[0,T]}\left\{\lambda\_{\min}({\bf Q}\_{t}),\lambda\_{\min}(({\bf I}-{\bf M}^{\top}){\bf Q}\_{t}({\bf I}-{\bf S}\_{t}))\right\}>0. |  |

Likewise, one can show that the same constant α𝐌g=α𝐌\alpha\_{{\bf M}}^{g}=\alpha\_{{\bf M}} can be used to satisfy ([19](https://arxiv.org/html/2511.12292v1#S4.E19 "In item (b) ‣ Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")), thereby fulfilling Assumption [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"). Although Assumption [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmassumption1 "Assumption 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")(c) and (d) are not equivalent, they both share the same key feature: the matrix 𝐌{\bf M} has only a moderate impact.

By Theorems [3.1](https://arxiv.org/html/2511.12292v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market") and [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), the solution of Problems [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")-[3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") under the quadratic rewards ([31](https://arxiv.org/html/2511.12292v1#S5.E31 "In 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) is immediately characterized by the following.

###### Corollary 5.1.

Under quadratic reward ([31](https://arxiv.org/html/2511.12292v1#S5.E31 "In 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝐱t=(r​𝐱t+𝐥−𝐊𝐯t+𝚷​𝐯¯t)​d​t+𝚺​(𝐈−diag​(𝐯t))​d​𝐖t,−d​𝐩t=(r​𝐩t+𝐐t​(𝐱t−𝐒t​𝐳t))​d​t−diag​(𝜼t)​d​𝐖t,𝐱0=(ξ1,…,ξH)⊤,𝐩T=𝐐T​(𝐱T−𝐒T​𝐳T)−𝜸,\left\{\begin{aligned} d{\bf x}\_{t}&=\left(r{\bf x}\_{t}+{\bf l}-{\bf K}{\bf v}\_{t}+{\bf\Pi}\bar{{\bf v}}\_{t}\right)dt+{\bf\Sigma}\left({\bf I}-\text{diag}({\bf v}\_{t})\right)d{\bf W}\_{t},\\ -d{\bf p}\_{t}&=\left(r{\bf p}\_{t}+{\bf Q}\_{t}({\bf x}\_{t}-{\bf S}\_{t}{\bf z}\_{t})\right)dt-\text{diag}(\boldsymbol{\eta}\_{t})d{\bf W}\_{t},\\ {\bf x}\_{0}&=(\xi^{1},\dots,\xi^{H})^{\top},\\ {\bf p}\_{T}&={\bf Q}\_{T}({\bf x}\_{T}-{\bf S}\_{T}{\bf z}\_{T})-\boldsymbol{\gamma},\end{aligned}\right. |  | (33) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝐳t=𝔼​[𝐱t],𝐯t=ProjIH​[𝐏t−1​(𝐊𝐩t+𝚺​𝜼t)+𝐑t​𝐯¯t],𝐯¯t=𝔼​[𝐯t],\displaystyle{\bf z}\_{t}=\mathbb{E}[{\bf x}\_{t}],\ {\bf v}\_{t}=\text{Proj}\_{I^{H}}\left[{\bf P}^{-1}\_{t}\left({\bf K}{\bf p}\_{t}+{\bf\Sigma}\boldsymbol{\eta}\_{t}\right)+{\bf R}\_{t}\bar{{\bf v}}\_{t}\right],\ \bar{{\bf v}}\_{t}=\mathbb{E}\left[{\bf v}\_{t}\right], |  |

and 𝐏t−1{\bf P}^{-1}\_{t} is the inverse matrix of 𝐏t{\bf P}\_{t}. In addition, Equation ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) is uniquely solvable under Assumption [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmassumption1 "Assumption 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market").

### 5.2 Equilibrium without Insurance Constraints

When no insurance constraint is imposed, i.e., I=ℝI=\mathbb{R}, the MF-FBSDE ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) admits a closed form solution, which can be represented in terms of the solutions of certain Riccati equations. In this case, the mean field term (v¯th)t∈[0,T](\bar{v}^{h}\_{t})\_{t\in[0,T]} and the optimal strategy (vth)t∈[0,T](v^{h}\_{t})\_{t\in[0,T]} can be reduced to the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vth=κh​pth+σh​ηthPth+Rth​v¯thandv¯th=κh​p¯th+σh​𝔼​[ηth]Pth​(1−Rth).v^{h}\_{t}=\frac{\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}}{P^{h}\_{t}}+R^{h}\_{t}\bar{v}^{h}\_{t}\quad\text{and}\quad\bar{v}^{h}\_{t}=\frac{\kappa^{h}\bar{p}^{h}\_{t}+\sigma^{h}\mathbb{E}[\eta^{h}\_{t}]}{P^{h}\_{t}(1-R^{h}\_{t})}. |  | (34) |

Let 𝚪⋅=diag​((Γ⋅h)h=1H):[0,T]→ℝH{\bf\Gamma}\_{\cdot}=\text{diag}((\Gamma^{h}\_{\cdot})\_{h=1}^{H}):[0,T]\to\mathbb{R}^{H} be the solution of the following Riccati equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Γthd​t−(κh)2​(Γth)2Pth+(σh)2​Γth+2​r​Γth+Qth=0,ΓTh=QTh.\begin{dcases}\frac{d\Gamma^{h}\_{t}}{dt}-\frac{(\kappa^{h})^{2}(\Gamma^{h}\_{t})^{2}}{P^{h}\_{t}+(\sigma^{h})^{2}\Gamma^{h}\_{t}}+2r\Gamma^{h}\_{t}+Q^{h}\_{t}=0,\\ \Gamma^{h}\_{T}=Q^{h}\_{T}.\end{dcases} |  | (35) |

Equation ([35](https://arxiv.org/html/2511.12292v1#S5.E35 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) enables us to characterize the system ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) and the optimal strategy by the deterministic functions 𝐩¯=(p¯h)h∈[H]\bar{{\bf p}}=(\bar{p}^{h})\_{h\in[H]} and 𝐳=(zh)h∈[H]{\bf z}=(z^{h})\_{h\in[H]} in an affine relationship. Indeed, using the ansatz and Itô’s lemma, it is straightforward to verify that 𝐩t=𝚪t​(𝐱t−𝐳t)+𝐩¯t{\bf p}\_{t}={\bf\Gamma}\_{t}({\bf x}\_{t}-{\bf z}\_{t})+\bar{\bf p}\_{t}, where (𝐩¯,𝐳)(\bar{\bf p},{\bf z}) satisfies the following FBODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝐳t=(r​𝐳t+𝐥+(𝚷−𝐊)​(𝐀t​𝐩¯t+𝐛t))​d​t,−d​𝐩¯t=(r​𝐩¯t+𝐐t​(𝐈−𝐒t)​𝐳t)​d​t,𝐳0=(𝔼​[ξ1],…,𝔼​[ξH]),𝐩¯T=𝐐T​(𝐈−𝐒T)​𝐳T−𝜸,\begin{dcases}d{\bf z}\_{t}=\left(r{\bf z}\_{t}+{\bf l}+\left({\bf\Pi}-{\bf K}\right)\left({\bf A}\_{t}\bar{{\bf p}}\_{t}+{\bf b}\_{t}\right)\right)dt,\\ -d\bar{{\bf p}}\_{t}=\left(r\bar{{\bf p}}\_{t}+{\bf Q}\_{t}({\bf I}-{\bf S}\_{t}){\bf z}\_{t}\right)dt,\\ {\bf z}\_{0}=(\mathbb{E}[\xi^{1}],\dots,\mathbb{E}[\xi^{H}]),\\ \bar{{\bf p}}\_{T}={\bf Q}\_{T}({\bf I}-{\bf S}\_{T}){\bf z}\_{T}-\boldsymbol{\gamma},\end{dcases} |  | (36) |

and

|  |  |  |
| --- | --- | --- |
|  | 𝐀t=𝐊​(𝚺2​𝚪t+𝐏t​(𝐈−𝐑t))−1,𝐛t=𝚺2​(𝚺2​𝚪t+𝐏t​(𝐈−𝐑t))−1​vec​(𝚪t),\displaystyle{\bf A}\_{t}={\bf K}\left({\bf\Sigma}^{2}\boldsymbol{\Gamma}\_{t}+{\bf P}\_{t}({\bf I}-{\bf R}\_{t})\right)^{-1},\ {\bf b}\_{t}={\bf\Sigma}^{2}\left({\bf\Sigma}^{2}\boldsymbol{\Gamma}\_{t}+{\bf P}\_{t}({\bf I}-{\bf R}\_{t})\right)^{-1}\text{vec}(\boldsymbol{\Gamma}\_{t}), |  |
|  |  |  |
| --- | --- | --- |
|  | 𝐂t=𝐊​(𝚺2​𝚪t+𝐏t)−1,𝐃t=𝐏t​𝐑t​(𝚺2​𝚪t+𝐏t)−1.\displaystyle{\bf C}\_{t}={\bf K}\left({\bf\Sigma}^{2}\boldsymbol{\Gamma}\_{t}+{\bf P}\_{t}\right)^{-1},\ {\bf D}\_{t}={\bf P}\_{t}{\bf R}\_{t}\left({\bf\Sigma}^{2}\boldsymbol{\Gamma}\_{t}+{\bf P}\_{t}\right)^{-1}. |  |

The discussion of the well-posedness of ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) is relegated to Appendix [E.2](https://arxiv.org/html/2511.12292v1#A5.SS2 "E.2 Well-posedness of (36) ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market"). Indeed, the FBODE ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) can further be reduced by considering the following ansatz:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐩¯t=𝚵t​𝐳t+𝜻t,\bar{{\bf p}}\_{t}={\bf\Xi}\_{t}{\bf z}\_{t}+\boldsymbol{\zeta}\_{t}, |  | (37) |

where 𝚵⋅:[0,T]→ℝH×ℝH{\bf\Xi}\_{\cdot}:[0,T]\to\mathbb{R}^{H}\times\mathbb{R}^{H} and 𝜻⋅:[0,T]→ℝH\boldsymbol{\zeta}\_{\cdot}:[0,T]\to\mathbb{R}^{H} satisfy the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝚵td​t+2​r​𝚵t+𝚵t​(𝚷−𝐊)​𝐀t​𝚵t+𝐐t​(𝐈−𝐒t)=0,d​𝜻td​t+(r​𝐈+𝚵t​(𝚷−𝐊)​𝐀t)​𝜻t+𝚵t​(𝐥+(𝚷−𝐊)​𝐛t)=0,𝚵T=𝐐T​(𝐈−𝐒T),𝜻T=−𝜸.\begin{dcases}\frac{d{\bf\Xi}\_{t}}{dt}+2r{\bf\Xi}\_{t}+{\bf\Xi}\_{t}\left({\bf\Pi}-{\bf K}\right){\bf A}\_{t}{\bf\Xi}\_{t}+{\bf Q}\_{t}({\bf I}-{\bf S}\_{t})=0,\\ \frac{d\boldsymbol{\zeta}\_{t}}{dt}+\left(r{\bf I}+{\bf\Xi}\_{t}\left({\bf\Pi}-{\bf K}\right){\bf A}\_{t}\right)\boldsymbol{\zeta}\_{t}+{\bf\Xi}\_{t}\left({\bf l}+\left({\bf\Pi}-{\bf K}\right){\bf b}\_{t}\right)=0,\\ {\bf\Xi}\_{T}={\bf Q}\_{T}({\bf I}-{\bf S}\_{T}),\\ \boldsymbol{\zeta}\_{T}=-\boldsymbol{\gamma}.\end{dcases} |  | (38) |

Hence, the well-posedness of ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) can be implied by that of ([38](https://arxiv.org/html/2511.12292v1#S5.E38 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), and the complete solution of the MFG can be characterized by ([35](https://arxiv.org/html/2511.12292v1#S5.E35 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) and ([38](https://arxiv.org/html/2511.12292v1#S5.E38 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")). The following summarizes the findings in this section.

###### Theorem 5.1.

Suppose that the system ([38](https://arxiv.org/html/2511.12292v1#S5.E38 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) admits a unique solution. Then, the optimal insurance strategy (𝐯t)t∈[0,T]({\bf v}\_{t})\_{t\in[0,T]} is given by

|  |  |  |
| --- | --- | --- |
|  | 𝐯t=𝐂t​(𝚪t​(𝐱t−𝐳t)+𝐩¯t)+𝐃t​𝐯¯t+𝐞t,{\bf v}\_{t}={\bf C}\_{t}\left({\bf\Gamma}\_{t}({\bf x}\_{t}-{\bf z}\_{t})+\bar{{\bf p}}\_{t}\right)+{\bf D}\_{t}\bar{{\bf v}}\_{t}+{\bf e}\_{t}, |  |

where 𝐞t=𝚺2​(𝚺2​𝚪t+𝐏t)−1​𝚪t{\bf e}\_{t}={\bf\Sigma}^{2}\left({\bf\Sigma}^{2}\boldsymbol{\Gamma}\_{t}+{\bf P}\_{t}\right)^{-1}\boldsymbol{\Gamma}\_{t}, 𝐯¯t=𝐀t​𝐩¯t+𝐛t\bar{{\bf v}}\_{t}={\bf A}\_{t}\bar{{\bf p}}\_{t}+{\bf b}\_{t}, 𝐩¯t\bar{\bf p}\_{t} is given by ([37](https://arxiv.org/html/2511.12292v1#S5.E37 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), and (𝐱t)t∈[0,T]({\bf x}\_{t})\_{t\in[0,T]}, (𝐳t)t∈[0,T]({\bf z}\_{t})\_{t\in[0,T]} are the solution of the following SDE and ODE, respectively:

|  |  |  |
| --- | --- | --- |
|  | {d​𝐱t=(r​𝐱t+𝐥−𝐊𝐯t+𝚷​𝐯¯t)​d​t+𝚺​(𝐈−diag​(𝐯t))​d​𝐖t,𝐱0=(ξh)h=1H,\displaystyle\left\{\begin{aligned} d{\bf x}\_{t}&=\left(r{\bf x}\_{t}+{\bf l}-{\bf K}{\bf v}\_{t}+{\bf\Pi}\bar{{\bf v}}\_{t}\right)dt+{\bf\Sigma}({\bf I}-\textup{diag}({\bf v}\_{t}))d{\bf W}\_{t},\\ {\bf x}\_{0}&=(\xi^{h})\_{h=1}^{H},\end{aligned}\right. |  |
|  |  |  |
| --- | --- | --- |
|  | {d​𝐳t=(r​𝐳t+𝐥+(𝚷−𝐊)​𝐯¯t)​d​t,𝐳0=(𝔼​[ξh])h=1H.\displaystyle\left\{\begin{aligned} d{\bf z}\_{t}&=\left(r{\bf z}\_{t}+{\bf l}+\left({\bf\Pi}-{\bf K}\right)\bar{{\bf v}}\_{t}\right)dt,\\ {\bf z}\_{0}&=(\mathbb{E}[\xi^{h}])\_{h=1}^{H}.\end{aligned}\right. |  |

###### Proof.

The proof is relegated to Appendix [E.1](https://arxiv.org/html/2511.12292v1#A5.SS1 "E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market").
∎

## 6 Numerical Experiments

In this section, we perform comprehensive numerical experiments to examine the equilibrium insurance strategies and the resulting wealth of representative members. All computations are performed using an NVIDIA RTX A5500 GPU.222The implementation code is publicly available on GitHub at: [https://github.com/WenyuanLi-HKU-SAAS/Mean-Field-Analysis-of-Mutual-Insurance-Market.git.](https://github.com/WenyuanLi-HKU-SAAS/Mean-Field-Analysis-of-Mutual-Insurance-Market.git) Supplementary tables in this section (Tables [3](https://arxiv.org/html/2511.12292v1#A6.T3 "Table 3 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market")-[6](https://arxiv.org/html/2511.12292v1#A6.T6 "Table 6 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market")) are provided in Appendix [F](https://arxiv.org/html/2511.12292v1#A6 "Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market").

In the first part of the experiment, we consider an MIC with two membership classes (H=2H=2), and the members exhibit quadratic rewards as described in ([31](https://arxiv.org/html/2511.12292v1#S5.E31 "In 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")). The following parameters are chosen as the baseline scenario:

|  |  |  |
| --- | --- | --- |
|  | r=0.03,l~1−μ1=l~2−μ2=0.02,P⋅1=P⋅2=Q⋅1=Q⋅2≡1,R⋅1=R⋅2≡0.1,\displaystyle r=0.03,\ \tilde{l}^{1}-\mu^{1}=\tilde{l}^{2}-\mu^{2}=0.02,\ P^{1}\_{\cdot}=P^{2}\_{\cdot}=Q^{1}\_{\cdot}=Q^{2}\_{\cdot}\equiv 1,\ R^{1}\_{\cdot}=R^{2}\_{\cdot}\equiv 0.1, |  |
|  |  |  |
| --- | --- | --- |
|  | S⋅1=S⋅2≡0.6,κ1=κ2=0.5,e1=e2=0.01,de1=de2=0.1​e1=0.001,\displaystyle S^{1}\_{\cdot}=S^{2}\_{\cdot}\equiv 0.6,\ \kappa^{1}=\kappa^{2}=0.5,\ e^{1}=e^{2}=0.01,\ d^{1}\_{e}=d^{2}\_{e}=0.1e^{1}=0.001, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ω1=ω2=0.5,σ1=σ2=0.3,γ1=γ2=1,ξ1=ξ2=2,d=0.05,T=1.\displaystyle\omega^{1}=\omega^{2}=0.5,\ \sigma^{1}=\sigma^{2}=0.3,\ \gamma^{1}=\gamma^{2}=1,\ \xi^{1}=\xi^{2}=2,\ d=0.05,\ T=1. |  | (39) |

The sharing proportion πh\pi^{h} of the surplus, and the fixed management fee rate dehd\_{e}^{h}, h=1,2h=1,2, are taken to be proportional to the membership fee as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πh:=eh∑k=12ek​ωk,deh=0.1​eh.\pi^{h}:=\frac{e^{h}}{\sum\_{k=1}^{2}e^{k}\omega^{k}},\ d\_{e}^{h}=0.1e^{h}. |  | (40) |

Under the baseline scenario, we have π1=1=π2\pi^{1}=1=\pi^{2} and de1=de2=0.001d\_{e}^{1}=d\_{e}^{2}=0.001. On the other hand, the net income rates are

|  |  |  |
| --- | --- | --- |
|  | l1=l~1−μ1−e1+π1​∑k=12ωk​(ek−dek)=0.019=l2.\displaystyle l^{1}=\tilde{l}^{1}-\mu^{1}-e^{1}+\pi^{1}\sum\_{k=1}^{2}\omega^{k}(e^{k}-d^{k}\_{e})=0.019=l^{2}. |  |

Furthermore, for h=1,2h=1,2, we set the cases listed in Table [2](https://arxiv.org/html/2511.12292v1#S6.T2 "Table 2 ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") to study the effect of the volatility σh\sigma^{h}, the safety loading κh\kappa^{h}, the risk aversion γh\gamma^{h}, the membership fee ehe^{h}, the net income rate before sharing l~h−μh\tilde{l}^{h}-\mu^{h}, and the relative class size ωh\omega^{h}.

Table 2: Parameters used across different test cases

|  |  |
| --- | --- |
| Case | Parameters |
| 1(a) | σ1=0.1\sigma^{1}=0.1, σ2=0.3\sigma^{2}=0.3 |
| 1(b) | ω1=0.8\omega^{1}=0.8, ω2=0.2\omega^{2}=0.2; σ1=0.1\sigma^{1}=0.1, σ2=0.3\sigma^{2}=0.3 |
| 1(c) | ω1=0.2\omega^{1}=0.2, ω2=0.8\omega^{2}=0.8; σ1=0.1\sigma^{1}=0.1, σ2=0.3\sigma^{2}=0.3 |
| 2(a) | γ1=1.0\gamma^{1}=1.0, γ2=1.6\gamma^{2}=1.6; |
| 2(b) | ω1=0.8\omega^{1}=0.8, ω2=0.2\omega^{2}=0.2; γ1=1.0\gamma^{1}=1.0, γ2=1.6\gamma^{2}=1.6 |
| 2(c) | ω1=0.2\omega^{1}=0.2, ω2=0.8\omega^{2}=0.8; γ1=1.0\gamma^{1}=1.0, γ2=1.6\gamma^{2}=1.6 |
| 3(a) | κ1=0.1\kappa^{1}=0.1, κ2=0.5\kappa^{2}=0.5, γ1=γ2=1.6\gamma^{1}=\gamma^{2}=1.6 |
| 3(b) | κ1=0.1\kappa^{1}=0.1, κ2=0.5\kappa^{2}=0.5, γ1=γ2=1.0\gamma^{1}=\gamma^{2}=1.0 |
| 4(a) | l~1−μ1=0.02\tilde{l}^{1}-\mu^{1}=0.02, l~2−μ2=0.1\tilde{l}^{2}-\mu^{2}=0.1 |
| 4(b) | e1=0.1e^{1}=0.1, e2=0.01e^{2}=0.01; l~1−μ1=0.02\tilde{l}^{1}-\mu^{1}=0.02, l~2−μ2=0.1\tilde{l}^{2}-\mu^{2}=0.1 |
| 4(c) | e1=0.01e^{1}=0.01, e2=0.1e^{2}=0.1; l~1−μ1=0.02\tilde{l}^{1}-\mu^{1}=0.02, l~2−μ2=0.1\tilde{l}^{2}-\mu^{2}=0.1 |

For all cases, we consider two scenarios: with and without an insurance constraint. In the former case, we impose an insurance constraint I=[0,1]I=[0,1], i.e., members are prohibited from taking a “short position”, nor transferring an amount more than their actual losses to the MIC. We remark that all the combinations of parameters above satisfy Assumption [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmassumption1 "Assumption 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market").

To obtain the optimal insurance strategies and the equilibrium wealth under insurance constraint, we solve the FBSDE ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) numerically using a deep BSDE approach, and the details are elaborated in the next subsection.

### 6.1 Neural Network Architectures

The deep BSDE approach presented in this subsection is an adaptation of the methods introduced in \@BBOPcite\@BAP\@BBNgermain2022numerical; carmona2022convergence; han2024learning\@BBCP. The central idea is to approach the backward equation (𝐩t)t∈[0,T]({\bf p}\_{t})\_{t\in[0,T]} in a forward manner, treating the initial value 𝐩0{\bf p}\_{0} as a trainable component by a neural network. The system is then simulated forward in time, solving both the forward equation for (𝐱t)t∈[0,T]({\bf x}\_{t})\_{t\in[0,T]} and the backward equation for (𝐩t)t∈[0,T]({\bf p}\_{t})\_{t\in[0,T]} using Monte Carlo methods. The loss function for the neural network is defined as the deviation between the simulated value 𝐩T{\bf p}\_{T} at the terminal time, and the prescribed terminal condition of the original backward equation. To accommodate the extended mean field game framework, a penalty term is introduced for the mean field term (𝐯¯t)t∈[0,T](\bar{{\bf v}}\_{t})\_{t\in[0,T]} to ensure the additional fixed point condition is satisfied. The complete architecture is described as follows.

We begin by building six neural networks for v¯1,v¯2,η1,η2,p01,p02\bar{v}^{1},\bar{v}^{2},\eta^{1},\eta^{2},p^{1}\_{0},p^{2}\_{0}: for t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | v¯t1=𝒩​𝒩1ϕ1​(t),v¯t2=𝒩​𝒩2ϕ2​(t),\displaystyle\bar{v}^{1}\_{t}=\mathcal{NN}^{\phi\_{1}}\_{1}(t),~\bar{v}^{2}\_{t}=\mathcal{NN}^{\phi\_{2}}\_{2}(t), |  |
|  |  |  |
| --- | --- | --- |
|  | ηt1=𝒩​𝒩3ϕ3​(t,xt1,zt1,pt1),ηt2=𝒩​𝒩4ϕ4​(t,xt2,zt2,pt2),\displaystyle\eta^{1}\_{t}=\mathcal{NN}^{\phi\_{3}}\_{3}(t,x^{1}\_{t},z^{1}\_{t},p^{1}\_{t}),~\eta^{2}\_{t}=\mathcal{NN}^{\phi\_{4}}\_{4}(t,x^{2}\_{t},z^{2}\_{t},p^{2}\_{t}), |  |
|  |  |  |
| --- | --- | --- |
|  | p01=𝒩​𝒩5ϕ5​(x01),p02=𝒩​𝒩6ϕ6​(x02),\displaystyle~p^{1}\_{0}=\mathcal{NN}^{\phi\_{5}}\_{5}(x^{1}\_{0}),~p^{2}\_{0}=\mathcal{NN}^{\phi\_{6}}\_{6}(x^{2}\_{0}), |  |

where ϕi\phi\_{i} are the weights and biases of neural network 𝒩​𝒩i\mathcal{NN}\_{i}. The optimal strategies are then computed by

|  |  |  |
| --- | --- | --- |
|  | vth=ProjI​[(fvh)−1​(−(κh​pth+σh​ηth);t,v¯th)],h=1,2.v^{h}\_{t}=\text{Proj}\_{I}\left[(f^{h}\_{v})^{-1}(-(\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t});t,\bar{v}^{h}\_{t})\right],\ h=1,2. |  |

Each neural network 𝒩​𝒩iϕi\mathcal{NN}\_{i}^{\phi\_{i}} above is chosen to have two hidden layers, and each layer consists of 32 hidden nodes. The Rectified Linear Unit (ReLU) function and the identity function are chosen as the activation function in the hidden layer and the output layer, respectively. Figure [1](https://arxiv.org/html/2511.12292v1#S6.F1 "Figure 1 ‣ 6.1 Neural Network Architectures ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") shows the structure of the neural network for (ηt1)t∈[0,T](\eta^{1}\_{t})\_{t\in[0,T]}. For cases with constraint 𝐯t∈[0,1]H{\bf v}\_{t}\in[0,1]^{H}, v¯th\bar{v}^{h}\_{t} are defined by projecting the output of the neural network 𝒩​𝒩h\mathcal{NN}\_{h} to I=[0,1]I=[0,1]:

|  |  |  |
| --- | --- | --- |
|  | v¯t1=Proj[0,1]​[𝒩​𝒩1ϕ1​(t)],v¯t2=Proj[0,1]​[𝒩​𝒩2ϕ2​(t)].\displaystyle\bar{v}^{1}\_{t}=\text{Proj}\_{[0,1]}[\mathcal{NN}^{\phi\_{1}}\_{1}(t)],~\bar{v}^{2}\_{t}=\text{Proj}\_{[0,1]}[\mathcal{NN}^{\phi\_{2}}\_{2}(t)]. |  |

To simulate the SDEs using the Euler-Maruyama method, we discretize [0,T][0,T] into a partition 𝒯={ti:i​Δ​t,i=0,1,…,M}\mathcal{T}=\{t\_{i}:i\Delta t,i=0,1,...,M\}, where Δ​t=T/M\Delta t=T/M. Then, we can formulate the loss function and the simulation scheme as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minϕ1,ϕ2,ϕ3,ϕ4,ϕ5,ϕ6​∑h=12𝔼​[(pTh+γh−QTh​(xTh−STh​zTh))2]+λM​∑i=0M−1∑h=12(𝔼​[vtih]−v¯tih)2,\displaystyle\min\limits\_{\phi\_{1},\phi\_{2},\phi\_{3},\phi\_{4},\phi\_{5},\phi\_{6}}\sum\limits\_{h=1}^{2}\mathbb{E}\left[(p^{h}\_{T}+\gamma^{h}-Q^{h}\_{T}(x^{h}\_{T}-S^{h}\_{T}z^{h}\_{T}))^{2}\right]+\frac{\lambda}{M}\sum\limits\_{i=0}^{M-1}\sum\limits\_{h=1}^{2}(\mathbb{E}[v^{h}\_{t\_{i}}]-\bar{v}^{h}\_{t\_{i}})^{2}, |  | (41) |
|  |  |  |
| --- | --- | --- |
|  | s.t.​xti+1h=xtih+(r​xtih+lh−κh​vtih+πh​∑j=12ωj​(κj−dj)​v¯tij)​Δ​t+σh​(1−vtih)​Δ​Wtih,\displaystyle\text{s.t.}~x^{h}\_{t\_{i+1}}=x^{h}\_{t\_{i}}+\left(rx^{h}\_{t\_{i}}+l^{h}-\kappa^{h}v^{h}\_{t\_{i}}+\pi^{h}\sum\limits\_{j=1}^{2}\omega^{j}(\kappa^{j}-d^{j})\bar{v}^{j}\_{t\_{i}}\right)\Delta t+\sigma^{h}(1-v^{h}\_{t\_{i}})\Delta W^{h}\_{t\_{i}}, |  |
|  |  |  |
| --- | --- | --- |
|  | pti+1h=ptih−[r​ptih−fxh,X​(t,xtih,ztih)]​Δ​t+ηtih​Δ​Wtih,\displaystyle~~~~~p^{h}\_{t\_{i+1}}=p^{h}\_{t\_{i}}-[rp^{h}\_{t\_{i}}-f^{h,X}\_{x}(t,x^{h}\_{t\_{i}},z^{h}\_{t\_{i}})]\Delta t+\eta^{h}\_{t\_{i}}\Delta W^{h}\_{t\_{i}}, |  |
|  |  |  |
| --- | --- | --- |
|  | zti+1h=ztih+(r​ztih+lh−κh​v¯tih+πh​∑j=12ωj​(κj−dj)​v¯tij)​Δ​t,\displaystyle~~~~~z^{h}\_{t\_{i+1}}=z^{h}\_{t\_{i}}+\left(rz^{h}\_{t\_{i}}+l^{h}-\kappa^{h}\bar{v}^{h}\_{t\_{i}}+\pi^{h}\sum\limits\_{j=1}^{2}\omega^{j}(\kappa^{j}-d^{j})\bar{v}^{j}\_{t\_{i}}\right)\Delta t, |  |
|  |  |  |
| --- | --- | --- |
|  | x0h=ξh,z0h=𝔼​[ξh],pTh=−γh+QTh​(xTh−STh​zTh),\displaystyle~~~~~x^{h}\_{0}=\xi^{h},~z^{h}\_{0}=\mathbb{E}[\xi^{h}],~p^{h}\_{T}=-\gamma^{h}+Q^{h}\_{T}(x^{h}\_{T}-S^{h}\_{T}z^{h}\_{T}), |  |
|  |  |  |
| --- | --- | --- |
|  | v¯t1=ProjI​[𝒩​𝒩1ϕ1​(ti)],v¯t2=ProjI​[𝒩​𝒩2ϕ2​(ti)],\displaystyle~~~~~\bar{v}^{1}\_{t}=\text{Proj}\_{I}[\mathcal{NN}^{\phi\_{1}}\_{1}(t\_{i})],~\bar{v}^{2}\_{t}=\text{Proj}\_{I}[\mathcal{NN}^{\phi\_{2}}\_{2}(t\_{i})], |  |
|  |  |  |
| --- | --- | --- |
|  | vti1=ProjI​[(fv1)−1​(−(κ1​pti1+σ1​ηti1);t,v¯ti1)],vti2=ProjI​[(fv2)−1​(−(κ2​pti2+σ2​ηti2);t,v¯ti2)],\displaystyle~~~~~v^{1}\_{t\_{i}}=\text{Proj}\_{I}\left[(f^{1}\_{v})^{-1}(-(\kappa^{1}p^{1}\_{t\_{i}}+\sigma^{1}\eta^{1}\_{t\_{i}});t,\bar{v}^{1}\_{t\_{i}})\right],v^{2}\_{t\_{i}}=\text{Proj}\_{I}\left[(f^{2}\_{v})^{-1}(-(\kappa^{2}p^{2}\_{t\_{i}}+\sigma^{2}\eta^{2}\_{t\_{i}});t,\bar{v}^{2}\_{t\_{i}})\right], |  |
|  |  |  |
| --- | --- | --- |
|  | ηti1=𝒩​𝒩3ϕ3​(ti,xti1,zti1,pti1),ηti2=𝒩​𝒩4ϕ4​(t,xti2,zti2,pti2),\displaystyle~~~~~\eta^{1}\_{t\_{i}}=\mathcal{NN}^{\phi\_{3}}\_{3}(t\_{i},x^{1}\_{t\_{i}},z^{1}\_{t\_{i}},p^{1}\_{t\_{i}}),~\eta^{2}\_{t\_{i}}=\mathcal{NN}^{\phi\_{4}}\_{4}(t,x^{2}\_{t\_{i}},z^{2}\_{t\_{i}},p^{2}\_{t\_{i}}), |  |
|  |  |  |
| --- | --- | --- |
|  | p01=𝒩​𝒩5ϕ5​(x01),p02=𝒩​𝒩6ϕ6​(x02),\displaystyle~~~~~p^{1}\_{0}=\mathcal{NN}^{\phi\_{5}}\_{5}(x^{1}\_{0}),~p^{2}\_{0}=\mathcal{NN}^{\phi\_{6}}\_{6}(x^{2}\_{0}), |  |

where Δ​Wtih=Wti+1h−Wtih\Delta W^{h}\_{t\_{i}}=W^{h}\_{t\_{i+1}}-W^{h}\_{t\_{i}}, λ>0\lambda>0 is the penalty parameter, and the expectations are computed by the average of the simulated paths. In other words, the loss function is the sum of expected squared loss of the terminal condition of the backward equations, and a penalty term for the difference between 𝔼​[vth]\mathbb{E}[v^{h}\_{t}] and v¯th\bar{v}^{h}\_{t}.

⋮\vdots⋮\vdots⋮\vdots⋮\vdotsttxt1x^{1}\_{t}zt1z^{1}\_{t}pt1p^{1}\_{t}H1(1)H^{(1)}\_{1}H32(1)H^{(1)}\_{32}H1(2)H^{(2)}\_{1}H32(2)H^{(2)}\_{32}ηt1\eta^{1}\_{t}InputHidden 1Hidden 2Ouput


Figure 1: Neural network for ηt1\eta^{1}\_{t} with a “4−32−32−14-32-32-1” structure.

In this study, we perform Monte-Carlo simulations for the system ([41](https://arxiv.org/html/2511.12292v1#S6.E41 "In 6.1 Neural Network Architectures ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")) with 10,00010,000 sample paths and M=100M=100 time steps. For each case, we train the neural network 1,0001,000 times. An Adam optimizer is applied to minimize the objective ([41](https://arxiv.org/html/2511.12292v1#S6.E41 "In 6.1 Neural Network Architectures ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")). The learning rate is set as 5×10−45\times 10^{-4}. To demonstrate the accuracy of the algorithm, under quadratic rewards, we use the non-constrained case as a benchmark and compute the relative error between the neural network approach and the ordinary differential equation (ODE) benchmark (Theorem [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), which is defined as

|  |  |  |
| --- | --- | --- |
|  | 14​M​∑i=0M−1∑h=12|𝒩​𝒩hϕh​(ti)−v¯tih,O​D​Emaxj∈{0,…,M−1}⁡|v¯tjh,O​D​E||+14​M​∑i=1M∑h=12|ztih,N​N−ztih,O​D​Emaxj∈{0,…,M−1}⁡|ztjh,O​D​E||,\displaystyle\frac{1}{4M}\sum\limits\_{i=0}^{M-1}\sum\limits\_{h=1}^{2}\left|\frac{\mathcal{NN}^{\phi\_{h}}\_{h}(t\_{i})-\bar{v}^{h,ODE}\_{t\_{i}}}{\max\limits\_{j\in\{0,\dots,M-1\}}\left|\bar{v}^{h,ODE}\_{t\_{j}}\right|}\right|+\frac{1}{4M}\sum\limits\_{i=1}^{M}\sum\limits\_{h=1}^{2}\left|\frac{z^{h,NN}\_{t\_{i}}-z^{h,ODE}\_{t\_{i}}}{\max\limits\_{j\in\{0,\dots,M-1\}}\left|z^{h,ODE}\_{t\_{j}}\right|}\right|, |  |

where the superscripts “ODE” and “NN” indicate that the values are generated by the ODE benchmark from Theorem [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market"), and by the neural network approach, respectively. The factor of 4 in the error definition accounts for averaging over the four functions (v¯t1,v¯t2,zt1,zt2\bar{v}^{1}\_{t},\bar{v}^{2}\_{t},z^{1}\_{t},z^{2}\_{t}). Table [3](https://arxiv.org/html/2511.12292v1#A6.T3 "Table 3 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market") in Appendix [F](https://arxiv.org/html/2511.12292v1#A6 "Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market") presents the relative errors under different choices of the penalty coefficient λ\lambda. Based on the result, we choose λ=10\lambda=10 for Cases 1, 4(b) and 4(c), and λ=1\lambda=1 for other cases to minimize the training errors. In practice, we recommend choosing λ\lambda from 1 to 10 to obtain the smallest computation errors.

Figure [2](https://arxiv.org/html/2511.12292v1#S6.F2 "Figure 2 ‣ 6.1 Neural Network Architectures ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") shows the loss curve for Case 1(a) with insurance constraint, illustrating that the loss function ([41](https://arxiv.org/html/2511.12292v1#S6.E41 "In 6.1 Neural Network Architectures ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")) decays rapidly to zero with the number of training iterations. The numerical values of the loss functions for all cases considered are provided in Tables [4](https://arxiv.org/html/2511.12292v1#A6.T4 "Table 4 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market") (without constraint) and [5](https://arxiv.org/html/2511.12292v1#A6.T5 "Table 5 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market") (with constraint) in Appendix [F](https://arxiv.org/html/2511.12292v1#A6 "Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market"). From the tables, we observe that both components of the training error, corresponding to the two summands in ([41](https://arxiv.org/html/2511.12292v1#S6.E41 "In 6.1 Neural Network Architectures ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")), are small, on the order of 10−310^{-3}. This demonstrates the accuracy of the proposed algorithm in satisfying the BSDE’s terminal condition and approximating the mean field term v¯h\bar{v}^{h}.

![Refer to caption](x1.png)


Figure 2: Loss curve for Case 1(a) with insurance constraints.

### 6.2 Equilibrium Wealth and Strategies

Figures [3](https://arxiv.org/html/2511.12292v1#S6.F3 "Figure 3 ‣ 6.2.1 The impact of 𝜎^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")-[9](https://arxiv.org/html/2511.12292v1#S6.F9 "Figure 9 ‣ 6.2.5 Impact of 𝑒^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") present the results for Cases 1-4, respectively. The equilibrium strategies 𝐯¯t=(v¯t1,v¯t2)\bar{{\bf v}}\_{t}=(\bar{v}^{1}\_{t},\bar{v}^{2}\_{t}), and the equilibrium wealth 𝐳t=(zt1,zt2){\bf z}\_{t}=(z^{1}\_{t},z^{2}\_{t}) are displayed in the left and right panels, respectively. In each figure, we distinguish the curves without constraint by solid line, and those with constraint by dashed line. The curve for Class 1 and Class 2 are plotted in blue and yellow respectively.
Table [6](https://arxiv.org/html/2511.12292v1#A6.T6 "Table 6 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market") supplements the figures by providing the numerical values of the equilibrium strategies of all cases for t=0t=0 and near the end of the planning horizon.

#### 6.2.1 The impact of σh\sigma^{h}

Figure [3](https://arxiv.org/html/2511.12292v1#S6.F3 "Figure 3 ‣ 6.2.1 The impact of 𝜎^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") depicts the effect of the volatility of the loss process on the equilibrium strategies. Figure [3(a)](https://arxiv.org/html/2511.12292v1#S6.F3.sf1 "In Figure 3 ‣ 6.2.1 The impact of 𝜎^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") shows that the equilibrium strategy increases with volatility, with the representative member from Class 2 (σ2=30%\sigma^{2}=30\%) purchasing more insurance than her counterpart in Class 1 (σ1=10%\sigma^{1}=10\%). Intuitively, when there is greater uncertainty about the severity of the loss, members tend to purchase more insurance to transfer the uncertainty to the insurance company. Consequently, with a higher insurance purchase and, therefore, higher premium payments, the equilibrium wealth of the representative member in Class 2 tends to be smaller than that of one in Class 1; see Figure [3(b)](https://arxiv.org/html/2511.12292v1#S6.F3.sf2 "In Figure 3 ‣ 6.2.1 The impact of 𝜎^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market").

![Refer to caption](x2.png)


(a) v¯h\bar{v}^{h} for Case 1(a)

![Refer to caption](x3.png)


(b) zhz^{h} for Case 1(a)

Figure 3: The equilibrium insurance strategies and wealth for representative members under Cases 1(a).

Examining the effect of the insurance constraint, we see that the constraint becomes binding for Class 1 near the end of the planning horizon. This restriction truncates the insurance strategy, leading members from Class 1 to ultimately forgo purchasing insurance. On the other hand, the constraint remains non-binding for Class 2, so their strategies are largely unchanged by the constraint. Nevertheless, small deviations do appear, stemming from the indirect influence of Class 1’s binding constraint through the sharing mechanism; see also Table [6](https://arxiv.org/html/2511.12292v1#A6.T6 "Table 6 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market"). Owing to the small deviations of the equilibrium strategies under the two scenarios, the effect of the insurance constraint on the equilibrium wealth is relatively small.

The impact of relative class sizes on the equilibrium strategies is illustrated in Table [6](https://arxiv.org/html/2511.12292v1#A6.T6 "Table 6 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market"). While the changes are not dramatic, we observe that members from both classes tend to reduce their insurance positions when the proportion of more risky members is smaller (Case 1(b), ω1=0.8,σ1=10%\omega^{1}=0.8,\sigma^{1}=10\%, ω2=0.2,σ2=30%\omega^{2}=0.2,\sigma^{2}=30\%), and increase their positions when the proportion of more risky members is higher (Case 1(c), ω1=0.2,σ1=10%\omega^{1}=0.2,\sigma^{1}=10\%, ω2=0.8,σ2=30%\omega^{2}=0.8,\sigma^{2}=30\%). Compared to Case 1(a), when insurance constraint is imposed, the initial equilibrium strategy v¯01\bar{v}^{1}\_{0} for Class 1 has been reduced by 2.20%2.20\% in Case 1(b), and increased by 1.94%1.94\% in Case 1(c). This can be explained by changes in the aggregate risk of the mutual as the composition of member riskiness varies. For instance, in Case 1(c), the greater presence of high-risk members incentivizes all members to take on larger insurance positions.

#### 6.2.2 The impact of γh\gamma^{h}

The effect of the parameter γh\gamma^{h}, h=1,2h=1,2, is depicted in Figure [4](https://arxiv.org/html/2511.12292v1#S6.F4 "Figure 4 ‣ 6.2.2 The impact of 𝛾^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market"). This parameter can serve as a measure of the risk aversion of the member. Specifically, when γh\gamma^{h} is high (resp. small), the member is more (resp. less) concerned about her absolute terminal wealth relative to its fluctuation, indicating that the member is less (resp. more) risk-averse. Clearly, members who are more risk-averse tend to purchase more insurance to transfer the risk to the MIC (see Class 11 (γ1=1\gamma^{1}=1) in Figure [4(a)](https://arxiv.org/html/2511.12292v1#S6.F4.sf1 "In Figure 4 ‣ 6.2.2 The impact of 𝛾^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")). This results in a lower equilibrium wealth as opposed to Class 2 (γ2=1.6\gamma^{2}=1.6), since (i) members of Class 11 are less aware of the dollar amount of their terminal wealth, and (ii) more premiums are paid due to higher insurance demand. Specifically, Figure [4(a)](https://arxiv.org/html/2511.12292v1#S6.F4.sf1 "In Figure 4 ‣ 6.2.2 The impact of 𝛾^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") shows that the risk-averse member from Class 1 purchases insurance, in contrast to the short position taken by the risk-seeking member from Class 2 when no insurance constraint is imposed. Due to the difference in the risk-aversion and the insurance strategies, the representative member from Class 2 has a higher equilibrium wealth than that from Class 1.

![Refer to caption](x4.png)


(a) v¯h\bar{v}^{h} for Case 2(a)

![Refer to caption](x5.png)


(b) zhz^{h} for Case 2(a)

Figure 4: The equilibrium insurance strategies and wealth for representative members under Case 2(a).

Imposing the insurance constraint has a prominent effect on the equilibrium strategy of Class 2, since it restricts members from taking a short position. Consequently, it reduces the difference in the insurance strategies and the wealth gap between the two classes. Despite the constraint is unbinding for Class 1, the drastic change in the insurance strategy of Class 2 under the constraint induces an increase in the insurance strategy of Class 1.

The impact of the membership class composition can be assessed by comparing Cases 2(b) and 2(c) with Case 2(a) in Table [6](https://arxiv.org/html/2511.12292v1#A6.T6 "Table 6 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market"). When the proportion of risk-averse members is high (Case 2(b), ω1=0.8\omega^{1}=0.8), members in both classes tend to purchase more insurance. Compared to Case 2(a), when the insurance constraint is imposed, the initial equilibrium strategy has increased by 2.03% for Class 1, and 2.73% for Class 2. The reasons are twofold. First, the overall risk awareness of the mutual has increased, driven by the larger share of risk-averse members. Second, the higher premium income contributed by Class 1 members leads to greater shared surplus, from which the more risk-seeking Class 2 members also benefit. This enhanced surplus distribution boosts their ability to afford more coverage. Conversely, the insurance strategies for members from both classes decrease when there is a smaller proportion of risk-averse members (Case 2(c), ω1=0.2\omega^{1}=0.2).

#### 6.2.3 The impact of κh\kappa^{h}

Figures [5](https://arxiv.org/html/2511.12292v1#S6.F5 "Figure 5 ‣ 6.2.3 The impact of 𝜅^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")-[6](https://arxiv.org/html/2511.12292v1#S6.F6 "Figure 6 ‣ 6.2.3 The impact of 𝜅^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") manifest the scenario under different κh\kappa^{h}, which is proportional to the safety loading θh\theta^{h} and the rate of loss μh\mu^{h}. In the study, members in Class 2 (κ2=0.5)\kappa^{2}=0.5) are charged with a higher cost of insurance than their Class 1 (κ1=0.1\kappa^{1}=0.1) counterparts, which can be due to higher rate of loss and safety loading of the policy.

![Refer to caption](x6.png)


(a) v¯h\bar{v}^{h} for Case 3(a)

![Refer to caption](x7.png)


(b) zhz^{h} for Case 3(a)

Figure 5: Equilibrium insurance strategies and wealth for representative members under Case 3(a).

Figures [5](https://arxiv.org/html/2511.12292v1#S6.F5 "Figure 5 ‣ 6.2.3 The impact of 𝜅^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")–[6](https://arxiv.org/html/2511.12292v1#S6.F6 "Figure 6 ‣ 6.2.3 The impact of 𝜅^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") reveal that variations in κh\kappa^{h} substantially influence how the equilibrium insurance strategy evolves over time. With a higher κh\kappa^{h} (Class 2 in Cases 3(a)-(b)), the equilibrium strategy tends to decay at a faster rate. Consequently, the relative size of the equilibrium wealth changes over time and is influenced by other parameters such as γh\gamma^{h}. When γh=1.6\gamma^{h}=1.6 (Case 3(a)), indicating a relatively low level of risk aversion, a higher κh\kappa^{h} (see Class 2 in Figure [5(a)](https://arxiv.org/html/2511.12292v1#S6.F5.sf1 "In Figure 5 ‣ 6.2.3 The impact of 𝜅^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")) leads to a reduction in the insurance purchases of members. The reason is straightforward: members are less inclined to buy overpriced insurance. Consequently, this lowers the equilibrium wealth for members in Class 2. The higher premium rate also lowers the equilibrium wealth for members in Class 2 compared to Class 1 when insurance constraint is imposed. In addition, for Class 2, the insurance constraint binds for roughly half of the planning horizon. In the unconstrained case, κh\kappa^{h} decays rapidly over time, whereas under the constraint, this decline forces v¯t2=0\bar{v}^{2}\_{t}=0. Consequently, the equilibrium insurance strategies differ substantially between the constrained and unconstrained settings for Class 2.

In contrast, when the level of risk aversion is relatively high (Case 3(b), γh=1\gamma^{h}=1), a higher κh\kappa^{h} does not necessarily lower the initial insurance demand. As shown in Figure [6(a)](https://arxiv.org/html/2511.12292v1#S6.F6.sf1 "In Figure 6 ‣ 6.2.3 The impact of 𝜅^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market"), members in Class 2 purchase more insurance than their Class 1 counterparts until the end of the planning horizon. This can be explained as follows. Given that the net income remains unchanged, an increase in κh\kappa^{h} may arise from both a higher μh\mu^{h} and l~h\tilde{l}^{h}. In this case, members face a greater expected loss intensity, which encourages them to purchase more insurance despite the higher premium cost. Moreover, when risk aversion is high, members in Class 2 place greater emphasis on mitigating wealth volatility within their class, resulting in higher insurance demand even at the expense of slower wealth accumulation. This pattern is reflected in Figure [6(b)](https://arxiv.org/html/2511.12292v1#S6.F6.sf2 "In Figure 6 ‣ 6.2.3 The impact of 𝜅^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market"), where their wealth growth is slower than their Class 1 counterpart. Owing to this and the higher time sensitivity of the insurance strategy under higher κh\kappa^{h}, their focus gradually shifts toward maximizing terminal wealth, leading to reduced insurance purchases when approaching TT.

![Refer to caption](x8.png)


(a) v¯h\bar{v}^{h} for Case 3(b)

![Refer to caption](x9.png)


(b) zhz^{h} for Case 3(b)

Figure 6: (continued) Equilibrium insurance strategies and wealth for representative members under Case 3(b).

#### 6.2.4 The impact of l~h−μh\tilde{l}^{h}-\mu^{h}

Figure [7](https://arxiv.org/html/2511.12292v1#S6.F7 "Figure 7 ‣ 6.2.4 The impact of 𝑙̃^ℎ-𝜇^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") illustrates the effect of the sharing-independent net income rate l~h−μh\tilde{l}^{h}-\mu^{h}, that is, the net income prior to any surplus or deficit transfers under the MIC, in Case 4(a). It is clear that the representative member from Class 2 (l~2−μ2=0.1)(\tilde{l}^{2}-\mu^{2}=0.1), who earns a higher net income rate than her Class 1 (l~1−μ1=0.02\tilde{l}^{1}-\mu^{1}=0.02) counterpart, tends to purchase more insurance due to the higher purchasing power. This high income rate also offsets the higher premium rate, leading to a higher equilibrium wealth for the member in Class 2.

![Refer to caption](x10.png)


(a) v¯h\bar{v}^{h} for Case 4(a)

![Refer to caption](x11.png)


(b) zhz^{h} for Case 4(a)

Figure 7: Equilibrium insurance strategies and wealth for representative members under Case 4(a).

#### 6.2.5 Impact of ehe^{h}

The effect of the membership fee rate ehe^{h} can be examined by comparing Cases 4(b)-4(c) with Case 4(a). In particular, under the proportional relation ([40](https://arxiv.org/html/2511.12292v1#S6.E40 "In 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")), a change in the membership fee rate would also alter the sharing proportion πh\pi^{h} and the management fee rate dehd\_{e}^{h}.

In Case 4(b) (Figure [8](https://arxiv.org/html/2511.12292v1#S6.F8 "Figure 8 ‣ 6.2.5 Impact of 𝑒^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")), the increased sharing proportion  π1=1.8182\pi^{1}=1.8182 for Class 1 compensate the income advantage of Class 2. As a result, the wealth of Class 1 exceeds that of Class 2, accompanied by a higher insurance position.

![Refer to caption](x12.png)


(a) v¯h\bar{v}^{h} for Case 4(b)

![Refer to caption](x13.png)


(b) zhz^{h} for Case 4(b)

Figure 8: Equilibrium insurance strategies and wealth for representative members under Case 4(b).

In Case 4(c) (Figure [9](https://arxiv.org/html/2511.12292v1#S6.F9 "Figure 9 ‣ 6.2.5 Impact of 𝑒^ℎ ‣ 6.2 Equilibrium Wealth and Strategies ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")), with e1=0.01e^{1}=0.01 and e2=0.1e^{2}=0.1, members from Class 1 face a reduction in the shared surplus, leading to lower equilibrium wealth and a reduced insurance strategy compared to Case 4(a). In contrast, members in Class 2 receive both higher incomes and surplus from the MIC then her counterpart in Class 1, leading to an even higher insurance strategy and equilibrium wealth compared to Case 4(a).

![Refer to caption](x14.png)


(a) v¯h\bar{v}^{h} for Case 4(c)

![Refer to caption](x15.png)


(b) zhz^{h} for Case 4(c)

Figure 9: Equilibrium insurance strategies and wealth for representative members under Case 4(c).

#### 6.2.6 Behavior with respect to time

Lastly, in all cases, we observe that the equilibrium insurance strategies decrease with time. The reasons are twofold.
First, the value of the protection provided by insurance often declines with time, as the window for significant losses to occur in the future has shortened. Consequently, the uncertainty of future losses decreases, leading to a lower demand for coverage. Second, as the length of the planning horizon shortens, members would prioritize maximizing terminal wealth over long-term risk management, further contributing to the reduction in insurance strategies. The time-decaying nature of indemnity functions is also documented in the actuarial literature, see e.g. \@BBOPcite\@BAP\@BBNzeng2011optimal\@BBCP, \@BBOPcite\@BAP\@BBNli2012optimal\@BBCP, and \@BBOPcite\@BAP\@BBNyi2013robust\@BBCP.

### 6.3 General Mixture of Reward Functions

The second study is based on an alternative class of reward functions. Specifically, we define

|  |  |  |
| --- | --- | --- |
|  | fh​(t,x,z,v,v¯):={γh1−γh​(ah​xγh+bh)1−γh−γh​(bh)1−γh1−γh−Qh2​(x−Bh)2−Ph2​(v−Rh​v¯)2,if ​x≥0;ah​(bh)−γh​x−Qh2​(x−Bh)2−Ph2​(v−Rh​v¯)2,if ​x<0,f^{h}(t,x,z,v,\bar{v}):=\begin{dcases}\frac{\gamma^{h}}{1-\gamma^{h}}\left(\frac{a^{h}x}{\gamma^{h}}+b^{h}\right)^{1-\gamma^{h}}-\frac{\gamma^{h}(b^{h})^{1-\gamma^{h}}}{1-\gamma^{h}}-\frac{Q^{h}}{2}(x-B^{h})^{2}-\frac{P^{h}}{2}(v-R^{h}\bar{v})^{2},\\ \qquad\qquad\qquad\qquad\qquad\qquad\qquad\text{if }x\geq 0;\\ a^{h}(b^{h})^{-\gamma^{h}}x-\frac{Q^{h}}{2}(x-B^{h})^{2}-\frac{P^{h}}{2}(v-R^{h}\bar{v})^{2},\quad\text{if }x<0,\end{dcases} |  |

and

|  |  |  |
| --- | --- | --- |
|  | gh​(x,z):={γh1−γh​(ah​xγh+bh)1−γh−γh​(bh)1−γh1−γh−Qh2​(x−Bh)2,if ​x≥0;ah​(bh)−γh​x−Qh2​(x−Bh)2,if ​x<0.g^{h}(x,z):=\begin{dcases}\frac{\gamma^{h}}{1-\gamma^{h}}\left(\frac{a^{h}x}{\gamma^{h}}+b^{h}\right)^{1-\gamma^{h}}-\frac{\gamma^{h}(b^{h})^{1-\gamma^{h}}}{1-\gamma^{h}}-\frac{Q^{h}}{2}(x-B^{h})^{2},&\text{if }x\geq 0;\\ a^{h}(b^{h})^{-\gamma^{h}}x-\frac{Q^{h}}{2}(x-B^{h})^{2},&\text{if }x<0.\end{dcases} |  |

These reward functions combine a hyperbolic absolute risk aversion (HARA) utility with a penalty relative to a specified benchmark. The parameter γh>0,γh≠1\gamma^{h}>0,\gamma^{h}\neq 1 represents the degree of relative risk aversion, while ah>0a^{h}>0 scales the utility function and governs its curvature. The parameter bh>0b^{h}>0 both shifts wealth to ensure positivity of the argument and governs how rapidly absolute risk aversion declines as wealth increases. Finally, Bh>0B^{h}>0 specifies a benchmark wealth level, penalizing deviations from the desired target. It is clear that the above choice of functions verifies Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") and [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), with α1X=α1g=Qh\alpha^{X}\_{1}=\alpha^{g}\_{1}=Q^{h}, α2X=α2g=0\alpha^{X}\_{2}=\alpha^{g}\_{2}=0, LX=Lg=Qh+(ah)2(bh)1+γhL^{X}=L^{g}=Q^{h}+\frac{(a^{h})^{2}}{(b^{h})^{1+\gamma^{h}}}. Hence, by ([21](https://arxiv.org/html/2511.12292v1#S4.E21 "In 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")), Assumption [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") would be fulfilled provided that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qh>‖𝐌‖2​(Qh+(ah)2(bh)1+γh).Q^{h}>\|{\bf M}\|\_{2}\left(Q^{h}+\frac{(a^{h})^{2}}{(b^{h})^{1+\gamma^{h}}}\right). |  | (42) |

In this experiment, we consider H=2H=2 and choose the same parameters as in base scenario ([39](https://arxiv.org/html/2511.12292v1#S6.E39 "In 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")), except

|  |  |  |
| --- | --- | --- |
|  | γ1=0.5,γ2=3.0,a1=a2=1.0,b1=b2=5.0,B1=B2=2.5,κ1=κ2=0.08,\displaystyle\gamma^{1}=0.5,\gamma^{2}=3.0,\ a^{1}=a^{2}=1.0,\ b^{1}=b^{2}=5.0,\ B^{1}=B^{2}=2.5,\ \kappa^{1}=\kappa^{2}=0.08, |  |

so that ([42](https://arxiv.org/html/2511.12292v1#S6.E42 "In 6.3 General Mixture of Reward Functions ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")) is fulfilled. We also define πh\pi^{h} (and thus lhl^{h}) using the same formula as in ([40](https://arxiv.org/html/2511.12292v1#S6.E40 "In 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")). We refer to this study as Case 5.

The last row of Table [5](https://arxiv.org/html/2511.12292v1#A6.T5 "Table 5 ‣ Appendix F Supplementary Tables for Section 6 ‣ Mean Field Analysis of Mutual Insurance Market") presents the training errors corresponding to the selected parameters and the reward functions in Case 5 using the training scheme ([41](https://arxiv.org/html/2511.12292v1#S6.E41 "In 6.1 Neural Network Architectures ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")). The results show that the training errors remain comparable, and even improved, to the quadratic case, while the training time increases modestly due to the more complex derivatives.

Figure [10](https://arxiv.org/html/2511.12292v1#S6.F10 "Figure 10 ‣ 6.3 General Mixture of Reward Functions ‣ 6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market") illustrates the mean field equilibrium insurance strategies and the corresponding wealth levels of members in the two classes under different choices of the risk aversion parameter γh\gamma^{h}, where a higher value indicates greater risk aversion. As expected, members in Class 2, with a higher risk aversion parameter γ2=3\gamma^{2}=3, tend to purchase more insurance coverage than their counterparts in Class 1 (γ1=0.5\gamma^{1}=0.5). Consequently, Class 1 members attain slightly higher equilibrium wealth due to lower premium payments. Notably, the imposed constraints are non-binding in this case, resulting in identical outcomes for the constrained and unconstrained settings.

![Refer to caption](x16.png)


(a) v¯h\bar{v}^{h} for Case 5

![Refer to caption](x17.png)


(b) zhz^{h} for Case 5

Figure 10: The equilibrium insurance strategies and wealth for representative members under Cases 5.

## 7 Concluding Remarks

In this article, we formulated a dynamic optimal insurance problem for a mutual insurance company within an extended mean field game framework. The optimal insurance strategies are characterized by a system of mean field forward-backward stochastic differential equations (MF-FBSDEs), where the global existence and uniqueness of solutions were established using the continuation method. To numerically solve the MF-FBSDEs and determine the optimal strategies, we proposed a deep BSDE approach.

This work opens several avenues for future research. First, incorporating a jump-diffusion setting could better capture the stochastic behavior of claim arrivals. Second, relaxing the separability of the objective function, as assumed in Assumption [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), would broaden the model’s applicability. Additionally, analogizing the mutual insurance company sharing mechanisms with those in decentralized insurance, this extended mean field game framework could be adapted to model optimal decision-making in decentralized insurance pools in future studies.

## Acknowledgments

Bohan Li is supported by the National Natural Science Foundation of China under grant No.12501661. Wenyuan Li gratefully acknowledges a start-up grant from the University of Hong Kong. Kenneth Ng acknowledges the financial support from the Univeristy of Illinois Urbana-Champaign, the Chinese University of Hong Kong, and the start-up fund from the Ohio State University. Phillip Yam acknowledges the financial supports from HKGRF-14301321 with the project title “General Theory for Infinite Dimensional Stochastic Control: Mean Field and Some Classical Problem”, HKGRF-14300123 with the project title “Well-posedness of Some Poisson-driven Mean Field Learning Models and their Applications”, and HKGRF-14300025 with the project title “A Generic Theory for Stochastic Control against Fractional Brownian Motions”. The work described in this article was also supported by a grant from the Germany/Hong Kong Joint Research Scheme sponsored by the Research Grants Council of Hong Kong and the German Academic Exchange Service of Germany (Reference No. G-CUHK411/23). He also thanks The University of Texas at Dallas for the kind invitation to be a Visiting Professor in Naveen Jindal School of Management.

## Appendix A Auxiliary Lemmas

In this section, we provide some auxiliary lemmas that are useful in constructing the optimal insurance strategies and establishing the well-posedness of the MF-FBSDE ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")). The first lemma is an elementary result in convex analysis.

###### Lemma A.1.

Let A⊂ℝnA\subset\mathbb{R}^{n} be a non-empty, closed, convex set. For any x∈ℝnx\in\mathbb{R}^{n}, there exists an x∗∈Ax^{\*}\in A such that |x−x∗|=minx′∈A⁡|x−x′||x-x^{\*}|=\min\_{x^{\prime}\in A}|x-x^{\prime}|. In addition, x∗x^{\*} is characterized by the following inequality:

|  |  |  |
| --- | --- | --- |
|  | ⟨y−x∗,x−x∗⟩≤0\langle y-x^{\*},x-x^{\*}\rangle\leq 0 |  |

for any y∈Ay\in A.

The next result is used in establishing the unique existence of solution of ([15](https://arxiv.org/html/2511.12292v1#S3.E15 "In 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")), which can be verified by a straightforward manner.

###### Lemma A.2.

Let a,b,u,l∈ℝa,b,u,l\in\mathbb{R} with u<lu<l. Denote by ap=Proj[l,u]​(a)a\_{p}=\text{Proj}\_{[l,u]}(a) and bp=Proj[l,u]​(b)b\_{p}=\text{Proj}\_{[l,u]}(b). For any non-decreasing function φ:ℝ→ℝ\varphi:\mathbb{R}\to\mathbb{R}, it holds that

|  |  |  |
| --- | --- | --- |
|  | (ap−bp)​(φ​(a)−φ​(b))≥(ap−bp)​(φ​(ap)−φ​(bp)).(a\_{p}-b\_{p})(\varphi(a)-\varphi(b))\geq(a\_{p}-b\_{p})(\varphi(a\_{p})-\varphi(b\_{p})). |  |

In the next lemma, we demonstrate a simple inequality used in establishing the existence of solution of the MF-FBSDE under the general setup in Theorem [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), and also under the quadratic reward in Assumption [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmassumption1 "Assumption 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market").

###### Lemma A.3.

Let 𝐗{\bf X} be a square integrable ℝd\mathbb{R}^{d}-valued random vector, and 𝐙:=𝔼​[𝐗]{\bf Z}:=\mathbb{E}[{\bf X}]. Then, for any d×dd\times d matrix ℳ\mathcal{M}, and any positive definite matrix 𝒬\mathcal{Q} such that λmin​(𝒬−ℳ)>0\lambda\_{\min}(\mathcal{Q}-\mathcal{M})>0, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨𝐗,𝒬​𝐗⟩]−⟨ℳ​𝐙,𝐙⟩>min⁡{λmin​(𝒬),λmin​(𝒬−ℳ)}​𝔼​[|𝐗|2].\mathbb{E}[\langle{\bf X},\mathcal{Q}{\bf X}\rangle]-\langle\mathcal{M}{\bf Z},{\bf Z}\rangle>\min\left\{\lambda\_{\min}(\mathcal{Q}),\lambda\_{\min}(\mathcal{Q}-\mathcal{M})\right\}\mathbb{E}[|{\bf X}|^{2}]. |  |

###### Proof.

Using the identity 𝔼​[⟨𝐗,𝒬​𝐗⟩]=𝔼​[⟨(𝐗−𝐙),𝒬​(𝐗−𝐙)⟩]+⟨𝐙,𝒬​𝐙⟩\mathbb{E}[\langle{\bf X},\mathcal{Q}{\bf X}\rangle]=\mathbb{E}[\langle({\bf X}-{\bf Z}),\mathcal{Q}({\bf X}-{\bf Z})\rangle]+\langle{\bf Z},\mathcal{Q}{\bf Z}\rangle, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[⟨𝐗,𝒬​𝐗⟩]−⟨ℳ​𝐙,𝐙⟩\displaystyle\mathbb{E}[\langle{\bf X},\mathcal{Q}{\bf X}\rangle]-\langle\mathcal{M}{\bf Z},{\bf Z}\rangle | =𝔼​[⟨(𝐗−𝐙),𝒬​(𝐗−𝐙)⟩]+⟨𝐙,(𝒬−ℳ)​𝐙⟩\displaystyle=\mathbb{E}[\langle({\bf X}-{\bf Z}),\mathcal{Q}({\bf X}-{\bf Z})\rangle]+\langle{\bf Z},(\mathcal{Q}-\mathcal{M}){\bf Z}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝔼​[⟨(𝐗−𝐙),𝒬​(𝐗−𝐙)⟩]+λmin​(𝒬−ℳ)​|𝐙|2\displaystyle\geq\mathbb{E}[\langle({\bf X}-{\bf Z}),\mathcal{Q}({\bf X}-{\bf Z})\rangle]+\lambda\_{\min}(\mathcal{Q}-\mathcal{M})|{\bf Z}|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥λmin​(𝒬)​𝔼​[|𝐗−𝐙|2]+λmin​(𝒬−ℳ)​|𝐙|2\displaystyle\geq\lambda\_{\min}(\mathcal{Q})\mathbb{E}[|{\bf X}-{\bf Z}|^{2}]+\lambda\_{\min}(\mathcal{Q}-\mathcal{M})|{\bf Z}|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λmin​(𝒬)​𝔼​[|𝐗|2]+(λmin​(𝒬−ℳ)−λmin​(𝒬))​|𝐙|2.\displaystyle=\lambda\_{\min}(\mathcal{Q})\mathbb{E}[|{\bf X}|^{2}]+\left(\lambda\_{\min}(\mathcal{Q}-\mathcal{M})-\lambda\_{\min}(\mathcal{Q})\right)|{\bf Z}|^{2}. |  |

If λmin​(𝒬−ℳ)>λmin​(𝒬)\lambda\_{\min}(\mathcal{Q}-\mathcal{M})>\lambda\_{\min}(\mathcal{Q}), then we immediately have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨𝐗,𝒬​𝐗⟩]−⟨ℳ​𝐙,𝐙⟩≥λmin​(𝒬)​𝔼​[|𝐗|2].\mathbb{E}[\langle{\bf X},\mathcal{Q}{\bf X}\rangle]-\langle\mathcal{M}{\bf Z},{\bf Z}\rangle\geq\lambda\_{\min}(\mathcal{Q})\mathbb{E}[|{\bf X}|^{2}]. |  |

Otherwise, by Jensen’s inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[⟨𝐗,𝒬​𝐗⟩]−⟨ℳ​𝐙,𝐙⟩\displaystyle\ \ \ \ \mathbb{E}[\langle{\bf X},\mathcal{Q}{\bf X}\rangle]-\langle\mathcal{M}{\bf Z},{\bf Z}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | ≥λmin​(𝒬−ℳ)​𝔼​[|𝐗|2]+(λmin​(𝒬)−λmin​(𝒬−ℳ))​(𝔼​[|𝐗|2]−|𝐙|2)\displaystyle\geq\lambda\_{\min}(\mathcal{Q}-\mathcal{M})\mathbb{E}[|{\bf X}|^{2}]+\left(\lambda\_{\min}(\mathcal{Q})-\lambda\_{\min}(\mathcal{Q}-\mathcal{M})\right)\left(\mathbb{E}[|{\bf X}|^{2}]-|{\bf Z}|^{2}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≥λmin​(𝒬−ℳ)​𝔼​[|𝐗|2].\displaystyle\geq\lambda\_{\min}(\mathcal{Q}-\mathcal{M})\mathbb{E}[|{\bf X}|^{2}]. |  |

The result then follows by combining the two cases.
∎

## Appendix B Proofs and Extensions for Section [2](https://arxiv.org/html/2511.12292v1#S2 "2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")

This section contains the proof of Theorem [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market") and discusses an extension of the model incorporating member survivorship.

### B.1 Proof of Theorem [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")

This section is devoted to proving Theorem [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"). The entire proof is decomposed into four steps. To begin, for each h∈[H]h\in[H] and i∈[Nh]i\in[N^{h}], let vi,hv^{i,h} be the optimal strategy obtained in Problems [2](https://arxiv.org/html/2511.12292v1#Thmproblem2 "Problem 2. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")-[3](https://arxiv.org/html/2511.12292v1#Thmproblem3 "Problem 3. ‣ 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), except that the Brownian motion WhW^{h} in the wealth process is replaced by Wi,hW^{i,h}. We also let y^i,h\hat{y}^{i,h} and x^i,h\hat{x}^{i,h} be the dynamics ([3](https://arxiv.org/html/2511.12292v1#S2.E3 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) under the NN-player game and the mean field dynamics ([5](https://arxiv.org/html/2511.12292v1#S2.E5 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) when the strategy vi,hv^{i,h} is taken, respectively. Since the Brownian motions Wi,hW^{i,h} and Wj,hW^{j,h} are independent for i≠ji\neq j, the controls vi,hv^{i,h} and vj,hv^{j,h} are independent and identically distributed (i.i.d.), so does the associated wealth processes x^i,h\hat{x}^{i,h} and x^j,h\hat{x}^{j,h}. However, y^i,h\hat{y}^{i,h} and y^j,h\hat{y}^{j,h} are in general dependent due to the presence of the idiosyncratic component.

The first result manifests that the difference between y^i,h\hat{y}^{i,h} and x^i,h\hat{x}^{i,h} decreases with the class sizes in the order of 1/21/2.

###### Lemma B.1.

For any t∈[0,T]t\in[0,T], h∈[H]h\in[H] and i∈[Nh]i\in[N^{h}], we have

|  |  |  |
| --- | --- | --- |
|  | suph∈[H]supi∈[Nh]𝔼​[sups≤t|x^si,h−y^si,h|2]=∑k=1HO​(1Nk).\sup\_{h\in[H]}\sup\_{i\in[N^{h}]}\mathbb{E}\left[\sup\_{s\leq t}\left|\hat{x}^{i,h}\_{s}-\hat{y}^{i,h}\_{s}\right|^{2}\right]=\sum\_{k=1}^{H}O\left(\frac{1}{N^{k}}\right). |  |

###### Proof.

By ([3](https://arxiv.org/html/2511.12292v1#S2.E3 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) and ([5](https://arxiv.org/html/2511.12292v1#S2.E5 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | x^ti,h−y^ti,h=\displaystyle\hat{x}^{i,h}\_{t}-\hat{y}^{i,h}\_{t}= | ∫0t(r​(x^si,h−y^si,h)+πh​∑k=1Hωk​(κk−dk)​∑j=1Nk(𝔼​[vs1,k]−vsj,k)Nk)​𝑑s\displaystyle\ \int\_{0}^{t}\left(r\left(\hat{x}^{i,h}\_{s}-\hat{y}^{i,h}\_{s}\right)+\pi^{h}\sum\_{k=1}^{H}\omega^{k}(\kappa^{k}-d^{k})\frac{\sum\_{j=1}^{N^{k}}\left(\mathbb{E}[v^{1,k}\_{s}]-v^{j,k}\_{s}\right)}{N^{k}}\right)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0tπh​∑k=1Hσk​ωkNk​∑j=1Nkvsj,k​d​Wsj,k.\displaystyle\ -\int\_{0}^{t}\pi^{h}\sum\_{k=1}^{H}\frac{\sigma^{k}\omega^{k}}{N^{k}}\sum\_{j=1}^{N^{k}}v^{j,k}\_{s}dW^{j,k}\_{s}. |  |

Hence, there exists K>0K>0 independent of (Nk)k=1H(N^{k})\_{k=1}^{H} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sups≤t|x^si,h−y^si,h|2]\displaystyle\ \mathbb{E}\left[\sup\_{s\leq t}\left|\hat{x}^{i,h}\_{s}-\hat{y}^{i,h}\_{s}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | K​∫0t𝔼​[|x^si,h−y^si,h|2]​𝑑s+K​∑k=1H∫0t𝔼​[(1Nk​∑j=1Nk(𝔼​[vs1,k]−vsj,k))2]​𝑑s\displaystyle\ K\int\_{0}^{t}\mathbb{E}\left[\left|\hat{x}^{i,h}\_{s}-\hat{y}^{i,h}\_{s}\right|^{2}\right]ds+K\sum\_{k=1}^{H}\int\_{0}^{t}\mathbb{E}\left[\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\left(\mathbb{E}[v^{1,k}\_{s}]-v^{j,k}\_{s}\right)\right)^{2}\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +K​∑k=1H𝔼​[sups≤t(1Nk​∑j=1Nk∫0svlj,k​𝑑Wlj,k)2].\displaystyle\ +K\sum\_{k=1}^{H}\mathbb{E}\left[\sup\_{s\leq t}\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\int\_{0}^{s}v^{j,k}\_{l}dW^{j,k}\_{l}\right)^{2}\right]. |  |

Since vj,kv^{j,k} and vi,kv^{i,k} are i.i.d. for i≠ji\neq j, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0t𝔼​[(1Nk​∑j=1Nk(𝔼​[vs1,k]−vsj,k))2]​𝑑s\displaystyle\int\_{0}^{t}\mathbb{E}\left[\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\left(\mathbb{E}[v^{1,k}\_{s}]-v^{j,k}\_{s}\right)\right)^{2}\right]ds | =1(Nk)2​∫0t∑j=1Nk𝔼​[(𝔼​[vs1,k]−vsj,k)2]​d​s=O​(1Nk),\displaystyle=\frac{1}{(N^{k})^{2}}\int\_{0}^{t}\sum\_{j=1}^{N^{k}}\mathbb{E}\left[\left(\mathbb{E}[v^{1,k}\_{s}]-v^{j,k}\_{s}\right)^{2}\right]ds=O\left(\frac{1}{N^{k}}\right), |  |

as Nk→∞N^{k}\to\infty. Similarly, by the Burkholder-Davis-Gundy inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sups≤t(1Nk​∑j=1Nk∫0svlj,k​𝑑Wlj,k)2]​d​s\displaystyle\mathbb{E}\left[\sup\_{s\leq t}\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\int\_{0}^{s}v^{j,k}\_{l}dW^{j,k}\_{l}\right)^{2}\right]ds | ≤1Nk​𝔼​[∫0t(vs1,k)2​𝑑s]=O​(1Nk).\displaystyle\leq\frac{1}{N^{k}}\mathbb{E}\left[\int\_{0}^{t}\left(v^{1,k}\_{s}\right)^{2}ds\right]=O\left(\frac{1}{N^{k}}\right). |  |

Therefore, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sups≤t|x^si,h−y^si,h|2]≤K​∫0t𝔼​[supl≤s|x^li,h−y^li,h|2]​𝑑s+∑k=1HO​(1Nk),\displaystyle\mathbb{E}\left[\sup\_{s\leq t}\left|\hat{x}^{i,h}\_{s}-\hat{y}^{i,h}\_{s}\right|^{2}\right]\leq K\int\_{0}^{t}\mathbb{E}\left[\sup\_{l\leq s}\left|\hat{x}^{i,h}\_{l}-\hat{y}^{i,h}\_{l}\right|^{2}\right]ds+\sum\_{k=1}^{H}O\left(\frac{1}{N^{k}}\right), |  |

and the result follows from Grönwall’s inequality.
∎

The next result depicts that the discrepancy between the objective function under the NN-player game, and the mean field objective function under the mean field optimal strategy, exhibits a square-root decay with respect to the class sizes.

###### Lemma B.2.

For h∈[H]h\in[H] and i∈[Nh]i\in[N^{h}], we have

|  |  |  |
| --- | --- | --- |
|  | |𝒥i,h​(vi,h;𝐲^−i,h,𝐯−i,h)−Ji,h​(vi,h;zh,v¯h)|=∑k=1HO​(1Nk).\left|\mathcal{J}^{i,h}\left(v^{i,h};\hat{{\bf y}}^{-i,h},{\bf v}^{-i,h}\right)-J^{i,h}\left(v^{i,h};z^{h},\bar{v}^{h}\right)\right|=\sum\_{k=1}^{H}O\left(\frac{1}{\sqrt{N^{k}}}\right). |  |

###### Proof.

By ([4](https://arxiv.org/html/2511.12292v1#S2.E4 "In 2.1 Preliminaries and the 𝑁-Player Problem ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")), ([6](https://arxiv.org/html/2511.12292v1#S2.E6 "In 2.2 Mean Field Game Formulation ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market")) and Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |𝒥i,h(vi,h;𝐲^−i,h,𝐯−i,h)−Ji,h(vi,h;𝐳],v¯h)|\displaystyle\ \left|\mathcal{J}^{i,h}\left(v^{i,h};\hat{{\bf y}}^{-i,h},{\bf v}^{-i,h}\right)-J^{i,h}\left(v^{i,h};{\bf z]},\bar{v}^{h}\right)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​[∫0T|fh​(t,y^ti,h,∑j≠iNhy^tj,hNh−1,vti,h,∑j≠iNhvtj,hNh−1)−fh​(t,x^ti,h,zth,vti,h,v¯th)|​𝑑t]\displaystyle\ \mathbb{E}\left[\int\_{0}^{T}\left|f^{h}\left(t,\hat{y}^{i,h}\_{t},\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{t}}{N^{h}-1},v^{i,h}\_{t},\frac{\sum\_{j\neq i}^{N^{h}}v^{j,h}\_{t}}{N^{h}-1}\right)-f^{h}(t,\hat{x}^{i,h}\_{t},z^{h}\_{t},v^{i,h}\_{t},\bar{v}^{h}\_{t})\right|dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[|gh​(y^ti,h,∑j≠iNhy^Tj,hNh−1)−gh​(xTi,h,zTh)|]\displaystyle\ +\mathbb{E}\left[\left|g^{h}\left(\hat{y}^{i,h}\_{t},\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{T}}{N^{h}-1}\right)-g^{h}(x^{i,h}\_{T},z^{h}\_{T})\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | L𝔼[∫0T(1+|y^ti,h|+|x^ti,h|+|∑j≠iNhy^tj,hNh−1|+|zth|+2|vti,h|+|∑j≠iNhv^tj,hNh−1|+|v¯th|)\displaystyle\ L\mathbb{E}\Bigg[\int\_{0}^{T}\left(1+|\hat{y}^{i,h}\_{t}|+|\hat{x}^{i,h}\_{t}|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{t}}{N^{h}-1}\right|+|z^{h}\_{t}|+2|v^{i,h}\_{t}|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{v}^{j,h}\_{t}}{N^{h}-1}\right|+|\bar{v}^{h}\_{t}|\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅(|y^ti,h−x^ti,h|+|∑j≠iNhy^tj,hNh−1−zth|+|∑j≠iNhvtj,hNh−1−v^th|)dt]\displaystyle\quad\cdot\left(\left|\hat{y}^{i,h}\_{t}-\hat{x}^{i,h}\_{t}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{t}}{N^{h}-1}-z^{h}\_{t}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}v^{j,h}\_{t}}{N^{h}-1}-\hat{v}^{h}\_{t}\right|\right)dt\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +L​𝔼​[(1+|y^Ti,h|+|x^Ti,h|+|∑j≠iNhy^Tj,hNh−1|+|zTh|)​(|y^Ti,h−x^Ti,h|+|∑j≠iNhy^Tj,hNh−1−zTh|)]\displaystyle\ +L\mathbb{E}\left[\left(1+|\hat{y}^{i,h}\_{T}|+|\hat{x}^{i,h}\_{T}|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{T}}{N^{h}-1}\right|+|z^{h}\_{T}|\right)\left(\left|\hat{y}^{i,h}\_{T}-\hat{x}^{i,h}\_{T}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{T}}{N^{h}-1}-z^{h}\_{T}\right|\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | L𝔼[∫0T(1+|y^ti,h|+|x^ti,h|+|∑j≠iNhy^tj,hNh−1|+|zth|+2|vti,h|+|∑j≠iNhv^tj,hNh−1|+|v¯th|)\displaystyle\ L\mathbb{E}\Bigg[\int\_{0}^{T}\left(1+|\hat{y}^{i,h}\_{t}|+|\hat{x}^{i,h}\_{t}|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{t}}{N^{h}-1}\right|+|z^{h}\_{t}|+2|v^{i,h}\_{t}|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{v}^{j,h}\_{t}}{N^{h}-1}\right|+|\bar{v}^{h}\_{t}|\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅(|y^ti,h−x^ti,h|+|∑j≠iNh(y^tj,h−x^tj,h)Nh−1|+|∑j≠iNh(x^tj,h−zth)Nh−1|+|∑j≠iNhvtj,hNh−1−v^th|)dt]\displaystyle\quad\cdot\left(\left|\hat{y}^{i,h}\_{t}-\hat{x}^{i,h}\_{t}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{y}^{j,h}\_{t}-\hat{x}^{j,h}\_{t})}{N^{h}-1}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{x}^{j,h}\_{t}-z^{h}\_{t})}{N^{h}-1}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}v^{j,h}\_{t}}{N^{h}-1}-\hat{v}^{h}\_{t}\right|\right)dt\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +L𝔼[(1+|y^Ti,h|+|x^Ti,h|+|∑j≠iNhy^Tj,hNh−1|+|zTh|)\displaystyle\ +L\mathbb{E}\Bigg[\left(1+|\hat{y}^{i,h}\_{T}|+|\hat{x}^{i,h}\_{T}|+\left|\frac{\sum\_{j\neq i}^{N^{h}}\hat{y}^{j,h}\_{T}}{N^{h}-1}\right|+|z^{h}\_{T}|\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⋅(|y^Ti,h−x^Ti,h|+|∑j≠iNh(y^Tj,h−x^Tj,h)Nh−1|+|∑j≠iNh(x^Tj,h−zTh)Nh−1|)].\displaystyle\qquad\cdot\left(\left|\hat{y}^{i,h}\_{T}-\hat{x}^{i,h}\_{T}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{y}^{j,h}\_{T}-\hat{x}^{j,h}\_{T})}{N^{h}-1}\right|+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{x}^{j,h}\_{T}-z^{h}\_{T})}{N^{h}-1}\right|\right)\Bigg]. |  | (43) |

By applying the Cauchy-Schwarz inequality to ([B.1](https://arxiv.org/html/2511.12292v1#A2.Ex121 "B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market")), along with the fact that the processes x^i,h,y^i,h\hat{x}^{i,h},\hat{y}^{i,h} are square-integrable, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |𝒥i,h​(vi,h;𝐲^−i,h,𝐯−i,h)−Ji,h​(vh;zh,v¯h)|\displaystyle\ \left|\mathcal{J}^{i,h}\left(v^{i,h};\hat{{\bf y}}^{-i,h},{\bf v}^{-i,h}\right)-J^{i,h}\left(v^{h};z^{h},\bar{v}^{h}\right)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | KTh(𝔼[∫0T(|y^ti,h−x^ti,h|2+|∑j≠iNh(y^tj,h−x^tj,h)Nh−1|2+|∑j≠iNh(x^tj,h−𝔼​[x^t1,h])Nh−1|2\displaystyle\ K^{h}\_{T}\Bigg(\mathbb{E}\bigg[\int\_{0}^{T}\bigg(\left|\hat{y}^{i,h}\_{t}-\hat{x}^{i,h}\_{t}\right|^{2}+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{y}^{j,h}\_{t}-\hat{x}^{j,h}\_{t})}{N^{h}-1}\right|^{2}+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{x}^{j,h}\_{t}-\mathbb{E}[\hat{x}^{1,h}\_{t}])}{N^{h}-1}\right|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|∑j≠iNh(vtj,h−𝔼​[v^t1,h])Nh−1|2)dt])12\displaystyle\ +\left|\frac{\sum\_{j\neq i}^{N^{h}}(v^{j,h}\_{t}-\mathbb{E}[\hat{v}^{1,h}\_{t}])}{N^{h}-1}\right|^{2}\bigg)dt\bigg]\Bigg)^{\frac{1}{2}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +KTh​(𝔼​[|y^Ti,h−x^Ti,h|2+|∑j≠iNh(y^Tj,h−x^Tj,h)Nh−1|2+|∑j≠iNh(x^Tj,h−𝔼​[x^T1,h])Nh−1|2])12,\displaystyle\ +K^{h}\_{T}\Bigg(\mathbb{E}\Bigg[\left|\hat{y}^{i,h}\_{T}-\hat{x}^{i,h}\_{T}\right|^{2}+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{y}^{j,h}\_{T}-\hat{x}^{j,h}\_{T})}{N^{h}-1}\right|^{2}+\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{x}^{j,h}\_{T}-\mathbb{E}[\hat{x}^{1,h}\_{T}])}{N^{h}-1}\right|^{2}\Bigg]\Bigg)^{\frac{1}{2}}, |  | (44) |

where KTh>0K^{h}\_{T}>0 is a generic constant independent of NkN^{k}, k∈[H]k\in[H], which may change from line to line. To proceed, by Lemma [B.1](https://arxiv.org/html/2511.12292v1#A2.Thmlemma1 "Lemma B.1. ‣ B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|y^ti,h−x^ti,h|2​𝑑t]=∑k=1HO​(1Nk),𝔼​[|y^Ti,h−x^Ti,h|2]=∑k=1HO​(1Nk).\mathbb{E}\left[\int\_{0}^{T}\left|\hat{y}^{i,h}\_{t}-\hat{x}^{i,h}\_{t}\right|^{2}dt\right]=\sum\_{k=1}^{H}O\left(\frac{1}{N^{k}}\right),\mathbb{E}\left[\left|\hat{y}^{i,h}\_{T}-\hat{x}^{i,h}\_{T}\right|^{2}\right]=\sum\_{k=1}^{H}O\left(\frac{1}{N^{k}}\right). |  | (45) |

Next, using the i.i.d. property of (vi,h)i∈[Nh](v^{i,h})\_{i\in[N^{h}]}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|∑j≠iNh(vtj,h−𝔼​[vt1,h])Nh−1|2​𝑑t]=1Nh−1​𝔼​[∫0T(vtj,h−𝔼​[vt1,h])2​𝑑t]=O​(1Nh).\mathbb{E}\left[\int\_{0}^{T}\left|\frac{\sum\_{j\neq i}^{N^{h}}\left(v^{j,h}\_{t}-\mathbb{E}[v^{1,h}\_{t}]\right)}{N^{h}-1}\right|^{2}dt\right]=\frac{1}{N^{h}-1}\mathbb{E}\left[\int\_{0}^{T}\left(v^{j,h}\_{t}-\mathbb{E}[v^{1,h}\_{t}]\right)^{2}dt\right]=O\left(\frac{1}{N^{h}}\right). |  | (46) |

In addition, by the i.i.d. property of (x^i,h)i∈[H](\hat{x}^{i,h})\_{i\in[H]}, we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|∑j≠iNh(x^tj,h−𝔼​[x^t1,h])Nh−1|2​𝑑t]\displaystyle\mathbb{E}\left[\int\_{0}^{T}\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{x}^{j,h}\_{t}-\mathbb{E}[\hat{x}^{1,h}\_{t}])}{N^{h}-1}\right|^{2}dt\right] | =O​(1Nh),𝔼​[|∑j≠iNh(x^Tj,h−𝔼​[x^T1,h])Nh−1|2]\displaystyle=O\left(\frac{1}{N^{h}}\right),\ \mathbb{E}\left[\left|\frac{\sum\_{j\neq i}^{N^{h}}(\hat{x}^{j,h}\_{T}-\mathbb{E}[\hat{x}^{1,h}\_{T}])}{N^{h}-1}\right|^{2}\right] | =O​(1Nh).\displaystyle=O\left(\frac{1}{N^{h}}\right). |  | (47) |

Therefore, the claim follows by substituting ([45](https://arxiv.org/html/2511.12292v1#A2.E45 "In B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market"))-([47](https://arxiv.org/html/2511.12292v1#A2.E47 "In B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market")) into ([B.1](https://arxiv.org/html/2511.12292v1#A2.Ex130 "B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market")).

∎

In the next step, we fix an arbitrary Class h0∈[H]h\_{0}\in[H] and a representative member i0∈[Nh]i\_{0}\in[N^{h}]. Suppose that this member takes an arbitrary admissible strategy ui0,h0u^{i\_{0},h\_{0}}, while all the other members within the MIC adopt the mean field equilibrium strategy. In that case, the wealth process yˇi0,h0\check{y}^{i\_{0},h\_{0}} of that member is governed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​yˇti0,h0\displaystyle d\check{y}^{i\_{0},h\_{0}}\_{t} | =(ryˇti0,h0+lh0−κh0uti0,h0+πh0(∑h0≠k∈[H]ωk(κk−dk)∑j=1Nkvtj,kNk\displaystyle=\Bigg(r\check{y}^{i\_{0},h\_{0}}\_{t}+l^{h\_{0}}-\kappa^{h\_{0}}u^{i\_{0},h\_{0}}\_{t}+\pi^{h\_{0}}\bigg(\sum\_{h\_{0}\neq k\in[H]}\omega^{k}(\kappa^{k}-d^{k})\frac{\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}}{N^{k}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ωh0(κh0−dh0)uti0,h0+∑j≠i0Nh0vtj,h0Nh0))dt+σh0(1−uti0,h0)dWi0,h0t\displaystyle\qquad+\omega^{h\_{0}}(\kappa^{h\_{0}}-d^{h\_{0}})\frac{u^{i\_{0},h\_{0}}\_{t}+\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}v^{j,h\_{0}}\_{t}}{N^{h\_{0}}}\bigg)\Bigg)dt+\sigma^{h\_{0}}(1-u^{i\_{0},h\_{0}}\_{t})dW^{i\_{0},h\_{0}}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +πh0​(∑h0≠k∈[H]σk​ωkNk​∑j=1Nkvtj,k​d​Wtj,k+uti0,h0+∑j≠i0Nh0vtj,h0Nh0​σh0​ωh0​d​Wti0,h0).\displaystyle\quad+\pi^{h\_{0}}\left(\sum\_{h\_{0}\neq k\in[H]}\frac{\sigma^{k}\omega^{k}}{N^{k}}\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}dW^{j,k}\_{t}+\frac{u^{i\_{0},h\_{0}}\_{t}+\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}v^{j,h\_{0}}\_{t}}{N^{h\_{0}}}\sigma^{h\_{0}}\omega^{h\_{0}}dW^{i\_{0},h\_{0}}\_{t}\right). |  |

Let also yˇi,h\check{y}^{i,h} be the wealth process for the member ii from Class hh, where (i,h)≠(i0,h0)(i,h)\neq(i\_{0},h\_{0}). Then, yˇi,h\check{y}^{i,h} is governed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​yˇti,h\displaystyle d\check{y}^{i,h}\_{t} | =(ryˇti,h+lh−κhvti,h+πh(∑h0≠k∈[H]ωk(κk−dk)∑j=1Nkvtj,kNk\displaystyle=\Bigg(r\check{y}^{i,h}\_{t}+l^{h}-\kappa^{h}v^{i,h}\_{t}+\pi^{h}\bigg(\sum\_{h\_{0}\neq k\in[H]}\omega^{k}(\kappa^{k}-d^{k})\frac{\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}}{N^{k}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ωh0(κh0−dh0)uti0,h0+∑j≠i0Nh0vtj,h0Nh0))dt+σh(1−vti,h)dWi,ht\displaystyle\qquad+\omega^{h\_{0}}(\kappa^{h\_{0}}-d^{h\_{0}})\frac{u^{i\_{0},h\_{0}}\_{t}+\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}v^{j,h\_{0}}\_{t}}{N^{h\_{0}}}\bigg)\Bigg)dt+\sigma^{h}(1-v^{i,h}\_{t})dW^{i,h}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +πh​(∑h0≠k∈[H]σk​ωkNk​∑j=1Nkvtj,k​d​Wtj,k+uti0,h0+∑j≠i0Nh0vtj,h0Nh0​σh0​ωh0​d​Wti0,h0).\displaystyle\quad+\pi^{h}\left(\sum\_{h\_{0}\neq k\in[H]}\frac{\sigma^{k}\omega^{k}}{N^{k}}\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}dW^{j,k}\_{t}+\frac{u^{i\_{0},h\_{0}}\_{t}+\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}v^{j,h\_{0}}\_{t}}{N^{h\_{0}}}\sigma^{h\_{0}}\omega^{h\_{0}}dW^{i\_{0},h\_{0}}\_{t}\right). |  |

We also define the process xˇi0,h0\check{x}^{i\_{0},h\_{0}} by

|  |  |  |
| --- | --- | --- |
|  | d​xˇti0,h0=(r​xˇti0,h0+lh0−κh0​uti0,h0+πh0​∑k=1Hωk​(κk−dk)​𝔼​[vt1,k])​d​t+σh​(1−uti0,h0)​d​Wti0,h0.d\check{x}^{i\_{0},h\_{0}}\_{t}=\left(r\check{x}^{i\_{0},h\_{0}}\_{t}+l^{h\_{0}}-\kappa^{h\_{0}}u^{i\_{0},h\_{0}}\_{t}+\pi^{h\_{0}}\sum\_{k=1}^{H}\omega^{k}(\kappa^{k}-d^{k})\mathbb{E}[v^{1,k}\_{t}]\right)dt+\sigma^{h}(1-u^{i\_{0},h\_{0}}\_{t})dW^{i\_{0},h\_{0}}\_{t}. |  |

The following result indicates that, when the class sizes NkN^{k}, k∈[H]k\in[H], are sufficiently large, the deviation from the mean field equilibrium wealth caused the member i0i\_{0} of Class h0h\_{0} would decline with the class sizes.

###### Lemma B.3.

For t≤Tt\leq T, h∈[H]h\in[H], i∈[Nh]i\in[N^{h}] with (i,h)≠(i0,h0)(i,h)\neq(i\_{0},h\_{0}), we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sups≤t|xˇsi0,h0−yˇsi0,h0|2]+𝔼​[sups≤t|x^si,h0−yˇsi,h0|2]+𝔼​[sups≤t|x^si,h−yˇsi,h|2]=∑k=1hO​(1Nk).\mathbb{E}\left[\sup\_{s\leq t}\left|\check{x}^{i\_{0},h\_{0}}\_{s}-\check{y}^{i\_{0},h\_{0}}\_{s}\right|^{2}\right]+\mathbb{E}\left[\sup\_{s\leq t}\left|\hat{x}^{i,h\_{0}}\_{s}-\check{y}^{i,h\_{0}}\_{s}\right|^{2}\right]+\mathbb{E}\left[\sup\_{s\leq t}\left|\hat{x}^{i,h}\_{s}-\check{y}^{i,h}\_{s}\right|^{2}\right]=\sum\_{k=1}^{h}O\left(\frac{1}{N^{k}}\right). |  |

###### Proof.

Notice that

|  |  |  |  |
| --- | --- | --- | --- |
|  | xˇti0,h0−yˇti0,h0\displaystyle\check{x}^{i\_{0},h\_{0}}\_{t}-\check{y}^{i\_{0},h\_{0}}\_{t} | =∫0t[r(xˇsi0,h0−yˇsi0,h0)+πh0(∑h0≠k∈[H]ωk(κk−dk)∑j=1Nk(𝔼​[vs1,k]−vsj,k)Nk\displaystyle=\int\_{0}^{t}\Bigg[r\left(\check{x}^{i\_{0},h\_{0}}\_{s}-\check{y}^{i\_{0},h\_{0}}\_{s}\right)+\pi^{h\_{0}}\Bigg(\sum\_{h\_{0}\neq k\in[H]}\omega^{k}(\kappa^{k}-d^{k})\frac{\sum\_{j=1}^{N^{k}}\left(\mathbb{E}[v^{1,k}\_{s}]-v^{j,k}\_{s}\right)}{N^{k}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ωh0(κh0−dh0)∑j≠i0Nh0(𝔼​[vs1,h0]−vsj,h0)+𝔼​[vs1,h0]−usi0,h0Nh0)]ds\displaystyle\qquad+\omega^{h\_{0}}(\kappa^{h\_{0}}-d^{h\_{0}})\frac{\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}\left(\mathbb{E}[v^{1,h\_{0}}\_{s}]-v^{j,h\_{0}}\_{s}\right)+\mathbb{E}[v\_{s}^{1,h\_{0}}]-u^{i\_{0},h\_{0}}\_{s}}{N^{h\_{0}}}\Bigg)\Bigg]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −πh0​(∫0t∑h0≠k∈[H]σk​ωkNk​∑j=1Nkvtj,k​d​Wsj,k+∫0tusi0,h0+∑j≠i0Nh0vsj,h0Nh0​σh0​ωh0​𝑑Wsi0,h0).\displaystyle\quad-\pi^{h\_{0}}\left(\int\_{0}^{t}\sum\_{h\_{0}\neq k\in[H]}\frac{\sigma^{k}\omega^{k}}{N^{k}}\sum\_{j=1}^{N^{k}}v^{j,k}\_{t}dW^{j,k}\_{s}+\int\_{0}^{t}\frac{u^{i\_{0},h\_{0}}\_{s}+\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}v^{j,h\_{0}}\_{s}}{N^{h\_{0}}}\sigma^{h\_{0}}\omega^{h\_{0}}dW^{i\_{0},h\_{0}}\_{s}\right). |  |

Hence, there exists KT>0K\_{T}>0 independent of NkN^{k}, k∈[H]k\in[H], such that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[sups≤t|xˇsi0,h0−yˇsi0,h0|2]\displaystyle\ \mathbb{E}\left[\sup\_{s\leq t}\left|\check{x}^{i\_{0},h\_{0}}\_{s}-\check{y}^{i\_{0},h\_{0}}\_{s}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | KT​∫0t𝔼​[|xˇsi0,h0−yˇsi0,h0|2]​𝑑s+KT​∑h0≠k∈[H]∫0t𝔼​[(1Nk​∑j=1Nk(𝔼​[vs1,k]−vsj,k))2]​𝑑s\displaystyle\ K\_{T}\int\_{0}^{t}\mathbb{E}\left[\left|\check{x}^{i\_{0},h\_{0}}\_{s}-\check{y}^{i\_{0},h\_{0}}\_{s}\right|^{2}\right]ds+K\_{T}\sum\_{h\_{0}\neq k\in[H]}\int\_{0}^{t}\mathbb{E}\left[\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\left(\mathbb{E}[v^{1,k}\_{s}]-v^{j,k}\_{s}\right)\right)^{2}\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +KT​∫0t𝔼​[(1Nh0​(∑j≠i0Nh0(𝔼​[vs1,h0]−vsj,h0)+𝔼​[vs1,h0]−usi0,h0))2]​𝑑s\displaystyle\ +K\_{T}\int\_{0}^{t}\mathbb{E}\left[\left(\frac{1}{N^{h\_{0}}}\left(\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}\left(\mathbb{E}[v^{1,h\_{0}}\_{s}]-v^{j,h\_{0}}\_{s}\right)+\mathbb{E}[v\_{s}^{1,h\_{0}}]-u^{i\_{0},h\_{0}}\_{s}\right)\right)^{2}\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +KT​∑k≠h0𝔼​[sups≤t(1Nk​∑j=1Nk∫0svlj,k​𝑑Wlj,k)2]​d​s\displaystyle\ +K\_{T}\sum\_{k\neq h\_{0}}\mathbb{E}\left[\sup\_{s\leq t}\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\int\_{0}^{s}v^{j,k}\_{l}dW^{j,k}\_{l}\right)^{2}\right]ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +KT​𝔼​[sups≤t(1Nh0​∑j=1Nh0∫0s(usi0,h0+∑j≠i0vsj,h0)​𝑑Wsi0,h0)2].\displaystyle\ +K\_{T}\mathbb{E}\left[\sup\_{s\leq t}\left(\frac{1}{N^{h\_{0}}}\sum\_{j=1}^{N^{h\_{0}}}\int\_{0}^{s}\left(u^{i\_{0},h\_{0}}\_{s}+\sum\_{j\neq i\_{0}}v^{j,h\_{0}}\_{s}\right)dW^{i\_{0},h\_{0}}\_{s}\right)^{2}\right]. |  | (48) |

By i.i.d. property of (vi,h)i∈[Nh](v^{i,h})\_{i\in[N^{h}]}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑k≠h0∫0t𝔼​[(1Nk​∑j=1Nk(𝔼​[vs1,k]−vsj,k))2]​𝑑s\displaystyle\sum\_{k\neq h\_{0}}\int\_{0}^{t}\mathbb{E}\left[\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\left(\mathbb{E}[v^{1,k}\_{s}]-v^{j,k}\_{s}\right)\right)^{2}\right]ds | =∑k≠h0O​(1Nk),\displaystyle=\sum\_{k\neq h\_{0}}O\left(\frac{1}{N^{k}}\right), |  | (49) |
|  | ∑k≠h0𝔼​[sups≤t(1Nk​∑j=1Nk∫0svlj,k​𝑑Wlj,k)2]​d​s\displaystyle\sum\_{k\neq h\_{0}}\mathbb{E}\left[\sup\_{s\leq t}\left(\frac{1}{N^{k}}\sum\_{j=1}^{N^{k}}\int\_{0}^{s}v^{j,k}\_{l}dW^{j,k}\_{l}\right)^{2}\right]ds | =∑k≠h0O​(1Nk),\displaystyle=\sum\_{k\neq h\_{0}}O\left(\frac{1}{N^{k}}\right), |  |

and that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫0t𝔼​[(1Nh0​(∑j≠i0Nh0(𝔼​[vs1,h0]−vsj,h0)+𝔼​[vs1,h0]−usi0,h0))2]​𝑑s\displaystyle\ \ \int\_{0}^{t}\mathbb{E}\left[\left(\frac{1}{N^{h\_{0}}}\left(\sum\_{j\neq i\_{0}}^{N^{h\_{0}}}\left(\mathbb{E}[v^{1,h\_{0}}\_{s}]-v^{j,h\_{0}}\_{s}\right)+\mathbb{E}[v\_{s}^{1,h\_{0}}]-u^{i\_{0},h\_{0}}\_{s}\right)\right)^{2}\right]ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤KT​∫0t(1Nh0​𝔼​[(vs1,h0−𝔼​[vs1,h0])2]+1(Nh0)2​∑j≠i0𝔼​[|𝔼​[vs1,h0]−vsj,h0|​|𝔼​[vs1,h0]−usi0,h0|])​𝑑s\displaystyle\leq K\_{T}\int\_{0}^{t}\left(\frac{1}{N^{h\_{0}}}\mathbb{E}\left[\left(v^{1,h\_{0}}\_{s}-\mathbb{E}[v^{1,h\_{0}}\_{s}]\right)^{2}\right]+\frac{1}{(N^{h\_{0}})^{2}}\sum\_{j\neq i\_{0}}\mathbb{E}\left[\left|\mathbb{E}[v^{1,h\_{0}}\_{s}]-v^{j,h\_{0}}\_{s}\right|\left|\mathbb{E}[v\_{s}^{1,h\_{0}}]-u^{i\_{0},h\_{0}}\_{s}\right|\right]\right)ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =O​(1Nh0),\displaystyle=O\left(\frac{1}{N^{h\_{0}}}\right), |  | (50) |

as Nh0→∞N^{h\_{0}}\to\infty. Likewise, using the Burkholder-Davis-Gundy inequality, one can show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sups≤t(1Nh0​∑j=1Nh0∫0s(usi0,h0+∑j≠i0vsj,h0)​𝑑Wsi0,h0)2​d​s]=O​(1Nh0).\mathbb{E}\left[\sup\_{s\leq t}\left(\frac{1}{N^{h\_{0}}}\sum\_{j=1}^{N^{h\_{0}}}\int\_{0}^{s}\left(u^{i\_{0},h\_{0}}\_{s}+\sum\_{j\neq i\_{0}}v^{j,h\_{0}}\_{s}\right)dW^{i\_{0},h\_{0}}\_{s}\right)^{2}ds\right]=O\left(\frac{1}{N^{h\_{0}}}\right). |  | (51) |

By substituting ([49](https://arxiv.org/html/2511.12292v1#A2.E49 "In B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market")), ([B.1](https://arxiv.org/html/2511.12292v1#A2.Ex148 "B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market")) and ([51](https://arxiv.org/html/2511.12292v1#A2.E51 "In B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market")) into ([B.1](https://arxiv.org/html/2511.12292v1#A2.Ex144 "B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market")), we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sups≤t|xˇsi0,h0−yˇsi0,h0|2]=∑k=1HO​(1Nk).\mathbb{E}\left[\sup\_{s\leq t}\left|\check{x}^{i\_{0},h\_{0}}\_{s}-\check{y}^{i\_{0},h\_{0}}\_{s}\right|^{2}\right]=\sum\_{k=1}^{H}O\left(\frac{1}{N^{k}}\right). |  |

The fact that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sups≤t|x^si,h0−yˇsi,h0|2]+𝔼​[sups≤t|x^si,h−yˇsi,h|2]=∑k=1HO​(1Nk)\mathbb{E}\left[\sup\_{s\leq t}\left|\hat{x}^{i,h\_{0}}\_{s}-\check{y}^{i,h\_{0}}\_{s}\right|^{2}\right]+\mathbb{E}\left[\sup\_{s\leq t}\left|\hat{x}^{i,h}\_{s}-\check{y}^{i,h}\_{s}\right|^{2}\right]=\sum\_{k=1}^{H}O\left(\frac{1}{N^{k}}\right) |  |

can be shown by a similar argument, henceforth the calculations are omitted.
∎

The following result is a consequence of Lemma [B.3](https://arxiv.org/html/2511.12292v1#A2.Thmlemma3 "Lemma B.3. ‣ B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market"), which can be shown by following the proof of Lemma [B.2](https://arxiv.org/html/2511.12292v1#A2.Thmlemma2 "Lemma B.2. ‣ B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market").

###### Lemma B.4.

For h0∈[H]h\_{0}\in[H], we have

|  |  |  |
| --- | --- | --- |
|  | |𝒥i0,h0​(ui0,h0;𝐲ˇ−i0,h0,𝐯−i0,h0)−Ji0,h0​(ui0,h0;zh0,v¯h0)|=∑k=1HO​(1Nk),\left|\mathcal{J}^{i\_{0},h\_{0}}\left(u^{i\_{0},h\_{0}};\check{{\bf y}}^{-i\_{0},h\_{0}},{\bf v}^{-i\_{0},h\_{0}}\right)-J^{i\_{0},h\_{0}}\left(u^{i\_{0},h\_{0}};z^{h\_{0}},\bar{v}^{h\_{0}}\right)\right|=\sum\_{k=1}^{H}O\left(\frac{1}{\sqrt{N^{k}}}\right), |  |

where 𝐲ˇ−i0,h0=(yˇi,h0)i∈[Nh0],i≠i0\check{{\bf y}}^{-i\_{0},h\_{0}}=(\check{y}^{i,h\_{0}})\_{i\in[N^{h\_{0}}],i\neq i\_{0}}.

As a result of Lemmas [B.2](https://arxiv.org/html/2511.12292v1#A2.Thmlemma2 "Lemma B.2. ‣ B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market") and [B.4](https://arxiv.org/html/2511.12292v1#A2.Thmlemma4 "Lemma B.4. ‣ B.1 Proof of Theorem 2.1 ‣ Appendix B Proofs and Extensions for Section 2 ‣ Mean Field Analysis of Mutual Insurance Market"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥i0,h0​(ui0,h0;𝐲ˇ−i0,h0,𝐯−i0,h0)\displaystyle\mathcal{J}^{i\_{0},h\_{0}}\left(u^{i\_{0},h\_{0}};\check{{\bf y}}^{-i\_{0},h\_{0}},{\bf v}^{-i\_{0},h\_{0}}\right) | ≤Ji0,h0​(ui0,h0;zh0,v¯h0)+∑k=1HO​(1Nk)\displaystyle\leq J^{i\_{0},h\_{0}}\left(u^{i\_{0},h\_{0}};z^{h\_{0}},\bar{v}^{h\_{0}}\right)+\sum\_{k=1}^{H}O\left(\frac{1}{\sqrt{N^{k}}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Ji0,h0​(vi0,h0;zh0,v¯h0)+∑k=1HO​(1Nk)\displaystyle\leq J^{i\_{0},h\_{0}}\left(v^{i\_{0},h\_{0}};z^{h\_{0}},\bar{v}^{h\_{0}}\right)+\sum\_{k=1}^{H}O\left(\frac{1}{\sqrt{N^{k}}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝒥i0,h0​(vi0,h0;𝐲^−i0,h0,𝐯−i0,h0)+∑k=1HO​(1Nk),\displaystyle\leq\mathcal{J}^{i\_{0},h\_{0}}\left(v^{i\_{0},h\_{0}};\hat{{\bf y}}^{-i\_{0},h\_{0}},{\bf v}^{-i\_{0},h\_{0}}\right)+\sum\_{k=1}^{H}O\left(\frac{1}{\sqrt{N^{k}}}\right), |  |

where the second inequality follows from the optimality of vi0,h0v^{i\_{0},h\_{0}}. The desired ε\varepsilon-Nash equilibrium is thus established.

## Appendix C Proofs of Assertions in Section [3](https://arxiv.org/html/2511.12292v1#S3 "3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")

This section contains the proofs of statements in Section [3](https://arxiv.org/html/2511.12292v1#S3 "3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market").

### C.1 Proof of Lemma [3.1](https://arxiv.org/html/2511.12292v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")

We first show that vh∈L𝔽h2​([0,T];ℝ)↦Jh​(vh)v^{h}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R})\mapsto J^{h}(v^{h}) is continuous. Let (zh)h∈[H](z^{h})\_{h\in[H]} and (v¯h)h∈[H](\bar{v}^{h})\_{h\in[H]} be exogeneously given. Fix vˇh∈L𝔽h2​([0,T];ℝ)\check{v}^{h}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}), and let xˇh\check{x}^{h} be the associated wealth process when vˇh\check{v}^{h} is adopted. For any vh∈L𝔽h2​([0,T];ℝ)v^{h}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}) with the corresponding wealth process xhx^{h}, consider

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |Jh​(vh)−Jh​(v^h)|\displaystyle\ \left|J^{h}(v^{h})-J^{h}(\hat{v}^{h})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​[∫0T|fh​(t,xth,zth,vth,v¯th)−fh​(t,xˇth,zth,vˇth,v¯th)|​𝑑t+|gh​(xTh,zTh)−gh​(xˇTh,zTh)|]\displaystyle\ \mathbb{E}\left[\int\_{0}^{T}\left|f^{h}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})-f^{h}(t,\check{x}^{h}\_{t},z^{h}\_{t},\check{v}^{h}\_{t},\bar{v}^{h}\_{t})\right|dt+\left|g^{h}(x^{h}\_{T},z^{h}\_{T})-g^{h}(\check{x}^{h}\_{T},z^{h}\_{T})\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | L𝔼[∫0T(1+|xth|+|xˇth|+|vth|+|vˇth|+2|zth|+2|v¯th|)(|xth−xˇth|+|vth−vˇth|)dt\displaystyle\ L\mathbb{E}\Bigg[\int\_{0}^{T}\left(1+|x^{h}\_{t}|+|\check{x}^{h}\_{t}|+|v^{h}\_{t}|+|\check{v}^{h}\_{t}|+2|z^{h}\_{t}|+2|\bar{v}^{h}\_{t}|\right)\left(\left|x^{h}\_{t}-\check{x}^{h}\_{t}\right|+\left|v^{h}\_{t}-\check{v}^{h}\_{t}\right|\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1+|xTh|+|xˇTh|+2|zTh|)|xTh−xˇTh|]\displaystyle\quad+\left(1+|x^{h}\_{T}|+|\check{x}^{h}\_{T}|+2|z^{h}\_{T}|\right)\left|x^{h}\_{T}-\check{x}^{h}\_{T}\right|\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | L𝔼[∫0T(1+|xth−xˇth|+2|xˇth|+|vth−vˇth|+2|vˇth|+2|zth|+2|v¯th|)\displaystyle\ L\mathbb{E}\Bigg[\int\_{0}^{T}\left(1+|x^{h}\_{t}-\check{x}^{h}\_{t}|+2|\check{x}^{h}\_{t}|+|v^{h}\_{t}-\check{v}^{h}\_{t}|+2|\check{v}^{h}\_{t}|+2|z^{h}\_{t}|+2|\bar{v}^{h}\_{t}|\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅(|xth−xˇth|+|vth−vˇth|)dt+(1+|xTh−xˇTh|+2|xˇTh|+2|zTh|)|xTh−xˇTh|],\displaystyle\quad\cdot\left(\left|x^{h}\_{t}-\check{x}^{h}\_{t}\right|+\left|v^{h}\_{t}-\check{v}^{h}\_{t}\right|\right)dt+\left(1+|x^{h}\_{T}-\check{x}^{h}\_{T}|+2|\check{x}^{h}\_{T}|+2|z^{h}\_{T}|\right)\left|x^{h}\_{T}-\check{x}^{h}\_{T}\right|\Bigg], |  |

where the second inequality follows from Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").A. By simple applications of Young’s and the Cauchy-Schwarz inequality, and noticing that

|  |  |  |  |
| --- | --- | --- | --- |
|  | xˇth\displaystyle\check{x}^{h}\_{t} | =∫0ter​(t−s)​(lh−κh​vˇs+πh​∑k=1Hωk​(κk−dk)​v¯tk)​𝑑s+σh​∫0ter​(t−s)​(1−vˇsh)​𝑑Wsh,\displaystyle=\int\_{0}^{t}e^{r(t-s)}\left(l^{h}-\kappa^{h}\check{v}\_{s}+\pi^{h}\sum\_{k=1}^{H}\omega^{k}(\kappa^{k}-d^{k})\bar{v}^{k}\_{t}\right)ds+\sigma^{h}\int\_{0}^{t}e^{r(t-s)}(1-\check{v}^{h}\_{s})dW^{h}\_{s}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | xth−xˇth\displaystyle x^{h}\_{t}-\check{x}^{h}\_{t} | =−κh​∫0ter​(t−s)​(vsh−vˇsh)​𝑑s−σh​∫0ter​(t−s)​(vsh−vˇsh)​𝑑Wsh,\displaystyle=-\kappa^{h}\int\_{0}^{t}e^{r(t-s)}(v^{h}\_{s}-\check{v}^{h}\_{s})ds-\sigma^{h}\int\_{0}^{t}e^{r(t-s)}(v^{h}\_{s}-\check{v}^{h}\_{s})dW^{h}\_{s}, |  |

we infer the existence of a constant KTh>0K^{h}\_{T}>0 independent of xh,vhx^{h},v^{h}, such that

|  |  |  |
| --- | --- | --- |
|  | |Jh​(vh)−Jh​(vˇh)|≤KTh​𝔼​[∫0T|vth−vˇth|2​𝑑t].\displaystyle\left|J^{h}(v^{h})-J^{h}(\check{v}^{h})\right|\leq K^{h}\_{T}\mathbb{E}\left[\int\_{0}^{T}\left|v^{h}\_{t}-\check{v}^{h}\_{t}\right|^{2}dt\right]. |  |

Therefore, the continuity is established.

Next, we show that vh↦Jh​(vh)v^{h}\mapsto J^{h}(v^{h}) is coercive and strictly concave in L𝔽h2​([0,T];ℝ)L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}). To this end, let θ∈ℝ\theta\in\mathbb{R} and v^h∈L𝔽h2​([0,T];ℝ)\hat{v}^{h}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}), and define vh,θ:=vh+θ​v^hv^{h,\theta}:=v^{h}+\theta\hat{v}^{h}. By linearity, the associated wealth process under the control vh,θv^{h,\theta} is given by xh,θ=xh+θ​x^hx^{h,\theta}=x^{h}+\theta\hat{x}^{h}, where x^h\hat{x}^{h} satisfies the following SDE:

|  |  |  |
| --- | --- | --- |
|  | d​x^th=(r​x^th−κh​v^th)​d​t−σh​v^th​d​Wth,x^0h=0.d\hat{x}^{h}\_{t}=(r\hat{x}^{h}\_{t}-\kappa^{h}\hat{v}^{h}\_{t})dt-\sigma^{h}\hat{v}^{h}\_{t}dW^{h}\_{t},\ \hat{x}^{h}\_{0}=0. |  |

To proceed, we shall first deduce an expression for the Gâteaux derivative of Jh​(vh)J^{h}(v^{h}). Notice that

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​θ​Jh​(vh,θ)\displaystyle\frac{d}{d\theta}J^{h}(v^{h,\theta}) | =𝔼​[∫0T[fxh​(t,xth,θ,zth,vth,θ,v¯th)​x^th+fvh​(t,xth,θ,zth,vth,θ,v¯th)​v^th]​𝑑t]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left[f\_{x}^{h}\left(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t}\right)\hat{x}^{h}\_{t}+f\_{v}^{h}\left(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t}\right)\hat{v}^{h}\_{t}\right]dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼​[gxh​(xTh,θ,zTh)​x^Th].\displaystyle\quad+\mathbb{E}[g\_{x}^{h}(x^{h,\theta}\_{T},z^{h}\_{T})\hat{x}^{h}\_{T}]. |  | (52) |

Consider the following BSDE:

|  |  |  |
| --- | --- | --- |
|  | {−d​pth,θ=[r​pth,θ−fxh​(t,xth,θ,zth,vth,θ,v¯th)]​d​t−ηth,θ​d​Wth,pTh,θ=−gxh​(xTh,θ,zTh).\left\{\begin{aligned} -dp^{h,\theta}\_{t}&=\left[rp^{h,\theta}\_{t}-f\_{x}^{h}\left(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t}\right)\right]dt-\eta^{h,\theta}\_{t}dW^{h}\_{t},\\ p^{h,\theta}\_{T}&=-g\_{x}^{h}(x^{h,\theta}\_{T},z^{h}\_{T}).\end{aligned}\right. |  |

Notice that the forward equations of xhx^{h} and x^h\hat{x}^{h} are decoupled from ph,θp^{h,\theta}, and thus the latter admits a unique solution, thanks to Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"). By applying Itô’s lemma on pth,θ​x^thp^{h,\theta}\_{t}\hat{x}^{h}\_{t}, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[gxh​(xTh,θ,zTh)​x^Th]\displaystyle\mathbb{E}[g\_{x}^{h}(x^{h,\theta}\_{T},z^{h}\_{T})\hat{x}^{h}\_{T}] | =𝔼​[∫0T[−fxh​(t,xth,θ,zth,vth,θ,v¯th)​x^th+(κh​pth,θ+σh​ηth,θ)​v^th]​𝑑t].\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left[-f\_{x}^{h}\left(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t}\right)\hat{x}^{h}\_{t}+\left(\kappa^{h}p^{h,\theta}\_{t}+\sigma^{h}\eta^{h,\theta}\_{t}\right)\hat{v}^{h}\_{t}\right]dt\right]. |  | (53) |

Substituting ([53](https://arxiv.org/html/2511.12292v1#A3.E53 "In C.1 Proof of Lemma 3.1 ‣ Appendix C Proofs of Assertions in Section 3 ‣ Mean Field Analysis of Mutual Insurance Market")) into ([C.1](https://arxiv.org/html/2511.12292v1#A3.Ex166 "C.1 Proof of Lemma 3.1 ‣ Appendix C Proofs of Assertions in Section 3 ‣ Mean Field Analysis of Mutual Insurance Market")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​θ​Jh​(vh,θ)\displaystyle\frac{d}{d\theta}J^{h}(v^{h,\theta}) | =𝔼​[∫0T[fvh​(t,xth,θ,zth,vth,θ,v¯th)+κh​pth,θ+σh​ηth,θ]​v^th​𝑑t]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left[f\_{v}^{h}\left(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t}\right)+\kappa^{h}p^{h,\theta}\_{t}+\sigma^{h}\eta^{h,\theta}\_{t}\right]\hat{v}^{h}\_{t}dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​[∫0Tqth,vh,θ​v^th​𝑑t],\displaystyle=\mathbb{E}\left[\int\_{0}^{T}q^{h,v^{h,\theta}}\_{t}\hat{v}^{h}\_{t}dt\right], |  | (54) |

where

|  |  |  |
| --- | --- | --- |
|  | qth,vh,θ:=fvh​(t,xth,θ,zth,vth,θ,v¯th)+κh​pth,θ+σh​ηth,θ,t∈[0,T].q^{h,v^{h,\theta}}\_{t}:=f\_{v}^{h}\left(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t}\right)+\kappa^{h}p^{h,\theta}\_{t}+\sigma^{h}\eta^{h,\theta}\_{t},\ t\in[0,T]. |  |

Next, for any θ,ϕ∈ℝ\theta,\phi\in\mathbb{R}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼[∫0T(qth,vh,θ−qth,vh,ϕ)(vth,θ−vth,ϕ))dt]\displaystyle\ \mathbb{E}\left[\int\_{0}^{T}\left(q^{h,v^{h,\theta}}\_{t}-q^{h,v^{h,\phi}}\_{t}\right)\left(v^{h,\theta}\_{t}-v^{h,\phi}\_{t}\right)\bigg)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[∫0T[fvh​(t,xth,θ,zth,vth,θ,v¯th)−fvh​(t,xth,ϕ,zth,vth,ϕ,v¯th)]​(vth,θ−vth,ϕ)​𝑑t]\displaystyle\ \mathbb{E}\left[\int\_{0}^{T}\left[f\_{v}^{h}(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t})-f\_{v}^{h}(t,x^{h,\phi}\_{t},z^{h}\_{t},v^{h,\phi}\_{t},\bar{v}^{h}\_{t})\right]\left(v^{h,\theta}\_{t}-v^{h,\phi}\_{t}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[∫0T[κh​(pth,θ−pth,ϕ)+σh​(ηth,θ−ηth,ϕ)]​(vth,θ−vth,ϕ)​𝑑t]\displaystyle\ +\mathbb{E}\left[\int\_{0}^{T}\left[\kappa^{h}(p^{h,\theta}\_{t}-p^{h,\phi}\_{t})+\sigma^{h}(\eta^{h,\theta}\_{t}-\eta^{h,\phi}\_{t})\right]\left(v^{h,\theta}\_{t}-v^{h,\phi}\_{t}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[∫0T[fvh​(t,xth,θ,zth,vth,θ,v¯th)−fvh​(t,xth,ϕ,zth,vth,ϕ,v¯th)]​(vth,θ−vth,ϕ)​𝑑t]\displaystyle\ \mathbb{E}\left[\int\_{0}^{T}\left[f\_{v}^{h}(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t})-f\_{v}^{h}(t,x^{h,\phi}\_{t},z^{h}\_{t},v^{h,\phi}\_{t},\bar{v}^{h}\_{t})\right]\left(v^{h,\theta}\_{t}-v^{h,\phi}\_{t}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[∫0T[fxh​(t,xth,θ,zth,vth,θ,v¯th)−fxh​(t,xth,ϕ,zth,vth,ϕ,v¯th)]​(xth,θ−xth,ϕ)​𝑑t]\displaystyle\ +\mathbb{E}\left[\int\_{0}^{T}\left[f\_{x}^{h}(t,x^{h,\theta}\_{t},z^{h}\_{t},v^{h,\theta}\_{t},\bar{v}^{h}\_{t})-f\_{x}^{h}(t,x^{h,\phi}\_{t},z^{h}\_{t},v^{h,\phi}\_{t},\bar{v}^{h}\_{t})\right]\left(x^{h,\theta}\_{t}-x^{h,\phi}\_{t}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[(gxh​(xTh,θ,zTh)−gxh​(xTh,ϕ,zTh))​(xTh,θ−xTh,ϕ)]\displaystyle\ +\mathbb{E}\left[\left(g\_{x}^{h}(x^{h,\theta}\_{T},z^{h}\_{T})-g\_{x}^{h}(x^{h,\phi}\_{T},z^{h}\_{T})\right)\left(x^{h,\theta}\_{T}-x^{h,\phi}\_{T}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | −α1V​𝔼​[∫0T|vth,θ−vth,ϕ|2​𝑑t],\displaystyle\ -\alpha^{V}\_{1}\mathbb{E}\left[\int\_{0}^{T}\left|v^{h,\theta}\_{t}-v^{h,\phi}\_{t}\right|^{2}dt\right], |  |

where the second equality follows from applying Itô’s lemma on (pth,θ−pth,ϕ)​(xth,θ−xth,ϕ)(p^{h,\theta}\_{t}-p^{h,\phi}\_{t})(x^{h,\theta}\_{t}-x^{h,\phi}\_{t}); and the last line follows from Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").B.

Finally, for any fixed v^h∈L𝔽h2​([0,T];ℝ)\hat{v}^{h}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}) and any vh∈L𝔽h2​([0,T];ℝ)v^{h}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jh​(vh)−Jh​(v^h)\displaystyle J^{h}(v^{h})-J^{h}(\hat{v}^{h}) | =−∫01dd​θ​Jh​(vh+θ​(v^h−vh))​𝑑θ\displaystyle=-\int\_{0}^{1}\frac{d}{d\theta}J^{h}(v^{h}+\theta(\hat{v}^{h}-v^{h}))d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫01𝔼​[∫0Tqth,vh+θ​(v^h−vh)​(v^th−vth)​𝑑t]​𝑑θ\displaystyle=-\int\_{0}^{1}\mathbb{E}\left[\int\_{0}^{T}q^{h,v^{h}+\theta(\hat{v}^{h}-v^{h})}\_{t}(\hat{v}^{h}\_{t}-v^{h}\_{t})dt\right]d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0111−θ​𝔼​[∫0Tqth,vh+θ​(v^h−vh)​(vth+θ​(v^th−vth)−v^th)​𝑑t]​𝑑θ\displaystyle=\int\_{0}^{1}\frac{1}{1-\theta}\mathbb{E}\left[\int\_{0}^{T}q^{h,v^{h}+\theta(\hat{v}^{h}-v^{h})}\_{t}\left(v^{h}\_{t}+\theta(\hat{v}^{h}\_{t}-v^{h}\_{t})-\hat{v}^{h}\_{t}\right)dt\right]d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01𝔼​[∫0Tqth,v^h​(vth−v^th)​𝑑t]​𝑑θ\displaystyle=\int\_{0}^{1}\mathbb{E}\left[\int\_{0}^{T}q^{h,\hat{v}^{h}}\_{t}\left(v^{h}\_{t}-\hat{v}^{h}\_{t}\right)dt\right]d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0111−θ​𝔼​[∫0T(qth,vh+θ​(v^h−vh)−qth,v^h)​(vth+θ​(v^th−vth)−v^th)​𝑑t]​𝑑θ\displaystyle\ +\int\_{0}^{1}\frac{1}{1-\theta}\mathbb{E}\left[\int\_{0}^{T}\left(q^{h,v^{h}+\theta(\hat{v}^{h}-v^{h})}\_{t}-q^{h,\hat{v}^{h}}\_{t}\right)\left(v^{h}\_{t}+\theta(\hat{v}^{h}\_{t}-v^{h}\_{t})-\hat{v}^{h}\_{t}\right)dt\right]d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[∫0Tqth,v^h​(vth−v^th)​𝑑t]−∫01α1V​(1−θ)​𝔼​[∫0T|vth−v^th|2​𝑑t]​𝑑θ\displaystyle\leq\mathbb{E}\left[\int\_{0}^{T}q^{h,\hat{v}^{h}}\_{t}\left(v^{h}\_{t}-\hat{v}^{h}\_{t}\right)dt\right]-\int\_{0}^{1}\alpha^{V}\_{1}(1-\theta)\mathbb{E}\left[\int\_{0}^{T}\left|v^{h}\_{t}-\hat{v}^{h}\_{t}\right|^{2}dt\right]d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0Tqth,v^h​(vth−v^th)​𝑑t]−α1V2​𝔼​[∫0T|vth−v^th|2​𝑑t],\displaystyle=\mathbb{E}\left[\int\_{0}^{T}q^{h,\hat{v}^{h}}\_{t}\left(v^{h}\_{t}-\hat{v}^{h}\_{t}\right)dt\right]-\frac{\alpha^{V}\_{1}}{2}\mathbb{E}\left[\int\_{0}^{T}\left|v^{h}\_{t}-\hat{v}^{h}\_{t}\right|^{2}dt\right], |  |

thereby establishing the strict concavity (more precisely, the α1V\alpha^{V}\_{1}-concavity) of the objective function.

Finally, for any fixed v^h\hat{v}^{h}, using the square integrability of qh,v^hq^{h,\hat{v}^{h}} and Young’s inequality,

|  |  |  |
| --- | --- | --- |
|  | Jh​(vh)−Jh​(v^h)≤1α1V​𝔼​[∫0T(qth,v^h)2​𝑑t]−α1V4​𝔼​[∫0T|vth−v^th|2​𝑑t]→−∞J^{h}(v^{h})-J^{h}(\hat{v}^{h})\leq\frac{1}{\alpha^{V}\_{1}}\mathbb{E}\left[\int\_{0}^{T}\left(q^{h,\hat{v}^{h}}\_{t}\right)^{2}dt\right]-\frac{\alpha^{V}\_{1}}{4}\mathbb{E}\left[\int\_{0}^{T}\left|v^{h}\_{t}-\hat{v}^{h}\_{t}\right|^{2}dt\right]\to-\infty |  |

as 𝔼​[∫0T|vth|2​𝑑t]→∞\mathbb{E}[\int\_{0}^{T}|v^{h}\_{t}|^{2}dt]\to\infty. Therefore, the objective function is coercive.

### C.2 Proof of Theorem [3.1](https://arxiv.org/html/2511.12292v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")

Let v^h∈𝒜𝔽h​(I)\hat{v}^{h}\in\mathcal{A}\_{\mathbb{F}^{h}}(I) be an arbitrary strategy, and x^h\hat{x}^{h} be its associated wealth process. Given (zh)h=1H(z^{h})\_{h=1}^{H} and (v¯h)h=1H(\bar{v}^{h})\_{h=1}^{H}, consider

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Jh​(v^h)−Jh​(vh)\displaystyle\ J^{h}(\hat{v}^{h})-J^{h}(v^{h}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[∫0T(fh​(t,x^th,zth,v^th,v¯th)−fh​(t,xth,zth,vth,v¯th))​𝑑t+(gh​(x^Th,zTh)−gh​(xTh,zTh))]\displaystyle\ \mathbb{E}\left[\int\_{0}^{T}\left(f^{h}(t,\hat{x}^{h}\_{t},z^{h}\_{t},\hat{v}^{h}\_{t},\bar{v}^{h}\_{t})-f^{h}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})\right)dt+\left(g^{h}(\hat{x}^{h}\_{T},z^{h}\_{T})-g^{h}(x^{h}\_{T},z^{h}\_{T})\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼[∫0T(fxh(t,xth,zth,vth,v¯th)(x^th−xth)+fvh(t,xth,zth,vth,v¯th)(v^th−vth))dt\displaystyle\ \mathbb{E}\Bigg[\int\_{0}^{T}\left(f^{h}\_{x}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})(\hat{x}^{h}\_{t}-x^{h}\_{t})+f^{h}\_{v}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})(\hat{v}^{h}\_{t}-v^{h}\_{t})\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +gxh(xTh,zTh)(x^Th−xTh)]\displaystyle\quad+g^{h}\_{x}(x^{h}\_{T},z^{h}\_{T})(\hat{x}^{h}\_{T}-x^{h}\_{T})\Bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[∫0T(fxh​(t,xth,zth,vth,v¯th)​(x^th−xth)+fvh​(t,xth,zth,vth,v¯th)​(v^th−vth))​𝑑t−pTh​(x^Th−xTh)],\displaystyle\ \mathbb{E}\Bigg[\int\_{0}^{T}\left(f^{h}\_{x}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})(\hat{x}^{h}\_{t}-x^{h}\_{t})+f^{h}\_{v}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})(\hat{v}^{h}\_{t}-v^{h}\_{t})\right)dt-p^{h}\_{T}(\hat{x}^{h}\_{T}-x^{h}\_{T})\Bigg], |  | (55) |

where the inequality follows from the Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market").B and Remark [2.2](https://arxiv.org/html/2511.12292v1#S2.Thmremark2 "Remark 2.2. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"). Notice that x^h−xh\hat{x}^{h}-x^{h} satisfies the following SDE:

|  |  |  |
| --- | --- | --- |
|  | d​(x^th−xth)=(r​(x^th−xth)−κh​(v^th−vth))​d​t−σh​(v^th−vth)​d​Wth,x^0h−x0h=0.d(\hat{x}^{h}\_{t}-x^{h}\_{t})=\left(r(\hat{x}^{h}\_{t}-x^{h}\_{t})-\kappa^{h}(\hat{v}^{h}\_{t}-v^{h}\_{t})\right)dt-\sigma^{h}(\hat{v}^{h}\_{t}-v^{h}\_{t})dW^{h}\_{t},\ \hat{x}^{h}\_{0}-x^{h}\_{0}=0. |  |

By applying Itô’s lemma to pth​(x^th−xth)p^{h}\_{t}(\hat{x}^{h}\_{t}-x^{h}\_{t}), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[pTh​(x^Th−xTh)]\displaystyle\mathbb{E}\left[p^{h}\_{T}(\hat{x}^{h}\_{T}-x^{h}\_{T})\right] | =𝔼[∫0T[pth(r(x^th−xth)−κh(v^th−vth))\displaystyle=\mathbb{E}\Bigg[\int\_{0}^{T}\bigg[p^{h}\_{t}\left(r(\hat{x}^{h}\_{t}-x^{h}\_{t})-\kappa^{h}(\hat{v}^{h}\_{t}-v^{h}\_{t})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(x^th−xth)(rpth−fxh(t,xth,zth,vth,v¯th))−σhηth(v^th−vth)]dt]\displaystyle\qquad-(\hat{x}^{h}\_{t}-x^{h}\_{t})\left(rp^{h}\_{t}-f^{h}\_{x}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})\right)-\sigma^{h}\eta^{h}\_{t}(\hat{v}^{h}\_{t}-v^{h}\_{t})\bigg]dt\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T(fxh​(t,xth,zth,vth,v¯th)​(x^th−xth)−(κh​pth+σh​ηth)​(v^th−vth))​𝑑t].\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(f^{h}\_{x}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})(\hat{x}^{h}\_{t}-x^{h}\_{t})-\left(\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right)\left(\hat{v}^{h}\_{t}-v^{h}\_{t}\right)\right)dt\right]. |  |

Substituting this into ([C.2](https://arxiv.org/html/2511.12292v1#A3.Ex185 "C.2 Proof of Theorem 3.1 ‣ Appendix C Proofs of Assertions in Section 3 ‣ Mean Field Analysis of Mutual Insurance Market")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jh​(v^h)−Jh​(vh)\displaystyle J^{h}(\hat{v}^{h})-J^{h}(v^{h}) | ≤𝔼​[∫0T(fvh​(t,xth,zth,vth,v¯th)+κh​pth+σh​ηth)​(v^th−vth)​𝑑t].\displaystyle\leq\mathbb{E}\Bigg[\int\_{0}^{T}\left(f^{h}\_{v}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})+\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right)\left(\hat{v}^{h}\_{t}-v^{h}\_{t}\right)dt\Bigg]. |  |

Hence, we derive the variational inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T(fvh​(t,xth,zth,vth,v¯th)+κh​pth+σh​ηth)​(v^th−vth)​𝑑t]≤0,\mathbb{E}\Bigg[\int\_{0}^{T}\left(f^{h}\_{v}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})+\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right)\left(\hat{v}^{h}\_{t}-v^{h}\_{t}\right)dt\Bigg]\leq 0, |  | (56) |

which implies Jh​(v^h)<Jh​(vh)J^{h}(\hat{v}^{h})<J^{h}(v^{h}). The arbitrariness of v^h\hat{v}^{h} then suggests that vhv^{h} is indeed the optimal control, whose existence is warranted by Lemma [3.1](https://arxiv.org/html/2511.12292v1#S3.Thmlemma1 "Lemma 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market").

Notice that ([56](https://arxiv.org/html/2511.12292v1#A3.E56 "In C.2 Proof of Theorem 3.1 ‣ Appendix C Proofs of Assertions in Section 3 ‣ Mean Field Analysis of Mutual Insurance Market")) holds if

|  |  |  |  |
| --- | --- | --- | --- |
|  | (fvh​(t,xth,zth,vth,v¯th)+κh​pth+σh​ηth)​(v^th−vth)≤0\left(f^{h}\_{v}(t,x^{h}\_{t},z^{h}\_{t},v^{h}\_{t},\bar{v}^{h}\_{t})+\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right)\left(\hat{v}^{h}\_{t}-v^{h}\_{t}\right)\leq 0 |  | (57) |

for all t∈[0,T]t\in[0,T]. Since v↦fvh​(t,x,z,⋅,v¯)v\mapsto f^{h}\_{v}(t,x,z,\cdot,\bar{v}) is strictly decreasing, the above inequality holds iff

|  |  |  |  |
| --- | --- | --- | --- |
|  | [(fvh)−1​(−(κh​pth+σh​ηth);t,xth,zth,v¯th)−vth]​(v^th−vth)≤0.\left[(f^{h}\_{v})^{-1}\left(-\left(\kappa^{h}p^{h}\_{t}+\sigma^{h}\eta^{h}\_{t}\right);t,x^{h}\_{t},z^{h}\_{t},\bar{v}^{h}\_{t}\right)-v^{h}\_{t}\right]\left(\hat{v}^{h}\_{t}-v^{h}\_{t}\right)\leq 0. |  | (58) |

By Lemma [A.1](https://arxiv.org/html/2511.12292v1#A1.Thmlemma1 "Lemma A.1. ‣ Appendix A Auxiliary Lemmas ‣ Mean Field Analysis of Mutual Insurance Market"), we conclude that the solution of the inequality is given by ([12](https://arxiv.org/html/2511.12292v1#S3.E12 "In Theorem 3.1. ‣ 3 Optimal Mean Field Insurance Strategy ‣ Mean Field Analysis of Mutual Insurance Market")).

## Appendix D Proofs of Assertions in Section [4](https://arxiv.org/html/2511.12292v1#S4 "4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")

This section contains the proofs of statements in Section [4](https://arxiv.org/html/2511.12292v1#S4 "4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market").

### D.1 Proof of Proposition [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")

We shall need the following lemmas:

###### Lemma D.1.

For any 𝐚,𝐛∈ℝd{\bf a},{\bf b}\in\mathbb{R}^{d},

|  |  |  |
| --- | --- | --- |
|  | λmin​(𝐚𝐛⊤+𝐛𝐚⊤)=𝐛⊤​𝐚−|𝐚|​|𝐛|​ and ​λmax​(𝐚𝐛⊤+𝐛𝐚⊤)=𝐛⊤​𝐚+|𝐚|​|𝐛|.\lambda\_{\min}({\bf a}{\bf b}^{\top}+{\bf b}{\bf a}^{\top})={\bf b}^{\top}{\bf a}-|{\bf a}||{\bf b}|\text{ and }\lambda\_{\max}({\bf a}{\bf b}^{\top}+{\bf b}{\bf a}^{\top})={\bf b}^{\top}{\bf a}+|{\bf a}||{\bf b}|. |  |

###### Proof.

Let 𝐔:=𝐚𝐛⊤+𝐛𝐚⊤{\bf U}:={\bf a}{\bf b}^{\top}+{\bf b}{\bf a}^{\top}. If either 𝐚{\bf a} or 𝐛{\bf b} is the zero vector, the claim is clearly true. Henceforth, we assume that both 𝐚{\bf a} and 𝐛{\bf b} are non-zero column vectors.

Case 1: 𝐚{\bf a} and 𝐛{\bf b} are linearly dependent
  
In this case, there exists a non-zero constant cc such that 𝐛=c​𝐚{\bf b}=c{\bf a}. Hence, 𝐔=2​c​𝐚𝐚⊤{\bf U}=2c{\bf a}{\bf a}^{\top} and 𝐔{\bf U} has at most one non-zero eigenvalue, 2​c​|𝐚|22c|{\bf a}|^{2}. If c>0c>0,

|  |  |  |
| --- | --- | --- |
|  | λmin​(𝐔)=0=𝐛⊤​𝐚−|𝐚|​|𝐛|,λmax​(𝐔)=2​c​|𝐚|2=c​|𝐚|2+|c|​|𝐚|2=𝐛⊤​𝐚+|𝐚|​|𝐛|.\displaystyle\lambda\_{\min}({\bf U})=0={\bf b}^{\top}{\bf a}-|{\bf a}||{\bf b}|,\ \lambda\_{\max}({\bf U})=2c|{\bf a}|^{2}=c|{\bf a}|^{2}+|c||{\bf a}|^{2}={\bf b}^{\top}{\bf a}+|{\bf a}||{\bf b}|. |  |

If c<0c<0,

|  |  |  |
| --- | --- | --- |
|  | λmin​(𝐔)=2​c​|𝐚|2=c​|𝐚|2−|c|​|𝐚|2=𝐛⊤​𝐚−|𝐚|​|𝐛|,λmax​(𝐔)=0=𝐛⊤​𝐚+|𝐚|​|𝐛|.\displaystyle\lambda\_{\min}({\bf U})=2c|{\bf a}|^{2}=c|{\bf a}|^{2}-|c||{\bf a}|^{2}={\bf b}^{\top}{\bf a}-|{\bf a}||{\bf b}|,\ \lambda\_{\max}({\bf U})=0={\bf b}^{\top}{\bf a}+|{\bf a}||{\bf b}|. |  |

Case 2: 𝐚{\bf a} and 𝐛{\bf b} are linearly independent
  
Let 𝒮:=span​{𝐚,𝐛}\mathcal{S}:=\text{span}\{{\bf a},{\bf b}\} and 𝒮⟂\mathcal{S}^{\perp} be its orthogonal complement. Since 𝐚{\bf a} and 𝐛{\bf b} are column vectors, we have rank​(𝐔)≤2\text{rank}({\bf U})\leq 2 which implies that 𝐔{\bf U} has at most two non-zero eigenvalues. Note that, for any 𝐱∈𝒮⟂{\bf x}\in\mathcal{S}^{\perp}, we have 𝐔𝐱=0{\bf U}{\bf x}=0. Therefore, the eigenvectors corresponding to the non-zero eigenvalues of 𝐔{\bf U} belong to 𝒮\mathcal{S}. Since

|  |  |  |
| --- | --- | --- |
|  | 𝐔𝐚=𝐚𝐛⊤​𝐚+𝐛​|𝐚|2​ and ​𝐔𝐛=𝐚​|𝐛|2+𝐛𝐚⊤​𝐛,{\bf U}{\bf a}={\bf a}{\bf b}^{\top}{\bf a}+{\bf b}|{\bf a}|^{2}\text{ and }{\bf U}{\bf b}={\bf a}|{\bf b}|^{2}+{\bf b}{\bf a}^{\top}{\bf b}, |  |

the linear transform 𝐔{\bf U} in the basis {𝐚,𝐛}\{{\bf a},{\bf b}\} can be represented as a 2×22\times 2 matrix 𝐔𝐚,𝐛{\bf U}\_{{\bf a},{\bf b}}, where

|  |  |  |
| --- | --- | --- |
|  | 𝐔𝐚,𝐛=(𝐛⊤​𝐚|𝐛|2|𝐚|2𝐚⊤​𝐛).{\bf U}\_{{\bf a},{\bf b}}=\begin{pmatrix}{\bf b}^{\top}{\bf a}&|{\bf b}|^{2}\\ |{\bf a}|^{2}&{\bf a}^{\top}{\bf b}\end{pmatrix}. |  |

The characteristic equation for 𝐔𝐚,𝐛{\bf U}\_{{\bf a},{\bf b}} is (𝐛⊤​𝐚−λ)2−|𝐚|2​|𝐛|2=0({\bf b}^{\top}{\bf a}-\lambda)^{2}-|{\bf a}|^{2}|{\bf b}|^{2}=0, which has solutions λ±=𝐛⊤​𝐚±|𝐚|​|𝐛|\lambda\_{\pm}={\bf b}^{\top}{\bf a}\pm|{\bf a}||{\bf b}|. By the Cauchy-Schwarz inequality, we have λ−≤0≤λ+\lambda\_{-}\leq 0\leq\lambda\_{+}. Therefore, λmin​(𝐔)=λ−=𝐛⊤​𝐚−|𝐚|​|𝐛|\lambda\_{\min}({\bf U})=\lambda\_{-}={\bf b}^{\top}{\bf a}-|{\bf a}||{\bf b}| and λmax​(𝐔)=λ+=𝐛⊤​𝐚+|𝐚|​|𝐛|\lambda\_{\max}({\bf U})=\lambda\_{+}={\bf b}^{\top}{\bf a}+|{\bf a}||{\bf b}|.

The desired result follows by combining the two cases.
∎

###### Lemma D.2.

Conditions 1-3 in Proposition [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") are equivalent.

###### Proof.

We first prove the equivalence of Conditions 1 and 3.
Using the identity 𝐈−𝐌⊤=𝐊​(𝐊−𝚷)−1{\bf I}-{\bf M}^{\top}={\bf K}({\bf K}-{\bf\Pi})^{-1} and ([18](https://arxiv.org/html/2511.12292v1#S4.E18 "In 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐈−𝐌⊤=𝐈+𝝅​𝝊⊤​𝐊−11−𝝊⊤​𝐊−1​𝝅,{\bf I}-{\bf M}^{\top}={\bf I}+\frac{\boldsymbol{\pi}\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}}{1-\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}\boldsymbol{\pi}}, |  | (59) |

where 𝝅\boldsymbol{\pi} and 𝝊\boldsymbol{\upsilon} are defined as in ([17](https://arxiv.org/html/2511.12292v1#S4.E17 "In 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")). By considering the symmetrization of 𝐈−𝐌⊤{\bf I}-{\bf M}^{\top}, we have

|  |  |  |
| --- | --- | --- |
|  | λmin​(𝐈−𝐌)=λmin​(𝐈−𝐌⊤)=1+λmin​(𝝅​𝝊⊤​𝐊−1+𝐊−1​𝝊​𝝅⊤)2−2​𝝊⊤​𝐊−1​𝝅.\lambda\_{\min}({\bf I}-{\bf M})=\lambda\_{\min}({\bf I}-{\bf M}^{\top})=1+\frac{\lambda\_{\min}(\boldsymbol{\pi}\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}+{\bf K}^{-1}\boldsymbol{\upsilon}\boldsymbol{\pi}^{\top})}{2-2\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}\boldsymbol{\pi}}. |  |

By Lemma [D.1](https://arxiv.org/html/2511.12292v1#A4.Thmlemma1 "Lemma D.1. ‣ D.1 Proof of Proposition 4.1 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | λmin​(𝝅​𝝊⊤​𝐊−1+𝐊−1​𝝊​𝝅⊤)\displaystyle\lambda\_{\min}(\boldsymbol{\pi}\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}+{\bf K}^{-1}\boldsymbol{\upsilon}\boldsymbol{\pi}^{\top}) | =𝝊⊤​𝐊−1​𝝅−|𝝅|​|𝐊−1​𝝊|\displaystyle=\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}\boldsymbol{\pi}-|\boldsymbol{\pi}||{\bf K}^{-1}\boldsymbol{\upsilon}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑h=1Hπh​ωh​κh−dκh−(∑h=1H(πh)2)​(∑h=1H(ωh​κh−dκh)2).\displaystyle=\sum\_{h=1}^{H}\pi^{h}\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}-\sqrt{\left(\sum\_{h=1}^{H}(\pi^{h})^{2}\right)\left(\sum\_{h=1}^{H}\left(\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}\right)^{2}\right)}. |  |

Thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | λmin​(𝐈−𝐌⊤)=2−∑h=1Hπh​ωh​κh−dκh−(∑h=1H(πh)2)​(∑h=1H(ωh​κh−dκh)2)2−2​∑h=1Hπh​ωh​κh−dκh,\lambda\_{\min}\left({\bf I}-{\bf M}^{\top}\right)=\frac{2-\sum\_{h=1}^{H}\pi^{h}\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}-\sqrt{\left(\sum\_{h=1}^{H}(\pi^{h})^{2}\right)\left(\sum\_{h=1}^{H}\left(\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}\right)^{2}\right)}}{2-2\sum\_{h=1}^{H}\pi^{h}\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}}, |  | (60) |

where the denominator 2−2​∑h=1Hπh​ωh​κh−dκh>02-2\sum\_{h=1}^{H}\pi^{h}\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}>0, since κh>d≥0\kappa^{h}>d\geq 0 for all h∈[H]h\in[H], and ∑h=1Hπh​ωh=1\sum\_{h=1}^{H}\pi^{h}\omega^{h}=1. It is then easy to see λmin​(𝐈−𝐌⊤)>0\lambda\_{\min}\left({\bf I}-{\bf M}^{\top}\right)>0 if and only if Condition 3 holds.

Next, we prove the equivalence of Conditions 2 and 3.
Using Lemma [D.1](https://arxiv.org/html/2511.12292v1#A4.Thmlemma1 "Lemma D.1. ‣ D.1 Proof of Proposition 4.1 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 2​λmax​(𝚷​𝐊−1)=λmax​(𝝅​𝝊⊤​𝐊−1+𝐊−1​𝝊​𝝅⊤)=𝝊⊤​𝐊−1​𝝅+|𝐊−1​𝝊|​|𝝅|\displaystyle 2\lambda\_{\max}({\bf\Pi}{\bf K}^{-1})=\lambda\_{\max}(\boldsymbol{\pi}\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}+{\bf K}^{-1}\boldsymbol{\upsilon}\boldsymbol{\pi}^{\top})=\boldsymbol{\upsilon}^{\top}{\bf K}^{-1}\boldsymbol{\pi}+|{\bf K}^{-1}\boldsymbol{\upsilon}||\boldsymbol{\pi}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑h=1Hπh​ωh​κh−dκh+(∑h=1H(πh)2)​(∑h=1H(ωh​κh−dκh)2).\displaystyle\sum\_{h=1}^{H}\pi^{h}\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}+\sqrt{\left(\sum\_{h=1}^{H}(\pi^{h})^{2}\right)\left(\sum\_{h=1}^{H}\left(\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}\right)^{2}\right)}. |  |

Therefore, λmax​(𝚷​𝐊−1)<1\lambda\_{\max}({\bf\Pi}{\bf K}^{-1})<1 if and only if Condition 3 holds.
∎

###### Lemma D.3.

Condition 4 of Proposition [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market") implies Conditions 1-3 of the same proposition.

###### Proof.

Given Condition 4 of Proposition [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), there exists a c>0c>0 such that πhωh<c<πhωh​κhκh−d\frac{\pi^{h}}{\omega^{h}}<c<\frac{\pi^{h}}{\omega^{h}}\frac{\kappa^{h}}{\kappa^{h}-d} for all h∈[H]h\in[H]. Let δh:=πhc​ωh\delta^{h}:=\frac{\pi^{h}}{c\omega^{h}}, which satisfies κh−dκh<δh<1\frac{\kappa^{h}-d}{\kappa^{h}}<\delta^{h}<1. Hence, we have

|  |  |  |
| --- | --- | --- |
|  | ∑h=1Hπh​ωh​κh−dκh+(∑h=1H(πh)2)​(∑h=1H(ωh​κh−dκh)2)\displaystyle\ \ \ \ \sum\_{h=1}^{H}\pi^{h}\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}+\sqrt{\left(\sum\_{h=1}^{H}(\pi^{h})^{2}\right)\left(\sum\_{h=1}^{H}\left(\omega^{h}\frac{\kappa^{h}-d}{\kappa^{h}}\right)^{2}\right)} |  |
|  |  |  |
| --- | --- | --- |
|  | <∑h=1Hπh​ωh​δh+(∑h=1H(πh)2)​(∑h=1H(ωh​δh)2).\displaystyle<\sum\_{h=1}^{H}\pi^{h}\omega^{h}\delta^{h}+\sqrt{\left(\sum\_{h=1}^{H}(\pi^{h})^{2}\right)\left(\sum\_{h=1}^{H}\left(\omega^{h}\delta^{h}\right)^{2}\right)}. |  |

By the Cauchy–Schwarz inequality and the fact that πh=c​ωh​δh\pi^{h}=c\omega^{h}\delta^{h}, we have

|  |  |  |
| --- | --- | --- |
|  | ∑h=1Hπh​ωh​δh+(∑h=1H(πh)2)​(∑h=1H(ωh​δh)2)=2​∑h=1Hπh​ωh​δh<2​∑h=1Hπh​ωh=2.\displaystyle\sum\_{h=1}^{H}\pi^{h}\omega^{h}\delta^{h}+\sqrt{\left(\sum\_{h=1}^{H}(\pi^{h})^{2}\right)\left(\sum\_{h=1}^{H}\left(\omega^{h}\delta^{h}\right)^{2}\right)}=2\sum\_{h=1}^{H}\pi^{h}\omega^{h}\delta^{h}<2\sum\_{h=1}^{H}\pi^{h}\omega^{h}=2. |  |

Therefore, Condition 4 implies Condition 3. By Lemma [D.2](https://arxiv.org/html/2511.12292v1#A4.Thmlemma2 "Lemma D.2. ‣ D.1 Proof of Proposition 4.1 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market"), the proof is complete.
∎

### D.2 Proof of Lemma [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmlemma2 "Lemma 4.2. ‣ 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")

For μ∈[0,1]\mu\in[0,1], we define the operator Ψμ+δ​(𝐱,𝐩,𝜼)=(𝐱^,𝐩^,𝜼^)\Psi\_{\mu+\delta}({\bf x},{\bf p},\boldsymbol{\eta})=(\hat{\bf x},\hat{\bf p},\hat{\boldsymbol{\eta}}), where the latter is the solution of the parametrized system ([30](https://arxiv.org/html/2511.12292v1#S4.E30 "In 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt\displaystyle\boldsymbol{\phi}\_{t} | =δ(𝐩t+(r𝐱t+𝐥−𝐊𝐯t+𝚷𝔼[𝐯t])+ϕ^t,\displaystyle=\delta\left({\bf p}\_{t}+(r{\bf x}\_{t}+{\bf l}-{\bf K}{\bf v}\_{t}+{\bf\Pi}\mathbb{E}[{\bf v}\_{t}]\right)+\hat{\boldsymbol{\phi}}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝍t\displaystyle\boldsymbol{\psi}\_{t} | =δ​(diag​(𝜼t)+𝚺​(𝐈−diag​(𝐯t)))+𝝍^t,\displaystyle=\delta\left(\text{diag}(\boldsymbol{\eta}\_{t})+{\bf\Sigma}({\bf I}-\text{diag}({\bf v}\_{t}))\right)+\hat{\boldsymbol{\psi}}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝃t\displaystyle\boldsymbol{\xi}\_{t} | =δ​(−𝐱t+r​𝐩t−∂𝐱𝐅​(t,𝐱t,𝐳t,𝐯t,𝔼​[𝐯t]))+𝝃^t,\displaystyle=\delta\left(-{\bf x}\_{t}+r{\bf p}\_{t}-\partial\_{\bf x}{\bf F}(t,{\bf x}\_{t},{\bf z}\_{t},{\bf v}\_{t},\mathbb{E}[{\bf v}\_{t}])\right)+\hat{\boldsymbol{\xi}}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜻T\displaystyle\boldsymbol{\zeta}\_{T} | =−δ​[∂𝐱𝐆​(𝐱T,𝐳T)+𝐱T]+𝜻^T,\displaystyle=-\delta\left[\partial\_{\bf x}{\bf G}({\bf x}\_{T},{\bf z}\_{T})+{\bf x}\_{T}\right]+\hat{\boldsymbol{\zeta}}\_{T}, |  |

Here, δ>0\delta>0 is a small positive constant to be chosen independently of μ\mu, ϕ^,𝝃^∈L𝔽[H]2​([0,T];ℝH)\hat{\boldsymbol{\phi}},\hat{\boldsymbol{\xi}}\in L^{2}\_{\mathbb{F}^{[H]}}([0,T];\mathbb{R}^{H}), 𝝍^∈L𝔽h2​([0,T];ℝH×ℝH)\hat{\boldsymbol{\psi}}\in L^{2}\_{\mathbb{F}^{h}}([0,T];\mathbb{R}^{H}\times\mathbb{R}^{H}), 𝜻^T∈L2​(Ω,ℱT,ℙ)\hat{\boldsymbol{\zeta}}\_{T}\in L^{2}(\Omega,\mathcal{F}\_{T},\mathbb{P}), and (𝐳t)t∈[0,T]({\bf z}\_{t})\_{t\in[0,T]}, (𝐯t)t∈[0,T]({\bf v}\_{t})\_{t\in[0,T]} are given by

|  |  |  |
| --- | --- | --- |
|  | 𝐳t=𝔼​[𝐱t],𝐯t=ProjIH​[(∂𝐯𝐅)−1​(−(𝐊𝐩t+𝚺​𝜼t);t,𝐱t,𝐳t,𝔼​[𝐯t])].{\bf z}\_{t}=\mathbb{E}[{\bf x}\_{t}],\ {\bf v}\_{t}=\text{Proj}\_{I^{H}}\left[\left(\partial\_{\bf v}{\bf F}\right)^{-1}\left(-\left({\bf K}{\bf p}\_{t}+{\bf\Sigma}\boldsymbol{\eta}\_{t}\right);t,{\bf x}\_{t},{\bf z}\_{t},\mathbb{E}[{\bf v}\_{t}]\right)\right]. |  |

Suppose that the system ([30](https://arxiv.org/html/2511.12292v1#S4.E30 "In 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) admits a solution for some μ0∈[0,1)\mu\_{0}\in[0,1). Let Ψμ0+δ​(𝐱i,𝐩i,𝜼i)=(𝐱^i,𝐩^i,𝜼^i)\Psi\_{\mu\_{0}+\delta}({\bf x}^{i},{\bf p}^{i},\boldsymbol{\eta}^{i})=(\hat{\bf x}^{i},\hat{\bf p}^{i},\hat{\boldsymbol{\eta}}^{i}), i=1,2i=1,2. Let also 𝐱~:=𝐱1−𝐱2\tilde{{\bf x}}:={\bf x}^{1}-{\bf x}^{2}, 𝐩~:=𝐩1−𝐩2\tilde{{\bf p}}:={\bf p}^{1}-{\bf p}^{2}, 𝜼~:=𝜼1−𝜼2\tilde{\boldsymbol{\eta}}:=\boldsymbol{\eta}^{1}-\boldsymbol{\eta}^{2}, 𝐯~:=𝐯1−𝐯2\tilde{{\bf v}}:={\bf v}^{1}-{\bf v}^{2}; 𝐱^~:=𝐱^1−𝐱^2\tilde{\hat{{\bf x}}}:=\hat{{\bf x}}^{1}-\hat{{\bf x}}^{2}, 𝐩^~:=𝐩^1−𝐩^2\tilde{\hat{{\bf p}}}:=\hat{{\bf p}}^{1}-\hat{{\bf p}}^{2}, 𝜼^~:=𝜼^1−𝜼^2\tilde{\hat{\boldsymbol{\eta}}}:=\hat{\boldsymbol{\eta}}^{1}-\hat{\boldsymbol{\eta}}^{2}, 𝐯^~:=𝐯^1−𝐯^2\tilde{\hat{{\bf v}}}:=\hat{{\bf v}}^{1}-\hat{{\bf v}}^{2}. We shall show that Ψμ0+δ\Psi\_{\mu\_{0}+\delta} is a contraction for any sufficiently small δ>0\delta>0 independent of μ0\mu\_{0}. Consequently, by the Banach fixed point theorem, one can deduce that the operator Ψμ0+δ\Psi\_{\mu\_{0}+\delta} admits a fixed point, which is indeed the solution of ([30](https://arxiv.org/html/2511.12292v1#S4.E30 "In 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) with μ=μ0+δ\mu=\mu\_{0}+\delta.

By applying Itô’s lemma to ⟨𝐱^~t,𝐩^~t⟩\langle\tilde{\hat{{\bf x}}}\_{t},\tilde{\hat{{\bf p}}}\_{t}\rangle and using Assumption [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | μ0​𝔼​[⟨𝐱^~T,−(∂𝐱𝐆​(𝐱^T1,𝐳^T1)−∂𝐱𝐆​(𝐱^T2,𝐳^T2))⟩]+(1−μ0)​𝔼​[|𝐱^~T|2]\displaystyle\mu\_{0}\mathbb{E}\left[\left\langle\tilde{\hat{{\bf x}}}\_{T},-\left(\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{1}\_{T},\hat{{\bf z}}^{1}\_{T})-\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{2}\_{T},\hat{{\bf z}}^{2}\_{T})\right)\right\rangle\right]+(1-\mu\_{0})\mathbb{E}\left[\left|\tilde{\hat{{\bf x}}}\_{T}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −δ​𝔼​[⟨𝐱^~T,(∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2))+𝐱~T⟩]\displaystyle\quad-\delta\mathbb{E}\left[\left\langle\tilde{\hat{{\bf x}}}\_{T},\left(\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})\right)+\tilde{{\bf x}}\_{T}\right\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μ0​𝔼​[∫0T⟨𝐱^~t,∂𝐱𝐅​(𝐱^t1,𝐳^t1,𝐯^t1,𝔼​[𝐯^t1])−∂𝐱𝐅​(𝐱^t2,𝐳^t2,𝐯^t2,𝔼​[𝐯^t2])⟩​𝑑t]\displaystyle=\mu\_{0}\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf x}}}\_{t},\partial\_{\bf x}{\bf F}(\hat{{\bf x}}^{1}\_{t},\hat{{\bf z}}^{1}\_{t},\hat{{\bf v}}^{1}\_{t},\mathbb{E}[\hat{{\bf v}}^{1}\_{t}])-\partial\_{\bf x}{\bf F}(\hat{{\bf x}}^{2}\_{t},\hat{{\bf z}}^{2}\_{t},\hat{{\bf v}}^{2}\_{t},\mathbb{E}[\hat{{\bf v}}^{2}\_{t}])\right\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −μ0​𝔼​[∫0T⟨𝐯^~t,𝐊​𝐩^~t+𝚺​𝜼^~t⟩​𝑑t]+μ0​𝔼​[∫0T⟨𝐩^~t,𝚷​𝔼​[𝐯^~t]⟩​𝑑t]\displaystyle\ -\mu\_{0}\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf v}}}\_{t},{\bf K}\tilde{\hat{{\bf p}}}\_{t}+{\bf\Sigma}\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right\rangle dt\right]+\mu\_{0}\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf p}}}\_{t},{\bf\Pi}\mathbb{E}[\tilde{\hat{{\bf v}}}\_{t}]\right\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1−μ0)​𝔼​[∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝜼^~t|2)​𝑑t]\displaystyle\ -(1-\mu\_{0})\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −δ​𝔼​[∫0T⟨𝐱^~t,−𝐱~t+r​𝐩~t−(∂𝐱𝐅​(𝐱t1,𝐳t1,𝐯t1,𝔼​[𝐯t1])−∂𝐱𝐅​(𝐱t1,𝐳t1,𝐯t1,𝔼​[𝐯t1]))⟩​𝑑t]\displaystyle\ -\delta\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf x}}}\_{t},-\tilde{{\bf x}}\_{t}+r\tilde{{\bf p}}\_{t}-\left(\partial\_{\bf x}{\bf F}({\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\mathbb{E}[{\bf v}^{1}\_{t}])-\partial\_{\bf x}{\bf F}({\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\mathbb{E}[{\bf v}^{1}\_{t}])\right)\right\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ​𝔼​[∫0T⟨𝐩^~t,𝐩~t+r​𝐱~t−𝐊​𝐯~t+𝚷​𝔼​[𝐯~t]⟩​𝑑t]+δ​𝔼​[∫0T⟨𝜼^~t,𝜼~t−𝚺​𝐯~t⟩​𝑑t]\displaystyle\ +\delta\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf p}}}\_{t},\tilde{{\bf p}}\_{t}+r\tilde{{\bf x}}\_{t}-{\bf K}\tilde{{\bf v}}\_{t}+{\bf\Pi}\mathbb{E}[\tilde{{\bf v}}\_{t}]\right\rangle dt\right]+\delta\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{\boldsymbol{\eta}}}\_{t},\tilde{\boldsymbol{\eta}}\_{t}-{\bf\Sigma}\tilde{{\bf v}}\_{t}\right\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤μ0​𝔼​[∫0T⟨𝐱^~t,∇𝐅𝐱​(𝐱^t1,𝐳^t1,𝐯^t1,𝔼​[𝐯^t1])−∇𝐅𝐱​(𝐱^t2,𝐳^t2,𝐯^t2,𝔼​[𝐯^t2])⟩​𝑑t]\displaystyle\leq\mu\_{0}\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf x}}}\_{t},\nabla{\bf F}\_{\bf x}(\hat{{\bf x}}^{1}\_{t},\hat{{\bf z}}^{1}\_{t},\hat{{\bf v}}^{1}\_{t},\mathbb{E}[\hat{{\bf v}}^{1}\_{t}])-\nabla{\bf F}\_{\bf x}(\hat{{\bf x}}^{2}\_{t},\hat{{\bf z}}^{2}\_{t},\hat{{\bf v}}^{2}\_{t},\mathbb{E}[\hat{{\bf v}}^{2}\_{t}])\right\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −μ0​𝔼​[∫0T⟨𝐯^~t,𝐊​𝐩^~t+𝚺​𝜼^~t⟩​𝑑t]+μ0​𝔼​[∫0T⟨𝐩^~t,𝚷​𝔼​[𝐯^~t]⟩​𝑑t]\displaystyle\ -\mu\_{0}\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf v}}}\_{t},{\bf K}\tilde{\hat{{\bf p}}}\_{t}+{\bf\Sigma}\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right\rangle dt\right]+\mu\_{0}\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf p}}}\_{t},{\bf\Pi}\mathbb{E}[\tilde{\hat{{\bf v}}}\_{t}]\right\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1−μ0)​𝔼​[∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝜼^~t|2)​𝑑t]\displaystyle\ -(1-\mu\_{0})\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}\right)dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +KT​δ​(𝔼​[∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝜼^~t|2+|𝐱~t|2+|𝐩~t|2+|𝜼~t|2)​𝑑t]),\displaystyle\ +K\_{T}\delta\left(\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}+\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{\boldsymbol{\eta}}\_{t}\right|^{2}\right)dt\right]\right), |  | (61) |

where KT>0K\_{T}>0 is a generic constant depending solely on TT, which changes from line to line in the subsequent calculations.

We estimate the terms on the right-hand side of ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex212 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")). Following the proof of ([23](https://arxiv.org/html/2511.12292v1#S4.E23 "In 4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")) in Theorem [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), one can show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T⟨𝐯^~t,𝐊​𝐩^~t+𝚺​𝜼^~t⟩​𝑑t]≥0.\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf v}}}\_{t},{\bf K}\tilde{\hat{{\bf p}}}\_{t}+{\bf\Sigma}\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right\rangle dt\right]\geq 0. |  | (62) |

Next, we estimate the term

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T⟨𝐩^~t,𝚷​𝔼​[𝐯^~t]⟩​𝑑t].\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf p}}}\_{t},{\bf\Pi}\mathbb{E}[\tilde{\hat{{\bf v}}}\_{t}]\right\rangle dt\right]. |  |

By considering the dynamics of ⟨𝐌​𝐳^~t,𝔼​[𝐩^~t]⟩\langle{\bf M}\tilde{\hat{\bf z}}\_{t},\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}]\rangle, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | μ0​𝔼​[⟨𝐌​𝐳^~T,−(∂𝐱𝐆​(𝐱^T1,𝐱^T1)−∂𝐱𝐆​(𝐱^T2,𝐱^T2))⟩]+(1−μ0)​⟨𝐌​𝐳^~T,𝐳^~T⟩\displaystyle\ \mu\_{0}\mathbb{E}\left[\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{T},-\left(\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{1}\_{T},\hat{{\bf x}}^{1}\_{T})-\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{2}\_{T},\hat{{\bf x}}^{2}\_{T})\right)\right\rangle\right]+(1-\mu\_{0})\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{T},\tilde{\hat{{\bf z}}}\_{T}\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ​𝔼​[⟨𝐌​𝐳^~T,−(∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)+𝐳~T)⟩]\displaystyle\quad+\delta\mathbb{E}\left[\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{T},-\left(\partial\_{{\bf x}}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{{\bf x}}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})+\tilde{{\bf z}}\_{T}\right)\right\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −(1−μ0)​∫0T(⟨𝐌​𝔼​[𝐩^~t],𝔼​[𝐩^~t]⟩+⟨𝐌​𝐳^~t,𝐳^~t⟩)​𝑑t\displaystyle\ -(1-\mu\_{0})\int\_{0}^{T}\left(\left\langle{\bf M}\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}]\right\rangle+\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},\tilde{\hat{{\bf z}}}\_{t}\right\rangle\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +μ0​∫0T⟨𝔼​[𝐩^~t],𝚷​𝔼​[𝐯^~t]⟩​𝑑t\displaystyle\quad+\mu\_{0}\int\_{0}^{T}\left\langle\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],{\bf\Pi}\mathbb{E}[\tilde{\hat{\bf v}}\_{t}]\right\rangle dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −μ0​∫0T⟨𝐌​𝐳^~t,−(∂𝐱𝐅​(t,𝐱^t1,𝐳^t1,𝐯^t1,𝔼​[𝐯^t1])−∂𝐱𝐅​(t,𝐱^t2,𝐳^t2,𝐯^t2,𝔼​[𝐯^t2]))⟩​𝑑t\displaystyle\ -\mu\_{0}\int\_{0}^{T}\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},-\left(\partial\_{{\bf x}}{\bf F}(t,\hat{{\bf x}}^{1}\_{t},\hat{{\bf z}}^{1}\_{t},\hat{{\bf v}}^{1}\_{t},\mathbb{E}[\hat{{\bf v}}^{1}\_{t}])-\partial\_{{\bf x}}{\bf F}(t,\hat{{\bf x}}^{2}\_{t},\hat{{\bf z}}^{2}\_{t},\hat{{\bf v}}^{2}\_{t},\mathbb{E}[\hat{{\bf v}}^{2}\_{t}])\right)\right\rangle dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ∫0T(⟨𝔼[𝐩^~t],𝐌(𝔼[𝐩~t]+r𝐳~t+𝚷𝔼[𝐯~t])⟩\displaystyle\ +\delta\int\_{0}^{T}\bigg(\left\langle\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],{\bf M}\left(\mathbb{E}[\tilde{{\bf p}}\_{t}]+r\tilde{{\bf z}}\_{t}+{\bf\Pi}\mathbb{E}[\tilde{{\bf v}}\_{t}]\right)\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +⟨𝐌𝐳^~t,𝐳~t−r𝔼[𝐩~t]+∂𝐱𝐅(𝐱t1,𝐳t1,𝐯t1,𝔼[𝐯t1])−∂𝐱𝐅(𝐱t1,𝐳t1,𝐯t1,𝔼[𝐯t1])⟩)dt\displaystyle\qquad+\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},\tilde{{\bf z}}\_{t}-r\mathbb{E}[\tilde{\bf p}\_{t}]+\partial\_{\bf x}{\bf F}({\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\mathbb{E}[{\bf v}^{1}\_{t}])-\partial\_{\bf x}{\bf F}({\bf x}^{1}\_{t},{\bf z}^{1}\_{t},{\bf v}^{1}\_{t},\mathbb{E}[{\bf v}^{1}\_{t}])\right\rangle\bigg)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | −(1−μ0)​∫0T(⟨𝐌​𝔼​[𝐩^~t],𝔼​[𝐩^~t]⟩+⟨𝐌​𝐳^~t,𝐳^~t⟩)​𝑑t\displaystyle\ -(1-\mu\_{0})\int\_{0}^{T}\left(\left\langle{\bf M}\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}]\right\rangle+\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},\tilde{\hat{{\bf z}}}\_{t}\right\rangle\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +μ0​∫0T⟨𝔼​[𝐩^~t],𝚷​𝔼​[𝐯^~t]⟩​𝑑t\displaystyle\ +\mu\_{0}\int\_{0}^{T}\left\langle\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],{\bf\Pi}\mathbb{E}[\tilde{\hat{\bf v}}\_{t}]\right\rangle dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −μ0​∫0T⟨𝐌​𝐳^~t,−𝔼​[∂𝐱𝐅​(t,𝐱^t1,𝐳^t1,𝐯^t1,𝔼​[𝐯^t1])−∂𝐱𝐅​(t,𝐱^t2,𝐳^t2,𝐯^t2,𝔼​[𝐯^t2])]⟩​𝑑t\displaystyle\ -\mu\_{0}\int\_{0}^{T}\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},-\mathbb{E}\left[\partial\_{{\bf x}}{\bf F}(t,\hat{{\bf x}}^{1}\_{t},\hat{{\bf z}}^{1}\_{t},\hat{{\bf v}}^{1}\_{t},\mathbb{E}[\hat{{\bf v}}^{1}\_{t}])-\partial\_{{\bf x}}{\bf F}(t,\hat{{\bf x}}^{2}\_{t},\hat{{\bf z}}^{2}\_{t},\hat{{\bf v}}^{2}\_{t},\mathbb{E}[\hat{{\bf v}}^{2}\_{t}])\right]\right\rangle dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −KT​δ​𝔼​[∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝐱~t|2+|𝐩~t|2+|𝜼~t|2)​𝑑t].\displaystyle\ -K\_{T}\delta\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}+\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{\boldsymbol{\eta}}\_{t}\right|^{2}\right)dt\right]. |  |

Rearranging yields

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | μ0​∫0T⟨𝔼​[𝐩^~t],𝚷​𝔼​[𝐯^~t]⟩​𝑑t\displaystyle\ \mu\_{0}\int\_{0}^{T}\left\langle\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],{\bf\Pi}\mathbb{E}[\tilde{\hat{\bf v}}\_{t}]\right\rangle dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | μ0​𝔼​[⟨𝐌​𝐳^~T,−(∂𝐱𝐆​(𝐱^T1,𝐱^T1)−∂𝐱𝐆​(𝐱^T2,𝐱^T2))⟩]+(1−μ0)​⟨𝐌​𝐳^~T,𝐳^~T⟩\displaystyle\ \mu\_{0}\mathbb{E}\left[\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{T},-\left(\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{1}\_{T},\hat{{\bf x}}^{1}\_{T})-\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{2}\_{T},\hat{{\bf x}}^{2}\_{T})\right)\right\rangle\right]+(1-\mu\_{0})\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{T},\tilde{\hat{{\bf z}}}\_{T}\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ​𝔼​[⟨𝐌​𝐳^~T,−(∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)+𝐳~T)⟩]\displaystyle\ +\delta\mathbb{E}\left[\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{T},-\left(\partial\_{{\bf x}}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{{\bf x}}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})+\tilde{{\bf z}}\_{T}\right)\right\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−μ0)​∫0T(⟨𝐌​𝔼​[𝐩^~t],𝔼​[𝐩^~t]⟩+⟨𝐌​𝐳^~t,𝐳^~t⟩)​𝑑t\displaystyle\ +(1-\mu\_{0})\int\_{0}^{T}\left(\left\langle{\bf M}\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}]\right\rangle+\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},\tilde{\hat{{\bf z}}}\_{t}\right\rangle\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −μ0​∫0T⟨𝐌​𝐳^~t,𝔼​[∂𝐱𝐅​(t,𝐱^t1,𝐳^t1,𝐯^t1,𝔼​[𝐯^t1])−∂𝐱𝐅​(t,𝐱^t2,𝐳^t2,𝐯^t2,𝔼​[𝐯^t2])]⟩​𝑑t\displaystyle\ -\mu\_{0}\int\_{0}^{T}\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},\mathbb{E}\left[\partial\_{{\bf x}}{\bf F}(t,\hat{{\bf x}}^{1}\_{t},\hat{{\bf z}}^{1}\_{t},\hat{{\bf v}}^{1}\_{t},\mathbb{E}[\hat{{\bf v}}^{1}\_{t}])-\partial\_{{\bf x}}{\bf F}(t,\hat{{\bf x}}^{2}\_{t},\hat{{\bf z}}^{2}\_{t},\hat{{\bf v}}^{2}\_{t},\mathbb{E}[\hat{{\bf v}}^{2}\_{t}])\right]\right\rangle dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +KT​δ​𝔼​[∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝐱~t|2+|𝐩~t|2+|𝜼~t|2)​𝑑t].\displaystyle\ +K\_{T}\delta\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}+\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{\boldsymbol{\eta}}\_{t}\right|^{2}\right)dt\right]. |  | (63) |

Following the derivation of ([4.2](https://arxiv.org/html/2511.12292v1#S4.Ex60 "4.2 Uniqueness of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market")), using Assumptions [2.1](https://arxiv.org/html/2511.12292v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.4 Assumptions ‣ 2 Model Formulation ‣ Mean Field Analysis of Mutual Insurance Market"), [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmassumption2 "Assumption 4.2. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), and substituting ([62](https://arxiv.org/html/2511.12292v1#A4.E62 "In D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market"))-([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex234 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")) into ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex212 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")), we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | KT​δ​𝔼​[|𝐱^~T|2+|𝐱~|T2+∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝜼^~t|2+|𝐱~t|2+|𝐩~t|2+|𝜼~t|2)​𝑑t]\displaystyle\ K\_{T}\delta\mathbb{E}\left[|\tilde{\hat{{\bf x}}}\_{T}|^{2}+|\tilde{{\bf x}}|\_{T}^{2}+\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}+\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{\boldsymbol{\eta}}\_{t}\right|^{2}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | KT​δ​(𝔼​[∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝜼^~t|2+|𝐱~t|2+|𝐩~t|2+|𝜼~t|2)​𝑑t])\displaystyle\ K\_{T}\delta\left(\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}+\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{\boldsymbol{\eta}}\_{t}\right|^{2}\right)dt\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ​𝔼​[⟨𝐱^~T−𝐌​𝐳^~T,∂𝐱𝐆​(𝐱T1,𝐳T1)−∂𝐱𝐆​(𝐱T2,𝐳T2)⟩]\displaystyle\ +\delta\mathbb{E}\left[\left\langle\tilde{\hat{{\bf x}}}\_{T}-{\bf M}\tilde{\hat{{\bf z}}}\_{T},\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})\right\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | μ0​𝔼​[⟨𝐱^~T−𝐌​𝐳^~T,−(∂𝐱𝐆​(𝐱^T1,𝐳^T1)−∂𝐱𝐆​(𝐱^T2,𝐳^T2))⟩]\displaystyle\ \mu\_{0}\mathbb{E}\left[\left\langle\tilde{\hat{{\bf x}}}\_{T}-{\bf M}\tilde{\hat{{\bf z}}}\_{T},-\left(\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{1}\_{T},\hat{{\bf z}}^{1}\_{T})-\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{2}\_{T},\hat{{\bf z}}^{2}\_{T})\right)\right\rangle\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−μ0)​(𝔼​[|𝐱^~T|2]−⟨𝐌​𝐳^~T,𝐳^~T⟩)\displaystyle\ +(1-\mu\_{0})\left(\mathbb{E}\left[\left|\tilde{\hat{{\bf x}}}\_{T}\right|^{2}\right]-\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{T},\tilde{\hat{{\bf z}}}\_{T}\right\rangle\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −μ0​𝔼​[∫0T⟨𝐱^~t−𝐌​𝐳^~t,∂𝐱𝐅​(t,𝐱^t1,𝐳^t1,𝐯^t1,𝔼​[𝐯^t1])−∂𝐱𝐅​(t,𝐱^t2,𝐳^t2,𝐯^t2,𝔼​[𝐯^t2])⟩​𝑑t]\displaystyle\ -\mu\_{0}\mathbb{E}\left[\int\_{0}^{T}\left\langle\tilde{\hat{{\bf x}}}\_{t}-{\bf M}\tilde{\hat{{\bf z}}}\_{t},\partial\_{\bf x}{\bf F}(t,\hat{{\bf x}}^{1}\_{t},\hat{{\bf z}}^{1}\_{t},\hat{{\bf v}}^{1}\_{t},\mathbb{E}[\hat{{\bf v}}^{1}\_{t}])-\partial\_{\bf x}{\bf F}(t,\hat{{\bf x}}^{2}\_{t},\hat{{\bf z}}^{2}\_{t},\hat{{\bf v}}^{2}\_{t},\mathbb{E}[\hat{{\bf v}}^{2}\_{t}])\right\rangle dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−μ0)​𝔼​[∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝜼^~t|2)​𝑑t]\displaystyle\ +(1-\mu\_{0})\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1−μ0)​∫0T(⟨𝐌​𝔼​[𝐩^~t],𝔼​[𝐩^~t]⟩+⟨𝐌​𝐳^~t,𝐳^~t⟩)​𝑑t\displaystyle\ -(1-\mu\_{0})\int\_{0}^{T}\left(\left\langle{\bf M}\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}],\mathbb{E}[\tilde{\hat{{\bf p}}}\_{t}]\right\rangle+\left\langle{\bf M}\tilde{\hat{{\bf z}}}\_{t},\tilde{\hat{{\bf z}}}\_{t}\right\rangle\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | [μ0​α𝐌𝐆+(1−μ0)​min⁡{λmin​(𝐈−𝐌),1}]​𝔼​[|𝐱^~T|2]\displaystyle\ \left[\mu\_{0}\alpha\_{\bf M}^{\bf G}+(1-\mu\_{0})\min\{\lambda\_{\min}({\bf I}-{\bf M}),1\}\right]\mathbb{E}\left[\left|\tilde{\hat{{\bf x}}}\_{T}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[μ0​α𝐌+(1−μ0)​min⁡{λmin​(𝐈−𝐌),1}]​𝔼​[∫0T|𝐱^~t|2​𝑑t]\displaystyle\ +\left[\mu\_{0}{\alpha}\_{\bf M}+(1-\mu\_{0})\min\{\lambda\_{\min}({\bf I}-{\bf M}),1\}\right]\mathbb{E}\left[\int\_{0}^{T}\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−μ0)​𝔼​[∫0T(min⁡{λmin​(𝐈−𝐌),1}​|𝐩^~t|2+|𝜼^~t|2)​𝑑t],\displaystyle\ +(1-\mu\_{0})\mathbb{E}\left[\int\_{0}^{T}\left(\min\{\lambda\_{\min}({\bf I}-{\bf M}),1\}\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}\right)dt\right], |  | (64) |

Note that the last inequality is a consequence of Lemma [A.3](https://arxiv.org/html/2511.12292v1#A1.Thmlemma3 "Lemma A.3. ‣ Appendix A Auxiliary Lemmas ‣ Mean Field Analysis of Mutual Insurance Market").

Next, we estimate

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T(|𝐩^~t|2+|𝜼^~t|2)​𝑑t].\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}\right)dt\right]. |  |

By applying Itô’s lemma to |𝐩^~t|2|\tilde{\hat{{\bf p}}}\_{t}|^{2}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼[|−μ0(∂𝐱𝐆(𝐱^T1,𝐳^T1)−∂𝐱𝐆(𝐱^T2,𝐳^T2))+(1−μ0)𝐱^~T\displaystyle\ \mathbb{E}\bigg[\bigg|-\mu\_{0}\left(\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{1}\_{T},\hat{{\bf z}}^{1}\_{T})-\partial\_{\bf x}{\bf G}(\hat{{\bf x}}^{2}\_{T},\hat{{\bf z}}^{2}\_{T})\right)+(1-\mu\_{0})\tilde{\hat{{\bf x}}}\_{T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −δ(∂𝐱𝐆(𝐱T1,𝐳T1)−∂𝐱𝐆(𝐱T2,𝐳T2)+𝐱~T)|2]−𝔼[|𝐩^~t|2]\displaystyle\quad-\delta\left(\partial\_{\bf x}{\bf G}({\bf x}^{1}\_{T},{\bf z}^{1}\_{T})-\partial\_{\bf x}{\bf G}({\bf x}^{2}\_{T},{\bf z}^{2}\_{T})+\tilde{{\bf x}}\_{T}\right)\bigg|^{2}\bigg]-\mathbb{E}\left[\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 2​μ0​𝔼​[∫tT(r​|𝐩^~s|2+⟨𝐩^~s,∂𝐱𝐅​(s,𝐱^s1,𝐳^s1,𝐯^s1,𝔼​[𝐯^s1])−∂𝐱𝐅​(s,𝐱^s2,𝐳^s2,𝐯^s2,𝔼​[𝐯^s2])⟩)​𝑑s]\displaystyle\ 2\mu\_{0}\mathbb{E}\left[\int\_{t}^{T}\left(r\left|\tilde{\hat{{\bf p}}}\_{s}\right|^{2}+\left\langle\tilde{\hat{{\bf p}}}\_{s},\partial\_{\bf x}{\bf F}(s,{\hat{{\bf x}}}^{1}\_{s},{\hat{{\bf z}}}^{1}\_{s},{\hat{{\bf v}}}^{1}\_{s},\mathbb{E}[{\hat{{\bf v}}}^{1}\_{s}])-\partial\_{\bf x}{\bf F}(s,{\hat{{\bf x}}}^{2}\_{s},{\hat{{\bf z}}}^{2}\_{s},{\hat{{\bf v}}}^{2}\_{s},\mathbb{E}[{\hat{{\bf v}}}^{2}\_{s}])\right\rangle\right)ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −2​(1−μ0)​𝔼​[∫tT⟨𝐩^~s,𝐱^~s⟩​𝑑s]+𝔼​[∫tT|𝜼^~s|2​𝑑s]\displaystyle\quad-2(1-\mu\_{0})\mathbb{E}\left[\int\_{t}^{T}\left\langle\tilde{\hat{{\bf p}}}\_{s},\tilde{\hat{{\bf x}}}\_{s}\right\rangle ds\right]+\mathbb{E}\left[\int\_{t}^{T}\left|\tilde{\hat{\boldsymbol{\eta}}}\_{s}\right|^{2}ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ𝔼[∫tT⟨𝐩^~s,−𝐱~s+r𝐩~s−(∂𝐱𝐅(s,𝐱s1,𝐳s1,𝐯s1,𝔼[𝐯s1])\displaystyle\quad+\delta\mathbb{E}\Bigg[\int\_{t}^{T}\bigg\langle\tilde{\hat{{\bf p}}}\_{s},-\tilde{{\bf x}}\_{s}+r\tilde{{\bf p}}\_{s}-\big(\partial\_{\bf x}{\bf F}(s,{\bf x}^{1}\_{s},{{\bf z}}^{1}\_{s},{{\bf v}}^{1}\_{s},\mathbb{E}[{{\bf v}}^{1}\_{s}]) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∂𝐱𝐅(s,𝐱s2,𝐳s2,𝐯s2,𝔼[𝐯s2]))⟩ds].\displaystyle\qquad\quad-\partial\_{\bf x}{\bf F}(s,{{\bf x}}^{2}\_{s},{{\bf z}}^{2}\_{s},{{\bf v}}^{2}\_{s},\mathbb{E}[{{\bf v}}^{2}\_{s}])\big)\bigg\rangle ds\Bigg]. |  | (65) |

By Assumption [4.1](https://arxiv.org/html/2511.12292v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Assumptions for Well-posedness of MF-FBSDE ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"), we further obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[|𝐩^~t|2]+𝔼​[∫tT|𝜼^~s|2​𝑑s]\displaystyle\ \mathbb{E}\left[\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}\right]+\mathbb{E}\left[\int\_{t}^{T}\left|\tilde{\hat{\boldsymbol{\eta}}}\_{s}\right|^{2}ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | KT​𝔼​[|𝐱^~T|2]+KT​𝔼​[∫tT(|𝐩^~s|2+|𝐱^~s|2)​𝑑s]\displaystyle\ K\_{T}\mathbb{E}\left[\left|\tilde{{\hat{{\bf x}}}}\_{T}\right|^{2}\right]+K\_{T}\mathbb{E}\left[\int\_{t}^{T}\left(\left|\tilde{\hat{{\bf p}}}\_{s}\right|^{2}+\left|\tilde{\hat{{\bf x}}}\_{s}\right|^{2}\right)ds\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +δ​KT​(𝔼​[|𝐱~T|2]+𝔼​[∫tT(|𝐩^~s|2+|𝐩~s|2+|𝐱~s|2)​𝑑s]).\displaystyle\ +\delta K\_{T}\left(\mathbb{E}[|\tilde{{\bf x}}\_{T}|^{2}]+\mathbb{E}\left[\int\_{t}^{T}\left(\left|\tilde{\hat{{\bf p}}}\_{s}\right|^{2}+\left|\tilde{{\bf p}}\_{s}\right|^{2}+\left|\tilde{{\bf x}}\_{s}\right|^{2}\right)ds\right]\right). |  | (66) |

By Grönwall’s inequality, we infer from ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex255 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|𝐩^~t|2]\displaystyle\mathbb{E}\left[\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}\right] | ≤KT​𝔼​[|𝐱^~T|2]+KT​𝔼​[∫0T|𝐱^~s|2​𝑑s]\displaystyle\leq K\_{T}\mathbb{E}\left[\left|\tilde{{\hat{{\bf x}}}}\_{T}\right|^{2}\right]+K\_{T}\mathbb{E}\left[\int\_{0}^{T}\left|\tilde{\hat{{\bf x}}}\_{s}\right|^{2}ds\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +δ​KT​(𝔼​[|𝐱~T|2]+𝔼​[∫0T(|𝐩~s|2+|𝐱~s|2)​𝑑s]).\displaystyle\ +\delta K\_{T}\left(\mathbb{E}[|\tilde{{\bf x}}\_{T}|^{2}]+\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{{\bf p}}\_{s}\right|^{2}+\left|\tilde{{\bf x}}\_{s}\right|^{2}\right)ds\right]\right). |  | (67) |

Substituting ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex257 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")) into the right-hand side of ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex255 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")), followed by integrating both sides over t=0t=0 to t=Tt=T, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T(|𝐩^~t|2+|𝜼^~t|2)​𝑑t]\displaystyle\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}\right)dt\right] | ≤KT​𝔼​[|𝐱^~T|2]+KT​𝔼​[∫0T|𝐱^~t|2​𝑑t]\displaystyle\leq K\_{T}\mathbb{E}\left[\left|\tilde{{\hat{{\bf x}}}}\_{T}\right|^{2}\right]+K\_{T}\mathbb{E}\left[\int\_{0}^{T}\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +δ​KT​(𝔼​[|𝐱~T|2]+𝔼​[∫0T(|𝐩~t|2+|𝐱~t|2)​𝑑t]).\displaystyle\ +\delta K\_{T}\left(\mathbb{E}[|\tilde{{\bf x}}\_{T}|^{2}]+\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}\right)dt\right]\right). |  | (68) |

If α𝐌𝐆>0\alpha^{\bf G}\_{{\bf M}}>0, by combining ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex258 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")) and ([D.2](https://arxiv.org/html/2511.12292v1#A4.Ex239 "D.2 Proof of Lemma 4.2 ‣ Appendix D Proofs of Assertions in Section 4 ‣ Mean Field Analysis of Mutual Insurance Market")), there exists KT>0K\_{T}>0 such that for any μ0∈[0,1]\mu\_{0}\in[0,1] and sufficiently small δ>0\delta>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[|𝐱^~T|2]+𝔼​[∫0T|𝐱^~t|2​𝑑t]+KT​𝔼​[∫0T(|𝐩^~t|2+|𝜼^~t|2)​𝑑t]\displaystyle\ \mathbb{E}\left[\left|\tilde{\hat{{\bf x}}}\_{T}\right|^{2}\right]+\mathbb{E}\left[\int\_{0}^{T}\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}dt\right]+K\_{T}\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | δ​KT​𝔼​[|𝐱^~T|2+|𝐱~T|2+∫0T(|𝐱^~t|2+|𝐩^~t|2+|𝜼^~t|2+|𝐱~t|2+|𝐩~t|2+|𝜼~t|2)​𝑑t]\displaystyle\ \delta K\_{T}\mathbb{E}\left[\left|\tilde{\hat{{\bf x}}}\_{T}\right|^{2}+\left|\tilde{{\bf x}}\_{T}\right|^{2}+\int\_{0}^{T}\left(\left|\tilde{\hat{{\bf x}}}\_{t}\right|^{2}+\left|\tilde{\hat{{\bf p}}}\_{t}\right|^{2}+\left|\tilde{\hat{\boldsymbol{\eta}}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}+\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{\boldsymbol{\eta}}\_{t}\right|^{2}\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ2​KT​(𝔼​[|𝐱~T|2]+𝔼​[∫0T(|𝐩~t|2+|𝐱~t|2)​𝑑t]).\displaystyle\ +\delta^{2}K\_{T}\left(\mathbb{E}[|\tilde{{\bf x}}\_{T}|^{2}]+\mathbb{E}\left[\int\_{0}^{T}\left(\left|\tilde{{\bf p}}\_{t}\right|^{2}+\left|\tilde{{\bf x}}\_{t}\right|^{2}\right)dt\right]\right). |  |

Therefore, one can pick δ>0\delta>0 such that Ψμ0+δ\Psi\_{\mu\_{0}+\delta} is a contraction for any μ0∈[0,1]\mu\_{0}\in[0,1] and the proof is complete.

## Appendix E Proofs of Assertions in Section [5](https://arxiv.org/html/2511.12292v1#S5 "5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")

This section contains the proofs of statements in Section [5](https://arxiv.org/html/2511.12292v1#S5 "5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market").

### E.1 Proof of Theorem [5.1](https://arxiv.org/html/2511.12292v1#S5.Thmtheorem1 "Theorem 5.1. ‣ 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")

We consider an ansatz of the adjoint process pthp^{h}\_{t} with the following feedback form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pth=Γth​(xth−zth)+p¯th.p^{h}\_{t}=\Gamma^{h}\_{t}(x^{h}\_{t}-z^{h}\_{t})+\bar{p}^{h}\_{t}. |  | (69) |

Using ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), applying Itô’s lemma on the right hand side of ([69](https://arxiv.org/html/2511.12292v1#A5.E69 "In E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | d​(Γth​(xth−zth)+p¯th)\displaystyle\ d\left(\Gamma^{h}\_{t}(x^{h}\_{t}-z^{h}\_{t})+\bar{p}^{h}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (d​Γthd​t​(xth−zth)−κh​Γth​(vth−v¯th)+r​(Γth​(xth−zth)−p¯th)−Qth​zth​(1−Sth))​d​t\displaystyle\ \left(\frac{d\Gamma^{h}\_{t}}{dt}(x^{h}\_{t}-z^{h}\_{t})-\kappa^{h}\Gamma^{h}\_{t}(v^{h}\_{t}-\bar{v}^{h}\_{t})+r\left(\Gamma^{h}\_{t}\left(x^{h}\_{t}-z^{h}\_{t}\right)-\bar{p}^{h}\_{t}\right)-Q^{h}\_{t}z^{h}\_{t}(1-S^{h}\_{t})\right)dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +Γth​σh​(1−vth)​d​Wth.\displaystyle\quad+\Gamma^{h}\_{t}\sigma^{h}(1-v^{h}\_{t})dW^{h}\_{t}. |  | (70) |

By comparing ([E.1](https://arxiv.org/html/2511.12292v1#A5.Ex262 "E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")) with the equation satisfied by php^{h} in ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market"))
, we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηth=Γth​σh​(1−vth), and thus ​𝔼​[ηth]=Γth​σh​(1−v¯th).\eta^{h}\_{t}=\Gamma^{h}\_{t}\sigma^{h}(1-v^{h}\_{t}),\text{ and thus }\mathbb{E}[\eta^{h}\_{t}]=\Gamma^{h}\_{t}\sigma^{h}(1-\bar{v}^{h}\_{t}). |  | (71) |

Substituting ([71](https://arxiv.org/html/2511.12292v1#A5.E71 "In E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")) into ([34](https://arxiv.org/html/2511.12292v1#S5.E34 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | v¯th=κh​p¯th+(σh)2​ΓthPth​(1−Rth)+(σh)2​Γth​ and ​vth=κh​pth+(σh)2​ΓthPth+(σh)2​Γth+Rth​PthPth+(σh)2​Γth​v¯th.\bar{v}^{h}\_{t}=\frac{\kappa^{h}\bar{p}^{h}\_{t}+(\sigma^{h})^{2}\Gamma^{h}\_{t}}{P^{h}\_{t}(1-R^{h}\_{t})+(\sigma^{h})^{2}\Gamma^{h}\_{t}}\text{ and }v^{h}\_{t}=\frac{\kappa^{h}p^{h}\_{t}+(\sigma^{h})^{2}\Gamma^{h}\_{t}}{P^{h}\_{t}+(\sigma^{h})^{2}\Gamma^{h}\_{t}}+\frac{R^{h}\_{t}P^{h}\_{t}}{P^{h}\_{t}+(\sigma^{h})^{2}\Gamma^{h}\_{t}}\bar{v}^{h}\_{t}. |  | (72) |

By further substituting this into ([E.1](https://arxiv.org/html/2511.12292v1#A5.Ex262 "E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")), and using the ansatz ([69](https://arxiv.org/html/2511.12292v1#A5.E69 "In E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | d​(Γth​(xth−zth)+p¯th)\displaystyle\ d\left(\Gamma^{h}\_{t}(x^{h}\_{t}-z^{h}\_{t})+\bar{p}^{h}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (d​Γthd​t​(xth−zth)−(κh)2​Γth​(pth−p¯th)Pth+(σh)2​Γth+r​(Γth​(xth−zth)−p¯th)−Qth​zth​(1−Sth))​d​t\displaystyle\ \left(\frac{d\Gamma^{h}\_{t}}{dt}(x^{h}\_{t}-z^{h}\_{t})-\frac{(\kappa^{h})^{2}\Gamma^{h}\_{t}\left(p^{h}\_{t}-\bar{p}^{h}\_{t}\right)}{P^{h}\_{t}+(\sigma^{h})^{2}\Gamma^{h}\_{t}}+r\left(\Gamma^{h}\_{t}\left(x^{h}\_{t}-z^{h}\_{t}\right)-\bar{p}^{h}\_{t}\right)-Q^{h}\_{t}z^{h}\_{t}(1-S^{h}\_{t})\right)dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Γth​σh​(1−vth)​d​Wth\displaystyle\ +\Gamma^{h}\_{t}\sigma^{h}(1-v^{h}\_{t})dW^{h}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ((xth−zth)(d​Γthd​t−(κh)2​(Γth)2Pth+(σh)2​Γth+2rΓth+Qth)−r(Γth(xth−zth)+p¯th)\displaystyle\ \Bigg((x^{h}\_{t}-z^{h}\_{t})\left(\frac{d\Gamma^{h}\_{t}}{dt}-\frac{(\kappa^{h})^{2}(\Gamma^{h}\_{t})^{2}}{P^{h}\_{t}+(\sigma^{h})^{2}\Gamma^{h}\_{t}}+2r\Gamma^{h}\_{t}+Q^{h}\_{t}\right)-r\left(\Gamma^{h}\_{t}(x^{h}\_{t}-z^{h}\_{t})+\bar{p}^{h}\_{t}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −Qth(xth−Sthzth))dt+Γhtσh(1−vth)dWht\displaystyle\quad-Q^{h}\_{t}(x^{h}\_{t}-S^{h}\_{t}z^{h}\_{t})\Bigg)dt+\Gamma^{h}\_{t}\sigma^{h}(1-v^{h}\_{t})dW^{h}\_{t} |  | (73) |

Using ([69](https://arxiv.org/html/2511.12292v1#A5.E69 "In E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")), ([E.1](https://arxiv.org/html/2511.12292v1#A5.Ex264 "E.1 Proof of Theorem 5.1 ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")), and comparing with the equation satisfied by php^{h} in ([33](https://arxiv.org/html/2511.12292v1#S5.E33 "In Corollary 5.1. ‣ 5.1 Equilibrium Solution ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")), we deduce that Γh\Gamma^{h} has to satisfy ([35](https://arxiv.org/html/2511.12292v1#S5.E35 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")). The proof that the solution of ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) can be expressed as ([37](https://arxiv.org/html/2511.12292v1#S5.E37 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) and ([38](https://arxiv.org/html/2511.12292v1#S5.E38 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) can be proven similarly, and thus we omit the proof.

### E.2 Well-posedness of ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market"))

In this section, we provide a global existence condition for the equation ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")). To this end, we need the following assumption.

###### Assumption E.1.

1. (a)

   λ1:=inft∈[0,T]λmin​(𝐈−𝐒t)>0\lambda\_{1}:=\inf\_{t\in[0,T]}\lambda\_{\min}({\bf I}-{\bf S}\_{t})>0;
2. (b)

   λ2:=inft∈[0,T]λmin​(𝚲​𝐀t)>0\lambda\_{2}:=\inf\_{t\in[0,T]}\lambda\_{\min}({\bf\Lambda}{\bf A}\_{t})>0,

where 𝚲:=𝐊−𝚷{\bf\Lambda}:={\bf K}-{\bf\Pi}.

###### Theorem E.1.

Under Assumption [E.1](https://arxiv.org/html/2511.12292v1#A5.Thmassumption1 "Assumption E.1. ‣ E.2 Well-posedness of (36) ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market"), there is at most one solution for the equation ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")).

###### Proof.

Let (𝐳1,𝐩1)({\bf z}^{1},{\bf p}^{1}) and (𝐳2,𝐩2)({\bf z}^{2},{\bf p}^{2}) be two solutions of ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")). Then, the functions 𝐳~t:=𝐳t1−𝐳t2\tilde{{\bf z}}\_{t}:={\bf z}^{1}\_{t}-{\bf z}^{2}\_{t} and 𝐩¯~t:=𝐩¯~t1−𝐩¯~t2\tilde{\bar{{\bf p}}}\_{t}:=\tilde{\bar{{\bf p}}}^{1}\_{t}-\tilde{\bar{{\bf p}}}^{2}\_{t} satisfies

|  |  |  |
| --- | --- | --- |
|  | {d​𝐳~t=(r​𝐳t−𝚲​𝐀t​𝐩¯~t)​d​t,−d​𝐩¯~t=(r​𝐩¯~t+𝐐t​(𝐈−𝐒t)​𝐳~t)​d​t,𝐳~0=𝟎,𝐩¯~T=𝐐T​(𝐈−𝐒T)​𝐳~T.\begin{dcases}d\tilde{{\bf z}}\_{t}=\left(r{\bf z}\_{t}-{\bf\Lambda}{\bf A}\_{t}\tilde{\bar{{\bf p}}}\_{t}\right)dt,\\ -d\tilde{\bar{{\bf p}}}\_{t}=\left(r\tilde{\bar{{\bf p}}}\_{t}+{\bf Q}\_{t}({\bf I}-{\bf S}\_{t})\tilde{{\bf z}}\_{t}\right)dt,\\ \tilde{{\bf z}}\_{0}={\bf 0},\\ \tilde{\bar{{\bf p}}}\_{T}={\bf Q}\_{T}({\bf I}-{\bf S}\_{T})\tilde{{\bf z}}\_{T}.\end{dcases} |  |

Using this, by considering the differential of 𝐳~t​𝐩¯~t\tilde{{\bf z}}\_{t}\tilde{\bar{{\bf p}}}\_{t}, we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐳~T​𝐐T​(𝐈−𝐒T)​𝐳~T+∫0T𝐳~t​𝐐t​(𝐈−𝐒T)​𝐳~t​𝑑t\displaystyle\tilde{{\bf z}}\_{T}{\bf Q}\_{T}({\bf I}-{\bf S}\_{T})\tilde{{\bf z}}\_{T}+\int\_{0}^{T}\tilde{{\bf z}}\_{t}{\bf Q}\_{t}({\bf I}-{\bf S}\_{T})\tilde{{\bf z}}\_{t}dt | =−∫0T𝐩¯~t​𝚲​𝐀t​𝐩¯~t​𝑑t\displaystyle=-\int\_{0}^{T}\tilde{\bar{{\bf p}}}\_{t}{\bf\Lambda}{\bf A}\_{t}\tilde{\bar{{\bf p}}}\_{t}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−12​inft∈[0,T]λmin​(𝚲​𝐀t+𝐀t​𝚲⊤)​∫0T|𝐩¯~t|2​𝑑t≤0.\displaystyle\leq-\frac{1}{2}\inf\_{t\in[0,T]}\lambda\_{\min}({\bf\Lambda}{\bf A}\_{t}+{\bf A}\_{t}{\bf\Lambda}^{\top})\int\_{0}^{T}|\tilde{\bar{{\bf p}}}\_{t}|^{2}dt\leq 0. |  |

This implies 𝐳~\tilde{{\bf z}} and thus 𝐩~\tilde{{\bf p}} must be identical to zero.
∎

To show that the FBODE indeed admits a solution, we again employ the continuation approach. To this end, we let 𝐳^\hat{{\bf z}} and 𝐩^\hat{{\bf p}} be the solution of the FBODE parametrized by μ0∈[0,1]\mu\_{0}\in[0,1]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​𝐳^t=(−(1−μ)​λ2​𝐩^t+μ​(r​𝐳^t−𝚲​𝐀t​𝐩^t+𝐥)+ϕt)​d​t,−d​𝐩^t=((1−μ)​λ1​𝐳^t+μ​(r​𝐩^t+𝐐t​(𝐈−𝐒t))+ψt)​d​t,𝐳^0=(𝔼​[ξh])h=1H,𝐩^T=(1−μ)​λ1​𝐳T+μ​𝐐T​(𝐈−𝐒T)​𝐳^T−𝜸,\begin{dcases}d\hat{{\bf z}}\_{t}=\left(-(1-\mu)\lambda\_{2}\hat{{\bf p}}\_{t}+\mu\left(r\hat{{\bf z}}\_{t}-{\bf\Lambda}{\bf A}\_{t}\hat{{\bf p}}\_{t}+{\bf l}\right)+\phi\_{t}\right)dt,\\ -d\hat{{\bf p}}\_{t}=\left((1-\mu)\lambda\_{1}\hat{{\bf z}}\_{t}+\mu\left(r\hat{{\bf p}}\_{t}+{\bf Q}\_{t}({\bf I}-{\bf S}\_{t})\right)+\psi\_{t}\right)dt,\\ \hat{{\bf z}}\_{0}=(\mathbb{E}[\xi^{h}])\_{h=1}^{H},\\ \hat{{\bf p}}\_{T}=(1-\mu)\lambda\_{1}{\bf z}\_{T}+\mu{\bf Q}\_{T}({\bf I}-{\bf S}\_{T})\hat{\bf z}\_{T}-\boldsymbol{\gamma},\end{dcases} |  | (74) |

where ϕt,ξt\phi\_{t},\xi\_{t} are square integrable functions over [0,T][0,T]. The spirit of the approach is in line with the proof of Lemma [4.2](https://arxiv.org/html/2511.12292v1#S4.Thmlemma2 "Lemma 4.2. ‣ 4.3 Global Existence of Solution ‣ 4 Well-posedness of the MF-FBSDE (15) ‣ Mean Field Analysis of Mutual Insurance Market"): if the system ([74](https://arxiv.org/html/2511.12292v1#A5.E74 "In E.2 Well-posedness of (36) ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")) has a solution for μ=μ0\mu=\mu\_{0}, and for any square-integrable functions ϕt,ξt\phi\_{t},\xi\_{t}, then the operator defined by ([74](https://arxiv.org/html/2511.12292v1#A5.E74 "In E.2 Well-posedness of (36) ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")) is a contraction for any μ∈[μ0,μ0+δ]\mu\in[\mu\_{0},\mu\_{0}+\delta], where δ>0\delta>0 is independent of μ0\mu\_{0}. Hence, the system ([74](https://arxiv.org/html/2511.12292v1#A5.E74 "In E.2 Well-posedness of (36) ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")) admits a solution whenever μ∈[μ0,μ0+δ]\mu\in[\mu\_{0},\mu\_{0}+\delta]. Using the fact that the solution ([74](https://arxiv.org/html/2511.12292v1#A5.E74 "In E.2 Well-posedness of (36) ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market")) admits a solution when μ=0\mu=0, we can conclude the existence of solution for any μ∈[0,1]\mu\in[0,1]. The details of the calculations are omitted.

###### Theorem E.2.

Under Assumption [E.1](https://arxiv.org/html/2511.12292v1#A5.Thmassumption1 "Assumption E.1. ‣ E.2 Well-posedness of (36) ‣ Appendix E Proofs of Assertions in Section 5 ‣ Mean Field Analysis of Mutual Insurance Market"), Equation ([36](https://arxiv.org/html/2511.12292v1#S5.E36 "In 5.2 Equilibrium without Insurance Constraints ‣ 5 Quadratic Rewards ‣ Mean Field Analysis of Mutual Insurance Market")) admits a solution.

## Appendix F Supplementary Tables for Section [6](https://arxiv.org/html/2511.12292v1#S6 "6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market")

This section presents tables summarizing the training errors and computational efficiency of the neural network algorithm used in Section [6](https://arxiv.org/html/2511.12292v1#S6 "6 Numerical Experiments ‣ Mean Field Analysis of Mutual Insurance Market").

Table 3: Computation errors of neural network approach with respect to the ODE approach under non-constrained cases.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Relative Error (%) | | | | | |
| Penalty coefficient λ\lambda | 0.1 | 1.0 | 10.0 | 100.0 | 1000.0 |
| Case 1(a) | 9.844555 | 0.915430 | 0.678508 | 7.141356 | 20.914042 |
| Case 1(b) | 9.739147 | 1.407824 | 0.608529 | 7.287133 | 19.793709 |
| Case 1(c) | 9.704202 | 1.084904 | 0.732753 | 7.099290 | 23.721090 |
| Case 2(a) | 5.520915 | 1.421929 | 1.565124 | 2.647546 | 8.175174 |
| Case 2(b) | 5.209600 | 1.402305 | 1.574674 | 2.877253 | 11.329953 |
| Case 2(c) | 5.610542 | 1.438909 | 1.556929 | 2.462988 | 11.801251 |
| Case 3(a) | 3.701866 | 1.549085 | 2.105542 | 3.224022 | 7.313468 |
| Case 3(b) | 5.162252 | 1.134077 | 1.410400 | 3.693166 | 6.850523 |
| Case 4(a) | 9.575447 | 0.908286 | 1.445545 | 3.657386 | 11.387693 |
| Case 4(b) | 9.883666 | 1.643441 | 1.464042 | 3.789543 | 11.719880 |
| Case 4(c) | 9.904698 | 1.665042 | 1.383423 | 3.927721 | 12.774165 |

The average time to compute each total error is 1886.94 seconds.




Table 4: Final loss functions for unconstrained cases.

|  |  |  |  |
| --- | --- | --- | --- |
| Unconstrained Cases | Case 1(a) | Case 1(b) | Case 1(c) |
| Terminal Condition Error | 1.548988×10−31.548988\times 10^{-3} | 1.667531×10−31.667531\times 10^{-3} | 1.450754×10−31.450754\times 10^{-3} |
| Mean Field Term Error | 3.235802×10−53.235802\times 10^{-5} | 4.012196×10−54.012196\times 10^{-5} | 2.563629×10−52.563629\times 10^{-5} |
| Time elapsed (secs) | 1893.98 | 1881.24 | 1931.42 |
|  | Case 2(a) | Case 2(b) | Case 2(c) |
| Terminal Condition Error | 6.176409×10−46.176409\times 10^{-4} | 6.400801×10−46.400801\times 10^{-4} | 6.024750×10−46.024750\times 10^{-4} |
| Mean Field Term Error | 1.265802×10−51.265802\times 10^{-5} | 2.451912×10−52.451912\times 10^{-5} | 6.414652×10−66.414652\times 10^{-6} |
| Time elapsed (secs) | 1896.25 | 1869.49 | 1868.24 |
|  | Case 3(a) | Case 3(b) | Case 4(a) |
| Terminal Condition Error | 2.784362×10−42.784362\times 10^{-4} | 5.350168×10−45.350168\times 10^{-4} | 8.624881×10−38.624881\times 10^{-3} |
| Mean Field Term Error | 2.395581×10−52.395581\times 10^{-5} | 5.165220×10−55.165220\times 10^{-5} | 1.511587×10−41.511587\times 10^{-4} |
| Time elapsed (secs) | 1865.63 | 1867.42 | 1879.71 |
|  | Case 4(b) | Case 4(c) | Case 5 |
| Terminal Condition Error | 1.638430×10−31.638430\times 10^{-3} | 1.698711×10−31.698711\times 10^{-3} | 1.663634×10−51.663634\times 10^{-5} |
| Mean Field Term Error | 5.030000×10−75.030000\times 10^{-7} | 1.427944×10−61.427944\times 10^{-6} | 4.262555×10−64.262555\times 10^{-6} |
| Time elapsed (secs) | 1865.49 | 1863.38 | 2124.92 |

The terminal condition error and the mean field term error refers to the term ∑h=12𝔼[(pTh+gx(xTh,zTh)]\sum\limits\_{h=1}^{2}\mathbb{E}\left[(p^{h}\_{T}+g\_{x}(x^{h}\_{T},z^{h}\_{T})\right] and 1M​∑i=0M−1∑h=12(𝔼​[vtih]−v¯tih)2\frac{1}{M}\sum\limits\_{i=0}^{M-1}\sum\limits\_{h=1}^{2}(\mathbb{E}[v^{h}\_{t\_{i}}]-\bar{v}^{h}\_{t\_{i}})^{2}, respectively.




Table 5: Final loss and penalty values for constrained cases

|  |  |  |  |
| --- | --- | --- | --- |
| Constrained Cases | Case 1(a) | Case 1(b) | Case 1(c) |
| Terminal Condition Error | 2.009435×10−32.009435\times 10^{-3} | 2.245595×10−32.245595\times 10^{-3} | 1.819428×10−31.819428\times 10^{-3} |
| Mean Field Term Error | 6.938315×10−56.938315\times 10^{-5} | 8.738402×10−58.738402\times 10^{-5} | 5.548106×10−55.548106\times 10^{-5} |
| Time elapsed (secs) | 1918.70 | 1945.75 | 1930.34 |
|  | Case 2(a) | Case 2(b) | Case 2(c) |
| Terminal Condition Error | 2.155019×10−32.155019\times 10^{-3} | 2.155019×10−32.155019\times 10^{-3} | 2.118284×10−32.118284\times 10^{-3} |
| Mean Field Term Error | 2.286199×10−42.286199\times 10^{-4} | 2.286199×10−42.286199\times 10^{-4} | 2.108407×10−42.108407\times 10^{-4} |
| Time elapsed (secs) | 1927.40 | 1936.75 | 1898.35 |
|  | Case 3(a) | Case 3(b) | Case 4(a) |
| Terminal Condition Error | 4.444087×10−34.444087\times 10^{-3} | 6.950257×10−46.950257\times 10^{-4} | 9.873541×10−49.873541\times 10^{-4} |
| Mean Field Term Error | 2.919305×10−32.919305\times 10^{-3} | 8.796966×10−58.796966\times 10^{-5} | 1.538552×10−41.538552\times 10^{-4} |
| Time elapsed (secs) | 1957.89 | 1907.67 | 1965.20 |
|  | Case 4(b) | Case 4(c) | Case 5 |
| Terminal Condition Error | 2.209101×10−32.209101\times 10^{-3} | 2.348184×10−32.348184\times 10^{-3} | 1.382007×10−51.382007\times 10^{-5} |
| Mean Field Term Error | 2.228195×10−52.228195\times 10^{-5} | 2.664459×10−52.664459\times 10^{-5} | 4.025126×10−64.025126\times 10^{-6} |
| Time elapsed (secs) | 1910.48 | 1914.44 | 2214.13 |

  



Table 6: Equilibrium insurance strategies with and without constraints for each case

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Case | Parameter | Constraint | v¯01\bar{v}^{1}\_{0} | v¯02\bar{v}^{2}\_{0} | v¯T−Δ​t1\bar{v}^{1}\_{T-\Delta t} | v¯T−Δ​t2\bar{v}^{2}\_{T-\Delta t} |
| 1(a) | |  | | --- | | σ1=0.1\sigma^{1}=0.1, σ2=0.3\sigma^{2}=0.3 | | No | 0.359091 | 0.440495 | -0.066468 | 0.015177 |
| Yes | 0.355441 | 0.435981 | 0.000000 | 0.033949 |
| 1(b) | |  | | --- | | 1(a) with | | ω1=0.8\omega^{1}=0.8 | | No | 0.352799 | 0.437634 | -0.069131 | 0.012958 |
| Yes | 0.347622 | 0.432593 | 0.000000 | 0.032654 |
| 1(c) | |  | | --- | | 1(a) with | | ω1=0.2\omega^{1}=0.2 | | No | 0.365121 | 0.442901 | -0.063986 | 0.017695 |
| Yes | 0.362339 | 0.439052 | 0.000000 | 0.035201 |
| 2(a) | |  | | --- | | γ1=1\gamma^{1}=1, γ2=1.6\gamma^{2}=1.6 | | No | 0.430947 | 0.175347 | 0.009570 | -0.265701 |
| Yes | 0.431735 | 0.133601 | 0.035397 | 0.000000 |
| 2(b) | |  | | --- | | 2(a) with | | ω1=0.8\omega^{1}=0.8 | | No | 0.442197 | 0.182480 | 0.017060 | -0.254958 |
| Yes | 0.440488 | 0.137245 | 0.038818 | 0.000000 |
| 2(c) | |  | | --- | | 2(a) with | | ω1=0.2\omega^{1}=0.2 | | No | 0.419688 | 0.167624 | 0.001187 | -0.275922 |
| Yes | 0.422559 | 0.129154 | 0.028175 | 0.000000 |
| 3(a) | |  | | --- | | κ1=0.1\kappa^{1}=0.1, κ2=0.5\kappa^{2}=0.5 | | γ1=γ2=1.6\gamma^{1}=\gamma^{2}=1.6 | | No | 0.165144 | 0.167612 | 0.024968 | -0.280722 |
| Yes | 0.174865 | 0.152342 | 0.020742 | 0.000000 |
| 3(b) | |  | | --- | | 3(a) with | | γ1=γ2=1\gamma^{1}=\gamma^{2}=1 | | No | 0.220572 | 0.431938 | 0.092434 | 0.009920 |
| Yes | 0.220646 | 0.426106 | 0.092528 | 0.029771 |
| 4(a) | |  | | --- | | l~1−μ1=0.02\tilde{l}^{1}-\mu^{1}=0.02 | | l~2−μ2=0.1\tilde{l}^{2}-\mu^{2}=0.1 | | No | 0.437253 | 0.449271 | 0.029694 | 0.050107 |
| Yes | 0.433595 | 0.448720 | 0.047438 | 0.063334 |
| 4(b) | |  | | --- | | 4(a) with | | e1=0.1e^{1}=0.1, e2=0.01e^{2}=0.01 | | No | 0.473885 | 0.443457 | 0.038497 | 0.019084 |
| Yes | 0.471770 | 0.438603 | 0.053599 | 0.036133 |
| 4(c) | |  | | --- | | 4(a) with | | e1=0.01e^{1}=0.01, e2=0.1e^{2}=0.1 | | No | 0.421126 | 0.495810 | 0.006337 | 0.052741 |
| Yes | 0.414905 | 0.495798 | 0.028501 | 0.065609 |
| 5 | |  | | --- | | γ1=0.5\gamma^{1}=0.5, γ2=3.0\gamma^{2}=3.0 | | No | 0.057585 | 0.103351 | 0.037535 | 0.057978 |
| Yes | 0.058370 | 0.104163 | 0.038957 | 0.058851 |