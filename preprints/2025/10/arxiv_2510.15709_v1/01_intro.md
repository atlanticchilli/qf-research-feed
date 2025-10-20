---
authors:
- Shunzhi Pang
doc_id: arxiv:2510.15709v1
family_id: arxiv:2510.15709
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Robust Insurance Pricing and Liquidity Management
url_abs: http://arxiv.org/abs/2510.15709v1
url_html: https://arxiv.org/html/2510.15709v1
venue: arXiv q-fin
version: 1
year: 2025
---


Shunzhi Pang
 School of Economics and Management, Tsinghua University; Faculty of Economics and Business, Katholieke Universiteit Leuven; Email: psz22@mails.tsinghua.edu.cn

(October 17, 2025)

###### Abstract

With the rise of emerging risks, model uncertainty poses a fundamental challenge in the insurance industry, making robust pricing a first-order question. This paper investigates how insurers’ robustness preferences shape competitive equilibrium in a dynamic insurance market. Insurers optimize their underwriting and liquidity management strategies to maximize shareholder value, leading to equilibrium outcomes that can be analytically derived and numerically solved. Compared to a benchmark without model uncertainty, robust insurance pricing results in significantly higher premiums and equity valuations. Notably, our model yields three novel insights: (1) The minimum, maximum, and admissible range of aggregate capacity all expand, indicating that insurers’ liquidity management becomes more conservative. (2) The expected length of the underwriting cycle increases substantially, far exceeding the range commonly reported in earlier empirical studies. (3) While the capacity process remains ergodic in the long run, the stationary density becomes more concentrated in low-capacity states, implying that liquidity-constrained insurers require longer to recover. Together, these findings provide a potential explanation for recent skepticism regarding the empirical evidence of underwriting cycles, suggesting that such cycles may indeed exist but are considerably longer than previously assumed.

  

Keywords: Model uncertainty; Equilibrium insurance pricing; Liquidity management; Underwriting cycles; Ergodicity

## 1 Introduction

