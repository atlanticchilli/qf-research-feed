---
authors:
- Zongxia Liang
- Jiayu Zhang
- Zhou Zhou
- Bin Zou
doc_id: arxiv:2601.12655v1
family_id: arxiv:2601.12655
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal Underreporting and Competitive Equilibrium
url_abs: http://arxiv.org/abs/2601.12655v1
url_html: https://arxiv.org/html/2601.12655v1
venue: arXiv q-fin
version: 1
year: 2026
---


Zongxia Liang
  
Jiayu Zhang
  
Zhou Zhou
  
Bin Zou
Department of Mathematical Sciences, and Center for Insurance and Risk Management, School of Economics and Management, Tsinghua University, China. Email: liangzongxia@tsinghua.edu.cnDepartment of Mathematical Sciences, Tsinghua University, China. Email: zjy23@mails.tsinghua.edu.cnSchool of Mathematics and Statistics, University of Sydney, Australia. Email: zhou.zhou@sydney.edu.auDepartment of Mathematics, University of Connecticut, USA. Email: bin.zou@uconn.edu

###### Abstract

This paper develops a dynamic insurance market model comprising two competing insurance companies and a continuum of insureds, and examines the interaction between strategic underreporting by the insureds and competitive pricing between the insurance companies under a Bonus-Malus System (BMS) framework. For the first time in an oligopolistic setting, we establish the existence and uniqueness of the insureds’ optimal reporting barrier, as well as its continuous dependence on the BMS premiums. For the 2-class BMS case, we prove the existence of Nash equilibrium premium strategies and conduct an extensive sensitivity analysis on the impact of the model parameters on the equilibrium premiums.

Keywords: Bonus-Malus System (BMS); Strategic underreporting; Oligopolistic competition; Nash Equilibrium; Stackelberg game

## 1 Introduction

