---
authors:
- Michele Bonollo
- Martino Grasselli
- Gianmarco Mori
- Havva Nilsu Oz
doc_id: arxiv:2511.21556v1
family_id: arxiv:2511.21556
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Informative Risk Measures in the Banking Industry: A Proposal based on the
  Magnitude-Propensity Approach'
url_abs: http://arxiv.org/abs/2511.21556v1
url_html: https://arxiv.org/html/2511.21556v1
venue: arXiv q-fin
version: 1
year: 2025
---


Michele Bonollo
Iason SRL, michele.bonollo@iasonltd.com and Politecnico di Milano, Italy.
  
Martino Grasselli
Department of Mathematics ”Tullio Levi Civita”, University of Padova, Italy, and De Vinci Research Center, Paris La Défense, France. martino.grasselli@unipd.it.
  
Gianmarco Mori
Iason SRL, gianmarco.mori@iasonltd.com.
  
Havva Nilsu Oz
Iason SRL, havva.nilsu@iasonltd.com. Acknowledgments: The authors thank Marco Veith for numerical support and Dr. Jorge Miguel Vegas (Intesa Bank) for valuable feedback.

###### Abstract

Despite decades of research in risk management, most of the literature has focused on scalar risk measures (like e.g. Value-at-Risk and Expected Shortfall). While such scalar measures provide compact and tractable summaries, they provide a poor informative value as they miss the intrinsic multivariate nature of risk.
To contribute to a paradigmatic enhancement, and building on recent theoretical work by [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)], we propose a novel multivariate representation of risk that better reflects the structure of potential portfolio losses, while maintaining desirable properties of interpretability and analytical coherence. The proposed framework extends the classical frequency–severity approach and provides a more comprehensive characterization of extreme events. Several empirical applications based on real-world data demonstrate the feasibility, robustness and practical relevance of the methodology, suggesting its potential for both regulatory and managerial applications.

JEL classification: C10, C13, G10, G20, G28

Keywords: Value-at-Risk, Expected Shortfall, Quantization, Risk measures.

## 1 Introduction and motivation

