---
authors:
- E. Benhamou
- JJ. Ohana
- B. Guez
- E. Setrouk
- T. Jacquot
doc_id: arxiv:2510.23183v1
family_id: arxiv:2510.23183
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'PEARL: Private Equity Accessibility Reimagined with Liquidity'
url_abs: http://arxiv.org/abs/2510.23183v1
url_html: https://arxiv.org/html/2510.23183v1
venue: arXiv q-fin
version: 1
year: 2025
---


E. Benhamou1,2
  
JJ. Ohana1
  
B. Guez1
  
E. Setrouk1
  
T. Jacquot1
  
1Ai for Alpha
  
2Dauphine PSL
  
{eric.benhamou, jean-jacques.ohana, beatrice.guez, ethan.setrouk, thomas.jacquot}@aiforalpha.com

###### Abstract

In this work, we introduce PEARL (Private Equity Accessibility Reimagined with Liquidity), an AI-powered framework designed to replicate and decode private equity funds using liquid, cost-effective assets. Relying on previous research methods such as Erik Stafford’s single stock selection (Stafford) and Thomson Reuters - Refinitiv’s sector approach (TR), our approach incorporates an additional asymmetry to capture the reduced volatility and better performance of private equity funds resulting from sale timing, leverage, and stock improvements through management changes. As a result, our model exhibits a strong correlation with well-established liquid benchmarks such as Stafford and TR, as well as listed private equity firms (Listed PE), while enhancing performance to better align with renowned quarterly private equity benchmarks like Cambridge Associates, Preqin, and Bloomberg Private Equity Fund indices. Empirical findings validate that our two-step approach—decoding liquid daily private equity proxies with a degree of negative return asymmetry—outperforms the initial daily proxies and yields performance more consistent with quarterly private equity benchmarks.
  
Keywords: Private equity funds replication, Liquid assets, Performance improvement, Decoding, Machine Learning

## 1 Introduction