Model uncertainty, also known as ambiguity, is a salient feature of the insurance industry (Knight,, [1921](https://arxiv.org/html/2510.15709v1#bib.bib39); Ellsberg,, [1961](https://arxiv.org/html/2510.15709v1#bib.bib22); Hogarth and Kunreuther,, [1989](https://arxiv.org/html/2510.15709v1#bib.bib34)). While risk pertains to stochastic events with known probability distributions, ambiguity arises when probability distributions are unknown, often referred to as “unknown unknowns.” In principle, insurers rely on statistical modeling and actuarial fairness principles to price insurance products. However, for catastrophic risks (e.g., earthquakes, hurricanes, and floods) or emerging risks (e.g., climate and cyber risks), the low frequency of events and the proprietary nature of data pose significant challenges to the accumulation of sufficient data for statistical modeling. Another defining characteristic of risks subject to model uncertainty is their propensity to generate correlated losses, thereby undermining the effectiveness of diversification through the law of large numbers (Hogarth and Kunreuther,, [1992](https://arxiv.org/html/2510.15709v1#bib.bib35)). For instance, hurricanes can cause widespread property destruction within a region, while a cyber-attack on cloud computing services may simultaneously disrupt multiple firms relying on the same infrastructure.

In practice, underwriting risks subject to model uncertainty often leads to substantial financial losses for insurers, prompting them to withdraw from offering coverage in subsequent periods (Kunreuther et al.,, [1993](https://arxiv.org/html/2510.15709v1#bib.bib43)). A recent notable example is the COVID-19 insurance policies sold by major Chinese property and casualty insurers in 2021-2022. These policies, which provided one-year coverage and included a payout of 20,000 RMB upon a confirmed COVID-19 diagnosis, were priced at merely 69 RMB. However, the unexpected surge in infections at the end of 2022 triggered an overwhelming volume of claims, resulting in severe financial distress for insurers, with some even refusing to honor payouts. This underscores the critical challenge insurers encounter in practice. To mitigate market failures, a rigorous theoretical framework is required to guide insurers in developing robust pricing and underwriting strategies.

Building on recent advances that integrate decision-making under ambiguity aversion with robust control theory (Hansen and Sargent,, [2001](https://arxiv.org/html/2510.15709v1#bib.bib28), [2008](https://arxiv.org/html/2510.15709v1#bib.bib29)), this study examines how insurers’ robustness preferences shape the competitive equilibrium of the insurance market, particularly in contrast to the benchmark case without model uncertainty. We adopt the continuous-time framework developed by Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) to model a competitive insurance market subject to financial frictions. Unlike the classical actuarial approach, where insurance premiums are exogenously determined by a safety loading factor or a predefined function of losses, this framework endogenizes the loading through the market-clearing condition, leading to dynamic fluctuations in insurance prices. This feature better captures the underwriting cycles observed in practice (Cummins and Outreville,, [1987](https://arxiv.org/html/2510.15709v1#bib.bib15); Lamm-Tennant and Weiss,, [1997](https://arxiv.org/html/2510.15709v1#bib.bib45); Chen et al.,, [1999](https://arxiv.org/html/2510.15709v1#bib.bib11); Harrington and Yu,, [2003](https://arxiv.org/html/2510.15709v1#bib.bib31)).

In the benchmark setting, each insurer decides its underwriting, dividend payout, and refinancing strategies to maximize expected shareholder value under the physical probability measure. However, when accounting for model uncertainty, insurers acknowledge the existence of alternative models and incorporate distorted probability measures into their decision-making process. This transforms the optimization problem into a robust control framework, where the underwriting scale, liquidity management policy, and the worst-case measure are jointly determined. The entropy cost associated with model uncertainty follows the specification in Maenhout et al., ([2020](https://arxiv.org/html/2510.15709v1#bib.bib53)) and Ling et al., ([2021](https://arxiv.org/html/2510.15709v1#bib.bib48)), providing a structured trade-off between maximizing firm value and ensuring robustness.

As insurers in our setting are assumed to be homogeneous differing only in initial capital endowments, their optimal underwriting and liquidity management strategies are likewise homogeneous in equilibrium. The industry dynamics are thus governed by the aggregate liquid reserves, which follow a barrier-type structure. When reserves reach a sufficiently high level, insurers distribute dividends to shareholders until capacity falls back below the payout boundary. Conversely, when reserves drop below a specified threshold, insurers raise external capital to restore reserves at least up to that boundary. Between these two boundaries lies the internal financing region, where both the insurance price and the market-to-book ratio are endogenously determined as functions of aggregate capacity. These quantities are jointly characterized by a system of ordinary differential equations derived from the Hamilton-Jacobi-Bellman-Isaacs (HJBI) framework.

The equilibrium outcomes are obtained numerically under reasonable parameter specifications. For any given capacity level, robust pricing leads to substantially higher premiums than the benchmark without model uncertainty, which in turn leads to a notable reduction in underwriting volume. This result is consistent with early survey-based empirical evidence (Kunreuther et al.,, [1995](https://arxiv.org/html/2510.15709v1#bib.bib44); Cabantous,, [2007](https://arxiv.org/html/2510.15709v1#bib.bib8); Cabantous et al.,, [2011](https://arxiv.org/html/2510.15709v1#bib.bib9)) and corroborates more recent theoretical predictions by Dietz and Walker, ([2019](https://arxiv.org/html/2510.15709v1#bib.bib19)) and Dietz and Niehörster, ([2021](https://arxiv.org/html/2510.15709v1#bib.bib18)). Quantitatively, we find that the premium per unit of risk rises by approximately 4.2%-5.6%. Furthermore, a higher ambiguity aversion coefficient (or equivalently, a lower level of trust in the physical model), and a higher external financing cost (i.e., the cost of capital in the insurance sector) both contribute to further elevating the equilibrium price. Relative to the benchmark, the market-to-book ratio of insurers in the robust equilibrium is also significantly higher at the same capacity level. This indicates that insurers demand a higher valuation of equity as compensation for bearing the risk of model misspecification. Put differently, robustness concerns effectively raise the shadow cost of capital.

Compared with the discrete-time framework, the main advantage of our continuous-time setting is that it allows us to analyze the impact of model uncertainty on the insurance sector from an evolutionary perspective. We highlight several novel predictions that emerge from our results. First, in the presence of model uncertainty, the minimum, maximum, and admissible range of aggregate capacity all expand. The refinancing boundary is no longer zero but strictly positive, indicating that insurers must maintain higher precautionary reserves. Also, the higher payout boundary and wider capacity range imply that dividend distributions are delayed and that the market can sustain a greater accumulation of liquid reserves. Together, these features highlight that insurers’ liquidity management becomes more conservative and cautious when model uncertainty is considered.

Second, while the insurance capacity and pricing dynamics in the robust equilibrium still exhibit cyclical patterns, the expected length of the underwriting cycle increases markedly. Specifically, both the soft market phase (i.e., capacity rising from the lower to the upper boundary, with falling prices and rising volumes) and the hard market phase (i.e., capacity declining from the upper to the lower boundary, with rising prices and shrinking volumes) are prolonged. In our benchmark versus robust equilibrium comparison, the expected soft market duration increases from 4.78 to 14.05 years, while the hard market duration rises from 4.84 to 11.92 years, leading the total cycle length to expand from 9.62 to 25.97 years. Both stronger ambiguity aversion and greater financial frictions would further extend the cycle length. Such long durations far exceed the commonly reported 6-10 year range in earlier empirical studies (Harrington et al.,, [2013](https://arxiv.org/html/2510.15709v1#bib.bib30)), and may help rationalize the recent findings by Boyer et al., ([2012](https://arxiv.org/html/2510.15709v1#bib.bib5)) and Boyer and Owadally, ([2015](https://arxiv.org/html/2510.15709v1#bib.bib6)) that statistical evidence of underwriting cycles in historical data is weak and fragile. If cycles are indeed much longer than previously assumed, then short data samples would fail to contain enough realizations to deliver robust statistical inference. Moreover, introducing model uncertainty renders the cycle more asymmetric. Under plausible parameterizations, the soft market persists substantially longer than the hard market, consistent with the empirical stylized fact emphasized by Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)).

Third, we find that the capacity process is ergodic, converging to a stationary distribution in the long run. Relative to the benchmark case without model uncertainty, the stationary density shifts upward at low capacity levels and downward at high capacity levels. As ambiguity aversion strengthens, the distribution becomes increasingly concentrated near the lower boundary, indicating that insurers are more likely to remain in low-capacity states under stronger robustness concerns. Such result also offers a structural explanation for the empirical difficulty of forecasting underwriting performance documented by Boyer et al., ([2012](https://arxiv.org/html/2510.15709v1#bib.bib5)). If the stationary distribution itself is skewed toward low-capacity states and recovery from adverse shocks is slow, then short-term predictability of underwriting ratios, as tested in their out-of-sample forecasting exercises, will necessarily be limited. In other words, prolonged persistence in depressed states implies that cycles exist in theory, but manifest only weakly in finite historical samples.

Our paper contributes to several strands of literature. First, it builds on the expanding body of research on model uncertainty in decision-making, particularly in the context of insurance and actuarial science. While much of the recent literature has focused on the implications of ambiguity for insurers’ investment and reinsurance decisions (Yi et al.,, [2013](https://arxiv.org/html/2510.15709v1#bib.bib62); Zeng et al.,, [2016](https://arxiv.org/html/2510.15709v1#bib.bib63); Guan and Liang,, [2019](https://arxiv.org/html/2510.15709v1#bib.bib27); Li and Young,, [2019](https://arxiv.org/html/2510.15709v1#bib.bib47); Cheng et al.,, [2024](https://arxiv.org/html/2510.15709v1#bib.bib12)), relatively few studies have examined its impact on insurance pricing and market equilibrium, despite its first-order importance. Several studies have established theoretical frameworks for robust insurance pricing. For instance, Zhao and Zhu, ([2011](https://arxiv.org/html/2510.15709v1#bib.bib64)), Pichler, ([2014](https://arxiv.org/html/2510.15709v1#bib.bib56)), and Dietz and Walker, ([2019](https://arxiv.org/html/2510.15709v1#bib.bib19)) propose different criteria for pricing under ambiguity; however, they do not incorporate demand-side dynamics or market-clearing conditions. Anwar and Zheng, ([2012](https://arxiv.org/html/2510.15709v1#bib.bib2)) analyze the effects of ambiguity on buyer and seller behavior in competitive markets, yet their model remains static and does not capture the dynamic evolution of insurance prices and underwriting cycles. Our study extends this literature by embedding robust pricing into a dynamic market equilibrium framework, offering new insights into its practical applications.

Second, we contribute to the growing literature on the financial economics of insurance, which emphasizes the role of insurers as financial intermediaries in capital markets and calls for a supply-side theory of insurance (Koijen and Yogo,, [2023](https://arxiv.org/html/2510.15709v1#bib.bib42)). While existing studies have demonstrated that financial frictions, product market power, and statutory reserve regulations impose shadow costs on insurance prices (Koijen and Yogo,, [2015](https://arxiv.org/html/2510.15709v1#bib.bib40), [2022](https://arxiv.org/html/2510.15709v1#bib.bib41); Ge,, [2022](https://arxiv.org/html/2510.15709v1#bib.bib24)), we identify an additional factor: insurers’ ambiguity aversion stemming from limited knowledge of risk.

Third, we contribute to the well-established literature on explanations for insurance underwriting cycles, including capacity constraints ([Gron, 1994a,](https://arxiv.org/html/2510.15709v1#bib.bib25) ; [Gron, 1994b,](https://arxiv.org/html/2510.15709v1#bib.bib26) ), reporting and regulatory lags (Cummins and Outreville,, [1987](https://arxiv.org/html/2510.15709v1#bib.bib15); Eckles et al.,, [2016](https://arxiv.org/html/2510.15709v1#bib.bib20)), and information asymmetry (Dicks and Garven,, [2022](https://arxiv.org/html/2510.15709v1#bib.bib17)). The cycle generated in our model belongs to the first category, namely capacity-driven fluctuations, but its duration is much longer than previous theoretical and empirical estimations. This provides a potential explanation for the ongoing debate on the actual existence of underwriting cycles (Boyer et al.,, [2012](https://arxiv.org/html/2510.15709v1#bib.bib5); Boyer and Owadally,, [2015](https://arxiv.org/html/2510.15709v1#bib.bib6)): cycles may indeed exist, but are stretched significantly by robustness concerns and financial frictions. As a result, within a conventional 30-40 year data window, fewer than two complete cycles may be observed, making statistical identification extremely difficult. Hence, rather than relying on short-term cycle predictions, we advocate that insurers adopt robust pricing strategies to mitigate the risk of underwriting losses.

Last, our work connects to the classical literature on liquidity management in financial intermediation. While insurers can raise debt financing at relatively low costs through policyholder reserves, equity remains expensive, similar to other financial intermediaries (Brunnermeier and Pedersen,, [2009](https://arxiv.org/html/2510.15709v1#bib.bib7); He and Krishnamurthy,, [2013](https://arxiv.org/html/2510.15709v1#bib.bib32)). Accumulated equity capital plays a critical role in shaping insurers’ behavior (Winter,, [1994](https://arxiv.org/html/2510.15709v1#bib.bib60); Henriet et al.,, [2016](https://arxiv.org/html/2510.15709v1#bib.bib33); Luciano and Rochet,, [2022](https://arxiv.org/html/2510.15709v1#bib.bib50)). However, unlike banks or funds, insurers are exposed not only to financial risks but also to physical risks. The occurrence of an extreme physical loss can substantially reduce insurers’ liquid assets and may even force them to fire-sell long-term investments, thereby heightening the risk of systemic spillovers to financial markets. In the post-pandemic era, we highlight the importance for financial intermediaries to incorporate model uncertainty into their risk and liquidity management frameworks.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.15709v1#S2 "2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management") introduces model uncertainty and defines the market equilibrium. Section [3](https://arxiv.org/html/2510.15709v1#S3 "3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management") presents insurers’ optimization problem and derives the theoretical results. Section [4](https://arxiv.org/html/2510.15709v1#S4 "4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management") provides a numerical analysis of equilibrium outcomes and compares the cases with and without model uncertainty. Section [5](https://arxiv.org/html/2510.15709v1#S5 "5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management") examines insurers’ long-run behavior, focusing on the duration of underwriting cycles and the ergodic property of capacity dynamics. Finally, Section [6](https://arxiv.org/html/2510.15709v1#S6 "6 Conclusion ‣ Robust Insurance Pricing and Liquidity Management") concludes the paper.

## 2 General Model and Problem Formulation

In this section, we build upon the theoretical framework of Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) and extend it to incorporate insurers’ concerns about model uncertainty, following the formulation of Hansen and Sargent, ([2001](https://arxiv.org/html/2510.15709v1#bib.bib28)) and Anderson et al., ([2003](https://arxiv.org/html/2510.15709v1#bib.bib1)). As we shall demonstrate, accounting for model uncertainty introduces additional complexity into the equilibrium analysis, ultimately shaping both insurers’ underwriting strategies and the equilibrium pricing of insurance.

Let (Ω,ℱ,{ℱt}t≥0,ℙ)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{t\geq 0},\mathbb{P}) be a complete probability space satisfying the usual conditions. All stochastic processes governing the insurance market in the subsequent discussion are assumed to be well-defined on this space.

### 2.1 Insurance Market

We consider a competitive insurance market consisting of a continuum of insurers, each providing coverage to individuals exposed to perfectly correlated risks. Idiosyncratic risks at the individual level are disregarded, as they can be fully diversified in a large population and thus have no impact on aggregate outcomes.111This setting aligns with the feature of risks subject to model uncertainty, their tendency to generate correlated losses, as discussed in the introduction. However, we acknowledge that studying a market with partially correlated risks is a meaningful extension.  The cumulative loss process for a representative insurer, denoted by L≜{Lt:t≥0}L\triangleq\{L\_{t}:t\geq 0\}, evolves as the following dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Lt=l​d​t+η​d​Bt,\mathrm{d}L\_{t}=l\mathrm{d}t+\eta\mathrm{d}B\_{t}, |  | (2.1) |

where l>0l>0 represents the expected instantaneous loss rate, η>0\eta>0 measures the insurer’s exposure to systematic loss risk, and B≜{Bt:t≥0}B\triangleq\{B\_{t}:t\geq 0\} is a one-dimensional standard Brownian motion.

Unlike traditional insurance markets, where insurers rely on extensive underwriting experience and historical data, the risks considered here belong to the category of “unknown unknowns”, where insurers possess limited data to form reliable probabilistic beliefs. Such risks are prevalent in practice, including catastrophic events (Jaffee and Russell,, [1997](https://arxiv.org/html/2510.15709v1#bib.bib36)), large-scale pandemics (Fan et al.,, [2017](https://arxiv.org/html/2510.15709v1#bib.bib23)), and emerging cyber threats (Eling and Schnell,, [2016](https://arxiv.org/html/2510.15709v1#bib.bib21)), where historical data are insufficient for precise risk assessment. Given their strong interdependencies, it is natural to model these them as systematic risks subject to model uncertainty.

Insurance contracts are assumed to be short-term. That is, for a continuously evolving risk process, each policy expires within an infinitesimal time interval, allowing both the insuree and the insurer to dynamically adjust their risk exposure. Such setting has been widely adopted in the literature on dynamic insurance markets (e.g., Henriet et al.,, [2016](https://arxiv.org/html/2510.15709v1#bib.bib33); Luciano and Rochet,, [2022](https://arxiv.org/html/2510.15709v1#bib.bib50)), and is particularly suitable for analyzing property and casualty (P&C) insurance markets, where contracts are typically of short maturity and insurers do not accumulate long-term liabilities. Assume the insurance premium per unit of time is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt​d​t=(l+η​pt)​d​t,\pi\_{t}\mathrm{d}t=(l+\eta p\_{t})\mathrm{d}t, |  | (2.2) |

which consists of two components: the actuarially fair premium ll, and a loading premium, determined by the risk exposure η\eta and a loading factor ptp\_{t}. The loading factor ptp\_{t} is endogenously determined through market-clearing between supply and demand. For simplicity, we refer to ptp\_{t} as the price of insurance in what follows.

In the literature, there are different approaches to characterize insurance market demand. Earlier classical studies examine optimal insurance and risk sharing within the framework of expected utility maximization, either in an intertemporal or life-cycle context (e.g., Yaari,, [1965](https://arxiv.org/html/2510.15709v1#bib.bib61); Rothschild and Stiglitz,, [1976](https://arxiv.org/html/2510.15709v1#bib.bib58); Campbell,, [1980](https://arxiv.org/html/2510.15709v1#bib.bib10); Cummins and Mahul,, [2004](https://arxiv.org/html/2510.15709v1#bib.bib14)). More recent contributions incorporate behavioral factors, such as rank-dependent utility, prospect theory, and ambiguity aversion (e.g., Bernard et al.,, [2015](https://arxiv.org/html/2510.15709v1#bib.bib3); Schmidt,, [2016](https://arxiv.org/html/2510.15709v1#bib.bib59); Peter and Ying,, [2020](https://arxiv.org/html/2510.15709v1#bib.bib55)).

In Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)), the market demand is exogenously specified by a continuously differentiable and decreasing function D​(p)D(p), without imposing any more restrictions on its functional form. While such a flexible setting is also feasible within our framework, we instead adopt the approach of Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)) and endogenize the demand function, which has the advantage of yielding a complete general equilibrium model. Specifically, assume that a representative insuree faces the unit loss process ([2.1](https://arxiv.org/html/2510.15709v1#S2.E1 "In 2.1 Insurance Market ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")), and transfers a fraction dtd\_{t} of the risk to the insurer by purchasing insurance at premium πt\pi\_{t}, while retaining the remaining fraction 1−dt1-d\_{t}. Under mean-variance preferences over an interval d​t\mathrm{d}t, the optimal coverage is given by dt∗=1−1α​η​ptd^{\ast}\_{t}=1-\frac{1}{\alpha\eta}p\_{t}, where α>0\alpha>0 denotes the degree of risk aversion.222The detailed derivation can be found in Appendix A of Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)). To simplify the analysis, we do not impose the restriction dt∈[0,1]d\_{t}\in[0,1] at this stage. Hence, the demand function can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(p)=1−1α​η​p.D(p)=1-\tfrac{1}{\alpha\eta}p. |  | (2.3) |

When p=0p=0, this corresponds to full insurance demand. In what follows, we shift our focus to the characterization of the supply side.

Since insurance contracts are assumed to have an infinitesimal duration, insurers bear no long-term liabilities and are therefore not required to hold reserves against them.333This assumption departs from actual practice, as even P&C insurers are typically required to hold additional reserves to meet solvency regulations. Here, we adopt this simplification to enhance analytical tractability. On each insurer’s balance sheet, the cash or liquid reserves on the asset side, denoted by m≜{mt:t≥0}m\triangleq\Big\{m\_{t}:t\geq 0\Big\}, should equal the equity e≜{et:t≥0}e\triangleq\Big\{e\_{t}:t\geq 0\Big\}. Thus, mtm\_{t} simultaneously represents the book value of equity for an insurer and can also be interpreted as the net wealth of the insurer.

Suppose an insurer’s underwriting scale process is given by x≜{xt≥0:t≥0}x\triangleq\Big\{x\_{t}\geq 0:t\geq 0\Big\}. Over an infinitesimal period (t,t+d​t)(t,t+\mathrm{d}t), the insurer collects premium income of xt​πt​d​tx\_{t}\pi\_{t}\mathrm{d}t and incurs claim payouts of xt​d​Ltx\_{t}\mathrm{d}L\_{t}. The difference xt​(πt​d​t−d​Lt)x\_{t}\big(\pi\_{t}\mathrm{d}t-\mathrm{d}L\_{t}\big), represents the underwriting profit, which can either be retained as cash reserves or distributed as dividends. Let δ≜{δt:t≥0}\delta\triangleq\Big\{\delta\_{t}:t\geq 0\Big\} denote the insurer’s cumulative dividend process. The insurer optimally determines the dividend payout d​δt≥0\mathrm{d}\delta\_{t}\geq 0 to distribute to shareholders. Additionally, in the event of financial distress, the insurer can raise external capital to replenish cash reserves. Let i≜{it:t≥0}i\triangleq\Big\{i\_{t}:t\geq 0\Big\} represent the cumulative recapitalization process, where d​it≥0\mathrm{d}i\_{t}\geq 0. Then, the insurer’s net wealth process evolves according to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​mt=xt​(πt​d​t−d​Lt)+d​it−d​δt=xt​η​pt​d​t−xt​η​d​Bt+d​it−d​δt.\mathrm{d}m\_{t}=x\_{t}\big(\pi\_{t}\mathrm{d}t-\mathrm{d}L\_{t}\big)+\mathrm{d}i\_{t}-\mathrm{d}\delta\_{t}=x\_{t}\eta p\_{t}\mathrm{d}t-x\_{t}\eta\mathrm{d}B\_{t}+\mathrm{d}i\_{t}-\mathrm{d}\delta\_{t}. |  | (2.4) |

Due to asymmetric information and managerial incentive problems, the corporate finance literature widely acknowledges that external financing is costly for firms.444There is extensive theoretical and empirical evidence on this topic, see Jensen and Meckling, ([1976](https://arxiv.org/html/2510.15709v1#bib.bib37)), Leland and Pyle, ([1977](https://arxiv.org/html/2510.15709v1#bib.bib46)), Myers and Majluf, ([1984](https://arxiv.org/html/2510.15709v1#bib.bib54)).  The same applies to financial intermediations such as insurers, where regulatory constraints and capital requirements further elevate financing costs (Cummins and Lamm-Tennant,, [1994](https://arxiv.org/html/2510.15709v1#bib.bib13); Cummins and Phillips,, [2005](https://arxiv.org/html/2510.15709v1#bib.bib16)). Let γ>0\gamma>0 denote the per-unit cost of raising external capital, which would be incorporated into the insurer’s financial evaluation. Finally, we assume that all insurers start with a positive liquid reserve level, i.e., m0j>0m^{j}\_{0}>0 for all j∈𝒥j\in\mathcal{J}.555This assumption ensures that, in equilibrium, the liquid reserve level of all insurers will maintain the same sign at any point in time, as will be demonstrated later.

### 2.2 Optimization Objective without Model Uncertainty

Let 𝒥≜[0,1]\mathcal{J}\triangleq[0,1] denote the set of insurers, each indexed by j∈𝒥j\in\mathcal{J}. Given the liquid reserve process of each individual insurer mjm^{j}, the aggregate liquid reserves (capacity) of the entire insurance sector are defined as M≜{Mt=∫𝒥mtj​dj:t≥0}M\triangleq\Big\{M\_{t}=\int\_{\mathcal{J}}m^{j}\_{t}\mathrm{d}j:t\geq 0\Big\}, which follow the process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mt\displaystyle\mathrm{d}M\_{t} | =Xt​η​pt​d​t−Xt​η​d​Bt+d​It−d​Δt\displaystyle=X\_{t}\eta p\_{t}\mathrm{d}t-X\_{t}\eta\mathrm{d}B\_{t}+\mathrm{d}I\_{t}-\mathrm{d}\Delta\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =D​(pt)​η​pt​d​t−D​(pt)​η​d​Bt+d​It−d​Δt,\displaystyle=D(p\_{t})\eta p\_{t}\mathrm{d}t-D(p\_{t})\eta\mathrm{d}B\_{t}+\mathrm{d}I\_{t}-\mathrm{d}\Delta\_{t}, |  | (2.5) |

where Xt=∫𝒥xtj​djX\_{t}=\int\_{\mathcal{J}}x^{j}\_{t}\mathrm{d}j, It=∫𝒥itj​djI\_{t}=\int\_{\mathcal{J}}i^{j}\_{t}\mathrm{d}j and Δt=∫𝒥δtj​dj\Delta\_{t}=\int\_{\mathcal{J}}\delta^{j}\_{t}\mathrm{d}j, represent the aggregate underwriting scale, cumulative recapitalization and dividend payouts, respectively. In equilibrium, the aggregate supply must equal market demand, leading to the market-clearing condition Xt=D​(pt)X\_{t}=D(p\_{t}).

Without considering model uncertainty, Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) solve the Markovian stationary equilibrium, where the price of insurance is a deterministic function of the aggregate level of reserves, i.e., pt=p​(Mt)p\_{t}=p(M\_{t}). Each individual insurer takes the dynamics ([2.5](https://arxiv.org/html/2510.15709v1#S2.E5 "In 2.2 Optimization Objective without Model Uncertainty ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")) and the equilibrium price function p​(M)p(M) as given and optimally chooses its underwriting scale x≥0x\geq 0, recapitalization policy d​i≥0\mathrm{d}i\geq 0, and dividend policy d​δ≥0\mathrm{d}\delta\geq 0 to maximize shareholder value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(m,M)=maxx≥0,d​δ≥0,d​i≥0⁡𝔼​{∫0∞e−r​t​[d​δt−(1+γ)​d​it]},v(m,M)=\max\_{x\geq 0,\mathrm{d}\delta\geq 0,\mathrm{d}i\geq 0}\mathbb{E}\left\{\int\_{0}^{\infty}e^{-rt}\Big[\mathrm{d}\delta\_{t}-(1+\gamma)\mathrm{d}i\_{t}\Big]\right\}, |  | (2.6) |

where r>0r>0 represents the discount factor, such as the risk-free rate.

###### Definition 1.

In the absence of model uncertainty concerns, a stationary Markovian competitive equilibrium consists of an aggregate liquid reserve process MM, a market price of insurance p​(M)p(M), insurance supply functions xj​(M),j∈𝒥x^{j}(M),j\in\mathcal{J}, that are compatible with each insurer’s optimization objective ([2.6](https://arxiv.org/html/2510.15709v1#S2.E6 "In 2.2 Optimization Objective without Model Uncertainty ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")) and the market-clearing condition ∫𝒥xj​(M)​dj=D​(p​(M))\int\_{\mathcal{J}}x^{j}(M)\mathrm{d}j=D(p(M)).

### 2.3 Optimization Objective with Model Uncertainty

Now, we consider the case where insurers are concerned about model uncertainty in the loss process, which is driven by the Brownian motion BB under the physical measure ℙ\mathbb{P}. The insurer acknowledges the possibility of alternative models and considers distorted probability measures that are mutually absolutely continuous with respect to ℙ\mathbb{P} over any finite time interval. To formalize this, let hh be a density generator associated with the loss process, and denote the set of all such generators by ℋ\mathcal{H}. Given h∈ℋh\in\mathcal{H}, we define process ξh≜{ξth:t≥0}\xi^{h}\triangleq\Big\{\xi^{h}\_{t}:t\geq 0\Big\} as follows:

|  |  |  |
| --- | --- | --- |
|  | ξth=exp⁡(−∫0ths​dBs−12​∫0ths2​ds).\xi\_{t}^{h}=\exp\left(-\int\_{0}^{t}h\_{s}\mathrm{d}B\_{s}-\frac{1}{2}\int\_{0}^{t}h\_{s}^{2}\mathrm{d}s\right). |  |

It is assumed that ∫0ths2​ds<∞\int\_{0}^{t}h\_{s}^{2}\mathrm{d}s<\infty for any t>0t>0, ensuring that ξh\xi^{h} is a martingale process.

By Girsanov’s Theorem, there exists a subjective probability measure ℚh\mathbb{Q}^{h} such that d​ℚhd​ℙ∣ℱt=ξth\frac{\mathrm{d}\mathbb{Q}^{h}}{\mathrm{d}\mathbb{P}}\mid\_{\mathcal{F}\_{t}}=\xi\_{t}^{h}. Under this new measure, the process Bh≜{Bth:t≥0}B^{h}\triangleq\Big\{B^{h}\_{t}:t\geq 0\Big\} defined by:

|  |  |  |
| --- | --- | --- |
|  | d​Bth=d​Bt+ht​d​t,\mathrm{d}B\_{t}^{h}=\mathrm{d}B\_{t}+h\_{t}\mathrm{d}t, |  |

is a standard Brownian motion. Correspondingly, the loss process ([2.1](https://arxiv.org/html/2510.15709v1#S2.E1 "In 2.1 Insurance Market ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")) can be rewritten as:

|  |  |  |
| --- | --- | --- |
|  | d​Lt=l​d​t+η​(d​Bth−ht​d​t)=(l−η​ht)​d​t+η​d​Bth.\mathrm{d}L\_{t}=l\mathrm{d}t+\eta\left(\mathrm{d}B^{h}\_{t}-h\_{t}\mathrm{d}t\right)=(l-\eta h\_{t})\mathrm{d}t+\eta\mathrm{d}B\_{t}^{h}. |  |

Similarly, the individual liquid reserve process ([2.4](https://arxiv.org/html/2510.15709v1#S2.E4 "In 2.1 Insurance Market ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")) evolves as:

|  |  |  |
| --- | --- | --- |
|  | d​mt=xt​(πt​d​t−d​Lt)+d​it−d​δt=xt​η​[(pt+ht)​d​t−d​Bth]+d​it−d​δt.\mathrm{d}m\_{t}=x\_{t}\left(\pi\_{t}\mathrm{d}t-\mathrm{d}L\_{t}\right)+\mathrm{d}i\_{t}-\mathrm{d}\delta\_{t}=x\_{t}\eta\left[\left(p\_{t}+h\_{t}\right)\mathrm{d}t-\mathrm{d}B\_{t}^{h}\right]+\mathrm{d}i\_{t}-\mathrm{d}\delta\_{t}. |  |

Here, the actuarially fair premium used for pricing remains ll, as it serves as the benchmark accepted by policyholders who do not exhibit preferences for robustness. Finally, from the insurer’s perspective, the dynamics of aggregate capacity for the entire insurance sector are given by:

|  |  |  |
| --- | --- | --- |
|  | d​Mt=Xt​η​(pt+ht)​d​t−Xt​η​d​Bth+d​It−d​Δt.\mathrm{d}M\_{t}=X\_{t}\eta(p\_{t}+h\_{t})\mathrm{d}t-X\_{t}\eta\mathrm{d}B\_{t}^{h}+\mathrm{d}I\_{t}-\mathrm{d}\Delta\_{t}. |  |

Notice that the density generators chosen by individual insurers do not necessarily have to be consistent across different insurers. But as we focus on an equilibrium where insurers are homogeneous in behavior, we pre-assume and later verify that the optimally chosen hjh^{j} should be the same value.

With model uncertainty, each insurer’s optimization objective deviates from ([2.6](https://arxiv.org/html/2510.15709v1#S2.E6 "In 2.2 Optimization Objective without Model Uncertainty ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")) and is evaluated under the subjective measure ℚh\mathbb{Q}^{h}, incorporating a penalty term to account for robustness against uncertainty aversion. We adopt the variational preferences framework of Anderson et al., ([2003](https://arxiv.org/html/2510.15709v1#bib.bib1)) and [Maccheroni et al., 2006a](https://arxiv.org/html/2510.15709v1#bib.bib51) ; [Maccheroni et al., 2006b](https://arxiv.org/html/2510.15709v1#bib.bib52) , where an insurer’s optimization objective is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | infℚh∈𝒬𝔼ℚh​{∫0∞e−r​t​[d​δt−(1+γ)​d​it]}+𝒦​(ℚh),\inf\_{\mathbb{Q}^{h}\in\mathcal{Q}}\mathbb{E}^{\mathbb{Q}^{h}}\left\{\int\_{0}^{\infty}e^{-rt}\Big[\mathrm{d}\delta\_{t}-(1+\gamma)\mathrm{d}i\_{t}\Big]\right\}+\mathcal{K}(\mathbb{Q}^{h}), |  | (2.7) |

where 𝒬\mathcal{Q} denotes the set of all admissible probability measures ℚh\mathbb{Q}^{h}, and 𝒦​(ℚh)\mathcal{K}(\mathbb{Q}^{h}) is a penalty term that quantifies the entropy cost of model uncertainty, specified as:

|  |  |  |
| --- | --- | --- |
|  | 𝒦​(ℚh)=12​𝔼ℚh​[∫0∞e−r​t​Θt​ht2​dt].\mathcal{K}(\mathbb{Q}^{h})=\frac{1}{2}\mathbb{E}^{\mathbb{Q}^{h}}\left[\int\_{0}^{\infty}e^{-rt}\Theta\_{t}h\_{t}^{2}\mathrm{d}t\right]. |  |

following Maenhout et al., ([2020](https://arxiv.org/html/2510.15709v1#bib.bib53)) and Ling et al., ([2021](https://arxiv.org/html/2510.15709v1#bib.bib48)).666This formulation is equivalent to 𝒦​(ℚh)=𝔼ℙ​[∫0∞e−r​t​Θt​dϕ​(ξthξ0h)]\mathcal{K}(\mathbb{Q}^{h})=\mathbb{E}^{\mathbb{P}}\left[\int\_{0}^{\infty}e^{-rt}\Theta\_{t}\mathrm{d}\phi\left(\frac{\xi^{h}\_{t}}{\xi^{h}\_{0}}\right)\right], where ϕ​(x)≜x​ln⁡x\phi(x)\triangleq x\ln x; see Maenhout et al., ([2020](https://arxiv.org/html/2510.15709v1#bib.bib53)) for technical details.  It represents a discounted, state‐weighted relative entropy between QhQ^{h} and the reference model ℙ\mathbb{P}, with Θt\Theta\_{t} determining the cost of distortion: larger Θt\Theta\_{t} makes deviations more expensive (less ambiguity), while smaller Θt\Theta\_{t} permits stronger worst‐case tilting. The value function is denoted as v​(m,M)v(m,M), jointly determined by two state variables, namely the individual liquid reserves mm and the aggregate capacity MM. We aim to eliminate one of them to simplify the solution to the control problem.

For tractability, we assume that Θt​(mt)=θ​mt\Theta\_{t}(m\_{t})=\theta m\_{t}, where θ>0\theta>0 measures the degree of concern for robustness among all insurers.777Equivalently, 1θ\frac{1}{\theta} represents the degree of ambiguity aversion ([Maccheroni et al., 2006a,](https://arxiv.org/html/2510.15709v1#bib.bib51) ; [Maccheroni et al., 2006b,](https://arxiv.org/html/2510.15709v1#bib.bib52) ). A larger θ\theta implies lower ambiguity aversion among insurers.  This assumption has two implications. First, the entropy cost is proportional to the insurer’s liquid reserves, which is economically intuitive since larger insurers face higher uncertainty-related costs. Second, such specification ensures that the optimization objective ([2.7](https://arxiv.org/html/2510.15709v1#S2.E7 "In 2.3 Optimization Objective with Model Uncertainty ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")) remains homogeneous in (m,x,d​δ,d​i)(m,x,\mathrm{d}\delta,\mathrm{d}i), implying the value function should be also linear in individual insurers’ net wealth.

Based on this, we assume that the value function takes the form v​(m,M)=m​u​(M)v(m,M)=mu(M), where u​(M)u(M) (m≠0m\neq 0) represents the market-to-book value of each insurer, which is identical across the entire insurance sector. It is conceptually equivalent to the insurance analogue of Tobin’s q ratio, as discussed in Winter, ([1994](https://arxiv.org/html/2510.15709v1#bib.bib60)) and Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)).

###### Definition 2.

In the presence of model uncertainty concerns, a stationary Markovian competitive equilibrium consists of an aggregate liquid reserve process MM, a market price of insurance p​(M)p(M), insurance supply functions xj​(M),j∈𝒥x^{j}(M),j\in\mathcal{J}, that are compatible with each insurer’s optimization objective ([2.7](https://arxiv.org/html/2510.15709v1#S2.E7 "In 2.3 Optimization Objective with Model Uncertainty ‣ 2 General Model and Problem Formulation ‣ Robust Insurance Pricing and Liquidity Management")) and the market-clearing condition ∫𝒥xj​(M)​dj=D​(p​(M))\int\_{\mathcal{J}}x^{j}(M)\mathrm{d}j=D(p(M)).

## 3 Equilibrium Solution

In this section, we derive the insurer’s optimal underwriting and liquidity management strategies by solving the robust control problem. We establish the conditions that must be satisfied by the insurance price and market-to-book value. We then analyze the equilibrium properties, emphasizing its key differences from the benchmark case without model uncertainty.

### 3.1 Benchmark Case

For a benchmark comparison, we first recall the market equilibrium without concerns of model uncertainty, as established by Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)). We omit the detailed derivation, and interested readers may refer to their work for further technical details.

###### Proposition 1 (Equilibrium without Model Uncertainty).

In the absence of model uncertainty, suppose that the following system of equations admits a solution for p∗​(M)p^{\ast}(M) and u∗​(M)u^{\ast}(M) on [0,M¯][0,\overline{M}]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {p​(M)=−u′​(M)u​(M)​D​(p​(M))​η,2​r=[u′′​(M)u​(M)−2​(u′​(M)u​(M))2]​D​(p​(M))2​η2,\left\{\begin{aligned} &p(M)=-\frac{u^{\prime}(M)}{u(M)}D(p(M))\eta,\\ &2r=\left[\frac{u^{\prime\prime}(M)}{u(M)}-2{\left(\frac{u^{\prime}(M)}{u(M)}\right)}^{2}\right]D(p(M))^{2}\eta^{2},\end{aligned}\right. |  | (3.1) |

subject to the demand function: D​(p​(M))=1−1α​η​p​(M)D(p(M))=1-\frac{1}{\alpha\eta}p(M), and boundary conditions: u​(0)=1+γu(0)=1+\gamma, u​(M¯)=1u(\overline{M})=1, and u′​(M¯)=0u^{\prime}(\overline{M})=0. Then, there exists a stationary Markovian equilibrium such that:

(1) For M∈(0,M¯)M\in(0,\overline{M}), the market price of insurance is p∗​(M)p^{\ast}(M), and each insurer’s market-to-book value function is u∗​(M)u^{\ast}(M).

(2) For M≥M¯M\geq\overline{M}, insurers distribute dividends to shareholders until the aggregate liquid reserves fall below M¯\overline{M}. For M≤0M\leq 0, insurers raise external capital to restore positive reserves.

###### Proposition 2.

The equilibrium insurance price p∗​(M)p^{\ast}(M) is strictly decreasing in the aggregate capacity MM. The upper bound is given by p∗​(0)p^{\ast}(0), while the lower bound satisfies p∗​(M¯)=0p^{\ast}(\overline{M})=0. Consequently, the equilibrium price remains non-negative for all M∈[0,M¯]M\in[0,\overline{M}], ensuring that insurers’ expected profits from underwriting remain non-negative.

As shown, the aggregate capacity of the insurance industry MM serves as the unique state variable determining both the equilibrium insurance price and the market-to-book ratio. In a dynamic setting, as MM fluctuates, insurance prices exhibit corresponding volatility, leading to underwriting cycles. The insurer’s decision-making problem results in a three-region structure for the state MM: an external financing region (M≤M¯M\leq\underline{M}), an internal financing region (M¯<M<M¯\underline{M}<M<\overline{M}), and a payout region (M≥M¯M\geq\overline{M}). Such barrier-type solution has been widely applied in liquidity management problems; see Rochet and Villeneuve, ([2011](https://arxiv.org/html/2510.15709v1#bib.bib57)) and Bolton et al., ([2011](https://arxiv.org/html/2510.15709v1#bib.bib4)). Next, we extend this solution structure to the case with model uncertainty.

### 3.2 Internal Financing Region

In the presence of model uncertainty concerns, an insurer’s value function v​(m,M)v(m,M) should satisfy the following Hamilton-Jacobi-Bellman-Isaacs (HJBI) equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r​v​(m,M)\displaystyle rv(m,M) | =supx≥0,d​δ≥0,d​i≥0infh∈ℋ{12Θ(m)h2+xη(p+h)vm+D(p)η(p+h)vM+12x2η2vm​m\displaystyle=\sup\_{x\geq 0,\mathrm{d}\delta\geq 0,\mathrm{d}i\geq 0}\inf\_{h\in\mathcal{H}}\bigg\{\frac{1}{2}\Theta(m)h^{2}+x\eta(p+h)v\_{m}+D(p)\eta(p+h)v\_{M}+\frac{1}{2}x^{2}\eta^{2}v\_{mm} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12D(p)2η2vM​M+xD(p)η2vm​M+dδ(1−vm)+di(vm−1−γ)}.\displaystyle+\frac{1}{2}D(p)^{2}\eta^{2}v\_{MM}+xD(p)\eta^{2}v\_{mM}+\mathrm{d}\delta(1-v\_{m})+\mathrm{d}i(v\_{m}-1-\gamma)\bigg\}. |  | (3.2) |

Here, we pre-assume that both v​(⋅,⋅)v(\cdot,\cdot) and u​(⋅)u(\cdot) are smooth functions, with u​(⋅)>0u(\cdot)>0, continuously differentiable up to the second order. Besides, we impose m≥0m\geq 0, it would be unreasonable to assume that the insurer continues underwriting when its liquid reserves are negative. Actually, when considering a barrier-type solution, the insurer is assumed to recapitalize once mm falls below a lower threshold M¯\underline{M}, which is typically non-negative.

We begin by analyzing the internal financing region, where the optimal dividend and recapitalization policies are d​δ∗=0\mathrm{d}\delta^{\ast}=0 and d​i∗=0\mathrm{d}i^{\ast}=0. Hence, the focus reduces to the max-min problem for the remaining controls. For m=0m=0, we have Θ​(m)=0\Theta(m)=0, and the minimization over hh admits an interior solution if and only if x∗=−vMvm​D​(p)x^{\ast}=-\frac{v\_{M}}{v\_{m}}D(p). Given the assumption that v​(m,M)=m​u​(M)v(m,M)=mu(M), it leads to x∗​(0,M)=−m​u′​(M)u​(M)|m=0​D​(p)=0x^{\ast}(0,M)=-\left.\frac{mu^{\prime}(M)}{u(M)}\right|\_{m=0}D(p)=0. Under this condition, the HJBI equation holds trivially, as both sides are equal to zero. This result hints that regardless of the aggregate capacity MM, an individual insurer does not engage in underwriting when it has zero liquid reserves.

For m>0m>0, the minimization over hh is attained at:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h∗=−x​η​vm+D​(p)​η​vMΘ​(m).h^{\ast}=-\frac{x\eta v\_{m}+D(p)\eta v\_{M}}{\Theta(m)}. |  | (3.3) |

Substituting it back into the HJBI equation, the first-order condition with respect to xx is given by:

|  |  |  |
| --- | --- | --- |
|  | ∂h∗∂x​[Θ​(m)​h∗+x​η​vm+D​(p)​η​vM]+η​(p+h∗)​vm+x​η2​vm​m+D​(p)​η2​vm​M=0.\frac{\partial h^{\ast}}{\partial x}\Big[\Theta(m)h^{\ast}+x\eta v\_{m}+D(p)\eta v\_{M}\Big]+\eta(p+h^{\ast})v\_{m}+x\eta^{2}v\_{mm}+D(p)\eta^{2}v\_{mM}=0. |  |

Under the assumption that v​(m,M)=m​u​(M)v(m,M)=mu(M), the candidate underwriting scale:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x∗​(m,M)=m​[θu​(M)​η​(p+u′​(M)u​(M)​D​(p)​η)−u′​(M)u​(M)​D​(p)],x^{\ast}(m,M)=m\left[\frac{\theta}{u(M)\eta}\left(p+\frac{u^{\prime}(M)}{u(M)}D(p)\eta\right)-\frac{u^{\prime}(M)}{u(M)}D(p)\right], |  | (3.4) |

is optimal when it is non-negative. Otherwise, due to the non-negativity constraint, the optimal scale is restricted to x∗​(m,M)=0x^{\ast}(m,M)=0.

We analyze the two cases separately. For some MM such that f​(M)≜θu​(M)​η​(p+u′​(M)u​(M)​D​(p)​η)−u′​(M)u​(M)​D​(p)>0f(M)\triangleq\frac{\theta}{u(M)\eta}\left(p+\frac{u^{\prime}(M)}{u(M)}D(p)\eta\right)-\frac{u^{\prime}(M)}{u(M)}D(p)>0, then x∗​(m,M)>0x^{\ast}(m,M)>0 and the optimal density generator is then given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h∗​(M)=−p​(M)−u′​(M)u​(M)​D​(p​(M))​η.h^{\ast}(M)=-p(M)-\frac{u^{\prime}(M)}{u(M)}D(p(M))\eta. |  | (3.5) |

Substituting ([3.4](https://arxiv.org/html/2510.15709v1#S3.E4 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) and ([3.5](https://arxiv.org/html/2510.15709v1#S3.E5 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) back into the HJBI equation ([3.2](https://arxiv.org/html/2510.15709v1#S3.E2 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​r=θu​(M)​(p​(M)+u′​(M)u​(M)​D​(p​(M))​η)2+[u′′​(M)u​(M)−2​(u′​(M)u​(M))2]​D​(p​(M))2​η2.2r=\frac{\theta}{u(M)}\left(p(M)+\frac{u^{\prime}(M)}{u(M)}D(p(M))\eta\right)^{2}+\left[\frac{u^{\prime\prime}(M)}{u(M)}-2{\left(\frac{u^{\prime}(M)}{u(M)}\right)}^{2}\right]D(p(M))^{2}\eta^{2}. |  | (3.6) |

However, if f​(M)≤0f(M)\leq 0, x∗​(m,M)=0x^{\ast}(m,M)=0 for all m>0m>0. Combined with x∗​(0,M)=0x^{\ast}(0,M)=0 for any MM, the market-clearing condition implies D​(p∗​(M))=0D(p^{\ast}(M))=0. Then, the optimal density generator solved by ([3.3](https://arxiv.org/html/2510.15709v1#S3.E3 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) is h∗​(M)=0h^{\ast}(M)=0. Substituting these values back into the HJBI equation, we have r​v​(m,M)=r​m​u​(M)=0rv(m,M)=rmu(M)=0, which contradicts the assumption that m>0m>0 and u​(M)>0u(M)>0. Thus, this scenario cannot occur. If an equilibrium exists, it must satisfy f​(M)>0f(M)>0 for any MM.

Based on ([3.4](https://arxiv.org/html/2510.15709v1#S3.E4 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) and x∗​(0,M)=0x^{\ast}(0,M)=0 for any MM, the market-clearing condition is equivalent to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(p​(M))=M​[θu​(M)​η​(p​(M)+u′​(M)u​(M)​D​(p​(M))​η)−u′​(M)u​(M)​D​(p​(M))],D(p(M))=M\left[\frac{\theta}{u(M)\eta}\left(p(M)+\frac{u^{\prime}(M)}{u(M)}D(p(M))\eta\right)-\frac{u^{\prime}(M)}{u(M)}D(p(M))\right], |  | (3.7) |

where D​(p​(M))D(p(M)) on the left side equals the sum of x∗​(m,M)x^{\ast}(m,M), and the multiplier MM on the right side is the sum of mm across insurers. Once the specific form of the demand function D​(p)D(p) is specified, we can express the equilibrium price p∗​(M)p^{\ast}(M) as a function of the market-to-book ratio u​(M)u(M) and its first-order derivative u′​(M)u^{\prime}(M), though their exact values have yet to be determined. Replacing the price function into equation ([3.6](https://arxiv.org/html/2510.15709v1#S3.E6 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")), we obtain a second-order ODE for u​(⋅)u(\cdot).

Finally, we note that the optimal underwriting scale derived in ([3.4](https://arxiv.org/html/2510.15709v1#S3.E4 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) remains valid for m=0m=0. This implies that each insurer’s underwriting scale is proportional to its liquid reserve level, aligning with the homogeneity assumption that v​(m,M)=m​u​(M)v(m,M)=mu(M). Furthermore, the optimal density generator ([3.5](https://arxiv.org/html/2510.15709v1#S3.E5 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) depends solely on the aggregate capacity MM, implying that all insurers with positive liquid reserves share the same belief regarding the worst-case scenario.

### 3.3 External Financing and Payout Regions

Next, we analyze the optimal dividend and recapitalization policies. Based on the HJBI equation ([3.2](https://arxiv.org/html/2510.15709v1#S3.E2 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")), the maximization with respect to d​δ\mathrm{d}\delta and d​i\mathrm{d}i is independent of the choice of hh. A necessary condition for the existence of an equilibrium solution is:

|  |  |  |
| --- | --- | --- |
|  | 1−vm≤0,andvm−1−γ≤0,1-v\_{m}\leq 0,\quad\text{and}\quad v\_{m}-1-\gamma\leq 0, |  |

that is 1≤u​(M)≤1+γ1\leq u(M)\leq 1+\gamma. Moreover, d​δ∗>0\mathrm{d}\delta^{\ast}>0 only if u​(M)=1u(M)=1, while d​i∗>0\mathrm{d}i^{\ast}>0 only if u​(M)=1+γu(M)=1+\gamma. In line with the benchmark case without model uncertainty, as well as many related liquidity management problems, we focus on a barrier-type solution. Specifically, M¯\overline{M} and M¯\underline{M} denote the payout boundary and the external financing boundary, respectively. And to ensure the existence of a solution, we impose the following assumption on the market-to-book ratio function.

###### Assumption 1.

For M∈[M¯,M¯]M\in[\underline{M},\overline{M}] with 0≤M¯<M¯0\leq\underline{M}<\overline{M}, it holds that 1≤u​(M)≤1+γ1\leq u(M)\leq 1+\gamma and u′​(M)≤0u^{\prime}(M)\leq 0. In other words, the market-to-book ratio of the insurance sector is assumed to be a decreasing function of aggregate capacity, bounded between its two boundary values.

The monotonicity of u​(⋅)u(\cdot) is essential for ensuring that the optimal policy takes a barrier-type form. Otherwise, the sets {M:u​(M)≤1}\{M:u(M)\leq 1\} and {M:u​(M)≥1+γ}\{M:u(M)\geq 1+\gamma\} could consist of multiple disconnected intervals, leading to multiple thresholds and more complex strategies.

When liquid reserves are relatively high (M≥M¯M\geq\overline{M}), the insurer maximizes shareholder value by distributing excess cash as dividends. At the payout boundary (M=M¯M=\overline{M}), the insurer is indifferent between retaining or distributing one additional dollar, implying u​(M¯)=1u(\overline{M})=1. This ensures that the marginal value of cash equals the marginal cost to shareholders, preventing excessive accumulation of reserves. Conversely, when liquid reserves fall below a critical threshold (M≤M¯M\leq\underline{M}), the insurer optimally raises external funds to restore liquidity. The external financing boundary satisfies u​(M¯)=1+γu(\underline{M})=1+\gamma. It ensures that the marginal value of cash equals the marginal cost of recapitalization, making external financing optimal only when strictly necessary.

Referring to Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) and Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)), we additionally impose a no-arbitrage condition at the boundaries. Let V​(M)=M​u​(M)V(M)=Mu(M) denote the market value of the entire insurance industry. Then, the absence of arbitrage opportunities requires the following smooth-pasting conditions:

|  |  |  |
| --- | --- | --- |
|  | V′​(M¯)=u​(M¯)+M¯​u′​(M¯)=1,\displaystyle V^{\prime}(\overline{M})=u(\overline{M})+\overline{M}u^{\prime}(\overline{M})=1, |  |
|  |  |  |
| --- | --- | --- |
|  | V′​(M¯)=u​(M¯)+M¯​u′​(M¯)=1+γ.\displaystyle V^{\prime}(\underline{M})=u(\underline{M})+\underline{M}u^{\prime}(\underline{M})=1+\gamma. |  |

In words, the marginal change in the aggregate market value induced by a dividend payout or recapitalization must equal the marginal flow of funds withdrawn from or injected into the industry by shareholders. At the upper bound, it derives that u′​(M¯)=0u^{\prime}(\overline{M})=0, as M¯>0\overline{M}>0. At the lower bound, however, it indicates that M¯=0\underline{M}=0 or u′​(M¯)=0u^{\prime}(\underline{M})=0.

The contingent condition M¯=0\underline{M}=0 cannot generally hold in our setting. Suppose M¯=0\underline{M}=0 and there exists a solution (p∗​(M),u∗​(M)),M∈[M¯,M¯]\left(p^{\ast}(M),u^{\ast}(M)\right),\,M\in[\underline{M},\overline{M}], to the market equilibrium. Then, the market-clearing condition ([3.7](https://arxiv.org/html/2510.15709v1#S3.E7 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) implies D​(p∗​(0))=0D(p^{\ast}(0))=0 and p∗​(0)=α​ηp^{\ast}(0)=\alpha\eta. Since equation ([3.6](https://arxiv.org/html/2510.15709v1#S3.E6 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) holds for M>0M>0, it should also hold at M=0M=0, provided that u​(0)≠0u(0)\neq 0 and both p​(⋅)p(\cdot) and u​(⋅)u(\cdot) are sufficiently smooth and bounded in a neighborhood of M=0M=0. Then, substituting M¯=0\underline{M}=0 and D​(p∗​(0))=0D(p^{\ast}(0))=0 into the equation yields:

|  |  |  |
| --- | --- | --- |
|  | 2​r=θ1+γ​α2​η2,2r=\frac{\theta}{1+\gamma}\alpha^{2}\eta^{2}, |  |

which does not generally hold unless specific parameter restrictions are satisfied. Therefore, the alternative condition u′​(M¯)=0,M¯>0u^{\prime}(\underline{M})=0,\ \underline{M}>0, should be satisfied.

###### Remark 1.

Unlike Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) and Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)), where the lower barrier is shown to be zero because the optimally solved u​(⋅)u(\cdot) is convex in the aggregate capacity (hence u′​(M¯)=0u^{\prime}(\underline{M})=0 and u′​(M¯)=0u^{\prime}(\overline{M})=0 cannot occur simultaneously), the incorporation of model uncertainty here leads to a different form of solution, and M¯=0\underline{M}=0 cannot generally hold. In Section [4](https://arxiv.org/html/2510.15709v1#S4 "4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management"), we demonstrate through numerical simulations that the market-to-book ratio can satisfy the value-matching and smooth-pasting boundary conditions, as well as the requirements in Assumption [1](https://arxiv.org/html/2510.15709v1#ThmAssumption1 "Assumption 1. ‣ 3.3 External Financing and Payout Regions ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management").

### 3.4 Market Equilibrium

Combining the solution to the control problem with the determination of the payout and external financing boundaries, we characterize the market equilibrium in the following proposition.

###### Proposition 3 (Equilibrium with Model Uncertainty).

In the presence of model uncertainty, suppose that the following system of equations admits a solution for p∗​(M)p^{\ast}(M) and u∗​(M)u^{\ast}(M) on [M¯,M¯][\underline{M},\overline{M}]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {D​(p​(M))=M​[θu​(M)​η​(p​(M)+u′​(M)u​(M)​D​(p​(M))​η)−u′​(M)u​(M)​D​(p​(M))],2​r=θu​(M)​(p​(M)+u′​(M)u​(M)​D​(p​(M))​η)2+[u′′​(M)u​(M)−2​(u′​(M)u​(M))2]​D​(p​(M))2​η2,\left\{\begin{aligned} &D(p(M))=M\left[\frac{\theta}{u(M)\eta}\left(p(M)+\frac{u^{\prime}(M)}{u(M)}D(p(M))\eta\right)-\frac{u^{\prime}(M)}{u(M)}D(p(M))\right],\\ &2r=\frac{\theta}{u(M)}\left(p(M)+\frac{u^{\prime}(M)}{u(M)}D(p(M))\eta\right)^{2}+\left[\frac{u^{\prime\prime}(M)}{u(M)}-2{\left(\frac{u^{\prime}(M)}{u(M)}\right)}^{2}\right]D(p(M))^{2}\eta^{2},\end{aligned}\right. |  | (3.8) |

subject to demand function: D​(p​(M))=1−1α​η​p​(M)D(p(M))=1-\frac{1}{\alpha\eta}p(M), boundary conditions: u​(M¯)=1+γu(\underline{M})=1+\gamma, u​(M¯)=1u(\overline{M})=1, u′​(M¯)=u′​(M¯)=0u^{\prime}(\underline{M})=u^{\prime}(\overline{M})=0, and the requirements in Assumption [1](https://arxiv.org/html/2510.15709v1#ThmAssumption1 "Assumption 1. ‣ 3.3 External Financing and Payout Regions ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management"). Then, there exists a stationary Markovian equilibrium such that:

(1) For M∈(M¯,M¯)M\in(\underline{M},\overline{M}), the market price of insurance is p∗​(M)p^{\ast}(M), each insurer’s market-to-book value function is u∗​(M)u^{\ast}(M), and the worst-case density generator is h∗​(M)h^{\ast}(M) as given in ([3.5](https://arxiv.org/html/2510.15709v1#S3.E5 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")). For the insurer with reserves mm, its optimal operation amount is x∗​(m,M)x^{\ast}(m,M) as given in ([3.4](https://arxiv.org/html/2510.15709v1#S3.E4 "In 3.2 Internal Financing Region ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) and the shareholders value is v∗​(m,M)=m​u∗​(M)v^{\ast}(m,M)=mu^{\ast}(M).

(2) For M≥M¯M\geq\overline{M}, insurers distribute dividends to shareholders until the aggregate liquid reserves fall below M¯\overline{M}. For M≤M¯M\leq\underline{M}, insurers raise external capital to restore reserves to the level of M¯\underline{M}.

Combining the first equation in ([3.8](https://arxiv.org/html/2510.15709v1#S3.E8 "In Proposition 3 (Equilibrium with Model Uncertainty). ‣ 3.4 Market Equilibrium ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) with the demand function, we have the representation:

|  |  |  |
| --- | --- | --- |
|  | p​(M)=g​(M)M​θu​(M)​η+1α​η​g​(M),whereg​(M)=1−M​u′​(M)u​(M)​(θu​(M)−1).p(M)=\frac{g(M)}{M\frac{\theta}{u(M)\eta}+\frac{1}{\alpha\eta}g(M)},\quad\text{where}\quad g(M)=1-M\frac{u^{\prime}(M)}{u(M)}\left(\frac{\theta}{u(M)}-1\right). |  |

Substituting this into the second equation yields a second-order ODE for u​(⋅)u(\cdot):

|  |  |  |  |
| --- | --- | --- | --- |
|  | u′′​(M)=2​u′2​(M)u​(M)+2​r​u​(M)​(1η+1α​η​u​(M)M​θ​g​(M))2−θ​(g​(M)+u′​(M)u​(M)​M​θu​(M))2.u^{\prime\prime}(M)=\frac{2{u^{\prime}}^{2}(M)}{u(M)}+2ru(M)\left(\frac{1}{\eta}+\frac{1}{\alpha\eta}\frac{u(M)}{M\theta}g(M)\right)^{2}-\theta\left(g(M)+\frac{u^{\prime}(M)}{u(M)}\frac{M\theta}{u(M)}\right)^{2}. |  | (3.9) |

Regarding the boundary conditions, since both M¯\underline{M} and M¯\overline{M} are endogenous and remain to be determined, we apply a change of variables by setting:

|  |  |  |
| --- | --- | --- |
|  | M​(z)=M¯+Δ​M⋅z,whereΔ​M=M¯−M¯,z∈[0,1].M(z)=\underline{M}+\Delta M\cdot z,\quad\text{where}\quad\Delta M=\overline{M}-\underline{M},\quad z\in[0,1]. |  |

Then, we define a set of auxiliary functions:

|  |  |  |
| --- | --- | --- |
|  | y1​(z)=u​(M​(z)),y2​(z)=y1′​(z)=Δ​M⋅u′​(M),y3​(z)=y2′​(z)=Δ​M2⋅u′′​(M),y\_{1}(z)=u(M(z)),\quad y\_{2}(z)=y\_{1}^{\prime}(z)=\Delta M\cdot u^{\prime}(M),\quad y\_{3}(z)=y\_{2}^{\prime}(z)=\Delta M^{2}\cdot u^{\prime\prime}(M), |  |

where u′′​(M)u^{\prime\prime}(M) can be represented by y1y\_{1} and y2y\_{2}, and the boundary conditions are given by:

|  |  |  |
| --- | --- | --- |
|  | y1​(0)=1+γ,y1​(1)=1,y2​(0)=y2​(1)=0.y\_{1}(0)=1+\gamma,\quad y\_{1}(1)=1,\quad y\_{2}(0)=y\_{2}(1)=0. |  |

This change of variables maps the free-boundary problem with unknown M¯\underline{M} and M¯\overline{M} onto a fixed domain z∈[0,1]z\in[0,1], which not only standardizes the boundary conditions but also facilitates numerical implementation by allowing the use of standard boundary value problem solvers.

Regarding the existence and uniqueness of market equilibrium, Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) rigorously proved that it holds for the result in Proposition [1](https://arxiv.org/html/2510.15709v1#ThmProposition1 "Proposition 1 (Equilibrium without Model Uncertainty). ‣ 3.1 Benchmark Case ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management") when there is no concern for model uncertainty. In contrast, for Proposition [3](https://arxiv.org/html/2510.15709v1#ThmProposition3 "Proposition 3 (Equilibrium with Model Uncertainty). ‣ 3.4 Market Equilibrium ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management"), both the structure of the equation and the boundary conditions are altered, which prevents us from providing a rigorous proof of existence and uniqueness.

Nevertheless, our numerical analysis in Section [4](https://arxiv.org/html/2510.15709v1#S4 "4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management") shows that, under standard parameter specifications, the ODE ([3.9](https://arxiv.org/html/2510.15709v1#S3.E9 "In 3.4 Market Equilibrium ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) with the specified boundary conditions indeed admits a solution satisfying Assumption [1](https://arxiv.org/html/2510.15709v1#ThmAssumption1 "Assumption 1. ‣ 3.3 External Financing and Payout Regions ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management"), namely boundedness and monotonicity. Moreover, there exist positive values M¯∗\underline{M}^{\ast} and M¯∗\overline{M}^{\ast} that satisfy the boundary conditions. Given one of the boundaries M¯∗\underline{M}^{\ast} (or M¯∗\overline{M}^{\ast}) fixed, if the ODE ([3.9](https://arxiv.org/html/2510.15709v1#S3.E9 "In 3.4 Market Equilibrium ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) admits a solution satisfying Assumption [1](https://arxiv.org/html/2510.15709v1#ThmAssumption1 "Assumption 1. ‣ 3.3 External Financing and Payout Regions ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management"), then this solution must be unique. The boundedness of u∗​(⋅)u^{\ast}(\cdot) guarantees that the right-hand side of ([3.9](https://arxiv.org/html/2510.15709v1#S3.E9 "In 3.4 Market Equilibrium ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) is locally Lipschitz in (u,u′)(u,u^{\prime}), which ensures uniqueness of the solution.888Establishing uniqueness in the presence of free boundaries would be more challenging, and we do not pursue this direction further, as it is not the main focus of the present paper.

### 3.5 Properties

Next, we discuss some properties of the equilibrium. In the benchmark model of Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)), it can be rigorously proven that u∗⁣′​(M)≤0u^{\ast\prime}(M)\leq 0, implying that the market-to-book ratio of the insurance sector is a monotonically decreasing function of aggregate capacity. This property not only guarantees the existence of a barrier-type equilibrium, but also suggests that insurers’ expected underwriting profits under the physical measure are non-negative; see Proposition [2](https://arxiv.org/html/2510.15709v1#ThmProposition2 "Proposition 2. ‣ 3.1 Benchmark Case ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management").

In Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)), it is further emphasized that the ratio R​(M)≜−u′​(M)u​(M)R(M)\triangleq-\frac{u^{\prime}(M)}{u(M)}, can be interpreted as the coefficient of market (absolute) risk aversion, which governs insurers’ underwriting and investment behavior and gives rise to insurance cycles. Since u∗⁣′​(M)≤0u^{\ast\prime}(M)\leq 0, it follows that R∗​(M)≥0R^{\ast}(M)\geq 0, indicating that insurers behave as if they were risk averse, even though shareholders are risk neutral when discounting future cash flows. In the equilibrium with concerns for model uncertainty, we obtain similar properties.

###### Proposition 4.

In the equilibrium characterized in Proposition [3](https://arxiv.org/html/2510.15709v1#ThmProposition3 "Proposition 3 (Equilibrium with Model Uncertainty). ‣ 3.4 Market Equilibrium ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management"), and under Assumption [1](https://arxiv.org/html/2510.15709v1#ThmAssumption1 "Assumption 1. ‣ 3.3 External Financing and Payout Regions ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management") which ensures u∗⁣′​(M)≤0u^{\ast\prime}(M)\leq 0, insurers behave as if they were risk averse, and their expected underwriting profit at the equilibrium price under the optimally chosen measure ℚh∗\mathbb{Q}^{h^{\ast}} is non-negative.

Under the optimally chosen measure, the expected profit per unit of underwritten insurance is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​(pt∗+ht∗)=−u∗⁣′​(Mt)u∗​(Mt)​D​(p∗​(Mt))​η2=R∗​(Mt)​D​(p∗​(Mt))​η2.\eta(p^{\ast}\_{t}+h^{\ast}\_{t})=-\frac{u^{\ast\prime}(M\_{t})}{u^{\ast}(M\_{t})}D(p^{\ast}(M\_{t}))\eta^{2}=R^{\ast}(M\_{t})D(p^{\ast}(M\_{t}))\eta^{2}. |  | (3.10) |

This expression consists of two components. The term pt∗p^{\ast}\_{t} represents the market price of insurance, while the density generator ht∗h^{\ast}\_{t} captures the market price of model uncertainty (Anderson et al.,, [2003](https://arxiv.org/html/2510.15709v1#bib.bib1)). Their sum, pt∗+ht∗p^{\ast}\_{t}+h^{\ast}\_{t}, therefore reflects the effective market price of underwriting per unit of risk in the presence of model uncertainty. In particular, ht∗h^{\ast}\_{t} can be interpreted as the additional premium required to compensate insurers for the risk of model misspecification, thereby serving as the shadow price of robustness. When ht∗=0h^{\ast}\_{t}=0, the pricing rule of insurance collapses to the benchmark case characterized in Proposition [1](https://arxiv.org/html/2510.15709v1#ThmProposition1 "Proposition 1 (Equilibrium without Model Uncertainty). ‣ 3.1 Benchmark Case ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management").

The expected profit per unit of underwritten risk is non-negative if and only if u∗⁣′​(M)≤0u^{\ast\prime}(M)\leq 0, which is equivalent to insurers behaving as if they were risk averse. Moreover, the ratio of the effective market price to market demand (which also equals total supply), representing the effective profit margin, is proportional to the market risk-aversion level. This implies that insurers with greater market risk aversion require higher profit margins as compensation for bearing market risk.

In Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)), it is further shown that market risk aversion R​(M)R(M) decreases with aggregate capacity, meaning that larger liquid reserves make insurers appear less risk averse. However, this monotonic property does not carry over to the robust equilibrium, since the presence of model uncertainty alters insurers’ effective pricing of risk. In particular, at the boundaries, dividend distributions and external financing dominate underwriting decisions, and the no-arbitrage condition implies that insurers are effectively neutral to incremental risk-taking. We will examine the dynamics of market risk aversion in greater detail in Section [4](https://arxiv.org/html/2510.15709v1#S4 "4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management").

###### Proposition 5.

In the limit as θ→∞\theta\rightarrow\infty, insurers effectively fully trust the physical probability model, thereby eliminating concerns about model uncertainty. Consequently, the system of equations that p∗​(⋅)p^{\ast}(\cdot) and u∗​(⋅)u^{\ast}(\cdot) must satisfy converges to the benchmark case without model uncertainty, although the boundary conditions remain different.

Mathematically, the market-clearing condition leads to:

|  |  |  |
| --- | --- | --- |
|  | Mu∗​(M)​η​(p∗​(M)+u∗⁣′​(M)u∗​(M)​D​(p∗​(M))​η)=1θ​(1+M​u∗⁣′​(M)u∗​(M))​D​(p∗​(M))→θ→∞0,\frac{M}{u^{\ast}(M)\eta}\left(p^{\ast}(M)+\frac{u^{\ast\prime}(M)}{u^{\ast}(M)}D(p^{\ast}(M))\eta\right)=\frac{1}{\theta}\left(1+M\frac{u^{\ast\prime}(M)}{u^{\ast}(M)}\right)D(p^{\ast}(M))\xrightarrow[]{\theta\rightarrow\infty}0, |  |

which implies p∗​(M)+u∗⁣′​(M)u∗​(M)​D​(p∗​(M))​η→0p^{\ast}(M)+\frac{u^{\ast\prime}(M)}{u^{\ast}(M)}D(p^{\ast}(M))\eta\rightarrow 0, if M≥ε>0M\geq\varepsilon>0, where ε\varepsilon is a small fixed constant ensuring that aggregate reserves are strictly positive. This result coincides with the first equation in ([3.1](https://arxiv.org/html/2510.15709v1#S3.E1 "In Proposition 1 (Equilibrium without Model Uncertainty). ‣ 3.1 Benchmark Case ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")) and further implies that the optimal density generator satisfies h∗​(M)→0h^{\ast}(M)\rightarrow 0, indicating that insurers no longer distort probability measures in the limit of vanishing model uncertainty. Similarly, given M≥ε>0M\geq\varepsilon>0, the second equilibrium condition becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​r\displaystyle 2r | =(p∗​(M)+u∗⁣′​(M)u∗​(M)​D​(p∗​(M))​η)​(1M+u∗⁣′​(M)u∗​(M))​D​(p∗​(M))​η\displaystyle=\left(p^{\ast}(M)+\frac{u^{\ast\prime}(M)}{u^{\ast}(M)}D(p^{\ast}(M))\eta\right)\left(\frac{1}{M}+\frac{u^{\ast\prime}(M)}{u^{\ast}(M)}\right)D(p^{\ast}(M))\eta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[u∗⁣′′​(M)u∗​(M)−2​(u∗⁣′​(M)u∗​(M))2]​D​(p∗​(M))2​η2\displaystyle+\left[\frac{u^{\ast\prime\prime}(M)}{u^{\ast}(M)}-2{\left(\frac{u^{\ast\prime}(M)}{u^{\ast}(M)}\right)}^{2}\right]D(p^{\ast}(M))^{2}\eta^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →θ→∞[u∗⁣′′​(M)u∗​(M)−2​(u∗⁣′​(M)u∗​(M))2]​D​(p∗​(M))2​η2,\displaystyle\xrightarrow[]{\theta\rightarrow\infty}\left[\frac{u^{\ast\prime\prime}(M)}{u^{\ast}(M)}-2{\left(\frac{u^{\ast\prime}(M)}{u^{\ast}(M)}\right)}^{2}\right]D(p^{\ast}(M))^{2}\eta^{2}, |  |

which is consistent with the second equation in ([3.1](https://arxiv.org/html/2510.15709v1#S3.E1 "In Proposition 1 (Equilibrium without Model Uncertainty). ‣ 3.1 Benchmark Case ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management")). Therefore, as insurers’ confidence in the physical probability model becomes arbitrarily large, the ODE satisfied by the market-to-book ratio formally converges to the benchmark case without model uncertainty on the domain M≥εM\geq\varepsilon. However, this convergence does not extend to the region near M→0M\rightarrow 0, and the boundary condition at M¯\underline{M} remains different from the benchmark case.

In our numerical analysis, we show that as θ\theta becomes sufficiently large, the solved value of M¯\underline{M} approaches zero, although it does not exactly coincide with the benchmark boundary. Moreover, both the market-to-book ratio and the price function converge closely to their benchmark counterparts, with the corresponding curves almost overlapping.

## 4 Quantitative Analysis

In this section, we conduct numerical simulations to solve the ODE system, characterize the dynamic equilibrium of the insurance market, and visually examine the impact of insurers’ concerns about model uncertainty. To facilitate comparison, we define pb∗p^{\ast}\_{b}, ub∗u^{\ast}\_{b} as the benchmark equilibrium solutions without model uncertainty; and pr∗p^{\ast}\_{r}, ur∗u^{\ast}\_{r} as the equilibrium under robustness.

As the benchmark setting, we specify the parameter values as follows. The risk-free interest rate is set to r=0.04r=0.04, corresponding to a 4% annualized rate, which serves as the discount factor for shareholders’ valuation of future cash flows. Following the estimation of Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)), we set the unit loss to l=1.0l=1.0 and the volatility of unit loss risk to η=0.28\eta=0.28; the cost of external financing is parameterized as γ=0.20\gamma=0.20, interpreted as the expected return on equity financing; the risk aversion coefficient of insurees (general households) is set to α=2.0\alpha=2.0. Finally, referring to Ling et al., ([2021](https://arxiv.org/html/2510.15709v1#bib.bib48)), we adopt θ=2.8\theta=2.8 as the benchmark degree of robustness concern.

In numerical computation, We employ MATLAB’s bvp4c (a fourth-order Lobatto collocation method with adaptive meshing) and treat the free boundaries M¯\underline{M} and M¯\overline{M} as unknown parameters, solving them jointly with the states from a smooth initial guess until convergence.

| Parameter | Symbol | Value |
| --- | --- | --- |
| Risk-free rate | rr | 4% |
| Expectation of loss risk | ll | 1.0 |
| Volatility of loss risk | η\eta | 28% |
| Cost of external financing | γ\gamma | 20% |
| Risk aversion of insuree | α\alpha | 2.0 |
| Robustness parameter | θ\theta | 2.8 |

Table 1: Benchmark Parameter Values.

### 4.1 Comparison of Equilibria with and without Model Uncertainty

The equilibria characterized by Propositions [1](https://arxiv.org/html/2510.15709v1#ThmProposition1 "Proposition 1 (Equilibrium without Model Uncertainty). ‣ 3.1 Benchmark Case ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management") and [3](https://arxiv.org/html/2510.15709v1#ThmProposition3 "Proposition 3 (Equilibrium with Model Uncertainty). ‣ 3.4 Market Equilibrium ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management") can be numerically solved without difficulty. Figure [4.1](https://arxiv.org/html/2510.15709v1#S4.F1 "Figure 4.1 ‣ 4.1 Comparison of Equilibria with and without Model Uncertainty ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management") reports the results for the market-to-book ratio, its first- and second-order derivatives, and the implied market risk aversion R​(M)R(M). The solid blue lines correspond to the case with concerns about model uncertainty, while the dashed purple lines represent the benchmark case without model uncertainty. Several notable features can be observed from the comparison.

![Refer to caption](equilibrium/compare_fig_u.png)

![Refer to caption](equilibrium/compare_fig_uPrime.png)

![Refer to caption](equilibrium/compare_fig_uPP.png)

![Refer to caption](equilibrium/compare_fig_R.png)

Figure 4.1: Equilibrium Market-to-Book Ratio with and without Model Uncertainty.

First, the minimum, maximum, and range of aggregate capacity all expand when accounting for model uncertainty. In the benchmark case, M¯b=0\underline{M}\_{b}=0, M¯b=0.52\overline{M}\_{b}=0.52, and Δ​Mb=0.52\Delta M\_{b}=0.52, whereas in the robust case, M¯r=0.15\underline{M}\_{r}=0.15, M¯r=0.78\overline{M}\_{r}=0.78, and Δ​Mr=0.63\Delta M\_{r}=0.63. The higher lower bound indicates that insurers under model uncertainty must hold larger minimum reserves, reflecting a more conservative stance. The higher upper bound suggests that the market can sustain a greater accumulation of reserves before dividend payouts occur. Consequently, the wider interval between the two barriers reflects more cautious capital management overall: dividend distributions are postponed, while the trigger for external recapitalization is also elevated.

Second, at the same aggregate capacity level, the market-to-book ratio in the robust equilibrium becomes significantly higher. Economically, this reflects that insurers demand a higher valuation of equity, as they require additional compensation for bearing the risk of model misspecification. In other words, robustness concerns raise the shadow cost of capital. While the ratio remains monotonically decreasing, it is no longer convex: the marginal decline in valuation first accelerates and then decelerates, reflecting a change in the curvature of equity valuation.

Third, the implied market risk aversion is no longer decreasing but instead increases initially and then decreases. This non-monotonicity arises because robustness concerns amplify risk perceptions differently across capacity levels. At low reserves, external recapitalization dominates, so effective risk aversion starts from zero. At intermediate reserves, the fear of ambiguous risk is most pronounced, raising insurers’ required compensation. At high reserves, abundant capital buffers mitigate the marginal effect of ambiguity, causing risk attitudes to gradually revert toward neutrality.

![Refer to caption](equilibrium/compare_fig_p.png)

![Refer to caption](equilibrium/compare_fig_D.png)

![Refer to caption](equilibrium/compare_fig_h.png)

![Refer to caption](equilibrium/compare_fig_V.png)

Figure 4.2: Equilibrium Insurance Market with and without Model Uncertainty.

Next, we analyze the differences in insurance market outcomes induced by model uncertainty, as shown in Figure [4.2](https://arxiv.org/html/2510.15709v1#S4.F2 "Figure 4.2 ‣ 4.1 Comparison of Equilibria with and without Model Uncertainty ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management").
Consistent with the intuition that insurers behave more conservatively, the equilibrium price of insurance is significantly higher for the same level of capacity. Quantitatively, the price increases by about 0.15-0.20 units, corresponding to a 4.2%-5.6% rise in the premium per unit of risk. While the equilibrium price remains a decreasing function of aggregate capacity, market demand correspondingly increases, highlighting the role of capital adequacy in insurance pricing. The market price of model uncertainty also rises with capacity and gradually approaches zero, indicating that concerns about model misspecification diminish when reserves are sufficiently abundant. Finally, the aggregate market value is higher under the robust equilibrium, suggesting that robustness concerns, while inducing more conservative behavior at the firm level, enhance the overall value of the insurance sector.

### 4.2 Impact of Robustness Degree

We next study how the degree of concern for robustness affects the equilibrium outcomes. Theoretically, a larger θ\theta corresponds to lower ambiguity aversion, meaning that insurers place greater trust in the reference probability model. Proposition [5](https://arxiv.org/html/2510.15709v1#ThmProposition5 "Proposition 5. ‣ 3.5 Properties ‣ 3 Equilibrium Solution ‣ Robust Insurance Pricing and Liquidity Management") suggests that as θ→∞\theta\to\infty, the ODE system solved by pr∗​(⋅)p\_{r}^{\ast}(\cdot) and ur∗​(⋅)u\_{r}^{\ast}(\cdot) converges to that of the benchmark case pb∗​(⋅)p\_{b}^{\ast}(\cdot) and ub∗​(⋅)u\_{b}^{\ast}(\cdot), although the boundary conditions remain different. Figure [4.3](https://arxiv.org/html/2510.15709v1#S4.F3 "Figure 4.3 ‣ 4.2 Impact of Robustness Degree ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management") illustrates this convergence by plotting the equilibrium market-to-book ratio and the market price of insurance for values of θ\theta ranging from 0.50.5 to 500500.
When θ=500\theta=500, the equilibrium curves (solid red curves) almost coincide with those of the benchmark case (purple dashed curves), confirming the limiting result. Consistently, the external financing and payout boundaries, M¯r,θ=500=0.0027\underline{M}\_{r,\theta=500}=0.0027 and M¯r,θ=500=0.5356\overline{M}\_{r,\theta=500}=0.5356, are also very close to their benchmark counterparts, M¯b=0\underline{M}\_{b}=0 and M¯b=0.52\overline{M}\_{b}=0.52.

Turning to comparative statics, there seems to be a clear monotonic relationship between the robustness degree and insurance prices.
Given the capacity level, the equilibrium price decreases as θ\theta increases, consistent with the intuition that more ambiguity-averse insurers (smaller θ\theta) require higher premia as compensation for model misspecification.

| Parameter | External Financing Boundary, M¯\underline{M} | Payout Boundary, M¯\overline{M} | Range of Capacity, Δ​M\Delta{M} |
| --- | --- | --- | --- |
| θ=0.5\theta=0.5 | 0.1313 | 0.5783 | 0.4470 |
| θ=2.8\theta=2.8 | 0.1494 | 0.7755 | 0.6261 |
| θ=5\theta=5 | 0.1133 | 0.7371 | 0.6238 |
| θ=50\theta=50 | 0.0222 | 0.5891 | 0.5669 |
| θ=500\theta=500 | 0.0027 | 0.5356 | 0.5329 |
| γ=0.06\gamma=0.06 | 0.2147 | 0.6609 | 0.4462 |
| γ=0.1\gamma=0.1 | 0.1876 | 0.7060 | 0.5184 |
| γ=0.2\gamma=0.2 | 0.1494 | 0.7755 | 0.6261 |
| γ=0.3\gamma=0.3 | 0.1273 | 0.8188 | 0.6915 |
| γ=0.4\gamma=0.4 | 0.1120 | 0.8493 | 0.7373 |

Table 2: Numerically Solved Boundary Values.

In contrast, no such monotonicity holds for the market-to-book ratio. For instance, the curve with θ=0.5\theta=0.5 lies between other curves, indicating that at the same capacity level, the market-to-book ratio first increases and then decreases with θ\theta. A similar non-monotonic pattern also emerges for the external financing and payout boundaries. As summarized in Table [2](https://arxiv.org/html/2510.15709v1#S4.T2 "Table 2 ‣ 4.2 Impact of Robustness Degree ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management"), both boundaries and the resulting range of admissible capacity first expand with θ\theta and then contract, suggesting that robustness concerns affect liquidity management in a non-linear fashion. Nevertheless, they remain consistently above the benchmark case, confirming the robustness of our analysis in Subsection [4.1](https://arxiv.org/html/2510.15709v1#S4.SS1 "4.1 Comparison of Equilibria with and without Model Uncertainty ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management").

![Refer to caption](equilibrium/compare_u_multi_theta_with_benchmark.png)

![Refer to caption](equilibrium/compare_p_multi_theta_with_benchmark.png)

Figure 4.3: Equilibrium Outcomes for Different Robustness Degree θ\theta.

### 4.3 Impact of Financing Cost

Further, we examine the impact of external financing cost γ\gamma on equilibrium outcomes, which reflects the degree of financial friction faced by insurers. It can also be interpreted as the required long-term rate of return demanded by capital providers for investing in the insurance industry.

First, as illustrated in Figure [4.4](https://arxiv.org/html/2510.15709v1#S4.F4 "Figure 4.4 ‣ 4.3 Impact of Financing Cost ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management"), we observe that as the cost γ\gamma rises from 6%6\% to 40%40\%, the equilibrium market price of insurance increases monotonically. This relationship also appears in the benchmark equilibrium of Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) without model uncertainty. Intuitively, when the required return on external capital is higher, or equivalently when the cost of funds is higher, insurers charge higher premia to compensate for the more expensive capital.

Second, the market-to-book ratio also exhibits a monotonic increasing relationship with γ\gamma. Economically, a higher financing cost makes equity capital more valuable, since shareholders demand greater compensation for supplying funds. This raises the valuation of each unit of equity relative to book value, leading to a higher market-to-book ratio.

Third, as reported in Table [2](https://arxiv.org/html/2510.15709v1#S4.T2 "Table 2 ‣ 4.2 Impact of Robustness Degree ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management"), both boundaries and the admissible range of aggregate capacity expand with γ\gamma. A higher financing cost makes external recapitalization more expensive, forcing insurers to maintain larger precautionary reserves (higher lower bound) and to delay dividend payouts (higher upper bound). The wider interval thus reflects more conservative liquidity management. These results also highlight that the amplitude of underwriting cycles is intrinsically linked to the severity of financial frictions in the insurance market.

![Refer to caption](equilibrium/compare_u_multi_gamma.png)

![Refer to caption](equilibrium/compare_p_multi_gamma.png)

Figure 4.4: Equilibrium Outcomes for Different Financing Cost γ\gamma.

## 5 Insurers’ Long-Run Behavior Pattern

In this section, we simulate the insurance market equilibrium in a dynamic setting to gain deeper insights into the long-run behavior of insurers. We continue to rely on the benchmark parameter specifications introduced in Section [4](https://arxiv.org/html/2510.15709v1#S4 "4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management"), together with the corresponding numerical solutions of the equilibrium. We then investigate how variations in key parameters shape the behavior patterns.

### 5.1 Underwriting Dynamics

Under the optimally chosen underwriting and pricing strategies, the aggregate capacity of the insurance sector evolves as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mb,t\displaystyle\mathrm{d}M\_{b,t} | =D​(pb∗​(Mb,t))​η​pb∗​(Mb,t)​d​t−D​(pb∗​(Mb,t))​η​d​Bt\displaystyle=D\!\left(p\_{b}^{\ast}(M\_{b,t})\right)\eta p\_{b}^{\ast}(M\_{b,t})\,\mathrm{d}t-D\!\left(p\_{b}^{\ast}(M\_{b,t})\right)\eta\,\mathrm{d}B\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Rb​(Mb,t)​(D​(pb∗​(Mb,t))​η)2⏟μb​(M)​d​t​−D​(pb∗​(Mb,t))​η⏟σb​(M)​d​Bt,Mb,t∈[0,M¯b],\displaystyle=\underbrace{R\_{b}(M\_{b,t})\Big(D(p\_{b}^{\ast}(M\_{b,t}))\eta\Big)^{2}}\_{\mu\_{b}(M)}\,\mathrm{d}t\underbrace{-D(p\_{b}^{\ast}(M\_{b,t}))\eta}\_{\sigma\_{b}(M)}\,\mathrm{d}B\_{t},\quad M\_{b,t}\in[0,\overline{M}\_{b}], |  | (5.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mr,t\displaystyle\mathrm{d}M\_{r,t} | =D​(pr∗​(Mr,t))​η​(pr∗​(Mr,t)+h∗​(Mr,t))​d​t−D​(pr∗​(Mr,t))​η​d​Bth∗\displaystyle=D\!\left(p\_{r}^{\ast}(M\_{r,t})\right)\eta\Big(p\_{r}^{\ast}(M\_{r,t})+h^{\ast}(M\_{r,t})\Big)\,\mathrm{d}t-D\!\left(p\_{r}^{\ast}(M\_{r,t})\right)\eta\,\mathrm{d}B\_{t}^{h^{\ast}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Rr​(Mr,t)​(D​(pr∗​(Mr,t))​η)2⏟μr​(M)​d​t​−D​(pr∗​(Mr,t))​η⏟σr​(M)​d​Bth∗,Mr,t∈[M¯r,M¯r],\displaystyle=\underbrace{R\_{r}(M\_{r,t})\Big(D(p\_{r}^{\ast}(M\_{r,t}))\eta\Big)^{2}}\_{\mu\_{r}(M)}\,\mathrm{d}t\underbrace{-D(p\_{r}^{\ast}(M\_{r,t}))\eta}\_{\sigma\_{r}(M)}\,\mathrm{d}B\_{t}^{h^{\ast}},\quad M\_{r,t}\in[\underline{M}\_{r},\overline{M}\_{r}], |  | (5.2) |

where the first process describes the dynamics under the physical measure ℙ\mathbb{P} in the absence of model uncertainty, while the second corresponds to the dynamics under the optimally chosen worst-case measure ℚh∗\mathbb{Q}^{h^{\ast}} in the presence of model uncertainty. Here, BtB\_{t} denotes a standard Brownian motion under ℙ\mathbb{P}, and Bth∗B\_{t}^{h^{\ast}} the Brownian motion under ℚh∗\mathbb{Q}^{h^{\ast}}. For numerical comparison, we impose the same Brownian increments across the two measures, so that differences in dynamics are solely attributable to model uncertainty rather than stochastic noise.

Figure [5.1](https://arxiv.org/html/2510.15709v1#S5.F1 "Figure 5.1 ‣ 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management") presents the simulated dynamic equilibrium outcomes for the insurance market, including the reserve process and the price process, with and without model uncertainty. The simulations are initialized with an aggregate capacity of M0=0.3M\_{0}=0.3. A key observation is that, regardless of whether model uncertainty is present, the insurance price adjusts dynamically with the level of aggregate capacity, generating the cyclical behavior commonly documented in insurance markets (Harrington et al.,, [2013](https://arxiv.org/html/2510.15709v1#bib.bib30)). The two paths display broadly similar directional movements, which is due to the fact that we impose identical Brownian increments.

Our primary interest lies in the impact of model uncertainty on market dynamics. Obviously, the robust equilibrium price pr​(Mr,t)p\_{r}(M\_{r,t}) is systematically higher than pb​(Mb,t)p\_{b}(M\_{b,t}), even though liquid reserves are also maintained at higher levels for most of the time. It reflects the additional premium that insurers require as compensation for model misspecification, while at the same time indicating that capital accumulation in the insurance sector becomes more resilient under robustness concerns.

A further observation is that the volatility of both the reserve and price processes in the robust equilibrium is relatively smaller than in the benchmark case. As shown in ([5.1](https://arxiv.org/html/2510.15709v1#S5.E1 "In 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management")) and ([5.2](https://arxiv.org/html/2510.15709v1#S5.E2 "In 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management")), the effective diffusion term |σr​(M)|\left|\sigma\_{r}(M)\right| is generally lower than |σb​(M)|\left|\sigma\_{b}(M)\right| because of reduced demand. Quantitatively, the drift term |μ​(M)|\left|\mu(M)\right| is very small compared to |σ​(M)|\left|\sigma(M)\right|, implying that fluctuations within the two boundaries are primarily driven by diffusion. The smaller volatility, combined with a wider admissible capacity range, lengthens the duration of cycles in the robust equilibrium. These features indicate that insurers operate in a more stable and conservative manner under robustness concerns: both reserve flows and price movements exhibit lower volatility, and capital adjustments (recapitalization as well as payouts) occur less frequently, leading to more persistent reserve dynamics.

![Refer to caption](equilibrium/sim_Mt.png)

![Refer to caption](equilibrium/sim_pMt.png)

Figure 5.1: Dynamic Equilibrium Outcomes with and without Model Uncertainty.



![Refer to caption](equilibrium/sim_MC_M.png)

![Refer to caption](equilibrium/sim_MC_p.png)

Figure 5.2: Monte Carlo Simulation of Dynamic Equilibrium Outcomes.

Figure [5.2](https://arxiv.org/html/2510.15709v1#S5.F2 "Figure 5.2 ‣ 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management") reports the Monte Carlo simulation of the dynamic equilibrium, where 2000 sample paths are generated and the mean together with the 5%-95% quantile bands are shown. Both the average aggregate reserves and the average market price are systematically higher in the robust equilibrium than in the benchmark case. As TT increases, the mean curves of both equilibria flatten out, indicating that the system converges to a stationary distribution.

### 5.2 Duration of Underwriting Cycles

We have documented the cyclical nature of insurance capacity and pricing dynamics in the previous analysis. In this subsection, we turn to the impact of model uncertainty on the duration of underwriting cycles. Formally, an underwriting cycle is defined as alternating phases of: (1) a soft market, during which insurers’ aggregate capacity expands from M¯\underline{M} to M¯\overline{M}, leading to falling equilibrium prices; and (2) a hard market, during which aggregate capacity contracts from M¯\overline{M} back to M¯\underline{M}, accompanied by rising prices. Similar to Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)), we compute the expected duration of each phase of the underwriting cycle based on the dynamics in ([5.1](https://arxiv.org/html/2510.15709v1#S5.E1 "In 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management")) and ([5.2](https://arxiv.org/html/2510.15709v1#S5.E2 "In 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management")).

Formally, let Ts​(M)T\_{s}(M) denote the expected time for the reserve process MtM\_{t} to reach the upper boundary M¯\overline{M} from any state M≤M¯M\leq\overline{M}. Then, Ts​(M¯)T\_{s}(\underline{M}) captures the expected duration of the soft market phase. Let Th​(M)T\_{h}(M) be the expected time for MtM\_{t} to return from any state M≥M¯M\geq\underline{M} to the lower boundary M¯\underline{M}. Then, Th​(M¯)T\_{h}(\overline{M}) represents the expected duration of the hard market phase. Finally, the total expected duration of an insurance cycle is given by Tc≜Ts​(M¯)+Th​(M¯)T\_{c}\triangleq T\_{s}(\underline{M})+T\_{h}(\overline{M}).

###### Proposition 6.

Let o∈{b,r}o\in\{b,r\} index the benchmark and robust equilibria, and let the aggregate capacity Mo,tM\_{o,t} evolve on [M¯o,M¯o][\underline{M}\_{o},\overline{M}\_{o}] with drift μo​(M)\mu\_{o}(M) and volatility σo​(M)\sigma\_{o}(M). Then, Ts,o​(⋅)T\_{s,o}(\cdot) and Th,o​(⋅)T\_{h,o}(\cdot) should solve the following ODEs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −1\displaystyle-1 | =μo​(M)​Ts,o′​(M)+12​σo2​(M)​Ts,o′′​(M),withTs,o′​(M¯o)=0,Ts,o​(M¯o)=0,\displaystyle=\mu\_{o}(M)T^{\prime}\_{s,o}(M)+\frac{1}{2}\sigma\_{o}^{2}(M)T^{\prime\prime}\_{s,o}(M),\quad\text{with}\quad T^{\prime}\_{s,o}(\underline{M}\_{o})=0,\ T\_{s,o}(\overline{M}\_{o})=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −1\displaystyle-1 | =μo​(M)​Th,o′​(M)+12​σo2​(M)​Th,o′′​(M),withTh,o​(M¯o)=0,Th,o′​(M¯o)=0.\displaystyle=\mu\_{o}(M)T^{\prime}\_{h,o}(M)+\frac{1}{2}\sigma\_{o}^{2}(M)T^{\prime\prime}\_{h,o}(M),\quad\text{with}\quad T\_{h,o}(\underline{M}\_{o})=0,\ T^{\prime}\_{h,o}(\overline{M}\_{o})=0. |  |

The Neumann conditions impose instantaneous reflection at the non-target boundary, while the Dirichlet conditions set the hitting time to zero upon arrival at the target boundary.

The result follows from the Feynman-Kac representation for diffusions with reflecting boundaries (see, e.g., Lions and Sznitman,, [1984](https://arxiv.org/html/2510.15709v1#bib.bib49); Karatzas and Shreve,, [2014](https://arxiv.org/html/2510.15709v1#bib.bib38)). For a detailed argument in a closely related setting, see Section 4.2 of Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)).

![Refer to caption](equilibrium/fig_duration_benchmark.png)

![Refer to caption](equilibrium/fig_duration_robust.png)

Figure 5.3: Expected Phase Durations with and without Model Uncertainty.

Figure [5.3](https://arxiv.org/html/2510.15709v1#S5.F3 "Figure 5.3 ‣ 5.2 Duration of Underwriting Cycles ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management") reports the numerical solutions for Ts,o​(⋅)T\_{s,o}(\cdot) and Th,o​(⋅)T\_{h,o}(\cdot) under both equilibria. Specifically, we obtain Ts,b​(M¯b)=4.78T\_{s,b}(\underline{M}\_{b})=4.78, Th,b​(M¯b)=4.84T\_{h,b}(\overline{M}\_{b})=4.84, Tc,b=9.62T\_{c,b}=9.62, while Ts,r​(M¯r)=14.05T\_{s,r}(\underline{M}\_{r})=14.05, Th,r​(M¯r)=11.92T\_{h,r}(\overline{M}\_{r})=11.92, Tc,r=25.97T\_{c,r}=25.97. First, the results indicate that the expected durations of both the soft and hard markets are substantially longer in the robust equilibrium with model uncertainty. As discussed above, this stems from more conservative underwriting and pricing strategies, which lower volatility and widen the admissible capacity range.

Second, the durations of the two phases become more asymmetric once model uncertainty is introduced. Under plausible parameterizations, the soft market is expected to last significantly longer than the hard market, consistent with the empirical stylized fact highlighted by Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)). By contrast, while the equilibrium without model uncertainty in Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)) also theoretically predicts such asymmetry, this feature is less pronounced in our benchmark results due to differences in the demand specification and parameter choices.

Table [3](https://arxiv.org/html/2510.15709v1#S5.T3 "Table 3 ‣ 5.2 Duration of Underwriting Cycles ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management") presents the estimated results of robust market phase durations under different parameters. While Table [2](https://arxiv.org/html/2510.15709v1#S4.T2 "Table 2 ‣ 4.2 Impact of Robustness Degree ‣ 4 Quantitative Analysis ‣ Robust Insurance Pricing and Liquidity Management") shows that the capacity range is non-monotone in the robustness degree θ\theta, here the expected duration of the insurance cycle appears to decrease with θ\theta. The more ambiguity-averse the insurers are, the longer the cycle becomes. This pattern reflects that stronger robustness concerns slow down capital adjustments and dampen fluctuations, thereby prolonging the time it takes for reserves and prices to traverse between boundaries. Similarly, with respect to the external financing cost γ\gamma, higher values of γ\gamma are associated with longer cycle durations. A higher cost of recapitalization makes insurers more cautious in their capacity management, reducing the speed of adjustment and thereby extending both the soft and hard market phases.

###### Remark 2.

In our numerical analysis, all parameters are specified on an annual basis. After incorporating robust pricing and liquidity management strategies, the expected duration of the insurance cycle extends from about 10 years to roughly 26 years, far exceeding the commonly reported 6-10 year range in earlier empirical studies (Cummins and Outreville,, [1987](https://arxiv.org/html/2510.15709v1#bib.bib15); Harrington et al.,, [2013](https://arxiv.org/html/2510.15709v1#bib.bib30)). Recent literature has questioned the very existence of underwriting cycles. For instance, Boyer et al., ([2012](https://arxiv.org/html/2510.15709v1#bib.bib5)) estimate cycle lengths of 8-11 years using AR(2)/AR(3) models, but these estimates are highly sensitive to small variations in coefficients and, within a 38-year sample, cover only 3-4 cycles, resulting in very low statistical confidence. Our results provide a possible explanation: underwriting cycles may indeed exist, but their duration is much longer than previously assumed. Consequently, short data samples may fail to contain enough realizations to allow for robust statistical inference.

|  |  |  |  |
| --- | --- | --- | --- |
| Parameter | Soft Market Duration, Ts,r​(M¯r)T\_{s,r}(\underline{M}\_{r}) | Hard Market Duration, Th,r​(M¯r)T\_{h,r}(\overline{M}\_{r}) | Total Duration, Tc,rT\_{c,r} |
| θ=0.5\theta=0.5 | 68.23 | 37.33 | 105.56 |
| θ=2.8\theta=2.8 | 14.05 | 11.92 | 25.97 |
| θ=5\theta=5 | 10.98 | 9.85 | 20.83 |
| θ=50\theta=50 | 6.14 | 6.11 | 12.25 |
| θ=500\theta=500 | 5.03 | 5.10 | 10.13 |
| γ=0.06\gamma=0.06 | 6.27 | 5.30 | 11.57 |
| γ=0.1\gamma=0.1 | 8.87 | 7.44 | 16.31 |
| γ=0.2\gamma=0.2 | 14.05 | 11.92 | 25.97 |
| γ=0.3\gamma=0.3 | 18.23 | 15.83 | 34.06 |
| γ=0.4\gamma=0.4 | 21.83 | 19.43 | 41.26 |

Table 3: Numerically Solved Expected Durations.

### 5.3 Ergodic Property

For the insurance cycle driven by fluctuations in aggregate capacity, we can further study its ergodic property. In other words, we are interested in whether the capacity process MtM\_{t} with reflecting boundaries [M¯,M¯][\underline{M},\overline{M}] converges to a stationary distribution in the long run, so that insurance cycles can be regarded as statistically recurrent stochastic fluctuations.

###### Proposition 7.

Let o∈{b,r}o\in\{b,r\} index the benchmark and robust equilibria, Then {Mo,t}t≥0\{M\_{o,t}\}\_{t\geq 0}, evolving according to ([5.1](https://arxiv.org/html/2510.15709v1#S5.E1 "In 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management")) or ([5.2](https://arxiv.org/html/2510.15709v1#S5.E2 "In 5.1 Underwriting Dynamics ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management")), is a strong Markov diffusion that admits a unique invariant probability measure πo\pi\_{o} and is ergodic in the sense that, for every bounded measurable ff:

|  |  |  |
| --- | --- | --- |
|  | limT→∞1T​∫0Tf​(Mo,t)​dt=∫M¯oM¯of​(M)​πo​(d​M),a.s..\lim\_{T\rightarrow\infty}\frac{1}{T}\int\_{0}^{T}f(M\_{o,t})\mathrm{d}t=\int\_{\underline{M}\_{o}}^{\overline{M}\_{o}}f(M)\pi\_{o}(\mathrm{d}M),\quad\text{a.s.}. |  |

Moreover, πo\pi\_{o} has a density π~o​(⋅)\tilde{\pi}\_{o}(\cdot) given by:

|  |  |  |
| --- | --- | --- |
|  | π~o​(M)=κo(D​(po∗​(M))​η)2​exp⁡(2​∫M¯oMRo∗​(z)​dz),M∈[M¯o,M¯o],\tilde{\pi}\_{o}(M)=\frac{\kappa\_{o}}{\big(D(p\_{o}^{\ast}(M))\eta\big)^{2}}\exp\left(2\int\_{\underline{M}\_{o}}^{M}R\_{o}^{\ast}(z)\mathrm{d}z\right),\quad M\in[\underline{M}\_{o},\overline{M}\_{o}], |  |

where the normalizing constant is κo−1=∫M¯oM¯o1(D​(po∗​(M))​η)2​exp⁡(2​∫M¯oMRo∗​(z)​dz)​dM\kappa\_{o}^{-1}=\int\_{\underline{M}\_{o}}^{\overline{M}\_{o}}\frac{1}{\big(D(p^{\ast}\_{o}(M))\eta\big)^{2}}\exp\!\Bigg(2\int\_{\underline{M}\_{o}}^{M}R^{\ast}\_{o}(z)\mathrm{d}z\Bigg)\mathrm{d}M.

The stationary density in the proposition is derived from the Fokker-Planck equation. Importantly, the term R​(M)=μ​(M)σ2​(M)R(M)=\frac{\mu(M)}{\sigma^{2}(M)} appears as the key driver inside the exponential, playing a role analogous to a kernel that shapes the distribution.

Figure [5.4](https://arxiv.org/html/2510.15709v1#S5.F4 "Figure 5.4 ‣ 5.3 Ergodic Property ‣ 5 Insurers’ Long-Run Behavior Pattern ‣ Robust Insurance Pricing and Liquidity Management") reports the numerically solved results. In both the benchmark and robust equilibria, the density function exhibits a downward slope, indicating that the probability mass is concentrated at relatively low capacity levels. This finding differs from the hump-shaped pattern documented by Luciano and Rochet, ([2022](https://arxiv.org/html/2510.15709v1#bib.bib50)), which arises when external investment opportunities are considered, but it is consistent with the results of Henriet et al., ([2016](https://arxiv.org/html/2510.15709v1#bib.bib33)).

Moreover, the curves of π~b\tilde{\pi}\_{b} and π~r\tilde{\pi}\_{r} intersect, showing that in the robust equilibrium the density is higher at low capacity levels and lower at high capacity levels. As ambiguity aversion strengthens, the stationary distribution shifts further toward the left boundary, reflecting more conservative capital management in the insurance sector. This also implies that when the industry is hit by a severe negative shock that substantially depletes reserves, it becomes harder and takes considerably longer for insurers to escape from such low-capacity states. Finally, an increase in the external financing cost γ\gamma raises the marginal value of precautionary reserves, thereby flattening the distribution and spreading the density more evenly across a wider range of capacity levels.

###### Remark 3.

Boyer et al., ([2012](https://arxiv.org/html/2510.15709v1#bib.bib5)) show that using estimated cyclical components to forecast underwriting ratios 1-2 years ahead yields very poor accuracy. Our results provide a structural explanation: the distribution of insurance cycles is not uniform across states. Once model uncertainty is introduced, the capacity process becomes more skewed toward low-capacity states, where insurers tend to remain trapped for longer and recover more slowly. This persistence in depressed states implies that, even though cycles exist in theory, their short-run predictive content is extremely limited.

![Refer to caption](equilibrium/stationary_density_theta_compare.png)

![Refer to caption](equilibrium/stationary_density_gamma_compare.png)

Figure 5.4: Stationary Density of Capacity with Different Parameters.

## 6 Conclusion

This paper investigates how model uncertainty influences equilibrium insurance pricing and liquidity management in a dynamic competitive market. By incorporating insurers’ robustness preferences, we show that ambiguity aversion fundamentally reshapes underwriting behavior, leading to higher premiums, high market-to-book ratios and more conservative liquidity management. The equilibrium outcomes reveal several novel patterns: the admissible capacity range expands, the expected length of underwriting cycles is substantially prolonged, and the stationary distribution of reserves becomes more concentrated in low-capacity states. Together, these features suggest that insurers adopt more cautious strategies when facing model misspecification, but at the cost of reduced market activity and longer recovery times following adverse shocks.

These findings provide theoretical justification for regulatory interventions such as stricter reserve requirements and more robust solvency standards, which can enhance the resilience of the insurance sector. More broadly, our results offer a potential explanation for the mixed empirical evidence on underwriting cycles: cycles may indeed exist, but are much longer than commonly assumed, making them difficult to detect within conventional data samples.

There are several ways to refine our model to explore more meaningful questions. For instance, we assume that insurers are homogeneous, differing only in their initial capital levels, which leads them to adopt identical underwriting and pricing strategies. However, in reality, insurers exhibit significant heterogeneity, and capital adequacy plays a crucial role in determining firm size and market power. Larger and smaller insurers are likely to adopt different strategies, making the analysis of market structure and its implications a promising avenue for future research.

Building on this, another important yet overlooked factor in our model is the optimal liquidation decision, which is commonly studied in liquidity management problems. In our current setting, this omission is not a major concern, as insurers are assumed to be homogeneous, and the entire insurance sector does not face insolvency. However, in a setting with heterogeneous insurers, model uncertainty in emerging or catastrophic risks could disproportionately impact smaller insurers, making them more susceptible to insolvency. Investigating how heterogeneous insurers respond to model uncertainty, including potential liquidation decisions, could further enrich the understanding of robust insurance pricing and liquidity management strategies.

## References

* Anderson et al., (2003)

  Anderson, E. W., Hansen, L. P., and Sargent, T. J. (2003).
  A quartet of semigroups for model specification, robustness, prices of risk, and model detection.
  Journal of the European Economic Association, 1(1):68–123.
* Anwar and Zheng, (2012)

  Anwar, S. and Zheng, M. (2012).
  Competitive insurance market in the presence of ambiguity.
  Insurance: Mathematics and Economics, 50(1):79–84.
* Bernard et al., (2015)

  Bernard, C., He, X., Yan, J.-A., and Zhou, X. Y. (2015).
  Optimal insurance design under rank-dependent expected utility.
  Mathematical Finance, 25(1):154–186.
* Bolton et al., (2011)

  Bolton, P., Chen, H., and Wang, N. (2011).
  A unified theory of Tobin’s q, corporate investment, financing, and risk management.
  The Journal of Finance, 66(5):1545–1578.
* Boyer et al., (2012)

  Boyer, M. M., Jacquier, E., and Van Norden, S. (2012).
  Are underwriting cycles real and forecastable?
  Journal of Risk and Insurance, 79(4):995–1015.
* Boyer and Owadally, (2015)

  Boyer, M. M. and Owadally, I. (2015).
  Underwriting apophenia and cryptids: are cycles statistical figments of our imagination?
  The Geneva Papers on Risk and Insurance-Issues and Practice, 40(2):232–255.
* Brunnermeier and Pedersen, (2009)

  Brunnermeier, M. K. and Pedersen, L. H. (2009).
  Market liquidity and funding liquidity.
  The Review of Financial Studies, 22(6):2201–2238.
* Cabantous, (2007)

  Cabantous, L. (2007).
  Ambiguity aversion in the field of insurance: Insurers’ attitude to imprecise and conflicting probability estimates.
  Theory and Decision, 62(3):219–240.
* Cabantous et al., (2011)

  Cabantous, L., Hilton, D., Kunreuther, H., and Michel-Kerjan, E. (2011).
  Is imprecise knowledge better than conflicting expertise? Evidence from insurers’ decisions in the united states.
  Journal of Risk and Uncertainty, 42:211–232.
* Campbell, (1980)

  Campbell, R. A. (1980).
  The demand for life insurance: An application of the economics of uncertainty.
  The Journal of Finance, 35(5):1155–1172.
* Chen et al., (1999)

  Chen, R., Wong, K. A., and Lee, H. C. (1999).
  Underwriting cycles in Asia.
  Journal of Risk and Insurance, pages 29–47.
* Cheng et al., (2024)

  Cheng, B., Wang, H., and Zhang, L. (2024).
  Robust investment for insurers with correlation ambiguity.
  The Quarterly Review of Economics and Finance, 93:247–257.
* Cummins and Lamm-Tennant, (1994)

  Cummins, J. D. and Lamm-Tennant, J. (1994).
  Capital structure and the cost of equity capital in the property-liability insurance industry.
  Insurance: Mathematics and Economics, 15(2-3):187–201.
* Cummins and Mahul, (2004)

  Cummins, J. D. and Mahul, O. (2004).
  The demand for insurance with an upper limit on coverage.
  Journal of Risk and Insurance, 71(2):253–264.
* Cummins and Outreville, (1987)

  Cummins, J. D. and Outreville, J. F. (1987).
  An international analysis of underwriting cycles in property-liability insurance.
  Journal of Risk and Insurance, pages 246–262.
* Cummins and Phillips, (2005)

  Cummins, J. D. and Phillips, R. D. (2005).
  Estimating the cost of equity capital for property-liability insurers.
  Journal of Risk and Insurance, 72(3):441–478.
* Dicks and Garven, (2022)

  Dicks, D. L. and Garven, J. R. (2022).
  Asymmetric information and insurance cycles.
  Journal of Risk and Insurance, 89(2):449–474.
* Dietz and Niehörster, (2021)

  Dietz, S. and Niehörster, F. (2021).
  Pricing ambiguity in catastrophe risk insurance.
  The Geneva Risk and Insurance Review, 46(2):112–132.
* Dietz and Walker, (2019)

  Dietz, S. and Walker, O. (2019).
  Ambiguity and insurance: capital requirements and premiums.
  Journal of Risk and Insurance, 86(1):213–235.
* Eckles et al., (2016)

  Eckles, D. L., McCarthy, D. G., and Zeng, X. (2016).
  The theory of optimal stochastic control as applied to insurance underwriting cycles.
  North American Actuarial Journal, 20(4):327–340.
* Eling and Schnell, (2016)

  Eling, M. and Schnell, W. (2016).
  What do we know about cyber risk and cyber risk insurance?
  The Journal of Risk Finance, 17(5):474–491.
* Ellsberg, (1961)

  Ellsberg, D. (1961).
  Risk, ambiguity, and the savage axioms.
  The Quarterly Journal of Economics, 75(4):643–669.
* Fan et al., (2017)

  Fan, V. Y., Jamison, D. T., and Summers, L. H. (2017).
  Pandemic risk: how large are the expected losses?
  Bulletin of the World Health Organization, 96(2):129.
* Ge, (2022)

  Ge, S. (2022).
  How do financial constraints affect product pricing? Evidence from weather and life insurance premiums.
  The Journal of Finance, 77(1):449–503.
* (25)

  Gron, A. (1994a).
  Capacity constraints and cycles in property-casualty insurance markets.
  The RAND Journal of Economics, pages 110–127.
* (26)

  Gron, A. (1994b).
  Evidence of capacity constraints in insurance markets.
  The Journal of Law and Economics, 37(2):349–377.
* Guan and Liang, (2019)

  Guan, G. and Liang, Z. (2019).
  Robust optimal reinsurance and investment strategies for an AAI with multiple risks.
  Insurance: Mathematics and Economics, 89:63–78.
* Hansen and Sargent, (2001)

  Hansen, L. P. and Sargent, T. J. (2001).
  Robust control and model uncertainty.
  American Economic Review, 91(2):60–66.
* Hansen and Sargent, (2008)

  Hansen, L. P. and Sargent, T. J. (2008).
  Robustness.
  Princeton university press.
* Harrington et al., (2013)

  Harrington, S. E., Niehaus, G., and Yu, T. (2013).
  Insurance price volatility and underwriting cycles.
  Handbook of Insurance, pages 647–667.
* Harrington and Yu, (2003)

  Harrington, S. E. and Yu, T. (2003).
  Do property-casualty insurance underwriting margins have unit roots?
  Journal of Risk and Insurance, 70(4):715–733.
* He and Krishnamurthy, (2013)

  He, Z. and Krishnamurthy, A. (2013).
  Intermediary asset pricing.
  American Economic Review, 103(2):732–770.
* Henriet et al., (2016)

  Henriet, D., Klimenko, N., and Rochet, J.-C. (2016).
  The dynamics of insurance prices.
  The Geneva Risk and Insurance Review, 41:2–18.
* Hogarth and Kunreuther, (1989)

  Hogarth, R. M. and Kunreuther, H. (1989).
  Risk, ambiguity, and insurance.
  Journal of Risk and Uncertainty, 2(1):5–35.
* Hogarth and Kunreuther, (1992)

  Hogarth, R. M. and Kunreuther, H. (1992).
  Pricing insurance and warranties: Ambiguity and correlated risks.
  The Geneva Papers on Risk and Insurance Theory, 17:35–60.
* Jaffee and Russell, (1997)

  Jaffee, D. M. and Russell, T. (1997).
  Catastrophe insurance, capital markets, and uninsurable risks.
  Journal of Risk and Insurance, pages 205–230.
* Jensen and Meckling, (1976)

  Jensen, M. C. and Meckling, W. H. (1976).
  Theory of the firm: Managerial behavior, agency costs and ownership structure.
  Journal of Financial Economics, 3(4):305–360.
* Karatzas and Shreve, (2014)

  Karatzas, I. and Shreve, S. (2014).
  Brownian Motion and Stochastic Calculus, volume 113.
  Springer.
* Knight, (1921)

  Knight, F. H. (1921).
  Risk, Uncertainty and Profit, volume 31.
  Houghton Mifflin.
* Koijen and Yogo, (2015)

  Koijen, R. S. and Yogo, M. (2015).
  The cost of financial frictions for life insurers.
  American Economic Review, 105(1):445–475.
* Koijen and Yogo, (2022)

  Koijen, R. S. and Yogo, M. (2022).
  The fragility of market risk insurance.
  The Journal of Finance, 77(2):815–862.
* Koijen and Yogo, (2023)

  Koijen, R. S. and Yogo, M. (2023).
  Financial Economics of Insurance.
  Princeton University Press.
* Kunreuther et al., (1993)

  Kunreuther, H., Hogarth, R., and Meszaros, J. (1993).
  Insurer ambiguity and market failure.
  Journal of Risk and Uncertainty, 7:71–87.
* Kunreuther et al., (1995)

  Kunreuther, H., Meszaros, J., Hogarth, R. M., and Spranca, M. (1995).
  Ambiguity and underwriter decision processes.
  Journal of Economic Behavior & Organization, 26(3):337–352.
* Lamm-Tennant and Weiss, (1997)

  Lamm-Tennant, J. and Weiss, M. A. (1997).
  International insurance cycles: rational expectations/institutional intervention.
  Journal of Risk and Insurance, pages 415–439.
* Leland and Pyle, (1977)

  Leland, H. E. and Pyle, D. H. (1977).
  Informational asymmetries, financial structure, and financial intermediation.
  The Journal of Finance, 32(2):371–387.
* Li and Young, (2019)

  Li, D. and Young, V. R. (2019).
  Optimal reinsurance to minimize the discounted probability of ruin under ambiguity.
  Insurance: Mathematics and Economics, 87:143–152.
* Ling et al., (2021)

  Ling, A., Miao, J., and Wang, N. (2021).
  Robust financial contracting and investment.
  Technical report, National Bureau of Economic Research.
* Lions and Sznitman, (1984)

  Lions, P.-L. and Sznitman, A.-S. (1984).
  Stochastic differential equations with reflecting boundary conditions.
  Communications on Pure and Applied Mathematics, 37(4):511–537.
* Luciano and Rochet, (2022)

  Luciano, E. and Rochet, J. C. (2022).
  The fluctuations of insurers’ risk appetite.
  Journal of Economic Dynamics and Control, 144:104543.
* (51)

  Maccheroni, F., Marinacci, M., and Rustichini, A. (2006a).
  Ambiguity aversion, robustness, and the variational representation of preferences.
  Econometrica, 74(6):1447–1498.
* (52)

  Maccheroni, F., Marinacci, M., and Rustichini, A. (2006b).
  Dynamic variational preferences.
  Journal of Economic Theory, 128(1):4–44.
* Maenhout et al., (2020)

  Maenhout, P. J., Vedolin, A., and Xing, H. (2020).
  Generalized robustness and dynamic pessimism.
  Technical report, National Bureau of Economic Research.
* Myers and Majluf, (1984)

  Myers, S. C. and Majluf, N. S. (1984).
  Corporate financing and investment decisions when firms have information that investors do not have.
  Journal of Financial Economics, 13(2):187–221.
* Peter and Ying, (2020)

  Peter, R. and Ying, J. (2020).
  Do you trust your insurer? Ambiguity about contract nonperformance and optimal insurance demand.
  Journal of Economic Behavior & Organization, 180:938–954.
* Pichler, (2014)

  Pichler, A. (2014).
  Insurance pricing under ambiguity.
  European Actuarial Journal, 4:335–364.
* Rochet and Villeneuve, (2011)

  Rochet, J.-C. and Villeneuve, S. (2011).
  Liquidity management and corporate demand for hedging and insurance.
  Journal of Financial Intermediation, 20(3):303–323.
* Rothschild and Stiglitz, (1976)

  Rothschild, M. and Stiglitz, J. (1976).
  Equilibrium in competitive insurance markets: An essay on the economics of imperfect information.
  The Quarterly Journal of Economics, 90(4):629–649.
* Schmidt, (2016)

  Schmidt, U. (2016).
  Insurance demand under prospect theory: A graphical analysis.
  Journal of Risk and Insurance, 83(1):77–89.
* Winter, (1994)

  Winter, R. A. (1994).
  The dynamics of competitive insurance markets.
  Journal of Financial Intermediation, 3(4):379–415.
* Yaari, (1965)

  Yaari, M. E. (1965).
  Uncertain lifetime, life insurance, and the theory of the consumer.
  The Review of Economic Studies, 32(2):137–150.
* Yi et al., (2013)

  Yi, B., Li, Z., Viens, F. G., and Zeng, Y. (2013).
  Robust optimal control for an insurer with reinsurance and investment under Heston’s stochastic volatility model.
  Insurance: Mathematics and Economics, 53(3):601–614.
* Zeng et al., (2016)

  Zeng, Y., Li, D., and Gu, A. (2016).
  Robust equilibrium reinsurance-investment strategy for a mean–variance insurer in a model with jumps.
  Insurance: Mathematics and Economics, 66:138–152.
* Zhao and Zhu, (2011)

  Zhao, L. and Zhu, W. (2011).
  Ambiguity aversion: A new perspective on insurance pricing.
  ASTIN Bulletin: The Journal of the IAA, 41(1):157–189.