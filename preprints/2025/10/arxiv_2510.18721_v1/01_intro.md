---
authors:
- Lydia J. Gabric
- Kenneth Q. Zhou
doc_id: arxiv:2510.18721v1
family_id: arxiv:2510.18721
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2510.18721v1
url_html: https://arxiv.org/html/2510.18721v1
venue: arXiv q-fin
version: 1
year: 2025
---

A Natural Hedging Framework for Longevity Risk with Graphical Risk Assessment

Lydia J. Gabrica and Kenneth Q. Zhoub,111Corresponding author. E-mail: kenneth.zhou@uwaterloo.ca

aSchool of Mathematical and Statistical Sciences, Arizona State University, USA

bDepartment of Statistics and Actuarial Science, University of Waterloo, Canada

Abstract: Natural hedging allows life insurers to manage longevity risk internally by offsetting the opposite exposures of life insurance and annuity liabilities. Although many studies have proposed natural hedging strategies under different settings, calibration methods, and mortality models, a unified framework for constructing and evaluating such hedges remains undeveloped. While graphical risk assessment has been explored for index-based longevity hedges, no comparable metric exists for natural hedging. This paper proposes a structured natural hedging framework paired with a graphical risk metric for hedge evaluation. The framework integrates valuation, calibration, and evaluation, while the graphical metric provides intuitive insights into residual dependencies and hedge performance. Applied to multiple hedging scenarios, the proposed methods demonstrate flexibility, interpretability, and practical value for longevity risk management.

Keywords: Natural hedging; Longevity risk; Stochastic mortality models; Graphical risk metric; Hedge effectiveness

## 1 Introduction

The uncertainty surrounding future mortality trends, known as longevity risk, has been extensively studied in the context of life insurance valuation and risk management. In general, there are two categories of longevity risk management solutions: internal and external. External solutions transfer longevity risk from life insurers to capital market investors through index-based hedging instruments and standardised contracts. Internal solutions, in contrast, utilize the insurer’s own portfolio structure to mitigate longevity and mortality risks. Among these, natural hedging has received considerable attention for its intuitive mechanism of balancing opposite exposures within life insurance and annuity portfolios.

