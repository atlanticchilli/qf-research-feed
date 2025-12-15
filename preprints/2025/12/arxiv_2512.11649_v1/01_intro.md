---
authors:
- Jean-Patrick Mascomère
- Jérémie Messud
- Yagnik Chatterjee
- Isabel Barros Garcia
doc_id: arxiv:2512.11649v1
family_id: arxiv:2512.11649
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Unified Approach to Portfolio Optimization using the ‘Gain Probability Density
  Function’ and Applications
url_abs: http://arxiv.org/abs/2512.11649v1
url_html: https://arxiv.org/html/2512.11649v1
venue: arXiv q-fin
version: 1
year: 2025
---


\fnmJean-Patrick \surMascomère
[jean-patrick.mascomere@totalenergies.com](mailto:jean-patrick.mascomere@totalenergies.com)
  
\fnmJérémie \surMessud
[jeremie.messud@totalenergies.com](mailto:jeremie.messud@totalenergies.com)
  
\fnmYagnik \surChatterjee
[yagnik.chatterjee@totalenergies.com](mailto:yagnik.chatterjee@totalenergies.com)
  
\fnmIsabel \surBarros Garcia
[isabel.barros-garcia@totalenergies.com](mailto:isabel.barros-garcia@totalenergies.com)
[

###### Abstract

This article proposes a unified framework for portfolio optimization (PO), recognizing an object called the ‘gain probability density function (PDF)’ as the fundamental object of the problem from which any objective function could be derived.
The gain PDF has the advantage of being 1-dimensional for any given portfolio and thus is easy to visualize and interpret.
The framework allows us to naturally incorporate all existing approaches (Markowitz, CVaR-deviation, higher moments…) and represents an interesting basis to develop new approaches.
It leads us to propose a method to directly match a target PDF defined by the portfolio manager, giving them maximal control on the PO problem and moving beyond approaches that focus only on expected return and risk.
As an example, we develop an application involving a new objective function to control high profits, to be applied after a conventional PO (including expected return and risk criteria) and thus leading to sub-optimality w.r.t. the conventional objective function.
We then propose a methodology to quantify a cost associated with this optimality deviation in a common budget unit, providing a meaningful information to portfolio managers.
Numerical experiments considering portfolios with energy-producing assets illustrate our approach. The framework is flexible and can be applied to other sectors (financial assets, etc).

###### keywords:

Portfolio Optimization, Probability Density Function, Statistics, High Gains, Return on Investment, Energy Markets, Finance.

## 1 Introduction

Modern single-period portfolio optimization (PO) started in 1952 with Markowitz’s pioneering paper [markowitz1952portfolio], which introduced the idea that investors should allocate their investments across a set of assets by balancing expected return and risk.

The PO approach is generally based on a statistical model of information related to the considered assets and the definition of a gain function that represents a portfolio ’satisfaction criterion’ [daniel2025portfolio, gunjan2023brief, meucci2005risk]. From these elements, statistical gain values can be computed for any given portfolio, related to a portfolio gain distribution.
Two application examples are:

* •

  Short-term financial trading, where the statistical information usually represents the return of each asset, and the gain function represents the portfolio total return, which is linear w.r.t. the portfolio asset shares [chaweewanchon2022markowitz, krokhmal2002portfolio, gatfaoui2019diversifying].
* •

  Long term investment in ‘physical assets’ (like energy-producing assets…) [jano2017investment, reus2018retail, tietjen2016investment], where the statistical information can represent the return as well as the cost related to each asset (both being uncertain in the long term), and the gain function might represent the portfolio return on investment (ROI), which is non-linear w.r.t. the portfolio asset shares.

After modeling the statistical information of the assets and defining the gain function, it is essential to establish profit and risk measures. These measures are typically expressed as expectations computed from the statistical gain values. By combining them within a multi-objective optimization, one obtains an efficient frontier (or Pareto front), which provides a set of optimal portfolios balancing expected risk and profit [daniel2025portfolio].
The portfolio manager then post-selects the most suitable portfolio according to additional criteria [xidonas2014multiobjective, bailey2012sharpe, grodzevich2006normalization].

The most widely used profit measure is the expectation of the statistical gain values, or first-order moment of these values.
For the risk measure, various options exist:

* •

  The emblematic work of Markowitz [markowitz1952portfolio] considered the second-order moment of the portfolio gain distribution, i.e. the variance of these values, in a framework where the gain function is linear. Even if Markowitz did not formulate his risk measure directly in terms of the portfilio gain distribution but using the asset information covariance matrix, both formulations are equivalent. Note, however, that the formulation used by Markowitz does not provide an obvious generalization of his risk measure to non-linear gain functions. Furthermore, the Markowitz risk measure has drawbacks. It is optimal only for a gaussian statistical model of asset information, which does not necessarily hold. Also, a risk measure that limits the profit-side variance (in addition to limiting the loss-side variance) may not represent what is desired by portfolio managers. This led Markowitz to propose the semi-variance measure of risk, that limits only the loss-side variance [markovitz1959portfolio]. Still, the gaussian hypothesis is underlying.
* •

  Thus, more sophisticated risk measures have been proposed, such as the value-at-risk (VaR) [metrics1996jp] and the conditional-value-at-risk (CVaR) [mcneil2015quantitative, rockafellar2000optimization]. The VaR emerged in the late 1980s, measuring the maximum loss within a specified confidence level and surpassing the gaussian hypothesis.
  The CVaR considers the expectation of the portfolio gain distribution beyond the VaR and has the nice feature to be sub-additive contrary to VaR [artzner1999coherent]. It can be used to compute a loss-side deviation known as the CVaR-deviation [rockafellar2002deviation].

To the best of our knowledge, the most used risk measures are all obtained from expectation values [meucci2005risk], which may not be enough to characterize the information contained in the gain distribution. Indeed, these measures typically capture only a single mode interpretation.
To remedy this, it has been proposed to consider higher-order moments of the gain distribution, e.g. skewness (third-order moment) [zhai2018mean, konno1993mean] and kurtosis (fourth-order moment) [lai2006mean, de2003incorporating], that allow to better account for asymmetry and flatness in the gain distribution, but these methods remain quite limited in the general case as they only add few additional (scalar) expectation values in the objective function.

The approach we propose in this article allows us to unify these frameworks and incorporate more information contained in the statistical gain values. It still begins with the statistical information available on the assets but also leverages the fundamental properties of the statistical framework. Namely the gain function of a given portfolio is recognized as a random variable (r.v.) whose probability density function (PDF) is the fundamental object of the PO problem from which any objective function shall be derived. We call this object the gain PDF, which has the advantage of being 1-dimensional for any portfolio. The framework allows us to naturally incorporates all existing approaches (Markowitz, CVaR-deviation, higher moments…) and represents an interesting basis to develop new approaches. It indeed leads us to propose a method to directly match a target PDF defined by the portfolio manager, giving maximal control on the PO problem.
This approach can be particularly useful when portfolio managers have specific requirements on the portfolio composition; e.g., we develop an application involving a new objective function to control high profits, to be applied after a conventional PO (including a risk or loss-oriented criterion) and thus leading to sub-optimality w.r.t. the conventional objective function.
We then propose a methodology to quantify a cost associated with this optimality deviation in a common budget unit, providing a meaningful information to portfolio managers.

The article is structured as follows. The second section clarifies the statistical assumptions underlying the single-period PO formulation and the necessary implications that arise from
them. The gain PDF will be introduced and, as a by-product, the Markowitz risk measure will be naturally generalized to non-linear gain functions (like ROI…). In the third section, we constraint the gain PDF estimator from first principles and very mild assumptions, and propose an original method based on the gain PDF to match a target PDF. In the fourth section, we apply the proposed method to foster high gains, as a second step after conventional PO. The method leverages projected gradient optimization and provides a ‘perturbed portfolio’. We propose a unified framework to quantify the marginal costs associated with the ‘perturbed portfolio’, enabling portfolio managers to justify their choices quantitatively. In the last section, we present numerical illustrations of PO considering ’physical assets’ and more precisely energy-producing assets.

## 2 PO Framework and Gain PDF

### 2.1 General Framework

The problem of PO generally consists in allocating a given budget (for example, a monetary investment in short-term financial trading, an amount of energy to be produced in long term investment in energy-producing assets, etc.) among a set of NN assets (A1,…,ANA\_{1},...,A\_{N}). The objective is to determine the proportions P→=(p1,…,pN)T\vec{P}=(p\_{1},...,p\_{N})^{T} of each asset to buy in order to maximize a satisfaction criterion established by the portfolio manager.
Within this framework, we have [daniel2025portfolio, meucci2005risk]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=1Npn=1,pn≥0.\sum\_{n=1}^{N}p\_{n}=1\quad,\quad p\_{n}\geq 0. |  | (1) |

We suppose that information about each asset AnA\_{n} at the time the portfolio is constructed can be estimated (usually from past data), and takes the form of a list of LL values related to various features of an asset (for example the expected return, cost, etc of an asset).
These values can be arranged into a column vector Y→n\vec{Y}\_{n}. The vectors Y→n\vec{Y}\_{n} are concatenated into a L×NL\times N matrix Y¯=[Y→1​…​Y→N]\underline{Y}=[\vec{Y}\_{1}\ldots\vec{Y}\_{N}].
A number of constraints—assumed here to be linear functions of both P→\vec{P} and Y¯\underline{Y}, such as maximum percentage limits for each asset— can be considered and restrict the set of feasible P→\vec{P}. These constraints are expressed in the form of a matrix inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | M¯​Y¯​P→≤C→,\underline{M}\,\ \underline{Y}\,\ \vec{P}\leq\vec{C}, |  | (2) |

where M¯\underline{M} is a matrix and C→\vec{C} is a column vector. The matrix M¯\underline{M} determines which rows (i.e., which types of information) within the Y→n\vec{Y}\_{n} the constraints pertain to, and the multiplication by P→\vec{P} specifies which relationships between the pnp\_{n} must be bounded by the elements of vector C→\vec{C}.

In practice, certain information—such as the expected return and sometimes the expected cost—is not known exactly at the time the portfolio is constructed. To account for possible variability, it is common to have a set of SS different values for each asset feature gathered in Y¯\underline{Y}, corresponding to possible scenarios [daniel2025portfolio, meucci2005risk].
In practical terms, Y¯\underline{Y} can therefore be considered as a scenario-dependent matrix, denoted Y¯​(s)\underline{Y}(s).
The first step in PO is to model relevant data Y¯​(s)\underline{Y}(s) at the given time horizon.

To optimize the portfolio selection, the portfolio manager must define a criterion
that quantifies their satisfaction with the chosen portfolio once specific values of the portfolio features Y¯​(s)\underline{Y}(s) become known (only one of the scenarios being effectively realized after the considered time step). Let us denote by Z¯\underline{Z} these values [daniel2025portfolio, meucci2005risk].
This criterion usually takes the form a scalar function that we call a gain function, denoted as g​(P→,Z¯)g(\vec{P},\underline{Z}):

* •

  Often, the indicator chosen is a measure of the portfolio total return, which can be expressed as [gunjan2023brief]:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | g​(P→,Z¯)=∑n=1Npn​zn,g(\vec{P},\underline{Z})=\sum\_{n=1}^{N}p\_{n}z\_{n}, |  | (3) |

  where znz\_{n} represents the realized return for asset AnA\_{n} (Z¯\underline{Z} is then ‘at least’ a one-row matrix), corresponding to one of the entries of the vector Y→n\vec{Y}\_{n}.
* •

  Alternative gain measure, such as ROI, may also be considered without altering the subsequent framework (but numerical caution must be taken as the problem becomes non-linear). The gain function then takes the form:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | g​(P→,Z¯)=∑n=1Npn​zn,1∑n=1Npn​zn,2,g(\vec{P},\underline{Z})=\frac{\sum\_{n=1}^{N}p\_{n}z\_{n,1}}{\sum\_{n=1}^{N}p\_{n}z\_{n,2}}, |  | (4) |

  where zn,1z\_{n,1} denotes the realized return for asset AnA\_{n}, and zn,2z\_{n,2} corresponds to the realized cost for that asset (Z¯\underline{Z} is then ‘at least’ a two-rows matrix).

### 2.2 Statistical Interpretation Choice and Gain PDF

Naturally, the values of Z¯\underline{Z} are not known at the time of portfolio construction; information about them is only available through scenario-dependent vectors Y→n​(s)\vec{Y}\_{n}(s) for each scenario ss. Consequently, it is necessary to adopt an interpretation to utilize the collection of scenario matrices Y¯​(s)\underline{Y}(s) [meucci2005risk, daniel2025portfolio]. A common practice in PO is to adopt a statistical framework, which, while seemingly straightforward, is essential to the subsequent arguments. The key implications of this framework are as follows:

1. 1.

   The different values of each Y→n​(s)\vec{Y}\_{n}(s) across scenarios ss are considered independent and identically distributed (i.i.d.) realizations of the same data random vector 𝐘→n\vec{\mathbf{Y}}\_{n} (where bold notation indicates random variables).
2. 2.

   The various gain and risk measures optimized in PO must be evaluated statistically over the scenarios indexed by ss, as result from a specific realization does not carry particular significance.
3. 3.

   The ordering of scenarios or realizations of the data random vector Y→n​(1),…,Y→n​(S)\vec{Y}\_{n}(1),\ldots,\vec{Y}\_{n}(S) is entirely arbitrary; thus, our calculations must be invariant to any permutation of the scenario index ss. While representing the data as a matrix-valued function Y¯​(s)\underline{Y}(s) is convenient, it is not strictly necessary.

Given this framework, the portfolio selection process requires applying the gain function g​(⋅,⋅)g(\cdot,\cdot) to the random matrix 𝐘¯\underline{\mathbf{Y}}. As a result, g​(P,𝐘¯)g(P,\underline{\mathbf{Y}}) becomes a real-valued r.v. [meucci2005risk], which is more tractable than when using the full matrix Y¯​(s)\underline{Y}(s). The probability distribution of this variable—supplemented, of course, by the imposed constraints—contains all the information needed to devise an optimal portfolio selection method.

For technical reasons that are not especially restrictive, we assume that for any P→\vec{P}, this distribution has a PDF with respect to the Lebesgue measure [bartle2014elements], denoted by :

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(P→,u),\sigma(\vec{P},u), |  | (5) |

where uu is the real variable associated with the gain. Due to the choice of a statistical framework, this PDF is the fundamental object in the PO problem: all relevant quantities for defining the problem can and should be constructed from it.
We call this object the gain PDF, which has the advantage of being 1-dimensional for any portfolio.

### 2.3 Objective Function Conventional Approach

The selection of optimal portfolios is carried out by optimizing an objective function, which itself is a function of the PDF σ​(P→,u)\sigma(\vec{P},u). This objective function translates an operational choice made by the portfolio manager.

The most common choice is to seek a balance between average gains and risks, which represents a multi-objective optimization whose solution is an efficient frontier [daniel2025portfolio].
For practical purpose, the problem can equivalently be expressed as a single-objective optimization, the objective being expressed as a linear combination:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(σ)=(1−a)×gain​(σ)−a×risk​(σ),F\_{a}(\sigma)=(1-a)\times\text{gain}(\sigma)-a\times\text{risk}(\sigma), |  | (6) |

where a∈[0,1]a\in[0,1] represents a risk aversion weight, controlling the trade-off between the gain and risk.
We then seek the optimal portfolios,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | P→a∗=argmaxP→Fa(σ(P→,.))\displaystyle\vec{P}\_{a}^{\*}=\arg\max\_{\vec{P}}F\_{a}(\sigma(\vec{P},.)) |  |  |
|  |  | s.t.pn≥0,∑npn=1,M¯Y¯P→≤C→\displaystyle s.t.\quad p\_{n}\geq 0,\quad\sum\_{n}p\_{n}=1,\quad\underline{M}\,\ \underline{Y}\,\ \vec{P}\leq\vec{C} | . |  |

The obtained set {P→a∗}\{\vec{P}\_{a}^{\*}\} for many (ideally all) values of aa are related to the efficient frontier sampling.
From posterior analysis, we finally select the specific portfolio (or value of aa) that we prefer to finalize the choice of the definitive portfolio.

The first to propose such an approach was Markowitz [markowitz1952portfolio], who considered for gain​(σ)\text{gain}(\sigma) the expected gain expressed as a mean value of the gain function g(.,.)g(.,.), and for risk​(σ)\text{risk}(\sigma) the variance of g(.,.)g(.,.). Formulated in terms of the gain PDF, the Markowitz approach leads to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | gain​(σ)=∫u​ ​σ​(P→,u)​ ​𝑑u,\text{gain}(\sigma)=\int u\text{ }\sigma(\vec{P},u)\text{ }du, |  | (8) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | riskM​a​r​k​(σ)=∫u2​ ​σ​(P→,u)​ ​𝑑u−gain​(σ)2,\text{risk}\_{Mark}(\sigma)=\int u^{2}\text{ }\sigma(\vec{P},u)\text{ }du-\text{gain}(\sigma)^{2}, |  | (9) |

where the variance has been considered in eq. ([9](https://arxiv.org/html/2512.11649v1#S2.E9 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
Even if equivalent to the formulation in eq. ([9](https://arxiv.org/html/2512.11649v1#S2.E9 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), the original formulation of Markowitz considered a linear gain function g(.,.)g(.,.) and it is not straightforward in his formulation to generalize the variance term to a non-linear gain function like a ROI, eq. ([4](https://arxiv.org/html/2512.11649v1#S2.E4 "In 2nd item ‣ 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
Interestingly, the formulation in terms of the gain PDF naturally generalizes the Markowitz variance, eq. ([9](https://arxiv.org/html/2512.11649v1#S2.E9 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), to non-linear gain functions.
So, the formulation in terms of the gain PDF seems more general.
Indeed, due to the choice of dealing with a statistical framework, the gain PDF represents the object containing the most exhaustive information on the PO problem.

As mentioned in the introduction, the Markowitz risk measured as a variance leads to various pathologies and many proposal have been done to improve this measure.
Among these, the CVaR-deviation [rockafellar2002deviation] allows us to compute a loss-side deviation from the average gains:

|  |  |  |  |
| --- | --- | --- | --- |
|  | riskC​d​e​vβ​(σ)=C​V​a​Rβ​(σ)−g​a​i​n​(σ),\text{risk}\_{Cdev\_{\beta}}(\sigma)=CVaR\_{\beta}(\sigma)-gain(\sigma), |  | (10) |

where CVaR seeks to quantify the average risk of losses related to a confidence level 1−β1-\beta with β∈]0,1[\beta\in]0,1[ (in practice β\beta is chosen close to one so that only low probability events but with strong losses are accounted for) [rockafellar2000optimization, rockafellar2002deviation]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​V​a​Rβ​(σ)=minα⁡α+11−β​∫R​e​L​U​(u−α)​ ​σ​(P→,u)​ ​𝑑u.CVaR\_{\beta}(\sigma)=\min\_{\alpha}\alpha+\frac{1}{1-\beta}\int ReLU(u-\alpha)\text{ }\sigma(\vec{P},u)\text{ }du. |  | (11) |

These examples illustrate the central role of the gain PDF σ(.,.)\sigma(.,.) in conventional PO and the fact that any objective can be expressed as a function of this object.
However, we notice that conventional PO methods extract only a limited set of numerical values with business significance to define the objective function, through expectations, allowing to capture only limited features of the gain PDF.
As mentioned in the introduction, it has been proposed to consider few higher-order moments of the gain PDF but this still remains limited to a few additional average quantities.
Accounting for more exhaustive information contained in the gain PDF thus seems to remain an open question.

## 3 New Approach Leveraging the Gain PDF

### 3.1 Objective Function

We now go further and propose an innovative and flexible approach by granting the portfolio manager maximum freedom to express their expectations regarding the distribution of profits and losses. Specifically, this means allowing the user to define their own target gain PDF, denoted as

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt​(u),\sigma\_{t}(u), |  | (12) |

which represents the ideal PDF they would like to achieve (which is not necessarily an easy task but a constructive method will be proposed further).
In practice, the goal will be to approximate this ideal target, since the finite number of degrees of freedom (the pnp\_{n} together with the constraints) do not give enough flexibility to attain exactly any arbitrary PDF.

An objective function to achieve this task must be a measure of the mismatch between the gain PDF and this ideally desired PDF, called the target PDF in the following. This measure, which we seek to minimize, quantifies how close the gain PDF is to the target PDF. Clearly, this approach provides the portfolio manager with a richer means of expressing their optimality requirements compared to previous methods, which relied on only few (usually two) expectations computed using the gain PDF.

It then remains to choose a suitable discrepancy measure D​(σ​(P→,⋅);σt​(⋅))D(\sigma(\vec{P},\cdot)\,;\,\sigma\_{t}(\cdot)) between the gain distribution produced by the portfolio and the target distribution. The PO problem can then be formulated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P→t∗=arg⁡minP→=D​(σ​(P→,⋅);σt​(⋅))\displaystyle\vec{P}^{\*}\_{t}=\arg\min\_{\vec{P}}=D\big(\sigma(\vec{P},\cdot)\,;\,\sigma\_{t}(\cdot)\big) |  | (13) |
|  |  |  |
| --- | --- | --- |
|  | s.t.pn≥0,∑npn=1,M¯Y¯P→≤C→.\displaystyle s.t.\quad p\_{n}\geq 0,\quad\sum\_{n}p\_{n}=1,\quad\underline{M}\,\ \underline{Y}\,\ \vec{P}\leq\vec{C}. |  |

The discrepancy measure must be carefully selected, as the obtained optimal portfolio P→t∗\vec{P}^{\*}\_{t} will depend on this choice.
Various choices are possible, each with their own characteristics:

* •

  The Kullback-Leibler divergence [kullback1951information] allows us to evaluate a mismatch between two PDFs:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | D(σ(P→,.);σt(.))=∫−∞∞σt(u)log(σ​(P→,u)σt​(u))du.D\big(\sigma(\vec{P},.);\sigma\_{t}(.)\big)=\int\_{-\infty}^{\infty}\sigma\_{t}(u)\log\bigg(\frac{\sigma(\vec{P},u)}{\sigma\_{t}(u)}\bigg)du. |  | (14) |

  Despite its widespread use—mainly due to its low computational cost—the Kullback-Leibler divergence is not the most suitable for our problem. Indeed, it has the drawback of not allowing a weighting of the matching in the uu direction. In other terms, the user cannot constrain to better match only a specific part of the PDF, but rather must constrain the entire PDF, which requires a very precise knowledge of the target (thus of the solution, which is inconsistent…) to achieve this.
* •

  Another option is to use a Wasserstein distance [villani2009wasserstein], but it is more computationally expensive.
* •

  Finally, an LpL\_{p} norm [rachev1995probability] raised to the power pp (with p≥1p\geq 1) can also be used:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | D(σ(P→,.);σt(.))=∫−∞∞θ(u) |σ(P→,u)−σt(u)|p du.D\big(\sigma(\vec{P},.);\sigma\_{t}(.)\big)=\int\_{-\infty}^{\infty}\theta(u)\text{ }|\sigma(\vec{P},u)-\sigma\_{t}(u)|^{p}\text{ }du. |  | (15) |

  It has the advantage of being inexpensive to compute and, more importantly, allows us to naturally introduce a weighting function θ​(u)\theta(u) to foster the matching of only specific parts of the target PDF in the optimization.

We choose the latter discrepancy measure for D(σ(P→,.);σt(.))D(\sigma(\vec{P},.);\sigma\_{t}(.)) with p=2p=2 (squared L2-norm) [stein2009real] and θ​(u)∈[0,1]\theta(u)\in[0,1] (e.g. the sigmoid function) to specify which part of the PDF is important to approximate as closely as possible (θ​(u)\theta(u) close to 11), and which part of the PDF can be given more leeway (θ​(u)\theta(u) close to 0).
In other terms, the target PDF must be precisely defined for the part where θ​(u)\theta(u) close to 11 only. An application targeting high-gains (which are not accounted for in the conventional PO scheme) will be proposed further.

### 3.2 Estimator Choice

The formulations above still do not allow us to solve the PO problem, i.e. to find the optimal portfolios through eq. ([2.3](https://arxiv.org/html/2512.11649v1#S2.Ex1 "2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) or eq. ([13](https://arxiv.org/html/2512.11649v1#S3.E13 "In 3.1 Objective Function ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
Indeed, the gain PDF σ​(P→,u)\sigma(\vec{P},u) form is not known a priori.
It is necessary to specify how we will express the gain PDF as a function of the data available to us, that is, to choose its estimation based on portfolio assets features values from each scenario, which requires an explicit statistical model.

To constrain the form of an estimator of the gain PDF, we consider first that the order in which the scenarios appear is arbitrary, as explained in section [2.2](https://arxiv.org/html/2512.11649v1#S2.SS2 "2.2 Statistical Interpretation Choice and Gain PDF ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"), so that the estimator must be a function of g​(P→,Y¯​(s))g(\vec{P},\underline{Y}(s)) that is invariant under permutation of the scenarios indexed by ss. The distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(P→,u)=1S​∑s=1Sδ​(u−g​(P→,Y¯​(s))),h(\vec{P},u)=\frac{1}{S}\sum\_{s=1}^{S}\delta\Big(u-g(\vec{P},\underline{Y}(s))\Big), |  | (16) |

therefore represents a sufficient statistics [lehmann1998theory]. We call it the ‘gain histogram’ by slight abuse of language.
The convolution of hh with a rectangular function of defined width gives the gain histogram in the common sense of the term, our gain histogram representing the limit of the common gain histogram when the rectangle’s width is infinitesimal [silverman2018density].
All our estimators must be functions of the gain histogram h​(P→,u)h(\vec{P},u).

Secondly, it is important to differentiate two cases:

* •

  When it comes to estimating expectation values, it is natural, for large number of available scenarios SS, to use the empirical means or averages over the scenarios, related to considering eq. ([16](https://arxiv.org/html/2512.11649v1#S3.E16 "In 3.2 Estimator Choice ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) as the probability distribution.
  Let us take the example of the Markowitz [markovitz1959portfolio] or CVaR-based [rockafellar2000optimization] components of the objective function that are expressed as expectations, remind eqs. ([8](https://arxiv.org/html/2512.11649v1#S2.E8 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), ([9](https://arxiv.org/html/2512.11649v1#S2.E9 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) and ([11](https://arxiv.org/html/2512.11649v1#S2.E11 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
  Using eq. ([16](https://arxiv.org/html/2512.11649v1#S3.E16 "In 3.2 Estimator Choice ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) allows us to recover the conventional formulations in terms of averages over scenarios [markowitz1952portfolio, rockafellar2000optimization, rockafellar2002deviation]:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | gain(σ(P→,.))≈gain(h(P→,.))=1S∑s=1Sg(P→,Y¯(s)),\text{gain}(\sigma(\vec{P},.))\approx\text{gain}(h(\vec{P},.))=\frac{1}{S}\sum\_{s=1}^{S}g(\vec{P},\underline{Y}(s)), |  | (17) |

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | riskM​a​r​k(σ(P→,.))≈riskM​a​r​k(h(P→,.))=1S∑s=1Sg(P→,Y¯(s))2−gain(σ)2,\text{risk}\_{Mark}(\sigma(\vec{P},.))\approx\text{risk}\_{Mark}(h(\vec{P},.))={\frac{1}{S}\sum\_{s=1}^{S}g(\vec{P},\underline{Y}(s))^{2}-\text{gain}(\sigma)^{2}}, |  | (18) |

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | CVaRβ(σ(P→,.))≈CVaRβ(h(P→,.))=minαα+11−β1S∑s=1SReLU(g(P→,Y¯(s))−α).CVaR\_{\beta}(\sigma(\vec{P},.))\approx CVaR\_{\beta}(h(\vec{P},.))=\min\_{\alpha}\alpha+\frac{1}{1-\beta}\frac{1}{S}\sum\_{s=1}^{S}ReLU(g(\vec{P},\underline{Y}(s))-\alpha). |  | (19) |

  Again, eq. ([18](https://arxiv.org/html/2512.11649v1#S3.E18 "In 1st item ‣ 3.2 Estimator Choice ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) naturally generalizes the Markowitz scheme (including the expectations estimations) to non-linear gain functions like ROI-based ones.
* •

  When it comes to estimating an entire function, here the gain PDF, things are not that simple (h(P→,.)h(\vec{P},.) cannot be directly taken as the estimator) and several possibilities exist.
  We now demonstrate that we can drastically reduce the choice of possible estimators using arguments that stem from the problem itself and from the hypotheses we have already made.

The estimation of the gain PDF is represented by an operator acting on the gain histogram that we denote as G​(h)​(v)G(h)(v).
To be an estimator of a PDF, G​(h)​(v)G(h)(v) must be positive and its integral must be equal to 1. We will therefore seek GG in the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(h)=F​(h)∫F​(h)​(v)​𝑑v.G(h)=\frac{F(h)}{\int F(h)(v)dv}. |  | (20) |

Under very reasonable hypotheses explicated in the demonstration below, we show that FF must be expressed as a convolution product
111Translation invariance suggests that, instead of the gain histogram, we could consider its Fourier Transform as the fundamental statistic of the problem and thus also the gain characteristic function instead of the gain PDF. Detailing this goes beyond the scope of the article.
:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(h)​(v)=∫K​(v−u)​ ​h​(u)​ ​𝑑u,F(h)(v)=\int K(v-u)\text{ }h(u)\text{ }du, |  | (21) |

where K(.)K(.) represents a chosen the convolution kernel [hardle2012smoothing].
For instance and as already mentioned, if K(.)K(.) is chosen as a rectangular function, F​(h)​(v)F(h)(v) a gain histogram in the common sense of the term.

G​(h)G(h) can therefore be considered as an estimator of the gain PDF using the kernel method [silverman2018density], which in itself is not a novel technique. However, it is worth noting that the form of the gain PDF estimator is quite constrained by the problem’s structure, as well as some fairly natural additional assumptions.
The kernel K(.)K(.) is thus the only degree of freedom of the gain PDF estimator.

Note that we could further constrain K(.)K(.) and require, for reasons of symmetry, that it must be sought within the class of even functions with quasi-bounded support. Finally, kernels such as Gaussian, Triangle, etc [hardle2012smoothing]. The final result should not depend much on the choice of the kernel to first order (which we verified in many practical cases).

□\Box Demonstration that K(.)K(.) must be a convolution kernel under mild hypotheses. We can constrain the G​(h)G(h) based on two observations that seem naturally suited to our problem:

* •

  Adding the same value ww to each samples u​(s)u(s) of the gain PDF σ(.,u)\sigma(.,u) should corresponds to a samples drawn from a PDF σ′(.,u)=σ(.,u−w)\sigma^{\prime}(.,u)=\sigma(.,u-w). The related gain histogram is hw(.,u)=h(.,u−w)h\_{w}(.,u)=h(.,u-w), which represents a translated version by an amount ww. GG must thus estimate σw\sigma\_{w} as effectively as σ\sigma and it is legitimate to require that GG (and thus FF) must be a translation-invariant operator:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | G(h(⋅,⋆−w))(v)=G(h(⋅,⋆))(v−w)G\Big(h(\cdot,\star-w)\Big)(v)=G(h(\cdot,\star))(v-w) |  | (22) |
* •

  The scenarios or samples should be interpretable as drawn from a mixture of PDFs. More precisely, we suppose that if the scenarios consist of two types of samples drawn from the PDFs σ1\sigma\_{1} and σ2\sigma\_{2} in proportions γ\gamma and (1−γ)(1-\gamma), the overall samples can be considered as drawn from the single PDF σ3=γ​σ1+(1−γ)​σ2\sigma\_{3}=\gamma\sigma\_{1}+(1-\gamma)\sigma\_{2}. This leads to h3=γ​h1+(1−γ)​h2h\_{3}=\gamma h\_{1}+(1-\gamma)h\_{2} for the corresponding gain histogram.
  It is legitimate to require that:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | G​(h3)=G​(γ​h1+(1−γ)​h2)=γ​G​(h1)+(1−γ)​G​(h2),G(h\_{3})=G\Big(\gamma h\_{1}+(1-\gamma)h\_{2}\Big)=\gamma G(h\_{1})+(1-\gamma)G(h\_{2}), |  | (23) |

  so that G​(h)G(h) can estimate σ3\sigma\_{3} using h3=γ​h1+(1−γ)​h2h\_{3}=\gamma h\_{1}+(1-\gamma)h\_{2} in addition to estimating σ1\sigma\_{1} and σ2\sigma\_{2} using h1h\_{1} and h2h\_{2}.
  The condition in eq. ([23](https://arxiv.org/html/2512.11649v1#S3.E23 "In 2nd item ‣ 3.2 Estimator Choice ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) is satisfied if we require F​(h)F(h) to be a linear operator
  222Indeed, the translation invariance combined with the linearity of FF implies that the normalization coefficient in eq. ([20](https://arxiv.org/html/2512.11649v1#S3.E20 "In 3.2 Estimator Choice ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) takes the same value for G​(γ​h1+(1−γ)​h2)G(\gamma h\_{1}+(1-\gamma)h\_{2}) and G​(h)G(h).
  .

FF must therefore be sought within the class of linear operators that are equivariant under translation, so FF can be expressed as a convolution product. □\Box

### 3.3 Full Specification of the New Optimization Problem

We now have everything needed to fully establish the objective function in eq. ([13](https://arxiv.org/html/2512.11649v1#S3.E13 "In 3.1 Objective Function ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) related to our new proposal, from the problem data or scenarios. The steps are the following:

* •

  A target PDF σt​(v)\sigma\_{t}(v) is first specified by the user, that needs to be accurate only on the part the user would like to precisely match (this can be challenging for the user but a constructive method will be proposed further).
* •

  For any portfolio P→\vec{P} and a chosen convolution kernel K(.)K(.), an estimation σ^​(P→,v)\hat{\sigma}(\vec{P},v) of the gain PDF based on the form we derived for G​(h)​(v)G(h)(v) and the scenarios Y¯​(s)\underline{Y}(s) is computed:

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | σ^​(P→,v)\displaystyle\hat{\sigma}(\vec{P},v) | =\displaystyle= | ∫K​(v−u)​ ​h​(P→,u)​ ​𝑑uα​(P→)\displaystyle\frac{\int K(v-u)\text{ }h(\vec{P},u)\text{ }du}{\alpha(\vec{P})} |  | (24) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | h​(P→,u)\displaystyle h(\vec{P},u) | =\displaystyle= | 1S​∑s=1Sδ​(u−g​(P→,Y¯​(s)))\displaystyle\frac{1}{S}\sum\_{s=1}^{S}\delta\Big(u-g(\vec{P},\underline{Y}(s))\Big) |  |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | α​(P→)\displaystyle\alpha(\vec{P}) | =\displaystyle= | ∫K​(v−u)​ ​h​(P→,u)​ ​𝑑u​ ​𝑑v.\displaystyle\int K(v-u)\text{ }h(\vec{P},u)\text{ }du\text{ }dv. |  |
* •

  A L2-based measure of the discrepancy between the estimator of the gain PDF and the target PDF is computed:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | D(σ^(P→,.);σt(.))=∫−∞∞θ(v) |σ^(P→,v)−σt(v)|2 dv.D(\hat{\sigma}(\vec{P},.);\sigma\_{t}(.))=\int\_{-\infty}^{\infty}\theta(v)\text{ }|\hat{\sigma}(\vec{P},v)-\sigma\_{t}(v)|^{2}\text{ }dv. |  | (25) |

  This measure must be minimized under constraints to determine the optimal P→t∗\vec{P}\_{t}^{\*}, eq. ([13](https://arxiv.org/html/2512.11649v1#S3.E13 "In 3.1 Objective Function ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
  θ​(v)\theta(v) represents a user-defined sigmoid-based weight that indicates which part of the target PDF must be precisely matched.

The remaining non-trivial task is to build a pertinent target PDF, corresponding to an operational need.
We now propose a methodology and an application targeting high-gains, which are not accounted for in the conventional PO scheme.

## 4 A Proposed Application: Constraining High Gains

### 4.1 Operational Context and Options

We wish to address the following operational issue: In conventional PO methods such as Markowitz [markowitz1952portfolio, markovitz1959portfolio] or CVaR-based [rockafellar2000optimization, rockafellar2002deviation] PO, the choice of a portfolio is determined by a trade-off between average return and risk. However, the portfolio manager may want to include a small portion of risky assets with high potential profits.
These assets are most probably not selected by conventional PO, as they usually carry a higher risk of significant losses and no term fostering specifically the high returns is usually included in the optimization.

Two approaches are available for redefining the objective function of the problem:

* •

  The first approach builds on the method proposed in section [2.3](https://arxiv.org/html/2512.11649v1#S2.SS3 "2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") and eq. ([2.3](https://arxiv.org/html/2512.11649v1#S2.Ex1 "2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
  If the portfolio manager is not fully satisfied with the assets selected form an initial conventional PO step,
  a third average term in the objective function ([6](https://arxiv.org/html/2512.11649v1#S2.E6 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) might be added to integrate, for example, a CVaR-type term for high returns (in the same spirit that eq. ([19](https://arxiv.org/html/2512.11649v1#S3.E19 "In 1st item ‣ 3.2 Estimator Choice ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) but focused on the profit-side tail of the PDF). Similar to the risk aversion weight for the risk term, an additional weight that favors strong and risky profits must be defined.
  The PO is then solved again considering this ‘augmented’ objective function; it is to be noted that the optimization solver might be adapted and the computational cost of the optimization might be strongly increased.
  Indeed, introducing an additional CVaR term focused on the return-side tail of the PDF might result in a minimax problem.
* •

  The second approach, which we propose, builds on the new method described in section [3.3](https://arxiv.org/html/2512.11649v1#S3.SS3 "3.3 Full Specification of the New Optimization Problem ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications").
  We still suppose that an initial conventional PO step has been performed, and would like to explore ‘perturbations’ around the selected portfolio Pa∗P^{\*}\_{a}. In this case, the user can compute the estimate σ^​(P→a∗,v)\hat{\sigma}(\vec{P}^{\*}\_{a},v) of the gain PDF for the optimal portfolio, and is thus well positioned to define from it a target PDF σt​(v)\sigma\_{t}(v) by applying a perturbation to it, for instance increasing the profit-side of σ^​(P→a∗,v)\hat{\sigma}(\vec{P}^{\*}\_{a},v) in a fully controlled way. Relaxing the loss-side is made possible by adapting the sigmoid-based weight θ​(v)\theta(v) (here close to 11 for gains and close to 0 for losses). Once the target σt​(v)\sigma\_{t}(v) defined, the problem is then posed as in section [3.3](https://arxiv.org/html/2512.11649v1#S3.SS3 "3.3 Full Specification of the New Optimization Problem ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") and eq. ([13](https://arxiv.org/html/2512.11649v1#S3.E13 "In 3.1 Objective Function ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), with the additional aspect that we seek a corrective adjustment to the initial portfolio.
  This makes an iterative local-optimization method initialized with P→a∗\vec{P}^{\*}\_{a} appropriate,
  as described in next section,
  which has the advantage of a reasonable numerical cost.

### 4.2 Projected Gradient Algorithm

Since the goal is to apply a correction to an already optimized portfolio, we consider an iterative
projected gradient scheme [bertsekas1999nonlinear]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P→k+1=P→k−κ×dP→k,P→k=0=P→a∗,\vec{P}\_{k+1}=\vec{P}\_{k}-\kappa\times d\vec{P}\_{k}\quad,\quad\vec{P}\_{k=0}=\vec{P}\_{a}^{\*}, |  | (26) |

where d​P→kd\vec{P}\_{k} represents a projected gradient and κ\kappa the descent step. It is not possible to take directly for d​P→kd\vec{P}\_{k} the gradient [bertsekas1999nonlinear]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇→(P→)​D​(σ^​(P→,⋅);σt​(⋅)).\vec{\nabla}\_{(\vec{P})}D(\hat{\sigma}(\vec{P},\cdot);\sigma\_{t}(\cdot)). |  | (27) |

Indeed, the constraints in eq. ([13](https://arxiv.org/html/2512.11649v1#S3.E13 "In 3.1 Objective Function ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) are not explicitly accounted for by a standard gradient descent, meaning that modifying P→k\vec{P}\_{k} into P→k+1\vec{P}\_{k+1} could (and in practice will) result in a violation of these constraints.
A solution is to use the projected gradient technique,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​P→k=Proj¯k​∇→(P→)​D​(σ^​(P→,⋅);σt​(⋅)),d\vec{P}\_{k}=\underline{\text{Proj}}\_{k}\vec{\nabla}\_{(\vec{P})}D(\hat{\sigma}(\vec{P},\cdot);\sigma\_{t}(\cdot)), |  | (28) |

where the projector Proj¯k\underline{\text{Proj}}\_{k} ensures each obtained P→k+1\vec{P}\_{k+1} satisfy all constraints.
The projector is defined adaptively:

* •

  First, we identify the constraints that become violated when moving from k−1k-1 to kk in a conventional gradient scheme and denote by dkd\_{k} the corresponding number of constraints. These constraints must be re-identified at each iteration, leading to a non-linearity and justifying the term ‘adaptive’.
* •

  Since all constraints we consider are linear in P→\vec{P}, they can be interpreted as scalar products of vectors with P→\vec{P}. We gather these vectors for the pn≥0p\_{n}\geq 0 and M¯​Y¯​P→≤C→\underline{M}\,\ \underline{Y}\,\ \vec{P}\leq\vec{C} violated constraints in a matrix (V→1,…,V→c)(\vec{V}\_{1},\ldots,\vec{V}\_{c}) (to avoid overloading the notation the dependence of the V→i\vec{V}\_{i} on kk is not made explicit).
  We must also respect the portfolio constraint ∑n=1Npn=1\sum\_{n=1}^{N}p\_{n}=1, which is interpreted as the scalar product of P→\vec{P} with the vector V→0=(1,…,1)\vec{V}\_{0}=(1,\ldots,1); the latter constraint will most probably always be violated so that V→0\vec{V}\_{0} will always be part of the set.
  The set of vectors (V→0,V→1,…,V→d)(\vec{V}\_{0},\vec{V}\_{1},\ldots,\vec{V}\_{d}) generates a vector subspace EE spanned by (e→0,…,e→d′)(\vec{e}\_{0},\ldots,\vec{e}\_{d^{\prime}}) (d′≤dd^{\prime}\leq d denotes the number of independent constraints).
  The idea is then to project the standard gradient vector onto the vector subspace orthogonal to EkE\_{k} (re-injecting the kk dependence which illustrates that the violated constraints may not always be the same from one iteration to the other), with the corresponding projector defined by:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Proj¯k=I¯−Q​(k)¯Q​(k)¯T,Q​(k)¯=(e→0(k),…,e→dk′(k))\underline{\text{Proj}}\_{k}=\underline{I}-\underline{Q(k)}\,\ \underline{Q(k)}^{T}\quad,\quad\underline{Q(k)}=(\vec{e}\_{0}(k),\ldots,\vec{e}\_{d\_{k}^{\prime}}(k)) |  | (29) |

  Then, the scalar products of the projected gradient with each of the V→i\vec{V}\_{i} is ensured to be zero, so that the obtained P→k+1\vec{P}\_{k+1} will not anymore violate any constraint.

The final adaptively projected gradient scheme is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P→k+1=P→k−κ×(I¯−Q​(k)¯​Q​(k)¯T)​∇→(P→k)​D​(σ^​(P→k,⋅);σt​(⋅)),\vec{P}\_{k+1}=\vec{P}\_{k}-\kappa\times\big(\underline{I}-\underline{Q(k)}\,\ \underline{Q(k)}^{T}\big)\vec{\nabla}\_{(\vec{P}\_{k})}D(\hat{\sigma}(\vec{P}\_{k},\cdot);\sigma\_{t}(\cdot)), |  | (30) |

where the standard gradient vector is numerically estimated by finite differences.
The computationally more expensive point may be that the (e→0​(k),…,e→dk′​(k))(\vec{e}\_{0}(k),\ldots,\vec{e}\_{d\_{k}^{\prime}}(k)) and the projector need to be recalculated at each iteration kk in the worst case. However, since the step size κ\kappa is assumed to be small, it is possible that the violated constraints remain the same as the iterations proceed, and that one only needs to complete the basis of constraint vectors V→i\vec{V}\_{i} defined at iteration kk from the violated constraints with additional vectors from newly violated constraints (and not to remove any vector e→i\vec{e}\_{i}). In this case, the Gram-Schmidt process [strang2012linear] (which is iterative and does not require matrix inversion) allows one to retain most of the calculations from the previous step.
For each kk, one can indeed derive from the vectors V→c\vec{V}\_{c} an orthonormal basis of EkE\_{k} using the Gram-Schmidt process [strang2012linear] initialized with e→0∝V→0\vec{e}\_{0}\propto\vec{V}\_{0}.

We highlight that violations of the positivity constraints for pnp\_{n} can be handled more simply and equivalently, to reduce the computational cost. Indeed, the projector onto the subspace of these particular constraints is diagonal and thus commutes with any other. It is therefore sufficient to project the vectors V→i\vec{V}\_{i} related to the other violated constraints onto this subspace (which is easily done by setting the corresponding entries to zero) before undertaking the Gram-Schmidt process [strang2012linear] on these modified vectors only. The dimension of the projector, and thus the amount of computation required, is accordingly reduced.

### 4.3 Evaluation of Marginal Cost

With the previously described adjustment, we have modified a portfolio P→a∗\vec{P}\_{a}^{\*} that was initially computed to satisfy a conventional PO optimality criterion, i.e. maximizing an ‘original’ objective function as in eqs. ([6](https://arxiv.org/html/2512.11649v1#S2.E6 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"))-([2.3](https://arxiv.org/html/2512.11649v1#S2.Ex1 "2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
The new portfolio P→t∗\vec{P}\_{t}^{\*} is obtained by considering another objective function ,
eq. ([13](https://arxiv.org/html/2512.11649v1#S3.E13 "In 3.1 Objective Function ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), and thus must be sub-optimal according to the original objective function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→t∗)<Fa​(P→a∗),\displaystyle F\_{a}(\vec{P}\_{t}^{\*})<F\_{a}(\vec{P}\_{a}^{\*}), |  | (31) |

where we denote Fa​(h​(P→,⋅))F\_{a}(h(\vec{P},\cdot)) by Fa​(P→)F\_{a}(\vec{P}) to lighten the notations.
The gap Fa​(P→a∗)−Fa​(P→t∗)F\_{a}(\vec{P}\_{a}^{\*})-F\_{a}(\vec{P}\_{t}^{\*}) provides an indication of the trade-offs that are made by adopting the portfolio P→t∗\vec{P}\_{t}^{\*} instead of P→a∗\vec{P}\_{a}^{\*}, as the objective function represents a business satisfaction measure, but this gap is not easy to interpret in terms of ’additional cost’.
We propose a method that addresses this point and the following operational question:
Can we quantify, in ‘additional cost’ terms relevant to the portfolio manager, this loss of optimality?

This question can be encapsulated into a general framework, where the cost is measured in a single ’budget’ unit so that different portfolio modifications can be easily compared (for instance a monetary unit in financial assets cases, an energy unit in energy assets cases, etc).
To begin with, let us consider eqs. ([1](https://arxiv.org/html/2512.11649v1#S2.E1 "In 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"))-([2](https://arxiv.org/html/2512.11649v1#S2.E2 "In 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) and make explicit the case where our portfolio problem is to allocates a given budget BB (or investment) among assets.
We assume that in the Y→n\vec{Y}\_{n} data features vectors, one of the entry quantifies the cost yny\_{n} to buy one unit of asset AnA\_{n}.
The fundamental portfolio problem is to find the quantities xnx\_{n} of each asset to buy w.r.t. a given budget BB:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n=1Nxnyn=B,xn≥0,\sum\_{n=1}^{N}x\_{n}y\_{n}=B\quad,\quad x\_{n}\geq 0, |  | (32) |

instead of eq. ([1](https://arxiv.org/html/2512.11649v1#S2.E1 "In 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), with inequality constraints acting on XX instead of eq. ([2](https://arxiv.org/html/2512.11649v1#S2.E2 "In 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")). Then, doing the variable change

|  |  |  |  |
| --- | --- | --- | --- |
|  | pn=xn​ynB,p\_{n}=x\_{n}\frac{y\_{n}}{B}, |  | (33) |

leads to the notations of section [2.1](https://arxiv.org/html/2512.11649v1#S2.SS1 "2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications").
This allows us to understand that the optimal objective function values, and portfolio P→a∗\vec{P}^{\*}\_{a} and P→t∗\vec{P}^{\*}\_{t} must be considered as functions of the budget BB:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P→a∗(B),P→t∗(B).\vec{P}^{\*}\_{a}(B)\quad,\quad\vec{P}\_{t}^{\*}(B). |  | (34) |

In many PO cases, the role of BB is crucial. This is especially true with energy assets PO where many inequality constraints are necessary (related to a a maximum possible energy production per asset) and can often be saturated, and a non-linear gain function is used (e.g. ROI). All this leads to a non-trivial dependency of P→a∗​(B)\vec{P}^{\*}\_{a}(B) and the objective function on BB.

Now that the meaning of the budget BB has been clarified, we come back to the original PO problem objective function,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→)=(1−a)×gain​(P→)+a×risk​(P→),F\_{a}(\vec{P})=(1-a)\times\text{gain}(\vec{P})+a\times\text{risk}(\vec{P}), |  | (35) |

where the risk term can for instance be the CVaR-deviation, riskC​d​e​vβ​(P→)\text{risk}\_{Cdev\_{\beta}}(\vec{P}), eqs. ([10](https://arxiv.org/html/2512.11649v1#S2.E10 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"))-([11](https://arxiv.org/html/2512.11649v1#S2.E11 "In 2.3 Objective Function Conventional Approach ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")),
and to eq. ([31](https://arxiv.org/html/2512.11649v1#S4.E31 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→t∗​(B))<Fa​(P→a∗​(B)).\displaystyle F\_{a}(\vec{P}\_{t}^{\*}(B))<F\_{a}(\vec{P}\_{a}^{\*}(B)). |  | (36) |

We note that the Fa​(P→t∗)F\_{a}(\vec{P}\_{t}^{\*}) lower value could have been achieved by optimizing the initial objective function while accounting for a budget B−Δ​BtB-\Delta B\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→t∗​(B))=Fa​(P→a∗​(B−Δ​Bt)).F\_{a}\big(\vec{P}\_{t}^{\*}(B)\big)=F\_{a}\big(\vec{P}\_{a}^{\*}(B-\Delta B\_{t})\big). |  | (37) |

We can then search for the Δ​Bt\Delta B\_{t} that solves the previous equation.
Practically, we calculate the optimal portfolios Fa​(P→a∗​(B−Δ​B))F\_{a}(\vec{P}\_{a}^{\*}(B-\Delta B)) for various Δ​B\Delta B values by running various optimizations considering the original objective function with a constant risk-aversion value of aa (parallel computing [severance2010high] is an ideal tool here). We then select the specific Δ​Bt\Delta B\_{t} value that allows us to satisfies eq. ([37](https://arxiv.org/html/2512.11649v1#S4.E37 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).

Δ​Bt\Delta B\_{t} can be interpreted as a cost of sub-optimality, here called marginal cost, representing the common budget unit we were searching for.
Intuitively, considering an identical objective function value as in eq. ([37](https://arxiv.org/html/2512.11649v1#S4.E37 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) means considering an identical business satisfaction measure.
Δ​Bt\Delta B\_{t} can thus be interpreted as the investment amount the portfolio manager would save in the original problem to obtain a business satisfaction value identical to the one related to P→t∗​(B)\vec{P}\_{t}^{\*}(B).
Conversely, Δ​Bt\Delta B\_{t} approximately gives the investment amount the portfolio manager would have to in add in the target gain PDF matching problem to obtain a business satisfaction value identical to the one related to P→a∗​(B)\vec{P}\_{a}^{\*}(B),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→t∗​(B+Δ​Bt))≈Fa​(P→a∗​(B)),F\_{a}\big(\vec{P}\_{t}^{\*}(B+\Delta B\_{t})\big)\approx F\_{a}\big(\vec{P}\_{a}^{\*}(B)\big), |  | (38) |

which is valid in the case where Δ​Bt\Delta B\_{t} is sufficiently small so that the linearity hypothesis holds.

This idea of assigning a marginal cost value to the modification of an optimal portfolio is all the more interesting as it can be generalized to various optimization problem parameters or features.
As an example, we can also assign a marginal cost to a modification a′a^{\prime} of any selected risk aversion parameter aa.
We have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→a′∗​(B))<Fa​(P→a∗​(B)),\displaystyle F\_{a}(\vec{P}\_{a^{\prime}}^{\*}(B))<F\_{a}(\vec{P}\_{a}^{\*}(B)), |  | (39) |

and search for the marginal cost Δ​Ba′\Delta B\_{a^{\prime}} such as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→a′∗​(B+Δ​Ba′))=Fa​(P→a∗​(B)),\displaystyle F\_{a}\big(\vec{P}\_{a^{\prime}}^{\*}(B+\Delta B\_{a^{\prime}})\big)=F\_{a}\big(\vec{P}\_{a}^{\*}(B)\big), |  | (40) |

equivalent for a sufficiently small Δ​Ba′\Delta B\_{a^{\prime}} to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fa​(P→a′∗​(B))≈Fa​(P→a∗​(B−Δ​Ba′)).\displaystyle F\_{a}\big(\vec{P}\_{a^{\prime}}^{\*}(B)\big)\approx F\_{a}\big(\vec{P}\_{a}^{\*}(B-\Delta B\_{a^{\prime}})\big). |  | (41) |

Computing Δ​Ba′\Delta B\_{a^{\prime}} provides a marginal cost to the modification of an optimal portfolio related to a risk-aversion value change a′=a+Δ​a′a^{\prime}=a+\Delta a^{\prime}. In other words, it provides a marginal cost to a risk level modification [bauer2016marginal] and
answers the following operational question:
If we had taken a little more risk, could we have saved a significant amount of investment?
Interestingly, the marginal cost quantifying the risk aversion parameter variation Δ​a′\Delta a^{\prime} is given in the same budget unit than in the case of the target gain PDF matching.
The method proposed here thus represents a way to quantitatively and homogeneously compare heterogeneous variations of parameters and features of the PO problem, in budget variation terms interpretable by the portfolio manager.

In practical terms, computing Δ​Ba′\Delta B\_{a^{\prime}} can be done using the method involving parallel computing mentioned above. However, a more efficient numerical scheme can be derived considering that Δ​Ba′\Delta B\_{a^{\prime}} is small.
A constant business satisfaction or objective function value w.r.t. a differential variation of the pair (B,a)(B,a) is expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=d​Fa​(P→a∗​(B))=∂Fa​(P→a∗​(B))∂B​d​B+∂Fa​(P→a∗​(B))∂a​d​a0=dF\_{a}(\vec{P}\_{a}^{\*}(B))=\frac{\partial F\_{a}(\vec{P}\_{a}^{\*}(B))}{\partial B}\,dB+\frac{\partial F\_{a}(\vec{P}\_{a}^{\*}(B))}{\partial a}\,da |  | (42) |

Around the point (B,a)(B,a), variations d​BdB of BB and d​ada of aa that maintain constant the value of the objective function are coupled: d​B=−∂Fa​(P→a∗​(B))∂a/∂Fa​(P→a∗​(B))∂BdB=-\frac{\partial F\_{a}(\vec{P}\_{a}^{\*}(B))}{\partial a}/\frac{\partial F\_{a}(\vec{P}\_{a}^{\*}(B))}{\partial B}, which leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ba′=−∂Fa​(P→a∗​(B))∂a∂Fa​(P→a∗​(B))∂B​Δ​a′.\Delta B\_{a^{\prime}}=-\frac{\frac{\partial F\_{a}(\vec{P}\_{a}^{\*}(B))}{\partial a}}{\frac{\partial F\_{a}(\vec{P}\_{a}^{\*}(B))}{\partial B}}\,\Delta a^{\prime}. |  | (43) |

The ratio in the previous equation is in practice computed using a finite difference method and represents a solution to eq. ([40](https://arxiv.org/html/2512.11649v1#S4.E40 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")). Again, eq. ([43](https://arxiv.org/html/2512.11649v1#S4.E43 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) can be used only for sufficiently small Δ​a′\Delta a^{\prime} and Δ​Ba′\Delta B\_{a^{\prime}}. For larger variations, one has to consider directly eq. ([40](https://arxiv.org/html/2512.11649v1#S4.E40 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) and parallel computation.

![Refer to caption](Objective_valley.png)


Figure 1: Objective function value landscape Fa​(P→a∗​(B))F\_{a}(\vec{P}\_{a}^{\*}(B)) for different values of aa and BB.

We now go a step further and would like to compute all pairs (B−Δ​Ba′,a+Δ​a′)(B-\Delta B\_{a^{\prime}},a+\Delta a^{\prime}) that satisfy eq. ([40](https://arxiv.org/html/2512.11649v1#S4.E40 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), i.e. leading to a similar initial objective function or business satisfaction value than the pair (B,a)(B,a), requiring several independent optimizations and thus strongly benefiting from parallel computing.
We obtain an objective function value landscape
from which iso-objective function lines related to any original (B,a)(B,a) value choices can be ‘drawn’, and thus from which all (B−Δ​Ba′,a+Δ​a′)(B-\Delta B\_{a^{\prime}},a+\Delta a^{\prime}) values satisfying eq. ([40](https://arxiv.org/html/2512.11649v1#S4.E40 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) can be recovered.
An illustrative example is given in Fig. [1](https://arxiv.org/html/2512.11649v1#S4.F1 "Figure 1 ‣ 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications").

This method naturally extends to any kind of portfolio optimality deviations,
e.g. to evaluate the marginal cost of modifying the CC parameters in the inequality constraints, eq. ([2](https://arxiv.org/html/2512.11649v1#S2.E2 "In 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
Again, the obtained cost will be in the same budget units than for the other optimality deviations described above, allowing to homogeneously compare heterogeneous variations of parameters and features of the PO problem, and making the result easily interpretable by the portfolio manager.

## 5 Numerical Illustration

### 5.1 Energy Assets PO

Having established the theoretical framework and proposed a method for PO leveraging the gain PDF together with marginal cost evaluation, we now illustrate how these approaches perform in practice. The following section presents numerical examples in the context of energy asset portfolios.

Portfolio optimization in energy markets is a particularly relevant application area, given the sector’s intrinsic volatility, regulatory complexity, and technological heterogeneity. This problem is frequently explored in two main contexts: short-term trading, which focuses on navigating high-frequency price fluctuations in electricity, petroleum, and gas markets [faia2017ad, narajewski2022optimal, gatfaoui2019diversifying], and long-term asset investment, which emphasizes diversified portfolios that integrate conventional and renewable sources while accounting for regulatory incentives and demand uncertainty [jano2017investment, reus2018retail, tietjen2016investment]. It is on the latter case that our illustrations focus.

Across these contexts, researchers have applied portfolio optimization techniques to a variety of energy markets, including petroleum products [lim2020analysis], hydro resources [lemos2012hydro], natural gas [rebennack2010energy], coal [selccuklu2023electricity], and hybrid renewable portfolios such as solar, wind, PV, and biomass [maier2016risk, stempien2017addressing, tolis2011impact]. Risk is typically modeled using metrics such as VaR [berleant2005electric, narajewski2022optimal], CVaR [ma2021optimal, bazmohammadi2018portfolio], and the mean-variance approach [tang2017selection, reus2018retail]. These approaches rely on multi-objective optimization of expectations of few functions of the gain distribution [meucci2005risk], which may not be enough to characterize the information contained in the gain PDF.
In the following numerical illustrations, we demonstrate how our unified approach exploiting directly the gain PDF addresses these limitations.

### 5.2 Constraining High Gains and Evaluating Marginal Cost

We consider synthetic data associated to energy producing assets AnA\_{n}, e.g. electricity generation plants distributed across multiple technologies (onshore and offshore wind farms, solar plants, gas plants…) as well as various countries. Among these assets, some are classified as ‘Secure’, characterized by a scenario distributions with small variance around the mean, while others are designated as ‘Merchant’ assets, characterized by greater uncertainty and broader scenario distributions.

The gain function is defined in terms of ROI and risk is measured using the CVaR-deviation. The statistical data for the assets is synthetic and comprises 100 scenarios, generated by modeling long-term scenarios of assets features (typically a few years). The equality constraint in eq. ([32](https://arxiv.org/html/2512.11649v1#S4.E32 "In 4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) is originally considered, where the budget BB is expressed in GigaWatts, and yny\_{n} denotes the cost of buying one GigaWatts unit of asset AnA\_{n}.
After a change of variables, the decision variable becomes P→\vec{P} and the equality constraint is reformulated as shown in eq. ([1](https://arxiv.org/html/2512.11649v1#S2.E1 "In 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")).
The constraints in eq. ([2](https://arxiv.org/html/2512.11649v1#S2.E2 "In 2.1 General Framework ‣ 2 PO Framework and Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) are limited to inequalities per asset, i.e. to a diagonal M¯​Y¯\underline{M}\,\ \underline{Y} matrix, and contain budget information:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (M¯​Y¯)n,n​pn≤cn.\displaystyle(\underline{M}\,\ \underline{Y})\_{n,n}\,\ p\_{n}\leq c\_{n}. |  | (44) |

After classical PO, we obtain portfolio shares P→a∗\vec{P}\_{a}^{\*} tagged ‘original portfolio’ in the following, see Fig. [3](https://arxiv.org/html/2512.11649v1#S5.F3 "Figure 3 ‣ 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"), and the corresponding estimated gain PDF σ^(P→,.)\hat{\sigma}(\vec{P},.) tagged ‘original PDF’ in the following, see Fig. [3](https://arxiv.org/html/2512.11649v1#S5.F3 "Figure 3 ‣ 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") (a standard gaussian kernel is used for K(.)K(.) in eq. ([24](https://arxiv.org/html/2512.11649v1#S3.E24 "In 2nd item ‣ 3.3 Full Specification of the New Optimization Problem ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"))).

![Refer to caption](x1.png)


Figure 2: Original portfolio (after classical PO).

![Refer to caption](x2.png)


Figure 3: Original gain PDF (after classical PO).

Firstly, we show that the method proposed in sections [3.3](https://arxiv.org/html/2512.11649v1#S3.SS3 "3.3 Full Specification of the New Optimization Problem ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") and [4](https://arxiv.org/html/2512.11649v1#S4 "4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")
is robust and makes it possible to match very well a target PDF.
To that aim, we relax the inequality constraints in eq. ([44](https://arxiv.org/html/2512.11649v1#S5.E44 "In 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")) or in other terms consider cn→∞c\_{n}\rightarrow\infty, and initialize with the original gain PDF the projected gradient iterations that will compute a perturbed PDF.
The target PDF is constructed from the original gain PDF by enhancing the high gains and appears in green in Fig. [4](https://arxiv.org/html/2512.11649v1#S5.F4 "Figure 4 ‣ 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"). The goal is not to match the entire PDF, but only the part located to the right of the red line (in dark green) in order to favor high gains.
This is formalized through the use of an L2 norm for D(σ^(P→,.);σt(.))D(\hat{\sigma}(\vec{P},.);\sigma\_{t}(.)) as in eq. ([25](https://arxiv.org/html/2512.11649v1#S3.E25 "In 3rd item ‣ 3.3 Full Specification of the New Optimization Problem ‣ 3 New Approach Leveraging the Gain PDF ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications")), where the weight θ(.)\theta(.) is a steep sigmoid centered on red dashed line in Fig. [4](https://arxiv.org/html/2512.11649v1#S5.F4 "Figure 4 ‣ 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") so that mostly only the dark green part of the target PDF is encouraged to be matched (we use the sigmoid and not a step function merely to have a differentiable function).
Note that the used target PDF represents a large ‘perturbation’, unrealistic in operational situations but here the goal is to make the test challenging.
The PDF result after projected gradient descent appears in orange in Fig. [4](https://arxiv.org/html/2512.11649v1#S5.F4 "Figure 4 ‣ 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications"), and it near-perfectly matches the dark green part of the target PDF.
This illustrates the robustness of the algorithm but is not fully coherent with the original PO problem as the the per asset inequality constraints were removed.

![Refer to caption](x3.png)


Figure 4: Gain PDF before and after our new optimization, and target PDF. The red dashed line represents the center of a sharp sigmoid. Case where the inequality constraints have been removed.

Figure [5](https://arxiv.org/html/2512.11649v1#S5.F5 "Figure 5 ‣ 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") shows similar results but this time including the inequality constraints. In this case the optimized PDF (in orange) does not exactly match the target PDF (the dark green part), but approaches it as closely as the constraints allow, demonstrating that the method remains robust even when the target PDF is not precisely defined. This is a key for an application in operation contexts. The corresponding portfolio shares are shown in orange in Fig. [6](https://arxiv.org/html/2512.11649v1#S5.F6 "Figure 6 ‣ 5.2 Constraining High Gains and Evaluating Marginal Cost ‣ 5 Numerical Illustration ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") and the initial portfolio shares are shown in black.
It can be observed that
our method fostering high gains suggests increased investment in Merchant assets (with greater variability), thereby enabling the achievement of higher ROI, while investment in Secure assets (with lower variability and thus lower ROI) is reduced, which is fully coherent.

![Refer to caption](x4.png)


Figure 5: Gain PDF before and after our new optimization, and target PDF. The red dashed line represents the center of a sharp sigmoid. Case with the inequality constraints.

![Refer to caption](x5.png)


Figure 6: Portfolio shares resulting from conventional portfolio optimization (black) and from the new optimization approach (orange).

Finally, we apply the marginal cost method described in section [4.3](https://arxiv.org/html/2512.11649v1#S4.SS3 "4.3 Evaluation of Marginal Cost ‣ 4 A Proposed Application: Constraining High Gains ‣ Unified Approach to Portfolio Optimization using the ‘Gain Probability Density Function’ and Applications") to quantify a budget variation that can be associated to the sub-optimality of the portfolio obtained with our new approach. In this study, the marginal cost variation Δ​Bt\Delta B\_{t} was computed by explicitly evaluating the objective function for a range of budget values and identifying the budget increment that yields a similar objective function between the original portfolio and the one obtained with the new method, rather than using a derivative-based approach, since the considered portfolio ‘perturbation’ is not small. We obtain Δ​Bt=−45\Delta B\_{t}=-45 GigaWatts, meaning that we need to increase the budget of the original PO problem by 45 GigaWatts (and not decrease it). This outcome is not the most common but can occur. Indeed, here more inequality constraints become saturated as we increase the budget BB in GigaWatts, forcing the allocation of resources to riskier assets and a decrease of the value of the objective function. The ROI gain function behavior also contributes to this result but the explanation goes beyond the scope of this article (in contrast with a linear gain function case where less restrictive constraints typically result in an increase in the objective function as the budget grows).

## 6 Conclusion

We have presented a unified framework for PO based on the gain PDF. This approach allows for a more comprehensive characterization of portfolio performance by leveraging the full statistical information available on the gain distribution, rather than relying only on expectation-based objective function terms. The method enables portfolio managers to directly target specific features of the gain distribution, providing maximal flexibility in expressing their preferences and requirements.

We explicated the statistical foundations of the proposed framework, generalized conventional risk measures to accommodate non-linear gain functions, introduced a novel procedure that matches a user-defined target gain PDF and detailed the estimation techniques.

We developed a method to constrain high-gains leveraging the information present in the gain PDF.
The method proceeds in two stages. First, a conventional PO is performed select a portfolio according to a balance between expected risk and profit. Starting from this portfolio, our new methodology is then applied to further optimize the portfolio by matching a target gain PDF, specifically to foster higher gains. This two-step process allows portfolio managers to benefit from established risk–profit trade-offs while also perturbing the portfolio according to their specific objectives regarding the gain distribution.
A projected gradient algorithm has been proposed for the optimization, to respect operational constraints, as well as a methodology to quantify a marginal cost associated to the perturbed portfolio in a common budget unit, providing a meaningful information to portfolio managers.
The practical relevance of the approach was illustrated through numerical experiments considering an energy-producing assets portfolio.
But the versatility of the proposed approach extends beyond this specific use case (trading, financial assets…).

Depending on the portfolio manager’s objectives, other regions of the gain PDF can be targeted and optimized, such as loss-side details (for loss control), central region (for stability), or
multi-modal features.
Similarly, the marginal cost method extends to any kind of portfolio optimality deviations,
e.g. to evaluate the marginal cost of modifying inequality constraint parameters, allowing to homogeneously compare heterogeneous variations of parameters and features of the PO problem.
This flexibility makes the methodology suitable for a wide range of applications and contexts. Future work will among others explore automated target PDF construction and develop numerical experiences on various PO applications and datasets.

## Acknowledgment

We would like to thank Matthieu Blondel, Thomas Balsan, Emeric de Monteville, David Jambois and Mikael Soliveres for their feedback and insightful comments on the methodology described in this article.
We thank TotalEnergies for the permission to publish this work.