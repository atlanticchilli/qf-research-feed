---
authors:
- Sungwoo Kang
doc_id: arxiv:2512.14134v1
family_id: arxiv:2512.14134
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Sources and Nonlinearity of High Volume Return Premium: An Empirical Study
  on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)'
url_abs: http://arxiv.org/abs/2512.14134v1
url_html: https://arxiv.org/html/2512.14134v1
venue: arXiv q-fin
version: 1
year: 2025
---


Sungwoo Kang
  
Department of Electrical and Computer Engineering, Korea University, Seoul 02841, Republic of Korea
  
Email: krml919@korea.ac.kr

###### Abstract

This study demonstrates that both investor identity and trading intensity determine the High Volume Return Premium, but intensity effects only emerge when measured correctly. Using Korean market data (2020-2024), we show that institutional buying intensity normalized by market capitalization reveals a perfect monotonic relationship with future returns (Q4: +10.07%; Q1: -0.05%), while trading value normalization fails. Retail investors exhibit an inverted pattern, confirming noise trader behavior. This reconciles decades of conflicting evidence: intensity matters profoundly, but requires (1) investor-type conditioning, (2) nonlinear quartile analysis, and (3) conviction-based (market cap) rather than participation-based (trading value) measurement.

## I Introduction

The seminal work of https://doi.org/10.1111/0022-1082.00349 established the ’High Volume Return Premium (HVRP)’ phenomenon, whereby stocks experiencing abnormal trading volume subsequently generate significant excess returns. Their core mechanism is rooted in behavioral finance: investors with ’limited attention’ respond to ’attention shocks’ from volume spikes, creating new buying demand. This aligns with merton1987simple’s ’investor recognition hypothesis,’ which posits that increased stock visibility reduces the cost of capital.

In the Korean market, ART001162590 verified the HVRP phenomenon using 2001-2003 KOSPI data, finding stronger effects in large-cap firms. They surmised that this difference “may originate from differences in the main investor composition of the two groups, namely institutional versus individual investors.” However, due to data limitations at the time, this ’investor type hypothesis’ remained an untested hypothesis. Our study begins precisely at this ’research gap’ that ART001162590 raised but could not answer.

Testing this ’investor type hypothesis’ has profound academic significance beyond merely filling a 20-year-old domestic research gap—it provides contemporary evidence for a core and longstanding debate in finance: “What role do retail investors play in the market?”

* •

  The ’Noise Trader’ Camp: Led by 10.1093/rfs/hhm079, this group argues that retail investors are ’noise traders’ who overreact to attention-grabbing stocks rather than conducting professional analysis. Recent NBER research by https://doi.org/10.1111/jofi.13183 demonstrates that net purchases by new retail investors significantly negatively predict future returns, confirming their ’poor stock selection’ ability.
* •

  The ’Informed Trader’ Camp: Conversely, https://doi.org/10.1111/j.1540-6261.2008.01316.x, KANIEL2012255, and https://doi.org/10.1111/jofi.13033 argue that retail investors are rational traders who provide liquidity to institutions or act on information, with their net purchases positively predicting future returns.

Approximately 20 years after ART001162590’s study, modern markets have undergone two major structural changes. First, the COVID-19 pandemic (10.1093/rapstu/raaa008) caused unprecedented market volatility. During this period, retail investor trading through fintech platforms exploded, with these investors serving as ’liquidity providers’ absorbing institutional selling pressure, as Ozik\_Sadka\_Shen\_2021 documented. This provides new impetus for reinterpreting the drivers of HVRP. Second, the ’Donghak Ant Movement’ (ART002752798) parallels the ’Meme Stock’ phenomenon in U.S. markets. 10.1093/rfs/hhad098 showed that Reddit’s WallStreetBets community possessed significant information value before the GameStop event but deteriorated into noise afterward, suggesting that collective action can function as ’collective intelligence’ only under specific conditions.

Against this backdrop, we employ a novel ’Dual Validation Methodology’ to elucidate the essence of the HVRP phenomenon. We analyze HVRP events using (1) a categorical variable examining ’who’ led the event (institutions/foreigners vs. retail), and (2) a continuous variable measuring ’how intensely’ they led (Dominance Score). Remarkably, these two methodologies yielded starkly contrasting results. The categorical approach showed strong predictive power, while the continuous approach exhibited correlations converging to zero. This initially suggested that investor identity matters while intensity does not.

However, our central discovery is that this initial interpretation was incomplete. By introducing a double-sort methodology that combines investor type classification with quartile-based intensity analysis, we uncover a powerful monotonic relationship that prior methods obscured. For institutional investors, events in the highest conviction quartile (measured as net buying relative to market capitalization) generate cumulative abnormal returns of +10.07% over 50 days, while the lowest quartile yields near-zero returns (-0.05%). This perfect monotonic pattern (Q1¡Q2¡Q3¡Q4) demonstrates that intensity matters profoundly—but only when measured correctly.

The critical methodological insight is that how we normalize intensity determines whether we detect informed trading signals. When intensity is normalized by daily trading value (measuring participation in trading flow), the monotonic pattern breaks down completely (Q3: +12.33% ¿ Q4: +4.22%). But when normalized by market capitalization (measuring conviction as position size relative to firm value), the relationship becomes crystal clear. This demonstrates that the near-zero correlation with the Dominance Score does not mean intensity is irrelevant; it means the relationship is nonlinear, type-dependent, and critically sensitive to measurement specification. Prior studies may have missed this relationship by using inappropriate normalization benchmarks or failing to account for investor heterogeneity.