Insurance companies commonly employ bonus–malus systems (BMS) that link future premiums to insureds’ historical claims in order to improve risk classification and to provide incentives for enhancing loss prevention, thereby mitigating ex-ante moral hazard. Such mechanisms allow premiums to more accurately reflect the true risk profile of the insureds. For example, Abbring et al. ([2003](https://arxiv.org/html/2601.12655v1#bib.bib26 "Moral hazard and dynamic insurance data")) document that claim frequency is negatively correlated with past claims and find no evidence of moral hazard, when analyzing French automobile insurance data under BMS.
The prototypical BMS operates as follows: if an insured does not file a claim in the preceding period, the premium for the subsequent period is reduced (“bonus”); conversely, if a claim occurs, the premium is increased (“malus”). Within this framework, insureds face strategic incentives to underreport losses. Specifically, an insured will choose not to report a loss if the expected increase in the subsequent premium caused by reporting exceeds the immediate benefit of the claim; on the other hand, reporting is optimal if the expected premium increase is smaller than the claim benefit. A substantial body of empirical and theoretical research has documented the existence of or studied such strategic underreporting by insureds (see, e.g., Haehling von Lanzenauer ([1974](https://arxiv.org/html/2601.12655v1#bib.bib32 "Optimal claim decisions by policyholders in automobile insurance with merit-rating structures")), Abbring et al. ([2008](https://arxiv.org/html/2601.12655v1#bib.bib41 "Better safe than sorry? Ex Ante, Ex Post, and moral hazard in dynamic insurance data")), and Robinson and Zheng ([2010](https://arxiv.org/html/2601.12655v1#bib.bib22 "Moral hazard, insurance claims, and repeated insurance contracts")), among many others).

Building on the aforementioned phenomenon of strategic underreporting, a natural question arises regarding the insureds’ optimal reporting decisions. Research on this topic remains relatively scarce, and we review recent progress as follows.
Zacks and Levikson ([2004](https://arxiv.org/html/2601.12655v1#bib.bib28 "Claiming strategies and premium levels for bonus malus systems")) employ standard dynamic programming methods to investigate the optimal reporting strategy and its impact on the insurer’s long-run average premium in multi-class BMS under risk neutrality with deductible insurance. Ludkovski and Young ([2010](https://arxiv.org/html/2601.12655v1#bib.bib29 "Ex post moral hazard and bayesian learning in insurance")) introduce a two-period model with asymmetric information, in which the insured adopts a stochastic reporting strategy modeled as a Bernoulli random variable, while the insurer updates beliefs about the risk type using Bayesian inference based on reported claims. Their results show that the optimal reporting strategy for a risk-neutral insured varies across risk types, and may involve full non-reporting, full reporting, or a mixed strategy. Charpentier et al. ([2017](https://arxiv.org/html/2601.12655v1#bib.bib7 "Optimal claiming strategies in bonus malus systems and implied markov chains")) provide a rigorous mathematical formulation of the claim reporting problem in discrete-time BMS settings. Using numerical methods, they compute the optimal reporting strategy and conduct sensitivity analyses for both the optimal strategy and underreporting probabilities. Cao et al. ([2024a](https://arxiv.org/html/2601.12655v1#bib.bib6 "Equilibrium reporting strategy: two rate classes and full insurance")) derive expressions for the optimal reporting strategy for insureds holding full-coverage insurance, providing a closed-form solution under risk neutrality and a semi-explicit form under risk aversion. Cao et al. ([2024b](https://arxiv.org/html/2601.12655v1#bib.bib8 "Strategic underreporting and optimal deductible insurance")) further investigate the optimal reporting strategy for insureds with deductible insurance, presenting conditions for non-zero reporting and a semi-explicit expression, and perform sensitivity analyses with respect to the optimal deductible. All above reviewed papers consider a discrete-time model; for optimal reporting problems in continuous-time, please refer to Cao et al. ([2025a](https://arxiv.org/html/2601.12655v1#bib.bib35 "Continuous-time optimal reporting with full insurance under the mean-variance criterion")) and Cao et al. ([2025b](https://arxiv.org/html/2601.12655v1#bib.bib34 "Optimal loss reporting in continuous time with full insurance")).

From the above summary, it is apparent that the existing literature on underreporting under the BMS frameworks focuses exclusively on insureds’ reporting strategies within a *monopolistic* insurance market (i.e., there is only one insurance company). However, real insurance markets are typically oligopolistic, characterized by intense competition among insurers. This gives rise to two fundamental questions:

* •

  Question 1: How should insureds’ reporting strategies be characterized in an oligopolistic insurance market?
* •

  Question 2: When insureds follow their optimal reporting strategies, how should competing insurance companies set the premiums for their individual BMS to reach (Nash) equilibrium?

To address these two questions above, we develop a discrete-time insurance market model with two competing insurance companies and a continuum of insureds. All insureds purchase full insurance but may choose either company as the provider. Both companies apply an NN-class BMS in pricing; however, their premiums may differ over rate classes. Because factors, such as service quality and the complexity of claims procedures, generate heterogeneous preferences across insurance companies (see, e.g., Ennew and Binks ([1996](https://arxiv.org/html/2601.12655v1#bib.bib19 "The impact of service quality and service characteristics on customer retention: small businesses and their banks")) and Cummins and Sommer ([1996](https://arxiv.org/html/2601.12655v1#bib.bib20 "Capital structure and fair profits in property-liability insurance"))), we incorporate a choice function η\eta to capture such insurer-specific preferences (here, η\eta is a function, which takes the premium difference from the two insurers as its argument and returns a probability for choosing Company 1 over Company 2). Following the approach of Zacks and Levikson ([2004](https://arxiv.org/html/2601.12655v1#bib.bib28 "Claiming strategies and premium levels for bonus malus systems")), Charpentier et al. ([2017](https://arxiv.org/html/2601.12655v1#bib.bib7 "Optimal claiming strategies in bonus malus systems and implied markov chains")), and Cao et al. ([2024b](https://arxiv.org/html/2601.12655v1#bib.bib8 "Strategic underreporting and optimal deductible insurance")), we assume that insureds employ a barrier reporting strategy when making reporting decisions. Let b={bni}i=1,2,n=1,⋯,Nb=\{b\_{n}^{i}\}\_{i=1,2,\,n=1,\cdots,N} denote a barrier reporting strategy, with bni≥0b\_{n}^{i}\geq 0 being the barrier when the insured is in rate class nn and buys insurance from Company ii. Then, such a strategy dictates the insured in rate class nn with Company ii to report a loss if and only if it is greater than the barrier bnib\_{n}^{i}.

For Question 1, we seek an optimal barrier strategy to minimize the expected total discounted expenses (i.e., insurance premiums plus hidden losses) and obtain a complete answer in Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium"), with additional results collected in Remarks [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmremark1 "Remark 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") and [3.2](https://arxiv.org/html/2601.12655v1#S3.Thmremark2 "Remark 3.2. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium").
We show that the optimal reporting barrier b∗b^{\*} exists and is unique. In addition, we derive the condition under which b∗b^{\*} is strictly positive, along with its semi-explicit expression.
The characterization of b∗b^{\*} has a clear economic meaning: it is the difference in expected expenses (or gain in expected utility) between reporting a loss and hiding a loss.

Regarding Question 2, which, to the best of our knowledge, has not been studied before in the literature, we consider a 2-class BMS (i.e., N=2N=2) and assume an exponential choice function η\eta for tractability. In this setting, we first obtain a finer result on the insureds’ optimal reporting barrier in Theorem [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"); next, we apply the Stackelberg game framework to study the interaction between the insurance companies and insureds. To be precise, the two insurance companies are the leaders and set the BMS premiums 𝐜i={cni}n=1,⋯,N\mathbf{c}^{i}=\{c^{i}\_{n}\}\_{n=1,\cdots,N}, for i=1,2i=1,2; the insureds are the followers and choose their optimal reporting barrier b∗​(𝐜1,𝐜2)b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}). Both companies aim to maximize their expected (per-period) profit, taking into account the possible underreporting from the insureds. Because of the competition in the market, each insurance company’s optimal premium strategy from the Stackelberg game depends on its competitor’s strategy, taking the form of 𝐜¯1​(𝐜2)\mathbf{\bar{c}}^{1}(\mathbf{c}^{2}) and 𝐜¯2​(𝐜1)\mathbf{\bar{c}}^{2}(\mathbf{c}^{1}), respectively. Finally, a Nash equilibrium premium strategy (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) is defined as a fixed point of the mapping (𝐜1,𝐜2)↦(𝐜¯1​(𝐜2),𝐜¯2​(𝐜1))(\mathbf{c}^{1},\mathbf{c}^{2})\mapsto(\mathbf{\bar{c}}^{1}(\mathbf{c}^{2}),\mathbf{\bar{c}}^{2}(\mathbf{c}^{1})).
We show that such an equilibrium premium strategy exists in Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), when the model parameters satisfy certain regularity conditions. We provide a concrete example to demonstrate that those regularity conditions can hold under a reasonable market.
Furthermore, we conduct an extensive sensitivity analysis to examine how various model parameters affect the insurers’ equilibrium premiums.

The remainder of the paper proceeds as follows. Section [2](https://arxiv.org/html/2601.12655v1#S2 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium") introduces the model framework. Section [3](https://arxiv.org/html/2601.12655v1#S3 "3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") derives the optimal reporting strategy for the insureds. Section [4](https://arxiv.org/html/2601.12655v1#S4 "4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") studies the insurance companies’ pricing game. Section [5](https://arxiv.org/html/2601.12655v1#S5 "5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium") presents numerical analyses and sensitivity results on the equilibrium premium strategies. Section [6](https://arxiv.org/html/2601.12655v1#S6 "6 Conclusion ‣ Optimal Underreporting and Competitive Equilibrium") concludes the paper. All proofs are placed in Appendix [A](https://arxiv.org/html/2601.12655v1#A1 "Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium").

## 2 Model

We consider an insurance market consisting of two *competing* insurance companies (insurers) and a continuum of insureds who seek insurance coverage on some non-life risk (such as automobile collision risk). On an infinite time horizon T:={1,2,⋯}T:=\{1,2,\cdots\}, we model each insured’s losses by a series of independently and identically distributed (i.i.d) nonnegative random variables, {Lt}t∈𝒯\{L\_{t}\}\_{t\in\mathcal{T}}, in which Lt​=𝑑​LL\_{t}\overset{d}{=}L denotes the loss amount in the tt-th period (over [t−1,t)[t-1,t)) and has the same distribution as a generic random variable LL. We assume that LL is a mixture of a point mass at zero, with probability p0∈(0,1)p\_{0}\in(0,1), and a continuously distributed positive random variable with full support over (0,∞)(0,\infty) (see, e.g., Haehling von Lanzenauer ([1974](https://arxiv.org/html/2601.12655v1#bib.bib32 "Optimal claim decisions by policyholders in automobile insurance with merit-rating structures")) and Cao et al. ([2024a](https://arxiv.org/html/2601.12655v1#bib.bib6 "Equilibrium reporting strategy: two rate classes and full insurance"))). With this assumption, the cumulative distribution function (cdf) FLF\_{L} of LL is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | FL​(x)=p0+∫0xfL​(ℓ)​dℓ,x≥0,\displaystyle F\_{L}(x)=p\_{0}+\int\_{0}^{x}f\_{L}(\ell)\mathrm{d}\ell,\quad x\geq 0, |  | (1) |

in which fL​(ℓ)>0f\_{L}(\ell)>0 for all ℓ>0\ell>0 and limℓ→+∞fL​(ℓ)=0\lim\_{\ell\rightarrow+\infty}f\_{L}(\ell)=0.
We fix a filtered probability space (Ω,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}) consistent with the above loss model, where 𝔽={ℱt}t∈T\mathbb{F}=\{\mathcal{F}\_{t}\}\_{t\in T} is a filtration; denote expectation taken under ℙ\mathbb{P} by 𝔼\mathbb{E}, and any subscript of 𝔼\mathbb{E} indicates a conditional expectation.

The two insurance companies offer *full insurance* covering the loss LL for the insureds, and they each apply an NN-class bonus-malus system (BMS) to price their policies (see, e.g., Lemaire ([2012](https://arxiv.org/html/2601.12655v1#bib.bib30 "Bonus-malus systems in automobile insurance")) for a standard reference on BMS). Denoting the set of rate classes and the index set of companies by

|  |  |  |
| --- | --- | --- |
|  | 𝒩:={1,2,⋯,N}andℐ:={1,2},\displaystyle\mathcal{N}:=\{1,2,\cdots,N\}\quad\text{and}\quad\mathcal{I}:=\{1,2\}, |  |

respectively, Company i∈ℐi\in\mathcal{I} sets the premium, cni>0c^{i}\_{n}>0, for all insureds in rate class n∈𝒩n\in\mathcal{N} over each single period. Without loss of generality, assume that class 1 is the best rating class, while class NN is the worst one; as such, the premiums should satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<c1i≤c2i≤⋯≤cNi,for ​i∈ℐ.\displaystyle 0<c\_{1}^{i}\leq c\_{2}^{i}\leq\cdots\leq c\_{N}^{i},\quad\text{for }i\in\mathcal{I}. |  | (2) |

For every insured, given their current rate class n∈𝒩n\in\mathcal{N}, the BMS sets their rate class in the next period by the following rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {max⁡{n−1,1},if there is no reported loss in the current period;min⁡{n+1,N},otherwise.\displaystyle\begin{cases}\max\{n-1,1\},&\text{if there is no \emph{reported} loss in the current period};\\ \min\{n+1,N\},&\text{otherwise}.\end{cases} |  | (3) |

Note that the update of rate class relies on the *reported*, not *incurred*, loss in each period; this setting is consistent with the practice in most non-life insurance lines, such as automobile insurance and home insurance, because insurers cannot monitor the actual loss status of the insureds (or it is too costly for them to implement monitoring or audit records).

Because premiums are cheaper for insureds in good rate classes, the BMS mechanism may incentivize some insureds to deliberately hide incurred losses, so that they remain in or get updated to good rate classes. The behavior of *underreporting losses* is well documented in the insurance (see, e.g., Cohen ([2005](https://arxiv.org/html/2601.12655v1#bib.bib21 "Asymmetric information and learning: evidence from the automobile insurance market")) and Braun et al. ([2006](https://arxiv.org/html/2601.12655v1#bib.bib33 "Modeling the “pseudodeductible” in insurance claims decisions"))), and related theoretical studies show that the optimal reporting decision is to employ a *barrier* strategy (see, e.g., Remark 2.1 in Cao et al. ([2025b](https://arxiv.org/html/2601.12655v1#bib.bib34 "Optimal loss reporting in continuous time with full insurance"))). Following this strand of literature, we assume that insureds adopt a barrier strategy to decide whether they should report an incurred loss, which we explain in detail as follows. Let X={Xt}t∈TX=\{X\_{t}\}\_{t\in T} denote the state process of a representative insured, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt∈𝒳:={(n,i)|n∈𝒩,i∈ℐ}\displaystyle X\_{t}\in\mathcal{X}:=\{(n,i)|n\in\mathcal{N},\,i\in\mathcal{I}\} |  | (4) |

records the insured’s rate class nn and their insurance provider, Company ii, in the tt-th period; note that Xt∈ℱt−1X\_{t}\in\mathcal{F}\_{t-1} is known at the beginning of the tt-th period, for all t∈Tt\in T. A barrier reporting strategy bb is a (time-homogeneous) function, mapping every x∈𝒳x\in\mathcal{X} into a nonnegative number b​(x)∈ℝ+b(x)\in\mathbb{R}\_{+}, and dictates the insured to report a loss if and only if Lt>b​(Xt)L\_{t}>b(X\_{t}) in the tt-th period and to hide a loss otherwise.

Recall that there are two competing insurance companies in the market, both offering the same insurance coverage, but possibly at different premiums. In theory, insureds should simply go with the cheaper supplier; however, empirical evidence suggests that practical factors, such as service quality, company reputation, and loyalty, may deter insureds from selecting the insurer with the lowest premium (see, e.g., Cummins and Sommer ([1996](https://arxiv.org/html/2601.12655v1#bib.bib20 "Capital structure and fair profits in property-liability insurance")) and Ennew and Binks ([1996](https://arxiv.org/html/2601.12655v1#bib.bib19 "The impact of service quality and service characteristics on customer retention: small businesses and their banks"))). With this in mind, we propose a random model for the switching of insureds from one company to the other, in which the transition probability depends on the difference of the premiums charged by the two companies and is independent of the loss. To be precise, let η:ℝ↦[0,1]\eta:\mathbb{R}\mapsto[0,1] be a continuous, nondecreasing and almost everywhere differentiable function; the probability that an insured in rate class nn chooses Company 11 is given by η​(cn2−cn1)\eta(c\_{n}^{2}-c\_{n}^{1}), for all n∈𝒩n\in\mathcal{N}. The nondecreasingness of η\eta captures the fact that the bigger the premium gap, the more likely that insureds will switch to the cheaper company. One may impose further conditions on η\eta, such as limΔ​c→+∞η​(Δ​c)=1\lim\limits\_{\Delta c\to+\infty}\eta(\Delta c)=1 and limΔ​c→−∞η​(Δ​c)=0\lim\limits\_{\Delta c\to-\infty}\eta(\Delta c)=0. To fully model the state transition of insureds, we introduce the following function η~\tilde{\eta}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | η~​(cni−cnj)={1−η​(cn2−cn1),i=1,η​(cn2−cn1),i=2,\tilde{\eta}(c\_{n}^{i}-c\_{n}^{j})=\begin{cases}1-\eta(c\_{n}^{2}-c\_{n}^{1}),&i=1,\\ \eta(c\_{n}^{2}-c\_{n}^{1}),&i=2,\end{cases} |  | (5) |

for all n∈𝒩n\in\mathcal{N} and i,j∈ℐi,j\in\mathcal{I} with i≠ji\neq j.

Based on the above setup, the insured’s state XX follows a Markov chain, with the transition probabilities given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Xt+1=((n−1)∨1,i)|Xt=(n,i))=ℙ​(Lt≤b​(Xt))⋅(1−η~​(c(n−1)∨1i−c(n−1)∨1j)),ℙ​(Xt+1=((n−1)∨1,j)|Xt=(n,i))=ℙ​(Lt≤b​(Xt))⋅η~​(c(n−1)∨1i−c(n−1)∨1j),ℙ​(Xt+1=((n+1)∧N,i)|Xt=(n,i))=ℙ​(Lt>b​(Xt))⋅(1−η~​(c(n−1)∨1i−c(n−1)∨1j)),ℙ​(Xt+1=((n+1)∧N,j)|Xt=(n,i))=ℙ​(Lt>b​(Xt))⋅η~​(c(n−1)∨1i−c(n−1)∨1j),\begin{split}\mathbb{P}\left(X\_{t+1}=((n-1)\vee 1,i)\,|\,X\_{t}=(n,i)\right)&=\mathbb{P}(L\_{t}\leq b(X\_{t}))\cdot\left(1-\tilde{\eta}\Big(c\_{(n-1)\vee 1}^{i}-c\_{(n-1)\vee 1}^{j}\Big)\right),\\ \mathbb{P}\left(X\_{t+1}=((n-1)\vee 1,j)\,|\,X\_{t}=(n,i)\right)&=\mathbb{P}(L\_{t}\leq b(X\_{t}))\cdot\tilde{\eta}\Big(c\_{(n-1)\vee 1}^{i}-c\_{(n-1)\vee 1}^{j}\Big),\\ \mathbb{P}\left(X\_{t+1}=((n+1)\wedge N,i)\,|\,X\_{t}=(n,i)\right)&=\mathbb{P}(L\_{t}>b(X\_{t}))\cdot\left(1-\tilde{\eta}\Big(c\_{(n-1)\vee 1}^{i}-c\_{(n-1)\vee 1}^{j}\Big)\right),\\ \mathbb{P}\left(X\_{t+1}=((n+1)\wedge N,j)\,|\,X\_{t}=(n,i)\right)&=\mathbb{P}(L\_{t}>b(X\_{t}))\cdot\tilde{\eta}\Big(c\_{(n-1)\vee 1}^{i}-c\_{(n-1)\vee 1}^{j}\Big),\end{split} |  | (6) |

for all t∈Tt\in T, n∈𝒩n\in\mathcal{N}, and i≠j∈ℐi\neq j\in\mathcal{I}, in which m1∨m2:=max⁡{m1,m2}m\_{1}\vee m\_{2}:=\max\{m\_{1},m\_{2}\} and m1∧m2:=min⁡{m1,m2}m\_{1}\wedge m\_{2}:=\min\{m\_{1},m\_{2}\} for all m1,m2∈ℝm\_{1},m\_{2}\in\mathbb{R}. To reduce notational burden, we introduce the following short-handed notation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | n↓:=(n−1)∨1andn↑:=(n+1)∧N,n∈𝒩,\displaystyle n\_{\downarrow}:=(n-1)\vee 1\quad\text{and}\quad n\_{\uparrow}:=(n+1)\wedge N,\quad n\in\mathcal{N}, |  | (7) |

where the direction of the arrow indicates when the rate class decreases (better rating) or increases (worse rating), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​cni​j:=cni−cnj,n∈𝒩,i,j∈ℐ,i≠j,\displaystyle\Delta c\_{n}^{ij}:=c\_{n}^{i}-c\_{n}^{j},\quad n\in\mathcal{N},i,j\in\mathcal{I},i\neq j, |  | (8) |

denotes the premium difference on rate class nn between Company ii and Company jj.

To study the decision-making of both the insureds and insurance companies, we follow the Stackelberg game framework to account for both parties’ interest; see, e.g., Chen and Shen ([2018](https://arxiv.org/html/2601.12655v1#bib.bib36 "On a new paradigm of optimal reinsurance: A stochastic Stackelberg differential game between an insurer and a reinsurer")), Li and Young ([2021](https://arxiv.org/html/2601.12655v1#bib.bib38 "Bowley solution of a mean–variance game in insurance")), Cao et al. ([2022](https://arxiv.org/html/2601.12655v1#bib.bib39 "Stackelberg differential game for insurance under model ambiguity")), and Boonen and Ghossoub ([2023](https://arxiv.org/html/2601.12655v1#bib.bib37 "Bowley vs. Pareto optima in reinsurance contracting")), among many others on the application of this game model in actuarial science. In our game model, we assume that the insureds are the followers and choose their barrier reporting strategy bb, and that the insurance companies are the leaders and set the premiums 𝐜i={cni}n∈𝒩\mathbf{c}^{i}=\{c^{i}\_{n}\}\_{n\in\mathcal{N}}, i∈ℐi\in\mathcal{I}. For every premium pair (𝐜1,𝐜2)(\mathbf{c}^{1},\mathbf{c}^{2}) set by the leaders (insurance companies), the insureds seek an optimal barrier strategy b∗:=b∗​(𝐜1,𝐜2)b^{\*}:=b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}), which depends on (𝐜1,𝐜2)(\mathbf{c}^{1},\mathbf{c}^{2}), to minimize the discounted total cost (premiums plus hidden losses); we analyze the insureds’ problem in Section [3](https://arxiv.org/html/2601.12655v1#S3 "3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium"). Knowing the response b∗​(𝐜1,𝐜2)b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}) in loss reporting to their premium strategies, the insurance companies aim to maximize their expected profit, and their competition is settled via a Nash game, yielding the equilibrium premiums (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}), which in turn leads to the equilibrium reporting strategy b∗​(𝐜∗,1,𝐜∗,2)b^{\*}(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}). The insurance companies’ equilibrium premium problems are solved in Section [4](https://arxiv.org/html/2601.12655v1#S4 "4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium").

## 3 The insureds’ optimal reporting problem

In this section, we formally introduce, and then solve, the insureds’ optimal reporting problem, when the premiums (𝐜1,𝐜2)(\mathbf{c}^{1},\mathbf{c}^{2}) are given from the insurance companies. The optimal barrier strategy b∗:=b∗​(𝐜1,𝐜2)b^{\*}:=b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}) is obtained in Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium").

In the analysis, we consider a representative insured whose initial state X0X\_{0}, though fixed, can take any value in the feasible set 𝒳\mathcal{X}. Because the state space 𝒳\mathcal{X} is finite, a barrier strategy bb (as a mapping) is equivalent to an N×2N\times 2 matrix {bni}n∈𝒩,i∈ℐ\{b\_{n}^{i}\}\_{n\in\mathcal{N},i\in\mathcal{I}}, with the one-to-one correspondence b​(x=(n,i))=bni≥0b(x=(n,i))=b\_{n}^{i}\geq 0. For convenience, we write b={bni}n∈𝒩,i∈ℐb=\{b\_{n}^{i}\}\_{n\in\mathcal{N},i\in\mathcal{I}} as a barrier strategy hereafter, and we denote by ℬ\mathcal{B} the set of all admissible barrier strategies, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ={(an​i)∈ℝ+N×2|an​i≥0,∀n∈𝒩,i∈ℐ}.\displaystyle\mathcal{B}=\bigl\{(a\_{ni})\in\mathbb{R}\_{+}^{N\times 2}\;\big|\;a\_{ni}\geq 0,\ \forall\,n\in\mathcal{N},i\in\mathcal{I}\bigr\}. |  | (9) |

Let 𝒞\mathcal{C} denote the set of feasible premiums (formally defined by ([15](https://arxiv.org/html/2601.12655v1#S4.E15 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")) later). We formulate the insured’s optimal reporting problem below.

###### Problem 3.1.

Given the premium pair (𝐜1,𝐜2)∈𝒞2(\mathbf{c}^{1},\mathbf{c}^{2})\in\mathcal{C}^{2} set by the two insurance companies, the representative insured seeks an optimal barrier strategy b∗:=b∗​(𝐜1,𝐜2)b^{\*}:=b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}) that minimizes the discount total cost

|  |  |  |  |
| --- | --- | --- | --- |
|  | b∗=arg​minb∈ℬ⁡𝔼​[∑t=1∞δt​(c​(Xt)+Lt⋅𝟏{Lt≤b​(Xt)})|X1∈𝒳]:=arg​minb∈ℬ⁡V​(X1;b),\displaystyle b^{\*}=\operatorname\*{arg\,min}\_{b\in\mathcal{B}}\,\mathbb{E}\left[\sum\_{t=1}^{\infty}\delta^{t}\left(c(X\_{t})+L\_{t}\cdot\mathbf{1}\_{\{L\_{t}\leq b(X\_{t})\}}\right)\Big|X\_{1}\in\mathcal{X}\right]:=\operatorname\*{arg\,min}\_{b\in\mathcal{B}}V(X\_{1};b), |  | (10) |

where δ∈(0,1)\delta\in(0,1) is a discounting factor, 𝟏D\mathbf{1}\_{D} is the indicator function of a set DD,

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(Xt)=cniandb​(Xt)=bni, for all ​Xt=(n,i)∈𝒩×ℐ.\displaystyle c(X\_{t})=c\_{n}^{i}\quad\text{and}\quad b(X\_{t})=b\_{n}^{i},\quad\text{ for all }X\_{t}=(n,i)\in\mathcal{N}\times\mathcal{I}. |  | (11) |

We call V∗​(n,i):=infb∈ℬV​(n,i;b)V^{\*}(n,i):=\inf\_{b\in\mathcal{B}}V(n,i;b) the *value function* for the initial state X1=(n,i)∈𝒳X\_{1}=(n,i)\in\mathcal{X}.

We briefly explain the insured’s problem as follows. At time t−1t-1, the insured’s state Xt=(n,i)∈𝒩×ℐX\_{t}=(n,i)\in\mathcal{N}\times\mathcal{I} is observable; that is, they are in rate class n∈𝒩n\in\mathcal{N} and buy insurance for the tt-th period from Company i∈ℐi\in\mathcal{I}, with both known at the beginning of the tt-th period. The total cost in the tt-th period is the sum of the insurance premium c​(Xt)c(X\_{t}) and the hidden loss LtL\_{t}, should it fall below the reporting barrier b​(Xt)b(X\_{t}).
In regardless of their initial state X1X\_{1}, the insured may switch to a different company at any time and reach any rate class over the infinite horizon; as such, their reporting decision must account for the entire state space 𝒳\mathcal{X}, not just for the initial state. This explains why every reporting strategy bb is a full matrix {bni}\{b\_{n}^{i}\} covering all possible (n,i)∈𝒳(n,i)\in\mathcal{X}. As the notation suggests, we expect the insured’s optimal strategy b∗b^{\*} to depend on the premium pair (𝐜1,𝐜2)(\mathbf{c}^{1},\mathbf{c}^{2}), and if such dependence relation needs to be emphasized, we write it as b∗​(𝐜1,𝐜2)b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}).

We show that Problem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmproblem1 "Problem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") admits a unique solution b∗b^{\*}, and it satisfies certain continuity condition.

###### Theorem 3.1.

For all 𝐜:=(𝐜1,𝐜2)∈𝒞2\mathbf{c}:=(\mathbf{c}^{1},\mathbf{c}^{2})\in\mathcal{C}^{2}, there exists a unique optimal barrier strategy b∗={bn∗,i​(𝐜)}n∈𝒩,i∈ℐb^{\*}=\{b^{\*,i}\_{n}(\mathbf{c})\}\_{n\in\mathcal{N},i\in\mathcal{I}} to the insured’s reporting problem in ([10](https://arxiv.org/html/2601.12655v1#S3.E10 "In Problem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")), and the mapping, 𝐜↦bn∗,i​(𝐜){\bf c}\mapsto b^{\*,i}\_{n}(\mathbf{c}), is continuous.
Moreover, we have the following characterization of the optimal barrier strategy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bn∗,i\displaystyle b^{\*,i}\_{n} | =0∨δ[(1−η~(Δcn↑i​j))V∗(n↑,i)+η~(Δcn↑i​j)V∗(n↑,j)\displaystyle=0\vee\delta\Bigl[\left(1-\tilde{\eta}\big(\Delta c^{ij}\_{n\_{\uparrow}}\big)\right)V^{\*}(n\_{\uparrow},i)+\tilde{\eta}\big(\Delta c^{ij}\_{n\_{\uparrow}}\big)V^{\*}(n\_{\uparrow},j) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(1−η~(Δcn↓i​j))V∗(n↓,i)−η~(Δcn↓i​j)V∗(n↓,j)]:=0∨φ(n,i),\displaystyle\quad-\left(1-\tilde{\eta}\big(\Delta c^{ij}\_{n\_{\downarrow}}\big)\right)V^{\*}(n\_{\downarrow},i)-\tilde{\eta}\big(\Delta c^{ij}\_{n\_{\downarrow}}\big)V^{\*}(n\_{\downarrow},j)\Bigr]:=0\vee\varphi(n,i), |  | (12) |

in which j=3−i∈ℐj=3-i\in\mathcal{I}, n↓n\_{\downarrow} and n↑n\_{\uparrow} (rating up or down by one class) are defined in ([7](https://arxiv.org/html/2601.12655v1#S2.E7 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")), and Δ​cni​j\Delta c\_{n}^{ij} (premium difference) is given by ([8](https://arxiv.org/html/2601.12655v1#S2.E8 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")).

###### Remark 3.1.

By Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium"), bn∗,i>0b\_{n}^{\*,i}>0 if and only if φ​(n,i)>0\varphi(n,i)>0, and this result is intuitive because φ\varphi in ([12](https://arxiv.org/html/2601.12655v1#S3.E12 "In Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")) can be interpreted as the “difference in cost” between hiding a loss and reporting it. By recalling the definition of η~\tilde{\eta} in ([5](https://arxiv.org/html/2601.12655v1#S2.E5 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")) and using ([12](https://arxiv.org/html/2601.12655v1#S3.E12 "In Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")), we get φ​(n,1)=φ​(n,2)\varphi(n,1)=\varphi(n,2) for all n∈𝒩n\in\mathcal{N}. As such, the insureds’ optimal barrier strategy is independent of the insurance companies from which they purchase insurance; that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | bn∗,1=bn∗,2for all ​n∈𝒩.\displaystyle b\_{n}^{\*,1}=b\_{n}^{\*,2}\quad\text{for all }n\in\mathcal{N}. |  | (13) |

Because of this symmetry result, we write b∗={bn∗}n∈𝒩b^{\*}=\{b^{\*}\_{n}\}\_{n\in\mathcal{N}}, without the company index i∈ℐi\in\mathcal{I}, as the insureds’ optimal barrier strategy.

In the special case of two rate classes (N=2N=2), it is obvious from the definition of φ​(n,i)\varphi(n,i) that b1∗=b2∗b\_{1}^{\*}=b\_{2}^{\*} (that is, the optimal barrier is the *same* for both rate classes).

###### Remark 3.2.

The optimization objective presented in Problem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmproblem1 "Problem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") aims to minimize the insured’s discounted total expenses, and it is widely used in the literature on loss (under)reporting (see, e.g., Haehling von Lanzenauer ([1974](https://arxiv.org/html/2601.12655v1#bib.bib32 "Optimal claim decisions by policyholders in automobile insurance with merit-rating structures")), Robinson and Zheng ([2010](https://arxiv.org/html/2601.12655v1#bib.bib22 "Moral hazard, insurance claims, and repeated insurance contracts")), and Charpentier et al. ([2017](https://arxiv.org/html/2601.12655v1#bib.bib7 "Optimal claiming strategies in bonus malus systems and implied markov chains"))). The linearity in the objective (see ([10](https://arxiv.org/html/2601.12655v1#S3.E10 "In Problem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium"))) simplifies the optimization problem and helps obtain an analytical solution to the optimal reporting strategy. From the perspective of expected utility theory (EUT), this linear preference is equivalent to assuming that insureds are *risk-neutral*; alternatively, one may apply a utility function to the insureds’ wealth (expenses), as suggested by the standard EUT. Cao et al. ([2024a](https://arxiv.org/html/2601.12655v1#bib.bib6 "Equilibrium reporting strategy: two rate classes and full insurance")) consider both risk-neutral and risk-averse insureds in their study; see Sections 3 and 4 therein for comparison.

Suppose that insureds are risk-averse in the sense that they apply a (strictly increasing) utility function UU to the expenses in each period. Instead of ([10](https://arxiv.org/html/2601.12655v1#S3.E10 "In Problem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")), they now solve the following reporting problem:

|  |  |  |
| --- | --- | --- |
|  | b~∗=arg⁡minb∈ℬ⁡𝔼​[∑t=1∞δt​U​(c​(Xt)+Lt⋅𝟏{Lt≤b​(Xt)})|X1∈𝒳]:=V~​(X1;b).\displaystyle\tilde{b}^{\*}=\arg\min\_{b\in\mathcal{B}}\,\mathbb{E}\left[\sum\_{t=1}^{\infty}\delta^{t}\,U\left(c(X\_{t})+L\_{t}\cdot\mathbf{1}\_{\{L\_{t}\leq b(X\_{t})\}}\right)\Big|X\_{1}\in\mathcal{X}\right]:=\tilde{V}(X\_{1};b). |  |

It is pleasing to report that all the results in Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") hold in a parallel way. Indeed, the above b~∗\tilde{b}^{\*} is unique, and it is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | b~n∗,i=0∨(U−1​[φ~​(n,i)+U​(cni)]−cni),n∈𝒩,i∈ℐ,\tilde{b}\_{n}^{\*,i}=0\vee\left(U^{-1}\left[\tilde{\varphi}(n,i)+U(c\_{n}^{i})\right]-c\_{n}^{i}\right),\quad n\in\mathcal{N},i\in\mathcal{I}, |  | (14) |

where φ~​(n,i)\tilde{\varphi}(n,i) is defined similarly to φ​(n,i)\varphi(n,i) with V∗V^{\*} replaced by the new value function V~∗\tilde{V}^{\*}.

## 4 The insurance companies’ pricing game

We obtain the insureds’ optimal barrier strategy b∗​(𝐜1,𝐜2)b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}) for reporting losses in Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium"), in response to the premium strategies (𝐜1,𝐜2)(\mathbf{c}^{1},\mathbf{c}^{2}) from two competing insurance companies. Knowing this optimal response function b∗​(𝐜1,𝐜2)b^{\*}(\mathbf{c}^{1},\mathbf{c}^{2}), the two insurance companies set their own premiums for the BMS to maximize the expected profit from the insurance business. As described in the setup, this pricing game is modeled as a two-step Stackelberg-Nash game: in the first step, Company ii (i=1,2i=1,2) solves its respective Stackelberg game with the insureds to obtain 𝐜¯i​(𝐜3−i)\mathbf{\bar{c}}^{i}(\mathbf{c}^{3-i}), when its competitor adopts strategy 𝐜3−i\mathbf{c}^{3-i}; in the second step, the two companies set the Nash equilibria (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) as their final premiums. The goal of this section is to study this pricing game.

We first define the set of admissible premiums for each insurance company as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞={(c1,⋯,cN)∈ℝ+N:c1≤c2≤⋯≤cN​ and ​cn∈[𝔼​[L],M]​ for all ​n∈𝒩},\displaystyle\mathcal{C}=\left\{(c\_{1},\cdots,c\_{N})\in\mathbb{R}\_{+}^{N}:c\_{1}\leq c\_{2}\leq\cdots\leq c\_{N}\text{ and }c\_{n}\in[\mathbb{E}[L],M]\text{ for all }n\in\mathcal{N}\right\}, |  | (15) |

in which M>0M>0 is a constant. In the above definition, the first condition is exactly ([2](https://arxiv.org/html/2601.12655v1#S2.E2 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")), as required by the ranking of all rate classes; in the second condition, cn≥𝔼​[L]c\_{n}\geq\mathbb{E}[L] is the so-called nonnegative loading condition (insurance companies ruin for sure if this fails), while MM is an upper bound on the premium so that insureds prefer purchasing full insurance to self-insurance.

For every admissible premium pair 𝐜=(𝐜1,𝐜2)∈𝒞2{\mathbf{c}}=(\mathbf{c}^{1},\mathbf{c}^{2})\in\mathcal{C}^{2}, let b∗​(𝐜)b^{\*}(\mathbf{c}) denote the insureds’ optimal barrier reporting strategy as characterized by ([12](https://arxiv.org/html/2601.12655v1#S3.E12 "In Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")). Recall from ([13](https://arxiv.org/html/2601.12655v1#S3.E13 "In Remark 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")) that b∗​(𝐜)b^{\*}(\mathbf{c}) is the same for insureds of both insurance companies. We obtain Company ii’s expected per-period profit from premium strategy 𝐜i={cni}n∈𝒩\mathbf{c}^{i}=\{c\_{n}^{i}\}\_{n\in\mathcal{N}}, when Company jj adopts 𝐜j\mathbf{c}^{j}, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ji​(𝐜i;𝐜j):=𝔼​[∑n=1N(cni−L⋅𝟏{L>bn∗​(𝐜)})​p​(n,i;𝐜)],i=1,2,j=3−i,\displaystyle J^{i}({\bf c}^{i};{\bf c}^{j}):=\mathbb{E}\left[\sum\_{n=1}^{N}\left(c\_{n}^{i}-L\cdot\mathbf{1}\_{\{L>b\_{n}^{\*}(\mathbf{c})\}}\right)p(n,i;\mathbf{c})\right],\quad i=1,2,\,j=3-i, |  | (16) |

where p​(n,i;𝐜)p(n,i;\mathbf{c}) denotes the long-run proportion of insureds in rate class n∈𝒩n\in\mathcal{N} who are insured
with Company ii, given the premium pair 𝐜\mathbf{c}. Under the optimal barrier reporting strategy b∗b^{\*},
the insureds’ state process evolves as a time-homogeneous Markov chain on a finite state space.
Standard Markov chain arguments then imply that the cross-sectional distribution of insureds converges to a unique stationary distribution. Let 𝒯b∗\mathcal{T}\_{b^{\*}} denote the corresponding transition
matrix. The stationary distribution vector pp is characterized as the solution to

|  |  |  |
| --- | --- | --- |
|  | (I−𝒯b∗⊤)​p=0,(I-\mathcal{T}\_{b^{\*}}^{\top})p=0, |  |

together with the normalization condition 𝟏⊤​p=1\mathbf{1}^{\top}p=1. Consequently, p​(n,i;𝐜)p(n,i;\mathbf{c})
represents the steady-state proportion of insureds in class nn with Company ii, endogenously
induced by the optimal reporting behavior and the premium pair 𝐜\mathbf{c}.

###### Definition 4.1.

For every fixed 𝐜2∈𝒞\mathbf{c}^{2}\in\mathcal{C}, denote 𝐜¯1​(𝐜2):=arg​sup𝐜1∈𝒞J1​(𝐜1;𝐜2)\mathbf{\bar{c}}^{1}(\mathbf{c}^{2}):=\arg\sup\limits\_{\mathbf{c}^{1}\in\mathcal{C}}\,J^{1}(\mathbf{c}^{1};\mathbf{c}^{2}) as Company 1’s optimal premium strategy; for every fixed 𝐜1∈𝒞\mathbf{c}^{1}\in\mathcal{C}, denote 𝐜¯2​(𝐜1):=arg​sup𝐜2∈𝒞J2​(𝐜2;𝐜1)\mathbf{\bar{c}}^{2}(\mathbf{c}^{1}):=\arg\sup\limits\_{\mathbf{c}^{2}\in\mathcal{C}}\,J^{2}(\mathbf{c}^{2};\mathbf{c}^{1}) as Company 2’s optimal premium strategy. A premium pair (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) is called an equilibrium pricing strategy if it is a fixed point of the mapping (𝐜1,𝐜2)↦(𝐜¯1​(𝐜2),𝐜¯2​(𝐜1))(\mathbf{c}^{1},\mathbf{c}^{2})\mapsto(\mathbf{\bar{c}}^{1}(\mathbf{c}^{2}),\mathbf{\bar{c}}^{2}(\mathbf{c}^{1})).

The equilibrium pricing strategy (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) is defined as an equilibrium to a (non-cooperative) Nash game, and such a definition is well recognized in the economics literature. However, finding an analytical solution for (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) under a general BMS is extremely challenging. Indeed, several recent works that study loss underreporting in discrete time only obtain analytical results when the BMS has two classes (see, e.g., Cao et al. ([2024a](https://arxiv.org/html/2601.12655v1#bib.bib6 "Equilibrium reporting strategy: two rate classes and full insurance"))). This motivates us to study the insurance companies’ pricing game for a 2-class BMS. To improve readability, we place all the proofs in Appendix [A](https://arxiv.org/html/2601.12655v1#A1 "Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium").

In the rest of this section, we assume that the BMS has two rate classes (with N=2N=2), and Class 1 is the “good” class, while Class 2 is the “bad” class. We further assume that both companies apply the same proportional penalty to the bad class; that is, for all 𝐜1={c11,c21}∈𝒞\mathbf{c}^{1}=\{c\_{1}^{1},c\_{2}^{1}\}\in\mathcal{C} and 𝐜2={c12,c22}∈𝒞\mathbf{c}^{2}=\{c\_{1}^{2},c\_{2}^{2}\}\in\mathcal{C}, there exists a common penalty κ∈(1,2)\kappa\in(1,2) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | c21=κ​c11andc22=κ​c12.\displaystyle c\_{2}^{1}=\kappa\,c^{1}\_{1}\quad\text{and}\quad c\_{2}^{2}=\kappa\,c\_{1}^{2}. |  | (17) |

(We impose an upper bound of 2 on the penalty κ\kappa for practical reasons.)
For notational convenience, we set

|  |  |  |
| --- | --- | --- |
|  | θ1:=c11andθ2:=c12,\displaystyle\theta\_{1}:=c^{1}\_{1}\quad\text{and}\quad\theta\_{2}:=c\_{1}^{2}, |  |

and with the above assumption, every 𝐜1\mathbf{c}^{1} (or 𝐜2\mathbf{c}^{2}) is uniquely linked with a one-dimensional parameter θ1\theta\_{1} (or θ2\theta\_{2}), which takes values from the following set (as a result of ([15](https://arxiv.org/html/2601.12655v1#S4.E15 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"))):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ:={θ∈ℝ+:θ∈[𝔼​[L],M/κ]}.\displaystyle\Theta:=\{\theta\in\mathbb{R}\_{+}:\theta\in[\mathbb{E}[L],\,M/\kappa]\}. |  | (18) |

In the model of Section [2](https://arxiv.org/html/2601.12655v1#S2 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium"), the probability that an insured chooses Company 1 over Company 2 is captured by a general, nondecreasing function η\eta, which yields the probability of switching companies in ([5](https://arxiv.org/html/2601.12655v1#S2.E5 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")). Here, we assume that η\eta is of the following exponential form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​(θ2−θ1)={k2​ek1​(θ2−θ1),θ1>θ2,1−(1−k2)​e−k1​(θ2−θ1),θ1≤θ2,\displaystyle\eta(\theta\_{2}-\theta\_{1})=\begin{cases}k\_{2}\,\mathrm{e}^{k\_{1}(\theta\_{2}-\theta\_{1})},&\theta\_{1}>\theta\_{2},\\ 1-(1-k\_{2})\,\mathrm{e}^{-k\_{1}(\theta\_{2}-\theta\_{1})},&\theta\_{1}\leq\theta\_{2},\end{cases} |  | (19) |

for all θ1,θ2∈Θ\theta\_{1},\theta\_{2}\in\Theta, where the η\eta, k2∈(0,1)k\_{2}\in(0,1) is the probability that insureds choose Company 1 when two companies offer the same premiums, and k1∈(0,1)k\_{1}\in(0,1) represents the sensitivity degree of insureds to the premium difference on the choice of an insurance provider. Note that a larger value of k1k\_{1} implies that insureds are more likely to choose the cheaper provider.

We summarize the specifications of the above 2-class BMS as follows.

###### Assumption 4.1.

The BMS has two rate classes (n=1,2n=1,2), and the premium strategies of two insurance companies, 𝐜1={c11,c21}∈𝒞\mathbf{c}^{1}=\{c\_{1}^{1},c\_{2}^{1}\}\in\mathcal{C} and 𝐜2={c12,c22}∈𝒞\mathbf{c}^{2}=\{c\_{1}^{2},c\_{2}^{2}\}\in\mathcal{C}, take the form of

|  |  |  |  |
| --- | --- | --- | --- |
|  | c11=θ1,c21=κ​θ1, and ​c12=θ2,c22=κ​θ2,\displaystyle c\_{1}^{1}=\theta\_{1},\,c\_{2}^{1}=\kappa\theta\_{1},\text{ and }c\_{1}^{2}=\theta\_{2},\,c\_{2}^{2}=\kappa\theta\_{2}, |  | (20) |

in which κ∈(1,2)\kappa\in(1,2) and θ1,θ2∈Θ\theta\_{1},\theta\_{2}\in\Theta (implying that 𝐜i\mathbf{c}^{i} is one-to-one with θi\theta\_{i}, i=1,2i=1,2). Given the premiums θ1\theta\_{1} and θ2\theta\_{2} on Class 1, the probability that insureds choose Company 1 over Company 2 is given by the η\eta function in ([19](https://arxiv.org/html/2601.12655v1#S4.E19 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")).

There are four states for the insured’s Markov state X=(n,i)X=(n,i), denoted by

|  |  |  |  |
| --- | --- | --- | --- |
|  | s1=(1,1),s2=(2,1),s3=(1,2),s4=(2,2),\displaystyle s\_{1}=(1,1),\;s\_{2}=(2,1),\;s\_{3}=(1,2),\;s\_{4}=(2,2), |  | (21) |

in which nn records their current rate class, and Company ii is their insurance provider. Given Assumption [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), we can strength the result of Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") and obtain the insured’s optimal reporting strategy in closed form.

###### Theorem 4.1.

Let Assumption [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") hold and (θ1,θ2)=(c11,c12)∈Θ2(\theta\_{1},\theta\_{2})=(c\_{1}^{1},c\_{1}^{2})\in\Theta^{2} be given. The unique optimal barrier reporting strategy b∗​(θ1,θ2)b^{\*}(\theta\_{1},\theta\_{2}) for Problem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmproblem1 "Problem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") is the same across all four states sjs\_{j} (j=1,2,3,4j=1,2,3,4), and it is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | b∗​(θ1,θ2)=δ​(κ−1)​[θ1⋅η​(θ1−θ2)+θ2⋅(1−η​(θ1−θ2))]>0.\displaystyle b^{\*}(\theta\_{1},\theta\_{2})=\delta(\kappa-1)\left[\theta\_{1}\cdot\eta(\theta\_{1}-\theta\_{2})+\theta\_{2}\cdot\big(1-\eta(\theta\_{1}-\theta\_{2})\big)\right]>0. |  | (22) |

Now knowing exactly how insureds underreport losses by the barrier strategy b∗​(θ1,θ2)b^{\*}(\theta\_{1},\theta\_{2}), the two insurance companies optimize their objective JiJ^{i} in ([16](https://arxiv.org/html/2601.12655v1#S4.E16 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")). We solve sup𝐜1∈𝒞J1​(𝐜1;𝐜2)\sup\limits\_{\mathbf{c}^{1}\in\mathcal{C}}\,J^{1}(\mathbf{c}^{1};\mathbf{c}^{2}) and sup𝐜2∈𝒞J2​(𝐜2;𝐜1)\sup\limits\_{\mathbf{c}^{2}\in\mathcal{C}}\,J^{2}(\mathbf{c}^{2};\mathbf{c}^{1}) and identify the conditions under which the optimizers 𝐜¯1​(𝐜2)\mathbf{\bar{c}}^{1}(\mathbf{c}^{2}) and 𝐜¯2​(𝐜1)\mathbf{\bar{c}}^{2}(\mathbf{c}^{1}) exist. Then, combining these conditions, we obtain the existence of the equilibrium premium strategy (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}), as presented in the next theorem. Denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | m1:=k1δ​(κ−1)2​k2​[(2​A1)∨(2​δ−A1)],A1:=k2​(2−δ​k2)2−k2,m2:=k1δ​(κ−1)2​(1−k2)​[(2​A2)∨(2​δ−A2)],A2:=(1−k2)​(2−δ​(1−k2))1+k2.\begin{split}\mathrm{m}\_{1}&:=\frac{k\_{1}}{\delta(\kappa-1)^{2}k\_{2}[(2A\_{1})\vee(2\delta-A\_{1})]},\,\hskip 28.45274ptA\_{1}:=\frac{k\_{2}(2-\delta k\_{2})}{2-k\_{2}},\\ \mathrm{m}\_{2}&:=\frac{k\_{1}}{\delta(\kappa-1)^{2}(1-k\_{2})[(2A\_{2})\vee(2\delta-A\_{2})]},\,A\_{2}:=\frac{(1-k\_{2})(2-\delta(1-k\_{2}))}{1+k\_{2}}.\end{split} |  | (23) |

###### Theorem 4.2.

Let Assumption [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") hold. There exists an equilibrium premium strategy (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) defined in Definition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") if the following three conditions hold:

* (i)

  supℓ∈ILfL′​(ℓ)fL​(ℓ)∈[−e​k12​e−1,k12]\displaystyle\sup\_{\ell\in I\_{L}}\,\frac{f\_{L}^{\prime}(\ell)}{f\_{L}(\ell)}\in\Big[-\frac{\mathrm{e}k\_{1}}{2\mathrm{e}-1},\,\frac{k\_{1}}{2}\Big], with IL:=[δ​(κ−1)​𝔼​[L],δ​(κ−1)​Mκ]I\_{L}:=\left[\delta(\kappa-1)\mathbb{E}[L],\,\frac{\delta(\kappa-1)M}{\kappa}\right];
* (ii)

  supℓ∈ILfL​(ℓ)≤m1∧m2\displaystyle\sup\_{\ell\in I\_{L}}f\_{L}(\ell)\leq\mathrm{m}\_{1}\wedge\mathrm{m}\_{2};
* (iii)

  (1−δ)​k1​Mκ≤A1∧A2\displaystyle\frac{(1-\delta)k\_{1}M}{\kappa}\leq A\_{1}\wedge A\_{2},

in which δ\delta is the discount factor, κ\kappa is the premium penalty in ([17](https://arxiv.org/html/2601.12655v1#S4.E17 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")), MM is the maximum on the premiums, fLf\_{L} is the density of the loss random variable LL, k1k\_{1}and k2k\_{2} are from ([19](https://arxiv.org/html/2601.12655v1#S4.E19 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")), and m1\mathrm{m}\_{1}, m2\mathrm{m}\_{2}, A1A\_{1} and A2A\_{2} are defined in ([23](https://arxiv.org/html/2601.12655v1#S4.E23 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")).

###### Remark 4.1.

Condition (i) in Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") indicates that when ℓ∈IL\ell\in I\_{L}, the derivative of the log density function is bounded over an interval multiplicative of parameter k1k\_{1}; this condition requires the density fLf\_{L} to vary relatively smoothly when losses are in ILI\_{L}. Losses from low-probability, high-severity insurance policies often follow heavy-tailed distributions, which typically satisfy this slowly varying condition (an example is Gamma distribution, frequently used in modeling insurance losses).

For loss distributions with fLf\_{L} bounded above by 1−p01-p\_{0} (such as Pareto distributions with shape parameter less than or equal to the minimum loss), Condition (ii) naturally holds, if the probability of losses, 1−p01-p\_{0}, satisfies

|  |  |  |
| --- | --- | --- |
|  | 1−p0≤k12​δ​(2−δ)​[k2∨(1−k2)]​(κ−1)2.1-p\_{0}\leq\frac{k\_{1}}{2\delta(2-\delta)[k\_{2}\vee(1-k\_{2})](\kappa-1)^{2}}. |  |

This condition is rather weak because κ∈(1.2,1.5)\kappa\in(1.2,1.5) in most BMS models (see Chapter 12 of Meyers and Jones ([2015](https://arxiv.org/html/2601.12655v1#bib.bib9 "Loss data analytics"))). To further illustrate the reasonableness of the technical conditions in Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), we provide in Appendix [B](https://arxiv.org/html/2601.12655v1#A2 "Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium") a concrete example in which all these conditions are simultaneously satisfied under economically plausible parameter specifications.

As seen from ([20](https://arxiv.org/html/2601.12655v1#S4.E20 "In Assumption 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")), every premium strategy (𝐜1,𝐜2)(\mathbf{c}^{1},\mathbf{c}^{2}) is uniquely linked with a pair (θ1,θ2)(\theta\_{1},\theta\_{2}), with θi\theta\_{i} being the premium charged on Class 1 from Company ii, i=1,2i=1,2. For this reason, we call (θ1∗,θ2∗)(\theta\_{1}^{\*},\theta\_{2}^{\*}) an equilibrium if it yields (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) in Definition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"). We next show an interesting result on the relative ordering of the equilibrium premiums θ1∗\theta\_{1}^{\*} and θ2∗\theta\_{2}^{\*}. Recall from ([19](https://arxiv.org/html/2601.12655v1#S4.E19 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")) that k2k\_{2} is the probability that insureds choose Company 1 when both companies offer the same premium (θ1=θ2\theta\_{1}=\theta\_{2}).

###### Proposition 4.1.

Suppose that an equilibrium premium strategy (θ1∗,θ2∗)(\theta\_{1}^{\*},\theta\_{2}^{\*}) exists. If the density function fL​(ℓ)f\_{L}(\ell) at strictly positive losses ℓ>0\ell>0 satisfies

|  |  |  |
| --- | --- | --- |
|  | supℓ∈ILℓ​fL​(ℓ)≤1(1−δ)​(κ−1),w​i​t​h​IL:=[δ​(κ−1)​𝔼​[L],δ​(κ−1)​Mκ],\sup\_{\ell\in I\_{L}}\,\ell f\_{L}(\ell)\leq\frac{1}{(1-\delta)(\kappa-1)},\,\,\,with\,\,I\_{L}:=\left[\delta(\kappa-1)\mathbb{E}[L],\,\frac{\delta(\kappa-1)M}{\kappa}\right], |  |

then the ordering of the equilibrium premiums is determined by k2k\_{2} as follows:
θ1∗≥θ2∗\theta\_{1}^{\*}\geq\theta\_{2}^{\*} when k2≥12k\_{2}\geq\frac{1}{2}, and θ1∗≤θ2∗\theta\_{1}^{\*}\leq\theta\_{2}^{\*} when k2≤12k\_{2}\leq\frac{1}{2}. In particular, θ1∗=θ2∗\theta\_{1}^{\*}=\theta\_{2}^{\*} when k2=12k\_{2}=\frac{1}{2}.

###### Remark 4.2.

The ordering results are consistent with intuition and the definition of k2k\_{2}. When k2≥1/2k\_{2}\geq 1/2, Company 1 has the preference advantage over Company 2 among insureds, and this advantage allows Company 1 to set a higher premium than Company 2 in the competition. We also note that the condition on fLf\_{L} in Proposition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") holds under the conditions of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), as shown by the inequalities below

|  |  |  |
| --- | --- | --- |
|  | supℓ∈ILℓ​fL​(ℓ)≤δ​(κ−1)​Mκ​supℓ∈ILfL​(ℓ)≤12​[k2∨(1−k2)]​(1−δ)​(κ−1)≤1(1−δ)​(κ−1).\displaystyle\sup\_{\ell\in I\_{L}}\,\ell f\_{L}(\ell)\leq\frac{\delta(\kappa-1)M}{\kappa}\,\sup\_{\ell\in I\_{L}}\,f\_{L}(\ell)\leq\frac{1}{2[k\_{2}\vee(1-k\_{2})](1-\delta)(\kappa-1)}\leq\frac{1}{(1-\delta)(\kappa-1)}. |  |

Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") establishes the existence of an equilibrium premium strategy (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) (or equivalently, (θ1∗,θ2∗)(\theta\_{1}^{\*},\theta\_{2}^{\*})), under three technical conditions. Remark [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmremark1 "Remark 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") offers some explanations to these conditions; however, it remains unclear whether all three conditions hold at the same time, as required by Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), under practical specifications. In the rest of this section, we provide an example offering a positive answer to this question.

## 5 Numerical analysis

Under the 2-class BMS in Section [4](https://arxiv.org/html/2601.12655v1#S4 "4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") shows that the equilibrium premium strategy (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) in Definition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") exists, when certain technical conditions hold. However, the equilibrium premiums depend strongly on the loss distribution, and they do not admit an analytical solution. As such, we conduct a numerical analysis in this section to gain further insights of the equilibrium premiums. Note that the analysis below focuses on the same 2-class BMS as in Section [4](https://arxiv.org/html/2601.12655v1#S4 "4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), under which a premium strategy (𝐜1,𝐜2)=({c11,c21},{c12,c22})(\mathbf{c}^{1},\mathbf{c}^{2})=(\{c\_{1}^{1},c\_{2}^{1}\},\{c\_{1}^{2},c\_{2}^{2}\}) is one-to-one with (θ1,θ2)∈Θ2(\theta\_{1},\theta\_{2})\in\Theta^{2}, as shown in ([20](https://arxiv.org/html/2601.12655v1#S4.E20 "In Assumption 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")). For this reason, we call (θ1∗,θ2∗)(\theta\_{1}^{\*},\theta\_{2}^{\*}) an equilibrium if it yields (𝐜∗,1,𝐜∗,2)(\mathbf{c}^{\*,1},\mathbf{c}^{\*,2}) in Definition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium").

To start, we assume that the insured’s per-period loss LL is a mixture of a point mass at zero and a G​a​m​m​a​(α,λ)Gamma(\alpha,\lambda) distribution (see Example [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmexample1 "Example B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium")), with weights p0∈(0,1)p\_{0}\in(0,1) and 1−p01-p\_{0}, respectively.
We set the parameter values for the model as listed in Table [1](https://arxiv.org/html/2601.12655v1#S5.T1 "Table 1 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium"), which constitutes the base case for our numerical study. When we study the impact of a particular parameter on the equilibrium (θ1∗,θ2∗)(\theta\_{1}^{\*},\theta\_{2}^{\*}), we let this parameter vary over a reasonable range (around its base value) but keep all other parameters fixed as in Table [1](https://arxiv.org/html/2601.12655v1#S5.T1 "Table 1 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium"). Recall that k1k\_{1} and k2k\_{2} are from the function η\eta in ([19](https://arxiv.org/html/2601.12655v1#S4.E19 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")), and κ\kappa is the premium penalty on Class 2 (see ([20](https://arxiv.org/html/2601.12655v1#S4.E20 "In Assumption 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"))).

| Parameter | Symbol | Value |
| --- | --- | --- |
| ℙ​(L=0)\mathbb{P}(L=0) | p0p\_{0} | 0.90.9 |
| L​|L>​0∼G​a​m​m​a​(α,λ)L|L>0\sim\,Gamma(\alpha,\lambda) | (α,λ)(\alpha,\lambda) | (1.2,0.0085)(1.2,0.0085) |
| Upper bound on the premium | MM | 35.85335.853 |
| Price sensitivity | k1k\_{1} | 0.0150.015 |
| Preference for Company 1 | k2k\_{2} | 0.80.8 |
| Premium penalty | κ\kappa | 1.251.25 |
| Discount factor | δ\delta | 0.970.97 |

Table 1: Model parameters in the base case

Assuming that the model parameters are given in Table [1](https://arxiv.org/html/2601.12655v1#S5.T1 "Table 1 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium"), we numerically compute the equilibrium premiums and obtain

|  |  |  |
| --- | --- | --- |
|  | θ1∗≈35.8293andθ2∗≈33.4501.\displaystyle\theta\_{1}^{\*}\approx 35.8293\quad\text{and}\quad\theta\_{2}^{\*}\approx 33.4501. |  |

Note that we have k2>0.5k\_{2}>0.5, and the above results confirm that θ1∗>θ2∗\theta\_{1}^{\*}>\theta\_{2}^{\*} as predicted by Proposition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"). Before we proceed to conducting sensitivity analysis, we note that the kinks (i.e., non-differentiable points) observed in the subsequent figures arise from the presence of an upper bound on premiums (MM in ([15](https://arxiv.org/html/2601.12655v1#S4.E15 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"))), which truncates the curves that would otherwise vary smoothly with respect to the parameters.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1: Effect of the price sensitivity coefficient k1k\_{1} on the equilibrium premiums

In the first sensitivity study, we investigate how the price sensitivity coefficient k1k\_{1} of the insureds affects the equilibrium premiums θ1∗\theta\_{1}^{\*} and θ2∗\theta\_{2}^{\*}, and their difference.
By ([19](https://arxiv.org/html/2601.12655v1#S4.E19 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")), the bigger the coefficient k1k\_{1}, the more likely that an insured chooses the cheaper insurance company to purchase insurance. The left panel of Figure [1](https://arxiv.org/html/2601.12655v1#S5.F1 "Figure 1 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium") shows that the equilibrium premiums θ1∗\theta\_{1}^{\*} and θ2∗\theta\_{2}^{\*} remain constant initially and then decrease as k1k\_{1} increases. For very small k1k\_{1}, the maximum premium constraint is binding, which explains the overlapping flat part.
As k1k\_{1} increases, however, insureds are more sensitive to the price difference between the two companies, and this naturally drives both companies to lower their premiums to attract insureds.
The right panel of Figure [1](https://arxiv.org/html/2601.12655v1#S5.F1 "Figure 1 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium") shows that the premium difference θ1∗−θ2∗\theta\_{1}^{\*}-\theta\_{2}^{\*} is initially equal to zero and then exhibits a sharp rise, followed by a monotonic decline.
When price sensitivity increases from very low levels, the market transitions from a regime dominated by intrinsic preference (or brand bias) to one in which price becomes a more important factor in the insured’s choice on insurance provider.
In this transition region, the disadvantaged insurer (Company 2) faces a higher effective demand elasticity, while the advantaged insurer (Company 1) benefits from a larger and more loyal base of customers. Consequently, Company 2 has a stronger incentive to reduce its premiums than Company 1 in the competition. This asymmetric adjustment leads to an increase in the equilibrium premium difference in the early stage of the transition. Such a behavior is consistent with the “fat-cat” strategy described by Fudenberg and Tirole ([1984](https://arxiv.org/html/2601.12655v1#bib.bib31 "The fat-cat effect, the puppy-dog ploy, and the lean and hungry look")), whereby an incumbent with market power responds less aggressively to emerging competitive threats, relying instead on its established advantage.
However, once k1k\_{1} exceeds a critical threshold, the price itself becomes the dominating factor when insureds choose their insurance provider, and the preference advantage of Company 1 over Company 2 weakens in the insureds’ decision. In this high-sensitivity regime, both companies apply similar pricing strategies, resulting in a rapid convergence of premiums.

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 2: Effect of the preference coefficient k2k\_{2} for Company 1 on the equilibrium premiums

Next, we examine the impact of the preference coefficient k2k\_{2} on the equilibrium premiums and their difference. Recall from ([19](https://arxiv.org/html/2601.12655v1#S4.E19 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")) that k2k\_{2} is the probability that an insured chooses Company 1 when two companies offer the same premiums; therefore, k2>0.5k\_{2}>0.5 (resp., k2<0.5k\_{2}<0.5) implies a preference advantage for Company 1 (resp., Company 2). The order of the equilibrium premiums in the left panel of Figure [2](https://arxiv.org/html/2601.12655v1#S5.F2 "Figure 2 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium") is fully consistent with the meaning of k2k\_{2} and confirms the theoretical result in Proposition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"). As long as the preference effect is strong enough (i.e., when k2k\_{2} is close to either 0 or 1), the advantaged company charges the maximum allowed premiums, but the disadvantaged company offers very low premiums in order to attract customers. It is worth pointing out that the equilibrium premiums from the two companies coincide over an *interval* around k2=0.5k\_{2}=0.5, not limited to k2=0.5k\_{2}=0.5; this is due to the existence of an upper bound on premiums, and for the particular base parameters, the equilibrium premiums are achieved at the upper bound for a range of k2k\_{2} near 0.5. Indeed, if we manually lift out the upper bound MM to 120, the difference θ1∗−θ2∗\theta\_{1}^{\*}-\theta\_{2}^{\*} is strictly increasing (from around -30 to 30) when k2k\_{2} increases from 0 to 1, and the two premiums are only equal at the point k2=0.5k\_{2}=0.5. (Graphs for this case are available upon request, and here we omit them to save space.)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 3: Effect of the upper bound on the premium MM on the equilibrium premiums

Finally, Figure [3](https://arxiv.org/html/2601.12655v1#S5.F3 "Figure 3 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium") demonstrates the impact of the upper bound on the premium MM on the equilibrium premiums and their difference. Figure [3](https://arxiv.org/html/2601.12655v1#S5.F3 "Figure 3 ‣ 5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium") (left panel) confirms an overall increasing relationship between the equilibrium premiums and the upper bound on the premium. In fine detail, the graph illustrates that the equilibrium premiums of the two insurance companies initially increase synchronously as the upper bound on the premium MM rises. Subsequently, the increase in θ1∗\theta\_{1}^{\*} outpaces that of θ2∗\theta\_{2}^{\*}, and both eventually converge to stable levels. The right panel shows that when MM is small (specifically, below 30.3450), the premium difference θ1∗−θ2∗\theta\_{1}^{\*}-\theta\_{2}^{\*} remains zero; once this threshold is exceeded, the difference increases monotonically and ultimately stabilizes at a certain level.

## 6 Conclusion

This paper considers a discrete-time BMS insurance model with two competing insurance companies and a continuum of insureds, aiming to understand the strategic decisions made by insureds regarding loss reporting and by insurance companies regarding BMS premiums. For given premiums, we solve the insureds’ loss reporting problem and obtain an optimal barrier strategy that minimizes the expected total expenses. Next, knowing how insureds report losses, the insurance companies set their premiums to maximize their expected profit over a unit period, and their competition is settled by a non-cooperative Nash game. We find sufficient conditions that guarantee the existence of a Nash equilibrium for the 2-class BMS setup. These theoretical results provide economic understandings of the strategic underreporting and inter-company competition in a competitive insurance market. Numerical analyses further illustrate the economic implications of the model. When the insureds’ price sensitivity increases, the equilibrium premiums of the two insurers converge, indicating intensified competition and a reduction in market power. Conversely, stronger brand preference induces persistent price asymmetry even when both companies face identical cost structures.

From a practical perspective, the findings provide a theoretical foundation for actuarial pricing under competitive and behaviorally complex environments. Future research directions include extending the model to asymmetric information settings or heterogeneous loss distributions.

#### Acknowledgements.

Zongxia Liang is supported by the National Natural Science Foundation of China (no.12271290). The authors thank the members of the group of Mathematical Finance and Actuarial Science at the Department of Mathematical Sciences, Tsinghua University, for their helpful feedback and conversations. The authors used ChatGPT (GPT-5, OpenAI, used in December 2025) to assist in improving the grammar and writing style of this manuscript.

## References

* J. H. Abbring, P. Chiappori, and T. Zavadil (2008)
  Better safe than sorry? Ex Ante, Ex Post, and moral hazard in dynamic insurance data.
  Technical report
  Note: Available at: <https://ssrn.com/abstract=1260168>
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p1.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium").
* J. H. Abbring, P. Chiappori, and J. Pinquet (2003)
  Moral hazard and dynamic insurance data.
  Journal of the European Economic Association 1 (4),  pp. 767–820.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p1.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium").
* Allstate (2023)
  Allstate reports first quarter 2023 results.
  Note: Accessed January 14, 2026
  External Links: [Link](https://www.businesswire.com/news/home/20230430593561/en/Allstate-Reports-First-Quarter-2023-Results)
  Cited by: [Example B.1](https://arxiv.org/html/2601.12655v1#A2.Thmexample1.p2.5.4 "Example B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium").
* T. J. Boonen and M. Ghossoub (2023)
  Bowley vs. Pareto optima in reinsurance contracting.
  European Journal of Operational Research 307 (1),  pp. 382–391.
  Cited by: [§2](https://arxiv.org/html/2601.12655v1#S2.p6.9 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* M. Braun, P. S. Fader, E. T. Bradlow, and H. Kunreuther (2006)
  Modeling the “pseudodeductible” in insurance claims decisions.
  Management Science 52 (8),  pp. 1258–1272.
  Cited by: [§2](https://arxiv.org/html/2601.12655v1#S2.p3.1 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* J. Cao, D. Li, V. R. Young, and B. Zou (2022)
  Stackelberg differential game for insurance under model ambiguity.
  Insurance: Mathematics and Economics 106,  pp. 128–145.
  Cited by: [§2](https://arxiv.org/html/2601.12655v1#S2.p6.9 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* J. Cao, D. Li, V. R. Young, and B. Zou (2024a)
  Equilibrium reporting strategy: two rate classes and full insurance.
  Journal of Risk and Insurance 91 (3),  pp. 721–752.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p2.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§2](https://arxiv.org/html/2601.12655v1#S2.p1.11 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium"),
  [Remark 3.2](https://arxiv.org/html/2601.12655v1#S3.Thmremark2.p1.1.1 "Remark 3.2. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§4](https://arxiv.org/html/2601.12655v1#S4.p4.2 "4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium").
* J. Cao, D. Li, V. R. Young, and B. Zou (2024b)
  Strategic underreporting and optimal deductible insurance.
  ASTIN Bulletin 54 (3),  pp. 767–790.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p2.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§1](https://arxiv.org/html/2601.12655v1#S1.p4.10 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium").
* J. Cao, D. Li, V. R. Young, and B. Zou (2025a)
  Continuous-time optimal reporting with full insurance under the mean-variance criterion.
  Insurance: Mathematics and Economics 120,  pp. 79–90.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p2.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium").
* J. Cao, D. Li, V. R. Young, and B. Zou (2025b)
  Optimal loss reporting in continuous time with full insurance.
  SIAM Journal on Financial Mathematics 16 (2),  pp. 448–479.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p2.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§2](https://arxiv.org/html/2601.12655v1#S2.p3.1 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* A. Charpentier, A. David, and R. Elie (2017)
  Optimal claiming strategies in bonus malus systems and implied markov chains.
  Risks 5 (4),  pp. 58.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p2.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§1](https://arxiv.org/html/2601.12655v1#S1.p4.10 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [Remark 3.2](https://arxiv.org/html/2601.12655v1#S3.Thmremark2.p1.1.1 "Remark 3.2. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium").
* L. Chen and Y. Shen (2018)
  On a new paradigm of optimal reinsurance: A stochastic Stackelberg differential game between an insurer and a reinsurer.
  ASTIN Bulletin 48 (2),  pp. 905–960.
  Cited by: [§2](https://arxiv.org/html/2601.12655v1#S2.p6.9 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* A. Cohen (2005)
  Asymmetric information and learning: evidence from the automobile insurance market.
  Review of Economics and Statistics 87 (2),  pp. 197–207.
  Cited by: [§2](https://arxiv.org/html/2601.12655v1#S2.p3.1 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* J. D. Cummins and D. W. Sommer (1996)
  Capital structure and fair profits in property-liability insurance.
  Journal of Banking and Finance 20 (6),  pp. 1069–1092.
  Note: Examines competition and pricing behavior in insurance markets.
  External Links: [Document](https://dx.doi.org/10.1016/0378-4266%2895%2900024-0)
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p4.10 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§2](https://arxiv.org/html/2601.12655v1#S2.p4.10 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* C. T. Ennew and M. R. Binks (1996)
  The impact of service quality and service characteristics on customer retention: small businesses and their banks.
  British Journal of Management 7 (3),  pp. 219–230.
  Note: Service quality and brand loyalty effects on customer retention.
  External Links: [Document](https://dx.doi.org/10.1111/j.1467-8551.1996.tb00115.x)
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p4.10 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§2](https://arxiv.org/html/2601.12655v1#S2.p4.10 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* E. W. Frees (2009)
  Regression modeling with actuarial and financial applications.
  International Series on Actuarial Science, Cambridge University Press, Cambridge, UK.
  External Links: ISBN 9780521135962,
  [Document](https://dx.doi.org/10.1017/CBO9780511814372)
  Cited by: [Example B.1](https://arxiv.org/html/2601.12655v1#A2.Thmexample1.p1.2.2 "Example B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium").
* D. Fudenberg and J. Tirole (1984)
  The fat-cat effect, the puppy-dog ploy, and the lean and hungry look.
  American Economic Review 74 (2),  pp. 361–366.
  Cited by: [§5](https://arxiv.org/html/2601.12655v1#S5.p4.11 "5 Numerical analysis ‣ Optimal Underreporting and Competitive Equilibrium").
* C. Haehling von Lanzenauer (1974)
  Optimal claim decisions by policyholders in automobile insurance with merit-rating structures.
  Operations Research 22 (5),  pp. 979–990.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p1.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§2](https://arxiv.org/html/2601.12655v1#S2.p1.11 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium"),
  [Remark 3.2](https://arxiv.org/html/2601.12655v1#S3.Thmremark2.p1.1.1 "Remark 3.2. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium").
* J. P. Kmetic (1993)
  A parametric model for health care claims.
  Technical report
  Technical Report Vol. 3, Actuarial Research Clearing House, Actuarial Research Clearing House, Society of Actuaries, Schaumburg, IL, USA.
  External Links: [Link](https://www.soa.org/globalassets/assets/library/research/actuarial-research-clearing-house/1990-99/1993/arch-3/arch93v33.pdf)
  Cited by: [Appendix B](https://arxiv.org/html/2601.12655v1#A2.p4.4 "Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium").
* J. Lemaire (2012)
  Bonus-malus systems in automobile insurance.
   Springer Science & Business Media, Dordrecht, Netherlands.
  External Links: ISBN 9789401042758,
  [Document](https://dx.doi.org/10.1007/978-94-011-0631-3)
  Cited by: [§2](https://arxiv.org/html/2601.12655v1#S2.p2.2 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* D. Li and V. R. Young (2021)
  Bowley solution of a mean–variance game in insurance.
  Insurance: Mathematics and Economics 98,  pp. 35–43.
  Cited by: [§2](https://arxiv.org/html/2601.12655v1#S2.p6.9 "2 Model ‣ Optimal Underreporting and Competitive Equilibrium").
* M. Ludkovski and V. R. Young (2010)
  Ex post moral hazard and bayesian learning in insurance.
  Journal of Risk and Insurance 77 (4),  pp. 829–856.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p2.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium").
* G. Meyers and J. A. Jones (2015)
  Loss data analytics.
   Cambridge University Press, Cambridge.
  Cited by: [Remark 4.1](https://arxiv.org/html/2601.12655v1#S4.Thmremark1.p2.4.1 "Remark 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium").
* C. Robinson and B. Zheng (2010)
  Moral hazard, insurance claims, and repeated insurance contracts.
  Canadian Journal of Economics 43 (3),  pp. 967–993.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p1.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [Remark 3.2](https://arxiv.org/html/2601.12655v1#S3.Thmremark2.p1.1.1 "Remark 3.2. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium").
* Swiss Re Institute (2025)
  U.S. property and casualty outlook – april 2025.
  Note: Accessed January 14, 2026
  External Links: [Link](https://www.swissre.com/institute/research/sigma-research/Insurance-Monitoring/us-property-casualty-outlook-april-2025.html)
  Cited by: [Example B.1](https://arxiv.org/html/2601.12655v1#A2.Thmexample1.p2.5.4 "Example B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium").
* S. Zacks and B. Levikson (2004)
  Claiming strategies and premium levels for bonus malus systems.
  Scandinavian Actuarial Journal 2004 (1),  pp. 14–27.
  Cited by: [§1](https://arxiv.org/html/2601.12655v1#S1.p2.1 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium"),
  [§1](https://arxiv.org/html/2601.12655v1#S1.p4.10 "1 Introduction ‣ Optimal Underreporting and Competitive Equilibrium").

## Appendix A Proofs

### A.1 Proof of Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")

###### Proof.

Given 𝐜\mathbf{c}, denote the “one-step” cost by
rx𝐜​(b):=δ​𝔼x​[c​(x)+L1​𝟏{L1≤b​(x)}]r^{\mathbf{c}}\_{x}(b):=\delta\mathbb{E}\_{x}\left[c(x)+L\_{1}\mathbf{1}\_{\{L\_{1}\leq b(x)\}}\right], in which the subscript indicates the condition on the initial state X1=x=(n,i)∈𝒳X\_{1}=x=(n,i)\in\mathcal{X}. For every x∈𝒳x\in\mathcal{X}, the value function V∗V^{\*} satisfies the Bellman equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗​(x)=infb∈ℬ{rx𝐜​(b)+δ​∑X2(ℙx,b,𝐜​(X2)​V∗​(X2))}:=ℒ𝐜​V∗​(x),\displaystyle V^{\*}(x)=\inf\_{b\in\mathcal{B}}\,\left\{r^{\mathbf{c}}\_{x}(b)+\delta\sum\_{X\_{2}}\big(\mathbb{P}\_{x,b,\mathbf{c}}(X\_{2})\,V^{\*}(X\_{2})\big)\right\}:=\,\mathcal{L}^{\mathbf{c}}\,V^{\*}(x), |  | (24) |

where X2X\_{2} can only take one of the four states, (n↓,i)(n\_{\downarrow},i), (n↓,3−i)(n\_{\downarrow},3-i), (n↑,i)(n\_{\uparrow},i), (n↑,3−i)(n\_{\uparrow},3-i), and the transition probabilities ℙx,b,𝐜​(X2)\mathbb{P}\_{x,b,\mathbf{c}}(X\_{2}), given the premium pair 𝐜\mathbf{c}, X1=xX\_{1}=x and a barrier strategy bb, are given by ([6](https://arxiv.org/html/2601.12655v1#S2.E6 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")).

Let 𝒱:={v:𝒳↦ℝ}\mathcal{V}:=\{v:\mathcal{X}\mapsto\mathbb{R}\} and equip 𝒱\mathcal{V} with the sup norm, ‖v‖:=supx∈𝒳|v​(x)|\|v\|:=\sup\limits\_{x\in\mathcal{X}}\,|v(x)| for all v∈𝒱v\in\mathcal{V}, then, (𝒱,∥⋅∥)(\mathcal{V},\|\cdot\|) is a Banach space. We first show that ℒ𝐜:v∈𝒱↦ℒ𝐜​v∈𝒱\mathcal{L}^{\mathbf{c}}:v\in\mathcal{V}\mapsto\mathcal{L}^{\mathbf{c}}v\in\mathcal{V} is a contraction. To that end, fix an arbitrary x∈𝒳x\in\mathcal{X} and consider two functions v1,v2∈𝒱v\_{1},v\_{2}\in\mathcal{V}, assume, without loss of generality, that ℒ𝐜​v1​(x)≥ℒ𝐜​v2​(x)\mathcal{L}^{\mathbf{c}}v\_{1}(x)\geq\mathcal{L}^{\mathbf{c}}v\_{2}(x) and let {b(m)}m=1∞\{b\_{(m)}\}\_{m=1}^{\infty} be a sequence of barrier strategies achieving the infimum in ℒ𝐜​v2​(x)\mathcal{L}^{\mathbf{c}}v\_{2}(x). Then we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ𝐜​v1​(x)−ℒ𝐜​v2​(x)=infb∈ℬ(rx𝐜​(b)+δ​∑X2∈𝒳ℙx,b,𝐜​(X2)​v1​(X2))−limm→+∞(rx𝐜​(b(m))+δ​∑X2∈𝒳ℙx,b(m),𝐜​(X2)​v2​(X2))≤lim infm→+∞[(rx𝐜​(b(m))+δ​∑X2∈𝒳ℙx,b(m),𝐜​(X2)​v1​(X2))−(rx𝐜​(b(m))+δ​∑X2∈𝒳ℙx,b(m),𝐜​(X2)​v2​(X2))]≤δ​lim infm→+∞∑X2∈Sℙx,b(m),𝐜​(X2)​(v1​(X2)−v2​(X2))≤δ​‖v1−v2‖.\begin{split}&\mathcal{L}^{\mathbf{c}}v\_{1}(x)-\mathcal{L}^{\mathbf{c}}v\_{2}(x)\\ =&\inf\_{b\in\mathcal{B}}\Big(r\_{x}^{\mathbf{c}}(b)+\delta\sum\_{X\_{2}\in\mathcal{X}}\mathbb{P}\_{x,b,\mathbf{c}}(X\_{2})v\_{1}(X\_{2})\Big)-\lim\limits\_{m\to+\infty}\Big(r\_{x}^{\mathbf{c}}(b\_{(m)})+\delta\sum\_{X\_{2}\in\mathcal{X}}\mathbb{P}\_{x,b\_{(m)},\mathbf{c}}(X\_{2})v\_{2}(X\_{2})\Big)\\ \leq&\liminf\_{m\rightarrow+\infty}\bigg[\Big(r\_{x}^{\mathbf{c}}(b\_{(m)})+\delta\sum\_{X\_{2}\in\mathcal{X}}\mathbb{P}\_{x,b\_{(m)},\mathbf{c}}(X\_{2})v\_{1}(X\_{2})\Big)-\Big(r\_{x}^{\mathbf{c}}(b\_{(m)})+\delta\sum\_{X\_{2}\in\mathcal{X}}\mathbb{P}\_{x,b\_{(m)},\mathbf{c}}(X\_{2})v\_{2}(X\_{2})\Big)\bigg]\\ \leq&\delta\,\liminf\_{m\rightarrow+\infty}\sum\_{X\_{2}\in S}\mathbb{P}\_{x,b\_{(m)},\mathbf{c}}(X\_{2})\big(v\_{1}(X\_{2})-v\_{2}(X\_{2})\big)\leq\delta\|v\_{1}-v\_{2}\|.\end{split} |  | (25) |

Similarly, if ℒ𝐜​v1​(x)≤ℒ𝐜​v2​(x)\mathcal{L}^{\mathbf{c}}v\_{1}(x)\leq\mathcal{L}^{\mathbf{c}}v\_{2}(x), then 0≤ℒ𝐜​v1​(x)−ℒ𝐜​v2​(x)≤δ​‖v1−v2‖0\leq\mathcal{L}^{\mathbf{c}}v\_{1}(x)-\mathcal{L}^{\mathbf{c}}v\_{2}(x)\leq\delta\|v\_{1}-v\_{2}\|. Because δ∈(0,1)\delta\in(0,1), ℒ𝐜\mathcal{L}^{\mathbf{c}} is a contraction mapping on (𝒱,∥⋅∥)(\mathcal{V},\|\cdot\|) as claimed. By Banach Fixed-Point Theorem, it follows that there exists a unique v∗∈𝒱v^{\*}\in\mathcal{V} such that ℒ𝐜​v∗=v∗\mathcal{L}^{\mathbf{c}}v^{\*}=v^{\*}, and this v∗v^{\*} coincides with the value function V∗V^{\*} in ([24](https://arxiv.org/html/2601.12655v1#A1.E24 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")).

Next, we prove the existence and uniqueness of an optimal barrier strategy b∗b^{\*}. From ([24](https://arxiv.org/html/2601.12655v1#A1.E24 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")), we obtain, for all (n,i)=x∈𝒳(n,i)=x\in\mathcal{X},

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗(n,i)=infb∈ℬ{\displaystyle V^{\*}(n,i)=\inf\_{b\in\mathcal{B}}\Bigl\{ | δ​𝔼​[cni+L​𝟏{L≤bni}]\displaystyle\,\delta\mathbb{E}\left[c\_{n}^{i}+L\mathbf{1}\_{\{L\leq b\_{n}^{i}\}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ​ℙ​(L≤bni)​(1−η~​(Δ​cn↓i,3−i))​V∗​(n↓,i)+δ​ℙ​(L≤bni)​η~​(Δ​cn↓i,3−i)​V∗​(n↓,3−i)\displaystyle+\delta\,\mathbb{P}(L\leq b\_{n}^{i})\left(1-\tilde{\eta}(\Delta c^{i,3-i}\_{n\_{\downarrow}})\right)V^{\*}(n\_{\downarrow},i)+\delta\,\mathbb{P}(L\leq b\_{n}^{i})\,\tilde{\eta}(\Delta c^{i,3-i}\_{n\_{\downarrow}})V^{\*}(n\_{\downarrow},3-i) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δℙ(L>bni)(1−η~(Δcn↑i,3−i))V∗(n↑,i)+δℙ(L>bni)η~(Δcn↑i,3−i)V∗(n↑,3−i)}\displaystyle+\delta\,\mathbb{P}(L>b\_{n}^{i})\left(1-\tilde{\eta}(\Delta c^{i,3-i}\_{n\_{\uparrow}})\right)V^{\*}(n\_{\uparrow},i)+\delta\,\mathbb{P}(L>b\_{n}^{i})\,\tilde{\eta}(\Delta c^{i,3-i}\_{n\_{\uparrow}})V^{\*}(n\_{\uparrow},3-i)\Bigl\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | :=infb∈ℬ\displaystyle:=\inf\_{b\in\mathcal{B}} | Q​(n,i;b).\displaystyle\,Q(n,i;b). |  |

Note that Q​(n,i;b)Q(n,i;b) only depends on bnib\_{n}^{i} and is independent of the rest entries in the matrix bb. Using this result and differentiating QQ with respect to bb yield

|  |  |  |
| --- | --- | --- |
|  | ∂Q∂b=diag​{δ​fL​(bni)​[bni−φ​(n,i)]}n∈𝒩,i∈ℐ,\frac{\partial Q}{\partial b}=\text{diag}\left\{\delta f\_{L}(b\_{n}^{i})\left[b\_{n}^{i}-\varphi(n,i)\right]\right\}\_{n\in\mathcal{N},i\in\mathcal{I}}\ , |  |

in which fLf\_{L} is the density in ([1](https://arxiv.org/html/2601.12655v1#S2.E1 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")), and φ\varphi is defined in ([12](https://arxiv.org/html/2601.12655v1#S3.E12 "In Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")). As such, we have b∗​(n,i)=φ​(n,i)∨0b^{\*}(n,i)=\varphi(n,i)\vee 0, establishing the existence and uniqueness of an optimal barrier strategy simultaneously.

At the last, we prove the continuity of b∗b^{\*} with respect to the given premium pair 𝐜\mathbf{c}. Let 𝐜,𝐜^∈𝒞2\mathbf{c},\ \widehat{\mathbf{c}}\in\mathcal{C}^{2} be two premium pairs from the insurance companies and denote the corresponding value functions by V𝐜∗V^{\*}\_{\mathbf{c}} and V𝐜^∗V^{\*}\_{\widehat{\mathbf{c}}}, respectively. Using ([24](https://arxiv.org/html/2601.12655v1#A1.E24 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖V𝐜^∗−V𝐜∗‖=‖ℒ𝐜^​V𝐜^∗−ℒ𝐜​V𝐜∗‖≤‖ℒ𝐜^​V𝐜^∗−ℒ𝐜^​V𝐜∗‖+‖ℒ𝐜^​V𝐜∗−ℒ𝐜​V𝐜∗‖≤δ​‖V𝐜^∗−V𝐜∗‖+‖ℒ𝐜^​V𝐜∗−ℒ𝐜​V𝐜∗‖.\begin{split}\|V^{\*}\_{\widehat{\mathbf{c}}}-V^{\*}\_{\mathbf{c}}\|&=\|\mathcal{L}^{\widehat{\mathbf{c}}}V^{\*}\_{\widehat{\mathbf{c}}}-\mathcal{L}^{\mathbf{c}}V^{\*}\_{\mathbf{c}}\|\leq\|\mathcal{L}^{\widehat{\mathbf{c}}}V^{\*}\_{\widehat{\mathbf{c}}}-\mathcal{L}^{\widehat{\mathbf{c}}}V^{\*}\_{\mathbf{c}}\|+\|\mathcal{L}^{\widehat{\mathbf{c}}}V^{\*}\_{\mathbf{c}}-\mathcal{L}^{\mathbf{c}}V^{\*}\_{\mathbf{c}}\|\\ &\leq\delta\|V^{\*}\_{\widehat{\mathbf{c}}}-V^{\*}\_{\mathbf{c}}\|+\|\mathcal{L}^{\widehat{\mathbf{c}}}V^{\*}\_{\mathbf{c}}-\mathcal{L}^{\mathbf{c}}V^{\*}\_{\mathbf{c}}\|.\end{split} |  | (26) |

Note that ℙx,b,𝐜\mathbb{P}\_{x,b,\mathbf{c}} is continuous with respect to 𝐜\mathbf{c}, recalling the definition of ℒ𝐜\mathcal{L}\_{\mathbf{c}} in ([24](https://arxiv.org/html/2601.12655v1#A1.E24 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) and following a similar argument as in ([25](https://arxiv.org/html/2601.12655v1#A1.E25 "In Proof. ‣ A.1 Proof of Theorem 3.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")), we have

|  |  |  |
| --- | --- | --- |
|  | lim𝐜^→𝐜‖ℒ𝐜^​V𝐜∗−ℒ𝐜​V𝐜∗‖=0.\lim\_{\widehat{\mathbf{c}}\rightarrow\mathbf{c}}\|\mathcal{L}^{\widehat{\mathbf{c}}}V^{\*}\_{\mathbf{c}}-\mathcal{L}^{\mathbf{c}}V^{\*}\_{\mathbf{c}}\|=0. |  |

Combining the above results yields

|  |  |  |
| --- | --- | --- |
|  | lim𝐜^→𝐜‖V𝐜^∗−V𝐜∗‖≤(1−δ)−1​lim𝐜^→𝐜‖ℒ𝐜^​V𝐜∗−ℒ𝐜​V𝐜∗‖=0,\lim\limits\_{\widehat{\mathbf{c}}\rightarrow\mathbf{c}}\|V^{\*}\_{\widehat{\mathbf{c}}}-V^{\*}\_{\mathbf{c}}\|\leq(1-\delta)^{-1}\lim\limits\_{\widehat{\mathbf{c}}\rightarrow\mathbf{c}}\|\mathcal{L}^{\widehat{\mathbf{c}}}V^{\*}\_{\mathbf{c}}-\mathcal{L}^{\mathbf{c}}V^{\*}\_{\mathbf{c}}\|=0, |  |

which impliess that V∗V^{\*} is continuous with respect to 𝐜\mathbf{c}. From the explicit expression of b∗b^{\*}, we conclude that b∗b^{\*} is also continuous with respect to 𝐜\mathbf{c}.
∎

### A.2 Proof of Theorem [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")

###### Proof.

Given (θ1,θ2)∈Θ2(\theta\_{1},\theta\_{2})\in\Theta^{2}, the corresponding premium pair is denoted by 𝐜\mathbf{c},
we first solve for the insureds’ optimal value function V∗V^{\*} defined as follows:

|  |  |  |
| --- | --- | --- |
|  | V∗​(X1)=infb∈ℬ𝔼​[∑t=1∞δt​(c​(Xt)+Lt⋅𝟏{Lt≤b​(Xt)})|X1∈𝒳].V^{\*}(X\_{1})=\inf\_{b\in\mathcal{B}}\;\mathbb{E}\left[\sum\_{t=1}^{\infty}\delta^{t}\left(c(X\_{t})+L\_{t}\cdot\mathbf{1}\_{\{L\_{t}\leq b(X\_{t})\}}\right)\Big|X\_{1}\in\mathcal{X}\right]. |  |

For every x∈𝒳x\in\mathcal{X}, the value function V∗V^{\*} satisfies the Bellman equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗​(x)\displaystyle V^{\*}(x) | =infb∈ℬ{rx𝐜​(b)+δ​∑X2(ℙx,b,𝐜​(X2)​V∗​(X2))}:=infb∈ℬ{rx𝐜​(b)+δ​𝒯b​V∗​(x)},\displaystyle=\inf\_{b\in\mathcal{B}}\,\left\{r^{\mathbf{c}}\_{x}(b)+\delta\sum\_{X\_{2}}\big(\mathbb{P}\_{x,b,\mathbf{c}}(X\_{2})\,V^{\*}(X\_{2})\big)\right\}:=\inf\_{b\in\mathcal{B}}\,\left\{r\_{x}^{\mathbf{c}}(b)+\delta\,\mathcal{T}\_{b}V^{\*}(x)\right\}, |  |

where rx𝐜​(b):=δ​𝔼x​[c​(x)+L1​𝟏{L1≤b​(x)}]r^{\mathbf{c}}\_{x}(b):=\delta\,\mathbb{E}\_{x}\left[c(x)+L\_{1}\mathbf{1}\_{\{L\_{1}\leq b(x)\}}\right].

By Theorem [3.1](https://arxiv.org/html/2601.12655v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium") and ([13](https://arxiv.org/html/2601.12655v1#S3.E13 "In Remark 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")), there exists a unique optimal reporting strategy b∗b^{\*} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗​(x)\displaystyle V^{\*}(x) | =rx𝐜​(b∗)+(δ​𝒯b∗​V∗)​(x)\displaystyle=r\_{x}^{\mathbf{c}}(b^{\*})+(\delta\,\mathcal{T}\_{b^{\*}}V^{\*})(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | b∗​(s1)\displaystyle b^{\*}(s\_{1}) | =b∗​(s2)=b∗​(s3)=b∗​(s4):=b¯∗,\displaystyle=b^{\*}(s\_{2})=b^{\*}(s\_{3})=b^{\*}(s\_{4}):=\bar{b}^{\*}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒯b∗​V∗)​(s1)\displaystyle(\mathcal{T}\_{b^{\*}}V^{\*})(s\_{1}) | =(𝒯b∗​V∗)​(s2)=(𝒯b∗​V∗)​(s3)=(𝒯b∗​V∗)​(s4),\displaystyle=(\mathcal{T}\_{b^{\*}}V^{\*})(s\_{2})=(\mathcal{T}\_{b^{\*}}V^{\*})(s\_{3})=(\mathcal{T}\_{b^{\*}}V^{\*})(s\_{4}), |  |

in which s1,s2,s3,s4s\_{1},s\_{2},s\_{3},s\_{4} are the four states defined in ([21](https://arxiv.org/html/2601.12655v1#S4.E21 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")).
Substituting the above results into Equation ([12](https://arxiv.org/html/2601.12655v1#S3.E12 "In Theorem 3.1. ‣ 3 The insureds’ optimal reporting problem ‣ Optimal Underreporting and Competitive Equilibrium")) and writing η:=η​(θ1−θ2)\eta:=\eta(\theta\_{1}-\theta\_{2}), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | b¯∗\displaystyle\bar{b}^{\*} | =δ​[(1−η)​V∗​(s4)+η​V∗​(s3)−(1−η)​V∗​(s2)−η​V∗​(s1)]\displaystyle=\delta\left[(1-\eta)V^{\*}(s\_{4})+\eta\,V^{\*}(s\_{3})-(1-\eta)V^{\*}(s\_{2})-\eta\,V^{\*}(s\_{1})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =δ​[(1−η)​rs4𝐜​(b∗)+η​rs3𝐜​(b∗)−(1−η)​rs2𝐜​(b∗)−η​rs1𝐜​(b∗)]\displaystyle=\delta\left[(1-\eta)\,r\_{s\_{4}}^{\mathbf{c}}({b^{\*}})+\eta\,r\_{s\_{3}}^{\mathbf{c}}({b^{\*}})-(1-\eta)r\_{s\_{2}}^{\mathbf{c}}({b^{\*}})-\eta\,r\_{s\_{1}}^{\mathbf{c}}({b^{\*}})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =δ​(κ−1)​[η​θ1+(1−η)​θ2].\displaystyle=\delta(\kappa-1)\left[\eta\,\theta\_{1}+(1-\eta)\theta\_{2}\right]. |  |

∎

### A.3 Proof of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")

Under the optimal barrier reporting strategy b∗b^{\*}, the insured’s state process constitutes a time-homogeneous Markov chain with a finite state space. As a result, the cross-sectional distribution of customer states converges to a unique stationary distribution, which can be obtained by solving

|  |  |  |
| --- | --- | --- |
|  | (I−𝒯b∗⊤)​p=0,(I-\mathcal{T}\_{b^{\*}}^{\top})\,p=0, |  |

together with the normalization condition 𝟏⊤​p=1\mathbf{1}^{\top}p=1. Thus the stationary distribution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(s1;θ1,θ2)\displaystyle p(s\_{1};\theta\_{1},\theta\_{2}) | =η​d1d1+d2=η​a,p​(s2;θ1,θ2)=η​d1​(1−η)d1+d2=(1−η)​a,\displaystyle=\frac{\eta\,d\_{1}}{d\_{1}+d\_{2}}=\eta\,a,\quad\quad\quad\,\,\,p(s\_{2};\theta\_{1},\theta\_{2})=\frac{\eta\,d\_{1}(1-\eta)}{d\_{1}+d\_{2}}=(1-\eta)a, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(s3;θ1,θ2)\displaystyle p(s\_{3};\theta\_{1},\theta\_{2}) | =b2​d2d1+d2=η​(1−a),p​(s4;θ1,θ2)=(1−b2)​d2d1+d2=(1−η)​(1−a),\displaystyle=\frac{b\_{2}d\_{2}}{d\_{1}+d\_{2}}=\eta\,(1-a),\quad p(s\_{4};\theta\_{1},\theta\_{2})=\frac{(1-b\_{2})d\_{2}}{d\_{1}+d\_{2}}=(1-\eta)(1-a), |  |

where a=ℙ​[L≤b∗],b∗=δ​(κ−1)​[η​θ1+(1−η)​θ2],ηa=\mathbb{P}[L\leq b^{\*}],\,b^{\*}=\delta(\kappa-1)\left[\eta\,\theta\_{1}+(1-\eta)\theta\_{2}\right],\,\eta is defined in ([5](https://arxiv.org/html/2601.12655v1#S2.E5 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")).

Having completed the preparatory steps described above, in what follows, adopting the perspective of the insurance company, we prove the existence of the equilibrium stated in Definition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") based on Theorem [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"). We first examine the maximizers of J1J^{1} and J2J^{2}.

Fix an arbitrary i∈ℐ,θi∈Θi\in\mathcal{I},\theta\_{i}\in\Theta, we aim to show that the function Ji​(θi;θ3−i)J^{i}(\theta\_{i};\theta\_{3-i}) admits a maximizer on Θ\Theta, and that this maximizer is unique. The argument proceeds by first analyzing the local curvature of JiJ^{i} at any stationary point and then combining this local result with a global monotonicity argument.

To this end, we begin by characterizing the second-order behavior of J1J^{1} at a critical point. The following lemmas provide sufficient conditions under which a stationary point is indeed a point of strict local maximum.

###### Lemma A.1.

Let θ2∈Θ\theta\_{2}\in\Theta, and suppose that there exists θ1≤θ2\theta\_{1}\leq\theta\_{2} such that

|  |  |  |
| --- | --- | --- |
|  | ∂J1∂θ1​(θ1;θ2)=0.\frac{\partial J^{1}}{\partial\theta\_{1}}(\theta\_{1};\theta\_{2})=0. |  |

Then
∂2J1∂θ12​(θ1;θ2)<0\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}(\theta\_{1};\theta\_{2})<0
if the following conditions hold:

* (i)

  supℓ∈ILfL′​(ℓ)fL​(ℓ)∈[−e​k12​e−1,k12]\displaystyle\sup\_{\ell\in I\_{L}}\frac{f\_{L}^{\prime}(\ell)}{f\_{L}(\ell)}\in\Big[-\frac{\mathrm{e}k\_{1}}{2\mathrm{e}-1},\frac{k\_{1}}{2}\Big] with IL:=[δ​(κ−1)​𝔼​[L],δ​(κ−1)​Mκ]I\_{L}:=\left[\delta(\kappa-1)\mathbb{E}[L],\delta(\kappa-1)\frac{M}{\kappa}\right];
* (ii)

  (1−δ)​Mκ​k1≤A1\displaystyle(1-\delta)\frac{M}{\kappa}k\_{1}\leq A\_{1},

where the fL​(ℓ)f\_{L}(\ell) denotes the density function of the loss LL on the positive support and A1A\_{1} is defined in ([23](https://arxiv.org/html/2601.12655v1#S4.E23 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")).

###### Proof.

If θ1≤θ2\theta\_{1}\leq\theta\_{2}, then

|  |  |  |
| --- | --- | --- |
|  | η=1−(1−k2)​e−k1​(θ2−θ1),∂η∂θ1=k1​(η−1).\eta=1-(1-k\_{2})\mathrm{e}^{-k\_{1}(\theta\_{2}-\theta\_{1})},\quad\frac{\partial\eta}{\partial\theta\_{1}}=k\_{1}(\eta-1). |  |

The first-order condition becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | k1​(1−η)​{θ1​[a+κ​(1−a)]−𝔼​[L​𝟏{L>b∗}]}=η​[a+κ​(1−a)+(θ1​(1−κ)+b∗)​q11],k\_{1}(1-\eta)\{\theta\_{1}[a+\kappa(1-a)]-\mathbb{E}[L\mathbf{1}\_{\{L>b^{\*}\}}]\}=\eta\left[a+\kappa(1-a)+(\theta\_{1}(1-\kappa)+b^{\*})q\_{1}^{1}\right], |  | (27) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | a=ℙ​[L≤b∗],q11=∂a∂θ1=fL​(b∗)​∂b∗∂θ1=fL​(b∗)​δ​(κ−1)​[η+k1​(θ2−θ1)​(1−η)]>0.a=\mathbb{P}[L\leq b^{\*}],\,q\_{1}^{1}=\frac{\partial a}{\partial\theta\_{1}}=f\_{L}(b^{\*})\frac{\partial b^{\*}}{\partial\theta\_{1}}=f\_{L}(b^{\*})\delta(\kappa-1)[\eta+k\_{1}(\theta\_{2}-\theta\_{1})(1-\eta)]>0. |  | (28) |

We now examine the second derivative:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂2J1∂θ12=\displaystyle\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}= | −k1​(2−η)​{[a+κ​(1−a)]+(θ1​(1−κ)+b∗)​q11}⏟I1\displaystyle\underbrace{-k\_{1}(2-\eta)\left\{\left[a+\kappa(1-a)\right]+(\theta\_{1}(1-\kappa)+b^{\*})q\_{1}^{1}\right\}}\_{I\_{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +η​(δ​[η+k1​(η−1)​(θ1−θ2)]−2)​(κ−1)​q11⏟I2+η​[θ1​(1−κ)+b∗]​q111⏟I3,\displaystyle+\underbrace{\eta\left(\delta[\eta+k\_{1}(\eta-1)(\theta\_{1}-\theta\_{2})]-2\right)(\kappa-1)q\_{1}^{1}}\_{I\_{2}}+\underbrace{\eta\left[\theta\_{1}(1-\kappa)+b^{\*}\right]q\_{1}^{11}}\_{I\_{3}}, |  |

where q111=∂q11∂θ1q\_{1}^{11}=\frac{\partial q\_{1}^{1}}{\partial\theta\_{1}}. To prove ∂2J1∂θ12<0\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}<0, define h1​(θ1;θ2)=−θ1+δ​[η​θ1+(1−η)​θ2]h\_{1}(\theta\_{1};\theta\_{2})=-\theta\_{1}+\delta[\eta\,\theta\_{1}+(1-\eta)\theta\_{2}], we distinguish two situations based on the sign of h1h\_{1}. Before that, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂b∗∂θ1\displaystyle\frac{\partial b^{\*}}{\partial\theta\_{1}} | =δ​(κ−1)​[η+k1​(θ2−θ1)​(1−η)]≤δ​(κ−1)​(1+1−k2e2).\displaystyle=\delta(\kappa-1)[\eta+k\_{1}(\theta\_{2}-\theta\_{1})(1-\eta)]\leq\delta(\kappa-1)\left(1+\frac{1-k\_{2}}{\mathrm{e}^{2}}\right). |  | (29) |

Case 1: h1≥0.h\_{1}\geq 0.

In this case, we apply Condition (i) to analyze the sign of I1+I3I\_{1}+I\_{3}. Using inequality ([29](https://arxiv.org/html/2601.12655v1#A1.E29 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) and Condition (i), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | η​q111\displaystyle\eta\,q\_{1}^{11} | −q11​k1​(2−η)≤(74​η−2)​k1​q11+η​fL​(b∗)​∂2b∗∂θ12.\displaystyle-q\_{1}^{1}k\_{1}(2-\eta)\leq\left(\frac{7}{4}\eta-2\right)k\_{1}q\_{1}^{1}+\eta\,f\_{L}(b^{\*})\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}. |  | (30) |

If θ1∈(θ2−2k1,θ2]\theta\_{1}\in(\theta\_{2}-\frac{2}{k\_{1}},\theta\_{2}], then using inequality ([30](https://arxiv.org/html/2601.12655v1#A1.E30 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​q111\displaystyle\eta\,q\_{1}^{11} | −q11​k1​(2−η)≤(74​η−2)​k1​q11+δ​(κ−1)​fL​(b∗)​k1​η​(η−1)​[2+k1​(θ1−θ2)]<0.\displaystyle-q\_{1}^{1}k\_{1}(2-\eta)\leq\left(\frac{7}{4}\eta-2\right)k\_{1}q\_{1}^{1}+\delta(\kappa-1)f\_{L}(b^{\*})k\_{1}\eta(\eta-1)\left[2+k\_{1}(\theta\_{1}-\theta\_{2})\right]<0. |  |

If instead θ1≤θ2−2k1\theta\_{1}\leq\theta\_{2}-\frac{2}{k\_{1}}, then η∈[1−1−k2e2,1)\eta\in[1-\frac{1-k\_{2}}{\mathrm{e}^{2}},1). As such

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | η​q111\displaystyle\eta\,q\_{1}^{11} | −q11​k1​(2−η)≤δ​(κ−1)​k1​fL​(b∗)​η​[(74​η−2)​[η+k1​(θ2−θ1)​(1−η)]+1−k2e3]\displaystyle-q\_{1}^{1}k\_{1}(2-\eta)\leq\delta(\kappa-1)k\_{1}f\_{L}(b^{\*})\eta\left[\left(\frac{7}{4}\eta-2\right)\left[\eta+k\_{1}(\theta\_{2}-\theta\_{1})(1-\eta)\right]+\frac{1-k\_{2}}{\mathrm{e}^{3}}\right] |  | (31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <δ​(κ−1)​k1​fL​(b∗)​η​(−14+1−k2e3)<0.\displaystyle<\delta(\kappa-1)k\_{1}f\_{L}(b^{\*})\eta\left(-\frac{1}{4}+\frac{1-k\_{2}}{\mathrm{e}^{3}}\right)<0. |  | (32) |

It follows that

|  |  |  |
| --- | --- | --- |
|  | I1+I3<(κ−1)​h1​(η​q111−q11​k1​(2−η))<0.I\_{1}+I\_{3}<(\kappa-1)h\_{1}(\eta\,q\_{1}^{11}-q\_{1}^{1}k\_{1}(2-\eta))<0. |  |

Similarly, define h0​(θ1;θ2)=δ​[η+k1​(η−1)​(θ1−θ2)]−2h\_{0}(\theta\_{1};\theta\_{2})=\delta\left[\eta+k\_{1}(\eta-1)(\theta\_{1}-\theta\_{2})\right]-2. Using ℓ​e−ℓ≤e−1\ell\mathrm{e}^{-\ell}\leq\mathrm{e}^{-1}, we obtain

|  |  |  |
| --- | --- | --- |
|  | h0≤δ​(1+1−k2e)−2<2​δ−2<0,\displaystyle h\_{0}\leq\delta\left(1+\frac{1-k\_{2}}{\mathrm{e}}\right)-2<2\delta-2<0, |  |

which implies I2=η​(κ−1)​q11​h0<0.I\_{2}=\eta(\kappa-1)q\_{1}^{1}h\_{0}<0.
Thus ∂2J1∂θ12=I1+I2+I3<0.\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}=I\_{1}+I\_{2}+I\_{3}<0.

Case 2: h1<0.h\_{1}<0.

If θ1∈[θ2−2k1,θ2]\theta\_{1}\in\left[\theta\_{2}-\frac{2}{k\_{1}},\theta\_{2}\right], as

|  |  |  |
| --- | --- | --- |
|  | ∂2b∗∂θ12=δ​k1​(κ−1)​(1−η)​[k1​(θ2−θ1)−2]≤0,h1≥(δ−1)​Mκ,\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}=\delta k\_{1}(\kappa-1)(1-\eta)[k\_{1}(\theta\_{2}-\theta\_{1})-2]\leq 0,\,h\_{1}\geq(\delta-1)\frac{M}{\kappa}, |  |

combining with inequality ([29](https://arxiv.org/html/2601.12655v1#A1.E29 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")), Condition (i) and Condition (ii) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | I2+I3η​(κ−1)​q11\displaystyle\frac{I\_{2}+I\_{3}}{\eta(\kappa-1)q\_{1}^{1}} | =h0+h1​[fL′​(b∗)fL​(b∗)​∂b∗∂θ1+k1+k1​(η−2)η+k1​(η−1)​(θ1−θ2)]\displaystyle=h\_{0}+h\_{1}\left[\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}\frac{\partial b^{\*}}{\partial\theta\_{1}}+k\_{1}+\frac{k\_{1}(\eta-2)}{\eta+k\_{1}(\eta-1)(\theta\_{1}-\theta\_{2})}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h0+(1−δ)​Mκ​k1​(e2​e−1​δ​(κ−1)​(1+1−k2e2)−1+2−ηη+k1​(η−1)​(θ1−θ2))\displaystyle\leq h\_{0}+(1-\delta)\frac{M}{\kappa}k\_{1}\left(\frac{\mathrm{e}}{2\mathrm{e}-1}\delta(\kappa-1)\left(1+\frac{1-k\_{2}}{\mathrm{e}^{2}}\right)-1+\frac{2-\eta}{\eta+k\_{1}(\eta-1)(\theta\_{1}-\theta\_{2})}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <h0+k2​(2−δ​k2)​1η+k1​(η−1)​(θ1−θ2).\displaystyle<h\_{0}+k\_{2}(2-\delta k\_{2})\frac{1}{\eta+k\_{1}(\eta-1)(\theta\_{1}-\theta\_{2})}. |  | (33) |

Denote B0=η+k1​(η−1)​(θ1−θ2)∈[k2,1+1−k2e2]B\_{0}=\eta+k\_{1}(\eta-1)(\theta\_{1}-\theta\_{2})\in\left[k\_{2},1+\frac{1-k\_{2}}{\mathrm{e}^{2}}\right], then the RHS of Inequality ([33](https://arxiv.org/html/2601.12655v1#A1.E33 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) can be written as

|  |  |  |
| --- | --- | --- |
|  | δ​B0+k2​(2−δ​k2)B0−2:=g0​(B0).\delta B\_{0}+\frac{k\_{2}(2-\delta k\_{2})}{B\_{0}}-2:=g\_{0}(B\_{0}). |  |

We now verify that g0​(B0)≤0g\_{0}(B\_{0})\leq 0 on its domain. Applying the properties of the concave function, it suffices to verify that the above expression is non-positive at the endpoints with respect to B0B\_{0}.

|  |  |  |
| --- | --- | --- |
|  | g0​(k2)=δ​k2+(2−δ​k2)−2=0,\displaystyle g\_{0}(k\_{2})=\delta k\_{2}+(2-\delta k\_{2})-2=0, |  |
|  |  |  |
| --- | --- | --- |
|  | g0​(1+1−k2e2)=δ​(1+1−k2e2)+k2​(2−δ​k2)1+1−k2e2−2:=g~0​(k2)1+1−k2e2,\displaystyle g\_{0}\left(1+\frac{1-k\_{2}}{\mathrm{e}^{2}}\right)=\delta\left(1+\frac{1-k\_{2}}{\mathrm{e}^{2}}\right)+\frac{k\_{2}(2-\delta k\_{2})}{1+\frac{1-k\_{2}}{\mathrm{e}^{2}}}-2:=\frac{\tilde{g}\_{0}\left(k\_{2}\right)}{1+\frac{1-k\_{2}}{\mathrm{e}^{2}}}, |  |
|  |  |  |
| --- | --- | --- |
|  | g~0′​(k2)=2​(1−δ​k2)+2−2​δe2+2​δ​(k2−1)e4>0,g0​(1+1−k2e2)≤g~0​(1)1+1−k2e2=0.\displaystyle\tilde{g}\_{0}^{\prime}(k\_{2})=2(1-\delta k\_{2})+\frac{2-2\delta}{\mathrm{e}^{2}}+\frac{2\delta(k\_{2}-1)}{\mathrm{e}^{4}}>0,\,g\_{0}\left(1+\frac{1-k\_{2}}{\mathrm{e}^{2}}\right)\leq\frac{\tilde{g}\_{0}(1)}{1+\frac{1-k\_{2}}{\mathrm{e}^{2}}}=0. |  |

Thus g0​(B0)≤0g\_{0}(B\_{0})\leq 0 for all admissible B0B\_{0}, implying I2+I3≤0I\_{2}+I\_{3}\leq 0.

If instead θ1<θ2−2k1\theta\_{1}<\theta\_{2}-\frac{2}{k\_{1}}, as ∂2b∗∂θ12>0\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}>0, combining with inequality ([29](https://arxiv.org/html/2601.12655v1#A1.E29 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) and Condition (i), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I2+I3η​(κ−1)​q11\displaystyle\frac{I\_{2}+I\_{3}}{\eta(\kappa-1)q\_{1}^{1}} | <h0+h1​fL′​(b∗)fL​(b∗)​∂b∗∂θ1\displaystyle<h\_{0}+h\_{1}\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}\frac{\partial b^{\*}}{\partial\theta\_{1}} |  | (34) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <1κ−1​∂b∗∂θ1−2+(1−δ)​k1​Mκ​e2​e−1​∂b∗∂θ1\displaystyle<\frac{1}{\kappa-1}\frac{\partial b^{\*}}{\partial\theta\_{1}}-2+(1-\delta)k\_{1}\frac{M}{\kappa}\frac{\mathrm{e}}{2\mathrm{e}-1}\frac{\partial b^{\*}}{\partial\theta\_{1}} |  | (35) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <(1κ−1+(2−δ)​e2​e−1)​∂b∗∂θ1−2<3​e−12​e−1​(1+1e2)−2<0.\displaystyle<\left(\frac{1}{\kappa-1}+(2-\delta)\frac{\mathrm{e}}{2\mathrm{e}-1}\right)\frac{\partial b^{\*}}{\partial\theta\_{1}}-2<\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left(1+\frac{1}{\mathrm{e}^{2}}\right)-2<0. |  | (36) |

That is, I2+I3<0I\_{2}+I\_{3}<0. Together with Equation ([27](https://arxiv.org/html/2601.12655v1#A1.E27 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")):

|  |  |  |
| --- | --- | --- |
|  | I1=−k12​(1−η)​(2−η)η​{θ1​[a+κ​(1−a)]−𝔼​[L​𝟏{L>b∗}]}<0,I\_{1}=-k\_{1}^{2}\frac{(1-\eta)(2-\eta)}{\eta}\left\{\theta\_{1}[a+\kappa(1-a)]-\mathbb{E}[L\mathbf{1}\_{\{L>b^{\*}\}}]\right\}<0, |  |

we again obtain ∂2J1∂θ12<0\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}<0. Hence, the second derivative is strictly negative if ∂J1∂θ1=0\frac{\partial J^{1}}{\partial\theta\_{1}}=0.
∎

###### Lemma A.2.

Under the assumptions of Lemma [A.1](https://arxiv.org/html/2601.12655v1#A1.Thmlemma1 "Lemma A.1. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium") (Conditions (i)–(ii) in Lemma [A.1](https://arxiv.org/html/2601.12655v1#A1.Thmlemma1 "Lemma A.1. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")),
let θ2∈Θ\theta\_{2}\in\Theta, and suppose that there exists θ1≥θ2\theta\_{1}\geq\theta\_{2} such that

|  |  |  |
| --- | --- | --- |
|  | ∂J1∂θ1​(θ1;θ2)=0.\frac{\partial J^{1}}{\partial\theta\_{1}}(\theta\_{1};\theta\_{2})=0. |  |

Then ∂2J1∂θ12​(θ1;θ2)<0\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}(\theta\_{1};\theta\_{2})<0
if the following condition holds:

* (iii)

  supℓ∈ILfL​(ℓ)≤m1\displaystyle\sup\_{\ell\in I\_{L}}f\_{L}(\ell)\leq\mathrm{m}\_{1} with IL:=[δ​(κ−1)​𝔼​[L],δ​(κ−1)​Mκ]I\_{L}:=[\delta(\kappa-1)\mathbb{E}[L],\delta(\kappa-1)\frac{M}{\kappa}].

where fL​(ℓ)f\_{L}(\ell) denotes the density function of LL on the positive support and m1\mathrm{m}\_{1} is defined in ([23](https://arxiv.org/html/2601.12655v1#S4.E23 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")).

###### Proof.

In this regime,

|  |  |  |
| --- | --- | --- |
|  | η=k2​e−k1​(θ1−θ2),∂η∂θ1=−k1​η.\eta=k\_{2}\mathrm{e}^{-k\_{1}(\theta\_{1}-\theta\_{2})},\quad\frac{\partial\eta}{\partial\theta\_{1}}=-k\_{1}\eta. |  |

The first-order condition becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | k1​{θ1​[a+κ​(1−a)]−𝔼​[L​𝟏{L>b∗}]}=a+κ​(1−a)+[θ1​(1−κ)+b∗]​q11,k\_{1}\{\theta\_{1}[a+\kappa(1-a)]-\mathbb{E}[L\mathbf{1}\_{\{L>b^{\*}\}}]\}=a+\kappa(1-a)+[\theta\_{1}(1-\kappa)+b^{\*}]q\_{1}^{1}, |  | (37) |

where

|  |  |  |
| --- | --- | --- |
|  | a=ℙ​[L≤b∗],q11=∂a∂θ1=fL​(b∗)​∂b∗∂θ1=fL​(b∗)​δ​(κ−1)​η​[1−k1​(θ1−θ2)],a=\mathbb{P}[L\leq b^{\*}],\,q\_{1}^{1}=\frac{\partial a}{\partial\theta\_{1}}=f\_{L}(b^{\*})\frac{\partial b^{\*}}{\partial\theta\_{1}}=f\_{L}(b^{\*})\delta(\kappa-1)\eta[1-k\_{1}(\theta\_{1}-\theta\_{2})], |  |

the second derivative can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1η⋅∂2J1∂θ12=\displaystyle\frac{1}{\eta}\cdot\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}= | q11​(κ−1)​{(fL′​(b∗)fL​(b∗)​∂b∗∂θ1−k1)​h1+δ​η​[1−k1​(θ1−θ2)]−2}−k1​(κ−1)​(1−a)⏟I4\displaystyle\underbrace{q\_{1}^{1}(\kappa-1)\left\{\left(\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}\frac{\partial b^{\*}}{\partial\theta\_{1}}-k\_{1}\right)h\_{1}+\delta\,\eta[1-k\_{1}(\theta\_{1}-\theta\_{2})]-2\right\}-k\_{1}(\kappa-1)(1-a)}\_{I\_{4}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −k1+(κ−1)​h1​fL​(b∗)​∂2b∗∂θ12⏟I5.\displaystyle\underbrace{-k\_{1}+(\kappa-1)h\_{1}f\_{L}(b^{\*})\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}}\_{I\_{5}}. |  |

where h1​(θ1;θ2)=−θ1+δ​[η​θ1+(1−η)​θ2]h\_{1}(\theta\_{1};\theta\_{2})=-\theta\_{1}+\delta[\eta\,\theta\_{1}+(1-\eta)\theta\_{2}]. We now show separately that I4<0I\_{4}<0 and I5≤0I\_{5}\leq 0 under the stated conditions.

Step 1: I4<0.I\_{4}<0.

We begin by distinguishing between the following two cases, according to the sign of q11q\_{1}^{1}.

If θ1∈[θ2+1k1,+∞)\theta\_{1}\in\left[\theta\_{2}+\frac{1}{k\_{1}},+\infty\right), then q11≤0q\_{1}^{1}\leq 0, combining with Condition (i), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (fL′​(b∗)fL​(b∗)​∂b∗∂θ1−k1)​h1\displaystyle\left(\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}\frac{\partial b^{\*}}{\partial\theta\_{1}}-k\_{1}\right)h\_{1} | >−k12​h1=1−δ2​θ1​k1+k1​(θ1−θ2)​δ​(1−η)2≥12−δ​k22​e,\displaystyle>-\frac{k\_{1}}{2}h\_{1}=\frac{1-\delta}{2}\theta\_{1}k\_{1}+k\_{1}(\theta\_{1}-\theta\_{2})\frac{\delta(1-\eta)}{2}\geq\frac{1}{2}-\frac{\delta k\_{2}}{2\mathrm{e}}, |  | (38) |

in which the last inequality follows from θ1​k1>1\theta\_{1}k\_{1}>1 and (1−η)​k1​(θ1−θ2)≥1−k2e.(1-\eta)k\_{1}(\theta\_{1}-\theta\_{2})\geq 1-\frac{k\_{2}}{\mathrm{e}}.

Denote y=δ​η​[1−k1​(θ1−θ2)]y=\delta\eta[1-k\_{1}(\theta\_{1}-\theta\_{2})], then y∈[−δ​k2e2,0).y\in\left[-\frac{\delta k\_{2}}{\mathrm{e}^{2}},0\right). Combining with Inequality ([38](https://arxiv.org/html/2601.12655v1#A1.E38 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | I4\displaystyle I\_{4} | ≤fL​(b∗)​(κ−1)2​y​(y−32−δ​k22​e)−k1​(κ−1)​(1−a)\displaystyle\leq f\_{L}(b^{\*})(\kappa-1)^{2}y\left(y-\frac{3}{2}-\frac{\delta k\_{2}}{2\mathrm{e}}\right)-k\_{1}(\kappa-1)(1-a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤fL​(b∗)​(κ−1)2​δ​k2e2​(δ​k2e2+δ​k22​e+32)−k1​(κ−1)​(1−a)\displaystyle\leq f\_{L}(b^{\*})(\kappa-1)^{2}\frac{\delta k\_{2}}{\mathrm{e}^{2}}\left(\frac{\delta k\_{2}}{\mathrm{e}^{2}}+\frac{\delta k\_{2}}{2\mathrm{e}}+\frac{3}{2}\right)-k\_{1}(\kappa-1)(1-a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | :=g1​(b∗).\displaystyle:=g\_{1}(b^{\*}). |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂g1​(b∗)∂b∗\displaystyle\frac{\partial g\_{1}(b^{\*})}{\partial b^{\*}} | =fL​(b∗)​[fL′​(b∗)fL​(b∗)​(κ−1)2​δ​k2e2​((2+e)​δ​k22​e2+32)+k1​(κ−1)]\displaystyle=f\_{L}(b^{\*})\left[\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}(\kappa-1)^{2}\frac{\delta k\_{2}}{\mathrm{e}^{2}}\left(\frac{(2+\mathrm{e})\delta k\_{2}}{2\mathrm{e}^{2}}+\frac{3}{2}\right)+k\_{1}(\kappa-1)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥fL​(b∗)​k1​(κ−1)​[1−e2​e−1​(κ−1)​δ​k2e2​((2+e)​δ​k22​e2+32)]>0.\displaystyle\geq f\_{L}(b^{\*})k\_{1}(\kappa-1)\left[1-\frac{\mathrm{e}}{2\mathrm{e}-1}(\kappa-1)\frac{\delta k\_{2}}{\mathrm{e}^{2}}\left(\frac{(2+\mathrm{e})\delta k\_{2}}{2\mathrm{e}^{2}}+\frac{3}{2}\right)\right]>0. |  |

Thus
g1​(b∗)<limb∗→+∞g1​(b∗)=0,g\_{1}(b^{\*})<\lim\limits\_{b^{\*}\rightarrow+\infty}g\_{1}(b^{\*})=0,
i.e., I4<0.I\_{4}<0.

If θ1∈[θ2,θ2+1k1)\theta\_{1}\in\left[\theta\_{2},\theta\_{2}+\frac{1}{k\_{1}}\right), then q11>0q\_{1}^{1}>0. Combining with Condition (i) and Condition (iii), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | (fL′​(b∗)fL​(b∗)​∂b∗∂θ1−k1)​h1\displaystyle\left(\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}\frac{\partial b^{\*}}{\partial\theta\_{1}}-k\_{1}\right)h\_{1} | ≤(1+e​δ​(κ−1)​k22​e−1)​k1​[(1−δ)​Mκ+δ​(1−η)​(θ1−θ2)]\displaystyle\leq\left(1+\frac{\mathrm{e}\delta(\kappa-1)k\_{2}}{2\mathrm{e}-1}\right)k\_{1}\left[(1-\delta)\frac{M}{\kappa}+\delta(1-\eta)(\theta\_{1}-\theta\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤3​e−12​e−1​[k2​(2−δ​k2)2−k2+δ​(1−k2e)].\displaystyle\leq\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left[\frac{k\_{2}(2-\delta k\_{2})}{2-k\_{2}}+\delta\left(1-\frac{k\_{2}}{\mathrm{e}}\right)\right]. |  |

Noting that in this case, y∈(0,δ​k2]y\in(0,\delta k\_{2}], we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I4\displaystyle I\_{4} | ≤fL​(b∗)​(κ−1)2​y​{y+3​e−12​e−1​[k2​(2−δ​k2)2−k2+δ​(1−k2e)]−2}\displaystyle\leq f\_{L}(b^{\*})(\kappa-1)^{2}y\left\{y+\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left[\frac{k\_{2}(2-\delta k\_{2})}{2-k\_{2}}+\delta\left(1-\frac{k\_{2}}{\mathrm{e}}\right)\right]-2\right\} |  | (39) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −k1​(κ−1)​(1−a)\displaystyle\quad\,-k\_{1}(\kappa-1)(1-a) |  | (40) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤fL​(b∗)​(κ−1)2​y​{δ​k2+3​e−12​e−1​[k2​(2−δ​k2)2−k2+δ​(1−k2e)]−2}\displaystyle\leq f\_{L}(b^{\*})(\kappa-1)^{2}y\left\{\delta k\_{2}+\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left[\frac{k\_{2}(2-\delta k\_{2})}{2-k\_{2}}+\delta\left(1-\frac{k\_{2}}{\mathrm{e}}\right)\right]-2\right\} |  | (41) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −k1​(κ−1)​(1−a)\displaystyle\quad\,-k\_{1}(\kappa-1)(1-a) |  | (42) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤fL​(b∗)​(κ−1)2​y​{δ+3​e−12​e−1​(2−δe)−2}−k1​(κ−1)​(1−a)\displaystyle\leq f\_{L}(b^{\*})(\kappa-1)^{2}y\left\{\delta+\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left(2-\frac{\delta}{e}\right)-2\right\}-k\_{1}(\kappa-1)(1-a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤fL​(b∗)​(κ−1)2​δ​k2​{δ+3​e−12​e−1​(2−δe)−2}−k1​(κ−1)​(1−a)\displaystyle\leq f\_{L}(b^{\*})(\kappa-1)^{2}\delta k\_{2}\left\{\delta+\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left(2-\frac{\delta}{e}\right)-2\right\}-k\_{1}(\kappa-1)(1-a) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | :=g2​(b∗).\displaystyle:=g\_{2}(b^{\*}). |  | (43) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂g2​(b∗)∂b∗\displaystyle\frac{\partial g\_{2}(b^{\*})}{\partial b^{\*}} | =fL​(b∗)​(κ−1)​{fL′​(b∗)fL​(b∗)​(κ−1)​δ​k2​[δ+3​e−12​e−1​(2−δe)−2]+k1}\displaystyle=f\_{L}(b^{\*})(\kappa-1)\left\{\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}(\kappa-1)\delta k\_{2}\left[\delta+\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left(2-\frac{\delta}{e}\right)-2\right]\!+\!k\_{1}\right\} |  | (44) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥fL​(b∗)​(κ−1)​k1​{1−(κ−1)​δ​k2​e2​e−1​[δ+3​e−12​e−1​(2−δe)−2]}\displaystyle\geq f\_{L}(b^{\*})(\kappa-1)k\_{1}\left\{1-(\kappa-1)\delta k\_{2}\frac{\mathrm{e}}{2\mathrm{e}-1}\left[\delta+\frac{3\mathrm{e}-1}{2\mathrm{e}-1}\left(2-\frac{\delta}{e}\right)-2\right]\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥fL​(b∗)​(κ−1)​k1​[1−(κ−1)​δ​e2​e−1​(2​e2−4​e+1(2​e−1)​e​δ+2​e2​e−1)]\displaystyle\geq f\_{L}(b^{\*})(\kappa-1)k\_{1}\left[1-(\kappa-1)\delta\frac{\mathrm{e}}{2\mathrm{e}-1}\left(\frac{2\mathrm{e}^{2}-4\mathrm{e}+1}{(2\mathrm{e}-1)\mathrm{e}}\delta+\frac{2\mathrm{e}}{2\mathrm{e}-1}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥fL​(b∗)​(κ−1)​k1​(2−κ)>0,\displaystyle\geq f\_{L}(b^{\*})(\kappa-1)k\_{1}(2-\kappa)>0, |  |

where the first inequality follows from that the content inside the braces in Expression ([42](https://arxiv.org/html/2601.12655v1#A1.E42 "In Proof. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) is monotonically increasing with respect to k2k\_{2}. Thus we have
g2​(b∗)≤limb∗→+∞g2​(b∗)=0,g\_{2}(b^{\*})\leq\lim\limits\_{b^{\*}\rightarrow+\infty}g\_{2}(b^{\*})=0, i.e., I4<0.I\_{4}<0.

Step 2: I5≤0.I\_{5}\leq 0.

It is immediately that if θ1∈(θ2+2k2,+∞)\theta\_{1}\in\left(\theta\_{2}+\frac{2}{k\_{2}},+\infty\right), then ∂2b∗∂θ12>0\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}>0, and consequently I5<0I\_{5}<0 follows. Hence, it suffices to consider the case corresponding to θ1∈[θ2,θ2+2k1].\theta\_{1}\in\left[\theta\_{2},\theta\_{2}+\frac{2}{k\_{1}}\right]. Observe that using Condition (i)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂(fL​(b∗)​∂2b∗∂θ12)∂θ1\displaystyle\frac{\partial\left(f\_{L}(b^{\*})\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}\right)}{\partial\theta\_{1}} | =fL(b∗)[δ(κ−1)k12η[3−k1(θ1−θ2)]\displaystyle=f\_{L}(b^{\*})\Bigl[\delta(\kappa-1)k\_{1}^{2}\eta[3-k\_{1}(\theta\_{1}-\theta\_{2})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ2(κ−1)2k1η2[k1(θ1−θ2)−2][1−k1(θ1−θ2)]fL′​(b∗)fL​(b∗)]\displaystyle+\delta^{2}(\kappa-1)^{2}k\_{1}\eta^{2}[k\_{1}(\theta\_{1}-\theta\_{2})-2][1-k\_{1}(\theta\_{1}-\theta\_{2})]\frac{f\_{L}^{\prime}(b^{\*})}{f\_{L}(b^{\*})}\Bigl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥fL​(b∗)​δ​(κ−1)​k12​η​[1−δ​(κ−1)​η]>0.\displaystyle\geq f\_{L}(b^{\*})\delta(\kappa-1)k\_{1}^{2}\eta\left[1-\delta(\kappa-1)\eta\right]>0. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂h1∂θ1\displaystyle\frac{\partial h\_{1}}{\partial\theta\_{1}} | =δ​η−1−δ​η​k1​(θ1−θ2)<0.\displaystyle=\delta\eta-1-\delta\eta k\_{1}(\theta\_{1}-\theta\_{2})<0. |  |

Let [θ2,θ2+2k1]\left[\theta\_{2},\theta\_{2}+\frac{2}{k\_{1}}\right] be divided into 2​z2z equal parts, z∈ℕ={1,2,⋯}z\in\mathbb{N}=\{1,2,\cdots\}. For 0≤m≤2​z−10\leq m\leq 2z-1 and m∈ℕm\in\mathbb{N}, using Condition(ii), it follows that on the interval [θ2+mz​k1,θ2+m+1z​k1]\left[\theta\_{2}+\frac{m}{zk\_{1}},\theta\_{2}+\frac{m+1}{zk\_{1}}\right],

|  |  |  |  |
| --- | --- | --- | --- |
|  | (κ−1)​h1​fL​(b∗)​∂2b∗∂θ12\displaystyle(\kappa-1)h\_{1}f\_{L}(b^{\*})\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}} | ≤(κ−1)​|h1​(θ2+m+1z​k1;θ2)|⋅|fL​(b∗)​∂2b∗∂θ12​(θ2+mz​k1;θ2)|\displaystyle\leq(\kappa-1)\left|h\_{1}(\theta\_{2}+\frac{m+1}{zk\_{1}};\theta\_{2})\right|\cdot\left|f\_{L}(b^{\*})\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}(\theta\_{2}+\frac{m}{zk\_{1}};\theta\_{2})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =fL​(b∗)​δ​(κ−1)2​k2​e−mz​(2−mz)​[k1​(1−δ)​θ1+m+1z​δ​(1−k2​e−m+1z)]\displaystyle=f\_{L}(b^{\*})\delta(\kappa-1)^{2}k\_{2}\mathrm{e}^{-\frac{m}{z}}\left(2-\frac{m}{z}\right)\left[k\_{1}(1-\delta)\theta\_{1}+\frac{m+1}{z}\delta(1-k\_{2}\mathrm{e}^{-\frac{m+1}{z}})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤fL​(b∗)​δ​(κ−1)2​k2​e−mz​(2−mz)​[A1+m+1z​δ]\displaystyle\leq f\_{L}(b^{\*})\delta(\kappa-1)^{2}k\_{2}\mathrm{e}^{-\frac{m}{z}}\left(2-\frac{m}{z}\right)\left[A\_{1}+\frac{m+1}{z}\delta\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∝g3​(m+1z),\displaystyle\propto g\_{3}\left(\frac{m+1}{z}\right), |  |

where the symbol ∝\propto denotes proportionality, the function g3​(⋅)g\_{3}(\cdot) is

|  |  |  |
| --- | --- | --- |
|  | g3​(ℓ)=e−ℓ+1z​(2+1z−ℓ)​(A1+δ​ℓ),ℓ∈[1z,2],g\_{3}(\ell)=\mathrm{e}^{-\ell+\frac{1}{z}}\left(2+\frac{1}{z}-\ell\right)\left(A\_{1}+\delta\ell\right),\quad\ell\in\left[\frac{1}{z},2\right], |  |

and its derivative is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g3′​(ℓ)\displaystyle g\_{3}^{\prime}(\ell) | =e−ℓ+1z​[δ​ℓ2−(δ​4​z+1z−A1)​ℓ−(3+1z)​A1+(2+1z)​δ].\displaystyle=\mathrm{e}^{-\ell+\frac{1}{z}}\left[\delta\ell^{2}-\left(\delta\frac{4z+1}{z}-A\_{1}\right)\ell-\left(3+\frac{1}{z}\right)A\_{1}+\left(2+\frac{1}{z}\right)\delta\right]. |  | (45) |

The sign of g3′g^{\prime}\_{3} is determined solely by the quadratic polynomial inside the square brackets, evaluating at endpoints gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g3′​(2)=e−2+1z​[−(2+1z)​δ−(1+1z)​A1]<0,g3′​(1z)=−3​A1+(2−3z)​δ.\displaystyle g\_{3}^{\prime}(2)=\mathrm{e}^{-2+\frac{1}{z}}\left[-\left(2+\frac{1}{z}\right)\delta-\left(1+\frac{1}{z}\right)A\_{1}\right]<0,\quad g\_{3}^{\prime}\left(\frac{1}{z}\right)=-3A\_{1}+\left(2-\frac{3}{z}\right)\delta. |  | (46) |

If 2​δ≤3​A12\delta\leq 3A\_{1}, we obtain g3′​(ℓ)<0g\_{3}^{\prime}(\ell)<0 for all ℓ∈[1z,2]\ell\in\left[\frac{1}{z},2\right]. Hence g3​(ℓ)g\_{3}(\ell) is strictly decreasing on this interval, and

|  |  |  |
| --- | --- | --- |
|  | g3​(ℓ)≤g3​(1z)=2​(A1+δz)→2​A1​(z→+∞).g\_{3}(\ell)\leq g\_{3}\left(\frac{1}{z}\right)=2\left(A\_{1}+\frac{\delta}{z}\right)\rightarrow 2A\_{1}\,(z\rightarrow+\infty). |  |

If 2​δ>3​A12\delta>3A\_{1}, let z≥⌈3​δ2​δ−3​A1​𝟏{3​A1<2​δ}⌉+1z\geq\lceil\frac{3\delta}{2\delta-3A\_{1}}\mathbf{1}\_{\{3A\_{1}<2\delta\}}\rceil+1, where ⌈(⋅)⌉\lceil(\cdot)\rceil denotes the ceiling of (⋅)(\cdot), then g3′​(1z)>0g\_{3}^{\prime}(\frac{1}{z})>0, g3g\_{3} attains its maximum when g3′​(ℓ)=0g\_{3}^{\prime}(\ell)=0, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g3​(ℓ)≤e−ℓ+1z​[(2+1z)​δ−A1−2​δ​ℓ]≤(2−1z)​δ−A1→(2​δ−A1)​(z→+∞).\displaystyle g\_{3}(\ell)\leq\mathrm{e}^{-\ell+\frac{1}{z}}\left[\left(2+\frac{1}{z}\right)\delta-A\_{1}-2\delta\ell\right]\leq\left(2-\frac{1}{z}\right)\delta-A\_{1}\rightarrow(2\delta-A\_{1})\,(z\rightarrow+\infty). |  | (47) |

Using Condition (iii), we obtain the uniform bound

|  |  |  |
| --- | --- | --- |
|  | (κ−1)​h1​fL​(b∗)​∂2b∗∂θ12≤supℓ∈ILfL​(ℓ)​δ​(κ−1)2​k2​[(2​A1)∨(2​δ−A1)]≤k1.(\kappa-1)h\_{1}f\_{L}(b^{\*})\frac{\partial^{2}b^{\*}}{\partial\theta\_{1}^{2}}\leq\sup\_{\ell\in I\_{L}}f\_{L}(\ell)\delta(\kappa-1)^{2}k\_{2}[(2A\_{1})\vee(2\delta-A\_{1})]\leq k\_{1}. |  |

This implies I5≤0.I\_{5}\leq 0.

Consequently,

|  |  |  |
| --- | --- | --- |
|  | ∂2J1∂θ12=η​(I4+I5)<0,\frac{\partial^{2}J^{1}}{\partial\theta\_{1}^{2}}=\eta(I\_{4}+I\_{5})<0, |  |

which is the desired result.
∎

Based on Lemmas [A.1](https://arxiv.org/html/2601.12655v1#A1.Thmlemma1 "Lemma A.1. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium") and [A.2](https://arxiv.org/html/2601.12655v1#A1.Thmlemma2 "Lemma A.2. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium"), we establish the following theorem concerning the existence and uniqueness of the maximizer of Ji,i∈ℐJ^{i},i\in\mathcal{I}.

###### Theorem A.1 (Existence and Uniqueness of the Maximizer of Ji,i∈ℐJ^{i},i\in\mathcal{I}).

Let i∈ℐ,θ3−i∈Θi\in\mathcal{I},\theta\_{3-i}\in\Theta, then the function JiJ^{i} admits a unique maximizer if the following conditions hold:

* (i)

  supℓ∈ILfL′​(ℓ)fL​(ℓ)∈[−e​k12​e−1,k12]\displaystyle\sup\_{\ell\in I\_{L}}\frac{f^{\prime}\_{L}(\ell)}{f\_{L}(\ell)}\in\Big[-\frac{\mathrm{e}k\_{1}}{2\mathrm{e}-1},\frac{k\_{1}}{2}\Big] with IL:=[δ​(κ−1)​𝔼​[L],δ​(κ−1)​Mκ]I\_{L}:=\left[\delta(\kappa-1)\mathbb{E}[L],\,\frac{\delta(\kappa-1)M}{\kappa}\right];
* (ii)

  supℓ∈ILfL​(ℓ)≤m\displaystyle\sup\_{\ell\in I\_{L}}f\_{L}(\ell)\leq\mathrm{m};
* (iii)

  (1−δ)​Mκ​k1≤A\displaystyle(1-\delta)\frac{M}{\kappa}k\_{1}\leq A,

where fL​(ℓ)f\_{L}(\ell) denotes the density function of the loss LL on the positive support, m=m1​𝟏{i=1}+m2​𝟏{i=2},A=A1​𝟏{i=1}+A2​𝟏{i=2}\mathrm{m}=\mathrm{m}\_{1}\mathbf{1}\_{\{i=1\}}+\mathrm{m}\_{2}\mathbf{1}\_{\{i=2\}},\,A=A\_{1}\mathbf{1}\_{\{i=1\}}+A\_{2}\mathbf{1}\_{\{i=2\}}, and m1,m2,A1\mathrm{m}\_{1},\mathrm{m}\_{2},A\_{1} and A2A\_{2} are defined in ([23](https://arxiv.org/html/2601.12655v1#S4.E23 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")).

###### Proof.

If i=1i=1, based on Lemma [A.1](https://arxiv.org/html/2601.12655v1#A1.Thmlemma1 "Lemma A.1. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium") and Lemma [A.2](https://arxiv.org/html/2601.12655v1#A1.Thmlemma2 "Lemma A.2. ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium"), if ∂J1∂θ1\frac{\partial J^{1}}{\partial\theta\_{1}} admits a zero, then it is unique and necessarily corresponds to a point of maximum. If ∂J1∂θ1\frac{\partial J^{1}}{\partial\theta\_{1}} has no zero, then J1​(θ1;θ2)J^{1}(\theta\_{1};\theta\_{2}) is monotone. In this case, the maximizer of J1J^{1} over Θ\Theta exists and is unique. In summary, J1J^{1} admits a unique maximizer over Θ\Theta.

Otherwise, if i=2i=2, we present prove the existence and uniqueness of J2J^{2}. The proof follows a symmetric argument to that of i=1i=1, with the roles of Company 1 and Company 2 interchanged. Corresponding adjustments are made to the function fL​(ℓ)f\_{L}(\ell) and the relevant parameters (see the expression for AA and m\mathrm{m}), while the overall logical structure remains unchanged. For the sake of brevity, the detailed derivation is omitted.
∎

We are now ready to complete the proof of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") considering all possible configurations of the first-order condition.

###### Proof of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium").

We define the mapping 𝒢:Θ2↦Θ2\mathcal{G}:\Theta^{2}\mapsto\Theta^{2} by

|  |  |  |
| --- | --- | --- |
|  | ∀(θ1,θ2)∈Θ2,𝒢​(θ1,θ2)=(θ1¯,θ2¯),\forall(\theta\_{1},\theta\_{2})\in\Theta^{2},\,\ \mathcal{G}(\theta\_{1},\theta\_{2})=(\bar{\theta\_{1}},\bar{\theta\_{2}}), |  |

where (θ1¯,θ2¯)(\bar{\theta\_{1}},\bar{\theta\_{2}}) satisfies

|  |  |  |
| --- | --- | --- |
|  | θ1¯=arg​supθ1∈ΘJ1​(θ1;θ2),θ2¯=arg​supθ2∈ΘJ2​(θ2;θ1).\bar{\theta\_{1}}=\arg\sup\limits\_{\theta\_{1}\in\Theta}J^{1}(\theta\_{1};\theta\_{2}),\,\bar{\theta\_{2}}=\arg\sup\limits\_{\theta\_{2}\in\Theta}J^{2}(\theta\_{2};\theta\_{1}). |  |

By Theorem [A.1](https://arxiv.org/html/2601.12655v1#A1.Thmtheorem1 "Theorem A.1 (Existence and Uniqueness of the Maximizer of {𝐽^𝑖,𝑖}∈ℐ). ‣ A.3 Proof of Theorem 4.2 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium"), for any θi∈Θ\theta\_{i}\in\Theta, i∈ℐi\in\mathcal{I}, the best response θ¯j​(θi)\bar{\theta}\_{j}(\theta\_{i}) exists, is unique, and depends continuously on θi\theta\_{i}.
Hence, 𝒢\mathcal{G} is a continuous self-mapping on the compact convex set Θ2\Theta^{2}. Thus, the existence of a fixed point follows from Brouwer’s Fixed Point Theorem.
∎

### A.4 Proof of Proposition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmproposition1 "Proposition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")

###### Proof.

We first consider the case k2≥12k\_{2}\geq\tfrac{1}{2} and argue by contradiction.
Suppose that an equilibrium premium exists with θ1<θ2\theta\_{1}<\theta\_{2}.
Then the first-order conditions imply

|  |  |  |
| --- | --- | --- |
|  | ∂J1∂θ1​(θ1;θ2)≤0and∂J2∂θ2​(θ2;θ1)≥0,\frac{\partial J^{1}}{\partial\theta\_{1}}(\theta\_{1};\theta\_{2})\leq 0\quad\text{and}\quad\frac{\partial J^{2}}{\partial\theta\_{2}}(\theta\_{2};\theta\_{1})\geq 0, |  |

that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​[a+κ​(1−a)+(θ1​(1−κ)+b∗)​q11]≤k1​(1−η)​[θ1​(a+κ​(1−a))−𝔼​[L​𝟏{L>b∗}]],\displaystyle\eta\bigl[a+\kappa(1-a)+(\theta\_{1}(1-\kappa)+b^{\*})q\_{1}^{1}\bigr]\leq k\_{1}(1-\eta)\bigl[\theta\_{1}(a+\kappa(1-a))-\mathbb{E}[L\mathbf{1}\_{\{L>b^{\*}\}}]\bigr], |  | (48) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a+κ​(1−a)+(θ2​(1−κ)+b∗)​q22≥k1​[θ2​(a+κ​(1−a))−𝔼​[L​𝟏{L>b∗}]].\displaystyle a+\kappa(1-a)+(\theta\_{2}(1-\kappa)+b^{\*})q\_{2}^{2}\geq k\_{1}\bigl[\theta\_{2}(a+\kappa(1-a))-\mathbb{E}[L\mathbf{1}\_{\{L>b^{\*}\}}]\bigr]. |  | (49) |

Multiplying Inequality ([48](https://arxiv.org/html/2601.12655v1#A1.E48 "In Proof. ‣ A.4 Proof of Proposition 4.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) by (1−η)−1(1-\eta)^{-1} and subtracting
Inequality ([49](https://arxiv.org/html/2601.12655v1#A1.E49 "In Proof. ‣ A.4 Proof of Proposition 4.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ:=\displaystyle\mathcal{H}:=\; | [2​η−11−η−k1​(θ1−θ2)]​[a+κ​(1−a)]\displaystyle\left[\frac{2\eta-1}{1-\eta}-k\_{1}(\theta\_{1}-\theta\_{2})\right][a+\kappa(1-a)] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +η1−η​[θ1​(1−κ)+b∗]​q11−[θ2​(1−κ)+b∗]​q22≤0,\displaystyle+\frac{\eta}{1-\eta}[\theta\_{1}(1-\kappa)+b^{\*}]q\_{1}^{1}-[\theta\_{2}(1-\kappa)+b^{\*}]q\_{2}^{2}\leq 0, |  | (50) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | q11\displaystyle q\_{1}^{1} | =fL​(b∗)​δ​(κ−1)​[η+k1​(θ2−θ1)​(1−η)]>0,\displaystyle=f\_{L}(b^{\*})\delta(\kappa-1)\bigl[\eta+k\_{1}(\theta\_{2}-\theta\_{1})(1-\eta)\bigr]>0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q22\displaystyle q\_{2}^{2} | =fL​(b∗)​δ​(κ−1)​(1−η)​[1+k1​(θ1−θ2)].\displaystyle=f\_{L}(b^{\*})\delta(\kappa-1)(1-\eta)\bigl[1+k\_{1}(\theta\_{1}-\theta\_{2})\bigr]. |  |

Because q11+q22=fL​(b∗)​δ​(κ−1)q\_{1}^{1}+q\_{2}^{2}=f\_{L}(b^{\*})\delta(\kappa-1), it follows that |q11|>|q22||q\_{1}^{1}|>|q\_{2}^{2}|.

Case 1: q22≤0q\_{2}^{2}\leq 0.
Using q22>−q11q\_{2}^{2}>-q\_{1}^{1}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | η1−η[θ1(1−κ)\displaystyle\frac{\eta}{1-\eta}[\theta\_{1}(1-\kappa) | +b∗]q11−[θ2(1−κ)+b∗]q22>q111−ηδ−1δb∗\displaystyle+b^{\*}]q\_{1}^{1}-[\theta\_{2}(1-\kappa)+b^{\*}]q\_{2}^{2}>\frac{q\_{1}^{1}}{1-\eta}\frac{\delta-1}{\delta}b^{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥η1−η​(κ−1)​(δ−1)​fL​(b∗)​b∗≥−η1−η​[a+κ​(1−a)].\displaystyle\geq\frac{\eta}{1-\eta}(\kappa-1)(\delta-1)f\_{L}(b^{\*})b^{\*}\geq-\frac{\eta}{1-\eta}[a+\kappa(1-a)]. |  |

Combining this with k1​(θ2−θ1)>1k\_{1}(\theta\_{2}-\theta\_{1})>1, we have

|  |  |  |
| --- | --- | --- |
|  | ℋ>(1−η)​[k1​(θ2−θ1)−1]​[a+κ​(1−a)]>0,\mathcal{H}>(1-\eta)\left[k\_{1}(\theta\_{2}-\theta\_{1})-1\right]\left[a+\kappa(1-a)\right]>0, |  |

which contradicts Inequality ([50](https://arxiv.org/html/2601.12655v1#A1.E50 "In Proof. ‣ A.4 Proof of Proposition 4.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")).

Case 2: q22>0q\_{2}^{2}>0.
If θ1​(1−κ)+b∗≥0\theta\_{1}(1-\kappa)+b^{\*}\geq 0, then it is immediate that ℋ>0\mathcal{H}>0.
It remains to consider the case θ1​(1−κ)+b∗<0\theta\_{1}(1-\kappa)+b^{\*}<0.
As b∗−(κ−1)​θ1>(δ−1)​(κ−1)​θ1≥δ−1δ​b∗b^{\*}-(\kappa-1)\theta\_{1}>(\delta-1)(\kappa-1)\theta\_{1}\geq\frac{\delta-1}{\delta}b^{\*}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | η1−η[θ1(1\displaystyle\frac{\eta}{1-\eta}[\theta\_{1}(1 | −κ)+b∗]q11−[θ2(1−κ)+b∗]q22\displaystyle-\kappa)+b^{\*}]q\_{1}^{1}-[\theta\_{2}(1-\kappa)+b^{\*}]q\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | >\displaystyle> | η1−η​[θ1​(1−κ)+b∗]​q11−[θ1​(1−κ)+b∗]​q22\displaystyle\frac{\eta}{1-\eta}[\theta\_{1}(1-\kappa)+b^{\*}]q\_{1}^{1}-[\theta\_{1}(1-\kappa)+b^{\*}]q\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | >\displaystyle> | fL​(b∗)​b∗​(δ−1)​(κ−1)​[2​η−11−η−k1​(θ1−θ2)]\displaystyle f\_{L}(b^{\*})b^{\*}(\delta-1)(\kappa-1)\left[\frac{2\eta-1}{1-\eta}-k\_{1}(\theta\_{1}-\theta\_{2})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | −[a+κ​(1−a)]​[2​η−11−η−k1​(θ1−θ2)]⟺ℋ>0,\displaystyle-[a+\kappa(1-a)]\left[\frac{2\eta-1}{1-\eta}-k\_{1}(\theta\_{1}-\theta\_{2})\right]\Longleftrightarrow\mathcal{H}>0, |  |

which again implies ℋ>0\mathcal{H}>0, contradicting ([50](https://arxiv.org/html/2601.12655v1#A1.E50 "In Proof. ‣ A.4 Proof of Proposition 4.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")). Consequently, when k2≥12k\_{2}\geq\tfrac{1}{2}, Inequality ([50](https://arxiv.org/html/2601.12655v1#A1.E50 "In Proof. ‣ A.4 Proof of Proposition 4.1 ‣ Appendix A Proofs ‣ Optimal Underreporting and Competitive Equilibrium")) cannot hold, and thus
θ1∗≥θ2∗\theta\_{1}^{\*}\geq\theta\_{2}^{\*}. When k2≤12k\_{2}\leq\tfrac{1}{2}, a symmetric argument between Company 1 and Company 2 yields θ1∗≤θ2∗\theta\_{1}^{\*}\leq\theta\_{2}^{\*}.
If k2=12k\_{2}=\tfrac{1}{2}, both the inequalities hold, implying θ1∗=θ2∗\theta\_{1}^{\*}=\theta\_{2}^{\*}.
∎

## Appendix B An Example

In the main paper, we show in Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") that a Nash equilibrium premium strategy exists when a set of technical conditions holds. However, despite discussions in Remark [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmremark1 "Remark 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"), it is not clear that all those conditions can hold simultaneously in a reasonable setup. To provide a (positive) answer to this question, we construct an example in which all conditions in Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") are satisfied.

###### Example B.1.

Assume that the positive part of the loss follows a Gamma distribution, L​|L>​0∼G​a​m​m​a​(α,λ)L|L>0\sim Gamma(\alpha,\lambda), which belongs to the exponential family of distributions and is capable of capturing the fat tails commonly observed in insurance data (see, e.g., Section 17.3.1 in Frees ([2009](https://arxiv.org/html/2601.12655v1#bib.bib2 "Regression modeling with actuarial and financial applications"))). As a result, the cdf of the loss random variable LL in ([1](https://arxiv.org/html/2601.12655v1#S2.E1 "In 2 Model ‣ Optimal Underreporting and Competitive Equilibrium")) is given by

|  |  |  |
| --- | --- | --- |
|  | FL​(x)=p0+(1−p0)​∫0xλαΓ​(α)​ℓα−1​e−λ​ℓ​dℓ,with ​Γ​(α)=∫0∞tα−1​e−t​𝑑t.\displaystyle F\_{L}(x)=p\_{0}+(1-p\_{0})\int\_{0}^{x}\frac{\lambda^{\alpha}}{\Gamma(\alpha)}\ell^{\alpha-1}\mathrm{e}^{-\lambda\ell}\mathrm{d}\ell,\quad\text{with }\Gamma(\alpha)=\int^{\infty}\_{0}t^{\alpha-1}\mathrm{e}^{-t}dt. |  |

Because the underlying losses are from non-life risks, we assume that p0>0.5p\_{0}>0.5 (for example, often more than 90% auto insurance policies do not incur losses over a unit period).

Regarding the upper bound MM on the BMS premiums, we assume a conservative condition below:

|  |  |  |
| --- | --- | --- |
|  | M≤3​𝔼​[L].M\leq 3\mathbb{E}[L]. |  |

Empirical evidence from property and casualty insurance markets shows that typical loss ratios L​R=incurred lossesearned premiumsLR=\frac{\text{incurred losses}}{\text{earned premiums}} range from 0.60.6 to 0.80.8, with combined ratios close to 11 (see Allstate ([2023](https://arxiv.org/html/2601.12655v1#bib.bib42 "Allstate reports first quarter 2023 results")) and Swiss Re Institute ([2025](https://arxiv.org/html/2601.12655v1#bib.bib43 "U.S. property and casualty outlook – april 2025"))). Thus, the above bound holds for most insurance lines in practice.

Applying Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") to the setup in Example [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmexample1 "Example B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium") yields a refined result below.

###### Corollary B.1.

Let Assumption [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") hold and further assume the specifications as in Example [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmexample1 "Example B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium"). There exists an equilibrium premium strategy (θ1∗,θ2∗)(\theta\_{1}^{\*},\theta\_{2}^{\*}) if the following conditions hold:

* (i)

  k1λ≥max⁡{2−1e,2​[α−1α​δ​(κ−1)​(1−p0)−1], 3​(κ−1)}\displaystyle\frac{k\_{1}}{\lambda}\geq\max\left\{2-\frac{1}{\mathrm{e}},2\left[\frac{\alpha-1}{\alpha\delta(\kappa-1)(1-p\_{0})}-1\right],\,3(\kappa-1)\right\};
* (ii)

  k1λ≤κ3​α​(1−p0)​(1−δ)​(A1∧A2),\displaystyle\frac{k\_{1}}{\lambda}\leq\frac{\kappa}{3\alpha(1-p\_{0})(1-\delta)}(A\_{1}\wedge A\_{2}),

where A1A\_{1} and A2A\_{2} are defined in ([23](https://arxiv.org/html/2601.12655v1#S4.E23 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")).

###### Proof.

First, a calculation confirms that Condition (i) of Corollary [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmcorollary1 "Corollary B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium") implies Condition (i) of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium").

We now verify Condition (ii) of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium").
If α≥1\alpha\geq 1, using the bound Γ​(α)>2​π​αα−1​e−α\Gamma(\alpha)>\sqrt{2\pi}\alpha^{\alpha-1}\mathrm{e}^{-\alpha}, we obtain

|  |  |  |
| --- | --- | --- |
|  | fL​(ℓ)≤fL​(α−1λ)<λ​e2​π​(1−1α)α−1​(1−p0).f\_{L}(\ell)\leq f\_{L}\left(\frac{\alpha-1}{\lambda}\right)<\frac{\lambda\mathrm{e}}{\sqrt{2\pi}}\left(1-\frac{1}{\alpha}\right)^{\alpha-1}(1-p\_{0}). |  |

Since (1−1α)α−1<1\left(1-\frac{1}{\alpha}\right)^{\alpha-1}<1 and 1−p0<0.51-p\_{0}<0.5, it follows that

|  |  |  |
| --- | --- | --- |
|  | supℓ∈ILfL​(ℓ)<λ​e2​2​π<k12<m1∧m2,\sup\_{\ell\in I\_{L}}f\_{L}(\ell)<\frac{\lambda e}{2\sqrt{2\pi}}<\frac{k\_{1}}{2}<\mathrm{m}\_{1}\wedge\mathrm{m}\_{2}, |  |

where m1\mathrm{m}\_{1} and m2\mathrm{m}\_{2} are defined by ([23](https://arxiv.org/html/2601.12655v1#S4.E23 "In 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium")). That is, Condition (ii) in Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") holds.

If α∈(0,1)\alpha\in(0,1), applying the Kershaw’s inequality, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(α)>(23)1−α​1α,\displaystyle\Gamma(\alpha)>\left(\frac{2}{3}\right)^{1-\alpha}\frac{1}{\alpha}, |  | (51) |

which, together with Condition (iii) of Corollary [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmcorollary1 "Corollary B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium"), implies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supℓ∈ILfL​(ℓ)=fL​(δ​(κ−1)​𝔼​[L])\displaystyle\sup\_{\ell\in I\_{L}}f\_{L}(\ell)=f\_{L}(\delta(\kappa-1)\mathbb{E}[L]) | <λ​(2​α1+α)α​1δ​(κ−1)<k13​δ​(κ−1)2<m1∧m2.\displaystyle<\lambda\left(\frac{2\alpha}{1+\alpha}\right)^{\alpha}\frac{1}{\delta(\kappa-1)}<\frac{k\_{1}}{3\delta(\kappa-1)^{2}}<\mathrm{m}\_{1}\wedge\mathrm{m}\_{2}. |  | (52) |

Condition (ii) of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") is again satisfied when α∈(0,1)\alpha\in(0,1).

Finally, we examine Condition (iii) of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium"). Condition (ii) of Corollary [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmcorollary1 "Corollary B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium") implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | M≤3​(1−p0)​αλ≤κ(1−δ)​k1​(A1∧A2).\displaystyle M\leq 3(1-p\_{0})\frac{\alpha}{\lambda}\leq\frac{\kappa}{(1-\delta)k\_{1}}(A\_{1}\wedge A\_{2}). |  | (53) |

As such, Condition (iii) of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") is satisfied. Thus, because all requirements of Theorem [4.2](https://arxiv.org/html/2601.12655v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") hold, we apply it to conclude that the equilibrium per Definition [4.1](https://arxiv.org/html/2601.12655v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 The insurance companies’ pricing game ‣ Optimal Underreporting and Competitive Equilibrium") exists.
∎

We discuss the conditions in Corollary [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmcorollary1 "Corollary B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium") as follows. Note that if the parameters satisfy

|  |  |  |
| --- | --- | --- |
|  | 1−p0≥0.095, 3​(1−δ)<k2<3​δ−2, 1.5>κ>1.3,α≤1.05<2​e2​e−(4​e−1)​δ​(κ−1)​(1−p0),1-p\_{0}\geq 0.095,\,3(1-\delta)<k\_{2}<3\delta-2,\,1.5>\kappa>1.3,\,\alpha\leq 1.05<\frac{2\mathrm{e}}{2\mathrm{e}-(4\mathrm{e}-1)\delta(\kappa-1)(1-p\_{0})}, |  |

then the three conditions in Corollary [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmcorollary1 "Corollary B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium") hold if the following conditions are satisfied:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 2−1e<k1λ\displaystyle 2-\frac{1}{\mathrm{e}}<\frac{k\_{1}}{\lambda} | <2≤11−p0<κ3​α​(1−p0)​(1−δ)​min⁡{(1−k2)​(2−δ​(1−k2))1+k2,k2​(2−δ​k2)2−k2}.\displaystyle<2\leq\frac{1}{1-p\_{0}}<\frac{\kappa}{3\alpha(1-p\_{0})(1-\delta)}\min\left\{\frac{(1-k\_{2})(2-\delta(1-k\_{2}))}{1+k\_{2}},\frac{k\_{2}(2-\delta k\_{2})}{2-k\_{2}}\right\}. |  | (54) |

We mention that the requirement on the loss distribution is practically plausible. For example, in the study of Kmetic ([1993](https://arxiv.org/html/2601.12655v1#bib.bib40 "A parametric model for health care claims")) on parametric modeling of medical insurance claims, nearly half of the fitted Gamma distributions have shape parameters α\alpha below 1.05, while the rate parameter λ\lambda falls within the interval (0.001,0.01)(0.001,0.01).
We close this section with an important remark: for the setup in Example [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmexample1 "Example B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium"), the region of the parameters under which an equilibrium (θ1∗,θ2∗)(\theta\_{1}^{\*},\theta\_{2}^{\*}) exists as in Corollary [B.1](https://arxiv.org/html/2601.12655v1#A2.Thmcorollary1 "Corollary B.1. ‣ Appendix B An Example ‣ Optimal Underreporting and Competitive Equilibrium") is non-empty.