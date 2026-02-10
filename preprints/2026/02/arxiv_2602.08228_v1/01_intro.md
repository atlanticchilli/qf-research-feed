---
authors:
- Alireza Ghahtarani
- Ahmed Saif
- Alireza Ghasemi
doc_id: arxiv:2602.08228v1
family_id: arxiv:2602.08228
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally
  Robust Asset Liability Management
url_abs: http://arxiv.org/abs/2602.08228v1
url_html: https://arxiv.org/html/2602.08228v1
venue: arXiv q-fin
version: 1
year: 2026
---


Alireza Ghahtarani
Corresponding author (alireza.ghahtarani@hec.ca).
Department of Logistics and Operations Management, HEC Montréal

Ahmed Saif
Contributing author (Ahmed.Saif@dal.ca).
Department of Industrial Engineering, Dalhousie University

Alireza Ghasemi
Contributing author (alireza.ghasemi@dal.ca).
Department of Industrial Engineering, Dalhousie University

###### Abstract

Asset Liability Management (ALM) represents a fundamental challenge for financial institutions, particularly pension funds, which must navigate the tension between generating competitive investment returns and ensuring the solvency of long-term obligations. To address the limitations of traditional frameworks under uncertainty, this paper implements Distributionally Robust Optimization (DRO), an emergent paradigm that accounts for a broad spectrum of potential probability distributions. We propose and evaluate three distinct DRO formulations: mixture ambiguity sets with discrete scenarios, box ambiguity sets of discrete distribution functions, and Wasserstein metric ambiguity sets. Utilizing empirical data from the Canada Pension Plan (CPP), we conduct a comparative analysis of these models against traditional stochastic programming approaches. Our results demonstrate that DRO formulations, specifically those utilizing Wasserstein and box ambiguity sets, consistently outperform both mixture-based DRO and stochastic programming in terms of funding ratios and overall fund returns. These findings suggest that incorporating distributional robustness significantly enhances the resilience and performance of pension fund management strategies.

Keywords: Asset Liability Management, Distributionally Robust Optimization, Pension Funds, Ambiguity Sets, Wasserstein Metric

## 1 Introduction