Over the past quarter-century, investments in private equity (PE) have significantly increased in size, as illustrated by various strategic consulting companies reports such as BCG ([2020](https://arxiv.org/html/2510.23183v1#bib.bib5)), McKinsey ([2020](https://arxiv.org/html/2510.23183v1#bib.bib14)) and lately McKinsey ([2023](https://arxiv.org/html/2510.23183v1#bib.bib15)). As of June 30, 2023, private equity funds’ assets under management (AUM) totaled over $13 trillion, reflecting a nearly 2% annual growth rate since 2018 as illustrated in McKinsey ([2023](https://arxiv.org/html/2510.23183v1#bib.bib15)). Large institutional investors, including pension funds and sovereign wealth funds, allocate substantial portions of their portfolios to private investments. For instance, the California Public Employees’ Retirement System (CalPERS) has increased its target exposure to private markets from 33% to 40 %, committing approximately $15 billion to co-investments over the past 18 months. Similarly, Singapore’s GIC, a sovereign wealth fund managing over $700 billion in assets, actively invests in private equity, including acquiring stakes in Western companies’ Chinese units, with undisclosed amounts rumoured though to be substantial. Likewise, as of June 30, 2024, Harvard University’s endowment (respectively the Canada Pension Plan Investment Board (CPPIB) and the Yale University’s endowment) was reported to have invested 39% (respectively 32% and 33 %) of its $53.2 billion (respectively $143 billion and $40 billion) capital.

However despite the capacity of PE funds to offer the potential for much higher returns than public equities markets, one of the major constraint is their inherent illiquidity. Investments in PE involve investing in illiquid, privately held assets that requires long-term capital commitments.
This illiquidity distinguishes PE from public equities and introduces substantial challenges for investors, particularly during periods with limited exit opportunities. During such times, the illiquidity of PE becomes especially pronounced and burdensome for large institutional investors who critically need to liquidate portions of their portfolio to fulfill obligations, such as distributions to pensioners.

This has led to strong interest in developing liquid alternatives to PE funds that can reproduce similar performance streams while avoiding the constraints of illiquidity beyond evergreen solutions that are very constrained by the size of the secondary market. However, the feasibility of such alternatives remains uncertain in the economic literature. It is often argued that the superior returns associated with PE funds are intrinsically tied to the illiquidity of their investment portfolios. Investors are generally willing to commit their capital only when they anticipate higher returns as compensation for bearing illiquidity risks as argued in Kaplan and Schoar ([2005](https://arxiv.org/html/2510.23183v1#bib.bib11)); Ang et al. ([2014b](https://arxiv.org/html/2510.23183v1#bib.bib3), [a](https://arxiv.org/html/2510.23183v1#bib.bib2)); Franzoni et al. ([2012](https://arxiv.org/html/2510.23183v1#bib.bib8)).

There has been various attempts to offer liquid replicating benchmark. Stafford ([2021](https://arxiv.org/html/2510.23183v1#bib.bib21)) uses small stocks selection while Thomson Reuters ([2014](https://arxiv.org/html/2510.23183v1#bib.bib22)) uses a sector based approach that provides greater scalability by focusing on broad industry groups. While these approaches address some liquidity concerns, they may fail first to be scalable as they involve public though not very liquid or scalable assets and second to capture the nuanced value drivers in private equity, including the impact of management changes, operational improvements, and the timing of strategic sales, as highlighted by Kaplan and Strömberg ([2009](https://arxiv.org/html/2510.23183v1#bib.bib12)), resulting in some lower volatility and better performance in downturn times. The key question is whether we could use more liquid instruments like large equity indexes futures that can scale to a much higher extent. Additionally, incorporating asymmetry in returns has emerged as a critical innovation. Studies such as Ang et al. ([2014b](https://arxiv.org/html/2510.23183v1#bib.bib3)) and Franzoni et al. ([2012](https://arxiv.org/html/2510.23183v1#bib.bib8)) highlight that private equity returns often exhibit asymmetric characteristics due to their exposure to risk-off environments and tail risk strategies. These factors contribute to the positive alpha observed in PE funds, making it imperative to account for these dynamics in any replication framework. By integrating these asymmetric return factors, hybrid strategies can better mimic the risk-return profile of private equity, offering a more comprehensive solution to liquidity constraints.

### 1.1 Innovation

Our contributions to the field of replicating private equity funds are threefold:

* •

  Enhanced Liquidity: We achieve greater liquidity by using highly liquid futures contracts, offering a scalable and practical solution for replicating private equity returns in public markets.
* •

  Improved Replication Precision: By employing advanced machine learning decoding techniques based on graphical models, which enhance traditional linear regression methods, our approach delivers more accurate replication of private equity performance.
* •

  Incorporation of Asymmetry in Decoding: Our method accounts for the asymmetry in the replication process to address the embedded and implicit put option arising from the ability to time sales as well as other private equity funds performance enhancement like management improvement and capital optimization, ensuring robustness in performance replication.

### 1.2 Structure of Paper

The rest of the paper is organized as follows:
Section [2](https://arxiv.org/html/2510.23183v1#S2 "2 Literature review ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") reviews the existing literature on private equity and replication strategies. It begins by exploring the three pillars of value creation in private equity: corporate governance, operational optimization, and financial engineering. Additionally, this section discusses attempts to provide liquid replication strategies for private equity returns, evaluating their methodologies, performance, and limitations.

Section [3](https://arxiv.org/html/2510.23183v1#S3 "3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") presents the methodological framework adopted in this study. It begins with a description of the two-step approach used to analyze private equity replication strategies, providing a systematic breakdown of the process. We also provide a primer on graphical models to explain why these models generalize and improve advanced successive linear regressions or Kalman filters. Furthermore, the section discusses the role of asymmetric factors in capturing unique aspects of private equity performance and risk-return profiles.

Section [4](https://arxiv.org/html/2510.23183v1#S4 "4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") provides the empirical results and statistical analyses. This section evaluates the impact of benchmark selection on the performance of replication strategies, focusing on how different benchmarks slightly change the results. Additionally, the correlation accuracy of the proposed replication models is analyzed to assess their robustness in mimicking private equity performance under various conditions.

Finally, in the concluding section [5](https://arxiv.org/html/2510.23183v1#S5 "5 Conclusion ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity"), we summarize key findings and discuss the limitations of the study, and suggest directions for future research.

## 2 Literature review

### 2.1 Private Equity value creation

Private equity (PE) funds differ significantly from venture capital in their investment strategy, focusing on acquiring majority control of mature firms rather than investing in emerging companies without majority control. The three pillars of value creation in leveraged buyouts—corporate governance, operational optimization, and financial engineering—have been central to PE value generation as explained in Kaplan and Strömberg ([2009](https://arxiv.org/html/2510.23183v1#bib.bib12)). The authors emphasize that these pillars enable general partners to introduce disciplined management incentives, optimize operations, and enhance financial structures within their portfolio companies.

Management incentivization is a cornerstone of private equity governance. For instance, Kaplan and Schoar ([2005](https://arxiv.org/html/2510.23183v1#bib.bib11)) found that transitioning firms from public to private ownership significantly increases management equity stakes, aligning their incentives with long-term growth objectives. Furthermore, the illiquid nature of PE compensation, through stock and options, ensures a focus on sustained value creation over short-term manipulation. Acharya et al. ([2009](https://arxiv.org/html/2510.23183v1#bib.bib1)) corroborate this finding, showing that PE-backed CEOs and management teams receive substantial equity stakes, reinforcing alignment between managers and investors.

Financial engineering is another critical value-creation mechanism in PE. By optimizing capital structures and leveraging debt, PE funds capitalize on tax shields and enhance returns. Jensen ([1986](https://arxiv.org/html/2510.23183v1#bib.bib10)) highlights how leverage mitigates free cash flow problems by enforcing financial discipline. However, excessive leverage can increase financial distress risks, as evidenced by Axelson et al. ([2013](https://arxiv.org/html/2510.23183v1#bib.bib4)), who found a negative relationship between extreme leverage and fund returns.

Operational optimization has gained increasing importance since the late 1980s. Top-performing PE firms now focus on sector-specific expertise and employ specialized professionals to implement productivity improvements, strategic changes, and cost-cutting measures. Studies show that PE-backed companies outperform their public counterparts in terms of operational efficiency, with cash flow-to-sales ratios improving significantly post-buyout as illustrated in Kaplan and Schoar ([2005](https://arxiv.org/html/2510.23183v1#bib.bib11)) and Acharya et al. ([2009](https://arxiv.org/html/2510.23183v1#bib.bib1)).

The risk-return profile of private equity is another distinguishing feature of the asset class. Traditional portfolio theory posits that asset returns are commensurate with their inherent risks Markowitz ([1952](https://arxiv.org/html/2510.23183v1#bib.bib13)). However, PE assets deviate from this paradigm due to their illiquid nature, unique risk exposures, and systematic risk factors absent in public markets. Döskeland and Strömberg ([2018](https://arxiv.org/html/2510.23183v1#bib.bib7)) argue that illiquidity necessitates a premium return, particularly during periods of market distress when PE holdings are difficult to liquidate. Moreover, diversification across vintage years can mitigate idiosyncratic risk, as shown by Robinson and Sensoy ([2016](https://arxiv.org/html/2510.23183v1#bib.bib19)).

### 2.2 Attempt to provide liquid replicating strategies

In the economic literature, there have been efforts to develop liquid replicating benchmarks for private equity (PE) returns. Replication strategies have gained attention as a means of emulating the performance of private equity investments through public market instruments, addressing challenges such as the opaque nature, irregular cash flows, and long-term commitment associated with PE investments.

Rasmussen and Chinono ([2015](https://arxiv.org/html/2510.23183v1#bib.bib18)) were among the first to explore the replication of private equity performance by focusing on small, value-oriented, and leveraged public stocks. They developed a ranking system prioritizing smaller, cheaper stocks with above-median leverage and incorporated metrics such as debt paydown and improving asset turnover. Their annual top-25 stock portfolio demonstrated alphas of 9.56% and 13.06% under the CAPM and the Fama-French 3-factor model, respectively, further enhanced by liquidity and momentum factors. This approach emphasized disciplined, long-term investment strategies while acknowledging the higher volatility inherent in such portfolios, which is often masked in private equity due to infrequent valuations.

Building on this foundation, Stafford ([2021](https://arxiv.org/html/2510.23183v1#bib.bib21)) introduced a strategy that replicates private equity buyouts by constructing portfolios of small public companies with low valuation multiples, such as EV/EBITDA. By applying incremental leverage and matching the holding periods of private equity investments, this strategy successfully simulates the risk-return profile of PE funds. Stafford’s analysis revealed alphas ranging from -2.4% to 11%, with the highest alpha observed in portfolios comprising stocks with the lowest valuations. This study demonstrated the feasibility of achieving competitive returns without the illiquidity constraints of private equity. However, replication portfolios face limitations, including irregular and infrequent cash flows and potential data inaccuracies, complicating risk-adjusted performance evaluation.

An alternative approach to replication is provided by Thomson Reuters Private Equity Index (as presented in Thomson Reuters ([2014](https://arxiv.org/html/2510.23183v1#bib.bib22))), which uses a sector-based methodology to achieve greater scalability. This method focuses on broad industry groups to create a replicable benchmark for private equity returns. By emphasizing sector allocation rather than individual company selection, this index offers a more scalable and accessible approach for investors seeking PE-like exposure. However, it may lack the granularity of strategies that rely on specific valuation multiples or leverage criteria

Gupta and Van Nieuwerburgh ([2021](https://arxiv.org/html/2510.23183v1#bib.bib9)) provide a complementary perspective by introducing a strip-by-strip valuation method that constructs a replicating portfolio using cash flows from listed equities and fixed-income instruments. Their model splits the risk-adjusted returns of private equity investments into individual cash flow components, capturing the timing, risk, and macroeconomic correlations of PE returns. While not explicitly a replication strategy, this approach provides valuable insights into the granular drivers of private equity performance and highlights the limitations of traditional replication methods.

Despite the promise of replication strategies, several challenges remain. Private equity funds are characterized by irregular and discretionary cash flows, making it difficult to match their performance with public market portfolios. Traditional risk estimation methods, such as time-series regressions, often struggle to account for the lagged and non-transparent valuations of private equity funds. Furthermore, replicating the operational and governance improvements brought by private equity general partners remains a significant hurdle, as these value-creation mechanisms are difficult to mirror in public market portfolios.

## 3 Methodology

### 3.1 Goal

The objective of this study is to replicate the performance of private equity benchmarks such as the Cambridge Associates, Preqin, or Bloomberg Private Equity Buyout Index. These benchmarks exhibit significantly higher Sharpe ratios, typically around 1.5, far above the traditional Sharpe ratio of approximately 0.5 observed in major large equity indexes. Moreover, they exhibit reduced drawdowns, lower volatility and superior annualized performance, ranging from 11% to close to 15%. However, these traditional benchmarks present significant limitations: they are published quarterly, often with delays of up to three months, making direct daily replication practically unfeasible.

### 3.2 Performance of Private Equity Benchmarks

Table [1](https://arxiv.org/html/2510.23183v1#S3.T1 "Table 1 ‣ 3.2 Performance of Private Equity Benchmarks ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") presents the historical performance of two widely recognized private equity benchmarks: the Cambridge Associates (CA) and Preqin indexes. Both exhibit strong annualized returns (13.9% and 14.2%, respectively) and moderate volatility (8.9% and 7.5%). Their Sharpe ratios of 1.56 and 1.89 indicate a favorable risk-adjusted return profile, while their drawdowns remain relatively contained. Notably, the 10% worst drawdowns are significantly lower than those observed in traditional equity markets, reinforcing the stability of these benchmarks.

Table 1: Performance of Traditional Private Equity Indexes

|  |  |  |
| --- | --- | --- |
|  | Cambridge Associates (CA) | Preqin |
| Start Date | 31/03/2011 | 31/03/2011 |
| End Date | 29/12/2023 | 29/12/2023 |
| Annual Return | 13.9% | 14.2% |
| Annual Volatility | 8.9% | 7.5% |
| Skew | -0.27 | 0.06 |
| Kurtosis | 1.64 | 1.46 |
| Sharpe Ratio | 1.56 | 1.89 |
| Sortino Ratio | 2.18 | 2.66 |
| Max DD | 9.5% | 7.3% |
| 10% Worst DD | 3.7% | 1.7% |
| Return/maxDD | 1.5 | 1.9 |
| Return/Worst 10% DD | 3.8 | 8.5 |
| Sampling | quarterly | quarterly |

Similarly, the Bloomberg Private Equity indexes, shown in Table [2](https://arxiv.org/html/2510.23183v1#S3.T2 "Table 2 ‣ 3.2 Performance of Private Equity Benchmarks ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity"), illustrate another perspective on private equity performance. The Bloomberg PEALL index has a slightly lower return (11.4%) compared to the Cambridge Associates and Preqin indexes but benefits from the lowest volatility (5.9%) and the highest Sharpe ratio (1.95). The Bloomberg PEBUY index, on the other hand, delivers a stronger annual return of 13.2% with a slightly higher volatility of 7.6%. These indexes confirm the robust risk-return characteristics of private equity investments, with both outperforming traditional equity benchmarks on a risk-adjusted basis.

Table 2: Performance of Bloomberg Private Equity Indexes

|  |  |  |
| --- | --- | --- |
|  | Bloomberg PEALL | Bloomberg PEBUY |
| Start Date | 31/03/2011 | 31/03/2011 |
| End Date | 29/12/2023 | 29/12/2023 |
| Annual Return | 11.4% | 13.2% |
| Annual Volatility | 5.9% | 7.6% |
| Skew | -0.29 | -0.54 |
| Kurtosis | 0.82 | 1.75 |
| Sharpe Ratio | 1.95 | 1.73 |
| Sortino Ratio | 4.07 | 2.34 |
| Max DD | 5.2% | 8.9% |
| 10% Worst DD | 2.% | 2.1% |
| Return/maxDD | 2.2 | 1.5 |
| Return/Worst 10% DD | 5.6 | 6.2 |
| Sampling | quarterly | quarterly |

The correlation matrix in Table [3](https://arxiv.org/html/2510.23183v1#S3.T3 "Table 3 ‣ 3.2 Performance of Private Equity Benchmarks ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") reveals two distinct benchmark groups. The Cambridge Associates (CA) benchmark is relatively independent, with a 61% correlation with Preqin and even lower correlations with the Bloomberg indexes (PEBUY: 75%, PEALL: 70%), suggesting a unique return pattern.

In contrast, Preqin, PEBUY, and PEALL are highly correlated, with Preqin at 91% with PEBUY and 96% with PEALL, while PEBUY and PEALL are nearly identical at 97%. This suggests that Preqin closely tracks the Bloomberg indexes, likely due to similar methodologies.

Thus, the benchmarks form two distinct families: (1) the independent CA benchmark and (2) the highly correlated Preqin, PEBUY, and PEALL benchmarks.

Table 3: Correlation between quarterly benchmarks

|  | CA | Prequin | PEBUY | PEALL |
| --- | --- | --- | --- | --- |
| CA | 100% |  |  |  |
| Prequin | 61% | 100% |  |  |
| PEBUY | 75% | 91% | 100% |  |
| PEALL | 70% | 96% | 97% | 100% |

### 3.3 Challenges and Alternatives with daily indexes

Despite their strong performance, these quarterly benchmarks suffer from reporting delays and lack of daily liquidity, making them impossible to replicate in real-time portfolios. As an alternative, daily liquid proxies such as the Erik Stafford (Stafford) single-stock selection method implemented via the SummerHaven Private Equity Strategy Index (SHPEISM Index), the Thomson Reuters Refinitiv (TR) Private Equity Benchmark provide more frequent quotations.

Table [4](https://arxiv.org/html/2510.23183v1#S3.T4 "Table 4 ‣ 3.3 Challenges and Alternatives with daily indexes ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") highlights the key differences between these daily liquid indexes and traditional private equity benchmarks. While the Thomson Reuters index achieves a respectable 12.5% annualized return, its volatility (24.8%) is significantly higher than that of quarterly benchmarks. Similarly, the Erik Stafford method, though often cited as a viable daily proxy, delivers lower annualized returns (10.9%) and exhibits even greater volatility (25.9%). The Listed Private Equity (Listed PE) index, while sharing the same annualized return (10.9%) as the Stafford index, demonstrates lower volatility (20.2%), resulting in a slightly improved Sharpe ratio (0.54). However, it exhibits a highly negative skew (-0.78) and extreme kurtosis (18.2), indicating a tendency toward large outlier events. This suggests that while the Listed index may appear more stable under normal market conditions, it is more prone to extreme tail-risk events. Its maximum drawdown (50.4%) is the highest among the three indexes, further reinforcing this concern. Interestingly, the 10% worst drawdowns (24.8%) are lower than those observed for the TR index (33.4%), suggesting that its typical downside risk is more contained despite its vulnerability to extreme tail losses.

Table 4: Performance of Daily Liquid Indexes

|  | Stafford | TR | Listed PE |
| --- | --- | --- | --- |
| Start Date | 31/03/2011 | 31/03/2011 | 31/03/2011 |
| End Date | 21/01/2025 | 21/01/2025 | 21/01/2025 |
| Annual Return | 10.90% | 12.50% | 10.90% |
| Annual Volatility | 25.90% | 24.80% | 20.20% |
| Skew | -0.33 | -0.64 | -0.78 |
| Kurtosis | 3.02 | 1.55 | 18.2 |
| Sharpe Ratio | 0.42 | 0.5 | 0.54 |
| Sortino Ratio | 0.52 | 0.62 | 0.63 |
| Max DD | 47.20% | 41.70% | 50.40% |
| 10% Worst DD | 21.10% | 33.40% | 24.80% |
| Return/maxDD | 0.2 | 0.3 | 0.2 |
| Return/Worst 10% DD | 0.5 | 0.4 | 0.4 |
| Sampling | daily | daily | daily |

As a result, these three daily benchmarks (Stafford, TR and Listed PE) suffer from substantially lower Sharpe ratios (0.42, 0.5 and respectively 0.54) and much deeper drawdowns (max drawdowns of 47.2%, 41.7% and respectively 50.4%). These findings underscore the challenges in replicating private equity performance with daily liquid instruments, as the trade-off between liquidity and performance (both in terms of Sharpe ratio and maximum drawdowns) remains substantial.

### 3.4 Objective of This Study

Given these limitations, this study aims to bridge the gap between quarterly private equity benchmarks and daily tradable alternatives. The goal is to construct a daily-replicable strategy that maintains the attractive risk-return profile of private equity indexes while avoiding their structural drawbacks, such as reporting delays and illiquidity. By leveraging insights from traditional and liquid proxies, this approach seeks to create an optimized model capable of closely mimicking private equity performance with a higher frequency of valuation.

### 3.5 Two-step Approach

To achieve this ambitious goal, we employ a two-step approach. First, we decode the daily benchmark with high accuracy using advanced graphical models, as outlined in Section [3.6](https://arxiv.org/html/2510.23183v1#S3.SS6 "3.6 Graphical Model Primer ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity"). This approach improves upon traditional replication methods, such as repetitive penalized linear regression, which suffers from issues like inconsistent weights and difficulties in determining when to update the model. Roncalli and Teiletche ([2007](https://arxiv.org/html/2510.23183v1#bib.bib20)) explored Kalman filtering to provide dynamic updates and correction mechanisms. Building on this, Benhamou et al. ([2024](https://arxiv.org/html/2510.23183v1#bib.bib6)), Ohana et al. ([2022](https://arxiv.org/html/2510.23183v1#bib.bib17)) demonstrated that incorporating graphical models could enhance Kalman filters by introducing richer interaction modeling between assets.

The second step introduces asymmetries to address the discrepancies between daily benchmarks and quarterly private equity indexes. By incorporating tailored factors, we aim to replicate the more stable performance profiles of quarterly benchmarks while capturing critical dynamics such as drawdown mitigation and volatility control.
The asymmetrical transformation of the daily index accounts for the tendency of private equity funds to mitigate negative returns. This is achieved by scaling down negative returns to reduce drawdown, mimicking the arbitrary valuation practices often employed by private equity funds. Specifically, for any negative returns, only 9%9\% of the return is considered. Additionally, we introduce new asymmetrical factors, denoted as A​FAF, to represent this adjustment.

The initial daily private equity benchmark return RtR\_{t} is transformed as follows:

|  |  |  |
| --- | --- | --- |
|  | Rt′={Rt,if ​Rt≥0,A​F⋅Rt,if ​Rt<0,R\_{t}^{\prime}=\begin{cases}R\_{t},&\text{if }R\_{t}\geq 0,\\ AF\cdot R\_{t},&\text{if }R\_{t}<0,\end{cases} |  |

where A​F=0.9AF=0.9.

Thus, the transformation ensures that positive returns remain unchanged, while negative returns are scaled down to 9%9\%, reflecting the drawdown adjustment characteristic of private equity valuations.

The full methodology is outlined in Algorithm [1](https://arxiv.org/html/2510.23183v1#alg1 "Algorithm 1 ‣ 3.5 Two-step Approach ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity"), following a structured process with the different steps described below:

* •

  We first decode a liquid daily proxy of private equity funds based either on the Erik Stafford, Thomson Reuters or he listed private equity indices (step 1).
* •

  We then introduce asymmetry in the returns by applying an adjustment factor to account for reduced drawn downs to better align with quarterly private equity funds indexes (step 2)
* •

  We finally evaluate the performance of decoding in terms of returns compared to quarterly benchmark (steps 3 and 4).
* •

  We finally add some model constraints to ensure the model will stay within historical bounds and to prevent extreme weight deviations (steps 5 and 6).

Algorithm 1  Decoding Liquid Daily Proxy for Private Equity Funds with Additional Steps for Sanity Check

1: Step 1: Decode liquid daily proxy for private equity funds using equity index futures either using Erik Stafford, Thomson Reuters or the S&P listed private equity index

2: Step 2: Introduce asymmetry in decoding the daily benchmark by reducing the size of negative returns by ten percents.

3: Step 3: Perform Maximum Likelihood Optimization on model parameters during training to generate the initial decoding model

4: Step 4: Run backtesting only on the test period with continuous prediction correction steps

5: Step 5: Check historical weights as a sanity check and validate that weights are not blowing up.

6: Step 6: Add constraints on the minimum and maximum historical weights to prevent model explosion

### 3.6 Graphical Model Primer

Graphical models provide a robust framework for dynamic Bayesian inference, enabling us to decode daily benchmarks effectively. These models represent the relationships between variables as a network of nodes (variables) and edges (dependencies), facilitating the estimation of the most probable allocations at each time step.

The methodology begins with constructing a probabilistic graphical model, as illustrated in Figure [1](https://arxiv.org/html/2510.23183v1#S3.F1 "Figure 1 ‣ 3.6 Graphical Model Primer ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity"). The overall idea is to capture the relationships between the weights in the various assets and the observed NAVs. The dynamic inference is done by incorporating time-dependent priors and observations, making it well-suited for daily updates. If we denote by N​A​VtNAV\_{t}, the observed net asset value of a fund, and assume various assets (Eq, Fx, Ir and Co), we are interested in finding the weights in these assets given the observed NAVs. If we denote by wte​q,wtF​x,wtI​rw^{eq}\_{t},w^{Fx}\_{t},w^{Ir}\_{t} and wtC​ow^{Co}\_{t} the respective weights, and by rte​q,rtF​x,rtI​rr^{eq}\_{t},r^{Fx}\_{t},r^{Ir}\_{t} and rtC​or^{Co}\_{t}, as well as the predicted N​A​V^t\widehat{NAV}\_{t}, the underlying relationship between latent nodes and observed node is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​A​V^t=N​A​V^t−1​(1+wt−1E​q​rtE​q+…+wt−1C​o​rtC​o)\widehat{NAV}\_{t}=\widehat{NAV}\_{t-1}\left(1+w^{Eq}\_{t-1}r^{Eq}\_{t}+\ldots+w^{Co}\_{t-1}r^{Co}\_{t}\right) |  | (1) |

Equation [1](https://arxiv.org/html/2510.23183v1#S3.E1 "In 3.6 Graphical Model Primer ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") reflects that the estimated NAV at time tt is obtained by adding the weighted returns of each asset to the previous estimated NAV, with the weights determined at the prior time step, t−1t-1.

Key steps in the graphical model approach include:

1. 1.

   State Space Representation: The weights are modeled as latent states influenced by observable asset prices and previous weights. This model is more precise than the Kalman filter, as the Kalman filter only accounts for interactions within each individual asset, without considering interactions between different assets.
2. 2.

   Dynamic Inference: Bayesian inference techniques, such as message passing algorithms, is used to estimate the latent states at each time step with a prediction correction step like in Kalman filter, hence making it more robust than piecewise regressions that do not account for previous weights in their estimations.
3. 3.

   Interaction Modeling: The graphical model accounts for interactions between assets, allowing for richer modeling compared to traditional independent assumptions.
4. 4.

   Updating Mechanisms: The model dynamically updates the allocation probabilities as new data becomes available, ensuring adaptability to changing market conditions. This ensures that the model continuously improves itself.

The graphical model framework enhances replication accuracy compared to other approach and provides insights into the underlying dynamics of the daily benchmark. Even if graphical models remain largely unknown to the financial community, they have been widely used in Machine Learning Murphy ([2012](https://arxiv.org/html/2510.23183v1#bib.bib16)) and have been the underlying building block for voice and world detection of the early versions of Apple Siri application.

Timet=1t=1t=2t=2t=3t=3t=4t=4NAV1NAV2NAV3NAV4Eq1Fx1Ir1Co1Eq2Fx2Ir2Co2Eq3Fx3Ir3Co3Eq4Fx4Ir4Co4

|  |  |
| --- | --- |
|  | Latent node (Eq, Fx, Ir, Co) |
|  | Observed node (NAVt) |

Simplified Graphical Model for Time Inference

Figure 1: Simplified graphical model showing the relationship between observed NAv and inferred allocation as time goes by. For illustration purpose, we use different assets, with one being an Equity shortened in Eq, a second one an exchange rate shorted in Fx, a third one, an interest rates instrument shortened in Ir and finally a commodity asset shortened in Co.

### 3.7 Asymmetric Factors

To align the daily benchmark more closely with quarterly private equity indexes, we introduce asymmetric factors to address the discrepancies in drawdowns and risk profiles. Private equity benchmarks typically exhibit smoother performance and reduced volatility due to their infrequent valuations and long-term investment horizons.

We incorporate the following asymmetric factors into our model:

1. 1.

   Tail Risk Strategies: Using volatility indices such as the VIX, we design strategies that hedge against extreme market movements, thereby mitigating pronounced drawdowns in the daily benchmark. A novel tail risk strategy is proposed to systematically capitalize on upward movements in VIX Futures by establishing long positions in either the front-end month (short-term, ST VIX) or the fourth-month (medium-term, MT VIX) futures, contingent upon prevailing market conditions. The core methodology employs a machine learning framework that identifies relatively infrequent yet pronounced positive trends in the VIX Futures curve based on three indicators:

   1. (a)

      The 20-day Volatility-Adjusted Return on the VIX Future, which captures short-term momentum.
   2. (b)

      The VIX Curve Future Ratio—defined as the ratio of the next VIX Future to the current VIX Future—to assess potential carry benefits for long VIX positions.
   3. (c)

      The overall level of the VIX, which reflects the mean reversion dynamics that often arise during periods of heightened or protracted market volatility.

   Once these indicators generate a probabilistic “activation signal,” the model allocates positions to ST VIX and MT VIX accordingly. By toggling between the front-month and fourth-month segments of the VIX curve, this approach achieves a more nuanced exposure to volatility, allowing it to capture both acute market shocks and longer-duration volatility regimes.

   Empirical findings indicate that integrating this Tail Risk Hedge Vol Strategy as an overlay on equity-oriented portfolios can bolster risk-adjusted performance metrics. Over the period from January 2007 to December 2024, the strategy not only enhances returns but also reduces overall portfolio volatility, resulting in a 71% increase in the Sharpe Ratio and a 2.5-fold improvement in the Return to Maximum Drawdown (Max DD). During low-volatility regimes—when equity markets tend to be complacent—this overlay provides a protective buffer against potential market downturns. Notably, the addition of the hedge lifts the annual return from 9% to 12%, while reducing annual volatility from 20% to 16% and curtailing the maximum drawdown from 56% to 29%. These results underscore the potential of a machine learning–driven tail risk hedge to enhance portfolio resilience and improve long-term investment outcomes.
2. 2.

   Momentum Strategies: Building on a traditional CTA cross-asset class framework, this strategy leverages a dedicated *risk-off filter*, implemented through a non-linear Hysteresis Filtering Algorithm, to systematically identify and prioritize trends negatively correlated with the global equity market. Demonstrating robust diversification capabilities, the strategy achieves a -36% correlation with the S&P 500 and delivers positive returns in 88% of months when the S&P 500 declines by more than -5% over the period 2010–2024. Furthermore, it generates an average monthly return of 3.6% during such downturns, outperforming the Benchmark Index of CTAs by a factor of two. By integrating momentum-based factors with the risk-off filter, the strategy provides superior hedging performance during medium- to long-term equity market declines while maintaining consistent risk-adjusted returns. These attributes establish the strategy as a useful tool for mitigating portfolio drawdowns and enhancing resilience in volatile market environments.

These asymmetric factors enhance the daily benchmark’s performance by reducing drawdowns and aligning its risk-return profile more closely with quarterly benchmarks, making it a viable alternative for replicating private equity returns.

## 4 Results and Statistics

### 4.1 Data description

We use for daily private equity funds three proxy indexes: the Erik Stafford whose Bloomberg ticker is SHPEI Index, the Thomson Reuters Refinitiv Private Equity Benchmark whose Bloomberg ticker is TRPEI Index and the S&P listed private equity funds whose Bloomberg ticker is SPLPEQNT Index. We collect data from 2005 up to January 21st 2025. We train our graphical model from 2005 up to end of 2010. The test set starts from 31 March 2011 as the Preqin index only starts at this dates. The performance benchmark in terms of private equity funds are the seminal quarterly indexes used by the private equity industry, namely the Cambridge Associates, the Preqin and the Bloomberg Private Equity Buyout (PEBUY) and the rivate Equity All (PEALL) Index.

### 4.2 Replication Accuracy

In order to determine the replication quality and accuracy in the proposed PEARL framework, we not only provide the key statistics in Table [5](https://arxiv.org/html/2510.23183v1#S4.T5 "Table 5 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") but also their respective correlation with their initial benchmarks in Table [6](https://arxiv.org/html/2510.23183v1#S4.T6 "Table 6 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity").

Table 5: Performance of decoding of the three strategies: Listed Private Equities Companies (Listed PE), Thomson Reuters (TR) and Erik Stafford (Stafford)

|  | Decoding | | |
| --- | --- | --- | --- |
|  | Listed PE | TR | Stafford |
| Start Date | 02/01/2012 | 02/01/2012 | 02/01/2012 |
| End Date | 21/01/2025 | 21/01/2025 | 21/01/2025 |
| Annual Return | 17.1% | 17.7% | 17.4% |
| Annual Volatility | 13.6% | 14.0% | 14.2% |
| Auto Correlation | 3.5% | 0.6% | 1.0% |
| Skew | -0.26 | -0.23 | -0.25 |
| Kurtosis | 4.48 | 3.75 | 4.1 |
| Sharpe Ratio | 1.26 | 1.27 | 1.23 |
| Sortino Ratio | 1.69 | 1.72 | 1.67 |
| Max DD | 17.6% | 19.2% | 19.2% |
| 10% Worst DD | 9.5% | 8.6% | 9.5% |
| Return/maxDD | 1 | 0.9 | 0.9 |
| Return/Worst 10% DD | 1.8 | 2.1 | 1.8 |




Table 6: Correlation of strategies with their benchmarks

| Strategy | Lifetime | 1Y | 3Y | 5Y | 7Y | 10Y |
| --- | --- | --- | --- | --- | --- | --- |
| Stafford | 64% | 94% | 68% | 81% | 73% | 71% |
| Listed PE | 63% | 89% | 65% | 79% | 75% | 72% |
| TR | 69% | 97% | 71% | 81% | 78% | 76% |

Table [5](https://arxiv.org/html/2510.23183v1#S4.T5 "Table 5 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") presents the decoding performance of the three strategies: Listed Private Equities Companies (Listed PE), Thomson Reuters (TR), and Erik Stafford (Stafford). Across all strategies, the annualized returns are comparable, with TR achieving the highest return (17.7%), followed closely by Stafford (17.4%) and Listed PE (17.1%). In terms of volatility, levels remain similar, with Listed PE exhibiting the lowest overall volatility (13.6%) and Stafford the highest (14.2%).

The autocorrelation measure is highest for Listed PE (3.5%), suggesting greater persistence in returns compared to TR (0.6%) and Stafford (1.0%). Skewness values indicate a slight negative bias across all strategies, with TR exhibiting the lowest absolute skew (-0.23), while kurtosis is highest for Listed PE (4.48), suggesting a higher occurrence of extreme events.

In terms of key performance ratios, as measured by the Sharpe and Sortino ratios, the three strategies are quite comparable with TR displaying a slight edge in both metrics (Sharpe: 1.27, Sortino: 1.72). Drawdown analysis highlights that Listed PE has the lowest maximum drawdown (17.6%) compared to TR and Stafford (both at 19.2%). Finally, return-to-drawdown ratios indicate that Listed PE achieves the highest Return/MaxDD (1.0) and Return/Worst 10% DD (1.8), although TR surpasses it in the latter metric (2.1). These findings suggest that while TR offers the highest returns and strong downside protection in extreme cases, Listed PE provides the most stable return profile with lower overall volatility and drawdown risk.

The results presented in Table [5](https://arxiv.org/html/2510.23183v1#S4.T5 "Table 5 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") (decoding performance of the PEARL strategy) demonstrate a significant improvement over the daily liquid benchmarks in Table [4](https://arxiv.org/html/2510.23183v1#S3.T4 "Table 4 ‣ 3.3 Challenges and Alternatives with daily indexes ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity"), while more closely aligning with the traditional private equity benchmarks in Tables [1](https://arxiv.org/html/2510.23183v1#S3.T1 "Table 1 ‣ 3.2 Performance of Private Equity Benchmarks ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") and [2](https://arxiv.org/html/2510.23183v1#S3.T2 "Table 2 ‣ 3.2 Performance of Private Equity Benchmarks ‣ 3 Methodology ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity").

First, the annualized returns of the PEARL strategy (17.1%–17.7%) are notably higher than those of the daily liquid indexes (10.9%–12.5%), while being comparable to, or exceeding, the traditional quarterly benchmarks (11.4%–14.2%). This suggests that the PEARL approach captures a return profile more consistent with long-term private equity performance.

Second, the Sharpe ratios for PEARL (1.23–1.27) significantly outperform those of the daily liquid indexes (0.42–0.54), highlighting superior risk-adjusted performance. While the Sharpe ratios remain slightly below those of traditional private equity benchmarks (1.56–1.95), the PEARL strategy represents a substantial enhancement in stability and efficiency relative to daily liquid proxies.

Additionally, PEARL exhibits lower maximum drawdowns (17.6%–19.2%) than the daily liquid benchmarks (41.7%–50.4%), reducing downside risk exposure. Although traditional private equity indices still demonstrate superior drawdown resilience, with max drawdowns below 10%, PEARL significantly mitigates the volatility and deep drawdowns characteristic of daily replication strategies.

These findings confirm that the PEARL strategy achieves a better balance between liquidity and performance, bridging the gap between daily liquid instruments and traditional private equity benchmarks. By enhancing returns, reducing drawdowns, and improving risk-adjusted returns, PEARL represents a meaningful advancement over existing daily replication approaches.

Table 7: Correlation between strategies

|  | Stafford | Listed PE | TR |
| --- | --- | --- | --- |
| Stafford | 100% | 83% | 74% |
| Listed PE | 83% | 100% | 83% |
| TR | 74% | 83% | 100% |




Table 8: Yearly returns

|  | Benchmark | | | Decoding | | |
| --- | --- | --- | --- | --- | --- | --- |
| Years | Listed PE | TR | Stafford | Listed PE | TR | Stafford |
| 2025 | 4.5% | 4.6% | 3.2% | 2.2% | 1.8% | 1.6% |
| 2024 | 24.0% | 31.3% | 2.7% | 16.0% | 16.1% | 16.2% |
| 2023 | 39.0% | 4.4% | 23.1% | 22.5% | 21.3% | 20.6% |
| 2022 | -29.0% | -31.1% | -11.1% | -4.2% | -4.0% | -1.1% |
| 2021 | 41.8% | 29.8% | 43.4% | 13.2% | 12.8% | 10.3% |
| 2020 | 4.5% | 25.6% | 17.1% | 52.3% | 53.2% | 52.2% |
| 2019 | 44.6% | 37.4% | 12.6% | 31.6% | 32.0% | 30.3% |
| 2018 | -14.0% | -11.9% | -14.7% | -8.9% | -7.9% | -8.4% |
| 2017 | 24.3% | 31.5% | 7.5% | 13.8% | 14.3% | 12.2% |
| 2016 | 13.6% | 8.6% | 28.5% | 9.3% | 10.2% | 11.2% |
| 2015 | -3.2% | 6.7% | -9.4% | 7.7% | 9.8% | 8.0% |
| 2014 | -1.6% | 20.6% | 7.8% | 32.5% | 39.6% | 40.2% |
| 2013 | 35.3% | 42.6% | 47.0% | 32.2% | 30.7% | 31.7% |
| 2012 | 29.0% | 20.4% | 17.9% | 16.0% | 15.4% | 16.0% |

Table [7](https://arxiv.org/html/2510.23183v1#S4.T7 "Table 7 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") is also consistent with the findings that the three strategies are quite similar. It shows strong correlations among the three strategies, with Listed PE exhibiting the highest alignment (83%) with both Stafford and TR. TR has the lowest correlation with Stafford (74%), suggesting some diversification benefits. Overall, the high correlations indicate that the choice of the liquid daily benchmark is not so meaningful.

Additionally, Table [6](https://arxiv.org/html/2510.23183v1#S4.T6 "Table 6 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") demonstrates that the PEARL method achieves a high correlation with its decoded benchmarks, particularly in shorter time horizons. The one-year correlations exceed 89% for all strategies, indicating strong short-term alignment with the benchmark. Over the lifetime period, correlations remain robust (63%–69%), confirming the PEARL method’s ability to effectively replicate private equity characteristics while maintaining liquidity. These results highlight the strategy’s effectiveness in capturing the dynamics of private equity performance with high fidelity.

Last but not least, Table [8](https://arxiv.org/html/2510.23183v1#S4.T8 "Table 8 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") and Figure [2](https://arxiv.org/html/2510.23183v1#S4.F2 "Figure 2 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") illustrate the yearly performance of private equity decoding strategies relative to their benchmarks. The PEARL method consistently tracks benchmark trends while mitigating extreme losses, particularly during downturns (e.g., 2022 and 2018). These results highlight the strategy’s effectiveness in capturing private equity returns with improved downside protection.

![Refer to caption](images/PrivateEquityComparison.png)

Figure 2: Comparison of Private Equity Returns decoding strategies with their benchmarks

Figure [2](https://arxiv.org/html/2510.23183v1#S4.F2 "Figure 2 ‣ 4.2 Replication Accuracy ‣ 4 Results and Statistics ‣ PEARL: Private Equity Accessibility Reimagined with Liquidity") visually compares the PEARL decoding strategies with their respective private equity benchmarks. The figure highlights the strong alignment between the decoded and benchmark returns while demonstrating the PEARL method’s ability to reduce volatility and mitigate extreme drawdowns and hence reproduce performance more in line with the quarterly benchmarks like the ones of Cambridge Associate, Preqin or Bloomberg indexes. Notably, the strategy effectively smooths negative shocks, as observed in 2022 and 2018, while maintaining competitive returns in high-growth periods, in a similar way as private equity funds do.

## 5 Conclusion

In this work, we introduced PEARL (Private Equity Accessibility Reimagined with Liquidity), an innovative AI-driven framework designed to replicate private equity (PE) funds using liquid and cost-effective assets. The methodology leverages advanced graphical models to decode daily benchmarks with high precision, addressing the limitations of existing replication approaches. By incorporating asymmetric factors such as tail risk and momentum strategies, PEARL aligns daily benchmark performance more closely with renowned private equity indexes like the Cambridge Associates and Preqin benchmarks. Overall, PEARL provides a significant step forward in making private equity funds liquid while maintaining its core performance characteristics in line with top private equity funds.
Future research could explore enhancements to the graphical model framework, particularly through deeper integration of macroeconomic indicators and alternative asset classes, to further improve replication accuracy.

## References

* Acharya et al. (2009)

  Viral V Acharya, Conor Kehoe, and Michael Reyner.
  Private equity vs. plc boards in the uk: A comparison of practices and effectiveness.
  Journal of Applied Corporate Finance, 21(1):45–56, 2009.
* Ang et al. (2014a)

  Andrew Ang, Bingxu Chen, William Goetzmann, and Ludovic Phalippou.
  Estimating private equity returns from limited partner cash flows.
  Technical Report 13-83, Columbia Business School Research Paper, 2014.
* Ang et al. (2014b)

  Andrew Ang, Dimitris Papanikolaou, and Mark M. Westerfield.
  Portfolio choice with illiquid assets.
  Management Science, 60(11):2737–2761, 2014.
* Axelson et al. (2013)

  Ulf Axelson, Tim Jenkinson, Per Strömberg, and Michael Weisbach.
  Borrow cheap, buy high? the determinants of leverage and pricing in buyouts.
  The Journal of Finance, pages 2223–2269, 2013.
* BCG (2020)

  BCG.
  Global Asset Management 2020, May 2020.
  Retrieved from Boston Consulting Group.
* Benhamou et al. (2024)

  Eric Benhamou, Jean-Jacques Ohana, and Beatrice Guez.
  GRIP: Graphical models revealing insights for portfolio replication - a learning approach.
  SSRN Electronic Journal, April 2024.
* Döskeland and Strömberg (2018)

  Trond Döskeland and Per Strömberg.
  Evaluating investments in unlisted equity for the norwegian government pension fund global (gpfg).
  Swedish House of Finance Research Paper, 1(23-03), 2018.
* Franzoni et al. (2012)

  Francesco Franzoni, Eric Nowak, and Ludovic Phalippou.
  Private equity performance and liquidity risk.
  The Journal of Finance, 67(6):2341–2373, 2012.
* Gupta and Van Nieuwerburgh (2021)

  Arpit Gupta and Stijn Van Nieuwerburgh.
  Valuing private equity investments strip by strip.
  The Journal of Finance, 76(6):3255–3307, 2021.
* Jensen (1986)

  Michael Jensen.
  Agency costs of free cash flow, corporate finance, and takeovers.
  The American Economic Review, pages 323–329, 1986.
* Kaplan and Schoar (2005)

  Steven N. Kaplan and Antoinette Schoar.
  Private equity performance: Returns, persistence, and capital flows.
  The Journal of Finance, 60(4):1791–1823, 2005.
* Kaplan and Strömberg (2009)

  Steven Kaplan and Per Strömberg.
  Leveraged buyouts and private equity.
  Journal of Economic Perspective, 23:121–146, 2009.
* Markowitz (1952)

  Harry Markowitz.
  Portfolio selection.
  The Journal of Finance, pages 77–91, 1952.
* McKinsey (2020)

  McKinsey.
  McKinsey’s Private Markets Annual Review, February 19 2020.
  Retrieved from McKinsey.
* McKinsey (2023)

  McKinsey.
  Mckinsey’s private markets annual review 2023.
  McKinsey Insights, 2023.
  Accessed online at <https://www.mckinsey.com/industries/private-capital/our-insights/mckinseys-private-markets-annual-review>.
* Murphy (2012)

  Kevin P Murphy.
  Machine learning: a probabilistic perspective.
  MIT press, 2012.
* Ohana et al. (2022)

  Jean-Jacques Ohana, Eric Benhamou, David Saltiel, and Beatrice Guez.
  Deep decoding of strategies.
  SSRN Electronic Journal, June 2022.
* Rasmussen and Chinono (2015)

  Daniel Rasmussen and Brian Chinono.
  Leveraged small value equities.
  Available at SSRN 2639647, 2015.
  Retrieved from SSRN.
* Robinson and Sensoy (2016)

  David T. Robinson and Berk A. Sensoy.
  Cyclicality, performance measurement, and cash flow liquidity in private equity.
  Journal of Financial Economics, 122(3):521–543, 2016.
* Roncalli and Teiletche (2007)

  Thierry Roncalli and Jerome Teiletche.
  An alternative approach to alternative beta.
  Available at SSRN 1035521, 2007.
* Stafford (2021)

  Erik Stafford.
  Replicating private equity with value investing, homemade leverage, and hold-to-maturity accounting.
  The Review of Financial Studies, 35(1):299–342, 02 2021.
* Thomson Reuters (2014)

  Thomson Reuters.
  Thomson Reuters Private Equity Buyout Index Methodology, 2014.
  Available at <https://www.thomsonreuters.com/content/dam/openweb/documents/pdf/tr-com-financial/methodology/private-equity-buyout-index-methodology.pdf>.