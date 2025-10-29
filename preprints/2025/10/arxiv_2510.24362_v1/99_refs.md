---
authors:
- Gabriel Montes-Rojas
- Fernando Toledo
- Nicolás Bertholet
- Kevin Corfield
doc_id: arxiv:2510.24362v1
family_id: arxiv:2510.24362
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Implicit quantile preferences of the Fed and the Taylor rule
url_abs: http://arxiv.org/abs/2510.24362v1
url_html: https://arxiv.org/html/2510.24362v1
venue: arXiv q-fin
version: 1
year: 2025
---


Gabriel Montes-Rojas111CONICET and Instituto Interdisciplinario de Economía Política, Universidad de Buenos Aires, Ciudad Autónoma de Buenos Aires, Argentina. gabriel.montes@economicas.uba.ar
  
Fernando Toledo222Universidad Nacional de La Plata, La Plata, Argentina. fernando.toledo@econo.unlp.edu.ar
  
Nicolás Bertholet333Instituto Interdisciplinario de Economía Política, Universidad de Buenos Aires, Ciudad Autónoma de Buenos Aires, Argentina. nicolasbertholet2008@economicas.uba.ar
  
Kevin Corfield444Universidad de Buenos Aires, Ciudad Autónoma de Buenos Aires, Argentina. kevincorfield@economicas.uba.ar

(October 2025)

###### Abstract

We study optimal monetary policy when a central bank maximizes a quantile utility objective rather than expected utility. In our framework, the central bank’s risk attitude is indexed by the quantile index level, providing a transparent mapping between hawkish/dovish stances and attention to adverse macroeconomic realizations. We formulate the infinite-horizon problem using a Bellman equation with the quantile operator. Implementing an Euler-equation approach, we get Taylor-rule-type reaction functions. Using an indirect inference approach, we derive a central bank risk aversion implicit quantile index. An empirical implementation for the US is outlined based on reduced-form laws of motion with conditional heteroskedasticity, enabling estimation of the new monetary policy rule and its dependence on the Fed risk attitudes. The results reveal that the Fed has mostly a dovish-type behavior but with some periods of hawkish attitudes.

Keywords: Taylor rule; inflation; output gap; quantile preferences; dynamic programming; recursive model.

JEL: C22; C61; E52; E58.

## 1 Introduction