Therefore, our study has four objectives. First, we replicate ART001162590’s study with 2020-2024 data to verify whether the HVRP phenomenon remains robust despite the 20-year gap and market structural changes. Second, we conduct the first empirical test of the ’investor type hypothesis’ that remained an ’inference’ in the original study, using actual investor-level trading data. This positions our findings within the core finance debate of “noise traders” (10.1093/rfs/hhm079) versus “informed traders” (https://doi.org/10.1111/j.1540-6261.2008.01316.x). Third, we demonstrate that trading intensity matters profoundly but is only detectable when measured correctly—specifically, when normalized by market capitalization rather than trading value, revealing a monotonic conviction-return relationship that prior methods obscured. Fourth, we analyze how modern market phenomena—the COVID-19 shock and ’Donghak Ant Movement’—moderate these core relationships, demonstrating that extreme conditions can temporarily transform traditional patterns.

## II Literature Review and Hypothesis Development

This study goes beyond merely confirming the existence of the High Volume Return Premium (HVRP) to identify its sources—’who’ (Who) generates it, and whether it is a matter of ’how much’ (How much) or ’what context’ (Context) from a contemporary perspective.

### A Theoretical Background: Beyond Visibility Shocks

The theoretical landscape explaining volume-return relationships has evolved substantially beyond the foundational work of merton1987simple and https://doi.org/10.1111/0022-1082.00349. Three complementary theoretical streams now provide rigorous foundations for understanding HVRP.

Investor Recognition and Limited Attention. merton1987simple’s ‘Investor Recognition Hypothesis’ posits that investors include only stocks they are aware of in their consideration set. When a stock’s recognition increases, its investor base expands, lowering required returns and increasing prices through risk diversification effects. https://doi.org/10.1111/0022-1082.00349 applied this theory to trading volume, establishing the HVRP phenomenon: under investors’ ‘limited attention,’ abnormal volume spikes serve as ‘attention shocks,’ attracting new buying interest and causing sustained price increases. https://doi.org/10.1111/j.1540-6261.2011.01679.x operationalized attention directly using Google Search Volume Index (SVI), finding that increased attention leads to higher near-term prices with eventual reversal—a pattern central to understanding HVRP dynamics.

Rational Inattention Models. https://doi.org/10.3982/ECTA11412 develop an equilibrium model where fund managers optimally allocate scarce attention, generating different risk premia for high-attention stocks. PENG2006563 show that investors with limited processing capacity engage in ‘category learning,’ processing more market-level than firm-specific information—explaining why high-volume stocks receiving attention might command different returns. These models provide rigorous information-theoretic foundations for attention-based return patterns.

Heterogeneous Beliefs and Speculation. doi:10.1086/378531 demonstrate that overconfident investors combined with short-sale constraints generate speculative bubbles—high trading volume reflects disagreement that produces a ‘resale option’ premium. This mechanism is particularly relevant for retail-dominated markets like Korea, where short-sale constraints are significant. DEFUSCO2022205 develop a dynamic theory showing how predictable price increases attract short-term investors who amplify volume through feedback trading.

Information Asymmetry and Liquidity. 10.2307/2118454 show that when liquidity traders sell, risk-averse market makers demand higher expected returns—volume thus captures risk premium information. https://doi.org/10.1111/j.1540-6261.1994.tb04424.x demonstrate that volume provides information about signal precision unavailable from prices alone, offering a fundamental reason why volume should predict returns.

Cross-Country Evidence. KANIEL2012255 analyze HVRP across 41 countries and find that the premium is pervasive globally but varies with market characteristics. The magnitude associates with individual investor participation, short-selling constraints, and information asymmetry—all factors where Korea differs substantially from developed markets. merton1987simple posits that abnormal trading volume positively relates to future investment and financing activities, with effects more pronounced in financially constrained firms with low investor recognition—providing a real-effects channel through which HVRP operates.

The Korean Market Puzzle. In the Korean market, ART001162590 empirically confirmed HVRP using 2001-2003 data, finding stronger premiums in large-cap stocks which they interpreted as related to lower information asymmetry in stocks with higher institutional ownership. However, subsequent research by CHAE2019101204 documents a striking reversal: using Korean data, they find that low-volume stocks outperform high-volume stocks—a Low Volume Return Premium (LVRP) rather than HVRP. Of 70 sample configurations, 16 show significant LVRP versus only 1 showing significant HVRP. They attribute this to mean-reversion of trading volume and positive contemporaneous correlation between returns and volume changes (CCRV). This pattern directly contradicts U.S. evidence and creates a puzzle our study addresses: whether the COVID-19 pandemic and associated retail trading surge altered this relationship, potentially shifting Korea toward developed-market HVRP patterns.

### B Core Debate: Are Retail Investors ’Noise’ or ’Information’?

To understand HVRP drivers, we must identify the actors causing abnormal volume, particularly the nature of ’retail investors.’ Academia is divided into two opposing views engaged in intense debate.

First, the ’Noise Trader’ hypothesis. 10.1093/rfs/hhm079 revealed that retail investors tend to net-buy stocks that are ’attention-grabbing’—such as those with media coverage or volume spikes—rather than conducting fundamental analysis. https://doi.org/10.1111/jofi.13183 use Robinhood data to show that app-induced attention causes herding—stocks with the largest daily user increases subsequently lose approximately 4.7% over the following month. Recently, https://doi.org/10.1111/jofi.13183 reported that new retail investors’ remarkable daily turnover rate (18.12%) stems from overconfidence rather than information value, with their net purchases negatively predicting future returns. 10.1093/rfs/hhj032 provide complementary evidence that share turnover positively relates to lagged returns for many months, consistent with overconfidence driving excessive trading. Under this view, retail-led HVRP represents merely temporary price pressure, unable to generate long-term excess returns.

Second, the ’Liquidity Provider & Informed Trader’ hypothesis. In contrast, https://doi.org/10.1111/j.1540-6261.2008.01316.x and KANIEL2012255 argued that retail investors earn liquidity premiums by making contrarian investments in response to institutional liquidity demands. https://doi.org/10.1111/jofi.12028 confirm that retail order imbalances positively predict returns over days to weeks. Furthermore, https://doi.org/10.1111/jofi.13033 showed through recent order flow analysis that retail net purchases predict approximately 10bp short-term excess returns (annualized 5%), suggesting retail investors may possess information value. This paradox—that retail trades predict returns yet retail investors underperform—is resolved by barber2024resolving, who show that retail investors provide liquidity by trading contrarian, predicting returns but losing on implementation costs.

Empirical Evidence on Investor Heterogeneity. STOFFMAN201450 compared institutional and retail trading behavior, finding that institutions engage in information-based trading while retail investors tend toward noise trading, implying that the two groups’ trades have different effects on market returns. Using actual trading records, STOFFMAN201450 analyzed 15 years of Finnish data and discovered that when institutions buy from retail investors prices rise, and when institutions sell to retail investors prices fall, while retail-to-retail trades show no consistent pattern and prices quickly revert. This empirically supports theories that institutions and retail investors differ in information processing ability and trading purposes.

Korean Market Investor Composition. Korea’s market exhibits substantial retail investor participation, creating a unique laboratory for testing investor heterogeneity effects. https://doi.org/10.1111/j.2041-6156.2011.01037.x show that foreigners in Korea behave like short-term momentum traders while individual investors act as contrarians. CHOE1999227 document strong positive feedback trading and herding by foreign investors during the Asian crisis, establishing precedents for understanding how different investor types respond to market stress.

By separately analyzing institution/foreign-led versus retail-led events, our study aims to provide decisive evidence for determining whether retail investors in the Korean market are mere ’noise generators’ or meaningful ’market participants.’

### C Modern Market Structural Changes: Crisis and Collective Action

Since ART001162590 analyzed 2001-2003, modern stock markets have experienced two major structural changes: the COVID-19 pandemic and social media proliferation.

COVID-19 and Retail Trading Surge. Ozik\_Sadka\_Shen\_2021 empirically demonstrated that the surge in retail investor trading through fintech apps during COVID-19 lockdowns acted as a buffer preventing market liquidity depletion, dampening effective spread increases by approximately 40%. ORTMANN2020101717 show that retail investors increased trading intensity by 13.9% as COVID cases doubled. In Korea specifically, the retail trading surge was extraordinary: kim2022behavioral document that Korean individual investor annual trading turnover reached above 1,600% during March-October 2020. This suggests that retail investors’ roles during crises may differ substantially from normal periods.

Critically, KWAK2024105027 documents significant attenuation in the positive association between individual investor purchases and stock returns following COVID-19 in Korea—suggesting the volume-return relationship structurally changed. KWAK2024105027 show that during the pandemic, Korean individual investors continued buying while pension funds, foreign, and institutional investors sold. This creates an ideal setting to test whether the traditional noise trader characterization of retail investors holds during crisis periods when they serve as liquidity providers.

Social Media and Collective Action. 10.1093/rfs/hhad098 analyzed online communities like ’WallStreetBets,’ discovering that individuals’ Due Diligence reports possessed significant information value before the GME event but deteriorated into mere price pressure or attention-grabbing noise after popularization. This implies that HVRP during Korea’s ’Donghak Ant Movement’ period may exhibit patterns different from normal periods. The collective action element—where retail investors coordinated through social media to absorb institutional selling pressure—mirrors doi:10.1086/378531’s speculation model but with an important twist: collective information sharing may temporarily transform noise traders into informed participants.

### D Methodological Issue: Identity versus Intensity

Prior studies have used both ’investor type (Identity)’ as a categorical variable and ’trading intensity (Intensity)’ as a continuous variable when analyzing investor behavior. However, recent studies suggest that the relationship between these two variables may be nonlinear.

Namouri26012018 demonstrated that ’threshold effects’ exist in the relationship between investor sentiment and returns, with relationships reversing or disappearing beyond certain levels. https://doi.org/10.1111/jofi.13183 also suggested that new investors’ high trading intensity is merely a ’symptom’ of their ’inexperience’ identity, not the essence of predictive power. HAN20221295 document that expected returns relate positively to volume among underpriced stocks but negatively among overpriced stocks—volume amplifies mispricing asymmetrically. 10.1093/rfs/hhab055 find that low-turnover stocks exhibit short-term reversal while high-turnover stocks display short-term momentum, demonstrating that volume conditions the return dynamics.

These findings suggest that when analyzing HVRP, examining only the linear correlation between net purchase intensity (Dominance Score) and returns is insufficient. An identity-centered approach to ’who led,’ combined with proper nonlinear analysis of intensity effects, is necessary.

### E Research Hypotheses

Based on the above discussion, we establish the following hypotheses.

Hypothesis 1 (Investor Type Heterogeneity): The sources of high volume return premium differ by investor type.

* •

  1a: Abnormal volume events led by institutions and foreign investors with information advantages will show persistent positive long-term excess returns (CAR).
* •

  1b: Events led by retail investors with limited attention and behavioral biases will show transient price increases followed by dissipation, failing to generate significant long-term excess returns (supporting the noise trader hypothesis).

Hypothesis 2 (Moderating Effects of Modern Market Shocks): Extreme market environments alter HVRP patterns.

* •

  2a: During periods of increased uncertainty from COVID-19 shocks, information asymmetry intensifies, amplifying the signaling effect of information-based trading (institutions/foreigners).
* •

  2b: During the ’Donghak Ant Movement’ period, retail investors’ collective action (coordination) through social media strengthens, causing retail-led events to show exceptionally strong persistence.

Hypothesis 3 (Nonlinearity and the Critical Role of Normalization): The predictive power of trading intensity is nonlinear and is only revealed when intensity is measured as a function of firm size.

* •

  3a (Linear Model Fails): A simple linear correlation between a composite ’smart money’ intensity score (Dominance Score) and future returns will be weak or insignificant, because the relationship operates through discrete regimes rather than continuous linear effects.
* •

  3b (Monotonic Pattern Emerges): After sorting events by investor type, a conditional analysis will reveal a strong, positive, and monotonic relationship between buying intensity and future returns for informed investors (institutions/foreigners).
* •

  3c (Normalization is Critical): This monotonic relationship will only emerge when intensity is normalized by market capitalization, which captures investor conviction (size of position relative to firm value), not merely participation in daily trading flow.
* •

  3d (The Horse Race): When intensity is normalized by daily trading value instead of market capitalization, the monotonic pattern will be significantly weaker or absent, demonstrating that measuring conviction relative to firm size is the superior specification for detecting informed trading signals.

## III Research Design

### A Data and Sample Selection

This study applies ART001162590’s 2001-2003 research to the current market (January 1, 2020, to December 31, 2024) to verify the persistence of the High Volume Return Premium phenomenon. Following the original study, we examine all stocks listed on the Korea Exchange and additionally perform detailed analysis of individual KOSPI and KOSDAQ markets.

Data Collection: Daily stock price and trading volume data were collected via Daishin Securities’ Creon Plus DataReader API. Investor type-specific net purchase data (institutional, foreign, and retail investor transactions) were collected using the pykrx library, which provides official Korea Exchange data. The data collection targets individual listed stocks only and includes daily prices, trading volume, and outstanding shares.

Sample Exclusion Criteria: To ensure consistency with the original study and data quality, we applied the following exclusion criteria to refine the sample:

* •

  Delisted stocks and stocks under administrative issues
* •

  Stocks priced below 1,000 won (to exclude low-liquidity penny stocks)
* •

  Stocks with zero trading volume for two or more consecutive days (liquidity-deficient stocks)
* •

  Stocks with changes in outstanding shares during the 20 trading days prior to the event date (to exclude effects of stock splits, mergers, or other capital structure changes)

### B Research Methodology

We faithfully follow ART001162590’s methodology while applying additional dual validation methodology to test the investor type hypothesis.

#### 1 Event Date Definition

An event date of abnormal trading volume is defined as a day when an individual stock’s daily volume exceeds 5 times its past 20-day moving average volume (A​D​T​V>5ADTV>5).

|  |  |  |
| --- | --- | --- |
|  | A​D​T​Vi,t=V​o​li,t120​∑j=120V​o​li,t−jADTV\_{i,t}=\frac{Vol\_{i,t}}{\frac{1}{20}\sum\_{j=1}^{20}Vol\_{i,t-j}} |  |

Events occurring within 50 trading days after an initial event are considered dependent events and excluded from analysis.

#### 2 Dual Validation Methodology

To robustly test the investor type hypothesis, we employ two independent methodologies in parallel.

Method 1: Double-Sort Methodology by Investor Type and Intensity

This is our primary methodology, representing our main contribution. We employ a two-stage classification process that separates investor identity from trading intensity.

Stage 1: Investor Type Classification

Each abnormal volume event is classified according to the net purchase ratios of three investor types (institutions, foreigners, retail) using an argmax rule. The investor group with the highest net buy ratio (measured initially as a percentage of total trading value for classification purposes) is identified as the leading investor:

* •

  Institution-Led: If institutional net buy ratio exceeds both foreign and retail ratios
* •

  Foreign-Led: If foreign net buy ratio exceeds both institutional and retail ratios
* •

  Retail-Led: If retail net buy ratio exceeds both institutional and foreign ratios

Stage 2: Intensity Quantification with Alternative Normalizations

After identifying the leading investor type, we quantify purchase conviction intensity using a quartile-based classification system. Critically, we test two alternative normalization specifications:

Specification A (Trading Value Normalization):

|  |  |  |
| --- | --- | --- |
|  | Intensityk,i,tT​V=Net Buy Valuek,i,tTotal Trading Valuei,t\text{Intensity}\_{k,i,t}^{TV}=\frac{\text{Net Buy Value}\_{k,i,t}}{\text{Total Trading Value}\_{i,t}} |  |

Specification B (Market Capitalization Normalization):

|  |  |  |
| --- | --- | --- |
|  | Intensityk,i,tM​C=Net Buy Valuek,i,tMarket Capitalizationi,t\text{Intensity}\_{k,i,t}^{MC}=\frac{\text{Net Buy Value}\_{k,i,t}}{\text{Market Capitalization}\_{i,t}} |  |

where kk denotes the leading investor type. Specification A measures an investor’s participation in daily trading flow, while Specification B measures their conviction as position size relative to firm value. We calculate quartiles (Q1-Q4) based on the distribution of intensity (including sign) across all events of that investor type. Q1 represents the lowest intensity (often net selling), while Q4 represents the highest conviction buying.

Methodological Rationale: This double-sort approach allows us to test whether the relationship between trading intensity and future returns depends on how intensity is measured. If market cap normalization produces a monotonic pattern while trading value normalization does not, this reveals that the choice of normalization is fundamental to detecting informed trading signals, not merely a technical detail.

Method 2: Baseline Linear Correlation Analysis

To establish a baseline for comparison, we test the simplest possible linear relationship using a composite ”smart money” intensity score. This method measures the combined net purchase intensity of information-advantaged investors (institutions + foreigners) as a continuous variable:

|  |  |  |
| --- | --- | --- |
|  | Dominance Scorei,t=Institution Net Buyi,t+Foreign Net Buyi,tTotal Trading Valuei,t\text{Dominance Score}\_{i,t}=\frac{\text{Institution Net Buy}\_{i,t}+\text{Foreign Net Buy}\_{i,t}}{\text{Total Trading Value}\_{i,t}} |  |

For each event, we calculate forward returns at 5-day, 20-day, and 60-day horizons and analyze Pearson correlation coefficients between dominance scores and forward returns by firm size (large-cap, mid-cap, small-cap).

Forward Returns Calculation: Forward returns are defined as the return from the event day closing price to the closing price after the target period. To account for non-trading days (weekends, holidays), we use the closing price of the trading day closest to the target period within a range of 80% to 150%. For example, for 20-day forward returns, we select the trading day closest to day 20 within the 16-30 day range. This approach prevents data loss due to non-trading days while maintaining proximity to the target period.

Methodological Complementarity: Method 2 provides a critical benchmark. If this simple linear correlation shows near-zero coefficients, while Method 1’s quartile-based analysis reveals strong monotonic patterns, this demonstrates that the relationship is nonlinear and type-dependent. The failure of linear models does not indicate that intensity is irrelevant; it reveals that proper detection requires: (1) accounting for investor heterogeneity through type-based sorting, (2) using nonlinear quartile analysis rather than linear correlation, and (3) normalizing by the correct benchmark (market cap rather than trading value). Method 2’s weak results thus validate the necessity of Method 1’s more sophisticated approach.

#### 3 Abnormal Return Calculation

Using event study methodology, we calculate cumulative abnormal returns (CAR) around event dates (-50 to +50 days). Abnormal returns (AR) use the market-adjusted return model (A​Ri,t=Ri,t−RM,tAR\_{i,t}=R\_{i,t}-R\_{M,t}).

## IV Empirical Results

### A Descriptive Statistics: ADTV Distribution

Before presenting event study results, we examine the distribution characteristics of abnormal daily trading volume (ADTV) in our sample period and compare them with the original study.

Table 1: ADTV Basic Statistics Comparison

| Statistic | Original Study (2001-2003) | This Study (2020-2024) |
| --- | --- | --- |
| Mean | 1.029 | 1.379 |
| Median | 0.773 | 0.686 |
| Std. Dev. | 0.935 | 8.292 |
| Skewness | 3.819 | 139.268 |
| Kurtosis | 27.042 | 43,503.08 |
| Min | 0.000 | 0.000 |
| Max | 14.439 | 3,789.10 |
| Observations | 65,490 | 2,753,106 |

The ADTV distribution exhibits dramatically higher skewness (139.27 vs. 3.82) and kurtosis (43,503 vs. 27) compared to the original study, indicating that modern markets experience more extreme trading volume events. The maximum ADTV increased from 14.44 to 3,789.10, reflecting the increased frequency of extraordinary market events during our sample period.

Table 2: ADTV Cumulative Distribution (2020-2024)

| ADTV Range | Frequency | Proportion (%) | Cumulative Freq. | Cumulative (%) |
| --- | --- | --- | --- | --- |
| [0, 5) | 2,677,890 | 97.32 | 2,677,890 | 97.32 |
| [5, 10) | 39,262 | 1.43 | 2,717,152 | 98.75 |
| [10, 15) | 11,964 | 0.43 | 2,729,116 | 99.19 |
| 15+ | 22,395 | 0.81 | 2,751,511 | 100.00 |

Only 2.68% of observations exceed the ADTV threshold of 5, yielding our event sample of approximately 73,500 total abnormal volume events (after excluding dependent events within 50 days, the final sample contains 26,604 independent events as shown in subsequent analyses).

### B Methodological Transparency: Analysis Specifications

To ensure reproducibility and clarity, Table [3](https://arxiv.org/html/2512.14134v1#S4.T3 "Table 3 ‣ B Methodological Transparency: Analysis Specifications ‣ IV Empirical Results ‣ Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)") documents the specific methodological approach used for each empirical analysis in this paper. Our study employs two primary normalization methods: (1) Market Cap Rank-based classification for broad market comparisons, and (2) Market Cap Normalization for intensity-based quartile analyses. This methodological variation reflects the specific research question addressed in each section.

Table 3: Methodological Specifications by Analysis Section

|  |  |  |
| --- | --- | --- |
| Section | Analysis Type | Normalization Method |
| 4.1 ADTV Distribution | Descriptive Statistics | N/A (Raw ADTV) |
| 4.2 HVRP Evolution | Event Study Comparison | Market Cap Rank |
| 4.2.1 Firm Size | Event Study by Size | Market Cap Rank (Terciles) |
| 4.3 Investor Type | Intensity Quartile Analysis | Market Cap Normalization |
| 4.4 Horse Race | Methodological Comparison | Both Methods Compared |
| 4.5 Correlation | Dominance-Return Relationship | Market Cap Normalization |
| 4.6.1 Market Conditions | Event Study by Period | Market Cap Rank |
| 4.6.3 COVID-19 Shock | Crisis Period Analysis | Standard Event Study |
| 4.6.4 Donghak Ant | Retail Transformation | Standard Event Study |
| Market Cap Rank: Firms classified by market cap percentile (large/mid/small). | | |
| Market Cap Normalization: Intensity = Net Buy Value / Market Capitalization. | | |
| All analyses use event windows of [-50, +50] trading days with ADTV threshold = 5. | | |

This methodological framework ensures that each research question is addressed with the most appropriate measurement approach, while maintaining consistency within each analytical dimension.

### C Evolution of HVRP: 20 Years of Change

We examine whether the HVRP phenomenon observed by ART001162590 in the early 2000s remains valid in the rapidly changing 2020s market environment and how it has evolved.

Table 4: Full Sample Event Study Results: 2003 Original Study vs 2024 Re-examination

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Original Study (2001-2003) | | | This Study (2020-2024) | | |
| Event Day | AAR(%) | t-stat | CAR(%) | AAR(%) | t-stat | CAR(%) |
| -25 | -0.361\*\*\* | -3.24 | -1.820 | -0.13%\*\*\* | -7.52 | -2.09% |
| -10 | -0.097 | -1.45 | -4.454 | -0.10%\*\*\* | -6.93 | -4.46% |
| -5 | -0.082 | -1.35 | -3.748 | -0.07%\*\*\* | -5.12 | -4.93% |
| -2 | 0.418\*\*\* | 6.92 | -3.441 | 0.14%\*\*\* | 8.28 | -4.75% |
| -1 | 2.454\*\*\* | 40.62 | -0.987 | 0.66%\*\*\* | 28.87 | -4.09% |
| 0 | 5.056\*\*\* | 83.66 | 4.068 | 6.15%\*\*\* | 118.81 | 2.06% |
| 1 | -0.200 | -3.31 | 3.869 | 0.09%\*\*\* | 2.72 | 2.15% |
| 2 | -0.126 | -2.08 | 3.743 | -0.00% | -0.18 | 2.15% |
| 5 | -0.043 | -0.71 | 3.598 | -0.05%\*\* | -2.34 | 2.19% |
| 10 | -0.006 | -0.10 | 3.779 | 0.01% | 0.28 | 2.33% |
| 25 | 0.195\*\* | 3.22 | 4.268 | 0.03% | 1.28 | 2.71% |
| 50 | -0.107 | -1.77 | 3.672 | 0.02% | 1.01 | 3.09% |
| \*p¡0.10, \*\*p¡0.05, \*\*\*p¡0.01 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Key findings:

1. 1.

   Increased Effect Size: Event day AAR increased from 5.06% to 6.15%, approximately 22% higher
2. 2.

   Enhanced Statistical Significance: Increased sample size (1,360 → 26,604 events) improved reliability
3. 3.

   Phenomenon Robustness: HVRP persists despite 20-year gap

### D Market Structural Characteristics: Firm Size and Market Type

While ART001162590 found the strongest effects in large-cap stocks, we confirm that the premium center has shifted to mid-cap stocks.

Table 5: Event Study Results by Firm Size: Mid-Cap Dominance Phenomenon

|  | Large-cap (1-100) | | | Mid-cap (101-300) | | | Small-cap (300+) | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Day | AAR | t-stat | CAR | AAR | t-stat | CAR | AAR | t-stat | CAR |
| 0 | 4.41% | 10.79\*\*\* | 2.47% | 6.06% | 25.19\*\*\* | 4.21% | 6.19% | 115.92\*\*\* | 1.93% |
| 50 | -0.01% | -0.04 | 1.43% | 0.16% | 1.98\*\* | 4.00% | 0.01% | 0.61 | 3.07% |

Mid-cap 50-day CAR reaches 4.00%, dominating large-cap (1.43%) and small-cap (3.07%). This suggests mid-cap stocks have emerged as the new ’opportunity window’ in modern markets, positioned between information-transparent large-caps and liquidity-constrained small-caps.

### E Sources of Investor Type Premium: Core Findings

The most important contribution of our study—investor type analysis—provides clear answers to a longstanding finance debate. Using our data-driven classification methodology, we categorized all 26,604 abnormal volume events by leading investor type.

Table 6: Investor Type Analysis: Intensity-Return Relationship (Market Cap Normalization)\*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Investor Type & Intensity | N Events | Day 0 AAR (%) | Day +20 CAR (%) | Day +50 CAR (%) |
| Institution-Led (Total: 2,831 events) | | | | |
| Q1 (Lowest Intensity) | 708 | 1.55% | -1.37 | -0.05% |
| Q2 | 914 | 2.54% | 1.70 | 3.76% |
| Q3 | 501 | 5.04% | 2.60 | 4.09% |
| Q4 (Highest Intensity) | 708 | 8.62% | 9.85 | 10.07% |
| Foreign-Led (Total: 9,416 events) | | | | |
| Q1 (Lowest Intensity) | 2,354 | 6.63% | 1.60 | 2.25% |
| Q2 | 2,354 | 6.05% | 0.27 | 0.39% |
| Q3 | 2,354 | 4.04% | -1.18 | -0.49% |
| Q4 (Highest Intensity) | 2,354 | 7.18% | 7.19 | 8.16% |
| Retail-Led (Total: 15,512 events) | | | | |
| Q1 (Lowest Intensity) | 3,878 | 8.72% | 9.55 | 10.27% |
| Q2 | 3,878 | 4.81% | 0.81 | 1.39% |
| Q3 | 3,878 | 6.43% | 0.38 | 0.42% |
| Q4 (Highest Intensity) | 3,878 | 6.48% | 0.74 | 0.48% |
| \*Market cap normalization applied. Intensity quartiles computed within each investor type. | | | | |
| --- | --- | --- | --- | --- |
| Total events differ from 26,604 due to data filtering requirements for intensity calculation. | | | | |

Key Findings: When we decompose each investor type by trading intensity (market cap normalized), three fundamentally distinct patterns emerge that reveal the nature of each investor group’s information advantage:

Institutional Investors Exhibit Monotonic Positive Relationship (Information Advantage): As institutional buying intensity increases from Q1 to Q4, day +50 CAR rises monotonically from -0.05% to 10.07%. This demonstrates that high-conviction institutional buying (Q4) predicts substantially higher long-term returns, validating the information advantage hypothesis. The strongest institutional conviction generates more than 200 times better returns than their lowest-conviction trades.

Foreign Investors Show U-Shaped Pattern (Mixed Signals): Foreign investors display a non-monotonic, U-shaped relationship. Both low-intensity (Q1: 2.25%) and high-intensity (Q4: 8.16%) events generate positive returns, while mid-intensity quartiles (Q2-Q3) yield near-zero or negative returns. This suggests foreign investors possess information in extreme cases but may trade for liquidity or rebalancing purposes in moderate-intensity situations.

Retail Investors Display Inverted Monotonic Relationship (Noise Trading): Most strikingly, retail investors exhibit an inverted pattern—as buying intensity increases from Q1 to Q4, day +50 CAR decreases from 10.27% to 0.48%. This means retail investors’ highest-conviction trades (Q4) generate 21 times worse long-term returns than their lowest-intensity trades (Q1). This inverted relationship provides powerful evidence that retail investors are predominantly noise traders whose strongest convictions systematically lead to inferior outcomes.

Core Discovery: The intensity-return relationship is not merely different across investor types—it is fundamentally opposite. Institutional Q4 (10.07%) outperforms retail Q4 (0.48%) by a factor of 21. More dramatically, retail investors perform best when they trade with lowest conviction (Q1: 10.27%), suggesting they accidentally benefit from contrarian positioning or mean reversion when less confident. Methodological Foundations. Our empirical approach follows established best practices from top finance journals. For standard errors in panel data, we follow 10.1093/rfs/hhn053, who provides the definitive comparison of clustered standard errors versus Fama-MacBeth approaches. For event study methodology with long-horizon returns, we follow https://doi.org/10.1111/0022-1082.00101, who document biases in buy-and-hold abnormal returns (BHAR) methodology and propose solutions. For investor classification using Korean Exchange data, we follow precedents established by CHOE1999227 and CAMPBELL200966.

This strongly supports Hypothesis 1 and provides nuanced evidence beyond simple investor type comparisons.

This finding directly contradicts https://doi.org/10.1111/j.1540-6261.2008.01316.x and https://doi.org/10.1111/jofi.13033’s claims of retail investor sophistication, while providing granular, intensity-decomposed support for 10.1093/rfs/hhm079 and https://doi.org/10.1111/jofi.13183’s ’noise trader’ hypothesis using 2020s Korean market data.

### F Main Finding: Intensity Matters, But Measurement is Critical

While Section 4.3 established that investor identity matters, we now demonstrate that trading intensity also matters profoundly—but its effect is nonlinear and only revealed when measured correctly. This section presents our central methodological contribution: demonstrating that the choice of normalization is not a technical detail but a fundamental determinant of whether we detect informed trading signals.

#### 1 The Horse Race: Market Cap vs. Trading Value Normalization

We test two alternative specifications for measuring institutional buying intensity:

* •

  Specification A (Trading Value): Intensity=Institution Net Buy ValueTotal Daily Trading Value\text{Intensity}=\frac{\text{Institution Net Buy Value}}{\text{Total Daily Trading Value}}
* •

  Specification B (Market Cap): Intensity=Institution Net Buy ValueMarket Capitalization\text{Intensity}=\frac{\text{Institution Net Buy Value}}{\text{Market Capitalization}}

Specification A measures an institution’s participation in daily trading flow—what percentage of today’s trading activity did they dominate? Specification B measures an institution’s conviction—how large a position did they take relative to the firm’s total value?

For both specifications, we classify institution-led events into quartiles (Q1-Q4) based on the intensity distribution and calculate 50-day cumulative abnormal returns. Table [7](https://arxiv.org/html/2512.14134v1#S4.T7 "Table 7 ‣ 1 The Horse Race: Market Cap vs. Trading Value Normalization ‣ F Main Finding: Intensity Matters, But Measurement is Critical ‣ IV Empirical Results ‣ Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)") presents the results.

Table 7: Horse Race Comparison: Trading Value vs. Market Cap Normalization

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Specification A (Trading Value) | | Specification B (Market Cap) | |
| Quartile | Day 0 AAR (%) | Day +50 CAR (%) | Day 0 AAR (%) | Day +50 CAR (%) |
| Q1 (Lowest) | -0.60% | -3.81% | 1.55% | -0.05% |
| Q2 | 4.20% | 6.69% | 2.54% | 3.76% |
| Q3 | 9.21% | 12.33% | 5.04% | 4.09% |
| Q4 (Highest) | 5.67% | 4.22% | 8.62% | 10.07% |
| Pattern | Non-monotonic (Q3 ¿ Q4) | | Perfect Monotonic (Q1¡Q2¡Q3¡Q4) | |

The Results Are Striking:

Specification A (Trading Value) Fails: While Q2, Q3, and Q4 all show positive returns, the pattern is non-monotonic. The strongest returns appear in Q3 (12.33%), not Q4 (4.22%). This broken monotonicity suggests that trading value normalization conflates informed conviction with noise trading participation.

Specification B (Market Cap) Succeeds: A perfect monotonic relationship emerges. Day +50 CAR progresses cleanly from -0.05% (Q1) →\rightarrow +3.76% (Q2) →\rightarrow +4.09% (Q3) →\rightarrow +10.07% (Q4). This demonstrates that when institutions take larger positions relative to firm size, they are acting on stronger information.

Economic Interpretation: Market capitalization normalization captures conviction. An institution buying $1M worth of stock sends a very different signal if the firm is worth $10M (10% conviction) versus $1B (0.0001% participation). Trading value normalization conflates high-conviction small bets with low-conviction large trades, obscuring the true information signal.

#### 2 Monotonic Pattern Analysis: Institutions vs. Retail

Figure [1](https://arxiv.org/html/2512.14134v1#S4.F1 "Figure 1 ‣ 2 Monotonic Pattern Analysis: Institutions vs. Retail ‣ F Main Finding: Intensity Matters, But Measurement is Critical ‣ IV Empirical Results ‣ Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)") visualizes the monotonic relationship for institution-led events under market cap normalization.

![Refer to caption](monotonic_pattern_analysis.png)


Figure 1: Monotonic Pattern: Institutional Buying Intensity (Market Cap Normalization)

The plot confirms three critical findings:

(1) Q1 (Net Selling): Events where institutions are net sellers show flat long-term returns near zero (-0.05%). This suggests that institutional selling does not predict negative returns, but rather reflects portfolio rebalancing or liquidity provision.

(2) Q2-Q3 (Moderate Conviction): Moderate institutional buying generates positive but modest returns (+3.76% and +4.09%), indicating weak positive information signals.

(3) Q4 (High Conviction): The highest quartile generates exceptional returns (+10.07%), more than double Q3’s returns. This nonlinear jump suggests a threshold effect—only the most convicted institutional positions predict substantial future performance.

Retail Investors: Inverted Pattern

The market cap normalization also reveals a striking inverted monotonic pattern for retail investors. While institutions’ highest conviction buying (Q4) predicts +10.07% returns, retail investors’ highest conviction buying predicts negative or near-zero returns. Their Q1 (net selling) quartile actually predicts the highest positive returns. This confirms the noise trader hypothesis with unprecedented clarity: retail investors systematically buy at peaks and sell at troughs.

Why Does This Matter?

This finding resolves a longstanding puzzle in behavioral finance. Prior studies found mixed evidence on whether trading intensity matters (Namouri26012018; https://doi.org/10.1111/jofi.13183), leading some to conclude that intensity is irrelevant. Our results demonstrate that intensity matters enormously, but researchers must measure it correctly. The failure of linear correlation models (Dominance Score analysis in Section 4.5) does not mean intensity is irrelevant—it means the relationship is nonlinear and type-dependent, requiring proper quartile-based analysis with conviction-based normalization.

Implications for Hypothesis 3: These results strongly support all four sub-hypotheses:

* •

  H3a: Linear Dominance Score correlation ≈\approx 0 (confirmed in Section 4.5)
* •

  H3b: Monotonic relationship emerges after investor type sorting (confirmed: Q1¡Q2¡Q3¡Q4)
* •

  H3c: Market cap normalization reveals the pattern (confirmed: perfect monotonicity)
* •

  H3d: Trading value normalization fails (confirmed: broken monotonicity, Q3¿Q4)

### G Methodological Validation: Nonlinearity of Identity versus Intensity

The second approach of our dual validation methodology presents highly interesting evidence of ’nonlinearity.’ We analyze correlations between Dominance Score and forward returns across multiple time horizons.

Table 8: Correlation Between Dominance Score and 5-Day Forward Returns

| Firm Size | Observations | Correlation | P-value | Mean Return |
| --- | --- | --- | --- | --- |
| Large-cap | 472 | -0.0333 | 0.470 | 0.27% |
| Mid-cap | 1,531 | 0.0209 | 0.415 | -0.11% |
| Small-cap | 25,514 | -0.0061 | 0.331 | 0.22% |




Table 9: Correlation Between Dominance Score and 20-Day Forward Returns

| Firm Size | Observations | Correlation | P-value | Mean Return |
| --- | --- | --- | --- | --- |
| Large-cap | 473 | -0.0334 | 0.468 | 0.88% |
| Mid-cap | 1,546 | -0.0142 | 0.576 | 0.12% |
| Small-cap | 25,753 | -0.0044 | 0.479 | 0.61% |




Table 10: Correlation Between Dominance Score and 60-Day Forward Returns

| Firm Size | Observations | Correlation | P-value | Mean Return |
| --- | --- | --- | --- | --- |
| Large-cap | 473 | -0.0261 | 0.571 | 0.18% |
| Mid-cap | 1,545 | -0.0357 | 0.161 | 0.02% |
| Small-cap | 25,743 | -0.0061 | 0.330 | 1.24% |

Across all three time horizons (5-day, 20-day, 60-day) and all firm size categories, correlations consistently converge to near-zero (—r— ¡ 0.04) and are completely statistically insignificant (all p ¿ 0.16). This robust pattern across multiple horizons confirms this is not a time-specific artifact but a fundamental characteristic of the phenomenon. Critically, this does not mean intensity is irrelevant—as Section 4.4 demonstrated, intensity matters profoundly when measured correctly. Instead, these near-zero correlations reveal three methodological limitations of the Dominance Score approach:

1. 1.

   Linear Model Inadequacy: The relationship between intensity and returns is nonlinear, operating through discrete quartile regimes rather than continuous linear effects. Pearson correlation cannot capture monotonic but nonlinear relationships.
2. 2.

   Investor Heterogeneity Ignored: Pooling institutions and foreigners into a single ”smart money” score masks type-specific patterns. As Section 4.4 showed, institutions and foreigners exhibit different intensity-return relationships.
3. 3.

   Wrong Normalization: The Dominance Score uses trading value normalization, which Section 4.4’s horse race demonstrated produces broken monotonicity. Market cap normalization is required to reveal the true pattern.

This validates our methodological choice in Section 4.4 to use type-specific, quartile-based analysis with market cap normalization. The failure of linear correlation does not indicate intensity is irrelevant—it validates the necessity of more sophisticated methods to detect nonlinear, type-dependent relationships.

### H Modern Market Phenomena: COVID-19 and Donghak Ant Movement

Modern market phenomena such as COVID-19 and the Donghak Ant Movement dramatically transformed traditional patterns. We analyze these two critical periods to test Hypothesis 2.

#### 1 Market Condition Effects: Bull vs. Bear Markets

The original study by ART001162590 found that HVRP appears stronger during bull markets. We replicate this analysis using modern data to verify whether this pattern persists. Market conditions are defined using a 20% threshold: bull markets are identified when the KOSPI index rises 20% or more from a prior trough, and bear markets when it falls 20% or more from a prior peak.

Table 11: Market Period Definitions

| Market Phase | Start Date | End Date |
| --- | --- | --- |
| Bull Market | | |
| Bull Market 1 | March 31, 2020 | January 26, 2022 |
| Bull Market 2 | June 2, 2023 | December 31, 2024 |
| Bear Market | | |
| Bear Market 1 | October 25, 2018 | March 30, 2020 |
| Bear Market 2 | January 27, 2022 | June 1, 2023 |




Table 12: Bull vs. Bear Market Event Study Results

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Bull Market | | | Bear Market | | |
| Event Day | AAR (%) | t-stat | CAR (%) | AAR (%) | t-stat | CAR (%) |
| -10 | -0.10% | -5.65\*\*\* | -4.69% | -0.10% | -4.02\*\*\* | -3.95% |
| -1 | 0.73% | 26.04\*\*\* | -4.19% | 0.51% | 12.93\*\*\* | -3.85% |
| 0 | 6.47% | 101.87\*\*\* | 2.28% | 5.47% | 61.58\*\*\* | 1.62% |
| 1 | 0.11% | 2.70\*\*\* | 2.39% | 0.05% | 0.82 | 1.66% |
| 10 | 0.04% | 1.33 | 2.60% | -0.06% | -1.59 | 1.77% |
| 25 | 0.05% | 2.00\*\* | 3.02% | -0.03% | -0.73 | 2.05% |
| 50 | 0.04% | 1.51 | 3.84% | -0.02% | -0.51 | 1.50% |
| \*p¡0.10, \*\*p¡0.05, \*\*\*p¡0.01 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Original study (2001-2003): Bull 5.668% vs. Bear 4.443% (t-value 3.13\*\*\*) | | | | | | |

The original study’s key finding that HVRP is stronger during bull markets is robustly replicated in modern markets. In bull markets, event day AAR is 6.47% and 50-day CAR reaches 3.84%, while in bear markets these are 5.47% and 1.50%, respectively. The absolute effect size increased in both market conditions compared to the original study: bull markets increased approximately 14% (from 5.668% to 6.47%), and bear markets increased approximately 23% (from 4.443% to 5.47%).

Interestingly, the relative difference narrowed slightly: the original study showed a 1.225 percentage point difference between bull and bear markets (5.668%-4.443%), while our study shows 1.003 percentage points (6.47%-5.47%). This is because the effect size increase in bear markets (23%) exceeded that in bull markets (14%). Nevertheless, the differential effect by market condition remains robust, confirming that the original study’s core finding remains valid in modern markets.

The most striking divergence appears in the 50-day CAR: bull market CAR of 3.84% is more than 2.5 times the bear market CAR of 1.50%. This suggests that market psychology significantly moderates the informational content embedded in abnormal volume events, with bullish sentiment amplifying and sustaining the price impact of volume shocks.

![Refer to caption](car_plot_bull_market_conditions.png)


(a) Bull Market

![Refer to caption](car_plot_bear_market_conditions.png)


(b) Bear Market

Figure 2: Cumulative Abnormal Returns (CAR) by Market Condition

Figure [2](https://arxiv.org/html/2512.14134v1#S4.F2 "Figure 2 ‣ 1 Market Condition Effects: Bull vs. Bear Markets ‣ H Modern Market Phenomena: COVID-19 and Donghak Ant Movement ‣ IV Empirical Results ‣ Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)") visually demonstrates the stark difference in CAR patterns by market condition. In bull markets (panel a), CAR rises continuously after the event day, reaching 3.835% by day +50. In bear markets (panel b), the increase is relatively limited, reaching only 1.503%. This clearly illustrates the moderating effect of market psychology on the informational value of abnormal trading volume.

#### 2 Period Justification

Our analysis focuses on two critical modern market phenomena: the COVID-19 shock and the Donghak Ant Movement. Precise period definition is crucial for isolating the effects of these distinct market regimes. Table [13](https://arxiv.org/html/2512.14134v1#S4.T13 "Table 13 ‣ 2 Period Justification ‣ H Modern Market Phenomena: COVID-19 and Donghak Ant Movement ‣ IV Empirical Results ‣ Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)") summarizes our period definitions and their justifications.

Table 13: Period Justification Summary

| Period Definition | Dates | Core Rationale |
| --- | --- | --- |
| COVID-19 Shock Start | 2020.02.01 | Systemic risk transmission beginning in Korea, synchronization with global markets, onset of structural deterioration in investment psychology |
| COVID-19 Shock End | 2020.04.30 | V-KOSPI volatility normalization, alignment with 10.1093/rapstu/raaa008 analysis endpoint, distinction from subsequent liquidity-driven rally |
| Donghak Ant Start | 2020.03.01 | Large-scale retail buyback responding to foreign investor selloff, manifestation of collective action |
| Donghak Ant End | 2021.12.31 | Policy rate increases (Aug/Nov 2021) deteriorating liquidity environment, retail investor shift to net selling, structural regime shift to ”Seohak” (U.S. market focus) |

COVID-19 Shock Period (February 1 - April 30, 2020):

While 10.1093/rapstu/raaa008 used February 24 as the start date for U.S. markets, we begin our COVID-19 shock period on February 1, 2020, to account for Korea’s earlier outbreak timing. Korea’s first confirmed case occurred on January 20, 2020, and the Daegu-Gyeongbuk outbreak (the epicenter of Korea’s COVID-19 first wave) in mid-February created systemic risk earlier than in U.S. markets. Financial markets pre-price real economy developments, and Korean market sentiment deteriorated sharply in early-mid February, preceding the U.S. market crash. Using February 24 would miss critical initial shock data specific to the Korean market context.

The end date of April 30, 2020, aligns with 10.1093/rapstu/raaa008’s methodology for international consistency. The V-KOSPI (Korea’s volatility index, analogous to the VIX in U.S. markets) reached historical peaks exceeding 60 points in March 2020 but fell below panic-selling thresholds by late April, indicating volatility normalization. This endpoint clearly distinguishes the collapse phase (February-April) from the subsequent V-shaped recovery and liquidity rally (May onward).

Donghak Ant Movement Period (March 1, 2020 - December 31, 2021):

We define the Donghak Ant Movement period as March 2020 through December 2021. The term ”Donghak Ants” references the 1894 Donghak Peasant Rebellion, representing retail investors’ collective defense against foreign capital flight during the March 2020 market crash (ART002752798). March 2020 marked the transformation of retail investors from passive participants to active market defenders through massive net buying that absorbed foreign institutional selling pressure. While retail buying occurred in January-February 2020, March represented the organized, collective movement.

The period ends in December 2021 due to three structural shifts. First, the Bank of Korea raised policy rates from 0.50% to 0.75% in August 2021 and to 1.00% in November 2021, ending the ultra-low interest rate environment that had fueled the movement and increasing margin loan costs. Second, retail investors executed a structural reversal to massive net selling, including a record 3+ trillion won single-day selloff on December 28, 2021. Third, investor focus shifted from domestic market defense (”Donghak”) to U.S. market opportunities (”Seohak Ants,” referring to retail investors who subsequently shifted their capital to U.S. markets in late 2021), as KOSPI stagnated near the 3,000 level while U.S. markets offered higher returns.

These period definitions capture inflection points where macroeconomic indicators (interest rates) and microeconomic trading data (retail net purchases) undergo structural changes, providing temporally precise boundaries optimized for HVRP research.

#### 3 COVID-19 Shock Analysis

During the COVID-19 shock period, HVRP exhibited significant amplification contrary to expectations of weakening during crises.

Table 14: COVID-19 Shock Period Event Study Results (Feb-Apr 2020)

|  |  |  |  |
| --- | --- | --- | --- |
| Event Day | AAR (%) | t-stat | CAR (%) |
| -25 | -0.34% | -3.65\*\*\* | -4.22% |
| -10 | -0.08% | -0.88 | -7.30% |
| -1 | 1.28% | 6.57\*\*\* | -5.02% |
| 0 | 6.31% | 20.62\*\*\* | 1.29% |
| 1 | -0.50% | -2.76\*\*\* | 0.79% |
| 10 | 0.13% | 0.98 | 0.72% |
| 25 | -0.21% | -1.63 | 0.67% |
| 50 | 0.13% | 1.09 | 3.12% |
| \*p¡0.10, \*\*p¡0.05, \*\*\*p¡0.01 | | | |
| --- | --- | --- | --- |

Three key patterns emerge: (1) Event day amplification: Day 0 AAR of 6.31% exceeds the full sample average of 6.15%, suggesting heightened information value during crises; (2) Enhanced long-term persistence: Day +50 CAR of 3.12% remains comparable to the full sample’s 3.09%, indicating HVRP persists even during crisis periods; (3) Pre-event information leakage: Day -1 AAR of 1.28% far exceeds the full sample’s 0.66%, indicating more active pre-trading during crisis uncertainty.

These results support Hypothesis 2a. As Ozik\_Sadka\_Shen\_2021 demonstrated, retail investors provided liquidity during institutional risk-averse selling, amplifying information signals embedded in abnormal volume. During crises when liquidity constraints intensify, abnormal volume events carry stronger informational content that is more powerfully reflected in prices.

#### 4 Donghak Ant Movement Analysis

The Donghak Ant Movement period reveals a remarkable transformation in retail investor behavior.

Table 15: Donghak Ant Movement Period: Retail-Led Events (Mar 2020-Dec 2021)

|  |  |  |  |
| --- | --- | --- | --- |
| Event Day | AAR (%) | t-stat | CAR (%) |
| -10 | -0.18% | -4.76\*\*\* | -6.40% |
| -1 | 0.93% | 13.15\*\*\* | -5.90% |
| 0 | 6.24% | 43.64\*\*\* | 0.34% |
| 1 | -0.08% | -0.86 | 0.26% |
| 10 | 0.05% | 0.90 | 0.52% |
| 25 | 0.06% | 1.07 | 1.72% |
| 50 | 0.11% | 1.77\* | 3.53% |
| \*p¡0.10, \*\*p¡0.05, \*\*\*p¡0.01 | | | |
| --- | --- | --- | --- |

Extraordinary Finding: During the Donghak period, retail-led events generated a day +50 CAR of 3.526%, compared to only 0.48% for the highest-intensity retail-led events (Q4) overall—a 7.3-fold increase. This represents a dramatic transformation from the inverted pattern observed in normal periods, strongly supporting Hypothesis 2b.

This finding parallels 10.1093/rfs/hhad098’s discovery that Reddit’s WallStreetBets possessed significant information value during the pre-GameStop period before deteriorating into noise after popularization. During the Donghak movement, social media coordination and collective intelligence temporarily transformed retail investors from ”noise traders” to meaningful market participants. The online community’s due diligence sharing and coordinated action created genuine information value, demonstrating that under specific conditions—collective organization through social media during market stress—retail trading can transcend behavioral biases to generate persistent returns.

Retail Investor Role Transformation During Donghak Period

The most striking discovery is the dramatic transformation of retail-led events’ characteristics across different periods. Table [16](https://arxiv.org/html/2512.14134v1#S4.T16 "Table 16 ‣ 4 Donghak Ant Movement Analysis ‣ H Modern Market Phenomena: COVID-19 and Donghak Ant Movement ‣ IV Empirical Results ‣ Sources and Nonlinearity of High Volume Return Premium: An Empirical Study on the Differential Effects of Investor Identity versus Trading Intensity (2020-2024)") presents a direct comparison.

Table 16: Retail-Led Event Comparison: Normal vs. Donghak Period

| Period | Day 0 AAR (%) | Day 50 CAR (%) | Characteristics |
| --- | --- | --- | --- |
| Full Period Retail-Led | 5.72 | 0.52 | Rapid decay after initial shock, limited persistence |
| Donghak Period Retail-Led | 6.25 | 3.75 | Strong persistence, institutional-level effects |

Under normal conditions, retail-led events show strong initial AAR of 5.72% on event day but rapidly decay to just 0.52% by day +50, confirming retail investors’ limited information processing capabilities. However, during the Donghak period (March 2020 - December 2021), retail-led events achieved 50-day CAR of 3.75%, comparable to institution-led (7.74%) and foreign-led (6.03%) events in terms of persistence patterns, though still lower in absolute magnitude.

This transformation can be attributed to three complementary mechanisms:

* •

  Collective Intelligence Effect: Online community platforms enabled information sharing and collective due diligence, improving retail investors’ information processing capabilities similar to Bradley et al.’s pre-GME WallStreetBets findings.
* •

  Self-fulfilling Prophecy: Coordinated massive buying pressure created genuine price impact that justified the initial volume signal.
* •

  Structural Market Change: Proliferation of mobile trading platforms and fintech accessibility fundamentally altered retail investor capabilities and market participation patterns.

Table 17: Summary: Impact of Special Market Periods

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Period | Day 0 AAR | Day 50 CAR | vs. Baseline | Interpretation |
| Overall Average | 6.15% | 3.12% | - | Baseline |
| Bull Market | 6.47% | 3.84% | +23% | Market condition effect |
| COVID-19 Shock | 6.79% | 4.09% | +31% | Information amplification |
| Donghak (All) | 6.25% | 3.53% | +13% | Collective action |
| Donghak (Retail) | 6.25% | 3.75% | +619%\* | Retail transformation |
| \*vs. retail-led normal period 0.52% | | | | |
| --- | --- | --- | --- | --- |

## V Discussion and Implications

### A Academic Contributions

Our study contributes to existing literature in five aspects:

First, transforming Ahn et al. (2005)’s ’inference’ into ’empirical evidence.’ We conducted the first empirical test of the ’investor type hypothesis’ proposed 20 years ago using actual data, confirming that investor identity fundamentally determines the persistence of abnormal returns following volume spikes.

Second, resolving the LVRP-HVRP puzzle in Korean markets. CHAE2019101204 documented that Korea exhibits a Low Volume Return Premium (LVRP)—the opposite of U.S. patterns. Our findings suggest this apparent contradiction arises from measurement issues: when volume is analyzed conditional on investor type and intensity is properly normalized, the relationship becomes clear. The LVRP finding may reflect pooling heterogeneous investor effects, where retail-led volume events (which predominate in Korea’s retail-dominated market) drag down aggregate returns. When decomposed by investor type, institution-led and foreign-led events exhibit strong positive returns consistent with the information hypothesis, while retail-led events show near-zero persistence. This reconciles Korean evidence with developed market patterns.

Third, resolving the intensity puzzle. Prior studies reported mixed or null findings on whether trading intensity predicts returns (Namouri26012018; https://doi.org/10.1111/jofi.13183; HAN20221295). We demonstrate that intensity matters profoundly, but only when: (1) analyzed conditional on investor type, (2) measured nonlinearly through quartile sorts, and (3) normalized by market capitalization rather than trading value. This methodological refinement reconciles decades of conflicting evidence.

Fourth, providing contemporary evidence for core finance debates. The result of retail-led CAR ≈\approx 0 contradicts https://doi.org/10.1111/j.1540-6261.2008.01316.x and https://doi.org/10.1111/jofi.13033 while supporting 10.1093/rfs/hhm079 and https://doi.org/10.1111/jofi.13183’s ’noise trader’ hypothesis. Moreover, the inverted monotonic pattern for retail investors provides unprecedented empirical clarity on systematic retail mistiming.

Fifth, identifying moderating effects of modern market shocks. Analysis of COVID-19 (31% HVRP amplification) and Donghak Ant Movement (7.2-fold increase in retail-led CAR) demonstrates how traditional anomalies transform under extreme conditions, with implications for understanding crisis-period trading behavior and social media coordination effects. This extends KWAK2024105027’s finding of attenuated volume-return relationships post-COVID by showing that attenuation varies dramatically by investor type.

### B Behavioral Finance Interpretation

Our findings can be interpreted through three behavioral finance mechanisms:

Attention-Based Trading: Consistent with 10.1093/rfs/hhm079, abnormal volume serves as an attention shock that attracts investors. However, the differential persistence by investor type reveals that attention alone does not explain returns—the quality of attention matters. Institutional attention reflects fundamental analysis, while retail attention often reflects speculative interest.

Herding Behavior and Collective Intelligence: The Donghak Ant Movement demonstrates that retail herding can occasionally generate information value. When social media coordination enables collective due diligence sharing and reduces individual behavioral biases through group wisdom, retail investors can temporarily transcend their typical noise-trading tendencies. However, this represents an exception rather than the rule, consistent with 10.1093/rfs/hhad098’s finding that online community information value deteriorates after initial success.

Information Processing Heterogeneity: The stark differences between institutional (CAR 7.74%), foreign (6.03%), and retail (0.52%) outcomes reflect fundamental differences in information processing capabilities. Institutions possess analytical resources, information networks, and professional training that enable them to identify and act on genuine value signals, while retail investors operate with limited resources and are susceptible to cognitive biases.

### C Nonlinearity and Measurement Sensitivity

The contrast between our methodologies reveals a critical insight into HVRP’s underlying mechanism. Our double-sort methodology (Method 1) uncovers strong monotonic patterns when using market cap normalization, while linear correlation analysis (Method 2) shows near-zero coefficients. This contrast demonstrates that the intensity-return relationship is nonlinear, type-dependent, and measurement-sensitive.

Both Identity AND Intensity Matter: Our findings refine prior understanding. Section 4.3 confirmed that investor identity (institutions vs. foreigners vs. retail) fundamentally matters. Section 4.4 then demonstrated that intensity also matters profoundly, but the relationship is nonlinear and only detectable with proper measurement. For institutions, the Q4-Q1 CAR spread is 10.12 percentage points (10.07% - (-0.05%)), economically large and highly significant. This refutes the simplistic interpretation that ”intensity doesn’t matter”—intensity matters enormously when measured as conviction (market cap normalization) rather than participation (trading value normalization).

Quartile Regimes vs. Linear Relationships: The monotonic pattern operates through discrete intensity quartiles rather than continuous linear effects. Within each quartile, there may be limited variation, but crossing from one quartile to the next predicts substantially different returns. This explains why Pearson correlation fails—it assumes linearity, which is inappropriate for relationships operating through ordered regimes with threshold effects between them.

Implications for Methodology: This finding has important methodological implications. Linear regression models assuming continuous relationships will underestimate or miss threshold effects entirely. Future research on investor behavior and market anomalies should consider event-based approaches, regime-switching models, or machine learning methods capable of capturing nonlinear relationships.

### D Practical Implications

From an investment strategy perspective, identifying ’who led’ rather than simply detecting volume spikes is crucial. Particularly, capturing abnormal volume led by institutions in mid-cap stocks can be the most effective alpha strategy. Additionally, the finding that information signals amplify during crisis situations provides rationale for active crisis response strategies.

The threshold effect implies that quantitative trading strategies should focus on binary signals (event occurrence) rather than continuous intensity measures. Monitoring which investor type drives volume spikes offers more predictive power than measuring the magnitude of their net purchases.

### E Policy Implications

Given the confirmed ’noise trading’ tendency of retail investors, investor education and information disclosure reforms are urgent. However, since retail investors can contribute to market efficiency under specific conditions like the Donghak Ant Movement, differentiated approaches by situation are needed rather than uniform regulation.

Policymakers should recognize that retail investor impact varies by context. During normal periods, retail investors require protection through education and transparency. During collective action periods with social media coordination, retail investors can play positive roles as liquidity providers and market stabilizers, suggesting that policies should enable beneficial coordination while preventing manipulation.

## VI Conclusion

This study resolves a longstanding puzzle in behavioral finance by demonstrating that both investor identity and trading intensity are critical determinants of the High Volume Return Premium—but only when intensity is measured correctly. Our central contribution is methodological: we are the first to show that the choice between normalizing trading intensity by market capitalization versus trading value is not a technical detail but a fundamental determinant of whether researchers detect informed trading signals.

The Core Discovery: Measurement Matters

Our double-sort methodology reveals a striking pattern. When we normalize institutional buying intensity by market capitalization (a proxy for conviction), a perfect monotonic relationship emerges: events in the highest conviction quartile (Q4) generate +10.07% cumulative abnormal returns over 50 days, while the lowest quartile (Q1, net selling) yields near-zero returns (-0.05%). In sharp contrast, normalizing by daily trading value produces a broken monotonic pattern where Q3 (+12.33%) exceeds Q4 (+4.22%). This horse race comparison definitively demonstrates that market cap normalization captures the true economic relationship between informed trading and future returns.

Reconciling Conflicting Evidence

This finding reconciles decades of conflicting evidence. Prior studies reported weak or insignificant linear correlations between trading intensity and returns (Namouri26012018; https://doi.org/10.1111/jofi.13183), leading some researchers to conclude that intensity is irrelevant—that ”who” matters but ”how much” does not. Our results demonstrate this conclusion was premature. The near-zero correlation we observe with the Dominance Score (r¡0.04, p¿0.16) does not indicate that intensity is irrelevant; it reveals that the relationship is nonlinear and type-dependent. Simple linear models fail because they cannot capture threshold effects and investor heterogeneity.

When we decompose events by investor type and measure conviction correctly, intensity emerges as a powerful predictor. The Q4-Q1 spread for institutions is 10.12 percentage points (10.07% - (-0.05%)), economically large and statistically robust. This demonstrates that institutional conviction, measured as position size relative to firm value, contains substantial predictive power that prior methodologies failed to detect.

Investor Identity Remains Critical

While our main contribution concerns intensity measurement, we also confirm that investor identity fundamentally matters. Institution-led and foreign-led events generate persistent long-term returns (Day +50 CAR: 7.74% and 6.03%), while retail-led events rapidly dissipate (CAR: 0.52%). Moreover, the market cap normalization reveals an inverted monotonic pattern for retail investors: their highest conviction buying predicts the weakest returns, confirming the noise trader hypothesis (10.1093/rfs/hhm079; https://doi.org/10.1111/jofi.13183) with unprecedented clarity. This heterogeneity validates our double-sort approach—intensity effects operate differently across investor types.

Modern Market Context

Our analysis of COVID-19 and the Donghak Ant Movement demonstrates that these core relationships can transform under extreme conditions. During the COVID-19 shock, HVRP amplified to 4.09% (31% premium over baseline), suggesting that information asymmetry intensifies during crises. During the Donghak Ant Movement, retail-led events generated 3.75% returns (7.2-fold increase over normal periods), indicating that collective action through social media temporarily transformed retail investors into meaningful market participants, paralleling 10.1093/rfs/hhad098’s findings on WallStreetBets.

Implications for Future Research

Our findings carry important methodological implications. Researchers studying informed trading must: (1) account for investor heterogeneity rather than using pooled analyses; (2) employ nonlinear methods (quartile sorts, threshold regressions) rather than linear correlation; and (3) normalize trading activity by economically meaningful benchmarks (firm size) rather than daily flow measures. The failure to do so may explain why some prior studies found weak or inconsistent results.

For practitioners, the monotonic conviction-return relationship provides actionable signals. Abnormal volume events where institutions take large positions relative to firm size (high Q4 conviction) predict substantial outperformance (+10.07% over 50 days), while events dominated by retail high-conviction buying predict underperformance. The ability to distinguish information from noise—and measure conviction correctly—remains a core competency in modern markets.

Final Reflection

Twenty years after ART001162590 proposed the investor type hypothesis as an untested conjecture, we provide the first comprehensive empirical test using actual investor-level data. The HVRP phenomenon persists robustly in modern markets, but its drivers are more nuanced than previously understood. Both ”who” trades (identity) and ”how much” they trade (intensity) matter profoundly, but detecting the intensity effect requires proper measurement. This study transforms the narrative from ”identity matters, intensity doesn’t” to ”identity matters, and intensity matters enormously when measured as conviction rather than participation.” This refined understanding advances our knowledge of how information flows through markets and how different investor types process and act on that information.

## Appendix A Appendix A: Full Sample Replication

This appendix presents a comprehensive comparison between the original ART001162590 study (2001-2003) and our re-examination (2020-2024) using all 26,604 abnormal volume events, verifying whether the HVRP phenomenon persists despite the 20-year gap and market structural changes.

Table 18: Full Sample Event Study Results: 2003 Original Study vs 2024 Re-examination (Extended)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Original Study (2001-2003) | | | This Study (2020-2024) | | |
| Event Day | AAR(%) | t-stat | CAR(%) | AAR(%) | t-stat | CAR(%) |
| -25 | -0.361\*\*\* | -3.24 | -1.820 | -0.13%\*\*\* | -7.52 | -2.09% |
| -10 | -0.097 | -1.45 | -4.454 | -0.10%\*\*\* | -6.93 | -4.46% |
| -5 | -0.082 | -1.35 | -3.748 | -0.07%\*\*\* | -5.12 | -4.93% |
| -2 | 0.418\*\*\* | 6.92 | -3.441 | 0.14%\*\*\* | 8.28 | -4.75% |
| -1 | 2.454\*\*\* | 40.62 | -0.987 | 0.66%\*\*\* | 28.87 | -4.09% |
| 0 | 5.056\*\*\* | 83.66 | 4.068 | 6.15%\*\*\* | 118.81 | 2.06% |
| 1 | -0.200 | -3.31 | 3.869 | 0.09%\*\*\* | 2.72 | 2.15% |
| 2 | -0.126 | -2.08 | 3.743 | -0.00% | -0.18 | 2.15% |
| 5 | -0.043 | -0.71 | 3.598 | -0.05%\*\* | -2.34 | 2.19% |
| 10 | -0.006 | -0.10 | 3.779 | 0.01% | 0.28 | 2.33% |
| 25 | 0.195\*\* | 3.22 | 4.268 | 0.03% | 1.28 | 2.71% |
| 50 | -0.107 | -1.77 | 3.672 | 0.02% | 1.01 | 3.09% |
| \*p¡0.10, \*\*p¡0.05, \*\*\*p¡0.01 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Key Findings: Phenomenon Persistence and Amplification

(1) Robust Replication of HVRP: The core pattern discovered in the original study appears identically in the 2020-2024 period. The fundamental structure—persistent negative CAR before the event day, sharp positive AAR on event day 0, followed by sustained positive levels—is fully replicated.

(2) Significant Increase in Effect Size: Remarkably, HVRP magnitude has expanded in modern markets. Event day AAR increased from 5.056% to 6.153% (approximately 22% increase), and day +50 CAR remained strong at 3.122% (compared to 3.672% in original study).

(3) Enhanced Statistical Significance: With a much larger sample size (original: 1,360 events → this study: 26,604 events), statistical significance strengthened substantially across most periods. Event day t-statistic increased from 83.66 to 118.877, enhancing confidence in the phenomenon.

(4) Pre-Event Pattern Changes: Interestingly, the pre-event pattern differs. The original study showed strong positive return on day -1 (2.454%), while our study shows this effect distributed across days -2 (0.489%) and -1 (0.661%). This suggests faster information diffusion in modern markets leads to more dispersed investor reactions.

Theoretical Consistency: These results confirm that ART001162590’s interpretation remains valid 20 years later: abnormal volume increases result from informed investors’ pre-trading, serving as signals of price increases, with post-event positive abnormal returns reflecting gradual information incorporation. The amplified effects may relate to modern market characteristics including expanded information asymmetry (despite big data/AI advances, the gap between professional and retail investors has widened), amplified behavioral biases (social media and online communities accelerate herding and overreaction), and increased market volatility (ADTV standard deviation surged from 0.935 to 8.292).

## Appendix B Appendix B: Firm Size Analysis

The original study’s key finding was that HVRP appears stronger in large firms. We replicate this analysis using official Korea Exchange classification: large-cap (ranks 1-100), mid-cap (ranks 101-300), and small-cap (rank 300+) based on market capitalization on event day.

Table 19: Event Study Results by Firm Size (Official Classification)

|  | Large-cap (1-100) | | | Mid-cap (101-300) | | | Small-cap (300+) | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Day | AAR | t-stat | CAR | AAR | t-stat | CAR | AAR | t-stat | CAR |
| -20 | -0.18 | -2.00\*\* | -3.15 | -0.13 | -2.19\*\* | -1.99 | -0.21 | -13.95\*\*\* | -2.98 |
| -10 | -0.10 | -1.04 | -3.51 | -0.06 | -1.15 | -2.91 | -0.10 | -6.78\*\*\* | -4.56 |
| -1 | 0.73 | 4.86\*\*\* | -1.94 | 0.81 | 7.85\*\*\* | -1.86 | 0.65 | 27.48\*\*\* | -4.24 |
| 0 | 4.41 | 10.79\*\*\* | 2.47 | 6.06 | 25.19\*\*\* | 4.21 | 6.20 | 115.99\*\*\* | 1.95 |
| 1 | -0.30 | -1.62 | 2.17 | -0.03 | -0.27 | 4.17 | 0.10 | 2.99\*\*\* | 2.05 |
| 10 | -0.07 | -0.57 | 2.18 | -0.02 | -0.23 | 3.99 | 0.01 | 0.53 | 2.26 |
| 25 | -0.10 | -0.81 | 2.38 | 0.03 | 0.35 | 3.73 | 0.03 | 1.24 | 2.68 |
| 50 | -0.01 | -0.04 | 1.43 | 0.16 | 1.98\*\* | 4.00 | 0.01 | 0.55 | 3.10 |

Key Discovery: Mid-Cap Dominance

Using the three-way classification, we find the strongest HVRP in mid-cap stocks. Event day AAR shows mid-cap 6.06%, small-cap 6.20%, large-cap 4.41%; day +50 CAR shows mid-cap 4.00%, small-cap 3.10%, large-cap 1.43%. This ”mid-cap ¿ small-cap ¿ large-cap” structure differs from the original study’s ”large ¿ small” pattern.

This shift likely reflects 20 years of market structural changes and the introduction of three-way classification. Mid-cap stocks occupy an optimal position—receiving institutional attention while maintaining sufficient liquidity. Large-cap stocks face information transparency reducing information asymmetry effects, while small-cap stocks suffer liquidity constraints limiting long-term return persistence.

## Appendix C Appendix C: Market Comparison (KOSPI vs KOSDAQ)

While the original study focused solely on KOSPI, we extend analysis to KOSDAQ. Differences between the two markets provide important insights into HVRP’s structural characteristics.

Table 20: Event Study Results by Market: KOSPI vs KOSDAQ

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | KOSPI | | | KOSDAQ | | |
| Event Day | AAR (%) | t-stat | CAR (%) | AAR (%) | t-stat | CAR (%) |
| -25 | -0.10% | -3.70\*\*\* | -1.66% | -0.14% | -6.56\*\*\* | -2.32% |
| -10 | -0.07% | -3.52\*\*\* | -3.42% | -0.11% | -5.98\*\*\* | -5.02% |
| -1 | 0.58% | 16.45\*\*\* | -2.83% | 0.70% | 23.75\*\*\* | -4.77% |
| 0 | 5.51% | 65.51\*\*\* | 2.68% | 6.50% | 99.36\*\*\* | 1.73% |
| 1 | 0.06% | 1.06 | 2.74% | 0.10% | 2.60\*\*\* | 1.83% |
| 10 | -0.02% | -0.74 | 2.78% | 0.02% | 0.79 | 2.08% |
| 25 | 0.02% | 0.56 | 3.22% | 0.03% | 1.15 | 2.43% |
| 50 | 0.07% | 2.18\*\* | 3.67% | -0.01% | -0.25 | 2.78% |
| \*p¡0.10, \*\*p¡0.05, \*\*\*p¡0.01 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Key Market Differences:

(1) Initial Effect Differences: KOSDAQ shows stronger event day AAR (6.50% vs 5.51%), but KOSPI demonstrates stronger long-term persistence (3.67% vs 2.78%).

(2) Information Leakage Patterns: KOSDAQ exhibits higher day -1 AAR (0.70% vs 0.58%), suggesting faster information diffusion.

(3) Statistical Significance: KOSDAQ shows statistical significance across more periods, reflecting the higher responsiveness of this small-and-mid-cap-focused market.

These differences reflect structural characteristics: KOSPI shows stable, persistent patterns centered on large-caps, while KOSDAQ shows rapid but limited response patterns centered on small-and-mid-caps.