Asset-liability management (ALM) refers to the challenge of managing the assets and liabilities of an entity in a way that ensures the entity can meet its financial obligations in the future (Zenios, [1995](https://arxiv.org/html/2602.08228v1#bib.bib42 "Asset/liability management under uncertainty for fixed-income securities")). The ALM problem typically arises in financial institutions such as banks, insurance companies, and pension funds, which have significant liabilities that must be met over a long period of time. In particular, ALM is a critical concern for pension funds that must ensure they meet specific obligations to individuals who have contributed to their funds while also generating investment returns (Bodie et al., [1988](https://arxiv.org/html/2602.08228v1#bib.bib43 "Defined benefit versus defined contribution pension plans: what are the real trade-offs?")).

Pension funds play a crucial role in the global financial landscape as evidenced by their substantial assets which exceeded $​60.6\mathdollar 60.6 trillion by the end of 2021, accounting for 33%33\% of global assets 111https://www.thinkingaheadinstitute.org/research-papers/global-pension-assets-study-2022/. This magnitude is exemplified by the fact that in nine out of the 38 Organisation for Economic Co-operation and Development (OECD) countries, pension fund assets surpassed their respective GDPs. In the last decade (2010-2020), pension assets have grown by 5.7%5.7\% 222https://www.statista.com/statistics/721151/average-growth-largest-pension-markets-worldwide/, outpacing the 2.6%2.6\% GDP growth rate over the same period 333https://www.macrotrends.net/countries/WLD/world/gdp-growth-rate and underscoring the increasing importance of retirement savings worldwide. However, as the aging population grows, outflows from pension funds to cover benefits are also accelerating. The ratio of benefits paid from retirement savings plans to GDP varies across OECD countries, ranging from 0.5%0.5\% to 8%8\% 444https://www.oecd.org/finance/private-pensions/globalpensionstatistics.htm. This growth in both assets and payouts highlights the need for prudent and sustainable management of pension funds to ensure that retirees receive their benefits without putting undue stress on the funds’ assets.

Pension funds are essential for ensuring retirement income security; however, they encounter challenges arising from demographic changes, low-interest rates, and increasing life expectancy. To address these challenges, reforms have been implemented, including raising the retirement age and promoting private pension plans (Holzmann, [2013](https://arxiv.org/html/2602.08228v1#bib.bib45 "Global pension systems and their reform: worldwide drivers, trends and challenges")). However, one of the major challenges for pension fund managers is the uncertainty surrounding future asset returns and liabilities. The asset returns and the value of liabilities can fluctuate due to factors like inflation, interest rates, and market conditions. To mitigate this risk, effective ALM strategies are necessary. These strategies involve monitoring and managing investment portfolios to ensure they are well-aligned with future obligations. By optimizing the ALM problem under uncertainty, pension funds can enhance long-term sustainability and avoid financial distress (Gülpınar et al., [2016](https://arxiv.org/html/2602.08228v1#bib.bib27 "A robust asset–liability management framework for investment products with guarantees")).

Among the powerful techniques for managing uncertainty in ALM problems is stochastic programming (SP), which explicitly models uncertainty through probability distributions of asset return and liability values and finds optimal asset allocation strategies of the portfolio under different scenarios. This approach allows investors to better hedge against unexpected changes in asset returns and liability values, while still maintaining a desirable level of return (Kouwenberg, [2001](https://arxiv.org/html/2602.08228v1#bib.bib19 "Scenario generation and stochastic programming models for asset liability management")). SP can also be used to optimize dynamic asset allocation strategies, where the asset allocation is periodically adjusted in response to changing market conditions and liability values (Consigli and Dempster, [1998](https://arxiv.org/html/2602.08228v1#bib.bib47 "Dynamic stochastic programmingfor asset-liability management"); Dempster and Consigli, [1996](https://arxiv.org/html/2602.08228v1#bib.bib48 "Dynamic stochastic programming for asset-liability management"); Hibiki, [2006](https://arxiv.org/html/2602.08228v1#bib.bib49 "Multi-period stochastic optimization models for dynamic asset allocation")). By modeling the stochastic behavior of asset returns and liability values, investors can make more informed decisions about the optimal timing and size of asset allocation adjustments, and better manage the risk of underfunding future liabilities. For more details on the application of SP in ALM problems, we refer to (Klaassen, [1997](https://arxiv.org/html/2602.08228v1#bib.bib20 "Discretized reality and spurious profits in stochastic programming models for asset/liability management"); Kouwenberg, [2001](https://arxiv.org/html/2602.08228v1#bib.bib19 "Scenario generation and stochastic programming models for asset liability management"); Consigli, [2008](https://arxiv.org/html/2602.08228v1#bib.bib15 "Asset-liability management for individual investors"); Duarte et al., [2017](https://arxiv.org/html/2602.08228v1#bib.bib17 "Asset liability management for open pension schemes using multistage stochastic programming under solvency-ii-based regulatory constraints"); Kopa et al., [2018](https://arxiv.org/html/2602.08228v1#bib.bib16 "Individual optimal pension allocation under stochastic dominance constraints"); Barro et al., [2022](https://arxiv.org/html/2602.08228v1#bib.bib18 "A stochastic programming model for dynamic portfolio management with financial derivatives")). Despite its intuitive appeal and favorable convergence properties, SP requires large amounts of data on asset returns and liability values to construct their probability distributions, which may be difficult to obtain or may not be available. Furthermore, SP is a risk-neutral approach and thus does not provide sufficient protection against adverse scenarios.

Another popular framework for dealing with uncertainty is robust optimization (RO), which seeks to find solutions that perform optimally under worst-case scenarios, in contrast to SP that aims to optimize the expected performance (Ben-Tal et al., [2009](https://arxiv.org/html/2602.08228v1#bib.bib21 "Robust optimization"); Gabrel et al., [2014](https://arxiv.org/html/2602.08228v1#bib.bib23 "Recent advances in robust optimization: an overview"); Ghahtarani et al., [2022](https://arxiv.org/html/2602.08228v1#bib.bib5 "Robust portfolio selection problems: a comprehensive review")). In the context of ALM, RO can be used to find an asset allocation strategy that is most robust to uncertainty in asset returns and liability values.

A few recent attempts have been made to apply RO to mitigate uncertainty in the ALM problem.
Iyengar and Ma ([2016](https://arxiv.org/html/2602.08228v1#bib.bib25 "A robust optimization approach to pension fund management")) introduced a robust factor model to capture the true uncertainty of asset returns in pension fund management. By incorporating a factor model with stochastic parameters, they developed an ALM formulation with a constraint on the funding ratio. The funding ratio, representing the assets’ value relative to the present value of liabilities, is subject to uncertainty. The proposed formulation assumes the funding ratio as an uncertain parameter and utilizes a Gaussian process for factors. Platanakis and Sutcliffe ([2017](https://arxiv.org/html/2602.08228v1#bib.bib26 "Asset–liability modelling and pension schemes: the application of robust optimization to uss")) extended this approach by considering ellipsoidal uncertainty sets for factor loading, box ambiguity sets for asset returns and liabilities, and upper and lower bounds for the covariance matrix of disturbances, which enabled the problem to be reformulated as a second-order cone programming (SOCP) model. Based on the results, these robust factor models and formulations enhance the out-of-sample performance of ALM problems.
Alongside robust factor models for ALM problems, Gülpinar and Pachamanova ([2013](https://arxiv.org/html/2602.08228v1#bib.bib10 "A robust optimization approach to asset-liability management under time-varying investment opportunities")) proposed a robust ALM using time-varying investment opportunities. They extended the multiperiod PSP formulation of Dantzig and Infanger ([1993](https://arxiv.org/html/2602.08228v1#bib.bib50 "Multi-stage stochastic linear programs for portfolio optimization")) by including liabilities and funding ratio constraints. In this formulation, cumulative rates of return of assets are treated as uncertain parameters within an ellipsoidal uncertainty set. Moreover, asset returns and interest rates are modeled by using the vector-autoregressive process to capture the dynamic nature of investments. In contrast to other robust ALM approaches, Gülpınar et al. ([2016](https://arxiv.org/html/2602.08228v1#bib.bib27 "A robust asset–liability management framework for investment products with guarantees")) developed an asymmetric uncertainty set to better reflect the actual uncertainty structure. Gajek and Krajewska ([2022](https://arxiv.org/html/2602.08228v1#bib.bib51 "Robust portfolio choice under the interest rate uncertainty")) proposed a robust ALM formulation with uncertain interest rates, where the distribution function of the uncertain parameters belongs to a nonempty ambiguity set. This formulation provides an upper bound on VaR (Value at Risk) for portfolio value changes caused by violations of the interest rate model. Finally, the ALM problem with discrete recourse decision and parameter uncertainty has been addressed by Ghahtarani et al. ([2023a](https://arxiv.org/html/2602.08228v1#bib.bib57 "A double-oracle, logic-based benders decomposition approach to solve the k-adaptability problem")) using the KK-adaptability approach.
However, despite being a risk-averse and distribution-free approach, RO usually results in overly conservative investment strategies, which can lead to missed opportunities for higher returns, thus negatively impacting the long-term performance of pension funds.

Disadvantages of the application of either SP or RO in ALM problems provide motivation for the application of a relatively new approach to ALM problems called distributionally robust optimization (DRO) (Rahimian and Mehrotra, [2019](https://arxiv.org/html/2602.08228v1#bib.bib54 "Distributionally robust optimization: a review")). Like RO, DRO aims to minimize the impact of uncertain scenarios on investment decisions. However, DRO goes one step further by enabling the available information about the probability distribution of random variables, albeit limited and imperfect, to be incorporated into the decision-making process, thus leading to less conservative and more stable investment strategies (Lin et al., [2022](https://arxiv.org/html/2602.08228v1#bib.bib52 "Distributionally robust optimization: a review on theory and applications")).
Various researchers, such as (Jiang et al., [2023](https://arxiv.org/html/2602.08228v1#bib.bib59 "Distributionally robust multi-period portfolio selection subject to bankruptcy constraints"); Zhang et al., [2023](https://arxiv.org/html/2602.08228v1#bib.bib60 "High-dimensional distributionally robust mean-variance efficient portfolio selection"); Blanchet et al., [2022](https://arxiv.org/html/2602.08228v1#bib.bib62 "Distributionally robust mean-variance portfolio selection with wasserstein distances"); Zhang et al., [2023](https://arxiv.org/html/2602.08228v1#bib.bib60 "High-dimensional distributionally robust mean-variance efficient portfolio selection")), have employed DRO in addressing the PSP. However, these implementations do not tackle the ALM problem, as they have not accounted for liabilities and uncertainties of liabilities within their models. Unlike SP and RO, which have been applied to the ALM problem, DRO is yet to be leveraged in this context. One reason for this is the inherent complexity of DRO models and their comparatively recent development. Notably, a study by Ghahtarani et al. ([2023b](https://arxiv.org/html/2602.08228v1#bib.bib56 "Worst-case conditional value at risk for asset liability management: a novel framework for general loss functions")) focused on moment-based ambiguity sets for the ALM problem and introduced worst-case Conditional Value at Risk (CVaR) as a risk measure to deal with parameter uncertainty in the problem. DRO has the potential to address some of the limitations of other methods, including the optimizer’s curse in SP and the over-conservatism in RO. Moreover, DRO provides a way to explicitly consider the ambiguity in the distribution of financial variables.

In this paper, we aim to fill this gap in the literature by proposing DRO formulations for the ALM problem. We explore scenarios-based approaches to address the uncertainty of parameters in the ALM problem.
Numerous studies have suggested that scenario-based analysis is superior to prediction-based analysis in financial problems. Boender ([1997](https://arxiv.org/html/2602.08228v1#bib.bib2 "A hybrid simulation/optimisation scenario model for asset/liability management")) argues that scenarios explicitly record assumptions about the future and provide a common framework for discussion. By utilizing scenarios, we can create a better understanding between managers and stakeholders, which can ultimately contribute to more effective decision-making. The main goal of this paper is to develop DRO scenario-based formulations and compare them against each other. The first formulation uses mixture ambiguity sets, each representing a convex combination of multiple distributions, each having multiple scenarios, which is commonly used in portfolio selection problems (Zhu and Fukushima, [2009](https://arxiv.org/html/2602.08228v1#bib.bib37 "Worst-case conditional value-at-risk with application to robust portfolio management")).
In the second formulation, we investigate the case
that the probabilities of scenarios are interval-bounded, but also there is a requirement that they add up to 1, which basically means that we are using a polyhedral set to represent the uncertain probabilities.
Lastly, we incorporate the Wasserstein ambiguity set into the ALM problem, which is a metric-based ambiguity set.
These ambiguity sets have been specifically chosen due to their suitability for utilization in scenario-based DRO formulation.

We develop DRO models for an ALM problem that accounts for the ambiguity about the distribution of asset returns and interest rates. We also compare the performance of our DRO models to the traditional SP formulation of the ALM problem to demonstrate the advantages and limitations of each approach. By doing so, we hope to contribute to the development of a more robust and flexible framework for ALM that can better account for the uncertainty and variability in financial markets.

The set of most used notations is shown in Table LABEL:table:1paper2, whereas the notations that are used once are defined in the text.

Table 1: Notations and symbols

| Symbol/Notation | Definition |
| --- | --- |
| t∈{0,…,T}t\in\{0,\dots,T\} | Indices of decision moments |
| TT | Investment horizon |
| s∈{1,…,S}s\in\{1,\dots,S\} | Indices of discount rate scenarios |
| k∈{1,…,K}k\in\{1,...,K\} | Indices of asset return scenarios |
| yty\_{t} | Contribution rate at tt, the fraction of sponsor and/or active employees’ wages |
| yt,sy\_{t,s} | Contribution rate at tt based on scenario ss |
| n∈{0,…,N}n\in\{0,\dots,N\} | Indices of assets, where n=0n=0 represents risk-free asset or cash |
| xn,tx\_{n,t} | Money invested in asset nn at tt |
| xn,t,kx\_{n,t,k} | Money invested in asset nn at tt based on scenario kk |
| AtA\_{t} | Value of assets owned by the fund at tt |
| WtW\_{t} | Wages earned by active members at tt |
| ltl\_{t} | Payments made by the fund to retirees at tt |
| LtL\_{t} | Net present value of liabilities of the fund at tt |
| Lt,sL\_{t,s} | Net present value of liabilities of the fund at tt based on scenario ss |
| ξn,t\xi\_{n,t} | Return on investment in asset nn at tt |
| ξn,t,k\xi\_{n,t,k} | Return on investment in asset nn at tt based on scenario kk |
| ψ\psi | Minimum threshold of funding ratio |
| γ\gamma | Discount rate for calculating the present value |
| WtW\_{t} | Net present value of wages at tt |
| pp | Discrete distribution function of discount rate |
| qq | Discrete distribution function of asset returns |
| PP | Ambiguity set of the distribution function of discount rate |
| QQ | Ambiguity set of the distribution function of asset returns |

The remaining sections of this paper are structured as follows. Section [2](https://arxiv.org/html/2602.08228v1#S2 "2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") introduces the mathematical formulation of the ALM problem.
In Section [3](https://arxiv.org/html/2602.08228v1#S3 "3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"), we present DRO formulations of the ALM problem based on the mixture distribution, the box, and the Wasserstein ambiguity sets. To test the proposed formulation, numerical experiments using real data from the Canada Pension Plan (CPP) are conducted, and the results are presented in Section [4](https://arxiv.org/html/2602.08228v1#S4 "4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"). Finally, Section [5](https://arxiv.org/html/2602.08228v1#S5 "5 Conclusions ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") offers some conclusions and suggests potential areas for future research.

## 2 ALM Model for Pension Funds

The ALM problem under consideration aims to find an optimal investment strategy that achieves a trade-off between augmenting investment returns and reducing the risk of insolvency.
The objective of the ALM for a pension fund is to minimize the contribution rate by both the sponsor and active employees of the fund (i.e., the contributors), as defined in previous studies (Bogentoft et al., [2001](https://arxiv.org/html/2602.08228v1#bib.bib1 "Asset/liability management for pension funds using cvar constraints")).
The financial burden is reduced by reducing the contribution rate, while the efficient investment strategy balances risk and returns over the investment horizon. The optimization process involves selecting the optimal portfolio of asset classes, such as stocks, bonds, and alternative investments, and the corresponding contribution rate for each period of the investment horizon. By finding the optimal solution to the ALM problem, the pension fund can ensure that it meets its future obligations while minimizing the financial burden on its stakeholders.

The investment horizon for the ALM problem under consideration, denoted as TT, encompasses a series of decision moments represented by t=0,…,Tt=0,\dots,T. Several variables and decision-making components are at play in the ALM problem for pension funds.
The contribution rate at tt is denoted by yty\_{t}, which is the fraction of the contributor’s wage wtw\_{t} collected. Additionally, the decision variables xn,tx\_{n,t} represent the amount of money invested in asset nn at tt, while ξn,t\xi\_{n,t} is the return of asset nn in tt​ht^{th} moment. The value of assets held by the fund at tt is represented by AtA\_{t}, while the liabilities at that moment, which are payments made by the fund to retirees, are denoted by ltl\_{t}. The present value of liabilities at tt is given by LtL\_{t}, which is calculated by ∑t=0Tlt(1+γ)t,∀t=0,…,T\sum\_{t=0}^{T}\frac{l\_{t}}{(1+\gamma)^{t}},\;\forall t=0,\dots,T. It is worth noting that in our study, benefit payments and liabilities are fixed and predefined, which classifies this type of pension fund as a *defined-benefit plan*. The discount rate, γ\gamma, for the calculation of the present value of liabilities is a random variable. The funding ratio, a crucial parameter in the ALM problem, ensures that the ratio of assets owned by the fund to the present value of liabilities at tt is maintained above a minimum threshold ψ\psi. This means that the fund has sufficient resources to meet its future obligations. Model ([1](https://arxiv.org/html/2602.08228v1#S2.E1 "Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) shows the mathematical formulation of the ALM problem:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | minyt,xn,t\displaystyle\min\_{y\_{t},x\_{n,t}}\quad | h​(y1,…,yT),\displaystyle{h(y\_{1},\dots,y\_{T})}, |  | | (1a) |
|  | s.t. | ∑n=0Nxn,t=At+wt​yt−lt,\displaystyle\sum\_{n=0}^{N}{x\_{n,t}}=A\_{t}+w\_{t}y\_{t}-l\_{t},\quad | t=0,…,T−1,\displaystyle t=0,\dots,T-1, |  | (1b) |
|  |  | At≥ψ​Lt,\displaystyle A\_{t}\geq\psi L\_{t},\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | (1c) |
|  |  | At=∑n=0Nxn,t−1​(1+ξn,t),\displaystyle A\_{t}=\sum\_{n=0}^{N}{x\_{n,t-1}}(1+\xi\_{n,t}),\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | (1d) |
|  |  | xn,t∈𝒳,yt∈𝒴,\displaystyle x\_{n,t}\in\mathcal{X},y\_{t}\in\mathcal{Y},\quad | t=0,…,T,n=0,…,N.\displaystyle t=0,\dots,T,n=0,\dots,N. |  | (1e) |

The objective function of the ALM problem ([1](https://arxiv.org/html/2602.08228v1#S2.E1 "Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), introduced by Bogentoft et al. ([2001](https://arxiv.org/html/2602.08228v1#bib.bib1 "Asset/liability management for pension funds using cvar constraints")), is denoted by h​(y1,…,yT)h(y\_{1},\dots,y\_{T}), which is a function defined in terms of the contribution rate and plays a crucial role in determining the optimal ALM strategy. In particular, the objective function ([1a](https://arxiv.org/html/2602.08228v1#S2.E1.1 "Equation 1a ‣ Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) can be defined as the present value of all contributions, i.e., h​(y1,…,yT)=∑t=1TWt​yth(y\_{1},\dots,y\_{T})=\sum\_{t=1}^{T}W\_{t}y\_{t}, where Wt=wt(1+γ)tW\_{t}=\frac{w\_{t}}{(1+\gamma)^{t}}. The balance constraint ([1b](https://arxiv.org/html/2602.08228v1#S2.E1.2 "Equation 1b ‣ Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) ensures
that the sum of all investments at tt is equal to the assets held by the fund plus the contributions gathered at tt minus liabilities in that period. The funding ratio constraint ([1c](https://arxiv.org/html/2602.08228v1#S2.E1.3 "Equation 1c ‣ Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) guarantees that the ratio of assets owned by the fund to the present value of liabilities at tt is greater than equal to a minimum threshold ψ\psi. Constraint ([1d](https://arxiv.org/html/2602.08228v1#S2.E1.4 "Equation 1d ‣ Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) describes how to calculate the value of assets owned by the fund at tt as a function of their values at (t−1)(t-1) and the return rates, ξn,t\xi\_{n,t}.
Any regulatory or practical (e.g., nonnegativity) restrictions on the investment strategy and the contribution rates are encapsulated in the sets 𝒳\mathcal{X} and 𝒴\mathcal{Y}, respectively, and are enforced by constraint ([1e](https://arxiv.org/html/2602.08228v1#S2.E1.5 "Equation 1e ‣ Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")). Moreover, A0A\_{0}, w0w\_{0}, y0y\_{0}, l0l\_{0}, and xn,0x\_{n,0} represent the initial values of variables in the current period (t=0t=0) of the fund capital, employees’ wages, contribution rate, liabilities, and asset holdings, respectively. These parameters signify the starting condition of the fund, assumed to be known to the decision-maker.

To simplify the formulation, we express the objective function of model ([1](https://arxiv.org/html/2602.08228v1#S2.E1 "Equation 1 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) using the vectors W=[W1,…,WT]⊺∈ℝT\mathrm{W}=[W\_{1},\dots,W\_{T}]^{\intercal}\in\mathbb{R}^{T} and y=[y1,…,yT]⊺∈ℝT\mathrm{y}=[y\_{1},\dots,y\_{T}]^{\intercal}\in\mathbb{R}^{T}, which represent the present value of the contributors’ wages and the contribution rate decision variables, respectively. The objective function can then be written as W⊺​y\mathrm{W}^{\intercal}\mathrm{y}.
We also introduce the vector rt=e+ξt\mathrm{r}\_{t}=\mathrm{e}+\upxi\_{t} for t=1,…,Tt=1,\dots,T, where e\mathrm{e} is an all-ones vector of size N+1N+1 and ξt\upxi\_{t} is an uncertain vector that captures the variation in the plan’s funding status. Additionally, we define the investment decision variable as a vector xt=[x0,t,…,xn,t]⊺\mathrm{x}\_{t}=[x\_{0,t},\dots,x\_{n,t}]^{\intercal} for each tt.
Using these notations, we can transform the ALM problem ([2](https://arxiv.org/html/2602.08228v1#S2.E2 "Equation 2 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) into a vector representation as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | miny,xt\displaystyle\min\_{\mathrm{y},\mathrm{x}\_{t}}\quad | W⊺​y,\displaystyle\mathrm{W}^{\intercal}\mathrm{y}, |  | | (2a) |
|  | s.t. | e⊺​xt=rt⊺​xt−1+wt​yt−lt,\displaystyle\mathrm{e}^{\intercal}\mathrm{x}\_{t}=\mathrm{r}\_{t}^{\intercal}\mathrm{x}\_{t-1}+w\_{t}y\_{t}-l\_{t},\quad | t=1,…,T−1,\displaystyle t=1,\dots,T-1, |  | (2b) |
|  |  | rt⊺​xt−1≥ψ​Lt,\displaystyle\mathrm{r}\_{t}^{\intercal}\mathrm{x}\_{t-1}\geq\psi L\_{t},\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | (2c) |
|  |  | xt∈𝒳,y∈𝒴\displaystyle\mathrm{x}\_{t}\in\mathcal{X},\mathrm{y}\in\mathcal{Y}\quad | t=1,…,T.\displaystyle t=1,\dots,T. |  | (2d) |

The deterministic model ([2](https://arxiv.org/html/2602.08228v1#S2.E2 "Equation 2 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) operates under the assumption of complete knowledge of all parameter values, such as the assets’ rates of return ξt\upxi\_{t}, and the discount rate γ\gamma, which dictates the present value of future liabilities LtL\_{t}. However, this assumption is unrealistic as these variables are inherently random.
To ensure the robustness of the model, it is important to account for the uncertainty associated with these parameters. In the following section, we present a DRO reformulation of ([2](https://arxiv.org/html/2602.08228v1#S2.E2 "Equation 2 ‣ 2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) to address this issue.

## 3 Distributionally Robust ALM

Before providing the DRO formulation, we begin by presenting a scenario-based SP formulation of the ALM problem. As previously discussed, the present value of wages, W\mathrm{W}, and the present value of future liabilities, LtL\_{t}, are both influenced by the uncertain discount rate, while all other parameters affecting them are assumed deterministic. As a result, they are perfectly correlated and thus can both be represented using a single set of discrete scenarios {s}s=1,…,S\{s\}\_{s=1,\dots,S} having a given distribution function p(.)p(.). Likewise, we use a finite set of scenarios {k}k=1,…,K\{k\}\_{k=1,\dots,K}, having the discrete distribution function q(.)q(.), to capture the uncertainty of asset returns. With that, model ([3](https://arxiv.org/html/2602.08228v1#S3.E3 "Equation 3 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) presents an SP formulation of the ALM based on these scenario sets and distribution functions. Note that the additional subscript (ss or kk) for the uncertain parameters denotes the scenario.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | miny,xt\displaystyle\min\_{\mathrm{y},\mathrm{x}\_{t}}\quad | 𝔼p​(Ws⊺​y),\displaystyle\mathbb{E}\_{p}(\mathrm{W}\_{s}^{\intercal}\mathrm{y}), |  | | (3a) |
|  | s.t. | e⊺​xt=𝔼q​(rt,k⊺​xt−1)+wt​yt−lt,\displaystyle\mathrm{e}^{\intercal}\mathrm{x}\_{t}=\mathbb{E}\_{q}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})+w\_{t}y\_{t}-l\_{t},\quad | t=1,…,T−1,\displaystyle t=1,\dots,T-1, |  | (3b) |
|  |  | 𝔼q​(rt,k⊺​xt−1)≥ψ​𝔼p​(Lt,s),\displaystyle\mathbb{E}\_{q}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})\geq\psi\mathbb{E}\_{p}(L\_{t,s}),\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | (3c) |
|  |  | xt∈𝒳,y∈𝒴\displaystyle\mathrm{x}\_{t}\in\mathcal{X},\mathrm{y}\in\mathcal{Y}\quad | t=1,…,T.\displaystyle t=1,\dots,T. |  | (3d) |

In model ([3](https://arxiv.org/html/2602.08228v1#S3.E3 "Equation 3 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), it is essential to have comprehensive knowledge of the distribution functions for accurate analysis and decision-making. This requirement arises due to the significant impact of uncertainty in the problem domain.
Additionally, the tractability of this problem is closely linked to the number of scenarios considered. As the number of scenarios increases, the complexity of the problem grows exponentially. Consequently, the computational burden and resource requirements for solving the problem also increase. Therefore, carefully considering the number of scenarios is crucial to balance accuracy and computational feasibility in tackling the model, which is a major limitation of this SP formulation.

However, in reality, these distribution functions may not be fully known, and therefore, we propose DRO as an alternative to SP for the ALM problem since the former does not require exact knowledge of the probability distributions. Moreover, DRO provides a robust solution by accounting for a range of possible different distributions, which enables decision-makers to hedge against various plausible distributional scenarios, leading to more reliable and stable solutions that are less sensitive to uncertain input parameters.
Consequently, we assume that the distribution functions belong to the sets that represent a range of possible probability distributions, called ambiguity sets.
Let PP and QQ be ambiguity sets for the distribution functions of asset return and discount rate, respectively. Then, the DRO formulation of the ALM is presented in model ([4](https://arxiv.org/html/2602.08228v1#S3.E4 "Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")):

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | miny,xt​supp∈P\displaystyle\min\_{\mathrm{y},\mathrm{x}\_{t}}\sup\_{p\in P}\quad | 𝔼p​(Ws⊺​y),\displaystyle\mathbb{E}\_{p}(\mathrm{W}\_{s}^{\intercal}\mathrm{y}), |  | | (4a) |
|  | s.t. | e⊺​xt=infq∈Q𝔼q​(rt,k⊺​xt−1)+wt​yt−lt,\displaystyle\mathrm{e}^{\intercal}\mathrm{x}\_{t}=\inf\_{q\in Q}\mathbb{E}\_{q}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})+w\_{t}y\_{t}-l\_{t},\quad | t=1,…,T−1,\displaystyle t=1,\dots,T-1, |  | (4b) |
|  |  | infq∈Q𝔼q​(rt,k⊺​xt−1)≥ψ​supp∈P𝔼p​(Lt,s),\displaystyle\inf\_{q\in Q}\mathbb{E}\_{q}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})\geq\psi\sup\_{p\in P}\mathbb{E}\_{p}(L\_{t,s}),\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | (4c) |
|  |  | xt∈𝒳,y∈𝒴\displaystyle\mathrm{x}\_{t}\in\mathcal{X},\mathrm{y}\in\mathcal{Y}\quad | t=1,…,T.\displaystyle t=1,\dots,T. |  | (4d) |

Model ([4](https://arxiv.org/html/2602.08228v1#S3.E4 "Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is based on the worst-case expected value of random variables.
For the remainder of the paper, we will explore various ambiguity sets that can be applied to the formulation presented in the model ([4](https://arxiv.org/html/2602.08228v1#S3.E4 "Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")).

### 3.1 Mixture Distribution

We are dealing with ambiguous discrete distribution functions, Whereas the scenarios themselves are deterministically defined. One approach to address this ambiguity of the distribution function is to use a set to represent the possible discrete distribution function. It is common to consider uncertain discrete distributions in portfolio selection problems (for more details, see Costa and Paiva ([2002](https://arxiv.org/html/2602.08228v1#bib.bib3 "Robust portfolio selection using linear-matrix inequalities")), Ghaoui et al. ([2003](https://arxiv.org/html/2602.08228v1#bib.bib4 "Worst-case value-at-risk and robust portfolio optimization: a conic programming approach")), Ghahtarani et al. ([2022](https://arxiv.org/html/2602.08228v1#bib.bib5 "Robust portfolio selection problems: a comprehensive review"))).
In this case, the ambiguity set is considered a mixture of predetermined likelihood distributions. Based on Zhu and Fukushima ([2009](https://arxiv.org/html/2602.08228v1#bib.bib37 "Worst-case conditional value-at-risk with application to robust portfolio management")),
these ambiguity sets are defined as PM:={p:p=∑i=1Iλi​pi;∑i=1Iλi=1;λi≥0;i=1,…,I}P\_{M}:=\left\{p:p=\sum\_{i=1}^{I}\lambda\_{i}p^{i};\sum\_{i=1}^{I}\lambda\_{i}=1;\lambda\_{i}\geq 0;i=1,\dots,I\right\}, where pip^{i} is the it​hi^{th} likelihood distribution and II is the number of likelihood distributions.

Likewise, QM:={q:q=∑j=1Jλjqj;∑j=1Jλj=1;λj≥0,;j=1,…,J}Q\_{M}:=\left\{q:q=\sum\_{j=1}^{J}\lambda\_{j}q^{j};\sum\_{j=1}^{J}\lambda\_{j}=1;\lambda\_{j}\geq 0,;j=1,\dots,J\right\}, where qjq^{j} is the jt​hj^{th} likelihood distribution and JJ is the number of likelihood distributions.
Although the ambiguity set PMP\_{M} includes all convex combinations of the II likelihood distributions pi,i=1,…,Ip^{i},\;i=1,\dots,I, it is easy to show that the worst-case distribution for any given values of the decision variables is one of II likelihood distributions themselves. This *maximal solution* property is due to the fact that finding the worst-case distribution is analogous to solving a binary knapsack problem with unit-sized items and a knapsack capacity of 1, where only one item (having the highest value) is selected. A similar argument can be made for the ambiguity set QMQ\_{M}, though with the lowest value item selected. Thus, to reformulate model ([4](https://arxiv.org/html/2602.08228v1#S3.E4 "Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) with the mentioned ambiguity sets, we introduce the auxiliary variables θ\theta, μt\mu\_{t}, and ωt\omega\_{t}, where θ≥∑s=1S(Ws⊺​y)​psi\theta\geq\sum\_{s=1}^{S}({\mathrm{W}\_{s}^{\intercal}\mathrm{y})p\_{s}^{i}}, μt≤∑k=1K(rt,k⊺​xt−1)​qkj\mu\_{t}\leq\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})q\_{k}^{j}, and ωt≥∑s=1SLt,s​psi\omega\_{t}\geq\sum\_{s=1}^{S}{L\_{t,s}p\_{s}^{i}}.
Using these ambiguity sets and auxiliary variables, the DRO problem can be written in the epigraph form as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | miny,xt,θ,μt,ωt\displaystyle\min\_{\mathrm{y},\mathrm{x}\_{t},\theta,\mu\_{t},\omega\_{t}}\quad | θ,\displaystyle{\theta}, |  | | (5a) |
|  | s.t. | θ≥∑s=1S(Ws⊺​y)​psi,\displaystyle\theta\geq\sum\_{s=1}^{S}{(\mathrm{W}\_{s}^{\intercal}\mathrm{y})p\_{s}^{i}},\quad | i=1,…,I,\displaystyle i=1,\dots,I, |  | (5b) |
|  |  | e⊺​xt=μt+wt​yt−lt,\displaystyle\mathrm{e}^{\intercal}\mathrm{x}\_{t}=\mu\_{t}+w\_{t}y\_{t}-l\_{t},\quad | t=1,…,T−1,\displaystyle t=1,\dots,T-1, |  | (5c) |
|  |  | μt≥ψ​ωt,\displaystyle\mu\_{t}\geq\psi\omega\_{t},\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | (5d) |
|  |  | μt≤∑k=1K(rt,k⊺​xt−1)​qkj\displaystyle\mu\_{t}\leq\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})q\_{k}^{j}\quad | t=1,…,T,j=1,…,J,\displaystyle t=1,\dots,T,j=1,\dots,J, |  | (5e) |
|  |  | ωt≥∑s=1SLt,s​psi,\displaystyle\omega\_{t}\geq\sum\_{s=1}^{S}{L\_{t,s}p\_{s}^{i}},\quad | t=1,…,T,i=1,…,I,\displaystyle t=1,\dots,T,i=1,\dots,I, |  | (5f) |
|  |  | xt∈𝒳,y∈𝒴\displaystyle\mathrm{x}\_{t}\in\mathcal{X},\mathrm{y}\in\mathcal{Y}\quad | t=1,…,T.\displaystyle t=1,\dots,T. |  | (5g) |

Model ([5](https://arxiv.org/html/2602.08228v1#S3.E5 "Equation 5 ‣ 3.1 Mixture Distribution ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is a linear programming model, which is a tractable model and captures the ambiguity of discrete distribution functions.

### 3.2 Discrete Distribution with Box Ambiguity

The mixture-distribution ambiguity set proposed in subsection [3.1](https://arxiv.org/html/2602.08228v1#S3.SS1 "3.1 Mixture Distribution ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") has two main drawbacks. First, it confines the ambiguity about the discrete probability distributions to finite sets of elements (distribution functions) and their convex combinations while ignoring the possibility that the true distribution functions can take other forms. Although this issue can be partially alleviated by increasing the value of II, i.e., using a large number of distribution functions that cover a wider range of possibilities, the problem size inevitably grows, thus reducing its tractability, which is the second drawback. Alternatively, a box ambiguity set can be used for the discrete distribution function, which provides does not need a large number of possible distribution functions in a convex set.
Note that for ambiguity sets of discrete distributions, model ([4](https://arxiv.org/html/2602.08228v1#S3.E4 "Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) can be expanded to:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | miny,xt​supp∈P\displaystyle\min\_{\mathrm{y},\mathrm{x}\_{t}}\sup\_{p\in P}\quad | ∑s=1S(Ws⊺​y)​ps,\displaystyle\sum\_{s=1}^{S}(\mathrm{W}\_{s}^{\intercal}\mathrm{y})p\_{s}, |  | | (6a) |
|  | s.t. | e⊺​xt=infq∈Q∑k=1K(rt,k⊺​xt−1)​qk+wt​yt−lt,\displaystyle\mathrm{e}^{\intercal}\mathrm{x}\_{t}=\inf\_{q\in Q}\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})q\_{k}+w\_{t}y\_{t}-l\_{t},\quad | t=1,…,T−1,\displaystyle t=1,\dots,T-1, |  | (6b) |
|  |  | infq∈Q∑k=1K(rt,k⊺​xt−1)​qk≥ψ​supp∈P∑s=1S(Lt,s)​ps,\displaystyle\inf\_{q\in Q}\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})q\_{k}\geq\psi\sup\_{p\in P}\sum\_{s=1}^{S}(L\_{t,s})p\_{s},\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | (6c) |
|  |  | xt∈𝒳,y∈𝒴\displaystyle\mathrm{x}\_{t}\in\mathcal{X},\mathrm{y}\in\mathcal{Y}\quad | t=1,…,T.\displaystyle t=1,\dots,T. |  | (6d) |

In model ([6](https://arxiv.org/html/2602.08228v1#S3.E6 "Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), we are dealing with two ambiguity sets PP and QQ that contain probability distributions of the random variables. Specifically, p​(⋅)∈Pp(\cdot)\in P, which is defined as P:={p:ps=ps0+ηs:∑s=1Sηs=0,η¯s≤ηs≤η¯s}P:=\{p:p\_{s}=p\_{s}^{0}+\eta\_{s}:\sum\_{s=1}^{S}\eta\_{s}=0,\underline{\eta}\_{s}\leq\eta\_{s}\leq\overline{\eta}\_{s}\}, where ps0p\_{s}^{0} is the nominal probability of scenario ss, and ηs∈[η¯s,η¯s]\eta\_{s}\in[\underline{\eta}\_{s},\overline{\eta}\_{s}] is a bounded perturbation from it. Likewise, q​(⋅)∈Qq(\cdot)\in Q, which is defined as Q:={q(.):qk=qk0+ξk:∑k=1Kξk=0,ξ¯k≤ξk≤ξ¯k}Q:=\{q(.):q\_{k}=q\_{k}^{0}+\xi\_{k}:\sum\_{k=1}^{K}\xi\_{k}=0,\underline{\xi}\_{k}\leq\xi\_{k}\leq\overline{\xi}\_{k}\}, where qk0q\_{k}^{0} is the nominal probability of scenario kk, while ξk∈[ξ¯k,ξ¯k]\xi\_{k}\in[\underline{\xi}\_{k},\overline{\xi}\_{k}].

To reformulate model ([6](https://arxiv.org/html/2602.08228v1#S3.E6 "Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), we apply LP duality to the inner problems. Specifically, the inner problem of the uncertain objective function ([6a](https://arxiv.org/html/2602.08228v1#S3.E6.1 "Equation 6a ‣ Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) can be expressed as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | maxηs\displaystyle\max\_{\eta\_{s}}\quad | ∑s=1S(Ws⊺​y)​(ps0+ηs),\displaystyle{\sum\_{s=1}^{S}(\mathrm{W}\_{s}^{\intercal}\mathrm{y})(p^{0}\_{s}+\eta\_{s})}, |  | | (7a) |
|  | s.t. | ∑s=1Sηs=0,\displaystyle\sum\_{s=1}^{S}\eta\_{s}=0,\quad | (z),\displaystyle\quad(z), |  | (7b) |
|  |  | ηs≤η¯s,\displaystyle\eta\_{s}\leq\overline{\eta}\_{s},\quad | s=1,…,S,(ds+),\displaystyle\quad s=1,\dots,S,\;\;\;\;\;(d\_{s}^{+}), |  | (7c) |
|  |  | −ηs≤−η¯s,\displaystyle-\eta\_{s}\leq-\underline{\eta}\_{s},\quad | s=1,…,S,(ds−),\displaystyle\quad s=1,\dots,S,\;\;\;\;\;(d\_{s}^{-}), |  | (7d) |

where zz, ds+d\_{s}^{+}, and ds−d\_{s}^{-} are the dual variables of their respective constraints. Problem ([7](https://arxiv.org/html/2602.08228v1#S3.E7 "Equation 7 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) aims to optimize over the perturbation parameters ηs\eta\_{s}. Thus, the dual form of model ([7](https://arxiv.org/html/2602.08228v1#S3.E7 "Equation 7 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) can be written as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | ∑s=1S(Ws⊺​y)​ps0+minds+≥0,ds−≥0,z\displaystyle\sum\_{s=1}^{S}(\mathrm{W}\_{s}^{\intercal}\mathrm{y})p^{0}\_{s}+\min\_{d\_{s}^{+}\geq 0,d\_{s}^{-}\geq 0,z}\quad | ∑s=1S(ds+​η¯s−ds−​η¯s),\displaystyle{\sum\_{s=1}^{S}{(d\_{s}^{+}\overline{\eta}\_{s}-d\_{s}^{-}\underline{\eta}\_{s}})}, |  | | (8a) |
|  | s.t. | z+ds+−ds−≥Ws⊺​y,\displaystyle z+d\_{s}^{+}-d\_{s}^{-}\geq\mathrm{W}\_{s}^{\intercal}\mathrm{y},\quad | s=1,…,S.\displaystyle s=1,\dots,S. |  | (8b) |

Likewise, constraints ([6b](https://arxiv.org/html/2602.08228v1#S3.E6.2 "Equation 6b ‣ Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) and ([6c](https://arxiv.org/html/2602.08228v1#S3.E6.3 "Equation 6c ‣ Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) involve the inner optimization of uncertain parameters related to asset returns. Specifically, this inner optimization can be expressed as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | minξk\displaystyle\min\_{\xi\_{k}}\quad | ∑k=1K(rt,k⊺​xt−1)​(qk0+ξk),\displaystyle{\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})(q^{0}\_{k}+\xi\_{k})}, |  | | (9a) |
|  | s.t. | ∑k=1Kξk=0,\displaystyle\sum\_{k=1}^{K}\xi\_{k}=0,\quad | (Γ),\displaystyle\quad(\Gamma), |  | (9b) |
|  |  | −ξ¯k≤−ξk,\displaystyle-\overline{\xi}\_{k}\leq-\xi\_{k},\quad | k=1,…,K,(ωk+),\displaystyle\quad k=1,\dots,K,\;\;\;\;\;(\omega\_{k}^{+}), |  | (9c) |
|  |  | ξ¯k≤ξk,\displaystyle\underline{\xi}\_{k}\leq\xi\_{k},\quad | k=1,…,K,(ωk−),\displaystyle\quad k=1,\dots,K,\;\;\;\;\;(\omega\_{k}^{-}), |  | (9d) |

where Γ\Gamma, ωk+\omega\_{k}^{+}, and ωk−\omega\_{k}^{-} are dual variables. The problem described in ([9](https://arxiv.org/html/2602.08228v1#S3.E9 "Equation 9 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) optimizes over the perturbation variables ξk\xi\_{k}. To achieve this goal, the objective function ([9a](https://arxiv.org/html/2602.08228v1#S3.E9.1 "Equation 9a ‣ Equation 9 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is reformulated as ∑k=1K(rt,k⊺​xt−1)​q0+minξk​∑k=1K(rt,k⊺​xt−1)​ξk\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})q^{0}+\min\_{\xi\_{k}}{\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})\xi\_{k}}, which expresses the minimum value of the linear combination ∑k=1K(rt,k⊺​xt−1)​ξk\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})\xi\_{k} over all possible values of ξk\xi\_{k}. The dual form of the model presented in ([9](https://arxiv.org/html/2602.08228v1#S3.E9 "Equation 9 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) can be expressed as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | ∑k=1K(rt,k⊺​xt−1)​q0+maxωk+≥0,ωk−≥0,Γ\displaystyle\sum\_{k=1}^{K}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})q^{0}+\max\_{\omega\_{k}^{+}\geq 0,\omega\_{k}^{-}\geq 0,\Gamma}\quad | ∑k=1K(ωk−​ξ¯k−ωk+​ξ¯k),\displaystyle{\sum\_{k=1}^{K}{(\omega\_{k}^{-}\underline{\xi}\_{k}-\omega\_{k}^{+}\overline{\xi}\_{k}})}, |  | | (10a) |
|  | s.t. | Γ+ωk−−ωk+≤rt,k⊺​xt−1,\displaystyle\Gamma+\omega\_{k}^{-}-\omega\_{k}^{+}\leq\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1},\quad | k=1,…,K.\displaystyle k=1,\dots,K. |  | (10b) |

Finally, the inner optimization model related to uncertainty of Lt,sL\_{t,s} for each tt in constraint ([6c](https://arxiv.org/html/2602.08228v1#S3.E6.3 "Equation 6c ‣ Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | maxηs\displaystyle\max\_{\eta\_{s}}\quad | ∑s=1SLt​s​(ps0+ηs),\displaystyle{\sum\_{s=1}^{S}{L\_{ts}}(p^{0}\_{s}+\eta\_{s})}, |  | | (11a) |
|  | s.t. | ∑s=1Sηs=0,\displaystyle\sum\_{s=1}^{S}\eta\_{s}=0,\quad | (z),\displaystyle\quad(z), |  | (11b) |
|  |  | ηs≤η¯s,\displaystyle\eta\_{s}\leq\overline{\eta}\_{s},\quad | s=1,…,S,(ds+),\displaystyle\quad s=1,\dots,S,\;\;\;\;\;(d\_{s}^{+}), |  | (11c) |
|  |  | −ηs≤−η¯s,\displaystyle-\eta\_{s}\leq-\underline{\eta}\_{s},\quad | s=1,…,S,(ds−).\displaystyle\quad s=1,\dots,S,\;\;\;\;\;(d\_{s}^{-}). |  | (11d) |

The optimization problem ([11](https://arxiv.org/html/2602.08228v1#S3.E11 "Equation 11 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is over ηs\eta\_{s}. Then the objective function ([11a](https://arxiv.org/html/2602.08228v1#S3.E11.1 "Equation 11a ‣ Equation 11 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is transformed to ∑s=1SLt​s​ps0+maxηs​∑s=1SLt​s​ηs\sum\_{s=1}^{S}{L\_{ts}}{p^{0}\_{s}}+\max\_{\eta\_{s}}{\sum\_{s=1}^{S}{L\_{ts}}\eta\_{s}}.
The dual form of model ([11](https://arxiv.org/html/2602.08228v1#S3.E11 "Equation 11 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) for each tt is as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | ∑s=1SLt​s​ps0+minds+≥0,ds−≥0,z\displaystyle\sum\_{s=1}^{S}{L\_{ts}}{p^{0}\_{s}}+\min\_{d\_{s}^{+}\geq 0,d\_{s}^{-}\geq 0,z}\quad | ∑s=1S(ds+​η¯s−ds−​η¯s),\displaystyle{\sum\_{s=1}^{S}{(d\_{s}^{+}\overline{\eta}\_{s}-d\_{s}^{-}\underline{\eta}\_{s}})}, |  | | (12a) |
|  | s.t. | z+ds+−ds−≥Lt,s,\displaystyle z+d\_{s}^{+}-d\_{s}^{-}\geq L\_{t,s},\quad | s=1,…,S.\displaystyle s=1,\dots,S. |  | (12b) |

The DRO of the ALM model with box ambiguity set can be formulated by substituting the dual forms of the optimization problems ([8](https://arxiv.org/html/2602.08228v1#S3.E8 "Equation 8 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), ([10](https://arxiv.org/html/2602.08228v1#S3.E10 "Equation 10 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), and ([12](https://arxiv.org/html/2602.08228v1#S3.E12 "Equation 12 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) into the original optimization problem expressed in ([6](https://arxiv.org/html/2602.08228v1#S3.E6 "Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")). The resulting final formulation is as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | miny,xt,ds+≥0,ds−,ωk+,ωk−≥0,Γ,z\displaystyle\min\_{\mathrm{y},\mathrm{x}\_{t},d\_{s}^{+}\geq 0,d\_{s}^{-},\omega\_{k}^{+},\omega\_{k}^{-}\geq 0,\Gamma,z}\quad | ∑s=1S(Ws⊺​y)​ps0+∑s=1S(ds+​η¯s−ds−​η¯s),\displaystyle{\sum\_{s=1}^{S}\left(\mathrm{W}\_{s}^{\intercal}\mathrm{y}\right)p^{0}\_{s}}+\sum\_{s=1}^{S}{\left(d\_{s}^{+}\overline{\eta}\_{s}-d\_{s}^{-}\underline{\eta}\_{s}\right)}, |  | | (13a) |
|  | | | | | |
|  | s.t. | e⊺​xt=∑k=1K(rt,k⊺​xt−1)​qk0+∑k=1K(ωk−​ξ¯k−ωk+​ξ¯k)+\displaystyle\mathrm{e}^{\intercal}\mathrm{x}\_{t}=\sum\_{k=1}^{K}\left(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1}\right)q^{0}\_{k}+\sum\_{k=1}^{K}\left(\omega\_{k}^{-}\underline{\xi}\_{k}-\omega\_{k}^{+}\overline{\xi}\_{k}\right)+ |  | |
|  |  | wt​yt−lt,\displaystyle w\_{t}y\_{t}-l\_{t},\quad | t=1,…,T−1,\displaystyle t=1,\dots,T-1, |  | (13b) |
|  | | | | | |
|  | ∑k=1K(rt,k⊺​xt−1)​qk0+∑k=1K(ωk−​ξ¯k−ωk+​ξ¯k)≥\displaystyle\sum\_{k=1}^{K}\left(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1}\right)q\_{k}^{0}+\sum\_{k=1}^{K}{\left(\omega\_{k}^{-}\underline{\xi}\_{k}-\omega\_{k}^{+}\overline{\xi}\_{k}\right)}\geq |  | | |
|  | ψ​(∑s=1SLt,s​ps0+∑s=1S(ds+​η¯s−ds−​η¯s)),\displaystyle\psi\left(\sum\_{s=1}^{S}{L\_{t,s}p^{0}\_{s}}+\sum\_{s=1}^{S}{\left(d\_{s}^{+}\overline{\eta}\_{s}-d\_{s}^{-}\underline{\eta}\_{s}\right)}\right),\quad | t=1,…,T,\displaystyle t=1,\dots,T, |  | | (13c) |
|  | | | | | |
|  | z+ds+−ds−≥Ws⊺​y,\displaystyle z+d\_{s}^{+}-d\_{s}^{-}\geq\mathrm{W}\_{s}^{\intercal}\mathrm{y},\quad | s=1,…,S,\displaystyle s=1,\dots,S, |  | | (13d) |
|  | Γ+ωk−−ωk+≤rt,k⊺​xt−1\displaystyle\Gamma+\omega\_{k}^{-}-\omega\_{k}^{+}\leq\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1}\quad | t=1,…,T,k=1,…,K,\displaystyle t=1,\dots,T,k=1,\dots,K, |  | | (13e) |
|  | z+ds+−ds−≥Lt,s\displaystyle z+d\_{s}^{+}-d\_{s}^{-}\geq L\_{t,s}\quad | t=1,…,T,s=1,…,S.\displaystyle t=1,\dots,T,s=1,\dots,S. |  | | (13f) |

Problem ([13](https://arxiv.org/html/2602.08228v1#S3.E13 "Equation 13 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is the tractable reformulation of ([6](https://arxiv.org/html/2602.08228v1#S3.E6 "Equation 6 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) with box ambiguity sets.

### 3.3 Wasserstein Ambiguity Set

An ambiguity set that has drawn a lot of attention recently due to its favorable properties (i.e., finite sample guarantee, asymptotic consistency, and tractability) is that based on the Wasserstein metric (Mohajerin Esfahani and Kuhn, [2018](https://arxiv.org/html/2602.08228v1#bib.bib12 "Data-driven distributionally robust optimization using the wasserstein metric: performance guarantees and tractable reformulations")). Unlike the mixture-distribution and box ambiguity sets utilized earlier, which consider only distributions that are supported on the same support set of the empirical distribution (i.e., use the same set of scenarios), the Wasserstein ambiguity set includes all distributions, discrete or continuous, that are sufficiently close to the empirical distribution.
Thus, it offers higher flexibility and a more realistic representation of the uncertainty of the random problem parameters. In other words, we do not only consider the “original” scenarios on which the empirical distribution is supported, but also other scenarios not seen before.

The Wasserstein ambiguity set can be constructed using the discrete empirical probability distribution p^=1S​∑s∈SδW^s\hat{p}=\frac{1}{S}\sum\_{s\in S}{\delta\_{\hat{\mathrm{W}}\_{s}}},
where δ\delta is an indicator function that takes the value 1 for elements of the discrete set of scenarios Ξ^W:=W^1,…,W^s⊂ΞW\hat{\Xi}\_{\mathrm{W}}:={\hat{\mathrm{W}}\_{1},...,\hat{\mathrm{W}}\_{s}}\subset\Xi\_{\mathrm{W}} and 0 elsewhere. Specifically, the ambiguity set is defined as D​(p^,ϵ1)={p∈M∣P​(W^∈ΞW)=1,d​w​(p^,p)≤ϵ1}D(\hat{p},\epsilon^{1})=\{p\in M\mid\begin{matrix}P(\hat{\mathrm{W}}\in\Xi\_{\mathrm{W}})=1,\ dw(\hat{p},p)\leq\epsilon^{1}\end{matrix}\}, where d​w​(p^,p)dw(\hat{p},p) is the Wasserstein distance between the discrete empirical distribution p^\hat{p} and a probability distribution pp, and ϵ1\epsilon^{1} is the radius of the ambiguity set. This ambiguity set is designed to capture a range of probability distributions within a certain distance of the empirical distribution.
Similarly, the ambiguity set for the vector of asset returns random variables 𝐫t\mathbf{r}\_{t}, denoted as D​(q^t,ϵt2)D(\hat{q}\_{t},\epsilon\_{t}^{2}), is constructed using the discrete empirical probability distribution q^t=1K​∑k∈Kδr^t\hat{q}\_{t}=\frac{1}{K}\sum\_{k\in K}{\delta\_{\hat{\mathrm{r}}\_{t}}}. Here, Ξ^rt:=r^t,1,…,r^t,k⊂Ξrt;∀t\hat{\Xi}\_{\mathrm{r}\_{t}}:={\hat{\mathrm{r}}\_{t,1},...,\hat{\mathrm{r}}\_{t,k}}\subset\Xi\_{\mathrm{r}\_{t}};\forall t is the set of empirical realizations of the vector of random variables 𝐫t\mathbf{r}\_{t}. The ambiguity set D​(q^t,ϵt2)D(\hat{q}\_{t},\epsilon\_{t}^{2}) is defined as D​(q^t,ϵt2)={qt∈M∣P​(rt^∈Ξ​rt)=1,d​w​(q^t,qt)≤ϵt2}D(\hat{q}\_{t},\epsilon\_{t}^{2})=\{q\_{t}\in M\mid\begin{matrix}P(\hat{\mathrm{r}\_{t}}\in\Xi{\mathrm{r}\_{t}})=1,\;\ dw(\hat{q}\_{t},q\_{t})\leq\epsilon\_{t}^{2}\end{matrix}\}, where d​w​(q^t,qt)dw(\hat{q}\_{t},q\_{t}) is the Wasserstein distance between the discrete empirical distribution q^t\hat{q}\_{t} and the probability distribution qtq\_{t}, and ϵt2\epsilon\_{t}^{2} is the radius of the ambiguity set.
To calculate the Wasserstein distance between two probability metrics q1q\_{1} and q2q\_{2}, we use the integral representation dw(q1,q2)=∫Ξ2||ξ1,ξ2||Q(dξ1,dξ2)dw(q\_{1},q\_{2})=\int\_{\Xi^{2}}||\xi\_{1},\xi\_{2}||Q(d\xi\_{1},d\xi\_{2}), where QQ is the joint distribution of ξ1\xi\_{1} and ξ2\xi\_{2} with marginal probabilities q1q\_{1} and q2q\_{2}, respectively. This distance measure is used to capture the similarity between two probability distributions, where a smaller Wasserstein distance corresponds to a higher similarity between the distributions.
Based on Mohajerin Esfahani and Kuhn ([2018](https://arxiv.org/html/2602.08228v1#bib.bib12 "Data-driven distributionally robust optimization using the wasserstein metric: performance guarantees and tractable reformulations")), under a convexity condition of the support set ΞW:={ℂ​W≤d}\Xi\_{\mathrm{W}}:=\{\mathbb{C}\mathrm{W}\leq\mathrm{d}\}, where ℂ∈ℝm×(t+1)\mathbb{C}\in\mathbb{R}^{m\times(t+1)}, d∈ℝm\mathrm{d}\in\mathbb{R}^{m}, constraint ([4a](https://arxiv.org/html/2602.08228v1#S3.E4.1 "Equation 4a ‣ Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) is transformed into:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | infλ,νs,γs≥0\displaystyle\inf\_{\lambda,\nu\_{s},\upgamma\_{s}\geq 0}\quad | λ​ϵ1+1S​∑s∈Sνs,\displaystyle{\lambda\epsilon^{1}+\frac{1}{S}\sum\_{s\in S}{\nu\_{s}}}, |  | | (14a) |
|  | s.t. | W^s⊺​y+(d−ℂ​W^s)⊺​γs≤νs,\displaystyle\hat{\mathrm{W}}^{\intercal}\_{s}\mathrm{y}+(\mathrm{d}-\mathbb{C}\hat{\mathrm{W}}\_{s})^{\intercal}\upgamma\_{s}\leq\nu\_{s},\quad | s=1,…,S,\displaystyle s=1,\dots,S, |  | (14b) |
|  |  | ‖ℂ⊺​γs−y‖∗≤λ,\displaystyle\|\mathbb{C}^{\intercal}\upgamma\_{s}-\mathrm{y}\|\_{\*}\leq\lambda,\quad | s=1,…,S,\displaystyle s=1,\dots,S, |  | (14c) |

where γs∈ℝm\upgamma\_{s}\in\mathbb{R}^{m}, and ∥.∥∗\|.\|\_{\*} is the dual norm of ∥.∥\|.\|, the norm used in the Wasserstein metric definition. With that, the right-hand side of constraint ([4c](https://arxiv.org/html/2602.08228v1#S3.E4.3 "Equation 4c ‣ Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), which has the pp-distributed random parameter LtL\_{t} with the support set ΞLt:={ft​Lt≤bt,∀t∈T}\Xi\_{L\_{t}}:=\{\mathrm{f}\_{t}L\_{t}\leq\mathrm{b}\_{t},\;\forall t\in T\}, where ft∈ℝm\mathrm{f}\_{t}\in\mathbb{R}^{m}, bt∈ℝm\mathrm{b}\_{t}\in\mathbb{R}^{m} and Lt∈ℝL\_{t}\in\mathbb{R}, reduces to:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | infθt,υs,t,δs,t≥0\displaystyle\inf\_{\theta\_{t},\upsilon\_{s,t},\updelta\_{s,t}\geq 0}\quad | θt​ϵt1+1S​∑s∈Sυs,t,\displaystyle{\theta\_{t}\epsilon\_{t}^{1}+\frac{1}{S}\sum\_{s\in S}{\upsilon\_{s,t}}}, |  | | (15a) |
|  | s.t. | L^s,t+(bt−ft​L^s,t)⊺​δs,t≤υs,t,\displaystyle\hat{L}\_{s,t}+(\mathrm{b}\_{t}-\mathrm{f}\_{t}\hat{L}\_{s,t})^{\intercal}\updelta\_{s,t}\leq\upsilon\_{s,t},\quad | s=1,…,S,t=1,…,T,\displaystyle s=1,\dots,S,t=1,\dots,T, |  | (15b) |
|  |  | ‖ft⊺​δs,t−1‖∗≤θt,\displaystyle\|\mathrm{f}\_{t}^{\intercal}\updelta\_{s,t}-1\|\_{\*}\leq\theta\_{t},\quad | s=1,…,S,t=1,…,T,\displaystyle s=1,\dots,S,t=1,\dots,T, |  | (15c) |

where δs,t∈ℝm\updelta\_{s,t}\in\mathbb{R}^{m}.

In constraints ([4b](https://arxiv.org/html/2602.08228v1#S3.E4.2 "Equation 4b ‣ Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) and ([4b](https://arxiv.org/html/2602.08228v1#S3.E4.2 "Equation 4b ‣ Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), infq∈Q𝔼q​(rt,k⊺​xt−1)=−supq∈Q𝔼q​(−rt,k⊺​xt−1)\inf\_{q\in Q}\mathbb{E}\_{q}(\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1})=-\sup\_{q\in Q}\mathbb{E}\_{q}(-\mathrm{r}\_{t,k}^{\intercal}\mathrm{x}\_{t-1}). Then, by assuming that Ξrt:={𝕄t​rt≤ut,t∈T}\Xi\_{\mathrm{r}\_{t}}:=\{\mathbb{M}\_{t}\mathrm{r}\_{t}\leq\mathrm{u}\_{t},\;t\in T\}, where 𝕄t∈ℝm×(n+1)\mathbb{M}\_{t}\in\mathbb{R}^{m\times(n+1)} and ut∈ℝm\mathrm{u}\_{t}\in\mathbb{R}^{m},
constraints ([4b](https://arxiv.org/html/2602.08228v1#S3.E4.2 "Equation 4b ‣ Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) and ([4b](https://arxiv.org/html/2602.08228v1#S3.E4.2 "Equation 4b ‣ Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) are reformulated as:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  | infϕt,φk,t,ζk,t≥0\displaystyle\inf\_{\phi\_{t},\varphi\_{k,t},\upzeta\_{k,t}\geq 0}\quad | ϕt​ϵt2+1K​∑k∈Kφk,t,\displaystyle{\phi\_{t}\epsilon\_{t}^{2}+\frac{1}{K}\sum\_{k\in K}{\varphi\_{k,t}}}, |  | | (16a) |
|  | s.t. | −r^k,t⊺​xt−1+(ut−𝕄t​r^k,t)⊺​ζk,t≤φk,t,\displaystyle-\hat{\mathrm{r}}\_{k,t}^{\intercal}\mathrm{x}\_{t-1}+(\mathrm{u}\_{t}-\mathbb{M}\_{t}\hat{\mathrm{r}}\_{k,t})^{\intercal}\upzeta\_{k,t}\leq\varphi\_{k,t},\quad | k=1,…,K,t=1,…,T,\displaystyle k=1,\dots,K,t=1,\dots,T, |  | (16b) |
|  |  | ‖𝕄t⊺​ζk,t−xt−1‖∗≤ϕt,\displaystyle\|\mathbb{M}^{\intercal}\_{t}\upzeta\_{k,t}-\mathrm{x}\_{t-1}\|\_{\*}\leq\phi\_{t},\quad | k=1,…,K,t=1,…,T,\displaystyle k=1,\dots,K,t=1,\dots,T, |  | (16c) |

where ζk,t∈ℝm\upzeta\_{k,t}\in\mathbb{R}^{m}. By substituting ([14](https://arxiv.org/html/2602.08228v1#S3.E14 "Equation 14 ‣ 3.3 Wasserstein Ambiguity Set ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), ([15](https://arxiv.org/html/2602.08228v1#S3.E15 "Equation 15 ‣ 3.3 Wasserstein Ambiguity Set ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), and ([16](https://arxiv.org/html/2602.08228v1#S3.E16 "Equation 16 ‣ 3.3 Wasserstein Ambiguity Set ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) in model ([4](https://arxiv.org/html/2602.08228v1#S3.E4 "Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), we have the DRO counterpart of the ALM as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
|  | infλ,νs,γs,ϕt,φk,t,ζk,t,θt,υs,t,δs,t≥0λ​ϵ1+1S​∑s∈Sνs,\displaystyle\;\;\inf\_{\lambda,\nu\_{s},\upgamma\_{s},\phi\_{t},\varphi\_{k,t},\upzeta\_{k,t},\theta\_{t},\upsilon\_{s,t},\updelta\_{s,t}\geq 0}{\lambda\epsilon^{1}+\frac{1}{S}\sum\_{s\in S}{\nu\_{s}}}, |  | (17a) |
|  | s.t.e⊺​xt=−ϕt​ϵt2−1K​∑k∈Kφk,t+wt​yt,s−lt,t=1,…,T−1,\displaystyle\;\;\text{s.t.}\;\;\;\;\mathrm{e}^{\intercal}\mathrm{x}\_{t}=-\phi\_{t}\epsilon\_{t}^{2}-\frac{1}{K}\sum\_{k\in K}{\varphi\_{k,t}}+w\_{t}y\_{t,s}-l\_{t},\;\;\;t=1,...,T-1, |  | (17b) |
|  | −ϕt​ϵt2−1K​∑k∈Kφk,t≥θt​ϵt1+1S​∑s∈Sυs,t,t=1,…,T,\displaystyle\;\;\;\;\;\;\;\;\;\;-\phi\_{t}\epsilon\_{t}^{2}-\frac{1}{K}\sum\_{k\in K}{\varphi\_{k,t}}\geq\theta\_{t}\epsilon\_{t}^{1}+\frac{1}{S}\sum\_{s\in S}{\upsilon\_{s,t}},\;t=1,\dots,T, |  | (17c) |
|  | W^s⊺​y+(d−ℂ​W^s)⊺​γs≤νs,s=1,…,S,\displaystyle\;\;\;\;\;\;\;\;\;\;\hat{\mathrm{W}}^{\intercal}\_{s}\mathrm{y}+(\mathrm{d}-\mathbb{C}\hat{\mathrm{W}}\_{s})^{\intercal}\upgamma\_{s}\leq\nu\_{s},\;s=1,\dots,S, |  | (17d) |
|  | ‖ℂ⊺​γs−y‖∗≤λ,s=1,…,S,\displaystyle\;\;\;\;\;\;\;\;\;\;\|\mathbb{C}^{\intercal}\upgamma\_{s}-\mathrm{y}\|\_{\*}\leq\lambda,\;s=1,\dots,S, |  | (17e) |
|  | −r^k,t⊺​xt−1+(ut−𝕄t​r^k,t)⊺​ζk,t≤φk,t,k=1,…,K,t=1,…,T,\displaystyle\;\;\;\;\;\;\;\;\;\;-\hat{\mathrm{r}}\_{k,t}^{\intercal}\mathrm{x}\_{t-1}+(\mathrm{u}\_{t}-\mathbb{M}\_{t}\hat{\mathrm{r}}\_{k,t})^{\intercal}\upzeta\_{k,t}\leq\varphi\_{k,t},\;k=1,\dots,K,t=1,\dots,T, |  | (17f) |
|  | ‖𝕄t⊺​ζk,t−xt−1‖∗≤ϕt,k=1,…,K,t=1,…,T,\displaystyle\;\;\;\;\;\;\;\;\;\;\|\mathbb{M}^{\intercal}\_{t}\upzeta\_{k,t}-\mathrm{x}\_{t-1}\|\_{\*}\leq\phi\_{t},\;k=1,\dots,K,t=1,\dots,T, |  | (17g) |
|  | L^s,t+(bt−ft​L^s,t)⊺​δs,t≤υs,t,s=1,…,S,t=0,…,T,\displaystyle\;\;\;\;\;\;\;\;\;\;\hat{L}\_{s,t}+(\mathrm{b}\_{t}-\mathrm{f}\_{t}\hat{L}\_{s,t})^{\intercal}\updelta\_{s,t}\leq\upsilon\_{s,t},\;s=1,\dots,S,t=0,\dots,T, |  | (17h) |
|  | ‖ft⊺​δs,t−1‖∗≤θt,s=1,…,S,t=1,…,T,\displaystyle\;\;\;\;\;\;\;\;\;\;\|\mathrm{f}\_{t}^{\intercal}\updelta\_{s,t}-1\|\_{\*}\leq\theta\_{t},\;s=1,\dots,S,t=1,\dots,T, |  | (17i) |
|  | xt∈𝒳,y∈𝒴.\displaystyle\;\;\;\;\;\;\;\;\;\;\mathrm{x}\_{t}\in\mathcal{X},\;\mathrm{y}\in\mathcal{Y}. |  | (17j) |

The tractability of problem ([17](https://arxiv.org/html/2602.08228v1#S3.E17 "Equation 17 ‣ 3.3 Wasserstein Ambiguity Set ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) depends on the dual norm ∥.∥∗\|.\|\_{\*}. We are using norm 2, ∥.∥2\|.\|\_{2}. Moreover, we use a box support set, where 𝕄=−𝕀\mathbb{M}=-\mathbb{I} and ℂ=𝕀\mathbb{C}=\mathbb{I}, and ℐ\mathcal{I} is the identity matrix that leads the box support sets for the uncertain parameters.

## 4 An application to the Canadian Pension Plan

For our study, we utilize data from the Canada Pension Plan (CPP) to conduct a series of numerical experiments. As a mandatory requirement for all employed Canadians aged 18-70, the CPP receives contributions from a vast majority of the working population. According to CPP’s official website 555https://open.canada.ca/data/en/dataset/1fab2afd-4f3c-4922-a07e-58d7bed9dcfc, approximately 5.8 million individuals currently receive retirement benefits from CPP, with an average payout of $\mathdollar811.21 in January 2023 666https://www.canada.ca/en/services/benefits/publicpensions/cpp/cpp-benefit/amount.html. Additionally, CPP’s investments report 777https://www.cppinvestments.com/the-fund/our-performance/financial-results/f2022-annual-results indicates that around 14,371,853 individuals are contributing to CPP.

CPP invests in a diverse portfolio of five asset classes, as per information from investing.com 888https://ca.investing.com/. These asset classes include fixed income, private equity, public equity, infrastructure, and real estate, which are geographically diversified in North America, Europe, and Asia. For our analysis, we have used data from ten major indexes from 2012 to 2022. The S&P 500 index represents public equities, while the Private Equity Index (PRIVEXD) represents private equities. In addition, we use the SP/TSX Capped Real Estate Index (GSPRTRE) for the real estate sector, Treasury Yield 10 Years (TNX) for fixed-income assets, and S&P Global Infrastructure TR (SPGTINTR) for infrastructure investment. The S&P/TSX Composite is used as the index for the Canadian market, while the FTSEurofirst 300 represents public equities in Europe. For the private equity index in Europe, we use the STOXX Europe 20. The Shanghai Stock Exchange (SSE) and Nikkei-225 indexes have been utilized as representatives of investment in Asia.
As of 2022, the total value of assets under CPP management is estimated to be $\mathdollar539 billion. Based on the most recent report from CPP 999https://www.osfi-bsif.gc.ca/Eng/oca-bac/ar-ra/cpp-rpc/Pages/cpp30.aspx, the projected earnings of contributors for 2022 have been calculated to be $\mathdollar585,498 million, of which $\mathdollar57,964 million (approximately 9.9%) represents the contribution to CPP.

The inputs of our proposed models are the value of liabilities in each tt, contributions of employees at each tt, scenarios of asset returns, benefits paid by pension, and scenarios of interest rates. To generate scenarios of asset returns, we use Monte Carlo simulation based on the geometric Brownian motion (GBM), which is a common approach to generate random data in financial problems (McLeish, [2011](https://arxiv.org/html/2602.08228v1#bib.bib55 "Monte carlo simulation and finance")). The formula for GBM is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​P​rP​r=μ​Δ​t+σ​ϵ​Δ​t,\displaystyle\frac{\Delta Pr}{Pr}=\mu\Delta t+\sigma\epsilon\sqrt{\Delta t}, |  | (18) |

where P​rPr is the asset price, Δ​P​r\Delta Pr is the change in asset price, μ\mu represents the expected return, σ\sigma denotes the standard deviation of returns, ϵ\epsilon is a normally-distributed random variable, and Δ​t\Delta t is the elapsed time period.
Our analysis is based on the monthly returns of the ten mentioned indexes spanning from November 2012 to November 2022. During this period, we identified four distinct market regimes based on the long-term mean and standard deviation of the last 30 years. The first period, from November 2012 to February 2018, was characterized by steady growth with low volatility. The second period, from March 2018 to January 2020, experienced higher volatility than the previous period but still maintained a positive trend. The third period, from January 2020 to December 2021, was marked by high volatility and significant fluctuations. Finally, the post-pandemic period from January 2022 to November 2022 saw a return to high volatility, albeit with a different market trajectory.
Using these historical data, we constructed different scenarios for our simulation. Our analysis, based on the kk-mean clustering method of Horvath et al. ([2021](https://arxiv.org/html/2602.08228v1#bib.bib58 "Clustering market regimes using the wasserstein distance")), reveals that during the observed period, 51%\% of the time the market exhibited steady growth with low volatility (LV), 22%\% of the time it had medium volatility (MV) but still showed growth, 17%\% of the time it was characterized by increasing high volatility (IHV) with positive returns and 10%\% of the time it was a decreasing high volatility (DHV) decreasing market with negative returns.
We generated 1000 scenarios for each asset in each period, corresponding to the 4 market regimes. The average return of these 1000 scenarios for each asset in each period, based on each market condition, is considered as the asset’s return in that period for the 4 regimes.

The sets 𝒳\mathcal{X} and 𝒴\mathcal{Y} in model ([4](https://arxiv.org/html/2602.08228v1#S3.E4 "Equation 4 ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) are defined using regulatory constraints based on the last decade’s real investment structure in CPP. These constraints ensure that the contribution rate in each period falls within a range of 5%5\% to 10%10\%, and the investment in the US market cannot exceed 60%60\% of the total fund, while the allocation to Canada must be at least 20%20\%. Additionally, we mandate that a minimum of 10%10\% of the fund be invested in fixed-income assets. The allocation to Asia must not exceed 15%15\% of the fund, and the funding ratio must be at least 1.051.05.

To evaluate the efficacy of our proposed DRO formulation, we conduct an out-of-sample performance analyses for four models.
The first model is the mixture distribution ALM (𝙼𝙳\mathtt{MD}) ([5](https://arxiv.org/html/2602.08228v1#S3.E5 "Equation 5 ‣ 3.1 Mixture Distribution ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")) that incorporates four market conditions: LV, MV, IHV, and DHV. To determine the discrete probabilities associated with each market condition, we leverage the trends observed in historical data spanning the last 30 years. For the period from 2012 to 2022, the distribution functions of the market conditions are as follows: LV with a probability of 0.51, MV with a probability of 0.22, IHV with a probability of 0.17, and DHV with a probability of 0.1. Similarly, for the period from 2002 to 2012, the distribution functions are: LV with a probability of 0.35, MV with a probability of 0.39, IHV with a probability of 0.15, and DHV with a probability of 0.11. Lastly, for the period from 1992 to 2002, the distribution functions are: LV with a probability of 0.41, MV with a probability of 0.19, IHV with a probability of 0.20, and DHV with a probability of 0.06. Additionally, we consider a case where equal probabilities are assigned to each market condition, resulting in a probability of 0.25 for each LV, MV, IHV, and DHV. The second model is the box discrete distribution ALM (𝙱𝙳\mathtt{BD}) ([13](https://arxiv.org/html/2602.08228v1#S3.E13 "Equation 13 ‣ 3.2 Discrete Distribution with Box Ambiguity ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), where half of the range of possible probabilities in each market condition is considered as volatility range in the box ambiguity set. The third mode is the Wasserstein metric ALM (𝚆𝙼\mathtt{WM}) ([17](https://arxiv.org/html/2602.08228v1#S3.E17 "Equation 17 ‣ 3.3 Wasserstein Ambiguity Set ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management")), where the radius of the Wasserstein ball is half of the range of possible probabilities in each market condition times to mean of asset return. The return on the market in the last 3 decades has been almost 10%\% 101010https://www.officialdata.org/us/stocks/s-p-500/2002. Finally, the stochastic programming of ALM (𝚂𝙿\mathtt{SP}) is the last model for comparison to the proposed models.

Asset allocation is a crucial component in addressing the ALM problem. It requires determining how to distribute investments among different asset classes to achieve the desired return while minimizing risk. To compare the optimal asset allocation of four models over the investment horizon, Figure [1](https://arxiv.org/html/2602.08228v1#S4.F1 "Figure 1 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") has been presented. The horizontal axis represents the investment horizon, while the vertical axis depicts the proportion of investment in each asset class. The figure displays four models that correspond to the asset allocation of the 𝙼𝙳\mathtt{MD} model, the 𝙱𝙳\mathtt{BD} model, the 𝚆𝙼\mathtt{WM} model, and the 𝚂𝙿\mathtt{SP} model, respectively.

The Herfindahl-Hirschman Index (HHI) is a widely used metric to quantify market concentration. In portfolio selection, HHI involves assessing the diversification potential and risk exposure across different market segments or asset classes. A low HHI signifies a market characterized by greater diversification, where a larger number of assets distribute market share more evenly among themselves. In portfolio selection, lower HHIs can offer broader diversification benefits, potentially reducing overall portfolio risk by spreading exposure across a more extensive range of assets. In comparing the HHI across four models, 𝙼𝙳\mathtt{MD}, 𝙱𝙳\mathtt{BD}, 𝚆𝙼\mathtt{WM}, and 𝚂𝙿\mathtt{SP}, we observe notable distinctions. 𝙼𝙳\mathtt{MD} exhibits the highest average HHI at 0.256, suggesting a lower diversification. Following closely, 𝚂𝙿\mathtt{SP} presents an average HHI of 0.218, indicating a market structure with considerable concentration, albeit slightly lower than 𝙼𝙳\mathtt{MD}. Conversely, 𝙱𝙳\mathtt{BD} and 𝚆𝙼\mathtt{WM} display lower average HHIs of 0.139 and 0.145 respectively, implying relatively more diversification with a greater number of asset classes sharing the portfolio more evenly. This comparison underscores varying degrees of diversification among the models.

![Refer to caption](paper2picture1.png)


Figure 1: Comparision of optimal asset allocation

The funding ratio (ψ\psi) threshold is an important factor that affects the optimal contribution rate in ALM. Table [2](https://arxiv.org/html/2602.08228v1#S4.T2 "Table 2 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") and Figure [2](https://arxiv.org/html/2602.08228v1#S4.F2 "Figure 2 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") present a comparison of the optimal contribution rates of four models (𝙼𝙳\mathtt{MD}, 𝙱𝙳\mathtt{BD}, 𝚆𝙼\mathtt{WM}, and 𝚂𝙿\mathtt{SP}) under different ψ\psi values.
Figure [2](https://arxiv.org/html/2602.08228v1#S4.F2 "Figure 2 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") indicates that the optimal contribution rates for all models increase as the ψ\psi threshold increases. This is expected because a higher ψ\psi threshold implies a higher level of required funding, which in turn requires higher contribution rates to meet the threshold. Moreover, the table indicates that the optimal contribution rates for each model are different for different ψ\psi values. For instance, the 𝚂𝙿\mathtt{SP} model has the lowest optimal contribution rates among the four models for all ψ\psi values, while the 𝙱𝙳\mathtt{BD} model has the highest optimal contribution rates for ψ\psi=1.15. Figure [2](https://arxiv.org/html/2602.08228v1#S4.F2 "Figure 2 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management") shows that the 𝚆𝙼\mathtt{WM} and 𝙱𝙳\mathtt{BD} models have relatively higher optimal contribution rates than the 𝙼𝙳\mathtt{MD} and 𝚂𝙿\mathtt{SP} models for all ψ\psi values. This suggests that the former models may be less conservative in managing mismatches between assets and liabilities and require higher contributions to ensure funding adequacy.

![Refer to caption](paper2picture2.png)


Figure 2: Optimal contribution rate for targeted funding ratios




Table 2: Optimal contribution rates of four models based on funding ratio

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Models | ψ\psi=1.02 | ψ\psi=1.05 | ψ\psi=1.07 | ψ\psi=1.1 | ψ\psi=1.15 |
| 𝙼𝙳\mathtt{MD} | 1.7%\% | 5.4%\% | 6.6%\% | 8.7%\% | 10.2%\% |
| 𝙱𝙳\mathtt{BD} | 3.1%\% | 6.4%\% | 9.3%\% | 11.8%\% | 14.8%\% |
| 𝚆𝙼\mathtt{WM} | 2.1%\% | 6.1%\% | 8.9%\% | 9.5%\% | 10.6%\% |
| 𝚂𝙿\mathtt{SP} | 1.1%\% | 3.4%\% | 5.2%\% | 8.1%\% | 10.1%\% |

We also evaluated the out-of-sample performance of the aforementioned models using a simulation to generate the testing data.
Out-of-sample analysis refers to a method of evaluating the performance and robustness of a statistical or predictive model using data that is separate from the data used to develop or train the model. Specifically, we generated 10001000 scenarios of asset returns based on their distribution functions reported in (Ghahtarani et al., [2023b](https://arxiv.org/html/2602.08228v1#bib.bib56 "Worst-case conditional value at risk for asset liability management: a novel framework for general loss functions")). We then employed the optimal investment strategies of the 𝙼𝙳\mathtt{MD}, 𝙱𝙳\mathtt{BD}, 𝚆𝙼\mathtt{WM}, and 𝚂𝙿\mathtt{SP} models to compare the average funding ratio and asset value in each period. The results of this analysis are presented in Table [5](https://arxiv.org/html/2602.08228v1#S4.T5 "Table 5 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").

The out-of-sample analysis reveals that the DRO formulations employed in the ALM, 𝚆𝙼\mathtt{WM}, and 𝙱𝙳\mathtt{BD} models exhibit superior performance compared to the 𝙼𝙳\mathtt{MD} and 𝚂𝙿\mathtt{SP} models.
Looking at the funding ratio for 𝙼𝙳\mathtt{MD}, the ratio starts at 1.043 at the moment one, the current tt, and decreases to 0.820 in period nine. However, the funding ratio then increases in tt 10 and 11, ending at 1.030. The fund return for 𝙼𝙳\mathtt{MD} starts at 0.001 at the current tt, decreases to -0.002 at moment four, and then increases to 0.014 in period five. The fund return fluctuates between positive and negative values for the remaining periods.
For 𝙱𝙳\mathtt{BD}, the funding ratio starts at 0.959 and gradually increases to 1.067 in period 11. The fund return for 𝙱𝙳\mathtt{BD} starts at 0.010 and steadily increases to 0.024 in period 11.
𝚆𝙼\mathtt{WM} starts with a funding ratio of 0.972, which increases to 1.088 in period 10 and then decreases slightly to 1.114 in period 11. The fund return for 𝚆𝙼\mathtt{WM} increases from 0.014 to 0.025 in period 10 and then remains constant at 0.025 in period 11.
Finally, 𝚂𝙿\mathtt{SP} starts with a funding ratio of 0.981, which increases to 0.992 in period 11. The fund return for 𝚂𝙿\mathtt{SP} starts at 0.001, decreases to -0.007 in period three, and then increases to 0.004 in period 10.

![Refer to caption](paper2picture3.png)


Figure 3: Funding Ratio of Different Models

![Refer to caption](paper2picture4.png)


Figure 4: Fund Return of Different Models

The average funding ratio for 𝙼𝙳\mathtt{MD} is 0.976, indicating an average funding ratio below 1. This suggests that, on average, the assets are lower than the liabilities for 𝙼𝙳\mathtt{MD}. 𝙱𝙳\mathtt{BD} has a mean funding ratio of 1.0115, indicating a slightly higher average ratio where assets are closer to liabilities. 𝚆𝙼\mathtt{WM} has the highest mean funding ratio among the models at 1.0480, suggesting a relatively higher average ratio of assets to liabilities. 𝚂𝙿\mathtt{SP} has the lowest mean funding ratio of 0.8661, indicating a lower average ratio where liabilities are higher than assets. In terms of the mean fund return, 𝙼𝙳\mathtt{MD} has a mean value of 0.0035, suggesting a slightly positive average return. 𝙱𝙳\mathtt{BD} has a higher mean fund return of 0.0140, indicating a relatively higher average return compared to 𝙼𝙳\mathtt{MD}. 𝚆𝙼\mathtt{WM} has a mean fund return of 0.0185, suggesting a slightly higher average return among the models. 𝚂𝙿\mathtt{SP} has the lowest mean fund return value of 0.0006, indicating a very low average return.

The standard deviation values provide insights into the variability or dispersion of the performance metrics. For the funding ratio, 𝙼𝙳\mathtt{MD} has a standard deviation of 0.077, indicating a relatively higher variability compared to the other models. 𝙱𝙳\mathtt{BD} has the lowest standard deviation of 0.034, suggesting a lower variability in funding ratio performance. 𝚆𝙼\mathtt{WM} and 𝚂𝙿\mathtt{SP} have standard deviations of 0.039 and 0.102, respectively, indicating moderate to high variability. Regarding the fund return, 𝙼𝙳\mathtt{MD} has a standard deviation of 0.008, suggesting a relatively higher variability in returns. 𝙱𝙳\mathtt{BD} has the lowest standard deviation of 0.004, indicating a lower variability in fund return performance. 𝚆𝙼\mathtt{WM} has a standard deviation of 0.005, similar to 𝙱𝙳\mathtt{BD}, suggesting relatively stable fund return outcomes. 𝚂𝙿\mathtt{SP} has a standard deviation of 0.003, indicating a lower variability compared to the other models.

Table 3: Pairwise comparison of means for funding ratio

Comparison
t-statistic
p-value

𝙼𝙳\mathtt{MD} vs 𝙱𝙳\mathtt{BD}
-1.6631
0.1119

𝙼𝙳\mathtt{MD} vs 𝚆𝙼\mathtt{WM}
-2.9507
0.0079

𝙼𝙳\mathtt{MD} vs 𝚂𝙿\mathtt{SP}
2.4832
0.0220

𝙱𝙳\mathtt{BD} vs 𝚆𝙼\mathtt{WM}
-2.2106
0.0389

𝙱𝙳\mathtt{BD} vs 𝚂𝙿\mathtt{SP}
4.2477
0.0004

𝚆𝙼\mathtt{WM} vs 𝚂𝙿\mathtt{SP}
5.2291
0.0000

The pairwise comparison of means for funding ratio, as presented in Table [3](https://arxiv.org/html/2602.08228v1#S4.T3 "Table 3 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"), reveals several notable distinctions between the ALM models. While no significant difference in means is observed between 𝙼𝙳\mathtt{MD} and 𝙱𝙳\mathtt{BD}, 𝙼𝙳\mathtt{MD} exhibits a lower mean funding ratio compared to 𝚆𝙼\mathtt{WM}, with a statistically significant difference confirmed by the negative t-statistic and p-value below 0.05. Conversely, 𝙼𝙳\mathtt{MD} demonstrates a higher mean funding ratio than 𝚂𝙿\mathtt{SP}, again with statistical significance, indicated by the positive t-statistic and p-value below 0.05. 𝙱𝙳\mathtt{BD} displays a lower mean funding ratio compared to both 𝚆𝙼\mathtt{WM} and 𝚂𝙿\mathtt{SP}, with statistically significant differences confirmed by the negative t-statistic and p-values below 0.05, respectively. Moreover, 𝙱𝙳\mathtt{BD} exhibits a higher mean funding ratio than 𝚂𝙿\mathtt{SP}, with a notably high t-statistic and a highly significant p-value of 0.0004. 𝚆𝙼\mathtt{WM}, on the other hand, exhibits a higher mean funding ratio than 𝚂𝙿\mathtt{SP}, with an extremely significant difference confirmed by the positive t-statistic and p-value of 0.0000.

Table 4: Pairwise comparison of means for fund return

Comparison
t-statistic
p-value

𝙼𝙳\mathtt{MD} vs 𝙱𝙳\mathtt{BD}
-3.4220
0.0027

𝙼𝙳\mathtt{MD} vs 𝚆𝙼\mathtt{WM}
-4.6446
0.0002

𝙼𝙳\mathtt{MD} vs 𝚂𝙿\mathtt{SP}
0.9851
0.3363

𝙱𝙳\mathtt{BD} vs 𝚆𝙼\mathtt{WM}
-2.0357
0.0552

𝙱𝙳\mathtt{BD} vs 𝚂𝙿\mathtt{SP}
7.4647
0.0000

𝚆𝙼\mathtt{WM} vs 𝚂𝙿\mathtt{SP}
8.7202
0.0000

The pairwise comparison of means for fund return, as detailed in Table [4](https://arxiv.org/html/2602.08228v1#S4.T4 "Table 4 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"), highlights significant differences between certain pairs of ALM models. Notably, 𝙼𝙳\mathtt{MD} exhibits statistically significant differences in mean fund return compared to both 𝙱𝙳\mathtt{BD} and 𝚆𝙼\mathtt{WM}, as indicated by t-statistics of -3.4220 and -4.6446, respectively, and p-values below 0.05. Conversely, the comparison between 𝙼𝙳\mathtt{MD} and 𝚂𝙿\mathtt{SP} shows no statistically significant difference in mean fund return, with a t-statistic of 0.9851 and a p-value exceeding 0.05. 𝙱𝙳\mathtt{BD} demonstrates a significant difference in mean fund return compared to 𝚂𝙿\mathtt{SP}, with a high t-statistic of 7.4647 and a very low p-value of 0.0000. Similarly, 𝚆𝙼\mathtt{WM} exhibits a significantly different mean fund return compared to 𝚂𝙿\mathtt{SP}, with a higher t-statistic of 8.7202 and an equally low p-value of 0.0000.

Table 5: Out-sample performance of the ALM models

𝙼𝙳\mathtt{MD}
𝙱𝙳\mathtt{BD}
𝚆𝙼\mathtt{WM}
𝚂𝙿\mathtt{SP}

Decision moments
Funding ratio
Fund return
Funding ratio
Fund return
Funding ratio
Fund return
Funding ratio
Fund return

1
1.043
0.001
0.959
0.010
0.972
0.014
0.981
0.001

2
1.016
0.001
0.960
0.010
0.983
0.014
0.983
0.004

3
1.022
0.007
0.965
0.011
1.036
0.015
0.774
-0.007

4
0.816
-0.002
1.022
0.011
1.044
0.021
0.730
-0.004

5
0.931
0.014
1.014
0.010
1.058
0.023
0.923
0.001

6
0.970
0.001
1.028
0.018
1.048
0.009
0.752
-0.003

7
0.976
0.004
1.016
0.013
1.049
0.018
0.770
0.001

8
0.978
0.013
1.012
0.015
1.059
0.014
0.781
0.004

9
0.820
-0.015
1.045
0.019
1.077
0.025
0.859
0.002

10
1.035
0.017
1.038
0.013
1.088
0.025
0.982
0.005

11
1.030
-0.002
1.067
0.024
1.114
0.025
0.992
0.003

Average
0.976
0.0035
1.0115
0.0140
1.0480
0.0185
0.8661
0.0006

Std. Dev.
0.077
0.008
0.034
0.004
0.039
0.005
0.102
0.003

Based on the results presented in Table [5](https://arxiv.org/html/2602.08228v1#S4.T5 "Table 5 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"), it is evident that the 𝚆𝙼\mathtt{WM} model outperforms the other models in terms of both fund return and funding ratio. With the highest mean values across the investment horizon, 𝚆𝙼\mathtt{WM} demonstrates superior performance from both perspectives while it has a moderate contribution rate in comparison to other models based on Table [2](https://arxiv.org/html/2602.08228v1#S4.T2 "Table 2 ‣ 4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"). In particular, the 𝚆𝙼\mathtt{WM} model exhibits a higher mean funding ratio compared to 𝙼𝙳\mathtt{MD} and 𝚂𝙿\mathtt{SP}, indicating a more favorable financial position. This implies that 𝚆𝙼\mathtt{WM} manages to maintain a healthier balance between assets and liabilities, resulting in a greater ability to meet financial obligations. The higher funding ratio suggests a more robust and secure asset-liability management strategy.
Additionally, 𝚆𝙼\mathtt{WM} achieves the highest mean fund return among all the models, surpassing 𝙱𝙳\mathtt{BD}, 𝙼𝙳\mathtt{MD}, and 𝚂𝙿\mathtt{SP}. This indicates that 𝚆𝙼\mathtt{WM} generates more favorable investment returns on average throughout the investment horizon. A higher mean fund return suggests better investment performance, potentially leading to higher profits and returns for the ALM strategy.
Therefore, based on the mean funding ratio and fund return values, it can be concluded that 𝚆𝙼\mathtt{WM} exhibits better performance than the other models in terms of stability and asset management. Its higher funding ratio indicates a stronger financial position, while the superior mean fund return reflects better investment outcomes. These findings highlight the effectiveness of the 𝚆𝙼\mathtt{WM} model in achieving both financial stability and favorable investment returns, making it a preferable choice among the options considered.

There is a technical reason why these models exhibit varying degrees of conservativeness and different out-of-sample performance. 𝚂𝙿\mathtt{SP} finds the optimal solution based on a single distribution function, specifically the empirical distribution function. As a result, it does not offer sufficient protection against unseen scenarios in the out-of-sample data. 𝙼𝙳\mathtt{MD} offers a solution by considering a broader range of possible distribution functions, as it takes into account the convex combination of multiple discrete distribution functions, forming a polyhedron. As a result, 𝙼𝙳\mathtt{MD} solutions are more conservative than 𝚂𝙿\mathtt{SP} solutions. On the other hand, 𝙼𝙳\mathtt{MD} solutions exhibit better out-of-sample performance compared to 𝚂𝙿\mathtt{SP} solutions. 𝙱𝙳\mathtt{BD} includes the widest range of distribution functions in its ambiguity set. Consequently, it offers the most conservative solution with the highest contribution rate, and highest opportunity cost. Finally, model 𝚆𝙼\mathtt{WM} uses a ball as its ambiguity set, covering a wide range of distribution functions. Although its contribution rate is not as high as that of
𝙱𝙳\mathtt{BD}, it offers the most diversified portfolio and demonstrates better out-of-sample performance than the other models.

## 5 Conclusions

Pension funds play a vital role in ensuring retirement income security for workers globally. However, they face challenges such as uncertainty of asset return and liability values. To address these issues, an effective asset-liability management (ALM) strategy must be implemented, balancing the competing objectives of generating returns and meeting future obligations. In this paper, we addressed the uncertainty of parameters in the ALM problem by exploring three different approaches: using mixture ambiguity sets with discrete scenarios and box uncertain discrete distribution functions. However, both of these approaches have limitations, and to overcome them, we incorporated the Wasserstein metric into the ALM problem. By incorporating the Wasserstein metric, we provide a more comprehensive and reliable approach to dealing with the limitations of ambiguity sets while maintaining the desirable properties of finite sample guarantee, asymptotic consistency, and tractability.

This study has used data from the CPP to conduct a series of numerical experiments and tests to simulate different market scenarios and their impact on the plan. Monte Carlo simulation based on geometric Brownian motion was used to generate scenarios of asset returns. The analysis revealed four distinct market regimes during the observed period from November 2012 to November 2022.

Our analysis indicated that 𝙱𝙳\mathtt{BD} and 𝚆𝙼\mathtt{WM} offer more diversified portfolios. However, the contribution rate of 𝚆𝙼\mathtt{WM} is nearly identical to that of 𝚂𝙿\mathtt{SP} and 𝙼𝙳\mathtt{MD} across various values of ψ\psi. In contrast, 𝙱𝙳\mathtt{BD} has the highest contribution rate, highlighting its conservative approach compared to the other models.

The out-of-sample analysis of the ALM models reveals that the 𝚆𝙼\mathtt{WM} model demonstrates superior performance compared to the 𝙼𝙳\mathtt{MD}, 𝙱𝙳\mathtt{BD}, and 𝚂𝙿\mathtt{SP} models in terms of both funding ratio and fund return.
The superior performance of the 𝚆𝙼\mathtt{WM} model in terms of funding ratio and fund return can be attributed to its robust optimization approach and risk management capabilities. By incorporating worst-case distribution functions based on the scenarios of asset returns, the 𝚆𝙼\mathtt{WM} model is designed to handle extreme market conditions and mitigate potential risks.
The higher mean funding ratio of the 𝚆𝙼\mathtt{WM} model indicates a more conservative approach to asset-liability management, ensuring that the liabilities are well-covered by the available assets. This conservative stance provides a buffer against unexpected market fluctuations and reduces the likelihood of financial instability.

Furthermore, the higher mean fund return of the 𝚆𝙼\mathtt{WM} model suggests that it is able to capture profitable investment opportunities more effectively than the other models. This can be attributed to the optimization framework of the 𝚆𝙼\mathtt{WM} model, which aims to maximize investment returns while considering the constraints imposed by liabilities and risk tolerance.
The stability of the 𝚆𝙼\mathtt{WM} model’s funding ratio and fund return is also evident from its lower standard deviation values compared to the other models. A lower standard deviation implies less variability and a more consistent performance over time. This stability is crucial for long-term financial planning and managing the risks associated with asset-liability mismatches.

Future research could focus on several directions to further enhance the understanding and application of ALM strategies for pension funds.
Firstly, it would be interesting to extend the analysis to consider the risk measures in the ALM problem. Incorporating such preferences into the ALM framework would allow for a more nuanced analysis of the trade-offs between risk and return and could provide insights into how different investors with varying risk preferences may adopt different ALM strategies.
Secondly, the current study used the Wasserstein metric to improve the robustness of the ALM models. However, there are other distance metrics that can be used to measure the discrepancy between probability distributions, such as the Kullback-Leibler divergence or the Total Variation distance. Future research could investigate the use of different distance metrics and compare their performance in the ALM context.
Lastly, the current study focused on the CPP, and it would be interesting to extend the analysis to other pension funds in different regions to explore the applicability and effectiveness of the ALM models in different contexts. Comparing the performance of ALM strategies across different pension funds could provide insights into how different market conditions and regulatory environments may impact the effectiveness of ALM strategies.

## References

* D. Barro, G. Consigli, and V. Varun (2022)
  A stochastic programming model for dynamic portfolio management with financial derivatives.
  Journal of Banking & Finance 140,  pp. 106445.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* A. Ben-Tal, L. El Ghaoui, and A. Nemirovski (2009)
  Robust optimization.
  Vol. 28, Princeton university press.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p5.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* J. Blanchet, L. Chen, and X. Y. Zhou (2022)
  Distributionally robust mean-variance portfolio selection with wasserstein distances.
  Management Science 68 (9),  pp. 6382–6410.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p7.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* Z. Bodie, A. J. Marcus, and R. C. Merton (1988)
  Defined benefit versus defined contribution pension plans: what are the real trade-offs?.
  In Pensions in the US Economy,
   pp. 139–162.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p1.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* G. C. Boender (1997)
  A hybrid simulation/optimisation scenario model for asset/liability management.
  European Journal of Operational Research 99 (1),  pp. 126–135.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p8.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* E. Bogentoft, H. E. Romeijn, and S. Uryasev (2001)
  Asset/liability management for pension funds using cvar constraints.
  The Journal of Risk Finance.
  Cited by: [§2](https://arxiv.org/html/2602.08228v1#S2.p1.1 "2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"),
  [§2](https://arxiv.org/html/2602.08228v1#S2.p3.18 "2 ALM Model for Pension Funds ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* G. Consigli and M. A. Dempster (1998)
  Dynamic stochastic programmingfor asset-liability management.
  Annals of Operations Research 81 (0),  pp. 131–162.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* G. Consigli (2008)
  Asset-liability management for individual investors.
  In Handbook of asset and liability management,
   pp. 751–827.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* O. Costa and A. Paiva (2002)
  Robust portfolio selection using linear-matrix inequalities.
  Journal of Economic Dynamics and Control 26 (6),  pp. 889–909.
  Cited by: [§3.1](https://arxiv.org/html/2602.08228v1#S3.SS1.p1.4 "3.1 Mixture Distribution ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* G. B. Dantzig and G. Infanger (1993)
  Multi-stage stochastic linear programs for portfolio optimization.
  Annals of Operations Research 45 (1),  pp. 59–76.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p6.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* M. Dempster and G. Consigli (1996)
  Dynamic stochastic programming for asset-liability management.
  Annals of Operations Research.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* T. B. Duarte, D. M. Valladão, and Á. Veiga (2017)
  Asset liability management for open pension schemes using multistage stochastic programming under solvency-ii-based regulatory constraints.
  Insurance: Mathematics and Economics 77,  pp. 177–188.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* V. Gabrel, C. Murat, and A. Thiele (2014)
  Recent advances in robust optimization: an overview.
  European journal of operational research 235 (3),  pp. 471–483.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p5.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* L. Gajek and E. Krajewska (2022)
  Robust portfolio choice under the interest rate uncertainty.
  Optimization 71 (9),  pp. 2727–2747.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p6.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* A. Ghahtarani, A. Saif, A. Ghasemi, and E. Delage (2023a)
  A double-oracle, logic-based benders decomposition approach to solve the k-adaptability problem.
  Computers & Operations Research 155,  pp. 106243.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p6.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* A. Ghahtarani, A. Saif, and A. Ghasemi (2022)
  Robust portfolio selection problems: a comprehensive review.
  Operational Research,  pp. 1–62.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p5.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"),
  [§3.1](https://arxiv.org/html/2602.08228v1#S3.SS1.p1.4 "3.1 Mixture Distribution ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* A. Ghahtarani, A. Saif, and A. Ghasemi (2023b)
  Worst-case conditional value at risk for asset liability management: a novel framework for general loss functions.
  Vol. , .
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p7.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"),
  [§4](https://arxiv.org/html/2602.08228v1#S4.p9.5 "4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* L. E. Ghaoui, M. Oks, and F. Oustry (2003)
  Worst-case value-at-risk and robust portfolio optimization: a conic programming approach.
  Operations research 51 (4),  pp. 543–556.
  Cited by: [§3.1](https://arxiv.org/html/2602.08228v1#S3.SS1.p1.4 "3.1 Mixture Distribution ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* N. Gülpinar and D. Pachamanova (2013)
  A robust optimization approach to asset-liability management under time-varying investment opportunities.
  Journal of Banking & Finance 37 (6),  pp. 2031–2041.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p6.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* N. Gülpınar, D. Pachamanova, and E. Çanakoğlu (2016)
  A robust asset–liability management framework for investment products with guarantees.
  OR Spectrum 38 (4),  pp. 1007–1041.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p3.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"),
  [§1](https://arxiv.org/html/2602.08228v1#S1.p6.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* N. Hibiki (2006)
  Multi-period stochastic optimization models for dynamic asset allocation.
  Journal of Banking & Finance 30 (2),  pp. 365–390.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* R. Holzmann (2013)
  Global pension systems and their reform: worldwide drivers, trends and challenges.
  International Social Security Review 66 (2),  pp. 1–29.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p3.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* B. Horvath, Z. Issa, and A. Muguruza (2021)
  Clustering market regimes using the wasserstein distance.
  arXiv preprint arXiv:2110.11848.
  Cited by: [§4](https://arxiv.org/html/2602.08228v1#S4.p3.13 "4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* G. Iyengar and A. K. C. Ma (2016)
  A robust optimization approach to pension fund management.
  In Asset management,
   pp. 339–363.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p6.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* L. Jiang, C. Wu, and S. Wang (2023)
  Distributionally robust multi-period portfolio selection subject to bankruptcy constraints.
  Journal of Industrial and Management Optimization 19 (2),  pp. 1044–1057.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p7.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* P. Klaassen (1997)
  Discretized reality and spurious profits in stochastic programming models for asset/liability management.
  European Journal of Operational Research 101 (2),  pp. 374–392.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* M. Kopa, V. Moriggia, and S. Vitali (2018)
  Individual optimal pension allocation under stochastic dominance constraints.
  Annals of Operations Research 260 (1),  pp. 255–291.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* R. Kouwenberg (2001)
  Scenario generation and stochastic programming models for asset liability management.
  European Journal of operational research 134 (2),  pp. 279–292.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p4.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* F. Lin, X. Fang, and Z. Gao (2022)
  Distributionally robust optimization: a review on theory and applications.
  Numerical Algebra, Control and Optimization 12 (1),  pp. 159–212.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p7.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* D. L. McLeish (2011)
  Monte carlo simulation and finance.
  Vol. 276, John Wiley & Sons.
  Cited by: [§4](https://arxiv.org/html/2602.08228v1#S4.p3.2 "4 An application to the Canadian Pension Plan ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* P. Mohajerin Esfahani and D. Kuhn (2018)
  Data-driven distributionally robust optimization using the wasserstein metric: performance guarantees and tractable reformulations.
  Mathematical Programming 171 (1),  pp. 115–166.
  Cited by: [§3.3](https://arxiv.org/html/2602.08228v1#S3.SS3.p1.1 "3.3 Wasserstein Ambiguity Set ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"),
  [§3.3](https://arxiv.org/html/2602.08228v1#S3.SS3.p2.30 "3.3 Wasserstein Ambiguity Set ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* E. Platanakis and C. Sutcliffe (2017)
  Asset–liability modelling and pension schemes: the application of robust optimization to uss.
  The European Journal of Finance 23 (4),  pp. 324–352.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p6.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* H. Rahimian and S. Mehrotra (2019)
  Distributionally robust optimization: a review.
  arXiv preprint arXiv:1908.05659.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p7.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* S. A. Zenios (1995)
  Asset/liability management under uncertainty for fixed-income securities.
  Annals of Operations Research 59 (1),  pp. 77–97.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p1.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* Z. Zhang, H. Jing, and C. Kao (2023)
  High-dimensional distributionally robust mean-variance efficient portfolio selection.
  Mathematics 11 (5),  pp. 1272.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p7.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").
* S. Zhu and M. Fukushima (2009)
  Worst-case conditional value-at-risk with application to robust portfolio management.
  Operations research 57 (5),  pp. 1155–1168.
  Cited by: [§1](https://arxiv.org/html/2602.08228v1#S1.p8.1 "1 Introduction ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management"),
  [§3.1](https://arxiv.org/html/2602.08228v1#S3.SS1.p1.4 "3.1 Mixture Distribution ‣ 3 Distributionally Robust ALM ‣ Comparing Mixture, Box, and Wasserstein Ambiguity Sets in Distributionally Robust Asset Liability Management").