The debate between hawkish and dovish monetary policy authorities has received increased attention (see Tobback, Nardelli, and Martens ([2017](https://arxiv.org/html/2510.24362v1#bib.bib69)), Hack, Istrefi, and Meier ([2025](https://arxiv.org/html/2510.24362v1#bib.bib38))). For example, the London Investment Service Company In Touch Capital Markets has introduced a relative scale to explain the position of Fed’s regarding their relative aversion to inflationary pressures: the lowest bound on the scale indicates very hawkish members and the upper bound specifies very dovish ones. In the empirical literature, CBs are often classified as hawkish or dovish based on projected Taylor rules, particularly the interest rate’s long-term response to inflation (see Castro ([2011](https://arxiv.org/html/2510.24362v1#bib.bib12)); Wilson ([2020](https://arxiv.org/html/2510.24362v1#bib.bib71)); Malmendier, Nagel, and Yan ([2021](https://arxiv.org/html/2510.24362v1#bib.bib49)); González-Astudillo and Tanvir ([2023](https://arxiv.org/html/2510.24362v1#bib.bib35))).

The responses of monetary authorities to the post-pandemic period and the Ukraine war are paramount to understand coordinated monetary policy actions in terms of interest rate hikes to recent global inflation synchronization (Ha, Kose, Ohnsorge, and Yilmazkuday ([2024](https://arxiv.org/html/2510.24362v1#bib.bib37))). Although this empirical regularity, the intensity of restrictive monetary policy measures differs among countries.
This stylized fact reminds us how important it is for CBs to find an optimal policy monetary rule that reflects the distinct degree of risk aversion to inflation and economic fluctuations. For example, the Fed’s approach was shaped by empirical evidence that gathered in the years before the pandemic, and the results were impacted by a decrease in inflation persistence, a flattening of the Phillips curve’s slope, and inaccurate assessments of real-time output or unemployment (Sargent and Williams ([2025](https://arxiv.org/html/2510.24362v1#bib.bib60))).

Taylor rules have become a cornerstone of modern monetary policy science (Woodford ([2003](https://arxiv.org/html/2510.24362v1#bib.bib73)), Taylor ([1993](https://arxiv.org/html/2510.24362v1#bib.bib67))). Optimal monetary policy involves setting short-term nominal interest rates to stabilize the economy by managing inflation and output gaps, often guided by rules that recommend increasing rates when inflation is high or output exceeds its potential and lowering them otherwise (Clarida, Galí, and Gertler ([1999](https://arxiv.org/html/2510.24362v1#bib.bib18))).

Although Taylor rules provide a simple and robust framework, true optimal policy depends on specific economic models, policy objectives, and whether policymakers prioritize inflation, output, or a combination of both, leading to ongoing debates and refinements of such rules. In that regard, during the last Jackson Hole Symposium (August 2025, 21-23), Nakamura, Riblier, and Steinsson ([2025](https://arxiv.org/html/2510.24362v1#bib.bib56)) presented a study that remarks the descriptive nature of Taylor rules instead of their prescriptive one. These authors have also observed deviations from the Taylor principle after exploring the recent Fed’s behavior and also pointed out the coexistence of early and late policy interest rate hikers.

In the case of New Keynesian macroeconomic models, the discussion about the theoretical validity of optimal Taylor rules usually includes these and other relevant issues (see Boehm and House ([2014](https://arxiv.org/html/2510.24362v1#bib.bib10))). The main point we would like to state here is the discontent that some contributions express in terms of the theoretical form of optimal Taylor rules (see Cochrane ([2007](https://arxiv.org/html/2510.24362v1#bib.bib19)), Benhabib, Schmitt-Grohé, and Uribe ([2001](https://arxiv.org/html/2510.24362v1#bib.bib5))).

Theoretical contributions have usually approached the different preferences toward the traditional monetary policy trade-off (inflation versus output fluctuations) by deriving an optimally monetary policy Taylor rule minimizing a quadratic loss intertemporal function (Woodford ([2003](https://arxiv.org/html/2510.24362v1#bib.bib73))). However, problems arise in applying these functions when the underlying economic model is nonlinear (Benigno and Eggertsson ([2023](https://arxiv.org/html/2510.24362v1#bib.bib6))), shocks are non-normal (Hofmann, Manea, and Mojon ([2024](https://arxiv.org/html/2510.24362v1#bib.bib44))), or the quadratic assumption is too simplistic (al Nowaihi and Stracca ([2002](https://arxiv.org/html/2510.24362v1#bib.bib2))). Furthermore, although linear-quadratic models offer analytical tractability for deriving optimal rules, they may fail to capture key asymmetric preferences that drive actual monetary policy behavior in the real world (Svensson ([2003](https://arxiv.org/html/2510.24362v1#bib.bib66)))555El-Shagi ([2025](https://arxiv.org/html/2510.24362v1#bib.bib28)) has recently shown that the Fed prioritizes business cycle stabilization over containing inflation.. So, traditional methods often look at the average policy reaction function of a CB.

After the 2008 global financial crisis, many authors argued that CBs should pay more attention to tail risks (especially downside risks) rather than just average outcomes (see Demirguc-Kunt, Detragiache, and Merrouche ([2013](https://arxiv.org/html/2510.24362v1#bib.bib25))). For instance, regardless of the US economy’s condition, Barci ([2025](https://arxiv.org/html/2510.24362v1#bib.bib4)) notes that monetary policy can increase downside risk; nevertheless, this ability is significantly diminished during economic expansions. Such disparity, if not appropriately taken into consideration, could cause monetary authorities to be too cautious when it comes to tightening during booms.

In the present paper, our theoretical contribution is to introduce quantile utility (QU) preferences into the intertemporal minimization of the loss function of CBs. As far as we know, this contribution is completely new. We add to the literature on quantile preferences applications a new analytical framework to analyze how CBs minimize their intertemporal loss function using dynamic programming through the Bellman equation solution as in de Castro and Galvao ([2019](https://arxiv.org/html/2510.24362v1#bib.bib21)). In contrast to the usual framework of minimizing a quadratic intertemporal loss function using expected utility to attain the optimal policy Taylor rule, we incorporate QU preferences to study how CBs respond to undesirable macroeconomic outcomes. It is worth noting that our analytical framework assumes full credibility of the policymaker’s announcements (see Woodford ([2003](https://arxiv.org/html/2510.24362v1#bib.bib73))).

Our research adds new arguments to the theoretical discussion about the accurate form of the optimal Taylor rule. We depart from the conventional dynamic optimization problem faced by CBs to propose a new closed analytical form for their reaction function. The main advantage of the new Taylor rule is that CBs are concerned not only with average inflation-output trade-off but also in analyzing scenarios of inflation and output gaps.

Moreover, by comparing the observed policy actions (i.e. interest rate) with the entire myriad of available actions for all quantiles, we can infer the type of the CB at each point in time. We define this the implicit quantile preference index, which is a dynamic index of the CB risk aversion. In turn, we intepret this index as a dovish/hawkish scale.

We use US quarterly long-run data from 1954-Q4 to 2025-Q2. This framework suggests that the Fed often appear more dovish than simple Taylor rules would suggest and they may be intrinsically less concerned with downside risks (unemployment spikes, financial instability). However, this is not a general description, and there are specific periods where the Fed is characterized with hawkish behavior. Our analysis delivers an index of the Fed’s risk aversion attitudes across time that is based on the implicit quantile preference.

This study relates to three branches of the literature. First, we add to the literature on optimal monetary policy the idea that CBs adjust their monetary policy actions to more complex optimal rules than traditional ones. We show how our theoretical framework relates to the New Keynesian macroeconomic models by getting a new Taylor rule that allows different risk aversion attitudes towards inflation and output combinations. Second, we contribute to the quantile preferences literature (see de Castro and Galvao ([2022](https://arxiv.org/html/2510.24362v1#bib.bib22))) with an innovative application: the formal derivation of a closed form for a new Taylor rule. We use dynamic programming methods and the Bellman equation to optimize the CB intertemporal loss function and obtain the new optimal reaction function of policymakers (see de Castro and Galvao ([2019](https://arxiv.org/html/2510.24362v1#bib.bib21)); Hills, Nakata, and Sunakawa ([2020](https://arxiv.org/html/2510.24362v1#bib.bib43))). Third, we deliver an indirect inference approach to estimate the Fed’s risk attitude across time, thus contributing to the analysis of parameter and/or model uncertainty (see Cogley, Colacito, Hansen, and Sargent ([2008](https://arxiv.org/html/2510.24362v1#bib.bib20))).

It should be noted that our approach is different from empirical papers that estimate heterogeneous responses in a Taylor rule regression model as in Chevapatrakul, Kim, and Mizen ([2009](https://arxiv.org/html/2510.24362v1#bib.bib15)), Wolters ([2012](https://arxiv.org/html/2510.24362v1#bib.bib72)), Chevapatrakul and Paez-Farrell ([2014](https://arxiv.org/html/2510.24362v1#bib.bib16)), Chen and Kashiwagi ([2017](https://arxiv.org/html/2510.24362v1#bib.bib14)) and Christou, Naraidoo, Gupta, and Kim ([2018](https://arxiv.org/html/2510.24362v1#bib.bib17)), among others. In those papers, the key goal is to evaluate heterogeneous responses of the interest rate to inflation and output gap (and others) using a quantile regression framework. In our paper, quantiles relate to a structural preference parameter of the CB and not to the conditional quantiles of the conditional distribution of the interest rate.

The paper proceeds as follows. Section [2](https://arxiv.org/html/2510.24362v1#S2 "2 Quantile preferences and risk attitude ‣ Implicit quantile preferences of the Fed and the Taylor rule") summarizes the quantile utility framework. Section [3](https://arxiv.org/html/2510.24362v1#S3 "3 Preferences of a CB and Taylor rule for QU maximizer ‣ Implicit quantile preferences of the Fed and the Taylor rule") applies dynamic programming to the intertemporal QU maximization problem to derive Taylor rules. Section [4](https://arxiv.org/html/2510.24362v1#S4 "4 Empirical implementation ‣ Implicit quantile preferences of the Fed and the Taylor rule") describes the empirical implementation strategy. Section [5](https://arxiv.org/html/2510.24362v1#S5 "5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") presents the estimation results. Section [6](https://arxiv.org/html/2510.24362v1#S6 "6 Conclusions and discussion ‣ Implicit quantile preferences of the Fed and the Taylor rule") concludes.

## 2 Quantile preferences and risk attitude

### 2.1 Quantile preferences for univariate outcomes

An expected utility (EU) maximizer with utility function u:ℝ→ℝu:\mathbb{R}\to\mathbb{R} prefers lottery XX to YY if E​[u​(X)]⩾E​[u​(Y)]\textnormal{E}[u(X)]\geqslant\textnormal{E}[u(Y)]. This refers to a case when a decision maker (DM) that is faced with uncertain outcomes chooses the action that maximizes the expected average outcome. Quantile utility666Quantile preferences were first introduced by Manski ([1988](https://arxiv.org/html/2510.24362v1#bib.bib50)). Rostek ([2010](https://arxiv.org/html/2510.24362v1#bib.bib58)) and
Chambers ([2009](https://arxiv.org/html/2510.24362v1#bib.bib13)) provide axioms for the static case, and de Castro and Galvao ([2022](https://arxiv.org/html/2510.24362v1#bib.bib22)) formally axiomatize both the static and dynamic quantile preferences.
Giovannetti ([2013](https://arxiv.org/html/2510.24362v1#bib.bib34)) studies a two-period economy for an intertemporal consumption model under quantile utility maximization.
de Castro and Galvao ([2019](https://arxiv.org/html/2510.24362v1#bib.bib21)) establish the properties of a
general dynamically consistent quantile preferences model. We refer to this type of preference modeling as quantile utility (QU hereafter). (QU) is based on a framework where optimal decisions and allocations correspond to maximizing a specific quantile of the distribution of outcomes or returns.777Given a random (univariate) variables, YY, let F​(y)=FY​(y)=Pr⁡(Y⩽y)F(y)=F\_{Y}(y)=\Pr\left(Y\leqslant y\right) denote the conditional cumulative distribution function (c.d.f.) of YY.
If the function y↦FY​(y)y\mapsto F\_{Y}(y) is strictly increasing and continuous in its support, its inverse is the quantile of YY, that is, Qτ​[Y]=FY−1​(τ)\textnormal{Q}\_{\tau}[Y]=F\_{Y}^{-1}(\tau), for τ∈(0,1)\tau\in(0,1).
If y↦FY​(y)y\mapsto F\_{Y}(y) is not invertible,
we can still define the quantile as one of its generalized inverses.
Following the standard practice, we define the quantile as the left-continuous version of the generalized inverse:

Qτ​[Y]≡inf{y∈ℝ:Pr⁡[Y⩽y]⩾τ}.\textnormal{Q}\_{\tau}[Y]\equiv\inf\{y\in\mathbb{R}:\Pr[Y\leqslant y]\geqslant\tau\}.
 Quantile preferences are defined by simply substituting the expectation by the quantile operator, that is,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X⪰Y\displaystyle X\succeq Y | ⇔Qτ​[u​(X)]⩾Qτ​[u​(Y)].\displaystyle\iff\textnormal{Q}\_{\tau}[u(X)]\geqslant\textnormal{Q}\_{\tau}[u(Y)]. |  | (1) |

The intuition is that, in the presence of uncertainty, a QU maximizer makes decisions based on maximizing a given τ\tau quantile of the distribution of potential outcomes.

For univariate random variables (i.e. monetary outcomes), quantiles enjoy the following property: for any continuous and increasing function f:ℝ→ℝf:\mathbb{R}\to\mathbb{R}, f​(Qτ​[X])=Qτ​[f​(X)]f(\textnormal{Q}\_{\tau}[X])=\textnormal{Q}\_{\tau}[f(X)].
If u:ℝ→ℝu:\mathbb{R}\to\mathbb{R} is strictly increasing and continuous, as usual, then we can take its inverse and apply to ([1](https://arxiv.org/html/2510.24362v1#S2.E1 "In 2.1 Quantile preferences for univariate outcomes ‣ 2 Quantile preferences and risk attitude ‣ Implicit quantile preferences of the Fed and the Taylor rule")), to obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X⪰Y\displaystyle X\succeq Y | ⇔u−1(Qτ[u(X)])⩾u−1(Qτ[u(Y)])⇔Qτ[X]⩾Qτ[Y].\displaystyle\iff u^{-1}(\textnormal{Q}\_{\tau}[u(X)])\geqslant u^{-1}(\textnormal{Q}\_{\tau}[u(Y)])\iff\textnormal{Q}\_{\tau}[X]\geqslant\textnormal{Q}\_{\tau}[Y]. |  |

In other words, for the univariate case, the utility functional form is not necessary to model DM behavior.

As noted by Manski ([1988](https://arxiv.org/html/2510.24362v1#bib.bib50)), under QU risk attitudes can be indexed by τ\tau itself. Intuitively, we can map risk aversion into the τ\tau scale, such that a τ\tau-DM is more risk averse than τ′\tau^{\prime}-DM if τ≤τ′\tau\leq\tau^{\prime}. In sum, a τ\tau-DM evaluates lotteries and actions based on choosing the ones with the highest τ\tau quantile, and then, the lower τ\tau is, the more the DM is concerned with low values or losses.

### 2.2 Quantile preferences for multivariate outcomes

For a multivariate random outcome variable, say mm dimensional vectors of the form Y=(Y1,Y2,…,Ym)Y=(Y\_{1},Y\_{2},...,Y\_{m}) with domain 𝒴⊆ℝm\mathcal{Y}\subseteq\mathbb{R}^{m}, inf{y∈𝒴:τ≤F​(y)}\inf\{y\in\mathcal{Y}:\tau\leq F(y)\} is (in general) not unique.

Take the bivariate case Y=(Y1,Y2)Y=(Y\_{1},Y\_{2}) with domain 𝒴⊆ℝ2\mathcal{Y}\subseteq\mathbb{R}^{2}. Quantiles are themselves then defined on regions, contours and depths (Hallin and Konen, [2024](https://arxiv.org/html/2510.24362v1#bib.bib40)).
A quantile on the bivariate domain is any pair (q1,q2)∈𝒴(q\_{1},q\_{2})\in\mathcal{Y} such that P​(Y1≤q1,Y2≤q2)=τP(Y\_{1}\leq q\_{1},Y\_{2}\leq q\_{2})=\tau, τ∈(0,1)\tau\in(0,1).
Figure [1](https://arxiv.org/html/2510.24362v1#S2.F1 "Figure 1 ‣ 2.2 Quantile preferences for multivariate outcomes ‣ 2 Quantile preferences and risk attitude ‣ Implicit quantile preferences of the Fed and the Taylor rule")a plots the contour plot for the probability density function of a bivariate distribution and adds two points that correspond to the same quantile τ\tau. Figure [1](https://arxiv.org/html/2510.24362v1#S2.F1 "Figure 1 ‣ 2.2 Quantile preferences for multivariate outcomes ‣ 2 Quantile preferences and risk attitude ‣ Implicit quantile preferences of the Fed and the Taylor rule")b plots the same contour plot but considers the curves corresponding to two different τ\tau’s.

Figure 1: (a) Two points representing quantile τ\tau. P​(Y1≤q1,Y2≤q2)=τP(Y\_{1}\leq q\_{1},Y\_{2}\leq q\_{2})=\tau. (b) Two contour lines for τ<τ′\tau<\tau^{\prime}

| (a) | (b) |
| --- | --- |
| Refer to caption | Refer to caption |

Note that the preceding analysis of QU cannot be applied to the multivariate domain unless additional considerations are taken. Consider two random variables X=(X1,X2)X=(X\_{1},X\_{2}) and Y=(Y1,Y2)Y=(Y\_{1},Y\_{2}) on the bivariate domain. Figure [2](https://arxiv.org/html/2510.24362v1#S2.F2 "Figure 2 ‣ 2.2 Quantile preferences for multivariate outcomes ‣ 2 Quantile preferences and risk attitude ‣ Implicit quantile preferences of the Fed and the Taylor rule") plots two different cases for the same quantile τ\tau with (a) and without (b) crossing. As such, there is no natural ordering that can be used in terms of the distribution function or its inverse, the quantiles.

Figure 2: (a) Qτ​(X)>>Qτ​(Y)Q\_{\tau}(X)>>Q\_{\tau}(Y). (b) Qτ(X)><Qτ(Y)Q\_{\tau}(X)><Q\_{\tau}(Y)

| (a) | (b) |
| --- | --- |
| Refer to caption | Refer to caption |

A consequence of this is that the QU model cannot evaluate random utility based on the multivariate distribution of the arguments determining the utility. For our purposes, a QU-maximizer CB that has preferences over inflation and output gap cannot resort to the joint distribution of these variables to evaluate policies. On the contrary, it does require the utility function and the relative valuation of each component.

Following Hallin, Paindaveine, and Šiman ([2010](https://arxiv.org/html/2510.24362v1#bib.bib41)) multivariate models can be decomposed into a series of univariate models in terms of quantile analysis. Quantiles are analyzed in terms of a magnitude and a direction. We define
T=(τ1,τ2,…,τm)∈(0,1)mT=(\tau\_{1},\tau\_{2},\ldots,\tau\_{m})\in(0,1)^{m} as a set of quantile indices.
The vector TT can be factorized as T≡τ​vT\equiv\tau v, where
τ=‖T‖∈(0,1)\tau=\|T\|\in(0,1) represents the magnitude, and
d∈ℝm−1≡{d∈ℝm:‖d‖=1}d\in\mathbb{R}^{m-1}\equiv\{d\in\mathbb{R}^{m}:\|d\|=1\}
represents the direction expressed as a unit vector in the Euclidean framework.

In this model, τ\tau is a scalar quantile index that specifies the position along the distribution,
while γ\gamma is a unit vector that determines the direction in the mm-dimensional space.
This vector can be interpreted as an (m−1)(m-1)-dimensional directional component that captures how quantile changes unfold across variables. This decomposition allows for an intuitive and geometric interpretation of multivariate quantiles in terms of distance and orientation within the variable space.

Vector directional quantile proposes to study univariate variables of the form d⋅yd\cdot y, where ⋅\cdot represent element-by-element vector multiplication. Figure [3](https://arxiv.org/html/2510.24362v1#S2.F3 "Figure 3 ‣ 2.2 Quantile preferences for multivariate outcomes ‣ 2 Quantile preferences and risk attitude ‣ Implicit quantile preferences of the Fed and the Taylor rule") plots this idea for the bivariate case (in the figure d⟂d^{\perp} is an orthonormal basis of the subspace orthogonal to dd). Once a direction is fixed, the problem becomes one of univariate quantiles, and QU analysis can be applied.

In the QU setup, the direction dd can be interpreted as a linearization of utility function over the multivariate domain. The direction reduces the dimensionality of preferences into a linear univariate model. Note, however, that is only valid in a local sense. Non-local comparisons require the use of the utility function to fulfill this role for all cases.

Figure 3: Vector directional quantile

![Refer to caption](x5.png)

### 2.3 Dynamic models

Many applications of intertemporal maximization use the standard recursive EU.
These models have been workhorses in several economic fields.
EU is simple and amenable to theoretical modeling.
The assumption of maximization of average utility, the average being a simple measure of centrality, has intuitive appeal as a behavioral postulate.
Nevertheless, the usual EU framework has been subjected to a number of criticisms, including in its dynamic version. For example, it has been well documented in the literature that it is not possible to separate the intertemporal substitution from the risk attitude parameters when using standard dynamic models based on the EU (see, e.g., Hall, [1988](https://arxiv.org/html/2510.24362v1#bib.bib39)).
The framework proposed by Kreps and Porteus ([1978](https://arxiv.org/html/2510.24362v1#bib.bib46)) to study temporal resolution of uncertainty was one of the first efforts to go beyond EU in the dynamic setting.
An expanding literature considers alternative recursive models.888We refer the reader to Epstein and Zin ([1989](https://arxiv.org/html/2510.24362v1#bib.bib30), [1991](https://arxiv.org/html/2510.24362v1#bib.bib31)), Weil ([1990](https://arxiv.org/html/2510.24362v1#bib.bib70)), Grant, Kajii, and Polak ([2000](https://arxiv.org/html/2510.24362v1#bib.bib36)), Epstein and Schneider ([2003](https://arxiv.org/html/2510.24362v1#bib.bib29)), Hansen and Sargent ([2004](https://arxiv.org/html/2510.24362v1#bib.bib42)), Maccheroni, Marinacci, and Rustichini ([2006](https://arxiv.org/html/2510.24362v1#bib.bib48)), Klibanoff, Marinacci, and Mukerji ([2009](https://arxiv.org/html/2510.24362v1#bib.bib45)), Marinacci and Montrucchio ([2010](https://arxiv.org/html/2510.24362v1#bib.bib51)),
Strzalecki ([2013](https://arxiv.org/html/2510.24362v1#bib.bib65)),
Bommier, Kochov, and Le Grand ([2017](https://arxiv.org/html/2510.24362v1#bib.bib11)), Sarver ([2018](https://arxiv.org/html/2510.24362v1#bib.bib61)), and Dejarnette, Dillenberger, Gottlieb, and Ortoleva ([2020](https://arxiv.org/html/2510.24362v1#bib.bib24)) among others.

de Castro and Galvao ([2019](https://arxiv.org/html/2510.24362v1#bib.bib21)) developed a new alternative to the EU recursive model based on QU. In their model, the economic agent chooses the alternative that leads to the the highest τ\tau-quantile of the stream of future utilities for a fixed τ∈(0,1)\tau\in(0,1).
The dynamic quantile preferences for intertemporal decisions are represented by an additively separable quantile model with standard discounting.
The associated recursive equation is characterized by the sum of the current period utility function and the discounted value of the certainty equivalent, which is obtained from a quantile operator.
This intertemporal model is tractable and simple to interpret, since the value function and Euler equation are transparent, and easy to calculate (analytically or numerically).
This framework allows for the separation of the risk attitude from the intertemporal substitution, which is not possible with EU, while maintaining important features of the standard model, such as dynamic consistency and monotonicity.

## 3 Preferences of a CB and Taylor rule for QU maximizer

### 3.1 General set-up

Consider now a CB that has τ\tau-QU preferences based on (πt−π∗)(\pi\_{t}-\pi^{\*}) where πt\pi\_{t} is inflation and π∗\pi\* is the target inflation rate, and output gap yt=(y¯t−yt∗)y\_{t}=(\bar{y}\_{t}-y\_{t}^{\*}) where y¯t\bar{y}\_{t} is output and yt∗y\_{t}^{\*} is a measure of output long-run trend and potential output. Moreover, we assume that the CB has a preference for smoothing policy variables over time (i.e. the interest rate).

The CB decisions can be represented along a utility function u​(y,π,i,z)u(y,\pi,i,z) that typically is a trade-off between inflation and output gaps, and it may depend on interest rate and current shocks.
In general, we could assume that the CB values more inflation and output closer to the target values.

We assume a quadratic utility function of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(πt,yt,it,zt)=−(πt−π∗)22−λ​(yt)22−δ​(it−it−1)22.u(\pi\_{t},y\_{t},i\_{t},z\_{t})=-\frac{(\pi\_{t}-\pi^{\*})^{2}}{2}-\frac{\lambda(y\_{t})^{2}}{2}-\frac{\delta(i\_{t}-i\_{t-1})^{2}}{2}. |  | (2) |

In this model, the CB has preferences for state variables close to the target values and for avoiding fluctuations in the interest rate.
This utility function is in fact a loss function multiplied by −1-1, and it can be derived from micro-foundations as in Woodford ([2003](https://arxiv.org/html/2510.24362v1#bib.bib73)). λ\lambda and δ\delta are structural parameters that correspond to the degree of substitution of the inflation gap, the output gap and the variations in interest rate along indiference curves.

Let x∈𝒳x\in\mathcal{X} denote the particular state and the state space, i∈ℐi\in\mathcal{I} be the action and the set of possible actions the CB may take, and z∈𝒵z\in\mathcal{Z}, the range of the shocks. For our purposes, xt=(yt,πt)x\_{t}=(y\_{t},\pi\_{t}), iti\_{t} is the interest rate and ztz\_{t} represents random components that affect xtx\_{t}. Moreover, we consider that zt=(zπ,t,zy,t)z\_{t}=(z\_{\pi,t},z\_{y,t}) a bivariate random vector. Although we do not explicitly consider it to reduce notation, the state variables may include lags of the variables. For our particular case, we use the lag of ii inside the utility function.

The next period state, xt+1x\_{t+1}, is defined by a law of motion function ϕ:𝒳×ℐ×𝒵→𝒳\phi:\mathcal{X}\times\mathcal{I}\times\mathcal{Z}\rightarrow\mathcal{X} that satisfies xt+1=ϕ​(xt,it,zt+1)x\_{t+1}=\phi(x\_{t},i\_{t},z\_{t+1}).
Given the current state xtx\_{t} and current shock ztz\_{t}, Γ​(xt,zt)\Gamma(x\_{t},z\_{t}) denotes the set of possible choices iti\_{t}, that is, the feasibility constraint set.

### 3.2 Infinite horizon and recursive maximization problem

In the proposed CB model, the uncertainty with respect to the future realizations of ztz\_{t} is given by a quantile applied to potential values of the utility function. In line with QU theory, the quantile index τ\tau represents CB attitudes towards risk. We refer to a τ′\tau^{\prime}-CB to be more risk averse than a τ\tau-CB one if τ′<τ\tau^{\prime}<\tau. That is, the τ′\tau^{\prime}-CB is more concerned with worse outcomes scenarios (i.e. high inflation, low output) than a τ\tau-CB.

In the QU framework, optimal decisions are taken to maximize the τ\tau quantile of intertemporal utility in an infinite horizon problem.
This framework does not allow for the same solution strategies as in the EU case, because we cannot apply the law of iterated expectations. However, under certain conditions described in de Castro and Galvao ([2019](https://arxiv.org/html/2510.24362v1#bib.bib21)), these dynamic intertemporal choices can be represented by the maximization of a value function v:𝒳×𝒵→ℝv:\mathcal{X}\times\mathcal{Z}\to\mathbb{R} that satisfies the recursive Bellman equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(x,z)=supi∈Γ​(x,z){u​(x,i,z)+β​Qτ​[v​(ϕ​(x,i,z′),z′)|z]},v(x,z)=\sup\_{i\in\Gamma(x,z)}\;\;\Bigl\{u\left(x,i,z\right)\;+\;\beta\textnormal{Q}\_{\tau}[\;v\left(\phi(x,i,z^{\prime}),\,z^{\prime}\right)\;|\;z]\Bigr\}, |  | (3) |

where z′z^{\prime} indicates the next period shock.

Note that this is similar to the usual dynamic programming problem, in which the expectation operator E​[⋅]\textnormal{E}[\cdot] is in place of Qτ​[⋅]\textnormal{Q}\_{\tau}[\cdot].
de Castro and Galvao ([2019](https://arxiv.org/html/2510.24362v1#bib.bib21)) and de Castro, Galvao, and Nunes ([2025](https://arxiv.org/html/2510.24362v1#bib.bib23)) endorse the construction of this type of recursive models from dated preferences. Those authors prove uniqueness of the solution to problem ([3](https://arxiv.org/html/2510.24362v1#S3.E3 "In 3.2 Infinite horizon and recursive maximization problem ‣ 3 Preferences of a CB and Taylor rule for QU maximizer ‣ Implicit quantile preferences of the Fed and the Taylor rule")), under a set of regularity conditions similar to those in dynamic programming set-up and some specific restrictions for the use of quantiles. The solution is a policy function iτ∗:𝒳×𝒵→ℐi\_{\tau}^{\ast}:\mathcal{X}\times\mathcal{Z}\to\mathcal{I}, that associates to each (xt,zt)(x\_{t},z\_{t}) the optimal solution iτ∗=i∗​(xt,zt)i\_{\tau}^{\ast}=i^{\ast}(x\_{t},z\_{t}).

### 3.3 Law of motion

Now consider a location-scale law of motion ϕ(.)\phi(.) for inflation and output gap, using autoregressive processes of order 1.

|  |  |  |
| --- | --- | --- |
|  | πt+1=ϕπ​(xt,it,zπ,t+1)=απ​0+απ​π​πt+απ​y​yt+απ​i​it+hπ​(πt,yt,it)​zπ,t+1,\pi\_{t+1}=\phi\_{\pi}(x\_{t},i\_{t},z\_{\pi,t+1})=\alpha\_{\pi 0}+\alpha\_{\pi\pi}\pi\_{t}+\alpha\_{\pi y}y\_{t}+\alpha\_{\pi i}i\_{t}+h\_{\pi}(\pi\_{t},y\_{t},i\_{t})z\_{\pi,t+1}, |  |

|  |  |  |
| --- | --- | --- |
|  | yt+1=ϕy​(xt,it,zy,t+1)=αy​0+αy​π​πt+αy​y​yt+αy​i​it+hy​(πt,yt,it)​zy,t+1,y\_{t+1}=\phi\_{y}(x\_{t},i\_{t},z\_{y,t+1})=\alpha\_{y0}+\alpha\_{y\pi}\pi\_{t}+\alpha\_{yy}y\_{t}+\alpha\_{yi}i\_{t}+h\_{y}(\pi\_{t},y\_{t},i\_{t})z\_{y,t+1}, |  |

where the α\alpha coefficients capture location mean effects, i.e. the persistence of inflation and output gap and how sensitive inflation and output gap are to changes in the interest rate iti\_{t}, and zπ,t+1z\_{\pi,t+1} and zy,t+1z\_{y,t+1} are random shocks, possibly correlated to each other but assumed to be independent of the state and interest rate variable, i.e. (zπ,t+1,zy,t+1)⟂(πt,yt,it)∣zt(z\_{\pi,t+1},z\_{y,t+1})\perp(\pi\_{t},y\_{t},i\_{t})\mid z\_{t}. They
have zero conditional mean E​[za,t+1|zπ,t,zy,t]=0,a=π,yE[z\_{a,t+1}|z\_{\pi,t},z\_{y,t}]=0,\ a=\pi,y and unit variance E​[za,t+12|zπ,t,zy,t]=1E[z\_{a,t+1}^{2}|z\_{\pi,t},z\_{y,t}]=1 (which anyway cannot be identified separately from hh). This is a reduced form that may be the result of intertemporal IS curve and a New Keynesian Phillips curve as in Woodford ([2003](https://arxiv.org/html/2510.24362v1#bib.bib73)) and Galí ([2015](https://arxiv.org/html/2510.24362v1#bib.bib32)).

Functions hπ(.)h\_{\pi}(.) and hy(.)h\_{y}(.) are skedastic strictly positive functions that control the conditional heteroskedasticity of the state variables, affecting the scale. In turn, they determine the structure of heterogeneity in the law of motion and whether the quantiles are not parallel to each other. We can refer to location shift only models to those where the hh functions are constant, and to location-scale shift models where the hh functions depend on (π,y,i)(\pi,y,i).

Several parameterizations can be applied, see for instance Romano and Wolf ([2017](https://arxiv.org/html/2510.24362v1#bib.bib57)). Different specifications used in the heteroskedasticity literature to model location-scale shift effects are

|  |  |  |
| --- | --- | --- |
|  | ha​(πt,yt,it)=(γa​0+γa​π​πt+γa​y​yt+γa​i​it)1/2,a=π,y.h\_{a}(\pi\_{t},y\_{t},i\_{t})=(\gamma\_{a0}+\gamma\_{a\pi}\pi\_{t}+\gamma\_{ay}y\_{t}+\gamma\_{ai}i\_{t})^{1/2},\ a=\pi,y. |  |

or

|  |  |  |
| --- | --- | --- |
|  | ha​(πt,yt,it)=e​x​p​[(γa​0+γa​π​πt+γa​y​yt+γa​i​it)1/2],a=π,y.h\_{a}(\pi\_{t},y\_{t},i\_{t})=exp\left[(\gamma\_{a0}+\gamma\_{a\pi}\pi\_{t}+\gamma\_{ay}y\_{t}+\gamma\_{ai}i\_{t})^{1/2}\right],\ a=\pi,y. |  |

The γ\gamma coefficients control whether the random shocks affect the scale impact of these shocks on inflation and output gap. Thus models with γ=0\gamma=0 have only location shifts, while γ≠0\gamma\neq 0 characterize location-scale shift ones.

In the context of quantile regression specifications, this representation allows for a random-coefficient model indexed by a quantile index, i.e.,

|  |  |  |
| --- | --- | --- |
|  | Qτπ​(πt+1|xt,it)=απ​0​(τπ)+απ​π​(τπ)​πt+απ​y​(τπ)​yt+απ​i​(τπ)​it,τπ∈(0,1),Q\_{\tau\_{\pi}}(\pi\_{t+1}|x\_{t},i\_{t})=\alpha\_{\pi 0}(\tau\_{\pi})+\alpha\_{\pi\pi}(\tau\_{\pi})\pi\_{t}+\alpha\_{\pi y}(\tau\_{\pi})y\_{t}+\alpha\_{\pi i}(\tau\_{\pi})i\_{t},\ \tau\_{\pi}\in(0,1), |  |

|  |  |  |
| --- | --- | --- |
|  | Qτy​(yt+1|xt,it)=αy​0​(τy)+αy​π​(τy)​πt+αy​y​(τy)​yt+αy​i​(τy)​it,τy∈(0,1),Q\_{\tau\_{y}}(y\_{t+1}|x\_{t},i\_{t})=\alpha\_{y0}(\tau\_{y})+\alpha\_{y\pi}(\tau\_{y})\pi\_{t}+\alpha\_{yy}(\tau\_{y})y\_{t}+\alpha\_{yi}(\tau\_{y})i\_{t},\ \tau\_{y}\in(0,1), |  |

where αa​b​(τa)=αa​b+∂ha​(xt,it)∂b​Qτa​(za|xt,it)\alpha\_{ab}(\tau\_{a})=\alpha\_{ab}+\frac{\partial h\_{a}(x\_{t},i\_{t})}{\partial b}Q\_{\tau\_{a}}(z\_{a}|x\_{t},i\_{t}), a=π,ya=\pi,y and b=0,π,y,ib=0,\pi,y,i. Here τπ\tau\_{\pi} and τy\tau\_{y} reflects different conditional responses of inflation and output gap to current state variables and policy choices. Both indexes are not necessarily independent and they need to be considered in a multivariate quantile model as in Montes-Rojas ([2017](https://arxiv.org/html/2510.24362v1#bib.bib53), [2019](https://arxiv.org/html/2510.24362v1#bib.bib54), [2022](https://arxiv.org/html/2510.24362v1#bib.bib55)).

### 3.4 Euler equations

Under certain conditions, the Taylor rule can be derived analytically from this function by implementing the Euler equation as in de Castro, Galvao, and Nunes ([2025](https://arxiv.org/html/2510.24362v1#bib.bib23)) Theorem 3.18. Consider an application of the theorem to get the Euler equation as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂u​(xt,it,zt)∂i+\displaystyle\frac{\partial u(x\_{t},i\_{t},z\_{t})}{\partial i}+ |  |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | βQτ[u​(xt+1,it+1,zt+1)∂π∂ϕπ​(xt,it,zt+1)∂i+\displaystyle\;\beta\textnormal{Q}\_{\tau}\left[\frac{u(x\_{t+1},i\_{t+1},z\_{t+1})}{\partial\pi}\frac{\partial\phi\_{\pi}(x\_{t},i\_{t},z\_{t+1})}{\partial i}+\right. |  |  |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | u​(xt+1,it+1,zt+1)∂y∂ϕy​(xt,it,zt+1)∂i|z]\displaystyle\left.\left.\frac{u(x\_{t+1},i\_{t+1},z\_{t+1})}{\partial y}\frac{\partial\phi\_{y}(x\_{t},i\_{t},z\_{t+1})}{\partial i}\right|\;z\right] | =0.\displaystyle=0. |  |  | (4) |

For this derivation to be applied, it requires that differentiability and the quantile operator can be interchanged, and that the shocks have an increasing monotonic effect.
In particular, we need the following univariate component

|  |  |  |
| --- | --- | --- |
|  | u​(xt+1,it+1,zt+1)∂π​∂ϕπ​(xt,it,zt+1)∂i+u​(xt+1,it+1,zt+1)∂y​∂ϕy​(xt,it,zt+1)∂i\frac{u(x\_{t+1},i\_{t+1},z\_{t+1})}{\partial\pi}\frac{\partial\phi\_{\pi}(x\_{t},i\_{t},z\_{t+1})}{\partial i}+\frac{u(x\_{t+1},i\_{t+1},z\_{t+1})}{\partial y}\frac{\partial\phi\_{y}(x\_{t},i\_{t},z\_{t+1})}{\partial i} |  |

to be monotonically increasing on zz. Note, however, that zz is bivariate, and therefore the monotonicity requirement has to be evaluated at particular vector directions. For the case in eq. ([2](https://arxiv.org/html/2510.24362v1#S3.E2 "In 3.1 General set-up ‣ 3 Preferences of a CB and Taylor rule for QU maximizer ‣ Implicit quantile preferences of the Fed and the Taylor rule")),

|  |  |  |
| --- | --- | --- |
|  | u​(xt+1,it+1,zt+1)∂π=−(πt+1−π∗),\frac{u(x\_{t+1},i\_{t+1},z\_{t+1})}{\partial\pi}=-(\pi\_{t+1}-\pi^{\*}), |  |

|  |  |  |
| --- | --- | --- |
|  | u​(xt+1,it+1,zt+1)∂y=−λ​yt+1,\frac{u(x\_{t+1},i\_{t+1},z\_{t+1})}{\partial y}=-\lambda y\_{t+1}, |  |

|  |  |  |
| --- | --- | --- |
|  | u​(xt,it,zt)∂i=−δ​(it−it−1).\frac{u(x\_{t},i\_{t},z\_{t})}{\partial i}=-\delta(i\_{t}-i\_{t-1}). |  |

Then the monotonicity requirement is that the random variable q​(x,i):=−ϕπ,i′​(x,i)​zπ−λ​ϕπ,i′​(x,i)​zyq(x,i):=-\phi^{\prime}\_{\pi,i}(x,i)z\_{\pi}-\lambda\phi^{\prime}\_{\pi,i}(x,i)z\_{y} with
ϕπ,i′​(x,i)=∂ϕπ​(x,i)∂i\phi^{\prime}\_{\pi,i}(x,i)=\frac{\partial\phi\_{\pi}(x,i)}{\partial i} and ϕy,i′=∂ϕy​(x,i)∂i\phi^{\prime}\_{y,i}=\frac{\partial\phi\_{y}(x,i)}{\partial i}, has a well defined quantile function.

We derive here Euler equations solutions. For simplicity we assume that απ​0=αy​0=0\alpha\_{\pi 0}=\alpha\_{y0}=0 (but this is not assumed in the empirical application).

#### Location shift only

Suppose first that γa​b=0​a,b=π,y,i\gamma\_{ab}=0\ a,b=\pi,y,i, that is, the quantiles of the random shocks are not affected by the state variables nor by the control variable.

Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −δ(it−it−1)+βQτ[−(απ​ππt+απ​yyt+απ​iit+zπ,t+1−π∗)απ​i\displaystyle-\delta(i\_{t}-i\_{t-1})+\beta\textnormal{Q}\_{\tau}\left[-(\alpha\_{\pi\pi}\pi\_{t}+\alpha\_{\pi y}y\_{t}+\alpha\_{\pi i}i\_{t}+z\_{\pi,t+1}-\pi^{\*})\alpha\_{\pi i}\right. |  |  |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | −λ(αy​ππt+αy​yyt+αy​iit+zy,t+1)αy​i∣zt]\displaystyle\left.-\lambda(\alpha\_{y\pi}\pi\_{t}+\alpha\_{yy}y\_{t}+\alpha\_{yi}i\_{t}+z\_{y,t+1})\alpha\_{yi}\mid z\_{t}\right] | =0.\displaystyle=0. |  |  | (5) |

Note that by the requirements on the validity of the Euler implementation for QU, Qτ​(−zπ,t+1​απ​i−λ​zy,t+1​αy​i∣zt)\textnormal{Q}\_{\tau}(-z\_{\pi,t+1}\alpha\_{\pi i}-\lambda z\_{y,t+1}\alpha\_{yi}\mid z\_{t}) needs to be monotonically increasing in both components (zπ,t+1,zy,t+1)(z\_{\pi,t+1},z\_{y,t+1}).

Thus we obtain the following Taylor rule for the τ\tau-QU problem

|  |  |  |
| --- | --- | --- |
|  | iτ∗​(πt,yt,it−1)=i^{\*}\_{\tau}(\pi\_{t},y\_{t},i\_{t-1})= |  |

|  |  |  |
| --- | --- | --- |
|  | (δ+β(απ​i2+λαy​i2))−1×{δit−1(\delta+\beta(\alpha\_{\pi i}^{2}+\lambda\alpha\_{yi}^{2}))^{-1}\times\left\{\delta i\_{t-1}\right. |  |

|  |  |  |
| --- | --- | --- |
|  | −β​[(απ​π​απ​i+αy​π​αy​i)​πt+λ​(απ​y​απ​i+αy​y​αy​i)​yt−απ​i​π∗]-\beta\left[(\alpha\_{\pi\pi}\alpha\_{\pi i}+\alpha\_{y\pi}\alpha\_{yi})\pi\_{t}+\lambda(\alpha\_{\pi y}\alpha\_{\pi i}+\alpha\_{yy}\alpha\_{yi})y\_{t}-\alpha\_{\pi i}\pi^{\*}\right] |  |

|  |  |  |
| --- | --- | --- |
|  | +βQτ(−zπ,t+1απ​i−λzy,t+1αy​i∣zt)}.\left.+\beta\textnormal{Q}\_{\tau}(-z\_{\pi,t+1}\alpha\_{\pi i}-\lambda z\_{y,t+1}\alpha\_{yi}\mid z\_{t})\right\}. |  |

This is similar to the typical Taylor rule derivation as in Giannoni and Woodford ([2003](https://arxiv.org/html/2510.24362v1#bib.bib33)). In the standard model, since the expectation of the random shocks is zero, the second term becomes zero.

For QU, however, the quantiles need to be computed on a case-by-case basis. For the location shift case, the quantile index τ\tau determines the quantiles of the two shocks in a particular direction given by dπ​zπ,t+1+dy​zπ,t+1d\_{\pi}z\_{\pi,t+1}+d\_{y}z\_{\pi,t+1} with dπ=−απ​iαπ2+λ2​αy2d\_{\pi}=\frac{-\alpha\_{\pi i}}{\sqrt{\alpha\_{\pi}^{2}+\lambda^{2}\alpha\_{y}^{2}}} and dy=−λ​αy​iαπ​i2+λ2​αy​i2d\_{y}=\frac{-\lambda\alpha\_{yi}}{\sqrt{\alpha\_{\pi i}^{2}+\lambda^{2}\alpha\_{yi}^{2}}}.

#### Location-scale on state variables only

Suppose now that γa​i=0​a=π,y\gamma\_{ai}=0\ a=\pi,y, that is, the interest rate exerts no scale effect on the random shocks, which may be affected by the state variables.

Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −δ(it−it−1)+βQτ[−(απ​ππt+απ​yyt+απ​iit+hπ(πt,yt)zπ,t+1−π∗)απ​i\displaystyle-\delta(i\_{t}-i\_{t-1})+\beta\textnormal{Q}\_{\tau}\left[-(\alpha\_{\pi\pi}\pi\_{t}+\alpha\_{\pi y}y\_{t}+\alpha\_{\pi i}i\_{t}+h\_{\pi}(\pi\_{t},y\_{t})z\_{\pi,t+1}-\pi^{\*})\alpha\_{\pi i}\right. |  |  |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | −λ(αy​ππt+αy​yyt+αy​iit+hy(πt,yt)zy,t+1)αy​i∣zt]\displaystyle\left.-\lambda(\alpha\_{y\pi}\pi\_{t}+\alpha\_{yy}y\_{t}+\alpha\_{yi}i\_{t}+h\_{y}(\pi\_{t},y\_{t})z\_{y,t+1})\alpha\_{yi}\mid z\_{t}\right] | =0,\displaystyle=0, |  |  | (6) |

|  |  |  |
| --- | --- | --- |
|  | iτ∗​(πt,yt,it−1)=i^{\*}\_{\tau}(\pi\_{t},y\_{t},i\_{t-1})= |  |

|  |  |  |
| --- | --- | --- |
|  | (δ+β(απ​i2+λαy​i2))−1×{δit−1(\delta+\beta(\alpha\_{\pi i}^{2}+\lambda\alpha\_{yi}^{2}))^{-1}\times\left\{\delta i\_{t-1}\right. |  |

|  |  |  |
| --- | --- | --- |
|  | −β​[(απ​π​απ​i+αy​π​αy​i)​πt+λ​(απ​y​απ​i+αy​y​αy​i)​yt−απ​i​π∗]-\beta\left[(\alpha\_{\pi\pi}\alpha\_{\pi i}+\alpha\_{y\pi}\alpha\_{yi})\pi\_{t}+\lambda(\alpha\_{\pi y}\alpha\_{\pi i}+\alpha\_{yy}\alpha\_{yi})y\_{t}-\alpha\_{\pi i}\pi^{\*}\right] |  |

|  |  |  |
| --- | --- | --- |
|  | +βQτ(−hπ(πt,yt)zπ,t+1απ​i−λhy(πt,yt)zy,t+1αy​i∣zt)}.\left.+\beta\textnormal{Q}\_{\tau}(-h\_{\pi}(\pi\_{t},y\_{t})z\_{\pi,t+1}\alpha\_{\pi i}-\lambda h\_{y}(\pi\_{t},y\_{t})z\_{y,t+1}\alpha\_{yi}\mid z\_{t})\right\}. |  |

For the location-scale shift case, the quantile index τ\tau determines the quantiles of the two shocks in a particular direction given by dπ​zπ,t+1+dy​zπ,t+1d\_{\pi}z\_{\pi,t+1}+d\_{y}z\_{\pi,t+1} with

|  |  |  |
| --- | --- | --- |
|  | dπ=−hπ​(πt,yt)​απ​i​(απ​i2​hπ​(πt,yt)2+λ2​hy​(πt,yt)2​αy​i2)−1/2d\_{\pi}=-h\_{\pi}(\pi\_{t},y\_{t})\alpha\_{\pi i}\left(\alpha\_{\pi i}^{2}h\_{\pi}(\pi\_{t},y\_{t})^{2}+\lambda^{2}h\_{y}(\pi\_{t},y\_{t})^{2}\alpha\_{yi}^{2}\right)^{-1/2} |  |

and

|  |  |  |
| --- | --- | --- |
|  | dy=−λ​hy​(πt,yt)​αy​i​(απ​i2​hπ​(πt,yt)2+λ2​hy​(πt,yt)2​αy​i2)−1/2.d\_{y}=-\lambda h\_{y}(\pi\_{t},y\_{t})\alpha\_{yi}\left(\alpha\_{\pi i}^{2}h\_{\pi}(\pi\_{t},y\_{t})^{2}+\lambda^{2}h\_{y}(\pi\_{t},y\_{t})^{2}\alpha\_{yi}^{2}\right)^{-1/2}. |  |

For this case, the direction is state dependent, that is, the QU analysis is (πt,yt)(\pi\_{t},y\_{t})-specific.

#### Location-scale on state and control variables

Finally, for the general case when there are no restrictions on γa​b,a,b=π,y,i\gamma\_{ab},\ a,b=\pi,y,i we have

|  |  |  |
| --- | --- | --- |
|  | −δ​(it−it−1)+\displaystyle-\delta(i\_{t}-i\_{t-1})+ |  |
|  |  |  |
| --- | --- | --- |
|  | βQτ[−(απ​ππt+απ​yyt+απ​iit+hπ(πt,yt,it)zπ,t+1−π∗)(απ​i+∂hπ​(πt,yt,it)∂izπ,t+1)\displaystyle\beta\textnormal{Q}\_{\tau}\left[-(\alpha\_{\pi\pi}\pi\_{t}+\alpha\_{\pi y}y\_{t}+\alpha\_{\pi i}i\_{t}+h\_{\pi}(\pi\_{t},y\_{t},i\_{t})z\_{\pi,t+1}-\pi^{\*})(\alpha\_{\pi i}+\frac{\partial h\_{\pi}(\pi\_{t},y\_{t},i\_{t})}{\partial i}z\_{\pi,t+1})\right. |  |
|  |  |  |
| --- | --- | --- |
|  | −λ(αy​ππt+αy​yyt+αy​iit+hy(πt,yt,it)zy,t+1)(αy​i+∂hy​(πt,yt,it)∂izy,t+1)∣zt]\displaystyle\left.-\lambda(\alpha\_{y\pi}\pi\_{t}+\alpha\_{yy}y\_{t}+\alpha\_{yi}i\_{t}+h\_{y}(\pi\_{t},y\_{t},i\_{t})z\_{y,t+1})(\alpha\_{yi}+\frac{\partial h\_{y}(\pi\_{t},y\_{t},i\_{t})}{\partial i}z\_{y,t+1})\mid z\_{t}\right] |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | =0.=0. |  | (7) |

Here, there is no analytical solution because the quantiles will depend on both zaz\_{a} and za2z\_{a}^{2}, a,b=π,ya,b=\pi,y. (Note that for the expected utility case, the expectation of the square is just replaced by its variance, and thus we could still derive a Taylor rule type model).

## 4 Empirical implementation

### 4.1 Algorithm for empirical implementation

Consider time-series data {πt,yt,it}t=0T\{\pi\_{t},y\_{t},i\_{t}\}\_{t=0}^{T} and set a target value π∗\pi^{\*} and parameters (β,λ,δ)(\beta,\lambda,\delta). Note that we are implicitly defining that the target value for output gap is 0. Define 𝒯\mathcal{T} as a discrete grid on the interval (0,1)(0,1).

1. 1.

   Estimate law of motion reduced form VAR(1) models for (πt,yt)(\pi\_{t},y\_{t}) using iti\_{t} as an exogenous variable to get the α\alpha coefficients.
2. 2.

   Estimate the skedastic functions hπh\_{\pi} and hyh\_{y} by running reduced form VAR(1) models of squared OLS residuals {u^π,t+12,u^y,t+12}\{\hat{u}^{2}\_{\pi,t+1},\hat{u}^{2}\_{y,t+1}\} on {πt,yt,it}\{\pi\_{t},y\_{t},i\_{t}\} to get γ\gamma coefficients.
3. 3.

   Compute {z^π,t,z^y,t}t=1T\{\hat{z}\_{\pi,t},\hat{z}\_{y,t}\}\_{t=1}^{T} stochastic shocks estimates, i.e. z^a,t=u^a,t/h^a,t\hat{z}\_{a,t}=\hat{u}\_{a,t}/\hat{h}\_{a,t}, a=π,ya=\pi,y. Then compute the empirical quantiles, Q^τ\widehat{\textnormal{Q}}\_{\tau}.
4. 4.

   Solve for iτ∗​(πt,yt,it−1)i\_{\tau}^{\*}(\pi\_{t},y\_{t},i\_{t-1}) for τ∈𝒯\tau\in\mathcal{T}.

Consider now the evaluation of the underlying preferences of the CB. Here we follow an indirect inference procedure. For each time period tt, we can evaluate the optimal response for all quantile indexes and then infer the τ\tau that produces the closest value of the observed policy variable. In other words

|  |  |  |
| --- | --- | --- |
|  | τ^t=arg⁡minτ∈𝒯⁡|it−iτ∗​(πt,yt,it−1)|.\hat{\tau}\_{t}=\arg\min\_{\tau\in\mathcal{T}}|i\_{t}-i\_{\tau}^{\*}(\pi\_{t},y\_{t},i\_{t-1})|. |  |

This procedure delivers an index of the implicit risk aversion quantile preferences of the CB.

### 4.2 Data sources and model calibration

#### 4.2.1 Data

The empirical estimation involved in step 1 of algorithm is based on three macroeconomic variables constructed from raw data obtained from the Federal Reserve Economic Data of St. Louis (FRED St. Louis) database. The original dataset comprised Real GDP (GDPC1), Potential GDP (GDPPOT), the Effective Federal Funds Rate (FEDFUNDS), and the Personal Consumption Expenditures Chain-type Price Index (PCECTPI). For consistency across series, monthly observations (FEDFUNDS) were converted to quarterly frequency using arithmetic averages. From these sources, we derived the following variables

1. 1.

   Output gap (yty\_{t})

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | yt=(G​D​P​C​1tG​D​P​P​O​Tt−1)∗100y\_{t}=\bigg(\frac{GDPC1\_{t}}{GDPPOT\_{t}}-1\bigg)\*100 |  | (8) |
2. 2.

   Inflation (πt\pi\_{t})

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | πt=100×Δ​ln⁡(P​C​E​C​T​P​It)\pi\_{t}=100\times\Delta\ln(PCECTPI\_{t}) |  | (9) |
3. 3.

   Interest rate (it)(i\_{t}), proxied by the Effective Federal Funds rate.

Table [1](https://arxiv.org/html/2510.24362v1#S4.T1 "Table 1 ‣ 4.2.1 Data ‣ 4.2 Data sources and model calibration ‣ 4 Empirical implementation ‣ Implicit quantile preferences of the Fed and the Taylor rule") reports summary statistics of the variables used in this paper.

Table 1: Descriptive Statistics

| Statistic | ii | yy | π\pi |
| --- | --- | --- | --- |
| Mean | 4.62 | -0.27 | 0.78 |
| Minimum | 0.06 | -9.02 | -1.61 |
| 1st Quartile | 1.94 | -1.58 | 0.41 |
| Median | 4.33 | -0.20 | 0.66 |
| 3rd Quartile | 6.24 | 1.25 | 1.01 |
| Maximum | 17.78 | 5.68 | 2.96 |

The three constructed series – the output gap (yty\_{t}), inflation (πt\pi\_{t}), and the nominal interest rate (iti\_{t}) – are employed in step 1 of the empirical algorithm. Specifically, they serve as the input variables for estimating the reduced-form law of motion VAR(1) models, from which the coefficients α\alpha are obtained. They are then used in step 2 to compute the skedastic functions and the zz shocks components in step 3.

These estimates provide the foundation for the subsequent steps of the empirical implementation. The final dataset used for estimation spans from the fourth quarter of 1954 to the second quarter of 2025, yielding a total of 283 quarterly observations.

The second VAR(1) model estimation incorporates two dummy variables to control for the extraordinary shocks associated with major global crises. The first dummy captures the exceptional effects of the global financial crisis, covering the period from the fourth quarter of 2007 to the fourth quarter of 2009. The second dummy accounts for the economic disruptions linked to the COVID-19 pandemic, spanning from the first quarter of 2020 to the first quarter of 2021. Including these variables ensures that the estimated relationships among the models endogenous variables are not biased by these exceptional and exogenous events.

#### 4.2.2 Calibration

We calibrate the remaining parameters of the model in step 4 of the algorithm, following the literature on the Taylor rule for the US.
The calibration strategy consists of setting some non-target structural parameters based on empirical evidence.

In particular, following Dennis ([2004](https://arxiv.org/html/2510.24362v1#bib.bib26)) the policy discount factor is set to β=0.99\beta=0.99999This represents the CB’s time preference, indicating how much it values future welfare compared to current welfare. A higher discount factor 0.99 means the CB is more patient and cares more about long-term stability., the relative weight on output gap stabilization is set to λ=1\lambda=1101010The quarterly calibration of lambda for a CB loss function with output equal to 1 involves using the loss function’s sensitivity to output deviations to determine the weight (lambda) on output in the loss function, relative to inflation. The value of lambda is adjusted to prioritize output stability and it is a matter of a CB deciding how to weigh output versus inflation., and the interest rate smoothing is set to δ=0.1\delta=0.1111111Interest-rate smoothing is the tendency for CBs, including the Fed, to adjust interest rates in small steps over time. A value of delta equal to δ=0.1\delta=0.1 in a policy rule represents the weight on a smoothing term in a simplified model, suggesting that about 10 percent of the adjustment in the desired interest rate is reflected in the policy rate within a quarter, indicating a very gradual policy response. The value of 0.1 is a hypothetical calibration that would imply a very fast adjustment compared to the historical norm (historically estimated to be closer to 0.8 in the US), though still gradual. This behavior can stem from optimal policy choices to reduce volatility and manage expectations, or from practical considerations like market reaction and uncertainty (see Sack and Weiland ([2000](https://arxiv.org/html/2510.24362v1#bib.bib59))). For our purposes, it helps in evaluating heterogeneity across quantiles in a relatively short period of time.. Finally, we assume that estimates that the average implied inflation target of the Fed is around 2 percent of annual inflation (0.496 percent in quarterly log differences). Among others, Andrade, Gali, Le Bihan, and Matheron ([2019](https://arxiv.org/html/2510.24362v1#bib.bib3)) and Bianchi ([2019](https://arxiv.org/html/2510.24362v1#bib.bib9)) calibrate their models using an inflation target consistent with the Fed’s 2 percent objective.121212Under former Chair Ben Bernanke, the Fed officially adopted a 2 percent inflation target in January 2012. This move brought the Fed in line with many other central banks and was based on a strategy of price stability, aiming for 2 percent inflation as the longer-run goal for achieving both maximum employment and price stability. Although the 2 percent target was made public and official in 2012, the Fed had been operating with a similar goal behind the scenes since 1996.

The baseline calibration is summarized in Table [2](https://arxiv.org/html/2510.24362v1#S4.T2 "Table 2 ‣ 4.2.2 Calibration ‣ 4.2 Data sources and model calibration ‣ 4 Empirical implementation ‣ Implicit quantile preferences of the Fed and the Taylor rule").

Table 2: Quarterly calibrated parameters

| Parameter | Value | Description | Source |
| --- | --- | --- | --- |
| β\beta | 0.99 | Policy discount factor | Dennis (2004) |
| λ\lambda | 1 | Relative weight on output gap | Dennis (2004) |
|  |  | stabilization |  |
| δ\delta | 0.1 | Interest rate smoothing | Sack and Weiland (2000) |
|  |  | parameter |  |
| π∗\pi^{\ast} | 0.496 | Quarterly inflation target | Andrade et al. (2019); Bianchi (2019) |

## 5 Results

### 5.1 Baseline model

Tables [3](https://arxiv.org/html/2510.24362v1#S5.T3 "Table 3 ‣ 5.1 Baseline model ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") and [4](https://arxiv.org/html/2510.24362v1#S5.T4 "Table 4 ‣ 5.1 Baseline model ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule")
report the reduced form VAR(1) models and the skedastic functions, respectively. In both cases we use two different models. A baseline model without COVID and Global Financial Crisis (GFC) dummies and another with those dummies included.

The VAR model reveals that lagged ii has a positive effect on inflation but a negative effect on output gap. Note that these estimated parameters do not imply a structural relationship among the variables, but they are only a reduced-form result.

In a reduced-form VAR model, the sign of the output gap’s coefficient in the inflation equation is typically positive, consistent with the New Keynesian Phillips curve. However, this relationship can be obscured, unstable, or even appear with the wrong sign (i.e. the flat Phillips curve puzzle) due to the nature of reduced-form estimation and the influence of other shocks. While the underlying structural relationship is positive, the sign we get from a simple reduced-form VAR estimation is not a reliable estimate of the Phillips curve slope (see Mavroeidis, Plagborg-Møller, and Stock ([2014](https://arxiv.org/html/2510.24362v1#bib.bib52))).

A similar argument applies for understanding the sing of the interest rate on inflation. In that regard, the price puzzle is the empirical finding that interest rate hikes can be followed by rising inflation (see Sims ([1992](https://arxiv.org/html/2510.24362v1#bib.bib62))). It is primarily a statistical illusion caused by the econometrician’s model failing to account for the fact that the CB is raising rates in anticipation of future inflation. When models are properly specified to include the CB’s information, the puzzle usually vanishes, and the standard theoretical relationship holds (see Stock and Watson ([2001](https://arxiv.org/html/2510.24362v1#bib.bib63)); Bernanke and Mihov ([1998](https://arxiv.org/html/2510.24362v1#bib.bib8)); and Leeper, Sims, and Zha ([1996](https://arxiv.org/html/2510.24362v1#bib.bib47))).

In addition, our empirical findings indicate that inflation and output gap have high autoregressive coefficients (close to 0.7 for inflation, 0.9 for output gap). The inclusion of the COVID and the GFC dummies do not change the sign of the estimated coefficients.

For the skedastic function, a preliminary analysis (not reported; available upon request) reveals that lagged ii is not statistically significant in the skedastic functions, and therefore we impose that γa​i=0​a=π,y\gamma\_{ai}=0\ a=\pi,y for the computation of the optimal Taylor rule. In turn, this determines that we follow the location-shift model with control variables only in the skedastic function, and that analytical derivations can be used.

Table 3: VAR(1) Results Full Sample

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Baseline | | Baseline + dummies | |
|  | Inflation (π\pi) | Output gap (yy) | Inflation (π\pi) | Output gap (yy) |
| it−1i\_{t-1} | 0.024∗∗∗ | −-0.029 | 0.024∗∗∗ | −-0.037∗ |
|  | (0.008) | (0.022) | (0.008) | (0.022) |
| πt−1\pi\_{t-1} | 0.719∗∗∗ | −-0.130 | 0.718∗∗∗ | −-0.149 |
|  | (0.045) | (0.125) | (0.045) | (0.123) |
| yt−1y\_{t-1} | 0.006 | 0.904∗∗∗ | 0.007 | 0.891∗∗∗ |
|  | (0.010) | (0.027) | (0.010) | (0.027) |
| Constant | 0.114∗∗∗ | 0.215∗∗ | 0.110∗∗∗ | 0.314∗∗∗ |
|  | (0.037) | (0.105) | (0.039) | (0.107) |
| COVID |  |  | 0.131 | −-0.922∗∗ |
|  |  |  | (0.164) | (0.451) |
| GFC |  |  | −-0.025 | −-0.979∗∗∗ |
|  |  |  | (0.123) | (0.337) |
| Observations | 282 | 282 | 282 | 282 |
| R2 | 0.668 | 0.804 | 0.669 | 0.812 |
| Adjusted R2 | 0.664 | 0.802 | 0.663 | 0.808 |
| Note: ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | |
| --- | --- | --- | --- | --- |




Table 4: Skedastic Models - Full Sample

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Baseline | | Baseline + dummies | |
|  | u^π2\hat{u}\_{\pi}^{2} | u^y2\hat{u}\_{y}^{2} | u^π2\hat{u}\_{\pi}^{2} | u^y2\hat{u}\_{y}^{2} |
| πt−1\pi\_{t-1} | 0.045 | −-0.311 | 0.078∗∗ | 0.101 |
|  | (0.040) | (0.463) | (0.038) | (0.337) |
| yt−1y\_{t-1} | −-0.010 | −-0.217∗ | −-0.001 | −-0.111 |
|  | (0.011) | (0.127) | (0.010) | (0.093) |
| COVID |  |  | 0.355∗∗ | 19.274∗∗∗ |
|  |  |  | (0.176) | (1.568) |
| GFC |  |  | 0.775∗∗∗ | 0.305 |
|  |  |  | (0.132) | (1.175) |
| Constant | 0.087∗∗ | 1.153∗∗ | 0.033 | 0.467 |
|  | (0.041) | (0.464) | (0.039) | (0.345) |
| Observations | 281 | 281 | 281 | 281 |
| R2 | 0.007 | 0.013 | 0.126 | 0.368 |
| Adjusted R2 | −-0.0004 | 0.006 | 0.113 | 0.359 |
| Note: ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | |
| --- | --- | --- | --- | --- |

Figure [4(a)](https://arxiv.org/html/2510.24362v1#S5.F4.sf1 "In Figure 4 ‣ 5.1 Baseline model ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") plots the observed Effective Federal Funds Rate (EFFR) together with the optimal interest rate response for a QU maximizer CB (i.e. the Fed), for different representative quantile indexes τ∈{0.1,0.25,0.5,0.75,0.9}\tau\in\{0.1,0.25,0.5,0.75,0.9\}. The graph represents the wide variety of optimal conditional reactions that may arise for any given QU preference.

Figure [4(b)](https://arxiv.org/html/2510.24362v1#S5.F4.sf2 "In Figure 4 ‣ 5.1 Baseline model ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") plots the implied τ\tau that represent the closest match to the observed interest rate using a discrete grid search τ∈{0.01,0.02,…,0.98,0.99}\tau\in\{0.01,0.02,...,0.98,0.99\}. Overall, the results indicate that most of the time the Fed has an implied behavior that is consistent with high values of τ\tau. However, in some periods, the implied τ\tau is drastically reduced.

Figures [5(a)](https://arxiv.org/html/2510.24362v1#S5.F5.sf1 "In Figure 5 ‣ 5.1 Baseline model ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") and [5(b)](https://arxiv.org/html/2510.24362v1#S5.F5.sf2 "In Figure 5 ‣ 5.1 Baseline model ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") presents the same exercise for the model with GFC and COVID dummies. Note that the results are very similar to the baseline model, thus suggesting that the periods highlighted by the dummies are not driving the main results.

Figure 4: Baseline results: Taylor interest-rate rule and Fed risk aversion.

(a) Observed rate and Taylor rule

![Refer to caption](x6.png)

(b) Implied τ\tau

![Refer to caption](x7.png)




Figure 5: Results with dummies: Taylor interest-rate rule and Fed risk aversion.

(a) Observed rate and Taylor rule

![Refer to caption](x8.png)

(b) Implied τ\tau

![Refer to caption](x9.png)

In economic terms, a higher τ\tau means a relatively lower risk aversion by the Fed’s authorities. In turn, a lower risk aversion relates to an implied QU preference of the Fed that gives more weight to good macroeconomic outcomes. These findings are consistent with the empirical evidence that shows a significant reduction in inflation and output volatility during the Great Moderation period (see Stock and Watson ([2012](https://arxiv.org/html/2510.24362v1#bib.bib64)), Bernanke ([2004](https://arxiv.org/html/2510.24362v1#bib.bib7))). By contrast, relatively lower values of τ\tau means higher risk aversion from monetary policy authorities and more weight on potential QU losses.

Here are some significant episodes where the Fed significantly increased the EFFR. These are in general matched with lower τ\tau values and changes in the US policymakers behavior regarding their higher risk aversion to undesirable macroeconomic outcomes. More precisely, with the adoption of more hawkish stances:

1. The Great Inflation Battles (late 1960s-early 1980s). This period was defined by the Fed’s struggle against persistently high inflation, which culminated in the most aggressive rate hikes in its history. The Fed began raising rates to combat inflation from the Vietnam War and the 1973 OPEC oil embargo. The EFFR rose from around 3.5 per cent in 1972 to a peak of near 13 per cent in July 1974. From 1977-1980, the inflation rate surged into double digits. Under Fed Chair G. William Miller and then Paul Volcker, the Fed became increasingly aggressive. The rate jumped from approximately 7 per cent in early 1977 to a staggering peak of 20 per cent in April 1980. After a brief easing, inflation remained high. Paul Volcker famously engineered a severe recession to break the back of inflation for good. The Fed drove the rate from near 10 per cent in mid-1980 to a second peak of 19 per cent in June 1981. This is the most famous and aggressive tightening cycle in Fed history.

2. Maintaining Credibility (1983-1984). With inflation now falling, the Fed needed to prove its resolve to keep it down as the economy recovered. The Fed funds rate was raised from near 8.5 per cent to approximately 11.5 per cent to prevent a resurgence of inflation.

3. The Soft-Landing Attempt (1987-1989). With Alan Greenspan now as Chair, the Fed tightened policy as inflation pressures began to build again. The rate rose from near 6.5 per cent to approximately 9.75 per cent.

4. The Preemptive Strike (1994-1995). This is a classic example of a preemptive strike against inflation. The economy was recovering strongly, and the Fed, fearing future inflation, raised rates before inflation actually materialized. A series of rapid hikes took the EFFR from near 3 per cent to approximately 6 per cent. This successful maneuver is often called a soft landing.

5. The Tech Bubble Era (1999-2000). The booming economy and fears of asset bubbles led the Fed to tighten monetary policy. The funds rate was raised from near 4.75 per cent to proximately 6.5 per cent.

6. The Measured Pace (2004-2006). After cutting rates to historic lows of 1 per cent following the dot-com bust, the Fed began a long, predictable cycle of 0.25 per cent hikes to normalize rates. The famous measured pace of 17 consecutive hikes took the funds rate from 1 per cent to 5.25 per cent.

7. The Post-Financial Crisis Liftoff (2015-2018). After seven years near zero following the 2008 crisis, the Fed began a very slow and cautious tightening cycle. Through a series of small, well-telegraphed hikes, the rate moved from near 0.25 per cent to a peak of approximately 2.5 per cent in 2018.

8. The Post-Pandemic Inflation Fight (2022-2023). In response to the highest inflation in 40 years, driven by pandemic stimulus, supply chain issues, and the war in Ukraine, the Fed embarked on its most aggressive tightening cycle since the 1980s. In just over a year, the Fed raised the EFFR from near 0.25 per cent to a target range of 5.25-5.50 per cent, where it remains as of mid-2024.

These findings are revealing in terms of showing that optimal interest rate response by the Fed relates to a specific value of τ\tau and, accordingly, to a certain degree aversion to undesirable macroeconomic scenarios in terms of inflation and economic activity deviations from their target values.

Additionally, the implied τ\tau series also report a consistent behavior with the US monetary policy history observed in the estimation period (see Figure [4(b)](https://arxiv.org/html/2510.24362v1#S5.F4.sf2 "In Figure 4 ‣ 5.1 Baseline model ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule")). We observe how higher values of τ\tau and low degrees of risk aversion by the Fed are the norm, with exceptional lower values of τ\tau and higher degrees of risk aversion related to macroeconomic critical and known events (for a review of the history of monetary policy rules in the US, see Taylor ([1999](https://arxiv.org/html/2510.24362v1#bib.bib68))).

These empirical findings allow us to remark some novel evidence. The dovish or hawkish Fed’s behavior varies through time according to the economic, institutional and political context prevailing in the US (see Eijffinger and Masciandaro ([2018](https://arxiv.org/html/2510.24362v1#bib.bib27))). Although we observe that during the great part of estimation period (1959-2025), the Fed’s monetary policy authorities display a conduct that approximates more to dovish patterns, we also notice that in critical circumstances, the Fed shows a hawkish stance.

Our theoretical and empirical contributions differ from the existent ones in the following terms. We introduce a more flexible theoretical framework that maps the dovish/hawkish stances of monetary policy regarding not only the variations of interest rates. Indeed, we consider a more complex analytical framework which allows to define an undesirable macroeconomic scenario in terms of inflation and output deviations from optimal targets jointly.

### 5.2 Robustness and sensitivity analysis

To assess the robustness of our empirical findings, we conducted a battery of sensitivity checks focusing on two main aspects: (i) the relative weight assigned to output stabilization in the CB loss function, parameterized by λ\lambda, and (ii) potential structural breaks in monetary policy behavior associated with the Volcker regime shift. The results appear in the Tables [5](https://arxiv.org/html/2510.24362v1#S5.T5 "Table 5 ‣ 5.2 Robustness and sensitivity analysis ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") and [6](https://arxiv.org/html/2510.24362v1#S5.T6 "Table 6 ‣ 5.2 Robustness and sensitivity analysis ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule") and Figure [6](https://arxiv.org/html/2510.24362v1#S5.F6 "Figure 6 ‣ 5.2 Robustness and sensitivity analysis ‣ 5 Results ‣ Implicit quantile preferences of the Fed and the Taylor rule").

Table 5: VAR(1) Results - Post 1979

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Baseline | | Baseline + dummies | |
|  | Inflation (π\pi) | Output gap (yy) | Inflation (π\pi) | Output gap (yy) |
| it−1i\_{t-1} | 0.023∗∗∗ | −-0.017 | 0.023∗∗∗ | −-0.026 |
|  | (0.008) | (0.023) | (0.009) | (0.023) |
| πt−1\pi\_{t-1} | 0.615∗∗∗ | −-0.093 | 0.614∗∗∗ | −-0.128 |
|  | (0.061) | (0.165) | (0.061) | (0.162) |
| yt−1y\_{t-1} | −-0.016 | 0.879∗∗∗ | −-0.015 | 0.863∗∗∗ |
|  | (0.014) | (0.037) | (0.014) | (0.037) |
| Constant | 0.144∗∗∗ | 0.054 | 0.145∗∗∗ | 0.177 |
|  | (0.048) | (0.130) | (0.050) | (0.133) |
| COVID |  |  | 0.074 | −-0.872∗ |
|  |  |  | (0.171) | (0.452) |
| GFC |  |  | −-0.051 | −-0.914∗∗∗ |
|  |  |  | (0.128) | (0.338) |
| Observations | 182 | 182 | 182 | 182 |
| R2 | 0.545 | 0.760 | 0.546 | 0.773 |
| Adjusted R2 | 0.537 | 0.756 | 0.533 | 0.766 |
| Note: | ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | |




Table 6: Skedastic Models - Post 1979

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Baseline | | Baseline + dummies | |
|  | u^π2\hat{u}\_{\pi}^{2} | u^y2\hat{u}\_{y}^{2} | u^π2\hat{u}\_{\pi}^{2} | u^y2\hat{u}\_{y}^{2} |
| πt−1\pi\_{t-1} | 0.059 | −-0.514 | 0.104∗ | 0.131 |
|  | (0.065) | (0.781) | (0.059) | (0.560) |
| yt−1y\_{t-1} | −-0.004 | −-0.358∗ | 0.006 | −-0.216 |
|  | (0.017) | (0.209) | (0.016) | (0.150) |
| COVID |  |  | 0.294 | 18.803∗∗∗ |
|  |  |  | (0.195) | (1.836) |
| GFC |  |  | 0.708∗∗∗ | 0.483 |
|  |  |  | (0.146) | (1.378) |
| Constant | 0.082 | 1.049 | 0.015 | 0.119 |
|  | (0.058) | (0.707) | (0.055) | (0.518) |
| Observations | 181 | 181 | 181 | 181 |
| R2 | 0.005 | 0.020 | 0.128 | 0.396 |
| Adjusted R2 | −-0.006 | 0.009 | 0.108 | 0.382 |
| Note: | ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | |




Figure 6: Robustness and sensitivity analysis

(a) Taylor rule - λ=0.5\lambda=0.5 - Baseline

![Refer to caption](x10.png)

(b) Implied τ\tau - λ=0.5\lambda=0.5 - Baseline

![Refer to caption](x11.png)

(c) Taylor rule - λ=2\lambda=2 - Baseline

![Refer to caption](x12.png)

(d) Implied τ\tau - λ=2\lambda=2- Baseline

![Refer to caption](x13.png)

(e) Taylor rule - λ=1\lambda=1 - Post-1979

![Refer to caption](x14.png)

(f) Implied τ\tau - λ=1\lambda=1 - Post-1979

![Refer to caption](x15.png)

(g) Taylor rule - λ=1\lambda=1 - Post-1979 with dummies

![Refer to caption](x16.png)

(h) Implied τ\tau - λ=1\lambda=1 - Post-1979 with dummies

![Refer to caption](x17.png)

First, we explored the sensitivity of the estimated Taylor-type quantile rule to alternative values of λ∈{0.5,1,2}\lambda\in\{0.5,1,2\}. This exercise allows us to gauge whether the implied policy stance and the inferred degree of risk aversion are contingent upon the assumed trade-off between inflation and output stabilization. The results remained qualitatively stable across specifications. Lower values of λ\lambda (0.50.5) led to slightly more aggressive responses to inflation deviations, reflecting a relatively more hawkish stance, while higher values (22) induced smoother interest rate paths, consistent with greater tolerance toward output fluctuations. Nevertheless, the implied quantile-based preferences (τt\tau\_{t}) maintained the same cyclical pattern, confirming that the estimated policy reaction functions are not overly sensitive to moderate changes in the structural weighting scheme.

Second, to account for potential regime shifts in the conduct of US monetary policy, we re-estimated the baseline VAR and conditional heteroskedasticity models using a truncated sample starting in the fourth quarter of 1979. This subsample captures the onset of the Volcker disinflation episode, a well-documented structural change in the Fed’s reaction to inflationary pressures. The results reported show that the estimated coefficients remain broadly consistent with those of the full sample, with minor quantitative adjustments reflecting a stronger disinflationary response of the Fed in the post-Volcker era. The inferred quantile preferences confirm a temporary decline in τt\tau\_{t} during the early 1980s, signaling a shift towards higher risk aversion and more hawkish policy attitudes, followed by a gradual return to higher τt\tau\_{t} values consistent with a more dovish stance in subsequent decades.

Overall, both exercises confirm the internal consistency and empirical robustness of our quantile-based Taylor rule. The results suggest that the main findings, the predominance of dovish-type behavior with episodic hawkish responses are not artifacts of parameter calibration or sample selection, but rather reflect persistent structural features of the US monetary policy.

## 6 Conclusions and discussion

The study of Taylor rules through quantile methods highlights that a one-size-fits-all linear rule may be inadequate, with more nuanced, quantile-aware approaches needed to understand and formulate policy, especially in diverse economic environments. A CB may not react linearly to economic variables; its responses can vary significantly at different quantiles of the distribution.

The QU framework allows to study how independent variables (like policy tools) impact the dependent variable (like interest rates) differently across the entire distribution of outcomes, revealing heterogeneity in policy reactions. QU models explore how agents make decisions under uncertainty by focusing on outcomes at different parts of the probability distribution, while Taylor rules describe how the CBs set interest rates based on inflation and economic output.

In this paper, we study optimal monetary policy when a CB maximizes a QU objective rather than expected utility operator. In our framework, the CB’s risk attitude is indexed by the quantile level t​a​utau, providing a transparent mapping between hawkish/dovish stances and attention to adverse macroeconomic realizations. We formulate the infinite-horizon problem using a Bellman equation with the quantile operator. Implementing an Euler-equation approach, we derive Taylor-rule-type reaction functions. The Taylor rule is recovered as a special case when quantiles replace the expectation operator. An empirical implementation is outlined based on reduced-form VAR(1) laws of motion with conditional heteroskedasticity, enabling estimation of the new rule and its dependence on risk attitudes. It is important to note that our analytical methodology makes the assumption that the policymaker’s statements are entirely credible. Determining optimality criteria for establishing a Taylor rule inside the quintile preference framework in the setting of monetary policy pronouncements lacking credibility is a tenable extension of this study.

If the CB is relatively more risk averse, it would react more aggressively to downside risks than to equivalent upside risks. If the CB is relatively less risk averse, policies are guided by the possibility of good economic results. This could justify the risk management approach often discussed at CBs.

Quantile preferences naturally incorporate concerns about tail risks that expected utility might underweight. Moreover, risk attitudes might not be constant across time. Our model allows us to identify risk aversion behavior through indirect inference, by mapping the observed policy variables with the corresponding value in the optimal CB behavior.

Our empirical results for the US show that the Fed has mostly a dovish attitude over long periods of time (higher τ\tau), but with hawkish attitudes in specific periods (lower τ\tau). These periods coincide with regime changing events, like the oil crisis in the middle of the 1970s, the Volcker new approach towards fighting inflation at the end of the 1970s, the global financial crash of 2008, and the post COVID pandemia. As such, the implied risk aversion estimates reveal important changes in the Fed preferences.

The policy implications are that focusing solely on the mean in economic modeling, as many traditional Taylor rules applications do, can be misleading, as non-linear relationships and risk preferences (represented by QU) can significantly alter optimal monetary policy and under specific conditions.

## References

* (1)
* al Nowaihi and Stracca (2002)

  al Nowaihi, A., and L. Stracca (2002): “Non-Standard Central Bank Loss Functions, Skewed Risks, and Certainty Equivalence,” ECB Working Paper 129, European Central Bank.
* Andrade, Gali, Le Bihan, and Matheron (2019)

  Andrade, P., J. Gali, H. Le Bihan, and J. Matheron (2019): “The Optimal Inflation Target and the Natural Rate of Interest,” *Brookings Papers on Economic Activity*, 50(2), 173–255.
* Barci (2025)

  Barci, G. (2025): “The effects of monetary policy on macroeconomic downside risk: state-dependence matters,” *Journal of Economic Dynamics & Control*, Journal Pre-Proof, https://doi.org/10.1016/j.jedc.2025.105201.
* Benhabib, Schmitt-Grohé, and Uribe (2001)

  Benhabib, J., S. Schmitt-Grohé, and M. Uribe (2001): “The Perils of Taylor Rules,” *Journal of Economic Theory*, 96, 40–69.
* Benigno and Eggertsson (2023)

  Benigno, P., and G. E. Eggertsson (2023): “It is baaack: The surge in inflation in the 2020s and the return of the non-linear Phillips curve,” NBER Working Paper 31197.
* Bernanke (2004)

  Bernanke, B. S. (2004): “The Great Moderation,” Remarks at the meetings of the Eastern Economic Association.
* Bernanke and Mihov (1998)

  Bernanke, B. S., and I. Mihov (1998): “Measuring Monetary Policy,” *Quarterly Journal of Economics*, 113(3), 869–902.
* Bianchi (2019)

  Bianchi, F. (2019): “Hitting the Elusive Inflation Target,” NBER Working Paper 26279, National Bureau of Economic Research.
* Boehm and House (2014)

  Boehm, C., and C. L. House (2014): “Optimal Taylor rules in New Keynesian models,” NBER Working Paper 20237.
* Bommier, Kochov, and Le Grand (2017)

  Bommier, A., A. Kochov, and F. Le Grand (2017): “On Monotone Recursive Preferences,” *Econometrica*, 85, 1433–1466.
* Castro (2011)

  Castro, V. (2011): “Can central banks’ monetary policy be described by a linear (augmented) Taylor Rule or by a nonlinear rule?,” *Journal of Financial Stability*, 7(4), 228–246.
* Chambers (2009)

  Chambers, C. P. (2009): “An Axiomatization of Quantiles on the Domain of Distribution Functions,” *Mathematical Finance*, 19, 335–342.
* Chen and Kashiwagi (2017)

  Chen, J.-e., and M. Kashiwagi (2017): “The Japanese Taylor rule estimated using censored quantile regressions,” *Empirical Economics*, 52, 357–371.
* Chevapatrakul, Kim, and Mizen (2009)

  Chevapatrakul, T., T.-H. Kim, and P. Mizen (2009): “The Taylor principle and monetary policy approaching a zero bound on nominal rates: Quantile regression results for the United States and Japan,” *Journal of Money, Credit and Banking*, 41(8), 1705–1723.
* Chevapatrakul and Paez-Farrell (2014)

  Chevapatrakul, T., and J. Paez-Farrell (2014): “Monetary Policy Reaction Functions in Small Open Economies: A Quantile Regression Approach,” *The Manchester School*, 82(2), 237–256.
* Christou, Naraidoo, Gupta, and Kim (2018)

  Christou, C., R. Naraidoo, R. Gupta, and W. J. Kim (2018): “Monetary policy reaction functions of the TICKs: A quantile regression approach,” *Emerging Markets Finance and Trade*, 54(15), 3552–3565.
* Clarida, Galí, and Gertler (1999)

  Clarida, R., J. Galí, and M. Gertler (1999): “The Science of Monetary Policy: A New Keynesian Perspective,” *Journal of Economic Literature*, 37, 1661–1707.
* Cochrane (2007)

  Cochrane, J. H. (2007): “Determinacy and Identification with Taylor Rules,” NBER Working Paper 13409.
* Cogley, Colacito, Hansen, and Sargent (2008)

  Cogley, T., R. Colacito, L. P. Hansen, and T. J. Sargent (2008): “Robustness and U.S. Monetary Policy Experimentation,” *Journal of Money, Credit and Banking*, 40(8), 1599–1623.
* de Castro and Galvao (2019)

  de Castro, L., and A. F. Galvao (2019): “Dynamic Quantile Models of Rational Behavior,” *Econometrica*, 87, 1893–1939.
* de Castro and Galvao (2022)

     (2022): “Static and Dynamic Quantile Preferences,” *Economic Theory*, 73, 747–779.
* de Castro, Galvao, and Nunes (2025)

  de Castro, L., A. F. Galvao, and D. Nunes (2025): “Dynamic economics with quantile preferences,” *Theoretical Economics*, 20, 353–425.
* Dejarnette, Dillenberger, Gottlieb, and Ortoleva (2020)

  Dejarnette, P., D. Dillenberger, D. Gottlieb, and P. Ortoleva (2020): “Time Lotteries and Stochastic Impatience,” *Econometrica*, 88, 619–656.
* Demirguc-Kunt, Detragiache, and Merrouche (2013)

  Demirguc-Kunt, A., E. Detragiache, and O. Merrouche (2013): “Bank capital: Lessons from the financial crisis,” *Journal of Money, Credit and Banking*, 45(6), 1147–1164.
* Dennis (2004)

  Dennis, R. (2004): “The Policy Preferences of the U.S. Federal Reserve,” Working Paper 2001-08, Federal Reserve Bank of San Francisco.
* Eijffinger and Masciandaro (2018)

  Eijffinger, S., and D. Masciandaro (2018): *Hawks and Doves: Deeds and Words Economics and Politics of Monetary Policymaking*. CEPR Press.
* El-Shagi (2025)

  El-Shagi, M. (2025): “Does the Fed adhere to its mandate? Estimating the Federal Reserve’s objective function,” *Economic Analysis and Policy*, 87, 1782–1796.
* Epstein and Schneider (2003)

  Epstein, L. G., and M. Schneider (2003): “Recursive Multiple-Priors,” *Journal of Economic Theory*, 113, 1–31.
* Epstein and Zin (1989)

  Epstein, L. G., and S. E. Zin (1989): “Substitution, Risk Aversion, and the Temporal Behavior of Consumption and Asset Returns: A Theoretical Framework,” *Econometrica*, 57, 937–969.
* Epstein and Zin (1991)

     (1991): “Substitution, Risk Aversion, and the Temporal Behavior of Consumption and Asset Returns: An Empirical Investigation,” *Journal of Political Economy*, 99(2), 263–286.
* Galí (2015)

  Galí, J. (2015): *Monetary Policy, Inflation, and the Business Cycle*. Princeton University Press, Princeton, NJ.
* Giannoni and Woodford (2003)

  Giannoni, M. P., and M. Woodford (2003): “Optimal Interest-Rate Rules: I. General Theory,” NBER Working Paper 9419.
* Giovannetti (2013)

  Giovannetti, B. C. (2013): “Asset Pricing under Quantile Utility Maximization,” *Review of Financial Economics*, 22, 169–179.
* González-Astudillo and Tanvir (2023)

  González-Astudillo, M., and R. Tanvir (2023): “Hawkish or Dovish Fed? Estimating a Time-Varying Reaction Function of the Federal Open Market Committees Median Participant,” Federal Open Market Committees Median Participant, Finance and Economics Discussion Series 2023-070, Board of Governors of the Federal Reserve System.
* Grant, Kajii, and Polak (2000)

  Grant, S., A. Kajii, and B. Polak (2000): “Temporal Resolution of Uncertainty and Recursive Non-Expected Utility Models,” *Econometrica*, 68(2), 425–434.
* Ha, Kose, Ohnsorge, and Yilmazkuday (2024)

  Ha, J., M. A. Kose, F. Ohnsorge, and H. Yilmazkuday (2024): “What explains global inflation,” *IMF Economic Review*.
* Hack, Istrefi, and Meier (2025)

  Hack, L., K. Istrefi, and M. Meier (2025): “The Systematic Origins of Monetary Policy Shocks,” Working Paper.
* Hall (1988)

  Hall, R. E. (1988): “Intertemporal Substitution in Consumption,” *Journal of Political Economy*, 96, 339–357.
* Hallin and Konen (2024)

  Hallin, M., and D. Konen (2024): “Multivariate Quantiles: Geometric and Measure-Transportation-Based Contours,” arXiv:2401.02499.
* Hallin, Paindaveine, and Šiman (2010)

  Hallin, M., D. Paindaveine, and M. Šiman (2010): “Multivariate quantiles and multiple-output regression quantiles: From L1L\_{1} optimization to halfspace depth,” *The Annals of Statistics*, 38(2), 635–669.
* Hansen and Sargent (2004)

  Hansen, L. P., and T. J. Sargent (2004): “Misspecification in Recursive Macroeconomic Theory,” manuscript.
* Hills, Nakata, and Sunakawa (2020)

  Hills, T., T. Nakata, and T. Sunakawa (2020): “A Promised Value Approach to Optimal Monetary Policy,” *Oxford Bulletin of Economics and Statistics*, 83(1), 173–198.
* Hofmann, Manea, and Mojon (2024)

  Hofmann, B., C. Manea, and B. Mojon (2024): “Targeted Taylor rules: Mmonetary policy responses to demand- and supply-driven inflation,” Discussion paper, Bank for International Settlements.
* Klibanoff, Marinacci, and Mukerji (2009)

  Klibanoff, P., M. Marinacci, and S. Mukerji (2009): “Recursive Smooth Ambiguity Preferences,” *Journal of Economic Theory*, 144(3), 930–976.
* Kreps and Porteus (1978)

  Kreps, D. M., and E. L. Porteus (1978): “Temporal Resolution of Uncertainty and Dynamic Choice Theory,” *Econometrica*, 46, 185–200.
* Leeper, Sims, and Zha (1996)

  Leeper, E. M., C. A. Sims, and T. Zha (1996): “What Does Monetary Policy Do?,” *Brookings Papers on Economic Activity*, 1996(2), 1–78.
* Maccheroni, Marinacci, and Rustichini (2006)

  Maccheroni, F., M. Marinacci, and A. Rustichini (2006): “Dynamic Variational Preferences,” *Journal of Economic Theory*, 128, 4–44.
* Malmendier, Nagel, and Yan (2021)

  Malmendier, U., S. Nagel, and Z. Yan (2021): “The making of hawks and doves,” *Journal of Monetary Economics*, 117, 19–42.
* Manski (1988)

  Manski, C. F. (1988): “Ordinal Utility Models of Decision Making under Uncertainty,” *Theory and Decision*, 25, 79–104.
* Marinacci and Montrucchio (2010)

  Marinacci, M., and L. Montrucchio (2010): “Unique Solutions for Stochastic Recursive Utilities,” *Journal of Economic Theory*, 145, 1776–1804.
* Mavroeidis, Plagborg-Møller, and Stock (2014)

  Mavroeidis, S., M. Plagborg-Møller, and J. H. Stock (2014): “Empirical Evidence on Inflation Expectations in the New Keynesian Phillips Curve,” *Journal of Economic Literature*, 52(1), 124–188.
* Montes-Rojas (2017)

  Montes-Rojas, G. (2017): “Reduced Form Vector Directional Quantiles,” *Journal of Multivariate Analysis*, 158, 20–30.
* Montes-Rojas (2019)

     (2019): “Quantile Impulse Response Functions,” *Journal of Time Series Analysis*, 40, 739–752.
* Montes-Rojas (2022)

     (2022): “Estimating Impulse-Response Functions for Macroeconomic Models using Directional Quantiles,” *Journal of Time Series Econometrics*, 14(2), 199–225.
* Nakamura, Riblier, and Steinsson (2025)

  Nakamura, E., V. Riblier, and J. Steinsson (2025): “Beyond the Taylor Rule,” NBER Working Paper 34200.
* Romano and Wolf (2017)

  Romano, J. P., and M. Wolf (2017): “Resurrecting Weighted Least Squares,” *Journal of Econometrics*, 197, 1–19.
* Rostek (2010)

  Rostek, M. (2010): “Quantile Maximization in Decision Theory,” *Review of Economic Studies*, 77, 339–371.
* Sack and Weiland (2000)

  Sack, B., and V. Weiland (2000): “Interest-rate smoothing and optimal monetary policy: a review of recent empirical evidence,” *Journal of Economics and Business*, 52(1–2), 205–228.
* Sargent and Williams (2025)

  Sargent, T. S., and N. Williams (2025): “Conquest Lost and Regained: American Inflation in the 2020s,” Mimeograph.
* Sarver (2018)

  Sarver, T. (2018): “Dynamic Mixture-Averse Preferences,” *Econometrica*, 86, 1347–1382.
* Sims (1992)

  Sims, C. A. (1992): “Interpreting the Macroeconomic Time Series Facts: The Effects of Monetary Policy,” *European Economic Review*, 36(5), 975–1000.
* Stock and Watson (2001)

  Stock, J. H., and M. W. Watson (2001): “Vector Autoregressions,” *Journal of Economic Perspectives*, 15(4), 101–115.
* Stock and Watson (2012)

     (2012): “Disentangling the Channels of the 2007-09 Recession,” *Brookings Papers on Economic Activity*, Spring 2012, 81–156.
* Strzalecki (2013)

  Strzalecki, T. (2013): “Temporal Resolution of Uncertainty and Recursive Models of Ambiguity Aversion,” *Econometrica*, 81, 1039–1074.
* Svensson (2003)

  Svensson, L. E. (2003): “What Is Wrong with Taylor Rules? Using Judgment in Monetary Policy through Targeting Rules,” *Journal of Economic Literature*, 41, 426–477.
* Taylor (1993)

  Taylor, J. B. (1993): “Discretion versus policy rules in practice,” *Carnegie-Rochester Conference Series on Public Policy*, 39, 195–214.
* Taylor (1999)

     (1999): *Monetary Policy Rules*. University of Chicago Press.
* Tobback, Nardelli, and Martens (2017)

  Tobback, E., S. Nardelli, and D. Martens (2017): “Between hawks and doves: Measuring central bank communication,” ECB Working Paper Series 2085, European Central Bank.
* Weil (1990)

  Weil, P. (1990): “Nonexpected Utility in Macroeconomics,” *Quarterly Journal of Economics*, 105, 29–42.
* Wilson (2020)

  Wilson, L. (2020): “A dove to hawk ranking of the Martin to Yellen federal reserves,” *Southwestern Economic Review*, 47, 101–109.
* Wolters (2012)

  Wolters, M. H. (2012): “Estimating monetary policy reaction functions using quantile regressions,” *Journal of Macroeconomics*, 34(2), 342–361.
* Woodford (2003)

  Woodford, M. (2003): *Interest and Prices*. Princeton University Press, Princeton, NJ.