The seminal work of Cox and Lin, ([2007](https://arxiv.org/html/2510.18721v1#bib.bib7)) introduced the concept of natural hedging by leveraging the inverse relationship between life insurance and annuity products to diversify mortality and longevity risks. When mortality changes, the values of life insurance and annuity liabilities typically move in opposite directions, allowing the insurer to offset these changes and reduce overall risk exposure. Since Cox and Lin, ([2007](https://arxiv.org/html/2510.18721v1#bib.bib7)), numerous studies have explored how this relationship can be more effectively utilized and implemented in different settings to manage mortality and longevity risks.

For instance, Lin and Tsai, ([2014](https://arxiv.org/html/2510.18721v1#bib.bib17)) proposed an immunization-based approach to construct natural hedges using sensitivity measures. Zhu and Bauer, ([2014](https://arxiv.org/html/2510.18721v1#bib.bib30)) explored a non-parametric mortality model and found that natural hedging performance may be less effective compared with parametric models. More recently, Yang et al., ([2019](https://arxiv.org/html/2510.18721v1#bib.bib27)) combined internal natural hedges with external index-based hedges under a unified framework. Chen et al., ([2024](https://arxiv.org/html/2510.18721v1#bib.bib5)) analysed product demand and supply considerations in natural hedging, while Cupido et al., ([2024](https://arxiv.org/html/2510.18721v1#bib.bib8)) studied the impact of spatial dependence on hedge performance. These studies collectively demonstrate the growing importance of natural hedging in longevity risk management.

Despite the aforementioned advancements, several challenges remain in constructing natural hedging effectively. First, identifying appropriate life insurance products to offset the mortality risk of annuity products can be complex. Second, determining the optimal quantity of life insurance products to effectively hedge requires detailed mathematical calibration. Third, evaluating hedge effectiveness is complicated due to residual risks such as calibration risk, structural basis risk, and model risk. Although prior research has attempted to address aspects of these challenges, there is still no unified framework that allows the systematic construction, calibration, and comparison of natural hedges across different models and methods.

In addition, existing studies primarily rely on numerical risk measures to evaluate hedging performance, which may not fully capture the joint behaviour of liabilities and hedging instruments. This shortfall could understate the strength of the inverse relationship or the offsetting effects in natural hedging. To address these gaps, this paper develops a unified natural hedging framework that integrates both numerical and graphical evaluation methods. The framework provides a consistent process for valuation, calibration and evaluation, while the accompanying graphical risk metric offers visual insights into the resulting hedge performance. The contributions of this paper are threefold.

The first contribution of this paper is the development of a risk management framework specifically designed for natural hedging. While frameworks for constructing and evaluating external longevity hedges have been proposed in prior studies, such as the index-based hedging procedure of Coughlan et al., ([2011](https://arxiv.org/html/2510.18721v1#bib.bib6)) and the decomposition of hedge effectiveness in Cairns et al., ([2014](https://arxiv.org/html/2510.18721v1#bib.bib3)), a comparable framework dedicated to natural hedging has not been established. To fill this gap, we propose a three-step hedging framework that extends the structure of Cairns et al., ([2014](https://arxiv.org/html/2510.18721v1#bib.bib3)) and adapts it for natural hedging.

The proposed framework consists of three stages: valuation, calibration, and evaluation. In the first stage, we derive formulas for valuing life insurance and annuity products under a stochastic mortality setting. In the second stage, we consider multiple hedge calibration techniques categorized by their objectives, including variance minimisation, duration matching, and delta hedging. In the third stage, hedge evaluation combines risk measures with graphical tools to provide a comprehensive and interpretable assessment of hedging effectiveness. The integration of graphical evaluation within the framework leads to our second contribution.

The second contribution of this paper is the introduction of a graphical risk metric specifically tailored to natural hedging. Graphical tools have been explored in the context of standardised longevity hedging, such as the graphical basis risk metrics proposed by Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4)) and extended by Sherris et al., ([2020](https://arxiv.org/html/2510.18721v1#bib.bib23)), as well as in Blake et al., ([2008](https://arxiv.org/html/2510.18721v1#bib.bib1)), Dowd et al., ([2010](https://arxiv.org/html/2510.18721v1#bib.bib9)) and Li and Liu, ([2021](https://arxiv.org/html/2510.18721v1#bib.bib14)). Since no comparable metric has been developed for evaluating natural hedges, we propose a graphical risk metric that visualizes the relationship between life annuity and insurance portfolios, allowing for a direct and intuitive evaluation of hedge performance.

The proposed graphical risk metric is constructed using a series of joint prediction regions that represent potential hedge outcomes across multiple confidence levels. To facilitate practical application, we further develop an interpretation procedure that enables users to visually assess hedge effectiveness and compare alternative hedging strategies. Visual elements such as shaded regions and reference lines highlight deviations from expected outcomes and the degree of diversification effects. This graphical approach provides a transparent and intuitive means to diagnose whether hedging shortfalls arise from under-hedging, over-hedging, or a lack of hedging effect.

The third contribution of this paper is the numerical implementation of the proposed natural hedging framework and graphical risk metric across three practical applications. First, we demonstrate how the framework can identify trade-offs when selecting an insurance portfolio as the hedging instrument. Second, we compare alternative calibration techniques to determine the optimal allocation of the hedging portfolio. Third, we evaluate model risk by comparing two stochastic mortality models and a non-parametric approach for a given portfolio configuration. The results from these illustrations show that the proposed framework and graphical risk metric together serve as a flexible and interpretable tool for constructing and evaluating natural hedges.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.18721v1#S2 "2 The Natural Hedging Framework") outlines the components of the natural hedging framework and demonstrates its use through a toy example. Section [3](https://arxiv.org/html/2510.18721v1#S3 "3 The Graphical Risk Metric") describes the construction and interpretation of the graphical risk metric. Section [4](https://arxiv.org/html/2510.18721v1#S4 "4 Numerical Illustrations") applies the framework and graphical metric to three practical illustrations. Finally, Section [5](https://arxiv.org/html/2510.18721v1#S5 "5 Conclusion") concludes the paper and discusses possible extensions and limitations.

## 2 The Natural Hedging Framework

Consider a life insurer issuing both life annuity and life insurance products. Let 𝒜\mathcal{A} and ℐ\mathcal{I} denote the present value random variables of the annuity and insurance portfolios, respectively. To hedge the longevity risk of 𝒜\mathcal{A}, the insurer employs a natural hedging strategy resulting in a hedged position

|  |  |  |
| --- | --- | --- |
|  | 𝒫​(h)=𝒜+ℒ​(h),\mathcal{P}(h)=\mathcal{A}+\mathcal{L}(h), |  |

where ℒ​(h)=h⋅ℐ\mathcal{L}(h)=h\cdot\mathcal{I} represent the calibrated life insurance portfolio and hh is the hedge ratio indicating the amount of ℐ\mathcal{I} needed for the hedged position.

To support a systematic implementation of such natural hedging, we develop a three-step framework in this section. We briefly summarise the three steps below:

1. 1.

   *Valuation of 𝒜\mathcal{A} and ℐ\mathcal{I}*: Derive the present value of the annuity and insurance liabilities, and obtain their expected values under stochastic mortality assumptions.
2. 2.

   *Calibration of hh*: Determine the hedge ratio that achieves a specified objective, such as variance minimization, duration matching, or delta neutral.
3. 3.

   *Evaluation of 𝒫​(h)\mathcal{P}(h)*: Assess the performance of the hedged portfolio through both numerical and graphical metrics, such as variance, Value-at-Risk, or histograms.

The rest of this section examines each step of the proposed framework in detail and concludes with a simple illustrative example.

### 2.1 Valuation

To construct a natural hedge, the insurer must first quantify the present value of the annuity and insurance liabilities. Under stochastic mortality modelling, these liabilities are random variables since their values depend on uncertain future survival outcomes. Thus, the first step of our natural hedging framework is to define and value these present value random variables as the foundation for establishing the hedge.

Let 𝒮x​(T)\mathcal{S}\_{x}(T) be the probability that an individual aged xx at time 0 will survive another TT years. This probability can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮x​(T)=∏s=1T(1−qx+s−1,s),\mathcal{S}\_{x}(T)=\prod\_{s=1}^{T}(1-q\_{x+s-1,s}), |  | (1) |

where qx,sq\_{x,s} is the probability that an individual aged xx at the beginning of year ss dies during year ss. In a stochastic setting, 𝒮x​(T)\mathcal{S}\_{x}(T) is a random variable since qx,sq\_{x,s}, for s=1,…,Ts=1,\ldots,T, is uncertain due to random mortality fluctuations. We denote its expectation by Sx​(T):=𝔼​[𝒮x​(T)]S\_{x}(T):=\mathbb{E}[\mathcal{S}\_{x}(T)]. The procedure for generating realisations of 𝒮x​(T)\mathcal{S}\_{x}(T) is provided in Appendix [B](https://arxiv.org/html/2510.18721v1#A2 "Appendix B Mortality Scenario Generator").

#### 2.1.1 Annuity liabilities

Recall that we denote 𝒜\mathcal{A} as the present value random variable of the annuity portfolio. If the insurer has nAn\_{A} distinct annuity products in the portfolio and applies a constant force of interest δ\delta, then 𝒜\mathcal{A} is given by

|  |  |  |
| --- | --- | --- |
|  | 𝒜=∑j=1nAωjA​∑k=τjτj+tj−1cj⋅e−δ​k⋅𝒮xj​(k),\mathcal{A}=\sum\_{j=1}^{n\_{A}}\omega\_{j}^{A}\sum\_{k=\tau\_{j}}^{\tau\_{j}+t\_{j}-1}c\_{j}\cdot e^{-\delta k}\cdot\mathcal{S}\_{x\_{j}}(k), |  |

where ωjA\omega\_{j}^{A} is the weight of the jj-th annuity product, τj\tau\_{j} is its deferral period, tjt\_{j} is the number of payments, cjc\_{j} is the payment size, and xjx\_{j} is the issuing age. The weights satisfy ∑j=1nAωjA=1\sum\_{j=1}^{n\_{A}}\omega\_{j}^{A}=1 and 0<ωjA≤10<\omega\_{j}^{A}\leq 1 for all jj.

It follows that the expectation of 𝒜\mathcal{A} represents the expected present value of the entire annuity portfolio liabilities, which can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | A:=𝔼​[𝒜]=∑j=1nAωjA​∑k=τjτj+tj−1cj⋅e−δ​k⋅Sxj​(k).A:=\mathbb{E}\left[\mathcal{A}\right]=\sum\_{j=1}^{n\_{A}}\omega\_{j}^{A}\sum\_{k=\tau\_{j}}^{\tau\_{j}+t\_{j}-1}c\_{j}\cdot e^{-\delta k}\cdot S\_{x\_{j}}(k). |  | (2) |

The distribution of 𝒜\mathcal{A} and the value of AA can be obtained using Monte Carlo simulations under stochastic mortality modelling.

#### 2.1.2 Insurance liabilities

Recall again that we denote ℐ\mathcal{I} as the present value random variable of the insurance portfolio. If the insurer has nIn\_{I} distinct insurance products in the portfolio and applies a constant force of interest δ\delta, then ℐ\mathcal{I} is given by

|  |  |  |
| --- | --- | --- |
|  | ℐ=∑j=1nIωjI​∑k=0tj−1bj⋅e−δ​(k+1)⋅(𝒮xj​(k)−𝒮xj​(k+1)),\mathcal{I}=\sum\_{j=1}^{n\_{I}}\omega\_{j}^{I}\sum\_{k=0}^{t\_{j}-1}b\_{j}\cdot e^{-\delta(k+1)}\cdot\left(\mathcal{S}\_{x\_{j}}(k)-\mathcal{S}\_{x\_{j}}(k+1)\right), |  |

where ωjI\omega\_{j}^{I} is the weight of the jj-th insurance product, tjt\_{j} is its term length, bjb\_{j} is the benefit amount, and xjx\_{j} is the issuing age. The weights again satisfy ∑j=1nIωjI=1\sum\_{j=1}^{n\_{I}}\omega\_{j}^{I}=1 and 0<ωjI≤10<\omega\_{j}^{I}\leq 1 for all jj.

Similar to the annuity liabilities, the expectation of ℐ\mathcal{I} is the expected present value of the entire insurance portfolio liabilities, which can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | I:=𝔼​[ℐ]=∑j=1nIωjI​∑k=0tj−1bj⋅e−δ​(k+1)⋅(Sxj​(k)−Sxj​(k+1)).I:=\mathbb{E}[\mathcal{I}]=\sum\_{j=1}^{n\_{I}}\omega\_{j}^{I}\sum\_{k=0}^{t\_{j}-1}b\_{j}\cdot e^{-\delta(k+1)}\cdot\left(S\_{x\_{j}}(k)-S\_{x\_{j}}(k+1)\right). |  | (3) |

The distribution of ℐ\mathcal{I} and the value of II also can be obtained using Monte Carlo simulations under stochastic mortality modelling.

#### 2.1.3 Summary of notations

Having derived the annuity and insurance portfolios, we now summarise the notations before presenting the next two steps of the framework. The hedge ratio is hh, the calibrated insurance portfolio is ℒ​(h)=h⋅ℐ\mathcal{L}(h)=h\cdot\mathcal{I} with its expected present value being L​(h)=h⋅IL(h)=h\cdot I, and the combined portfolio (i.e., the hedged position) is 𝒫​(h)=𝒜+ℒ​(h)\mathcal{P}(h)=\mathcal{A}+\mathcal{L}(h) with its expected present value being P​(h)=A+L​(h)P(h)=A+L(h). For ease of reference, Table [1](https://arxiv.org/html/2510.18721v1#S2.T1 "Table 1 ‣ 2.1.3 Summary of notations ‣ 2.1 Valuation ‣ 2 The Natural Hedging Framework") provides a summary of the notations introduced for the natural hedging framework.

| Description | Present Value (PV) | Expected PV | Mean-adjusted PV |
| --- | --- | --- | --- |
| Annuity portfolio | 𝒜\mathcal{A} | AA | 𝒜~=𝒜−A\tilde{\mathcal{A}}=\mathcal{A}-A |
| Insurance portfolio | ℐ\mathcal{I} | II | ℐ~=ℐ−I\tilde{\mathcal{I}}=\mathcal{I}-I |
| Calibrated portfolio | ℒ​(h)\mathcal{L}(h) | L​(h)L(h) | ℒ~​(h)=ℒ​(h)−L​(h)\tilde{\mathcal{L}}(h)=\mathcal{L}(h)-L(h) |
| Combined portfolio | 𝒫​(h)\mathcal{P}(h) | P​(h)P(h) | 𝒫~​(h)=𝒫​(h)−P​(h)\tilde{\mathcal{P}}(h)=\mathcal{P}(h)-P(h) |

Table 1: Summary of the notations used in the natural hedging framework.

### 2.2 Calibration

We now turn to the calibration step of the framework. The hedge ratio hh determines how the insurance liabilities offsets annuity liabilities, and calibrating hh is therefore a critical step that directly affects the effectiveness of the natural hedge. In this section, we categorize calibration methods into three groups: optimization, immunization, and Greek neutral. Before outlining a specific technique from each category to be implemented later in this paper, we briefly review the main approaches and related literature.

The first category is optimization, which calibrates hh by minimizing a chosen risk measure. Cupido et al., ([2024](https://arxiv.org/html/2510.18721v1#bib.bib8)) implemented a risk-minimization approach to construct a naturally hedged portfolio that accounts for spatial dependencies between different populations. Yang et al., ([2019](https://arxiv.org/html/2510.18721v1#bib.bib27)) proposed a unified hedging framework that minimizes changes in the insurer’s profit function for a portfolio combining internal natural hedges and external index-based hedges. Zhu and Bauer, ([2014](https://arxiv.org/html/2510.18721v1#bib.bib30)) applied a financial hedging approach to minimize economic capital, as originally introduced by Zhu and Bauer, ([2011](https://arxiv.org/html/2510.18721v1#bib.bib29)).

The next category is immunization, which seeks to minimize portfolio liability sensitivity to changes in mortality rates. Li and Luo, ([2012](https://arxiv.org/html/2510.18721v1#bib.bib15)) proposed a key q-Duration framework that matches sensitivities in mortality rates to hedge longevity risk with q-forward contracts. Tsai et al., ([2010](https://arxiv.org/html/2510.18721v1#bib.bib24)) introduced a conditional Value-at-Risk minimization approach that optimizes the insurer’s product mix and compared it with the modified duration matching method of Wang et al., ([2010](https://arxiv.org/html/2510.18721v1#bib.bib26)). Chen et al., ([2024](https://arxiv.org/html/2510.18721v1#bib.bib5)) generalized the approach of Tsai et al., ([2010](https://arxiv.org/html/2510.18721v1#bib.bib24)) to incorporate both insurance supply and demand, while Gatzert and Wesker, ([2014](https://arxiv.org/html/2510.18721v1#bib.bib11)) extended the method of Wang et al., ([2010](https://arxiv.org/html/2510.18721v1#bib.bib26)) to the entire insurance perspective, building on the framework of Gatzert and Wesker, ([2012](https://arxiv.org/html/2510.18721v1#bib.bib10)).

Lastly, Greek neutral techniques aim to reduce portfolio liabilities with respect to changes in model-specific mortality quantities. Cairns, ([2013](https://arxiv.org/html/2510.18721v1#bib.bib2)) introduced delta-nuga hedging as a robust approach to address recalibration risk in portfolios with index-based hedging instruments. Liu and Li, ([2017](https://arxiv.org/html/2510.18721v1#bib.bib18)) expanded the delta-nuga method of Cairns, ([2013](https://arxiv.org/html/2510.18721v1#bib.bib2)) through a generalized state-space hedging framework. To hedge changes in the reserves of a naturally hedged portfolio, Luciano et al., ([2017](https://arxiv.org/html/2510.18721v1#bib.bib20)) developed delta-gamma hedging based on first- and second-order approximations. Jevtić and Regis, ([2015](https://arxiv.org/html/2510.18721v1#bib.bib12)) applied this approach to assess the solvency of a naturally hedged portfolio from an asset-liability perspective.

We remark that the above review is not intended to be exhaustive but rather to provide context for the calibration step of the natural hedging framework. A simple benchmark is the uncalibrated hedge, where the hedge ratio is set to h=1h=1 and the insurer makes no adjustment to the insurance liabilities. Lastly, under a stochastic mortality model, the hedge ratio will need be calculated using Monte Carlo simulations. In the remainder of this section, we focus on one representative technique from each category, which will later be used in our numerical implementation.

#### 2.2.1 Optimization

The aim of optimization is to calibrate the hedge ratio hh by minimizing a chosen risk measure of the hedged position. Formally, this optimization problem can be written as

|  |  |  |
| --- | --- | --- |
|  | minh∈ℝ⁡ρ​(𝒫​(h)),\min\_{h\in\mathbb{R}}\rho(\mathcal{P}(h)), |  |

where ρ\rho denotes a selected risk measure and 𝒫​(h)=𝒜+h⋅ℐ\mathcal{P}(h)=\mathcal{A}+h\cdot\mathcal{I} is the hedged portfolio.

When ρ\rho is taken to be variance, the problem reduces to variance minimization, a well-established approach in longevity risk management. In this case, Cairns et al., ([2014](https://arxiv.org/html/2510.18721v1#bib.bib3)) showed that the optimal hedge ratio h(V​M)h^{(VM)} has a closed-form solution given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | h(V​M)=−Cov​(𝒜,ℐ)Var​(ℐ).h^{(VM)}=-\frac{\text{Cov}(\mathcal{A},\mathcal{I})}{\text{Var}(\mathcal{I})}. |  | (4) |

The corresponding hedged portfolio is denoted by 𝒫​(h(V​M))=𝒜+h(V​M)⋅ℐ\mathcal{P}(h^{(VM)})=\mathcal{A}+h^{(VM)}\cdot\mathcal{I}. This case will be used in the numerical illustrations later in the paper.

#### 2.2.2 Immunization

Immunization was originally introduced by Redington, ([1952](https://arxiv.org/html/2510.18721v1#bib.bib21)) for hedging interest rate risk. Wang et al., ([2010](https://arxiv.org/html/2510.18721v1#bib.bib26)) adapted it for natural hedging, where the goal is to neutralize the sensitivity of annuity and insurance liabilities to changes in mortality. The mortality duration of the combined portfolio P​(h)P(h) with respect to the force of mortality μ\mu is defined as

|  |  |  |
| --- | --- | --- |
|  | DμP=d​P​(h)d​μ=d​Ad​μ+d​L​(h)d​μ=d​Ad​μ+h​d​Id​μ.D^{P}\_{\mu}=\frac{dP(h)}{d\mu}=\frac{dA}{d\mu}+\frac{dL(h)}{d\mu}=\frac{dA}{d\mu}+h\frac{dI}{d\mu}. |  |

The optimal hedge ratio under this approach is obtained by setting DμP=0D^{P}\_{\mu}=0.

To approximate the mortality durations in DμPD^{P}\_{\mu}, we define the modified durations of the annuity and insurance portfolios as DμA=A+−A−2​ϵD^{A}\_{\mu}=\frac{A^{+}-A^{-}}{2\epsilon} and DμI=I+−I−2​ϵD^{I}\_{\mu}=\frac{I^{+}-I^{-}}{2\epsilon}, where ϵ\epsilon is a small constant, A±A^{\pm} and I±I^{\pm} are the expected present values of the annuity and insurance liabilities, respectively, evaluated under adjusted mortality μ±ϵ\mu\pm\epsilon. These quantities capture how much the expected present values change in response to a small shift in mortality. The resulting hedge ratio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | h(D​M)=−DμADμI.\displaystyle h^{(DM)}=-\frac{D^{A}\_{\mu}}{D^{I}\_{\mu}}. |  | (5) |

The corresponding hedged portfolio is P​(h(D​M))=A+h(D​M)​IP(h^{(DM)})=A+h^{(DM)}I. This portfolio matches the modified durations of the annuity and insurance portfolios, thereby aligning their sensitivities to mortality fluctuations.

#### 2.2.3 Greek neutral

Greek neutral methods extend the notion of Greeks to mortality and longevity hedging. Luciano et al., ([2012](https://arxiv.org/html/2510.18721v1#bib.bib19)) first introduced this idea, and Zhou and Li, ([2021](https://arxiv.org/html/2510.18721v1#bib.bib28)) further developed it for index-based longevity hedging, where the longevity delta was defined as a sensitivity measure with respect to the period effect of a stochastic mortality model. We now adapt this approach to natural hedging.

Consider the Lee-Carter (LC) model (Lee and Carter,, [1992](https://arxiv.org/html/2510.18721v1#bib.bib13)):

|  |  |  |
| --- | --- | --- |
|  | ln⁡(mx,t)=αx+βx​κt,\ln(m\_{x,t})=\alpha\_{x}+\beta\_{x}\kappa\_{t}, |  |

where mx,tm\_{x,t} is the central death rate for age xx in year tt, and αx\alpha\_{x}, βx\beta\_{x}, and κt\kappa\_{t} are the LC parameters, with κt\kappa\_{t} following a random walk with drift. The longevity delta measures the first-order sensitivity of the survival probability Sx​(T)S\_{x}(T) to changes in the current period effect κ0\kappa\_{0}, and is defined as Δx​(T):=∂Sx​(T)∂κ0\Delta\_{x}(T):=\frac{\partial S\_{x}(T)}{\partial\kappa\_{0}}. Assuming a constant force of mortality between integer ages, Zhou and Li, ([2021](https://arxiv.org/html/2510.18721v1#bib.bib28)) showed that Δx​(T)\Delta\_{x}(T) can be written as

|  |  |  |
| --- | --- | --- |
|  | Δx​(T)=−∑s=1Tβx+s−1​𝔼​[exp⁡(Yx​(s)−Zx​(T))],\Delta\_{x}(T)=-\sum\_{s=1}^{T}\beta\_{x+s-1}\,\mathbb{E}\!\left[\exp\!\left(Y\_{x}(s)-Z\_{x}(T)\right)\right], |  |

where Yx​(s)=αx+s−1+βx+s−1​κsY\_{x}(s)=\alpha\_{x+s-1}+\beta\_{x+s-1}\kappa\_{s} and Zx​(T)=∑s=1Texp⁡(Yx​(s))Z\_{x}(T)=\sum\_{s=1}^{T}\exp(Y\_{x}(s)), with Δx​(0)=0\Delta\_{x}(0)=0 since Sx​(0)=1S\_{x}(0)=1.

For the natural hedging framework, the longevity deltas of the annuity and insurance portfolios from Section [2.1](https://arxiv.org/html/2510.18721v1#S2.SS1 "2.1 Valuation ‣ 2 The Natural Hedging Framework") can then be derived as
ΔA=∑j=1nAωjA​∑k=τjτj+tjcj​e−δ​k​Δxj​(k)\Delta^{A}=\sum\_{j=1}^{n\_{A}}\omega\_{j}^{A}\sum\_{k=\tau\_{j}}^{\tau\_{j}+t\_{j}}c\_{j}e^{-\delta k}\Delta\_{x\_{j}}(k)
and
ΔI=∑j=1nIωjI​∑k=0tj−1bj​e−δ​(k+1)​(Δxj​(k)−Δxj​(k+1))\Delta^{I}=\sum\_{j=1}^{n\_{I}}\omega\_{j}^{I}\sum\_{k=0}^{t\_{j}-1}b\_{j}e^{-\delta(k+1)}\left(\Delta\_{x\_{j}}(k)-\Delta\_{x\_{j}}(k+1)\right).
A delta-neutral natural hedge would require ΔA+h​ΔI=0\Delta^{A}+h\Delta^{I}=0, and thus the hedge ratio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | h(D​N)=−ΔAΔI.\displaystyle h^{(DN)}=-\frac{\Delta^{A}}{\Delta^{I}}. |  | (6) |

The corresponding delta-neutral hedged portfolio is P​(h(D​N))=A+h(D​N)​IP(h^{(DN)})=A+h^{(DN)}I. Lastly, we note that longevity delta is model-dependent. While we have illustrated it under the LC model, the delta-neutral approach can be applied to other stochastic mortality models by deriving the corresponding longevity deltas.

### 2.3 Evaluation

The last step of the proposed natural hedging framework is evaluation. In this step, the insurer evaluates the effectiveness of a hedged position 𝒫​(h)\mathcal{P}(h) using both numerical and graphical assessment tools. We discuss both types of assessments in this subsection and consider them in the toy example shown in the next subsection.

A numerical risk measure for natural hedging can be defined in general as a mapping

|  |  |  |
| --- | --- | --- |
|  | ρ:𝒫​(h)↦ℝ,\rho:\mathcal{P}(h)\mapsto\mathbb{R}, |  |

which assigns a real-valued assessment to the hedged position 𝒫​(h)\mathcal{P}(h). A fundamental example is the portfolio variance, given by Var​(𝒫​(h))=Var​(𝒜)+h2​Var​(ℐ)+2​h​Cov​(𝒜,ℐ)\text{Var}(\mathcal{P}(h))=\text{Var}(\mathcal{A})+h^{2}\text{Var}(\mathcal{I})+2h\,\text{Cov}(\mathcal{A},\mathcal{I}). If the insurer focuses on downside risk, the Value-at-Risk (VaR) can be considered, defined as VaRα​(𝒫​(h))=inf{x∈ℝ:F𝒫​(h)​(x)≥α}\text{VaR}\_{\alpha}(\mathcal{P}(h))=\inf\{x\in\mathbb{R}:F\_{\mathcal{P}(h)}(x)\geq\alpha\} at confidence level α∈(0,1)\alpha\in(0,1), where F𝒫​(h)F\_{\mathcal{P}(h)} is the distribution function of 𝒫​(h)\mathcal{P}(h). A related measure is Expected Shortfall (ES), given by ESα​(𝒫​(h))=11−α​∫α1VaRu​(𝒫​(h))​𝑑u\text{ES}\_{\alpha}(\mathcal{P}(h))=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\text{VaR}\_{u}(\mathcal{P}(h))du, which captures the average loss in the tail beyond VaR. For a natural hedge, these numerical risk measures can provide complementary perspectives on the risk profile of the hedged position.

We make two remarks on numerical risk measures. First, beyond variance, VaR, and ES, other measures may also be considered, and they can be applied to transformations of the hedged position. For example, one may evaluate hedge effectiveness using VaRα​(𝒫~​(h))\text{VaR}\_{\alpha}(\tilde{\mathcal{P}}(h)), where 𝒫~​(h)\tilde{\mathcal{P}}(h) is the mean-adjusted hedged portfolio given in Table [1](https://arxiv.org/html/2510.18721v1#S2.T1 "Table 1 ‣ 2.1.3 Summary of notations ‣ 2.1 Valuation ‣ 2 The Natural Hedging Framework"). Second, we do not aim to identify a single numerical risk measure that is universally applicable to hedged portfolios. In optimization, the chosen objective is a natural candidate, but in immunization or Greek neutral approaches no obvious measure exists. In such cases, it is important to consider multiple numerical risk measures and complementary graphical assessments.

In conjunction with numerical measures, graphical risk metrics can further provide visual insights into the distribution of the hedged position. A common approach is to plot histograms of 𝒫​(h)\mathcal{P}(h) or 𝒫~​(h)\tilde{\mathcal{P}}(h), and overlay numerical risk measures such as VaR and ES. Other useful visualizations include empirical cumulative distribution functions, Q-Q plots, or kernel density estimates. While these graphical tools are widely used, they remain limited in the depth of analysis they provide. In Section [3](https://arxiv.org/html/2510.18721v1#S3 "3 The Graphical Risk Metric"), we extend beyond such standard methods and propose a new graphical risk metric tailored for natural hedging.

In summary, the last step of our framework incorporates both numerical and graphical risk assessments to evaluate hedged positions, aiming to provide a comprehensive view of their risk profile. However, relying solely on numerical measures can overlook important aspects of hedge performance, and simple graphical diagnostics may also be insufficient. To illustrate these issues, the next subsection presents a toy example that demonstrates the implementation of the proposed natural hedging framework and motivates the new graphical risk metric introduced in Section [3](https://arxiv.org/html/2510.18721v1#S3 "3 The Graphical Risk Metric").

### 2.4 Framework summary and toy example

We now summarise the proposed natural hedging framework and illustrate its implementation through a toy example. Table [2](https://arxiv.org/html/2510.18721v1#S2.T2 "Table 2 ‣ 2.4 Framework summary and toy example ‣ 2 The Natural Hedging Framework") provides a compact reference for the three steps of the framework. Under stochastic mortality modelling, each step requires future mortality projections. In practice, Monte Carlo simulations are used to compute present values in the valuation step, hedge ratios in the calibration step, and risk measures in the evaluation step. The mortality simulation methods need not be identical across steps, which in turn allows model uncertainty to present in the natural hedge. The mortality simulation methods considered in this paper are presented in Appendix [B](https://arxiv.org/html/2510.18721v1#A2 "Appendix B Mortality Scenario Generator").

| Step | Details |
| --- | --- |
| |  | | --- | | Step 1: | | Valuation | | |  | | --- | | Derive and calculate the present values of annuity and insurance liabilities to be included in the hedge. | |
| |  | | --- | | Step 2: | | Calibration | | |  | | --- | | Determine the hedge ratio, either set to 11 for an uncalibrated hedge or calculated under a chosen calibration method. | |
| |  | | --- | | Step 3: | | Evaluation | | |  | | --- | | Assess the resulting hedged positions using numerical risk measures and graphical risk assessment tools. | |
| |  | | --- | | Projected | | Mortality | | |  | | --- | | Mortality scenarios are required in each of the valuation, calibration, and evaluation steps. | |

Table 2: The proposed natural hedging framework.

To demonstrate the implementation of the proposed framework, we now present a toy example. Consider a life insurer with an annuity portfolio consisting of a single 20-year deferred 20-term life annuity issued to a 45-year-old individual, paying $20 annually at the beginning of each year after the deferral period. To hedge this liability, the insurer issues a 30-year term life insurance policy with a death benefit of $250, payable at the end of the year of death, to an individual aged either 40 or 50. For both issuing ages, the hedge ratio is set to h=1h=1, yielding two uncalibrated hedges. The interest rate is assumed to be i=4%i=4\% (or δ=ln⁡(1.04)\delta=\ln(1.04)).

Following the framework, Step 1 derives the present values of the annuity 𝒜\mathcal{A} and the two insurance portfolios ℐ1\mathcal{I}\_{1} and ℐ2\mathcal{I}\_{2} for ages 40 and 50, respectively. Step 2 constructs the calibrated insurance portfolios ℒ1​(1)=ℐ1\mathcal{L}\_{1}(1)=\mathcal{I}\_{1} and ℒ2​(1)=ℐ2\mathcal{L}\_{2}(1)=\mathcal{I}\_{2} by setting h1=h2=1h\_{1}=h\_{2}=1. Step 3 evaluates the hedged portfolios 𝒫1=𝒜+ℐ1\mathcal{P}\_{1}=\mathcal{A}+\mathcal{I}\_{1} and 𝒫2=𝒜+ℐ2\mathcal{P}\_{2}=\mathcal{A}+\mathcal{I}\_{2} using both numerical and graphical risk assessments. Mortality scenarios are generated using the bootstrapping method described in Appendix [B.2](https://arxiv.org/html/2510.18721v1#A2.SS2 "B.2 Model-free approach ‣ Appendix B Mortality Scenario Generator"), based on U.S. male mortality data (ages 40-99, years 1970-2018) obtained from the Human Mortality Database.222HMD. Human Mortality Database. Max Planck Institute for Demographic Research (Germany), University of California, Berkeley (USA), and French Institute for Demographic Studies (France). Available at www.mortality.org (data downloaded on 2 January 2024).

[Table 3](https://arxiv.org/html/2510.18721v1#S2.T3 "Table 3 ‣ 2.4 Framework summary and toy example ‣ 2 The Natural Hedging Framework") reports the mean, variance, VaR0.95\text{VaR}\_{0.95}, and the excess of VaR0.95\text{VaR}\_{0.95} over the mean for the annuity portfolio 𝒜\mathcal{A}, the two insurance portfolios ℒ1\mathcal{L}\_{1} and ℒ2\mathcal{L}\_{2}, and the combined hedged portfolios 𝒫1\mathcal{P}\_{1} and 𝒫2\mathcal{P}\_{2}. The variance is greatly reduced when either ℒ1\mathcal{L}\_{1} or ℒ2\mathcal{L}\_{2} is added to 𝒜\mathcal{A}, reflecting the hedging effect of combining portfolios. Between the two hedged portfolios, 𝒫2\mathcal{P}\_{2} has the smaller variance and excess VaR, while 𝒫1\mathcal{P}\_{1} achieves the lower mean and lower VaR. The mixed results underscore the complexity of assessing hedge effectiveness in natural hedging and motivate the need for further graphical risk assessments.

| Portfolio | Mean | Variance | VaR0.95\text{VaR}\_{0.95} | VaR0.95−Mean\text{VaR}\_{0.95}-\text{Mean} |
| --- | --- | --- | --- | --- |
| 𝒜\mathcal{A} | 98.81 | 1.61 | 100.84 | 2.03 |
| ℒ1\mathcal{L}\_{1} | 22.00 | 1.01 | 23.69 | 1.68 |
| ℒ2\mathcal{L}\_{2} | 43.52 | 2.67 | 46.27 | 2.75 |
| 𝒫1\mathcal{P}\_{1} | 120.81 | 0.39 | 121.83 | 1.01 |
| 𝒫2\mathcal{P}\_{2} | 142.33 | 0.27 | 143.19 | 0.86 |

Table 3: Numerical risk measures for the annuity portfolio 𝒜\mathcal{A}, the two insurance portfolios ℒ1\mathcal{L}\_{1} and ℒ2\mathcal{L}\_{2}, and the hedged portfolios 𝒫1\mathcal{P}\_{1} and 𝒫2\mathcal{P}\_{2}.

[Figure 1](https://arxiv.org/html/2510.18721v1#S2.F1 "Figure 1 ‣ 2.4 Framework summary and toy example ‣ 2 The Natural Hedging Framework") provides a graphical assessment of the hedged portfolios using histograms. Panel (a) shows the empirical distributions of 𝒫1\mathcal{P}\_{1} and 𝒫2\mathcal{P}\_{2}, with dashed lines indicating their VaR0.95\text{VaR}\_{0.95}. Consistent with the numerical results, 𝒫1\mathcal{P}\_{1} has a smaller VaR0.95\text{VaR}\_{0.95}, reflecting lower liabilities compared to 𝒫2\mathcal{P}\_{2}. Panel (b) displays the empirical distributions of the mean-adjusted portfolios 𝒫~1\tilde{\mathcal{P}}\_{1} and 𝒫~2\tilde{\mathcal{P}}\_{2} (defined in Table [1](https://arxiv.org/html/2510.18721v1#S2.T1 "Table 1 ‣ 2.1.3 Summary of notations ‣ 2.1 Valuation ‣ 2 The Natural Hedging Framework")), again with dashed lines marking their VaR0.95\text{VaR}\_{0.95}. In this panel, 𝒫2\mathcal{P}\_{2} shows smaller deviations from its mean than 𝒫1\mathcal{P}\_{1}, confirming the lower variance observed in the numerical measures.

![Refer to caption](x1.png)


(a) Liabilities for each hedged portfolio with pink and blue dashed lines denoting the VaR0.95\text{VaR}\_{0.95} for 𝒫1\mathcal{P}\_{1} (pink) and 𝒫2\mathcal{P}\_{2} (blue), respectively.

![Refer to caption](x2.png)


(b) Mean-adjusted liabilities for each hedged portfolio with pink and blue dashed lines denoting the VaR0.95\text{VaR}\_{0.95} for 𝒫~1\tilde{\mathcal{P}}\_{1} and 𝒫~2\tilde{\mathcal{P}}\_{2}, respectively.

Figure 1: Graphical risk assessment for the hedged portfolios 𝒫1\mathcal{P}\_{1} (pink) and 𝒫2\mathcal{P}\_{2} (blue).

This toy example illustrates how different numerical and graphical risk assessments can lead to inconclusive results about hedge effectiveness. More importantly, such assessments cannot capture the underlying relationship between the annuity portfolio 𝒜\mathcal{A} and the insurance portfolio ℒ\mathcal{L} within the hedged position 𝒫\mathcal{P}. For example, when the realized liability of 𝒫\mathcal{P} exceeds its VaR0.95\text{VaR}\_{0.95}, it is unclear whether this outcome reflects weak offsetting effect between 𝒜\mathcal{A} and ℒ\mathcal{L}, or whether both portfolios simultaneously contribute to large losses. Answering such questions can help insurers to make more informed decisions in portfolio selection and in the design of natural hedges, which we address in Section [3](https://arxiv.org/html/2510.18721v1#S3 "3 The Graphical Risk Metric").

## 3 The Graphical Risk Metric

This section introduces a new graphical risk metric for natural hedging. The metric provides a deeper analysis of the hedged position by examining the joint distribution of the underlying annuity and insurance portfolios on a two-dimensional scale. In the following, we first describe how this graphical risk metric is constructed and then develop an interpretation procedure that enables an enhanced risk assessment of the hedged position. To illustrate the construction and interpretation, we continue to use the toy example outlined in Section [2.4](https://arxiv.org/html/2510.18721v1#S2.SS4 "2.4 Framework summary and toy example ‣ 2 The Natural Hedging Framework").

### 3.1 Constructing the metric

The construction of our graphical risk metric is inspired by the work of Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4)), who introduced a visual tool for evaluating population basis risk in index-based longevity hedges. A brief review of the original method by Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4)) is provided in Appendix [A.1](https://arxiv.org/html/2510.18721v1#A1.SS1 "A.1 Review of Chan et al., (2016) ‣ Appendix A Metric Construction"). We adapt this approach to the context of natural hedging and construct a two-dimensional assessment of the joint distribution of the underlying annuity and insurance portfolios, rather than focusing solely on the hedged position. This representation enables direct visualisation of the dependence structure between the annuity and insurance liabilities.

![Refer to caption](x3.png)


Figure 2: Graphical risk metric illustrating the joint distribution of the annuity portfolio 𝒜\mathcal{A} and the insurance portfolio ℒ1\mathcal{L}\_{1} for the hedged position 𝒫1\mathcal{P}\_{1} from the toy example.

Figure [2](https://arxiv.org/html/2510.18721v1#S3.F2 "Figure 2 ‣ 3.1 Constructing the metric ‣ 3 The Graphical Risk Metric") illustrates the result of applying the metric to the hedged position 𝒫1\mathcal{P}\_{1} from the toy example. Details on how this figure is constructed are provided in Appendix [A.2](https://arxiv.org/html/2510.18721v1#A1.SS2 "A.2 Construction of the graphical risk metric ‣ Appendix A Metric Construction"). The x- and y-axes represent the present values of the annuity portfolio 𝒜\mathcal{A} and the insurance portfolio ℒ1\mathcal{L}\_{1}, respectively. Each black dot corresponds to a realisation of (𝒜,ℒ1)(\mathcal{A},\mathcal{L}\_{1}), while the shaded pink regions denote joint prediction regions at different confidence levels. The figure reveals a clear inverse relationship between 𝒜\mathcal{A} and ℒ1\mathcal{L}\_{1}, forming a downward-sloping pattern in both the point cloud and the shaded regions.

The graphical risk metric illustrated in Figure [2](https://arxiv.org/html/2510.18721v1#S3.F2 "Figure 2 ‣ 3.1 Constructing the metric ‣ 3 The Graphical Risk Metric") enables a visual evaluation of the hedge effectiveness of a single portfolio. The same construction can be extended to compare multiple hedged portfolios, which is particularly useful when several hedging opportunities are available. Figure [3](https://arxiv.org/html/2510.18721v1#S3.F3 "Figure 3 ‣ 3.1 Constructing the metric ‣ 3 The Graphical Risk Metric") illustrates such an extension by jointly displaying the annuity portfolio 𝒜\mathcal{A} against two insurance portfolios, ℒ1\mathcal{L}\_{1} and ℒ2\mathcal{L}\_{2}, corresponding to the hedged positions 𝒫1\mathcal{P}\_{1} and 𝒫2\mathcal{P}\_{2} from the toy example. This extension allows for a direct comparison of alternative natural hedges under a single visual platform.

![Refer to caption](x4.png)


(a) Unadjusted

![Refer to caption](x5.png)


(b) Mean-adjusted

Figure 3: Graphical risk metric illustrating the effectiveness of the hedged positions 𝒫1\mathcal{P}\_{1} (pink) and 𝒫2\mathcal{P}\_{2} (blue) from the toy example.

Panel (a) of Figure [3](https://arxiv.org/html/2510.18721v1#S3.F3 "Figure 3 ‣ 3.1 Constructing the metric ‣ 3 The Graphical Risk Metric") plots the annuity portfolio 𝒜\mathcal{A} against the corresponding insurance portfolios ℒ1\mathcal{L}\_{1} and ℒ2\mathcal{L}\_{2}. Since the annuity is identical across both portfolios, the larger insurance liabilities of ℒ2\mathcal{L}\_{2} (relative to ℒ1\mathcal{L}\_{1}) result in higher total liabilities, consistent with the numerical measures reported in [Table 3](https://arxiv.org/html/2510.18721v1#S2.T3 "Table 3 ‣ 2.4 Framework summary and toy example ‣ 2 The Natural Hedging Framework"). This outcome is expected, as the life insurance policy from 𝒫2\mathcal{P}\_{2} is issued to a 50-year-old individual, whose higher mortality risk will lead to greater liabilities than the 40-year-old policy from 𝒫1\mathcal{P}\_{1}.

To enable a fairer comparison, Panel (b) of Figure [3](https://arxiv.org/html/2510.18721v1#S3.F3 "Figure 3 ‣ 3.1 Constructing the metric ‣ 3 The Graphical Risk Metric") presents the mean-adjusted annuity and insurance liabilities, represented by (𝒜~,ℒ~1)(\tilde{\mathcal{A}},\tilde{\mathcal{L}}\_{1}) and (𝒜~,ℒ~2)(\tilde{\mathcal{A}},\tilde{\mathcal{L}}\_{2}), whose joint prediction regions are centred at the origin. The solid black line with slope −1-1 represents the benchmark line, corresponding to scenarios in which deviations in the annuity and insurance liabilities perfectly offset (i.e., 𝒜~+ℒ~=0\tilde{\mathcal{A}}+\tilde{\mathcal{L}}=0), resulting in a “perfect” hedge. Building on this benchmark, we next introduce an interpretative procedure to analyse potential hedging outcomes based on the mean-adjusted portfolios.

### 3.2 Interpreting the metric

To gain a comprehensive visual understanding of the risk profile underlying a hedged position, we now develop an interpretation aid for the proposed graphical risk metric. This aid functions as a diagnostic tool for analysing the joint behaviour of the annuity and insurance portfolios. By representing all present value realisations in the (𝒜~,ℒ~)(\tilde{\mathcal{A}},\tilde{\mathcal{L}}) plane, it enables visual assessment of how effectively deviations in the insurance liability offset those in the annuity liability.

![Refer to caption](x6.png)


(a) Interpretation

![Refer to caption](x7.png)


(b) Application

Figure 4: Interpretation procedure for the proposed graphical risk metric and its application to the hedged positions 𝒫1\mathcal{P}\_{1} (pink) and 𝒫2\mathcal{P}\_{2} (blue) from the toy example.

Figure [4](https://arxiv.org/html/2510.18721v1#S3.F4 "Figure 4 ‣ 3.2 Interpreting the metric ‣ 3 The Graphical Risk Metric") illustrates our interpretation procedure. Panel (a) defines the shaded regions and benchmark lines used to classify hedging outcomes, where the shading corresponds to different types of hedging outcome and the dashed lines indicate the magnitude of deviation from a perfect hedge. To clarify the interpretation of these shaded regions, we provide brief explanations of the scenarios marked by Points A, B, C, and D in Figure [4(a)](https://arxiv.org/html/2510.18721v1#S3.F4.sf1 "In Figure 4 ‣ 3.2 Interpreting the metric ‣ 3 The Graphical Risk Metric"):

* •

  Point A: The annuity liability is $2 below its expected value, while the insurance liability is $2 above. The surplus in the insurance liability fully offsets the annuity shortfall, representing a perfectly hedged scenario. All points along the benchmark line correspond to this ideal outcome.
* •

  Point B: The annuity liability is $3 above its expectation, but the insurance liability is only $2 below. The shortfall in the insurance liability leaves a net liability surplus of $1 for the hedged position, corresponding to the case of *Not Enough Insurance Liabilities* (red region).
* •

  Point C: The annuity liability is $1 below its expected value, while the insurance liability is $2 above. The excess in the insurance liability leads to a net liability surplus of $1 for the hedged position, representing the case of *Too Much Insurance Liabilities* (blue region).
* •

  Point D: Both the annuity and insurance liabilities fall below their expectations, by $1 and $1.5 respectively. This scenario creates a combined liability deficit of $2.5, indicating the case of *No Hedging Effect* (grey region), where losses occur simultaneously in both portfolios.

The two dashed lines in Figure [4(a)](https://arxiv.org/html/2510.18721v1#S3.F4.sf1 "In Figure 4 ‣ 3.2 Interpreting the metric ‣ 3 The Graphical Risk Metric") represent equal magnitudes of deviation from the expected total liability, corresponding to either a surplus or a deficit of $1. Since Point D lies below the lower dashed line, it immediately means that it has a larger magnitude of deviation than Points B and C. Although Points B and C both have a surplus of $1, they arise from different causes; Point B has insufficient insurance liabilities, while Point C has excessive insurance liabilities. This distinction would not be apparent in a one-dimensional graphical assessment, such as a histogram. Figure [5](https://arxiv.org/html/2510.18721v1#S3.F5 "Figure 5 ‣ 3.2 Interpreting the metric ‣ 3 The Graphical Risk Metric") extends this idea by showing simulated realisations coloured by hedging outcome types.

![Refer to caption](x8.png)


(a) Hedged position 𝒫~1\tilde{\mathcal{P}}\_{1}

![Refer to caption](x9.png)


(b) Hedged position 𝒫~2\tilde{\mathcal{P}}\_{2}

Figure 5: Simulated outcomes of 𝒫~1\tilde{\mathcal{P}}\_{1} and 𝒫~2\tilde{\mathcal{P}}\_{2}, coloured by hedging outcome with the dashed line denoting the mean-adjusted VaR0.95\text{VaR}\_{0.95}.

Figure [5](https://arxiv.org/html/2510.18721v1#S3.F5 "Figure 5 ‣ 3.2 Interpreting the metric ‣ 3 The Graphical Risk Metric") presents 20,000 simulated realisations of (𝒜~,ℒ~1)(\tilde{\mathcal{A}},\tilde{\mathcal{L}}\_{1}) and (𝒜~,ℒ~2)(\tilde{\mathcal{A}},\tilde{\mathcal{L}}\_{2}) in Panels (a) and (b), respectively. Points are coloured by the type of hedging outcome. Pink and blue indicate *Too Much Insurance Liabilities*, leading to a surplus and deficit in total liability, respectively. Green and teal denote *Not Enough Insurance Liabilities*, leading to a deficit and surplus in total liability, respectively. Red and gold represent *No Hedging Effect*, where both the insurance and annuity portfolios deviate in the same direction. The dashed lines mark the mean-adjusted VaR0.95\text{VaR}\_{0.95} of the corresponding hedged positions. Any realisations above these lines exceed the respective VaR0.95\text{VaR}\_{0.95} values reported in [Table 3](https://arxiv.org/html/2510.18721v1#S2.T3 "Table 3 ‣ 2.4 Framework summary and toy example ‣ 2 The Natural Hedging Framework").

Comparing the simulated hedging outcomes in Figure [5](https://arxiv.org/html/2510.18721v1#S3.F5 "Figure 5 ‣ 3.2 Interpreting the metric ‣ 3 The Graphical Risk Metric"), 𝒫~1\tilde{\mathcal{P}}\_{1} shows more realisations associated with *Not Enough Insurance Liabilities* (green and teal) and *No Hedging Effect* (red and gold) than 𝒫~2\tilde{\mathcal{P}}\_{2}. Conversely, 𝒫~2\tilde{\mathcal{P}}\_{2} exhibits a higher frequency of *Too Much Insurance Liabilities* (pink and blue), indicating that its insurance exposure tends to overcompensate for annuity deviations. Among the outcomes that exceed the mean-adjusted VaR0.95\text{VaR}\_{0.95} as marked by the dashed lines, those from 𝒫~1\tilde{\mathcal{P}}\_{1} primarily arise from *Not Enough Insurance Liabilities* (teal) and *No Hedging Effect* (gold), while those from 𝒫~2\tilde{\mathcal{P}}\_{2} are mostly driven by *Too Much Insurance Liabilities* (pink).

We now return to Figure [4(b)](https://arxiv.org/html/2510.18721v1#S3.F4.sf2 "In Figure 4 ‣ 3.2 Interpreting the metric ‣ 3 The Graphical Risk Metric"), which applies the interpretation aid to compare 𝒫~1\tilde{\mathcal{P}}\_{1} and 𝒫~2\tilde{\mathcal{P}}\_{2} by overlaying their joint prediction regions. The dashed lines above and below the solid benchmark line represent equal magnitudes of surplus and deficit in the hedged position. It is clear that the joint prediction region of 𝒫~1\tilde{\mathcal{P}}\_{1} extends further into the area associated with *Not Enough Insurance Liabilities*, while 𝒫~2\tilde{\mathcal{P}}\_{2} covers more of the *Too Much Insurance Liabilities* area. More importantly, the joint prediction region of 𝒫~1\tilde{\mathcal{P}}\_{1} extends above the upper dashed line, indicating more severe (liability surplus) scenarios than that of 𝒫~2\tilde{\mathcal{P}}\_{2}.

In conclusion, the proposed graphical risk metric complements numerical evaluation by exposing the underlying hedging behaviour. Specifically, 𝒫2\mathcal{P}\_{2} achieves stronger offsets between annuity and insurance liabilities but is more prone to excess insurance exposure, whereas 𝒫1\mathcal{P}\_{1} faces greater downside risk from insufficient offsetting. These findings highlight how the graphical risk metric reveals important behavioural differences between hedged positions. In the next section, we apply this graphical framework to a broader set of numerical illustrations to further explore its practical use and interpretive value.

## 4 Numerical Illustrations

We now demonstrate how the natural hedging framework and the graphical risk metric can be applied to address practical natural hedging problems. Three illustrations are considered: (1) identifying the most effective insurance portfolio, (2) selecting the optimal hedge calibration technique, and (3) evaluating model risk arising from alternative mortality projections. Each illustration follows the same framework as in Section [2](https://arxiv.org/html/2510.18721v1#S2 "2 The Natural Hedging Framework") and employs the graphical risk metric developed in Section [3](https://arxiv.org/html/2510.18721v1#S3 "3 The Graphical Risk Metric"). Appendix [C](https://arxiv.org/html/2510.18721v1#A3 "Appendix C Numerical Illustration Details") provides the details of the annuity and insurance portfolios considered in this section.

### 4.1 Illustration 1: Insurance Portfolio Selection

Our first illustration investigates how to identify an effective insurance portfolio for natural hedging. Consider an insurer managing an annuity portfolio issued to individuals aged 40-60, with $10,000 annual payments starting at age 65. The insurer considers three candidate insurance portfolios, each providing a death benefit of $750,000 payable at the end of the year of death: (1) whole life policies issued to individuals aged 40-60 (ℐ1\mathcal{I}\_{1}), (2) whole life policies issued to individuals aged 40-49 (ℐ2\mathcal{I}\_{2}), and (3) 20-year term policies issued to individuals aged 40-49 (ℐ3\mathcal{I}\_{3}). The annual interest rate is assumed to be 4%, and the limiting age is set at 100. Table [4](https://arxiv.org/html/2510.18721v1#S4.T4 "Table 4 ‣ 4.1 Illustration 1: Insurance Portfolio Selection ‣ 4 Numerical Illustrations") summarises how the natural hedging framework is applied to this illustration. The three steps are applied consistently, with the only difference arising from the features of the insurance portfolios.

| Step | Details |
| --- | --- |
| |  | | --- | | Step 1: | | Valuation | | |  | | --- | | Derive the present values of the annuity portfolio (issuing ages 40-60, deferred to age 65, 35 annual payments of $10,000) and three candidate insurance portfolios with a $750,000 death benefit: ℐ1\mathcal{I}\_{1} (issuing ages 40-60, whole life), ℐ2\mathcal{I}\_{2} (issuing ages 40-49, whole life), and ℐ3\mathcal{I}\_{3} (issuing ages 40-49, 20-year term). | |
| |  | | --- | | Step 2: | | Calibration | | |  | | --- | | Calibrate hedge ratios h1h\_{1}, h2h\_{2}, and h3h\_{3} using the variance-minimisation method. | |
| |  | | --- | | Step 3: | | Evaluation | | |  | | --- | | Construct the hedged portfolios 𝒫1\mathcal{P}\_{1}, 𝒫2\mathcal{P}\_{2}, and 𝒫3\mathcal{P}\_{3}, and evaluate them comparatively using both numerical risk measures and the proposed graphical risk metric. | |
| |  | | --- | | Projected | | Mortality | | |  | | --- | | Mortality scenarios are generated using the bootstrapping method described in Appendix [B.2](https://arxiv.org/html/2510.18721v1#A2.SS2 "B.2 Model-free approach ‣ Appendix B Mortality Scenario Generator"), applied consistently across the valuation, calibration, and evaluation steps. | |

Table 4: Natural hedging framework applied to Illustration 1.

Table [5](https://arxiv.org/html/2510.18721v1#S4.T5 "Table 5 ‣ 4.1 Illustration 1: Insurance Portfolio Selection ‣ 4 Numerical Illustrations") reports the calibrated hedge ratios and numerical risk measures for the three hedged portfolios. Based on the variance and the mean-adjusted VaR0.95\text{VaR}\_{0.95}, 𝒫1\mathcal{P}\_{1} outperforms 𝒫2\mathcal{P}\_{2} and 𝒫3\mathcal{P}\_{3}, whereas the VaR0.95\text{VaR}\_{0.95} indicates that 𝒫3\mathcal{P}\_{3} performs best. To complement these numerical results and reveal the underlying hedging behaviour, Figure [6](https://arxiv.org/html/2510.18721v1#S4.F6 "Figure 6 ‣ 4.1 Illustration 1: Insurance Portfolio Selection ‣ 4 Numerical Illustrations") presents the graphical risk metric for the three hedged portfolios. In Panel (a), the unadjusted version shows that the three portfolios differ in the magnitude of their calibrated insurance liabilities, with 𝒫1\mathcal{P}\_{1} having the largest and 𝒫3\mathcal{P}\_{3} the smallest. The mean-adjusted version in Panel (b) shows that 𝒫~1\tilde{\mathcal{P}}\_{1} aligns most closely with the benchmark line, indicating stronger offsetting between annuity and insurance liabilities, 𝒫~2\tilde{\mathcal{P}}\_{2} exhibits greater variability with more outcomes falling into the *Not Enough Insurance Liabilities* and *Too Much Insurance Liabilities* regions, and 𝒫~3\tilde{\mathcal{P}}\_{3} displays the widest dispersion and more frequent *No Hedging Effect*.

| Portfolio | Hedge Ratio | Variance | VaR0.95\text{VaR}\_{0.95} | Mean-adjusted VaR0.95\text{VaR}\_{0.95} |
| --- | --- | --- | --- | --- |
| 𝒫1=𝒜+h1⋅ℐ1\mathcal{P}\_{1}=\mathcal{A}+h\_{1}\cdot\mathcal{I}\_{1} | 0.267 | 34,090 | 133,295 | 290 |
| 𝒫2=𝒜+h2⋅ℐ2\mathcal{P}\_{2}=\mathcal{A}+h\_{2}\cdot\mathcal{I}\_{2} | 0.275 | 112,252 | 123,496 | 563 |
| 𝒫3=𝒜+h3⋅ℐ3\mathcal{P}\_{3}=\mathcal{A}+h\_{3}\cdot\mathcal{I}\_{3} | 0.311 | 875,566 | 90,413 | 1,571 |

Table 5: Calibrated hedge ratios and numerical risk measures for Illustration 1.



![Refer to caption](x10.png)


(a) Unadjusted

![Refer to caption](x11.png)


(b) Mean-adjusted

Figure 6: Graphical risk metric applied to the hedged positions 𝒫1\mathcal{P}\_{1} (yellow), 𝒫2\mathcal{P}\_{2} (blue) and 𝒫3\mathcal{P}\_{3} (pink) from Illustration 1.

In summary, this illustration demonstrates how the proposed framework and graphical risk metric together facilitate the selection of an appropriate insurance portfolio for natural hedging. Consistent with expectations, 𝒫1\mathcal{P}\_{1} with whole life policies issued to the same age range as the annuity portfolio provides the most effective hedge. Restricting the insurance portfolio to younger issuing ages, as in 𝒫2\mathcal{P}\_{2}, increases variability and weakens the offset between annuity and insurance liabilities. Further shortening the policy term to 20 years, as in 𝒫3\mathcal{P}\_{3}, amplifies this effect and leads to more outcomes with *No Hedging Effect*. These results highlight that when issuing ages or policy terms deviate from those of the underlying annuity portfolio, the effectiveness of natural hedging reduces and the residual risk becomes more pronounced.

### 4.2 Illustration 2: Hedge Calibration

The second illustration examines how different hedge calibration methods affect the effectiveness of a natural hedge. Consider an insurer managing an annuity portfolio issued to individuals aged 40-60, with $10,000 annual payments starting at age 65 for 20 years. The insurer constructs an insurance portfolio of whole life policies issued to the same age range and applies three different calibration methods for determining the hedge ratio: variance-minimisation (VM), duration-matching (DM), and delta-neutral (DN). Table [6](https://arxiv.org/html/2510.18721v1#S4.T6 "Table 6 ‣ 4.2 Illustration 2: Hedge Calibration ‣ 4 Numerical Illustrations") summarises how the natural hedging framework is applied to this illustration. The valuation and evaluation steps remain identical across the three methods, with the only difference lying in the calibration step.

| Step | Details |
| --- | --- |
| |  | | --- | | Step 1: | | Valuation | | |  | | --- | | Derive the present values of the annuity portfolio (issuing ages 40-60, deferred to 65, 20 annual payments of $10,000) and the insurance portfolio of whole life policies with a $750,000 death benefit issued to individuals aged 40-60. | |
| |  | | --- | | Step 2: | | Calibration | | |  | | --- | | Calibrate the hedge ratio using three different methods: h(V​M)h^{(VM)} from the variance-minimisation method, h(D​M)h^{(DM)} from the duration-matching method, and h(D​N)h^{(DN)} from the delta-neutral method. | |
| |  | | --- | | Step 3: | | Evaluation | | |  | | --- | | Construct the hedged portfolios 𝒫(V​M)\mathcal{P}^{(VM)}, 𝒫(D​M)\mathcal{P}^{(DM)}, and 𝒫(D​N)\mathcal{P}^{(DN)}, and evaluate them comparatively using both numerical risk measures and the proposed graphical risk metric. | |
| |  | | --- | | Projected | | Mortality | | |  | | --- | | Mortality scenarios are generated using the Lee-Carter model described in Appendix [B.1](https://arxiv.org/html/2510.18721v1#A2.SS1 "B.1 Model-based approach ‣ Appendix B Mortality Scenario Generator"), applied consistently across the valuation, calibration, and evaluation steps. | |

Table 6: Natural hedging framework applied to Illustration 2.

Table [7](https://arxiv.org/html/2510.18721v1#S4.T7 "Table 7 ‣ 4.2 Illustration 2: Hedge Calibration ‣ 4 Numerical Illustrations") reports the calibrated hedge ratios and numerical risk measures for the three portfolios. The hedge ratios range between 0.189 and 0.211, with the smallest from duration matching and the largest from delta neutral. As expected, 𝒫(V​M)\mathcal{P}^{(VM)} achieves the lowest variance while 𝒫(D​N)\mathcal{P}^{(DN)} exhibits the highest risk across all measures. Figure [7](https://arxiv.org/html/2510.18721v1#S4.F7 "Figure 7 ‣ 4.2 Illustration 2: Hedge Calibration ‣ 4 Numerical Illustrations") compares the three hedged portfolios using the graphical risk metric. In Panel (a), the unadjusted portfolios show that 𝒫(D​M)\mathcal{P}^{(DM)} requires the least amount of insurance liabilities, while 𝒫(D​N)\mathcal{P}^{(DN)} requires the most, consistent with their respective hedge ratios. Panel (b) displays the mean-adjusted portfolios, where 𝒫~(V​M)\tilde{\mathcal{P}}^{(VM)} lies closest to the benchmark line, indicating balanced offsetting between annuity and insurance liabilities. In contrast, 𝒫~(D​M)\tilde{\mathcal{P}}^{(DM)} tilts toward the *Not Enough Insurance Liabilities* region, and 𝒫~(D​N)\tilde{\mathcal{P}}^{(DN)} toward the *Too Much Insurance Liabilities* region, revealing systematic under- and over-hedging tendencies.

| Portfolio | Hedge Ratio | Variance | VaR0.95\text{VaR}\_{0.95} | Mean-adjusted VaR0.95\text{VaR}\_{0.95} |
| --- | --- | --- | --- | --- |
| 𝒫(V​M)=𝒜+h(V​M)⋅ℐ\mathcal{P}^{(VM)}=\mathcal{A}+h^{(VM)}\cdot\mathcal{I} | 0.198 | 4,816 | 108,670 | 113 |
| 𝒫(D​M)=𝒜+h(D​M)⋅ℐ\mathcal{P}^{(DM)}=\mathcal{A}+h^{(DM)}\cdot\mathcal{I} | 0.189 | 5,744 | 106,614 | 123 |
| 𝒫(D​N)=𝒜+h(D​N)⋅ℐ\mathcal{P}^{(DN)}=\mathcal{A}+h^{(DN)}\cdot\mathcal{I} | 0.211 | 6,642 | 111,690 | 132 |

Table 7: Calibrated hedge ratios and numerical risk measures for Illustration 2.



![Refer to caption](x12.png)


(a) Unadjusted

![Refer to caption](x13.png)


(b) Mean-adjusted

Figure 7: Graphical risk metric applied to the hedged positions 𝒫(V​M)\mathcal{P}^{(VM)} (yellow), 𝒫(D​M)\mathcal{P}^{(DM)} (blue), and 𝒫(D​N)\mathcal{P}^{(DN)} (pink) from Illustration 2.

In summary, this illustration shows how the choice of hedge ratio calibration method influences both numerical performance and hedging behaviour. The variance-minimisation method achieves the most balanced hedge, with the lowest variance and a symmetric distribution of hedging outcomes. The duration-matching approach tends to under-hedge, while the delta-neutral approach tends to over-hedge, leaving asymmetric residual risk exposure in the hedged position. The numerical and graphical results jointly provide a coherent view of the trade-offs underlying different calibration methods.

### 4.3 Illustration 3: Model Risk

Our final illustration examines the impact of model risk on natural hedging effectiveness. Suppose an insurer uses the Lee-Carter (LC) model to calibrate a natural hedge but is concerned that actual mortality may not be accurately described by it. To investigate the risk that the mortality model assumed for calibration differs from the one generating actual future mortality, the insurer considers two additional models for evaluation: the Cairns-Blake-Dowd (CBD) model and a non-parametric bootstrapping (BS) model. The goal is to assess whether the hedged position constructed by the LC model is robust to alternative mortality generating methods. Table [8](https://arxiv.org/html/2510.18721v1#S4.T8 "Table 8 ‣ 4.3 Illustration 3: Model Risk ‣ 4 Numerical Illustrations") summarises how the natural hedging framework is applied to this setting. The annual interest rate is again assumed to be 4%, and the limiting age is set at 100.

| Step | Details |
| --- | --- |
| |  | | --- | | Step 1: | | Valuation | | |  | | --- | | Derive the present values of the annuity portfolio (issuing ages 40-60, deferred to age 65, 35 annual payments of $10,000) and the whole-life insurance portfolio with a $750,000 death benefit issued to the same ages. | |
| |  | | --- | | Step 2: | | Calibration | | |  | | --- | | Calibrate the hedge ratio hh using the variance-minimisation method with mortality scenarios generated from the LC model. | |
| |  | | --- | | Step 3: | | Evaluation | | |  | | --- | | Construct and compare the hedged portfolios 𝒫(L​C)\mathcal{P}^{(LC)}, 𝒫(C​B​D)\mathcal{P}^{(CBD)}, and 𝒫(B​S)\mathcal{P}^{(BS)}, which are evaluated using mortality scenarios generated by the LC, CBD, and BS models, respectively. | |
| |  | | --- | | Projected | | Mortality | | |  | | --- | | Mortality scenarios are generated from the LC model in the calibration step, and from the LC, CBD, and BS models in the evaluation step. The mortality generating processes are provided in Appendix [B](https://arxiv.org/html/2510.18721v1#A2 "Appendix B Mortality Scenario Generator"). | |

Table 8: Natural hedging framework applied to Illustration 3.

Table [9](https://arxiv.org/html/2510.18721v1#S4.T9 "Table 9 ‣ 4.3 Illustration 3: Model Risk ‣ 4 Numerical Illustrations") reports the calibrated hedge ratio and numerical risk measures for the three portfolios. The hedge ratio is identical across all portfolios (h=0.310h=0.310). When evaluated by the same model used in the calibration step, 𝒫(L​C)\mathcal{P}^{(LC)} exhibits the lowest variance and mean-adjusted VaR0.95\text{VaR}\_{0.95}. However, when mortality is generated from an alternative model, 𝒫(C​B​D)\mathcal{P}^{(CBD)} shows substantially higher variability, while 𝒫(B​S)\mathcal{P}^{(BS)} lies between 𝒫(L​C)\mathcal{P}^{(LC)} and 𝒫(C​B​D)\mathcal{P}^{(CBD)} in both variance and mean-adjusted VaR0.95\text{VaR}\_{0.95}. These results suggest that when a natural hedge is both calibrated and evaluated under the LC model, its hedge effectiveness may be significantly overestimated.

| Portfolio | Hedge Ratio | Variance | VaR0.95\text{VaR}\_{0.95} | Mean-adjusted VaR0.95\text{VaR}\_{0.95} |
| --- | --- | --- | --- | --- |
| 𝒫(L​C)\mathcal{P}^{(LC)} | 0.310 | 1,628 | 143,093 | 67 |
| 𝒫(C​B​D)\mathcal{P}^{(CBD)} | 0.310 | 245,611 | 142,538 | 697 |
| 𝒫(B​S)\mathcal{P}^{(BS)} | 0.310 | 66,711 | 143,290 | 350 |

Table 9: Calibrated hedge ratio and numerical risk measures for Illustration 3.

Figure [8](https://arxiv.org/html/2510.18721v1#S4.F8 "Figure 8 ‣ 4.3 Illustration 3: Model Risk ‣ 4 Numerical Illustrations") compares the three portfolios using the graphical risk metric. In Panel (a), the unadjusted version shows that 𝒫(L​C)\mathcal{P}^{(LC)} exhibits the smallest joint prediction region, while 𝒫(C​B​D)\mathcal{P}^{(CBD)} and 𝒫(B​S)\mathcal{P}^{(BS)} display much wider dispersion in both the annuity and insurance portfolios. The mean-adjusted version in Panel (b) reveals that 𝒫~(L​C)\tilde{\mathcal{P}}^{(LC)} lies closest to the benchmark line, whereas both 𝒫~(C​B​D)\tilde{\mathcal{P}}^{(CBD)} and 𝒫~(B​S)\tilde{\mathcal{P}}^{(BS)} tilt toward the *Too Much Insurance Liabilities* region. This suggests that the LC-calibrated natural hedge tends to require an excessive amount of insurance liabilities, resulting in suboptimal hedging outcomes when actual mortality deviates from the LC model. This is an insight that cannot be easily inferred from the numerical results alone.

![Refer to caption](x14.png)


(a) Unadjusted

![Refer to caption](x15.png)


(b) Mean-adjusted

Figure 8: Graphical risk metric applied to the hedged positions 𝒫(L​C)\mathcal{P}^{(LC)} (yellow), 𝒫(C​B​D)\mathcal{P}^{(CBD)} (blue), and 𝒫(B​S)\mathcal{P}^{(BS)} (pink) in Illustration 3.

From Figure [8](https://arxiv.org/html/2510.18721v1#S4.F8 "Figure 8 ‣ 4.3 Illustration 3: Model Risk ‣ 4 Numerical Illustrations"), we see that 𝒫~(C​B​D)\tilde{\mathcal{P}}^{(CBD)} extends beyond the dashed lines, while 𝒫~(B​S)\tilde{\mathcal{P}}^{(BS)} remains within them, indicating that the CBD model implies more volatile and extreme hedging outcomes than the non-parametric BS approach. To further illustrate their differences, Figure [9](https://arxiv.org/html/2510.18721v1#S4.F9 "Figure 9 ‣ 4.3 Illustration 3: Model Risk ‣ 4 Numerical Illustrations") plots simulated realisations of 𝒫~(C​B​D)\tilde{\mathcal{P}}^{(CBD)} and 𝒫~(B​S)\tilde{\mathcal{P}}^{(BS)}, coloured by hedging outcome. Both portfolios show a concentration of realisations in the *Too Much Insurance Liabilities* region. However, when compared against their respective mean-adjusted VaR0.95\text{VaR}\_{0.95} thresholds (marked by the dashed lines), the exceedances for 𝒫~(C​B​D)\tilde{\mathcal{P}}^{(CBD)} occur mainly due to *Too Much Insurance Liabilities*, whereas for 𝒫~(B​S)\tilde{\mathcal{P}}^{(BS)}, the exceedances arise across all three hedging outcome types.

![Refer to caption](x16.png)


(a) Hedged position 𝒫~(C​B​D)\tilde{\mathcal{P}}^{(CBD)}

![Refer to caption](x17.png)


(b) Hedged position 𝒫~(B​S)\tilde{\mathcal{P}}^{(BS)}

Figure 9: Simulated outcomes of 𝒫~(C​B​D)\tilde{\mathcal{P}}^{(CBD)} and 𝒫~(B​S)\tilde{\mathcal{P}}^{(BS)}, coloured by hedging outcome with the dashed line denoting the mean-adjusted VaR0.95\text{VaR}\_{0.95}.

In summary, this illustration demonstrates that model risk can significantly distort the perceived effectiveness of a natural hedge. When the mortality model used for evaluation differs from the one used in calibration, the hedged position exhibits suboptimal performance and excess volatility under our natural hedging framework. The proposed graphical risk metric complements traditional numerical measures by revealing how these distortions arise from differing mortality dynamics and by exposing variations in hedging outcome types that numerical summaries alone would overlook.

## 5 Conclusion

This paper developed a comprehensive framework for constructing and evaluating natural hedging strategies, complemented by a graphical risk metric specifically designed for visual assessment of natural hedges. The proposed framework unifies the valuation, calibration, and evaluation steps of natural hedging to provide a structured process for comparing different portfolio settings, calibration techniques, and mortality scenarios. The graphical risk metric provides a new evaluation dimension by visualizing the joint distribution of annuity and insurance liabilities and by distinguishing different hedging outcome types. Together, these risk management tools form an integrated approach for analysing longevity and mortality risks underlying a life insurer’s balance sheet.

The proposed natural hedging framework and graphical risk metric offer several practical benefits. The framework enables consistent implementation of natural hedging across multiple policy types, calibration techniques, and model assumptions. It is also highly flexible and can accommodate various existing or newly developed natural hedging strategies beyond those demonstrated in this paper. The graphical risk metric complements the framework as an innovative evaluation tool for assessing and comparing multiple natural hedges when making hedging decisions. It further enhances interpretability by revealing whether poor performance arises from insufficient or excessive diversification, or from a lack of offsetting effects between liabilities.

Using three numerical illustrations, we demonstrated the capability and diagnostic value of the proposed methods. The results show that the framework can identify trade-offs among different insurance portfolios, assess calibration techniques across variance-minimisation, duration-matching, and delta-neutral approaches, and evaluate hedge robustness under alternative mortality scenario generators. In all cases, the graphical risk metric reveals dependencies and asymmetries in hedge performance that are otherwise hidden within numerical risk measures. Although the underlying risks differ across illustrations, the proposed methods effectively address each scenario, demonstrating their flexibility and practical applicability.

This study has several limitations that call for further development. First, future research could extend the framework to incorporate stochastic interest rates, dynamic hedging strategies, and alternative mortality models. Second, the graphical risk metric can be enhanced by asymmetric or non-convex joint prediction regions to capture skewed risk profiles and sudden mortality shocks. Finally, the natural hedging framework could be expanded to integrate solvency capital requirements and to support intuitive visualization for regulatory solvency assessments. Together, these potential directions would further advance the integration of natural hedging within longevity risk management research.

## Conflict of Interest

The authors declare that they have no competing interests.

## Data Availability

Replication code and data used in this study are available from the corresponding author upon reasonable request. All simulated mortality and portfolio data were generated using publicly available mortality inputs from the Human Mortality Database.

## Funding

This research was supported by the Natural Sciences and Engineering Research Council of Canada under Grant No. RGPIN-2025-04157 and DGECR-2025-00488. The funder had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## References

* Blake et al., (2008)

  Blake, D., Dowd, K., and Cairns, A. J. (2008).
  Longevity risk and the grim reaper’s toxic tail: The survivor fan
  charts.
  Insurance: Mathematics and Economics, 42(3):1062–1066.
* Cairns, (2013)

  Cairns, A. J. (2013).
  Robust hedging of longevity risk.
  Journal of Risk and Insurance, 80(3):621–648.
* Cairns et al., (2014)

  Cairns, A. J., Dowd, K., Blake, D., and Coughlan, G. D. (2014).
  Longevity hedge effectiveness: A decomposition.
  Quantitative Finance, 14(2):217–235.
* Chan et al., (2016)

  Chan, W.-S., Li, J. S., Zhou, K. Q., and Zhou, R. (2016).
  Towards a large and liquid longevity market: A graphical population
  basis risk metric.
  The Geneva Papers on Risk and Insurance-Issues and Practice,
  41:118–127.
* Chen et al., (2024)

  Chen, H., Gao, J., and Zhu, W. (2024).
  A unified framework for insurance demand and mortality immunization.
  North American Actuarial Journal, 28(2):469–490.
* Coughlan et al., (2011)

  Coughlan, G. D., Khalaf-Allah, M., Ye, Y., Kumar, S., Cairns, A. J., Blake, D.,
  and Dowd, K. (2011).
  Longevity hedging 101: A framework for longevity basis risk analysis
  and hedge effectiveness.
  North American Actuarial Journal, 15(2):150–176.
* Cox and Lin, (2007)

  Cox, S. H. and Lin, Y. (2007).
  Natural hedging of life and annuity mortality risks.
  North American Actuarial Journal, 11(3):1–15.
* Cupido et al., (2024)

  Cupido, K., Jevtić, P., Regis, L., and Zhou, K. Q. (2024).
  Spatial natural hedging: a general framework with application to the
  mortality of u.s. states.
  Scandinavian Actuarial Journal, 0(0):1–29.
* Dowd et al., (2010)

  Dowd, K., Blake, D., and Cairns, A. J. (2010).
  Facing up to uncertain life expectancy: The longevity fan charts.
  Demography, 47:67–78.
* Gatzert and Wesker, (2012)

  Gatzert, N. and Wesker, H. (2012).
  The impact of natural hedging on a life insurer’s risk situation.
  The Journal of Risk Finance, 13(5):396–423.
* Gatzert and Wesker, (2014)

  Gatzert, N. and Wesker, H. (2014).
  Mortality risk and its effect on shortfall and risk management in
  life insurance.
  Journal of Risk and Insurance, 81(1):57–90.
* Jevtić and Regis, (2015)

  Jevtić, P. and Regis, L. (2015).
  Assessing the solvency of insurance portfolios via a continuous-time
  cohort model.
  Insurance: Mathematics and Economics, 61:36–47.
* Lee and Carter, (1992)

  Lee, R. D. and Carter, L. R. (1992).
  Modeling and forecasting us mortality.
  Journal of the American statistical association,
  87(419):659–671.
* Li and Liu, (2021)

  Li, J. S.-H. and Liu, Y. (2021).
  Recent declines in life expectancy: Implication on longevity risk
  hedging.
  Insurance: Mathematics and Economics, 99:376–394.
* Li and Luo, (2012)

  Li, J. S.-H. and Luo, A. (2012).
  Key q-duration: A framework for hedging longevity risk.
  Astin Bulletin: The Journal of the IAA, 42(2):413–452.
* Li and Ng, (2011)

  Li, J. S.-H. and Ng, A. C.-Y. (2011).
  Canonical valuation of mortality-linked securities.
  Journal of Risk and Insurance, 78(4):853–884.
* Lin and Tsai, (2014)

  Lin, T. and Tsai, C. C.-L. (2014).
  Applications of mortality durations and convexities in natural
  hedges.
  North American Actuarial Journal, 18(3):417–442.
* Liu and Li, (2017)

  Liu, Y. and Li, J. S.-H. (2017).
  The locally linear cairns–blake–dowd model: a note on delta–nuga
  hedging of longevity risk.
  ASTIN Bulletin: The Journal of the IAA, 47(1):79–151.
* Luciano et al., (2012)

  Luciano, E., Regis, L., and Vigna, E. (2012).
  Delta–gamma hedging of mortality and interest rate risk.
  Insurance: Mathematics and Economics, 50(3):402–412.
* Luciano et al., (2017)

  Luciano, E., Regis, L., and Vigna, E. (2017).
  Single-and cross-generation natural hedging of longevity and
  financial risk.
  Journal of Risk and Insurance, 84(3):961–986.
* Redington, (1952)

  Redington, F. M. (1952).
  Review of the principles of life-office valuations.
  Journal of the Institute of Actuaries, 78(3):286–340.
* Riffe, (2015)

  Riffe, T. (2015).
  Reading human fertility database and human mortality database data
  into r.
  Technical Report TR-2015-004, MPIDR.
* Sherris et al., (2020)

  Sherris, M., Xu, Y., and Ziveyi, J. (2020).
  Cohort and value-based multi-country longevity risk management.
  Scandinavian Actuarial Journal, 2020(7):650–676.
* Tsai et al., (2010)

  Tsai, J. T., Wang, J. L., and Tzeng, L. Y. (2010).
  On the optimal product mix in life insurance companies using
  conditional value at risk.
  Insurance: Mathematics and Economics, 46(1):235–241.
* Villegas et al., (2018)

  Villegas, A. M., Kaishev, V. K., and Millossovich, P. (2018).
  StMoMo: An R package for stochastic mortality modeling.
  Journal of Statistical Software, 84(3):1–38.
* Wang et al., (2010)

  Wang, J. L., Huang, H., Yang, S. S., and Tsai, J. T. (2010).
  An optimal product mix for hedging longevity risk in life insurance
  companies: The immunization theory approach.
  Journal of Risk and Insurance, 77(2):473–497.
* Yang et al., (2019)

  Yang, S. S., Huang, H.-C., and Yeh, Y.-Y. (2019).
  Optimal longevity hedging framework for insurance companies
  considering basis and mispricing risks.
  The Journal of Risk and Insurance, 86(3):783–805.
* Zhou and Li, (2021)

  Zhou, K. Q. and Li, J. S.-H. (2021).
  Longevity Greeks: What do insurers and capital market investors
  need to know?
  North American Actuarial Journal, 25(sup1):S66–S96.
* Zhu and Bauer, (2011)

  Zhu, N. and Bauer, D. (2011).
  Applications of forward mortality factor models in life insurance
  practice.
  The Geneva Papers on Risk and Insurance-Issues and Practice,
  36(4):567–594.
* Zhu and Bauer, (2014)

  Zhu, N. and Bauer, D. (2014).
  A cautionary note on natural hedging of longevity risk.
  North American Actuarial Journal, 18(1):104–115.

## Appendix A Metric Construction

### A.1 Review of Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4))

Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4)) proposed a graphical risk metric to visually assess population basis risk that cannot be transferred through an index-based longevity hedge. It serves as a visualization tool to identify the reference population with the lowest basis risk. In this appendix, we briefly review the construction of this risk metric, which we adapted for developing the graphical risk metric for natural hedging.

Suppose a hedger seeks to mitigate the longevity risk of its mortality-dependent liabilities associated with population HH that is proportional to a survivor measure S(H)S^{(H)}. The hedger selects a mortality-dependent derivative linked to population RR, with a payoff proportional to a survivor index S(R)S^{(R)}. The graphical population basis risk metric aims to visualize the potential deviations between the mortality dependent liabilities S(H)S^{(H)} and the derivatives S(R)S^{(R)}. Let C(i)=S(i)−𝔼​(S(i))C^{(i)}=S^{(i)}-\mathbb{E}(S^{(i)}) be the mean-adjusted value of S(i)S^{(i)} for i=Ri=R and HH. Using C(i)C^{(i)} instead of S(i)S^{(i)} has two advantages: it focuses on deviations from the expectation rather than the values themselves, and it centers the realisations of S(i)S^{(i)} at the origin, allowing visual comparison of outcome of different reference populations RR.

Prior to constructing the graphical metric, Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4)) incorporates a variance minimization hedging approach, similar to the one provided in Section [2.2.1](https://arxiv.org/html/2510.18721v1#S2.SS2.SSS1 "2.2.1 Optimization ‣ 2.2 Calibration ‣ 2 The Natural Hedging Framework"). The hedge ratio is calibrated with realisations of C(R)C^{(R)} and C(H)C^{(H)}, denoted as h(R)h^{(R)} for the reference population RR. Therefore, the hedged position contains C(H)C^{(H)} and h(R)​C(R)h^{(R)}C^{(R)}. The graphical risk metric constructs multiple joint prediction regions, reflecting varying uncertainty levels, defined by deviations between C(H)C^{(H)} and h(R)​C(R)h^{(R)}C^{(R)}. Formally, the joint prediction region 𝐉α\mathbf{J}\_{\alpha} for (C(H),h(R)​C(R))(C^{(H)},h^{(R)}C^{(R)}) is defined as

|  |  |  |
| --- | --- | --- |
|  | Pr⁡{(C(H),h(R)​C(R))∈𝐉α}=1−α,\Pr\left\{\left(C^{(H)},h^{(R)}C^{(R)}\right)\in\mathbf{J}\_{\alpha}\right\}=1-\alpha, |  |

where α∈[0,1]\alpha\in[0,1] is the level of uncertainty, such that the area of 𝐉α\mathbf{J}\_{\alpha} contains 100​(1−α)100(1-\alpha)% of the realisations of (C(H),h(R)​C(R))(C^{(H)},h^{(R)}C^{(R)}). A higher level of population basis risk corresponds to a larger area spanned by 𝐉α\mathbf{J}\_{\alpha} for a given α\alpha.

Finally, the graphical population basis risk metric is constructed as follows:

1. 1.

   Simulate NN realisations of the mortality rates that are relevant to S(H)S^{(H)} and S(R)S^{(R)}, and use the simulated mortality rates to calculate NN realized values of C(H)=S(H)−𝔼​(S(H))C^{(H)}=S^{(H)}-\mathbb{E}(S^{(H)}) and C(R)=S(R)−𝔼​(S(R))C^{(R)}=S^{(R)}-\mathbb{E}(S^{(R)}).
2. 2.

   Use the realized values of C(H)C^{(H)} and C(R)C^{(R)} to compute the hedge ratio h(R)h^{(R)}, and obtain the hedged position consisting of C(H)C^{(H)} and h(R)​C(R)h^{(R)}C^{(R)}.
3. 3.

   For each realisation of 𝐘:=(C(H),h(R)​C(R))′\mathbf{Y}:=\left(C^{(H)},h^{(R)}C^{(R)}\right)^{{}^{\prime}}, calculate the Mahalanobis distance to the origin as 𝐘′​𝚺−1​𝐘\mathbf{Y}^{{}^{\prime}}\mathbf{\Sigma}^{-1}\mathbf{Y}, where 𝚺\mathbf{\Sigma} is the covariance matrix of 𝐘\mathbf{Y} and is estimated using the NN realisations of 𝐘\mathbf{Y}.
4. 4.

   Order the NN realisations of 𝐘\mathbf{Y} by their Mahalanobis distance, and select the observations that have the shortest N​(1−α)N(1-\alpha) distances with α=0.1,0.2,…,0.9\alpha=0.1,0.2,\dots,0.9.
5. 5.

   Enclose the selected N​(1−α)N(1-\alpha) observations of 𝐘\mathbf{Y} by drawing a convex hull to form the joint prediction region for each α\alpha, where different values of α\alpha will be given different levels of shading transparency.

### A.2 Construction of the graphical risk metric

In this appendix, we provide the procedure for constructing the proposed graphical risk metric for natural hedging. Recall from Table [1](https://arxiv.org/html/2510.18721v1#S2.T1 "Table 1 ‣ 2.1.3 Summary of notations ‣ 2.1 Valuation ‣ 2 The Natural Hedging Framework") that 𝒜\mathcal{A} and ℐ\mathcal{I} are the present value random variables of the annuity and insurance portfolios, respectively, in the valuation step. The present value of the calibrated insurance portfolio is defined as ℒ:=ℒ​(h)=h⋅ℐ\mathcal{L}:=\mathcal{L}(h)=h\cdot\mathcal{I}, where hh is the hedge ratio computed in the calibration step. At the evaluation step, the hedged portfolio is expressed as 𝒫​(h)=𝒜+ℒ​(h)\mathcal{P}(h)=\mathcal{A}+\mathcal{L}(h).

![Refer to caption](x18.png)


(a) A scatter plot of 20,000 realisations of the assumed annuity and insurance portfolios, (𝒜,ℒ)(\mathcal{A},\mathcal{L}).

![Refer to caption](x19.png)


(b) Two red arrow lines indicating the physical distance from a realisation of (𝒜,ℒ)(\mathcal{A},\mathcal{L}) to the expectation point (A,L)(A,L).

![Refer to caption](x20.png)


(c) Convex hull for 𝐉0.05\mathbf{J}\_{0.05}, the joint prediction region that contains 95% of the 20,000 realisations of (𝒜,ℒ)(\mathcal{A},\mathcal{L}).

![Refer to caption](x21.png)


(d) A series of convex hulls for 𝐉α\mathbf{J}\_{\alpha}, α=0.05,0.10,…,0.95\alpha=0.05,0.10,\dots,0.95, with a darker degree of shading as α\alpha increases.

Figure A.1: The construction of graphical risk metric for natural hedging.

An objective of our graphical risk metric is to visualize the joint distribution of (𝒜,ℒ)(\mathcal{A},\mathcal{L}). Figure [A.1](https://arxiv.org/html/2510.18721v1#A1.F1 "Figure A.1 ‣ A.2 Construction of the graphical risk metric ‣ Appendix A Metric Construction") presents the step-by-step progression of a graphical region construction for a single portfolio. This portfolio is from the toy example with an issuing age of 40 for life insurance. Figure [1(a)](https://arxiv.org/html/2510.18721v1#A1.F1.sf1 "In Figure A.1 ‣ A.2 Construction of the graphical risk metric ‣ Appendix A Metric Construction") shows a scatter plot of 20,000 realisations of (𝒜,ℒ)(\mathcal{A},\mathcal{L}), generated by the Lee-Carter model. We observe an inverse relationship between 𝒜\mathcal{A} and ℒ\mathcal{L} – as 𝒜\mathcal{A} increases, ℒ\mathcal{L} generally decreases, forming a downward sloping cloud of points. This relationship is expected, as both variables depend on survival probabilities in opposite ways; when projected survival probabilities rise, the present value of future annuity liabilities increase, while the present value of future insurance liabilities decrease.

Following Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4)), we measure the Mahalanobis distance for each pair (𝒜,ℒ)(\mathcal{A},\mathcal{L}) to its expectation value (A,L)(A,L), where A=𝔼​[𝒜]A=\mathbb{E}[\mathcal{A}] and L=𝔼​[ℒ]L=\mathbb{E}[\mathcal{L}]. The Mahalanobis distance of the realisations 𝓨:=(𝒜,ℒ)′\bm{\mathcal{Y}}:=(\mathcal{A},\mathcal{L})^{\prime} to 𝐘:=(A,L)′\mathbf{Y}:=(A,L)^{\prime} is calculated as

|  |  |  |
| --- | --- | --- |
|  | (𝓨−𝒀)′​𝚺−1​(𝓨−𝒀),\left(\bm{\mathcal{Y}}-\bm{Y}\right)^{{}^{\prime}}\bm{\Sigma}^{-1}\left(\bm{\mathcal{Y}}-\bm{Y}\right), |  |

where 𝚺\bm{\Sigma} is the covariance matrix of 𝓨\bm{\mathcal{Y}}. In [1(b)](https://arxiv.org/html/2510.18721v1#A1.F1.sf2 "1(b) ‣ Figure A.1 ‣ A.2 Construction of the graphical risk metric ‣ Appendix A Metric Construction"), the red dot at the center of the cloud represents the position of 𝐘\mathbf{Y}, while the two red lines depicts the physical distance of the realisations of 𝓨\bm{\mathcal{Y}} to 𝐘\mathbf{Y}. The Mahalanobis distance can be interpreted as the physical distance weighted by the covariance matrix 𝚺\bm{\Sigma}.

We are now ready to construct the graphical risk metric. Similar to Chan et al., ([2016](https://arxiv.org/html/2510.18721v1#bib.bib4)), our proposed graphical risk metric consists of multiple joint prediction regions representing different levels of uncertainty. For a probability α∈[0,1]\alpha\in[0,1], the joint prediction region 𝐉α\mathbf{J}\_{\alpha} for (𝒜,ℒ)(\mathcal{A},\mathcal{L}) is given by

|  |  |  |
| --- | --- | --- |
|  | Pr⁡{(𝒜,ℒ)∈𝐉α}=1−α.\Pr\left\{(\mathcal{A},\mathcal{L})\in\mathbf{J}\_{\alpha}\right\}=1-\alpha. |  |

[1(c)](https://arxiv.org/html/2510.18721v1#A1.F1.sf3 "1(c) ‣ Figure A.1 ‣ A.2 Construction of the graphical risk metric ‣ Appendix A Metric Construction") displays the joint prediction region for α=0.05\alpha=0.05, where 𝐉0.05\mathbf{J}\_{0.05} contains 95% of the 20,000 realisations of (𝒜,ℒ)(\mathcal{A},\mathcal{L}).

[1(d)](https://arxiv.org/html/2510.18721v1#A1.F1.sf4 "1(d) ‣ Figure A.1 ‣ A.2 Construction of the graphical risk metric ‣ Appendix A Metric Construction") displays multiple joint prediction regions where different levels of shading distinguish the varying values of α\alpha. As α\alpha increases, the corresponding joint prediction region is shaded darker. [1(d)](https://arxiv.org/html/2510.18721v1#A1.F1.sf4 "1(d) ‣ Figure A.1 ‣ A.2 Construction of the graphical risk metric ‣ Appendix A Metric Construction") illustrates the gradient effect of joint prediction regions for α=0.05,0.10,…,0.95\alpha=0.05,0.10,\dots,0.95. The layers of joint prediction regions form an oval-shape object, with the smallest region at the center containing 5% of the realisations and the largest region, with the lightest shading, containing 95% of the realisations.

We outline the procedure for constructing a series of joint prediction regions for the graphical risk metric for natural hedging:

1. 1.

   Simulate NN realisations of 𝒜\mathcal{A} and ℒ\mathcal{L} using a selected mortality scenario generator, such as the Lee-Carter model.
2. 2.

   Calculate the Mahalanobis distance for each realisation of (𝒜,ℒ)(\mathcal{A},\mathcal{L}) to its empirical expectation.
3. 3.

   Sort the NN realisations of (𝒜,ℒ)(\mathcal{A},\mathcal{L}) by their Mahalanobis distance, and subset the observations with the shortest N​(1−α)N(1-\alpha) distances for α=0.05,0.1,…,0.95\alpha=0.05,0.1,\dots,0.95.
4. 4.

   Draw a convex hull that encloses the selected N​(1−α)N(1-\alpha) observations for each α\alpha, adjusting the shading level as α\alpha changes.

## Appendix B Mortality Scenario Generator

### B.1 Model-based approach

To simulate survival probabilities under a stochastic mortality model, we apply the following procedure:

1. 1.

   Data: Import data into R from the Human Mortality Database using the HMDHFDplus R package (Riffe,, [2015](https://arxiv.org/html/2510.18721v1#bib.bib22)). We imported central death rates for lives aged xx in year tt, denoted as mx,tm\_{x,t}, from the US male population with years 1970-2018 and age 40-99.
2. 2.

   Fitting: Use the StMoMo package in R (Villegas et al.,, [2018](https://arxiv.org/html/2510.18721v1#bib.bib25)) to:

   1. (a)

      Define an StMoMo object for the selected model. For the Lee-Carter model, define the object by lc(link = ‘‘log’’, const = ‘‘sum’’). For the Cairns-Blake-Dowd model, define the object by cbd(link = ‘‘logit’’).
   2. (b)

      Fit the model using the fit() function, where the argument includes the StMoMo model object and the mortality data to be fitted.
3. 3.

   Projection: Project mortality rates using the simulate() function, where the argument includes the fitted model, the number of sample paths, and the projection horizon. The output consists of projected central death rates mx,tm\_{x,t} for the Lee-Carter model and probabilities of death qx,tq\_{x,t} for the Cairns-Blake-Dowd model
4. 4.

   Calculation:
   Substitute the projected m​x,tm{x,t} values into equation ([1](https://arxiv.org/html/2510.18721v1#S2.E1 "In 2.1 Valuation ‣ 2 The Natural Hedging Framework")) to obtain simulated survival probabilities 𝒮x​(T)\mathcal{S}\_{x}(T). For the Cairns-Blake-Dowd model, we convert qx,tq\_{x,t} into mx,tm\_{x,t} using the constant force of mortality assumption.

### B.2 Model-free approach

To generate stochastic survival probabilities from a non-parametric bootstrapping method, we follow the procedure outlined in Li and Ng, ([2011](https://arxiv.org/html/2510.18721v1#bib.bib16)).

1. 1.

   Data: Import data into R from the Human Mortality Database using the HMDHFDplus R package (Riffe,, [2015](https://arxiv.org/html/2510.18721v1#bib.bib22)). We imported central death rates for lives aged xx in year tt, denoted as mx,tm\_{x,t}, from the US male population with years 1970-2018 and age 40-99.
2. 2.

   Reduction calculation:

   1. (a)

      Obtain historical mortality reduction rates for lives aged xx in year tt, denoted as rx,t=mx,t+1mx,tr\_{x,t}=\frac{m\_{x,t+1}}{m\_{x,t}}.
      Since the dataset spans 49 years (1970-2018), we have a total of 48 reduction rates for each age.
   2. (b)

      Construct a mortality reduction matrix, where each row corresponds an age xx and each column denotes a year tt. The mortality reduction matrix from our data is

      |  |  |  |
      | --- | --- | --- |
      |  | 𝐫=[r40,1970r40,1971…r40,2017r41,1970r41,1971…r41,2017⋮⋮⋱⋮r99,1970r99,1971…r99,2017].\mathbf{r}=\begin{bmatrix}r\_{40,1970}&r\_{40,1971}&\dots&r\_{40,2017}\\ r\_{41,1970}&r\_{41,1971}&\dots&r\_{41,2017}\\ \vdots&\vdots&\ddots&\vdots\\ r\_{99,1970}&r\_{99,1971}&\dots&r\_{99,2017}\end{bmatrix}. |  |
   3. (c)

      Form overlapping mortality reduction blocks of size two, following Li and Ng, ([2011](https://arxiv.org/html/2510.18721v1#bib.bib16)). We obtained 47 mortality reduction blocks, corresponding to t=1970,…,2017t=1970,\dots,2017: (𝐫1970,𝐫1971),(𝐫1971,𝐫1972),…,(𝐫2016,𝐫2017)\left(\mathbf{r}\_{1970},\mathbf{r}\_{1971}\right),\left(\mathbf{r}\_{1971},\mathbf{r}\_{1972}\right),\dots,\left(\mathbf{r}\_{2016},\mathbf{r}\_{2017}\right).
3. 3.

   Pseudo sampling:

   1. (a)

      Set the initial mortality rates to those from the most recent year in the dataset. We set the initial rates to mx,2018m\_{x,2018} for x=40,…,99x=40,\dots,99.
   2. (b)

      Sample with replacement from the mortality reduction blocks to form a pseudo reduction matrix of future mortality. We sampled 35 blocks with replacement to project mortality for 70 future years.
   3. (c)

      Calculate the projected mortality rates by multiplying the initial rates across the pseudo reduction matrix. We calculated the projected values of mx,tm\_{x,t} for x=40,…,99x=40,\dots,99 and t=2019,…,2089t=2019,\dots,2089.
   4. (d)

      Repeat Steps 3(a)-3(c) to obtain multiple sets of projected mortality rates. We repeated these steps 20,000 times.
4. 4.

   Calculation:
   Substitute the projected mx,tm\_{x,t} values into equation ([1](https://arxiv.org/html/2510.18721v1#S2.E1 "In 2.1 Valuation ‣ 2 The Natural Hedging Framework")) to compute simulated survival probabilities 𝒮x​(T)\mathcal{S}\_{x}(T).

## Appendix C Numerical Illustration Details

This appendix summarises the policy specifications used in the numerical illustrations presented in Section [4](https://arxiv.org/html/2510.18721v1#S4 "4 Numerical Illustrations"). Table [C.1](https://arxiv.org/html/2510.18721v1#A3.T1 "Table C.1 ‣ Appendix C Numerical Illustration Details") outlines the issuing ages xx, terms tt, deferrals τ\tau and weights ω\omega of the annuity and insurance portfolios considered in the three illustrations. Specifically, Annuity Portfolio 1 and Insurance Portfolios 1-3 are used in Illustration 1, Annuity Portfolio 2 along with Insurance Portfolio 1 are used in Illustration 2, and Annuity Portfolio 1 together with Insurance Portfolio 1 are used in Illustration 3.

| jj | Annuity 1 | | | | Annuity 2 | | | | Insurance 1 | | | Insurance 2 | | | Insurance 3 | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xjx\_{j} | ωj\omega\_{j} | τj\tau\_{j} | tjt\_{j} | xjx\_{j} | ωj\omega\_{j} | τj\tau\_{j} | tjt\_{j} | xjx\_{j} | ωj\omega\_{j} | tjt\_{j} | xjx\_{j} | ωj\omega\_{j} | tjt\_{j} | xjx\_{j} | ωj\omega\_{j} | tjt\_{j} |
| 1 | 40 | 0.0517 | 25 | 35 | 40 | 0.0517 | 25 | 20 | 40 | 0.0517 | 60 | 40 | 0.1084 | 60 | 40 | 0.1084 | 20 |
| 2 | 41 | 0.0512 | 24 | 35 | 41 | 0.0512 | 24 | 20 | 41 | 0.0512 | 59 | 41 | 0.1073 | 59 | 41 | 0.1073 | 20 |
| 3 | 42 | 0.0506 | 23 | 35 | 42 | 0.0506 | 23 | 20 | 42 | 0.0506 | 58 | 42 | 0.1062 | 58 | 42 | 0.1062 | 20 |
| 4 | 43 | 0.0494 | 22 | 35 | 43 | 0.0494 | 22 | 20 | 43 | 0.0494 | 57 | 43 | 0.1035 | 57 | 43 | 0.1035 | 20 |
| 5 | 44 | 0.0477 | 21 | 35 | 44 | 0.0477 | 21 | 20 | 44 | 0.0477 | 56 | 44 | 0.1000 | 56 | 44 | 0.1000 | 20 |
| 6 | 45 | 0.0467 | 20 | 35 | 45 | 0.0467 | 20 | 20 | 45 | 0.0467 | 55 | 45 | 0.0980 | 55 | 45 | 0.0980 | 20 |
| 7 | 46 | 0.0456 | 19 | 35 | 46 | 0.0456 | 19 | 20 | 46 | 0.0456 | 54 | 46 | 0.0955 | 54 | 46 | 0.0955 | 20 |
| 8 | 47 | 0.0450 | 18 | 35 | 47 | 0.0450 | 18 | 20 | 47 | 0.0450 | 53 | 47 | 0.0942 | 53 | 47 | 0.0942 | 20 |
| 9 | 48 | 0.0447 | 17 | 35 | 48 | 0.0447 | 17 | 20 | 48 | 0.0447 | 52 | 48 | 0.0937 | 52 | 48 | 0.0937 | 20 |
| 10 | 49 | 0.0445 | 16 | 35 | 49 | 0.0445 | 16 | 20 | 49 | 0.0445 | 51 | 49 | 0.0932 | 51 | 49 | 0.0932 | 20 |
| 11 | 50 | 0.0458 | 15 | 35 | 50 | 0.0458 | 15 | 20 | 50 | 0.0458 | 50 | – | – | – | – | – | – |
| 12 | 51 | 0.0484 | 14 | 35 | 51 | 0.0484 | 14 | 20 | 51 | 0.0484 | 49 | – | – | – | – | – | – |
| 13 | 52 | 0.0494 | 13 | 35 | 52 | 0.0494 | 13 | 20 | 52 | 0.0494 | 48 | – | – | – | – | – | – |
| 14 | 53 | 0.0480 | 12 | 35 | 53 | 0.0480 | 12 | 20 | 53 | 0.0480 | 47 | – | – | – | – | – | – |
| 15 | 54 | 0.0464 | 11 | 35 | 54 | 0.0464 | 11 | 20 | 54 | 0.0464 | 46 | – | – | – | – | – | – |
| 16 | 55 | 0.0458 | 10 | 35 | 55 | 0.0458 | 10 | 20 | 55 | 0.0458 | 45 | – | – | – | – | – | – |
| 17 | 56 | 0.0461 | 9 | 35 | 56 | 0.0461 | 9 | 20 | 56 | 0.0461 | 44 | – | – | – | – | – | – |
| 18 | 57 | 0.0471 | 8 | 35 | 57 | 0.0471 | 8 | 20 | 57 | 0.0471 | 43 | – | – | – | – | – | – |
| 19 | 58 | 0.0484 | 7 | 35 | 58 | 0.0484 | 7 | 20 | 58 | 0.0484 | 42 | – | – | – | – | – | – |
| 20 | 59 | 0.0488 | 6 | 35 | 59 | 0.0488 | 6 | 20 | 59 | 0.0488 | 41 | – | – | – | – | – | – |
| 21 | 60 | 0.0487 | 5 | 35 | 60 | 0.0487 | 5 | 20 | 60 | 0.0487 | 40 | – | – | – | – | – | – |

Table C.1: Specifications and weights for the annuity and insurance portfolios used in the numerical illustrations.

All portfolio weights are constructed using population counts from the U.S. male population in year 2023, obtained from the Human Mortality Database via the HMDHFDplus package (Riffe,, [2015](https://arxiv.org/html/2510.18721v1#bib.bib22)). For each issuing age xx, the weight ωx\omega\_{x} is calculated as the proportion of the population at age xx relative to the total population across all ages considered in that portfolio:

|  |  |  |
| --- | --- | --- |
|  | ωx=Population count at age ​x∑x′∈𝒳Population count at age ​x′,\omega\_{x}=\frac{\text{Population count at age }x}{\sum\_{x^{\prime}\in\mathcal{X}}\text{Population count at age }x^{\prime}}, |  |

where 𝒳\mathcal{X} is the set of all ages considered.