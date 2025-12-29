---
authors:
- Benjamin Avanzi
- Debbie Kusch Falden
- Mogens Steffensen
doc_id: arxiv:2512.21973v1
family_id: arxiv:2512.21973
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and
  Risk Constraints'
url_abs: http://arxiv.org/abs/2512.21973v1
url_html: https://arxiv.org/html/2512.21973v1
venue: arXiv q-fin
version: 1
year: 2025
---


Benjamin Avanzi
[b.avanzi@unimelb.edu.au](mailto:b.avanzi@unimelb.edu.au)

Debbie Kusch Falden
[dkfalden@liverpool.ac.uk](mailto:dkfalden@liverpool.ac.uk)

Mogens Steffensen
[mogens@math.ku.dk](mailto:mogens@math.ku.dk)
Department of Economics, Faculty of Business and Economics
  
University of Melbourne, Melbourne VIC 3010, Australia
Department of Mathematical Sciences, University of Liverpool
  
L69 7ZL, Liverpool, UK
Department of Mathematical Sciences, University of Copenhagen
  
DK-2100 Copenhagen, Denmark

###### Abstract

In high-risk environments, traditional indemnity insurance is often unaffordable or ineffective, despite its well-known optimality under expected utility. This paper compares excess-of-loss indemnity insurance with parametric insurance within a common mean–variance framework, allowing for fixed costs, heterogeneous premium loadings, and binding budget constraints. We show that, once these realistic frictions are introduced, parametric insurance can yield higher welfare for risk-averse individuals, even under the same utility objective. The welfare advantage arises precisely when indemnity insurance becomes impractical, and disappears once both contracts are unconstrained. Our results help reconcile classical insurance theory with the growing use of parametric risk transfer in high-risk settings.

###### keywords:

Insurance , Parametric insurance , Expected utility
JEL codes: C44 , C61 , G22 , G32 , MSC classes:
60G51 , 93E20 , 91G70 , 62P05 91B30

## 1 Introduction