The pursuit of effective risk measures in the financial industry is
an intriguing and long-standing endeavor that has garnered significant
attention from both scientific and regulatory perspectives.
An adequate comprehensive risk management process typically consists
of the following key steps: (i) Identify risks, to detect all sources
of risk; (ii) Assess risks, i.e., measure them; (iii) Manage risks,
practically to avoid, transfer, hedge, or set limits and warnings;
(iv) Monitor and review risks, with ongoing activity. While some steps,
such as identification and management, relate to business knowledge
and the enterprise’s organization and processes, the measurement step
(ii) is highly technical, involving several related challenging components,
such as: the choice of a "good" risk measure, the setup of its parameters,
a probabilistic model for random adverse events, the statistical calibration
of model parameters, and finally, the statistical estimation of risk
measures given empirical data. From a conceptual perspective, the
choice of risk measures, i.e., how to represent or summarize the randomness
of business variables (Profits and Losses in financial markets, Credit
Default events, Operational Losses), is a highly intriguing task,
as the adopted risk measures should satisfy certain quantitative and
qualitative properties. Briefly, given a univariate random variable
XX describing the potential profits and losses of a portfolio
(PnL for brevity), one aims to summarize in a single scalar
value, the risk measure, the uncertainty that the bank (or insurance
companies) must manage. It is noteworthy that the risk evaluation
goal is often combined with return evaluation, as most capital allocation
choices are driven by the objective of optimizing the risk-versus-return
trade-off in some sense. Extensive work has been devoted in corporate
finance research to topics such as RORAC (Return on Risk-adjusted
Capital) and RAROC (risk-adjusted return on capital) indicators,
i.e., how to allocate capital, the scarce resource, by seeking the
best allocation on the efficient frontier concerning the enterprise’s
risk appetite. A seminal reference in this field, recently updated,
is [[Brealey et al., 2019](https://arxiv.org/html/2511.21556v1#bib.bibx11)]. Adopting these models requires reliable
input in terms of (expected) return and risk estimation. While return
on an investment primarily poses statistical forecasting challenges,
capturing risk concisely for a portfolio is a more arduous task involving
subtle mathematical and conceptual points. We recall that risk, namely
the profits and losses behavior, is typically described
by a random variable. Furthermore, in many real-world models, the
distribution of this random variable is unknown, as it is the outcome
of a sophisticated model involving several risk factors, non-linear
relationships, non-Gaussian elementary distributions, and so on. This extends the problem from risk quantification to model uncertainty, where the distribution itself is not certain, usually known as model risk, see [[Daníelsson et al., 2016](https://arxiv.org/html/2511.21556v1#bib.bibx14)] for a deep empirical survey. An extensive literature on risk measures exists, stemming
from both academic research and financial practitioners. The subtle
distinction between risk and uncertainty, along with a review of risk
measures, is provided in [[Biglova et al., 2008](https://arxiv.org/html/2511.21556v1#bib.bibx10)].
The banking
and insurance sectors exhibit a high level of regulation; hence, regulators
(i.e., governments, central banks, banking authorities) have devoted
significant effort to defining appropriate risk measures to disclose
banks’ risks to the market and all stakeholders. In particular, for over a decade now, international regulations and authorities have been emphasizing the concept of a Risk Appetite Framework (RAF), which banks are required to establish, and the promotion of Risk Culture.
In this context, the concepts of Risk Capacity (or Tolerance) – the maximum risk that can be borne, especially Risk Appetite – the desired risk level, and Risk Profile – the actual risk over time, are crucial, see see [[European Central Bank, 2021](https://arxiv.org/html/2511.21556v1#bib.bibx21)] (specifically the "Definitions" on page 15), and the Basel Committee’s paper No. 328 for further guidance.
Risk culture pertains to the dissemination and awareness of risk among the bank’s top figures (Board, Top Management), cascading throughout the organization, encompassing risk assumptions, risk types, models, and measures. Section 9 of the [[European Central Bank, 2021](https://arxiv.org/html/2511.21556v1#bib.bibx21)] guidelines provides insights on this aspect.
From a practical standpoint, the RAF is further articulated into a Risk Appetite Statement (RAS), which contains high-level (strategic) indicators, known as Tier 1, for various risk types, followed by managerial indicators (Tier 2), and finally, operational or warning indicators at Tier 3 level.
Of course, different regulations
prescribe different risk measures. The general ambitious goal of a
risk measure is to summarize the risky side of the uncertainty concept,
i.e., how much extreme losses could affect the expected return of
any investment strategy. As the extreme losses must be faced by the
own capital of the bank (or the insurance company), it is quite common to
say that the risks absorbe capital. At a very general level, we define
XθX\_{\theta} as the random variable describing the phenomenon
to be investigated, where (θ)(\theta) represents the parameter (scalars
or arrays) characterizing the variable. Let F​(x;θ)F(x;\theta)
be its cumulative distribution, i.e., F​(x;θ)=P​(Xθ≤x)F(x;\theta)=P(X\_{\theta}\leq x).
More generally, let ℱ{\cal F} be the set of all random variables
on the real space (typically, ℱ=L∞​(ℝ){\cal F}=L^{\infty}(\mathbb{R})).
Following [[Embrechts et al., 2015b](https://arxiv.org/html/2511.21556v1#bib.bibx19)], the ways to measure risk
can be grouped into four categories: the notional-amount approach,
sensitivity measures, risk measures based on scenarios (stress tests), and
risk measures based on the PnLs distribution. Focusing
on the last category, most portfolio
risk measures are statistical quantities describing the conditional
or unconditional loss distribution over some predetermined horizon.
The most popular include volatility σ\sigma, Value-at-Risk
(VaR), and Expected Shortfall (ES). More formally, a risk
measure is an application ρ​(X):ℱ→ℝ+\rho(X):{\cal F}\rightarrow\mathbb{R}\_{+}
mapping the random variable XX into a positive scalar value, representing
its uncertainty. A first point is to recall that risk relates to uncertainty,
but in most situations, banks focus on downside risk, i.e., the adverse
side of risk, where extreme losses in the business might occur with
a given frequency. For this reason, volatility σ\sigma (estimated
standard deviation of portfolio returns), although widely popular
due to its simplicity and ubiquitous use in the asset management field
to rank products by their risk, is not adopted in financial regulation,
as it captures randomness from a symmetric perspective.
To define what a good risk measure is, the notion of coherent
risk measures has become prevalent, as outlined in the seminal paper
by [[Artzner et al., 1997](https://arxiv.org/html/2511.21556v1#bib.bibx5)], see the next section for a detailed
overview. If we change perspective, we could wonder if the traditional
approach, i.e., seeking "the best" risk measure, is the proper approach,
or if an alternative strategy should be adopted. Can a one-dimensional
approach, i.e., a scalar measure summarizing adverse P​n​L​sPnLs results,
truly provide sufficient information about risk? Or should we move
to a multidimensional set of values to represent it? To apply this perspective, which key theoretical or conceptual ideas need to be adapted? Are there alternative approaches to risk management beyond the search for an appropriate scalar risk measure? Describing risk by a
couple (or a few) indicators is quite common in fields other than
financial risk management. In the insurance sector, particularly in
the incident claims area, it is popular to summarize each event category
by two parameters: the frequency (λ\lambda) and the claim amount (SS).
If the two are independent or approximately independent,
one can easily obtain the expected value of the claims to be
managed as C=λ⋅SC=\lambda\cdot S. The loss (LL) in a given time horizon
(TT) is represented in the simplest case by a Compound Poisson process,
namely: L​(T)=∑i:t​(i)≤TS​(i),L(T)=\sum\_{i:t(i)\leq T}S(i), where the sum of random losses
(lognormal, gamma, or other appropriate random variable) is extended
to a random number of events driven by the Poisson random variable.
A similar approach prevails in the operational risk sector in banks,
i.e., the risk of losses arising from incidents, errors, failures,
or fraud. In the Loss Distribution Approach
(LDA), a random number of negative events are recorded over
time, each with its severity. Even in the simplest lognormal approach
for severity, we do not know the exact closed-form distribution of
a sum of lognormal random variables, a fortiori if the number
of events itself is random. To this extent, several analytical approximations
have been suggested, some from the mathematical finance field, see
e.g. [[Turnbull and Wakeman, 1991](https://arxiv.org/html/2511.21556v1#bib.bibx50)], others specifically developed in the
operational risk context, like e.g. [[Peters and Shevchenko, 2015](https://arxiv.org/html/2511.21556v1#bib.bibx40)]. If we
move to enterprise risk management, even in large corporate contexts,
the methodology relies less on quantitative tools, as expert assessment
is the most popular approach. Once the risks in the company have been
identified and listed, for each risk, the process owner or the expert
panel is asked to complete a questionnaire to assign some Key Performance
Indicators (KPIs), such as: (i) The probability that no losses are
observed; (ii) The expected loss in normal situations; (iii) The magnitude
of losses in extreme cases, where "extreme" is qualified by some
percentile level or as the worst case over a very long horizon, etc.
A detailed guide to this approach is outlined in [[Institute of Operational Risk, 2019](https://arxiv.org/html/2511.21556v1#bib.bibx31)].
To summarize the above alternative approach and to avoid any confusion,
we point out that while the definition of a good (scalar) risk measure
focuses on the final output of uncertainty, i.e., the extreme losses
for the institution, the risk representation by a few parameters (probability
of the event, its severity, etc.) concerns the components, i.e., the
inputs to the final risk measure. The general idea underlying our
work is to combine these two aspects, namely the classical scalar
approach generally adopted in practice for defining a risk measure
in the risk management process, along with the multivariate perspective
based on its typical parameters on the input side.

From a theoretical standpoint, we refer to the recent work on the
magnitude-propensity approach in risk management by [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)].
The authors’ groundbreaking work employs two closely related approaches
in their theoretical framework: optimal transport and quantization
techniques. Their methodology can be distilled into three key points.
Firstly, they argue that traditional single-valued risk measures, such as VaR or ES, are inadequate for fully capturing the underlying uncertainty.
Secondly,
they acknowledge the binary nature of losses - they either occur or
they don’t. Lastly, they propose approximating the original risk model
(represented by the random variable XX) with a binary variable,
which offers a more nuanced perspective on risk, balancing simplicity
with a richer representation of uncertainty. This simplified model
is characterized by two parameters: pp, the probability of incurring
no losses, and mm, the magnitude of losses when they do occur (with
probability 1−p1-p). Such distribution approximation problem is mathematically
formulated as mass transportation in Wasserstein metric space. The
optimal transportation to a discrete measure is analogous to the optimal
quantization problem, a well-established concept in Engineering and
Signal Processing literature. Consequently, the proposed approach
for quantifying risk on both magnitude and propensity scales can be
characterized as a specialized, constrained optimal quantization problem.
The formulation of [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)] provides a rigorous mathematical
framework for risk assessment, bridging the gap between theoretical
optimal transport and practical risk quantification. It leverages
the Wasserstein metric’s properties to capture the multidimensional
nature of risk, while the quantization aspect ensures computational
tractability and interpretability of the results. We immediately note that the approach of [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)] differs from that of vector risk measures, first introduced by [[Jouini et al., 2004](https://arxiv.org/html/2511.21556v1#bib.bibx32)] and later revisited and developed by [[Ben Tahat and Lépinette, 2014](https://arxiv.org/html/2511.21556v1#bib.bibx9)], [[Feinstein and Rudloff, 2015](https://arxiv.org/html/2511.21556v1#bib.bibx24)], and [[Ararat and Feinstein, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx4)], in order to account for proportional transaction costs in multi-asset markets.

Numerous attempts have been made to introduce additional properties aimed at improving these measures, identifying desirable characteristics, and clarifying what constitutes a well-defined notion of risk at the vector level. However, extending the same axioms used for scalar coherence often renders vector risk measures difficult to interpret and, in particular, to implement, since an additional selection procedure is typically required to determine a specific capital requirement or allocation rule within the set-valued framework, see [[Ararat and Feinstein, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx4)] for a recent overview of these methods.
The multidimensional approach we adopt here is of a different nature and not directly comparable to theirs.

Regarding our contribution to this field, from a theoretical point of view,
we endeavor to extend the framework of [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)] to the 3-point
(i.e., zero, moderate, and extreme losses). In this multidimensional context, this contribution is significant. While the Risk Appetite Framework encompasses not only market and credit risk (the focus of our examples) but also liquidity, operational, reputational, and other risks, one of the pressing issues for banks, as requested by the European Central Bank during inspections, is "How did you determine the set of limits, i.e., the level of capacity/tolerance or warning levels?".
There is no common practice or guidelines on this matter. Most banks adopt the following approach: they consider the historical Value-at-Risk data, take the highest value, perhaps add a 10−20%10-20\% buffer, and set that as the tolerance level (keeping in mind that, at the bank level, as opposed to sub-portfolios, there may also be regulatory limits). In this regard, our optimal upper threshold m2m\_{2} corresponding to extreme losses could serve as an excellent "automatic machine" (recall that ECB highly appreciates objectivity in the determination of the thresholds) to determine and support the setting of tolerance and/or capacity levels. For risks that involve only losses (operational, financial), the lower threshold m1m\_{1}, corresponding to moderate losses, could also be an equally automatic tool for defining the risk appetite as observed in the past or as a "floor" for such appetite.
In the context of Risk Culture and top management’s awareness of risks, a description using (m1,m2)(m\_{1},m\_{2}) with the associated probabilities (p1,p2)(p\_{1},p\_{2}) could provide an intuitive and complementary alternative to VaR and, more importantly, to the more complex Expected Shortfall, due to its familiarity with concepts such as severity and frequency.
Finally, for "financial conglomerates" under European directives, i.e., groups that include banks, insurance companies, and asset management firms, the regulations mandate the integration (effectively, uniformity and convergence) of measurement methods and risk culture across the various legal entities within the group. Our approach, which combines ideas from finance and insurance logic, could be a viable solution in this context.

Furthermore, our contribution
is also focused on applications, as we discuss certain constraints
that must be incorporated into the optimization problem to render
the solution more realistic in practical contexts. We apply
the technique to the historical simulation approach for VaR
calculation and to the Montecarlo simulation for the Default Risk
Charge (DRC) measure, which are largely the most adopted by major
banks, precisely 19 out of 31 in the 2021 ECB review, see [[European Central Bank, 2021](https://arxiv.org/html/2511.21556v1#bib.bibx21)].
To accomplish our objective, we utilize the PnLs derived
from the real portfolio of a significant European bank. This makes
our work complementary to [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)], which primarily pertains
to the insurance sector, where we implement the third application case. The paper is organized as follows:
Section 2 reviews the relevant literature on risk measures; Section
3, after a brief background on quantization and the magnitude-propensity
approach, elucidates the extensions we implement to make this proposal
more suitable in the field of risk management; Section 4 illustrates
the application and the dataset employed for calibrating the models;
Section 5 contains our results, along with a discussion of the key
points; Section 6 summarizes the conclusions and outlines further
research avenues. We gather in the Appendix the technical proofs and some material on the numerical optimization procedures.

## 2 Scalar Risk Measures: Review and Limitations

Risk quantification and measurement constitute essential elements
in the domains of finance, insurance, and decision-making processes.
Throughout the years, a diverse array of risk measures has been proposed
and analyzed, each exhibiting distinct advantages and limitations.
Coherent risk measures represent a fundamental and well-established
framework for quantifying risk in financial and insurance contexts.
These measures adhere to a set of axioms that ensure a consistent
and rational approach to risk assessment. The coherence properties,
including subadditivity, monotonicity, translation invariance, and
positive homogeneity, provide a robust foundation for comparing and
aggregating risks across diverse portfolios and financial instruments,
see e.g. [[Artzner et al., 1997](https://arxiv.org/html/2511.21556v1#bib.bibx5)]. The field of risk measurement
has witnessed the development and application of numerous theories,
ranging from the widely utilized Value-at-Risk and Expected
Shortfall to *Stress Tests*. Researchers and practitioners have
extensively explored these methodologies to evaluate potential losses
and manage uncertainties in various financial contexts.
VaR, a ubiquitously employed risk metric within the financial sector,
provides a probabilistic estimate of potential losses at a predetermined
confidence level over a specified temporal horizon. This measure enables
financial institutions to quantify and articulate downside risk with
precision, thereby facilitating informed decision-making and risk
management strategies. The diffusion of VaR lies in its ability to
distill complex risk profiles into a single, comprehensible figure,
rendering it a useful tool for risk communication among stakeholders,
regulatory compliance, and internal risk control mechanisms. For a
given holding period and a level α∈(0,1)\alpha\in(0,1) the VaR of the
PnL distribution XX is defined as

|  |  |  |
| --- | --- | --- |
|  | V​a​Rα​(X):=−inf{x∈ℝ:ℙ​(X≤x)>α},VaR\_{\alpha}(X):=-\inf\{x\in\mathbb{R}:\mathbb{P}(X\leq x)>\alpha\}, |  |

or, equivalently, V​a​Rα=inf{x∈ℝ:ℙ​(L​o​s​s≥x)≤α}VaR\_{\alpha}=\inf\{x\in\mathbb{R}:\mathbb{P}(Loss\geq x)\leq\alpha\}.
One of the primary merits of VaR lies in its simplicity and
interpretability, offering a lucid and succinct estimation of potential
financial losses. This characteristic enables risk managers to swiftly
evaluate and juxtapose risks across diverse portfolios or trading
positions. Nevertheless, VaR is not without its limitations,
particularly in its sensitivity to extreme events, where its single-point
estimate may inadequately capture tail risk. The work of [[Embrechts et al., 2015b](https://arxiv.org/html/2511.21556v1#bib.bibx19)]
elucidates how VaR embodies the propensity aspect of risk
by determining the leftmost quantile, yet fails to encapsulate the
magnitude of potential losses. Furthermore, VaR has been
subject to substantial criticism due to its non-subadditivity, a property
that contravenes the axioms of coherent risk measures. This deficiency
renders the aggregation of VaR values across portfolios problematic.
To illustrate this point, one can readily construct an example utilizing
two sub-portfolios, P1P\_{1} and P2P\_{2}, where the following inequality
holds: V​a​Rα​(P=P1∪P2)>V​a​Rα​(P1)+V​a​Rα​(P2)VaR\_{\alpha}(P=P\_{1}\cup P\_{2})>VaR\_{\alpha}(P\_{1})+VaR\_{\alpha}(P\_{2}).
This mathematical representation underscores the inherent limitations
of VaR in accurately reflecting the cumulative risk of combined
portfolios, thereby highlighting the need for more robust risk measurement
methodologies in complex financial environments.

Conversely, the essential supremum, denoted as ρ∞​(X):=e​s​s​supX\rho\_{\infty}(X):=ess\sup X,
represents the antithetical extreme to VaR, quantifying the
maximal magnitude of a potential loss without estimating the associated
probabilities. This risk measure, also known as the worst-case scenario
or tail Value-at-Risk, encapsulates the most extreme potential
loss, irrespective of its probability of occurrence. As such, it provides
a conservative estimate of the worst possible outcome but does not
offer a comprehensive risk assessment that incorporates both magnitude
and propensity aspects. One of the primary advantages of ρ∞​(X)\rho\_{\infty}(X)
lies in its simplicity and interpretability. By focusing solely on
the maximum potential loss, it enables risk managers to identify worst-case
scenarios and allocate capital reserves accordingly. In situations
where extreme events can have severe consequences, ρ∞​(X)\rho\_{\infty}(X)
provides a valuable upper bound for risk exposure, ensuring that institutions
are adequately prepared for the most adverse outcomes. However, this
extreme focus on maximum loss is not without drawbacks. By disregarding
probabilities, ρ∞​(X)\rho\_{\infty}(X) neglects the likelihood of less
extreme but still significant losses. Consequently, risk managers
relying exclusively on this measure might overlook the impact of moderately
severe yet more probable events, potentially leading to suboptimal
risk management strategies. Furthermore, ρ∞​(X)\rho\_{\infty}(X) exhibits
high sensitivity to outliers and extreme observations, rendering it
vulnerable to estimation errors and model mis-specifications. In practice,
financial data often display heavy-tailed distributions, implying
that extreme events occur more frequently than a Normal distribution
would suggest. As a result, ρ∞​(X)\rho\_{\infty}(X) might overstate worst-case
scenarios, leading to excessively conservative risk assessments and
potential over-allocation of capital reserves. The theoretical underpinnings
and practical implications of the essential supremum in risk measurement
have been extensively explored in the seminal works of [[Rockafellar and Uryasev, 2002](https://arxiv.org/html/2511.21556v1#bib.bibx43)]
and [[Pichler and Shapiro, 2021](https://arxiv.org/html/2511.21556v1#bib.bibx41)].

Expected Shortfall (ES), also known as Conditional Value-at-Risk,
emerges as the most promising alternative to address VaR’s
limitations. ES quantifies the expected value of losses beyond the
VaR threshold, providing information on extreme event severity
and tail behavior. It is formally defined as:

|  |  |  |
| --- | --- | --- |
|  | E​Sα=𝔼​[L​o​s​s|L​o​s​s≥V​a​Rα].ES\_{\alpha}=\mathbb{E}[Loss|Loss\geq VaR\_{\alpha}]. |  |

Expected Shortfall exemplifies a coherent risk measure, adhering to
the fundamental axioms of coherent measures (translation invariance,
subadditivity, positive homogeneity, and monotonicity, see [[Artzner et al., 1997](https://arxiv.org/html/2511.21556v1#bib.bibx5)]).
By quantifying potential losses beyond the VaR threshold,
*ES* provides a more comprehensive and robust risk assessment,
particularly for heavy-tailed distributions, see [[Acerbi and Tasche, 2002](https://arxiv.org/html/2511.21556v1#bib.bibx3)].
This attribute renders *ES* preferable in financial risk management,
where tail events can precipitate significant systemic consequences.
Regulatory bodies and financial institutions increasingly adopt *ES*,
acknowledging its capacity to address VaR’s limitations and
more accurately represent extreme risk scenarios. Then *ES* is
going to replace VaR (α=99%,h=10\alpha=99\%,h=10 days) in the impending
Fundamental Review of the Trading Book (FRTB) regulation for market
risk minimum capital requirement calculations, see [[Basel Committee of Banking Supervision, 2019](https://arxiv.org/html/2511.21556v1#bib.bibx8)].
In the forthcoming regulatory framework, Expected Shortfall is employed
to quantify market risk at a α=97.5%\alpha=97.5\% confidence level and
different time horizons hh (hh = 10,20,40, 60, 120 days depending
on the liquidy ot the risk factors categories). However, financial
institutions are still required to validate their models using the
back-testing procedure based on VaR calculated at both α=99%\alpha=99\%
and α=95%\alpha=95\% confidence levels. This unconventional regulatory
setup stems from a decade-long debate surrounding the elicitability
property of risk measures. Elicitability, derived from point forecasting,
requires statistical functionals to maintain consistency with their
evaluation through historical averaging, akin to M−M-functionals
(see [[Gneiting, 2011](https://arxiv.org/html/2511.21556v1#bib.bibx27)]). In this context, VaR is elicitable
but not coherent, while Expected Shortfall is coherent and law-invariant
but not elicitable. Notably, ES exhibits joint elicitability with
VaR ([[Fissler and Ziegel, 2016](https://arxiv.org/html/2511.21556v1#bib.bibx25)]). Furthermore, *ES* possesses
the crucial property of backtestability, enabling rigorous performance
evaluation in historical simulations and real-world scenarios, as
elucidated by [[Acerbi and Székely, 2017](https://arxiv.org/html/2511.21556v1#bib.bibx1)], who underscore ES’s capacity to
provide robust and reliable risk assessments, rendering it an invaluable
tool for risk managers in evaluating potential losses across diverse
financial scenarios111Our magnitude-propensity–based approach can be subjected to backtesting by extending the regulatory framework prescribed for VaR, see [[Kupiec, 1995](https://arxiv.org/html/2511.21556v1#bib.bibx35)], as well as the more sophisticated joint VaR–ES testing procedures proposed by [[Acerbi and Székely, 2017](https://arxiv.org/html/2511.21556v1#bib.bibx1)]. A comprehensive analysis of backtestability and the extension of the notion of elicitability to our multivariate framework requires a dedicated investigation and will therefore be developed in a forthcoming paper.. More recently, the competition among the different
proposals for good risk measures has been enriched by some works about
the concept of *observability* of a risk measure. Quite surprisingly,
the popular volatility indicator and the *ES* show to
be more observable than *VaR*. To this extent, an insightful
analysis is provided in [[Acerbi and Székely, 2023](https://arxiv.org/html/2511.21556v1#bib.bibx2)], by leveraging the concept
of *sharp backtest*.

Finally, it is worth to note that in the FRTB regulation the banks
must also calculate another risk measure, the *Default Risk Charge*
(DRC), namely a 1-Year *VaR* with α=99.9%\alpha=99.9\%. This capital
requirement aims to capture the default risk in the trading book.
Until the 2008-2011 financial crisis, the so called *market risk*building block in the Basel regulation included only the *spread
risk*, i.e. the price uncertainty coming form the spread level, e.g
in the bond evaluation. According to the Basel 2.5 Reform, it was
requested to estimate the potential losses coming from the default
(or migration) events also for the trading book of the bank, see [[European Banking Authority, 2012](https://arxiv.org/html/2511.21556v1#bib.bibx20)].
While the P​n​L​sPnLs of the traditional market risk come from the movements
of the risk factors (equities, interest rates, forex rates, spreads,
commodities) that are commonly assumed to have continuous distribution,
in the credit risk case the portfolio losses are originated by the default binary events DnD\_{n} associated to the obligors (n=1,⋯,Nn=1,\cdots,N):

|  |  |  |
| --- | --- | --- |
|  | L​o​s​sD​R​C=∑nE​A​Dn⋅𝟏Dn⋅L​G​Dn,Loss\_{DRC}=\sum\_{n}EAD\_{n}\cdot\mathbb{\mathbf{1}}\_{D\_{n}}\cdot LGD\_{n}, |  |

where E​A​DnEAD\_{n} and L​G​DnLGD\_{n} represent, respectively, the amount
of exposure and the fraction that the bank is not able to recover
once the default happens, modeled as a deterministic coefficient in
the range [0,1]\left[0,1\right], or by a random variable, usually a *Beta (a,b)*.
It is important to notice that the combinatorial effects associated with default events lead to an intrinsic instability of any risk measure, due to the fact that extreme
values of the distribution are so pronounced that the VaR no longer provides an adequate representation of
tail risk. We will illustrate this effect in the Appendix [B](https://arxiv.org/html/2511.21556v1#A2 "Appendix B Intrinsic Instability of the Quantile in Credit Risk Modeling ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach").

Stress tests represent a pivotal tool for risk analysis,
enabling institutions to assess resilience against adverse market
conditions and extreme events. These tests simulate hypothetical crisis scenarios, such as
economic recessions, market shocks, or event-related crises, by subjecting portfolios or financial systems to
various stress factors.
By modeling extreme conditions, stress tests identify vulnerabilities
and quantify potential losses under adverse circumstances. The results
provide insights into an institution’s risk exposure, capital adequacy,
and overall financial stability. This risk management tool has become
increasingly crucial for regulatory compliance and is widely adopted
by financial institutions to ensure robust risk management practices.
Notably, stress tests have been instrumental in enhancing the financial
sector’s resilience following the 2008 global financial crisis. By
simulating scenario outcomes, stress tests empower institutions to
implement appropriate risk mitigation strategies and maintain financial
stability in turbulent times. From a conceptual standpoint, stress
tests diverge significantly from measures such as Value-at-Risk and
Expected Shortfall. On one hand, stress tests are more objective in
their results and are based on a simple "what-if" logic: given a
scenario, banks can calculate the related PnL with high accuracy.
On the other hand, regulations mandate the use of extreme
yet plausible scenarios, a goal that is arduous to achieve even for
regulatory authorities. Furthermore, stress test results lack information
about the associated probabilities.

In this respect,
the common practice consists of some heuristic methods. To determine thresholds for risk tolerance or risk appetite in the their risk appetite framework, typically some banks consider the past time average of the Value-at-Risk and increase it by some subjective quantity (e.g. 20%20\%), other banks calculate directly the Stressed VaR, i.e. VaR under stressed parameters. Such approach is quite reasonable but exhibits some drawbacks, being too judgmental without a rational basis. Furthermore, these methods do not add any relevant additional information about risk beyond what is provided by the VaR itself. Additional information is required, which only a multidimensional approach can provide, as will be explained in the following section.
VaR does not provide insights into the underlying risk factors or the potential severity and frequency of extreme events. By simply scaling the VaR up or down by a fixed percentage, the resulting stressed scenarios fail to capture the complex dynamics and interdependencies of risk factors, as well as the potential for tail events that may deviate significantly from the assumed distribution.
A multidimensional approach, on the other hand, can incorporate additional risk dimensions, such as severity and frequency, as well as the potential for non-linear interactions between risk factors.
In the following section, we will explore a multidimensional approach that incorporates severity and frequency dimensions to provide a more comprehensive and informative framework for risk management and scenario analysis.

## 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions

[[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)] observe that VaR and
ES are traditionally calculated for popular confidence levels α\alpha
(e.g., 95%,99%,97.5%95\%,99\%,97.5\%), introducing a degree of subjectivity
to these risk measures and highlighting potential weaknesses in comparing
distinct PnLs distributions. The magnitude-propensity approach
aims to address these limitations. Given the random variable for the
PnL, say XX, the approach consists in defining a discrete
binary random variable YY that works as an informative summary of
the whole XX, whose distribution is given by

|  |  |  |
| --- | --- | --- |
|  | PY=(1−p)⋅δ0+p⋅δm,P^{Y}=(1-p)\cdot\delta\_{0}+p\cdot\delta\_{m}, |  |

where pp is the probability that the loss is zero, mm represents
the magnitude of the loss and δx\delta\_{x} denotes the Dirac distribution concentrated at the point xx.
Various methodologies have
been developed to discretize continuous risk distributions, providing
decision-makers with robust tools for risk assessment and strategic
planning.
Two main approaches
emerge in the literature - the optimal transport approach and the
optimal quantization approach.
The optimal transport method
approximates continuous distributions by minimizing mass transportation
costs between distributions, as explained by [[Villani, 2009](https://arxiv.org/html/2511.21556v1#bib.bibx51)].
On the other hand, optimal quantization, described by [[Graf and Luschgy, 2000](https://arxiv.org/html/2511.21556v1#bib.bibx28)], [[Pagès et al., 2004](https://arxiv.org/html/2511.21556v1#bib.bibx39)]
and [[Luschgy and Pagès, 2023](https://arxiv.org/html/2511.21556v1#bib.bibx37)], represents risk data using finite point grids222We also mention other methods like K−K-means clustering, studied by [[Liu and Pagès, 2020](https://arxiv.org/html/2511.21556v1#bib.bibx36)], which groups similar
risk data points, then revealing underlying risk patterns, and the quantile-based
methods, explored by [[Chernozhukov and Hong, 2004](https://arxiv.org/html/2511.21556v1#bib.bibx12)], that partition risk distributions
based on predefined quantiles, focusing on specific risk thresholds..

While both the optimal transport
and quantization approaches aim to disentangle the magnitude and propensity
aspects of risk, they employ distinct mathematical frameworks to achieve
this goal. The optimal transport approach represents the search for
the binary random variable YY as a mass transportation problem,
whereas the quantization approach treats it as an optimal discrete
representation problem. However, optimal transportation to discrete measures
also corresponds to a special case of optimal quantization, in fact
the proposed approach to quantify risk on both the magnitude and propensity
scales amounts to a special, constrained, optimal quantization problem.
Specifically, we briefly review the formulation of the bivariate magnitude-propensity
risk measure and its optimization using Wasserstein distance
for the optimal transport approach. Furthermore, we explore the intricacies
of the optimal quantization problem and its relevance in approximating
risk distributions with discrete measures. We then attempt to establish
a solid theoretical foundation for our research, which aims at extending
the original 2-points distribution framework of [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)]
by developing a novel 3-points distribution approach. Our extended
methodology incorporates an additional quantile, enabling a more informative
and comprehensive risk quantification process.

### 3.1 Optimal Transport Approach

The optimal transport (OT) problem, formally introduced by [[Kantorovich, 1942](https://arxiv.org/html/2511.21556v1#bib.bibx33)],
addresses the transformation of a probability distribution PXP^{X}
of the random variable XX to a distribution PYP^{Y} of the variable
YY, while minimizing the associated transition cost function c​(x,y):X×Y→[0,+∞]c(x,y):X\times Y\rightarrow[0,+\infty].
The Monge-Kantorovich optimal transportation problem has a clear physical
interpretation: considering the random variables as material locations,
then c​(x,y)c(x,y) represents the cost of transporting a unit of material
from xx to yy. Optimal cost functions typically represent the
transport cost as the product of mass and inter-location distance.
The problem is constrained by complete material relocation. This framework
has diverse applications, spanning economics, image processing, and
machine learning, providing a robust methodology for distribution
transformation analysis and optimization. The formulation maintains
scientific rigor while offering concise elegance, emphasizing the
concept’s broad academic and practical relevance. This version further
condenses the information while preserving the scientific tone and
elegant expression. It highlights the key points about cost function
formulation, problem constraints, and the wide-ranging applicability
of the optimal transport framework. Mathematically, the Monge-Kantorovich
optimal transport problem is formulated as:

|  |  |  |
| --- | --- | --- |
|  | infπ∈Π​(PX,PY)∫ℝ×ℝc​(x,y)​π​(d​x,d​y)\inf\_{\pi\in\Pi(P^{X},P^{Y})}\int\_{\mathbb{R}\times\mathbb{R}}c(x,y)\,\pi(dx,dy) |  |

where Π​(PX,PY)\Pi(P^{X},P^{Y}) is the set of all transport plans, i.e.,
joint probability measures on ℝ×ℝ\mathbb{R}\times\mathbb{R} with marginals
PXP^{X} and PYP^{Y}, respectively. Under regularity conditions,
the optimal transportation plan is defined as a Monge map TT, namely
π​(x,y)=π​(x,T​(x))\pi(x,y)=\pi(x,T(x)), see e.g. [[Rachev and Rüschendorf, 1998](https://arxiv.org/html/2511.21556v1#bib.bibx42)], [[Villani, 2009](https://arxiv.org/html/2511.21556v1#bib.bibx51)].
In the degenerate case where PY=δmP^{Y}=\delta\_{m}, with m∈ℝm\in\mathbb{R},
Π​(PX,PY)\Pi(P^{X},P^{Y}) reduces to the singleton product measure {PX​(d​x)×δm​(d​y)}\{P^{X}(dx)\times\delta\_{m}(dy)\}
and the OT problem becomes

|  |  |  |
| --- | --- | --- |
|  | infm∈ℝ∫c​(x,m)​PX​(d​x)=infm∈ℝ𝔼​[c​(X,m)].\inf\_{m\in\mathbb{R}}\int c(x,m)P^{X}(dx)=\inf\_{m\in\mathbb{R}}\mathbb{E}[c(X,m)]. |  |

For c​(x,y)=(x−y)2c(x,y)=(x-y)^{2} one gets the squared L2L^{2}-Wasserstein
metric W2W\_{2} and the OT problem reads

|  |  |  |
| --- | --- | --- |
|  | W22​(PX,δm)=infm∈ℝ𝔼​[(X−m)2]=V​a​r​(X),W\_{2}^{2}(P^{X},\delta\_{m})=\inf\_{m\in\mathbb{R}}\mathbb{E}[(X-m)^{2}]=Var(X), |  |

which is minimized for the mean m=𝔼​[X]m=\mathbb{E}[X]. For the L1L^{1}
distance c​(x,y)=|x−y|c(x,y)=|x-y| one gets the median, while for the
asymmetric cost c​(x,y)=(x−y)​α​1x−y≥0+(y−x)​(1−α)​1y−x>0c(x,y)=(x-y)\alpha 1\_{x-y\geq 0}+(y-x)(1-\alpha)1\_{y-x>0}
with 0<α<10<\alpha<1 one gets the (left)-α\alpha quantile m=qα​(X)m=q\_{\alpha}(X),
i.e. the Value-at-Risk (see [[Koenker, 2005](https://arxiv.org/html/2511.21556v1#bib.bibx34)]. Finally, for c​(x,y)=y+(x−y)​1x≥y1−αc(x,y)=y+\frac{(x-y)1\_{x\geq y}}{1-\alpha}
one gets the Conditional Value-at-Risk, namely the ES, see [[Rockafellar and Uryasev, 2002](https://arxiv.org/html/2511.21556v1#bib.bibx43)].

In the magnitude-propensity approach investigated by [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)],
the optimal transport approach scrutinizes traditional risk measure
limitations by reframing them as mass transportation from the original
risk distribution PXP^{X} to a binary distribution PYP^{Y}, encapsulating
both risk magnitude and propensity. The corresponding risk measure
(m,p)(m,p) is derived by minimizing the Wasserstein W2−W\_{2}-distance
between PXP^{X} and PYP^{Y} within a constrained distribution set
𝒫0:={PY=p​δm+(1−p)​δ0,p∈(0,1),m∈ℝ+}{\cal P}\_{0}:=\{P^{Y}=p\delta\_{m}+(1-p)\delta\_{0},p\in(0,1),m\in\mathbb{R}\_{+}\}.
This methodology provides a novel perspective on risk quantification,
integrating the multidimensional nature of risk into a cohesive framework,
where a loss of magnitude mm occurs with probability pp,
and no loss (i.e. the loss amount equals zero) occurs with probability
(1−p)(1-p). It then offers a more nuanced approach to risk assessment,
potentially enhancing decision-making processes in financial and economic
contexts. If we denote with QXQ\_{X} (resp. QYQ\_{Y}) the quantile
function associated with the distribution PXP^{X} (resp. PYP^{Y}),
then the L2−L^{2}-Wasserstein W2−W\_{2}-distance between PXP^{X} and
PYP^{Y} reads (see e.g. [[Rachev and Rüschendorf, 1998](https://arxiv.org/html/2511.21556v1#bib.bibx42)]):

|  |  |  |
| --- | --- | --- |
|  | W2​(PX,PY)=(∫01(QX​(x)−QY​(x))2​𝑑x)1/2W\_{2}(P^{X},P^{Y})=\left(\int\_{0}^{1}\left(Q\_{X}(x)-Q\_{Y}(x)\right)^{2}\,dx\right)^{1/2} |  |

where QX​(z):=inf{x:FX​(x)≥z},0<z<1Q\_{X}(z):=\inf\{x:F\_{X}(x)\geq z\},0<z<1 and FXF\_{X} represents
the cumulative distribution function of the distribution PXP^{X},
where XX is assumed to have finite variance. For the two-point distribution
PYP^{Y}, the quantile function reads QY​(z)=m​𝟏1−p<z≤1Q\_{Y}(z)=m{\bf 1}\_{1-p<z\leq 1},
and the optimal quantities (m,p)(m,p) can be found explicitly
by direct optimization, see [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)]. We omit the details
of their results as our work employs the quantization method, which
proves to be significantly more efficient in our context. In Appendix [C](https://arxiv.org/html/2511.21556v1#A3 "Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach") we provide some additional details on the algorithmic implementation of the Optimal Transport procedure that we adopted in our analysis.

### 3.2 The Quantization Approach

Quantization, rooted in engineering and signal processing, offers
an alternative paradigm for achieving analogous objectives. This approach
involves the optimal discretization of continuous risk distributions,
akin to analog-to-digital conversion and data compression methodologies.
The primary aim is to identify a finite set of points (codebook) that
minimizes the mean squared error or distortion between the original
risk distribution PXP^{X} and its quantized counterpart PYP^{Y}.
This process effectively transforms complex, continuous risk landscapes
into more manageable, discrete representations.

Following [[Graf and Luschgy, 2000](https://arxiv.org/html/2511.21556v1#bib.bibx28)] and [[Luschgy and Pagès, 2023](https://arxiv.org/html/2511.21556v1#bib.bibx37)], an NN-vector quantizer on (ℝd,||.||)(\mathbb{R}^{d},||.||)
is a mapping T:ℝd→{x1,…,xN}T:\mathbb{R}^{d}\rightarrow\{x\_{1},...,x\_{N}\} where
{x1,…,xN}\{x\_{1},...,x\_{N}\} is a codebook of size NN, i.e. there is a
partition (called Voronoi tessellation) {Ai}1≤i≤N\{A\_{i}\}\_{1\leq i\leq N} with Ai={x∈ℝd:T​(x)=xi}A\_{i}=\{x\in\mathbb{R}^{d}:T(x)=x\_{i}\},
so that

|  |  |  |
| --- | --- | --- |
|  | T​(x)=∑i=0Nxi​𝟏Ai​(x).T(x)=\sum\_{i=0}^{N}x\_{i}\mathbb{\mathbf{1}}\_{A\_{i}}(x). |  |

For a given N∈ℕN\in\mathbb{N}, an NN-tuple of elementary quantizers
(x1,…,xN)(x\_{1},\ldots,x\_{N}) is optimal if it minimizes over (ℝd)N(\mathbb{R}^{d})^{N}
the quantization error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖X−X^‖r=min(y1,…,yN)∈(ℝd)N⁡𝔼​[min1≤i≤N⁡‖X−yi‖r]1/r\|X-\hat{X}\|\_{r}=\min\_{(y\_{1},\ldots,y\_{N})\in(\mathbb{R}^{d})^{N}}\mathbb{E}\left[\min\_{1\leq i\leq N}\|X-y\_{i}\|^{r}\right]^{1/r} |  | (1) |

induced by replacing XX by X^\widehat{X}. Then, instead of transmitting
the complete signal X​(ω)X(\omega) itself, one first selects the closest
xix\_{i} in the quantizer set and transmits its (binary or Gray coded)
label ii. After reception, a proxy X^​(ω)\widehat{X}(\omega) of X​(ω)X(\omega)
is reconstructed using the code book correspondence i→xii\rightarrow x\_{i}.
Typically rr is fixed to be equal to 2, leading to a quadratic quantization
error. In this case, an NN-optimal quantizer for a distribution
PXP^{X} is a NN-quantizer that minimizes the mean squared error
(also called the  distortion function):

|  |  |  |
| --- | --- | --- |
|  | infT𝔼​[(X−T​(X))2].\inf\_{T}\mathbb{E}[(X-T(X))^{2}]. |  |

In dd dimensions, the minimal quantization error converges to zero
at a rate of N−1dN^{-\frac{1}{d}} as N→∞N\to\infty, according to the
so-called Zador theorem. Several stochastic optimization procedures
based on simulation have been developed to compute these optimal quantizers.
For a comprehensive exposition of mathematical aspects of quantization, we refer to [[Graf and Luschgy, 2000](https://arxiv.org/html/2511.21556v1#bib.bibx28)] and [[Luschgy and Pagès, 2023](https://arxiv.org/html/2511.21556v1#bib.bibx37)].
Remarkably, it can be shown (e.g. [[Graf and Luschgy, 2000](https://arxiv.org/html/2511.21556v1#bib.bibx28)]) that an optimal
quantizer is a Monge map minimizing the Wasserstein metric W2​(PX,PY)W\_{2}(P^{X},P^{Y})
between PXP^{X} and PYP^{Y}, where PYP^{Y} is a discrete measure
with NN points. In the case where PYP^{Y} has two values, with
respect to the simplest quantization approach, we impose additional
constraints on the codebook points, with one point mass at zero and
another at a positive magnitude mm, to indicate the presence of
loss. The quantization problem is then defined as the constrained
two-points quantizer with centers {x1,x2}:={0,m}\{x\_{1},x\_{2}\}:=\{0,m\}, i.e.
as a mapping T:ℝ+→{0,m}T:\mathbb{R}^{+}\to\{0,m\} with

|  |  |  |
| --- | --- | --- |
|  | T​(x)={mx≥a0x<a,T(x)=\begin{cases}m&x\geq a\\ 0&x<a,\end{cases} |  |

where aa is a threshold to determine. Then, the optimal quantization
problem for X∼PXX\sim P^{X} with constrained knot at zero writes

|  |  |  |
| --- | --- | --- |
|  | infa,m∈ℝ+𝔼​[(X−T​(X))2],\inf\_{a,m\in\mathbb{R}^{+}}\mathbb{E}[(X-T(X))^{2}], |  |

and, as the boundary of the Voronoi cells separating the two quantizers
x1,x2x\_{1},x\_{2} is given by the center of the interval [0,m][0,m], it
turns out that the Voronoi partition is given by the two regions A1={x∈ℝ+:0≤x≤m/2}A\_{1}=\{x\in\mathbb{R}\_{+}:0\leq x\leq m/2\}
and A2={x∈ℝ+:x2≥m/2}A\_{2}=\{x\in\mathbb{R}\_{+}:x\_{2}\geq m/2\}. Thus, in the case
where r=2,N=2,x1=0,x2=mr=2,N=2,x\_{1}=0,x\_{2}=m, ([1](https://arxiv.org/html/2511.21556v1#S3.E1 "In 3.2 The Quantization Approach ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖X−X^‖2=minm∈ℝ+⁡𝔼​[min⁡{X2,(X−m)2}]1/2\|X-\hat{X}\|\_{2}=\min\_{m\in\mathbb{R}\_{+}}\mathbb{E}\left[\min\{X^{2},(X-m)^{2}\}\right]^{1/2} |  | (2) |

For the two-point distribution for PYP^{Y}, [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)] proved
the following result.

###### Theorem 3.1.

(i) If 𝔼​(X2)<∞\mathbb{E}(X^{2})<\infty and the support of PXP^{X} contains
at least two points, then there exists a magnitude-propensity pair
(pX,mX)(p\_{X},m\_{X}) minimizing the distortion.

(ii) An optimal pair (pX,mX)(p\_{X},m\_{X}) is characterized by solving for
aa the equation

|  |  |  |
| --- | --- | --- |
|  | 2​a=𝔼​[X​|X>​a],a>02a=\mathbb{E}[X|X>a],a>0 |  |

and then setting mX=2​a,pX=PX​(X>a)m\_{X}=2a,p\_{X}=P^{X}(X>a).

Note that mXm\_{X} can be interpreted either as (twice) a V​a​RαVaR\_{\alpha}
(resp. as an E​SαES\_{\alpha}) for a special value of the confidence
level α\alpha:

|  |  |  |
| --- | --- | --- |
|  | mX=C​V​a​RpX​(X)=2​V​a​R1−pX​(X).m\_{X}=CVaR\_{p\_{X}}(X)=2VaR\_{1-p\_{X}}(X). |  |

What is more, the confidence level α\alpha is no longer a subjective
choice dependent on the user. This is an improvement from a technical
perspective, possibly a drawback in the application playground, as
the prudential level is usually regulation-driven, i.e. assigned by
the authorities: typically, α=99%\alpha=99\% in the market risk field,
α=99.9%\alpha=99.9\% in the credit risk, finally α=99.5%\alpha=99.5\% in the
*Solvency* insurance regulation.

### 3.3 Extension to the case of 3-Points Optimal Constrained Quantization

In this subsection we are going to prove the main theoretical contribution
of the paper, namely the extension of the results of [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)]
to the case of three points. The 3-Points distribution introduces
a sophisticated and comprehensive approach to risk quantification,
transcending the limitations of conventional methods. This distribution
represents risk through three distinct points. The first point is
the no loss case, m0=0m\_{0}=0. The second point aims to designate moderate
risk (m1,p1)(m\_{1},p\_{1}), where m1m\_{1} represents the magnitude of
potential moderate losses (corresponding to the most likely scenarios),
and p1p\_{1} represents the probability of occurrence for these losses.
The third point must capture extreme losses (m2,p2)(m\_{2},p\_{2}), with
m2m\_{2} denoting their magnitude and p2p\_{2} indicating the probability
of occurrence for these severe events. As an example, the so-called
3-point risk analysis consists of summarizing the risk with 3 relevant
values, namely: the best case, the worst case, and the most likely
case. The three values are usually stimated (assessed) by submitting a standardized
questionnaire to a panel of experts. For an extended review of these
qualitative risk assessment techniques, see e.g., [[Aven, 2016](https://arxiv.org/html/2511.21556v1#bib.bibx6)].
The quantitative approach of our work differs from this kind of methodology
for its more rigorous and objective framework. The 3-Points distribution
with a specific constraint introduces an additional criterion that
influences the optimal selection of the discrete distribution parameters.
This modification aims to avoid that the pure mathematical optimal
solution does not highlight high magnitude losses. Furthermore, the
stability of a risk measure over time is a general requirement of
any risk measure in the banking regulation.

Following [[Graf and Luschgy, 2000](https://arxiv.org/html/2511.21556v1#bib.bibx28)], a 33-vector quantizer on ℝ,||.||)\mathbb{R},||.||)
is a mapping T:ℝ→{x0,x1,x2}T:\mathbb{R}\rightarrow\{x\_{0},x\_{1},x\_{2}\}, where
we relabeled the codebook ({x1,x2,x3}→{x0,x1,x2}\{x\_{1},x\_{2},x\_{3}\}\rightarrow\{x\_{0},x\_{1},x\_{2}\})
for notational convenience. More specifically, one can refine a measure
of risk into a classification between a “moderate” and a “large”
loss, by using a three points discrete measure, PY=(1−p1−p2)​δ0+p1​δm1+p2​δm2P^{Y}=(1-p\_{1}-p\_{2})\delta\_{0}+p\_{1}\delta\_{m\_{1}}+p\_{2}\delta\_{m\_{2}},
with 0<m1<m20<m\_{1}<m\_{2} and where x0=m0=0x\_{0}=m\_{0}=0. Utilizing a three-point
discrete measure enables the encoding and quantification of both moderate
and large losses on the magnitude and propensity scales. This is achieved
through the pairs (m1;p1)(m\_{1};p\_{1}) and (m2;p2)(m\_{2};p\_{2}), respectively.
One thus introduces the constrained three-point quantizers with centers
{0,x1,x2}:={0,m1,m2}\{0,x\_{1},x\_{2}\}:=\{0,m\_{1},m\_{2}\}, i.e. as a mapping T:[0,∞)→{0,m1,m2}T:[0,\infty)\rightarrow\{0,m\_{1},m\_{2}\}
with T​(x)=0​𝟏x≤a1+m1​𝟏a1<x≤a2+m2​𝟏x>a2T(x)=0{\bf 1}\_{x\leq a\_{1}}+m\_{1}{\bf 1}\_{a\_{1}<x\leq a\_{2}}+m\_{2}{\bf 1}\_{x>a\_{2}},
where 0≤a1<a20\leq a\_{1}<a\_{2} are thresholds to be determined. Then, the
optimal quantization problem with constrained knot at zero for a random
variable XX with 𝔼​[X2]<∞\mathbb{E}[X^{2}]<\infty (and whose support
contains at least three points) writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf(a1,m1,a2,m2)∈[0,+∞)4𝔼​[(X−T​(X))2].\displaystyle\inf\_{(a\_{1},m\_{1},a\_{2},m\_{2})\in[0,+\infty)^{4}}\mathbb{E}[(X-T(X))^{2}]. |  | (3) |

Using standard arguments, see e.g. [[Graf and Luschgy, 2000](https://arxiv.org/html/2511.21556v1#bib.bibx28)] and [[Luschgy and Pagès, 2023](https://arxiv.org/html/2511.21556v1#bib.bibx37)], one already knows that a1=m1/2a\_{1}=m\_{1}/2 and a2=(m1+m2)/2a\_{2}=(m\_{1}+m\_{2})/2,
i.e. that the Voronoi regions write

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A0\displaystyle A\_{0} | ={x:0≤x≤m1/2},\displaystyle=\{x:0\leq x\leq m\_{1}/2\}, |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A1\displaystyle A\_{1} | ={x:m1/2≤x≤(m1+m2)/2},\displaystyle=\{x:m\_{1}/2\leq x\leq(m\_{1}+m\_{2})/2\}, |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A2\displaystyle A\_{2} | ={x:x≥(m1+m2)/2}.\displaystyle=\{x:x\geq(m\_{1}+m\_{2})/2\}. |  | (6) |

As a consequence, the distortion/objective function writes as a sole
function of the magnitudes m1,m2m\_{1},m\_{2} as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | D​(m1,m2)\displaystyle D(m\_{1},m\_{2}) | =𝔼​[X2∧(X−m1)2∧(X−m2)2]=𝔼​[X2∧(X−m2)2]​𝟏m2≥m1,\displaystyle=\mathbb{E}[X^{2}\wedge(X-m\_{1})^{2}\wedge(X-m\_{2})^{2}]=\mathbb{E}[X^{2}\wedge(X-m\_{2})^{2}]{\bf 1}\_{m\_{2}\geq m\_{1}}, |  | (7) |

since m2>m1m\_{2}>m\_{1}. Introduce now for x=(x1,x2)∈ℝ+2x=(x\_{1},x\_{2})\in\mathbb{R}\_{+}^{2}

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(x1,x2)\displaystyle H(x\_{1},x\_{2}) | =h0​(x1,x2)∧h1​(x1,x2)∧h2​(x1,x2):=X2∧(X−x1)2∧(X−x2)2.\displaystyle=h\_{0}(x\_{1},x\_{2})\wedge h\_{1}(x\_{1},x\_{2})\wedge h\_{2}(x\_{1},x\_{2}):=X^{2}\wedge(X-x\_{1})^{2}\wedge(X-x\_{2})^{2}. |  |

Note that h0,h1,h2h\_{0},h\_{1},h\_{2} are differentiable functions, so that
the function HH is (at least) piecewise differentiable, and it has
directional derivatives everywhere, as shown in Figure [1](https://arxiv.org/html/2511.21556v1#S3.F1 "Figure 1 ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")
where we display the function HH for X=2X=2.

![Refer to caption](x1.jpg)


Figure 1: Graphic of the function H​(m1,m2)=22∧(m1−2)2∧(m2−2)2H(m\_{1},m\_{2})=2^{2}\wedge(m\_{1}-2)^{2}\wedge(m\_{2}-2)^{2}.

As shown in [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)], a convenient tool in the setting of
optimization of piecewise smooth functions is the concept of Bouligand
derivative (B-derivative), see e.g. [[Scholtes, 2012](https://arxiv.org/html/2511.21556v1#bib.bibx44)]. By dropping the
requirement of linearity of the differential, it represents a first-order
approximation and allows to have a single-valued notion of differential.

###### Definition 3.1.

A function f:ℝ2→ℝf:\mathbb{R}^{2}\rightarrow\mathbb{R} is B-differentiable
at x~∈ℝ2\tilde{x}\in\mathbb{R}^{2} if there exists a positive homogeneous
function ∇Bf​(x~):ℝ2→ℝ\nabla^{B}f(\tilde{x}):\mathbb{R}^{2}\rightarrow\mathbb{R}
s.t.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(x~+v)\displaystyle f(\tilde{x}+v) | =f​(x~)+∇Bf​(x~)​(v)+o​(‖v‖),∀v∈ℝ2.\displaystyle=f(\tilde{x})+\nabla^{B}f(\tilde{x})(v)+o(||v||),\ \ \forall v\in\mathbb{R}^{2}. |  | (8) |

We have the following lemma on the B-differentiability of the function
HH.

###### Lemma 3.2.

Let H​(x)=min⁡(h0​(x);h1​(x);h2​(x))H(x)=\min(h\_{0}(x);h\_{1}(x);h\_{2}(x)), where h0,h1,h2:ℝ2→ℝh\_{0},h\_{1},h\_{2}:\mathbb{R}^{2}\rightarrow\mathbb{R}
are differentiable functions. Then HH is B-differentiable, and its B-differential is given as follows.

1. 1.

   For i,j,ki,j,k distinct indexes in {0,1,2}\{0,1,2\}, for xx such that hi​(x)<min⁡(hj​(x);hk​(x))h\_{i}(x)<\min(h\_{j}(x);h\_{k}(x))

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x)​(v)\displaystyle\nabla^{B}H(x)(v) | =∇hi​(x)​v=∂hi∂x1​(x)​v1+∂hi∂x2​(x)​v2.\displaystyle=\nabla h\_{i}(x)v=\frac{\partial h\_{i}}{\partial x\_{1}}(x)v\_{1}+\frac{\partial h\_{i}}{\partial x\_{2}}(x)v\_{2}. |  |
2. 2.

   For xx such that hi​(x)=hj​(x)<hk​(x)h\_{i}(x)=h\_{j}(x)<h\_{k}(x)

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x)​(v)\displaystyle\nabla^{B}H(x)(v) | =min⁡(∇hi​(x)​v;∇hj​(x)​v).\displaystyle=\min(\nabla h\_{i}(x)v;\nabla h\_{j}(x)v). |  |
3. 3.

   For xx such that h0​(x)=h1​(x)=h2​(x)h\_{0}(x)=h\_{1}(x)=h\_{2}(x)

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x)​(v)\displaystyle\nabla^{B}H(x)(v) | =min⁡(∇h0​(x)​v;∇h1​(x)​v;∇h2​(x)​v).\displaystyle=\min(\nabla h\_{0}(x)v;\nabla h\_{1}(x)v;\nabla h\_{2}(x)v). |  |

###### Proof.

See Appendix [A](https://arxiv.org/html/2511.21556v1#A1 "Appendix A Proofs ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach").

Before proving the B-differentiability of the distortion function
DD, we recall that a point xx is critical (that is, a potential minimizing point) for DD if ∇BD​(x)​(v)≥0​∀v∈ℝ2\nabla^{B}D(x)(v)\geq 0\ \forall v\in\mathbb{R}^{2}.

###### Theorem 3.3.

The distortion function DD defined in ([7](https://arxiv.org/html/2511.21556v1#S3.E7 "In 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))
for a random variable X∈L2X\in L^{2} is B-differentiable on x∈ℝ+2x\in\mathbb{R}\_{+}^{2},
with B-derivative given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇BD​(x1,x2)​(v)\displaystyle\nabla^{B}D(x\_{1},x\_{2})(v) | =𝔼​[2​(x2−X)​v2​𝟏x1+x2<2​X]\displaystyle=\mathbb{E}[2(x\_{2}-X)v\_{2}{\bf 1}\_{x\_{1}+x\_{2}<2X}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2𝔼[min((x1−X)v1𝟏x1<2​X𝟏x1+x2>2​X]\displaystyle+2\mathbb{E}[\min((x\_{1}-X)v\_{1}{\bf 1}\_{x\_{1}<2X}{\bf 1}\_{x\_{1}+x\_{2}>2X}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2​𝔼​[min⁡(0;2​X​v1)​𝟏x1=2​X].\displaystyle+2\mathbb{E}[\min(0;2Xv\_{1}){\bf 1}\_{x\_{1}=2X}]. |  | (9) |

Moreover, the points (0,0),(0,2​X),(2​X,0),(2​X,2​X),(0,x2)(0,0),(0,2X),(2X,0),(2X,2X),(0,x\_{2}) (with
x2>2​Xx\_{2}>2X) and (x1,0)(x\_{1},0) (with x1>2​Xx\_{1}>2X) are not critical
for the distortion function, since ∇BD​(x)​(v)<0\nabla^{B}D(x)(v)<0 for some
v∈ℝ2v\in\mathbb{R}^{2}.

###### Proof.

See Appendix [A](https://arxiv.org/html/2511.21556v1#A1 "Appendix A Proofs ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach").

We have now all the ingredient to characterize the critical points,
namely we can find the quantizers of the 3-points distribution by
solving a system of equations. From Equation ([9](https://arxiv.org/html/2511.21556v1#S3.E9 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")), by taking
separatly v1=0,v2=0v\_{1}=0,v\_{2}=0 we get

|  |  |  |
| --- | --- | --- |
|  | P​(X=x1+x22)=P​(X=x12)=0,\displaystyle P\left(X=\frac{x\_{1}+x\_{2}}{2}\right)=P\left(X=\frac{x\_{1}}{2}\right)=0, |  |

and we find the following system

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(x1−X)​𝟏x12<X<x1+x22]\displaystyle\mathbb{E}[(x\_{1}-X){\bf 1}\_{\frac{x\_{1}}{2}<X<\frac{x\_{1}+x\_{2}}{2}}] | =0,\displaystyle=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(x2−X)​𝟏X>x1+x22]\displaystyle\mathbb{E}[(x\_{2}-X){\bf 1}\_{X>\frac{x\_{1}+x\_{2}}{2}}] | =0,\displaystyle=0, |  |

which leads to the optimal quantizers:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | m1\displaystyle m\_{1} | =𝔼​[X|m12<X<m1+m22],\displaystyle=\mathbb{E}\left[X|\frac{m\_{1}}{2}<X<\frac{m\_{1}+m\_{2}}{2}\right], |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | m2\displaystyle m\_{2} | =𝔼​[X​|X>​m1+m22].\displaystyle=\mathbb{E}\left[X|X>\frac{m\_{1}+m\_{2}}{2}\right]. |  | (11) |

Eventually, once the system is solved using a fixed-point technique,
the probabilities p1,p2p\_{1},p\_{2} associated with the quantizers are
given by integrating the probability of XX on the Voronoi regions
given by ([5](https://arxiv.org/html/2511.21556v1#S3.E5 "In 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))–([6](https://arxiv.org/html/2511.21556v1#S3.E6 "In 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")). Finally, the probability mass
of the initial (constrained) quantizer m0=0m\_{0}=0 is given by (1−p1−p2)(1-p\_{1}-p\_{2}).

###### Remark 3.1.

The points m1m\_{1} and m2m\_{2}
optimally represent the underlying loss distribution, independently of any a​p​r​i​o​r​ia\ priori thresholds such as those described by V​a​RVaR or E​SES associated with some confidence level. Consequently, there is no guaranty that m2m\_{2}, intended to represent an extreme loss, can be directly compared to V​a​RVaR or E​SES, nor that the associated probability
p2p\_{2} has any direct relationship to the confidence level α\alpha. Therefore, it is not surprising that, as we show in our numerical experiments, the value of m2m\_{2} can differ from V​a​RVaR. In other words, comparing m2m\_{2} with V​a​RVaR is not a meaningful exercise, as we only have one m2m\_{2} while we can compute many V​a​RVaR according to the relevant confidence levels adopted by the financial regulation used in practice (0.95, 0.99, 0.995, 0.999, etc.).
Nevertheless, it is advisable to introduce a constraint to prevent the purely mathematical optimum from neglecting high-magnitude losses and to ensure the temporal stability of the risk measure, which is a requirement in banking regulation. In the context of market risk, where m2m\_{2}
typically turns out to be slightly lower than V​a​RVaR, it seems reasonable to impose an additional restriction on m2m\_{2}, ensuring that it reaches a value at least equal to V​a​RVaR. This preserves its interpretation as an indicator of extreme risk while maintaining compliance with regulatory standards, which are expressed in terms of V​a​RVaR.
From an analytical standpoint, the introduction of such a constraint increases the complexity of the optimization procedure. However, from a numerical perspective, the procedure remains highly efficient (see the appendix for further details on the optimization procedures), and the resulting performance is fully satisfactory.

## 4 Case Study based on Real Datasets

### 4.1 Practical Risk Management

In this section we try to exploit the features of the magnitude-propensity approach in relevant different fields.
To achieve significant insights, some concepts about practical risk management are needed.
First, the risk category must be well defined.
In a high level classification, we distinguish market risk vs. credit risk. Market risk is given by the PnLs (profits and losses) uncertainty due to the price dynamics of the assets in the portfolio. Financial portfolios of large banks typically are not concentrated; even if we may observe extreme events due to volatility peaks, the PnLs typical distribution is quite smooth.
Credit risk is related to the losses implied by any default in the portfolio, where once the default occurs, the recovery rate drives the amount that one can get back. In this case, we have also concentrated portfolio, and the binary nature of the outcome (no default, default) implies a loss distribution that sometimes shows some peaks in the extreme losses region.
Due to high quality, high frequency data and finally a long history of the risk management in the financial area, the regulation typically asks for more conservative confidence level in the credit risk (e.g. 0,999), as we have low frequency data, low data coverage (e.g. many issuers in the portfolio might be unrated, with missing default probability), and the default correlations are not strict sense observable.
The above issues are summarized in the model risk definition, i.e. the risk arising from misspecifications in the model itself or in its parameters.
The boundary between market and credit risk is quite flexible. A relevant example is given by the migration risk, i.e. the risk of losses due to downgrade (rating worsening) of one or more issuers in the portfolio.
Furthermore, the well known spread risk, i.e. the risk of losses due to the increase of the spread level (e.g. in the government bonds in portfolios) is clearly assigned to the market risk discipline in the banking context, see [[Basel Committee of Banking Supervision, 2019](https://arxiv.org/html/2511.21556v1#bib.bibx8)], while it can be allocated to market or credit risk filed according to the Solvency regulation for the insurance companies, see [[European Commission, 2015](https://arxiv.org/html/2511.21556v1#bib.bibx22)].
See [[Embrechts et al., 2015a](https://arxiv.org/html/2511.21556v1#bib.bibx18)] for a comprehensive survey of the main modeling methodologies related to market and credit risk.
Taking into account the above practical and regulatory concepts, we decided to exploit the capabilities of the magnitude-propensity 3-points proposal in three different application contexts, trying to cover a relevant area of the broad market and credit risk fields, as summarized in Table [1](https://arxiv.org/html/2511.21556v1#S4.T1 "Table 1 ‣ 4.1 Practical Risk Management ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach").

| ID Case | Description | Risk Category | Regulation | PnLs Model | Confidence level | Horizon |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Market Risk Trading book | Market Risk | Basel | Historical non parametric | 99% | 1D |
| 2 | Credit Risk Trading Book | Credit Risk | Basel | Monte Carlo parametric | 99.9% | 1Y |
| 3 | Market Risk Insurance | Market Risk | Solvency | Monte Carlo parametric | 99.5% | 1Y |

Table 1: Overview of VaR calculation according to regulatory risk cases: model type, regulation, model calculation, confidence level and horizon.

### 4.2 Applications Overview and Preliminary Concepts

Financial Institutions commonly adopt two main approaches to measure
the risk of a financial position, which they select based on their
specific purposes and regulatory requirements: sensitivity measures
and risk measures based on the profit and loss (PnLs) distribution. Both these approaches are prescribed by the regulations and adopted by the risk management departments.

To have a better understanding, let us denote the value of a generic
portfolio at the evaluation time t0t\_{0} as Vt0V\_{t\_{0}}. Following standard
risk-management practice, Vt0V\_{t\_{0}} is modeled as a function of time
tt (the index t0t\_{0} represents the current time, so that e.g. t0−1t\_{0}-1 indicates the previous time and so on) and a d−d-dimensional random vector 𝐙t=(Zt1,Zt2,⋯,Ztd){\bf Z}\_{t}=(Z\_{t}^{1},Z\_{t}^{2},\cdots,Z\_{t}^{d})
of risk factors, i.e., underlying variables or drivers like e.g. interest
rates, stock prices, implied volatility, or exchange rates. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt0=f​(t0,𝐙),V\_{t\_{0}}=f(t\_{0},{\bf Z}), |  | (12) |

with f:ℝ×ℝd→ℝf:\mathbb{R}\times\mathbb{R}^{d}\rightarrow\mathbb{R} and where 𝐙{\bf Z} informally represents the heterogeneous set of risk factors (scalar, array, surface, cubes etc.) recorded at past observation times, depending on specific payoffs of the instruments of the portfolio.

For the sake of simplicity, we omitted in the expression the various parameters on which depend the stochastic processes that describe the risk factors Zt\textbf{Z}\_{t} dynamics.
Sensitivity based risk measures rely on each risk factor impact, which
can be defined as the change in value of an instrument (position) given a small, predetermined (hypothetical) movement in a risk factor that affects
the instrument’s value: from a mathematical perspective, sensitivities
are computed as partial derivatives of the function ff with respect
to ZZ. By defining Δ​𝐙=𝐙t−𝐙t−1\Delta{\bf Z}={\bf Z}\_{t}-{\bf Z}\_{t-1} the vector of observed shocks applied to the risk factors, this approach enables the estimation, assuming linearity between VV
and 𝐙{\bf Z}, of the portfolio response to the new market conditions by multiplying Δ​𝐙\Delta{\bf Z}
with the corresponding factor sensitivities, namely Δ​V≅∇f⋅𝚫​𝐙\Delta V\cong\nabla f\cdot{\bf\Delta Z}.
Technically speaking, it is just a differential of the value function
ff evaluated for some small increment Δ​𝐙\Delta{\bf Z}. Of course, the second order impact could be added to improve the accuracy of the approximation. The most popular second order approximations are referred according to some naming conventions, such as the gamma effect, i.e. the second order derivative of an option the the underlying price, and the convexity, namely the second order impact of the interest rate level change on a bond or interest derivative (e.g swaps, caps and floor options).
Such risk measures, though valuable in providing information about
the robustness of a portfolio value to specific events, have limitations
when making capital-adequacy decisions: they do not deal with the
dependency properties of the risk drivers, hence they can not create
a picture of the overall riskiness of the portfolio of a financial
institution, and they do not have any information about the likelihood
of the approximated *PnLs*, see [[McNeil et al., 2005](https://arxiv.org/html/2511.21556v1#bib.bibx38)]. Furthermore, sensitivity approach is a typical what-if approach, where there is some subjectivity in defining the level of the extreme market shock to be applied.
For this reason, the so called probabilistic measures, such as V​a​RVaR and E​SES, are prominent in the financial regulation, to ensure that banks and the insurance companies have enough own capital to face the potential losses under "extreme yet plausible" scenarios, a statement adopted very often by the financial authorities to define the scope of the stress test exercise. The following subsections give more details on the context of the three applications of the methodology.

#### 4.2.1 Market Risk with Historical Simulation

In the introduction, we recalled that the historical simulation is
the most popular approach in the large banks to evaluate the financial
risk, by *VaR*, *ES* or any other measure. Let us give a
brief formal explanation, mainly of the historical simulation
through the *full evaluation* methodology. We can define the daily portfolio
PnLs as the change in value of the portfolio, driven by the
series of risk factor changes 𝐘t{\bf Y}\_{t} where 𝐘t:=𝐙t−𝐙t−1=Δ​𝐙{\bf Y}\_{t}:={\bf Z}\_{t}-{\bf Z}\_{t-1}=\Delta{\bf Z}
or alternatively 𝐘t:=ln⁡(𝐙t/𝐙t−1){\bf Y}\_{t}:=\ln\left({\bf Z}\_{t}/{\bf Z}\_{t-1}\right).
The additive (or absolute) vs multiplicative (or percent) definition of
a shock is calculated depending on the asset class of the risk factor: usually,
banks adopt the additive convention for interest rates and spreads, while
the multiplicative convention for returns on equities, foreign exchange rates and funds. For a useful survey, see e.g. [[Hudson and Gregoriou, 2010](https://arxiv.org/html/2511.21556v1#bib.bibx30)].
For each t=t0−1,⋯,t0−St=t\_{0}-1,\cdots,t\_{0}-S in our array of historical scenarios, the
portfolio value is calculated by summing up the contributions over all proper pricing functions fmf\_{m} (related to the instrument m=1,⋯,Mm=1,\cdots,M) that select just the required risk factors, typically a small subset of the whole market
data 𝐙{\bf Z}.

If we adopt the full evaluation approach, the
portfolio’s PnL at a given calculation time (t0t\_{0}) and for any observed scenario
[t,t0][t,t\_{0}] with t=t0−1,⋯,t0−St=t\_{0}-1,\cdots,t\_{0}-S, is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​n​L[t,t0]=∑mfm​(t0,𝐙+𝐘t)−fm​(t0,𝐙).PnL\_{[t,t\_{0}]}=\sum\_{m}f\_{m}(t\_{0},{\bf Z}+{\bf Y}\_{t})-f\_{m}(t\_{0},{\bf Z}). |  | (13) |

The value (or *PnLs*) of the portfolio is then the sum of a huge
variety of pricing functions with heterogenous risk factor inputs.

###### Remark 4.1.

The above stylized expression uses the additive convention for the shock. In the multiplicative case the part fm​(t0,𝐙+𝐘t)f\_{m}(t\_{0},{\bf Z}+{\bf Y}\_{t})
is replaced by fm​(t0,𝐙⋅exp⁡(𝐘t))f\_{m}(t\_{0},{\bf Z}\cdot\exp({\bf Y}\_{t})).

###### Remark 4.2.

In the above expression we refer to absolute (eur, dollar, etc.) PnLs, i.e. the standard convention for bank portfolios. In the asset management field it is common to switch to relative (percent) PnLs, by a scaling factor, i.e. the current value Vt0V\_{t\_{0}} of the portfolio.

###### Remark 4.3.

If P​n​LPnL is calculated using the sensitivities approach, the function fm(.)f\_{m}(.) is replaced by the gradient vector, and we have P​n​L≅∇fm⋅𝚫​𝐙PnL\cong\nabla f\_{m}\cdot{\bf\Delta Z}, possibly enriched with the second order term based on the Hessian matrix.

###### Remark 4.4.

One could replace the term fm​(t0,𝐙+𝐘t)f\_{m}(t\_{0},{\bf Z}+{\bf Y}\_{t}) by the more general expression fm​(t0+1,𝐙+𝐘t)f\_{m}(t\_{0}+1,{\bf Z}+{\bf Y}\_{t})
to properly take into account the “ageing effect”, meaning that if the
market shocks are supposed to prevail in a given time horizon hh ( h=1h=1 for simplicity in this case), then the hypothetical *PnLs*
must take into account such time shift in order to shorten the time to maturity of the instruments, such as bonds or derivatives. Despite this seems an obvious
concept, very often the ageing is not actually considered, as it would
require that all the pricing libraries of the bank are able to price
in the future, i.e. not only taking into account the time decay (such
as the decreasing maturity for a bond) but also all the other possible events,
such as dividend payments and so on. In most cases, a risk factor shock is applied, but not the time shift, so applying the *instantaneous shock* assumption. For the insurance sector, see the survey in [[EIOPA, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx16)], where it is outlined that only 6
out of 20 insurance companies manage the ageing effect, while the
remaining ones apply the instantaneous shock model.

In other words, PnLs distribution consists in the range of
possible values XX (potential profits and losses) that a portfolio
may experience over a specific time horizon.
The historical simulation approach is data driven, as no parametric distribution family is assumed for the returns. Furthermore, we do not need any correlation parameters or dependence modeling as it is assumed that the dependencies among the risk factors are divided into small pieces inside each scenario (t)(t).
Recalling that in measuring
portfolio’s risk the fundamental aspect is estimating the cumulative
density function of the PnLs, namely F​(x)=ℙ​(X≤x)F(x)=\mathbb{P}(X\leq x),
or functionals of it, see [[McNeil et al., 2005](https://arxiv.org/html/2511.21556v1#bib.bibx38)] and that Value at Risk is essentially a
quantile (typically 95%,99%,99.9%95\%,99\%,99.9\%) of the above mentioned PnLs
distribution, the final step consists in estimating a suited percentile to be applied to the vector
of PnLs. For the number SS of scenarios, banks usually adopt S=250S=250 or S=500S=500, i.e. they
collect about 1 or 2 years of daily changes in all the risk factors to which the portfolio is sensitive. The regulatory time horizon hh differs
from the daily popular horizon, e.g. h=10h=10 days in the current Basel
regulation. Collecting a sample of historical non-overlapping risk
factors returns (𝐘t,h=𝐙t+h−𝐙t)\left({\bf Y}\_{t,h}={\bf Z}\_{t+h}-{\bf{\bf Z}}\_{t}\right)
could be quite difficult. As an example, to achieve S=250S=250 non overlapping scenarios with h=10h=10 days, we need h⋅S=2500h\cdot\ S=2500 observations, i.e. around 10 years of full time series for all the risk factors.
Hence, the authorities generally accept the
*square root* rule, namely V​a​R​(α,h)≡V​a​R​(α,1)⋅hVaR\left(\alpha,h\right)\equiv VaR\left(\alpha,1\right)\cdot\sqrt{h}.

In daily practice, VaR can be estimated in many ways: from the
basic empirical percentile to some more robust estimators, such as
L−L-estimators and Harrel-Davis estimator, that smooth the estimation
by averaging the PnLs in a neighborhood of the empirical
quantile, see[[Harrel, 1982](https://arxiv.org/html/2511.21556v1#bib.bibx29)]. In this field a comprehensive reference is given by [[David and Nagaraja, 2004](https://arxiv.org/html/2511.21556v1#bib.bibx15)]. These more advanced estimators of course may be used also in the other simulation contexts, such the Monte Carlo simulation.
The historical simulation approach is very popular in the banking industry
due to some key reasons. First, it is very intuitive, as the
empirical past (recent) distribution of the risk factors returns is
accepted (assumed) to be the best estimation of the unknown exact distribution.
No functional subjective assumption is made about the distribution
shape. Being purely data-driven, it does not rely on any parameters
(volatility, correlations, etc). In real world, portfolios may
contain many thousands of risk factors: estimating the related parameters
and updating periodically the estimates is a very challenging
task. For the sake of simplicity, in the following applications we
will refer to the basic empirical quantile (e.g. the 5​t​h5th worst
result in an array of S=500S=500 P​n​LPnL).

#### 4.2.2 Credit Risk in the Trading Book: the Default Risk Charge by Montecarlo approach

The Default Risk Charge (*DRC*) is a regulatory measure designed
to capture default risk within the trading portfolio, as required
by Basel standards, particularly within the framework of the Fundamental
Review of the Trading Book (FRTB) outlined in the [[Basel Committee of Banking Supervision, 2019](https://arxiv.org/html/2511.21556v1#bib.bibx8)]
document. This model is designed to quantify the risk of loss resulting
from the failure of a counterparty or issuer of financial instruments,
including equity, bond, and derivative exposures. The Default *DRC*
is specified in Chapter 7, and in the updated Basel Framework, in Paragraphs MAR 33.18- 33.38. These documents establish the criteria
for calculating default risk, specifying that

* •

  It must be calculated over a one-year horizon.
* •

  It must reflect a 99.9% confidence level.
* •

  It must include all exposures sensitive to default risk within the
  trading portfolio, excluding those specifically defined as non-material
  risks.

In the practice, the default of each issuer is modeled by a Merton
type model. The credit worthiness dynamics of the obligor n​(n=1,…,N)n\ (n=1,...,N)
is defined by the model

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Xn=∑k=1Kβk,n⋅Wk+σ⋅εn\Delta X\_{n}=\sum\_{k=1}^{K}\beta\_{k,n}\cdot W\_{k}+\sigma\cdot\varepsilon\_{{}\_{n}} |  | (14) |

where the coefficients βk,n\beta\_{k,n} are the *factor loadings*
and describe the systematic risk, driven by a set of risk factors
k=1,…,Kk=1,...,K, the term εn\varepsilon\_{n} is the specific (obligor) factor,
with WkW\_{k} correlated standardized Normal random variables, with E​[Wk​εn]=0​∀n,kE\left[W\_{k}\varepsilon\_{n}\right]=0\ \forall n,k.

In this standardized framework, the default happens if the credit
worthless is below a given threshold, Dn={Xn≤Φn−1​(P​Dn)}D\_{n}=\left\{X\_{n}\leq\Phi\_{n}^{-1}\left(PD\_{n}\right)\right\},
where Φn\Phi\_{n} and P​DnPD\_{n} indicate the cumulative distribution
of Δ​Xn\Delta X\_{n} and the default probability of the n−t​hn-th issuer
in the portfolio. The factor loading coefficients are estimated by
a statistical regression step, by combining the time series of
the list of risk factors with the issuer equity prices or spreads.
In large banks, we generally have hundreds of issuers (NN) and some
dozens of risk factors (KK). The distribution of the portfolio loss is given by [2](https://arxiv.org/html/2511.21556v1#S2.Ex3 "2 Scalar Risk Measures: Review and Limitations ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"), that we recall here:

|  |  |  |
| --- | --- | --- |
|  | L​o​s​sD​R​C=∑n=1NE​A​Dn⋅𝟏Dn⋅L​G​Dn.Loss\_{DRC}=\sum\_{n=1}^{N}EAD\_{n}\cdot\mathbb{\mathbf{1}}\_{D\_{n}}\cdot LGD\_{n}. |  |

This quantity
may not be available in closed form, thus most banks develop
Montecarlo simulation algorithms. Indeed, also the Basel regulation
explicitly refers to the simulation approach. Due to the extremely high confidence
level α=99.9%\alpha=99.9\%, to achieve a sufficient accuracy the number
of simulation scenarios must be very high, usually in the range [100​k,1​M​l​n]\left[100k,1Mln\right].
At the end of the simulation cycle, the quantile is estimated (empirically or using some smoother estimator, in line with the usual approach adopted for computing the *VaR* by historical simulation).

With respect to the work by [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)], where the authors deal
with the losses coming from the claims of the clients (i.e., the domain of
the distribution lies in one-side in the real axis), we recall that for the *VaR*
of the financial portfolio, a bank can experience both profits and
losses, while for the *DRC* we just have losses, so making the
context identical to that of the insurance sector.

#### 4.2.3 Market Risk in the Insurance field: Monte Carlo approach

While in the banking sector the liabilities side of the balance sheet typically mirrors the asset side—comprising the same types of instruments such as bonds, equities, derivatives, and loans with opposite signs—in the insurance business the situation is structurally different. The asset side, usually consisting of bonds and investment funds, is primarily designed to hedge the liabilities, namely the claims arising from policyholders’ underwriting activity.

Since the products sold to clients span very heterogeneous categories (life, longevity, accident, financial, and others) and often include numerous complex clauses linked to a wide range of contingent events, it becomes extremely challenging to construct a fully granular model incorporating all the specific inputs. For this reason, most insurance companies adopting a probabilistic approach to risk modeling rely instead on a compact set of risk factors, which are expected to adequately capture the distribution of profits and losses across the entire balance sheet.

To do that, the insurances use an economic scenario generator (ESG) that adopts the Monte Carlo simulation to project thousands of paths of the selected risk factors. For each path, all the positions of the insurance are evaluated to obtain the profile of profits and losses. Finally, the desired risk measures (percentiles, expected shortfall, etc) are estimated by analyzing the simulated results.
For a recent extended review see [[EIOPA, 2025](https://arxiv.org/html/2511.21556v1#bib.bibx17)].
Briefly, the Monte Carlo approach is not a choice in the insurance sector, but it represents a mandatory tool, due to the high number of risk factors and to the complexity of the products managed in insurance.
Of course, also in the practical applications several improvements have been implemented to reduce the weaknesses of the basic Monte Carlo approach, such as the simulation error.
The improvements are related to both the simulation step (by low discrepancy algorithm, quasi Monte Carlo methods, etc) and the estimation step, by smoothing the straight empirical estimator with more robust estimators, e,g, the Harrel-Davis estimator.
In our application, we collected samples of 100K or 200K simulations related to the market risk of a major European insurance company and compared the 3-points results, mainly m1m\_{1} and m2m\_{2}, with respect to the 0.995 1 year Solvency V​a​RVaR.

### 4.3 The Dataset

The data on which we apply the approach presented in this paper includes
1 year of daily PnLs time series of a representative portfolio
of a large European bank, encompassing both its banking and trading
books. As explained in the previous section, the PnLs have
been obtained by full revaluation of the positions composing the portfolio
with historical simulations of the risk factors. The time window includes
254 business dates (July 3rd 2023- July 1st 2024).

The portfolio consists of more that 100k positions, spanning from
bonds to equities to derivatives. A couple of business dates where
some outliers were detected (due to failures in the bank software
systems) have been removed. It is worth to note that the process to
get the portfolio VaR is typically a bottom-up process. In
other words, Formula [13](https://arxiv.org/html/2511.21556v1#S4.E13 "In 4.2.1 Market Risk with Historical Simulation ‣ 4.2 Applications Overview and Preliminary Concepts ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach") is just a synthetic definition, as
it is practically calculated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​n​L[t,t0+h]=∑m=1Mfm​(t0+h,𝐙+𝐘t+h,𝐏n),PnL\_{[t,t\_{0}+h]}=\sum\_{m=1}^{M}f\_{m}(t\_{0}+h,{\bf Z}+{\bf Y}\_{t+h},{\bf P}\_{n}), |  | (15) |

being nn the index of each position in the portfolio and 𝐏n{\bf P}\_{n}
the information (maturity, coupon, currency, etc) related to any position.
The *VaR* in historical simulation (Case 1) is then usually reported at
a portfolio level, but it can be easily broken down for any purpose
at any more granular level, according to the different analysis that
are required.

As concerns the DRC (Case 2), we have for the same bank a set of some end-of-month calculation, referred to March 2024, June 2024, December 2024
and to February 2025. The outcomes are based on 200​k200k simulations.
The portfolio consists of many thousands positions, belonging to O​(103)O\left(10^{3}\right)
issuers chat could default. Finally, for the insurance portfolio (Case 3), we analyzed an array of 100​k100k PnL generated by a multi dimensional Gaussian copula based on about 150150 risk factors.

To test the methodology and the numerical procedures in a more comprehensive context, we exploit the methods for the three fields defined in the previous section.

* •

  Case 1: Market Risk in the Banking sector. In this case the methodology for the PnL distribution is based on the historical simulation with 250 scenarios. Regulatory VaR (Basel regulation): 1 day, 99% confidence level.
  Risk sources: equity, interest rates, forex, spread, commodities.
* •

  Case 2: Credit Risk in the Banking sector. Then we refer to binary events driven by PD (Default Probability), that determine the losses by the LGD (loss given default) parameter applied to the defaulted position. LGD could be stochastic, e.g. a Beta random variable in the [0,100%][0,100\%] range. Methodology for the PnL distribution: Montecarlo simulation, multivariate gaussian copula, Merton-type default model. Regulatory VaR (Basel regulation): 1 year, 99.9% confidence level. Risk source: default.
* •

  Case 3: Market Risk in the Insurance sector. Here the methodology for the PnL distribution is based on Montecarlo simulation, multivariate gaussian copula, and Merton-type default model. Regulatory VaR (Solvency regulation): 1 year, 99.5% confidence level. Risk sources: equity, interest rates, forex, spread, credit migration.

### 4.4 Results

In this subsection we will show that overall, the results demonstrate that our methodology based on the magnitude propensity remains theoretically sound, numerically stable, and flexible enough to account for diverse risk profiles, while preserving interpretability across market, credit, and insurance domains.

#### 4.4.1 Case 1: Market Risk in the Banking Sector

In the initial stage of analysis, we consider the analytical solution obtained by quantization using the fixed-point method, allowing the quantities m1m\_{1} and m2m\_{2} to vary freely, i.e. subject only to the natural constraint
0<m1<m2<w​o​r​s​t​c​a​s​e0<m\_{1}<m\_{2}<worst\ case. Figure [2](https://arxiv.org/html/2511.21556v1#S4.F2 "Figure 2 ‣ 4.4.1 Case 1: Market Risk in the Banking Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach") illustrates the daily evolution of m1m\_{1} and m2m\_{2}, and compares them with the conventional risk measures—V​a​RVaR at the 99% confidence level and ES at the
97.5% level, the latter chosen to ensure comparability with the 99% VaR under a Gaussian framework. The unconstrained three-point distribution provides a clear and interpretable structure for quantifying risk, yielding results of a conservative nature that capture both moderate and extreme losses while avoiding excessive overestimation.

The interpretation of m1m\_{1} as a measure of moderate risk appears straightforward; however, the parameter m2m\_{2}
often exhibits overly conservative behavior, frequently taking values below the corresponding VaR. This outcome is expected, as the VaR constraint becomes more binding in market environments characterized by moderate tail risk and smoother loss distributions. Consequently, the resulting estimates tend to be slightly conservative, consistent with the regulatory framework that defines VaR at the 99% confidence level over a one-day horizon. To maintain coherence with this framework—where VaR is associated with extreme risk levels—we subsequently impose a constraint requiring m2m\_{2}
to exceed the VaR threshold.

![Refer to caption](Images/mkt_timeseries_noconstr.png)


Figure 2: Time series plot of VaR 99%, ES 97.5%, m1m\_{1} and m2m\_{2} (without constraints on m2m\_{2}).

If we add a constraint on the m2m\_{2}, the methodology provides the most satisfactory results, see Figure [3](https://arxiv.org/html/2511.21556v1#S4.F3 "Figure 3 ‣ 4.4.1 Case 1: Market Risk in the Banking Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach").

![Refer to caption](Images/mkt_timeseries_constr.png)


Figure 3: Time series plot of VaR 99%, ES 97.5%, m1m\_{1} and m2m\_{2} (with constraint m2>V​a​Rm\_{2}>VaR).

The
magnitude parameters m1m\_{1} and m2m\_{2} are intuitive, capturing both moderate and extreme
losses, with stable dynamics over time relative to VaR and ES. Meanwhile, p1p\_{1} and p2p\_{2}
remain smooth, with p2p\_{2} constrained by m2>V​a​Rm\_{2}>VaR and p1p\_{1} free to vary within the (0,1)(0,1)
range.

As concerns the volatility of m2m\_{2}, this naturally follows from the variability of the VaR computed by the historical simulation method. Indeed, when the scenarios contributing to the empirical percentile fall outside the rolling window used for VaR, jumps may occur independently of the portfolio composition. This phenomenon, known as the reshuffling effect, could be mitigated or controlled through smoothing techniques, in analogy with those employed in filtered historical simulation, see e.g. [[Barone-Adesi et al., 1999](https://arxiv.org/html/2511.21556v1#bib.bibx7)].

Furthermore, Table [2](https://arxiv.org/html/2511.21556v1#S4.T2 "Table 2 ‣ 4.4.1 Case 1: Market Risk in the Banking Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach") shows that employing different optimization methods—including those based on Differential Evolution (briefly recalled in Appendix [D](https://arxiv.org/html/2511.21556v1#A4 "Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) and on the Optimal Transport approach introduced earlier—yields remarkably consistent results. Computational times are extremely short (on the order of one second), thereby demonstrating the robustness and efficiency of the proposed methodology.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parameter Metric | Without Constraint Fixed Point Eq. Semi-Analytical | Without Constraint Quantization Diff. Evol. | VaR 99% Constraint Quantization Diff. Evol. | Without Constraint Opt. Transport Sinkhorn-Knopp | VaR 99% Constraint Opt. Transport Sinkhorn-Knopp |
| m1m\_{1} | 8,206,458 | 8,210,913 | 8,878,795 | 8,465,072 | 8,834,289 |
| m2m\_{2} | 21,452,567 | 21,453,539 | 24,397,039 | 21,971,367 | 23,925,852 |
| p0p\_{0} | 67.96% | 67.99% | 69.34% | 68.51% | 69.25% |
| p1p\_{1} | 26.77% | 26.74% | 27.26% | 26.94% | 27.26% |
| p2p\_{2} | 5.27% | 5.27% | 3.40% | 4.54% | 3.48% |
| VaR 99% | 22,531,887 | | | | |
| ES 97.5% | 23,636,174 | | | | |
| Worst-case | 34,616,367 | | | | |

Table 2: Market risk — Fixed Point Eq. (Semi-analytical using ([10](https://arxiv.org/html/2511.21556v1#S3.E10 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")),([11](https://arxiv.org/html/2511.21556v1#S3.E11 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))), Quantization with Differential Evolution and Optimal Transport (Sinkhorn-Knopp) methods. Comparison with and without the VaR 99% constraint on m2m\_{2}.

#### 4.4.2 Case 2: Credit Risk in the Banking Sector

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parameter Metric | Without Constraint Fixed Point Eq. Semi-Analytical | Without Constraint Quantization Diff. Evol. | VaR 99.9% Constraint Quantization Diff. Evol. | Without Constraint Opt. Transport Sinkhorn-Knopp | VaR 99.9% Constraint Opt. Transport Sinkhorn-Knopp |
| m1m\_{1} | 66,944,517 | 66,944,702 | 66,944,602 | 66,944,517 | 66,944,517 |
| m2m\_{2} | 455,901,571 | 455,900,234 | 455,901,519 | 455,901,571 | 455,901,571 |
| p0p\_{0} | 98.84% | 98.84% | 98.84% | 98.84% | 98.84% |
| p1p\_{1} | 1.13% | 1.13% | 1.13% | 1.13% | 1.13% |
| p2p\_{2} | 0.03% | 0.03% | 0.03% | 0.03% | 0.03% |
| VaR | 125,882,878 | | | | |
| ES | 256,621,107 | | | | |
| Worst-case | 980,312,060 | | | | |

Table 3: Credit risk comparison — Fixed Point Eq. (Semi-analytical using ([10](https://arxiv.org/html/2511.21556v1#S3.E10 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")),([11](https://arxiv.org/html/2511.21556v1#S3.E11 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))), Quantization with Differential Evolution and Optimal Transport (Sinkhorn-Knopp) methods. Comparison with and without the VaR 99.9% constraint on m2m\_{2}.

Within the Credit Risk framework—modeled through a Merton-type setting with a multivariate Gaussian copula—the VaR constraint on m2m\_{2} plays a less active role, as we can immediately see from Table [3](https://arxiv.org/html/2511.21556v1#S4.T3 "Table 3 ‣ 4.4.2 Case 2: Credit Risk in the Banking Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"). Due to portfolio concentration effects, the presence of dominant exposures shifts the loss distribution to the right, leading to a naturally high value of
m2m\_{2}, which already captures the fat-tail behavior of the underlying risk factors.
Moreover, due to typical combinatorial effects associated with default events, significantly different scenarios may lead to very similar loss values, thereby making risk measures structurally unstable and leading to even more fragile risk decomposition techniques, as illustrated in the Appendix [B](https://arxiv.org/html/2511.21556v1#A2 "Appendix B Intrinsic Instability of the Quantile in Credit Risk Modeling ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach").
Consequently, imposing a constraint on the value of m2m\_{2}
(for instance, requiring m2m\_{2}
to exceed the VaR) may be of limited relevance, since the tail of the distribution is already heavily skewed toward extreme values, forcing m2m\_{2}
into a region that the VaR is not able to reach, even with
the typical credit risk regulatory requirement of a 99.9% confidence level. In other words, the extreme values of the distribution are so pronounced that the VaR no longer provides an adequate representation of tail risk, whereas m2m\_{2}
effectively captures the true risk embedded in the distribution—yielding substantially higher values and thereby making any additional VaR-based constraint redundant.

![Refer to caption](Images/Credit_Risk_Tail_loss_Distrib.png)


Figure 4: Credit Risk in the Banking Sector (VaR 99.9%, ES 99.9 %): tail of the Loss distribution.

A comparison between m2m\_{2}
and the worst-case scenario, together with the graphical inspection of the losses histogram (see Figure [4](https://arxiv.org/html/2511.21556v1#S4.F4 "Figure 4 ‣ 4.4.2 Case 2: Credit Risk in the Banking Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")), clearly points out how
m2m\_{2}, acting as a barycenter of the extreme-loss scenarios, is positioned well above the VaR level, but remains consistently below the worst-case value.
In fact, from Figure [4](https://arxiv.org/html/2511.21556v1#S4.F4 "Figure 4 ‣ 4.4.2 Case 2: Credit Risk in the Banking Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach") we realize a sparse distribution on the right tail, leading to extreme losses with relatively non negligible probabilities. This is well captured by a relatively high value for m2m\_{2} with respect to the VaR and ES that underestimate the risk.

Due to the very high magnitude and low frequency of extreme losses, the associated parameter p2p\_{2} has a very small value. It is worth recalling, from an intuitive standpoint and in analogy with the theory of optimal transport, that the parameters (m,p)(m,p) jointly minimize the “effort” required to transfer probability masses and values from a continuous distribution toward its discrete representation.
This observation underscores the inherent tendency of VaR and ES to underestimate the probability of extreme losses, as is often the case in credit risk modeling.

In conclusion, the proposed methodology once again provides a more accurate and comprehensive representation of both moderate and extreme risks than traditional measures based on VaR and ES, particularly within the complex framework of credit risk.

#### 4.4.3 Case 3: Market Risk in the Insurance Sector

In the Insurance Market Risk case, the one-year horizon and 99.5% confidence level adopted under Solvency II standards confirm the adaptability of the proposed approach to different regulatory settings, see Table [4](https://arxiv.org/html/2511.21556v1#S4.T4 "Table 4 ‣ 4.4.3 Case 3: Market Risk in the Insurance Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach").

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parameter Metric | Without Constraint Fixed Point Eq. Semi-Analytical | Without Constraint Quantization Diff. Evol. | VaR 99.5% Constraint Quantization Diff. Evol. | Without Constraint Opt. Transport Sinkhorn-Knopp | VaR 99.5% Constraint Opt. Transport Sinkhorn-Knopp |
| m1m\_{1} | 292,726,533 | 292,251,249 | 292,250,135 | 292,726,533 | 292,726,533 |
| m2m\_{2} | 1,326,307,230 | 1,326,305,007 | 1,326,304,534 | 1,326,307,230 | 1,326,307,230 |
| p0p\_{0} | 90.03% | 90.00% | 90.00% | 90.03% | 90.03% |
| p1p\_{1} | 9.21% | 9.24% | 9.24% | 9.21% | 9.21% |
| p2p\_{2} | 0.76% | 0.76% | 0.76% | 0.76% | 0.76% |
| VaR | 1,103,006,334 | | | | |
| ES | 1,524,216,012 | | | | |
| Worst-case | 2,791,623,043 | | | | |

Table 4: Insurance market risk — Fixed Point Eq. (Semi-analytical using ([10](https://arxiv.org/html/2511.21556v1#S3.E10 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")),([11](https://arxiv.org/html/2511.21556v1#S3.E11 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))), Quantization with Differential Evolution and Optimal Transport (Sinkhorn-Knopp) methods. Comparison with and without the VaR 99.5% constraint on m2m\_{2}.

![Refer to caption](Images/Insurance_Market_Risk_Tail_loss_Distrib.png)


Figure 5: Insurance market risk (VaR 99.5%, ES 99.5%): tail of the Loss distribution.

In Figure [5](https://arxiv.org/html/2511.21556v1#S4.F5 "Figure 5 ‣ 4.4.3 Case 3: Market Risk in the Insurance Sector ‣ 4.4 Results ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach") we show the tail of the loss distribution, from which we deduce a considerable amount of losses beyond the VaR, although the difference between the parameter m2m\_{2}
and the VaR level is much less dramatic than in the previous case of Credit Risk. This behavior is consistent with the nature of the portfolio and the types of risks considered. Indeed, market risk within the insurance context also encompasses spread risk and migration risk (see Section [4.2.3](https://arxiv.org/html/2511.21556v1#S4.SS2.SSS3 "4.2.3 Market Risk in the Insurance field: Monte Carlo approach ‣ 4.2 Applications Overview and Preliminary Concepts ‣ 4 Case Study based on Real Datasets ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")). As a result, the PnL distribution may include potential jump events, yet with tail effects that are less pronounced than those typically observed in pure credit risk settings. Consequently,
m2m\_{2}
assumes a meaningful position from an informative standpoint, identifying potentially significant losses, while p2p\_{2}
—associated with extreme risk events—reflects a degree of conservatism (or prudence) broadly in line with the regulatory confidence level.

## 5 Conclusion

One of the long-standing challenges in risk management is the search for a risk measure that simultaneously satisfies the goals of objectivity, intuitiveness, and theoretical soundness. In this respect, the long and ongoing regulatory transition from Value-at-Risk (VaR) to Expected Shortfall (ES) clearly illustrates the difficulty of introducing new measures that can meet the expectations and requirements of all potential users.

In our work, we build on a frequency–severity framework, a well-established approach in the insurance domain that has recently received a rigorous theoretical foundation from [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)], who formalized the search for optimality within this setting. Our main contribution consists in extending this framework to the three-point case, which is particularly relevant from a practical perspective, as it captures the essential structure of risk profiles through three representative outcomes: “no loss,” “small loss” (with medium-to-high probability), and “extreme loss” (with low probability). This setting is especially meaningful in the insurance field, where such discrete representations of risk are commonly employed.

The magnitude–propensity framework was tested across three distinct and relevant use cases, with the aim of assessing both the behavior of the numerical procedures and the practical implementation of the results. In the unconstrained case, the optimization is free to explore the parameter space for the optimal configuration
(m1,m2,p1,p2)(m\_{1},m\_{2},p\_{1},p\_{2}). We then introduced a constraint on
m2m\_{2}
to align with regulatory requirements—specifically, the prescribed confidence level and time horizon associated with the Value-at-Risk (VaR) measure—thus enforcing
m2≥V​a​Rm\_{2}\geq VaR.

In the unconstrained setting, the numerical procedures exhibit mutual convergence and match the analytical fixed-point solution derived from the theoretical framework. This confirms that (i) the numerical algorithms are robust and reliable, and (ii) the theoretical formulation—yielding substantial computational savings—is correct. In the constrained case, where a theoretical benchmark is not yet available, the numerical methods still converge to consistent results. From a practical perspective, running multiple procedures in parallel may serve as a valuable cross-validation strategy to ensure stability and reliability of the optimal solution.

Finally, we note that the computational performance of the fixed-point approach is excellent, with execution times close to zero, confirming its efficiency and suitability for large-scale or real-time applications.

In the risk management process, an essential step is capital allocation, that is, the ex-ante assignment of the risk budget to individual business units and the ongoing monitoring to verify the risk reward performance of each business owner. This task requires rigorous methods of risk decomposition, particularly in the case of financial conglomerates or banking groups. A seminal reference in this area includes [[Garman, 1997](https://arxiv.org/html/2511.21556v1#bib.bibx26)], see also [[Tasche, 2002](https://arxiv.org/html/2511.21556v1#bib.bibx48)] and [[Tasche, 2004](https://arxiv.org/html/2511.21556v1#bib.bibx49)] for a formal rigorous framework.

As an initial approach, we consider it useful to extend the existing literature by treating the discrete variables m1m\_{1} and m2m\_{2}
as if they represented the true loss distribution, allowing the application of the above mentioned techniques. Roughly speaking, one has to calculate the expected loss of each business unit conditioned on the total loss of the parent portfolio, i.e., VaR in the classical approach, while m2m\_{2} in our setting. Under this perspective, risk decomposition reduces to the computation of a conditional expectation with respect to the discrete values assumed by the distribution.

We believe that our approach could be evaluated from a managerial perspective, not only as a tool for risk measurement and reporting, but also as a useful instrument to support the quantification of strategic parameters for financial institutions, such as risk appetite and risk tolerance.

## Appendix A Proofs

### A.1 Proof of Lemma [3.2](https://arxiv.org/html/2511.21556v1#S3.Thmthm2 "Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")

1. 1.

   Fix xx such that, w.l.o.g., h0​(x)<min⁡(h1​(x);h2​(x))h\_{0}(x)<\min(h\_{1}(x);h\_{2}(x)) and define
   d:=min⁡(h1​(x);h2​(x))−h0​(x)>0d:=\min(h\_{1}(x);h\_{2}(x))-h\_{0}(x)>0. Take 0<ϵ1<d,0<ϵ2<d−ϵ10<\epsilon\_{1}<d,0<\epsilon\_{2}<d-\epsilon\_{1}
   (that is, ϵ1+ϵ2<d\epsilon\_{1}+\epsilon\_{2}<d). Since h1,h2h\_{1},h\_{2} are
   continuous, also h1∧h2h\_{1}\wedge h\_{2} is continuous, then there exists
   δ>0\delta>0 such that ∀v∈ℝ2\forall v\in\mathbb{R}^{2} such that ‖v‖<δ||v||<\delta
   we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | h0​(x+v)≤\displaystyle h\_{0}(x+v)\leq | h0​(x)+ϵ1,\displaystyle h\_{0}(x)+\epsilon\_{1}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | h1​(x+v)∧h2​(x+v)≥\displaystyle h\_{1}(x+v)\wedge h\_{2}(x+v)\geq | h1​(x)∧h2​(x)−ϵ2.\displaystyle h\_{1}(x)\wedge h\_{2}(x)-\epsilon\_{2}. |  |

   Now, from h0​(x)=h1​(x)∧h2​(x)−dh\_{0}(x)=h\_{1}(x)\wedge h\_{2}(x)-d we get h0​(x)+ϵ1=h1​(x)∧h2​(x)+ϵ1−dh\_{0}(x)+\epsilon\_{1}=h\_{1}(x)\wedge h\_{2}(x)+\epsilon\_{1}-d,
   so that

   |  |  |  |
   | --- | --- | --- |
   |  | h0​(x+v)≤h1​(x)∧h2​(x)+ϵ1−d<h1​(x)∧h2​(x)−ϵ2≤h1​(x+v)∧h2​(x+v).\displaystyle h\_{0}(x+v)\leq h\_{1}(x)\wedge h\_{2}(x)+\epsilon\_{1}-d<h\_{1}(x)\wedge h\_{2}(x)-\epsilon\_{2}\leq h\_{1}(x+v)\wedge h\_{2}(x+v). |  |

   Therefore H​(x+v)=h0​(x+v)∀‖v‖<δH(x+v)=h\_{0}(x+v)\quad\forall||v||<\delta,
   so that HH is differentiable, with derivative given by ∇HB​(x)​(v)=∇H​(x)​v=∇h0​(x)​v\nabla H^{B}(x)(v)=\nabla H(x)v=\nabla h\_{0}(x)v.
2. 2.

   Take w.l.o.g. h0​(x)=h1​(x)<h2​(x)h\_{0}(x)=h\_{1}(x)<h\_{2}(x), so that H​(x)=h0​(x)∧h1​(x)H(x)=h\_{0}(x)\wedge h\_{1}(x).
   By repeating the same reasoning of the previous point, there exists
   δ>0\delta>0 such that for all ‖v‖<δ||v||<\delta

   |  |  |  |
   | --- | --- | --- |
   |  | H​(x+v)=h0​(x+v)∧h1​(x+v).\displaystyle H(x+v)=h\_{0}(x+v)\wedge h\_{1}(x+v). |  |

   Now, from Lemma 3.3 in [[Faugeras and Pagès, 2024](https://arxiv.org/html/2511.21556v1#bib.bibx23)] we have that h0∧h1h\_{0}\wedge h\_{1}
   is B-differentiable, so that HH is also B-differentiable and ∇BH​(x)​(v)=∇h1​(x)​v\nabla^{B}H(x)(v)=\nabla h\_{1}(x)v.
3. 3.

   We have H​(x)=h0​(x)=h1​(x)=h2​(x)H(x)=h\_{0}(x)=h\_{1}(x)=h\_{2}(x), so that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | H​(x+v)−H​(x)\displaystyle H(x+v)-H(x) | =min⁡(h0​(x+v)−h0​(x);h1​(x+v)−h1​(x);h2​(x+v)−h2​(x))\displaystyle=\min(h\_{0}(x+v)-h\_{0}(x);h\_{1}(x+v)-h\_{1}(x);h\_{2}(x+v)-h\_{2}(x)) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =min⁡(h0​(x+v)−h0​(x);min⁡(h1​(x+v)−h1​(x);h2​(x+v)−h2​(x))).\displaystyle=\min(h\_{0}(x+v)-h\_{0}(x);\min(h\_{1}(x+v)-h\_{1}(x);h\_{2}(x+v)-h\_{2}(x))). |  |

   Now, using the inequality |min⁡(a;b)−min⁡(c;d)|≤max⁡(|a−c|;|b−d|)|\min(a;b)-\min(c;d)|\leq\max(|a-c|;|b-d|)
   with

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | a\displaystyle a | =h0​(x+v)−h0​(x),\displaystyle=h\_{0}(x+v)-h\_{0}(x), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | b\displaystyle b | =min⁡(h1​(x+v)−h1​(x);h2​(x+v)−h2​(x)),\displaystyle=\min(h\_{1}(x+v)-h\_{1}(x);h\_{2}(x+v)-h\_{2}(x)), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | c\displaystyle c | =∇h0​(x)​v,\displaystyle=\nabla h\_{0}(x)v, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | d\displaystyle d | =∇B(h1∧h2)⁡(x)​(v),\displaystyle=\nabla^{B}(h\_{1}\wedge h\_{2})(x)(v), |  |

   we get

   |  |  |  |
   | --- | --- | --- |
   |  | |H(x+v)−H(x)−min(∇h0(x)v;∇Bh1∧h2)(x)(v))|\displaystyle|H(x+v)-H(x)-\min(\nabla h\_{0}(x)v;\nabla^{B}h\_{1}\wedge h\_{2})(x)(v))| |  |
   |  |  |  |
   | --- | --- | --- |
   |  | ≤max⁡(|h0​(x+v)−h0​(x)−∇h0​(x)​v|;|min⁡(h1​(x+v)−h1​(x);h2​(x+v)−h2​(x))−∇B(h1∧h2)⁡(x)​v|)\displaystyle\leq\max(|h\_{0}(x+v)-h\_{0}(x)-\nabla h\_{0}(x)v|;|\min(h\_{1}(x+v)-h\_{1}(x);h\_{2}(x+v)-h\_{2}(x))-\nabla^{B}(h\_{1}\wedge h\_{2})(x)v|) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | =max⁡(|h0​(x+v)−h0​(x)−∇h0​(x)​v|;|h1∧h2​(x+v)−h1∧h2​(x)−∇B(h1∧h2)⁡(x)​(v)|)\displaystyle=\max(|h\_{0}(x+v)-h\_{0}(x)-\nabla h\_{0}(x)v|;|h\_{1}\wedge h\_{2}(x+v)-h\_{1}\wedge h\_{2}(x)-\nabla^{B}(h\_{1}\wedge h\_{2})(x)(v)|) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | =max⁡(‖v‖​|o​(1)|;|h1∧h2​(x+v)−h1∧h2​(x)−min⁡(∇h1​(x)​v;∇h2​(x)​v)|)\displaystyle=\max(||v|||o(1)|;|h\_{1}\wedge h\_{2}(x+v)-h\_{1}\wedge h\_{2}(x)-\min(\nabla h\_{1}(x)v;\nabla h\_{2}(x)v)|) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | =‖v‖​max⁡(|o​(1)|;|o​(1)|),\displaystyle=||v||\max(|o(1)|;|o(1)|), |  |

   therefore

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x)​(v)\displaystyle\nabla^{B}H(x)(v) | =min⁡(∇h0​(x)​v;min⁡(∇h1​(x)​v;∇h2​(x)​v))\displaystyle=\min(\nabla h\_{0}(x)v;\min(\nabla h\_{1}(x)v;\nabla h\_{2}(x)v)) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =min⁡(∇h0​(x)​v;∇h1​(x)​v;∇h2​(x)​v),\displaystyle=\min(\nabla h\_{0}(x)v;\nabla h\_{1}(x)v;\nabla h\_{2}(x)v), |  |

   and the proof is complete.

### A.2 Proof of Theorem [3.3](https://arxiv.org/html/2511.21556v1#S3.Thmthm3 "Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")

The proof is organized in two steps.

#### A.2.1 Step 1: B-derivatives of the function HH

Let H​(x1,x2)=X2∧(X−x1)2∧(X−x2)2H(x\_{1},x\_{2})=X^{2}\wedge(X-x\_{1})^{2}\wedge(X-x\_{2})^{2}
with 0<x1<x20<x\_{1}<x\_{2}. Fix XX and set h0​(x1,x2)=X2;h1​(x1,x2)=(X−x1)2;h2​(x1,x2)=(X−x2)2h\_{0}(x\_{1},x\_{2})=X^{2};h\_{1}(x\_{1},x\_{2})=(X-x\_{1})^{2};h\_{2}(x\_{1},x\_{2})=(X-x\_{2})^{2}.
We have then the following seven possibilities.

1. 1.

   h0​(x)=h1​(x)=h2​(x)h\_{0}(x)=h\_{1}(x)=h\_{2}(x) for x=(x1,x2)∈{(0,0),(0,2​X),(2​X,0),(2​X,2​X)}x=(x\_{1},x\_{2})\in\{(0,0),(0,2X),(2X,0),(2X,2X)\}.
   In this case we have H​(x1,x2)=X2H(x\_{1},x\_{2})=X^{2} and the B-derivatives
   are given respectively by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(0,0)​(v)\displaystyle\nabla^{B}H(0,0)(v) | =min⁡(0;−2​X​v1;−2​X​v2),\displaystyle=\min(0;-2Xv\_{1};-2Xv\_{2}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(0,2​X)​(v)\displaystyle\nabla^{B}H(0,2X)(v) | =min⁡(0;−2​X​v1;2​X​v2),\displaystyle=\min(0;-2Xv\_{1};2Xv\_{2}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(2​X,0)​(v)\displaystyle\nabla^{B}H(2X,0)(v) | =min⁡(0;2​X​v1;−2​X​v2),\displaystyle=\min(0;2Xv\_{1};-2Xv\_{2}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(2​X,2​X)​(v)\displaystyle\nabla^{B}H(2X,2X)(v) | =min⁡(0;2​X​v1;2​X​v2).\displaystyle=\min(0;2Xv\_{1};2Xv\_{2}). |  |
2. 2.

   h0​(x)=h1​(x)<h2​(x)h\_{0}(x)=h\_{1}(x)<h\_{2}(x) for x=(x1,x2)x=(x\_{1},x\_{2}) such that (x1=0a​n​dx2>2​X)(x\_{1}=0\quad and\quad x\_{2}>2X)
   or (x1=2​Xa​n​dx2>2​X)(x\_{1}=2X\quad and\quad x\_{2}>2X). In this case we still have H​(x1,x2)=X2H(x\_{1},x\_{2})=X^{2}
   and the B-derivative is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(0,x2)​(v)\displaystyle\nabla^{B}H(0,x\_{2})(v) | =min⁡(0;−2​X​v1),\displaystyle=\min(0;-2Xv\_{1}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(2​X,x2)​(v)\displaystyle\nabla^{B}H(2X,x\_{2})(v) | =min⁡(0;2​X​v1),\displaystyle=\min(0;2Xv\_{1}), |  |

   provided that x2>2​Xx\_{2}>2X.
3. 3.

   h0​(x)=h2​(x)<h1​(x)h\_{0}(x)=h\_{2}(x)<h\_{1}(x) for (x1>2​Xa​n​dx2=0)(x\_{1}>2X\quad and\quad x\_{2}=0) or (x1>2​Xa​n​dx2=2​X)(x\_{1}>2X\quad and\quad x\_{2}=2X).
   In this case we still have H​(x1,x2)=X2H(x\_{1},x\_{2})=X^{2} and the B-derivative
   is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x1,0)​(v)\displaystyle\nabla^{B}H(x\_{1},0)(v) | =min⁡(0;−2​X​v2),\displaystyle=\min(0;-2Xv\_{2}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x1,2​X)​(v)\displaystyle\nabla^{B}H(x\_{1},2X)(v) | =min⁡(0;2​X​v2),\displaystyle=\min(0;2Xv\_{2}), |  |

   provided that x1>2​Xx\_{1}>2X.
4. 4.

   h1​(x)=h2​(x)<h0​(x)h\_{1}(x)=h\_{2}(x)<h\_{0}(x) for (x1+x2=2​Xa​n​d0<x1<x2<2​X)(x\_{1}+x\_{2}=2X\quad and\quad 0<x\_{1}<x\_{2}<2X).
   This time we have H​(x1,x2)=(X−x1)2=(X−x2)2H(x\_{1},x\_{2})=(X-x\_{1})^{2}=(X-x\_{2})^{2} and
   the B-derivative is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x1,2​X−x1)​(v)\displaystyle\nabla^{B}H(x\_{1},2X-x\_{1})(v) | =min⁡(−2​(X−x1)​v1;−2​(X−x2)​v2),\displaystyle=\min(-2(X-x\_{1})v\_{1};-2(X-x\_{2})v\_{2}), |  |

   provided that x1+x2=2​Xx\_{1}+x\_{2}=2X and 0<x1<x2<2​X0<x\_{1}<x\_{2}<2X.
5. 5.

   h0​(x)<h1​(x)∧h2​(x)h\_{0}(x)<h\_{1}(x)\wedge h\_{2}(x) for x1>2​Xx\_{1}>2X. We have H​(x1,x2)=X2H(x\_{1},x\_{2})=X^{2}
   and the B-derivative is zero.
6. 6.

   h1​(x)<h0​(x)<h2​(x)h\_{1}(x)<h\_{0}(x)<h\_{2}(x) for (x1<2​Xa​n​dx1+x2>2​X)(x\_{1}<2X\quad and\quad x\_{1}+x\_{2}>2X).
   This time we have H​(x1,x2)=(X−x1)2H(x\_{1},x\_{2})=(X-x\_{1})^{2} and the B-derivative
   is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x1,x2)​(v)\displaystyle\nabla^{B}H(x\_{1},x\_{2})(v) | =−2​(X−x1)​v1,\displaystyle=-2(X-x\_{1})v\_{1}, |  |

   provided that x1<2​Xx\_{1}<2X and x1+x2>2​Xx\_{1}+x\_{2}>2X.
7. 7.

   h2​(x)<h0​(x)<h1​(x)h\_{2}(x)<h\_{0}(x)<h\_{1}(x) for (x1+x2<2​X)(x\_{1}+x\_{2}<2X). This time we
   have H​(x1,x2)=(X−x2)2H(x\_{1},x\_{2})=(X-x\_{2})^{2} and the B-derivative is given
   by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BH​(x1,x2)​(v)\displaystyle\nabla^{B}H(x\_{1},x\_{2})(v) | =−2​(X−x2)​v2,\displaystyle=-2(X-x\_{2})v\_{2}, |  |

   provided that x1+x2<2​Xx\_{1}+x\_{2}<2X.

#### A.2.2 Step 2: B-differentiability of the objective function DD and critical points for the distortion

Set

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇BD​(x)​(v):=𝔼​[∇BH​(x)​(v)],\displaystyle\nabla^{B}D(x)(v):=\mathbb{E}[\nabla^{B}H(x)(v)], |  | (16) |

and consider now the different possibilities listed in the previous
subsection.

1. 1.

   The point x=(0,0)x=(0,0) is critical for the distortion function if ∇BD​(0,0)​(v)≥0​∀v∈ℝ2\nabla^{B}D(0,0)(v)\geq 0\forall v\in\mathbb{R}^{2}.
   Now,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(0,0)​(v)\displaystyle\nabla^{B}D(0,0)(v) | =𝔼​[min⁡(0;−2​X​v1;−2​X​v2)]\displaystyle=\mathbb{E}[\min(0;-2Xv\_{1};-2Xv\_{2})] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =𝔼​[min⁡(−2​X​v1;−2​X​v2)]<0\displaystyle=\mathbb{E}[\min(-2Xv\_{1};-2Xv\_{2})]<0 |  |

   for v1>0,v2>0v\_{1}>0,v\_{2}>0, therefore the point x=(0,0)x=(0,0) is not critical
   for the distortion. The same holds true for (0,2​X)(0,2X), since ∇BD​(0,2​X)​(v)=𝔼​[min⁡(0;−2​X​v1;−2​X​v2)]<0\nabla^{B}D(0,2X)(v)=\mathbb{E}[\min(0;-2Xv\_{1};-2Xv\_{2})]<0
   for v1>0,v2<0v\_{1}>0,v\_{2}<0. Using the same argument one can exclude also
   (2​X,0),(2​X,2​X)(2X,0),(2X,2X).
2. 2.

   Consider now x2>2​Xx\_{2}>2X, we get

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(0,x2)​(v)\displaystyle\nabla^{B}D(0,x\_{2})(v) | =𝔼​[min⁡(0;−2​X​v1)]<0f​o​rv1>0,\displaystyle=\mathbb{E}[\min(0;-2Xv\_{1})]<0\quad\quad for\quad v\_{1}>0, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(2​X,x2)​(v)\displaystyle\nabla^{B}D(2X,x\_{2})(v) | =𝔼​[min⁡(0;2​X​v1)]<0f​o​rv1<0,\displaystyle=\mathbb{E}[\min(0;2Xv\_{1})]<0\quad\quad\quad for\quad v\_{1}<0, |  |

   so that the (0,x2),(2​X,x2)(0,x\_{2}),(2X,x\_{2}) are not critical for x2>2​Xx\_{2}>2X.
3. 3.

   Let x1>2​Xx\_{1}>2X,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(x1,0)​(v)\displaystyle\nabla^{B}D(x\_{1},0)(v) | =𝔼​[min⁡(0;−2​X​v2)]<0f​o​rv2>0,\displaystyle=\mathbb{E}[\min(0;-2Xv\_{2})]<0\quad\quad for\quad v\_{2}>0, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(x1,2​X)​(v)\displaystyle\nabla^{B}D(x\_{1},2X)(v) | =𝔼​[min⁡(0;2​X​v2)]<0f​o​rv2<0,\displaystyle=\mathbb{E}[\min(0;2Xv\_{2})]<0\quad\quad for\quad v\_{2}<0, |  |

   therefore (x1,0),(x1,2​X)(x\_{1},0),(x\_{1},2X) are not critical for x1>2​Xx\_{1}>2X.
4. 4.

   Consider x1+x2=2​Xx\_{1}+x\_{2}=2X and 0<x1<x2<2​X0<x\_{1}<x\_{2}<2X:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(x1,2​X−x1)​(v)\displaystyle\nabla^{B}D(x\_{1},2X-x\_{1})(v) | =𝔼​[min⁡(−2​(X−x1)​v1;−2​(X−x2)​v2)]<0f​o​rv1>0,v2<0,\displaystyle=\mathbb{E}[\min(-2(X-x\_{1})v\_{1};-2(X-x\_{2})v\_{2})]<0\quad\quad for\quad v\_{1}>0,v\_{2}<0, |  |

   therefore (x1,2​X−x1)(x\_{1},2X-x\_{1}) is not critical for x1+x2=2​Xx\_{1}+x\_{2}=2X
   and 0<x1<x2<2​X0<x\_{1}<x\_{2}<2X.
5. 5.

   We have ∇BD​(x1,x2)​(v)=0\nabla^{B}D(x\_{1},x\_{2})(v)=0 for x1>2​Xx\_{1}>2X.
6. 6.

   Take x1<2​Xx\_{1}<2X and x1+x2>2​Xx\_{1}+x\_{2}>2X:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(x1,x2)​(v)=\displaystyle\nabla^{B}D(x\_{1},x\_{2})(v)= | 𝔼​[−2​(X−x1)​v1​𝟏x1<2​X​𝟏x1+x2>2​X]\displaystyle\mathbb{E}[-2(X-x\_{1})v\_{1}{\bf 1}\_{x\_{1}<2X}{\bf 1}\_{x\_{1}+x\_{2}>2X}] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +𝔼​[min⁡(0;2​X​v1)​𝟏x1=2​X​𝟏x2>2​X]\displaystyle+\mathbb{E}[\min(0;2Xv\_{1}){\bf 1}\_{x\_{1}=2X}{\bf 1}\_{x\_{2}>2X}] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +𝔼​[min⁡(−2​(X−x1)​v1;−2​(X−x1)​v2)​𝟏x1<2​X​𝟏x1+x2=2​X],\displaystyle+\mathbb{E}[\min(-2(X-x\_{1})v\_{1};-2(X-x\_{1})v\_{2}){\bf 1}\_{x\_{1}<2X}{\bf 1}\_{x\_{1}+x\_{2}=2X}], |  |

   so that (x1,x2)(x\_{1},x\_{2}) may be a critical point.
7. 7.

   Finally, let consider x1+x2<2​Xx\_{1}+x\_{2}<2X:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∇BD​(x1,x2)​(v)\displaystyle\nabla^{B}D(x\_{1},x\_{2})(v) | =𝔼​[−2​(X−x2)​v2​𝟏x1+x2<2​X],\displaystyle=\mathbb{E}[-2(X-x\_{2})v\_{2}{\bf 1}\_{x\_{1}+x\_{2}<2X}], |  |

   then (x1,x2)(x\_{1},x\_{2}) may be a critical point.

In conclusion, it turns out that the function v→∇BD​(x)​(v)v\rightarrow\nabla^{B}D(x)(v)
is positively homogeneous for x∈ℝ+2x\in\mathbb{R}\_{+}^{2}, hence DD
is B-differentiable. Moreover, collecting the different cases one gets
([9](https://arxiv.org/html/2511.21556v1#S3.E9 "In Theorem 3.3. ‣ Lemma 3.2. ‣ Definition 3.1. ‣ 3.3 Extension to the case of 3-Points Optimal Constrained Quantization ‣ 3 From Scalar to Vectorial Risk Measures and from Continuous to Discrete Distributions ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")), and the proof of the theorem is complete.

## Appendix B Intrinsic Instability of the Quantile in Credit Risk Modeling

Extreme quantiles such as the 99.9% VaR play a central role in the computation of the
Default Risk Charge (DRC).
However, when applied to concentrated credit portfolios, these percentiles may exhibit a
structural instability that does not originate from Monte Carlo error,
but from the intrinsic combinatorial geometry of the loss distribution.
Before analysing this phenomenon, we introduce the simplified analytical setup used to isolate and quantify such behavior.

Analytical setup.
Consider a reduced set of the NN largest obligors (covering the majority of portfolio EAD)
and model defaults via a one–factor Gaussian copula.
For obligor n=1,…,Nn=1,\ldots,N, we define

|  |  |  |
| --- | --- | --- |
|  | Zn=ρn​U+1−ρn​εn,Z\_{n}=\sqrt{\rho\_{n}}\,U+\sqrt{1-\rho\_{n}}\,\varepsilon\_{n}, |  |

where U,εnU,\varepsilon\_{n} are independent standard Gaussian random variables, and a default occurs whenever ZnZ\_{n} falls below the threshold given by the corresponding default probability, i.e.
bn:=Φ−1​(PDn)b\_{n}:=\Phi^{-1}(\mathrm{PD}\_{n}).
The portfolio loss in
[2](https://arxiv.org/html/2511.21556v1#S2.Ex3 "2 Scalar Risk Measures: Review and Limitations ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")
is therefore

|  |  |  |
| --- | --- | --- |
|  | L​o​s​sD​R​C=∑n=1NE​A​Dn⋅𝟏{Zn≤bn}⋅L​G​Dn,Loss\_{DRC}=\sum\_{n=1}^{N}EAD\_{n}\cdot\mathbf{1}\_{\{Z\_{n}\leq b\_{n}\}}\cdot LGD\_{n}, |  |

with deterministic LGD in this experiment.

Since each obligor may be in default or not, the loss distribution is supported on the
2N2^{N} possible default/non–default combinations.
For each configuration r⊂{1,…,N}r\subset\{1,\ldots,N\}, the corresponding loss is

|  |  |  |
| --- | --- | --- |
|  | Lossr=∑n∈rE​A​Dn⋅𝟏{Zn≤bn}⋅L​G​Dn,\mathrm{Loss}\_{r}=\sum\_{n\in r}EAD\_{n}\cdot\mathbf{1}\_{\{Z\_{n}\leq b\_{n}\}}\cdot LGD\_{n}, |  |

while its probability under the copula reduces to a one–dimensional integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr=∫−∞+∞[∏n∈rΦ​(bn−ρn​u1−ρn)]​[∏n∉r(1−Φ​(bn−ρn​u1−ρn))]​ϕ​(u)​𝑑u,P\_{r}=\int\_{-\infty}^{+\infty}\left[\prod\_{n\in r}\Phi\!\Big(\tfrac{b\_{n}-\sqrt{\rho\_{n}}u}{\sqrt{1-\rho\_{n}}}\Big)\right]\left[\prod\_{n\notin r}\Big(1-\Phi\!\Big(\tfrac{b\_{n}-\sqrt{\rho\_{n}}u}{\sqrt{1-\rho\_{n}}}\Big)\Big)\right]\phi(u)\,du, |  | (17) |

evaluated via Gaussian quadrature.
Sorting all (Lossr,Pr)(\mathrm{Loss}\_{r},P\_{r}) pairs yields the exact loss distribution and, in particular,
the exact 99.9% Default Risk Charge DRC is defined as

|  |  |  |
| --- | --- | --- |
|  | DRC=min⁡{Lossr:Pcum​(r)≥0.999},\mathrm{DRC}=\min\big\{\mathrm{Loss}\_{r}:P\_{\mathrm{cum}}(r)\geq 0.999\big\}, |  |

where Pcum​(r)=∑|m|≤|r|PmP\_{\mathrm{cum}}(r)=\sum\_{|m|\leq|r|}P\_{m}, where the sum is extended to uncompatible events.

Focusing on the percentile instability.
To analyse how the percentile behaves in the tail,
we examine the symmetric window

|  |  |  |
| --- | --- | --- |
|  | {k−500,…,k+500},\{k-500,\ldots,k+500\}, |  |

where kk is the index of the order statistic corresponding to the 99.9% quantile.
This window contains the ranked scenarios whose cumulative probabilities lie immediately below and above 0.999—precisely where small perturbations may change the identity of the selected quantile.

![Refer to caption](Images/Default_scenarios_n31_v7.png)

Figure 6: Tail–stability analysis around the 99.9% VaR (DRC). The figure shows the ordered loss contributions in the neighbourhood of the 99.9% percentile, highlighting how consecutive scenarios exhibit nearly identical loss levels.
Because cumulative probabilities are extremely small in the tail, even minimal perturbations in PDs, correlations, exposures or in the ordering of almost equal losses may shift the DRC from Loss(k)\mathrm{Loss}^{(k)} to Loss(k+1)\mathrm{Loss}^{(k+1)} without any material change in magnitude.
The visual alignment of points illustrates this intrinsic sensitivity of the DRC to local fluctuations in the extreme tail.

Figure [6](https://arxiv.org/html/2511.21556v1#A2.F6 "Figure 6 ‣ Appendix B Intrinsic Instability of the Quantile in Credit Risk Modeling ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach") displays, for each scenario in the quantile window,
(i) the default pattern across the N=31N=31 obligors (orange dots),
(ii) the cumulative probability αr\alpha\_{r},
and (iii) the corresponding loss Lossr\mathrm{Loss}\_{r}.
The figure highlights a crucial structural phenomenon:
despite the fact that default patterns differ significantly across scenarios, the resulting losses in this tail region are numerically almost identical.
In other words, the instability is note related to the magnitude of the loss, but rather to the specific configuration of the defaulting obligors.
This arises because many combinations of EADn​LGDn\mathrm{EAD}\_{n}\mathrm{LGD}\_{n} sum to nearly the same value, an effect amplified by the combinatorial explosion of the support.

Consequently, since adjacent cumulative levels satisfy

|  |  |  |
| --- | --- | --- |
|  | αr+1−αr=Pr+1,\alpha\_{r+1}-\alpha\_{r}=P\_{r+1}, |  |

and the probabilities PrP\_{r} are extremely small near the tail, a minimal perturbation
(e.g. slight changes in PDs, correlations, exposures, or simply a reordering of nearly equal losses)
may shift the DRC from Loss(k)\mathrm{Loss}^{(k)} to Loss(k±1)\mathrm{Loss}^{(k\pm 1)} without any meaningful variation in loss magnitude.
The percentile therefore experiences a discontinuous jump driven purely by ranking, not by economic information.

Implication for VaR-based DRC.
The analysis makes clear that, for concentrated credit portfolios and extreme confidence levels,
the usability of VaR as a tail-risk measure is inherently limited: the 99.9% percentile becomes
highly sensitive to microscopic changes in the loss distribution and does not reliably reflect
the underlying risk structure.
This motivates the use of tail-aggregation methods—such as the magnitude–propensity framework introduced in our paper—which summarize information across multiple extreme-loss configurations rather than relying on a single order statistic.

## Appendix C The Sinkhorn–Knopp (SK) Algorithm

In this appendix, we provide some details on the numerical procedure adopted for the solution of the entropically regularized optimal transport problem, following the classical matrix-scaling approach originally introduced in [[Sinkhorn, 1964](https://arxiv.org/html/2511.21556v1#bib.bibx45), [Sinkhorn and Knopp, 1967](https://arxiv.org/html/2511.21556v1#bib.bibx46)] and later applied to optimal transport in [[Cuturi, 2013](https://arxiv.org/html/2511.21556v1#bib.bibx13)].

Consider two discrete probability measures
μ=∑i=1npi​δxi\mu=\sum\_{i=1}^{n}p\_{i}\,\delta\_{x\_{i}} and
ν=∑j=1mqj​δyj\nu=\sum\_{j=1}^{m}q\_{j}\,\delta\_{y\_{j}}, where
𝒑=(p1,…,pn)⊤\bm{p}=(p\_{1},\dots,p\_{n})^{\top} and 𝒒=(q1,…,qm)⊤\bm{q}=(q\_{1},\dots,q\_{m})^{\top}
are probability vectors, i.e. pi≥0p\_{i}\geq 0, qj≥0q\_{j}\geq 0 and
∑ipi=∑jqj=1\sum\_{i}p\_{i}=\sum\_{j}q\_{j}=1.
Let C∈ℝn×mC\in\mathbb{R}^{n\times m} be the cost matrix with entries
ci​j=c​(xi,yj)c\_{ij}=c(x\_{i},y\_{j}) for a given cost function c​(⋅,⋅)c(\cdot,\cdot).
The entropically regularized optimal transport problem reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | minΠ∈ℝ+n×m⁡{⟨C,Π⟩+ε​∑i=1n∑j=1mΠi​j​(log⁡Πi​j−1)}s.t.Π​𝟏m=𝒑,Π⊤​𝟏n=𝒒,\min\_{\Pi\in\mathbb{R}\_{+}^{n\times m}}\left\{\langle C,\Pi\rangle+\varepsilon\sum\_{i=1}^{n}\sum\_{j=1}^{m}\Pi\_{ij}\bigl(\log\Pi\_{ij}-1\bigr)\right\}\quad\text{s.t.}\quad\Pi\bm{1}\_{m}=\bm{p},\;\Pi^{\top}\bm{1}\_{n}=\bm{q}, |  | (18) |

where ε>0\varepsilon>0 is the regularization parameter,
⟨C,Π⟩=∑i​jci​j​Πi​j\langle C,\Pi\rangle=\sum\_{ij}c\_{ij}\Pi\_{ij},
and 𝟏k\bm{1}\_{k} denotes the kk-dimensional vector of ones.

Introducing the kernel matrix

|  |  |  |
| --- | --- | --- |
|  | Ki​j=exp⁡(−ci​jε),i=1,…,n,j=1,…,m,K\_{ij}=\exp\!\left(-\frac{c\_{ij}}{\varepsilon}\right),\qquad i=1,\dots,n,\;j=1,\dots,m, |  |

it is well known that any solution of ([18](https://arxiv.org/html/2511.21556v1#A3.E18 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) can be written in the
scaling form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π⋆=diag⁡(𝒖)​K​diag⁡(𝒗),\Pi^{\star}=\operatorname{diag}(\bm{u})\,K\,\operatorname{diag}(\bm{v}), |  | (19) |

for some positive vectors
𝒖∈ℝ++n\bm{u}\in\mathbb{R}^{n}\_{++} and 𝒗∈ℝ++m\bm{v}\in\mathbb{R}^{m}\_{++}.
The Sinkhorn–Knopp algorithm is an iterative matrix scaling procedure
that computes (𝒖,𝒗)(\bm{u},\bm{v}) such that the marginal constraints
in ([18](https://arxiv.org/html/2511.21556v1#A3.E18 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) are satisfied.

Let 𝒖(0)∈ℝ++n\bm{u}^{(0)}\in\mathbb{R}^{n}\_{++} and 𝒗(0)∈ℝ++m\bm{v}^{(0)}\in\mathbb{R}^{m}\_{++}
be initial scaling vectors, typically chosen as vectors of ones.
At iteration ℓ=0,1,2,…\ell=0,1,2,\dots, the algorithm performs the updates

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ui(ℓ+1)\displaystyle u^{(\ell+1)}\_{i} | =pi∑j=1mKi​j​vj(ℓ),i=1,…,n,\displaystyle=\frac{p\_{i}}{\sum\_{j=1}^{m}K\_{ij}v^{(\ell)}\_{j}},\qquad i=1,\dots,n, |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vj(ℓ+1)\displaystyle v^{(\ell+1)}\_{j} | =qj∑i=1nKi​j​ui(ℓ+1),j=1,…,m\displaystyle=\frac{q\_{j}}{\sum\_{i=1}^{n}K\_{ij}u^{(\ell+1)}\_{i}},\qquad j=1,\dots,m |  | (21) |

The sequence {(𝒖(ℓ),𝒗(ℓ))}ℓ≥0\{(\bm{u}^{(\ell)},\bm{v}^{(\ell)})\}\_{\ell\geq 0}
generated by ([20](https://arxiv.org/html/2511.21556v1#A3.E20 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))–([21](https://arxiv.org/html/2511.21556v1#A3.E21 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) defines a sequence of transport
plans

|  |  |  |
| --- | --- | --- |
|  | Π(ℓ)=diag⁡(𝒖(ℓ))​K​diag⁡(𝒗(ℓ)),\Pi^{(\ell)}=\operatorname{diag}\bigl(\bm{u}^{(\ell)}\bigr)\,K\,\operatorname{diag}\bigl(\bm{v}^{(\ell)}\bigr), |  |

whose row and column sums converge to 𝒑\bm{p} and 𝒒\bm{q}, respectively, under mild
assumptions on KK (e.g. all entries strictly positive).
In practice, the iterations are stopped when the violation of the marginals
is below a prescribed tolerance τ>0\tau>0, i.e. when

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Π(ℓ)​𝟏m−𝒑‖1+‖(Π(ℓ))⊤​𝟏n−𝒒‖1≤τ.\left\|\Pi^{(\ell)}\bm{1}\_{m}-\bm{p}\right\|\_{1}+\left\|(\Pi^{(\ell)})^{\top}\bm{1}\_{n}-\bm{q}\right\|\_{1}\leq\tau. |  | (22) |

For numerical stability, in particular when ε\varepsilon is small
and the entries of KK may underflow, the updates
([20](https://arxiv.org/html/2511.21556v1#A3.E20 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))–([21](https://arxiv.org/html/2511.21556v1#A3.E21 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) can be implemented in the log-domain.
Defining 𝜶(ℓ)=log⁡𝒖(ℓ)\bm{\alpha}^{(\ell)}=\log\bm{u}^{(\ell)} and
𝜷(ℓ)=log⁡𝒗(ℓ)\bm{\beta}^{(\ell)}=\log\bm{v}^{(\ell)}, one replaces the matrix–vector
products by log-sum-exp operations, which reduces the risk of numerical
underflow/overflow while leaving the fixed point ([19](https://arxiv.org/html/2511.21556v1#A3.E19 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) unchanged.

Once convergence has been reached (according to ([22](https://arxiv.org/html/2511.21556v1#A3.E22 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))),
the transport plan Π⋆\Pi^{\star} in ([19](https://arxiv.org/html/2511.21556v1#A3.E19 "In Appendix C The Sinkhorn–Knopp (SK) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) is used to compute
the (regularized) optimal transport cost

|  |  |  |
| --- | --- | --- |
|  | 𝒲ε​(𝒑,𝒒)=⟨C,Π⋆⟩+ε​∑i,jΠi​j⋆​(log⁡Πi​j⋆−1),\mathcal{W}\_{\varepsilon}(\bm{p},\bm{q})=\langle C,\Pi^{\star}\rangle+\varepsilon\sum\_{i,j}\Pi^{\star}\_{ij}\bigl(\log\Pi^{\star}\_{ij}-1\bigr), |  |

which is then employed in the subsequent stages of the analysis.

## Appendix D The Differential Evolution (DE) Algorithm

In this appendix, we provide some details on the numerical procedure we adopted for the optimization problem.

The Differential Evolution (DE) algorithm, originally proposed by
[[Storn and Price, 1997](https://arxiv.org/html/2511.21556v1#bib.bibx47)], is a stochastic and population-based global optimization technique belonging
to the family of evolutionary algorithms. It is particularly effective for solving
non-convex, non-differentiable, and multi-modal optimization problems.
Unlike gradient-based methods, DE relies exclusively on function evaluations, which makes it
robust even when the objective function f​(𝐱)f(\mathbf{x}) is noisy or discontinuous.

The algorithm evolves a population of candidate solutions across generations through a
sequence of variation mechanisms — mutation, crossover, and selection.
At each iteration, these operations allow the population to progressively explore the search
space and concentrate around high-performing regions, eventually converging to a near-optimal
solution for the problem under consideration.

The optimization problem is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐱∈Ω⁡f​(𝐱),\min\_{\mathbf{x}\in\Omega}f(\mathbf{x}), |  | (23) |

where Ω⊆ℝd\Omega\subseteq\mathbb{R}^{d} denotes the feasible domain of the
dd-dimensional decision vector 𝐱\mathbf{x}.
The approach consists in evolving a set of candidate solutions over successive generations.

At generation gg, the algorithm maintains a population of NPN\_{P} candidate
solutions,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱i,g=(xi,g(1),xi,g(2),…,xi,g(d)),i=1,2,…,NP,\mathbf{x}\_{i,g}=\bigl(x\_{i,g}^{(1)},x\_{i,g}^{(2)},\ldots,x\_{i,g}^{(d)}\bigr),\qquad i=1,2,\ldots,N\_{P}, |  | (24) |

which evolve iteratively through mutation, crossover, and selection.

Mutation. For each target vector 𝐱i,g\mathbf{x}\_{i,g}, a mutant vector
𝐯i,g\mathbf{v}\_{i,g} is generated according to the classical
DE/rand/1/bin scheme,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐯i,g=𝐱r1,g+F​(𝐱r2,g−𝐱r3,g),\mathbf{v}\_{i,g}=\mathbf{x}\_{r\_{1},g}+F\bigl(\mathbf{x}\_{r\_{2},g}-\mathbf{x}\_{r\_{3},g}\bigr), |  | (25) |

where r1,r2,r3∈{1,…,NP}r\_{1},r\_{2},r\_{3}\in\{1,\ldots,N\_{P}\} are distinct indices different from
ii, and F∈[0,2]F\in[0,2] is the mutation factor controlling the amplification of
the differential variation.
Equation ([25](https://arxiv.org/html/2511.21556v1#A4.E25 "In Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) therefore perturbs a base vector
𝐱r1,g\mathbf{x}\_{r\_{1},g} by adding a scaled difference of two other individuals,
thereby promoting exploration of the search space.

Crossover. To increase population diversity, a trial vector
𝐮i,g\mathbf{u}\_{i,g} is formed by combining components of the mutant and target
vectors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ui,g(j)={vi,g(j),if ​randj​(0,1)≤CR​ or ​j=jrand,xi,g(j),otherwise,j=1,…,d,u\_{i,g}^{(j)}=\begin{cases}v\_{i,g}^{(j)},&\text{if }\mathrm{rand}\_{j}(0,1)\leq C\_{R}\text{ or }j=j\_{\mathrm{rand}},\\[5.69054pt] x\_{i,g}^{(j)},&\text{otherwise},\end{cases}\qquad j=1,\ldots,d, |  | (26) |

where CR∈[0,1]C\_{R}\in[0,1] is the crossover probability and jrandj\_{\mathrm{rand}} is a
randomly chosen index ensuring that at least one component originates from the
mutant vector.
Hence, ([26](https://arxiv.org/html/2511.21556v1#A4.E26 "In Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) mixes the information contained in
𝐱i,g\mathbf{x}\_{i,g} and 𝐯i,g\mathbf{v}\_{i,g}, with the parameter CRC\_{R} regulating
the expected proportion of mutated components.

Selection. Selection is then performed to determine whether the trial
vector replaces the target vector in the next generation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱i,g+1={𝐮i,g,if ​f​(𝐮i,g)≤f​(𝐱i,g),𝐱i,g,otherwise.\mathbf{x}\_{i,g+1}=\begin{cases}\mathbf{u}\_{i,g},&\text{if }f(\mathbf{u}\_{i,g})\leq f(\mathbf{x}\_{i,g}),\\[2.84526pt] \mathbf{x}\_{i,g},&\text{otherwise.}\end{cases} |  | (27) |

According to ([27](https://arxiv.org/html/2511.21556v1#A4.E27 "In Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")), the better (or equal) solution survives,
which guarantees that the population’s overall fitness does not deteriorate
over successive generations.
The evolutionary process continues until a stopping criterion is met, such as a
maximum number of generations GmaxG\_{\max}, or when the relative improvement in
the best fitness value falls below a threshold ε>0\varepsilon>0, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |fbest,g−fbest,g−1||fbest,g−1|<ε.\frac{\bigl|f\_{\mathrm{best},g}-f\_{\mathrm{best},g-1}\bigr|}{\bigl|f\_{\mathrm{best},g-1}\bigr|}<\varepsilon. |  | (28) |

Condition ([28](https://arxiv.org/html/2511.21556v1#A4.E28 "In Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) prevents unnecessary iterations once the
algorithm has essentially converged.

To apply the approach to empirical data in our context, the algorithm is used
to solve the nonlinear systems defining the quantities
(mx,px)(m\_{x},p\_{x}) and (m1,m2,p1,p2)(m\_{1},m\_{2},p\_{1},p\_{2}) for the 2-point and 3-point cases,
respectively. In a historical simulation setting, the vector of the SS P&Ls is
interpreted as the empirical distribution of the underlying risk factor.
Each point in the vector is therefore assigned the probability mass

|  |  |  |  |
| --- | --- | --- | --- |
|  | ps=1S,s=1,…,S,p\_{s}=\frac{1}{S},\qquad s=1,\ldots,S, |  | (29) |

with S=250S=250 or S=500S=500 in most of our applications.

Once the P&Ls have been reordered, we denote by PnL​(s)\mathrm{PnL}(s) the
empirical cumulative distribution, which can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(PnL​(s))=sS,s=1,…,S,F\bigl(\mathrm{PnL}(s)\bigr)=\frac{s}{S},\qquad s=1,\ldots,S, |  | (30) |

while for any generic point z∈ℝz\in\mathbb{R} the empirical distribution
function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(z)=#​{s:PnLs≤z}S.F(z)=\frac{\#\{s:\mathrm{PnL}\_{s}\leq z\}}{S}. |  | (31) |

Equations ([29](https://arxiv.org/html/2511.21556v1#A4.E29 "In Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach"))–([31](https://arxiv.org/html/2511.21556v1#A4.E31 "In Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")) provide
the empirical probabilities and cumulative distribution that constitute the
input to the objective function optimized by the DE algorithm in
([23](https://arxiv.org/html/2511.21556v1#A4.E23 "In Appendix D The Differential Evolution (DE) Algorithm ‣ Informative Risk Measures in the Banking Industry: A Proposal based on the Magnitude-Propensity Approach")).

## References

* [Acerbi and Székely, 2017]

  Acerbi, C. and Székely, B. (2017).
  General properties of backstable risk measures.
  Mathematics and Financial Economics, 11(2):181–202.
* [Acerbi and Székely, 2023]

  Acerbi, C. and Székely, B. (2023).
  Backtestability and the ridge backtest.
  Frontiers of Mathematical Finance, 2(4):497–521.
* [Acerbi and Tasche, 2002]

  Acerbi, F. and Tasche, D. (2002).
  On the coherence of expected shortfall.
  Journal of Banking & Finance, 26(7):1487–1503.
* [Ararat and Feinstein, 2024]

  Ararat, C. and Feinstein, Z. (2024).
  Short Communication: On the Separability of Vector-Valued Risk
  Measures.
  SIAM Journal on Financial Mathematics, 15(4).
* [Artzner et al., 1997]

  Artzner, P., Delbaen, F., Eber, J.-M., and Heath, D. (1997).
  Coherent risk measures.
  Mathematical Finance, 7(3):203–228.
* [Aven, 2016]

  Aven, T. (2016).
  Risk assessment and risk management: Review of recent advances
  on their foundation, volume 253.
  European Journal of Operational Research.
* [Barone-Adesi et al., 1999]

  Barone-Adesi, G., Giannopoulos, K., and Vosper, L. (1999).
  VaR without Correlations for Portfolios for Portfolios of Derivative
  Securities.
  Journal of Futures Markets, 19:583–602.
* [Basel Committee of Banking Supervision, 2019]

  Basel Committee of Banking Supervision (2019).
  Minimal capital requirements for market risk.
  Technical Report 457, Bank for International Settlements, available
  at https://www.bis.org/bcbs/publ/d457.pdf.
* [Ben Tahat and Lépinette, 2014]

  Ben Tahat, I. and Lépinette, E. (2014).
  Vector-valued coherent risk measure processes.
  International Journal of Theoretical and Applied Finance,
  17:https://doi.org/10.1142/S0219024914500113.
* [Biglova et al., 2008]

  Biglova, A., Fabozzi, F., Ortobelli, S., Rachev, S., and Stoyanov, S. (2008).
  Desirable properties of an ideal risk measure in portfolio theory.
  International Journal of Theoretical and Applied Finance,
  11(01):19–54.
* [Brealey et al., 2019]

  Brealey, R., Myers, S., and Allen, F. (2019).
  Principles of Corporate Finance.
  Mc-Graw GHill Series in Finance.
* [Chernozhukov and Hong, 2004]

  Chernozhukov, V. and Hong, H. (2004).
  An MCMC approach to classical estimation.
  Journal of Econometrics, 115(2):293–346.
* [Cuturi, 2013]

  Cuturi, M. (2013).
  Sinkhorn Distances: Lightspeed Computation of Optimal Transport.
  In Advances in Neural Information Processing Systems (NIPS),
  pages 2292–2300.
* [Daníelsson et al., 2016]

  Daníelsson, J., James, K., Valenzuela, M., and Zer, I. (2016).
  Model risk of risk models.
  Journal of Financial Stability, 23(C):79–91.
* [David and Nagaraja, 2004]

  David, H. and Nagaraja, H. (2004).
  Order statistics.
  Wiley.
* [EIOPA, 2024]

  EIOPA (2024).
  Ye2022 comparative study on market and credit risk modeling.
  Technical Report EBA/GL/2012/3, EIOPA, available at
  https://www.eiopa.europa.eu/browse/supervisory-convergence/internal-models/market-and-credit-risk-comparative-study-ye2022en.
* [EIOPA, 2025]

  EIOPA (2025).
  Peer review on the supervision of stochastic valuation nder solvency
  ii.
  Technical report, EIOPA/Bos/25/066, available at
  https://www.eiopa.europa.eu.
* [Embrechts et al., 2015a]

  Embrechts, P., Frey, R., and A., M. (2015a).
  Quantitative Risk Management: Concepts, Techniques and Tools.
  Princeton Series in Finance.
* [Embrechts et al., 2015b]

  Embrechts, P., Frey, R., and McNeil, A. (2015b).
  Quantitative Risk Management: Concepts, Techniques, and Tools.
  Princeton University Press.
* [European Banking Authority, 2012]

  European Banking Authority (2012).
  Guidelines on the incremental default and migration risk charge.
  Technical Report EBA/GL/2012/3, European Banking Authority, available
  at https://www.eba.europa.eu.
* [European Central Bank, 2021]

  European Central Bank (2021).
  Targeted review of internal models.
  Technical report, European Central Bank, available at
  https://www.bankingsupervision.europa.eu.
* [European Commission, 2015]

  European Commission (2015).
  Solvency ii delegated regulation eu/2015/35.
  Technical Report 2015/35, European Commission, available at
  https://eur-lex.europa.eu.
* [Faugeras and Pagès, 2024]

  Faugeras, O. and Pagès, G. (2024).
  Risk quantization by magnitude and propensity.
  Insurance Mathematics and Economics, 116:134–147.
* [Feinstein and Rudloff, 2015]

  Feinstein, Z. and Rudloff, B. (2015).
  A comparison of techniques for dynamic multivariate risk measures.
  in Set Optimization and Applications - the State of the Art.
  From Set Relations to Set-Valued Risk Measures, A. H. Hamel, F. Heyde, B.
  Rudloff Löhne, and C. Schrage, eds., Springer Proc. Math. Stat., Springer
  Cham, 151:3–41.
* [Fissler and Ziegel, 2016]

  Fissler, T. and Ziegel, J. F. (2016).
  Higher-order elicitability and Osband’s principle.
  Bernoulli, 22(3):1611–1631.
* [Garman, 1997]

  Garman, M. (1997).
  Taking VaR to Pieces.
  Risk Magazine, 10(10).
* [Gneiting, 2011]

  Gneiting, T. (2011).
  Making and evaluating point forecasts.
  Journal of the American Statistical Association,
  106(494):746–762.
* [Graf and Luschgy, 2000]

  Graf, S. and Luschgy, H. (2000).
  Foundations of Quantization for Probability Distributions.
  Lecture Notes in Mathematics n. 1739, Springer-Verlag.
* [Harrel, 1982]

  Harrel, F.E., D. C. (1982).
  A new distribution-free quantile estimator.
  Biometrika, 69(3):635–640.
* [Hudson and Gregoriou, 2010]

  Hudson, R. and Gregoriou, G. N. (2010).
  Calculating and Comparing Security Returns is Harder than you
  Think.
  Review of Financial Economics, 19(4):163–168.
* [Institute of Operational Risk, 2019]

  Institute of Operational Risk (2019).
  Risk and Control Self Assessment.
  Technical report, Institute of Operational Risk (IOR), available at
  https://www.ior-institute.org/sound-practice-guidance/risk-and-control-self-assessment/.
* [Jouini et al., 2004]

  Jouini, E., Meddeb, M., and Touzi, N. (2004).
  Vector-valued coherent risk measures.
  Finance and Stochastics, 8:531–552.
* [Kantorovich, 1942]

  Kantorovich, L. V. (1942).
  On the transfer of mass.
  Dokl. Akad. Nauk. USSR, 37:227–229.
* [Koenker, 2005]

  Koenker, R. (2005).
  Quantile regression.
  Econometric Society Monographs, vol. 38. Cambridge University Press,
  Cambridge.
* [Kupiec, 1995]

  Kupiec, P. H. (1995).
  Techniques for Verifying the Accuracy of Risk Management Models.
  The Journal of Derivatives, 3(2):73–84.
* [Liu and Pagès, 2020]

  Liu, Y. and Pagès, G. (2020).
  Convergence Rate of Optimal Quantization and Application to the
  Clustering Performance of the Empirical Measure.
  Journal of Machine Learning Research, 21:1–36.
* [Luschgy and Pagès, 2023]

  Luschgy, H. and Pagès, G. (2023).
  Marginal and Functional Quantization of Stochastic Processes.
  Springer.
* [McNeil et al., 2005]

  McNeil, A., Frey, R., and Embrechts, P. (2005).
  Quantitative Risk Management: Concepts, Techniques and Tools.
  Princeton University Press.
* [Pagès et al., 2004]

  Pagès, G., Pham, H., and Printemps, J. (2004).
  Optimal quantization methods and applications to numerical problems
  in finance.
  in Handbook of Computational and Numerical Methods in Finance,
  Springer.
* [Peters and Shevchenko, 2015]

  Peters, G. W. and Shevchenko, P. V. (2015).
  Single Loss Closed-Form Approximations of Risk Measures.
  in Advances in Heavy Tailed Risk Modeling, Wiley, pages
  433–516.
* [Pichler and Shapiro, 2021]

  Pichler, A. and Shapiro, A. (2021).
  Mathematical Foundations of Distributionally Robust Multistage
  Optimization.
  Siam Journal on Optimization, 31(4):3044–3067.
* [Rachev and Rüschendorf, 1998]

  Rachev, S. T. and Rüschendorf, L. (1998).
  Mass Transportation Problems: Volume 1: Theory.
  In: Probability and its applications, Springer-Verlag, New York Inc.
* [Rockafellar and Uryasev, 2002]

  Rockafellar, R. T. and Uryasev, S. (2002).
  Conditional value-at-risk for general loss distributions.
  Journal of Banking & Finance, 26(7):1443–1471.
* [Scholtes, 2012]

  Scholtes, S. (2012).
  Introduction to piecewise differentiable equations.
  Springer-Briefs in Optimization, New York.
* [Sinkhorn, 1964]

  Sinkhorn, R. (1964).
  A relationship between arbitrary positive matrices and doubly
  stochastic matrices.
  Annals of Mathematical Statistics, 35(2):876–879.
* [Sinkhorn and Knopp, 1967]

  Sinkhorn, R. and Knopp, P. (1967).
  Concerning nonnegative matrices and doubly stochastic matrices.
  Pacific Journal of Mathematics, 21(2):343–348.
* [Storn and Price, 1997]

  Storn, R. and Price, K. (1997).
  Differential Evolution – A Simple and Efficient Heuristic for
  global Optimization over Continuous Spaces.
  Journal of Global Optimization, 11:341–359.
* [Tasche, 2002]

  Tasche, D. (2002).
  Expected shortfall and beyond.
  Journal of Banking and Finance, 26:1519–1533.
* [Tasche, 2004]

  Tasche, D. (2004).
  Capital Allocation with CreditRisk+.
  In: "Credit Risk+ in the Banking Industry", M. Gundlach and F.
  Lehrbass (Eds.), Springer Finance, pages 25–43.
* [Turnbull and Wakeman, 1991]

  Turnbull, S. and Wakeman, L. (1991).
  A quick algorithm for pricing European average options.
  Journal of Financial and Quantitative Analysis, 26:377–389.
* [Villani, 2009]

  Villani, C. (2009).
  Optimal transport: Old and new.
  In: Old and New. In: Grundlehren der Mathematischen Wissenschaften
  (Fundamental Principles of Mathematical Sciences), vol.338. Springer-Verlag,
  Berlin.