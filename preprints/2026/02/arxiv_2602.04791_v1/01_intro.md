---
authors:
- Hong Beng Lim
- Mengyi Xu
- Kenneth Q. Zhou
doc_id: arxiv:2602.04791v1
family_id: arxiv:2602.04791
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Fair Pricing in Long-Term Insurance: A Unified Framework'
url_abs: http://arxiv.org/abs/2602.04791v1
url_html: https://arxiv.org/html/2602.04791v1
venue: arXiv q-fin
version: 1
year: 2026
---


Hong Beng Lim
Corresponding author. E-mail: <benhblim@cuhk.edu.hk>
Department of Finance, Chinese University of Hong Kong, China

Mengyi Xu
School of Risk and Actuarial Studies, UNSW Sydney, Australia

Kenneth Q. Zhou
Department of Statistics and Actuarial Science, University of Waterloo, Canada

###### Abstract

Extant literature on fair pricing methods for actuarial contexts has primarily focused on the regression setting. While such approaches are well-suited to short-term products, it is unclear how they generalize to long-term products, whose pricing essentially relies on estimating transition rates in multi-state models. To address this gap, we propose a unified framework that recasts the estimation of any given multi-state transition model as a set of Poisson regression problems. This reformulation enables the direct application of existing fair pricing methods, which together constitute our proposed methodology. As an illustration, we apply the framework to a fair pricing exercise for a stylized long-term care insurance product using data from the University of Michigan Health and Retirement Study (HRS), focusing on a post-processing approach. We further explain how the framework readily accommodates pre-processing and in-processing fairness methods.

## 1 Introduction

Insurance pricing lies at the intersection of risk classification and fairness, raising difficult questions about how premiums should be constructed. A growing literature has sought to address this tension by proposing fair pricing methodologies, which can broadly be divided into two main strands. The first line of research focuses on the concept of the discrimination-free premium pioneered by Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")). Their formula is designed to mitigate the indirect impact of the discriminatory covariate on the model. Building on this work, Araiza Iturria et al. ([2024](https://arxiv.org/html/2602.04791v1#bib.bib13 "A discrimination-free premium under a causal framework")) explain the formula within a causal framework, identifying scenarios where its application may be socially acceptable or inappropriate. Additional extensions of this approach have been developed for settings where information on the discriminatory covariate is incomplete (Lindholm et al., [2024a](https://arxiv.org/html/2602.04791v1#bib.bib43 "A multi-task network approach for calculating discrimination-free insurance prices")) or unavailable (Gabric et al., [2024](https://arxiv.org/html/2602.04791v1#bib.bib35 "A Bayesian approach to discrimination-free insurance pricing")).