Insurance markets are increasingly strained in regions exposed to low-frequency, high-severity risks such as floods, wildfires, and cyclones. In many such areas, indemnity insurance has become prohibitively expensive or altogether unavailable, as rising hazard intensity, capital requirements, and fixed costs push premiums and deductibles to levels that leave households effectively uninsured. A key practical limitation is that household indemnity insurance is typically written on a full-value (sum-insured) basis: the premium is charged to cover the entire exposure, and the main lever to restore affordability is to raise the deductible. In high-risk areas, this mechanism can push deductibles to economically unrealistic levels (e.g., tens or hundreds of thousands of dollars), rendering the contract formally available but delivering negligible effective protection. By contrast, parametric insurance is inherently scalable: households can purchase a smaller, explicitly bounded layer of protection (a fixed payment per event) without having to insure the full loss.
Recent developments in flood and wildfire insurance markets illustrate this trend: insurers have withdrawn from parts of the California residential market, flood insurance take-up remains persistently low in high-risk zones, and coverage gaps are expanding even in advanced economies (e.g., Kousky and Cooke, [2012](https://arxiv.org/html/2512.21973v1#bib.bib17)). Yet when disasters occur, losses are rarely borne privately alone. Instead, they are often socialized ex post through government relief, reconstruction grants, and implicit guarantees. This growing disconnect between private insurance provision and public risk-bearing raises a fundamental economic question: when full indemnification is no longer feasible, what forms of risk transfer can still improve individual welfare?

Classical insurance theory provides a clear benchmark. Under broad and well-understood conditions, an excess-of-loss indemnity contract maximizes the expected utility of a risk-averse agent when premiums are loaded proportionally to expected losses (Arrow, [1971](https://arxiv.org/html/2512.21973v1#bib.bib2); Raviv, [1979](https://arxiv.org/html/2512.21973v1#bib.bib19)). This result has shaped both theoretical and practical views of optimal insurance design for decades. However, it relies on assumptions that are increasingly violated in high-risk environments. In particular, it abstracts from differences in risk borne and fixed costs borne by insurers across contract types, as well as binding budget constraints faced by households. When insurance is expensive, the deductible that is still affordable becomes so large that indemnity insurance offers little or no effective protection, even though it remains optimal in a purely formal sense.

This paper revisits the optimality of indemnity insurance in such settings by comparing it with parametric insurance. Parametric contracts replace loss-based indemnification with a fixed payment triggered by an objective index, such as the occurrence of a disaster event. While this design introduces basis risk (arising from imperfect loss matching), it eliminates most of the loss adjustment costs, allows for rapid payouts, and materially reduces the risk borne by insurers. As a result, parametric insurance can be priced with lower loadings and smaller fixed costs, and can remain feasible in environments where indemnity insurance breaks down. Despite its growing use in sovereign and corporate risk transfer, parametric insurance for households remains underdeveloped. That said, policy and industry discussions increasingly contemplate parametric household covers for catastrophic perils.

Nevertheless, indemnity insurance is still widely considered the best (or only) way to provide effective protection. We show that this view is incomplete. Using a tractable model of frequency and severity, we compare indemnity and parametric insurance under the same expected mean–variance utility criterion. Losses arrive according to a Poisson process and have censored exponential severity. This specification can capture the salient features of natural disaster risk (low-frequency, high-severity) while allowing for closed-form solutions. The indemnity contract is of excess-of-loss type with a deductible, while the parametric contract pays a fixed amount per event and shares the same trigger, so there is no basis risk on frequency. Importantly, we allow for distinct premium loadings and fixed costs across contract types, reflecting the higher capital requirements, claims management costs, and reconstruction delays associated with indemnity insurance.

Our main result is that, once these realistic frictions are introduced, parametric insurance can dominate indemnity insurance under the same utility objective. This dominance arises most clearly when households face binding budget constraints. In such cases, the deductible required to make indemnity insurance affordable may be so large that the contract is economically irrelevant. In contrast, a parametric contract can still provide a modest but meaningful transfer. We characterize indifference thresholds between the two designs and show that the welfare advantage of parametric insurance follows a non-monotonic pattern in the available premium budget: it emerges when budgets are small, disappears as indemnity insurance becomes effective, and vanishes entirely once both contracts are unconstrained.

These findings contribute to several strands of the literature. First, they complement the classical optimal insurance results by identifying conditions under which their practical relevance breaks down, without abandoning expected-utility-based evaluation. Our analysis complements the classical insurance literature following Arrow ([1963](https://arxiv.org/html/2512.21973v1#bib.bib1)) and Raviv ([1979](https://arxiv.org/html/2512.21973v1#bib.bib19)), which establishes the optimality of deductible insurance under proportional pricing and frictionless markets. Rather than challenging these results, we show how their economic relevance may erode when heterogeneous fixed costs and loadings, as well as budget constraints, are introduced. In this sense, the paper bridges the gap between foundational insurance theory and the observed expansion of parametric risk transfer in high-risk environments. Second, they add to the emerging economic analysis of parametric insurance, which has focused largely on sovereign and corporate applications (Clarke, [2016](https://arxiv.org/html/2512.21973v1#bib.bib10); Huang and Shi, [2024](https://arxiv.org/html/2512.21973v1#bib.bib13)). Third, they speak directly to current policy debates on disaster risk financing, insurance affordability, and the appropriate role of governments in supporting risk transfer in high-risk areas. Our analysis suggests that parametric insurance should not be viewed merely as an inferior substitute for indemnity insurance, but as a potentially welfare-improving instrument precisely where traditional insurance fails.

The key message is that, once affordability and implementation frictions are taken seriously, parametric insurance can improve welfare precisely in the environments where indemnity insurance becomes economically
irrelevant.

The remainder of the paper is organized as follows. Section 2 introduces the model and utility framework. Section 3 derives the optimal indemnity and parametric contracts in the absence of budget constraints. Section 4 analyzes the comparison under binding premium budgets and presents numerical illustrations. Section 5 discusses policy implications for disaster risk reduction, insurance market design, and public intervention. Section 6 concludes.

## 2 Theoretical framework for traditional indemnity and parametric insurance

### 2.1 Losses and benefits

We consider an agent who faces aggregate losses SS over a year that may stem from multiple events:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=∑i=1NYi,\displaystyle S=\sum\_{i=1}^{N}Y\_{i}, |  | (2.1) |

where NN denotes the number of loss-causing events in the year and YiY\_{i} are i.i.d. severities independent of N.111Throughout, we speak of an “event count” NN, but the same notation also covers a “claim count” interpretation. The distinction matters only when a single event can generate multiple claims; see Remark [2.1](https://arxiv.org/html/2512.21973v1#S2.Thmremark1 "Remark 2.1 (Event-level versus claim-level deductibles). ‣ 2.1 Losses and benefits ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints").
Let 𝔅(.)(N,Y1,…,YN,.)\mathfrak{B}^{(\text{.})}\left(N,Y\_{1},\dots,Y\_{N},.\right) be the insurance benefit (indemnity) paid by the insurer against the aggregate loss SS.

We compare two stylized benefit structures. In the traditional indemnity design,
𝔅(d)​(N,Y1,…,YN,d)\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right), the insurer indemnifies the realized loss above a deductible dd:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔅(d)​(N,Y1,…,YN,d)=∑i=1N(Yi−d)+,(a−b)+=max⁡(a−b,0).\displaystyle\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right)=\sum\_{i=1}^{N}(Y\_{i}-d)\_{+},\qquad(a-b)\_{+}=\max(a-b,0). |  | (2.2) |

In the parametric design,
𝔅(p)​(N,Y1,…,YN,k)\mathfrak{B}^{(\text{p})}\left(N,Y\_{1},\dots,Y\_{N},k\right), the insurer pays a constant amount kk per event regardless of the realized severity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔅(p)​(N,Y1,…,YN,k)=∑i=1Nk=k​N.\displaystyle\mathfrak{B}^{(\text{p})}\left(N,Y\_{1},\dots,Y\_{N},k\right)=\sum\_{i=1}^{N}k=kN. |  | (2.3) |

Because the parametric payment depends on NN but not on the individual severities YiY\_{i}, we henceforth write 𝔅(p)​(N,k)\mathfrak{B}^{(\text{p})}\left(N,k\right) to emphasize that its residual uncertainty is driven entirely by the event count. In practice, what constitutes an increment of NN is defined by an objective trigger based on event characteristics (e.g. flood depth or wind speed), rather than on the monetary loss YiY\_{i} itself (e.g. the cost of repairing a house).

The parametric structure also has operational implications. Because 𝔅(p)​(N,k)\mathfrak{B}^{(\text{p})}\left(N,k\right) does not require an assessment of YiY\_{i}, claims handling can be fast and inexpensive provided the trigger defining NN is transparent and verifiable. Two examples illustrate this mechanism. FloodFlash is a parametric flood cover available in the UK and the US: a device attached to the insured property measures flood depth and pays predetermined amounts as a function of observed water height.222FloodFlash offers products for both individuals and businesses, though marketing materials appear primarily targeted at commercial customers. Redicova is a parametric cyclone cover available in Australia (mainly in Queensland), where the trigger is defined using wind speed (as measured by the Australian Bureau of Meteorology) and location; typical insureds include banana farmers. These operational differences motivate allowing the premium structures of the two products to differ; see Section [2.4](https://arxiv.org/html/2512.21973v1#S2.E4 "In 2.2 Premia ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")–[2.5](https://arxiv.org/html/2512.21973v1#S2.E5 "In 2.2 Premia ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints") below.

A salient difference is that the parametric design can overpay relative to realized damage: if k>Yik>Y\_{i}, the insured makes a profit on that event. This issue is mitigated in the catastrophic-risk applications that motivate this paper. First, for disasters such as floods, cyclones/hurricanes/typhoons, and bushfires/wildfires, the insured has no meaningful control over the incidence of events, so classical moral-hazard concerns with respect to NN are limited.333By contrast, moral hazard can be more salient under indemnity: generous coverage may weaken incentives to mitigate severity (e.g. by undertaking protective measures), and slow or contested loss adjustment can create opportunities for exaggeration or fraud in large-loss settings. Second, the demand for parametric cover is most relevant precisely when full traditional insurance is unaffordable or unavailable because losses are deemed effectively uninsurable; in that regime, severities YiY\_{i} are typically so large that they will exceed any affordable per-event payment kk, making both the likelihood and the magnitude of “profit” cases small.

Finally, while we adopt the simplest parametric structure 𝔅(p)​(N,k)\mathfrak{B}^{(\text{p})}\left(N,k\right), the framework naturally extends to more general indemnity functions. For instance, one may allow a piecewise-constant benefit schedule kjk\_{j} (as in FloodFlash, where payouts depend on flood depth). Such an extension has three implications. (i) It introduces dependence between the trigger and payment levels, complicating calculations because correlations between NN and the benefit must be tracked. (ii) It reduces basis risk (see Remark [2.2](https://arxiv.org/html/2512.21973v1#S2.Thmremark2 "Remark 2.2 (Basis risk and richer parametric designs). ‣ 2.1 Losses and benefits ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")). (iii) It increases expected utility by reducing the volatility of net losses. Since (ii)–(iii) make parametric insurance more attractive, we deliberately focus on the most conservative benchmark 𝔅(p)​(N,k)\mathfrak{B}^{(\text{p})}\left(N,k\right): any welfare gains established in this setting should be interpreted as lower bounds for designs with richer payout functions.

###### Remark 2.1 (Event-level versus claim-level deductibles).

Classical results due to Borch ([1960](https://arxiv.org/html/2512.21973v1#bib.bib5), [1962](https://arxiv.org/html/2512.21973v1#bib.bib6), [1974](https://arxiv.org/html/2512.21973v1#bib.bib7)) and Arrow ([1963](https://arxiv.org/html/2512.21973v1#bib.bib1), [1971](https://arxiv.org/html/2512.21973v1#bib.bib2)) show that, under concave preferences and linear pricing, the optimal insurance contract is an excess-of-loss contract with a deductible. In the standard setting where each loss-causing event generates at most one claim, a per-claim deductible coincides with a per-event deductible, and per-claim excess-of-loss coverage is optimal because it insures the largest losses.

If a single event may generate multiple claims, this equivalence breaks down. The relevant loss to consider is then the aggregate event loss rather than the individual claim. In that setting, the appropriate benchmark for optimal design is a per-event excess-of-loss contract that pools all claims from the same underlying cause and covers the tail of the pooled loss.

In our comparisons, we abstract from this distinction and treat NN as the relevant count of losses. This simplification does not invalidate the welfare comparison; if anything, when per-claim deductibles are no longer optimal, it becomes easier for parametric insurance to dominate a (now) suboptimal deductible benchmark, all else equal.

###### Remark 2.2 (Basis risk and richer parametric designs).

Huang and Shi ([2024](https://arxiv.org/html/2512.21973v1#bib.bib13), in a mean-variance setting similar to ours) compare indemnity insurance with index insurance. They show that improving the index reduces basis risk and brings the parametric cover closer to indemnity in expected-utility terms. Their results, therefore, support an important implication for our analysis: moving beyond the constant benefit kk and reducing basis risk through index triggers or richer indemnity functions can make the welfare case for parametric insurance even more compelling.

In practice, basis risk can arise from misalignment in both YiY\_{i} and NN, because the trigger is typically defined using an auxiliary indicator (e.g., wind speed) rather than the presence and magnitude of actual loss. That said, FloodFlash requires proof of (any) actual damage before payment in the US (a requirement that does not exist in the UK), which materially reduces basis risk on NN.

Our optimization below focuses on the utility loss from basis risk in YiY\_{i}. A more general setup could model two dependent processes NtrueN\_{\text{true}} and NtriggerN\_{\text{trigger}}, with 𝔅(d)​(N,Y1,…,YN,d)\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right) formulated on NtrueN\_{\text{true}} and 𝔅(p)​(N,k)\mathfrak{B}^{(\text{p})}\left(N,k\right) on NtriggerN\_{\text{trigger}}. When (Ntrue,Ntrigger)(N\_{\text{true}},N\_{\text{trigger}}) form dependent compound Poisson processes, the claim counts decompose into common and idiosyncratic components, and calculations remain straightforward.

### 2.2 Premia

For the traditional indemnity benefit 𝔅(d)​(N,Y1,…,YN,d)\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right) we define the premium under the expectation principle as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒫(d)​(d;θd,γd)\displaystyle\mathcal{P}^{(\text{d})}\left(d;\theta\_{d},\gamma\_{d}\right) | =(1+θd)​(E​[𝔅(d)​(N,Y1,…,YN,d)]+γd)=(1+θd)​(E​[(Yi−d)+]​E​[N]+γd),\displaystyle=(1+\theta\_{d})\bigl(E[\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right)]+\gamma\_{d}\bigr)=(1+\theta\_{d})\bigl(E[(Y\_{i}-d)\_{+}]E[N]+\gamma\_{d}\bigr), |  | (2.4) |

where θd\theta\_{d} is a loading factor and γd\gamma\_{d} captures additional expenses not directly proportional to losses (including the “unallocated loss adjustment expenses” (ULAE) and other overheads).

For the parametric benefit 𝔅(p)​(N,k)\mathfrak{B}^{(\text{p})}\left(N,k\right) we analogously set

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒫(p)​(k;θp,γp)\displaystyle\mathcal{P}^{(\text{p})}\left(k;\theta\_{p},\gamma\_{p}\right) | =(1+θp)​(E​[𝔅(p)​(N,k)]+γp)=(1+θp)​(k​E​[N]+γp),\displaystyle=(1+\theta\_{p})\bigl(E[\mathfrak{B}^{(\text{p})}\left(N,k\right)]+\gamma\_{p}\bigr)=(1+\theta\_{p})\bigl(kE[N]+\gamma\_{p}\bigr), |  | (2.5) |

with loading θp\theta\_{p} and fixed-cost component γp\gamma\_{p} for ULAE. We treat the fixed-cost component as requiring risk capital. Consequently, it is included in the expected-value premium principle and therefore also risk-loaded. Under this interpretation, for each premium the resulting minimum premium (1+θ)​γ(1+\theta)\gamma reflects the insurer’s cost-of-risk requirements even in low-loss regimes.

The loading is intended to compensate the insurer for bearing risk beyond the expected claim cost. In practice, one expects θd>θp\theta\_{d}>\theta\_{p}. Intuitively, the indemnity contract 𝔅(d)​(⋅)\mathfrak{B}^{(\text{d})}\left(\cdot\right) covers the right tail of severity outcomes (losses beyond dd), precisely the component that matters most for a risk-averse insured and underlies the classical optimality of deductibles. From the insurer’s perspective, however, tail exposure increases required capital: right-tail quantiles of per-policy benefits are higher under 𝔅(d)​(⋅)\mathfrak{B}^{(\text{d})}\left(\cdot\right) than under 𝔅(p)​(⋅)\mathfrak{B}^{(\text{p})}\left(\cdot\right), so a higher loading is economically justified.

Similarly, one typically expects γd>γp\gamma\_{d}>\gamma\_{p} for three related reasons. First, loss adjustment for indemnity insurance is costlier: assessing and settling 𝔅(d)​(⋅)\mathfrak{B}^{(\text{d})}\left(\cdot\right) requires measuring actual damages, and catastrophe environments exacerbate these costs because claims are numerous, access can be difficult, and disputes are more likely. Second, post-disaster reconstruction costs often exceed pre-loss insured values due to demand surges for labor and materials; some markets reflect this in policies that pay up to (say) 125%125\% of insured value after major events. Under expectation pricing, an up-scaling of YiY\_{i} increases the expected indemnity cost and can therefore be represented as an additive component in the premium that we absorb into γd\gamma\_{d}.444If pricing involved explicit variance loading or risk measures, the treatment would need to distinguish cost-level changes from risk-level changes, and γ\gamma would no longer be a sufficient reduced-form summary. Third, indemnity claims typically take a long time to settle; even when delays translate into direct costs (e.g. temporary accommodation) captured by the first component, they also justify an additional frictional penalty reflected by γd\gamma\_{d}.

In ([2.4](https://arxiv.org/html/2512.21973v1#S2.E4 "In 2.2 Premia ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints"))–([2.5](https://arxiv.org/html/2512.21973v1#S2.E5 "In 2.2 Premia ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) the fixed-cost terms γ⋅\gamma\_{\cdot} do not multiply E​[N]E[N]. While the first two components above are plausibly proportional to the number of events, the third is not. A fully disaggregated model would therefore introduce multiple fixed-cost parameters. We adopt the reduced-form specification for two reasons: it keeps the analysis transparent, and it allows γd\gamma\_{d} (especially when γp≡0\gamma\_{p}\equiv 0) to serve as a single quantitative proxy for operational frictions that differentiate indemnity from parametric insurance. Moreover, interpreting γ\gamma as a per-period penalty (rather than per-event) is often more natural in household contexts. A per-event formulation can be recovered by rescaling by 1/E​[N]=1/λ1/E[N]=1/\lambda if desired.555Equivalently, one may interpret γ\gamma as already incorporating the relevant scaling given the typical event frequency in the market considered.

Note that conceptually the spread in γ\gamma’s pertain to differences in expected loss, whereas the spread in θ\theta’s pertain to risk premium (the cost of protecting the insurer).

### 2.3 Decision making criteria

The agent evaluates insurance choices using a mean–variance objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | MV(.)⁡(W;β)=E​[W]−β⋅Var⁡(W),β>0,\displaystyle\operatorname{MV}^{(\text{.})}\left(W;\beta\right)=E[W]-\beta\cdot\operatorname{Var}(W),\qquad\beta>0, |  | (2.6) |

where terminal wealth is

|  |  |  |  |
| --- | --- | --- | --- |
|  | W=w0−𝒫(.)(⋅;⋅)−S+𝔅(.)(N,Y1,…,YN,.),\displaystyle W=w\_{0}-\mathcal{P}^{(\text{.})}\left(\cdot;\cdot\right)-S+\mathfrak{B}^{(\text{.})}\left(N,Y\_{1},\dots,Y\_{N},.\right), |  | (2.7) |

and w0w\_{0} denotes initial wealth.

A technical feature of mean–variance preferences is that the variance term has units of currency squared, whereas the expectation has units of currency. A common normalization is therefore to scale risk aversion by wealth and set

|  |  |  |  |
| --- | --- | --- | --- |
|  | β=1w0,\beta=\frac{1}{w\_{0}}, |  | (2.8) |

which ensures that both terms in the objective are comparable and aligns with interpreting variance as a relative dispersion measure. In static optimization, this normalization can always be absorbed into the calibration of β\beta in numerical work. In dynamic settings, the normalization becomes more delicate; examples from mathematical finance include Jin and Zhou ([2004](https://arxiv.org/html/2512.21973v1#bib.bib15)), Xu and Zhou ([2014](https://arxiv.org/html/2512.21973v1#bib.bib21)), and Björk et al. ([2014](https://arxiv.org/html/2512.21973v1#bib.bib4)), who scale the variance by wealth similarly to us.

Each insurance design has a single contract parameter to be chosen. We define the optimal deductible and optimal parametric payment by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗=arg⁡maxd⁡MV(d)⁡(W;d,β,θd,γd),k∗=arg⁡maxk⁡MV(p)⁡(W;k,β,θp,γp).\displaystyle d^{\*}=\arg\max\_{d}\ \operatorname{MV}^{(\text{d})}\left(W;d,\beta,\theta\_{d},\gamma\_{d}\right),\qquad k^{\*}=\arg\max\_{k}\ \operatorname{MV}^{(\text{p})}\left(W;k,\beta,\theta\_{p},\gamma\_{p}\right). |  | (2.9) |

Closed-form expressions for expected payouts, second moments, and the resulting mean–variance objectives under censored exponential severity and Poisson frequency are collected in Appendix [A](https://arxiv.org/html/2512.21973v1#S1a "A Moments and mean–variance objectives under censored exponential severity ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints").

### 2.4 Research question: indemnity vs parametric insurance

Under the expectation premium principle, where the premium loading is proportional to expected loss, classical results imply that the deductible structure 𝔅(d)​(N,Y1,…,YN,d)\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right) is optimal under expected-utility maximization; see Borch ([1969](https://arxiv.org/html/2512.21973v1#bib.bib8)); Arrow ([1974](https://arxiv.org/html/2512.21973v1#bib.bib3)). Our goal is to revisit this benchmark in settings motivated by catastrophic household risks, where the traditional paradigm is strained by affordability, availability, and operational frictions.

The key economic motivation is that indemnity insurance is typically priced and designed to cover (or at least credibly underwrite) the full underlying loss distribution. When full cover becomes unaffordable, the main actuarial lever to reduce the premium is to increase the deductible—often to levels that are difficult to interpret as meaningful household protection (a mechanism we will illustrate numerically). By contrast, parametric insurance is naturally scalable: the insured can purchase a modest layer of per-event protection kk at a correspondingly modest premium, and the benefit can be paid quickly upon verification of the trigger, without requiring the household to incur a huge out-of-pocket loss before receiving any payment.

This paper, therefore, investigates whether and when parametric insurance can be optimal (or welfare-improving) once realistic frictions and constraints are introduced. Concretely, we allow for (i) differences in operational and settlement frictions summarized by fixed-cost terms γd\gamma\_{d} and γp\gamma\_{p}; (ii) potentially different loadings θd\theta\_{d} and θp\theta\_{p} reflecting different capital requirements and severity-risk exposures; and (iii) explicit premium budget constraints that may bind for households in high-risk regions. Finally, the question is timely in light of emerging policy discussions around parametric home insurance for catastrophic perils. For example, in some jurisdictions (e.g. Australia; see Jarzabkowski et al., [2024](https://arxiv.org/html/2512.21973v1#bib.bib14)) there are calls for the introduction of parametric home insurance for catastrophic risks such as floods, cyclones, or bushfires. The subsequent sections analyze these mechanisms theoretically and numerically.

## 3 Explicit results in the compound Poisson case

In this section, we make specific assumptions about the distributions of NN and YiY\_{i} to obtain explicit results for the optimal strategy parameters, as well as the corresponding premia and expected utility levels.

### 3.1 Dual relationship between d∗d^{\*} and k∗k^{\*} in the compound Poisson case

We now assume that the claim count NN is Poisson distributed with mean λ\lambda, so that the aggregate loss S=∑i=1NYiS=\sum\_{i=1}^{N}Y\_{i} follows a compound Poisson distribution. Under this assumption, and provided that preferences are
described by the mean–variance objective, and insurance premiums are calculated according to the expectation principle, we obtain explicit and straightforward expressions for both the optimal deductible d∗d^{\*} and the optimal parametric per–event cover k∗k^{\*}. We further assume that θd=θp\theta\_{d}=\theta\_{p}.

The key mathematical property underlying these results is the equi-dispersion identity for Poisson random variables,

|  |  |  |
| --- | --- | --- |
|  | Var⁡(N)=E​[N]=λ,\displaystyle\operatorname{Var}(N)=E[N]=\lambda, |  |

which implies that the variance of a random sum of i.i.d. terms reduces to

|  |  |  |
| --- | --- | --- |
|  | Var⁡(∑i=1NYi)=λ​E​[Yi2].\displaystyle\operatorname{Var}\!\left(\sum\_{i=1}^{N}Y\_{i}\right)=\lambda\,E[Y\_{i}^{2}]. |  |

This linear structure ensures that, under the mean–variance objective, the variance component of terminal wealth does not depend on nonlinear interactions between the distribution of NN and the deductible or per–event cover.

In Appendix [B](https://arxiv.org/html/2512.21973v1#S2a "B Duality: 𝐸⁢[𝑌_𝑖]=𝑑^∗+𝑘^∗ ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints"), we show that, under the combined assumptions of
(i) the mean–variance objective,
(ii) the Poisson claim number model, and
(iii) the expectation principle for premiums,
the first-order conditions for the two optimization problems reduce to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗=θ2​β,k∗=E​[Yi]−θ2​β,\displaystyle d^{\*}=\frac{\theta}{2\beta},\qquad k^{\*}=E[Y\_{i}]-\frac{\theta}{2\beta}, |  | (3.1) |

when the loading factors coincide, i.e., θd=θp=θ\theta\_{d}=\theta\_{p}=\theta. Importantly, these expressions do not depend on the distributional form of the claim severity, as long as it has a finite second moment.

A direct implication is the following duality identity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[Yi]=d∗+k∗.E[Y\_{i}]=d^{\*}+k^{\*}. |  | (3.2) |

This relation has a natural economic interpretation: d∗d^{\*} is the optimal amount of protection removed from full insurance, whereas k∗k^{\*} is the optimal amount of protection added from no cover. The two adjustments sum precisely to the mean insured loss.

It is crucial to emphasize that the duality is not universal. As detailed in Appendix [B](https://arxiv.org/html/2512.21973v1#S2a "B Duality: 𝐸⁢[𝑌_𝑖]=𝑑^∗+𝑘^∗ ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints"), the identity relies essentially on all three
assumptions listed above. If one replaces the expectation principle by any premium calculation involving variance loading or risk measures, or if NN does not satisfy
Var⁡(N)=E​[N]\operatorname{Var}(N)=E[N], the optimality conditions no longer reduce to the simple linear forms above, and the duality identity fails. We also stress that the dualty relation is based on interior solutions, i.e., no budget or risk constraints.

###### Remark 3.1.

Interestingly γ⋅\gamma\_{\cdot} does not feature in ([3.1](https://arxiv.org/html/2512.21973v1#S3.E1 "In 3.1 Dual relationship between 𝑑^∗ and 𝑘^∗ in the compound Poisson case ‣ 3 Explicit results in the compound Poisson case ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")). This is because it affects expected wealth but not the insured’s marginal risk–return trade-off. Under mean–variance preferences and expectation-principle pricing, optimal contract parameters are determined entirely by marginal premium loadings and variance reduction, so additive premium components vanish from the first-order conditions.

### 3.2 Optimal results under censored exponential losses

Assume now that YiY\_{i} is a censored exponential random variable with mixed density

|  |  |  |  |
| --- | --- | --- | --- |
|  | fYi​(y)={ν​e−ν​y,y∈[0,L);e−ν​L,y=L;0,otherwise.f\_{Y\_{i}}(y)=\begin{cases}\nu e^{-\nu y},&y\in[0,L);\\ e^{-\nu L},&y=L;\\ 0,&\text{otherwise}.\end{cases} |  | (3.3) |

This structure is justified by property insurance, which typically has a limited sum at risk LL (the value of the property). Furthermore, there will typically be a positive probability of complete write-off (here e−ν​Le^{-\nu L}). Of course, the exponential assumption here simplifies some calculations, but it is not unreasonable in an insurance context, and we don’t expect that the use of a more sophisticated distribution would materially alter our conclusions.

###### Remark 3.2.

The limit LL is formulated on the loss. A policy limit MM would be applied on the benefit 𝔅(.)(N,Y1,…,YN,.)\mathfrak{B}^{(\text{.})}\left(N,Y\_{1},\dots,Y\_{N},.\right) such that Yi−dY\_{i}-d (the loss net of the deductible) would be capped at MM. Calculations can easily be extended to this case, but do not lead to materially different conclusions and hence have been omitted here.

###### Remark 3.3.

If ν⟶0\nu\longrightarrow 0 for fixed LL then the distribution in ([3.3](https://arxiv.org/html/2512.21973v1#S3.E3 "In 3.2 Optimal results under censored exponential losses ‣ 3 Explicit results in the compound Poisson case ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) becomes point-mass (LL with probability 1). In this case we retain E​[Yi]=L=d∗+k∗E[Y\_{i}]=L=d^{\*}+k^{\*}, however d∗≠k∗d^{\*}\neq k^{\*} in general. Both policies become identical, with payout k∗=L−d∗k^{\*}=L-d^{\*} for each event.

Let YiY\_{i} have the density function of equation ([3.3](https://arxiv.org/html/2512.21973v1#S3.E3 "In 3.2 Optimal results under censored exponential losses ‣ 3 Explicit results in the compound Poisson case ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​FYi​(y)=ν​e−ν​y​d​y+e−ν​L​δL​(d​y).dF\_{Y\_{i}}(y)=\nu e^{-\nu y}\,dy+e^{-\nu L}\,\delta\_{L}(dy). |  | (3.4) |

From Appendix [A](https://arxiv.org/html/2512.21973v1#S1a "A Moments and mean–variance objectives under censored exponential severity ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints"), we have that the expected mean-variance of the indemnity cover is

|  |  |  |  |
| --- | --- | --- | --- |
|  | MV(d)⁡(W;d,β,θd,γd)=w0−𝒫(d)​(d;θd,γd)−λ​E​[Yi]+λ​E​[(Yi−d)+]−β​λ​2ν2​[1−e−ν​d​(1+ν​d)].\operatorname{MV}^{(\text{d})}\left(W;d,\beta,\theta\_{d},\gamma\_{d}\right)=w\_{0}-\mathcal{P}^{(\text{d})}\left(d;\theta\_{d},\gamma\_{d}\right)-\lambda E[Y\_{i}]+\lambda E[(Y\_{i}-d)\_{+}]-\beta\lambda\frac{2}{\nu^{2}}\big[1-e^{-\nu d}(1+\nu d)\big]. |  | (3.5) |

Differentiation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂MV(d)∂d=λ​e−ν​d​(θd−2​β​d),∂2MV(d)∂d2=λ​e−ν​d​(−ν​θd+2​ν​β​d−2​β),\frac{\partial\text{MV}^{(d)}}{\partial d}=\lambda e^{-\nu d}(\theta\_{d}-2\beta d),\qquad\frac{\partial^{2}\text{MV}^{(d)}}{\partial d^{2}}=\lambda e^{-\nu d}(-\nu\theta\_{d}+2\nu\beta d-2\beta), |  | (3.6) |

so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗=θd2​β,∂2MV(d)∂d2|d∗=−2​β​λ​e−ν​d∗<0.d^{\*}=\frac{\theta\_{d}}{2\beta},\qquad\frac{\partial^{2}\text{MV}^{(d)}}{\partial d^{2}}\Big|\_{d^{\*}}=-2\beta\lambda e^{-\nu d^{\*}}<0. |  | (3.7) |

On the other hand, the expected mean-variance of the parametric cover is

|  |  |  |  |
| --- | --- | --- | --- |
|  | MV(p)⁡(W;k,β,θp,γp)=w0−𝒫(p)​(k;θp,γp)−λ​E​[Yi]+λ​k−β​λ​(Var​(Yi)+(E​[Yi]−k)2);\operatorname{MV}^{(\text{p})}\left(W;k,\beta,\theta\_{p},\gamma\_{p}\right)=w\_{0}-\mathcal{P}^{(\text{p})}\left(k;\theta\_{p},\gamma\_{p}\right)-\lambda E[Y\_{i}]+\lambda k-\beta\lambda\big(\mathrm{Var}(Y\_{i})+(E[Y\_{i}]-k)^{2}\big); |  | (3.8) |

see Appendix [A](https://arxiv.org/html/2512.21973v1#S1a "A Moments and mean–variance objectives under censored exponential severity ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints"). Differentiation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂MV(p)∂k=λ​(−θp+2​β​(E​[Yi]−k)),∂2MV(p)∂k2=−2​β​λ<0,\frac{\partial\text{MV}^{(p)}}{\partial k}=\lambda(-\theta\_{p}+2\beta(E[Y\_{i}]-k)),\qquad\frac{\partial^{2}\text{MV}^{(p)}}{\partial k^{2}}=-2\beta\lambda<0, |  | (3.9) |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | k∗=E​[Yi]−θp2​β.k^{\*}=E[Y\_{i}]-\frac{\theta\_{p}}{2\beta}. |  | (3.10) |

### 3.3 Robustness and modeling choices

The modeling choices adopted here are deliberately conservative. The parametric contract is specified as a constant per-event payment, which maximizes basis risk and therefore places parametric insurance at a theoretical disadvantage relative to indemnity insurance. Allowing for more flexible parametric designs—such as piecewise-constant payouts or index-linked triggers—would mechanically reduce basis risk. Therefore, it is unlikely to overturn our conclusions.

Similarly, the censored exponential severity distribution is neither light- nor heavy-tailed, and serves primarily to deliver closed-form expressions. In environments with heavier-tailed losses, the capital intensity and fixed costs of indemnity insurance are likely to be even more pronounced, strengthening the relative appeal of parametric
coverage under budget constraints.

## 4 Numerical illustrations

This section illustrates the welfare comparison between indemnity (excess-of-loss) and parametric insurance in a low-frequency, high-severity environment, using the closed-form expressions derived in Sections [2](https://arxiv.org/html/2512.21973v1#S2 "2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")–[3](https://arxiv.org/html/2512.21973v1#S3 "3 Explicit results in the compound Poisson case ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints") (and implemented in the companion numerical appendix).
Throughout, we report mean–variance (MV) values, with larger values corresponding to higher welfare.

### 4.1 Baseline calibration

Consider a household with a house worth $500,000. Their wealth corresponds to 30% of the value of the house, that is, $150,000. The house is built in a flood plain with a 1-in-50-year chance of severe flooding (λ=1/50\lambda=1/50). Such an event will happen at least twice in a lifetime (of 80 years) with probability 48%.

Should such a flood occur, damages to the house follow the distribution in ([3.3](https://arxiv.org/html/2512.21973v1#S3.E3 "In 3.2 Optimal results under censored exponential losses ‣ 3 Explicit results in the compound Poisson case ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")), with ν=1/350,000\nu=1/350,000. This means E​[Yi]=$​266,122E[Y\_{i}]=\mathdollar 266,122, and the probability of a complete write-off is Pr⁡[Yi=L]=24%\Pr[Y\_{i}=L]=24\%. Importantly, a large amount of loss density is in its tail, which will naturally favor an excess-of-loss cover over a parametric cover.

This set-up corresponds to a realistic flood risk scenario. In Ipswich (Queensland, Australia), a 1-in-50-year event corresponds to a gauge at 18.7m in its CBD (Queensland Reconstruction Autority, [2019](https://arxiv.org/html/2512.21973v1#bib.bib18)). This is a similar level to that observed in the 2011 floods in this region, which saw many homes completely written off.

### 4.2 Unconstrained optima and one-dimensional comparative statics

We begin by considering the case γp≡0\gamma\_{p}\equiv 0 and θd=θp≡θ=0.3\theta\_{d}=\theta\_{p}\equiv\theta=0.3. Whence, we compare the expected mean-variance utility of both covers for varying levels of γd≥0\gamma\_{d}\geq 0. In this case,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗=$​22,500 and k∗=$​243,622.d^{\*}=\mathdollar 22,\!500\quad\text{ and }\quad k^{\*}=\mathdollar 243,\!622. |  | (4.1) |

Corresponding premiums are (at the baseline γd=0\gamma\_{d}=0)

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫(d)​(d∗;θ,0)=$​6,353 and 𝒫(p)​(k∗;θ,0)=$​6,334.\mathcal{P}^{(\text{d})}\left(d^{\*};\theta,0\right)=\mathdollar 6,\!353\quad\text{ and }\quad\mathcal{P}^{(\text{p})}\left(k^{\*};\theta,0\right)=\mathdollar 6,\!334. |  | (4.2) |

Figure [1](https://arxiv.org/html/2512.21973v1#S4.F1 "Figure 1 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")(a) shows levels of premium as per ([2.4](https://arxiv.org/html/2512.21973v1#S2.E4 "In 2.2 Premia ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints"))-([2.5](https://arxiv.org/html/2512.21973v1#S2.E5 "In 2.2 Premia ‣ 2 Theoretical framework for traditional indemnity and parametric insurance ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) at the bottom (coordinates on the left). The premium for the indemnity insurance increases linearly with γd\gamma\_{d} with slope (1+θ)(1+\theta), whereas the premium for parametric insurance is not affected by γd\gamma\_{d} and remains constant. The expected mean-variance functions are shown in green and purple, respectively. The level of γd\gamma\_{d} that makes an agent indifferent between either coverage is $3,239. If one forces the agent to spend as much on the parametric cover as they spend on the indemnity cover (increasing kk beyond its optimal level), the corresponding expected mean-variance (in orange) decreases until k=Lk=L and no additional cover can be purchased, after which it stays constant. Under such a scheme, the level of γd\gamma\_{d} that makes the agent indifferent between the two covers is larger and sits at $9,980.

![Refer to caption](fig_gamma_1d.png)

(a) One-dimensional comparative statics in γd\gamma\_{d}: premiums and
mean–variance at unconstrained optima d∗​(θ)d^{\*}(\theta) and k∗​(θ)k^{\*}(\theta).

![Refer to caption](fig_surface_d_gamma_premiummatch.png)

(b) Premium-matching surface over (d,γd)(d,\gamma\_{d}): positive part of
M​V(p)−M​V(d)MV^{(p)}-MV^{(d)}, with the cap region {k=L}\{k=L\} highlighted on the floor.

Figure 1: Comparison of indemnity and parametric insurance under premium
matching. Panel (a) shows one-dimensional comparative statics in the
indemnity fixed cost γd\gamma\_{d}, while panel (b) extends the comparison to
the two-dimensional (d,γd)(d,\gamma\_{d}) space and highlights the region in which
parametric insurance yields higher mean–variance utility.

The idea of varying kk to match premia is generalized in Figure [1](https://arxiv.org/html/2512.21973v1#S4.F1 "Figure 1 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")(b). For each grid point (d,γd)(d,\gamma\_{d}) we compute the indemnity premium π(d)​(d;θd,γd)\pi^{(d)}(d;\theta\_{d},\gamma\_{d}) and choose the parametric payment

|  |  |  |  |
| --- | --- | --- | --- |
|  | k​(d,γd)=min⁡{𝒫(d)​(d;θd,γd)/(1+θp)−γpλ,L},k(d,\gamma\_{d})=\min\!\left\{\frac{\mathcal{P}^{(\text{d})}\left(d;\theta\_{d},\gamma\_{d}\right)/(1+\theta\_{p})-\gamma\_{p}}{\lambda},\,L\right\}, |  | (4.3) |

so that the parametric premium matches the indemnity premium whenever the implied kk lies below LL. The MV difference surface then plots
M​V(p)​(k​(d,γd);θp,γp)−M​V(d)​(d;θd,γd)MV^{(p)}(k(d,\gamma\_{d});\theta\_{p},\gamma\_{p})-MV^{(d)}(d;\theta\_{d},\gamma\_{d}), truncated at zero so that only regions where parametric is strictly better remain visible.

When k​(d,γd)<Lk(d,\gamma\_{d})<L, the mapping in ([4.3](https://arxiv.org/html/2512.21973v1#S4.E3 "In 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) is smooth and the MV difference varies smoothly in (d,γd)(d,\gamma\_{d}). When the implied payment exceeds LL, the constraint k≤Lk\leq L binds, creating a corner solution: parametric protection cannot increase further even if the indemnity premium continues to increase. In the corresponding surface plots, we explicitly mark the set {(d,γd):k​(d,γd)=L}\{(d,\gamma\_{d}):k(d,\gamma\_{d})=L\} (the cap region) in black on the “floor”. The black region, therefore, identifies where the premium-matching rule hits the parametric maximum payment, not where the MV difference is negative.

One can see that the indemnity cover is indeed always optimal for
γ=0\gamma=0, but it becomes suboptimal for tiny γ\gamma’s already when
dd is very suboptimal (large).

An analogous construction applies over (θd,γd)(\theta\_{d},\gamma\_{d}), where indemnity is evaluated at d∗​(θd)d^{\*}(\theta\_{d}) and parametric is premium-matched to 𝒫(d)​(d∗​(θd);θd,γd)\mathcal{P}^{(\text{d})}\left(d^{\*}(\theta\_{d});\theta\_{d},\gamma\_{d}\right), yielding a surface in the fundamental pricing parameter θd>θp=0.2\theta\_{d}>\theta\_{p}=0.2 (cost of coverage) rather than contract parameters. Here γd=γp=0\gamma\_{d}=\gamma\_{p}=0.

The interpretation of Figure [2](https://arxiv.org/html/2512.21973v1#S4.F2 "Figure 2 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints") is analogous to that of Figure [1](https://arxiv.org/html/2512.21973v1#S4.F1 "Figure 1 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints"). Here, the θd\theta\_{d} that leads to indifference between both covers is 1.291.29 without premium matching, and 1.571.57 with premium matching. It can be shown that such a root exists and is unique on the range of sensible values for θ\theta (those that lead to d∗≤Ld^{\*}\leq L).

Figure [2](https://arxiv.org/html/2512.21973v1#S4.F2 "Figure 2 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints") illustrates how the welfare
comparison between indemnity and parametric insurance evolves as the
indemnity pricing parameters change. While panel (a) highlights the
non-monotonic behavior of premium-matched parametric utility as a function
of θd\theta\_{d}, panel (b) shows that this mechanism persists once fixed costs
γd\gamma\_{d} are introduced, and identifies the region in which parametric
insurance dominates under equal-premium constraints.

![Refer to caption](fig_theta_1d.png)

(a) One-dimensional comparative statics in the indemnity loading
θd\theta\_{d}: premiums and mean–variance at unconstrained optima
d∗​(θd)d^{\*}(\theta\_{d}) and k∗​(θp)k^{\*}(\theta\_{p}), together with the premium-matched
parametric value M​Vp(budget ​Pd)MV\_{p}^{(\text{budget }P\_{d})}.

![Refer to caption](fig_surface_theta_gamma_premiummatch.png)

(b) Premium-matching surface over (θd,γd)(\theta\_{d},\gamma\_{d}):
The parametric contract is calibrated to match the premium of the
optimal indemnity contract d∗​(θd)d^{\*}(\theta\_{d}) at each point.
The surface shows the positive part of M​V(p)−M​V(d)MV^{(p)}-MV^{(d)}.

Figure 2: Premium matching in the space of indemnity pricing parameters.
Panel (a) shows how premiums and mean–variance utilities vary with the
indemnity loading θd\theta\_{d} in one dimension. Panel (b) extends the
comparison to the two-dimensional (θd,γd)(\theta\_{d},\gamma\_{d}) space and
identifies regions in which the premium-matched parametric contract
delivers higher mean–variance utility than the optimal indemnity contract.



![Refer to caption](fig_budget_1d_dualaxis.png)

(a) Fixed γd\gamma\_{d}: effective premiums (left axis) and
budget-constrained mean–variance values (right axis) as functions of the
available premium budget P¯\bar{P}. Vertical lines indicate
PdminP\_{d}^{\min}, Pd∗P\_{d}^{\*}, Pp∗P\_{p}^{\*}, and the indifference budget
P¯indif\bar{P}\_{\mathrm{indif}} (when it exists).

![Refer to caption](fig_budget_gamma_surface_pos.png)

(b) Positive region of
Δ​M​V​(P¯,γd)\Delta MV(\bar{P},\gamma\_{d}) in ([4.6](https://arxiv.org/html/2512.21973v1#S4.E6 "In 4.3 Budget-constrained choice and two-dimensional budget surfaces ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")):
parameter combinations for which the parametric contract yields strictly
higher mean–variance utility than the best available alternative
(indemnity within budget or no insurance).

Figure 3: Budget-constrained comparison of indemnity and parametric insurance.
Panel (a) illustrates how optimal contract choice and welfare evolve as the
available premium budget P¯\bar{P} increases for a fixed cost
γd\gamma\_{d}. Panel (b) extends the analysis to the two-dimensional
(P¯,γd)(\bar{P},\gamma\_{d}) space and highlights the region in which parametric
insurance strictly dominates the best budget-feasible alternative.

### 4.3 Budget-constrained choice and two-dimensional budget surfaces

We now adopt the comparison most relevant for affordability: an agent faces an exogenous premium budget P¯\bar{P} and chooses the best contract they can buy within that budget. Critically, the agent can always opt out and remain uninsured. This formulation captures the practical asymmetry: under indemnity pricing with fixed costs, low budgets may translate into either infeasibility or an effectively useless deductible layer, whereas the same budget translates mechanically into a positive parametric payment as long as P¯>(1+θp)​γp\bar{P}>(1+\theta\_{p})\gamma\_{p}.

For each P¯\bar{P}, the parametric choice solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​Vbud(p)​(P¯)=max⁡{M​V(0),max0≤k≤L:𝒫(p)​(k)≤P¯⁡M​V(p)​(k;θp,γp)}.MV^{(p)}\_{\mathrm{bud}}(\bar{P})=\max\Bigl\{MV^{(0)},\ \max\_{0\leq k\leq L:\ \mathcal{P}^{(p)}(k)\leq\bar{P}}MV^{(p)}(k;\theta\_{p},\gamma\_{p})\Bigr\}. |  | (4.4) |

Similarly, given (γd,θd)(\gamma\_{d},\theta\_{d}), the indemnity choice solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​Vbud(d)​(P¯,γd)=max⁡{M​V(0),max0≤d≤L:𝒫(d)​(d)≤P¯⁡M​V(d)​(d;θd,γd)}.MV^{(d)}\_{\mathrm{bud}}(\bar{P},\gamma\_{d})=\max\Bigl\{MV^{(0)},\ \max\_{0\leq d\leq L:\ \mathcal{P}^{(d)}(d)\leq\bar{P}}MV^{(d)}(d;\theta\_{d},\gamma\_{d})\Bigr\}. |  | (4.5) |

Because 𝒫(p)\mathcal{P}^{(p)} is affine in kk, the parametric constraint can be inverted explicitly. For indemnity, monotonicity of 𝒫(d)​(d)\mathcal{P}^{(d)}(d) in dd allows us to invert the constraint numerically (or in closed form under the censored exponential moments used here).

Figure [3](https://arxiv.org/html/2512.21973v1#S4.F3 "Figure 3 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")(a) fixes γd=1,000\gamma\_{d}=1,\!000 (and the remaining parameters) and plots, as functions of P¯\bar{P}: (i) the effective premium actually spent by each product (which can be strictly below P¯\bar{P} once the unconstrained optimum becomes affordable), and (ii) the corresponding budget-constrained mean–variance values M​Vbud(p)​(P¯)MV^{(p)}\_{\mathrm{bud}}(\bar{P}) and M​Vbud(d)​(P¯,γd)MV^{(d)}\_{\mathrm{bud}}(\bar{P},\gamma\_{d}). For tiny budgets, indemnity may be infeasible due to the additive friction: the minimum feasible indemnity premium at deductible LL is Pdmin​(γd)=𝒫(d)​(L;θd,γd)=(1+θd)​γd.P\_{d}^{\min}(\gamma\_{d})=\mathcal{P}^{(d)}(L;\theta\_{d},\gamma\_{d})=(1+\theta\_{d})\gamma\_{d}.
In that region, the best indemnity-or-no-insurance option is simply no insurance (M​V(0)MV^{(0)}), while parametric can already begin providing welfare gains if γp\gamma\_{p} is smaller and the linear premium constraint allows k>0k>0.

As P¯\bar{P} increases, parametric mean–variance typically rises and then flattens once the unconstrained k∗k^{\*} becomes affordable. Indemnity MV is flat at M​V(0)MV^{(0)} until P¯\bar{P} reaches Pdmin​(γd)P\_{d}^{\min}(\gamma\_{d}), and then increases as affordable deductibles begin to reduce variance efficiently. The two MV curves may cross at an indifference budget P¯indif\bar{P}\_{\mathrm{indif}}: parametric is better for small budgets, but indemnity dominates once a sufficient premium is available.

To generalize Figure [3](https://arxiv.org/html/2512.21973v1#S4.F3 "Figure 3 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")(a) across additive indemnity frictions, Figure [3](https://arxiv.org/html/2512.21973v1#S4.F3 "Figure 3 ‣ 4.2 Unconstrained optima and one-dimensional comparative statics ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")(b) plots the incremental welfare conferred by parametric insurance relative to the best alternative among “indemnity within budget” and “no insurance”:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​M​V​(P¯,γd)=M​Vbud(p)​(P¯)−M​Vbud(d)​(P¯,γd),shown only when ​Δ​M​V​(P¯,γd)>0.\Delta MV(\bar{P},\gamma\_{d})=MV^{(p)}\_{\mathrm{bud}}(\bar{P})-MV^{(d)}\_{\mathrm{bud}}(\bar{P},\gamma\_{d}),\qquad\text{shown only when }\Delta MV(\bar{P},\gamma\_{d})>0. |  | (4.6) |

The surface therefore appears exactly in the region where parametric insurance is strictly welfare-improving relative to the best feasible indemnity choice (including the option of not insuring at all). The surface is absent when Δ​M​V≤0\Delta MV\leq 0, which can occur for two distinct reasons:
(i) the budget is so small that both products optimally reduce to no insurance (so Δ​M​V=0\Delta MV=0), or
(ii) the budget is large enough (and/or γd\gamma\_{d} small enough) that a deductible contract becomes feasible and dominates parametric
(so Δ​M​V<0\Delta MV<0).
Importantly, when indemnity is infeasible because P¯<Pdmin​(γd)\bar{P}<P\_{d}^{\min}(\gamma\_{d}), we have M​Vbud(d)​(P¯,γd)=M​V(0)MV^{(d)}\_{\mathrm{bud}}(\bar{P},\gamma\_{d})=MV^{(0)} by construction, so parametric can indeed dominate in that region whenever it can deliver any strict improvement over M​V(0)MV^{(0)}.

For any fixed γd\gamma\_{d} slice of the surface in panel (b), ([4.6](https://arxiv.org/html/2512.21973v1#S4.E6 "In 4.3 Budget-constrained choice and two-dimensional budget surfaces ‣ 4 Numerical illustrations ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) reproduces the intuition in panel (a): the advantage of parametric typically starts at 0 when P¯=0\bar{P}=0, increases as small budgets allow meaningful parametric payments. At the same time, indemnity remains infeasible or dominated by no insurance, and then declines once indemnity becomes feasible and (eventually) overtakes parametric at higher budgets.

## 5 Policy implications

Our results have direct implications for disaster risk financing, insurance regulation, and the design of public–private risk-sharing mechanisms in high-risk environments. While the analysis is stylized, it highlights structural limitations of indemnity insurance that are most pronounced precisely in settings where risk transfer is most socially valuable.

### 5.1 Insurance failure in high-risk areas

A growing body of evidence indicates that indemnity insurance is becoming unaffordable or unavailable in regions exposed to severe natural hazards, such as floods, wildfires, and cyclones. In these areas, insurers either raise premiums sharply, impose large deductibles, or withdraw coverage altogether, as recently observed in parts of California’s wildfire market and in flood-prone regions worldwide.

Our analysis provides a microeconomic foundation for this phenomenon. Even when indemnity insurance remains theoretically optimal under expected utility maximization, realistic pricing frictions—such as fixed costs, higher capital requirements, and binding budget constraints—push optimal deductibles to levels that render coverage ineffective in practice. In such cases, indemnity insurance ceases to perform its primary economic function: smoothing consumption in adverse states of the world.

This distinction between theoretical optimality and economic relevance is crucial. A deductible that is optimal in a frictionless model may be so large that it offers little or no meaningful protection to households facing liquidity constraints. From a policy perspective, such outcomes should be interpreted as market failure, even if insurers remain solvent and contracts remain actuarially fair.

### 5.2 Parametric insurance as partial risk transfer

Within this context, parametric insurance emerges as a form of partial risk transfer that can dominate indemnity insurance once realistic constraints are acknowledged. While parametric contracts introduce basis risk and do not replicate loss-contingent indemnification, they avoid several frictions inherent to indemnity insurance.

First, parametric payouts can be structured to remain affordable even when indemnity premiums escalate. Because the insurer does not bear loss severity risk, capital requirements and associated loadings are lower (Cummins and Mahul, [2012](https://arxiv.org/html/2512.21973v1#bib.bib11)). Second, parametric contracts remain economically meaningful at low premium levels: even modest budgets translate into immediate protection, whereas indemnity insurance may offer no effective coverage until losses exceed a very high deductible.

Our results show that, under budget constraints, parametric insurance can deliver higher expected utility than the best feasible indemnity contract, even for risk-averse agents. This finding does not overturn the classical optimality of indemnity insurance in frictionless settings (Arrow, [1963](https://arxiv.org/html/2512.21973v1#bib.bib1); Raviv, [1979](https://arxiv.org/html/2512.21973v1#bib.bib19)); rather, it clarifies the economic conditions under which that result ceases to be policy-relevant.

### 5.3 Speed of payout, recovery, and resilience

An important policy dimension—only imperfectly captured in our utility framework—is the timing of payouts. Indemnity insurance typically involves claims assessment, verification, and reconstruction processes that can take months or years, particularly following large-scale disasters when local capacity is constrained (Kahn, [2021](https://arxiv.org/html/2512.21973v1#bib.bib16)).

Parametric insurance, by contrast, allows for rapid disbursement of funds, often within days or weeks of the triggering event (Clarke and Dercon, [2016](https://arxiv.org/html/2512.21973v1#bib.bib9)). Even if payouts are smaller or imperfectly aligned with actual losses, early liquidity can materially improve recovery outcomes. This suggests that the welfare gains from parametric insurance identified in our model may understate its broader social value.

From a public finance perspective, faster payouts may also reduce reliance on ad hoc government assistance and emergency relief, thereby lowering fiscal uncertainty and political pressure following disasters.

### 5.4 Reconstruction incentives and resilience investment

Indemnity insurance typically reimburses losses on a “like-for-like” basis, replacing damaged assets with their pre-disaster equivalents. While this aligns with traditional notions of indemnification, it can discourage investment in more resilient reconstruction. Improvements that reduce future vulnerability—such as flood-resilient materials or elevated structures—may not be fully covered if they exceed the cost of restoring the original asset.

Parametric insurance does not face this constraint. Because payouts are not tied to realized repair costs, households retain discretion over how funds are used. This flexibility creates opportunities for resilience-enhancing investments that would otherwise fall outside standard indemnity contracts. However, it also introduces a policy concern: there is no guarantee that parametric payouts will be used for reconstruction. If funds are diverted to consumption or debt repayment, future losses may increase, potentially shifting greater liability onto governments.

This highlights a role for complementary policy measures, such as resilience incentives, rebuilding guidelines, or conditional grants, to align private choices with social objectives (Hallegatte et al., [2019](https://arxiv.org/html/2512.21973v1#bib.bib12)).

### 5.5 Implications for insurance regulation

Our findings suggest that insurance regulation focused exclusively on indemnity products may be ill-suited for high-risk environments. Regulatory frameworks that implicitly privilege indemnity insurance—through capital rules, consumer protection standards, or product approval processes—may inadvertently suppress welfare-enhancing alternatives.

A more flexible regulatory approach would recognize parametric insurance as a distinct class of risk-transfer instruments rather than a second-best substitute for indemnity. This includes clarifying disclosure requirements around basis risk, ensuring contract transparency, and facilitating experimentation with hybrid designs that combine parametric triggers and partial indemnification (Huang and Shi, [2024](https://arxiv.org/html/2512.21973v1#bib.bib13)).

Importantly, the results caution against policies that seek to preserve the affordability of indemnity insurance at all costs, for example, through premium caps or cross-subsidies that obscure underlying risk. In settings where full indemnification is no longer economically viable, encouraging partial but
effective risk transfer may be preferable to maintaining the appearance of comprehensive coverage.

### 5.6 The role of government in enabling parametric markets

Finally, our analysis underscores a constructive role for governments in supporting parametric insurance markets without directly providing insurance. Governments can contribute by investing in high-quality hazard data, standardized indices, and transparent trigger definitions, all of which reduce
basis risk and transaction costs (World Bank, [2021](https://arxiv.org/html/2512.21973v1#bib.bib20)).

Recent Australian reviews illustrate this direction of travel: proposals have emphasized parametric options for household catastrophe protection alongside investments in hazard measurement and transparent triggers (Jarzabkowski et al., [2024](https://arxiv.org/html/2512.21973v1#bib.bib14)).

Rather than crowding out private insurance, well-designed parametric schemes can complement public disaster risk management by strengthening household
resilience and reducing long-term fiscal exposure. In this sense, parametric insurance should be viewed not as a replacement for indemnity insurance, but
as a policy-relevant addition to the menu of risk-transfer instruments in a changing climate.

## 6 Conclusion

This paper revisits the classical optimality of indemnity insurance in environments characterized by low-frequency, high-severity risk and binding budget constraints. While excess-of-loss indemnity contracts are well known to maximize expected utility under proportional premium loadings, we show that this benchmark can lose practical relevance when fixed costs, heterogeneous loadings, and affordability constraints are taken into account. In such settings, the deductible implied by utility maximization may become so large that indemnity insurance delivers little effective risk transfer, despite remaining formally optimal.

Within a tractable expected mean–variance framework, we compare indemnity and parametric insurance designs under a common objective and shared trigger. Allowing for realistic frictions that penalize indemnity insurance—including higher loadings, fixed costs, and delayed loss adjustment—we identify regions in which parametric contracts yield strictly higher welfare. These gains arise not because parametric insurance dominates indemnity insurance in general, but because it remains feasible and economically meaningful precisely when indemnity insurance becomes unaffordable or ineffective.

Our results highlight a non-monotonic welfare comparison between the two designs. Parametric insurance may dominate at low premium budgets, lose its advantage as indemnity insurance becomes viable, and eventually become irrelevant once both contracts are unconstrained. This pattern helps reconcile classical insurance theory with the observed resurgence of parametric risk transfer in high-risk environments.

The analysis has direct implications for disaster risk financing and insurance market design. As climate change and urban development expand the set of regions where full indemnification is no longer viable, policies that focus exclusively on restoring traditional indemnity insurance may be insufficient. Parametric insurance should instead be viewed as a complementary instrument that can improve individual welfare and resilience when standard contracts fail. Future research could extend the framework to richer utility specifications, endogenous risk mitigation, and hybrid insurance designs that combine parametric and indemnity elements.

## Acknowledgements

Avanzi acknowledges support under the Australian Research Council’s Discovery Project (DP200101859) funding scheme. The views and opinions expressed in this paper are solely those of the authors and do not reflect those of their affiliated institutions.

## Data availability statement

All results in this paper are reproducible using R, with code available on GitHub at <https://github.com/agi-lab/parametric>.

## References

## References

* Arrow (1963)

  Arrow, K. J., 1963. Uncertainty and the Welfare Economics of Medical Care.
  The American Economic Review 53 (5), 941–973.
* Arrow (1971)

  Arrow, K. J., 1971. Essays in the Theory of Risk-Bearing. North-Holland,
  Amsterdam.
* Arrow (1974)

  Arrow, K. J., 1974. Optimal insurance and generalized deductibles. Scandinavian
  Actuarial Journal 1974 (1), 1–42.
* Björk et al. (2014)

  Björk, T., Murgoci, A., Zhou, X., 2014. Mean-variance portfolio
  optimization with state-dependent risk aversion. Mathematical Finance 24 (1),
  1–24.
* Borch (1960)

  Borch, K., 1960. The safety loading of reinsurance premiums. Skandinavisk
  Aktuarietidskrift 43, 163–184.
* Borch (1962)

  Borch, K., 1962. Equilibrium in a reinsurance market. Econometrica 30 (3),
  424–444.
* Borch (1974)

  Borch, K., 1974. The Mathematical Theory of Insurance. Liexington Books.
* Borch (1969)

  Borch, K. H., 1969. The optimal reinsurance treaty. ASTIN Bulletin 5 (2),
  293–297.
* Clarke and Dercon (2016)

  Clarke, D., Dercon, S., 2016. Dull Disasters? How Planning Ahead Will Make a
  Difference. Oxford University Press.
* Clarke (2016)

  Clarke, D. J., 2016. A theory of rational demand for index insurance. American
  Economic Journal: Microeconomics 8 (1), 283–306.
* Cummins and Mahul (2012)

  Cummins, J. D., Mahul, O., 2012. Catastrophe Risk Financing in Developing
  Countries. World Bank.
* Hallegatte et al. (2019)

  Hallegatte, S., et al., 2019. Lifelines: The Resilient Infrastructure
  Opportunity. World Bank.
* Huang and Shi (2024)

  Huang, S., Shi, P., Dec. 2024. Bridging the disaster protection gap with index
  insurance. Tech. Rep. 5052692, SSRN.
* Jarzabkowski et al. (2024)

  Jarzabkowski, P., Meissner, K., Mason, M., 2024. Insurance status review and
  recommendations for lismore. Tech. rep., Northern Rivers Adaptation Division
  NSW Reconstruction Authority.
* Jin and Zhou (2004)

  Jin, H., Zhou, X. Y., 2004. Behavioral portfolio selection in continuous time.
  Mathematical Finance 17 (3), 385–426.
* Kahn (2021)

  Kahn, M. E., 2021. Adapting to Climate Change: Markets and the Management of an
  Uncertain Future. Yale University Press.
* Kousky and Cooke (2012)

  Kousky, C., Cooke, R., 2012. Explaining the failure to insure catastrophic
  risks. Geneva Papers on Risk and Insurance 37 (2), 206–227.
* Queensland Reconstruction Autority (2019)

  Queensland Reconstruction Autority, 2019. Brisbane river strategic floodplain
  management plan. Tech. rep., The State of Queensland.
* Raviv (1979)

  Raviv, A., 1979. The design of an optimal insurance policy. American Economic
  Review 69 (1), 84–96.
* World Bank (2021)

  World Bank, 2021. Financial protection against natural disasters.
* Xu and Zhou (2014)

  Xu, Z. Q., Zhou, X. Y., 2014. Optimal investment with behavioral criteria in
  incomplete markets. Finance and Stochastics 17 (3), 423–456.

## References

* (1)

## A Moments and mean–variance objectives under censored exponential severity

This appendix collects the moment formulas and the mean–variance objectives
used throughout the paper, under the assumption that the number of events
N∼Pois​(λ)N\sim\mathrm{Pois}(\lambda) and that severities are i.i.d. and censored at
L>0L>0. Specifically, if Z∼Exp​(ν)Z\sim\mathrm{Exp}(\nu) then our losses YiY\_{i} are distributed as a censored version of ZZ, that is,

|  |  |  |
| --- | --- | --- |
|  | Yi∼min⁡{Z,L},i=1,….Y\_{i}\sim\min\{Z,L\},\quad i=1,\ldots. |  |

Then YiY\_{i} has density ν​e−ν​y\nu e^{-\nu y} on [0,L)[0,L) and an atom of mass
e−ν​Le^{-\nu L} at LL, i.e.

|  |  |  |
| --- | --- | --- |
|  | d​FYi​(y)=ν​e−ν​y​d​y+e−ν​L​δL​(d​y),y≥0.dF\_{Y\_{i}}(y)=\nu e^{-\nu y}\,dy+e^{-\nu L}\,\delta\_{L}(dy),\qquad y\geq 0. |  |

We denote by S=∑i=1NYiS=\sum\_{i=1}^{N}Y\_{i} the aggregate annual loss.

### A.1 Basic severity moments

The first two raw moments of YiY\_{i} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Yi]\displaystyle\mathbb{E}[Y\_{i}] | =∫0Ly​ν​e−ν​y​𝑑y+L​e−ν​L=1−e−ν​Lν,\displaystyle=\int\_{0}^{L}y\nu e^{-\nu y}\,dy+Le^{-\nu L}=\frac{1-e^{-\nu L}}{\nu}, |  | (A.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Yi2]\displaystyle\mathbb{E}[Y\_{i}^{2}] | =∫0Ly2​ν​e−ν​y​𝑑y+L2​e−ν​L=2ν2−2​e−ν​Lν2−2​L​e−ν​Lν.\displaystyle=\int\_{0}^{L}y^{2}\nu e^{-\nu y}\,dy+L^{2}e^{-\nu L}=\frac{2}{\nu^{2}}-\frac{2e^{-\nu L}}{\nu^{2}}-\frac{2Le^{-\nu L}}{\nu}. |  | (A.2) |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(Yi)=𝔼​[Yi2]−(𝔼​[Yi])2.\mathrm{Var}(Y\_{i})=\mathbb{E}[Y\_{i}^{2}]-\bigl(\mathbb{E}[Y\_{i}]\bigr)^{2}. |  | (A.3) |

### A.2 Excess–loss moments for the deductible contract

For a deductible level d∈[0,L]d\in[0,L], define (x)+:=max⁡{x,0}(x)\_{+}:=\max\{x,0\}. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[(Yi−d)+]\displaystyle\mathbb{E}\bigl[(Y\_{i}-d)\_{+}\bigr] | =∫dL(y−d)​ν​e−ν​y​𝑑y+(L−d)​e−ν​L=e−ν​d−e−ν​Lν,\displaystyle=\int\_{d}^{L}(y-d)\nu e^{-\nu y}\,dy+(L-d)e^{-\nu L}=\frac{e^{-\nu d}-e^{-\nu L}}{\nu}, |  | (A.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[(Yi−d)+2]\displaystyle\mathbb{E}\bigl[(Y\_{i}-d)\_{+}^{2}\bigr] | =∫dL(y−d)2​ν​e−ν​y​𝑑y+(L−d)2​e−ν​L=2​e−ν​dν2−2​e−ν​Lν2+2​(d−L)​e−ν​Lν.\displaystyle=\int\_{d}^{L}(y-d)^{2}\nu e^{-\nu y}\,dy+(L-d)^{2}e^{-\nu L}=\frac{2e^{-\nu d}}{\nu^{2}}-\frac{2e^{-\nu L}}{\nu^{2}}+\frac{2(d-L)e^{-\nu L}}{\nu}. |  | (A.5) |

We also record the mixed moment

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Yi​(Yi−d)+]\displaystyle\mathbb{E}\bigl[Y\_{i}(Y\_{i}-d)\_{+}\bigr] | =∫dLy​(y−d)​ν​e−ν​y​𝑑y+L​(L−d)​e−ν​L\displaystyle=\int\_{d}^{L}y(y-d)\nu e^{-\nu y}\,dy+L(L-d)e^{-\nu L} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =d​(e−ν​d+e−ν​L)ν+2​e−ν​dν2−2​e−ν​Lν2−2​L​e−ν​Lν.\displaystyle=\frac{d(e^{-\nu d}+e^{-\nu L})}{\nu}+\frac{2e^{-\nu d}}{\nu^{2}}-\frac{2e^{-\nu L}}{\nu^{2}}-\frac{2Le^{-\nu L}}{\nu}. |  | (A.6) |

A simplification that is repeatedly used is

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(d):\displaystyle G(d): | =𝔼[min(Yi,d)2]=𝔼[(Yi−(Yi−d)+)2]\displaystyle=\mathbb{E}[\min(Y\_{i},d)^{2}]=\mathbb{E}[(Y\_{i}-(Y\_{i}-d)\_{+})^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[Yi2]+𝔼​[(Yi−d)+2]−2​𝔼​[Yi​(Yi−d)+]\displaystyle=\mathbb{E}[Y\_{i}^{2}]+\mathbb{E}\bigl[(Y\_{i}-d)\_{+}^{2}\bigr]-2\mathbb{E}\bigl[Y\_{i}(Y\_{i}-d)\_{+}\bigr] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2ν2​[1−e−ν​d​(1+ν​d)],d∈[0,L].\displaystyle=\frac{2}{\nu^{2}}\bigl[1-e^{-\nu d}(1+\nu d)\bigr],\qquad d\in[0,L]. |  | (A.7) |

### A.3 Premiums under the expectation principle

Under the expectation principle with loading and a fixed-cost term, the
premiums are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫(d)​(d;θd,γd)\displaystyle\mathcal{P}^{(\text{d})}\left(d;\theta\_{d},\gamma\_{d}\right) | =(1+θd)​(𝔼​[𝔅(d)​(N,Y1,…,YN,d)]+γd)=(1+θd)​(λ​𝔼​[(Yi−d)+]+γd)\displaystyle=(1+\theta\_{d})\Bigl(\mathbb{E}\bigl[\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right)\bigr]+\gamma\_{d}\Bigr)=(1+\theta\_{d})\Bigl(\lambda\,\mathbb{E}\bigl[(Y\_{i}-d)\_{+}\bigr]+\gamma\_{d}\Bigr) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(1+θd)​(λ​e−ν​d−e−ν​Lν+γd),d∈[0,L],\displaystyle=(1+\theta\_{d})\left(\lambda\frac{e^{-\nu d}-e^{-\nu L}}{\nu}+\gamma\_{d}\right),\qquad d\in[0,L], |  | (A.8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒫(p)​(k;θp,γp)\displaystyle\mathcal{P}^{(\text{p})}\left(k;\theta\_{p},\gamma\_{p}\right) | =(1+θp)​(𝔼​[𝔅(p)​(N,k)]+γp)=(1+θp)​(λ​k+γp),k≥0.\displaystyle=(1+\theta\_{p})\Bigl(\mathbb{E}\bigl[\mathfrak{B}^{(\text{p})}\left(N,k\right)\bigr]+\gamma\_{p}\Bigr)=(1+\theta\_{p})(\lambda k+\gamma\_{p}),\qquad k\geq 0. |  | (A.9) |

### A.4 Mean–variance objective: deductible indemnity

Let terminal wealth be

|  |  |  |  |
| --- | --- | --- | --- |
|  | W=w0−𝒫(.)(.;.)−S+𝔅(.)(N,Y1,…,YN,⋅),MV(.)(W;β)=𝔼[W]−βVar(W),β>0.W=w\_{0}-\mathcal{P}^{(\text{.})}\left(.;.\right)-S+\mathfrak{B}^{(\text{.})}\left(N,Y\_{1},\dots,Y\_{N},\cdot\right),\qquad\operatorname{MV}^{(\text{.})}\left(W;\beta\right)=\mathbb{E}[W]-\beta\,\mathrm{Var}(W),\quad\beta>0. |  | (A.10) |

For the deductible contract,

|  |  |  |
| --- | --- | --- |
|  | 𝔅(d)​(N,Y1,…,YN,d)=∑i=1N(Yi−d)+,S=∑i=1NYi.\mathfrak{B}^{(\text{d})}\left(N,Y\_{1},\dots,Y\_{N},d\right)=\sum\_{i=1}^{N}(Y\_{i}-d)\_{+},\qquad S=\sum\_{i=1}^{N}Y\_{i}. |  |

Using N∼Pois​(λ)N\sim\mathrm{Pois}(\lambda) and independence of NN and (Yi)(Y\_{i}), one obtains

|  |  |  |  |
| --- | --- | --- | --- |
|  | MV(d)⁡(W;d,β,θd,γd)=w0−𝒫(d)​(d;θd,γd)−λ​𝔼​[Yi]+λ​𝔼​[(Yi−d)+]−β​λ​G​(d).\operatorname{MV}^{(\text{d})}\left(W;d,\beta,\theta\_{d},\gamma\_{d}\right)=w\_{0}-\mathcal{P}^{(\text{d})}\left(d;\theta\_{d},\gamma\_{d}\right)-\lambda\,\mathbb{E}[Y\_{i}]+\lambda\,\mathbb{E}\bigl[(Y\_{i}-d)\_{+}\bigr]-\beta\,\lambda\,G(d). |  | (A.11) |

Differentiating ([A.11](https://arxiv.org/html/2512.21973v1#S1.E11 "In A.4 Mean–variance objective: deductible indemnity ‣ A Moments and mean–variance objectives under censored exponential severity ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂MV(d)∂d\displaystyle\frac{\partial\text{MV}^{(d)}}{\partial d} | =λ​e−ν​d​(θd−2​β​d),\displaystyle=\lambda e^{-\nu d}\bigl(\theta\_{d}-2\beta d\bigr), |  | (A.12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂2MV(d)∂d2\displaystyle\frac{\partial^{2}\text{MV}^{(d)}}{\partial d^{2}} | =λ​e−ν​d​(−ν​θd+2​ν​β​d−2​β).\displaystyle=\lambda e^{-\nu d}\bigl(-\nu\theta\_{d}+2\nu\beta d-2\beta\bigr). |  | (A.13) |

Thus, the interior critical point is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗=θd2​β,d^{\*}=\frac{\theta\_{d}}{2\beta}, |  | (A.14) |

and the curvature at d∗d^{\*} is negative:

|  |  |  |
| --- | --- | --- |
|  | ∂2MV(d)∂d2|d=d∗=−2​β​λ​e−ν​d∗<0.\frac{\partial^{2}\text{MV}^{(d)}}{\partial d^{2}}\Big|\_{d=d^{\*}}=-2\beta\lambda e^{-\nu d^{\*}}<0. |  |

(When contractual bounds are imposed, one projects d∗d^{\*} onto [0,L][0,L].)

### A.5 Mean–variance objective: per–event parametric cover

For the parametric contract,

|  |  |  |
| --- | --- | --- |
|  | 𝔅(p)​(N,k)=k​N,S=∑i=1NYi.\mathfrak{B}^{(\text{p})}\left(N,k\right)=kN,\qquad S=\sum\_{i=1}^{N}Y\_{i}. |  |

Under the same assumptions,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | MV(p)⁡(W;k,β,θp,γp)\displaystyle\operatorname{MV}^{(\text{p})}\left(W;k,\beta,\theta\_{p},\gamma\_{p}\right) | =w0−𝒫(p)​(k;θp,γp)−λ​𝔼​[Yi]+λ​k−β​λ​(𝔼​[Yi2]+k2−2​k​𝔼​[Yi]).\displaystyle=w\_{0}-\mathcal{P}^{(\text{p})}\left(k;\theta\_{p},\gamma\_{p}\right)-\lambda\,\mathbb{E}[Y\_{i}]+\lambda k-\beta\lambda\bigl(\mathbb{E}[Y\_{i}^{2}]+k^{2}-2k\,\mathbb{E}[Y\_{i}]\bigr). |  | (A.15) |

Differentiating gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂MV(p)∂k=λ​(−θp+2​β​(𝔼​[Yi]−k)),∂2MV(p)∂k2=−2​β​λ<0,\frac{\partial\text{MV}^{(p)}}{\partial k}=\lambda\bigl(-\theta\_{p}+2\beta(\mathbb{E}[Y\_{i}]-k)\bigr),\qquad\frac{\partial^{2}\text{MV}^{(p)}}{\partial k^{2}}=-2\beta\lambda<0, |  | (A.16) |

so that the unique maximiser is

|  |  |  |  |
| --- | --- | --- | --- |
|  | k∗=𝔼​[Yi]−θp2​β,k^{\*}=\mathbb{E}[Y\_{i}]-\frac{\theta\_{p}}{2\beta}, |  | (A.17) |

(with projection onto any admissible range such as [0,L][0,L] if imposed).

### A.6 Optional limiting case as L→∞L\to\infty

If L→∞L\to\infty, then Yi→Y∼Exp​(ν)Y\_{i}\to Y\sim\mathrm{Exp}(\nu) with
𝔼​[Y]=1/ν\mathbb{E}[Y]=1/\nu and Var​(Y)=1/ν2\mathrm{Var}(Y)=1/\nu^{2}. In that case,
([A.15](https://arxiv.org/html/2512.21973v1#S1.E15 "In A.5 Mean–variance objective: per–event parametric cover ‣ A Moments and mean–variance objectives under censored exponential severity ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) reduces to

|  |  |  |
| --- | --- | --- |
|  | MV(p)⁡(W;k,β,θp,γp)=w0−(1+θp)​(λ​k+γp)−λ​1ν+λ​k−β​λ​(2ν2+k2−2​kν),\operatorname{MV}^{(\text{p})}\left(W;k,\beta,\theta\_{p},\gamma\_{p}\right)=w\_{0}-(1+\theta\_{p})(\lambda k+\gamma\_{p})-\lambda\frac{1}{\nu}+\lambda k-\beta\lambda\left(\frac{2}{\nu^{2}}+k^{2}-\frac{2k}{\nu}\right), |  |

and ([A.17](https://arxiv.org/html/2512.21973v1#S1.E17 "In A.5 Mean–variance objective: per–event parametric cover ‣ A Moments and mean–variance objectives under censored exponential severity ‣ When Indemnity Insurance Fails: Parametric Coverage under Binding Budget and Risk Constraints")) becomes k∗=1ν−θp2​βk^{\*}=\frac{1}{\nu}-\frac{\theta\_{p}}{2\beta}.
Analogous simplifications apply to the deductible expressions.

## B Duality: E​[Yi]=d∗+k∗E[Y\_{i}]=d^{\*}+k^{\*}

This appendix provides full derivations of the optimal deductible d∗d^{\*} and the optimal parametric per–event cover k∗k^{\*} under the mean–variance objective. It further identifies the exact conditions under which the duality

|  |  |  |
| --- | --- | --- |
|  | E​[Yi]=d∗+k∗\displaystyle E[Y\_{i}]=d^{\*}+k^{\*} |  |

holds, and explains why this identity is specific to a combination of
(i) mean–variance preferences,
(ii) a Poisson claim count model, and
(iii) premiums calculated via the expectation principle.
If any one of these three ingredients is altered, the duality fails.

Let NN be the claim count, YiY\_{i} the capped severity,
and m​(d)=E​[(Yi−d)+]m(d)=E[(Y\_{i}-d)\_{+}] the expected excess loss above dd.
Premiums under the expectation principle are

|  |  |  |
| --- | --- | --- |
|  | 𝒫(d)​(d∗;θd,γd)=(1+θd)​(E​[N]​m​(d)+γd),𝒫(p)​(k;θp,γp)=(1+θp)​(E​[N]​k+γp).\displaystyle\mathcal{P}^{(\text{d})}\left(d^{\*};\theta\_{d},\gamma\_{d}\right)=(1+\theta\_{d})\big(E[N]\,m(d)+\gamma\_{d}\big),\qquad\mathcal{P}^{(\text{p})}\left(k;\theta\_{p},\gamma\_{p}\right)=(1+\theta\_{p})\big(E[N]\,k+\gamma\_{p}\big). |  |

### B.1. General claim count model

Define μ=E​[N]\mu=E[N] and σN2=Var⁡(N)\sigma\_{N}^{2}=\operatorname{Var}(N), without assuming that NN is
Poisson. Standard random–sum identities yield, for the parametric cover,

|  |  |  |
| --- | --- | --- |
|  | Var⁡(S−k​N)=μ​Var⁡(Yi)+σN2​(E​[Yi]−k)2.\displaystyle\operatorname{Var}(S-kN)=\mu\operatorname{Var}(Y\_{i})+\sigma\_{N}^{2}(E[Y\_{i}]-k)^{2}. |  |

The mean–variance objective, therefore, takes the form

|  |  |  |
| --- | --- | --- |
|  | MV(p)⁡(W;k,β,θp,γp)=const−μ​θp​k−β​[μ​Var⁡(Yi)+σN2​(E​[Yi]−k)2],\displaystyle\operatorname{MV}^{(\text{p})}\left(W;k,\beta,\theta\_{p},\gamma\_{p}\right)=\text{const}-\mu\theta\_{p}k-\beta\!\left[\mu\operatorname{Var}(Y\_{i})+\sigma\_{N}^{2}(E[Y\_{i}]-k)^{2}\right], |  |

where ’const’ represents a constant in kk. Differentiation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | k∗=E​[Yi]−μσN2​θp2​β.k^{\*}=E[Y\_{i}]-\frac{\mu}{\sigma\_{N}^{2}}\,\frac{\theta\_{p}}{2\beta}. |  | (B.1) |

Thus the optimal k∗k^{\*} depends on the ratio μ/σN2\mu/\sigma\_{N}^{2}. In particular,
k∗k^{\*} reduces to a simple expression only when Var⁡(N)=E​[N]\operatorname{Var}(N)=E[N].

For the deductible cover, the retained loss per event is Rd=min⁡(Yi,d)R\_{d}=\min(Y\_{i},d).
Using random–sum variance formulas,

|  |  |  |
| --- | --- | --- |
|  | Var⁡(∑i=1NRd)=μ​Var⁡(Rd)+σN2​(E​[Rd])2,\displaystyle\operatorname{Var}\!\Big(\sum\_{i=1}^{N}R\_{d}\Big)=\mu\,\operatorname{Var}(R\_{d})+\sigma\_{N}^{2}(E[R\_{d}])^{2}, |  |

and differentiating the resulting mean–variance objective gives the first–order
condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​θd=2​β​(μ​d∗+(σN2−μ)​E​[Rd∗]),\mu\theta\_{d}=2\beta\big(\,\mu d^{\*}+(\sigma\_{N}^{2}-\mu)E[R\_{d^{\*}}]\,\big), |  | (B.2) |

which in general has no closed form and depends explicitly on Var⁡(N)\operatorname{Var}(N).

### B.2. Specialization to the compound Poisson case

Now assume N∼Pois​(λ)N\sim\mathrm{Pois}(\lambda), so that

|  |  |  |
| --- | --- | --- |
|  | μ=σN2=λ.\displaystyle\mu=\sigma\_{N}^{2}=\lambda. |  |

This equi-dispersion property causes significant simplifications. The parametric solution reduces to

|  |  |  |
| --- | --- | --- |
|  | k∗=E​[Yi]−θp2​β.\displaystyle k^{\*}=E[Y\_{i}]-\frac{\theta\_{p}}{2\beta}. |  |

Similarly, for the deductible, the variance identity reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var⁡(∑i=1NRd)=λ​E​[Rd2],\operatorname{Var}\!\Big(\sum\_{i=1}^{N}R\_{d}\Big)=\lambda E[R\_{d}^{2}], |  | (B.3) |

and the nonlinear term in the first-order condition disappears, such that

|  |  |  |
| --- | --- | --- |
|  | λ​θd=2​β​λ​d∗,so thatd∗=θd2​β.\displaystyle\lambda\theta\_{d}=2\beta\lambda d^{\*},\qquad\text{so that}\qquad d^{\*}=\frac{\theta\_{d}}{2\beta}. |  |

These closed–form solutions rely critically on:

1. 1.

   the mean–variance objective (quadratic variance term),
2. 2.

   Poisson equi–dispersion (Var⁡(N)=E​[N]\operatorname{Var}(N)=E[N]), and
3. 3.

   expectation–principle premiums (linearity in E​[(Yi−d)+]E[(Y\_{i}-d)\_{+}]
   and in kk).

Removing any of these assumptions breaks the linear structure of the
first–order conditions.

### B.3. Duality

Assuming identical loadings (θd=θp=θ\theta\_{d}=\theta\_{p}=\theta), we have shown:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d∗=θ2​β,k∗=E​[Yi]−θ2​β.d^{\*}=\frac{\theta}{2\beta},\qquad k^{\*}=E[Y\_{i}]-\frac{\theta}{2\beta}. |  | (B.4) |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[Yi]=d∗+k∗.E[Y\_{i}]=d^{\*}+k^{\*}. |  | (B.5) |

This identity provides the duality described in Section 3.1. It is a direct
consequence of the combination of assumptions (1)–(3) above and does not hold
for general claim count distributions or for premium principles other than the
expectation principle.