Another line of research draws on notions of fairness developed in the machine learning literature, as well as methods designed to enforce such notions (see Pessach and Shmueli, [2022](https://arxiv.org/html/2602.04791v1#bib.bib53 "A review on fairness in machine learning"), for a review). In the actuarial context, Grari et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib36 "A fair pricing model via adversarial learning")) use a penalized neural network approach to impose fairness constraints, specifically addressing continuous discriminatory covariates. Xin and Huang ([2024](https://arxiv.org/html/2602.04791v1#bib.bib61 "Antidiscrimination insurance pricing: Regulations, fairness criteria, and models")) examine different levels of non-discrimination required by regulation and identify suitable machine learning methodologies for each level. Optimal transport methods have also been explored: Lindholm et al. ([2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")) use them to pre-process the data toward enforcing demographic parity, whereas Hu et al. ([2024](https://arxiv.org/html/2602.04791v1#bib.bib39 "A sequentially fair mechanism for multiple sensitive attributes")) apply them to post-process predictions to enforce sequential fairness in multiple sensitive attributes. Côté et al. ([2025](https://arxiv.org/html/2602.04791v1#bib.bib52 "A fair price to pay: exploiting causal graphs for fairness in insurance")) propose a comprehensive causal framework to classify existing fair pricing methodologies in terms of the type of fairness enforced.

The aforementioned body of research has largely focused on incorporating fairness constraints into predictions of expected loss, in contrast to traditional machine learning settings where fair decision-making (i.e., classification) is of interest. As a result, methodologies have primarily been developed for the regression setting, with the loss variable serving as the response variable. However, this setup becomes limiting in the context of long-term insurance products. It is primarily suited to short-term products, such as home or automobile insurance, where premiums correspond directly to expected losses. For long-term insurance products, including life insurance and long-term care insurance (LTCI), premiums are instead derived from expected present value calculations that depend on estimates of transition rates in an underlying multi-state model, such as mortality rates in life insurance or multiple health-state transition rates in LTCI. In these settings, there is typically no single outcome variable whose expectation directly corresponds to the final price, making it unclear how existing fair pricing methods generalize beyond short-term products.

Two additional features of long-term products further underscore the importance of fairness considerations in this context. First, unlike short-term insurance products that are often purchased by companies or organizations, such as in commercial insurance and group health insurance, long-term products are typically issued to individuals. As a result, fairness concerns are more directly tied to individual policyholders in the long-term context. Secondly, while short-term products are often renewed annually, long-term policies often span over decades. The impact of a possibly unfair premium is far more enduring in the latter case, potentially persisting throughout the policyholder’s lifetime. These features highlight the importance of addressing fairness at the outset when pricing long-term insurance products.

The distinctive features of long-term insurance pricing, together with the lasting individual consequences of unfair premiums, motivate a careful examination of how fair pricing methodologies can be applied to long-term products. This has become even more pressing in the age of big data and artificial intelligence, as the use of complex predictive models has intensified regulatory concerns about algorithmic fairness. In particular, several U.S. jurisdictions have introduced laws that require insurers utilizing external consumer data to assess whether such use has resulted in unfair outcomes for protected groups. Notable examples include Colorado’s Senate Bill (SB) 21-169 (Colorado General Assembly, [2021](https://arxiv.org/html/2602.04791v1#bib.bib48 "Restrict insurers’ use of external consumer data")) and New York’s Circular Letter No. 7 (New York State Department of Financial Services, [2024](https://arxiv.org/html/2602.04791v1#bib.bib49 "Use of artificial intelligence systems and external consumer data and information sources in insurance underwriting and pricing")).

Given that fair pricing methods are readily applicable in the regression setting, one natural way to extend them to the long-term context is to reformulate the estimation of transition rates in multi-state models as a set of regression problems. This is precisely the approach we adopt. Specifically, we build upon the formulation dating back to Sverdrup ([1965](https://arxiv.org/html/2602.04791v1#bib.bib59 "Estimates and test procedures in connection with stochastic models for deaths, recoveries and transfers between different states of health")) and further developed in Renshaw and Haberman ([1995](https://arxiv.org/html/2602.04791v1#bib.bib58 "On the graduations associated with a multiple state model for permanent health insurance")); Wang et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib57 "Multistate health transition modeling using neural networks")), that the number of transitions for a given group over a prespecified time interval follows a Poisson distribution. We lend further support to this formulation using the Poisson-survival connection, and use it to construct a unified framework in which any multi-state model can be expressed as a series of Poisson regression models. Building on this framework, we propose a fair pricing procedure for long-term insurance products by first expressing the estimation of the underlying multi-state model in terms of its constituent Poisson regressions, and then applying a chosen fair pricing method to each regression component.

Our contributions are threefold. First, we make a methodological contribution by showing that a general multi-state modeling problem can be re-expressed as a set of Poisson regression models, with transition counts treated as outcomes and exposure times as offsets. This representation provides a unified and transparent statistical structure for estimating transition probabilities in long-term insurance settings. Moreover, this reformulation allows practitioners working on long-term pricing problems to leverage well-developed Poisson regression tools that are more commonly used in short-term insurance contexts.

Second, we make a conceptual contribution by proposing a framework that enables fair pricing methods developed for short-term insurance products to be applied in long-term settings. Specifically, we describe how representative approaches from each of three commonly used fairness adjustment categories—pre-processing, in-processing, and post-processing—can be adapted to the long-term pricing context in a coherent manner. Utilizing our unified representation, the proposed framework accommodates fairness adjustments without altering the underlying multi-state structure.

Third, we make a practical contribution by demonstrating how the proposed framework can be implemented through an LTCI pricing exercise using data from the University of Michigan Health and Retirement Study (HRS). Our case study illustrates how fairness adjustments applied at the transition level can be incorporated within a multi-state model and reflected in the resulting premiums of LTCI products. This exercise serves as a concrete illustration of the mechanics of fairness adjustments in long-term insurance pricing.

The rest of this paper is organized as follows. Section [2](https://arxiv.org/html/2602.04791v1#S2 "2 Pricing for Long-Term Insurance Products ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") reviews a general pricing approach for long-term insurance products. Section [3](https://arxiv.org/html/2602.04791v1#S3 "3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") summarizes existing fair pricing methods and discusses the challenges of adapting them to long-term contexts. Section [4](https://arxiv.org/html/2602.04791v1#S4 "4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") introduces a unified framework that presents a pathway toward overcoming these challenges. The proposed fair pricing framework for long-term insurance is then illustrated through a case study in Section [5](https://arxiv.org/html/2602.04791v1#S5 "5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") and presented in a more general form in Section [6](https://arxiv.org/html/2602.04791v1#S6 "6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). Finally, Section [7](https://arxiv.org/html/2602.04791v1#S7 "7 Discussion and Conclusion ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") concludes with a discussion of the broader implications of the proposed framework and directions for future research.

## 2 Pricing for Long-Term Insurance Products

A variety of long-term insurance products is available on the market, including life insurance, disability insurance, critical illness insurance, and LTCI. These products share several common features. First, benefit payouts are contingent upon the insured either transitioning to, or remaining in, a particular health state. Second, premiums collected in earlier periods are typically invested to fund coverage in later periods, so that pricing relies on expected present value calculations. Third, the duration of the policy is central to its value proposition, either because benefits are paid as a stream over time or because substantial future costs are spread across earlier periods.

The expected present value calculation involves transition probabilities between the health states of interest. We first describe how these multi-state transition models are set up and estimated, and then explain how the transition rates are used to price these products.

### 2.1 Multi-state transition models

Figure [1](https://arxiv.org/html/2602.04791v1#S2.F1 "Figure 1 ‣ 2.1 Multi-state transition models ‣ 2 Pricing for Long-Term Insurance Products ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") illustrates two multi-state models commonly used in the pricing of long-term insurance products. One of the most commonplace of such products, life insurance, may be viewed as being priced using a two-state model: this is shown in the left panel. There is a single possible transition type, as recovery from death is impossible. More generally, multi-state models are set up with three or more states, where returning from a state may be permitted. The right panel depicts such a model. This is a three-state model with healthy, disabled, and dead states, in which recovery from disability is permitted, resulting in four possible transition types. Depending on the application, alternative model specifications may restrict recovery or incorporate additional health states.

AliveDead(a)HealthyDisabledDead(b)


Figure 1: Multi-state transition models. Note: Panel (a) depicts the two-state model for pricing life insurance and annuity products. Panel (b) depicts a three-state model with recovery from disability.

Transitions between states are usually characterized by their transition intensities, which are modeled as functions of risk factors. A common specification assumes that each transition intensity follows a log-linear form in covariates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡λk,m​(t)=𝜷m′⋅𝐳k+𝜸m′⋅𝝎k​(t),\ln\lambda\_{k,m}(t)=\bm{\beta}^{\prime}\_{m}\cdot\mathbf{z}\_{k}+\bm{\gamma}^{\prime}\_{m}\cdot\bm{\omega}\_{k}(t), |  | (1) |

where, for the kkth individual, 𝐳k\mathbf{z}\_{k} denotes the vector of static covariates, and 𝝎k​(t)\bm{\omega}\_{k}(t) denotes the vector of time-varying covariates at time tt. The model parameters, 𝜽=(𝜷,𝜸)′\bm{\theta}=(\bm{\beta},\bm{\gamma})^{\prime}, are then estimated using the maximum likelihood estimation (MLE) method.

To this end, we formulate the log-likelihood function for the multi-state model. Suppose there are KK individuals, MM transition types, and II observation occasions. Let tk,it\_{k,i} denote the time of the ithi^{\text{th}} observation for the kthk^{\text{th}} individual, and let t^k,i\hat{t}\_{k,i} denote the time at which a transition occurs between the ithi^{\text{th}} and the (i+1)th(i+1)^{\text{th}} observations, if any. Define the indicator variable Tk,m,iT\_{k,m,i}, which equals 1 if a transition of type mm occurs in the interval between tit\_{i} and ti+1t\_{i+1}, and 0 otherwise. In addition, let Rk,m​(t)R\_{k,m}(t) indicate whether the kthk^{\text{th}} individual is exposed to the risk of experiencing transition type mm at time tt.

Based on these definitions, the log-likelihood function for the multi-state model can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | l​(𝜽)=∑k=1K∑m=1M∑i=1I−1lk,m,i​(𝜽),l\left(\bm{\theta}\right)=\sum\limits\_{k=1}^{K}\sum\limits\_{m=1}^{M}\sum\limits\_{i=1}^{I-1}l\_{k,m,i}\left(\bm{\theta}\right), |  | (2) |

where the contribution of individual kk, transition type mm, and observation occasion ii is given by

|  |  |  |
| --- | --- | --- |
|  | lk,m,i​(𝜽)=Tk,m,i​ln⁡λk,m​(t^k,i)−Rk,m​(tk,i)​∫tk,imin⁡{t^k,i,tk,i+1}λk,m​(u)​du−Rk,m​(t^k,i)​∫min⁡{t^k,i,tk,i+1}tk,i+1λk,m​(u)​du.\begin{split}l\_{k,m,i}\left(\bm{\theta}\right)=T\_{k,m,i}\,\ln\lambda\_{k,m}(\hat{t}\_{k,i})-R\_{k,m}(t\_{k,i})\int\_{t\_{k,i}}^{\min\{\hat{t}\_{k,i},t\_{k,i+1}\}}\lambda\_{k,m}(u)\mathrm{d}u\\ -R\_{k,m}(\hat{t}\_{k,i})\int\_{\min\{\hat{t}\_{k,i},t\_{k,i+1}\}}^{t\_{k,i+1}}\lambda\_{k,m}(u)\mathrm{d}u.\end{split} |  |

### 2.2 Pricing formula

We use the estimated transition intensities to derive actuarially fair premiums. Since premiums are paid at discrete points in time in practice, we work in a discrete-time setting. For simplicity, we consider annual time intervals, noting that the framework can be readily adapted to more frequent payment intervals.

A key step in the premium calculation is the computation of multi-year transition probabilities. These are obtained from the one-year transition probabilities via the Chapman-Kolmogorov equations. The one-year transition probabilities, in turn, are computed from the transition intensities using the matrix exponential, which solves the Kolmogorov forward equations.

Actuarially fair premiums are derived by equating the expected present value (EPV) of premiums to the EPV of benefits. The EPV of premiums equals the premium itself in the case of a single lump-sum payment. Alternatively, if a level premium of PP is paid annually in advance, and lapses are ignored, the EPV of premiums is given by

|  |  |  |
| --- | --- | --- |
|  | EPV​(Premiums)=P​∑t=0∞vt​Pr⁡(Jx+t∈𝒫∣Jx=Initial state),\mathrm{EPV}(\text{Premiums})=P\sum\_{t=0}^{\infty}v^{t}\Pr(J\_{x+t}\in\mathcal{P}\mid J\_{x}=\text{Initial state}), |  |

where vv is the discount factor, JxJ\_{x} denotes the health state at age xx, and 𝒫\mathcal{P} refers to the set of states in which premiums are payable.

Turning to benefits, a common type of benefit is payable while the insured is in a given state. Suppose that an amount BtB\_{t} is payable at time tt, conditional on the insured being in a benefit-paying state. The EPV of benefits is given by

|  |  |  |
| --- | --- | --- |
|  | EPV​(Benefits)=∑t=0∞vt​Bt​Pr⁡(Jx+t∈ℬ∣Jx=Initial health state),\mathrm{EPV}(\text{Benefits})=\sum\_{t=0}^{\infty}v^{t}\,B\_{t}\,\Pr(J\_{x+t}\in\mathcal{B}\mid J\_{x}=\text{Initial health state}), |  |

where ℬ\mathcal{B} is the set of states in which benefits are payable.

Another common type of benefit is a death benefit. If a unit benefit is payable at the end of the year of death, the EPV of the death benefit is

|  |  |  |
| --- | --- | --- |
|  | EPV​(Death benefit)\displaystyle\quad\mathrm{EPV}(\text{Death benefit}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑t=0∞vt+1​[Pr⁡(Jx+t+1=Dead∣Jx=Initial state)−Pr⁡(Jx+t=Dead∣Jx=Initial state)].\displaystyle=\sum\_{t=0}^{\infty}v^{t+1}\,\left[\Pr(J\_{x+t+1}=\text{Dead}\mid J\_{x}=\text{Initial state})-\Pr(J\_{x+t}=\text{Dead}\mid J\_{x}=\text{Initial state})\right]. |  |

## 3 Fair Pricing Methodology

Pricing methodologies that incorporate fairness constraints are rarely built from scratch. Instead, they typically begin with a model known to perform well on the desired task and then modify aspects of the model-fitting process to improve specific fairness metrics. These modifications can take place at three points relative to when the model is fit: before (pre-processing), during (in-processing), or after (post-processing).

In this section, we first outline the most prominent notions of fairness used in practice. We then discuss fair pricing methodologies at each of these three stages of modification: pre-processing, in-processing, and post-processing. Finally, we discuss how the characteristics of the methodologies at each of the three stages constrain generalization to long-term contexts.

### 3.1 Notions of fairness

To discuss existing fair pricing methodologies, we first define commonly used notions of fairness. We use the following notation throughout this discussion:

* •

  YY: the response variable, usually representing the realized loss and used in model estimation.
* •

  Y^\hat{Y}: the model prediction, usually representing the estimated premium which corresponds to the expected loss.
* •

  𝐙\mathbf{Z}: the vector of covariates representing policyholder characteristics used for underwriting.
* •

  SS: the sensitive attribute for the purposes of assessing fairness.

Notions of *group fairness*, developed extensively in the machine learning literature, are central to many existing fair pricing methodologies. The three most commonly used notions are the following (Barocas et al., [2023](https://arxiv.org/html/2602.04791v1#bib.bib28 "Fairness and machine learning: limitations and opportunities")); note that the notation ⟂\perp denotes statistical independence:

* •

  Demographic parity: Also known as *independence*, it requires that Y^⟂S\hat{Y}\perp S.
* •

  Equalized odds: Also known as *separation*, it requires that Y^⟂S∣Y\hat{Y}\perp S\mid Y.
* •

  Predictive parity: Also known as *sufficiency*, it requires that Y⟂S∣Y^Y\perp S\mid\hat{Y}.

Both equalized odds and predictive parity require conditioning on YY and Y^\hat{Y}, respectively. This conditioning is natural in classification settings, where outcomes (YY) and predictions (Y^\hat{Y}) are categorical. In actuarial applications, however, both YY and Y^\hat{Y} tend to be continuous variables, making these notions of fairness difficult to utilize. As a result, actuarial fair pricing methodologies that rely on group fairness most often focus on demographic parity (Grari et al., [2022](https://arxiv.org/html/2602.04791v1#bib.bib36 "A fair pricing model via adversarial learning"); Hu et al., [2024](https://arxiv.org/html/2602.04791v1#bib.bib39 "A sequentially fair mechanism for multiple sensitive attributes"); Lindholm et al., [2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")). This paper adopts the same focus.

While useful, enforcing notions of group fairness may result in unintended cross-subsidization in the actuarial context. For this reason, fair pricing methodologies may instead appeal to notions of *individual fairness*. Broadly speaking, individual fairness aims to ensure that similar individuals are treated similarly (Dwork et al., [2012](https://arxiv.org/html/2602.04791v1#bib.bib51 "Fairness through awareness")). The primary challenge in applying this notion lies in defining an appropriate metric of similarity. Consequently, much of the existing literature on individual fairness proposes intuitive fairness measures that can be viewed as falling within this category, rather than proposing an appropriate metric.

One notion of fairness this paper focuses on is the avoidance of *proxy discrimination* as defined by Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")). They notice that, even when the sensitive attribute SS is excluded from a model, conditioning on certain values of 𝐙\mathbf{Z} may yield 𝔼⁡[Y∣𝐙=𝐳]≈𝔼⁡[Y∣𝐙=𝐳,S=s]\operatorname{\mathbb{E}}[Y\mid\mathbf{Z}=\operatorname{\mathbf{z}}]\approx\operatorname{\mathbb{E}}[Y\mid\mathbf{Z}=\operatorname{\mathbf{z}},S=s] for some ss. In such cases, information about SS is inadvertently incorporated through the covariates 𝐙\mathbf{Z}. This phenomenon follows from the tower property of expectation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼⁡[Y∣𝐙=𝐳]\displaystyle\operatorname{\mathbb{E}}[Y\mid\operatorname{\mathbf{Z}}=\operatorname{\mathbf{z}}] | =∫s𝔼⁡[Y∣𝐙=𝐳,S=s]​dℙ​(S=s∣𝐙=𝐳).\displaystyle=\int\_{s}\operatorname{\mathbb{E}}[Y\mid\operatorname{\mathbf{Z}}=\operatorname{\mathbf{z}},S=s]\mathrm{d}\mathbb{P}(S=s\mid\operatorname{\mathbf{Z}}=\operatorname{\mathbf{z}}). |  | (3) |

Proxy discrimination therefore arises from the confluence of two effects: when SS has a non-negligible effect on the mean, and when 𝐙\mathbf{Z} is informative for SS. One way to mitigate this issue is to replace ℙ​(S=s∣𝐙=𝐳)\mathbb{P}(S=s\mid\operatorname{\mathbf{Z}}=\operatorname{\mathbf{z}}) with a probability measure that does not depend on 𝐙\mathbf{Z}. This idea underlies the methodology proposed by Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")), which we discuss in more detail in Section [3.2](https://arxiv.org/html/2602.04791v1#S3.SS2 "3.2 Types of processing for incorporating fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

### 3.2 Types of processing for incorporating fairness

We now discuss pre-processing, in-processing, and post-processing methods in turn, using one representative methodology for each to illustrate their key ideas.

*Pre-processing* methods aim to transform input data so that models trained on transformed data can produce predictions that better conform to a desired notion of fairness. A representative example is the optimal transport methodology of Lindholm et al. ([2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")). Recall that demographic parity requires S⟂Y^S\perp\hat{Y}. If Y^=g​(𝐙)\hat{Y}=g(\operatorname{\mathbf{Z}}) for some gg, then this requirement is satisfied whenever 𝐙⟂S\operatorname{\mathbf{Z}}\perp S. This methodology achieves such independence through the following steps:

* •

  Identify a candidate probability distribution under which 𝐙⟂S\operatorname{\mathbf{Z}}\perp S is satisfied.
* •

  Identify an optimal transport map rr to transform the observed distribution of 𝐙\mathbf{Z} to this candidate probability distribution.
* •

  Defining 𝐙⟂:=r​(𝐙)\mathbf{Z}^{\perp}:=r(\mathbf{Z}), we have 𝐙⟂⟂S\mathbf{Z}^{\perp}\perp S by construction. Hence, any model trained on (𝐙⟂,Y)(\mathbf{Z}^{\perp},Y) yields predictions Y^=g​(𝐙⟂)\hat{Y}=g(\mathbf{Z}^{\perp}) that satisfy demographic parity with respect to SS.

*In-processing* methods modify an existing model by altering the training objective, the training procedure, or both, so that the resulting predictions conform to a desired notion of fairness. A representative example is the adversarial debiasing methodology of Beutel et al. ([2017](https://arxiv.org/html/2602.04791v1#bib.bib26 "Data decisions and theoretical implications when adversarially learning fair representations")), which incorporates both types of modifications. Specifically, this methodology trains a neural network with the structure as seen in Figure [2](https://arxiv.org/html/2602.04791v1#S3.F2 "Figure 2 ‣ 3.2 Types of processing for incorporating fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). WW is an intermediate representation that is encouraged to contain no information about the sensitive attribute SS, by training WW adversarially to satisfy W⟂SW\perp S. The standard loss of the predictions with respect to YY (e.g., a likelihood-based loss) is then augmented with a penalty corresponding to the *negative* of the accuracy of predicting SS from WW. If the training succeeds in enforcing W⟂SW\perp S, then Y^=g​(W)\hat{Y}=g(W) is also independent of SS, thereby guaranteeing demographic parity.

𝐙\operatorname{\mathbf{Z}}Encoder f​(𝐙)f(\mathbf{Z})WWRegressor g​(W)g(W)YYAdversaryh​(W)h(W)SS


Figure 2: The adversarial learning framework of Beutel et al. ([2017](https://arxiv.org/html/2602.04791v1#bib.bib26 "Data decisions and theoretical implications when adversarially learning fair representations")). Note: W=f​(𝐙)W=f(\mathbf{Z}) refers to the trained representation, whereas ff, gg and hh are functions learned by the network.

*Post-processing* methods operate by applying an additional adjustment after predictions are generated, producing revised predictions Y^\hat{Y} that adhere to a desired notion of fairness. A representative example is the methodology of Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")). Recall from Equation ([3](https://arxiv.org/html/2602.04791v1#S3.E3 "In 3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")) their observation that 𝔼⁡[Y∣𝐙=𝐳]\operatorname{\mathbb{E}}[Y\mid\operatorname{\mathbf{Z}}=\operatorname{\mathbf{z}}] implicitly incorporates information on SS through the tower property of expectation. To remove this implicit dependence and thereby avoid proxy discrimination, they propose replacing ℙ​(S=s|𝐙=𝐳)\mathbb{P}(S=s|\mathbf{Z}=\mathbf{z}) with a probability measure that does not depend on 𝐙\mathbf{Z}. Their approach proceeds in two steps:

* •

  Fit a model that predicts μ​(𝐳,s)=𝔼⁡[Y∣𝐙=𝐳,S=s]\mu(\operatorname{\mathbf{z}},s)=\operatorname{\mathbb{E}}[Y\mid\operatorname{\mathbf{Z}}=\operatorname{\mathbf{z}},S=s].
* •

  Obtain the discrimination-free mean functional as

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | μ∗​(𝐳)\displaystyle\mu^{\*}(\operatorname{\mathbf{z}}) | =∫sμ​(𝐳,s)​dℙ∗​(S=s),\displaystyle=\int\_{s}\mu(\operatorname{\mathbf{z}},s)\mathrm{d}\mathbb{P}^{\*}(S=s), |  |

  where ℙ∗\mathbb{P}^{\*} is a user-specified probability measure.

### 3.3 Challenges in adapting existing methodologies to long-term insurance

We have seen that in-processing and post-processing techniques for incorporating fairness constraints rely on a single, well-defined outcome variable. However, in the long-term insurance setting where transition rates are estimated via multi-state models, it is unclear which quantity, if any, could serve this role. Over the lifetime of an insured, transitions may occur between multiple states, and in some settings, such as long-term care, individuals may return to a previously attained state (e.g., through recovery from disability). As a result, the notion of a single representative outcome is not well defined.

More broadly, the difficulty in choosing a single representative outcome complicates both the assessment of fairness and the formulation of fair pricing methodologies. For instance, demographic parity requires independence between the model predictions and the sensitive attribute. When it is unclear what constitutes the relevant prediction in a long-term context, enforcing demographic parity becomes problematic, even for methods that ostensibly do not interact with the response variable. Take the pre-processing methodology of Lindholm et al. ([2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")) as an example. Although it operates solely by transforming covariates to be independent of the sensitive attribute, such transformations are difficult to evaluate when it is unclear whether the resulting predictions actually satisfy demographic parity.

One may argue for the expected present value of the product’s cash flows to serve as the outcome. However, this choice renders the outcome product-dependent and does not align with standard practice in multi-state modeling, where the primary quantities being estimated are transition rates rather than prices. This contrasts with short-term insurance products, where the outcome variable directly corresponds to the expected loss being modeled. In general, whether the outcome used should be product-dependent (e.g., price) or product-agnostic (e.g., transition rates) needs to be resolved in developing a coherent fair pricing methodology for long-term insurance products.

## 4 A Unified Framework for Multi-state Modeling

The primary difficulty in extending fair pricing methodology to long-term insurance products lies in the absence of a clearly defined outcome variable within multi-state models. In this section, we propose a unified framework that reformulates any multi-state modeling problem as a set of Poisson regressions. In this setting, both the outcome variable and the corresponding predictions are well defined, thereby enabling the adaptation of fair pricing methodologies to the long-term insurance setting.

We begin by outlining the Poisson-survival connection, which forms the backbone of this framework. We then discuss practical considerations for implementing this approach, with particular emphasis on actuarial applications.

### 4.1 The Poisson-survival connection

We introduce our unified framework by building upon the notations used in Section [2.1](https://arxiv.org/html/2602.04791v1#S2.SS1 "2.1 Multi-state transition models ‣ 2 Pricing for Long-Term Insurance Products ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), but in a simplified setting involving a single individual. The key to this unified framework is the fact that any survival process can be viewed as a (possibly non-homogeneous) stopping Poisson process. Thus, over any fixed time interval, the number of events generated by such a process follows a Poisson distribution.

This representation extends to multi-state models. The time spent in a given state may be viewed as a competing risks process, where the competing risks correspond to the MM possible transitions. Each of the MM transitions can be modeled as an independent stopping Poisson process. As a result, over a fixed time interval, the number of occurrences for each of the MM transitions follows MM independent Poisson distributions.

This connection becomes explicit when examining the likelihood for a single individual. For simplicity, suppose each of the MM types of possible transitions has a constant transition rate λm\lambda\_{m}, and that all transitions are possible from the individual’s current state. Let t^\hat{t} denote the time of transition, and let TmT\_{m} be an indicator taking value 1 if the observed transition is of type mm and 0 otherwise. Let 𝜽\bm{\theta} denote the vector of model parameters. The likelihood is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(𝜽)\displaystyle L(\bm{\theta}) | =exp⁡(−t^​∑m=1Mλm)​∏m=1MλmTm.\displaystyle=\exp\left(-\hat{t}\sum\_{m=1}^{M}\lambda\_{m}\right)\prod\_{m=1}^{M}\lambda\_{m}^{T\_{m}}. |  |

We may rewrite this likelihood, up to a proportionality constant, as

|  |  |  |
| --- | --- | --- |
|  | L​(𝜽)∝∏m=1Mexp⁡(−t^⋅λm)​(t^⋅λm)TmTm!,\displaystyle L(\bm{\theta})\propto\prod\_{m=1}^{M}\frac{\exp\left(-\hat{t}\cdot\lambda\_{m}\right)(\hat{t}\cdot\lambda\_{m})^{T\_{m}}}{T\_{m}!}, |  |

which is equivalent to the likelihood of MM independent Poisson processes with intensity λm\lambda\_{m} observed over an interval of length t^\hat{t}, where the observed count for each process, TmT\_{m}, is limited to either 0 or 1.

In a practical multi-state model, an individual does not remain in a single state indefinitely. Because Poisson processes have independent increments over non-overlapping time intervals, the time spent in each successive state may be modeled as independent of the time spent in other states. Moreover, although there are MM possible transitions in the overall multi-state model, only a subset is possible from any given state. Thus, for each sojourn in a particular state, the competing risks component reduces to those transitions that are possible from that state.

### 4.2 The unified framework in practice

The assumption that each λm\lambda\_{m} is constant, both over an individual’s lifetime and across individuals, is overly restrictive for practical applications. We therefore relax this assumption by allowing λm\lambda\_{m} to vary with covariates. Time-varying covariates are readily accommodated by the model, as they are commonly specified in piecewise constant form in practice. The model can thus be partitioned into intervals over which the transition rates remain constant.

In long-term insurance, transition rates are traditionally modeled using a log-linear form, as given by Equation ([1](https://arxiv.org/html/2602.04791v1#S2.E1 "In 2.1 Multi-state transition models ‣ 2 Pricing for Long-Term Insurance Products ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")). However, several fair pricing methods explicitly require the use of neural networks to model the predicted value (see Section [6.3](https://arxiv.org/html/2602.04791v1#S6.SS3 "6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")), motivating a more flexible methodology. By viewing multi-state models as a set of Poisson regressions, one may employ any method compatible with a Poisson likelihood loss, such as generalized additive models, tree-based ensemble methods, and, importantly, neural network-based methods commonly used in fair pricing literature. This leads to the more general formulation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡λk,m​(t)=fm​(𝐳k,𝝎k​(t)).\ln\lambda\_{k,m}(t)=f\_{m}(\mathbf{z}\_{k},\bm{\omega}\_{k}(t)). |  | (4) |

We now specialize the framework to align with standard actuarial pricing practice. Insurers typically employ tables of annual transition probabilities for pricing, indexed by the insured’s attained age. We accommodate this convention by assuming a constant λm\lambda\_{m} for each integer-valued age xx, where age may be defined as age last birthday, age nearest birthday, or age next birthday. For the rest of this paper, we measure age as age last birthday.

We next consider the covariate structure relevant for underwriting and pricing. Because transition rates are estimated for underwriting purposes and applied at policy inception, covariates other than age are treated as static for a given insured. Accordingly, the kkth insured is associated with a vector of static covariates 𝐳k\mathbf{z}\_{k}. We further assume that the transition rates depend on time only through the insured’s attained age. Under these assumptions, the transition rate for insured kk, transition mm at age xx, denoted λk,m​(x)\lambda\_{k,m}(x), is modeled via the following specialization of Equation ([4](https://arxiv.org/html/2602.04791v1#S4.E4 "In 4.2 The unified framework in practice ‣ 4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡λk,m​(x)\displaystyle\ln\lambda\_{k,m}(x) | =fm​(𝐳k,x).\displaystyle=f\_{m}(\mathbf{z}\_{k},x). |  |

With this structure in place, for (k,m,x)(k,m,x) indexing the entry for age xx for insured kk in transition mm, we model the the transition event Tk,m,xT\_{k,m,x} as a Poisson random variable with mean τk,m,x⋅λk,m​(x)\tau\_{k,m,x}\cdot\lambda\_{k,m}(x), where τk,m,x∈[0,1]\tau\_{k,m,x}\in[0,1] denotes the exposure associated with Tk,m,xT\_{k,m,x}.

The value of τk,m,x\tau\_{k,m,x} depends on how the health state of insured kk changes at age xx. Recall that only a subset of transitions may be possible from any given health state. Thus, if throughout age xx, insured kk remains in states from which transition mm is impossible, we set τk,m,x=0\tau\_{k,m,x}=0 and exclude the observation from the estimation sample; otherwise, τk,m,x>0\tau\_{k,m,x}>0.

Running the Poisson regression requires the data to be structured so that age remains constant on each interval and that each transition count is paired with the appropriate exposure. An illustration of this restructuring process, using the data introduced in the case study of Section [5](https://arxiv.org/html/2602.04791v1#S5 "5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") and its associated multi-state model, is provided in Appendix [A](https://arxiv.org/html/2602.04791v1#A1 "Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). Once this restructuring is done, the Poisson regression for transition mm can then be run using the log-link function, with Tk,m,xT\_{k,m,x} as the number of occurrences, i.e., the response variable, ln⁡τk,m,x\ln\tau\_{k,m,x} as an offset variable, and (𝐳k,x)(\mathbf{z}\_{k},x) as covariates.

## 5 Case Study: Fair Pricing for LTCI

With the unified framework of Section [4](https://arxiv.org/html/2602.04791v1#S4 "4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") in place, we now introduce the general framework for applying fair pricing methods to long-term insurance products. Since this involves restructuring the data to accommodate the Poisson regressions required under the unified framework, the framework is best illustrated through an example. We conduct a case study that prices a stylized LTCI product using the HRS dataset. We focus on LTCI because both its underlying multi-state model and benefit structure are sufficiently complex to highlight the practical challenges that may arise when implementing this methodology.

In this section, we first describe how we use the HRS data in our case study. We then present three types of LTCI premiums, including a fairness-adjusted premium obtained by adapting the discrimination-free pricing formula of Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")).

### 5.1 Dataset construction from the HRS

Given the proprietary nature of LTCI portfolio data, we rely on publicly available data from the HRS for our case study. The HRS is a biennial panel survey of initially non-institutionalized Americans aged 50 and older since 1992. The extensive range of variables collected by HRS and its longitudinal design make this dataset well-suited for modeling health state transitions and examining their associations with various covariates. We analyze data from 1998 to 2020 due to inconsistencies in survey questions on functional limitations before 1998 (Fong et al., [2015](https://arxiv.org/html/2602.04791v1#bib.bib65 "Disaggregating activities of daily living limitations for predicting nursing home admission")). To reduce the likelihood of multiple unobserved health state transitions between interview waves, we restrict our sample to respondents who participated in every interview following their entry into the survey.

We construct two datasets to support our modeling approach. The first dataset records the timing of health state transitions, assuming the underlying process follows the three-state model shown in the right panel of Figure [1](https://arxiv.org/html/2602.04791v1#S2.F1 "Figure 1 ‣ 2.1 Multi-state transition models ‣ 2 Pricing for Long-Term Insurance Products ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). The health states are defined based on six Activities of Daily Living (ADLs) and the Langa-Weir classification of cognitive function (Langa et al., [2020](https://arxiv.org/html/2602.04791v1#bib.bib64 "Langa-Weir classification of cognitive function (1995 onward)")). Consistent with benefit triggers commonly used in commercial LTCI products (Administration for Community Living, [2020](https://arxiv.org/html/2602.04791v1#bib.bib37 "Receiving long-term care insurance benefits")), an individual is classified as disabled if they have two or more ADL limitations or exhibit cognitive impairment. The date of death is directly available in the HRS, and all other transitions are assumed to occur at the midpoint between two consecutive interviews.
For estimation, the raw transition data from the first dataset are not directly suitable for the Poisson regressions required by the unified framework. We use the procedure described in Appendix [A](https://arxiv.org/html/2602.04791v1#A1 "Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") to reshape the data into the form discussed in Section [4.2](https://arxiv.org/html/2602.04791v1#S4.SS2 "4.2 The unified framework in practice ‣ 4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

The second dataset focuses on covariate information collected at each individual’s initial interview, mirroring the underwriting process by recording baseline characteristics only at study entry. Table [1](https://arxiv.org/html/2602.04791v1#S5.T1 "Table 1 ‣ 5.1 Dataset construction from the HRS ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") lists the covariates included in our study, all of which are based on self-reported data. These covariates include factors likely to influence disability and mortality, such as health behaviors (e.g., drinking and smoking), socioeconomic variables (e.g., education), as well as demographic attributes relevant to fairness considerations, such as race (with three categories: White/Caucasian, Black/African American, and Other) and gender.

Table 1: List of variables. C denotes categorical variables, and N denotes numerical variables.

|  |  |  |
| --- | --- | --- |
| Demographic | Health and disease | Finance |
| Age (N) | Self-rated health (C) | Non-housing wealth§ (N) |
| Gender (C) | Ever had diabetes (C) | Household income∥\| (N) |
| Race† (C) | Ever had lung disease (C) |  |
| Ethnicity‡ (C) | Ever had heart problems (C) |  |
| Years of education (C) | Ever had stroke (C) |  |
| Census region (C) | Body mass index (BMI) (N) |  |
| Marital status (C) | Ever drinks any alcohol (C) |  |
| Labor force participation (C) | Ever smoked cigarettes (C) |  |
| Number of household members (N) |  |  |

* †

  Race includes three categories: White/Caucasian, Black/African American, and Other.
* ‡

  Ethnicity indicates whether the survey respondent identifies as Hispanic.
* §

  Non-housing wealth includes both tangible assets (e.g., vehicles, businesses) and financial assets (e.g., retirement accounts, stocks, bonds, savings), net of non-mortgage debt.
* ∥\|

  Household income is the total income for the previous calendar year, including respondent and spouse earnings, pensions and annuities, Supplemental Security Income and Social Security Disability, Social Security retirement benefits, unemployment and workers’ compensation, other government transfers, household capital income, and other income sources.
* Note: Job physicality was initially included but was later excluded due to a high proportion of missing values.

Before the covariate dataset can be used, missing values must be addressed. We first remove variables with a particularly large proportion of missing data, which leads to the exclusion of job physicality, as it contains 14% missing values. We then delete all remaining incomplete observations, resulting in the removal of 3% of entries and yielding a complete final dataset.

### 5.2 LTCI pricing under different settings

Although the HRS is not designed as an insurance dataset, the health state transition rates estimated from the surveyed population are sufficient for our purposes and can be used to price LTCI products. We model transition rates using log-linear models, as these are widely adopted in the literature. This approach allows us to leverage the glm routine in the R programming language with a log-link and the Poisson family of distributions. When the data is appropriately structured, estimation proceeds straightforwardly using R’s native formula and offset interface.

To develop a parsimonious model, we fit the model with all the covariates and then identify covariate transformations—such as regrouping categorical levels—that do not materially affect model fit. As this case study is intended to showcase our pricing methodology, we relegate these details to Appendix [B](https://arxiv.org/html/2602.04791v1#A2 "Appendix B Model Selection for Illustrative GLM Model ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). After these transformations are implemented, the model is refit using all available covariates.

We treat the transition rates estimated from our model, for the purposes of this case study, as if they describe the experience of a representative LTCI portfolio. To approximate a realistic insured population, we restrict our pricing analysis to individuals aged 50–80 at issue (on an age-last-birthday basis) and exclude those with disqualifying health conditions. Specifically, eligible individuals must not be disabled at issue and must not report severe heart or lung conditions, diabetes, or stroke. These restrictions yield a relatively healthy baseline population suitable for LTCI pricing analysis.

We consider an LTCI product with a lump-sum premium paid at policy inception and an annual benefit of $1 for each year spent in the disabled state. We assume that each individual in our baseline insured population represents an insured whose coverage begins immediately after the individual’s previous birthday. We also assume that this insured’s transition rates are given by those predicted for the same individual, with a terminal age of 110 imposed on the transition rates. Using the pricing formula introduced in Section [2.2](https://arxiv.org/html/2602.04791v1#S2.SS2 "2.2 Pricing formula ‣ 2 Pricing for Long-Term Insurance Products ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), the lump-sum premium for a policy issued to an individual aged xx is given by

|  |  |  |
| --- | --- | --- |
|  | Lump sum premium=∑t=0110−xvt​Pr⁡(Jx+t=Disabled∣Jx=Healthy),\text{Lump sum premium}=\sum\_{t=0}^{110-x}v^{t}\Pr(J\_{x+t}=\text{Disabled}\mid J\_{x}=\text{Healthy}), |  |

where the discount factor vv is set to 1.03−11.03^{-1}.

We choose race as the sensitive attribute, denoted by SS. All other covariates, where we denote the non-age covariates collectively as 𝐳\mathbf{z}, are listed in Table [1](https://arxiv.org/html/2602.04791v1#S5.T1 "Table 1 ‣ 5.1 Dataset construction from the HRS ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). To evaluate fairness in pricing, we compute three types of premiums under different modeling assumptions:

* •

  Best-estimate price: Transition rates λ^m​(𝐳,x,s)\hat{\lambda}\_{m}(\mathbf{z},x,s), for transition type m=1,…,4m=1,\ldots,4, are estimated using all available covariates 𝐳\mathbf{z}, the policyholder’s age xx, and their sensitive attribute ss, based on the fitted multi-state GLM model:

  |  |  |  |
  | --- | --- | --- |
  |  | λ^m​(𝐳,x,s)=exp⁡(f^m(Best)​(𝐳,x,s)),\hat{\lambda}\_{m}(\mathbf{z},x,s)=\exp\!\left(\hat{f}^{(\mathrm{Best})}\_{m}(\mathbf{z},x,s)\right), |  |

  where f^m(Best)​(⋅)\hat{f}^{(\mathrm{Best})}\_{m}(\cdot) denotes the fitted GLM predictor function that includes race as an explanatory variable.
* •

  Race-blind price: Transition rates λ^m​(𝐳,x)\hat{\lambda}\_{m}(\mathbf{z},x) are re-estimated after removing race from the covariate set, which assumes the insurer is unaware of the sensitive attribute:

  |  |  |  |
  | --- | --- | --- |
  |  | λ^m​(𝐳,x)=exp⁡(f^m(Blind)​(𝐳,x)),\hat{\lambda}\_{m}(\mathbf{z},x)=\exp\!\left(\hat{f}^{(\mathrm{Blind})}\_{m}(\mathbf{z},x)\right), |  |

  where f^m(Blind)​(⋅)\hat{f}^{(\mathrm{Blind})}\_{m}(\cdot) denotes the re-fitted GLM predictor function excluding race from both data and estimation.
* •

  Fairness-adjusted price: Transition rates are adjusted using the λm∗​(𝐳,x)\lambda^{\*}\_{m}(\mathbf{z},x) obtained using the procedure which will be described in detail in Section [5.3](https://arxiv.org/html/2602.04791v1#S5.SS3 "5.3 Tailored post-processing for long-term insurance ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

### 5.3 Tailored post-processing for long-term insurance

To obtain fairness-adjusted transition rates, we adapt the discrimination-free pricing methodology of Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")) to the long-term insurance context.
The objective of this methodology is to prevent nonsensitive covariates from acting as proxies for the sensitive attribute. In our setting, these covariates are (𝐙,x)(\mathbf{Z},x). Proxying through them can therefore be mitigated by fitting each λm\lambda\_{m} as a function of (𝐙,x,S)(\mathbf{Z},x,S), and then taking an appropriate expectation of λm\lambda\_{m} with respect to a chosen distribution for SS.

A standard choice for this distribution is the empirical marginal distribution. However, this raises the question of which empirical distribution to use: that for the sample of policies, or the respective ones for each Poisson regression problem. As discussed briefly in Sections [4.2](https://arxiv.org/html/2602.04791v1#S4.SS2 "4.2 The unified framework in practice ‣ 4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") and [5.1](https://arxiv.org/html/2602.04791v1#S5.SS1 "5.1 Dataset construction from the HRS ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") and in detail in Appendix [A](https://arxiv.org/html/2602.04791v1#A1 "Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), additional observations are artificially created to maintain constant transition rates over each time interval. The number of such observations is an artifact of each insured’s realized health trajectory. Hence, the empirical distribution at the policy level is the more appropriate choice. We therefore propose the following post-processing procedure for long-term insurance:

1. 1.

   Begin with the sample of observed policies. Let 𝐳k\mathbf{z}\_{k}, xu,kx\_{u,k}, and sks\_{k} denote the vector of covariates, the age at entry, and the sensitive, respectively, for the kkth insured, and let ℙn\mathbb{P}\_{n} denote the empirical distribution of this sample.
2. 2.

   Construct MM datasets corresponding to each type of transition. Using the Poisson regression technique of choice, estimate λm\lambda\_{m} as a function of 𝐙,x\mathbf{Z},x, and SS.
3. 3.

   For each desired combination of (𝐳,x)(\mathbf{z},x), calculate the discrimination-free transition rate as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | λm∗​(𝐳,x)\displaystyle\lambda\_{m}^{\*}(\mathbf{z},x) | =∫λ^m​(𝐳,x,s)​dℙn​(s)\displaystyle=\int\hat{\lambda}\_{m}(\mathbf{z},x,s)\mathrm{d}\mathbb{P}\_{n}(s) |  |
4. 4.

   The price for any insured P​(𝐳,xu)P(\mathbf{z},x\_{u}) can then be calculated using λ^m∗​(𝐳,x)\hat{\lambda}^{\*}\_{m}(\mathbf{z},x).

This procedure ensures that the calculated λ∗​(𝐳,x)\lambda^{\*}(\mathbf{z},x) is estimated free from proxy discrimination with respect to (𝐙,x)(\mathbf{Z},x), and consequently that the resulting price P​(𝐳,xu)P(\mathbf{z},x\_{u}) inherits this property.

### 5.4 Results and discussion

Figure [3](https://arxiv.org/html/2602.04791v1#S5.F3 "Figure 3 ‣ 5.4 Results and discussion ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") shows premiums computed under three different modeling assumptions. Each point represents the lump-sum premium charged to an individual. For a given age and racial group, premiums vary due to differences in nonsensitive covariates used for pricing. To facilitate comparison across racial groups, we overlay three smoothed curves in each panel, one for each racial group. These curves are obtained using generalized additive models, with the lump-sum premium regressed on age.

![Refer to caption](x1.png)


Figure 3: Lump-sum premiums by racial group. Note: Each panel represents a different modeling assumption, as indicated by the panel title. There are three smoothed lines in each panel, one for each racial group. Each smoothed line is generated using a generalized additive model (GAM), regressing the lump-sum premium on age. The gray band represents the 95% confidence interval of the GAM.

Interestingly, across races and modeling assumptions, the smoothed lump-sum premiums exhibit relatively little variation with age. This pattern reflects the interaction of two opposing effects. As age increases, the probability of transitioning from healthy to disabled rises, while that of recovery from disability declines, increasing the expected present value of benefits. At the same time, mortality rates increase with age, reducing the expected duration an individual spends in the disabled state.

We now visually assess how each set of prices compares in terms of group fairness. We first compare the best estimate prices, whose underlying transition rates explicitly include race as a covariate, with the race-unaware prices, which omit the covariate of race. The clearer separation between the White/Caucasian and the other two groups under the best estimate prices suggests that race is an important predictor in the fitted model. Indeed, according to the likelihood contributions for each predictor in Appendix [C](https://arxiv.org/html/2602.04791v1#A3 "Appendix C Likelihood Contributions of Fitted Covariates ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), race is the third most important predictor in the model, behind age and years of education.

Although race-unaware prices exclude race as a covariate, the gap between the average prices nevertheless persists, albeit to a smaller extent. While race-unaware transition rates no longer include direct effects of race, indirect effects may still arise through other covariates that are correlated with race. Such proxy effects likely contribute to the remaining disparity.

To address this issue, we apply the post-processing procedure adapted from Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")) to ensure that such inference of the sensitive attribute is no longer present in the adjusted transition rates. However, as shown by Lindholm et al. ([2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")), the absence of proxy discrimination and notions of group fairness in general do not imply one another. Hence, we do not expect price differences to be fully eliminated. Indeed, a comparison of the middle and right panels of Figure [3](https://arxiv.org/html/2602.04791v1#S5.F3 "Figure 3 ‣ 5.4 Results and discussion ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") shows that, although the gap persists, it is further reduced. Since the reweighting method eliminates indirect effects of race, we interpret the remaining gap as reflecting average differences attributable solely to the direct effects of the other covariates.

Notably, the reduction in the price gap is most pronounced between the Black/African American and White/Caucasian groups, whereas the gap between the Other and White/Caucasian groups appears largely unchanged. This suggests that for the Black/African American group, the race-unaware prices contain substantial indirect effects of race through other covariates, which are effectively mitigated by the adjusted prices. In contrast, indirect effects of race appear to be much weaker for the Other group.

## 6 A Fair Pricing Framework for Long-Term Insurance

Through the case study, we illustrated how to apply our fair pricing framework in the LTCI context using the post-processing methodology of Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")). In this section, we provide a pipeline for applying this framework more broadly. We first describe the overall framework and then provide two illustrations—corresponding to pre-processing and in-processing approaches—to demonstrate its practical implementation and to discuss issues that may arise in application.

### 6.1 General framework

The unified framework introduced in Section [4](https://arxiv.org/html/2602.04791v1#S4 "4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") expresses transition rate estimation in multi-state models as a set of Poisson regression problems. This leads to a two-step procedure for applying fair pricing methods to long-term insurance products:

1. 1.

   Reformulate the multi-state modeling problem in terms of its constituent Poisson regression problems.
2. 2.

   Apply the desired fair pricing method to each of the constituent Poisson regression problems.

This two-step procedure has proven effective for the post-processing approach of Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")), as demonstrated in Section [5](https://arxiv.org/html/2602.04791v1#S5 "5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). However, as we shall see in Sections [6.2](https://arxiv.org/html/2602.04791v1#S6.SS2 "6.2 Illustration 1: Pre-processing via optimal transport ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") and [6.3](https://arxiv.org/html/2602.04791v1#S6.SS3 "6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), extending fairness concepts to the multi-state setting requires particular care because age enters not only into the estimation of transition rates, but also into the calculation of premiums through the age at underwriting. Consequently, care needs to be taken in the treatment of age in each case, depending both on the exact methodology being considered and the notion of fairness desired.

### 6.2 Illustration 1: Pre-processing via optimal transport

We begin by illustrating how our framework applies to the optimal transport methodology of Lindholm et al. ([2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")), which performs pre-processing. Optimal transport maps are generally ill-defined for categorical variables, which lack a natural distance metric. This is an issue even for short-term insurance products. For simplicity, we present the case only where 𝐙\mathbf{Z} is solely composed of continuous covariates.

Recall that demographic parity requires independence between the outcome variable and the sensitive variable, i.e., Y^⟂S\hat{Y}\perp S. In Lindholm et al. ([2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")), this requirement is enforced by altering covariate values such that they are independent of the sensitive variable SS. In the long-term insurance setting, the main challenge concerns the treatment of age, and the appropriate handling depends on the form of demographic parity being imposed.

Let xux\_{u} denote the age of an insured at underwriting, and let P​(𝐳,xu)P(\mathbf{z},x\_{u}) denote the price charged to an insured with covariates 𝐳\mathbf{z} and age xux\_{u}. One could argue that demographic parity should require the prices charged to each insured, P​(𝐙,xu)P(\mathbf{Z},x\_{u}), to be independent of SS, where 𝐙\mathbf{Z} and xux\_{u} are both random realizations from the data. However, enforcing this condition would require altering ages, raising additional fairness concerns. We therefore adopt a simpler requirement: for each fixed value of x∗x^{\*}, P​(𝐙,x∗)P(\mathbf{Z},x^{\*}) should be independent of SS.

We propose the following modified procedure for the long-term insurance context:

1. 1.

   Begin with the sample of observed policies, where 𝐳k\mathbf{z}\_{k} and xu,kx\_{u,k}, respectively, denote the vector of covariates and the age at entry of the kkth insured, and let ℙn\mathbb{P}\_{n} denote the empirical distribution of this sample.
2. 2.

   Identify a candidate distribution ℙ⟂\mathbb{P}^{\perp} under which 𝐙⟂S\mathbf{Z}\perp S, while preserving the marginal distribution of xux\_{u} from ℙn\mathbb{P}\_{n}.
3. 3.

   Determine the optimal transport map rr which maps the empirical probability distribution ℙn\mathbb{P}\_{n} to ℙ⟂\mathbb{P}^{\perp}.
4. 4.

   Define 𝐳k⟂:=r​(𝐳k)\mathbf{z}\_{k}^{\perp}:=r(\mathbf{z}\_{k}). Using the modified data (𝐳k⟂,xu,k)(\mathbf{z}^{\perp}\_{k},x\_{u,k}), construct the Poisson regression datasets for each of the MM transitions, and estimate the corresponding transition rates λm\lambda\_{m}.
5. 5.

   Calculate the price for the kkth insured, P​(𝐳k⟂,xu,k)P(\mathbf{z}\_{k}^{\perp},x\_{u,k}), using the estimated λm\lambda\_{m}.

While the actual premium charged to each insured still depends on the insured’s age at entry, the form of demographic parity guaranteed by this procedure is *conditional on issue age*. For each fixed age xx and transition mm, λm​(𝐳k⟂,x)\lambda\_{m}(\mathbf{z}\_{k}^{\perp},x) is independent of SS. The price P​(𝐳k⟂,x∗)P(\mathbf{z}\_{k}^{\perp},x^{\*}) is then a function of λm​(𝐳k⟂,x)\lambda\_{m}(\mathbf{z}^{\perp}\_{k},x) evaluated over ages x=x∗,x∗+1,…,110x=x^{\*},x^{\*}+1,\ldots,110 and transitions m=1,2,…,Mm=1,2,\ldots,M. Since each of these quantities is independent of SS, the resulting price is likewise independent of SS for each x∗x^{\*}.

### 6.3 Illustration 2: In-processing via adversarial debiasing

We now illustrate how the methodology of Beutel et al. ([2017](https://arxiv.org/html/2602.04791v1#bib.bib26 "Data decisions and theoretical implications when adversarially learning fair representations")) can be adapted to long-term insurance pricing. To this end, we supplement the general description in Section [3.2](https://arxiv.org/html/2602.04791v1#S3.SS2 "3.2 Types of processing for incorporating fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") with the specific adversarial learning procedure as described below.

The objective function of the model is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | minf,g⁡maxh⁡𝔼​[LY​(Y,g​(f​(𝐙)))−α​LS​(S,h​(f​(𝐙)))],\displaystyle\min\_{f,g}\;\max\_{h}\;\mathbb{E}\Big[L\_{Y}\!\left(Y,\;g\big(f(\mathbf{Z})\big)\right)-\alpha\,L\_{S}\!\left(S,\;h\big(f(\mathbf{Z})\big)\right)\Big], |  | (5) |

where LYL\_{Y} is the loss with respect to the outcome variable (here, the likelihood loss), and LSL\_{S} is the cross-entropy loss. Training proceeds via alternating two steps: an adversarial gradient step to maximize Equation ([5](https://arxiv.org/html/2602.04791v1#S6.E5 "In 6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")) with respect to hh, and a model gradient step to minimize Equation ([5](https://arxiv.org/html/2602.04791v1#S6.E5 "In 6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")) with respect to (f,g)(f,g).

By alternating between the adversary and the model, one can in principle obtain W⟂SW\perp S, while ensuring WW remains maximally predictive for YY. As in the case of pre-processing, W⟂SW\perp S implies Y^=g​(W)⟂S\hat{Y}=g(W)\perp S, yielding demographic parity. In practice, however, achieving demographic parity often requires sacrificing accuracy to an unacceptable degree and vice versa. The parameter α\alpha therefore serves as a tuning parameter to find a suitable balance between these two objectives.

We now describe how this methodology can be tailored to the long-term context. A key modeling choice concerns the treatment of age, specifically whether it forms part of the representation. Since each λm\lambda\_{m} is a function of (𝐙,x)(\mathbf{Z},x), one possibility would be to include age directly in the representation as W=f​(𝐙,x)W=f(\mathbf{Z},x). However, it is difficult to define how the adversary should interact with such a representation in a way that guarantees some form of independence between the prices and SS. We therefore restrict the representation to W=f​(𝐙)W=f(\mathbf{Z}), and train the network such that W⟂SW\perp S under the distribution of observed policyholders; the predicted transition rate is then obtained as λ^m=gm​(W,x)\hat{\lambda}\_{m}=g\_{m}(W,x). While this specification does not guarantee that P​(𝐙,xu)P(\mathbf{Z},x\_{u}) is independent of SS, it does guarantee that P​(𝐙,x∗)P(\mathbf{Z},x^{\*}) is independent of SS for each fixed value of x∗x^{\*}.

Given that we are training MM regression problems—one for each transition—we again have two choices in how the representations are trained. The more straightforward approach is to obtain separate representations and adversaries for each transition. While this approach aligns closely with the divide-and-conquer structure of the unified framework, it is relatively data-inefficient for training the adversary since we simply apply the methodology of Beutel et al. ([2017](https://arxiv.org/html/2602.04791v1#bib.bib26 "Data decisions and theoretical implications when adversarially learning fair representations")) MM times. We therefore relegate this approach to Appendix [D](https://arxiv.org/html/2602.04791v1#A4 "Appendix D A Divide-and-Conquer Version of In-Processing ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

Instead, we focus on a more data-efficient approach which utilizes a common representation and a common adversary across all transitions. Separate regressors for each transition then make use of this common representation, along with age, to obtain predictions. The architecture for this approach is shown in Figure [4](https://arxiv.org/html/2602.04791v1#S6.F4 "Figure 4 ‣ 6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

𝐙,x\operatorname{\mathbf{Z}},x𝐙\mathbf{Z}Encoder f​(𝐙)f(\mathbf{Z})xxWWW,xW,xAdversaryh​(W)h(W)SSRegressor 2 g2​(W,x)g\_{2}(W,x)Y2Y\_{2}Regressor 1 g1​(W,x)g\_{1}(W,x)Y1Y\_{1}⋮\vdotsRegressor MMgM​(W,x)g\_{M}(W,x)YMY\_{M}


Figure 4: Adversarial learning framework tailored to long-term insurance, adapted from Beutel et al. ([2017](https://arxiv.org/html/2602.04791v1#bib.bib26 "Data decisions and theoretical implications when adversarially learning fair representations")). Note: 𝐙\mathbf{Z} and xx refer to the non-age covariates and age, respectively; W=f​(𝐙)W=f(\mathbf{Z}) is the trained representation, and functions ff, hh and g1,…,gMg\_{1},\ldots,g\_{M} are functions learned by the network.

The proposed procedure is as follows:

1. 1.

   Begin with the sample of observed policies, with 𝐳k\mathbf{z}\_{k}, xu,kx\_{u,k}, and sks\_{k}, respectively, denoting the vector of covariates, age at entry, and sensitive attribute of the kkth insured.
2. 2.

   Let wk=f​(𝐳k)w\_{k}=f(\mathbf{z}\_{k}). Using cross-entropy loss LSL\_{S}, form the adversary loss

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝐿𝑜𝑠𝑠A​d​v\displaystyle\mathit{Loss}\_{Adv} | =1n​∑k=1nLS​(sk,h​(wk)).\displaystyle=\frac{1}{n}\sum\_{k=1}^{n}L\_{S}(s\_{k},h(w\_{k})). |  |
3. 3.

   Construct MM datasets corresponding to each transition. Let (k,m,j)(k,m,j) index the jjth entry for the kkth insured and the mmth transition, with nk,mn\_{k,m} denoting the number of entries and nm=∑k=1nnk,mn\_{m}=\sum\_{k=1}^{n}n\_{k,m}. Using the Poisson likelihood loss LYL\_{Y}, form the loss for the mmth transition

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝐿𝑜𝑠𝑠m\displaystyle\mathit{Loss}\_{m} | =1nm​∑k=1n∑j=1nk,mLY​(Yk,m,j,gm​(wk,xk,m,j)).\displaystyle=\frac{1}{n\_{m}}\sum\_{k=1}^{n}\sum\_{j=1}^{n\_{k,m}}L\_{Y}(Y\_{k,m,j},g\_{m}(w\_{k},x\_{k,m,j})). |  |
4. 4.

   Form the total loss

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | 𝐿𝑜𝑠𝑠\displaystyle\mathit{Loss} | =1∑m=1Mnm​∑m=1Mnm​𝐿𝑜𝑠𝑠m−α​𝐿𝑜𝑠𝑠A​d​v.\displaystyle=\frac{1}{\sum\_{m=1}^{M}n\_{m}}\sum\_{m=1}^{M}n\_{m}\mathit{Loss}\_{m}-\alpha\mathit{Loss}\_{Adv}. |  | (6) |
5. 5.

   Alternate between gradient steps to maximize Equation ([6](https://arxiv.org/html/2602.04791v1#S6.E6 "In item 4 ‣ 6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")) with respect to hh, and to minimize Equation ([6](https://arxiv.org/html/2602.04791v1#S6.E6 "In item 4 ‣ 6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")) with respect to (f,g1,…,gM)(f,g\_{1},\ldots,g\_{M}), until convergence.
6. 6.

   Calculate the price for the kkth insured, P​(𝐳k,xu,k)P(\mathbf{z}\_{k},{x\_{u,k}}), using λ^m​(𝐳,x)=gm​(f​(𝐳),x)\hat{\lambda}\_{m}(\mathbf{z},x)=g\_{m}(f(\mathbf{z}),x).

Under this adversarial learning procedure, WW is independent of SS. For each transition mm and fixed age xx, λ^m​(𝐳k,x)=gm​(W,x)\hat{\lambda}\_{m}(\mathbf{z}\_{k},x)=g\_{m}(W,x) is a function of WW and is therefore independent of SS. Thus, as a function of such quantities, P​(𝐳k,x∗)P(\mathbf{z}\_{k},x^{\*}) is independent of SS for each fixed x∗x^{\*}. Again, the actual prices charged to each insured will differ from those used to measure demographic parity.

## 7 Discussion and Conclusion

We presented a unified framework for modeling transition rates in multi-state models using Poisson regression, and demonstrated how this framework enables the application of existing fair pricing methods to long-term insurance products. We illustrated the approach through a pricing exercise based on the HRS data, extending the post-processing methodology of Lindholm et al. ([2022](https://arxiv.org/html/2602.04791v1#bib.bib42 "Discrimination-free insurance pricing")) to the long-term insurance setting. We further discussed how the framework can be extended to the in-processing and pre-processing methodologies of Beutel et al. ([2017](https://arxiv.org/html/2602.04791v1#bib.bib26 "Data decisions and theoretical implications when adversarially learning fair representations")) and Lindholm et al. ([2024b](https://arxiv.org/html/2602.04791v1#bib.bib29 "What is fair? Proxy discrimination vs. demographic disparities in insurance pricing")), respectively.

While this paper focused on applying the unified Poisson-based framework to fair pricing in long-term insurance, the framework itself is substantially more general than the specifications used in our case study. We adopted log-linear models in our case study to reflect standard practice in multi-state modeling. However, a key contribution of the unified framework is that it removes the constraints imposed by the complexity of traditional multi-state likelihood functions, thereby accommodating more flexible functional forms for transition rates, such as that given by Equation ([4](https://arxiv.org/html/2602.04791v1#S4.E4 "In 4.2 The unified framework in practice ‣ 4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")). For example, an insurer employing our unified framework may choose to model transition rates as smooth functions of age using generalized additive models, aligning with the standard practice of smoothing and graduating age-specific mortality rates. This added flexibility opens the door to richer modeling choices beyond log-linear specifications, offering a new direction for improving the modeling and pricing of complex products such as LTCI.

As regulators continue to assess and enforce fairness in insurance pricing, a key challenge is ensuring that chosen notions of fairness are applied coherently across different insurance products. One approach is to ensure fairness with respect to the price of each product. Thus, in adapting existing methodologies to the long-term insurance context, we have sought—wherever possible—to ensure that the final computed price also satisfies the enforced notion of fairness. As demonstrated in Section [6](https://arxiv.org/html/2602.04791v1#S6 "6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), doing so is possible for certain notions of fairness such as demographic parity, but requires careful formulation of the adapted methodology. It is unclear whether this ability to preserve the notion of fairness in the final price can be replicated for all existing notions or future proposed notions of fairness, but it is nevertheless a desired objective due to the coherence of defining fairness at the price level.

## Acknowledgments

We acknowledge the financial support provided by the Society of Actuaries Research Institute.

## References

* Administration for Community Living (2020)
  Receiving long-term care insurance benefits.
  Web page
   U.S. Department of Health and Human Services, Washington, D.C..
  External Links: [Link](https://acl.gov/ltc/costs-and-who-pays/what-is-long-term-care-insurance/receiving-long-term-care-insurance-benefits)
  Cited by: [§5.1](https://arxiv.org/html/2602.04791v1#S5.SS1.p2.1 "5.1 Dataset construction from the HRS ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* C. A. Araiza Iturria, M. Hardy, and P. Marriott (2024)
  A discrimination-free premium under a causal framework.
  North American Actuarial Journal 28 (4),  pp. 801–821.
  External Links: [Document](https://dx.doi.org/10.1080/10920277.2023.2291524)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p1.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* S. Barocas, M. Hardt, and A. Narayanan (2023)
  Fairness and machine learning: limitations and opportunities.
   MIT Press.
  Cited by: [§3.1](https://arxiv.org/html/2602.04791v1#S3.SS1.p2.1 "3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* A. Beutel, J. Chen, Z. Zhao, and E. H. Chi (2017)
  Data decisions and theoretical implications when adversarially learning fair representations.
  Fairness, Accountability and Transparency in Machine Learning ’17,  pp. 1–5.
  Cited by: [Figure D.1](https://arxiv.org/html/2602.04791v1#A4.F1 "In Appendix D A Divide-and-Conquer Version of In-Processing ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [Figure 2](https://arxiv.org/html/2602.04791v1#S3.F2 "In 3.2 Types of processing for incorporating fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.2](https://arxiv.org/html/2602.04791v1#S3.SS2.p3.10 "3.2 Types of processing for incorporating fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [Figure 4](https://arxiv.org/html/2602.04791v1#S6.F4 "In 6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§6.3](https://arxiv.org/html/2602.04791v1#S6.SS3.p1.1 "6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§6.3](https://arxiv.org/html/2602.04791v1#S6.SS3.p5.2 "6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§7](https://arxiv.org/html/2602.04791v1#S7.p1.1 "7 Discussion and Conclusion ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* Colorado General Assembly (2021)
  Restrict insurers’ use of external consumer data.
  Senate Bill (SB) 21-169
   Denver, CO.
  External Links: [Link](https://leg.colorado.gov/bills/sb21-169)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p5.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* O. Côté, M. Côté, and A. Charpentier (2025)
  A fair price to pay: exploiting causal graphs for fairness in insurance.
  Journal of Risk and Insurance 92 (1),  pp. 33–75.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/jori.12503),
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/jori.12503)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p2.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* C. Dwork, M. Hardt, T. Pitassi, O. Reingold, and R. Zemel (2012)
  Fairness through awareness.
  In Proceedings of the 3rd Innovations in Theoretical Computer Science Conference,
  ITCS ’12,  pp. 214–226.
  External Links: ISBN 9781450311151,
  [Link](https://doi.org/10.1145/2090236.2090255)
  Cited by: [§3.1](https://arxiv.org/html/2602.04791v1#S3.SS1.p3.1 "3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* J. H. Fong, O. S. Mitchell, and B. S. K. Koh (2015)
  Disaggregating activities of daily living limitations for predicting nursing home admission.
  Health Services Research 50 (2),  pp. 560–578.
  External Links: [Document](https://dx.doi.org/10.1111/1475-6773.12235)
  Cited by: [§5.1](https://arxiv.org/html/2602.04791v1#S5.SS1.p1.1 "5.1 Dataset construction from the HRS ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* L. J. Gabric, S. Zhou, and K. Q. Zhou (2024)
  A Bayesian approach to discrimination-free insurance pricing.
  Working Paper
   Arizona State University.
  External Links: [Link](https://papers.ssrn.com/abstract=4785927)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p1.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* V. Grari, A. Charpentier, S. Lamprier, and M. Detyniecki (2022)
  A fair pricing model via adversarial learning.
  Working Paper
  External Links: [Link](https://arxiv.org/pdf/2202.12008.pdf)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p2.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.1](https://arxiv.org/html/2602.04791v1#S3.SS1.p2.7 "3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* F. Hu, P. Ratz, and A. Charpentier (2024)
  A sequentially fair mechanism for multiple sensitive attributes.
  Proceedings of the AAAI Conference on Artificial Intelligence 38 (11),  pp. 12502–12510.
  External Links: ISSN 2374-3468,
  [Document](https://dx.doi.org/10.1609/aaai.v38i11.29143)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p2.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.1](https://arxiv.org/html/2602.04791v1#S3.SS1.p2.7 "3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* K. M. Langa, D. R. Weir, M. Kabeto, and A. Sonnega (2020)
  Langa-Weir classification of cognitive function (1995 onward).
  Survey Research Center
   Institute for Social Research, University of Michigan.
  External Links: [Link](https://hrsdata.isr.umich.edu/sites/default/files/documentation/data-descriptions/Data_Description_Langa_Weir_Classifications2016.pdf)
  Cited by: [§5.1](https://arxiv.org/html/2602.04791v1#S5.SS1.p2.1 "5.1 Dataset construction from the HRS ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* M. Lindholm, R. Richman, A. Tsanakas, and M. V. Wüthrich (2022)
  Discrimination-free insurance pricing.
  ASTIN Bulletin 52 (1),  pp. 55–89.
  External Links: ISSN 0515-0361, 1783-1350,
  [Document](https://dx.doi.org/10.1017/asb.2021.23)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p1.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.1](https://arxiv.org/html/2602.04791v1#S3.SS1.p4.11 "3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.1](https://arxiv.org/html/2602.04791v1#S3.SS1.p4.6 "3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.2](https://arxiv.org/html/2602.04791v1#S3.SS2.p4.5 "3.2 Types of processing for incorporating fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§5.3](https://arxiv.org/html/2602.04791v1#S5.SS3.p1.5 "5.3 Tailored post-processing for long-term insurance ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§5.4](https://arxiv.org/html/2602.04791v1#S5.SS4.p5.1 "5.4 Results and discussion ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§5](https://arxiv.org/html/2602.04791v1#S5.p2.1 "5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§6.1](https://arxiv.org/html/2602.04791v1#S6.SS1.p1.2 "6.1 General framework ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§6](https://arxiv.org/html/2602.04791v1#S6.p1.1 "6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§7](https://arxiv.org/html/2602.04791v1#S7.p1.1 "7 Discussion and Conclusion ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* M. Lindholm, R. Richman, A. Tsanakas, and M. V. Wüthrich (2024a)
  A multi-task network approach for calculating discrimination-free insurance prices.
  European Actuarial Journal 14 (2),  pp. 329–369.
  External Links: ISSN 2190-9741,
  [Document](https://dx.doi.org/10.1007/s13385-023-00367-z)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p1.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* M. Lindholm, R. Richman, A. Tsanakas, and M. V. Wüthrich (2024b)
  What is fair? Proxy discrimination vs. demographic disparities in insurance pricing.
  Scandinavian Actuarial Journal 2024 (9),  pp. 935–970.
  External Links: [Document](https://dx.doi.org/10.1080/03461238.2024.2364741),
  [Link](https://doi.org/10.1080/03461238.2024.2364741)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p2.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.1](https://arxiv.org/html/2602.04791v1#S3.SS1.p2.7 "3.1 Notions of fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.2](https://arxiv.org/html/2602.04791v1#S3.SS2.p2.4 "3.2 Types of processing for incorporating fairness ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§3.3](https://arxiv.org/html/2602.04791v1#S3.SS3.p2.1 "3.3 Challenges in adapting existing methodologies to long-term insurance ‣ 3 Fair Pricing Methodology ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§5.4](https://arxiv.org/html/2602.04791v1#S5.SS4.p5.1 "5.4 Results and discussion ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§6.2](https://arxiv.org/html/2602.04791v1#S6.SS2.p1.1 "6.2 Illustration 1: Pre-processing via optimal transport ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§6.2](https://arxiv.org/html/2602.04791v1#S6.SS2.p2.2 "6.2 Illustration 1: Pre-processing via optimal transport ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"),
  [§7](https://arxiv.org/html/2602.04791v1#S7.p1.1 "7 Discussion and Conclusion ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* New York State Department of Financial Services (2024)
  Use of artificial intelligence systems and external consumer data and information sources in insurance underwriting and pricing.
  Insurance Circular Letter No. 7
  External Links: [Link](https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p5.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* D. Pessach and E. Shmueli (2022)
  A review on fairness in machine learning.
  ACM Computing Surveys 55 (3),  pp. 51:1–51:44.
  External Links: ISSN 0360-0300,
  [Document](https://dx.doi.org/10.1145/3494672)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p2.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* A.E. Renshaw and S. Haberman (1995)
  On the graduations associated with a multiple state model for permanent health insurance.
  Insurance: Mathematics and Economics 17 (1),  pp. 1–17.
  External Links: ISSN 0167-6687,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/0167-6687%2895%2900011-G),
  [Link](https://www.sciencedirect.com/science/article/pii/016766879500011G)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p6.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* E. Sverdrup (1965)
  Estimates and test procedures in connection with stochastic models for deaths, recoveries and transfers between different states of health.
  Scandinavian Actuarial Journal 1965 (3-4),  pp. 184–211.
  External Links: [Document](https://dx.doi.org/10.1080/03461238.1965.10405687)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p6.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* Q. Wang, K. Hanewald, and X. Wang (2022)
  Multistate health transition modeling using neural networks.
  Journal of Risk and Insurance 89 (2),  pp. 475–504.
  External Links: ISSN 1539-6975,
  [Document](https://dx.doi.org/10.1111/jori.12364)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p6.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").
* X. Xin and F. Huang (2024)
  Antidiscrimination insurance pricing: Regulations, fairness criteria, and models.
  North American Actuarial Journal 28 (2),  pp. 285–319.
  External Links: ISSN 1092-0277,
  [Document](https://dx.doi.org/10.1080/10920277.2023.2190528)
  Cited by: [§1](https://arxiv.org/html/2602.04791v1#S1.p2.1 "1 Introduction ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

## Appendix A Transforming transition data to support the unified framework

We describe the procedure for transforming the transition data in Section [5.1](https://arxiv.org/html/2602.04791v1#S5.SS1 "5.1 Dataset construction from the HRS ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework") to support the Poisson regressions required by the unified framework of Section [4](https://arxiv.org/html/2602.04791v1#S4 "4 A Unified Framework for Multi-state Modeling ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

Table A.1: Snippet of the transition dataset prior to any transformations.

| Initial state | Ending state | Starting age | Ending age | Exposure |
| --- | --- | --- | --- | --- |
| Healthy | Disabled | 70.5 | 71.9 | 1.4 |
| Disabled | Dead | 71.9 | 73.8 | 1.9 |

Consider two rows from the transition dataset prior to any transformations, as shown in Table [A.1](https://arxiv.org/html/2602.04791v1#A1.T1 "Table A.1 ‣ Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"). Recall from our LTCI multi-state model that the type of transitions to which an insured is exposed depends on the insured’s initial health state: disability and healthy mortality (transitions 1 and 3, respectively) can occur only for healthy insureds, whereas recovery and disabled mortality (transitions 2 and 4, respectively) can occur only for disabled insureds. Our unified framework requires the creation of additional rows to indicate exposure to a given transition, and an event indicator to indicate whether the transition actually occurred. This transformation is illustrated in Table [A.2](https://arxiv.org/html/2602.04791v1#A1.T2 "Table A.2 ‣ Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

Table A.2: Snippet of the transition dataset after transformation to indicate exposure, corresponding to the data shown in Table [A.1](https://arxiv.org/html/2602.04791v1#A1.T1 "Table A.1 ‣ Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

| Transition | Starting age | Ending age | Event | Exposure |
| --- | --- | --- | --- | --- |
| 1. Healthy →\to Disabled | 70.5 | 71.9 | 1 | 1.4 |
| 3. Healthy →\to Dead | 70.5 | 71.9 | 0 | 1.4 |
| 2. Disabled →\to Healthy | 71.9 | 73.8 | 0 | 1.9 |
| 4. Disabled →\to Dead | 71.9 | 73.8 | 1 | 1.9 |

The columns of transition type, event indicator, and exposure would be sufficient if transition rates were independent of age. However, we model transition rates as functions of age through the insured’s age last birthday. Hence, coherent estimation of the transition rates using our proposed Poisson regression approach requires the age last birthday to remain constant within each row. We therefore create additional rows to split the observed period into time intervals over which this condition holds. For periods in which a transition occurs at the end of the observation window, the event indicator is assigned to the final interval, with all preceding intervals indicating no event, as illustrated in Table [A.3](https://arxiv.org/html/2602.04791v1#A1.T3 "Table A.3 ‣ Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

Table A.3: Snippet of the transition dataset after further transformation to ensure a constant age at last birthday for each row, following the transformation shown in Table [A.2](https://arxiv.org/html/2602.04791v1#A1.T2 "Table A.2 ‣ Appendix A Transforming transition data to support the unified framework ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

| Transition | Starting age | Ending age | Age | Event | Exposure |
| --- | --- | --- | --- | --- | --- |
| 1. Healthy →\to Disabled | 70.5 | 71.0 | 70 | 0 | 0.5 |
| 1. Healthy →\to Disabled | 71.0 | 71.9 | 71 | 1 | 0.9 |
| 3. Healthy →\to Dead | 70.5 | 71.0 | 70 | 0 | 0.5 |
| 3. Healthy →\to Dead | 71.0 | 71.9 | 71 | 0 | 0.9 |
| 2. Disabled →\to Healthy | 71.9 | 72.0 | 71 | 0 | 0.1 |
| 2. Disabled →\to Healthy | 72.0 | 73.0 | 72 | 0 | 1.0 |
| 2. Disabled →\to Healthy | 73.0 | 73.8 | 73 | 0 | 0.8 |
| 4. Disabled →\to Dead | 71.9 | 72.0 | 71 | 0 | 0.1 |
| 4. Disabled →\to Dead | 72.0 | 73.0 | 72 | 0 | 1.0 |
| 4. Disabled →\to Dead | 73.0 | 73.8 | 73 | 1 | 0.8 |

Once the transition dataset is restructured, the columns of starting age and ending age are no longer needed and can be discarded. The final step is to merge the covariate dataset with the restructured transition dataset. We first remove entries in the restructured dataset corresponding to individuals excluded during the covariate data cleaning process. The two datasets are merged using individual identifiers, with the relevant covariate information appended to each corresponding row.

The merged dataset is ready for the estimation of transition rates. Estimation for each transition type uses only the subset of observations corresponding to that transition; accordingly, the combined dataset is partitioned by transition type before being fed into the Poisson regression code.

## Appendix B Model Selection for Illustrative GLM Model

To obtain a parsimonious GLM model for our case study in Section [5.2](https://arxiv.org/html/2602.04791v1#S5.SS2 "5.2 LTCI pricing under different settings ‣ 5 Case Study: Fair Pricing for LTCI ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), we make the following changes:

* •

  Marital status is consolidated into five categories: Married, Separated, Partnered, Widowed, Never.
* •

  Years of education is grouped into the eight categories: did not complete elementary school (0-5 years), completed elementary but not middle school (6-7 years), completed middle school (8 years), some high school (9-11 years), completed high school (12 years), some college (13-15 years), completed college (16 years), and postgraduate (17+ years).
* •

  Observations with census region coded as 5 are removed due to their scarcity (17 out of approximately 30,000 records), and because the U.S. Census Bureau defines only four census regions: Northeast, Midwest, South, and West.

In addition, we apply log-transformations to the financial variables to address their skewness. In particular, total household income is transformed using ln⁡(1+x)\ln(1+x) before inclusion as a covariate. The treatment of total non-housing wealth is more complicated, as this variable can take negative values and therefore cannot be log-transformed directly. Letting WW denote the wealth, we find that the transformation ln⁡(1+|W|)\ln(1+|W|) gives an approximately normal distribution. To capture both the magnitude and sign of wealth, we include three covariates: ln⁡(1+|W|)\ln(1+|W|), sgn⁡(W)\operatorname{sgn}(W), and the interaction term sgn⁡(W)⋅ln⁡(1+|W|)\operatorname{sgn}(W)\cdot\ln(1+|W|).

## Appendix C Likelihood Contributions of Fitted Covariates

We measure the importance of each fitted covariate by the increase in likelihood it contributes to the model. Each contribution represents the additional likelihood gained by including that covariate after all other covariates have already been accounted for. The results are shown in Table [C.1](https://arxiv.org/html/2602.04791v1#A3.T1 "Table C.1 ‣ Appendix C Likelihood Contributions of Fitted Covariates ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

Table C.1: Likelihood contributions for each of the covariates in the fitted GLMs.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Transition | | | |  |
| Covariate | H→FH\to F | F→HF\to H | H→DH\to D | F→DF\to D | Total |
| Demographic factors | | | | | |
| Age | 2,360.23 | 1,587.60 | 2,031.35 | 2,498.03 | 8,477.21 |
| Years of education | 1,112.97 | 347.81 | 10.38 | 63.10 | 1,534.26 |
| Race | 695.94 | 40.99 | 1.79 | 21.12 | 759.84 |
| Labor force participation | 170.40 | 104.89 | 38.16 | 63.31 | 376.76 |
| Gender | 115.30 | 0.18 | 140.09 | 68.62 | 324.19 |
| Marital status | 30.80 | 37.62 | 38.12 | 15.44 | 121.98 |
| Ethnicity | 15.91 | 3.87 | 35.08 | 20.94 | 75.80 |
| Census region | 41.74 | 3.03 | 11.87 | 2.69 | 59.33 |
| Number of household residents | 0.22 | 2.31 | 1.91 | 0.29 | 4.73 |
| Health and disease factors | | | | | |
| Self-rated health | 228.09 | 108.44 | 282.31 | 98.38 | 717.22 |
| Ever had diabetes | 23.13 | 27.14 | 95.10 | 159.14 | 304.51 |
| Ever smoked cigarettes | 11.43 | 0.73 | 156.55 | 78.27 | 246.98 |
| Ever had lung disease | 0.50 | 0.13 | 131.57 | 80.02 | 212.22 |
| Ever drinks any alcohol | 29.83 | 28.94 | 10.49 | 10.57 | 147.57 |
| Ever had stroke | 32.92 | 56.89 | 9.73 | 33.94 | 133.48 |
| Ever had heart problems | 4.22 | 0.41 | 46.44 | 52.83 | 103.90 |
| BMI | 0.26 | 8.28 | 13.68 | 33.29 | 55.51 |
| Financial variables | | | | | |
| Non-housing wealth | 248.22 | 42.43 | 45.79 | 9.49 | 345.93 |
| Household income | 17.57 | 0.27 | 0.81 | 0.17 | 18.82 |

* Note: HH stands for healthy, FF for (functionally) disabled, and DD for dead. Likelihood contributions are measured conditional on all other terms being included in the model. Variables are ordered by category, and in decreasing order of total likelihood contributions.

Across all categories of factors, the four most important factors—each with a total likelihood contribution exceeding 500—are age, years of education, race, and self-rated health, in decreasing order of importance. Age is by far the most important factor, with likelihood contributions far exceeding any other variable across all four transitions. This clearly establishes the primary role of age in driving transition rates. Years of education and race follow in importance, primarily influencing transitions through their effects on disability transition rates. Self-rated health ranks fourth, with a more evenly distributed likelihood contribution across all four transitions.

The importance of race is particularly notable given its role as the sensitive attribute of interest. The variable remains highly important despite controlling for various socioeconomic, health, and behavioral factors through the inclusion of other covariates. While race itself is unlikely to have any intrinsic effect on the transition rates, it may act as a proxy for other socioeconomic or health indicators not fully captured by the variables already included.

## Appendix D A Divide-and-Conquer Version of In-Processing

We describe a divide-and-conquer variant of the procedure presented in Section [6.3](https://arxiv.org/html/2602.04791v1#S6.SS3 "6.3 Illustration 2: In-processing via adversarial debiasing ‣ 6 A Fair Pricing Framework for Long-Term Insurance ‣ Fair Pricing in Long-Term Insurance: A Unified Framework"), with the corresponding architecture illustrated in Figure [D.1](https://arxiv.org/html/2602.04791v1#A4.F1 "Figure D.1 ‣ Appendix D A Divide-and-Conquer Version of In-Processing ‣ Fair Pricing in Long-Term Insurance: A Unified Framework").

𝐙,x\operatorname{\mathbf{Z}},x𝐙\operatorname{\mathbf{Z}}xxEncoder fm​(𝐙)f\_{m}(\mathbf{Z})WmW\_{m}Wm,xW\_{m},xRegressor gm​(Wm,x)g\_{m}(W\_{m},x)YYAdversaryhm​(Wm)h\_{m}(W\_{m})SS


Figure D.1: A version of the adversarial learning framework tailored to long-term insurance, adapted from Beutel et al. ([2017](https://arxiv.org/html/2602.04791v1#bib.bib26 "Data decisions and theoretical implications when adversarially learning fair representations")) using the divide-and-conquer approach, shown for transition mm. Note: 𝐙\mathbf{Z} and xx refer to the non-age covariates and age, respectively; Wm=fm​(𝐙)W\_{m}=f\_{m}(\mathbf{Z}) is the trained representation, and functions fmf\_{m}, gmg\_{m} and hmh\_{m} are functions learned by the network.

Repeat the following precedure for m=1,2,…,Mm=1,2,\ldots,M:

1. 1.

   Begin with the sample of observed policies, with 𝐳k\mathbf{z}\_{k}, xu,kx\_{u,k}, and sks\_{k} respectively denoting the vector of covariates, the age at entry, and the sensitive attribute associated with the kkth insured.
2. 2.

   Let wk,m=fm​(𝐳k)w\_{k,m}=f\_{m}(\mathbf{z}\_{k}). Using cross-entropy loss LSL\_{S}, form the mthm^{\text{th}} adversary loss

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝐿𝑜𝑠𝑠A​d​v,m\displaystyle\mathit{Loss}\_{Adv,m} | =1n​∑k=1nLS​(sk,hm​(wk,m)).\displaystyle=\frac{1}{n}\sum\_{k=1}^{n}L\_{S}(s\_{k},h\_{m}(w\_{k,m})). |  |
3. 3.

   Construct the dataset corresponding to transition mm. Let (k,m,j)(k,m,j) index the jjth entry for the kkth insured and the mmth transition, with nk,mn\_{k,m} denoting the number of entries and nm=∑k=1nnk,mn\_{m}=\sum\_{k=1}^{n}n\_{k,m}. Using the Poisson likelihood loss LYL\_{Y}, form the prediction loss for the mmth transition

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝐿𝑜𝑠𝑠P​r​e​d,m\displaystyle\mathit{Loss}\_{Pred,m} | =1nm​∑k=1n∑j=1nk,mLY​(Yk,m,j,gm​(wk,m,xk,m,j)).\displaystyle=\frac{1}{n\_{m}}\sum\_{k=1}^{n}\sum\_{j=1}^{n\_{k,m}}L\_{Y}(Y\_{k,m,j},g\_{m}(w\_{k,m},x\_{k,m,j})). |  |
4. 4.

   Form the total loss for transition mm

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | 𝐿𝑜𝑠𝑠m\displaystyle\mathit{Loss\_{m}} | =𝐿𝑜𝑠𝑠P​r​e​d,m−α​𝐿𝑜𝑠𝑠A​d​v,m.\displaystyle=\mathit{Loss}\_{Pred,m}-\alpha\mathit{Loss}\_{Adv,m}. |  | (7) |
5. 5.

   Alternate between gradient steps to maximize Equation ([7](https://arxiv.org/html/2602.04791v1#A4.E7 "In item 4 ‣ Appendix D A Divide-and-Conquer Version of In-Processing ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")) with respect to hmh\_{m}, and to minimize Equation ([7](https://arxiv.org/html/2602.04791v1#A4.E7 "In item 4 ‣ Appendix D A Divide-and-Conquer Version of In-Processing ‣ Fair Pricing in Long-Term Insurance: A Unified Framework")) with respect to (fm,gm)(f\_{m},g\_{m}), until convergence.
6. 6.

   Calculate the price for the kkth insured, P​(𝐳k,xu,k)P(\mathbf{z}\_{k},{x\_{u,k}}), using λ^m​(𝐳,x)=gm​(fm​(𝐳),x)\hat{\lambda}\_{m}(\mathbf{z},x)=g\_{m}(f\_{m}(\mathbf{z}),x).

The procedure ensures that demographic parity for the prices in the sense that P​(𝐳k,x∗)P(\mathbf{z}\_{k},x^{\*}) is independent of sks\_{k}, for each fixed x∗x^{\*}.